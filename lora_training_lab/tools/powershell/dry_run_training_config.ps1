param(
    [string]$Config = "06_experiments\training_configs\A_sanity_r8_lr0001.json"
)

$ErrorActionPreference = "Stop"
Write-Host "Atlas Reader dry-run training config check"
Write-Host "Config: $Config"

python scripts\train_atlas_reader_qlora.py --config $Config --dry-run
