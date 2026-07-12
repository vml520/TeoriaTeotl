# SPEC0b Pre-registration — the nonlinear ℓ=3 condensate (frontier)

**Date:** 2026-07-12 (before computing). Continuation of SPEC, which found the
ℓ=3 "triangular" bound mode = the generation-dial carrier. Goal: condense it
at finite amplitude and try to read the dial potential V(δ) → r.

**Sharp risk flagged up front:** the *spatial orientation* of a single ℓ=3
deformation on a rotationally symmetric ball is a rotational Goldstone —
rotating the whole triangle costs zero energy, so E(orientation) is exactly
flat. But SINT-1 proved the M-program dial δ is a gauge-invariant *loop
flux / internal current phase*, not a spatial orientation. These may be
different degrees of freedom. The computation must TEST this, not assume it.

## Stages and gate

**NL-1 [flatness test, decides the interpretation].** Build ψ = f(ρ) +
a·χ₃(ρ)cos(3(φ−δ)) (χ₃ = the actual ℓ=3 eigenmode profile from SPEC), compute
the full nonlinear energy E(δ) at finite a. Prediction split:
  - if E(δ) is FLAT → the ℓ=3 spatial orientation is NOT the dial (it is a
    Goldstone); r is not in the static shape; the dial is the current phase
    (confirming SINT-1 from a new angle). [expected]
  - if E(δ) has cos3δ/cos6δ structure → the orientation IS the dial; read r.

**NL-2 [anharmonicity, physical by-product].** Compute E(a) − E(0) for the
ℓ=3 deformation: the quadratic coefficient (must be > 0, mode is stable — a
check) and the sign of the quartic. Quartic < 0 = self-focusing → the ball
energetically PREFERS a triangular condensate (spontaneous three-site
structure); quartic > 0 = defocusing (no spontaneous triangle). This decides
whether the three-generation structure forms on its own.

**Gate:**
- **PASS** = E(δ) carries cos3δ/cos6δ and yields r within 20%.
- **FAIL (advancing)** = E(δ) flat → r not in the static shape; report the
  refined location (current-phase dial) + the anharmonicity sign.

**Honest prior:** FAIL expected via flatness — but it would rigorously refine
SINT-1 (the dial is the current phase, confirmed by an independent route) and
the anharmonicity sign is a real, new, physical result (does the soliton want
to be triangular). No tuning; χ₃ is the computed mode; amplitude a is scanned,
not fitted.
