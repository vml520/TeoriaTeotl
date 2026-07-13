# Black holes under TFT — horizon, no singularity, bounce, entropy

*13 July 2026. A gravity/cosmology companion, alongside the particle-sector docs.*

TFT's gravity is emergent geometry sourced by the phase field's energy (the 1/r
shape and universal sign are derived; the toy solar system and Mercury's 42.9″
follow). Two further derived facts seed a black hole: **√(2GM/r) is the inflow
rate of space** toward a mass (reaching c at the Schwarzschild radius), and
**time is the turning of the phase** (dτ = ℏ dθ/E). Reading those literally
gives a complete, and in places distinctive, black-hole picture — each piece a
consequence of the same substrate.

Labels: **[derived]** · **[computed]** · **[consistency]** (matches GR) ·
**[structural]** · **[floor]** (an absolute value the U(1) field does not fix).
Pre-registrations: `BH0_`, `BHB0_`, `BHE0_`.

## 1. The horizon, and frozen time (`bh_study.py`)

**The horizon is where space's inflow overtakes light [derived route].** The
derived inflow rate v = √(2GM/r) equals c exactly at r_s = 2GM/c². Inside, space
falls in faster than phase can propagate out, so outgoing light is dragged
inward — a horizon, obtained from TFT's *own* inflow rate rather than imposed
(the river / Gullstrand–Painlevé picture). The location r_s matches GR
**[consistency]**.

**Time freezes at the horizon, literally [structural].** Since time is phase
cycling, the rate of time ∝ √g₀₀ = √(1−r_s/r) → 0 at r_s. An outside observer
watches infalling phase *freeze* at the horizon — the old "frozen star" made
exact: the phase-cycling that *is* time stops there.

## 2. No singularity — a regular core (`bh_study.py`)

The distinctive departure from GR. The phase field is **bounded**: the phase
gradient cannot exceed ~one turn per coherence length (|∇θ| ≲ 1/ℓ₀) and the
amplitude is finite, so the energy density **cannot diverge** — it caps at
~Planck density. The mass therefore sits in a **regular core**, not a point
singularity: for a solar mass, r_core ≈ 4.5×10⁻²³ m — about 3×10¹² Planck
lengths across (a real, extended object, not a Planck point), buried ~10⁻²⁶ of
the way in from the horizon. **A TFT black hole is a horizon wrapped around a
Planck-density, phase-frozen core** — in the regular-black-hole / Planck-star /
gravastar family, but here the singularity resolution comes *specifically* from
the phase field's boundedness. **[TFT-native prediction]**

## 3. The core bounces (`bh_bounce.py`)

That core is not static — it **bounces**. Taking the framework's own stable
particle (the φ⁶ Q-ball), squeezing it out of equilibrium, and evolving the full
field equations, the core density peaks and re-expands, oscillating and staying
finite — it breathes rather than collapsing **[computed]**. The mechanism is the
same boundedness: the potential is *repulsive* at high density (dV/d(ρ²) climbs
from +0.17 to +1.13 as it compresses) — a field "degeneracy pressure" that
forbids collapse to a point **[derived]**. No ad-hoc quantum gravity: the same
boundedness that removes the singularity drives the bounce.

**An observable follows.** In the core's proper time the bounce is fast
(~t_Planck), but the horizon's extreme time dilation stretches it into an
external delay ~(M/m_P)² t_P (the Rovelli–Vidotto Planck-star scaling, here
*motivated by* the TFT bounce). Working it through, a **primordial black hole of
~6×10²² kg would be completing its bounce now** — arriving as a short
high-energy burst. The exact mass is scaling-dependent (~10¹¹–10²⁴ kg by the
assumed bounce law), so this is a candidate signal, not a hard number — but the
structure is real: TFT black holes are delayed rebounders, not eternal sinks.
**[derived scaling; observable model-dependent]**

## 4. The entropy — the area law derived, the ¼ a floor (`bh_entropy.py`)

The deepest piece, split honestly.

