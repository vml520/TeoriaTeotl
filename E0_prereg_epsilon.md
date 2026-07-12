# E0 Pre-registration — the origin of ε (DRAFT for Vic's gate)

**Date:** 2026-07-11 (drafted BEFORE any E-stage computation; no E-stage runs
until Vic sanctions this document)

**Question:** what sets the generation-dial offset? Equivalently: why is the
electron 2.27° from silence?

## The measured targets (PDG-propagated, frozen here)

One unknown, two equivalent decompositions of the dial position δ:
- **ε = δ_zero − δ = 0.0395790 ± 0.0000018 rad** (offset from the mass-channel
  zero at δ_zero = arccos(−1/A); the "electron lightness" reading);
- **β = δ − 120° = 0.2222296 ± 0.0000084 rad** (offset from the nearest
  locking notch allowed by M3; the "symmetric point + breaking" reading).
σ_δ = 8.4×10⁻⁶ rad, dominated by the PDG tau mass (±0.12 MeV).

Note recorded up front: under the second reading, ε itself may be a *derived
difference* (π/12 − β), not a fundamental input — "why is the electron light"
would decompose into "why β ≈ 2/9 rad" plus the geometric 15° between notch
and zero. A mechanism may legitimately target either decomposition; it must
say which BEFORE computing.

## Binding exclusions (inherited; re-testing forbidden)

- Polynomial internal energetics of degree ≤ 5 (M3: 26,620σ); pure cubic
  det-class relaxation; extremal-Q; positivity-boundary; per-dof equipartition.
- Ring symmetries/dualities for the balance (G3, theorem-grade); ring-local
  energetics (G4); U(1) rotor and shared-core coefficient (G5).
- Excitation towers (SP1–SP3); ε = 1/(8π) (25σ).
- A ≈ √2 stays PARKED (Koide-arc standing criterion); no E-stage may assume
  its derivation.

## Anti-numerology protocol (hard rules, learned the hard way)

1. **The candidate list below is closed.** No constant, fraction, or angle
   may be added after this document is sanctioned. Comparisons not listed
   here may only enter via E2/E3: a relation must be DERIVED symbolically
   first, its number compared second.
2. **Every comparison is reported** — hits and misses — with its z-score and
   the look-elsewhere correction for its candidate class.
3. **The 2/9-rad form is grandfathered** as the single literature target
   (Brannen class, logged at 0.9σ in M3). It is a *constraint any mechanism
   must hit*, never itself evidence of a mechanism.
4. Formula-level care (the M2 lesson): every gate below is stated in the
   measured quantities (ε, β, σ_δ), not in a chosen parametrization.

## Stages and gates

**E1 — topological quantization, tested against its own prediction class.**
Physical hypothesis: if the dial offset is set by winding topology, it is a
2π-rational angle. Pre-committed candidate class: offsets 2π·p/q with
gcd(p,q)=1, q ≤ 36, tested against ε, β, and δ (three targets).
Tolerance: 3σ_δ. Look-elsewhere: ~400 candidates × 3 targets × 6σ window →
expected ~2% false-positive rate for the whole scan, computed and reported.
- PASS = a match survives the correction (then E1 hands the specific p/q to
  E2 as the structure to derive).
- FAIL = the naive topological-quantization class is EXCLUDED for the dial
  offset (a real result: it kills the flagged M3/M4 escape route in its
  simplest form).
Honest prior, recorded: β/2π = 0.03537 and ε/2π = 0.00630 do not look like
small fractions; expected verdict is FAIL. The class dies or it doesn't —
either way the record gains a fact.

**E2 — derive the breaking (the make-or-break stage).**
Target: a second-order internal-dynamics calculation on the locked dial
(locking notch at a 60° multiple is permitted — M3's exclusion applies only
to polynomial energetics acting ALONE) whose leading correction to the dial
angle is forced, with Z₃-combinatoric/integer coefficients and no continuous
tuning, to equal **β = 0.22223 ± 0.00003 rad** (equivalently to hit 2/9 rad
if exact). Candidate sources to try, in this order, each labeled before its
number is computed: (a) second-order mixing between the n=1 and n=2 internal
harmonics through the mode sector demonstrated in M2′; (b) back-reaction of
the bound generation dial on its own locking potential; (c) a quantized
misalignment inherited from the winding-even projection axis (links to the
BMC helicity structure).
- PASS = the coefficient is forced (symbolic derivation first, number
  second) and lands within 3σ of β.
- FAIL = coefficients remain free or land elsewhere → logged, stop.

**E3 — ε from an already-measured small quantity.**
Closed list of small quantities already in the record: the M2′ mode
misalignment η = 1.1×10⁻³; the Koide deviation |Q − 2/3| = 6.2×10⁻⁶; the
amplitude deviation √2 − A = 1.3×10⁻⁵. Gate: a DERIVED relation (symbolic
first) connecting one of these to ε or β within errors. No power/log fishing:
the relation must come from the mechanism, not from exponent scanning.
- PASS/FAIL as above. Honest prior: no candidate relation is currently known;
  this stage exists so that if E2's calculation naturally produces one, its
  comparison is already licensed.

**E4 (scoping only, not a gate — requires Vic's separate approval).**
Scale-dependence: Koide and hence ε hold at POLE masses; at running masses
the relation degrades (known). Locating the scale at which ε is exact would
locate where the mechanism lives (on-shell/IR vs UV). Requires external
running-mass inputs beyond PDG pole values — flagged because it imports
literature numbers, against the program's PDG-only convention so far.

## Stop conditions and closure

Stages are independent; a FAIL in any does not block the next. If E1–E3 all
FAIL: the ε program closes with "ε remains a free parameter; topological
quantization excluded in its simplest form; the breaking is not second-order
forced by the mechanisms tried" — and the falsifiability anchor stands:
**a ~10× better tau mass tests the 2/9-rad form at high sharpness** (if 2/9
dies empirically, E2's target dissolves with it; if it survives, any future
mechanism has one exact number to hit).

## Vic's decision points

1. Sanction the candidate class in E1 as-is (q ≤ 36), narrower, or wider?
2. Sanction the E2 source list and order (a → b → c)?
3. E4: approve external inputs, defer, or strike?
4. Anything to add to the E3 closed list before it freezes?
