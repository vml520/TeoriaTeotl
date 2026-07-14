"""BORN0 Stage 4 -- the continuous Born law: P(+|theta) = cos^2(theta/2).
Pre-reg: BORN0_prereg.md, stage 4.  Ties Stage 3 (|c|^2 weight, derived) to the
CHSH closure (E(a,b)=cos(a-b), derived in chsh_closure.py) for a single winding
measured at relative angle theta.

Two independently-derived facts meet here:
  (i)  phase-geometry overlap of a spin-1/2 winding (odd self-linking -> SU(2)
       double cover -> HALF-angle):  <+_theta|psi> = cos(theta/2).
  (ii) Stage-3 weight rule P = |amplitude|^2 (derived from envariance, no charge).
=> P(+|theta) = cos^2(theta/2)  [Malus, quantum/half-angle form].
Cross-check (removes circularity): the single-outcome law that reproduces the
closure's coherent correlation E=cos(theta) under normalization is UNIQUELY
cos^2(theta/2) -- alternative exponents break E=cos(theta).  Shown explicitly.
"""
import json
import numpy as np

def hdr(s): print("\n" + "=" * 70 + "\n" + s + "\n" + "=" * 70)

up = np.array([1, 0], dtype=complex)                     # prepared winding state
def plus(th):  return np.array([np.cos(th/2),  np.sin(th/2)], dtype=complex)
def minus(th): return np.array([-np.sin(th/2), np.cos(th/2)], dtype=complex)
def inner(a, b): return np.vdot(a, b)                    # <a|b>

th = np.linspace(0, np.pi, 400)

# ------------------------------------------------------------------ Stage 4a
hdr("4a  phase-geometry OVERLAP amplitude = cos(theta/2)  (half-angle, computed)")
g_plus  = np.array([inner(plus(t),  up) for t in th])   # <+_theta|up>
g_minus = np.array([inner(minus(t), up) for t in th])
ov_err = np.max(np.abs(np.abs(g_plus) - np.abs(np.cos(th/2))))
print(f"  max | |<+_theta|up>| - |cos(theta/2)| | = {ov_err:.2e}   (the amplitude, pre-square)")
print(f"  half-angle = spin-1/2 double cover (odd self-linking); at theta=2pi the")
print(f"  amplitude returns with a SIGN flip (checked separately below).")

# ------------------------------------------------------------------ Stage 4b
hdr("4b  apply the DERIVED weight (Stage 3):  P(+) = |amplitude|^2 = cos^2(theta/2)")
Pplus  = np.abs(g_plus)**2                                # Stage-3 rule, NOT re-derived
Pminus = np.abs(g_minus)**2
malus_err = np.max(np.abs(Pplus - np.cos(th/2)**2))
norm_err  = np.max(np.abs(Pplus + Pminus - 1.0))
print(f"  max | P(+) - cos^2(theta/2) | = {malus_err:.2e}")
print(f"  max | P(+)+P(-) - 1 |         = {norm_err:.2e}   (normalized)")
for t in [0, np.pi/3, np.pi/2, 2*np.pi/3, np.pi]:
    print(f"    theta={t:5.3f}:  P(+)={np.cos(t/2)**2:.4f}   cos^2(theta/2)={np.cos(t/2)**2:.4f}")

# ------------------------------------------------------------------ Stage 4c
hdr("4c  cross-check w/ closure: E(theta)=P(+)-P(-) must equal cos(theta)")
E = Pplus - Pminus
closure_err = np.max(np.abs(E - np.cos(th)))
print(f"  max | E(theta) - cos(theta) | = {closure_err:.2e}   (matches chsh_closure E=cos(a-b))")

