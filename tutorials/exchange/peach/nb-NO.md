---
name: Fersken
description: Komplett guide til bruk av Peach og veksling av bitcoins P2P
---
![cover](assets/cover.webp)

![peach](https://youtu.be/ziwhv9KqVkM)

## Innledning

KYC-frie peer-to-peer-børser (P2P) er avgjørende for å bevare brukernes konfidensialitet og økonomiske uavhengighet. De muliggjør direkte transaksjoner mellom enkeltpersoner uten behov for identitetsbekreftelse, noe som er avgjørende for de som verdsetter personvern. For en mer inngående forståelse av de teoretiske konseptene, ta en titt på BTC204-kurset:

https://planb.network/courses/btc204
### 1. Hva er fersken?

Peach er en P2P-utvekslingsplattform som lar brukerne kjøpe og selge bitcoins uten KYC. Den tilbyr et intuitivt grensesnitt og avanserte sikkerhetsfunksjoner. Sammenlignet med andre løsninger som Bisq, HodlHodl og Robosat, skiller Peach seg ut for sin brukervennlighet og lave gebyrer.

### 2. Personvern og datainnsamling

**Hvilken informasjon samler Peach inn?

Peach bestreber seg på å lagre et absolutt minimum av data om brukerne. Her er en oversikt over dataene som lagres på serverne:


- En hash av din unike applikasjonsidentifikator (AdID)
- En hash av betalingsopplysningene dine
- Dine krypterte samtaler
- Transaksjonsdata for å sikre at anonyme brukere ikke overskrider handelsgrensen (typer betalingsmetoder som brukes, kjøps- og salgsbeløp)
- Adresser som brukes til å sende og motta fra sperret konto
- Bruksdata (Firebase og Google Analytics), kun med ditt samtykke

En hash er data som er gjort ugjenkjennelige, på samme måte som kryptering. De samme dataene vil alltid produsere den samme hashen, noe som gjør det mulig å oppdage duplikater uten å kjenne originaldataene.

*For mer informasjon om hashing, kan du følge dette kurset:*

https://planb.network/courses/cyp201
**Hvem kan se betalingsopplysningene mine?


- Bare motparten din kan se betalingsopplysningene dine
- Data overføres via Peach-servere, men er fullstendig kryptert fra ende til ende
- Ved en eventuell tvist vil betalingsopplysningene og samtalehistorikken din være synlig for den tildelte Peach-mekleren

## Installasjon og konfigurasjon

### 1. Installer Peach-applikasjonen

![Installation de Peach](assets/fr/01.webp)


- Last ned applikasjonen fra [Peach Bitcoin] (https://peachbitcoin.com/fr/quick-start/).
- Følg installasjonsinstruksjonene på enheten din.
- Under installasjonen blir du bedt om å velge om du ønsker å dele visse data for å forbedre Peach-applikasjonen (bilde 1)
- På det neste skjermbildet (bilde 2) har du to alternativer:
 - Hvis du er en ny bruker, klikker du på "Ny bruker" for å opprette en ny profil
 - Hvis du allerede har en konto, kan du bruke "Gjenopprett" for å gjenopprette din eksisterende profil
- Hvis du har en henvisningskode, kan du oppgi den her.
- For å gjenopprette en eksisterende konto (bilde 3), trenger du :
 - Sikkerhetskopifilen din
 - Passordet for å dekryptere denne filen

### 2. Oversikt over hovedskjermbildene

Peach-applikasjonen er organisert rundt fire hovedskjermbilder som er tilgjengelige fra den nederste navigasjonslinjen:

![Navigation dans l'application](assets/fr/02.webp)


- Hjem** : Hovedskjermen for kjøp og salg av bitcoins. Det er her du kan opprette nye transaksjoner og få tilgang til tilgjengelige tilbud.
- Lommebok**: Din integrerte bitcoin-lommebok som lar deg :
 - Sjekk saldoen din
 - Motta bitcoins
 - Send bitcoins
 - Se transaksjonshistorikken din
- Handler** : Ditt senter for handelsadministrasjon hvor du finner :
 - Dine nåværende transaksjoner
 - En komplett historikk over utvekslingene dine
 - Status for hver transaksjon
- Innstillinger** : Din kontokonfigurasjonshub for :
 - Administrer betalingsmåtene dine
 - Konfigurer sikkerhetskopiene dine
 - Tilpass preferansene dine
 - Tilgang til hjelp og støtte

### 3. Konfigurer betalingsmåtene dine

![Accès aux paramètres de paiement](assets/fr/03.webp)

Få tilgang til betalingsmåter via fanen Innstillinger (bilde 8)

**Online-betalinger

![Configuration des paiements en ligne](assets/fr/04.webp)


- Klikk på knappen for å legge til en ny betalingsmåte
- Velg valuta
- Velg ønsket betalingsmåte

*Betalingsmåter som er tilgjengelige:*

***Bankoverføringer er tilgjengelige: ***


- SEPA (standard eller øyeblikkelig)
- Fyll inn SEPA-bankopplysningene dine

***Online lommebøker akseptert :***


- Flere alternativer er tilgjengelige avhengig av hvilket land du bor i (Revolut, Paypal, Wise, Strike osv.)
- Følg instruksjonene for å legge til påloggingsinformasjonen din

***Gavekortet som kan brukes :***


- Amazonas
- Angi kortets utstedelsesland og annen nødvendig informasjon

***Nasjonale betalingsalternativer:***

Landspesifikke betalingssystemer :


- Satispay (Italia)
- MB Way (Portugal)
- Bizum (Spania)
- Raskere betalinger (Storbritannia)

***Personlige betalinger:***

![Configuration des paiements en personne](assets/fr/05.webp)


- Velg "Meetup
- Velg deretter møtet ditt fra listen

### Bruksanvisning


- Du kan sette opp flere betalingsmetoder samtidig
- Jo flere metoder du legger til, desto flere tilbud får du tilgang til
- Vennligst sjekk at informasjonen er korrekt før du registrerer deg
- Du kan når som helst endre eller slette betalingsmåtene dine

**Sikkerhetsnotat**: Betalingsinformasjonen din er kryptert og deles kun med vekslingspartneren din under en transaksjon.

### 4. Slik sikrer du porteføljen din

**Forståelse av Peach-kontoen din

En Peach-konto er ikke en tradisjonell konto med innlogging og passord. Det er en fil som er lagret lokalt på telefonen din, noe som betyr at Peach ikke trenger å lagre dataene dine eller kjenne identiteten din: Du har kontrollen. Denne filen inneholder alle dataene dine, fra bitcoin-lommeboknøklene til betalingsinformasjonen din.

Denne tilnærmingen garanterer større konfidensialitet, men innebærer også et større ansvar. Hvis du mister telefonen uten sikkerhetskopi, mister du tilgangen til Peach-kontoen og pengene dine. Det er derfor viktig å ta sikkerhetskopi av denne filen og beskytte den med et sterkt passord.

**Opprett sikkerhetskopiene dine**

![Accéder aux sauvegardes](assets/fr/13.webp)


- Åpne innstillinger fra fanen nederst til høyre på startskjermen
- Velg alternativet "sikkerhetskopier" i innstillingsmenyen

![Processus de sauvegarde](assets/fr/06.webp)

To typer sikkerhetskopiering er tilgjengelig:

**Lagre kontofilen (bilde 14)**


- Klikk på "Opprett ny sikkerhetskopi"
- Opprett et sterkt passord for å kryptere sikkerhetskopifilen
- Oppbevar denne filen på et trygt sted

Filsikkerhetskopien gjenoppretter hele Peach-kontoen din, inkludert :


- Din portefølje
- Betalingsmåtene dine
- Samtalehistorikk
- Betalingsdata
- Transaksjonshistorikk med motpartsopplysninger

**Lagring av gjenopprettingsfrasen (bilde 15)**


- Følg instruksjonene for å vise gjenopprettingsfrasen din
- Skriv ordene nøye ned i riktig rekkefølge
- Lagre denne sikkerhetskopien på et sikkert sted, helst et annet sted enn kontofilen

Gjenopprettingsfrasen gjenoppretter bare :


- Tilgang til kontoen din
- Dine bitcoin-midler

Du vil tape:


- Samtalehistorikk
- Betalingsdata
- Motpartsinformasjon i transaksjonshistorikken

For optimal sikkerhet anbefaler vi at du utfører begge typer sikkerhetskopiering.

## Kjøp og salg av Bitcoins

### 1. Hvordan kjøpe Bitcoins

![Création et vue des offres](assets/fr/07.webp)


- Klikk på "Kjøp"-knappen på startskjermen (bilde 16)
- Konfigurer kjøpet ditt i henhold til dine preferanser (bilde 17)
- Bla gjennom listen over tilgjengelige tilbud (bilde 18)

![Sélection et confirmation d'achat](assets/fr/08.webp)


- Velg det tilbudet som passer best for deg (bilde 19)
- Foreta betaling på avtalt måte
- Bekreft betalingen i applikasjonen og evaluer transaksjonen (bilde 20)

![Réception des bitcoins](assets/fr/09.webp)


- Følg med på statusen til transaksjonen din
- Sjekk bekreftelse på mottak av bitcoins
- Midlene vil være tilgjengelige i Peach-porteføljen din

### 2. Hvordan selge Bitcoins

![Création d'un ordre de vente](assets/fr/10.webp)


- Konfigurer salgstilbudet ditt (bilde 24)
- Finansier transaksjonen ved å sende bitcoins til den oppgitte adressen (bilde 25)
- Vent på bekreftelse av transaksjonen (bilde 26)
- Tilbudet ditt er nå synlig for kjøpere (bilde 27)

![Attente du paiement](assets/fr/11.webp)


- Overvåk status for tilbudet ditt
- Vent på betalingsbekreftelse fra kjøperen
- Sjekk transaksjonsdetaljer

![Finalisation de la vente](assets/fr/12.webp)


- Sjekk betalingsstatus
- Bekreft mottak av betaling
- Evaluer transaksjonen
- Bitcoins frigjøres automatisk til kjøperen

**Tips for en vellykket transaksjon**


- Svar raskt på meldinger fra motparten din
- Sjekk betalingsopplysningene nøye
- Ikke nøl med å bruke meklingstjenesten hvis du har et problem

**Sikkerhetsmerknad**: Bekreft aldri mottak av en betaling før du har bekreftet at den er mottatt på kontoen din.

## Fordeler og ulemper

### Fordeler med fersken


- Ingen KYC kreves**: Bevarer brukernes konfidensialitet.
- Ingen tilgang til bankopplysninger**: Peach har ikke tilgang til bankopplysningene dine eller identiteten din.
- Intuitivt grensesnitt**: Enkelt å bruke for viderekomne brukere.
- Åpen kildekode** : Kildekoden er offentlig og kan verifiseres av fellesskapet.

### Ulemper med fersken


- Begrenset likviditet**: Mindre handelsvolum enn på mer etablerte plattformer.
- Regulatorisk risiko** : Applikasjonen administreres av et sveitsisk selskap. Den er derfor underlagt sveitsisk regelverk, som kan utvikle seg og potensielt sensurere applikasjonen.

## Nyttige ressurser


- Fransk forklaringsvideo: [YouTube] (https://youtu.be/ziwhv9KqVkM)
- Hurtigstartveiledning: [Peach Bitcoin] (https://peachbitcoin.com/fr/quick-start/)