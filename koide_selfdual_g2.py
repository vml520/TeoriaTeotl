import numpy as np

def hdr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70)
SQRT2 = np.sqrt(2)
def Q_of_A(A): return 1/3 + A**2/6
def ok(A): return "  PASS (=sqrt2)" if abs(A-SQRT2)<1e-6 else "  fail"

hdr("G2  Candidate principles -> predicted amplitude A  (target A=sqrt2)")

print("Recall: A^2 = 2 * (breaking power)/(symmetric power);  Q = 1/3 + A^2/6\n")

# Candidate 1: naive per-real-degree-of-freedom equipartition (n=0,+1,-1 each equal)
A1 = np.sqrt(2*2.0)   # breaking:symmetric = 2:1
print(f"1. per-real-dof equipartition (breaking = 2 modes)   A={A1:.4f} Q={Q_of_A(A1):.4f}{ok(A1)}")

# Candidate 2: per-harmonic equipartition (reality pair n=+-1 counts once)
A2 = np.sqrt(2*1.0)
print(f"2. per-HARMONIC equipartition (breaking = 1 mode)     A={A2:.4f} Q={Q_of_A(A2):.4f}{ok(A2)}")

# Candidate 3: positivity boundary (max A keeping all sqrt(m_k)>=0 at best phase)
#   3 equally spaced cosines: best-case min cosine = -1/2  ->  1 + A*(-1/2) = 0 -> A = 2
A3 = 2.0
print(f"3. positivity-cone boundary (max A, some sqrt m ->0)  A={A3:.4f} Q={Q_of_A(A3):.4f}{ok(A3)}")

# Candidate 4: extremize Q over A  (dQ/dA = A/3 != 0 for A>0 -> no interior extremum)
print(f"4. extremal Q                                         A=none  (Q strictly increasing in A){' '*0}  fail")

# Candidate 5: cycle-graph 'BPS'  -- gradient energy on the 3-cycle couples ONLY to
#   the breaking (fundamental) sector; DC has zero gradient. So no principle of the
#   form gradient=potential ties symmetric:breaking at 1:1.
print(f"5. gradient(3-cycle)=potential BPS split              A=none  (gradient sees only breaking) fail")

hdr("Verdict against the G0 gate")
print("""Only Candidate 2 (per-harmonic / reality-pair-as-one-mode) yields A=sqrt2.
Candidates 1,3 give A=2 (the ruled-out Q=1); 4,5 give nothing.

BUT the honest tension (why this is NOT yet a derivation):
  * Candidate 2 is justified by the REALITY condition F_{-1}=conj(F_{+1}),
    which makes the fundamental one physical complex mode for a REAL field.
  * TFT's field is COMPLEX (psi = rho e^{i theta}); for a complex field
    F_{+1} and F_{-1} are INDEPENDENT -> that argues the OTHER way (toward 2).
  So sqrt2 emerges from a real-field mode count, but TFT does not yet FORCE
  the reduction to a real field on the internal circle. The winner is the
  physically natural count, not a forced one.

Also (scope honesty): self-duality fixes only Q (ONE relation). The individual
masses still need the scale M and the phase delta:""")

# show delta is a second, unfixed input
m = np.array([0.51099895, 105.6583755, 1776.86]); v=np.sqrt(m); M=v.mean()
c = (v/M - 1)/SQRT2                      # = cos(delta + 2pi k/3)
th = np.arctan2(np.sqrt(np.clip(1-c**2,0,1)), c)  # rough
# recover delta from k=... just report the fitted phase spread
delta = np.degrees(np.arccos(np.clip(c[np.argmax(v)],-1,1)))
print(f"   fitted phase delta ~ {delta:.2f} deg  (sets which generation is heaviest;")
print(f"   NOT fixed by self-duality -> even a full sqrt2 proof predicts m_tau")
print(f"   from m_e,m_mu, i.e. ONE relation, not all three masses).")

hdr("G0 RESULT: characterization ACHIEVED, derivation NOT achieved (logged, stop)")
print("""Delivered: Koide reduced to one exact, verified, TFT-native statement
(equal power per harmonic on the internal S^1), with A=0/sqrt2/2 mapped to
symmetric-only / per-harmonic / per-real-dof counting. Eliminated positivity,
extremal-Q, and cycle-BPS as the source. Remaining crux is a single sharp
question: does TFT force a REAL reduction of the internal-circle profile?
Per the pre-registered gate, sqrt2 is not yet forced -> NOT derived.""")
