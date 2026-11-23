# Przenosi generator Opisów NFZ z obecnej aplikacji (repo opisy-nfz) do wersji SaaS.
# Logika i teksty bez zmian; nakładane są tylko poprawki z listy PATCHES (każda opisana). Wynik: generator/nfz.html,
# generator/szablony.js, generator/wspolne.css. Użycie: python3 tests/tools/przenies_generator.py <ścieżka do opisy-nfz>
# Skrypt kończy się błędem, jeśli którakolwiek poprawka nie pasuje dokładnie raz (zmiana w oryginale = świadoma decyzja).
import os, shutil, subprocess, sys

OLD = os.path.abspath(sys.argv[1])
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'generator')
commit = subprocess.run(['git', '-C', OLD, 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()

PATCHES = [
  ('P1 czcionki lokalnie zamiast Google Fonts (prywatność: brak wysyłania IP do Google; CSP tylko własne zasoby)',
   '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">',
   '<link rel="stylesheet" href="/opisy-nfz/zasoby/fonts.css">'),
  ('P2 tytuł strony w aplikacji Gabinet',
   '<title>Generator opisów NFZ</title>', '<title>Opisy NFZ – Gabinet</title>'),
  ('P3 bez manifestu i ikon wersji statycznej (aplikacja SaaS ma własne)',
   '<link rel="manifest" href="manifest.webmanifest">\n<link rel="icon" href="favicon.svg" type="image/svg+xml">\n<link rel="apple-touch-icon" href="apple-touch-icon.png">\n', ''),
  ('P4 wspólne style z zasobów chronionych logowaniem',
   '<link rel="stylesheet" href="wspolne.css?v=1">', '<link rel="stylesheet" href="/opisy-nfz/zasoby/wspolne.css">'),
  ('P5 wspolne.js (sejf lokalny z hasłem) → gabinet-saas.js (konto SaaS: klucz urządzenia, synchronizacja danych bez treści opisów); dane startowe wstawia serwer w miejsce znacznika',
   '<script src="wspolne.js?v=1"></script>', '<!--GABINET_DANE--><script src="/opisy-nfz/zasoby/gabinet-saas.js"></script>'),
  ('P6 szablony.js z zasobów chronionych logowaniem',
   '<script src="szablony.js?v=2026-11-15-10"></script>', '<script src="/opisy-nfz/zasoby/szablony.js"></script>'),
  ('P7 identyfikator gabinetu: UUID z bazy (36 znaków) zamiast „c1”…„c24” z Kalendarza',
   "gab:typeof x.gab==='string'&&/^[A-Za-z0-9_-]{1,24}$/.test(x.gab)?x.gab:''};",
   "gab:typeof x.gab==='string'&&/^[A-Za-z0-9_-]{1,40}$/.test(x.gab)?x.gab:''};"),
  ('P8 pasek dolny (Historia, Statystyki, Ustawienia): bez kwoty „Dziś: … zł” – zarobki tylko w statystykach (prompt Patryka 21.11.2026, pkt 3.1; obliczenia bez zmian)',
   '<span class="miss">${todayLine()}</span>', '<span class="miss"></span>'),
  ('P9 pasek dolny (Kody): bez kwoty „Dziś: … zł” (pkt 3.1)',
   "const tl=DB.ready&&dbList().some(m=>m.date===todayISO())?' · '+todayLine():'';", "const tl='';"),
  ('P10 pasek dolny (Pytania, Opis): bez wyceny wizyty w zł – wycena zostaje w karcie „Cały opis” i „Rozliczenie wizyty” (pkt 3.1)',
   '+(P.rows.length?` · <span style="color:var(--accent);font-weight:600">${esc(moneyLine(P))}</span>`:\'\')', ''),
  ('P11 badanie po urazie (ST28): przyczyna „nagryzienie na twardy przedmiot” jako osobna opcja (pkt 7.1; trafia do opisu jak pozostałe przyczyny)',
   "opts:['upadek','uderzenie','upadek i nagryzienie na twardy przedmiot']",
   "opts:['upadek','uderzenie','nagryzienie na twardy przedmiot','upadek i nagryzienie na twardy przedmiot']"),
  ('P12 leczenie zachowawcze: opcjonalna informacja o niepewnym rokowaniu (pkt 7.2) – domyślnie nic nie dodaje; wybór użytkownika, tekst edytowalny w kroku 3',
   "  if(ex) f.push(...examFields()); else if(hig){f.push({k:'sh.api',label:'API',type:'num',unit:'%',w:'s'},{k:'sh.gi',label:'GI (Löe–Silness)',type:'num',w:'s'});}\n",
   "  if(ex) f.push(...examFields()); else if(hig){f.push({k:'sh.api',label:'API',type:'num',unit:'%',w:'s'},{k:'sh.gi',label:'GI (Löe–Silness)',type:'num',w:'s'});}\n"
   "  if(state.codes.some(c=>ZACH_CODES.includes(c))) f.push({k:'sh.rok',label:'Niepewne rokowanie zęba (tylko jeśli pacjent został poinformowany)',type:'seg',opts:ROK_OPTS,opt:true,full:true,rer:'shared'});\n"),
  ('P13 niepewne rokowanie: zdanie na końcu opisu ostatniego zabiegu zachowawczego (tylko po wyborze w P12)',
   "function buildOut(){return state.codes.map(c=>({code:c,text:D[c].render()}));}",
   "const ZACH_CODES=GROUPS.find(g=>g[0]==='Leczenie zachowawcze')[1];\n"
   "const ROK_TXT={'pełna informacja':'Pacjent został poinformowany o niepewnym rokowaniu dotyczącym dalszego utrzymania zęba oraz o możliwych dalszych konsekwencjach leczenia.','krótka informacja':'Pacjenta poinformowano o niepewnym rokowaniu leczonego zęba.'};\n"
   "const ROK_OPTS=['nie dotyczy','pełna informacja','krótka informacja'];\n"
   "function buildOut(){const o=state.codes.map(c=>({code:c,text:D[c].render()}));const r=ROK_TXT[str(state.a['sh.rok'])];\n"
   "  if(r){for(let i=o.length-1;i>=0;i--){if(ZACH_CODES.includes(o[i].code)){o[i]={code:o[i].code,text:o[i].text+'\\n'+r};break;}}}\n"
   "  return o;}"),
  ('P14 Statystyki – dni: bez kolumn „Z punktów” i „Z przeglądów” (prompt Patryka 21.11.2026, pkt 3.2; „Razem”, punkty i godziny przeglądów zostają)',
   "{h:'Punkty',r:1},{h:'Z punktów',r:1},{h:'Przeglądy',r:1},{h:'Z przeglądów',r:1},{h:'Dodatkowe',r:1},{h:'Czas wizyt',r:1}];",
   "{h:'Punkty',r:1},{h:'Przeglądy',r:1},{h:'Dodatkowe',r:1},{h:'Czas wizyt',r:1}];"),
  ('P15 Statystyki – dni: wiersze bez kwot „z punktów” i „z przeglądów”',
   "fmtP(A.ptsC/100),fmtC(A.pe),fmtH(A.revHc/100),fmtC(A.rv),fmtC(A.ex),fmtMin(A.min)];",
   "fmtP(A.ptsC/100),fmtH(A.revHc/100),fmtC(A.ex),fmtMin(A.min)];"),
  ('P16 Statystyki – tygodnie: bez kolumn „Z punktów” i „Z przeglądów” (pkt 3.2)',
   "{h:'Wizyty',r:1},{h:'Punkty',r:1},{h:'Z punktów',r:1},{h:'Z przeglądów',r:1},{h:'Dodatkowe',r:1}];",
   "{h:'Wizyty',r:1},{h:'Punkty',r:1},{h:'Dodatkowe',r:1}];"),
  ('P17 Statystyki – tygodnie: wiersze bez tych kwot',
   "A.vis,fmtP(A.ptsC/100),fmtC(A.pe),fmtC(A.rv),fmtC(A.ex)];",
   "A.vis,fmtP(A.ptsC/100),fmtC(A.ex)];"),
  ('P18 Statystyki – miesiące: bez kolumn „Z punktów” i „Z przeglądów” (pkt 3.2)',
   "{h:'Punkty',r:1},{h:'Z punktów',r:1},{h:'Z przeglądów',r:1},{h:'Dodatkowe',r:1},{h:'Czas pracy',r:1}];",
   "{h:'Punkty',r:1},{h:'Dodatkowe',r:1},{h:'Czas pracy',r:1}];"),
  ('P19 Statystyki – miesiące: wiersze bez tych kwot',
   "fmtP(A.ptsC/100),fmtC(A.pe),fmtC(A.rv),fmtC(A.ex),fmtMin(A.work)];",
   "fmtP(A.ptsC/100),fmtC(A.ex),fmtMin(A.work)];"),
  ('P20 lakiery fluorkowe (1101): lista podpowiedzi rozszerzona – Duraphat, Fluor Protector (decyzja Patryka 21.11.2026, pkt 1.1); własna nazwa nadal wpisywana ręcznie',
   "dl:['VOCO Profluorid Varnish']",
   "dl:G.mat('lakier',FLUOR_PREPS)"),
  ('P21 lakierowanie zębów (1006): opcjonalny wybór preparatu – dopisywany do opisu tylko po wybraniu (pkt 1.1); Elmex jako żel (nie lakier)',
   "   render:()=>['LAKIEROWANIE ZĘBÓW (1006)',SEG.T1006].join('\\n')},",
   "   fields:()=>[{k:'1006.prep',label:'Preparat (opcjonalnie – trafi do opisu)',type:'text',dl:G.mat('lakier',FLUOR_PREPS),w:'l',opt:true}],\n"
   "   render:()=>['LAKIEROWANIE ZĘBÓW (1006)',SEG.T1006].concat(str(state.a['1006.prep'])?['Zastosowany preparat: '+str(state.a['1006.prep'])+'.']:[]).join('\\n')},"),
  ('P22 lista preparatów fluorkowych (wspólna dla 1101 i 1006)',
   "const GROUPS=[",
   "const FLUOR_PREPS=['VOCO Profluorid Varnish','Duraphat (Colgate)','Fluor Protector (Ivoclar)','Elmex gelée (żel fluorkowy)'];\nconst GROUPS=["),
  ('P23 nazwa kompozytu: podpowiedzi z „Moich materiałów” (Ustawienia; prompt Patryka 21.11.2026, pkt 1.2) – nadal można wpisać dowolną nazwę',
   "if(m==='kompozyt') f.push({k:p+'name',label:'Nazwa kompozytu',type:'text'});",
   "if(m==='kompozyt') f.push({k:p+'name',label:'Nazwa kompozytu',type:'text',dl:G.mat('kompozyt')});"),
  ('P24 materiał podkładowy (głęboka próchnica): pole przy leczeniu zachowawczym i urazie – domyślnie Ionosit (tekst bez zmian), podpowiedzi z „Moich materiałów” (pkt 1.2)',
   "  if(state.codes.some(c=>ZACH_CODES.includes(c))) f.push({k:'sh.rok',",
   "  if(state.codes.some(c=>ZACH_CODES.includes(c)||c==='ST28')) f.push({k:'sh.pod',label:'Materiał podkładowy (przy próchnicy głębokiej)',type:'text',dl:G.mat('podklad',['Ionosit']),ph:'Ionosit',opt:true});\n"
   "  if(state.codes.some(c=>ZACH_CODES.includes(c))) f.push({k:'sh.rok',"),
  ('P25 materiał podkładowy w opisie: wybrana nazwa zamiast „Ionosit” (puste pole = Ionosit, jak dotąd)',
   "  if(r){for(let i=o.length-1;",
   "  const pod=str(state.a['sh.pod']).trim();if(pod&&pod!=='Ionosit')o.forEach((x,i)=>{o[i]={code:x.code,text:x.text.split('materiał podkładowy Ionosit').join('materiał podkładowy '+pod)};});\n"
   "  if(r){for(let i=o.length-1;"),
  ('P26 wędzidełka: domyślnie „Typ I – śluzówkowy” (decyzja Patryka 21.11.2026, pkt 2.1); zmiana tylko, gdy jest inaczej',
   "function examFields(){return [",
   "function examFields(){['sh.wg','sh.wd'].forEach(k=>{if(state.a[k]===undefined)state.a[k]=WEDZ[0];});return ["),
  ('P27 wywiad: opcjonalne pole „aktualnie przyjmowane leki” (pkt 2.1; tylko w treści opisu na urządzeniu)',
   "  {k:'sh.lk',label:'Przyjmowane leki na stałe',type:'brak'}];}",
   "  {k:'sh.lk',label:'Przyjmowane leki na stałe',type:'brak'},\n  {k:'sh.lka',label:'Aktualnie przyjmowane leki (doraźnie, opcjonalnie)',type:'text',opt:true,w:'l'}];}"),
  ('P28 opis badania: wędzidełka domyślnie Typ I (P26)',
   "'Wędzidełko warg górnej : '+V('sh.wg','wędzidełko górne'),",
   "'Wędzidełko warg górnej : '+(str(state.a['sh.wg'])||WEDZ[0]),"),
  ('P28a opis badania: wędzidełko dolne domyślnie Typ I (P26)',
   "'Wędzidełko warg dolnej: '+V('sh.wd','wędzidełko dolne'),",
   "'Wędzidełko warg dolnej: '+(str(state.a['sh.wd'])||WEDZ[0]),"),
  ('P29 opis badania: linia „Aktualnie przyjmowane leki – …” tylko, gdy wpisano (P27)',
   "'Przyjmowane leki na stałe – '+V('sh.lk','leki')].join('\\n');}",
   "'Przyjmowane leki na stałe – '+V('sh.lk','leki')].concat(str(state.a['sh.lka'])?['Aktualnie przyjmowane leki – '+str(state.a['sh.lka'])]:[]).join('\\n');}"),
  ('P30 przycisk „Wywiad bez obciążeń” – jednym kliknięciem brak alergii, chorób i leków; nie nadpisuje wpisanych (pkt 2.1)',
   '<div class="grid">${f.map(fieldHTML).join(\'\')}</div>${insH}</section>',
   '<div class="grid">${f.map(fieldHTML).join(\'\')}</div>${ex?\'<div class="row" style="margin-top:8px"><button type="button" class="btn ghost sm" data-act="wywbrak">Wywiad bez obciążeń – brak alergii, chorób i leków</button></div>\':\'\'}${insH}</section>'),
  ('P30a obsługa przycisku „Wywiad bez obciążeń”: uzupełnia tylko puste pola',
   "  if(a==='brak'){setVal(el.dataset.key,'brak');afterChange(el);return;}",
   "  if(a==='wywbrak'){['sh.al','sh.ch','sh.lk'].forEach(k=>{if(!str(state.a[k]))setVal(k,'brak');});afterChange(el);return;}\n  if(a==='brak'){setVal(el.dataset.key,'brak');afterChange(el);return;}"),
  ('P31 znieczulenie przy wypełnieniach, endo i ST30 (decyzja Patryka 21.11.2026, pkt 6.3): przyciski Dentocaine / Mark3 / bez znieczulenia + własny preparat; rodzaj i dawka (domyślnie 1 amp., do zmiany); nic nie wybrane = opis bez zmian',
   "  if(state.codes.some(c=>ZACH_CODES.includes(c)||c==='ST28')) f.push({k:'sh.pod',",
   "  if(state.codes.some(c=>AN_CODES.includes(c))){const anP=str(state.a['sh.anw'])||str(state.a['sh.an']);\n"
   "    f.push({k:'sh.an',label:'Znieczulenie – preparat (opcjonalnie)',type:'seg',opts:AN_OPTS,opt:true,full:true,rer:'shared'},{k:'sh.anw',label:'Inny preparat (zamiast przycisku)',type:'text',dl:G.mat('inne',[]),opt:true,w:'l',rer:'shared'});\n"
   "    if(anP&&anP!=='bez znieczulenia'){if(state.a['sh.and']===undefined)state.a['sh.and']=AN_DOSE[1];\n"
   "      f.push({k:'sh.ant',label:'Rodzaj znieczulenia',type:'seg',opts:['nasiękowe','przewodowe','powierzchniowe'],opt:true},{k:'sh.and',label:'Dawka',type:'seg',opts:AN_DOSE,opt:true},{k:'sh.andw',label:'Inna dawka',type:'text',opt:true,w:'s'});}}\n"
   "  if(state.codes.some(c=>ZACH_CODES.includes(c)||c==='ST28')) f.push({k:'sh.pod',"),
  ('P32 znieczulenie w opisie: zdanie zaraz po tytule pierwszego zabiegu z listy (P31); ekstrakcje ST01/ST02 bez zmian (mają własne znieczulenie)',
   "  const pod=str(state.a['sh.pod']).trim();",
   "  {const anP=str(state.a['sh.anw']).trim()||str(state.a['sh.an']),fi=o.findIndex(x=>AN_CODES.includes(x.code));\n"
   "   if(anP&&fi>=0){const ty=str(state.a['sh.ant']),dz=str(state.a['sh.andw']).trim()||str(state.a['sh.and'])||AN_DOSE[1];\n"
   "     const ln=anP==='bez znieczulenia'?'Zabieg wykonano bez znieczulenia.':'Znieczulenie miejscowe'+(ty?' '+ty:'')+': '+anP+', '+dz+'.';\n"
   "     const L=o[fi].text.split('\\n');L.splice(1,0,ln);o[fi]={code:o[fi].code,text:L.join('\\n')};}}\n"
   "  const pod=str(state.a['sh.pod']).trim();"),
  ('P33 stałe znieczuleń (P31–P32)',
   "const ROK_OPTS=['nie dotyczy','pełna informacja','krótka informacja'];",
   "const ROK_OPTS=['nie dotyczy','pełna informacja','krótka informacja'];\n"
   "const AN_CODES=ZACH_CODES.concat(['ST30']);\nconst AN_OPTS=['Dentocaine (40 mg + 0,005 mg)/ml','Mark3 20% benzokaina','bez znieczulenia'];\nconst AN_DOSE=['½ amp. (0,85 ml)','1 amp. (1,7 ml)','2 amp. (3,4 ml)'];"),
  ('P34 zalecenia: przełącznik „ustnie / ustnie i pisemnie” przy każdej wizycie, domyślnie „ustnie” (decyzja Patryka 21.11.2026, pkt 6.5)',
   "  if(state.codes.some(c=>AN_CODES.includes(c))){const anP",
   "  if(state.a['sh.zal']===undefined)state.a['sh.zal']=ZAL_OPTS[0];\n"
   "  f.push({k:'sh.zal',label:'Zalecenia przekazano pacjentowi',type:'seg',opts:ZAL_OPTS,opt:true});\n"
   "  if(state.codes.some(c=>AN_CODES.includes(c))){const anP"),
  ('P35 zalecenia w opisie: przy „ustnie” fraza „ustnie i pisemnie” ze stałych tekstów zamieniona na „ustnie” (stałe teksty w Ustawieniach bez zmian)',
   "  const pod=str(state.a['sh.pod']).trim();",
   "  if((str(state.a['sh.zal'])||ZAL_OPTS[0])==='ustnie')o.forEach((x,i)=>{o[i]={code:x.code,text:x.text.split('ustnie i pisemnie').join('ustnie')};});\n"
   "  const pod=str(state.a['sh.pod']).trim();"),
  ('P36 stałe zaleceń (P34–P35)',
   "const AN_CODES=ZACH_CODES.concat(['ST30']);",
   "const AN_CODES=ZACH_CODES.concat(['ST30']);\nconst ZAL_OPTS=['ustnie','ustnie i pisemnie'];"),
  ('P37 trzy szybkie opcje (decyzja Patryka 21.11.2026, pkt 6.4): kolor wypełnienia, nazwa kompozytu, lakier fluorkowy – 3 najczęściej używane (licznik na tym urządzeniu, bez danych pacjentów; na start: A1/A2/A3 i początek listy); nadal można wpisać własną wartość',
   "${brak}</div>${dl}</div>`;",
   "${brak}</div>${dl}${quickNfz(f)}</div>`;"),
  ('P38 funkcje szybkich opcji NFZ (P37)',
   "function buildOut(){",
   "const QK='gabinet:nfz-szybkie';\n"
   "function qGroup(k){return /[.|]color$/.test(k)?'color':/[.|]name$/.test(k)?'kompozyt':/^(1101|1006)\\.prep$/.test(k)?'lakier':'';}\n"
   "function qCounts(){try{return JSON.parse(localStorage.getItem(QK)||'{}')||{};}catch(e){return {};}}\n"
   "function quickLearn(){const c=qCounts();Object.keys(state.a).forEach(k=>{const g=qGroup(k),x=state.a[k];if(!g||typeof x!=='string'||!x.trim())return;const v=x.trim();c[g]=c[g]||{};c[g][v]=(c[g][v]||0)+1;});try{localStorage.setItem(QK,JSON.stringify(c));}catch(e){}}\n"
   "function quickNfz(f){if(f.type!=='text')return '';const g=qGroup(f.k);if(!g)return '';const c=qCounts()[g]||{},base=g==='color'?['A1','A2','A3']:(f.dl||[]);\n"
   "  const top=[...new Set(Object.keys(c).sort((a,b)=>c[b]-c[a]).concat(base))].slice(0,3);if(!top.length)return '';const cur=str(getVal(f.k));\n"
   "  return '<div class=\"row\" style=\"margin-top:6px;gap:6px\">'+top.map(v=>`<button type=\"button\" class=\"mini${cur===v?' on':''}\" data-act=\"qv\" data-key=\"${esc(f.k)}\" data-v=\"${esc(v)}\" aria-pressed=\"${cur===v}\">${esc(v)}</button>`).join('')+'</div>';}\n"
   "function buildOut(){"),
  ('P39 obsługa szybkich opcji i nauka „najczęściej używanych” przy kopiowaniu opisu',
   "  if(a==='wywbrak'){",
   "  if(a==='qv'){setVal(el.dataset.key,el.dataset.v);afterChange(el);return;}\n  if(a==='wywbrak'){"),
  ('P39a zapamiętanie użytych wartości (kolor, kompozyt, lakier) przy kopiowaniu opisu',
   "  if(a==='copy'||a==='copyall'){const outs=buildOut(),",
   "  if(a==='copy'||a==='copyall'){quickLearn();const outs=buildOut(),"),
  ('P39b wygląd zaznaczonej szybkiej opcji',
   ".mini{font:inherit;font-size:12px;",
   ".mini.on{background:var(--accent);border-color:var(--accent);color:#fff}\n.mini{font:inherit;font-size:12px;"),
  ('P40 podsumowanie na początku opisu (decyzja Patryka 21.11.2026, pkt 6.1): „Wykonano: …” z nazw zaznaczonych zabiegów, zębów i powierzchni; domyślnie włączone, wyłącznik w Ustawieniach; kopiowane razem z opisem',
   "function genTxt(){return buildOut().map(o=>plain(o.text)).join('\\n\\n');}",
   "function sumItem(c){const d=D[c];let s=d.name.charAt(0).toLowerCase()+d.name.slice(1);\n"
   "  if(d.diag&&d.diag.mode!=='quad'){const ts=teethOf(c);if(ts.length)s+=' – '+(ts.length>1?'zęby ':'ząb ')+ts.map(t=>t+(d.diag.mode==='surf'&&surfOf(c,t).length?' ('+SORD.filter(x=>surfOf(c,t).includes(x)).join('')+')':'')).join(', ');}\n"
   "  if(d.diag&&(d.diag.mode==='quad'||d.diag.mode==='mixed')){const q=(state.quads[c]||[]).slice().sort();if(q.length)s+=' – '+(q.length>1?'ćwiartki ':'ćwiartka ')+q.join(', ');}\n"
   "  return s;}\n"
   "function sumPrefix(){if(cfg.sum===false||!state.codes.length)return '';return 'Wykonano: '+state.codes.map(sumItem).join('; ')+'.\\n\\n';}\n"
   "function genTxt(){return sumPrefix()+buildOut().map(o=>plain(o.text)).join('\\n\\n');}"),
  ('P40a podsumowanie także w podglądzie „Cały opis”',
   '<div class="out all">${htmlOut(outs.map(o=>o.text).join(\'\\n\\n\'))}</div>',
   '<div class="out all">${htmlOut(sumPrefix()+outs.map(o=>o.text).join(\'\\n\\n\'))}</div>'),
  ('P40b wyłącznik podsumowania w Ustawieniach modułu',
   "    ${row('Tryb zapisu',",
   "    ${row('Podsumowanie na początku opisu','<div class=\"seg\" role=\"group\"><button type=\"button\" data-act=\"sumopt\" data-v=\"on\" class=\"'+(cfg.sum!==false?'on':'')+'\" aria-pressed=\"'+(cfg.sum!==false)+'\">włączone</button><button type=\"button\" data-act=\"sumopt\" data-v=\"off\" class=\"'+(cfg.sum===false?'on':'')+'\" aria-pressed=\"'+(cfg.sum===false)+'\">wyłączone</button></div>','krótkie „Wykonano: …” z zaznaczonych zabiegów – kopiowane razem z opisem')}\n"
   "    ${row('Tryb zapisu',"),
  ('P40c obsługa wyłącznika podsumowania',
   "  if(a==='basis'){",
   "  if(a==='sumopt'){cfg.sum=el.dataset.v!=='off';cfgSave();render();return;}\n  if(a==='basis'){"),
  ('P30 audyt NFZ R-ST30DG-WIEK (decyzja Patryka D1=B, 22.11.2026): ST30E/ST30G u pacjenta ≥ 18 lat – ostrzeżenie zamiast błędu; bez wpisanego wieku – przypomnienie (źródło: Zarządzenie 60/2023/DSOZ t.j. od 1.09.2026, 95/2026/DSOZ)',
   "  ['ST30E','ST30G'].forEach(c=>{if(has(c)&&a!==null&&a>=18)err.push({codes:[c],msg:`${c}: pakiety profesjonalnej higienizacji (ST30D–ST30G) są przeznaczone dla dzieci i młodzieży do 18 r.ż.`});});",
   "  ['ST30E','ST30G'].forEach(c=>{if(!has(c))return;if(a!==null&&a>=18)warn.push({codes:[c],msg:`${c}: pakiety profesjonalnej higienizacji (ST30D–ST30G) są przeznaczone dla dzieci i młodzieży do 18 r.ż. (Zarządzenie 60/2023/DSOZ t.j. od 1.09.2026, 95/2026/DSOZ). U dorosłych rozlicz ST30 (złogi twarde).`});\n    else if(a===null)warn.push({codes:[c],msg:`${c}: wpisz wiek pacjenta – pakiety ST30D–ST30G tylko do 18 r.ż. (Zarządzenie 60/2023/DSOZ t.j. od 1.09.2026, 95/2026/DSOZ).`});});"),
  ('P31 audyt NFZ R-LAKIER-01: lakierowanie 1006 u pacjenta ≥ 18 lat – ostrzeżenie; bez wieku – przypomnienie (źródło: rozporządzenie koszykowe, t.j. Dz.U. 2025 poz. 615)',
   "  const vt=visitTime(),tot=vt.nfz;",
   "  if(has('1006')){if(a!==null&&a>=18)warn.push({codes:['1006'],msg:'1006: lakierowanie zębów jest świadczeniem gwarantowanym tylko dla dzieci i młodzieży do 18 r.ż. (rozporządzenie MZ, t.j. Dz.U. 2025 poz. 615).'});\n    else if(a===null)warn.push({codes:['1006'],msg:'1006: wpisz wiek pacjenta – lakierowanie tylko do 18 r.ż. (Dz.U. 2025 poz. 615).'});}\n  const vt=visitTime(),tot=vt.nfz;"),
  ('P32 audyt NFZ R-KIR-DZ (decyzja D4=A; aktualizacja 22.11.2026): kiretaż ST04 u dziecka < 15 r.ż. – INFORMACJA „stan sporny” (komunikat Prezesa NFZ nr 627276 z 22.07.2026, pismo NRL z 31.07.2026; źródło: Gazeta Lekarska 9/2026)',
   "  cs.forEach(c=>{if(NFZ_LIMIT[c])warn.push(",
   "  if(has('ST04')&&a!==null&&a<15)warn.push({codes:['ST04'],info:true,msg:'Informacja (stan sporny): NFZ nie zapłaci za kiretaż u dziecka poniżej 15 r.ż. (od 15 r.ż. rozliczany normalnie) – komunikat Prezesa NFZ nr 627276 (22.07.2026), dotyczy świadczeń od 1.01.2026; wyjątek – przypadek udokumentowany i uzasadniony medycznie: wniosek do OW NFZ o indywidualną ocenę. NRL (pismo z 31.07.2026) kwestionuje komunikat jako sprzeczny z rozporządzeniem (zał. 2 bez limitu wieku). Źródło: Gazeta Lekarska 9/2026.'});\n  cs.forEach(c=>{if(NFZ_LIMIT[c])warn.push("),
  ('P33 audyt NFZ R-ZNI-02 (decyzja Patryka 22.11.2026 – ostrzeżenie): znieczulenie wpisane osobno przy ekstrakcji (ST01/ST02) lub kiretażu (ST04) – jest wliczone w pakiet; osobno tylko do wypełnienia, 1105 lub 1206 (źródło: Zarządzenie 60/2023/DSOZ t.j., zał. 1c/1d – lista ST1)',
   "  if(has('ST04')&&a!==null&&a<15)warn.push(",
   "  if(['ST01','ST02','ST04'].some(has)&&Object.keys(PTS_AN).some(k=>parseInt(str(state.a['pt.an'+k]),10)>0))warn.push({codes:['ST01','ST02','ST04'].filter(has),msg:'Znieczulenie przy ekstrakcji i kiretażu jest wliczone w pakiet (Zarządzenie 60/2023/DSOZ t.j. od 1.09.2026, lista ST1). W „znieczulenia rozliczane osobno” wpisz tylko znieczulenia do wypełnień, 1105 lub 1206.'});\n  if(has('ST04')&&a!==null&&a<15)warn.push("),
  ('P34 komunikaty NFZ: INFORMACJA (reguły „wymaga weryfikacji”) wyświetlana jako notatka, nie ostrzeżenie (D4=A)',
   "${hard.map(w=>`<div class=\"warn\">${esc(w.msg)}</div>`).join('')}",
   "${hard.map(w=>`<div class=\"${w.info?'note':'warn'}\">${esc(w.msg)}</div>`).join('')}"),
  ('P35 audyt NFZ N1: dane audytu (generator/nfz-dane.js z data/nfz/, scripts/nfz_dane_przegladarka.py) ładowane razem z szablonami – tylko do odczytu na urządzeniu',
   '<script src="/opisy-nfz/zasoby/szablony.js"></script>',
   '<script src="/opisy-nfz/zasoby/szablony.js"></script>\n<script src="/opisy-nfz/zasoby/nfz-dane.js"></script>'),
  ('P36 audyt NFZ N2: silnik reguł z danych audytu (łączenie spoza tabeli „nie sumuje się”, limity jako informacja – D7=B, przełom roku – D6=A, ocena wg daty wizyty) – tylko na urządzeniu (D2=A)',
   "  return {err,warn,tot,vt};",
   "  nfzAudyt(cs,saveDate()).forEach(x=>{if(x.lvl==='err')err.push({codes:x.codes,msg:x.msg});else warn.push({codes:x.codes,msg:x.msg,info:x.lvl==='info'});});\n  return {err,warn,tot,vt};"),
  ('P36a audyt NFZ N2: funkcje silnika reguł (przed nfzIssues)',
   "function nfzIssues(){",
   "/* ---------- audyt NFZ – etap N2: reguły z data/nfz (window.NFZ_DANE, docs/nfz/) liczone tylko na urządzeniu (D2=A) ----------\n   łączenie: pary z listy audytu, których nie obejmuje NFZ_NOSUM (BLOKADA tylko dla reguł POTWIERDZONYCH);\n   limity zależne od historii – zawsze INFORMACJA (D7=B); rok kalendarzowy + ostrzeżenie na przełomie roku (D6=A);\n   reguła obowiązuje według daty wizyty (od/do). */\nconst NA_KOD=c=>/^ST/.test(c)?c:'23.'+c, Z_KOD=k=>/^23\\./.test(k)?k.slice(3):k;\nfunction nfzRegulaAkt(r,date){return !!r&&(!/^\\d{4}-\\d{2}-\\d{2}$/.test(r.od||'')||r.od<=date)&&(!r.do||date<=r.do);}\nfunction nfzAudyt(cs,date){\n  const N=window.NFZ_DANE,out=[];if(!N||!cs.length)return out;\n  const R={};N.reguly.forEach(r=>{R[r.id]=r;});\n  const kody=cs.map(NA_KOD),seen=new Set(),src=r=>r&&r.zrodla.length?' (źródło: '+r.zrodla[0].split(' – ')[0]+')':'';\n  N.laczenie.forEach(p=>{const i=kody.indexOf(p.a),j=kody.indexOf(p.b);if(i<0||j<0||i===j)return;\n    const key=[p.a,p.b].sort().join('+');if(seen.has(key))return;seen.add(key);\n    const x=Z_KOD(p.a),y=Z_KOD(p.b),r=R[p.regula];if(!nfzRegulaAkt(r,date))return;\n    if((NFZ_NOSUM[x]||[]).includes(y)||(NFZ_NOSUM[y]||[]).includes(x))return;               // już zgłaszane przez tabelę „nie sumuje się”\n    if(p.status==='NIEDOZWOLONE')out.push({lvl:r.poziom==='BLOKADA'&&r.status==='POTWIERDZONA'?'err':'warn',codes:[x,y],msg:`${x} i ${y}: ${r.tresc}${src(r)}`});\n    else if(p.status!=='DOZWOLONE')out.push({lvl:'info',codes:[x,y],msg:`Informacja (${p.status.toLowerCase()}): ${x} + ${y} – ${p.uwagi||r.tresc}`});});\n  const mies=date.slice(5,7),przelom=mies==='12'||mies==='01';let roczny=false;\n  N.limity.forEach(l=>{const c=l.kod.filter(k=>kody.includes(k));if(!c.length)return;const r=R[l.regula];if(!nfzRegulaAkt(r,date))return;\n    if(/w roku|rok kalendarzow/.test(l.tresc))roczny=true;\n    out.push({lvl:'info',codes:c.map(Z_KOD),msg:`Limit NFZ (${c.map(Z_KOD).join(', ')}): ${l.tresc} Sprawdź w historii pacjenta – aplikacja nie zna wizyt z innych gabinetów.`});});\n  if(roczny&&przelom)out.push({lvl:'warn',codes:[],msg:`Przełom roku: limity NFZ liczone są w roku kalendarzowym – ta wizyta (${date}) liczy się do limitów roku ${date.slice(0,4)}.`});\n  return out;\n}\nfunction nfzIssues(){"),
  ('P37 audyt NFZ N2: rozwijana lista „Zasady NFZ dla wybranych kodów” (treść, poziom, status, źródło) pod komunikatami NFZ',
   "function nfzBox(){",
   'function nfzZasadyHTML(){\n  const N=window.NFZ_DANE;if(!N||!state.codes.length)return \'\';const date=saveDate(),kody=state.codes.map(NA_KOD);\n  const rs=N.reguly.filter(r=>r.dotyczy.some(k=>kody.includes(k))&&nfzRegulaAkt(r,date));if(!rs.length)return \'\';\n  return `<details class="nfz-zas" style="font-size:13.5px"><summary>Zasady NFZ dla wybranych kodów (${rs.length}) – dane audytu ${esc(N.wersja)}</summary><ul>${rs.map(r=>`<li><b>${esc(r.poziom.toLowerCase())}</b>${r.decyzja?` <span class="sub-n" style="display:inline">(audyt: ${esc(r.poziom_audyt.toLowerCase())} – ${esc(r.decyzja)})</span>`:\'\'} · ${esc(r.tresc)}<span class="sub-n" style="display:block;font-size:12px">${esc(r.id)} · ${esc(r.status.toLowerCase())} · od ${esc(r.od)} · ${esc(r.zrodla.map(z=>z.split(\' – \')[0]).join(\'; \'))}</span></li>`).join(\'\')}</ul><div class="nfz-src">${esc(N.uwaga)}</div></details>`;\n}\nfunction nfzBox(){'),
  ('P37a lista zasad NFZ widoczna także bez błędów i ostrzeżeń',
   "  if(!err.length&&!hard.length&&!timeLine) return '<div id=\"nfz-box\"></div>';",
   "  const zas=nfzZasadyHTML();\n  if(!err.length&&!hard.length&&!timeLine&&!zas) return '<div id=\"nfz-box\"></div>';"),
  ('P37b lista zasad NFZ na końcu okienka komunikatów',
   "${err.length||hard.length?`<div class=\"nfz-src\">${esc(NFZ_SRC)}</div>`:''}</div>`;",
   "${err.length||hard.length?`<div class=\"nfz-src\">${esc(NFZ_SRC)}</div>`:''}${zas}</div>`;"),
  ('P38 audyt NFZ N5 (D3=A): rozpoznanie ICD-10 wybrane przez lekarza z podpowiedzi pokazywane przy kodzie i w tabeli (domyślnie jak dotąd)',
   "const icdOf=c=>typeof D[c].icd==='function'?D[c].icd():D[c].icd;",
   "const icdOf0=c=>typeof D[c].icd==='function'?D[c].icd():D[c].icd;\nconst icdOf=c=>{const w=str(state.a[c+'.icd10']);return w?w+' (wybrane)':icdOf0(c);};"),
  ('P39 audyt NFZ N5: podpowiedzi ICD-10 z mapowań audytu w karcie każdej procedury (pakiet → procedury kierunkowe; brak podkodu → kod nadrzędny)',
   "function renderStep2(){return linkBanner()+nfzBox()+sharedCard()+state.codes.map(cardHTML).join('')+ptsExtraCard();}",
   'function icdSug(c){const N=window.NFZ_DANE;if(!N)return [];const P=N.podpowiedzi_icd10,seen=new Set(),out=[];\n  const src=/^ST/.test(c)?(N.pakiety[c]||[]):[\'23.\'+c];\n  src.forEach(k=>{let q=k;while(q.length>5&&!P[q])q=q.slice(0,-1);(P[q]||[]).forEach(x=>{if(seen.has(x.k))return;seen.add(x.k);out.push(Object.assign({n:(N.icd10[x.k]||{}).n||\'\'},x));});});\n  return out;}\nfunction icdSugHTML(c){const L=icdSug(c);if(!L.length)return \'\';const w=str(state.a[c+\'.icd10\']),op=ui.icdOpen&&ui.icdOpen[c];\n  return `<details class="icd-sug"${op?\' open\':\'\'}><summary>Podpowiedzi ICD-10 (${L.length}) – wybiera lekarz</summary><div class="chips">${L.map(x=>`<button type="button" class="chip" data-act="icd10" data-c="${esc(c)}" data-v="${esc(x.k)}" aria-pressed="${w===x.k}" title="${esc(x.u||\'\')}">${esc(x.k)} ${esc(x.n)}</button>`).join(\'\')}</div><p class="note" style="margin:6px 0 0">Nazwy robocze z audytu NFZ (do porównania z wydaniem CeZ). NFZ nie narzuca pary procedura–rozpoznanie. Wybór pokazuje się przy kodzie i w tabeli – nie zmienia treści opisu ani wyceny; zostaje na tym urządzeniu.</p></details>`;}\nfunction renderStep2(){'+"return linkBanner()+nfzBox()+sharedCard()+state.codes.map(c=>cardHTML(c).replace(/<\\/section>\\s*$/,icdSugHTML(c)+'</section>')).join('')+ptsExtraCard();}"),
  ('P40 audyt NFZ N5: wybór / odznaczenie podpowiedzi ICD-10',
   "  if(a==='rmcode'){state.codes.splice(state.codes.indexOf(el.dataset.c),1);render();return;}",
   "  if(a==='rmcode'){state.codes.splice(state.codes.indexOf(el.dataset.c),1);render();return;}\n  if(a==='icd10'){const k=el.dataset.c+'.icd10';state.a[k]=str(state.a[k])===el.dataset.v?'':el.dataset.v;ui.icdOpen=Object.assign({},ui.icdOpen,{[el.dataset.c]:true});render();return;}"),
  ('P41 baza stomatologiczna (I1): dane checklist (generator/baza-dane.js z data/, scripts/baza_dane_przegladarka.py) ładowane w Opisach NFZ – tylko do odczytu',
   '<script src="/opisy-nfz/zasoby/nfz-dane.js"></script>',
   '<script src="/opisy-nfz/zasoby/nfz-dane.js"></script>\n<script src="/opisy-nfz/zasoby/baza-dane.js"></script>'),
  ('P42 baza stomatologiczna (I1): funkcje kontroli kompletności dokumentacji (ostrzeżenie bez blokady – decyzja Patryka 22.11.2026)',
   "function renderStep3(){",
   '/* ---------- baza stomatologiczna (integracja I1): kontrola kompletności dokumentacji – ostrzeżenie, bez blokady (decyzja Patryka 22.11.2026) ----------\n   Elementy z checklist kart (data/procedury-icd9, generator/baza-dane.js). Automatycznie sprawdzane: zęby / ćwiartki na diagramie, wiek, data, opis,\n   rozpoznanie, lekarz; pozostałe – „do sprawdzenia” przez lekarza. Nie zmienia treści opisu ani wyceny. */\nfunction bazaAuto(e,c){\n  const id=e.id||\'\',pole=e.pole||\'\';\n  if(id===\'CHK-W-DATA\')return [true,\'data wizyty: \'+saveDate()];\n  if(id===\'CHK-W-OPIS\')return [true,\'opis generowany z formularza\'];\n  if(id===\'CHK-W-LEKARZ\')return [true,\'z konta lekarza\'];\n  if(id===\'CHK-W-ROZPOZNANIE\'){const t=str(icdOf(c));return t?[true,t]:[false,\'brak rozpoznania\'];}\n  if(id===\'CHK-W-ZAB-ISO\'||pole===\'POLE-ZAB\'||pole===\'POLE-ZEBY\'||pole===\'POLE-LUK\'||pole===\'POLE-LOKALIZACJA\'){\n    if(!D[c]||!D[c].diag)return [null,\'\'];const n=teethOf(c).length+(state.quads[c]||[]).length;return n?[true,\'zaznaczono na diagramie\']:[false,\'nie zaznaczono zębów / ćwiartek\'];}\n  if(pole===\'POLE-WIEK\')return AGE()!==null?[true,\'wiek: \'+AGE()]:[false,\'nie wpisano wieku\'];\n  return [null,\'\'];}\nfunction bazaChk(){\n  const B=window.BAZA_DANE;if(!B)return [];\n  return state.codes.filter(c=>B.kody[c]).map(c=>{const k=B.kody[c];\n    const el=k.wspolne.map(w=>Object.assign({id:w},B.wspolne[w])).concat(k.elementy).filter(e=>e&&e.tekst);\n    return {c,k,el:el.map(e=>{const [ok,info]=bazaAuto(e,c);return {e,ok,info,warn:ok===false&&(e.poziom===\'obowiazkowe\'||e.poziom===\'rozliczeniowe\')};})};});}\nfunction bazaChkHTML(){\n  const L=bazaChk();if(!L.length)return \'\';const n=L.reduce((s,x)=>s+x.el.filter(i=>i.warn).length,0);\n  const POZ={obowiazkowe:\'obowiązkowe\',zalecane:\'zalecane\',sytuacyjne:\'zależne od sytuacji\',rozliczeniowe:\'rozliczenie NFZ\'};\n  return `<details class="card baza-chk" data-testid="baza-chk"${n?\' open\':\'\'}><summary><b>Kontrola kompletności dokumentacji</b> – ${n?`<span style="color:var(--warn)">${n} do uzupełnienia</span>`:\'bez braków wykrytych automatycznie\'} <span class="note">(baza wiedzy – wersja robocza, tylko ostrzeżenie)</span></summary>${L.map(x=>`<div style="margin:8px 0"><b class="code">${esc(x.c)}</b> ${esc(x.k.nazwa)} <span class="note">karta ${esc(x.k.kod)} – ${x.k.status===\'verified\'?\'zweryfikowana\':\'do weryfikacji\'}</span><ul style="margin:4px 0 0;padding-left:20px">${x.el.map(i=>`<li${i.warn?\' class="warn-li" style="color:var(--warn)"\':\'\'}>${i.ok===true?\'✓\':i.ok===false?\'⚠\':\'☐\'} ${esc(i.e.tekst)} <span class="note">[${esc(POZ[i.e.poziom]||i.e.poziom)}${i.e.warunek?\' – \'+esc(i.e.warunek):\'\'}]${i.info?\' – \'+esc(i.info):\'\'}</span></li>`).join(\'\')}</ul></div>`).join(\'\')}<p class="note" style="margin:6px 0 0">✓ sprawdzone automatycznie · ⚠ brak (tylko ostrzeżenie – zapis możliwy) · ☐ do sprawdzenia przez lekarza. Pełne karty: <a href="/katalog-procedur" target="_blank" rel="noopener">Katalog procedur</a>.</p></details>`;}\nfunction renderStep3(){'),
  ('P42a kontrola kompletności w kroku 3 (Opis) – przed opisem; treść opisu i wycena bez zmian',
   "  return nfzBox()+all+ptsCard()+sum2+each;",
   "  return nfzBox()+bazaChkHTML()+all+ptsCard()+sum2+each;"),
  ('P43 opis z karty procedury (etap I2, decyzja Patryka 22.11.2026): dane kart zweryfikowanych (generator/karty-opisy.js) i okienko (generator/opis-z-karty.js) – tylko na urządzeniu',
   '<script src="/opisy-nfz/zasoby/baza-dane.js"></script>',
   '<script src="/opisy-nfz/zasoby/baza-dane.js"></script>\n<script src="/opisy-nfz/zasoby/karty-opisy.js"></script>\n<script src="/opisy-nfz/zasoby/opis-z-karty.js"></script>'),
  ('P43a przycisk „Opis z karty” obok „Edytuj tekst” (krok 3) – generator opisu NFZ bez zmian',
   '<button type="button" class="btn ghost sm" data-act="edtxt" id="edTxtBtn">Edytuj tekst</button>',
   '<button type="button" class="btn ghost sm" data-act="edtxt" id="edTxtBtn">Edytuj tekst</button>${window.OpisZKarty?OpisZKarty.przycisk(\'btn ghost sm\'):\'\'}'),
  ('P43b przycisk „Opis z karty” także w trybie edycji tekstu',
   '<button type="button" class="btn ghost sm" data-act="regen" id="regenBtn">Wygeneruj tekst z formularza</button>',
   '<button type="button" class="btn ghost sm" data-act="regen" id="regenBtn">Wygeneruj tekst z formularza</button>${window.OpisZKarty?OpisZKarty.przycisk(\'btn ghost sm\'):\'\'}'),
  ('P43c wstawienie: tekst z karty dopisany na końcu opisu jako edycja ręczna (state.ed) – zapis, szkic i historia jak przy „Edytuj tekst”',
   "function fullTxt(){return state.ed?state.ed.txt:genTxt();}",
   "function fullTxt(){return state.ed?state.ed.txt:genTxt();}\n"
   "if(window.OpisZKarty)OpisZKarty.podlacz({moze:()=>state.codes.length&&state.step===3?true:'Najpierw wybierz zabiegi i przejdź do opisu.',"
   "wstaw:t=>{const g=genTxt();if(!state.ed)state.ed={txt:g,gen:g};state.ed.txt=String(state.ed.txt||'').replace(/\\s+$/,'')+(state.ed.txt?'\\n\\n':'')+t;render();autoSave();refreshSave();draftSched();}});"),
  ('P44 ST30D i ST30F w Opisach NFZ (decyzja Patryka 22.11.2026, 1A): profesjonalna higienizacja z instruktażem – ½ łuku (66 pkt) i całe uzębienie (138 pkt); zał. 1c/1d – Zarządzenie 95/2026/DSOZ; komunikaty Centrali NFZ z 23.09.2026 i 9.11.2026',
   " ST26:{name:'Leczenie zmian na błonie śluzowej',",
   " ST30D:{name:'Profesjonalna higienizacja z instruktażem – ½ łuku',icd:'K03.6 + Z01.2',tips:['z badaniem lekarskim i instruktażem higieny (23.0101)','NFZ: 1× w roku kalendarzowym – badanie z instruktażem 1× w roku (zamiast ST33)','1 pakiet = ½ łuku = 1 ćwiartka; pozostałe ćwiartki jako ST30E (przy ST30D maks. 3)','dla dzieci i młodzieży do 18 r.ż.'],exam:true,instr:true,\n"
   "   diag:{mode:'quad',label:'Kliknij ząb w ćwiartce, z której usunięto złogi miękkie (ST30D = 1 ćwiartka; pozostałe zaznacz w ST30E)'},\n"
   "   fields:()=>[{k:'ST30D.czas',label:'Czas procedury (min. NFZ '+nfzMin('ST30D')+' min)',type:'num',unit:'min',w:'s'}],\n"
   "   render:()=>{const q=(state.quads.ST30D||[]).slice().sort();const rem=SEG.ST30G_REMOVAL.replace('w kwadrantach jamy ustnej – zgodnie z diagramem','w kwadrancie jamy ustnej '+(q.length?q.join(', '):MISS('ćwiartka (diagram)'))+' – zgodnie z diagramem');\n"
   "     return ['PROFESJONALNA HIGIENIZACJA Z INSTRUKTAŻEM HIGIENY ½ ŁUKU ZĘBOWEGO (ST30D)','Badanie lekarskie stomatologiczne, które obejmuje również instruktaż higieny jamy ustnej;',SEG.ST30G_EXAM_A,examMid(),SEG.EXAM_B,rem,'Czas wykonania procedury '+V('ST30D.czas','czas')+' min.',SEG.INSTR_HEAD,instr()].join('\\n');}},\n"
   " ST30F:{name:'Profesjonalna higienizacja z instruktażem – całe uzębienie',icd:'K03.6 + Z01.2',tips:['z badaniem lekarskim i instruktażem higieny (23.0101)','NFZ: 1× w roku kalendarzowym – badanie z instruktażem 1× w roku (zamiast ST33)','do ST30F można dosumować tylko 1101','dla dzieci i młodzieży do 18 r.ż.'],exam:true,instr:true,\n"
   "   fields:()=>[{k:'ST30F.czas',label:'Czas procedury (min. NFZ '+nfzMin('ST30F')+' min)',type:'num',unit:'min',w:'s'}],\n"
   "   render:()=>['PROFESJONALNA HIGIENIZACJA Z INSTRUKTAŻEM HIGIENY CAŁE UZĘBIENIE (ST30F)','Usunięcie złogów nazębnych miękkich. Badanie lekarskie stomatologiczne, które obejmuje również instruktaż higieny jamy ustnej;',SEG.ST30G_EXAM_A,examMid(),SEG.EXAM_B,SEG.ST30G_REMOVAL,'Czas wykonania procedury '+V('ST30F.czas','czas')+' min.',SEG.INSTR_HEAD,instr()].join('\\n')},\n"
   " ST26:{name:'Leczenie zmian na błonie śluzowej',"),
  ('P44a ST30G zgodnie z nazwą pakietu – BEZ instruktażu (decyzja Patryka 22.11.2026, 2A): usunięta sekcja instruktażu z opisu; z instruktażem = ST30F',
   "ST30G:{name:'Profesjonalna higienizacja – całe uzębienie',icd:'K03.6 + Z01.2',tips:['dokładny diagram','dla dzieci i młodzieży do 18 r.ż.'],exam:true,instr:true,",
   "ST30G:{name:'Profesjonalna higienizacja – całe uzębienie (bez instruktażu)',icd:'K03.6 + Z01.2',tips:['bez instruktażu higieny – z instruktażem rozlicz ST30F (138 pkt)','dokładny diagram','dla dzieci i młodzieży do 18 r.ż.'],exam:true,"),
  ('P44b ST30G – opis bez sekcji instruktażu higieny',
   "'Czas wykonania procedury '+V('ST30G.czas','czas')+' min.',SEG.INSTR_HEAD,instr()].join('\\n')}",
   "'Czas wykonania procedury '+V('ST30G.czas','czas')+' min.'].join('\\n')}"),
  ('P44c ST30D i ST30F na liście kodów (Profilaktyka i higienizacja) i domyślny czas',
   " ['Profilaktyka i higienizacja',['ST30','ST30G','ST30E','1101','1006']],",
   " ['Profilaktyka i higienizacja',['ST30','ST30F','ST30G','ST30D','ST30E','1101','1006']],"),
  ('P44d czas minimalny, „nie sumuje się” i „dosumować wyłącznie” dla ST30D / ST30F (zał. 1d – Zarządzenie 95/2026/DSOZ)',
   "const NFZ_MIN={ST30:10,ST30E:5,ST30G:20};",
   "const NFZ_MIN={ST30:10,ST30D:15,ST30E:5,ST30F:30,ST30G:20};\n"
   "const NFZ_ONLY={ST30D:['ST30E','1101'],ST30F:['1101']};   // zał. 1d: „do świadczenia można dosumować wyłącznie…”"),
  ('P44e limity roczne ST30D / ST30F / ST33 – badanie z instruktażem (23.0101) 1× w roku kalendarzowym (komunikat Centrali NFZ 9.11.2026)',
   "const NFZ_LIMIT={ST30E:'max 4× w roku',ST30G:'max 1× w roku',ST33:'1× w roku kalendarzowym'};",
   "const NFZ_LIMIT={ST30D:'1× w roku kalendarzowym – zawiera badanie z instruktażem (23.0101); jeśli w tym roku był ST33 lub ST30F, NFZ nie zapłaci',ST30E:'max 4× w roku (3×, jeśli w tym roku był ST30D)',ST30F:'1× w roku kalendarzowym – zawiera badanie z instruktażem (23.0101); jeśli w tym roku był ST33 lub ST30D, NFZ nie zapłaci',ST30G:'max 1× w roku',ST33:'1× w roku kalendarzowym – jeśli w tym roku był ST30D lub ST30F (zawierają badanie z instruktażem), NFZ nie zapłaci'};"),
  ('P44f wycena: ST30D 66 pkt, ST30F 138 pkt (zał. 1c – Zarządzenie 95/2026/DSOZ)',
   "const PTS={ST01:93,ST02:104,ST04:130,ST19:86,ST26:51,ST28:96,ST30:44,ST30E:24,ST30G:96,",
   "const PTS={ST01:93,ST02:104,ST04:130,ST19:86,ST26:51,ST28:96,ST30:44,ST30D:66,ST30E:24,ST30F:138,ST30G:96,"),
  ('P44g jednostka ST30D (½ łuku = 1 ćwiartka)',
   "const PTS_UNIT={ST01:'ząb',ST02:'ząb',ST30:'ćwiartka',ST30E:'ćwiartka',",
   "const PTS_UNIT={ST01:'ząb',ST02:'ząb',ST30:'ćwiartka',ST30D:'ćwiartka',ST30E:'ćwiartka',"),
  ('P44h ostrzeżenia ST30D / ST30F: wiek < 18, „dosumować wyłącznie”, ST30D = 1 ćwiartka, maks. 3 × ST30E przy ST30D, podpowiedź 1× ST30D + ST30E, ST30G bez instruktażu',
   "  ['ST30E','ST30G'].forEach(c=>{if(!has(c))return;if(a!==null&&a>=18)",
   "  Object.keys(NFZ_ONLY).forEach(c=>{if(!has(c))return;const zle=cs.filter(o=>o!==c&&!NFZ_ONLY[c].includes(o)&&!((NFZ_NOSUM[c]||[]).includes(o)));\n"
   "    if(zle.length)err.push({codes:[c,...zle],msg:`${c}: NFZ nie zapłaci – do ${c} można dosumować wyłącznie ${NFZ_ONLY[c].join(' i ')} (zał. 1d, Zarządzenie 95/2026/DSOZ). Usuń: ${zle.join(', ')}.`});});\n"
   "  if(has('ST30D')){const q=(state.quads.ST30D||[]).length,qe=(state.quads.ST30E||[]).length;\n"
   "    if(q>1)warn.push({codes:['ST30D'],msg:'ST30D obejmuje ½ łuku (1 ćwiartkę) – pozostałe ćwiartki zaznacz w ST30E (komunikat Centrali NFZ 23.09.2026).'});\n"
   "    if(has('ST30E')&&qe>3)warn.push({codes:['ST30D','ST30E'],msg:`Przy ST30D NFZ zapłaci maks. za 3 × ST30E w roku – zaznaczono ${qe} ćwiartki ST30E.`});}\n"
   "  if(has('ST30E')&&!has('ST30D')&&!has('ST33'))warn.push({codes:['ST30E'],info:true,msg:'Jeśli na wizycie był instruktaż higieny: NFZ zaleca 1× ST30D (½ łuku z badaniem i instruktażem, 66 pkt) + pozostałe ćwiartki jako ST30E (komunikat Centrali NFZ 23.09.2026).'});\n"
   "  if(has('ST30G'))warn.push({codes:['ST30G'],info:true,msg:'ST30G jest bez instruktażu higieny – jeśli był instruktaż, rozlicz ST30F (138 pkt zamiast 96; zał. 1c, Zarządzenie 95/2026/DSOZ).'});\n"
   "  ['ST30D','ST30E','ST30F','ST30G'].forEach(c=>{if(!has(c))return;if(a!==null&&a>=18)"),
  ('P44i domyślny czas ST30D 16 min i ST30F 31 min (jak ST30E/ST30G: minimum NFZ + 1 min)',
   "state.a['ST30E.czas']='11';",
   "state.a['ST30E.czas']='11'; state.a['ST30D.czas']='16'; state.a['ST30F.czas']='31';"),
]

PATCHES_PRYW = [
  ('R1 bez manifestu i ikon wersji statycznej',
   '<link rel="manifest" href="manifest.webmanifest">\n<link rel="icon" href="favicon.svg" type="image/svg+xml">\n<link rel="apple-touch-icon" href="apple-touch-icon.png">\n', ''),
  ('R2 czcionki lokalnie zamiast Google Fonts',
   '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">',
   '<link rel="stylesheet" href="/opisy-nfz/zasoby/fonts.css">'),
  ('R3 wspólne style z zasobów chronionych logowaniem',
   '<link rel="stylesheet" href="wspolne.css?v=1">', '<link rel="stylesheet" href="/opisy-nfz/zasoby/wspolne.css">'),
  ('R4 wspolne.js → gabinet-saas.js (konto SaaS, klucz urządzenia, synchronizacja bez treści, pól szablonu, e-ZLA i inicjałów)',
   '<script src="wspolne.js?v=1"></script>', '<!--GABINET_DANE--><script src="/opisy-nfz/zasoby/gabinet-saas.js"></script>'),
  ('R5 katalog procedur z zasobów chronionych logowaniem',
   '<script src="prywatne-katalog.js?v=1"></script>', '<script src="/opisy-nfz/zasoby/prywatne-katalog.js"></script>'),
  ('R6 historia: wpis z innego urządzenia (z chmury) – komunikat, że treść jest na urządzeniu zapisu (zamiast „usunięta”)',
   "'<span class=\"pw-note\">treść opisu usunięta (ustawienie prywatności)</span>'",
   "'<span class=\"pw-note\">' + (m.cloud ? 'treść opisu jest tylko na urządzeniu, na którym zapisano wizytę' : 'treść opisu usunięta (ustawienie prywatności)') + '</span>'"),
  ('R7 historia: brak treści opisu na tym urządzeniu – czytelny komunikat zamiast „Wczytuję…” bez końca (prompt Patryka 21.11.2026, etap 5: „opisy nie zawsze się wyświetlają”)',
   "const S = { ready: false, tab: 'wiz', visits: new Map(), bodies: new Map(), allBodies: false,",
   "const S = { ready: false, tab: 'wiz', visits: new Map(), bodies: new Map(), bodyMiss: new Set(), allBodies: false,"),
  ('R7a odczyt treści: zapamiętanie, że treści nie ma (zamiast ponownego „Wczytuję…”)',
   "  if (b) S.bodies.set(id, b); return b;",
   "  if (b) { S.bodies.set(id, b); S.bodyMiss.delete(id); } else S.bodyMiss.add(id); return b;"),
  ('R7b „Pokaż opis”: komunikat o braku treści na tym urządzeniu',
   "esc(b ? b.txt : 'Wczytuję…')",
   "esc(b ? b.txt : S.bodyMiss.has(m.id) ? 'Treści tego opisu nie ma na tym urządzeniu (zapisano ją w innej przeglądarce albo usunięto dane witryny). Kwoty i procedury są zachowane; treść przywrócisz z „Kopii danych z tego urządzenia” (Konto).' : 'Wczytuję…')"),
  ('R7c „Kopiuj opis” bez treści na urządzeniu: konkretny komunikat zamiast „Nie udało się skopiować”',
   "toast(ok ? 'Skopiowano opis: ' + whoOf(m) : 'Nie udało się skopiować.')",
   "toast(ok ? 'Skopiowano opis: ' + whoOf(m) : b ? 'Nie udało się skopiować.' : 'Treści tego opisu nie ma na tym urządzeniu.')"),
  ('R8 podpowiedzi materiałów w szablonach: lista wbudowana + „Moje materiały” z konta (prompt Patryka 21.11.2026, pkt 1.2); pola: materiał wypełnienia, podkład, materiał w zębodole',
   "  $('#dls').innerHTML = KAT.proc.map(p => (p.fields || []).filter(f => f.sug).map(f => '<datalist id=\"dl_' + p.id + '_' + f.k + '\">' + f.sug.map(",
   "  const sugOf = qSug;\n"
   "  $('#dls').innerHTML = KAT.proc.map(p => (p.fields || []).filter(f => sugOf(f).length).map(f => '<datalist id=\"dl_' + p.id + '_' + f.k + '\">' + sugOf(f).map("),
  ('R8a pole „Materiał w zębodole” też z podpowiedziami „Moich materiałów”',
   "(f.sug ? ' list=\"dl_' + esc(procOf(it).id) + '_' + f.k + '\"' : '')",
   "(f.sug || f.k === 'matz' ? ' list=\"dl_' + esc(procOf(it).id) + '_' + f.k + '\"' : '')"),
  ('R9 zalecenia ustne (decyzja Patryka 21.11.2026, pkt 6.5): „Zalecenia przekazano pacjentowi w formie ustnej.” na końcu opisu wizyty – domyślnie tak, do wyłączenia przy wizycie',
   "  if (S.ust.podpis) parts.push(String(S.ust.podpis));",
   "  if (v.items.length && v.zalUst !== false) parts.push('Zalecenia przekazano pacjentowi w formie ustnej.');\n  if (S.ust.podpis) parts.push(String(S.ust.podpis));"),
  ('R9a pole wyboru przy wizycie (obok e-ZLA)',
   "'<section class=\"g-card\"><label class=\"pw-bool\"><input type=\"checkbox\" id=\"ez_on\"'",
   "'<section class=\"g-card\"><label class=\"pw-bool\"><input type=\"checkbox\" id=\"zal_ust\"' + (V.zalUst !== false ? ' checked' : '') + '> Zalecenia przekazano pacjentowi w formie ustnej (dopisz do opisu)</label><label class=\"pw-bool\"><input type=\"checkbox\" id=\"ez_on\"'"),
  ('R9b obsługa pola „zalecenia ustne”',
   "  if (t.id === 'ez_on') {",
   "  if (t.id === 'zal_ust') { V.zalUst = t.checked; render(); draftSched(); return; }\n  if (t.id === 'ez_on') {"),
  ('R10 szybkie opcje (pkt 6.2–6.4): 3 najczęściej używane wartości z historii jako przyciski (materiały, środek znieczulający); 5 dolegliwości do klikania przy wywiadzie (zachowawcze, endo, diagnostyka); dawka znieczulenia ½ / 1 / 2 amp. (domyślnie 1 amp. = 1,7 ml); zawsze można wpisać własną wartość',
   "  return '<div class=\"pw-f' + wide + '\">' + h + '</div>';",
   "  h += quickHTML(it, i, f);\n  return '<div class=\"pw-f' + wide + '\">' + h + '</div>';"),
  ('R10a funkcje szybkich opcji i podpowiedzi (wspólne dla datalist i przycisków)',
   "function fieldHTML(it, i, f) {",
   "const QMAT = { mat: ['kompozyt', 'inne'], podklad: ['podklad'], matz: ['inne'] }, QBASE = { znprep: ['Dentocaine (artykaina 4% z adrenaliną 1:100 000)', 'Mark3 20% benzokaina (żel)'] };\n"
   "const DOLEGL = ['ból samoistny', 'ból na zimno/ciepło', 'ból przy nagryzaniu', 'nadwrażliwość', 'ukruszenie/złamanie zęba (lub wypełnienia)'];\n"
   "const ZN_DOSE = [['0,85', '½ amp. (0,85 ml)'], ['1,7', '1 amp. (1,7 ml)'], ['3,4', '2 amp. (3,4 ml)']];\n"
   "function qSug(f) { const base = (QBASE[f.k] || []).concat(f.sug || []); const all = (QMAT[f.k] ? G.mat(QMAT[f.k], []) : []).concat(base); return all.filter((x, j) => all.indexOf(x) === j); }   // własne materiały przed wbudowanymi\n"
   "function quickTop(k, list) { const c = new Map(); for (const m of S.visits.values()) for (const x of (m.items || [])) { const v = x.vals && x.vals[k]; if (typeof v === 'string' && v.trim()) c.set(v.trim(), (c.get(v.trim()) || 0) + 1); }\n"
   "  return [...new Set([...c.keys()].sort((a, b) => c.get(b) - c.get(a)).concat(list))].slice(0, 3); }\n"
   "function quickHTML(it, i, f) {\n"
   "  const p = procOf(it), v = it.vals[f.k], b = (a, val, lab, on) => '<button type=\"button\" class=\"pw-ib pw-qb' + (on ? ' on' : '') + '\" data-a=\"' + a + '\" data-i=\"' + i + '\" data-k=\"' + esc(f.k) + '\" data-v=\"' + esc(val) + '\" aria-pressed=\"' + !!on + '\">' + esc(lab) + '</button>';\n"
   "  let q = [];\n"
   "  if (f.k === 'wywiad' && ['zach', 'endo', 'diag'].includes(p.kat)) { const cur = String(v || '').split(',').map(x => x.trim()); q = DOLEGL.map(d => b('qtog', d, d, cur.includes(d))); }\n"
   "  else if (f.k === 'zndawka') { const zn = it.vals.zn; if (!zn || zn === 'nie stosowano') return ''; if (v === undefined || v === '') it.vals[f.k] = '1,7'; q = ZN_DOSE.map(d => b('qset', d[0], d[1], String(it.vals[f.k]) === d[0])); }\n"
   "  else if (f.t !== 'area' && f.t !== 'multi' && f.t !== 'select' && f.t !== 'bool' && f.t !== 'rows' && f.t !== 'num' && f.t !== 'date' && f.t !== 'tooth' && f.t !== 'teeth') { const l = qSug(f); if (l.length) q = quickTop(f.k, l).map(x => b('qset', x, x, v === x)); }\n"
   "  return q.length ? '<div class=\"pw-q\">' + q.join('') + '</div>' : ''; }\n"
   "function fieldHTML(it, i, f) {"),
  ('R10b obsługa przycisków szybkich opcji',
   "  if (a === 'fold') { it.fold = !it.fold; rerenderItem(i); return; }",
   "  if (a === 'qset' || a === 'qtog') { const k = t.dataset.k, val = t.dataset.v;\n"
   "    if (a === 'qset') it.vals[k] = val; else { const cur = String(it.vals[k] || '').split(',').map(x => x.trim()).filter(Boolean), j = cur.indexOf(val); if (j >= 0) cur.splice(j, 1); else cur.push(val); it.vals[k] = cur.join(', '); }\n"
   "    rerenderItem(i); refreshSide(); draftSched(); return; }\n"
   "  if (a === 'fold') { it.fold = !it.fold; rerenderItem(i); return; }"),
  ('R10c wygląd przycisków szybkich opcji',
   ".pw-toast{",
   ".pw-q{display:flex;flex-wrap:wrap;gap:6px;margin-top:6px}.pw-qb.on{background:var(--g-accent);border-color:var(--g-accent);color:var(--g-accent-ink)}\n.pw-toast{"),
  ('R11 podsumowanie na początku opisu (decyzja Patryka 21.11.2026, pkt 6.1): „Wykonano: …” z procedur wizyty i zębów; domyślnie włączone, wyłącznik w Ustawieniach',
   "function visitText(v) {\n  v = v || V; const parts = v.items.map(itemText).filter(Boolean);",
   "function sumP(it) { const p = procOf(it), n = String(p.name || ''), z = fieldsOf(p); let s = n.charAt(0).toLowerCase() + n.slice(1);\n"
   "  for (const f of z.values()) if ((f.t === 'tooth' || f.t === 'teeth') && it.vals[f.k]) { const ts = String(it.vals[f.k]); s += ' – ' + (/[,;]/.test(ts) ? 'zęby ' : 'ząb ') + ts; break; }\n"
   "  return s + (it.qty > 1 ? ' ×' + it.qty : ''); }\n"
   "function visitText(v) {\n  v = v || V; const parts = v.items.map(itemText).filter(Boolean);\n"
   "  if (v.items.length && S.ust.sum !== false) parts.unshift('Wykonano: ' + v.items.map(sumP).join('; ') + '.');"),
  ('R11a wyłącznik podsumowania w Ustawieniach (obok podpisu)',
   "    '<input class=\"pw-in\" id=\"u_podpis\" maxlength=\"120\" value=\"' + esc(S.ust.podpis || '') + '\" style=\"max-width:480px\"></section>' +",
   "    '<input class=\"pw-in\" id=\"u_podpis\" maxlength=\"120\" value=\"' + esc(S.ust.podpis || '') + '\" style=\"max-width:480px\"></section>' +\n"
   "    '<section class=\"g-card\"><h2>Podsumowanie na początku opisu</h2><label class=\"pw-bool\"><input type=\"checkbox\" id=\"u_sum\"' + (S.ust.sum !== false ? ' checked' : '') + '> Dodawaj „Wykonano: …” (procedury i zęby) na początku każdego opisu</label></section>' +"),
  ('R11b obsługa wyłącznika podsumowania',
   "  if (t.id === 'zal_ust') {",
   "  if (t.id === 'u_sum') { S.ust.sum = t.checked; ustSave(); render(); return; }\n  if (t.id === 'zal_ust') {"),
  ('R12 bezpiecznik startu (zgłoszenie Patryka 21.11.2026: „czasem zostaje Wczytuję…”, zwłaszcza po przejściu z Opisów NFZ): po 8 s bez gotowości – informacja i „Odśwież”; za pierwszym razem samo odświeżenie (najwyżej raz na minutę)',
   "async function init() {\n  await G.ready('prywatne');",
   "function startGuard() {\n"
   "  setTimeout(() => { if (S.ready) return; let last = 0; try { last = +sessionStorage.getItem('pryw:odswiez') || 0; } catch (e) { }\n"
   "    if (Date.now() - last > 60000) { try { sessionStorage.setItem('pryw:odswiez', String(Date.now())); } catch (e) { } location.reload(); return; }\n"
   "    $('#main').innerHTML = '<div class=\"g-err\" role=\"alert\">Wczytywanie Opisów prywatnych trwa dłużej niż zwykle (przeglądarka nie udostępnia lokalnej bazy). Dane są bezpieczne. <button type=\"button\" class=\"g-btn sm\" onclick=\"location.reload()\">Odśwież</button> – jeśli nie pomoże, zamknij inne karty z Gabinetem.</div>'; }, 8000);\n"
   "}\n"
   "async function init() {\n  startGuard();\n  await G.ready('prywatne');"),
  ('R13 opis z karty procedury (etap I2, decyzja Patryka 22.11.2026): dane kart zweryfikowanych i okienko – tylko na urządzeniu',
   '<script src="/opisy-nfz/zasoby/prywatne-katalog.js"></script>',
   '<script src="/opisy-nfz/zasoby/prywatne-katalog.js"></script>\n<script src="/opisy-nfz/zasoby/karty-opisy.js"></script>\n<script src="/opisy-nfz/zasoby/opis-z-karty.js"></script>'),
  ('R13a przycisk „Opis z karty” obok „Edytuj tekst” / „Wygeneruj tekst z formularza”',
   "'<button type=\"button\" class=\"g-btn ghost sm\" data-a=\"new\" id=\"b_new\">Nowa wizyta</button></div>'",
   "(window.OpisZKarty ? OpisZKarty.przycisk('g-btn ghost sm') : '') + '<button type=\"button\" class=\"g-btn ghost sm\" data-a=\"new\" id=\"b_new\">Nowa wizyta</button></div>'"),
  ('R13b wstawienie: tekst z karty dopisany na końcu opisu jako edycja ręczna (V.edited) – zapis i szkic jak przy „Edytuj tekst”',
   "const curText = () => V.edited && typeof V.txt === 'string' ? V.txt : visitText();",
   "const curText = () => V.edited && typeof V.txt === 'string' ? V.txt : visitText();\n"
   "if (window.OpisZKarty) OpisZKarty.podlacz({ moze: () => V.items.length ? true : 'Najpierw dodaj procedurę do wizyty.',\n"
   "  wstaw: t => { if (!V.edited) { V.edited = true; V.txt = visitText(); V.genAtEdit = V.txt; } V.txt = String(V.txt || '').replace(/\\s+$/, '') + (V.txt ? '\\n\\n' : '') + t; refreshSide(); draftSched(); } });"),
  ('R14 karty procedur do klikania (etap K1, decyzja Patryka 22.11.2026): 144 karty zweryfikowane jako procedury w Opisach prywatnych (generator/prywatne-karty.js – tylko na urządzeniu)',
   '<script src="/opisy-nfz/zasoby/opis-z-karty.js"></script>',
   '<script src="/opisy-nfz/zasoby/opis-z-karty.js"></script>\n<script src="/opisy-nfz/zasoby/prywatne-karty.js"></script>'),
  ('R14a tekst procedury z karty: szablon standardowy karty + blok dokumentacyjny (rozpoznanie, znieczulenie z dawką, powikłania, informacja i zgoda); puste obowiązkowe → [UZUPEŁNIJ]',
   "function itemText(it) {\n  const p = procOf(it), fm = fieldsOf(p), vals = it.vals || {};\n",
   "function itemText(it) {\n  const p = procOf(it), fm = fieldsOf(p), vals = it.vals || {};\n"
   "  if (p.ktpl && window.KartyPryw) return tidy(KartyPryw.tekst(p, k => { const f = fm.get(k); return f && visible(f, vals) ? fmtVal(f, vals[k]) : ''; }, k => (fm.get(k) || {}).l || k,\n"
   "    k => { const f = fm.get(k); return !!(f && f.req && visible(f, vals)); }, k => vals[k]));\n"),
  ('R14b zapis wersji szablonu karty w wizycie (otwarcie z historii odtwarza ten sam tekst)',
   "def: { name: d.name, kat: d.kat, fields: d.fields || [], tpl: d.tpl || '', ver: d._ver || d.ver || 1 } };",
   "def: { name: d.name, kat: d.kat, fields: d.fields || [], tpl: d.tpl || '', ver: d._ver || d.ver || 1, ktpl: d.ktpl, karta: d.karta, zab: d.zab } };"),
  ('R14c zdanie o informacji / zgodzie pacjenta przy kilku procedurach z kart – w opisie wizyty tylko raz',
   "  v = v || V; const parts = v.items.map(itemText).filter(Boolean);\n",
   "  v = v || V; let parts = v.items.map(itemText).filter(Boolean); if (window.KartyPryw) parts = KartyPryw.dedupe(parts);\n"),
  ('R14d podpowiedzi rozpoznania z karty liczone tylko z wizyt tej samej procedury (nie podpowiada próchnicy przy ekstrakcji)',
   "function quickTop(k, list) { const c = new Map(); for (const m of S.visits.values()) for (const x of (m.items || [])) { const v = x.vals && x.vals[k];",
   "function quickTop(k, list, pid) { const c = new Map(); for (const m of S.visits.values()) for (const x of (m.items || [])) { if (pid && x.pid !== pid) continue; const v = x.vals && x.vals[k];"),
  ('R14e wywołanie podpowiedzi z identyfikatorem procedury (pola z kart)',
   "if (l.length) q = quickTop(f.k, l).map(",
   "if (l.length) q = quickTop(f.k, l, f.qloc ? it.pid : null).map("),
  ('R14f Szablony: karty procedur bez edycji i duplikowania (tekst z bazy kart zweryfikowanych) – ulubione i ukrywanie działają',
   """<button type="button" class="pw-ib" data-a="tedit" data-id="' + p.id + '">Edytuj</button><button type="button" class="pw-ib" data-a="tdup" data-id="' + p.id + '">Duplikuj</button>' +""",
   """' + (p.karta ? '<span class="pw-tag">karta ' + esc(p.karta) + ' – tekst z bazy kart</span>' : '<button type="button" class="pw-ib" data-a="tedit" data-id="' + p.id + '">Edytuj</button><button type="button" class="pw-ib" data-a="tdup" data-id="' + p.id + '">Duplikuj</button>') +"""),
  ('R14g karty: Dentocaine wpisywane samo przy znieczuleniu iniekcyjnym (decyzja Patryka 22.11.2026: „tylko Dentocaine”), jak dawka 1,7 ml – do zmiany; przy powierzchniowym nic',
   "function fieldHTML(it, i, f) {\n  const id = 'f_' + it.u + '_' + f.k, v = it.vals[f.k],",
   "function fieldHTML(it, i, f) {\n  if (f.k === 'znprep' && procOf(it).karta && it.vals.zn && !['nie stosowano', 'powierzchniowe'].includes(it.vals.zn) && it.vals[f.k] === undefined) it.vals[f.k] = QBASE.znprep[0];   // przed rysowaniem pola – widać od razu\n  const id = 'f_' + it.u + '_' + f.k, v = it.vals[f.k],"),
  ('R15 warianty leczenia zachowawczego (prompt Patryka 23.11.2026, pkt 4): 1, 2, 3 powierzchnie i nakład jako osobne procedury z ceną w Cenniku (generator/prywatne-warianty.js)',
   '<script src="/opisy-nfz/zasoby/prywatne-katalog.js"></script>\n<script src="/opisy-nfz/zasoby/karty-opisy.js"></script>',
   '<script src="/opisy-nfz/zasoby/prywatne-katalog.js"></script>\n<script src="/opisy-nfz/zasoby/prywatne-warianty.js"></script>\n<script src="/opisy-nfz/zasoby/karty-opisy.js"></script>'),
  ('R16 błąd „0 zł lekarza” (prompt Patryka 23.11.2026, pkt 6): brak % w Cenniku → % gabinetu z „Gabinety” (modele procentowe); % zapisywany w pozycji wizyty (zmiana % później nie przelicza historii)',
   "  return { c: e.c != null ? e.c : null, m: own === 'kw' ? 'kw' : 'pct', p: own === 'kw' ? null : own === 'pct' ? e.p : (g.pct != null ? g.pct : null), kw: own === 'kw' ? (e.kw || 0) : null };\n}",
   "  return { c: e.c != null ? e.c : null, m: own === 'kw' ? 'kw' : 'pct', p: own === 'kw' ? null : own === 'pct' ? e.p : (g.pct != null ? g.pct : clinicPct(gab)), kw: own === 'kw' ? (e.kw || 0) : null };\n}\n"
   "function clinicPct(gab) {                                         // % gabinetu z „Gabinety” (model procentowy); godzinowy / dzienny / bez gabinetu – brak %\n"
   "  const k = (S.clinics || []).find(x => x.id === gab); return k && /^pct/.test(k.model || '') && k.pct != null && !isNaN(+k.pct) ? +k.pct : null; }"),
  ('R16a komunikat o braku % – wskazuje oba miejsca ustawienia (Cennik albo Gabinety) i gabinety godzinowe/dzienne',
   "' – ustaw domyślny % gabinetu w zakładce Cennik.</div>'",
   "' – ustaw % w zakładce Cennik albo model procentowy gabinetu w „Gabinety” (gabinet godzinowy / dzienny lub wizyta bez gabinetu: wynagrodzenie z dyżuru w Kalendarzu).</div>'"),
  ('R17 diagnostyka i odporność startu (prompt Patryka 23.11.2026, pkt 9): bezpiecznik po 15 s (jedno ponowne otwarcie bazy mieści się przed przeładowaniem), komunikat z etapem, na którym start stanął; etapy modułu w G.etap',
   " Dane są bezpieczne. <button type=\"button\" class=\"g-btn sm\" onclick=\"location.reload()\">Odśwież</button> – jeśli nie pomoże, zamknij inne karty z Gabinetem.</div>'; }, 8000);",
   " Dane są bezpieczne. <button type=\"button\" class=\"g-btn sm\" onclick=\"location.reload()\">Odśwież</button> – jeśli nie pomoże, zamknij inne karty z Gabinetem.<br><span class=\"g-small\" data-testid=\"start-etap\">Etap: ' + esc(G.etapNow || 'start') + '</span></div>'; try { console.warn('[Gabinet] start Opisów prywatnych stanął', G.etapy); } catch (e) { } }, 15000);"),
  ('R17a etapy startu modułu (dane modułu → gotowe)',
   "  await G.ready('prywatne');\n  uiLoad();",
   "  await G.ready('prywatne');\n  G.etap('dane Opisów prywatnych');\n  uiLoad();"),
  ('R17b etap: gotowe',
   "  await autoPurge();\n  S.ready = true;",
   "  await autoPurge();\n  S.ready = true; G.etap('gotowe');"),
]

PATCHES_KAL = [
  ('K1 bez ikon i manifestu wersji statycznej',
   '<link rel="icon" href="favicon.svg" type="image/svg+xml">\n<link rel="apple-touch-icon" href="apple-touch-icon.png">\n<link rel="manifest" href="manifest.webmanifest">\n', ''),
  ('K2 czcionki lokalnie zamiast Google Fonts',
   '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">',
   '<link rel="stylesheet" href="/opisy-nfz/zasoby/fonts.css">'),
  ('K3 wspólne style z zasobów chronionych logowaniem',
   '<link rel="stylesheet" href="wspolne.css?v=1">', '<link rel="stylesheet" href="/opisy-nfz/zasoby/wspolne.css">'),
  ('K4 wspolne.js → gabinet-saas.js (konto SaaS: dokumenty Kalendarza na koncie, gabinety wspólne z całą aplikacją, sumy z opisów z serwera)',
   '<script src="wspolne.js?v=1"></script>', '<!--GABINET_DANE--><script src="/opisy-nfz/zasoby/gabinet-saas.js"></script>'),
  ('K5 identyfikator gabinetu domyślnego: UUID (wspólna tabela gabinetów) zamiast „c1”…',
   "return { id: 'c' + (i + 1), name: 'Gabinet ' + (i + 1),", "return { id: crypto.randomUUID(), name: 'Gabinet ' + (i + 1),"),
  ('K6 identyfikator nowego gabinetu: UUID zamiast „c…”',
   "var c = defClinic(cs.length); c.id = 'c' + uid(); c.color = color;", "var c = defClinic(cs.length); c.id = crypto.randomUUID(); c.color = color;"),
  ('K7 notatka dyżuru zapisuje się na koncie – przypomnienie, żeby nie wpisywać danych pacjentów',
   '<label class="f">Notatka<input type="text" id="f-note"', '<label class="f">Notatka (bez danych pacjentów)<input type="text" id="f-note"'),
  ('K8 status zapisu w nagłówku: bez „zaszyfrowane, na tym urządzeniu” (dane Kalendarza są na koncie; stan wysyłki pokazuje pasek aplikacji)',
   "saved: 'Zapisano (zaszyfrowane)', local: 'Zaszyfrowane, na tym urządzeniu' }", "saved: 'Zapisano', local: 'Zapisano' }"),
  ('K9 opis „Dane” w Ustawieniach: dane Kalendarza są na koncie Gabinet (nie „tylko w tej przeglądarce”)',
   "'Dane są zapisane tylko w tej przeglądarce, na tym urządzeniu – nikt inny ich nie widzi i nie trafiają na żaden serwer. Rób co jakiś czas kopię (.json): Safari na iPhonie usuwa dane stron nieotwieranych przez 7 dni używania przeglądarki; po dodaniu aplikacji do ekranu początkowego („Udostępnij” → „Do ekranu początk.”) ten limit jej nie dotyczy.'",
   "'Dane Kalendarza (dyżury, kwoty, koszty, kursy, ustawienia) są zapisane na Twoim koncie Gabinet – widzisz je tylko Ty, na każdym urządzeniu po zalogowaniu. Gabinety są wspólne z całą aplikacją (zakładka „Gabinety”). Nie wpisuj tu danych pacjentów.'"),
  ('K10 „Usuń wszystkie dane” usuwa dyżury, kursy i ustawienia Kalendarza, ale nie gabinety (wspólne z Opisami i Zarobkami – usuwa się je w „Gabinety”)',
   "'reset-do': function () { Object.keys(Store.docs).forEach(function (k) { Store.remove(k); }); UI.ask = null;",
   "'reset-do': function () { var keep = S().clinics; Object.keys(Store.docs).forEach(function (k) { Store.remove(k); }); var ns = defaultSettings(); ns.clinics = keep; Store.docs.settings = normalizeSettings(ns); Store.touch('settings'); UI.ask = null;"),
  ('K11 pytanie przed usunięciem danych Kalendarza: gabinety zostają',
   "'<span class=\"confirm\">Usunąć wszystkie dyżury i ustawienia? ", "'<span class=\"confirm\">Usunąć wszystkie dyżury, kursy i ustawienia Kalendarza? Gabinety zostają. "),
  ('K12 zmiany z innego urządzenia (scalone na koncie) od razu w otwartym Kalendarzu – bez nadpisywania pola, które właśnie edytujesz',
   'function setSync(s) { Store.sync = s; renderHeader(); }',
   'function setSync(s) { Store.sync = s; renderHeader(); }\nwindow.addEventListener(\'gabinet:grafik\', function (e) {\n  var d = e.detail || {};\n  Object.keys(d).forEach(function (k) { if (Store.isDirty(k)) return; if (d[k]) Store.docs[k] = d[k]; else delete Store.docs[k]; });\n  if (Store.docs.settings) normalizeSettings(Store.docs.settings);\n  invalidate(); renderWhenIdle();\n});'),
  ('K13 nazwa modelu rozliczenia: „% po odjęciu kosztów własnych” (decyzja Patryka 21.11.2026; logika bez zmian)',
   "pct_lab: '% po odjęciu labu/implantów'", "pct_lab: '% po odjęciu kosztów własnych'"),
  ('K14 domyślne ustawienia bez założeń o użytkowniku (decyzja Patryka 21.11.2026): pusty start JDG, brak formy opodatkowania i okresów ZUS – wybiera użytkownik (kreator K16)',
   "jdgStart: '2026-10', regimes: { 2026: 'skala', 2027: 'ryczalt' }, ryczaltRate: 14,\n    uop: {}, kwotaJDG: true, zus: [{ id: 'z1', from: '2026-10', variant: 'custom', amount: 800, base: 0, chor: true }],",
   "jdgStart: '', regimes: {}, ryczaltRate: 14,\n    uop: {}, kwotaJDG: true, zus: [],"),
  ('K15 bez ustawionych podatków i ZUS nie pokazujemy „netto ≈” ani „odłóż” (zamiast wyniku liczonego z cudzych założeń); taxReady() = start JDG + forma + okres ZUS',
   "function reserveRatio(mk) {\n  var o = monthRes(mk, 'fcst');",
   "function curYear() { return +todayStr().slice(0, 4); }\nfunction taxReady() { var s = S(); return /^\\d{4}-\\d{2}$/.test(s.jdgStart || '') && Object.keys(s.regimes || {}).length > 0 && Array.isArray(s.zus) && s.zus.length > 0; }\nfunction taxNote(tag) { return '<' + (tag || 'div') + ' class=\"note\" data-tax-todo>Ustaw <b>podatki i ZUS</b> – wtedy policzę netto i kwoty do odłożenia. <button class=\"btn sm\" data-a=\"wiz-open\">Ustaw teraz</button></' + (tag || 'div') + '>'; }\nfunction reserveRatio(mk) {\n  if (!taxReady()) return null;\n  var o = monthRes(mk, 'fcst');"),
  ('K15a podsumowanie miesiąca bez ustawień podatków: zaproszenie do kreatora zamiast „JDG nieaktywna (start: )”',
   "  if (!a.active) return '<div class=\"note\">JDG nieaktywna w tym miesiącu (start: ' + esc(S().jdgStart) + ').</div>';",
   "  if (!a.active) return taxReady() ? '<div class=\"note\">JDG nieaktywna w tym miesiącu (start: ' + esc(S().jdgStart) + ').</div>' : taxNote();"),
  ('K15b pasek miesiąca bez ustawień podatków: zaproszenie do kreatora',
   "  if (!a.active) return '<span class=\"muted\">JDG nieaktywna w tym miesiącu (start: ' + esc(S().jdgStart) + ')</span>';",
   "  if (!a.active) return taxReady() ? '<span class=\"muted\">JDG nieaktywna w tym miesiącu (start: ' + esc(S().jdgStart) + ')</span>' : '<span class=\"muted\">Ustaw podatki i ZUS, żeby liczyć netto</span>';"),
  ('K15c Podsumowanie bez ustawień podatków: zaproszenie do kreatora',
   "  if (!a.active) h += '<div class=\"note\">W tym miesiącu JDG nie była aktywna (start: ' + esc(S().jdgStart) + '). Datę zmienisz w Ustawieniach → Podatek.</div>';",
   "  if (!a.active) h += taxReady() ? '<div class=\"note\">W tym miesiącu JDG nie była aktywna (start: ' + esc(S().jdgStart) + '). Datę zmienisz w Ustawieniach → Podatek.</div>' : taxNote();"),
  ('K15d tydzień: „Netto ≈” tylko przy ustawionych podatkach i ZUS',
   "['Netto ≈', zl0(n.net), '']",
   "['Netto ≈', taxReady() ? zl0(n.net) : '—', taxReady() ? '' : 'ustaw podatki i ZUS']"),
  ('K16 kreator „Ustaw podatki i ZUS” przy pierwszym otwarciu (3 pytania, bez wartości z góry; można pominąć i wrócić)',
   "function nudges() {\n  if (!UI.loaded) return '<div class=\"note\">Wczytuję Twoje dane…</div>';\n  var out = [], todo = todoShifts();",
   "function wizard() {\n  var cy = curYear(), opt = function (o) { return Object.keys(o).map(function (k) { return '<option value=\"' + k + '\">' + o[k] + '</option>'; }).join(''); };\n  return '<div class=\"card\" id=\"wiz\" style=\"margin-bottom:12px\"><h3 style=\"margin-top:0\">Ustaw podatki i ZUS</h3><p class=\"small muted\">Z tego policzę netto, kwoty do odłożenia i terminy. Niczego nie zakładam z góry – zmienisz to w każdej chwili w Ustawieniach.</p><div class=\"frow\">' +\n    '<label class=\"f\">1. Od kiedy prowadzisz JDG<input type=\"month\" id=\"wiz-start\"><span class=\"hint\">miesiąc rozpoczęcia lub wznowienia</span></label>' +\n    '<label class=\"f\">2. Forma opodatkowania w ' + cy + '<select id=\"wiz-reg\"><option value=\"\">— wybierz —</option>' + opt(REGIMES) + '</select></label>' +\n    '<label class=\"f\">Od ' + (cy + 1) + ' (opcjonalnie)<select id=\"wiz-reg2\"><option value=\"\">bez zmiany</option>' + opt(REGIMES) + '</select></label>' +\n    '<label class=\"f\">3. Składki społeczne ZUS<select id=\"wiz-zus\"><option value=\"\">— wybierz —</option>' + opt(ZUSV) + '</select></label>' +\n    '<label class=\"f\">Kwota (zł)<input type=\"text\" inputmode=\"decimal\" id=\"wiz-amt\"><span class=\"hint\">„z eZUS”: miesięczne społeczne · „własna podstawa”: podstawa wymiaru</span></label>' +\n    '<label class=\"chk\" style=\"align-self:end\"><input type=\"checkbox\" id=\"wiz-chor\"> chorobowe (dobrowolne)</label></div>' +\n    '<div class=\"row\"><button class=\"btn primary\" data-a=\"wiz-save\">Zapisz</button><button class=\"btn ghost\" data-a=\"wiz-skip\">Pomiń na razie</button></div></div>';\n}\nfunction nudges() {\n  if (!UI.loaded) return '<div class=\"note\">Wczytuję Twoje dane…</div>';\n  var out = [], todo = todoShifts();\n  if (Store.mode !== 'demo' && (UI.wiz || (!taxReady() && !S().setup.wizSkip))) out.push(wizard());\n  else if (Store.mode !== 'demo' && !taxReady()) out.push('<button class=\"nudge accent\" data-a=\"wiz-open\"><b>Ustaw podatki i ZUS</b> – wtedy policzę netto i kwoty do odłożenia</button>');"),
  ('K16a akcje kreatora i „Ustaw od nowa” (czyści tylko ustawienia podatków i ZUS – po potwierdzeniu; dyżury, gabinety, koszty i kursy zostają)',
   "  'uop-calc': function () {",
   "  'wiz-open': function () { UI.wiz = true; UI.tab = 'cal'; UI.edit = null; render(); window.scrollTo(0, 0); },\n  'wiz-skip': function () { S().setup.wizSkip = true; UI.wiz = false; saveSettings(); render(); },\n  'wiz-save': function () {\n    var v = function (id) { return (document.getElementById(id) || {}).value || ''; };\n    var st = v('wiz-start'), r = v('wiz-reg'), r2 = v('wiz-reg2'), zv = v('wiz-zus'), amt = num(v('wiz-amt'));\n    if (!/^\\d{4}-\\d{2}$/.test(st)) return toast('Podaj miesiąc startu JDG');\n    if (!REGIMES[r]) return toast('Wybierz formę opodatkowania');\n    if (!ZUSV[zv]) return toast('Wybierz wariant składek ZUS');\n    if ((zv === 'custom' || zv === 'base') && !(amt > 0)) return toast(zv === 'custom' ? 'Wpisz miesięczną kwotę społecznych z eZUS' : 'Wpisz podstawę wymiaru');\n    var s = S(), cy = curYear(), y0 = +st.slice(0, 4), b = Math.max(y0, cy);\n    s.jdgStart = st; s.regimes = {}; s.regimes[y0] = r; s.regimes[b] = r; if (r2 && r2 !== r) s.regimes[b + 1] = r2;\n    s.zus = [{ id: uid(), from: st, variant: zv, amount: zv === 'custom' ? amt : 0, base: zv === 'base' ? amt : 0, chor: !!(document.getElementById('wiz-chor') || {}).checked }];\n    s.setup.zus = true; s.setup.wizSkip = false; UI.wiz = false; saveSettings(); render(); toast('Zapisano – netto liczę wg Twoich ustawień');\n  },\n  'tax-reset-ask': function () { UI.taxReset = true; render(); },\n  'tax-reset-no': function () { UI.taxReset = false; render(); },\n  'tax-reset-do': function () {\n    var s = S(); s.jdgStart = ''; s.regimes = {}; s.zus = []; s.uop = {}; s.wakacje = {}; s.annualOverride = {}; s.params = {}; s.healthMode = 'auto'; s.ryczaltRate = 14; s.kwotaJDG = true;\n    s.setup.zus = false; s.setup.uop = false; s.setup.wizSkip = false; UI.taxReset = false; saveSettings(); ACT['wiz-open'](); toast('Wyczyszczono ustawienia podatków i ZUS – ustaw je od nowa');\n  },\n  'uop-calc': function () {"),
  ('K17 przycisk „Ustaw od nowa” w Ustawieniach → Działalność i podatek (z potwierdzeniem)',
   "'<section class=\"set-sec\" id=\"sec-tax\"><h2>Działalność i podatek</h2><div class=\"card\"><div class=\"frow\">' +",
   "'<section class=\"set-sec\" id=\"sec-tax\"><h2>Działalność i podatek</h2>' + (UI.taxReset ? '<div class=\"confirm\" data-tax-reset>Wyczyścić ustawienia podatków i ZUS (start JDG, formę opodatkowania, okresy ZUS, wakacje składkowe, dochód z etatu, parametry lat, prognozę przychodu)? Dyżury, gabinety, koszty i kursy zostają. <button class=\"btn sm danger\" data-a=\"tax-reset-do\">Tak, wyczyść</button><button class=\"btn sm\" data-a=\"tax-reset-no\">Nie</button></div>' : '<div class=\"row\" style=\"margin-bottom:10px\"><button class=\"btn ghost\" data-a=\"wiz-open\">Kreator: ustaw podatki i ZUS</button><button class=\"btn ghost danger\" data-a=\"tax-reset-ask\">Ustaw od nowa (wyczyść)</button></div>') + '<div class=\"card\"><div class=\"frow\">' +"),
  ('K18 opis pola startu JDG – ogólny (nie tylko wznowienie)',
   "Start JDG (wznowienie)", "Start JDG (lub wznowienie)"),
  ('K19 etat: bieżący rok zamiast stałego 2026 (Ustawienia, pomocnik, pierwsze kroki)',
   "'<div class=\"card\"><h3>Etat w 2026 (skala)</h3><div class=\"frow\">' + fld('Dochód z etatu 2026 (zł)', 'uop-2026', 'uop.2026', (s.uop || {})[2026], { num: 1, hint: 'przychód − koszty − Twoje składki społeczne (PIT-11)' }) +\n    '<label class=\"f\">Pomocnik: brutto z etatu w 2026<input",
   "'<div class=\"card\"><h3>Etat w ' + curYear() + ' (skala, jeśli masz)</h3><div class=\"frow\">' + fld('Dochód z etatu ' + curYear() + ' (zł)', 'uop-' + curYear(), 'uop.' + curYear(), (s.uop || {})[curYear()], { num: 1, hint: 'przychód − koszty − Twoje składki społeczne (PIT-11)' }) +\n    '<label class=\"f\">Pomocnik: brutto z etatu w ' + curYear() + '<input"),
  ('K19a pomocnik etatu zapisuje bieżący rok',
   "s.uop = s.uop || {}; s.uop[2026] = v;", "s.uop = s.uop || {}; s.uop[curYear()] = v;"),
  ('K19b pierwsze kroki: „Podatki i ZUS” (kreator) zamiast „Kwota ZUS z eZUS”; etat bieżącego roku i opcjonalny',
   "['Kwota ZUS z eZUS', 'set', 'sec-zus', !!s.setup.zus],\n    ['Dochód z etatu 2026', 'set', 'sec-tax', !!s.setup.uop || (num((s.uop || {})[2026]) || 0) > 0],",
   "['Podatki i ZUS', 'wiz', '', taxReady() && !!s.setup.zus],\n    ['Dochód z etatu (jeśli masz)', 'set', 'sec-tax', !!s.setup.uop || (num((s.uop || {})[curYear()]) || 0) > 0],"),
  ('K19c pierwsze kroki: krok „wiz” otwiera kreator',
   "var act = x[1] === 'tpl' ? 'data-a=\"tpl-open\"' :", "var act = x[1] === 'tpl' ? 'data-a=\"tpl-open\"' : x[1] === 'wiz' ? 'data-a=\"wiz-open\"' :"),
  ('K20 koszty firmowe: opis ogólny zamiast planu jednej osoby (skala do końca 2026)',
   "<p>Na skali (do końca 2026) koszty obniżają podatek i zdrowotną. Na ryczałcie zmniejszają tylko Twoje netto – dlatego większe zakupy warto rozważyć jeszcze w 2026 (potwierdź z księgową).</p>",
   "<p>Na skali i podatku liniowym koszty obniżają podatek i zdrowotną. Na ryczałcie nie obniżają podatku – zmniejszają tylko Twoje netto (szczegóły potwierdź z księgową).</p>"),
  ('K21 „+ Dodaj okres” ZUS przy pustej liście: od startu JDG (albo bieżącego miesiąca), wariant do wyboru',
   "var s = S(), last = s.zus[s.zus.length - 1]; s.zus.push({ id: uid(), from: mkAdd(last && last.from ? last.from : s.jdgStart, 12), variant: 'full',",
   "var s = S(), last = s.zus[s.zus.length - 1]; s.zus.push({ id: uid(), from: last && last.from ? mkAdd(last.from, 12) : (s.jdgStart || mkOf(todayStr())), variant: last ? 'full' : 'custom',"),
  ('K22 przykład (demo) z własnymi, oznaczonymi wartościami podatków – domyślne są puste',
   "s.setup = { clinics: true, zus: true, uop: true, grid: true }; s.uop = { 2026: 85000 };",
   "s.setup = { clinics: true, zus: true, uop: true, grid: true }; s.uop = {}; s.uop[curYear()] = 85000;\n  s.jdgStart = (curYear() - 1) + '-01'; s.regimes = {}; s.regimes[curYear() - 1] = 'skala'; s.zus = [{ id: 'z1', from: s.jdgStart, variant: 'custom', amount: 1600, base: 0, chor: true }];"),
  ('K23 domyślnie zero gabinetów (decyzja Patryka 21.11.2026): wcześniej puste konto dostawało 4 przykładowe gabinety z UUID, które przy pierwszym zapisie ustawień trafiały do tabeli gabinetów konta',
   "  return { v: 1, clinics: [0, 1, 2, 3].map(defClinic), jdgStart:",
   "  return { v: 1, clinics: [], jdgStart:"),
  ('K23a pusta lista gabinetów zostaje pusta (bez dopełniania przykładowymi)',
   "  if (!Array.isArray(s.clinics) || !s.clinics.length) s.clinics = d.clinics;",
   "  if (!Array.isArray(s.clinics)) s.clinics = [];"),
  ('K23b przykład (demo) tworzy własne 4 gabinety przykładowe',
   "  var s = defaultSettings(), names = [",
   "  var s = defaultSettings(); s.clinics = [0, 1, 2, 3].map(defClinic); var names = ["),
  ('K24 zachęta „Dodaj pierwszy gabinet” (Gabinety w aplikacji) zamiast „Ustaw dni pracy”, gdy konto nie ma gabinetów',
   "  if (Store.mode !== 'demo' && !activeClinics().some(hasWeek)) out.push(",
   "  if (Store.mode !== 'demo' && !clinics().length) out.push('<a class=\"nudge accent\" data-first-clinic href=\"/gabinety?nowy=1\"><b>Dodaj pierwszy gabinet</b> – nazwa i zasady rozliczenia; potem zaznaczysz dni pracy, a kalendarz wypełni się sam</a>');\n  else if (Store.mode !== 'demo' && !activeClinics().some(hasWeek)) out.push("),
  ('K25 bez gabinetu: nowy dyżur prosi o dodanie gabinetu (zamiast błędu)',
   "function openEditor(id, date, pre) {\n",
   "function noClinic() { if (clinics().length) return false; toast('Najpierw dodaj gabinet – Ustawienia → Gabinety albo „Gabinety” w menu'); UI.tab = 'set'; UI.edit = null; UI.modal = null; renderModal(); render(); scrollToId('sec-clinics'); return true; }\nfunction openEditor(id, date, pre) {\n  if (!id && noClinic()) return;\n"),
  ('K25a bez gabinetu: „Dodaj dyżury” prosi o dodanie gabinetu',
   "  'shift-new': function () { UI.modal = 'bulk';",
   "  'shift-new': function () { if (noClinic()) return; UI.modal = 'bulk';"),
  ('K25b bez gabinetu: nowy wzór dni pracy prosi o dodanie gabinetu',
   "  'tpl-new': function () {\n    var c = activeClinics()[0] || clinics()[0];",
   "  'tpl-new': function () {\n    if (noClinic()) return;\n    var c = activeClinics()[0] || clinics()[0];"),
  ('K25c bez gabinetu: klik w siatkę tygodnia nie odwołuje się do nieistniejącego gabinetu',
   "  var c0 = activeClinics()[0] || clinics()[0], p0 = (c0.presets || []).filter(inP)[0];",
   "  var c0 = activeClinics()[0] || clinics()[0] || { id: null, presets: [] }, p0 = (c0.presets || []).filter(inP)[0];"),
  ('K39 wygląd jak reszta aplikacji (prompt Patryka 21.11.2026, pkt 4.1; wzorzec: Opisy NFZ): czcionka IBM Plex, paleta Gabinetu, wyróżnienia (przyciski główne, aktywna zakładka, dziś, podpowiedzi) w kolorze morskim zamiast czarnego, zakładki jako „pigułki”; logika bez zmian; kolory gabinetów bez zmian',
   '</style>',
   '/* K39: wygląd jak w Opisach NFZ */\n:root{--font-body:"IBM Plex Sans","Segoe UI",system-ui,-apple-system,sans-serif;--font-display:"IBM Plex Sans","Segoe UI",system-ui,-apple-system,sans-serif}\n:root:not([data-theme]){--bg:var(--g-bg);--surface:var(--g-surface);--ink:var(--g-ink);--muted:var(--g-muted);--line:var(--g-line)}\n.brand .logo{display:none}.brand h1{font-size:24px;font-weight:700;font-variation-settings:normal}\n.tabs{gap:6px;padding:4px 0 8px}.tab{border:1px solid var(--line);border-radius:999px;padding:7px 14px;background:var(--surface)}.tab:hover{border-color:var(--g-accent)}\n.tab[aria-selected=\"true\"]{background:var(--g-accent);border-color:var(--g-accent);color:var(--g-accent-ink)}\n.btn.primary,.nudge.accent{background:var(--g-accent);border-color:var(--g-accent);color:var(--g-accent-ink)}.btn.primary:hover{background:color-mix(in srgb,var(--g-accent) 86%,#000)}\n.cf[aria-pressed=\"true\"]{border-color:var(--g-accent);box-shadow:inset 0 0 0 1px var(--g-accent)}\n.cell.today .dnum,.wk-hd.today b,.onb .ck.ok,.sb-now,.bk-num{background:var(--g-accent);border-color:var(--g-accent);color:var(--g-accent-ink)}\n.meter .m-d{background:var(--g-accent)}.yd.today{box-shadow:inset 0 0 0 2px var(--g-accent)}label.chk input{accent-color:var(--g-accent)}\n</style>'),
  ('K40 strona nie przeskakuje po wejściu do Kalendarza (zgłoszenie Patryka 21.11.2026: „ucina zakładki u góry”): gdy strona jest na samej górze, przerysowanie (np. podpowiedzi po wczytaniu danych) nie przewija jej w dół',
   "if (r.bottom > h + 48) return { key: bl[i].dataset.key, top: r.top }; }",
   "if (r.bottom > h + 48) return { key: bl[i].dataset.key, top: r.top, y: window.scrollY }; }"),
  ('K40a utrzymanie miejsca na ekranie tylko, gdy strona była przewinięta',
   "function stackRestore(a) {\n  if (!a) return;",
   "function stackRestore(a) {\n  if (!a || a.y < 1) return;"),
  ('K41 Rozliczenia i Podsumowanie przeniesione do Zarobków (decyzja Patryka 21.11.2026): ten sam kod i obliczenia, otwierane pod /zarobki/rozliczenia i /zarobki/podatki (widok z danych startowych); w menu aktywne „Zarobki”',
   "G.bar('kalendarz');",
   "var WIDOK = (window.__GABINET && window.__GABINET.widok) || '', WIDOK_TAB = { rozliczenia: 'inv', podatki: 'sum' }[WIDOK] || '';\n"
   "var ZAR_URL = { inv: '/zarobki/rozliczenia', sum: '/zarobki/podatki' };\n"
   "G.bar(WIDOK_TAB ? 'zarobki' : 'kalendarz');"),
  ('K41a zakładki: w Kalendarzu bez „Podsumowanie” i „Rozliczenia”; w widoku Zarobków tylko wybrany widok',
   "  ['dl', 'Terminy', 'terminy'], ['cmp', 'Porównaj formy', 'porownaj'], ['set', 'Ustawienia', 'ustawienia']];",
   "  ['dl', 'Terminy', 'terminy'], ['cmp', 'Porównaj formy', 'porownaj'], ['set', 'Ustawienia', 'ustawienia']];\n"
   "var TABS_ALL = TABS; TABS = WIDOK_TAB ? TABS.filter(function (t) { return t[0] === WIDOK_TAB; }) : TABS.filter(function (t) { return t[0] !== 'sum' && t[0] !== 'inv'; });"),
  ('K41b w widoku Zarobków zamiast zakładek Kalendarza – nawigacja Zarobki · Rozliczenia · Podatki i ZUS',
   "function renderTabs() {\n  var todo",
   "function renderTabs() {\n"
   "  if (WIDOK_TAB) { var h1 = document.querySelector('.brand h1'); if (h1) h1.textContent = 'Zarobki'; document.title = (WIDOK_TAB === 'inv' ? 'Rozliczenia' : 'Podatki i ZUS') + ' – Zarobki – Gabinet';\n"
   "    document.getElementById('tabs').innerHTML = [['/zarobki', 'Zarobki', ''], [ZAR_URL.inv, 'Rozliczenia', 'inv'], [ZAR_URL.sum, 'Podatki i ZUS', 'sum']].map(function (x) {\n"
   "      return '<a class=\"tab\" href=\"' + x[0] + '\"' + (x[2] === WIDOK_TAB ? ' aria-current=\"page\" aria-selected=\"true\"' : '') + ' style=\"text-decoration:none\">' + x[1] + '</a>'; }).join(''); return; }\n"
   "  var todo"),
  ('K41c start: w widoku Zarobków właściwa zakładka; stare adresy #podsumowanie / #rozliczenia prowadzą do Zarobków',
   "  TABS.forEach(function (t) { if (t[2] === h) UI.tab = t[0]; });",
   "  if (!WIDOK_TAB && (h === 'podsumowanie' || h === 'rozliczenia')) { location.replace(h === 'rozliczenia' ? ZAR_URL.inv : ZAR_URL.sum); return; }\n"
   "  TABS.forEach(function (t) { if (t[2] === h) UI.tab = t[0]; });\n"
   "  if (WIDOK_TAB) UI.tab = WIDOK_TAB; else if (UI.tab === 'sum' || UI.tab === 'inv') UI.tab = 'cal';"),
  ('K41d przejścia do zakładek z innych miejsc (podpowiedzi, terminy): Podsumowanie/Rozliczenia → Zarobki; z widoku Zarobków do pozostałych → Kalendarz',
   "  'tab': function (el) { UI.tab = el.dataset.v;",
   "  'tab': function (el) { var v = el.dataset.v;\n"
   "    if (!WIDOK_TAB && ZAR_URL[v]) { location.href = ZAR_URL[v]; return; }\n"
   "    if (WIDOK_TAB && v !== WIDOK_TAB) { var t = TABS_ALL.filter(function (x) { return x[0] === v; })[0]; location.href = ZAR_URL[v] || ('/kalendarz' + (t ? '#' + t[2] : '')); return; }\n"
   "    UI.tab = v;"),
  ('K41e Rozliczenia: kolumna „Zarobek lekarza (z dyżurów)” – ta sama nazwa i kwota co w Zarobkach',
   "<th class=\"r\">Z Twojego kalendarza</th>",
   "<th class=\"r\">Zarobek lekarza (z dyżurów)</th>"),
  ('K60 obrót a opisy (prompt Patryka 23.11.2026, pkt 7.2): przy obrocie dyżuru wybór „obejmuje opisy z tego dnia” (domyślnie – jak dotąd) albo „dodatkowy (poza opisami)” – Zarobki nie liczą tego samego przychodu dwa razy',
   "'<label class=\"f\">Lab / implanty<input type=\"text\" inputmode=\"decimal\" id=\"f-lab\" value=\"' + esc(d.lab) + '\" placeholder=\"0\"></label></div>' + hintHtml(d);",
   "'<label class=\"f\">Lab / implanty<input type=\"text\" inputmode=\"decimal\" id=\"f-lab\" value=\"' + esc(d.lab) + '\" placeholder=\"0\"></label></div>' +\n"
   "    '<div class=\"f\"><span class=\"small\"><b>Obrót a opisy z tego dnia</b></span><div class=\"seg\" role=\"group\" aria-label=\"Obrót a opisy\" data-testid=\"obrot-typ\">' +\n"
   "    '<button type=\"button\" data-a=\"f-otyp\" data-v=\"opisy\" aria-pressed=\"' + (d.obrotTyp !== 'dodatkowy') + '\">Obejmuje opisy z tego dnia</button>' +\n"
   "    '<button type=\"button\" data-a=\"f-otyp\" data-v=\"dodatkowy\" aria-pressed=\"' + (d.obrotTyp === 'dodatkowy') + '\">Dodatkowy (poza opisami)</button></div>' +\n"
   "    '<span class=\"hint\">' + (d.obrotTyp === 'dodatkowy' ? 'Zarobki: opisy + ten obrót (usługi, których nie ma w opisach).' : 'Zarobki: przychód dnia = ten obrót; opisy z tego dnia nie są doliczane drugi raz.') + '</span></div>' + hintHtml(d);"),
  ('K60a obrót a opisy – wartość przy edycji dyżuru',
   "amount: inputNum(s.amount), override: inputNum(s.override), note: s.note || '', timesTouched: true };",
   "amount: inputNum(s.amount), override: inputNum(s.override), note: s.note || '', timesTouched: true, obrotTyp: s.obrotTyp === 'dodatkowy' ? 'dodatkowy' : 'opisy' };"),
  ('K60b obrót a opisy – zapis w dyżurze',
   "amount: num(d.amount), override: num(d.override), note: (d.note || '').trim() };",
   "amount: num(d.amount), override: num(d.override), note: (d.note || '').trim(), obrotTyp: d.obrotTyp === 'dodatkowy' ? 'dodatkowy' : 'opisy' };"),
  ('K60c obrót a opisy – przełącznik',
   "  'f-status': function (el) { UI.edit.draft.status = el.dataset.v; render(); },",
   "  'f-status': function (el) { UI.edit.draft.status = el.dataset.v; render(); },\n  'f-otyp': function (el) { UI.edit.draft.obrotTyp = el.dataset.v === 'dodatkowy' ? 'dodatkowy' : 'opisy'; render(); },"),
  ('K61 ustawienia gabinetu w Kalendarzu bez rozliczeń (prompt Patryka 23.11.2026, pkt 8): bez pól Rozliczenie, Twój %, Minimum za dzień, Spodziewany przychód, Termin płatności – ustawienia w Gabinety (app.clinics – źródło prawdy), dane zostają',
   '      sel(\'Rozliczenie\', p + \'model\', b + \'model\', c.model, Object.keys(MODELS).map(function (k) { return [k, MODELS[k]]; })) +\n      \'<div class="frow">\' + modelFields + fld(\'Minimum za dzień (zł)\', p + \'min\', b + \'minDaily\', c.minDaily, { num: 1, hint: \'0 = brak\' }) + \'</div>\' +\n      \'<div class="frow">\' + fld(\'Spodziewany przychód z dyżuru\', p + \'exp\', b + \'expected\', c.expected, { num: 1, hint: \'do prognozy, zanim powstanie historia\' }) + fld(\'Termin płatności (dni)\', p + \'pay\', b + \'payDays\', c.payDays, { num: 1 }) + \'</div>\' +\n',
   '      \'<p class="small muted" data-testid="rozl-w-gabinetach">Rozliczenie gabinetu (model, Twój %, stawki, minimum za dzień) ustawiasz w <a href="/gabinety">Gabinety</a>, a zarobki i rozliczenia widzisz w <a href="/zarobki">Zarobki</a>.</p>\' +\n'),
]

def przenies(plik, patches):
    src = open(os.path.join(OLD, plik), encoding='utf-8').read()
    for name, old, new in patches:
        n = src.count(old)
        if n != 1: sys.exit(f'Poprawka „{name}” pasuje {n} razy (oczekiwano 1) – sprawdź zmiany w opisy-nfz/{plik}')
        src = src.replace(old, new)
    head = f'<!-- Gabinet SaaS: przeniesione z opisy-nfz@{commit} ({plik}) przez tests/tools/przenies_generator.py; poprawki: generator/ZMIANY.md -->\n'
    open(os.path.join(OUT, plik), 'w', encoding='utf-8').write(head + src)

przenies('nfz.html', PATCHES)
przenies('prywatne.html', PATCHES_PRYW)
przenies('kalendarz.html', PATCHES_KAL)
shutil.copy(os.path.join(OLD, 'prywatne-katalog.js'), os.path.join(OUT, 'prywatne-katalog.js'))
shutil.copy(os.path.join(OLD, 'szablony.js'), os.path.join(OUT, 'szablony.js'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'scripts'))
import nfz_dane_przegladarka; nfz_dane_przegladarka.zapisz()   # audyt NFZ (N1): data/nfz → generator/nfz-dane.js
import baza_dane_przegladarka; baza_dane_przegladarka.zapisz()   # baza stomatologiczna (I1): checklisty → generator/baza-dane.js
import karty_opisy_przegladarka; karty_opisy_przegladarka.zapisz()   # opis z karty (I2): szablony kart zweryfikowanych → generator/karty-opisy.js
shutil.copy(os.path.join(OLD, 'wspolne.css'), os.path.join(OUT, 'wspolne.css'))
with open(os.path.join(OUT, 'ZMIANY.md'), 'w', encoding='utf-8') as f:
    f.write(f'# Moduły Opisy NFZ, Opisy prywatne i Kalendarz – zmiany względem obecnej aplikacji\n\nŹródło: repo `opisy-nfz`, commit `{commit}` – pliki `nfz.html`, `szablony.js`, `prywatne.html`, `prywatne-katalog.js`, `kalendarz.html`, `wspolne.css` (logika, pytania, reguły NFZ, szablony i teksty bez zmian).\n'
            'Plik `wspolne.js` (sejf z hasłem w przeglądarce) zastąpiony przez `gabinet-saas.js`.\n\n## Opisy NFZ (`nfz.html`)\n\n| # | Poprawka |\n|---|---|\n')
    for name, _, _ in PATCHES: f.write(f'| {name.split(" ", 1)[0]} | {name.split(" ", 1)[1]} |\n')
    f.write('\n## Opisy prywatne (`prywatne.html`)\n\n| # | Poprawka |\n|---|---|\n')
    for name, _, _ in PATCHES_PRYW: f.write(f'| {name.split(" ", 1)[0]} | {name.split(" ", 1)[1]} |\n')
    f.write('\n## Kalendarz (`kalendarz.html`)\n\n| # | Poprawka |\n|---|---|\n')
    for name, _, _ in PATCHES_KAL: f.write(f'| {name.split(" ", 1)[0]} | {name.split(" ", 1)[1]} |\n')
print(f'przeniesiono z opisy-nfz@{commit}: nfz.html ({len(PATCHES)}), prywatne.html ({len(PATCHES_PRYW)}), kalendarz.html ({len(PATCHES_KAL)} poprawek)')
