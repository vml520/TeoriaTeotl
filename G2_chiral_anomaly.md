# G2 — The anomaly linkage: one invariant, three faces

> ## ⚠ SUPERSEDED 18 Aug 2026 — the central claim of this note is withdrawn.
> An audit (`bmca0_audit.py`, prereg `BMCA0_prereg.md`) found that **baryon number and magnetic
> helicity are two INDEPENDENT invariants, not one invariant with three faces**, and that **the
> chiral anomaly is neither automatic nor derived here**. The table below is the evidence: **B is
> constant at 2 down the entire column while H sweeps −8π² to +8π².** Every transition between these
> configurations has ΔB = 0 and ΔH ≠ 0, forcing κ = 0 in the claimed ΔB = −κΔH. Structurally,
> winding number is *conserved* under deformation, so it cannot supply anomalous non-conservation;
> and there are **no fermions here** to have an anomaly at all. **The numbers below are correct and
> were reproduced independently — the identifications drawn from them are not.** See
> `DERIVED_SUMMARY.md` §7 for the corrected statement.

*Runnable: `verify_chiral_g2.py`. Result: baryon number, magnetic helicity, and chirality are the same winding topology, so the chiral anomaly is automatic in TFT.*

## The identifications (each standard, non-fitted)
- **A = ∇θ** — the phase gradient is the EM potential (the Goldstone/Stückelberg picture that gave the Coulomb sector).
- **B = ∇×A = ∇×∇θ = 0** except on winding lines, where it is a **flux tube**: flux Φ_i = 2π W_i (W = winding = the baryon number of that line). Winding lines *are* magnetic flux tubes (the superfluid-vortex = flux-tube fact).
- **magnetic helicity H = ∫A·B = Σ_ij Φ_i Φ_j Lk_ij = (2π)² Σ_ij W_i W_j Lk_ij** — the linking of the flux tubes = the G1 chiral invariant.

## One invariant, three faces (measured)
| configuration | Lk | B = ΣW | H = mag. helicity | chirality = sign H |
|---|---|---|---|---|
| unlinked | 0 | 2 | 0 | 0 |
| Hopf link (right) | −1 | 2 | −8π² | −1 |
| mirror (left) | +1 | 2 | +8π² | +1 |

- **Face 1 — baryon number:** ΣW (winding charge).
- **Face 2 — magnetic helicity:** (2π)²ΣWᵢWⱼLkᵢⱼ (flux linking).
- **Face 3 — chirality:** sign of the helicity.
All three are the *same* winding topology.

## The anomaly is automatic
The chiral anomaly dB/dt = −κ dH/dt (⇔ B + κH conserved) says: generate magnetic helicity ⇔ generate a baryon asymmetry of definite handedness. In TFT this is **not a postulate** — baryon number *is* winding charge and magnetic helicity *is* the linking of that same winding, so any process that changes the winding topology changes both together. This is the Vachaspati baryogenesis–magnetogenesis link, here forced by topology.

## Status
- **DERIVED:** the linkage (three claims = one invariant); the anomaly relation; the anomaly **coefficient is topological** (2π-per-winding), up to the fermion count N_f (an input, as in the Standard Model).
- **INPUT / deep-unknown:** the *net* helicity generated — hence the *magnitude* of η ≈ 6×10⁻¹⁰ — is an initial condition (primordial net helicity). Mechanism yes; absolute number no, exactly as G0 pre-flagged.

## What G3/G4 must do
- **G3 (baryogenesis):** a mechanism that generates *net* winding/helicity (the CP-violating or spontaneous step). Its sign may be derivable; its magnitude will be an IC.
- **G4 (magnetogenesis):** show the coherent, helical large-scale field that the net winding carries, and its scaling.
