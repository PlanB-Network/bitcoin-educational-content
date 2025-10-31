---
name: Proton Authenticator
description: Hvordan kan jeg bruke Proton Authenticator til å sikre kontoene mine med 2FA?
---
![cover](assets/cover.webp)



Tofaktorautentisering (2FA) legger til en ekstra sikkerhetsbarriere for kontoene dine ved å kreve, i tillegg til passordet ditt, ytterligere bevis på at bare du har det. Ved å aktivere 2FA reduseres risikoen for hacking drastisk, selv om passordet ditt blir kompromittert gjennom phishing eller en datalekkasje. Uten 2FA trenger en angriper bare passordet ditt for å få tilgang til kontoene dine, men med 2FA trenger han også den andre faktoren din, noe som avverger de fleste forsøk på kontotyveri.



Det finnes ulike typer 2FA. SMS-koder er bedre enn ingenting, men de er fortsatt sårbare for SIM-bytteangrep og avlytting. Vi anbefaler ikke SMS som primær 2FA. Autentiseringsapplikasjoner (TOTP) generate midlertidige koder lokalt på enheten din, noe som gjør dem mye vanskeligere å avskjære. Fysiske sikkerhetsnøkler gir best sikkerhet, men krever dedikert maskinvare.



Proton Authenticator er en TOTP-autentisering. Det er Protons svar på begrensningene i eksisterende applikasjoner: mange er proprietære, inneholder annonsesporere og tilbyr ikke kryptert sikkerhetskopiering. Proton Authenticator skiller seg ut ved å tilby en applikasjon med åpen kildekode, fri for annonser og sporere, med ende-til-ende-kryptert sikkerhetskopiering.



## Vi introduserer Proton Authenticator



Proton Authenticator er en TOTP-autentiseringsapplikasjon for mobil og PC, utviklet av Proton, som er kjent for sine personvernfokuserte tjenester. Som alle Proton-produkter er applikasjonen åpen kildekode og har gjennomgått uavhengige sikkerhetsrevisjoner. Den er tilgjengelig gratis på alle plattformer (Android, iOS, Windows, macOS, Linux).



Proton Authenticator tilbyr følgende nøkkelfunksjoner:





- Generering av **TOTP-koder** for 2FA-kontoene dine, kompatible med de fleste nettsteder som bruker Google Authenticator, Authy osv.





- **Valgfri kryptert sikkerhetskopiering i skyen**: Du kan koble applikasjonen til Proton-kontoen din for å sikkerhetskopiere og synkronisere kodene dine med ende-til-ende-kryptering. Hvis du mister enheten din, er det bare å koble til en ny for å gjenopprette alle kodene dine.





- **Synkronisering av flere enheter**: Ved å logge inn på Proton i appen synkroniseres 2FA-kodene dine automatisk mellom flere enheter via ende-til-ende-kryptering. På iOS er et alternativ synkronisering via iCloud.





- **Lokal låsing med passord eller biometri**: applikasjonen tilbyr låsing med PIN-kode og/eller fingeravtrykk/ansikts-ID. Så selv om noen fysisk får tilgang til den ulåste telefonen din, vil de ikke kunne åpne Proton Authenticator.





- **Ingen datainnsamling eller sporere**: Proton har forpliktet seg til å ikke samle inn personopplysninger via applikasjonen. Det er ingen skjult reklame eller atferdsanalyse.





- **Enkel import/eksport**: En av Proton Authenticators sterke sider er importveiviseren for eksisterende kontoer, som er kompatibel med andre applikasjoner (Google Authenticator, Authy, Aegis osv.). Du kan også eksportere kodene dine til en fil om nødvendig.



Kort sagt har Proton Authenticator som mål å være en kompromissløs 2FA-løsning: sikker, privat og fleksibel.



## Installasjon



Proton Authenticator er tilgjengelig gratis på alle plattformer. For å laste ned applikasjonen, gå til den offisielle siden: [https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)



![PROTON AUTHENTICATOR](assets/fr/01.webp)



*Offisiell Proton Authenticator-side som viser programmets hovedfunksjoner og Interface*



På denne siden finner du nedlastingslenker for alle operativsystemer: Android, iOS, Windows, macOS og Linux. Bare klikk på det operativsystemet du ønsker, og følg standard installasjonstrinn.



