# G1 — The chiral root: does TFT have a chiral structure?

> ## ⚠ PARTLY SUPERSEDED 18 Aug 2026 — read with `DERIVED_SUMMARY.md` §7.
> **What SURVIVES, and is the honest core of this note:** the minimal action is exactly CP-symmetric,
> so **net chirality is NOT forced** — that result is untouched and was correctly labelled.
> **What is WITHDRAWN:** the section below headed *"one invariant, three faces"*. An audit
> (`bmca0_audit.py`) found baryon number (ΣW, linear in the windings) and magnetic helicity
> ((2π)²ΣWᵢWⱼLkᵢⱼ, quadratic and linking-dependent) are **two independent invariants**, not one with
> three faces — two unlinked W=+1 windings give B=2, H=0, while a linked W=+1/W=−1 pair gives B=0,
> H=+8π². **The linking machinery here is correct and reusable; the identification drawn from it is
> not.** See also the superseded banner on `G2_chiral_anomaly.md`.

*Runnable check: `verify_chiral_g1.py`. Outcome: the chiral invariant EXISTS (= winding-line helicity, Vic's "winding directions"), but the minimal action is CP-symmetric so net chirality is not forced.*

## A. The minimal action is CP-symmetric
Energy density e = ½(∇θ)² + Λ(1−cos θ). Under C: θ → −θ. Both (∇θ)² and cos θ are invariant → **e is CP-even** (verified exactly: max|e − e_flip| = 0). So the minimal sine-Gordon TFT produces **equal + and − windings — matter = antimatter, zero net handedness.** Chirality is NOT automatic.

## B. The chiral invariant exists — winding-line helicity
The linking number (helicity) of two winding lines, Gauss integral Lk = (1/4π)∮∮(r₁−r₂)·(dl₁×dl₂)/|r₁−r₂|³:
| configuration | Lk |
|---|---|
| linked, right-handed | −1 |
| unlinked | 0 |
| mirror (left-handed) | +1 |

A topological invariant that **distinguishes handedness** (CP flips its sign), nonzero **only when windings link/twist**. **This is "chirality from winding directions"** — chirality = the helicity of the winding field, the correlation of the winding *directions* of linked defect lines. (Vic's memory confirmed.)

## Why this unlocks the trio — one invariant, three faces
The winding-line helicity is simultaneously:
- winding **charge** around the line = **baryon number** (baryogenesis),
- **linking of flux** = **magnetic helicity** (magnetogenesis),
- **sign of the linking** = **chirality**.

So the chiral anomaly (baryon number ↔ magnetic helicity) is not an extra postulate — in TFT it is the statement that these are the *same* topological quantity. That is G2.

## Verdict
- **Chiral structure PRESENT** — the trio has a genuine topological home; the program is not dead at the root.
- **NOT forced** — minimal action is CP-even, so a *net* chirality (the actual matter excess / preferred handedness) is an **initial condition** (net primordial helicity) or requires a **CP-violating input** (a winding vacuum/θ-angle, an added term).
- **Consequence, pre-flagged:** the *linkage* (G2) is derivable; the *net asymmetry* (sign & magnitude of η) will bottom out at an IC / deep-unknown, like a₀'s coefficient and |Λ|. Mechanism yes; absolute number, almost certainly not.
