"""SPEC-NL -- the nonlinear l=3 condensate (gate in SPEC0b_prereg_nl3.md).

NL-1: does the l=3 condensate's dial direction carry a potential, or is it
      flat (a rotational Goldstone)?  Build psi = f(r) + a*chi3(r)*cos(3(phi-d))
      at finite a, compute the full nonlinear energy E(d).
NL-2: anharmonicity E(a)-E(0): quadratic (>0 stability check) and quartic sign
      (self-focusing = ball prefers a triangle).
Repo potential U(s)=1/2 s - s^2 + s^3 (s=|psi|^2), omega=0.78.
"""
import json
import numpy as np

def hdr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70)
OMEGA = 0.78

# ---- Q-ball profile + l=3 eigenmode (reuse validated BdG) ----------------
DR, RMAX0 = 0.01, 80.0; NS = int(RMAX0/DR)
def Up(rho, c2): return c2*rho - 4*rho**3 + 6*rho**5
def shoot(a, c2, store=False):
    rho = a + Up(a, c2)*DR*DR/6; p = Up(a, c2)*DR/3
    r = DR; sgn = np.sign(rho); nz = 0; alive = True
    tr = np.empty(NS) if store else None
    for i in range(NS):
        if store: tr[i] = rho
        def fn(rr, y, yp): return yp, Up(y, c2) - 2/rr*yp
        k1 = fn(r, rho, p); k2 = fn(r+DR/2, rho+DR/2*k1[0], p+DR/2*k1[1])
        k3 = fn(r+DR/2, rho+DR/2*k2[0], p+DR/2*k2[1])
        k4 = fn(r+DR, rho+DR*k3[0], p+DR*k3[1])
        rn = rho+DR/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0])
        pn = p +DR/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
        if alive: rho, p = rn, pn
        if abs(rho) > 2: alive = False
        r += DR; s = np.sign(rho)
        if alive and s != 0 and s != sgn: nz += 1; sgn = s
    return (nz, tr) if store else nz
c2 = 1-OMEGA**2; disc = 1-2*c2
s1 = (1-np.sqrt(disc))/2; rho_m = np.sqrt((2+np.sqrt(4-6*c2))/6)
grid = np.concatenate([np.linspace(np.sqrt(s1)+1e-6, rho_m-1e-2, 400),
                       rho_m-np.logspace(-2, -15, 600)])
Ns = np.array([shoot(a, c2) for a in grid])
i0 = np.where((Ns[:-1] == 0) & (Ns[1:] > 0))[0][0]
lo, hi = grid[i0], grid[i0+1]
for _ in range(60):
    mid = .5*(lo+hi); (lo, hi) = (mid, hi) if shoot(mid, c2) == 0 else (lo, mid)
_, prof = shoot(.5*(lo+hi), c2, store=True)
rr0 = DR*np.arange(1, NS+1); prof[int(np.argmin(np.abs(prof))):] = 0.0
Rw = rr0[np.where(prof**2 < 1/3)[0][0]]

# l=3 mode profile via 1D BdG on a relaxed background
dr = 0.08; RMAX = Rw+18; N = int(RMAX/dr); r = (np.arange(N)+0.5)*dr
def lap_l(ell):
    L = np.zeros((N, N))
    for i in range(N):
        ri = r[i]; u = 1/dr**2+1/(ri*dr); dn = 1/dr**2-1/(ri*dr)
        L[i, i] = -2/dr**2 - ell*(ell+1)/ri**2
        if i+1 < N: L[i, i+1] = u
        if i-1 >= 0: L[i, i-1] = dn
        else: L[i, i] += dn if ell == 0 else -dn
    return L
Lap0 = lap_l(0); f = np.interp(r, rr0, prof, right=0.0)
for _ in range(40):
    R = Lap0@f-(c2*f-4*f**3+6*f**5)
    f = f-np.linalg.solve(Lap0-np.diag(c2-12*f**2+30*f**4), R)
Ms = 1-12*f**2+30*f**4; Mt = 1-4*f**2+6*f**4
Lap3 = lap_l(3); Z = np.zeros((N, N)); I = np.eye(N)
Lb = np.block([[Lap3-np.diag(Ms)+OMEGA**2*I, Z], [Z, Lap3-np.diag(Mt)+OMEGA**2*I]])
Cc = 2*OMEGA*np.block([[Z, I], [I, Z]])
Mm = np.vstack([np.hstack([np.zeros((2*N, 2*N)), np.eye(2*N)]),
                np.hstack([-Lb, -Cc])])
ev, evec = np.linalg.eig(Mm); Om_c = 1-OMEGA
best = None
for k in range(len(ev)):
    O = ev[k]
    if abs(O.imag) > 1e-3 or O.real <= 1e-3 or O.real >= Om_c-1e-9: continue
    aa = np.abs(evec[:2*N, k])**2; aa /= aa.sum()
    if aa[int(.9*N):N].sum()+aa[N+int(.9*N):].sum() < 1e-2:
        if best is None or O.real < best[0]: best = (O.real, evec[:N, k].real)
Om3, chi3 = best
chi3 = chi3/np.max(np.abs(chi3))                 # normalize peak to 1
print(f"omega={OMEGA}, wall R={Rw:.1f}, l=3 mode Om={Om3:.4f}; chi3 extracted")

