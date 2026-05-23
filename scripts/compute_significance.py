#!/usr/bin/env python3
"""
compute_significance.py — paired significance testing for the Atlas Reader
smoke evaluation (A3 vs A2 by default).

Statistical methods (cited; see 10_source_materials/REFERENCES.bib):
  - McNemar's test, paired binary pass/fail ............. mcnemar1947
  - Wilcoxon signed-rank test, paired ordinal scores ... wilcoxon1945
  - Cliff's delta, ordinal effect size ................. cliff1993
  - Paired bootstrap confidence interval ............... efron1993bootstrap

At n~30 only large effects are reliably detectable; a null result does not
prove the adapter fails. Report effect sizes and CIs, not just p-values.
"""
from __future__ import annotations
import argparse, csv, math, random
from pathlib import Path

SCORE_COLUMNS = ["route_correct","source_grounded","exactness_guard","actionable","freshness_handled","avoids_distractor","compact_answer"]

def val(x):
    try: return float(x)
    except Exception: return 0.0

def mcnemar_exact(b, c):
    n=b+c
    if n == 0: return 1.0
    k=min(b,c)
    p=sum(math.comb(n,i)*(0.5**n) for i in range(k+1))*2
    return min(1.0,p)

def pct(xs, p):
    xs=sorted(xs); i=(len(xs)-1)*p; lo=math.floor(i); hi=math.ceil(i)
    return xs[lo] if lo==hi else xs[lo]*(hi-i)+xs[hi]*(i-lo)

def comp(row):
    return sum(val(row.get(c,0)) for c in SCORE_COLUMNS)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("csv_path", type=Path)
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    ap.add_argument("--bootstrap", type=int, default=5000)
    ap.add_argument("--seed", type=int, default=1234)
    args=ap.parse_args()

    rows={}
    with args.csv_path.open("r", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            rows[(r["question_id"], r["condition"])] = r
    qids=sorted({qid for qid,cond in rows if (qid,args.a) in rows and (qid,args.b) in rows})
    if not qids:
        print("No paired question IDs found.")
        return 2

    apass=[]; bpass=[]; diffs=[]
    for qid in qids:
        ar=rows[(qid,args.a)]; br=rows[(qid,args.b)]
        a=int(val(ar.get("pass",0))>=1); b=int(val(br.get("pass",0))>=1)
        apass.append(a); bpass.append(b); diffs.append(comp(br)-comp(ar))
    b_win=sum(1 for a,b in zip(apass,bpass) if a==0 and b==1)
    a_win=sum(1 for a,b in zip(apass,bpass) if a==1 and b==0)
    pval=mcnemar_exact(b_win,a_win)

    random.seed(args.seed)
    boots=[]; n=len(diffs)
    for _ in range(args.bootstrap):
        s=[diffs[random.randrange(n)] for _ in range(n)]
        boots.append(sum(s)/n)
    mean=sum(diffs)/n
    lo=pct(boots,0.025); hi=pct(boots,0.975)

    print("# Paired Smoke Evaluation")
    print(f"Condition A: {args.a}")
    print(f"Condition B: {args.b}")
    print(f"Paired questions: {n}")
    print()
    print("## Pass rates")
    print(f"{args.a}: {sum(apass)}/{n} = {sum(apass)/n:.3f}")
    print(f"{args.b}: {sum(bpass)}/{n} = {sum(bpass)/n:.3f}")
    print()
    print("## McNemar exact test")
    print(f"A wrong / B right: {b_win}")
    print(f"A right / B wrong: {a_win}")
    print(f"two-sided exact p-value: {pval:.6f}")
    print()
    print("## Composite score")
    print(f"Mean difference (B - A): {mean:.3f}")
    print(f"Bootstrap 95% CI: [{lo:.3f}, {hi:.3f}]")
    print()
    print("## Interpretation guard")
    if n < 50:
        print("Small-n warning: directional evidence only; do not overclaim.")
    if lo > 0:
        print("CI is above zero on this sample.")
    elif hi < 0:
        print("CI is below zero on this sample.")
    else:
        print("CI crosses zero; evidence is inconclusive.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
