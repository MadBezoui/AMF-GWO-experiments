
import argparse, json, time, numpy as np
from amfgwo.algorithm import AMFGWO

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--instance", required=True)
    p.add_argument("--seed", type=int, default=1)
    p.add_argument("--pop", type=int, default=50)
    p.add_argument("--gen", type=int, default=300)
    args = p.parse_args()

    inst = json.load(open(args.instance))
    algo = AMFGWO(inst["bounds"], pop_size=args.pop, max_gen=args.gen, seed=args.seed)
    t0 = time.time()
    X, F = algo.run()
    print(f"Run finished in {time.time()-t0:.2f}s, {len(X)} Pareto solutions.")
    np.savez("results.npz", X=X, F=F)
    print("Saved results to results.npz")

if __name__ == "__main__":
    main()
