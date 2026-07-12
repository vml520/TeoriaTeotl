import json
import numpy as np

def hdr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70)
SQRT2 = np.sqrt(2)

# ---------------------------------------------------------------------
# G4 GATE (pre-registered in RESULTS.md 2026-07-07, BEFORE this run):
#   Lead: Derrick/virial equipartition. Static 1-D solitons obey
#   integral(gradient) = integral(potential) exactly (scale invariance);
#   candidate map: hopping weight 6|beta|^2 <-> gradient energy,
#   on-site weight 3M^2 <-> potential energy -> virial forces Koide.
#   PASS = a concrete internal-ring/soliton energy functional where
#     (i) the sqrt-mass components identify with gradient/potential
#         weights with NO ad hoc choices, AND
#     (ii) stationarity yields 2|beta|^2 = M^2 with no tuning.
#   FAIL = the identification must be assumed.
# ---------------------------------------------------------------------

m = np.array([0.51099895, 105.6583755, 1776.86])   # e, mu, tau (MeV, PDG)
v = np.sqrt(m)
Q = m.sum()/v.sum()**2
w = np.exp(2j*np.pi/3)
n3 = np.arange(3)
c = np.array([v @ np.conj(w**(n*n3)) for n in range(3)])/3
M, b, delta = c[0].real, abs(c[1]), np.angle(c[1])
print(f"Lepton ring point (from G3): M={M:.5f}  |beta|={b:.5f}  "
      f"delta={np.degrees(delta):.3f} deg   Q={Q:.6f}")

hdr("G4-A  Derrick/virial VERIFIED on the TFT kink -- and why it is 'vertical'")

x = np.arange(-20.0, 20.0, 1e-3)
print("sine-Gordon kink phi = 4 arctan(e^{mu x}),  U = mu^2 (1 - cos phi):")
for mu in (0.31, 1.0, 2.7):
    phi = 4*np.arctan(np.exp(mu*x))
    Eg = np.trapz(0.5*np.gradient(phi, x)**2, x)
    Ep = np.trapz(mu**2*(1-np.cos(phi)), x)
    assert abs(Eg/Ep - 1) < 1e-4, "kink virial violated -- ABORT"
    print(f"  mu={mu:4.2f}:  E_grad={Eg:.6f}  E_pot={Ep:.6f}  "
          f"(equal; mass = {Eg+Ep:.4f} = 8mu)")
print("""=> Equipartition holds for EVERY mu, i.e. for solitons of ANY mass.
   It is a PER-SOLITON identity (fixes each particle's internal energy
   budget), so it carries ZERO information about ratios BETWEEN masses.
   Koide is a horizontal (across-family) relation; Derrick is vertical.
   For Derrick to yield Koide, the gradient/potential split must align
   with the DC/modulation split ACROSS the family. Test that next.""")

hdr("G4-B  transplants onto the generation ring: every local version fails")

print("""First, the reading matters. If C were a HAMILTONIAN, the uniform
on-site M would be an energy-zero offset (pure gauge) -- but eig(C) are
the physical sqrt-masses, so M is physical: C must be a matrix of FIELD
VALUES (vevs). Then 'energy' means a functional of the ring profile
v_k = M + 2|beta| cos(delta + 2pi k/3). The natural functionals:""")

# discrete nearest-neighbour gradient and spectral gradient of the profile
d_nn = np.sum((np.roll(v, -1) - v)**2)             # sum (v_{k+1}-v_k)^2
F = np.fft.fft(v)
dv = np.fft.ifft(1j*np.array([0, 1, -1])*F)
d_sp = np.sum(np.abs(dv)**2)                       # spectral d/dtheta, sampled
assert abs(d_nn - 18*b**2) < 1e-8 and abs(d_sp - 6*b**2) < 1e-8
pot_q = np.sum(v**2)                               # local quadratic potential
print(f"  NN gradient  sum(v_k+1 - v_k)^2 = {d_nn:.4f} = 18|beta|^2")
print(f"  spectral gradient sum|dv|^2     = {d_sp:.4f} =  6|beta|^2")
print(f"  local quadratic sum v_k^2       = {pot_q:.4f} = 3M^2 + 6|beta|^2")

print("""
Equipartition E_grad = E_pot, unit couplings (the no-tuning choice):
  1. NN gradient vs local quadratic:   18b^2 = 3M^2 + 6b^2
       -> M^2 = 4b^2 -> A = 2b/M = 1      -> Q = 1/2      RULED OUT
  2. spectral grad vs local quadratic:  6b^2 = 3M^2 + 6b^2
       -> M = 0 (A unbounded, sqrt-m < 0) -> unphysical   RULED OUT
  3. free couplings kappa, omega^2: one equation, two couplings ->
       satisfiable for ANY (M, b)         -> selects NOTHING
Measured Q = 0.666661. No local equipartition lands on 2/3.""")

hdr("G4-C  constrained-stationarity scan of E = sum(m) = 3M^2 + 6|beta|^2")

detC = M**3 - 3*M*b**2 + 2*b**3*np.cos(3*delta)
S = np.roll(np.eye(3), 1, axis=0)
Cmat = M*np.eye(3) + c[1]*S + np.conj(c[1])*S.T
assert abs(np.linalg.det(Cmat).real - detC) < 1e-8  # circulant det identity
c_needed = (2*M**2 - b**2)/(M*b)
print(f"fixed trace  (3M):  stationarity -> beta = 0        -> A=0, Q=1/3  (ruled out)")
print(f"fixed fluct  (6b^2): stationarity -> M = 0           -> unphysical")
print(f"fixed det:   Lagrange condition needs cos(3 delta) = (2M^2-b^2)/(Mb)")
print(f"             at the lepton point = {c_needed:.3f}  > 1  -> leptons NOT stationary;")
print(f"             solving exactly (sin 3delta = 0) -> M = b  -> A=2, Q=1   (ruled out)")
print("""=> Ring-local stationarity only ever selects the already-eliminated
   corners A=0 (Q=1/3) and A=2 (Q=1), or selects nothing. A = sqrt2 is
   never a stationary point of any of these. (Same corners as G2 -- the
   pattern is structural, not an accident of candidates.)""")

