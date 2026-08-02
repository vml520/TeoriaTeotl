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
- **The SI second is derived, not imported** (`verify_units_closure.py`, 1 Aug 2026). ℏ = E₀τ₀/2π together with ℓ₀ = cτ₀ fix the second from the two primitives, so no result here can carry a hidden unit convention — a units error would surface as a *dimensional mismatch*, not as a tension. Every gate runs in code units (ℓ₀ = c = E₀ = 1); the only carriers of 's' in the repo are c, ℏ, H₀.
  - *Consequence — **INFERENCE**, see §4 and §9:* feeding in G = ℓ₀c⁴/E₀ closes the system — G = 2πℏc⁵/E₀², hence **E₀ = √(2π)·E_Pl, ℓ₀ = √(2π)·ℓ_Pl, τ₀ = √(2π)·t_Pl** (all three ratios 2.506628, exact as algebra, independent of the CODATA values). The 2π is the **circumference of the compact time-circle** — the same 2π as in a₀ = cH₀/2π and in ℏ = E₀τ₀/2π: the primitives are the Planck units dressed by one trip around S¹. **Conditional on G's O(1) coefficient being 1, which is the open quantum-gravity step — this does not derive G.**

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
  - *Sharpened 1 Aug 2026 (`verify_units_closure.py`, INFERENCE):* with ω₀ ≡ 1/τ₀ and ρ₀ ≡ E₀/(c²ℓ₀³), **G = ω₀²/ρ₀ holds exactly in TFT's own primitives** — the "rate of time" is literally the **inverse compact-time period**, not a borrowed Planck frequency, so the reframing is native rather than a Planck-unit coincidence. Same condition as §1: it assumes G = ℓ₀c⁴/E₀ with coefficient 1, and **the coefficient stays OPEN** (§9).

## 5. DELIVERED — the toy solar system (`tft_solar_system.py`)
Planets as **geodesics** of the Sun's emergent metric. **One** frozen constant K = G·M_sun = 4π² (1 AU→1 yr); G not derived (allowed). Output: 8 periods ≤0.06%, Kepler III T²/a³=1.0000, **Mercury 42.90″/cy** (obs 42.98). *Caveats: Kepler is by-construction (any 1/r); Mercury 43″ is the generic 1PN result, not unique to TFT.*

## 6. DERIVED — galaxy rotation curves without dark matter (a₀ program G0–G5)
- **The derived-Newtonian sector FAILS** the Milky Way (32% off, baryons only) — same dark-matter problem as Newton. The fix is not in that sector.
- **a₀ = cH₀/2π = 1.08×10⁻¹⁰ m/s² is DERIVED, not fitted** (MOND *fits* a₀): the phase field is **ultralight** (mass gap m = √Λ/ℓ₀ = the Hubble mass ⇒ Compton wavelength = Hubble radius ⇒ Λ ~ 10⁻¹²²). Its Compton frequency = H₀/2π (2π = h/ℏ = one S¹ cycle) → a₀ = c·f = cH₀/2π. **This is Vic's "α from Λ."** Effectively massless below the cosmic scale (→ §4 gravity), biting only at a₀. **Tested per-galaxy against SPARC** (`verify_a0_sparc_fit.py`, 2696 pts / 147 galaxies): our own log-space RAR fit gives g† = 1.16×10⁻¹⁰ (deep-MOND 1.33×10⁻¹⁰); the derived a₀ = 1.04–1.13×10⁻¹⁰ sits at **0.90–0.97 × g†**, scatter 0.133 dex (lit ~0.12) reproduced, scale universal where constrained → **consistent within ~20% systematics** (M/L, distances), nothing fitted to SPARC.
- **Self-consistency (G2):** if that field *is* the dark energy (Friedmann), Λ cancels → a₀ ∝ cH₀ without solving the CC problem.
- **Mechanism = modified inertia** ("inertia saturates"): inertia is cut off by the smaller of the acceleration horizon c²/a and the cosmic horizon c/H₀ → below a₀, μ → a/a₀ → **deep-MOND a = √(a_N a₀)** → flat curves + **baryonic Tully-Fisher V⁴ = GMa₀, slope exactly 4** (SPARC: 3.85±0.09).
- **Fits:** Milky Way 2.9% (baryons only, derived a₀); **consistent with the SPARC RAR** within its 0.13-dex scatter.
- **Caveats/OPEN:** exact a₀ coefficient = ω₀/H₀, a natural quintessence O(1) → the **coincidence problem**; the interpolation *shape* is model-dependent (as in MOND); a rigorous action-level derivation and a per-galaxy χ² (needs raw SPARC data) are open.

