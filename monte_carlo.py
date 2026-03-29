#!/usr/bin/env python3
"""monte_carlo - Monte Carlo simulations."""
import sys,argparse,json,random,math
def estimate_pi(n):
    inside=sum(1 for _ in range(n) if random.random()**2+random.random()**2<=1)
    return 4*inside/n
def integrate(fn_str,a,b,n):
    total=0
    for _ in range(n):
        x=random.uniform(a,b)
        total+=eval(fn_str,{"x":x,"math":math,"__builtins__":{}})
    return (b-a)*total/n
def random_walk(steps,dims=2):
    pos=[0]*dims
    path=[pos[:]]
    for _ in range(steps):
        d=random.randint(0,dims-1);pos[d]+=random.choice([-1,1])
        path.append(pos[:])
    dist=math.sqrt(sum(p**2 for p in pos))
    return dist,path
def main():
    p=argparse.ArgumentParser(description="Monte Carlo")
    sub=p.add_subparsers(dest="cmd")
    pi=sub.add_parser("pi");pi.add_argument("-n",type=int,default=100000)
    ig=sub.add_parser("integrate");ig.add_argument("fn");ig.add_argument("a",type=float);ig.add_argument("b",type=float);ig.add_argument("-n",type=int,default=100000)
    rw=sub.add_parser("walk");rw.add_argument("--steps",type=int,default=1000);rw.add_argument("--trials",type=int,default=100)
    args=p.parse_args()
    if args.cmd=="pi":
        pi_est=estimate_pi(args.n)
        print(json.dumps({"estimate":round(pi_est,6),"actual":round(math.pi,6),"error":round(abs(pi_est-math.pi),6),"samples":args.n}))
    elif args.cmd=="integrate":
        result=integrate(args.fn,args.a,args.b,args.n)
        print(json.dumps({"function":args.fn,"range":[args.a,args.b],"integral":round(result,6),"samples":args.n}))
    elif args.cmd=="walk":
        dists=[random_walk(args.steps)[0] for _ in range(args.trials)]
        print(json.dumps({"steps":args.steps,"trials":args.trials,"avg_distance":round(sum(dists)/len(dists),4),"expected":round(math.sqrt(args.steps),4),"max_distance":round(max(dists),4)}))
    else:p.print_help()
if __name__=="__main__":main()
