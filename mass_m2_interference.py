"""M2 -- the make-or-break gate of the mass-interference program.

Pre-registered gate (M0_prereg_mass_interference.md, verbatim):
  PASS = a concrete TFT field configuration with two coherent components
  (symmetric core + rotating internal mode) whose three Z3 orientations
  have energies proportional to |1 + A e^{i(delta+2pik/3)}|^2 -- i.e., a
  structure where amplitudes ADD before squaring into energy.
  FAIL = no such coherent-amplitude structure exists in TFT.

Strict discipline: part A first tests the LITERAL gate formula against
the PDG data itself, before any construction.
"""
import json
import numpy as np

def hdr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70)

m = np.array([0.51099895, 105.6583755, 1776.86])   # e, mu, tau (MeV, PDG)
v = np.sqrt(m)
w = np.exp(2j*np.pi/3)
c = np.array([v @ np.conj(w**(n*np.arange(3))) for n in range(3)])/3
M, delta = c[0].real, np.angle(c[1])
A = 2*abs(c[1])/M                                  # M1 values (observed)
alpha = delta + 2*np.pi*np.arange(3)/3
Qobs = m.sum()/v.sum()**2

hdr("M2-A  the LITERAL gate formula, tested against the data first")
print("""Literal target: m_k ~ |z0 + z1 e^{i alpha_k}|^2 = a + b cos(alpha_k+phi)
with a = |z0|^2+|z1|^2, b = 2|z0||z1|.  AM-GM forces b <= a for ANY
complex pair (z0, z1): a modulus-squared can never dip below zero.""")
F1 = np.sum(m*np.conj(w**np.arange(3)))
b_over_a = (2/3)*abs(F1)/m.mean()
print(f"leptons: cosine amplitude / mean = b/a = {b_over_a:.4f}")
print(f"required for the literal form:    b/a <= 1")
print(f"""=> the literal M2 formula is EXCLUDED BY THE PDG MASSES THEMSELVES:
the mass-cosine dips NEGATIVE (a-b = {m.mean()-(2/3)*abs(F1):.1f} MeV), which no
modulus-squared can do. The formula in M0 was MIS-SPECIFIED (drafting
error, mine): 'amplitudes add before squaring' written as a complex
modulus instead of a real projection. Per the working rules the literal
gate is ruled FAIL-BY-DATA (no TFT object could ever pass it, because
the leptons themselves do not). The corrected target is stated below
and put to Vic as amendment M2' -- NOT self-certified.""")

hdr("M2-B  what the data FORCES the interference to be (two theorems)")
print(f"""THEOREM 1 (reality / sign change). The surviving two-component form
is a REAL projection: sqrt(m_k) = M (1 + A cos alpha_k), verified exact
in M1. The electron amplitude {1+A*np.cos(alpha[0]):.5f} sits {np.degrees(np.arccos(-1/A)-delta):.3f} deg from a
SIGN CHANGE (a true zero crossing), which a complex modulus never has.
So the electron is light by CANCELLATION of two real contributions --
interference through a real projection (e.g. a cos-type coupling; TFT
owns one: the sine-Gordon term Lambda(1-cos theta) selects the real
direction of the phase). [Data-forced; coupling identification PROPOSED]

THEOREM 2 (parallelism / Cauchy-Schwarz). If state k's field is
f_core + a_k f_mode, its (quadratic) energy is a PERFECT SQUARE of a
linear amplitude iff f_mode is PARALLEL to f_core in the energy inner
product -- one spatial shape, three amplitudes. Misalignment eta breaks
Koide at second order. Numerically:""")
def QK_of_eta(eta):
    E = (1+A*np.cos(alpha))**2 + (eta*A*np.cos(alpha))**2
    s = np.sqrt(E)
    return E.sum()/s.sum()**2
etas = np.logspace(-5, -0.5, 400001)
dev = np.array([abs(QK_of_eta(e)-2/3) for e in [0]])  # baseline
qks = (1+A*np.cos(alpha))**2
base = abs(qks.sum()/np.sqrt(qks).sum()**2 - 2/3)
dQ_obs = abs(Qobs - 2/3)
# find eta whose ADDITIONAL Koide shift equals the observed deviation
lo, hi = 1e-6, 0.5
for _ in range(200):
    mid = np.sqrt(lo*hi)
    if abs(QK_of_eta(mid)-2/3) - base < dQ_obs: lo = mid
    else: hi = mid
