"""Attempt: derive the Koide 45deg / sqrt(2) from a self-dual principle. Test candidate principles.

The sqrt(m) vector v decomposes into a 1-D 'democratic' mode e0=(1,1,1)/sqrt3 and a 2-D 'breaking'
subspace (the plane orthogonal to it). Koide's condition is:
      |v_parallel|^2 = |v_perp|^2      (the 1-D symmetric part = the 2-D breaking part)  -> a=sqrt(2).

Candidate principles that might FORCE this, tested honestly:
  (A) per-mode equipartition: c0^2 = c1^2 = c2^2 (all three orthonormal modes carry equal energy).
  (B) subspace self-duality: |v_par|^2 = |v_perp|^2 (1-D block = 2-D block).
Which one is Koide, and is either one FORCED by anything in TFT?
"""
import numpy as np

def Q_of_a(a): return (1 + a**2/2)/3          # Koide Q for amplitude a
def parallel_perp(a):
    # |v_par|^2 = 3 M^2 ; |v_perp|^2 = 3 M^2 a^2/2  (units M=1)
    return 3.0, 3.0*a**2/2

# --- observed leptons: which condition do they satisfy? ---
m = np.array([0.51099895, 105.6583755, 1776.86]); v = np.sqrt(m)
par = np.dot(v, np.ones(3)/np.sqrt(3))**2
perp = np.dot(v, v) - par
print("  observed leptons:  |v_par|^2 = {:.1f}   |v_perp|^2 = {:.1f}   ratio = {:.4f}".format(
      par, perp, perp/par))
print("  => the condition realized in nature is  |v_par|^2 = |v_perp|^2  (subspace balance).\n")

# --- (A) per-mode equipartition: c0=c1=c2 ---
# c0^2 = 3M^2 (democratic), c1^2+c2^2 = 3M^2 a^2/2. Equal per mode: c1^2=c2^2=c0^2 => 3M^2 a^2/2 = 2*3M^2
a_equi = np.sqrt(4.0)                          # a^2/2 = 2  -> a = 2
print("  (A) per-mode equipartition (c0=c1=c2):")
print(f"      forces a = {a_equi:.3f}  -> Q = {Q_of_a(a_equi):.3f}  -> sqrt(m)_min = M(1-{a_equi:.2f}) < 0  (UNPHYSICAL)")
print("      => WRONG: per-mode equipartition does not give Koide; it is not the principle.\n")

# --- (B) subspace self-duality: |v_par|^2 = |v_perp|^2 ---
a_dual = np.sqrt(2.0)                           # 3M^2 = 3M^2 a^2/2  -> a^2=2
print("  (B) subspace self-duality (1-D democratic block = 2-D breaking block):")
print(f"      forces a = sqrt(2) = {a_dual:.3f}  -> Q = {Q_of_a(a_dual):.4f} = 2/3   <-- THIS is Koide.")
print("      This is the correct condition. But it must be IMPOSED; nothing derived here forces")
print("      the 1-D and 2-D subspaces to balance. That balance is the unexplained content.\n")

print("  VERDICT (honest): the Koide sqrt(2) = a 1-D/2-D subspace self-duality of the sqrt(m) vector.")
print("  Per-mode equipartition (the obvious 'equal energy' principle) gives the WRONG, unphysical")
print("  answer (a=2). So the balance is specifically between the symmetric block and the breaking")
print("  block as WHOLES -- a genuine self-duality -- and NO TFT mechanism here forces it.")
print("  Suggestive-but-unproven lead: sqrt(2) is also the constant in canonical quantization")
print("  x=(a+a_dagger)/sqrt2 -- but identifying the two requires assumptions we cannot justify.")
print("  RESULT: NOT derived. The self-dual point is the right target; forcing it is genuinely open.")
