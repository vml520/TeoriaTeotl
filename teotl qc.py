"""
Teotl QC v0.3 — Madelung kernel, conservative complex field
───────────────────────────────────────────────────────────────────────────────
Framework: TFT-Classical conservative regime (2026-07-05).
Regime: ψ = ρ e^{iθ}, second-order conservative field.  NOT the dissipative
Kuramoto/rectified regime — that regime failed to produce stable localized
particles and is retired here.

A qubit is two node basins in R³, each internally phase-coherent:

    ψ_k  = sqrt(m_k) · exp(i·θ̄_k)     k ∈ {0,1}
    P(1) = m₁ / (m₀ + m₁)
    φ    = θ̄₁ − θ̄₀
    Q    = Σ_i m_i · ω_i               (U(1) Noether charge proxy)

One kernel — Madelung (DERIVED, conservative):
    θ̇_i = ω_i + g Σ_j S[i,j]·√(m_j/m_i)·cos(θ_j−θ_i)
    ṁ_i = −2g Σ_j S[i,j]·√(m_i·m_j)·sin(θ_j−θ_i)
    S symmetric → pairwise-antisymmetric flow → total mass conserved.
    This is exactly discrete Schrödinger (ψ_i = √m_i e^{iθ_i}, H = ω − gS).

Three preparation methods:
    prepare(state)       — asymmetric mass, random phases (standard qubit init)
    prepare_qball(state, omega) — coherent phase, uniform ω (U(1)-charged state)
    prepare_vortex(basin)       — arctan2 phase texture; seeds a topological defect

Epistemic labels:
    DERIVED  — Madelung kernel from conservative TFT field equations.
    DERIVED  — Winding readout: meaningful in broken-symmetry (ρ=v) regime.
    OPEN     — Whether Kernel B is derivable from the TFT action; Born statistics;
               CHSH S > 2.
    RETIRED  — Rectified / Kuramoto kernel: dissipative regime, failed for physics.
───────────────────────────────────────────────────────────────────────────────
"""

import numpy as np
from teotl_math import wrap_theta, wrap_to_pi, winding_density_2d, circular_mean

# ── First-class scales ────────────────────────────────────────────────────────
E_0, l_0 = 1.0, 1.0
XI        = 3.0 * l_0
SIGMA     = l_0
DIST_EPS  = 1e-6
MASS_EPS  = 1e-9

K_PER_BASIN  = 16
BASIN_SEP    = 2.0 * l_0
BASIN_RADIUS = 0.4 * l_0


