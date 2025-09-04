---
name: Firefox
description: Hoe Firefox configureren om uw privacy te beschermen?
---

![cover](assets/cover.webp)



## Inleiding



We brengen allemaal uren online door, vaak zonder ons te realiseren wat onze browser over ons onthult. Elke klik, elke zoekopdracht, elke site die we bezoeken voedt een enorme industrie van persoonlijke gegevensverzameling.



![Statistiques navigateurs 2024](assets/fr/01.webp)


*Marktaandeel webbrowsers: Chrome domineert met 65% van de markt, gevolgd door Safari en Edge. Bron: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*



Zoals deze grafiek laat zien, domineert Google Chrome massaal, met meer dan 65% van het wereldwijde gebruik. Deze hegemonie betekent dat de meerderheid van de internetgebruikers hun surfgegevens toevertrouwt aan Google, een bedrijf waarvan het bedrijfsmodel is gebaseerd op gerichte reclame. Firefox, met slechts 3% van de markt, vertegenwoordigt een alternatief dat is ontwikkeld door Mozilla, een non-profitorganisatie die geen commercieel belang heeft bij het exploiteren van uw gegevens.



Maar Firefox kiezen is slechts de eerste stap. Standaard vereist zelfs Firefox aanpassingen om uw bescherming te maximaliseren. Deze gids neemt u stap voor stap mee, van de eenvoudigste tot de meest geavanceerde, om Firefox in een echt schild tegen tracking te veranderen met behoud van een prettige browse-ervaring.



### Waarom Firefox?





- Gratis en open-source** (Gecko-engine): controleerbare, transparante code
- Non-profitorganisatie**: Mozilla Foundation, missie van algemeen belang
- Ingebouwde native beveiligingen**: Verbeterde Trackingbescherming (ETP), Totale cookiebescherming (TCP), State Partitioning, Alleen HTTPS-modus, DNS over HTTPS (DoH)
- Geavanceerde aanpassingen**: in tegenstelling tot Chrome kunt u bij Firefox het gedrag diepgaand aanpassen



### Belangrijke principes voordat je begint





- Geen universeel recept**: hoe meer je aanpast, hoe meer je het risico loopt op te vallen (fingerprinting). Het doel is om beter beschermd te zijn zonder op te vallen.
- Stap-voor-stap vooruitgang**: Verander een instelling, test je gebruikelijke sites en ga dan verder. Je hoeft niet alles in één keer te veranderen.
- Persoonlijke balans**: Vind JOUW compromis tussen privacy en gebruiksgemak.



## Snelle installatie



![Téléchargement Firefox](assets/fr/02.webp)



