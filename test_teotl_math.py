"""
Unit tests for teotl_math primitives.

Checks:
  1. wrap_to_pi: boundary and sign correctness
  2. wrap_theta: [0, 2π) constraint
  3. s1_gradient: antisymmetry and branch-cut safety
  4. winding_density_2d: vortex → +1, antivortex → −1, smooth → 0
  5. Numerical identity: wrap_theta(x) == x % (2*pi) on a random batch
     (guarantees the refactored solvers produce bit-identical outputs)
"""
import numpy as np
from teotl_math import (
    wrap_to_pi, wrap_theta, s1_gradient, winding_density_2d,
    angular_distance, circular_mean,
)

PI = np.pi


def test_wrap_to_pi():
    # Range is [−π, π); ±π are the same point on S¹ so either sign is correct there
    cases = [
        (0.0,      0.0),
        (3*PI/2,  -PI/2),
        (-3*PI/2,  PI/2),
        (2*PI,     0.0),
        (-2*PI,    0.0),
    ]
    for x, expected in cases:
        got = float(wrap_to_pi(x))
        assert abs(got - expected) < 1e-12, f"wrap_to_pi({x:.4f}) = {got:.6f}, expected {expected:.6f}"
    # edge: ±π should produce the same value (same point on S¹)
    assert abs(wrap_to_pi(PI) - wrap_to_pi(-PI)) < 1e-12, "±π should map to same value"
    # vectorised: all outputs in [−π, π)
    xs = np.linspace(-3*PI, 3*PI, 500)
    ws = wrap_to_pi(xs)
    assert np.all(ws >= -PI - 1e-12) and np.all(ws < PI + 1e-12), "wrap_to_pi out of [−π,π)"
    print("  wrap_to_pi          PASS")


def test_wrap_theta():
    cases = [
        (0.0,    0.0),
        (2*PI,   0.0),
        (-0.1,   2*PI - 0.1),
        (3*PI,   PI),
    ]
    for x, expected in cases:
        got = float(wrap_theta(x))
        assert abs(got - expected) < 1e-12, f"wrap_theta({x:.4f}) = {got:.6f}, expected {expected:.6f}"
    xs = np.linspace(-3*PI, 3*PI, 500)
    ws = wrap_theta(xs)
    assert np.all(ws >= 0) and np.all(ws < 2*PI + 1e-12), "wrap_theta out of [0,2π)"
    print("  wrap_theta          PASS")


def test_s1_gradient():
    rng = np.random.default_rng(7)
    theta = rng.uniform(0, 2*PI, 20)
    G = s1_gradient(theta)
    assert G.shape == (20, 20), "wrong shape"
    # antisymmetry
    assert np.allclose(G, -G.T, atol=1e-12), "not antisymmetric"
    # diagonal zero
    assert np.allclose(np.diag(G), 0.0, atol=1e-12), "diagonal non-zero"
    # all values in (−π, π]
    assert np.all(G > -PI - 1e-12) and np.all(G <= PI + 1e-12), "values outside (−π,π]"
    print("  s1_gradient         PASS")


def test_winding_density_2d():
    # Vortex: phases wind +2π counterclockwise → plaquette winding = +1
    theta_vortex = np.array([
        [0.0,        PI/2],
        [3*PI/2,     PI],
    ])
    w = winding_density_2d(theta_vortex)
    assert w.shape == (1, 1), f"unexpected shape {w.shape}"
    assert w[0, 0] == 1, f"vortex gave {w[0,0]}, expected +1"

    # Antivortex: phases wind −2π → plaquette winding = −1
    theta_anti = np.array([
        [0.0,        3*PI/2],
        [PI/2,       PI],
    ])
    w = winding_density_2d(theta_anti)
    assert w[0, 0] == -1, f"antivortex gave {w[0,0]}, expected −1"

    # Smooth: tiny variation → winding = 0 everywhere
    rng = np.random.default_rng(3)
    theta_smooth = rng.uniform(0, 0.05, (8, 8))
    w = winding_density_2d(theta_smooth)
    assert np.all(w == 0), f"smooth field has non-zero winding: {w}"

    print("  winding_density_2d  PASS")


def test_numerical_identity():
    """wrap_theta must be bit-identical to % (2*pi) — guarantees solver outputs unchanged."""
    rng = np.random.default_rng(99)
    xs = rng.uniform(-10, 10, 10000)
    ref = xs % (2 * np.pi)
    got = wrap_theta(xs)
    assert np.array_equal(ref, got), "wrap_theta diverges from % (2*pi)"
    print("  numerical identity  PASS")


def test_angular_distance():
    assert abs(angular_distance(0.0, PI) - PI) < 1e-12
    assert abs(angular_distance(0.1, 0.1)) < 1e-12
    assert abs(angular_distance(0.0, -0.5) - 0.5) < 1e-12
    print("  angular_distance    PASS")


def test_circular_mean():
    # Uniform distribution on S¹ → mean undefined / magnitude ≈ 0; just check no crash
    theta = np.linspace(0, 2*PI, 100, endpoint=False)
    m = circular_mean(theta)
    assert isinstance(m, float)
    # Two identical phases → mean equals that phase
    m2 = circular_mean([0.7, 0.7])
    assert abs(m2 - 0.7) < 1e-10
    print("  circular_mean       PASS")


if __name__ == "__main__":
    print("teotl_math unit tests\n")
    test_wrap_to_pi()
    test_wrap_theta()
    test_s1_gradient()
    test_winding_density_2d()
    test_numerical_identity()
    test_angular_distance()
    test_circular_mean()
    print("\nAll tests passed.")
