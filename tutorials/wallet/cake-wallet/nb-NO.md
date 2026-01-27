---
name: Cake Wallet
description: Opplæring om Cake Wallet og stille betalinger
---

![cover](assets/cover.webp)


Denne guiden utforsker [**Cake Wallet**](https://cakewallet.com/): en åpen kildekode, ikke-frihetsberøvende, personvernfokusert wallet med flere valutaer tilgjengelig for Android, iOS, macOS, Linux og Windows. Vi dykker ned i de Bitcoin-spesifikke personvernfunksjonene, går gjennom sending/mottak av Bitcoin via **Silent Payments** (en forbedret on-chain-personvernprotokoll) og tar en titt på implementeringen av PayJoin v2 for asynkrone transaksjoner.


## 🎉 Viktige funksjoner



- [**Silent Payments (BIP-352)**](https://bips.dev/352/) forbedrer den tidligere [BIP 47 betalingskoder](https://silentpayments.xyz/docs/comparing-proposals/bip47/), også kalt "PayNyms", med gjenbrukbare stealth-adresser. Når en avsender bruker din Silent Payment-adresse, utleder deres wallet en unik engangsadresse ved hjelp av forskjellige nøkler som kombineres til en unik engangsadresse Taproot. Blokkjedeoppføringene viser ikke-relaterte transaksjoner, noe som forhindrer kobling av innkommende betalinger. Silent Payments tilbyr en rekke fordeler, blant annet
    - Gjenbrukbare adresser: Du trenger ikke å generate en ny adresse for hver transaksjon, noe som gir en bedre brukeropplevelse og økt personvern
    - Null kostnadsøkning: Silent Payments øker ikke størrelsen på eller kostnadene ved transaksjoner.
    - Forbedret anonymitet: Uvedkommende kan ikke knytte transaksjoner til en Silent Payment-adresse.
    - Ingen interaksjon mellom avsender og mottaker er nødvendig: Transaksjoner kan gjennomføres uten kommunikasjon mellom partene.
    - Unike adresser for hver betaling: Eliminerer risikoen for utilsiktet gjenbruk av adresser.
    - Ingen server er nødvendig: Stille betalinger kan utføres uten behov for en dedikert server.
- PayJoin v2** reduserer transaksjonsgrafanalysen ved å slå sammen inndataene fra avsendere og mottakere til én enkelt transaksjon. Kake Wallet implementerer to viktige fremskritt:
    - Asynkrone transaksjoner**: Avsender og mottaker trenger ikke lenger å være online samtidig for å fullføre en privat transaksjon.
    - Serverløs kommunikasjon**: Ingen av partene trenger å kjøre en Payjoin-server, noe som fjerner en viktig teknisk barriere.
- Coin Control** muliggjør manuelt valg av UTXO under transaksjoner. Dette forhindrer utilsiktet kobling av adresser når du bruker flere UTXO-er med forskjellig opprinnelse.
- Støtte for TOR**, slik at brukerne kan rute nettverkstrafikken sin gjennom Tor-nettverket
- RBF** (Replace-By.Fee) lar deg justere gebyret etter at du har sendt en transaksjon.


## 1️⃣ Sette opp din Wallet


Cake Wallet tilbyr et bredt spekter av plattformstøtte. Du kan velge mellom `Android`, `iOS / macOS`, `Linux` og `Windows`.  For å begynne, besøk https://docs.cakewallet.com/get-started/ og velg ditt operativsystem.


![image](assets/en/01.webp)


Etter installasjonen angir du en PIN-kode (4 eller 6 siffer). Du vil da se:


1. `Opprett en ny Wallet` (for nye brukere)

2. `Restore Wallet` (for eksisterende lommebøker)


![image](assets/en/02.webp)


På neste skjermbilde kan du velge mellom et bredt spekter av kryptovalutaer. Velg `Bitcoin` og trykk på `Neste` og oppgi et `Wallet navn` for å identifisere wallet. Ved å trykke på `Avanserte innstillinger` vises en rekke `Innstillinger for personvern`. Gjør disse endringene:



- Fiat API:** velg `Tor Only` (ruter prisforespørsler gjennom Tor)
- Swap:** velg `Tor Only` (anonymiserer utvekslingstrafikken)


BIP-39 seed-typen genereres som standard, med mulighet for å endre til Electrum seed-typen. Avledningsstiene er følgende:



- Electrum: `m/0'`
- BIP-39: `m/84'/0'/0`


Hvis du vil legge til et ekstra sikkerhetslag, kan du sette opp en `passphrase`.  Hovedformålet med en passphrase er å gi ekstra beskyttelse mot fysiske angrep. Selv om en angriper finner seed-frasen, kan han eller hun ikke få tilgang til wallet uten riktig passphrase. Med andre ord representerer seed-frasen alene én wallet, mens seed-frasen pluss passphrase skaper en helt annen wallet uten noen forbindelse til den opprinnelige. Denne funksjonen muliggjør også "hemmelige lommebøker" beskyttet av passphrase, og gir deg plausibel benektbarhet. I en tvangssituasjon kan du avsløre seed-frasen mens du holder større verdier trygge i den passphrase-beskyttede wallet.


Hvis du allerede kjører din egen node, kan du slå på "Legg til ny egendefinert node" og oppgi "Node Address" for å validere transaksjoner og blokker i din egen infrastruktur. Når du er ferdig, trykker du på `Continue` og `Next` for å opprette din wallet.


![image](assets/en/03.webp)


På neste skjermbilde får du en ansvarsfraskrivelse:


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Hvis du vil lære hvordan du lagrer minnefrasen din, kan du lese denne veiledningen:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Trykk på `Jeg forstår. Vis meg min seed` og lagre disse ordene på et sikkert sted! Trykk deretter på `Verifiser seed` og etter verifisering `Åpne Wallet`.


## 2️⃣ Innstillinger


Før vi går dypere inn i dette, skal vi ta en titt på `Hjem-skjermen` og `Innstillinger`.


På startskjermen kan vi se forskjellige elementer som vises:



- `Hamburgermenyen` bringer oss til `innstillinger`
- Tilgjengelig saldo
- Silent Payments Card for å begynne å skanne etter transaksjoner sendt til Silent Payment-adressen din
- Payjoin-kort for å aktivere Payjoin som en personvernbevarende og gebyrbesparende funksjon
- nederst er det snarveier til `Wallet Oversikt`, `Mottak`, `Bytte` mellom Bitcoin og andre valutaer, `Send` og `Kjøp`


![image](assets/en/11.webp)


Ved å trykke på `Hamburgermeny`-ikonet åpnes innstillingsmenyen. La oss gå gjennom alternativene.


![image](assets/en/05.webp)


### A - Tilkobling og synkronisering 🔗


Her kan vi koble til wallet på nytt, administrere noder og koble til vår egen node (anbefales). Med `Silent Payments Scanning` kan vi tilpasse skanningen ved å spesifisere enten `Scan from block height` eller `Scan from date`.


![image](assets/en/06.webp)


Som en "Alpha"-funksjon er det også mulig å aktivere innebygd Tor for å rute trafikk gjennom Tor-nettverket.


### B - Innstillinger for stille betalinger 🔈


Vi kan slå på Silent Payments-kortet på startskjermen for å vise denne funksjonen. Ved å aktivere "Alltid skanning" kan wallet kontinuerlig overvåke blokkjeden for innkommende Silent Payments. Vi kan spesifisere skanneparametere for å tilpasse skanneprosessen til våre behov som beskrevet ovenfor.


![image](assets/en/07.webp)


### C - Sikkerhet og sikkerhetskopiering 🗝️


For å sikre wallet kan vi lage en sikkerhetskopi ved å følge instruksjonene i appen. Dette vil sikre at vi har en trygg kopi av våre private nøkler, slik at vi kan gjenopprette wallet hvis den mistes eller blir stjålet. I tillegg kan vi se seed-frasen og de private nøklene våre, endre PIN-koden vår, aktivere biometrisk autentisering, signere/verifisere og konfigurere 2FA for et ekstra lag med beskyttelse.


![image](assets/en/08.webp)


**Merknad**: Fra og med september 2025 kreves det at biometrisk autentisering av fingeravtrykk på Android-enheter fungerer med minst en biometrisk klasse 2-implementering, se [her](https://source.android.com/docs/security/features/biometric/measure#biometric-classes) for mer informasjon. Dette kravet kan imidlertid bli endret i fremtiden.


### D - Personverninnstillinger 🔒


Vi kan også forbedre sikkerheten til wallet ved å bruke Tor til å kryptere internettforbindelsen vår og beskytte personvernet vårt når vi går inn på eksterne kilder. I tillegg kan vi forhindre skjermbilder for å holde wallet-informasjonen konfidensiell, aktivere automatisk genererte adresser for å opprette nye for hver transaksjon, og deaktivere kjøp/salg-handlinger for å forhindre uautoriserte transaksjoner. Videre kan vi aktivere PayJoin, som er en annen personvernfunksjon vi skal se nærmere på senere.


![image](assets/en/09.webp)


### E - Andre innstillinger 🔧


Andre innstillinger gjør det mulig for oss å administrere gebyrprioriteten og angi standard gebyrnivå for transaksjonene våre. Dette gjør det mulig for oss å kontrollere transaksjonsgebyrene knyttet til våre Silent Payments, med hensyn til gjeldende nettverksutnyttelse.


![image](assets/en/10.webp)


## 3️⃣ Motta ₿itcoin ved hjelp av Silent Payments


Det finnes flere alternativer og adressetyper for mottak av Bitcoin. `Segwit (P2WPKH)` *(starter med bc1q....)* er standardalternativet.  La oss velge `Silent Payments` i dette eksempelet.


For å motta en Silent Payment trykker du først på `Mottak`-ikonet i Cake Wallet. Deretter skriver du inn beløpet du forventer å motta. For å spesifisere adressetypen trykker du på `Mottak` øverst på skjermen igjen, og velger deretter `Silent Payments` blant alternativene.


På hovedskjermen vises QR-koden og adressen til din gjenbrukbare Silent Payment. Som forventet er adressen ganske lang:


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


Bruk nå en BIP-352-kompatibel wallet (for eksempel Blue Wallet) til å skanne denne QR-koden og sende betalingen. Du vil se at wallet utleder en unik destinasjonsadresse fra den stille adressen din.


![image](assets/en/13.webp)


## 4️⃣ Sending av bitcoin ved hjelp av Silent Payments


Ettersom Blue Wallet bare kan `Sende` Stille betalinger, vil vi bruke en annen BIP 352 kompatibel wallet som mottaker. Denne prosessen er identisk med en vanlig Bitcoin-transaksjon.



- Trykk på "Send" på startskjermen
- enten ved å lime inn vår gjenbrukbare `sp1qq...`-adresse eller ved å skanne QR-koden direkte i appen.
- Velg hvor mye du vil bruke av den tilgjengelige saldoen din
- Trykk på `Send` nederst på skjermen for å bekrefte transaksjonen


Når vi har angitt `sp1qq...`-adressen, utleder wallet automatisk en tilsvarende `bc1p...` Taproot-adresse (P2TR) i bakgrunnen, som vil bli brukt til Silent Payment.


Vi kan velge å skrive en intern note for hver transaksjon, justere gebyrinnstillingene eller velge bestemte UTXO-er for transaksjonen ved hjelp av funksjonen `Coin Control`.


![image](assets/en/14.webp)


sveip til høyre for å bekrefte transaksjonen.


Når du har sendt transaksjonen, blir du spurt om du vil legge til denne kontakten i adresseboken din.


![image](assets/en/15.webp)


## 5️⃣ PayJoin


La oss se på hva PayJoin er [om](https://docs.cakewallet.com/cryptos/bitcoin/#payjoin):


_Payjoin v2 er en personvernbevarende og gebyrbesparende funksjon i Bitcoin som gjør det mulig for avsender og mottaker av en transaksjon å samarbeide om å opprette én enkelt transaksjon. Denne transaksjonen har input fra *både* avsender og mottaker, noe som bryter de vanligste overvåkningsteknikkene mot Bitcoin og muliggjør bedre skalering og gebyrbesparelser i noen tilfeller også._ _


Hvis du vil lære mer om PayJoin, kan du også besøke følgende veiledning.


https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

For å bruke PayJoin trenger begge parter en PayJoin-kompatibel wallet, og mottakeren må ha minst én mynt eller utgang i sin wallet. Følg disse trinnene for å starte:


1. Trykk på `Hamburger Menu` og trykk på `Privacy`-knappen

2. Slå på alternativet `Bruk Payjoin`

3.  Trykk på "Motta" på startskjermen, og du vil bli presentert med en PayJoin QR-kode og en kopieringsknapp (når du har valgt Segwit)


![image](assets/en/16.webp)


## 6️⃣ Andre funksjoner


Det er flere andre funksjoner som `Swaps` i flere valutaer, `Kjøp og selg`-alternativer med forskjellige leverandørforbindelser og kakespesifikke programmer som `Cake Pay`, som lar deg kjøpe forhåndsbetalte kort eller gavekort.


![image](assets/en/17.webp)


## 🎯 Konklusjon


Dette er vår anmeldelse av Cake Wallet, som tilbyr praktisk Bitcoin-personvern takket være funksjoner som Silent Payments (BIP-352) og Payjoin v2.


Silent Payments erstatter engangsadresser med gjenbrukbare stealth-adresser for å forhindre on-chain-kobling av innkommende transaksjoner. Selv om synkroniseringsproblemene fra tidligere versjoner har blitt betydelig forbedret, er det noen økte beregningskrav for å skanne og oppdage Silent Payments, noe som krever mer ressurser og båndbredde.


Payjoin v2 bryter med kjedeanalysen ved å slå sammen avsender- og mottakerinput til én enkelt transaksjon uten ekstra avgifter eller sentral koordinering. Dette bryter med den vanlige heuristikken om eierskap til inndata, noe som er en betydelig fordel ettersom det betyr at du ikke kan anta at alle inndata tilhører avsenderen.


For brukere som prioriterer økonomisk anonymitet, er Cake Wallet et levedyktig alternativ. Den inkorporerer personvernprotokoller direkte i kjernefunksjonaliteten, noe som gjør dem tilgjengelige uten teknisk kompleksitet. Etter hvert som overvåkningen på offentlige blokkjeder øker, bidrar verktøy som dette til å opprettholde transaksjonelt personvern der det betyr mest. En bredere implementering av disse standardene i wallet-landskapet vil være en velkommen utvikling.


## 📚 Ressurser


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://bips.dev/352/](https://bips.dev/352/)


https://payjoin.org/