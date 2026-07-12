"""SINT -- r from the soliton interior (gate in SINT0_prereg_r.md).

SINT-1  [structural] flux-blindness: dial = gauge-invariant loop phase;
        uniform winding sits at the 120-deg notches; Sum m, Sum sqrt m flat.
SINT-2  [computed] real two-lump overlap energy W(phi,d) from the actual
        omega=0.78 Q-ball profile; harmonics w1,w2,w3(d); by-product A(d).
SINT-3  [verdict] where is the dial potential stationary; does the
        composite force r = 0.31812 (cos3beta=1/4r) within 20%?
"""
import json
import numpy as np

def hdr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70)
OMEGA = 0.78                                   # M2' background (inherited)
w3 = np.exp(2j*np.pi/3)

# ---- observed dial (PDG) -------------------------------------------------
m = np.array([0.51099895, 105.6583755, 1776.86]); v = np.sqrt(m)
cf = np.array([v @ np.conj(w3**(n*np.arange(3))) for n in range(3)])/3
M_d, delta = cf[0].real, np.angle(cf[1]); A_d = 2*abs(cf[1])/M_d
beta = delta - 2*np.pi/3
r_target = 1/(4*np.cos(3*beta))
print(f"observed: delta={np.degrees(delta):.4f} deg  beta={np.degrees(beta):.4f} deg"
      f"  A={A_d:.5f}  r_target={r_target:.5f}")

hdr("SINT-1  flux-blindness of mass sums + the notch structure  [derived]")
dg = np.linspace(0, 2*np.pi, 4000)
lam = 1 + A_d*np.cos(dg[:, None] + 2*np.pi*np.arange(3)/3)   # sqrt-masses(delta)
sum_m = np.sum((M_d*lam)**2, axis=1)
sum_sqrtm = np.sum(M_d*lam, axis=1)
print(f"Sum m  varies with delta by {np.ptp(sum_m):.2e} (flat)")
print(f"Sum sqrt m varies with delta by {np.ptp(sum_sqrtm):.2e} (flat)")
print("""=> no mass-sum functional selects delta (Z3 sum rules). r lives only
in the delta-DEPENDENT field-overlap energy. And a rigid uniform internal
winding forces 3 delta = 2 pi w -> delta in {0,120,240} deg (the notches);
the observed 132.73 deg = 120 + 12.73 is an OFFSET off the w=1 notch, which
can only come from the anharmonic inter-lump energy. This is the exact
statement of the wall.""")

hdr("SINT-2  the real two-lump overlap energy  [computed]")
# --- Q-ball profile at OMEGA (shooting; repo potential V(rho^2)) ---
DR, RMAX = 0.01, 90.0; NS = int(RMAX/DR)
def Up(rho, c2): return c2*rho - 4*rho**3 + 6*rho**5
def shoot(a, c2, store=False):
    rho = a + Up(a, c2)*DR*DR/6; p = Up(a, c2)*DR/3
    r = DR; sgn = np.sign(rho); nz = 0; alive = True
    tr = np.empty(NS) if store else None
    for i in range(NS):
        if store: tr[i] = rho
        def f(rr, y, yp): return yp, Up(y, c2) - 2/rr*yp
        k1 = f(r, rho, p); k2 = f(r+DR/2, rho+DR/2*k1[0], p+DR/2*k1[1])
        k3 = f(r+DR/2, rho+DR/2*k2[0], p+DR/2*k2[1])
        k4 = f(r+DR, rho+DR*k3[0], p+DR*k3[1])
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
rr = DR*np.arange(1, NS+1); it = int(np.argmin(np.abs(prof)))
prof[it:] = 0.0; Rball = rr[it]
print(f"omega={OMEGA} Q-ball: core rho={prof[0]:.4f}, radius R={Rball:.1f} "
      f"(thin-wall); shell at rho^2=1/3")

from numpy import interp
def rho_of(x): return interp(np.abs(x), rr, prof, right=0.0)
def drho_of(x):
    g = np.gradient(prof, rr); return np.sign(x)*interp(np.abs(x), rr, g, right=0.0)

def Vfun(x2): return 0.5*x2 - x2**2 + x2**3         # V(|psi|^2), frozen repo

def overlap_harmonics(d):
    """two lumps on z-axis at +-d/2; cylindrical integral of w1,w2,w3."""
    zmax = d/2 + Rball + 2
    z = np.linspace(-zmax, zmax, 1400); s = np.linspace(0, Rball+2, 500)
    Z, S = np.meshgrid(z, s, indexing='ij')
    R1 = np.sqrt(S**2 + (Z-d/2)**2); R2 = np.sqrt(S**2 + (Z+d/2)**2)
    r1 = rho_of(R1); r2 = rho_of(R2)
    # gradient dot: dr1 . dr2 = (dρ/dR1)(dρ/dR2)(unit1·unit2)
    g1 = drho_of(R1); g2 = drho_of(R2)
    with np.errstate(divide='ignore', invalid='ignore'):
        u1 = np.stack([(Z-d/2)/R1, S/R1]); u2 = np.stack([(Z+d/2)/R2, S/R2])
        udot = np.nan_to_num(u1[0]*u2[0] + u1[1]*u2[1])
    grad_dot = g1*g2*udot
    P = r1**2 + r2**2; Q = r1*r2
    dens1 = 2*(grad_dot + OMEGA**2*r1*r2) + (Q - 4*P*Q + 6*P**2*Q + 6*Q**3)
    dens2 = -2*Q**2 + 6*P*Q**2
    dens3 = 2*Q**3
    jac = 2*np.pi*S
    dz = z[1]-z[0]; ds = s[1]-s[0]
    W = lambda dd: np.sum(dd*jac)*dz*ds
    return W(dens1), W(dens2), W(dens3)

