param (
    [string]$Message = ""
)

$scriptDir = $PSScriptRoot
Set-Location $scriptDir

Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "          Automaticky Git Push na GitHub" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Prehled zmen:" -ForegroundColor Yellow
git status -s
Write-Host ""

if ([string]::IsNullOrWhiteSpace($Message)) {
    $inputMsg = Read-Host "Zadej popis zmen (stiskni ENTER pro automaticky popis)"
    if ([string]::IsNullOrWhiteSpace($inputMsg)) {
        $now = Get-Date -Format "yyyy-MM-dd HH:mm"
        $Message = "Aktualizace: $now"
    } else {
        $Message = $inputMsg
    }
}

Write-Host "`n1/3 Pridavam soubory (git add .)..." -ForegroundColor Cyan
git add .

Write-Host "2/3 Vytvarim commit: `"$Message`"..." -ForegroundColor Cyan
git commit -m "$Message"

Write-Host "3/3 Odesilam na GitHub (git push origin main)..." -ForegroundColor Cyan
git push origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n========================================================" -ForegroundColor Green
    Write-Host "[OK] Vse bylo uspesne nahrano na GitHub!" -ForegroundColor Green
    Write-Host "========================================================" -ForegroundColor Green
} else {
    Write-Host "`n========================================================" -ForegroundColor Red
    Write-Host "[CHYBA] Nahravani na GitHub se nezdarilo." -ForegroundColor Red
    Write-Host "========================================================" -ForegroundColor Red
}
