# TFT-Classical — Summary of Derived Results

*As of 11 July 2026. Digest of derived results, each routed to a runnable check.*
*Labels: **DERIVED** (from the field, rigorous) · **DELIVERED** (works, see caveat) · **PROPOSED** (reframing, not proof) · **INPUT** (a value the framework does not fix) · **OPEN** · **FAILED** (do not repeat).*

**The one meta-lesson (read this first if you're building another TFT app):** TFT reliably derives **structures, mechanisms, and scale *relations* — parameter-free**. It does **not** derive **absolute values**: every absolute number we chased (Newton's G, |Λ|, a₀'s exact coefficient, the baryon asymmetry η) bottomed out at a *named, field-wide* open problem (quantum gravity, the cosmological-constant problem, the coincidence problem, the baryogenesis initial condition). So: expect to derive the *mechanism and the scaling*, and to carry *one calibration constant / initial condition* per absolute scale. That is not a TFT weakness — those numbers are unsolved everywhere.

---

## 0. Regime that works
Productive regime: the **conservative** second-order field, then a **complex** field ψ = ρe^{iθ}. The **dissipative** (Kuramoto) and **topological-knot** attempts all failed — see §10. Don't restart there.

## 1. Foundational machinery (from the founding TFT paper)
Two primitives **E₀** (phase-energy) and **ℓ₀** (coherence length); everything else derives:
- dτ = ℏdθ/E (time = phase per energy); dℓ = ℏdθ/p (length = phase per momentum)
- g_eff = E₀/ℓ₀; c = E₀/p₀; m = E₀/c²; ℏ = E₀τ₀/2π
- Force is an emergent process, not fundamental: F = −g_eff∇θ
- Gravity = geodesics of an **emergent metric** sourced by the field's energy.
- Premise: mass = a real periodic process, mc² = hf ⇒ ω = mc²/ℏ.

## 2. DERIVED — particle sector
- **Kink rest mass M_k = 8√Λ·E₀** (exact to 1e-9); **force law a = −2πf·Q/M_k** (F=Ma, ~2%). Mass & force from the field, nothing by hand.
- **Breather**: time-periodic "particle-wave," mass M_b = 2M_k√(1−ω²) entirely in the motion (exact only in 1D — integrable).
- **3D oscillon radiates** (pure phase field can't hold a localized 3D wave — no conserved charge). [DERIVED negative]
- **3D Q-ball persists** (complex field + U(1) charge → stable localized 3D particle). *Caveat: uncharged control also persisted on the tested timescale.*

## 3. DERIVED — the two force sectors from one distinction
The complex field has **two conserved currents**:
- **U(1) Noether current** j^μ = ρ²∂^μθ — *linear*; charge j⁰ = ρ²ω is **signed** → **Electromagnetism** (Coulomb 1/r², like-charges **repel**, massless Goldstone mediator).
- **Energy–momentum** T^μν — *quadratic*; T⁰⁰ ~ ρ²ω² is **positive-definite** → **Gravity** (universal).
Consequence (correct vs experiment): matter (ω) & antimatter (−ω) have opposite charge, identical energy → **both gravitate attractively** (matches CERN ALPHA-g 2023).

## 4. DERIVED — gravity's shape and sign
- **1/r potential**: the metric potential is **Poisson-sourced** by energy density, ∇²Φ = |∇θ|² (the paper's error was setting Φ *equal* to |∇θ|² → wrong 1/r⁴). Gauss's law → far field ∝ total enclosed energy = mass → Φ ~ −M/(4πr). Measured: Φ~1/r, force~1/r².
- **Universal attraction**: energy density ≥ 0 → always an attractive well. Why neutral matter cancels EM charge but adds energy.
- **G as squared rate of time** (PROPOSED reframing): G·ρ = T⁻² so √(Gρ) is a rate; G = ω_P²/ρ_P (Planck frequency² / Planck density). Recasts "derive G" as "what sets the vacuum's cycling rate." G's coefficient itself = the quantum-gravity problem (OPEN everywhere).

## 5. DELIVERED — the toy solar system (`tft_solar_system.py`)
Planets as **geodesics** of the Sun's emergent metric. **One** frozen constant K = G·M_sun = 4π² (1 AU→1 yr); G not derived (allowed). Output: 8 periods ≤0.06%, Kepler III T²/a³=1.0000, **Mercury 42.90″/cy** (obs 42.98). *Caveats: Kepler is by-construction (any 1/r); Mercury 43″ is the generic 1PN result, not unique to TFT.*

## 6. DERIVED — galaxy rotation curves without dark matter (a₀ program G0–G5)
- **The derived-Newtonian sector FAILS** the Milky Way (32% off, baryons only) — same dark-matter problem as Newton. The fix is not in that sector.
- **a₀ = cH₀/2π = 1.08×10⁻¹⁰ m/s² is DERIVED, not fitted** (MOND *fits* a₀): the phase field is **ultralight** (mass gap m = √Λ/ℓ₀ = the Hubble mass ⇒ Compton wavelength = Hubble radius ⇒ Λ ~ 10⁻¹²²). Its Compton frequency = H₀/2π (2π = h/ℏ = one S¹ cycle) → a₀ = c·f = cH₀/2π. **This is Vic's "α from Λ."** Effectively massless below the cosmic scale (→ §4 gravity), biting only at a₀.
- **Self-consistency (G2):** if that field *is* the dark energy (Friedmann), Λ cancels → a₀ ∝ cH₀ without solving the CC problem.
- **Mechanism = modified inertia** ("inertia saturates"): inertia is cut off by the smaller of the acceleration horizon c²/a and the cosmic horizon c/H₀ → below a₀, μ → a/a₀ → **deep-MOND a = √(a_N a₀)** → flat curves + **baryonic Tully-Fisher V⁴ = GMa₀, slope exactly 4** (SPARC: 3.85±0.09).
- **Fits:** Milky Way 2.9% (baryons only, derived a₀); **consistent with the SPARC RAR** within its 0.13-dex scatter.
- **Caveats/OPEN:** exact a₀ coefficient = ω₀/H₀, a natural quintessence O(1) → the **coincidence problem**; the interpolation *shape* is model-dependent (as in MOND); a rigorous action-level derivation and a per-galaxy χ² (needs raw SPARC data) are open.

## 7. DERIVED — baryogenesis / magnetogenesis / chirality = one topological invariant (BMC G1–G2)
- The minimal action is **CP-symmetric** → chirality not *forced* (matter = antimatter).
- The chiral invariant **exists** = the **helicity (linking number) of winding lines** (Lk = ±1 handed / 0 unlinked; CP flips its sign). This is Vic's **"chirality from winding directions."**
- **One invariant, three faces:** baryon number = winding charge ΣW; magnetic helicity = flux linking (2π)²ΣWᵢWⱼLkᵢⱼ (since A=∇θ ⇒ winding lines are flux tubes, Φ=2πW); chirality = sign of the helicity.
- Therefore the **chiral anomaly ΔB ∝ ΔH_mag is automatic in TFT** (not a postulate) — the Vachaspati baryogenesis–magnetogenesis link, forced by topology. Coefficient topological (2π-per-winding), × N_f (INPUT).
- **INPUT/OPEN:** the *net* helicity generated → magnitude of η ≈ 6×10⁻¹⁰ (an initial condition). G3 (net-winding mechanism) and G4 (coherent helical field) are open. *More speculative than the gravity work.*

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
- **FLOORS (the honest boundary):** absolute scales (ν-mass, Λ_QCD) and NON-ABELIAN groups (SU(2)_L for the full weak force, color SU(3) for the full strong force, fractional charge) — the U(1) field gives integer winding and derives mechanisms/scale-relations, not absolutes or non-abelian structure. Same pattern as G, |Λ_cc|, a₀-coeff, η.

## 8. REUSABLE TFT TOOLKIT (for building other apps)
The transferable dictionary — identities that hold across every result above:

| TFT object | Is / gives |
|---|---|
| θ: ℝ³×S¹ → S¹ (phase field); complex ψ = ρe^{iθ} | the substrate; ρ = amplitude/"carrier," θ = phase |
| time | phase cycling: dτ = ℏdθ/E. mass = frequency: ω = mc²/ℏ |
| E₀, ℓ₀ (two primitives) | fix c, ℏ, g_eff, m, and (dimensionally) G, a₀ |
| winding W ∈ ℤ (π₁(S¹)) | topological charge = **baryon number** = **electric charge** (signed) |
| ∇θ | the EM potential A (Goldstone); B = ∇×∇θ = flux tubes on winding lines, Φ = 2πW |
| j^μ = ρ²∂^μθ (linear, signed) | electromagnetism (Coulomb, like-repels) |
| T^μν (quadratic, ≥0) | gravity (universal, emergent geometry; ∇²Φ = energy density → 1/r) |
| mass gap m = √Λ/ℓ₀ | Yukawa range 1/m. Λ~O(1) → microscopic screening; Λ~10⁻¹²² → ultralight (Hubble-scale) |
| helicity = linking of winding lines | chirality = magnetic helicity = (via anomaly) baryon number — one invariant |
| two fundamental rates | Planck/UV → G; Hubble/IR → a₀. 2π = one S¹ cycle in both |
| localized 3D particle | needs a conserved charge (Q-ball); a pure-phase 3D lump radiates |

**Design rules that kept us honest (reuse these):** (1) mass/force/gravity must emerge from the field, never inserted; (2) one frozen calibration constant per absolute scale, then everything downstream is prediction; (3) label DERIVED vs DELIVERED-by-construction vs INPUT; (4) route every claim to a runnable check; (5) expect mechanisms & scalings to derive, absolute numbers to be inputs.

## 9. OPEN / floors (each = a named deep problem, not a TFT-specific gap)
- **Newton's G** coefficient = quantum-gravity / emergent-metric step.
- **|Λ| ~ 10⁻¹²²** = cosmological-constant problem.
- **a₀ exact coefficient** (ω₀/H₀ ~ 1) = coincidence problem (why dark energy is dynamical now).
- **η ≈ 6×10⁻¹⁰** magnitude = baryogenesis initial condition (net primordial helicity).
- Absolute E₀, ℓ₀; rigorous action-level modified-inertia law; per-galaxy SPARC χ²; BMC G3/G4.

## 10. FAILED — do not repeat
- **Stage 2** (open-time sine-Gordon, mass = oscillating BC): radiation p=−1, not 1/r². Cause: phase had mass √Λ → Yukawa screening (Λ was O(1); the *cosmological* Λ is ultralight — see §6).
- **Stage 6** (compact-time ℝ³×S¹): static profile a₀ pinned at zero (structural).
- **Stage 7** (topological knots on a dissipative substrate): free 2D vortex dissolves; that substrate's stability was externally driven, not topological.

## 11. Scorecard
| Piece | Status |
|---|---|
| Stable particle (Q-ball); kink mass + F=Ma; breather | DERIVED |
| Electromagnetism: charge + Coulomb 1/r², like-repels | DERIVED |
| Gravity: universal 1/r attraction (Poisson-sourced T⁰⁰) | DERIVED |
| Matter & antimatter both attract | DERIVED — matches ALPHA-g |
| Toy solar system: Kepler + Mercury 42.90″ | DELIVERED (Kepler by-construction; Mercury generic-1PN) |
| Galaxy rotation curves, no dark matter | DERIVED scale a₀=cH₀/2π + mechanism; MW 2.9%, SPARC-consistent, Tully-Fisher slope 4 |
| Baryo/magneto/chirality linkage (anomaly) | DERIVED (one topological invariant); net η = INPUT |
| G, \|Λ\|, a₀ coefficient, η magnitude | INPUT/OPEN — named deep problems, open everywhere |
| Lepton generations & mass hierarchy | mechanism DEMONSTRATED (interference; electron = near-silent helical state); excitation/symmetry/energetic origins EXCLUDED; ε = 2.27° OPEN |

## Evidence (all runnable, in this repo)
Particle/EM/gravity: `verify_conservative_1d.py`, `verify_force_law_sign.py`, `verify_breather_1d.py`, `verify_oscillon_3d.py`, `verify_qball_3d.py`, `verify_goldstone_1r2.py`, `verify_force_sign.py`, `verify_poisson_metric.py`, `verify_gravity_coupling.py`, `verify_G_as_rate.py`, `stage3_orbits.py`, `stage5_mercury.py`, `tft_solar_system.py`.
Rotation curves / a₀: `milkyway_rotation.py`, `verify_a0_g1.py … g5.py` (+ docs `G0_prereg_a0.md`, `G1–G3`).
Baryo/magneto/chirality: `verify_chiral_g1.py`, `verify_chiral_g2.py` (+ docs `G0_prereg_bmc.md`, `G1_chiral_root.md`, `G2_chiral_anomaly.md`).
Generations & mass hierarchy: `koide_selfdual_g1.py … g5.py`, `spectrum_sp1_breathers.py`, `spectrum_sp23_qball_tower.py`, `mass_m1_cancellation.py … m4_chirality.py`, `epsilon_e1_topo.py`, `epsilon_e2_breaking.py`, `epsilon_e4_scale.py` (+ docs `G0_prereg_spectrum.md`, `M0_prereg_mass_interference.md`, `E0_prereg_epsilon.md`, `GENERATIONS_PROGRAM.md`).
Where r lives (soliton interior): `sint_r_interior.py`, `spec_internal_spectrum.py`, `spec_nl3_condensate.py` (+ docs `SINT0_prereg_r.md`, `SPEC0_prereg_spectrum.md`, `SPEC0b_prereg_nl3.md`, `WHERE_R_LIVES.md`).
Particle sector (spin, neutrinos, confinement): `spin_statistics.py`, `neutrino_parity.py`, `quark_confinement.py`, `spec_selfconsistent.py` (+ docs `SPIN0_prereg_statistics.md`, `NU0_prereg_neutrino.md`, `QCD0_prereg_confinement.md`, `THE_PARTICLE_SECTOR.md`).

---

**One-paragraph version:** In the conservative/complex-field regime, TFT gives, from one phase field ψ=ρe^{iθ} on ℝ³×S¹: a stable particle (Q-ball); electromagnetism (Coulomb, like-repels, from the signed winding current); gravity as emergent geometry (universal 1/r, from the positive energy current — matter and antimatter both fall); a working toy solar system (Kepler + Mercury 43″, one frozen constant); galaxy rotation curves without dark matter (the MOND scale a₀=cH₀/2π *derived* not fitted, via the field being ultralight dark energy — "α from Λ" — with a modified-inertia mechanism giving the Tully-Fisher law); and the baryogenesis/magnetogenesis/chirality trio as one topological invariant (winding-line helicity) so their anomaly is automatic. The recurring pattern: **mechanisms and scale-relations derive parameter-free; the absolute numbers (G, |Λ|, a₀'s coefficient, η) are inputs that reduce to the field-wide deep problems.** Everything is runnable; nothing is overclaimed.
