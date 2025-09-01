---
name: Firefox
description: Hur konfigurerar jag Firefox för att skydda din integritet?
---

![cover](assets/cover.webp)



## Inledning



Vi tillbringar alla timmar på nätet, ofta utan att inse vad vår webbläsare avslöjar om oss. Varje klick, varje sökning, varje webbplats vi besöker ger näring åt en massiv industri för insamling av personuppgifter.



![Statistiques navigateurs 2024](assets/fr/01.webp)


*Marknadsandel för webbläsare: Chrome dominerar med 65% av marknaden, följt av Safari och Edge. Källa: [gs.statcounter.com [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*



Som framgår av diagrammet dominerar Google Chrome stort, med över 65 % av den globala användningen. Denna hegemoni innebär att majoriteten av Internetanvändarna anförtror sina surfdata till Google, ett företag vars affärsmodell bygger på riktad reklam. Firefox, med bara 3 % av marknaden, utgör ett alternativ som utvecklats av Mozilla, en ideell organisation som inte har något kommersiellt intresse av att utnyttja dina uppgifter.



Men att välja Firefox är bara det första steget. Som standard kräver även Firefox justeringar för att maximera ditt skydd. Den här guiden tar dig steg för steg, från det enklaste till det mest avancerade, för att förvandla Firefox till en veritabel sköld mot spårning samtidigt som du behåller en trevlig surfupplevelse.



### Varför Firefox?





- Fri och öppen källkod** (Gecko-motor): granskningsbar, transparent kod
- Ideell organisation**: Mozilla Foundation, uppdrag av allmänt intresse
- Inbyggda inbyggda skydd**: Enhanced Tracking Protection (ETP), Total Cookie Protection (TCP), State Partitioning, HTTPS-only-läge, DNS över HTTPS (DoH)
- Avancerad anpassning**: till skillnad från Chrome låter Firefox dig ändra dess beteende på djupet



### Viktiga principer innan du börjar





- Inget universellt recept**: ju mer du ändrar, desto större är risken att du sticker ut (fingeravtryck). Målet är att få ett bättre skydd utan att sticka ut från mängden.
- Steg-för-steg-utveckling**: Ändra en inställning, testa dina vanliga webbplatser och fortsätt sedan. Det finns inget behov av att ändra allt på en gång.
- Personlig balans**: Hitta din kompromiss mellan integritet och användarvänlighet.



## Snabb installation



![Téléchargement Firefox](assets/fr/02.webp)



**Officiell nedladdning:** Gå till [firefox.com/browsers/desktop] (https://www.firefox.com/en-US/browsers/desktop/). På den här sidan väljer du operativsystem (Windows, macOS, Linux) för att komma till rätt nedladdningssida med specifika installationsinstruktioner.





- Windows**: ladda ner installationsprogrammet `.exe`, dubbelklicka och följ installationsguiden
- macOS**: ladda ner filen `.dmg`, öppna den och dra Firefox till mappen Program
- Linux**: flera alternativ tillgängliga - paket `.deb`/`.rpm`, Flatpak (Flathub), Snap, eller via pakethanteraren (apt, dnf, pacman). Föredrar officiella Mozilla-källor.



**Tips:** När du har installerat, kontrollera om det finns uppdateringar via Hjälp → **Om Firefox** (viktigt för säkerhetsfixar).



![Configuration initiale Firefox](assets/fr/03.webp)


*Första skärmen vid start av Firefox: ställ in Firefox som din standardwebbläsare, lägg till den i dina genvägar och klicka sedan på "Spara och fortsätt"*



![Création compte Firefox](assets/fr/04.webp)


*Valfritt steg: skapa eller logga in på ett Firefox-konto. Du kan hoppa över detta steg genom att klicka på "Inte nu" längst ner till höger*



![Page d'accueil Firefox](assets/fr/05.webp)


*Firefox startskärm när konfigurationen är klar. Notera ☰-menyn längst upp till höger, som ger tillgång till Inställningar och Tillägg för att anpassa Firefox*



## Skydd som redan är aktiverade som standard (betryggande)





- Webbplatsisolering (Fission)**: i progressiv driftsättning. Den här funktionen kör varje webbplats i en separat process för att förhindra att en skadlig flik får åtkomst till en annans data. Kontrollera dess status via `about:support` (sök efter "Fission"). Om den inte är aktiverad kan du aktivera den manuellt i `about:config` med `fission.autostart = true`.
- Total Cookie Protection (TCP)**: aktiv som standard. Cookies och annan lagring begränsas till förstapartswebbplatsen (en "burk" per webbplats), vilket neutraliserar spårning på andra webbplatser. Tillfälliga undantag görs via Storage Access API när det behövs (integrerade inloggningsknappar).
- Skydd mot spårning av bounce/omdirigering**: Firefox upptäcker och rensar automatiskt bort cookies som lämnats kvar av bounce-webbplatser (länkar som omdirigerar dig via en spårare före destinationen), vilket minskar denna spårningskanal utan någon åtgärd från din sida.



## Nivå 1 - Grundläggande (≤ 10 minuter)



Mål: stora integritetsvinster utan att förstöra webben. För 90 % av användarna.



För att komma åt inställningarna klickar du på menyn ☰ uppe till höger och sedan på **"Inställningar"**:



![Paramètres généraux](assets/fr/07.webp)


*Inställningssida för Firefox - fliken "Allmänt". Det är här du konfigurerar de flesta av dina sekretessalternativ*



**Spårningsskydd (ETP)**




- Byt **ETP** till **Strict**. Du blockerar fler spårare (cross-site cookies, fingeravtryck, kryptomining, sociala widgetar ...).
- Om en webbplats går sönder (video, inloggningsknapp ...), avaktivera skyddet endast för den webbplatsen via 🛡️-skölden och uppdatera sedan fliken.



Här är de olika säkerhetsnivåerna för ETP:




- Standard** (balanserad, maximal kompatibilitet)
  - Blockerar: sociala spårare, cross-site cookies (alla fönster), spårning av innehåll i privat surfning, kryptovalutautvinnare, fingeravtrycksdetektorer.
  - Inkluderar **Total Cookie Protection** (TCP): en burk per webbplats.
- Strikt** (rekommenderas för sekretess)
  - Blockerar även spårningsinnehåll i alla fönster + kända och misstänkta fingeravtryck.
  - Kan förstöra vissa webbplatser; använd 🛡️-skölden för ett lokalt undantag.
- Anpassad** (avancerad)
  - Finjustering: cookies, spårning av innehåll, minderåriga, fingeravtryck (kända/misstänkta).



![Paramètres protection contre le pistage](assets/fr/06.webp)



**Cookies och webbplatsdata




- Aktivera **"Ta bort cookies och webbplatsdata vid stängning"** för att starta om rent varje gång du startar om.
- Lägg till **Undantag** för 2-3 viktiga webbplatser om du vill (e-post, bank).


**Automatisk datainmatning, förslag och hemsida**




- Avaktivera **auto-fyll** (ID, adresser, kort). Använd istället en lösenordshanterare.
- Sök**: avaktivera **"Visa sökförslag"**.
- Address bar**: klipp **"Sponsrade förslag"** och **"Kontextuella förslag"**.
- Hem**: avaktivera **Pocket** och **sponsrat innehåll**.



![Paramètres cookies et mots de passe](assets/fr/08.webp)



**Endast HTTPS**




- Aktivera **"HTTPS-läge endast i alla fönster"**.


![Configuration DNS over HTTPS](assets/fr/09.webp)



**Telemetri och mätning av reklam




- I "Datainsamling av Firefox", **avmarkera alla**.
- Avaktivera **"Privacy-friendly advertising measures"** (PPA).
- Säker surfning**: behåll den aktiverad (rekommenderas). Firefox kontrollerar webbplatser mot hotlistor via hashade förfrågningar och lokala kontroller, vilket skyddar mot nätfiske och skadlig kod med minimal integritetspåverkan.



**Global Privacy Control (tillval)**




- Aktivera **GPC** för att signalera att du vägrar att sälja/dela data.



**Sökmotor




- Byt till **DuckDuckGo**, **Startpage**, **Qwant** eller **Brave Search** (Inställningar → Sök).



![Configuration moteur de recherche DuckDuckGo](assets/fr/11.webp)



**Privat navigering**




- Privata fönster (Ctrl/Cmd+Shift+P) för engångssessioner (gåvor, sekundära konton...). Undvik läget "alltid privat": tillägg kan vara inaktiva och cookie-undantag mindre användbara.



**Essential extensions** (installera från den officiella katalogen)




- uBlock Origin**: blockerar annonser och aktuell spårning, lättviktig.
- Privacy Badger**: lär sig att blockera vad som följer dig; skickar Do Not Track / GPC.
- ClearURLs** (valfritt): Firefox (ETP Strict) och uBO rensar redan upp en hel del; behåll det om du fortfarande ser "smutsiga" webbadresser (utm, fbclid).
- Firefox behållare för flera konton**: **isolerar cookies/sessioner och lagring per behållare; parallella multikonton; mindre spårning mellan webbplatser**. Officiellt tillägg: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.



![Extension Multi-Account Containers](assets/fr/12.webp)



**Lösenord och 2FA**




- Använd en särskild lösenordshanterare** (Bitwarden, KeePassXC). ** Undvik** att lagra lösenord i webbläsaren. **Aktivera 2FA** där det är möjligt.



## Nivå 2 - Förstärkt (uppdelning i fack och nätverk)



Mål: Avgränsa aktiviteter och minska nätverksläckage.



**DNS över HTTPS (DoH)**




- Standardstatus**: Automatiskt aktiverad i vissa regioner (USA, Kanada, Ryssland, Ukraina). I övriga länder krävs manuell aktivering.
- Konfiguration**: Inställningar → Allmänt → Nätverksinställningar → **Aktivera DoH** → **Cloudflare** eller **Quad9** → **Maximalt skydd**.
- Maximalt skydd = endast TRR** (ingen reserv till systemets DNS). Om ett företags- eller hotellnätverk blockeras, byt tillbaka till **Standard** eller inaktivera DoH.
- Redundans**: Om du redan använder ett pålitligt VPN med egen säker DNS kan DoH vara överflödigt.
- Verifieringstest**: `https://www.dnsleaktest.com/` ska endast visa den valda DoH-leverantören.



![Sélection fournisseur DNS Cloudflare](assets/fr/10.webp)



**Avdelningsindelning med containrar och profiler




- Behållare med flera konton**: skapa utrymmen (personligt, arbete, ekonomi, sociala nätverk, shopping, engångsbruk). Konfigurera **"Öppna alltid i den här behållaren"** för dina återkommande webbplatser. Officiell förlängning: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.
- Varför använda dem?
  - Stark isolering** av cookies/sessioner/lagring per utrymme.
  - Mindre spårning mellan olika webbplatser**: begränsa jättarna (Facebook, Google).
  - Flera samtidiga konton** på samma tjänst.
  - Mindre risk för CSRF/XSS** mellan segmenterade identiteter.
  - Tips: åtminstone särskilda behållare för Sociala nätverk/Google, Arbete, Ekonomi.
- Facebook Container** (tillval): en förenklad version som är avsedd för FB/Instagram.
- Separata profiler**: via `about:profiles` (huvudprofil, minimal "ultra-säker" profil, testprofil). Total uppdelning av data och tillägg.



**Avancerade tillägg** (reserveras för senare ändringar)




- Cookie AutoDelete**: raderar en webbplats cookies så snart fliken stängs (användbart om Firefox är öppen under en längre tid).
- LocalCDN**: serverar aktuella bibliotek lokalt (minskar antalet anrop till Google/Microsoft). Partiell kompatibilitet.



**Mobil (Android)**




- Firefox Android + uBlock Origin**: liknande skydd när du är på resande fot.



## Nivå 3 - Expert (about:config & Arkenfox)



Mål: avancerad härdning med accepterade kompromisser. Rekommenderas på en **separat profil**.



Välj endast ett av följande två tillvägagångssätt:



**Tillvägagångssätt A - Manuella ändringar**: Ett fåtal riktade justeringar via `about:config` (enklare, mer exakt kontroll)


**Tillvägagångssätt B - Arkenfox user.js**: Fullständigt automatiserad konfiguration (mer komplex, maximalt skydd)



➡️ **Arkenfox innehåller redan ALLA about:config-ändringar som nämns nedan** + hundratals fler. Om du väljer Arkenfox, ignorera avsnittet about:config.



### Tillvägagångssätt A: Manuella ändringar via about:config



Skriv `about:config` i Address-fältet → Acceptera risk.



![Avertissement about:config](assets/fr/13.webp)



![Interface about:config](assets/fr/14.webp)



![Préférences about:config](assets/fr/15.webp)





- Motståndskraft mot fingeravtryck (ärvt från Tor Browser)


```text
privacy.resistFingerprinting = true
```


Effekter: UTC-tidszon, **letterboxing** (standardfönsterstorlekar), standardiserade User-Agent/policies, Canvas/WebGL/AudioContext-restriktioner. Mer enhetlighet, men några "konstigheter" (tidsförskjutning, ibland lite engelska).





- Inaktivera WebRTC (undviker IP-läckor; bryter Web visio)


```text
media.peerconnection.enabled = false
```





- Referer plus kompatibel (standard)


```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```


Strikt alternativ (kan bryta betalningar/SSO):


```text
network.http.referer.XOriginPolicy = 2
```





- Begränsning av chattande API:er och spekulation


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



Gyllene regel: om något går sönder, gå tillbaka till den senaste ändringen.



### Tillvägagångssätt B: Arkenfox user.js (helautomatisk konfiguration)



Projektet **Arkenfox** tillhandahåller en community-underhållen `user.js`-fil som automatiskt tillämpar hundratals integritets- och säkerhetsorienterade Firefox-inställningar. Vid omstart läser Firefox den här filen från din profil och tillämpar dessa inställningar.





- Vad är poängen? Starta från en **konsekvent härdad bas** utan att "klicka överallt"; minska antalet förbiseenden; spara tid.
- Vad det ändrar (exempel): telemetri skärs, cookies/cache/referrer/HTTPS stärks, **RFP** + letterboxing, **WebRTC inaktiverad**, DoH/TLS-justeringar, chatty API:er begränsade.
- När ska du använda den: om du vill ha Firefox härdad på 10 minuter och accepterar några få undantag (DRM/streaming, Web visio, SSO/betalningar).
- Fördelar: snabb, konsekvent, **uppdaterad** (ESR-anpassad), mycket väl **dokumenterad** (wiki + kommentarer), **anpassningsbar** via åsidosättningar.
- Begränsningar: kompatibilitet (vissa webbappar), komfort (UTC, fönsterstorlekar) och en påminnelse: **det är inte Tor** (ingen nätverksanonymitet).



Installation (helst på en **dedikerad profil**)


1. Spara profil/favoriter och lista dina webbplatser med cookie-undantag.


2. Ladda ner `user.js` från `https://github.com/arkenfox/user.js` (ESR/stabil version).


3. Du hittar din profilmapp via `about:profiles`:




   - Windows: `%APPDATA%/Mozilla/Firefox/Profiler/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/Bibliotek/Applikationsstöd/Firefox/Profiler/...`


4. Stäng Firefox och flytta `user.js` till roten av profilmappen.


5. Återstarta; anpassa via `about:config` eller en overrides-fil.



Uppdateringar




- Följ Arkenfox-utgåvorna (ESR-anpassade), byt ut `user.js`, starta Firefox igen; läs releaseanteckningarna.



**Anpassning via Overrides**



Arkenfox är avsiktligt restriktiv som standard. För att anpassa vissa inställningar till dina behov (streaming, visio, specifika webbplatser) kan du skapa en `user-overrides.js`-fil i samma mapp som `user.js`. Med den här filen kan du "åsidosätta" vissa Arkenfox-inställningar utan att ändra huvudfilen.



Skapa `user-overrides.js` och lägg till dina anpassningar:


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



Bästa praxis




- Använd en separat **"Arkenfox"-profil** och behåll en "normal" profil för bekvämlighetens skull.
- Minimera tillägg (uBlock Origin OK) för att begränsa attackytan och unikheten.
- Lägg till undantag på varje enskild plats (skydda 🛡️, uBO, NoScript om det används) vid behov.
- Testa efter varje förändring: WebRTC/DNS-läckor, täck dina spår, CreepJS.



## Bästa praxis





- Uppdateringar**: Firefox och tillägg uppdaterade.
- Förlängningar**: rimliga och tillförlitliga; se upp för "tvivelaktiga" inlösen.
- Nedladdningar**: försiktighet; testa känsliga filer på VirusTotal.
- Lösenord**: **dedikerad hanterare** (Bitwarden, KeePassXC); **2FA** aktiverat; undvik att lagra i webbläsaren.
- Hygien**: begränsa Google/Facebook till behållare; stäng/öppna regelbundet för att "återställa" sammanhanget.



## Gränser och alternativ





- En härdad webbläsare ≠ nätverksanonymitet: utan **VPN** förblir din IP synlig; även med den förblir korrelation möjlig.
- Att modifiera för mycket kan göra dig **unik**. **RFP** standardiserar; randomiseringsverktyg (t.ex. Chameleon) kan ... göra dig annorlunda. Testa, jämför, justera.
- Alternativ/komplement:
 - Tor Browser: nätverksanonymitet via Tor; långsammare. Se vår kompletta installations- och konfigurationsguide**:



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb



 - Mullvad webbläsare: "Tor utan Tor", för att kombineras med VPN; standardiserat fotavtryck. Ta reda på hur du installerar den i vår dedikerade handledning**:



https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e



- Rekommenderade kombinationer: Firefox (nivå 2) + VPN för daglig användning; Tor/Mullvad för känsliga aktiviteter; separata profiler för uppdelning.



## Slutsats



Genom att följa denna steg-för-steg-guide har du förvandlat Firefox till ett verkligt bålverk mot digital övervakning. Från viktiga nivå 1-inställningar till avancerade Arkenfox-konfigurationer, varje ändring stärker din integritet utan att kompromissa med din surfupplevelse.



**Din integritet är nu bättre skyddad**: annonsspårare blockerade, cookies uppdelade, IP Address läckor neutraliserade, telemetri inaktiverad. Firefox är inte längre bara en webbläsare, utan ett digitalt motståndsverktyg som är skräddarsytt efter dina behov.



**Kom ihåg: sekretess är aldrig en självklarhet. Testa ditt skydd regelbundet, uppdatera dina inställningar och tveka inte att justera konfigurationen när dina vanor förändras. Din anonymitet på nätet beror lika mycket på dina verktyg som på dina vanor.



## Resurser



### Plan ₿ Network




- SCU 202 - Förbättra din personliga digitala säkerhet: För att lära dig mer om de digitala säkerhetskoncept som behandlas i denna handledning**



https://planb.network/courses/ameliorer-sa-securite-numerique-personnelle-4ba0e3de-e67f-4ea1-a514-f111206810d1

### Mozilla-dokumentation




- [Förbättrat spårningsskydd] (https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop): Officiell guide till förbättrat spårningsskydd
- [State Partitioning](https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning): Teknisk dokumentation om state partitioning
- [MDN Web Security](https://developer.mozilla.org/docs/Web/Security): Komplett referens om webbsäkerhet



### Arkenfox




- [Wiki- och installationsguide](https://github.com/arkenfox/user.js/wiki): Komplett dokumentation av Arkenfox-projektet
- [Insättningar och releaser](https://github.com/arkenfox/user.js): Ladda ner filen user.js och spåra uppdateringar



### Guider & samhällen




- [PrivacyGuides - Webbläsare för datorer](https://www.privacyguides.org/en/desktop-browsers/): Rekommendationer och jämförelser av webbläsare
- Reddit**: r/firefox, r/privacy för feedback och support
- PrivacyGuides forum**: djupgående tekniska diskussioner



### Testverktyg




- [Täck dina spår (EFF)] (https://coveryourtracks.eff.org/): Digitala fingeravtryck och antispårningseffektivitet
- [Test av DNS-läckage] (https://www.dnsleaktest.com/): DNS-läckagetest och DoH-effektivitet
- [BrowserLeaks] (https://browserleaks.com/): Komplett testsvit (WebRTC, Canvas, Fonts, etc.)
- [BadSSL] (https://badssl.com/): Tester för validering av SSL/TLS-certifikat
- [CreepJS] (https://abrahamjuliot.github.io/creepjs/): Avancerad analys av 50+ fingeravtrycksvektorer
- [Cloudflare DNS-test](https://1.1.1.1/help): Kontrollerar att Cloudflare DoH fungerar korrekt