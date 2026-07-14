"""BORN0 Stage 1 -- equal amplitudes => equal weights by EXACT symmetry.
Pre-reg: BORN0_prereg.md, stage 1. Follows chsh_closure.py (the closure DERIVED
that the compact-time S^1 coherent phase = a Hilbert space; we work in it).

Claim tested: for an entangled two-channel state (two winding sectors of the
S^1 phase field) entangled with an environment ("which-sector" record),
   |psi> = c0 |0>_S|e0>_E + c1 |1>_S|e1>_E,
the system SWAP U_S (0<->1) can be undone by a PURELY ENVIRONMENTAL unitary U_E
IF AND ONLY IF |c0| = |c1|.  Because a purely-environmental op cannot change any
probability local to S, envariance then FORCES P(0)=P(1) -- with NO use of |c|^2.
The control (unequal moduli => U_E non-unitary) proves the argument discriminates.
"""
import json
import numpy as np

def hdr(s): print("\n" + "=" * 70 + "\n" + s + "\n" + "=" * 70)

I2 = np.eye(2, dtype=complex)
U_S = np.array([[0, 1], [1, 0]], dtype=complex)      # system swap 0<->1

def C_of(c0, c1):                                     # Schmidt-diagonal state matrix
    return np.array([[c0, 0], [0, c1]], dtype=complex)

def required_UE(C):
    """The environment op that must undo U_S:  U_S C U_E^T = C  =>  U_E=(C^-1 U_S C)^T.
    (U_S is its own inverse.)  Returns U_E; unitarity of U_E is the crux."""
    return (np.linalg.inv(C) @ U_S @ C).T

def unitarity_defect(U):
    return np.linalg.norm(U @ U.conj().T - I2)

def restore_residual(C, UE):
    return np.linalg.norm(U_S @ C @ UE.T - C)         # global state exactly restored?

# ------------------------------------------------------------------ Stage 1a
hdr("1a  EQUAL moduli (various phases): environment counter-swap is UNITARY")
print("state |psi> = c0|0>|e0> + c1|1>|e1>;  test U_S undone by a pure-E unitary.")
equal_cases = []
for (ph0, ph1, label) in [(0.0, 0.0, "real, equal"),
                          (0.4, 1.1, "phases 0.4,1.1"),
                          (-2.0, 0.7, "phases -2.0,0.7")]:
    c0 = np.exp(1j * ph0) / np.sqrt(2)
    c1 = np.exp(1j * ph1) / np.sqrt(2)                 # |c0|=|c1|=1/sqrt2 exactly
    C = C_of(c0, c1)
    UE = required_UE(C)
    ud, rr = unitarity_defect(UE), restore_residual(C, UE)
    print(f"  {label:16s}: |c0|={abs(c0):.4f} |c1|={abs(c1):.4f}  "
          f"U_E unitarity-defect={ud:.2e}  restore-residual={rr:.2e}")
    equal_cases.append((label, ud, rr))
max_ud = max(u for _, u, _ in equal_cases)
max_rr = max(r for _, _, r in equal_cases)

# ------------------------------------------------------------------ Stage 1b
hdr("1b  CONTROL -- UNEQUAL moduli: the counter-swap is NOT unitary")
print("if envariance held for any amplitudes it would be vacuous; it must FAIL here.")
control = []
for p0 in [0.6, 0.7, 0.9]:                            # |c0|^2 = p0 (label only)
    c0 = np.sqrt(p0); c1 = np.sqrt(1 - p0)             # real, UNequal moduli
    UE = required_UE(C_of(c0, c1))
    ud = unitarity_defect(UE)
    offmag = abs(UE[0, 1])                             # = |c0/c1|, != 1 when unequal
    print(f"  |c0|^2={p0:.2f}: U_E unitarity-defect={ud:.3f}  |U_E offdiag|={offmag:.4f}"
          f"  (unitary needs 1.0000)")
    control.append((p0, ud))
min_control_defect = min(d for _, d in control)

# ------------------------------------------------------------------ the argument
hdr("1c  the envariance argument  =>  P(0)=P(1), with NO |c|^2 inserted")
print("""(1) A purely-ENVIRONMENTAL unitary U_E acts only on E, so it cannot change
    any probability of a measurement local to the system S.
(2) For EQUAL moduli (1a) there IS a unitary U_E with U_S C U_E^T = C: the pure
    system swap 0<->1 is exactly undone by an environment-only operation. So the
    swapped state and the original differ ONLY by U_E acting on E.
(3) Therefore relabeling 0<->1 leaves every S-local probability unchanged
    => P(0) = P(1).  Nowhere did we form |c0|^2; the equality is a SYMMETRY.
(4) Control (1b): for unequal moduli NO such unitary exists, so the argument does
    not force equality there -- exactly as it must (that case isn't equiprobable).""")

# consistency note (labeled: NOT used to derive the equality above)
rhoS = C_of(1/np.sqrt(2), 1/np.sqrt(2)) @ C_of(1/np.sqrt(2), 1/np.sqrt(2)).conj().T
print(f"[consistency only] reduced-state diagonal for equal case = "
      f"{np.real(np.diag(rhoS)).round(4)}  (= 1/2,1/2; consistent w/ |c|^2, "
      f"but derived above from symmetry, not assumed)")

# ------------------------------------------------------------------ gate
hdr("VERDICT  (gate pre-committed in BORN0_prereg.md, stage 1)")
PASS = (max_ud < 1e-12) and (max_rr < 1e-12) and (min_control_defect > 1e-3)
print(f"equal-moduli max U_E unitarity-defect = {max_ud:.2e}   (< 1e-12 required)")
print(f"equal-moduli max restore-residual     = {max_rr:.2e}   (< 1e-12 required)")
print(f"control min unitarity-defect          = {min_control_defect:.3f}   (> 1e-3 required)")
verdict = ("PASS" if PASS else "FAIL")
print(f"\n[{verdict}] Equal-amplitude equiprobability is FORCED by an exact envariance "
      f"symmetry\n  of the S^1 field (counter-swap unitary iff |c0|=|c1|), independent of "
      f"phases,\n  with NO |c|^2 inserted. Discriminates correctly (control fails). This "
      f"fixes\n  ONLY the equal-amplitude case; unequal amplitudes -> Stage 3 (fine-graining).")

# stop-on-fail at runtime (spec sec.0), not logged after the fact
assert PASS, "STAGE 1 GATE FAILED -- STOP. Envariance symmetry did not hold as pre-registered."

out = dict(prereg="BORN0_prereg.md stage 1", stage="1 envariance / equal-amplitude",
           equal_max_unitarity_defect=float(max_ud),
           equal_max_restore_residual=float(max_rr),
           control_min_unitarity_defect=float(min_control_defect),
           verdict=verdict,
           note="P(0)=P(1) DERIVED from exact envariance symmetry (pure-environment "
                "counter-swap unitary iff |c0|=|c1|), phase-independent, no |c|^2 used. "
                "Equal-amplitude case only; unequal amplitudes deferred to stage 3.")
json.dump(out, open("outputs/BORN_stage1.json", "w"), indent=2)
print("\n[results block written: outputs/BORN_stage1.json]")
