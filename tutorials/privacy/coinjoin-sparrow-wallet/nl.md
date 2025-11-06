---
name: CoinJoin - Sparrow wallet
description: Hoe voer je een CoinJoin uit op Sparrow wallet?
---
![cover](assets/cover.webp)


***WAARSCHUWING:** Na de arrestatie van de oprichters van Samourai Wallet en de inbeslagname van hun servers op 24 april, werkt de Whirlpool tool niet meer, zelfs niet voor individuen die hun eigen Dojo hebben of Sparrow wallet gebruiken. Het blijft echter mogelijk dat deze tool in de komende weken weer in gebruik wordt genomen of op een andere manier opnieuw wordt gelanceerd. Bovendien blijft het theoretische deel van dit artikel relevant voor het begrijpen van de principes en doelstellingen van coinjoins in het algemeen (niet alleen Whirlpool), en voor het begrijpen van de effectiviteit van het Whirlpool model.*


we volgen de ontwikkelingen van deze zaak en de ontwikkelingen met betrekking tot de bijbehorende tools op de voet. Wees gerust dat we deze handleiding zullen bijwerken zodra er nieuwe informatie beschikbaar is._


deze handleiding is alleen bedoeld voor educatieve en informatieve doeleinden. We keuren het gebruik van deze tools voor criminele doeleinden niet goed en moedigen dit ook niet aan. Het is de verantwoordelijkheid van elke gebruiker om te voldoen aan de wetten in hun rechtsgebied._


---

In deze tutorial leer je wat een CoinJoin is en hoe je er een uitvoert met behulp van de Sparrow wallet software en de Whirlpool implementatie.


## Wat is een CoinJoin op Bitcoin?

**Een CoinJoin is een techniek die de traceerbaarheid van bitcoins op de Blockchain verbreekt**. Het vertrouwt op een collaboratieve transactie met een specifieke structuur met dezelfde naam: de CoinJoin transactie.


Coinjoins verbeteren de privacy van Bitcoin gebruikers door ketenanalyse voor externe waarnemers te bemoeilijken. Hun structuur maakt het mogelijk om meerdere munten van verschillende gebruikers samen te voegen in één transactie, waardoor de sporen vervagen en het moeilijk wordt om de links tussen invoer- en uitvoeradressen te bepalen.


Het principe van de CoinJoin is gebaseerd op een collaboratieve aanpak: verschillende gebruikers die hun bitcoins willen mengen, storten identieke bedragen als input van dezelfde transactie. Deze bedragen worden vervolgens herverdeeld als outputs van gelijke waarde voor elke gebruiker. Aan het einde van de transactie wordt het onmogelijk om een specifieke output te associëren met een bekende gebruiker bij de input. Er bestaat geen direct verband tussen de inputs en outputs, waardoor de associatie tussen de gebruikers en hun UTXO verbroken wordt, evenals de geschiedenis van elke Coin.

![coinjoin](assets/notext/1.webp)


Voorbeeld van een CoinJoin transactie (niet van mij): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


Om een CoinJoin uit te voeren en er tegelijkertijd voor te zorgen dat elke gebruiker te allen tijde de controle over zijn geld behoudt, begint het proces met het samenstellen van de transactie door een coördinator, die deze vervolgens doorstuurt naar elke deelnemer. Elke gebruiker ondertekent dan de transactie nadat hij geverifieerd heeft dat deze bij hem past. Alle verzamelde handtekeningen worden uiteindelijk geïntegreerd in de transactie. Als een gebruiker of de coördinator probeert geld om te leiden door de uitvoer van de CoinJoin transactie aan te passen, zullen de handtekeningen ongeldig blijken, wat leidt tot afwijzing van de transactie door de knooppunten.


Er zijn verschillende implementaties van CoinJoin, zoals Whirlpool, JoinMarket of Wabisabi, elk met als doel de coördinatie tussen deelnemers te beheren en de efficiëntie van CoinJoin transacties te verhogen.


In deze tutorial richten we ons op de **Whirlpool** implementatie, die ik beschouw als de meest effectieve oplossing voor het uitvoeren van coinjoins op Bitcoin. Hoewel het beschikbaar is op verschillende wallets, wordt in deze tutorial uitsluitend het gebruik met de Sparrow wallet Desktop software onderzocht.

## Waarom CoinJoins uitvoeren op Bitcoin?


Een van de eerste problemen met elk peer-to-peer betalingssysteem is Double-spending: hoe voorkom je dat kwaadwillende individuen dezelfde monetaire eenheden meerdere keren uitgeven zonder hun toevlucht te nemen tot een centrale autoriteit voor arbitrage?


Satoshi Nakamoto bood een oplossing voor dit dilemma met het Bitcoin protocol, een peer-to-peer elektronisch betalingssysteem dat onafhankelijk van enige centrale autoriteit opereert. In zijn white paper benadrukt hij dat de enige manier om de afwezigheid van Double-spending te garanderen, is om de zichtbaarheid van alle transacties binnen het betalingssysteem te garanderen.


Om er zeker van te zijn dat elke deelnemer op de hoogte is van de transacties, moeten ze openbaar worden gemaakt. De werking van Bitcoin berust dus op een transparante en gedistribueerde infrastructuur, waardoor elke knooppuntoperator de hele elektronische handtekeningketen en de geschiedenis van elke Coin kan verifiëren, vanaf het aanmaken ervan door een Miner.


Het transparante en gedistribueerde karakter van Blockchain betekent dat elke netwerkgebruiker de transacties van alle andere deelnemers kan volgen en analyseren. Bijgevolg is anonimiteit op transactieniveau onmogelijk. De anonimiteit blijft echter behouden op het niveau van individuele identificatie. In tegenstelling tot het traditionele banksysteem, waar elke rekening gekoppeld is aan een persoonlijke identiteit, worden op Bitcoin fondsen geassocieerd met paren cryptografische sleutels, waardoor gebruikers een vorm van pseudonimiteit krijgen achter cryptografische identifiers.


