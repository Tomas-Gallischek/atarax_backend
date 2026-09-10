$scriptPath = $PSScriptRoot
if (Test-Path "$scriptPath\manage.py") {
    Set-Location $scriptPath
} elseif (Test-Path "$scriptPath\atarax_backend\manage.py") {
    Set-Location "$scriptPath\atarax_backend"
} else {
    Write-Error "Soubor manage.py nebyl nalezen!"
    exit 1
}

Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "Spoustim Django backend a oteviram http://127.0.0.1:8000/admin/" -ForegroundColor Green
Write-Host "Ukonceni serveru: CTRL + C" -ForegroundColor Yellow
Write-Host "========================================================" -ForegroundColor Cyan

# Otevreni v prohlizeci s kratkym zpozdenim na pozadi
Start-Job -ScriptBlock {
    Start-Sleep -Seconds 2
    Start-Process "http://127.0.0.1:8000/admin/"
} | Out-Null

python manage.py runserver
