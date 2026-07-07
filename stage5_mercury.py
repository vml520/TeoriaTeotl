"""Stage 5 — perihelion precession from the TFT metric term (baseline-subtracted).

Newtonian part (frozen): a = -K r/r^3,  K = 4*pi^2  (1 AU -> 1 yr calibration).
c is derived in TFT; here it is the physical value in AU/yr.

The velocity-Verlet integrator has its own small numerical perihelion drift. It is identical
with and without the (tiny) physical perturbation, so we measure it (Newtonian-only run) and
SUBTRACT it. Physical precession = measured(perturbed) - measured(Newtonian).

Two constructions for the metric term:
  (B) standard weak-field metric (spatial curvature ∝ Φ ∝ 1/r): parameter-free.
        a = -(K/r^2)[1 + 3 h^2/(c^2 r^2)] r_hat.   c derived, K frozen. NO free constant.
  (A) literal |∇θ|^2 ∝ 1/r^4 potential: δΦ = α/r^4. α is a SECOND free constant.
        Shape test: ratios (planet/Mercury) are α-independent — compare their SHAPE to GR.
"""
import numpy as np

K  = 4*np.pi**2
c  = 299792458.0*3.15576e7/1.495978707e11          # AU/yr (derived scale)
print(f"derived c = {c:.1f} AU/yr\n")

def precession(a_sma, e, mode, alpha=0.0, n_orbits=25, spp=30000):
    r_p = a_sma*(1-e); v_p = np.sqrt(K*(1+e)/r_p)
    p = np.array([r_p, 0.0]); v = np.array([0.0, v_p])
    dt = (a_sma**1.5)/spp
    def accel(p, v):
        r = np.hypot(p[0], p[1]); aN = -K*p/r**3
        if mode == 'newton': return aN
        if mode == 'B':
            h = p[0]*v[1]-p[1]*v[0]; return aN*(1.0 + 3.0*h*h/(c*c*r*r))
        if mode == 'A':
            return aN + (4.0*alpha/r**5)*(p/r)
    a = accel(p, v); ang=[]; ts=[]; t=0.0
    for i in range(int(n_orbits*spp)):
        v = v + 0.5*dt*a; p = p + dt*v; a = accel(p, v); v = v + 0.5*dt*a; t += dt
        if i % 50 == 0:
            r = np.hypot(p[0],p[1]); h = p[0]*v[1]-p[1]*v[0]
            Ax = v[1]*h - K*p[0]/r; Ay = -v[0]*h - K*p[1]/r
            ang.append(np.arctan2(Ay, Ax)); ts.append(t)
    ang = np.unwrap(np.array(ang)); ts = np.array(ts)
    return np.polyfit(ts, ang, 1)[0]*100.0*(180/np.pi)*3600.0   # arcsec/century

planets = [("Mercury",0.38710,0.20563,42.98),
           ("Venus",  0.72333,0.00677, 8.62),
           ("Earth",  1.00000,0.01671, 3.84),
           ("Mars",   1.52371,0.09341, 1.35)]

print("=== Construction B: standard weak-field metric (parameter-free) ===")
print("  " + "{:>8s} {:>10s} {:>10s} {:>12s} {:>12s} {:>7s}".format(
      "planet","numfloor","B raw","B - floor","GR obs","ratio"))
for nm,a_sma,e,gr in planets:
    fl = precession(a_sma,e,'newton'); b = precession(a_sma,e,'B'); phys = b-fl
    print("  " + "{:>8s} {:>10.3f} {:>10.3f} {:>12.3f} {:>12.2f} {:>7.3f}".format(
          nm, fl, b, phys, gr, phys/gr))

print("\n=== Construction A: literal 1/r^4 term — SHAPE test (ratios normalized to Mercury) ===")
alpha = 1e-4
Aphys = {}
for nm,a_sma,e,gr in planets:
    fl = precession(a_sma,e,'newton'); aa = precession(a_sma,e,'A',alpha=alpha)
    Aphys[nm] = aa-fl
base = Aphys["Mercury"]; grbase = 42.98
print("  " + "{:>8s} {:>16s} {:>16s}".format("planet","A ratio/Merc","GR ratio/Merc"))
for nm,a_sma,e,gr in planets:
    print("  " + "{:>8s} {:>16.4f} {:>16.4f}".format(nm, Aphys[nm]/base, gr/grbase))
