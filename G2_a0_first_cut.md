# G2 — First cut: is the field mass the Hubble mass? (self-consistency)

*Goal: derive G1's one assumption — m = ℏH₀/c² — from the field being the dark energy. Runnable check: `verify_a0_g2.py`. Outcome: mechanism works, exact coefficient does NOT (a real ~3× tension, flagged not hidden).*

## The mechanism
If the phase field's vacuum energy **is** the dark energy, it drives the expansion. Close the loop:
- field mass-gap frequency: ω₀ = c√Λ/ℓ₀
- field vacuum energy density: ρ ~ E₀Λ/ℓ₀³ (the potential-energy scale of the field)
- Friedmann (field = dark energy): H₀² = 8πGρ/(3c²)
- TFT relation: G = ℓ₀c⁴/E₀

Solve for ω₀/H₀. **Λ cancels** — the loop fixes the *ratio* of the mass gap to the Hubble rate independent of the (unknown, ~10⁻¹²²) absolute value of Λ:

> **ω₀/H₀ = √(3/8π) = 0.3455** (confirmed numerically, Λ-independent to 4 digits).

So the field being the dark energy **does** lock its mass to the Hubble scale — **m ≈ 0.35 × (Hubble mass)**. That is the substance: a₀ ~ cH₀ is a *consequence* of the field being dark energy, not a fitted parameter. And it enters through Λ (the mass gap m = √Λ/ℓ₀), exactly as Vic remembered.

## What's DERIVED
- **The relation m ~ ℏH₀/c**² (mass gap tied to the Hubble rate) — from self-consistency, **with Λ cancelling**, so *without* needing to solve the cosmological-constant problem.
- **The CC connection:** requiring m = Hubble mass gives Λ = (ℓ₀/R_H)² = 1.5×10⁻¹²² — landing on the observed cosmological-constant scale.
- So a₀ ~ cH₀ (order of magnitude + mechanism + the a₀↔Λ↔dark-energy link) is established.

## What is NOT resolved — the honest tension
The two derivation routes give **different coefficients**:
| route | a₀ | ratio to empirical (g† = 1.20×10⁻¹⁰) |
|---|---|---|
| G1 geometric (m = Hubble mass exactly → Compton freq = H₀/2π) | cH₀/2π = 1.08×10⁻¹⁰ | **0.90** ✓ |
| G2 dynamical (self-consistency → m = 0.345 × Hubble mass) | cH₀/18.2 = 3.7×10⁻¹¹ | **0.31** ✗ |

They disagree by **√(8π/3) = 2.89×**, and the dynamical route undershoots the data by ~3×.

**This trips G0 falsifier #1**: the crossover comes out ∝ cH₀ but the *coefficient* is not cleanly 1/2π — the geometric argument (which matches data) and the dynamical self-consistency (which is ~3× low) disagree. One of them carries uncontrolled O(1) factors:
- the vacuum-energy estimate ρ ~ E₀Λ/ℓ₀³ (field amplitude, exact potential normalization) is crude — plausibly wrong by O(few);
- the Friedmann 8π/3 and the crossover identification a₀ = c·(Compton freq) each carry O(1) factors.

## G2 status
- **DERIVED:** the mechanism — field-as-dark-energy self-consistently gives a₀ ~ cH₀ (Λ cancels; tied to Λ and the CC scale). a₀ is **not ad hoc**. This vindicates the core of Vic's claim.
- **NOT DERIVED:** the exact coefficient / the clean 1/2π. Geometric route matches data (0.90×); dynamical route is 3× low (0.31×). **Unresolved ~3× tension.**
- **NOT TOUCHED:** the absolute value of Λ (~10⁻¹²²) — the cosmological-constant problem, an input.

## What G3 must do
Resolve the O(1) coefficients and the 2.89× discrepancy — control the vacuum-energy normalization (field amplitude, exact potential) and the crossover factor, and determine whether the true coefficient is 1/2π (geometric, matches data) or something the dynamics forces. Until then: **a₀ ∝ cH₀ is derived; the precise 1/2π is not.**

*Honest one-liner: the framework predicts a₀ ~ cH₀ from the dark-energy field (not a free parameter, and it comes through Λ) — but the exact factor that makes it match the data to 10% is, right now, only in the geometric argument, not the dynamics; the two are 3× apart and reconciling them is the open step.*
