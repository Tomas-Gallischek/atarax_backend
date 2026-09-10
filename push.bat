@echo off
setlocal enabledelayedexpansion

:: Prechod do slozky se skriptem (atarax_backend)
cd /d "%~dp0"

echo ========================================================
echo           Automaticky Git Push na GitHub
echo ========================================================
echo.

:: Zobrazeni zmen
echo Prehled zmen:
git status -s
echo.

:: Moznost zadat vlastni commit zpravu nebo pouzit vychozi
set "commit_msg=%*"
if "%commit_msg%"=="" (
    set /p "commit_msg=Zadej popis zmen (stiskni ENTER pro automaticky popis): "
)

if "%commit_msg%"=="" (
    set "commit_msg=Aktualizace: %date% %time:~0,5%"
)

echo.
echo 1/3 Pridavam soubory do Gitu (git add .)...
git add .

echo 2/3 Vytvarim commit s popisem: "%commit_msg%"...
git commit -m "%commit_msg%"

echo 3/3 Odesilam na GitHub (git push origin main)...
git push origin main

if %ERRORLEVEL% equ 0 (
    echo.
    echo ========================================================
    echo [OK] Vse bylo uspesne nahrano na GitHub!
    echo ========================================================
) else (
    echo.
    echo ========================================================
    echo [CHYBA] Nahravani na GitHub se nezdarilo.
    echo ========================================================
)

echo Okno se zavre za 4 sekundy...
timeout /t 4 >nul
