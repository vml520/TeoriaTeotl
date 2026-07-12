"""M4 -- the weak-force / chirality link (final authorized M-stage).

Gate (M0, pre-registered): PASS = the cancellation point coincides with a
helicity/winding-reversal structure of the TFT object (connecting to the
derived winding-line chirality arc); FAIL = no link found.

Basis: TFT identifications already on file --
  chirality = winding direction        (BMC arc, G1/G2, DERIVED structure)
  antiparticle = opposite winding      (charge arc, DERIVED)
  charge = integer winding, quantized  (charge arc, DERIVED)
The M2' composition: generation-k mode amplitude q_k = 1 + A cos(alpha_k),
alpha_k = delta + 2pi k/3. cos(alpha) = (e^{i alpha} + e^{-i alpha})/2 is
the EQUAL-weight sum of the two internal winding directions: the mass
channel is the winding-reversal-EVEN projection. The odd projection is
A sin(alpha). M4 asks what the cancellation point is in this language.
"""
import json
import numpy as np

def hdr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70)
w = np.exp(2j*np.pi/3)
m = np.array([0.51099895, 105.6583755, 1776.86])
v = np.sqrt(m)
c = np.array([v @ np.conj(w**(n*np.arange(3))) for n in range(3)])/3
M, delta = c[0].real, np.angle(c[1])
A = 2*abs(c[1])/M
alpha = delta + 2*np.pi*np.arange(3)/3
a0 = np.arccos(-1/A)                                # the cancellation angle

hdr("M4-A  the cancellation point in the winding basis  [DERIVED in M2']")
even = 1 + A*np.cos(alpha)                          # mass channel (W-even)
odd  = A*np.sin(alpha)                              # W-odd content
purity = odd**2/(even**2 + odd**2)
print("state    even (mass amp)   odd (W-odd)   odd-purity")
for k, name in enumerate(["e  ", "mu ", "tau"]):
    print(f"  {name}      {even[k]:8.5f}      {odd[k]:8.5f}      {purity[k]*100:6.2f}%")
print(f"\nAT the cancellation angle: even = 1 + A cos = {1+A*np.cos(a0):.2e} (exact 0),"
      f"  odd = {A*np.sin(a0):.4f} (nonzero)")
print("""=> The cancellation point is EXACTLY the dial direction where the
object becomes a PURE ODD EIGENSTATE of winding reversal: the
winding-reversal-even (mass-making) content of core + mode cancels
identically, and only winding-reversal-odd content survives. The
electron, 2.27 deg away, is 99.85% winding-reversal-odd -- an almost
purely 'helical' internal state, nearly invisible to the mass channel.
Mass ordering = even-content ordering (tau is 98% even). This IS a
helicity/winding-reversal structure at the cancellation point.""")

hdr("M4-B  winding reversal = particle <-> antiparticle  [consistency]")
anti = (1 + A*np.cos(-delta + 2*np.pi*np.arange(3)/3))**2
print(f"W maps the family dial delta -> -delta (a REFLECTED family).")
print(f"particle masses^ (norm):  {np.sort((even**2))}")
print(f"antiparticle family:      {np.sort(anti)}")
assert np.allclose(np.sort(even**2), np.sort(anti), rtol=1e-12)
print("""=> identical spectra, exactly: q(alpha) is W-even, so the mirrored
family has the same three masses. Matches the repo-DERIVED result
'antiparticle = opposite winding, IDENTICAL mass' -- H-MASS inherits it
for the whole family automatically.""")

hdr("M4-C  why lepton UNIVERSALITY survives 3477x mass splitting")
print("""A naive 'weak force couples to the odd amplitude' would VIOLATE
lepton universality (odd content differs: 1.04, -1.35, 0.31), and
universality is measured to ~0.1%. The TFT resolution is already on
file: GAUGE couplings are winding NUMBERS -- integers, topologically
quantized, identical for all three dial positions (charge-quantization
arc, DERIVED). MASSES are amplitudes -- continuous, dial-dependent.
So the picture PREDICTS: exact gauge universality across generations
AND hierarchical masses, simultaneously -- which is exactly what is
observed. [consistency, resting on charge = winding DERIVED]""")

