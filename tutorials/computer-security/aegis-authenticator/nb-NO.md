---
name: Aegis Authenticator
description: Hvordan kan du bruke Aegis Authenticator til å sikre kontoene dine med dobbel autentisering?
---

![cover](assets/cover.webp)



I dag er tofaktorautentisering (2FA) avgjørende for å sikre nettkontoer. I tillegg til passordet legges det til en ekstra faktor (ofte en sekssifret kode) som utløper etter 30 sekunder, noe som gjør det betydelig vanskeligere for hackere. Det er tryggere å bruke en dedikert TOTP-applikasjon (*Time-based One-Time Password*) enn SMS, som kan kapres ved SIM-bytteangrep.



Men ikke alle autentiseringsapplikasjoner er like gode. Mange proprietære løsninger (Google Authenticator, Authy osv.) byr på problemer: De er proprietære og har lukket kildekode (umulig å kontrollere sikkerheten), integrerer noen ganger reklamesporere, tilbyr ikke kryptert sikkerhetskopiering av kodene dine og kan til og med forhindre eksport av kontoene dine for å låse deg inn i økosystemet deres.



Aegis Authenticator, derimot, presenterer seg som et gratis og etisk alternativ til disse applikasjonene. Aegis er en gratis, sikker applikasjon med åpen kildekode for å administrere totrinnsbekreftelsestokens på Android. Utviklingen fokuserer på viktige funksjoner som andre apper ikke tilbyr, inkludert robust kryptering av lokale data og muligheten for sikker sikkerhetskopiering. Alt i alt tilbyr Aegis en lokal, reviderbar løsning for dobbel autentisering, som er ideell for alle som ønsker å ha full kontroll over sine 2FA-koder.



## Vi introduserer Aegis Authenticator



Aegis Authenticator er en 2FA-applikasjon med åpen kildekode for Android, utgitt under GPL v3-lisensen. Den skiller seg ut med sin "privacy by design"-filosofi: applikasjonen fungerer helt offline og krever ingen tilkobling til en ekstern tjeneste. Tokenene dine forblir derfor lagret lokalt på enheten din, i en sikker safe som bare du har nøkkelen til.



### Viktige funksjoner



**Kryptert hvelv:** Alle OTP-kodene dine lagres i et AES-256-kryptert hvelv (GCM-modus), beskyttet av et brukerdefinert hovedpassord. Du kan låse opp dette hvelvet via passord eller biometriske data (fingeravtrykk, ansiktsgjenkjenning) for ekstra bekvemmelighet. Uten passord vil dataene være ukrypterte, så vi anbefaler på det sterkeste at du angir et passord.



**Avansert organisering:** Aegis holder orden på de mange 2FA-kontoene dine. Du kan sortere oppføringene alfabetisk eller i den rekkefølgen du ønsker, gruppere dem etter kategori (f.eks. Personlig, Jobb, Sosial) for enkel gjenfinning, og tildele hver oppføring et personlig ikon. Et søkefelt er inkludert for å finne en tjeneste eller konto umiddelbart ved hjelp av navnet.



**Krypterte lokale sikkerhetskopier:** For å sikre at du aldri mister tilgangen til kontoene dine, tilbyr Aegis automatisk sikkerhetskopiering av safen din. Disse er krypterte (via et passord) og kan lagres på et valgfritt sted (intern lagring, skymappe osv.). Programmet kan også eksportere kontodatabasen manuelt, i kryptert eller ukryptert format etter behov. Det er like enkelt å importere kontoer fra andre 2FA-programmer (Aegis støtter import fra Authy, Google Authenticator, FreeOTP, andOTP osv.).



**Sikkerhet og personvern:** Programmet er som standard helt frakoblet. Det krever ingen nettverkstillatelser - noe som betyr at det ikke overfører data til omverdenen, og det inneholder ingen annonsesporere eller atferdsanalysemoduler. Aegis viser ikke annonser, og krever ingen brukerkonto: Så snart det er installert, er det oppe og går uten registrering. Siden kildekoden er offentlig på GitHub, kan fellesskapet fritt revidere den, noe som garanterer fraværet av ondsinnede eller skjulte funksjoner.



