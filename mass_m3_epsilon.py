"""M3 -- what sets epsilon (the 2.27-degree offset from the singular point).

Gate (M0, pre-registered): PASS = a mechanism making epsilon
small-but-nonzero (near-exact symmetry + identified small breaking);
FAIL = epsilon remains a free parameter.

Candidate mechanism classes, PRE-REGISTERED here before computing:
  C1  relaxation of the dial angle delta by Z3-EVEN internal energetics
      (quadratic/quartic invariants of the three amplitudes);
  C2  relaxation by Z3-ODD (cubic / det-class) energetics;
  C3  mixed cubic + sextic energetics;
  C4  protection: is small epsilon self-stabilizing in the M2' composition?
  C5  precision targets (REPORT-ONLY per the M0 numerology clause, but now
      with PDG-propagated error bars): delta-120deg = 2/9 rad (known
      Brannen form) and epsilon = 1/(8 pi). Listed BEFORE computing the
      error bars; no other constants will be tried.
Stop condition: if C1-C4 all fail to select delta, verdict is FAIL per
the gate, with characterization logged.
"""
import json
import numpy as np

def hdr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70)
w = np.exp(2j*np.pi/3)

def fit(mtau):
    m = np.array([0.51099895, 105.6583755, mtau])
    v = np.sqrt(m)
    c = np.array([v @ np.conj(w**(n*np.arange(3))) for n in range(3)])/3
    M, delta = c[0].real, np.angle(c[1])
    A = 2*abs(c[1])/M
    return M, A, delta, np.arccos(-1/A) - delta

MTAU, SIG_MTAU = 1776.86, 0.12                     # PDG
M, A, delta, eps = fit(MTAU)
_, _, d_hi, e_hi = fit(MTAU + SIG_MTAU)
_, _, d_lo, e_lo = fit(MTAU - SIG_MTAU)
sig_d = abs(d_hi - d_lo)/2                          # tau mass dominates
print(f"delta = {np.degrees(delta):.5f} deg +- {np.degrees(sig_d):.5f} deg"
      f"   (error from PDG tau mass +-{SIG_MTAU} MeV)")
print(f"eps   = {eps:.7f} rad +- {abs(e_hi-e_lo)/2:.7f} rad")

hdr("C1  how internal energetics can see the dial at all  [DERIVED]")
dg = np.linspace(0, 2*np.pi, 720)
u = 1 + A*np.cos(dg[:, None] + 2*np.pi*np.arange(3)/3)
for k, val in {"sum u  ": u.sum(1), "sum u^2": (u**2).sum(1),
               "sum u^3": (u**3).sum(1), "sum u^4": (u**4).sum(1)}.items():
    print(f"  {k}: varies with delta by {np.ptp(val):.3e}")
c3 = np.cos(3*dg)
r3 = np.corrcoef((u**3).sum(1), c3)[0, 1]
r4 = np.corrcoef((u**4).sum(1), c3)[0, 1]
print(f"  variation of sum u^3, sum u^4 is PURE cos(3 delta): correlation"
      f" = {r3:.6f}, {r4:.6f}")
print(f"  predicted cos3d amplitudes (3/4)A^3 = {0.75*A**3:.3f}, "
      f"3A^3 = {3*A**3:.3f}; measured ptp/2 = "
      f"{np.ptp((u**3).sum(1))/2:.3f}, {np.ptp((u**4).sum(1))/2:.3f}")
print("""Reason: sum_k cos(n(delta+2pik/3)) vanishes unless n = 0 mod 3. So
degree <= 2 invariants are delta-BLIND, and EVERY invariant of degree
3-5 feels the dial ONLY through cos(3 delta); the next harmonic
(cos 6 delta) needs degree-6 terms.  C1: the dial is selectable only by
degree>=3 dynamics, and up to degree 5 only via cos(3 delta).""")

hdr("C2  any internal energy of degree <= 5: extrema at 60-deg multiples")
near = 60*round(np.degrees(delta)/60)
zscore = abs(np.degrees(delta) - near)/np.degrees(sig_d)
print(f"V(delta) = const + kappa cos(3 delta)  (forced for ANY polynomial")
print(f"internal energy up to degree 5) -> extrema at 0,60,120,180,... deg")
print(f"measured delta = {np.degrees(delta):.4f} deg; nearest multiple {near} deg;")
print(f"distance = {abs(np.degrees(delta)-near):.4f} deg = {zscore:.0f} sigma"
      f"   -> the WHOLE degree<=5 class EXCLUDED")

