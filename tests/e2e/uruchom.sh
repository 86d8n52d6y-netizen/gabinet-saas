#!/usr/bin/env bash
# Testy całości w przeglądarce (Chrome + Playwright). Każdy plik t_*.py dostaje ŚWIEŻĄ bazę i własny serwer produkcyjny,
# poczta zapisywana do plików. Użycie: bash tests/e2e/uruchom.sh [tests/e2e/t_plik.py ...]
# Wymaga: `npx next build`, PostgreSQL testowego (bash tests/pg-start.sh), python3 + playwright, Google Chrome.
cd "$(dirname "$0")/../.."
export TZ=${TZ:-Europe/Warsaw}   # przeglądarka testowa w strefie użytkowników (w UTC „dziś” między 0:00 a 1:00 różni się od daty polskiej)
export PGHOST=${PGHOST:-/tmp/pgtest} PGPORT=${PGPORT:-55432} PGUSER=${PGUSER:-migrator}
DB=gabinet_e2e PORT=${E2E_PORT:-3990} MAILS=/tmp/gabinet-e2e-mail PIDF=/tmp/gabinet-e2e.pid
rm -rf .next/standalone/.next/static && cp -r .next/static .next/standalone/.next/static
stop() { [ -f $PIDF ] && kill "$(cat $PIDF)" 2>/dev/null; rm -f $PIDF; sleep 0.3; }
start() {
  stop
  psql -X -q -d postgres -c "DROP DATABASE IF EXISTS $DB WITH (FORCE)" -c "CREATE DATABASE $DB" >/dev/null 2>&1
  DATABASE_ADMIN_URL="postgresql://$PGUSER@localhost:$PGPORT/$DB?host=$PGHOST" DB_APP_PASSWORD=haslo-e2e-1234567890 node scripts/migrate.mjs >/dev/null || exit 1
  rm -rf "$MAILS" && mkdir -p "$MAILS"
  ( cd .next/standalone && exec env NODE_ENV=production PORT=$PORT HOSTNAME=127.0.0.1 \
    DATABASE_URL="postgresql://gabinet_web:haslo-e2e-1234567890@localhost:$PGPORT/$DB?host=$PGHOST" \
    AUTH_SECRET=$(openssl rand -hex 32) APP_ENC_KEY=$(openssl rand -hex 32) APP_URL=http://127.0.0.1:$PORT \
    MAIL_DIR=$MAILS PASSWORD_BREACH_CHECK=0 MFA_ENROLL=${MFA:-0} node server.js > /tmp/gabinet-e2e-server.log 2>&1 ) &
  echo $! > $PIDF
  for i in $(seq 1 40); do curl -sf -o /dev/null http://127.0.0.1:$PORT/api/zdrowie && return; sleep 0.25; done
  echo "Serwer nie wystartował"; tail -20 /tmp/gabinet-e2e-server.log; exit 1
}
export E2E_URL=http://127.0.0.1:$PORT E2E_MAILS=$MAILS E2E_DB=$DB
if [ $# -gt 0 ]; then files=("$@"); else files=(tests/e2e/t_*.py); fi
rc=0
for f in "${files[@]}"; do
  MFA=0; [ "$(basename "$f")" = t_konta.py ] && MFA=1     # t_konta: pełny test 2FA (konta, które już mają 2FA); reszta: włączanie 2FA wyłączone jak w aplikacji
  start
  (cd tests/e2e && python3 "$(basename "$f")") || { rc=1; echo "--- log serwera ($f):"; tail -15 /tmp/gabinet-e2e-server.log; }
done
stop
exit $rc
