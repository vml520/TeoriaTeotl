# TFT — Predictions (for the paper)

*Labels: **[prediction]** forced & testable · **[consistency]** reproduces known physics, not unique · **[open]** connection identified, derivation unfinished · **[candidate]** predicted, needs development.*

## Tier 1 — Genuine, distinctive predictions (lead with these)

**1. The galactic acceleration scale is tied to the expansion rate: a₀ ∝ cH₀.**
The **proportionality** follows from the mechanism (the field is the dark energy; Λ cancels). The
**coefficient is not derived** — see the withdrawal below. **[open — mechanism derived, coefficient not]**

> ## ⚠ WITHDRAWN (4 September 2026): "a₀ = cH₀/2π, parameter-free"
>
> **This entry previously read "The galactic acceleration scale is not free: a₀ = cH₀/2π…
> Parameter-free… MOND must *fit* this; TFT *predicts* it. [prediction, matches data]". That claim
> is withdrawn.** The 16 August note below is retained for provenance but is **itself understated**.
>
> Study **TWOPI1** (26 Aug 2026) checked two independent routes and **both return the factor 1, not
> 1/2π**: the linearised field equation's propagator pole fixes the range to the **reduced** Compton
> wavelength (fitted decay length **1.000000** vs reduced, **0.159155** vs full), giving a₀ = cω₀;
> and the Milgrom-style thermal condition carries 2π on *both* sides, so they **cancel exactly**,
> giving a = cH₀. **Both land on a₀ = cH₀ — the value this project's own test records as 5.5
> scatter-widths from g† and "excluded outright".**
>
> So the 2π is **not an absorbable convention** but a **6.28× factor the framework needs to reach the
> data and cannot obtain from its own dynamics.** The escape TWOPI1 left open — a genuine
> *modified-inertia* mechanism — was then closed by **INER0**, which found field inertia ≡ stiffness
> ≡ f², so TFT is committed to modified *gravity*.
>
> **What survives:** the mechanism (**a₀ ∝ cH₀**), a proportionality **Milgrom established in 1983**;
> and the SPARC work below, which is empirical and unaffected. **The data select a 2π-ish factor
> (2π at 0.5 scatter-widths, π at 1.8, none at 5.5) — the data select it, the theory does not derive
> it.** Full statement: **`A0_STATUS.md`**.

*Tested directly against SPARC, per galaxy* (`verify_a0_sparc_fit.py`; 2696 points from 147 galaxies): fitting the Radial Acceleration Relation ourselves gives g† = 1.16×10⁻¹⁰ m s⁻² (deep-MOND a₀ = 1.33×10⁻¹⁰), against which the value cH₀/2π = 1.04–1.13×10⁻¹⁰ *(the coefficient selected by the data, not derived — see above)* sits at **0.90–0.97 × g†** — consistent within the ~20% systematic band set by mass-to-light ratios and distances, with the relation's tightness reproduced (0.133 dex vs the literature's ~0.12) and the same scale recovered across galaxy mass wherever the data constrain it. Nothing here is fitted to SPARC; H₀ is an input.

