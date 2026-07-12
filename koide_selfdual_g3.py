import json
import numpy as np

def hdr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70)
SQRT2 = np.sqrt(2)
rng = np.random.default_rng(0)

# ---------------------------------------------------------------------
# G3 GATE (pre-registered in RESULTS.md 2026-07-07, BEFORE this run):
#   PASS = a TFT reason the generation ring sits at self-duality
#          (symmetry or energetic fixed point), forcing sqrt2, no tuning.
#   FAIL = self-duality must still be imposed by hand.
# Named lead: sqrt-mass matrix = Hermitian circulant (on-site M,
# hopping beta); Q=2/3 <=> 2|beta|^2 = M^2 <=> diag Frobenius weight =
# off-diag Frobenius weight <=> "Aubry-Andre/Harper self-dual point".
# This script (a) verifies the circulant reframe exactly, then
# (b) makes the AA duality precise on the 3-ring and tests the claim.
# ---------------------------------------------------------------------

m = np.array([0.51099895, 105.6583755, 1776.86])   # e, mu, tau (MeV, PDG)
v = np.sqrt(m)
Q = m.sum()/v.sum()**2
w = np.exp(2j*np.pi/3)
n3 = np.arange(3)
S = np.roll(np.eye(3), 1, axis=0)                  # shift on the ring, S|n> = |n+1>

hdr("G3-A  sqrt-mass matrix as Hermitian circulant on the 3-site ring")

# Fourier coefficients of v on Z_3:  v_k = sum_n c_n w^{nk}
c = np.array([v @ np.conj(w**(n*n3)) for n in range(3)])/3
assert abs(c[2]-np.conj(c[1])) < 1e-12             # reality of v ties c_2 = conj(c_1)
M, beta = c[0].real, c[1]
delta = np.degrees(np.angle(beta))

C = M*np.eye(3) + beta*S + np.conj(beta)*S.T       # the circulant sqrt-mass matrix
lam = np.linalg.eigvalsh(C)
err = np.max(np.abs(np.sort(lam)-np.sort(v)))
assert err < 1e-9, "circulant eigenvalues != sqrt masses -- ABORT"
print(f"C = M*I + beta*S + conj(beta)*S^T   (on-site M, hopping beta)")
print(f"  M = {M:.5f}   |beta| = {abs(beta):.5f}   delta = {delta:.3f} deg")
print(f"  eigenvalues(C) reproduce sqrt(m_e,mu,tau) exactly (max err {err:.1e})")
print(f"  Koide amplitude A = 2|beta|/M = {2*abs(beta)/M:.6f}   (sqrt2 = {SQRT2:.6f})")

frob_diag, frob_off = 3*M**2, 6*abs(beta)**2
ratio = 2*abs(beta)**2/M**2
print(f"\nFrobenius weights:  diagonal 3M^2 = {frob_diag:.4f}"
      f"   off-diag 6|beta|^2 = {frob_off:.4f}")
print(f"self-dual ratio 2|beta|^2/M^2 = {ratio:.6f}   (= 3Q-1 = {3*Q-1:.6f})")
assert abs(ratio-1) < 1e-4, "leptons not at the balance point -- ABORT"
print("=> reframe VERIFIED (5 sig figs): Koide <=> on-site^2 = 2 x hopping^2")
print("   equivalently: eigenvalue variance = eigenvalue mean^2 "
      f"({np.sum((v-M)**2):.4f} = {3*M**2:.4f})")

hdr("G3-B  the Aubry-Andre duality, made EXACT on the 3-site ring")

F = w**np.outer(n3, n3)/np.sqrt(3)                 # DFT unitary on Z_3
Cd = F @ C @ F.conj().T
offd = Cd - np.diag(np.diag(Cd))
print("Duality = conjugation by the DFT unitary F (position <-> Fourier).")
print(f"F C F^dag is DIAGONAL (max off-diag {np.max(np.abs(offd)):.1e}):")
print(f"  diag = M + 2|beta|cos(2pi k/3 + delta)  ->  "
      f"{np.round(np.real(np.diag(Cd)),4)}")
