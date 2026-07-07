"""Milky Way rotation curve: derived-Newtonian TFT gravity vs the paper's proposed a0 = c H0 / 2pi.

TWO SEPARATE QUESTIONS, kept apart on purpose:
  (A) The gravity we DERIVED this session is Poisson/Newtonian (del^2 Phi = 4 pi G rho, 1/r).
      With baryons only it predicts a FALLING (Keplerian) curve -> the dark-matter problem.
  (B) The paper PROPOSES (does NOT derive) a low-acceleration scale a0 = c H0 / 2pi ~ 1.1e-10 m/s^2,
      applied MOND-style via the empirical Radial Acceleration Relation (RAR, McGaugh 2016):
          g_obs = g_N / (1 - exp(-sqrt(g_N/a0))).
      This is imported MOND phenomenology with the paper's a0 value. NOT a TFT derivation.

Baryonic Milky Way model (approximate, representative literature values; NOT tuned to the curve):
  stellar disk 5.0e10 Msun (R_d=2.6 kpc), bulge 1.5e10 Msun, gas 1.2e10 Msun (R_g=7 kpc).
Observed curve: representative points (Eilers+2019 / Sofue style), roughly flat ~200-230 km/s.
"""
import numpy as np

G, Msun, kpc, c = 6.674e-11, 1.989e30, 3.086e19, 2.998e8
H0 = 70e3/3.086e22                     # 70 km/s/Mpc in 1/s
a0 = c*H0/(2*np.pi)
print(f"  a0 = c H0 / 2pi = {a0:.3e} m/s^2   (empirical MOND a0 ~ 1.2e-10)\n")

Md, Rd = 5.0e10*Msun, 2.6*kpc
Mb, ab = 1.5e10*Msun, 0.5*kpc
Mg, Rg = 1.2e10*Msun, 7.0*kpc
print(f"  total baryonic mass = {(Md+Mb+Mg)/Msun:.2e} Msun\n")

def M_enc(R):
    disk  = Md*(1-(1+R/Rd)*np.exp(-R/Rd))
    gas   = Mg*(1-(1+R/Rg)*np.exp(-R/Rg))
    bulge = Mb*R**2/(R+ab)**2
    return disk+gas+bulge

def curves(R):
    M  = M_enc(R)
    gN = G*M/R**2
    VN = np.sqrt(G*M/R)                             # (A) derived Newtonian gravity, baryons only
    gO = gN/(1-np.exp(-np.sqrt(gN/a0)))             # (B) RAR with paper's a0
    VM = np.sqrt(gO*R)
    return VN/1e3, VM/1e3

R_kpc = np.array([5, 8, 12, 16, 20, 25])
V_obs = np.array([225, 230, 222, 214, 205, 198])   # representative observed (km/s)

print("  " + "{:>7s} {:>16s} {:>16s} {:>10s}".format(
      "R(kpc)", "(A) Newtonian", "(B) a0=cH0/2pi", "observed"))
for r, vo in zip(R_kpc, V_obs):
    vN, vM = curves(r*kpc)
    print("  " + "{:>7.0f} {:>16.1f} {:>16.1f} {:>10.0f}".format(r, vN, vM, vo))

# simple goodness numbers (rms % deviation from observed)
vN = np.array([curves(r*kpc)[0] for r in R_kpc])
vM = np.array([curves(r*kpc)[1] for r in R_kpc])
print(f"\n  rms deviation from observed:  Newtonian = {np.sqrt(np.mean(((vN-V_obs)/V_obs)**2))*100:.1f}%"
      f"   a0-model = {np.sqrt(np.mean(((vM-V_obs)/V_obs)**2))*100:.1f}%")
print("\n  (A) derived Newtonian gravity FALLS well below observed -> needs a dark sector.")
print("  (B) the paper's proposed a0 flattens the curve to ~observed -- i.e. MOND with a0=cH0/2pi,")
print("      an IMPORTED, NOT-DERIVED modification. TFT's contribution is only the a0 value.")
