#!/usr/bin/env bash
# Test całości w przeglądarce (Chrome + Playwright): świeża baza, zbudowany serwer produkcyjny, poczta do plików.
# Użycie: bash tests/e2e/uruchom.sh   (wymaga: zbudowanej aplikacji `npx next build`, PostgreSQL testowego, python3 + playwright)
set -e
cd "$(dirname "$0")/../.."
export PGHOST=${PGHOST:-/tmp/pgtest} PGPORT=${PGPORT:-55432} PGUSER=${PGUSER:-migrator}
DB=gabinet_e2e PORT=${E2E_PORT:-3990} MAILS=/tmp/gabinet-e2e-mail
psql -X -q -d postgres -c "DROP DATABASE IF EXISTS $DB WITH (FORCE)" -c "CREATE DATABASE $DB" >/dev/null
DATABASE_ADMIN_URL="postgresql://$PGUSER@localhost:$PGPORT/$DB?host=$PGHOST" DB_APP_PASSWORD=haslo-e2e-1234567890 node scripts/migrate.mjs >/dev/null
rm -rf "$MAILS" && mkdir -p "$MAILS"
rm -rf .next/standalone/.next/static && cp -r .next/static .next/standalone/.next/static
[ -f /tmp/gabinet-e2e.pid ] && kill "$(cat /tmp/gabinet-e2e.pid)" 2>/dev/null || true
( cd .next/standalone && exec env NODE_ENV=production PORT=$PORT HOSTNAME=127.0.0.1 \
  DATABASE_URL="postgresql://gabinet_web:haslo-e2e-1234567890@localhost:$PGPORT/$DB?host=$PGHOST" \
  AUTH_SECRET=$(openssl rand -hex 32) APP_ENC_KEY=$(openssl rand -hex 32) APP_URL=http://127.0.0.1:$PORT \
  MAIL_DIR=$MAILS PASSWORD_BREACH_CHECK=0 node server.js > /tmp/gabinet-e2e-server.log 2>&1 ) &
echo $! > /tmp/gabinet-e2e.pid
for i in $(seq 1 40); do curl -sf -o /dev/null http://127.0.0.1:$PORT/api/zdrowie && break; sleep 0.25; done
rc=0
E2E_URL=http://127.0.0.1:$PORT E2E_MAILS=$MAILS E2E_DB=$DB python3 tests/e2e/t_konta.py || rc=$?
kill "$(cat /tmp/gabinet-e2e.pid)" 2>/dev/null || true
[ $rc -eq 0 ] || { echo "--- log serwera:"; tail -30 /tmp/gabinet-e2e-server.log; }
exit $rc
