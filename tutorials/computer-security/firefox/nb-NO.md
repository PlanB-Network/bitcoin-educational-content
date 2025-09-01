---
name: Firefox
description: Hvordan konfigurerer du Firefox for å beskytte personvernet ditt?
---

![cover](assets/cover.webp)



## Innledning



Vi tilbringer alle timevis på nettet, ofte uten å være klar over hva nettleseren vår avslører om oss. Hvert klikk, hvert søk, hvert nettsted vi besøker, gir næring til en enorm industri for innsamling av personopplysninger.



![Statistiques navigateurs 2024](assets/fr/01.webp)


*Markedsandel for nettlesere: Chrome dominerer med 65 % av markedet, etterfulgt av Safari og Edge. Kilde: [gs.statcounter.com [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*



Som denne grafen viser, dominerer Google Chrome massivt, med over 65 % av bruken på verdensbasis. Dette hegemoniet betyr at flertallet av Internett-brukerne overlater nettleserdataene sine til Google, et selskap hvis forretningsmodell er basert på målrettet reklame. Firefox, med bare 3 % av markedet, representerer et alternativ som er utviklet av Mozilla, en ideell organisasjon som ikke har noen kommersiell interesse av å utnytte dataene dine.



Men å velge Firefox er bare det første steget. Som standard krever selv Firefox justeringer for å maksimere beskyttelsen din. Denne veiledningen tar deg steg for steg, fra det enkleste til det mest avanserte, for å forvandle Firefox til et veritabelt skjold mot sporing, samtidig som du får en behagelig surfeopplevelse.



### Hvorfor Firefox?





- Fri og åpen kildekode** (Gecko-motor): reviderbar, transparent kode
- Ideell organisasjon**: Mozilla Foundation, oppdrag av allmenn interesse
- Innebygd innebygd beskyttelse**: Enhanced Tracking Protection (ETP), Total Cookie Protection (TCP), State Partitioning, kun HTTPS-modus, DNS over HTTPS (DoH)
- Avansert tilpasning**: I motsetning til Chrome lar Firefox deg endre oppførselen i dybden



### Viktige prinsipper før du begynner





- Det finnes ingen universaloppskrift**: Jo mer du modifiserer, desto mer risikerer du å skille deg ut (fingeravtrykk). Målet er å være bedre beskyttet uten å skille seg ut fra mengden.
- Trinnvis fremgang**: Endre en innstilling, test de vanlige nettstedene dine, og fortsett deretter. Det er ikke nødvendig å endre alt på én gang.
- Personlig balanse**: Finn ditt kompromiss mellom personvern og brukervennlighet.



## Rask installasjon



![Téléchargement Firefox](assets/fr/02.webp)



**Offisiell nedlasting:** Gå til [firefox.com/browsers/desktop] (https://www.firefox.com/en-US/browsers/desktop/). På denne siden velger du operativsystem (Windows, macOS, Linux) for å få tilgang til den aktuelle nedlastingssiden med spesifikke installasjonsinstruksjoner.





- Windows**: Last ned installasjonsprogrammet `.exe`, dobbeltklikk og følg installasjonsveiviseren
- macOS**: Last ned .dmg-filen, åpne den og dra Firefox inn i Programmer-mappen
- Linux**: flere alternativer tilgjengelig - pakke `.deb`/`.rpm`, Flatpak (Flathub), Snap, eller via pakkebehandler (apt, dnf, pacman). Foretrekker offisielle Mozilla-kilder.



**Tips:** Når du har installert programmet, se etter oppdateringer via Hjelp → **Om Firefox** (viktig for sikkerhetsoppdateringer).



![Configuration initiale Firefox](assets/fr/03.webp)


*Første skjermbilde ved oppstart av Firefox: Angi Firefox som standard nettleser, legg den til i snarveiene dine, og klikk deretter på "Lagre og fortsett"*



![Création compte Firefox](assets/fr/04.webp)


*Valgfritt trinn: Opprett eller logg inn på en Firefox-konto. Du kan hoppe over dette trinnet ved å klikke på "Ikke nå" nederst til høyre*



![Page d'accueil Firefox](assets/fr/05.webp)


*Firefox-startskjermen når konfigurasjonen er fullført. Legg merke til ☰-menyen øverst til høyre, som gir tilgang til Innstillinger og Utvidelser for å tilpasse Firefox*



## Beskyttelsen er allerede aktivert som standard (betryggende)





- Isolering av nettsteder (Fission)**: i progressiv distribusjon. Denne funksjonen kjører hvert nettsted i en separat prosess for å forhindre at en ondsinnet fane får tilgang til dataene på en annen. Sjekk statusen via `about:support` (søk etter "Fission"). Hvis den ikke er aktivert, kan du aktivere den manuelt i `about:config` med `fission.autostart = true`.
- Total Cookie Protection (TCP)**: aktiv som standard. Informasjonskapsler og annen lagring er begrenset til førstepartsnettstedet (én "krukke" per nettsted), noe som nøytraliserer sporing på tvers av nettsteder. Midlertidige unntak gjøres via API-et for lagringstilgang når det er nødvendig (integrerte påloggingsknapper).
- Beskyttelse mot sporing av avvisning/omdirigering**: Firefox oppdager og rydder automatisk opp i informasjonskapsler som etterlates av avvisningssider (lenker som viderekobler deg via en sporingsenhet før målet), og reduserer denne sporingskanalen uten at du trenger å gjøre noe.



## Nivå 1 - Nødvendig (≤ 10 minutter)



Mål: store personverngevinster uten å ødelegge nettet. For 90 % av brukerne.



For å få tilgang til innstillingene, klikk på menyen ☰ øverst til høyre, og deretter **"Innstillinger"**:



![Paramètres généraux](assets/fr/07.webp)


*Firefox-innstillingssiden - fanen "Generelt". Det er her du konfigurerer de fleste personvernalternativene*



**Beskyttelse mot sporing (ETP)**




- Bytt **ETP** til **Strict**. Du blokkerer flere sporere (informasjonskapsler på tvers av nettsteder, fingeravtrykk, kryptomining, sosiale widgeter ...).
- Hvis et nettsted går i stykker (video, påloggingsknapp ...), deaktiverer du beskyttelsen bare for det nettstedet via 🛡️ shield, og oppdaterer deretter fanen.



Her er de ulike sikkerhetsnivåene for ETP:




- Standard** (balansert, maksimal kompatibilitet)
  - Blokkerer: sosiale sporere, informasjonskapsler på tvers av nettsteder (alle vinduer), sporing av innhold i privat surfing, utvinnere av kryptovaluta, fingeravtrykksdetektorer.
  - Inkluderer **Total Cookie Protection** (TCP): én krukke per nettsted.
- Strict** (anbefalt av hensyn til konfidensialitet)
  - Blokkerer også sporingsinnhold i alle vinduer + kjente og mistenkte fingeravtrykk.
  - Kan ødelegge noen nettsteder; bruk 🛡️ shield for et lokalt unntak.
- Tilpasset** (avansert)
  - Finjustering: informasjonskapsler, sporing av innhold, mindreårige, fingeravtrykk (kjent/mistenkt).



![Paramètres protection contre le pistage](assets/fr/06.webp)



**Cookies og nettstedsdata




- Aktiver **"Slett informasjonskapsler og nettsteddata ved avslutning"** for å starte på nytt hver gang du starter på nytt.
- Legg til **Undtak** for 2-3 viktige nettsteder hvis du ønsker det (e-post, bank).


**Automatisk dataregistrering, forslag og startside**




- Deaktiver **automatisk utfylling** (ID-er, adresser, kort). Bruk en passordbehandler i stedet.
- Søk**: deaktiver **"Vis søkeforslag"**.
- Address bar**: kutt **"Sponsede forslag"** og **"Kontekstuelle forslag"**.
- Hjem**: Deaktiver **Pocket** og **sponset innhold**.



![Paramètres cookies et mots de passe](assets/fr/08.webp)



**Kun https




- Aktiver **"HTTPS-modus bare i alle vinduer"**.


![Configuration DNS over HTTPS](assets/fr/09.webp)



**Telemetri og måling av reklame




- I "Datainnsamling av Firefox", **hev avmerkingen for alle**.
- Deaktiver **"Personvernvennlige annonseringstiltak"** (PPA).
- Safe Browsing**: Hold det aktivert (anbefalt). Firefox sjekker nettsteder mot trussellister via hashede spørringer og lokale kontroller, noe som beskytter mot phishing og skadelig programvare med minimal innvirkning på personvernet.



**Global personvernkontroll (valgfritt)**




- Aktiver **GPC** for å signalisere at du nekter å selge/dele data.



**Søkemotor




- Bytt til **DuckDuckGo**, **Startpage**, **Qwant** eller **Brave Search** (Innstillinger → Søk).



![Configuration moteur de recherche DuckDuckGo](assets/fr/11.webp)



**Privat navigasjon**




- Private vinduer (Ctrl/Cmd+Shift+P) for engangsøkter (gaver, sekundære kontoer...). Unngå "alltid privat"-modus: utvidelser kan være inaktive og cookie-unntak mindre nyttige.



**Essensielle utvidelser** (installer fra den offisielle katalogen)




- uBlock Origin**: blokkerer annonser og sporing av strøm, lettvekt.
- Privacy Badger**: lærer seg å blokkere det som følger deg; sender Do Not Track / GPC.
- ClearURLs** (valgfritt): Firefox (ETP Strict) og uBO rydder allerede opp mye; behold den hvis du fremdeles ser "skitne" nettadresser (utm, fbclid).
- Beholdere med flere Firefox-kontoer**: **isolerer informasjonskapsler/økter og lagring per container; parallelle multikontoer; mindre sporing på tvers av nettsteder**. Offisiell utvidelse: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.



![Extension Multi-Account Containers](assets/fr/12.webp)



*passord og 2FA** *Passord og 2FA




- Bruk en dedikert passordbehandler** (Bitwarden, KeePassXC). **Unngå** å lagre passord i nettleseren. **Aktiver 2FA** der det er mulig.



## Nivå 2 - Forsterket (oppdeling og nettverk)



Mål: Oppdele aktiviteter og redusere nettverkslekkasje.



**DNS over HTTPS (DoH)**




- Standard status**: Automatisk aktivert i enkelte regioner (USA, Canada, Russland, Ukraina). Andre steder kreves manuell aktivering.
- Konfigurasjon**: Innstillinger → Generelt → Nettverksinnstillinger → **Aktiver DoH** → **Cloudflare** eller **Quad9** → **Maksimal beskyttelse**.
- Maksimal beskyttelse = kun TRR** (ingen tilbakefall til system-DNS). Hvis et bedrifts-/hotellnettverk blokkerer, bytter du tilbake til **Standard** eller deaktiverer DoH.
- Redundans**: Hvis du allerede bruker et pålitelig VPN med egen sikker DNS, kan DoH være overflødig.
- Verifikasjonstest**: `https://www.dnsleaktest.com/` skal bare vise den valgte DoH-leverandøren.



![Sélection fournisseur DNS Cloudflare](assets/fr/10.webp)



**Oppdeling med containere og profiler




- Containere med flere kontoer**: opprett mellomrom (personlig, jobb, økonomi, sosiale nettverk, shopping, engangsbruk). Konfigurer ** "Åpne alltid i denne beholderen"** for dine tilbakevendende nettsteder. Offisiell utvidelse: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.
- Hvorfor bruke dem?
  - Sterk isolering** av informasjonskapsler/økter/lagring etter plass.
  - Mindre sporing på tvers av nettsteder**: Begrens gigantene (Facebook, Google).
  - Flere kontoer** samtidig på samme tjeneste.
  - Mindre risiko for CSRF/XSS** mellom segmenterte identiteter.
  - Tips: I det minste dedikerte beholdere for sosiale nettverk/Google, arbeid og økonomi.
- Facebook Container** (valgfritt): en forenklet versjon dedikert til FB/Instagram.
- Separate profiler**: via `about:profiles` (hovedprofil, minimal "ultra-sikker" profil, testprofil). Total oppdeling av data og utvidelser.



**Avanserte utvidelser** (må reserveres)




- Cookie AutoDelete**: sletter informasjonskapslene til et nettsted så snart fanen lukkes (nyttig hvis Firefox er åpen i lang tid).
- LocalCDN**: serverer aktuelle biblioteker lokalt (reduserer anrop til Google/Microsoft). Delvis kompatibilitet.



**Mobil (Android)**




- Firefox Android + uBlock Origin**: lignende beskyttelse når du er på farten.



## Nivå 3 - Ekspert (about:config & Arkenfox)



Mål: avansert herding med aksepterte kompromisser. Anbefales på en **separat profil**.



Velg bare én av følgende to tilnærminger:



**Tilnærming A - Manuelle endringer**: Noen få målrettede justeringer via `about:config` (enklere, mer presis kontroll)


**Tilnærming B - Arkenfox user.js**: Fullautomatisk konfigurasjon (mer kompleks, maksimal beskyttelse)



➡️ **Arkenfox inkluderer allerede ALLE about:config-endringene som er nevnt nedenfor** + hundrevis flere. Hvis du velger Arkenfox, kan du ignorere about:config-delen.



### Tilnærming A: Manuelle endringer via about:config



Skriv inn `about:config` i Address-linjen → Godta risiko.



![Avertissement about:config](assets/fr/13.webp)



![Interface about:config](assets/fr/14.webp)



![Préférences about:config](assets/fr/15.webp)





- Motstand mot fingeravtrykk (arvet fra Tor Browser)


```text
privacy.resistFingerprinting = true
```


Effekter: UTC-tidssone, **bokstavboksing** (standard vindusstørrelser), standardiserte brukeragenter/policyer, Canvas/WebGL/AudioContext-restriksjoner. Mer ensartethet, men noen få "særegenheter" (forskjøvet tid, noen ganger litt engelsk).





- Deaktiver WebRTC (unngår IP-lekkasjer, men ødelegger Web visio)


```text
media.peerconnection.enabled = false
```





- Referer pluss kompatibel (standard)


```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```


Strengt alternativ (kan bryte betalinger/SSO):


```text
network.http.referer.XOriginPolicy = 2
```





- Begrensning av API-er og spekulasjoner


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



Gylden regel: Hvis noe går i stykker, går du tilbake til den siste endringen.



### Tilnærming B: Arkenfox user.js (helautomatisk konfigurasjon)



**Arkenfox**-prosjektet tilbyr en fellesskapsvedlikeholdt `user.js`-fil som automatisk bruker hundrevis av personvern- og sikkerhetsorienterte Firefox-preferanser. Når du starter Firefox på nytt, leser Firefox denne filen fra profilen din og bruker disse innstillingene.





- Hva er poenget? Start fra en **konsekvent, herdet base** uten å "klikke overalt"; færre forglemmelser; spare tid.
- Hva det endrer (eksempler): telemetri kuttet, cookies/cache/referrer/HTTPS styrket, **RFP** + letterboxing, **WebRTC deaktivert**, DoH/TLS-justeringer, chatty API-er begrenset.
- Når bør du bruke den: Hvis du vil ha Firefox herdet på 10 minutter og aksepterer noen få unntak (DRM/strømming, Web visio, SSO/betaling).
- Fordeler: rask, konsistent, **oppdatert** (ESR-justert), svært godt **dokumentert** (wiki + kommentarer), **tilpassbar** via overstyringer.
- Begrensninger: kompatibilitet (noen webapper), komfort (UTC, vindusstørrelser), og en påminnelse: **det er ikke Tor** (ingen nettverksanonymitet).



Installasjon (ideelt sett på en **dedikert profil**)


1. Lagre profil/favoritter og liste opp nettsteder med unntak for informasjonskapsler.


2. Last ned `user.js` fra `https://github.com/arkenfox/user.js` (ESR/stable-versjon).


3. Finn profilmappen din via `about:profiles`:




   - Windows: `%APPDATA%/Mozilla/Firefox/Profiler/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/Library/Application Support/Firefox/Profiles/...``


4. Lukk Firefox og flytt `user.js` til roten av profilmappen.


5. Start på nytt; tilpass via `about:config` eller en overstyringsfil.



Oppdateringer




- Følg Arkenfox-utgivelsene (ESR-tilpasset), erstatt `user.js`, start Firefox på nytt; les utgivelsesmerknadene.



**Tilpasning via Overrides**



Arkenfox er bevisst restriktiv som standard. For å tilpasse visse innstillinger til dine behov (streaming, visio, spesifikke nettsteder), kan du opprette en `user-overrides.js`-fil i samme mappe som `user.js`. Denne filen lar deg "overstyre" visse Arkenfox-preferanser uten å endre hovedfilen.



Opprett `user-overrides.js`, og legg til tilpasningene dine:


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



Beste praksis




- Bruk en egen **"Arkenfox"-profil** og behold en "normal" profil for komfort.
- Minimer utvidelser (uBlock Origin OK) for å begrense angrepsflaten og unikhet.
- Legg til unntak for hvert enkelt nettsted (skjold 🛡️, uBO, NoScript hvis det brukes) når det er nødvendig.
- Test etter hver endring: WebRTC/DNS-lekkasjer, dekk sporene dine, CreepJS.



## Beste praksis





- Oppdateringer**: Firefox og utvidelser er oppdatert.
- Forlengelser**: rimelige og pålitelige; se opp for "tvilsomme" innløsninger.
- Nedlastinger**: forsiktighet; test sensitive filer på VirusTotal.
- Passord**: **dedikert manager** (Bitwarden, KeePassXC); **2FA** aktivert; unngå lagring i nettleseren.
- Hygiene**: Begrens Google/Facebook til containere; lukk/åpne regelmessig for å "tilbakestille" konteksten.



## Grenser og alternativer





- En herdet nettleser ≠ nettverksanonymitet: Uten **VPN** forblir IP-en din synlig; selv med den er korrelasjon fortsatt mulig.
- Hvis du modifiserer for mye, kan det gjøre deg **unik**. **RFP** standardiserer; randomiseringsverktøy (f.eks. Chameleon) kan ... gjøre deg unik. Test, sammenlign, juster.
- Alternativer/supplementer:
 - Tor Browser: nettverksanonymitet via Tor; tregere. Se vår komplette installasjons- og konfigurasjonsveiledning**:



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb



 - Mullvad Browser: "Tor uten Tor", som kan kombineres med VPN; standardisert fotavtrykk. Finn ut hvordan du installerer den i vår dedikerte veiledning**:



https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e



- Anbefalte kombinasjoner: Firefox (nivå 2) + VPN for daglig bruk; Tor/Mullvad for sensitive aktiviteter; separate profiler for oppdeling.



## Konklusjon



Ved å følge denne trinnvise veiledningen har du forvandlet Firefox til et ekte bolverk mot digital overvåking. Fra viktige nivå 1-innstillinger til avanserte Arkenfox-konfigurasjoner - hver eneste endring styrker personvernet ditt uten at det går på bekostning av nettleseropplevelsen.



**Personvernet ditt er nå bedre beskyttet**: annonsesporere blokkert, informasjonskapsler oppdelt, IP Address-lekkasjer nøytralisert, telemetri deaktivert. Firefox er ikke lenger bare en nettleser, men et digitalt motstandsverktøy som er skreddersydd til dine behov.



**Husk: konfidensialitet er aldri en selvfølge. Test beskyttelsen regelmessig, oppdater innstillingene, og ikke nøl med å justere konfigurasjonen etter hvert som vanene dine endres. Din anonymitet på nettet avhenger like mye av verktøyene dine som av hvordan du bruker dem.



## Ressurser



### Plan ₿ Network




- SCU 202 - Forbedre din personlige digitale sikkerhet: For å lære mer om de digitale sikkerhetskonseptene som dekkes i denne opplæringen**



https://planb.network/courses/ameliorer-sa-securite-numerique-personnelle-4ba0e3de-e67f-4ea1-a514-f111206810d1

### Mozilla-dokumentasjon




- [Forbedret sporingsbeskyttelse] (https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop): Offisiell guide til forbedret sporingsbeskyttelse
- [State Partitioning] (https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning): Teknisk dokumentasjon om tilstandspartisjonering
- [MDN Web Security] (https://developer.mozilla.org/docs/Web/Security): Komplett referanse om websikkerhet



### Arkenfox




- [Wiki- og installasjonsveiledning] (https://github.com/arkenfox/user.js/wiki): Komplett dokumentasjon av Arkenfox-prosjektet
- [Innskudd og utgivelser] (https://github.com/arkenfox/user.js): Last ned filen user.js og følg med på oppdateringer



### Guider og lokalsamfunn




- [PrivacyGuides - Desktop-nettlesere](https://www.privacyguides.org/en/desktop-browsers/): Anbefalinger og sammenligninger av nettlesere
- Reddit**: r/firefox, r/privacy for tilbakemeldinger og støtte
- PrivacyGuides-forum**: grundige tekniske diskusjoner



### Testverktøy




- [Cover Your Tracks (EFF)] (https://coveryourtracks.eff.org/): Digitale fingeravtrykk og effektivitet mot sporing
- [DNS-lekkasjetest] (https://www.dnsleaktest.com/): DNS-lekkasjetest og DoH-effektivitet
- [BrowserLeaks] (https://browserleaks.com/): Komplett testpakke (WebRTC, Canvas, fonter osv.)
- [BadSSL] (https://badssl.com/): SSL/TLS-sertifikatvalideringstester
- [CreepJS] (https://abrahamjuliot.github.io/creepjs/): Avansert analyse av mer enn 50 fingeravtrykksvektorer
- [Cloudflare DNS Test](https://1.1.1.1/help): Kontrollerer at Cloudflare DoH fungerer som den skal