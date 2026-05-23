# RAG Handoff Guide

Status: active handoff guide  
Version added: v0.2.9-dev20  
Date: 2026-05-23

## Purpose

This repo can now be used as:

1. a full research repo with `lora_training_lab/`;
2. a clean Atlas/RAG package with training, private handoff, and forensic archive material removed.

For the **LoRA adapter GitHub repo**, keep `lora_training_lab/`.

## Remove for RAG handoff

```text
lora_training_lab/
11_incoming_user_updates/AIWF_ATLAS_uploaded_2026-05-23_FOR_FORENSIC_WITH_GIT/
11_incoming_user_updates/codex-profile-handoff/
11_incoming_user_updates/persona-packs-torchie/
```

## Keep for RAG handoff

```text
00_landing_page/
01_strategy/
02_atlas_contracts/
03_lane_system/
05_evaluation/
07_quality_control/
08_visuals/
09_research_notes/
10_source_materials/
11_incoming_user_updates/
AGENTS.md
README.md
PROJECT_PREINSTALL_STATUS.md
PROJECT_STATUS.md
REPO_NAVIGATION.md
DIRECTORY_MAP.md
```

## Uploaded Atlas source

The uploaded archive was preserved without `.git` here:

```text
11_incoming_user_updates/AIWF_ATLAS_uploaded_2026-05-23/
```

## Canonical VOL1 lanes added

```text
03_lane_system/vol1_canonical_research_lanes/
```

Canonical lanes copied: 35  
Canonical retrieval cards copied: 410

## No-wins reminder

This repackage adds structure and source material. It does not train a LoRA or prove performance.
