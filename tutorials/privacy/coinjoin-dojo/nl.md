---
name: CoinJoin - Dojo
description: Hoe voer je een CoinJoin uit met je eigen Dojo?
---
![cover](assets/cover.webp)


***WAARSCHUWING:** Na de arrestatie van de oprichters van Samourai Wallet en de inbeslagname van hun servers op 24 april, werkt de Whirlpool tool niet meer, zelfs niet voor individuen die hun eigen Dojo hebben of Sparrow wallet gebruiken. Het blijft echter mogelijk dat deze tool in de komende weken weer in gebruik wordt genomen of op een andere manier opnieuw wordt gelanceerd. Bovendien blijft het theoretische deel van dit artikel relevant voor het begrijpen van de principes en doelstellingen van coinjoins in het algemeen (niet alleen Whirlpool), en voor het begrijpen van de effectiviteit van het Whirlpool model.*


we volgen de ontwikkelingen van deze zaak en de ontwikkelingen met betrekking tot de bijbehorende tools op de voet. Wees gerust dat we deze handleiding zullen bijwerken zodra er nieuwe informatie beschikbaar is._


deze handleiding is alleen bedoeld voor educatieve en informatieve doeleinden. We keuren het gebruik van deze tools voor criminele doeleinden niet goed en moedigen dit ook niet aan. Het is de verantwoordelijkheid van elke gebruiker om te voldoen aan de wetten in hun rechtsgebied._


---

In deze tutorial leer je wat een CoinJoin is en hoe je er een uitvoert met behulp van de Samourai Wallet software en de Whirlpool implementatie, met behulp van je eigen Dojo. Naar mijn mening is dit momenteel de beste methode om je bitcoins te mixen.


## Wat is een CoinJoin op Bitcoin?

**Een CoinJoin is een techniek die de traceerbaarheid van bitcoins op de Blockchain verbreekt**. Het vertrouwt op een collaboratieve transactie met een specifieke structuur met dezelfde naam: de CoinJoin transactie.


Coinjoins verbeteren de privacy van Bitcoin gebruikers door ketenanalyse voor externe waarnemers te bemoeilijken. Hun structuur maakt het mogelijk om meerdere munten van verschillende gebruikers samen te voegen in één transactie, waardoor de sporen vervagen en het moeilijk wordt om de links tussen invoer- en uitvoeradressen te bepalen.


Het principe van de CoinJoin is gebaseerd op een collaboratieve aanpak: meerdere gebruikers die hun bitcoins willen mengen storten identieke bedragen als input van dezelfde transactie. Deze bedragen worden vervolgens herverdeeld als outputs van gelijke waarde voor elke gebruiker. Aan het einde van de transactie wordt het onmogelijk om een specifieke output te associëren met een bekende gebruiker bij de input. Er bestaat geen direct verband tussen de inputs en outputs, waardoor de associatie tussen de gebruikers en hun UTXO verbroken wordt, evenals de geschiedenis van elke Coin.

![coinjoin](assets/notext/1.webp)


Voorbeeld van een CoinJoin transactie (niet van mij): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


Om een CoinJoin uit te voeren en er tegelijkertijd voor te zorgen dat elke gebruiker te allen tijde de controle over zijn geld behoudt, begint het proces met het samenstellen van de transactie door een coördinator, die deze vervolgens doorstuurt naar de deelnemers. Elke gebruiker ondertekent vervolgens de transactie nadat is geverifieerd dat deze bij hem past. Alle verzamelde handtekeningen worden uiteindelijk geïntegreerd in de transactie. Als een gebruiker of de coördinator probeert geld om te leiden door de uitvoer van de CoinJoin transactie te wijzigen, zullen de handtekeningen ongeldig blijken, wat leidt tot de afwijzing van de transactie door de knooppunten.


Er zijn verschillende implementaties van CoinJoin, zoals Whirlpool, JoinMarket of Wabisabi, elk met als doel de coördinatie tussen deelnemers te beheren en de efficiëntie van CoinJoin transacties te verhogen.

In deze tutorial zullen we ons verdiepen in de implementatie van **Whirlpool**, die ik beschouw als de meest efficiënte oplossing voor het uitvoeren van coinjoins op Bitcoin. Hoewel het beschikbaar is op verschillende wallets, zullen we in deze tutorial uitsluitend het gebruik ervan onderzoeken met de Samourai Wallet mobiele applicatie, zonder Dojo.


## Waarom coinjoins uitvoeren op Bitcoin?

Een van de eerste problemen met elk peer-to-peer betalingssysteem is het dubbel uitgeven: hoe voorkom je dat kwaadwillenden dezelfde monetaire eenheden meerdere keren uitgeven zonder een beroep te doen op een centrale autoriteit om te arbitreren?


Satoshi Nakamoto bood een oplossing voor dit dilemma met het Bitcoin protocol, een peer-to-peer elektronisch betalingssysteem dat onafhankelijk van enige centrale autoriteit opereert. In zijn white paper benadrukt hij dat de enige manier om de afwezigheid van dubbele uitgaven te garanderen, is om de zichtbaarheid van alle transacties binnen het betalingssysteem te garanderen.


Om er zeker van te zijn dat elke deelnemer op de hoogte is van de transacties, moeten ze openbaar worden gemaakt. Daarom is de werking van Bitcoin gebaseerd op een transparante en gedistribueerde infrastructuur, waardoor elke knooppuntoperator de hele elektronische handtekeningketen en de geschiedenis van elke Coin kan verifiëren, vanaf het aanmaken ervan door een Miner.


