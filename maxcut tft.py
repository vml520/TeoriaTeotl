"""
TFT Phase-Native Optimization — MAX-CUT benchmark
─────────────────────────────────────────────────
Claim under test: the field's dissipative settling dynamics (Kuramoto sin
coupling + annealed phase pinning, the Λ_eff-nucleation analogue) solve
MAX-CUT competitively with simulated annealing.

Mapping: vertex i → phase θ_i on S¹; edge weight w_ij → ANTI-aligning
coupling. Dynamics:  dθ_i/dt = −Σ_j w_ij sin(θ_i−θ_j) − K_s(t)·sin(2θ_i) + ξ(t)
K_s ramps 0→K_max (phase freezing; the solver analogue of Λ_eff nucleation),
noise anneals to 0. Readout: s_i = sign(cos θ_i); 1-opt polish.

Honest notes: couplings are problem-defined (not row-normalized); the
binarizing pinning term is a second harmonic — a solver-specific variant
outside the AGI's odd-k invariant, stated rather than hidden.
"""
import numpy as np, time

rng = np.random.default_rng(0)

# ── instances ────────────────────────────────────────────────────────────────
def planted_bipartite(n=300, p=0.1, seed=1):
    r = np.random.default_rng(seed)
    half = n//2
    W = np.zeros((n,n))
    for i in range(half):
        for j in range(half, n):
            if r.random() < p: W[i,j]=W[j,i]=1.0
    return W, W.sum()/2  # optimum cuts ALL edges

def complete_graph(n=60):
    W = np.ones((n,n)) - np.eye(n)
    return W, n*n//4   # known optimum floor(n^2/4)

def erdos_renyi(n=400, p=0.05, seed=2):
    r = np.random.default_rng(seed)
    A = (r.random((n,n)) < p).astype(float)
    W = np.triu(A,1); W = W + W.T
    return W, None

def k_regular(n=400, k=3, seed=3):
    r = np.random.default_rng(seed)
    # configuration-model-ish: random perfect matchings
    W = np.zeros((n,n))
    for _ in range(k):
        perm = r.permutation(n)
        for a in range(0, n-1, 2):
            i,j = perm[a], perm[a+1]
            if i!=j: W[i,j]=W[j,i]=1.0
    return W, None

def cut_value(W, s):
    return (W.sum() - s @ W @ s) / 4.0

def polish_1opt(W, s):
    h = W @ s
    improved = True
    while improved:
        improved = False
        gains = s * h            # flipping i changes cut by +s_i h_i
        i = np.argmax(gains)
        if gains[i] > 1e-9:
            s[i] = -s[i]
            h += 2*s[i]*W[:,i]
            improved = True
    return s

# ── TFT field solver ─────────────────────────────────────────────────────────
def tft_solve(W, steps=1500, restarts=12, dt=0.08, Ks_max=None, seed=0):
    n = W.shape[0]
    r = np.random.default_rng(seed)
    deg = W.sum(1).mean()
    Ks_max = Ks_max or 1.2*deg
    th = r.uniform(0, 2*np.pi, (restarts, n))
    t0 = time.time()
    for step in range(steps):
        frac  = step/steps
        Ks    = Ks_max * frac                    # phase-freezing ramp (Λ_eff analogue)
        sig   = 0.8*deg*(1-frac)**2              # annealed noise
        C, S  = np.cos(th), np.sin(th)
        WC, WS= C @ W.T, S @ W.T                 # (R,n)
        coup  = -(S*WC - C*WS)                   # −Σ w_ij sin(θi−θj)
        pin   = -Ks*np.sin(2*th)
        th    = (th + dt*(coup + pin) + np.sqrt(dt)*sig*r.normal(0,1,th.shape)) % (2*np.pi)
    best, bs = -np.inf, None
    for k in range(restarts):
        s = np.where(np.cos(th[k])>=0, 1.0, -1.0)
        s = polish_1opt(W, s)
        c = cut_value(W, s)
        if c > best: best, bs = c, s
    return best, time.time()-t0

# ── simulated annealing baseline ─────────────────────────────────────────────
def sa_solve(W, sweeps=400, restarts=6, T0=None, seed=0):
    n = W.shape[0]
    r = np.random.default_rng(seed)
    deg = W.sum(1).mean()
    T0 = T0 or 1.5*deg
    Tf = 0.01
    best = -np.inf
    t0 = time.time()
    for rs in range(restarts):
        s = r.choice([-1.0,1.0], n)
        h = W @ s
        for sw in range(sweeps):
            T = T0*(Tf/T0)**(sw/sweeps)
            order = r.permutation(n)
            u = r.random(n)
            for idx, i in enumerate(order):
                dC = s[i]*h[i]                    # cut gain from flipping i
                if dC > 0 or u[idx] < np.exp(dC/max(T,1e-12)):
                    s[i] = -s[i]
                    h += 2*s[i]*W[:,i]
        s = polish_1opt(W, s)
        c = cut_value(W, s)
        if c > best: best = c
    return best, time.time()-t0

# ── run benchmark ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("TFT Phase-Native Optimization — MAX-CUT benchmark\n")
    instances = [
        ("planted bipartite n=300 (optimum known)", *planted_bipartite()),
        ("complete K60 (optimum 900)",             *complete_graph()),
        ("Erdős–Rényi n=400 p=0.05",               *erdos_renyi()),
        ("random 3-regular n=400",                 *k_regular()),
    ]
    print(f"{'instance':42} {'TFT cut':>9} {'SA cut':>9} {'opt':>7}  {'TFT s':>6} {'SA s':>6}")
    results = []
    for name, W, opt in instances:
        c_t, t_t = tft_solve(W)
        c_s, t_s = sa_solve(W)
        opt_s = f"{int(opt)}" if opt else "  ?"
        print(f"{name:42} {c_t:9.0f} {c_s:9.0f} {opt_s:>7}  {t_t:6.1f} {t_s:6.1f}")
        results.append((name, c_t, c_s, opt))
    np.save("maxcut_results.npy", np.array([(r[1], r[2]) for r in results]))