**The area law is derived and TFT-native [computed].** The puzzle of
black-hole entropy is that it scales with the horizon *area*, not volume. The
reason, computed here: the entropy is the **entanglement entropy of the phase
field's massless Goldstone across the horizon** (Srednicki's mechanism, applied
to TFT's own field). A radial-lattice calculation — build the Goldstone's
vacuum, trace out the interior, sum the entanglement over angular momenta —
gives **S ∝ R^1.9, the area law**, definitively not the volume law (R³). The
field's vacuum correlations are short-ranged, so only boundary-hugging modes
contribute → entropy tracks area. The holographic surprise falls out of the
phase field's ground-state entanglement, parameter-free.

**The coefficient ¼ is located, but not conjured [structural / floor].** In
induced gravity (Sakharov, Jacobson, Susskind–Uglum — TFT's lineage), the *same*
field fluctuations that give S_ent = C·A/ε² also *induce* 1/G = C′/ε²; the
Planck-scale cutoff divides out of the ratio, so S_ent = A/4G. The ¼ is
**inherited and tied to G by the one field — not a free fit** — but pinning it
to the last digit needs the phase field's exact induced-G spectrum. That is the
strain point, the direct analog of the Immirzi parameter in loop quantum gravity
or the microstate count in string theory: a constrained **floor**. The whole
coefficient reduces to one number — entropy per Planck cell = ¼ nat — which
reproduces S ~ 10⁷⁷ for a solar mass and S ∝ M² exactly **[consistency]**.

## A related falsifiable edge: dark energy cannot go phantom (`a0_de_study.py`)

TFT's dark energy is the *same* ultralight phase field, with the sine-Gordon
cosine potential — a pseudo-Nambu-Goldstone **thawing quintessence**, an ordinary
scalar, so **w ≥ −1 always: it cannot cross into phantom (w < −1)**
**[derived]**. The field mass that gives a₀ = cH₀/2π (~H₀) makes it just-thawing
now; matched to the observed w₀ = −0.88 it predicts **wₐ ≈ −0.24** with the field
mass ~0.72 H₀ — one field for both a₀ and the equation of state **[computed]**.
DESI's w₀wₐCDM fit prefers a *phantom crossing* (w < −1 in the past), which a
thawing scalar cannot produce. **The falsifier is sharp: if DESI DR2 / Euclid
confirm phantom crossing, TFT's dark energy is falsified; if the fit relaxes onto
the thawing track (w ≥ −1), it is confirmed.** A near-term yes/no.

## The ledger

| statement | label |
|---|---|
| horizon at r_s from TFT's own inflow rate reaching c | **derived route** (r_s = **consistency**) |
| time (= phase cycling) freezes at the horizon | **structural** |
| no singularity — a regular Planck-density core (bounded phase field) | **derived** (TFT-native) |
| the core bounces (φ⁶ degeneracy pressure); Planck-star burst | **computed** (observable model-dependent) |
| black-hole entropy ∝ area, from the Goldstone's entanglement | **computed** |
| S = A/4G — the ¼ is the induced-gravity coefficient, tied to G | **structural** (constrained) |
| dark energy cannot go phantom (w ≥ −1) — falsifier vs DESI | **derived** (falsifiable) |
| exact ¼; absolute scales (ℓ₀=ℓ_P?, Λ_cc, H₀); Kerr; full GR bounce | **floor / open** |

## The boundary, drawn honestly

TFT reproduces GR where GR is tested (r_s, the thermodynamic scales) and adds
distinctive, in-principle-testable structure where GR breaks down — no
singularity, a bouncing core, and a first-principles *area law* for the entropy.
What it does not do is conjure the absolute coefficients (the exact ¼, the
Planck scale, Λ_cc) from nothing — those are the framework's recurring floors,
open here as everywhere. Deriving the area law while honestly leaving the ¼ as a
constrained floor is the state of the art; no framework does better without a
tunable input.

## Reproduce

```bash
pip install numpy
mkdir -p outputs
python3 bh_study.py      # horizon (river model), frozen time, singularity-free core
python3 bh_bounce.py     # the core bounces (Planck-star burst scaling)
python3 bh_entropy.py    # entropy area law from the Goldstone's entanglement
python3 a0_de_study.py   # dark energy cannot go phantom (DESI falsifier)
```

Inputs: physical constants and the repo field only. Each script prints its
pre-registered gate and verdict; JSON lands in `outputs/`.