class TeotlQubit:
    def __init__(self, detuning=0.0, kernel="madelung",
                 g=0.05, beta=0.0, phase_noise=0.0, seed=42,
                 Lambda=0.0, v_sq=None):
        if kernel != "madelung":
            raise ValueError(
                f"kernel={kernel!r} is retired. Only 'madelung' (conservative "
                "complex field) is supported. See §0 of the TFT-Classical framework."
            )
        self.rng         = np.random.default_rng(seed)
        self.kernel      = kernel
        self.g           = g
        self.beta        = beta
        self.phase_noise = phase_noise
        self.Lambda      = Lambda
        self.N           = 2 * K_PER_BASIN
        self.basin       = np.array([0]*K_PER_BASIN + [1]*K_PER_BASIN)

        # v_sq = ρ² at the broken-symmetry vacuum (Mexican hat minimum).
        # Default: 1/N so that uniform mass m_i=v_sq has Σm_i=1 and the
        # potential term -2Λ(m_i-v_sq) sums to zero → total mass conserved.
        self.v_sq = v_sq if v_sq is not None else 1.0 / (2 * K_PER_BASIN)

        pos = np.zeros((self.N, 3))
        for k in range(self.N):
            c = np.array([(-1 if self.basin[k] == 0 else 1)*BASIN_SEP/2, 0, 0])
            pos[k] = c + self.rng.normal(0, BASIN_RADIUS/2, 3)
        self.pos = pos

        self.omega = np.where(self.basin == 0, -detuning/2, +detuning/2).astype(float)
        self.theta = self.rng.uniform(0, 2*np.pi, self.N)
        self.mass  = np.ones(self.N) / self.N

        self._S_intra = self._build_S(0.0)
        self._S_full  = self._build_S(1.0)
        self.set_bridge(0.0)

    def _build_S(self, bridge_amp):
        """Symmetric Gaussian coupling, cutoff XI, cross-basin scaled by bridge."""
        d = np.linalg.norm(self.pos[None,:,:] - self.pos[:,None,:], axis=2)
        S = np.where((d < XI) & (d > DIST_EPS), np.exp(-d**2/(2*SIGMA**2)), 0.0)
        cross = self.basin[None,:] != self.basin[:,None]
        S = np.where(cross, S*bridge_amp, S)
        return S

    def set_bridge(self, amp):
        self.bridge_amp = amp
        if   amp <= 0.0: self.S = self._S_intra
        elif amp >= 1.0: self.S = self._S_full
        else:            self.S = self._build_S(amp)
        rs = self.S.sum(axis=1, keepdims=True) + 1e-12
        self.W = self.S / rs  # row-normalised (retained for legacy callers)

    # ── preparation methods ───────────────────────────────────────────────────

    def prepare(self, state="0"):
        """Standard qubit init: asymmetric mass, random near-zero phases."""
        self.theta = wrap_theta(self.rng.normal(0, 0.02, self.N))
        hi, lo = 1.0/K_PER_BASIN, 1e-4
        self.mass = np.where(self.basin == (0 if state == "0" else 1), hi, lo)
        self.mass /= self.mass.sum()

    def prepare_qball(self, state="0", omega=0.5):
        """
        Q-ball initial condition: coherent locked phase, uniform rotation ω.

        All nodes rotate at the same ω — the U(1) charge Q = ω·M is well-defined
        and conserved (M is conserved by the Madelung kernel).  Active basin phase
        locked to 0; inactive basin to π.  This is the TFT-Classical broken-symmetry
        ground state for the qubit sector.
        """
        hi, lo = 1.0/K_PER_BASIN, 1e-4
        active = 0 if state == "0" else 1
        self.mass = np.where(self.basin == active, hi, lo)
        self.mass /= self.mass.sum()
        self.theta = np.where(self.basin == active, 0.0, np.pi).astype(float)
        self.omega = np.full(self.N, omega, dtype=float)

    def prepare_vortex(self, basin=0, uniform_mass=False, noise=0.01):
        """
        Vortex initial condition: phase winds 2π around the basin centre.

        uniform_mass=False  — concentrate mass in the vortex basin (standard qubit).
        uniform_mass=True   — set all nodes to m_i=v_sq (broken-symmetry vacuum).
                              Use this with Lambda>0 for topologically stable defects:
                              the potential cost at the vortex core (ρ→0) prevents
                              unwinding, so winding_readout() should stay ±1 indefinitely.
        """
        if uniform_mass:
            self.mass = np.full(self.N, self.v_sq)
        else:
            hi, lo = 1.0/K_PER_BASIN, 1e-4
            self.mass = np.where(self.basin == basin, hi, lo)
            self.mass /= self.mass.sum()

        cx = (-1 if basin == 0 else 1) * BASIN_SEP / 2
        cy = 0.0
        xs, ys = self.pos[:, 0], self.pos[:, 1]
        vortex = np.arctan2(ys - cy, xs - cx)

        self.theta = np.where(self.basin == basin, vortex, 0.0)
        self.theta = wrap_theta(self.theta + self.rng.normal(0, noise, self.N))

    # ── dynamics ──────────────────────────────────────────────────────────────

    def step(self, dt=0.02):
        th    = self.theta
        cdiff = np.cos(th[None,:] - th[:,None])
        diff  = np.sin(th[None,:] - th[:,None])
        sqm   = np.sqrt(np.maximum(self.mass, MASS_EPS))
        amp_ratio = sqm[None,:] / sqm[:,None]
        dth   = self.omega + self.g * np.sum(self.S * amp_ratio * cdiff, axis=1)
        flow  = -2*self.g * self.S * (sqm[:,None]*sqm[None,:]) * diff
        dm    = flow.sum(axis=1) - self.beta * self.mass
        if self.Lambda > 0:
            # Mexican hat V(m) = Λ(m-v²)²; dV/dm = 2Λ(m-v²)
            # Drives ρ → v everywhere. Sums to zero when Σm = N·v_sq → mass conserved.
            dm = dm - 2 * self.Lambda * (self.mass - self.v_sq)

        if self.phase_noise > 0:
            dth = dth + self.phase_noise*self.rng.normal(0, 1, self.N)/np.sqrt(dt)

        self.theta = wrap_theta(th + dt*dth)
        self.mass  = np.clip(self.mass + dt*dm, 0, None)

    def evolve(self, steps, dt=0.02):
        for _ in range(steps):
            self.step(dt)

    # ── readout ───────────────────────────────────────────────────────────────

    def basin_phase(self, b):
        th = self.theta[self.basin == b]
        m  = self.mass[self.basin == b]
        return float(np.angle(np.sum(np.sqrt(np.maximum(m, 0))*np.exp(1j*th))))

    def basin_mass(self, b):
        return float(self.mass[self.basin == b].sum())

    def coherence(self, b):
        th = self.theta[self.basin == b]
        return float(np.abs(np.mean(np.exp(1j*th))))

    def charge(self):
        """U(1) Noether charge proxy: Q = Σ m_i · ω_i. Conserved when ω uniform."""
        return float(np.dot(self.mass, self.omega))

    def bloch(self):
        m0, m1 = self.basin_mass(0), self.basin_mass(1)
        tot = m0 + m1 + 1e-12
        P1  = m1/tot
        phi = wrap_theta(self.basin_phase(1) - self.basin_phase(0))
        return {"P1": P1, "phi": phi, "z": (m0-m1)/tot,
                "r0": self.coherence(0), "r1": self.coherence(1),
                "total_mass": m0+m1}

    def winding_readout(self, grid_nx=12, grid_ny=8):
        """
        Project the phase field onto a 2D (x, y) grid and return plaquette
        winding numbers.  Meaningful in the broken-symmetry regime (ρ=v);
        use prepare_vortex() to seed a testable topological defect.

        Returns
        -------
        grid  : (grid_ny, grid_nx) float array, phase per cell in [0, 2π)
        w_map : (grid_ny−1, grid_nx−1) int array, +1 vortex / −1 antivortex / 0 smooth
        """
        xs, ys = self.pos[:, 0], self.pos[:, 1]
        x_lo, x_hi = xs.min() - 0.05, xs.max() + 0.05
        y_lo, y_hi = ys.min() - 0.05, ys.max() + 0.05

        gx = np.clip(((xs - x_lo) / (x_hi - x_lo) * grid_nx).astype(int), 0, grid_nx - 1)
        gy = np.clip(((ys - y_lo) / (y_hi - y_lo) * grid_ny).astype(int), 0, grid_ny - 1)

        grid = np.full((grid_ny, grid_nx), np.nan)
        for row in range(grid_ny):
            for col in range(grid_nx):
                mask = (gx == col) & (gy == row)
                if mask.any():
                    grid[row, col] = wrap_theta(circular_mean(self.theta[mask]))

        fill = wrap_theta(circular_mean(self.theta))
        grid = np.where(np.isnan(grid), fill, grid)
        return grid, winding_density_2d(grid)


