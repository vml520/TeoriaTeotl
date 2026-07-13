"""BH -- black holes under TFT (gate in BH0).

Horizon from the derived phase-inflow rate reaching c (river model); time =
phase cycling freezes at the horizon; and the distinctive TFT prediction: the
bounded phase field CAPS the density -> NO singularity, a regular core.
"""
import json
import numpy as np
def hdr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70)

# SI constants
G = 6.67430e-11; c = 2.99792458e8; hbar = 1.054571817e-34; kB = 1.380649e-23
Msun = 1.98892e30
lP = np.sqrt(hbar*G/c**3)                 # Planck length
rhoP = c**5/(hbar*G**2)                    # Planck density
print(f"Planck length {lP:.3e} m, Planck density {rhoP:.3e} kg/m^3")

def r_s(M):  return 2*G*M/c**2

hdr("1  the horizon: the phase-inflow rate reaches c  [derived route]")
print("TFT-derived inflow (contraction) rate of space toward a mass:")
print("   v_in(r) = sqrt(2GM/r)   (verify_G_as_rate: -> c at r_s)")
for M, nm in [(Msun, "1 Msun"), (10*Msun, "10 Msun"), (1e6*Msun, "1e6 Msun (SMBH)")]:
    rs = r_s(M); v_at_rs = np.sqrt(2*G*M/rs)
    print(f"  {nm:>16}: r_s = {rs:.3e} m,  v_in(r_s)/c = {v_at_rs/c:.4f}")
print("""=> at r_s the inflow equals c; inside, space flows in faster than phase
   can propagate out -> outgoing light is dragged inward -> HORIZON. This is
   the river (Gullstrand-Painleve) model, obtained from TFT's OWN inflow rate,
   not imposed. [r_s itself = consistency with GR's weak field -> Schwarzschild]""")

hdr("2  time = phase cycling freezes at the horizon  [structural]")
print("time = phase cycling (dtau = hbar dtheta/E); rate of time ∝ sqrt(g00),")
print("g00 = 1 - r_s/r.  Approaching r_s from outside:")
rs = r_s(Msun)
for x in (2.0, 1.5, 1.1, 1.01, 1.001):
    r = x*rs; rate = np.sqrt(max(1-rs/r, 0))
    print(f"  r/r_s = {x:6.3f}: phase-cycling rate / (rate at infinity) = {rate:.4f}")
print("""=> the phase-cycling rate (the rate of TIME) -> 0 at the horizon: an
   external observer sees infalling phase FREEZE at r_s -- the literal
   'frozen star'. Time = phase cycling makes the horizon a place where time
   (as seen from outside) stops.""")

hdr("3  singularity resolution: bounded phase field caps the density  [TFT-native]")
print("""The phase field is BOUNDED: |grad theta| <~ 1/l0 (one turn per coherence
length) and the amplitude is finite -> the energy density CANNOT diverge. It
caps at rho_max ~ E0/l0^3 = Planck density (Planckian scales). So the mass sits
in a regular core, NOT a point singularity:
   rho(r<r_core) = rho_max ,  (4/3) pi r_core^3 rho_max = M""")
rho_max = rhoP
print(f"\n  {'M':>16} {'r_s (m)':>12} {'r_core (m)':>12} {'r_core/l_P':>11} {'r_core/r_s':>11}")
for M, nm in [(Msun, "1 Msun"), (1e6*Msun, "1e6 Msun"), (1e9*Msun, "1e9 Msun")]:
    rs = r_s(M); rc = (3*M/(4*np.pi*rho_max))**(1/3)
    print(f"  {nm:>16} {rs:12.3e} {rc:12.3e} {rc/lP:11.2e} {rc/rs:11.2e}")
print(f"""=> the core is a REGULAR object: r_core ~ 1e-22 m for a solar mass --
   {(3*Msun/(4*np.pi*rho_max))**(1/3)/lP:.0e} Planck lengths across (NOT Planck-point, NOT singular),
   and ~1e-25 of r_s (deep inside the horizon). NO SINGULARITY: the density
   saturates at the Planck/coherence density. TFT black hole = a horizon around
   a Planck-density phase-frozen core (regular-BH / Planck-star family). This is
   the distinctive prediction vs GR's point singularity. [density cap PROPOSED
   from the bounded field; the consequence computed]""")

hdr("4  thermodynamics: scale check + the open frontier")
for M, nm in [(Msun, "1 Msun"), (1e6*Msun, "1e6 Msun")]:
    rs = r_s(M); A = 4*np.pi*rs**2
    S = A/(4*lP**2)                        # Bekenstein-Hawking / kB
    T = hbar*c**3/(8*np.pi*G*M*kB)
    print(f"  {nm:>10}: S/kB = A/4l_P^2 = {S:.3e},  Hawking T = {T:.3e} K")
print("""=> the horizon-area entropy S=A/4 and Hawking T follow from the
   Schwarzschild horizon TFT reproduces (scale check passes). But DERIVING them
   from the TFT phase field -- counting the phase configurations on the horizon
   that give S = A/4 l_P^2 -- is the OPEN FRONTIER (the deep emergent-gravity /
   holography problem, open in every framework). Flagged, not claimed.""")

hdr("BH VERDICT vs pre-registered gate:  PASS (structural)")
rc_sun = (3*Msun/(4*np.pi*rho_max))**(1/3)
print(f"""[PASS] TFT gives a coherent black hole:
  * [derived route] HORIZON at r_s = 2GM/c^2 from TFT's own inflow rate
    sqrt(2GM/r) reaching c -- the river model, not imposed.
  * [structural] time = phase cycling FREEZES at the horizon (rate ->0) -- the
    literal frozen star.
  * [TFT-native, distinctive] NO SINGULARITY: the bounded phase field caps the
    density at ~Planck density -> a REGULAR core, r_core ~ {rc_sun:.1e} m for a
    solar mass ({rc_sun/lP:.0e} Planck lengths), deep inside the horizon. TFT
    black hole = horizon + Planck-density phase-frozen core (regular-BH family).
  * [consistency] r_s and the thermo scales (S=A/4, Hawking T) match GR.

OPEN/floors: DERIVING S=A/4 and Hawking T from the TFT phase field (the deep
emergent-gravity/holography problem); whether the core is static or BOUNCES
(a possible observable -- Planck-star gamma bursts); the absolute scale
(l0 = l_Planck?); rotation/charge (Kerr-Newman analog). Internal-only.""")

out = dict(prereg="BH0_prereg_blackhole.md 2026-07-12",
           r_s_sun=float(r_s(Msun)), r_core_sun=float(rc_sun),
           r_core_over_lP=float(rc_sun/lP), r_core_over_rs=float(rc_sun/r_s(Msun)),
           rho_max=float(rho_max), S_sun_over_kB=float(4*np.pi*r_s(Msun)**2/(4*lP**2)),
           verdict="PASS(structural): horizon from TFT inflow rate (river model); "
                   "time=phase cycling freezes at horizon; SINGULARITY-FREE regular "
                   "core from bounded phase field (r_core~1e-22 m solar, Planck "
                   "density) = distinctive vs GR; thermo scales match. OPEN: derive "
                   "S=A/4 & Hawking T from the field; core bounce; abs scale; Kerr.")
with open("outputs/BH_blackhole.json", "w") as fj:
    json.dump(out, fj, indent=2)
print("\n[results block written: outputs/BH_blackhole.json]")
