# Training Data Risk Register

Status: active QC file  
Version added: v0.2.9-dev4

## Known risks

| Risk | Severity | Mitigation |
|---|---|---|
| Scaffold answers teach meta-routing instead of useful answering | High | Rewrite sample answers into real task answers before training |
| Broad `must_retrieve` placeholders remain in cards | Medium | Replace with exact source/file paths as the Atlas matures |
| Small models may overfit the fixed answer format | Medium | Include varied phrasing and multiple answer styles |
| Distractor cards may be too obvious | Medium | Use neighboring-lane distractors with shared surface terms |
| Freshness-sensitive claims may become stale | High | Mark volatile records and require current verification |
| LoRA may learn style but not routing | High | Evaluate route accuracy separately from answer polish |
| Atlas RAG may be strong enough without LoRA | Medium | Compare base + Atlas RAG vs LoRA + Atlas RAG |
| Dataset may teach overconfidence | High | Include insufficient-context and exactness-guard records |

## QC rule

Do not advance to training until the dataset has both:

```text
schema validity
answer-quality validity
```

Schema validity alone is not enough.
