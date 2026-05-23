# Evaluation Rationale: What Counts as Useful

Status: active evaluation note  
Version added: v0.2.9-dev18  
Date: 2026-05-22

## Useful success

The adapter is useful if:

```text
Atlas RAG + LoRA
```

beats:

```text
Atlas RAG alone
```

on measured behaviors without damaging source discipline.

## Useful failure

The adapter failure is useful if it identifies why the idea did not work.

Useful failure categories:

| Failure | What it teaches |
|---|---|
| LoRA learns formatting only | Need better answer-quality records |
| LoRA overuses lane labels | Training examples leak routing language |
| LoRA ignores exactness guard | Need stronger negative/exactness examples |
| LoRA worsens freshness handling | Need more stale/current claim examples |
| Atlas RAG beats raw RAG but LoRA adds nothing | Value may be in structure, not adapter |
| Raw RAG beats Atlas RAG | Lane/card design needs redesign |
| Small model cannot use the context | Contract may be too complex for target model |

## Non-useful failure

A failure is not useful if:

- logs are missing;
- dataset version is unknown;
- config is unknown;
- model is unknown;
- outputs are not saved;
- scoring is changed after seeing results.

## Rule

Do not protect the hypothesis.

Protect the evidence.
