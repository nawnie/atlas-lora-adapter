# Conversation Source Audit

Status: source-completeness audit  
Version added: v0.2.9-dev10  
Date: 2026-05-22

## Purpose

The user asked to review the conversation and make sure all sources discussed are cited.

This file records what was included, what was not included, and why.

## Included as citation sources

| Topic/source mentioned in conversation | Citation key | Why included |
|---|---|---|
| Foundational RAG | `lewis2020rag` | Baseline RAG prior art |
| GraphRAG / graph-structured retrieval | `edge2024graphrag` | Structured/graph RAG prior art |
| Knowledge graph / graph-neural RAG | `mavromatis2024gnnrag` | KG/graph-RAG adjacent work |
| RAPTOR / recursive tree retrieval | `sarthi2024raptor` | Hierarchical/tree retrieval prior art |
| Self-RAG | `asai2023selfrag` | Retrieval + critique/reflection prior art |
| RAFT | `zhang2024raft` | Retrieval-aware fine-tuning and distractor training prior art |
| ALoFTRAG | `devine2025aloftrag` | LoRA fine-tuning for RAG accuracy prior art |
| RDR2 / document-structure-aware RAG | `xu2025rdr2` | Document-structure-aware retrieval prior art |
| Poly-PRAG | `su2025polyprag` | Parametric RAG / LoRA routing adjacent work |
| AutoRAG-LoRA | `dwivedi2025autoraglora` | RAG + LoRA hallucination/factuality adjacent work |
| LoRA rank/domain robustness paper | `rathore2025_lora_rank` | Supports testing rank/generalization rather than assuming |
| Task-aware LoRA composition | `adsul2026taskaware_lora` | Adapter-composition adjacent work |
| LoRA paper | `hu2021lora` | Mechanism/source for LoRA itself |
| QLoRA paper | `dettmers2023qlora` | Mechanism/source for 4-bit adapter training |
| TRL SFTTrainer docs | `hf_trl_sfttrainer` | Training implementation source |
| PEFT LoRAConfig docs | `hf_peft_loraconfig` | Training implementation source |
| Transformers bitsandbytes docs | `hf_transformers_bitsandbytes` | 4-bit quantization implementation source |
| Transformers Trainer docs | `hf_transformers_trainer` | Training-arguments implementation source |
| Hugging Face Datasets docs | `hf_datasets_docs` | Dataset object / training-script dependency |
| Hugging Face Accelerate docs | `hf_accelerate_docs` | Training stack dependency |
| Safetensors docs | `hf_safetensors_docs` | Adapter/model serialization dependency |

## Excluded from citations

| Mention | Why excluded |
|---|---|
| Claude / ChatGPT / AI assistant output | Drafting aid only; not evidence |
| SuperAnnotate blog | Industry commentary; not needed for core claim support |
| SitePoint blog | Industry commentary; not needed for core claim support |
| Personal project history / EveryDream timeline comments | User/project context; requires separate verification if published |
| Generic references to 'metadata filtering' and 'parent-document retrieval' | Useful concepts, but not currently load-bearing in the repo claims; can add official LangChain/LlamaIndex citations later if those become core claims |

## Remaining verification queue

Before public release, re-open and verify:

- exact titles;
- author lists;
- publication venues;
- dates;
- citation keys;
- whether any newer work supersedes the related-work framing.

## Bottom line

The repo now has a wider citation system that covers all load-bearing sources discussed in the conversation.

It still correctly excludes AI assistants as sources.
