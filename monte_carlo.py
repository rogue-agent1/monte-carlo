#!/usr/bin/env python3
"""Monte Carlo simulations. Zero dependencies."""
import random, math

def estimate_pi(n=10000, seed=42):
    random.seed(seed)
    inside = sum(1 for _ in range(n) if random.random()**2+random.random()**2 <= 1)
    return 4 * inside / n

def monte_carlo_integrate(fn, a, b, n=10000, seed=42):
    random.seed(seed)
    total = sum(fn(random.uniform(a, b)) for _ in range(n))
    return (b - a) * total / n

def bootstrap(data, stat_fn, n_resamples=1000, seed=42):
    random.seed(seed)
    stats = []
    for _ in range(n_resamples):
        sample = [random.choice(data) for _ in range(len(data))]
        stats.append(stat_fn(sample))
    stats.sort()
    mean = sum(stats) / len(stats)
    ci_low = stats[int(0.025 * len(stats))]
    ci_high = stats[int(0.975 * len(stats))]
    return {"mean": mean, "ci_low": ci_low, "ci_high": ci_high, "std": _std(stats)}

def _std(data):
    m = sum(data)/len(data)
    return math.sqrt(sum((x-m)**2 for x in data)/len(data))

def random_walk(steps=100, seed=42):
    random.seed(seed)
    pos = 0; path = [0]
    for _ in range(steps):
        pos += random.choice([-1, 1]); path.append(pos)
    return path

def markov_chain_mc(transition_matrix, start, steps=1000, seed=42):
    random.seed(seed)
    state = start; counts = {}
    for _ in range(steps):
        counts[state] = counts.get(state, 0) + 1
        r = random.random(); cumsum = 0
        for next_state, prob in transition_matrix[state].items():
            cumsum += prob
            if r <= cumsum: state = next_state; break
    return {k: v/steps for k, v in counts.items()}

if __name__ == "__main__":
    print(f"Pi estimate: {estimate_pi(100000):.4f}")
