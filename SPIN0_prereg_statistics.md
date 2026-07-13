# SPIN0 Pre-registration — spin & Fermi statistics from TFT solitons

**Date:** 2026-07-12 (before computing). New quantum-sector front.

**The sharp tension motivating this:** the lepton-mass program modeled the
charged leptons as Q-balls — which are **spin-0 bosons** (spherically symmetric;
a 2π rotation is trivial). But real electrons/muons/taus are **spin-½
fermions**. So the Q-ball is at best the *mass* skeleton; the true lepton
soliton must carry a fermionic topological structure the plain Q-ball lacks.
This asks whether TFT's bosonic phase field can produce fermions at all, and by
what invariant.

**Mechanism under test (Finkelstein–Rubinstein / Hopf):** a soliton of a
bosonic field is quantizable as a fermion iff a 2π spatial rotation is a
NON-contractible loop in its configuration space (π₁ nontrivial, a Z₂ sign).
For a U(1) phase field the natural carrier is a **linked/twisted/knotted vortex
loop** (a vorton / Hopfion): its **self-linking number** (writhe + twist)
controls the rotation sign — ODD self-linking ⇒ the (−1) ⇒ fermion; EVEN ⇒
boson. Claim to test: that self-linking is the SAME invariant as the
winding-line helicity derived in the baryo/magneto/chirality (BMC) arc.

## Computation

1. **Boson baseline:** confirm the spherically-symmetric Q-ball's 2π rotation
   is trivial (self-linking 0) ⇒ spin-0 boson.
2. **Linking is an integer topological invariant [computed]:** evaluate the
   Gauss linking integral Lk = (1/4π)∮∮ (r₁−r₂)·(dr₁×dr₂)/|r₁−r₂|³ for
   unlinked vs linked vortex rings → 0 vs ±1 (quantized).
3. **Self-linking of a twisted loop (the vorton) [computed]:** self-linking =
   writhe + twist (Călugăreanu–White); build a twisted ring, show SL is a
   nonzero integer set by the twist = the internal current winding.
4. **Spin-statistics assignment [derived]:** map SL → rotation sign (−1)^SL →
   boson/fermion; state the spin.

## Gate

- **PASS (structural)** = TFT admits fermionic solitons: a configuration with
  odd self-linking exists, its invariant IS the BMC helicity, and the FR/Hopf
  argument assigns it half-integer spin / Fermi statistics — while the plain
  Q-ball is a boson. (Establishes fermions are AVAILABLE and identifies the
  invariant.)
- **FAIL** = the topology forbids it (all TFT configs have even/zero self-
  linking, or the rotation loop is always contractible).

**Honest prior & scope:** PASS on availability expected (the U(1) vorton/Hopf
mechanism is established physics; the novelty is tying it to the derived BMC
helicity and to the lepton picture). What will remain OPEN even on PASS:
whether TFT *forces* spin-½ for the electron specifically (vs merely allowing
it) depends on the coefficient of the topological/Hopf term — model-dependent
(cf. Witten's N_c in the Skyrme model), an absolute-coefficient floor like G,
Λ, and the generation amplitude. No tuning; linking integrals are parameter-
free topology.
