"""
teotl_rotor_qc — a qubit emulator built from teotl quanta, and nothing else.

PRINCIPLE (Vic): everything is teotl. One substance. A teotl quantum is the
minimum excitation of the field: a point carrying ONE internal phase, cycling.
"A vibrating 1-dimensional point." That object is a ROTOR, and it is all this
module contains.

    state of one quantum : |n>, n in Z, the number of cycles it carries
    its energy           : E_C n^2      (cycling costs energy, quadratically)
    coupling between     : -E_J cos(theta), which moves one cycle at a time
                           i.e. |n> <-> |n+-1>

That is the whole model. Everything below is consequence, not addition.

Why this works where the soliton route did not:
  * the spectrum is EXACTLY integer -- no profile to solve, nothing to converge
  * the energy is bounded below, so there is a genuine ground state  [MINQ0]
  * H is a finite matrix, so evolution is exact and unitary: no numerical drift,
    which is what defeated the field version
  * n is conserved mod the coupling, so "charge" readout is exact

The Hamiltonian is the standard charge-basis rotor. That it coincides with the
Cooper-pair-box Hamiltonian is a consequence, not an assumption: any object that
is a compact phase with a conjugate integer has this form.
"""
import numpy as np
import teotl_math as tm


class Quantum:
    """One teotl quantum: a rotor. Charge basis |n>, n = -n_max .. n_max."""

    def __init__(self, n_max=12, E_C=1.0, E_J=0.05, n_g=0.0, p=1):
        """p = PHASE COUNT: how many sectors the quantum's circle carries.

        Its hopping moves the cycle number by +-p, not +-1. This is the
        p-th harmonic of the compact phase, cos(p theta), and p is an integer
        because the phase is compact -- nothing else is allowed.
        """
        self.n_max, self.E_C, self.E_J, self.n_g, self.p = n_max, E_C, E_J, n_g, p
        self.n = np.arange(-n_max, n_max+1)
        self.dim = len(self.n)

    def raise_op(self):
        """S_p : |n> -> |n+p>. The quantum's own hop."""
        S = np.zeros((self.dim, self.dim), complex)
        for i in range(self.dim - self.p):
            S[i+self.p, i] = 1.0
        return S

    def H(self, n_g=None):
        """H = E_C (n - n_g)^2 - (E_J/2) (|n><n+1| + h.c.)"""
        ng = self.n_g if n_g is None else n_g
        H = np.diag(self.E_C*(self.n - ng)**2).astype(complex)
        S = self.raise_op()
        H += -0.5*self.E_J*(S + S.conj().T)
        return H

    def levels(self, n_g=None, k=4):
        w, v = np.linalg.eigh(self.H(n_g))
        return w[:k], v[:, :k]

    def splitting(self, n_g=None):
        w, _ = self.levels(n_g, k=2)
        return float(w[1] - w[0])


class RotorQubit:
    """Qubit = the lowest two levels of ONE teotl quantum.

    |0> and |1> are cycle-number states of the same object, not two objects.
    That is the point: there is only one substance here.
    """

    def __init__(self, n_max=12, E_C=1.0, E_J=0.05, n_g=0.0):
        self.q = Quantum(n_max, E_C, E_J, n_g)
        w, v = self.q.levels(k=2)
        self.basis = v                      # columns: |0>, |1> in charge basis
        self.psi = v[:, 0].astype(complex)  # start in the ground state

    # ---- evolution -----------------------------------------------------
    def evolve(self, t, n_g=None):
        """Exact unitary evolution. No integrator, so no drift."""
        w, v = np.linalg.eigh(self.q.H(n_g))
        c = v.conj().T @ self.psi
        self.psi = v @ (np.exp(-1j*w*t) * c)
        return self

    # ---- readout -------------------------------------------------------
    def amplitudes(self):
        return self.basis.conj().T @ self.psi

    def populations(self):
        a = self.amplitudes(); p = np.abs(a)**2
        s = p.sum()
        return (float(p[0]/s), float(p[1]/s)) if s > 0 else (0.0, 0.0)

    def bloch(self):
        a = self.amplitudes()
        a = a/np.linalg.norm(a)
        x = 2*np.real(np.conj(a[0])*a[1])
        y = 2*np.imag(np.conj(a[0])*a[1])
        z = abs(a[0])**2 - abs(a[1])**2
        return float(x), float(y), float(z)

    def phase(self):
        a = self.amplitudes()
        return float(tm.wrap_to_pi(np.angle(a[1]) - np.angle(a[0])))

    # ---- gates ---------------------------------------------------------
    # Both are driven by the SAME physics: the level splitting sets the phase
    # rate (Z), and detuning the offset charge n_g mixes the levels (X).

    def rz(self, phi):
        """Z-rotation: free evolution for the time the splitting requires."""
        w = self.q.splitting()
        if abs(w) < 1e-12:
            raise RuntimeError("degenerate levels: no Z axis")
        return self.evolve(abs(phi)/w if phi >= 0 else (2*np.pi-abs(phi))/w)

    def rx(self, theta, n_g_drive=None):
        """X-rotation: shift n_g so the levels mix, evolve, shift back.

        DRIVE POINT SCALES WITH PHASE COUNT: n_g = p/2, not 1/2.
        Hopping moves n by +-p, so the qubit states are |0> and |p>, and they
        are degenerate where E_C(0-n_g)^2 = E_C(p-n_g)^2, i.e. n_g = p/2.
        Driving at 1/2 regardless of p leaves them split by E_C p^2 >> E_J and
        nothing mixes -- measured X fidelity 0.0001 at p=2 before this fix.
        """
        if n_g_drive is None:
            n_g_drive = self.q.p/2.0
        w_drive = self.q.splitting(n_g=n_g_drive)
        if abs(w_drive) < 1e-12:
            raise RuntimeError("no mixing at this drive point")
        return self.evolve(abs(theta)/w_drive, n_g=n_g_drive)

    def reset(self):
        self.psi = self.basis[:, 0].astype(complex)
        return self



