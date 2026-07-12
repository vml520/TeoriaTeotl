# Where the last lepton-mass number lives — and why it is protected

*12 July 2026. A companion to [`GENERATIONS_PROGRAM.md`](GENERATIONS_PROGRAM.md).*

The generations program compressed the entire mystery of the three lepton
masses into a **single continuous number**: r ≈ 0.318, the ratio that fixes
how far the "generation dial" sits from the point where the electron would be
massless. Everything else — the 207× and 17× mass gaps, Koide's exact balance,
the electron's anomalous lightness — follows from it. This note is the honest
record of three gated attempts to compute r from the actual soliton, and what
they establish. **r is not solved here.** What *is* delivered is the sharpest
possible statement of where it lives, a validated computation of the object
that carries it, and a rigorous argument for why it has resisted every method.

Labels as before: **[derived]** rigorous · **[computed]** numerical, validated ·
**[consistency]** · **[excluded]** · **[open]**. Every stage has a pass/fail
gate fixed before running (`SINT0_`, `SPEC0_`, `SPEC0b_` pre-registrations).

## 1. r is not in the masses — it is in a flux (SINT)

*`SINT0_prereg_r.md`, `sint_r_interior.py`.*

The dial angle δ is a **gauge-invariant loop quantity** — the phase of the
coupling that ties the three generations together, a flux, not a property of
any one of them. Two facts pin this down **[derived]**:

- The mass sums Σm and Σ√m are **exactly independent of δ** (verified to
  10⁻¹²). No amount of "energy = sum of the generation masses" can ever select
  δ. This is the precise reason every mass-level argument failed.
- A rigid, uniform internal winding forces δ to exactly 0°, 120°, or 240° —
  the "notches." The observed 132.7° is 120° + 12.7°, an **offset** off a notch
  that can only come from the anharmonic energy of how the field overlaps
  itself.

I then computed that overlap energy directly from the real soliton profile.
The result **[computed]**: the offset-producing harmonics are exponentially
tiny when two lumps merely touch, and reach the size needed for r ≈ 0.3 only in
**deep overlap** — where the lumps have effectively merged into one object.
So the "three separated lumps" (molecule) picture of the generations is
**excluded**: it gives r ≈ 0 wherever it is self-consistent, and r ≈ 0.3 only
where it has collapsed. **r's seat is a single merged soliton with internal
structure** — the same hard object that holds the amplitude A ≈ √2 and every
absolute scale in the framework.

## 2. The dial is a real, computed mode of the soliton (SPEC)

*`SPEC0_prereg_spectrum.md`, `spec_internal_spectrum.py`.*

I computed the actual internal fluctuation spectrum of the Q-ball —
Bogoliubov–de Gennes, resolved by angular momentum ℓ — with the background
relaxed on the computation grid so the exact zero-mode identities hold. The
solver is **validated**: the U(1) Goldstone appears at ℓ=0 (frequency 5×10⁻¹⁴,
machine-exact) and the translation zero mode at ℓ=1, both as they must.

At the relevant ball the internal spectrum is clean **[computed]**:

| ℓ | bound internal mode |
|---|---|
| 0 | only the Goldstone (no bound breathing mode) |
| 1 | only the translation zero mode |
| 2 | one bound **quadrupole** shape mode |
| 3 | one bound **triangular** shape mode ← **the generation dial** |
| 4 | none |

So the three-fold structure the generations program inferred is a genuine,
computed object: the soliton's **triangular surface oscillation**. Honest
qualification: it is bound only for large (thin-wall) balls — it unbinds for
compact ones — so the generation structure is a feature of the large-charge
regime, not of every soliton. The dial now has a face; it is not an
abstraction.

## 3. Why r is in the most protected place there is (SPEC-NL)

*`SPEC0b_prereg_nl3.md`, `spec_nl3_condensate.py`.*

The natural next step — condense that triangular mode and read off the dial
potential — was attempted, and it fails for a clean, rigorous reason
**[derived + computed]**. Rotating a single triangular deformation on a round
ball is just rotating the whole thing; it costs **zero energy**. I built the
finite-amplitude condensate from the real computed mode and swept the dial: the
energy is flat to 3 parts in 100,000. **The orientation of a single mode is a
rotational Goldstone, not the dial.** r is in no single-mode condensate.

This is the decisive localization. The dial potential has both a three-fold and
a six-fold harmonic; for the energy to depend on δ at all, **two different
angular sectors (the three-fold and the six-fold) must both be present, with an
independent relative phase between them.** r is that relative phase — a flux
between sectors. This is the tightest place a number can hide, and it
retroactively explains the whole program: r survived symmetry arguments, local
energetics, collective dynamics, topological quantization, *and* the
single-mode condensate, because it was never in any of them. Two independent
routes — the flux picture (§1) and the Goldstone argument (§3) — converge on
the same answer: **the dial is a relative phase between sectors, not any one
mode's orientation.**

A physical by-product **[computed]**: the triangular mode's self-interaction is
*defocusing* (positive quartic) — the ball does **not** spontaneously become
triangular. The three-generation structure is a *sustained, coupled* structure,
not a spontaneously broken one.

## What this settles

| statement | label |
|---|---|
| δ is a gauge-invariant flux; mass sums are exactly δ-independent | **derived** |
| the loose three-lump "molecule" picture of the generations | **excluded** |
| r's seat is a single merged soliton (not separated lumps) | **derived** |
| the generation dial = the soliton's triangular (ℓ=3) surface mode | **computed, validated** |
| that mode is bound only in the large-charge (thin-wall) regime | **computed** |
| a single-mode condensate has a flat dial (rotational Goldstone) | **derived + computed** |
| r is a two-sector (three-fold × six-fold) relative-phase / flux quantity | **derived** |
| the soliton does not spontaneously become triangular (defocusing) | **computed** |
| the value of r ≈ 0.318 | **open** |

## What remains

r is not computed — and after this, the reason is precise, not vague. Its value
is the relative phase of two coupled angular sectors of the nonlinear
condensate: a quantity absent from any single mode or static shape of one
soliton, requiring a **current-carrying / higher-charge configuration** to even
exist. That is the concrete next object. Like the amplitude A ≈ √2 beside it,
and like Newton's G, |Λ|, and the a₀ coefficient elsewhere in the framework, r
is an **absolute internal number** that bottoms out on the full nonlinear
soliton interior — the framework's one recurring frontier, reached here by the
narrowest and best-characterized path in the whole program.

## Reproduce

```bash
pip install numpy
mkdir -p outputs
python3 sint_r_interior.py          # r is a flux; molecule excluded; seat located
python3 spec_internal_spectrum.py   # the internal BdG spectrum; l=3 dial mode (validated)
python3 spec_nl3_condensate.py      # single-mode dial is flat -> r is two-sector
```

Inputs: PDG lepton masses and the repo Q-ball potential only. Each script
prints its pre-registered gate and verdict; JSON lands in `outputs/`.
