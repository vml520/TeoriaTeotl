"""
teotl_math — branch-cut-safe S¹ primitives (numpy-only, no framework deps).

All phase arithmetic in the TFT cluster should route through these instead
of raw % (2*pi) so the branch-cut is handled uniformly.
"""
import numpy as np


def wrap_to_pi(x):
    """Wrap angle(s) to [−π, π). The boundary −π and +π are equivalent on S¹."""
    return ((np.asarray(x, dtype=float) + np.pi) % (2 * np.pi)) - np.pi


def wrap_theta(theta):
    """Wrap phase(s) to [0, 2π). Named alias for % 2π."""
    return np.asarray(theta, dtype=float) % (2 * np.pi)


def s1_gradient(theta):
    """
    Pairwise S¹-correct phase differences.

    Returns (N, N) array where out[i, j] = wrap_to_pi(theta[j] − theta[i]).
    Use this instead of bare (theta[None,:] − theta[:,None]) whenever the
    raw difference might straddle the branch cut.
    """
    theta = np.asarray(theta, dtype=float)
    return wrap_to_pi(theta[None, :] - theta[:, None])


def winding_density_2d(theta):
    """
    Plaquette winding numbers for a 2D phase field.

    theta : (H, W) array of phases (any range; wrapped internally).
    Returns (H−1, W−1) int array: +1 vortex, −1 antivortex, 0 smooth.

    Each plaquette sums four branch-cut-safe edge differences going
    clockwise: right → down → left → up.  Dividing by 2π and rounding
    gives the topological charge.
    """
    th = np.asarray(theta, dtype=float)
    d1 = wrap_to_pi(th[:-1, 1:]  - th[:-1, :-1])  # right along top
    d2 = wrap_to_pi(th[1:,  1:]  - th[:-1, 1:])   # down along right
    d3 = wrap_to_pi(th[1:,  :-1] - th[1:,  1:])   # left along bottom
    d4 = wrap_to_pi(th[:-1, :-1] - th[1:,  :-1])  # up along left
    return np.round((d1 + d2 + d3 + d4) / (2 * np.pi)).astype(int)


def angular_distance(a, b):
    """Shortest arc length between angles a and b on S¹ (always ≥ 0)."""
    return np.abs(wrap_to_pi(np.asarray(a, dtype=float) - np.asarray(b, dtype=float)))


def circular_mean(theta, weights=None):
    """
    Mean angle on S¹, optionally mass-weighted.

    theta   : array of phase values.
    weights : optional non-negative weights (need not sum to 1).
    Returns scalar in (−π, π].
    """
    theta = np.asarray(theta, dtype=float)
    e = np.exp(1j * theta)
    if weights is not None:
        e = np.asarray(weights, dtype=float) * e
    return float(np.angle(np.sum(e)))
