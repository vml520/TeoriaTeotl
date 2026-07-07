"""G1 first cut: does a0 = c H0 / 2pi fall out of TFT structurally, via the field mass (Lambda)?

Chain under test:
  1. TFT field mass gap (from sine-Gordon coupling Lambda): m = sqrt(Lambda)/l0.   [DERIVED earlier]
  2. COSMOLOGICAL identification (the assumption to justify in G2, = Vic's "alpha from Lambda"):
     the field is ultralight, its reduced Compton wavelength = the Hubble radius:
        lambda_bar = hbar/(m c) = c/H0     <=>     m = hbar H0 / c^2   (the "Hubble mass").
  3. Then the field's Compton FREQUENCY is  f = m c^2 / h = H0 / 2pi   (2pi = h/hbar = one S^1 cycle).
  4. Crossover acceleration:  a0 = c * f = c H0 / 2pi.   (An acceleration a has characteristic
     frequency a/c; when a/c drops below the field's Compton frequency H0/2pi, gravity is modified.)

Checks: (a) field mass ~ 10^-33 eV (Hubble/cosmological-constant scale); (b) a0 = cH0/2pi matches
the empirical RAR scale; (c) the Compton (screening) length = Hubble radius >> galactic/solar scales,
so the field is effectively MASSLESS locally -> the 1/r gravity we derived -- and only bites at a0.
"""
import numpy as np

hbar, c, e = 1.054571817e-34, 2.99792458e8, 1.602176634e-19
h = 2*np.pi*hbar
H0 = 70e3/3.086e22                      # 70 km/s/Mpc in 1/s
kpc, AU = 3.086e19, 1.495978707e11

# 2. field mass = Hubble mass
m = hbar*H0/c**2
print("  (a) field mass = hbar H0 / c^2 (Hubble mass):")
print(f"      m = {m:.3e} kg = {m*c**2/e:.3e} eV   (cosmological-constant scale ~1e-33 eV)")

# reduced Compton wavelength vs Hubble radius
lam_bar = hbar/(m*c)
R_H     = c/H0
print(f"      reduced Compton lambda_bar = {lam_bar:.3e} m ;  Hubble radius c/H0 = {R_H:.3e} m")
print(f"      ratio lambda_bar / R_H = {lam_bar/R_H:.4f}   (=1: Compton wavelength IS the Hubble radius)\n")

# 3-4. a0 = c * Compton frequency = cH0/2pi
f_field = m*c**2/h
a0 = c*f_field
print("  (b) a0 = c * (Compton frequency f = m c^2 / h = H0/2pi):")
print(f"      f_field = {f_field:.3e} Hz = H0/2pi = {H0/(2*np.pi):.3e}")
print(f"      a0 = c H0 / 2pi = {a0:.3e} m/s^2")
print(f"      empirical RAR scale g_dagger = 1.20e-10 +/- 0.24(syst)  ->  ratio = {a0/1.20e-10:.3f}\n")

# (c) locally massless: screening length (= Compton = Hubble radius) vs galactic/solar scales
print("  (c) Yukawa screening length = Compton wavelength = Hubble radius. Locally negligible:")
for label, L in [("galaxy (30 kpc)", 30*kpc), ("solar system (30 AU)", 30*AU)]:
    print(f"      {label:>22s}: screening length / scale = {R_H/L:.2e}  (>>1 => effectively massless)")
print("\n  => same field is MASSLESS on sub-cosmological scales (gives the 1/r gravity we derived),")
print("     and its tiny (Hubble) mass sets the acceleration a0 where gravity changes regime.")
print("     Stage 2 failed because it used Lambda~O(1) (screening at l0); the cosmological Lambda")
print("     is ultralight (screening at the Hubble radius). Vic's 'alpha from Lambda' -> a0 via m=sqrt(L)/l0.")
