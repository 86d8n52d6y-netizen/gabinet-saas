// Katalog NFZ z bazy (tabela app.nfz_catalog – wspólna, tylko do odczytu) → format silnika.
import 'server-only';
import { withUser } from '../db';
import type { Catalog, CatalogEntry } from './engine';

export type CatalogRow = CatalogEntry & { source: string; validFrom: string | null; verifiedAt: string; icd: string | null };

export async function loadCatalog(userId: string): Promise<{ catalog: Catalog; rows: CatalogRow[] }> {
  const r = await withUser(userId, c => c.query(
    `SELECT code, name, points::float8 AS points, source, valid_from::text, verified_at::text, definition FROM app.nfz_catalog
      WHERE valid_to IS NULL OR valid_to >= current_date ORDER BY (definition->>'kind') = 'anest', code ~ '^ST' DESC, code`));
  const rows: CatalogRow[] = r.rows.map(x => ({
    code: x.code, name: x.name, points: Number(x.points), kind: x.definition.kind, unit: x.definition.unit ?? null,
    no15: !!x.definition.no15, no08: !!x.definition.no08, minPerPkg: x.definition.minPerPkg ?? null,
    source: x.source, validFrom: x.valid_from, verifiedAt: x.verified_at, icd: x.definition.icd ?? null,
  }));
  return { catalog: Object.fromEntries(rows.map(x => [x.code, x])), rows };
}