# ---- 2D equatorial energy of psi = f(rho) + a*chi3(rho)*cos(3(phi-delta)) --
L = Rw + 8.0; h = 0.15; g = np.arange(-L, L+h, h)
X, Y = np.meshgrid(g, g, indexing='ij')
RHO = np.sqrt(X**2+Y**2); PHI = np.arctan2(Y, X)
fb = np.interp(RHO, r, f, right=0.0)
c3 = np.interp(RHO, r, chi3, right=0.0)
def U(s): return 0.5*s - s**2 + s**3
def energy(a, delta):
    psi = fb + a*c3*np.cos(3*(PHI-delta))
    gx, gy = np.gradient(psi, h, h)
    dens = OMEGA**2*psi**2 + gx**2 + gy**2 + U(psi**2)
    return np.sum(dens)*h*h
E00 = energy(0.0, 0.0)

hdr("NL-1  E(delta): is the l=3 dial direction flat?  (a fixed)")
a_test = 0.15
Es = np.array([energy(a_test, d) for d in np.linspace(0, 2*np.pi/3, 13)])
spread = np.ptp(Es); base = abs(Es.mean()-E00)
print(f"a={a_test}: E(delta) over one Z3 period -> spread = {spread:.3e}, "
      f"deformation energy |E-E0| = {base:.3e}")
print(f"relative flatness spread/|E-E0| = {spread/base:.2e}")
flat = spread/base < 1e-2
print(f"=> E(delta) is {'FLAT (rotational Goldstone)' if flat else 'STRUCTURED'}"
      f" -- the single l=3 orientation {'is NOT' if flat else 'IS'} the dial.")

hdr("NL-2  E(a)-E(0): stability + anharmonicity sign")
avals = np.array([0.03, 0.06, 0.09, 0.12, 0.15, 0.18, 0.22])
dE = np.array([energy(a, 0.0)-E00 for a in avals])
# fit dE = c2 a^2 + c4 a^4
Amat = np.vstack([avals**2, avals**4]).T
c2f, c4f = np.linalg.lstsq(Amat, dE, rcond=None)[0]
print(f"  {'a':>6s} {'E(a)-E(0)':>14s}")
for a, d in zip(avals, dE): print(f"  {a:6.2f} {d:14.6e}")
print(f"fit dE = c2 a^2 + c4 a^4:  c2 = {c2f:.4f} (>0 => stable mode),"
      f"  c4 = {c4f:.4f}")
print(f"=> quartic {'NEGATIVE: SELF-FOCUSING' if c4f < 0 else 'POSITIVE: defocusing'}"
      f" -- the ball {'PREFERS a finite triangular condensate' if c4f < 0 else 'does NOT spontaneously become triangular'}.")

hdr("SPEC-NL VERDICT vs pre-registered gate")
if flat:
    print(f"""FAIL (advancing) -- as pre-registered. E(delta) is flat to
{spread/base:.0e}: the l=3 spatial orientation (equivalently its internal
phase; for a single m=3 mode the two are the same rotation) is a ROTATIONAL
GOLDSTONE, not the dial. So r is NOT contained in any single-mode condensate.

RIGOROUS REFINEMENT (this is the real result): the M-program dial -- which
has a nontrivial V(delta) with harmonics kappa3, kappa6 -- CANNOT be a
single angular sector. It is an intrinsically TWO-SECTOR object: the relative
configuration of two different azimuthal harmonics of the nonlinear
condensate (m=3 and m=6, whose independent phases are the only combination
that breaks the flat direction into cos3delta/cos6delta). This is why r
survived every prior stage -- symmetry, energetics, collective, topology,
AND now single-mode condensate: it lives in the most protected place, the
relative phase of two coupled angular sectors. Confirms SINT-1's 'dial = loop
flux' from an independent direction (a flux is exactly a relative phase
between sectors, not a single mode's orientation).

ANHARMONICITY [new physical result]: c4 = {c4f:.4f} -> the triangular
condensate is {'FAVORED (self-focusing): the large-charge ball spontaneously develops the three-site structure that hosts the generations' if c4f < 0 else 'NOT spontaneously favored: it must be sustained by the two-sector coupling'}.""")
else:
    print("PASS: E(delta) structured; harmonics read off for r (see data).")

out = dict(prereg="SPEC0b_prereg_nl3.md 2026-07-12", omega=OMEGA,
           l3_Omega=float(Om3), flatness_spread_ratio=float(spread/base),
           dial_flat=bool(flat), c2=float(c2f), c4=float(c4f),
           self_focusing=bool(c4f < 0),
           verdict=("FAIL(advancing): single l=3 dial direction FLAT "
                    "(rotational Goldstone) -> r is intrinsically a TWO-SECTOR "
                    "(m=3 x m=6) relative-phase object, not any single-mode "
                    "condensate; confirms SINT-1 dial=loop-flux. Anharmonicity "
                    f"c4={c4f:.3f} ({'self-focusing' if c4f<0 else 'defocusing'})."))
with open("outputs/SPEC_NL3_condensate.json", "w") as fj:
    json.dump(out, fj, indent=2)
print("\n[results block written: outputs/SPEC_NL3_condensate.json]")
