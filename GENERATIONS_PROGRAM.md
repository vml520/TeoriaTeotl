# The Generations Program — where the lepton mass hierarchy stands

*11 July 2026. The complete record of a gated research program on one question:
**why do the electron, muon, and tau have the masses they do?***

Every stage below was run against a pass/fail criterion written down **before**
computing, with no parameter tuning and no criterion adjusted after the fact.
Failures are reported with the same care as passes — several of the most useful
results here are the failures. Labels: **[derived]** follows from the framework
or the data · **[consistency]** reproduces a known result · **[proposed]** a
mechanism named, not forced · **[open]** unexplained · **[excluded]** ruled out.

## The data, restated

Three empirical facts anchor everything:

1. **Koide's relation (1981).** The three lepton masses satisfy
   Q = (Σm)/(Σ√m)² = 0.666661 — within 10⁻⁵ of exactly 2/3. Unexplained for
   four decades. Given only the electron and muon, it predicts the tau mass to
   **0.006%**.
2. **The one-angle form.** All three masses are reproduced exactly by one
   scale, three phases 120° apart, and a single angle:
   √m_k = M(1 + A·cos(δ + 2πk/3)), with A = 1.414201 (≈ √2, the Koide value),
   δ = 132.7328° ± 0.0005°.
3. **The zero.** The function 1 + A·cos(·) has an exact zero at 135°. Nature's
   δ sits **ε = 2.2677° away from it**. The electron's amplitude is a 4%
   whisper because it is 2.27° from perfect cancellation; m_e ∝ ε². **The muon
   and tau are not heavy — the electron is anomalously light.** [derived, M1]

The framework connection: "three generations = three phase states of one
object" (the founding intuition) maps exactly onto this structure.

## Part I — the balance is not forced by symmetry or simple energetics

Three gated attempts to *derive* the Koide balance (scripts
`koide_selfdual_g1.py` … `g5.py`), all pre-registered, all honest failures
that closed entire mechanism classes:

| gate | mechanism class tested | verdict |
|---|---|---|
| G3 | symmetries/dualities of the 3-state ring (Aubry–André type) | **excluded** — the balanced quantity is *central*: no symmetry on the ring can touch it (theorem-grade) |
| G4 | ring-local energetics (Derrick/virial equipartition) | **excluded** — the virial is per-particle ("vertical"); no local potential produces the required split; stationarity only re-finds already-dead corners |
| G5 | collective/zero-mode dynamics (rotor, shared-core exchange) | **excluded/free** — the rotor is exactly blind to the balance; exchange generates the right *operator* but its coefficient stays free |

Net result of Part I: Koide's relation compresses from "three mysterious
masses" to **one unexplained coefficient** — the equality of two couplings in
the object's internal potential. A by-product with independent value:
**generation towers built from rigid-rotor excitation are excluded outright**
(their Q can never exceed 5/9, and their mass ratios cap at 4 vs the observed
16.8). [derived exclusions]

## Part II — generations are not excitations

If the three generations were the same object vibrating in higher modes, their
masses would be rungs of a ladder. Tested twice, independently
(`spectrum_sp1_breathers.py`, `spectrum_sp23_qball_tower.py`; pre-registration
in `G0_prereg_spectrum.md`):

- **1D, exact.** The sine-Gordon quantum breather tower (integrable, exactly
  known): m₂/m₁ ≤ 2 for *every* coupling — the observed 206.8 is unreachable
  by two orders of magnitude. **[excluded, parameter-free]**
- **3D, numerical.** The framework's stable particle (the Q-ball) **does**
  possess a three-state tower at equal conserved charge — the structural
  prerequisite for generations exists **[derived]** — but its mass ratios are
  1.08–1.19: near-degenerate. **[excluded as the lepton pattern]**

Both towers hug Q ≈ 1/3 (the all-equal corner). The leptons sit at Q = 2/3.
**Whatever splits the generations, it is not gentle excitation** — and near a
cancellation point (Part III), enormous ratios cost nothing. The exclusion and
the mechanism fit together.

## Part III — the interference mechanism (the M program)

Pre-registration: `M0_prereg_mass_interference.md`. Hypothesis **H-MASS**: the
hierarchy is near-destructive interference — the electron sits near an exact
zero of a two-component amplitude.

**M1 (`mass_m1_cancellation.py`) — PASS.** The cancellation point is the
**singular point of the generation matrix** (determinant exactly zero, rank 2;
the electron is the near-null direction). At exact cancellation the remaining
mass ratio is forced in closed form: m_τ/m_μ → (2+√3)² = 13.93 (measured:
16.82; the ε offset supplies the difference). One angle controls the whole
hierarchy: μ/e and τ/e scale as 1/ε². [derived, matrix level]

