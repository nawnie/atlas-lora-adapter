# Training Code Source Map

Status: active source map  
Version added: v0.2.9-dev8

## Purpose

This file maps the training code to the official references it is based on.

## Source map

| Repo file | Source basis | Why |
|---|---|---|
| `scripts/train_atlas_reader_qlora.py` | Hugging Face TRL SFTTrainer docs | SFT training, conversational datasets, assistant-only loss, PEFT support |
| `scripts/train_atlas_reader_qlora.py` | Hugging Face PEFT LoRAConfig docs | LoRA rank, alpha, dropout, target modules, task type |
| `scripts/train_atlas_reader_qlora.py` | Hugging Face Transformers bitsandbytes docs | 4-bit quantization, NF4, double quantization, BitsAndBytesConfig |
| `scripts/train_atlas_reader_qlora.py` | Hugging Face Transformers Trainer docs | training arguments, logging/eval/save cadence |
| `scripts/render_atlas_sft_dataset.py` | Atlas training-record schema | Converts Atlas record format into conversational SFT format |
| `scripts/create_train_eval_split.py` | Project evaluation protocol | Creates deterministic split for smoke training |
| `scripts/compute_significance.py` | Project smoke protocol | Computes paired evaluation statistics |

## Important

The official docs justify API usage.

They do not prove that the Atlas Reader LoRA works.

Performance proof requires measured local outputs from the smoke protocol.
