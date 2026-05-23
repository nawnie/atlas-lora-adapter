# Related Work and Smoke Protocol QC v0.2.9-dev5

Status: QC pass  
Date: 2026-05-22

## Added

```text
01_strategy/RELATED_WORK.md
05_evaluation/SMOKE_TRAIN_PROTOCOL.md
05_evaluation/GOLDEN_QUESTIONS_SMOKE_25.jsonl
05_evaluation/SMOKE_RESULTS_TEMPLATE.csv
05_evaluation/sample_smoke_results.csv
05_evaluation/SMOKE_TRAIN_RESULTS_REPORT_TEMPLATE.md
scripts/compute_significance.py
```

## Related-work cleanup

`Phase 6` wording was changed to `cross-corpus transfer experiment` to match current project governance.

## Significance script test

Return code:

```text
0
```

Output:

```text
# Paired Smoke Evaluation
Condition A: atlas_rag
Condition B: atlas_lora_rag
Paired questions: 25

## Pass rates
atlas_rag: 13/25 = 0.520
atlas_lora_rag: 16/25 = 0.640

## McNemar exact test
A wrong / B right: 7
A right / B wrong: 4
two-sided exact p-value: 0.548828

## Composite score
Mean difference (B - A): 0.120
Bootstrap 95% CI: [-0.400, 0.680]

## Interpretation guard
Small-n warning: directional evidence only; do not overclaim.
CI crosses zero; evidence is inconclusive.

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

## Verdict

```text
related_work_added: true
smoke_protocol_added: true
significance_script_runs: True
training_run_completed: false
adapter_trained: false
```

This is not a v0.3.0 promotion.
