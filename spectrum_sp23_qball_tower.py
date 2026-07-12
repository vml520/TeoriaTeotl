"""SP-2/SP-3: the 3D Q-ball generation tower (gates pre-registered in
G0_prereg_spectrum.md BEFORE this run).

Model (frozen, from verify_qball_3d.py): V(rho) = 1/2 rho^2 - rho^4 + rho^6.
Stationary states psi = rho(r) e^{i omega t}:
    rho'' + (2/r) rho' = (1-omega^2) rho - 4 rho^3 + 6 rho^5
Shooting on rho(0)=a, node-counting classifier. Branch n = number of radial
nodes (n = 0,1,2 = the candidate generation tower at equal charge Q).

SP-2 gates (solver validity -- ALL must hold or STOP):
  (a) Derrick virial E_grad = -3W to <=1% for every kept solution
  (b) thick-wall limit E/Q -> 1 (within 5%) at omega = 0.98 (ground branch)
  (c) Q(omega) has interior minimum, rising toward both window ends
SP-3a: common charge range where n=0,1,2 all exist (else STOP: no tower).
SP-3b: scan Q*: PASS-strong if E1/E0 ~ 206.768 AND E2/E1 ~ 16.817 (5%);
       consistent-with if |Q_K - 2/3| < 0.01; else EXCLUSION.
"""
import json
import numpy as np

def hdr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70)

DR, RMAX = 0.0075, 60.0
NSTEP = int(RMAX/DR)
MU_E, TAU_MU = 105.6583755/0.51099895, 1776.86/105.6583755

def Uprime(rho, c2):  return c2*rho - 4*rho**3 + 6*rho**5
def Vfun(rho):        return 0.5*rho**2 - rho**4 + rho**6

def sweep(om, a_arr, store=False):
    """Integrate the profile ODE for an array of shooting amplitudes.
    Returns crossing counts; if store, also the (single) trajectory."""
    c2 = 1.0 - om*om
    a = np.atleast_1d(np.asarray(a_arr, dtype=float))
    rho = a + Uprime(a, c2)*DR*DR/6.0
    p   = Uprime(a, c2)*DR/3.0
    sgn = np.sign(rho)
    N     = np.zeros(len(a), dtype=int)
    alive = np.ones(len(a), dtype=bool)
    traj = np.empty((2, NSTEP)) if store else None
    r = DR
    for i in range(NSTEP):
        if store: traj[0, i], traj[1, i] = rho[0], p[0]
        def f(rr, y0, y1): return y1, Uprime(y0, c2) - (2.0/rr)*y1
        k1 = f(r,          rho,               p)
        k2 = f(r + DR/2,   rho + DR/2*k1[0],  p + DR/2*k1[1])
        k3 = f(r + DR/2,   rho + DR/2*k2[0],  p + DR/2*k2[1])
        k4 = f(r + DR,     rho + DR*k3[0],    p + DR*k3[1])
        rho_n = rho + DR/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])
        p_n   = p   + DR/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
        # freeze diverged trajectories: keep last sane state, stop counting
        rho = np.where(alive, rho_n, rho)
        p   = np.where(alive, p_n, p)
        alive &= np.abs(rho) < 2.0
        r  += DR
        new = np.sign(rho)
        crossed = alive & (new != 0) & (new != sgn)
        N += crossed
        sgn = np.where(crossed, new, sgn)
    return (N, traj) if store else N

def solve_branches(om, nmax=2, nbisect=56):
    """Find the n-node solutions at this omega. Returns dict n -> a*.

    Higher-node shooting boundaries accumulate exponentially below the
    watershed amplitude rho_m (= max of the mechanical potential -U_om,
    where trajectories linger before rolling): the coarse grid must be
    log-spaced in (rho_m - a) to resolve them."""
    c2 = 1.0 - om*om
    disc = 1.0 - 2.0*c2
    if disc <= 0: return {}
    s1 = (1-np.sqrt(disc))/2
    rho_m = np.sqrt((2 + np.sqrt(4 - 6*c2))/6)     # U_om'(rho)=0, deeper root
    grid = np.concatenate([
        np.linspace(np.sqrt(s1)+1e-6, rho_m-1e-2, 400),
        rho_m - np.logspace(-2, -15, 600)])
    N = sweep(om, grid)
    out = {}
    for n in range(nmax+1):
        idx = np.where((N[:-1] <= n) & (N[1:] > n))[0]
        if len(idx) == 0: continue
        lo, hi = grid[idx[0]], grid[idx[0]+1]
        for _ in range(nbisect):
            mid = 0.5*(lo+hi)
            if sweep(om, [mid])[0] <= n: lo = mid
            else:                        hi = mid
        out[n] = 0.5*(lo+hi)
    return out

