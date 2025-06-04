---
name: Nakamochi
description: Node Running Made Easy - Hvordan sette opp og bruke Nakamochi Bitcoin og Lightning node.
---
Å drive din egen Bitcoin- og Lightning-node trenger ikke lenger å være en kompleks oppgave som er begrenset til tekniske eksperter. Tradisjonelt har det å sette opp og administrere noder krevd inngående kunnskap om kryptografi, nettverk og programvareutvikling. Nakamochi endrer dette ved å gjøre noder tilgjengelige for alle, uavhengig av teknisk bakgrunn.

Med Nakamochi kan hvem som helst sette opp og drive en node hjemmefra, noe som gir fullt personvern og økonomisk uavhengighet. Ved å drive en full node sikrer du ikke bare dine egne transaksjoner, men bidrar også til Bitcoin-nettverkets styrke. Et desentralisert og robust Bitcoin-nettverk er avhengig av en bred distribusjon av noder for å sikre sikkerhet og uavhengighet.

### Innholdsfortegnelse


- Hva er Nakamochi og hvordan fungerer det?
- Sette opp Nakamochi
- Om Lightning Network
- Åpne kanaler og foreta transaksjoner i Lightning-nettverket

## Hva er Nakamochi og hvordan fungerer det?

Nakamochi er en fullverdig Bitcoin-node som støtter både Bitcoin- og Lightning-nettverkene. Den inkluderer en integrert Bitcoin- og Lightning-lommebok, slik at brukerne kan kjøre en sikker, selvsuveren Bitcoin-node samtidig som de drar nytte av Lightning-nettverkets hastighet og lave transaksjonskostnader.

