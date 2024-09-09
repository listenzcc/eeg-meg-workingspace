#! Powershell script for ./search files.py

# ----------------------------------------
# ---- Get current script path ----
$scriptPath = $MyInvocation.MyCommand.Path
$scriptFolder = Split-Path $scriptPath -Parent

# ----------------------------------------
# ---- Insert python path ----
$pythonPath = Split-Path $scriptFolder -Parent
. (Join-Path $scriptFolder "insert python path.ps1")

# ----------------------------------------
# ---- Run python cli ----
python (Join-Path $scriptFolder "search files.py")