def observables(om, a_star, n_nodes):
    """Profile -> (E, Q, virial residual, r_trunc, rho_trunc)."""
    _, traj = sweep(om, [a_star], store=True)
    rho, p = traj
    r = DR*np.arange(1, NSTEP+1)
    # truncate at min |rho| after the last node (tail onset of divergence)
    sgn = np.sign(rho); flips = np.where(sgn[1:] != sgn[:-1])[0]
    start = (flips[-1]+1) if len(flips) else 0
    it = start + int(np.argmin(np.abs(rho[start:])))
    kap = np.sqrt(1.0-om*om)
    rr, rh, pp = r[:it+1], rho[:it+1], p[:it+1]
    rt = np.linspace(r[it], 500.0, 40000)
    rho_t = rho[it]*(r[it]/rt)*np.exp(-kap*(rt-r[it]))
    p_t = -rho_t*(kap + 1.0/rt)
    def tot(dens_in, dens_tail):
        return (np.trapezoid(dens_in*4*np.pi*rr**2, rr)
                + np.trapezoid(dens_tail*4*np.pi*rt**2, rt))
    Q  = tot(om*rh**2, om*rho_t**2)
    Eg = tot(0.5*pp**2, 0.5*p_t**2)
    W  = tot(Vfun(rh)-0.5*om**2*rh**2, Vfun(rho_t)-0.5*om**2*rho_t**2)
    E  = tot(0.5*om**2*rh**2 + 0.5*pp**2 + Vfun(rh),
             0.5*om**2*rho_t**2 + 0.5*p_t**2 + Vfun(rho_t))
    vir = abs(Eg + 3*W)/Eg
    return E, Q, vir, r[it], abs(rho[it])

hdr("SP-2/SP-3  solving the Q-ball tower  (n = 0,1,2 radial nodes)")
omegas = [0.72, 0.75, 0.78, 0.80, 0.82, 0.84, 0.86, 0.88,
          0.90, 0.92, 0.94, 0.96, 0.98]
data = {0: [], 1: [], 2: []}
dropped = []
for om in omegas:
    found = solve_branches(om)
    row = f"  omega={om:.2f} :"
    for n in range(3):
        if n not in found:
            row += f"   n={n}: --"
            continue
        E, Q, vir, rt, rhot = observables(om, found[n], n)
        if vir > 0.01 or rhot > 1e-3:
            dropped.append((om, n, vir, rhot))
            row += f"   n={n}: dropped(vir={vir:.1e})"
            continue
        data[n].append((om, found[n], E, Q, vir))
        row += f"   n={n}: E={E:8.2f} Q={Q:8.2f} vir={vir:.0e}"
    print(row, flush=True)

for n in data: data[n] = np.array(data[n])

hdr("SP-2 GATES (solver validity)")
worst_vir = max(d[:, 4].max() for d in data.values() if len(d))
print(f"(a) Derrick virial: worst kept residual = {worst_vir:.2e}  "
      f"(gate <= 1e-2)  {'PASS' if worst_vir <= 0.01 else 'FAIL'}")
g = data[0]
eq98 = g[np.argmin(np.abs(g[:, 0]-0.98)), 2]/g[np.argmin(np.abs(g[:, 0]-0.98)), 3]
print(f"(b) thick-wall E/Q at omega=0.98 = {eq98:.4f}  (gate 1.00 +- 0.05)  "
      f"{'PASS' if abs(eq98-1) < 0.05 else 'FAIL'}")
iQmin = np.argmin(g[:, 3])
c_ok = 0 < iQmin < len(g)-1 and g[0, 3] > g[iQmin, 3] and g[-1, 3] > g[iQmin, 3]
print(f"(c) Q(omega) ground branch: min Q = {g[iQmin,3]:.2f} at "
      f"omega = {g[iQmin,0]:.2f}, endpoints Q = {g[0,3]:.2f}, {g[-1,3]:.2f}  "
      f"{'PASS' if c_ok else 'FAIL'}")
if dropped: print(f"    dropped points (transparency): {dropped}")
assert worst_vir <= 0.01 and abs(eq98-1) < 0.05 and c_ok, "SP-2 FAIL -- STOP"
print("SP-2: PASS -- solver trusted.")

hdr("SP-3a  does a same-charge three-state tower exist?")
if any(len(data[n]) < 2 for n in range(3)):
    print("A branch is missing entirely -> NO tower. STOP per prereg.")
    raise SystemExit
