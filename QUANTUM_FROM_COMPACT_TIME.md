# Quantum correlations from compact time

*13 July 2026 (CHSH closure); 14 July 2026 (Born rule). A quantum-foundations
companion, extending the CHSH result in `teotl chsh.py`.*

The qubit emulator (`teotl qc.py`) reproduces single qubits faithfully — a lone
qubit is just a phase and an amplitude, which a classical field carries. The
hard part is entanglement: the Bell/CHSH correlations that are provably too
strong for any *local* classical description. `teotl chsh.py` reported the
honest result — **TFT's local field saturates CHSH at exactly S = 2.0000**, the
classical bound, while the exact quantum reference reaches 2√2 ≈ 2.828.

This note asks whether **compact time** (the ℝ³×S¹ structure, time as a closed
loop) changes that — and finds that, worked through honestly, it **derives** the
quantum value 2√2 with no free parameters, reframing quantum non-locality as
compact-time coherence. It also states, prominently, what that does and does not
buy. Pre-registration: `CHSH0_prereg_compact.md`.

> **Read this first.** The result below **reproduces** quantum mechanics; it does
> not beat it and, by a Bell test, cannot be distinguished from it. Its value is
> conceptual — a deterministic, single-valued-phase account of *why* the quantum
> correlation has the value and the ceiling it does. The **Born rule** (single-
> outcome |ψ|²), previously flagged here as open, is now **derived** from the same
> closure (§6, `born1..5_*.py`) — assumption-conditional, and still degenerate with
> QM — leaving **one** clearly-marked open problem: a distinguishing experiment. It
> is not a claim to have surpassed quantum mechanics.

## 1. Why S > 2 is not, by itself, a result (`chsh_compact_time.py`)

First, the honest trap. Bell's S ≤ 2 rests on three assumptions: locality, single
outcomes, and **measurement independence** (the hidden variable is uncorrelated
with the settings). The quantum value 2√2 is **no-signaling** — the measurement
marginals stay flat — so exceeding 2 does *not* require faster-than-light
signaling; it requires giving up measurement independence. Compact time offers
a *non-conspiratorial* way to do that: on a closed time loop the "past" state and
the "future" setting lie on the same manifold, so the periodicity condition ties
them (the time-symmetric / two-state-vector picture), not superdeterministic
fine-tuning.

But a *posited* time-loop reweighting of the hidden variable is **unconstrained**
— we checked, and a naive one reaches **S = 2.90, above the quantum bound** (a
no-signaling super-quantum, PR-box-like correlation). That over-reach is the
tell: an arbitrary measurement-dependence can give any value up to 4, so "compact
time lets S exceed 2" is, alone, *vacuous*. The physics has to come from the
actual field, not a chosen weight.

## 2. The closure, derived (`chsh_closure.py`)

The fix is that TFT's S¹ variable is not an arbitrary weight — it is a
**single-valued complex phase**. That one physical fact does all the work:

- **The hidden variable cancels.** Two measurement events on the loop carry field
  phases θ_A, θ_B; setting *a* reads the phase relative to *a*. Demanding the
  phase be single-valued around the loop *fixes* the difference θ_A − θ_B, and the
  individual hidden phases **drop out** of the correlation, leaving exactly
  **E(a,b) = cos(a − b)** — the quantum form — with **no tunable input**. The
  determinism is real and present; it simply cancels from what can be measured.
  The marginals vanish → **no-signaling**.
- **The quantum ceiling is automatic.** A coherent complex phase lives in a
  Hilbert space, so **Tsirelson's theorem caps CHSH at 2√2** — no assumption
  added. Searching 40,000 settings, the closure never exceeds **2.828**; the 2.90
  overshoot is not merely avoided but *forbidden* once the phase must be a genuine
  phase.

The three cases line up exactly: dephase the S¹ (lose the phase) → 2, classical;
treat it as an arbitrary weight → 2.90, unphysical; keep it a single-valued
coherent phase → 2√2, quantum.

## 3. What it means

**Quantum coherence is the phase closing single-valuedly on the compact time
circle.** The "spooky" Bell correlation is, in this account, the deterministic
geometry of a closed-time phase seen from ℝ³ — the hidden phase is perfectly
definite, it just cancels from the observable correlation, so ℝ³ *looks*
uncertain. The quantum *value* (cos) and the quantum *ceiling* (Tsirelson) both
follow from single-valuedness, with nothing tuned. This makes precise the thesis
that what is usually called quantum uncertainty is ordinary S¹ behavior.

## The ledger

| statement | label |
|---|---|
| local field saturates CHSH at S = 2.0000 | **computed** (the honest baseline) |
| S > 2 is no-signaling → needs measurement-dependence, not signaling | **derived** |
| an arbitrary time-loop weight is unconstrained (reaches 2.90) | **computed** (a warning) |
| single-valued S¹ phase ⇒ hidden variable cancels ⇒ E = cos(a−b), no tuning | **derived** |
| coherent phase ⇒ Tsirelson ⇒ CHSH capped at 2√2 automatically | **derived** (2.828 numerically) |
| "quantum coherence = the phase closing on the S¹ time circle" | **interpretation** (coherent) |
| a measurement that distinguishes compact-time TFT from standard QM | **open** — the real prize |
| single-outcome probabilities (the Born rule = \|c_k\|²) | **derived** (§6, assumption-conditional) |

