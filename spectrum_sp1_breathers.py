import json
import numpy as np

def hdr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70)

# ---------------------------------------------------------------------
# SP-1 (gate pre-registered in G0_prereg_spectrum.md BEFORE this run):
#   sine-Gordon quantum spectrum (DHN, exact): M_n = 2 M_k sin(n pi xi/2),
#   n = 1 .. < 1/xi.  Three breathers exist for xi <= 1/3.
#   GATE: PASS if any xi in (0, 1/3] gives (mu/e AND tau/mu within 5%)
#         or |Q_K - 2/3| < 0.01;  otherwise EXCLUSION logged.
#   Consecutive levels n = 1,2,3 only (no-tuning clause).
# ---------------------------------------------------------------------

MU_E, TAU_MU = 105.6583755/0.51099895, 1776.86/105.6583755
print(f"targets: mu/e = {MU_E:.3f}   tau/mu = {TAU_MU:.3f}   Q_K = 2/3")

xi = np.linspace(1e-6, 1/3, 400001)
x = np.pi*xi/2                                    # in (0, pi/6]
m1, m2, m3 = np.sin(x), np.sin(2*x), np.sin(3*x)  # ratios only; 2M_k drops
r21, r32 = m2/m1, m3/m2
QK = (m1+m2+m3)/(np.sqrt(m1)+np.sqrt(m2)+np.sqrt(m3))**2

hdr("SP-1  the exact sine-Gordon breather tower, whole coupling range")
print(f"m2/m1 = 2 cos(pi xi/2)      range ({r21.min():.4f}, {r21.max():.4f})"
      f"   target mu/e  = {MU_E:.1f}")
print(f"m3/m2 = sin(3x)/sin(2x)     range ({r32.min():.4f}, {r32.max():.4f})"
      f"   target tau/mu = {TAU_MU:.2f}")
print(f"Koide Q_K over all xi:      range ({QK.min():.4f}, {QK.max():.4f})"
      f"   target 2/3 = {2/3:.4f}")
print(f"  (limits: xi->0 tower m_n ~ n gives Q_K = {6/(1+np.sqrt(2)+np.sqrt(3))**2:.4f};"
      f"  xi=1/3 gives Q_K = {QK[-1]:.4f})")

pass_ratio = np.any((np.abs(r21/MU_E-1) < .05) & (np.abs(r32/TAU_MU-1) < .05))
pass_koide = np.any(np.abs(QK-2/3) < .01)
assert not pass_ratio and not pass_koide

hdr("SP-1 GATE: EXCLUSION (exact, parameter-free)")
print(f"""* m2/m1 <= 2 for EVERY coupling (exact bound: 2 cos(pi xi/2) < 2):
  the mu/e ratio 206.8 is unreachable by two orders of magnitude.
* m3/m2 in (1.155, 1.5): tau/mu = 16.8 unreachable.
* Q_K stays in ({QK.min():.4f}, {QK.max():.4f}) — a near-degenerate tower
  hugging the A=0 corner (Q_K = 1/3); it never approaches 2/3.
=> The integrable 1D excitation tower is EXCLUDED as a generation
   structure: exact result, no parameters, consecutive levels.
   (Structural lesson, PROPOSED: excitation towers of one object give
   O(1) ratios; the e:mu:tau hierarchy needs a different mechanism.)
   Arc continues to SP-2/3 (3D Q-ball tower is a different object).""")

out = dict(
    gate="SP-1 pre-registered 2026-07-11 in G0_prereg_spectrum.md",
    verdict="EXCLUSION -- exact: m2/m1<=2 (need 206.8), m3/m2 in "
            "(1.155,1.5) (need 16.8), Q_K in (%.4f,%.4f) (need 2/3)"
            % (QK.min(), QK.max()),
    r21_range=[float(r21.min()), float(r21.max())],
    r32_range=[float(r32.min()), float(r32.max())],
    QK_range=[float(QK.min()), float(QK.max())],
)
with open("outputs/SP1_breathers.json", "w") as f:
    json.dump(out, f, indent=2)
print("\n[results block written: outputs/SP1_breathers.json]")
