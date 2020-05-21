$OLDWD = Get-Location
Set-Location $PSScriptRoot
Set-Location ..

Invoke-Command -ScriptBlock {
    python -m venv radiox/radiox_environment
    .\radiox\radiox_environment\Scripts\Activate.ps1
    pip install requests
    pip install beautifulsoup4
    pip install spotipy
} | Out-Null

Set-Location $OLDWD
