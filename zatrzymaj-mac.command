#!/bin/bash
# Zatrzymuje Gabinet. Dane w bazie zostają (wolumen dane_bazy), kopie w ~/Gabinet/kopie.
cd "$(dirname "$0")" || exit 1
export PATH="/usr/local/bin:/opt/homebrew/bin:/Applications/Docker.app/Contents/Resources/bin:$PATH"
docker compose stop && echo "⏹ Zatrzymano. Dane zostają."
