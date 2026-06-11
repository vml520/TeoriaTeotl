"""
Teotl QC — Milestone 3: CHSH / Bell test  (v2 — exact integrator)
───────────────────────────────────────────────────────────────────────────────
Question (Vic's conjecture): can a polynomial-resource TFT field on R³ × S¹,
with cyclical time active, produce CHSH S > 2?

Field state: 4 nodes [A0, A1, B0, B1], each carrying (m, θ) — equivalently
one complex amplitude c = √m·e^{iθ} per node. 8 real numbers total.
Dynamics: the Madelung kernel's exact generator, integrated via matrix
exponential (regular at m=0, exactly conservative). Same physics as
milestone 1; better integrator.

Honesty requirements:
  • single-shot ±1 outcomes: sign(m_q0 − m_q1) per qubit
  • identical pulse composite on exact 2-QUBIT Hilbert space (16 reals,
    tensor product) → must reach 2√2, proving protocol capability
  • CHSH angles grid-optimized per system
  • V2 no-signaling check: A's marginal vs B's setting
───────────────────────────────────────────────────────────────────────────────
"""
import numpy as np

# ── exact 2-level building blocks (shared by reference and field gates) ──────
sx = np.array([[0,1],[1,0]], complex)
I2 = np.eye(2, dtype=complex)
def Rz(a): return np.array([[np.exp(-1j*a/2),0],[0,np.exp(1j*a/2)]], complex)
def Rx(a): return np.cos(a/2)*I2 - 1j*np.sin(a/2)*sx
def meas_unitary(a):
    """Measure spin along equatorial axis a, built from Rz/Rx only."""
    return Rz(np.pi/2) @ Rx(np.pi/2) @ Rz(-np.pi/2) @ Rz(-a)

# ── exact 2-qubit reference (tensor product, 16 reals) ───────────────────────
def ref_singlet_E(a, b):
    psi = np.array([0, 1, -1, 0], complex)/np.sqrt(2)
    U = np.kron(meas_unitary(a), meas_unitary(b))
    p = np.abs(U @ psi)**2
    return p[0] - p[1] - p[2] + p[3]

# ── TFT field: 4 nodes, single shared excitation field (8 reals) ─────────────
def expmH(H, T):
    """exp(-i H T) for Hermitian H via eigendecomposition."""
    w, V = np.linalg.eigh(H)
    return (V * np.exp(-1j*w*T)) @ V.conj().T

def block_U(qubit, U2, g_e=0.0, T=1.0):
    """Embed a 2x2 gate on one qubit's basin pair; background inter-qubit
       hopping (A1<->B0, strength g_e) acts simultaneously if nonzero."""
    if g_e == 0.0:
        U = np.eye(4, dtype=complex)
        i = 0 if qubit == "A" else 2
        U[i:i+2, i:i+2] = U2
        return U
    # simultaneous gate + background coupling: build joint generator
    # gate generator G from U2 = exp(-i G T)
    w, V = np.linalg.eigh(U2 @ U2.conj().T)  # placeholder, not used
    raise RuntimeError("use gate_with_bg for g_e>0")

def gate_generator(kind, angle, T):
    """2x2 Hermitian generator H2 with exp(-i H2 T) = R{z,x}(angle)."""
    if kind == "z":
        return (angle/T) * np.diag([0.5, -0.5]).astype(complex) * -1  # Rz(a)=exp(-i a σz/2): H=(a/T)σz/2
    if kind == "x":
        return (angle/T) * (sx/2)
    raise ValueError(kind)

def H_embed(qubit, H2):
    H = np.zeros((4,4), complex)
    i = 0 if qubit == "A" else 2
    H[i:i+2, i:i+2] = H2
    return H

def H_bg(g_e):
    H = np.zeros((4,4), complex)
    H[1,2] = H[2,1] = -g_e
    return H

# fix Rz generator sign: Rz(a) = exp(-i a σz / 2), σz = diag(1,-1)
def Hz(qubit, angle, T):
    return H_embed(qubit, (angle/T) * np.diag([0.5,-0.5]).astype(complex))
def Hx(qubit, angle, T):
    return H_embed(qubit, (angle/T) * (sx/2))

T_GATE = 1.0   # nominal gate duration (exact integrator → value only matters
               # relative to background coupling strength in V2)

def measure_pulse_ops(qubit, a, g_e=0.0):
    """List of 4x4 unitaries implementing meas_unitary(a) on `qubit`,
       with background field coupling active during each segment (V2)."""
    segs = [("z", -a), ("z", -np.pi/2), ("x", np.pi/2), ("z", np.pi/2)]
    ops = []
    for kind, ang in segs:
        Hseg = (Hz if kind=="z" else Hx)(qubit, ang, T_GATE) + H_bg(g_e)
        ops.append(expmH(Hseg, T_GATE))
    return ops

def prepare_lambda_batch(L):
    """Singlet shadow: φ_A = λ, φ_B = λ+π, equal masses. c: (L,4)."""
    lam = np.linspace(0, 2*np.pi, L, endpoint=False)
    c = np.zeros((L,4), complex)
    c[:,0] = 1; c[:,1] = np.exp(1j*lam)
    c[:,2] = 1; c[:,3] = np.exp(1j*(lam+np.pi))
    c /= 2.0          # masses 0.25 each
    return c, lam

