# Related Work and Positioning

Status: research positioning (v0.2.9-dev5)
Date: 2026-05-22

## Purpose of this document

This file states honestly where the Atlas Reader LoRA sits relative to existing
research. It exists so that any reviewer — technical or not — can see that the
project knows the landscape and is not claiming to have invented things that
already exist.

The short version:

```text
We are not inventing retrieval-aware fine-tuning.
We are proposing a standard interface and a discipline on top of it.
```

Better metaphor than "improving the wheel":

```text
RAFT and similar methods built better wheels (better-trained adapters).
We are proposing a standard axle — a versioned contract that defines how an
adapter mounts onto a structured corpus — so the adapter and the corpus can
evolve independently.
```

---


## Attribution note

This document is a project-authored research-positioning draft. It may have been developed with drafting assistance, but drafting assistance is not a source. The only acceptable public citations are the primary papers, official documentation, official repositories/model cards, and measured project results verified directly.

---

## What already exists (prior art we build on)

These are real, published methods. The Atlas Reader LoRA does not replace them
and should cite them.

### 1. Retrieval-aware fine-tuning (the core mechanism)

Training a model (often via LoRA/QLoRA) to use retrieved context better is
established work.

- RAFT (Retrieval-Augmented Fine-Tuning) [`zhang2024raft`] — trains a model to ignore distractor
  documents and answer from the relevant one.
- ALoFTRAG (Automatic Local Fine-Tuning for RAG, 2025) [`devine2025aloftrag`] — generates and filters
  synthetic training data, then performs LoRA fine-tuning to improve citation
  and answer accuracy on a given domain without manually labeled data. Reported
  average improvements across many datasets and languages.

Implication for us: the *act* of fine-tuning an adapter to read retrieval better
is NOT our contribution. Our `ignore_distractor` and source-priority training
records are in the same family as RAFT-style training.

### 2. Structure-aware retrieval

Giving retrieval explicit structure rather than a flat chunk pile is also
established.

- GraphRAG, knowledge-graph RAG, hierarchical retrieval, RAPTOR-style recursive
  summary trees.
- RDR2 / document-structure-aware RAG [`xu2025rdr2`].

Implication for us: our "lanes → cards → source priority" structure is a cousin
of these. The *idea* that structure beats flat chunks is not ours.

### 3. Adapter routing / composition

Routing between multiple LoRA adapters, or composing them, is an active area.

- Poly-PRAG (2025) [`su2025polyprag`] — uses a small set of LoRA adapters that encode general
  knowledge; each document is encoded through a latent routing function, jointly
  training adapters and the router so each adapter captures shared knowledge
  across documents.
- LoraHub, LoRA-Flow, and task-aware LoRA composition via similarity retrieval [`adsul2026taskaware_lora`] —
  banks of adapters selected/merged at inference time.

Implication for us: routing itself is well-explored. Our lane routing is a
content-level routing protocol, not a new adapter-mixture algorithm.

### 4. Small-model fine-tuning as a 2025-2026 trend

Fine-tuning small language models (roughly the .8B-7B band) became a major
practical trend in 2025-2026, driven by lower VRAM requirements and better
tooling (Unsloth, PEFT, QLoRA). Our `.8B`-`4B` target sits inside this trend.

---

## The evidence that our central bet is reasonable

Our load-bearing hypothesis is that an adapter can learn *transferable reading
behavior* rather than memorize one corpus. Recent evidence supports that this is
at least possible:

- A December 2025 study on LoRA rank trade-offs [`rathore2025_lora_rank`] found that LoRA-tuned models
  trained on one domain and evaluated on another often generalize, sometimes
  improving over the base model (reported cross-domain gains training on one QA
  domain and evaluating on a different one). The authors concluded LoRA was
  "not merely memorizing facts specific to the training domain" but learning
  "more abstract and transferable skills."

This does not prove our adapter will transfer. It means the transfer hypothesis
is credible enough to be worth testing, which is exactly what the cross-corpus transfer experiment is for.

---

## What appears to be unoccupied (our actual contribution)

After reviewing the above, the following combination does not appear to be
filled by existing work. We claim this as our contribution and nothing more.

### Claim 1 — Content-agnostic reading adapter (behavior, not facts)

