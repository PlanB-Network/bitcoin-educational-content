---
name: LineageOS
description: Gratis, usammenhengende Android-operativsystem for smarttelefoner
---

![cover](assets/cover.webp)



Konvensjonelle Android-systemer som er forhåndsinstallert på smarttelefonene våre, byr på en rekke velkjente problemer: intensiv integrering av Google-tjenester som fører til konstant datasporing, uønskede sponsede applikasjoner (bloatware) pålagt av produsentene, og oppgivelse av oppdateringssporing etter noen år, noe som dømmer fortsatt fungerende enheter til programmert foreldelse.



LineageOS presenterer seg selv som et elegant svar på disse problemene. LineageOS er et produkt av åpen kildekode-fellesskapet og en direkte etterfølger til CyanogenMod (som ble avviklet i slutten av 2016), og er et gratis Android-basert mobiloperativsystem som gir brukerne tilbake kontrollen over smarttelefonene sine. Prosjektet ble offisielt lansert i desember 2016, og har nå over 4,4 millioner aktive installasjoner over hele verden og støtter hundrevis av telefonmodeller fra over 20 forskjellige merker.



![lineageos-homepage](assets/fr/01.webp)



*Offisielt LineageOS-nettsted som presenterer prosjektet og dets mål*



## Hva er LineageOS?



### Filosofi og målsettinger



LineageOS er et mobiloperativsystem med åpen kildekode basert på Android Open Source Project (AOSP), utviklet av et stort fellesskap av frivillige bidragsytere over hele verden. Det uoffisielle mottoet kan være "Din enhet, dine regler": Prosjektet har som mål å forlenge levetiden til smarttelefoner og samtidig tilby en strømlinjeformet, personvernvennlig Android-opplevelse.



Prosjektet oppsto fra asken til CyanogenMod, en av de mest populære alternative Android ROM-ene i historien. Da CyanogenMod Inc. stengte dørene i desember 2016, mobiliserte samfunnet seg for å skape LineageOS, og beholdt ånden av innovasjon og åpen kildekode-filosofi som preget forgjengeren.



I motsetning til OEM Android-distribusjoner forhåndsinstallerer ikke LineageOS noen Google-applikasjoner som standard, og eliminerer bloatware fullstendig. Brukerne starter med et minimalistisk system som kun inneholder de viktigste applikasjonene (telefon, meldinger, kamera, nettleser), og står fritt til å velge hva de vil legge til senere.



### Påvirkning og fellesskap



Offisiell statistikk avslører omfanget av prosjektet: med over 4,4 millioner aktive installasjoner i 224 land, representerer LineageOS et av de mest utbredte Android-alternativene i verden. Brasil leder an med over 2 millioner brukere, etterfulgt av Kina og USA, noe som viser den universelle appellen til en gratis, tilpassbar Android.




## Hovedfunksjoner



### Interface og brukeropplevelse



**Ren Android**: LineageOS tilbyr en autentisk Android-opplevelse nær AOSP, uten produsentoverlegg eller overflødige applikasjoner. Interface forblir kjent for Android-brukere, samtidig som den gir optimal flyt takket være fraværet av bloatware.



**Google-fri som standard**: Ingen Google-tjenester er forhåndsinstallert, av juridiske og etiske årsaker. Denne "Google-frie" tilnærmingen garanterer full kontroll over personopplysningene dine og forbedrer ytelsen ved å unngå tjenester som kjører i bakgrunnen.



### Tilpasning og sikkerhet



**Avansert tilpasning**: LineageOS låser opp mange alternativer som ikke er tilgjengelige på standard Android: omkonfigurering av navigasjonsknapper, tilpassbare systemtemaer, bruksprofiler tilpasset ulike kontekster (jobb, privat, spill).



**Outil Trust**: Integrert funksjonalitet som overvåker enhetens sikkerhetsstatus og varsler deg om potensielle trusler, slik at du får oversikt over systemets sikkerhet i sanntid.



**Utvidede oppdateringer**: LineageOS-fellesskapet har forpliktet seg til å levere månedlige sikkerhetsoppdateringer, slik at enheter som ikke lenger produseres av produsentene, kan fortsette å motta de nyeste Android-sikkerhetsoppdateringene.



