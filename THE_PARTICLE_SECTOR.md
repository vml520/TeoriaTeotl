# The particle sector — what particles are in TFT, and how far it goes

*12 July 2026. Third companion to [`GENERATIONS_PROGRAM.md`](GENERATIONS_PROGRAM.md)
(lepton masses) and [`WHERE_R_LIVES.md`](WHERE_R_LIVES.md) (the soliton interior).*

The mass program left a loud gap: it modeled the charged leptons as **Q-balls**,
which are **spin-0 bosons** — but electrons are **spin-½ fermions**. So the
Q-ball was only ever the *mass and charge skeleton*. This note fills in the rest
of the particle picture — spin and statistics, the neutrino, parity, and quark
confinement — and draws the honest boundary where a U(1) framework stops.

The through-line: **one topological invariant — the winding-line linking /
helicity, already derived in the baryo/magneto/chirality arc — turns out to
carry spin, statistics, baryon number, and chirality all at once.** Everything
below is a reading of that one fact, plus the sine-Gordon mass and the mass
dial. Labels: **[derived]** · **[computed]** · **[consistency]** ·
**[proposed]** · **[floor]** (an absolute value / non-abelian group the U(1)
field does not fix — open in TFT as it is elsewhere). Pre-registrations:
`SPIN0_`, `NU0_`, `QCD0_`.

## 1. Fermions from linking — spin & statistics (`spin_statistics.py`)

A soliton of a *bosonic* field can be quantized as a fermion
(Finkelstein–Rubinstein) iff a 2π rotation is a non-contractible loop in its
configuration space. A spherical Q-ball's rotation is trivial → **spin-0
boson**. The carrier of fermions in a U(1) phase field is a **twisted,
current-carrying vortex loop** (a vorton / Hopfion), whose **self-linking**
(writhe + twist) sets the rotation sign.

Computed, as parameter-free topology: the Gauss linking integral is quantized
(unlinked rings Lk = 0.000, Hopf link Lk = −1.000 → ±1); the self-linking of a
twisted loop equals its twist = the internal current winding (SL = 0,1,2,3 for
winding 0,1,2,3). Then **odd self-linking → (−1) under 2π rotation → spin-½
fermion; even → boson** [derived]. That self-linking is the *same* winding-line
helicity as baryon number and chirality — **one linking invariant, four
meanings**.

**Resolution [consistency]:** the leptons are not plain Q-balls — the true
lepton is a vorton/Hopfion with *odd* self-linking. The Q-ball gave the mass
and charge; the fermionic nature lives in the loop's linking. (And the electron
being a near-silent winding-*odd* state — why it is light, from the mass dial —
and being a *fermion* are the same topological data.)

## 2. The lepton dial completed — neutrinos & parity (`neutrino_parity.py`)

The mass program (see `GENERATIONS_PROGRAM.md`) put the three charged leptons on
one dial, with the electron light because it is 99.85% **winding-reversal-odd**
(the mass lives in the *even* channel). Push that to its end:

- **The neutrino is the pure-odd limit [derived].** The odd-purity ladder runs
  e 99.85%, μ 84%, τ 2%; its even→0 endpoint is a state that is massless,
  100% winding-odd, and single-chirality — a neutrino. The electron is already
  99.85% of the way there; its 0.15% even content *is* its entire mass. The
  neutrino is not a new object — it is the massless-chiral limit of the *same*
  dial.
- **Parity violation is forced [derived].** The parity-like operation is winding
  reversal (θ→−θ): it fixes the even channel and flips the odd. A coupling to
  the odd (axial) channel is therefore **100% parity-violating** — pure V−A,
  verified as an exact sign flip — matching the weak force's defining property.
  A pure-odd neutrino has one winding sense → one chirality → **no ν_R**.
- **Large PMNS vs small CKM [proposed].** Two states with splitting Δ and a
  common coupling ε mix by tan2θ = 2ε/Δ. Same ε, opposite outcomes: the charged
  leptons are hierarchical (Δ ~ 100–1700 MeV) → mixing ~0.01°, like CKM; the
  neutrinos sit near-degenerate at the cancellation (Δ ~ 0.01 eV) → mixing
  ~20–40°, like PMNS. **Neutrinos are light and maximally-mixing for the same
  reason — they live near the cancellation point.**

This gives the weak force's two TFT-native features — the neutrino and parity —
with no SU(2). The gauge machinery (W/Z, the doublet) is a **[floor]**.

## 3. Quark confinement (`quark_confinement.py`)

A quark is a winding-line endpoint. Two facts:

