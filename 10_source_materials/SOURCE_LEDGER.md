# Source Ledger

Status: active source ledger  
Version added: v0.2.9-dev8  
Date: 2026-05-22

## Purpose

This file makes the repo's source base explicit.

It separates:

```text
project source material
training code
official external technical references
visual assets
quality-control outputs
```

## Source policy

AI assistants are drafting aids, not sources.

Do not cite assistant output as evidence.

Valid evidence sources are:

- primary papers;
- official documentation;
- official repositories/model cards;
- measured local experiment outputs;
- project-authored source materials clearly marked as internal/source documents.

## User-provided source materials added

- `10_source_materials/AIWF_force_multiplier_insert.md`
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap`

## Official external training references

### Hugging Face TRL SFTTrainer

- URL: `https://huggingface.co/docs/trl/main/en/sft_trainer`
- Type: official_documentation
- Verification: verified_url_opened_2026-05-22
- Used for:
  - SFTTrainer support
  - conversational messages dataset format
  - assistant_only_loss
  - packing
  - PEFT adapter training through SFTTrainer

### Hugging Face PEFT LoRAConfig

- URL: `https://huggingface.co/docs/peft/main/en/package_reference/lora`
- Type: official_documentation
- Verification: verified_url_opened_2026-05-22
- Used for:
  - LoRA rank r
  - lora_alpha
  - lora_dropout
  - target_modules
  - task_type

### Hugging Face Transformers bitsandbytes quantization

- URL: `https://huggingface.co/docs/transformers/main/en/quantization/bitsandbytes`
- Type: official_documentation
- Verification: verified_url_opened_2026-05-22
- Used for:
  - 4-bit quantization
  - NF4
  - double quantization
  - BitsAndBytesConfig

### Hugging Face Transformers Trainer

- URL: `https://huggingface.co/docs/transformers/main_classes/trainer`
- Type: official_documentation
- Verification: verified_url_opened_2026-05-22
- Used for:
  - training arguments concepts
  - gradient accumulation
  - gradient checkpointing
  - logging/eval/save cadence

## Repo source categories

### atlas_contract

- `02_atlas_contracts/ATLAS_CONTRACT_NAMING.md` (6012 bytes)
- `02_atlas_contracts/ATLAS_CONTRACT_SCHEMA_V1.json` (1278 bytes)
- `02_atlas_contracts/README.md` (175 bytes)
- `02_atlas_contracts/atlas-contract_mini_128L-12C-5D_v1.json` (885 bytes)

### evaluation_design

- `05_evaluation/BASELINE_MATRIX.md` (1000 bytes)
- `05_evaluation/EVALUATION_PLAN.md` (1189 bytes)
- `05_evaluation/GOLDEN_QUESTIONS_SEED.jsonl` (2040 bytes)
- `05_evaluation/GOLDEN_QUESTIONS_SMOKE_25.jsonl` (5039 bytes)
- `05_evaluation/README.md` (550 bytes)
- `05_evaluation/RESULTS_TEMPLATE.csv` (227 bytes)
- `05_evaluation/RUBRIC.md` (1742 bytes)
- `05_evaluation/SMOKE_RESULTS_TEMPLATE.csv` (160 bytes)
- `05_evaluation/SMOKE_TRAIN_PROTOCOL.md` (2273 bytes)
- `05_evaluation/SMOKE_TRAIN_RESULTS_REPORT_TEMPLATE.md` (828 bytes)
- `05_evaluation/sample_smoke_results.csv` (10060 bytes)

### lane_card_source

