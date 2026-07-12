# G0 Pre-registration — the SPECTRUM problem (first pass)

**Date:** 2026-07-11 (written BEFORE any spectrum number is computed)
**Question:** Does TFT possess a generation tower — three or more localized
stationary states with the SAME conserved charge and hierarchical masses —
and do its mass ratios reproduce any observed lepton pattern?

**Targets (PDG):** mu/e = 206.768, tau/mu = 16.817, Koide Q_K = 2/3 (0.666661).

## Pre-committed model (no freedom)

The field theory is the repo's own, frozen before this arc existed:
1. **3D sector:** complex field psi = rho e^{i theta}, U(1) potential
   **V(rho) = 1/2 rho^2 − rho^4 + rho^6** — verbatim from
   `verify_qball_3d.py` (4 Jul 2026). Coefficients are NOT adjustable.
   Stationary states: psi = rho(r) e^{i omega t}, window omega in (1/sqrt2, 1).
   Charge Q = omega ∫rho² dV, energy E = ∫[½omega²rho² + ½rho'² + V] dV
   (same conventions as the dynamic script).
2. **1D anchor:** the sine-Gordon quantum spectrum (exact, DHN):
   breather masses M_n = 2M_kink sin(n pi xi / 2), n = 1, ..., < 1/xi.
   TFT-native (kink + breather verified in repo); integrable, parameter = xi only.

**No-tuning clause:** no potential coefficients changed, no level selection
(consecutive states only: n = 1,2,3 in 1D; radial node number n = 0,1,2 in 3D),
no criterion adjusted after seeing results. Code units: only RATIOS are
meaningful; the overall mass scale is not predicted. The equal-charge scan
parameter Q* is ONE continuous dof — matching TWO ratios would remain
overdetermined; matching the single Koide condition is consistent-with at best.

## Stages and gates (pre-committed)

**SP-1 (1D exact tower).** Compute mass ratios and Koide Q_K for the three
lightest breathers over the whole coupling range xi in (0, 1/3].
GATE SP-1: PASS if any xi gives (mu/e AND tau/mu within 5%) or |Q_K−2/3|<0.01;
otherwise EXCLUSION logged (the arc continues — 3D is a different object).

**SP-2 (3D ground-state Q-ball family — solver validation).** Shooting solve
of rho'' + (2/r)rho' = (1−omega²)rho − 4rho³ + 6rho⁵ across the window.
GATE SP-2 (all must hold or the arc STOPS as solver-invalid):
  (a) Derrick virial for 3D stationary states: E_grad = −3W where
      W = ∫[V − ½omega²rho²]dV, satisfied to ≤1% for every kept solution;
  (b) thick-wall limit: E/Q → 1 (within 5%) as omega → 0.98;
  (c) Q(omega) diverges toward both window ends with a minimum between
      (the known structure for this potential class).

**SP-3a (existence of the tower).** Find radially excited states (1 and 2
nodes) across the window. GATE: a common charge range where n = 0, 1, 2 all
exist. If none exists → "no same-charge three-state tower in this potential"
= the finding; STOP.

**SP-3b (the match).** On the common range, scan Q*; masses E_n(Q*) with
E_n = lowest energy on branch n at that charge.
  PASS-strong: some Q* has |E1/E0 / 206.768 − 1| < 0.05 AND
               |E2/E1 / 16.817 − 1| < 0.05  (two conditions, one dof).
  CONSISTENT-WITH: some Q* has |Q_K(Q*) − 2/3| < 0.01 (one condition, one
               dof — weak label, flagged as such).
  Otherwise: EXCLUSION — "generations ≠ radial Q-ball excitations of this
               potential" — logged as TFT's first quantitative spectrum
               statement. Stability labels (dQ/domega sign, E/Q vs 1)
               recorded either way.

**Honest expectation (PROPOSED, recorded up front):** radial excitation
towers generically give O(1–3) mass ratios; 206.8 is likely unreachable and
the expected outcome is EXCLUSION. That outcome is a result, not a failure
of the arc: it would be the first sharp quantitative statement TFT makes
about the particle spectrum, and it directs the search (hierarchy needs a
different mechanism than radial excitation).

**Relation to the closed Koide arc:** Q_K of an actual TFT tower is exactly
the "explicit soliton internals" test the standing criterion demands. If
|Q_K − 2/3| < 0.01 occurs it will be labeled consistent-with (scan dof), and
only a Q*-independent 2/3 would reopen the Koide arc.
