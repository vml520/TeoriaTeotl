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
> - **The amplitude ρ is an ordinary radial mode, with no protecting symmetry *generically*.**
>   Corrections go as the cutoff, δm² ~ Λ_cut²/16π², dragging it toward **f/(4π) ≈ 9.7×10²⁶ eV**.
>
>   > **Narrowed 19 Aug 2026.** This first read *"with no protecting symmetry"* flatly, and quoted a
>   > tuning of ~3×10⁻⁴³ for the electron. **Two qualifications, both of which weaken it:**
>   > **(i) The lepton sector DOES have a protecting symmetry, derived in this repo.** Winding
>   > reversal θ → −θ is an *exact* symmetry of the minimal action (`G1_chiral_root.md`; reproduced
>   > independently), the mass-making channel is its **even** projection, and the pure winding-**odd**
>   > state is **massless** — it is the neutrino. So m = 0 is symmetry-enforced and every lepton mass
>   > is the *breaking* of it, exactly as a chiral fermion mass is. **A symmetry-protected small mass
>   > is not fine-tuned**, so the tuning framing does not apply to the electron.
>   > **(ii) The tuning figure assumed Λ_cut = f**, and **f is a decay constant, not an established
>   > cutoff** — the corpus fixes no cutoff anywhere. The tuning is real in kind; its size is not
>   > established.
>   >
>   > **What does NOT change:** the *map* below. Every derived claim still sits in the protected
>   > sector and every floor in the unprotected one — and the open problem is now sharper, not
>   > softer. **The symmetry explains why a light lepton EXISTS; it does not set the scale.**
>   > Back-solving m = (even fraction)ⁿ × M₀ fails: no n makes the electron and the tau agree
>   > (n = 1 off by 0.7 orders, n = 2 by 2.1, n = 3 by 4.9). **So the open question is "what sets the
>   > lepton sector's scale?" — one number, alongside v_EW and Λ_QCD — rather than a 22-order
>   > tuning.**
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

