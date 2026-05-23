# Training Code Inventory

Status: active inventory  
Version added: v0.2.9-dev8  
Date: 2026-05-22

## Purpose

This file explicitly lists the training-related code, configs, and launch helpers included in the repo.

## Training code files

| Path | Role | Bytes | SHA256 |
|---|---|---:|---|
| `06_experiments/training_configs/A_sanity_r8_lr0001.json` | training_config | 1303 | `2d63269d93695f3d528986f790cc7e96927b1cc779d0ff78f1f8e54e163e5ef2` |
| `06_experiments/training_configs/B_baseline_r16_lr0002.json` | training_config | 1397 | `981ef0ee2e58f99ab58817c3df04205a9c5afc61689c17410bf913076e823792` |
| `06_experiments/training_configs/C_capacity_r32_lr0001.json` | training_config | 1397 | `69f8c4c5555f494603925917ed60e4e67ab9e19b6417db67b0a71f6463b3a94d` |
| `06_experiments/training_configs/D_stability_r32_lr00005.json` | training_config | 1400 | `571709be38406ac60ce67df19ea40efa64cc961fabc7e5d4084d5aa27aee5a0c` |
| `06_experiments/training_configs/E_nodrop_r16_lr0002.json` | training_config | 1392 | `3034be0141961cf5806e520ed48b4820fc5ac1ea053cc6afce805b9f31336073` |
| `06_experiments/training_configs/F_context4096_r16.json` | training_config | 1389 | `31a4fd38d5561a6836efda4f7b9c0ab739d693a30000e756afb0afd68b0f1d19` |
| `06_experiments/training_configs/G_rank64_stress.json` | training_config | 1386 | `8ef44ebbcc403d12ddfa33cd70f1bba1ebaa6e07861fac524770b12729d56d3e` |
| `06_experiments/training_configs/H_packing_efficiency.json` | training_config | 1394 | `ebe1bb91334efd6717bdf59215be0c454ecace84202c46a17df0f4476174fb50` |
| `requirements-training.txt` | requirements | 305 | `a81c39fe489000f77df5a5d9c8053aed300175d7f47598a7bfb9d8fd412e2e17` |
| `scripts/build_seed_training_records.py` | python_script | 4088 | `f0e79c90dd2717770b64ef3300aa7e4c2c5254849204609bda028a8e33c09a7b` |
| `scripts/check_training_record_quality.py` | python_script | 2899 | `53820bc698981e0af4903736406e88b83601b23861cacf5d40b0f1e9a9dcd3c9` |
| `scripts/compute_significance.py` | python_script | 3080 | `9d1f0228c28aa96641af0c9744fc8f8bdb550cea136303a9ea81197724a1f786` |
| `scripts/create_train_eval_split.py` | python_script | 1767 | `f3cdcd2ce6863af6afebe1bad2c7348a8bc18aa9a811f7caeaa0935e193b3290` |
| `scripts/render_atlas_sft_dataset.py` | python_script | 2993 | `3aec2f6b5b03a1d185897e69584d6c6211beefbda810ac9a82a29cc50d005125` |
| `scripts/summarize_results.py` | python_script | 1570 | `bffe5dd766f521202cb6396afe5addbd498579ecf01f2a84f14ba245e5271a94` |
| `scripts/train_atlas_reader_qlora.py` | python_script | 15226 | `4c0e47c30b54ad60787be860297f2511e51e97e232cc56dc7dbd23bbe8375e11` |
| `scripts/validate_seed_cards.py` | python_script | 3900 | `0f155b9908b742372225fb7e841dc6c5216d2e481ef453e7367d7deb82e87065` |
| `scripts/validate_training_records.py` | python_script | 3398 | `44e5cac7c8cf367c1e23c0550132e60863f2ee64b96abc5d0d64c30947e7b326` |
| `tools/powershell/dry_run_training_config.ps1` | powershell_helper | 278 | `0f2c975be465408788a5357acbd0bbfb629a76992c22788d093e18a3f527d6f9` |
| `tools/powershell/train_atlas_reader.ps1` | powershell_helper | 251 | `25e50c5700db3f8e87414e36ddb8dd0bec1be1ec41c66236f796116791691f15` |


## Critical training files

### `scripts/train_atlas_reader_qlora.py`

Main runnable TRL/PEFT QLoRA training script.

Handles:

- dry-run config validation;
- Atlas-record or chat-message JSONL loading;
- Atlas record to messages conversion;
- TRL `SFTTrainer`;
- PEFT `LoraConfig`;
- optional 4-bit BitsAndBytes quantization;
- run metadata output;
- adapter output folder creation.

### `scripts/create_train_eval_split.py`

Deterministic train/eval split helper.

### `scripts/render_atlas_sft_dataset.py`

Converts Atlas training records to chat-style SFT JSONL.

### `scripts/validate_training_records.py`

Structural validator for Atlas training records.

### `scripts/check_training_record_quality.py`

Quality-risk checker for scaffold/meta-answer leakage.

### `scripts/compute_significance.py`

Paired smoke-evaluation statistics script.

## Training code source policy

Training code is project source code.

It is not treated as external evidence that the method works.

The code must be evaluated by running it and recording measured outputs.