## Kompatible enheter



LineageOS støtter hundrevis av enheter fra over 20 produsenter: Samsung, Xiaomi, OnePlus, Motorola, Sony, Google Pixel, Fairphone og mange andre. Denne brede kompatibiliteten er en av prosjektets største fordeler i forhold til alternativer som GrapheneOS, som er begrenset til Pixel-enheter.



![devices-compatibility](assets/fr/02.webp)



*LineageOS-kompatible enheter med filtre etter produsent*



![google-devices](assets/fr/03.webp)



*Google-enheter støttes, inkludert Pixel 4 (kodenavn "flame")*



### Populære enheter



Ifølge offisiell statistikk inkluderer de mest brukte modellene en rekke enheter som dekker ulike pris- og aldersklasser, noe som viser LineageOS' evne til å blåse nytt liv i eldre smarttelefoner samt optimalisere nyere.



### Viktige punkter før installasjon



**Ulåst oppstartslaster**: Sjekk at produsenten/operatøren din tillater opplåsing. Noen merker, som Huawei, har fjernet denne muligheten på nyere modeller, mens andre pålegger spesifikke prosedyrer.



**Nøyaktig modell**: Det er viktig å laste ned ROM-en som passer nøyaktig til enheten din. To modeller med lignende handelsnavn kan være teknisk forskjellige (for eksempel Galaxy S10 vs S10 5G) og krever forskjellige bilder.



**Skalerbar støtte**: Nyere enheter støttes kanskje ikke umiddelbart, ettersom portering krever at en frivillig utvikler tar seg av dem. Omvendt kan støtten opphøre hvis den som vedlikeholder en enhet, trekker seg fra prosjektet.



## Installasjon



### Viktige forutsetninger



⚠️ **Les disse instruksjonene fullstendig før du begynner** for å unngå problemer!



**Gå tilbake til standard fastvare (om nødvendig) :**




