# Overnight Training Run Matrix

Status: planning matrix  
Version added: v0.2.9-dev6  
Use: choose one or more configs to run overnight after dataset QC passes.

## Hard rule

Do not treat any of these settings as guaranteed.

They are experiment starting points.

## Preflight before every run

- Confirm dataset is answer-quality, not scaffold/meta-only.
- Confirm train/eval split exists.
- Confirm `scripts/validate_training_records.py` passes.
- Confirm `scripts/check_training_record_quality.py` does not show scaffold-heavy warnings.
- Save exact base model name and revision.
- Save exact dataset file/hash.
- Save GPU, driver, CUDA, torch, transformers, peft, trl, bitsandbytes versions.
- Run baseline eval before adapter eval.

## Run matrix

| Run ID | Purpose | Rank | Alpha | Dropout | Target modules | LR | Epochs | Seq len | Packing | Notes |
|---|---|---:|---:|---:|---|---:|---:|---:|---|---|
| A_sanity_r8_lr0001 | lowest-risk sanity | 8 | 16 | 0.05 | q_proj,v_proj | 0.0001 | 1 | 2048 | false | Should train fast; checks pipeline |
| B_baseline_r16_lr0002 | baseline Mini attempt | 16 | 32 | 0.05 | q,k,v,o + MLP | 0.0002 | 2 | 2048 | false | Main first overnight run |
| C_capacity_r32_lr0001 | more behavior capacity | 32 | 64 | 0.05 | q,k,v,o + MLP | 0.0001 | 2 | 2048 | false | Tests whether rank 16 is too small |
| D_stability_r32_lr00005 | slower stable training | 32 | 64 | 0.05 | q,k,v,o + MLP | 0.00005 | 3 | 2048 | false | Use if B/C are unstable or overfit |
| E_nodrop_r16_lr0002 | overfit check | 16 | 32 | 0.00 | q,k,v,o + MLP | 0.0002 | 2 | 2048 | false | Compare against dropout run |
| F_context4096_r16 | longer context test | 16 | 32 | 0.05 | q,k,v,o + MLP | 0.0001 | 2 | 4096 | false | Use only if 2048 truncates cards |
| G_rank64_stress | high-capacity stress | 64 | 128 | 0.05 | q,k,v,o + MLP | 0.0001 | 1 | 2048 | false | Use only after lower ranks behave |
| H_packing_efficiency | speed/throughput test | 16 | 32 | 0.05 | q,k,v,o + MLP | 0.0002 | 2 | 2048 | true | Only after labels/format are safe |

## Recommended first overnight schedule

If running one model overnight, do:

```text
A_sanity_r8_lr0001
B_baseline_r16_lr0002
C_capacity_r32_lr0001
```

If there is time left:

```text
D_stability_r32_lr00005
```

## How to judge the runs

Do not pick the run with the lowest training loss automatically.

Pick the run that improves:

- route correctness;
- exactness guard behavior;
- freshness handling;
- distractor rejection;
- compact useful answer style;
- C vs D improvement over Atlas RAG alone.

## Expected failure modes

| Symptom | Likely issue | Next action |
|---|---|---|
| Repeats lane IDs instead of answering | scaffold leakage | rewrite training answers |
| Always uses secondary lane | cross-lane examples too strong | add negative secondary-lane examples |
| Invents node names/commands | exactness examples too weak | add exactness-guard records |
| Claims current facts from old notes | freshness records too weak | add freshness/verification examples |
| Good format, bad reasoning | overfit to answer pattern | add hard distractors and real answers |
| Training loss fine, eval worse | overfit or bad split | reduce epochs/LR, improve eval set |
| OOM | context/rank too high | lower seq len, rank, batch, or use checkpointing |
