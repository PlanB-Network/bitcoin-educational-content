---
name: Braiins Pool

description: Introduksjon til Braiins Pool
---

![signup](assets/cover.webp)

Braiins Pool, tidligere kjent som Slush Pool, er den aller første Bitcoin mining-poolen. Etablert i november 2010, minet den sin første blokk den 16. desember 2010, blokk 97834.

Per mai 2024 har Braiins Pool en databehandlingskraft på 13 EH/s, som representerer omtrent 1,8% av den totale Bitcoin hashraten. Den har minet totalt 1,307,188 bitcoins, som er omtrent 6% av de maksimale 21 millioner bitcoins som noensinne vil eksistere.

### Kompensasjonssystem

Siden slutten av 2023 har Braiins Pool endret sitt kompensasjonssystem til å adoptere FPPS (Full Pay Per Share)-systemet. Dette betyr at minerne mottar belønninger hver dag for alt sitt arbeid fra forrige dag, selv om poolen ikke fant en blokk. Dette er forskjellig fra det gamle systemet hvor minerne kun mottok en belønning når poolen fant en blokk.

**Det er verdt å merke seg, [ifølge en tweet av Mononaut](https://x.com/mononautical/status/1777686545715089605) som analyserer Bitcoin TimeChain, at mange mining-pools som bruker FPPS-systemet ville sende de minede bitcoins til en adresse tilhørende AntPool, noe som ville bety at AntPool kontrollerer hashraten til alle disse poolene, omtrent 47% av den globale Bitcoin hashraten. Dette er veldig dårlige nyheter for desentraliseringen av nettverket.**

### Pool Avgifter

Avgiftene for Braiins Pool er 2,5%, men hvis du bruker BraiinsOS på maskinene dine vil avgiftene være 0%

### Uttak

**Lightning Uttak**
Lightning uttak lar deg ta ut dine belønninger uten minimumsbeløp en gang om dagen via en Lightning-adresse.
For å bruke denne metoden må du ha en lommebok som er kompatibel med Lightning-adresser.

**On-Chain Uttak**
On-Chain uttak er begrenset til et minimumsbeløp og kan være underlagt gebyrer.
Minimumsbeløp: 20,000 sats
Gebyrer: 10,000 sats for beløp mindre enn 500,000 sats
Gratis for beløp over 500,000 sats
Uttak kan utløses av tidsintervall eller av beløp.

## Opprette Konto

For å begynne å bruke Braiins Pool [gå til deres nettside](https://braiins.com/pool) og klikk på "SIGN UP" øverst til høyre


![signup](assets/3.webp)

Skriv inn informasjonen din og valider, du vil deretter motta en e-post som ber om bekreftelse av adressen din. Bekreft med lenken i e-posten du mottok og logg deretter inn på plattformen

![signup](assets/4.webp)


## Legge til en "worker"
En worker er mineren som du vil koble til poolen. For å legge til en ny miner, klikk på "Workers" i venstre sidemeny.
![signup](assets/7.webp)

Klikk deretter på den lilla "Connect Workers +" knappen.

I dette vinduet, velg ditt geografiske område.

Hvis mineren du ønsker å koble til bruker BraiinsOS, velg "Stratum V2"-protokollen. Ellers, velg "Stratum V1".

![signup](assets/8.webp)

Du vil ha informasjonen for å angi på din miners nettside (se din miners dokumentasjon for å vite hvor du skal angi denne informasjonen).

Her er **"stratum+tcp://eu.stratum.braiins.com:3333"** pool-URLen.
**JimZap.workerName** er din identifikator og navnet på din miner, hvor JimZap er identifikatoren og .workerName er navnet på mineren. Hvis du har flere minere, kan du enten gi dem samme navn, i så fall vil deres databehandlingskraft bli lagt sammen på dashbordet, eller gi dem forskjellige navn for å overvåke dem individuelt.
Og passordet er alltid det samme **"anything123"**

Når du har angitt denne informasjonen på din miners nettside og den har startet med mining, vil du se den dukke opp etter noen minutter på Braiins Pool Dashboard.

## Oversikt over Dashbord

![signup](assets/9.webp)

I toppbanneret kan du se den gjennomsnittlige totale hashraten for alle dine minere over 5 minutter, 1 time og 24 timer. Og et sammendrag av antall minere online eller offline.
Nedenfor lar et diagram deg følge utviklingen av din databehandlingskraft.

![signup](assets/10.webp)

Under dette diagrammet har du flere stykker informasjon om dine belønninger i sats.

**"Dagens Miningbelønninger"** Indikerer antall sats du har minet i dag. Ved slutten av dagen vil denne verdien bli tilbakestilt til 0 og satsene vil bli sendt til kontoen din.

**"Gårsdagens Totale Belønning"** Antall sats du minet dagen før

**"Est. Lønnsomhet (1 TH/s)"** Er et estimat av antall sats du tjener på en dag for en databehandlingskraft på 1 TH/s. For eksempel, hvis verdien er 77 sats, og du har en databehandlingskraft på 10 TH/s kontinuerlig gjennom dagen, da ville du teoretisk tjene 77 x 10 = 770 sats per dag.

**"All Time Reward"** Det totale antallet sats du har minet med Braiins Pool

**"Reward Scheme"** Gebyrsatsen som blir anvendt av poolen

**"Next Payout ETA"** Estimat av tiden det vil ta før du kan ta ut satsene fra plattformen. Her viser estimatet ingenting fordi miningen bare har vært i gang i noen minutter.

**"Account Balance"** Antall sats tilgjengelig på kontoen din, som du deretter kan ta ut.
## Sette opp Uttak
Du kan ta ut dine belønninger enten on-chain eller via lightning med en adresse.

Øverst, klikk på "Funds". Som standard har du en "Bitcoin Account". Du kan opprette andre for å dele belønningene. Vi vil komme tilbake til dette i neste seksjon.

For nå, klikk på "Set up".

![signup](assets/17.webp)

I dette nye vinduet kan du velge "Onchain payout".

Navngi denne lommeboken, oppgi en BTC-adresse, og velg hvilken type utløser du ønsker. "Threshold" betyr at betalingen vil bli utløst når du har akkumulert en definert mengde BTC, og med "Time interval", vil betalingen bli utløst med jevne mellomrom (dag/uker/måneder).

Merk at minimumsbeløpet er 0.0002 BTC og at under 0.005 BTC, vil et gebyr på 0.0001 BTC bli anvendt.

![signup](assets/18.webp)

Hvis du ønsker å bruke Lightning-uttak, trenger du en lommebok som gir en Lightning-adresse. For eksempel kan du bruke getAlby.

Klikk øverst i vinduet på "Lightning payout".

Skriv inn din Lightning-adresse og kryss av i boksen "I understand..." deretter valider.

Med denne uttaksmetoden vil dine belønninger bli sendt til lommeboken din hver dag.

![signup](assets/14.webp)
Når du har validert utbetalingsinnstillingene dine, vil du motta en bekreftelses-e-post.
![signup](assets/15.webp)

## Deling av Belønninger

Braiins Pool lar deg også dele dine belønninger på tvers av flere lommebøker.

For å gjøre dette, klikk på "Mining" øverst, deretter på "Settings" på venstre side.

![signup](assets/19.webp)

På denne siden vil du kunne legge til en annen "Financial Account" ved å klikke på "Add Another Financial Account" og fordele dine belønninger i % på tvers av disse forskjellige kontoene som du må knytte til en lommebok. For å knytte en ny lommebok til en Financial Account, se forrige seksjon.