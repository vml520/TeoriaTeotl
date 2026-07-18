# MEAS4 Pre-registration — classical limit + arrow of time (piece 4)

**Date:** 2026-07-15 (before computing). The complement to piece 3: why the world
looks classical (no macroscopic superpositions; a definite pointer basis) and why
time has a direction, given that the microscopic laws — and TFT's loop-closure —
are time-symmetric.

**Stated honestly, including where it must bottom out.** Two sub-claims, with very
different honest status:

- **Classical limit / einselection** — standard decoherence already derives the
  pointer basis (Zurek's predictability sieve: the basis that commutes with the
  system–environment interaction is robust; superpositions in it decohere) and the
  fast quantum→classical scaling with size. TFT *reproduces* this; its only added
  content is the piece-3 bridge (einselected robust states = single-valued closable
  histories). Expect: DERIVED, but essentially standard.
- **Arrow of time** — the honest, non-obvious point: the thermodynamic arrow does
  NOT come from the laws (they are T-symmetric), and it should NOT be derived from
  compact time either. Mainstream physics locates it in a low-entropy **boundary
  condition** (the past hypothesis). So the defensible TFT claims are narrow: (i) a
  *microscopic clock direction* from **energy positivity** (E>0 ⇒ phase cycles one
  way, e^{−iEt}; matter vs antimatter = opposite winding) — a real, TFT-native T-odd
  direction; (ii) recasting the past hypothesis as a low-entropy condition on the
  **loop seam**. The *thermodynamic* arrow itself is a boundary-condition floor. A
  theory claiming to *derive* the entropic arrow from its structure would be wrong
  (it would violate T-symmetry); getting a floor here is the *correct* answer.

## Computation (pre-committed; no tuning)

1. **Einselection / classical limit [compute].** System qubit + N environment
   qubits, pure-dephasing coupling H = σ_z^S Σ_j g_j σ_z^j. Show (a) the σ_z
   (pointer) basis is **robust** (its states carry no coherence to lose) while an
   X-superposition's coherence |r(t)| = ∏_j|cos(2g_j t)| decays; (b) decoherence is
   more complete with larger N (classical limit); (c) the pointer basis is the one
   commuting with H_int (predictability sieve). TFT framing: robust = closable
   (piece 3).
2. **Microscopic arrow from E>0 [compute].** Phase evolution e^{−iEt}: the winding
   rate dθ/dt = −E is T-odd, and its **sign is fixed by energy positivity**
   (spectrum bounded below ⇒ one cycling direction). Show it flips under t→−t and
   under E→−E (matter↔antimatter). This is a clock direction, NOT yet entropy.
3. **Thermodynamic arrow is a boundary condition [compute].** Entanglement entropy
   S_S(t) of the system from a low-entropy (product) state at t=0. Show
   **S_S(t) = S_S(−t)** — entropy grows in BOTH time directions away from t=0 — so
   the dynamics is time-symmetric and the arrow = the *choice* of the low-entropy
   end (past hypothesis / low-entropy seam), not a consequence of the loop.

## Gate

- **PASS** = classical limit (einselection + scaling) derived AND the
  *thermodynamic* arrow derived from compact-time structure.
- **PARTIAL** = classical limit / einselection reproduced (robust pointer basis,
  decoherence scaling, tied to piece-3 closability); a *microscopic* clock arrow
  derived from E>0; but the *thermodynamic* arrow reduces to a boundary condition
  (past hypothesis / low-entropy seam), not derived from the loop.
- **FAIL** = einselection/decoherence not reproduced, or no arrow content at all.

**Honest prior: PARTIAL — and PARTIAL is the *correct* answer, not a shortfall.**
Deriving the entropic arrow from the laws/loop would contradict T-symmetry;
mainstream physics agrees it is a boundary condition. TFT's genuine contributions
are the microscopic clock-direction (E>0, matter/antimatter winding) and the
reframing of the past hypothesis as a low-entropy loop seam; the entropic arrow
stays a floor of the same initial/boundary-condition class as η, r, and the
piece-3 selection variable λ. No tuning; couplings/energies are inputs.
