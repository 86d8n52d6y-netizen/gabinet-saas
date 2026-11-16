#!/usr/bin/env bash
# Testowy PostgreSQL 16 w środowisku deweloperskim Claude (bez Dockera): /tmp/pgtest, port 55432, superużytkownik migrator.
# Tworzy klaster przy pierwszym uruchomieniu; przy kolejnych tylko go startuje.
set -e
B=/usr/lib/postgresql/16/bin D=/tmp/pgtest/data
if [ ! -f "$D/PG_VERSION" ]; then
  mkdir -p /tmp/pgtest && chown postgres /tmp/pgtest
  su postgres -c "$B/initdb -D $D -U migrator --auth=trust -E UTF8 --locale=C.UTF-8" >/dev/null
fi
su postgres -c "$B/pg_ctl -D $D status" >/dev/null 2>&1 || su postgres -c "$B/pg_ctl -D $D -o '-p 55432 -k /tmp/pgtest' -l /tmp/pgtest.log -w start" >/dev/null
psql -X -q -h /tmp/pgtest -p 55432 -U migrator -d postgres -tc "SELECT 1 FROM pg_database WHERE datname='gabinet'" | grep -q 1 || psql -X -q -h /tmp/pgtest -p 55432 -U migrator -d postgres -c "CREATE DATABASE gabinet"
echo "PostgreSQL testowy działa (/tmp/pgtest:55432)"
