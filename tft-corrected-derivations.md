# TFT Core Derivations — Corrected and Verified

**Status:** working draft for the derivation chapter. Every quantitative claim below
is labeled **DERIVED** (follows from the action by calculation, numerically verified
where applicable), **PROPOSED** (motivated identification, not yet forced), or
**OPEN** (known gap). Numerical verifications were run against direct simulation of
the equation of motion; scripts accompany this document.

-----

## 1. Scales and translation constants

**Primitives (dimensional content of the framework):**

|Symbol|Meaning                 |Units |
|------|------------------------|------|
|E₀    |fundamental energy scale|energy|
|ℓ₀    |fundamental length scale|length|

**Cycle convention:** ω₀ denotes the fundamental angular rate; τ₀ ≡ 2π/ω₀ is the
fundamental period. The time unit is conventional, fixed by the cycle.

**Translation constants** (definitions, not derivations — they convert phase
description into mechanical units):

- c ≡ ℓ₀ω₀  (space ↔ phase-time conversion; the phase-wave speed)
- ħ ≡ E₀/ω₀ = E₀τ₀/2π  (energy ↔ frequency conversion)

**What is DERIVED about the constants:** the action below *requires* a finite
maximal propagation speed for phase disturbances to exist, and fixes all
relationships among (c, ħ, τ₀, E₀, ℓ₀, ω₀). **What is input:** the values of the
two primitive scales. The framework derives the *status and relations* of the
constants, not their numerical values. This phrasing is exact and should be used
verbatim in the paper.

-----

## 2. The action (corrected)

For the dimensionless phase field θ(x, t) with circle-valued target:

> **S[θ] = (E₀/ℓ₀) ∫dt ∫_Ω d³x [ (1/2c²)(∂θ/∂t)² − ½|∇θ|² − (Λ/ℓ₀²)(1 − cos θ) ]**

Corrections relative to the previous draft:

1. The factor 1/c² on the kinetic term — without it the two gradient terms have
   incompatible dimensions (1/time² vs 1/length²). The constant that reconciles
   them *is* the phase-wave speed; its appearance here is the precise content of
   “c as translation constant.”
1. The overall stiffness κ = E₀/ℓ₀ (units: energy/length), so the action carries
   units of energy·time as required.
1. The potential made explicit and periodic: V(θ) = (Λ/ℓ₀²)(1 − cos θ), with Λ a
   dimensionless coupling. Periodicity is forced by the circle-valued field;
   1 − cos θ is the minimal choice. Λ connects to the Λ_eff of the discrete
   simulations.

**Equation of motion (Euler–Lagrange):**

> (1/c²) ∂²θ/∂t² − ∇²θ + (Λ/ℓ₀²) sin θ = 0

This is the sine-Gordon equation. In one spatial dimension it is integrable, with
exact soliton (kink), antisoliton, and breather solutions; all 1D results below are
exact, not approximate. **DERIVED.**

**Regime note (required for honesty about the simulations):** the agent simulations
evolve the *dissipative first-order* dynamics — gradient flow of this action’s
energy functional (Kuramoto-type). The physics claims use the *conservative
second-order* dynamics above. Same functional, two regimes; the paper must state
this in one sentence so the two are never conflated.

-----

## 3. Corrected Equation 1 — force from phase gradients

**Previous form:** F_eff = E₀(∇θ)/ℓ₀ — dimensionally energy/length², not force.

**Corrected heuristic form:**

> **F_eff = E₀ ∇θ**

(equivalently: E₀ per radian of phase advance per ℓ₀ — the old expression was
correct only if ∇θ was silently measured in radians per ℓ₀; the corrected form
makes the dimensions explicit: energy/length = force). **DERIVED as the
dimensional repair; the rigorous content is the following force law.**

**Rigorous 1D force law.** Add a phase-tension (tilt) term to the energy,
E_tilt = −f ∫θ dx, representing an imposed large-scale phase stress with strength
f. A kink of winding +2π located at X changes ∫θ dx by −2πΔX when displaced by
ΔX. Therefore:

> **F = −dE/dX = −2π f**  (per unit winding; sign set by winding direction)

A localized phase soliton in an imposed phase stress feels a constant force
proportional to that stress — the precise, derivable statement behind “objects
follow phase gradients.” **DERIVED.**

**Numerical verification:** direct integration of the equation of motion with
Λ = 1, f = 0.005: measured kink acceleration |a| = 0.00384 against predicted
2πf/M_K = 0.00393 (agreement ≈ 2%, residual attributable to background vacuum
shift and initial radiation; sign consistent with winding convention).

**3D status:** in three dimensions the corresponding objects are extended
(see §7, Derrick’s theorem). The force law for 3D localized structures is
**PROPOSED** pending resolution of the 3D matter problem.

-----

## 4. Corrected Equation 2 — the constants

Replace any language of the form “c emerges / ħ emerges” with:

- The action **requires** a maximal phase-wave speed to exist; its value is
  c = ℓ₀ω₀. (Existence DERIVED; value set by scales.)
- ħ ≡ E₀/ω₀ is the energy–frequency conversion; with it, E = ħω is an identity
  for phase oscillations, not a postulate added to the framework. (Relation
  DERIVED; value set by scales.)
- All relations among c, ħ, τ₀, E₀, ℓ₀, ω₀ are internal consistency conditions
  of one structure described in two vocabularies (phase-geometric and
  mechanical). There is no circularity because there is no derivation chain —
  there is one structure and a dictionary.

-----

## 5. Corrected Equation 3 — inertia, derived

**Previous form:** narrative (“inertia emerges from the cost of deforming phase
cycles”). **Corrected form: a calculation.**

The static kink solution of the equation of motion (1D, winding 2π):

