# Teotl Field Theory — Computational Demonstrations

Companion code for *⟨paper title⟩* (V. Luna, ⟨year⟩). Each program is a small, self-contained check
that anyone can run in a few seconds.

> **What these are.** Demonstrations and consistency checks — **not proofs.** They show that the
> framework's mechanisms produce the stated behavior, and that it reproduces known physics where it
> should. Each result below is labeled by what it establishes. Nothing here claims uniqueness or
> proves the theory; that is what experiment is for. The framework is **in progress**; this is what
> it does so far.

The whole thing rests on four scales (**E₀, ℓ₀, τ₀, α₀**) and three equations
(**mc² = hf**, *time = the turning of phase*, *force = the slope of the phase*) — see the paper.
These programs exercise those few pieces across five orders of magnitude in scale:
**particle → planet → galaxy → cosmos.**

**New here?** Read [`WHAT_TFT_IS.md`](WHAT_TFT_IS.md) first — a short mathematical reading of what
the framework *is* (one circle-valued phase field, and why so much standard physics turns out to be
its geometry and topology).

**Convocatoria / collaboration.** This project's open call for scientific collaboration — its
philosophical roots, epistemic discipline, open problems, and why its intellectual home is Mexico —
is in [`CONVOCATORIA.md`](CONVOCATORIA.md) (in Spanish). The quantum-sector experiments it describes
(`teotl qc.py`, `teotl chsh.py`, `maxcut tft.py`, `verify derivations.py`, `winding_solver.py`) live
in this repository alongside the demonstrations below — including the CHSH/Bell **negative result**
(the local field saturates S = 2.0000 and does not cross it), reported with the same discipline as
the positives.

## Run it

```bash
pip install numpy
python3 verify_conservative_1d.py      # or any file below — each prints its own result
```

Requirements: Python 3.8+ and NumPy. No other dependencies. Every file is standalone.

## The demonstrations, by scale

Labels: **[derived]** follows from the framework · **[consistency]** reproduces a known result,
not a unique prediction · **[input]** a value the framework does not yet fix.

### A. The substrate and its particles
| file | what it shows | status |
|---|---|---|
| `verify_conservative_1d.py`, `verify_force_law_sign.py` | a particle's rest mass = 8√Λ·E₀ (to 1e-9); it obeys F = Ma | **derived** |
| `verify_breather_1d.py` | a particle as a standing wave — mass entirely in the motion | **derived** (exact in 1D) |
| `verify_oscillon_3d.py`, `verify_qball_3d.py` | a lone phase can't hold a 3-D particle; a conserved charge (Q-ball) can | **derived** (charge-vs-alt. not fully isolated) |

### B. The two forces, from one distinction
| file | what it shows | status |
|---|---|---|
| `verify_goldstone_1r2.py`, `verify_force_sign.py` | electromagnetism: a 1/r² Coulomb force, like charges repel | **derived** |
| `verify_poisson_metric.py`, `verify_gravity_coupling.py` | gravity from energy: universal 1/r attraction; matter and antimatter both fall (cf. CERN ALPHA-g 2023) | **derived**, matches experiment |
| `verify_G_as_rate.py` | Newton's G read as (rate of time)² / density | reframing, not a value |

### C. The classical world
| file | what it shows | status |
|---|---|---|
| `tft_solar_system.py`, `stage3_orbits.py`, `stage5_mercury.py` | a solar system from one calibration: 8 periods to <0.1%, Kepler's third law, Mercury 42.9″/century | **consistency** (closed orbits by-construction; Mercury is the standard GR value, not unique) |

### D. The cosmic scale — galaxies without dark matter
| file | what it shows | status |
|---|---|---|
| `verify_a0_g1.py` … `g5.py` | the galactic acceleration scale α₀ = cH₀/2π — set by the universe's expansion, not fitted | scale **derived**; exact coefficient = the "why now" coincidence problem |
| `milkyway_rotation.py` | Milky Way rotation curve to ~3%, baryons only; tracks the 175-galaxy acceleration relation | **fits** (transition shape model-dependent, as in MOND) |
| `verify_a0_g4.py` | the mass–rotation (Tully–Fisher) exponent = exactly 4 (observed 3.85 ± 0.09) | **derived**, parameter-free |

