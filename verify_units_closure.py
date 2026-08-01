"""Is the SI second an input to TFT, or does the theory make it? (UNIT0)

Vic's question: could standard time units -- "joules per second" -- be quietly causing a
tension in the calculations?

Answer: no, and the reason is structural. The second is a DERIVED unit here. Two of the
theory's own statements fix it (both already in DERIVED_SUMMARY sec.1):

  A2  ell0 = c * tau0             from c = E0/p0 with dtau = hbar dtheta/E, dl = hbar dtheta/p
  A3  hbar = E0 * tau0 / (2 pi)

Given the two primitives (E0, ell0) the second is fully determined; there is no leftover
convention to correct for. A units error in a theory like this would surface as a DIMENSIONAL
MISMATCH, not as a tension. Every gate in this repo runs in code units (ell0 = c = E0 = 1) and
reinstates the second only at the reporting boundary; the only carriers of 's' anywhere are
c [m/s], hbar [J s], H0 [1/s].

What falls out is sharper than the question. Adding the dimensional form of G,

  A1  G = ell0 c^4 / E0           (sec.4; its O(1) coefficient is the OPEN quantum-gravity step)

closes the system:  G = c^5 tau0 / E0  and  tau0 = 2 pi hbar / E0  give

  G = 2 pi hbar c^5 / E0^2   =>   E0 = sqrt(2 pi hbar c^5 / G) = sqrt(2 pi) * E_Planck

and likewise ell0 = sqrt(2pi) * l_Planck, tau0 = sqrt(2pi) * t_Planck. The 2pi is the
CIRCUMFERENCE of the compact time-circle -- the same 2pi that appears in a0 = c H0 / 2pi and in
hbar = E0 tau0 / 2pi. TFT's primitives are not the Planck units; they are the Planck units
dressed by one trip around S^1.

LABELS -- read these before quoting the result.
  DERIVED    A2, A3 are the theory's own definitions. The second is not an input. (sec.1)
  INFERENCE  the sqrt(2pi) values. This is exact algebra ON TOP OF setting A1's O(1)
             coefficient to 1, and that coefficient is precisely the emergent-metric /
             quantum-gravity step listed as OPEN in sec.9. THIS DOES NOT DERIVE G. It sharpens
             "E0, ell0 are ~Planckian" into an exact conditional statement, and it shows the
             floor "absolute E0, ell0" and the floor "Newton's G coefficient" are ONE floor,
             not two.
  NEGATIVE   the units question does NOT explain any standing tension in the program. Both
             live ones are shown below to be unit-immune.
"""
import numpy as np

# CODATA 2018
hbar = 1.054571817e-34      # J s
c    = 2.99792458e8         # m s^-1
G    = 6.67430e-11          # m^3 kg^-1 s^-2
eV   = 1.602176634e-19      # J

SQ2PI = np.sqrt(2 * np.pi)


def hdr(s):
    print("\n" + "=" * 74 + "\n" + s + "\n" + "=" * 74)


hdr("1  DERIVED -- the second is manufactured from the primitives, not imported")
print("  A3: hbar = E0 tau0 / 2pi  =>  tau0 = 2 pi hbar / E0")
print("  A2: ell0 = c tau0")
print("  Given (E0, ell0) the second is fixed. Nothing left to 'correct for'; a unit error")
print("  would appear as a dimensional mismatch, not a tension.")

hdr("2  INFERENCE -- adding G = ell0 c^4/E0 pins the primitives to sqrt(2pi) x Planck")
E_pl = np.sqrt(hbar * c**5 / G)
l_pl = np.sqrt(hbar * G / c**3)
t_pl = np.sqrt(hbar * G / c**5)

E0   = np.sqrt(2 * np.pi * hbar * c**5 / G)     # from G = 2 pi hbar c^5 / E0^2
tau0 = 2 * np.pi * hbar / E0                     # A3
ell0 = c * tau0                                  # A2

print("  {:6s} {:>15s} {:>15s}   {:s}".format("", "TFT", "Planck", "ratio"))
for name, v, p, u in [("E0", E0, E_pl, "J"), ("ell0", ell0, l_pl, "m"), ("tau0", tau0, t_pl, "s")]:
    print("  {:6s} {:15.6e} {:15.6e}   {:.6f}  [{:s}]".format(name, v, p, v / p, u))
    assert abs(v / p - SQ2PI) < 1e-9, name