## 6. The Born rule, derived (`born1..5_*.py`)

The closure gives the two-point *correlation* coherently; that single measurement
*outcomes* follow |ψ|² is a separate step, taken here. Pre-registration:
`BORN0_prereg.md`. Five pre-committed stages, each with a runtime gate — verdict
**PASS (structural, assumption-conditional)**, all gates met at machine precision,
no tuning.

- **Equal amplitudes ⇒ equal weights, by an exact symmetry (`born1`).** For an
  entangled two-channel state, the system swap 0↔1 is undone by a *purely
  environmental* unitary **iff |c₀| = |c₁|** (counter-op unitarity defect ~1e-16
  equal-moduli; 0.6–8 for the unequal control). A pure-environment operation
  cannot change a system-local probability, so the swap leaves them unchanged ⇒
  P(0)=P(1) — with **no |c|² inserted** (Zurek envariance, realized on the field).
- **|c_k|² for *all* amplitudes, from that symmetry alone (`born3`, load-bearing).**
  Fine-grain a rational weight m/n into n branches; the branches come out all
  equal-modulus (1/√n), so envariance makes them equiprobable ⇒ P = m/n = |c_k|²,
  independent of n. The **exponent 2 is coherent-superposition normalization** —
  equal branches must carry amplitude 1/√n, so branch-count = 1/amplitude² — **not**
  a charge postulate. An independent route via the field's own conserved U(1)
  charge on the Haar S¹ measure agrees (`born2`), with the Born *additivity* of
  exclusive outcomes tracing to winding-orthogonality (the interference cross-term
  vanishes).
- **The continuous law: Malus (`born4`).** A spin-½ winding measured at relative
  angle θ has phase-geometry overlap cos(θ/2) (the SU(2) half-angle), so the
  weight rule gives **P(+|θ) = cos²(θ/2)**. It is *uniquely pinned* by consistency
  with the closure's E = cos θ: no other exponent reproduces the coherent
  correlation (q = 1, 3, 4 break it).
- **One rule does everything (`born5`).** A single object, P = |⟨·|Ψ⟩|², yields the
  marginals, no-signaling, E(a,b)=cos(a−b), Tsirelson S=2√2, and Malus (its
  product-state limit) — mutually consistent, no second mechanism glued on.

**What this buys, and its floor.** The Born rule reduces to *the S¹ swap symmetry
+ additivity*: quantum probability is ordinary coherent-phase behaviour on the
time circle, the single-outcome counterpart of the correlation result above. Two
honest limits, unchanged from the CHSH story: it **rests on non-contextuality /
additivity** over exclusive branches — the standard soft spot of envariance
derivations, assumed not derived — and it **reproduces QM exactly**, so it adds no
distinguishing test. The one open prize remains the same: an observable where
compact-time TFT and QM differ.

## The honest boundary

This is a *reinterpretation with a derived correlation structure*, not a
surpassing of quantum mechanics. Two things it is not:

1. **It does not beat QM, and CHSH cannot distinguish it from QM.** Reproducing
   2√2 is degenerate with standard quantum mechanics on this test. The genuine
   prize — untouched — is an observable where compact-time TFT and ordinary QM
   *differ*; only that could make the picture empirically preferable, and it may
   not exist.
2. **The Born rule is derived, but assumption-conditionally.** §6 reduces
   single-outcome |ψ|² to the S¹ swap symmetry plus additivity/non-contextuality;
   it does not derive that last assumption, and — like the correlation — it
   reproduces QM exactly, so it too cannot distinguish the picture from standard QM.

What it does buy: the compact-time conjecture, previously ill-posed (any S
reachable), is now **well-posed and constrained** — the field's own
single-valuedness fixes the answer to the quantum value and the quantum ceiling,
deterministically and with no free parameter. That is a real step, honestly
bounded.

## Reproduce

```bash
pip install numpy
mkdir -p outputs
python3 chsh_compact_time.py   # local S=2; the naive time-loop overshoots (a warning)
python3 chsh_closure.py        # single-valued phase -> cos(a-b), Tsirelson-capped 2sqrt2
python3 born1_envariance.py    # equal amplitudes -> equal weights, by exact symmetry
python3 born2_measure.py       # U(1)-charge measure -> |c|^2, additivity from orthogonality
python3 born3_finegrain.py     # |c|^2 for all amplitudes from envariance alone (exponent 2)
python3 born4_malus.py         # continuous Born law P(+|theta)=cos^2(theta/2)
python3 born5_closure_knit.py  # one rule -> marginals + E=cos(a-b) + Tsirelson + Malus
```
Each prints its pre-registered gate and verdict; JSON lands in `outputs/`.
