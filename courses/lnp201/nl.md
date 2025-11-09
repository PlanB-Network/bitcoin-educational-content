---
name: Lightning Network-theorie
goal: Ontdek de Lightning Network vanuit een technisch perspectief
objectives:
- Begrijp de werking van de kanalen van het netwerk.
- Maak jezelf vertrouwd met de termen HTLC, LNURL en UTXO.
- Het beheer van liquiditeit en de vergoedingen van het LNN gelijkstellen.
- Herken de Lightning Network als een netwerk.
- Het theoretische gebruik van de Lightning Network begrijpen.
---

# Een reis naar Bitcoin's tweede Layer


Duik in het hart van de Lightning Network, een essentieel systeem voor de toekomst van Bitcoin transacties. LNP201 is een theoretische cursus over de technische werking van Lightning. Het onthult de fundamenten en mechanismen van dit tweede Layer netwerk, ontworpen om Bitcoin betalingen snel, zuinig en schaalbaar te maken.


Dankzij het netwerk van betalingskanalen maakt Lightning snelle en veilige transacties mogelijk zonder elke Exchange op de Bitcoin Blockchain te registreren. Door de hoofdstukken heen leert u hoe het openen, beheren en sluiten van kanalen werkt, hoe betalingen veilig door tussenliggende knooppunten worden geleid terwijl de behoefte aan vertrouwen tot een minimum wordt beperkt, en hoe u liquiditeit beheert. Je zult ontdekken wat Commitment transacties, HTLC's, revocation keys, strafmechanismen, onion routing en facturen zijn.


Of je nu een Bitcoin beginner bent of een meer ervaren gebruiker, deze cursus biedt waardevolle informatie om de Lightning Network te begrijpen en te gebruiken. Hoewel we in de eerste delen een aantal basisprincipes van de werking van de Bitcoin behandelen, is het essentieel om de basisprincipes van de uitvinding van de Satoshi onder de knie te krijgen, voordat je in LNP201 duikt.


Geniet van je ontdekking!


+++

# Inleiding

<partId>9da7290a-3895-49a2-93ea-2a6272ca4af4</partId>


## Cursus Overzicht

<chapterId>f2e71062-5121-4114-a7f8-27df69884ce8</chapterId>


Welkom bij de LNP201 cursus!


Deze training is bedoeld om je een diepgaand technisch inzicht te geven in de Lightning Network, een overlay netwerk dat ontworpen is om snelle en vaak goedkope Bitcoin transacties mogelijk te maken. Je zult geleidelijk de fundamentele concepten ontdekken die dit systeem besturen, van het openen van betalingskanalen tot routeringstechnieken en liquiditeitsbeheer.


**Deel 1: Grondbeginselen**

We zullen beginnen met een algemene introductie tot Lightning Network, waarbij we essentiële fundamenten leggen over Bitcoin, de adressen, UTXO's en hoe transacties werken. Dit fundamentele overzicht is nodig om te begrijpen hoe de Lightning Network vertrouwt op de onderliggende Blockchain mechanismen om veilig te werken.


**Sectie 2: Kanalen openen en sluiten**

In dit gedeelte verkennen we het kanaalopeningsproces, dat de hoeksteen van Lightning Network is. Je zult leren hoe Commitment transacties aangemaakt worden, de rol van revocation keys voor beveiliging en hoe kanalen gezamenlijk of eenzijdig gesloten kunnen worden. Elke stap wordt nauwkeurig en technisch uitgelegd, zodat je alle subtiliteiten begrijpt.


**Deel 3: Een liquiditeitsnetwerk**

De Lightning Network is niet beperkt tot individuele kanalen; het is een echt betalingsnetwerk. We zullen zien hoe transacties kunnen worden gerouteerd via intermediaire knooppunten met behulp van HTLC's. In dit deel maak je ook kennis met de uitdagingen van inkomende en uitgaande liquiditeit.


**Deel 4: Lightning Network Gereedschappen**

In dit onderdeel worden praktische tools van de Lightning Network gepresenteerd, zoals *Facturen*, *LNURL* en *Keysend*. U leert ook hoe u de liquiditeit van uw kanalen beheert, een essentieel aspect om betalingen soepel te laten verlopen en de efficiëntie van uw transacties op Lightning te maximaliseren.


**Sectie 5: Verder gaan**

Tot slot sluiten we de training af met een recapitulatie van de behandelde concepten en maken we de weg vrij voor meer geavanceerde onderwerpen voor degenen die hun kennis van de Lightning Network willen verdiepen.


Klaar om de technische mechanismen van de Lightning Network te ontdekken? Laten we erin duiken!


---

*Hier zijn enkele termen die je in de cursusdiagrammen in het Engels zult tegenkomen, samen met hun vertaling om je te helpen ze beter te begrijpen in je eigen taal:*

| Engels             | Vertaling - uitleg            |
| ------------------ | ----------------------------- |
| *timelock*         | Tijdslot                      |
| *Revocation Key*   | Intrekkingssleutel            |
| *invoice*          | Factuur / betalingsverzoek    |
| *sig* (signature)  | Handtekening                  |
| *secret*           | Geheim                        |
| *amount*           | Bedrag                        |
| *scan QR code*     | QR-code scannen               |
| *Show QR code*     | QR-code tonen                 |
| *Asks the invoice* | Vraagt de factuur aan         |
| *Give the invoice* | Geeft de factuur              |
| *Payment*          | Betaling                      |
| *Preimage*         | Voorbeeld                     |

# De grondbeginselen


<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>


## De Lightning Network begrijpen


<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>


:::video id=4315a277-12fe-4946-bb49-a807e60c09a7:::



De Lightning Network is een netwerk van betalingskanalen gebouwd bovenop het Bitcoin protocol, met als doel snelle en goedkope transacties mogelijk te maken. Het maakt het creëren van betalingskanalen tussen deelnemers mogelijk, waarbinnen transacties vrijwel direct en met minimale kosten kunnen worden uitgevoerd, zonder dat elke transactie afzonderlijk op de Blockchain hoeft te worden geregistreerd. De Lightning Network probeert dus de schaalbaarheid van Bitcoin te verbeteren en het bruikbaar te maken voor laagwaardige betalingen.


Voordat we het "netwerk"-aspect gaan verkennen, is het belangrijk om het concept van een **betaalkanaal** op Lightning te begrijpen, hoe het werkt en wat de specifieke kenmerken ervan zijn. Dat is het onderwerp van dit eerste hoofdstuk.


### Het concept betalingskanaal


Met een betalingskanaal kunnen twee partijen, hier **Alice** en **Bob**, Exchange geld over de Lightning Network storten. Elke protagonist heeft een knooppunt, gesymboliseerd door een cirkel, en het kanaal tussen hen wordt weergegeven door een lijnstuk.


![LNP201](assets/en/001.webp)


In ons voorbeeld heeft Alice 100.000 satoshi's aan haar kant van het kanaal, en Bob heeft er 30.000, voor een totaal van 130.000 satoshi's, wat de **kanaalcapaciteit** vormt.


**Maar wat is een Satoshi? **


De **Satoshi** (of "sat") is een rekeneenheid op Bitcoin. Vergelijkbaar met een cent voor de euro, is een Satoshi gewoon een fractie van Bitcoin. Eén Satoshi is gelijk aan **0,00000001 Bitcoin**, of een honderdmiljoenste van een Bitcoin. Het gebruik van de Satoshi wordt steeds praktischer naarmate de waarde van Bitcoin stijgt.


### De toewijzing van fondsen in het Kanaal


Laten we terugkeren naar het betalingskanaal. Het sleutelbegrip hier is de "**kant van het kanaal**". Elke deelnemer heeft fondsen aan zijn kant van het kanaal: Alice 100.000 satoshis en Bob 30.000. Zoals we hebben gezien, vertegenwoordigt de som van deze fondsen de totale capaciteit van het kanaal, een getal dat wordt ingesteld wanneer het wordt geopend.


![LNP201](assets/en/002.webp)


Laten we een voorbeeld nemen van een Lightning-transactie. Als Alice 40.000 satoshis naar Bob wil sturen, is dit mogelijk omdat ze genoeg geld heeft (100.000 satoshis). Na deze transactie heeft Alice 60.000 satoshis aan haar kant en Bob 70.000.


![LNP201](assets/en/003.webp)


De **kanaalcapaciteit**, 130.000 satoshi, blijft constant. Wat verandert is de toewijzing van fondsen. Dit systeem staat niet toe meer geld te sturen dan iemand bezit. Als Bob bijvoorbeeld 80.000 satoshi's wil terugsturen naar Alice, kan dat niet, omdat hij maar 70.000 heeft.


Een andere manier om je de toewijzing van fondsen voor te stellen is door je een **cursor** voor te stellen die aangeeft waar de fondsen zich binnen het kanaal bevinden. In het begin, met 100.000 satoshi's voor Alice en 30.000 voor Bob, staat de cursor meer aan de kant van Bob, omdat Alice veel meer geld heeft. Na de transactie van 40.000 satoshi's verschuift de cursor iets in de richting van Alice, die nu 60.000 satoshi's bezit.


![LNP201](assets/en/004.webp)


Deze voorstelling kan nuttig zijn om de balans van fondsen in een kanaal voor te stellen.


### De basisregels van een betalingskanaal


Het eerste punt om te onthouden is dat de **kanaalcapaciteit** vast is. Het is een beetje zoals de diameter van een pijp: het bepaalt de maximale hoeveelheid geld die in één keer door het kanaal kan worden gestuurd.

Laten we een voorbeeld nemen: als Alice 130.000 satho's aan haar kant heeft, kan ze in één enkele transactie maximaal 130.000 satho's naar Bob sturen. Bob kan dit geld echter terugsturen naar Alice, geheel of gedeeltelijk.


Wat belangrijk is om te begrijpen, is dat de vaste capaciteit van het kanaal het maximale bedrag van een enkele transactie beperkt, maar niet het totale aantal mogelijke transacties, noch het totale volume aan geld dat binnen het kanaal wordt uitgewisseld.


**Wat moet je meenemen uit dit hoofdstuk?**



- De capaciteit van een kanaal ligt vast en bepaalt het maximale bedrag dat in een enkele transactie verstuurd kan worden.
- De fondsen in een kanaal worden verdeeld tussen de twee deelnemers, en elk kan alleen de fondsen naar de ander sturen die ze aan hun kant bezitten.
- De Lightning Network maakt dus een snelle en efficiënte Exchange van fondsen mogelijk, met inachtneming van de beperkingen die worden opgelegd door de capaciteit van de kanalen.


Dit is het einde van dit eerste hoofdstuk, waarin we de basis hebben gelegd voor de Lightning Network. In de volgende hoofdstukken zullen we zien hoe je een kanaal opent en dieper ingaan op de concepten die hier zijn besproken.


## Bitcoin, Adressen, UTXO en Transacties


<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>


:::video id=75323eef-ea03-45ac-9a6e-46d73ca255de:::


Dit hoofdstuk is een beetje speciaal, omdat het niet direct aan Lightning is gewijd, maar aan de Bitcoin. De Lightning Network is namelijk een Layer bovenop de Bitcoin. De Lightning Network is namelijk een Layer bovenop de Bitcoin. Het is daarom essentieel om bepaalde fundamentele concepten van Bitcoin te begrijpen om de werking van Lightning in de volgende hoofdstukken goed te begrijpen. In dit hoofdstuk bespreken we de basis van Bitcoin ontvangstadressen, UTXO's en de werking van Bitcoin transacties.


### Bitcoin Adressen, privé sleutels en openbare sleutels


Een Bitcoin Address is een reeks karakters afgeleid van een **publieke sleutel**, die zelf berekend wordt uit een **private sleutel**. Zoals je ongetwijfeld weet, wordt het gebruikt om bitcoins te vergrendelen, wat gelijk staat aan het ontvangen ervan in onze Wallet.


De private sleutel is een geheim element dat **nooit** gedeeld mag worden, terwijl de publieke sleutel en het Address gedeeld kunnen worden zonder veiligheidsrisico (hun onthulling vormt alleen een risico voor je privacy). Hier is een algemene voorstelling die we in deze training zullen gebruiken:



- De **private sleutels** worden **verticaal** weergegeven.
- De **publieke sleutels** worden **horizontaal** weergegeven.
- Hun kleur geeft aan wie ze bezit (Alice in oranje en Bob in zwart...).


