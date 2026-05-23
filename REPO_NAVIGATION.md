# Repository Navigation

Version: v0.2.9-dev21  
Status: GitHub upload prep / public review navigation

## Reviewer path

| Step | Read |
|---:|---|
| 1 | `README.md` |
| 2 | `01_strategy/RELATED_WORK.md` |
| 3 | `01_strategy/SOURCE_AND_ATTRIBUTION_POLICY.md` |
| 4 | `03_lane_system/README.md` |
| 5 | `lora_training_lab/04_training_data/TRAINING_PLAN_ATLAS_READER_MINI.md` |
| 6 | `lora_training_lab/04_training_data/OVERNIGHT_TRAINING_RUN_MATRIX.md` |
| 7 | `lora_training_lab/05_evaluation/SMOKE_TRAIN_PROTOCOL.md` |
| 8 | `07_quality_control/PUBLIC_REVIEW_CHECKLIST.md` |

## Folder map

| Folder | Purpose |
|---|---|
| `00_landing_page/` | Plain-language public explanation |
| `01_strategy/` | Strategy, related work, source policy, project claims |
| `02_atlas_contracts/` | Atlas contract schema and naming |
| `03_lane_system/` | Lanes, cards, validation target |
| `04_training_data/` | Pointer showing training material moved to `lora_training_lab/` |
| `05_evaluation/` | Smoke protocol, golden questions, scoring templates |
| `06_experiments/` | Pointer showing experiment material moved to `lora_training_lab/` |
| `07_quality_control/` | QC reports, review checklists, policy checks |
| `08_visuals/` | Diagrams and visual references |
| `09_research_notes/` | Project status notes and decision logs |
| `scripts/` | Repo-level validation, source inventory, and statistics helper scripts |
| `lora_training_lab/` | LoRA training/install lane; keep for the adapter repo, remove only for clean RAG handoff |

## Current stats

```text
seed lanes: 18
seed cards: 216
diagrams: 3
sample/scaffold training records: 21
adapter trained: no
training run completed: no
```

## Important

This is a structured research project in planning/seed-build status.

Do not cite assistant outputs as sources.

Do not claim performance before the smoke train and evaluation results exist.

## v0.2.9-dev7 training scripts

```text
lora_training_lab/scripts/train_atlas_reader_qlora.py
lora_training_lab/scripts/create_train_eval_split.py
lora_training_lab/04_training_data/RUNNABLE_TRAINING_LAYER.md
lora_training_lab/tools/powershell/
```

## v0.2.9-dev8 source ledger

Source materials and code inventories now live in:

```text
10_source_materials/
```

Key files:

```text
10_source_materials/SOURCE_LEDGER.md
10_source_materials/TRAINING_CODE_INVENTORY.md
10_source_materials/TRAINING_CODE_SOURCE_MAP.md
```

## v0.2.9-dev9 citations

Citation files:

```text
10_source_materials/SOURCE_CITATIONS.md
10_source_materials/CITATION_MATRIX.md
10_source_materials/REFERENCES.bib
```

## v0.2.9-dev10 conversation source audit

```text
10_source_materials/CONVERSATION_SOURCE_AUDIT.md
07_quality_control/CONVERSATION_SOURCE_AUDIT_QC_v0.2.9-dev10.md
```

## v0.2.9-dev11 brand/citation polish

```text
01_strategy/BRAND_AND_POSITIONING_GUIDE.md
00_landing_page/PUBLIC_SUMMARY_DRAFT.md
10_source_materials/CITATION_STYLE_GUIDE.md
```

## v0.2.9-dev12 TensorBoard dashboard

```text
lora_training_lab/04_training_data/TENSORBOARD_TRAINING_DASHBOARD.md
lora_training_lab/tools/powershell/start_tensorboard.ps1
lora_training_lab/scripts/list_tensorboard_runs.py
```

## v0.2.9-dev14 lab installer

```text
lora_training_lab/labinstall.bat
lora_training_lab/tools/powershell/labinstall.ps1
lora_training_lab/scripts/lab_smoke_test.py
lora_training_lab/04_training_data/LAB_INSTALL_GUIDE.md
```

## v0.2.9-dev15 labinstall QC

```text
lora_training_lab/scripts/qc_labinstall_static.py
07_quality_control/LAB_INSTALL_QC_v0.2.9-dev15.md
```

## v0.2.9-dev16 AIWF branding

```text
01_strategy/AIWF_BRAND_SYSTEM.md
00_landing_page/AIWF_ATLAS_READER_LANDING_DRAFT.md
00_landing_page/AIWF_README_HEADER_SNIPPET.md
08_visuals/AIWF_VISUAL_BRANDING_NOTES.md
```

## v0.2.9-dev17 no-wins QC

```text
PROJECT_PREINSTALL_STATUS.md
00_landing_page/NO_WINS_YET_PUBLIC_NOTE.md
07_quality_control/REPORT_TEMPLATE_POLICY.md
07_quality_control/NO_WINS_CLAIM_AUDIT_v0.2.9-dev17.md
```

## v0.2.9-dev18 research rationale

```text
01_strategy/RESEARCH_RATIONALE_UNKNOWN_MEANS_INSTRUMENT_IT.md
00_landing_page/UNKNOWN_MEANS_INSTRUMENT_IT.md
05_evaluation/EVALUATION_RATIONALE_USEFUL_FAILURE.md
```

## v0.2.9-dev19 agent protocol lane

```text
AGENTS.md
01_strategy/AGENT_PROTOCOL_LANE.md
05_evaluation/AGENT_ATTACHMENT_LORA_COMPARISON_PLAN.md
00_landing_page/ATLAS_BEFORE_THE_ADAPTER.md
plugins/aiwf-atlas-protocol/
.agents/plugins/marketplace.json
```

## v0.2.9-dev20 repackage / RAG handoff

```text
lora_training_lab/
RAG_HANDOFF_GUIDE.md
03_lane_system/vol1_canonical_research_lanes/
11_incoming_user_updates/
07_quality_control/REPACKAGE_QC_v0.2.9-dev20.md
```

Remove `lora_training_lab/` before using the repo as a clean Atlas/RAG package.

## v0.2.9-dev21 forensic Git preservation

```text
11_incoming_user_updates/AIWF_ATLAS_uploaded_2026-05-23_FOR_FORENSIC_WITH_GIT/
11_incoming_user_updates/AIWF_ATLAS_FORENSIC_GIT_PRESERVATION_REPORT.md
11_incoming_user_updates/AIWF_ATLAS_FORENSIC_GIT_INVENTORY.json
```
