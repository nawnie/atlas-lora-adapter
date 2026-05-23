# GitHub Upload Notes

Version: v0.2.9-dev21  
Purpose: prepare the Atlas Reader LoRA adapter package for GitHub upload.

## Recommended upload

Use this folder as the GitHub repo root:

```text
C:\Users\shawn\Desktop\ai project workspace\Repos\atlas-lora-adapter
```

This is the LoRA adapter research package, so keep:

```text
lora_training_lab/
```

That folder is only removed for a clean Atlas/RAG handoff package.

## Do not upload by default

The following paths are preserved locally for provenance but are ignored for normal public GitHub upload:

```text
11_incoming_user_updates/AIWF_ATLAS_uploaded_2026-05-23/
11_incoming_user_updates/AIWF_ATLAS_uploaded_2026-05-23_FOR_FORENSIC_WITH_GIT/
11_incoming_user_updates/codex-profile-handoff/
11_incoming_user_updates/persona-packs-torchie/
11_incoming_user_updates/metadata/
11_incoming_user_updates/top_level_docs/
08_visuals/incoming_from_AIWF_ATLAS/
```

Reason:

```text
They are source/archive payloads, duplicate public Atlas material, private/local handoff material, visual-source archive material, or forensic Git history.
```

The `.gitignore` file enforces this for `git add .`.

## Suggested first commit message

```text
Prepare Atlas Reader LoRA research package
```

## Current validation commands

Run from repo root:

```powershell
python scripts\validate_seed_cards.py
python scripts\validate_training_records.py lora_training_lab\04_training_data\SAMPLE_ATLAS_READER_MINI_RECORDS.jsonl
python scripts\check_training_record_quality.py lora_training_lab\04_training_data\SAMPLE_ATLAS_READER_MINI_RECORDS.jsonl
python lora_training_lab\scripts\qc_labinstall_static.py
```

Known expected result:

```text
Training records validate as schema/scaffold records.
Quality checker warns that the 21 sample records are not production SFT quality.
```

## Version status

This is still planning / seed-build work.

Do not promote to v0.3.0 without explicit owner approval.
