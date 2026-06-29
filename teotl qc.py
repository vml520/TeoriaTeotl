"""
Teotl QC v0.2 — Milestone 1: single qubit, Rabi test, dual-kernel
───────────────────────────────────────────────────────────────────────────────
M = R³ × S¹

A qubit is DEFINED as two node basins in R³, each internally phase-coherent.
Nothing quantum is injected; quantum-looking quantities are READ OUT:

    ψ_k  = sqrt(m_k) · exp(i·θ̄_k)     k ∈ {0,1}  (basin mass, circular-mean phase)
    P(1) = m₁ / (m₀ + m₁)
    φ    = θ̄₁ − θ̄₀

Two carrier-transport kernels, compared head-to-head:

  KERNEL A — "rectified" (v20.3-native, DERIVED from existing TFT code):
      θ̇_i = ω_i + g Σ_j W[i,j]·sin(θ_j−θ_i)            (Kuramoto)
      ṁ_i = g Σ_j W[i,j]·max(sin(θ_j−θ_i),0) − β m_i    (source + decay)
      Open-system: mass is created/destroyed, not moved.

  KERNEL B — "madelung" (PROPOSED conservative limit):
      θ̇_i = ω_i + g Σ_j S[i,j]·√(m_j/m_i)·cos(θ_j−θ_i)
      ṁ_i = −2g Σ_j S[i,j]·√(m_i·m_j)·sin(θ_j−θ_i)
      S symmetric → pairwise-antisymmetric flow → total mass conserved.
      This is exactly discrete Schrödinger (ψ_i = √m_i e^{iθ_i}, H = ω − gS)
      in Madelung/Bohm hydrodynamic variables — the same mathematical
      territory as the pilot-wave framework TFT cites as closest prior.

  HONEST NOTE: Kernel B's phase coupling is cos(·), weighted by amplitude —
  NOT Kuramoto's sin(·). The sin/cos distinction is the precise mathematical
  boundary between synchronizing classical dynamics (A) and unitary quantum
  dynamics (B). Locating that boundary is itself a milestone-1 result.

Epistemic labels:
  DERIVED   — Kernel A behavior from v20.3 conventions; free-precession
              Z-rotation from per-node ω detuning (works under both kernels).
  PROPOSED  — Kernel B as TFT's conservative carrier-transport sector;
              bridge amplitude ↔ X-drive; β ↔ T1; phase noise ↔ T2.
  OPEN      — whether Kernel B is derivable from the TFT action rather than
              postulated; Born statistics; CHSH (milestone 3).
───────────────────────────────────────────────────────────────────────────────
"""

import numpy as np
from teotl_math import wrap_theta, winding_density_2d, circular_mean

# ── First-class scales ────────────────────────────────────────────────────────
E_0, l_0 = 1.0, 1.0
XI       = 3.0 * l_0
SIGMA    = l_0
DIST_EPS = 1e-6
MASS_EPS = 1e-9

K_PER_BASIN  = 16
BASIN_SEP    = 2.0 * l_0
BASIN_RADIUS = 0.4 * l_0

