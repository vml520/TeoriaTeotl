"""G3: control the vacuum-energy normalization. Does the coefficient come out at 1/2pi?

Proper treatment. The sine-Gordon potential energy density is
    u_V(theta) = (E0 Lambda / l0^3) (1 - cos theta)          [axion-like, mu^4 (1-cos)]
- Mass gap (curvature at theta=0):  omega0 = c sqrt(Lambda)/l0.  FIXED, independent of where the
  field sits. This is what enters a0 = c * (Compton freq) = c * omega0/2pi.  The 2pi is clean:
  it is h/hbar = one full S^1 cycle. NOT the source of the discrepancy.
- Dark energy density = the potential HEIGHT at the field's current position theta_i:
    rho_DE = (E0 Lambda / l0^3)(1 - cos theta_i).
  This depends on theta_i (a cosmological initial condition / how far the field has rolled).

Friedmann H0^2 = 8piG rho_DE/(3c^2), with G = l0 c^4/E0.  Lambda cancels. Result:
    a0 = (c H0 / 2pi) * sqrt( 3 / (8 pi (1 - cos theta_i)) ).
So the 2pi is clean; the LEFTOVER O(1) is sqrt(3/(8pi(1-cos theta_i))) = omega0/H0 -- how close the
field mass is to the Hubble mass, set by the field's position. NOT uniquely fixed by the framework.
"""
import numpy as np

cH0_over_2pi = 1.082e-10           # from earlier (c H0 / 2pi), m/s^2
g_emp = 1.20e-10

def a0(theta_i):
    x = 1 - np.cos(theta_i)
    return cH0_over_2pi*np.sqrt(3/(8*np.pi*x)), np.sqrt(3/(8*np.pi*x))  # (a0, omega0/H0)

print("  a0 = (cH0/2pi) * sqrt(3/(8pi(1-cos theta_i))).  The 2pi is geometric; the rest is theta_i.\n")
print("  " + "{:>10s} {:>10s} {:>12s} {:>12s} {:>10s}".format(
      "theta_i", "omega0/H0", "a0 (m/s^2)", "= cH0/N", "vs emp"))
for th in [0.2, 0.44, np.pi/4, np.pi/2, np.pi]:
    a, r = a0(th)
    N = 2*np.pi/r
    print("  " + "{:>10.3f} {:>10.3f} {:>12.3e} {:>12s} {:>10.2f}".format(
          th, r, a, f"cH0/{N:.1f}", a/g_emp))

# what theta_i does the data prefer?
x_needed = 3/(8*np.pi*(g_emp/cH0_over_2pi)**2)
th_needed = np.arccos(1 - x_needed)
print(f"\n  data (a0=1.20e-10) wants 1-cos(theta_i) = {x_needed:.3f}  ->  theta_i = {th_needed:.2f} rad (~{np.degrees(th_needed):.0f} deg)")
print("  i.e. omega0 ~ H0 (field mass ~ Hubble mass), the standard quintessence 'thawing' condition.\n")
print("  VERDICT: the 2pi is derived (Compton/S^1). The remaining coefficient is omega0/H0 = O(1),")
print("  set by the field's cosmic position -- NATURAL to be ~1 (quintessence), consistent with data,")
print("  but NOT uniquely fixed by the framework. Generic theta_i~O(1) gives ~3x low; data wants m~=H0.")
