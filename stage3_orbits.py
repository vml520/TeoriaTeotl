"""Stage 3/4 — planetary paths from the TFT force law (simplest version).

TFT primitives: E0 = l0 = 1  =>  g_eff = E0/l0 = 1.
A central mass sources the harmonic phase dressing  theta(r) = -A/r  (point defect, del^2 theta = 0).
Force on a test body (paper Ch.7,11):  F = -g_eff * grad(theta)  =>  a = -(g_eff*A) r_vec / r^3.

So the Newtonian potential IS the phase field:  Phi(r) = g_eff*theta(r) = -K/r,  K = g_eff*A.
K is the ONE calibration constant. Fix it once so a circular orbit at r=1 (=1 AU) has period 1
(=1 year), then FREEZE it.  For that:  v_circ = sqrt(K/r), T = 2*pi*r^{3/2}/sqrt(K); T(1)=1 => K=4*pi^2.

This reproduces Kepler BY CONSTRUCTION (as the SPEC notes, it tests the integrator + wiring, not
new physics). The genuine beyond-Newton TFT prediction — Mercury precession from the |grad theta|^2
metric term — is the NEXT step. Here we verify the skeleton: closed ellipses, Kepler III, real periods.
Integrator: velocity Verlet (symplectic).
"""
import numpy as np

# ---- TFT scales ----
E0 = 1.0; l0 = 1.0
g_eff = E0/l0
K = 4*np.pi**2            # = g_eff * A ; calibration constant (1 AU -> 1 yr), FROZEN

def accel(p):
    r = np.sqrt(p[0]*p[0] + p[1]*p[1])
    return -K*p/r**3

def energy(p, v):
    return 0.5*(v[0]**2+v[1]**2) - K/np.sqrt(p[0]**2+p[1]**2)

def step(p, v, a, dt):
    v = v + 0.5*dt*a
    p = p + dt*v
    a = accel(p)
    v = v + 0.5*dt*a
    return p, v, a

def measure_period(a_sma, dt_frac=2e-5):
    """Circular orbit at radius a_sma; measure the period by accumulating orbital angle to 2*pi."""
    v_c = np.sqrt(K/a_sma)
    p = np.array([a_sma, 0.0]); v = np.array([0.0, v_c])
    dt = (a_sma**1.5)*dt_frac
    acc = accel(p)
    cum = 0.0; ang_prev = 0.0; t = 0.0
    while cum < 2*np.pi and t < 20*a_sma**1.5:
        p, v, acc = step(p, v, acc, dt); t += dt
        ang = np.arctan2(p[1], p[0])
        d = ang - ang_prev
        if d < -np.pi: d += 2*np.pi
        elif d > np.pi: d -= 2*np.pi
        cum += d; ang_prev = ang
    return t

# ---- Test 1: calibration ----
print("=== Test 1: calibration (1 AU -> 1 year) ===")
T1 = measure_period(1.0)
print(f"  circular orbit at r=1 AU: measured period = {T1:.6f} yr   (target 1.000000)\n")

# ---- Test 2: Kepler's third law ----
print("=== Test 2: Kepler III  (T^2 / a^3 should be constant = 1) ===")
print(f"  {'a (AU)':>8s} {'T meas (yr)':>12s} {'a^1.5':>10s} {'T^2/a^3':>10s}")
for a_sma in [0.387, 1.0, 5.203, 30.07]:
    T = measure_period(a_sma)
    print(f"  {a_sma:8.3f} {T:12.5f} {a_sma**1.5:10.5f} {T*T/a_sma**3:10.6f}")
print()

# ---- Test 3: closed ellipse + energy conservation + spurious precession ----
print("=== Test 3: eccentric orbit (a=1, e=0.3) — closure, energy, precession ===")
a_sma, e = 1.0, 0.3
r_p = a_sma*(1-e)
v_p = np.sqrt(K*(1+e)/r_p)          # vis-viva at perihelion
p = np.array([r_p, 0.0]); v = np.array([0.0, v_p])
dt = (a_sma**1.5)*2e-5
acc = accel(p)
E_start = energy(p, v)
peri_angles = []; r_prev2 = r_prev1 = None; t = 0.0
n_orbits_target = 20
while len(peri_angles) < n_orbits_target and t < 40:
    p, v, acc = step(p, v, acc, dt); t += dt
    r = np.sqrt(p[0]**2+p[1]**2)
    if r_prev1 is not None and r_prev2 is not None:
        if r_prev1 < r_prev2 and r_prev1 < r:          # local min of r = perihelion
            peri_angles.append(np.degrees(np.arctan2(p_prev1[1], p_prev1[0])))
    r_prev2, r_prev1, p_prev1 = r_prev1, r, p.copy()
E_end = energy(p, v)
peri = np.array(peri_angles)
drift_per_orbit = np.mean(np.diff(peri)) if len(peri) > 1 else float('nan')
print(f"  perihelion direction over {len(peri)} orbits: first={peri[0]:+.4f} deg  last={peri[-1]:+.4f} deg")
print(f"  spurious precession = {drift_per_orbit*3600:+.3f} arcsec/orbit  (should be ~0 for pure 1/r)")
print(f"  energy drift over run: {abs(E_end-E_start)/abs(E_start):.2e}\n")

# ---- Test 4: the real solar system ----
print("=== Test 4: 8 planets, real semi-major axes -> periods from the TFT field ===")
names = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
a_real = [0.387, 0.723, 1.000, 1.524, 5.203, 9.537, 19.191, 30.07]
T_real = [0.241, 0.615, 1.000, 1.881, 11.862, 29.457, 84.011, 164.79]
print(f"  {'planet':>8s} {'a (AU)':>8s} {'T TFT (yr)':>11s} {'T real (yr)':>12s} {'err %':>7s}")
for nm, a_sma, Tr in zip(names, a_real, T_real):
    T = measure_period(a_sma)
    print(f"  {nm:>8s} {a_sma:8.3f} {T:11.4f} {Tr:12.3f} {100*(T-Tr)/Tr:+7.2f}")
