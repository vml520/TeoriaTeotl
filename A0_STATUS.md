# Where a₀ actually stands (status note, 4 September 2026)

**This note supersedes every earlier statement in this repository about a₀ = cH₀/2π, including the
16 August 2026 correction in `PREDICTIONS.md`, which is now itself understated.**

Several documents here still present **a₀ = cH₀/2π** as *derived* and *parameter-free*. **That claim
is withdrawn.** This note states what survives, what does not, and why.

---

## What was claimed

That TFT *predicts* the MOND acceleration scale, **a₀ = cH₀/2π ≈ 1.1×10⁻¹⁰ m s⁻²**, parameter-free —
"MOND must fit this; TFT predicts it."

## What is withdrawn

**The coefficient. The framework does not supply the 2π.**

Two independent routes were checked (study **TWOPI1**, 26 August 2026), and **both** return the
factor **1**, not 1/2π:

1. **The field equation.** Integrating the linearised static equation ∇²φ − (ω₀/c)²φ = Sδ³(x) inward
   from the decaying asymptotic (200 000 points), the fitted decay length is **1.000000** against the
   **reduced** Compton wavelength c/ω₀, and **0.159155** against the full Compton wavelength 2πc/ω₀.
   **The propagator pole fixes the range to the reduced wavelength.** So the length the dynamics
   actually supply gives **a₀ = cω₀, with no 2π.**

2. **The thermal (Milgrom-style) route.** The vacuum condition T_Unruh = T_deSitter carries 2π on
   *both* sides — k_BT_U = ħa/2πc and k_BT_dS = ħH₀/2π — so the factors **cancel exactly**, giving
   **a = cH₀.** The thermal route does not deliver the 2π either; it delivers **1**.

**Why this is not a harmless convention.** The paper's own test records that **a₀ = cH₀ sits 5.5
scatter-widths from the fitted RAR scale g† and is excluded outright.** Both routes above land on
precisely that excluded value. **The 2π is therefore a 6.28× factor the framework needs in order to
reach the data and cannot presently obtain from its own dynamics.**

The 16 August note framed the 2π as an *absorbable convention applied consistently*. **TWOPI1's
finding is stronger and less comfortable: it is not that the framework fails to force the convention,
but that its dynamics positively deliver the other answer.**

**The one escape has since closed too.** TWOPI1 explicitly left open that a genuine *modified-inertia*
mechanism — a different equation of motion — was not excluded by its gate. Study **INER0** then found
that in TFT field inertia ≡ field stiffness ≡ f², forced by Lorentz invariance, so **"modified
inertia" is the wrong label for TFT: it is committed to modified *gravity*.** That route is not
available.

## What survives

- **The mechanism.** The field being the dark energy, with Λ cancelling so that **a₀ ∝ cH₀** follows
  dynamically, still stands. What is missing is the **O(1) coefficient**, not the proportionality.
- **Priority, correctly assigned.** **Milgrom showed a₀ ∼ cH₀ in 1983.** The proportionality is his;
  TFT's contribution was to claim the coefficient, and that is the part now withdrawn.
- **The empirical work is unaffected.** `verify_a0_sparc_fit.py` (2696 points, 147 galaxies) remains
  a real result: the fitted RAR scale is g† = 1.16×10⁻¹⁰ m s⁻², the relation's tightness is
  reproduced at **0.133 dex**, and the scale is recovered across galaxy mass. **What changes is only
  what may be claimed about where 1.1×10⁻¹⁰ came from.** Empirically the data select a 2π-ish factor
  (2π sits at 0.5 scatter-widths, π at 1.8, no factor at 5.5) — **the data select it; the theory does
  not derive it.**
- **The baryonic Tully–Fisher exponent of 4** is a separate result and is untouched.

## The honest statement, for reuse

> TFT's mechanism gives **a₀ ∝ cH₀**, a proportionality **Milgrom established in 1983**. The
> **coefficient is not derived**: TFT's own field equation and the thermal route both return
> a₀ = cH₀, which is excluded at 5.5 scatter-widths. The value 1/2π that matches observation is
> **selected by the data, not supplied by the theory.**

## Consequence for publication

The Foundations of Physics submission built on this claim was **shelved on 3 September 2026** rather
than submitted, on exactly this ground. It un-shelves only if the coefficient is derived.

*Studies: TWOPI1 (2026-08-26), ADE1 (2026-08-26), INER0, NFREE0. Internal records: `RESULTS.md`,
`TFT-Classical-Master-Handoff.md`.*
