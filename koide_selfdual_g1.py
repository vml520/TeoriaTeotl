import numpy as np

# --- lepton masses (MeV, PDG) ---
m = np.array([0.51099895, 105.6583755, 1776.86])   # e, mu, tau
v = np.sqrt(m)                                       # sqrt-mass "amplitude" vector
N = 3

def hdr(s): print("\n"+"="*68+"\n"+s+"\n"+"="*68)

hdr("G1  Koide restated in TFT internal-circle (S^1) variables")

# --- 1. the Koide number ---
Q = m.sum()/v.sum()**2
print(f"Q = (sum m)/(sum sqrt m)^2 = {Q:.6f}   (Koide: 2/3 = {2/3:.6f})")

# --- 2. geometric form: angle of v to the democratic axis (1,1,1) ---
nhat = np.ones(3)/np.sqrt(3)
cos2 = (v@nhat)**2 / (v@v)
phi = np.degrees(np.arccos(np.sqrt(cos2)))
print(f"\nangle(v, (1,1,1)) : cos^2 = {cos2:.6f} (self-dual=1/2)  ->  phi = {phi:.4f} deg  (45 deg)")

# --- 3. symmetric / breaking split ---
vpar2  = (v.sum()**2)/3           # power in symmetric (DC) subspace
vperp2 = m.sum() - vpar2          # power in breaking subspace
print(f"\n|v_par|^2 (symmetric) = {vpar2:.4f}")
print(f"|v_perp|^2 (breaking) = {vperp2:.4f}")
print(f"ratio breaking/symmetric = {vperp2/vpar2:.6f}   (self-dual = 1.000000)")

# --- 4. the amplitude coefficient A  (v_k = M(1 + A cos theta_k)) ---
M = v.mean()
A = np.sqrt(2*vperp2/vpar2)
print(f"\nM = mean(sqrt m) = {M:.4f}")
print(f"A (fitted amplitude coefficient) = {A:.6f}   (Koide: sqrt2 = {np.sqrt(2):.6f})")

# --- 5. Fourier / DFT reading on the 3-point circle ---
F = np.fft.fft(v)
P0   = abs(F[0])**2                 # DC power  (harmonic |n|=0)
Pfun = abs(F[1])**2 + abs(F[2])**2  # fundamental power (n=+1 and n=-1)
print(f"\nDFT power  P(|n|=0) = {P0:.4f}")
print(f"DFT power  P(|n|=1) = {Pfun:.4f}   [= |F_+1|^2 + |F_-1|^2]")
print(f"ratio P(|n|=1)/P(|n|=0) = {Pfun/P0:.6f}   (self-dual = 1.000000)")
print(f"note reality ties them: |F_+1| = |F_-1| = {abs(F[1]):.4f} = {abs(F[2]):.4f}")

# --- 6. the crux: how you COUNT the breaking mode fixes A ---
hdr("The crux, made exact:  what does 'equipartition' count?")
def Q_from_ratio(r):        # r = breaking_power / symmetric_power
    # vperp2/vpar2 = r  ->  A^2 = 2r ;  Q = 1/3 + A^2/6 = 1/3 + r/3
    A2 = 2*r
    return 1/3 + A2/6, np.sqrt(A2)
for name, r in [("all power in symmetric (A=0)", 0.0),
                ("per-HARMONIC equipartition  P(|n|=0)=P(|n|=1)  -> ONE breaking mode", 1.0),
                ("per-REAL-MODE equipartition n=0,+1,-1 all equal -> TWO breaking modes", 2.0)]:
    q,a = Q_from_ratio(r)
    tag = "  <-- physical leptons" if abs(a-np.sqrt(2))<1e-6 else ""
    print(f"  {name:62s}:  A={a:.4f}  Q={q:.4f}{tag}")

print("""
READ:
  - DC (n=0) is one real mode. The breaking is the conjugate pair (n=+1,-1),
    tied by reality |F_+1|=|F_-1|.
  - Koide (A=sqrt2) = equal power PER HARMONIC |n|, counting the reality-locked
    pair (n=+-1) as ONE mode.
  - The ruled-out A=2 (Q=1) = counting n=+1 and n=-1 as TWO independent modes
    (naive per-real-dof equipartition).
  => The ENTIRE Koide content reduces to one yes/no question:
     does the first-harmonic breaking count as ONE mode or TWO?
""")
