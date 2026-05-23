## v0.2.9-dev21 upload prep — 2026-05-23

Prepared the Atlas Reader LoRA package for a normal public GitHub upload without
claiming training results.

Changed:

- added `.gitignore` rules for runtime artifacts, model weights, local secrets,
  preserved incoming payloads, private handoff material, and forensic Git
  history;
- refreshed README, project status, navigation, roadmap, release gates, and
  milestone notes to point training/install material at `lora_training_lab/`;
- displayed all three project diagrams in the GitHub-facing README and public
  landing draft;
- marked the incoming visual-source archive as local-only so the public visuals
  folder stays focused on the three project diagrams;
- regenerated `MANIFEST.json` for the public upload shape, excluding local-only
  archive payloads while keeping the LoRA training lab;
- verified seed-card validation, training-record schema validation, and
  labinstall static QC;
- left the quality checker warning intact because the 21 records are scaffold
  examples, not production SFT data.

Still true:

- no adapter has been trained;
- no evaluation win is claimed;
- no Git repo has been initialized in this folder without owner approval.

## v0.2.9-dev13 — 2026-05-23

### Review pass + statistical-methods citation gap closed

External review of the dev12 training + TensorBoard layer. Findings and fixes:

**Verified sound (no change needed):**
- `scripts/train_atlas_reader_qlora.py` — runnable, defensive (dry-run before
  heavy imports, version-tolerant kwargs filtering, runtime+git capture).
  Dry-run validated on real seed data (18 records, atlas_record shape detected).
- Citation infrastructure (SOURCE_LEDGER, CITATION_MATRIX, CITATION_REGISTRY,
  REFERENCES.bib) confirmed thorough: 23 source entries covering RAFT, QLoRA,
  LoRA, RAG, Self-RAG, RAPTOR, GraphRAG, and the HF official docs the training
  code is based on.
- SOURCE_AND_ATTRIBUTION_POLICY confirmed: AI-assistant output correctly
  excluded as a citable source.

**Gap found and fixed — statistical methods were uncited:**
- `compute_significance.py` and `SMOKE_TRAIN_PROTOCOL.md` use McNemar,
  Wilcoxon signed-rank, Cliff's delta, and paired bootstrap CI with no method
  citations.
- Added 4 references to REFERENCES.bib: mcnemar1947, wilcoxon1945, cliff1993,
  efron1993bootstrap (now 27 total bib entries).
- Registered them in CITATION_MATRIX.md (new dev13 section).
- Added a cited methods header to compute_significance.py at point of use.

**Note on the snapshot filename:** the zip is labeled "tensorboard-dashboard"
but EXPERIMENT_LOG.csv is empty (headers only) and no tfevents run files exist.
This is the training + TensorBoard *scaffolding*, not training *results*. That
is correct for the project's current pre-training phase — flagged here only so
the status is unambiguous.

# Changelog

## 2026-05-22 — Phase 2 testing/documentation scaffold

Added:

- `ROADMAP.md`
- expanded `README.md`
- full `ATLAS_READER_LORA_STRATEGY.md`
- `strategy/` docs
- `training/` schema, examples, and dataset plan
- `evaluation/` rubric, baseline matrix, golden-question seed, and results template
- `experiments/` templates
- `scripts/validate_training_records.py`
- `scripts/summarize_results.py`
- `research-notes/DECISION_LOG.md`
- `research-notes/RESEARCH_VALUE_NOTE.md`

Purpose:

- move from concept naming to testable research scaffold;
- preserve useful positive and negative results;
- prepare the repo for training-data generation and baseline testing.

## Phase 3 — 2026-05-22

Added the 128-lane Atlas validation gate as a pretraining requirement for Atlas Reader LoRA.

New files:

- `atlas-lane-validation/ATLAS_128_LANE_TARGET.md`
- `atlas-lane-validation/ATLAS_128_LANE_TARGET.csv`
- `atlas-lane-validation/atlas_128_lane_target.json`
- `atlas-lane-validation/LANE_VALIDATION_SCHEMA.json`
- `atlas-lane-validation/LANE_VALIDATION_WORKFLOW.md`
- `atlas-lane-validation/PRETRAINING_GATE.md`

Purpose: make lane expansion part of the adapter-efficiency strategy. The LoRA should learn structured-RAG reading behavior across 128 validated lanes before serious training claims are made.

## Phase 4 — Landing Page Copy — 2026-05-22

Added dedicated landing-page copy explaining Atlas Reader LoRA for non-technical readers.

New files:

