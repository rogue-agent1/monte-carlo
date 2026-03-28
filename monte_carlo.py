#!/usr/bin/env python3
"""Monte Carlo — estimate pi, integrate functions, simulate."""
import sys, random, math
def estimate_pi(n=100000):
    inside=sum(1 for _ in range(n) if random.random()**2+random.random()**2<=1)
    return 4*inside/n
def integrate(f, a, b, n=100000):
    total=sum(f(random.uniform(a,b)) for _ in range(n))
    return (b-a)*total/n
def random_walk(steps=1000, dims=2):
    pos=[0]*dims
    for _ in range(steps):
        d=random.randint(0,dims-1); pos[d]+=random.choice([-1,1])
    return math.sqrt(sum(x**2 for x in pos))
def cli():
    n=int(sys.argv[1]) if len(sys.argv)>1 else 100000
    pi=estimate_pi(n)
    print(f"  π estimate ({n} samples): {pi:.6f} (error: {abs(pi-math.pi):.6f})")
    area=integrate(lambda x: math.sin(x), 0, math.pi, n)
    print(f"  ∫sin(x)dx [0,π] = {area:.6f} (exact: 2.0)")
    walks=[random_walk(1000) for _ in range(100)]
    print(f"  2D random walk (1000 steps, 100 trials): avg dist = {sum(walks)/len(walks):.1f}")
if __name__=="__main__": cli()