### Bitcoin Transacties: Geld verzenden en scripts


Op Bitcoin bestaat een transactie uit het versturen van geld van de ene Address naar de andere. Laten we het voorbeeld nemen van Alice die 0,002 Bitcoin naar Bob stuurt. Alice gebruikt de privésleutel die aan haar Address is gekoppeld om de transactie te **ondertekenen**, waarmee ze bewijst dat ze inderdaad in staat is om dit geld uit te geven. Maar wat gebeurt er precies achter deze transactie? De fondsen op een Address Bitcoin zijn vergrendeld door een **script**, een soort miniprogramma dat bepaalde voorwaarden stelt aan het uitgeven van de fondsen.


Het meest voorkomende script vereist een handtekening met de privé-sleutel geassocieerd met Address. Wanneer Alice een transactie ondertekent met haar private sleutel, **vrijgavet ze het script** dat de fondsen blokkeert, en ze kunnen dan worden overgedragen. De overdracht van fondsen omvat het toevoegen van een nieuw script aan deze fondsen, waarin staat dat om ze deze keer uit te geven, de handtekening met de privé-sleutel** van **Bob vereist is.


![LNP201](assets/en/005.webp)


### UTXO's: Ongebruikte transactie-uitgangen


Op Bitcoin, wat we eigenlijk Exchange zijn niet direct bitcoins, maar **UTXOs** (_Unspent Transaction Outputs_), wat betekent "niet uitgegeven transactie-uitgangen".


Een UTXO is een stuk Bitcoin dat elke waarde kan hebben, bijvoorbeeld **2.000 bitcoins**, **8 bitcoins**, of zelfs **8.000 Sats**. Elke UTXO wordt vergrendeld door een script, en om het uit te geven moet men voldoen aan de voorwaarden van het script, vaak een handtekening met de private sleutel die overeenkomt met een bepaalde ontvangende Address.


UTXO's kunnen niet worden verdeeld. Elke keer dat ze worden gebruikt om het bedrag in bitcoins dat ze vertegenwoordigen uit te geven, moet dat in zijn geheel gebeuren. Het is een beetje zoals een bankbiljet: als je een biljet van €10 hebt en je bent de bakker €5 schuldig, dan kun je het biljet niet zomaar doormidden snijden. Je moet hem het biljet van €10 geven en hij zal je €5 teruggeven als wisselgeld. Dit is precies hetzelfde principe voor UTXO's op Bitcoin! Wanneer Alice bijvoorbeeld een script ontgrendelt met haar privésleutel, ontgrendelt ze UTXO in zijn geheel. Als ze slechts een deel van de fondsen, vertegenwoordigd door deze UTXO, naar Bob wil sturen, kan ze het "fragmenteren" in verschillende kleinere. Ze zal dan 0,0015 BTC naar Bob sturen en de rest, 0,0005 BTC, naar een **Wijzig Address**.


Hier is een voorbeeld van een transactie met 2 uitgangen:



- Een UTXO van 0,0015 BTC voor Bob, vergrendeld door een script dat de handtekening van Bob's private sleutel vereist.
- Een UTXO van 0,0005 BTC voor Alice, vergrendeld door een script dat haar eigen handtekening vereist.


![LNP201](assets/en/006.webp)


### Adressen met meerdere handtekeningen


Naast eenvoudige adressen gegenereerd uit een enkele publieke sleutel, is het mogelijk om **multi-handtekening adressen** te maken uit meerdere publieke sleutels. Een bijzonder interessant geval voor de Lightning Network is de **2/2 multi-handtekening Address**, gegenereerd uit twee publieke sleutels:


![LNP201](assets/en/007.webp)


Om de middelen uit te geven die vergrendeld zijn met deze 2/2-meervoudige handtekening Address, is het nodig om te ondertekenen met de twee privésleutels die geassocieerd zijn met de publieke sleutels.


![LNP201](assets/en/008.webp)


Dit type Address is precies de representatie op de Bitcoin Blockchain van betaalkanalen op de Lightning Network.


**Wat moet je meenemen uit dit hoofdstuk?**



- Een **Bitcoin Address** is afgeleid van een openbare sleutel, die zelf weer is afgeleid van een privésleutel.
- Fondsen op Bitcoin zijn vergrendeld door **scripts**, en om deze fondsen uit te geven moet men voldoen aan het script, wat over het algemeen inhoudt dat men een handtekening met de bijbehorende privésleutel moet geven.
- **UTXO's** zijn stukken bitcoins die vergrendeld zijn door scripts, en elke transactie op Bitcoin bestaat uit het ontgrendelen van een UTXO en het creëren van een of meer nieuwe in ruil daarvoor.
- 2/2 adressen met **meerdere handtekeningen** vereisen de handtekening van twee privésleutels om het geld uit te geven. Deze specifieke adressen worden gebruikt in de context van Lightning om betalingskanalen te maken.


In dit hoofdstuk over de Bitcoin hebben we een aantal essentiële begrippen besproken voor wat volgt. In het volgende hoofdstuk zullen we specifiek ontdekken hoe het openen van kanalen op de Lightning Network werkt.


# Kanalen openen en sluiten


<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>


## Kanaal openen


<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>


:::video id=6098fee1-735e-4d8d-9f57-0faf5fef6d76:::


In dit hoofdstuk zullen we meer precies zien hoe je een betalingskanaal opent op de Lightning Network en de link begrijpen tussen deze operatie en het onderliggende Bitcoin systeem.


### Bliksemkanalen


Zoals we in het eerste hoofdstuk hebben gezien, kan een **betaalkanaal** op Lightning worden vergeleken met een "pijp" voor het uitwisselen van geld tussen twee deelnemers (**Alice** en **Bob** in onze voorbeelden). De capaciteit van dit kanaal komt overeen met de som van de beschikbare fondsen aan elke kant. In ons voorbeeld heeft Alice **100.000 satoshi** en Bob **30.000 satoshi**, wat een **totale capaciteit** geeft van **130.000 satoshi**.


![LNP201](assets/en/009.webp)


### Informatieniveaus Exchange


Het is cruciaal om duidelijk onderscheid te maken tussen de verschillende niveaus van Exchange op de Lightning Network:



- **Peer-to-peer-communicatie (Lightning-protocol)**: Dit zijn de berichten die Lightning-knooppunten naar elkaar sturen om te communiceren. We zullen deze berichten weergeven met stippellijnen in onze diagrammen.
- **Betalingskanalen (Lightning-protocol)**: Dit zijn de paden voor het uitwisselen van geld op Lightning, die we zullen weergeven met ononderbroken zwarte lijnen.
- **Bitcoin transacties (Bitcoin protocol)**: Dit zijn de onchain transacties, die we weergeven met oranje lijnen.


![LNP201](assets/en/010.webp)


Het is vermeldenswaard dat een Lightning-knooppunt via het P2P protocol kan communiceren zonder een kanaal te openen, maar voor Exchange fondsen is een kanaal nodig.


### Stappen om een Lightning-kanaal te openen



- **Bericht Exchange**: Alice wil een kanaal openen met Bob. Ze stuurt hem een bericht met het bedrag dat ze in het kanaal wil storten (130.000 Sats) en haar publieke sleutel. Bob antwoordt door zijn eigen publieke sleutel te delen.


![LNP201](assets/en/011.webp)



- Creatie van de **Address** met meerdere handtekeningen: Met deze twee openbare sleutels creëert Alice een **2/2-meervoudige handtekening Address**, wat betekent dat voor het geld dat later op deze Address wordt gestort, beide handtekeningen (Alice en Bob) nodig zijn om uitgegeven te worden.


![LNP201](assets/en/012.webp)



- **Stortingstransactie**: Alice bereidt een Bitcoin transactie voor om geld te storten op deze Address met meerdere handtekeningen. Ze kan bijvoorbeeld besluiten om **130.000 satoshis** naar deze Address met meerdere handtekeningen te sturen. Deze transactie is **opgebouwd, maar nog niet gepubliceerd** op Blockchain.


![LNP201](assets/en/013.webp)



- **Opnametransactie**: Voordat Alice de stortingstransactie publiceert, construeert ze een opnametransactie, zodat ze haar geld kan terugkrijgen in geval van een probleem met Bob. Zodra Alice namelijk de stortingstransactie publiceert, wordt haar Sats geblokkeerd op een 2/2 Address met meerdere handtekeningen, die zowel haar handtekening als die van Bob nodig heeft om te worden gedeblokkeerd. Alice beschermt zich tegen dit verliesrisico door de opnametransactie zo te construeren dat ze haar geld kan terugkrijgen.


![LNP201](assets/en/014.webp)



- **Bob's handtekening**: Alice stuurt de stortingstransactie naar Bob als bewijs en vraagt hem de opnametransactie te ondertekenen. Zodra Bob's handtekening is verkregen op de opnametransactie, is Alice ervan verzekerd dat ze haar geld op elk moment kan terugkrijgen, omdat alleen haar eigen handtekening nog nodig is om de multihashandtekening te ontgrendelen.


![LNP201](assets/en/015.webp)



- **Publicatie van de depottransactie**: Zodra de handtekening van Bob is verkregen, kan Alice de depottransactie publiceren op Bitcoin Blockchain, waardoor het Lightning-kanaal tussen de twee gebruikers officieel wordt geopend.


![LNP201](assets/en/016.webp)


### Wanneer is het kanaal open?


Het kanaal wordt als open beschouwd zodra de stortingstransactie is opgenomen in een Bitcoin blok en het een bepaalde diepte van bevestigingen heeft bereikt (aantal volgende blokken).


**Wat moet je onthouden uit dit hoofdstuk?**



- Het openen van een kanaal begint met de Exchange van **berichten** tussen de twee partijen (Exchange van bedragen en publieke sleutels).
- Een kanaal wordt gevormd door een **2/2 multihandtekening Address** aan te maken en er geld in te storten via een Bitcoin transactie.
- De persoon die het kanaal opent, zorgt ervoor dat hij **zijn fondsen** kan terugvorderen door middel van een opnametransactie die door de andere partij is ondertekend voordat hij de stortingstransactie publiceert.


In het volgende hoofdstuk gaan we dieper in op de technische werking van een Lightning-transactie binnen een kanaal.


## Commitment Transaction


<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>


:::video id=c17454f3-14c5-47a0-8c9c-42ee12932bd3:::


In dit hoofdstuk ontdekken we de technische werking van een transactie binnen een kanaal op de Lightning Network, dat wil zeggen, wanneer geld van de ene kant van het kanaal naar de andere kant wordt verplaatst.


### Herinnering aan de levenscyclus van kanalen


Zoals eerder gezien, begint een Lightning-kanaal met een **opening** via een Bitcoin transactie. Het kanaal kan op elk moment **gesloten** worden, ook via een Bitcoin transactie. Tussen deze twee momenten kan een bijna oneindig aantal transacties worden uitgevoerd binnen het kanaal, zonder door de Bitcoin Blockchain te gaan. Laten we eens kijken wat er gebeurt tijdens een transactie in het kanaal.


![LNP201](assets/en/017.webp)


### De initiële toestand van het kanaal


Op het moment dat het kanaal werd geopend, stortte Alice **130.000 satoshis** op de meerstemmige Address van het kanaal. In de begintoestand zijn alle fondsen dus aan de kant van Alice. Voordat Alice het kanaal opende, liet ze Bob ook een **opnametransactie** ondertekenen, waardoor ze haar fondsen kon terugkrijgen als ze het kanaal wilde sluiten.


![LNP201](assets/en/018.webp)


### Ongepubliceerde transacties: De Commitment-transacties


Wanneer Alice een transactie in het kanaal maakt om geld naar Bob te sturen, wordt een nieuwe Bitcoin transactie aangemaakt om deze verandering in de verdeling van het geld weer te geven. Deze transactie, **Commitment Transaction** genaamd, wordt niet gepubliceerd op de Blockchain, maar vertegenwoordigt de nieuwe toestand van het kanaal na de Lightning-transactie.


Laten we een voorbeeld nemen waarbij Alice 30.000 satoshis naar Bob stuurt:



- **Aanvankelijk**: Alice heeft 130.000 satoshis.
- **Na de transactie**: Alice heeft 100.000 satoshis en Bob 30.000 satoshis.

