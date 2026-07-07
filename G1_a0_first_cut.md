# G1 — First cut: a₀ = cH₀/2π from the field mass (Λ)

*Structural derivation. Runnable check: `verify_a0_g1.py`. Status labels inline.*

## The anchor: TFT has two fundamental rates
Time = phase cycling. Gravity's two acceleration scales are the same idea at opposite ends of scale:
- **UV:** G = ω_P²/ρ_P, ω_P = 1/t_P the Planck cycling rate. *(Result from `verify_G_as_rate.py`.)*
- **IR:** a₀ = cH₀/2π, i.e. a₀/c = H₀/2π, a *cosmological* cycling rate.
The 2π is the S¹ period in both. Deriving a₀ is the IR mirror of the G result.

## The chain (each link labeled)

**(1) Field mass gap — DERIVED.** The sine-Gordon coupling Λ gives the field a mass gap m = √Λ/ℓ₀ (the same √Λ that sets the kink mass 8√Λ and the Yukawa screening length ℓ₀/√Λ). *(Established earlier this session.)*

**(2) Cosmological identification — ASSUMED (this is the crux, → G2; and it is Vic's "α from Λ").**
The field is **ultralight**: its reduced Compton wavelength equals the Hubble radius,
> ƛ = ℏ/(mc) = c/H₀  ⟺  **m = ℏH₀/c²** (the "Hubble mass") ⟺ **√Λ/ℓ₀ ↔ ℏH₀/c²**.
This is the single physical input not yet derived. It ties Λ (the coupling) to cosmology (H₀). Numerically m = 1.5×10⁻³³ eV — exactly the cosmological-constant / ultralight scale.

**(3) Compton frequency — algebra.** The field's Compton frequency is
> f = mc²/h = ℏH₀/h = **H₀/2π**.
The 2π is literally **h/ℏ = one full S¹ cycle** (full vs reduced Compton wavelength). *This is where the 2π comes from — the S¹ geometry, not a fit.*

**(4) Crossover acceleration — the result.** An acceleration a has a characteristic frequency a/c. When a/c falls below the field's own Compton frequency H₀/2π, the acceleration is slower than the field can oscillate and the massless-like (Newtonian) response fails → modified regime. The crossover:
> **a₀ = c·f = cH₀/2π.**

## Numerical confirmation (`verify_a0_g1.py`)
- field mass = ℏH₀/c² = **1.49×10⁻³³ eV** (Hubble/Λ scale) ✓
- reduced Compton wavelength / Hubble radius = **1.0000** ✓
- a₀ = cH₀/2π = **1.08×10⁻¹⁰ m/s²**; empirical RAR g† = 1.20×10⁻¹⁰ ± 0.24(syst) → ratio **0.90** (within systematics) ✓

## Bonus — this retro-explains Stage 2 and unifies the gravity picture
The field's screening length = Compton wavelength = **Hubble radius**, which is 10⁵× a galaxy and 10¹³× the solar system. So the *same field* is **effectively massless on all sub-cosmological scales** → it gives the **1/r gravity we derived** (via the massless-Goldstone / Poisson route), and its tiny Hubble-scale mass only bites at the acceleration a₀.
> **Stage 2 failed because it used Λ ~ O(1)** — screening at the microscopic ℓ₀. The *cosmological* Λ is ultralight — screening at the Hubble radius. Same equation, right Λ: massless gravity locally **plus** a MOND crossover at a₀. Vic's memory that "α fell out of Λ" is structurally vindicated: a₀ enters through the mass gap m = √Λ/ℓ₀.

## G1 status
- **DERIVED (structural):** the *form* a₀ = cH₀/2π, with the **2π = S¹** (full Compton cycle), and the link a₀ ↔ Λ via the mass gap.
- **ASSUMED (→ G2, the gate):** the ultralight identification m = ℏH₀/c² (√Λ/ℓ₀ ↔ Hubble mass). Everything hinges on this one input.
- **ASSUMED (→ G3):** that a₀ = c·(Compton frequency) is the physical crossover (needs the field-equation mechanism, not just the scale-match).

## What G2 must do
Justify **m = ℏH₀/c²** from TFT — i.e. show the phase field's mass is set to the Hubble scale by the framework itself (candidate: self-consistency, where the field's own vacuum energy sets both H₀ and its mass — the cosmological-constant sector). If G2 can only *impose* m = Hubble mass rather than derive it, then a₀ = cH₀/2π is a **consistency relation**, not a first-principles prediction — an honest and still-useful outcome, but labeled as such.
