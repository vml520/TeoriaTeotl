# Foundations and limits: what the field is, and where the picture breaks

*18 July 2026. A foundations companion. It asks what the Teotl field **is** (not
just what it does), and — with equal weight — where the framework **fails or
bottoms out**. It contains the sharpest honest negative in the program.*

> **Read this first.** Most results here **reproduce standard physics** and are, by
> construction, *empirically degenerate* with it — their value is conceptual: a
> single circle-valued field is shown to *unify* time, charge, the galactic
> acceleration scale, and dark energy, and to *recast* the measurement problem as a
> problem of time. But two results are limits, not victories: the "classical"
> version of the field **cannot** reproduce generic quantum entanglement (§4), and
> the dark-energy fit needs a **super-Planckian** decay constant (§5). Both are
> stated plainly. Nothing here claims to beat quantum mechanics or to solve the
> cosmological-constant problem. Pre-registrations and gates are in the `*_prereg.md`
> files; every verdict was fixed before computing.

## 1. Time emerges from the phase (`pw_emergent_time.py`)

TFT says "time = phase cycling." We make this precise via the **Page–Wootters**
mechanism. A globally *timeless* constraint state (Ĥ_C + Ĥ_S)|Ψ⟩ = 0 — built from
the Hamiltonians alone, **no external time** — with the S¹ phase as the clock,
reproduces Schrödinger evolution of the rest **when conditioned on the phase-clock**
(fidelity 1.000000). The emergent time is **cyclic** and the clock spectrum is a
**comb** — the same compact-time structure that appears elsewhere in the program.

The payoff is ontological: the internal phase circle (whose *winding* is charge) and
the time circle (whose *cycling* is time) are **one structure**. Time is the phase
read relationally. **Honest floor:** this reproduces standard quantum mechanics
exactly, so "the phase *is* time" is an *identification*, not a forced result — an
ordinary external-time reading fits the same data.

## 2. One circle, one scale: time, charge, a₀, and dark energy (`scale_darkenergy.py`)

If that same S¹ is the cosmological dark-energy field (an axion-like pNGB), a single
circle at the Hubble scale ties together four things:

- **a₀ = cH₀/2π ≈ 1.05×10⁻¹⁰ m s⁻²** — 87% of the observed galactic acceleration
  scale, the 2π from the circle;
- the **dark-energy equation of state**: the cosine potential gives thawing
  quintessence with **w ≥ −1 always** (no phantom crossing, analytic) and
  w₀ ≈ −0.88 → wₐ ≈ −0.18 to −0.25;
- with the *same* circle also carrying **time** (§1) and **charge** (winding).

Because one field sets both, **a₀ and the dark-energy w(a) are locked** — a joint,
DESI-testable signature no standard framework offers (ΛCDM has neither; MOND has a₀
but no dark-energy dynamics). A **confirmed phantom crossing (w < −1) would falsify
it.** There is even a natural reading of a₀ itself: it equals the field's own de
Sitter quantum fluctuation δφ ~ H₀/2π (§5), i.e. the acceleration below which the
field's quantum fluctuation dominates the dynamics.

**Honest floors:** the absolute scale (ρ_DE / H₀) is an **input** — this does *not*
solve the cosmological-constant problem; and the quantum-time = dark-energy-circle
identity is a *hypothesis* (empirically degenerate), tested by consistency and
consequence, not proven. The falsifiable content (no-phantom, wₐ) is the physics of
the dark-energy companion; here it is attached to the *one circle that is also time*.

## 3. The measurement problem as loop-closure (`meas3_selection.py`, `meas4_classical_arrow.py`)

Recasting measurement as a problem of *time*: TFT does not replace decoherence, it
**completes** it. Only definite (decohered) branches can close as single-valued
histories — a coherent "cat" of macroscopically-distinct branches cannot close (its
closure amplitude → 0 with size). The loop's seam phase then selects **one** outcome
per run (no branching), with Born frequencies. Einselection (the pointer basis) is
reproduced, and energy positivity (E>0) supplies a microscopic clock direction
(matter vs antimatter = opposite winding).

**Honest floors:** definiteness and the pointer basis follow, but *which* outcome is
realized (the seam phase) is a boundary condition, **not derived** — collapse is
*reframed* as deterministic loop-closure, not conjured away. And the **thermodynamic
arrow** is a low-entropy boundary condition (the past hypothesis), correctly *not*
derived from the time-symmetric dynamics — deriving it would violate T-symmetry.

