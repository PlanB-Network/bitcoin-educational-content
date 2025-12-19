---
name: Braiins Pool

description: Inleiding tot Braiins zwembad
---

![signup](assets/cover.webp)


Braiins Pool, vroeger bekend als Slush Pool, is de allereerste Bitcoin Mining pool. Het werd opgericht in november 2010 en heeft zijn eerste blok gedolven op 16 december 2010, blok 97834.


Vanaf mei 2024 heeft Braiins Pool een rekenkracht van 13 EH/s, wat ongeveer 1,8% van de totale Bitcoin Hashrate is. Het heeft in totaal 1.307.188 bitcoins gedolven, wat ongeveer 6% is van de maximale 21 miljoen bitcoins die ooit zullen bestaan.


### Compensatiesysteem


Sinds eind 2023 heeft Braiins Pool zijn vergoedingssysteem veranderd naar het FPPS-systeem (Full Pay Per Share). Dit betekent dat miners elke dag een beloning ontvangen voor al hun werk van de vorige dag, zelfs als de pool geen blok heeft gevonden. Dit verschilt van het oude systeem waarbij miners alleen een beloning ontvingen als de pool een blok vond.


**Het is vermeldenswaard, [volgens een tweet van Mononaut](https://x.com/mononautical/status/1777686545715089605) die de Bitcoin TimeChain analyseert, dat veel Mining pools die gebruik maken van het FPPS systeem de gemijnde bitcoins naar een Address van AntPool zouden sturen, wat zou betekenen dat AntPool de Hashrate van al deze pools controleert, ongeveer 47% van de wereldwijde Bitcoin Hashrate. Dit is zeer slecht nieuws voor de decentralisatie van het netwerk.**


### Zwembadkosten


De kosten voor Braiins Pool zijn 2,5%, maar als je BraiinsOS gebruikt op je machines zijn de kosten 0%


### Opnames


**bliksemsnelle terugtrekking**

Met Lightning-opnames kun je één keer per dag je beloningen zonder minimumbedrag opnemen via een Lightning Address.

Om deze methode te gebruiken, moet je een Wallet hebben die compatibel is met Lightning-adressen.


**On-Chain Intrekkingen**

On-Chain opnames zijn beperkt tot een minimumbedrag en er kunnen kosten aan verbonden zijn.

Minimumbedrag: 20.000 Sats

Vergoedingen: 10.000 Sats voor bedragen van minder dan 500.000 Sats

Gratis voor bedragen boven 500.000 Sats

Opnames kunnen worden getriggerd door tijdsinterval of door bedrag.


## Account aanmaken


Om gebruik te maken van Braiins Pool [ga naar hun website](https://braiins.com/pool) en klik op "AANMELDEN" rechtsboven



![signup](assets/3.webp)


Voer je gegevens in en bevestig, je ontvangt dan een e-mail met het verzoek je Address te bevestigen. Bevestig met de link in de e-mail die je hebt ontvangen en log in op het platform


![signup](assets/4.webp)



## Een "werker" toevoegen

Een worker is de Miner die je met de pool verbindt. Om een nieuwe Miner toe te voegen, klik je op "Workers" in het linker zijbalkmenu.

![signup](assets/7.webp)


Klik vervolgens op de paarse knop "Workers + verbinden".


Selecteer in dit venster je geografische gebied.


Als de Miner die je wilt aansluiten BraiinsOS gebruikt, kies dan het "Stratum V2" protocol. Kies anders "Stratum V1".


![signup](assets/8.webp)


U krijgt de informatie om in te voeren op de webpagina van uw Miner (raadpleeg de documentatie van uw Miner om te weten waar u deze informatie moet invoeren).


Hier is **"stratum+tcp://eu.stratum.braiins.com:3333"** de URL van de pool.


**JimZap.workerName** is je identifier en de naam van je Miner, waarbij JimZap de identifier is en .workerName de naam van de Miner is. Als je meerdere miners hebt, kun je ze dezelfde naam geven, in welk geval hun rekenkracht bij elkaar opgeteld wordt op het dashboard, of geef ze verschillende namen om ze afzonderlijk te controleren.


En het wachtwoord is altijd hetzelfde **"alles123"**


Zodra u deze informatie hebt ingevoerd op de webpagina van uw Miner en Mining is opgestart, ziet u het na een paar minuten verschijnen op het Braiins Pool Dashboard.


## Dashboard Overzicht


![signup](assets/9.webp)


In de bovenste banner zie je het gemiddelde totale Hashrate van al je miners over 5 minuten, 1 uur en 24 uur. En een overzicht van het aantal miners online of offline.

Hieronder vind je een grafiek waarmee je de evolutie van je rekenkracht kunt volgen.


![signup](assets/10.webp)


Onder deze grafiek staan verschillende stukjes informatie over je beloningen in Sats.


**"Mining beloningen van vandaag"** Geeft aan hoeveel Sats je vandaag hebt gedolven. Aan het einde van de dag wordt deze waarde op 0 gezet en wordt de Sats naar je account gestuurd.


**"Totale beloning van gisteren"** Het aantal Sats dat je de dag ervoor hebt gedolven


**"Est. Winstgevendheid (1 TH/s)"** Is een schatting van het aantal Sats dat je op een dag verdient bij een rekenkracht van 1 TH/s. Bijvoorbeeld, als de waarde 77 Sats is, en je hebt een rekenkracht van 10 TH/s continu gedurende de dag, dan zou je theoretisch 77 x 10 = 770 Sats per dag verdienen.


**"All Time Reward"** Het totaal Sats dat je hebt gedolven met Braiins Pool


**"Beloningssysteem"** De vergoeding die door de pool wordt toegepast


**"Next Payout ETA"** Schatting van de tijd die het duurt voordat je Sats van het platform kunt halen. Hier laat de schatting niets zien omdat Mining nog maar een paar minuten onderweg is.


**"Account Balance"** Het aantal Sats dat beschikbaar is op je account en dat je kunt opnemen.

## Opnames instellen

Je kunt je beloningen opnemen met On-Chain of via lightning met een Address.


Klik bovenaan op "Fondsen". Standaard heb je een "Bitcoin Account". Je kunt anderen aanmaken om de beloningen te delen. Hier komen we in de volgende paragraaf op terug.


Klik nu op "Instellen".


![signup](assets/17.webp)


In dit nieuwe venster kun je kiezen voor "Onchain uitbetaling".


Geef deze Wallet een naam, geef een BTC Address op en selecteer het type trigger dat je wilt. "Drempel" betekent dat de betaling wordt getriggerd wanneer je een bepaalde hoeveelheid BTC hebt verzameld, en met "Tijdsinterval" wordt de betaling getriggerd op regelmatige tijdstippen (dag/weken/maanden).


Merk op dat het minimumbedrag 0,0002 BTC is en dat onder 0,005 BTC een vergoeding van 0,0001 BTC zal worden toegepast.


![signup](assets/18.webp)


Als je Lightning opnames wilt gebruiken, heb je een Wallet nodig die een Lightning Address levert. Je kunt bijvoorbeeld getAlby gebruiken.


Klik bovenaan het venster op "Lightning uitbetaling".


Voer uw Lightning Address in en vink het vakje "I understand..." aan en valideer.


Met deze opnamemethode worden je beloningen elke dag naar je Wallet gestuurd.


![signup](assets/14.webp)


Zodra je je uitbetalingsinstellingen hebt gevalideerd, ontvang je een bevestigingsmail.


![signup](assets/15.webp)


## Beloningen delen


Braiins Pool stelt je ook in staat om je beloningen over meerdere wallets te verdelen.


Klik hiervoor bovenaan op "Mining" en dan links op "Instellingen".


![signup](assets/19.webp)


Op deze pagina kunt u andere "financiële rekeningen" toevoegen door te klikken op "Nog een financiële rekening toevoegen" en uw beloningen in % verdelen over deze verschillende rekeningen waaraan u een Wallet moet koppelen. Om een nieuwe Wallet aan een financiële rekening te koppelen, zie het vorige hoofdstuk.