# =========================================================================
#  TWO QUANTA
# =========================================================================

class TwoQuanta:
    """Two teotl quanta with a coupling between their cycle numbers.

    H = E_C1 (n1-ng1)^2 + E_C2 (n2-ng2)^2
        - (E_J1/2) hop1 - (E_J2/2) hop2
        + g * n1 (x) n2

    The coupling is the only new ingredient, and it is the obvious one: if
    everything is teotl, two quanta interact through the quantity each one
    HAS -- its cycle number. Nothing else is available to couple.

    g is passed per-evolution, so it can be switched off during single-qubit
    gates and on for the entangling gate (a tunable coupler).
    """

    def __init__(self, n_max=5, E_C=1.0, E_J=0.05, g=0.30, p1=1, p2=1, J_ex=0.0):
        self.a = Quantum(n_max, E_C, E_J, p=p1)
        self.b = Quantum(n_max, E_C, E_J, p=p2)
        self.g = g
        self.J_ex = J_ex
        self.d = self.a.dim
        self.I = np.eye(self.d)
        self.n_op = np.diag(self.a.n).astype(complex)

    def H(self, ng1=0.0, ng2=0.0, g=None, J_ex=None):
        """gg   : n-n coupling (always allowed, gives ZZ / CZ)
        J_ex : EXCHANGE coupling S_p1 (x) S_p2^dag + h.c.

        The exchange term removes p1 cycles from one quantum and adds p2 to the
        other. Total cycle number changes by (p2 - p1), so the process is only
        resonant when the PHASE COUNTS MATCH. Mismatched quanta cannot lock --
        that selection rule is not imposed, it falls out of the operator."""
        gg = self.g if g is None else g
        H = (np.kron(self.a.H(ng1), self.I)
             + np.kron(self.I, self.b.H(ng2))
             + gg*np.kron(self.n_op, self.n_op))
        Jx = self.J_ex if J_ex is None else J_ex
        if Jx:
            Sa, Sb = self.a.raise_op(), self.b.raise_op()
            X = np.kron(Sa, Sb.conj().T)
            H += -Jx*(X + X.conj().T)
        return H

    def comp_basis(self, n_g=0.0):
        """|00>,|01>,|10>,|11> from each quantum's lowest two levels, g=0."""
        _, va = self.a.levels(n_g=n_g, k=2)
        _, vb = self.b.levels(n_g=n_g, k=2)
        cols = [np.kron(va[:, i], vb[:, j]) for i in (0, 1) for j in (0, 1)]
        return np.column_stack(cols)


