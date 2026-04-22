---
name: Bull Bitcoin-wallet
description: Ontdek hoe je de Bull Bitcoin-wallet gebruikt
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*Deze videotutorial van BTC Sessions leidt je door het proces van het instellen en gebruiken van de Bull Bitcoin-wallet!*


Deze handleiding neemt je mee door de installatie, configuratie en het gebruik van de Bull Bitcoin-wallet. Je leert geld verzenden en ontvangen via de Bitcoin on-chain, Liquid en Lightning-netwerken, en hoe je de bitcoin daartussen kunt verplaatsen. De uitgebreide functies van de wallet maken het een krachtige, alles-in-één tool voor het beheren van je Bitcoin. Laten we aan de slag gaan.


## Inleiding


Bull Bitcoin-wallet, ontwikkeld door [Bull Bitcoin](https://www.bullbitcoin.com/), is een **self-custodial** Bitcoin-wallet, wat betekent dat je volledige controle hebt over je privésleutels en dus je fondsen, zonder afhankelijk te zijn van een derde partij. Open-source en geworteld in een cypherpunk-filosofie, combineert deze wallet eenvoud, vertrouwelijkheid en geavanceerde functies zoals cross-network swaps en PayJoin ondersteuning. Je kunt je bitcoins op drie netwerken beheren: **Bitcoin on-chain**, **Liquid** en **Lightning**, elk op maat gemaakt voor specifiek gebruik. Op de [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49), kun je actuele onderwerpen en komende ontwikkelingen bekijken. Aangezien het project 100% open-source is en "gebouwd in het openbaar", kun je ook je suggesties en bugs die je tegenkomt opsturen. Terwijl sommige wallets nu meerdere netwerken ondersteunen, onderscheidt de Bull Bitcoin-wallet zich door de diepgaande integratie van privacyfuncties over al deze netwerken, waardoor het een krachtig hulpmiddel is voor het beheren van je bitcoin over alle grote netwerken.


## 1️⃣ Vereisten


Voordat je de **Bull Bitcoin-wallet** in gebruik neemt, moet je ervoor zorgen dat je de volgende onderdelen hebt:



- **Compatibele smartphone**: Een **iOS** (iPhone of iPad) of **Android**-apparaat
- **Internetverbinding**
- **Veilige back-up media**: Schrijf je **herstelzin** (12 woorden) op papier of metaal en bewaar deze op een veilige plaats.
- **Basiskennis**: Een minimum aan kennis van Bitcoin-concepten (adressen, transacties, kosten) is nuttig, hoewel deze tutorial elke stap uitlegt voor beginners.


## 2️⃣ Installatie


Je kunt de applicatie installeren via:



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(voor iOS-apparaten)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) (voor Android-apparaten)


Android-gebruikers hebben ook alternatieve opties:



- Download de APK rechtstreeks van de [GitHub Releases](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) pagina of
- Installeren via de Nostr-compatibele [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap)


Volg na het installeren van de applicatie het welkomstscherm om je account te configureren.


## 3️⃣ Eerste configuratie


Bij het openen worden de volgende opties gevraagd:



- `Create New Wallet`
- `Recover Wallet` en
- `Advanced Options`


Laten we beginnen door op `Advanced Options` te tikken.


Hier kunnen we de geavanceerde instellingen configureren voordat we een wallet aanmaken of herstellen:


1. Schakel de `Tor proxy` in om verkeer over het Tor-netwerk te routeren.
      1. [Orbot-app](https://orbot.app/en/) moet geïnstalleerd en actief zijn voordat je deze inschakelt
      2. Tor Proxy is alleen van toepassing op Bitcoin (niet Liquid) en kan resulteren in een langzamere verbinding.

2. Een `Aangepaste Electrum Server` instellen, of

3. Pas de `Recover Bull` instellingen aan. We zullen later meer leren over de [Recover Bull](https://recoverbull.com/).


Nadat je alle optionele aanpassingen hebt gemaakt, tikt je op `Gedaan`. Als je een bestaande wallet opnieuw wilt gebruiken, klik dan op `Herstel wallet` en vul de 12 woorden van je herstelzin in.


Klik anders op `Create a New Wallet`.


![image](assets/en/01.webp)


## 4️⃣ beginscherm


Voordat we dieper duiken, kijken we eerst naar het `Home scherm` om ons te oriënteren:



- het `transactieoverzicht` (Transactions) en `instellingsmenu` (Settings) bevinden zich bovenaan.
- Het `Beschikbaar Saldo` (Available Balance) heeft een privacy-optie die `aan of uit` kan worden gezet.
- Ga naar de `Bitcoin Bull exchange` om te `Kopen, Verkopen of Betalen` (dit hangt af van de jurisdictie en kan KYC vereisen).
- `Overdracht` (Transfer) van fondsen tussen wallets.
- `Secure Bitcoin` is gelijk aan on-chain Bitcoin-wallet.
- `Instant payments` via het Lightning- / Liquid Network *(Opmerking: Bull Bitcoin-wallet maakt het mogelijk betalingen te doen en te ontvangen via Lightning. Fondsen ontvangen via Lightning worden opgeslagen op het [*Liquid netwerk](https://liquid.net/) (in de wallet Instant Payments) dankzij een automatische swap via [*Boltz exchange](https://boltz.exchange/). Dit geeft je de mogelijkheid om te communiceren met Lightning zonder liquiditeitskanalen te hoeven beheren, terwijl je in self-custody blijft.)*
- `Versturen` (Send) en `Ontvangen` (Receive) van fondsen.


![image](assets/en/02.webp)


Laten we eerst een aantal belangrijke configuraties maken en beginnen met `Backup`.


## 5️⃣ Back-up


Om het back-upproces te starten, tik je op het `gear icoon (⚙)` in de rechterbovenhoek van de app en selecteer je `Wallet Backup`. Je krijgt twee methoden te zien om je wallet te beveiligen: `Encrypted Vault` en `Physical Backup`. Laten we ze verkennen.


![image](assets/en/03.webp)


### Fysieke back-up


Tik op `Physical Backup` om een lijst van 12 woorden te zien die jouw herstel- of seed zin vertegenwoordigen. Overweeg het volgende:



- Schrijf je `herstelzin` met de grootste zorg op. Schrijf het op papier of metaal en bewaar het op een veilige plaats (kluis, offline locatie). Deze zin is je enige manier om toegang te krijgen tot je bitcoins in het geval van verlies van je apparaat of verwijdering van de applicatie.
- Het is ook belangrijk om te weten dat iedereen met deze zin al je bitcoins kan stelen. Sla het nooit digitaal op:
    - Geen screenshot
    - Geen cloud-, e-mail- of berichtenback-ups
    - Geen kopiëren/plakken (risico van opslaan op klembord)


![image](assets/en/25.webp)


Op het volgende scherm moet je de woorden in de juiste volgorde zetten om er zeker van te zijn dat je de herstelzin goed hebt. Je krijgt een bevestiging als de test geslaagd is.


! **Dit punt is cruciaal**. Voor verdere hulp :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### Gecodeerde kluis


Er is ook de optie van een versleutelde, anonieme back-up in de cloud. Maar zeiden we in de vorige paragraaf niet dat cloudback-ups riskant zijn en vermeden moeten worden? Het Bull Bitcoin-team heeft echter een slimme manier ontwikkeld om het proces veilig te maken. Dit is hoe het werkt:


`Recoverbull` is een back-upprotocol dat het beveiligen van je Bitcoin-wallet vereenvoudigt door de back-up in twee delen op te splitsen. Ten eerste wordt het back-upbestand van je wallet versleuteld op je apparaat met behulp van een sterke versleutelingscode. Je kunt dit versleutelde bestand opslaan waar je maar wilt, zoals Google Drive of je apparaat. Ten tweede, de coderingssleutel die nodig is om het bestand te ontgrendelen is opgeslagen door de Recoverbull Key Server. Om je wallet te herstellen, heb je zowel het versleutelde back-upbestand als de sleutel nodig, die je opent met je PIN-code of wachtwoord. Dit ontwerp zorgt ervoor dat je cloud back-up alleen nutteloos is en dat de sleutel server (Key Server) alleen nutteloos is zonder je specifieke back-up bestand. Hierdoor blijven je fondsen veilig, zelfs als één onderdeel is gecompromitteerd.


Zie het als een kluis. Het versleutelde back-up bestand is de *box*, die je overal kunt opslaan (zoals Google Drive). Je recovery PIN is de *sleutel*, die apart wordt opgeslagen door de Recoverbull Key Server. Een dief zou zowel je specifieke doos als je specifieke sleutel moeten hebben om het te openen. Dit ontwerp zorgt ervoor dat zelfs als iemand je back-up bestand krijgt, het nutteloos is zonder de sleutel van de server, en de sleutel van de server is nutteloos zonder je unieke back-up bestand.


Leer meer over het `Recoverbull` wallet back-upprotocol [hier](https://recoverbull.com/).


Tik op `Encrypted Vault` en vervolgens op `Continue` om het gebruik van de standaardserver te bevestigen. De verbinding wordt omgeleid via het `Tor` Netwerk om privacy en anonimiteit te garanderen.


**Inzicht in je pincodes**



- **`App Unlock PIN`:** De optionele PIN die is ingesteld in `Settings > Security-PIN` om de app op je telefoon te vergrendelen.
- **`Recovery PIN`:** De verplichte PIN die is aangemaakt tijdens het `Encrypted Vault` back-upproces en die wordt gebruikt om je back-upbestand te decoderen tijdens het herstel.


Dit zijn twee afzonderlijke PIN-codes. Vergeet je Recovery PIN niet, want deze is essentieel voor het herstellen van je wallet."


**Recovery PIN instellen:**



- Je moet een PIN-code of wachtwoord aanmaken om weer toegang te krijgen tot je wallet.
- De PIN-code / het wachtwoord moet minstens 6 cijfers lang zijn (vermijd bijvoorbeeld eenvoudige reeksen zoals 123456, die niet worden geaccepteerd).
- Zonder deze PIN is wallet herstel onmogelijk.


Selecteer vervolgens een vault provider:



- Google Drive` of
- een `gekozen locatie` (bijvoorbeeld je apparaat)


![image](assets/en/04.webp)


Sla nu het `back-up bestand` op. Tik vervolgens op `Test Recovery`, selecteer je opgeslagen back-upbestand of kluis en tik op `Decrypt Vault`. Voer je `PIN` of `wachtwoord` in. Als alles werkt, verschijnt het scherm `Test completed successfully`.


### Labels importeren/exporteren


Nu we onze back-up hebben gemaakt, gaan we eens kijken naar `labels`.  De Bull Bitcoin-wallet verbetert de privacy en organisatie door gebruikers in staat te stellen aangepaste labels te maken voor hun ontvangstadressen en transacties. Deze labels helpen je bij het categoriseren van je geld, omdat transacties die naar een gelabeld adres worden gestuurd, dat label overnemen, en je kunt ook uitgaande transacties labelen om hun verandering bij te houden. De wallet ondersteunt de [BIP-329](https://bip329.org/) standaard volledig, wat betekent dat je al je labels naar een bestand kunt exporteren en in een andere wallet kunt importeren. Deze functie zorgt ervoor dat je naadloos een back-up kunt maken van je transactiegeschiedenis en categorisaties, of deze kunt migreren tussen verschillende instanties van de wallet, zonder je persoonlijke organisatie te verliezen.


![image](assets/en/05.webp)


## 6️⃣ Instellingen


Nu je primaire back-up veilig is gesteld, gaan we de andere functies in de instellingen verkennen.


### A - Toegang beveiligen


Om de app te beveiligen, navigeer naar `Settings` en kies `Security PIN` om een PIN-code te selecteren. Maak een sterke PIN-code aan om de toegang tot je wallet te vergrendelen. Hoewel deze stap optioneel is, wordt het sterk aanbevolen om onbevoegde toegang te voorkomen als iemand anders je telefoon gebruikt.


![image](assets/en/06.webp)


### B - Verbinding met een persoonlijke node (optioneel)


De Bull Bitcoin-wallet maakt standaard verbinding met Electrum servers: de eerste wordt beheerd door Bull Bitcoin en een secundaire server van Blockstream, die beide geen logs bijhouden, waardoor het risico op tracering kleiner is.


Voor meer vertrouwelijkheid kun je de applicatie verbinden met je eigen Bitcoin node via een Electrum server. Tik hiervoor op `Settings` > `Bitcoin Settings` > `Electrum Server Settings`, tik vervolgens op `+ Add Custom Server` om het adres en de gegevens van je server in te voeren.


![image](assets/en/07.webp)


### C - Valuta


Het beschikbare saldo wordt op het hoofdscherm weergegeven in zowel `sats` als `USD`. Om dit te veranderen, ga je naar `Settings` > `Currency`. Daar kun je wisselen tussen `sats/BTC` en je `standaard fiatvaluta` selecteren.


![image](assets/en/08.webp)


### D - Bitcoin instellingen


Het menu `Bitcoin Settings` biedt diepgaande toegang tot de kernconfiguraties en -gegevens van je wallet. Hier kun je de fundamentele details van je `Secure Bitcoin` en `Instant payments wallets` bekijken. Hier kun je de fundamentele details van je `Secure Bitcoin` en `Instant payments wallets` bekijken, waardoor je volledige transparantie en controle hebt. De belangrijkste functies in dit menu zijn:



- **Wallet Details:** Navigeer naar je Beveiligde Bitcoin of Directe betalingen wallet om specifieke informatie te bekijken.
- **Wallet vingerafdruk:** Een unieke identificatie voor je wallet.
- Publieke sleutel (Pubkey):** De sleutel die gebruikt wordt om generate je Bitcoin ontvangstadressen te geven.
- **Descriptor:** Een technische samenvatting van de structuur van je wallet.
- **Afleidingspad:** Het specifieke pad dat wordt gebruikt om generate alle adressen van je privésleutel af te leiden.
- **Address bekijken:** Bekijk een lijst met je ongebruikte ontvangstadressen en wijzig adressen (verschijnt binnenkort)


Bovendien heb je de optie om:



- `Enable Auto Transfer` instellingen om een maximum wallet saldo in te stellen, dat vervolgens automatisch wordt overgeboekt naar de beveiligde bitcoin-wallet.
- Generieke wallets via `Mnemonic` zin of `watch-only` importeren.
- Verbind `Hardware wallets`: momenteel worden ColdcardQ, SeedSigner, Specter, Krux, Blockstream Jade en Foundation Passport ondersteund.


## 7️⃣ Bull Bitcoin exchange


Direct vanuit de wallet heb je toegang tot de [Bull Bitcoin exchange](https://www.bullbitcoin.com/), zodat je bitcoin kunt kopen, verkopen en betalen zonder de app te verlaten. Deze integratie biedt een handige oplossing voor het beheren van je Bitcoin behoeften. Houd er rekening mee dat de toegang tot de exchange en de diensten beperkt kan zijn, afhankelijk van je jurisdictie, en dat het voltooien van een KYC-verificatie (Know Your Customer) vereist kan zijn om te voldoen aan de wettelijke normen en gebruik te maken van alle functies van het platform.


Om te beginnen tik je op `Exchange` in de rechterbenedenhoek en vervolgens op `Sign up` of `Login` voor je account.


De exchange biedt de volgende [functies](https://www.bullbitcoin.com/):



- Bitcoin kopen met self-custody van je bankrekening
- Non-custodial
- Particulieren of bedrijven
- Onmiddellijke opname
- Geen verborgen kosten
- Lightning Network beschikbaar
- Geen transactielimieten
- Recurrente koopopties


![image](assets/en/09.webp)


Ga voor meer informatie naar deze tutorial:


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣ Geld ontvangen


Geld ontvangen met **Bull Bitcoin-wallet** is eenvoudig en flexibel, met ondersteuning voor drie verschillende netwerken, op maat gemaakt voor verschillende gebruikssituaties:



- Het `Bitcoin (on-chain)` netwerk voor veilige, langdurige opslag.
- Het `Liquid` netwerk voor snelle, meer vertrouwelijke transacties.
- Het `Lightning` netwerk voor directe, goedkope betalingen.


De app genereert automatisch het juiste adres of de juiste factuur op basis van je geselecteerde netwerk. Hier lees je hoe je te werk gaat voor elk netwerk.


### Ontvangen via onchain (Bitcoin-netwerk)


Om on-chain fondsen te ontvangen, kun je ofwel de `Secure Bitcoin Wallet` op het beginscherm selecteren en op `Receive` tikken, of op de hoofdknop `Receive` tikken en dan het `Bitcoin netwerk` kiezen.


Je hebt twee primaire modi voor het genereren van een ontvangstadres:


**Standaardmodus (URI met extra invoerparameters)**


Standaard genereert de wallet een [BIP21 URI](https://bips.dev/21/). Dit is een gestandaardiseerd formaat dat meer informatie verpakt dan een eenvoudig adres, waaronder een bedrag, een persoonlijke notitie en PayJoin parameters om de privacy te verbeteren. Deze uitgebreide URI wordt gecodeerd in een QR-code en beschikbaar gesteld om te kopiëren. Het formaat ziet er als volgt uit: `bitcoin:<adres>?<parameter1>=<waarde1>&<parameter2>=<waarde2>`.



- **Extra invoerparameters:**
    - **Bedrag:** Geef een gevraagd bedrag op in BTC, sats of een fiatvaluta.
    - **Bericht:** Voeg een persoonlijke notitie toe die zichtbaar is voor de afzender.
    - **PayJoin:** Schakel deze optie in om de privacy te verbeteren door de input van zowel de verzender als de ontvanger te combineren in de transactie.


Voorbeeld URI:


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


*Belangrijke opmerking: Stuur geen geld naar de adressen in deze tutorial, de wallet zal worden verwijderd.*


![image](assets/en/10.webp)


**Kopieer of scan adres alleen optie ingeschakeld**


Met de `Copy or scan Address only` optie ingeschakeld, genereert de applicatie een eenvoudig Bitcoin-adres in SegWit (bech32) formaat.


Voorbeeld:


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


Zelfs als je een bedrag of een notitie invoert, worden deze niet opgenomen in de QR-code of het gekopieerde adres.


![image](assets/en/11.webp)


### Ontvangen via het Liquid Network


Je kunt een betaling ontvangen op het Liquid Network. Eenmaal op het `Receive` scherm, heb je dezelfde twee opties om een betalingsverzoek te genereren:


**1. Eenvoudig adres:** Kopieer het standaard `Liquid adres`. Dit is een unieke identificatie voor je wallet op het Liquid-netwerk en bevat geen specifiek bedrag of bericht.


Voorbeeld Address:


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2. Gedetailleerd betalingsverzoek (URI):** Voor een meer gestructureerd verzoek kun je een bedrag en een persoonlijke notitie opgeven. Deze informatie wordt automatisch gecodeerd in een deelbare URI en de bijbehorende QR-code.



- **Bedrag:** Je kunt het bedrag instellen in Bitcoin (BTC), Satoshis (sats) of een fiatvaluta.
- **Opmerking:** Voeg een persoonlijk bericht toe om de transactie te identificeren.


**Voorbeeld URI:**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


Om de transactie te voltooien, geef je de afzender het `adres` of de `URI`. Je kunt dit doen door het naar je klembord te kopiëren of door ze de QR-code rechtstreeks vanaf je scherm te laten scannen.


![image](assets/en/12.webp)


### Ontvangen via Lightning



Met de Bull Bitcoin-wallet kun je ook betalingen verzenden en ontvangen via het Lightning Network. Een belangrijk kenmerk is dat geld dat je via Lightning ontvangt automatisch wordt omgewisseld en opgeslagen op het `Liquid Network` binnen je `Instant Payments Wallet`. Deze dienst wordt aangedreven door de `Boltz`. Door dit ontwerp kan je profiteren van de snelheid en lage kosten van Lightning zonder de complexiteit van het beheren van liquiditeitskanalen, terwijl je je fondsen volledig zelf bewaart. Hoewel deze hybride benadering self-custodial is en de complexiteit van het beheren van kanalen vermijdt, introduceert het een dienst van een derde partij (Boltz), een kleine swapvergoeding en afhankelijkheid van de Liquid Network federatie van functionarissen als keyholders, wat anders is dan een traditionele, niet-custodial Lightning-wallet waar je je eigen kanalen beheert. Je kan hier meer te weten komen over Liquid en hun bestuursmodel:


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- **Grenzen:**
    - **Minimumbedrag:** Een minimumfactuurbedrag is vereist. Controleer de app voor de huidige limiet.
    - **Kosten:** Jij, de ontvanger, bent verantwoordelijk voor een kleine swapvergoeding. Deze kosten worden afgetrokken van het bedrag dat de verzender overmaakt en kunnen veranderen.
- **Voordelen:**
    - **Self-Custodial:** je geld is altijd onder jouw controle, beveiligd op het Liquid-netwerk.
    - **Vermijd hoge on-chain kosten:** Door Lightning te gebruiken en op te slaan op Liquid, omzeil je de on-chain kosten die gepaard gaan met het openen van een traditioneel Lightning-kanaal. Je kan ervoor kiezen om later geld over te hevelen naar een on-chain-kanaal, wanneer het geaccumuleerde bedrag de kosten rechtvaardigt.
    - **Tip:** Voor de meest kosteneffectieve transactie tussen twee Bull Bitcoin-gebruikers, gebruik je het **Liquid netwerk rechtstreeks** om de Lightning swapkosten volledig te vermijden.


Om een betaling te ontvangen, moet je een `Lightning-factuur` genereren:


1. **`Voer een bedrag in`:** Geef het bedrag op dat je wilt ontvangen in Bitcoin (BTC), Satoshis (Sats) of een fiatvaluta.

2. **`Voeg een notitie toe` (optioneel):** Voeg een memo of notitie toe. Deze wordt opgenomen in de factuur en weergegeven in je transactiegeschiedenis zodra de betaling is voltooid, zodat je deze gemakkelijker kunt identificeren.

3. **`Geldigheid invoice`:** De Lightning-factuur is tijdsgevoelig en vervalt na **12 uur**. Als de factuur niet binnen deze periode wordt betaald, wordt deze ongeldig en moet je een nieuwe factuur genereren.


Geef de factuur aan de verzender door deze te kopiëren naar je klembord of door de QR-code te laten scannen die op je scherm wordt weergegeven.


![image](assets/en/13.webp)


## 9️⃣ Geld versturen


Je kunt het verzendscherm rechtstreeks openen vanaf de startpagina of vanuit een van je wallets. Bull Bitcoin-wallet vereenvoudigt het proces door automatisch het bestemmingsnetwerk te detecteren - `Bitcoin`, `Liquid` of `Lightning` op basis van het adres of de factuur die je invoert, geplakt of gescand via een QR-code.


### on-chain verzending via het Bitcoin Netwerk


Geld overmaken via on-chain betekent dat je transactie direct wordt geregistreerd op de Bitcoin-blockchain. Deze methode is het beste voor grotere overschrijvingen of niet-tijdgevoelige overschrijvingen. Om te beginnen kun je rechtsonder op de `Send` knop tikken, en een `standaard Bitcoin adres` scannen of invoeren.


Als het adres dat je opgeeft geen specifiek bedrag bevat, wordt je gevraagd om de details in te vullen op het verzendscherm. Je kunt het bedrag opgeven in de eenheid van je voorkeur, zoals BTC, satoshis of een fiat equivalent. Je hebt ook de optie om een persoonlijke notitie toe te voegen, wat een privémemo is voor je eigen referentie om je te helpen de transactie later te identificeren. Deze notitie wordt niet gedeeld met de ontvanger.


Omgekeerd, als het betalingsverzoek dat je scant of plakt al alle nodige details bevat, zoals een BIP21 URI met een vooraf bepaald bedrag, zal de wallet het gegevensinvoerscherm omzeilen en je rechtstreeks naar het bevestigingsscherm brengen om de betaling te autoriseren.


![image](assets/en/14.webp)


Voordat je transactie wordt uitgezonden, krijg je een bevestigingsscherm te zien. Het is van cruciaal belang dat je even de tijd neemt om elke parameter zorgvuldig te bekijken, waarbij je veel aandacht besteedt aan het adres van de ontvanger, het bedrag dat wordt verzonden en de netwerkkosten. Dit scherm biedt ook krachtige hulpmiddelen om je transactie aan te passen.


Je kunt de kosten op twee manieren regelen. De eerste methode is het selecteren van een gewenste transactiesnelheid, zoals laag, medium of hoog, en de wallet berekent automatisch de juiste vergoeding voor je. De tweede methode biedt een preciezere controle door je een specifieke vergoeding te laten instellen, hetzij als een absoluut totaal in satoshi's of als een relatief tarief per byte, dat vervolgens een geschatte bevestigingstijd oplevert.


Voor geavanceerde gebruikers biedt de wallet verschillende instellingen om de transactie nauwkeurig af te stellen. `Replace-by-Fee` (RBF) is standaard  ingeschakeld, wat een waardevolle functie is waarmee je een transactie kunt versnellen als deze vastloopt in de mempool door deze opnieuw uit te zenden met een hogere vergoeding. Je kunt ook handmatig kiezen uit welke `Unspent Transaction Outputs` (UTXOs) je wilt uitgeven. Dit is een krachtig hulpmiddel voor UTXO consolidatie, een strategie waarbij je meerdere kleine inputs combineert tot één grotere. Hoewel dit meer kosten met zich meebrengt voor de huidige transactie, kan het de kosten voor toekomstige transacties aanzienlijk verlagen, vooral als de netwerkkosten naar verwachting zullen stijgen.


![image](assets/en/15.webp)


PayJoin wordt automatisch geactiveerd als je een betalingsverzoek van een ontvanger scant (een BIP21 URI) met een `pj=` parameter. Als je gewoon een adres plakt zonder extra parameters, wordt deze functie niet geactiveerd. Deze collaboratieve methode verbetert de privacy door de input van zowel de verzender als de ontvanger te combineren, waardoor de heuristiek van gemeenschappelijk input-eigendom wordt doorbroken en er in sommige omstandigheden ook beter kan worden geschaald en kosten kunnen worden bespaard.


### Verzenden naar het Liquid Network


Het `Liquid Network` is ontworpen voor snelle, vertrouwelijke transacties met minimale kosten. Wanneer je geld verstuurt via Liquid, wordt het opgenomen uit je `Instant Payments Wallet`. Het proces is eenvoudig: je hoeft alleen maar het `Liquid` adres van de ontvanger in te voeren of te scannen.


Als het adres geen bedrag opgeeft, wordt je gevraagd om er een op te geven op het verzendscherm. Je kunt het bedrag invoeren in BTC, satoshis of fiat. Een belangrijk voordeel van Liquid is de lage minimumdrempel. Net als bij on-chain transacties, kun je een optionele persoonlijke notitie toevoegen voor je eigen administratie. Als het betalingsverzoek al een bedrag bevat, gaat de wallet direct door naar het bevestigingsscherm.


Bekijk de details van je Liquid-transactie op het bevestigingsscherm. De kosten zijn bijzonder laag en worden berekend op basis van de complexiteit van de transactie. Ze liggen meestal rond de 0,1 sat/vB, wat voor een eenvoudige transactie neerkomt op slechts 20-40 satoshis (bijvoorbeeld 26 satoshis op 21 december 2025).


![image](assets/en/16.webp)


### Verzenden naar het Lightning Network


Je kunt een Lightning-adres scannen (bijv. `runningbitcoin@rizful.com`) waarmee je het bedrag en een optionele notitie voor de ontvanger kunt instellen, of een factuur met een vooraf gedefinieerd bedrag scannen, waarmee je direct naar het bevestigingsscherm gaat.


*Houd er rekening mee dat er minimumbedragen en kosten van toepassing zijn.*


De Bull Bitcoin-wallet neemt geld uit je `Instant Payments Wallet` (op Liquid) en wisselt dit via `Boltz` om Lightning-betalingen te versturen. Deze hybride benadering is volledig self-custodial en vermijdt de hoge on-chain kosten voor het beheren van een speciaal Lightning-kanaal, maar vereist wel het betalen van `swapkosten`. Stuur voor de laagste kosten rechtstreeks naar het Liquid-adres van een ontvanger als deze ook een Bull Bitcoin-wallet gebruikt.


## geld overboeken tussen je wallets


Bull Bitcoin maakt het mogelijk om je Bitcoin te verplaatsen tussen je `Secure Bitcoin Wallet` en je `Instant Payments Wallet` op het Liquid Network of naar een `externe wallet`. Om een overschrijving uit te voeren, navigeer je gewoon naar de `Transfer` sectie, selecteer je de bron- en doelwallet, voer je het bedrag in dat je wilt verplaatsen en bevestig je de transactie.


![image](assets/en/17.webp)


## 1️⃣1️⃣ Je Bull Bitcoin-wallet herstellen


Dit hoofdstuk legt uit hoe je weer toegang krijgt tot je Bull Bitcoin-wallet fondsen als je je apparaat verliest, de app verwijdert, of gewoon naar een nieuw apparaat moet overschakelen. Zoals eerder uitgelegd, zijn er twee primaire methoden voor herstel: met de unieke `Recoverbull` methode en met een standaard `BIP39 seed zin`.


### Methode 1: Recoverbull


Recapitulatie: wallet back-ups worden lokaal versleuteld. Het versleutelde bestand kan opgeslagen worden in een cloud opslag, of op een ander apparaat. De encryptie sleutel wordt opgeslagen door de Recoverbull Key Server. Beide worden apart gehouden en moeten gecombineerd worden om een wallet te herstellen.


Om te beginnen wis ik de wallet met alle fondsen erop en installeer ik de wallet opnieuw. We komen weer op het welkomstscherm. Selecteer deze keer de optie `Recover Wallet`. Navigeer vervolgens naar de `Encrypted Vault` methode, bevestig het gebruik van de `Default Key server` en selecteer de locatie van de `Vault provider` waar je het back-up bestand hebt opgeslagen.


![image](assets/en/18.webp)


Er staat dat de kluis met succes is geïmporteerd. Tik op de knop `Decrypt Vault` en voer de `PIN` in. Het volgende scherm toont je `saldi` en het `aantal transacties` dat is hersteld.


![image](assets/en/19.webp)


### Methode 2: herstelzin (seed phrase)


Deze methode gebruikt de master herstelzin van je wallet, een standaard lijst van 12 woorden die dient als ultieme back-up voor je fondsen. Het is de meest universele manier om een Bitcoin-wallet te herstellen, omdat het niet gebonden is aan een specifieke dienst of server. Zolang je deze zin hebt, kun je je wallet herstellen op elk compatibel apparaat, zelfs zonder toegang tot de Bull Bitcoin Keyserver.


Selecteer in het welkomstscherm `Recover wallet`. Kies deze keer de `Physical backup` methode. De app toont een raster van woorden. Selecteer zorgvuldig elk woord van je 12-woorden herstelzin in de juiste volgorde. Wees nauwgezet, want één foutje resulteert in een onjuiste wallet.


## 1️⃣2️⃣ Een Hardware wallet aansluiten


Voor het hoogste niveau van veiligheid kiezen veel Bitcoin-gebruikers ervoor om hun geld op te slaan in `cold storage`. Dit betekent dat de `privésleutels` die je Bitcoin controleren op een apparaat bewaard worden dat nooit met het internet verbonden is. Een `hardware wallet` (of signing device) is een gespecialiseerd fysiek apparaat dat precies voor dit doel is ontworpen. Het fungeert als een digitale kluis voor je sleutels en zorgt ervoor dat ze nooit worden blootgesteld aan de potentiële bedreigingen van een online computer of smartphone.


Door een hardware wallet aan te sluiten op de Bull Bitcoin app, krijgt je het beste van twee werelden: de compromisloze veiligheid van cold storage voor je privésleutels, gecombineerd met de krachtige functies en gebruiksvriendelijke interface van de Bull Bitcoin-wallet voor het bekijken van saldi en het beheren van transacties. In dit laatste hoofdstuk laten we zien hoe je een hardware wallet, zoals een [Coldcard Q](https://coldcard.com/q), op je Bull Bitcoin-wallet aansluit. Deze tutorial gaat niet dieper in op het instellen van een Coldcard Q; dat kun je hier leren:


https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### Een wallet importeren


![image](assets/en/26.webp)


Selecteer eerst in het hoofdmenu van je Coldcard Q `Export wallet` en kies dan `Bull wallet`. Je Coldcard zal een QR code genereren.


![image](assets/en/20.webp)


Open de Bull Bitcoin-wallet en navigeer naar `Settings` > `Bitcoin Settings` > `Import wallet` en selecteer `Coldcard Q` op je telefoon en tik op `Open the camera` om deze QR-code te scannen om de publieke sleutels van je hardware wallet te importeren.


![image](assets/en/21.webp)


### Ontvangen met Coldcard Q


Om Bitcoin te ontvangen via je aangesloten Coldcard Q, hoeft het apparaat niet fysiek verbonden te zijn met je telefoon. De Bull Bitcoin-wallet heeft de benodigde publieke sleutels al geïmporteerd, waardoor het zelfstandig  ontvangstadressen kan genereren.


1. Tik op je geïmporteerde Coldcard Q wallet en selecteer `Receive`.

2. De app zal automatisch een vers Bitcoin adres weergeven van de wallet van je Coldcard.

3. Gebruik dit adres om geld te ontvangen. De Bitcoin wordt direct beveiligd met de sleutels van de hardware wallet, ook al was het apparaat offline tijdens het proces.


![image](assets/en/22.webp)


### Verzenden met Coldcard Q


Het verzenden van Bitcoin met je Coldcard Q vereist je fysieke bevestiging om elke transactie te autoriseren. Hoewel de Bull wallet app wordt gebruikt om de transactie op te bouwen, kan de uiteindelijke handtekening alleen worden aangemaakt op de hardware wallet zelf.


Open om te beginnen je `Coldcard Q` wallet en tik op `Versturen`. Open vervolgens de camera om de QR-code van het ontvangstadres te scannen. Na het scannen voer je het `bedrag` in dat je wilt versturen en pas je de `kostenprioriteit` aan als dat nodig is.


Voor meer opties kun je kijken onder Advanced Settings. Hier vind je de optie `Replace by Fee` (RBF), die standaard geactiveerd is en waarmee je een vastgelopen transactie later kunt versnellen. Je hebt ook de `Coin Control` optie, waarmee je handmatig de specifieke UTXO's kunt selecteren die je wilt uitgeven.


Zodra je alle details hebt bekeken, tik je op `Show PSBT` om de transactie voor te bereiden.


![image](assets/en/23.webp)


Tik op de `Scan` knop op je Coldcard Q en gebruik de camera om de QR code op je telefoon te scannen. Het Coldcard scherm toont je vervolgens alle transactie details. Controleer zorgvuldig het bedrag, het adres van de ontvanger en je wisselgeldsadres. Als alles correct is, druk dan op de `Enter` knop op de Coldcard Q om de transactie te ondertekenen. Vervolgens verschijnt er een QR code van de ondertekende transactie op het scherm.


![image](assets/en/24.webp)


Tik op de Bull wallet op `I'm done`, tik vervolgens op de `Camera` knop om de QR-code van de `ondertekende transactie` te scannen van je Coldcard Q. De Bull wallet toont nu een overzichtsscherm van de ondertekende transactie. Controleer het nog een laatste keer en tik dan op `Broadcast Transactie`. Dit rondt het proces af door de transactie naar het Bitcoin-netwerk te sturen, en je geld is onderweg.


## 🎯 Conclusie


Je hebt nu je reis door de Bull Bitcoin-wallet voltooid. De app brengt krachtige privacy- en beveiligingstools binnen handbereik, waardoor geavanceerde functies eenvoudig te gebruiken zijn. Het helpt je privé te blijven met functies zoals `PayJoin`, dat je transacties verbergt op de blockchain, en `Tor integratie`, dat je netwerkactiviteit maskeert voor nieuwsgierige ogen. Voor degenen die ultieme controle willen, kun je verbinding maken met je `eigen persoonlijke Bitcoin node` om niet meer afhankelijk te zijn van servers van derden, en een `Hardware wallet` gebruiken om je privésleutels volledig offline en veilig te bewaren. Met slimme back-upopties en naadloze ondersteuning voor Bitcoin, Liquid en Lightning is de Bull Bitcoin-wallet een sterke, alles-in-één keuze voor iedereen die zijn geld privé, veilig en volledig onder eigen controle wil houden.


## 📚 Bull Wallet tools


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Website ](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)
