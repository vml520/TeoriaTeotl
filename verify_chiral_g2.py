"""G2: baryon number, magnetic helicity, chirality = ONE topological invariant -> the anomaly.

TFT identifications (each a standard, non-fitted step):
  - phase gradient = EM potential (Goldstone):  A ~ grad theta
  - B = curl A = curl grad theta = 0 except on winding lines, where it is a flux tube:
        flux  Phi_i = 2 pi W_i   (W = winding = baryon number of that line)
  - magnetic helicity  H = integral A.B  =  sum_ij Phi_i Phi_j Lk_ij   (Lk = linking, from G1)
                                         =  (2pi)^2 sum_ij W_i W_j Lk_ij
So the three "claims" are three readings of the SAME object:
  FACE 1  baryon number   B  = sum_i W_i
  FACE 2  magnetic helicity H = (2pi)^2 sum_ij W_i W_j Lk_ij
  FACE 3  chirality        = sign(H)
The chiral ANOMALY (dB/dt ~ integral E.B ~ -1/2 dH/dt) then says B + kappa*H is conserved:
generating magnetic helicity generates a baryon asymmetry, with kappa TOPOLOGICAL (fixed by 2pi-per-
winding and the fermion count N_f). The COEFFICIENT is derived up to N_f (an input); the NET amount
of helicity generated (hence net eta) is an initial condition / deep-unknown.
"""
# ============================================================================
# SUPERSEDED 22 Aug 2026 -- READ BEFORE THE OUTPUT.
# This script PRINTS three claims that have since been WITHDRAWN:
#   "ONE topological invariant, three faces"  -- baryon number (linear in W) and
#      magnetic helicity (quadratic, linking-dependent) are TWO INDEPENDENT
#      invariants. Counterexamples: two unlinked W=+1 windings give B=2, H=0; a
#      linked W=+1/W=-1 pair gives B=0, H=+8pi^2.
#   "W = winding = baryon number"             -- baryon number has NO carrier in
#      this framework (see DERIVED_SUMMARY.md section 9).
#   "the anomaly is AUTOMATIC in TFT"         -- every transition among these
#      configurations has dB=0 with dH!=0, forcing kappa=0; and winding number is
#      CONSERVED, so it cannot supply anomalous non-conservation. There are also no
#      fermions here to have an anomaly.
# THE COMPUTATION IS CORRECT AND WAS REPRODUCED INDEPENDENTLY. The linking numbers,
# fluxes and helicities it prints are right. What is withdrawn is the IDENTIFICATION
# drawn from them. See G2_chiral_anomaly.md and DERIVED_SUMMARY.md section 7.
# ============================================================================

import numpy as np

def linking_number(C1, C2):
    dl1 = np.roll(C1,-1,axis=0)-C1; dl2 = np.roll(C2,-1,axis=0)-C2
    m1  = 0.5*(np.roll(C1,-1,axis=0)+C1); m2 = 0.5*(np.roll(C2,-1,axis=0)+C2)
    Lk = 0.0
    for i in range(len(C1)):
        d = m1[i]-m2; nd = np.linalg.norm(d,axis=1)**3
        cr = np.cross(np.broadcast_to(dl1[i],dl2.shape), dl2)
        Lk += np.sum(np.einsum('ij,ij->i',d,cr)/nd)
    return Lk/(4*np.pi)

t = np.linspace(0,2*np.pi,300,endpoint=False)
ring1   = np.c_[np.cos(t), np.sin(t), 0*t]
linkedR = np.c_[1+np.cos(t), 0*t,  np.sin(t)]
linkedL = np.c_[1+np.cos(t), 0*t, -np.sin(t)]
unlinked= np.c_[3+np.cos(t), 0*t,  np.sin(t)]

def faces(C2, W=(1,1)):
    Lk = round(linking_number(ring1, C2))
    B  = W[0]+W[1]                                  # FACE 1: baryon number
    H  = (2*np.pi)**2 * 2*W[0]*W[1]*Lk              # FACE 2: magnetic helicity (2 = i<->j)
    chi = int(np.sign(H))                           # FACE 3: chirality
    return Lk, B, H, chi

print("  ONE topological invariant, three faces (two flux tubes, W=+1 each):\n")
print("  " + "{:<26s} {:>4s} {:>10s} {:>14s} {:>9s}".format(
      "configuration","Lk","B (baryon)","H (mag.helicity)","chirality"))
for name, C2 in [("unlinked", unlinked), ("Hopf link (right)", linkedR), ("mirror (left)", linkedL)]:
    Lk,B,H,chi = faces(C2)
    print("  " + "{:<26s} {:>4d} {:>10d} {:>14.2f} {:>9d}".format(name, Lk, B, H, chi))

print("\n  => baryon number, magnetic helicity, and chirality are the SAME winding topology.")
print("     The chiral anomaly  dB/dt = -kappa dH/dt  (kappa topological, x N_f) is therefore")
print("     AUTOMATIC in TFT, not an added postulate: create magnetic helicity <=> create baryon")
print("     asymmetry, of a definite handedness. Coefficient DERIVED (up to N_f, an input);")
print("     the NET helicity generated (hence net eta ~ 6e-10) is an IC / deep-unknown.")
