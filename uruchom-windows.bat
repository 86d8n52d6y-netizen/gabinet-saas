@echo off
chcp 65001 >nul
REM Gabinet – start lokalny (Windows). Kliknij dwa razy.
cd /d "%~dp0"
docker info >nul 2>&1
if errorlevel 1 (
  echo Docker Desktop nie jest uruchomiony. Otworz Docker Desktop, poczekaj az sie uruchomi i sprobuj ponownie.
  pause & exit /b 1
)
if not exist .env type nul > .env
REM brakujace wartosci sa dopisywane - istniejacych nie zmieniamy
powershell -NoProfile -Command "$e=Get-Content .env -ErrorAction SilentlyContinue; function D($k,$n){ if(-not ($e -match ('^'+$k+'='))){ $b=New-Object byte[] $n; [Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($b); Add-Content -Encoding ascii .env ($k+'='+(($b|%%{$_.ToString('x2')}) -join '')); Write-Host ('Dopisuje '+$k) } }; D 'DB_ADMIN_PASSWORD' 16; D 'DB_APP_PASSWORD' 16; D 'AUTH_SECRET' 32; D 'APP_ENC_KEY' 32"
echo Buduje i uruchamiam Gabinet (pierwszy raz kilka minut)...
docker compose up --build -d
if errorlevel 1 ( echo Blad uruchamiania - skopiuj komunikat i przeslij go. & pause & exit /b 1 )
echo Czekam az aplikacja odpowie...
for /l %%i in (1,1,60) do (
  powershell -NoProfile -Command "try{Invoke-WebRequest -UseBasicParsing http://localhost:3000/api/zdrowie -TimeoutSec 2 ^| Out-Null; exit 0}catch{exit 1}" && goto ok
  timeout /t 2 >nul
)
echo Aplikacja nie odpowiada. Logi:
docker compose logs --tail=40 app migrate
pause & exit /b 1
:ok
echo Gotowe: http://localhost:3000   (testowa poczta: http://localhost:8025)
start http://localhost:3000
pause
