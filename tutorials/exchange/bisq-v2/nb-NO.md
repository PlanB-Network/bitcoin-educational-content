---
name: Bisq 2
description: Komplett guide til bruk av Bisq 2 og veksling av bitcoins P2P
---
![cover](assets/cover.webp)

## Innledning

KYC-frie peer-to-peer-børser (P2P) er avgjørende for å bevare brukernes konfidensialitet og økonomiske uavhengighet. De muliggjør direkte transaksjoner mellom enkeltpersoner uten behov for identitetsbekreftelse, noe som er avgjørende for de som verdsetter personvern. For en mer inngående forståelse av de teoretiske konseptene, ta en titt på BTC204-kurset:

https://planb.network/courses/btc204
### Hva er Bisq 2?

Bisq 2 er den nye versjonen av den populære desentraliserte Bisq-børsen, som ble lansert i 2024. I motsetning til forgjengeren er Bisq 2 utviklet for å støtte flere utvekslingsprotokoller, noe som gir brukerne større fleksibilitet.

**Viktige nye funksjoner:**


- Støtte for flere personvernnettverk (Tor, I2P)
- Flere identiteter for større konfidensialitet
- REST API for handelsroboter
- Støtte for flere porteføljetyper
- Rollesystem med obligatorisk innskudd i BSQ

Denne veiledningen fokuserer utelukkende på "Bisq Easy", den eneste protokollen som er tilgjengelig for øyeblikket. Bisq Easy er utviklet spesielt for nye Bitcoin-brukere. Denne protokollen gjør det mulig for brukere å kjøpe og selge Bitcoins mot fiat-valutaer på en desentralisert peer-to-peer-plattform. Transaksjonene er begrenset til tilsvarende 600 USD (med et minimum på 6 USD), og sikkerheten er avhengig av BTC-selgernes omdømme. Bisq Easy har ingen handelsgebyrer eller krav til depositum. Bisq Easy forventes å erstatte Bisq 1 for kontantbørser under 600 USD (eller tilsvarende).

**Hovedfunksjoner:**


- Skrivebordsapplikasjon på tvers av plattformer
- Flere tilgjengelige utvekslingsprotokoller
- Desentralisert P2P-nettverk
- Fokus på konfidensialitet (ingen KYC, bruk av Tor)
- Ikke-forvaring (du beholder kontrollen over midlene dine)
- Åpen kildekode (AGPL)

### Forskjeller med Bisq 1

**For kjøpere:**


- Ingen depositum kreves
- Ingen handelsavgifter
- Ingen gruveavgifter
- Sikkerhet basert på leverandørens omdømme
- Lavere handelsgrenser (tilsvarende USD 600)

**For selgere:**


- Ingen depositum kreves
- Å bygge et omdømme
- Mulighet for å brenne BSQ eller skape BSQ-obligasjoner
- Potensielt høyere salgspremie (10-15 % over markedet)

**Når Bisq Multisig-protokollen er implementert i Bisq 2, kan den gamle versjonen av Bisq fases ut. Bisq 1 vil imidlertid fortsatt bli brukt som administrasjonsverktøy for Bisq CAD og for BSQ-BTC-børser.

### Utvekslingsprosess


- Den som utarbeider tilbudet, definerer vilkårene for utvekslingen
- Når forhandlerne har blitt enige om vilkårene (betalingsmåte og pris), begynner utvekslingen
- Selgeren sender bankopplysningene sine til kjøperen, og kjøperen sender Bitcoin-adressen sin til selgeren
- Kjøperen betaler kontant og gir selgeren beskjed om dette
- Når betalingen er mottatt, sender selgeren bitcoinsene til kjøperens adresse
- Utvekslingen er fullført når kjøperen mottar bitcoinsene

### Viktige regler


- Før utveksling av betalingsinformasjon kan utvekslingen kanselleres uten begrunnelse
- Etter at detaljer er utvekslet, kan manglende oppfyllelse av forpliktelser føre til utestengelse
- Ved bankoverføringer må du **aldri bruke begrepene "Bisq" eller "Bitcoin"** i årsaken til betalingen (dette kan føre til at midlene fryses eller til og med at mottakerens eller betalerens bankkonto sperres)
- Tradere må logge seg på minst én gang om dagen for å følge prosessen
- Hvis det oppstår et problem, kan næringsdrivende benytte seg av en megler