Het transparante en gedistribueerde karakter van Bitcoin betekent dat elke gebruiker van het netwerk de transacties van alle andere deelnemers kan volgen en analyseren. Hierdoor is anonimiteit op transactieniveau onmogelijk. De anonimiteit blijft echter behouden op het niveau van individuele identificatie. In tegenstelling tot het traditionele banksysteem, waar elke rekening gekoppeld is aan een persoonlijke identiteit, worden op Bitcoin fondsen geassocieerd met paren cryptografische sleutels, waardoor gebruikers een vorm van pseudonimiteit krijgen achter cryptografische identifiers.


De privacy op Bitcoin komt dus in het gedrang wanneer externe waarnemers erin slagen om specifieke UTXO's te associëren met geïdentificeerde gebruikers. Zodra deze associatie is vastgesteld, wordt het mogelijk om hun transacties te traceren en de geschiedenis van hun bitcoins te analyseren. CoinJoin is juist een techniek die ontwikkeld is om de traceerbaarheid van UTXO's te doorbreken, waardoor Bitcoin gebruikers een zekere mate van privacy wordt geboden op transactieniveau.


## Hoe werkt Whirlpool?

Whirlpool onderscheidt zich van andere CoinJoin methoden door het gebruik van "_ZeroLink_" transacties, die ervoor zorgen dat er strikt geen technisch verband mogelijk is tussen alle inputs en alle outputs. Deze perfecte vermenging wordt bereikt door een structuur waarbij elke deelnemer een identieke hoeveelheid input bijdraagt (behalve de Mining vergoedingen), waardoor outputs van perfect gelijke hoeveelheden worden gegenereerd.

Deze restrictieve benadering van inputs geeft Whirlpool CoinJoin transacties een uniek kenmerk: de volledige afwezigheid van deterministische verbanden tussen de inputs en outputs. Met andere woorden, elke output heeft een gelijke waarschijnlijkheid om toegewezen te worden aan een deelnemer, vergeleken met alle andere outputs in de transactie.

Aanvankelijk was het aantal deelnemers in elke Whirlpool CoinJoin beperkt tot 5, met 2 nieuwkomers en 3 remixers (we zullen deze concepten verderop uitleggen). De stijging in On-Chain transactiekosten die in 2023 werd waargenomen, zette de Samourai-teams er echter toe aan hun model te heroverwegen om de privacy te verbeteren en tegelijkertijd de kosten te verlagen. Dus, rekening houdend met de marktsituatie van vergoedingen en het aantal deelnemers, kan de coördinator nu coinjoins organiseren met 6, 7 of 8 deelnemers. Deze verbeterde sessies worden "_Surge Cycles_" genoemd. Het is belangrijk op te merken dat, ongeacht de opzet, er altijd maar 2 nieuwe deelnemers zijn in de Whirlpool coinjoins.


Whirlpool transacties worden dus gekenmerkt door een identiek aantal in- en uitgangen, die kunnen zijn:


- 5 ingangen en 5 uitgangen;

![coinjoin](assets/notext/2.webp)


- 6 ingangen en 6 uitgangen;

![coinjoin](assets/notext/3.webp)


- 7 ingangen en 7 uitgangen;

![coinjoin](assets/notext/4.webp)


- 8 ingangen en 8 uitgangen.

![coinjoin](assets/notext/5.webp)

Het model dat Whirlpool voorstelt is dus gebaseerd op kleine CoinJoin transacties. In tegenstelling tot Wasabi en JoinMarket, waar de robuustheid van anonsets afhangt van het aantal deelnemers in een enkele cyclus, zet Whirlpool in op het aaneenschakelen van meerdere kleine cycli.


In dit model betaalt de gebruiker alleen vergoedingen bij zijn eerste toetreding tot een pool, waardoor hij kan deelnemen aan een groot aantal remixes zonder extra vergoedingen. Het zijn de nieuwkomers die de Mining vergoedingen voor de remixers betalen.


Met elke extra CoinJoin waaraan een Coin deelneemt, samen met zijn in het verleden gevonden soortgenoten, zullen de anonsets exponentieel groeien. Het doel is dus om te profiteren van deze gratis remixen, die met elk optreden bijdragen aan het vergroten van de dichtheid van de anonsets die geassocieerd zijn met elke gemengde Coin.


Bij het ontwerp van Whirlpool is rekening gehouden met twee belangrijke vereisten:


- De toegankelijkheid van de implementatie op mobiele apparaten, aangezien Samourai Wallet in de eerste plaats een smartphoneapplicatie is;
- De snelheid van remixing cycli om een aanzienlijke toename van anonsets te bevorderen.

Deze vereisten leidden de keuzes van de ontwikkelaars van Samourai Wallet in het ontwerp van Whirlpool, waardoor ze het aantal deelnemers per cyclus beperkten. Te weinig deelnemers zou de efficiëntie van CoinJoin in gevaar hebben gebracht, waardoor het aantal gegenereerde anonsets per cyclus drastisch zou zijn gedaald, terwijl te veel deelnemers problemen zouden hebben opgeleverd bij het beheer van mobiele toepassingen en de doorstroming van de cycli zouden hebben belemmerd.

**Het is uiteindelijk niet nodig om een hoog aantal deelnemers per CoinJoin op Whirlpool te hebben, aangezien de anonsets worden bereikt door de accumulatie van meerdere CoinJoin cycli.**