Om deze overdracht te valideren, creëren Alice en Bob een nieuwe **niet-gepubliceerde Bitcoin-transactie** die **100.000 satoshi's naar Alice** en **30.000 satoshi's naar Bob** zou sturen vanuit de Address met meerdere handtekeningen. Beide partijen stellen deze transactie onafhankelijk op, maar met dezelfde gegevens (bedragen en adressen). Zodra de transactie is samengesteld, ondertekenen beide partijen deze en wisselen hun handtekening uit met de andere partij. Hierdoor kunnen beide partijen de transactie op elk moment publiceren als dat nodig is om hun aandeel in het kanaal op de hoofd Bitcoin Blockchain terug te krijgen.

![LNP201](assets/en/019.webp)


### Overdrachtsproces: De Invoice


Wanneer Bob geld wil ontvangen, stuurt hij Alice een **_invoice_** voor 30.000 satoshis. Alice gaat dan verder met het betalen van deze Invoice door de overdracht binnen het kanaal te starten. Zoals we hebben gezien, berust dit proces op het aanmaken en ondertekenen van een nieuwe **Commitment Transaction**.


Elke Commitment Transaction vertegenwoordigt de nieuwe verdeling van fondsen in het kanaal na de overdracht. In dit voorbeeld heeft Bob na de transactie 30.000 satoshi en Alice 100.000 satoshi. Als een van de twee deelnemers zou besluiten om deze Commitment Transaction te publiceren op Blockchain, zou dit resulteren in het sluiten van het kanaal en zouden de fondsen worden verdeeld volgens deze laatste verdeling.


![LNP201](assets/en/020.webp)


### Nieuwe staat na een tweede transactie


Laten we een ander voorbeeld nemen: na de eerste transactie, waarbij Alice 30.000 satoshi's naar Bob stuurde, besluit Bob om **10.000 satoshi's terug te sturen naar Alice**. Dit creëert een nieuwe toestand van het kanaal. De nieuwe **Commitment Transaction** vertegenwoordigt deze bijgewerkte verdeling:



- **Alice** heeft nu **110.000 satoshis**.
- **Bob** heeft **20.000 satoshis**.


![LNP201](assets/en/021.webp)


Ook deze transactie wordt niet gepubliceerd op de Blockchain, maar kan op elk moment worden gepubliceerd als het kanaal gesloten is.


Samengevat, wanneer fondsen worden overgedragen binnen een Lightning-kanaal:



- Alice en Bob creëren een nieuwe **Commitment Transaction**, die de nieuwe verdeling van fondsen weergeeft.
- Deze Bitcoin transactie is **ondertekend** door beide partijen, maar **niet gepubliceerd** op Bitcoin Blockchain zolang het kanaal open blijft.
- De Commitment transacties zorgen ervoor dat elke deelnemer zijn geld op elk moment op Bitcoin Blockchain kan terugkrijgen door de laatst ondertekende transactie te publiceren.


Dit systeem heeft echter een potentiële tekortkoming, die we Address in het volgende hoofdstuk zullen behandelen. We zullen zien hoe elke deelnemer zichzelf kan beschermen tegen een poging om vals te spelen door de andere partij.


## Herroepingssleutel


<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>

:::video id=1d850f23-eff1-4725-b284-ce12456a2c26:::

In dit hoofdstuk gaan we dieper in op hoe transacties werken op de Lightning Network door de mechanismen te bespreken die valsspelen tegengaan en ervoor zorgen dat elke partij zich aan de regels houdt binnen een kanaal.


### Herinnering: Commitment Transacties


Zoals eerder gezien, zijn transacties op Lightning gebaseerd op niet-gepubliceerde **Commitment transacties**. Deze transacties geven de huidige verdeling van fondsen in het kanaal weer. Wanneer er een nieuwe Lightning-transactie wordt gedaan, wordt er een nieuwe Commitment Transaction aangemaakt en ondertekend door beide partijen om de nieuwe status van het kanaal weer te geven.


Laten we een eenvoudig voorbeeld nemen:



- **Begintoestand**: Alice heeft **100.000 satos**, Bob **30.000 satos**.
- Na een transactie waarbij Alice **40.000 satoshis** naar Bob stuurt, verdeelt de nieuwe Commitment Transaction het geld als volgt:
  - Alice: **60.000 satoshis**
  - Bob: **70.000 satoshis**


![LNP201](assets/en/022.webp)


Op elk moment kunnen beide partijen de **laatste Commitment Transaction** publiceren om het kanaal te sluiten en hun geld terug te krijgen.


### De fout: valsspelen door een oude transactie te publiceren


Er kan een probleem ontstaan als een van de partijen besluit om **cheat** te spelen door een oude Commitment Transaction te publiceren. Alice zou bijvoorbeeld een oudere Commitment Transaction kunnen publiceren, waarin ze **100.000 satoshi's** had, terwijl ze nu in werkelijkheid slechts **60.000** heeft. Hierdoor zou ze **40.000 satoshis** kunnen stelen van Bob.


![LNP201](assets/en/023.webp)


Erger nog, Alice kan de allereerste opname-transactie publiceren, die voordat het kanaal werd geopend, waar ze **130.000 satoshis** had, en zo de fondsen van het hele kanaal stelen.


![LNP201](assets/en/024.webp)


### Oplossing: Intrekkingsleutel en tijdslot


Om dit soort valsspelen door Alice te voorkomen, zijn op de Lightning Network **veiligheidsmechanismen** toegevoegd aan de Commitment transacties:



- **Het tijdslot**: Elke Commitment Transaction bevat een tijdslot voor Alice's fondsen. Het tijdslot is een Smart contract primitieve die een tijdsvoorwaarde stelt waaraan voldaan moet worden voordat een transactie aan een blok kan worden toegevoegd. Dit betekent dat Alice haar fondsen niet kan terugkrijgen totdat een bepaald aantal blokken voorbij is, als ze één van de Commitment transacties publiceert. Dit tijdslot gaat in vanaf de bevestiging van Commitment Transaction. De duur is meestal evenredig met de grootte van het kanaal, maar kan ook handmatig worden ingesteld.
- **Herroepingssleutel**: Alice's fondsen kunnen ook onmiddellijk uitgegeven worden door Bob als hij de **herroepingssleutel** bezit. Deze sleutel bestaat uit een geheim van Alice en een geheim van Bob. Merk op dat dit geheim voor elke Commitment Transaction anders is.

Dankzij deze 2 gecombineerde mechanismen heeft Bob de tijd om Alice's poging om vals te spelen te detecteren en haar te straffen door zijn output terug te halen met de revocatiesleutel, wat voor Bob betekent dat alle fondsen van het kanaal worden teruggehaald. Onze nieuwe Commitment Transaction ziet er nu zo uit:


![LNP201](assets/en/025.webp)


Laten we samen de werking van dit mechanisme in detail bekijken.


### Proces voor het bijwerken van transacties


Wanneer Alice en Bob de toestand van het kanaal bijwerken met een nieuwe Lightning-transactie, Exchange ze vooraf hun respectievelijke **geheimen** voor de vorige Commitment Transaction (degene die verouderd zal raken en een van hen zou kunnen laten valsspelen). Dit betekent dat, in de nieuwe toestand van het kanaal:



- Alice en Bob hebben een nieuwe Commitment Transaction die de huidige verdeling van fondsen na de Lightning-transactie weergeeft.
- Elk van hen heeft het geheim van de ander voor de vorige transactie, waardoor ze de herroepingssleutel alleen kunnen gebruiken als een van hen probeert vals te spelen door een transactie met een oude status te publiceren in de mempools van de Bitcoin knooppunten. Om de andere partij te straffen, is het inderdaad nodig om beide geheimen te hebben en de Commitment Transaction van de ander, die de ondertekende invoer bevat. Zonder deze transactie is de revocatiesleutel alleen nutteloos. De enige manier om deze transactie te verkrijgen is door deze uit de mempools te halen (in de transacties die wachten op bevestiging) of in de bevestigde transacties op de Blockchain tijdens de tijdslot, wat bewijst dat de andere partij probeert vals te spelen, opzettelijk of niet.


Laten we een voorbeeld nemen om dit proces goed te begrijpen:



- **Oorspronkelijke staat**: Alice heeft **100.000 satos**, Bob **30.000 satos**.


![LNP201](assets/en/026.webp)



- Bob wil 40.000 satoshis ontvangen van Alice via hun Lightning-kanaal. Om dit te doen:
   - Hij stuurt haar een Invoice samen met zijn geheim voor de herroepingssleutel van zijn vorige Commitment Transaction.
   - Als antwoord geeft Alice haar handtekening voor Bob's nieuwe Commitment Transaction, evenals haar geheim voor de herroepingssleutel van haar vorige transactie.
   - Tenslotte stuurt Bob zijn handtekening voor Alice's nieuwe Commitment Transaction.
   - Deze uitwisselingen stellen Alice in staat om **40.000 satoshis** naar Bob op Lightning te sturen via hun kanaal, en de nieuwe Commitment transacties weerspiegelen nu deze nieuwe verdeling van fondsen.


![LNP201](assets/en/027.webp)



- Als Alice probeert het oude Commitment Transaction te publiceren, waar ze nog **100.000 satoshis** bezat, kan Bob, die de revocatiesleutel heeft verkregen, het geld onmiddellijk terughalen met deze sleutel, terwijl Alice wordt geblokkeerd door het tijdslot.


![LNP201](assets/en/028.webp)


Zelfs als Bob er in dit geval geen economisch belang bij heeft om te proberen vals te spelen, als hij dat toch doet, profiteert Alice ook van symmetrische bescherming die haar dezelfde garanties biedt.


**Wat moet je meenemen uit dit hoofdstuk?**


De **Commitment transacties** op de Lightning Network bevatten beveiligingsmechanismen die zowel het risico van valsspelen als de stimulans om vals te spelen verminderen. Voor het tekenen van een nieuwe Commitment Transaction, Alice en Bob Exchange hun respectievelijke **geheimen** voor de vorige Commitment transacties. Als Alice een oude Commitment Transaction probeert te publiceren, kan Bob de **herroepingssleutel** gebruiken om alle fondsen terug te krijgen voordat Alice dat kan (omdat ze geblokkeerd is door het tijdslot), wat haar straft voor haar poging om vals te spelen.


Dit beveiligingssysteem zorgt ervoor dat deelnemers zich aan de regels van de Lightning Network houden en dat ze geen voordeel kunnen halen uit het publiceren van oude Commitment-transacties.


Op dit punt in de training weet je nu hoe Lightning-kanalen worden geopend en hoe transacties binnen deze kanalen werken. In het volgende hoofdstuk ontdekken we de verschillende manieren om een kanaal te sluiten en je bitcoins terug te krijgen op het hoofdkanaal Blockchain.


## Kanaal Sluiting


<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>


:::video id=4d8ad4e6-32ff-46d3-bd17-343929aa863b:::


In dit hoofdstuk bespreken we het sluiten van een **kanaal** op de Lightning Network, wat gedaan wordt via een Bitcoin transactie, net als het openen van een kanaal. Na gezien te hebben hoe transacties binnen een kanaal werken, is het nu tijd om te zien hoe je een kanaal sluit en de fondsen terugvordert op de Bitcoin Blockchain.


### Herinnering aan de levenscyclus van kanalen


De **levenscyclus van een kanaal** begint met het **openen** ervan, via een Bitcoin transactie, vervolgens worden er Lightning-transacties binnen gedaan, en ten slotte, wanneer de partijen hun geld willen terugvorderen, wordt het kanaal **gesloten** via een tweede Bitcoin transactie. De tussenliggende transacties op Lightning worden weergegeven door niet-gepubliceerde **Commitment transacties**.


![LNP201](assets/en/029.webp)


### De drie soorten kanaalafsluiting


Er zijn drie manieren om dit kanaal te sluiten, die we **de goede, de brute en de spijbelaar** kunnen noemen (geïnspireerd door Andreas Antonopoulos in _Mastering the Lightning Network_):



- **Het goede**: de **coöperatieve sluiting**, waarbij Alice en Bob overeenkomen het kanaal te sluiten.
- **De Slechte**: de **gedwongen sluiting**, waarbij een van de partijen besluit om het kanaal eerlijk te sluiten, maar zonder toestemming van de ander.
- **The Ugly**: de **sluiting met bedrog**, waarbij een van de partijen probeert fondsen te stelen door een oude Commitment Transaction te publiceren (elke, maar niet de laatste, die de werkelijke en eerlijke verdeling van fondsen weergeeft).


