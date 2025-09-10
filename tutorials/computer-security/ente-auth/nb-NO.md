---
name: Ente Auth
description: En åpen kildekode, ende-til-ende-kryptert 2FA-autentisering
---
![cover](assets/cover.webp)



To-faktor autentisering (2FA) har blitt uunnværlig for å sikre nettkontoene våre. I tillegg til det vanlige passordet kreves det en midlertidig kode, som vanligvis genereres av et dedikert program. Denne mekanismen, kjent som TOTP (Time-Based One-Time Password), garanterer at selv om passordet ditt blir kompromittert, vil en angriper ikke kunne få tilgang til kontoen din uten å ha denne andre faktoren, som fornyes hvert 30. sekund.



Det er imidlertid ikke trivielt å velge riktig autentiseringsprogram. Google Authenticator er populær, men har store begrensninger: proprietær kode som er umulig å kontrollere, synkronisering uten ende-til-ende-kryptering og risiko for totalt tap av koder hvis det oppstår problemer med telefonen. Andre løsninger, som Authy, krever et telefonnummer og garanterer ikke total konfidensialitet.



**Ente Auth** skiller seg ut som et moderne og sikkert alternativ. Denne gratis, åpen kildekode-applikasjonen for flere plattformer, utviklet av teamet bak [Ente Photos] (https://ente.io), tilbyr ende-til-ende-kryptert sikkerhetskopiering i skyen og sømløs synkronisering mellom alle enhetene dine. I motsetning til proprietære løsninger gir Ente Auth deg full kontroll over autentiseringskodene dine, uten at det går på bekostning av personvernet ditt.



I denne veiledningen viser vi deg trinn for trinn hvordan du installerer og bruker Ente Auth, og hvorfor denne løsningen skiller seg fra tradisjonelle autentiseringsløsninger.



## Vi introduserer Ente Auth



Ente Auth ble utviklet av teamet bak Ente Photos, en ende-til-ende-kryptert og personvernvennlig fotolagringstjeneste. I tråd med Ente-filosofien ("Ente" betyr "min" på malayalam, og symboliserer kontroll over dataene dine) ble Ente Auth utviklet for å gi brukerne tilbake full kontroll over tofaktorautentiseringskodene sine.



### Hovedfunksjoner



**Standard TOTP-koder **: Ente Auth genererer midlertidige koder som er kompatible med de fleste tjenester (GitHub, Google, Binance, ProtonMail osv.). Du kan legge til så mange 2FA-kontoer du trenger, og programmet beregner kodene basert på de oppgitte hemmelighetene.



**Ende-til-ende-kryptert sikkerhetskopiering i skyen**: Kodene dine lagres sikkert på nettet. Det er bare du som kan dekryptere dem - krypteringsnøkkelen er avledet fra passordet ditt og er kun kjent for deg. Ente (serveren) har ingen kjennskap til hemmelighetene dine, eller til og med kontotitlene dine, ettersom alt er kryptert på klientsiden ved hjelp av en nullkunnskapsarkitektur.



**Synkronisering av flere enheter**: Du kan installere Ente Auth på flere enheter (smarttelefon, nettbrett, datamaskin) og få tilgang til kodene dine på dem alle. Eventuelle endringer overføres automatisk og umiddelbart til de andre enhetene dine via den krypterte skyen, noe som gir deg stor fleksibilitet i det daglige arbeidet.



**Minimalistisk, intuitiv Interface**: Programmet tilbyr en strømlinjeformet Interface, som er enkel å lære selv for ikke-tekniske brukere. 2FA-kontoer vises med tjenestenavnet, innloggingen din og den 6-sifrede koden, som oppdateres i sanntid. Ente Auth viser også den neste koden noen sekunder i forveien, slik at du unngår å bli tatt på sengen når koden utløper.



**Åpen kildekode og revidert**: Ente Auths kildekode er [offentlig på GitHub] (https://github.com/ente-io/auth) under AGPL v3.0-lisensen. Alle utviklere kan revidere den for å se etter feil eller uønsket oppførsel. Kryptografien som er implementert har vært gjenstand for en [uavhengig ekstern revisjon](https://ente.io/blog/cryptography-audit/), en garanti for seriøsiteten i applikasjonens sikkerhet.



### Fordeler og begrensninger



**Fordeler:**




- Innebygd personvern med ende-til-ende-kryptering
- Sikker synkronisering mellom alle enhetene dine
- Etterprøvbar åpen kildekode
- Interface oversiktlig, intuitiv bruker Interface
- Automatisk sikkerhetskopiering for å forhindre tap av koder
- Tilgjengelig på alle plattformer (mobil og PC)



**Begrensninger:**




- Internett-tilkobling kreves for synkronisering
- Avanserte brukere foretrekker kanskje 100 % offline-løsninger som Aegis (kun Android)
- Relativt ny sammenlignet med etablerte løsninger



## Installasjon



Ente Auth er tilgjengelig på de fleste populære plattformer. Du kan laste ned applikasjonen fra [det offisielle nettstedet] (https://ente.io/auth) eller fra de offisielle butikkene.



![Installation d'Ente Auth](assets/fr/01.webp)



*Ente Auth-nedlastingsside med alle tilgjengelige plattformer*



### Android


Du har flere alternativer:




- Google Play Store**: Søk etter "Ente Auth" for klassisk installasjon
- F-Droid**: Tilgjengelig fra Android-applikasjonskatalogen med åpen kildekode, med garanti for verifisert konstruksjon og uten proprietært innhold
- Manuell installasjon** : APK-filer kan lastes ned fra [prosjektets GitHub-side] (https://github.com/ente-io/auth/releases) med integrert varsling om nye versjoner



### iOS (iPhone/iPad)


Installer Ente Auth direkte fra Apple App Store ved å søke etter appnavnet. IOS-appen kan også kjøres på Mac-maskiner utstyrt med Apple Silicon-brikker (M1/M2) via Mac App Store.



### Datamaskiner (Windows, macOS, Linux)


Ente Auth tilbyr native desktop-applikasjoner. Besøk [ente.io/download] (https://ente.io/download) eller [Releases-delen av GitHub] (https://github.com/ente-io/auth/releases) :





- Windows**: Et EXE-installasjonsprogram følger med
- macOS**: Dra og slipp DMG-diskbilde i Programmer
- Linux** : Flere formater tilgjengelige (AppImage portable, .deb for Debian/Ubuntu, .rpm for Fedora/Red Hat)



**Denne veiledningen er basert på Ente Auth v4.4.4 og nyere. Tidligere versjoner kan ha mindre Interface-forskjeller.



### Interface Web


Uten installasjon kan du få tilgang til kodene dine via [auth.ente.io] (https://auth.ente.io) fra hvilken som helst nettleser. Interface web er begrenset til visning av koder (nyttig for feilsøking), ettersom det å legge til kontoer av sikkerhetsgrunner krever mobil- eller skrivebordsapplikasjonen.



## Første konfigurasjon



### Opprettelse av konto



Når du starter Ente Auth for første gang, har du to alternativer:



![Premier lancement d'Ente Auth](assets/fr/02.webp)



*Startskjermbildet til Ente Auth med alternativer for kontooppretting*



**Med konto (anbefalt)**: Velg "Opprett konto" og skriv inn e-postadressen din Address og et passord. **Viktig**: Dette passordet fungerer som hovedpassord for kryptering av dataene dine. Velg et sterkt, unikt passord, da det ikke finnes noen konvensjonell tilbakestillingsprosedyre uten tap av data. Hvis du mister det, vil de krypterte dataene dine ikke kunne gjenopprettes.



**Offline-modus**: Velg "Bruk uten sikkerhetskopier" for å bruke applikasjonen lokalt uten en sky. I denne modusen forblir kodene dine på enheten, men du må eksportere dem manuelt for å unngå å miste dem.



![Vérification email et récupération de clé](assets/fr/03.webp)



*E-postbekreftelse og generering av 24 ords gjenopprettingsnøkkel*



Du kan bli bedt om en e-postbekreftelse for å bekrefte opprettelsen av kontoen og aktivere gjenoppretting på en ny enhet. Ente Auth vil også gi deg en gjenopprettingsnøkkel på 24 ord (basert på BIP39-metoden). **Det er viktig at du lagrer denne nøkkelen** på et trygt sted: Det er den eneste måten du kan gjenopprette dataene dine på hvis du glemmer passordet ditt.



### Lokal sikkerhet



Jeg anbefaler på det sterkeste at du aktiverer lokal beskyttelse med kode eller biometri. Gå til **Innstillinger → Sikkerhet → Låseskjerm** og konfigurer :





- Biometrisk opplåsing**: Ansikts-ID, fingeravtrykk, avhengig av enhetens funksjoner
- Applikasjonsspesifikk PIN-kode/passord**
- Automatisk låsing med forsinkelse**: f.eks. "Umiddelbart" eller etter 30 sekunder uten aktivitet



Denne beskyttelsen forhindrer uautorisert tilgang til kodene dine hvis noen får tilgang til den ulåste telefonen din. Merk at denne låsen er en ekstra barriere: dataene dine forblir ende-til-ende-kryptert selv uten denne beskyttelsen.



## Legg til 2FA-kontoer



### Standard prosedyre



For å legge til en ny 2FA-konto, la oss ta et konkret eksempel med aktivering av 2FA på Bull Bitcoin :



![Configuration du premier compte](assets/fr/04.webp)



*Ente Auths hoved Interface klar til å legge til den første 2FA*-kontoen



**Tjenestesiden (Bull Bitcoin)**: Logg inn på Bull Bitcoin-kontoen din, gå til sikkerhetsinnstillinger og aktiver tofaktorautentisering.



![Paramètres de sécurité Bull Bitcoin](assets/fr/05.webp)



*Interface Bull Bitcoin* meny for sikkerhetsinnstillinger



![Activation 2FA Bull Bitcoin](assets/fr/06.webp)



*Mulighet for å aktivere tofaktorautentisering på Bull Bitcoin*



Tjenesten viser deretter en QR-kode som du kan skanne med autentiseringsprogrammet ditt:



![QR code 2FA Bull Bitcoin](assets/fr/07.webp)



*QR-kode generert av Bull Bitcoin som skal skannes med autentiseringsenheten din*



**I Ente Auth**: Klikk på "Enter a setup key" og skann deretter QR-koden som vises av Bull Bitcoin. Ente Auth vil automatisk gjenkjenne kontoen og fylle ut feltene.



![Ajout du compte dans Ente Auth](assets/fr/08.webp)



*Konfigurere Bull Bitcoin-kontodetaljer i Ente Auth*



Du kan tilpasse navnet på tjenesten og påloggingen din for å gjøre den enklere å finne. Avanserte innstillinger (SHA1-algoritme, 30s periode, 6 sifre) er vanligvis riktige som standard.



**Validering på tjenestesiden**: Gå tilbake til Bull Bitcoin og skriv inn den 6-sifrede koden som genereres av Ente Auth for å fullføre aktiveringen.



![Saisie du code 2FA](assets/fr/09.webp)



*Skriv inn kode generert av Ente Auth for å validere 2FA*-aktivering



![2FA activée](assets/fr/10.webp)



*Bekreftelse på vellykket 2FA-aktivering på Bull Bitcoin*



**Backup-koder**: Bull Bitcoin gir deg gjenopprettingskoder. **Lagre dem på et trygt sted, atskilt fra autentiseringsenheten.



![Gestion des codes de sauvegarde](assets/fr/11.webp)



*Mulighet for generate nødreservekoder på Bull Bitcoin*



![Codes de récupération](assets/fr/12.webp)



*Liste over gjenopprettingskoder som skal oppbevares på et trygt sted*



### Organisering og ledelse



Ente Auth tilbyr flere praktiske funksjoner:



**Hurtigkopiering**: Trykk på koden for å kopiere den automatisk til utklippstavlen.



**Kontekstsensitive handlinger**: Trykk og hold nede (eller høyreklikk på skrivebordet) for å redigere, slette, dele eller feste en oppføring.



**Tagger og søk**: Organiser kontoene dine med tagger (personlig/profesjonell, etter tjenestekategori), og bruk søkefeltet til å filtrere raskt.



![Création d'un tag](assets/fr/17.webp)



*Opprettelsesprosess for tagger: kontekstuell meny og opprettelsesdialog*



![Tag appliqué](assets/fr/18.webp)



*Taggen "Bitcoin" er vellykket brukt på Bull Bitcoin*-kontoen



**Automatiske ikoner**: Hver oppføring kan illustreres med tjenestens logo, takket være integreringen av ikonpakken [Simple Icons] (https://simpleicons.org/).



**Temporær sikker deling**: Sikker deling er en unik Ente Auth-funksjon som lar deg sende en 2FA-kode til en kollega uten å avsløre den underliggende hemmeligheten. generate en kryptert lenke som er gyldig i maksimalt 2, 5 eller 10 minutter - mottakeren ser koden i sanntid, men kan ikke eksportere den eller få tilgang til kontodata. Denne metoden er ideell for teknisk assistanse eller midlertidig samarbeid, og gir et sikkerhetsnivå som ikke er mulig med et enkelt skjermbilde eller en tekstmelding.



![Partage sécurisé](assets/fr/19.webp)



*Interface midlertidig sikker deling: velg varighet (5 min)*



**Sikker eksport/import**: Med Ente Auth kan du eksportere kodene dine til andre applikasjoner, eller importere dem fra Google Authenticator og andre løsninger. Eksporten skjer via en kryptert fil eller QR-kode, slik at du kan overføre dataene dine uten at det går på bekostning av sikkerheten.



**BIP39-gjenopprettingsnøkkel**: Programmet genererer automatisk en gjenopprettingsfrase på 24 ord i henhold til BIP39-standarden (Bitcoin Improvement Proposal), som er identisk med kryptovaluta-lommebøker. Denne frasen er din ultimate gjenopprettingsnøkkel, slik at du kan gjenopprette alle kodene dine selv om du glemmer hovedpassordet ditt.



## Konfigurasjon og innstillinger



Ente Auth tilbyr en rekke tilpasningsmuligheter som er tilgjengelige via programinnstillingene:



![Paramètres principaux d'Ente Auth](assets/fr/13.webp)



*Oversikt over tilgjengelige parametere i Ente Auth*



### Konto- og datahåndtering



![Paramètres de sécurité](assets/fr/14.webp)



*Avanserte sikkerhetsalternativer: e-postbekreftelse, PIN-kode, aktive økter*



Med sikkerhetsinnstillingene kan du :




- Aktiver e-postbekreftelse for nye tilkoblinger
- Aktiver passordnøkkel
- Se aktive økter på de ulike enhetene dine
- Sette opp en PIN-kode eller biometri



### Interface og bruksalternativer



![Paramètres généraux](assets/fr/15.webp)



*Interface-parametere og applikasjonstilpasning*



Generelle innstillinger inkluderer :




- Språk**: Interface flerspråklig
- Display**: Store ikoner, kompakt modus
- Personvern**: Skjul koder, hurtigsøk
- Telemetri**: Feilrapportering (kan deaktiveres)



## Sikkerhetskopiering og synkronisering



### Slik fungerer kryptering



Når du legger til en konto med en tilkoblet Ente-konto, krypterer programmet umiddelbart disse sensitive dataene lokalt ved hjelp av hovednøkkelen din (utledet fra passordet ditt). De krypterte dataene sendes deretter til Ente-serveren for lagring.



Takket være denne mekanismen er en ende-til-ende-kryptert sikkerhetskopi av kodene dine alltid tilgjengelig i skyen. Hvis du mister enheten din, er det bare å installere Ente Auth på nytt og koble til igjen: Programmet vil automatisk laste ned og dekryptere alle kodene dine.



### Synkronisering av flere enheter



Hvis du bruker Ente Auth på både smarttelefonen og datamaskinen, vil eventuelle tilføyelser eller endringer på den ene enheten vises i løpet av sekunder på den andre. Denne synkroniseringen går gjennom Ente-skyen, men siden dataene er kryptert fra ende til ende, ser serveren bare uleselig kryptert innhold.



![Synchronisation mobile](assets/fr/16.webp)



*Synkroniseringsdemo: samme Bull Bitcoin-konto tilgjengelig på mobil og datamaskin*



Synkroniseringen er sømløs: installer Ente Auth på smarttelefonen din, logg inn med legitimasjonen din, og alle 2FA-kodene dine (her Bull Bitcoin) vises automatisk. Eksemplet ovenfor viser perfekt synkronisering mellom PC og mobil - den samme Bull Bitcoin-koden er tilgjengelig på begge enhetene.



Når det gjelder konfidensialitet, har verken Ente eller noen tredjepart tilgang til 2FA-hemmelighetene dine. Selv metadata (tagger, notater, tjenestenavn) krypteres før de sendes. Denne nullkunnskapsarkitekturen sikrer at bare du kan dechiffrere kodene dine.



### Frakoblet bruk



Synkronisering krever Internett, men Ente Auth fungerer perfekt offline på alle enheter, siden alle data lagres lokalt. Frakoblede endringer settes i kø og synkroniseres så snart tilkoblingen er gjenopprettet.



## Sikkerhet og personvern



### Kryptografiske garantier



Ente Auth er basert på robust ende-til-ende-kryptering med nullkunnskapsarkitektur. Kodene dine krypteres med en nøkkel som du er alene om å ha, og som er avledet fra hovedpassordet ditt ved hjelp av avanserte nøkkelderiveringsfunksjoner.



**Zerkunnskapsarkitektur: Ente har ikke fysisk tilgang til dataene dine. Selv metadata (tjenestenavn, tagger, notater) krypteres på klientsiden før overføring. Denne tilnærmingen sikrer at Ente, i tilfelle et angrep på serverne dine eller en forespørsel fra myndighetene, bare kan utlevere krypterte data som ikke kan leses uten passordet ditt.



**Lokal kryptering**: Krypteringsprosessen foregår i sin helhet på enheten din før den sendes til skyen. Entes servere mottar og lagrer kun krypterte data, noe som gjør uautorisert tilgang umulig, selv for tjenesteadministratorer.



### Åpenhet og revisjon



Siden koden er [åpen kildekode](https://github.com/ente-io/auth), kan samfunnet verifisere at det ikke finnes bakdører. Ente har fått utført [flere eksterne revisjoner](https://ente.io/blog/cryptography-audit/) for å validere sikkerheten i implementeringen:





- Cure53** (Tyskland): Applikasjons- og kryptografisk sikkerhetsrevisjon
- Symbolic Software** (Frankrike): Spesialisert kryptografisk ekspertise
- Fallible** (India): Penetrasjonstesting og sårbarhetsanalyse



Disse uavhengige revisjonene, som utføres av anerkjente firmaer, garanterer at Ente Auths kryptografiske implementering er i samsvar med beste sikkerhetspraksis og ikke har noen kritiske feil.



### Retningslinjer for personvern



Ente Auth bruker en [eksemplarisk personvernerklæring] (https://ente.io/privacy/) basert på minimal datainnsamling. Kun informasjon som er strengt nødvendig for driften av tjenesten oppbevares: din e-post Address for autentisering og kontogjenoppretting.



**Ingen sporing eller telemetri**: I motsetning til de fleste applikasjoner samler Ente Auth ikke inn bruksmålinger, identifiserende krasjdata eller atferdsinformasjon. Programmet fungerer uten påtrengende reklame eller analytiske sporere.



**GDPR-samsvar**: Ente overholder den europeiske personvernforordningen fullt ut. Du har rett til å få tilgang til, korrigere eller slette dataene dine når som helst. Dataeksport] (https://ente.io/take-control/) er bare et klikk unna, og permanent sletting av kontoen din sletter alle dataene dine fra serverne.



**Desentralisert, sikker lagring**: De krypterte dataene dine replikeres på tre forskjellige leverandører i tre forskjellige land, noe som garanterer optimal tilgjengelighet samtidig som du unngår avhengighet av én enkelt skyleverandør.



Entes forretningsmodell er basert på den betalte Ente Photos-tjenesten, noe som gjør det mulig for oss å tilby Ente Auth **gratis og uten begrensninger** uten å gå på akkord med personvernet ditt ved å tjene penger på dataene dine. Denne tilnærmingen garanterer tjenestens bærekraft uten å basere seg på reklame eller videresalg av personopplysninger.



## Sammenligning med andre løsninger



| Application              | Open Source | Sauvegarde Cloud | E2EE | Sync multi-devices | Plateformes                                        |
| ------------------------ | ----------- | ---------------- | ---- | ------------------ | -------------------------------------------------- |
| **Ente Auth**            | ✅           | ✅                | ✅    | ✅                  | Android, iOS, Linux, macOS, Windows                |
| **Google Authenticator** | ❌           | ✅ (sans E2EE)    | ❌    | ✅                  | Android, iOS                                       |
| **Aegis**                | ✅           | ❌                | ✅    | ❌                  | Android                                            |
| **Authy**                | ❌           | ✅                | ❌    | ✅                  | Android, iOS *(apps desktop supprimées août 2024)* |
| **Proton Auth**          | ✅           | ✅                | ✅    | ✅                  | Android, iOS *(récent, moins établi)*              |

Ente Auth skiller seg ut som en av de få løsningene som kombinerer alle fordelene: åpenhet i kildekoden, kryptert sikkerhetskopiering i skyen og synkronisering på tvers av plattformer.



## Anbefalte bruksområder



### Individuelle brukere



Ente Auth er ideell for sikkerhetsbevisste personer som systematisk aktiverer 2FA. Du trenger ikke lenger å bekymre deg for å miste kodene dine når du bytter telefon, eller å måtte velge mellom bekvemmelighet og sikkerhet.



### Familie og bruk av flere enheter



Appen kommer til sin rett hvis du bruker flere enheter. Du kan lagre kodene dine på smarttelefoner og nettbrett, eller dele visse familiekoder (Netflix, familieskyen) synkront og sikkert.



### Profesjonell bruk



For team som administrerer sensitive kontoer, gjør Ente Auth det enklere å samarbeide samtidig som sikkerheten ivaretas, takket være de avanserte delingsfunksjonene som er integrert i delen "Organisering og administrasjon".



## Beste praksis





- Lagre nødkodene dine**: Hold gjenopprettingskodene fra hver tjeneste borte fra telefonen.





- Bruk et sterkt hovedpassord**: Hovedpassordet til Ente Auth må være unikt og robust, ettersom det beskytter alle kodene dine.





- Aktiver lokal beskyttelse**: Konfigurer PIN-kode eller biometri for å hindre uautorisert fysisk tilgang.





- Ikke overtilpasse**: Unngå avanserte modifikasjoner som kan gå ut over synkroniseringen.





- Hold applikasjonen oppdatert**: Oppdateringer retter sikkerhetshull og forbedrer funksjonaliteten.





- Test gjenoppretting**: Sjekk av og til at du kan gjenopprette kodene dine på en annen enhet.



## Konklusjon



Ente Auth representerer en moderne og omfattende løsning for tofaktorautentisering. Ved å kombinere sikkerhet, åpenhet og brukervennlighet oppfyller denne applikasjonen med åpen kildekode behovene til krevende brukere uten at det går på bekostning av brukervennligheten.



I motsetning til proprietære løsninger som låser deg inn i et ugjennomsiktig økosystem, gir Ente Auth deg tilbake kontrollen over autentiseringsdataene dine og beskytter deg samtidig mot utilsiktet tap takket være krypterte sikkerhetskopier.



Enten du er en privatperson som ønsker å sikre dine personlige kontoer, eller et team som administrerer bedriftstilgang, er Ente Auth et smart valg for å modernisere din tilnærming til digital sikkerhet uten at det går på bekostning av personvernet.



## Ressurser og støtte



### Offisiell dokumentasjon




- Offisiell nettside**: [ente.io/auth] (https://ente.io/auth)
- Hjelpesenter**: [help.ente.io/auth] (https://help.ente.io/auth)
- Teknisk blogg**: [ente.io/blog](https://ente.io/blog)



### Kildekode og åpenhet




- GitHub**: [github.com/ente-io/auth](https://github.com/ente-io/auth)
- Kryptografirevisjon**: [ente.io/blog/cryptography-audit] (https://ente.io/blog/cryptography-audit)



### Fellesskapet




- Discord**: [discord.gg/z2YVKkycX3] (https://discord.gg/z2YVKkycX3)
- Reddit**: [r/enteio](https://reddit.com/r/enteio)