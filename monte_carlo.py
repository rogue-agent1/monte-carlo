#!/usr/bin/env python3
"""Monte Carlo - Estimate pi, integrals, and run probabilistic simulations."""
import sys, random, math

def estimate_pi(n=1000000, seed=42):
    random.seed(seed); inside = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1: inside += 1
    return 4 * inside / n

def integrate(f, a, b, n=100000, seed=42):
    random.seed(seed)
    total = sum(f(random.uniform(a, b)) for _ in range(n))
    return (b - a) * total / n

def birthday_paradox(people=23, trials=100000, seed=42):
    random.seed(seed); matches = 0
    for _ in range(trials):
        bdays = set()
        for _ in range(people):
            b = random.randint(1, 365)
            if b in bdays: matches += 1; break
            bdays.add(b)
    return matches / trials

def buffon_needle(n=100000, seed=42):
    random.seed(seed); crosses = 0
    for _ in range(n):
        y = random.random(); theta = random.uniform(0, math.pi)
        if y <= 0.5 * math.sin(theta): crosses += 1
    return 2 * n / crosses if crosses else 0

def main():
    print("=== Monte Carlo Simulations ===\n")
    for n in [1000, 10000, 100000, 1000000]:
        pi = estimate_pi(n)
        err = abs(pi - math.pi)
        print(f"  π estimate (n={n:>8d}): {pi:.6f}  error={err:.6f}")
    area = integrate(lambda x: x**2, 0, 1, 100000)
    print(f"\n  ∫x² dx [0,1] = {area:.6f} (exact: 0.333333)")
    area2 = integrate(lambda x: math.sin(x), 0, math.pi, 100000)
    print(f"  ∫sin(x) dx [0,π] = {area2:.6f} (exact: 2.000000)")
    prob = birthday_paradox(23)
    print(f"\n  Birthday paradox (23 people): {prob:.4f} (exact: ~0.5073)")
    pi_buffon = buffon_needle()
    print(f"  Buffon's needle π: {pi_buffon:.6f}")

if __name__ == "__main__":
    main()
