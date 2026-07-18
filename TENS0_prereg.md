# TENS0 Pre-registration — tensor completeness (does one S¹ field give the full 2ⁿ?)

**Date:** 2026-07-18 (before computing). The last live quantum-side question, and the
sharpest test of the framework's quantum ambition. CHSH/Born/GHZ all *reproduced* QM
— but using the abstract Hilbert space the closure *claims* to be. This asks whether
the **physical single circle-valued field**, taken as an economical (polynomial-
resource) object, actually realizes the full 2ⁿ-dimensional tensor-product Hilbert
space of n subsystems, or saturates at a restricted subspace.

**The dichotomy under test (stated honestly).** A single classical field profile is
specified by a **polynomial** number of parameters (field values on a grid / n
winding modes = O(n) complex numbers). A general n-qubit state needs **2ⁿ** complex
amplitudes. By dimension counting a polynomial-resource field cannot parametrize
generic n-body-entangled states — this is essentially the statement that efficient
classical simulation of quantum computing is impossible (BQP ⊄ P/poly). The
canonical polynomial-parameter family interpolating product → full is the
**matrix-product state (MPS)** with bond dimension χ (n·χ² params); we use χ as the
resource knob. The honest expectation: a polynomial-resource ("classical") Teotl
field is **entanglement-bounded** — it reproduces low-entanglement QM (product, GHZ,
area-law) but NOT volume-law entanglement → distinguishable from full QM by generic
deep-circuit / quantum-supremacy states. Full 2ⁿ completeness would require
**exponential** (quantized / Fock) DOF — at which point the theory is standard QFT,
not an economical classical circle-valued field. The framework cannot be both
economical-classical AND full QM.

## Computation (pre-committed; no tuning)

1. **Dimension counting [state/compute].** Field manifold dim (polynomial, ~O(n)) vs
   2ⁿ; ratio → 0. The economical-field states are a measure-zero manifold in Hilbert
   space for n ≳ few.
2. **Random-state fidelity [compute].** For Haar-random n-qubit states, compute the
   best fidelity a bond-χ (resource-bounded) representation achieves — the sum of the
   top-χ Schmidt probabilities across the central cut — vs n, for fixed χ∈{1,2,4}.
   Test whether it stays O(1) (full) or decays (restricted).
3. **Entanglement gap + why GHZ passed [compute].** Compare the entanglement entropy
   of a generic state (Page value ~ (n/2)ln2) to the bounded-χ cap (ln χ). Confirm
   GHZ carries only 1 ebit (χ=2 suffices → representable → explains the earlier GHZ
   pass) while volume-law states are NOT representable at bounded χ → the falsifiable
   gap is volume-law entanglement (quantum supremacy), not GHZ.

## Gate

- **PASS (economical field = full QM)** = a polynomial-resource (bounded-χ)
  representation keeps O(1) random-state fidelity and closes the entanglement gap as
  n grows → one S¹ field spans 2ⁿ. (Would contradict complexity theory; not expected.)
- **RESOLVED-NEGATIVE (the honest expected outcome)** = the polynomial field is
  entanglement-bounded: random-state fidelity → 0, the entanglement gap grows,
  low-entanglement states (product/GHZ/area-law) are representable but volume-law is
  not. ⇒ an economical "classical" Teotl field is a **bounded-entanglement
  subtheory** — falsified by quantum-supremacy (volume-law) experiments — and full
  tensor completeness requires quantizing the field (exponential/Fock DOF = standard
  QFT, degenerate and not economical).

**Honest prior: RESOLVED-NEGATIVE.** This is the sharpest limit on the quantum
program and I expect it to bite: "TFT-Classical," taken literally as a classical
circle-valued field, cannot reproduce generic (volume-law) entanglement; it is an
area-law/MPS-like subtheory. That is *why* CHSH/Born/GHZ passed (all low-entanglement)
and it predicts a real failure at volume-law — where nature (quantum computers) sides
with full QM. To keep full QM the field must be quantized, forfeiting the economical-
classical claim. A genuine, important negative, stated plainly, not a failure of the
test. No tuning; states are Haar-random inputs, the resource bound is the knob.
