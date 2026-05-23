# Source Citations

Status: active citation registry  
Version updated: v0.2.9-dev10  
Date: 2026-05-22

## Rule

This file lists the sources that should be cited in project docs.

AI assistants are not sources.

Use these sources for claims about prior art, LoRA/QLoRA mechanics, structured RAG, training-code APIs, and evaluation framing. Keep the tone factual: citations support claims; they do not prove Atlas Reader LoRA works.

## Citation list

| Key | Source | Use |
|---|---|---|
| `adsul2026taskaware_lora` | [Task-Aware LoRA Adapter Composition via Similarity Retrieval in Vector Databases](https://arxiv.org/abs/2602.21222) | Retrieval-based LoRA adapter composition/routing is related work.; Atlas Reader should distinguish corpus/card routing from adapter-bank routing. |
| `asai2023selfrag` | [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://arxiv.org/abs/2310.11511) | Training models to retrieve, critique, and reflect on retrieved evidence is prior art.; Insufficient-context and critique-style behavior are related prior art. |
| `dettmers2023qlora` | [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) | QLoRA trains adapters through 4-bit quantized frozen models.; NF4, double quantization, and memory-efficient fine-tuning are prior art. |
| `devine2025aloftrag` | [ALoFTRAG: Automatic Local Fine Tuning for Retrieval Augmented Generation](https://arxiv.org/abs/2501.11929) | LoRA fine-tuning to improve RAG citation/answer accuracy is prior art.; Synthetic data generation/filtering for RAG fine-tuning is prior art. |
| `dwivedi2025autoraglora` | [AutoRAG-LoRA: Hallucination-Triggered Knowledge Retuning via Lightweight Adapters](https://arxiv.org/abs/2507.10586) | RAG + LoRA adapter retuning for hallucination/factuality control is related work.; Atlas Reader LoRA should state its contribution as contract/interface discipline, not adapter retuning generally. |
| `edge2024graphrag` | [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130) | GraphRAG / graph-structured retrieval is prior art.; Atlas should not claim structured or graph-like RAG as new. |
| `hf_accelerate_docs` | [Hugging Face Accelerate documentation](https://huggingface.co/docs/accelerate/index) | Accelerate is a training dependency used under Hugging Face training stacks.; Hardware/device orchestration should cite official docs when discussed. |
| `hf_datasets_docs` | [Hugging Face Datasets documentation](https://huggingface.co/docs/datasets/index) | Dataset loading and Dataset object usage in training scripts.; The training script's use of Hugging Face Datasets should cite official docs. |
| `hf_peft_loraconfig` | [PEFT LoRA documentation](https://huggingface.co/docs/peft/main/en/package_reference/lora) | LoraConfig parameters: r, target_modules, lora_alpha, lora_dropout, bias, task_type.; LoRA config examples used by the training templates. |
| `hf_safetensors_docs` | [Safetensors documentation](https://huggingface.co/docs/safetensors/index) | Safetensors is included in training requirements.; Adapter/model serialization claims should cite official docs when discussed. |
| `hf_transformers_bitsandbytes` | [Transformers bitsandbytes quantization documentation](https://huggingface.co/docs/transformers/main/en/quantization/bitsandbytes) | BitsAndBytesConfig.; 4-bit quantization.; NF4 for training 4-bit base models.; Nested/double quantization. |
| `hf_transformers_trainer` | [Transformers Trainer documentation](https://huggingface.co/docs/transformers/main_classes/trainer) | Gradient accumulation.; Gradient checkpointing.; Training arguments and stability settings. |
| `hf_trl_sfttrainer` | [TRL SFT Trainer documentation](https://huggingface.co/docs/trl/main/en/sft_trainer) | SFTTrainer usage.; Conversational messages dataset format.; packing=True.; assistant_only_loss=True.; PEFT adapter training through SFTTrainer. |
| `hu2021lora` | [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) | LoRA freezes base model weights and trains low-rank adapter matrices.; Atlas Reader LoRA uses LoRA as mechanism, not invention. |
| `lewis2020rag` | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | RAG itself is prior art.; Atlas Reader LoRA should not claim retrieval-augmented generation as new.; RAG keeps knowledge external to the model while generation uses retrieved context. |
| `mavromatis2024gnnrag` | [GNN-RAG: Graph Neural Retrieval for Large Language Model Reasoning](https://arxiv.org/abs/2405.20139) | Knowledge-graph / graph-neural retrieval for RAG is related prior art.; Graph-based retrieval and reasoning are not novel to Atlas. |
| `rathore2025_lora_rank` | [How Much is Too Much? Exploring LoRA Rank Trade-offs for Retaining Knowledge and Domain Robustness](https://arxiv.org/abs/2512.15634) | Alias key retained because earlier related-work draft used this spelling.; LoRA rank affects downstream performance and robustness.; Cross-domain/robustness questions are legitimate to evaluate rather than assume. |
| `rathore2025lora_rank` | [How Much is Too Much? Exploring LoRA Rank Trade-offs for Retaining Knowledge and Domain Robustness](https://arxiv.org/abs/2512.15634) | LoRA rank affects downstream performance and robustness.; Cross-domain/robustness questions are legitimate to evaluate rather than assume. |
| `sarthi2024raptor` | [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://arxiv.org/abs/2401.18059) | Tree-organized / hierarchical retrieval is prior art.; Atlas lanes/cards should be positioned as a structured interface, not the first hierarchical retrieval system. |
| `su2025polyprag` | [Parametric Retrieval-Augmented Generation using Latent Routing of LoRA Adapters](https://arxiv.org/abs/2511.17044) | LoRA adapter routing / parametric RAG is related prior art.; Atlas lane routing should be framed as content-level protocol, not new adapter routing algorithm. |
| `xu2025rdr2` | [Equipping Retrieval-Augmented Large Language Models with Document Structure Awareness](https://arxiv.org/abs/2510.04293) | Structure-aware retrieval is prior art.; Atlas lanes/cards should be framed as a structured-RAG cousin, not a new structured-RAG invention. |
| `zhang2024raft` | [RAFT: Adapting Language Model to Domain Specific RAG](https://arxiv.org/abs/2403.10131) | Retrieval-aware fine-tuning is prior art.; Distractor-aware RAG training is prior art.; Atlas Reader LoRA should not claim retrieval-aware fine-tuning as new. |


## Citation use map

### Baseline RAG / structured retrieval prior art

Use:

```text
lewis2020rag
edge2024graphrag
sarthi2024raptor
mavromatis2024gnnrag
xu2025rdr2
asai2023selfrag
```

### Retrieval-aware fine-tuning / RAG + LoRA prior art

Use:

```text
zhang2024raft
devine2025aloftrag
dwivedi2025autoraglora
su2025polyprag
adsul2026taskaware_lora
```

### LoRA / QLoRA mechanics

Use:

```text
hu2021lora
dettmers2023qlora
rathore2025_lora_rank
hf_peft_loraconfig
hf_transformers_bitsandbytes
```

### Training code / implementation docs

Use:

```text
hf_trl_sfttrainer
hf_peft_loraconfig
hf_transformers_bitsandbytes
hf_transformers_trainer
hf_datasets_docs
hf_accelerate_docs
hf_safetensors_docs
```

## Important

The presence of a citation does not prove Atlas Reader LoRA works.

Performance proof still requires measured outputs from the smoke protocol.


## Style note

Use citation keys consistently in prose.

Example:

```text
Retrieval-aware fine-tuning is prior art [zhang2024raft], and LoRA itself is prior art [hu2021lora]. Atlas Reader LoRA's candidate contribution is the versioned Atlas contract and content-agnostic reading protocol, not a new adapter algorithm.
```


## v0.2.9-dev12 TensorBoard dashboard citations

| Key | Source | Use |
|---|---|---|
| `tensorboard_get_started` | [Get started with TensorBoard](https://www.tensorflow.org/tensorboard/get_started) | TensorBoard dashboard, scalar metrics, launching with logdir |
| `hf_transformers_callbacks` | [Transformers Callbacks documentation](https://huggingface.co/docs/transformers/main_classes/callback) | TensorBoardCallback and Trainer log integration |


## v0.2.9-dev14 lab installer citation

| Key | Source | Use |
|---|---|---|
| `pytorch_get_started` | [PyTorch Get Started Locally](https://pytorch.org/get-started/locally/) | Python 3.10+ support, Windows pip install guidance, CUDA wheel indexes, CUDA verification |


## v0.2.9-dev15 labinstall QC citation

| Key | Source | Use |
|---|---|---|
| `hf_bitsandbytes_install` | [bitsandbytes Installation Guide](https://huggingface.co/docs/bitsandbytes/main/en/installation) | bitsandbytes Python/PyTorch requirements, Windows CUDA wheel support, pip install guidance |


## v0.2.9-dev19 agent protocol citations

| Key | Source | Use |
|---|---|---|
| `openai_codex_agents_md` | [Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md) | AGENTS.md as repo/project guidance for Codex |
| `openai_codex_plugins_build` | [Build plugins](https://developers.openai.com/codex/plugins/build) | Codex plugin skeleton, plugin manifest, skills, repo marketplace |
| `openai_codex_rules` | [Rules](https://developers.openai.com/codex/rules) | Codex rules, command policy, experimental caveat |
| `openai_agent_evals` | [Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals) | Treating agent protocol as an evaluation arm |