# ── Experiments ───────────────────────────────────────────────────────────────

def exp_qball_stability(omega=0.5, bridge=0.0, steps=1000, dt=0.02):
    """
    Q-ball charge conservation test.  Charge Q = ω·M should stay constant
    (M is conserved by the Madelung kernel; ω is a fixed parameter).
    With bridge=0 the basins are isolated; with bridge>0 mass can flow but Q still holds.
    """
    q = TeotlQubit(seed=42)
    q.prepare_qball(state="0", omega=omega)
    q.set_bridge(bridge)
    Q0 = q.charge()
    M0 = q.basin_mass(0) + q.basin_mass(1)
    t  = np.arange(steps) * dt
    Q  = np.zeros(steps)
    P1 = np.zeros(steps)
    for s in range(steps):
        q.step(dt)
        Q[s]  = q.charge()
        P1[s] = q.bloch()["P1"]
    return t, Q, P1, Q0, M0


def exp_free_precession(detuning=0.4, steps=600, dt=0.02):
    q = TeotlQubit(detuning=detuning)
    q.prepare("0")
    q.set_bridge(0.0)
    phis = []
    for _ in range(steps):
        q.step(dt)
        phis.append(q.bloch()["phi"])
    rate = np.polyfit(np.arange(steps)*dt, np.unwrap(np.array(phis)), 1)[0]
    return rate, q.bloch()


