"""E2 -- derive the breaking beta = delta - 120deg (make-or-break stage).

Gate (E0, sanctioned): PASS = a second-order internal-dynamics calculation
whose leading correction to the locked dial angle is FORCED (Z3-combinatoric
/ integer coefficients, no continuous tuning) to equal beta = 0.22223
+- 0.00003 rad. FAIL = coefficients remain free or land elsewhere.
Sources in sanctioned order:
  (a) second-order mixing of n=1 / n=2 internal harmonics via the mode sector
  (b) back-reaction of the bound generation dial on its own locking potential
  (c) quantized misalignment inherited from the winding-even projection axis
Protocol: symbolic derivation FIRST, number SECOND; closed candidate lists;
no numeric interpretation of unforced values.
"""
import json
import numpy as np

def hdr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70)
w3 = np.exp(2j*np.pi/3)
m = np.array([0.51099895, 105.6583755, 1776.86])
v = np.sqrt(m)
c = np.array([v @ np.conj(w3**(n*np.arange(3))) for n in range(3)])/3
M, delta = c[0].real, np.angle(c[1])
A = 2*abs(c[1])/M
beta = delta - 2*np.pi/3
Qobs = m.sum()/v.sum()**2
dQ_budget = abs(Qobs - 2/3)
print(f"target beta = {beta:.6f} rad;  Koide budget |Q-2/3| = {dQ_budget:.2e}")

def minima(V, n_expected=None):
    """all local minima of V on the circle (dense grid + Newton polish)"""
    a = np.linspace(0, 2*np.pi, 200001)[:-1]
    y = V(a)
    idx = np.where((y < np.roll(y, 1)) & (y < np.roll(y, -1)))[0]
    out = []
    for i in idx:
        x = a[i]; h = 1e-6
        for _ in range(60):
            d1 = (V(x+h)-V(x-h))/(2*h); d2 = (V(x+h)-2*V(x)+V(x-h))/h**2
            if d2 <= 0: break
            x -= d1/d2
        out.append(x % (2*np.pi))
    return np.sort(np.array(out))

def koide_of(alphas):
    u = 1 + A*np.cos(alphas)
    return np.sum(u**2)/np.sum(np.abs(u))**2

hdr("E2-1  RIGIDITY THEOREM: what kind of term can move the dial at all")
print("""Symbolic first. The three generations are the three minima of the dial
potential. A perturbation with harmonic number n splits into two cases:
  n = 0 mod 3 (Z3-invariant): shifts all three minima by the SAME angle
     -- a rigid rotation; 120-degree spacing preserved exactly.
  n != 0 mod 3 (Z3-breaking): shifts the minima UNEVENLY -- the spacing
     splits at first order, deforming the exact circulant structure that
     Koide's measured 1e-5 precision certifies.
So beta (a 0.22-rad COMMON rotation) can only come from Z3-invariant
harmonics, and all Z3-breaking content is bounded by the Koide budget.
Numerical verification and the bound:""")
for n_pert, tag in [(1, "n=1"), (2, "n=2")]:
    rows = []
    for eta in (1e-3, 3e-3, 1e-2):
        Vp = lambda a: np.cos(3*(a-delta)) + eta*np.cos(n_pert*a)
        mins = minima(Vp)
        sp = np.diff(np.concatenate([mins, [mins[0]+2*np.pi]]))
        split = np.degrees(np.ptp(sp))
        dQ = abs(koide_of(mins) - koide_of(minima(
            lambda a: np.cos(3*(a-delta)))))
        rows.append((eta, split, dQ))
    # power-law inversion of the Koide budget
    e1, e2 = rows[0], rows[-1]
    p = np.log(e2[2]/e1[2])/np.log(e2[0]/e1[0])
    eta_max = e1[0]*(dQ_budget/e1[2])**(1/p)
    print(f"  {tag}: spacing split {rows[-1][1]:.3f} deg at eta=1e-2 "
          f"(grows ~eta^1); dQ ~ eta^{p:.1f};")
    print(f"       Koide budget forces eta/kappa3 <= {eta_max:.1e}"
          f"  -> CANNOT supply beta = 0.22 rad")

hdr("E2-2  source (b): dial back-reaction -- KILLED by the theorem")
print(f"""Symbolic: the bound mode's energy per state is proportional to
(1 + A cos alpha)^2 = (1 + A^2/2) + 2A cos(alpha) + (A^2/2) cos(2 alpha),
i.e. harmonics n = 1 (coefficient 2A = {2*A:.3f}) and n = 2 (A^2/2 =
{A*A/2:.3f}) -- BOTH Z3-breaking. By E2-1 the back-reaction cannot rotate
the orbit; it can only contaminate the spacing, and the Koide budget
bounds its strength to the 1e-3 level (the same scale as the M2' mode-
misalignment reading of the Koide imperfection -- one consistent story:
ALL Z3-breaking contamination sits at ~1e-3). Source (b): FAIL.""")