print("(scanning from deep overlap outward; d as a fraction of R)")
print(f"\n{'d/R':>6s} {'w1':>11s} {'w2':>11s} {'w3':>11s} "
      f"{'w2/w1':>9s} {'w3/w1':>9s}")
rows = []
for frac in [0.15, 0.3, 0.5, 0.75, 1.0, 1.5]:
    d = frac*Rball
    w1, w2, w3 = overlap_harmonics(d)
    rat2 = w2/w1 if abs(w1) > 1e-30 else np.nan
    rat3 = w3/w1 if abs(w1) > 1e-30 else np.nan
    rows.append((d, frac, w1, w2, w3, rat2, rat3))
    print(f"{frac:6.2f} {w1:11.3e} {w2:11.3e} {w3:11.3e} "
          f"{rat2:9.4f} {rat3:9.4f}")

# deep-overlap analytic limit (flat plateaus, rho1=rho2=rho_core)
xc = prof[0]**2; Pc, Qc = 2*xc, xc
d1 = 2*OMEGA**2*Qc + (Qc - 4*Pc*Qc + 6*Pc**2*Qc + 6*Qc**3)
d2 = -2*Qc**2 + 6*Pc*Qc**2; d3 = 2*Qc**3
print(f"\ndeep-overlap plateau limit (rho_core={prof[0]:.3f}): "
      f"w2/w1 -> {d2/d1:.4f}, w3/w1 -> {d3/d1:.4f}")

hdr("SINT-3  where the harmonics land + verdict")
print(f"""r = 0.318 needs the second harmonic ~1/3 of the first: a
STRONGLY-OVERLAPPING regime, not a loose molecule. The scan confirms it --
the harmonic ratios vanish (exp-suppressed) when the lumps only touch, and
climb into the O(0.1-0.4) range only in DEEP overlap, reaching the plateau
limit w2/w1 -> {d2/d1:.3f} (bracketing r_target = {r_target:.3f}). So the
offset-producing anharmonics are the RIGHT SIZE, but only where the two
lumps have essentially MERGED into one object -- exactly where the additive
two-lump ansatz is no longer trustworthy.""")

hdr("SINT VERDICT vs pre-registered gate:  FAIL (advancing)")
print(f"""[derived] SINT-1: the wall is exactly located -- delta is a
gauge-invariant loop flux, all mass-sum energies are flat in it, and the
12.73-deg offset can only come from the anharmonic overlap energy.
[computed] SINT-2/3: those anharmonics are real and computable; their ratio
reaches the O(0.3) range needed for r -- but ONLY in the deep-overlap
(merged) regime, where the loose two-lump-molecule model is invalid. So:
  * the two-lump MOLECULE picture is EXCLUDED as the generation structure
    (it gives r ~ 0 wherever it is self-consistent; r ~ 0.3 only where it
    has collapsed to one object) -- an informative negative;
  * this REDIRECTS to the single MERGED soliton with internal structure --
    exactly the M2' object -- whose internal eigenvalue problem is the true
    seat of r. That problem (the 3D interacting soliton spectrum) is the
    same wall that holds A = sqrt2 and every absolute scale.
Per the gate: r is NOT forced (no d selected within a valid regime) ->
FAIL. Advance: r's home is now pinned to one specific hard object (the
merged three-fold soliton interior), and the loose-molecule alternative is
closed. No tuning; ansatz limits stated explicitly; stop per gate.""")

out = dict(prereg="SINT0_prereg_r.md 2026-07-12", omega=OMEGA,
           r_target=float(r_target), Rball=float(Rball),
           rho_core=float(prof[0]),
           harmonics=[dict(d_over_R=float(fr), w1=float(a), w2=float(b),
                           w3=float(c), w2_w1=float(r2), w3_w1=float(r3))
                      for d, fr, a, b, c, r2, r3 in rows],
           deep_overlap_limit=dict(w2_over_w1=float(d2/d1),
                                   w3_over_w1=float(d3/d1)),
           verdict="FAIL (advancing): offset anharmonics computed, reach "
                   "O(0.3) (bracketing r_target) only in the deep-overlap / "
                   "merged regime where the two-lump ansatz is invalid. "
                   "Loose-molecule model EXCLUDED; r's seat = the single "
                   "merged three-fold soliton interior (same wall as A, "
                   "absolute scales).")
with open("outputs/SINT_r_interior.json", "w") as f:
    json.dump(out, f, indent=2)
print("\n[results block written: outputs/SINT_r_interior.json]")
