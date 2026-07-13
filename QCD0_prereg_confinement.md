# QCD0 Pre-registration — quarks, confinement, and hadron statistics

**Date:** 2026-07-12 (before computing). New quantum-sector front, building on
the charge=winding result, the SPIN arc (linking→statistics), and Vic's
topological-confinement seed.

**The picture under test.** In the U(1) phase field, a "quark" is a source of
winding (a vortex-line endpoint). Two topological facts:
1. **No free end:** a winding line cannot terminate in free space (the winding
   around any loop is conserved along the line) → an isolated quark is
   forbidden; quarks appear only in winding-neutral combinations.
2. **Sine-Gordon confinement:** the Λ(1−cosθ) term (which gave the derived kink
   mass 8√Λ) forbids θ from winding freely — the winding is squeezed into a
   **domain wall** (a kink extended transversely) of finite tension. Pulling
   two quarks apart stretches the wall → **linear confinement**, string tension
   σ = the kink/wall tension ∝ √Λ — the SAME √Λ that sets particle masses.

## Computation

1. **String tension [computed]:** σ = energy of the sine-Gordon kink/wall,
   ∫[½θ′² + Λ(1−cosθ)]dx, for several Λ. Predict σ = 8√Λ (the kink mass),
   verify the √Λ scaling and coefficient.
2. **Confining potential [derived]:** V(L) = σL for a q–q̄ pair connected by
   one wall (linear); contrast with the non-confining Coulomb 1/r of the
   massless-phase (EM) sector.
3. **Hadron statistics [derived, from SPIN arc]:** quarks = odd-self-linking
   fermions ⇒ mesons (q q̄, 2 fermions) = BOSONS, baryons (qqq, 3 fermions) =
   FERMIONS. Check this matches observation.
4. **Confinement scale = mass scale [derived]:** σ ∝ √Λ and M_kink = 8√Λ share
   one scale — the confinement scale and the hadron mass scale are the same √Λ.

## Gate

- **PASS (structural)** = a TFT-native linear confinement mechanism (σ ∝ √Λ,
  computed) with the no-free-end obstruction, and the correct meson=boson /
  baryon=fermion statistics from the linking picture — with the confinement
  scale unified with the mass scale.
- **FAIL** = confinement comes out non-linear/absent, or statistics wrong.

**Honest prior & scope, flagged up front.** PASS on the mechanism expected
(SG domain-wall confinement is established physics; the novelty is tying σ to
the derived kink mass and to the SPIN-arc statistics). What stays OPEN even on
PASS, and must be labeled as such:
- **Fractional charge & color SU(3):** quark charges (±1/3, ±2/3) and the
  3-quark/Z₃ structure need the color group; the U(1) phase field gives integer
  winding only. The 3-strand junction is PROPOSED, not derived — getting Z₃
  needs structure beyond U(1). Flagged, not claimed.
- **The absolute scale Λ (→ Λ_QCD):** an absolute-value floor, like G, |Λ_cc|,
  a₀'s coefficient, η, the generation amplitude, and the Hopf θ.
- **Actual baryon masses:** require solving the junction/knot configuration —
  the open hard problem the spectrum arc always flagged.
No tuning; σ is the parameter-free kink energy; statistics is topology.
