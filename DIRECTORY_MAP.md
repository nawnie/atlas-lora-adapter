# Directory Map

```text
atlas-lora-adapter/
  README.md
  REPO_NAVIGATION.md
  DIRECTORY_MAP.md
  ROADMAP.md
  MILESTONES.md
  VERSIONING_POLICY.md
  RELEASE_GATES.md
  HUMAN_RELEASE_APPROVAL_GATE.md
  CHANGELOG.md
  MANIFEST.json
  LICENSE_NOTICE.md
  requirements.txt

  00_landing_page/
    README.md
    LANDING_PAGE_COPY.md
    LANDING_PAGE_PLAIN_TEXT.txt

  01_strategy/
    README.md
    ATLAS_READER_LORA_STRATEGY.md
    ARCHITECTURE_OVERVIEW.md
    CLAIMS_AND_LIMITS.md
    SMALL_MODEL_ATLAS_READER_MODE.md
    STANDARD_RAG_VS_ATLAS_RAG.md
    TERMINOLOGY.md

  02_atlas_contracts/
    README.md
    ATLAS_CONTRACT_NAMING.md
    ATLAS_CONTRACT_SCHEMA_V1.json
    atlas-contract_mini_128L-12C-5D_v1.json

  03_lane_system/
    README.md
    atlas-lane-validation/
      ATLAS_128_LANE_TARGET.md
      ATLAS_128_LANE_TARGET.csv
      atlas_128_lane_target.json
      CARD_TARGET_PLAN.md
      LANE_VALIDATION_SCHEMA.json
      LANE_VALIDATION_WORKFLOW.md
      PRETRAINING_GATE.md
    lanes/
      36_retrieval_card_authoring/
      37_small_model_retrieval_optimization/
      41_comfyui_workflow_repair/
      42_comfyui_socket_contract_debugging/
      44_video_vram_optimization/
      45_last_frame_chaining_video_extension/

  04_training_data/
    TRAINING_MOVED_TO_LORA_LAB.md

  05_evaluation/
    README.md
    EVALUATION_PLAN.md
    RUBRIC.md
    BASELINE_MATRIX.md
    GOLDEN_QUESTIONS_SEED.jsonl
    RESULTS_TEMPLATE.csv

  06_experiments/
    EXPERIMENTS_MOVED_TO_LORA_LAB.md

  lora_training_lab/
    README.md
    labinstall.bat
    requirements-training.txt
    04_training_data/
      SAMPLE_ATLAS_READER_MINI_RECORDS.jsonl
      TRAINING_PLAN_ATLAS_READER_MINI.md
      TRAINING_RECORD_QUALITY_GATES.md
      OVERNIGHT_TRAINING_RUN_MATRIX.md
      ATLAS_SFT_FORMATTING_GUIDE.md
    05_evaluation/
      SMOKE_TRAIN_PROTOCOL.md
    06_experiments/
      training_configs/
    scripts/
      train_atlas_reader_qlora.py
      create_train_eval_split.py
      qc_labinstall_static.py
    tools/
      powershell/

  07_quality_control/
    README.md
    QC_REPORT_v0.2.6.md
    QC_SUMMARY_v0.2.6.json
    v0.3_OWNER_REVIEW_PACKET.md

  08_visuals/
    README.md
    ATLAS_SYSTEM_OVERVIEW_DIAGRAM.png
    ATLAS_SYSTEM_OVERVIEW_DIAGRAM.md

  09_research_notes/
    README.md
    PROJECT_STATUS_*.md
    PROGRESS_LOG.md
    DECISION_LOG.md
    RESEARCH_VALUE_NOTE.md

  scripts/
    validate_seed_cards.py
    validate_training_records.py
    summarize_results.py
```


## v0.2.9-dev6.2 notable review files

```text
PROJECT_STATUS.md
07_quality_control/PUBLIC_REVIEW_CHECKLIST.md
07_quality_control/OWNER_REVIEW_CHECKLIST_v0.3.0.md
07_quality_control/POLISH_QC_v0.2.9-dev6.2.md
```


## v0.2.9-dev8 source materials

```text
10_source_materials/
  SOURCE_LEDGER.md
  SOURCE_LEDGER.json
  TRAINING_CODE_INVENTORY.md
  TRAINING_CODE_SOURCE_MAP.md
  AIWF_force_multiplier_insert.md
  AIWF_Project_Chat_Distribution_Roadmap/
```


## v0.2.9-dev11 brand/citation polish

```text
01_strategy/BRAND_AND_POSITIONING_GUIDE.md
00_landing_page/PUBLIC_SUMMARY_DRAFT.md
10_source_materials/CITATION_STYLE_GUIDE.md
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
lora_training_lab/                         # removable training/install lab
RAG_HANDOFF_GUIDE.md                       # what to remove for RAG handoff
03_lane_system/vol1_canonical_research_lanes/
11_incoming_user_updates/                  # uploaded source material
```
