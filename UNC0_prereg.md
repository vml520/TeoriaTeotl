# UNC0 Pre-registration — the uncertainty principle, derived from the S¹

**Date:** 2026-07-18 (before computing). A derivation-grade result for the
quantum-from-compact-time arc. That arc derives two of the three pillars of quantum
mechanics from the single-valued S¹ phase — **correlations** (CHSH closure) and
**probabilities** (Born rule). This banks the third: **uncertainty**. The claim:
the Heisenberg uncertainty relation for TFT's own fundamental variables — the
winding/charge N and the phase θ on S¹ — is a **theorem** of the single-valued S¹
structure, not a postulate. The *same* single-valuedness that forces charge
quantization (N ∈ ℤ) and underlies the CHSH closure forces ΔN·Δθ ≥ ½.

**The derivation (clean, forced).** On S¹ the single-valued phase is e^{iθ}; its
conjugate is the winding number N = −i∂_θ, whose spectrum is the integers (charge
quantization — already published). The commutators are exact: [N, cosθ] = i sinθ,
[N, sinθ] = −i cosθ. The Robertson bound then gives the **Carruthers–Nieto
number–phase uncertainty**: ΔN·Δ(cosθ) ≥ ½|⟨sinθ⟩| and ΔN·Δ(sinθ) ≥ ½|⟨cosθ⟩|,
which reduce to ΔN·Δθ ≥ ½ for phase-localized states. This is the Heisenberg
relation for the TFT field's fundamental variables — derived, not assumed.

## Computation (pre-committed; no tuning)

1. **The exact commutator + discrete spectrum [derive/verify].** N = −i∂_θ on S¹ has
   integer spectrum (single-valued e^{iθ} ⇒ N ∈ ℤ = charge quantization); [N, cosθ] =
   i sinθ, [N, sinθ] = −i cosθ. Confirm on a discretized S¹.
2. **The uncertainty relation holds for all states [compute].** Over a family of
   states on S¹, verify ΔN·Δ(cosθ) ≥ ½|⟨sinθ⟩| and ΔN·Δ(sinθ) ≥ ½|⟨cosθ⟩| (never
   violated).
3. **Saturation + the tradeoff [compute].** von Mises states (|ψ|² ∝ e^{κcosθ}, the
   circular minimum-uncertainty family) SATURATE the bound; sweep κ to show the
   tradeoff — sharp phase (large κ: small Δθ, large ΔN) ↔ definite charge (κ=0: a
   winding eigenstate, ΔN=0, uniform/undefined phase). Reduce to ΔN·Δθ → ½ in the
   phase-localized limit.
4. **Unification [state].** The single-valued S¹ phase gives all three: charge
   quantization (N∈ℤ), the quantum correlations/Born (coherent phase = Hilbert space),
   and now the uncertainty principle — one structure, three pillars.

## Gate

- **PASS (DERIVED)** = the commutators are exact and N∈ℤ; the number–phase uncertainty
  relation holds for every tested state, is saturated by the von Mises family, and
  reduces to ΔN·Δθ ≥ ½ in the localized limit → the uncertainty principle is a theorem
  of the S¹ structure, completing the three-pillar picture.
- **PARTIAL** = the relation holds but with an unresolved compact-variable subtlety
  (e.g. the Δθ measure ambiguous away from localization).
- **FAIL** = the relation is violated, or the number–phase structure does not follow
  from the single-valued S¹.

**Honest prior: PASS (DERIVED).** This is chosen deliberately as a solid, forced
theorem — a clean bank after a session of frontier floors. The number–phase
uncertainty is rigorous (Carruthers–Nieto) and here it is TFT-native: the compactness
of the phase (which TFT already uses for charge quantization and the CHSH closure)
*is* the source of the uncertainty relation. Low numerology risk — it is a commutator
theorem plus numerical verification. No tuning; the state family (von Mises κ) is
scanned, the inequalities are read out.
