# BHE0 Pre-registration — black-hole entropy from the phase field

**Date:** 2026-07-13 (before computing). The deepest black-hole target; flagged
as the frontier where every emergent-gravity program strains. Splits into two
honestly-separated pieces.

**The two pieces of S = A/4ℓ_P².**
1. **The AREA LAW (S ∝ A, not volume) — the holographic surprise.** This IS
   derivable and TFT-native: the black-hole entropy is the **entanglement
   entropy of the phase field's massless Goldstone mode** across the horizon.
   Entanglement is a *boundary* effect (short-range correlations across the
   cut), so S ∝ boundary area — Srednicki's 1993 mechanism, applied to TFT's
   own field. Computable on a lattice.
2. **The coefficient 1/4.** In INDUCED / emergent gravity (Sakharov 1967,
   Jacobson, Susskind–Uglum — TFT's lineage), the SAME field fluctuations that
   give S_ent ∝ A/ε² also induce 1/G ∝ 1/ε²; the ε-divergences CANCEL in the
   ratio → S_ent = A/4G. So the 1/4 is **inherited and constrained** (tied to G
   via one field), not a free fit — but computing it *exactly* needs the phase
   field's full induced-G spectrum. This is the strain point.

## Computation

1. **Area law [computed].** Discretize the phase Goldstone (free massless
   scalar) on a radial lattice; for each angular momentum ℓ build the coupling
   matrix, form the Gaussian ground state (X=½K^{-1/2}, P=½K^{1/2}), trace out
   r>R, get the symplectic eigenvalues, and sum the entanglement entropy over ℓ
   (weight 2ℓ+1). Prediction: **S(R) ∝ R² (area), not R³ (volume)** — fit the
   exponent.
2. **The coefficient [structural].** State the induced-gravity cancellation
   S_ent = A/4G and the identity that S = s₀·A/ℓ_P² matches A/4ℓ_P² iff the
   entropy per Planck cell s₀ = 1/4 nat. Reproduce the magnitude (~10⁷⁷ solar).
3. **Verdict split** clearly: area law DERIVED (computed), 1/4
   inherited-in-principle from induced gravity (constrained, not free), exact
   coefficient = the frontier floor.

## Gate

- **PASS (structural, honest split)** = the area law is COMPUTED from the phase
  field's entanglement (exponent ≈ 2, area not volume), and the 1/4 is located
  precisely as the induced-gravity coefficient (constrained by G, exact value a
  floor). This is the honest state of the art — no framework does better on the
  coefficient from first principles without a tunable input.
- **FAIL** = the entanglement entropy comes out volume-law (∝ R³), or the 1/4
  is claimed as freely derived (overclaim).

**Honest prior & scope.** PARTIAL-PASS expected: area law is real and
computable; the 1/4 is a constrained floor (like the Immirzi parameter in LQG,
the microstate count in strings). OPEN: the exact coefficient from the phase
field's induced-G spectrum; the absolute scale (ℓ₀=ℓ_P?). No tuning; the
lattice scalar is parameter-free.