- Android Flash-verktøy**: Bruk det offisielle Google-verktøyet [flash.android.com](https://flash.android.com) for å enkelt gjenopprette Pixel-enheten din til standard Android fra nettleseren din (Chrome/Edge kreves)
- Alternativ**: Fabrikkbilder manuelt fra [developers.google.com/android/images](https://developers.google.com/android/images)



**Obligatoriske forkunnskapstester:**




- Start enheten minst én gang** med det opprinnelige standardsystemet
- Test alle funksjoner**: SMS, samtaler, Wi-Fi, mobildata
- Viktig**: Sjekk at du kan sende/motta SMS og ringe/motta samtaler (inkludert via WiFi og 4G/5G). Hvis det ikke fungerer på standardsystemet, vil det heller ikke fungere på LineageOS!
- Nyere enheter**: Noen krever at VoLTE/VoWiFi brukes minst én gang på standardsystemet for å klargjøre IMS



**Systemforberedelser:**




- Fjern alle Google**-kontoer fra enheten for å unngå beskyttelse mot tilbakestilling til fabrikkinnstilling, som kan blokkere aktivering
- Full sikkerhetskopiering** : Prosessen vil slette telefonen din fullstendig. Sikkerhetskopier bilder, kontakter, applikasjoner og viktige filer



**ADB- og Fastboot-verktøy:** Følg den [offisielle LineageOS-veiledningen](https://wiki.lineageos.org/adb_fastboot_guide#installing-adb-and-fastboot) for å installere Android SDK Platform Tools. Bekreft installasjonen med `adb version` og `fastboot --version`.



**Telefonkonfigurasjon:**




- Aktiver **Utvikleralternativer**: Innstillinger > Om > trykk på "Build number" 7 ganger



![android-version](assets/fr/06.webp)



*Gå til Innstillinger > Om telefonen for å aktivere utviklermodus*





- Aktiver **USB-feilsøking** i Utvikleralternativer
- Aktiver **OEM Unlock** (viktig for å låse opp bootloaderen)



![developer-options](assets/fr/07.webp)



*Aktiver utvikleralternativer, USB-feilsøking og OEM-opplåsing*



### Detaljert installasjon



⚠️ **Disse instruksjonene er spesifikke for LineageOS 22.2. Følg hvert trinn nøyaktig. Ikke gå videre hvis noe mislykkes!



#### Trinn 1: Kontroll av fastvare



**Firmware kreves**: Enheten din må ha Android 13 installert før du kan fortsette (for Pixel 4). Fastvare refererer til de enhetsspesifikke bildene som er inkludert i standardsystemet.



![pixel4-info](assets/fr/04.webp)



*Offisiell Pixel 4-side med nedlastingslenker og installasjonsveiledninger*



![downloads-page](assets/fr/05.webp)



*Nedlastingsside og filer for LineageOS build*



**Spesifikke nedlastinger for Pixel 4:**




- Bygg LineageOS**: [download.lineageos.org/devices/flame/builds](https://download.lineageos.org/devices/flame/builds)
- Nødvendige filer**: Last ned de tre nødvendige filene fra denne siden (de vil bli brukt i de følgende trinnene):
  - `lineage-22.2-YYYYYYMMDD-nightly-flame-signed.zip` (hoved-ROM)
  - dtbo.img` (partition device tree blob)
  - `boot.img` (gjenoppretting LineageOS)



⚠️ **Viktig**: Sjekk Android-versjonen, ikke produsentens OS-versjon. Å bruke en tilpasset ROM (selv LineageOS) garanterer ikke at dette kravet er oppfylt.



💡 ** Tips **: Hvis du er i tvil om fastvaren din, gå tilbake til aksjesystemet før du fortsetter!



#### Trinn 2: Låse opp bootloaderen



⚠️ **Dette trinnet sletter alle dataene dine!





- Test ADB-tilkoblingen**: Koble til enheten via USB og test med kommandoen `adb devices` fra terminalen på datamaskinen



![adb-devices](assets/fr/08.webp)



*Sjekk ADB-tilkoblingen med kommandoen `adb devices`*





- Godkjenn tilkobling** på telefonen din



![usb-debugging-auth](assets/fr/09.webp)



*USB-feilsøking aktivert med datamaskinens RSA-fingeravtrykk*





- Start opp i bootloader-modus** :


```
adb -d reboot bootloader
```


Eller hold **Volume ned + Power** enheten av





- Kontroller fastboot**-tilkoblingen:


```
fastboot devices
```



![fastboot-mode](assets/fr/10.webp)



*Fastboot-kommandoer i terminal for å sjekke tilkoblingen*



![bootloader-screen](assets/fr/11.webp)



*Pixel 4s fastboot-skjerm med systeminformasjon*





- Lås opp bootloaderen** :


```
fastboot flashing unlock
```


På enheten bruker du volumtastene til å navigere og trykker på **Power**-knappen for å velge "Unlock the bootloader" og bekrefte operasjonen



![unlock-bootloader](assets/fr/12.webp)



*Bekreftelse av opplåsing av bootloader på enheten*



⚠️ **Telefonen starter automatisk på nytt** etter bekreftelse av opplåsing





- Etter automatisk omstart** aktiverer du USB-feilsøking på nytt i utvikleralternativene




#### Trinn 3: Flash flere partisjoner



⚠️ **Kreves for at gjenopprettingen skal fungere ordentlig**





- Start bootloaderen på nytt**: Volum ned + Power
- Flash** (erstatt `/path/to/` med mappen der du lastet ned filen) :


```
fastboot flash dtbo /chemin/vers/dtbo.img
```



![flash-partitions](assets/fr/13.webp)



*Flash av dtbo- og boot.img-partisjoner via fastboot*



#### Trinn 4: Installere LineageOS-gjenoppretting





- Flash recovery** (erstatt `/path/to/` med mappen der du lastet ned filen) :


```
fastboot flash boot /chemin/vers/boot.img
```




- Start på nytt i gjenoppretting** for å sjekke



#### Trinn 5: Installere LineageOS





- Start på nytt i gjenopprettingsmodus**: Volum ned + Power → Gjenopprettingsmodus



![recovery-mode](assets/fr/14.webp)



*Interface fra LineageOS-gjenoppretting med hovedmeny*





- Fabrikkinnstilling** : Skriv inn "Fabrikkinnstilling" → "Formater data / fabrikkinnstilling"



![factory-reset](assets/fr/15.webp)



*Tilbakestilling til fabrikkinnstilling i LineageOS*-gjenoppretting





- Gå tilbake til hovedmenyen**
- Sideload LineageOS** :
   - På enheten: "Bruk oppdatering" → "Bruk fra ADB"
   - På PC: `adb -d sideload /path/to/lineageos.zip`



![apply-update](assets/fr/16.webp)



*Velg "Apply Update" og deretter "Apply from ADB" i recovery*



![sideload-process](assets/fr/17.webp)



*LineageOS-installasjon pågår via sideload*



![sideload-terminal](assets/fr/18.webp)



*Sideload-kommando i terminal med installasjonsfremdrift*



💡 **Normal**: Prosessen kan stoppe ved 47% eller vise "Success"-feil - dette er normalt!



#### Trinn 6: Første oppstart





- Start på nytt**: "Start systemet på nytt nå"
- Første oppstart**: Kan ta opptil 15 minutter



🎉 **Installasjonen er fullført!** **



### Oppmerksomhetspunkter



⚠️ **Advarsel**: LineageOS leveres "som det er" uten garanti. Selv om vi gjør vårt ytterste for å sikre at alt fungerer, installerer du dette på egen risiko!



**Kritiske kontroller:**




- Fastvarekompatibilitet**: Sørg for å sjekke hvilken fastvareversjon som kreves på nedlastingssiden for din modell
- Aldri lås** bootloaderen på nytt etter installasjon av LineageOS
- Følg de spesifikke instruksjonene** for enheten din



## Konfigurasjon og bruksområder



### Første oppstart


Strømlinjeformet Interface, nær lager Android, uten Google. Enkel konfigurasjon: språk, Wi-Fi, ingen konto kreves.



### Alternative bruksområder



**Sikre applikasjonskilder:**



**F-Droid** : Referansebutikken for applikasjoner med åpen kildekode, forhåndsinstallert med LineageOS for microG eller kan lastes ned direkte. F-Droid tilbyr kun programvare med åpen kildekode som er verifisert og kompilert på en transparent måte, noe som garanterer fravær av trackere eller skadelige komponenter.



**Aurora Store**: Anonym klient for tilgang til Google Play Store uten en Google-konto. Aurora låner delte anonyme kontoer, slik at du kan laste ned vanlige apper og samtidig bevare personvernet ditt.



**Viktige alternative applikasjoner:**





- Navigasjon**: Organic Maps (offline-kart basert på OpenStreetMap)
- Kommunikasjon**: Signal (ende-til-ende-krypterte meldinger), K-9 Mail (gratis e-postklient)
- Medier**: NewPipe (reklamefri, sporingsfri YouTube), VLC (universell mediespiller)
- Produktivitet**: Nextcloud (selvbetjent sky), Simple Calendar (CalDAV-synkronisering)
- Sikkerhet**: Bitwarden (passordbehandling), Aegis Authenticator (2FA-koder)



Disse applikasjonene, hvorav de fleste er tilgjengelige via F-Droid, utgjør et sammenhengende økosystem som fullt ut kan erstatte Googles tjenester, samtidig som de gir en moderne og funksjonell brukeropplevelse.



## Bruk og vedlikehold



### Daglig erfaring



LineageOS forvandler Android-opplevelsen, og prioriterer flyt og respons. Den strømlinjeformede Interface er spesielt effektiv på eldre enheter, som får et nytt liv, med ytelse som generelt er bedre enn produsentens ROM-er takket være fraværet av tunge overlegg og overflødige prosesser.



Grunnleggende funksjoner (samtaler, SMS, bilder, surfing) fungerer sømløst, mens tilpasningsverktøy gjør det mulig å finjustere systemet til individuelle preferanser uten at det går på bekostning av stabiliteten.



### OTA-oppdateringssystem



LineageOS har et spesielt brukervennlig Over-The-Air-oppdateringssystem. Nye versjoner foreslås automatisk via varsler, og installasjonen tar bare noen få klikk, uten behov for kompliserte tekniske inngrep. Prosessen bevarer dine installerte data og applikasjoner fullt ut.



Disse regelmessige oppdateringene er en stor fordel, spesielt for enheter som ikke lenger produseres av produsentene, som kan fortsette å dra nytte av de nyeste sikkerhetsoppdateringene for Android.



### Anbefalt beste praksis



**Sikkerhet etter installasjon:**




- Angi en sterk PIN-kode eller et passord for opplåsing
- Kontroller at lagringskryptering er aktivert (vanligvis som standard)
- Installer en passordbehandler som Bitwarden via F-Droid



**Forebyggende vedlikehold:**




- Regelmessige OTA-oppdateringer for sikkerhet
- Begrens installasjon av applikasjoner til pålitelige kilder (F-Droid, Aurora Store)
- Gjennomgå jevnlig tillatelsene som er gitt til applikasjoner
- Sporadiske omstarter optimaliserer ytelsen og frigjør minne



## Fordeler og begrensninger



✅ **Fordeler:**




- Standard personvern (ingen Google-sporing)
- Bred kompatibilitet (mer enn 300 modeller)
- Overlegen ytelse (ingen bloatware)
- Utvidede oppdateringer på eldre enheter



❌ **Begrensninger:**




- Teknisk installasjon
- Ingen Android Auto/Google Pay
- Bankapper kan være problematiske



## GrapheneOS vs LineageOS: Hva er forskjellen?



### Forskjellige tilnærminger



**GrapheneOS** fokuserer utelukkende på maksimal sikkerhet, og kjører kun på Google Pixels for å utnytte deres dedikerte sikkerhetsbrikker. Systemet inneholder en rekke avanserte tiltak mot sårbarheter og styrker applikasjonssandkassen betraktelig.



**LineageOS** balanserer sikkerhet, personvern og brukervennlighet på så mange enheter som mulig. Tilnærmingen er mer pragmatisk, og sikter mot utvidet kompatibilitet fremfor absolutt sikkerhet.



### Administrere Google-tjenester



**GrapheneOS**: Tilbyr et valgfritt Google Play-system med sandkasse. Google Play kan installeres, men kjører i en streng sandkasse, uten spesielle systemrettigheter. Denne unike tilnærmingen gjør det mulig å bruke Googles økosystem og samtidig opprettholde streng sikkerhetskontroll.



**LineageOS**: Lar brukeren velge å installere Google-tjenester (GApps), microG (gratis alternativ), eller forbli helt Google-fri. Maksimal fleksibilitet for å dekke dine behov.



### Teknisk sammenligning



| **Aspect** | **GrapheneOS** | **LineageOS** |
|------------|----------------|---------------|
| **Compatibilité** | Pixels uniquement | Centaines d'appareils |
| **Sécurité** | Mitigations avancées | Sécurité AOSP standard |
| **Google Play** | Sandboxé optionnel | Installation classique possible |
| **Installation** | Interface web + USB | Procédure manuelle technique |
| **Philosophie** | Sécurité avant tout | Équilibre et liberté de choix |

### Anbefalinger for bruk



**Velg GrapheneOS** hvis du eier en Pixel, hvis maksimal sikkerhet er din høyeste prioritet, og hvis du aksepterer begrensninger for forbedret beskyttelse.



**Velg LineageOS** hvis du har en enhet som ikke er en Pixel-enhet, er på utkikk etter en god balanse mellom personvern og praktisk bruk, eller vil ha friheten til å velge ditt eget kompromissnivå med Googles økosystem.



## Konklusjon



LineageOS tilbyr et modent alternativ for å gjenvinne kontrollen over Android-smarttelefonen din. Ubundet opplevelse, optimal ytelse, omfattende kompatibilitet: det ideelle valget for å kombinere personvern og praktisk bruk i hverdagen.



## Ressurser



### Offisiell dokumentasjon




- [LineageOS offisielle nettside](https://lineageos.org)
- [LineageOS Wiki](https://wiki.lineageos.org) - Installasjonsveiledninger etter modell
- [LineageOS for microG](https://lineage.microg.org) - Versjon med integrert microG



### Fellesskapet




- [Subreddit r/LineageOS](https://reddit.com/r/LineageOS)
- [Mastodon-konto @LineageOS](https://fosstodon.org/@LineageOS)



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1