"""
!!! ABANDONED -- DOES NOT WORK. DO NOT BUILD ON THIS FILE. !!!

Kept for the record only. The Q-ball profile solver in this module is WRONG:
it returns solitons roughly TEN TIMES too large. Measured half-max radius is
17-22 across omega = 0.55..0.92, against an expected tail decay length of
1.2-2.6 (e^{-sqrt(1-omega^2) r}). The "solitons" do not fit in any practical
box, so at every separation they are one smeared blob rather than two objects.

CONSEQUENCE: every population, charge, gate and overlap result produced with
this module is INVALID -- the 0.50/0.50 populations were geometry, not physics.
The phase results (single-soliton advance measured at exactly +0.7000 against
nominal omega = 0.7; relative precession matching detuning to 0.4%) are
probably sound, because phase does not depend on the object being compact, but
they have NOT been re-verified against a correct profile.

CAUSE: the bisection converges to the critical rho_0 from below, and just below
critical the solution lingers on a plateau for a very long radius before
turning over -- classic separatrix behaviour. Three different shooting
formulations were tried; each failed differently. Shooting is the wrong tool.

FIX, NOT ATTEMPTED: scipy.integrate.solve_bvp, imposing rho'(0)=0 and
rho(inf)=0 directly and relaxing onto the solution, instead of hunting a
separatrix by bisection.

WHAT IS STILL GOOD HERE: the analytic parts, which were verified independently.
omega_min^2 = 1 - 3/(16 sigma) (Q-balls require sigma >= 3/16) and the stability
window 3/16 < sigma <= 1/4 are correct and are used by the working emulator.

For a qubit emulator that WORKS, see teotl_rotor_qc.py.
"""

"""
teotl_substrate — lattice complex field with a FUNDAMENTAL sextic, supporting
Q-ball solitons usable as qubit basis states.

Purpose (Vic, 2026-09-01): a substrate for a qubit emulator. This is NOT an
attempt to derive sigma from anything — sigma is a MODEL PARAMETER, chosen so
the solitons we need actually exist and are stable.

    V(rho) = 1/2 rho^2 - 1/4 rho^4 + (sigma/6) rho^6      [fundamental sextic]

Why the defaults are what they are (from the TFT-Classical floor studies):
  * Q-balls require  omega_min^2 = 1 - 3/(16 sigma) >= 0   ->  sigma >= 3/16   [FISS0]
  * the whole Q-ball family is fission-stable by sigma ~ 0.24 (fraction 1.00);
    at sigma = 0.20 only ~0.67 of the branch is                              [FISS0]
  * so SIGMA_DEFAULT = 0.24 sits inside 3/16 < sigma <= 1/4 with full stability.

2D lattice by choice: Q-balls exist in 2D (E = E_grad + lam^2 E_V + lam^-2 E_Q
has a genuine minimum) and it is ~100x cheaper to evolve than 3D, which matters
for an emulator. The physics of the qubit does not need the third dimension.

Phase arithmetic routes through teotl_math so the branch cut is handled in one
place (that module exists precisely for this).
"""
import numpy as np
import teotl_math as tm

SIGMA_DEFAULT = 0.24


def omega_min(sigma=SIGMA_DEFAULT):
    """Lowest Q-ball frequency. Below this no Q-ball exists."""
    val = 1.0 - 3.0 / (16.0 * sigma)
    if val < 0:
        raise ValueError(f"sigma={sigma} < 3/16: no Q-ball exists (FISS0)")
    return np.sqrt(val)


def V(rho, sigma=SIGMA_DEFAULT):
    return 0.5*rho**2 - 0.25*rho**4 + (sigma/6.0)*rho**6


def dV(rho, sigma=SIGMA_DEFAULT):
    return rho - rho**3 + sigma*rho**5