Laten we een voorbeeld nemen:



- Alice bezit **100.000 satoshis** en Bob **30.000 satoshis**.
- Deze verdeling wordt weerspiegeld in **2 Commitment transacties** (één per gebruiker) die niet gepubliceerd worden, maar dat wel zouden kunnen worden in het geval van kanaalafsluiting.


![LNP201](assets/en/030.webp)


### Het goede: de coöperatieve sluiting


In een **coöperatieve sluiting** komen Alice en Bob overeen om het kanaal te sluiten. Het gaat als volgt:



- Alice stuurt een bericht naar Bob via het Lightning communicatieprotocol om voor te stellen het kanaal te sluiten.
- Bob gaat akkoord en de twee partijen verrichten geen verdere transacties in het kanaal.


![LNP201](assets/en/031.webp)



- Alice en Bob onderhandelen samen over de vergoedingen van de **sluitende transactie**. Deze vergoedingen worden doorgaans berekend op basis van de Bitcoin vergoedingenmarkt op het moment van afsluiten. Het is belangrijk op te merken dat **het altijd de persoon is die het kanaal** heeft geopend (Alice in ons voorbeeld) die de afsluitprovisie betaalt.
- Ze construeren een nieuwe **sluitende transactie**. Deze transactie lijkt op een Commitment Transaction, maar zonder tijdsloten of herroepingsmechanismen, omdat beide partijen samenwerken en er geen risico is op valsspelen. Deze coöperatieve sluitingstransactie verschilt daarom van Commitment transacties.


Als Alice bijvoorbeeld **100.000 satoshi's** bezit en Bob **30.000 satoshi's**, dan zal de sluitingstransactie **100.000 satoshi's** naar Address van Alice sturen en **30.000 satoshi's** naar Address van Bob, zonder tijdsbeperkingen. Zodra deze transactie door beide partijen is ondertekend, wordt ze gepubliceerd door Alice. Zodra de transactie is bevestigd op Bitcoin Blockchain, wordt het Lightning-kanaal officieel gesloten.


![LNP201](assets/en/032.webp)


De **coöperatieve sluiting** heeft de voorkeur omdat het snel is (geen tijdslot) en de transactiekosten worden aangepast aan de huidige Bitcoin marktomstandigheden. Zo wordt voorkomen dat er te weinig wordt betaald, waardoor de transactie in de mempools zou kunnen worden geblokkeerd, of dat er onnodig te veel wordt betaald, wat leidt tot onnodig financieel verlies voor de deelnemers.


### Het slechte: de gedwongen sluiting


Wanneer Alice's knooppunt een bericht stuurt naar Bob's met de vraag om een coöperatieve sluiting, als hij niet reageert (bijvoorbeeld door een internetstoring of een technisch probleem), kan Alice overgaan tot een **gedwongen sluiting** door de **laatst ondertekende Commitment Transaction** te publiceren.

In dit geval zal Alice gewoon de laatste Commitment Transaction publiceren, die de toestand van het kanaal weergeeft op het moment dat de laatste Lightning-transactie plaatsvond met de correcte verdeling van fondsen.


![LNP201](assets/en/033.webp)


Deze transactie bevat een **timelock** voor Alice's fondsen, waardoor de afsluiting langzamer verloopt.


![LNP201](assets/en/034.webp)


Ook kunnen de vergoedingen van de Commitment Transaction ongeschikt zijn op het moment van afsluiten, omdat ze werden vastgesteld toen de transactie werd aangemaakt, soms enkele maanden daarvoor. Over het algemeen schatten Lightning klanten de vergoedingen te hoog in om toekomstige problemen te voorkomen, maar dit kan leiden tot te hoge vergoedingen of juist te lage.


Samengevat is **gedwongen afsluiting** een laatste redmiddel als de peer niet meer reageert. Het is langzamer en minder zuinig dan een coöperatieve afsluiting. Daarom moet het zoveel mogelijk vermeden worden.


### De valsspeler: valsspelen


Tenslotte treedt een afsluiting met **cheating** op wanneer een van de partijen probeert een oude Commitment Transaction te publiceren, vaak wanneer ze meer geld bezat dan zou moeten. Alice kan bijvoorbeeld een oude transactie publiceren waarin ze **120.000 satoshi** bezat, terwijl ze nu eigenlijk maar **100.000** bezit.


![LNP201](assets/en/035.webp)


Bob, om dit bedrog te voorkomen, controleert Bitcoin Blockchain en haar Mempool om er zeker van te zijn dat Alice geen oude transactie publiceert. Als Bob een poging tot valsspelen ontdekt, kan hij de **herroepingssleutel** gebruiken om de fondsen van Alice terug te krijgen en haar straffen door de volledige fondsen van het kanaal af te pakken. Omdat Alice geblokkeerd is door het tijdslot op haar uitgang, heeft Bob de tijd om het zonder tijdslot aan zijn kant uit te geven om het hele bedrag terug te krijgen op een Address die hij bezit.


![LNP201](assets/en/036.webp)


Het is duidelijk dat valsspelen kan slagen als Bob niet handelt binnen de tijd die wordt opgelegd door het tijdslot op Alice's uitvoer. In dat geval wordt de uitvoer van Alice ontgrendeld, zodat ze die kan consumeren om een nieuwe uitvoer te maken naar een Address die ze controleert.


**Wat moet je meenemen uit dit hoofdstuk?**


Er zijn drie manieren om een kanaal te sluiten:



- **Coöperatieve afsluiting**: Snel en goedkoper, waarbij beide partijen overeenkomen om het kanaal te sluiten en een op maat gemaakte sluitingstransactie publiceren.
- **Gedwongen sluiting**: Minder wenselijk, omdat dit afhankelijk is van het publiceren van een Commitment Transaction, met mogelijk ongeschikte vergoedingen en een tijdslot, wat de afsluiting vertraagt.
- **Valsspelen**: Als een van de partijen geld probeert te stelen door een oude transactie te publiceren, kan de andere partij de revocatiesleutel gebruiken om dit bedrog te bestraffen.


In de komende hoofdstukken zullen we de Lightning Network vanuit een breder perspectief bekijken, met de nadruk op hoe het netwerk werkt.


# Een liquiditeitsnetwerk


<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>


## Lightning Network


<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>


:::video id=38419c23-5592-4573-b0a7-84824a5bfb77:::


In dit hoofdstuk zullen we onderzoeken hoe betalingen op de Lightning Network een ontvanger kunnen bereiken, zelfs als ze niet direct verbonden zijn door een betalingskanaal. Lightning is namelijk een **netwerk van betalingskanalen**, dat het mogelijk maakt om geld naar een ver knooppunt te sturen via de kanalen van andere deelnemers. We zullen ontdekken hoe betalingen over het netwerk worden geleid, hoe liquiditeit tussen kanalen beweegt en hoe transactiekosten worden berekend.


### Het netwerk van betaalkanalen


Op de Lightning Network komt een transactie overeen met een overdracht van geld tussen twee knooppunten. Zoals in vorige hoofdstukken is gezien, is het noodzakelijk om een kanaal met iemand te openen om Lightning transacties uit te voeren. Dit kanaal staat een bijna oneindig aantal off-chain transacties toe, voordat het gesloten wordt om het On-Chain saldo terug te vorderen. Deze methode heeft echter het nadeel dat er een direct kanaal met de andere persoon nodig is om geld te ontvangen of te versturen, wat een openingstransactie en een sluitingstransactie voor elk kanaal inhoudt. Als ik van plan ben om een groot aantal betalingen te doen met deze persoon, wordt het openen en sluiten van een kanaal kosteneffectief. Omgekeerd, als ik slechts een paar Lightning transacties moet uitvoeren, is het openen van een direct kanaal niet voordelig, omdat het me 2 On-Chain transacties zou kosten voor een beperkt aantal off-chain transacties. Dit geval kan zich bijvoorbeeld voordoen wanneer ik met Lightning wil betalen bij een winkelier zonder van plan te zijn om terug te keren.


Om dit probleem op te lossen, maakt de Lightning Network het mogelijk om een betaling via verschillende kanalen en tussenliggende knooppunten te routeren, waardoor een transactie mogelijk wordt zonder een direct kanaal met de andere persoon.


Stel je dat bijvoorbeeld voor:



- **Alice** (in oranje) heeft een kanaal met **Suzie** (in grijs) met **100.000 satoshis** aan haar kant en **30.000 satoshis** aan Suzie's kant.
- **Suzie** heeft een kanaal met **Bob** waarin zij **250.000 satoshis** bezit en Bob geen satoshis heeft.


![LNP201](assets/en/037.webp)


Als Alice geld wil sturen naar Bob zonder een direct kanaal met hem te openen, zal ze via Suzie moeten gaan, en elk kanaal zal de liquiditeit aan beide kanten moeten aanpassen. **De verzonden satoshis blijven binnen hun respectievelijke kanalen**; ze "kruisen" de kanalen niet echt, maar de overdracht wordt gemaakt via een aanpassing van de interne liquiditeit in elk kanaal.


Stel dat Alice **50.000 satoshis** naar Bob wil sturen:



- **Alice** stuurt 50.000 satoshis naar **Suzie** in hun gemeenschappelijke kanaal.
- **Suzie** repliceert deze overdracht door 50.000 satoshis te sturen naar **Bob** in hun kanaal.


![LNP201](assets/en/038.webp)


Zo wordt de betaling naar Bob geleid via een beweging van liquiditeit in elk kanaal. Aan het einde van de operatie heeft Alice 50.000 Sats. Ze heeft inderdaad 50.000 Sats overgedragen, aangezien ze aanvankelijk 100.000 had. Bob, aan zijn kant, eindigt met nog eens 50.000 Sats. Voor Suzie (het tussenliggende knooppunt) is deze operatie neutraal: aanvankelijk had ze 30.000 Sats in haar kanaal met Alice en 250.000 Sats in haar kanaal met Bob, een totaal van 280.000 Sats. Na de operatie heeft ze 80.000 Sats in haar kanaal met Alice en 200.000 Sats in haar kanaal met Bob, wat dezelfde som is als aan het begin.


Deze overdracht wordt dus beperkt door de **beschikbare liquiditeit** in de richting van de overdracht.


### Berekening van de route- en liquiditeitslimieten


Laten we een theoretisch voorbeeld nemen van een ander netwerk met:



- **130.000 satoshis** aan Alice's kant (in oranje) in haar kanaal met **Suzie** (in grijs).
- **90.000 satoshis** aan **Suzie's** kant en **200.000 satoshis** aan **Carol's** kant (in roze).
- **150.000 satoshis** aan de kant van **Carol** en **100.000 satoshis** aan de kant van **Bob**.


![LNP201](assets/en/039.webp)


Het maximum dat Alice kan sturen naar Bob in deze configuratie is **90.000 satos**, omdat ze beperkt is door de kleinste liquiditeit die beschikbaar is in het kanaal van **Suzie naar Carol**. In de tegenovergestelde richting (van Bob naar Alice) is geen betaling mogelijk, omdat **Suzie's** kant in het kanaal met **Alice** geen satoshis bevat. Daarom is er **geen route** bruikbaar voor een transfer in deze richting.

Alice stuurt **40.000 satoshis** naar Bob via de kanalen:



- Alice maakt 40.000 satoshis over naar haar kanaal met Suzie.
- Suzie maakt 40.000 satoshis over naar Carol in hun gedeelde kanaal.
- Carol maakt uiteindelijk 40.000 satoshis over naar Bob.


![LNP201](assets/en/040.webp)


De verzonden **satoshis** in elk kanaal **blijven in het kanaal**, dus de satoshis die Carol naar Bob stuurt zijn niet dezelfde als die Alice naar Suzie stuurt. De overdracht vindt alleen plaats door de liquiditeit in elk kanaal aan te passen. Bovendien blijft de totale capaciteit van de kanalen onveranderd.


![LNP201](assets/en/041.webp)


Net als in het vorige voorbeeld heeft het bronknooppunt (Alice) na de transactie 40.000 satoshi minder. De tussenliggende knooppunten (Suzie en Carol) behouden hetzelfde totale bedrag, waardoor de transactie voor hen neutraal is. Ten slotte ontvangt het bestemmingsknooppunt (Bob) nog eens 40.000 satoshi.


