param(
    [string]$LogDir = "06_experiments\runs",
    [int]$Port = 6006,
    [string]$HostAddress = "127.0.0.1"
)

$ErrorActionPreference = "Stop"

Write-Host "Atlas Reader TensorBoard Dashboard"
Write-Host "LogDir: $LogDir"
Write-Host "URL: http://$HostAddress`:$Port"

$tb = Get-Command tensorboard -ErrorAction SilentlyContinue
if ($tb) {
    tensorboard --logdir $LogDir --host $HostAddress --port $Port
} else {
    python -m tensorboard.main --logdir $LogDir --host $HostAddress --port $Port
}