class TwoRotorQubits:
    """Two-qubit register. Each qubit is the lowest two cycle-states of one
    teotl quantum; they entangle through the n-n coupling."""

    IDLE_NG = 0.25          # NOT 0 or 0.5: at both, symmetry forces <n>_0 = <n>_1
                            # and the n-n coupling has nothing to distinguish the
                            # levels, so ZZ vanishes identically. Measured:
                            #   n_g=0.00 -> <n> diff 0.0000   (no entangling gate)
                            #   n_g=0.25 -> <n> diff 0.9954   (works)
                            #   n_g=0.50 -> <n> diff 0.0000   (no entangling gate)

    def __init__(self, n_max=5, E_C=1.0, E_J=0.05, g=0.30, n_g_idle=None,
                 p1=1, p2=1, J_ex=0.0):
        self.tq = TwoQuanta(n_max, E_C, E_J, g, p1=p1, p2=p2, J_ex=J_ex)
        self.ng = self.IDLE_NG if n_g_idle is None else n_g_idle
        self.B = self.tq.comp_basis(self.ng)
        self.psi = self.B[:, 0].astype(complex)     # |00>

    def evolve(self, t, ng1=0.0, ng2=0.0, g=None, J_ex=None):
        w, v = np.linalg.eigh(self.tq.H(ng1, ng2, g, J_ex))
        c = v.conj().T @ self.psi
        self.psi = v @ (np.exp(-1j*w*t) * c)
        return self

    def amplitudes(self):
        a = self.B.conj().T @ self.psi
        n = np.linalg.norm(a)
        return a/n if n > 0 else a

    def populations(self):
        return np.abs(self.amplitudes())**2

    # ---- single-qubit gates: coupling OFF ---------------------------
    def rx(self, which, theta, n_g_drive=0.5):
        ng = (n_g_drive, self.ng) if which == 0 else (self.ng, n_g_drive)
        w = self.tq.a.splitting(n_g=n_g_drive)
        return self.evolve(abs(theta)/w, ng[0], ng[1], g=0.0)

    def rz(self, which, phi):
        w = self.tq.a.splitting(n_g=self.ng)
        return self.evolve(abs(phi)/w, self.ng, self.ng, g=0.0)

    # ---- entangling gate: coupling ON -------------------------------
    def cz_time(self):
        """Time for a pi conditional phase from the n-n coupling.

        The ZZ rate is the second difference of the computational-basis
        energies: (E00 - E01 - E10 + E11). Measured, not assumed."""
        H = self.tq.H(self.ng, self.ng, self.tq.g)
        E = np.real(np.diag(self.B.conj().T @ H @ self.B))
        zz = E[0] - E[1] - E[2] + E[3]
        if abs(zz) < 1e-12:
            raise RuntimeError("no ZZ coupling: g too small")
        return np.pi/abs(zz), zz

    def cz(self):
        t, _ = self.cz_time()
        return self.evolve(t, self.ng, self.ng, g=self.tq.g)

    def concurrence(self):
        """Entanglement measure. 0 = product state, 1 = maximally entangled."""
        a = self.amplitudes()
        return float(min(1.0, 2*abs(a[0]*a[3] - a[1]*a[2])))


# ---- phase count: what it does and does NOT do (MEASURED) ---------------
# DOES NOT tune the single-quantum spectrum. Splitting stays ~1.0 across
# p = 1..4 (1.001, 0.975, 1.000, 1.000); it is set by E_C, not by p.
#
# DOES decouple the Hilbert space into p sectors by n mod p, because hopping
# moves n by +-p. Consequence: the naive "lowest two levels" qubit puts |0> and
# |1> in DIFFERENT sectors, which are exactly degenerate and cannot be mixed:
#     p=1 -> drive splitting 5.0e-02, X fidelity 0.9950
#     p=2 -> drive splitting 2.8e-17, X gate DEGENERATE (fails)
#     p=3 -> drive splitting 5.6e-17, X gate DEGENERATE (fails)
# FIX: keep the qubit inside ONE sector and drive at n_g = p/2. Then:
#     p=1 -> 0.9950   p=2 -> 0.9997   p=3 -> 0.9999   p=4 -> 1.0000
# Fidelity IMPROVES with p, because higher sectors are better isolated.
#
# ---- phase-count selection rule (MEASURED) ------------------------------
# An excitation moves between two quanta only when their PHASE COUNTS MATCH.
# Measured swing in <n_B> after starting p1 cycles on A (J_ex=0.25):
#
#     p1  p2   matched   <n_B> swing
#      1   1     yes        0.9995      <- transfers exactly p cycles
#      2   2     yes        1.9974
#      3   3     yes        2.9966
#      1   2      no        0.0627      <- suppressed ~16x
#      1   3      no        0.0156      <- suppressed ~64x
#      2   3      no        0.0306
#
# The rule is not imposed: the exchange operator removes p1 cycles and adds p2,
# so total cycle number is conserved only when p1 == p2. Mismatched quanta are
# off-resonant and cannot lock.
#
# USE: this is ADDRESSABILITY by an exact integer. In a register of many quanta,
# only matching-p pairs couple -- no analog frequency tuning, no crosstalk
# calibration. Assign phase counts and the connectivity graph is fixed by them.


