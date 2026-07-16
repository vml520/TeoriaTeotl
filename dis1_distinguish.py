"""DIS0 -- hunting a distinguishing observable (compact-time TFT vs standard QM).
Pre-reg: DIS0_prereg.md.  Two channels tested + a scale/feasibility scoping.
No tuning; energies and settings are inputs, deviations are read out.
"""
import json
import numpy as np

def hdr(s): print("\n" + "=" * 70 + "\n" + s + "\n" + "=" * 70)
hbar_eVs = 6.582119569e-16          # eV*s
H0 = 2.19e-18                        # 1/s  (H0 ~ 67.7 km/s/Mpc)
mec2 = 511e3                         # eV

# ================================================================= Stage 1
hdr("1  BELL channel: discretize/compactify the time circle -> does E(a,b) move?")
def E_ring(a, b, N, d0=0.0):
    """Closure correlation with the hidden time-phase on N discrete ring points."""
    phi = 2*np.pi*np.arange(N)/N
    thA, thB = phi, phi - d0
    amp = np.exp(1j*(thA - a)) * np.conj(np.exp(1j*(thB - b)))
    return np.mean(amp).real
# CHSH at the standard optimal angles
a0, a1, b0, b1 = 0.0, np.pi/2, np.pi/4, 3*np.pi/4
def S_ring(N):
    return abs(E_ring(a0,b0,N) - E_ring(a0,b1,N) + E_ring(a1,b0,N) + E_ring(a1,b1,N))
grid = np.linspace(0, 2*np.pi, 50)
max_dev, max_S_dev = 0.0, 0.0
for N in [2, 3, 5, 10, 1000]:
    dev = max(abs(E_ring(a,b,N) - np.cos(a-b)) for a in grid for b in grid)
    Sdev = abs(S_ring(N) - 2*np.sqrt(2))
    max_dev = max(max_dev, dev); max_S_dev = max(max_S_dev, Sdev)
    print(f"  N={N:5d}: max|E_N - cos(a-b)| = {dev:.2e}   |S_N - 2sqrt2| = {Sdev:.2e}")
print("  -> the hidden time-phase CANCELS (correlation depends on the setting")
print("     DIFFERENCE only) => Bell channel is degenerate at ANY loop size N.")
bell_degenerate = (max_dev < 1e-12) and (max_S_dev < 1e-12)

# ================================================================= Stage 2
hdr("2  ENERGY/TEMPORAL channel: compact time -> energy comb + exact revival")
print("single-valuedness e^{-iET}=1 on period T  =>  E_n = 2*pi*n / T  (a comb).")
# (a) snap distortion of an arbitrary target energy onto the comb, vs T
print("(a) distortion to snap arbitrary energies onto the comb (<= pi/T, -> 0):")
targets = np.array([1.0, np.sqrt(2), np.e])      # arbitrary real energies (units 1/s-ish)
snap_tab = {}
for T in [1.0, 10.0, 100.0, 1e4]:
    g = 2*np.pi/T
    snapped = np.round(targets/g)*g
    dmax = np.max(np.abs(targets - snapped))
    snap_tab[T] = dmax
    print(f"    T={T:8.0f}: comb spacing g={g:.3e}, max snap |dE| = {dmax:.3e}  (bound pi/T={np.pi/T:.3e})")
snap_vanishes = snap_tab[1e4] < snap_tab[1.0]     # distortion shrinks with T

# (b) revival: incommensurate 3-level system
print("(b) revival of a 3-level system, incommensurate energies [1, sqrt2, sqrt3]:")
E = np.array([1.0, np.sqrt(2), np.sqrt(3)]); w = np.ones(3)/3
t = np.linspace(0.01, 5000, 500000)
A = np.abs(w @ np.exp(-1j*np.outer(E, t)))        # QM autocorrelation |<psi(0)|psi(t)>|
qm_max_revival = A.max()
print(f"    QM: max|A(t)| over t<=5000 = {qm_max_revival:.5f}  (quasiperiodic; near-revives")
print(f"        arbitrarily close to 1 at irregular times -> amplitude alone does NOT separate)")
# compact time: snap E onto comb of period T => A(T) = 1 exactly
for T in [50.0, 500.0]:
    g = 2*np.pi/T; Esnap = np.round(E/g)*g
    A_T = abs(w @ np.exp(-1j*Esnap*T))
    frac_dist = np.max(np.abs(E-Esnap)/E)
    print(f"    compact T={T:6.0f}: |A(T)| = {A_T:.5f} (EXACT revival); spectrum distorted "
          f"by dE/E <= {frac_dist:.2e} (-> 0 as T grows)")
