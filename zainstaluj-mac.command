#!/bin/bash
# Gabinet – instalacja i aktualizacja na Macu. Uruchom w Terminalu:  bash zainstaluj-mac.command
#  • tworzy folder ~/Gabinet (klucze .env i kopie zapasowe bazy) – wspólny dla wszystkich kolejnych wersji,
#  • przed aktualizacją robi kopię bazy, buduje i uruchamia aplikację,
#  • tworzy aplikację „Gabinet” w ~/Applications (start jednym kliknięciem; Docker Desktop uruchomi się sam).
set -u
cd "$(dirname "$0")" || exit 1
DIR="$(pwd)"; HOMEDIR="$HOME/Gabinet"; KOPIE="$HOMEDIR/kopie"; APP="$HOME/Applications/Gabinet.app"
export PATH="/usr/local/bin:/opt/homebrew/bin:/Applications/Docker.app/Contents/Resources/bin:$PATH"
stop() { echo "❌ $1"; read -r -p "Naciśnij Enter, aby zamknąć…"; exit 1; }

# 1. Docker Desktop
if ! docker info >/dev/null 2>&1; then
  echo "🐳 Uruchamiam Docker Desktop…"; open -a Docker 2>/dev/null
  for i in $(seq 1 90); do docker info >/dev/null 2>&1 && break; sleep 2; done
  docker info >/dev/null 2>&1 || stop "Docker Desktop nie działa. Otwórz aplikację Docker, poczekaj aż wieloryb przestanie migać i uruchom ten plik ponownie."
fi

# 2. klucze (.env): jeden plik w ~/Gabinet – kolejne wersje aplikacji używają tych samych kluczy i hasła bazy
mkdir -p "$KOPIE" && chmod 700 "$HOMEDIR"
if [ ! -f "$HOMEDIR/.env" ]; then
  if [ -s .env ]; then cp .env "$HOMEDIR/.env"; echo "🔑 Zapisuję klucze z tego folderu w ~/Gabinet/.env"
  else for d in ../gabinet-saas-main*/ ../gabinet-saas*/; do [ -s "$d.env" ] && [ "$d" != "./" ] && { cp "$d.env" "$HOMEDIR/.env"; echo "🔑 Znalazłem klucze w $d – zapisuję w ~/Gabinet/.env"; break; }; done; fi
fi
touch "$HOMEDIR/.env"; chmod 600 "$HOMEDIR/.env"
[ -s "$HOMEDIR/.env" ] && [ -n "$(tail -c1 "$HOMEDIR/.env")" ] && echo >> "$HOMEDIR/.env"
dopisz() { grep -q "^$1=" "$HOMEDIR/.env" || { echo "🔑 Nowy klucz $1"; printf '%s=%s\n' "$1" "$2" >> "$HOMEDIR/.env"; }; }
dopisz DB_ADMIN_PASSWORD "$(openssl rand -hex 16)"
dopisz DB_APP_PASSWORD "$(openssl rand -hex 16)"
dopisz AUTH_SECRET "$(openssl rand -hex 32)"
dopisz APP_ENC_KEY "$(openssl rand -hex 32)"
grep -q '^GABINET_KOPIE=' "$HOMEDIR/.env" || printf 'GABINET_KOPIE=%s\n' "$KOPIE" >> "$HOMEDIR/.env"
if [ -f .env ] && ! cmp -s .env "$HOMEDIR/.env"; then cp .env ".env.poprzedni-$(date +%Y%m%d%H%M%S)"; fi
cp "$HOMEDIR/.env" .env; chmod 600 .env

# 3. kopia bazy przed aktualizacją (jeśli Gabinet już działał)
if [ -n "$(docker compose ps -q db 2>/dev/null)" ] && docker compose exec -T db pg_isready -U migrator -d gabinet >/dev/null 2>&1; then
  f="$KOPIE/przed-aktualizacja-$(date +%Y-%m-%d_%H%M).dump"
  echo "💾 Kopia bazy przed aktualizacją → $f"
  docker compose exec -T db pg_dump -U migrator -d gabinet -Fc > "$f" && [ -s "$f" ] || stop "Nie udało się zrobić kopii bazy – aktualizacja przerwana (dane nietknięte)."