Nakamochi-noden din administreres via en mobilapp, [BitBanana (Android)] (https://bitbanana.app) og [Zeus (iOS)] (https://bitbanana.app), slik at du enkelt kan kontrollere den fra hvor som helst. Disse appene fungerer som en fjernkontroll for noden din, slik at du enkelt kan betale direkte med Bitcoin eller Lightning, administrere transaksjoner, åpne eller lukke kanaler, sjekke saldoer og overvåke nodens ytelse.

## Det tar bare 5 minutter å sette opp Nakamochi

### Trinn 1: Koble deg til og kom i gang

1. Koble Nakamochi til strøm og Wi-Fi.

2. Klikk på **"Sett opp ny lommebok"** og lagre gjenopprettingsfrasen på 24 ord på en sikker måte.

3. Bruk en nodeadministrasjonsapp (Zeus eller BitBanana) for å koble deg til Nakamochi:

4. Åpne appen og skann QR-koden som vises på Nakamochi.

5. For ekstra sikkerhet kan du angi en PIN-kode på enheten.

![image](assets/en/01.webp)

_Connect to power and write down your 24-word seed phrase__

![image](assets/en/02.webp)

_Vent til blokkjeden har tatt oss igjen_ _Vent til blokkjeden har tatt oss igjen

![image](assets/en/03.webp)

_Sett opp en ny lommebok i Lightning Tab_

![image](assets/en/04.webp)

_Skann QR-kode med Node Management App_

![image](asset/en/05.webp)

_For ekstra sikkerhet, angi en PIN-kode_

**Merk:** _Gjør det mulig for Nakamochi-noden din å synkronisere med blokkjeden. Denne prosessen kan ta litt tid avhengig av internettforbindelsen din

## Om Lightning Network

Bitcoin Lightning Network revolusjonerer Bitcoin-transaksjoner ved å gjøre dem raskere, billigere og mer effektive. Det er perfekt for hverdagsbruk, og muliggjør nesten øyeblikkelige betalinger med minimale avgifter, noe som er ideelt for mikrotransaksjoner som å kjøpe en kaffe eller håndtere hyppige småkjøp.

Ved å operere utenfor kjeden er Lightning designet for å kunne skalere og støtte tusenvis av transaksjoner i sekundet uten å overbelaste Bitcoins hovedblokkjede. Dette gjør den til en nøkkelaktør i Bitcoins utvikling til et praktisk, globalt betalingssystem.

Personvern er en annen fordel, ettersom transaksjoner på Lightning rutes gjennom private betalingskanaler i stedet for å registreres direkte på blokkjeden. Dette sikrer en mer diskret måte å utføre transaksjoner på, samtidig som Bitcoins robuste sikkerhet opprettholdes.

#### Forklaring av betalingskanaler

Lightning-nettverket opererer gjennom betalingskanaler, som er forbindelser mellom to parter som muliggjør flere transaksjoner uten å samhandle direkte med blokkjeden. Når en kanal er åpen, oppdateres saldoen mellom de to partene på denne andre lags Lightning-løsningen for hver transaksjon, noe som sikrer raske og rimelige betalinger. Bare kanalens åpning og stenging registreres i kjeden, noe som reduserer overbelastningen på Bitcoin-blokkjeden. Dette designet sikrer skalerbarhet og personvern, ettersom individuelle transaksjoner ikke registreres i den offentlige hovedboken.

**Eksempel:** Alice og Bob åpner en kanal ved å overføre Bitcoin til den. Alice sender Bitcoins til Bob, og saldoen deres utenfor kjeden oppdateres umiddelbart uten at det registreres i kjeden. Hvis Alice deretter betaler Charlie, og Alice ikke har noen direkte kanal til Charlie, kan betalingen rutes gjennom Bobs kanal for å nå Charlie. Ruting gjennom mellomliggende noder sikrer betalinger selv uten direkte forbindelser, noe som gjør nettverket svært effektivt.

## Åpne kanaler og foreta transaksjoner i Lightning-nettverket

Når Nakamochi er satt opp og koblet til en nodeadministrasjonsapp, kan du begynne å bruke Lightning Network ved å åpne kanaler og foreta transaksjoner.

### Åpne kanaler på Zeus (iOS):

1. Gå til fanen **"Channels"** (nederste meny).

2. Klikk på **"+"** for å åpne en ny kanal.

3. Skann eller skriv inn pubnøkkelen til noden du vil koble deg til.

4. Angi det låste beløpet (velg sammen med kollegaen din eller bruk det faste minimumsbeløpet for kjente noder).

5. Klikk på **"Åpne kanal"**.

![image](asset/en/06.webp)

_ZEUS Skjermbilde_ _ZEUS

For mer informasjon: [Kanaler | Zeus-dokumentasjon](https://docs.zeusln.app/)

### Åpne kanaler på BitBanana (Android):

1. Åpne hamburgermenyen (til venstre).

2. Gå til **"Kanaler"**.

3. Klikk på **"+"** for å legge til/åpne en ny kanal.

4. Skann eller lim inn pubnøkkelen.

5. Angi det låste beløpet (velg sammen med kollegaen din eller bruk det faste minimumsbeløpet for kjente noder).

![image](asset/en/07.webp)

_Bitbanana Skjermbilde

For mer informasjon: [BitBanana](https://bitbanana.com)

Når kanalen din er åpen, kan betalinger dirigeres gjennom den til andre deltakere i nettverket. Saldoen justeres utenfor kjeden, slik at transaksjonene skjer nesten umiddelbart og med minimale gebyrer.

Hvis du ikke lenger trenger en kanal, kan du stenge den. Denne handlingen gjør opp den endelige saldoen mellom deg og motparten din og registrerer den i kjeden. Ideelt sett er begge parter enige og er online for en "kooperativ avslutning" (raskere og med lavere gebyrer enn en "tvungen avslutning" med en motpart som ikke svarer eller er offline).

Generelt anbefaler vi å la kanalene være åpne for å redusere kostnadene og øke nettverkets pålitelighet og effektivitet. Ved å holde kanalene åpne minimerer du transaksjonsgebyrene i kjeden, unngår nedetid for kanaltilkoblinger og opprettholder en stabil rutingkapasitet for sømløs betalingsbehandling. Denne tilnærmingen bidrar til et robust og motstandsdyktig nettverk, samtidig som den forbedrer den generelle brukeropplevelsen og reduserer driftskostnadene.

### Nyttige lenker


- [Om Nakamochi](https://nakamochi.io/)
- [Abonner på Nakamochis nyhetsbrev](https://90c7addc.sibforms.com/serve/MUIFAHG7H5YBPpm-kZ8G6TuS-nmL4uaq85rlpBfI__S79tZ5jheIJfF3kJYudycgs_6_RUdDBkt8Sd7OyNL_JDTTJvOb36ifF6vcQoabBXKp4cbefzh1DYqnok_jItexICcQL13ucd2aS581ngqy7jr0Q1H3HhxV3z2eWKE5-Z-YMasj-MMotQeDvdorMCSi0XgCWDqs8rEMQC7E)