- `03_lane_system/README.md` (227 bytes)
- `03_lane_system/atlas-lane-validation/ATLAS_128_LANE_TARGET.csv` (16788 bytes)
- `03_lane_system/atlas-lane-validation/ATLAS_128_LANE_TARGET.md` (3991 bytes)
- `03_lane_system/atlas-lane-validation/CARD_TARGET_PLAN.md` (5949 bytes)
- `03_lane_system/atlas-lane-validation/LANE_VALIDATION_SCHEMA.json` (2559 bytes)
- `03_lane_system/atlas-lane-validation/LANE_VALIDATION_WORKFLOW.md` (2164 bytes)
- `03_lane_system/atlas-lane-validation/PRETRAINING_GATE.md` (2744 bytes)
- `03_lane_system/atlas-lane-validation/atlas_128_lane_target.json` (34454 bytes)
- `03_lane_system/lanes/36_retrieval_card_authoring/ANSWER_PATTERNS.md` (176 bytes)
- `03_lane_system/lanes/36_retrieval_card_authoring/CANONICAL_OVERVIEW.md` (583 bytes)
- `03_lane_system/lanes/36_retrieval_card_authoring/CONCEPT_MAP.md` (459 bytes)
- `03_lane_system/lanes/36_retrieval_card_authoring/DO_NOT_CONFUSE_WITH.md` (122 bytes)
- `03_lane_system/lanes/36_retrieval_card_authoring/FAILURE_SIGNATURES.md` (201 bytes)
- `03_lane_system/lanes/36_retrieval_card_authoring/GAP_AUDIT_AND_VOL2_QUEUE.md` (456 bytes)
- `03_lane_system/lanes/36_retrieval_card_authoring/QA_TEST_PROMPTS.md` (179 bytes)
- `03_lane_system/lanes/36_retrieval_card_authoring/RETRIEVAL_CARDS.jsonl` (10274 bytes)
- `03_lane_system/lanes/36_retrieval_card_authoring/SOURCE_COVERAGE.md` (362 bytes)
- `03_lane_system/lanes/36_retrieval_card_authoring/lane_profile.json` (275 bytes)
- `03_lane_system/lanes/37_small_model_retrieval_optimization/ANSWER_PATTERNS.md` (169 bytes)
- `03_lane_system/lanes/37_small_model_retrieval_optimization/CANONICAL_OVERVIEW.md` (664 bytes)
- `03_lane_system/lanes/37_small_model_retrieval_optimization/CONCEPT_MAP.md` (415 bytes)
- `03_lane_system/lanes/37_small_model_retrieval_optimization/DO_NOT_CONFUSE_WITH.md` (143 bytes)
- `03_lane_system/lanes/37_small_model_retrieval_optimization/FAILURE_SIGNATURES.md` (150 bytes)
- `03_lane_system/lanes/37_small_model_retrieval_optimization/GAP_AUDIT_AND_VOL2_QUEUE.md` (467 bytes)
- `03_lane_system/lanes/37_small_model_retrieval_optimization/QA_TEST_PROMPTS.md` (157 bytes)
- `03_lane_system/lanes/37_small_model_retrieval_optimization/RETRIEVAL_CARDS.jsonl` (11233 bytes)
- `03_lane_system/lanes/37_small_model_retrieval_optimization/SOURCE_COVERAGE.md` (406 bytes)
- `03_lane_system/lanes/37_small_model_retrieval_optimization/lane_profile.json` (263 bytes)
- `03_lane_system/lanes/38_windows_ai_workstation_setup/ANSWER_PATTERNS.md` (170 bytes)
- `03_lane_system/lanes/38_windows_ai_workstation_setup/CANONICAL_OVERVIEW.md` (609 bytes)
- `03_lane_system/lanes/38_windows_ai_workstation_setup/CONCEPT_MAP.md` (488 bytes)
- `03_lane_system/lanes/38_windows_ai_workstation_setup/DO_NOT_CONFUSE_WITH.md` (109 bytes)
- `03_lane_system/lanes/38_windows_ai_workstation_setup/FAILURE_SIGNATURES.md` (195 bytes)
- `03_lane_system/lanes/38_windows_ai_workstation_setup/GAP_AUDIT_AND_VOL2_QUEUE.md` (542 bytes)
- `03_lane_system/lanes/38_windows_ai_workstation_setup/QA_TEST_PROMPTS.md` (196 bytes)
- `03_lane_system/lanes/38_windows_ai_workstation_setup/RETRIEVAL_CARDS.jsonl` (10518 bytes)
- `03_lane_system/lanes/38_windows_ai_workstation_setup/SOURCE_COVERAGE.md` (344 bytes)
- `03_lane_system/lanes/38_windows_ai_workstation_setup/lane_profile.json` (251 bytes)
- `03_lane_system/lanes/39_cuda_torch_runtime_alignment/ANSWER_PATTERNS.md` (216 bytes)
- `03_lane_system/lanes/39_cuda_torch_runtime_alignment/CANONICAL_OVERVIEW.md` (617 bytes)
- `03_lane_system/lanes/39_cuda_torch_runtime_alignment/CONCEPT_MAP.md` (528 bytes)
- `03_lane_system/lanes/39_cuda_torch_runtime_alignment/DO_NOT_CONFUSE_WITH.md` (124 bytes)
- `03_lane_system/lanes/39_cuda_torch_runtime_alignment/FAILURE_SIGNATURES.md` (151 bytes)
- `03_lane_system/lanes/39_cuda_torch_runtime_alignment/GAP_AUDIT_AND_VOL2_QUEUE.md` (548 bytes)
- `03_lane_system/lanes/39_cuda_torch_runtime_alignment/QA_TEST_PROMPTS.md` (172 bytes)
- `03_lane_system/lanes/39_cuda_torch_runtime_alignment/RETRIEVAL_CARDS.jsonl` (9988 bytes)
- `03_lane_system/lanes/39_cuda_torch_runtime_alignment/SOURCE_COVERAGE.md` (371 bytes)
- `03_lane_system/lanes/39_cuda_torch_runtime_alignment/lane_profile.json` (257 bytes)
- `03_lane_system/lanes/40_model_folder_architecture/ANSWER_PATTERNS.md` (151 bytes)
- `03_lane_system/lanes/40_model_folder_architecture/CANONICAL_OVERVIEW.md` (598 bytes)
- `03_lane_system/lanes/40_model_folder_architecture/CONCEPT_MAP.md` (463 bytes)
- `03_lane_system/lanes/40_model_folder_architecture/DO_NOT_CONFUSE_WITH.md` (122 bytes)
- `03_lane_system/lanes/40_model_folder_architecture/FAILURE_SIGNATURES.md` (150 bytes)
- `03_lane_system/lanes/40_model_folder_architecture/GAP_AUDIT_AND_VOL2_QUEUE.md` (539 bytes)
- `03_lane_system/lanes/40_model_folder_architecture/QA_TEST_PROMPTS.md` (159 bytes)
- `03_lane_system/lanes/40_model_folder_architecture/RETRIEVAL_CARDS.jsonl` (9735 bytes)
- `03_lane_system/lanes/40_model_folder_architecture/SOURCE_COVERAGE.md` (361 bytes)
- `03_lane_system/lanes/40_model_folder_architecture/lane_profile.json` (245 bytes)
- `03_lane_system/lanes/41_comfyui_workflow_repair/ANSWER_PATTERNS.md` (147 bytes)
- `03_lane_system/lanes/41_comfyui_workflow_repair/CANONICAL_OVERVIEW.md` (665 bytes)
- `03_lane_system/lanes/41_comfyui_workflow_repair/CONCEPT_MAP.md` (456 bytes)
- `03_lane_system/lanes/41_comfyui_workflow_repair/DO_NOT_CONFUSE_WITH.md` (116 bytes)
- `03_lane_system/lanes/41_comfyui_workflow_repair/FAILURE_SIGNATURES.md` (152 bytes)
- `03_lane_system/lanes/41_comfyui_workflow_repair/GAP_AUDIT_AND_VOL2_QUEUE.md` (456 bytes)
- `03_lane_system/lanes/41_comfyui_workflow_repair/QA_TEST_PROMPTS.md` (194 bytes)
- `03_lane_system/lanes/41_comfyui_workflow_repair/RETRIEVAL_CARDS.jsonl` (10774 bytes)
- `03_lane_system/lanes/41_comfyui_workflow_repair/SOURCE_COVERAGE.md` (378 bytes)
- `03_lane_system/lanes/41_comfyui_workflow_repair/lane_profile.json` (241 bytes)
- `03_lane_system/lanes/42_comfyui_socket_contract_debugging/ANSWER_PATTERNS.md` (181 bytes)
- `03_lane_system/lanes/42_comfyui_socket_contract_debugging/CANONICAL_OVERVIEW.md` (590 bytes)
- `03_lane_system/lanes/42_comfyui_socket_contract_debugging/CONCEPT_MAP.md` (548 bytes)
- `03_lane_system/lanes/42_comfyui_socket_contract_debugging/DO_NOT_CONFUSE_WITH.md` (134 bytes)
- `03_lane_system/lanes/42_comfyui_socket_contract_debugging/FAILURE_SIGNATURES.md` (157 bytes)
- `03_lane_system/lanes/42_comfyui_socket_contract_debugging/GAP_AUDIT_AND_VOL2_QUEUE.md` (465 bytes)
- `03_lane_system/lanes/42_comfyui_socket_contract_debugging/QA_TEST_PROMPTS.md` (214 bytes)
- `03_lane_system/lanes/42_comfyui_socket_contract_debugging/RETRIEVAL_CARDS.jsonl` (10471 bytes)
- `03_lane_system/lanes/42_comfyui_socket_contract_debugging/SOURCE_COVERAGE.md` (404 bytes)
- `03_lane_system/lanes/42_comfyui_socket_contract_debugging/lane_profile.json` (293 bytes)
- `03_lane_system/lanes/43_inpainting_fundamentals/ANSWER_PATTERNS.md` (151 bytes)
- `03_lane_system/lanes/43_inpainting_fundamentals/CANONICAL_OVERVIEW.md` (571 bytes)
- `03_lane_system/lanes/43_inpainting_fundamentals/CONCEPT_MAP.md` (481 bytes)
- `03_lane_system/lanes/43_inpainting_fundamentals/DO_NOT_CONFUSE_WITH.md` (96 bytes)
- `03_lane_system/lanes/43_inpainting_fundamentals/FAILURE_SIGNATURES.md` (155 bytes)
- `03_lane_system/lanes/43_inpainting_fundamentals/GAP_AUDIT_AND_VOL2_QUEUE.md` (537 bytes)
- `03_lane_system/lanes/43_inpainting_fundamentals/QA_TEST_PROMPTS.md` (185 bytes)
- `03_lane_system/lanes/43_inpainting_fundamentals/RETRIEVAL_CARDS.jsonl` (9984 bytes)
- `03_lane_system/lanes/43_inpainting_fundamentals/SOURCE_COVERAGE.md` (345 bytes)
- `03_lane_system/lanes/43_inpainting_fundamentals/lane_profile.json` (241 bytes)
- `03_lane_system/lanes/44_video_vram_optimization/ANSWER_PATTERNS.md` (139 bytes)
- `03_lane_system/lanes/44_video_vram_optimization/CANONICAL_OVERVIEW.md` (604 bytes)
- `03_lane_system/lanes/44_video_vram_optimization/CONCEPT_MAP.md` (533 bytes)
- `03_lane_system/lanes/44_video_vram_optimization/DO_NOT_CONFUSE_WITH.md` (112 bytes)
- `03_lane_system/lanes/44_video_vram_optimization/FAILURE_SIGNATURES.md` (148 bytes)
- `03_lane_system/lanes/44_video_vram_optimization/GAP_AUDIT_AND_VOL2_QUEUE.md` (455 bytes)
- `03_lane_system/lanes/44_video_vram_optimization/QA_TEST_PROMPTS.md` (212 bytes)
- `03_lane_system/lanes/44_video_vram_optimization/RETRIEVAL_CARDS.jsonl` (9873 bytes)
- `03_lane_system/lanes/44_video_vram_optimization/SOURCE_COVERAGE.md` (413 bytes)
- `03_lane_system/lanes/44_video_vram_optimization/lane_profile.json` (273 bytes)
- `03_lane_system/lanes/45_last_frame_chaining_video_extension/ANSWER_PATTERNS.md` (149 bytes)
- `03_lane_system/lanes/45_last_frame_chaining_video_extension/CANONICAL_OVERVIEW.md` (687 bytes)
- `03_lane_system/lanes/45_last_frame_chaining_video_extension/CONCEPT_MAP.md` (482 bytes)
- `03_lane_system/lanes/45_last_frame_chaining_video_extension/DO_NOT_CONFUSE_WITH.md` (106 bytes)
- `03_lane_system/lanes/45_last_frame_chaining_video_extension/FAILURE_SIGNATURES.md` (113 bytes)
- `03_lane_system/lanes/45_last_frame_chaining_video_extension/GAP_AUDIT_AND_VOL2_QUEUE.md` (472 bytes)
- `03_lane_system/lanes/45_last_frame_chaining_video_extension/QA_TEST_PROMPTS.md` (139 bytes)
- `03_lane_system/lanes/45_last_frame_chaining_video_extension/RETRIEVAL_CARDS.jsonl` (11094 bytes)
- `03_lane_system/lanes/45_last_frame_chaining_video_extension/SOURCE_COVERAGE.md` (411 bytes)
- `03_lane_system/lanes/45_last_frame_chaining_video_extension/lane_profile.json` (269 bytes)
- `03_lane_system/lanes/46_gradio_multi_venv_orchestration/ANSWER_PATTERNS.md` (183 bytes)
- `03_lane_system/lanes/46_gradio_multi_venv_orchestration/CANONICAL_OVERVIEW.md` (608 bytes)
- `03_lane_system/lanes/46_gradio_multi_venv_orchestration/CONCEPT_MAP.md` (470 bytes)
- `03_lane_system/lanes/46_gradio_multi_venv_orchestration/DO_NOT_CONFUSE_WITH.md` (105 bytes)
- `03_lane_system/lanes/46_gradio_multi_venv_orchestration/FAILURE_SIGNATURES.md` (165 bytes)
- `03_lane_system/lanes/46_gradio_multi_venv_orchestration/GAP_AUDIT_AND_VOL2_QUEUE.md` (545 bytes)
- `03_lane_system/lanes/46_gradio_multi_venv_orchestration/QA_TEST_PROMPTS.md` (191 bytes)
- `03_lane_system/lanes/46_gradio_multi_venv_orchestration/RETRIEVAL_CARDS.jsonl` (10118 bytes)
- `03_lane_system/lanes/46_gradio_multi_venv_orchestration/SOURCE_COVERAGE.md` (335 bytes)
- `03_lane_system/lanes/46_gradio_multi_venv_orchestration/lane_profile.json` (257 bytes)
- `03_lane_system/lanes/47_raw_rag_vs_atlas_comparison/ANSWER_PATTERNS.md` (132 bytes)
- `03_lane_system/lanes/47_raw_rag_vs_atlas_comparison/CANONICAL_OVERVIEW.md` (602 bytes)
- `03_lane_system/lanes/47_raw_rag_vs_atlas_comparison/CONCEPT_MAP.md` (423 bytes)
- `03_lane_system/lanes/47_raw_rag_vs_atlas_comparison/DO_NOT_CONFUSE_WITH.md` (86 bytes)
- `03_lane_system/lanes/47_raw_rag_vs_atlas_comparison/FAILURE_SIGNATURES.md` (126 bytes)
- `03_lane_system/lanes/47_raw_rag_vs_atlas_comparison/GAP_AUDIT_AND_VOL2_QUEUE.md` (541 bytes)
- `03_lane_system/lanes/47_raw_rag_vs_atlas_comparison/QA_TEST_PROMPTS.md` (173 bytes)
- `03_lane_system/lanes/47_raw_rag_vs_atlas_comparison/RETRIEVAL_CARDS.jsonl` (9403 bytes)
- `03_lane_system/lanes/47_raw_rag_vs_atlas_comparison/SOURCE_COVERAGE.md` (323 bytes)
- `03_lane_system/lanes/47_raw_rag_vs_atlas_comparison/lane_profile.json` (249 bytes)
- `03_lane_system/lanes/48_small_vs_large_model_benchmarking/ANSWER_PATTERNS.md` (152 bytes)
- `03_lane_system/lanes/48_small_vs_large_model_benchmarking/CANONICAL_OVERVIEW.md` (627 bytes)
- `03_lane_system/lanes/48_small_vs_large_model_benchmarking/CONCEPT_MAP.md` (450 bytes)
- `03_lane_system/lanes/48_small_vs_large_model_benchmarking/DO_NOT_CONFUSE_WITH.md` (97 bytes)
- `03_lane_system/lanes/48_small_vs_large_model_benchmarking/FAILURE_SIGNATURES.md` (163 bytes)
- `03_lane_system/lanes/48_small_vs_large_model_benchmarking/GAP_AUDIT_AND_VOL2_QUEUE.md` (550 bytes)
- `03_lane_system/lanes/48_small_vs_large_model_benchmarking/QA_TEST_PROMPTS.md` (139 bytes)
- `03_lane_system/lanes/48_small_vs_large_model_benchmarking/RETRIEVAL_CARDS.jsonl` (9511 bytes)
- `03_lane_system/lanes/48_small_vs_large_model_benchmarking/SOURCE_COVERAGE.md` (332 bytes)
- `03_lane_system/lanes/48_small_vs_large_model_benchmarking/lane_profile.json` (266 bytes)
- `03_lane_system/lanes/49_aiwf_core_philosophy/ANSWER_PATTERNS.md` (126 bytes)
- `03_lane_system/lanes/49_aiwf_core_philosophy/CANONICAL_OVERVIEW.md` (610 bytes)
- `03_lane_system/lanes/49_aiwf_core_philosophy/CONCEPT_MAP.md` (439 bytes)
- `03_lane_system/lanes/49_aiwf_core_philosophy/DO_NOT_CONFUSE_WITH.md` (84 bytes)
- `03_lane_system/lanes/49_aiwf_core_philosophy/FAILURE_SIGNATURES.md` (153 bytes)
- `03_lane_system/lanes/49_aiwf_core_philosophy/GAP_AUDIT_AND_VOL2_QUEUE.md` (537 bytes)
- `03_lane_system/lanes/49_aiwf_core_philosophy/QA_TEST_PROMPTS.md` (199 bytes)
- `03_lane_system/lanes/49_aiwf_core_philosophy/RETRIEVAL_CARDS.jsonl` (8986 bytes)
- `03_lane_system/lanes/49_aiwf_core_philosophy/SOURCE_COVERAGE.md` (319 bytes)
- `03_lane_system/lanes/49_aiwf_core_philosophy/lane_profile.json` (240 bytes)
- `03_lane_system/lanes/50_diagram_visual_asset_system/ANSWER_PATTERNS.md` (157 bytes)
- `03_lane_system/lanes/50_diagram_visual_asset_system/CANONICAL_OVERVIEW.md` (634 bytes)
- `03_lane_system/lanes/50_diagram_visual_asset_system/CONCEPT_MAP.md` (438 bytes)
- `03_lane_system/lanes/50_diagram_visual_asset_system/DO_NOT_CONFUSE_WITH.md` (93 bytes)
- `03_lane_system/lanes/50_diagram_visual_asset_system/FAILURE_SIGNATURES.md` (143 bytes)
- `03_lane_system/lanes/50_diagram_visual_asset_system/GAP_AUDIT_AND_VOL2_QUEUE.md` (548 bytes)
- `03_lane_system/lanes/50_diagram_visual_asset_system/QA_TEST_PROMPTS.md` (185 bytes)
- `03_lane_system/lanes/50_diagram_visual_asset_system/RETRIEVAL_CARDS.jsonl` (9254 bytes)
- `03_lane_system/lanes/50_diagram_visual_asset_system/SOURCE_COVERAGE.md` (365 bytes)
- `03_lane_system/lanes/50_diagram_visual_asset_system/lane_profile.json` (258 bytes)
- `03_lane_system/lanes/51_atlas_lane_design_system/ANSWER_PATTERNS.md` (157 bytes)
- `03_lane_system/lanes/51_atlas_lane_design_system/CANONICAL_OVERVIEW.md` (467 bytes)
- `03_lane_system/lanes/51_atlas_lane_design_system/CONCEPT_MAP.md` (470 bytes)
- `03_lane_system/lanes/51_atlas_lane_design_system/DO_NOT_CONFUSE_WITH.md` (96 bytes)
- `03_lane_system/lanes/51_atlas_lane_design_system/FAILURE_SIGNATURES.md` (128 bytes)
- `03_lane_system/lanes/51_atlas_lane_design_system/GAP_AUDIT_AND_VOL2_QUEUE.md` (499 bytes)
- `03_lane_system/lanes/51_atlas_lane_design_system/QA_TEST_PROMPTS.md` (143 bytes)
- `03_lane_system/lanes/51_atlas_lane_design_system/RETRIEVAL_CARDS.jsonl` (10084 bytes)
- `03_lane_system/lanes/51_atlas_lane_design_system/SOURCE_COVERAGE.md` (362 bytes)
- `03_lane_system/lanes/51_atlas_lane_design_system/lane_profile.json` (248 bytes)
- `03_lane_system/lanes/52_source_ledger_maintenance/ANSWER_PATTERNS.md` (125 bytes)
- `03_lane_system/lanes/52_source_ledger_maintenance/CANONICAL_OVERVIEW.md` (484 bytes)
- `03_lane_system/lanes/52_source_ledger_maintenance/CONCEPT_MAP.md` (450 bytes)
- `03_lane_system/lanes/52_source_ledger_maintenance/DO_NOT_CONFUSE_WITH.md` (89 bytes)
- `03_lane_system/lanes/52_source_ledger_maintenance/FAILURE_SIGNATURES.md` (120 bytes)
- `03_lane_system/lanes/52_source_ledger_maintenance/GAP_AUDIT_AND_VOL2_QUEUE.md` (500 bytes)
- `03_lane_system/lanes/52_source_ledger_maintenance/QA_TEST_PROMPTS.md` (182 bytes)
- `03_lane_system/lanes/52_source_ledger_maintenance/RETRIEVAL_CARDS.jsonl` (10039 bytes)
- `03_lane_system/lanes/52_source_ledger_maintenance/SOURCE_COVERAGE.md` (336 bytes)
- `03_lane_system/lanes/52_source_ledger_maintenance/lane_profile.json` (250 bytes)
- `03_lane_system/lanes/53_claim_freshness_verification/ANSWER_PATTERNS.md` (133 bytes)
- `03_lane_system/lanes/53_claim_freshness_verification/CANONICAL_OVERVIEW.md` (492 bytes)
- `03_lane_system/lanes/53_claim_freshness_verification/CONCEPT_MAP.md` (505 bytes)
- `03_lane_system/lanes/53_claim_freshness_verification/DO_NOT_CONFUSE_WITH.md` (100 bytes)
- `03_lane_system/lanes/53_claim_freshness_verification/FAILURE_SIGNATURES.md` (155 bytes)
- `03_lane_system/lanes/53_claim_freshness_verification/GAP_AUDIT_AND_VOL2_QUEUE.md` (507 bytes)
- `03_lane_system/lanes/53_claim_freshness_verification/QA_TEST_PROMPTS.md` (188 bytes)
- `03_lane_system/lanes/53_claim_freshness_verification/RETRIEVAL_CARDS.jsonl` (10074 bytes)
- `03_lane_system/lanes/53_claim_freshness_verification/SOURCE_COVERAGE.md` (342 bytes)
- `03_lane_system/lanes/53_claim_freshness_verification/lane_profile.json` (260 bytes)