## 4. The tensor-completeness limit — the sharp negative (`tens_completeness.py`)

Can a single **economical** (polynomial-resource) circle-valued field realize the
full 2ⁿ-dimensional Hilbert space of n subsystems? **No.** A single field profile has
polynomially many parameters; a general n-qubit state needs 2ⁿ amplitudes. The field
is therefore **entanglement-bounded** (matrix-product-state-like): random-state
fidelity collapses with n, and the entanglement it can carry is capped.

Crucially, this **explains why** the CHSH, Born, and GHZ results elsewhere in the
program succeeded — those states are all *low-entanglement* (GHZ is one ebit,
representable at bond dimension 2). But **volume-law entanglement is not
representable.** So the economical "classical" Teotl field is a *bounded-entanglement
subtheory* — and is therefore **falsified by quantum-supremacy experiments**, where
nature realizes exactly the volume-law entanglement the field cannot.

The only way to recover full quantum mechanics is to **quantize the field**
(exponential / Fock degrees of freedom) — at which point it is standard quantum field
theory, degenerate with QM and no longer "just a classical circle-valued field." **The
framework cannot be both economical-classical and full quantum mechanics.** This is
the sharpest limit on the program's quantum ambition, and we state it without
softening.

## 5. The super-Planckian tension (`swmp_tension.py`)

The dark-energy fit of §2 requires a decay constant **f ≳ 1.45 M_Pl** — super-
Planckian, a genuine swampland concern shared with *all* thawing quintessence.
Clockwork/alignment mechanisms would lower it but need *many* circles, breaking the
one-S¹ picture. **Monodromy** — winding the *single* circle Q ~ 15 times — is
compatible with one circle and native to TFT (winding = charge = the theory's own
integer), giving an effective super-Planckian f from a sub-Planckian fundamental. So
the tension is **not eliminated but relocated** to a winding-number floor (same class
as the framework's other integer/initial-condition inputs).

**Does the tension leak into R³ uncertainty?** No — it is **decoupled**. The field's
de Sitter fluctuation δφ ~ H₀/2π is *f-independent* and equals **a₀/c**; super-
Planckian f only shrinks the *angle* uncertainty δθ ~ H₀/(2πf) (the phase
classicalizes). So the observable R³ acceleration-uncertainty scale a₀ = cH₀/2π is
set by the circle's size (H₀), **protected** from the super-Planckian problem, which
stays confined to field space. (The Planck-scale duality still holds abstractly:
super-Planckian f is the field-space mirror of the R³ minimal-length/GUP limit — but
the *observable* R³ scale is H₀, not M_Pl.)

## What this companion does and does not establish

- **Establishes (conceptual):** one circle-valued field unifies time (§1), charge,
  a₀, and dark energy (§2) at the Hubble scale, and recasts the measurement problem
  as loop-closure (§3). Time = the phase read relationally.
- **Establishes (limit / negative):** the *economical classical* field is
  entanglement-bounded and cannot be full QM (§4) — falsifiable by quantum supremacy;
  the dark-energy fit needs super-Planckian f (§5).
- **Does not establish:** that the phase *is* fundamentally time (identification, not
  forced); a solution to the cosmological-constant problem (absolute scale is input);
  a distinguishing experiment vs standard QM (the correlations are degenerate).
- **Floors, named:** which measurement outcome (seam phase), the thermodynamic arrow
  (past hypothesis), the absolute cosmological scale, and the super-Planckian /
  winding-number input.

## Reproduce

```bash
pip install numpy
mkdir -p outputs
python3 pw_emergent_time.py       # time emerges from the S^1 phase (Page-Wootters)
python3 scale_darkenergy.py       # one S^1 at H0: a0=cH0/2pi + no-phantom w(a), locked
python3 meas3_selection.py        # single-outcome selection by loop-closure
python3 meas4_classical_arrow.py  # classical limit (einselection) + arrow of time
python3 tens_completeness.py      # the sharp limit: classical field is entanglement-bounded
python3 swmp_tension.py           # super-Planckian tension + monodromy + R^3 decoupling
```
Each prints its pre-registered gate and verdict; JSON lands in `outputs/`.
Pre-registrations: `PW0_prereg.md`, `SCALE0_prereg.md`, `MEAS3_prereg.md`,
`MEAS4_prereg.md`, `TENS0_prereg.md`, `SWMP0_prereg.md`.
