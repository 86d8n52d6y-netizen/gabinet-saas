#!/bin/bash
# Gabinet – start (macOS). Od tej wersji instalacja i aktualizacja: bash zainstaluj-mac.command (tworzy też aplikację „Gabinet”).
cd "$(dirname "$0")" || exit 1
exec bash ./zainstaluj-mac.command
