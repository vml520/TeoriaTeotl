"""Dynamical dark energy from the TFT ultralight field (developing the prediction like a0).

Dark energy = the same ultralight phase field whose mass gap gives a0. Its potential is axion-like,
V(phi) = V0 (1 - cos(phi/f)), with mass m ~ H0 (the TFT 'mass = Hubble mass' condition). A field with
m ~ H0 is frozen by Hubble friction at high z (w = -1) and THAWS -- begins rolling -- only now, when H
has dropped to ~ m. Thawing quintessence => w = -1 in the past, w > -1 today, w_a < 0.

We integrate the field in an FRW universe (matter + field), no fitting to DESI, and read off
w(z), then w0 and w_a (CPL: w(a) = w0 + w_a (1-a)). Compare to DESI 2024.

Units: reduced Planck M_p = 1, H0 = 1.  Omega_m0 = 0.3, Omega_phi0 ~ 0.7.
Free inputs (the SAME initial conditions that set a0): m/H0 (~1) and theta_i = phi_i/f (~O(1)).
"""
import numpy as np

Om0 = 0.3
rho_m0 = 3*Om0                     # 3 H0^2 Omega_m0, with H0=1
mH0 = 1.0                          # field mass in units of H0 (TFT: mass ~ Hubble mass)
theta_i = 1.0                      # initial field angle (an initial condition; ~ the a0 IC)

V0 = 3*(1-Om0)/(1-np.cos(theta_i)) # set so V(theta_i) ~ dark-energy density today
f  = np.sqrt(V0)/mH0               # decay constant from m^2 = V0/f^2
phi_i = f*theta_i

def derivs(N, phi, u):
    V   = V0*(1-np.cos(phi/f))
    Vp  = (V0/f)*np.sin(phi/f)
    rho_m = rho_m0*np.exp(-3*N)
    H2  = (rho_m + V)/(3 - 0.5*u**2)
    HdotoverH2 = -0.5*(rho_m + H2*u**2)/H2
    return u, -(3 + HdotoverH2)*u - Vp/H2, H2, V

# integrate N = ln a from -7 (z~1100) to 0 (today), RK4
N0, N1, steps = -7.0, 0.0, 40000
dN = (N1-N0)/steps
phi, u, N = phi_i, 0.0, N0
Ns, ws, as_ = [], [], []
for i in range(steps+1):
    dphi, du, H2, V = derivs(N, phi, u)
    phidot2 = H2*u**2
    rho_phi = 0.5*phidot2 + V
    p_phi   = 0.5*phidot2 - V
    w = p_phi/rho_phi
    Ns.append(N); ws.append(w); as_.append(np.exp(N))
    # RK4 step
    k1p,k1u,_,_ = derivs(N, phi, u)
    k2p,k2u,_,_ = derivs(N+dN/2, phi+dN/2*k1p, u+dN/2*k1u)
    k3p,k3u,_,_ = derivs(N+dN/2, phi+dN/2*k2p, u+dN/2*k2u)
    k4p,k4u,_,_ = derivs(N+dN, phi+dN*k3p, u+dN*k3u)
    phi += dN/6*(k1p+2*k2p+2*k3p+k4p)
    u   += dN/6*(k1u+2*k2u+2*k3u+k4u)
    N   += dN

as_, ws = np.array(as_), np.array(ws)
w0 = ws[-1]
# CPL fit w(a) = w0 + w_a (1-a) over the dark-energy era (a > 0.3)
mask = as_ > 0.3
A = np.vstack([np.ones(mask.sum()), (1-as_[mask])]).T
coef = np.linalg.lstsq(A, ws[mask], rcond=None)[0]
w0_fit, wa_fit = coef

# final Omega_phi
_,_,H2f,Vf = derivs(0.0, phi, u)
rho_phi_f = 0.5*H2f*u**2 + Vf
Om_phi = rho_phi_f/(3*H2f)

print("  TFT ultralight field as dark energy (m ~ H0, thawing):")
print(f"    Omega_phi today = {Om_phi:.2f}  (target ~0.7)\n")
print("  equation of state w(z):")
for z in [3.0, 1.0, 0.5, 0.0]:
    a = 1/(1+z); i = np.argmin(np.abs(as_-a))
    print(f"    z={z:>4.1f} (a={a:.2f}):  w = {ws[i]:+.3f}")
print(f"\n  today:  w0 = {w0_fit:+.3f}   w_a = {wa_fit:+.3f}")
print(f"  DESI 2024 (DESI+CMB+SNe):  w0 ~ -0.8,  w_a ~ -0.8  (thawing: w0>-1, w_a<0)")
print("\n  => predicts THAWING quintessence: w=-1 in the past, rising above -1 now, w_a<0.")
print("     Same field, same initial condition that sets a0 => a0 and (w0,w_a) are LINKED,")
print("     not independent. That is the distinctive, falsifiable TFT statement.")
