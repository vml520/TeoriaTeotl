# Teotl Field Theory — current status

*One page. What is claimed, what is open, what was withdrawn. Everything here links to
`DERIVED_SUMMARY.md` for the derivation and to a runnable script for the number.*

**Last audited 3 September 2026.**

---

## The theory in a paragraph

Physical reality is a single complex field ψ = ρe^{iθ}. Its **phase** turns on a circle, and **time
is the cycling of that phase** — so mass is a rate, not a substance. The circle is not assumed: it is
the field's vacuum manifold, so compactness is *earned*. From that one premise a large part of
quantum mechanics follows as consequence rather than postulate, gravity appears as the geometry the
field's energy induces, and the dark sectors become aspects of one field. The programme's discipline
is that every claim is gated, and negative results are recorded as prominently as positive ones.

---

## DERIVED — holds independently of how the field is described

These rest only on the low-energy field living on a circle. **Audited 3 Sep 2026: none is
regime-dependent; the teotl-quanta reframing changes none of them.**

| claim | where |
|---|---|
| **Charge quantisation** — integer, from single-valuedness of the phase | §2, §7d |
| **Number–phase uncertainty** ΔN·Δθ ≥ ½ — a theorem, not a postulate | §7d |
| **CHSH closure → 2√2**, and the **Born rule** \|c\|² from envariance | §7d |
| **Spin-statistics** — spin-½ from ℤ₂ self-linking of vortex lines | §7c |
| **Gravity's shape and sign** — 1/r, universal attraction, matter and antimatter alike | §4 |
| **Solar-system reproduction** — Kepler + Mercury's 42.9″, one frozen constant | §5 |
| **a₀ ∝ cH₀ *scaling*** — because the field *is* the dark energy, so Λ cancels | §6 |

---

## OPEN (1) — undetermined constants

Consolidated 1–3 Sep 2026. A dozen previously-declared "floors" reduce to **three numbers**.

| number | what it is | status |
|---|---|---|
| **Λ** ≈ 8.7×10⁻¹²² | the cosmological constant | **shared with all of physics** — not TFT's alone |
| **σ** | the soliton-interior shape | the mass hierarchy and the metric coefficient both reduce to it |
| **Nξ** | the kinetic normalisation | physical but UV-anchored; inert at low energy |

**The cutoff *scale* is not among them** — E₀, ℓ₀, τ₀ follow from measured {ħ, c, G}. What is
undetermined is σ's *value* at that scale, which is the ordinary effective-field-theory situation.

> **⚠ σ's status is contingent on the particle model (noted 4 Sep 2026).** The sextic term whose
> coefficient σ is exists for exactly one reason: **Derrick's theorem**, which forces a *static 3-D
> lump* to carry a stabiliser. That requirement comes from modelling the particle as a **Q-ball /
> amplitude soliton**. Under a particle model of **persistent excitations** — a mode rather than a
> lump — **Derrick never applies, no stabiliser is required, and σ is not a parameter of the theory
> at all.** Study IMPORT0 (4 Sep 2026) found σ is therefore an artefact of a **modelling choice**,
> not a floor the framework itself imposes.
>
> **This is NOT yet a withdrawal.** The corpus still records the amplitude-soliton reading, and which
> particle model TFT actually asserts is unsettled. **Recorded here so the reader knows σ's status
> depends on that open question, and that everything reducing to σ — the mass-hierarchy angle, the
> metric coefficient, the fission window — inherits the same contingency.**

## OPEN (2) — unanswered questions

Distinct from the constants above: these are **not missing numbers but missing physics**, and work
could still close them.

| question | where it stands |
|---|---|
| **Is there an equation of motion for the metric?** | **No.** The metric is *sourced* but not dynamical. Getting one needs covariantisation — which four structures lean against — plus an induced coefficient that is the σ floor. |
| **What carries baryon number?** | **Nothing identified.** Winding was withdrawn as the carrier, and the proton-stability claim went with it. |
| **What does the winding number W do?** | **Unassigned.** It carries a local sector label: no monopole moment, confined, no relics. A proposed T-duality role was withdrawn (3 Sep). |
| **Does the field account for the dark sector?** | **Not fully.** The phase sector cannot clump on cluster scales; the amplitude sector clumps but is not transparent. Neither supplies the observed lensing offset. |
| **What sets the mass hierarchy's angle?** | Structure is exact (√m_k = M(1 + A cos(δ + 2πk/3)) reproduces all three leptons), but the one free angle **reduces to σ**. Degree-6 dynamics can place it; that is a fit, not a derivation. |
| **The particle spectrum** | The least-developed sector: no first-principles masses or couplings. |
| **Is TFT's phase-regime requirement negotiable?** | Unresolved, and it matters — the argument for it is from what other results *need*, **not a theorem**. It decides whether the quanta emulator models the theory or is a separate object sharing a Hamiltonian. |

---

## WITHDRAWN — claimed, then retracted by our own checks

Listed so a reader meets them once, here, rather than discovering them scattered.

| withdrawn claim | why | when |
|---|---|---|
| a₀'s **2π** is derived | the field equation gives cω₀; the 2π is a factor of 6.28 the framework cannot supply | Aug 2026 |
| **charge = winding** | charge is the Noether charge; winding has no monopole moment | Aug 2026 |
| **baryon number = winding** | no carrier; the proton-stability claim went with it | Aug 2026 |
| metric ansatz g_ij = δ_ij(1+\|∇θ\|²/E₀²) | wrong shape (1/r⁴); the weak-field form is what works | Aug 2026 |
| **T-duality** prevents the infinities | a field winds for free; only extended objects stretch | Sep 2026 |
| quanta are **two-state** (fragmentation bound) | true in the charge regime only; TFT's regime is harmonic and stable | Sep 2026 |

---

## CLOSED — do not repeat

| question | verdict |
|---|---|
| SU(2)/SU(3) from one circle | **no** — four independent routes, one wall (added structure required) |
| modified inertia from an action | **no** — four studies; the mechanism is a horizon heuristic |
| the lepton hierarchy from *counting* | **no** — excitation and binding both give ratios that flatten while the data explode |
| compact time **replaces** quantisation | **no** — it fixes the spectrum *within* QM; it does not derive QM |

---

## Where to look

- **`DERIVED_SUMMARY.md`** — every derivation, with the script that computes it.
- **`PREDICTIONS.md`** — the falsifiable edges.
- **`teotl_rotor_qc.py`, `teotl_field_qc.py`** — the quanta emulator (self-test: `python3 teotl_rotor_qc.py`).
  **Note:** it runs in the *charge* regime; TFT proper needs the *phase* regime. It is a working
  emulator, not a model of TFT's regime.
- **`teotl_substrate.py`** — **abandoned, marked at the top of the file.** Kept for the record.
