---
name: Bitchat
description: Desentralisert, internettfri meldingsformidling for fri kommunikasjon
---

![cover](assets/cover.webp)


![video](https://youtu.be/WfzcKAzgB9s)


*Denne videoveiledningen fra BTC Sessions går gjennom prosessen med å sette opp og bruke Bitchat!


Bitchat ble til etter en rask prototypingsprosess der [@jack] (https://primal.net/jack) utviklet det opprinnelige konseptet i løpet av en helges kodingsøkt. [@calle](https://primal.net/calle) ble med i prosjektet kort tid etter for å være med på å utvikle Android-implementeringen. Jack leder for tiden utviklingen av iOS-versjonen, mens calle har ansvaret for Android-versjonen med støtte fra mange andre bidragsytere.


## Introduksjon: Chat fritt, uten nett


Tenk deg å sende meldinger når internett går ned, under en naturkatastrofe eller på steder der kommunikasjonen er begrenset. Bitchat gjør dette mulig. Det er en desentralisert, peer-to-peer-meldingsapp som hopper over sentrale servere og lar enheter snakke direkte med hverandre, helt offline ved hjelp av Bluetooth og mesh-nettverk. Bitchat er utviklet med tanke på personvern og robusthet, og er ideell for bruk i områder der tradisjonell tilkobling er upålitelig eller utilgjengelig - for eksempel i katastrofescenarioer, på avsidesliggende steder eller for dem som ønsker å unngå overvåking. Bitchat bruker kryptografi for å sikre at alle meldinger er kryptert fra ende til ende, verifisert og manipulasjonssikkert.


I denne veiledningen viser vi hvordan Bitchat fungerer, og hvordan du kan bruke det til virkelig privat, offline-klar kommunikasjon.


## 🚀 Viktige funksjoner


Bitchat gjør det mulig å sende meldinger offline ved hjelp av disse [funksjonene] (https://github.com/permissionlesstech/bitchat-android?tab=readme-ov-file#features):



- Kompatibel på tvers av plattformer**: Full protokollkompatibilitet mellom iOS og Android.
- Desentralisert mesh-nettverk**: Automatisk oppdagelse av motparter og videreformidling av meldinger via Bluetooth Low Energy (BLE)
- Ende-til-ende-kryptering**: X25519-nøkkelutveksling + AES-256-GCM for private meldinger
- Kanalbaserte chatter**: Emnebaserte gruppemeldinger med valgfri passordbeskyttelse
- Lagre og videresend**: Meldinger mellomlagres for frakoblede motparter og leveres når de kobler seg til igjen
- Personvern først**: Ingen kontoer, ingen telefonnumre, ingen vedvarende identifikatorer
- Kommandoer i IRC-stil: Velkjent grensesnitt i stil med `/join, /msg, /who`.
- Oppbevaring av meldinger**: Valgfri lagring av meldinger for hele kanalen, kontrollert av kanaleierne
- Nødsletting**: Trykk tre ganger på logoen for å slette alle data umiddelbart
- Moderne Android-grensesnitt**: Jetpack Compose med Material Design 3
- Mørke/lyse temaer**: Terminal-inspirert estetikk som matcher iOS-versjonen
- Batterioptimalisering**: Adaptiv skanning og strømstyring


## 1️⃣ Hvordan Bitchat fungerer - helt enkelt


Med Bitchat kan du sende meldinger til telefoner i nærheten direkte via Bluetooth (`BLE` som følger), uten behov for internett eller mobilsignal. Når du starter en chat, utfører telefonene et sikkert håndtrykk for å opprette en unik, midlertidig krypteringsnøkkel for samtalen. Hver melding beskyttes med ende-til-ende-kryptering, og en ny nøkkel brukes for hver enkelt melding for å sikre at tidligere meldinger forblir trygge selv om telefonen din senere blir kompromittert. Til slutt deler appen meldingene opp i små biter og blander dem med tilfeldige dummy-data for å skjule meldingsaktiviteten din. For direkte chatter mellom enheter fungerer det bare innenfor en rekkevidde på opptil 100 meter. Det er som å sende krypterte lapper i et overfylt rom - enhetene hvisker direkte til hverandre og makulerer nøklene etter hver melding.


Bitchat lar deg også bli med i stedsbaserte chatterom ved hjelp av Nostr-protokollen og `#geohashes`. En geohash er en kort kode, som `#u33d`, som representerer et bestemt geografisk område, fra et enkelt nabolag, opp til en hel by eller region. Du kan `teleportere` deg inn i et hvilket som helst geohash-chatterom rundt om i verden ved å taste inn koden. Meldingene dine sendes gjennom et desentralisert nettverk av reléer, noe som beskytter den nøyaktige posisjonen din. Hver gang du blir med i et geohash-rom, får du dessuten en ny, midlertidig identitet, noe som gir et ekstra lag med personvern til de stedsbaserte samtalene dine.


For mer nøyaktige tekniske detaljer, se [offisiell hvitbok] (https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md).


## 2️⃣ Installasjon og oppsett


### Hvor får man tak i Bitchat


Du kan installere Bitchat gjennom:



- [Apple App Store] (https://apps.apple.com/us/app/bitchat-mesh/id6748219622) (for iOS-enheter)
- [Google Play Store] (https://play.google.com/store/apps/details?id=com.bitchat.droid) (for Android-enheter)


Android-brukere har også alternative muligheter:



- Last ned APK direkte fra [GitHub Releases] (https://github.com/permissionlesstech/bitchat-android/releases) eller
- Installer via den Nostr-kompatible [Zapstore] (https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqgkxmmd9e3xjarrdpshgtnywfhkjeqxtfkcr)


![image](assets/en/01.webp)


**Merknad**: _Denne veiledningen fokuserer primært på Android-implementeringen. IOS-versjonen kan avvike


### Oppsettprosess


Etter installasjonen åpner du Bitchat for å se dette første skjermbildet for tillatelser. Her er hva du må gjøre:


1. **Gi disse nødvendige tillatelsene:**


   - Bluetooth-tilgang** (for å oppdage Bitchat-brukere i nærheten)
   - Nøyaktig posisjon** (Android krever dette for Bluetooth-funksjonalitet)
   - Varsler** (for å motta private meldinger)

2. **Deaktiver batterioptimalisering**:


   - Dette gjør at Bitchat kan kjøre i bakgrunnen
   - Opprettholder mesh-nettverkstilkoblinger kontinuerlig


Trykk på `Grant Permissions` , følg `prompts` og `Disable Battery Optimization` for å gå til neste skjermbilde.


![image](assets/en/02.webp)


Velkommen til Bitchats hovedskjerm. La oss orientere oss:


### Innstillinger


En ting av gangen. Innstillingsmenyen kan åpnes ved å trykke på `Bitchat-logoen`.  Følgende alternativer er tilgjengelige:



- Still inn `utseende` (system/lys/mørk).
- aktiver `Proof of work` til geohash for å forhindre spam (valgfritt)
- Slå på `Tor` for å forbedre personvernet.


![image](assets/en/16.webp)


### Angi identiteten din


Trykk på feltet `bitchat/anonXXXXXX` øverst for å velge brukernavn. Det er slik andre vil se deg i både Bluetooth- og Internett-modus. Du kan for eksempel endre "anon2022" til et brukernavn du selv velger.


![image](assets/en/03.webp)


### Velg nettverkskanaler


Bruk menyen `#location channels` (til høyre for brukernavnet) for å bytte mellom tilkoblingstyper:



- BLE Mesh***: Standard Bluetooth-modus (uten internett, fra 10 til 50 meters rekkevidde)
- #geohashes**: Internett-aktiverte geografiske lokalsamfunn som bruker [Nostr-protokollen] (https://nostr.com/)


Når du velger `#geohashes`-modus, integreres Bitchat med Nostr-protokollen for å muliggjøre geografiske fellesskap. Meldingene dine publiseres til `desentraliserte Nostr-reléer` i stedet for Bitchats peer-to-peer-nettverk, noe som muliggjør bredere, men stedsfiltrerte samtaler. Bitchat-identitetsnøklene dine signerer kryptografisk alle Nostr-hendelser for å opprettholde autentisering, mens geohash-tagger (som `#u4pruyd` for et nabolag) filtrerer meldinger til det presisjonsnivået du har valgt. Dette betyr at du kan delta i lokale diskusjoner uten å avsløre nøyaktige koordinater, selv om det kreves internettilgang.


![image](assets/en/04.webp)


### Overvåk jevnaldrende

lisens: CC-BY-SA-V4

Peer-telleren viser brukere:



- I nærheten (BLE Mesh) eller
- I geohash-sonen din (#geohashes)


![image](assets/en/05.webp)


## 3️⃣ Global chat og private meldinger


Bitchat tilbyr to forskjellige kommunikasjonsmoduser som passer til ulike behov:



- Offentlige kanaler:** For åpne samtaler med andre. Du kan koble deg til enten gjennom det lokale BLE-nettverket for brukere i nærheten eller via en global #geohash for internettaktiverte, stedsbaserte fellesskap.
- Private meldinger:** For sikre samtaler på tomannshånd. Disse oppretter en direkte, kryptert forbindelse for å holde utvekslingene konfidensielle.


Å forstå begge modusene vil hjelpe deg å navigere i samtalene dine.


### Offentlige kanaler: The Community Hub


Menyen `#lokasjonskanaler` (øverst til høyre) styrer din synlighet for offentligheten. Ved å velge `mesh` kobles du til alle brukere i nærheten via BLE mesh, vanligvis enheter innenfor 10-50 meter. Dette skaper et åpent forum der meldinger sendes ut til alle innenfor rekkevidde, noe som er ideelt for kunngjøringer om arrangementer eller lokale varsler.


For større geografisk rekkevidde kan du velge en hvilken som helst `#geohash`-tagg for å bli med i internettdrevne fellesskap filtrert etter sted. Disse kanalene bruker Nostr-protokollreléer, noe som gjør det mulig å kommunisere på tvers av byer eller regioner, samtidig som den stedsbaserte relevansen opprettholdes. Meldingene dine vises direkte til andre i samme kanal, og nye deltakere ser automatisk den siste meldingshistorikken når de blir med.


![image](assets/en/06.webp)


### Private samtaler: Sikker og kryptert


For å starte en privat samtale kan du trykke direkte på et `brukernavn` som vises i `Peers Overview`. Du kan også trykke på `stjerneikonet` for å markere denne brukeren som en favoritt, noe som vil holde vedkommende synlig i kontaktlisten din selv når vedkommende er frakoblet.


![image](assets/en/07.webp)


Bitchat starter automatisk et "sikkerhetshandshake" når du starter en privat chat. Enhetene utveksler kortvarige nøkler for å opprette en kryptert tunnel spesielt for samtalen din. Denne prosessen sikrer at alle meldinger og delte filer forblir konfidensielle takket være kontinuerlig ende-til-ende-kryptering. Private meldinger støtter tekst- og fildeling.


![image](assets/en/08.webp)


## 4️⃣ Tilleggsfunksjoner


Du får tilgang til handlingspanelet umiddelbart ved å skrive `/` hvor som helst i Bitchat. Dette viser en kommandomeny for raske handlinger.



- Administrer tilkoblinger**: blokker brukere eller Fjern blokkering av jevnaldrende
- Kanalkontroller**: `Vis kanaler` eller `Legg til/opprett kanal`
- Sosiale interaksjoner**: `Sende varm klem` eller `slå med ørret` 🎣
- Vedlikehold av chat**: "Tøm chat-meldinger
- Personvernverktøy**: "Se hvem som er på nett" eller "Send privat melding


Kommandoer utføres umiddelbart - som `/blokker Satoshi` for å stilne kritikere eller `/kram Hal` for å spre positivitet 🫂.


![image](assets/en/09.webp)


## 5️⃣ Opprette en kanal


Kanaler i Bitchat muliggjør organisert kommunikasjon rundt temaer, steder eller fellesskap. Følg denne arbeidsflyten for å opprette din egen:


### Trinn 1: Opprett en kanal


Du oppretter en kanal ved å skrive `/j` eller `/join` etterfulgt av `kanalnavnet` i en hvilken som helst chat (f.eks. `/j <kanalnavn>`). Etter opprettelsen vises et nytt `ikon ⧉` som indikerer den nye kanalen. Andre brukere kan bli med ved å skrive den samme kommandoen (f.eks. `/j bitchat_tutorial`).


![image](assets/en/10.webp)


### Trinn 2: Konfigurer innstillinger


I tillegg til standardkommandoene er følgende innstillinger tilgjengelige i en kanal:



- `/save` for å lagre meldinger lokalt
- `/transfer` for å overføre kanaleierskap og
- `/pass` for å endre kanalpassordet.


For private fellesskap aktiverer denne kommandoen passordbeskyttelse, slik at godkjente medlemmer må oppgi et egendefinert passord før de kan bli medlem.


## 6️⃣ Panikkmodus


La oss nå snakke om "panikkmodus": Ved å trykke tre ganger på "Bitchat-logoen" starter en fullstendig sletting av alle lokale meldinger og data i appen. Dette er din ultimate personvernbeskyttelse, perfekt for situasjoner som krever umiddelbar diskresjon.


**Viktig påminnelse:** _Panikkmodus er permanent. Når den er aktivert, kan ikke data gjenopprettes. Bruk med forsiktighet


![image](assets/en/11.webp)


## 7️⃣ Geohashes


Geohash-kanaler muliggjør målrettede samtaler basert på geografiske steder i stedet for tradisjonelle nettverkstilkoblinger. Denne funksjonen gjør bitchat til et stedsbevisst kommunikasjonsverktøy som er ideelt for lokal koordinering, samfunnsbygging og stedsspesifikke diskusjoner.


### Slik fungerer `#geohashes`


Systemet deler verden inn i ruter ved hjelp av [Geohash-systemet] (https://en.wikipedia.org/wiki/Geohash), der hvert tegn i hashen representerer større presisjon:



- Nivå 4** (f.eks. `u33d`): Dekker ca. 25 km × 25 km - ideelt for byomfattende diskusjoner
- Nivå 6** (f.eks. `u33d8z`): Dekker ca. 1,2 km × 1,2 km - nabolagspresisjon
- Nivå 8** (f.eks. `u33d8z1k`): Dekker omtrent 150 m × 150 m - nøyaktighet for gatesegmenter


Presisjonsvalg balanserer personvern med nytte: Høyere nivåer skaper mer eksklusive soner, men avslører posisjonen din mer nøyaktig.


### Bli med i `#geohash`-kanaler


1. Åpne menyen `#lokasjonskanaler`.

2. Velg ønsket presisjonsnivå, og skriv inn `#geohash` (f.eks. #u33d)

3. Trykk på `Teleport`-knappen for å bli med i `#location channel`.


![image](assets/en/12.webp)


Alternativt kan du trykke på "kartikonet" for å bruke kartvisningen til å bestemme presisjonsnivået, og trykke på "velg" for å bli med i "lokasjonskanalen".


![image](assets/en/13.webp)


**Viktig påminnelse**: _#geohash-funksjonalitet krever en aktiv internettforbindelse - i motsetning til BLE mesh som fungerer offline via Bluetooth


## 8️⃣ Varmekart


Heatmaps er en kul måte å oppdage Bitchat-hendelser og -kanaler rundt om i verden. [Bitmap] (https://bitmap.lat/) visualiserer og sporer anonyme, stedsbaserte meldinger på tvers av Nostr-nettverket, og viser kortvarige Nostr-hendelser. Ta en titt og bli med i stedsspesifikke kanaler og chatter.


![image](assets/en/15.webp)


## 🎯 Konklusjon


Bitchat muliggjør sikker, desentralisert kommunikasjon i situasjoner der tradisjonell meldingsformidling ikke fungerer. Den kan fungere uten internettinfrastruktur ved hjelp av BLE mesh-nettverk, noe som gjør den egnet for protester, katastrofesoner og avsidesliggende områder der tilkoblingsmulighetene er begrensede eller sensurerte. Appen sikrer personvernet gjennom kryptering med flyktige nøkler, geohash-baserte lokasjonskanaler og sletting av data i panikkmodus.


Appen er fortsatt i en tidlig utviklingsfase, men den er allerede lovende. Brukere bør forvente sporadiske feil og rapportere problemer via [GitHub] (https://github.com/permissionlesstech/bitchat-android/issues). Forbedringer er planlagt, blant annet integrering av `ecash` for private transaksjoner i appen ved hjelp av Cashu-protokollen.


![image](assets/en/14.webp)


## 📚 Bitchat Resources


[Github] (https://github.com/permissionlesstech) | [Website] (https://bitchat.free/)| [Whitepaper] (https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)