### quality_control

- `07_quality_control/GITHUB_STRUCTURE_QC_v0.2.7.md` (645 bytes)
- `07_quality_control/OWNER_REVIEW_CHECKLIST_v0.3.0.md` (1076 bytes)
- `07_quality_control/POLISH_QC_v0.2.9-dev6.2.md` (824 bytes)
- `07_quality_control/PUBLIC_REVIEW_CHECKLIST.md` (1802 bytes)
- `07_quality_control/QC_REPORT_v0.2.6.md` (8743 bytes)
- `07_quality_control/QC_SUMMARY_v0.2.6.json` (2177 bytes)
- `07_quality_control/README.md` (134 bytes)
- `07_quality_control/RELATED_WORK_AND_SMOKE_PROTOCOL_QC_v0.2.9-dev5.md` (2342 bytes)
- `07_quality_control/RUNNABLE_TRAINING_LAYER_QC_v0.2.9-dev7.md` (1066 bytes)
- `07_quality_control/SEED_LANE_GROWTH_QC_v0.2.8.md` (1457 bytes)
- `07_quality_control/SEED_LANE_GROWTH_QC_v0.2.9-dev1.md` (496 bytes)
- `07_quality_control/SEED_LANE_GROWTH_QC_v0.2.9-dev2.md` (567 bytes)
- `07_quality_control/SEED_LANE_GROWTH_QC_v0.2.9.md` (642 bytes)
- `07_quality_control/SOURCE_POLICY_QC_v0.2.9-dev5-clean.md` (917 bytes)
- `07_quality_control/TRAINING_LAYER_QC_REPORT_v0.2.9-dev4.md` (9694 bytes)
- `07_quality_control/TRAINING_PLAN_QC_v0.2.9-dev3.md` (982 bytes)
- `07_quality_control/TRAINING_RESEARCH_MATRIX_QC_v0.2.9-dev6.md` (926 bytes)
- `07_quality_control/v0.3_OWNER_REVIEW_PACKET.md` (1107 bytes)
- `07_quality_control/v0.3_OWNER_REVIEW_REMINDER_v0.2.9.md` (534 bytes)

