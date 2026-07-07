"""What is the sqrt(2) really asking for? Reframing Koide's amplitude into its cleanest geometric form.

sqrt(m)_k = M(1 + sqrt(2) cos(delta + 2pi k/3)).  The amplitude sqrt(2) <=> Q=2/3. Equivalent forms:
  (i)   the vector v=(sqrt(m_e),sqrt(m_mu),sqrt(m_tau)) makes a 45-degree angle with the
        'democratic' axis (1,1,1): its component ALONG (1,1,1) equals its component PERPENDICULAR.
        i.e. |symmetric part| = |symmetry-breaking part|  (EQUIPARTITION).
  (ii)  RMS of the fluctuation of sqrt(m) equals the mean of sqrt(m).
  (iii) Q=2/3 is the exact MIDPOINT of the allowed range [1/3 (all equal) .. 1 (one dominant)].
So 'why sqrt(2)' = 'why do the symmetric and the breaking modes carry EQUAL weight' (45 deg).
Verify all three on the real lepton masses.
"""
import numpy as np

m = np.array([0.51099895, 105.6583755, 1776.86])   # e, mu, tau (MeV)
v = np.sqrt(m)                                       # the sqrt(m) vector

# (i) decompose v into democratic (1,1,1) part and perpendicular (breaking) part
d = np.ones(3)/np.sqrt(3)
v_par = np.dot(v, d)                                 # length along (1,1,1)
v_perp = np.sqrt(np.dot(v,v) - v_par**2)             # length perpendicular
angle = np.degrees(np.arctan2(v_perp, v_par))
print("  (i) tilt of the sqrt(m) vector from the equal-mass axis (1,1,1):")
print(f"      |symmetric part|  = {v_par:.3f}")
print(f"      |breaking part|   = {v_perp:.3f}")
print(f"      angle = {angle:.3f} deg     (sqrt(2) <=> exactly 45 deg, |sym| = |breaking|)\n")

# (ii) RMS fluctuation of sqrt(m) vs mean
mean = v.mean(); rms_fluc = np.sqrt(((v-mean)**2).mean())
print("  (ii) fluctuation vs mean of sqrt(m):")
print(f"      mean(sqrt m)          = {mean:.3f}")
print(f"      RMS fluctuation       = {rms_fluc:.3f}     (sqrt(2) <=> these are EQUAL)\n")

# (iii) Q vs the range midpoint
Q = m.sum()/v.sum()**2
print("  (iii) Koide Q vs its allowed range:")
print(f"      Q = {Q:.5f} ;  range = [1/3={1/3:.4f} (all equal) .. 1 (one dominant)] ;  midpoint = {2/3:.4f}")
print(f"      Q sits at the exact MIDPOINT.\n")

print("  => the sqrt(2) is EQUIPARTITION: the 'average' and the 'difference' of the sqrt-masses")
print("     carry equal weight (a 45-degree tilt). That is the single fact TFT must produce.")
print("  HONEST: this REFRAMES 'why sqrt(2)' into 'why equipartition / 45 deg' -- a more physical,")
print("  suggestive target (a self-dual / critical balance of symmetric vs symmetry-breaking modes).")
print("  It is NOT a derivation. Koide's value is still unexplained; we have only found its cleanest form.")