## Installasjon og konfigurasjon

### 1. Last ned og verifiser Bisq 2

![Téléchargement de Bisq 2](assets/fr/01.webp)


- Gå til [bisq.network](https://bisq.network/downloads/)
- Last ned Bisq 2-versjonen som passer til operativsystemet ditt (bla nedover på siden)
- Bekreft ektheten til den nedlastede filen (anbefales på det sterkeste). Du finner en detaljert veiledning om signaturverifisering i følgende veiledning:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
### 2. Installasjon i henhold til ditt system

Følg installeringstrinnene som gjelder for ditt operativsystem. Hvis du støter på problemer under installasjonen, kan du se den detaljerte veiledningen på [official Bisq wiki] (https://bisq.wiki/Downloading_and_installing).

### 3. Første oppstart


- Start Bisq 2 og godta vilkårene for bruk

![Conditions d'utilisation](assets/fr/01.webp)


- Opprett en ny profil ved å velge et navn og en avatar

![Création du profil](assets/fr/02.webp)


- Du blir deretter ført til programmets hoveddashboard, hvor du kan starte Bisq Easy for å kjøpe eller selge dine første bitcoins

![Page d'accueil de Bisq 2](assets/fr/03.webp)

### 4. Sette opp betalingsmetoder


- Gå til betalingskontoene fra hovedmenyen

![Liste des comptes de paiement](assets/fr/04.webp)


- Legg til en ny betalingsmåte ved å fylle ut den nødvendige informasjonen

![Création d'un nouveau compte de paiement](assets/fr/05.webp)

Det er valgfritt å forhåndskonfigurere betalingsmåter, men det anbefales for å spare tid når du handler. Du kan også konfigurere betalingsmåtene dine direkte under en handel ved å kontakte vekslingspartneren din.

### 5. Kontosikkerhet

**Sikkerhetskopiering av data:**

I motsetning til Bisq 1 har Bisq 2 for øyeblikket ikke integrert en Bitcoin-lommebok: Transaksjoner utføres derfor via dine egne eksterne lommebøker. Vi anbefaler likevel at du regelmessig tar sikkerhetskopi av Bisq 2-datamappen din. For å finne datamappen din, se [offisiell Bisq-wiki] (https://bisq.wiki/Backing_up_application_data#Back_up_the_entire_Bisq_data_directory).

**Identitetsstyring:**

Bisq 2 lar deg opprette flere identiteter. Hver identitet kan brukes til ulike typer transaksjoner. Identitetene lagres i datamappen.

## Kjøp og salg av Bitcoins

### Hvordan kjøpe Bitcoins

**Alternativ 1: Benytt deg av et eksisterende tilbud**


- På hovedskjermen velger du "Bisq Easy", fanen "Komme i gang", og klikker deretter på "Start handelsveiviseren"

![Lancer trade wizard](assets/fr/06.webp)


- Velg "Kjøp Bitcoin" og velg valutaen din

![Sélection achat Bitcoin](assets/fr/07.webp)

![Choix de la devise](assets/fr/08.webp)


- Konfigurer dine foretrukne betalingsmetoder (SEPA, Revolut osv.)

![Configuration méthodes de paiement](assets/fr/09.webp)


- På dette tidspunktet har du enten en liste over tilbud som samsvarer med dine tidligere kriterier, eller du må gå til "Tilbudsboken"

![Liste des offres](assets/fr/10.webp)


- I det andre tilfellet kan du vise og filtrere tilbud ved hjelp av knappene øverst til høyre i grensesnittet

![Filtres des offres](assets/fr/11.webp)


- Når du har valgt tilbudet ditt, er alt du trenger å gjøre å velge betalingsmåte, og deretter validere handelsoversikten

![Choix modalités de paiement](assets/fr/12.webp)

![Configuration du trade](assets/fr/13.webp)

![Récapitulatif du trade](assets/fr/14.webp)

**Alternativ 2: Lag ditt eget tilbud**


- Velg "Bisq Easy" og deretter "Offerbook"
- Velg ditt handelspar (f.eks. BTC/EUR)
- Klikk på "Opprett tilbud
- Følg veiviseren for oppretting av tilbud: Definer beløpet (fast eller intervall)

![Configuration du montant](assets/fr/20.webp)


- Velg aksepterte betalingsmetoder

![Sélection méthodes de paiement](assets/fr/21.webp)


  - Sjekk sammendraget og publiser tilbudet

![Récapitulatif et publication](assets/fr/22.webp)

Når utvekslingen er igangsatt :


- Send Bitcoin-adressen din eller Lightning-fakturaen til selgeren

![Envoi adresse Bitcoin](assets/fr/15.webp)


- Motta selgerens bankopplysninger

![Réception coordonnées bancaires](assets/fr/16.webp)

![Détails coordonnées bancaires](assets/fr/17.webp)


- Foreta betalingen (uten å nevne "Bisq" eller "Bitcoin")
- Gi selgeren beskjed om betalingen din

![Notification paiement](assets/fr/18.webp)


- Vent på at bitcoinsene skal ankomme

![Attente réception](assets/fr/19.webp)

### Hvordan selge Bitcoins?

Salgsprosessen på Bisq 2 følger en lignende logikk som kjøpsprosessen, med de samme hovedtrinnene, men i omvendt rekkefølge. Du kan enten opprette ditt eget salgstilbud eller svare på et eksisterende kjøpstilbud. Her er en oversikt over de ulike alternativene og trinnene i prosessen:

**Alternativ 1: Opprett et tilbud om salg**


- Velg "Bisq Easy" og deretter "Offerbook"
- Klikk på "Opprett tilbud" og velg "Selg Bitcoin"
- Konfigurer tilbudet ditt :
 - Velg valuta (EUR, USD osv.)
 - Velg de aksepterte betalingsmetodene
 - Angi beløpet (mellom 6 og 600 USD)
 - Fastsett prisen (fast eller % av markedet)
- Sjekk detaljer og publiser tilbudet

**Alternativ 2: Benytt deg av et eksisterende tilbud**


- Bla gjennom tilbud i fanen "Tilbudsbok"
- Filtrer etter valuta og betalingsmåte
- Velg et tilbud som passer deg
- Sjekk detaljer og godta tilbudet

**Salgsprosess:**

Når utvekslingen er igangsatt :


   - Send bankopplysningene dine til kjøperen
   - Vent på kjøperens Bitcoin-adresse
   - Kontroller at adressen er gyldig

Etter betalingsvarsel :


   - Sjekk at betalingen er mottatt på kontoen din
   - Bekreft at beløp og detaljer stemmer overens
   - Send bitcoins til den oppgitte adressen
   - Merk transaksjonen som fullført

Ferdigstillelse :


   - Vent på bekreftelse fra kjøperen
   - Legg igjen tilbakemelding på transaksjonen
   - Bygg omdømmet ditt for fremtidig salg

**Viktig merknad:** Som selger må du være spesielt oppmerksom på risikoen for tilbakeføringer. Bruk helst sikre betalingsmetoder, og sjekk alltid at betalingen er mottatt før du sender bitcoins.

## God praksis og sikkerhet

### Sikkerhetstips

**For kjøpere:**


- Begynn med små mengder
- Sjekk selgernes omdømme (minimum 30 000 poeng)
- Bruk kun de foreslåtte betalingsmåtene
- Sjekk at selgeren er aktiv før du sender betaling
- Bruk kun bankopplysningene som oppgis i utvekslingschatten
- Kommuniser aldri utenfor Bisq 2-plattformen
- Oppbevar bevis på betaling
- Send aldri sensitiv informasjon

**For selgere:**


- Vær forsiktig med nye kontoer
- Unngå betalingsmetoder som er følsomme for tilbakebetalinger (PayPal, Venmo)
- Kontroller at kontoopplysningene stemmer overens med kjøperen
- Begrens kommunikasjonen til chat Bisq 2
- Åpne en mekling i tvilstilfeller

### Omdømmebygging (for selgere)

For å forbedre omdømmet ditt som selger på Bisq bør du gjennomføre regelmessige transaksjoner og opprettholde en profesjonell kommunikasjon med kjøperne. Svar raskt på forespørsler fra kjøpere for å sikre en positiv opplevelse. Du kan også opprette et BSQ-obligasjon for å vise din forpliktelse til plattformen. Disse handlingene vil bygge tillit og tiltrekke seg flere kjøpere.

### Tvisteløsning


- Kontakt motparten din via chat
- Om nødvendig, åpne en tvist
- Legge frem alle etterspurte bevis
- Følg meklerens instruksjoner

### Retningslinjer for personvern :


- Ingen registrering eller sentralisert identitetsbekreftelse kreves
- Alle tilkoblinger går gjennom Tor-nettverket (og snart I2P)
- Ingen sentral server for lagring av data
- Transaksjonsdetaljer kan bare leses av de involverte partene

### Beskyttelse mot sensur :


- Fullt distribuert P2P-nettverk
- Bruk Tor-nettverket (og snart I2P) til å motstå sensur
- Prosjekt med åpen kildekode administrert av en DAO, uten sentralisert juridisk enhet

## Fordeler og ulemper

### Fordeler med Bisq 2


- Maksimal konfidensialitet**: Ingen KYC, bruk av Tor
- Desentralisering**: Ingen sentral server
- Sikkerhet**: Åpen kildekode, ikke-frihetsberøvende kode
- Intuitivt grensesnitt**: enklere enn Bisq 1
- Fleksibilitet**: Flere utvekslingsprotokoller

### Ulemper med Bisq 2


- Begrenset likviditet** (for øyeblikket) :
 - Ny protokoll i oppstartsfasen
 - Få salgstilbud tilgjengelig
 - Potensielt lang ventetid på å finne en kjøper
- Handelsgrenser**: Maksimalt USD 600 per transaksjon (med Bisq easy)
- Kun for datamaskiner**: Ingen mobilapplikasjon

## Fremtidige protokoller

Selv om Bisq Easy for øyeblikket er den eneste tilgjengelige protokollen, er flere andre protokoller under utvikling for Bisq 2 :


- Bisq Lightning**: Utvekslingsprotokoll basert på et escrow-system som bruker flerpartskryptografi på Lightning-nettverket.
- Bisq MuSig**: Migrering av hovedprotokollen fra Bisq 1 til Bisq 2, ved hjelp av en 2-på-2 multisig med sikkerhetsdepositum.
- BSQ-bytter**: Øyeblikkelige atombytter mellom BSQ og BTC.
- Liquid Swaps**: Utveksling av eiendeler på Liquid-nettverket (USDT, BTC-L) via atombytter.
- Monero Swaps**: Atomutveksling mellom Bitcoin og Monero.
- Liquid MuSig**: En versjon av multisig-protokollen som bruker L-BTC for lavere kostnader og større konfidensialitet.
- Submarine bytter**: Utvekslinger mellom Bitcoin på Lightning-nettverket og Bitcoin på kjeden.
- Stablecoin-bytter**: Atomutveksling mellom Bitcoin og USD stablecoins.
- Multisig-opsjoner**: Opprettelse av P2P-salgs- og kjøpsopsjoner med BTC-blokkering i en multisig-transaksjon i kjeden.
- Multisig åpne kontrakter**: Gjør det mulig å opprette tilpassede betingede kontrakter ved hjelp av et 2-på-3 multisig-system med arbitrasje.

Disse protokollene er under utvikling og vil gradvis bli integrert i Bisq 2, noe som vil gi brukerne større fleksibilitet i henhold til deres spesifikke behov.

## Nyttige ressurser


- Offisiell nettside: [bisq.network](https://bisq.network)
- Dokumentasjon: [Bisq Wiki](https://bisq.wiki)
- Støtte: [Forum Bisq](https://bisq.community)
- Kildekode : [GitHub] (https://github.com/bisq-network)