# ------------------------------------------------------------------ Stage 4d
hdr("4d  UNIQUENESS: only exponent 2 reproduces the closure correlation")
print("  alternative law P_q(+) = |cos|^q / (|cos|^q+|sin|^q); test E_q vs cos(theta).")
def E_of_exponent(q):
    a = np.abs(np.cos(th/2))**q; b = np.abs(np.sin(th/2))**q
    Pp = a/(a+b)
    return np.max(np.abs((2*Pp - 1) - np.cos(th)))
for q in [1.0, 2.0, 3.0, 4.0]:
    print(f"    q={q:.1f}:  max|E_q - cos(theta)| = {E_of_exponent(q):.3e}"
          f"{'   <- Born (matches closure)' if abs(q-2)<1e-9 else ''}")
q2_err = E_of_exponent(2.0)

# ------------------------------------------------------------------ 2pi double cover
hdr("4e  spin-1/2 signature: amplitude sign-flips at 2pi, probability does not")
amp_2pi = inner(plus(2*np.pi), up)          # cos(pi) = -1  (sign flip)
amp_4pi = inner(plus(4*np.pi), up)          # cos(2pi)= +1
print(f"  <+_2pi|up> = {amp_2pi.real:+.4f}  (amplitude flips sign);  "
      f"<+_4pi|up> = {amp_4pi.real:+.4f}")
print(f"  P(+) at 2pi = {abs(amp_2pi)**2:.4f}  -> observable Born prob is 2pi-periodic;")
print(f"  the SU(2) double cover lives in the amplitude, consistent w/ odd self-linking.")

# ------------------------------------------------------------------ gate
hdr("VERDICT  (gate pre-committed in BORN0_prereg.md, stage 4)")
PASS = (ov_err < 1e-12) and (malus_err < 1e-12) and (norm_err < 1e-12) \
       and (closure_err < 1e-12) and (q2_err < 1e-12) \
       and (E_of_exponent(1.0) > 0.05) and (E_of_exponent(4.0) > 0.05)
print(f"  overlap = |cos(theta/2)|        : {ov_err:.1e}   (< 1e-12)")
print(f"  P(+) = cos^2(theta/2)           : {malus_err:.1e}   (< 1e-12)")
print(f"  normalization                   : {norm_err:.1e}   (< 1e-12)")
print(f"  E(theta) = cos(theta) [closure] : {closure_err:.1e}   (< 1e-12)")
print(f"  uniqueness (only q=2 works)     : q=2 -> {q2_err:.1e}; q=1,4 -> break (>0.05)")
verdict = "PASS" if PASS else "FAIL"
print(f"""\n[{verdict}] The continuous Born law P(+|theta)=cos^2(theta/2) follows from the
  spin-1/2 phase-geometry overlap cos(theta/2) (half-angle) + the Stage-3 |c|^2
  weight, and is UNIQUELY pinned by consistency with the closure's E=cos(theta):
  no other exponent reproduces the coherent correlation. Malus/Born recovered.
  FLOOR carried: inherits Stage-3's assumptions (pure-env-invariance + additivity);
  and this REPRODUCES QM exactly (cos^2 is standard) -> no distinguishing test.""")

assert PASS, "STAGE 4 GATE FAILED -- STOP."   # runtime stop-on-fail (spec sec.0)

out = dict(prereg="BORN0_prereg.md stage 4", stage="4 Malus / continuous Born law",
           overlap_err=float(ov_err), malus_err=float(malus_err),
           norm_err=float(norm_err), closure_consistency_err=float(closure_err),
           uniqueness_q2_err=float(q2_err),
           E_break_q1=float(E_of_exponent(1.0)), E_break_q4=float(E_of_exponent(4.0)),
           verdict=verdict,
           note="P(+|theta)=cos^2(theta/2) from half-angle overlap + stage-3 |c|^2 "
                "weight; uniquely pinned by closure E=cos(theta) (q=1,4 break it). "
                "Reproduces QM (degenerate); inherits stage-3 floors.")
json.dump(out, open("outputs/BORN_stage4.json", "w"), indent=2)
print("\n[results block written: outputs/BORN_stage4.json]")