I denne veiledningen viser vi deg hvordan du installerer og konfigurerer den på macOS, og deretter ser vi på hvordan du installerer appen på iOS og synkroniserer kodene dine mellom de to enhetene.



### Installasjon på macOS



Når du har lastet ned og installert programmet, starter du Proton Authenticator. Ved første gangs oppstart veileder programmet deg gjennom noen innledende konfigurasjonsskjermbilder:



![PROTON AUTHENTICATOR](assets/fr/02.webp)



*Proton Authenticators velkomstskjerm med meldingen "Sikkerhet i hver kode" og "Kom i gang"*-knappen



### Første import



Hvis Proton Authenticator oppdager at du tidligere har brukt et annet 2FA-program, kan en importveiviser vises. Den støtter direkte import fra visse applikasjoner (Google Authenticator, 2FAS, Authy, Aegis osv.). Alternativt kan du hoppe over dette trinnet og legge til kontoene dine manuelt senere.



![PROTON AUTHENTICATOR](assets/fr/03.webp)



*Importveiviser for overføring av koder fra andre autentiseringsprogrammer*



![PROTON AUTHENTICATOR](assets/fr/04.webp)



*Kompatible importprogrammer: 2FAS, Aegis Authenticator, Authy, Bitwarden Authenticator, Ente Auth og Google Authenticator*



### Beskyttelse av lokale applikasjoner



Angi en PIN-kode for opplåsing, eller aktiver biometrisk opplåsing (Touch ID) hvis tilgjengelig. Dette trinnet er avgjørende for å forhindre at noen som bruker Mac-en din, får fri tilgang til 2FA-kodene dine.



![PROTON AUTHENTICATOR](assets/fr/05.webp)



*Touch ID-konfigurasjonsskjerm med meldingen "Beskytt dataene dine" og knappen "Aktiver Touch ID"*



### Synkroniseringsalternativer



Programmet lar deg også aktivere iCloud-synkronisering for å sikkerhetskopiere dataene dine sikkert mellom Apple-enhetene dine.



![PROTON AUTHENTICATOR](assets/fr/06.webp)



*ICloud-synkroniseringsalternativ med meldingen "Sikkerhetskopier dataene dine sikkert med kryptert iCloud-synkronisering"*



Når disse trinnene er fullført, er Proton Authenticator klar til bruk.



![PROTON AUTHENTICATOR](assets/fr/07.webp)



*Interface hovedtomt Proton Authenticator med alternativene "Opprett en ny kode" og "Importer koder"*



## Legg til en 2FA-konto med ProtonMail



Vi skal nå se på hvordan du legger til din første 2FA-kode, med ProtonMail som eksempel. Denne metoden fungerer på samme måte for alle tjenester som støtter tofaktorautentisering.



### Aktiver 2FA på ProtonMail



Først og fremst kan du lese vår guide til ProtonMail for mer informasjon:



https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

Logg inn på ProtonMail-kontoen din og gå til sikkerhetsinnstillingene. Se etter alternativet "Tofaktorautentisering" og aktiver det.



![PROTON AUTHENTICATOR](assets/fr/08.webp)



*ProtonMail-innstillingssiden med alternativet "Authenticator app" i delen "To-faktor autentisering"*



Klikk på knappen for å aktivere autentiseringsenheten, og ProtonMail vil be deg om å velge et autentiseringsprogram.



![PROTON AUTHENTICATOR](assets/fr/09.webp)



*ProtonMail 2FA-konfigurasjonsvindu med knappene "Avbryt" og "Neste"*



ProtonMail viser deretter en QR-kode som du kan skanne med autentiseringsprogrammet ditt.



![PROTON AUTHENTICATOR](assets/fr/10.webp)



*ProtonMail QR-kode til skanning med autentiseringsprogrammet ditt, med alternativet "Skriv inn nøkkel manuelt i stedet" tilgjengelig*



Hvis du foretrekker å skrive inn nøkkelen manuelt, kan du klikke på "Skriv inn nøkkel manuelt i stedet" for å se den hemmelige nøkkelen.



![PROTON AUTHENTICATOR](assets/fr/11.webp)



