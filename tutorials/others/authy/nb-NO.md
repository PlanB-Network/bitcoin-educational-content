---
name: AUTHY 2FA
description: Hvordan bruke en 2FA-applikasjon?
---
![cover](assets/cover.webp)

I dag har tofaktorautentisering (2FA) blitt essensielt for å forbedre sikkerheten til online kontoer mot uautorisert tilgang. Med økningen i cyberangrep, er det noen ganger ikke tilstrekkelig å kun stole på et passord for å sikre kontoene dine. 2FA introduserer et ekstra sikkerhetslag ved å kreve en sekundær form for autentisering i tillegg til passordet. Denne verifiseringen kan ta flere former, som en kode sendt via SMS, en dynamisk kode generert av en dedikert app, eller bruk av en fysisk sikkerhetsnøkkel. Bruken av 2FA reduserer sterkt risikoen for at kontoene dine blir kompromittert, selv i tilfelle passordet ditt blir stjålet.

## 2FA via Autentiseringsapper

Vi vil utforske andre løsninger som fysiske sikkerhetsnøkler i andre veiledninger, men i denne ønsker jeg spesifikt å diskutere 2FA-applikasjoner. Driften av disse applikasjonene er ganske enkel: når 2FA er aktivert på en konto, vil du ved hvert innlogging bli bedt om ikke bare ditt vanlige passord, men også en 6-sifret kode. Denne koden genereres av din 2FA-applikasjon. En viktig egenskap ved denne 6-sifrede koden er at den ikke er statisk; en ny kode genereres av applikasjonen hvert 30. sekund.
![AUTHY 2FA](assets/notext/01.webp)
Fornyelsen av koden hvert 30. sekund gjør det veldig vanskelig for en angriper å få tilgang til kontoen din. Dette systemet forhindrer angripere fra å gjenbruke en stjålet eller avlyttet kode, ettersom den utløper raskt. Så selv om en angriper klarer å skaffe koden, vil de bare kunne bruke den i et veldig kort tidsvindu før en ny kode kreves. Dessuten reduserer det faktum at koden endres så hyppig betydelig tiden tilgjengelig for en hacker som forsøker å gjette koden gjennom brute force.

2FA via autentiseringsapper representerer dermed en enkel-å-bruke og gratis metode for å betydelig forbedre sikkerheten til dine online kontoer.

Det finnes mange applikasjoner for å sette opp 2FA, blant hvilke Google Authenticator og Microsoft Authenticator er de mest kjente. Men i denne veiledningen ønsker jeg å introdusere deg for en annen, mindre kjent løsning kalt Authy. Alle disse applikasjonene opererer ved bruk av samme TOTP (*Time based One Time Password*) protokoll, noe som gjør deres bruk ganske lik.
Authy tilbyr flere fordeler over andre løsninger fra de store teknologiselskapene. Først og fremst, tillater det deg å synkronisere dine 2FA-token på tvers av flere enheter, noe som kan være nyttig i tilfelle tap eller bytte av telefon. Authy gjør det også mulig for deg å generere en kryptert sikkerhetskopi og lagre den online, noe som sikrer at du aldri mister tilgangen til dine token, selv om du mister din primærenhet. Fra et brukergrensesnittperspektiv, finner jeg personlig at Authy også tilbyr en mer behagelig og intuitiv opplevelse enn sine alternativer.

## Hvordan installere Authy?

På smarttelefonen din, gå til appbutikken (Google Play Store eller Apple Store), og søk etter "*Twilio Authy Authenticator*".

