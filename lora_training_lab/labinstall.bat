@echo off
setlocal EnableExtensions EnableDelayedExpansion

title AIWF Atlas Reader LoRA Lab Install - Python 3.10

echo ============================================================
echo  AI Without Fear - Atlas Reader LoRA Lab Install
echo  Target: Windows + Python 3.10 + NVIDIA CUDA PyTorch
echo  AIWF: Master principles, not platforms.
echo ============================================================
echo.

cd /d "%~dp0"

set "VENV_DIR=.venv310"
set "PY_CMD=py -3.10"
set "TORCH_CUDA=cu128"
set "TORCH_INDEX=https://download.pytorch.org/whl/cu128"

if /I "%~1"=="cu128" (
  set "TORCH_CUDA=cu128"
  set "TORCH_INDEX=https://download.pytorch.org/whl/cu128"
)
if /I "%~1"=="cu126" (
  set "TORCH_CUDA=cu126"
  set "TORCH_INDEX=https://download.pytorch.org/whl/cu126"
)
if /I "%~1"=="cu118" (
  set "TORCH_CUDA=cu118"
  set "TORCH_INDEX=https://download.pytorch.org/whl/cu118"
)
if /I "%~1"=="cpu" (
  set "TORCH_CUDA=cpu"
  set "TORCH_INDEX=https://download.pytorch.org/whl/cpu"
)

echo [0/9] Optional NVIDIA check...
where nvidia-smi >nul 2>&1
if errorlevel 1 (
  echo nvidia-smi not found in PATH. This is not always fatal, but CUDA training needs an NVIDIA driver visible to PyTorch.
) else (
  nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv,noheader
)

echo.
echo [1/9] Checking Python 3.10...
%PY_CMD% --version >nul 2>&1
if errorlevel 1 (
  echo Python launcher command failed: py -3.10
  echo Trying plain python.exe...
  python -c "import sys; raise SystemExit(0 if sys.version_info[:2] == (3,10) else 1)" >nul 2>&1
  if errorlevel 1 (
    echo.
    echo ERROR: Python 3.10 was not found.
    echo Install Python 3.10, then run this again.
    echo Expected command:
    echo   py -3.10 --version
    echo or:
    echo   python --version
    echo.
    pause
    exit /b 1
  ) else (
    set "PY_CMD=python"
  )
)

%PY_CMD% --version

echo.
echo [2/9] Creating virtual environment: %VENV_DIR%
if not exist "%VENV_DIR%\Scripts\python.exe" (
  %PY_CMD% -m venv "%VENV_DIR%"
  if errorlevel 1 (
    echo ERROR: Failed to create venv.
    pause
    exit /b 1
  )
) else (
  echo Existing venv found. Reusing it.
)

echo.
echo [3/9] Activating venv...
call "%VENV_DIR%\Scripts\activate.bat"
if errorlevel 1 (
  echo ERROR: Failed to activate venv.
  pause
  exit /b 1
)

echo.
echo [4/9] Upgrading pip tooling...
python -m pip install --upgrade pip setuptools wheel
if errorlevel 1 (
  echo ERROR: pip tooling upgrade failed.
  pause
  exit /b 1
)

echo.
echo [5/9] Installing PyTorch build: %TORCH_CUDA%
echo Index: %TORCH_INDEX%
python -m pip install --upgrade torch torchvision torchaudio --index-url %TORCH_INDEX%
if errorlevel 1 (
  echo.
  echo ERROR: PyTorch install failed for %TORCH_CUDA%.
  echo Try one of these:
  echo   labinstall.bat cu126
  echo   labinstall.bat cu118
  echo   labinstall.bat cpu
  echo.
  pause
  exit /b 1
)

echo.
echo [6/9] Installing Atlas Reader training requirements...
if exist requirements-training.txt (
  python -m pip install --upgrade -r requirements-training.txt
) else (
  python -m pip install --upgrade transformers datasets accelerate peft trl safetensors scipy pandas tensorboard bitsandbytes
)
if errorlevel 1 (
  echo.
  echo ERROR: Training requirements install failed.
  echo.
  echo Common cause on Windows: bitsandbytes wheel/toolchain mismatch.
  echo Try:
  echo   python -m pip install --upgrade bitsandbytes
  echo   labinstall.bat cu126
  echo   labinstall.bat cu118
  echo.
  echo The venv is still available at %VENV_DIR%.
  echo.
  pause
  exit /b 1
)

echo.
echo [7/9] Running GPU / package smoke test...
python scripts\lab_smoke_test.py
if errorlevel 1 (
  echo.
  echo WARNING: Smoke test reported a problem.
  echo Read lab_smoke_test_report.json and the output above.
  echo Install may still be partially usable, but do not start training until CUDA/package checks pass.
  echo.
) else (
  echo Smoke test passed.
)

echo.
echo [8/9] Writing installed package list...
python -m pip freeze > lab_pip_freeze.txt

echo.
echo [9/9] Checking TensorBoard command...
python -c "import tensorboard; print('TensorBoard import OK')" >nul 2>&1
if errorlevel 1 (
  echo WARNING: TensorBoard import failed.
) else (
  echo TensorBoard import OK.
)

echo.
echo ============================================================
echo  Install complete.
echo ============================================================
echo.
echo Activate later with:
echo   %VENV_DIR%\Scripts\activate.bat
echo.
echo Start TensorBoard with:
echo   tools\powershell\start_tensorboard.ps1
echo.
echo Dry-run first training config with:
echo   python scripts\train_atlas_reader_qlora.py --config 06_experiments\training_configs\A_sanity_r8_lr0001.json --dry-run
echo.
echo If CUDA failed, try:
echo   labinstall.bat cu126
echo   labinstall.bat cu118
echo.
pause
exit /b 0
