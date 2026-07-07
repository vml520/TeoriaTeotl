"""Sign test: do two like phase-charges ATTRACT (gravity) or REPEL (Coulomb)?

The massless Goldstone field of the broken U(1) has energy  E = 1/2 integral |grad theta|^2
(positive definite).  Two localized monopole sources produce fields that superpose;
the interaction energy is the cross term
    E_int(d) = integral grad(phi_1) . grad(phi_2)  d^3x   =   q1 q2 / (4 pi d).

  LIKE charges  (q1 q2 > 0): E_int > 0, DECREASING with d  -> force pushes apart  -> REPULSIVE
  OPPOSITE      (q1 q2 < 0): E_int < 0, more negative when close -> pulls together -> ATTRACTIVE

Gravity requires UNIVERSAL ATTRACTION between like sources (all masses positive, all attract).
If like charges repel, this 1/r^2 force is Coulomb/EM-like, not gravity.

Numerics: softened point potentials phi_i = -q_i/(4 pi sqrt(r^2+eps^2)) on a 3D grid.
E_int = E[phi1+phi2] - E[phi1] - E[phi2]  (self-energies cancel exactly).
"""
import numpy as np

n, L = 96, 48.0
h    = L/n
eps  = 1.0
ax   = (np.arange(n) - n/2)*h
X, Y, Z = np.meshgrid(ax, ax, ax, indexing='ij')

def phi(q, z0):
    R = np.sqrt(X**2 + Y**2 + (Z - z0)**2 + eps**2)
    return -q/(4*np.pi*R)

def Efield(th):
    gx, gy, gz = np.gradient(th, h)
    return 0.5*np.sum(gx*gx + gy*gy + gz*gz)*h**3

print(f"grid {n}^3  box L={L}  h={h}  (Coulomb expectation q1q2/4pi = {1/(4*np.pi):+.4f})\n")
print(f"  {'config':>14s} {'d':>5s} {'E_int':>11s} {'E_int * d':>11s} {'force sign':>12s}")

for label, q2 in [("LIKE (+,+)", +1.0), ("OPPOSITE (+,-)", -1.0)]:
    E_of_d = {}
    for d in [6.0, 10.0, 16.0]:
        p1 = phi(1.0, +d/2); p2 = phi(q2, -d/2)
        Eint = Efield(p1 + p2) - Efield(p1) - Efield(p2)
        E_of_d[d] = Eint
    for d in [6.0, 10.0, 16.0]:
        # force = -dE/dd via central/one-sided difference where available
        if d == 10.0:
            F = -(E_of_d[16.0] - E_of_d[6.0])/(16.0 - 6.0)
            sign = "REPULSIVE" if F > 0 else "ATTRACTIVE"
            fs = f"{sign}"
        else:
            fs = ""
        print(f"  {label:>14s} {d:5.1f} {E_of_d[d]:11.5f} {E_of_d[d]*d:11.5f} {fs:>12s}")
    print()

print("Reading: E_int*d ~ constant confirms a 1/d potential (=> 1/r^2 force).")
print("Sign of that constant is the verdict: + = like-repel (Coulomb),  - = like-attract (gravity).")
