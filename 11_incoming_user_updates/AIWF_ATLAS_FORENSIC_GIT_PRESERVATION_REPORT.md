# AIWF ATLAS Forensic Git Preservation Report

Status: forensic preservation package  
Version added: v0.2.9-dev21  
Date: 2026-05-23

## Why this exists

The earlier dev20 repackaged archives were smaller than the uploaded source because `.git/` history was not carried forward.

This package preserves the uploaded Git history.

## Important safety choice

The uploaded `.git/` folder is preserved under:

```text
11_incoming_user_updates/AIWF_ATLAS_uploaded_2026-05-23_FOR_FORENSIC_WITH_GIT/
```

It is **not** placed at the merged repo root.

Reason:

```text
The uploaded .git history belongs to the original uploaded working tree.
The dev20/dev21 merged package has additional generated/merged files.
Putting the old .git at the merged root could create confusing git status/history behavior.
```

## Counts

```text
incoming total files: 4528
incoming .git files: 2389
incoming non-.git files: 2139
incoming total bytes: 65606040
incoming .git bytes: 20804288
incoming non-.git bytes: 44801752
```

## Git metadata

```text
.git/HEAD: None
branch ref: None
refs found: 0
```

## Forensic use

To inspect the original uploaded Git repo:

```powershell
cd 11_incoming_user_updates\AIWF_ATLAS_uploaded_2026-05-23_FOR_FORENSIC_WITH_GIT
git status
git log --oneline --decorate --graph --all -n 20
```

## RAG handoff note

Do **not** include this forensic package for a clean RAG handoff unless Git history is intentionally needed.

For RAG, use the RAG-clean package or remove:

```text
11_incoming_user_updates/AIWF_ATLAS_uploaded_2026-05-23_FOR_FORENSIC_WITH_GIT/.git/
lora_training_lab/
```

## No-wins guardrail

This is an archive/preservation pass only.

No adapter has been trained.

No install result exists.

No performance claim is added.
