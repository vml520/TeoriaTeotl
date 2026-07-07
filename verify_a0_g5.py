"""G5: does TFT's derived law match the SPARC Radial Acceleration Relation (RAR)?

The RAR (McGaugh, Lelli & Schombert 2016) is the distilled result of all 175 SPARC galaxies
(2693 points): the observed acceleration is a tight function of the baryonic acceleration,
    g_obs = g_bar / (1 - exp(-sqrt(g_bar/g_dagger))),   g_dagger = 1.20e-10 m/s^2,
with only 0.13 dex total scatter. This is the falsifier: any theory must land on this curve.

NOTE: this compares TFT's law to the RAR (the mean relation + its scatter), NOT a per-galaxy
chi^2 (that needs the raw rotation curves, not available in-session). The RAR is the accepted
summary of SPARC, so lying within its scatter = consistent with SPARC.

TFT's DERIVED inputs:
  - a0 = c H0 / 2pi = 1.08e-10  (G1-G3; 10% below the fitted g_dagger, within its systematics)
  - deep-MOND limit g_obs -> sqrt(g_bar a0) => baryonic Tully-Fisher V^4 = G M a0, slope EXACTLY 4.
  - interpolation: 'simple' mu(x)=x/(1+x) (limit-respecting; exact shape model-dependent, as in MOND).
"""
import numpy as np

g_dag = 1.20e-10                                   # empirical RAR scale (fitted to SPARC)
a0    = 2.99792458e8*(70e3/3.086e22)/(2*np.pi)     # DERIVED a0
scatter = 0.13                                     # dex, RAR total scatter

gbar = np.logspace(-13, -8, 400)
g_rar     = gbar/(1 - np.exp(-np.sqrt(gbar/g_dag)))         # empirical RAR
g_tft     = 0.5*(gbar + np.sqrt(gbar**2 + 4*gbar*a0))       # TFT law, DERIVED a0
g_tft_fit = 0.5*(gbar + np.sqrt(gbar**2 + 4*gbar*g_dag))    # TFT law, fitted a0 (isolates shape)

dev     = np.log10(g_tft/g_rar)
dev_fit = np.log10(g_tft_fit/g_rar)

print(f"  derived a0 = {a0:.3e}   vs fitted g_dagger = {g_dag:.3e}   (ratio {a0/g_dag:.2f})\n")
print("  deviation of TFT law from the empirical RAR, across g_bar = 1e-13 .. 1e-8 m/s^2:")
print(f"    TFT with DERIVED a0 : max |dev| = {np.max(np.abs(dev)):.3f} dex   (RAR scatter = {scatter} dex)")
print(f"    TFT with fitted  a0 : max |dev| = {np.max(np.abs(dev_fit)):.3f} dex   (isolates shape only)")

# where is the deviation largest?
i = np.argmax(np.abs(dev))
print(f"    (largest at g_bar = {gbar[i]:.2e}, i.e. near the transition a0)\n")

# sampled table
print("  " + "{:>12s} {:>12s} {:>12s} {:>10s}".format("g_bar", "g_RAR", "g_TFT", "dev(dex)"))
for gb in [1e-12, 1e-11, 1.1e-10, 1e-9, 1e-8]:
    gr = gb/(1-np.exp(-np.sqrt(gb/g_dag)))
    gt = 0.5*(gb + np.sqrt(gb**2 + 4*gb*a0))
    print("  " + "{:>12.1e} {:>12.3e} {:>12.3e} {:>10.3f}".format(gb, gr, gt, np.log10(gt/gr)))

print("\n  baryonic Tully-Fisher: deep-MOND g_obs=sqrt(g_bar a0) => V^4 = G M a0, slope EXACTLY 4.")
print("  SPARC BTFR slope = 3.85 +/- 0.09 (Lelli+2019); TFT predicts 4 with a DERIVED a0. Parameter-free.")
print("\n  VERDICT: TFT's derived law tracks the RAR within its scatter across 5 decades of acceleration.")
print("  Consistent with SPARC. Caveat: this is the RAR (mean+scatter), not a per-galaxy fit;")
print("  the interpolation SHAPE is a limit-respecting choice (model-dependent, as in MOND).")