eta_max = np.sqrt(lo*hi)
print(f"  observed Koide deviation |Q-2/3| = {dQ_obs:.2e}")
print(f"  misalignment that would produce it: eta = {eta_max:.2e}")
print(f"""=> IF H-MASS holds, the generation mode is aligned with the core to
~{eta_max*100:.2f}% -- and the known non-exactness of Koide acquires a natural
reading: a small, unprotected mode misalignment. [PROPOSED]""")

hdr("M2-C  the construction: a TFT-native object with real amplitude addition")

# --- C1: re-solve the omega=0.78 ground Q-ball (repo potential, inline) ---
DR, RMAX = 0.0075, 60.0
NSTEP = int(RMAX/DR)
def Uprime(rho, c2): return c2*rho - 4*rho**3 + 6*rho**5
def sweep(om, a_arr, store=False):
    c2 = 1.0-om*om
    a = np.atleast_1d(np.asarray(a_arr, float))
    rho = a + Uprime(a, c2)*DR*DR/6.0; p = Uprime(a, c2)*DR/3.0
    sgn = np.sign(rho); N = np.zeros(len(a), int)
    alive = np.ones(len(a), bool)
    traj = np.empty(NSTEP) if store else None
    r = DR
    for i in range(NSTEP):
        if store: traj[i] = rho[0]
        def f(rr, y0, y1): return y1, Uprime(y0, c2) - (2.0/rr)*y1
        k1 = f(r, rho, p); k2 = f(r+DR/2, rho+DR/2*k1[0], p+DR/2*k1[1])
        k3 = f(r+DR/2, rho+DR/2*k2[0], p+DR/2*k2[1])
        k4 = f(r+DR, rho+DR*k3[0], p+DR*k3[1])
        rho_n = rho + DR/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0])
        p_n   = p   + DR/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
        rho = np.where(alive, rho_n, rho); p = np.where(alive, p_n, p)
        alive &= np.abs(rho) < 2.0
        r += DR
        new = np.sign(rho)
        crossed = alive & (new != 0) & (new != sgn)
        N += crossed; sgn = np.where(crossed, new, sgn)
    return (N, traj) if store else N

om = 0.78
c2 = 1-om*om; disc = 1-2*c2
s1 = (1-np.sqrt(disc))/2
rho_m = np.sqrt((2+np.sqrt(4-6*c2))/6)
grid = np.concatenate([np.linspace(np.sqrt(s1)+1e-6, rho_m-1e-2, 400),
                       rho_m - np.logspace(-2, -15, 600)])
N = sweep(om, grid)
i0 = np.where((N[:-1] == 0) & (N[1:] > 0))[0][0]
lo, hi = grid[i0], grid[i0+1]
for _ in range(56):
    mid = 0.5*(lo+hi)
    if sweep(om, [mid])[0] == 0: lo = mid
    else: hi = mid
_, rho_bg = sweep(om, [0.5*(lo+hi)], store=True)
r = DR*np.arange(1, NSTEP+1)
it = np.argmin(np.abs(rho_bg))                      # truncate before tail blowup
rho_bg = np.where(np.arange(NSTEP) <= it, rho_bg, 0.0)
print(f"background: omega={om} ground Q-ball re-solved "
      f"(core rho={rho_bg[0]:.4f}, shell at rho^2=1/3)")

# --- C2: bound internal mode chi in the object's own well U(r)=F(rho^2) ---
Ufun = 1 - 4*rho_bg**2 + 6*rho_bg**4               # ->1 outside (mass gap)
step = 5                                            # dr=0.0375 for eigensolve
rr, UU = r[::step], Ufun[::step]
n = len(rr); h = rr[1]-rr[0]
H = (np.diag(2/h**2 + UU) + np.diag(-1/h**2*np.ones(n-1), 1)
     + np.diag(-1/h**2*np.ones(n-1), -1))           # u = r*chi, u(0)=u(R)=0
evals, evecs = np.linalg.eigh(H)
Eb = evals[0]
phi = evecs[:, 0]/np.sqrt(h*np.sum(evecs[:, 0]**2))  # normalized u(r)
loc = h*np.sum(phi[rr < 40]**2)
print(f"lowest internal mode: E = {Eb:.4f} (continuum starts at 1.0) "
      f"{'BOUND' if Eb < 1 else 'NOT BOUND'};  localization(r<40) = {loc:.4f}")
assert Eb < 1.0 and loc > 0.99, "no bound internal mode -- construction fails"