class TeotlQubit:
    def __init__(self, detuning=0.0, kernel="madelung",
                 g=0.05, beta=0.0, phase_noise=0.0, seed=42):
        self.rng    = np.random.default_rng(seed)
        self.kernel = kernel
        self.g      = g
        self.beta   = beta
        self.phase_noise = phase_noise
        self.N      = 2 * K_PER_BASIN
        self.basin  = np.array([0]*K_PER_BASIN + [1]*K_PER_BASIN)

        pos = np.zeros((self.N, 3))
        for k in range(self.N):
            c = np.array([(-1 if self.basin[k]==0 else 1)*BASIN_SEP/2, 0, 0])
            pos[k] = c + self.rng.normal(0, BASIN_RADIUS/2, 3)
        self.pos = pos

        self.omega = np.where(self.basin==0, -detuning/2, +detuning/2).astype(float)
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
        # Kernel A uses row-normalized coupling (v20.3 convention)
        rs = self.S.sum(axis=1, keepdims=True) + 1e-12
        self.W = self.S / rs

    def prepare(self, state="0"):
        self.theta = wrap_theta(self.rng.normal(0, 0.02, self.N))
        hi, lo = 1.0/K_PER_BASIN, 1e-4
        if state == "0":
            self.mass = np.where(self.basin==0, hi, lo)
        else:
            self.mass = np.where(self.basin==1, hi, lo)
        self.mass /= self.mass.sum()

    def step(self, dt=0.02):
        th   = self.theta
        diff = np.sin(th[None,:] - th[:,None])     # [i,j] = sin(θj−θi)

        if self.kernel == "rectified":
            coup  = self.g * np.sum(self.W * diff, axis=1)
            dth   = self.omega + coup
            inflow = self.g * np.sum(self.W * np.maximum(diff,0), axis=1)
            dm    = inflow - self.beta * self.mass
        elif self.kernel == "madelung":
            cdiff = np.cos(th[None,:] - th[:,None])
            sqm   = np.sqrt(np.maximum(self.mass, MASS_EPS))
            amp_ratio = sqm[None,:] / sqm[:,None]            # √(m_j/m_i)
            dth = self.omega + self.g * np.sum(self.S * amp_ratio * cdiff, axis=1)
            flow = -2*self.g * self.S * (sqm[:,None]*sqm[None,:]) * diff
            dm   = flow.sum(axis=1) - self.beta * self.mass
        else:
            raise ValueError(self.kernel)

        if self.phase_noise > 0:
            dth = dth + self.phase_noise*self.rng.normal(0,1,self.N)/np.sqrt(dt)

        self.theta = wrap_theta(th + dt*dth)
        self.mass  = np.clip(self.mass + dt*dm, 0, None)

    def evolve(self, steps, dt=0.02):
        for _ in range(steps):
            self.step(dt)

    # ── readout ────────────────────────────────────────────────────────────────
    def basin_phase(self, b):
        th = self.theta[self.basin==b]
        m  = self.mass[self.basin==b]
        return float(np.angle(np.sum(np.sqrt(np.maximum(m,0))*np.exp(1j*th))))

    def basin_mass(self, b):
        return float(self.mass[self.basin==b].sum())

    def coherence(self, b):
        th = self.theta[self.basin==b]
        return float(np.abs(np.mean(np.exp(1j*th))))

    def bloch(self):
        m0, m1 = self.basin_mass(0), self.basin_mass(1)
        tot = m0 + m1 + 1e-12
        P1  = m1/tot
        phi = wrap_theta(self.basin_phase(1) - self.basin_phase(0))
        return {"P1":P1, "phi":phi, "z":(m0-m1)/tot,
                "r0":self.coherence(0), "r1":self.coherence(1),
                "total_mass": m0+m1}

    def winding_readout(self, grid_nx=6, grid_ny=4):
        """
        Project the phase field onto a 2D (x, y) grid and return plaquette
        winding numbers.  Not called by step() or evolve() — opt-in only.

        Nodes are projected by (x, y) position onto a grid_ny × grid_nx grid;
        each cell gets the circular-mean phase of its nodes.  Empty cells are
        filled with the global circular mean so winding_density_2d never sees NaN.

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
def exp_free_precession(kernel, detuning=0.4, steps=600, dt=0.02):
    q = TeotlQubit(detuning=detuning, kernel=kernel)
    q.prepare("0"); q.set_bridge(0.0)
    phis = []
    for _ in range(steps):
        q.step(dt); phis.append(q.bloch()["phi"])
    rate = np.polyfit(np.arange(steps)*dt, np.unwrap(np.array(phis)), 1)[0]
    return rate, q.bloch()

def exp_rabi(kernel, detuning=0.0, bridge=1.0, steps=6000, dt=0.02,
             record_winding=False):
    q = TeotlQubit(detuning=detuning, kernel=kernel)
    q.prepare("0"); q.set_bridge(bridge)
    t = np.arange(steps)*dt
    P1 = np.zeros(steps); cons = np.zeros(steps)
    r0 = np.zeros(steps); r1 = np.zeros(steps)
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
    sig = sig - sig.mean()
    freqs = np.fft.rfftfreq(len(sig), d=t[1]-t[0])
    spec  = np.abs(np.fft.rfft(sig))
    return freqs[1:][np.argmax(spec[1:])]

if __name__ == "__main__":
    print("Teotl QC v0.2 — milestone 1, dual kernel\n")

    print("── Exp 1: free precession, Δω=0.4, bridge OFF ──")
    for k in ["rectified", "madelung"]:
        rate, b = exp_free_precession(k)
        print(f"  {k:>9}:  dφ/dt={rate:.4f} (target 0.4)  P1={b['P1']:.4f}  "
              f"r0={b['r0']:.3f} r1={b['r1']:.3f}")

    print("\n── Exp 2: Rabi, resonant (Δω=0), bridge=1.0 ──")
    for k in ["rectified", "madelung"]:
        t, P1, cons, r0, r1 = exp_rabi(k)
        f = dominant_freq(t, P1)
        print(f"  {k:>9}:  P1 ∈ [{P1.min():.3f},{P1.max():.3f}]  "
              f"contrast={P1.max()-P1.min():.3f}  f={f:.4f}  "
              f"mass drift={abs(cons[-1]-cons[0])/cons[0]:.2e}  "
              f"r0_end={r0[-1]:.3f} r1_end={r1[-1]:.3f}")

    print("\n── Exp 3: Rabi frequency vs bridge amplitude (madelung) ──")
    amps, fs = [0.25, 0.5, 0.75, 1.0], []
    for a in amps:
        t, P1, *_ = exp_rabi("madelung", bridge=a, steps=12000)
        f = dominant_freq(t, P1); fs.append(f)
        print(f"  bridge={a:.2f}:  f_Rabi={f:.4f}  contrast={P1.max()-P1.min():.3f}")
    slope = np.polyfit(amps, fs, 1)
    corr  = np.corrcoef(amps, fs)[0,1]
    print(f"  linearity: f = {slope[0]:.4f}·amp + {slope[1]:.4f}   r = {corr:.5f}")

    print("\n── Exp 4: detuned Rabi — generalized frequency check (madelung) ──")
    t, P1, *_ = exp_rabi("madelung", detuning=0.0, bridge=1.0, steps=6000)
    f_res = dominant_freq(t, P1)
    Omega0 = 2*np.pi*f_res
    for det in [0.1, 0.2, 0.4]:
        t, P1, *_ = exp_rabi("madelung", detuning=det, bridge=1.0, steps=6000)
        f_meas = dominant_freq(t, P1)
        f_pred = np.sqrt(Omega0**2 + det**2)/(2*np.pi)
        print(f"  Δω={det:.1f}:  f_meas={f_meas:.4f}  f_pred=√(Ω₀²+Δω²)/2π={f_pred:.4f}  "
          f"P1_max={P1.max():.3f}  (pred {Omega0**2/(Omega0**2+det**2):.3f})")

    print("\n── Exp 5: plaquette winding readout during Rabi (madelung, 600 steps) ──")
    t5, P1_5, cons_5, *_, winding = exp_rabi(
        "madelung", bridge=1.0, steps=600, dt=0.02, record_winding=True)
    total_charge = winding.sum()
    nonzero = int(np.count_nonzero(winding))
    print(f"  steps recorded : {len(winding)}")
    print(f"  non-zero winding steps : {nonzero} / {len(winding)}  "
          f"(defects nucleated at {nonzero/len(winding)*100:.1f}% of steps)")
    print(f"  total topological charge accumulated : {total_charge}")
    print(f"  winding range : [{winding.min()}, {winding.max()}]")
    print(f"  Rabi P1 range : [{P1_5.min():.3f}, {P1_5.max():.3f}]  "
          f"mass drift : {abs(cons_5[-1]-cons_5[0])/cons_5[0]:.2e}  (unchanged)")
