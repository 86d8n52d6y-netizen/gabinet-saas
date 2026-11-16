#!/bin/bash
# Gabinet – kopia bazy teraz (np. przed większymi zmianami). Plik trafia do ~/Gabinet/kopie (nie jest usuwany automatycznie).
cd "$(dirname "$0")" || exit 1
export PATH="/usr/local/bin:/opt/homebrew/bin:/Applications/Docker.app/Contents/Resources/bin:$PATH"
KOPIE="$HOME/Gabinet/kopie"; mkdir -p "$KOPIE"
f="$KOPIE/reczna-$(date +%Y-%m-%d_%H%M).dump"
if docker compose exec -T db pg_dump -U migrator -d gabinet -Fc > "$f" && [ -s "$f" ]; then echo "✅ Kopia: $f ($(du -h "$f" | cut -f1))"
else rm -f "$f"; echo "❌ Nie udało się – czy Gabinet jest uruchomiony?"; fi
read -r -p "Enter…"
