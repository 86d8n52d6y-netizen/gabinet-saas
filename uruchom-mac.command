#!/bin/bash
# Gabinet – start lokalny (macOS). Kliknij dwa razy w Finderze.
cd "$(dirname "$0")" || exit 1
if ! docker info >/dev/null 2>&1; then
  echo "❌ Docker Desktop nie jest uruchomiony. Otwórz aplikację Docker, poczekaj aż ikona wieloryba przestanie migać i uruchom ten plik ponownie."
  read -r -p "Naciśnij Enter, aby zamknąć…"; exit 1
fi
if [ ! -f .env ]; then
  echo "🔑 Tworzę plik .env z losowymi hasłami (tylko na tym komputerze)…"
  printf 'DB_ADMIN_PASSWORD=%s\nDB_APP_PASSWORD=%s\n' "$(openssl rand -hex 16)" "$(openssl rand -hex 16)" > .env
  chmod 600 .env
fi
echo "🐳 Buduję i uruchamiam Gabinet (pierwszy raz może potrwać kilka minut)…"
docker compose up --build -d || { echo "❌ Błąd uruchamiania – skopiuj komunikat powyżej i prześlij go."; read -r -p "Enter…"; exit 1; }
echo "⏳ Czekam aż aplikacja odpowie…"
for i in $(seq 1 60); do
  if curl -fs http://localhost:3000/api/zdrowie >/dev/null; then
    echo "✅ Gotowe: http://localhost:3000   (testowa poczta: http://localhost:8025)"
    open http://localhost:3000; exit 0
  fi
  sleep 2
done
echo "⚠️ Aplikacja nie odpowiada. Logi:"; docker compose logs --tail=40 app migrate
read -r -p "Enter…"