*Manuell inntasting av 2FA-informasjon: Nøkkel, intervall (30) og sifre (6)*



### Skann QR-koden med Proton Authenticator



I Proton Authenticator på macOS klikker du på "Opprett en ny kode". Programmet tilbyr deg flere alternativer: **Skann en QR-kode** eller **Skriv inn nøkkelen manuelt**.



Bruk kameraet på Mac-en til å skanne QR-koden som vises på ProtonMail-skjermen. Når du har skannet QR-koden, kommer du til skjermbildet for konfigurering av den nye koden.



![PROTON AUTHENTICATOR](assets/fr/12.webp)



*Nytt vindu for oppretting av oppføring med felt for tittel (ProtonMail), hemmelighet, avsender (Proton), sifferparametere og intervall*



Proton Authenticator fyller automatisk ut informasjonen. Du kan tilpasse navnet hvis du ønsker det, og deretter klikker du på "Lagre".



![PROTON AUTHENTICATOR](assets/fr/13.webp)



*TOTP-kode generert for ProtonMail (848 812) med visning av gjenværende tid*



### Valider konfigurasjonen



ProtonMail vil be deg om å oppgi en 6-sifret kode generert av Proton Authenticator for å bekrefte at 2FA fungerer som den skal.



![PROTON AUTHENTICATOR](assets/fr/14.webp)



*Valideringsskjermbildet for ProtonMail ber deg om å oppgi den 6-sifrede koden (848812)*



Kopier koden fra applikasjonen (ved å klikke på den) og lim den inn i ProtonMail for å fullføre aktiveringen.



Når du har validert, vil ProtonMail be deg om å laste ned gjenopprettingskodene dine. Det er viktig å lagre dem nøye.



![PROTON AUTHENTICATOR](assets/fr/15.webp)



*ProtonMail-gjenopprettingskoder-skjermbilde med liste over redningskoder og "Last ned"*-knappen



### Nødkoder



Når du legger til en konto, bør du ta vare på gjenopprettingskodene du får fra tjenesten. De fleste nettsteder tilbyr statiske engangskoder som du kan lagre på et trygt sted. Oppbevar disse sikkerhetskopikodene utenfor Proton Authenticator, slik at du kan få tilgang til kontoen din hvis du mister tilgangen til 2FA-programmet.



## IOS-installasjon og kodeimport



Nå som du har konfigurert Proton Authenticator på macOS, vil du kanskje også bruke det på iPhone eller iPad. Slik får du 2FA-kodene dine på flere enheter.



### Last ned applikasjonen på iOS



Gå til App Store og søk etter "Proton Authenticator". Last ned og installer applikasjonen på iOS-enheten din.



![PROTON AUTHENTICATOR](assets/fr/16.webp)



*Installasjonsprosess på iOS: velkomstskjerm, importveiviser, valg av kompatible applikasjoner og endelig "Importer koder fra Proton Authenticator"*-skjerm



### Metode 1: Eksporter/importer via JSON-fil



Hvis du ikke bruker automatisk synkronisering (iCloud eller Proton-konto), må du overføre kodene dine manuelt fra Mac-en til iPhone:



**Trinn 1 - Eksporter fra macOS** :



Åpne Proton Authenticator på Mac-en din og gå til Innstillinger (tannhjulikonet). I menyen klikker du på "Eksporter".



![PROTON AUTHENTICATOR](assets/fr/17.webp)



*Proton Authenticator-innstillingsmenyen på macOS med alternativet "Export" synlig*



![PROTON AUTHENTICATOR](assets/fr/18.webp)



*Eksportvindu med filnavnet "Proton_Authenticator_backup_2025" og "Lagre"*-knappen



Lagre JSON-filen på Mac-en. Du kan sende den via sikker e-post eller lagre den i iCloud Drive, slik at du får tilgang til den fra iPhone.



**Trinn 2 - Importer på iOS** :



Installer Proton Authenticator på iPhone, og velg å importere koder under konfigurasjonen. Velg "Proton Authenticator" fra listen og importer JSON-filen.



![PROTON AUTHENTICATOR](assets/fr/19.webp)



*Importprosess på iOS: JSON-fillokalisering, importbekreftelse og konfigurasjonsskjermbilder med Face ID- og iCloud-alternativer*



