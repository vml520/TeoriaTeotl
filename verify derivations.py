"""Numerical verification of the corrected TFT derivations (1D sector).
Units: E0 = l0 = c = 1, so kappa_1 = E0*l0 = 1, omega_m = sqrt(L)*c/l0.
EOM from corrected action:  theta_tt = c^2 theta_xx - (L c^2/l0^2) sin(theta) + f*c^2/kappa
"""
import numpy as np

# ── Check 1: kink rest energy  E_kink = 8 sqrt(Lambda) E0 ────────────────────
for Lam in [0.5, 1.0, 2.0]:
    w  = 1.0/np.sqrt(Lam)                       # kink width l0/sqrt(Lambda)
    x  = np.linspace(-40, 40, 400001)
    th = 4*np.arctan(np.exp(x/w))
    dth= np.gradient(th, x)
    dens = 0.5*dth**2 + Lam*(1-np.cos(th))      # kappa_1 = 1
    E  = np.trapezoid(dens, x)
    print(f"Lambda={Lam:4.1f}:  E_kink = {E:.6f}   predicted 8*sqrt(L) = {8*np.sqrt(Lam):.6f}   "
          f"rel.err = {abs(E-8*np.sqrt(Lam))/(8*np.sqrt(Lam)):.2e}")

# ── Check 2: force law  F = 2*pi*f  →  a = 2*pi*f / M_K ─────────────────────
Lam, f = 1.0, 0.005
Mk     = 8*np.sqrt(Lam)
a_pred = 2*np.pi*f/Mk

L_box, dx = 160.0, 0.05
x  = np.arange(-L_box/2, L_box/2, dx)
N  = len(x)
th = 4*np.arctan(np.exp(x))                     # kink at 0
v  = np.zeros(N)
dt = 0.02
def lap(u):
    out = np.empty_like(u)
    out[1:-1] = (u[2:]-2*u[1:-1]+u[:-2])/dx**2
    out[0] = out[1]; out[-1] = out[-2]
    return out

Ts, Xs = [], []
t = 0.0
for step in range(3000):
    acc = lap(th) - Lam*np.sin(th) + f
    v  += dt*acc
    th += dt*v
    t  += dt
    if step % 50 == 0:
        # kink center: theta = pi crossing
        i = np.argmin(np.abs(th - np.pi))
        # linear interpolation
        if 0 < i < N-1 and th[i+1] != th[i-1]:
            X = x[i] + (np.pi-th[i])*(2*dx)/(th[i+1]-th[i-1])
        else:
            X = x[i]
        Ts.append(t); Xs.append(X)

Ts, Xs = np.array(Ts), np.array(Xs)
coef = np.polyfit(Ts, Xs, 2)        # X = 0.5 a t^2 + ...
a_meas = 2*coef[0]
print(f"\nForce law:  a_measured = {a_meas:.6f}   a_predicted = 2πf/M_K = {a_pred:.6f}   "
      f"rel.err = {abs(a_meas-a_pred)/a_pred:.2e}")

# ── Check 3: Option B spectrum — compact time forces omega_n = n*omega0 ─────
# Linearized modes: omega^2 = c^2 k^2 + omega_m^2 ; with t-periodicity tau0,
# allowed omega = n*omega0. Verify numerically: evolve small fluctuation on
# periodic time? (Analytic statement; we verify dispersion relation instead.)
Lam = 1.0
k_test = 0.7
om_pred = np.sqrt(k_test**2 + Lam)
# evolve small plane-wave perturbation, measure oscillation frequency
th = 0.001*np.cos(k_test*x)
v  = np.zeros(N)
amp = []
for step in range(4000):
    acc = lap(th) - Lam*np.sin(th)
    v += dt*acc; th += dt*v
    amp.append(th[N//2])
amp = np.array(amp)
freqs = np.fft.rfftfreq(len(amp), d=dt)*2*np.pi
om_meas = freqs[1:][np.argmax(np.abs(np.fft.rfft(amp-amp.mean()))[1:])]
print(f"Dispersion: omega_measured = {om_meas:.4f}   sqrt(c²k²+ω_m²) = {om_pred:.4f}   "
      f"rel.err = {abs(om_meas-om_pred)/om_pred:.2e}")