elif docker volume inspect gabinet_dane_bazy >/dev/null 2>&1; then
  echo "💾 Uruchamiam bazę, żeby zrobić kopię przed aktualizacją…"
  docker compose up -d db >/dev/null 2>&1; for i in $(seq 1 30); do docker compose exec -T db pg_isready -U migrator -d gabinet >/dev/null 2>&1 && break; sleep 2; done
  f="$KOPIE/przed-aktualizacja-$(date +%Y-%m-%d_%H%M).dump"
  docker compose exec -T db pg_dump -U migrator -d gabinet -Fc > "$f" && [ -s "$f" ] || stop "Nie udało się zrobić kopii bazy – aktualizacja przerwana (dane nietknięte)."
  echo "   → $f"
fi

# 4. budowa i start
echo "🐳 Buduję i uruchamiam Gabinet (pierwszy raz kilka minut, kolejne 1–2 minuty)…"
docker compose up --build -d --remove-orphans || stop "Błąd uruchamiania – skopiuj komunikat powyżej i prześlij go."
echo "⏳ Czekam aż aplikacja odpowie…"
ok=""; for i in $(seq 1 60); do curl -fs http://localhost:3000/api/zdrowie >/dev/null && { ok=1; break; }; sleep 2; done
[ -n "$ok" ] || { docker compose logs --tail=40 app migrate; stop "Aplikacja nie odpowiada (logi powyżej)."; }

# 5. aplikacja „Gabinet” (tworzona na tym Macu – bez blokady Gatekeepera)
mkdir -p "$APP/Contents/MacOS"
cat > "$APP/Contents/Info.plist" <<PL
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
<key>CFBundleName</key><string>Gabinet</string><key>CFBundleDisplayName</key><string>Gabinet</string>
<key>CFBundleIdentifier</key><string>pl.gabinet.lokalny</string><key>CFBundleVersion</key><string>1</string>
<key>CFBundlePackageType</key><string>APPL</string><key>CFBundleExecutable</key><string>Gabinet</string>
<key>LSUIElement</key><true/>
</dict></plist>
PL
cat > "$APP/Contents/MacOS/Gabinet" <<SH
#!/bin/bash
export PATH="/usr/local/bin:/opt/homebrew/bin:/Applications/Docker.app/Contents/Resources/bin:\$PATH"
DIR="$DIR"
alert() { osascript -e "display alert \"Gabinet\" message \"\$1\"" >/dev/null; }
note() { osascript -e "display notification \"\$1\" with title \"Gabinet\"" >/dev/null; }
curl -fs http://localhost:3000/api/zdrowie >/dev/null && { open http://localhost:3000; exit 0; }
[ -d "\$DIR" ] || { alert "Nie ma folderu aplikacji: \$DIR. Uruchom ponownie zainstaluj-mac.command z aktualnego folderu."; exit 1; }
if ! docker info >/dev/null 2>&1; then
  note "Uruchamiam Docker Desktop…"; open -a Docker
  for i in \$(seq 1 90); do docker info >/dev/null 2>&1 && break; sleep 2; done
fi
docker info >/dev/null 2>&1 || { alert "Docker Desktop nie wystartował. Otwórz aplikację Docker i spróbuj ponownie."; exit 1; }
note "Uruchamiam Gabinet…"
cd "\$DIR" && docker compose up -d >/tmp/gabinet-start.log 2>&1 || { alert "Nie udało się uruchomić. Szczegóły: /tmp/gabinet-start.log"; exit 1; }
for i in \$(seq 1 60); do curl -fs http://localhost:3000/api/zdrowie >/dev/null && { open http://localhost:3000; exit 0; }; sleep 2; done
alert "Aplikacja nie odpowiada. Spróbuj ponownie za minutę."
SH
chmod +x "$APP/Contents/MacOS/Gabinet"
touch "$APP"

echo ""
echo "✅ Gotowe: http://localhost:3000"
echo "   • Start na co dzień: Finder → Aplikacje (w katalogu domowym) → Gabinet  (możesz przeciągnąć ją do Docka)"
echo "   • Kopie bazy: ~/Gabinet/kopie (automatycznie codziennie, 30 ostatnich)"
echo "   • Poczta testowa (potwierdzenia, reset hasła): http://localhost:8025"
open http://localhost:3000
