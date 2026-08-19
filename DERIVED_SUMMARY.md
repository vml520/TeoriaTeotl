# TFT-Classical — Summary of Derived Results

*As of 11 July 2026. Digest of derived results, each routed to a runnable check.*
*Labels: **DERIVED** (from the field, rigorous) · **DELIVERED** (works, see caveat) · **PROPOSED** (reframing, not proof) · **INPUT** (a value the framework does not fix) · **OPEN** · **FAILED** (do not repeat).*

**The one meta-lesson (read this first if you're building another TFT app):** TFT reliably derives **structures, mechanisms, and scale *relations* — parameter-free**. It does **not** derive **absolute values**: every absolute number we chased (Newton's G, |Λ|, a₀'s exact coefficient, the baryon asymmetry η) bottomed out at a *named, field-wide* open problem (quantum gravity, the cosmological-constant problem, the coincidence problem, the baryogenesis initial condition). So: expect to derive the *mechanism and the scaling*, and to carry *one calibration constant / initial condition* per absolute scale. That is not a TFT weakness — those numbers are unsolved everywhere.

> **Sharpened 18 Aug 2026 — the split is not "structure vs absolute". It is SYMMETRY PROTECTION.**
> The framework's field is ψ = ρe^{iθ}, and its two sectors are protected differently:
> - **The phase θ is a pseudo-Nambu–Goldstone boson.** A shift symmetry θ → θ + c protects it, so
>   radiative corrections to its mass are *proportional to the symmetry breaking itself*. **A small
>   mass is technically natural** — it stays small once it is small. This is why axions are light,
>   and it is why the tiny number in the phase potential (κ = 2N·Λ, which at the paper's N = 1/2 is
>   **κ = Λ = 8.71×10⁻¹²²** exactly) is not a tuning in the usual sense.
> - **The amplitude ρ is an ordinary radial mode with no protecting symmetry.** Corrections go as the
>   cutoff, δm² ~ Λ_cut²/16π², dragging it to **f/(4π) ≈ 9.7×10²⁶ eV**. Placing the electron at
>   511 keV requires a tuning of **~3×10⁻⁴³**.
>
> **The map onto this document is exact:**
>
> | claim | sector | protected? | status here |
> |---|---|---|---|
> | dark energy w ≥ −1; a₀ = cω₀/2π; charge quantisation; CHSH, Born, number–phase | **phase** | **yes** | **DERIVED** |
> | lepton mass absolutes; v_EW; r ≈ 0.318, A ≈ √2 | **amplitude** | no | **FLOOR** |
>
> **Every derived claim sits in the protected sector; every floor sits in the unprotected one.**
> So the floors are not a scattered list of stubborn numbers — **they are one sector, identified by a
> single property. TFT derives what a shift symmetry protects, and floors on everything else.**
>
> **What this does NOT say.** It does not say the mass program is wrong. Its near-cancellation
> mechanism ("the electron is 99.85% winding-odd") organises the *spectrum* and does so well — tau
> 98% even against electron 0.15% is a factor ~653, the right order for m_τ/m_e = 3477. **But an
> even-fraction of 1.5×10⁻³ is 2.8 orders of suppression against the 22.7 needed to reach the
> electron from f.** It is a *ratio* mechanism, which is what it was built to be; **it was never an
> absolute-scale mechanism, and should not be read as one.**
>
> **What would be needed.** The open question is not "derive m_e" but **"why is the radial mode
> light?"** The known answers are a protecting symmetry or a dynamically generated scale. TFT has
> neither in the amplitude sector: dimensional transmutation is closed (the scalar quartic runs to a
> Landau pole, not to zero — no asymptotic freedom), and instanton effects generate potentials for
> *pseudo-scalars*, not masses for radial modes, so **the mechanism that plausibly explains the phase
> sector cannot be transported to the particle sector.** Supplying one is a research programme, not a
> calculation.

---

## 0. Regime that works
Productive regime: the **conservative** second-order field, then a **complex** field ψ = ρe^{iθ}. The **dissipative** (Kuramoto) and **topological-knot** attempts all failed — see §10. Don't restart there.

## 1. Foundational machinery (from the founding TFT paper)
Two scales **E₀** (phase-energy) and **ℓ₀** (coherence length) organise everything below:

> **Framing correction (15 Aug 2026).** This line previously read *"Two primitives … everything
> else derives."* **E₀ and ℓ₀ are not free primitives, and c is not among the things that derive
> from them.** The framework's own three relations — ℏ = E₀τ₀/2π, ℓ₀ = cτ₀, G = ℓ₀c⁴/E₀ — are
> three equations in three unknowns with three *imported* constants, so E₀, τ₀ and ℓ₀ are
> **determined by {ℏ, c, G}** (as √(2π) × the Planck values). In particular **E₀/ℓ₀ = c⁴/G
> identically**, so relations of the form "X follows from the primitives" are frequently
> G = ℓ₀c⁴/E₀ read backwards. The line below reading c = E₀/p₀ should be understood the same way:
> it fixes p₀ given c, not c. **What survives is that E₀ and ℓ₀ are a useful organising pair and
> that the relations below are internally consistent — not that they are an independent
> starting point.**
- dτ = ℏdθ/E (time = phase per energy); dℓ = ℏdθ/p (length = phase per momentum)
- g_eff = E₀/ℓ₀; c = E₀/p₀; m = E₀/c²; ℏ = E₀τ₀/2π
- Force is an emergent process, not fundamental: **F = −E₀∇θ**, equivalently
  **F/F_Planck = ℓ₀|∇θ|** — every force is the Planck force times the dimensionless phase strain.
  - *Corrected 18 Aug 2026:* this previously read **F = −g_eff∇θ**. **That is dimensionally
    inconsistent**: g_eff = E₀/ℓ₀ is *already* a force (energy/length), so g_eff∇θ has dimensions of
    force per length. The consistent form carries one factor of ℓ₀, giving F = −E₀∇θ. **No result
    changes** — every computation in this repository was done in code units where the distinction is
    invisible — but the stated law was wrong as written. *(Noted alongside: since E₀/ℓ₀ = c⁴/G
    identically, and the phase gradient is separately taken to be bounded by |∇θ| ≲ 1/ℓ₀, this form
    implies F ≤ c⁴/G — the same posited bound that gives the Planck-density cap in `BLACK_HOLES.md`,
    read as a force instead of a density. One assumption, two consequences; not independent
    evidence.)*
- Gravity = geodesics of an **emergent metric** sourced by the field's energy.
- Premise: mass = a real periodic process, mc² = hf ⇒ ω = mc²/ℏ.
- **The second is fixed by the framework's own relations, not chosen** (`verify_units_closure.py`, 1 Aug 2026). ℏ = E₀τ₀/2π together with ℓ₀ = cτ₀ determine it, so no result here can carry a hidden unit convention — a units error would surface as a *dimensional mismatch*, not as a tension. Every gate runs in code units (ℓ₀ = c = E₀ = 1); the only carriers of 's' in the repo are c, ℏ, H₀.
  - **Correction (15 Aug 2026):** this bullet previously read *"the SI second is **derived, not imported** … from the two primitives."* **Both halves overstate.** The second follows from *three* relations — ℏ = E₀τ₀/2π, ℓ₀ = cτ₀, G = ℓ₀c⁴/E₀ — and the second of those **asserts** c rather than deriving it, so the construction is circular in c. And E₀, ℓ₀, τ₀ are not free primitives: three relations in three unknowns with three imported constants leaves them **fully determined by {ℏ, c, G}**. The operative content of this bullet is unaffected and still holds: the units are internally consistent, and the standing tensions are provably unit-immune (see below).
  - *Consequence — **INFERENCE**, see §4 and §9:* feeding in G = ℓ₀c⁴/E₀ closes the system — G = 2πℏc⁵/E₀², hence **E₀ = √(2π)·E_Pl, ℓ₀ = √(2π)·ℓ_Pl, τ₀ = √(2π)·t_Pl** (all three ratios 2.506628, exact as algebra, independent of the CODATA values). The 2π is the **circumference of the compact time-circle** — the same 2π as in a₀ = cH₀/2π and in ℏ = E₀τ₀/2π: the primitives are the Planck units dressed by one trip around S¹. **Conditional on G's O(1) coefficient being 1, which is the open quantum-gravity step — this does not derive G.**

## 2. DERIVED — particle sector
- **Kink rest mass M_k = 8√Λ·E₀** (exact to 1e-9); **force law a = −2πf·Q/M_k** (F=Ma, ~2%). Mass & force from the field, nothing by hand.
- **Breather**: time-periodic "particle-wave," mass M_b = 2M_k√(1−ω²) entirely in the motion (exact only in 1D — integrable).
- **3D oscillon radiates** (pure phase field can't hold a localized 3D wave — no conserved charge). [DERIVED negative]
- **3D Q-ball persists** (complex field + U(1) charge → stable localized 3D particle). *Caveat: uncharged control also persisted on the tested timescale.*

## 3. DERIVED — the two force sectors from one distinction
The complex field has **two conserved currents**:
- **U(1) Noether current** j^μ = ρ²∂^μθ — *linear*; charge j⁰ = ρ²ω is **signed** → **Electromagnetism** (Coulomb 1/r², like-charges **repel**, massless Goldstone mediator). ✅ **Re-verified 18 Aug 2026 (CHRG1):** the interaction energy computed directly from ½∫|∇θ|² gives like-charges repelling and unlike attracting, matching the analytic Coulomb cross term 4πq₁q₂/d. *(This is electrostatic gradient energy ½∫|E|², not scalar exchange — the "even-spin exchange attracts" intuition does not apply.)* **CHRG1 established that this — not the winding — is TFT's electric charge.**
- **Energy–momentum** T^μν — *quadratic*; T⁰⁰ ~ ρ²ω² is **positive-definite** → **Gravity** (universal).
Consequence (correct vs experiment): matter (ω) & antimatter (−ω) have opposite charge, identical energy → **both gravitate attractively** (matches CERN ALPHA-g 2023).

### 3b. The Coulomb barrier, and what tunnelling through it does and does not give (5 August 2026)
**Where the barrier comes from [derived].** Two same-sign windings cannot relax their relative phase gradient, and the field energy ½ρ²|∇θ|² is positive-definite, so the cost is positive and rises monotonically as they approach — **calculated:** E(++) rises 93.0 → 100.1 as separation falls 3.0 → 1.2 while E(+−) falls 88.0 → 82.6. Nothing electrostatic is assumed: **the repulsion is the field's own energy refusing to go down**, and the Coulomb barrier is that refusal.

**Penetration [exponent yes, prefactor no].** Barrier penetration is a Euclidean-action calculation. **Calculated against alpha-decay half-lives spanning 24.2 orders of magnitude** (²¹²Po 3.0e-7 s → ²³²Th 4.4e17 s), regressed on G = 2πZ₁Z₂α√(μc²/2Q): **slope 0.865 against a predicted 1.000, R² = 0.9996, nothing fitted.** The exponent comes out. The **intercept does not** — it is an absolute rate and needs E₀/ℓ₀, the same floor as Newton's G coefficient (§1, §9). Slope yes, intercept no: the programme's recurring signature.

**Short distance.** The 1/r form holds until winding cores overlap, at a scale tracing to ℓ₀ ≈ 4e-35 m — **19.7 orders below nuclear contact (2e-15 m)**. So **no observable modification of the barrier at 1–2 fm** is predicted. This follows from the absolute-scale floor, not from any modelling choice.

**Macroscopic tunnelling — calculated, for the record.** The requirement is ΔE·L² ≤ (ħ ln(1/P))²/8m, so only the *product* matters (formula calibrated first against a known case: a 1 eV barrier 1 nm wide admits 1.82 electron masses — an STM). For a **1 gram** sphere at P = 1e-6: at any laboratory width the admissible barrier is **~10⁻²⁵ of kT** — which is not a barrier at all, being 10²⁵ times below thermal noise. A *real* barrier becomes crossable only at Planck-scale width (~1.0 MJ at ℓ_Pl). Against an ordinary barrier (1 J, 1 mm) the suppression is **10^(−3.7e29)** — one attempt per Planck time since the Big Bang gives ~10⁶¹ attempts, so the shortfall is **28 orders of magnitude in the exponent itself**. For scale, 1 g is **19 orders of mass** beyond the heaviest object ever shown to interfere (~25,000 amu, Fein et al. 2019). **The operative obstacle is not this exponent but coherence** across ~5e22 constituents — see `FOUNDATIONS_AND_LIMITS.md` §3, where the assumption that a decaying amplitude helps with that is calculated and withdrawn.

## 4. DERIVED — gravity's shape and sign
- **1/r potential**: the metric potential is **Poisson-sourced** by energy density, ∇²Φ = |∇θ|² (the paper's error was setting Φ *equal* to |∇θ|² → wrong 1/r⁴). Gauss's law → far field ∝ total enclosed energy = mass → Φ ~ −M/(4πr). Measured: Φ~1/r, force~1/r².
- **Universal attraction**: energy density ≥ 0 → always an attractive well. Why neutral matter cancels EM charge but adds energy.
- **G as squared rate of time** (PROPOSED reframing): G·ρ = T⁻² so √(Gρ) is a rate; G = ω_P²/ρ_P (Planck frequency² / Planck density). Recasts "derive G" as "what sets the vacuum's cycling rate." G's coefficient itself = the quantum-gravity problem (OPEN everywhere).
  - *Sharpened 1 Aug 2026 (`verify_units_closure.py`, INFERENCE):* with ω₀ ≡ 1/τ₀ and ρ₀ ≡ E₀/(c²ℓ₀³), **G = ω₀²/ρ₀ holds exactly in TFT's own primitives** — the "rate of time" is literally the **inverse compact-time period**, not a borrowed Planck frequency, so the reframing is native rather than a Planck-unit coincidence. Same condition as §1: it assumes G = ℓ₀c⁴/E₀ with coefficient 1, and **the coefficient stays OPEN** (§9).

## 5. DELIVERED — the toy solar system (`tft_solar_system.py`)
Planets as **geodesics** of the Sun's emergent metric. **One** frozen constant K = G·M_sun = 4π² (1 AU→1 yr); G not derived (allowed). Output: 8 periods ≤0.06%, Kepler III T²/a³=1.0000, **Mercury 42.90″/cy** (obs 42.98). *Caveats: Kepler is by-construction (any 1/r); Mercury 43″ is the generic 1PN result, not unique to TFT.*

## 6. DERIVED — galaxy rotation curves without dark matter (a₀ program G0–G5)
- **The derived-Newtonian sector FAILS** the Milky Way (32% off, baryons only) — same dark-matter problem as Newton. The fix is not in that sector.
- **a₀ = cH₀/2π = 1.08×10⁻¹⁰ m/s² is DERIVED, not fitted** (MOND *fits* a₀): the phase field is **ultralight** (mass gap m = √Λ/ℓ₀ = the Hubble mass ⇒ Compton wavelength = Hubble radius ⇒ Λ ~ 10⁻¹²²). Its Compton frequency = H₀/2π (2π = h/ℏ = one S¹ cycle) → a₀ = c·f = cH₀/2π. **This is Vic's "α from Λ."** Effectively massless below the cosmic scale (→ §4 gravity), biting only at a₀. **Tested per-galaxy against SPARC** (`verify_a0_sparc_fit.py`, 2696 pts / 147 galaxies): our own log-space RAR fit gives g† = 1.16×10⁻¹⁰ (deep-MOND 1.33×10⁻¹⁰); the derived a₀ = 1.04–1.13×10⁻¹⁰ sits at **0.90–0.97 × g†**, scatter 0.133 dex (lit ~0.12) reproduced, scale universal where constrained → **consistent within ~20% systematics** (M/L, distances), nothing fitted to SPARC.
- **Self-consistency (G2):** if that field *is* the dark energy (Friedmann), Λ cancels → a₀ ∝ cH₀ without solving the CC problem.
> **Correction (16 August 2026) — the status of the mechanism below.** The horizon argument is a
> **heuristic**, and four studies have now established that it cannot be derived as stated.
> (i) Modified inertia requires **time-nonlocal** equations of motion (Milgrom, *Phys. Rev. D* **106**,
> 064060, 2022); the argument below is **instantaneous**, so it is not modified inertia in that
> sense — nor modified gravity, since it does not touch the Poisson equation. (ii) **No local action
> can produce m_eff = m·μ(a/a₀)**: μ is non-analytic in |a|, and higher-derivative terms give
> higher-*order* equations, not a rescaled mass. (iii) A retarded self-interaction — the one native
> nonlocal structure — does not supply it either: the static self-energy is UV-dominated and
> insensitive to any horizon cutoff, while the radiation-zone energy is a *radiated* energy carrying
> a², which cut at c²/a gives a total derivative and cut at c/H₀ gives a higher-derivative term.
> (iv) A memory kernel of any kind organises physics by **rate**, giving a transition at fixed
> angular frequency (v ∝ R), whereas the observed transition is at fixed **acceleration** (v ∝ √R) —
> and SPARC confirms this directly: acceleration organises the mass discrepancy **1.6× more tightly**
> than frequency (0.134 vs 0.215 dex within-bin scatter). **The heuristic's step from "fraction of
> the deformation inside the horizon" to "fraction of the inertia" is where the argument actually
> lives, and no self-energy calculation supplies it.** The deep-MOND limit and Tully–Fisher slope
> below follow from the *interpolation law* and are unaffected; what is withdrawn is the claim that
> the mechanism is derived. Anyone attacking this should start from Milgrom's nonlocal-functional
> construction, not from a field-theoretic self-interaction.

- **Mechanism = modified inertia** ("inertia saturates"): inertia is cut off by the smaller of the acceleration horizon c²/a and the cosmic horizon c/H₀ → below a₀, μ → a/a₀ → **deep-MOND a = √(a_N a₀)** → flat curves + **baryonic Tully-Fisher V⁴ = GMa₀, slope exactly 4** (SPARC: 3.85±0.09).
- **Fits:** Milky Way 2.9% (baryons only, derived a₀); **consistent with the SPARC RAR** within its 0.13-dex scatter.
- **The modified-inertia signature was searched for in SPARC and is NOT there** *(added 18 Aug 2026)*. Modified inertia makes the mass discrepancy depend on the orbit as a whole, so at *fixed* g_bar the residual should still vary with radius **within a single galaxy**; modified gravity makes it a function of local g_bar alone, so it should not. Testing that on **131 galaxies / 3032 points** (SPARC quality Q ≤ 2, inclination ≥ 30°, ≥ 8 points each; pipeline control: global RAR fit g† = 1.02×10⁻¹⁰ m/s² against the literature 1.2×10⁻¹⁰): **mean per-galaxy ρ(R, residual) = +0.028, median −0.031, 51% negative, p = 0.54.** Consistent with **zero radial trend**, and the sign **flips** between quality cuts (Q ≤ 2: +0.028; Q = 1 only: −0.034), so there is no stable effect. **This does not refute the mechanism — the test constrains a *signature*, and the same radial axis is also tilted by M/L gradients, bulge/disk decomposition and beam smearing — but the distinctive prediction that would have favoured modified inertia over modified gravity is not detected.** *(A first attempt combined the per-galaxy correlations by Fisher weighting, giving an apparent p = 6×10⁻¹⁴; that statistic assumes the radial points are independent, which smooth rotation curves are not, and it is withdrawn.)*
- **Caveats/OPEN:** exact a₀ coefficient = ω₀/H₀, a natural quintessence O(1) → the **coincidence problem**; the interpolation *shape* is model-dependent (as in MOND); a rigorous action-level derivation and a per-galaxy χ² (needs raw SPARC data) are open.

## 6b. Black holes + the dark-energy falsifier (13 July 2026)
Full record: `BLACK_HOLES.md`. **Reading two derived facts — √(2GM/r) = the inflow rate of space, and time = phase cycling — gives a complete black hole.**
- **Horizon [derived route]:** the inflow rate reaches c at r_s (river/Gullstrand-Painlevé, from TFT's OWN rate); **time freezes at the horizon** (rate ∝ √g₀₀ → 0 = literal frozen star). r_s and thermo scales = consistency w/ GR.
- **NO SINGULARITY [TFT-native]:** the bounded phase field (|∇θ|≲1/ℓ₀, finite amplitude) caps the density at ~Planck density → a **regular Planck-density core** (r_core ~ 4.5e-23 m solar, regular-BH/Planck-star family) — distinctive vs GR's point singularity.
- **The core BOUNCES [computed]:** a squeezed Q-ball breathes/oscillates (φ⁶ high-density repulsion = field degeneracy pressure) — same boundedness that resolves the singularity; time-dilated → Planck-star delayed burst (PBH ~6e22 kg bounces now, mass model-dependent).
- **Entropy [computed area law + floor]:** S ∝ **area** (S~R^1.9, computed as the phase Goldstone's entanglement entropy, Srednicki — WHY BH entropy is holographic); the **¼** = the induced-gravity coefficient (S_ent=A/4G, ε cancels because one field gives S_ent AND G) — inherited/constrained, exact value a floor (cf. Immirzi). Magnitude ~1e77 solar, S∝M² reproduced.
- **Dark energy CANNOT go phantom [derived, falsifiable]:** DE = the same phase field (pNGB thawing quintessence, ordinary scalar) → **w ≥ −1 always** (integration: w_min=−1.0000); matched to w₀=−0.88 → wₐ≈−0.20 (re-integrated 15 Aug 2026 at the corrected decay constant; supersedes −0.24; −0.196 as −dw/da, −0.168 under a CPL fit; insensitive to f at the 9% level over f = 1.5–10 M_Pl), mass ~H₀ (a₀-consistent, one field both). DESI's CPL prefers phantom crossing (w<−1 past) → **sharp falsifier. STATUS (DR2, 2025): in tension.** The evolving-DE preference firmed 2.6σ (DR1, DESI+CMB) → 3.1σ (DR2), 2.8–4.2σ +SNe; DR2 best fit w₀=−0.838±0.055, wₐ=−0.62 crosses w=−1 in the past and DESI reports non-phantom models **disfavoured**. TFT agrees DE evolves (both reject ΛCDM); they part on wₐ's magnitude. The prediction w≥−1 stands and the current data do not meet it — if the crossing hardens (DR3/Euclid), TFT's DE sector is excluded. **Refreshed 2026-08-07:** DESI DR2 Results IV (+full-shape Lyman-α, arXiv:2607.27410) gives **2.7σ (DESI+CMB) / 3.2σ (+SNe)** — *softer* than the earlier 3.1σ / 2.8–4.2σ, recorded because it happened rather than because it helps. Direction unchanged: arXiv:2510.21976 finds every parameterisation at w₀>−1, wₐ<0, **w₀+wₐ<−1** (Quintom-B = phantom past → quintessence now = a crossing). Easing from 4.2σ to 3.2σ is still a tension; nothing has approached 5σ either way.

## 7. PARTLY WITHDRAWN — baryogenesis / magnetogenesis / chirality (BMC G1–G2)

> **Corrected 18 Aug 2026 (BMCA0 audit).** This section previously read *"DERIVED — …= one
> topological invariant."* **The headline identification is false and is withdrawn.** Baryon number
> ΣW is *linear* in the windings and blind to linking; helicity (2π)²ΣWᵢWⱼLkᵢⱼ is *quadratic* and
> depends on linking. They are **two independent invariants of one object, plus a sign** — not one
> invariant with three faces. Both counterexamples are explicit: two unlinked W=+1 windings give
> **B=2, H=0**; a linked W=+1/W=−1 pair gives **B=0, H=+8π²**. The G2 results table below in fact
> *shows* this — B is constant at 2 down the whole column while H sweeps −8π² to +8π² — and was
> captioned as demonstrating the opposite. Verified with an independently written Gauss linking
> integral that reproduces G2's own three rows exactly (`bmca0_audit.py`).
> **The topological machinery is sound and is kept; what fails is the claim that it is one thing.**
- The minimal action is **CP-symmetric** → chirality not *forced* (matter = antimatter).
- The chiral invariant **exists** = the **helicity (linking number) of winding lines** (Lk = ±1 handed / 0 unlinked; CP flips its sign). This is Vic's **"chirality from winding directions."**
- **Two invariants and a sign** (corrected): ~~baryon number = winding charge ΣW~~ (**further corrected 18 Aug 2026, CHRG0/CHRG1: W is neither baryon number nor electric charge — it is the vortex/self-linking charge. See the winding row below; baryon number has no topological carrier, and electric charge is the Noether charge**); magnetic helicity = flux linking (2π)²ΣWᵢWⱼLkᵢⱼ (since A=∇θ ⇒ winding lines are flux tubes, Φ=2πW); chirality = sign of the helicity. **The third genuinely is a face of the second. The first is independent of both.**
- **The chiral anomaly is NOT automatic and NOT derived** (was: *"automatic in TFT, not a postulate"* — **withdrawn**). Two independent reasons. **(i)** Every transition among G2's own three configurations has ΔB = 0 with ΔH ≠ 0, so the claimed ΔB = −κΔH forces **κ = 0**. The deeper reason is structural: winding number is *conserved* under continuous deformation — that is what makes it topological — so **it cannot supply the anomalous non-conservation an anomaly exists to describe.** **(ii)** The chiral anomaly is a fermion-loop effect, and **there are no fermions in this construction**; G2 imports the coefficient N_f explicitly. What G2 actually establishes is a structural **analogy** to the B/N_CS pair — genuine and reusable, but not a derivation.
- **No mechanism exists for either genesis.** G1 found the minimal action *exactly* CP-symmetric, so net chirality is not forced; **G3 (net-winding mechanism) and G4 (coherent helical large-scale field) were never run.** And since A = ∇θ makes B = ∇×∇θ vanish except distributionally on the winding lines, TFT's "magnetic field" is supported on a set of **measure zero** — a static identification of vortices with quantised flux tubes, not a genesis and not a large-scale field.
- **INPUT/OPEN:** the *net* helicity generated → magnitude of η ≈ 6×10⁻¹⁰ (an initial condition; this flag was pre-registered at G0 and was honest). *More speculative than the gravity work.*
- **What survives:** quantised flux Φ=2πW on winding lines; helicity as a genuine invariant; chirality = sign H; the CP-symmetry result; and η's magnitude as an IC. **What does not: the one-invariant claim, the automatic anomaly, and both "genesis" labels.**

## 7b. The generations & mass-hierarchy program (11–12 July 2026)
Full gated record: `GENERATIONS_PROGRAM.md`. Headlines:
- **Koide characterization DERIVED, exactly:** all three lepton masses = one scale + 120° phases + ONE angle ε = 2.2677° from an exact cancellation point; the **electron is anomalously light** (m_e ∝ ε², the near-null direction of a nearly singular generation matrix); at exact cancellation m_τ/m_μ → (2+√3)² = 13.93 (closed form).
- **EXCLUDED (pre-registered gates):** Koide's balance from ring symmetries/dualities, from local energetics, and from collective/zero-mode dynamics (G3–G5); generations as excitation towers, 1D exact and 3D numerical (SP1–SP3) — excitation ratios cap at ~2 and Q hugs 1/3.
- **DERIVED (structural positive):** the framework's Q-ball possesses a three-state equal-charge tower (the right state-space) and binds a localized internal "generation dial" whose energy is exactly a real amplitude squared — the interference mechanism EXISTS (M2′); the data itself forces real, sign-changing interference.
- **DERIVED within the construction (M4):** the cancellation point = a pure winding-reversal-ODD state (electron 99.85% "helical"); antiparticle family spectrum identical automatically; **couplings = winding integers (universal) vs masses = amplitudes (hierarchical)** — exact lepton universality + 3477× hierarchy simultaneously, as observed.
- **The ε sub-program (E-arc):** topological quantization of the offset **EXCLUDED** (E1, 212σ — the offset is not a winding fraction of a turn); ε's origin must be **Z₃-symmetry-respecting** (E2 rigidity theorem; all symmetry-breaking bounded to ~10⁻³ by Koide's precision) and lives in **one interference channel** (κ₃cos3α+κ₆cos6α) whose pitchfork threshold (r > 1/4) is what makes the electron light — a threshold crossing that also spontaneously gives the particle/antiparticle mirror pair; Koide/ε is an **on-shell (pole-mass)** structure (E4, degrades ~186× under running).
- **Where r lives (soliton-interior study, `WHERE_R_LIVES.md`):** r is a gauge-invariant **flux**, not a mass-sum (Σm, Σ√m exactly δ-independent) → the loose three-lump "molecule" picture **EXCLUDED**, r's seat = a single *merged* soliton. Its carrier is a **computed, validated bound triangular (ℓ=3) internal mode** (Bogoliubov–de Gennes spectrum; solver validated on Goldstone + translation zero modes; bound only in the large-charge regime). A single-mode condensate has a **flat** dial (rotational Goldstone) → **r is intrinsically a two-sector (three-fold × six-fold) relative phase / flux** — the most protected place, which is why it survived symmetry, energetics, collective, topological, AND single-mode arguments; needs a current-carrying / higher-charge configuration to exist.
- **OPEN (the honest floor):** the values A ≈ √2 and the ratio r ≈ 0.318 — one continuous ratio carries the whole lepton-spectrum mystery; not fixed by symmetry, energetics, collective dynamics, topology, or any single-mode condensate; waits on the full nonlinear soliton interior (like G, |Λ|, a₀'s coefficient). Falsifiable anchor: δ−120° = 2/9 rad (pole-mass, 0.9σ), tested by a ~10× better τ mass. **Terminus (`spec_selfconsistent.py`): r (=A) bottoms out at the generation-mode EXCITATION AMPLITUDE — an initial-condition floor, same class as η, not dynamically derived.**

## 7c. The particle sector — what particles are (12 July 2026)
Full record: `THE_PARTICLE_SECTOR.md`. **One linking invariant (the derived winding-line helicity of §7) carries spin, statistics, baryon number, and chirality at once.** Headlines:
- **Fermions from a bosonic field [derived]:** a spherical Q-ball is a spin-0 BOSON; a twisted vortex loop with ODD self-linking is a spin-½ FERMION (Finkelstein–Rubinstein). Linking computed as parameter-free topology (Hopf link ±1, twist=winding). So leptons are vortons/Hopfions (odd linking), NOT plain Q-balls — the Q-ball was only the mass/charge skeleton. (Resolves: the mass work modeled leptons as bosons.)
- **Neutrinos & parity [derived], no SU(2):** the neutrino = the pure winding-ODD (massless-chiral) limit of the SAME lepton dial (electron 99.85% there; its 0.15% even content IS its mass). Parity violation FORCED — winding reversal flips the odd channel → weak coupling is 100% V−A, no ν_R. Large PMNS / small CKM from ν near-degeneracy vs charged-lepton hierarchy [proposed].
- **Confinement [computed]:** quark = winding-line end; no free end; sine-Gordon term → domain wall of tension σ = 8√Λ = the DERIVED kink mass → linear V(L)=σL. Meson=boson, baryon=fermion (linking parity). ONE scale √Λ sets both hadron mass AND confinement tension (as in real QCD).
- **FLOORS (the honest boundary):** absolute scales (ν-mass, Λ_QCD) and NON-ABELIAN groups (SU(2)_L for the full weak force, color SU(3) for the full strong force, fractional charge) — the U(1) field gives integer charge (from the number/Noether spectrum — *noun corrected 18 Aug 2026, UNC1; this read "integer winding"*) and derives mechanisms/scale-relations, not absolutes or non-abelian structure. Same pattern as G, |Λ_cc|, a₀-coeff, η. **See §9's consolidated sub-Planckian mass floor** — the absolute-scale gap is now stated as one problem (a Planckian condensate at f = M_Planck ≈ 1.22×10¹⁹ GeV against particle masses 17–22 orders below it) rather than a list.

## 7d. Quantum correlations from compact time (13 July 2026; Born rule 14 July 2026)
Full record (with prominent caveats): `QUANTUM_FROM_COMPACT_TIME.md`. **The local field saturates CHSH at S=2.0000 (classical); compact time DERIVES the quantum value AND the Born rule.**
- **The correlation:** TFT's S¹ is a SINGLE-VALUED COMPLEX PHASE. Single-valuedness fixes the loop phase difference; the hidden variable CANCELS → E(a,b)=cos(a−b) (quantum form, NO tuning, no-signaling). A coherent phase = Hilbert space → **Tsirelson caps CHSH at 2√2 automatically** (numerically 2.828; the naive arbitrary-reweight overshoot of 2.90 is FORBIDDEN once the phase is genuine). Quantum coherence = the phase closing single-valuedly on the S¹ time circle → makes precise "quantum uncertainty = ordinary deterministic S¹ behaviour."
- **The Born rule (`born1..5_*.py`, pre-reg `BORN0_prereg.md`):** single-outcome |ψ|² DERIVED from the same closure. Equal amplitudes → equal weights by an EXACT envariance symmetry (pure-environment counter-swap unitary iff |c₀|=|c₁|), no |c|² inserted; **|c_k|² for all amplitudes from that symmetry alone**, exponent 2 = coherent-superposition normalization (equal branches carry 1/√n ⇒ count=1/amp²), not a charge postulate; continuous **Malus P(+|θ)=cos²(θ/2)** uniquely pinned by E=cos θ (other exponents break it); ONE rule |⟨·|Ψ⟩|² gives marginals+no-signaling+E=cos(a−b)+Tsirelson+Malus. Born reduced to the S¹ swap symmetry + additivity.
- **The uncertainty principle (`uncertainty_s1.py`) — the THIRD pillar, DERIVED, no degeneracy caveat:** the single-valued S¹ phase makes the **number/Noether** operator N=−i∂_θ integer (charge quantization) *(noun corrected 18 Aug 2026, UNC1 — this read "the winding". N=−i∂_θ generates phase rotations, so it is the Noether/number charge, not the topological winding; Carruthers–Nieto, cited in the same sentence, call it the number operator. **This is what actually quantises electric charge** — see the withdrawn-then-restored bullet in `PREDICTIONS.md`.)* with exact [N,cosθ]=i sinθ → the Carruthers–Nieto number–phase uncertainty **ΔN·Δθ ≥ ½**, verified for all states, saturated by von Mises (minimum-uncertainty) states, → Heisenberg ½ in the localized limit (0.500). Physical tradeoff: definite charge/winding ⇒ uniform/undefined phase. So ONE structure (single-valued S¹) gives all three QM pillars: charge quantization + correlations/Born + uncertainty.
- **HONEST BOUNDARY:** the correlation and Born results REPRODUCE QM — do NOT beat it, and a Bell test CANNOT distinguish compact-time TFT from standard QM (the uncertainty theorem, §8, is a clean derivation with no such caveat). Value is conceptual (a deterministic account of the correlation, its ceiling, and now the single-outcome probabilities). The Born derivation is assumption-conditional: it rests on non-contextuality/additivity (the envariance soft spot), assumed not derived. OPEN (the real prize, untouched): a distinguishing observable — CHSH and Born are both degenerate with QM.

## 7e. Foundations and limits — what the field is, and where it breaks (18 July 2026)
Full record: `FOUNDATIONS_AND_LIMITS.md`. Asks what the Teotl field IS, with equal weight on where it fails.
- **Time emerges (`pw_emergent_time.py`):** a timeless constraint (Ĥ_C+Ĥ_S)|Ψ⟩=0 with the S¹ phase as Page–Wootters clock reproduces Schrödinger evolution on conditioning (fidelity 1); emergent time cyclic + comb spectrum → the internal-phase S¹ (winding=charge) and the time-S¹ are ONE structure; "time = phase cycling" = relational time. Floor: reproduces QM → "phase IS time" is an identification, not forced.
- **One circle, one scale (`scale_darkenergy.py`):** one S¹ at H₀ unifies time+charge+a₀+dark energy — a₀=cH₀/2π (87% of obs), thawing **w≥−1 always**, w₀≈−0.88→wₐ≈−0.2, **a₀↔w locked** (phantom crossing falsifies). Floors: absolute scale=input (CC problem unsolved); quantum=DE identity=hypothesis (degenerate).
- **Measurement as loop-closure (`meas3/4_*.py`):** only definite branches close (single outcome, no branching, Born frequencies), einselection reproduced, E>0 = clock arrow. Floors: *which* outcome (seam phase) + thermodynamic arrow (past hypothesis) = boundary conditions, correctly not derived.
- **THE SHARP NEGATIVE — tensor completeness (`tens_completeness.py`):** an economical (classical) S¹ field is ENTANGLEMENT-BOUNDED — reproduces product/GHZ/area-law (WHY CHSH/Born/GHZ passed, all low-entanglement) but NOT volume-law → **FALSIFIED by quantum-supremacy experiments**. Full 2ⁿ QM requires quantizing the field (Fock/exponential) = standard QFT. **The framework cannot be both economical-classical AND full QM.**
- **Super-Planckian tension (`swmp_tension.py`):** dark energy needs f≳1.45 M_Pl (swampland concern, shared with all thawing quintessence); monodromy (wind one circle ~15×) = one-S¹-native evasion → winding floor. R³ uncertainty DECOUPLED: a₀=cH₀/2π is the field's own de Sitter fluctuation (f-independent), protected from the tension.

## 8. REUSABLE TFT TOOLKIT (for building other apps)
The transferable dictionary — identities that hold across every result above:

| TFT object | Is / gives |
|---|---|
| **ψ = ρe^{iθ} : ℝ³ × ℝ → ℂ** (the Teotl field) | the substrate — **one complex field**, whose value has a modulus ρ (amplitude/"carrier") and an argument θ (phase). **Amended 18 Aug 2026:** this row previously led with *θ: ℝ³ × ℝ → S¹ (phase field)* and mentioned the complex form second, leaving the field content ambiguous. It is now settled the other way, because **the corpus computes in the complex field and cannot compute without it**: an audit of eleven results found seven work under either reading, while four require the amplitude outright — Q-balls and localized 3D particles, the lepton-mass/Koide program, the entire GPE/quantum-dynamics arc, and the electric charge j⁰ = ρ²ω. A pure phase cannot supply them: with both terms of E(λ) = λE₂ + λ³E_V positive, any lump collapses (Derrick), and with no amplitude to trade against rotation there are no Q-balls — **a pure-phase theory has domain walls and vortex lines and no particles at all**, which this file already recorded further down ("a pure-phase 3D lump radiates"). **Consequence: the circle is the VACUUM MANIFOLD {\|ψ\| = v}, not the target.** π₁(ℂ) = 0, so the target carries no topology; the circle — and with it winding, charge quantisation, the CHSH closure, the Born rule, number–phase uncertainty and vortices — arises from the potential's minimum set. **Every one of those results survives unchanged; what changes is provenance: compactness is emergent, not primitive.** The earlier argument that S¹ is "the unique compact, smooth, connected 1-manifold" is **withdrawn** — it justified a choice the theory does not make. **Monism is unaffected and is worth stating precisely: the Teotl field is ONE field (ρ and θ are polar coordinates on its value, not two substances), and nothing external acts on it.** What monism does *not* license is **minimality of scales**: the amplitude potential V(ρ) and the phase potential V(θ) are independent functions with independent scales, and no principle in the framework yet relates them. **That independence is what makes the theory viable** — the phase gap is pinned near H₀ (dark energy, a₀) while particle masses are set by V(ρ), and forcing them to share one scale would put the electron ~39 orders from the only available mass. *(Superseding the 17 Aug correction below, which stands on its own point: S¹ is internal, not a dimension of spacetime, and the compact-time reading is withdrawn.)* <br><br> **The 17 Aug 2026 correction, retained:** this row previously read *θ: ℝ³×S¹ → S¹*, which showed **two circles** and implied a compact time dimension. **S¹ is the TARGET space of the phase — internal, in the same sense the U(1) of electromagnetism is internal — not a dimension of spacetime.** An audit of every derived result found that eight of ten use only the target reading (winding/charge, CHSH, Born, number–phase uncertainty, the e^{inθ} ladder, forced periodicity of the potential, kinks and the classical sector), one uses neither, and exactly one — the thermal/KMS argument — used the compact-base reading. That one is withdrawn: compactifying Euclidean time is how every finite-temperature theory is computed and implies nothing about time being a circle, and the corpus had assigned the same circle two periods differing by 2×10⁶¹ (τ₀ ≈ 1.35×10⁻⁴³ s versus 2π/H₀ ≈ 2.88×10¹⁸ s). **Nothing else changes; the framework is a U(1)-valued field on ordinary space and ordinary time.** |
| time | phase cycling: dτ = ℏdθ/E. mass = frequency: ω = mc²/ℏ |
| E₀, ℓ₀ (**not free primitives** — see note) | fix g_eff, m, and (dimensionally) a₀. They do **not** fix c or ℏ: c enters ℓ₀'s own definition (ℓ₀ = cτ₀), and E₀/ℓ₀ = c⁴/G *identically* (the Planck force). Given {ℏ, c, G}, E₀ = √(2π)E_Pl, ℓ₀ = √(2π)ℓ_Pl, τ₀ = √(2π)t_Pl are **determined**, so this row is a re-parameterisation of {ℏ, c, G} rather than an independent starting point. *(Corrected 15 Aug 2026; the row previously read "two primitives … fix c, ℏ, …", which runs backwards.)* |
| winding W ∈ ℤ (π₁(S¹)) | **line-defect (vortex) charge, and the self-linking/twist that carries spin-statistics — NOT electric charge.** ⚠ **Corrected twice, 18 Aug 2026 (BMCA0 → CHRG0 → CHRG1).** This row first equated W with *both* baryon number and electric charge. **Neither survives.** Not baryon number: the electron has B=0 but is spin-½, so its self-linking (= W) is *odd*, and 0 is even. Not electric charge: **electric charge is the monopole moment, and a winding configuration has none** — the Gauss flux of a closed vortex loop is zero at every radius (verified to 4×10⁻¹⁸ relative), while a Noether source gives −4πq. Structurally, **π₂(S¹) = 0**: an S¹-valued field on ℝ³ has *no point-like topological charge to have*. **Electric charge is the U(1) Noether charge j⁰ = ρ²ω (§3 above), which is what every derivation in this repo actually uses.** |
| ∇θ | the EM potential A (Goldstone); B = ∇×∇θ = flux tubes on winding lines, Φ = 2πW |
| j^μ = ρ²∂^μθ (linear, signed) | electromagnetism (Coulomb, like-repels) |
| T^μν (quadratic, ≥0) | gravity (universal, emergent geometry; ∇²Φ = energy density → 1/r) |
| mass gap m = √Λ/ℓ₀ | Yukawa range 1/m. Λ~O(1) → microscopic screening; Λ~10⁻¹²² → ultralight (Hubble-scale) |
| helicity = linking of winding lines | chirality = sign of magnetic helicity. ⚠ *Corrected 18 Aug 2026:* the "= (via anomaly) baryon number — one invariant" clause is **withdrawn** (see §7). |
| two fundamental rates | Planck/UV → G; Hubble/IR → a₀. 2π = one S¹ cycle in both |
| localized 3D particle | needs a conserved charge (Q-ball); a pure-phase 3D lump radiates |

**Design rules that kept us honest (reuse these):** (1) mass/force/gravity must emerge from the field, never inserted; (2) one frozen calibration constant per absolute scale, then everything downstream is prediction; (3) label DERIVED vs DELIVERED-by-construction vs INPUT; (4) route every claim to a runnable check; (5) expect mechanisms & scalings to derive, absolute numbers to be inputs.

## 9. OPEN / floors (each = a named deep problem, not a TFT-specific gap)
- **Newton's G** coefficient = quantum-gravity / emergent-metric step. *(1 Aug 2026: this floor and "absolute E₀, ℓ₀" below are now known to be **one floor, not two** — `verify_units_closure.py` shows that fixing G's O(1) coefficient fixes E₀, ℓ₀ and τ₀ exactly, at √(2π) × the Planck values. Fewer independent unknowns; the wall itself is unmoved.)*
- **|Λ| ~ 10⁻¹²²** = cosmological-constant problem.
- **a₀ exact coefficient** (ω₀/H₀ ~ 1) = coincidence problem (why dark energy is dynamical now).
- **η ≈ 6×10⁻¹⁰** magnitude = baryogenesis initial condition (net primordial helicity).
- **THE SUB-PLANCKIAN MASS FLOOR** *(consolidated and sharpened 18 Aug 2026)* — **one floor, two
  instances, only one of which was recorded.** TFT's condensate sits at **f = M_Planck (non-reduced)
  = √(8π)·M̄_Pl ≈ 1.22×10¹⁹ GeV = 1.22×10²⁸ eV** — the value derived in the a₀ paper from
  f = √(2N)·M_Planck at N = 1/2 — and every particle scale lies far below it:
  - **v_EW = 246 GeV** (equivalently m_h = 125 GeV) — **16.7 orders** below f.
  - **the electron, m_e = 511 keV** — **22.4 orders** below f. **This instance was never recorded**,
    because the mass program derives Koide *ratios* and never had to place an absolute.

  **So the open problem is a single missing mechanism: how a Planckian condensate yields
  sub-Planckian particle masses.** It is a hierarchy problem, and it is the same one for the
  electroweak scale and for the lepton spectrum.

  **Two scales, kept distinct** *(they were previously conflated under "the soliton interior")*:
  - the **phase** potential's scale is fixed — μ⁴ = E₀κ/ℓ₀³ with **E₀ cancelling from the mass
    entirely**, leaving m_φ = √(κ/2N)/ℓ₀, so **κ = 2N·Λ carries all of it — and at the paper's
    N = 1/2 this is κ = Λ = 8.71×10⁻¹²² exactly.** That is the cosmological-constant fine-tuning,
    not a separate unknown.
  - the **amplitude** potential's scale is where the particle masses live, and it is identified with
    f — hence Planckian, hence the 17- and 22.7-order gaps above.

  **Distinct from the r/A floor, which is dimensionless.** r ≈ 0.318 and A ≈ √2 set mass *ratios*
  (Koide); this floor sets mass *absolutes*. **Deriving r would not give the electron mass, and
  fixing the mass scale would not give Koide** — two different unknowns that a shared label had been
  hiding. Same class as the entries above: mechanisms and ratios derived, absolute scales are floors.
- **The Standard-Model gauge sector** — see §10. Not a floor of the usual kind (a number awaiting a
  mechanism) but a structural barrier, and the reopening conditions are stated there.
- Absolute E₀, ℓ₀ (see the G bullet above — tied to G's coefficient, not independent of it); rigorous action-level modified-inertia law; per-galaxy SPARC χ²; BMC G3/G4.

## 10. FAILED — do not repeat
- **Stage 2** (open-time sine-Gordon, mass = oscillating BC): radiation p=−1, not 1/r². Cause: phase had mass √Λ → Yukawa screening (Λ was O(1); the *cosmological* Λ is ultralight — see §6).
- **Stage 6** (compact-time ℝ³×S¹): static profile a₀ pinned at zero (structural).
- **Stage 7** (topological knots on a dissipative substrate): free 2D vortex dissolves; that substrate's stability was externally driven, not topological.

### The SM / 16×16 reconstruction — closed (28 July 2026)
Four routes to the Standard Model's gauge sector were run to their ends. **All four fail, and they
fail for one reason wearing four faces: the single S¹.** Recorded here because each is formally
excluded rather than merely unachieved — these are no-goes, not to-do items.
- **The dial-product picture** — *arithmetically impossible, independently of TFT.* 16 = 2⁴ and
  **3 ∤ 16**, so no product of dial counts containing a 3-state colour dial can ever equal 16
  (exhaustive search over all sub-products of {3,2,2,2}: none = 16; full product 24). **The 16 is a
  SPINOR — the even-parity half of {±}⁵ — not a lattice of dial settings.** An abelian product of Z_n
  dials gives a lattice; a spinor is not a lattice. Corollary: colour must enter as **three binary
  labels** whose permutations lift to SU(3), *not* as one Z₃ dial. (The Z₃ centre labels triality and
  is correct as confinement physics, but a centre element cannot supply a triplet index.)
- **Building the Clifford algebra from independent dials** — *impossible as a theorem.* Operators with
  disjoint tensor support always commute (max |[A_i,B_j]| = 0.00e+00 over 400 random Hermitian pairs),
  while a Clifford algebra requires anticommutation. Naive dial gammas get the 5 same-dial pairs right
  and **all 40 cross-dial pairs wrong** — the same 5/40 split as the Cartan/root division of so(10).
  **Anticommutation requires nonlocal structure**, and TFT's only nonlocality is spatial (vortex
  linking), not internal.
- **The odd-mode Kuramoto engine as a dial generator** — *closed.* Σ_{k odd} sin(kΔθ)/k is a truncated
  square wave with **g > 0 throughout (0,π)**, so no locked relative phase exists besides in-phase;
  g′(0) = +5 (stable), g′(π) = −5 (antipodal unstable). Simulation across four regimes and three seeds
  finds **no multiplet state anywhere**. The lead conflated a *pairwise coupling function* with a
  *potential harmonic* — the Z_n dials come from V = −cos(nβ), not from the coupling.
- **Octonions as a TFT-forced structure** — *excluded by a rank count.* 𝕆 is objectively distinguished
  (the Cayley–Dickson tower terminates there: sedenions have zero divisors, e.g.
  (e₁+e₁₀)(e₄−e₁₅) = 0), and Aut(𝕆) = G₂ with the stabiliser of one imaginary unit being **su(3)**
  (dim 14 → dim 8, rank 2, verified) — a genuine derivation of the *group*. But TFT cannot reach it:
  FKS enhancement on n compact bosons yields rank n, **so(8) = D₄ needs rank 4, and monism supplies
  one circle.** So the octonion route is *borrowed* mathematics — TFT would have to acquire 𝕆, not
  imply it. **"Why 8?" replaces "why 3?"; the question is relocated, not closed.**

**Reopening conditions** (the arc is closed, not forbidden): (1) a nonlocal *internal* ordering;
(2) rank > 1 from a single circle; or (3) a demonstration that TFT *requires* a normed division
algebra of maximal dimension — which would force 𝕆, and hence SU(3). Only (3) is a research
programme rather than a contradiction.

### The weak sector's obstruction is not topological (2 August 2026)

*(Note added 18 Aug 2026, CHRG1/UNC1: the premise quoted here — "charge = integer winding" — has
itself since been **withdrawn**; electric charge is the Noether charge, and its integrality comes
from the number operator's spectrum, not from a winding. **That does not weaken this section — it
strengthens it.** The inference recorded below was already wrong on its own terms; it is now wrong
twice over, since the invariant it invoked was never the charge to begin with.)*

A natural inference from "charge = integer winding" is that TFT *topologically forbids* the
flavour-changing decays the weak interaction performs, since a topological invariant cannot change
under continuous evolution. **That inference is wrong, and it is recorded here because it is the
obvious thing to conclude.** Beta decay is winding-neutral:

```
neutron (0)  ->  proton (+1) + electron (-1) + antineutrino (0)      total winding 0 -> 0
```

No invariant changes. The process is winding/anti-winding **pair nucleation** out of a neutral
configuration — it costs **energy, not topology** — and the amplitude zero it requires exists in
ψ = ρe^{iθ}. (Whether the resulting defect is *stable* is a separate and open matter: Stage 7 in
§10 found a free 2D vortex dissolves.) So there is no topological barrier to the weak sector, and
none should be claimed.

**What winding conservation does buy, and it is not nothing:** the proton is the lightest winding-1
state, so winding conservation forbids proton decay — consistent with the >10³⁴ yr experimental
limit, and obtained for free rather than imposed. The conservation law protects exactly what is
observed to be protected.

**What remains barred is the absolute rate, not the mechanism.** Producing 878.4 s requires an
absolute scale, and E₀/ℓ₀ are the standing floor — shown in §1/§9 to be the *same* floor as
Newton's G coefficient. The weak sector therefore does not add an independent open problem; it
inherits the programme's oldest one.

**A negative worth recording so the route is not re-opened.** Framing decay rates as relaxation
toward equilibrium with the environment does reproduce the observed environmental dependence —
e.g. bound-state beta decay, where ¹⁶³Dy is stable as a neutral atom but decays with t½ ≈ 47 d when
fully ionised, because stripping the electrons opens a final state that Pauli occupancy had
blocked. But such an account **cannot diverge from the standard one**, because entropy is a count of
accessible states and phase space is a count of accessible states: they are the same operation. The
reframing is exact, and therefore empirically empty. There is no measurement that can distinguish
them, and the reason is structural rather than a limit of effort.

## 11. Scorecard
| Piece | Status |
|---|---|
| Stable particle (Q-ball); kink mass + F=Ma; breather | DERIVED |
| Electromagnetism: charge + Coulomb 1/r², like-repels | DERIVED |
| Gravity: universal 1/r attraction (Poisson-sourced T⁰⁰) | DERIVED |
| Matter & antimatter both attract | DERIVED — matches ALPHA-g |
| Toy solar system: Kepler + Mercury 42.90″ | DELIVERED (Kepler by-construction; Mercury generic-1PN) |
| Galaxy rotation curves, no dark matter | DERIVED scale a₀=cH₀/2π + mechanism; MW 2.9%, SPARC-consistent, Tully-Fisher slope 4 |
| Baryo/magneto/chirality linkage (anomaly) | ⚠ **WITHDRAWN 18 Aug 2026** — two independent invariants, not one; anomaly neither automatic nor derived; no genesis mechanism (G3/G4 never run). Topological machinery survives. See §7. |
| G, \|Λ\|, a₀ coefficient, η magnitude | INPUT/OPEN — named deep problems, open everywhere |
| Lepton generations & mass hierarchy | mechanism DEMONSTRATED (interference; electron = near-silent helical state); excitation/symmetry/energetic origins EXCLUDED; ε = 2.27° OPEN |
| Standard-Model gauge sector (SU(2)/SU(3), the 16×16) | **NOT DERIVED — structurally barred.** Four routes closed (§10); the obstruction is the single S¹ and is one problem in four forms, so partial fixes do not help. Reopening conditions stated. |
| Coulomb barrier + tunnelling | Barrier **DERIVED** (unrelaxable phase gradient between like windings; positive-definite energy). Penetration **exponent recovered** — Gamow form organises 24.2 orders of alpha half-life, slope 0.865 vs 1.000, R² = 0.9996, nothing fitted — **prefactor NOT derived** (absolute rate = the E₀/ℓ₀ floor). No observable short-distance modification (core scale 19.7 orders below nuclear contact). §3b |
| Quantisation of light | **NOT reproduced.** The photoelectric effect is passed but never discriminated (classical field + quantised matter suffices). Any classical intensity distribution obeys **g₂(0) ≥ 1** (calculated, min 1.000 over five distributions); measured antibunching and α = 0.18 ± 0.06 sit **13σ** below that bound. Same limit as the tensor-completeness negative, reached independently. |
| Classical limit from dissipation | **FALSE — withdrawn.** Calculated: deterministic amplitude decay leaves normalised coherence **exactly invariant** (deviation 0.0e+00), so it decoheres nothing. Decoherence needs a stochastic or entangling element. The loop-closure account stands alone. |
| Weak sector (flavour-changing decay) | **Obstruction is NOT topological** — beta decay is winding-neutral (0 → +1, −1, 0), i.e. pair nucleation, costing energy not topology (§10). Proton stability IS derived from winding conservation (>10³⁴ yr, free). **The absolute rate is NOT derived** — it needs the E₀/ℓ₀ scale, the same floor as G's coefficient (§1, §9). An entropy/relaxation reframing reproduces environmental dependence but is **provably empirically empty** (entropy counting = phase-space counting). |
| Higgs sector (amplitude mode of the condensate) | Yukawa job RETIRED (chirality is winding parity, so no VEV is needed to permit a mass term); W/Z mass + WW unitarisation NOT ADDRESSABLE (same barrier); **conditional prediction: κ_λ ≥ 5/3**, forced by the same attractive-quartic sign structure that lets solitons exist — HL-LHC-testable. v_EW = INPUT (§9). |

## Evidence (all runnable, in this repo)
Particle/EM/gravity: `verify_conservative_1d.py`, `verify_force_law_sign.py`, `verify_breather_1d.py`, `verify_oscillon_3d.py`, `verify_qball_3d.py`, `verify_goldstone_1r2.py`, `verify_force_sign.py`, `verify_poisson_metric.py`, `verify_gravity_coupling.py`, `verify_G_as_rate.py`, `verify_units_closure.py`, `stage3_orbits.py`, `stage5_mercury.py`, `tft_solar_system.py`.
Rotation curves / a₀: `milkyway_rotation.py`, `verify_a0_g1.py … g5.py` (+ docs `G0_prereg_a0.md`, `G1–G3`).
Baryo/magneto/chirality: `verify_chiral_g1.py`, `verify_chiral_g2.py` (+ docs `G0_prereg_bmc.md`, `G1_chiral_root.md`, `G2_chiral_anomaly.md`).
Generations & mass hierarchy: `koide_selfdual_g1.py … g5.py`, `spectrum_sp1_breathers.py`, `spectrum_sp23_qball_tower.py`, `mass_m1_cancellation.py … m4_chirality.py`, `epsilon_e1_topo.py`, `epsilon_e2_breaking.py`, `epsilon_e4_scale.py` (+ docs `G0_prereg_spectrum.md`, `M0_prereg_mass_interference.md`, `E0_prereg_epsilon.md`, `GENERATIONS_PROGRAM.md`).
Where r lives (soliton interior): `sint_r_interior.py`, `spec_internal_spectrum.py`, `spec_nl3_condensate.py` (+ docs `SINT0_prereg_r.md`, `SPEC0_prereg_spectrum.md`, `SPEC0b_prereg_nl3.md`, `WHERE_R_LIVES.md`).
Particle sector (spin, neutrinos, confinement): `spin_statistics.py`, `neutrino_parity.py`, `quark_confinement.py`, `spec_selfconsistent.py` (+ docs `SPIN0_prereg_statistics.md`, `NU0_prereg_neutrino.md`, `QCD0_prereg_confinement.md`, `THE_PARTICLE_SECTOR.md`).
Black holes + dark-energy falsifier: `bh_study.py`, `bh_bounce.py`, `bh_entropy.py`, `a0_de_study.py` (+ docs `BH0_prereg_blackhole.md`, `BHB0_prereg_bounce.md`, `BHE0_prereg_entropy.md`, `ADE0_prereg_a0_darkenergy.md`, `BLACK_HOLES.md`).
Quantum from compact time: `chsh_compact_time.py`, `chsh_closure.py`, `born1_envariance.py`, `born2_measure.py`, `born3_finegrain.py`, `born4_malus.py`, `born5_closure_knit.py`, `dis1_distinguish.py`, `dis2_ghz.py`, `uncertainty_s1.py` (+ docs `CHSH0_prereg_compact.md`, `BORN0_prereg.md`, `DIS0_prereg.md`, `UNC0_prereg.md`, `QUANTUM_FROM_COMPACT_TIME.md`); builds on `teotl qc.py`, `teotl chsh.py`.
Foundations and limits: `pw_emergent_time.py`, `scale_darkenergy.py`, `meas3_selection.py`, `meas4_classical_arrow.py`, `tens_completeness.py`, `swmp_tension.py` (+ preregs `PW0/SCALE0/MEAS3/MEAS4/TENS0/SWMP0_prereg.md`, doc `FOUNDATIONS_AND_LIMITS.md`).
- **Distinguishing observable — searched, none feasible (§7 of the companion):** compact-time TFT is **empirically degenerate** with QM. Bell is exactly degenerate at any loop size (hidden time-phase cancels); the temporal energy-comb Eₙ=2πn/T differs but scales 1/T (unobservable at T~1/H₀; microscopic T excluded by continuous spectra); GHZ/Mermin reaches **M=4=QM** (full contextuality reproduced). The QC arc's "no distinguishing test" is now a quantified result, not a caveat. One open edge: whether the single-field S¹ construction realizes the full 2ⁿ tensor Hilbert space — if it saturates at 2-body it gives M~0 and is falsified by GHZ.

---

**One-paragraph version:** In the conservative/complex-field regime, TFT gives, from one phase field ψ=ρe^{iθ} on ℝ³×S¹: a stable particle (Q-ball); electromagnetism (Coulomb, like-repels, from the signed winding current); gravity as emergent geometry (universal 1/r, from the positive energy current — matter and antimatter both fall); a working toy solar system (Kepler + Mercury 43″, one frozen constant); galaxy rotation curves without dark matter (the MOND scale a₀=cH₀/2π *derived* not fitted, via the field being ultralight dark energy — "α from Λ" — with a modified-inertia mechanism giving the Tully-Fisher law); and the baryogenesis/magnetogenesis/chirality trio as one topological invariant (winding-line helicity) so their anomaly is automatic. The recurring pattern: **mechanisms and scale-relations derive parameter-free; the absolute numbers (G, |Λ|, a₀'s coefficient, η) are inputs that reduce to the field-wide deep problems.** Everything is runnable; nothing is overclaimed.