print("""So the duality maps:
  hopping beta            ->  diagonal MODULATION of amplitude 2|beta|
  uniform on-site M (DC)  ->  uniform on-site M   (M*I is INVARIANT: central)""")

# The full AA family on the ring:  H = M0*I + t(S+S^T) + V diag(cos(2pi n/3 + phi))
def aa(M0, t, V, phi):
    return (M0*np.eye(3) + t*(S+S.T) + V*np.diag(np.cos(2*np.pi*n3/3+phi)))

def decompose(H):
    """-> (uniform diag M0', modulation amplitude V', hopping magnitude t')"""
    d = np.real(np.diag(H))
    M0p = d.mean()
    Vp = np.sqrt(np.sum((d-M0p)**2)/1.5)           # sum cos^2 over Z_3 = 3/2
    hop = np.abs(H[1,0]), np.abs(H[2,1]), np.abs(H[0,2])
    assert np.ptp(hop) < 1e-10                     # ring-uniform hopping
    return M0p, Vp, hop[0]

M0, t, V, phi = 5.0, 1.3, 3.1, 0.7                 # generic point, nothing tuned
Hd = F @ aa(M0, t, V, phi) @ F.conj().T
M0p, Vp, tp = decompose(Hd)
print(f"General AA family under F:  (M0,t,V)=({M0},{t},{V})  ->  "
      f"(M0',t',V')=({M0p:.4f},{tp:.4f},{Vp:.4f})")
assert abs(M0p-M0)<1e-10 and abs(tp-V/2)<1e-10 and abs(Vp-2*t)<1e-10
print("=> duality swap:  t <-> V/2 ,  M0 -> M0.   Self-dual: V = 2t  (Harper).")
print(f"   Frobenius check: modulation weight (3/2)V^2 = hopping weight 6t^2")
print(f"   <=> V = 2t  -- so 'equal Frobenius weight' IS AA self-duality, but")
print(f"   between MODULATION and HOPPING, not between DC and hopping.")

print("""
Where the Koide matrix sits in this family:  (t, V) = (|beta|, 0).
Its dual is (t', V') = (0, 2|beta|)  --  a DIFFERENT family member.
The AA self-dual condition V = 2t NEVER involves M: the duality is blind
to the DC component, which is exactly what Koide's balance constrains.""")

# Spectral triviality of the duality on the commensurate ring
Qd = np.trace(Cd @ Cd).real/np.trace(Cd).real**2
print(f"Q before/after duality: {Q:.6f} / {Qd:.6f}  (F is unitary -> Q invariant)")
assert abs(Q-Qd) < 1e-12
ipr = [np.sum(np.abs(np.linalg.eigh(M0r*np.eye(3)+br*S+np.conj(br)*S.T)[1]**4))/3
       for M0r, br in zip(rng.normal(5,2,50), rng.normal(0,1,50)+1j*rng.normal(0,1,50))]
print(f"IPR of eigenvectors over 50 random (M,beta): all = 1/3 "
      f"(spread {np.ptp(ipr):.1e}) -> always extended, NO localization")
print("""=> On the commensurate 3-ring the AA 'duality' is a unitary relabeling:
   spectrum-preserving, no localization transition, no critical point.
   (True AA criticality needs incommensurate frequency; 3 generations
   pin the ring to N=3, commensurate by construction.)""")

hdr("G3-C  why NO ring symmetry/duality can force the balance")

trs, frobs, qs, dsplits = [], [], [], []
for _ in range(1000):
    Z = rng.normal(size=(3,3)) + 1j*rng.normal(size=(3,3))
    U, _ = np.linalg.qr(Z)
    Cu = U @ C @ U.conj().T
    trs.append(np.trace(Cu).real); frobs.append(np.sum(np.abs(Cu)**2))
    qs.append(np.sum(np.abs(Cu)**2)/np.trace(Cu).real**2)
    d = np.real(np.diag(Cu)); dsplits.append(np.sum(d**2)/np.sum(np.abs(Cu)**2))
