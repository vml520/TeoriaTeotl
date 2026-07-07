"""Are particle properties intrinsic labels, or field configurations?

Demonstration: 'charge' is not a property a particle HAS; it is the WINDING NUMBER of the phase
field -- and winding is forced to be an integer by topology alone (theta: closed loop -> S^1 has
integer degree). So charge quantization is automatic, not an external rule.

We measure the winding W = (1/2pi) * sum of wrap_to_pi(delta theta) around a closed loop, for:
  - vortices of imposed charge W (get exactly W)
  - a two-vortex configuration (get the sum)
  - a generic random smooth field (still an integer)
No configuration can carry a fractional charge -- that is the point.
"""
import numpy as np

n = 400
ax = np.linspace(-1, 1, n)
X, Y = np.meshgrid(ax, ax)

def wrap(a): return (a + np.pi) % (2*np.pi) - np.pi

def winding_on_loop(theta, cx=0.0, cy=0.0, R=0.6, npts=2000):
    t = np.linspace(0, 2*np.pi, npts, endpoint=False)
    xs, ys = cx + R*np.cos(t), cy + R*np.sin(t)
    ix = np.clip(((xs+1)/2*(n-1)).astype(int), 0, n-1)
    iy = np.clip(((ys+1)/2*(n-1)).astype(int), 0, n-1)
    vals = theta[iy, ix]
    return np.sum(wrap(np.diff(np.append(vals, vals[0]))))/(2*np.pi)

def vortex(W, x0=0.0, y0=0.0):
    return W*np.arctan2(Y - y0, X - x0)

print("  'charge' = winding number of the field, measured around a closed loop:\n")
print("  " + "{:<38s} {:>12s}".format("configuration", "winding W"))
for W in [0, 1, 2, 3, -1, -2]:
    th = vortex(W) if W != 0 else np.zeros_like(X)
    print("  " + "{:<38s} {:>12.4f}".format(f"single vortex, imposed charge {W:+d}", winding_on_loop(th)))

# two vortices enclosed by one big loop -> charges add
th2 = vortex(+2, -0.3, 0) + vortex(-1, +0.3, 0)
print("  " + "{:<38s} {:>12.4f}".format("two vortices (+2 and -1) in one loop", winding_on_loop(th2, R=0.8)))

# a generic random smooth field -> still an integer
rng = np.random.default_rng(3)
kx, ky = rng.normal(size=6), rng.normal(size=6)
ph = rng.uniform(0, 2*np.pi, 6)
thr = np.zeros_like(X)
for a in range(6):
    thr += 0.4*np.sin(3*(kx[a]*X + ky[a]*Y) + ph[a])
print("  " + "{:<38s} {:>12.4f}".format("generic smooth random field", winding_on_loop(thr, R=0.7)))

print("\n  => every closed loop gives an INTEGER, always. You cannot build a fractional charge.")
print("     Charge is quantized because it is a winding number -- topology, not an added postulate.")
print("     (Companion results: mass is field energy M_k = 8 sqrt(Lambda) E0, not an intrinsic tag;")
print("      antiparticle = opposite winding, IDENTICAL mass. Properties are configurations of one field.)")
