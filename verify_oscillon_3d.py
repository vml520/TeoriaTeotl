"""3D sine-Gordon OSCILLON test: does a localized time-periodic wave persist in 3D?

Spherically-symmetric EOM:  theta_tt = theta_rr + (2/r) theta_r - Lambda sin(theta)
Units E0=l0=c=1, m=sqrt(Lambda), mass gap omega_m = m.

3D is NOT integrable, so there is no exact eternal solution (unlike the 1D breather).
The question is quantitative: launch a localized bump, absorb outgoing radiation with a
sponge, and measure whether a persistent oscillating core remains.

A genuine oscillon:
  - core energy drops during an initial transient (sheds radiation), then PLATEAUS
  - survivor oscillates at omega < omega_m (inside the mass gap -> can't radiate at
    its fundamental, which is why it lives long)
If instead the core energy drains toward 0, the wave does not survive in 3D.

Diagnostic per initial bump theta(r,0)=A exp(-(r/w)^2), theta_t(r,0)=0.
"""
import numpy as np

Lam    = 1.0
m      = np.sqrt(Lam)
om_gap = m

R_max, dr, dt = 80.0, 0.05, 0.005
r   = np.arange(0.0, R_max + dr/2, dr)
N   = len(r)
vol = 4*np.pi*r**2

# absorbing sponge in the outer layer (leaves the core region untouched)
R_s, g0 = 55.0, 3.0
gamma   = np.where(r > R_s, g0*((r - R_s)/(R_max - R_s))**2, 0.0)

def laplacian(th):
    lap = np.empty_like(th)
    lap[1:-1] = (th[2:]-2*th[1:-1]+th[:-2])/dr**2 \
                + (2.0/r[1:-1])*(th[2:]-th[:-2])/(2*dr)
    lap[0]  = 6.0*(th[1]-th[0])/dr**2          # regular origin: lap = 3*theta_rr
    lap[-1] = (2*th[-2]-2*th[-1])/dr**2
    return lap

def energy_core(th, v, Rcore=15.0):
    thr  = np.gradient(th, dr)
    dens = 0.5*v**2 + 0.5*thr**2 + Lam*(1-np.cos(th))
    mask = r <= Rcore
    return np.trapezoid((dens*vol)[mask], r[mask])

def envelope_at(h, t, half=6.0):
    i = int(t/dt); w = int(half/dt)
    lo, hi = max(0, i-w), min(len(h), i+w)
    return np.max(np.abs(h[lo:hi]))

def freq_late(h, frac=0.55):
    seg = h[int(len(h)*frac):].copy()
    seg -= seg.mean()
    sgn = np.sign(seg); sgn[sgn == 0] = 1
    idx = np.where(np.diff(sgn) != 0)[0]
    if len(idx) < 3:
        return float('nan')
    return 2*np.pi/(2*np.mean(np.diff(idx))*dt)

def run(A, w, T=150.0, rec_every=40):
    th = A*np.exp(-(r/w)**2)
    v  = np.zeros(N)
    steps = int(T/dt)
    h  = np.empty(steps)
    Ec_t, Ec_v = [], []
    for s in range(steps):
        acc = laplacian(th) - Lam*np.sin(th) - gamma*v
        v  += dt*acc
        th += dt*v
        h[s] = th[0]
        if s % rec_every == 0:
            Ec_t.append(s*dt); Ec_v.append(energy_core(th, v))
    return h, np.array(Ec_t), np.array(Ec_v)

def Ec_at(Ec_t, Ec_v, t):
    return Ec_v[np.argmin(np.abs(Ec_t - t))]

print(f"mass gap omega_m = {om_gap:.3f}   sponge at r>{R_s}   R_max={R_max}\n")
sample_t = [2, 10, 30, 60, 100, 149]

for A, w in [(1.5, 3.0), (2.5, 3.0), (3.5, 3.0)]:
    h, Ec_t, Ec_v = run(A, w)
    Ec0 = Ec_v[0]
    print(f"=== bump A={A}, w={w} ===   E_core(0) = {Ec0:.3f}")
    print(f"   {'t':>5s} {'amp|th0|':>9s} {'E_core':>9s} {'E/E0':>7s}")
    for t in sample_t:
        ec = Ec_at(Ec_t, Ec_v, t)
        print(f"   {t:5d} {envelope_at(h, t):9.4f} {ec:9.3f} {ec/Ec0:7.3f}")
    wl = freq_late(h)
    tag = 'BELOW gap (oscillon-like)' if wl < om_gap else 'at/above gap (radiating)'
    # persistence: compare late plateau to post-transient level (t~30)
    plateau = Ec_at(Ec_t, Ec_v, 149) / max(Ec_at(Ec_t, Ec_v, 30), 1e-9)
    print(f"   late-time freq = {wl:.4f}   omega_m = {om_gap:.3f}   omega/omega_m = {wl/om_gap:.3f}   {tag}")
    print(f"   persistence E(149)/E(30) = {plateau:.3f}")
    print()
