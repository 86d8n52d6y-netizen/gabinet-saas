#!/bin/sh
# Automatyczna kopia bazy (kontener „kopie”): przy starcie, gdy ostatnia kopia jest starsza niż 20 h, i potem co godzinę sprawdza.
# Pliki: /kopie/gabinet-RRRR-MM-DD_GGMM.dump (format pg_dump -Fc). Zostaje 30 ostatnich kopii automatycznych; kopie „reczna-…”
# i „przed-…” (przed aktualizacją / przywróceniem) nie są usuwane automatycznie.
set -eu
mkdir -p /kopie
while true; do
  last=$(ls -1t /kopie/gabinet-*.dump 2>/dev/null | head -1 || true)
  if [ -z "$last" ] || [ -n "$(find "$last" -mmin +1200 2>/dev/null)" ]; then
    f="/kopie/gabinet-$(date +%Y-%m-%d_%H%M).dump"
    if pg_dump -h db -U migrator -d gabinet -Fc -f "$f.tmp" && pg_restore -l "$f.tmp" >/dev/null; then
      mv "$f.tmp" "$f"; echo "kopia: $f ($(du -h "$f" | cut -f1))"
      ls -1t /kopie/gabinet-*.dump | tail -n +31 | xargs -r rm -f
    else
      rm -f "$f.tmp"; echo "BŁĄD kopii bazy $(date)" >&2
    fi
  fi
  sleep 3600
done