- **No free end [derived].** A winding line cannot terminate in free space
  (winding is conserved along it) — a lone quark would need a wall to infinity
  = infinite energy. Only winding-neutral combinations are free states.
- **Linear confinement, tension = the kink mass [computed].** The sine-Gordon
  Λ(1−cosθ) term squeezes the winding into a domain wall whose tension is
  σ = ∫[½θ′² + Λ(1−cosθ)]dx = **8√Λ exactly** (verified, √Λ scaling). Pulling
  quarks apart stretches the wall → V(L) = σL, unbounded → confinement, versus
  the massless-phase (EM) sector's Coulomb 1/L → 0.

Two payoffs. **Statistics [consistency]:** quark = odd-linking fermion ⇒ meson
(q q̄) = boson, baryon (qqq) = fermion — as observed, pure linking parity.
**Unification [derived]:** σ = 8√Λ is the *same* 8√Λ as the derived kink rest
mass — **one scale √Λ sets both the hadron mass and the confinement tension**
(Λ_QCD and the hadron mass are the same number, as in real QCD).

Honest: "quarks are wall-endpoints" is the topological-confinement seed made
concrete on the derived kink — a model of what a quark is, not a derivation of
QCD. Fractional charge and color SU(3) are a **[floor]** (the U(1) field gives
integer winding only; the 3-strand/Z₃ junction is [proposed]).

## 4. The mass numbers — an honest terminus (`spec_selfconsistent.py`)

`WHERE_R_LIVES.md` localized the last unexplained lepton-mass number, r ≈ 0.318,
to a two-sector flux and showed it collapses together with the amplitude
A ≈ √2 into one residual. The self-consistent solve settles what that residual
is [derived]: the fully self-induced dial is **flat** (the induced sectors
co-rotate with the dipole — a global rotation), so a non-trivial r requires
*independently-excited* sectors; and A = √2 plus U(1) charge quantization are
only two conditions on three amplitudes — a one-parameter family survives, r
varying along it. **So r (and A) bottom out at the generation-mode excitation
amplitude — an initial-condition-class quantity, the same floor as the baryon
asymmetry η, not a dynamically-derived number.** The mechanism is fully mapped;
the final number is a floor.

## The ledger

| statement | label |
|---|---|
| self-linking is a quantized topological invariant (Hopf link ±1, twist = winding) | **computed** |
| odd self-linking → spin-½ fermion; Q-ball → spin-0 boson | **derived** |
| spin, statistics, baryon number, chirality = one linking invariant | **derived** |
| leptons are vortons/Hopfions (odd linking), not plain Q-balls | **consistency** |
| neutrino = pure winding-odd, massless-chiral limit of the lepton dial | **derived** |
| parity violation forced by chirality = winding (100% V−A, no ν_R) | **derived** |
| large PMNS / small CKM = neutrino near-degeneracy vs charged-lepton hierarchy | **proposed** |
| linear confinement, string tension σ = 8√Λ = the kink mass | **computed** |
| meson = boson, baryon = fermion (linking parity) | **consistency** |
| one scale √Λ sets both hadron mass and confinement tension | **derived** |
| the last mass number r (=A) = an excitation amplitude, an initial condition | **derived** (a floor) |
| absolute scales (ν-mass, Λ_QCD, …); non-abelian groups (SU(2)_L, color SU(3)) | **floor** |

## The boundary, drawn honestly

TFT's particle sector is a U(1) phase field, and it goes exactly as far as a
U(1) field can: it **derives structures, mechanisms, and scale-relations** —
what a particle is (a soliton), why some are fermions (odd linking), why the
electron is light and the neutrino massless and chiral (the mass dial's
cancellation), why parity is violated (chirality = winding), why quarks confine
and why the confinement scale equals the mass scale (the sine-Gordon wall). It
does **not** fix the **absolute scales** (every mass scale, Λ_QCD, the mixing
couplings) or supply the **non-abelian groups** (SU(2)_L for the full weak
interaction, color SU(3) for the full strong one). Those are the named floors —
open in TFT, and mostly open everywhere. The line between the two is where this
note ends.

## Reproduce

```bash
pip install numpy
mkdir -p outputs
python3 spin_statistics.py       # fermions from odd self-linking; Q-ball = boson
python3 neutrino_parity.py       # neutrino = pure-chiral dial limit; parity; mixing
python3 quark_confinement.py     # linear confinement, sigma = 8 sqrt(Lambda) = kink mass
python3 spec_selfconsistent.py   # r/A bottom out at an excitation amplitude (a floor)
```

Inputs: PDG masses and the repo field only. Each script prints its pre-
registered gate and verdict; JSON lands in `outputs/`.
