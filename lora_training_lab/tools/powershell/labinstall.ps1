param(
    [ValidateSet("cu128","cu126","cu118","cpu")]
    [string]$TorchBuild = "cu128"
)

$ErrorActionPreference = "Stop"
Write-Host "AI Without Fear - Atlas Reader LoRA Lab Install"
Write-Host "Torch build: $TorchBuild"

& "$PSScriptRoot\..\..\labinstall.bat" $TorchBuild
