"""G2 first cut: does the field's mass = Hubble mass follow from it being the dark energy?

Self-consistency loop (the mechanism):
  - field mass gap frequency:      omega0 = c sqrt(Lambda) / l0
  - field vacuum energy density:   rho ~ E0 Lambda / l0^3   (potential-energy scale of the field)
  - IF the field IS the dark energy, it drives expansion via Friedmann:
                                    H0^2 = 8 pi G rho / (3 c^2)
  - using the TFT relation G = l0 c^4 / E0, solve for omega0 / H0.

KEY: Lambda CANCELS. The loop fixes the RATIO omega0/H0 independent of the (unknown) absolute
value of Lambda. So we derive the RELATION m ~ H0 WITHOUT needing to solve the cosmological
constant problem (the absolute value of Lambda ~ 1e-122 stays an input).

Honest question: does the coefficient come out at the clean geometric value (=> a0 = cH0/2pi),
or something else?
"""
import numpy as np

G, c, hbar = 6.674e-11, 2.998e8, 1.054571817e-34
lP = np.sqrt(hbar*G/c**3)          # Planck length (= l0)
EP = np.sqrt(hbar*c**5/G)          # Planck energy (= E0)
H0 = 70e3/3.086e22
RH = c/H0

# --- solve the loop numerically for a few Lambda, show the ratio is Lambda-independent ---
print("  omega0/H0 from the self-consistency loop (should be Lambda-independent):")
for Lam in [1e-122, 1e-120, 1e-124]:
    omega0 = c*np.sqrt(Lam)/lP
    rho    = EP*Lam/lP**3
    H0F    = np.sqrt(8*np.pi*G*rho/(3*c**2))
    print(f"    Lambda={Lam:.0e}:  omega0/H0F = {omega0/H0F:.4f}")
ratio = np.sqrt(3/(8*np.pi))
print(f"  analytic ratio = sqrt(3/8pi) = {ratio:.4f}   => mass gap = {ratio:.3f} * Hubble mass\n")

# --- consequence for a0 ---
a0_selfcons = c*H0*ratio/(2*np.pi)     # a0 = c * (omega0/2pi),  omega0 = ratio*H0
a0_clean    = c*H0/(2*np.pi)           # G1 geometric value (m = Hubble mass exactly)
g_emp       = 1.20e-10
print("  a0 predictions:")
print(f"    self-consistency (naive):  a0 = {a0_selfcons:.3e}  = cH0/{2*np.pi/ratio:.1f}   ratio to obs = {a0_selfcons/g_emp:.2f}")
print(f"    G1 geometric (cH0/2pi):    a0 = {a0_clean:.3e}  = cH0/{2*np.pi:.2f}   ratio to obs = {a0_clean/g_emp:.2f}")
print(f"    empirical RAR g_dagger:         {g_emp:.3e}")
print(f"    --> the two routes disagree by sqrt(8pi/3) = {1/ratio:.2f}x. NOT resolved.\n")

# --- cosmological-constant connection (absolute scale = the CC problem, NOT solved) ---
Lam_cc = (lP/RH)**2
print(f"  Lambda (if m = Hubble mass) = (l0/R_H)^2 = {Lam_cc:.2e}  ~ cosmological constant ~1e-122")
print("  The RELATION m~H0 is derived (Lambda cancels); the ABSOLUTE value ~1e-122 is the CC problem.")
