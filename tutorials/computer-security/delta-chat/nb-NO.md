---
name: Delta Chat
description: Praktisk veiledning til et desentralisert meldingsverktøy
---

![image](assets/cover.webp)




## Introduksjon - Chatkontroll og personvern



De siste årene har det vært stadig mer snakk om Chat Control, et lovforslag som tar sikte på å innføre automatisk skanning av private meldinger på store kommunikasjonsplattformer. Det uttalte målet er å bekjempe ulovlig innhold, men problemet er at denne mekanismen i realiteten vil innebære masseovervåkning, undergrave ende-til-ende-kryptering og dermed personvernet til alle brukere, ikke bare lovbrytere.



Den virkelige risikoen er at chattene blir kontrollerte miljøer, der hver eneste melding, hvert eneste bilde eller vedlegg kan bli gransket før de når mottakeren. Og det er her en mulig løsning kommer inn i bildet: Gå bort fra sentraliserte plattformer og over til desentraliserte meldingssystemer, som ikke er avhengige av én enkelt leverandør og ikke så lett kan utsettes for denne typen kontroll.



En slik løsning vil bli presentert i denne opplæringen: Delta Chat. Et modent og allerede brukbart verktøy.




## Hvorfor Delta Chat og hvordan det fungerer



Delta Chat er en allerede veldig god meldingsløsning for daglig bruk: veldig nyttig for å snakke med venner, familie og andre mennesker, akkurat som en ekte ekvivalent av WhatsApp.



Det er et desentralisert meldingssystem som utelukkende er basert på e-post. Det utnytter i utgangspunktet infrastrukturen til tradisjonell e-post, men bygger et moderne direktemeldingsgrensesnitt og -opplevelse på toppen av den. Ved første øyekast kan dette virke litt improvisert, men det fungerer faktisk veldig bra og er overraskende robust. Du kan bruke dedikerte e-postservere kalt ChatMail, men det kan også fungere sømløst med vanlige e-postservere. Det betyr at du kan logge inn med en eksisterende konto hvis du vil, uten å måtte opprette noe nytt.



Et annet høydepunkt er støtte for WebXDC-er, som er små webapplikasjoner som kan brukes direkte i chatter, på samme måte som mini-appene i Telegram. Den viktige forskjellen er at disse appene ikke har Internett-tilgang, slik at de ikke kan spore brukeren eller sende data eksternt.



Fra et sikkerhetsperspektiv bruker Delta Chat verifisert ende-til-ende-kryptering, basert på PGP, men med moderne utvidelser som gjør at beskyttelsesnivået kan sammenlignes med Signal. Det eneste som mangler for øyeblikket, er Perfect Forward Secrecy, men det er et aspekt som er under utvikling.



Delta Chat er utelukkende basert på e-post, og unngår det helt:




- obligatoriske telefonnumre
- Sentraliserte ID-er
- registreringer knyttet til en enkelt tjeneste



Og det er det som gjør dette verktøyet svært motstandsdyktig mot inngripende reguleringer som Chat Control.




## Installasjon



