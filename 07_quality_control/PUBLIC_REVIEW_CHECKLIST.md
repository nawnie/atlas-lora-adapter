# Public Review Checklist

Status: active review checklist  
Version added: v0.2.9-dev6.2

Use this before sharing the repo publicly or asking for outside technical review.

## Claim review

- [ ] Does the README avoid claiming a new LoRA algorithm?
- [ ] Does the repo avoid claiming the adapter works before training?
- [ ] Does related work credit prior art before stating the niche?
- [ ] Does the project state its contribution as methodology/interface, not algorithm invention?
- [ ] Does the project say the load-bearing test is transfer/evaluation?

## Source review

- [ ] Are AI assistants treated only as drafting aids, not sources?
- [ ] Are related-work items marked as leads until primary sources are verified?
- [ ] Are volatile claims marked for freshness verification?
- [ ] Are current tool/model/license claims avoided unless sourced?

## Training-data review

- [ ] Are sample records clearly marked as scaffold examples?
- [ ] Does the repo warn not to train final adapters on scaffold-only answers?
- [ ] Does the quality gate require real answer-quality records?
- [ ] Are exactness and freshness behaviors explicitly tested?

## Evaluation review

- [ ] Does the repo define base/no-RAG, raw RAG, Atlas RAG, and Atlas RAG + LoRA conditions?
- [ ] Does the repo identify C vs D as the key adapter-value comparison?
- [ ] Does the repo include paired evaluation/statistics tooling?
- [ ] Does the repo warn that n=25 is directional only?

## Visual review

- [ ] Are all three diagrams present in `08_visuals/`?
- [ ] Are diagrams treated as explanatory assets, not proof?
- [ ] Are diagrams named clearly?

## Governance review

- [ ] Is the project still below v0.3.0?
- [ ] Does the owner-approval gate remain active?
- [ ] Is the version clearly marked as a dev/polish build?
