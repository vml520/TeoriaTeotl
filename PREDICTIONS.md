# TFT — Predictions (for the paper)

*Labels: **[prediction]** forced & testable · **[consistency]** reproduces known physics, not unique · **[open]** connection identified, derivation unfinished · **[candidate]** predicted, needs development.*

## Tier 1 — Genuine, distinctive predictions (lead with these)

**1. The galactic acceleration scale is not free: a₀ = cH₀/2π ≈ 1.1×10⁻¹⁰ m/s².**
Parameter-free — set by the cosmic expansion rate. MOND must *fit* this; TFT *predicts* it. Matches observation within ~10%. **[prediction, matches data]**

**2. The baryonic Tully–Fisher exponent is exactly 4** (V⁴ ∝ M).
Parameter-free consequence of the deep-MOND limit. Observed: 3.85 ± 0.09 (SPARC). **[prediction, matches data]**

**3. Dark matter and dark energy are the same field.**
The galactic "dark-matter" scale equals the dark-energy scale (a₀ ↔ ρ_Λ). Corollary: **no dark-matter particle exists** — direct-detection and collider searches stay null. Distinctive from ΛCDM. **[prediction, falsifiable]**

**4. Dark energy is dynamical (thawing quintessence), not a constant — and it CANNOT go phantom.**
The field is the S¹ phase with the sine-Gordon cosine potential = a pseudo-Nambu-Goldstone thawing quintessence, an ordinary scalar, so **w ≥ −1 at all times** (a full integration gives w_min = −1.0000 on the whole track). w = −1 in the past, rising today: **w₀ ≈ −0.88**, **wₐ ≈ −0.24**. Opposite of a cosmological constant, and opposite of a phantom. **[prediction — the no-phantom feature is the sharp falsifier]**

**5. ⭐ Galaxies predict dark energy (the centerpiece).**
Because a₀ and dark energy are one field (mass ~ H₀, giving both a₀ = cH₀/2π and just-thawing-now), the scale that fits *galaxy rotation curves* **forces** the dark-energy equation of state: w₀ ≈ −0.88 and a specific wₐ ≈ −0.24, with w ≥ −1. No other framework connects these (MOND has no dark energy; ΛCDM has neither a₀ nor evolution). **The falsifier is now categorical, not a matter of degree:** DESI's w₀wₐCDM fit prefers a *phantom crossing* (w < −1 in the past) that a thawing scalar cannot produce. If DESI DR2 / Euclid **confirm phantom crossing → TFT's dark energy is falsified**; if the fit **relaxes onto the thawing track (w ≥ −1) → confirmed.** A near-term yes/no. See `a0_de_study.py` / `BLACK_HOLES.md`. **[prediction; sharp falsifier]**

## Tier 2 — Predicted, needs development

**6. a₀ evolves with cosmic time: a₀(z) ∝ cH(z).** Early-universe galaxies had a *higher* transition acceleration — a clean discriminator from constant-a₀ MOND; testable with high-z rotation curves. **[candidate]**

**7. ⭐ Primordial magnetic fields are helical, with a handedness locked to the matter–antimatter asymmetry.** A parity-odd cosmic signature (CMB parity / Faraday rotation) — the most original prediction; no standard model produces it. **[candidate]**

## Structural results — real, but *consistency*, not novel predictions

- **Charge is quantized in integer units** because it is a winding number — answers "why integer charge" (the Standard Model inserts it by hand). In the Skyrme/topological-soliton lineage. **[consistency]**
- **Gravity is universally attractive; matter and antimatter both fall** (✓ ALPHA-g 2023) — but GR+CPT predicts it too. **[consistency]**
- **Solar system: Kepler + Mercury's 42.9″/century** from one constant — Kepler is by-construction, Mercury is the generic relativistic result. **[consistency]**
- **Exact lepton universality coexisting with a 3477× mass hierarchy.** Gauge couplings are winding *integers* (topologically quantized → identical for all three generations); masses are *amplitudes* (continuous → hierarchical). One structure yields both observed facts at once. See `GENERATIONS_PROGRAM.md` / `mass_m4_chirality.py`. **[consistency]**
- **Mesons are bosons and baryons are fermions**, from one rule: a quark is a soliton of odd self-linking (a spin-½ fermion by Finkelstein–Rubinstein), so hadron statistics = (−1)^(#quarks). The same **linking invariant carries spin, statistics, baryon number, and chirality**. See `THE_PARTICLE_SECTOR.md` / `spin_statistics.py`. **[consistency]**
- **Parity violation is forced, not inserted**: the parity operation is winding reversal, and the weak (chiral) coupling is to the winding-odd channel → 100% V−A, and **no right-handed neutrino**. The **neutrino** is the pure-odd (massless-chiral) limit of the *same* lepton dial. See `neutrino_parity.py`. **[consistency / derived]**
- **The confinement scale equals the hadron mass scale**: linear confinement with string tension σ = 8√Λ = the derived kink mass — one scale √Λ sets both, as in real QCD (m_proton ~ Λ_QCD). See `quark_confinement.py`. **[consistency]**
- **Large neutrino mixing (PMNS) but small quark mixing (CKM)** from one mechanism: neutrinos sit near the mass-cancellation point → near-degenerate → maximal mixing; charged fermions are hierarchical → tiny mixing. **[candidate]**

## Striking connection — mechanism demonstrated, coefficients open (state explicitly)

- **Three lepton generations = three phases of one particle = the Koide relation**, which predicts the tau mass from the electron and muon to **0.006%.** Status after the gated generations program (full record: `GENERATIONS_PROGRAM.md`): the pattern is exactly **one scale + one angle ε = 2.27° from a cancellation point** — the electron is anomalously *light* (m_e ∝ ε²), an almost purely winding-odd ("helical") state, 99.85% invisible to the mass channel. The interference mechanism **exists in the framework** (the Q-ball binds an internal generation dial with an exact square-law energy), generations-as-excitations is **excluded** (1D exact + 3D numerical), and three whole mechanism classes for the balance are **closed**. The ε sub-program then narrowed the last unknown: topological quantization of the offset is **excluded** (212σ), ε's origin must respect the 120° symmetry (rigidity theorem) and lives in **one interference channel whose pitchfork threshold is what makes the electron light**, and Koide is an **on-shell (pole-mass)** fact. What remains open is a single continuous ratio r ≈ 0.318 — like every absolute number in the framework, it waits on the soliton interior. **[mechanism demonstrated — one ratio open]**
- **A falsifiable precision hook on ε (no mechanism attached, flagged as such):** the dial angle satisfies δ − 120° = **2/9 rad** to within 0.9σ of current data (the known Brannen form) — specifically a **pole-mass** statement (it degrades under short-distance running). A ~10× improvement in the tau mass — feasible at future e⁺e⁻ machines — confirms or kills it sharply. The nearby candidate 1/(8π) is already excluded at 25σ, and the whole class of rational-fraction-of-a-turn values at 212σ. **[watch item, falsifiable]**

## Null / long-term

- **The proton is absolutely stable** (τ_p > 10⁴⁰ yr) — baryon number is topological. Testable at Hyper-Kamiokande. **[prediction, null]**
- **No dark-matter particle** (from #3). **[prediction, null]**

---

**One-line framing:** *TFT's central testable claim is that dark matter and dark energy are one dynamical field — which makes galaxy rotation predict the dark-energy equation of state, a cross-observable link no other framework offers, already matching DESI's w₀ and falsifiable in its wₐ by DESI DR2 / Euclid.*