Daarom wordt de privacy op Bitcoin aangetast wanneer externe waarnemers erin slagen om specifieke UTXO's te associëren met geïdentificeerde gebruikers. Zodra deze associatie is vastgesteld, wordt het mogelijk om hun transacties te traceren en de geschiedenis van hun bitcoins te analyseren. CoinJoin is juist een techniek die ontwikkeld is om de traceerbaarheid van UTXO's te doorbreken en zo Layer een zekere privacy te bieden aan Bitcoin gebruikers op transactieniveau.


## Hoe werkt Whirlpool?


Whirlpool onderscheidt zich van andere CoinJoin methoden door het gebruik van "_ZeroLink_" transacties, die ervoor zorgen dat er strikt geen technisch verband mogelijk is tussen alle inputs en alle outputs. Deze perfecte vermenging wordt bereikt door een structuur waarbij elke deelnemer een identieke hoeveelheid input bijdraagt (behalve de Mining vergoedingen), waardoor outputs van perfect gelijke hoeveelheden worden gegenereerd.


Deze restrictieve benadering van de inputs geeft Whirlpool CoinJoin transacties een uniek kenmerk: de totale afwezigheid van deterministische verbanden tussen de inputs en de outputs. Met andere woorden, elke output heeft een gelijke waarschijnlijkheid om te worden toegewezen aan een deelnemer, vergeleken met alle andere outputs van de transactie.

Aanvankelijk was het aantal deelnemers in elke Whirlpool CoinJoin beperkt tot 5, met 2 nieuwkomers en 3 remixers (we zullen deze concepten verderop uitleggen). De stijging van de transactiekosten voor On-Chain die in 2023 werd waargenomen, zette de Samourai-teams er echter toe aan hun model te heroverwegen om de privacy te verbeteren en tegelijkertijd de kosten te verlagen. Dus, rekening houdend met de marktsituatie van vergoedingen en het aantal deelnemers, kan de coördinator nu coinjoins organiseren met 6, 7 of 8 deelnemers. Deze verbeterde sessies worden "_Surge Cycles_" genoemd. Het is belangrijk op te merken dat, ongeacht de opzet, er altijd slechts 2 nieuwe deelnemers zijn in de Whirlpool coinjoins.


Daarom worden Whirlpool transacties gekenmerkt door een identiek aantal in- en uitgangen, die kunnen zijn:


- 5 ingangen en 5 uitgangen;

![coinjoin](assets/notext/2.webp)


- 6 ingangen en 6 uitgangen;

![coinjoin](assets/notext/3.webp)


- 7 ingangen en 7 uitgangen;

![coinjoin](assets/notext/4.webp)


- 8 ingangen en 8 uitgangen.

![coinjoin](assets/notext/5.webp)

Het model dat Whirlpool voorstelt is dus gebaseerd op kleine CoinJoin transacties. In tegenstelling tot Wasabi en JoinMarket, waar de robuustheid van de anonsets afhangt van het aantal deelnemers in een enkele cyclus, zet Whirlpool in op het aaneenschakelen van meerdere kleine cycli.


In dit model betaalt de gebruiker alleen kosten bij zijn eerste toetreding tot een pool, waardoor hij kan deelnemen aan een groot aantal remixes zonder extra kosten. Het zijn de nieuwkomers die de Mining vergoedingen voor de remixers betalen.


Met elke extra CoinJoin waaraan een Coin deelneemt, samen met zijn in het verleden gevonden soortgenoten, zullen de anonsets exponentieel groeien. Het doel is dus om te profiteren van deze gratis remixen, die met elk optreden bijdragen aan het versterken van de dichtheid van de anonsets die geassocieerd zijn met elke gemengde Coin.


Bij het ontwerp van Whirlpool is rekening gehouden met twee belangrijke vereisten:


- De toegankelijkheid van de implementatie op mobiele apparaten, aangezien Samourai Wallet voornamelijk een smartphone-applicatie is;
- De snelheid van de remixing cycli om een significante toename in anonsets te bevorderen.


Deze vereisten leidden de keuzes van de ontwikkelaars van Samourai Wallet in het ontwerp van Whirlpool, waardoor ze het aantal deelnemers per cyclus beperkten. Te weinig deelnemers zou de effectiviteit van de CoinJoin in gevaar hebben gebracht, omdat de anonsets die bij elke cyclus werden gegenereerd drastisch zouden zijn verminderd, terwijl te veel deelnemers problemen zouden hebben opgeleverd bij het beheer van mobiele toepassingen en de doorstroming van de cycli zouden hebben belemmerd.


**Het is uiteindelijk niet nodig om een hoog aantal deelnemers per CoinJoin op Whirlpool te hebben, omdat de anonsets worden gemaakt over de opeenstapeling van meerdere CoinJoin cycli.**

