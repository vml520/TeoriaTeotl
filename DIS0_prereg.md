# DIS0 Pre-registration — the distinguishing observable (compact-time TFT vs QM)

**Date:** 2026-07-15 (before computing). The one open prize left by the QC arc:
CHSH-CLOSURE and BORN0 both **reproduce QM exactly** (2√2; cos²(θ/2)) → neither can
distinguish compact-time TFT from standard QM. This study asks whether ANY
observable separates them, and — crucially — whether such an observable is
**scale-independent** (falsifiable at any loop size = the real prize) or its size
is **set by the compact-time period T** (exists in principle, unobservable if T is
the cosmological S¹ that TFT's a₀/dark-energy sector fixes).

**Why any signal must come from finite T (stated honestly).** The closure gets QM
by demanding the S¹ phase be single-valued; in the large-loop limit T→∞ compact
time → open time → standard QM. So a distinguishing signal can only come from the
*finite* compactness. Two structurally different channels are tested:

- **Spatial / Bell channel** — does discretizing/compactifying the time circle
  change the entanglement correlation E(a,b)? Prior: NO — the closure's hidden
  phase *cancels* (it appears only as a difference), so the correlation should be
  insensitive to the circle's granularity. If confirmed, CHSH is degenerate at
  *any* loop size (strengthening the numerical 2√2 to a structural statement).
- **Temporal / energy channel** — compact real time of period T forces
  single-valuedness e^{−iET}=1 ⇒ **energy is quantized, Eₙ = 2πn/T** (a comb;
  the Matsubara analogue for real time), and ⇒ **exact periodic revival at T** for
  any state. Standard QM (time = ℝ): energy continuous, generic states never
  exactly revive. This is where compactness = discreteness must bite, if anywhere.

## Computation (pre-committed; no tuning)

1. **Bell channel [compute].** Build the closure correlation on a time circle
   discretized to N points, E_N(a,b); sweep N∈{2,3,5,10,10³}. Test E_N vs cos(a−b)
   and CHSH S_N vs 2√2. Prior: E_N = cos exactly, N-independent (hidden phase
   cancels) ⇒ this channel cannot distinguish, at any loop size.
2. **Energy/temporal channel [compute].** (a) Show single-valuedness on period T
   forces Eₙ = 2πn/T; the distortion needed to snap an arbitrary target energy
   onto the comb is δE ≤ π/T. (b) Revival: a 3-level system with *incommensurate*
   energies (1,√2,√3) — QM autocorrelation A(t)=⅓Σe^{−iEₙt} is quasiperiodic,
   max|A|<1 over any window (never exact revival); compact time snaps Eₙ onto the
   comb ⇒ A(T)=1 exactly. Compute the QM revival deficit and how the snap
   distortion δE/E scales with T. Also test **time-winding interference** (phases
   differing by a full loop): phase per winding = 2πn ⇒ e^{i2πn}=1 ⇒ prior: no
   observable difference (windings degenerate).
3. **Scale/feasibility [scoping, not a gate].** Insert TFT's own S¹ period. (a)
   Cosmological T = 2π/H₀ ⇒ comb spacing ΔE = ℏH₀; revival time ~1/H₀. (b)
   Microscopic (Compton) T = 2π/ω_C ⇒ energies in units of mc². Assess each
   against data (continuously-tunable lab spectra exist to high precision).

## Gate

- **PASS (the prize)** = a distinguishing observable that is **order-1 /
  T-independent** — does not vanish as T→∞ — hence falsifiable at any loop size.
- **PARTIAL** = a real distinguishing observable exists (energy comb / exact
  revival / forbidden frequencies) but its **magnitude is set by 1/T**; at the T
  consistent with observed continuous spectra it is unobservable → *distinguishable
  in principle, empirically degenerate in practice.* Report the sharpest
  in-principle falsifier and the bound on T it already implies.
- **FAIL** = compact time equals QM **exactly** on all computed observables (no
  comb, no revival difference, Bell degenerate) → no distinguishing observable
  here; the prize, if it exists, is elsewhere.

**Honest prior, flagged up front: PARTIAL.** Expectation: the Bell channel is
exactly degenerate (structural), and the temporal channel *does* differ (energy
comb, exact revival) but the difference scales as 1/T. At TFT's cosmological S¹
(T~1/H₀) the comb spacing is ~10⁻³³ eV and the revival time ~ the age of the
universe — unobservable; a microscopic T is excluded because it would quantize
energies in units of mc² (contradicting eV-scale atomic spectra). If so, the
sharpest honest statement is: *compact-time TFT predicts forbidden transition
frequencies between comb teeth; observed continuous spectra bound T ≳ 1/H₀,
already satisfied — the theory is empirically degenerate with QM for any feasible
experiment.* A PASS (T-independent separation) is the hoped-for surprise; the
computation, not the prior, decides. No tuning; energies and settings are inputs,
deviations are read out.

## Addendum — Stage 4: multipartite contextuality (GHZ / Mermin), 2026-07-15

A different kind of distinguisher: not whether compact-time TFT *exceeds* QM, but
whether it *falls short*. GHZ (3 qubits, |000⟩+|111⟩) gives all-or-nothing
contextuality — QM reaches Mermin **M=4** (LHV bound 2), and the correlations are
**irreducible to 2-body** (all pairwise correlations vanish). Test whether the
coherent-phase closure, extended to 3 parties, reproduces M=4 or is stuck lower.

**Compute:** (i) QM/coherent-closure E(φₐ,φᵦ,φ_c)=⟨GHZ|σ(φₐ)σ(φᵦ)σ(φ_c)|GHZ⟩ built
from the closure's own primitive (σ(φ)=phase read relative to setting); verify it
= cos(φₐ+φᵦ+φ_c), the GHZ paradox values, hidden-phase cancellation (no-signaling),
and Mermin M. (ii) LHV bound (brute ±1 assignments). (iii) a **2-body-only**
model (GHZ has zero pairwise correlations) to show genuine 3-body coherence is
required.

**Gate:** **DISTINGUISHER (PASS)** = the closure cannot reach M=4 (stuck ≤2, LHV-
like) → TFT falls short of QM contextuality → falsifiable, and refuted by real GHZ
experiments. **DEGENERATE** = closure reaches M=4 = QM → GHZ reproduced, no
distinguisher (but confirms TFT captures irreducible multipartite contextuality,
not just 2-body). Honest prior: DEGENERATE if the S¹ closure delivers full
tensor-product coherence (CHSH established 2-body; 3-body via the same mechanism);
the open sub-question is whether the single-field construction genuinely gives the
full 2ⁿ-dim tensor space — if it saturates at 2-body, GHZ is the falsifier.
