# CHSH0 Pre-registration — the compact-time CHSH conjecture

**Date:** 2026-07-13 (before computing). First QC-side target. Tests Vic's
conjecture (convocatoria): can a polynomial-resource TFT field on ℝ³×S¹, with
cyclical time active, produce CHSH **S > 2** — exceeding the classical bound the
local field already saturates at exactly 2.0000 (`teotl chsh.py`)?

**The mechanism under test (stated honestly).** Bell's S ≤ 2 rests on three
assumptions: locality, single outcomes, and **measurement independence** (the
hidden variable is uncorrelated with the settings). TFT's *local, open-time*
field respects all three → S = 2. Compact time (S¹) offers a
**non-conspiratorial** violation of measurement independence: on a time circle
the "initial" state and the "final" measurement lie on the *same* closed
manifold, so the periodicity boundary condition naturally correlates the future
settings with the past hidden variable — the time-symmetric / two-state-vector /
retrocausal picture (Price, Wharton), NOT superdeterministic fine-tuning. The
question: does this legitimately lift S above 2, and how far?

## Computation

1. **Reproduce the bound [computed].** A local, setting-INDEPENDENT phase hidden
   variable with ±1 outcomes A=sign(cos(λ−a)), B=sign(cos(λ−b)) gives the
   TRIANGLE correlation → S = 2. Confirm (matches teotl chsh S=2.0000).
2. **The target [computed].** COSINE correlations E(a,b) = cos(a−b) give the
   Tsirelson value S = 2√2. Verify at the optimal CHSH angles.
3. **The compact-time correlation [computed].** Compute the free phase field's
   two-point function on the time circle S¹, ⟨cos(θ(0)−θ(τ))⟩, and test whether
   the S¹ structure yields COSINE (quantum-like) rather than triangle (local)
   correlations as the settings rotate.
4. **Realize S>2 with no-signaling [computed].** Build an explicit compact-time /
   retrocausal model — ρ(λ | a,b) set by the S¹ closure — and compute S. Verify
   **no-signaling**: the marginals ⟨A⟩, ⟨B⟩ stay setting-independent (this is
   what separates a legitimate boundary-condition correlation from a signaling /
   conspiratorial one).
5. **Cap [computed].** Check whether S saturates at 2√2 (Tsirelson, cosine) or
   reaches the algebraic max 4 (PR-box / super-quantum).

## Gate

- **PASS (conjecture supported)** = compact time lifts S above 2 (toward/at 2√2)
  via a **no-signaling, time-symmetric** measurement-dependence — a legitimate
  Bell evasion, not signaling — with the honest caveats below.
- **PARTIAL** = the mechanism reaches S>2 only by a correlation that also
  signals (marginals move) → it is a conspiratorial loophole, not a clean
  evasion; report as such.
- **FAIL** = S stays at 2 (the local bound is robust to the compact-time
  structure; the S=2.0000 is structural).

**Honest prior & scope (flagged up front).** Likely outcome: compact time CAN
reach S = 2√2 (QM) via time-symmetric measurement-dependence, no-signaling, and
is capped at Tsirelson (no super-quantum) — SUPPORTING the conjecture that S>2
is reachable. But two hard honesties: (i) this *reproduces* QM, so the value S
alone cannot confirm compact time is nature's mechanism (degenerate with
standard QM); (ii) it rests on accepting retrocausal/compact-time physics — a
coherent but non-standard interpretational stance, not a proof. FLOORS/OPEN: a
test that *distinguishes* compact-time TFT from standard QM (S cannot); whether
the S¹ closure is physically realized. No tuning; correlations are the field's.