Fra den offisielle nettsiden til [Delta Chat] (https://delta.chat/download) kan du gå til nedlastingsdelen. På Linux er det lett tilgjengelig gjennom Flathub, men det finnes også pakker for Arch, NixOS, Snap og frittstående versjoner.



![image](assets/it/01.webp)



Den er også tilgjengelig for:




- [F-Droid](https://f-droid.org/app/com.b44t.messenger)
- [Play Store] (https://play.google.com/store/apps/details?id=chat.delta)
- [iOS] (https://apps.apple.com/it/app/delta-chat/id1459523234)
- [Windows] (https://apps.microsoft.com/detail/9pjtxx7hn3pk)
- [macOS](https://apps.apple.com/it/app/delta-chat-desktop/id1462750497)
- [Ubuntu Touch] (https://open-store.io/app/deltatouch.lotharketterer)
- og andre butikker...



Hvis du er på utkikk etter en veiledning for å installere F-Droid, kan denne veiledningen hjelpe deg:



https://planb.academy/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

En veldig viktig ting: skrivebordsversjoner krever ikke en telefon. I motsetning til WhatsApp eller SimpleX Chat trenger du ikke å registrere deg fra mobilen først. Du kan opprette profilen din direkte på PC-en eller overføre den fra en annen enhet.




## Opprettelse av profil



Når appen er åpen, spør Delta Chat om du vil opprette en ny profil eller bruke en eksisterende.



![image](assets/it/02.webp)



Ved å opprette en ny profil kan du gå inn:




- et navn
- et bilde (valgfritt)



En ChatMail-server er foreslått som standard, men det er mulig:




- velge en annen ChatMail-server
- bruke en klassisk e-postkonto
- konfigurere IMAP og SMTP manuelt
- registrere deg med en annen brukers invitasjonskode



Etter noen sekunder er profilen klar, og du kan begynne å bruke appen.



![image](assets/it/03.webp)




## Interface og chat



Grensesnittet er veldig enkelt og oversiktlig:




- Enhetsmeldinger, som er lokal kommunikasjon
- Lagrede meldinger, tilsvarende dem i Telegram og synkroniserbare mellom enheter



![image](assets/it/04.webp)



Bare legg til en kontakt:




- Viser QR-koden din
- Skann den andre personens
- Inviter via lenke (del invitasjonslenke).



![image](assets/it/05.webp)



Når forbindelsen er opprettet, konfigureres ende-til-ende-kryptering automatisk. Brukergrensesnittet for chat er svært likt det som brukes i WhatsApp:




- tekst- og talemeldinger
- bilder, videoer og filer
- svar på meldinger
- reaksjoner
- popup-meldinger
- tilpassbare varsler.



![image](assets/it/06.webp)



## WebXDC: apper i chatter:



Delta Chat gjør det mulig å bruke WebXDC, dvs. små applikasjoner som er innebygd i samtaler. Her er en kort liste over de mest nyttige som er identifisert:




- spørreundersøkelser
- tegnebrett
- midlertidige private chatter
- spill med delte chat-poengsummer



Det er også mulig å starte mer komplekse spill, noe som viser hvor fleksibelt dette verktøyet er.



![image](assets/it/07.webp)



## Grupper, kanaler og avanserte funksjoner



Du kan opprette grupper, bruke klistremerker (spesielt på stasjonære datamaskiner) og, ved å aktivere de eksperimentelle alternativene, til og med kanaler, på samme måte som i Telegram.



I de avanserte innstillingene kan du slå på:




- taleanrop (fortsatt på forsøksstadiet)
- avansert administrasjon av e-postprofiler
- fullstendige sikkerhetskopier.



![image](assets/it/08.webp)



## Flere enheter og sikkerhetskopiering



Delta Chat har full støtte for flere enheter:




- du kan legge til en ekstra enhet via QR-kode
- kan du utføre en fullstendig overføring via sikkerhetskopiering.



På få sekunder finner du igjen chatter, grupper og hele historikken din, uten å være avhengig av en sentral server.



![image](assets/it/09.webp)




## Konklusjon



I en tid der det snakkes stadig mer om å kontrollere privat kommunikasjon, representerer Delta Chat et konkret svar: desentraliserte, krypterte meldinger som virkelig kan brukes hver dag.



Det er den løsningen som, av alle de jeg har prøvd, har overbevist meg mest for enkelhet, personvern og frihet. Hvis du vil, kan du også kontakte meg på Delta Chat via følgende [invitasjonslenke] (https://i.delta.chat/#38824F04DD40600D5D4F079C1F5E0EBA875A6D7E&i=GStGfNW5LMIXhwQMiuQWj3QU&s=cVi5izRJ9NsbIcPlU8yC_SeB&a=9l4la5imj%40nine.testrun.org&n=SatoSats)



Hvis du likte denne guiden, kan du støtte meg ved å donere og legge igjen en tommel opp. Og husk: Bare ved å bruke og utforske Delta Chat fra både mobil og datamaskin vil du virkelig oppdage den fulle funksjonaliteten.



Til neste gang.