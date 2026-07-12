"""E4 -- scale scoping (E0, sanctioned separately by Vic): does the
Koide/epsilon structure live at the physical on-shell (pole) masses or at
short-distance running masses?

NOT a gate -- a scoping stage. External inputs beyond PDG poles, declared:
alpha = 1/137.035999 (PDG) and standard one-loop QED mass renormalization
(leptons carry no QCD charge, so one loop IS the leading effect):
  pole -> MSbar at own scale:  mbar(m) = M / (1 + alpha/pi)
  running:  d ln mbar / d ln mu = -gamma,  gamma = 3 alpha / (2 pi)
Key one-loop structure: gamma is the SAME for e, mu, tau, so running all
three to a COMMON scale mu multiplies each by (mu/m_i)^-gamma -- the common
mu^-gamma factor drops out of ratios, leaving m_i -> m_i^(1+gamma) up to a
shared constant. So at one loop (fixed alpha) the common-scale spectrum is
mu-INDEPENDENT: the pole-vs-running comparison is a single, calculable
deformation, not a curve. alpha(mu) running and EW effects enter at the
next order; precision statements below the ~1e-5 level are beyond one loop
and are NOT made.
"""
import json
import numpy as np

def hdr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70)
w3 = np.exp(2j*np.pi/3)
ALPHA = 1/137.035999
gamma = 3*ALPHA/(2*np.pi)

def observables(m):
    v = np.sqrt(m)
    c = np.array([v @ np.conj(w3**(n*np.arange(3))) for n in range(3)])/3
    M, delta = c[0].real, np.angle(c[1])
    A = 2*abs(c[1])/M
    Q = m.sum()/v.sum()**2
    eps = np.arccos(-1/A) - delta
    beta = delta - 2*np.pi/3
    r = 1/(4*np.cos(3*beta))
    return Q, eps, beta, r

m_pole = np.array([0.51099895, 105.6583755, 1776.86])
m_run = m_pole**(1+gamma)          # common-scale MSbar spectrum (one loop),
                                   # shared constants dropped (ratios only)

hdr("E4  pole (on-shell) vs running (common-scale MSbar) -- one loop")
print(f"gamma = 3 alpha/(2 pi) = {gamma:.6f}   "
      f"(common-scale masses ~ m_pole^(1+gamma))")
rows = {}
for tag, m in [("POLE (on-shell)", m_pole), ("MSbar common mu", m_run)]:
    Q, eps, beta, r = observables(m)
    rows[tag] = dict(Q=Q, dQ=abs(Q-2/3), eps_deg=np.degrees(eps),
                     beta=beta, d29=abs(beta-2/9), r=r)
    print(f"\n{tag}:")
    print(f"  Q = {Q:.6f}   |Q - 2/3| = {abs(Q-2/3):.2e}")
    print(f"  eps = {np.degrees(eps):.4f} deg   beta = {beta:.6f} rad"
          f"   |beta - 2/9| = {abs(beta-2/9):.2e}")
    print(f"  r_needed = 1/(4 cos 3beta) = {r:.5f}")

deg = rows["MSbar common mu"]["dQ"]/rows["POLE (on-shell)"]["dQ"]
print(f"""
Degradation factor |Q-2/3|_running / |Q-2/3|_pole = {deg:.0f}x
(and the 2/9 agreement degrades from {rows['POLE (on-shell)']['d29']:.1e}
to {rows['MSbar common mu']['d29']:.1e} rad -- the 2/9 form is a POLE-mass
statement).""")

hdr("E4 SCOPING CONCLUSION (labels strict)")
print(f"""* The Koide/epsilon structure is an ON-SHELL statement [derived at one
  loop]: the exactness lives at the physical pole masses; deforming to
  common-scale running masses degrades |Q - 2/3| by ~{deg:.0f}x, and the
  degradation is scale-independent at this order (a single deformation,
  not a drift). Precision below ~1e-5 (two-loop, EW, alpha-running) is
  beyond this calculation and no claim is made there -- in particular,
  whether the exact optimum sits precisely AT the pole is unresolved.
* Consonance with H-MASS [consistency, not proof]: TFT's reading of mass
  is the energy of the physical, dressed, on-shell object -- exactly the
  quantity in which the interference structure is exact. A short-distance
  Yukawa-parameter origin would have no reason to prefer pole masses; an
  on-shell-object origin has no choice. The scoping points where the
  framework already stood.
* For the epsilon-channel: r_needed moves from {rows['POLE (on-shell)']['r']:.5f} (pole)
  to {rows['MSbar common mu']['r']:.5f} (running) -- any future mechanism for r
  must produce the POLE value; a mechanism natural at short distance
  would need to explain the on-shell preference too.""")

out = dict(
    stage="E4 scoping (E0 sanctioned separately); NOT a gate",
    inputs="PDG poles + alpha=1/137.035999 + one-loop QED (declared)",
    one_loop_structure="common-scale spectrum = m_pole^(1+gamma), "
                       "mu-independent at fixed alpha",
    pole=rows["POLE (on-shell)"], msbar=rows["MSbar common mu"],
    degradation_factor=float(deg),
    conclusion="Koide/epsilon is an ON-SHELL (pole-mass) structure; "
               "consonant with TFT's mass = on-shell field energy; "
               "sub-1e-5 statements beyond one loop, not made",
)
with open("outputs/E4_scale.json", "w") as f:
    json.dump(out, f, indent=2, default=float)
print("\n[results block written: outputs/E4_scale.json]")
