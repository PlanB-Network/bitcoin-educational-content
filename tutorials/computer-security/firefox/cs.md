---
name: Firefox
description: Jak nastavit Firefox tak, aby chránil vaše soukromí?
---

![cover](assets/cover.webp)



## Úvod



Všichni trávíme hodiny online, aniž bychom si uvědomovali, co o nás náš prohlížeč prozrazuje. Každé kliknutí, každé vyhledávání, každá navštívená stránka živí obrovský průmysl sběru osobních údajů.



![Statistiques navigateurs 2024](assets/fr/01.webp)


*Podíl webových prohlížečů na trhu: Podíl prohlížeče Chrome na trhu je 65 %, následují Safari a Edge. Zdroj: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*



Jak ukazuje tento graf, prohlížeč Google Chrome má masivní převahu a celosvětově se používá z více než 65 %. Tato hegemonie znamená, že většina uživatelů internetu svěřuje svá data o prohlížení webu společnosti Google, jejíž obchodní model je založen na cílené reklamě. Firefox s pouhými 3 % trhu představuje alternativu vyvinutou Mozillou, neziskovou organizací, která nemá žádný komerční zájem na zneužívání vašich dat.



Výběr prohlížeče Firefox je však pouze prvním krokem. I Firefox ve výchozím nastavení vyžaduje úpravy, abyste maximalizovali svou ochranu. Tento průvodce vás krok za krokem provede od nejjednoduššího po nejpokročilejší, abyste Firefox proměnili ve skutečný štít proti sledování a zároveň zachovali příjemné prohlížení.



### Proč Firefox?





- Svobodný a otevřený zdrojový kód** (engine Gecko): kontrolovatelný, transparentní kód
- Nezisková organizace**: Mozilla Foundation, poslání obecného zájmu
- Vestavěné nativní ochrany**: Rozšířená ochrana proti sledování (ETP), celková ochrana proti souborům cookie (TCP), rozdělení stavu, režim pouze HTTPS, DNS přes HTTPS (DoH)
- Pokročilé přizpůsobení**: na rozdíl od prohlížeče Chrome umožňuje Firefox hloubkově upravit své chování



### Důležité zásady před zahájením





- Žádný univerzální recept**: čím více upravujete, tím více riskujete, že se odlišíte (fingerprinting). Cílem je být lépe chráněn, aniž byste vyčnívali z davu.
- Postup krok za krokem**: Změňte nastavení, otestujte obvyklé stránky a pokračujte. Není nutné měnit vše najednou.
- Osobní rovnováha**: Najděte SVŮJ kompromis mezi soukromím a snadným používáním.



## Rychlá instalace



![Téléchargement Firefox](assets/fr/02.webp)