### repo_root_or_other

- `00_landing_page/LANDING_PAGE_COPY.md` (3412 bytes)
- `00_landing_page/LANDING_PAGE_PLAIN_TEXT.txt` (3312 bytes)
- `00_landing_page/README.md` (191 bytes)
- `06_experiments/EXPERIMENT_LOG.csv` (104 bytes)
- `06_experiments/EXPERIMENT_TEMPLATE.md` (691 bytes)
- `06_experiments/README.md` (242 bytes)
- `CHANGELOG.md` (11325 bytes)
- `DIRECTORY_MAP.md` (2371 bytes)
- `GITHUB_UPLOAD_NOTES.md` (853 bytes)
- `HUMAN_RELEASE_APPROVAL_GATE.md` (2349 bytes)
- `LICENSE_NOTICE.md` (478 bytes)
- `MANIFEST.json` (22881 bytes)
- `MILESTONES.md` (10508 bytes)
- `PROJECT_STATUS.md` (571 bytes)
- `README.md` (4340 bytes)
- `RELEASE_GATES.md` (2490 bytes)
- `REPO_NAVIGATION.md` (1841 bytes)
- `ROADMAP.md` (9160 bytes)
- `VERSIONING_POLICY.md` (4198 bytes)
- `requirements.txt` (32 bytes)

