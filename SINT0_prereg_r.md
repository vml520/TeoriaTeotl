# SINT0 Pre-registration — r from the soliton interior (DRAFT, frontier)

**Date:** 2026-07-12 (drafted BEFORE any SINT computation)

**Question:** compute r = κ₆/κ₃ = 0.31812 — the last unexplained number of the
lepton spectrum — from the actual field configuration of the TFT soliton,
rather than inserting it.

## What r physically is (fixed by the M/E arcs, restated)

The three generations are √m_k = M(1 + A cos(δ + 2πk/3)), k = 0,1,2, at ONE
dial angle δ. E2 showed δ is selected by an effective dial potential
V(δ) = κ₃ cos3δ + κ₆ cos6δ (the only Z₃-invariant harmonics through order 6),
with the observed δ requiring r = κ₆/κ₃ = 1/(4cos3β) = 0.31812 (β = δ−120°).
So **r is a property of V(δ) = the δ-dependence of the composite soliton's
energy.** Deriving r = deriving that energy's first two Z₃ harmonics from the
soliton profile.

Two facts already on file constrain the interior:
- **δ is a gauge-invariant loop quantity** (the phase of the circulant hopping
  β = |β|e^{iδ}, i.e. a flux threading the three-fold structure), NOT a phase
  of any single site. [from G3 circulant + M4 winding]
- **A = 2|β|/M ≈ √2** is itself an interior overlap ratio (hopping/on-site),
  parked open with its own standing criterion.

## Binding inheritance (re-testing forbidden)

- Σm and Σ√m are δ-independent by the Z₃ sum rules (to be verified, then used):
  no mass-sum functional can select δ. r must come from the δ-DEPENDENT part of
  the field energy (gradient + current + potential overlap), not rest masses.
- All prior exclusions stand (symmetry G3, energetics G4/M3, collective G5,
  topological-quantization E1). A is parked; no SINT stage may assume its value
  is derived, but SINT MAY compute A(d) as a by-product and report it.

## Stages and gate

**SINT-1 [structural, expected DERIVED].** Prove the selection obstruction:
δ is a gauge-invariant flux; the mass-sum energies are exactly flat in δ
(Z₃ sum rules); therefore r lives entirely in the field-overlap energy. This
is rigorous regardless of what follows and states precisely why every prior
stage (which used mass-level or symmetry arguments) could not reach r.

**SINT-2 [computed].** From the actual Q-ball profile (ω = 0.78, the M2′
background, re-solved), compute the neighbour relative-phase interaction
W(φ, d) = ∫[2cosφ(∇ρ₁·∇ρ₂ + ω²ρ₁ρ₂) + V(ρ₁²+ρ₂²+2ρ₁ρ₂cosφ) − V(ρ₁²) − V(ρ₂²)]
between two adjacent lumps at separation d, and Fourier-extract its harmonics
w₁, w₂, w₃. This is the irreducible soliton-interior number: the ρ⁴, ρ⁶ terms
of the frozen repo potential V generate up to cos3φ from the overlap. Report
w_n(d) and the by-product A(d) = 2|β(d)|/M(d) — including whether A = √2 is
hit at any separation.

**SINT-3 [computed + verdict].** Map the two-body harmonics to the ring dial
potential V(δ) and form r(d). Then apply the framework's selection principle
(energy stationarity of the composite in the separation/size d) and read r at
the selected configuration.

## Gate (pre-committed, tolerance stated up front)

- **PASS** = the composite's own energy stationarity selects a configuration
  (no free continuous parameter left) at which r = 0.318 within **20%**
  (ansatz-limited tolerance, declared now; STRONG PASS within 8%).
- **FAIL** = r remains a function of an unfixed separation, OR the selected
  configuration gives r outside 20%.

**Honest prior (recorded):** FAIL is the likely outcome — either the additive
ansatz's energy does not uniquely pin d, or the pinned value misses 0.318.
Both are advances: they either (i) show r is computable but the *selection
principle* is the open piece, or (ii) falsify the two-lump-molecule model of
the generations. A PASS would be surprising and must be robust to the ansatz
and to d-grid before it is believed.

## No-numerology / honesty rules (carried from E0)

Symbolic structure first, numbers second. The ansatz (additive two-lump,
frozen background) is stated as an approximation, not hidden. No coefficient is
tuned; ω = 0.78 is inherited from M2′, not chosen here. Every harmonic reported
with its d-dependence. If the map from two-body (harmonics 1,2,3) to ring
(harmonics 3,6) requires an assumption, that assumption is flagged, not buried.
