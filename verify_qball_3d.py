"""3D Q-BALL test: does a CHARGE-carrying localized wave persist where the oscillon failed?

Complex field  psi = u + i v  (psi = rho e^{i phase},  rho = |psi| = carrier amplitude).
Lagrangian: |d_t psi|^2 - |grad psi|^2 - V(rho),   U(1)-symmetric potential
    V(rho) = 1/2 rho^2 - rho^4 + rho^6     (m^2 = V''(0) = 1; UNIQUE vacuum at rho=0)
=> F(rho) = V'(rho)/rho = 1 - 4 rho^2 + 6 rho^4
EOM (spherical):  u_tt = lap u - F(rho) u ,   v_tt = lap v - F(rho) v.

A Q-ball is  psi = rho(r) e^{i omega t}  with omega in the existence window (0.707, 1).
Conserved Noether charge  Q = integral (u v_t - v u_t) dV.

A/B test, identical profile and potential:
  charged (omega=0.85): expect a PERSISTENT Q-ball (core energy plateaus, Q conserved).
  uncharged (omega=0)  : unique vacuum + no charge => must radiate (the oscillon story).
The contrast isolates the CHARGE as the stabilizer.
"""
import numpy as np

R_max, dr, dt = 80.0, 0.05, 0.005
r   = np.arange(0.0, R_max + dr/2, dr)
N   = len(r)
vol = 4*np.pi*r**2
R_s, g0 = 55.0, 3.0
gamma   = np.where(r > R_s, g0*((r - R_s)/(R_max - R_s))**2, 0.0)
m_gap   = 1.0

def Vfun(rho2): return 0.5*rho2 - rho2**2 + rho2**3
def Ffun(rho2): return 1.0 - 4.0*rho2 + 6.0*rho2*rho2

def lap(f):
    L = np.empty_like(f)
    L[1:-1] = (f[2:]-2*f[1:-1]+f[:-2])/dr**2 + (2.0/r[1:-1])*(f[2:]-f[:-2])/(2*dr)
    L[0]  = 6.0*(f[1]-f[0])/dr**2
    L[-1] = (2*f[-2]-2*f[-1])/dr**2
    return L

def energy_core(u, v, du, dv, Rcore=15.0):
    ur = np.gradient(u, dr); vr = np.gradient(v, dr)
    dens = 0.5*(du*du+dv*dv) + 0.5*(ur*ur+vr*vr) + Vfun(u*u+v*v)
    mask = r <= Rcore
    return np.trapezoid((dens*vol)[mask], r[mask])

def charge_total(u, v, du, dv):
    return np.trapezoid((u*dv - v*du)*vol, r)

def run(omega, A=0.9, R0=5.0, delta=1.5, T=150.0, rec=40):
    rho0 = A*0.5*(1 - np.tanh((r - R0)/delta))
    u  = rho0.copy(); v  = np.zeros(N)
    du = np.zeros(N); dv = omega*rho0.copy()
    steps = int(T/dt)
    ts, Ec, Qs, rc, ph = [], [], [], [], []
    for s in range(steps):
        rho2 = u*u+v*v; F = Ffun(rho2)
        au = lap(u) - F*u - gamma*du
        av = lap(v) - F*v - gamma*dv
        du += 0.5*dt*au; dv += 0.5*dt*av
        u += dt*du; v += dt*dv
        rho2 = u*u+v*v; F = Ffun(rho2)
        au = lap(u) - F*u - gamma*du
        av = lap(v) - F*v - gamma*dv
        du += 0.5*dt*au; dv += 0.5*dt*av
        if s % rec == 0:
            ts.append(s*dt); Ec.append(energy_core(u,v,du,dv))
            Qs.append(charge_total(u,v,du,dv))
            rc.append(np.sqrt(u[0]**2+v[0]**2)); ph.append(np.arctan2(v[0], u[0]))
    return (np.array(ts), np.array(Ec), np.array(Qs), np.array(rc), np.array(ph))

def at(ts, arr, t): return arr[np.argmin(np.abs(ts - t))]

sample_t = [2, 10, 30, 60, 100, 149]
print(f"mass gap m = {m_gap}   Q-ball window omega in (0.707, 1)\n")

for label, omega in [("CHARGED  omega=0.85", 0.85), ("UNCHARGED omega=0", 0.0)]:
    ts, Ec, Qs, rc, ph = run(omega)
    E0 = Ec[0]
    print(f"=== {label} ===   E_core(0)={E0:.3f}   Q(0)={Qs[0]:.3f}")
    print(f"   {'t':>5s} {'rho(0)':>8s} {'E_core':>9s} {'E/E0':>7s} {'Q_total':>9s}")
    for t in sample_t:
        print(f"   {t:5d} {at(ts,rc,t):8.4f} {at(ts,Ec,t):9.3f} "
              f"{at(ts,Ec,t)/E0:7.3f} {at(ts,Qs,t):9.3f}")
    persist = at(ts, Ec, 149)/max(at(ts, Ec, 30), 1e-9)
    # phase-rotation frequency from unwrapped core phase (late window)
    k = len(ts)//2
    if omega > 0 and len(ts) - k > 3:
        pu = np.unwrap(ph[k:]); slope = np.polyfit(ts[k:], pu, 1)[0]
        om_meas = abs(slope)
        qcons = at(ts, Qs, 149)/max(at(ts, Qs, 30), 1e-9)
        print(f"   persistence E(149)/E(30) = {persist:.3f}   "
              f"phase freq = {om_meas:.4f} (set {omega})   Q(149)/Q(30) = {qcons:.3f}")
    else:
        print(f"   persistence E(149)/E(30) = {persist:.3f}")
    print()
