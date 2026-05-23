# Training Config Templates

Status: experiment templates  
Version added: v0.2.9-dev6

These JSON files are not tied to one training framework.

They capture the settings to test.

A training launcher can translate them into TRL/PEFT, Unsloth, Axolotl, or another runner later.

## Files

```text
A_sanity_r8_lr0001.json
B_baseline_r16_lr0002.json
C_capacity_r32_lr0001.json
D_stability_r32_lr00005.json
E_nodrop_r16_lr0002.json
F_context4096_r16.json
G_rank64_stress.json
H_packing_efficiency.json
```

## Most important first runs

```text
A_sanity_r8_lr0001
B_baseline_r16_lr0002
C_capacity_r32_lr0001
```

Do not use these configs as proof of correctness.

They are starting hypotheses for overnight testing.
