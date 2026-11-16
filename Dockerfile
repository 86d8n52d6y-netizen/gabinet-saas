# Gabinet – obraz aplikacji (Next.js standalone). Budowany wieloetapowo, uruchamiany jako użytkownik bez uprawnień root.
FROM node:22-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --no-audit --no-fund

FROM deps AS build
COPY . .
ENV NEXT_TELEMETRY_DISABLED=1
RUN npm run build

# Jednorazowe migracje bazy (tylko zależności produkcyjne + skrypt + pliki SQL)
FROM node:22-alpine AS migrate
WORKDIR /app
ENV NODE_ENV=production
COPY package.json package-lock.json ./
RUN npm ci --omit=dev --no-audit --no-fund && npm cache clean --force
COPY scripts ./scripts
COPY db/migrations ./db/migrations
USER node
CMD ["node", "scripts/migrate.mjs"]

# Serwer aplikacji
FROM node:22-alpine AS app
WORKDIR /app
ENV NODE_ENV=production NEXT_TELEMETRY_DISABLED=1 PORT=3000 HOSTNAME=0.0.0.0
COPY --from=build --chown=node:node /app/.next/standalone ./
COPY --from=build --chown=node:node /app/.next/static ./.next/static
USER node
EXPOSE 3000
HEALTHCHECK --interval=15s --timeout=5s --start-period=20s --retries=5 \
  CMD wget -qO- http://127.0.0.1:3000/api/zdrowie >/dev/null || exit 1
CMD ["node", "server.js"]
