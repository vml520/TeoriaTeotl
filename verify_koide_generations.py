"""Three generations as three phases of one particle -> the Koide relation.

Vic's idea: e, mu, tau are the SAME object at three phases. The natural way to place three states
symmetrically on a phase circle is 120 degrees apart (a Z3 / three-fold structure). Write

    sqrt(m_k) = M ( 1 + sqrt(2) cos(delta + 2*pi*k/3) ),   k = 0,1,2

This is EXACTLY Koide's empirical relation (1981): with three phases 120 apart and amplitude sqrt(2),
    Q = (m_e + m_mu + m_tau) / (sqrt(m_e)+sqrt(m_mu)+sqrt(m_tau))^2 = 2/3   (identically).

Two free numbers (overall scale M, phase offset delta) fix three masses -> ONE genuine prediction.
Test with NO knobs tuned to the answer: given the electron and muon, PREDICT the tau.
"""
import numpy as np

# measured charged-lepton masses (MeV) -- PDG
m_e, m_mu, m_tau = 0.51099895, 105.6583755, 1776.86

# --- 1. Koide's Q for the measured masses ---
se, smu, st = np.sqrt([m_e, m_mu, m_tau])
Q = (m_e+m_mu+m_tau)/(se+smu+st)**2
print(f"  Koide Q (measured e, mu, tau) = {Q:.6f}   (three-phase structure forces 2/3 = {2/3:.6f})\n")

# --- 2. PREDICT tau from e and mu only (no tau input) ---
A, B = m_e+m_mu, se+smu
st_pred = 2*B + np.sqrt(6*B**2 - 3*A)         # solve Q=2/3 for sqrt(m_tau)
m_tau_pred = st_pred**2
print("  predict the tau from the electron and muon alone (Q=2/3, nothing tuned to tau):")
print(f"    m_tau predicted = {m_tau_pred:.2f} MeV")
print(f"    m_tau measured  = {m_tau:.2f} MeV")
print(f"    agreement: {100*abs(m_tau_pred-m_tau)/m_tau:.3f}% \n")

# --- 3. show the three-phase form reproduces all three masses ---
M = (se+smu+st)/3
# recover delta from the electron: (se/M - 1)/sqrt(2) = cos(delta)
delta = np.arccos((se/M - 1)/np.sqrt(2))
print("  three phases 120 deg apart on a circle, amplitude sqrt(2):")
print("  " + "{:>10s} {:>12s} {:>12s}".format("k (gen)", "sqrt(m) form", "sqrt(m) meas"))
for k,(nm,sm) in enumerate([("e",se),("mu",smu),("tau",st)]):
    form = M*(1 + np.sqrt(2)*np.cos(delta + 2*np.pi*k/3))
    print("  " + "{:>10s} {:>12.4f} {:>12.4f}".format(nm, form, sm))

print("\n  => the three generations sit at 120-degree phases of one object, and that structure")
print("     PREDICTS the tau mass to ~0.01%. This is Koide's relation -- and it is exactly")
print("     'three phases of a single particle.'")
print("  HONEST STATUS: Koide (1981) is EMPIRICAL and unexplained for 40+ years. What is TFT's to")
print("  derive: (a) three-fold phase structure (why 3 -- plausibly the S^1 / SU(3) three-fold),")
print("  (b) the sqrt(m) relation, (c) the amplitude sqrt(2) that fixes Q=2/3. (c) is the crux and")
print("  is NOT derived. If TFT derives it, the tau mass is a FORCED, falsifiable prediction.")