- `landing-page/LANDING_PAGE_COPY.md`
- `landing-page/LANDING_PAGE_PLAIN_TEXT.txt`

Purpose: preserve the neural-network/lane/map explanation as the public-facing project introduction.

## Phase 5 — 12-Card Small-Model Baseline — 2026-05-22

Locked the first serious Atlas Reader LoRA card target:

```text
128 lanes x 12 cards per lane = 1,536 validated cards
```

Added small-model-first design guidance for `.8B` to `4B` models.

New files:

- `atlas-lane-validation/CARD_TARGET_PLAN.md`
- `strategy/SMALL_MODEL_ATLAS_READER_MODE.md`
- `training/ATLAS_CARD_SCHEMA_V1.json`
- `training/ATLAS_CARD_TEMPLATE.json`

Purpose: avoid overbuilding the card network before proof. Larger 24-card or 32-card lane variants are deferred until the 12-card baseline demonstrates value.

## Phase 6 — Atlas Contract Naming — 2026-05-22

Added formal adapter naming and Atlas Contract files.

New files:

- `strategy/ATLAS_CONTRACT_NAMING.md`
- `strategy/ATLAS_CONTRACT_SCHEMA_V1.json`
- `strategy/atlas-contract_mini_128L-12C-5D_v1.json`

Baseline adapter name:

```text
atlas-reader-mini_qwen3-4b_128L-12C-5D_v1
```

Purpose: make every LoRA name show the base model, lane count, cards per lane, retrieval depth, and version.

## v0.2.1 — Planning Version Correction — 2026-05-22

Corrected project maturity language.

This repository is still in the v0.2 planning track: the concept, roadmap, Atlas contract, lane/card target, and evaluation approach are defined, but no trained model exists yet.

Added:

- `VERSIONING_POLICY.md`
- `RELEASE_GATES.md`

Policy update:

- avoid unnecessary phase/version inflation;
- use patch versions for small documentation/schema changes;
- reserve v1.0 for the first trained adapter experiment with posted results;
- treat good, bad, and mixed results as valid research outcomes if documented honestly.

## v0.2.2 — Milestone Roadmap — 2026-05-22

Added explicit milestone gates for v0.3 through v1.0.

New file:

- `MILESTONES.md`

Updated:

- `ROADMAP.md`
- `RELEASE_GATES.md`
- `MANIFEST.json`

Purpose: keep the project on task by defining what must exist before advancing each version.

## v0.2.3 — Human Release Approval Gate — 2026-05-22

Added owner-controlled milestone promotion policy.

New file:

- `HUMAN_RELEASE_APPROVAL_GATE.md`

Updated:

- `README.md`
- `VERSIONING_POLICY.md`
- `RELEASE_GATES.md`
- `MILESTONES.md`
- `MANIFEST.json`

Policy:

No AI assistant, automation, or external reviewer may promote the project from an `x.x.9` release to the next `.0` milestone without explicit approval from Shawn O'Hagan.

## v0.2.4 — Diagram and Seed Lanes — 2026-05-22

Added:

- `visuals/ATLAS_SYSTEM_OVERVIEW_DIAGRAM.png`
- `visuals/ATLAS_SYSTEM_OVERVIEW_DIAGRAM.md`
- `lanes/36_retrieval_card_authoring/*`
- `lanes/42_comfyui_socket_contract_debugging/*`
- `lanes/44_video_vram_optimization/*`
- `research-notes/PROJECT_STATUS_v0.2.4.md`

Summary:

- 3 seed lanes started
- 36 seed cards added
- diagram archived into the repo package

This remains v0.2.x seed work and does not promote the project to v0.3.

## v0.2.5 — Six Seed Lanes — 2026-05-22

Added 3 more seed lanes:

- `lanes/37_small_model_retrieval_optimization/*`
- `lanes/41_comfyui_workflow_repair/*`
- `lanes/45_last_frame_chaining_video_extension/*`

Seed totals:

```text
6 seed lanes
72 seed cards
```

This remains v0.2.x seed-build work. Promotion to v0.3 requires owner approval.

## v0.2.6 — Seed Lane Quality Control — 2026-05-22

Added QC report and validation script.

New files:

- `quality-control/QC_REPORT_v0.2.6.md`
- `quality-control/QC_SUMMARY_v0.2.6.json`
- `quality-control/v0.3_OWNER_REVIEW_PACKET.md`
- `scripts/validate_seed_cards.py`
- `research-notes/PROJECT_STATUS_v0.2.6.md`

Result:

```text
6 seed lanes
72 seed cards
0 blocking schema issues
ready_for_owner_review
```

