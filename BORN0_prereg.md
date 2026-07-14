# BORN0 Pre-registration — the Born rule from the compact-time closure

**Date:** 2026-07-14 (before computing). Direct successor to CHSH-CLOSURE
(`chsh_closure.py`, DERIVED), which left exactly one QC-side hole: the S¹
single-valued phase gives the right *correlations* coherently — E(a,b)=cos(a−b),
Tsirelson-capped, no-signaling — but that single-outcome *probabilities* follow
**|ψ|²** was not shown. This registers that derivation.

**The claim under test (stated honestly).** In compact-time TFT the probability
of a measurement outcome k is the **conserved U(1) Noether charge in channel k**,
P(k) = |⟨k|ψ⟩|² / ⟨ψ|ψ⟩. Two independent pillars are supposed to *force* this,
neither newly postulated:

1. **Quadratic is structural, not chosen.** ψ is a single-valued *complex* phase
   field. Its physically meaningful, positive, conserved density is the U(1)
   Noether charge j⁰ = |ψ|² — the *same* winding-charge density that already gave
   integer charge quantization elsewhere in the program. "How much field sits in
   channel k" is a sesquilinear (quadratic) form in the field *by what a complex
   amplitude means* — not a fitted exponent. Coherent additivity across channels
   is already DERIVED in the closure (Hilbert-space inner product).

2. **Equal amplitudes ⇒ equal weights by an exact symmetry (envariance).** For an
   entangled two-channel state c₀|0⟩|e₀⟩ + c₁|1⟩|e₁⟩ with |c₀|=|c₁|, a
   relative-phase-and-swap operation on the S¹ field is an exact symmetry that
   leaves the local marginal invariant ⇒ the two outcomes *must* be equiprobable
   (Zurek envariance, realized as a symmetry of the TFT field — not an assumption).
   Fine-graining unequal (rational) weights into equal-amplitude sub-channels
   extends this to |c_k|² for all amplitudes; continuity covers irrationals.

**The compact-time role.** The outcome ensemble is the field's phase sampled
around the S¹ time loop. Its invariant (Haar/translation-invariant) measure on
the circle is uniform — so the "typicality measure" is *fixed by the S¹ geometry*,
not chosen. This is the one place TFT claims to do better than a generic
hidden-variable typicality postulate.

## Computation (all stages pre-committed; no field written by hand — §0)

1. **Baseline symmetry [compute].** Build the two-channel S¹ field with |c₀|=|c₁|.
   Exhibit the phase-swap operation and verify numerically it leaves the local
   marginal invariant ⇒ P(0)=P(1)=½ *forced by symmetry*, not by inserting |c|².
2. **The measure [compute].** For ψ = c₀|0⟩ + c₁|1⟩, compute the outcome frequency
   as the uniform-over-S¹-hidden-phase fraction landing in channel 0, sweeping
   |c₀|² ∈ (0,1). Test: frequency = |c₀|² across the whole sweep (not |c₀|¹, |c₀|⁴).
3. **Envariance extension [compute].** Realize a rational weight p=m/n by fine-
   graining into n equal sub-channels; confirm the symmetry argument returns
   exactly |c_k|² with no free exponent, independent of n.
4. **Sharpest Born test — Malus [compute].** Projective measurement of a single
   winding at relative angle θ. From the charge overlap of the S¹ phase geometry,
   test P(+|θ) = cos²(θ/2) across θ ∈ [0,π]. This is the quantitative Born law.
5. **Closure-consistency [compute].** Verify the *same* coherent-phase structure
   that produced E(a,b)=cos(a−b) in `chsh_closure.py` reproduces these single-
   outcome marginals (no second, incompatible mechanism smuggled in).

Each stage writes a results block before the next begins; stop-on-fail in-script.

## Gate

- **PASS** = outcome probabilities come out **|c_k|²** (Stage 4: Malus cos²(θ/2))
  with **no tunable exponent**, the quadratic *forced* by the U(1)/coherent-phase
  structure, AND equal amplitudes → equal weights by the *exact* swap symmetry
  (Stage 1), extended non-contextually to all amplitudes (Stage 3).
- **PARTIAL** = the swap symmetry forces the equal-amplitude case and the quadratic
  measure is natural + numerically consistent, but exponent 2 rests on *choosing*
  the U(1) charge as the measure (vs. another invariant functional) rather than
  TFT forcing that choice → Born rule **consistent with, not forced by** the
  closure. Report which assumption remains.
- **FAIL** = the S¹ measure yields a non-Born exponent (|c|¹, |c|⁴, …) or the
  equal-amplitude swap symmetry does not hold.

**Honest prior & scope (flagged up front).** Likely outcome: **PARTIAL**. The
genuinely forced pieces are strong — (a) equal-amplitude equiprobability is a real
symmetry (envariance), and (b) the *quadratic* is natural because the conserved
U(1) density is sesquilinear and coherent additivity is already DERIVED. The
residual floor is the classic one: *why empirical measurement frequency equals the
abstract S¹ measure* (the typicality→frequency identification). TFT narrows this
more than generic hidden-variable theories — the compact circle's invariant
measure is uniform by translation symmetry, not chosen — but "the field spends
S¹-proper-time in proportion to charge, and that equals what a detector counts"
is an identification, not yet a theorem. **Degeneracy caveat:** like CHSH, a
successful Born derivation *reproduces* QM → it cannot by itself distinguish
compact-time TFT from standard QM; a distinguishing observable remains the real
prize (untouched here). **No parameter tuning** — c₀,c₁,θ are scanned inputs, the
measure is the field's own U(1) charge, the exponent is read out, never set.