> **This file is the DETAIL.** For the one-page picture — what is claimed, what is open,
> what was withdrawn — see [`STATUS.md`](STATUS.md). Sections below are numbered in the order
> results were *derived*, not the order they are best *read*; STATUS.md gives the reading order.

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
  - *Consequence — **INFERENCE**, see §4 and §9:* feeding in G = ℓ₀c⁴/E₀ closes the system — G = 2πℏc⁵/E₀², hence **E₀ = √(2π)·E_Pl, ℓ₀ = √(2π)·ℓ_Pl, τ₀ = √(2π)·t_Pl** (all three ratios 2.506628, exact as algebra, independent of the CODATA values). The 2π is the **circumference of the compact time-circle** — the same 2π as in a₀ = cH₀/2π and in ℏ = E₀τ₀/2π: the primitives are the Planck units dressed by one trip around S¹. **⚠ Note (4 Sep 2026): the a₀ half of this pattern no longer supports the argument — TWOPI1 found the framework does not supply that 2π (`A0_STATUS.md`); the ℏ = E₀τ₀/2π half is unaffected.** **Conditional on G's O(1) coefficient being 1, which is the open quantum-gravity step — this does not derive G.**

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

  > **⚠ SCOPE CORRECTED 21 Aug 2026 (PPN0). The caveat above says Mercury's 43″ is "not unique to
  > TFT". The accurate statement is stronger: it is not REACHABLE from what this framework derives.**
  > The PPN perihelion factor is **(2 + 2γ − β)/3**, which equals 1 only when the **spatial** metric
  > is present. This framework derives only the weak-field **00** equation, i.e. **γ = 0**, giving
  > **14.33″/century — one third of the observed 42.98.** The 42.90″ above came from integrating a
  > **full Schwarzschild metric**, whose spatial part is not produced here.
  >
  > **The four classic tests, scoped honestly:**
  >
  > | effect | needs | this framework, as derived |
  > |---|---|---|
  > | gravitational time dilation | g₀₀ | **✓ works** — solar redshift 2.1×10⁻⁶ |
  > | spatial contraction | g_rr | absent |
  > | light deflection | g₀₀ + g_rr | **half** — 0.88″ vs 1.75″ (Einstein's own 1911 value) |
  > | frame dragging | g₀ᵢ | **zero** — vs Gravity Probe B's 37.2 ± 7.2 mas/yr |
  >
  > **Three of these are GAPS, not failures: lensing, contraction and dragging are never claimed
  > here.** Mercury *is* claimed, and that is what this note corrects.
  >
  > **The structural reason, and it is one gap not four:** ∇²Φ = 4πc²|∇θ|² is a **scalar** equation
  > yielding **one** function, where even the simplest static geometry needs **two** (g₀₀ and g_rr).
  > **A scalar cannot be a geometry** — so this framework distorts *time* without distorting *space*.
  > In GR the two are locked (g₀₀·g_rr = −1 exactly, at every radius) **by the field equation**, which
  > is precisely what is absent here.
  >
  > **What still stands, and is unaffected:** the **1/r shape** and the **universal sign** (T⁰⁰ is
  > positive-definite, so matter and antimatter both attract) are derived, and gravitational time
  > dilation works. **What is imported is the metric's spatial part and G's value.**
  >
  > **A route exists and is short.** Writing the same geometry as a *flow* — the
  > Gullstrand–Painlevé/river form this repo already uses for black holes (`BH0_prereg_blackhole.md`:
  > *"√(2GM/r) = the inflow/contraction rate of space… River / Gullstrand–Painlevé model, from TFT's
  > own inflow rate"*) — supplies the missing spatial part, and **an equal-and-opposite contraction is
  > exactly γ = 1, giving 1.751″ against the observed 1.750″.** Giving the flow an angular component
  > supplies g₀ᵢ and hence dragging. ⚠ **But that form IS Schwarzschild** (verified: identical g₀₀ from
  > r/r_s = 2 to 1000), so it would fix these tests **by being GR** — a reformulation, not a rival —
  > **and √(2GM/r) still imports GM**, exactly as the frozen K = GM above does. **Shape derived, scale
  > imported.**

  > ---
  >
  > ### ✅ SUPERSEDED 4 September 2026 — the spatial and vector sectors are now reachable
  >
  > **The note above is correct as of 21 August and is retained in full. Its central negative claims
  > — Mercury "not reachable", dragging "zero", "a scalar cannot be a geometry" — no longer hold.**
  >
  > **What changed.** Studies GIJ0 and GOI0 supplied the two missing metric sectors. Writing
  > g₀₀ = −f², g_ij = h²δ_ij, one condition — **f·h = 1**, i.e. *the fundamental cell (τ₀, ℓ₀)
  > occupies a position-independent coordinate extent per axis* — fixes the whole spatial sector and
  > gives **γ = 0.999999988** (Cassini: 0.91 σ, against 4.35×10⁴ σ at γ = 0). The **vector** sector
  > then costs nothing: TFT's action is Lorentz invariant (LOR0), so boosting the static solution
  > gives h̄₀ᵢ = (v/c)h̄₀₀ by tensor transformation alone, **|ratio to GR| = 1.000001**.
  >
  > | effect | 21 Aug (γ = 0) | now | observed |
  > |---|---|---|---|
  > | time dilation | ✓ | ✓ | ✓ |
  > | light deflection | 0.8756″ | **1.7512″** | 1.7512″ |
  > | Mercury perihelion | 14.33″/cy | **42.98″/cy** | 42.98″/cy |
  > | Shapiro delay | 0.50 × GR | **1.0000** | 1.0 |
  > | frame dragging | 0.00 | **39.20 mas/yr** | 37.2 ± 7.2 |
  >
  > **⚠ Credit where the record already had it, and this matters for how much GIJ0 can claim.** The
  > note above *already identified the missing lock* — *"in GR the two are locked (g₀₀·g_rr = −1
  > exactly, at every radius) by the field equation"* — and *already found a route to γ = 1* via the
  > Gullstrand–Painlevé flow form. **f·h = 1 is that same lock.** GIJ0 did **not** discover that γ = 1
  > is reachable; the corpus knew on 21 August. What GIJ0 adds is a **motivation stated in this
  > framework's own terms** (cells tiling the posited background) rather than adopting the GP form
  > wholesale, and GOI0 adds the vector sector for free. **And it cannot be claimed that the per-axis
  > reading was reached independently of the 21 August note, which names exactly that condition.**
  >
  > **⚠ The 21 August objection — *"it would fix these tests by being GR — a reformulation, not a
  > rival"* — still applies, and is now the stated GOAL rather than a defect:** the aim is to
  > *reinterpret* GR so it can meet the quantum sector, not to refute it. **But the consequence must
  > be stated plainly: because the 1PN metric here IS GR's, these four tests do NOT discriminate
  > between this framework and GR. They are a consistency floor that had to be cleared, not evidence
  > for the framework.** The first genuine difference appears at 2PN (f·h = 1 − M²/4r² for
  > Schwarzschild), where it is **1.6×10⁻¹⁶ at Mercury — real, and unmeasurable.**
  >
  > **⚠ The cost, labelled.** **f·h = 1 is INSERTED, not derived** — it does not follow from
  > {ψ = ρe^{iθ}, ℓ₀ = cτ₀, mass = cycle rate}. **And its reading is chosen, not forced:** the
  > 4-volume reading (√−g = 1) gives **γ = 1/3** and is excluded; only the **per-axis** reading gives
  > γ = 1. The honest total is **one inserted posit plus one chosen reading**, which is cheaper than
  > importing the field equations but is not free.
  >
  > **What was checked and did NOT go the framework's way, reported because it is what makes the
  > above non-trivial:** the closure relation ℓ₀ = cτ₀ **alone cannot fix the spatial metric** (it
  > relates two proper-frame quantities; h drops out identically), and the intuitive
  > excitation-size reading gives **γ = −1, the wrong sign**. On the vector side, the natural
  > superfluid reading — shift = phase flow — gives **∇×∇θ = 0 and therefore exactly zero dragging**.
  >
  > **One structural question was raised and settled (P6R0):** is f·h = 1 a gauge condition or a
  > physical principle needing a preferred frame? **Neither.** Gauge cannot change an observable, and
  > this moves deflection by 0.88″; and the construction references only **source–observer relative**
  > velocity, so the preferred-frame parameters α₁, α₂, α₃ are **structurally absent**. The condition
  > is boost-invariant at first order in Φ, failing only at O(Φ²) with coefficient
  > −8β²/(1−β²)² (measured −3.555869 vs analytic −3.555556).
  >
  > ---
  >
  > ### ⚠ REVISED 5 September 2026 — f·h = 1 is a CHECK, not the mechanism, and it cannot radiate
  >
  > **Two limitations of the block above, found the day after it was written.**
  >
  > **1. This construction has the wrong radiative content.** A symmetric metric has 10 components;
  > gauge and constraints leave GR with **2 propagating degrees of freedom — the two tensor
  > polarisations LIGO and Virgo observe.** The construction above is built from **one function**
  > (g₀₀ = −f², g_ij = f⁻²δ_ij), so it carries **1** degree of freedom: a **scalar breathing mode**.
  > **It reproduces the static 1PN metric correctly and cannot reproduce gravitational radiation at
  > all.** That is not a gap to be filled later by the same route — a one-function metric has nowhere
  > to put a second polarisation.
  >
  > **2. The actual dynamics were already located elsewhere, and they make f·h = 1 redundant.**
  > EGC0 (18 Jul 2026) identified gravity's coefficient as the **Sakharov induced-gravity
  > coefficient**, with the clean coupling factor **(1/6 − ξ) = 1/6** for minimal coupling — which is
  > how this framework's phase couples. Sakharov induction generates an **Einstein–Hilbert term**, and
  > a theory whose gravitational action *is* Einstein–Hilbert has Einstein's field equations. So
  > **γ = 1 and β = 1 follow from varying an action**, not from a condition imposed on components —
  > and the two tensor polarisations come with them.
  >
  > | route | inserted posits |
  > |---|---|
  > | f·h = 1 + covariance (components by hand) | 1 + 1 chosen reading |
  > | induced gravity (dynamics) | **0** |
  >
  > **The price is not new:** G's coefficient was already open on three independent counts — *"G not
  > derived (allowed)"* in §5 above, ACTION0's finding that E₀/ℓ₀ = c⁴/G is an **identity** rather
  > than a check, and EGC0's own floor. **The induced route trades an inserted posit for a floor this
  > file already carried: one fewer independent unknown.**
  >
  > **⇒ So the block above should be read as a CONSISTENCY CHECK — an independent confirmation that
  > the induced route lands where it should — and NOT as the mechanism by which the spatial metric is
  > obtained.** Its numbers stand unchanged. Its role is demoted. **And note that β was never fixed by
  > f·h = 1 at all; induced Einstein–Hilbert supplies it for free.**
  >
  > **What is still NOT derived, and this is unchanged by any of the above:** the **O(1) coefficient
  > of G** (regularisation scheme, species count — EGC0's floor), and whether one-loop induction is
  > more than a heuristic. A numerical check with cutoff Λ = 1/ℓ₀ returns G's order **by
  > construction**, because ℓ₀ is *defined* through G — that is an identity, not evidence.
  > **"The route exists" is not "the dynamics are derived."**
  >
  > **CLOSED 5 Sep 2026 — "is the induced R term the leading one?"** It was listed here as open the
  > day before; it should not have been, because the number is not close. The suppression parameter is
  > **R·ℓ₀²** (curvature in cutoff units): **1.4×10⁻⁹²** at the solar surface, **2.8×10⁻⁷⁸** at a
  > neutron-star surface, and **1.8×10⁻⁷⁶** even just outside a solar-mass black hole. **The induced
  > R term dominates everywhere; higher-curvature corrections are not a threat.**
  >
  > The confusion was that **"higher order" means two different things here, and they differ by ~86
  > orders of magnitude.** At the solar surface the **post-Newtonian** parameter is **4.2×10⁻⁶** while
  > the **higher-curvature** parameter is **1.4×10⁻⁹²**. The 2PN deviation noted above lives in the
  > first; quantum-gravity corrections live in the second. Conflating them produced a worry that was
  > never real.
  >
  > ### The contraction picture — a third route, and the one matching this framework's ontology
  >
  > In this framework spacetime **contracts** rather than curves. Technically that is the
  > **Gullstrand–Painlevé** form already used for black holes here:
  > ds² = −(1 − v²/c²)c²dt² + 2v·dr·dt + dr² + r²dΩ², with **v = √(2GM/r)** the inflow rate — and
  > **g_rr = 1 exactly**, so the spatial slices are **flat** and all the geometry sits in the shift.
  > Since PG *is* Schwarzschild (verified here in August), **the four classic tests come out right
  > with no f·h = 1 posit at all.** *(g_rr at r = 3 km: PG gives **1.0000**, the isotropic form gives
  > **65.23** — the same geometry, described completely differently.)*
  >
  > **And the contraction rate is the natural variable:** **(v/c)² = r_s/r = the post-Newtonian
  > parameter, exactly**, at every radius from the solar surface to a horizon.
  >
  > **⚠ But it is a FRAME CHOICE, not a prediction.** PG and Schwarzschild are the same geometry in
  > different coordinates and every observable agrees. "Contracts rather than curves" is an
  > **ontological reading and a guide to which variables are natural — not a distinct empirical
  > claim.** This file's own 21 August note flagged the same hazard about this route (*"it would fix
  > these tests by being GR"*), and that flag still applies.
  >
  > ### The one outstanding structural problem
  >
  > **Neither f·h = 1 nor the contraction form can produce gravitational radiation.** Both are built
  > from a single function and carry **one** propagating degree of freedom; GR has **two**, the tensor
  > polarisations LIGO and Virgo observe. The full ADM decomposition (shift 3 + spatial metric 6)
  > **can** carry them — but then the economy claimed above is a property of the **static spherical
  > case only** and does not generalise. **This is now the single outstanding structural gap in the
  > metric sector, and only the induced/ADM route can close it.**

## 6. DERIVED — galaxy rotation curves without dark matter (a₀ program G0–G5)
- **The derived-Newtonian sector FAILS** the Milky Way (32% off, baryons only) — same dark-matter problem as Newton. The fix is not in that sector.
- **⚠ WITHDRAWN 4 Sep 2026 — this read "a₀ = cH₀/2π = 1.04×10⁻¹⁰ m/s² is DERIVED, not fitted".** The **proportionality a₀ ∝ cH₀ is derived** (and is Milgrom's, 1983); the **coefficient is not**. TWOPI1 found TFT's own field equation gives the *reduced* Compton range (decay length 1.000000 vs reduced, 0.159155 vs full) ⇒ a₀ = cω₀, and the thermal route's 2π's cancel ⇒ a = cH₀ — both landing on the value this project's own test excludes at 5.5 scatter-widths. INER0 closed the modified-inertia escape. **The data select the 2π; the theory does not supply it.** See `A0_STATUS.md`. Original entry follows for provenance: **a₀ = cH₀/2π = 1.04×10⁻¹⁰ m/s²** *(value corrected 18 Aug 2026: this read 1.08×10⁻¹⁰, which is cH₀/2π at H₀ = 70. At the Planck/DESI H₀ = 67.4 used by the paper and by `PREDICTIONS.md` the value is 1.04×10⁻¹⁰ — and that is the one consistent with the “87% of observed” figure quoted later in this file, since 1.04/1.20 = 87%.)* (MOND *fits* a₀): the phase field is **ultralight** (mass gap m = √Λ/ℓ₀ = the Hubble mass ⇒ Compton wavelength = Hubble radius ⇒ Λ ~ 10⁻¹²²). Its Compton frequency = H₀/2π (2π = h/ℏ = one S¹ cycle) → a₀ = c·f = cH₀/2π. **This is Vic's "α from Λ."** Effectively massless below the cosmic scale (→ §4 gravity), biting only at a₀. **Tested per-galaxy against SPARC** (`verify_a0_sparc_fit.py`, 2696 pts / 147 galaxies): our own log-space RAR fit gives g† = 1.16×10⁻¹⁰ (deep-MOND 1.33×10⁻¹⁰); the derived a₀ = 1.04–1.13×10⁻¹⁰ sits at **0.90–0.97 × g†**, scatter 0.133 dex (lit ~0.12) reproduced, scale universal where constrained → **consistent within ~20% systematics** (M/L, distances), nothing fitted to SPARC.
- **Self-consistency (G2):** if that field *is* the dark energy (Friedmann), Λ cancels → a₀ ∝ cH₀ without solving the CC problem. *(⚠ 4 Sep 2026: the Friedmann relation here is an **unregistered import** — an FRW background assumed, not derived from TFT. Flagged, not withdrawn: the Λ-cancellation argument may not depend on it, but that has not been checked. See study COSM0.)*
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
Full record: `BLACK_HOLES.md`. **Reading two derived facts — √(2GM/r) = the inflow rate of space, and time = phase cycling — gives a complete black hole.** *(Read correctly, 21 Aug 2026: "time = phase cycling" is a statement about **clocks**, not about spacetime. The phase is a **Page–Wootters clock** — what cycles is the clock's **reading**, while the time it measures runs monotonically and without bound. Time is **not** circular here, and the S¹ is **not** a time dimension: it is the vacuum manifold of a ℂ-valued field, and the base manifold is ℝ³ × ℝ. A compact second time would bring ghosts and guaranteed closed timelike curves, and this repo's own arithmetic already excluded it — the same circle had been assigned two periods differing by 61 orders, τ₀ = 1.35×10⁻⁴³ s against 2π/H₀ = 2.88×10¹⁸ s. The phase clock also reproduces special-relativistic time dilation exactly, ticking at 1/γ in the lab frame.)*
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

  > **⚠ CLOSED AT THE SOURCE 21 Aug 2026 (INFL0) — G3 and G4 are not merely unrun.** This framework's
  > symmetry breaking is **pre-inflationary**, by a wide margin: with f = 1.22×10¹⁹ GeV and the tensor
  > bound r < 0.03 giving H_inf < 4.3×10¹³ GeV, the largest de Sitter temperature the field can see is
  > **H_inf/2π < 6.8×10¹² GeV — smaller than f by 6.6 orders.** The symmetry is therefore broken
  > throughout inflation and never thermally restored. Reversing this would need H_inf ≈ 2πf ≈ 10²⁰
  > GeV — seven orders above the observational limit and above the Planck mass — so it does not depend
  > on the inflationary model.
  >
  > **Consequence: any defects formed at breaking are inflated away. This framework predicts NO cosmic
  > strings, NO domain walls and NO primordial winding-line network in the observable universe** — a
  > falsifiable statement this file did not previously make. **So G4's raw material is absent: the
  > magnetogenesis route is closed at the source, not open-but-unfinished.**
  >
  > *(The same fact justifies treating θᵢ as a single global number rather than a distribution: one
  > inflated patch covers the observable volume, so θᵢ is homogeneous.)*
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
- **OPEN (the honest floor):** the values A ≈ √2 and the ratio r ≈ 0.318 — one continuous ratio carries the whole lepton-spectrum mystery; not fixed by symmetry, energetics, collective dynamics, topology, or any single-mode condensate; waits on the full nonlinear soliton interior (like G, |Λ|, a₀'s coefficient). Falsifiable anchor: δ−120° = 2/9 rad (pole-mass, 0.9σ), tested by a ~10× better τ mass. **Terminus (`spec_selfconsistent.py`): r (=A) bottoms out at the generation-mode EXCITATION AMPLITUDE — an initial-condition floor, same class as η, not dynamically derived.** **Sharpened 21 Aug 2026 (RAD0 → LEPS0):** the *dimensionless* ratios r and A are only half of this floor, and the other half is now **identified**: the lepton sector's **absolute scale is M₀ = 313.84 MeV**, fixed by this repo's own mass-dial parametrisation √M₀ = (Σ√m_k)/3 (Koide ratio 2/3 to 0.0009%; electron bracket 0.0404 — the near-cancellation; tau 2.379 ≈ 1+√2). **It is not constructible from this framework's scales** — the best quarter-power fit in f and m_φ misses by 0.41 orders, which is *worse* than the 0.23 expected by chance from that grid. **M₀ sits in the QCD band, closest to the constituent quark mass m_N/3 = 312.76 MeV (0.35%)** — *a known observation in the Koide literature, inherited here rather than discovered, and worth p ≈ 0.05 after accounting for the five QCD-band candidates it could have landed near.* **So this floor is dimensionful and the r/A floor is dimensionless: two different unknowns that a shared label had been hiding. Deriving r would not give the electron's mass; fixing M₀ would not give Koide.**

## 7c. The particle sector — what particles are (12 July 2026)
Full record: `THE_PARTICLE_SECTOR.md`. **One linking invariant (the derived winding-line helicity of §7) carries spin, statistics, baryon number, and chirality at once.** Headlines:
- **Fermions from a bosonic field [derived]:** a spherical Q-ball is a spin-0 BOSON; a twisted vortex loop with ODD self-linking is a spin-½ FERMION (Finkelstein–Rubinstein). Linking computed as parameter-free topology (Hopf link ±1, twist=winding). So leptons are vortons/Hopfions (odd linking), NOT plain Q-balls — the Q-ball was only the mass/charge skeleton. (Resolves: the mass work modeled leptons as bosons.)
- **Neutrinos & parity [derived], no SU(2):** the neutrino = the pure winding-ODD (massless-chiral) limit of the SAME lepton dial (electron 99.85% there; its 0.15% even content IS its mass). Parity violation FORCED — winding reversal flips the odd channel → weak coupling is 100% V−A, no ν_R. Large PMNS / small CKM from ν near-degeneracy vs charged-lepton hierarchy [proposed]. **Sharpened 21 Aug 2026 (WEAK0): "no SU(2)" understates what is here.** Of the weak force's four defining features, **two are already in place** — the maximal parity violation stated above (*the hardest one to obtain accidentally*), and **flavour change is not forbidden**, since beta decay is winding-neutral (see the weak-sector note below). **What is missing is specifically the GAUGE STRUCTURE:** three generators and the mediator masses. **And the route is nameable: SU(2) *is* S³ as a manifold**, so a target carrying S³ would supply it natively rather than by bolting on a gauge field — priced at **+2 real degrees of freedom**. ⚠ **But π₁(S³) = 0, so that target kills the vortex sector — which is exactly where the confinement mechanism above lives. The strong and weak sectors want DIFFERENT targets, and any completion must reconcile that.** *(Ruled out, on three independent grounds: geometric dilation/contraction cannot supply the weak force — ~10⁻⁴⁴ intra-atomically, parity-even and flavour-blind, and a distortion of U(1) is still U(1). Generators come from the symmetry of the target, not the geometry of the base.)*
- **Confinement [computed mechanism, ⚠ scale withdrawn]:** quark = winding-line end; no free end; sine-Gordon term → domain wall → linear V(L). Meson=boson, baryon=fermion (linking parity). ⚠ **Corrected 21 Aug 2026 (QCDA0).** This previously ended *"ONE scale √Λ sets both hadron mass AND confinement tension (as in real QCD)"* — **that is a code-unit statement with no hadronic content in physical units.** A sine-Gordon wall has σ = 8m_φf² and width w ~ 1/m_φ, so the effective string tension is **μ = σw = 8f² — m_φ cancels entirely** — giving **1.19×10⁵⁷ eV² against QCD's 1.94×10¹⁷ eV²: 40 orders too LARGE**, because f is Planckian. **Two dimensional slips travelled with it:** *σ = 8√Λ = the derived kink mass* equates a **1+1D kink MASS** (energy; f dimensionless there) with a **3+1D wall TENSION** (energy³; f an energy there); and **"V(L) = σL" needs a *string* tension, not a wall tension** — it is recoverable only as a strip of width w, so the shorthand silently carries an extra length. **What SURVIVES, and is stronger than the original claim: the confinement MECHANISM is FORCED, not assumed.** A6's single-minimum cosine collapses the vacuum manifold to a point, so every winding must climb the potential and drags a domain wall — a winding-line end cannot be freed. STRUCT1 derived those walls from the vacuum manifold *without reference to confinement*; this section posited them from the sine-Gordon term. **Two independent routes, same structure.** *(And `THE_PARTICLE_SECTOR.md`'s own label — "a model of what a quark is, not a derivation of QCD" — was correct all along; the defect was this line beside it.)* **A wall-endpoint carries exactly ONE established quantum number: spin-½ via odd self-linking.** Fractional charge and colour are floors; baryon number has no carrier (CHRG0); charge-as-winding is withdrawn (CHRG1).
- **FLOORS (the honest boundary):** absolute scales (ν-mass, Λ_QCD) and NON-ABELIAN groups (SU(2)_L for the full weak force, color SU(3) for the full strong force, fractional charge) — the U(1) field gives integer charge (from the number/Noether spectrum — *noun corrected 18 Aug 2026, UNC1; this read "integer winding"*) and derives mechanisms/scale-relations, not absolutes or non-abelian structure. Same pattern as G, |Λ_cc|, a₀-coeff, η. **See §9's consolidated sub-Planckian mass floor** — the absolute-scale gap is now stated as one problem (a Planckian condensate at f = M_Planck ≈ 1.22×10¹⁹ GeV against particle masses 17–22 orders below it) rather than a list. **Consolidated 21 Aug 2026: four of these entries are ONE missing sector.** Fractional charge, colour SU(3), the lepton scale M₀ (§ above) and the confinement tension (§ above) all terminate on the **non-abelian/confining sector this framework does not have** — the same floor, reached four ways. Stating it once is more honest than four separate admissions.

## 7d. Quantum correlations from compact time (13 July 2026; Born rule 14 July 2026)
Full record (with prominent caveats): `QUANTUM_FROM_COMPACT_TIME.md`. **The local field saturates CHSH at S=2.0000 (classical); compact time DERIVES the quantum value AND the Born rule.**
- **The correlation:** TFT's S¹ is a SINGLE-VALUED COMPLEX PHASE. Single-valuedness fixes the loop phase difference; the hidden variable CANCELS → E(a,b)=cos(a−b) (quantum form, NO tuning, no-signaling). A coherent phase = Hilbert space → **Tsirelson caps CHSH at 2√2 automatically** (numerically 2.828; the naive arbitrary-reweight overshoot of 2.90 is FORBIDDEN once the phase is genuine). Quantum coherence = the phase closing single-valuedly on the S¹ time circle → makes precise "quantum uncertainty = ordinary deterministic S¹ behaviour."
- **The Born rule (`born1..5_*.py`, pre-reg `BORN0_prereg.md`):** single-outcome |ψ|² DERIVED from the same closure. Equal amplitudes → equal weights by an EXACT envariance symmetry (pure-environment counter-swap unitary iff |c₀|=|c₁|), no |c|² inserted; **|c_k|² for all amplitudes from that symmetry alone**, exponent 2 = coherent-superposition normalization (equal branches carry 1/√n ⇒ count=1/amp²), not a charge postulate; continuous **Malus P(+|θ)=cos²(θ/2)** uniquely pinned by E=cos θ (other exponents break it); ONE rule |⟨·|Ψ⟩|² gives marginals+no-signaling+E=cos(a−b)+Tsirelson+Malus. Born reduced to the S¹ swap symmetry + additivity.
- **The uncertainty principle (`uncertainty_s1.py`) — the THIRD pillar, DERIVED, no degeneracy caveat:** the single-valued S¹ phase makes the **number/Noether** operator N=−i∂_θ integer (charge quantization) *(noun corrected 18 Aug 2026, UNC1 — this read "the winding". N=−i∂_θ generates phase rotations, so it is the Noether/number charge, not the topological winding; Carruthers–Nieto, cited in the same sentence, call it the number operator. **This is what actually quantises electric charge** — see the withdrawn-then-restored bullet in `PREDICTIONS.md`.)* with exact [N,cosθ]=i sinθ → the Carruthers–Nieto number–phase uncertainty **ΔN·Δθ ≥ ½**, verified for all states, saturated by von Mises (minimum-uncertainty) states, → Heisenberg ½ in the localized limit (0.500). Physical tradeoff: definite charge/winding ⇒ uniform/undefined phase. So ONE structure (single-valued S¹) gives all three QM pillars: charge quantization + correlations/Born + uncertainty.
- **HONEST BOUNDARY:** the correlation and Born results REPRODUCE QM — do NOT beat it, and a Bell test CANNOT distinguish compact-time TFT from standard QM (the uncertainty theorem, §8, is a clean derivation with no such caveat). Value is conceptual (a deterministic account of the correlation, its ceiling, and now the single-outcome probabilities). The Born derivation is assumption-conditional: it rests on non-contextuality/additivity (the envariance soft spot), assumed not derived. OPEN (the real prize, untouched): a distinguishing observable — CHSH and Born are both degenerate with QM.

## 7e. Foundations and limits — what the field is, and where it breaks (18 July 2026)
Full record: `FOUNDATIONS_AND_LIMITS.md`. Asks what the Teotl field IS, with equal weight on where it fails.
- **Time emerges (`pw_emergent_time.py`):** a timeless constraint (Ĥ_C+Ĥ_S)|Ψ⟩=0 with the S¹ phase as Page–Wootters clock reproduces Schrödinger evolution on conditioning (fidelity 1); emergent time cyclic + comb spectrum. ⚠ *Corrected 18 Aug 2026: this clause read “→ the internal-phase S¹ (winding=charge) and the time-S¹ are ONE structure”. **Both halves are withdrawn.** There is no time-S¹ — S1ONT0 established the base manifold is ℝ³ × ℝ — and charge is the **Noether** charge, not the winding (CHRG1). What survives is the Page–Wootters result itself, which uses only the phase as a clock.* "time = phase cycling" = relational time. Floor: reproduces QM → "phase IS time" is an identification, not forced.
- **One circle, one scale (`scale_darkenergy.py`):** one S¹ at H₀ unifies time+charge+a₀+dark energy — a₀ ∝ cH₀ (at cH₀/2π, 87% of obs; *coefficient not derived, `A0_STATUS.md`*), thawing **w≥−1 always**, w₀≈−0.88→wₐ≈−0.2, **a₀↔w locked** (phantom crossing falsifies). Floors: absolute scale=input (CC problem unsolved); quantum=DE identity=hypothesis (degenerate).
- **Measurement as loop-closure (`meas3/4_*.py`):** only definite branches close (single outcome, no branching, Born frequencies), einselection reproduced, E>0 = clock arrow. Floors: *which* outcome (seam phase) + thermodynamic arrow (past hypothesis) = boundary conditions, correctly not derived.
- **THE SHARP NEGATIVE — tensor completeness (`tens_completeness.py`):** an economical (classical) S¹ field is ENTANGLEMENT-BOUNDED — reproduces product/GHZ/area-law (WHY CHSH/Born/GHZ passed, all low-entanglement) but NOT volume-law → **FALSIFIED by quantum-supremacy experiments**. Full 2ⁿ QM requires quantizing the field (Fock/exponential) = standard QFT. **The framework cannot be both economical-classical AND full QM.**
- **Super-Planckian tension (`swmp_tension.py`):** dark energy needs f ≳ 1.45 M̄_Pl in **reduced** Planck units (swampland concern, shared with all thawing quintessence); **TFT's own f = M_Planck(non-reduced) = √(8π)·M̄_Pl ≈ 5.01 M̄_Pl clears that bound but is strongly super-Planckian, so the tension is worse rather than better — see the a₀ paper, which declines to soften it**; monodromy (wind one circle ~15×) = one-S¹-native evasion → winding floor. R³ uncertainty DECOUPLED: a₀ ∝ cH₀ is the field's own de Sitter fluctuation (f-independent), protected from the tension *(the 1/2π coefficient is not derived — `A0_STATUS.md`)*.

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

## 10b. Teotl quanta — a working emulator, and what it does NOT settle (2 Sep 2026)

Built on one principle: **everything is teotl.** A teotl quantum is the field's minimum excitation —
a point carrying one internal phase, cycling. |n⟩ = cycles carried; energy E_C n²; coupling moves one
cycle. Everything below is consequence, not addition.

**`teotl_rotor_qc.py` — DERIVED.** Self-test: X-gate fidelity 0.9950, Ramsey phase error 4.4×10⁻¹⁶,
CZ conditional-phase error 0.0109, **Bell concurrence 0.9997**, norms exact. Works where a soliton
field version failed, because the spectrum is exactly integer, the energy is bounded below (a real
ground state), and H is a finite matrix — so evolution is exactly unitary and the numerical drift
that defeated the field version is structurally impossible.

**Phase count p (hopping moves n by ±p) — DERIVED selection rule.** Exchange requires **p₁ = p₂**;
not imposed, it falls out of the operator, since the exchange moves p₁ cycles off one and p₂ onto the
other. Suppression **15.9× / 65.2× / 146.4×** for p = 1/2/3. **A second, stronger selector follows
from mass = cycle rate:** energy conservation gives **n_A − n_B = p**, measured at 92× suppression
(p = 2). Two quanta can be coupled or decoupled by changing their **states**.

**Two caveats, both measured, both against my own first claims:**
- **The ZZ channel is p-blind** (0.29726 / 0.29823 / 0.29860 matched vs mismatched). p blocks only
  *exchange*; mismatched quanta still entangle. **A selection rule on one channel, not a
  connectivity switch.**
- **No commensurate enhancement.** Multiples ≈ coprimes; suppression tracks **|p₁ − p₂|**.

**`teotl_field_qc.py` — both maps (ℝ³ position, S¹ phase), couplings DERIVED.** Range = the
**reduced** Compton length; coupling J ∝ e^{−r/λ}/r (Yukawa). **Prediction: λ_n ∝ 1/n², so a more
excited quantum has SHORTER reach** — influence radius 2.92/0.73/0.32 for n = 1/2/3. Free parameters
**2 → 1**. The sphere of influence is a **rate limit, not an on/off switch**: concurrence ~0.997 at
every separation, CZ time 2.6 → 46.9 → 7675 for sep 0.5 → 2 → 6.

**Metric — SOURCED (Construction B).** Uses the weak-field form, **not** g_ij = δ_ij(1+|∇θ|²/E₀²),
which §10 records as falsified. Energy density ≥ 0 everywhere ⇒ contraction has one sign. **More
excited ⇒ deeper well:** dτ/dt = 0.971/0.830/0.533 for n = 1/2/3.

**⚠ WHAT THIS DOES NOT SETTLE — three open items, stated plainly:**
1. **The metric is SOURCED, not DYNAMICAL.** There is still **no equation of motion for the metric**
   anywhere in this work. Computing the geometry the quanta produce is not the same as geometry that
   evolves. **This is the gap between having a gravity sector and having gravity.**
2. **The n² mass spectrum does NOT give the lepton hierarchy.** μ/e needs √206.77 = 14.379 (not an
   integer). τ/e needs 58.968, near 59 — **recorded as coincidence and refused**, since the other
   ratio misses badly. Structural: tower ratios *decrease* (4, 2.25, 1.78) while the hierarchy
   *increases* (207, 17). Same wall §10's spectrum work already reached.
3. **Not competitive as a QC tool.** 2 qubits, no noise models, no scaling past ~3–4 quanta.
   `scqubits` does the Cooper-pair box, cos(2φ) and coherence estimation properly. **What is claimed
   here is the derivation, not the tool.**

**Independently reproduced a real device class.** The phase-count structure at p = 2 is the cos(2φ)
qubit, whose parity protection — *"couples only charge states within the same parity sector"* — is
exactly the sector decoupling measured here. Arrived at from the principle, not imported.


### The mass hierarchy: both counting routes excluded, and ε reduces to σ (3 Sep 2026)

**A bound, and it is not circular — but it is REGIME-DEPENDENT.** E_n = E_C n² is **superadditive**,
so splitting always lowers energy (|2⟩→|1⟩+|1⟩ costs 4, yields 2); every state above n = 1 is then
unstable to fragmentation and each quantum is two-state. This follows from the spectrum's shape and
**not** from ℓ₀ = cτ₀.

> **⚠ CORRECTION (3 Sep 2026, audit): this is a CHARGE-REGIME result and does NOT apply to TFT.**
> Superadditivity is a property of E ∝ n². **TFT requires the *phase* regime** (long-range phase
> coherence is phase localisation), where the tower is approximately harmonic, E_n ≈ ħω(n+½), and
> splitting **costs** energy — |1⟩+|1⟩ is 3.0 against a whole of 2.5. **There every state is stable:
> no fragmentation bound, and quanta are not two-state.** The bound holds for the emulator, which
> runs at E_J/E_C = 0.05, not for the theory.

**So particles must be composites. Binding was tested and fails too:** M(N)/M(1) = 1, 2, 3, 4, 5 —
exactly linear, consecutive ratios 2.0 → 1.25, decreasing toward 1.

**The structural argument, independent of coupling strength:** the observed log-mass increments are
5.332 then 2.822 — they **shrink by half**. A binding law adds more binding as N grows (N(N−1)/2
pairs), so its increments **grow or flatten**. Wrong direction. **⇒ Not merely "excitation towers
fail" but "anything monotone in a count fails."**

**The interference route survives, and M3's pointer is confirmed.** Under the ℤ₃ sum only harmonics
n ≡ 0 mod 3 appear, so degrees 3–5 admit only n = 3 and force extrema onto 60° multiples (excluded at
26,620σ). **Degree 6 is the first to admit {3, 6}** and can place an extremum at the observed
δ = 132.73282° with ratio a₆/a₃ = −0.318 (O(1), untuned), a genuine minimum for a₃ < 0.

**This is a FIT, not a derivation** — one equation, one ratio, fed the observed δ; nothing spare.
**But the degree-6 coefficient is the sextic, i.e. σ. So ε is not a new free parameter: it reduces to
σ**, the floor already recorded. The count of independent unknowns does not grow.

### T-duality: examined and ruled out for TFT (3 Sep 2026)

**The mechanism is real.** E² = (n/R)² + (wR)² is exactly invariant under R → k/R with n ↔ w
(verified to 1e-12), so probing below the self-dual radius costs the same as probing above its
reciprocal — there is no new physics below it. **It is the one mechanism that prevents
short-distance infinities without an external anchor**, and unlike a cutoff it is an internal
symmetry.

**TFT cannot have it, and the reason is general.** A compact *field* on a circle of circumference L
has θ(x+L) = θ(x) + 2πw, hence ∂θ = 2πw/L and **E_w = (f²/2)(2πw)²/L — inversely proportional to L,
the same direction as momentum.** A *string* winding scales as **L**, the opposite direction, which
is what makes the swap possible.

**T-duality requires an extended object that must physically stretch to wrap. A field winds for
free — the gradient simply spreads out.** So no duality is available on any circle: not the compact
time direction, not a spatial one.

Two related claims are withdrawn: that this route escapes the cutoff problem (it would, but is
unavailable), and that it assigns a role to the winding sector (it does not — the winding number is
a vortex charge in non-compact space, not momentum's partner on a shared compact dimension).


---

## 11. Scorecard
| Piece | Status |
|---|---|
| Stable particle (Q-ball); kink mass + F=Ma; breather | DERIVED |
| Electromagnetism: charge + Coulomb 1/r², like-repels | DERIVED |
| Gravity: universal 1/r attraction (Poisson-sourced T⁰⁰) | DERIVED |
| Matter & antimatter both attract | DERIVED — matches ALPHA-g |
| Toy solar system: Kepler + Mercury 42.90″ | DELIVERED (Kepler by-construction; Mercury generic-1PN) |
| Galaxy rotation curves, no dark matter | mechanism DERIVED, scale a₀ ∝ cH₀; **coefficient NOT derived (`A0_STATUS.md`)**; MW 2.9%, SPARC-consistent, Tully-Fisher slope 4 |
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
Quantum from compact time: `chsh_compact_time.py`, `chsh_closure.py`, `born1_envariance.py`, `born2_measure.py`, `born3_finegrain.py`, `born4_malus.py`, `born5_closure_knit.py`, `dis1_distinguish.py`, `dis2_ghz.py`, `uncertainty_s1.py` (+ docs `CHSH0_prereg_compact.md`, `BORN0_prereg.md`, `DIS0_prereg.md`, `UNC0_prereg.md`, `QUANTUM_FROM_COMPACT_TIME.md`); builds on `teotl_qc.py`, `teotl chsh.py`.
Foundations and limits: `pw_emergent_time.py`, `scale_darkenergy.py`, `meas3_selection.py`, `meas4_classical_arrow.py`, `tens_completeness.py`, `swmp_tension.py` (+ preregs `PW0/SCALE0/MEAS3/MEAS4/TENS0/SWMP0_prereg.md`, doc `FOUNDATIONS_AND_LIMITS.md`).
- **Distinguishing observable — searched, none feasible (§7 of the companion):** compact-time TFT is **empirically degenerate** with QM. Bell is exactly degenerate at any loop size (hidden time-phase cancels); the temporal energy-comb Eₙ=2πn/T differs but scales 1/T (unobservable at T~1/H₀; microscopic T excluded by continuous spectra); GHZ/Mermin reaches **M=4=QM** (full contextuality reproduced). The QC arc's "no distinguishing test" is now a quantified result, not a caveat. One open edge: whether the single-field S¹ construction realizes the full 2ⁿ tensor Hilbert space — if it saturates at 2-body it gives M~0 and is falsified by GHZ.

---

**One-paragraph version:** *(rewritten 18 Aug 2026 — the previous version predated this year's audits and still asserted three things withdrawn elsewhere in this same file. It is replaced rather than patched.)* TFT gives, from **one complex field ψ = ρe^{iθ}: ℝ³ × ℝ → ℂ** — a compact phase and a non-compact amplitude, with the circle appearing as the **vacuum manifold**, not the target: a stable particle (Q-ball); **electromagnetism** (Coulomb, like-charges repel) from the **U(1) Noether charge** j⁰ = ρ²ω — *not* from the winding, which sources no monopole field; gravity as emergent geometry (universal 1/r, matter and antimatter both fall); a working toy solar system (Kepler + Mercury 43″, one frozen constant — **but see §6's scope correction: the 43″ is not reachable from the derived 00-equation alone, which gives 14.33″; the full metric's spatial part is imported**); and galaxy rotation curves without dark matter, with the MOND scale **a₀ ∝ cH₀ following from the field being ultralight dark energy — the proportionality derived (and Milgrom's, 1983), but the coefficient 1/2π NOT derived: withdrawn 4 Sep 2026, see `A0_STATUS.md`**. **Withdrawn from the earlier version of this paragraph:** the baryogenesis/magnetogenesis/chirality trio as *one* topological invariant with an *automatic* anomaly (§7 — they are two independent invariants and the anomaly is neither automatic nor derived); charge as the *winding* (see the substrate row); and the base manifold ℝ³ × S¹ (time is not compact). **The recurring pattern, sharpened:** what a **shift symmetry protects** derives parameter-free — the phase sector, where every DERIVED claim lives; what it does not protect is a floor — the amplitude sector, where every absolute mass sits, 16–22 orders below the condensate. Everything is runnable, and the withdrawals above are as much a part of the record as the derivations.