## 6b. Black holes + the dark-energy falsifier (13 July 2026)
Full record: `BLACK_HOLES.md`. **Reading two derived facts — √(2GM/r) = the inflow rate of space, and time = phase cycling — gives a complete black hole.**
- **Horizon [derived route]:** the inflow rate reaches c at r_s (river/Gullstrand-Painlevé, from TFT's OWN rate); **time freezes at the horizon** (rate ∝ √g₀₀ → 0 = literal frozen star). r_s and thermo scales = consistency w/ GR.
- **NO SINGULARITY [TFT-native]:** the bounded phase field (|∇θ|≲1/ℓ₀, finite amplitude) caps the density at ~Planck density → a **regular Planck-density core** (r_core ~ 4.5e-23 m solar, regular-BH/Planck-star family) — distinctive vs GR's point singularity.
- **The core BOUNCES [computed]:** a squeezed Q-ball breathes/oscillates (φ⁶ high-density repulsion = field degeneracy pressure) — same boundedness that resolves the singularity; time-dilated → Planck-star delayed burst (PBH ~6e22 kg bounces now, mass model-dependent).
- **Entropy [computed area law + floor]:** S ∝ **area** (S~R^1.9, computed as the phase Goldstone's entanglement entropy, Srednicki — WHY BH entropy is holographic); the **¼** = the induced-gravity coefficient (S_ent=A/4G, ε cancels because one field gives S_ent AND G) — inherited/constrained, exact value a floor (cf. Immirzi). Magnitude ~1e77 solar, S∝M² reproduced.
- **Dark energy CANNOT go phantom [derived, falsifiable]:** DE = the same phase field (pNGB thawing quintessence, ordinary scalar) → **w ≥ −1 always** (integration: w_min=−1.0000); matched to w₀=−0.88 → wₐ≈−0.24, mass ~H₀ (a₀-consistent, one field both). DESI's CPL prefers phantom crossing (w<−1 past) → **sharp falsifier. STATUS (DR2, 2025): in tension.** The evolving-DE preference firmed 2.6σ (DR1, DESI+CMB) → 3.1σ (DR2), 2.8–4.2σ +SNe; DR2 best fit w₀=−0.838±0.055, wₐ=−0.62 crosses w=−1 in the past and DESI reports non-phantom models **disfavoured**. TFT agrees DE evolves (both reject ΛCDM); they part on wₐ's magnitude. The prediction w≥−1 stands and the current data do not meet it — if the crossing hardens (DR3/Euclid), TFT's DE sector is excluded.

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

## 7d. Quantum correlations from compact time (13 July 2026; Born rule 14 July 2026)
Full record (with prominent caveats): `QUANTUM_FROM_COMPACT_TIME.md`. **The local field saturates CHSH at S=2.0000 (classical); compact time DERIVES the quantum value AND the Born rule.**
- **The correlation:** TFT's S¹ is a SINGLE-VALUED COMPLEX PHASE. Single-valuedness fixes the loop phase difference; the hidden variable CANCELS → E(a,b)=cos(a−b) (quantum form, NO tuning, no-signaling). A coherent phase = Hilbert space → **Tsirelson caps CHSH at 2√2 automatically** (numerically 2.828; the naive arbitrary-reweight overshoot of 2.90 is FORBIDDEN once the phase is genuine). Quantum coherence = the phase closing single-valuedly on the S¹ time circle → makes precise "quantum uncertainty = ordinary deterministic S¹ behaviour."
- **The Born rule (`born1..5_*.py`, pre-reg `BORN0_prereg.md`):** single-outcome |ψ|² DERIVED from the same closure. Equal amplitudes → equal weights by an EXACT envariance symmetry (pure-environment counter-swap unitary iff |c₀|=|c₁|), no |c|² inserted; **|c_k|² for all amplitudes from that symmetry alone**, exponent 2 = coherent-superposition normalization (equal branches carry 1/√n ⇒ count=1/amp²), not a charge postulate; continuous **Malus P(+|θ)=cos²(θ/2)** uniquely pinned by E=cos θ (other exponents break it); ONE rule |⟨·|Ψ⟩|² gives marginals+no-signaling+E=cos(a−b)+Tsirelson+Malus. Born reduced to the S¹ swap symmetry + additivity.
- **The uncertainty principle (`uncertainty_s1.py`) — the THIRD pillar, DERIVED, no degeneracy caveat:** the single-valued S¹ phase makes the winding N=−i∂_θ integer (charge quantization) with exact [N,cosθ]=i sinθ → the Carruthers–Nieto number–phase uncertainty **ΔN·Δθ ≥ ½**, verified for all states, saturated by von Mises (minimum-uncertainty) states, → Heisenberg ½ in the localized limit (0.500). Physical tradeoff: definite charge/winding ⇒ uniform/undefined phase. So ONE structure (single-valued S¹) gives all three QM pillars: charge quantization + correlations/Born + uncertainty.
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
- **Newton's G** coefficient = quantum-gravity / emergent-metric step. *(1 Aug 2026: this floor and "absolute E₀, ℓ₀" below are now known to be **one floor, not two** — `verify_units_closure.py` shows that fixing G's O(1) coefficient fixes E₀, ℓ₀ and τ₀ exactly, at √(2π) × the Planck values. Fewer independent unknowns; the wall itself is unmoved.)*
- **|Λ| ~ 10⁻¹²²** = cosmological-constant problem.
- **a₀ exact coefficient** (ω₀/H₀ ~ 1) = coincidence problem (why dark energy is dynamical now).
- **η ≈ 6×10⁻¹⁰** magnitude = baryogenesis initial condition (net primordial helicity).
- **v_EW = 246 GeV** (equivalently m_h = 125 GeV) = INPUT. TFT's identified condensate sits at
  f = 2.09 M_Pl — 16.3 orders away — so the electroweak scale is not derived. Same class as the
  entries above: mechanisms and ratios derived, absolute scales are floors.
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
| Baryo/magneto/chirality linkage (anomaly) | DERIVED (one topological invariant); net η = INPUT |
| G, \|Λ\|, a₀ coefficient, η magnitude | INPUT/OPEN — named deep problems, open everywhere |
| Lepton generations & mass hierarchy | mechanism DEMONSTRATED (interference; electron = near-silent helical state); excitation/symmetry/energetic origins EXCLUDED; ε = 2.27° OPEN |
| Standard-Model gauge sector (SU(2)/SU(3), the 16×16) | **NOT DERIVED — structurally barred.** Four routes closed (§10); the obstruction is the single S¹ and is one problem in four forms, so partial fixes do not help. Reopening conditions stated. |
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