This does not promote the project to v0.3. Owner approval is required.

## v0.2.7 — GitHub Navigation Structure — 2026-05-22

Organized the archive structure for GitHub and easier navigation.

Added:

- `REPO_NAVIGATION.md`
- `DIRECTORY_MAP.md`
- `GITHUB_UPLOAD_NOTES.md`
- README files inside numbered major folders
- `09_research_notes/PROJECT_STATUS_v0.2.7.md`

Moved/organized:

- strategy docs into `01_strategy/`
- contract docs into `02_atlas_contracts/`
- lanes into `03_lane_system/lanes/`
- lane validation docs into `03_lane_system/atlas-lane-validation/`
- training docs into `04_training_data/`
- evaluation docs into `05_evaluation/`
- QC artifacts into `07_quality_control/`
- visuals into `08_visuals/`
- research notes into `09_research_notes/`

Updated:

- `scripts/validate_seed_cards.py` now points to `03_lane_system/lanes/`.

This remains v0.2.x organization work and does not promote the project to v0.3.

## v0.2.8 — Infrastructure Seed Lanes — 2026-05-22

Added 3 infrastructure seed lanes:

- `03_lane_system/lanes/38_windows_ai_workstation_setup/`
- `03_lane_system/lanes/39_cuda_torch_runtime_alignment/`
- `03_lane_system/lanes/40_model_folder_architecture/`

Current seed totals:

```text
9 seed lanes
108 seed cards
```

Added QC file:

- `07_quality_control/SEED_LANE_GROWTH_QC_v0.2.8.md`

This remains v0.2.x seed-build work and does not promote the project to v0.3.

## v0.2.9 — Expanded Seed Lanes — 2026-05-22

Added 3 seed lanes:

- `03_lane_system/lanes/43_inpainting_fundamentals/`
- `03_lane_system/lanes/46_gradio_multi_venv_orchestration/`
- `03_lane_system/lanes/47_raw_rag_vs_atlas_comparison/`

Current seed totals:

```text
12 seed lanes
144 seed cards
```

Added QC file:

- `07_quality_control/SEED_LANE_GROWTH_QC_v0.2.9.md`

This remains v0.2.x work. Promotion to v0.3.0 requires owner approval.

## v0.2.9-dev1 — Continued Seed Build — 2026-05-22

Added 3 seed lanes while staying below the v0.3 approval gate:

- `03_lane_system/lanes/48_small_vs_large_model_benchmarking/`
- `03_lane_system/lanes/49_aiwf_core_philosophy/`
- `03_lane_system/lanes/50_diagram_visual_asset_system/`

Current seed totals:

```text
15 seed lanes
180 seed cards
```

This is not a v0.3.0 promotion.

## v0.2.9-dev2 — Atlas Governance Seed Lanes — 2026-05-22

Added 3 seed lanes while staying below the v0.3 approval gate:

- `03_lane_system/lanes/51_atlas_lane_design_system/`
- `03_lane_system/lanes/52_source_ledger_maintenance/`
- `03_lane_system/lanes/53_claim_freshness_verification/`

Current seed totals:

```text
18 seed lanes
216 seed cards
```

This is not a v0.3.0 promotion.

## v0.2.9-dev3 — Training Plan and Schemas — 2026-05-22

Added Atlas Reader Mini training-plan assets:

- `04_training_data/TRAINING_PLAN_ATLAS_READER_MINI.md`
- `04_training_data/CONTEXT_PACK_SCHEMA_V1.json`
- `04_training_data/TRAINING_RECORD_SCHEMA_V1.json`
- `04_training_data/CONTEXT_PACK_DESIGN.md`
- `04_training_data/DATASET_BUILD_PIPELINE.md`
- `04_training_data/NEGATIVE_EXAMPLES_AND_DISTRACTORS.md`
- `04_training_data/SMOKE_TRAINING_RUN_PLAN.md`
- `04_training_data/SAMPLE_ATLAS_READER_MINI_RECORDS.jsonl`
- `scripts/build_seed_training_records.py`
- `scripts/validate_training_records.py`
- `07_quality_control/TRAINING_PLAN_QC_v0.2.9-dev3.md`
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev3.md`

Sample training records added:

```text
21
```

This is not a training run and not a v0.3.0 promotion.

## v0.2.9-dev4 — Training Layer QC — 2026-05-22

Added training-layer QC and stricter quality gates.

New files:

- `04_training_data/TRAINING_RECORD_QUALITY_GATES.md`
- `04_training_data/SAMPLE_RECORDS_STATUS.md`
- `04_training_data/TRAINING_DATA_RISK_REGISTER.md`
- `04_training_data/MANUAL_TRAINING_DATA_REVIEW_CHECKLIST.md`
- `scripts/check_training_record_quality.py`
- `07_quality_control/TRAINING_LAYER_QC_REPORT_v0.2.9-dev4.md`
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev4.md`