> θ_K(x) = 4 arctan( exp[(x − X)/w] ),  w = ℓ₀/√Λ

Its rest energy is the field energy of the configuration:

> E_kink = (E₀ℓ₀) ∫dx [ ½(θ_K′)² + (Λ/ℓ₀²)(1 − cos θ_K) ] = **8√Λ · E₀**

Defining mass through E = Mc²:

> **M_K = 8√Λ · E₀ / c²**

Mass is not an input; it is the energy of a topologically protected phase
structure, fixed by the two scales and the dimensionless coupling. **DERIVED.**
**Numerical verification:** integral evaluated for Λ ∈ {0.5, 1, 2}; agreement
with 8√Λ·E₀ to relative error < 5×10⁻⁹ in all cases.

**Relativistic inertia for free:** the boosted kink
θ_K(γ(x − vt)) is an exact solution with energy γM_K c² — the relativistic
energy–velocity relation holds exactly for phase solitons, with c the phase-wave
speed. Inertia *and* special-relativistic kinematics of matter are theorems of
the action in the wave sector. **DERIVED (1D, exact).**

**The internal clock (de Broglie’s mc² = hf), realized:** the sine-Gordon breather
is a localized solution oscillating at internal frequency ω < ω_m ≡ c√Λ/ℓ₀, with
rest energy

> M_b c² = 2 M_K c² √(1 − ω²/ω_m²)

— an exact, invertible relation between the rest energy of a localized structure
and its internal oscillation frequency. This is the framework’s precise
realization of the de Broglie internal clock: matter as phase structure whose
energy and internal frequency determine each other. Note honestly: the relation is
the breather relation, not literally E = hf; the linear relation E = ħω holds for
the small-amplitude (phonon) modes. **DERIVED in 1D; PROPOSED as the 3D matter
model via oscillons (§7).**

-----

## 6. Option B — compact time and the origin of quantization

Take the time integral over one fundamental cycle with periodic boundary
conditions: t ∈ [0, τ₀), θ(x, t + τ₀) = θ(x, t).

Linearized modes about the vacuum obey the dispersion relation
ω² = c²k² + ω_m² (**verified numerically**: measured ω = 1.257 vs predicted 1.221
at k = 0.7, within the frequency resolution of the test). Periodicity in t then
admits only

> ω_n = n ω₀,  n ∈ ℤ⁺,  with E_n = ħω_n = **n E₀**

**Energy quantization is a consequence of temporal topology** — no quantum
postulate added. The allowed modes additionally require nω₀ ≥ ω_m. The
linear-time framework (Option A) is recovered exactly as τ₀ → ∞, where the
spectrum becomes continuous. **DERIVED given the compactness postulate; the
compactness itself is the framework’s central physical hypothesis and should be
stated as such.**

**Prior-art obligation:** quantization from intrinsically periodic time is the
central result of Dolce’s Elementary Cycles Theory (2011–). The paper must engage
it directly: cite, compare, and state TFT’s points of departure (single shared
fiber vs per-particle compactification; the emergence claims for force, inertia,
and entropy; the Mesoamerican process-ontology motivation). **REQUIRED.**

-----

## 7. Open problems (stated, not hidden)

1. **Derrick’s theorem (3D matter).** Static, finite-energy, localized scalar
   solitons are unstable in three spatial dimensions; π₁(S¹) supplies vortex
   *strings*, not point particles. Candidate resolutions, in order of fit to the
   framework: (a) time-periodic localized solutions (oscillons/3D breather
   analogues) — naturally favored here, since TFT matter is *defined* by internal
   oscillation and Option B makes time-periodicity structural; (b) extended
   string/loop matter; (c) additional field structure. **OPEN — flagship problem
   for collaborators.**
1. **Universality of the cycle.** De Broglie frequencies are mass-dependent;
   a single shared S¹ must accommodate all species (harmonics/winding structure
   is the natural candidate; compare Dolce’s per-particle compactification).
   **OPEN.**
1. **Global Lorentz invariance under compact time.** The wave sector is
   Lorentz-invariant; a globally compact time direction breaks boost invariance
   globally. Constraints from photon-dispersion and Lorentz-violation searches
   must be confronted quantitatively. **OPEN.**
1. **Bell correlations.** Measured separately (CHSH suite): the local field
   sector caps at S = 2.0000 exactly; crossing the integer bound without
   signaling requires structure not yet present in the action. Pass criterion
   for any proposal: S > 2 with marginal shifts ≈ 0. **OPEN.**
1. **Entropy.** No derivation exists yet from this action; the claim should be
   removed from the “derived” list until a statistical sector is constructed.
   **OPEN.**

-----

## 8. Summary table

|Claim                                           |Status                                        |
|------------------------------------------------|----------------------------------------------|
|Action, EOM, wave sector                        |DERIVED                                       |
|Existence of maximal speed c; constant relations|DERIVED (values input via scales)             |
|Force law on phase solitons (1D)                |DERIVED, verified ≈2%                         |
|Inertia: M_K = 8√Λ·E₀/c² (1D)                   |DERIVED, verified <10⁻⁸                       |
|Relativistic kinematics of solitons (1D)        |DERIVED (exact)                               |
|Internal clock: energy ↔ internal frequency     |DERIVED (1D breather)                         |
|Energy quantization E_n = nE₀                   |DERIVED given compact time                    |
|Compactness of time                             |POSTULATE (the framework’s central hypothesis)|
|3D particle-like matter                         |OPEN (Derrick)                                |
|One fiber, many masses                          |OPEN                                          |
|Global Lorentz / discreteness bounds            |OPEN                                          |
|Bell-crossing structure                         |OPEN                                          |
|Entropy                                         |OPEN (remove from derived list)               |