Existing retrieval-aware fine-tuning (ALoFTRAG, AutoRAG-LoRA [`dwivedi2025autoraglora`]) trains the adapter
to be better *at a domain*. We deliberately do the opposite: the adapter is
trained to learn a reading protocol — lane routing, source-priority discipline,
do-not-confuse boundaries, exactness guards, insufficient-context refusal — while
being explicitly forbidden from memorizing the corpus.

```text
Knowledge lives in the Atlas (RAG).
Behavior lives in the LoRA.
The LoRA must remain swappable across different Atlases.
```

### Claim 2 — A named, versioned corpus<->adapter contract

We formalize the interface between the corpus and the adapter as a versioned
artifact:

```text
atlas-contract_mini_128L-12C-5D_v1
  128 lanes
  12 cards per lane
  retrieval depth ~5 cards
  target model range .8B to 4B
```

The adapter name declares the RAG shape it was trained to navigate. This makes
adapters and corpora independently versionable and comparable. We have not found
this interface formalized as a portable, named spec elsewhere.

### Claim 3 — Small-model-first compact card budget

We design the card budget (12 compact, high-signal cards per lane) around the
capacity limits of `.8B`-`4B` models, rather than scaling card count for larger
models. This is a deliberate constraint, not a limitation we ran into.

---

## What we explicitly do NOT claim

Consistent with `CLAIMS_AND_LIMITS.md`:

- We do NOT claim a new LoRA algorithm or a new training method.
- We do NOT claim retrieval-aware fine-tuning as our invention.
- We do NOT claim structured RAG as our invention.
- We do NOT claim the adapter works before experiments show it.
- We do NOT claim a 4B model becomes a 7B model in general.

Our contribution is a **methodology and an interface standard**, plus the
evaluation evidence for whether it holds.

---

## The one experiment that decides whether this matters

Everything above is positioning. The project's value is decided by a single
experiment, already specified in the roadmap as the cross-corpus transfer experiment:

> Does an Atlas Reader LoRA trained on one Atlas transfer its reading behavior
> (routing, source priority, refusal, formatting) to a *different, non-AIWF*
> Atlas?

Two honest outcomes:

```text
If it transfers:
  We have a versioned contract plus a demonstrated transferable reading adapter.
  That is a publishable methodology contribution.

If it does not transfer:
  We have a structured RAFT variant that overfit to one corpus.
  That is a publishable negative result, and still useful evidence about where
  structured RAG helps without an adapter.
```

Either way the project produces reviewable research, which is the stated goal.

---

## How to cite this honestly in a writeup

Recommended framing for any public description:

> The Atlas Reader LoRA applies retrieval-aware fine-tuning (in the RAFT /
> ALoFTRAG family) to a structured, lane-routed corpus. Its novel elements are
> not the training mechanism but (1) a deliberately content-agnostic reading
> adapter intended to transfer across corpora, (2) a named, versioned
> corpus-adapter contract, and (3) a small-model-first compact card budget. The
> central open question is cross-corpus behavioral transfer, evaluated in
> the cross-corpus transfer experiment.

This framing is defensible: it credits prior art, states a bounded contribution,
and names the experiment that confirms or refutes it.

---

## Cited sources

The active citation registry is now maintained in:

```text
10_source_materials/SOURCE_CITATIONS.md
10_source_materials/CITATION_MATRIX.md
10_source_materials/REFERENCES.bib
```

Use citation keys from those files in public-facing docs.

Do not cite AI assistants or drafting conversations as sources.


---

## v0.2.9-dev5 governance note

This document is a positioning artifact, not proof. The listed references are
leads to verify against primary sources before public citation. The project
remains below the `v0.3.0` owner-approval gate.


## Additional prior-art citations from conversation audit

Use the following additional citation keys for baseline and structured retrieval claims:

```text
lewis2020rag
asai2023selfrag
sarthi2024raptor
edge2024graphrag
mavromatis2024gnnrag
```

These are tracked in `10_source_materials/CONVERSATION_SOURCE_AUDIT.md`.


## Brand-safe claim

Use this wording when describing the project publicly:

> Atlas Reader LoRA does not claim to invent retrieval-aware fine-tuning, LoRA, QLoRA, or structured RAG. It tests whether a small adapter can learn a portable reading protocol for a named, versioned Atlas contract.

That claim is intentionally narrow, testable, and source-aware.