### E. Matter, fields, and handedness — one topological object
| file | what it shows | status |
|---|---|---|
| `verify_chiral_g1.py`, `verify_chiral_g2.py` | baryon number, magnetism, and chirality are three readings of one topological quantity (winding + linking); their anomaly link is automatic | **linkage derived**; the *size* of the matter–antimatter imbalance is an initial condition |

### F. The three generations and the mass hierarchy
*Full narrative with all gates and verdicts: [`GENERATIONS_PROGRAM.md`](GENERATIONS_PROGRAM.md).
Pre-registrations: `G0_prereg_spectrum.md`, `M0_prereg_mass_interference.md`.*

| file | what it shows | status |
|---|---|---|
| `koide_selfdual_g1.py` … `g5.py` | the Koide relation (predicts the tau mass to 0.006%) reduced to ONE coefficient; symmetry, local-energetic, and collective origins each closed by a pre-registered gate | characterization **derived**; three mechanism classes **excluded** |
| `spectrum_sp1_breathers.py`, `spectrum_sp23_qball_tower.py` | a three-state, equal-charge particle tower **exists** in the framework — but excitation towers are near-degenerate: generations are **not** vibrations of one object (1D exact + 3D numerical) | tower **derived**; lepton pattern **excluded** |
| `mass_m1_cancellation.py` | all three lepton masses = one scale, 120° phases, and ONE angle ε = 2.27° from an exact zero — the **electron is anomalously light** (m_e ∝ ε²), at the near-singular point of the generation matrix | **derived** (exact restatement) |
| `mass_m2_interference.py` | the data forces *real, sign-changing* interference; the framework's Q-ball binds an internal "generation dial" whose energy is exactly the square of a real amplitude — the mechanism exists (A, δ inserted, not derived) | mechanism **demonstrated**; coefficients **open** |
| `mass_m3_epsilon.py` | what sets ε: all polynomial internal energetics to degree 5 excluded (~27,000σ); ε classically unprotected; the 2/9-rad form survives at 0.9σ — falsifiable with a better tau mass | honest **FAIL**: ε remains free |
| `mass_m4_chirality.py` | the cancellation point = a pure winding-reversal-**odd** state (the electron is 99.85% "helical"); couplings are winding *integers* (universal) while masses are *amplitudes* (hierarchical) — exact lepton universality + 3477× mass ratio, simultaneously, as observed | **derived** within the construction; weak-channel link **proposed** |

## A fuller digest

`DERIVED_SUMMARY.md` — a scale-by-scale summary of what is derived, what is reproduced by
construction, and what remains an open input (with each open number named: G, the cosmological
constant, the coincidence problem, the baryon asymmetry).

## The one honest pattern

Across every result: the framework derives **mechanisms and scale-relations** without free
parameters, and carries **one calibration constant per absolute scale**. The remaining absolute
numbers (G, |Λ|, α₀'s exact coefficient, the baryon asymmetry) each reduce to a problem that is
open in *every* framework — not a gap unique to this one.

## From theory to solver to application

The same phase-settling dynamics studied here as physics is also a practical **solver**. When the
field relaxes, it minimizes frustration in a network of cyclic (phase) constraints — which is exactly
a signed MAX-CUT / coupled-oscillator optimization. That solver lives in this repository
(`winding_solver.py`, `maxcut tft.py`, `teotl_math.py`) and benchmarks in the band reported for
oscillator Ising machines (see `CONVOCATORIA.md`).

Its provenance and its uses form one chain:

- **Theory** (this repo) — the winding/phase dynamics *is* the TFT field settling; that is what the
  demonstrations above establish.
- **Solver** — the domain-agnostic core (a `WindingSolver` over a `ConstraintGraph`), validated
  against simulated annealing.
- **Applications** — the solver powers **[Hum](https://github.com/vml520/Hum)**, a privacy-first
  calendar-*coherence* tool (it scores structural tension in recurring commitments), and is
  generalized to other constraint domains (genetics, logistics, protein backbone dihedrals) on Hum's
  `engine/*` branches.

**One honesty rule carries across all three:** the solver is *deterministic oscillator dynamics* —
fully explainable, on-device — never marketed as "AI," and the field **language model (TeotlAGI) is
kept entirely separate** from both the solver and any application. Theory, solver, and product each
keep their own home; this section is the link between them, not a merge of them.

## Cite

If you use this code, please cite the archived release:
`https://doi.org/10.5281/zenodo.⟨ID⟩`

## License

MIT — see [`LICENSE`](LICENSE).
