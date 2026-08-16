# G3 — Controlling the vacuum-energy normalization

*Goal: does the coefficient in a₀ = (coeff)·cH₀ come out at 1/2π when the O(1) factors are done properly? Runnable check: `verify_a0_g3.py`. Outcome: the 2π is clean; the residual is a cosmological O(1), not a first-principles constant.*

## The proper calculation
The sine-Gordon potential-energy density is axion-like:
> u_V(θ) = (E₀Λ/ℓ₀³)(1 − cos θ) ≡ μ⁴(1 − cos θ).

Two distinct quantities come from it:
- **Mass gap** (curvature at θ=0): ω₀ = c√Λ/ℓ₀. **Fixed**, independent of where the field sits. This is what enters a₀ = c·(Compton frequency) = c·ω₀/2π. **The 2π is h/ℏ = one full S¹ cycle — clean, and not the source of any discrepancy.**
- **Dark-energy density** = the potential *height* at the field's current position θ_i: ρ_DE = μ⁴(1 − cos θ_i). This depends on **θ_i** — a cosmological quantity (how far the ultralight field has rolled).

Friedmann H₀² = 8πGρ_DE/(3c²Ω_DE) with G = ℓ₀c⁴/E₀. **Λ cancels.** The result:

> **a₀ = (cH₀/2π) · √( 3 Ω_DE / (8π(1 − cos θ_i)) ).**

The bracket is exactly **ω₀/H₀** — how close the field mass is to the Hubble mass.

> **Correction (15 August 2026) — two amendments to this derivation, one numerical.**
>
> **(1) Ω_DE was missing.** This page previously wrote the Friedmann equation as
> H₀² = 8πGρ_DE/(3c²), which is dark energy as the *only* component — i.e. Ω_DE = 1. The universe
> has Ω_DE ≈ 0.685. Carrying it multiplies the bracket by √Ω_DE, so **the old expression overstated
> ω₀/H₀ by 1/√Ω_DE ≈ 1.21, a 21% error.** The table below has been recomputed and the
> data-preferred θ_i moves from **0.44 rad to 0.353 rad**. *`SWMP0_prereg.md` already carried the
> correct form (f ≳ M_Pl√(3Ω_Λ)); this page was the one out of step, and the repo now agrees with
> itself.*
>
> **(2) "with G = ℓ₀c⁴/E₀" does not eliminate the decay constant — it fixes it.** Written in
> standard variables the same steps give ω₀ = μ²/f and
> **ω₀/H₀ = (M_Pl/f)·√(3Ω_DE/(1 − cos θ_i))**. The amplitude μ cancels — that part of the claim
> above is correct and survives — **but f does not.** The boxed result is recovered if and only if
> **f = √(8π)·M_Pl = M_Planck (non-reduced)**. So the primitive notation ω₀ = c√Λ/ℓ₀ is
> *equivalent to* setting the decay constant to the Planck mass; it does not remove it. This is
> stated so the notation does not carry it silently.
>
> **Neither amendment touches the headline.** a₀ = cH₀/2π is the value *at* ω₀ = H₀, whatever Ω_DE
> is; what moves is the (f, θ_i) pair that satisfies that condition. **The 2π and the ∝ cH₀
> scaling are unaffected, and the honest verdict below is unchanged in substance** — the residual
> is still a cosmological O(1) rather than a first-principles constant. If anything the floor is
> now slightly steeper: a generic θ_i ~ O(1) is **~4× low**, not ~3×.

## What this says (measured, `verify_a0_g3.py`)
*Recomputed 15 August 2026 with Ω_DE = 0.685 carried (see the correction above). The
superseded Ω_DE = 1 values are kept alongside so the change is auditable.*

| θ_i | ω₀/H₀ (old, Ω_DE=1) | **ω₀/H₀ (corrected)** | **a₀ (corrected)** | **a₀/emp** |
|---|---|---|---|---|
| π/2 (generic O(1)) | 0.345 | **0.286** | **2.98×10⁻¹¹** | **0.25** |
| 0.44 rad (old preferred) | 1.12 | **0.926** | **9.66×10⁻¹¹** | **0.80** |
| **0.353 rad (~20°) — now the data-preferred value** | 1.39 | **1.151** | **1.20×10⁻¹⁰** | **1.00** |
| π | 0.244 | **0.202** | **2.11×10⁻¹¹** | **0.18** |

The data (a₀ = 1.20×10⁻¹⁰) corresponds to **θ_i ≈ 0.353 rad**, i.e. **ω₀ ≈ H₀ — the field mass ≈ the Hubble mass.** That is precisely the standard quintessence "thawing" condition: a scalar becomes dynamical when its mass drops to the current Hubble rate. So the data-preferred value is *physically the expected one*, not an arbitrary fit.

## Honest verdict
- **The 2π is DERIVED** — geometric (Compton frequency, h/ℏ, S¹). It was never the problem.
- **a₀ ∝ cH₀ is DERIVED** — mechanism (field = dark energy), Λ cancels, tied to the CC scale.
- **The exact coefficient is NOT uniquely fixed.** It is ω₀/H₀ = √(3Ω_DE/(8π(1−cosθ_i))), an **O(1) set by the field's cosmic position θ_i**. Quintessence *naturally* puts ω₀ ~ H₀ (mass ~ Hubble mass, becoming dynamical now), which gives a₀ ~ cH₀/2π and matches data. But a *generic* θ_i ~ O(1) gives ~4× low. So the coefficient is **natural and consistent with data, not first-principles-forced.**

**This does not fully clear G3.** Attacking the normalization did not turn the coefficient into a pure constant; it revealed that the residual factor is **a real cosmological quantity** (the dark-energy field's position / equation of state), which the data pins to the natural "m ≈ H₀" value. That is *not* a free knob we tuned — it's ω₀/H₀, physically ~1 for quintessence — but neither is it derived from nothing.

## Where the a₀ program stands (G1–G3)
- **a₀ ∝ cH₀** — DERIVED. Not ad hoc (contra MOND). Comes through Λ, via the field being dark energy. ✓ (Vic's core claim.)
- **The 2π** — DERIVED (S¹/Compton), *given* m = Hubble mass.
- **m = Hubble mass** — the natural quintessence condition (m ~ H₀); the exact coefficient carries an O(1) tied to the field's position, which data fixes to the thawing value. **Natural, consistent, not uniquely predicted.**
- **|Λ| ~ 10⁻¹²²** — the cosmological-constant problem, untouched.

**One-liner:** a₀ ~ cH₀ with the 2π from S¹ is real and predicted; matching the data to 10% requires the ultralight field to have mass ≈ the current Hubble rate — the standard "dark energy becoming dynamical now" condition — which is natural but is a cosmological input, not a derived constant. **Deriving a₀ exactly = deriving why dark energy is dynamical now = the coincidence problem.** That is the honest floor.
