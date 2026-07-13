# BH0 Pre-registration — black holes under TFT (first study)

**Date:** 2026-07-12 (before computing). Second classical/cosmological target.
Builds on the gravity arc: gravity = emergent geometry sourced by the field's
energy (Φ ~ −M/r derived, sign+shape derived, 1PN Mercury); √(2GM/r) = the
inflow/contraction rate of space (derived), reaching c at r_s; time = phase
cycling (dτ = ℏdθ/E).

**What a black hole is in TFT (to test).** A region where (i) space flows
inward faster than phase can propagate outward (a horizon), and (ii) the field
piles up — but the phase field is BOUNDED (finite coherence length ℓ₀, finite
max amplitude), so the energy density CANNOT diverge: **no singularity, a
regular maximum-density core**. Distinctive from GR's point singularity; in the
regular-black-hole / Planck-star / gravastar family, here from the bounded
phase field.

## Computation

1. **Horizon from the phase-inflow [derived route].** The derived inflow rate
   v_in = √(2GM/r) equals c at r_s = 2GM/c². Inside, space flows in faster than
   c → outgoing phase/light is dragged inward → horizon. (River / Gullstrand–
   Painlevé model, from TFT's own inflow rate.) Report r_s(M).
2. **Time = phase cycling freezes at the horizon [structural].** g₀₀ = 1−r_s/r;
   the phase-cycling rate (= the rate of time) ∝ √g₀₀ → 0 at r_s. An external
   observer sees infalling phase FREEZE at the horizon — the literal "frozen
   star." Show the rate → 0.
3. **Singularity resolution [TFT-native prediction].** The energy density is
   capped at ρ_max ~ E₀/ℓ₀³ (= Planck density for Planckian scales) because the
   phase gradient |∇θ| ≲ 1/ℓ₀ and the amplitude are bounded. The mass sits in a
   regular core r_core ~ (3M/4πρ_max)^{1/3}. Compute r_core, ρ_max for stellar
   and supermassive M; verify r_core ≫ ℓ_Planck (a real, regular core) and
   r_core ≪ r_s (deep inside). NO singularity.
4. **Thermodynamics [scale check + open frontier].** Report the horizon-area
   entropy S = A/4ℓ_P² and Hawking T = ℏc³/8πGMk_B (these follow from the
   Schwarzschild horizon TFT reproduces); flag their DERIVATION from the TFT
   phase field (counting horizon phase configurations) as the open frontier.

## Gate

- **PASS (structural)** = TFT gives a coherent black hole: a horizon at r_s from
  its own inflow rate, a phase-freeze at the horizon, and — the distinctive
  part — a **singularity-free regular core** from the bounded phase field, with
  computed r_core; thermodynamics reproduced at the scale level with its
  derivation flagged open.
- **FAIL** = no horizon, or the density does not cap (singularity survives).

**Honest prior & scope.** PASS expected. What is TFT-NATIVE: the derivation
route (inflow→horizon, phase-freeze) and the singularity resolution (the
distinctive prediction). What is CONSISTENCY-with-GR: r_s, the thermo scales
(TFT matches GR's weak field → Schwarzschild → these follow). OPEN/floors: the
entropy/Hawking DERIVATION from TFT (the deep emergent-gravity problem); the
absolute scale (ℓ₀ = ℓ_Planck?); whether the core bounces/is stable. No tuning.
