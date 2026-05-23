# Atlas Contract Naming

Status: Phase 6 naming standard  
Date: 2026-05-22  
Project: Atlas Reader LoRA  
Purpose: make every adapter name describe the Atlas/RAG structure it was trained to navigate.

## Why this exists

Atlas Reader LoRA is not a generic style adapter.

It is trained to read a specific kind of structured RAG system. That structure is called an **Atlas Contract**.

The adapter name should tell a user or researcher what the LoRA expects:

- adapter type;
- target base model;
- lane count;
- cards per lane;
- retrieval depth;
- version.

This prevents confusion when different Atlas sizes or retrieval strategies exist.

## Standard naming pattern

Use this format:

```text
atlas-reader-{tier}_{base-model}_{lane-count}L-{cards-per-lane}C-{retrieval-depth}D_v{version}
```

## Recommended first adapter name

```text
atlas-reader-mini_qwen3-4b_128L-12C-5D_v1
```

## Meaning

| Segment | Meaning |
|---|---|
| `atlas-reader` | Adapter family. It reads Atlas-style structured RAG. |
| `mini` | Small-model contract tier. |
| `qwen3-4b` | Compatible base model family and size. |
| `128L` | Trained for a 128-lane Atlas contract. |
| `12C` | Trained for 12 cards per lane. |
| `5D` | Trained for retrieval depth around 5 cards per answer. |
| `v1` | Contract/training version. |

## Why `12C` instead of `12CPL`

`12C` is short and readable once the repo defines that `C` means cards per lane.

If maximum clarity is needed for a public-facing filename, use the long form:

```text
atlas-reader-mini_qwen3-4b_128lanes-12cards-5depth_v1
```

Preferred internal/research form:

```text
atlas-reader-mini_qwen3-4b_128L-12C-5D_v1
```

## Contract tiers

### Mini

Small-model-first.

```text
atlas-reader-mini
```

Target model range:

```text
.8B to 4B
```

Expected Atlas contract:

```text
128 lanes
12 cards per lane
1-5 retrieved cards per answer
compact card schema
strict source priority
strict do-not-confuse rules
```

Purpose:

```text
Stay in the lane. Read the signs. Do not make unsupported claims.
```

### Extended

For larger models after Mini proves useful.

```text
atlas-reader-extended
```

Target model range:

```text
7B+
```

Expected Atlas contract:

```text
128+ lanes
24 cards per lane
5-8 retrieved cards per answer
more secondary-lane support
more synthesis
```

Purpose:

```text
Use more context and perform deeper cross-lane reasoning.
```

### Deep

Research-grade later variant.

```text
atlas-reader-deep
```

Target model range:

```text
14B+ or stronger
```

Expected Atlas contract:

```text
128+ lanes
32 cards per lane
8-12 retrieved cards per answer
larger card network
cross-domain synthesis
```

Purpose:

```text
Test whether a larger Atlas card network improves expert-level reasoning.
```

## Example adapter names

```text
atlas-reader-mini_qwen3-0.8b_128L-12C-2D_v1
atlas-reader-mini_qwen3-1.7b_128L-12C-3D_v1
atlas-reader-mini_qwen3-4b_128L-12C-5D_v1
atlas-reader-extended_qwen3-7b_128L-24C-8D_v1
atlas-reader-deep_qwen3-14b_128L-32C-12D_v1
```

## Retrieval depth guidance

Retrieval depth means the number of cards the model is expected to handle in one answer context.

| Model size | Suggested depth | Example suffix |
|---|---:|---|
| `.8B` to `1.5B` | 1-2 cards | `2D` |
| `2B` to `3B` | 2-3 cards | `3D` |
| `4B` | 3-5 cards | `5D` |
| `7B+` | 5-8 cards | `8D` |
| `14B+` | 8-12 cards | `12D` |

Depth is not a hard runtime limit. It describes the retrieval pattern used during training and evaluation.

## What the name does not mean

`128L-12C-5D` does not mean the adapter can never work with 129 lanes or 13 cards per lane.

It means the adapter was trained and evaluated against that contract.

Small changes are acceptable. Major changes should be treated as a new contract.

## When to train a new LoRA

Train a new LoRA when the Atlas contract changes substantially.

Examples:

| Change | New LoRA needed? | Reason |
|---|---|---|
| 128 lanes to 130 lanes | Usually no | Small structure drift. |
| 12 cards per lane to 14 | Usually no | Small card-count drift. |
| 12 compact cards to 32 detailed cards | Yes | Different navigation contract. |
| 5-card retrieval depth to 12-card depth | Yes | Different context expectations. |
| AIWF-only lanes to multi-domain Atlas lanes | Probably yes | Different generalization target. |
| Different base model architecture | Yes | LoRAs are usually base-model specific. |

## Base model compatibility

A LoRA normally needs to match the base model family it was trained on.

The naming convention must include the base model:

```text
atlas-reader-mini_qwen3-4b_128L-12C-5D_v1
```

Do not release an adapter as:

```text
atlas-reader-mini_128L-12C-5D_v1
```

unless it is a training recipe or dataset, not a model adapter.

## Dataset naming

Datasets should use a related but separate pattern:

```text
atlas-reader-dataset_{lane-count}L-{cards-per-lane}C-{record-count}R_v{version}
```

Example:

```text
atlas-reader-dataset_128L-12C-5000R_v1
```

## Contract file naming

Atlas contract files should use:

```text
atlas-contract_{tier}_{lane-count}L-{cards-per-lane}C-{retrieval-depth}D_v{version}.json
```

Example:

```text
atlas-contract_mini_128L-12C-5D_v1.json
```

## Research run naming

Experiments should include model, contract, and run number:

```text
run_{base-model}_{contract}_{date}_{run-number}
```

Example:

```text
run_qwen3-4b_128L-12C-5D_2026-05-22_001
```

## Public wording

Use this wording for public docs:

> Atlas Reader LoRA adapters are named by their Atlas Contract, so the filename shows the base model, lane count, cards per lane, retrieval depth, and training version.

## Current locked baseline

The current baseline is:

```text
atlas-reader-mini_{base-model}_128L-12C-5D_v1
```

For the first serious small-model target:

```text
atlas-reader-mini_qwen3-4b_128L-12C-5D_v1
```

## Final rule

The adapter name should make the expected map visible.

If someone has to open the README to know what kind of Atlas the LoRA expects, the name is too vague.
