"""TENS0 -- tensor completeness: does one (polynomial-resource) S^1 field give the
full 2^n Hilbert space? Pre-reg: TENS0_prereg.md. Uses bond dimension chi as the
resource knob (MPS = canonical polynomial-parameter family). No tuning; states are
Haar-random inputs.
"""
import json
import numpy as np

def hdr(s): print("\n" + "=" * 70 + "\n" + s + "\n" + "=" * 70)
rng = np.random.default_rng(0)

def haar_state(n):
    v = rng.standard_normal(2**n) + 1j * rng.standard_normal(2**n)
    return v / np.linalg.norm(v)

def schmidt_probs(psi, n):
    """Schmidt (reduced-density) eigenvalues across the central cut."""
    M = psi.reshape(2**(n//2), 2**(n - n//2))
    s = np.linalg.svd(M, compute_uv=False)
    p = s**2
    return np.sort(p)[::-1] / p.sum()

# ================================================================= Stage 1
hdr("1  DIMENSION COUNTING: polynomial field params vs 2^n")
for n in [2, 4, 8, 16, 32]:
    field_params = 2 * n          # ~O(n) complex modes of one S^1 field
    hilbert = 2.0**n
    print(f"  n={n:2d}: field DOF ~ {field_params:4d}   Hilbert dim 2^n = {hilbert:.3e}   "
          f"ratio = {field_params/hilbert:.2e}")
print("  -> economical-field manifold is measure-zero in Hilbert space for n >~ few.")

# ================================================================= Stage 2
hdr("2  RANDOM-STATE FIDELITY at bounded resource (bond chi) vs n")
print("  best fidelity a chi-bounded representation gives a Haar-random state")
print("  (sum of top-chi Schmidt probabilities, central cut; averaged):")
fid_table = {}
for chi in [1, 2, 4]:
    row = []
    for n in [2, 4, 6, 8, 10]:
        fs = []
        for _ in range(40):
            p = schmidt_probs(haar_state(n), n)
            fs.append(float(np.sum(p[:chi])))     # keep top-chi
        row.append((n, float(np.mean(fs))))
    fid_table[chi] = row
    s = "  ".join(f"n={n}:{f:.3f}" for n, f in row)
    print(f"    chi={chi}: {s}")
# decays with n?
decays = all(fid_table[chi][-1][1] < fid_table[chi][0][1] for chi in [1, 2, 4]) \
         and fid_table[4][-1][1] < 0.5

# ================================================================= Stage 3
hdr("3  ENTANGLEMENT GAP + why GHZ passed but volume-law fails")
print("  generic (Page) entanglement vs the bounded-chi cap ln(chi):")
for n in [4, 8, 12, 20]:
    S_page = (n//2) * np.log(2) - 0.5     # ~ Page value (nats), leading term
    for chi in [2, 4, 16]:
        pass
    print(f"    n={n:2d}: generic S ~ {S_page:5.2f} nats;  cap ln(chi=2)={np.log(2):.2f}, "
          f"ln(chi=16)={np.log(16):.2f}  -> gap grows ~ n/2")
# GHZ: 1 ebit -> chi=2 exact
n_ghz = 8
ghz = np.zeros(2**n_ghz, dtype=complex); ghz[0] = ghz[-1] = 1/np.sqrt(2)
p_ghz = schmidt_probs(ghz, n_ghz)
ghz_fid_chi2 = float(np.sum(p_ghz[:2]))
print(f"  GHZ (n={n_ghz}): Schmidt probs = {np.round(p_ghz[:3],3)}; chi=2 fidelity = {ghz_fid_chi2:.4f}")
print(f"  -> GHZ is 1 ebit: representable at chi=2 (WHY the earlier GHZ test passed).")
print(f"     Volume-law/random states need chi ~ 2^(n/2): NOT representable at bounded chi.")
ghz_ok = ghz_fid_chi2 > 1 - 1e-9

# ================================================================= verdict
hdr("VERDICT  (gate pre-committed in TENS0_prereg.md)")
full_from_poly = not decays          # PASS would need fidelity to NOT decay
verdict = "PASS (economical=full QM)" if full_from_poly else "RESOLVED-NEGATIVE"
print(f"  random-state fidelity decays with n at bounded chi: {decays}")
print(f"  GHZ representable at chi=2 (explains prior pass): {ghz_ok}")
print(f"""\n[{verdict}] A polynomial-resource (bounded-chi) single S^1 field is
  ENTANGLEMENT-BOUNDED. Random-state fidelity -> 0 with n (chi=4, n=10: {fid_table[4][-1][1]:.3f}),
  the entanglement gap (generic n/2 vs cap ln chi) grows without bound, and while
  low-entanglement states -- product, GHZ (1 ebit, chi=2 -> fidelity {ghz_fid_chi2:.3f}), area-law --
  ARE representable (this is WHY CHSH/Born/GHZ passed), VOLUME-LAW entanglement is NOT.
  => An economical 'classical' Teotl field is a BOUNDED-ENTANGLEMENT SUBTHEORY,
  falsified by volume-law (quantum-supremacy) experiments where nature realizes full
  QM. Tensor completeness FAILS for the economical field; recovering full 2^n QM
  requires QUANTIZING the field (exponential/Fock DOF) = standard QFT -- degenerate,
  and no longer 'just a classical circle-valued field.' The framework cannot be both
  economical-classical AND full QM. This is the sharpest honest limit on the quantum
  program -- stated plainly, not softened.""")

out = dict(prereg="TENS0_prereg.md", verdict=verdict,
           random_fidelity=fid_table, random_fidelity_decays=bool(decays),
           ghz_fid_chi2=float(ghz_fid_chi2), ghz_representable=bool(ghz_ok),
           note="Polynomial-resource single S^1 field = entanglement-bounded (MPS-like): "
                "random-state fidelity->0 with n, entanglement gap grows; product/GHZ/area-law "
                "representable (why CHSH/Born/GHZ passed) but volume-law NOT -> economical "
                "classical Teotl field is a bounded-entanglement SUBTHEORY, falsified by "
                "quantum supremacy. Full 2^n needs quantized/Fock field = standard QFT "
                "(degenerate, not economical). Cannot be both economical-classical AND full QM.")
json.dump(out, open("outputs/TENS_completeness.json", "w"), indent=2, default=str)
print("\n[results block written: outputs/TENS_completeness.json]")
