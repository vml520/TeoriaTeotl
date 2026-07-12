import json
import numpy as np

def hdr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70)
rng = np.random.default_rng(1)

# ---------------------------------------------------------------------
# G5 GATE (pre-registered in RESULTS.md 2026-07-11, BEFORE this run):
#   Lead: derive the democratic (tr Phi)^2 term from TFT collective
#   dynamics. The (1,1,1) direction is the ring's ZERO MODE (rigid
#   phase rotation of the 3-state object); integrating out / quantizing
#   the collective coordinate is the natural TFT source of a
#   trace-squared term.
#   PASS = the collective-mode calculation produces the democratic pair
#          with coupling ratio a = 2/3 (equivalently forces
#          (tr Phi)^2 = (3/2) tr Phi^2) with NO tuning.
#   FAIL = a remains free.
# ---------------------------------------------------------------------

m = np.array([0.51099895, 105.6583755, 1776.86])   # e, mu, tau (MeV, PDG)
v = np.sqrt(m)
Q = m.sum()/v.sum()**2
w = np.exp(2j*np.pi/3)
c = np.array([v @ np.conj(w**(n*np.arange(3))) for n in range(3)])/3
M, b = c[0].real, abs(c[1])
T = 3*M**2 + 6*b**2                                # tr Phi^2  (total power)
s2, o2 = 3*M**2, 6*b**2                            # singlet / octet power
print(f"Lepton point: trPhi^2 = {T:.4f}, singlet s^2 = {s2:.4f}, "
      f"octet o^2 = {o2:.4f}, Q = {Q:.6f}")
print("Koide <=> o^2 = s^2  <=>  Q = (s^2+o^2)/(3 s^2) = 2/3")

hdr("G5-A  quantizing the U(1) zero mode: the rotor is BLIND to Koide")

print("""Rigid rotation of the 3-state object: psi_k = v_k e^{i(theta_k+alpha)}.
Kinetic energy of the zero mode alpha:  (1/2) I alpha_dot^2  with
  I = sum_k v_k^2 = tr Phi^2      (exact -- U(1) inertia = total power).
Quantization (alpha periodic) -> winding n in Z ->
  E_rot = n^2 / (2 tr Phi^2).
E_rot is a function of tr Phi^2 ONLY. Demonstration -- three profiles
with the SAME tr Phi^2 but wildly different Q:""")
for tag, r in [("Q=1/3 (b=0)      ", 0.0), ("Q=2/3 (leptons)  ", 1.0),
               ("Q=0.95           ", 3*0.95-1)]:
    s2i = T/(1+r); o2i = T-s2i
    Erot = 1.0/(2*(s2i+o2i))
    print(f"  {tag}: s^2={s2i:9.3f} o^2={o2i:9.3f}  "
          f"E_rot(n=1) = {Erot:.8f}")
print("""=> identical rotor energy across the whole Q range. Koide constrains
the RATIO (tr Phi)^2 / tr Phi^2; the rotor term knows only the
denominator. The named mechanism does not just fail to fix a -- it
DECOUPLES from the Koide direction exactly.  KILL 1.
(Adding E_rot = f(trPhi^2) to any potential V(s,o) changes stationarity
to V_s/s = V_o/o, which forces s=o ONLY if the couplings are s<->o
symmetric -- i.e. only if the self-duality is already assumed. And G3
proved the singlet direction is CENTRAL: no ring transformation exists
to protect that coupling symmetry.)""")

hdr("G5-B  generations AS rotor levels: quantitatively EXCLUDED")

x = np.logspace(-4, 8, 400001)                     # x = c/m0, tower m0 + c n^2
Qtow = (3+5*x)/(1+np.sqrt(1+x)+np.sqrt(1+4*x))**2  # |n| = 0,1,2 consecutive
supQ = Qtow.max()
print(f"Minimal tower m_n = m0 + c n^2, |n| = 0,1,2 (no level choices):")
print(f"  sup over all m0,c of Q = {supQ:.6f}  ->  5/9 = {5/9:.6f} < 2/3")
assert supQ < 2/3 - 0.05, "tower reached 2/3?! -- ABORT"
print(f"  hierarchy bound: m2/m1 = (1+4x)/(1+x) <= 4;  "
      f"observed m_tau/m_mu = {m[2]/m[1]:.2f}")
print(f"  (and |n| = 0,+1,-1 gives m_mu = m_tau, degenerate: ruled out)")
print("""=> The rigid-rotor generation tower can NEVER reach Q=2/3 (sup 5/9)
AND violates the tau/mu hierarchy by 4x. Two independent kills.
Non-consecutive level choices (|n|=0,1,4,...) would be discrete tuning
-- excluded by pre-commitment.  KILL 2.
(Scope: this kills 'generations = rotor excitations of one soliton',
NOT 'generations = three phase states' -- the circulant picture that
predicts m_tau to 0.006% stands.)""")

hdr("G5-C  shared-core exchange: democratic OPERATOR yes, coefficient FREE")

# Exact Gaussian integration of a shared core mode chi coupled to all
# three states equally (they are states of ONE soliton):
#   V(chi) = (w2/2) chi^2 - g chi sum_k v_k
#   -> V_eff = -g^2 (sum v)^2 / (2 w2) = -(3 g^2/2 w2) * s^2
g, w2 = 0.7, 2.3                                   # arbitrary demo values
chi = np.linspace(-100, 100, 2000001)
Vmin = np.min(0.5*w2*chi**2 - g*chi*v.sum())
assert abs(Vmin - (-g**2*v.sum()**2/(2*w2))) < 1e-4
print(f"integrate out shared core chi:  V_eff = -g^2 (tr Phi)^2 / (2 w^2)")
print(f"  numeric check: {Vmin:.4f} = {-g**2*v.sum()**2/(2*w2):.4f}")
print("""=> a genuine DEMOCRATIC (tr Phi)^2 term appears -- the only collective
structure found that produces the operator Koide needs. Its coefficient
is g^2/(2 w^2): set by the core stiffness and coupling, i.e. by the full
soliton internals. Is a = 2/3 selected? Scan the general singlet/octet
potential  V = mu1 s^2/2 + mu2 o^2/2 + l1 s^4/4 + l2 o^4/4 + l12 s^2o^2/2
(the democratic term shifts mu1) over its coupling space:""")

