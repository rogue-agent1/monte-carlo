#!/usr/bin/env python3
"""monte_carlo - Monte Carlo simulations (pi, integration, birthday paradox)."""
import sys, random, math

def estimate_pi(n=1000000):
    inside=sum(1 for _ in range(n) if random.random()**2+random.random()**2<=1)
    pi_est=4*inside/n
    print(f"  π ≈ {pi_est:.6f} (actual: {math.pi:.6f}, error: {abs(pi_est-math.pi):.6f})")
    print(f"  Samples: {n:,}")

def integrate(f_str, a, b, n=1000000):
    """Estimate integral of f from a to b."""
    f=eval(f'lambda x: {f_str}')
    total=sum(f(random.uniform(a,b)) for _ in range(n))
    result=(b-a)*total/n
    print(f"  ∫({f_str}) from {a} to {b} ≈ {result:.6f}")

def birthday(people=23, trials=100000):
    matches=0
    for _ in range(trials):
        bdays=set()
        for _ in range(people):
            b=random.randint(1,365)
            if b in bdays: matches+=1; break
            bdays.add(b)
    prob=matches/trials
    print(f"  P(shared birthday in {people} people) ≈ {prob:.4f} ({prob*100:.1f}%)")

def monty_hall(trials=100000):
    switch_wins=stay_wins=0
    for _ in range(trials):
        prize=random.randint(0,2)
        choice=random.randint(0,2)
        if choice==prize: stay_wins+=1
        else: switch_wins+=1
    print(f"  Stay:   {stay_wins/trials*100:.1f}%")
    print(f"  Switch: {switch_wins/trials*100:.1f}%")

def main():
    args=sys.argv[1:]
    if not args or '-h' in args:
        print("Usage:\n  monte_carlo.py pi [N]\n  monte_carlo.py integrate 'x**2' 0 1\n  monte_carlo.py birthday [N]\n  monte_carlo.py monty"); return
    n=int(args[1]) if len(args)>1 and args[1].isdigit() else 100000
    if args[0]=='pi': estimate_pi(n)
    elif args[0]=='integrate': integrate(args[1],float(args[2]),float(args[3]),n)
    elif args[0]=='birthday': birthday(n if n<366 else 23, 100000)
    elif args[0]=='monty': monty_hall()
    else: estimate_pi()

if __name__=='__main__': main()
