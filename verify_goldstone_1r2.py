"""Broken-symmetry U(1): does the massless Goldstone mediate a 1/r^2 force?

Complex field psi = rho e^{i theta}, Mexican-hat potential
    V(rho) = (lam/4)(rho^2 - v^2)^2      => vacuum at rho=v, phase theta is MASSLESS.
Amplitude mass m_rho = sqrt(2 lam) v (short range, as always).
Phase = Goldstone (massless) => a localized phase source should give a LONG-range field.

PART A  (nonlinear, the real test)
  Spherically-symmetric radial phase source of fixed flux C:  r^2 rho^2 theta' = C.
  Static amplitude eq:  rho'' + (2/r) rho' = C^2/(r^4 rho^3) + lam rho(rho^2 - v^2).
  Relax rho(r); then theta'(r) = C/(r^2 rho^2).
  If rho heals to v, theta'(r) -> C/(v^2 r^2)  ~  1/r^2  (Newtonian force falloff),
  and the potential theta(r) ~ 1/r.  Measure the exponent over a decade.

PART B  (linear contrast: why breaking matters)
  Massless mediator  ∇^2 phi = 0           -> phi ~ 1/r     (power law)
  Massive  mediator  ∇^2 phi - m^2 phi = 0 -> phi ~ e^{-mr}/r (Yukawa, screened)
  Same geometry/BCs; shows the massive case (what Stage 2 / sine-Gordon had) is screened.
"""
import numpy as np

lam, v = 1.0, 1.0
m_rho  = np.sqrt(2*lam)*v

R0, R_max, dr = 1.0, 60.0, 0.02
r = np.arange(R0, R_max + dr/2, dr)
N = len(r)

def lap(f, inner='neumann'):
    L = np.empty_like(f)
    L[1:-1] = (f[2:]-2*f[1:-1]+f[:-2])/dr**2 + (2.0/r[1:-1])*(f[2:]-f[:-2])/(2*dr)
    if inner == 'neumann':
        L[0] = 2*(f[1]-f[0])/dr**2          # f'(R0)=0
    else:
        L[0] = 0.0                          # Dirichlet inner (handled outside)
    L[-1] = 0.0
    return L

def loglog_slope(x, y, lo, hi):
    m = (x >= lo) & (x <= hi) & (y > 0)
    return np.polyfit(np.log(x[m]), np.log(y[m]), 1)[0]

# ── PART A: nonlinear broken-symmetry monopole ──────────────────────────────
C     = 0.5
gamma = 0.6
dt    = 0.008
steps = 60000

rho = np.full(N, v)
vel = np.zeros(N)
for s in range(steps):
    rho = np.clip(rho, 0.05, None)
    src = C**2/(r**4 * rho**3)
    acc = lap(rho) - src - lam*rho*(rho**2 - v**2) - gamma*vel
    acc[-1] = 0.0
    vel += dt*acc; vel[-1] = 0.0
    rho += dt*vel; rho[-1] = v

thp   = C/(r**2 * rho**2)                    # theta'(r)  = the force field
# potential theta(r): integrate inward from R_max with theta(R_max)=0
theta = np.zeros(N)
for i in range(N-2, -1, -1):
    theta[i] = theta[i+1] - 0.5*(thp[i]+thp[i+1])*dr

sl_force = loglog_slope(r, thp,           3.0, 30.0)
sl_pot   = loglog_slope(r, np.abs(theta), 3.0, 30.0)
heal     = loglog_slope(r, np.abs(rho-v)+1e-15, 3.0, 8.0)  # amplitude healing (Yukawa->steep)

print("=== PART A: nonlinear broken-symmetry monopole (massless phase) ===")
print(f"  lam={lam} v={v}  m_rho={m_rho:.3f}  flux C={C}")
print(f"  rho(core R0)={rho[0]:.4f}   rho(far)={rho[-1]:.4f}   "
      f"(healed to v => phase is clean Goldstone)")
print(f"  {'r':>6s} {'rho':>8s} {'theta_prime':>12s} {'theta(pot)':>11s}")
for rr in [2, 3, 5, 10, 20, 30, 50]:
    i = np.argmin(np.abs(r-rr))
    print(f"  {r[i]:6.1f} {rho[i]:8.4f} {thp[i]:12.5e} {theta[i]:11.4e}")
print(f"  FORCE  theta'(r) log-log slope over [3,30] = {sl_force:+.3f}   (Newtonian = -2)")
print(f"  POTENTIAL theta(r) slope over [3,30]       = {sl_pot:+.3f}   (Newtonian = -1)")
print()

# ── PART B: linear massless vs massive Green's functions (same geometry) ────
def green(mass2, gamma=0.6, dt=0.01, steps=40000):
    phi = np.exp(-(r-R0)); phi[-1] = 0.0
    w   = np.zeros(N)
    for s in range(steps):
        acc = lap(phi, inner='dirichlet') - mass2*phi - gamma*w
        acc[0] = 0.0; acc[-1] = 0.0                 # phi(R0)=1, phi(R_max)=0 fixed
        w += dt*acc; phi += dt*w
        phi[0] = 1.0; phi[-1] = 0.0
    return phi

phi0 = green(0.0)          # massless -> 1/r
phiM = green(1.0**2)       # massive m=1 (the sine-Gordon phase mass) -> Yukawa

print("=== PART B: mediator range, massless vs massive (linear) ===")
print(f"  {'r':>6s} {'massless phi':>13s} {'massive phi':>13s}")
for rr in [2, 5, 10, 15, 20]:
    i = np.argmin(np.abs(r-rr))
    print(f"  {r[i]:6.1f} {phi0[i]:13.5e} {phiM[i]:13.5e}")
print(f"  massless slope [5,15] = {loglog_slope(r, phi0, 5, 15):+.3f}   (1/r => -1)")
print(f"  massive  slope [5,15] = {loglog_slope(r, phiM, 5, 15):+.3f}   (Yukawa: steep, not a power law)")
i5  = np.argmin(np.abs(r-5)); i15 = np.argmin(np.abs(r-15))
print(f"  massless phi(5)/phi(15) = {phi0[i5]/phi0[i15]:.3f}   "
      f"massive phi(5)/phi(15) = {phiM[i5]/phiM[i15]:.3e}  (screened)")
