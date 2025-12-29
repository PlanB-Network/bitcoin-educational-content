---
name: Bull Bitcoin Wallet
description: Ontdek hoe je de Wallet Bull Bitcoin gebruikt
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*Deze videotutorial van BTC Sessions leidt je door het proces van het instellen en gebruiken van Bull Bitcoin Wallet!


Deze handleiding neemt je mee door de installatie, configuratie en het gebruik van Bull Bitcoin Wallet. Je leert geld verzenden en ontvangen op de Bitcoin On-Chain, Liquid en Lightning netwerken, en hoe je de Bitcoin daartussen kunt verplaatsen. De uitgebreide functies van de wallet maken het een krachtige, alles-in-één tool voor het beheren van uw Bitcoin. Laten we aan de slag gaan.


## Inleiding


Bull Bitcoin Wallet, ontwikkeld door [Bull Bitcoin](https://www.bullbitcoin.com/), is een **zelfbehoudende** Bitcoin wallet, wat betekent dat je volledige controle hebt over je privésleutels en dus je fondsen, zonder afhankelijk te zijn van een derde partij. Open-source en geworteld in een Cypherpunk filosofie, combineert deze Wallet eenvoud, vertrouwelijkheid en geavanceerde functies zoals cross-network swaps en PayJoin ondersteuning. Je kunt je bitcoins op drie netwerken beheren: **Bitcoin onchain**, **Liquid** en **Lightning**, elk op maat gemaakt voor specifiek gebruik. Op de [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49), kunt u de huidige onderwerpen en komende ontwikkelingen bekijken. Aangezien het project 100% open-source is en "gebouwd in het openbaar", kun je ook je suggesties en bugs die je tegenkomt opsturen. Terwijl sommige wallets nu meerdere netwerken ondersteunen, onderscheidt de Bull Bitcoin Wallet zich door de diepgaande integratie van privacyfuncties over al deze netwerken, waardoor het een krachtig hulpmiddel is voor het beheren van je Bitcoin over alle grote netwerken


## 1️⃣ Vereisten


Voordat u de **Bull Bitcoin Wallet** in gebruik neemt, moet u ervoor zorgen dat u de volgende onderdelen hebt:



- Compatibele smartphone**: Een **iOS** (iPhone of iPad) of **Android** apparaat
- Internetverbinding
- Veilige back-upmedia**: Schrijf je **herstelzin** (12 woorden) op papier of metaal en bewaar deze op een veilige plaats.
- Basiskennis**: Een minimum aan kennis van Bitcoin concepten (adressen, transacties, kosten) is nuttig, hoewel deze tutorial elke stap uitlegt voor beginners.


## 2️⃣ Installatie


Je kunt de applicatie installeren via:



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(voor iOS-apparaten)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) (voor Android-apparaten)


Android-gebruikers hebben ook alternatieve opties:



- Download de APK rechtstreeks van de [GitHub Releases](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) pagina of
- Installeren via de Nostr-compatibele [Zapstore] (https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap)


Volg na het installeren van de applicatie het welkomstscherm om je account te configureren.


## 3️⃣ Eerste configuratie


Bij het openen worden de volgende opties gevraagd:



- `Maak nieuw Wallet`
- `Recover Wallet` en
- `Geavanceerde opties`


Laten we beginnen door op `Geavanceerde opties` te tikken.


Hier kunnen we de geavanceerde instellingen configureren voordat we een wallet aanmaken of herstellen:


1. Schakel de `Tor proxy` in om verkeer over het Tor-netwerk te routeren.