### research_note

- `09_research_notes/DECISION_LOG.md` (892 bytes)
- `09_research_notes/PROGRESS_LOG.md` (1197 bytes)
- `09_research_notes/PROJECT_STATUS_v0.2.1.md` (801 bytes)
- `09_research_notes/PROJECT_STATUS_v0.2.2.md` (838 bytes)
- `09_research_notes/PROJECT_STATUS_v0.2.3.md` (736 bytes)
- `09_research_notes/PROJECT_STATUS_v0.2.4.md` (634 bytes)
- `09_research_notes/PROJECT_STATUS_v0.2.5.md` (671 bytes)
- `09_research_notes/PROJECT_STATUS_v0.2.6.md` (610 bytes)
- `09_research_notes/PROJECT_STATUS_v0.2.7.md` (951 bytes)
- `09_research_notes/PROJECT_STATUS_v0.2.8.md` (618 bytes)
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev1.md` (494 bytes)
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev2.md` (367 bytes)
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev3.md` (727 bytes)
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev4.md` (718 bytes)
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev5-clean.md` (610 bytes)
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev5.md` (534 bytes)
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev6.1.md` (465 bytes)
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev6.2.md` (527 bytes)
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev6.md` (504 bytes)
- `09_research_notes/PROJECT_STATUS_v0.2.9-dev7.md` (619 bytes)
- `09_research_notes/PROJECT_STATUS_v0.2.9.md` (446 bytes)
- `09_research_notes/README.md` (183 bytes)
- `09_research_notes/RESEARCH_VALUE_NOTE.md` (1451 bytes)

### strategy_and_claim_governance

- `01_strategy/ARCHITECTURE_OVERVIEW.md` (1364 bytes)
- `01_strategy/ATLAS_READER_LORA_STRATEGY.md` (22704 bytes)
- `01_strategy/CLAIMS_AND_LIMITS.md` (1349 bytes)
- `01_strategy/README.md` (206 bytes)
- `01_strategy/RELATED_WORK.md` (9654 bytes)
- `01_strategy/SMALL_MODEL_ATLAS_READER_MODE.md` (2690 bytes)
- `01_strategy/SOURCE_AND_ATTRIBUTION_POLICY.md` (1425 bytes)
- `01_strategy/STANDARD_RAG_VS_ATLAS_RAG.md` (1377 bytes)
- `01_strategy/TERMINOLOGY.md` (1108 bytes)

### training_config

- `06_experiments/training_configs/A_sanity_r8_lr0001.json` (1303 bytes)
- `06_experiments/training_configs/B_baseline_r16_lr0002.json` (1397 bytes)
- `06_experiments/training_configs/C_capacity_r32_lr0001.json` (1397 bytes)
- `06_experiments/training_configs/D_stability_r32_lr00005.json` (1400 bytes)
- `06_experiments/training_configs/E_nodrop_r16_lr0002.json` (1392 bytes)
- `06_experiments/training_configs/F_context4096_r16.json` (1389 bytes)
- `06_experiments/training_configs/G_rank64_stress.json` (1386 bytes)
- `06_experiments/training_configs/H_packing_efficiency.json` (1394 bytes)
- `06_experiments/training_configs/README.md` (714 bytes)

### training_data_design

- `04_training_data/ATLAS_CARD_SCHEMA_V1.json` (1583 bytes)
- `04_training_data/ATLAS_CARD_TEMPLATE.json` (1435 bytes)
- `04_training_data/ATLAS_SFT_FORMATTING_GUIDE.md` (1051 bytes)
- `04_training_data/CONTEXT_PACK_DESIGN.md` (2040 bytes)
- `04_training_data/CONTEXT_PACK_SCHEMA_V1.json` (1867 bytes)
- `04_training_data/DATASET_BUILD_PIPELINE.md` (1903 bytes)
- `04_training_data/DATASET_BUILD_PLAN.md` (1049 bytes)
- `04_training_data/DATASET_CARD_TEMPLATE.md` (903 bytes)
- `04_training_data/MANUAL_TRAINING_DATA_REVIEW_CHECKLIST.md` (1366 bytes)
- `04_training_data/NEGATIVE_EXAMPLES_AND_DISTRACTORS.md` (1733 bytes)
- `04_training_data/OVERNIGHT_TRAINING_RUN_MATRIX.md` (3305 bytes)
- `04_training_data/README.md` (754 bytes)
- `04_training_data/RUNNABLE_TRAINING_LAYER.md` (2241 bytes)
- `04_training_data/SAMPLE_ATLAS_READER_MINI_RECORDS.jsonl` (88371 bytes)
- `04_training_data/SAMPLE_RECORDS.jsonl` (10130 bytes)
- `04_training_data/SAMPLE_RECORDS_STATUS.md` (1195 bytes)
- `04_training_data/SMOKE_TRAINING_RUN_PLAN.md` (1308 bytes)
- `04_training_data/TRAINING_DATA_RISK_REGISTER.md` (1217 bytes)
- `04_training_data/TRAINING_DATA_SCHEMA.json` (3299 bytes)
- `04_training_data/TRAINING_EXAMPLE_TYPES.md` (1053 bytes)
- `04_training_data/TRAINING_PLAN_ATLAS_READER_MINI.md` (5694 bytes)
- `04_training_data/TRAINING_RECORD_QUALITY_GATES.md` (2934 bytes)
- `04_training_data/TRAINING_RECORD_SCHEMA_V1.json` (4521 bytes)
- `04_training_data/TRAINING_RESEARCH_NOTES_v0.2.9-dev6.md` (3584 bytes)
- `04_training_data/generated_seed_training_records.jsonl` (68889 bytes)

### training_or_repo_code

- `requirements-training.txt` (305 bytes)
- `scripts/__pycache__/compute_significance.cpython-313.pyc` (7276 bytes)
- `scripts/__pycache__/create_train_eval_split.cpython-313.pyc` (3452 bytes)
- `scripts/__pycache__/render_atlas_sft_dataset.cpython-313.pyc` (5081 bytes)
- `scripts/__pycache__/train_atlas_reader_qlora.cpython-313.pyc` (21423 bytes)
- `scripts/build_seed_training_records.py` (4088 bytes)
- `scripts/check_training_record_quality.py` (2899 bytes)
- `scripts/compute_significance.py` (3080 bytes)
- `scripts/create_train_eval_split.py` (1767 bytes)
- `scripts/render_atlas_sft_dataset.py` (2993 bytes)
- `scripts/summarize_results.py` (1570 bytes)
- `scripts/train_atlas_reader_qlora.py` (15226 bytes)
- `scripts/validate_seed_cards.py` (3900 bytes)
- `scripts/validate_training_records.py` (3398 bytes)
- `tools/powershell/dry_run_training_config.ps1` (278 bytes)
- `tools/powershell/train_atlas_reader.ps1` (251 bytes)

### user_provided_source_material

- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/AI_FIELD_GUIDE_AGENT_PLAN.md` (1317 bytes)
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/CHANGELOG.md` (1103 bytes)
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/CHAT_HANDOFFS/01_brand_hub_chat.md` (2824 bytes)
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/CHAT_HANDOFFS/02_envpack_workstation_validator_chat.md` (3579 bytes)
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/CHAT_HANDOFFS/03_model_checker_chat.md` (3403 bytes)
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/CHAT_HANDOFFS/04_field_manual_chat.md` (3919 bytes)
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/CHAT_HANDOFFS/05_knowledge_pack_assistant_chat.md` (3063 bytes)
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/CHAT_HANDOFFS/06_workflow_packs_chat.md` (3413 bytes)
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/CHAT_HANDOFFS/07_comfyui_nodes_chat.md` (3343 bytes)
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/CHAT_HANDOFFS/08_old_photo_restore_chat.md` (3335 bytes)
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/CHAT_HANDOFFS/09_qwenvl_vqa_llm_nodes_chat.md` (3483 bytes)
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/CHAT_HANDOFFS/10_aiwf_photos_chat.md` (3119 bytes)
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/CHAT_HANDOFFS/11_labs_preservation_bridge_chat.md` (3386 bytes)
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/CHAT_HANDOFFS/12_release_packaging_chat.md` (3267 bytes)
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/CHAT_SCOPE_FIREWALL.md` (1588 bytes)
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/CROSS_CHAT_CHECKLIST.md` (2127 bytes)
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/MASTER_DISTRIBUTION_ROADMAP.md` (7397 bytes)
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/PROJECT_CHAT_MAP.md` (4036 bytes)
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/README.md` (1347 bytes)
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap/AIWF-Project-Chat-Distribution-Roadmap/SENDOFF_MASTER.md` (2184 bytes)
- `10_source_materials/AIWF_force_multiplier_insert.md` (3361 bytes)

### visual_asset

- `08_visuals/ATLAS_ROUTING_FLOWCHART_OVERVIEW.png` (1026374 bytes)
- `08_visuals/ATLAS_ROUTING_SYSTEM_FLOWCHART_OVERVIEW.png` (1108293 bytes)
- `08_visuals/ATLAS_SYSTEM_OVERVIEW_DIAGRAM.md` (594 bytes)
- `08_visuals/ATLAS_SYSTEM_OVERVIEW_DIAGRAM.png` (1700968 bytes)
- `08_visuals/DIAGRAM_INDEX.md` (641 bytes)
- `08_visuals/README.md` (398 bytes)



## v0.2.9-dev9 citation layer

Source inventory is not enough by itself.

The repo now includes direct citation files:

```text
10_source_materials/SOURCE_CITATIONS.md
10_source_materials/CITATION_MATRIX.md
10_source_materials/CITATION_REGISTRY.json
10_source_materials/REFERENCES.bib
```

Use these citation keys in public-facing claims and training-code documentation.
