"""G4 first cut: derive the modified-dynamics LAW (not import the empirical RAR).

TFT-native mechanism = MODIFIED INERTIA (the paper's "inertia saturates below a0"), from horizons:
  - Inertia in TFT = the cost of deforming the surrounding phase cycles to accelerate an object.
  - An object at acceleration a has a Rindler (acceleration) horizon at distance l_a = c^2/a.
  - The phase deformation that produces inertia is cut off by the smaller of l_a and the cosmological
    (Hubble) horizon R_H = c/H0.
  - a > a0 (l_a < R_H): full deformation -> normal inertia,  mu = 1        -> NEWTONIAN.
  - a < a0 (l_a > R_H): only the FRACTION R_H/l_a = R_H a/c^2 ~ a/a0 of the deformation is inside the
    cosmic horizon -> inertia reduced by a/a0,  mu -> a/a0                 -> DEEP MOND.

Consequences (DERIVED limits): mu(a/a0)*a = a_N gives
  - a >> a0:  a = a_N              (Newton)
  - a << a0:  a = sqrt(a_N a0)     (deep MOND)  ->  flat rotation curves + baryonic Tully-Fisher V^4 = G M a0.
The EXACT interpolation shape (transition region) is model-dependent -- same status as MOND.

Test: Milky Way with a limit-respecting interpolation (the "simple" mu) using the DERIVED a0.
"""
import numpy as np

G, Msun, kpc, c = 6.674e-11, 1.989e30, 3.086e19, 2.998e8
H0 = 70e3/3.086e22
a0 = c*H0/(2*np.pi)          # DERIVED in G1-G3
R_H = c/H0

# --- 1. the crossover is the acceleration-length = Hubble-radius condition ---
print("  crossover: acceleration length l_a = c^2/a  equals the Hubble radius at a ~ cH0:")
print(f"    c^2/a0 = {c**2/a0:.3e} m ;  2*pi*R_H = {2*np.pi*R_H:.3e} m  (equal: a0 = cH0/2pi)\n")

# --- 2. Milky Way with the DERIVED deep-MOND limit (simple interpolation, derived a0) ---
Md, Rd = 5.0e10*Msun, 2.6*kpc
Mb, ab = 1.5e10*Msun, 0.5*kpc
Mg, Rg = 1.2e10*Msun, 7.0*kpc
def Menc(R):
    return (Md*(1-(1+R/Rd)*np.exp(-R/Rd)) + Mg*(1-(1+R/Rg)*np.exp(-R/Rg)) + Mb*R**2/(R+ab)**2)

def V_tft(R):
    gN = G*Menc(R)/R**2
    g  = 0.5*(gN + np.sqrt(gN**2 + 4*gN*a0))   # mu(x)=x/(1+x): right LIMITS (Newton & sqrt(gN a0))
    return np.sqrt(g*R)/1e3

R_kpc = np.array([5, 8, 12, 16, 20, 25])
V_obs = np.array([225, 230, 222, 214, 205, 198])
V     = np.array([V_tft(r*kpc) for r in R_kpc])
print("  Milky Way, TFT modified-inertia law (derived a0, limit-respecting interpolation):")
print("  " + "{:>7s} {:>12s} {:>10s}".format("R(kpc)", "V_TFT(km/s)", "observed"))
for r, v, vo in zip(R_kpc, V, V_obs):
    print("  " + "{:>7.0f} {:>12.1f} {:>10.0f}".format(r, v, vo))
rms = np.sqrt(np.mean(((V-V_obs)/V_obs)**2))*100
print(f"  rms deviation = {rms:.1f}%   (empirical-RAR fit was 3.6%)\n")

# --- 3. the DERIVED parameter-free prediction: baryonic Tully-Fisher ---
Mbar = Md+Mb+Mg
Vflat = (G*Mbar*a0)**0.25/1e3
print("  baryonic Tully-Fisher (DERIVED, parameter-free): V_flat = (G M_bary a0)^(1/4)")
print(f"    M_bary = {Mbar/Msun:.2e} Msun  ->  V_flat = {Vflat:.0f} km/s   (observed MW ~200-220)")
print("\n  DERIVED: mechanism (modified inertia from horizons) + deep-MOND limit + Tully-Fisher.")
print("  MODEL-DEPENDENT (open): the exact interpolation shape in the transition -- as in MOND.")