hdr("M4-D  the topological dial (M3's escape route, assembled)")
phis = np.array([0.3, 1.1, 2.4])
for p3 in phis:
    mins = np.sort(np.mod(np.array([(np.pi - p3)/3 + 2*np.pi*j/3
                                    for j in range(3)]), 2*np.pi))
    gaps = np.diff(mins)
    assert np.allclose(gaps, 2*np.pi/3, atol=1e-12)
print("""cos(3 alpha + phi3) locking (the MINIMAL dial-sensitive harmonic,
M3-C1 DERIVED) has exactly THREE minima, 120.0000 deg apart, for every
locking phase phi3 (verified above for arbitrary phi3). Assembled
picture [PROPOSED, from derived parts]:
  * the dial is locked by the minimal Z3 harmonic -> exactly three
    discrete positions -> three generations (not two, not four);
  * the three positions are degenerate in DIAL energy, so masses come
    only from the mode amplitude -> the Koide pattern, automatically;
  * delta = the MISALIGNMENT between the locking axis (phi3) and the
    reality/projection axis (the winding-even direction). M3's
    exclusion says these two axes are NOT set by the same physics
    (else delta would sit at a 60-deg multiple). WHY the misalignment
    is 12.73 deg -- equivalently epsilon = 2.27 deg -- remains the one
    unexplained number (M3 verdict unchanged).""")

hdr("M4 VERDICT vs pre-registered gate:  PASS  (with labels)")
print("""The cancellation point coincides with a winding-reversal structure:
it is the dial direction where the object is a pure ODD eigenstate of
winding reversal (even content cancels exactly; verified numerically;
electron = 99.85% odd). Labels, strictly:
  DERIVED (within the M2' composition): zero of mass channel = pure
    W-odd direction; W-invariance of all family masses (= antiparticle
    mass equality, inherited); universality-vs-hierarchy split
    (couplings topological, masses amplitudes).
  RESTING ON: chirality = winding direction (BMC arc), charge =
    winding number (charge arc) -- both previously derived structures.
  PROPOSED: identifying the W-odd channel with the weak interaction's
    chiral coupling; the Z3-locking origin of exactly three states.
  UNCHANGED: epsilon (2.27 deg) unexplained -- M3's FAIL stands.
This is a consistency/structure PASS inside H-MASS, not an independent
confirmation of H-MASS.

M-PROGRAM COMPLETE: M1 PASS, M2' PASS (Vic-sanctioned amendment),
M3 FAIL (epsilon free), M4 PASS. Net: the interference mechanism
exists in TFT, is data-forced in form, links the light electron to a
near-pure helical state, and predicts universality + hierarchy
coexistence. The single number epsilon carries the whole remaining
mystery.""")

out = dict(
    gate="M4 (M0 prereg): cancellation point ~ helicity/winding-reversal "
         "structure",
    verdict="PASS -- cancellation point = pure winding-reversal-ODD "
            "eigenstate direction (even content cancels exactly); "
            "electron 99.85% odd; consistency PASS within M2' composition",
    odd_purity_pct=dict(e=float(purity[0]*100), mu=float(purity[1]*100),
                        tau=float(purity[2]*100)),
    antiparticle_spectrum_identical=True,
    universality="gauge couplings = winding integers (universal); masses "
                 "= amplitudes (hierarchical) -- both as observed",
    z3_locking="cos(3a) minimal harmonic -> exactly 3 positions, 120 deg "
               "apart, any phase [PROPOSED assembly]",
    unresolved="epsilon = 2.27 deg (M3 FAIL stands)",
)
with open("outputs/M4_chirality.json", "w") as f:
    json.dump(out, f, indent=2)
print("\n[results block written: outputs/M4_chirality.json]")