1. [Orbot-app](https://orbot.app/en/) moet geïnstalleerd en actief zijn voordat u deze inschakelt

2. Tor Proxy is alleen van toepassing op Bitcoin (niet Liquid) en kan resulteren in een langzamere verbinding.

2. Een `Aangepaste Electrum Server` instellen, of

3. Pas de `Recover Bull` instellingen aan. We zullen later meer leren over de [Recover Bull] (https://recoverbull.com/).


Nadat u alle optionele aanpassingen hebt gemaakt, tikt u op `Gedaan`. Als u een bestaande Wallet opnieuw wilt gebruiken, klik dan op `Herstel Wallet` en vul de 12 woorden van uw herstelzin in.


Klik anders op `Maak een nieuwe Wallet`.


![image](assets/en/01.webp)


## 4️⃣ beginscherm


Voordat we dieper duiken, kijken we eerst naar het `Home scherm` om ons te oriënteren:



- het `transactieoverzicht` en `instellingsmenu` bevinden zich bovenaan.
- Het `Beschikbaar Saldo` heeft een privacy-optie die `aan of uit` kan worden gezet.
- Ga naar de `Bitcoin Bull Exchange` om te `Kopen, Verkopen of Betalen` (dit hangt af van de jurisdictie en kan KYC vereisen).
- overdracht` van fondsen tussen portemonnees
- `Veilig Bitcoin` is gelijk aan Onchain Bitcoin Wallet
- `Instant payments` via de Lightning- / Liquid Network *(Opmerking: Bull Bitcoin Wallet maakt het mogelijk betalingen te doen en te ontvangen via Lightning. Fondsen ontvangen via Lightning worden opgeslagen op het [*Liquid netwerk](https://liquid.net/) (in de Wallet Instant Payments) dankzij een automatische swap via [*Boltz exchange](https://boltz.exchange/). Dit geeft u de mogelijkheid om te communiceren met Lightning zonder liquiditeitskanalen te hoeven beheren, terwijl u in zelfbewaarneming blijft.)*
- `Versturen` en `Ontvangen` van fondsen


![image](assets/en/02.webp)


Laten we eerst een aantal belangrijke configuraties maken en beginnen met `Backup`.


## 5️⃣ Back-up


Om het back-upproces te starten, tik je op het `gear icoon (⚙)` in de rechterbovenhoek van de app en selecteer je `Wallet Backup`. Je krijgt twee methoden te zien om je wallet te beveiligen: `Encrypted Vault` en `Physical Backup`. Laten we ze verkennen.


![image](assets/en/03.webp)


### Fysieke back-up


Tik op `Physical Backup` om een lijst van 12 woorden te zien die jouw herstel- of seed zin vertegenwoordigen. Overweeg het volgende:



- Schrijf je `herstelzin` met de grootste zorg op. Schrijf het op papier of metaal en bewaar het op een veilige plaats (kluis, offline locatie). Deze zin is uw enige manier om toegang te krijgen tot uw bitcoins in het geval van verlies van uw apparaat of verwijdering van de applicatie.
- Het is ook belangrijk om te weten dat iedereen met deze zin al je bitcoins kan stelen. Sla het nooit digitaal op:
- Geen screenshot
- Geen cloud-, e-mail- of berichtenback-ups
- Geen kopiëren/plakken (risico van opslaan op klembord)


![image](assets/en/25.webp)


Op het volgende scherm moet je de woorden in de juiste volgorde zetten om er zeker van te zijn dat je de seed zin goed hebt. Je krijgt een bevestiging als de test geslaagd is.


! **Dit punt is cruciaal**. Voor verdere hulp :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### Gecodeerde kluis


Er is ook de optie van een versleutelde, anonieme back-up in de cloud. Maar zeiden we in de vorige paragraaf niet dat cloudback-ups riskant zijn en vermeden moeten worden? Het Bull Bitcoin team heeft echter een slimme manier ontwikkeld om het proces veilig te maken. Dit is hoe het werkt:


`Recoverbull` is een back-upprotocol dat het beveiligen van uw Bitcoin wallet vereenvoudigt door de back-up in twee delen op te splitsen. Ten eerste wordt het back-upbestand van je wallet versleuteld op je apparaat met behulp van een sterke versleutelingscode. Je kunt dit versleutelde bestand opslaan waar je maar wilt, zoals Google Drive of je apparaat. Ten tweede, de coderingssleutel die nodig is om het bestand te ontgrendelen is opgeslagen door de Recoverbull Key Server. Om uw wallet te herstellen, heeft u zowel het versleutelde back-up bestand als de sleutel nodig, die u opent met uw PIN-code of wachtwoord. Dit ontwerp zorgt ervoor dat uw cloud back-up alleen nutteloos is en dat de sleutel server alleen nutteloos is zonder uw specifieke back-up bestand. Hierdoor blijven uw fondsen veilig, zelfs als één onderdeel is gecompromitteerd.


Zie het als een kluis. Het versleutelde back-up bestand is de *box*, die u overal kunt opslaan (zoals Google Drive). Uw Recovery PIN is de *sleutel*, die apart wordt opgeslagen door de Recoverbull Key Server. Een dief zou zowel uw specifieke doos als uw specifieke sleutel moeten hebben om het te openen. Dit ontwerp zorgt ervoor dat zelfs als iemand uw back-up bestand krijgt, het nutteloos is zonder de sleutel van de server, en de sleutel van de server is nutteloos zonder uw unieke back-up bestand.


Leer meer over het `Recoverbull` wallet back-upprotocol [hier] (https://recoverbull.com/).


Tik op `Gecodeerde kluis` en vervolgens op `Doorgaan` om het gebruik van de Standaardserver te bevestigen. De verbinding wordt omgeleid via het `Tor` Netwerk om privacy en anonimiteit te garanderen.


**Inzicht in uw pincodes**



- `App Unlock PIN`**:** De optionele PIN die is ingesteld in `Instellingen > Beveiligings-PIN` om de app op uw telefoon te vergrendelen.
- `Recovery PIN`**:** De verplichte PIN die is aangemaakt tijdens het `Encrypted Vault` back-upproces en die wordt gebruikt om uw back-upbestand te decoderen tijdens het herstel.


Dit zijn twee afzonderlijke PIN-codes. Vergeet uw Herstel PIN niet, want deze is essentieel voor het herstellen van uw wallet."


**Recovery PIN instellen:**



- U moet een PIN-code of wachtwoord aanmaken om weer toegang te krijgen tot uw wallet.
- De PIN-code / het wachtwoord moet minstens 6 cijfers lang zijn (vermijd bijvoorbeeld eenvoudige reeksen zoals 123456, die niet worden geaccepteerd).
- Zonder deze PIN is wallet herstel onmogelijk.


Selecteer vervolgens een vault provider:



- google Drive` of
- een `gekozen locatie` (bijvoorbeeld uw apparaat)


![image](assets/en/04.webp)


Sla nu het `back-up bestand` op. Tik vervolgens op `Test herstel`, selecteer je opgeslagen back-upbestand of kluis en tik op `Kluis ontsleutelen`. Voer je `PIN` of `Wachtwoord` in. Als alles werkt, verschijnt het scherm `Test succesvol voltooid`.


### Labels importeren/exporteren


Nu we onze Back-up hebben gemaakt, gaan we eens kijken naar `labels`.  De Bull Bitcoin wallet verbetert de privacy en organisatie door gebruikers in staat te stellen aangepaste labels te maken voor hun ontvangstadressen en transacties. Deze labels helpen je bij het categoriseren van je geld, omdat transacties die naar een gelabeld adres worden gestuurd, dat label overnemen, en je kunt ook uitgaande transacties labelen om hun verandering bij te houden. De wallet ondersteunt de [BIP-329] (https://bip329.org/) standaard volledig, wat betekent dat u al uw labels naar een bestand kunt exporteren en in een andere wallet kunt importeren. Deze functie zorgt ervoor dat u naadloos een back-up kunt maken van uw transactiegeschiedenis en categorisaties, of deze kunt migreren tussen verschillende instanties van de wallet, zonder uw persoonlijke organisatie te verliezen.


![image](assets/en/05.webp)


## 6️⃣ Instellingen


Nu je primaire back-up veilig is gesteld, gaan we de andere functies in de instellingen verkennen.


### A - Toegang beveiligen


Om de app te beveiligen, navigeer naar `Instellingen` en kies `Beveiligings-PIN` om een PIN-code te selecteren. Maak een sterke PIN-code aan om de toegang tot uw wallet te vergrendelen. Hoewel deze stap optioneel is, wordt het sterk aanbevolen om onbevoegde toegang te voorkomen als iemand anders uw telefoon gebruikt.


![image](assets/en/06.webp)


### B - Verbinding met een persoonlijk knooppunt (optioneel)


De Wallet BullBitcoin maakt standaard verbinding met Electrum servers: de eerste wordt beheerd door Bull Bitcoin en een secundaire server van Blockstream, die beide geen logs bijhouden, waardoor het risico op tracering kleiner is.


Voor meer vertrouwelijkheid kunt u de applicatie verbinden met uw eigen Bitcoin knooppunt via een Electrum server. Tik hiervoor op `Instellingen` > `Bitcoin Instellingen` > `Electrum Server Instellingen`, tik vervolgens op `+ Aangepaste server toevoegen` om het adres en de gegevens van uw server in te voeren.


![image](assets/en/07.webp)


### C - Valuta


Het beschikbare saldo wordt op het hoofdscherm weergegeven in zowel `sats` als `USD`. Om dit te veranderen, ga je naar `Instellingen` > `Munteenheid`. Daar kun je wisselen tussen `sats/BTC` en je `standaard fiatvaluta` selecteren.


![image](assets/en/08.webp)


### D - Bitcoin Instellingen


Het menu `Bitcoin Instellingen` biedt diepgaande toegang tot de kernconfiguraties en -gegevens van je wallet. Hier kun je de fundamentele details van je `Secure Bitcoin` en `Instant payments wallets` bekijken. Hier kunt u de fundamentele details van uw `Secure Bitcoin` en `Instant payments wallets` bekijken, waardoor u volledige transparantie en controle heeft. De belangrijkste functies in dit menu zijn:



- Wallet Details:** Navigeer naar uw Beveiligde Bitcoin of Directe betalingen wallet om specifieke informatie te bekijken.
- Wallet vingerafdruk:** Een unieke identificatie voor uw wallet.
- Publieke sleutel (Pubkey):** De sleutel die gebruikt wordt om generate uw Bitcoin ontvangstadressen te geven.
- Descriptor:** Een technische samenvatting van de structuur van je wallet.
- Afleidingspad:** Het specifieke pad dat wordt gebruikt om generate alle adressen van je privésleutel af te leiden.
- Address bekijken:** Bekijk een lijst met uw ongebruikte ontvangstadressen en wijzig adressen (verschijnt binnenkort)


Bovendien heb je de optie om:



- `Enable Auto Transfer` instellingen om een maximum direct wallet saldo in te stellen, dat vervolgens automatisch wordt overgeboekt naar de beveiligde bitcoin wallet.
- Generieke portemonnees importeren via `Mnemonic` zin of `watch-only` importeren
- Verbind `Hardware wallets`: momenteel worden ColdcardQ, SeedSigner, Specter, Krux, Blockstream Jade en Foundation Passport ondersteund


## 7️⃣ Bull Bitcoin Exchange


Direct vanuit de wallet heb je toegang tot de [Bull Bitcoin exchange] (https://www.bullbitcoin.com/), zodat je Bitcoin kunt kopen, verkopen en betalen zonder de app te verlaten. Deze integratie biedt een handige oplossing voor het beheren van uw Bitcoin behoeften. Houd er rekening mee dat de toegang tot de beurs en de diensten beperkt kan zijn, afhankelijk van uw jurisdictie, en dat het voltooien van een KYC-verificatie (Know Your Customer) vereist kan zijn om te voldoen aan de wettelijke normen en gebruik te maken van alle functies van het platform.


Om te beginnen tikt u op `Exchange` in de rechterbenedenhoek en vervolgens op `Sign up` of `Login` voor uw account.


De beurs biedt de volgende [functies] (https://www.bullbitcoin.com/):



- Bitcoin kopen met zelfbehoud van je bankrekening
- Niet-vrijheidsberovende
- Particulieren of bedrijven
- Onmiddellijke opname
- Geen verborgen kosten
- Lightning Network beschikbaar
- Geen transactielimieten
- Terugkerende koopopties


![image](assets/en/09.webp)


Ga voor meer informatie naar deze tutorial:


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣ Geld ontvangen


Geld ontvangen met **Bull Bitcoin Wallet** is eenvoudig en flexibel, met ondersteuning voor drie verschillende netwerken, op maat gemaakt voor verschillende gebruikssituaties:



- Het `Bitcoin (onchain)` netwerk voor veilige, langdurige opslag.
- Het `Liquid` netwerk voor snelle, meer vertrouwelijke transacties.
- Het `Lightning` netwerk voor directe, goedkope betalingen.


De app genereert automatisch het juiste adres of de juiste factuur op basis van je geselecteerde netwerk. Hier lees je hoe je te werk gaat voor elk netwerk.


### Ontvangen via Onchain (Bitcoin netwerk)


Om on-chain fondsen te ontvangen, kun je ofwel de `Veilig Bitcoin Wallet` op het Beginscherm selecteren en op `Ontvangen` tikken, of op de hoofdknop `Ontvangen` tikken en dan het `Bitcoin netwerk` kiezen.


Je hebt twee primaire modi voor het genereren van een ontvangstadres:


**Standaardmodus (URI met extra invoerparameters)


Standaard genereert de wallet een [BIP21 URI] (https://bips.dev/21/). Dit is een gestandaardiseerd formaat dat meer informatie verpakt dan een eenvoudig adres, waaronder een bedrag, een persoonlijke notitie en PayJoin parameters om de privacy te verbeteren. Deze uitgebreide URI wordt gecodeerd in een QR-code en beschikbaar gesteld om te kopiëren. Het formaat ziet er als volgt uit: `bitcoin:<adres>?<parameter1>=<waarde1>&<parameter2>=<waarde2>`.



- Extra invoerparameters:**
    - Bedrag:** Geef een gevraagd bedrag op in BTC, sats of een fiatvaluta.
    - Bericht:** Voeg een persoonlijke notitie toe die zichtbaar is voor de afzender.
    - PayJoin:** Schakel deze optie in om de privacy te verbeteren door de input van zowel de verzender als de ontvanger te combineren in de transactie.


Voorbeeld URI:


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


*Belangrijke opmerking: Stuur geen geld naar de adressen in deze tutorial, de wallet zal worden verwijderd.*


![image](assets/en/10.webp)


**Kopieer of scan alleen Address optie ingeschakeld


Met de `Kopieer of scan alleen Address optie` ingeschakeld, genereert de applicatie een eenvoudig Bitcoin adres in SegWit (bech32) formaat.


Voorbeeld:


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


Zelfs als je een bedrag of een notitie invoert, worden deze niet opgenomen in de QR-code of het gekopieerde adres.


![image](assets/en/11.webp)


### Ontvangen via de Liquid Network


Je kunt een betaling ontvangen op de Liquid Network. Eenmaal op het `Ontvangen` scherm, heb je dezelfde twee opties om een betalingsverzoek te genereren:


**1. Eenvoudige Address:** Kopieer het standaard `Liquid adres`. Dit is een unieke identificatie voor je wallet op het Liquid netwerk en bevat geen specifiek bedrag of bericht.


Voorbeeld Address:


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2. Gedetailleerd betalingsverzoek (URI):** Voor een meer gestructureerd verzoek kun je een bedrag en een persoonlijke notitie opgeven. Deze informatie wordt automatisch gecodeerd in een deelbare URI en de bijbehorende QR-code.



- Bedrag:** Je kunt het bedrag instellen in Bitcoin (BTC), Satoshis (Sats) of een fiatvaluta.
- Opmerking:** Voeg een persoonlijk bericht toe om de transactie te identificeren.


**Voorbeeld URI:**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


Om de transactie te voltooien, geef je de afzender het `adres` of de `URI`. Je kunt dit doen door het naar je klembord te kopiëren of door ze de QR-code rechtstreeks vanaf je scherm te laten scannen.


![image](assets/en/12.webp)


### Ontvangen via Lightning



Met de Bull Bitcoin Wallet kun je ook betalingen verzenden en ontvangen via de Lightning Network. Een belangrijk kenmerk is dat geld dat je via Lightning ontvangt automatisch wordt omgewisseld en opgeslagen op de `Liquid Network` binnen je `Instant Payments Wallet`. Deze dienst wordt aangedreven door de `Boltz`. Door dit ontwerp kunt u profiteren van de snelheid en lage kosten van Lightning zonder de complexiteit van het beheren van liquiditeitskanalen, terwijl u uw fondsen volledig zelf bewaart. Hoewel deze hybride benadering self-custodial is en de complexiteit van het beheren van kanalen vermijdt, introduceert het een dienst van een derde partij (Boltz), een kleine swapvergoeding en afhankelijkheid van de Liquid Network federatie van functionarissen als keyholders, wat anders is dan een traditionele, niet-custodial Lightning wallet waar u uw eigen kanalen beheert. Je kunt hier meer te weten komen over Liquid en hun bestuursmodel:


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- Grenzen:**
    - Minimumbedrag:** Een minimumfactuurbedrag is vereist. Controleer de app voor de huidige limiet
    - Kosten:** Jij, de ontvanger, bent verantwoordelijk voor een kleine swapvergoeding. Deze kosten worden afgetrokken van het bedrag dat de verzender overmaakt en kunnen veranderen
- Voordelen:**
    - Zelfbeheerd:** Uw geld is altijd onder uw controle, beveiligd op het Liquid-netwerk.
    - Vermijd hoge On-Chain kosten:** Door Lightning te gebruiken en op te slaan op Liquid, omzeilt u de on-chain kosten die gepaard gaan met het openen van een traditioneel Lightning-kanaal. U kunt ervoor kiezen om later geld over te hevelen naar een on-chain-kanaal, wanneer het geaccumuleerde bedrag de kosten rechtvaardigt.
    - Tip:** Voor de meest kosteneffectieve transactie tussen twee Bull Bitcoin gebruikers, gebruikt u het **Liquid netwerk rechtstreeks** om de Lightning swapkosten volledig te vermijden.


Om een betaling te ontvangen, moet je generate een `bliksemfactuur` hebben:


1. voer een bedrag in**:** Geef het bedrag op dat je wilt ontvangen in Bitcoin (BTC), Satoshis (Sats) of een fiatvaluta.

2. notitie toevoegen` **(Optioneel):** Voeg een memo of notitie toe. Deze wordt opgenomen in de factuur en weergegeven in je transactiegeschiedenis zodra de betaling is voltooid, zodat je deze gemakkelijker kunt identificeren.

3. `Invoice Geldigheid`**:** De Lightning-factuur is tijdsgevoelig en vervalt na **12 uur**. Als de factuur niet binnen deze periode wordt betaald, wordt deze ongeldig en moet u generate een nieuwe factuur maken.


Geef de factuur aan de verzender door hem naar je klembord te kopiëren of door hem de QR-code te laten scannen die op je scherm wordt weergegeven.


![image](assets/en/13.webp)


## 9️⃣ Geld versturen


Je kunt het verzendscherm rechtstreeks openen vanaf de startpagina of vanuit een van je portemonnees. Bull Bitcoin Wallet vereenvoudigt het proces door automatisch het bestemmingsnetwerk te detecteren - `Bitcoin`, `Liquid` of `Lightning` op basis van het adres of de factuur die je invoert, geplakt of gescand via een QR-code.


### On-Chain Verzending via het Bitcoin Netwerk


Geld overmaken via on-chain betekent dat uw transactie direct wordt geregistreerd op de Bitcoin blockchain. Deze methode is het beste voor grotere overschrijvingen of niet-tijdgevoelige overschrijvingen. Om te beginnen kun je rechtsonder op de `Verstuur Knop` tikken, en een `standaard Bitcoin adres` scannen of invoeren.


Als het adres dat je opgeeft geen specifiek bedrag bevat, wordt je gevraagd om de details in te vullen op het verzendscherm. Je kunt het bedrag opgeven in de eenheid van je voorkeur, zoals BTC, satoshis of een fiat equivalent. Je hebt ook de optie om een persoonlijke notitie toe te voegen, wat een privémemo is voor je eigen referentie om je te helpen de transactie later te identificeren. Deze notitie wordt niet gedeeld met de ontvanger.


Omgekeerd, als het betalingsverzoek dat je scant of plakt al alle nodige details bevat, zoals een BIP21 URI met een vooraf bepaald bedrag, zal de wallet het gegevensinvoerscherm omzeilen en je rechtstreeks naar het bevestigingsscherm brengen om de betaling te autoriseren.


![image](assets/en/14.webp)


Voordat je transactie wordt uitgezonden, krijg je een bevestigingsscherm te zien. Het is van cruciaal belang dat je even de tijd neemt om elke parameter zorgvuldig te bekijken, waarbij je veel aandacht besteedt aan het adres van de ontvanger, het bedrag dat wordt verzonden en de netwerkkosten. Dit scherm biedt ook krachtige hulpmiddelen om je transactie aan te passen.


Je kunt de kosten op twee manieren regelen. De eerste methode is het selecteren van een gewenste transactiesnelheid, zoals laag, medium of hoog, en de wallet berekent automatisch de juiste vergoeding voor je. De tweede methode biedt een preciezere controle door u een specifieke vergoeding te laten instellen, hetzij als een absoluut totaal in satoshi's of als een relatief tarief per byte, dat vervolgens een geschatte bevestigingstijd oplevert.


Voor geavanceerde gebruikers biedt de wallet verschillende instellingen om de transactie nauwkeurig af te stellen. standaard is `Replace-by-Fee` (RBF) ingeschakeld, wat een waardevolle functie is waarmee je een transactie kunt versnellen als deze vastloopt in de mempool door deze opnieuw uit te zenden met een hogere vergoeding. Je kunt ook handmatig kiezen uit welke `Unspent Transaction Outputs` (UTXOs) je wilt uitgeven. Dit is een krachtig hulpmiddel voor UTXO consolidatie, een strategie waarbij je meerdere kleine ingangen combineert tot één grotere. Hoewel dit meer kosten met zich meebrengt voor de huidige transactie, kan het de kosten voor toekomstige transacties aanzienlijk verlagen, vooral als de netwerkkosten naar verwachting zullen stijgen.


![image](assets/en/15.webp)


PayJoin wordt automatisch geprobeerd wanneer je een betalingsverzoek van een ontvanger scant (een BIP21 URI) dat een `pj=` parameter bevat. Als je gewoon een adres plakt zonder extra parameters, wordt deze functie niet geactiveerd. Deze collaboratieve methode verbetert de privacy door de input van zowel de verzender als de ontvanger te combineren, waardoor de heuristiek van gemeenschappelijk input-eigendom wordt doorbroken en er in sommige omstandigheden ook beter kan worden geschaald en kosten kunnen worden bespaard.


### Verzenden naar de Liquid Network


De `Liquid Network` is ontworpen voor snelle, vertrouwelijke transacties met minimale kosten. Wanneer je geld verstuurt via de Liquid, wordt het opgenomen uit je `Instant Payments Wallet`. Het proces is eenvoudig: je hoeft alleen maar het `Liquid` adres van de ontvanger in te voeren of te scannen.


Als het adres geen bedrag opgeeft, wordt je gevraagd om er een op te geven op het verzendscherm. Je kunt het bedrag invoeren in BTC, satoshis of fiat. Een belangrijk voordeel van Liquid is de lage minimumdrempel. Net als bij on-chain transacties, kun je een optionele persoonlijke notitie toevoegen voor je eigen administratie. Als het betalingsverzoek al een bedrag bevat, gaat wallet direct door naar het bevestigingsscherm.


Op het bevestigingsscherm voor een Liquid transactie bekijk je de details. De kosten zijn bijzonder laag en worden berekend op basis van de complexiteit van de transactie. Ze liggen meestal rond de 0,1 sat/vB, wat voor een eenvoudige transactie neerkomt op slechts 20-40 satoshis (bijvoorbeeld 26 satoshis per 21 december 2025).


![image](assets/en/16.webp)


### Verzenden naar de Lightning Network


Je kunt een Lightning Address scannen (bijv. `runningbitcoin@rizful.com`) waarmee je het bedrag en een optionele notitie voor de ontvanger kunt instellen, of een factuur met een vooraf gedefinieerd bedrag scannen, waarmee je direct naar het bevestigingsscherm gaat.


*Houd er rekening mee dat er minimumbedragen en kosten van toepassing zijn.*


De Bull Bitcoin Wallet verstuurt Lightning-betalingen door geld op te nemen uit uw `Instant Payments Wallet` (op Liquid) en dit om te wisselen via `Boltz`. Deze hybride benadering is volledig self-custodial en vermijdt de hoge on-chain kosten voor het beheren van een speciaal Lightning-kanaal, maar vereist wel het betalen van `swapkosten`. Stuur voor de laagste kosten rechtstreeks naar het Liquid adres van een ontvanger als deze ook een Bull Bitcoin wallet gebruikt.


## geld overboeken tussen uw portefeuilles


Bull Bitcoin maakt het mogelijk om je Bitcoin te verplaatsen tussen je `Secure Bitcoin` wallet en je `Instant Payments Wallet` op de Liquid Network of naar een `externe Wallet`. Om een overschrijving uit te voeren, navigeer je gewoon naar de `Overschrijving` sectie, selecteer je de bron- en doelportemonnee, voer je het bedrag in dat je wilt verplaatsen en bevestig je de transactie.


![image](assets/en/17.webp)


## 1️⃣1️⃣ Uw Bull Bitcoin Wallet herstellen


Dit hoofdstuk legt uit hoe je weer toegang krijgt tot je Bull Bitcoin Wallet fondsen als je je apparaat verliest, de app verwijdert, of gewoon naar een nieuw apparaat moet overschakelen. Zoals eerder uitgelegd, zijn er twee primaire methoden voor herstel: met de unieke `Recoverbull` methode en met een standaard `BIP39 seed zin`.


### Methode 1: Herstelbull


Recapitulatie: Wallet back-ups worden lokaal versleuteld. Het versleutelde bestand kan opgeslagen worden in een cloud opslag, of op een ander apparaat. De encryptie sleutel wordt opgeslagen door de Recoverbull Key Server. Beide worden apart gehouden en moeten gecombineerd worden om een wallet te herstellen.


Om te beginnen wis ik de Wallet met alle fondsen erop en installeer ik de wallet opnieuw. We komen weer op het `Welkom scherm`. Selecteer deze keer de optie `Wallet herstellen`. Navigeer vervolgens naar de `Encrypted Vault` methode, bevestig het gebruik van de `Default Key server` en selecteer de locatie of `Vault provider` waar je het back-up bestand hebt opgeslagen.


![image](assets/en/18.webp)


Er staat dat de kluis met succes is geïmporteerd. Tik op de knop `Kluis ontsleutelen` en voer de `PIN` in. Het volgende scherm toont je `saldi` en het `aantal transacties` dat is hersteld.


![image](assets/en/19.webp)


### Methode 2: Zaadzin


Deze methode gebruikt de master herstelzin van uw wallet, een standaard lijst van 12 woorden die dient als ultieme back-up voor uw fondsen. Het is de meest universele manier om een Bitcoin wallet te herstellen, omdat het niet gebonden is aan een specifieke dienst of server. Zolang je deze zin hebt, kun je je wallet herstellen op elk compatibel apparaat, zelfs zonder toegang tot de Bull Bitcoin keyserver.


Selecteer in het welkomstscherm `Recover Wallet`. Kies deze keer de `Physical backup` methode. De app toont een raster van woorden. Selecteer zorgvuldig elk woord van je 12-woorden seed zin in de juiste volgorde. Wees nauwgezet, want één foutje resulteert in een onjuiste wallet.


## 1️⃣2️⃣ Een Hardware Wallet aansluiten


Voor het hoogste niveau van veiligheid kiezen veel Bitcoin gebruikers ervoor om hun geld op te slaan in `cold storage`. Dit betekent dat de `private sleutels` die uw Bitcoin besturen op een apparaat bewaard worden dat nooit met het internet verbonden is. Een `hardware wallet` (of Signing device) is een gespecialiseerd fysiek apparaat dat precies voor dit doel is ontworpen. Het fungeert als een digitale kluis voor uw sleutels en zorgt ervoor dat ze nooit worden blootgesteld aan de potentiële bedreigingen van een online computer of smartphone.


Door een hardware wallet aan te sluiten op de Bull Bitcoin app, krijgt u het beste van twee werelden: de compromisloze veiligheid van koude opslag voor uw privésleutels, gecombineerd met de krachtige functies en gebruiksvriendelijke interface van de Bull Bitcoin wallet voor het bekijken van saldi en het beheren van transacties. In dit laatste hoofdstuk laten we zien hoe je een hardware wallet, zoals een [Coldcard Q] (https://coldcard.com/q), op je Bull Bitcoin wallet aansluit. Deze tutorial gaat niet dieper in op het instellen van een Coldcard Q; dat kun je hier leren:


https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### Een Wallet importeren


![image](assets/en/26.webp)


Selecteer eerst in het hoofdmenu van je Coldcard Q `Export Wallet` en kies dan `Bull Wallet`. Je Coldcard zal generate een QR code krijgen.


![image](assets/en/20.webp)


Open de Bull Bitcoin Wallet en navigeer naar `Instellingen` > `Bitcoin Instellingen` > `Import wallet` en selecteer `Coldcard Q` op uw telefoon en tik op `Open de camera` om deze QR-code te scannen om de publieke sleutels van uw hardware wallet te importeren.


![image](assets/en/21.webp)


### Ontvangen met Coldcard Q


Om Bitcoin te ontvangen via uw aangesloten Coldcard Q, hoeft het apparaat niet fysiek verbonden te zijn met uw telefoon. De Bull Bitcoin Wallet heeft de benodigde publieke sleutels al geïmporteerd, waardoor het zelfstandig generate adressen kan ontvangen.


1. Tik op uw geïmporteerde Coldcard Q ondertekeningsapparaat en selecteer `Ontvangen`.

2. De app zal automatisch een vers Bitcoin adres weergeven van de wallet van je Coldcard.

3. Gebruik dit adres om geld te ontvangen. De Bitcoin wordt direct beveiligd met de sleutels van de hardware wallet, ook al was het apparaat offline tijdens het proces.


![image](assets/en/22.webp)


### Verzenden met Coldcard Q


Het verzenden van Bitcoin met uw Coldcard Q vereist uw fysieke bevestiging om elke transactie te autoriseren. Hoewel de Bull Wallet app wordt gebruikt om de transactie op te bouwen, kan de uiteindelijke handtekening alleen worden aangemaakt op de hardware wallet zelf.


Open om te beginnen je `Coldcard Q` wallet en tik op `Versturen`. Open vervolgens de camera om de QR-code voor het ontvangende adres te scannen. Na het scannen voer je het `bedrag` in dat je wilt versturen en pas je de `kostenprioriteit` aan als dat nodig is.


Voor meer opties kun je kijken onder Geavanceerde instellingen. Hier vind je de optie `Vervangen door vergoeding` (RBF), die standaard geactiveerd is en waarmee je een vastgelopen transactie later kunt versnellen. Je hebt ook de `Coin Control` optie, waarmee je handmatig de specifieke UTXO's kunt selecteren die je wilt uitgeven.


Zodra je alle details hebt bekeken, tik je op `Toon PSBT` om de transactie voor te bereiden.


![image](assets/en/23.webp)


Tik op de `Scan` knop op uw Coldcard Q en gebruik de camera om de QR code op uw telefoon te scannen. Het Coldcard scherm toont u vervolgens alle transactie details. Controleer zorgvuldig het bedrag, het adres van de ontvanger en uw wijzigingsadres. Als alles correct is, druk dan op de `Enter` knop op de Coldcard Q om de transactie te ondertekenen. Vervolgens verschijnt er een QR code van de ondertekende transactie op het scherm.


![image](assets/en/24.webp)


Tik op de Bull wallet op `Ik ben klaar`, tik vervolgens op de `Camera` knop om de QR-code van de `ondertekende transactie` te scannen van uw Coldcard Q. De Bull wallet toont nu een overzichtsscherm van de ondertekende transactie. Controleer het nog een laatste keer en tik dan op `Transactie verzenden`. Dit rondt het proces af door de transactie naar het Bitcoin netwerk te sturen, en uw geld is onderweg.


## conclusie


Je hebt nu je reis door de Bull Bitcoin Wallet voltooid. De app brengt krachtige privacy- en beveiligingstools binnen handbereik, waardoor geavanceerde functies eenvoudig te gebruiken zijn. Het helpt je privé te blijven met functies zoals `PayJoin`, dat je transacties verbergt op de blockchain, en `Tor integratie`, dat je netwerkactiviteit maskeert voor nieuwsgierige ogen. Voor degenen die ultieme controle willen, kun je verbinding maken met je `eigen persoonlijke Bitcoin node` om niet meer afhankelijk te zijn van servers van derden, en een `Hardware wallet` gebruiken om je privésleutels volledig offline en veilig te bewaren. Met slimme back-upopties en naadloze ondersteuning voor Bitcoin, Liquid en Lightning is de Bull Bitcoin Wallet een sterke, alles-in-één keuze voor iedereen die zijn geld privé, veilig en volledig onder eigen controle wil houden.


## bull Wallet Hulpmiddelen


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Website ](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)