#!/bin/bash
# Zatrzymuje Gabinet. Dane w bazie zostają (wolumen dane_bazy).
cd "$(dirname "$0")" && docker compose stop && echo "⏹ Zatrzymano."
