"""
winding_solver.py — Anti-ferromagnetic MAX-CUT + winding-number diagnostic
────────────────────────────────────────────────────────────────────────────
The Kuramoto solver in maxcut_tft.py uses ferromagnetic coupling, which
ALIGNS phases — the wrong direction for MAX-CUT. This solver flips the sign:

  Kuramoto:  dθ_i = −Σ_j W_ij sin(θ_i−θ_j)   [aligns, ferromagnetic]
  Winding:   dθ_i = +Σ_j W_ij sin(θ_i−θ_j)   [anti-aligns, correct for MAX-CUT]

Both add the same binarizing pinning term −K·sin(2θ_i) and annealed noise.
The coupling flip makes gradient descent on the correct energy landscape:

  E = +Σ_{i<j} W_ij cos(θ_i−θ_j)        [minimized when phases anti-align → cut]
  E += −K/2 · Σ_i cos(2θ_i)              [minimized at θ ∈ {0,π}]

Winding diagnostic:
  Vertices embedded via spectral layout (Fiedler eigenvectors of Laplacian).
  At the midpoint of annealing (before pinning collapses phases to {0,π}),
  the phase field still has continuous texture. Plaquette winding on the 2D
  grid shows domain structure:

    vortex count low  → clean domain wall between partitions (bipartite-like)
    vortex count high → frustrated cycles resist settlement; defects persist

  This is a topological indicator of solution difficulty, not just cut value.

Honest labels:
  DERIVED  — anti-FM coupling aligns with the TFT force-sign result (§3):
             like-winding repels → opposite winding attracts → anti-FM order.
  DELIVERED — cut values; 1-opt polish identical to Kuramoto solver.
  NEW      — spectral layout + midpoint winding as per-instance difficulty metric.
"""
import numpy as np, time
from teotl_math import wrap_theta, winding_density_2d, circular_mean

# ── graph generators (same instances as maxcut_tft.py) ───────────────────────

def planted_bipartite(n=300, p=0.1, seed=1):
    r = np.random.default_rng(seed)
    half = n // 2
    W = np.zeros((n, n))
    for i in range(half):
        for j in range(half, n):
            if r.random() < p:
                W[i, j] = W[j, i] = 1.0
    return W, int(W.sum() / 2)

def complete_graph(n=60):
    return np.ones((n, n)) - np.eye(n), n * n // 4

def erdos_renyi(n=400, p=0.05, seed=2):
    r = np.random.default_rng(seed)
    A = (r.random((n, n)) < p).astype(float)
    W = np.triu(A, 1); W = W + W.T
    return W, None

def k_regular(n=400, k=3, seed=3):
    r = np.random.default_rng(seed)
    W = np.zeros((n, n))
    for _ in range(k):
        perm = r.permutation(n)
        for a in range(0, n - 1, 2):
            i, j = perm[a], perm[a + 1]
            if i != j:
                W[i, j] = W[j, i] = 1.0
    return W, None

def cut_value(W, s):
    return (W.sum() - s @ W @ s) / 4.0

def polish_1opt(W, s):
    s = s.copy(); h = W @ s
    improved = True
    while improved:
        improved = False
        gains = s * h
        i = np.argmax(gains)
        if gains[i] > 1e-9:
            s[i] = -s[i]; h += 2 * s[i] * W[:, i]
            improved = True
    return s


def round_and_polish(W, theta, n_angles=16):
    """
    Random-hyperplane rounding sweep (Goemans–Williamson style).

    A single fixed threshold s_i = sign(cos θ_i) throws away most of the phase
    information. Instead sweep the cut-plane angle φ over [0, π) (φ and φ+π give
    the same partition), round s_i = sign(cos(θ_i − φ)) at each, 1-opt polish,
    and keep the best cut. n_angles=1 reproduces the old single-threshold
    rounding exactly, so this can never do worse.
    """
    best_c, best_s = -np.inf, None
    for phi in np.linspace(0.0, np.pi, n_angles, endpoint=False):
        s = np.where(np.cos(theta - phi) >= 0, 1.0, -1.0)
        s = polish_1opt(W, s)
        c = cut_value(W, s)
        if c > best_c:
            best_c, best_s = c, s
    return best_c, best_s

# ── spectral layout ───────────────────────────────────────────────────────────

def spectral_layout(W):
    """
    Embed graph vertices in 2D using the two Fiedler eigenvectors of the
    graph Laplacian. Positions in [−1, 1]². Bipartite graphs get clean
    two-cluster layout; frustrated graphs get more interleaved structure.
    """
    L = np.diag(W.sum(1)) - W
    _, vecs = np.linalg.eigh(L)
    pos = vecs[:, 1:3].copy()                          # 2nd and 3rd eigenvecs
    scale = np.abs(pos).max(axis=0, keepdims=True) + 1e-9
    return pos / scale

# ── winding diagnostic ────────────────────────────────────────────────────────

def winding_count(theta, pos, grid_n=16):
    """
    Project phase field onto a grid_n×grid_n grid and return Σ|W_p|
    (total vortex count). Meaningful when phases are not yet fully at {0,π}.
    """
    xs, ys = pos[:, 0], pos[:, 1]
    x_lo, x_hi = xs.min() - 0.05, xs.max() + 0.05
    y_lo, y_hi = ys.min() - 0.05, ys.max() + 0.05
    gx = np.clip(((xs - x_lo) / (x_hi - x_lo) * grid_n).astype(int), 0, grid_n - 1)
    gy = np.clip(((ys - y_lo) / (y_hi - y_lo) * grid_n).astype(int), 0, grid_n - 1)
    grid = np.full((grid_n, grid_n), np.nan)
    for row in range(grid_n):
        for col in range(grid_n):
            mask = (gx == col) & (gy == row)
            if mask.any():
                grid[row, col] = wrap_theta(circular_mean(theta[mask]))
    fill = wrap_theta(circular_mean(theta))
    grid = np.where(np.isnan(grid), fill, grid)
    return int(np.abs(winding_density_2d(grid)).sum())