### Metode 2: Automatisk synkronisering



**Via Proton-konto (for synkronisering på flere plattformer)** :



Hvis du ennå ikke har opprettet en Proton-konto og ønsker å synkronisere mellom ulike operativsystemer, vil programmet be deg om å opprette eller koble til en Proton-konto.



![PROTON AUTHENTICATOR](assets/fr/20.webp)



*Skjermbildet for enhetssynkronisering ber deg om å opprette en gratis Proton-konto eller koble deg til en eksisterende konto*



**Via iCloud (kun for Apples økosystem)** :


Hvis du bare bruker Apple-enheter, kan du velge iCloud-synkronisering i programinnstillingene. Denne metoden vil automatisk og sikkert synkronisere kodene dine mellom alle Apple-enhetene dine, uten at du trenger en Proton-konto.



## Kryptert sikkerhetskopiering og gjenoppretting



En av nøkkelfunksjonene i Proton Authenticator er ende-til-ende-sikkerhetskopiering av 2FA-koder, noe som sikrer at tap eller bytte av enhet ikke betyr at du må begynne helt på nytt igjen.



### Ende-til-ende-kryptering



Når det gjelder kryptert sikkerhetskopiering i skyen med Proton Authenticator, krypteres TOTP-hemmelighetene dine lokalt på enheten din før de sendes til Proton-serveren. Dekryptering er bare mulig av deg, på enhetene dine som er koblet til Proton-kontoen din. Proton AG har ikke nøkkelen til å lese de registrerte kodene dine.



Hvis du velger iCloud i stedet for Proton-kontoen på iOS, krypteres dataene dine i henhold til Apple-standarder. Med lokal sikkerhetskopiering på Android kan du kryptere sikkerhetskopifilen med et passord du selv velger.



### Gjenoppretting i tilfelle tap



Hvis telefonen din blir borte, stjålet eller du bytter håndsett :



**Med Proton-sikkerhetskopiering aktivert**: Installer Proton Authenticator på den nye enheten. Under det første oppsettet logger du inn på den samme Proton-kontoen. Programmet vil umiddelbart synkronisere og laste ned alle 2FA-kodene dine fra den krypterte sikkerhetskopien.



**Med iCloud-sikkerhetskopiering (iOS)**: Koble den nye iPhone/iPad til med samme Apple-ID og sørg for å aktivere iCloud nøkkelring. Etter at du har installert Proton Authenticator, kobler du til iCloud. Kodene dine skal synkroniseres via iCloud og vises.



**Ingen sikkerhetskopiering i skyen**: Du må importere kontoene dine manuelt. Hvis du har eksportert en sikkerhetskopifil, kan du bruke importfunksjonen i Proton Authenticator. I verste fall, hvis du ikke hadde noen sikkerhetskopi, må du bruke sikkerhetskopikodene for hver tjeneste, eller kontakte kundestøtte.



Med Proton Authenticator kan du når som helst eksportere kontoene dine, enten som en kryptert fil eller som en QR-kode med flere kontoer. Disse alternativene gir deg ekstra trygghet.



## Beste praksis



Bruk av en 2FA-autentisering øker sikkerheten din betraktelig, men du må følge visse retningslinjer:



### Lagre nødkodene dine



Når du aktiverer 2FA på en tjeneste, får du ofte en liste med gjenopprettingskoder. Oppbevar dem utenfor telefonen (på papir, i en kryptert passordbehandler osv.). Disse statiske kodene vil redde deg i tilfelle du mister autentiseringsenheten din.



### Ikke bland sammen passord og 2FA-koder



Det er fristende å bruke en passordbehandler som også lagrer TOTP-er. Å oppbevare passordet og 2FA-koden på samme sted skaper imidlertid et enkelt feilpunkt og svekker den doble autentiseringen. For maksimal sikkerhet anbefaler mange eksperter å skille de to faktorene: passord i en sikker passordbehandler og 2FA-koder i en separat applikasjon, for eksempel Proton Authenticator. Det er likevel bedre å bruke en integrert manager enn å ikke ha 2FA i det hele tatt.



### Aktiver flere 2FA-metoder