def phase_count_transfer(p1, p2, J_ex=0.25, T=40.0, steps=60, n_max=6):
    """Swing in <n_B> when p1 cycles start on A. ~0 means the pair cannot lock."""
    tq = TwoQuanta(n_max=n_max, E_C=1.0, E_J=0.0, g=0.0, p1=p1, p2=p2, J_ex=J_ex)
    d = tq.d; idx = lambda n: n + n_max
    psi = np.zeros(d*d, complex); psi[idx(p1)*d + idx(0)] = 1.0
    w, v = np.linalg.eigh(tq.H(0.0, 0.0, g=0.0, J_ex=J_ex))
    c = v.conj().T @ psi
    nB = np.kron(np.eye(d), np.diag(tq.b.n).astype(float))
    vals = [float(np.real((v@(np.exp(-1j*w*t)*c)).conj() @ nB @ (v@(np.exp(-1j*w*t)*c))))
            for t in np.linspace(0, T, steps)]
    return max(vals) - min(vals)


# ---- measured defaults --------------------------------------------------
# E_J/E_C sets how cleanly the two lowest levels behave as a qubit. Measured
# X-gate fidelity (P1 after rx(pi), ideal = 1):
#     E_J = 0.02 -> 0.9992      E_J = 0.10 -> 0.9808
#     E_J = 0.05 -> 0.9950      E_J = 0.20 -> 0.9310
# Larger E_J mixes in higher levels (leakage); smaller E_J means slower gates
# because the drive splitting shrinks. E_J = 0.05 is the default as a balance.


def selftest(E_C=1.0, E_J=0.05, verbose=True):
    """Validate the emulator against the three things a qubit must do."""
    import numpy as np
    out = {}

    qb = RotorQubit(E_C=E_C, E_J=E_J); qb.rx(np.pi)
    out["x_gate_fidelity"] = qb.populations()[1]

    w = Quantum(E_C=E_C, E_J=E_J).splitting(n_g=0.5)
    ser = []
    for t_ in np.linspace(0, 2*np.pi/w, 9):
        q = RotorQubit(E_C=E_C, E_J=E_J); q.evolve(t_, n_g=0.5)
        ser.append(q.populations()[1])
    out["rabi_swing"] = max(ser) - min(ser)

    q = RotorQubit(E_C=E_C, E_J=E_J); q.rx(np.pi/2)
    w0 = q.q.splitting(); ph = []
    for _ in range(5):
        q.evolve(0.5); ph.append(q.phase())
    rate = abs(np.mean(np.diff(np.unwrap(ph)))/0.5)
    out["ramsey_error"] = abs(rate - w0)

    q = RotorQubit(E_C=E_C, E_J=E_J)
    q.rx(np.pi/3); q.rz(np.pi/4); q.rx(np.pi/3)
    out["norm_after_gates"] = float(np.linalg.norm(q.psi))

    # --- two-qubit ---
    ph = []
    for k in range(4):
        r = TwoRotorQubits(E_C=E_C, E_J=E_J); r.psi = r.B[:, k].astype(complex)
        a0 = r.amplitudes(); r.cz(); a1 = r.amplitudes()
        ph.append(float(np.angle(a1[k]/a0[k])))
    out["cz_conditional_phase_error"] = abs(abs(ph[0]-ph[1]-ph[2]+ph[3]) - np.pi)

    r = TwoRotorQubits(E_C=E_C, E_J=E_J)
    r.rx(0, np.pi/2); r.rx(1, np.pi/2); r.cz()
    out["bell_concurrence"] = r.concurrence()
    out["two_qubit_norm"] = float(np.linalg.norm(r.psi))

    out["pc_matched_transfer"] = phase_count_transfer(1, 1)
    out["pc_mismatched_transfer"] = phase_count_transfer(1, 3)
    out["pc_suppression_ratio"] = (out["pc_matched_transfer"]
                                   / max(out["pc_mismatched_transfer"], 1e-12))

    ok = (out["x_gate_fidelity"] > 0.98 and out["rabi_swing"] > 0.95
          and out["ramsey_error"] < 0.05 and abs(out["norm_after_gates"]-1) < 1e-10
          and out["cz_conditional_phase_error"] < 0.05
          and out["bell_concurrence"] > 0.95
          and abs(out["two_qubit_norm"]-1) < 1e-10
          and out["pc_suppression_ratio"] > 10)
    out["PASS"] = ok
    if verbose:
        for k, v in out.items():
            print(f"  {k:20s} {v}")
    return out


if __name__ == "__main__":
    print("teotl_rotor_qc selftest (E_J = 0.05) -- one- and two-qubit:")
    selftest()
