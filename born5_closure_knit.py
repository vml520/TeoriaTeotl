"""BORN0 Stage 5 -- consistency knit: ONE rule (|<.|Psi>|^2 on the coherent S^1
phase) gives the single-outcome marginals, the closure correlation E=cos(a-b),
no-signaling, AND Tsirelson S=2sqrt2 -- with Stage-4 Malus as the product-state
special case.  No second, incompatible mechanism.
Pre-reg: BORN0_prereg.md, stage 5.  Uses the Stage-3 weight (derived) and the
entangled two-winding (singlet) state.
"""
import json
import numpy as np

def hdr(s): print("\n" + "=" * 70 + "\n" + s + "\n" + "=" * 70)

def plus(a):  return np.array([np.cos(a/2),  np.sin(a/2)], dtype=complex)
def minus(a): return np.array([-np.sin(a/2), np.cos(a/2)], dtype=complex)
up = np.array([1, 0], dtype=complex)

# entangled two-winding (singlet) state in C^4, basis |uu>,|ud>,|du>,|dd>
singlet = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)

def joint_P(a, b):
    """The ONE rule: P(A,B|a,b) = |<A_a (x) B_b | singlet>|^2 (Stage-3 weight)."""
    P = {}
    for sA, fA in [(+1, plus), (-1, minus)]:
        for sB, fB in [(+1, plus), (-1, minus)]:
            ket = np.kron(fA(a), fB(b))
            P[(sA, sB)] = np.abs(np.vdot(ket, singlet))**2
    return P

# ------------------------------------------------------------------ Stage 5a
hdr("5a  ONE rule -> joint probabilities; normalized")
rng = np.random.default_rng(3)
norm_errs = []
for _ in range(500):
    a, b = rng.uniform(0, 2*np.pi, 2)
    norm_errs.append(abs(sum(joint_P(a, b).values()) - 1.0))
max_norm = max(norm_errs)
print(f"  sum_AB P(A,B|a,b) over 500 random (a,b): max |sum-1| = {max_norm:.2e}")

# ------------------------------------------------------------------ Stage 5b
hdr("5b  no-signaling: marginal P(A=+) is INDEPENDENT of the far setting b")
a_fixed = 0.4
margs = []
for b in np.linspace(0, 2*np.pi, 40):
    P = joint_P(a_fixed, b)
    margs.append(P[(+1, +1)] + P[(+1, -1)])          # P(A=+) = sum over B
margs = np.array(margs)
ns_spread = np.ptp(margs)
print(f"  P(A=+ | a=0.4) as far setting b sweeps: mean={margs.mean():.4f}  "
      f"spread={ns_spread:.2e}")
print(f"  -> marginal fixed at 1/2, independent of b: NO-SIGNALING (same as closure).")

# ------------------------------------------------------------------ Stage 5c
hdr("5c  same rule -> closure correlation E(a,b) and Tsirelson S=2sqrt2")
def E(a, b):
    P = joint_P(a, b)
    return P[(1,1)] + P[(-1,-1)] - P[(1,-1)] - P[(-1,1)]
th = np.linspace(0, 2*np.pi, 200)
Evals = np.array([E(0.0, t) for t in th])
corr_err = np.max(np.abs(Evals - (-np.cos(th))))     # singlet: E = -cos(a-b)
print(f"  max |E(0,b) - (-cos b)| = {corr_err:.2e}   (singlet sign; |E|=|cos|, closure form)")
# CHSH at the standard optimal angles
a0, a1, b0, b1 = 0.0, np.pi/2, np.pi/4, 3*np.pi/4
S = abs(E(a0, b0) - E(a0, b1) + E(a1, b0) + E(a1, b1))
print(f"  CHSH S = {S:.6f}   Tsirelson 2sqrt2 = {2*np.sqrt(2):.6f}   "
      f"(SAME rule reproduces the closure headline)")
S_err = abs(S - 2*np.sqrt(2))

# ------------------------------------------------------------------ Stage 5d
hdr("5d  Stage-4 Malus is the PRODUCT-state special case of the same rule")
th2 = np.linspace(0, np.pi, 200)
malus = np.array([np.abs(np.vdot(plus(t), up))**2 for t in th2])   # 1-particle, same |amp|^2
malus_err = np.max(np.abs(malus - np.cos(th2/2)**2))
print(f"  single winding |up> measured at theta: max |P(+) - cos^2(theta/2)| = {malus_err:.2e}")
print(f"  => marginals (5b), correlation (5c), Malus (5d) ALL from |<.|Psi>|^2. One rule.")

# ------------------------------------------------------------------ gate
hdr("VERDICT  (gate pre-committed in BORN0_prereg.md, stage 5)")
PASS = (max_norm < 1e-12) and (ns_spread < 1e-12) and (abs(margs.mean()-0.5) < 1e-12) \
       and (corr_err < 1e-12) and (S_err < 1e-6) and (malus_err < 1e-12)
print(f"  normalization           : {max_norm:.1e}   (< 1e-12)")
print(f"  no-signaling spread     : {ns_spread:.1e}   (< 1e-12), marginal={margs.mean():.4f}")
print(f"  closure correlation     : {corr_err:.1e}   (< 1e-12)")
print(f"  Tsirelson S             : {S:.6f}  (|S-2sqrt2|={S_err:.1e} < 1e-6)")
print(f"  Malus (product case)    : {malus_err:.1e}   (< 1e-12)")
verdict = "PASS" if PASS else "FAIL"
print(f"""\n[{verdict}] A SINGLE coherent-phase rule -- P = |<.|Psi>|^2 (the Stage-3 weight)
  -- yields the single-outcome marginals, no-signaling, the closure's E=cos(a-b),
  Tsirelson S=2sqrt2, and Stage-4 Malus (its product-state limit), all mutually
  consistent. No second mechanism was introduced: the correlations and the
  single-outcome probabilities are the same object.
  FLOOR (unchanged): reproduces QM exactly -> no distinguishing test; inherits the
  Stage-3 assumptions (pure-env-invariance + additivity/non-contextuality).""")

assert PASS, "STAGE 5 GATE FAILED -- STOP."   # runtime stop-on-fail (spec sec.0)

out = dict(prereg="BORN0_prereg.md stage 5", stage="5 closure consistency knit",
           max_norm_err=float(max_norm), no_signaling_spread=float(ns_spread),
           marginal_mean=float(margs.mean()), closure_corr_err=float(corr_err),
           CHSH_S=float(S), tsirelson=float(2*np.sqrt(2)), S_err=float(S_err),
           malus_product_err=float(malus_err), verdict=verdict,
           note="One rule P=|<.|Psi>|^2 gives marginals + no-signaling + E=cos(a-b) + "
                "Tsirelson 2sqrt2 + Malus (product limit), mutually consistent, no "
                "second mechanism. FLOOR: reproduces QM (degenerate); inherits stage-3 "
                "assumptions.")
json.dump(out, open("outputs/BORN_stage5.json", "w"), indent=2)
print("\n[results block written: outputs/BORN_stage5.json]")
