# Manual Training Data Review Checklist

Status: active checklist  
Version added: v0.2.9-dev4

Use this before any smoke training run.

## Record-level checklist

For each reviewed record, confirm:

- [ ] JSONL parses correctly.
- [ ] Record type is correct.
- [ ] Context pack has 1-5 cards.
- [ ] Primary lane is correct.
- [ ] Secondary lane is justified, if present.
- [ ] Distractor cards are ignored, if present.
- [ ] Expected answer actually answers the user.
- [ ] Expected answer does not only describe routing.
- [ ] Exact commands, node names, paths, versions, or licenses are not invented.
- [ ] Freshness-sensitive claims are qualified or sourced.
- [ ] The answer follows the relevant card answer pattern.
- [ ] The answer does not overclaim Atlas/LoRA performance.

## Dataset-level checklist

Before smoke training, confirm:

- [ ] At least 300 records exist.
- [ ] At least 50 records have human review.
- [ ] All high-risk records are reviewed.
- [ ] All freshness records are reviewed.
- [ ] All exactness-guard records are reviewed.
- [ ] All secondary-lane records are reviewed.
- [ ] Failure cases are included.
- [ ] Distractor cases are included.
- [ ] Insufficient-context cases are included.
- [ ] The dataset card states limitations.

## Hard stop

Do not run a real training attempt if most records still contain scaffold/meta answers.