def outcomes(c):
    m = np.abs(c)**2
    A = np.where(m[:,0] >= m[:,1], +1, -1)
    B = np.where(m[:,2] >= m[:,3], +1, -1)
    return A, B

def selftest():
    print("── Self-tests ──")
    phis = np.linspace(0, 2*np.pi, 48, endpoint=False); a = 0.7
    pe = []
    for ph in phis:
        psi = np.array([1, np.exp(1j*ph)], complex)/np.sqrt(2)
        pe.append(abs((meas_unitary(a) @ psi)[0])**2)
    pe = np.array(pe)
    c = np.zeros((len(phis),4), complex)
    c[:,0]=1; c[:,1]=np.exp(1j*phis); c[:,2]=1; c[:,3]=1
    c /= 2.0
    for U in measure_pulse_ops("A", a):
        c = c @ U.T
    m = np.abs(c)**2
    pf = m[:,0]/(m[:,0]+m[:,1])
    err = np.max(np.abs(pe-pf))
    cons = abs((np.abs(c)**2).sum(1).mean() - 1.0)
    print(f"  field vs exact measurement P(+):  max err = {err:.2e}")
    print(f"  conservation drift = {cons:.2e}")
    assert err < 1e-9, "measurement composite mismatch"

def E_table_V1(angles, L=720):
    n = len(angles); E = np.zeros((n,n))
    opsA = {a: measure_pulse_ops("A", a) for a in angles}
    opsB = {b: measure_pulse_ops("B", b) for b in angles}
    for ia, a in enumerate(angles):
        for ib, b in enumerate(angles):
            c, lam = prepare_lambda_batch(L)
            for U in opsA[a]: c = c @ U.T
            for U in opsB[b]: c = c @ U.T
            A, B = outcomes(c)
            E[ia,ib] = np.mean(A*B)
    return E

def E_table_V2(angles, L=720, g_e=1.0, K_cycles=6, T_drift=2.0):
    """Connected field + cyclical time: measurement epoch repeats K times
       around S¹; background hopping active throughout."""
    n = len(angles)
    E = np.zeros((n,n)); PA = np.zeros((n,n)); PB = np.zeros((n,n))
    U_drift = expmH(H_bg(g_e), T_drift)
    opsA = {a: measure_pulse_ops("A", a, g_e) for a in angles}
    opsB = {b: measure_pulse_ops("B", b, g_e) for b in angles}
    for ia, a in enumerate(angles):
        for ib, b in enumerate(angles):
            c, lam = prepare_lambda_batch(L)
            for k in range(K_cycles):
                for U in opsA[a]: c = c @ U.T
                for U in opsB[b]: c = c @ U.T
                c = c @ U_drift.T
            A, B = outcomes(c)
            E[ia,ib]  = np.mean(A*B)
            PA[ia,ib] = np.mean(A == 1)
            PB[ia,ib] = np.mean(B == 1)
    return E, PA, PB

def chsh_from_table(E, angles):
    n = len(angles); best = (-np.inf, None)
    for ia in range(n):
        for iap in range(n):
            for ib in range(n):
                for ibp in range(n):
                    S = E[ia,ib]-E[ia,ibp]+E[iap,ib]+E[iap,ibp]
                    if abs(S) > best[0]: best = (abs(S),(ia,iap,ib,ibp))
    return best

def no_signaling(PA, PB):
    dA = np.max(np.abs(PA - PA.mean(axis=1, keepdims=True)))
    dB = np.max(np.abs(PB - PB.mean(axis=0, keepdims=True)))
    return dA, dB

if __name__ == "__main__":
    print("Teotl QC — Milestone 3: CHSH (exact integrator)\n")
    selftest()
    angles = np.linspace(0, np.pi, 12, endpoint=False)

    print("\n── REF: exact 2-qubit singlet (16-real tensor state) ──")
    Eref = np.array([[ref_singlet_E(a,b) for b in angles] for a in angles])
    S_ref, _ = chsh_from_table(Eref, angles)
    print(f"  S_quantum = {S_ref:.4f}   (Tsirelson 2√2 = {2*np.sqrt(2):.4f})")

    print("\n── V1: TFT field, isolated qubits (8-real field state, LHV) ──")
    E1 = E_table_V1(angles)
    S1, _ = chsh_from_table(E1, angles)
    print(f"  S_V1 = {S1:.4f}   (classical bound 2)")

    print("\n── V2: connected field + cyclical time (8-real field state) ──")
    rows = []
    for g_e in [0.25, 0.5, 1.0, 2.0, 4.0]:
        E2, PA, PB = E_table_V2(angles, g_e=g_e)
        S2, _ = chsh_from_table(E2, angles)
        dA, dB = no_signaling(PA, PB)
        rows.append((g_e, S2, dA, dB))
        print(f"  g_e={g_e:.2f}:  S_V2 = {S2:.4f}   no-signaling Δ: A={dA:.4f}  B={dB:.4f}")

    np.save("chsh_Eref.npy", Eref); np.save("chsh_E1.npy", E1)
    np.save("chsh_angles.npy", angles); np.save("chsh_v2.npy", np.array(rows))
    print("\nDone.")
