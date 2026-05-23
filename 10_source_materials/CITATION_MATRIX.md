# Citation Matrix

Status: active citation map  
Version added: v0.2.9-dev9  
Date: 2026-05-22

## Purpose

This file maps project claims and training-code choices to the source that should be cited.

## Related-work claims

| Claim | Cite |
|---|---|
| Retrieval-aware fine-tuning and distractor-aware RAG training are prior art. | `zhang2024raft` |
| LoRA fine-tuning to improve RAG citation/answer accuracy is prior art. | `devine2025aloftrag` |
| Structure-aware retrieval is prior art. | `xu2025rdr2` |
| LoRA adapter routing / parametric RAG is adjacent prior art. | `su2025polyprag` |
| RAG + LoRA adapter retuning for hallucination/factuality control is adjacent prior art. | `dwivedi2025autoraglora` |
| LoRA rank and domain robustness are valid variables to test. | `rathore2025lora_rank` |
| Retrieval-based LoRA adapter composition is adjacent prior art. | `adsul2026taskaware_lora` |

## Training-code claims

| Code/design choice | Cite |
|---|---|
| SFTTrainer supports supervised fine-tuning and conversational `messages` format. | `hf_trl_sfttrainer` |
| `assistant_only_loss=True` for conversational datasets. | `hf_trl_sfttrainer` |
| `packing=True` for efficiency tests. | `hf_trl_sfttrainer` |
| PEFT adapter training via `peft_config=LoraConfig()`. | `hf_trl_sfttrainer`, `hf_peft_loraconfig` |
| LoRA rank `r`, alpha, dropout, target modules, bias, task type. | `hf_peft_loraconfig`, `hu2021lora` |
| 4-bit QLoRA, NF4, double quantization. | `dettmers2023qlora`, `hf_transformers_bitsandbytes` |
| Gradient accumulation and checkpointing settings. | `hf_transformers_trainer` |

## Atlas-specific claims

| Atlas claim | Cite |
|---|---|
| Atlas Reader LoRA is not claiming a new LoRA algorithm. | Project README / Related Work + `hu2021lora` |
| Atlas Reader LoRA is not claiming retrieval-aware fine-tuning as new. | Project README / Related Work + `zhang2024raft`, `devine2025aloftrag` |
| Atlas Reader LoRA's candidate contribution is the content-agnostic reading adapter + versioned contract + small-model card budget. | Project README / Related Work |
| Whether the adapter works must be decided by measured evaluation. | Project smoke protocol / evaluation reports |


## v0.2.9-dev10 conversation-source audit additions

| Conversation source / concept | Citation key | Status |
|---|---|---|
| Foundational RAG / external knowledge retrieval | `lewis2020rag` | Added |
| Self-RAG / retrieve-generate-critique behavior | `asai2023selfrag` | Added |
| RAPTOR / tree-organized retrieval | `sarthi2024raptor` | Added |
| Microsoft GraphRAG paper / graph-structured retrieval | `edge2024graphrag` | Added |
| Knowledge-graph / GNN-RAG adjacent work | `mavromatis2024gnnrag` | Added |
| Hugging Face Datasets dependency | `hf_datasets_docs` | Added |
| Hugging Face Accelerate dependency | `hf_accelerate_docs` | Added |
| Safetensors dependency | `hf_safetensors_docs` | Added |
| SuperAnnotate blog mention | not cited | Excluded from core claims; industry commentary only |
| SitePoint blog mention | not cited | Excluded from core claims; industry commentary only |
| AI assistant / drafting conversation | not cited | Explicitly excluded by source policy |


## v0.2.9-dev12 TensorBoard dashboard

| Claim / feature | Cite |
|---|---|
| TensorBoard provides ML workflow measurement and visualization. | `tensorboard_get_started` |
| TensorBoard Scalars/Time Series can track loss, metrics, training speed, and learning rate. | `tensorboard_get_started` |
| Hugging Face Trainer can log to TensorBoard through TensorBoardCallback. | `hf_transformers_callbacks` |
| `TENSORBOARD_LOGGING_DIR` / output-dir based TensorBoard logging behavior exists. | `hf_transformers_callbacks` |

## v0.2.9-dev13 statistical-methods citations

The smoke-protocol significance script (`scripts/compute_significance.py`) and
the evaluation protocol (`05_evaluation/SMOKE_TRAIN_PROTOCOL.md`) use established
statistical tests. These are now cited.

| Statistical method | Where used | Cite |
|---|---|---|
| McNemar's test (paired binary pass/fail, A3 vs A2) | `compute_significance.py`, smoke protocol | `mcnemar1947` |
| Wilcoxon signed-rank test (paired ordinal rubric scores) | `compute_significance.py`, smoke protocol | `wilcoxon1945` |
| Cliff's delta (ordinal effect size) | `compute_significance.py`, smoke protocol | `cliff1993` |
| Paired bootstrap confidence interval | `compute_significance.py`, smoke protocol | `efron1993bootstrap` |


## v0.2.9-dev14 lab installer

| Claim / feature | Cite |
|---|---|
| PyTorch latest stable requires Python 3.10 or later. | `pytorch_get_started` |
| PyTorch on Windows supports Python 3.10-3.14. | `pytorch_get_started` |
| CUDA PyTorch installs should use the platform-appropriate PyTorch wheel index. | `pytorch_get_started` |
| CUDA visibility can be checked with `torch.cuda.is_available()`. | `pytorch_get_started` |


## v0.2.9-dev15 labinstall QC

| Claim / feature | Cite |
|---|---|
| bitsandbytes requires Python >= 3.10 and PyTorch >= 2.4. | `hf_bitsandbytes_install` |
| bitsandbytes supports NVIDIA CUDA and NF4/FP4 quantization. | `hf_bitsandbytes_install` |
| bitsandbytes lists Windows x86-64 CUDA wheel support. | `hf_bitsandbytes_install` |


## v0.2.9-dev19 agent protocol lane

| Claim / feature | Cite |
|---|---|
| Codex can use AGENTS.md as project instructions. | `openai_codex_agents_md` |
| Codex supports repo-level and layered instruction files. | `openai_codex_agents_md` |
| Codex plugins use `.codex-plugin/plugin.json`. | `openai_codex_plugins_build` |
| Codex plugins can include skills via `skills/<skill>/SKILL.md`. | `openai_codex_plugins_build` |
| Repo marketplaces can expose local plugins via `.agents/plugins/marketplace.json`. | `openai_codex_plugins_build` |
| Codex command rules are experimental and should be treated cautiously. | `openai_codex_rules` |
| Agent workflows should be evaluated rather than assumed effective. | `openai_agent_evals` |