n_try, kept, qs = 200000, 0, []
mu = -rng.uniform(0.2, 3.0, (n_try, 2))
l1, l2 = rng.uniform(0.2, 3.0, n_try), rng.uniform(0.2, 3.0, n_try)
l12 = rng.uniform(-1.0, 1.0, n_try)
for i in range(n_try):
    det = l1[i]*l2[i] - l12[i]**2
    if det <= 0:  continue                          # quartic must be PD
    s2i = (-mu[i,0]*l2[i] + mu[i,1]*l12[i]) / det
    o2i = (-mu[i,1]*l1[i] + mu[i,0]*l12[i]) / det
    if s2i <= 0 or o2i <= 0:  continue              # both must condense
    kept += 1
    qs.append((s2i+o2i)/(3*s2i))
qs = np.array(qs)
frac = np.mean(np.abs(qs-2/3) < 0.01*2/3)
print(f"  {kept} valid minima:  Q ranges {qs.min():.3f} .. {qs.max():.3f}"
      f"  (median {np.median(qs):.3f})")
print(f"  fraction within 1% of 2/3: {frac:.4f}  -- nothing selects it")

# the one configuration that DOES pin 2/3: s<->o symmetric couplings
det = 1.5*1.5 - 0.3**2
s2s = (0.8*1.5 - 0.8*0.3)/det; o2s = (0.8*1.5 - 0.8*0.3)/det
Qs = (s2s+o2s)/(3*s2s)
assert abs(Qs - 2/3) < 1e-12
print(f"  symmetric couplings (mu1=mu2, l1=l2): Q = {Qs:.12f} = 2/3 exactly")
print("""=> Q at the minimum sweeps CONTINUOUSLY with the coupling ratios;
a = 2/3 is a codimension-1 surface reached exactly when the couplings
are singlet<->octet SYMMETRIC -- which is the self-duality itself,
re-imposed one level up. The collective mode generates the operator
but the coefficient traces back to the unsolved soliton interior.
Per the gate's own words: a remains FREE.  KILL 3.""")

hdr("G5 VERDICT against the pre-registered gate:  FAIL  (logged, stop)")
print("""* The U(1) zero-mode rotor couples to tr Phi^2 only -- exactly blind
  to the Koide ratio (KILL 1).
* Generations-as-rotor-levels is quantitatively excluded: sup Q = 5/9
  < 2/3 and tau/mu <= 4 vs observed 16.8 (KILL 2 -- a falsifiable
  negative worth keeping: any excitation-tower model of generations
  must be non-rotor).
* Shared-core exchange generates the democratic (tr Phi)^2 operator
  naturally, but its coefficient is set by the soliton interior and
  the scan shows Q sweeps continuously; 2/3 = symmetric couplings =
  the self-duality re-imposed by hand (KILL 3).

ARC CLOSURE (G1-G5, honest endpoint):
  G3 closed symmetries/dualities (singlet is central -- theorem-grade).
  G4 closed ring-local energetics (no local potential gives the split).
  G5 closed collective/zero-mode dynamics (blind, excluded, or free).
  What Koide IS, in TFT terms, after this arc: the statement that the
  internal potential's singlet and octet couplings are EQUAL -- one
  coefficient, protected by no symmetry, selected by no local or
  collective mechanism found here. Deriving it requires the full
  nonlinear 3-state soliton solution: the already-flagged open
  spectrum problem ('the wall'). No cheaper route was found in three
  gated attempts. No new gate is pre-registered -- the honest next
  step on Koide IS the spectrum problem, not another shortcut.
  Standing acceptance criterion for any future claim: derive the
  singlet=octet coupling equality (a = 2/3) from explicit soliton
  internals, with no tuning.""")

out = dict(
    gate="G5 pre-registered 2026-07-11: PASS=collective mode yields "
         "democratic coupling a=2/3 no tuning; FAIL=a remains free",
    verdict="FAIL -- rotor blind (couples to trPhi^2 only); rotor-tower "
            "generations excluded (supQ=5/9, tau/mu<=4); shared-core "
            "exchange gives the operator but coefficient free (Q sweeps "
            "continuously; 2/3 = symmetric couplings = self-duality "
            "re-imposed). No tuning. Stopped per gate. ARC CLOSED.",
    rotor="E_rot = n^2/(2 trPhi^2), function of trPhi^2 only",
    tower_supQ=float(supQ), tower_hierarchy_bound=4.0,
    observed_tau_over_mu=float(m[2]/m[1]),
    scan=dict(n_valid=int(kept), Q_min=float(qs.min()),
              Q_max=float(qs.max()), Q_median=float(np.median(qs)),
              frac_within_1pct_of_koide=float(frac)),
    arc_closure="Koide in TFT = singlet/octet coupling equality; only "
                "remaining route = full 3-state soliton solution (open "
                "spectrum problem). Standing criterion: derive a=2/3 "
                "from soliton internals, no tuning.",
)
with open("outputs/G5_koide_collective.json", "w") as f:
    json.dump(out, f, indent=2, default=float)
print("\n[results block written: outputs/G5_koide_collective.json]")
