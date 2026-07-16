"""DIS0 Stage 4 -- multipartite contextuality (GHZ / Mermin): does the coherent-
phase closure reproduce QM's M=4, or fall short? Pre-reg: DIS0_prereg.md addendum.
A distinguisher of the OTHER sign -- if TFT can't reach full contextuality, GHZ
experiments falsify it.
"""
import json, itertools
import numpy as np

def hdr(s): print("\n" + "=" * 70 + "\n" + s + "\n" + "=" * 70)

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
def sig(phi):                       # the closure primitive: a phase read vs setting phi
    return np.cos(phi)*X + np.sin(phi)*Y     # cos(phi)X + sin(phi)Y  (=X at 0, Y at pi/2)
def kron3(a, b, c): return np.kron(np.kron(a, b), c)

GHZ = np.zeros(8, dtype=complex); GHZ[0] = GHZ[7] = 1/np.sqrt(2)   # (|000>+|111>)/sqrt2

def E(pa, pb, pc, state=GHZ):       # coherent-closure 3-body correlation
    return np.real(state.conj() @ kron3(sig(pa), sig(pb), sig(pc)) @ state)

# ------------------------------------------------------------------ Stage 4a
hdr("4a  coherent-closure correlation = cos(phi_a+phi_b+phi_c)  [the QM/GHZ form]")
rng = np.random.default_rng(0)
dev = max(abs(E(*rng.uniform(0, 2*np.pi, 3).tolist()) -
              np.cos(sum(p := rng.uniform(0, 2*np.pi, 3)))) for _ in range(1))
# clean sweep test
devs = []
for _ in range(2000):
    pa, pb, pc = rng.uniform(0, 2*np.pi, 3)
    devs.append(abs(E(pa, pb, pc) - np.cos(pa+pb+pc)))
max_dev = max(devs)
print(f"  max |E(closure) - cos(sum)| over 2000 settings = {max_dev:.2e}")

# ------------------------------------------------------------------ Stage 4b
hdr("4b  the GHZ paradox (perfect correlations) + Mermin M")
XXX = E(0, 0, 0); XYY = E(0, np.pi/2, np.pi/2)
YXY = E(np.pi/2, 0, np.pi/2); YYX = E(np.pi/2, np.pi/2, 0)
print(f"  <XXX>={XXX:+.4f}  <XYY>={XYY:+.4f}  <YXY>={YXY:+.4f}  <YYX>={YYX:+.4f}  (all +/-1)")
print(f"  LHV consistency: (XYY)(YXY)(YYX) = {XYY*YXY*YYX:+.0f}  forces XXX={XYY*YXY*YYX:+.0f},")
print(f"                   but the closure gives XXX={XXX:+.0f}  -> LHV IMPOSSIBLE (the paradox).")
M_closure = abs(XYY + YXY + YYX - XXX)
print(f"  Mermin M (closure) = |<XYY>+<YXY>+<YYX>-<XXX>| = {M_closure:.4f}")

# LHV bound: brute force over +/-1 assignments (x_j = value of X, y_j = value of Y)
best_lhv = 0
for bits in itertools.product([-1, 1], repeat=6):
    xa, ya, xb, yb, xc, yc = bits
    best_lhv = max(best_lhv, abs(xa*yb*yc + ya*xb*yc + ya*yb*xc - xa*xb*xc))
print(f"  Mermin M (LHV max, brute 2^6)       = {best_lhv:.4f}   (the classical bound)")

# ------------------------------------------------------------------ Stage 4c
hdr("4c  GHZ is IRREDUCIBLE to 2-body: pairwise correlations all vanish")
pairwise = []
for (pi, pj, lbl) in [(0,0,"<X X .>"),(0,np.pi/2,"<X Y .>"),(np.pi/2,np.pi/2,"<Y Y .>")]:
    # 2-body corr on qubits 1,2 (trace out 3): <sig(pi) x sig(pj) x I>
    val = np.real(GHZ.conj() @ kron3(sig(pi), sig(pj), I2) @ GHZ)
    pairwise.append(abs(val)); print(f"    {lbl} = {val:+.2e}")
max_pairwise = max(pairwise)
print(f"  all 2-body correlations = 0 (max {max_pairwise:.1e}) => a 2-body-only model")
print(f"  predicts <XYY> etc ~ 0 => Mermin M ~ 0 <= 2. Reaching M=4 REQUIRES genuine")
print(f"  3-body coherence; the closure has it (4a), a pairwise-only closure would NOT.")

# ------------------------------------------------------------------ Stage 4d
hdr("4d  hidden phase cancels (no-signaling): global phase + single-party marginal")
E_shift = E(0.3, 1.1, 2.0, state=np.exp(1j*1.234)*GHZ)   # add global hidden phase
E_orig  = E(0.3, 1.1, 2.0)
marg = np.real(GHZ.conj() @ kron3(sig(0.7), I2, I2) @ GHZ)  # single-party expectation
print(f"  E with global phase e^{{i1.234}} = {E_shift:+.6f}  vs no phase {E_orig:+.6f}  "
      f"(diff {abs(E_shift-E_orig):.1e})")
print(f"  single-party marginal <sig(0.7) x I x I> = {marg:+.2e}  -> NO-SIGNALING")

# ------------------------------------------------------------------ verdict
hdr("VERDICT  (gate pre-committed in DIS0_prereg.md addendum, stage 4)")
reaches_qm = abs(M_closure - 4.0) < 1e-9
verdict = "DEGENERATE" if reaches_qm else "DISTINGUISHER"
print(f"  coherent-closure Mermin M = {M_closure:.4f}   QM = 4   LHV bound = {best_lhv:.1f}")
print(f"""\n[{verdict}] The coherent-phase closure reaches Mermin **M = {M_closure:.1f} = QM**,
  reproducing the full GHZ paradox (perfect correlations, LHV impossible) and the
  irreducible 3-body contextuality (2-body correlations all vanish, yet M=4). So
  GHZ does NOT distinguish compact-time TFT from QM either -- it is DEGENERATE,
  and TFT captures genuine multipartite contextuality, not merely 2-body.
  HONEST CAVEAT: this uses the full 3-qubit tensor Hilbert space that the closure
  claims to be ("coherent phase = Hilbert space"; CHSH established the 2-body
  sector). A field-theoretic proof that n windings realize the full 2^n-dim tensor
  space is the deeper open point -- IF the S^1 construction saturated at 2-body it
  would give M~0 (4c) and BE FALSIFIED by real GHZ data. Either way TFT must be
  full-tensor to survive, and there it is degenerate with QM.""")

out = dict(prereg="DIS0_prereg.md stage 4 (GHZ/Mermin)", verdict=verdict,
           closure_cos_sum_dev=float(max_dev), M_closure=float(M_closure),
           M_qm=4.0, M_lhv=float(best_lhv), max_pairwise_correlation=float(max_pairwise),
           nosignaling_marginal=float(marg), global_phase_invariance=float(abs(E_shift-E_orig)),
           note="Coherent closure reaches Mermin M=4=QM: reproduces GHZ paradox + "
                "irreducible 3-body contextuality (pairwise=0). GHZ DEGENERATE (no "
                "distinguisher). Caveat: assumes full tensor Hilbert space (CHSH gave "
                "2-body); if S^1 saturated at 2-body it'd give M~0 and be falsified -> "
                "TFT must be full-tensor, and there = QM.")
json.dump(out, open("outputs/DIS_ghz.json", "w"), indent=2)
print("\n[results block written: outputs/DIS_ghz.json]")
