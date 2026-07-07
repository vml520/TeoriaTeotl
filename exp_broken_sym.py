"""
exp_broken_sym.py — Goldstone-motivated broken-symmetry qubit experiment.

Standard prepare("0") puts all mass in basin 0.  This puts EQUAL mass in
both basins with a π phase offset between them — the broken-symmetry
ground state ρ=v for both basins, maximum off-diagonal coherence.

Questions:
  1. Does the π phase offset alone drive mass transfer without a bridge?
     (Isolates whether phase texture ≠ explicit coupling.)
  2. How do Rabi dynamics differ from |0⟩ init at the same bridge?
  3. Does the equal-mass / π-offset state show a different winding texture?
"""
import importlib.util, sys
import numpy as np

spec = importlib.util.spec_from_file_location(
    "teotl_qc", "/tmp/TT3/teotl qc.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

TeotlQubit   = mod.TeotlQubit
dominant_freq = mod.dominant_freq
K_PER_BASIN  = mod.K_PER_BASIN


def prepare_broken_pi(q, noise=0.02):
    """Both basins equal mass; basin 0 phases ≈ 0, basin 1 phases ≈ π."""
    hi = 1.0 / K_PER_BASIN
    q.mass  = np.full(q.N, hi)
    q.mass /= q.mass.sum()
    q.theta = np.where(
        q.basin == 0,
        q.rng.normal(0.0,   noise, q.N),
        q.rng.normal(np.pi, noise, q.N),
    ) % (2 * np.pi)


def run(label, bridge, prep_fn, steps=3000, dt=0.02):
    q = TeotlQubit(kernel="madelung", seed=42)
    prep_fn(q)
    q.set_bridge(bridge)

    t  = np.arange(steps) * dt
    P1   = np.zeros(steps)
    cons = np.zeros(steps)

    for s in range(steps):
        q.step(dt)
        b = q.bloch()
        P1[s]   = b["P1"]
        cons[s] = b["total_mass"]

    contrast   = P1.max() - P1.min()
    f          = dominant_freq(t, P1) if P1.std() > 1e-4 else 0.0
    mass_drift = abs(cons[-1] - cons[0]) / cons[0]
    _, w_final = q.winding_readout()
    w_sum      = int(w_final.sum())

    print(f"  {label:32}  P1∈[{P1.min():.3f},{P1.max():.3f}]  "
          f"contrast={contrast:.3f}  f={f:.4f}  "
          f"mass_drift={mass_drift:.1e}  w_final={w_sum:+d}")
    return P1, cons, f, contrast


print("Broken-symmetry Goldstone qubit — Madelung kernel\n")
hdr = f"  {'experiment':32}  {'P1 range':>16}  contrast   f_Rabi  mass_drift  w_final"
print(hdr)
print("  " + "─" * (len(hdr) - 2))

# ── isolation: can phase texture alone transfer mass? ─────────────────────────
print()
print("  [isolation — bridge = 0]")
run("A  bridge=0  broken_pi",  0.0, prepare_broken_pi, steps=3000)
run("A' bridge=0  |0⟩",       0.0, lambda q: q.prepare("0"), steps=3000)

# ── weak coupling ─────────────────────────────────────────────────────────────
print()
print("  [weak coupling — bridge = 0.25]")
run("B  bridge=0.25  |0⟩",       0.25, lambda q: q.prepare("0"), steps=3000)
run("B' bridge=0.25  broken_pi", 0.25, prepare_broken_pi, steps=3000)

# ── full coupling ─────────────────────────────────────────────────────────────
print()
print("  [full coupling — bridge = 1.0]")
run("C  bridge=1.0  |0⟩",       1.0, lambda q: q.prepare("0"), steps=3000)
run("C' bridge=1.0  broken_pi", 1.0, prepare_broken_pi, steps=3000)

print()
print("Interpretation guide:")
print("  contrast ≈ 0   → no Rabi oscillation (expected: isolation, and possibly broken_pi at equator)")
print("  w_final ≠ 0    → topological defect in final phase field")
print("  broken_pi starts at Bloch equator (P1=0.5, φ=π) — Rabi shows as equatorial rotation,")
print("  not pole-to-pole swing, so lower P1 contrast is expected even with strong coupling.")
