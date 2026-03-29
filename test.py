import math
from monte_carlo import estimate_pi, monte_carlo_integrate, bootstrap, random_walk, markov_chain_mc
pi = estimate_pi(100000)
assert abs(pi - math.pi) < 0.05
integral = monte_carlo_integrate(lambda x: x**2, 0, 1, 100000)
assert abs(integral - 1/3) < 0.02
data = [1,2,3,4,5,6,7,8,9,10]
bs = bootstrap(data, lambda d: sum(d)/len(d))
assert 4 < bs["mean"] < 7
assert bs["ci_low"] < bs["ci_high"]
walk = random_walk(100)
assert len(walk) == 101 and walk[0] == 0
tm = {"A": {"A":0.7,"B":0.3}, "B": {"A":0.4,"B":0.6}}
dist = markov_chain_mc(tm, "A", 10000)
assert abs(dist.get("A",0) - 0.571) < 0.1
print("monte_carlo tests passed")