Ideelt sett bør du bruke mer enn én sekundær faktor på kritiske kontoer. Ikke nøl med å legge til en fysisk sikkerhetsnøkkel hvis tjenesten tillater det. Se veiledningen vår om fysiske Yubikey-nøkler for mer informasjon:



https://planb.academy/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Ha også trykte nødkoder tilgjengelig.



### Vær diskret og beskytt enheten din



Ikke la noen søke i den ulåste telefonen din. Med Proton Authenticator er kodene dine beskyttet av PIN-kode/biometri - ikke avslør denne PIN-koden. Vær også på vakt mot phishing: Selv med 2FA kan en angriper bruke koden din i sanntid hvis du oppgir den til et falskt nettsted.



### Oppdateringer og revisjoner



Hold Proton Authenticator oppdatert (oppdateringer korrigerer mulige feil). Siden koden er åpen, utfører fellesskapet uformelle revisjoner, og Proton publiserer resultatene av formelle revisjoner.



## Sammenligning med andre applikasjoner



Hvordan står Proton Authenticator seg i forhold til andre autentiseringsprogrammer? Her er en sammenlignende oppsummering:



**Proton Authenticator**: Åpen kildekode, valgfri E2EE-kryptert sikkerhetskopiering i skyen, synkronisering av flere enheter, lokal låsing, ingen sporing, tilgjengelig på mobil og PC.



**Google Authenticator**: Proprietær, sikkerhetskopiering via Google-konto siden 2023, men uten ende-til-ende-kryptering (nøkler kan sees av Google), synkronisering av flere enheter lagt til i 2023, ingen applikasjonslås som standard, inneholder Google-sporere.



**Aegis Authenticator**: Åpen kildekode, kun lokal sikkerhetskopiering, ingen synkronisering i skyen, kode/biometrisk lås, ingen sporing, kun Android.



**Authy**: Egenutviklet, passordkryptert sikkerhetskopiering i skyen, men lukket kode, synkronisering av flere enheter, PIN-lås/fingeravtrykk, samler inn telefonnummer, skrivebordsapplikasjon avviklet i mars 2024.



Du finner vår guide til Authy nedenfor:



https://planb.academy/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Proton Authenticator er en av de mest omfattende og sikre løsningene som finnes: åpen kildekode, kryptert synkronisering på flere enheter, ingen kommersiell oppfølging.



## Ressurser og støtte



### Offisiell dokumentasjon




- **Offisiell nettside**: [proton.me/authenticator](https://proton.me/authenticator) - Produktpresentasjon og nedlastinger
- **Nedlastingsside**: [proton.me/en/authenticator/download](https://proton.me/fr/authenticator/download) - Lenker for alle operativsystemer
- **Proton support**: [proton.me/support/two-factor-authentication-2fa](https://proton.me/support/two-factor-authentication-2fa) - Offisiell 2FA-aktiveringsveiledning
- **Proton-blogg**: [proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - Kunngjøring og detaljerte funksjoner



### Kildekode og åpenhet




- **GitHub Proton Authenticator**: [github.com/ProtonMail/proton-authenticator](https://github.com/ProtonMail/proton-authenticator) - åpen kildekode
- **Sikkerhetsrevisjoner**: [proton.me/community/security-audits](https://proton.me/community/security-audits) - Uavhengige revisjonsrapporter



### Anbefalte sikkerhetstester


Test oppsettet etter at du har konfigurert det:




- [Have I Been Pwned] (https://haveibeenpwned.com/) - Sjekk om kontoene dine har blitt kompromittert
- [2FA Directory](https://2fa.directory/) - Liste over tjenester som støtter 2FA



### Fellesskap og diskusjoner




- Reddit r/Proton: [reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - Det offisielle Proton-fellesskapet
- Forum for personvernguider: [discuss.privacyguides.net](https://discuss.privacyguides.net) - Tekniske diskusjoner om personvernspørsmål
- **Reddit r/privacy**: [reddit.com/r/privacy](https://reddit.com/r/privacy) - Generelle tips om personvern



### Annet




- [Have I Been Pwned] (https://haveibeenpwned.com/) - Sjekk om kontoene dine har blitt kompromittert
- [2FA Directory](https://2fa.directory/) - Liste over tjenester som støtter 2FA