> **Correction (16 August 2026) — the 2π.** ⚠ *Retained for provenance; **SUPERSEDED** by the
> 4 September withdrawal above, which found this framing too mild — the dynamics do not merely
> fail to force the convention, they deliver the other answer.*
> This sentence previously ended "the 2π is the derived
> content." **That overstates and is withdrawn.** The 2π is the conversion h/ℏ between angular and
> cyclic frequency, and it is *absorbable*: writing a₀ = cν₀ with ν₀ the mass gap's cyclic rate
> removes it entirely. So the substantive claim is **"the relevant rate is cyclic, not angular,"**
> and nothing in the framework *forces* that for the mass gap specifically — the appeal to "one
> cycle of the circle" concerns traversal of S¹, whereas the mass gap is a curvature of the
> potential. What does support it is that the framework applies the per-cycle convention
> **consistently** (in ℏ = E₀τ₀/2π, in the field's inertia, and here), which is worth stating and
> is not the same as forced. Empirically, against g† and the relation's 0.133 dex scatter: omitting
> the factor entirely sits **5.5 scatter-widths** away and is excluded; 2π sits at **0.5**; but π
> sits at **1.8** — disfavoured, not killed. **The data select a 2π-ish factor; they do not isolate
> 2π.** What remains derived is the *mechanism* — the field is the dark energy, Λ cancels, and
> a₀ ∝ cH₀ follows.

**2. The baryonic Tully–Fisher exponent is exactly 4** (V⁴ ∝ M).
Parameter-free consequence of the deep-MOND limit. Observed: 3.85 ± 0.09 (SPARC). **[prediction, matches data]**

**2b. Inherited liability: galaxy clusters.** Reproducing MOND phenomenology on galaxy scales means
inheriting MOND's most-discussed failure. In clusters a residual mass discrepancy of ≈1.5–2 survives
the modification, and **this framework's position is slightly worse rather than better**: cluster
accelerations sit near the transition (≈0.8 a₀ at 1 Mpc for Coma), where g ≈ √(g_N a₀) makes the
required baryonic mass scale as 1/a₀ — so adopting 1.04×10⁻¹⁰ rather than the *fitted* 1.2×10⁻¹⁰
raises the requirement by ≈9% and the residual to ≈1.6–2.2. **A freely fitted a₀ can drift upward to
relieve this; one pinned to cH₀/2π cannot** *(though, per `A0_STATUS.md`, that coefficient is now
selected by the data rather than derived — so this liability is softer than previously stated)*.
No resolution is offered, and nothing native rescues it:
there is no larger external field for the most massive bound systems, tuning the interpolation would
be fitting, and a dark-matter component is what the framework exists to avoid. **[known failure,
stated]**

**3. Dark matter and dark energy are the same field.**
The galactic "dark-matter" scale equals the dark-energy scale (a₀ ↔ ρ_Λ). Corollary: **no dark-matter particle exists** — direct-detection and collider searches stay null. Distinctive from ΛCDM. **[prediction, falsifiable]**

**4. Dark energy is dynamical (thawing quintessence), not a constant — and it CANNOT go phantom.**
The field is the S¹ phase with the sine-Gordon cosine potential = a pseudo-Nambu-Goldstone thawing quintessence, an ordinary scalar, so **w ≥ −1 at all times** (a full integration gives w_min = −1.0000 on the whole track). w = −1 in the past, rising today: **w₀ ≈ −0.88**, **wₐ ≈ −0.20**.
*(Updated 15 Aug 2026: re-integrated at the corrected decay constant, giving **wₐ ≈ −0.20** — −0.196 as −dw/da at a=1, −0.168 under a CPL fit over 0<z<2. This supersedes the earlier −0.24. The result is insensitive to f: holding w₀ = −0.88 and re-shooting the misalignment, wₐ moves only from −0.213 to −0.194 across f = 1.5–10 M_Pl.)* Opposite of a cosmological constant, and opposite of a phantom. **[prediction — the no-phantom feature is the sharp falsifier]**

**5. ⭐ Galaxies predict dark energy (the centerpiece).**
Because a₀ and dark energy are one field (mass ~ H₀, giving both a₀ ∝ cH₀ — *coefficient not
derived, see `A0_STATUS.md`* — and just-thawing-now), the scale that fits *galaxy rotation curves* **forces** the dark-energy equation of state: w₀ ≈ −0.88 and a specific wₐ ≈ −0.20, with w ≥ −1. No other framework connects these (MOND has no dark energy; ΛCDM has neither a₀ nor evolution). **The falsifier is categorical, not a matter of degree:** DESI's w₀wₐCDM fit prefers a *phantom crossing* (w < −1 in the past) that a thawing scalar cannot produce.

**Status as of August 2026 — the tension still runs against this prediction.** Across two releases the preference for an *evolving* equation of state has firmed rather than faded: 2.6σ in DR1 (DESI+CMB) → **3.1σ in DR2**, and 2.8–4.2σ once supernovae are added. The DR2 best fit (DESI+CMB+Pantheon+) is w₀ = −0.838 ± 0.055, wₐ = −0.62 (+0.22/−0.19) — a trajectory that **crosses w = −1 in the past** — and DESI reports that non-phantom models are **disfavoured**. TFT and DESI *agree* on what separates both from a cosmological constant: dark energy evolves, and ΛCDM is disfavoured. They part on the magnitude of wₐ — on whether w ever dipped below −1. We state the prediction (**w ≥ −1**) and we state that the current measurements do not meet it. If the crossing hardens with DR3 / Euclid, **TFT's dark-energy sector is excluded.** **Refreshed 7 August 2026.** The most recent DESI analysis — DR2 Results IV, adding the full-shape Lyman-α forest (arXiv:2607.27410) — puts the evolving-DE preference at **2.7σ (DESI+CMB)** and **3.2σ (with supernovae)**, *softer* than the earlier DR2 figures of 3.1σ and 2.8–4.2σ. **This is recorded because it happened, not because it helps.** The direction is unchanged: the dedicated Lyman-α analysis (arXiv:2510.21976, A&A 2026) finds *every* parameterisation favouring w₀ > −1, wₐ < 0 and **w₀ + wₐ < −1** — Quintom-B, i.e. phantom in the past and quintessence today, which is a crossing, and a crossing is what this prediction forbids. A tension easing from 4.2σ to 3.2σ is still a tension. No combination has approached 5σ in either direction; Lyman-α with galaxy BAO alone reaches only ~1.6σ.

See `a0_de_study.py` / `BLACK_HOLES.md`. **[prediction; sharp falsifier — currently in tension]**

## Tier 2 — Predicted, needs development

**6. a₀ evolves with cosmic time: a₀(z) ∝ cH(z).** Early-universe galaxies had a *higher* transition acceleration — a clean discriminator from constant-a₀ MOND; testable with high-z rotation curves. **[candidate]**

**7. Primordial magnetic fields are helical, with a handedness correlated with the matter–antimatter asymmetry.** A parity-odd cosmic signature (CMB parity / Faraday rotation); no standard model produces it. **[CONJECTURE — downgraded 18 Aug 2026, was ⭐ "the most original prediction"]**

> **Why downgraded (BMCA0 audit).** "Locked" requires the sign of the helicity to be *determined by*
> the sign of the baryon asymmetry. **It is not, and the lock breaks in both directions:** two
> unlinked W=+1 windings give maximal baryon asymmetry with **zero** helicity and no handedness at
> all; a linked W=+1/W=−1 pair gives **zero** baryon asymmetry with maximal helicity and a definite
> handedness. Baryon number and helicity are independent topological invariants (see
> `DERIVED_SUMMARY.md` §7), and **no TFT mechanism correlating them was ever built** — G3 and G4
> were never run. The correlation remains reasonable *as a conjecture*, since in the Vachaspati
> scenario one mechanism does generate both; but in TFT that mechanism is precisely what is missing.
> **This was published as a starred prediction with no derivation behind it.**

## Structural results — real, but *consistency*, not novel predictions

- ~~**Charge is quantized in integer units** because it is a winding number~~ — **WITHDRAWN 18 Aug 2026 (CHRG1).** **The winding is not the electric charge.** Electric charge is the monopole moment of the long-range field, and a winding configuration has none: the Gauss flux of a closed vortex loop is zero at every radius, while the U(1) Noether source gives −4πq. Structurally, **π₂(S¹) = 0** — an S¹-valued field on ℝ³ has no point-like topological charge at all; its defects are *lines*. Every derivation in this repo (Coulomb, the Q-ball's mass and charge) uses the **Noether** charge j⁰ = ρ²ω, which is **continuous** classically. **So TFT does not currently explain why charge comes in integer units** — this repo *imposes* U(1) charge quantisation as a condition (`THE_PARTICLE_SECTOR.md`:102), which is the same move this bullet criticised the Standard Model for. **[WITHDRAWN]**

  > **RESTORED, in a weaker and more honest form — 18 Aug 2026 (UNC1).** The route named above was
  > taken the same day, and it works: this repo's number–phase result (`uncertainty_s1.py`) already
  > proves the integer spectrum — it had simply **labelled its operator "the winding."** N = −i∂_θ
  > generates phase rotations, so it is the **number/Noether** charge (as Carruthers–Nieto, the
  > cited source, call it). **Charge quantisation was never missing; it was mis-attributed.**
  >
  > Verified, with the control that makes it a result: on single-valued states the spectrum is
  > exactly ℤ, and **twisting the boundary condition to ψ(θ+2π) = e^{iα}ψ(θ) moves every eigenvalue
  > to n + α/2π** — so single-valuedness on S¹ is doing the work and the outcome could have been
  > otherwise.
  >
  > **Scope, stated plainly, because the original bullet overclaimed.** ⚠ **The mechanism is the
  > textbook compact-U(1) argument** ('t Hooft; Dirac) — *any* complex scalar with a compact phase
  > gives it. TFT does **not** explain integer charge where the Standard Model cannot. What is
  > distinctive is only the **provenance**: the SM *takes* U(1)_Y compact because it works, whereas
  > TFT's field target **is** S¹ — a founding primitive adopted long before charge was considered.
  >
  > **The genuinely distinctive claim is a different one: species commensurability.** The real
  > puzzle is not "why integers" for one species but **why Q_proton = −Q_electron exactly.** Two
  > independent U(1)s with generic couplings give irrational charge ratios; the SM fixes its ratios
  > using anomaly cancellation plus the observed fermion content. **In TFT every particle is a
  > configuration of ONE field with ONE U(1), so every charge is an integer multiple of one unit
  > automatically.** That is earned by the same single-field monism that costs this framework
  > baryon and lepton number.
  >
  > **Cost:** charge quantisation is now a consequence of **quantising** the theory, not a classical
  > or topological fact about it — and the quantisation step itself is posited (see the
  > compact-phase companion). **[RESTORED — quantum, not topological; textbook mechanism, distinctive
  > provenance]**

## Striking connection — mechanism demonstrated, coefficients open (state explicitly)

- **Three lepton generations = three phases of one particle = the Koide relation**, which predicts the tau mass from the electron and muon to **0.006%.** Status after the gated generations program (full record: `GENERATIONS_PROGRAM.md`): the pattern is exactly **one scale + one angle ε = 2.27° from a cancellation point** — the electron is anomalously *light* (m_e ∝ ε²), an almost purely winding-odd ("helical") state, 99.85% invisible to the mass channel. The interference mechanism **exists in the framework** (the Q-ball binds an internal generation dial with an exact square-law energy), generations-as-excitations is **excluded** (1D exact + 3D numerical), and three whole mechanism classes for the balance are **closed**. The ε sub-program then narrowed the last unknown: topological quantization of the offset is **excluded** (212σ), ε's origin must respect the 120° symmetry (rigidity theorem) and lives in **one interference channel whose pitchfork threshold is what makes the electron light**, and Koide is an **on-shell (pole-mass)** fact. What remains open is a single continuous ratio r ≈ 0.318 — like every absolute number in the framework, it waits on the soliton interior. **[mechanism demonstrated — one ratio open]**
- **A falsifiable precision hook on ε (no mechanism attached, flagged as such):** the dial angle satisfies δ − 120° = **2/9 rad** to within 0.9σ of current data (the known Brannen form) — specifically a **pole-mass** statement (it degrades under short-distance running). A ~10× improvement in the tau mass — feasible at future e⁺e⁻ machines — confirms or kills it sharply. The nearby candidate 1/(8π) is already excluded at 25σ, and the whole class of rational-fraction-of-a-turn values at 212σ. **[watch item, falsifiable]**

## Null / long-term

- **The proton is absolutely stable** (τ_p > 10⁴⁰ yr) — ~~baryon number is topological~~. Testable at Hyper-Kamiokande. **[WITHDRAWN 18 Aug 2026 — the stated basis does not exist]**

  > **Why withdrawn (CHRG0).** The prediction rests on baryon number being a topological invariant.
  > **It is not, because there is nothing left to carry it.** A single S¹-valued phase field supplies
  > exactly **one** integer topological charge, the winding W — and this repo spends that same
  > integer three times: as electric charge (the integer-charge result), as baryon number (this
  > prediction), and as self-linking parity (the spin-statistics result, where
  > `THE_PARTICLE_SECTOR.md` states **SL = W** outright).
  >
  > **The electron decides which use is legitimate.** It is a spin-½ fermion, so its self-linking
  > must be odd, so **W must be odd** — and it has baryon number 0. If W were baryon number the
  > electron would have W = 0, hence even self-linking, hence **spin 0**. It is not a boson.
  > **So baryon number has no topological carrier.** *(Corrected 18 Aug 2026: this note first
  > continued "…so W **is** electric charge." **That was a non-sequitur** — spin-½ constrains only the
  > **parity** of W, not its value, and CHRG1 has since shown W cannot be electric charge at all. The
  > argument **against** B = W is untouched, so this withdrawal stands.)*
  >
  > The remaining candidates fail for computable reasons: magnetic helicity is **quadratic** in the
  > windings, so it vanishes identically whenever W = 0 (the neutron, Q = 0, would get B = 0); the
  > U(1) **Noether** charge is **continuous** classically and cannot be an integer baryon number;
  > and self-linking reduces to **writhe** when the twist vanishes, which is also continuous.
  >
  > **This does not predict that the proton decays.** It withdraws the claim that TFT *forbids* it.
  > Restoring the prediction requires new structure — a second phase field (abandoning the
  > single-field monism the spec declares) or a quantised Noether charge — and either is a change
  > of theory whose cost should be stated up front.
  >
  > **Related gap, previously unflagged:** by the same argument **lepton number has no carrier
  > either**, and the term appeared nowhere in this repo before this note.
- **No dark-matter particle** (from #3). **[prediction, null]**

---

**One-line framing:** *TFT's central testable claim is that dark matter and dark energy are one dynamical field — which makes galaxy rotation predict the dark-energy equation of state, a cross-observable link no other framework offers, matching DESI's w₀ and its finding that dark energy evolves, but in tension with DR2's preferred wₐ, which crosses the phantom divide TFT forbids.*