- [Apple](https://apps.apple.com/us/app/twilio-authy/id494168017)
- [Android](https://play.google.com/store/apps/details?id=com.authy.authy)
![AUTHY 2FA](assets/notext/02.webp)
Ved første oppstart av appen, vil du trenge å opprette en konto. Velg landskoden din, samt ditt telefonnummer, og klikk på "*Submit*".
![AUTHY 2FA](assets/notext/03.webp)
Skriv inn din e-postadresse for kodegjenoppretting.
![AUTHY 2FA](assets/notext/04.webp)En e-post vil bli sendt til deg for å verifisere adressen din. Skriv inn de 6 sifrene du mottar for å bekrefte.
![AUTHY 2FA](assets/notext/05.webp)
Velg en av de to tilgjengelige metodene for å verifisere telefonnummeret ditt. Hvis du velger å motta en SMS, skriv inn den 6-sifrede koden du mottar via melding for å bekrefte nummeret ditt.
![AUTHY 2FA](assets/notext/06.webp)
Gratulerer, din Authy-konto har blitt opprettet!
![AUTHY 2FA](assets/notext/07.webp)
## Hvordan konfigurere Authy?

For å starte, gå til appens innstillinger ved å klikke på de tre små prikkene som er plassert øverst til høyre på skjermen.
![AUTHY 2FA](assets/notext/08.webp)
Deretter klikker du på "*Innstillinger*".
![AUTHY 2FA](assets/notext/09.webp)
I fanen "*Min Konto*", har du muligheten til å endre kontoen din. Jeg anbefaler å legge til en PIN-kode til appen ved å velge "*Appbeskyttelse*". Dette legger til et ekstra lag med sikkerhet for å få tilgang til applikasjonen din.
![AUTHY 2FA](assets/notext/10.webp)
I fanen "*Kontoer*", kan du sette opp en sikkerhetskopi for dine tokens. Denne sikkerhetskopien tillater gjenoppretting av kodene dine i tilfelle et problem. Den er kryptert ved hjelp av et passord som du må definere. Det er viktig at dette passordet er sterkt og oppbevares på et sikkert sted. Å sette opp denne sikkerhetskopien er ikke nødvendigvis obligatorisk hvis du har andre gjenopprettingsmetoder, som for eksempel et annet apparat med samme Authy-konto.
![AUTHY 2FA](assets/notext/11.webp)I fanen "*Enheter*", kan du se alle enhetene synkronisert med din Authy-konto. Du har muligheten til å deaktivere bruken av flere enheter, som begrenser tilgangen til kontoen din til den enheten alene. Hvis du kun bruker én enhet, kan dette øke sikkerheten til kontoen din, men sørg for at du har en annen gjenopprettingsmetode i tilfelle du mister den enheten.

Hvis du foretrekker å tillate tillegg av andre enheter, råder jeg deg til å aktivere alternativet som krever bekreftelse fra de for øyeblikket autoriserte enhetene på din Authy-konto før du legger til en ny enhet.
![AUTHY 2FA](assets/notext/12.webp)
For å legge til en ny enhet, gjenta ganske enkelt installasjonsprosessen presentert i den forrige delen ved å bruke de samme legitimasjonene. Du vil da bli bedt om å bekrefte denne nye tilgangen fra din hovedenhet.

## Hvordan sette opp 2FA på en konto?

For å sette opp en 2FA-autentiseringskode via en app som Authy på en konto, må kontoen støtte denne funksjonen. I dag tilbyr flertallet av nettjenester denne 2FA-alternativet, men dette er ikke alltid tilfellet. La oss ta eksemplet med Proton mail-kontoen som jeg presenterte i en annen veiledning:

https://planb.network/tutorials/others/proton-mail
![AUTHY 2FA](assets/notext/13.webp)
Du vil generelt finne denne 2FA-alternativet i innstillingene til kontoen din, ofte under "*Passord*" eller "*Sikkerhet*" seksjonen.
![AUTHY 2FA](assets/notext/14.webp)
Når du aktiverer denne alternativet på din Proton mail-konto, blir en QR-kode presentert for deg. Du må da skanne denne QR-koden med din Authy-app.
![AUTHY 2FA](assets/notext/15.webp)
På Authy, klikk på "*+*" knappen.
![AUTHY 2FA](assets/notext/16.webp)
Klikk på "*Scan QR Code*". Skann deretter QR-koden på nettsiden. ![AUTHY 2FA](assets/notext/17.webp)
Du har også muligheten til å justere brukernavnet ditt om nødvendig. Etter å ha gjort endringer, klikk på "*LAGRE*" knappen.
![AUTHY 2FA](assets/notext/18.webp)
Authy vil deretter vise din dynamiske 6-sifrede kode spesifikk for den kontoen som oppdateres hvert 30. sekund.
![AUTHY 2FA](assets/notext/19.webp)
Skriv inn denne koden på nettsiden for å fullføre oppsettet av 2FA.
![AUTHY 2FA](assets/notext/20.webp)
Noen nettsteder vil også gi deg gjenopprettingskoder etter å ha aktivert 2FA. Disse kodene lar deg få tilgang til kontoen din hvis du mister tilgangen til Authy-appen din. Jeg anbefaler å lagre dem på et sikkert sted.
![AUTHY 2FA](assets/notext/21.webp)Kontoen din er nå sikret med tofaktorautentisering via Authy-appen.
![AUTHY 2FA](assets/notext/22.webp)
Hver gang du logger inn på kontoen, må du oppgi den dynamiske koden generert av Authy. Du kan nå sikre alle kontoene dine som er kompatible med denne 2FA-metoden. For å legge til en ny konto på Authy, klikk på de tre små prikkene øverst til høyre i appen.
![AUTHY 2FA](assets/notext/23.webp)
Klikk deretter på "*Legg til konto*".
![AUTHY 2FA](assets/notext/24.webp)
Følg de samme stegene som de som ble brukt for den første kontoen. Dine ulike dynamiske koder vil være synlige på Authy-hjemmesiden.