print("\n  sqrt(2pi) = {:.6f}  -- all three ratios, asserted to 1e-9.".format(SQ2PI))

G_back = 2 * np.pi * hbar * c**5 / E0**2
print("  round-trip: G = 2 pi hbar c^5/E0^2 = {:.6e}  vs CODATA {:.6e}  (rel err {:.1e})"
      .format(G_back, G, abs(G_back / G - 1)))
assert abs(G_back / G - 1) < 1e-12
print("  (the ratios are exactly sqrt(2pi) as ALGEBRA -- independent of the CODATA values.)")

hdr("3  INFERENCE -- 'G = (rate of time)^2 / density' becomes native (cf. verify_G_as_rate.py)")
omega0 = 1.0 / tau0                  # the compact-time cycling rate = the rate of time
rho0   = E0 / (c**2 * ell0**3)       # one phase-quantum per coherence volume, as mass density
print("  omega0 = 1/tau0             = {:.6e} s^-1".format(omega0))
print("  rho0   = E0/(c^2 ell0^3)    = {:.6e} kg m^-3".format(rho0))
print("  omega0^2 / rho0             = {:.6e}   vs G = {:.6e}  (rel err {:.1e})"
      .format(omega0**2 / rho0, G, abs((omega0**2 / rho0) / G - 1)))
assert abs((omega0**2 / rho0) / G - 1) < 1e-12
print("  => holds EXACTLY in TFT's own primitives, with the rate of time being literally the")
print("     INVERSE COMPACT-TIME PERIOD rather than a borrowed Planck frequency. The earlier")
print("     reframing was not a Planck-unit coincidence. (Still conditional on A1.)")

hdr("4  NEGATIVE -- the standing tensions are unit-immune; this does NOT explain them")
H0 = 2.19e-18                                     # s^-1
a0, a0_obs = c * H0 / (2 * np.pi), 1.2e-10
print("  (a) a0 = c H0/2pi -- both sides are RATES read on the SAME clock:")
print("      a0/c = {:.6e} s^-1   H0/2pi = {:.6e} s^-1   (identical)".format(a0 / c, H0 / (2 * np.pi)))
print("      a0_pred/a0_obs = {:.4f}. The residual is DIMENSIONLESS -- no time-unit".format(a0 / a0_obs))
print("      convention moves a ratio of two rates measured on one clock.")

MPC     = 3.0856775814913673e22
H0_cos  = 67.4e3 / MPC
E_H0    = hbar * H0_cos / eV
MPL_RED = np.sqrt(hbar * c**5 / (8 * np.pi * G)) / eV
rho_obs = 0.685 * 3.0 * E_H0**2 * MPL_RED**2      # eV^4, Friedmann
hbarc   = hbar * c / eV                            # eV m
ell0_need = hbarc / (16 * np.pi**2 * rho_obs)**0.25
print("\n  (b) Lambda: rho_vac ~ 1/ell0^4 converts through hbar*c = {:.4e} eV m".format(hbarc))
print("      -- an ENERGY x LENGTH. No second appears anywhere in that conversion.")
print("      ell0 REQUIRED = {:.1f} um   vs   ell0 above = {:.3e} m".format(ell0_need * 1e6, ell0))
print("      ratio = {:.3e}  ({:.0f} orders) -- a ratio of two LENGTHS. Unit-immune."
      .format(ell0_need / ell0, np.log10(ell0_need / ell0)))

print("\n  (c) the uncertainty relation dN * dtheta >= 1/2 (see uncertainty_s1.py) has BOTH")
print("      factors dimensionless. TFT's native conjugate pair carries no second at all;")
print("      hbar enters only on translation to a lab clock.")

hdr("VERDICT")
print("  The second is DERIVED, so there is nothing to make up for. Adding G's dimensional")
print("  form pins the primitives to sqrt(2pi) x Planck exactly -- INFERENCE, contingent on")
print("  the open O(1) coefficient, and NOT a derivation of G. The two live tensions are a")
print("  dimensionless ratio and a length ratio respectively: not unit artifacts.")
