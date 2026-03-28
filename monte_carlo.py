#!/usr/bin/env python3
"""monte_carlo - Monte Carlo simulations."""
import argparse, random, math

def estimate_pi(n):
    inside = sum(1 for _ in range(n) if random.random()**2 + random.random()**2 <= 1)
    return 4 * inside / n

def estimate_integral(f, a, b, n, y_max=1):
    inside = sum(1 for _ in range(n) if random.uniform(0, y_max) <= f(random.uniform(a, b)))
    return (b - a) * y_max * inside / n

def random_walk_2d(steps):
    x, y, max_dist = 0, 0, 0
    for _ in range(steps):
        dx, dy = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
        x += dx; y += dy
        max_dist = max(max_dist, math.sqrt(x*x + y*y))
    return math.sqrt(x*x + y*y), max_dist

def birthday_paradox(n_people, trials=10000):
    collisions = 0
    for _ in range(trials):
        bdays = set()
        for _ in range(n_people):
            b = random.randint(1, 365)
            if b in bdays: collisions += 1; break
            bdays.add(b)
    return collisions / trials

def monty_hall(trials=10000):
    switch_wins = stay_wins = 0
    for _ in range(trials):
        car = random.randint(0, 2); choice = random.randint(0, 2)
        if choice == car: stay_wins += 1
        else: switch_wins += 1
    return stay_wins / trials, switch_wins / trials

def main():
    p = argparse.ArgumentParser(description="Monte Carlo simulations")
    p.add_argument("sim", choices=["pi", "integral", "walk", "birthday", "monty-hall"])
    p.add_argument("-n", type=int, default=100000)
    args = p.parse_args()
    if args.sim == "pi":
        pi = estimate_pi(args.n)
        print(f"Pi estimate: {pi:.6f} (error: {abs(pi-math.pi):.6f})")
    elif args.sim == "integral":
        result = estimate_integral(lambda x: math.sin(x), 0, math.pi, args.n, 1)
        print(f"Integral of sin(x) from 0 to pi: {result:.6f} (exact: 2.0)")
    elif args.sim == "walk":
        trials = min(args.n, 1000)
        dists = [random_walk_2d(100)[0] for _ in range(trials)]
        avg = sum(dists) / len(dists)
        print(f"2D random walk (100 steps, {trials} trials): avg distance = {avg:.2f}")
        print(f"  Expected (sqrt(n)): {math.sqrt(100):.2f}")
    elif args.sim == "birthday":
        for n in [23, 30, 40, 50, 57, 70]:
            prob = birthday_paradox(n, min(args.n, 10000))
            print(f"  {n:2d} people: {prob:.3f} collision probability")
    elif args.sim == "monty-hall":
        stay, switch = monty_hall(args.n)
        print(f"Monty Hall ({args.n} trials):")
        print(f"  Stay win rate:   {stay:.3f}")
        print(f"  Switch win rate: {switch:.3f}")

if __name__ == "__main__":
    main()