[-> Meer informatie over Whirlpool anonsets] (https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


### De zwembaden en CoinJoin vergoedingen

Willen deze meervoudige cycli de anonsets van de gemengde munten effectief verhogen, dan moet er een bepaald kader worden vastgesteld om de gebruikte hoeveelheden UTXO te beperken. Whirlpool definieert dus verschillende pools.


Een pool vertegenwoordigt een groep gebruikers die samen willen mengen, en die afspreken hoeveel UTXO ze willen gebruiken om het CoinJoin proces te optimaliseren. Elke pool specificeert een vaste hoeveelheid UTXO, waar de gebruiker zich aan moet houden om te kunnen deelnemen. Om coinjoins met Whirlpool uit te voeren, moet je dus een pool selecteren. Momenteel zijn de volgende pools beschikbaar:


- 0.5 bitcoins;
- 0.05 Bitcoin;
- 0.01 Bitcoin;
- 0.001 Bitcoin (= 100.000 Sats).


Als je je aansluit bij een pool met je bitcoins, worden deze verdeeld in generate UTXO's die perfect homogeen zijn met die van de andere deelnemers in de pool. Elke pool heeft een maximumlimiet; voor bedragen die deze limiet overschrijden, word je dus gedwongen om twee aparte inschrijvingen te doen binnen dezelfde pool of om over te stappen naar een andere pool met een hoger bedrag:


| Pool (bitcoin) | Maximum amount per entry (bitcoin) |
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

Zoals eerder vermeld, wordt een UTXO geacht tot een groep te behoren wanneer hij klaar is om in een CoinJoin geïntegreerd te worden. Dit betekent echter niet dat de gebruiker het bezit ervan verliest. **Door de verschillende mengcycli behoudt u de volledige controle over uw sleutels en dus ook over uw bitcoins.** Dit is wat de CoinJoin techniek onderscheidt van andere gecentraliseerde mengtechnieken.


Om mee te doen aan een CoinJoin pool, moeten servicekosten en Mining kosten betaald worden. De servicekosten zijn vastgesteld voor elke pool en zijn bedoeld om de teams te compenseren die verantwoordelijk zijn voor de ontwikkeling en het onderhoud van Whirlpool.

Servicekosten voor het gebruik van Whirlpool hoeven maar één keer betaald te worden bij het betreden van de pool. Na deze stap heb je de mogelijkheid om deel te nemen aan een onbeperkt aantal remixen zonder extra kosten. Hier zijn de huidige vaste kosten voor elke pool:


| Pool (bitcoin) | Entry Fee (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


Deze vergoedingen fungeren in wezen als een toegangsbewijs voor de gekozen pool, ongeacht het bedrag dat je in CoinJoin stopt. Dus, of je nu toetreedt tot de 0,01 pool met precies 0,01 BTC of toetreedt met 0,5 BTC, de vergoedingen blijven hetzelfde in absolute waarde.


Voordat er wordt overgegaan tot coinjoins, heeft de gebruiker dus de keuze tussen 2 strategieën:


- Kies voor een kleinere pool om de servicekosten te minimaliseren, wetende dat ze in ruil daarvoor verschillende kleine UTXO's zullen ontvangen;
- Of ze geven de voorkeur aan een grotere pool en gaan akkoord met het betalen van hogere vergoedingen om te eindigen met een kleiner aantal UTXO's met een grotere waarde.


Het wordt in het algemeen afgeraden om meerdere gemengde UTXO's samen te voegen na de CoinJoin cycli, omdat dit de verkregen privacy in gevaar kan brengen, vooral door de Common-Input-Ownership Heuristiek (CIOH). Daarom kan het verstandig zijn om een grotere pool te kiezen, zelfs als dat betekent dat er meer betaald moet worden, om te voorkomen dat er teveel UTXO's met een kleine waarde bij de uitvoer komen. De gebruiker moet deze afwegingen maken om de pool te kiezen waaraan hij de voorkeur geeft.


Naast de servicekosten moet ook rekening worden gehouden met de Mining kosten die inherent zijn aan elke Bitcoin transactie. Als gebruiker van Whirlpool, moet je de Mining kosten betalen voor de voorbereidingstransactie (`Tx0`), evenals die voor de eerste CoinJoin. Alle volgende remixen zullen gratis zijn, dankzij het model van Whirlpool, dat afhankelijk is van de betaling van nieuwe toetreders.


Inderdaad, in elke Whirlpool CoinJoin zijn twee gebruikers onder de input nieuwkomers. De andere input is afkomstig van remixers. Als gevolg daarvan worden de Mining vergoedingen voor alle deelnemers aan de transactie gedekt door deze twee nieuwe deelnemers, die dan ook profiteren van gratis remixen:

![coinjoin](assets/en/6.webp)

Dankzij dit vergoedingensysteem onderscheidt Whirlpool zich echt van andere CoinJoin diensten, omdat de anonimiteit van de UTXO's niet evenredig is met de prijs die de gebruiker betaalt. Het is dus mogelijk om een aanzienlijk hoog niveau van anonimiteit te bereiken door alleen de instapkosten van de pool te betalen en de Mining kosten voor twee transacties (de `Tx0` en de initiële mix).

Het is belangrijk op te merken dat de gebruiker ook de Mining kosten moet betalen om zijn UTXO's uit de pool te halen na het voltooien van zijn meervoudige coinjoins, tenzij hij de `mix to` optie heeft geselecteerd, die we in de tutorial hieronder zullen bespreken.


### De HD Wallet rekeningen gebruikt door Whirlpool

Om een CoinJoin uit te voeren via Whirlpool, moet de Wallet meerdere afzonderlijke generate accounts hebben. Een account, in de context van een HD (*hiërarchisch deterministisch*) Wallet, vormt een sectie die volledig geïsoleerd is van de anderen, deze scheiding vindt plaats op het derde diepteniveau van de Wallet hiërarchie, dat wil zeggen, op het niveau van de `xpub`.


Een HD Wallet kan theoretisch tot `2^(32/2)` verschillende accounts afleiden. Het initiële account, standaard gebruikt op alle Bitcoin wallets, komt overeen met de index `0'`.


Voor wallets die aangepast zijn aan Whirlpool, zoals Samourai of Sparrow, worden 4 accounts gebruikt om aan de behoeften van het CoinJoin proces te voldoen:


- De **deposito** rekening, geïdentificeerd door de index `0'`;
- De **slechte bank** (of doxxic change) rekening, geïdentificeerd door de index `2 147 483 644'`;
- De **premix** rekening, geïdentificeerd door de index `2 147 483 645'`;
- De **postmix** rekening, geïdentificeerd door de index `2 147 483 646'`.


Elk van deze accounts vervult een specifieke functie binnen de CoinJoin.


Al deze accounts zijn gekoppeld aan één seed, waarmee de gebruiker toegang kan krijgen tot al zijn bitcoins met behulp van zijn herstelzin en, indien nodig, zijn passphrase. Het is echter noodzakelijk om de software tijdens dit herstel de verschillende accountindexen te geven die werden gebruikt.


Laten we nu eens kijken naar de verschillende stadia van een Whirlpool CoinJoin binnen deze rekeningen.


### De verschillende stadia van samenvoegen op Whirlpool

**Fase 1: De Tx0**

Het startpunt van elke Whirlpool CoinJoin is de **deposit** account. Dit is het account dat je automatisch gebruikt als je een nieuwe Bitcoin Wallet aanmaakt. Deze rekening moet worden gecrediteerd met de bitcoins die men wil mengen.

De `Tx0` vertegenwoordigt de eerste stap in het Whirlpool mengproces. Het doel is om de UTXO voor te bereiden en te egaliseren voor de CoinJoin, door ze te verdelen in eenheden die overeenkomen met de hoeveelheid van de geselecteerde pool, om de homogeniteit van het mengen te garanderen. De geëgaliseerde UTXO worden dan naar de **premix** rekening gestuurd. Het verschil dat niet naar de pool kan, wordt gescheiden in een specifieke rekening: de **slechte bank** (of "doxxic change").

Deze initiële transactie `Tx0` dient ook om de servicekosten te vereffenen die verschuldigd zijn aan de mengcoördinator. In tegenstelling tot de volgende stappen werkt deze transactie niet samen; de gebruiker moet daarom alle Mining vergoedingen betalen:

![coinjoin](assets/en/7.webp)


In dit voorbeeld van een `Tx0` transactie, wordt een input van `372.000 Sats` van onze **deposito** rekening verdeeld in verschillende output UTXO, die als volgt worden verdeeld:


- Een bedrag van `5.000 Sats` bestemd voor de coördinator servicekosten, overeenkomend met de opname in de pool van `100.000 Sats`;
- Drie UTXO klaargemaakt om te mengen, doorgestuurd naar onze **premix** rekening en geregistreerd bij de coördinator. Deze UTXO zijn geëgaliseerd op `108.000 Sats` per stuk, om de Mining vergoedingen voor hun toekomstige eerste mix te dekken;
- Het overschot dat niet in de pool kan, omdat het te klein is, wordt beschouwd als giftig wisselgeld. Het wordt naar een specifieke rekening gestuurd. Hier bedraagt deze verandering `40.000 Sats`;
- Tenslotte zijn er `3.000 Sats` die geen uitvoer vormen, maar de Mining vergoedingen zijn die nodig zijn om de `Tx0` te bevestigen.


Hier is bijvoorbeeld een echte Whirlpool Tx0 (niet van mij): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**Stap 2: De doxxische verandering**

Het overschot dat niet geïntegreerd kon worden in de pool, hier gelijk aan `40.000 Sats`, wordt omgeleid naar de **slechte bank** rekening, ook wel "doxxic change" genoemd, om een strikte scheiding te garanderen met de andere UTXO in de Wallet.


Deze UTXO is gevaarlijk voor de privacy van de gebruiker, omdat het niet alleen nog steeds verbonden is met het verleden, en dus mogelijk met de identiteit van de eigenaar, maar bovendien staat genoteerd dat het toebehoort aan een gebruiker die een CoinJoin heeft uitgevoerd.

Als deze UTXO samengevoegd wordt met gemengde uitgangen, zullen ze alle privacy verliezen die ze opgedaan hebben tijdens de CoinJoin cycli, met name vanwege de Common-Input-Ownership-Heuristic (CIOH). Als het samengevoegd wordt met andere doxische veranderingen, loopt de gebruiker het risico privacy te verliezen, omdat dit de verschillende inputs van de CoinJoin cycli met elkaar verbindt. Daarom moet er voorzichtig mee worden omgegaan. De manier om met deze giftige UTXO om te gaan wordt in het laatste deel van dit artikel beschreven, en toekomstige tutorials zullen deze methodes uitgebreider behandelen op PlanB Network.


**Stap 3: De eerste mix**

Nadat de `Tx0` is voltooid, worden de geëgaliseerde UTXO's naar de **premix** rekening van onze Wallet gestuurd, klaar om te worden ingevoerd in hun eerste CoinJoin cyclus, ook wel de "initiële mix" genoemd. Als, zoals in ons voorbeeld, de `Tx0` meerdere UTXO's genereert die bedoeld zijn om te mengen, wordt elk van hen geïntegreerd in een aparte initiële CoinJoin.


Aan het einde van deze eerste mixen zal de **premix** rekening leeg zijn, terwijl onze munten, die de Mining vergoedingen voor deze eerste CoinJoin hebben betaald, precies zullen worden aangepast aan het bedrag dat is gedefinieerd door de gekozen pool. In ons voorbeeld zijn onze initiële UTXO's van `108 000 Sats` teruggebracht tot precies `100 000 Sats`.

![coinjoin](assets/en/8.webp)

**Stap 4: De remixen**

Na de eerste mix worden de UTXO's overgebracht naar het **postmix** account. Dit account verzamelt de UTXO's die al gemengd zijn en de UTXO's die wachten op remixen. Wanneer de Whirlpool client actief is, zijn de UTXO's in het **postmix** account automatisch beschikbaar voor remixen en worden willekeurig gekozen om deel te nemen aan deze nieuwe cycli.


Ter herinnering, de remixen zijn dan 100% gratis: er zijn geen extra servicekosten of Mining kosten nodig. Door de UTXO's in de **postmix** account te houden, blijft hun waarde intact en wordt tegelijkertijd hun anonset verbeterd. Daarom is het belangrijk om deze munten deel te laten nemen aan meerdere CoinJoin cycli. Het kost je strikt niets en het verhoogt hun anonimiteit.


Als je besluit om gemengde UTXO's uit te geven, kun je dat direct doen vanuit dit **postmix** account. Het is raadzaam om de gemengde UTXO's op dit account te houden om te kunnen profiteren van gratis remixen en om te voorkomen dat ze het Whirlpool circuit verlaten, wat hun privacy zou kunnen schaden.


Zoals we in de volgende tutorial zullen zien, is er ook de optie `mix to`, die de mogelijkheid biedt om je gemengde munten automatisch naar een andere Wallet te sturen, zoals een Cold Wallet, na een bepaald aantal coinjoins.

Na het behandelen van de theorie, duiken we in de praktijk met een tutorial over het gebruik van Whirlpool via de Samourai Wallet Android applicatie, gesynchroniseerd met Whirlpool CLI en GUI op je eigen Dojo!

## Tutorial: CoinJoin Whirlpool met je eigen Dojo

Er zijn veel opties om Whirlpool te gebruiken. Degene die ik hier wil introduceren is de Samourai Wallet optie, een open-source Bitcoin Wallet beheerapplicatie op Android, maar deze keer **met je eigen Dojo**.


Het uitvoeren van coinjoins via Samourai Wallet met behulp van je eigen Dojo is naar mijn mening de meest effectieve strategie voor het uitvoeren van coinjoins op Bitcoin tot nu toe. Deze aanpak vergt enige initiële investering in termen van setup, maar eenmaal geïnstalleerd, biedt het de mogelijkheid om je bitcoins continu te mixen en remixen, 24 uur per dag, 7 dagen per week, zonder de noodzaak om je Samourai-toepassing altijd actief te houden. Sterker nog, dankzij Whirlpool CLI die op een Bitcoin node werkt, ben je altijd klaar om deel te nemen aan coinjoins. De Samourai-applicatie geeft je dan de mogelijkheid om je gemengde fondsen op elk moment uit te geven, waar je ook bent, rechtstreeks vanaf je smartphone. Bovendien heeft deze methode het voordeel dat je nooit verbonden bent met servers die beheerd worden door de Samourai-teams, waardoor je `xpub` gevrijwaard blijft van enige externe blootstelling.


Deze techniek is daarom ideaal voor wie op zoek is naar maximale privacy en de hoogste kwaliteit CoinJoin cycli. Het vereist echter wel dat je een Bitcoin knooppunt tot je beschikking hebt en, zoals we later zullen zien, vereist het enige configuratie. Het is dus meer geschikt voor gemiddelde tot gevorderde gebruikers. Voor beginners raad ik aan om kennis te maken met CoinJoin via deze twee andere tutorials, die laten zien hoe je het doet vanuit Sparrow wallet of Samourai Wallet (zonder Dojo):


- [Sparrow wallet CoinJoin tutorial](https://planb.network/tutorials/privacy/on-chain/coinjoin-sparrow-wallet-84def86d-faf5-4589-807a-83be60720c8b)**;
- [Samourai Wallet CoinJoin tutorial (without Dojo)](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)**.


### De installatie begrijpen

Om te beginnen heb je een Dojo nodig! Dojo is een Bitcoin node implementatie gebaseerd op Bitcoin core, ontwikkeld door de Samourai teams.


Om je eigen Dojo te draaien, heb je de optie om zelfstandig een Dojo node te installeren, of om gebruik te maken van Dojo bovenop een andere "node-in-box" Bitcoin node oplossing. Momenteel zijn de beschikbare opties:


- [RoninDojo](https://ronindojo.io/), wat een Dojo is met extra tools, waaronder een installatie assistent en een administratie assistent. Ik beschrijf de procedure voor het instellen en gebruiken van RoninDojo in deze andere tutorial: [RONINDOJO V2](https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8);
- [Umbrel](https://umbrel.com/) met de toepassing "Samourai Server";
- [MyNode](https://mynodebtc.com/) met de "Dojo"-toepassing;
- [Nodl](https://www.nodl.eu/) met de "Dojo"-toepassing;
- [Citadel](https://runcitadel.space/) met de "Samourai" toepassing.

![coinjoin](assets/notext/9.webp)

In onze opstelling zullen we drie verschillende interfaces gebruiken:


- Samourai Wallet**, die onze Bitcoin Wallet voor coinjoins zal hosten. Deze FOSS-applicatie is gratis beschikbaar op Android en stelt je in staat om je Wallet mixen te bedienen, speciaal voor het uitgeven van je postmix vanaf je smartphone;
- Whirlpool CLI** (_Command Line Interface_), die werkt op het knooppunt waar de Dojo staat. Deze software heeft toegang tot de sleutels van je Samourai Wallet. Het is verantwoordelijk voor de communicatie met de coördinator en het continue beheer van de coinjoins. Het fungeert als een kopie van jouw Samourai Wallet op jouw node, klaar om op elk moment deel te nemen aan coinjoins;
- Whirlpool GUI** (_Graphical User Interface_), de grafische gebruiker Interface die we zullen gebruiken om de activiteit van Whirlpool CLI te monitoren en op afstand te mengen. Whirlpool GUI geeft een visuele voorstelling van de activiteiten van Whirlpool CLI. Deze software moet geïnstalleerd worden op een computer die los staat van de Dojo. Voor gebruikers van Umbrel, MyNode, Nodl en Citadel is Whirlpool GUI verplicht. Echter, met RoninDojo is de Whirlpool GUI Interface al geïntegreerd in het Interface web van je node via de `Whirlpool` applicatie. Daarom hoef je het niet op een aparte PC te installeren.


Naar mijn mening is RoninDojo de beste oplossing om coinjoins uit te voeren met een Dojo. Omdat deze node-in-box software rechtstreeks samenwerkt met de Samourai-teams, is RoninDojo hiervoor veel beter geoptimaliseerd. Bovendien vereenvoudigt de integratie van de Whirlpool GUI in de web Interface het installatieproces aanzienlijk. In deze tutorial zal ik nog uitleggen hoe het moet met de andere oplossingen die Dojo integreren (Umbrel, Nodl, MyNode en Citadel).


### Je dojo voorbereiden

Om te beginnen moet je Dojo installeren en de QR-code of de link verkrijgen waarmee je op afstand verbinding kunt maken. Deze link is een Tor Address eindigend op `.onion`. Als je RoninDojo gebruikt, navigeer dan naar het `Pairing` menu om bij deze informatie te komen.

![coinjoin](assets/notext/10.webp)


Klik onder `Samourai Dojo` op de knop `Pair now`.


![coinjoin](assets/notext/11.webp)


De QR-code van je verbinding en de bijbehorende link worden weergegeven.


![coinjoin](assets/notext/12.webp)


Als je Umbrel gebruikt, ga dan naar de App Store en zoek naar de applicatie `Samourai Server`. Deze bevindt zich in het tabblad `Bitcoin`.


![coinjoin](assets/notext/13.webp)


Installeer de toepassing.


![coinjoin](assets/notext/14.webp)


Na het openen van de applicatie heb je toegang tot de QR-code waarmee je verbinding kunt maken met je Dojo.


![coinjoin](assets/notext/15.webp)


Als je een andere node-in-box software zoals MyNode, Citadel of Nodl gebruikt, is het proces vergelijkbaar met dat van Umbrel. Je moet de Samourai of Dojo applicatie installeren om de benodigde informatie te verkrijgen om verbinding te maken met je Dojo.


![coinjoin](assets/notext/16.webp)


### Uw Samourai Wallet voorbereiden

Na het ophalen van de verbindingsinformatie met je Dojo, is het nu tijd om je Wallet in te stellen voor coinjoins. Er zijn twee scenario's: als je nog geen Samourai Wallet op je smartphone hebt, is het proces eenvoudig: maak gewoon een nieuwe aan.


Als je echter al een Samourai Wallet hebt, moet je de applicatie opnieuw installeren om deze te koppelen aan een nieuwe Dojo. Deze stap is nodig omdat de verbinding met een Dojo alleen tot stand kan worden gebracht bij de eerste keer opstarten van de applicatie. Maar dankzij het automatisch gegenereerde versleutelde back-upbestand van Samourai op je telefoon is deze procedure eenvoudig en snel.


*Als je Samourai nog nooit hebt gebruikt, kun je deze voorbereidende stappen overslaan en direct doorgaan met de installatie van de applicatie.*


Zorg er eerst en vooral voor dat je Samourai Wallet applicatie up-to-date is. Controleer hiervoor de Google Play Store of vergelijk de versie van uw applicatie in `Instellingen > Overige` met de versie die beschikbaar is op de Samourai website.


![coinjoin](assets/notext/17.webp)


Zorg ervoor dat u uw Samourai Wallet herstelzin hebt en dat deze leesbaar is. Voer vervolgens een test uit van uw BIP39 passphrase door te navigeren naar `Instellingen > Problemen oplossen > passphrase/Backup test` om de nauwkeurigheid te bevestigen.


![coinjoin](assets/notext/18.webp)

Voer je passphrase in en controleer dan of Samourai de geldigheid bevestigt.

![coinjoin](assets/notext/19.webp)


Als je passphrase ongeldig is, of als je je herstelzin niet hebt, is het noodzakelijk om de procedure onmiddellijk te stoppen! **U riskeert uw bitcoins te verliezen tijdens deze operatie.** In dit geval is het aangeraden om uw fondsen over te schrijven naar een andere Wallet en te beginnen met een nieuwe lege Samourai Wallet. De volgende stappen moeten alleen worden gevolgd als je zeker weet dat je alle benodigde back-up informatie hebt en dat je passphrase geldig is.


Maak dan een versleutelde back-up van uw Wallet en kopieer deze naar uw klembord. Klik hiervoor op de drie kleine puntjes rechtsboven in het scherm en selecteer vervolgens `Export Wallet backup`.


![coinjoin](assets/notext/20.webp)


**Kopieer vanaf deze stap niets meer naar je klembord!** Het is absoluut essentieel dat je je gekopieerde back-up bewaart.


Als je de vorige stappen correct hebt uitgevoerd, ben je nu in staat om je Samourai Wallet veilig te verwijderen. Ga hiervoor naar: `Instellingen > Wallet > Wallet veilig wissen`.


![coinjoin](assets/notext/21.webp)


![coinjoin](assets/notext/22.webp)


*Als je Samourai nog nooit hebt gebruikt en de applicatie vanaf nul installeert, kun je de tutorial bij deze stap hervatten.*


Uw Samourai-toepassing is nu gereset. Open de applicatie en ga verder met de installatiestappen alsof je deze voor de eerste keer gebruikt.


![coinjoin](assets/notext/23.webp)


In de volgende stap ga je naar de pagina voor het configureren van je Dojo. Selecteer de optie `Dojo` en voer de inloggegevens van je Dojo in. Hiervoor heb je de optie om de informatie te scannen door op `Scan QR` te drukken.


![coinjoin](assets/notext/24.webp)


*Voor nieuwe gebruikers van Samourai, zal het dan nodig zijn om een Wallet vanaf nul aan te maken. Als je hulp nodig hebt, kun je de instructies voor het opzetten van een nieuwe Samourai Wallet [in deze tutorial, specifiek in het hoofdstuk "Een Software Wallet aanmaken"](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)* raadplegen


Als u een reeds bestaande Samourai Wallet wilt herstellen, kies dan `Restore existing Wallet` en vervolgens `I have a Samourai backup file`.


![coinjoin](assets/notext/25.webp)

Normaal gesproken moet je altijd je herstelbestand in je klembord hebben. Klik dan op `PASTE` om uw bestand op de aangegeven plaats in te voegen. Om het te ontsleutelen, moet je ook de BIP39 passphrase van je Wallet invoeren in het veld eronder. Klik op `FINISH` om af te sluiten.

![coinjoin](assets/notext/26.webp)


Je wordt dan doorgestuurd naar je Samourai Wallet, die deze keer verbonden is met je eigen Dojo.


![coinjoin](assets/notext/27.webp)


### Whirlpool GUI installeren

Het is nu tijd om Whirlpool GUI te installeren, de grafische gebruiker Interface waarmee je je CoinJoin cycli vanaf je gewone PC kunt beheren. Voor RoninDojo gebruikers is deze stap niet nodig, omdat het beheer van coinjoins direct via het web Interface in `Apps > Whirlpool` kan worden gedaan. Als je echter een andere Bitcoin "node-in-box" oplossing gebruikt, is het noodzakelijk om door te gaan met deze installatie.

![coinjoin](assets/notext/28.webp)

Ga naar je pc en download de Whirlpool software van de officiële Samourai Wallet website, selecteer de versie die overeenkomt met jouw besturingssysteem.


![coinjoin](assets/notext/29.webp)


Voor je Whirlpool GUI start, is het noodzakelijk om JAVA 8 of een hogere versie op je machine te installeren. Hiervoor [kunt u OpenJDK installeren] (https://adoptium.net/).

![coinjoin](assets/notext/30.webp)

Het is ook noodzakelijk om Tor daemon of Tor Browser op de achtergrond operationeel te hebben op je computer. Zorg ervoor dat je Tor start voor elke Whirlpool GUI gebruikssessie. Als Tor nog niet geïnstalleerd is op je machine, [je kunt het downloaden en installeren van de officiële project website](https://www.torproject.org/download/), zorg er dan voor dat je het op de achtergrond start.


![coinjoin](assets/notext/31.webp)


Zodra JDK op je systeem geïnstalleerd is en Tor op de achtergrond gestart is, kun je Whirlpool GUI starten.


![coinjoin](assets/notext/32.webp)


Klik in de Whirlpool GUI op `Geavanceerd: Remote CLI` om verbinding te maken met je Whirlpool CLI die op je Dojo staat. Je hebt de Tor Address van je Whirlpool CLI nodig.


![coinjoin](assets/notext/33.webp)


Om je Tor Address te lokaliseren op Umbrel en andere "node-in-box" oplossingen, start gewoon de Samourai Server of Dojo applicatie (de naam kan variëren afhankelijk van de gebruikte software). De Tor Address zal direct zichtbaar zijn op de pagina van de applicatie.

![coinjoin](assets/notext/34.webp)

In Whirlpool GUI, voer de Tor Address in die je eerder verkregen hebt in het `CLI Address` veld. Behoud de `http://` prefix, maar voeg de `:8899` poort niet toe aan het einde. Plak alleen de Address zoals je die hebt gekregen.

![coinjoin](assets/notext/35.webp)


Voer in het Tor Proxy veld `socks5://127.0.0.1:9050` in als je Tor daemon gebruikt, of `socks5://127.0.0.1:9150` als het Tor Browser is. Wanneer je voor het eerst verbinding maakt met Whirlpool CLI via Whirlpool GUI, is het mogelijk om het API sleutel veld leeg te laten. Als dit niet uw eerste verbinding is, voer dan uw API-sleutel in de daarvoor bestemde ruimte in. Deze sleutel kan gevonden worden op dezelfde pagina als je Tor Address.


![coinjoin](assets/notext/36.webp)


Als je alles hebt ingevuld, klik je op de knop `Connect`. Wacht even, de verbinding kan enkele minuten duren.


![coinjoin](assets/notext/37.webp)


### Uw Samourai Wallet koppelen met Whirlpool GUI

*Gebruikers van RoninDojo kunnen de tutorial hier hervatten.*


We gaan nu de Samourai Wallet die we eerder geconfigureerd hebben koppelen met de Whirlpool GUI software, of rechtstreeks met RoninDojo voor degenen die deze software gebruiken. Of je nu Whirlpool GUI of RoninDojo gebruikt, je wordt gevraagd om de koppelingsinformatie van je Samourai Wallet te plakken of te scannen.


![coinjoin](assets/notext/38.webp)


Om deze informatie te vinden, ga je naar de instellingen van je Wallet.


![coinjoin](assets/notext/39.webp)


Klik op `Transacties`, dan op `Pair to Whirlpool GUI`.


![coinjoin](assets/notext/40.webp)


Samourai geeft je dan de nodige informatie om de verbinding tot stand te brengen. Wees voorzichtig, deze gegevens zijn gevoelig! Je kunt ze overbrengen naar je pc door ze rechtstreeks te kopiëren of door de weergegeven QR-code te scannen met de webcam van je computer nadat je op het QR-codesymbool hebt geklikt.


![coinjoin](assets/notext/41.webp)


Na het uitvoeren van deze handeling, selecteer `Initialiseer GUI` in Whirlpool GUI. Wacht even, want deze stap kan even duren.


![coinjoin](assets/notext/42.webp)


Of je nu Whirlpool GUI of RoninDojo gebruikt, je wordt gevraagd om de passphrase van je Samourai Wallet in te voeren. Voer het in het daarvoor bestemde veld in en druk dan op de `Login` knop om verder te gaan.


![coinjoin](assets/notext/43.webp)


Je komt dan op de homepage van Whirlpool CLI


![coinjoin](assets/notext/44.webp)


### Co-joins initiëren vanuit Whirlpool GUI

*Voor RoninDojo gebruikers is het te volgen proces identiek. De Whirlpool app Interface geïntegreerd in RoninDojo biedt dezelfde opties en functionaliteiten als de Whirlpool GUI software op de desktop. Daarom kunt u deze instructies op dezelfde manier volgen.*

Nu alles is ingesteld, ben je klaar om je bitcoins te mengen. Om dit te doen, maak je de bitcoins die je wilt mengen over naar de **Deposit** account van je Samourai Wallet. Deze handeling kan direct worden uitgevoerd via de Samourai Wallet app of op de Whirlpool GUI. Klik op de hoofdpagina op de `+ Deposit` knop linksboven.


![coinjoin](assets/notext/45.webp)


Whirlpool GUI zal generate een ontvangende Address. Het toont ook het minimumbedrag dat nodig is om deel te nemen aan elke CoinJoin-pool. Dit bedrag varieert afhankelijk van de vergoedingsmarkt. Het is raadzaam een bedrag te storten dat iets hoger is dan het vereiste minimum, want als de Mining vergoedingen niet dalen, wordt jouw UTXO misschien niet geaccepteerd in de gewenste pool. Stuur daarom je bitcoins naar de opgegeven Address. Om een nieuwe Address te krijgen, klik je gewoon op de `Vernieuw Address` knop.


![coinjoin](assets/notext/46.webp)


Zodra de storting is bevestigd, kun je deze zien verschijnen in de **Deposit** account op Whirlpool GUI.


![coinjoin](assets/notext/47.webp)


Om de CoinJoin cycli te starten, selecteert u de UTXO's die u wilt mengen en drukt u op de `Premix` knop. Wees voorzichtig: als je verschillende UTXO's tegelijk selecteert, worden ze samengevoegd tijdens de `TX0` voorbereidingstransactie. Dit samenvoegen kan leiden tot minder privacy, vooral als de UTXO's van verschillende bronnen komen, vanwege de Common Input Ownership Heuristic (CIOH).


![coinjoin](assets/notext/48.webp)


De Whirlpool configuratiepagina wordt geopend. Je kunt kiezen in welke pool je wilt instappen. Selecteer ook de Mining vergoedingen voor de `TX0` en de eerste coinjoins. Onderaan deze pagina zie je een samenvatting met de hoeveelheid doxxic wisselgeld en de hoeveelheid en het aantal UTXO's die worden geëgaliseerd en opgenomen in de CoinJoin cycli. Als je tevreden bent met deze configuratie, druk dan op de `Premix` knop om de CoinJoin cycli te starten.

![coinjoin](assets/notext/49.webp)


Zodra de `TX0` is aangemaakt, kun je je geëgaliseerde UTXO's zien in de **Premix** account, wachtend op bevestiging. Om je munten 24 uur per dag, 7 dagen per week automatisch te laten remixen, raad ik je aan de optie `Automatisch premix & postmix mixen` te activeren. Je vindt deze functie in de `Configuratie` tab, links van je Whirlpool GUI venster.

![coinjoin](assets/notext/50.webp)

Na het starten van de coinjoins, kun je zowel Whirlpool GUI als Samourai Wallet verlaten. Alleen jouw node hoeft verbonden te blijven om te kunnen deelnemen aan continue coinjoins. Het is echter raadzaam om regelmatig de voortgang van je CoinJoin cycli te controleren. Als je merkt dat je UTXO's gedurende enige tijd niet meer geselecteerd worden voor een CoinJoin, kan dit duiden op een bug. Ga in dat geval naar Whirlpool CLI en selecteer `Start` om je beschikbaarheid voor coinjoins opnieuw te starten.


![coinjoin](assets/notext/51.webp)


Je gemengde UTXO's zijn zichtbaar via het **Postmix** account op de Whirlpool GUI. Daarnaast heb je de optie om ze direct te bekijken en uit te geven via de Whirlpool Interface op je Samourai Wallet. Om dit menu te openen, klik je op de blauwe `+` onderaan je scherm en kies je vervolgens `Whirlpool`.


![coinjoin](assets/notext/52.webp)


Whirlpool accounts zijn gemakkelijk te herkennen op Samourai Wallet door hun blauwe kleur. Hierdoor kun je je gemengde UTXO's overal en altijd uitgeven, direct vanaf je smartphone.


![coinjoin](assets/notext/53.webp)


Om je automatische coinjoins bij te houden, raad ik ook aan om een Watch-only wallet in te stellen via de Sentinel app. Voeg de ZPUB van je **Postmix** account toe en monitor de voortgang van je CoinJoin cycli in real-time. Als je wilt begrijpen hoe je Sentinel moet gebruiken, raad ik je aan deze andere tutorial op PlanB Network te raadplegen: [**SENTINEL WATCH-ONLY**](https://planb.network/tutorials/wallet/mobile/sentinel-9876f960-e964-4d20-8a6e-36231de1f4d9)