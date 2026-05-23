# Source Ledger and Training Code QC v0.2.9-dev8

Status: QC pass  
Date: 2026-05-22

## User request addressed

This pass makes sure the repo is pulling source materials explicitly, especially training code.

## Added source materials

- `10_source_materials/AIWF_force_multiplier_insert.md`
- `10_source_materials/AIWF_Project_Chat_Distribution_Roadmap`

## Added inventory files

```text
10_source_materials/SOURCE_LEDGER.md
10_source_materials/SOURCE_LEDGER.json
10_source_materials/TRAINING_CODE_INVENTORY.md
10_source_materials/TRAINING_CODE_SOURCE_MAP.md
scripts/build_source_inventory.py
```

## Training-code inventory count

```text
20 training/code/config/helper files indexed
```

## Compile check

```text
scripts/build_source_inventory.py: passed
```

## Source policy

AI assistants remain drafting aids, not sources.

Official training references are included as source leads for code/API usage.

Training code is included as project source code but is not proof that the method works.

## Next step

Use the source ledger during future research passes and keep `TRAINING_CODE_INVENTORY.md` updated when code changes.