hdr("G4-D  what the split REQUIRES: a democratic (non-local) term  [exact]")

print("""For 'potential weight = 3M^2' with a LOCAL potential sum_k U(v_k):
  d^2/db^2 [ sum_k U(M + 2b cos theta_k) ]_(b=0) = 6 U''(M)
must vanish for all M  ->  U linear  ->  potential ~ 3aM + const,
which can never equal 3M^2.  NO local U gives the split.  Exact kill.

The unique object that does:  3M^2 = (sum_k v_k)^2 / 3 = (tr Phi)^2 / 3
-- a DEMOCRATIC, all-site (trace-squared) interaction, non-local on the
ring. And then 'gradient weight' = tr(Phi^2) - (tr Phi)^2/3. Verify:""")
tr1, tr2 = v.sum(), np.sum(v**2)
print(f"  (tr Phi)^2/3          = {tr1**2/3:.4f}   (= 3M^2      = {3*M**2:.4f})")
print(f"  tr(Phi^2)-(trPhi)^2/3 = {tr2-tr1**2/3:.4f}   (= 6|beta|^2 = {6*b**2:.4f})")
print(f"""
With democratic terms ALLOWED, 'equipartition' reads
  (tr Phi)^2/3 = tr(Phi^2) - (tr Phi)^2/3   <=>   (tr Phi)^2 = (3/2) tr(Phi^2)
  <=>  Q = 2/3  identically  --  it RESTATES Koide, it does not force it.
(check: (trPhi)^2 / trPhi^2 = {tr1**2/tr2:.6f}, 3/2 = 1.5)
The whole mechanism collapses into ONE number: the ratio of the
(tr Phi)^2 and tr(Phi^2) couplings in the internal potential. E.g.
V = lambda [tr(Phi^2) - a (tr Phi)^2]^2 has stationary manifold
tr(Phi^2) = a (tr Phi)^2, i.e. it pins Q = a exactly; a = 2/3 gives
Koide -- but a is put in BY HAND. This is precisely where the
Koide/yukawaon model-building literature parks the problem. TFT has not
derived a; per the gate, the identification 'must be assumed'.""")

hdr("G4 VERDICT against the pre-registered gate:  FAIL  (logged, stop)")
print("""The Derrick/virial mechanism does NOT force Koide:
  * The genuine TFT virial identity is per-soliton (vertical) -- it
    holds for every mass separately and constrains no mass ratio.
  * Every LOCAL transplant onto the ring gives the wrong point
    (Q=1/2), an unphysical point (M=0), or no constraint at all;
    constrained stationarity only re-finds the eliminated corners
    A=0 and A=2. A=sqrt2 is never stationary.
  * The required (3M^2 | 6b^2) split provably cannot come from any
    local potential; it demands a democratic (tr Phi)^2 term whose
    coefficient must be assumed -> FAIL by the gate's own words.

Characterization gained (adds to G3):
  G3 closed the SYMMETRY/DUALITY class; G4 closes RING-LOCAL
  ENERGETICS. What remains is exactly one door: a democratic
  (all-generation) interaction with coupling ratio a = 2/3. Koide,
  in TFT terms, is now ONE unexplained coefficient, not a relation.

FORWARD -- G5 (pre-registered lead, NOT run here): derive the
  democratic term from TFT collective dynamics. The (1,1,1) direction
  is the ring's ZERO MODE (rigid phase rotation of the 3-state object);
  integrating out / quantizing the collective coordinate is the natural
  TFT source of a (tr Phi)^2 term. G5 PASS = the collective-mode
  calculation produces the democratic pair with coupling ratio a = 2/3
  (equivalently forces (tr Phi)^2 = (3/2) tr Phi^2) with no tuning;
  FAIL = a remains free. Named, NOT claimed.""")

out = dict(
    gate="G4 pre-registered 2026-07-07: PASS=non-ad-hoc grad/pot "
         "identification + stationarity gives 2b^2=M^2; FAIL=assumed",
    verdict="FAIL -- virial is per-soliton (no ratio content); all local "
            "ring transplants give Q=1/2, M=0, or nothing; stationarity "
            "scan re-finds only A=0/A=2 corners; the required split needs "
            "a democratic (trPhi)^2 term whose coefficient is assumed. "
            "No tuning. Stopped per gate.",
    kink_virial="E_grad=E_pot verified to <1e-4 for mu=0.31,1.0,2.7",
    NN_equipartition_Q=0.5, spectral_equipartition="M=0 (unphysical)",
    fixed_det_lagrange_cos3delta_needed=c_needed,
    democratic_identity_check=dict(trPhi_sq_over_3=tr1**2/3, three_Msq=3*M**2,
                                   fluct=tr2-tr1**2/3, six_bsq=6*b**2,
                                   trPhi_sq_over_trPhi2=tr1**2/tr2),
    forward_G5="derive democratic (trPhi)^2 coupling ratio a=2/3 from TFT "
               "collective/zero-mode dynamics; gate in RESULTS.md",
)
with open("outputs/G4_koide_derrick.json", "w") as f:
    json.dump(out, f, indent=2, default=float)
print("\n[results block written: outputs/G4_koide_derrick.json]")
