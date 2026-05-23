# Training Research Notes: Atlas Reader LoRA

Status: research planning  
Version added: v0.2.9-dev6  
Purpose: prepare multiple overnight training settings to test once answer-quality records exist.

## Important boundary

This project is still pre-training.

The current repository has schemas, sample records, and a smoke protocol, but the sample records were previously QC'd as scaffold-quality only.

Do not run a meaningful adapter training attempt until the dataset has real answer-quality records.

## What we are training

The target is not a knowledge-memorization adapter.

The target is a behavior adapter:

```text
query -> primary lane -> selected card pack -> source/claim rules -> grounded answer
```

The Atlas/RAG keeps the facts.

The LoRA learns the reading protocol.

## Training method baseline

Use supervised fine-tuning with LoRA/QLoRA first.

Why:

- SFT directly teaches route/answer behavior.
- LoRA keeps the base model mostly frozen and trains small adapter weights.
- QLoRA keeps the base model quantized to reduce memory cost.
- The smoke run needs a simple, measurable training path before preference optimization.

## Things to vary overnight

The main training knobs worth testing are:

| Knob | Values to test | Why it matters |
|---|---|---|
| LoRA rank `r` | 8, 16, 32, 64 | Adapter capacity |
| LoRA alpha | 16, 32, 64, 128 | Adapter scaling |
| LoRA dropout | 0.00, 0.03, 0.05, 0.10 | Overfit control |
| Target modules | q/v only, q/k/v/o, all linear | How much behavior capacity the adapter can change |
| Learning rate | 0.00005, 0.0001, 0.0002 | Stability vs speed |
| Epochs | 1, 2, 3 | Underfit vs overfit |
| Sequence length | 1024, 2048, 4096 | Context pack size and truncation risk |
| Packing | false first, true later | Efficiency vs clean record boundaries |
| Assistant-only loss | true when supported | Prevents training on user/context tokens |
| Quantization | 4-bit NF4 + double quant | Fits larger base models in VRAM |

## Recommended testing order

Start with stability.

Do not begin with the largest rank or longest context.

Suggested order:

1. conservative rank 8 / LR 0.0001 sanity run;
2. rank 16 / LR 0.0002 baseline run;
3. rank 32 / LR 0.0001 capacity run;
4. rank 32 / LR 0.00005 stability run;
5. rank 64 stress test only if earlier runs behave well.

## What to watch overnight

Stop or mark failed if:

- training loss becomes NaN;
- training loss drops fast but eval behavior gets worse;
- outputs repeat routing labels instead of answering;
- adapter overuses secondary lanes;
- adapter makes more unsupported exact claims;
- adapter ignores freshness checks;
- adapter learns scaffold/meta phrasing.

Good signs:

- route accuracy improves;
- exactness guard improves;
- freshness handling improves;
- answer format stays compact;
- adapter does not overfit to lane IDs;
- Atlas RAG + LoRA beats Atlas RAG alone on the same questions.

## Key evaluation rule

The adapter only proves value if:

```text
base model + Atlas RAG + LoRA
```

beats:

```text
base model + Atlas RAG
```

on the same scored questions.

If Atlas RAG already gives the improvement and LoRA adds nothing, that is still useful research, but it is not proof that the adapter itself helped.

## Source notes

This file intentionally cites concepts at the source level in the repo's related-work/source-policy style. Before public release, verify each source against the primary document.

- LoRA: PEFT LoRA docs and LoRA paper.
- QLoRA: QLoRA paper, BitsAndBytes/Transformers quantization docs.
- SFT: Hugging Face TRL SFTTrainer docs.


## Citation-backed training-code basis

Use the following citation keys when discussing the training-code choices:

```text
SFTTrainer / messages / assistant-only loss / packing: hf_trl_sfttrainer
LoRA config knobs: hf_peft_loraconfig, hu2021lora
QLoRA / NF4 / double quantization: dettmers2023qlora, hf_transformers_bitsandbytes
gradient accumulation / checkpointing: hf_transformers_trainer
```

Full citation details are in:

```text
10_source_materials/SOURCE_CITATIONS.md
10_source_materials/REFERENCES.bib
```