hdr("E2-3  the ONLY surviving channel: n=3 with n=6 interference")
print("""Symbolic: phase-locking is automatic if the n=6 harmonic descends from
the square of the n=3 source (cos^2(3a+p3) -> cos(6a+2p3)). Then
  V(a) = kappa3 cos(3a) + kappa6 cos(6a)      (locked phases, r = k6/k3)
  V' = -3 sin(3a) [kappa3 + 4 kappa6 cos(3a)]
Two branches: sin(3a)=0 (the symmetric notches) or cos(3a) = -k3/(4 k6).
The notch destabilizes at r = 1/4 (a pitchfork): beyond it the minima
move off symmetrically, offset 3*beta with cos(3 beta) = 1/(4r).
Numerical verification:""")
for r in (0.20, 0.26, 0.3181, 0.40):
    mins = minima(lambda a: np.cos(3*a) + r*np.cos(6*a))
    fam = "2 mirrored families of 3" if len(mins) == 6 else "1 family of 3"
    if len(mins) == 6:   # families interleave when sorted: A,B,A,B,A,B
        ok = all(np.allclose(np.diff(mins[i::2]), 2*np.pi/3, atol=1e-9)
                 for i in (0, 1))
    else:
        ok = np.allclose(np.diff(mins), 2*np.pi/3, atol=1e-9)
    b_off = np.degrees(np.arccos(min(1, 1/(4*r)))/3) if r > 0.25 else 0.0
    print(f"  r={r:6.4f}: {len(mins)} minima ({fam}); 120-deg spacing "
          f"within each family: {ok};  offset = {b_off:7.4f} deg")
r_needed = 1/(4*np.cos(3*beta))
print(f"""
Reproducing the measured beta = {np.degrees(beta):.4f} deg requires
  r = kappa6/kappa3 = 1/(4 cos 3beta) = {r_needed:.5f}
a CONTINUOUS value. Source (a), the sanctioned second-order calculation:
generating kappa6 from kappa3 at second order (anharmonic self-mixing,
classical or quantum-rotor) gives kappa6/kappa3 = c * kappa3/DeltaE with
c an O(1) combinatoric factor but kappa3/DeltaE a CONTINUOUS dynamical
ratio -- NOT forced by any Z3 counting. No integer structure reaches r.
Per protocol, no numeric interpretation of r = {r_needed:.4f} is offered.
Source (a): FAIL (coefficient not forced).

Consistency note (within the locked model, derived): for r > 1/4 the
pitchfork produces exactly TWO mirrored three-state families with
identical mass spectra -- which is precisely M4's particle/antiparticle
pair (dial delta and -delta). The one channel that CAN produce beta also
reproduces the matter/antimatter dial structure for free.""")

hdr("E2-4  source (c): projection-axis misalignment -- no licensed route")
print("""The only quantized angles a topological axis-misalignment can offer
without dynamics are 2pi-rationals -- E1's class, excluded at 212 sigma.
With dynamics, the angle passes through the same unforced ratio as E2-3.
No forced derivation found; adding new numeric candidate classes is
forbidden by the sanctioned protocol. Source (c): FAIL.""")

hdr("E2 VERDICT vs pre-registered gate:  FAIL  (logged, stop)")
print(f"""No calculation forces beta: (a) unforced ratio, (b) killed by the
rigidity theorem, (c) no licensed route. Characterization gained:
  * RIGIDITY THEOREM [derived]: beta's origin must be Z3-INVARIANT;
    all Z3-breaking content is bounded at ~1e-3 by Koide precision --
    coherent with the M2' misalignment reading (one contamination story).
  * beta lives in exactly ONE channel: n=3/n=6 harmonic interference
    past its pitchfork (r > 1/4), with cos(3 beta) = 1/(4r) -- and that
    channel spontaneously produces the particle/antiparticle mirror
    pair [derived within the model].
  * The entire epsilon mystery is now ONE continuous ratio kappa6/kappa3
    = {r_needed:.4f}, with no mechanism -- sharper than 'one angle': the
    angle now has a NAMED dynamical owner and a threshold (r > 1/4)
    whose crossing is what makes the electron light at all.
Per E0: E3 has no licensed relation to try (beta connects to none of the
closed-list quantities by any derived formula found here); the program's
remaining live item is E4 (scale scoping, needs separate approval) and
the standing 2/9-rad falsifiability anchor.""")

out = dict(
    gate="E2 (E0 sanctioned): PASS=forced coefficient hits beta; FAIL=free",
    verdict="FAIL -- (a) kappa6/kappa3 continuous, not forced; (b) killed "
            "by rigidity theorem (n=1,2 harmonics bounded ~1e-3 by Koide "
            "budget); (c) no licensed route. Stopped per gate.",
    rigidity_theorem="beta must be Z3-invariant in origin; Z3-breaking "
                     "content <= ~1e-3 (Koide budget)",
    surviving_channel=dict(form="V = k3 cos3a + k6 cos6a (phase-locked)",
                           pitchfork="r = k6/k3 = 1/4",
                           offset_law="cos(3 beta) = 1/(4r)",
                           r_needed=float(r_needed),
                           mirror_pair="= M4 particle/antiparticle families"),
    beta_target=float(beta),
)
with open("outputs/E2_breaking.json", "w") as f:
    json.dump(out, f, indent=2)
print("\n[results block written: outputs/E2_breaking.json]")