**Officiële download:** Ga naar [firefox.com/browsers/desktop](https://www.firefox.com/en-US/browsers/desktop/). Selecteer op deze pagina je besturingssysteem (Windows, macOS, Linux) om toegang te krijgen tot de juiste downloadpagina met specifieke installatie-instructies.





- Windows**: download het `.exe` installatieprogramma, dubbelklik en volg de installatiewizard
- macOS**: download het `.dmg`-bestand, open het en sleep Firefox naar de map Toepassingen
- Linux**: verschillende opties beschikbaar - pakket `.deb`/`.rpm`, Flatpak (Flathub), Snap, of via pakketbeheerder (apt, dnf, pacman). Geef de voorkeur aan officiële Mozilla-bronnen.



**Tip:** Controleer na installatie op updates via Help → **Over Firefox** (belangrijk voor beveiligingspatches).



![Configuration initiale Firefox](assets/fr/03.webp)


*Eerste scherm bij het starten van Firefox: stel Firefox in als uw standaardbrowser, voeg deze toe aan uw snelkoppelingen en klik vervolgens op "Opslaan en doorgaan"*



![Création compte Firefox](assets/fr/04.webp)


*Optionele stap: een Firefox-account aanmaken of u aanmelden. U kunt deze stap overslaan door rechtsonder op "Niet nu" te klikken*



![Page d'accueil Firefox](assets/fr/05.webp)


*Het startscherm van Firefox zodra de configuratie is voltooid. Let op het ☰-menu rechtsboven, dat toegang geeft tot Instellingen en Extensies voor het aanpassen van Firefox*



## Standaard al beveiligingen geactiveerd (geruststellend)





- Site-isolatie (Fission)**: in progressieve implementatie. Deze functie voert elke site in een apart proces uit om te voorkomen dat een kwaadaardig tabblad toegang krijgt tot de gegevens van een ander. Controleer de status via `about:support` (zoek naar "Fission"). Als het niet is ingeschakeld, kun je het handmatig activeren in `about:config` met `fission.autostart = true`.
- Total Cookie Protection (TCP)**: standaard actief. Cookies en andere opslag worden beperkt tot de site van de eerste partij (één "potje" per site), waardoor cross-site tracking wordt geneutraliseerd. Waar nodig worden tijdelijke uitzonderingen gemaakt via de Storage Access API (geïntegreerde aanmeldingsknoppen).
- Bescherming tegen volgen via bounce/omleiding**: Firefox detecteert en ruimt automatisch cookies op die zijn achtergelaten door bounce-sites (koppelingen die u via een tracker vóór de bestemming omleiden), waardoor dit trackingkanaal zonder enige actie van uw kant wordt verminderd.



## Niveau 1 - Essentieel (≤ 10 minuten)



Doel: grote privacywinst zonder het web kapot te maken. Voor 90% van de gebruikers.



Om de instellingen te openen, klikt u op het menu ☰ rechtsboven en vervolgens op **"Instellingen"**:



![Paramètres généraux](assets/fr/07.webp)


*Firefox-instellingenpagina - tabblad "Algemeen". Hier configureert u de meeste van uw privacyopties*



**Tracking bescherming (ETP)**




- Schakel **ETP** over naar **Strict**. Je blokkeert meer trackers (cross-site cookies, fingerprinting, cryptomining, sociale widgets...).
- Als een site breekt (video, aanmeldknop...), deactiveer dan alleen de bescherming voor die site via het schild 🛡️ en vernieuw vervolgens het tabblad.



Hier zijn de verschillende ETP beveiligingsniveaus:




- Standaard** (gebalanceerd, maximale compatibiliteit)
  - Blokkeert: sociale trackers, cross-site cookies (alle vensters), inhoud volgen in privénavigatie, cryptocurrency miners, vingerafdrukdetectors.
  - Inclusief **Total Cookie Protection** (TCP): één potje per site.
- Strict** (aanbevolen voor vertrouwelijkheid)
  - Blokkeert ook tracking-inhoud in alle vensters + bekende en vermoede vingerafdrukken.
  - Kan sommige sites breken; gebruik het 🛡️ schild voor een lokale uitzondering.
- Aangepast** (geavanceerd)
  - Fijnafstemming: cookies, tracking-inhoud, minderjarigen, vingerafdrukken (bekend/verdacht).



![Paramètres protection contre le pistage](assets/fr/06.webp)



**Cookies en sitegegevens




- Schakel **"Cookies en sitegegevens verwijderen bij afsluiten"** in om elke keer dat u opnieuw opstart schoon te beginnen.
- Voeg **Uitzonderingen** toe voor 2-3 essentiële sites als je dat wilt (e-mail, bank).


**Automatische gegevensinvoer, suggesties en startpagina**




- Deactiveer **autofill** (ID's, adressen, kaarten). Gebruik in plaats daarvan een wachtwoordmanager.
- Zoeken**: uitschakelen **"Zoeksuggesties weergeven"**.
- Address balk**: knip **"Gesponsorde suggesties"** en **"Contextuele suggesties"**.
- Home**: schakel **Pocket** en **gesponsorde inhoud** uit.



![Paramètres cookies et mots de passe](assets/fr/08.webp)



*alleen *HTTPS**




- Activeer **"HTTPS-modus alleen in alle vensters"**.


![Configuration DNS over HTTPS](assets/fr/09.webp)



**Telemetrie en reclamemeting




- Schakel bij "Gegevensverzameling door Firefox" **alles** uit.
- Deactiveer **"Privacyvriendelijke advertentiemaatregelen"** (PPA).
- Safe Browsing**: ingeschakeld houden (aanbevolen). Firefox controleert sites op dreigingslijsten via gehashte query's en lokale controles, en beschermt zo tegen phishing en malware met minimale gevolgen voor de privacy.



**Global Privacy Control (optioneel)**




- Activeer de **GPC** om aan te geven dat u weigert gegevens te verkopen/delen.



**Zoekmachine




- Schakel over naar **DuckDuckGo**, **Startpage**, **Qwant** of **Brave Search** (Instellingen → Zoeken).



![Configuration moteur de recherche DuckDuckGo](assets/fr/11.webp)



**Privénavigatie**




- Privévensters (Ctrl/Cmd+Shift+P) voor eenmalige sessies (cadeaus, secundaire accounts...). Vermijd de modus "altijd privé": extensies kunnen inactief zijn en cookie-uitzonderingen zijn minder nuttig.



**Essentiële extensies** (installeren vanuit de officiële catalogus)




- uBlock Origin**: blokkeert advertenties en huidige tracking, lichtgewicht.
- Privacy Badger**: leert te blokkeren wat jou volgt; stuurt Do Not Track / GPC.
- ClearURLs** (optioneel): Firefox (ETP Strict) en uBO ruimen al veel op; bewaar deze als je nog steeds "vuile" URL's ziet (utm, fbclid).
- Firefox Containers voor meerdere accounts**: **isoleert cookies/sessies en opslag per container; parallelle multi-accounts; minder cross-site tracking**. Officiële extensie: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.



![Extension Multi-Account Containers](assets/fr/12.webp)



**Wachtwoorden en 2FA**




- Gebruik een speciale wachtwoordmanager** (Bitwarden, KeePassXC). **Vermijd** het opslaan van wachtwoorden in de browser. **Enable 2FA** waar mogelijk.



## Niveau 2 - Versterkt (Compartimentering & Netwerk)



Doel: activiteiten compartimenteren en netwerklekken verminderen.



**DNS over HTTPS (DoH)**




- Standaardstatus**: Automatisch geactiveerd in sommige regio's (VS, Canada, Rusland, Oekraïne). Elders handmatige activering vereist.
- Configuratie**: Instellingen → Algemeen → Netwerkinstellingen → **DoH inschakelen** → **Cloudflare** of **Quad9** → **Maximale bescherming**.
- Maximale bescherming = alleen TRR** (geen fallback naar systeem DNS). Als een bedrijfs-/hotelnetwerk blokkeert, schakel dan terug naar **Standaard** of schakel DoH uit.
- Redundantie**: Als je al een vertrouwd VPN gebruikt met een eigen beveiligde DNS, kan DoH overbodig zijn.
- Controletest**: `https://www.dnsleaktest.com/` moet alleen de gekozen DoH provider weergeven.



![Sélection fournisseur DNS Cloudflare](assets/fr/10.webp)



**Compartimentering met containers en profielen




- Containers met meerdere accounts**: maak ruimtes (Persoonlijk, Werk, Financiën, Sociale netwerken, Winkelen, Wegwerp). Configureer **"Altijd openen in deze container"** voor uw terugkerende sites. Officiële extensie: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.
- Waarom zou je ze gebruiken?
  - Sterke isolatie** van cookies/sessies/opslag per ruimte.
  - Minder cross-site tracking**: beperk de reuzen (Facebook, Google).
  - Gelijktijdige multi-accounts** op dezelfde service.
  - Minder risico op CSRF/XSS** tussen gesegmenteerde identiteiten.
  - Tip: op zijn minst speciale containers voor Sociale netwerken/Google, Werk, Financiën.
- Facebook Container** (optioneel): een vereenvoudigde versie speciaal voor FB/Instagram.
- Aparte profielen**: via `about:profiles` (hoofdprofiel, minimaal "ultraveilig" profiel, testprofiel). Volledige compartimentering van gegevens en extensies.



**Geavanceerde uitbreidingen** (nog te reserveren)




- Cookie AutoDelete**: verwijdert de cookies van een website zodra het tabblad wordt gesloten (handig als Firefox lange tijd open staat).
- LocalCDN**: serveert de huidige bibliotheken lokaal (vermindert oproepen naar Google/Microsoft). Gedeeltelijke compatibiliteit.



**Mobiel (Android)**




- Firefox Android + uBlock Origin**: vergelijkbare bescherming onderweg.



## Niveau 3 - Expert (about:config & Arkenfox)



Doel: geavanceerde verharding met geaccepteerde compromissen. Aanbevolen op een **afzonderlijk profiel**.



Kies slechts één van de volgende twee benaderingen:



**Aanpak A - Handmatige aanpassingen**: Een paar gerichte aanpassingen via `about:config` (eenvoudiger, preciezere controle)


**Aanpak B - Arkenfox user.js**: Volledig geautomatiseerde configuratie (complexer, maximale bescherming)



➡️ **Arkenfox bevat al ALLE about:config wijzigingen die hieronder worden genoemd** + honderden meer. Als u voor Arkenfox kiest, negeer dan de about:config sectie.



### Aanpak A: Handmatige wijzigingen via about:config



Typ `about:config` in de Address balk → Accepteer risico.



![Avertissement about:config](assets/fr/13.webp)



![Interface about:config](assets/fr/14.webp)



![Préférences about:config](assets/fr/15.webp)





- Weerstand tegen fingerprinting (geërfd van Tor Browser)


```text
privacy.resistFingerprinting = true
```


Effecten: UTC-tijdzone, **letterboxing** (standaard venstergroottes), gestandaardiseerde User-Agent/policies, Canvas/WebGL/AudioContext beperkingen. Meer uniformiteit, maar een paar "eigenaardigheden" (compensatietijd, soms een beetje Engels).





- WebRTC uitschakelen (voorkomt IP-lekken; breekt Webvisio)


```text
media.peerconnection.enabled = false
```





- Referer plus compatibel (standaard)


```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```


Strikte optie (kan betalingen/SSO verbreken):


```text
network.http.referer.XOriginPolicy = 2
```





- Het beperken van chatterende API's en speculatie


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



Gouden regel: als er iets kapot gaat, ga dan terug naar de laatste wijziging.



### Benadering B: Arkenfox user.js (volledig geautomatiseerde configuratie)



Het **Arkenfox** project biedt een door de community onderhouden `user.js` bestand dat automatisch honderden privacy- en beveiligingsgerichte Firefox-voorkeuren toepast. Bij het opnieuw opstarten leest Firefox dit bestand uit uw profiel en past deze instellingen toe.





- Wat is het nut? Start vanuit een **consistente geharde basis** zonder "overal te klikken"; verminder fouten; bespaar tijd.
- Wat het verandert (voorbeelden): telemetrie onderbroken, cookies/cache/referrer/HTTPS versterkt, **RFP** + letterboxing, **WebRTC uitgeschakeld**, DoH/TLS aanpassingen, chatachtige API's beperkt.
- Wanneer te gebruiken: als je Firefox in 10 minuten gehard wilt hebben en een paar uitzonderingen wilt accepteren (DRM/streaming, Webvisio, SSO/betalingen).
- Voordelen: snel, consistent, **bijgewerkt** (ESR-aligned), zeer goed **gedocumenteerd** (wiki + commentaar), **aanpasbaar** via overschrijvingen.
- Beperkingen: compatibiliteit (sommige webapps), comfort (UTC, venstergroottes) en een geheugensteuntje: **het is geen Tor** (geen netwerkanonimiteit).



Installatie (idealiter op een **dedicated profiel**)


1. Sla profiel/favorieten op en maak een lijst van je sites met cookie-uitzonderingen.


2. Download `user.js` van `https://github.com/arkenfox/user.js` (ESR/stable versie).


3. Zoek je profielmap via `about:profiles`:




   - Windows: `%APPDATA%/Mozilla/Firefox/Profiles/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/Library/Application Support/Firefox/Profiles/...`


4. Sluit Firefox en verplaats `user.js` naar de root van de profielmap.


5. Herstart; pas aan via `about:config` of een overrides bestand.



Updates




- Volg de Arkenfox-releases (ESR uitgelijnd), vervang de `user.js`, start Firefox opnieuw; lees de release notes.



**Aanpassing via Overrides**



Arkenfox is standaard opzettelijk restrictief. Om bepaalde instellingen aan te passen aan uw behoeften (streaming, visio, specifieke sites), kunt u een `user-overrides.js` bestand aanmaken in dezelfde map als `user.js`. Met dit bestand kunt u bepaalde voorkeuren van Arkenfox "opheffen" zonder het hoofdbestand aan te passen.



Maak `user-overrides.js` en voeg je aanpassingen toe:


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



Beste praktijken




- Gebruik een apart **"Arkenfox"-profiel** en behoud een "normaal" profiel voor comfort.
- Minimaliseer extensies (uBlock Origin OK) om aanvalsoppervlak en uniciteit te beperken.
- Voeg per site uitzonderingen toe (schild 🛡️, uBO, NoScript indien gebruikt) wanneer nodig.
- Test na elke wijziging: WebRTC/DNS-lekken, Dek je sporen, CreepJS.



## Beste praktijken





- Updates**: Firefox en extensies bijgewerkt.
- Verlengingen**: redelijk en betrouwbaar; kijk uit voor "dubieuze" aflossingen.
- Downloads**: let op; test gevoelige bestanden op VirusTotal.
- Wachtwoorden**: **dedicated manager** (Bitwarden, KeePassXC); **2FA** ingeschakeld; voorkom opslaan in browser.
- Hygiëne**: beperk Google/Facebook tot containers; sluit/open regelmatig om de context te "resetten".



## Grenzen & alternatieven





- Een verharde browser ≠ netwerkanonimiteit: zonder **VPN** blijft je IP zichtbaar; zelfs met blijft correlatie mogelijk.
- Te veel aanpassen kan je **uniek** maken. **RFP** standaardiseert; randomisatietools (bijv. Kameleon) kunnen... je onderscheiden. Test, vergelijk, pas aan.
- Alternatieven/complementen:
 - Tor Browser: netwerkanonimiteit via Tor; langzamer. Bekijk onze volledige installatie- en configuratiegids**:



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb



 - Mullvad-browser: "Tor zonder Tor", te combineren met VPN; gestandaardiseerde footprint. Ontdek hoe je het installeert in onze speciale tutorial**:



https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e



- Aanbevolen combinaties: Firefox (Level 2) + VPN voor dagelijks gebruik; Tor/Mullvad voor gevoelige activiteiten; aparte profielen voor compartimentering.



## Conclusie



Door deze stapsgewijze handleiding te volgen, hebt u Firefox omgetoverd tot een waar bolwerk tegen digitale surveillance. Van essentiële niveau 1-instellingen tot geavanceerde Arkenfox-configuraties, elke wijziging versterkt uw privacy zonder uw surfervaring in gevaar te brengen.



**Uw privacy is nu beter beschermd**: advertentietrackers geblokkeerd, cookies gecompartimenteerd, IP Address lekken geneutraliseerd, telemetrie uitgeschakeld. Firefox is niet langer alleen een browser, maar een digitaal weerstandsmiddel op maat van uw behoeften.



**Onthoud: vertrouwelijkheid is nooit vanzelfsprekend. Test je bescherming regelmatig, werk je instellingen bij en aarzel niet om je configuratie aan te passen als je gewoonten veranderen. Je online anonimiteit hangt evenveel af van je tools als van je gewoontes.



## Bronnen



### Plan ₿ Network




- SCU 202 - Uw persoonlijke digitale veiligheid verbeteren: Voor meer informatie over de concepten voor digitale beveiliging die in deze tutorial aan bod komen**



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Mozilla-documentatie




- [Verbeterde Trackingbescherming](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop): Officiële gids voor verbeterde trackingbescherming
- [State Partitioning](https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning): Technische documentatie over partitionering van toestanden
- [MDN Webbeveiliging](https://developer.mozilla.org/docs/Web/Security): Volledige referentie over webbeveiliging



### Arkenfox




- [Wiki en installatiegids](https://github.com/arkenfox/user.js/wiki): Volledige documentatie over het Arkenfox-project
- [Stortingen en releases](https://github.com/arkenfox/user.js): Het bestand user.js downloaden en updates bijhouden



### Gidsen & gemeenschappen




- [PrivacyGidsen - Desktopbrowsers](https://www.privacyguides.org/en/desktop-browsers/): Browseraanbevelingen en -vergelijkingen
- Reddit**: r/firefox, r/privacy voor feedback en ondersteuning
- PrivacyGuides forum**: diepgaande technische discussies



### Testgereedschap




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/): Digitale vingerafdrukken en de effectiviteit van anti-tracking
- [DNS-lektest](https://www.dnsleaktest.com/): DNS-lektest en DoH-efficiëntie
- [BrowserLeaks](https://browserleaks.com/): Volledige testsuite (WebRTC, Canvas, lettertypen, enz.)
- [BadSSL](https://badssl.com/): SSL/TLS-certificaat validatietests
- [CreepJS](https://abrahamjuliot.github.io/creepjs/): Geavanceerde analyse van 50+ vingerafdrukvectoren
- [Cloudflare DNS Test](https://1.1.1.1/help): Controleren of Cloudflare DoH goed werkt