class Substrate:
    """2D lattice complex field psi = rho e^{i theta} with a fundamental sextic."""

    def __init__(self, N=128, L=40.0, sigma=SIGMA_DEFAULT):
        if sigma <= 3/16:
            raise ValueError(f"sigma={sigma} must exceed 3/16 for Q-balls (FISS0)")
        self.N, self.L, self.sigma = N, L, sigma
        self.dx = L / N
        x = (np.arange(N) - N//2) * self.dx
        self.X, self.Y = np.meshgrid(x, x, indexing="ij")
        self.psi = np.zeros((N, N), complex)
        self.psi_t = np.zeros((N, N), complex)
        self.V_ext = np.zeros((N, N))          # external trap (gate control)

    def set_trap(self, barrier=0.0, tilt=0.0, width=3.0):
        """External potential added to the field equation.

        barrier : height of a Gaussian wall at x=0. HIGH barrier isolates the
                  basins (no charge exchange); LOW barrier opens tunnelling.
                  This is the X / Rabi knob.
        tilt    : linear ramp in x. Makes one basin deeper than the other, i.e.
                  a detuning. This is the Z / phase knob.
        """
        # tanh, not a linear ramp: a ramp over the whole box reaches |tilt|*L/2,
        # which dwarfs V and shreds the solitons. tanh saturates at +-tilt, so it
        # is a bounded ASYMMETRY between the two basins, which is what we want.
        self.V_ext = (barrier*np.exp(-self.X**2/(2*width**2))
                      + tilt*np.tanh(self.X/width))
        return self

    # ---- construction -------------------------------------------------
    def qball_profile(self, omega, rmax=30.0, n=4000):
        """TRUE 2D radial Q-ball profile by shooting on
              rho'' + (1/r) rho' = dV/drho - omega^2 rho.

        A sech ansatz is NOT a solution: it breathes and the frequency drifts off
        nominal, which breaks phase gates.

        Mechanical analogy: a particle released at rest at rho_0, rolling in -W
        with W = V - omega^2 rho^2/2, must asymptote to the hilltop at rho=0.
        It needs W(rho_0) < 0, which holds only BETWEEN the two positive roots of
        W -- not on (0, rho_e). Within that band the failure modes are:
          * rho_0 too small -> friction wins, rho turns around before reaching 0
          * rho_0 too large -> runaway growth
        Neither mode crosses zero, so the classifier tests for RUNAWAY, not sign."""
        from scipy.integrate import solve_ivp
        W  = lambda x: V(x, self.sigma) - 0.5*omega**2*x**2
        xs = np.linspace(1e-6, 12, 400000); neg = np.where(W(xs) < 0)[0]
        if len(neg) == 0:
            raise RuntimeError(f"no W<0 band at omega={omega}: no Q-ball")
        lo_root, hi_root = xs[neg[0]], xs[neg[-1]]

        def rhs(r, y):
            return [y[1], dV(y[0], self.sigma) - omega**2*y[0] - y[1]/max(r, 1e-9)]

        def runs_away(rho0):
            s = solve_ivp(rhs, [1e-6, rmax], [rho0, 0.0], rtol=1e-10, atol=1e-12,
                          dense_output=True, max_step=0.05)
            return (s.y[0].max() > 1.5*rho0) or (not np.isfinite(s.y[0]).all()), s

        lo, hi = lo_root*1.001, None
        for cand in np.linspace(lo_root*1.001, hi_root*0.999, 200):
            if runs_away(cand)[0]:
                hi = cand; break
        if hi is None:
            raise RuntimeError(f"no runaway found in the W<0 band at omega={omega}")
        for _ in range(80):
            mid = 0.5*(lo+hi)
            if runs_away(mid)[0]: hi = mid
            else:                 lo = mid
        rho0 = lo                                  # last non-runaway
        sol = runs_away(rho0)[1]
        r = np.linspace(1e-6, rmax, n)
        prof = np.clip(sol.sol(r)[0], 0.0, None)
        z = np.where(prof < 1e-5)[0]               # truncate past the first zero
        if len(z): prof[z[0]:] = 0.0
        return r, prof

    def add_qball(self, x0=0.0, y0=0.0, omega=0.7, R=None):
        """Place a TRUE Q-ball (solved profile). omega must lie in (omega_min, 1)."""
        om_lo = omega_min(self.sigma)
        if not (om_lo < omega < 1.0):
            raise ValueError(f"omega={omega} outside ({om_lo:.4f}, 1.0)")
        r, prof = self.qball_profile(omega)
        rr = np.hypot(self.X - x0, self.Y - y0)
        field = np.interp(rr, r, prof, left=prof[0], right=0.0)
        self.psi   += field.astype(complex)
        self.psi_t += 1j*omega*field
        return self

    # ---- dynamics -----------------------------------------------------
    def _accel(self, psi):
        lap = (np.roll(psi, 1, 0) + np.roll(psi, -1, 0) +
               np.roll(psi, 1, 1) + np.roll(psi, -1, 1) - 4*psi) / self.dx**2
        rho = np.abs(psi)
        safe = np.where(rho > 1e-12, rho, 1.0)
        return lap - (dV(safe, self.sigma)/safe) * psi - self.V_ext * psi

    def step(self, dt):
        """Leapfrog: conservative, and preserves the U(1) charge exactly."""
        self.psi_t += 0.5*dt*self._accel(self.psi)
        self.psi   += dt*self.psi_t
        self.psi_t += 0.5*dt*self._accel(self.psi)

    def run(self, steps, dt=0.01):
        for _ in range(steps):
            self.step(dt)
        return self

    # ---- observables --------------------------------------------------
    def charge(self):
        return float(np.sum(np.imag(np.conj(self.psi)*self.psi_t)) * self.dx**2)

    def energy(self):
        gx = (np.roll(self.psi, -1, 0) - np.roll(self.psi, 1, 0)) / (2*self.dx)
        gy = (np.roll(self.psi, -1, 1) - np.roll(self.psi, 1, 1)) / (2*self.dx)
        dens = (np.abs(self.psi_t)**2 + np.abs(gx)**2 + np.abs(gy)**2
                + 2*V(np.abs(self.psi), self.sigma)
                + 2*self.V_ext*np.abs(self.psi)**2)
        return float(0.5*np.sum(dens) * self.dx**2)

    def charge_in_halfplane(self, sign=+1):
        """Charge on one side of x=0 — the qubit's population readout."""
        m = (self.X*sign) > 0
        return float(np.sum(np.imag(np.conj(self.psi)*self.psi_t)[m]) * self.dx**2)

    def mean_phase(self, x0, y0, R=4.0):
        """Circular-mean phase in a disc, via teotl_math (branch-cut safe)."""
        m = np.hypot(self.X-x0, self.Y-y0) < R
        return float(tm.circular_mean(np.angle(self.psi[m]),
                                      weights=np.abs(self.psi[m])**2))


class SubstrateQubit:
    """Two Q-balls in separate basins. |0> = charge left, |1> = charge right.

    Field-theoretic counterpart of teotl_qc.TeotlQubit, whose basins are
    point-node clusters rather than solitons.

    OPERATING NOTE (measured 2026-09-01, not assumed)
    ------------------------------------------------
    The two Q-balls couple through their overlapping tails, so the pair behaves
    as two coupled oscillators and PHASE-LOCKS below a separation threshold.
    Measured relative-phase advance vs the detuning (om1-om0):

        sep=14, detuning 0.16  ->  measured -0.070   LOCKED (coupling too strong)
        sep=20, detuning 0.16  ->  measured  0.1593  free precession, 0.4% error
        sep=28, detuning 0.40  ->  measured  0.4457  free precession, ~11% error

    sep=20 is therefore the default: far enough to precess freely, close enough
    that the coupling is still available for a two-qubit gate. Locking is real
    physics (an Arnold tongue), not a numerical artefact -- it is the knob you
    would use to turn interaction on and off.
    """

    def __init__(self, sep=20.0, omega0=0.7, omega1=0.7, N=180, L=64.0,
                 sigma=SIGMA_DEFAULT):
        self.sub = Substrate(N=N, L=L, sigma=sigma)
        self.sep = sep
        self.sub.add_qball(-sep/2, 0.0, omega=omega0)
        self.sub.add_qball(+sep/2, 0.0, omega=omega1)
        self._barrier = 0.0

    def populations(self):
        qL = abs(self.sub.charge_in_halfplane(-1))
        qR = abs(self.sub.charge_in_halfplane(+1))
        tot = qL + qR
        return (qL/tot, qR/tot) if tot > 0 else (0.5, 0.5)

    def relative_phase(self):
        a = self.sub.mean_phase(-self.sep/2, 0.0)
        b = self.sub.mean_phase(+self.sep/2, 0.0)
        return tm.wrap_to_pi(b - a)

    def run(self, steps, dt=0.01):
        self.sub.run(steps, dt); return self

    # ---- gate operations ---------------------------------------------
    # Both gates are CALIBRATED, not assumed: rabi_frequency() and
    # phase_rate() measure the machine's response, and the gate methods
    # solve for the time needed. Nothing here hard-codes a rate.

    def measure(self):
        """Population readout: (P0, P1) = normalised charge left/right."""
        return self.populations()

    def phase_rate(self, tilt, probe_steps=400, dt=0.01):
        """Measured d(relative phase)/dt at a given tilt. Non-destructive:
        runs on a copy so the qubit state is not disturbed."""
        import copy
        c = copy.deepcopy(self)
        c.sub.set_trap(barrier=self._barrier, tilt=tilt)
        ph = []
        for _ in range(5):
            c.run(probe_steps//5, dt); ph.append(c.relative_phase())
        return float(np.mean(np.diff(np.unwrap(ph)))) / (probe_steps//5 * dt)

    def rz(self, phi, tilt=0.15, dt=0.01):
        """Z-rotation by phi: tilt the trap, wait, restore."""
        rate = self.phase_rate(tilt, dt=dt)
        if abs(rate) < 1e-9:
            raise RuntimeError("no measurable phase rate at this tilt")
        steps = int(round(abs(phi/rate)/dt))
        self.sub.set_trap(barrier=self._barrier, tilt=np.sign(phi)*abs(tilt)*np.sign(rate))
        self.run(steps, dt)
        self.sub.set_trap(barrier=self._barrier, tilt=0.0)
        return self

    def rabi_period(self, barrier, max_steps=6000, dt=0.01):
        """Measure the population-oscillation period at a given barrier."""
        import copy
        c = copy.deepcopy(self)
        c.sub.set_trap(barrier=barrier, tilt=0.0)
        p0 = c.populations()[0]; series=[p0]
        for _ in range(max_steps//50):
            c.run(50, dt); series.append(c.populations()[0])
        s = np.array(series) - np.mean(series)
        if np.max(np.abs(s)) < 1e-3:
            return None                     # no exchange: barrier too high
        f = np.fft.rfftfreq(len(s), d=50*dt)
        amp = np.abs(np.fft.rfft(s)); amp[0] = 0
        return float(1.0/f[np.argmax(amp)])

    # ---- resonance-gate layer ----------------------------------------
    # Architecture: the geometry is FIXED. Both gates are driven by the
    # DETUNING (the trap tilt), exploiting that coupled oscillators exchange
    # charge only when |detuning| < coupling J.
    #
    #   tilt != 0  -> detuned, coupling cannot bridge the gap
    #                 -> no charge exchange, phases precess     -> Rz
    #   tilt == 0  -> resonant, weak coupling still gives FULL
    #                 exchange, just slowly at rate ~J          -> Rx
    #
    # Measured basis: at sep=14 a detuning of 0.16 LOCKED the pair (so J>0.16
    # there); at sep=20 the same detuning precessed freely (J<0.16). Nonzero
    # but small -- which is exactly the regime this architecture wants.

    IDLE_TILT = 0.30          # park here between gates: detuned, no exchange

    def _clone(self):
        import copy
        return copy.deepcopy(self)

    def calibrate(self, force=False, dt=0.01):
        """Measure BOTH gate rates on this machine and cache them.

        Nothing downstream hard-codes a rate: the response depends on sigma,
        separation and the solved profiles, all of which have surprised us.
        """
        if getattr(self, "_cal", None) is not None and not force:
            return self._cal
        z_rate = self.phase_rate(self.IDLE_TILT, dt=dt)          # rad per unit time
        T = self.rabi_period(barrier=0.0, max_steps=8000, dt=dt) # at zero tilt
        x_rate = (2*np.pi/T) if T else None                      # rad per unit time
        self._cal = {"z_rate": z_rate, "rabi_period": T, "x_rate": x_rate}
        return self._cal

    def rz(self, phi, dt=0.01):
        """Z-rotation by phi. Detune (tilt on), wait, return to idle."""
        cal = self.calibrate(dt=dt)
        rate = cal["z_rate"]
        if abs(rate) < 1e-9:
            raise RuntimeError("no measurable phase rate; check IDLE_TILT")
        steps = int(round(abs(phi/rate)/dt))
        self.sub.set_trap(barrier=0.0, tilt=np.sign(phi/rate)*self.IDLE_TILT)
        self.run(steps, dt)
        self.park()
        return self

    def rx(self, theta, dt=0.01):
        """X-rotation by theta. Drop to RESONANCE (tilt 0), wait, re-detune."""
        cal = self.calibrate(dt=dt)
        if cal["x_rate"] is None:
            raise RuntimeError("no charge exchange at resonance: coupling too "
                               "weak at this separation, or probe too short")
        steps = int(round(abs(theta/cal["x_rate"])/dt))
        self.sub.set_trap(barrier=0.0, tilt=0.0)          # resonant
        self.run(steps, dt)
        self.park()
        return self

    def park(self):
        """Idle: detuned, so the qubit holds its state without exchanging."""
        self.sub.set_trap(barrier=0.0, tilt=self.IDLE_TILT)
        return self

    def prepare_biased(self, steps=300, dt=0.01, tilt=0.8):
        """Localise charge toward one basin, so Rabi has something to move."""
        self.sub.set_trap(barrier=0.0, tilt=tilt)
        self.run(steps, dt)
        self.park()
        return self
