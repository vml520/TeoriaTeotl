# Appendix: Computational Demonstrations

*Companion code for ⟨paper title⟩ (V. Luna, ⟨year⟩). Each program is standalone (Python 3 + NumPy), prints its own result, and runs in seconds.*

> **What these are.** Demonstrations and consistency checks — **not proofs.** Labels: **[derived]** follows from the framework · **[consistency]** reproduces known physics, not a unique prediction · **[input]** a value the framework does not fix · **[open]** attempted, not solved. Nothing here claims uniqueness or proves the theory; that is what experiment is for. The framework is **in progress** — this is what it does so far. Together the programs span **five orders of magnitude — particle → planet → galaxy → cosmos — from one field and one set of equations.**

**Repository:** `https://github.com/vml520/TeoriaTeotl` · **Archived (cite this):** `https://doi.org/10.5281/zenodo.⟨ID⟩`

---

## A. The substrate and its particles
| file | what it shows | status |
|---|---|---|
| `verify_conservative_1d.py`, `verify_force_law_sign.py` | a particle's rest mass = 8√Λ·E₀ (to 1 part in 10⁹) and it obeys F = Ma — mass and force from the field, not inserted | **[derived]** |
| `verify_breather_1d.py` | a particle as a standing wave: localized, time-periodic, mass entirely in the motion | **[derived]** |
| `verify_oscillon_3d.py`, `verify_qball_3d.py` | a lone phase can't hold a 3-D particle (it radiates); a conserved charge (Q-ball) can | **[derived]** |

## B. The two forces, from one distinction
| file | what it shows | status |
|---|---|---|
| `verify_goldstone_1r2.py`, `verify_force_sign.py` | electromagnetism: a 1/r² Coulomb force, like charges repel (from the field's charge current) | **[derived]** |
| `verify_poisson_metric.py` | gravity: energy density sources a 1/r potential (Poisson), so every mass attracts | **[derived]** |
| `verify_gravity_coupling.py` | matter and antimatter carry opposite charge but identical energy → both fall the same way | **[derived — matches CERN ALPHA-g 2023]** |
| `verify_G_as_rate.py` | Newton's G read as (rate of time)² / density | [reframing, not a value] |

## C. The classical world
| file | what it shows | status |
|---|---|---|
| `tft_solar_system.py`, `stage3_orbits.py`, `stage5_mercury.py` | a solar system from one calibration: 8 planetary periods to <0.1%, Kepler's third law, Mercury's 42.9″/century | **[consistency]** — closed orbits are by-construction; Mercury is the standard relativistic value, not unique |

## D. Galaxies without dark matter
| file | what it shows | status |
|---|---|---|
| `verify_a0_g1.py`…`g3.py` | the galactic acceleration scale α₀ = cH₀/2π ≈ 1.1×10⁻¹⁰ m/s², set by the cosmic expansion — not fitted | scale **[derived]**; exact coefficient = the coincidence problem |
| `verify_a0_g4.py`, `milkyway_rotation.py` | modified inertia → deep-MOND limit; Milky Way curve to ~3% (baryons only); **Tully–Fisher exponent exactly 4** (obs 3.85±0.09) | mechanism + slope-4 **[derived]**; interpolation shape [open] |
| `verify_a0_g5.py` | TFT's law tracks the 175-galaxy SPARC acceleration relation within its scatter | **[consistency with SPARC]** |

## E. Dark energy — and the paper's central prediction
| file | what it shows | status |
|---|---|---|
| `verify_dark_sectors.py` | dark matter and dark energy are one field: the galactic scale = the dark-energy scale (three independent numbers within ~1.8×) | **[derived]** |
| `verify_dynamical_de.py` | dark energy is dynamical (thawing quintessence): w rises from −1 to **w₀ = −0.88** today — matches DESI 2024's signature and w₀ | signature + w₀ **[derived]**; wₐ testable |
| `verify_a0_de_consistency.py` | **⭐ the field fixed by galaxy rotation *predicts* the dark-energy w₀ (= −0.83, matches DESI), and forecasts wₐ ≈ −0.2 to −0.3** — a cross-observable link no other framework makes | **[prediction]** — w₀ confirmed; wₐ a ~1.7σ tension, falsifiable by DESI DR2 / Euclid |

## F. Matter, fields, and handedness — one topological object
| file | what it shows | status |
|---|---|---|
| `verify_chiral_g1.py`, `verify_chiral_g2.py` | baryon number, magnetic helicity, and chirality are three readings of one topological quantity (winding + linking) — so their anomaly link is automatic, and primordial fields must be helical | linkage **[derived]**; the *size* of the matter–antimatter asymmetry is an [input] |

## G. Quantum sector — particle properties from field dynamics
| file | what it shows | status |
|---|---|---|
| `verify_charge_quantization.py` | 'charge' is the winding number of the field — an exact integer by topology; mass is field energy; antiparticle = opposite winding, identical mass. Properties are configurations, not intrinsic labels | principle **[derived]**; the particle *spectrum* is [open] |
| `verify_koide_generations.py`, `verify_koide_sqrt2.py` | three generations as three phases 120° apart = the **Koide relation**, which predicts the tau mass from the electron and muon to **0.006%**; its coefficient reduces to a 45° self-duality of the mass vector | **[consistency, not derived]** — Koide is empirical; TFT *expresses* it |
| `verify_selfdual_attempt.py` | attempt to derive that self-duality: the condition is pinned exactly, and the obvious principle (equipartition) is ruled out | **[open]** — not derived; a well-posed target |

---

**Reproducing these.** Each file is self-contained (Python 3.8+, NumPy only) and prints its result on `python3 <file>.py`. A referee can check any single claim in seconds.

**What is *not* claimed.** Uniqueness; the absolute constants (Newton's G, the cosmological constant, the exact a₀ coefficient, the baryon asymmetry, the lepton masses); or that any of this proves the theory. The recurring, honest pattern: **the framework derives mechanisms and scale-relations without free parameters, and carries one calibration constant (or one open number) per absolute scale — and every such open number is a problem that is open in *every* framework, not a gap unique to this one.**
