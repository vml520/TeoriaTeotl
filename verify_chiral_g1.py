"""G1 (chiral root): does the TFT action have a chiral / CP-violating structure?

Two checks:
  A. Is the minimal TFT (sine-Gordon) action CP-symmetric? If yes, no chirality is FORCED.
       energy density e = 1/2(grad theta)^2 + Lambda(1-cos theta).
       Under C: theta -> -theta.  (grad theta)^2 invariant; cos(-theta)=cos(theta) invariant.  => CP-even.
  B. The chiral INVARIANT that "winding directions" refers to: the linking number (helicity) of two
     winding lines (defect/flux tubes). Gauss integral
       Lk = (1/4pi) ∮∮ (r1-r2).(dl1 x dl2)/|r1-r2|^3.
     Linked (right-handed) -> +1 ; unlinked -> 0 ; mirror image -> -1.  CP flips the sign.
     This is helicity = chirality, and it is nonzero ONLY when windings are LINKED/twisted.
"""
import numpy as np

# ---- A. CP symmetry of the minimal action ----
rng = np.random.default_rng(0)
th = rng.uniform(-np.pi, np.pi, 4000)
def e_density(t):
    g = np.gradient(t)
    return 0.5*g**2 + 1.0*(1 - np.cos(t))
dE = np.max(np.abs(e_density(th) - e_density(-th)))
print(f"  A. CP symmetry (theta -> -theta): max|e - e_flip| = {dE:.2e}  => minimal action is CP-EVEN")
print("     => the minimal sine-Gordon TFT does NOT force any chirality (equal +/- windings).\n")

# ---- B. the chiral invariant: linking number of winding lines ----
def linking_number(C1, C2):
    n1, n2 = len(C1), len(C2)
    dl1 = np.roll(C1, -1, axis=0) - C1          # segment vectors (closed loops)
    dl2 = np.roll(C2, -1, axis=0) - C2
    m1  = 0.5*(np.roll(C1, -1, axis=0) + C1)     # segment midpoints
    m2  = 0.5*(np.roll(C2, -1, axis=0) + C2)
    Lk = 0.0
    for i in range(n1):
        d = m1[i] - m2                            # (n2,3)
        nd = np.linalg.norm(d, axis=1)**3
        cross = np.cross(np.broadcast_to(dl1[i], dl2.shape), dl2)
        Lk += np.sum(np.einsum('ij,ij->i', d, cross)/nd)
    return Lk/(4*np.pi)

t = np.linspace(0, 2*np.pi, 300, endpoint=False)
ring1        = np.c_[np.cos(t),      np.sin(t),      0*t]          # xy-plane, origin
ring_linkedR = np.c_[1+np.cos(t),    0*t,            np.sin(t)]    # threads ring1 (right-handed)
ring_linkedL = np.c_[1+np.cos(t),    0*t,           -np.sin(t)]    # mirror image (left-handed)
ring_unlinked= np.c_[3+np.cos(t),    0*t,            np.sin(t)]    # far away

print("  B. linking number (helicity / chirality) of two winding lines:")
print(f"     linked, right-handed : Lk = {linking_number(ring1, ring_linkedR):+.3f}")
print(f"     unlinked             : Lk = {linking_number(ring1, ring_unlinked):+.3f}")
print(f"     mirror (left-handed) : Lk = {linking_number(ring1, ring_linkedL):+.3f}")
print("     => a topological invariant that DISTINGUISHES handedness (CP flips its sign),")
print("        and is nonzero only when windings LINK/twist. THIS is 'chirality from winding directions'.")
