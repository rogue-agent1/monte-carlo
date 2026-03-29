#!/usr/bin/env python3
"""monte_carlo - Monte Carlo methods (pi estimation, integration, simulation)."""
import sys, math, random

def estimate_pi(n=100000, seed=None):
    if seed is not None:
        random.seed(seed)
    inside = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1:
            inside += 1
    return 4 * inside / n

def integrate(f, a, b, n=100000, seed=None):
    if seed is not None:
        random.seed(seed)
    total = 0.0
    for _ in range(n):
        x = a + random.random() * (b - a)
        total += f(x)
    return (b - a) * total / n

def bootstrap_mean(data, n_bootstrap=1000, seed=None):
    if seed is not None:
        random.seed(seed)
    means = []
    n = len(data)
    for _ in range(n_bootstrap):
        sample = [data[random.randint(0, n-1)] for _ in range(n)]
        means.append(sum(sample) / n)
    means.sort()
    ci_low = means[int(0.025 * n_bootstrap)]
    ci_high = means[int(0.975 * n_bootstrap)]
    return sum(means) / len(means), ci_low, ci_high

def random_walk(steps, seed=None):
    if seed is not None:
        random.seed(seed)
    x, y = 0, 0
    path = [(x, y)]
    for _ in range(steps):
        dx, dy = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
        x += dx
        y += dy
        path.append((x, y))
    return path

def test():
    pi = estimate_pi(100000, seed=42)
    assert abs(pi - math.pi) < 0.05
    # integrate x^2 from 0 to 1 = 1/3
    integral = integrate(lambda x: x**2, 0, 1, 100000, seed=42)
    assert abs(integral - 1/3) < 0.01
    # bootstrap
    data = [10, 12, 14, 11, 13, 15, 9, 11, 12, 14]
    mean, lo, hi = bootstrap_mean(data, 1000, seed=42)
    assert 10 < mean < 14
    assert lo < mean < hi
    # random walk
    path = random_walk(100, seed=42)
    assert len(path) == 101
    assert path[0] == (0, 0)
    print("OK: monte_carlo")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        print("Usage: monte_carlo.py test")