QC result:

```text
sample records parsed: 21
structural issues: 0
training_ready: false
```

The sample records are schema-valid scaffolds, not final SFT-quality training records.

This is not a v0.3.0 promotion.

## v0.2.9-dev5 — Related Work and Smoke Protocol — 2026-05-22

Added related-work positioning and smoke-evaluation protocol.

Script test:

```text
compute_significance.py return code: 0
```

This is not a v0.3.0 promotion and not a training result.

## v0.2.9-dev5-clean — Source Policy Correction — 2026-05-22

Added source-attribution policy and clarified that AI assistants are not valid research sources.

Added:

- `01_strategy/SOURCE_AND_ATTRIBUTION_POLICY.md`
- `07_quality_control/SOURCE_POLICY_QC_v0.2.9-dev5-clean.md`
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev5-clean.md`

Updated:

- `01_strategy/RELATED_WORK.md`

This is not a v0.3.0 promotion.

## v0.2.9-dev6 — Training Research Matrix — 2026-05-22

Added training research notes, overnight run matrix, SFT formatting guide, config templates, and renderer script.

This is not a v0.3.0 promotion and not a training result.

## v0.2.9-dev6.1 — All Three Diagrams — 2026-05-22

Added the two missing diagram PNGs to `08_visuals/` and created `08_visuals/DIAGRAM_INDEX.md`.

This is a package-content correction, not a milestone promotion.
## v0.2.9-dev6.2 — GitHub/Public Review Polish — 2026-05-22

Polished the package for easier review.

Updated:

- `README.md`
- `REPO_NAVIGATION.md`
- `08_visuals/DIAGRAM_INDEX.md`
- `MANIFEST.json`

Added:

- `PROJECT_STATUS.md`
- `07_quality_control/PUBLIC_REVIEW_CHECKLIST.md`
- `07_quality_control/OWNER_REVIEW_CHECKLIST_v0.3.0.md`
- `07_quality_control/POLISH_QC_v0.2.9-dev6.2.md`
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev6.2.md`

This is a polish package, not a v0.3.0 promotion.

## v0.2.9-dev7 — Runnable Training Layer — 2026-05-22

Added runnable TRL/PEFT QLoRA training script, split helper, requirements file, PowerShell helpers, and QC compile report.

This is not a v0.3.0 promotion and not a training result.

## v0.2.9-dev8 — Source Ledger and Training-Code Inventory — 2026-05-22

Added source-ledger and training-code inventory.

New files:

- `10_source_materials/SOURCE_LEDGER.md`
- `10_source_materials/SOURCE_LEDGER.json`
- `10_source_materials/TRAINING_CODE_INVENTORY.md`
- `10_source_materials/TRAINING_CODE_SOURCE_MAP.md`
- `scripts/build_source_inventory.py`
- `07_quality_control/SOURCE_LEDGER_TRAINING_CODE_QC_v0.2.9-dev8.md`
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev8.md`

This is not a v0.3.0 promotion and not a training result.

## v0.2.9-dev9 — Cited Sources — 2026-05-22

Added direct citation registry, citation matrix, and BibTeX references.

New files:

- `10_source_materials/SOURCE_CITATIONS.md`
- `10_source_materials/CITATION_MATRIX.md`
- `10_source_materials/CITATION_REGISTRY.json`
- `10_source_materials/REFERENCES.bib`
- `07_quality_control/SOURCE_CITATION_QC_v0.2.9-dev9.md`
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev9.md`

This is not a v0.3.0 promotion and not a training result.

## v0.2.9-dev10 — Conversation Source Audit — 2026-05-22

Reviewed the conversation for cited/mentioned sources and expanded citation coverage.

Added:

- `10_source_materials/CONVERSATION_SOURCE_AUDIT.md`
- `07_quality_control/CONVERSATION_SOURCE_AUDIT_QC_v0.2.9-dev10.md`
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev10.md`

Updated citation registry, citation matrix, BibTeX, related work, and training docs.

This is not a v0.3.0 promotion and not a training result.

## v0.2.9-dev11 — Brand and Citation Polish — 2026-05-22

Added brand/positioning and citation-style polish.

New files:

- `01_strategy/BRAND_AND_POSITIONING_GUIDE.md`
- `00_landing_page/PUBLIC_SUMMARY_DRAFT.md`
- `10_source_materials/CITATION_STYLE_GUIDE.md`
- `07_quality_control/BRAND_CITATION_POLISH_QC_v0.2.9-dev11.md`
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev11.md`