# (c) time-winding interference: phase per full loop = E*T = 2*pi*n on-comb
wind_phase = np.max(np.abs(np.mod(Esnap*T, 2*np.pi)))   # = 0 mod 2pi for on-comb E
print(f"(c) time-winding interference: max(E*T mod 2pi) on-comb = {wind_phase:.2e}")
print("    -> winding sectors differ by e^{i2*pi*n}=1 => NO observable interference.")

# ================================================================= Stage 3
hdr("3  SCALE / FEASIBILITY (scoping, not a gate): insert TFT's own S^1 period")
T_cosmo = 2*np.pi/H0
dE_cosmo = hbar_eVs * 2*np.pi / T_cosmo           # = hbar*H0
print(f"  cosmological S^1  T=2pi/H0 = {T_cosmo:.3e} s (~{T_cosmo/3.15e7:.1e} yr, ~age of universe)")
print(f"    comb spacing dE = hbar*H0 = {dE_cosmo:.2e} eV  -> UNOBSERVABLE")
omega_C = mec2/hbar_eVs
dE_compton = hbar_eVs * omega_C                    # = m_e c^2
print(f"  microscopic (Compton) S^1  T=2pi/omega_C: comb spacing dE = m_e c^2 = {dE_compton:.3e} eV")
print(f"    -> energies quantized in units of 511 keV; eV atomic lines FORBIDDEN => EXCLUDED by data.")
print("  => only cosmological T survives; there every distinguishing effect is unobservable.")

# ================================================================= verdict
hdr("VERDICT  (gate pre-committed in DIS0_prereg.md)")
# PASS needs an order-1, T-INDEPENDENT separation. We found none: Bell exactly
# degenerate; temporal differences (comb, revival) all scale as 1/T; winding null.
found_T_independent = False
comb_exists = True                                 # E_n = 2pi n / T is a real, structural difference
if found_T_independent:
    verdict = "PASS"
elif comb_exists and snap_vanishes and bell_degenerate:
    verdict = "PARTIAL"
else:
    verdict = "FAIL"
print(f"""[{verdict}] No T-INDEPENDENT distinguishing observable found (no PASS/prize).
  * BELL channel: EXACTLY degenerate for any loop size N (hidden time-phase
    cancels; max|E_N-cos|={max_dev:.1e}, |S_N-2sqrt2|={max_S_dev:.1e}) -- upgrades the
    numerical 2sqrt2 to a structural statement: CHSH can NEVER distinguish them.
  * TEMPORAL channel: compact time DOES differ from QM -- a real energy comb
    E_n=2pi n/T, and revival that is EXACT + strictly periodic at a single T
    (QM near-revives quasiperiodically, max|A|={qm_max_revival:.4f}, at irregular times -- so the
    clean separator is the comb's structural discreteness, not revival amplitude)
    -- but every such effect scales as 1/T and vanishes as T->infinity.
  * SCALE: the only T consistent with observed continuously-tunable spectra is
    cosmological (comb ~1e-33 eV, revival ~age of universe = unobservable); a
    microscopic T is excluded (would quantize energy in m_e c^2 units).
  * WINDING: time-winding sectors are degenerate (phase 2*pi*n) -- no signal.
  DISTINGUISHABLE IN PRINCIPLE (the energy comb / exact revival), EMPIRICALLY
  DEGENERATE IN PRACTICE. Sharpest in-principle falsifier: forbidden transition
  frequencies between comb teeth -> observed continuous spectra bound T >~ 1/H0,
  already satisfied. The quantum reinterpretation is not experimentally separable
  from QM by any feasible measurement -- an honest negative, quantified.""")

out = dict(prereg="DIS0_prereg.md", verdict=verdict,
           bell_max_dev=float(max_dev), bell_S_dev=float(max_S_dev),
           bell_degenerate_any_N=bool(bell_degenerate),
           qm_max_revival=float(qm_max_revival),
           snap_distortion_T=snap_tab, snap_vanishes_with_T=bool(snap_vanishes),
           winding_phase_residual=float(wind_phase),
           comb_spacing_cosmo_eV=float(dE_cosmo), comb_spacing_compton_eV=float(dE_compton),
           T_independent_separation_found=bool(found_T_independent),
           note="No T-independent (order-1) distinguisher. Bell channel exactly "
                "degenerate any N (hidden phase cancels). Temporal channel differs "
                "(energy comb E_n=2pi n/T, exact revival) but scales 1/T; at TFT's "
                "cosmological S^1 unobservable, microscopic T excluded by continuous "
                "spectra. Winding degenerate. Distinguishable in principle, "
                "empirically degenerate in practice; falsifier bounds T>~1/H0 (met).")
json.dump(out, open("outputs/DIS_stage.json", "w"), indent=2, default=str)
print("\n[results block written: outputs/DIS_stage.json]")
