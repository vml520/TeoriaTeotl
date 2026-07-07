"""Deriving the 1/r-form gravitational metric from the phase field.

The paper writes the metric potential as ALGEBRAICALLY equal to the energy density:
    Phi_A(r) = |grad theta|^2 / E0^2      -> for theta~1/r this is ~1/r^4  (WRONG shape, falsified).

But the paper's own Chapter 9 says the field minimizes Dirichlet energy: the vacuum obeys
Laplace  del^2 theta = 0.  With a SOURCE (a mass = localized energy), Laplace becomes POISSON:
    del^2 Phi = u(x),     u = energy density = |grad theta|^2 .
The potential is SOURCED by the density, not EQUAL to it. By Gauss's law the far field then depends
on the TOTAL enclosed energy (= the mass M), which is finite:
    Phi_B(r) -> -M/r   (right shape),   force -grad Phi_B ~ 1/r^2.

Universality: u >= 0 everywhere, so enclosed "charge" is always positive -> Phi_B is always an
attractive well -> ALL masses attract. No signed charge possible (unlike the EM winding sector).

Test: take a smoothed point defect theta = -A/sqrt(r^2+a^2); u = |grad theta|^2 (~1/r^4 far out).
Compare the algebraic potential (paper) vs the Poisson-sourced potential (corrected).
"""
import numpy as np

A, a = 1.0, 1.0
r = np.linspace(1e-3, 200.0, 400000)

# smoothed point defect and its energy density
theta   = -A/np.sqrt(r**2 + a**2)
dtheta  = A*r/(r**2 + a**2)**1.5          # d(theta)/dr
u       = dtheta**2                        # energy density |grad theta|^2  (~ A^2/r^4 far field)

M_tot = np.trapezoid(u*4*np.pi*r**2, r)    # total energy = "mass"

# --- Poisson solve:  del^2 Phi_B = u   (spherical), Phi_B(inf)=0 ---
# closed form:  Phi_B(r) = -[ enclosed(r)/r + tail(r) ],
#   enclosed(r) = ∫_0^r u s^2 ds ,  tail(r) = ∫_r^inf u s ds
cum       = np.concatenate([[0.0], np.cumsum(0.5*(u[1:]*r[1:]**2 + u[:-1]*r[:-1]**2)*np.diff(r))])
enclosed  = cum
tail_full = np.trapezoid(u*r, r)
tail_cum  = np.concatenate([[0.0], np.cumsum(0.5*(u[1:]*r[1:] + u[:-1]*r[:-1])*np.diff(r))])
tail      = tail_full - tail_cum
Phi_B     = -(enclosed/r + tail)
force_B   = enclosed/r**2                   # |Phi_B'(r)| = enclosed(r)/r^2

# --- Algebraic (paper):  Phi_A = u ---
Phi_A = u.copy()

def slope(x, y, lo, hi):
    m = (x >= lo) & (x <= hi) & (np.abs(y) > 0)
    return np.polyfit(np.log(x[m]), np.log(np.abs(y[m])), 1)[0]

print(f"total energy (mass) M = 4*pi*Q = {M_tot:.4f}\n")
print("            construction        far-field falloff (log-log slope over r in [5,50])")
print(f"  ALGEBRAIC  Phi_A = |grad th|^2      slope = {slope(r, Phi_A, 5, 50):+.3f}   (paper: 1/r^4, short range)")
print(f"  POISSON    del^2 Phi_B = |grad th|^2 slope = {slope(r, Phi_B, 5, 50):+.3f}   (corrected: 1/r  -> gravity)")
print(f"  POISSON    force -grad Phi_B          slope = {slope(r, force_B, 5, 50):+.3f}   (1/r^2 Newtonian force)")

print("\n  sanity: Phi_B * r  should be ~ -M/(4*pi) constant in the far field:")
for rr in [10, 30, 60, 100]:
    i = np.argmin(np.abs(r-rr))
    print(f"    r={rr:4d}   Phi_B={Phi_B[i]:+.6e}   Phi_B*r={Phi_B[i]*rr:+.6f}   -M/4pi={-M_tot/(4*np.pi):+.6f}")

# --- universality: two energy blobs both dig the SAME-sign well ---
print("\n  universality check: min(u) = {:.3e}  (>= 0 everywhere => enclosed charge always +".format(u.min()))
print("  => every mass sources an attractive well; two masses' wells add -> universal attraction.)")
