"""Confirm the kink force-law SIGN in the conservative sine-Gordon EOM.
Claim under test:  a = -2*pi*f*Q / M_K, where Q = topological charge, M_K = 8 sqrt(Lambda).
Units E0=l0=c=1.  EOM: theta_tt = theta_xx - Lambda sin(theta) + f
"""
import numpy as np

Lam = 1.0
Mk  = 8*np.sqrt(Lam)
L_box, dx, dt = 160.0, 0.05, 0.02
x = np.arange(-L_box/2, L_box/2, dx)
N = len(x)

def lap(u):
    out = np.empty_like(u)
    out[1:-1] = (u[2:]-2*u[1:-1]+u[:-2])/dx**2
    out[0] = out[1]; out[-1] = out[-2]
    return out

def measure_accel(th0, f, steps=3000):
    th = th0.copy(); v = np.zeros(N); t = 0.0
    Ts, Xs = [], []
    for step in range(steps):
        acc = lap(th) - Lam*np.sin(th) + f
        v += dt*acc; th += dt*v; t += dt
        if step % 50 == 0:
            i = np.argmin(np.abs(th - np.pi))
            if 0 < i < N-1 and th[i+1] != th[i-1]:
                X = x[i] + (np.pi-th[i])*(2*dx)/(th[i+1]-th[i-1])
            else:
                X = x[i]
            Ts.append(t); Xs.append(X)
    coef = np.polyfit(np.array(Ts), np.array(Xs), 2)
    return 2*coef[0]

kink     = 4*np.arctan(np.exp( x))   # Q = +1  (theta: 0 -> 2pi)
antikink = 4*np.arctan(np.exp(-x))   # Q = -1  (theta: 2pi -> 0)

cases = [
    ("kink Q=+1, f=+0.005", kink,     +0.005, +1),
    ("kink Q=+1, f=-0.005", kink,     -0.005, +1),
    ("antik Q=-1, f=+0.005", antikink,+0.005, -1),
]
print(f"{'case':24s} {'a_meas':>10s} {'a_pred=-2pi f Q/M':>18s} {'rel.err':>9s}")
for name, th0, f, Q in cases:
    a_meas = measure_accel(th0, f)
    a_pred = -2*np.pi*f*Q/Mk
    rel = abs(a_meas - a_pred)/abs(a_pred)
    print(f"{name:24s} {a_meas:+10.6f} {a_pred:+18.6f} {rel:9.2e}")
