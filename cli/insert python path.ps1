# Insert the $pythonPath to the $env:PYTHONPATH environment
$env:PYTHONPATH=$pythonPath;$env:PYTHONPATH
Write-Output "PS: Added $pythonPath to env:PYTHONPATH"