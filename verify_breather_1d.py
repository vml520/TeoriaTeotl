"""1D sine-Gordon BREATHER — a time-periodic localized 'particle-wave'.

Units E0=l0=c=1, m = sqrt(Lambda).  EOM: theta_tt = theta_xx - Lambda sin(theta).

Exact breather (rest frame), internal frequency w in (0,1):
    theta(x,t) = 4 arctan[ (sqrt(1-w^2)/w) * sin(w m t) / cosh(sqrt(1-w^2) m x) ]

At t=0 this is  theta=0  with a pure velocity profile
    theta_t(x,0) = 4 m beta / cosh(m beta x),   beta = sqrt(1-w^2)
so the whole rest energy is KINETIC at t=0 — the mass is in the motion.

Predictions:
    oscillation frequency  Omega = w * sqrt(Lambda)
    rest mass  M_b = 2 M_k sqrt(1-w^2) = 16 sqrt(Lambda) sqrt(1-w^2),   M_k = 8 sqrt(Lambda)
    => M_b < 2 M_k always, tunable by frequency.

Tests: (1) E(0) == M_b and E conserved,  (2) stays localized,  (3) frequency == Omega.
Evolution: velocity-Verlet (symplectic).
"""
import numpy as np

Lam = 1.0
m   = np.sqrt(Lam)
Mk  = 8*m

L_box, dx, dt = 120.0, 0.05, 0.01
x = np.arange(-L_box/2, L_box/2, dx)
N = len(x)

def lap(u):
    out = np.empty_like(u)
    out[1:-1] = (u[2:]-2*u[1:-1]+u[:-2])/dx**2
    out[0]=out[1]; out[-1]=out[-2]
    return out

def energy(th, v):
    thx = np.gradient(th, dx)
    dens = 0.5*v**2 + 0.5*thx**2 + Lam*(1-np.cos(th))
    return np.trapezoid(dens, x)

def local_fraction(th, v, halfwidth=8.0):
    thx = np.gradient(th, dx)
    dens = 0.5*v**2 + 0.5*thx**2 + Lam*(1-np.cos(th))
    tot  = np.trapezoid(dens, x)
    mask = np.abs(x) <= halfwidth
    return np.trapezoid(dens[mask], x[mask]) / tot

print(f"{'w':>4s} {'M_b pred':>9s} {'E(0)':>9s} {'E(end)':>9s} {'E drift':>9s} "
      f"{'loc frac':>9s} {'Om meas':>9s} {'Om pred':>9s} {'rel.err':>8s}")

for w in [0.3, 0.6, 0.9]:
    beta = np.sqrt(1 - w**2)
    th = np.zeros(N)
    v  = 4*m*beta/np.cosh(m*beta*x)          # exact breather IC (theta=0, pure velocity)
    Mb_pred = 2*Mk*beta
    E0      = energy(th, v)
    Om_pred = w*m
    T       = 2*np.pi/Om_pred
    steps   = int(6*T/dt)                     # evolve ~6 periods

    center, tgrid, loc_min = [], [], 1.0
    t = 0.0
    for s in range(steps):
        acc = lap(th) - Lam*np.sin(th); v += 0.5*dt*acc
        th += dt*v
        acc = lap(th) - Lam*np.sin(th); v += 0.5*dt*acc
        t += dt
        center.append(th[N//2]); tgrid.append(t)
        if s % 200 == 0:
            loc_min = min(loc_min, local_fraction(th, v))

    Eend = energy(th, v)
    loc  = local_fraction(th, v)

    # frequency from zero-crossings of the center signal (resolution-independent)
    c   = np.array(center); c = c - c.mean()
    sgn = np.sign(c); sgn[sgn == 0] = 1
    idx = np.where(np.diff(sgn) != 0)[0]
    tc  = np.array(tgrid)[idx]
    if len(tc) >= 3:
        Tfull   = 2*np.mean(np.diff(tc))       # two zero-crossings per period
        Om_meas = 2*np.pi/Tfull
    else:
        Om_meas = float('nan')
    rel = abs(Om_meas - Om_pred)/Om_pred

    print(f"{w:4.1f} {Mb_pred:9.4f} {E0:9.4f} {Eend:9.4f} {abs(Eend-E0)/E0:9.2e} "
          f"{min(loc,loc_min):9.4f} {Om_meas:9.4f} {Om_pred:9.4f} {rel:8.2e}")
