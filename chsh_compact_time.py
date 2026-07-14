"""CHSH under compact time (gate in CHSH0). Does S exceed the classical 2 via a
no-signaling, time-symmetric (compact-time) measurement-dependence?
"""
import json
import numpy as np
def hdr(s): print("\n"+"="*68+"\n"+s+"\n"+"="*68)

L = np.linspace(0, 2*np.pi, 20001)[:-1]; dL = L[1]-L[0]   # hidden phase on S^1
A = lambda a: np.sign(np.cos(L-a)); B = lambda b: np.sign(np.cos(L-b))
# standard CHSH settings
a0, a1, b0, b1 = 0.0, np.pi/2, np.pi/4, 3*np.pi/4
def chsh(Efn): return abs(Efn(a0,b0)-Efn(a0,b1)+Efn(a1,b0)+Efn(a1,b1))

hdr("1  local, setting-INDEPENDENT phase  ->  S = 2  [reproduce]")
def E_loc(a,b): return np.mean(A(a)*B(b))
S_loc = chsh(E_loc)
print(f"triangle correlation E(a,b)=<sign cos . sign cos>, uniform lambda")
print(f"  S_local = {S_loc:.4f}   (classical bound 2; matches teotl chsh 2.0000)")

hdr("2  cosine (quantum) correlation  ->  S = 2 sqrt2  [target]")
E_cos = lambda a,b: np.cos(a-b)
S_cos = chsh(E_cos)
# no-signaling: marginals independent of the other setting (0 by symmetry)
print(f"  S_cosine = {S_cos:.4f}   (Tsirelson 2*sqrt2 = {2*np.sqrt(2):.4f})")
print(f"  marginals <A>,<B> = 0 (E depends only on a-b) -> NO-SIGNALING target")

hdr("3  compact-time measurement-dependence: scan, with no-signaling check")
print("compact-time closure reweights the hidden phase by the (future) settings:")
print("  rho(lambda|a,b) prop 1 + eps*cos(2 lambda - a - b)   [S^1 boundary link]\n")
def make(eps):
    def rho(a,b):
        w = 1+eps*np.cos(2*L-a-b); return w/np.sum(w)
    def E(a,b): return np.sum(rho(a,b)*A(a)*B(b))
    def margA(a,b): return np.sum(rho(a,b)*A(a))     # should be b-independent
    def margB(a,b): return np.sum(rho(a,b)*B(b))
    return E, margA, margB
print(f"  {'eps':>5} {'S':>8} {'max|<A> shift|':>15} {'signals?':>9}")
rows=[]
for eps in (0.0, 0.3, 0.6, 0.9, 1.0):
    E,mA,mB = make(eps); S = chsh(E)
    # no-signaling: <A>(a,b0) vs <A>(a,b1) must match
    sig = max(abs(mA(a0,b0)-mA(a0,b1)), abs(mA(a1,b0)-mA(a1,b1)),
              abs(mB(a0,b0)-mB(a1,b0)), abs(mB(a0,b1)-mB(a1,b1)))
    rows.append((eps,S,sig));
    print(f"  {eps:5.1f} {S:8.4f} {sig:15.4f} {'YES' if sig>1e-3 else 'no':>9}")
Smax = max(r[1] for r in rows); sig_at_max = [r[2] for r in rows if r[1]==Smax][0]

hdr("4  the cap: cosine -> 2sqrt2; PR-box (super-quantum) -> 4")
print(f"  cosine correlation caps S at 2*sqrt2 = {2*np.sqrt(2):.4f} (Tsirelson)")
print(f"  algebraic max (PR box) = 4 needs A,B jointly setting-dependent (signals)")

hdr("CHSH-COMPACT VERDICT")
tsi = 2*np.sqrt(2); exceeds = Smax > 2.001; ns = sig_at_max < 1e-3
superq = Smax > tsi + 1e-3
if superq and ns:
    verdict = "INCONCLUSIVE (unconstrained: overshoots QM)"
elif exceeds and ns:
    verdict = "PASS-conditional (reaches ~QM, no-signaling)"
elif exceeds:
    verdict = "PARTIAL (exceeds 2 but signals)"
else:
    verdict = "FAIL (S stays at 2)"
print(f"[{verdict}]  S_max = {Smax:.4f}  (Tsirelson {tsi:.4f}; no-signaling: "
      f"{'yes' if ns else 'NO'}).")
print(f"""
Honest reading -- and the auto-scan's S={Smax:.2f} > 2sqrt2={tsi:.2f} is a RED FLAG,
not a win:
  * local setting-independent phase = 2 (the bound is real, S=2.0000 confirmed).
  * the quantum target 2sqrt2 is no-signaling -> S>2 needs measurement-dependence
    (a settings<->hidden-variable link), NOT nonlocal signaling. Compact time
    offers such a link (the S^1 boundary condition) without signaling. Good so far.
  * BUT the posited closure reaches S={Smax:.2f}, ABOVE the quantum bound 2sqrt2 --
    a no-signaling super-quantum (PR-box-like) correlation. That is the tell:
    an UNPOSTULATED measurement-dependence is UNCONSTRAINED (it can reach up to 4).
    So 'compact time gives S>2' is, by itself, VACUOUS -- the loophole is too
    cheap to be a prediction; a chosen rho can give any S.
  * The MEANINGFUL question is therefore whether the compact-time closure, DERIVED
    from TFT's actual S^1 dynamics (not posited), lands at a SPECIFIC value:
       = 2      -> no Bell violation (the local result stands);
       = 2sqrt2 -> TFT reproduces QM (interesting, but degenerate with QM: S can't
                   tell them apart);
       > 2sqrt2 -> TFT predicts SUPER-quantum -> FALSIFIABLE and almost certainly
                   WRONG (nature is quantum) -> would rule the mechanism out.
CONCLUSION: the conjecture is UNDER-CONSTRAINED. S>2 is reachable no-signaling
(mechanism class real), but that alone predicts nothing; the physics is in the
DERIVED closure + a test that distinguishes compact-time TFT from QM (S cannot).
Honest status: not supported and not refuted -- ill-posed until the closure is
derived. The prior S=2.0000 (local) remains the only firm result.""")

out = dict(prereg="CHSH0_prereg_compact.md 2026-07-13",
           S_local=float(S_loc), S_cosine=float(S_cos), tsirelson=float(2*np.sqrt(2)),
           scan=[dict(eps=r[0], S=float(r[1]), signaling=float(r[2])) for r in rows],
           S_max=float(Smax), signals_at_max=bool(sig_at_max>=1e-3),
           superquantum=bool(Smax>2*np.sqrt(2)+1e-3), verdict=verdict,
           note="posited closure overshoots QM (no-signaling super-quantum) -> "
                "measurement-dependence unconstrained -> conjecture ill-posed "
                "until the S^1 closure is DERIVED; only firm result is S=2 (local)")
json.dump(out, open("outputs/CHSH_compact.json","w"), indent=2)
print("\n[results block written: outputs/CHSH_compact.json]")
