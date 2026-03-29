#!/usr/bin/env python3
"""monte_carlo - Monte Carlo methods: pi estimation, integration, option pricing."""
import sys, json, math, random

def estimate_pi(n=100000, seed=42):
    rng = random.Random(seed); inside = 0
    for _ in range(n):
        x, y = rng.random(), rng.random()
        if x*x + y*y <= 1: inside += 1
    return 4 * inside / n

def mc_integrate(f, a, b, n=100000, seed=42):
    rng = random.Random(seed)
    total = sum(f(rng.uniform(a, b)) for _ in range(n))
    return (b - a) * total / n

def buffon_needle(n=100000, L=1, D=2, seed=42):
    rng = random.Random(seed); crosses = 0
    for _ in range(n):
        y = rng.uniform(0, D/2)
        theta = rng.uniform(0, math.pi)
        if y <= L/2 * math.sin(theta): crosses += 1
    return 2*L*n / (crosses*D) if crosses else float('inf')

def black_scholes_mc(S, K, T, r, sigma, n=100000, seed=42):
    rng = random.Random(seed); payoffs = []
    for _ in range(n):
        z = sum(rng.gauss(0,1) for _ in range(12)) - 6  # approx normal
        ST = S * math.exp((r - 0.5*sigma**2)*T + sigma*math.sqrt(T)*z)
        payoffs.append(max(ST - K, 0))
    return math.exp(-r*T) * sum(payoffs) / n

def main():
    print("Monte Carlo methods demo\n")
    for n in [1000, 10000, 100000, 1000000]:
        pi = estimate_pi(n)
        err = abs(pi - math.pi)
        print(f"  π estimate (n={n:>7d}): {pi:.6f} (error={err:.6f})")
    # Integration
    integral = mc_integrate(lambda x: math.sin(x), 0, math.pi, 100000)
    print(f"\n  ∫sin(x) [0,π] = {integral:.6f} (exact=2.0)")
    # Buffon's needle
    pi_buffon = buffon_needle(500000)
    print(f"  Buffon's π = {pi_buffon:.4f}")
    # Option pricing
    price = black_scholes_mc(S=100, K=105, T=1, r=0.05, sigma=0.2)
    print(f"\n  Call option price: ${price:.2f}")

if __name__ == "__main__":
    main()
