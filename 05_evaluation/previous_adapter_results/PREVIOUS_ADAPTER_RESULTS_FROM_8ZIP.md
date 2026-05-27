# Previous Atlas Adapter Evaluation Results

Date: 2026-05-27

## Scope

This file summarizes the prior Atlas LoRA adapter evaluation runs that led into the later O mixed-schema off-ramp pass.

It preserves run-level metrics, comparison conclusions, and token-cost results.

## Main Results

| Run | Adapter Pass | Base Pass | Adapter Avg Tokens | Base Avg Tokens | Key read |
|---|---:|---:|---:|---:|---|
| `J_seed_cards_full_r16_lr0002_base_vs_adapter` | 59/65 | 5/65 | 652.94 | 647.97 | Best 0.5B practical compact-card run before O. |
| `K_seed_cards_full_r16_lr0002_atlas_trigger_base_vs_adapter` | 58/65 | 10/65 | 687.83 | 693.58 | Activator-token variant; slightly worse than J and higher token cost. |
| `L_seed_cards_capacity_r32_lr0001_base_vs_adapter` | 57/65 | 5/65 | 653.05 | 647.97 | Higher-rank 0.5B variant; did not improve over J. |
| `N_seed_cards_4b_r16_lr0001_1epoch_base_vs_adapter` | 65/65 | 1/65 | 647.00 | 646.40 | Best compact-card quality run before O; 4B adapter reached 65/65 on this eval. |
| `base_vs_adapter_20260526_095842` | 2/2 | 0/2 | n/a | n/a | Tiny two-record smoke check; useful only as a sanity check. |
| `base_vs_adapter_20260526_095918` | 38/65 | 4/65 | n/a | n/a | Early full 65-record run; adapter improved pass rate but still missed many lane routes. |
| `workspace_rag_J_base_vs_adapter` | 2/65 | 0/65 | 3327.37 | 3325.91 | Raw workspace/RAG control; routed well with adapter but failed grounding and cost far more tokens. |

## Compact Adapter Comparison

| Run | Model | Setting | Adapter Pass | Base Pass | Avg Tokens/Query | Quality per 1k Tokens | Main Finding |
|---|---|---|---:|---:|---:|---:|---|
| J | Qwen 0.5B Chat | r16, LR 0.0002, 2 epochs | 59/65 | 5/65 | 652.9 | 1.39 | Best 0.5B result before O |
| K | Qwen 0.5B Chat | J plus `*atlas` activator | 58/65 | 10/65 | 687.8 | 1.30 | Activator cost tokens and did not help |
| L | Qwen 0.5B Chat | r32, LR 0.0001, 2 epochs | 57/65 | 5/65 | 653.0 | 1.34 | Bigger rank did not help |
| N | Qwen 4B Chat | r16, LR 0.0001, 1 epoch | 65/65 | 1/65 | 647.0 | 1.55 | Best quality result before O |
| Workspace/RAG J | Qwen 0.5B Chat | raw lane files in prompt | 2/65 | 0/65 | 3327.4 | 0.01 | Raw context was costly and noisy |

Quality per 1k tokens is pass rate divided by average total query tokens, scaled to 1000. It is a rough efficiency comparison rather than a final benchmark metric.

## Token Cost Picture

For 1000 similar queries:

- J compact adapter prompt: about 653k total tokens
- N 4B compact adapter prompt: about 647k total tokens
- K activator prompt: about 688k total tokens
- Raw workspace/RAG prompt: about 3.33M total tokens

Raw workspace context cost about 5.1x as many tokens as the compact adapter path in this run and produced far fewer passing answers.

## What The Prior Runs Suggested

The lane/card representation appears useful in these controlled runs. The adapter learned routing, grounding, and answer shape from compact seed-card records.

The activator token is not worth using as the primary routing mechanism. It added prompt cost and slightly reduced pass rate.

Increasing the 0.5B adapter rank was not the fix. The r32 run produced strong training behavior but worse held-out behavior than J.

The 4B model raised the observed ceiling in this eval set. With the same basic data and one epoch, N reached 65/65. That suggests the adapter direction benefits from a stronger base model, but broader validation is still required.

Raw workspace/RAG directory dumps are not a good main path for this task. Feeding full lane directories into the prompt made the model route better but answer worse under the exact card-grounded evaluator.

## Workspace/RAG Control

| Condition | Pass | Route Correct | Source Grounded | Exactness Guard | Hallucination Flags | Avg Prompt Tokens | Avg Total Tokens |
|---|---:|---:|---:|---:|---:|---:|---:|
| workspace_base | 0/65 | 14/65 | 0/65 | 14/65 | 1/65 | 3197.7 | 3325.9 |
| workspace_adapter | 2/65 | 63/65 | 2/65 | 44/65 | 22/65 | 3197.7 | 3327.4 |

The adapter still routed well with raw lane files, but the final answers failed source/card grounding and exactness checks. This suggests the raw workspace format was noisy for this task. The lane/card idea worked best when cards were distilled into a compact training/eval representation instead of full lane directories being placed into context.

## Recommendation From Prior Runs

Before O, the best quality path was N when 4B inference was acceptable. The best small/fast practical path was J.

The next useful work identified by these prior runs was harder eval data, exact ID-copy reinforcement, compact retrieval-card testing, and avoiding activator-token dependence.
