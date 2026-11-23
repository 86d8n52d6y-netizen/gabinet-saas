/* Warianty leczenia zachowawczego w Opisach prywatnych (prompt Patryka 23.11.2026, pkt 4): 1, 2, 3 powierzchnie i nakład –
   osobne procedury (osobna cena i wynagrodzenie lekarza w Cenniku). Plik aplikacji SaaS (nie pochodzi ze starej aplikacji).
   Formularz i tekst: na wzór „Opracowanie ubytku + odbudowa kompozytowa” (zach-kompozyt) – Twoja procedura zostaje bez zmian.
   Dokładane do window.PRYW_KATALOG przed startem modułu, zaraz po zach-kompozyt. */
(function () {
  'use strict';
  const P = window.PRYW_KATALOG; if (!P || !Array.isArray(P.proc)) return;
  const wz = P.proc.find(p => p.id === 'zach-kompozyt'); if (!wz) return;
  const clone = o => JSON.parse(JSON.stringify(o));
  const POW = (n, nazwa) => {
    const p = clone(wz);
    p.id = 'zach-' + n + 'pow'; p.name = nazwa; p.saas = true;
    p.desc = 'Opracowanie ubytku i odbudowa kompozytowa – ' + (n === 1 ? '1 powierzchnia' : n + ' powierzchnie') + ' (osobna cena w Cenniku).';
    p.fields.forEach(f => { if (f.k === 'pows') { f.req = 1; f.l = 'Powierzchnie (' + n + ')'; } });
    p.tpl = p.tpl.replace('Ząb {zab}{?pows}, powierzchnie {pows}{/pows}.', 'Ząb {zab}: wypełnienie ' + (n === 1 ? 'jednej powierzchni' : n === 2 ? 'dwóch powierzchni' : 'trzech powierzchni') + ' – powierzchnie {pows}.');
    p.npow = n;
    return p;
  };
  const naklad = clone(wz);
  Object.assign(naklad, { id: 'zach-naklad', name: 'Nakład (inlay / onlay / overlay)', saas: true,
    desc: 'Odbudowa pośrednia nakładem – etap przygotowania lub osadzenia (osobna cena w Cenniku).' });
  naklad.fields = naklad.fields.filter(f => !['wiaz', 'odcien', 'czyn'].includes(f.k));
  const iz = naklad.fields.findIndex(f => f.k === 'pows');
  naklad.fields.splice(iz + 1, 0,
    { k: 'rodzaj', t: 'select', l: 'Rodzaj nakładu', opts: ['inlay', 'onlay', 'overlay'], req: 1 },
    { k: 'etap', t: 'select', l: 'Etap', opts: ['opracowanie, wycisk / skan, uzupełnienie tymczasowe', 'osadzenie nakładu'], req: 1 });
  naklad.fields.forEach(f => { if (f.k === 'mat') { f.l = 'Materiał nakładu'; f.sug = ['ceramika szklana (e.max)', 'kompozyt pośredni', 'cyrkon']; f.req = 1; } });
  naklad.fields.splice(naklad.fields.findIndex(f => f.k === 'mat') + 1, 0,
    { k: 'cem', t: 'text', l: 'Cementowanie', sug: ['cement kompozytowy adhezyjny', 'cement kompozytowy samoadhezyjny'], show: { k: 'etap', eq: 'osadzenie nakładu' } },
    { k: 'kontr', t: 'select', l: 'Kontrola zwarcia i punktów stycznych', opts: ['prawidłowa', 'skorygowana'], show: { k: 'etap', eq: 'osadzenie nakładu' } });
  naklad.tpl = naklad.tpl
    .replace('Ząb {zab}{?pows}, powierzchnie {pows}{/pows}.', 'Ząb {zab}: nakład typu {rodzaj}{?pows}, powierzchnie {pows}{/pows} – {etap}.')
    .replace('{?czyn}Przebieg: {czyn}.{/czyn}\n', '').replace('{?wiaz}Technika wiązania: {wiaz}.{/wiaz}\n', '')
    .replace('Odbudowa: {mat}{?odcien}, odcień {odcien}{/odcien}.', 'Materiał nakładu: {mat}.{?cem} Cementowanie: {cem}.{/cem}{?kontr} Kontrola zwarcia i punktów stycznych: {kontr}.{/kontr}');
  const at = P.proc.indexOf(wz) + 1;
  P.proc.splice(at, 0, POW(1, 'Wypełnienie – 1 powierzchnia'), POW(2, 'Wypełnienie – 2 powierzchnie'), POW(3, 'Wypełnienie – 3 powierzchnie'), naklad);
})();
