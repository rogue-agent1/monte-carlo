#!/usr/bin/env python3
"""Monte Carlo simulation toolkit — pi estimation, integration, random walk."""
import sys, random, math

def estimate_pi(n=10000):
    inside = sum(1 for _ in range(n) if random.random()**2 + random.random()**2 <= 1)
    return 4 * inside / n

def mc_integrate(f, a, b, n=10000):
    total = sum(f(random.uniform(a, b)) for _ in range(n))
    return (b - a) * total / n

def random_walk_2d(steps):
    x = y = 0
    path = [(x, y)]
    for _ in range(steps):
        dx, dy = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
        x += dx; y += dy
        path.append((x, y))
    return path

def bootstrap_mean(data, n_samples=1000):
    means = []
    for _ in range(n_samples):
        sample = [random.choice(data) for _ in range(len(data))]
        means.append(sum(sample) / len(sample))
    means.sort()
    return sum(means)/len(means), means[int(0.025*n_samples)], means[int(0.975*n_samples)]

def test():
    random.seed(42)
    pi = estimate_pi(100000)
    assert abs(pi - math.pi) < 0.05
    area = mc_integrate(lambda x: x**2, 0, 1, 100000)
    assert abs(area - 1/3) < 0.02
    path = random_walk_2d(100)
    assert len(path) == 101
    mean, lo, hi = bootstrap_mean([1,2,3,4,5,6,7,8,9,10])
    assert 4 < mean < 7
    assert lo < hi
    print("  monte_carlo: ALL TESTS PASSED")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test": test()
    else: print(f"Pi estimate: {estimate_pi():.4f}")
