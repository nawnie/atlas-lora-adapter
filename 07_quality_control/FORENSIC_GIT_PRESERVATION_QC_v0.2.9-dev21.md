# Forensic Git Preservation QC v0.2.9-dev21

Status: QC pass  
Date: 2026-05-23

## User request

The user selected `a`: repackage with `.git/` preserved too.

## Done

Preserved the uploaded `AIWF - ATLAS.zip` contents including `.git/` under:

```text
11_incoming_user_updates/AIWF_ATLAS_uploaded_2026-05-23_FOR_FORENSIC_WITH_GIT/
```

## Why not root `.git/`

The merged dev21 package is not the exact original uploaded working tree.

Placing the uploaded `.git/` at root could make Git report confusing changes because the merged repo contains generated dev20/dev21 files.

The forensic copy keeps original Git history inspectable without corrupting the merged package's working-tree assumptions.

## Counts

```text
incoming total files: 4528
incoming .git files: 2389
incoming non-.git files: 2139
incoming total bytes: 65606040
incoming .git bytes: 20804288
incoming non-.git bytes: 44801752
```

## Added

```text
11_incoming_user_updates/AIWF_ATLAS_FORENSIC_GIT_PRESERVATION_REPORT.md
11_incoming_user_updates/AIWF_ATLAS_FORENSIC_GIT_INVENTORY.json
07_quality_control/FORENSIC_GIT_PRESERVATION_QC_v0.2.9-dev21.md
09_research_notes/PROJECT_STATUS_v0.2.9-dev21.md
```

## Boundary

This is preservation only.

No training, install, or evaluation result is claimed.