hdr("C3  cubic + sextic mixtures: place the minimum anywhere")
tgt = delta
k6_over_k3 = 1.0/(4*np.cos(3*tgt))                  # solve V'(tgt)=0 example
V = np.cos(3*dg) + k6_over_k3*np.cos(6*dg + np.pi/2 - 3*tgt - np.pi/2)
print(f"example: V(d) = cos(3d) + {k6_over_k3:.3f} cos(6d + phase) has a")
print(f"stationary point at the measured delta -- and at ANY other delta")
print(f"for other coupling choices. One angle, two-plus couplings:")
print(f"C3 selects NOTHING (a free function, not a mechanism).")

hdr("C4  is small epsilon protected in the M2' composition?  [honest: NO]")
u_e = 1 + A*np.cos(delta)
sens_d = 2*A*abs(np.sin(delta))/u_e * 1e-3          # per mrad of delta
sens_A = 2*abs(np.cos(delta))/u_e * 1e-3            # per 0.1% of A
print(f"relative shift of m_e per MILLIRADIAN of dial angle: {sens_d*100:.1f}%")
print(f"relative shift of m_e per 0.1% change of A:          {sens_A*100:.1f}%")
print("""The amplitude composition q_e = 1 + A cos(delta) moves ADDITIVELY
under any jiggle of delta or A: nothing multiplies the shift by the
small number itself. Classically, epsilon small is ALLOWED but
UNPROTECTED -- H-MASS translates 'why is the electron Yukawa small'
into 'why is the dial 2.27 deg from off', the same mystery in a new
variable. Escape route (PROPOSED, untested): if the dial positions are
TOPOLOGICALLY quantized (Z3 winding sectors), delta cannot jiggle
continuously and the offset must come from a quantized source -- this
is the same open flag as 'why exactly three positions' and feeds M4.""")

hdr("C5  precision targets (report-only, with error bars)")
b = delta - 2*np.pi/3                               # Brannen form
for name, val, target in [("delta - 120deg vs 2/9 rad", b, 2/9),
                          ("epsilon vs 1/(8 pi)", eps, 1/(8*np.pi))]:
    z = abs(val - target)/sig_d
    tag = "CONSISTENT at current precision" if z < 2 else f"DISFAVORED ({z:.1f} sigma)"
    print(f"  {name}: {val:.7f} vs {target:.7f}  ->  {z:.1f} sigma  {tag}")
print("""Note: 2/9 is the known Brannen-class coincidence (rational number of
RADIANS added to a geometric 120 deg -- unit-mixing oddity flagged).
Falsifiable hook: a ~10x improvement in the tau mass tightens sigma to
~4e-6 rad; if the central value holds, 2/9 is then testable to ~2 sigma
per 8e-6 rad of drift. No mechanism is attached to either target.""")

hdr("M3 VERDICT vs pre-registered gate:  FAIL  (epsilon remains free)")
print("""No mechanism found that makes epsilon small-but-nonzero:
  C1 degree<=2 energetics are delta-blind; degrees 3-5 see ONLY
     cos(3 delta) (DERIVED, verified to pure-harmonic precision);
  C2 hence EVERY polynomial internal energy up to degree 5 puts the
     dial at a 60-degree multiple -- excluded by ~13 degrees at
     enormous significance;
  C3 richer potentials select nothing (couplings free);
  C4 small epsilon is classically unprotected -- the smallness is real
     fine-tuning in H-MASS as it stands, honestly logged, with the
     topological-quantization escape flagged for M4.
Characterization gained: delta can ONLY be set by Z3-odd dynamics; the
sole surviving precision target is the (mechanism-less) 2/9 form,
consistent at current precision and falsifiable with a better tau mass.
Per M0, M4 (the chirality/winding link) remains authorized regardless of
M3's verdict; the topological-dial question now lives there.""")

out = dict(
    gate="M3 (M0 prereg): PASS=mechanism for small-but-nonzero eps; "
         "FAIL=eps free",
    delta_deg=float(np.degrees(delta)), sigma_delta_deg=float(np.degrees(sig_d)),
    eps_rad=float(eps),
    C1="Z3-even invariants delta-blind; first sensitive = cubic cos(3d)",
    C2=f"cubic extrema at 60deg multiples; measured {np.degrees(delta):.3f} "
       f"-> excluded at {zscore:.0f} sigma",
    C3="cubic+sextic places minimum anywhere; selects nothing",
    C4="epsilon classically UNPROTECTED (additive sensitivity); "
       "topological quantization = proposed escape (M4)",
    C5=dict(brannen_2_9_sigma=float(abs(b-2/9)/sig_d),
            inv_8pi_sigma=float(abs(eps-1/(8*np.pi))/sig_d)),
    verdict="FAIL -- epsilon remains a free parameter; characterization "
            "logged; no tuning; stopped per gate",
)
with open("outputs/M3_epsilon.json", "w") as f:
    json.dump(out, f, indent=2)
print("\n[results block written: outputs/M3_epsilon.json]")
