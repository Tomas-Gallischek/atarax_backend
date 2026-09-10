@echo off
setlocal

:: Detekce slozky s manage.py
if exist "%~dp0manage.py" (
    cd /d "%~dp0"
) else if exist "%~dp0atarax_backend\manage.py" (
    cd /d "%~dp0atarax_backend"
) else (
    echo Chyba: Soubor manage.py nebyl nalezen!
    pause
    exit /b 1
)

echo ========================================================
echo Spoustim Django backend a oteviram http://192.168.0.95:8008/admin/
echo Ukonceni serveru: CTRL + C
echo ========================================================

:: Otevreni prohlizece na pozadi po 2 sekundach
start "" cmd /c "timeout /t 2 /nobreak >nul & start http://192.168.0.95:8008/admin/"

:: Spusteni vyvojoveho serveru
python manage.py runserver
