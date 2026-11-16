#!/bin/bash
# Gabinet – start lokalny (macOS). Kliknij dwa razy w Finderze.
cd "$(dirname "$0")" || exit 1
if ! docker info >/dev/null 2>&1; then
  echo "❌ Docker Desktop nie jest uruchomiony. Otwórz aplikację Docker, poczekaj aż ikona wieloryba przestanie migać i uruchom ten plik ponownie."
  read -r -p "Naciśnij Enter, aby zamknąć…"; exit 1
fi
touch .env; chmod 600 .env
[ -s .env ] && [ -n "$(tail -c1 .env)" ] && echo >> .env          # brak końca linii w ostatnim wierszu
# brakujące wartości (także po aktualizacji aplikacji) są dopisywane – istniejących nie zmieniamy
dopisz() { grep -q "^$1=" .env || { echo "🔑 Dopisuję $1 do .env"; printf '%s=%s\n' "$1" "$(openssl rand -hex "$2")" >> .env; }; }
dopisz DB_ADMIN_PASSWORD 16
dopisz DB_APP_PASSWORD 16
dopisz AUTH_SECRET 32
dopisz APP_ENC_KEY 32
echo "🐳 Buduję i uruchamiam Gabinet (pierwszy raz może potrwać kilka minut)…"
docker compose up --build -d || { echo "❌ Błąd uruchamiania – skopiuj komunikat powyżej i prześlij go."; read -r -p "Enter…"; exit 1; }
echo "⏳ Czekam aż aplikacja odpowie…"
for i in $(seq 1 60); do
  if curl -fs http://localhost:3000/api/zdrowie >/dev/null; then
    echo "✅ Gotowe: http://localhost:3000   (testowa poczta: http://localhost:8025, stan: http://localhost:3000/stan)"
    open http://localhost:3000; exit 0
  fi
  sleep 2
done
echo "⚠️ Aplikacja nie odpowiada. Logi:"; docker compose logs --tail=40 app migrate
read -r -p "Enter…"