print(f"1000 random unitary conjugations of C:")
print(f"  tr C        : spread {np.ptp(trs):.1e}   (invariant)")
print(f"  ||C||_F^2   : spread {np.ptp(frobs):.1e}   (invariant)")
print(f"  Q           : spread {np.ptp(qs):.1e}   (invariant)")
print(f"  diag share  : ranges {min(dsplits):.3f} .. {max(dsplits):.3f}  (basis junk)")
print("""READ: M = tr(C)/3 and sum(m) = ||C||_F^2 are invariants of EVERY
unitary conjugation, and Koide is a relation purely between invariants
(variance of eigenvalues = mean^2). The Weyl algebra on Z_3 has the DC
component in its CENTER: every inner symmetry/duality of the internal
ring -- DFT, clock-shift Cliffords, all of them -- acts trivially on M
and can permute only the harmonics among themselves. So NO symmetry or
duality implemented ON the generation ring can tie M to |beta|.""")

hdr("G3 VERDICT against the pre-registered gate:  FAIL  (logged, stop)")
print("""The named mechanism is ELIMINATED, with a precise reason:
  * 'diag weight = off-diag weight' is NOT the AA self-dual point.
    AA self-duality balances MODULATION vs HOPPING (V=2t); Koide
    balances DC vs HOPPING (M^2 = 2|beta|^2) -- a pair no inner
    duality of the ring can even mix (M is central).
  * On the commensurate 3-ring the duality is a unitary relabeling:
    no fixed-point content, no criticality to sit at.
No TFT-native symmetry forces sqrt2 here -> per gate: NOT derived.

Characterization gained (exact, verified):
  Koide <=> generation ring with on-site energy M, hopping beta, and
  on-site^2 = 2 x hopping^2  (eigenvalue variance = mean^2).
  And a THEOREM-GRADE narrowing: the balance CANNOT come from any
  symmetry/duality acting on the internal ring; it must be DYNAMICAL
  (an energy functional selecting the ratio) or external.

FORWARD -- G4 (pre-registered lead, NOT run here): Derrick/virial.
  For static 1-D solitons, scale invariance FORCES gradient energy =
  potential energy exactly (the sine-Gordon kink saturates it). Map:
  hopping weight 6|beta|^2 <-> gradient energy; on-site weight 3M^2 <->
  potential energy; the virial identity then gives 3M^2 = 6|beta|^2 =
  Koide. G4 PASS = a concrete internal-ring energy functional where
  (i) the sqrt-mass components identify with gradient/potential weights
  with no ad hoc choices and (ii) stationarity yields 2|beta|^2 = M^2;
  FAIL = the identification must be assumed. Named, NOT claimed.""")

out = dict(
    gate="G3 pre-registered 2026-07-07: PASS=TFT reason for self-duality, "
         "FAIL=imposed by hand",
    verdict="FAIL -- AA self-duality mechanism ELIMINATED (duality balances "
            "modulation vs hopping, is blind to the central DC component M; "
            "unitary relabeling on the commensurate 3-ring). Circulant "
            "characterization VERIFIED. No tuning. Stopped per gate.",
    Q=Q, M=M, abs_beta=abs(beta), delta_deg=delta,
    A=2*abs(beta)/M, selfdual_ratio_2b2_M2=ratio,
    frob_diag=frob_diag, frob_offdiag=frob_off,
    duality_swap="(M0,t,V) -> (M0, V/2, 2t); self-dual V=2t; M untouched",
    forward_G4="Derrick/virial equipartition: grad=pot for static 1D solitons "
               "<-> 6|beta|^2 = 3M^2; gate pre-registered in RESULTS.md",
)
with open("outputs/G3_koide_selfdual.json", "w") as f:
    json.dump(out, f, indent=2, default=float)
print("\n[results block written: outputs/G3_koide_selfdual.json]")
