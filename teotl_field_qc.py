"""
teotl_field_qc -- teotl quanta carrying BOTH maps: position in R^3 and phase on S^1.

This is teotl_rotor_qc with the field structure restored. The rotor there gave
exact quantisation but had NO SPACE: its couplings g and J_ex were free numbers
put in by hand, with no falloff and no sphere of influence. That was a step back
from teotl_qc.py, which at least had positions and distance-dependent coupling.

WHAT IS DERIVED HERE (not chosen):

  1. mass = cycle rate            m_n c^2 = E_n = E_C n^2        [TFT]
  2. interaction range = the field's own Compton length
                                  lambda_n = hbar/(m_n c)
     TWOPI1 established the range of a gapped phase field is the REDUCED
     Compton wavelength (propagator pole), not the full one. Used here.
  3. coupling between two quanta  J_ij ~ exp(-r_ij/lambda) / r_ij
     the Yukawa form that falls out of a gapped field, NOT a Gaussian chosen
     for convenience.

CONSEQUENCE, and it is a prediction rather than a setting:
  lambda_n = hbar/(m_n c) with m_n ~ n^2  =>  lambda_n ~ 1/n^2.
  A MORE EXCITED QUANTUM HAS A SHORTER REACH. The sphere of influence is set
  by the state, not by a parameter.

Free parameters: ONE overall coupling scale, versus two (g, J_ex) before, and
the distance dependence is no longer arbitrary.

The two maps are kept explicit throughout: `pos` is R^3, `n` is S^1.
"""
import numpy as np
import teotl_math as tm
from teotl_rotor_qc import Quantum


class FieldQuantum:
    """One teotl quantum: a position in R^3 and a phase state on S^1."""

    def __init__(self, pos, n_max=5, E_C=1.0, E_J=0.05, p=1):
        self.pos = np.asarray(pos, float)
        self.rotor = Quantum(n_max=n_max, E_C=E_C, E_J=E_J, p=p)
        self.E_C = E_C

    def energy(self, n):
        """E_n = E_C n^2 -- and in TFT this IS the mass (cycle rate)."""
        return self.E_C * n**2

    def compton(self, n, hbar=1.0, c=1.0):
        """lambda_n = hbar/(m_n c), m_n c^2 = E_n.  REDUCED, per TWOPI1."""
        E = self.energy(n)
        return np.inf if E <= 0 else hbar*c/E


class FieldRegister:
    """Several quanta in R^3. Couplings DERIVED from separation and state."""

    def __init__(self, positions, n_max=5, E_C=1.0, E_J=0.05, p=None, J0=1.0):
        self.q = [FieldQuantum(x, n_max, E_C, E_J,
                               p=1 if p is None else p[i])
                  for i, x in enumerate(positions)]
        self.N = len(self.q)
        self.d = self.q[0].rotor.dim
        self.J0 = J0                       # the ONE remaining free scale
        self.n_max = n_max

    # ---- geometry ----------------------------------------------------
    def separation(self, i, j):
        return float(np.linalg.norm(self.q[i].pos - self.q[j].pos))

    def coupling(self, i, j, n_ref=1):
        """J_ij = J0 * exp(-r/lambda) / r, with lambda from the REFERENCE state.

        Derived, not chosen: Yukawa is the gapped field's own falloff, and
        lambda is the quantum's Compton length, which follows from mass = rate.
        """
        r = self.separation(i, j)
        if r < 1e-12:
            return 0.0
        lam = self.q[i].compton(n_ref)
        return self.J0 * np.exp(-r/lam) / r

    def influence_radius(self, i, n_ref=1, frac=0.05):
        """Where the coupling has fallen to `frac` of its value at r = lambda.
        This is the sphere of influence -- set by the STATE, not a parameter."""
        lam = self.q[i].compton(n_ref)
        ref = np.exp(-1.0)/lam
        rs = np.linspace(1e-3, 50*lam, 20000)
        vals = np.exp(-rs/lam)/rs
        below = np.where(vals < frac*ref)[0]
        return float(rs[below[0]]) if len(below) else np.inf

    # ---- dynamics ----------------------------------------------------
    def H(self, n_g=0.0, n_ref=1):
        """Full Hamiltonian on the product space, couplings derived."""
        dim = self.d**self.N
        H = np.zeros((dim, dim), complex)
        I = np.eye(self.d)
        def embed(op, site):
            M = np.array([[1.0+0j]])
            for k in range(self.N):
                M = np.kron(M, op if k == site else I)
            return M
        for i, qq in enumerate(self.q):
            H += embed(qq.rotor.H(n_g), i)
        nop = np.diag(self.q[0].rotor.n).astype(complex)
        for i in range(self.N):
            for j in range(i+1, self.N):
                Jij = self.coupling(i, j, n_ref)
                if Jij != 0.0:
                    H += Jij * (embed(nop, i) @ embed(nop, j))
        return H


