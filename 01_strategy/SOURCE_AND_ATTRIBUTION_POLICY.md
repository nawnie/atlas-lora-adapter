# Source and Attribution Policy

Status: active project policy  
Version added: v0.2.9-dev5-clean  
Date: 2026-05-22

## Rule

AI assistants, chatbots, drafting tools, or model outputs are not treated as scholarly or technical sources for this project.

They may help draft, organize, critique, or transform project material, but they are not cited as evidence.

## Source hierarchy

Valid sources for factual or research claims include:

1. primary papers;
2. official documentation;
3. official repositories or model cards;
4. measured local experiment outputs;
5. project-authored notes clearly marked as internal reasoning or draft material.

Invalid as evidence:

```text
assistant output
chatbot output
drafting-model response
unsourced AI-generated summaries
```

## Related-work handling

`01_strategy/RELATED_WORK.md` is treated as a project-authored research-positioning draft.

It is not a citation to an AI assistant.

The references listed inside it are leads that must be verified against primary sources before public release.

## Public citation rule

Before public release, cite the papers, official docs, repositories, or measured results directly.

Do not cite the assistant that helped prepare the draft.

## Reason

This protects the project from circular sourcing and keeps the research posture credible.

The Atlas project can use AI tools as drafting aids without treating those tools as authorities.

## v0.2.9-dev8 source-ledger addition

The repository now includes a source ledger:

```text
10_source_materials/SOURCE_LEDGER.md
10_source_materials/SOURCE_LEDGER.json
10_source_materials/TRAINING_CODE_INVENTORY.md
10_source_materials/TRAINING_CODE_SOURCE_MAP.md
```

Training code is treated as project source code and must be evaluated through measured runs, not treated as proof by itself.