De rol van de tussenliggende knooppunten is daarom erg belangrijk in de werking van de Lightning Network. Zij faciliteren overdrachten door meerdere paden voor betalingen aan te bieden. Om deze knooppunten aan te moedigen hun liquiditeit ter beschikking te stellen en deel te nemen aan het routeren van betalingen, worden **routing fees** aan hen betaald.


### Routingkosten


De tussenliggende knooppunten passen vergoedingen toe om betalingen door hun kanalen te laten gaan. Deze vergoedingen worden vastgesteld door **elk knooppunt voor elk kanaal**. De vergoedingen bestaan uit 2 Elements:



- "**Basistarief**": een vast bedrag per kanaal, vaak standaard **1 sat**, maar aanpasbaar.
- "**Variabele vergoeding**": een percentage van de overgebrachte hoeveelheid, berekend in **deeltjes per miljoen (ppm)**. Standaard is het **1 ppm** (1 sat per miljoen overgebrachte satoshi's), maar het kan ook worden aangepast.


De kosten verschillen ook afhankelijk van de richting van de overdracht. Bijvoorbeeld, voor een transfer van Alice naar Suzie, zijn de kosten van Alice van toepassing. Omgekeerd, van Suzie naar Alice, worden de kosten van Suzie gebruikt.


Bijvoorbeeld, voor een kanaal tussen Alice en Suzie, zouden we kunnen hebben:



- **Alice**: basisvergoeding van 1 sat en 1 ppm voor variabele vergoedingen.
- **Suzie**: basisvergoeding van 0,5 sat en 10 ppm voor variabele vergoedingen.


![LNP201](assets/en/042.webp)


Om beter te begrijpen hoe vergoedingen werken, bestuderen we dezelfde Lightning Network als eerder, maar nu met de volgende routeringsvergoedingen:



- Kanaal **Alice - Suzie**: basistarief van 1 Satoshi en 1 ppm voor Alice.
- Kanaal **Suzie - Carol**: basisvergoeding van 0 Satoshi en 200 ppm voor Suzie.
- Carol - **Bob** Kanaal: basistarief van 1 Satoshi en 1 ppm voor Suzie 2.

![LNP201](assets/en/043.webp)


Voor dezelfde betaling van **40.000 satos** aan Bob zal Alice iets meer moeten sturen, omdat elk tussenliggend knooppunt zijn kosten zal aftrekken:



- **Carol** trekt 1,04 satoshis af op het kanaal met Bob:

$$ f_{\text{Carol-Bob}} = \text{basisvergoeding} + \left(\frac{\text{ppm} \times \text{bedrag}}{10^6}\right) $$

$$ f_{Carol-Bob} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0.04 = 1.04 \text{ Sats} $$



- **Suzie** trekt 8 satoshis af aan vergoedingen op het kanaal met Carol:

$$ f_{\text{Suzie-Carol}} = \text{basisvergoeding} + \left (\frac{\text{ppm} \times \text{bedrag}}{10^6}\right) $$

$$ f_{Suzie-Carol} = 0 + \frac{200 \times 40001.04}{10^6} = 0 + 8.0002 \approx 8 \text{ Sats} $$


De totale kosten voor deze betaling op dit pad zijn daarom **9,04 satoshis**. Alice moet dus **40.009,04 satoshis** sturen om Bob precies **40.000 satoshis** te laten ontvangen.


![LNP201](assets/en/044.webp)


De liquiditeit is daarom bijgewerkt:


![LNP201](assets/en/045.webp)


### Uienroutering


Om een betaling van de verzender naar de ontvanger te routeren, gebruikt de Lightning Network een methode die "**onion routing**" wordt genoemd. In tegenstelling tot de routering van klassieke gegevens, waarbij elke router de richting van de gegevens bepaalt op basis van hun bestemming, werkt onion routing anders:



- Het verzendende knooppunt berekent de volledige route: Alice, bijvoorbeeld, bepaalt dat haar betaling via Suzie en Carol moet gaan voordat ze Bob bereikt.
- Elk tussenliggend knooppunt kent alleen zijn directe buren: Suzie weet alleen dat ze geld heeft ontvangen van Alice en dat ze dit moet overmaken aan Carol. Suzie weet echter niet of Alice het bronknooppunt is of een tussenliggend knooppunt, en ze weet ook niet of Carol het ontvangende knooppunt is of gewoon een ander tussenliggend knooppunt. Dit principe geldt ook voor Carol en alle andere knooppunten op het pad. Bij onion routing blijft de vertrouwelijkheid van transacties dus behouden door de identiteit van de verzender en de uiteindelijke ontvanger te verhullen.

Om ervoor te zorgen dat het zendende knooppunt een volledige route naar de ontvanger kan berekenen bij onion routing, moet het een **netwerkgrafiek** bijhouden om de topologie te kennen en mogelijke routes te bepalen.

**Wat moet je meenemen uit dit hoofdstuk?**



- Op Lightning kunnen betalingen worden gerouteerd tussen knooppunten die indirect verbonden zijn via intermediaire kanalen. Elk van deze intermediaire knooppunten faciliteert de liquiditeitsrelais.
- Intermediaire knooppunten ontvangen een commissie voor hun diensten, bestaande uit vaste en variabele vergoedingen.
- Met onion routing kan de zendende node de volledige route berekenen zonder dat tussenliggende nodes de bron of eindbestemming kennen.


In dit hoofdstuk hebben we het routeren van betalingen op de Lightning Network onderzocht. Maar er rijst een vraag: wat voorkomt dat tussenliggende knooppunten een inkomende betaling accepteren zonder deze door te sturen naar de volgende bestemming, met als doel de transactie te onderscheppen? Dit is precies de rol van HTLC's die we in het volgende hoofdstuk zullen bestuderen.


## HTLC - Gehashte tijd Contract vergrendeld


<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>


:::video id=6f204b92-55a5-4939-9440-7c5b96a297bf:::


In dit hoofdstuk zullen we ontdekken hoe Lightning betalingen door tussenliggende knooppunten laat lopen zonder ze te hoeven vertrouwen, dankzij **HTLC** (_Hashed Time-Locked Contracts_). Deze slimme contracten zorgen ervoor dat elk tussenliggend knooppunt alleen het geld van zijn kanaal ontvangt als het de betaling doorstuurt naar de eindontvanger, anders wordt de betaling niet gevalideerd.


Het probleem dat zich voordoet bij het routeren van betalingen is daarom het noodzakelijke vertrouwen in de tussenliggende knooppunten en tussen de tussenliggende knooppunten onderling. Om dit te illustreren, gaan we terug naar ons vereenvoudigde Lightning Network voorbeeld met 3 knooppunten en 2 kanalen:



- Alice heeft een kanaal met Suzie.
- Suzie heeft een kanaal met Bob.


Alice wil 40.000 Sats naar Bob sturen, maar ze heeft geen direct kanaal met hem en wil er ook geen openen. Ze zoekt een route en besluit via Suzie's node te gaan.


![LNP201](assets/en/046.webp)


Als Alice naïef 40.000 satoshis naar Suzie stuurt in de hoop dat Suzie dit bedrag zal overmaken naar Bob, kan Suzie het geld voor zichzelf houden en niets overmaken naar Bob.


![LNP201](assets/en/047.webp)

Om deze situatie te vermijden, gebruiken we op Lightning HTLC's (Hashed Time-Locked Contracts), die de betaling aan het tussenliggende knooppunt voorwaardelijk maken, wat betekent dat Suzie aan bepaalde voorwaarden moet voldoen om toegang te krijgen tot de fondsen van Alice en ze over te maken naar Bob.


### Hoe HTLC's werken


Een HTLC is een speciale Contract gebaseerd op twee principes:



- **Toegangsvoorwaarde**: De ontvanger moet een geheim onthullen om de betaling die hem toekomt te ontgrendelen.
- **Vervaldatum**: Als de betaling niet volledig is afgerond binnen een bepaalde periode, wordt deze geannuleerd en gaat het geld terug naar de verzender.


Dit is hoe dit proces werkt in ons voorbeeld met Alice, Suzie en Bob:


![LNP201](assets/en/048.webp)


**Het geheim maken**: Bob genereert een willekeurig geheim genoteerd als _s_ (het voorbeeld), en berekent zijn Hash genoteerd als _r_ met de Hash functie genoteerd als _h_. We hebben:


$$
r = h(s)
$$


Het gebruik van een Hash functie maakt het onmogelijk om _s_ te vinden met alleen _h(s)_, maar als _s_ gegeven wordt, is het eenvoudig om te controleren of het overeenkomt met _h(s)_.


![LNP201](assets/en/049.webp)


**Het betalingsverzoek verzenden**: Bob stuurt een **Invoice** naar Alice en vraagt om een betaling. Deze Invoice bevat met name de Hash _r_.


![LNP201](assets/en/050.webp)


**Stuurt de voorwaardelijke betaling**: Alice stuurt een HTLC van 40.000 satoshis naar Suzie. De voorwaarde voor Suzie om dit geld te ontvangen is dat ze Alice voorziet van een geheim _s'_ dat voldoet aan de volgende vergelijking:


$$
h(s') = r
$$


![LNP201](assets/en/051.webp)


**Het overdragen van de HTLC aan de uiteindelijke ontvanger**: Suzie moet, om de 40.000 satoshi's van Alice te verkrijgen, een soortgelijke HTLC van 40.000 satoshi's overdragen aan Bob, die dezelfde voorwaarde heeft, namelijk dat hij Suzie moet voorzien van een geheim _s'_ dat voldoet aan de vergelijking:


$$
h(s') = r
$$


![LNP201](assets/en/052.webp)


**Validatie door de geheime _s_**: Bob geeft _s_ aan Suzie om de 40.000 satoshis te ontvangen die beloofd zijn in de HTLC. Met dit geheim kan Suzie dan Alice's HTLC ontgrendelen en de 40.000 satoshis van Alice verkrijgen. De betaling wordt dan correct doorgestuurd naar Bob.


![LNP201](assets/en/053.webp)

Dit proces voorkomt dat Suzie het geld van Alice houdt zonder de overdracht naar Bob te voltooien, omdat ze de betaling naar Bob moet sturen om het geheime _s_ te verkrijgen en zo Alice's HTLC te ontgrendelen. De operatie blijft hetzelfde, zelfs als de route meerdere tussenliggende knooppunten bevat: het is gewoon een kwestie van Suzie's stappen te herhalen voor elk tussenliggend knooppunt. Elk knooppunt wordt beschermd door de voorwaarden van de HTLC's, omdat het ontgrendelen van de laatste HTLC door de ontvanger automatisch het ontgrendelen van alle andere HTLC's in een cascade activeert.


### Vervaldatum en beheer van HTLC's in geval van problemen


Als tijdens het betalingsproces een van de tussenliggende knooppunten of het ontvangende knooppunt stopt met reageren, vooral in het geval van een internet- of stroomstoring, dan kan de betaling niet worden voltooid, omdat het geheim dat nodig is om de HTLC's te ontgrendelen niet wordt verzonden. In ons voorbeeld met Alice, Suzie en Bob treedt dit probleem bijvoorbeeld op als Bob het geheim _s_ niet naar Suzie verzendt. In dit geval worden alle HTLC's stroomopwaarts van het pad geblokkeerd, en de fondsen die ze beveiligen ook.


![LNP201](assets/en/054.webp)


Om dit te voorkomen hebben HTLC's op Lightning een vervaldatum die het mogelijk maakt om de HTLC te verwijderen als deze na een bepaalde tijd niet is voltooid. De expiratie volgt een specifieke volgorde, omdat het eerst begint bij de HTLC die het dichtst bij de ontvanger is, en dan geleidelijk oploopt naar de uitgever van de transactie. In ons voorbeeld, als Bob nooit het geheim _s_ aan Suzie geeft, zou dit eerst de HTLC van Suzie naar Bob laten verlopen.


![LNP201](assets/en/055.webp)


Dan de HTLC van Alice naar Suzie.


![LNP201](assets/en/056.webp)


Als de volgorde van verval omgekeerd zou zijn, zou Alice haar betaling kunnen terugvorderen voordat Suzie zichzelf zou kunnen beschermen tegen mogelijk bedrog. Inderdaad, als Bob terugkomt om zijn HTLC op te eisen terwijl Alice de hare al verwijderd heeft, zou Suzie in het nadeel zijn. Deze cascade volgorde van HTLC verval zorgt er dus voor dat geen enkel tussenliggend knooppunt oneerlijke verliezen lijdt.


### Vertegenwoordiging van HTLC's in Commitment transacties


Commitment-transacties vertegenwoordigen HTLC's op zo'n manier dat de voorwaarden die ze opleggen aan Lightning overgedragen kunnen worden naar Bitcoin in het geval van een gedwongen kanaalsluiting tijdens de levensduur van een HTLC. Ter herinnering, Commitment transacties vertegenwoordigen de huidige toestand van het kanaal tussen de twee gebruikers en maken een eenzijdige gedwongen sluiting mogelijk in geval van problemen. Bij elke nieuwe toestand van het kanaal worden 2 Commitment transacties aangemaakt: één voor elke partij. Laten we ons voorbeeld met Alice, Suzie en Bob nog eens bekijken, maar dan wat er gebeurt op kanaalniveau tussen Alice en Suzie als HTLC wordt aangemaakt.

![LNP201](assets/en/057.webp)


Voor het begin van de 40.000 Sats betaling tussen Alice en Bob, heeft Alice 100.000 Sats in haar kanaal met Suzie, terwijl Suzie er 30.000 heeft. Hun Commitment transacties zijn als volgt:


![LNP201](assets/en/058.webp)


Alice heeft zojuist Bob's Invoice ontvangen, die met name _r_ bevat, de Hash van het geheim. Ze kan dus een HTLC van 40.000 satoshis met Suzie construeren. Deze HTLC wordt weergegeven in de laatste Commitment transacties als een output genaamd "**_HTLC Out_**" aan Alice's kant, aangezien de fondsen uitgaand zijn, en "**_HTLC In_**" aan Suzie's kant, aangezien de fondsen inkomend zijn.


![LNP201](assets/en/059.webp)


Deze uitgangen van de HTLC hebben precies dezelfde voorwaarden, namelijk:



- Als Suzie de geheime _s_ kan geven, kan ze deze uitgang onmiddellijk ontgrendelen en overbrengen naar een Address die ze controleert.
- Als Suzie het geheim _s_ niet bezit, kan ze deze uitgang niet ontgrendelen, en Alice zal het na een tijdslot kunnen ontgrendelen om het naar een Address te sturen die ze controleert. Het tijdslot geeft Suzie dus een periode om te reageren als ze _s_ bemachtigt.


Deze voorwaarden zijn alleen van toepassing als het kanaal gesloten is (d.w.z. een Commitment Transaction is On-Chain gepubliceerd) terwijl de HTLC nog steeds actief is op Lightning, wat betekent dat de betaling tussen Alice en Bob nog niet is afgerond, en de HTLC's nog niet zijn verlopen. Dankzij deze voorwaarden kan Suzie de 40.000 satoshis van de HTLC terugvorderen door _s_ te geven. Anders krijgt Alice de fondsen terug na het verstrijken van de tijdslot, want als Suzie _s_ niet kent, betekent het dat ze de 40.000 satoshi's niet heeft overgemaakt aan Bob, en daarom zijn de fondsen van Alice haar niet verschuldigd.


Bovendien, als het kanaal gesloten wordt terwijl er meerdere HTLC's in behandeling zijn, zullen er net zoveel extra uitgangen zijn als er HTLC's in behandeling zijn.

Als het kanaal niet gesloten is, dan worden na het verlopen of slagen van de Lightning-betaling nieuwe Commitment transacties aangemaakt om de nieuwe, nu stabiele, toestand van het kanaal weer te geven, dat wil zeggen, zonder lopende HTLC's. De uitgangen met betrekking tot de HTLC's kunnen daarom worden verwijderd uit de Commitment transacties.

![LNP201](assets/en/060.webp)


Tenslotte, in het geval van een coöperatieve kanaalsluiting terwijl een HTLC actief is, stoppen Alice en Suzie met het accepteren van nieuwe betalingen en wachten ze op de resolutie of afloop van de lopende HTLCs. Dit stelt hen in staat om een lichtere sluitingstransactie te publiceren, zonder de outputs gerelateerd aan de HTLC's, waardoor de kosten worden verlaagd en het wachten op een mogelijke tijdslot wordt vermeden.


**Wat moet je meenemen uit dit hoofdstuk?**


HTLC's maken het mogelijk om Lightning-betalingen door meerdere knooppunten te routeren zonder ze te hoeven vertrouwen. Dit zijn de belangrijkste punten om te onthouden:



- HTLC's garanderen de veiligheid van betalingen door middel van een geheim (preimage) en een verlooptijd.
- Het oplossen of verlopen van HTLC's volgt een specifieke volgorde: van de bestemming naar de bron, om elk knooppunt te beschermen.
- Zolang een HTLC niet is opgelost of verlopen, wordt het bijgehouden als uitvoer in de meest recente Commitment transacties.


In het volgende hoofdstuk zullen we ontdekken hoe een knooppunt dat een Lightning-transactie uitvoert routes vindt en selecteert om de betaling bij het ontvangende knooppunt te krijgen.


## Je weg vinden


<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>


:::video id=e5baa834-111d-46f5-a28b-3538bed2bbb0:::


In de vorige hoofdstukken hebben we gezien hoe je kanalen van andere knooppunten kunt gebruiken om betalingen te routeren en een knooppunt te bereiken zonder er direct mee verbonden te zijn via een kanaal. We hebben ook besproken hoe we de veiligheid van de overdracht kunnen garanderen zonder de tussenliggende knooppunten te vertrouwen. In dit hoofdstuk richten we ons op het vinden van de best mogelijke route om een doelknooppunt te bereiken.


### Het probleem van routeren in Lightning


Zoals we hebben gezien, is het in Lightning het knooppunt dat de betaling verstuurt dat de volledige route naar de ontvanger moet berekenen, omdat we een "onion routing" systeem gebruiken. De tussenliggende knooppunten kennen noch het punt van herkomst noch de eindbestemming. Ze weten alleen waar de betaling vandaan komt en naar welk knooppunt ze het vervolgens moeten sturen. Dit betekent dat het verzendende knooppunt een dynamische lokale topologie van het netwerk moet bijhouden, met de bestaande Lightning-knooppunten en de kanalen tussen elk, rekening houdend met openingen, sluitingen en statusupdates.


![LNP201](assets/en/061.webp)

Zelfs met deze topologie van de Lightning Network is er essentiële informatie voor de routering die ontoegankelijk blijft voor het verzendende knooppunt, namelijk de exacte verdeling van de liquiditeit in de kanalen op elk gegeven moment. Elk kanaal toont namelijk alleen zijn **totale capaciteit**, maar de interne verdeling van de fondsen is alleen bekend bij de twee deelnemende knooppunten. Dit vormt een uitdaging voor efficiënte routering, aangezien het succes van de betaling met name afhangt van het feit of het bedrag lager is dan de laagste liquiditeit op de gekozen route. De liquiditeiten zijn echter niet allemaal zichtbaar voor het verzendende knooppunt.

![LNP201](assets/en/062.webp)


### Netwerkkaart bijwerken


Om hun netwerkkaart up-to-date te houden, sturen knooppunten regelmatig Exchange berichten via een algoritme genaamd "**_gossip_**". Dit is een gedistribueerd algoritme dat gebruikt wordt om informatie op een epidemische manier te verspreiden naar alle knooppunten in het netwerk, wat Exchange en synchronisatie van de Global State van de kanalen mogelijk maakt in een paar communicatiecycli. Elk knooppunt verspreidt informatie naar een of meer al dan niet willekeurig gekozen buren, deze verspreiden op hun beurt de informatie naar andere buren enzovoort totdat een globaal gesynchroniseerde toestand is bereikt.


De 2 belangrijkste berichten die worden uitgewisseld tussen Lightning nodes zijn de volgende:



- "**Kanaalaankondigingen**": berichten die de opening van een nieuw kanaal aankondigen.
- "**Channel Updates**": updateberichten over de toestand van een kanaal, met name over de ontwikkeling van vergoedingen (maar niet over de verdeling van liquiditeit).


Lightning nodes monitoren ook de Bitcoin Blockchain om kanaalsluitende transacties te detecteren. Het gesloten kanaal wordt dan van de kaart verwijderd, omdat het niet langer gebruikt kan worden om onze betalingen te routeren.


### Een betaling doorsturen


Laten we een voorbeeld nemen van een kleine Lightning Network met 7 knooppunten: Alice, Bob, 1, 2, 3, 4 en 5. Stel dat Alice een betaling wil sturen naar Bob, maar via tussenliggende knooppunten moet gaan.


![LNP201](assets/en/063.webp)


Hier is de werkelijke verdeling van fondsen in deze kanalen:



- Kanaal tussen Alice en **1**: 250.000 Sats aan de kant van Alice, 80.000 aan de kant van 1 (totale capaciteit van 330.000 Sats).
- **Kanaal tussen 1 en 2**: 300.000 Sats aan de kant van 1, 200.000 aan de kant van 2 (totale capaciteit van 500.000 Sats).
- **Kanaal tussen 2 en 3**: 50.000 Sats aan de kant van 2, 60.000 aan de kant van 3 (totale capaciteit van 110.000 Sats).
- Kanaal tussen 2 en 5: 90.000 Sats aan kant 2, 160.000 aan kant 5 (totale capaciteit van 250.000 Sats).
- Kanaal tussen 2 en 4: 180.000 Sats aan kant 2, 110.000 aan kant 4 (totale capaciteit van 290.000 Sats).
- **Kanaal tussen 4 en 5**: 200.000 Sats aan kant 4, 10.000 aan kant 5 (totale capaciteit van 210.000 Sats).
- Kanaal tussen 3 en **Bob**: 50.000 Sats aan kant 3, 250.000 aan kant Bob (totale capaciteit van 300.000 Sats).
- Kanaal tussen 5 en **Bob**: 260.000 Sats aan kant 5, 100.000 aan kant Bob (totale capaciteit van 360.000 Sats).


![LNP201](assets/en/064.webp)


Om een betaling van 100.000 Sats te doen van Alice naar Bob, worden de routingopties beperkt door de beschikbare liquiditeit in elk kanaal. De optimale route voor Alice, gebaseerd op de bekende liquiditeitsverdelingen, zou de reeks `Alice → 1 → 2 → 4 → 5 → Bob` kunnen zijn:


![LNP201](assets/en/065.webp)


Maar omdat Alice de exacte verdeling van fondsen in elk kanaal niet kent, moet ze de optimale route waarschijnlijk schatten, rekening houdend met de volgende criteria:



- **Waarschijnlijkheid van succes**: het is waarschijnlijker dat een kanaal met een hogere totale capaciteit voldoende liquiditeit bevat. Bijvoorbeeld, het kanaal tussen knooppunt 2 en knooppunt 3 heeft een totale capaciteit van 110.000 Sats, dus het is onwaarschijnlijk om 100.000 Sats of meer te vinden aan de kant van knooppunt 2, hoewel het mogelijk blijft.
- **Transactiekosten**: bij het kiezen van de beste route houdt het verzendende knooppunt ook rekening met de kosten die door elk tussenliggend knooppunt worden aangerekend en probeert het de totale routeringskosten te minimaliseren.
- **Vervaldatum van HTLC's**: om geblokkeerde betalingen te vermijden, is de vervaldatum van HTLC's ook een parameter om rekening mee te houden.
- **Aantal tussenliggende knooppunten**: Tot slot, meer in het algemeen, zal het verzendende knooppunt proberen een route te vinden met zo min mogelijk knooppunten om het risico op mislukking te verkleinen en Lightning-transactiekosten te beperken.


Door deze criteria te analyseren, kan het verzendende knooppunt de meest waarschijnlijke routes testen en proberen deze te optimaliseren. In ons voorbeeld zou Alice de beste routes als volgt kunnen rangschikken:



- `Alice → 1 → 2 → 5 → Bob`, omdat dit de kortste route is met de hoogste capaciteit.
- gW-458 → 1 → 2 → 4 → 5 → Bob`, omdat deze route goede capaciteiten biedt, hoewel hij langer is dan de eerste.
- `Alice → 1 → 2 → 3 → Bob`, omdat deze route het kanaal `2 → 3` bevat, dat een zeer beperkte capaciteit heeft, maar potentieel bruikbaar blijft.


### Uitvoering van betalingen


Alice besluit haar eerste route te testen (`Alice → 1 → 2 → 5 → Bob`). Ze stuurt daarom een HTLC van 100.000 Sats naar knooppunt 1. Dit knooppunt controleert of het voldoende liquiditeit heeft bij knooppunt 2 en zet de transmissie voort. Dit knooppunt controleert of het voldoende liquiditeit heeft bij knooppunt 2 en gaat verder met de verzending. Knooppunt 2 ontvangt vervolgens de HTLC van knooppunt 1, maar realiseert zich dat het niet genoeg liquiditeit in zijn kanaal met knooppunt 5 heeft om een betaling van 100.000 Sats door te sturen. Het stuurt dan een foutbericht terug naar knooppunt 1, die het doorstuurt naar Alice. Deze route is mislukt.


![LNP201](assets/en/066.webp)


Alice probeert dan haar betaling te routeren via haar tweede route (`Alice → 1 → 2 → 4 → 5 → Bob`). Ze stuurt een HTLC van 100.000 Sats naar knooppunt 1, die het doorzendt naar knooppunt 2, vervolgens naar knooppunt 4, naar knooppunt 5 en tenslotte naar Bob. Dit keer is er voldoende liquiditeit en de route is goed. Deze keer is de liquiditeit voldoende en is de route functioneel. Elk knooppunt ontgrendelt zijn HTLC in cascade met behulp van het preimage van Bob (het geheim _s_), waardoor de betaling van Alice aan Bob succesvol kan worden afgerond.


![LNP201](assets/en/067.webp)


Het zoeken naar een route verloopt als volgt: het verzendende knooppunt begint met het identificeren van de best mogelijke routes en probeert vervolgens achtereenvolgens betalingen totdat een functionele route is gevonden.


Het is vermeldenswaard dat Bob Alice kan voorzien van informatie in de **Invoice** om de routering te vergemakkelijken. Hij kan bijvoorbeeld kanalen in de buurt met voldoende liquiditeit aangeven of het bestaan van privékanalen onthullen. Deze aanwijzingen stellen Alice in staat om routes met weinig kans op succes te vermijden en eerst de door Bob aanbevolen paden te proberen.


**Wat moet je meenemen uit dit hoofdstuk?**



- Knooppunten houden de netwerktopologie in kaart via aankondigingen en door kanaalsluitingen op de Bitcoin Blockchain te controleren.
- Het zoeken naar een optimale route voor een betaling blijft probabilistisch en hangt af van veel criteria.
- Bob kan aanwijzingen geven in de **Invoice** om de routering van Alice te leiden en haar te behoeden voor het testen van onwaarschijnlijke routes.


In het volgende hoofdstuk zullen we specifiek de werking van facturen bestuderen, naast enkele andere tools die gebruikt worden op de Lightning Network.


# De gereedschappen van de Lightning Network


<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>


## Invoice, LNURL en Keysend


<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>

:::video id=309c3412-506e-4189-ad46-5e5088c55008:::


In dit hoofdstuk gaan we dieper in op de werking van Lightning **facturen**, dat wil zeggen betalingsverzoeken die door het ontvangende knooppunt naar het verzendende knooppunt worden gestuurd. Het doel is om te begrijpen hoe je betalingen kunt uitvoeren en ontvangen op Lightning. We bespreken ook 2 alternatieven voor klassieke facturen: LNURL en Keysend.


![LNP201](assets/en/068.webp)


### De structuur van Lightning-facturen


Zoals uitgelegd in het hoofdstuk over HTLC's, begint elke betaling met het genereren van een **Invoice** door de ontvanger. Deze Invoice wordt dan doorgestuurd naar de betaler (via een QR-code of door te kopiëren) om de betaling te initiëren. Een Invoice bestaat uit twee hoofdonderdelen:



- **Het menselijk leesbare gedeelte**: dit gedeelte bevat duidelijk zichtbare metagegevens om de gebruikerservaring te verbeteren.
- **De payload**: dit gedeelte bevat informatie die bedoeld is voor machines om de betaling te verwerken.


De typische structuur van een Invoice begint met een identificator `LN` voor "Lightning", gevolgd door `bc` voor Bitcoin, dan de hoeveelheid van de Invoice. Een scheidingsteken `1` onderscheidt het menselijk leesbare deel van het gegevens (payload) deel.


Laten we de volgende Invoice als voorbeeld nemen:


```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```


We kunnen het al opdelen in 2 delen. Ten eerste is er het menselijk leesbare deel:


```invoice
lnbc100u
```


Dan het deel dat bedoeld is voor de nuttige lading:


```invoice

p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```


De twee delen worden gescheiden door een `1`. Dit scheidingsteken is gekozen in plaats van een speciaal teken om het kopiëren van de hele Invoice te vergemakkelijken door te dubbelklikken.


In het eerste deel kunnen we dat zien:



- `LN` geeft aan dat het een Lightning-transactie is.
- `bc` geeft aan dat de Lightning Network op de Bitcoin Blockchain staat (en niet op de Testnet of op Litecoin).
- `100u` geeft de hoeveelheid Invoice aan, uitgedrukt in **microbitcoins** (`u` betekent "micro"), wat hier gelijk is aan 10.000 Sats.


Om het betalingsbedrag aan te duiden, wordt het uitgedrukt in subeenheden van Bitcoin. Dit zijn de gebruikte eenheden:



- **Millibitcoin (aangeduid met `m`):** Vertegenwoordigt een duizendste van een Bitcoin.


$$
1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satoshis}
$$



- **Microbitcoin (ook wel `u` genoemd):** Wordt ook wel "bit" genoemd, staat voor een miljoenste van een Bitcoin.


$$
1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satoshis}
$$



- **Nanobitcoin (aangeduid met `n`):** Vertegenwoordigt een miljardste van een Bitcoin.


$$
1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satoshis}
$$



- **Picobitcoin (aangeduid met `p`):** Vertegenwoordigt een triljoenste van een Bitcoin.

$$
1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satoshis}
$$


### De lading van een Invoice


De payload van een Invoice bevat verschillende stukjes informatie die nodig zijn voor het verwerken van de betaling:



- **De Timestamp:** Het moment waarop de Invoice werd aangemaakt, uitgedrukt in Unix Timestamp (het aantal seconden dat verstreken is sinds 1 januari 1970).
- **Hashing van het geheim**: Zoals we zagen in de sectie over HTLC's, moet het ontvangende knooppunt het verzendende knooppunt voorzien van de Hash van het preimage. Dit wordt gebruikt in HTLC's om de transactie te beveiligen. We hebben hiernaar verwezen als "_r_".
- **Het betalingsgeheim**: Een ander geheim wordt gegenereerd door de ontvanger, maar deze keer wordt het doorgestuurd naar het verzendende knooppunt. Het wordt gebruikt in onion routing om te voorkomen dat tussenliggende knooppunten raden of het volgende knooppunt de uiteindelijke ontvanger is of niet. Dit zorgt dus voor een vorm van vertrouwelijkheid voor de ontvanger ten opzichte van het laatste tussenliggende knooppunt op de route.
- **De openbare sleutel van de ontvanger**: Geeft aan de betaler de identifier van de te betalen persoon.
- **De aflooptijd**: De maximale tijd voor de Invoice om betaald te worden (standaard 1 uur).
- **Routing Hints**: Extra informatie verstrekt door de ontvanger om de verzender te helpen de betalingsroute te optimaliseren.
- **De handtekening**: Garandeert de integriteit van de Invoice door alle informatie te verifiëren.


De facturen worden dan gecodeerd in **bech32**, hetzelfde formaat als voor Bitcoin SegWit adressen (formaat dat begint met `bc1`).


### LNURL Terugtrekking


Bij een traditionele transactie, zoals een aankoop in een winkel, wordt de Invoice gegenereerd voor het totale te betalen bedrag. Zodra de Invoice wordt aangeboden (in de vorm van een QR-code of tekenreeks), kan de klant deze scannen en de transactie afronden. De betaling volgt dan het traditionele proces dat we in de vorige sectie bestudeerden. Dit proces kan soms echter erg omslachtig zijn voor de gebruikerservaring, omdat de ontvanger informatie naar de verzender moet sturen via de Invoice.


Voor bepaalde situaties, zoals het opnemen van bitcoins van een online dienst, is het traditionele proces te omslachtig. In zulke gevallen vereenvoudigt de **LNURL** opnameoplossing dit proces door een QR-code weer te geven die de Wallet van de ontvanger scant om automatisch de Invoice aan te maken. De dienst betaalt vervolgens de Invoice, en de gebruiker ziet gewoon een onmiddellijke opname.


![LNP201](assets/en/069.webp)


LNURL is een communicatieprotocol dat een reeks functionaliteiten specificeert die ontworpen zijn om interacties tussen Lightning nodes en clients en toepassingen van derden te vereenvoudigen. De LNURL terugtrekking, zoals we zojuist hebben gezien, is dus slechts een voorbeeld onder andere functionaliteiten.

Dit protocol is gebaseerd op HTTP en maakt het mogelijk om links aan te maken voor verschillende handelingen, zoals een betalingsverzoek, een opnameverzoek of andere functionaliteiten die de gebruikerservaring verbeteren. Elke LNURL is een bech32 gecodeerde URL met het voorvoegsel lnurl, die na het scannen een reeks automatische acties activeert op de Lightning Wallet.

De LNURL-Withdraw (LUD-03) functie maakt het bijvoorbeeld mogelijk om geld op te nemen van een dienst door het scannen van een QR-code, zonder de noodzaak om handmatig generate en Invoice te gebruiken. Op dezelfde manier maakt LNURL-auth (LUD-04) het mogelijk om in te loggen op online diensten met behulp van een privésleutel op iemands Lightning Wallet in plaats van een wachtwoord.


### Een Lightning-betaling verzenden zonder Invoice: Keysend


Een ander interessant geval is het overmaken van geld zonder vooraf een Invoice te hebben ontvangen, bekend als "**Keysend**". Dit protocol maakt het mogelijk om geld te versturen door een preimage toe te voegen aan de versleutelde betalingsgegevens, alleen toegankelijk voor de ontvanger. Dit preimage stelt de ontvanger in staat om de HTLC te ontgrendelen en zo het geld op te halen zonder eerst een Invoice te hebben gegenereerd.


Eenvoudigheidshalve is het in dit protocol de verzender die het geheim genereert dat in de HTLC's wordt gebruikt, in plaats van de ontvanger. In de praktijk kan de verzender hierdoor een betaling doen zonder eerst contact te hebben gehad met de ontvanger.


![LNP201](assets/en/070.webp)


**Wat moet je meenemen uit dit hoofdstuk?**



- Een **Lightning Invoice** is een betalingsverzoek dat bestaat uit een menselijk leesbaar deel en een machinegegevensdeel.
- De Invoice is gecodeerd in **bech32**, met een `1` scheidingsteken om het kopiëren te vergemakkelijken en een datadeel dat alle informatie bevat die nodig is om de betaling te verwerken.
- Er bestaan andere betalingsprocessen op Lightning, met name **LNURL-Withdraw** om opnames te vergemakkelijken, en **Keysend** voor directe overschrijvingen zonder Invoice.


In het volgende hoofdstuk zullen we zien hoe een node operator de liquiditeit in zijn kanalen kan beheren, om nooit geblokkeerd te worden en altijd betalingen te kunnen verzenden en ontvangen op de Lightning Network.


## Uw liquiditeit beheren


<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>


:::video id=96096aef-e4ce-4c44-a022-57e27082232a:::


In dit hoofdstuk onderzoeken we strategieën voor effectief liquiditeitsbeheer op de Lightning Network. Liquiditeitsbeheer varieert afhankelijk van het type gebruiker en de context. We zullen kijken naar de belangrijkste principes en bestaande technieken om beter te begrijpen hoe we dit beheer kunnen optimaliseren.


### Liquiditeitsbehoeften


Er zijn drie hoofdgebruikersprofielen op Lightning, elk met specifieke liquiditeitsbehoeften:



- **De Betaler**: Dit is degene die betalingen doet. Ze hebben uitgaande liquiditeit nodig om geld over te kunnen maken naar andere gebruikers. Dit kan bijvoorbeeld een consument zijn.
- **De verkoper (of begunstigde)**: Dit is degene die betalingen ontvangt. Ze hebben inkomende liquiditeit nodig om betalingen naar hun node te kunnen accepteren. Dit kan bijvoorbeeld een bedrijf of een online winkel zijn.
- **De router**: Een tussenliggend knooppunt, vaak gespecialiseerd in het routeren van betalingen, dat zijn liquiditeit in elk kanaal moet optimaliseren om zoveel mogelijk betalingen te routeren en vergoedingen te verdienen.


Deze profielen liggen natuurlijk niet vast; een gebruiker kan wisselen tussen betaler en begunstigde, afhankelijk van de transacties. Bob zou bijvoorbeeld zijn salaris op Lightning kunnen ontvangen van zijn werkgever, waardoor hij in de positie komt van een "verkoper" die inkomende liquiditeit nodig heeft. Als hij vervolgens zijn salaris wil gebruiken om voedsel te kopen, wordt hij een "betaler" en heeft hij uitgaande liquiditeit nodig.


Om het beter te begrijpen, nemen we het voorbeeld van een eenvoudig netwerk dat bestaat uit drie knooppunten: de koper (Alice), de router (Suzie) en de verkoper (Bob).


![LNP201](assets/en/071.webp)


Stel dat de koper 30.000 Sats naar de verkoper wil sturen en dat de betaling via het knooppunt van de router gaat. Elke partij moet dan een minimale hoeveelheid liquiditeit hebben in de richting van de betaling:



- De betaler moet ten minste 30.000 satoshis hebben aan zijn kant van het kanaal met de router.
- De verkoper moet een kanaal hebben met 30.000 satoshi's aan de andere kant om ze te kunnen ontvangen.
- De router moet 30.000 satoshis hebben aan de kant van de betaler in zijn kanaal, en ook 30.000 satoshis aan zijn kant in het kanaal met de verkoper, om de betaling te kunnen routeren.


![LNP201](assets/en/072.webp)


### Strategieën voor liquiditeitsbeheer


Betalers moeten zorgen voor voldoende liquiditeit aan hun kant van de kanalen om uitgaande liquiditeit te garanderen. Dit blijkt relatief eenvoudig te zijn, aangezien het voldoende is om nieuwe Lightning-kanalen te openen om over deze liquiditeit te beschikken. De initiële fondsen die in de Multisig On-Chain zijn opgesloten, bevinden zich bij aanvang immers volledig aan de kant van de betaler in het Lightning-kanaal. De betalingscapaciteit is dus verzekerd zolang er kanalen worden geopend met voldoende fondsen. Als de uitgaande liquiditeit op is, is het voldoende om nieuwe kanalen te openen.

Aan de andere kant is de taak voor de verkoper complexer. Om betalingen te kunnen ontvangen, moeten ze liquiditeit hebben aan de andere kant van hun kanalen. Daarom is het openen van een kanaal niet genoeg: ze moeten ook een betaling doen in dit kanaal om de liquiditeit naar de andere kant te verplaatsen voordat ze zelf betalingen kunnen ontvangen. Voor bepaalde Lightning gebruikersprofielen, zoals handelaren, is er een duidelijke wanverhouding tussen wat hun node verstuurt en wat het ontvangt, aangezien het doel van een bedrijf in de eerste plaats is om meer te verzamelen dan het uitgeeft, om generate winst te maken. Gelukkig bestaan er voor deze gebruikers met specifieke inkomende liquiditeitsbehoeften verschillende oplossingen:



- **Kanalen aantrekken**: De merchant heeft een voordeel door het volume aan inkomende betalingen dat op zijn node wordt verwacht. Hiermee rekening houdend kunnen ze proberen routeringsknooppunten aan te trekken die op zoek zijn naar inkomsten uit transactievergoedingen en die mogelijk kanalen naar hen openen in de hoop hun betalingen te routeren en de bijbehorende vergoedingen te innen.



- **Liquiditeitsbeweging**: De verkoper kan ook een kanaal openen en een deel van het geld naar de andere kant overmaken door fictieve betalingen te doen aan een ander knooppunt, dat het geld op een andere manier zal teruggeven. We zullen in het volgende deel zien hoe we deze operatie kunnen uitvoeren.



- **Driehoeksopening**: Er bestaan platformen voor knooppunten die samen kanalen willen openen, zodat elk kan profiteren van onmiddellijke inkomende en uitgaande liquiditeit. Bijvoorbeeld, [LightningNetwork+](https://lightningnetwork.plus/) biedt deze service. Als Alice, Bob en Suzie een kanaal willen openen met 100.000 Sats, kunnen ze op dit platform afspreken dat Alice een kanaal opent naar Bob, Bob naar Suzie en Suzie naar Alice. Op deze manier heeft ieder 100.000 Sats aan uitgaande liquiditeit en 100.000 Sats aan inkomende liquiditeit, terwijl ze slechts 100.000 Sats hebben opgesloten.


![LNP201](assets/en/073.webp)



- **Kanalen kopen**: Er bestaan ook diensten voor het huren van Lightning-kanalen om inkomende liquiditeit te verkrijgen, zoals [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) of [Lightning Labs Pool](https://lightning.engineering/pool/). Alice kan bijvoorbeeld een kanaal van een miljoen satoshis naar haar node kopen om betalingen te ontvangen.


![LNP201](assets/en/074.webp)


Tot slot moeten routers, die als doel hebben het aantal verwerkte betalingen en de geïnde vergoedingen te maximaliseren:



- Open goed gefinancierde kanalen met strategische knooppunten.
- Pas de verdeling van fondsen in de kanalen regelmatig aan volgens de behoeften van het netwerk.


### De Loop Out Service


De [Loop Out](https://lightning.engineering/loop/) dienst, aangeboden door Lightning Labs, maakt het mogelijk om liquiditeit te verplaatsen naar de andere kant van het kanaal, terwijl de fondsen op de Bitcoin Blockchain worden teruggevorderd. Alice stuurt bijvoorbeeld 1 miljoen satoshi via Lightning naar een loop-node, die haar dat geld teruggeeft in On-Chain bitcoins. Dit brengt haar kanaal in balans met 1 miljoen satos aan elke kant, waardoor haar capaciteit om betalingen te ontvangen wordt geoptimaliseerd.


![LNP201](assets/en/075.webp)


Daarom maakt deze service inkomende liquiditeit mogelijk terwijl men zijn bitcoins On-Chain terugvordert, wat helpt om de immobilisatie van contant geld te beperken die nodig is om betalingen met Lightning te accepteren.


**Wat moet je meenemen uit dit hoofdstuk?**



- Om betalingen op Lightning te verzenden, moet u voldoende liquiditeit aan uw kant hebben in uw kanalen. Om deze verzendcapaciteit te verhogen, opent u gewoon nieuwe kanalen.
- Om betalingen te ontvangen, moet je aan de andere kant liquiditeit hebben in je kanalen. Het vergroten van deze ontvangstcapaciteit is complexer, omdat het vereist dat anderen kanalen naar je toe openen of (fictieve of echte) betalingen doen om de liquiditeit naar de andere kant te verplaatsen.
- De gewenste liquiditeit behouden kan een nog grotere uitdaging zijn, afhankelijk van het gebruik van de kanalen. Daarom bestaan er tools en diensten om de kanalen naar wens in balans te houden.


In het volgende hoofdstuk stel ik voor om de belangrijkste concepten van deze training te bespreken.


# Ga verder


<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>


## Samenvatting van de cursus



<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>


:::video id=5f4f4344-ef27-4765-8f09-8262e6833bde:::


In dit laatste hoofdstuk, dat het einde van de LNP201-training markeert, stel ik voor om de belangrijke concepten die we samen hebben behandeld nog eens de revue te laten passeren.


Het doel van deze training was om je een uitgebreid en technisch inzicht te geven in de Lightning Network. We ontdekten hoe de Lightning Network vertrouwt op de Bitcoin Blockchain om off-chain transacties uit te voeren, terwijl de fundamentele kenmerken van Bitcoin behouden blijven, met name de afwezigheid van de noodzaak om andere nodes te vertrouwen.


### Betalingskanalen


In de eerste hoofdstukken hebben we onderzocht hoe twee partijen, door het openen van een betalingskanaal, transacties kunnen uitvoeren buiten de Bitcoin Blockchain. Dit zijn de stappen die zijn behandeld:



- **Kanaal openen**: Het aanmaken van het kanaal gebeurt via een Bitcoin transactie die de fondsen vergrendelt in een 2/2 Address met meerdere handtekeningen. Deze storting vertegenwoordigt het Lightning-kanaal op de Blockchain.


![LNP201](assets/en/076.webp) 2. **Transactions in the Channel**: In this channel, it is then possible to carry out numerous transactions without having to publish them on the blockchain. Each Lightning transaction creates a new state of the channel reflected in a commitment transaction.

![LNP201](assets/en/077.webp)



- **Beveiligen en afsluiten**: Deelnemers committeren zich aan de nieuwe toestand van het kanaal door revocatiesleutels uit te wisselen om de fondsen te beveiligen en valsspelen te voorkomen. Beide partijen kunnen het kanaal gezamenlijk sluiten door een nieuwe transactie op de Bitcoin Blockchain, of als laatste redmiddel door een gedwongen sluiting. Deze laatste optie, hoewel minder efficiënt omdat het langer duurt en soms slecht geëvalueerd is in termen van vergoedingen, maakt het nog steeds mogelijk om fondsen terug te krijgen. In geval van valsspelen kan het slachtoffer de valsspeler straffen door alle fondsen van het kanaal op de Blockchain terug te vorderen.


![LNP201](assets/en/078.webp)


### Het netwerk van kanalen


Na het bestuderen van geïsoleerde kanalen hebben we onze analyse uitgebreid naar het netwerk van kanalen:



- **Routing**: Als twee partijen niet rechtstreeks met elkaar verbonden zijn via een kanaal, kan het netwerk routeren via tussenliggende knooppunten. Betalingen gaan dan van het ene knooppunt naar het andere.


![LNP201](assets/en/079.webp)



- **HTLC's**: Betalingen die via tussenliggende knooppunten lopen, worden beveiligd door "_Hash Time-Locked Contracts_" (HTLC), die ervoor zorgen dat de fondsen worden vergrendeld totdat de betaling end-to-end is voltooid.


![LNP201](assets/en/080.webp)



- **Uienroutering**: Om de vertrouwelijkheid van de betaling te garanderen, verbergt onion routing de eindbestemming voor tussenliggende knooppunten. Het verzendende knooppunt moet daarom de volledige route berekenen, maar omdat het geen volledige informatie heeft over de liquiditeit van de kanalen, doorloopt het opeenvolgende pogingen om de betaling te routeren.


![LNP201](assets/en/081.webp)


### Liquiditeitsbeheer


We hebben gezien dat liquiditeitsbeheer een uitdaging is voor Lightning om een soepele stroom van betalingen te garanderen. Het verzenden van betalingen is relatief eenvoudig: je hoeft alleen maar een kanaal te openen. Voor het ontvangen van betalingen is het echter nodig om liquiditeit te hebben aan de andere kant van je kanalen. Hier worden enkele strategieën besproken:



- **Kanalen aantrekken**: Door andere knooppunten aan te moedigen kanalen naar zichzelf te openen, verkrijgt een gebruiker inkomende liquiditeit.



- **Liquiditeit verplaatsen**: Door betalingen naar andere kanalen te sturen, verschuift liquiditeit naar de andere kant.


![LNP201](assets/en/082.webp)



- Diensten zoals **Loop en Pool** gebruiken: Deze diensten maken herbalancering of het kopen van kanalen met liquiditeit aan de andere kant mogelijk.

![LNP201](assets/en/083.webp)


- **Gezamenlijke openingen**: Er zijn ook platforms beschikbaar voor het verbinden om driehoeksopeningen uit te voeren en om inkomende liquiditeit te hebben.


![LNP201](assets/en/084.webp)


# Laatste Sectie


<partId>b8715c1c-7ae2-49b7-94c7-35bf85346ad3</partId>


## Beoordelingen


<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>

<isCourseReview>true</isCourseReview>

## Eindexamen


<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>

<isCourseExam>true</isCourseExam>

## Conclusie


<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>

<isCourseConclusion>true</isCourseConclusion>