This is not a v0.3.0 promotion and not a training result.

## v0.2.9-dev12 — TensorBoard Dashboard — 2026-05-22

Added TensorBoard dashboard support for training metrics.

This is not a v0.3.0 promotion and not a training result.

## v0.2.9-dev14 — Lab Install — 2026-05-22

Added Windows Python 3.10 lab installer, smoke test, install guide, and PyTorch install citation.

This is not a v0.3.0 promotion and not a training result.

## v0.2.9-dev15 — Lab Install QC — 2026-05-22

Hardened labinstall, improved TensorBoard launcher, updated bitsandbytes requirement, added installer static QC, and added bitsandbytes install citation.

This is not a v0.3.0 promotion and not a training result.

## v0.2.9-dev16 — AIWF Branding — 2026-05-22

Added AI Without Fear branding layer.

New files:

- `01_strategy/AIWF_BRAND_SYSTEM.md`
- `00_landing_page/AIWF_ATLAS_READER_LANDING_DRAFT.md`
- `00_landing_page/AIWF_README_HEADER_SNIPPET.md`
- `08_visuals/AIWF_VISUAL_BRANDING_NOTES.md`
- `07_quality_control/AIWF_BRANDING_QC_v0.2.9-dev16.md`
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev16.md`

This is not a v0.3.0 promotion and not a training result.

## v0.2.9-dev17 — No-Wins Pre-Install QC — 2026-05-22

Added strict pre-install/no-results guardrails.

New files:

- `PROJECT_PREINSTALL_STATUS.md`
- `00_landing_page/NO_WINS_YET_PUBLIC_NOTE.md`
- `07_quality_control/REPORT_TEMPLATE_POLICY.md`
- `07_quality_control/NO_WINS_CLAIM_AUDIT_v0.2.9-dev17.md`
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev17.md`

Report templates were preserved, but explicitly framed as templates rather than results.

This is not a v0.3.0 promotion and not a training result.

## v0.2.9-dev18 — Research Rationale — 2026-05-22

Added a no-hype research rationale around uncertainty, measurement, and useful failure.

New files:

- `01_strategy/RESEARCH_RATIONALE_UNKNOWN_MEANS_INSTRUMENT_IT.md`
- `00_landing_page/UNKNOWN_MEANS_INSTRUMENT_IT.md`
- `05_evaluation/EVALUATION_RATIONALE_USEFUL_FAILURE.md`
- `07_quality_control/RESEARCH_RATIONALE_QC_v0.2.9-dev18.md`
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev18.md`

This is not a v0.3.0 promotion and not a training result.

## v0.2.9-dev19 — Agent Protocol Lane — 2026-05-23

Added an Agent Protocol lane as a smaller part of the Atlas concept.

New files include:

- `AGENTS.md`
- `01_strategy/AGENT_PROTOCOL_LANE.md`
- `05_evaluation/AGENT_ATTACHMENT_LORA_COMPARISON_PLAN.md`
- `00_landing_page/ATLAS_BEFORE_THE_ADAPTER.md`
- `plugins/aiwf-atlas-protocol/`
- `.agents/plugins/marketplace.json`

This is not a v0.3.0 promotion and not a training result.

## v0.2.9-dev20 — Repackage with Training Lab Isolation — 2026-05-23

Repackaged repo so LoRA/training/install material lives under `lora_training_lab/`. Added uploaded AIWF Atlas source material and canonical VOL1 lanes/cards.

Added:

- `lora_training_lab/`
- `RAG_HANDOFF_GUIDE.md`
- `03_lane_system/vol1_canonical_research_lanes/`
- `11_incoming_user_updates/AIWF_ATLAS_uploaded_2026-05-23/`
- `11_incoming_user_updates/AIWF_ATLAS_UPLOAD_MERGE_REPORT.md`
- `07_quality_control/REPACKAGE_QC_v0.2.9-dev20.md`
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev20.md`

This is not a v0.3.0 promotion and not a training result.

## v0.2.9-dev21 — Forensic Git Preservation — 2026-05-23

Preserved the uploaded `.git/` history from `AIWF - ATLAS.zip` under:

```text
11_incoming_user_updates/AIWF_ATLAS_uploaded_2026-05-23_FOR_FORENSIC_WITH_GIT/
```

This is not a v0.3.0 promotion and not a training result.