# --- C3: exact square law + nonlinear correction at lepton amplitudes ---
# The internal mode is a PHASE-DIRECTION (orthogonal) excitation: the
# repo EOM gives both complex components the same well F(rho^2), and for
# an orthogonal perturbation |psi| = sqrt(rho^2 + (q chi)^2) the linear
# term is absent identically -- energy is quadratic in q up to O(q^4).
q0 = 1e-3
qs = q0*(1 + A*np.cos(alpha))                       # the three REAL amplitudes
chi = phi/np.maximum(rr, h)                         # chi = u/r
def Vfun(x): return 0.5*x**2 - x**4 + x**6
rho_r = rho_bg[::step]
corr = []
for q in qs:
    full = Vfun(np.sqrt(rho_r**2 + (q*chi)**2)) - Vfun(rho_r)
    quad = 0.5*UU*(q*chi)**2
    dEnl = np.trapezoid((full-quad)*4*np.pi*rr**2, rr)
    Equad = 0.5*Eb*q**2                             # mode energy ~ q^2 exactly
    corr.append(abs(dEnl)/max(Equad, 1e-300))
print(f"mode = phase-direction internal excitation (linear term absent")
print(f"identically); E(q) = (Eb/2) q^2 quadratic; relative nonlinear")
print(f"corrections at the three lepton amplitudes (q0={q0}): "
      + ", ".join(f"{x:.1e}" for x in corr))
assert max(corr) < 1e-3
Ek = qs**2                                          # ratios; square law
print(f"\ncomposed states: q_k = q0 (1 + A cos(delta + 2pi k/3)),"
      f"  A={A:.6f}, delta={np.degrees(delta):.4f} deg  [INSERTED, not derived]")
print(f"  mass ratios: E_mu/E_e = {Ek[1]/Ek[0]:.2f} (PDG {m[1]/m[0]:.2f}),"
      f"  E_tau/E_mu = {Ek[2]/Ek[1]:.3f} (PDG {m[2]/m[1]:.3f})")
print(f"  Koide Q of the three mode energies: "
      f"{Ek.sum()/np.sqrt(Ek).sum()**2:.6f}  (PDG {Qobs:.6f})")

hdr("M2 VERDICT (strict, against the pre-registered gate)")
print(f"""LITERAL GATE: **FAIL-BY-DATA / MIS-SPECIFIED.** The written formula
(|1+Ae^..|^2, a complex modulus) cannot fit the leptons at all
(needs cosine/mean <= 1; data has {b_over_a:.3f}). My drafting error in M0;
no construction was attempted against it. Logged, not patched silently.

AMENDED TARGET M2' (put to Vic, evidence assembled but NOT self-passed):
  energies = [real amplitude]^2, amplitude = core + real projection of a
  rotating internal component: E_k ~ (1 + A cos(delta+2pik/3))^2.
Evidence that TFT supplies this structure:
  * mass = field energy, quadratic in amplitude (repo-DERIVED), so
    sqrt-mass IS an amplitude -- the square comes for free;
  * the object's own potential well binds a localized internal mode
    (E = {Eb:.3f} < 1, computed on the actual Q-ball background) -- a
    'generation dial' that is part of the particle, not radiation;
  * two real contributions into one mode amplitude add coherently and
    the energy is exactly their square (verified; nonlinear corrections
    < {max(corr):.0e} at lepton amplitudes);
  * data-forced theorems: the interference is a REAL projection (the
    electron sits near a sign change), and the mode must be PARALLEL to
    the core (Cauchy-Schwarz) -- with the measured Koide non-exactness
    naturally read as a ~{eta_max*100:.2f}% misalignment. [PROPOSED]
NOT delivered (honest boundary): A and delta are INSERTED, not derived
(M3's question); the orientation quantization (why exactly three Z3
positions) and the background-energy bookkeeping (the core's own energy
must be common-mode) are OPEN and flagged.""")

out = dict(
    prereg="M0_prereg_mass_interference.md; strict ruling on literal gate",
    literal_gate="FAIL-BY-DATA: modulus form needs b/a<=1, leptons have "
                 f"{b_over_a:.4f}; M0 formula mis-specified (agent error)",
    theorems=dict(reality="electron near a SIGN CHANGE -> real projection",
                  parallelism="perfect square iff mode parallel to core",
                  misalignment_reading_eta=float(eta_max)),
    construction=dict(background=f"omega={om} ground Q-ball",
                      bound_mode_E=float(Eb), localization=float(loc),
                      nonlinear_corr_max=float(max(corr)),
                      inserted=["A", "delta"],
                      open_flags=["orientation quantization (why Z3)",
                                  "background-energy bookkeeping",
                                  "A, delta underived (M3)"]),
    verdict="literal M2 FAIL-BY-DATA; amended M2' evidence assembled; "
            "ruling deferred to Vic per working rules",
)
with open("outputs/M2_interference.json", "w") as f:
    json.dump(out, f, indent=2)
print("\n[results block written: outputs/M2_interference.json]")
