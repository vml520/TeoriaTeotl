"""Attacking the gravitational coupling G — what a mass couples to, and where G lives.

Complex field psi = rho e^{i theta}.  Two conserved currents:
  U(1) Noether current  j^mu = rho^2 d^mu theta   -> charge density j^0 = rho^2 * omega   (LINEAR, signed)
  energy-momentum       T^mu,nu                    -> energy density  T^00 ~ rho^2 omega^2  (QUADRATIC, >=0)

Claim: EM couples to j (signed -> Coulomb, like-repel: the sign test); gravity couples to T^00
(positive -> universal attraction). Sharp check: matter (omega>0) vs antimatter (omega<0) should have
OPPOSITE charge but IDENTICAL energy => both gravitate the same way (attractive). Test it.

Then: where is Newton's G?  The phase-field action contains NO gravity (no T-metric coupling), so G
is not fixed by the field dynamics. Dimensionally the two primitives give  G = l0 c^4 / E0 . Check that
this is an identity when (E0, l0) are the Planck scale — i.e. G is expressible in the primitives.
"""
import numpy as np

# ---- oscillating lump: charge (linear in omega) vs energy (quadratic in omega) ----
x   = np.linspace(-20, 20, 200000)
sig = 2.0
rho = np.exp(-x**2/(2*sig**2))          # amplitude profile |psi|
drho = np.gradient(rho, x)
c = 1.0

def charge(omega):                       # Q = ∫ rho^2 * omega dx  (U(1) charge)
    return np.trapezoid(rho**2 * omega, x)

def energy(omega):                       # E = ∫ [1/2 rho^2 omega^2 / c^2 + 1/2 (drho)^2] dx
    return np.trapezoid(0.5*rho**2*omega**2/c**2 + 0.5*drho**2, x)

print("  oscillating lump: charge j^0=rho^2*omega (EM)  vs  energy T^00~rho^2*omega^2 (gravity)")
print(f"  {'omega':>7s} {'charge Q':>12s} {'energy E':>12s}")
for w in [+2.0, +1.0, -1.0, -2.0]:
    print(f"  {w:>7.1f} {charge(w):>12.4f} {energy(w):>12.4f}")
print("  => charge flips sign with omega (matter vs antimatter: opposite EM charge);")
print("     energy is identical for +/-|omega| and always positive (both gravitate attractively).")
print("     This is the derived reason gravity is universal and EM is not.\n")

# ---- G = l0 c^4 / E0 : identity at the Planck scale ----
c_SI   = 2.99792458e8
hbar   = 1.054571817e-34
G_CODATA = 6.67430e-11
l_P = np.sqrt(hbar*G_CODATA/c_SI**3)     # Planck length  (E0=Planck energy, l0=Planck length)
E_P = np.sqrt(hbar*c_SI**5/G_CODATA)     # Planck energy
G_from_primitives = l_P * c_SI**4 / E_P

print("  Newton's G from the two primitives (E0=Planck energy, l0=Planck length):")
print(f"    l0 = {l_P:.4e} m    E0 = {E_P:.4e} J")
print(f"    G = l0 c^4 / E0 = {G_from_primitives:.6e}   CODATA G = {G_CODATA:.6e}")
print(f"    ratio = {G_from_primitives/G_CODATA:.6f}")
print("  => G IS expressible in E0, l0 (Planckian). But this is a DIMENSIONAL identity, not a")
print("     derivation of the coefficient: the phase-field action has no T-metric coupling, so the")
print("     STRENGTH of gravity (the O(1) coefficient / existence of the Poisson coupling) is not")
print("     fixed by the field. That is the emergent-metric / quantum-gravity step — genuinely open.")