[-> Meer informatie over Whirlpool anonsets] (https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### CoinJoin zwembaden en vergoedingen

Om ervoor te zorgen dat meerdere cycli de anonsets van gemengde munten effectief verhogen, moet een bepaald kader worden vastgesteld om de gebruikte hoeveelheden UTXO's te beperken. Whirlpool definieert verschillende pools voor dit doel.


Een pool vertegenwoordigt een groep gebruikers die samen willen mengen, die overeenkomen hoeveel UTXO's ze willen gebruiken om het CoinJoin proces te optimaliseren. Elke pool specificeert een vast bedrag voor de UTXO, waar de gebruiker zich aan moet houden om te kunnen deelnemen. Om coinjoins uit te voeren met Whirlpool, moet je dus een pool selecteren. De momenteel beschikbare pools zijn als volgt:


- 0.5 bitcoins;
- 0.05 Bitcoin;
- 0.01 Bitcoin;
- 0.001 Bitcoin (= 100.000 Sats).


Als je lid wordt van een pool met je bitcoins, worden ze verdeeld in generate UTXO's die perfect homogeen zijn met die van de andere deelnemers in de pool. Elke pool heeft een maximumlimiet; voor bedragen die deze limiet overschrijden, word je dus gedwongen om twee aparte inschrijvingen te doen binnen dezelfde pool of om over te stappen naar een andere pool met een hoger bedrag:


| Pool (bitcoin) | Maximum amount per entry (bitcoin) |
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

Zoals eerder vermeld, wordt een UTXO geacht deel uit te maken van een groep wanneer hij klaar is om in een CoinJoin geïntegreerd te worden. Dit betekent echter niet dat de gebruiker het bezit ervan verliest. **Door de verschillende mengcycli behoudt je de volledige controle over je sleutels en dus ook over je bitcoins.** Dit is wat de CoinJoin techniek onderscheidt van andere gecentraliseerde mengtechnieken.


Om toe te treden tot een CoinJoin groep, moeten servicekosten en Mining kosten betaald worden. De servicekosten zijn vastgesteld voor elke pool en zijn bedoeld om de teams te compenseren die verantwoordelijk zijn voor de ontwikkeling en het onderhoud van Whirlpool. Voor Sparrow wallet gebruikers worden deze vergoedingen door de Samourai teams doorgegeven aan de ontwikkelaars van Sparrow.


De servicekosten voor het gebruik van Whirlpool moeten eenmalig betaald worden bij het betreden van de pool. Zodra deze stap is voltooid, heb je de mogelijkheid om deel te nemen aan een onbeperkt aantal remixes zonder extra kosten. Hier zijn de huidige vaste kosten voor elke pool:


| Pool (bitcoin) | Entry Fee (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


Deze vergoedingen fungeren in wezen als een toegangsbewijs voor de gekozen pool, ongeacht het bedrag dat je in CoinJoin stopt. Dus of je nu toetreedt tot de 0,01 pool met precies 0,01 BTC of dat je toetreedt met 0,5 BTC, de vergoedingen blijven in absolute waarde gelijk.


Voordat de gebruiker verder gaat met coinjoins, heeft hij dus de keuze tussen 2 strategieën:


- Kies voor een kleinere pool om de servicekosten te minimaliseren, wetende dat ze in ruil daarvoor verschillende kleine UTXO's zullen ontvangen;
- Of ze geven de voorkeur aan een grotere pool en gaan akkoord met het betalen van hogere vergoedingen om te eindigen met een kleiner aantal UTXO's met een grotere waarde.


Over het algemeen wordt afgeraden om meerdere gemengde UTXO's samen te voegen na de CoinJoin cycli, omdat dit de verworven privacy in gevaar kan brengen, vooral door de Common-Input-Ownership Heuristic (CIOH). Daarom kan het verstandig zijn om een grotere pool te kiezen, zelfs als dat betekent dat er meer betaald moet worden, om te voorkomen dat er te veel UTXO's met een kleine waarde als uitvoer komen. De gebruiker moet deze afwegingen maken om de pool te kiezen waaraan hij de voorkeur geeft.


Naast de servicekosten moet ook rekening worden gehouden met de Mining kosten die inherent zijn aan elke Bitcoin transactie. Als Whirlpool gebruiker moet je de Mining kosten voor de voorbereidingstransactie (`Tx0`) betalen, evenals die voor de eerste CoinJoin. Alle volgende remixen zijn gratis, dankzij het model van Whirlpool dat gebaseerd is op betaling van nieuwe toetreders. Alle volgende remixen zijn gratis, dankzij het model van Whirlpool, dat afhankelijk is van de betaling van nieuwe toetreders.


Inderdaad, in elke Whirlpool CoinJoin zijn twee gebruikers onder de input nieuwkomers. De andere input is afkomstig van remixers. Als gevolg daarvan worden de Mining vergoedingen voor alle deelnemers aan de transactie gedekt door deze twee nieuwe deelnemers, die dan ook profiteren van gratis remixen:

![coinjoin](assets/en/6.webp)

Dankzij dit vergoedingensysteem onderscheidt Whirlpool zich echt van andere CoinJoin diensten, omdat de anonimiteit van de UTXO's niet evenredig is met de prijs die de gebruiker betaalt. Het is dus mogelijk om een aanzienlijk hoog niveau van anonimiteit te bereiken door alleen de instapkosten van de pool te betalen en de Mining kosten voor twee transacties (de `Tx0` en de initiële mix).


Het is belangrijk op te merken dat de gebruiker ook de Mining kosten moet betalen om hun UTXO's uit de pool te halen na het voltooien van hun meervoudige coinjoins, tenzij ze de `mix to` optie hebben geselecteerd, die we in de tutorial hieronder zullen bespreken.


### De HD Wallet rekeningen gebruikt door Whirlpool

Om een CoinJoin via Whirlpool uit te voeren, moet de Wallet verschillende afzonderlijke accounts generate. Een account, in de context van een HD (Hierarchical Deterministic) Wallet, vormt een sectie die volledig geïsoleerd is van de anderen, deze scheiding vindt plaats op het derde diepteniveau van de hiërarchie van de Wallet, dat wil zeggen op het niveau van de `xpub`.

Een HD Wallet kan theoretisch tot `2^(32/2)` verschillende accounts afleiden. Het initiële account, dat standaard gebruikt wordt op alle Bitcoin portemonnees, komt overeen met de index `0'`.


Voor portemonnees die aangepast zijn aan Whirlpool, zoals Samourai of Sparrow, worden 4 accounts gebruikt om aan de behoeften van het CoinJoin proces te voldoen:


- De **deposito** rekening, geïdentificeerd door de index `0'`;
- De **slechte bank** (of doxxic change) rekening, geïdentificeerd door de index `2 147 483 644'`;
- De **premix** rekening, geïdentificeerd door de index `2 147 483 645'`;
- De **postmix** rekening, geïdentificeerd door de index `2 147 483 646'`.


Elk van deze accounts vervult een specifieke functie binnen de CoinJoin.


Al deze accounts zijn gekoppeld aan één seed, waarmee de gebruiker toegang kan krijgen tot al zijn bitcoins door zijn herstelzin en, indien van toepassing, zijn passphrase te gebruiken. Het is echter noodzakelijk om tijdens dit herstel aan de software aan te geven welke verschillende accountindexen werden gebruikt.


Laten we nu eens kijken naar de verschillende stadia van een Whirlpool CoinJoin binnen deze rekeningen.


### De verschillende stadia van coinjoins op Whirlpool

**Fase 1: De Tx0**

Het startpunt van elke Whirlpool CoinJoin is de **deposit** account. Dit is het account dat je automatisch gebruikt als je een nieuw Bitcoin Wallet aanmaakt. Deze rekening moet worden gecrediteerd met de bitcoins die je wilt mengen.


De `Tx0` vertegenwoordigt de eerste fase van het Whirlpool mengproces. Het doel is om de UTXO's voor de CoinJoin voor te bereiden en te egaliseren, door ze te verdelen in eenheden die overeenkomen met de hoeveelheid van de geselecteerde pool, om de homogeniteit van het mengen te garanderen. De geëgaliseerde UTXO's worden dan naar de **premix** rekening gestuurd. Het verschil dat niet in de pool kan, wordt gescheiden in een specifieke rekening: de **slechte bank** (of "doxxic change").


Deze initiële transactie `Tx0` dient ook om de servicekosten te vereffenen die verschuldigd zijn aan de mixcoördinator. In tegenstelling tot de volgende fasen is deze transactie niet collaboratief; de gebruiker moet daarom de volledige Mining kosten op zich nemen:

![coinjoin](assets/en/7.webp)

In dit voorbeeld van een transactie `Tx0`, wordt een input van `372.000 Sats` van onze **deposito** rekening verdeeld in verschillende uitgaande UTXO's, die als volgt worden verdeeld:


- Een bedrag van `5.000 Sats` bestemd voor de coördinator servicekosten, overeenkomend met de opname in de pool van `100.000 Sats`;
- Drie UTXO's klaargemaakt voor menging, doorgestuurd naar onze **premix** rekening en geregistreerd bij de coördinator. Deze UTXO's zijn geëgaliseerd op `108.000 Sats` per stuk, om de Mining vergoedingen voor hun toekomstige eerste menging te dekken;
- Het overschot, dat niet in de pool kan omdat het te klein is, wordt beschouwd als giftige verandering. Het wordt naar een specifieke rekening gestuurd. Hier bedraagt deze verandering `40.000 Sats`;
- Tenslotte zijn er `3.000 Sats` die geen uitvoer vormen, maar de Mining vergoedingen zijn die nodig zijn om de `Tx0` te bevestigen.


Hier is bijvoorbeeld een echte Tx0 Whirlpool (die niet van mij komt): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**Stap 2: De giftige verandering**

Het overschot, dat niet in de pool kon worden geïntegreerd, hier gelijk aan `40.000 Sats`, wordt omgeleid naar de **slechte bank** rekening, ook wel `giftige verandering` genoemd, om een strikte scheiding met de andere UTXO's in de Wallet te waarborgen.


Deze UTXO is gevaarlijk voor de privacy van de gebruiker, omdat het niet alleen altijd verbonden is aan het verleden, en dus mogelijk aan de identiteit van de eigenaar, maar bovendien wordt genoteerd als behorend aan een gebruiker die een CoinJoin heeft uitgevoerd.


Als deze UTXO samengevoegd wordt met gemengde uitgangen, zal deze laatste alle privacy verliezen die verworven werd tijdens de CoinJoin cycli, met name door de CIOH (*Common-Input-Ownership-Heuristic*). Als het samengevoegd wordt met andere toxische veranderingen, loopt de gebruiker het risico privacy te verliezen, omdat dit de verschillende ingangen van de CoinJoin cycli met elkaar verbindt. Het moet daarom met voorzichtigheid behandeld worden. De manier om deze giftige UTXO te beheren wordt in het laatste deel van dit artikel beschreven, en toekomstige tutorials zullen dieper ingaan op deze methodes op het PlanB Netwerk.


**Stap 3: De eerste mix**

Na voltooiing van de `Tx0`, worden de geëgaliseerde UTXO's naar de **premix** rekening van onze Wallet gestuurd, klaar om te worden ingevoerd in hun eerste cyclus van CoinJoin, ook wel "initiële mix" genoemd. Als, zoals in ons voorbeeld, de `Tx0` meerdere UTXO's genereert die bedoeld zijn om te mengen, wordt elk van hen geïntegreerd in een aparte initiële CoinJoin.

Aan het einde van deze eerste mixen zal de **premix** rekening leeg zijn, terwijl onze munten, die de Mining vergoedingen voor deze eerste CoinJoin hebben betaald, precies zullen worden aangepast aan het bedrag dat is gedefinieerd door de gekozen pool. In ons voorbeeld zijn onze initiële UTXO's van `108 000 Sats` teruggebracht tot precies `100 000 Sats`.

![coinjoin](assets/en/8.webp)

**Stap 4: De remixen**

Na de eerste mix worden de UTXO's overgebracht naar het **postmix** account. Dit account verzamelt de UTXO's die al gemengd zijn en de UTXO's die wachten om opnieuw gemengd te worden. Wanneer de Whirlpool client actief is, zijn de UTXO's in het **postmix** account automatisch beschikbaar voor remixen en worden willekeurig gekozen om deel te nemen aan deze nieuwe cycli.


Ter herinnering, remixen zijn dan 100% gratis: er zijn geen extra servicekosten of Mining kosten nodig. Door de UTXO's in de **postmix** account te houden, blijft hun waarde intact en wordt tegelijkertijd hun anonset verbeterd. Daarom is het belangrijk om deze munten deel te laten nemen aan meerdere CoinJoin cycli. Het kost je strikt niets en het verhoogt hun anonimiteit.


Wanneer je besluit om gemengde UTXO's uit te geven, kun je dat rechtstreeks vanuit dit **postmix** account doen. Het is raadzaam om de gemengde UTXO's op dit account te houden om te kunnen profiteren van gratis remixen en om te voorkomen dat ze het Whirlpool circuit verlaten, wat hun privacy zou kunnen schaden.


Zoals we in de volgende tutorial zullen zien, is er ook de optie `mix to`, die de mogelijkheid biedt om je gemengde munten automatisch naar een andere Wallet te sturen, zoals een Cold Wallet, na een bepaald aantal coinjoins.


Na het bespreken van de theorie, duiken we in de praktijk met een tutorial over het gebruik van Whirlpool via de Sparrow wallet desktop software!


## Handleiding: CoinJoin Whirlpool op Sparrow wallet

Er zijn verschillende opties om Whirlpool te gebruiken. De eerste die ik je wil voorstellen is de Sparrow wallet optie, een open-source Bitcoin Wallet beheersoftware voor de PC.

Het gebruik van Sparrow heeft het voordeel dat het vrij eenvoudig is om mee te beginnen, snel is op te zetten en geen andere apparatuur vereist dan een computer en een internetverbinding. Er is echter een opvallend nadeel: coinjoins vinden alleen plaats wanneer Sparrow gestart en verbonden is. Dit betekent dat als je 24/7 je bitcoins wilt mixen en remixen, je je computer constant aan moet laten staan.


### Sparrow wallet installeren

Om te beginnen heb je natuurlijk de Sparrow wallet software nodig. Deze kun je direct downloaden van [de officiële website](https://sparrowwallet.com/download/) of op [hun GitHub](https://github.com/sparrowwallet/Sparrow/releases).


Voordat je de software installeert, is het belangrijk om de handtekening en integriteit van het zojuist gedownloade uitvoerbare bestand te verifiëren. Als je meer details wilt over het installatieproces en de verificatie van Sparrow software, raad ik je aan deze andere tutorial te lezen: *[The Sparrow wallet Guides](https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)*


### Een Software Wallet aanmaken

Na het installeren van de software, moet je een Bitcoin Wallet aanmaken. Het is belangrijk om te weten dat voor coinjoins het gebruik van een Software Wallet (ook wel een "Hot Wallet" genoemd) essentieel is. Daarom is het **niet mogelijk om coinjoins uit te voeren met een Wallet beveiligd door een Hardware Wallet**.


Hoewel het niet noodzakelijk is, is het in het geval dat je van plan bent om aanzienlijke hoeveelheden te mengen, sterk aan te raden om te kiezen voor het gebruik van een sterke BIP39 passphrase voor deze Wallet.


Om een nieuwe Wallet te maken, open Sparrow, klik dan op het tabblad `Bestand` en `Nieuwe Wallet`.


![sparrow](assets/notext/9.webp)


Kies een naam voor deze Wallet, bijvoorbeeld: "CoinJoin Wallet". Klik op de knop `Wallet aanmaken`.


![sparrow](assets/notext/10.webp)


Laat de standaardinstellingen staan en klik dan op de knop `Nieuw of Geïmporteerd Software Wallet`.


![sparrow](assets/notext/11.webp)


Wanneer je het Wallet creatie venster opent, raad ik je aan om een 12-woorden reeks te kiezen, aangezien dat ruim voldoende is. Selecteer `generate Nieuw` om generate een nieuwe herstelzin te maken en klik op `Gebruik passphrase` als je een passphrase van BIP39 wilt toevoegen. Het is belangrijk om een fysieke back-up te maken van je herstelinformatie, op papier of op een metalen drager, om de veiligheid van je bitcoins te garanderen.


![sparrow](assets/notext/12.webp)

Controleer de geldigheid van de back-up van uw herstelzin voordat u op `Back-up bevestigen...` klikt. Sparrow zal u dan vragen om uw zinsdeel opnieuw in te voeren om te verifiëren dat u het heeft genoteerd. Zodra deze stap is voltooid, gaat u verder door op `Create Keystore` te klikken.

![sparrow](assets/notext/13.webp)


Laat het voorgestelde afleidingspad als standaard staan en druk op `Import Keystore`. In mijn voorbeeld verschilt het afleidingspad enigszins, omdat ik de Testnet gebruik voor deze tutorial. Het afleidingspad dat voor jou zou moeten verschijnen is als volgt:

```plaintext
m/84'/0'/0'
```


![sparrow](assets/notext/14.webp)


Daarna toont Sparrow de afleidingsdetails van uw nieuwe Wallet. Als u een passphrase heeft ingesteld, is het sterk aanbevolen om uw `Master fingerprint` te noteren. Hoewel deze master key fingerprint geen gevoelige gegevens zijn, is het handig voor u om later te verifiëren dat u inderdaad toegang heeft tot de juiste Wallet en om te bevestigen dat er geen fouten zijn opgetreden bij het invoeren van uw passphrase.


Klik op de knop `Toepassen`.


![sparrow](assets/notext/15.webp)


Sparrow nodigt u uit om een wachtwoord voor uw Wallet aan te maken. Dit wachtwoord is nodig om toegang te krijgen via de Sparrow wallet software. Kies een sterk wachtwoord, maak er een back-up van en klik dan op `Set Password`.


![sparrow](assets/notext/16.webp)


### Bitcoins ontvangen

Na het aanmaken van je Wallet, heb je in eerste instantie één account, met de index `0'`. Dit is de **deposit** account waar we het in de vorige delen over hebben gehad. Dit is de rekening waarnaar je de bitcoins moet sturen om te mixen.


Selecteer hiervoor de tab `Ontvangen` aan de linkerkant van het venster. Sparrow zal automatisch generate een nieuwe lege Address aanmaken om bitcoins te ontvangen.


![sparrow](assets/notext/17.webp)


Je kunt een label invoeren voor deze Address, en dan de bitcoins ernaar toe sturen die gemixt moeten worden.


![sparrow](assets/notext/18.webp)


### De Tx0 maken

Zodra je transactie is bevestigd, kun je naar het tabblad `UTXO's` gaan.


![sparrow](assets/notext/19.webp)


Kies vervolgens de UTXO(s) die je aan de CoinJoin cycli wilt onderwerpen. Om meerdere UTXO's tegelijk te selecteren houd je de `Ctrl` toets ingedrukt terwijl je op de UTXO's van je keuze klikt.


![sparrow](assets/notext/20.webp)


Klik dan op de knop `Mix Selected` onderaan het venster. Als deze knop niet verschijnt op je Interface, komt dat omdat je op een Wallet zit die beveiligd is met een Hardware Wallet. Je moet een Software Wallet gebruiken om coinjoins uit te voeren met Sparrow.

![sparrow](assets/notext/21.webp)

Er wordt een venster geopend waarin wordt uitgelegd hoe Whirlpool werkt. Dit is een vereenvoudiging van wat ik in de vorige delen heb uitgelegd. Klik op `Volgende` om verder te gaan.


![sparrow](assets/notext/22.webp)


Op de volgende pagina kun je een "SCODE" invoeren als je die hebt. Een SCODE is een promotiecode die korting geeft op de servicekosten van het zwembad. Samourai Wallet geeft af en toe zulke codes aan haar gebruikers tijdens speciale evenementen. Ik raad je aan om Samourai Wallet](https://twitter.com/SamouraiWallet) te [volgen] op sociale media, zodat je toekomstige SCODE's niet mist.


Op dezelfde pagina moet je ook het tarief voor de `Tx0` en je initiële mix instellen. Deze keuze beïnvloedt de snelheid van bevestiging voor je voorbereidende transactie en je eerste CoinJoin. Vergeet niet dat je verantwoordelijk bent voor de Mining kosten voor de `Tx0` en de initiële mix, maar dat je geen Mining kosten verschuldigd bent voor latere remixen. Pas de `Premix Prioriteit` schuifknop aan volgens jouw voorkeuren en klik dan op `Volgende`.


![sparrow](assets/notext/23.webp)


In dit nieuwe venster heb je de mogelijkheid om de pool die je wilt invoeren te selecteren met behulp van de vervolgkeuzelijst. In mijn geval, nadat ik aanvankelijk een UTXO van `456 214 Sats` had geselecteerd, is mijn enige mogelijke keuze de pool van `100 000 Sats`. Deze Interface informeert je ook over de te betalen servicekosten en het aantal UTXO's dat in de pool wordt opgenomen. Als de voorwaarden je bevredigend lijken, ga dan verder door op `Preview Premix` te klikken.


![sparrow](assets/notext/24.webp)


Na deze stap vraagt Sparrow u om het wachtwoord voor uw Wallet in te voeren, het wachtwoord dat u hebt ingesteld bij het aanmaken in de software. Zodra het wachtwoord is ingevoerd, krijgt u toegang tot de preview van uw `Tx0`. Aan de linkerkant van het venster ziet u dat Sparrow de verschillende accounts heeft gegenereerd die nodig zijn voor het gebruik van Whirlpool (`Deposit`, `Premix`, `Postmix` en `Badbank`). U kunt ook de structuur van uw `Tx0` bekijken, met de verschillende uitgangen:


- De servicekosten;
- De geëgaliseerde UTXO's die bedoeld zijn om in de pool te komen;
- De giftige verandering (Doxxic Change).


![sparrow](assets/notext/25.webp)


Als de transactie naar wens is, klik je op `Transactie uitzenden` om je `Tx0` uit te zenden. Anders heb je de mogelijkheid om de parameters van deze `Tx0` aan te passen door `Clear` te selecteren om de ingevoerde gegevens te wissen en het creatieproces vanaf het begin te beginnen.


### Coinjoins uitvoeren

Zodra de Tx0 is uitgezonden, vind je je UTXO's klaar om gemengd te worden in het `Premix` account.

![sparrow](assets/notext/26.webp)


Zodra de `Tx0` is bevestigd, worden je UTXO's geregistreerd bij de coördinator en beginnen de eerste mixen automatisch na elkaar.


![sparrow](assets/notext/27.webp)


Als je de `Postmix`-account controleert, zie je de UTXO's die het resultaat zijn van de eerste mixen. Deze munten blijven klaar voor latere remixen, die geen extra kosten met zich meebrengen.


![sparrow](assets/notext/28.webp)


In de kolom `Mixes` kun je het aantal coinjoins zien dat door elk van je munten is uitgevoerd. Zoals we in de volgende secties zullen zien, is wat er echt toe doet niet zozeer het aantal remixen op zich, maar eerder de bijbehorende anonsets, hoewel deze twee indicatoren gedeeltelijk aan elkaar gerelateerd zijn.


![sparrow](assets/notext/29.webp)


Om de coinjoins tijdelijk te stoppen, klik je op `Stop Mixing`. Je hebt op elk moment de mogelijkheid om de bewerking te hervatten door `Start Mixing` te selecteren.


![sparrow](assets/notext/30.webp)


Om de continue beschikbaarheid van je UTXO's voor remixen te garanderen, is het noodzakelijk om de Sparrow software actief te houden. Als je de software afsluit of je computer uitschakelt, worden de coinjoins onderbroken. Een oplossing om dit probleem te omzeilen is om de slaapfuncties uit te schakelen via de instellingen van je besturingssysteem. Daarnaast biedt Sparrow een optie om te voorkomen dat uw computer automatisch in slaapstand gaat, die u kunt vinden onder het tabblad `Tools` met de titel `Prevent Computer Sleep`.


![sparrow](assets/notext/31.webp)


### De coinjoins voltooien

Om je gemengde bitcoins uit te geven, heb je verschillende opties. De meest directe methode is om naar de `Postmix` account te gaan en het tabblad `Versturen` te selecteren.


![sparrow](assets/notext/32.webp)


In dit gedeelte hebt u de mogelijkheid om de bestemming Address, het te verzenden bedrag en de transactiekosten in te voeren, op dezelfde manier als voor elke andere transactie die met Sparrow wallet wordt gemaakt. Als u wilt, kunt u ook gebruik maken van geavanceerde privacyfuncties, zoals Stonewall, door op de knop `Privacy` te klikken.


![sparrow](assets/notext/33.webp)


[-> Meer informatie over Stonewall-transacties](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


Als je een preciezere selectie wilt maken van de munten die je wilt uitgeven, ga dan naar het tabblad `UTXO's`. Selecteer de UTXO's die je specifiek wilt verbruiken en druk vervolgens op de knop `Verstuur Geselecteerd` om de transactie te starten.


![sparrow](assets/notext/34.webp)

Tot slot maakt de `Mix to...` optie beschikbaar op Sparrow het mogelijk om een geselecteerde UTXO automatisch te verwijderen uit CoinJoin cycli, zonder extra kosten. Deze functie maakt het mogelijk een aantal remixen te bepalen, waarna de UTXO niet opnieuw in je `Postmix` account wordt opgenomen, maar in plaats daarvan direct naar een andere Wallet wordt overgezet. Deze optie wordt vaak gebruikt om gemengde bitcoins automatisch naar een Cold Wallet te sturen.

Om deze optie te gebruiken, opent u eerst de ontvanger Wallet naast uw CoinJoin Wallet in de Sparrow-software.


![sparrow](assets/notext/35.webp)


Ga vervolgens naar het tabblad `UTXOs` en klik op de knop `Mix to...` onder in het venster.


![sparrow](assets/notext/36.webp)


Er wordt een venster geopend, begin met het selecteren van de bestemming Wallet uit de vervolgkeuzelijst.


![sparrow](assets/notext/37.webp)


Kies de CoinJoin drempel waarboven de opname automatisch zal plaatsvinden. Ik kan je geen exact aantal remixen geven om uit te voeren, omdat dit varieert afhankelijk van je persoonlijke situatie en je privacy doelen, maar vermijd het kiezen van een te lage drempel. Ik raad je aan dit andere artikel te raadplegen voor meer informatie over het remixproces: [REMIX - Whirlpool](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)


Je kunt de optie `Indexbereik` op de standaardwaarde `Volledig` laten staan. Deze functie maakt het mogelijk om gelijktijdig van verschillende clients te mixen, maar dat is niet wat we in deze tutorial willen doen. Om de `Mix to...` optie af te sluiten en te activeren, druk je op `Restart Whirlpool`.


![sparrow](assets/notext/38.webp)


Wees echter voorzichtig bij het gebruik van de optie `Mix to`, omdat het verwijderen van gemengde munten van uw `Postmix`-account het risico op het schenden van uw privacy aanzienlijk kan verhogen. De redenen voor dit risico worden in de volgende secties beschreven.


## Hoe weet je de kwaliteit van onze CoinJoin cycli?

Wil een CoinJoin echt effectief zijn, dan is het essentieel dat er een goede homogeniteit is tussen de hoeveelheden inputs en outputs. Deze homogeniteit vergroot het aantal mogelijke interpretaties in de ogen van een externe waarnemer, waardoor de onzekerheid rond de transactie toeneemt. Om deze onzekerheid van een CoinJoin te kwantificeren, kan men de entropie van de transactie berekenen. Voor een diepgaande verkenning van deze indicatoren verwijs ik je naar de tutorial: [BOLTZMANN CALCULATOR](https://planb.network/tutorials/privacy/analysis/boltzmann-entropy-738e45af-18a6-4ce6-af1a-1bf58e15f1fe). Het Whirlpool model wordt erkend als het model dat de meeste homogeniteit in coinjoins oplevert.

Vervolgens wordt de prestatie van verschillende CoinJoin cycli geëvalueerd op basis van de grootte van de groepen waarin een Coin verborgen zit. De grootte van deze groepen bepaalt wat de anonsets genoemd worden. Er zijn twee soorten anonsets: de eerste beoordeelt de privacywinst tegen retrospectieve analyse (van het heden naar het verleden) en de tweede tegen prospectieve analyse (van het verleden naar het heden). Voor een gedetailleerde uitleg van deze twee indicatoren nodig ik je uit om de tutorial te raadplegen: [Whirlpool STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


## Hoe postmix beheren?

Na het uitvoeren van CoinJoin cycli is de beste strategie om je UTXO's in de **postmix** account te bewaren, wachtend op toekomstig gebruik. Het is zelfs aan te raden om ze onbeperkt te laten remixen totdat je ze nodig hebt om uit te geven.


Sommige gebruikers zouden kunnen overwegen om hun gemengde bitcoins over te zetten naar een Wallet beveiligd door een Hardware Wallet. Dit is mogelijk, maar het is belangrijk om de aanbevelingen van Samourai Wallet nauwgezet op te volgen om de verworven privacy niet in gevaar te brengen.


Het samenvoegen van UTXO's is de meest gemaakte fout. Het is noodzakelijk om gemengde UTXO's niet te combineren met ongemengde UTXO's in dezelfde transactie, om de CIOH (*Common-Input-Ownership-Heuristic*) te vermijden. Dit vereist zorgvuldig beheer van je UTXO's binnen je Wallet, vooral wat betreft labeling. Buiten CoinJoin is het samenvoegen van UTXO's over het algemeen een slechte gewoonte die vaak leidt tot verlies van privacy als het niet goed beheerd wordt.


Het is ook belangrijk om voorzichtig te zijn met het consolideren van gemengde UTXO's met elkaar. Gematigde consolidaties zijn denkbaar als je gemengde UTXO's aanzienlijke anonsets hebben, maar dit zal onvermijdelijk de privacy van je munten verminderen. Zorg ervoor dat consolidaties niet te groot zijn of na een onvoldoende aantal remixen worden uitgevoerd, omdat dit het risico met zich meebrengt dat er afleidbare verbanden worden gelegd tussen je UTXO's voor en na de CoinJoin cycli. In geval van twijfel over deze manipulaties, is de beste praktijk om de postmix UTXO's niet te consolideren en ze één voor één over te brengen naar je Hardware Wallet, waarbij je telkens een nieuwe lege Address genereert. Nogmaals, vergeet niet om elke ontvangen UTXO goed te labelen.

Het wordt ook afgeraden om je postmix UTXO's over te zetten naar een Wallet met behulp van ongebruikelijke scripts. Als je bijvoorbeeld Whirlpool invoert vanuit een Multisig Wallet met behulp van `P2WSH` scripts, is de kans klein dat je gemengd wordt met andere gebruikers die oorspronkelijk hetzelfde type Wallet hebben. Als je je postmix terugtrekt naar diezelfde Multisig Wallet, zal het privacyniveau van je gemengde bitcoins sterk afnemen. Naast scripts zijn er nog veel meer Wallet fingerprints die je kunnen misleiden.

Zoals bij elke Bitcoin transactie, is het ook belangrijk om ontvangstadressen niet te hergebruiken. Elke nieuwe transactie moet worden ontvangen op een nieuwe, lege Address.


De eenvoudigste en veiligste oplossing is om je gemengde UTXO's te laten rusten in hun **postmix** account, ze te laten remixen en ze alleen aan te raken om uit te geven. Samourai en Sparrow wallets hebben extra bescherming tegen al deze ketenanalyse-gerelateerde risico's. Deze beschermingen helpen je fouten te voorkomen.


## Hoe ga je om met doxische verandering?

Vervolgens moet je voorzichtig zijn met het beheren van doxische verandering, de verandering die niet in de CoinJoin pool kon komen. Deze toxische UTXO's, die het gevolg zijn van het gebruik van Whirlpool, vormen een risico voor je privacy, omdat ze een verband leggen tussen jou en het gebruik van CoinJoin. Daarom is het noodzakelijk om er voorzichtig mee om te gaan en ze niet te combineren met andere UTXO's, vooral gemengde UTXO's. Hier zijn verschillende strategieën om ze te gebruiken:


- Mengen in kleinere zwembaden:** Als uw giftige UTXO groot genoeg is om alleen in een kleiner zwembad te komen, overweeg dan om het te mengen. Dit is vaak de beste optie. Het is echter cruciaal dat je niet meerdere giftige UTXO's samenvoegt om toegang te krijgen tot een pool, omdat dit je verschillende inzendingen met elkaar kan verbinden;
- Markeer ze als "onbesteedbaar":** Een andere aanpak is om ze niet langer te gebruiken, ze te markeren als "onbesteedbaar" in hun speciale account en gewoon HODL te gebruiken. Dit zorgt ervoor dat je ze niet per ongeluk uitgeeft. Als de waarde van Bitcoin stijgt, kunnen er nieuwe pools ontstaan die geschikter zijn voor jouw giftige UTXO's;
- Donaties doen:** Overweeg om donaties te doen, zelfs bescheiden, aan ontwikkelaars die werken aan Bitcoin en de bijbehorende software. Je kunt ook doneren aan organisaties die BTC accepteren. Als het beheren van je giftige UTXO's te ingewikkeld lijkt, kun je er gewoon vanaf komen door een donatie te doen;
- Cadeaubonnen kopen:** Platformen zoals [Bitrefill](https://www.bitrefill.com/) stellen je in staat om Exchange bitcoins om te wisselen voor cadeaubonnen die je kunt gebruiken bij verschillende winkels. Dit kan een manier zijn om van je giftige UTXO's af te komen zonder de bijbehorende waarde te verliezen.
- Consolideer ze op Monero:** Samourai Wallet biedt nu een atomic swap service tussen BTC en XMR. Dit is ideaal voor het beheren van giftige UTXO's door ze te consolideren op Monero, zonder je privacy in gevaar te brengen via de CIOH, voordat je ze terugstuurt naar Bitcoin. Deze optie kan echter duur zijn in termen van Mining vergoedingen en de premie als gevolg van liquiditeitsbeperkingen.
- Stuur ze naar de Lightning Network:** Deze UTXO's naar de Lightning Network sturen om te profiteren van lagere transactiekosten is een optie die interessant kan zijn. Deze methode kan echter bepaalde informatie onthullen, afhankelijk van je gebruik van Lightning, en moet daarom met voorzichtigheid worden toegepast.


Gedetailleerde tutorials over het implementeren van deze verschillende technieken worden binnenkort aangeboden op PlanB Network.


**Toegevoegde bronnen:**

[Sparrow wallet Video Tutorial](https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

[Samourai Wallet Video Tutorial](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)


- [Samourai Wallet Documentatie - Whirlpool](https://docs.samourai.io/Whirlpool/basic-concepts);
- [Twitter Thread over CoinJoins](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Blog Post op CoinJoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).