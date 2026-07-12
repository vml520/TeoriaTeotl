"""E1 -- topological quantization of the dial offset, tested against its
own prediction class (E0_prereg_epsilon.md, sanctioned by Vic 2026-07-11).

Pre-registered: if winding topology sets the dial offset, the offset is a
2pi-rational angle. Candidate class: 2pi*p/q, gcd(p,q)=1, q <= 36, p<q.
Targets: eps, beta = delta-120deg, delta. Tolerance: 3 sigma_delta.
PASS = a match survives the look-elsewhere correction (hand p/q to E2).
FAIL = the simplest topological-quantization class is EXCLUDED.
Protocol: every nearest comparison reported, hit or miss.
"""
import json
from math import gcd
import numpy as np

def hdr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70)
w = np.exp(2j*np.pi/3)

def fit(mtau):
    m = np.array([0.51099895, 105.6583755, mtau])
    v = np.sqrt(m)
    c = np.array([v @ np.conj(w**(n*np.arange(3))) for n in range(3)])/3
    M, delta = c[0].real, np.angle(c[1])
    A = 2*abs(c[1])/M
    return delta, np.arccos(-1/A) - delta

MTAU, SIG = 1776.86, 0.12
delta, eps = fit(MTAU)
d_hi, e_hi = fit(MTAU+SIG); d_lo, e_lo = fit(MTAU-SIG)
sig_d = abs(d_hi-d_lo)/2
beta = delta - 2*np.pi/3
tol = 3*sig_d
targets = {"eps  ": eps, "beta ": beta, "delta": delta}
print(f"targets (rad): eps={eps:.7f}  beta={beta:.7f}  delta={delta:.7f}")
print(f"sigma_delta = {sig_d:.2e} rad; pre-registered tolerance 3 sigma = "
      f"{tol:.2e} rad")
print(f"(eps's own refit sigma is tighter, {abs(e_hi-e_lo)/2:.1e} rad; the "
      f"pre-registered 3 sigma_delta is the MORE permissive test)")

hdr("E1  scan: 2pi p/q, gcd(p,q)=1, q <= 36  (the closed candidate class)")
cands = sorted({(p, q) for q in range(1, 37) for p in range(1, q)
                if gcd(p, q) == 1})
vals = np.array([2*np.pi*p/q for p, q in cands])
print(f"candidates: {len(cands)} fractions in (0, 2pi)")
# look-elsewhere: chance of ANY hit if targets were random on (0, 2pi)
fp = 1 - (1 - len(cands)*2*tol/(2*np.pi))**len(targets)
print(f"look-elsewhere: expected whole-scan false-positive probability = "
      f"{fp*100:.2f}%  (well-posed test)")

hits = []
print(f"\n{'target':8s} {'nearest 2pi*p/q':>18s} {'value':>11s} "
      f"{'|diff| rad':>11s} {'z':>9s}  verdict")
for name, t in targets.items():
    order = np.argsort(np.abs(vals - t))
    for rank in range(3):
        i = order[rank]
        p, q = cands[i]
        d = abs(vals[i] - t); z = d/sig_d
        verdict = "HIT" if d < tol else "miss"
        if d < tol: hits.append((name.strip(), p, q, z))
        lbl = f"2pi*{p}/{q}"
        print(f"{name if rank==0 else '':8s} {lbl:>18s} {vals[i]:11.7f} "
              f"{d:11.2e} {z:9.0f}  {verdict}")

hdr("E1 VERDICT vs pre-registered gate")
if hits:
    print(f"HITS surviving tolerance: {hits} -> evaluate against the "
          f"{fp*100:.2f}% false-positive rate; hand p/q to E2.")
else:
    zmin = min(abs(vals - t).min()/sig_d for t in targets.values())
    print(f"""NO candidate within 3 sigma of ANY target (closest approach across
the whole scan: {zmin:.0f} sigma). VERDICT: **FAIL** -- the simplest
topological-quantization class (2pi-rational offsets, q <= 36) is
EXCLUDED for the dial offset. This kills the naive form of the escape
route flagged in M3/M4: if the dial is topologically locked, the OFFSET
itself is not a bare winding fraction -- any topological origin must
act through a derived, non-rational angle (exactly E2's territory:
forced coefficients from dynamics, not bare fractions).
Honest note: this was the recorded prior. The record now owns the fact.
Per E0: proceed to E2 (independent stage) when authorized.""")

out = dict(
    prereg="E0_prereg_epsilon.md (sanctioned 2026-07-11), stage E1",
    targets_rad=dict(eps=float(eps), beta=float(beta), delta=float(delta)),
    sigma_delta=float(sig_d), tolerance=float(tol),
    n_candidates=len(cands), false_positive_rate=float(fp),
    hits=hits,
    closest_z=float(min(abs(vals - t).min()/sig_d for t in targets.values())),
    verdict="FAIL -- 2pi-rational class (q<=36) excluded for eps, beta, "
            "delta; naive topological quantization of the dial offset dead; "
            "E2 remains authorized-pending",
)
with open("outputs/E1_topo.json", "w") as f:
    json.dump(out, f, indent=2)
print("\n[results block written: outputs/E1_topo.json]")