Qlo = max(data[n][:, 3].min() for n in range(3))
Qhi = min(data[n][:, 3].max() for n in range(3))
print(f"branch charge ranges: " + "  ".join(
    f"n={n}: [{data[n][:,3].min():.1f}, {data[n][:,3].max():.1f}]"
    for n in range(3)))
if Qhi <= Qlo:
    print("No common charge range -> NO same-charge tower. STOP per prereg.")
    raise SystemExit
print(f"common charge range: Q* in [{Qlo:.1f}, {Qhi:.1f}]  -> tower EXISTS")

def E_of_Q(branch, Qstar):
    """lowest E on this branch at charge Qstar (branch may be two-valued)"""
    om, E, Q = branch[:, 0], branch[:, 2], branch[:, 3]
    i0 = np.argmin(Q); best = np.inf
    for seg in (slice(0, i0+1), slice(i0, len(Q))):
        qs, es = Q[seg], E[seg]
        o = np.argsort(qs)
        if qs.min() <= Qstar <= qs.max():
            best = min(best, np.interp(Qstar, qs[o], es[o]))
    return best

hdr("SP-3b  the tower vs the leptons (equal-charge scan)")
Qstars = np.linspace(Qlo, Qhi, 400)
rows = []
for Qs in Qstars:
    E0, E1, E2 = (E_of_Q(data[n], Qs) for n in range(3))
    if not all(np.isfinite([E0, E1, E2])): continue
    QK = (E0+E1+E2)/(np.sqrt(E0)+np.sqrt(E1)+np.sqrt(E2))**2
    rows.append((Qs, E0, E1, E2, E1/E0, E2/E1, QK))
rows = np.array(rows)
r10, r21, QK = rows[:, 4], rows[:, 5], rows[:, 6]
print(f"E1/E0 over the tower: range ({r10.min():.4f}, {r10.max():.4f})"
      f"   target mu/e  = {MU_E:.1f}")
print(f"E2/E1 over the tower: range ({r21.min():.4f}, {r21.max():.4f})"
      f"   target tau/mu = {TAU_MU:.2f}")
print(f"Koide Q_K over the tower: range ({QK.min():.4f}, {QK.max():.4f})"
      f"   target 2/3 = {2/3:.4f}")
i = len(rows)//2
print(f"sample mid-tower point Q*={rows[i,0]:.1f}: "
      f"E = ({rows[i,1]:.1f}, {rows[i,2]:.1f}, {rows[i,3]:.1f})")
eq_flags = []
for n in range(3):
    eqn = data[n][:, 2]/data[n][:, 3]
    eq_flags.append((eqn.min(), eqn.max()))
    print(f"binding n={n}: E/Q in ({eqn.min():.3f}, {eqn.max():.3f})"
          f"  ({'bound (E/Q<1) exists' if eqn.min()<1 else 'UNBOUND everywhere'})")

strong = np.any((np.abs(r10/MU_E-1) < .05) & (np.abs(r21/TAU_MU-1) < .05))
koide  = np.any(np.abs(QK-2/3) < .01)
print(f"\nGATE SP-3b:  lepton-ratio match: {'YES' if strong else 'NO'}"
      f"   Koide 2/3 crossing: {'YES' if koide else 'NO'}")

verdict = ("PASS-strong" if strong else
           "CONSISTENT-WITH-KOIDE (weak, scan dof)" if koide else "EXCLUSION")
hdr(f"SP-3 VERDICT: {verdict}")

out = dict(
    prereg="G0_prereg_spectrum.md 2026-07-11",
    sp2=dict(worst_virial=float(worst_vir), thickwall_EoverQ=float(eq98),
             Qmin_omega=float(g[iQmin, 0]), Qmin=float(g[iQmin, 3])),
    branches={int(n): dict(omega=data[n][:, 0].tolist(),
                           a0=data[n][:, 1].tolist(),
                           E=data[n][:, 2].tolist(),
                           Q=data[n][:, 3].tolist()) for n in data},
    common_Q=[float(Qlo), float(Qhi)],
    tower=dict(r10_range=[float(r10.min()), float(r10.max())],
               r21_range=[float(r21.min()), float(r21.max())],
               QK_range=[float(QK.min()), float(QK.max())]),
    gates=dict(lepton_match=bool(strong), koide_crossing=bool(koide)),
    verdict=verdict,
)
with open("outputs/SP23_qball_tower.json", "w") as f:
    json.dump(out, f, indent=2)
print("[results block written: outputs/SP23_qball_tower.json]")