**Oficiální stažení:** Přejděte na [firefox.com/browsers/desktop](https://www.firefox.com/en-US/browsers/desktop/). Na této stránce vyberte svůj operační systém (Windows, macOS, Linux) a přejděte na příslušnou stránku ke stažení s konkrétními pokyny k instalaci.





- Windows**: stáhněte si instalační soubor `.exe`, dvakrát na něj klikněte a postupujte podle průvodce instalací
- macOS**: stáhněte soubor `.dmg`, otevřete jej a přetáhněte Firefox do složky Aplikace
- Linux**: k dispozici je několik možností - balíček `.deb`/`.rpm`, Flatpak (Flathub), Snap nebo prostřednictvím správce balíčků (apt, dnf, pacman). Upřednostňujte oficiální zdroje Mozilly.



**Tip:** Po instalaci zkontrolujte aktualizace prostřednictvím nápovědy → **O Firefoxu** (důležité pro bezpečnostní záplaty).



![Configuration initiale Firefox](assets/fr/03.webp)


*První obrazovka při spuštění Firefoxu: nastavte Firefox jako výchozí prohlížeč, přidejte jej do zástupců a klikněte na "Uložit a pokračovat "*



![Création compte Firefox](assets/fr/04.webp)


*Volitelný krok: Vytvořte si účet Firefox nebo se k němu přihlaste. Tento krok můžete přeskočit kliknutím na "Not now" vpravo dole*



![Page d'accueil Firefox](assets/fr/05.webp)


*Domovská obrazovka Firefoxu po dokončení konfigurace. Všimněte si nabídky ☰ vpravo nahoře, která umožňuje přístup k Nastavení a Rozšíření pro přizpůsobení Firefoxu*



## Ochrana je aktivována již ve výchozím nastavení (uklidňující)





- Izolace místa (Fission)**: při postupném nasazování. Tato funkce spouští každý web v samostatném procesu, aby se zabránilo přístupu jedné škodlivé karty k datům jiné. Zkontrolujte její stav prostřednictvím `about:support` (vyhledejte "Fission"). Pokud není povolena, můžete ji aktivovat ručně v `about:config` pomocí `fission.autostart = true`.
- Total Cookie Protection (TCP)**: ve výchozím nastavení aktivní. Soubory cookie a další úložiště jsou omezeny na stránky první strany (jedna "sklenice" na každou stránku), což neutralizuje sledování napříč stránkami. Dočasné výjimky jsou v případě potřeby prováděny prostřednictvím rozhraní API pro přístup k úložišti (integrovaná přihlašovací tlačítka).
- Ochrana před sledováním odrazu/ přesměrování**: Firefox automaticky detekuje a čistí soubory cookie, které po sobě zanechávají stránky, na nichž došlo k přesměrování (odkazy, které vás přesměrují přes sledovací zařízení před cílovým místem), a omezuje tak tento sledovací kanál bez vašeho přičinění.



## Úroveň 1 - základní (≤ 10 minut)



Cíl: velký přínos pro ochranu soukromí bez narušení webu. Pro 90 % uživatelů.



Chcete-li se dostat do nastavení, klikněte na nabídku ☰ vpravo nahoře a poté na **"Nastavení "**:



![Paramètres généraux](assets/fr/07.webp)


*Stránka nastavení Firefoxu - karta "Obecné". Zde se nastavuje většina možností ochrany soukromí*



**Ochrana sledování (ETP)**




- Přepněte **ETP** na **Strict**. Zablokujete více sledovacích zařízení (cross-site cookies, fingerprinting, cryptomining, social widgets...).
- Pokud se některý web rozbije (video, přihlašovací tlačítko...), deaktivujte ochranu pouze pro tento web pomocí štítu 🛡️ a poté kartu obnovte.



Zde jsou uvedeny různé úrovně zabezpečení ETP:




- Standard** (vyvážený, maximální kompatibilita)
  - Blokuje: sociální trackery, cross-site cookies (všechna okna), sledování obsahu při soukromém prohlížení, těžaře kryptoměn, detektory otisků prstů.
  - Zahrnuje **Total Cookie Protection** (TCP): jedna nádoba na web.
- Přísný** (doporučeno z důvodu důvěrnosti)
  - Blokuje také sledovací obsah ve všech oknech + známé a podezřelé otisky prstů.
  - Může poškodit některé weby; pro místní výjimku použijte štít 🛡️.
- Vlastní** (pokročilé)
  - Jemné ladění: soubory cookie, sledování obsahu, nezletilí, otisky prstů (známé/podezřelé).



![Paramètres protection contre le pistage](assets/fr/06.webp)



**Soubory cookie a údaje o webu




- Povolte funkci **"Smazat soubory cookie a data webu při zavření "**, aby se při každém restartu restartoval čistě.
- Pokud chcete, přidejte **výjimky** pro 2-3 základní stránky (e-mail, banka).


**Automatické zadávání dat, návrhy a domovská stránka**




- Deaktivujte **automatické vyplňování** (ID, adresy, karty). Místo toho použijte správce hesel.
- Vyhledávání**: deaktivujte **"Zobrazit návrhy vyhledávání "**.
- Proužek Address**: vyjměte **"Sponzorované návrhy "** a **"Kontextové návrhy "**.
- Domovská stránka**: vypněte **Kapsu** a **sponzorovaný obsah**.



![Paramètres cookies et mots de passe](assets/fr/08.webp)



**Pouze pro HTTP**




- Aktivujte **"Režim HTTPS pouze ve všech oknech "**.


![Configuration DNS over HTTPS](assets/fr/09.webp)



**Telemetrie a měření reklamy




- V části "Shromažďování dat prohlížečem Firefox" **odškrtněte vše**.
- Deaktivujte **"Reklamní opatření šetrná k soukromí "** (PPA).
- Bezpečné procházení**: ponechte ji povolenou (doporučeno). Firefox kontroluje weby podle seznamů hrozeb pomocí dotazů s hashováním a místních kontrol, čímž chrání před phishingem a malwarem s minimálním dopadem na soukromí.



**Globální kontrola soukromí (volitelné)**




- Aktivujte **GPC**, abyste dali najevo, že odmítáte prodávat/sdílet data.



**Vyhledávač




- Přepněte na **DuckDuckGo**, **Startpage**, **Qwant** nebo **Brave Search** (Nastavení → Hledání).



![Configuration moteur de recherche DuckDuckGo](assets/fr/11.webp)



**Soukromá navigace**




- Soukromá okna (Ctrl/Cmd+Shift+P) pro jednorázové relace (dárky, sekundární účty...). Vyhněte se režimu "vždy soukromé": rozšíření mohou být neaktivní a výjimky ze souborů cookie méně užitečné.



**Zásadní rozšíření** (instalace z oficiálního katalogu)




- uBlock Origin**: blokuje reklamy a aktuální sledování, lehký.
- Privacy Badger**: naučí se blokovat, co vás sleduje; odesílá Do Not Track / GPC.
- ClearURLs** (nepovinné): Firefox (ETP Strict) a uBO již hodně čistí; ponechte si ji, pokud stále vidíte "špinavé" adresy URL (utm, fbclid).
- Kontejnery Firefoxu pro více účtů**: **odděluje soubory cookie/relace a úložiště pro každý kontejner; paralelní více účtů; méně sledování napříč stránkami**. Oficiální rozšíření: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.



![Extension Multi-Account Containers](assets/fr/12.webp)



**Hesla a 2FA**




- Používejte specializovaný správce hesel** (Bitwarden, KeePassXC). **Vyhněte se** ukládání hesel v prohlížeči. **Všude, kde je to možné, zapněte 2FA**.



## Úroveň 2 - Zesílená (rozdělení do oddílů a sítě)



Cíl: rozdělit činnosti a omezit únik informací ze sítě.



**DNS přes HTTPS (DoH)**




- Výchozí stav**: V některých regionech (USA, Kanada, Rusko, Ukrajina) se aktivuje automaticky. Jinde je nutná ruční aktivace.
- Konfigurace**: Nastavení → Obecné → Nastavení sítě → **Zapnout DoH** → **Cloudflare** nebo **Quad9** → **Maximální ochrana**.
- Maximální ochrana = pouze TRR** (bez zpětného přechodu na systém DNS). Pokud se firemní/hotelová síť zablokuje, přepněte zpět na **Standard** nebo vypněte DoH.
- Zbytečnost**: Pokud již používáte důvěryhodnou síť VPN s vlastním zabezpečeným systémem DNS, může být služba DoH nadbytečná.
- Ověřovací test**: `https://www.dnsleaktest.com/` by měl zobrazit pouze vybraného poskytovatele DoH.



![Sélection fournisseur DNS Cloudflare](assets/fr/10.webp)



**Kompartmentalizace pomocí kontejnerů a profilů




- Kontejnery pro více účtů**: vytvořte si prostory (osobní, pracovní, finanční, sociální sítě, nákupní, jednorázové). Nastavte **"Vždy otevřít v tomto kontejneru "** pro opakující se stránky. Oficiální rozšíření: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.
- Proč je používat?
  - Silná izolace** souborů cookie/relace/úložiště podle prostoru.
  - Méně sledování napříč stránkami**: omezte giganty (Facebook, Google).
  - Současné používání více účtů** ve stejné službě.
  - Menší riziko CSRF/XSS** mezi segmentovanými identitami.
  - Tip: přinejmenším vyhrazené kontejnery pro sociální sítě/Google, práci a finance.
- Facebook Container** (volitelné): zjednodušená verze určená pro FB/Instagram.
- Oddělené profily**: přes `about:profiles` (hlavní profil, minimální "ultrabezpečný" profil, testovací profil). Celková kompartmentalizace dat a rozšíření.



**Pokročilá rozšíření** (bude rezervováno)




- Cookie AutoDelete**: odstraní soubory cookie webu, jakmile je karta zavřena (užitečné, pokud je Firefox otevřen delší dobu).
- LocalCDN**: obsluhuje aktuální knihovny lokálně (snižuje počet volání na Google/Microsoft). Částečná kompatibilita.



**Mobilní zařízení (Android)**




- Firefox Android + uBlock Origin**: podobná ochrana na cestách.



## Úroveň 3 - Expert (about:config & Arkenfox)



Cíl: pokročilé zpevnění s přijatelnými kompromisy. Doporučeno na **odděleném profilu**.



Vyberte si pouze jeden z následujících dvou přístupů:



**Přístup A - ruční úpravy**: Několik cílených úprav pomocí `about:config` (jednodušší, přesnější ovládání)


**Přístup B - Arkenfox user.js**: (složitější, maximální ochrana)



➡️ **Arkenfox již obsahuje VŠECHNY níže uvedené změny v about:config** + stovky dalších. Pokud se rozhodnete pro Arkenfox, ignorujte sekci about:config.



### Přístup A: Ruční úpravy pomocí about:config



Do panelu Address napište `about:config` → Přijmout riziko.



![Avertissement about:config](assets/fr/13.webp)



![Interface about:config](assets/fr/14.webp)



![Préférences about:config](assets/fr/15.webp)





- Odolnost proti snímání otisků prstů (zděděná po prohlížeči Tor Browser)


```text
privacy.resistFingerprinting = true
```


Účinky: Časové pásmo UTC, **letterboxing** (standardní velikosti oken), standardizované User-Agent/politiky, omezení Canvas/WebGL/AudioContext. Větší jednotnost, ale několik "výstředností" (posun času, někdy trochu angličtiny).





- Zakázat WebRTC (zabrání úniku IP adres; naruší Web visio)


```text
media.peerconnection.enabled = false
```





- Odkaz plus kompatibilní (výchozí)


```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```


Přísná volba (může porušit platby/SSO):


```text
network.http.referer.XOriginPolicy = 2
```





- Omezení chatování API a spekulací


```text
dom.battery.enabled = false
device.sensors.enabled = false
beacon.enabled = false
geo.enabled = false
media.navigator.enabled = false
network.prefetch-next = false
browser.urlbar.speculativeConnect.enabled = false
network.http.speculative-parallel-limit = 0
```



Zlaté pravidlo: pokud se něco pokazí, vraťte se k poslední změně.



### Přístup B: Arkenfox user.js (plně automatizovaná konfigurace)



Projekt **Arkenfox** poskytuje komunitou spravovaný soubor `user.js`, který automaticky aplikuje stovky předvoleb Firefoxu zaměřených na soukromí a zabezpečení. Při opětovném spuštění Firefox načte tento soubor z vašeho profilu a použije tato nastavení.





- Jaký to má smysl? Vycházejte z **konzistentního zpevněného základu** bez "klikání všude"; omezte přehlédnutí; ušetřete čas.
- Co se změní (příklady): omezení telemetrie, posílení cookies/cache/referrer/HTTPS, **RFP** + letterboxing, **WebRTC zakázáno**, úpravy DoH/TLS, omezení chatovacích API.
- Kdy ji použít: pokud chcete Firefox zpevnit během 10 minut a přijmout několik výjimek (DRM/streamování, Web visio, SSO/platby).
- Výhody: rychlý, konzistentní, **aktualizovaný** (ESR-aligned), velmi dobře **dokumentovaný** (wiki + komentáře), **přizpůsobitelný** pomocí přepisů.
- Omezení: kompatibilita (některé webové aplikace), pohodlí (UTC, velikosti oken) a připomínka: **není to Tor** (žádná síťová anonymita).



Instalace (ideálně na **vyhrazeném profilu**)


1. Uložení profilu/oblíbených stránek a seznam webů s výjimkami ze souborů cookie.


2. Stáhněte si soubor `user.js` z adresy `https://github.com/arkenfox/user.js` (ESR/stable verze).


3. Složku profilu najdete pomocí `about:profiles`:




   - Windows: `%APPDATA%/Mozilla/Firefox/Profiles/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/Library/Application Support/Firefox/Profiles/...`


4. Zavřete Firefox a přesuňte soubor `user.js` do kořenové složky profilu.


5. Opětovné spuštění; přizpůsobení pomocí `about:config` nebo souboru overrides.



Aktualizace




- Postupujte podle vydání Arkenfoxu (v souladu s ESR), nahraďte soubor `user.js`, znovu spusťte Firefox; přečtěte si poznámky k vydání.



**Přizpůsobení pomocí přepisů**



Arkenfox je ve výchozím nastavení záměrně restriktivní. Chcete-li přizpůsobit některá nastavení svým potřebám (streamování, visio, konkrétní stránky), můžete vytvořit soubor `user-overrides.js` ve stejné složce jako `user.js`. Tento soubor vám umožní "přepsat" určité předvolby Arkenfoxu, aniž byste museli měnit hlavní soubor.



Vytvořte soubor `user-overrides.js` a přidejte své úpravy:


```javascript
// DRM/streaming
user_pref("media.eme.enabled", true);

// Safe Browsing (si vous préférez le garder)
user_pref("browser.safebrowsing.phishing.enabled", true);
user_pref("browser.safebrowsing.malware.enabled", true);

// Historique moins restrictif
user_pref("places.history.expiration.max_pages", 200000);

// Synchronisation Firefox
user_pref("identity.fxaccounts.enabled", true);

// WebRTC (si visio nécessaire)
user_pref("media.peerconnection.enabled", true);

// Referer plus compatible
user_pref("network.http.referer.XOriginPolicy", 1);
user_pref("network.http.referer.trimOnCrossOrigin", true);
```



Osvědčené postupy




- Používejte samostatný profil **"Arkenfox "** a pro větší pohodlí si ponechte "normální" profil.
- Minimalizujte rozšíření (uBlock Origin OK), abyste omezili plochu útoku a jedinečnost.
- V případě potřeby přidejte výjimky pro jednotlivé stránky (štít 🛡️, uBO, NoScript, pokud je používán).
- Testujte po každé změně: WebRTC/DNS leaks, Cover Your Tracks, CreepJS.



## Osvědčené postupy





- Aktualizace**: Firefox a rozšíření jsou aktuální.
- Prodloužení**: rozumné a spolehlivé; pozor na "pochybné" výkupy.
- Soubory ke stažení**: opatrně; otestujte citlivé soubory na VirusTotal.
- Hesla**: **dedikovaný správce** (Bitwarden, KeePassXC); **2FA** povoleno; vyhnout se ukládání v prohlížeči.
- Hygiena**: omezte Google/Facebook na kontejnery; pravidelně je zavírejte/otevírejte, abyste obnovili kontext.



## Omezení a alternativy





- Zabezpečený prohlížeč ≠ síťová anonymita: bez **VPN** zůstává vaše IP viditelná; i s ní je možná korelace.
- Přílišné úpravy vás mohou učinit **jedinečnými**. **RFP** standardizuje; randomizační nástroje (např. Chameleon) vás mohou... odlišit. Testujte, porovnávejte, upravujte.
- Alternativy/doplňky:
 - Prohlížeč Tor Browser: síťová anonymita přes Tor; pomalejší. Viz náš kompletní průvodce instalací a konfigurací**:



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb



 - Mullvad Browser: "Tor bez Toru", který lze kombinovat s VPN; standardizovaná stopa. Jak jej nainstalovat, se dozvíte v našem speciálním návodu**:



https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e



- Doporučené kombinace: Pro každodenní použití Firefox (úroveň 2) + VPN; Tor/Mullvad pro citlivé činnosti; oddělené profily pro rozdělení.



## Závěr



Postupem podle tohoto průvodce krok za krokem jste proměnili Firefox ve skutečnou ochrannou hráz proti digitálnímu dohledu. Od základních nastavení 1. úrovně až po pokročilé konfigurace Arkenfoxu - každá změna posiluje vaše soukromí, aniž by ohrozila váš zážitek z prohlížení.



**Vaše soukromí je nyní lépe chráněno**: reklamní trackery jsou blokovány, cookies jsou rozděleny, úniky IP Address jsou neutralizovány, telemetrie je zakázána. Firefox už není jen prohlížeč, ale nástroj digitální odolnosti přizpůsobený vašim potřebám.



**Zapomeňte: důvěrnost není nikdy samozřejmostí. Pravidelně testujte ochranu, aktualizujte nastavení a neváhejte upravovat konfiguraci podle toho, jak se mění vaše zvyky. Vaše online anonymita závisí stejně tak na vašich nástrojích jako na vašich postupech.



## Zdroje



### Plan ₿ Network




- SCU 202 - Zlepšení osobní digitální bezpečnosti: Chcete-li se dozvědět více o koncepcích digitální bezpečnosti, které jsou obsaženy v tomto kurzu**



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Dokumentace Mozilly




- [Zvýšená ochrana sledování](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop): Oficiální průvodce rozšířenou ochranou sledování
- [State Partitioning](https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning): Technická dokumentace k rozdělování stavů
- [MDN Web Security](https://developer.mozilla.org/docs/Web/Security): Kompletní reference o zabezpečení webu



### Arkenfox




- [Wiki a průvodce instalací](https://github.com/arkenfox/user.js/wiki): Kompletní dokumentace projektu Arkenfox
- [Vklad a uvolnění](https://github.com/arkenfox/user.js): Stáhnout soubor user.js a sledovat aktualizace



### Průvodci a komunity




- [Průvodci ochranou osobních údajů - Prohlížeče pro stolní počítače](https://www.privacyguides.org/en/desktop-browsers/): Doporučení a srovnání prohlížečů
- Reddit**: r/firefox, r/privacy pro zpětnou vazbu a podporu
- Fórum PrivacyGuides**: podrobné technické diskuse



### Testovací nástroje




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/): Digitální otisky prstů a účinnost ochrany proti sledování
- [Test úniku DNS](https://www.dnsleaktest.com/): Test úniku DNS a účinnost DoH
- [BrowserLeaks](https://browserleaks.com/): Kompletní sada testů (WebRTC, Canvas, písma atd.)
- [BadSSL](https://badssl.com/): Testy ověření platnosti certifikátů SSL/TLS
- [CreepJS](https://abrahamjuliot.github.io/creepjs/): Pokročilá analýza více než 50 vektorů otisků prstů
- [Cloudflare DNS Test](https://1.1.1.1/help): Kontrola správného fungování služby Cloudflare DoH
