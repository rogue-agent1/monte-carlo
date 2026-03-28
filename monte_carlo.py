#!/usr/bin/env python3
"""monte_carlo - Monte Carlo simulations."""
import sys,random,math
def estimate_pi(n=1000000):
    inside=sum(1 for _ in range(n) if random.random()**2+random.random()**2<=1)
    return 4*inside/n
def integrate(f,a,b,n=100000):
    total=sum(f(random.uniform(a,b)) for _ in range(n))
    return(b-a)*total/n
def birthday_paradox(people=23,trials=10000):
    matches=0
    for _ in range(trials):
        bdays=set()
        for _ in range(people):
            b=random.randint(1,365)
            if b in bdays:matches+=1;break
            bdays.add(b)
    return matches/trials
def monty_hall(trials=10000,switch=True):
    wins=0
    for _ in range(trials):
        car=random.randint(0,2);choice=random.randint(0,2)
        doors=[0,1,2];doors.remove(car if car!=choice else (set(doors)-{car,choice}).pop())
        if switch:choice=(set([0,1,2])-{choice}-set(doors)).pop() if len(set([0,1,2])-{choice}-set(doors))>0 else choice
        if choice==car:wins+=1
    return wins/trials
if __name__=="__main__":
    if len(sys.argv)<2:print("Usage: monte_carlo.py <pi|integrate|birthday|monty>");sys.exit(1)
    cmd=sys.argv[1];n=int(sys.argv[2]) if len(sys.argv)>2 else 100000
    if cmd=="pi":pi=estimate_pi(n);print(f"π ≈ {pi:.6f} (error: {abs(pi-math.pi):.6f})")
    elif cmd=="birthday":p=birthday_paradox(23,n);print(f"Birthday paradox (23 people): {p:.2%}")
    elif cmd=="monty":
        s=monty_hall(n,True);ns=monty_hall(n,False)
        print(f"Monty Hall - Switch: {s:.2%}, Stay: {ns:.2%}")
