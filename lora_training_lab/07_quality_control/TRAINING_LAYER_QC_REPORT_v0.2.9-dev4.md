# Training Layer QC Report v0.2.9-dev4

Status: QC pass with quality warnings  
Date: 2026-05-22  
Source: `atlas-lora-adapter-v0.2.9-dev3-training-plan-2026-05-22.zip`

## Summary

This pass reviewed the training-plan layer added in v0.2.9-dev3.

The structure is valid, but the sample records should remain classified as scaffold examples, not final training data.

## Structural validation

| Check | Result |
|---|---:|
| Sample records parsed | 21 |
| Parse issues | 0 |
| Structural issues | 0 |
| Average cards per record | 4.29 |
| Validator return code | 0 |
| Builder return code | 0 |
| Generated builder records | 18 |

## Record type counts

- `freshness_check`: 3
- `ignore_distractor`: 12
- `secondary_lane_reference`: 6

## Primary lane coverage in sample records

- `36_retrieval_card_authoring`: 1
- `37_small_model_retrieval_optimization`: 1
- `38_windows_ai_workstation_setup`: 1
- `39_cuda_torch_runtime_alignment`: 2
- `40_model_folder_architecture`: 2
- `41_comfyui_workflow_repair`: 1
- `42_comfyui_socket_contract_debugging`: 2
- `43_inpainting_fundamentals`: 1
- `44_video_vram_optimization`: 2
- `45_last_frame_chaining_video_extension`: 1
- `46_gradio_multi_venv_orchestration`: 1
- `47_raw_rag_vs_atlas_comparison`: 2
- `48_small_vs_large_model_benchmarking`: 1
- `52_source_ledger_maintenance`: 1
- `53_claim_freshness_verification`: 2

## Structural issues

- None found.

## Quality warnings

- SEED-REC-0001: expected answer is scaffold/meta-style; useful for schema testing, not final SFT training.
- SEED-REC-0002: expected answer is scaffold/meta-style; useful for schema testing, not final SFT training.
- SEED-REC-0003: expected answer is scaffold/meta-style; useful for schema testing, not final SFT training.
- SEED-REC-0004: expected answer is scaffold/meta-style; useful for schema testing, not final SFT training.
- SEED-REC-0005: expected answer is scaffold/meta-style; useful for schema testing, not final SFT training.
- SEED-REC-0006: expected answer is scaffold/meta-style; useful for schema testing, not final SFT training.
- SEED-REC-0007: limits field may not strongly enforce exactness/freshness boundaries.
- SEED-REC-0008: limits field may not strongly enforce exactness/freshness boundaries.
- SEED-REC-0009: limits field may not strongly enforce exactness/freshness boundaries.
- SEED-REC-0010: limits field may not strongly enforce exactness/freshness boundaries.
- SEED-REC-0011: limits field may not strongly enforce exactness/freshness boundaries.
- SEED-REC-0012: limits field may not strongly enforce exactness/freshness boundaries.
- SEED-REC-0013: limits field may not strongly enforce exactness/freshness boundaries.
- SEED-REC-0014: limits field may not strongly enforce exactness/freshness boundaries.
- SEED-REC-0015: limits field may not strongly enforce exactness/freshness boundaries.
- SEED-REC-0016: limits field may not strongly enforce exactness/freshness boundaries.
- SEED-REC-0017: limits field may not strongly enforce exactness/freshness boundaries.
- SEED-REC-0018: limits field may not strongly enforce exactness/freshness boundaries.
- SEED-REC-0019: expected answer is scaffold/meta-style; useful for schema testing, not final SFT training.
- SEED-REC-0019: limits field may not strongly enforce exactness/freshness boundaries.
- SEED-REC-0020: expected answer is scaffold/meta-style; useful for schema testing, not final SFT training.
- SEED-REC-0020: limits field may not strongly enforce exactness/freshness boundaries.
- SEED-REC-0021: expected answer is scaffold/meta-style; useful for schema testing, not final SFT training.
- SEED-REC-0021: limits field may not strongly enforce exactness/freshness boundaries.

## Validator output

```text
Records checked: 21
PASSED

Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 720, in _warm_feature_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 704, in _warm_collaboration_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/generated/interface/models.py", line 48821, in hydrate_crdt_from_proto
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/remote.py", line 747, in __call__
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/client.py", line 150, in call
artifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document.
```

## Builder output

```text
Wrote 18 records to /mnt/data/atlas_lora_v029_dev4_qc_work/atlas-lora-adapter/04_training_data/generated_seed_training_records.jsonl

Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 720, in _warm_feature_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 704, in _warm_collaboration_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/generated/interface/models.py", line 48821, in hydrate_crdt_from_proto
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/remote.py", line 747, in __call__
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/client.py", line 150, in call
artifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document.
```

## Strict quality checker output

```text
Records checked: 21
Record type counts:
- freshness_check: 3
- ignore_distractor: 12
- secondary_lane_reference: 6
WARNINGS
- SEED-REC-0001: scaffold/meta answer; not production SFT quality
- SEED-REC-0002: scaffold/meta answer; not production SFT quality
- SEED-REC-0003: scaffold/meta answer; not production SFT quality
- SEED-REC-0003: freshness flag set but answer may not require verification/qualification
- SEED-REC-0004: scaffold/meta answer; not production SFT quality
- SEED-REC-0005: scaffold/meta answer; not production SFT quality
- SEED-REC-0006: scaffold/meta answer; not production SFT quality
- SEED-REC-0006: freshness flag set but answer may not require verification/qualification
- SEED-REC-0007: scaffold/meta answer; not production SFT quality
- SEED-REC-0008: scaffold/meta answer; not production SFT quality
- SEED-REC-0009: scaffold/meta answer; not production SFT quality
- SEED-REC-0010: scaffold/meta answer; not production SFT quality
- SEED-REC-0010: freshness flag set but answer may not require verification/qualification
- SEED-REC-0011: scaffold/meta answer; not production SFT quality
- SEED-REC-0012: scaffold/meta answer; not production SFT quality
- SEED-REC-0013: scaffold/meta answer; not production SFT quality
- SEED-REC-0014: scaffold/meta answer; not production SFT quality
- SEED-REC-0015: scaffold/meta answer; not production SFT quality
- SEED-REC-0016: scaffold/meta answer; not production SFT quality
- SEED-REC-0017: scaffold/meta answer; not production SFT quality
- SEED-REC-0018: scaffold/meta answer; not production SFT quality
- SEED-REC-0019: scaffold/meta answer; not production SFT quality
- SEED-REC-0020: scaffold/meta answer; not production SFT quality
- SEED-REC-0021: scaffold/meta answer; not production SFT quality

Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 720, in _warm_feature_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 704, in _warm_collaboration_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/generated/interface/models.py", line 48821, in hydrate_crdt_from_proto
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/remote.py", line 747, in __call__
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/client.py", line 150, in call
artifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document.
```

## QC verdict

```text
schema_valid: True
training_ready: False
```

The training layer is ready as a planning/schema scaffold.

It is not yet ready as a real LoRA training dataset.

## Required next fixes before training

1. Rewrite scaffold/meta expected answers into actual useful user-facing answers.
2. Expand from 21 sample records to 300-600 smoke records.
3. Add stronger distractor records with neighboring-lane ambiguity.
4. Add more insufficient-context examples.
5. Add more exactness-guard examples.
6. Replace broad source placeholders with exact file/source paths where possible.
7. Human-review at least 50 records before smoke training.

## Important

This is not a v0.3.0 promotion and not a training attempt.
