@echo off
chcp 65001 >nul
REM Gabinet – start lokalny (Windows). Kliknij dwa razy.
cd /d "%~dp0"
docker info >nul 2>&1
if errorlevel 1 (
  echo Docker Desktop nie jest uruchomiony. Otworz Docker Desktop, poczekaj az sie uruchomi i sprobuj ponownie.
  pause & exit /b 1
)
if not exist .env (
  echo Tworze plik .env z losowymi haslami...
  powershell -NoProfile -Command "'DB_ADMIN_PASSWORD='+[guid]::NewGuid().ToString('N') | Out-File -Encoding ascii .env; 'DB_APP_PASSWORD='+[guid]::NewGuid().ToString('N') | Out-File -Encoding ascii -Append .env"
)
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