# ── anti-ferromagnetic solver ─────────────────────────────────────────────────

def winding_solve(W, steps=1500, restarts=12, dt=0.08,
                  K_max=None, seed=0, grid_n=16, n_angles=16):
    """
    Anti-FM MAX-CUT solver. Coupling: +Σ W_ij sin(θ_i−θ_j) drives phases apart.

    schedule (same as Kuramoto): K = K_max·(t/T), noise ∝ (1−t/T)²
    Winding readout at step steps//2 (mid-anneal, before full binarization).

    Returns: (best_cut, vortex_count_at_midpoint, elapsed_seconds)
    """
    n = W.shape[0]
    r = np.random.default_rng(seed)
    deg = W.sum(1).mean()
    K_max = K_max or 1.2 * deg
    pos = spectral_layout(W)

    th = r.uniform(0, 2 * np.pi, (restarts, n))
    mid_v = 0
    t0 = time.time()

    for step in range(steps):
        frac = step / steps
        sig  = 0.8 * deg * (1 - frac) ** 2
        K    = K_max * frac
        C, S = np.cos(th), np.sin(th)
        WC   = C @ W; WS = S @ W        # W symmetric → W = W.T
        coup = S * WC - C * WS          # +Σ W_ij sin(θ_i−θ_j) [anti-FM]
        pin  = -K * np.sin(2 * th)
        th   = wrap_theta(th + dt * (coup + pin)
                          + np.sqrt(dt) * sig * r.normal(0, 1, th.shape))
        if step == steps // 2:
            mid_v = winding_count(th[0], pos, grid_n=grid_n)

    best_cut = -np.inf
    for k in range(restarts):
        c, _ = round_and_polish(W, th[k], n_angles=n_angles)
        if c > best_cut:
            best_cut = c
    return best_cut, mid_v, time.time() - t0

# ── Kuramoto baseline (FM, for comparison) ────────────────────────────────────

def kuramoto_solve(W, steps=1500, restarts=12, dt=0.08, K_max=None, seed=0, n_angles=16):
    """Kuramoto (FM coupling, −Σ W_ij sin(θ_i−θ_j)). Same schedule as winding_solve."""
    n = W.shape[0]
    r = np.random.default_rng(seed)
    deg = W.sum(1).mean()
    K_max = K_max or 1.2 * deg
    th = r.uniform(0, 2 * np.pi, (restarts, n))
    t0 = time.time()
    for step in range(steps):
        frac = step / steps
        sig  = 0.8 * deg * (1 - frac) ** 2
        K    = K_max * frac
        C, S = np.cos(th), np.sin(th)
        WC   = C @ W; WS = S @ W
        coup = -(S * WC - C * WS)       # −Σ W_ij sin(θ_i−θ_j) [FM]
        pin  = -K * np.sin(2 * th)
        th   = wrap_theta(th + dt * (coup + pin)
                          + np.sqrt(dt) * sig * r.normal(0, 1, th.shape))
    best = -np.inf
    for k in range(restarts):
        c, _ = round_and_polish(W, th[k], n_angles=n_angles)
        if c > best: best = c
    return best, time.time() - t0

# ── benchmark ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Winding-Number Solver — anti-FM MAX-CUT benchmark\n")
    print("Coupling: +Σ sin(θ_i−θ_j) [anti-FM / winding]  vs")
    print("          −Σ sin(θ_i−θ_j) [FM / Kuramoto]\n")

    instances = [
        ("planted bipartite n=300", *planted_bipartite()),
        ("complete K60",            *complete_graph()),
        ("Erdős–Rényi n=400 p=0.05", *erdos_renyi()),
        ("random 3-regular n=400",  *k_regular()),
    ]

    hdr = (f"{'instance':28} {'anti-FM':>8} {'Kuramoto':>9} {'opt':>6}  "
           f"{'vortex@½T':>9}  {'win':>4}  time(s)")
    print(hdr)
    print("─" * len(hdr))

    w_wins = k_wins = ties = 0
    for name, W_g, opt in instances:
        c_w, v_mid, t_w = winding_solve(W_g)
        c_k, t_k        = kuramoto_solve(W_g)
        opt_s = f"{int(opt)}" if opt else "?"
        if   c_w > c_k + 0.5: win = "W"; w_wins += 1
        elif c_k > c_w + 0.5: win = "K"; k_wins += 1
        else:                  win = "tie"; ties += 1
        print(f"{name:28} {c_w:8.0f} {c_k:9.0f} {opt_s:>6}  "
              f"{v_mid:>9d}  {win:>4}  {t_w:.1f}/{t_k:.1f}")

    print(f"\nanti-FM wins {w_wins}, Kuramoto wins {k_wins}, ties {ties} "
          f"(of {len(instances)})")
    print()
    print("vortex@½T: winding count on spectral layout at mid-anneal.")
    print("  Low  → domain wall forming cleanly  (bipartite-like instance)")
    print("  High → frustrated cycles resist settlement (harder instance)")
