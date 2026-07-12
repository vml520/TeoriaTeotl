# SPEC0 Pre-registration — the merged-soliton internal spectrum (frontier)

**Date:** 2026-07-12 (drafted BEFORE the spectrum computation). Continuation of
SINT, which pinned r's seat to the single merged three-fold soliton interior.

**Question:** compute the actual internal fluctuation spectrum of the TFT
Q-ball (Bogoliubov–de Gennes, resolved by angular momentum ℓ), and ask whether
it contains a **three-fold (Z₃) bound internal mode** that can be the
generation dial — the concrete carrier of the M-program's δ and hence r.

## Method (no free knobs)

Linearize the complex field ψ = e^{iωt}(f(r) + σ + iτ) around the Q-ball
background f (repo potential V(ρ)=½ρ²−ρ⁴+ρ⁶, ω inherited). The amplitude (σ)
and phase (τ) fluctuations obey, per angular momentum ℓ and frequency Ω:
  (L_σ + Ω²)σ = −2ωΩ τ ,  (L_τ + Ω²)τ = −2ωΩ σ
  L_σ = ∇²_ℓ − V''(f) + ω²  = ∇²_ℓ − (1 − 12f² + 30f⁴) + ω²
  L_τ = ∇²_ℓ − V'(f)/f + ω² = ∇²_ℓ − (1 − 4f²  + 6f⁴ ) + ω²
solved as a companion eigenproblem. Continuum threshold Ω_c = 1 − ω; bound
modes have real Ω in (0, Ω_c) with a localized eigenvector.

**Validation (must pass or the solver is untrusted):**
- ℓ=0 phase channel has an exact Ω=0 mode (U(1) Goldstone: L_τ f = 0).
- ℓ=1 has an Ω≈0 mode (translation zero mode ∝ ∂_r f).

## Gate (pre-committed)

- **PASS (structural)** = a three-fold (ℓ=3) bound internal mode EXISTS — the
  generation dial is concretely identified as a real vibrational mode of the
  merged soliton; report its frequency and the full low-ℓ spectrum.
- **STRONG PASS** = additionally, the spectrum fixes r with no free continuous
  parameter (not expected; r needs the mode's finite-amplitude condensate).
- **FAIL** = no ℓ=3 bound mode → the three-fold dial is not an internal
  vibration of the single Q-ball, redirecting again (higher charge / genuinely
  different topology).

**Honest prior:** the ℓ=3 mode is a *surface/shape* oscillation — bound only if
the ball is thin-wall (large). Likely bound at ω=0.78 (R≈33), possibly not at
compact ω. Whether it is bound is a real, falsifiable outcome. Even a PASS
leaves r open (its value = the mode's nonlinear condensate amplitude), so the
expected end state is "dial identified, r's carrier concrete, value still on
the nonlinear wall." No tuning; ω stated; the ℓ ordering is the physics.