**Moderne Interface:** Aegis har en ryddig Material Design, med støtte for mørke temaer (inkludert en AMOLED-modus) og til og med en valgfri flisvisning for å vise kodene dine som rutenett. Interface er ryddig, uten dikkedarer, og forhindrer skjermopptak av koder som et sikkerhetstiltak.



## Installasjon



Siden Aegis Authenticator er åpen kildekode, foretrekker utviklerne personvernvennlige distribusjonskanaler. Det er to hovedmåter å installere den på:



### Via F-Droid (anbefalt)



Den tryggeste og enkleste måten er gjennom F-Droid, den gratis alternative butikken. Hvis F-Droid ennå ikke er installert på telefonen din, kan du starte med å laste den ned fra det offisielle nettstedet [F-Droid.org] (https://f-droid.org). Deretter :





- Åpne F-Droid og sørg for at du har oppdatert repositoriene dine for å få den nyeste listen over applikasjoner
- Søk etter "Aegis Authenticator" i F-Droid. Den offisielle applikasjonen skal vises (utgiver: Beem Development)
- Start installasjonen ved å trykke på Install. Siden Aegis er et av programmene som er verifisert av F-Droid, kan du dra nytte av en pålitelig og sikker nedlasting



Ved å installere via F-Droid får du fordelen av å motta automatiske programoppdateringer så snart de blir utgitt. I tillegg garanterer F-Droid at applikasjonen er fri for uønskede proprietære komponenter.



### Via GitHub (signert APK)



Hvis du foretrekker å installere applikasjonen uten å gå gjennom en butikk, kan du laste ned den offisielle APK-en direkte fra prosjektets GitHub-side. På Aegis repository ([github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis)), gå til delen Releases der stabile versjoner publiseres.





- Last ned den nyeste APK-versjonen
- Før du installerer APK-filen, må du sørge for at du har godkjent installasjon av applikasjoner fra ukjente kilder på enheten din (i Android-innstillinger)
- APK-en som tilbys på GitHub er signert av utvikleren med samme nøkkel som på F-Droid



Etter manuell installasjon vil applikasjonen fungere identisk. Vær oppmerksom på at oppdateringer ikke vil skje automatisk: du må sjekke GitHub med jevne mellomrom for nye versjoner.



### Google Play Store vs F-Droid



Aegis Authenticator er tilgjengelig både i Google Play Store og F-Droid, slik at du kan velge hvilken installasjonsmetode du vil bruke:



**Google Play Store:**




- ✅ Automatiske oppdateringer integrert i Android-systemet
- ✅ Enkel, velkjent installasjon
- ✅ Samme signerte APK som på andre kanaler



**F-Droid (anbefalt) :**




- ✅ Gratis butikk med åpen kildekode
- ✅ Reproduserbar og etterprøvbar konstruksjon
- ✅ Ingen Google-tjeneste kreves
- ✅ Respekt for fri programvare-filosofien



Valget mellom disse to alternativene avhenger av dine preferanser når det gjelder Googles økosystem. Hvis du foretrekker enkelhet, er Play Store ideell. Hvis du vil ha en mer personvernvennlig tilnærming, uavhengig av Google-tjenester, er F-Droid det bedre valget.



## Første konfigurasjon



Når Aegis startes for første gang, foreslås det en innledende konfigurasjonsprosedyre for å sikre 2FA-koden din:



![Configuration initiale Aegis](assets/fr/01.webp)



*Innledende Aegis-konfigurasjonsprosess: velkomstskjermbilde, sikkerhetsvalg, definisjon av hovedpassord og ferdigstilling*



### Angi et hovedpassord



Aegis vil først be deg om å velge et hovedpassord. Dette passordet vil bli brukt til å kryptere alle autentiseringstokener som er lagret i hvelvet. Vi anbefaler på det sterkeste at du velger et sterkt, unikt passord som bare du kjenner til.



**⚠️ Advarsel:** Ikke glem dette passordet - hvis du mister det, vil de krypterte 2FA-kodene dine bli utilgjengelige (det finnes ingen bakdør). Aegis vil be deg om å skrive inn passordet to ganger for bekreftelse.



### Aktiver biometrisk opplåsing (valgfritt)



Hvis Android-enheten din er utstyrt med en fingeravtrykksleser eller en annen biometrisk sensor, vil Aegis be deg om å aktivere biometrisk opplåsing. Dette alternativet er valgfritt, men veldig praktisk: Det lar deg raskt låse opp applikasjonen med fingeravtrykket eller ansiktet ditt, i stedet for å skrive inn passordet hver gang.



Merk at biometri er en ekstra bekvemmelighet: Hovedpassordet ditt kreves fortsatt hvis biometrien endres eller enheten startes på nytt.



### Oppdag programinnstillinger



Når du er inne i applikasjonen (hovedskjermen Interface er tom til å begynne med), kan du gjøre deg kjent med de tilgjengelige konfigurasjonsalternativene. Åpne innstillingene via rullegardinmenyen øverst til høyre på skjermen (tre vertikale prikker), og velg deretter "Settings".



![Interface principale et paramètres](assets/fr/02.webp)



*Interface hoved Aegis tom ved start, tilgang til parametermeny og oversikt over tilgjengelige alternativer*



Aegis-innstillingsmenyen samler flere viktige deler:





- Utseende**: Tilpass tema (lys, mørk, AMOLED), språk og andre visuelle innstillinger
- Oppførsel**: Konfigurer programmets oppførsel når det samhandler med listen over oppføringer
- Ikonpakker**: Administrer og importer ikonpakker for å tilpasse utseendet på kontoene dine
- Sikkerhet**: Innstillinger for kryptering, biometrisk opplåsing, automatisk låsing og andre sikkerhetsparametere
- Sikkerhetskopier**: Konfigurer automatisk sikkerhetskopiering til et sted du selv velger
- Import og eksport**: Importer sikkerhetskopier fra andre autentiseringsprogrammer og eksporter Aegis-hvelvet manuelt
- Revisjonslogg**: Detaljert logg over alle viktige hendelser i applikasjonen



Denne oversiktlige organiseringen gjør at du kan konfigurere Aegis i henhold til dine preferanser og sikkerhetsbehov.



## Legg til en 2FA-konto



Når Aegis er konfigurert, kan vi gå videre til det viktigste: å legge til tofaktorkontoer. Prosessen er enkel, og Aegis tilbyr flere metoder for å integrere autentiseringskodene dine.



### De tre tilgjengelige addisjonsmetodene



Fra hovedskjermen i Aegis Interface trykker du på **+**-knappen nederst til høyre for å få tilgang til alternativene for å legge til. Du har tre alternativer:





- Skann QR-kode**: Skann QR-koden som vises av nettjenesten direkte
- Skann bilde**: Skann en QR-kode fra et bilde som er lagret på enheten din
- Skriv inn manuelt**: Skriv inn 2FA-kontoinformasjon manuelt



### Praktisk eksempel: konfigurering av Bitwarden



La oss ta et konkret eksempel på aktivering av 2FA på Bitwarden for å illustrere prosessen:



![Exemple avec Bitwarden](assets/fr/04.webp)



*Eksempel på aktivering av 2FA på Bitwarden: Interface web med autentiseringsalternativer og Aegis-anbefaling*





- Logg inn og få tilgang til innstillinger**: Logg inn på Bitwarden-kontoen din og gå til innstillingene, fanen "Sikkerhet"
- Leverandører-delen**: Gå til "Providers"-delen og klikk på "Manage" i "Authenticator app"-delen



![Configuration 2FA avec QR code](assets/fr/05.webp)



*Fullstendig prosess for å legge til en konto: QR-koden vises av tjenesten, den hemmelige nøkkelen er synlig og bekreftelseskoden er tastet inn*





- Skann QR-koden**: Et popup-vindu åpnes med QR-koden og den hemmelige nøkkelen
- I Aegis**: Bruk "Skann QR-kode" for å fange opp informasjon automatisk
- Bekreftelse**: Skriv inn den sekssifrede koden som genereres av Aegis i feltet "Verifiseringskode"
- Aktivering**: Klikk på "Slå på" for å fullføre aktiveringen



### Legg til detaljer manuelt



Hvis du foretrekker eller ikke kan skanne QR-koden, kan du bruke alternativet "Skriv inn manuelt". I skjemaet kan du skrive inn :



![Ajout d'un compte 2FA](assets/fr/03.webp)



*Prosess for å legge til en ny 2FA-konto: tom Interface, legg til alternativer, manuelt inngangsskjema og konto lagt til*





- Navn** : Tjenestenavn (f.eks. Bitwarden, GitHub ...)
- Utsteder** : Utstederen (ofte identisk med navnet)
- Gruppe**: Valgfritt, for å organisere kontoene dine etter kategori
- Merknad** : Personlige bemerkninger til denne kontoen
- Hemmelig** : Den hemmelige nøkkelen som leveres av tjenesten (maskert som standard)
- Avansert**: Avanserte parametere (algoritme, periode, antall sifre)



Når kontoen er lagt til, vises den i listen med gjeldende kode og en tidsindikator som viser hvor lang tid det er igjen før fornyelse.



### Universell kompatibilitet



Aegis er kompatibel med alle tjenester som bruker TOTP- og HOTP-standardene, inkludert praktisk talt alle nettsteder som tilbyr 2FA: sosiale nettverk, banker, passordadministratorer, kryptoplattformer osv.



### Inngangsorganisasjon



Når du har lagt til flere kontoer, vil du sette pris på Aegis' organisasjonsverktøy:





- Tilpasset sortering:** Som standard vises kontoer i alfabetisk rekkefølge, men du kan endre rekkefølgen manuelt
- Grupper og kategorier:** Opprett grupper for å skille personlige kontoer fra bedriftskontoer, eller gruppér dem etter type tjeneste (bank, e-post, sosiale nettverk osv.)
- Tilpassede ikoner:** Aegis prøver automatisk å tildele et passende ikon hvis det er tilgjengelig, ellers kan du velge mellom mange generiske ikoner eller importere et bilde
- Hurtigsøk:** I søkefeltet øverst kan du skrive inn noen få bokstaver for å filtrere ut matchende oppføringer umiddelbart



Ved å berøre en oppføring vises OTP-koden i full størrelse (hvis den var skjult), og du kan kopiere den til utklippstavlen med et langt trykk - praktisk når du skal lime den inn i applikasjonen du vil koble til.



## Sikkerhet og sikkerhetskopiering



Med sikkerhet i sentrum for Aegis er det viktig å forstå hvordan 2FA-kodene dine er beskyttet, og hvordan du sikrer at de vedvarer i tilfelle et problem.



### Sikkerhetsarkitektur



**Robust kryptering**: Alle kodene dine lagres i en kryptert safe ved hjelp av **AES-256-algoritmen i GCM-modus**, kombinert med hovedpassordet ditt. Nøkkelutledningen er basert på **scrypt**, noe som gir forbedret beskyttelse mot brute-force-angrep.



**Sikker opplåsing** : Hovedpassordet kreves for å dekryptere dataene dine. Biometri (valgfritt) bruker **Android Secure Keystore** og TEE (Trusted Execution Environment) for å beskytte krypteringsnøkkelen.



**Minimale tillatelser**: Aegis fungerer offline som standard, og krever kun tilgang til kameraet (QR-skanning), biometri og vibrator. Ingen data samles inn eller deles.



### Alternativer for sikkerhetskopiering



Aegis tilbyr flere ulike backup-strategier for å dekke ulike behov for sikkerhet og brukervennlighet:



![Configuration des sauvegardes](assets/fr/06.webp)



*Interface komplett med ekstra konto, sikkerhetskopivarsel, automatiske innstillinger for sikkerhetskopiering og strategier for sikkerhetskopiering*



**1. Automatisk lokal sikkerhetskopiering **




- Konfigurer en valgfri målmappe
- Tilpassbar frekvens (etter hver endring, daglig osv.)
- Passordbeskyttede krypterte filer (.aesvault)
- Kompatibel med synkroniserte mapper (Nextcloud, Dropbox osv.)



![Sélection du dossier de sauvegarde](assets/fr/07.webp)



*Prosess for valg av sikkerhetskopimappe: filutforsker, målmappe og tilgangsautorisasjon*



**2. Android** sikkerhetskopiering i skyen




- Valgfri integrasjon med Android backup-system
- Kun tilgjengelig for krypterte safer (sikkerhet bevart)
- Transparent sikkerhetskopiering med andre Android-data
- Automatisk gjenoppretting ved enhetsbytte



**3. Manuell** eksport




- Eksporter på forespørsel via **Innstillinger > Import og eksport**
- Valg mellom kryptert (anbefalt) eller klart format
- Nyttig for migreringer eller sporadiske sikkerhetskopier



### God sikkerhetspraksis





- Ta flere sikkerhetskopier** for å forhindre korrupsjon
- Test** sikkerhetskopiene regelmessig ved å prøve å gjenopprette dem
- Oppbevar de servicegodkjente gjenopprettingskodene dine separat**
- Hovedpassordet ditt** er fortsatt påkrevd, selv med sikkerhetskopiering i skyen
- Sikre hovedpassordet ditt**: Bruk et unikt, sterkt passord som er lagret i en passordbehandler
- Hold applikasjonen oppdatert** med de nyeste sikkerhetsoppdateringene
- Aktiver automatisk låsing** i innstillingene for å sikre tilgangen til applikasjonen
- Deaktiver skjermbilder** (standardalternativ) for å forhindre at kodene dine blir snappet opp
- Bruk biometri sparsomt**: Foretrekk passord for kritiske tilganger



## Sammenligning med andre applikasjoner



Hvordan står Aegis seg i forhold til andre populære autentiseringsprogrammer?



### Aegis vs Google Authenticator



**Aegis :**




- ✅ Åpen kildekode og reviderbar
- ✅ Lokal kryptert sikkerhetskopiering
- ✅ Avansert organisering (grupper, ikoner, søk)
- ✅ Ingen datainnsamling
- ❌ Kun Android



**Google Authenticator :**




- ✅ Tilgjengelig på Android og iOS
- ✅ Synkronisering i skyen (siden 2023)
- ❌ Lukket kildekode
- ❌ Begrenset funksjonalitet
- ❌ Potensiell datainnsamling fra Google



### Aegis vs Authy



**Aegis :**




- ✅ Åpen kildekode
- ✅ Ingen konto kreves
- ✅ Eksport av kode mulig
- ✅ Total datakontroll
- ❌ Ingen innebygd synkronisering av flere enheter



**Authy :**




- ✅ Synkronisering av flere enheter
- ✅ Tilgjengelig på Android og iOS
- ❌ Lukket kildekode
- ❌ Krever et telefonnummer
- ❌ Kan ikke eksportere koder
- ❌ Desktop-applikasjoner fjernes i mars 2024



Aegis utmerker seg for Android-brukere som setter pris på åpenhet, lokal sikkerhet og full kontroll over dataene sine. Alternativer som Authy er bedre egnet hvis du absolutt trenger automatisk synkronisering av flere enheter.




## Konklusjon



Aegis Authenticator er en utmerket løsning for deg som er på utkikk etter et personvernvennlig, sikkert og transparent 2FA-program. Den åpne kildekode-tilnærmingen, kombinert med robust kryptering og en pen Interface, gjør den til et førsteklasses valg for å sikre nettkontoene dine.



Selv om Aegis er begrenset til Android og mangler innebygd skysynkronisering, veier Aegis mer enn opp for disse begrensningene med sin "privacy by design"-filosofi og totale datakontroll. For brukere som er opptatt av sitt digitale personvern, tilbyr Aegis et troverdig og kraftfullt alternativ til markedets dominerende proprietære løsninger.



Sikkerheten til nettkontoene dine trenger ikke å være avhengig av kommersielle selskapers velvilje. Med Aegis beholder du kontrollen over autentiseringskodene dine, i en digital safe som bare du har nøkkelen til.



## Ressurser



### Offisielle nettsider




- Offisiell nettside**: [getaegis.app](https://getaegis.app/) - Presentasjon og nedlasting av søknaden
- Kildekode**: [github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis) - Official GitHub repository
- F-Droid** : [f-droid.org/packages/com.beemdevelopment.aegis](https://f-droid.org/packages/com.beemdevelopment.aegis/) - Installasjon via gratisbutikken



### Teknisk dokumentasjon




- Vault-dokumentasjon**: [Vault design] (https://github.com/beemdevelopment/Aegis/blob/master/docs/vault.md) - Teknisk beskrivelse av kryptering og sikker arkitektur
- Offisiell FAQ**: [getaegis.app/#faq](https://getaegis.app/#faq) - Svar på ofte stilte spørsmål
- Prosjektwiki**: [github.com/beemdevelopment/Aegis/wiki] (https://github.com/beemdevelopment/Aegis/wiki) - Full brukerdokumentasjon