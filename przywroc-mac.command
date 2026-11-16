#!/bin/bash
# Gabinet – przywrócenie bazy z kopii (~/Gabinet/kopie). Obecny stan bazy zostanie ZASTĄPIONY stanem z kopii,
# dlatego najpierw robiona jest kopia „przed-przywroceniem-…”. Treści opisów w przeglądarce to nie dotyczy.
cd "$(dirname "$0")" || exit 1
export PATH="/usr/local/bin:/opt/homebrew/bin:/Applications/Docker.app/Contents/Resources/bin:$PATH"
KOPIE="$HOME/Gabinet/kopie"
docker compose exec -T db pg_isready -U migrator -d gabinet >/dev/null 2>&1 || { echo "❌ Baza nie działa – uruchom najpierw Gabinet."; read -r -p "Enter…"; exit 1; }
mapfile_list=(); while IFS= read -r l; do mapfile_list+=("$l"); done < <(ls -1t "$KOPIE"/*.dump 2>/dev/null | head -20)
[ ${#mapfile_list[@]} -gt 0 ] || { echo "Brak kopii w $KOPIE"; read -r -p "Enter…"; exit 1; }
echo "Kopie (najnowsze na górze):"; for i in "${!mapfile_list[@]}"; do printf '  %2d) %s\n' $((i+1)) "$(basename "${mapfile_list[$i]}")"; done
read -r -p "Numer kopii do przywrócenia (Enter = anuluj): " n
[[ "$n" =~ ^[0-9]+$ ]] && [ "$n" -ge 1 ] && [ "$n" -le ${#mapfile_list[@]} ] || { echo "Anulowano."; exit 0; }
f="${mapfile_list[$((n-1))]}"
echo "⚠️  Baza zostanie zastąpiona stanem z: $(basename "$f")"
read -r -p "Wpisz TAK, aby kontynuować: " ok; [ "$ok" = "TAK" ] || { echo "Anulowano – nic nie zmieniono."; exit 0; }
s="$KOPIE/przed-przywroceniem-$(date +%Y-%m-%d_%H%M).dump"
docker compose exec -T db pg_dump -U migrator -d gabinet -Fc > "$s" && [ -s "$s" ] || { echo "❌ Nie udało się zrobić kopii bieżącego stanu – przerwano."; exit 1; }
echo "💾 Bieżący stan zapisany: $(basename "$s")"
docker compose stop app kopie >/dev/null
if docker compose exec -T db pg_restore -U migrator -d gabinet --clean --if-exists --single-transaction < "$f"; then echo "✅ Przywrócono."
else echo "❌ Przywracanie nie powiodło się – baza bez zmian (operacja w jednej transakcji)."; fi
docker compose up -d app kopie >/dev/null && echo "▶ Gabinet uruchomiony: http://localhost:3000"
read -r -p "Enter…"