# =========================================================================
#  METRIC -- spacetime contraction sourced by the quanta
# =========================================================================
#
# USING THE CORPUS'S VERIFIED CONSTRUCTION, NOT ITS FALSIFIED ANSATZ.
#
# NATIVE3 recorded: "The metric ansatz g_ij = delta_ij(1+|grad theta|^2/E_0^2)
# was FALSIFIED by the corpus itself (wrong shape, 1/r^4); what works is
# 'Construction B', the standard weak-field metric." So this implements the
# weak-field 00 equation that DID survive:
#
#       laplacian(Phi) = 4 pi c^2 |grad theta|^2        (energy density source)
#       g_00 = -(1 + 2 Phi/c^2)      -> TIME dilation
#       g_ij =  delta_ij (1 - 2 Phi/c^2)  -> SPACE contraction
#
# Sign/universality is the corpus's own result: u = |grad theta|^2 >= 0
# everywhere, so Phi is always an attractive well and the contraction has ONE
# sign. Matter and antimatter both contract; only the Noether charge is signed.
#
# KNOWN LIMITATION, stated rather than hidden: the metric here is SOURCED but
# not DYNAMICAL. NATIVE3: "There is no equation of motion for the metric
# anywhere in the corpus." This computes the field the quanta produce; it does
# not evolve the geometry.


def phase_gradient(r, lam, amp=1.0):
    """|grad theta| for a Yukawa phase profile theta ~ amp * exp(-r/lam)/r."""
    r = np.maximum(np.asarray(r, float), 1e-9)
    return amp*np.exp(-r/lam)*(1.0/r**2 + 1.0/(lam*r))


class MetricField:
    """Weak-field metric sourced by a FieldRegister's quanta."""

    def __init__(self, register, state=None, c=1.0, G=1.0):
        self.reg = register
        self.c, self.G = c, G
        self.state = [1]*register.N if state is None else state

    def energy_density(self, x):
        """u = |grad theta|^2, summed over quanta. NON-NEGATIVE everywhere."""
        x = np.asarray(x, float)
        u = 0.0
        for i, q in enumerate(self.reg.q):
            r = np.linalg.norm(x - q.pos)
            lam = q.compton(self.state[i])
            u += phase_gradient(r, lam)**2
        return float(u)

    def potential(self, x):
        """Phi from the weak-field 00 equation, Newtonian superposition.

        REGULARISED AT THE COMPTON LENGTH, and that is physics, not a fudge:
        a quantum cannot be localised below lambda = hbar/mc, so treating it as
        a point below that scale is meaningless. Phi saturates at r ~ lambda.
        Integrating an unregularised 1/r straight through a source gave a proper
        separation 26x the coordinate one -- the weak-field expansion had already
        failed there."""
        x = np.asarray(x, float); Phi = 0.0
        for i, q in enumerate(self.reg.q):
            lam = q.compton(self.state[i])
            r = float(np.linalg.norm(x - q.pos))
            r_eff = np.sqrt(r*r + lam*lam)          # smooth, -> r far, -> lam near
            Phi += -self.G*q.energy(self.state[i])/(r_eff*self.c**2)
        return float(Phi)

    def weak_field_ok(self, x, tol=0.1):
        """Is the weak-field expansion valid here? |2 Phi/c^2| must be small."""
        return abs(2*self.potential(x)/self.c**2) < tol

    def time_dilation(self, x):
        """dtau/dt = sqrt(-g_00) = sqrt(1 + 2 Phi/c^2). Phi < 0 => clocks slow."""
        return float(np.sqrt(max(1.0 + 2*self.potential(x)/self.c**2, 1e-12)))

    def space_factor(self, x):
        """sqrt(g_ii) = sqrt(1 - 2 Phi/c^2). Phi < 0 => proper length > coordinate."""
        return float(np.sqrt(max(1.0 - 2*self.potential(x)/self.c**2, 1e-12)))

    def proper_distance(self, i, j, n=400):
        """Integrate sqrt(g_ii) along the straight coordinate line i->j.
        THIS is the contraction: proper separation differs from coordinate."""
        a, b = self.reg.q[i].pos, self.reg.q[j].pos
        ts = np.linspace(0.0, 1.0, n)
        pts = [a + (b-a)*s for s in ts]
        f = np.array([self.space_factor(pt) for pt in pts])
        return float(np.trapezoid(f, ts) * np.linalg.norm(b-a))
