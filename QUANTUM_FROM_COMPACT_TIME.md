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
> QM. The distinguishing-experiment question is now itself answered (§7): a search
> of the natural channels finds the theory **empirically degenerate** with QM, with
> one open falsifiable edge (tensor-completeness). It
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
| a measurement that distinguishes compact-time TFT from standard QM | **searched (§7)** — none feasible; empirically degenerate; one edge (tensor-completeness) open |
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

## 7. No distinguishing observable — a quantified degeneracy (`dis1`, `dis2`)

Both results above reproduce QM, so the standing open question was: is there ANY
observable where compact-time TFT and standard QM *differ*? We searched the
channels where compact time *can* differ, with the gates fixed in advance
(`DIS0_prereg.md`). The honest answer: **there is one in principle, but the theory
is empirically degenerate with QM for any feasible experiment.**

- **Bell channel — exactly degenerate, structurally (`dis1`).** Discretizing /
  compactifying the time circle to any size N leaves E(a,b)=cos(a−b) and S=2√2
  *unchanged* (machine precision, N-independent), because the hidden time-phase
  **cancels** (correlations see only setting differences). CHSH can *never*
  distinguish them — upgrading the numerical 2√2 to a structural statement.
- **Temporal / energy channel — a real difference, but 1/T (`dis1`).** Single-
  valuedness on a period-T loop forces an energy comb Eₙ=2πn/T and revival that is
  exact and strictly periodic at T. But the effect scales as 1/T. The only T
  consistent with observed continuously-tunable spectra is **cosmological**
  (T~1/H₀ → comb spacing ~10⁻³³ eV, revival ~ age of the universe = unobservable);
  a *microscopic* T is excluded — it would quantize energy in mc²≈511 keV units,
  forbidding eV atomic lines. Time-winding sectors are degenerate (phase 2πn).
- **Multipartite contextuality / GHZ — degenerate (`dis2`).** The coherent-phase
  closure, extended to three parties, reaches **Mermin M = 4 = QM**: the full GHZ
  paradox and contextuality *irreducible to 2-body* (all pairwise correlations
  vanish, yet M=4). So even the "does TFT *fall short* of QM?" test comes back
  degenerate.

Sharpest in-principle falsifier: forbidden transition frequencies between comb
teeth → observed continuous spectra already bound T ≳ 1/H₀ (satisfied). **The QC
arc's old caveat ("reproduces QM, no distinguishing test") is now a *result*, not a
hand-wave** — the reinterpretation is not experimentally separable from QM by any
feasible measurement. Its value is conceptual/foundational.

**The one surviving falsifiable edge (honest, open).** The GHZ computation used the
full 2ⁿ-dim tensor Hilbert space the closure *claims* to be; CHSH established only
the 2-body sector. A field-theoretic proof that *n windings realize the full 2ⁿ
tensor space* is undone — and if the single-field S¹ construction secretly
saturates at 2-body it would give Mermin M~0 and **be falsified by real GHZ
experiments**. So TFT must be full-tensor to survive, and there it is degenerate
with QM. That tensor-completeness question is the genuine remaining frontier.

## 8. The uncertainty principle, derived (`uncertainty_s1.py`)

The two results above are the *correlation* and *probability* pillars of quantum
mechanics, from the S¹. The third pillar — **uncertainty** — follows from the *same*
single-valued phase, as a theorem rather than a postulate.

On S¹ the single-valued phase is e^{iθ}; its conjugate is the winding number
N = −i∂_θ, whose spectrum is the **integers** — this *is* charge quantization
(`verify_charge_quantization.py`). The commutators are exact: [N, cosθ] = i sinθ,
[N, sinθ] = −i cosθ (verified to 1e-13). The Robertson bound then gives the
Carruthers–Nieto **number–phase uncertainty**

  ΔN · Δ(sinθ) ≥ ½|⟨cosθ⟩|,

which we verify holds for **every** state, is **saturated** by the von Mises
(circular minimum-uncertainty) family, and reduces to **ΔN·Δθ = ½** (Heisenberg) in
the phase-localized limit (numerically 0.500). The tradeoff is physical and forced: a
definite charge/winding (ΔN=0) has a **uniform, undefined phase**; sharpening the
phase spreads the charge.

So the **same single-valued S¹ phase** underwrites all three pillars — charge
quantization *and* the coherent correlations/Born rule *and* the uncertainty
principle. One structure, three pillars — with **uncertainty derived, not assumed**
(and, unlike §1–7, this one is a clean theorem with no degeneracy caveat: it *is*
the quantum uncertainty relation for the field's own conjugate variables).

## The honest boundary

This is a *reinterpretation with a derived correlation structure*, not a
surpassing of quantum mechanics. Two things it is not:

1. **It does not beat QM, and no feasible experiment distinguishes it from QM.**
   Reproducing 2√2 is degenerate on the CHSH test, and §7 now shows the same across
   the Bell (exactly, any loop size), temporal (1/T-suppressed, unobservable at the
   cosmological loop), and GHZ/contextuality (M=4=QM) channels. An observable where
   compact-time TFT and ordinary QM *differ* was searched for and not found; the
   only surviving edge is the tensor-completeness question of §7.
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
python3 dis1_distinguish.py    # search for a distinguishing observable: none feasible (1/T)
python3 dis2_ghz.py            # GHZ/Mermin: coherent closure reaches M=4=QM (degenerate)
python3 uncertainty_s1.py     # the uncertainty principle DERIVED: dN*dtheta>=1/2 from the S^1
```
Each prints its pre-registered gate and verdict; JSON lands in `outputs/`.
