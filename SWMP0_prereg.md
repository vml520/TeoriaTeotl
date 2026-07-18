# SWMP0 Pre-registration — the super-Planckian decay-constant tension (SCALE0)

**Date:** 2026-07-18 (before computing). SCALE0's viable dark-energy fit required a
decay constant f ≈ 2 M_Pl — super-Planckian, a well-known swampland / distance-
conjecture concern (EFTs with super-Planckian axion decay constants are argued not to
be UV-completable in quantum gravity). This tests (a) how robust the f > M_Pl
requirement is, and (b) whether TFT's structure offers a *natural* evasion consistent
with its one-S¹ ontology.

**Honest framing.** Super-Planckian f is a generic problem for thawing quintessence,
not special to TFT. The known evasions are model-building: **clockwork/alignment**
(many coupled sub-Planckian circles → enhanced effective f) and **monodromy** (the
field winds a single circle many times → large effective field range from a
sub-Planckian period). The TFT-specific question: clockwork needs *many* circles,
which **conflicts with the one-S¹ unification** (PW0/SCALE0); monodromy uses *one*
circle wound many times, which is **native to TFT** (winding = charge = the theory's
integer). So the honest expectation is that the tension is real but *relocatable* to a
winding-number floor — not eliminated.

## Computation (pre-committed; no tuning)

1. **Robustness of f > M_Pl [compute].** Thawing needs m_φ ≲ H₀ with Λ⁴ ≈ ρ_DE =
   3Ω_Λ H₀²M_Pl². Since m_φ ∼ Λ²/f, this gives f ≳ M_Pl√(3Ω_Λ). Compute the bound and
   tabulate f vs the achievable w₀ (from the SCALE0 family). Test: is f > M_Pl forced
   for observationally-viable w₀ (≳ −0.9)?
2. **Clockwork/alignment cost [compute].** Effective enhancement f_eff = q^N f₀
   (clockwork) or f_eff = √N f₀ (alignment). Compute the number N of sub-Planckian
   circles (f₀ ~ 0.1 M_Pl) needed to reach f_eff ≈ 1.5 M_Pl. Flag: N circles breaks
   the one-S¹ ontology.
3. **Monodromy cost [compute].** One circle wound Q times gives effective range /
   flatness enhancement ~ Q·f₀. Compute the winding Q needed for f_eff ≈ 1.5 M_Pl
   from f₀ ~ 0.1 M_Pl. This is compatible with one S¹ and native to TFT (a
   winding-number input).

## Gate

- **PASS** = TFT structurally forces a sub-Planckian mechanism (no super-Planckian f
  needed) → tension resolved from within the framework.
- **PARTIAL** = f > M_Pl is robustly required (shared with all thawing quintessence),
  but TFT offers a *native* evasion — monodromy via winding the single circle Q times
  — consistent with the one-S¹ ontology, relocating the tension to a winding-number
  floor (an integer input, same class as η, r). Not eliminated.
- **FAIL** = f > M_Pl is required and TFT offers no evasion compatible with one S¹ →
  the framework inherits the full super-Planckian swampland problem with no mitigation.

**Honest prior: PARTIAL.** f ≳ 1.45 M_Pl is robust; clockwork/alignment would fix it
but need many circles (breaking one-S¹); monodromy (wind one circle Q ∼ 15 times) is
the one-S¹-compatible, TFT-native mitigation, trading super-Planckian f for a winding
floor. Monodromy has its own model-building issues; this is the most natural of the
known evasions given TFT's winding structure, not a solution. No tuning; Ω_Λ, f₀ are
inputs, the bound and costs are read out.

## Addendum — Stage 4: super-Planckian f vs R³ uncertainty (2026-07-18)

Question (Vic): does the super-Planckian tension relate to uncertainty in R³? Test
via the de Sitter quantum fluctuation of the pNGB. **Compute:** the canonical field
fluctuation δφ ~ H₀/2π (standard, light field in quasi-de Sitter), the angle
fluctuation δθ = δφ/f, and compare δφ to the R³ acceleration scale a₀ = cH₀/2π.
**Gate:** DECOUPLED = δφ is f-independent and equals a₀/c (the R³ uncertainty scale
is set by the S¹ size H₀, protected from super-Planckian f, which only shrinks δθ →
classicalizes the phase); COUPLED = R³ uncertainty grows with f (the tension leaks
into R³). Honest prior: DECOUPLED — the super-Planckian problem is confined to field
space; the R³ scale a₀ is the field's own de Sitter fluctuation and is f-independent.
