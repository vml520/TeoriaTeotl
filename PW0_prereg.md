# PW0 Pre-registration — does time emerge from the Teotl phase? (Page–Wootters)

**Date:** 2026-07-17 (before computing). Ontology, not phenomenology: the framework
says "time = phase cycling" and carries (at least) two circles — the **internal
phase S¹** (whose winding = charge) and the **compact-time S¹** — without
establishing they are the same object. This tests whether the internal phase can
serve as a **Page–Wootters clock**, so that a globally *timeless* constraint state
reproduces Schrödinger evolution of the rest when conditioned on the phase-clock —
making "time = phase cycling" precise as *relational time*, and unifying the two S¹s.

**Mechanism under test (stated honestly).** Page–Wootters: a static universe state
|Ψ⟩ obeying a zero-energy constraint (Ĥ_C + Ĥ_S)|Ψ⟩ = 0 (Wheeler–DeWitt-like) with
a clock C entangled with a system S; conditioning S on the clock reading t yields
|ψ_S(t)⟩ that satisfies the Schrödinger equation — time is *relational*, not an
external parameter. The TFT-specific content: the clock is the **S¹ phase** (a
cyclic, finite rotor), so (i) emergent time is **cyclic** and the clock spectrum is
an **energy comb** p_n = 2πn/(dΔt) — the *same* structure as compact time and the
DIS0 comb; (ii) the clock that carries winding (charge) is the clock that carries
time → the two S¹s are one. **Honest limits, flagged up front:** PW is established
physics; this reproduces standard Schrödinger QM exactly → empirically degenerate
(no new observable), consistent with DIS0. "The phase *is* time" stays an
identification, not a forced result. And PW needs the clock bandwidth ≥ the
system's energy spread (the clock must be "larger" than what it times).

## Computation (pre-committed; no tuning)

1. **Timeless constraint → Schrödinger emerges [compute].** Build an S¹ phase-clock
   (dimension d, cyclic shift; energies = comb p_n) and a system Ĥ_S (general
   Hermitian, energies on the comb). Form J = Ĥ_C⊗I + I⊗Ĥ_S **from the Hamiltonians
   alone — no external time**. Find ker(J) (the timeless physical states); take the
   history state for a chosen |ψ_0⟩; verify ‖J|Ψ⟩‖ ≈ 0. Condition on clock time t_j
   and test |ψ_S(t_j)⟩ = e^{−iĤ_S t_j}|ψ_0⟩ (Schrödinger evolution recovered),
   fidelity over all j. Non-circular: the timeless state comes from the constraint;
   Schrödinger is *discovered* inside it.
2. **S¹ signatures [compute].** Show emergent time is **cyclic** (period T=dΔt: the
   conditioned state at j and j+d coincide) and the clock spectrum is a **comb**
   (spacing 2π/(dΔt)) — i.e., the emergent time IS the compact-time S¹.
3. **Finite-clock corrections / classical limit + the DIS0 tie [compute].** For
   generic (off-comb) system energies the constraint is satisfied only approximately;
   the residual mismatch min_n|p_n+E_a| ≤ π/(dΔt) → 0 as the clock (bandwidth d)
   grows. Show the correction scales as the comb spacing ~1/(dΔt) ~ 1/T — the *same*
   1/T suppression as DIS0 (unobservable for a cosmic clock).

## Gate

- **PASS (structural)** = the timeless J=0 phase-clock state reproduces Schrödinger
  evolution on conditioning (fidelity → 1), AND the S¹ signatures hold (cyclic time,
  energy comb) → the internal-phase S¹ can serve as the time clock; the two S¹s are
  one structure; "time = phase cycling" = relational time on the S¹.
- **PARTIAL** = time emergence works only approximately / with a caveat that does not
  cleanly vanish in the large-clock limit, or the cyclic/comb signatures fail to tie
  to compact time.
- **FAIL** = conditioning on the phase-clock does NOT yield Schrödinger evolution
  (the phase cannot serve as time).

**Honest prior: PASS (structural), with a degeneracy floor.** Expectation: the
mechanism works (PW is sound; an S¹ clock reproduces Schrödinger, cyclically, with a
comb spectrum), delivering the ontological payoff — internal-phase S¹ = time S¹,
"time = phase cycling" made precise. But it reproduces standard QM (degenerate, no
distinguishing observable — same lesson as DIS0), the finite-clock correction is
1/T-suppressed (unobservable), and "the phase *is* fundamentally time" remains an
identification, not derived. A conceptual/structural unification, honestly bounded.
No tuning; Hamiltonians and |ψ_0⟩ are inputs, the emergent evolution is read out.
