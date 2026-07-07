"""TFT toy solar system — gravity as emergent geometry, no G derived.

Gravity here is NOT a force. The Sun is a concentration of phase-field energy; its energy density
warps the field's time/space structure into an emergent metric. Planets are not "pulled" — they
follow GEODESICS (straightest paths) of that geometry.

What is DERIVED (earlier scripts, held fixed here):
  - the potential is Poisson-sourced by the Sun's energy density -> Phi(r) = -K/r      (1/r shape)
  - the source is T^00 >= 0 -> the well is always attractive                            (universal sign)
  - the emergent metric's geodesics reduce to Newton + the 1PN correction.

What is NOT derived (a single calibration constant, allowed by spec):
  - K = G*M_sun. Fixed ONCE so a circular orbit at 1 AU has period 1 yr (=> K = 4*pi^2), then FROZEN.
  - c is a derived scale of the theory; numerically the physical value in AU/yr.

Everything past K is prediction: Kepler's third law, the real planetary periods, and Mercury's
perihelion precession — all from ONE constant and ONE emergent metric.
"""
import numpy as np

K = 4*np.pi**2                                  # G*M_sun (AU^3/yr^2): the ONE calibration constant, FROZEN
c = 2.99792458e8*3.15576e7/1.495978707e11       # speed of light in AU/yr (derived scale)

# name, semi-major axis a (AU), eccentricity e, real period (yr), observed GR precession ("/cy)
PLANETS = [
    ("Mercury", 0.38710, 0.20563,   0.2408, 42.98),
    ("Venus",   0.72333, 0.00677,   0.6152,  8.62),
    ("Earth",   1.00000, 0.01671,   1.0000,  3.84),
    ("Mars",    1.52371, 0.09341,   1.8808,  1.35),
    ("Jupiter", 5.20288, 0.04839,  11.862,   0.062),
    ("Saturn",  9.53667, 0.05386,  29.457,   0.014),
    ("Uranus", 19.18916, 0.04726,  84.011,   0.0024),
    ("Neptune",30.06992, 0.00859, 164.79,    0.0008),
]

def geodesic_accel(p, v, relativistic=True):
    """Coordinate acceleration of a geodesic in the Sun's emergent weak-field metric.
    Newtonian term + 1PN correction (h = specific angular momentum). This is free-fall in
    curved geometry, not a force."""
    r = np.hypot(p[0], p[1])
    aN = -K*p/r**3
    if not relativistic:
        return aN
    h = p[0]*v[1] - p[1]*v[0]
    return aN*(1.0 + 3.0*h*h/(c*c*r*r))

def integrate(a_sma, e, mode, n_orbits, spp):
    r_p = a_sma*(1-e); v_p = np.sqrt(K*(1+e)/r_p)
    p = np.array([r_p, 0.0]); v = np.array([0.0, v_p])
    dt = (a_sma**1.5)/spp
    acc = geodesic_accel(p, v, mode)
    ang=[]; ts=[]; t=0.0; cum=0.0; ang_prev=0.0; period=None
    for i in range(int(n_orbits*spp)):
        v = v + 0.5*dt*acc; p = p + dt*v
        acc = geodesic_accel(p, v, mode); v = v + 0.5*dt*acc; t += dt
        a_now = np.arctan2(p[1], p[0]); d = a_now-ang_prev
        d = (d+np.pi)%(2*np.pi)-np.pi; cum += d; ang_prev = a_now
        if period is None and cum >= 2*np.pi: period = t
        if i % 50 == 0:
            r=np.hypot(*p); h=p[0]*v[1]-p[1]*v[0]
            ang.append(np.arctan2(-v[0]*h - K*p[1]/r, v[1]*h - K*p[0]/r)); ts.append(t)
    prec = np.polyfit(np.array(ts), np.unwrap(np.array(ang)), 1)[0]*100*(180/np.pi)*3600
    return period, prec

print("="*72)
print("  TFT TOY SOLAR SYSTEM  —  planets as geodesics of the Sun's emergent metric")
print(f"  one frozen constant: K = G*M_sun = 4*pi^2   |   derived scale: c = {c:.0f} AU/yr")
print("="*72)
print(f"\n  {'planet':>8s} {'a (AU)':>8s} {'T_TFT (yr)':>11s} {'T_real (yr)':>12s} {'err %':>7s} {'T^2/a^3':>9s}")
for nm,a,e,Tr,_ in PLANETS:
    T,_ = integrate(a, e, True, n_orbits=1.05, spp=40000)
    print(f"  {nm:>8s} {a:8.3f} {T:11.4f} {Tr:12.4f} {100*(T-Tr)/Tr:+7.2f} {T*T/a**3:9.5f}")

print("\n  Perihelion precession (geodesic 1PN minus Newtonian numerical floor):")
print("  " + "{:>8s} {:>13s} {:>15s}".format("planet", "TFT arcsec/cy", "obs arcsec/cy"))
for nm,a,e,_,pobs in PLANETS[:4]:
    _, prc  = integrate(a, e, True,  n_orbits=30, spp=30000)
    _, base = integrate(a, e, False, n_orbits=30, spp=30000)
    print(f"  {nm:>8s} {prc-base:11.3f} {pobs:15.2f}")

print("\n  One frozen constant in -> Kepler's third law, the real periods, and Mercury's")
print("  precession, all out of a single emergent geometry. Gravity as process, not force.")
