"""The consistency test: does ONE field configuration fit BOTH the galactic a0 AND DESI's dark energy?

a0 FIXES the field mass. From a0 = c*(Compton frequency) = c*(m c^2/h):
    omega0 = 2*pi*a0/c = 2.5e-18 /s ,  H0 = 2.27e-18 /s  ->  m ~ 1.1 * Hubble mass.
So galaxies pin m/H0 ~ 1.1. The only free dial left is the field's starting angle theta_i.
(Omega_phi ~ 0.7 is a standard calibration that fixes V0 given theta_i.)

Scan theta_i. For each, integrate the FRW field and read off (w0, w_a, Omega_phi).
Question: is there a theta_i giving DESI (w0 ~ -0.83, w_a ~ -0.75) with Omega_phi ~ 0.7?
If yes -> one field does galaxies AND DESI (strong). If the locus misses DESI -> honest tension.
"""
import numpy as np

Om0 = 0.3
mH0 = 1.10                    # fixed by the galactic a0

def integrate(theta_i, steps=8000):
    V0 = 3*(1-Om0)/(1-np.cos(theta_i))
    f  = np.sqrt(V0)/mH0
    rho_m0 = 3*Om0
    def derivs(N, phi, u):
        V  = V0*(1-np.cos(phi/f)); Vp = (V0/f)*np.sin(phi/f)
        rm = rho_m0*np.exp(-3*N)
        H2 = (rm+V)/(3-0.5*u**2)
        Hd = -0.5*(rm+H2*u**2)/H2
        return u, -(3+Hd)*u - Vp/H2, H2, V
    N0,N1 = -7.0,0.0; dN=(N1-N0)/steps
    phi,u,N = f*theta_i,0.0,N0
    as_,ws=[],[]
    for i in range(steps+1):
        _,_,H2,V = derivs(N,phi,u); pd2=H2*u**2
        ws.append((0.5*pd2-V)/(0.5*pd2+V)); as_.append(np.exp(N))
        k1p,k1u,_,_=derivs(N,phi,u)
        k2p,k2u,_,_=derivs(N+dN/2,phi+dN/2*k1p,u+dN/2*k1u)
        k3p,k3u,_,_=derivs(N+dN/2,phi+dN/2*k2p,u+dN/2*k2u)
        k4p,k4u,_,_=derivs(N+dN,phi+dN*k3p,u+dN*k3u)
        phi+=dN/6*(k1p+2*k2p+2*k3p+k4p); u+=dN/6*(k1u+2*k2u+2*k3u+k4u); N+=dN
    as_,ws=np.array(as_),np.array(ws)
    m=as_>0.3; A=np.vstack([np.ones(m.sum()),(1-as_[m])]).T
    w0,wa=np.linalg.lstsq(A,ws[m],rcond=None)[0]
    _,_,H2f,Vf=derivs(0.0,phi,u); Omp=(0.5*H2f*u**2+Vf)/(3*H2f)
    return w0,wa,Omp

print(f"  field mass fixed by galactic a0:  m ~ {mH0} * Hubble mass\n")
print("  " + "{:>8s} {:>8s} {:>8s} {:>9s}".format("theta_i","w0","w_a","Omega_phi"))
for th in [0.4,0.7,1.0,1.4,1.8,2.2,2.6]:
    w0,wa,Omp = integrate(th)
    print("  " + "{:>8.2f} {:>8.3f} {:>8.3f} {:>9.2f}".format(th,w0,wa,Omp))

print("\n  DESI 2024 (DESI+CMB+Pantheon+):  w0 ~ -0.83,  w_a ~ -0.75  (+/- ~0.3 on w_a)")
print("  a0 (galaxies) already fixed m ~ 1.1 H0. Read the locus above:")
print("  - if a theta_i hits w0~-0.83 AND w_a~-0.75 at Omega_phi~0.7  -> ONE field does both (strong).")
print("  - if w_a stays too mild across all theta_i                    -> honest tension to report.")
