# MEAS3 Pre-registration — single-outcome selection by S¹ loop-closure (piece 3)

**Date:** 2026-07-15 (before computing). The measurement problem's hardest piece:
why a superposition yields ONE definite outcome. BORN0 gave the *probabilities*
(|c_k|²) but was agnostic between "one outcome with those odds" and "all outcomes
(branches) with those weights." This tests TFT's distinctive claim: on a **closed
time loop**, single-valuedness (the phase must close on itself) is a
self-consistency condition that (a) admits only *definite* branches as closed
histories — forbidding macroscopic superpositions — and (b) selects the one
realized outcome via the loop's seam phase, with Born frequencies.

**The mechanism, stated honestly (and where it likely bottoms out).** TFT does not
replace decoherence — it *completes* it. Decoherence (system coupled to an
environment/pointer) already derives the pointer **basis** and drives the
superposition's coherence → 0 (einselection), but yields an *improper mixture* —
it never says which outcome is actual (this is the residual measurement problem).
TFT's addition: single-valuedness on S¹ means the realized history must **close**;
a decohered branch closes as a definite history, a coherent "cat" of
macroscopically-distinct branches **cannot** close as one single-valued object
(its branches need incompatible seam phases). The seam phase λ (the loop-closure
hidden variable, uniform/Haar) then picks *which* branch closes, with measure
|c_k|² (BORN0). Likely floor: the *value* of λ per run is a boundary condition —
not derived. So the honest target is: definiteness + basis + Born-consistency
DERIVED; "which outcome is actual" reduced to a deterministic, empirically
invisible (CHSH-closure) hidden variable — collapse reframed as loop-closure, not
conjured away.

## Computation (pre-committed; no tuning)

1. **Definiteness / anti-cat [compute].** System qubit ⊗ n environment modes;
   measurement imprints outcome-dependent phases. Compute the coherent "cat"
   closure amplitude C(n) = ∏_j |⟨p_j^(0)|p_j^(1)⟩| (the off-diagonal that a
   single-valued closed history must preserve). Test: C(n) → 0 as n grows
   (macroscopic superpositions excluded as closed histories) while each *definite*
   branch closes with amplitude 1 → the closed histories ARE the definite pointer
   outcomes. This is the quantum→classical boundary as loop-closability.
2. **Deterministic selection + Born consistency [compute].** Map the seam phase
   λ∈[0,2π) → a single outcome via the BORN0 charge measure (arcs of length
   2π|c_k|²). Verify (a) exactly ONE outcome per λ (definiteness, no branching),
   and (b) over uniform λ the selection frequencies = |c_k|² (consistency with
   BORN0). Report outcomes-realized-per-run = 1 (vs MWI's "all").
3. **Invisibility of the hidden variable [compute].** Confirm the selection
   variable λ cancels from correlations (marginals independent of λ's role) — so
   this determinism reproduces QM statistics (ties to CHSH-closure): the mechanism
   adds ontology (a definite world) without adding any signaling or new statistics.

## Gate

- **PASS** = single-valuedness dynamically selects **definite** pointer outcomes
  (cat closure C(n)→0, definite branches close), AND the loop-phase λ gives a
  single outcome per run with Born (|c_k|²) frequencies, empirically invisible —
  reframing collapse as deterministic loop-closure with NO physical collapse and
  NO branching, fully consistent with BORN0 + CHSH-closure.
- **PARTIAL** = definiteness + basis + Born-consistency hold, but the *actuality*
  of one branch still rests on positing λ's value per run (a boundary-condition
  floor) → collapse is converted to a deterministic hidden-variable selection, not
  eliminated. (This is a genuine reframing, honestly bounded.)
- **FAIL** = single-valuedness does NOT select definite outcomes (cat closes as
  well as definite branches; no basis; no λ→single-outcome map) → loop-closure
  does not dissolve definiteness.

**Honest prior: PARTIAL.** Expectation: definiteness/basis emerge (decoherence-as-
closure, C(n)→0) and Born frequencies follow from BORN0's measure, but "which
outcome" = the loop-seam hidden variable λ, whose per-run value is an
initial/boundary-condition floor (same class as η, r). That is not a failure but
the honest endpoint: TFT recasts the measurement problem's *definiteness* as a
consequence of physical closed time, and its *randomness* as a deterministic,
provably-invisible hidden variable — leaving only "why this λ," which no dynamics
supplies. No tuning; amplitudes and phases are inputs, the selection is read out.