**M2 (`mass_m2_interference.py`) — literal gate FAILED, amended gate
sanctioned.** Full disclosure: the M0 gate formula was mis-specified (a complex
modulus), and the data itself excludes that form — the lepton mass-cosine dips
negative, which no modulus can do (needs amplitude/mean ≤ 1; data: 1.833). The
failure was logged, not patched; the owner sanctioned the corrected gate M2′.
What the data *forces* instead: **real, sign-changing interference** — the
electron sits 2.27° from a genuine sign flip **[derived from data]** — and, by
Cauchy–Schwarz, the two interfering components must share one spatial shape;
the measured 10⁻⁵ imperfection of Koide then reads naturally as a **0.11% mode
misalignment** [proposed]. The construction: the framework's own Q-ball binds
a localized internal mode in its own potential well (eigenvalue 0.608 vs
continuum 1.0) — a "generation dial" that is part of the particle — and for
this mode, energy is *exactly* the square of a real amplitude (nonlinear
corrections < 10⁻⁵ at the lepton amplitudes). Two real contributions into one
mode reproduce 206.77, 16.817, and Q = 0.666661 — **with A and δ inserted, not
derived**. [mechanism demonstrated; coefficients open]

**M3 (`mass_m3_epsilon.py`) — FAIL, honestly.** What sets ε? Derived: the
internal 120° symmetry makes all simple energetics *blind* to the dial angle,
and every polynomial internal energy up to degree 5 would park the dial at a
60° multiple — excluded by 12.73° at ~27,000σ. Richer dynamics select nothing
(free couplings). And ε is **classically unprotected**: m_e shifts ~5% per
milliradian of dial angle. **H-MASS relocates the fine-tuning; it does not yet
remove it.** One precision target survives, with no mechanism attached:
δ − 120° = 2/9 rad, consistent at 0.9σ (the known Brannen form; the tempting
1/(8π) is excluded at 25σ). A ~10× better tau mass makes 2/9 sharply testable.
[open; falsifiable hook]

**M4 (`mass_m4_chirality.py`) — PASS.** In the framework, chirality = winding
direction (derived earlier, `verify_chiral_g*.py`). Writing the dial in the
winding basis: the mass-making channel is the **winding-reversal-EVEN**
projection, and the cancellation point is exactly where the object becomes a
**pure ODD eigenstate of winding reversal**. The electron is **99.85%
winding-odd** — an almost purely helical internal state, nearly invisible to
the mass channel; the tau is 98% even. Three consistency results follow at
machine precision: (i) the antiparticle family (all windings flipped) has an
identical mass spectrum — inherited automatically; (ii) **gauge couplings are
winding integers (quantized → identical across generations) while masses are
amplitudes (continuous → hierarchical)** — predicting exact lepton
universality coexisting with a 3477× mass ratio, which is what is observed;
(iii) the *minimal* dial-locking energy allowed by the 120° symmetry has
exactly **three** notches, always — a proposed origin for why there are three
generations, assembled entirely from derived parts. [derived within M2′;
weak-channel identification proposed]

## The ledger

| statement | label |
|---|---|
| Koide ⟺ one angle ε from the singular point; m_e ∝ ε² | **derived** (exact restatement) |
| the interference is real and sign-changing (not modulus) | **derived from data** |
| a TFT object with the required structure exists (bound internal dial, exact square law) | **derived** (construction) |
| cancellation point = pure winding-reversal-odd state; electron 99.85% odd | **derived** within the construction |
| universality + hierarchy coexistence (couplings topological, masses amplitudes) | **consistency**, matches observation |
| antiparticle spectrum identical | **consistency**, inherited |
| exactly three generations from minimal Z₃ locking | **proposed** |
| the odd channel = the weak interaction's chiral coupling | **proposed** |
| the values of A (≈√2) and δ (equivalently ε = 2.2677°) | **open** — the entire remaining mystery |
| symmetry, local-energetic, collective, and excitation-tower origins | **excluded** (Parts I–II) |

## The one number

Everything unexplained about the lepton spectrum now lives in a single small
angle: **ε = 2.2677° ± 0.0001°** — how far the generation dial sits from
perfect silence. It is measured, it is not protected by any mechanism found
here, and one mechanism-less precision form (2/9 rad) awaits a better tau mass
to be confirmed or killed. Finding what sets ε — with topological quantization
of the dial as the flagged candidate — is the program's open front.

## Reproduce

```bash
pip install numpy
mkdir -p outputs                    # scripts write their JSON results here
python3 mass_m1_cancellation.py     # the zero, the angle, the singular matrix
python3 mass_m2_interference.py     # data theorems + the construction
python3 mass_m3_epsilon.py          # the epsilon exclusions (honest FAIL)
python3 mass_m4_chirality.py        # the winding/chirality structure
python3 spectrum_sp1_breathers.py   # 1D excitation towers excluded (exact)
python3 spectrum_sp23_qball_tower.py  # 3D tower exists; leptons excluded (~min)
python3 koide_selfdual_g3.py        # symmetry class closed
python3 koide_selfdual_g4.py        # local-energetics class closed
python3 koide_selfdual_g5.py        # collective class closed; rotor towers dead
```

Inputs: PDG lepton masses only. Each script prints its own pre-registered gate
and verdict. JSON results land in `outputs/`.