def exp_rabi(detuning=0.0, bridge=1.0, steps=6000, dt=0.02, record_winding=False):
    q = TeotlQubit(detuning=detuning)
    q.prepare("0")
    q.set_bridge(bridge)
    t  = np.arange(steps) * dt
    P1   = np.zeros(steps)
    cons = np.zeros(steps)
    r0   = np.zeros(steps)
    r1   = np.zeros(steps)
    winding = np.zeros(steps, dtype=int) if record_winding else None
    for s in range(steps):
        q.step(dt)
        b = q.bloch()
        P1[s], cons[s], r0[s], r1[s] = b["P1"], b["total_mass"], b["r0"], b["r1"]
        if record_winding:
            _, w_map = q.winding_readout()
            winding[s] = int(w_map.sum())
    if record_winding:
        return t, P1, cons, r0, r1, winding
    return t, P1, cons, r0, r1


def dominant_freq(t, sig):
    sig   = sig - sig.mean()
    freqs = np.fft.rfftfreq(len(sig), d=t[1]-t[0])
    spec  = np.abs(np.fft.rfft(sig))
    return freqs[1:][np.argmax(spec[1:])]


if __name__ == "__main__":
    print("Teotl QC v0.3 — Madelung / conservative complex field\n")

    # ── Exp 1: Q-ball charge conservation ────────────────────────────────────
    print("── Exp 1: Q-ball charge conservation (bridge=0 and bridge=1.0) ──")
    for br in [0.0, 1.0]:
        t, Q, P1, Q0, M0 = exp_qball_stability(omega=0.5, bridge=br, steps=2000)
        dQ = abs(Q[-1] - Q0) / abs(Q0)
        print(f"  bridge={br:.1f}:  Q0={Q0:.5f}  Q_final={Q[-1]:.5f}  "
              f"dQ/Q0={dQ:.2e}  P1_range=[{P1.min():.3f},{P1.max():.3f}]")

    # ── Exp 2: Rabi oscillations (resonant) ──────────────────────────────────
    print("\n── Exp 2: Rabi, resonant (Δω=0), bridge=1.0 ──")
    t, P1, cons, r0, r1 = exp_rabi()
    f = dominant_freq(t, P1)
    print(f"  madelung:  P1 ∈ [{P1.min():.3f},{P1.max():.3f}]  "
          f"contrast={P1.max()-P1.min():.3f}  f={f:.4f}  "
          f"mass drift={abs(cons[-1]-cons[0])/cons[0]:.2e}  "
          f"r0_end={r0[-1]:.3f} r1_end={r1[-1]:.3f}")

    # ── Exp 3: Rabi frequency vs bridge amplitude ─────────────────────────────
    print("\n── Exp 3: Rabi frequency vs bridge amplitude ──")
    amps, fs = [0.25, 0.5, 0.75, 1.0], []
    for a in amps:
        t, P1, *_ = exp_rabi(bridge=a, steps=12000)
        f = dominant_freq(t, P1)
        fs.append(f)
        print(f"  bridge={a:.2f}:  f_Rabi={f:.4f}  contrast={P1.max()-P1.min():.3f}")
    slope = np.polyfit(amps, fs, 1)
    corr  = np.corrcoef(amps, fs)[0,1]
    print(f"  linearity: f = {slope[0]:.4f}·amp + {slope[1]:.4f}   r = {corr:.5f}")

    # ── Exp 4: detuned Rabi ───────────────────────────────────────────────────
    print("\n── Exp 4: detuned Rabi — generalised frequency check ──")
    t, P1, *_ = exp_rabi(detuning=0.0, bridge=1.0, steps=6000)
    f_res  = dominant_freq(t, P1)
    Omega0 = 2*np.pi*f_res
    for det in [0.1, 0.2, 0.4]:
        t, P1, *_ = exp_rabi(detuning=det, bridge=1.0, steps=6000)
        f_meas = dominant_freq(t, P1)
        f_pred = np.sqrt(Omega0**2 + det**2)/(2*np.pi)
        print(f"  Δω={det:.1f}:  f_meas={f_meas:.4f}  "
              f"f_pred=√(Ω₀²+Δω²)/2π={f_pred:.4f}  "
              f"P1_max={P1.max():.3f}  (pred {Omega0**2/(Omega0**2+det**2):.3f})")

    # ── Exp 5: Mexican hat potential — vortex persistence vs Λ ───────────────
    print("\n── Exp 5: vortex persistence vs Mexican hat strength Λ (grid 12×8) ──")
    print("  uniform mass (ρ=v everywhere), basin-0 vortex, bridge=0, dt=0.02")
    print(f"  {'Λ':>6}  {'t=0':>5}  {'t=1':>5}  {'t=4':>5}  {'t=10':>5}  "
          f"{'t=20':>5}  {'t=40':>5}  mass_drift")

    checkpoints = [0, 50, 200, 500, 1000, 2000]  # steps → t = 0,1,4,10,20,40

    for lam in [0.0, 0.1, 0.5, 1.0, 2.0]:
        q = TeotlQubit(seed=42, Lambda=lam)
        q.prepare_vortex(basin=0, uniform_mass=True)
        q.set_bridge(0.0)
        m0 = q.mass.sum()

        readings = []
        prev = 0
        for ck in checkpoints:
            q.evolve(ck - prev)
            _, w = q.winding_readout()
            readings.append(w.sum())
            prev = ck

        drift = abs(q.mass.sum() - m0) / m0
        vals  = "  ".join(f"{r:+d}" for r in readings)
        print(f"  {lam:>6.1f}  {vals}  {drift:.1e}")

    # ── Exp 5b: fine-grained winding timeseries for Λ=0 and Λ=1 ─────────────
    print("\n── Exp 5b: winding timeseries t=0..40 every Δt=0.5 (Λ=0 vs Λ=1) ──")
    print("  t      Λ=0   Λ=1")
    dt_ts  = 0.02
    stride = 25    # 25 steps × 0.02 = 0.5 time units per row
    rows   = 80    # 80 rows × 0.5 = t=40

    ts = {lam: None for lam in [0.0, 1.0]}
    for lam in [0.0, 1.0]:
        q = TeotlQubit(seed=42, Lambda=lam)
        q.prepare_vortex(basin=0, uniform_mass=True)
        q.set_bridge(0.0)
        series = []
        for _ in range(rows):
            q.evolve(stride)
            _, w = q.winding_readout()
            series.append(int(w.sum()))
        ts[lam] = series

    for i, (w0, w1) in enumerate(zip(ts[0.0], ts[1.0])):
        t_val = (i + 1) * stride * dt_ts
        print(f"  {t_val:5.1f}  {w0:+d}    {w1:+d}")
