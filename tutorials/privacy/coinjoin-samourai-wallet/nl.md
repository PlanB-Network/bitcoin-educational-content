---
name: CoinJoin - Samourai Wallet
description: Hoe voer je een CoinJoin uit op een Samourai Wallet?
---
![cover](assets/cover.webp)


***WAARSCHUWING:** Na de arrestatie van de oprichters van Samourai Wallet en de inbeslagname van hun servers op 24 april, werkt de Whirlpool tool niet meer, zelfs niet voor individuen die hun eigen Dojo hebben of Sparrow wallet gebruiken. Het blijft echter mogelijk dat deze tool in de komende weken weer in gebruik wordt genomen of op een andere manier opnieuw wordt gelanceerd. Bovendien blijft het theoretische deel van dit artikel relevant voor het begrijpen van de principes en doelstellingen van coinjoins in het algemeen (niet alleen Whirlpool), en voor het begrijpen van de effectiviteit van het Whirlpool model.*


we volgen de ontwikkelingen van deze zaak en de ontwikkelingen met betrekking tot de bijbehorende tools op de voet. Wees gerust dat we deze handleiding zullen bijwerken zodra er nieuwe informatie beschikbaar is._


deze handleiding is alleen bedoeld voor educatieve en informatieve doeleinden. We keuren het gebruik van deze tools voor criminele doeleinden niet goed en moedigen dit ook niet aan. Het is de verantwoordelijkheid van elke gebruiker om te voldoen aan de wetten in hun rechtsgebied._


---

> *een Bitcoin Wallet voor de straten*

In deze tutorial leer je wat een CoinJoin is en hoe je er een uitvoert met behulp van de Samourai Wallet software en de Whirlpool implementatie.


## Wat is een CoinJoin op Bitcoin?

**CoinJoin is een techniek die de traceerbaarheid van bitcoins op de Blockchain** doorbreekt. Het vertrouwt op een collaboratieve transactie met een specifieke structuur met dezelfde naam: de CoinJoin transactie.


Coinjoins verbeteren de privacy van Bitcoin gebruikers door ketenanalyse voor externe waarnemers te bemoeilijken. Hun structuur maakt het mogelijk om meerdere munten van verschillende gebruikers samen te voegen in een enkele transactie, waardoor de sporen onleesbaar worden en het moeilijk wordt om de links tussen invoer- en uitvoeradressen te bepalen.


Het principe van CoinJoin is gebaseerd op een collaboratieve aanpak: verschillende gebruikers die hun bitcoins willen mengen, storten identieke bedragen als input van dezelfde transactie. Deze bedragen worden vervolgens herverdeeld als outputs van gelijke waarde voor elke gebruiker. Aan het einde van de transactie wordt het onmogelijk om een specifieke output te associëren met een bekende gebruiker als input. Er bestaat geen directe link tussen de inputs en outputs, waardoor de associatie tussen gebruikers en hun UTXO verbroken wordt, evenals de geschiedenis van elke Coin.

![coinjoin](assets/notext/1.webp)


Voorbeeld van een CoinJoin transactie (niet van mij): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


Om een CoinJoin uit te voeren en er tegelijkertijd voor te zorgen dat elke gebruiker te allen tijde de controle over zijn geld behoudt, begint het proces met het samenstellen van de transactie door een coördinator, die deze vervolgens doorstuurt naar de deelnemers. Elke gebruiker ondertekent vervolgens de transactie nadat is geverifieerd dat deze bij hem past. Alle verzamelde handtekeningen worden uiteindelijk geïntegreerd in de transactie. Als een gebruiker of de coördinator probeert geld af te leiden door de uitvoer van de CoinJoin transactie te wijzigen, zullen de handtekeningen ongeldig blijken, wat leidt tot afwijzing van de transactie door de knooppunten.


Er zijn verschillende implementaties van CoinJoin, zoals Whirlpool, JoinMarket of Wabisabi, die elk de coördinatie tussen deelnemers willen beheren en de efficiëntie van CoinJoin transacties willen verhogen.

In deze tutorial zullen we ons verdiepen in de implementatie van **Whirlpool**, die ik beschouw als de meest efficiënte oplossing voor het uitvoeren van coinjoins op Bitcoin. Hoewel het beschikbaar is op verschillende wallets, zullen we in deze tutorial uitsluitend het gebruik ervan onderzoeken met de Samourai Wallet mobiele applicatie, zonder Dojo.


## Waarom coinjoins uitvoeren op Bitcoin?

Een van de eerste problemen met elk peer-to-peer betalingssysteem is het dubbel uitgeven: hoe voorkom je dat kwaadwillenden dezelfde monetaire eenheden meerdere keren uitgeven zonder een beroep te doen op een centrale autoriteit om te arbitreren?


Satoshi Nakamoto bood een oplossing voor dit dilemma met het Bitcoin protocol, een peer-to-peer elektronisch betalingssysteem dat onafhankelijk van enige centrale autoriteit opereert. In zijn white paper benadrukt hij dat de enige manier om de afwezigheid van dubbele uitgaven te certificeren is door de zichtbaarheid van alle transacties binnen het betalingssysteem te garanderen.


Om te garanderen dat elke deelnemer op de hoogte is van de transacties, moeten ze openbaar worden gemaakt. Daarom is de werking van Bitcoin gebaseerd op een transparante en gedistribueerde infrastructuur, waardoor elke knooppuntoperator de volledige elektronische handtekeningketen en de geschiedenis van elke Coin kan verifiëren, vanaf het aanmaken ervan door een Miner.


Het transparante en gedistribueerde karakter van Blockchain betekent dat elke netwerkgebruiker de transacties van alle andere deelnemers kan volgen en analyseren. Hierdoor is anonimiteit op transactieniveau onmogelijk. De anonimiteit blijft echter behouden op het niveau van individuele identificatie. In tegenstelling tot het traditionele banksysteem, waar elke rekening gekoppeld is aan een persoonlijke identiteit, worden op Bitcoin fondsen geassocieerd met paren cryptografische sleutels, waardoor gebruikers een vorm van pseudonimiteit krijgen achter cryptografische identifiers.


De privacy op Bitcoin komt dus in het gedrang wanneer externe waarnemers erin slagen om specifieke UTXO's te associëren met geïdentificeerde gebruikers. Zodra deze associatie is vastgesteld, wordt het mogelijk om hun transacties te traceren en de geschiedenis van hun bitcoins te analyseren. CoinJoin is juist een techniek die ontwikkeld is om de traceerbaarheid van UTXO's te doorbreken, waardoor Bitcoin gebruikers op transactieniveau een zekere Layer privacy wordt geboden.


## Hoe werkt Whirlpool?

Whirlpool onderscheidt zich van andere CoinJoin methoden door het gebruik van "_ZeroLink_" transacties, die ervoor zorgen dat er strikt geen technisch verband mogelijk is tussen alle inputs en alle outputs. Deze perfecte vermenging wordt bereikt door een structuur waarbij elke deelnemer een identieke hoeveelheid input bijdraagt (behalve de Mining vergoedingen), waardoor outputs van perfect gelijke hoeveelheden worden gegenereerd.

Deze restrictieve benadering van inputs geeft Whirlpool CoinJoin transacties een uniek kenmerk: de totale afwezigheid van deterministische verbanden tussen inputs en outputs. Met andere woorden, elke output heeft een gelijke waarschijnlijkheid om te worden toegewezen aan een deelnemer, vergeleken met alle andere outputs in de transactie.

Aanvankelijk was het aantal deelnemers in elke Whirlpool CoinJoin beperkt tot 5, met 2 nieuwkomers en 3 remixers (we zullen deze concepten verderop uitleggen). De stijging van de transactiekosten voor On-Chain die in 2023 werd waargenomen, zette de Samourai-teams er echter toe aan hun model te heroverwegen om de privacy te verbeteren en tegelijkertijd de kosten te verlagen. Dus, rekening houdend met de marktsituatie van vergoedingen en het aantal deelnemers, kan de coördinator nu coinjoins organiseren met 6, 7 of 8 deelnemers. Deze verbeterde sessies worden "_Surge Cycles_" genoemd. Het is belangrijk op te merken dat, ongeacht de configuratie, er altijd slechts 2 nieuwe deelnemers zijn in Whirlpool coinjoins.


Whirlpool transacties worden dus gekenmerkt door een identiek aantal in- en uitgangen, die kunnen zijn:


- 5 ingangen en 5 uitgangen;

![coinjoin](assets/notext/2.webp)


- 6 ingangen en 6 uitgangen;

![coinjoin](assets/notext/3.webp)


- 7 ingangen en 7 uitgangen;

![coinjoin](assets/notext/4.webp)


- 8 ingangen en 8 uitgangen.

![coinjoin](assets/notext/5.webp)

Het model dat Whirlpool voorstelt is dus gebaseerd op kleine CoinJoin transacties. In tegenstelling tot Wasabi en JoinMarket, waar de robuustheid van de anonsets afhangt van het aantal deelnemers in een enkele cyclus, zet Whirlpool in op het aaneenschakelen van meerdere kleine cycli.


In dit model betaalt de gebruiker de vergoedingen alleen bij zijn eerste deelname aan een pool, waardoor hij kan deelnemen aan een groot aantal remixes zonder extra kosten. Het zijn de nieuwkomers die de Mining vergoedingen voor de remixers betalen.


Met elke extra CoinJoin waaraan een Coin deelneemt, samen met zijn soortgenoten uit het verleden, zullen de anonsets exponentieel groeien. Het doel is daarom om te profiteren van deze gratis remixen, die met elk optreden bijdragen aan het versterken van de dichtheid van de anonsets die geassocieerd zijn met elke gemengde Coin.


Bij het ontwerp van Whirlpool is rekening gehouden met twee belangrijke vereisten:


- De toegankelijkheid van de implementatie op mobiele apparaten, aangezien Samourai Wallet voornamelijk een smartphone-applicatie is;
- De snelheid van de remixing cycli om een significante toename in anonsets te bevorderen.

Deze vereisten leidden de ontwikkelaars van Samourai Wallet in het ontwerp van Whirlpool, waardoor ze het aantal deelnemers per cyclus beperkten. Te weinig deelnemers zou de efficiëntie van CoinJoin in gevaar hebben gebracht en het aantal anonsets dat per cyclus werd gegenereerd drastisch hebben verminderd, terwijl te veel deelnemers problemen zouden hebben opgeleverd bij het beheer van mobiele toepassingen en de doorstroming van de cycli zouden hebben belemmerd.

**Uiteindelijk is het niet nodig om een hoog aantal deelnemers per CoinJoin op Whirlpool te hebben, aangezien de anonsets worden bereikt door de accumulatie van meerdere CoinJoin cycli.**


[-> Meer informatie over Whirlpool anonsets] (https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


### De zwembaden en CoinJoin vergoedingen

Willen deze meervoudige cycli de anonsets van de gemengde munten effectief verhogen, dan moet er een bepaald kader worden vastgesteld om de gebruikte hoeveelheden UTXO te beperken. Whirlpool definieert dus verschillende pools.


Een pool vertegenwoordigt een groep gebruikers die samen willen mengen, en die afspreken hoeveel UTXO ze willen gebruiken om het CoinJoin proces te optimaliseren. Elke pool specificeert een vaste hoeveelheid UTXO, waar de gebruiker zich aan moet houden om te kunnen deelnemen. Om coinjoins met Whirlpool uit te voeren, moet je dus een pool selecteren. Momenteel zijn de volgende pools beschikbaar:


- 0.5 bitcoins;
- 0.05 Bitcoin;
- 0.01 Bitcoin;
- 0.001 Bitcoin (= 100.000 Sats).


Als je je aansluit bij een pool met je bitcoins, worden deze verdeeld in generate UTXO's die perfect homogeen zijn met die van de andere deelnemers in de pool. Elke pool heeft een maximumlimiet; voor bedragen die deze limiet overschrijden, word je dus gedwongen om twee aparte inschrijvingen te doen binnen dezelfde pool of om je te oriënteren op een andere pool met een hoger bedrag:


| Pool (bitcoin) | Maximum amount per entry (bitcoin) |
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

Zoals eerder vermeld, wordt een UTXO geacht deel uit te maken van een groep wanneer hij klaar is om in een CoinJoin geïntegreerd te worden. Dit betekent echter niet dat de gebruiker het bezit ervan verliest. **Door de verschillende mengcycli behoudt u de volledige controle over uw sleutels en dus ook over uw bitcoins.** Dit is wat de CoinJoin techniek onderscheidt van andere gecentraliseerde mengtechnieken.


Om deel te nemen aan een CoinJoin pool, moeten servicekosten en Mining kosten betaald worden. De servicekosten zijn vastgesteld voor elke pool en zijn bedoeld om de teams die verantwoordelijk zijn voor de ontwikkeling en het onderhoud van Whirlpool te compenseren.

Servicekosten voor het gebruik van Whirlpool hoeven maar één keer betaald te worden bij het betreden van de pool. Na deze stap heb je de mogelijkheid om deel te nemen aan een onbeperkt aantal remixen zonder extra kosten. Hier zijn de huidige vaste kosten voor elke pool:


| Pool (bitcoin) | Entry Fee (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


Deze vergoedingen fungeren in wezen als een toegangsbewijs voor de gekozen pool, ongeacht het bedrag dat je in CoinJoin stopt. Dus, of je nu toetreedt tot de 0.01 pool met precies 0.01 BTC of toetreedt met 0.5 BTC, de vergoedingen blijven in absolute waarde gelijk.


Alvorens over te gaan tot coinjoins, heeft de gebruiker dus de keuze tussen 2 strategieën:


- Kies voor een kleinere pool om de servicekosten te minimaliseren, wetende dat ze in ruil daarvoor verschillende kleine UTXO's zullen ontvangen;
- Of ze geven de voorkeur aan een grotere pool en gaan akkoord met hogere vergoedingen om uiteindelijk een kleiner aantal UTXO's van grotere waarde te krijgen.


Het wordt over het algemeen afgeraden om meerdere gemengde UTXO's samen te voegen na de CoinJoin cycli, omdat dit de verkregen privacy in gevaar kan brengen, vooral door de Common-Input-Ownership Heuristic (CIOH). Daarom kan het verstandig zijn om een grotere pool te kiezen, zelfs als dat betekent dat er meer betaald moet worden, om te voorkomen dat er te veel UTXO's met een kleine waarde als uitvoer komen. De gebruiker moet deze compromissen afwegen om de pool te kiezen waaraan hij de voorkeur geeft.


Naast de servicekosten moet ook rekening worden gehouden met de Mining kosten die inherent zijn aan elke Bitcoin transactie. Als Whirlpool gebruiker moet je de Mining kosten betalen voor de voorbereidingstransactie (`Tx0`) en die voor de eerste CoinJoin. Alle volgende remixen zijn gratis, dankzij het model van Whirlpool dat gebaseerd is op betaling van nieuwe toetreders. Alle volgende remixen zullen gratis zijn, dankzij het model van Whirlpool dat afhankelijk is van de betaling van nieuwe toetreders.


Inderdaad, in elke Whirlpool CoinJoin zijn twee gebruikers onder de input nieuwkomers. De andere input is afkomstig van remixers. Als gevolg daarvan worden de Mining vergoedingen voor alle deelnemers aan de transactie gedekt door deze twee nieuwe deelnemers, die dan ook profiteren van gratis remixen:

![coinjoin](assets/en/6.webp)

Dankzij dit vergoedingensysteem onderscheidt Whirlpool zich echt van andere CoinJoin diensten, omdat de anonimiteit van de UTXO's niet evenredig is met de prijs die de gebruiker betaalt. Het is dus mogelijk om een aanzienlijk hoog niveau van anonimiteit te bereiken door alleen de instapkosten van de pool te betalen en de Mining kosten voor twee transacties (de `Tx0` en de initiële mix).

Het is belangrijk op te merken dat de gebruiker ook de Mining kosten moet betalen om zijn UTXO's uit de pool te halen na het voltooien van zijn meervoudige coinjoins, tenzij hij de `mix to` optie heeft geselecteerd, die we in de tutorial hieronder zullen bespreken.


### De HD Wallet rekeningen gebruikt door Whirlpool

Om een CoinJoin uit te voeren via Whirlpool, moet de Wallet meerdere afzonderlijke generate accounts hebben. Een account, in de context van een HD (*Hierarchical Deterministic*) Wallet, vormt een sectie die volledig geïsoleerd is van de anderen, deze scheiding vindt plaats op het derde diepteniveau van de hiërarchie van de Wallet, dat wil zeggen, op het niveau van de `xpub`.


Een HD Wallet kan theoretisch tot `2^(32/2)` verschillende accounts afleiden. Het initiële account, standaard gebruikt op alle Bitcoin wallets, komt overeen met de index `0'`.


Voor portemonnees die aangepast zijn aan Whirlpool, zoals Samourai of Sparrow, worden 4 accounts gebruikt om aan de behoeften van het CoinJoin proces te voldoen:


- De **deposito** rekening, geïdentificeerd door de index `0'`;
- De **slechte bank** (of doxxic change) rekening, geïdentificeerd door de index `2 147 483 644'`;
- De **premix** rekening, geïdentificeerd door de index `2 147 483 645'`;
- De **postmix** rekening, geïdentificeerd door de index `2 147 483 646'`.


Elk van deze accounts vervult een specifieke functie binnen het CoinJoin proces.


Al deze accounts zijn gekoppeld aan één seed, waarmee de gebruiker toegang kan krijgen tot al zijn bitcoins met behulp van zijn herstelzin en, indien van toepassing, zijn passphrase. Het is echter noodzakelijk om tijdens dit herstel aan de software aan te geven welke verschillende accountindexen werden gebruikt. Het is echter noodzakelijk om tijdens dit herstel aan de software aan te geven welke verschillende accountindexen werden gebruikt.


Laten we nu eens kijken naar de verschillende stadia van een Whirlpool CoinJoin binnen deze rekeningen.


### De verschillende stadia van samenvoegingen op Whirlpool

**Fase 1: De Tx0**

Het startpunt van elke Whirlpool CoinJoin is de **deposit** account. Dit is het account dat je automatisch gebruikt als je een nieuw Bitcoin Wallet aanmaakt. Deze rekening moet worden gecrediteerd met de bitcoins die men wil mengen.

De `Tx0` vertegenwoordigt de eerste stap in het Whirlpool mengproces. Het doel is om de UTXO voor te bereiden en te egaliseren voor de CoinJoin, door ze te verdelen in eenheden die overeenkomen met de hoeveelheid van de geselecteerde pool, om de homogeniteit van de mix te garanderen. De geëgaliseerde UTXO worden dan naar de **premix** rekening gestuurd. Het verschil dat niet in de pool kan, wordt gescheiden in een specifieke rekening: de **slechte bank** (of "doxxic change").

Deze initiële transactie `Tx0` dient ook om de servicekosten te vereffenen die verschuldigd zijn aan de mengcoördinator. In tegenstelling tot de volgende stappen werkt deze transactie niet samen; de gebruiker moet daarom alle Mining kosten op zich nemen:

![coinjoin](assets/en/7.webp)


In dit voorbeeld van een `Tx0` transactie, wordt een input van `372.000 Sats` van onze **deposito** rekening verdeeld in verschillende output UTXO, die als volgt worden verdeeld:


- Een bedrag van `5.000 Sats` bestemd voor de coördinator servicekosten, overeenkomend met de opname in de pool van `100.000 Sats`;
- Drie UTXO klaargemaakt om te mengen, doorgestuurd naar onze **premix** rekening en geregistreerd bij de coördinator. Deze UTXO zijn geëgaliseerd op `108.000 Sats` per stuk, om de Mining vergoedingen voor hun toekomstige eerste mix te dekken;
- Het overschot dat niet in de pool kan, omdat het te klein is, wordt beschouwd als giftig wisselgeld. Het wordt naar een specifieke rekening gestuurd. Hier bedraagt deze verandering `40.000 Sats`;
- Tenslotte zijn er `3.000 Sats` die geen uitvoer vormen, maar de Mining vergoedingen zijn die nodig zijn om de `Tx0` te bevestigen.


Hier is bijvoorbeeld een echte Whirlpool Tx0 (niet van mij): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**Stap 2: De doxxische verandering**

Het overschot dat niet geïntegreerd kon worden in de pool, hier gelijk aan `40.000 Sats`, wordt omgeleid naar de **slechte bank** rekening, ook wel "doxxic change" genoemd, om een strikte scheiding met de andere UTXO in de Wallet te garanderen.


Deze UTXO is gevaarlijk voor de privacy van de gebruiker, omdat het niet alleen nog steeds verbonden is met het verleden, en dus mogelijk met de identiteit van de eigenaar, maar bovendien staat genoteerd dat het toebehoort aan een gebruiker die een CoinJoin heeft uitgevoerd.

Als deze UTXO samengevoegd wordt met gemengde uitgangen, zullen ze alle privacy verliezen die ze opgedaan hebben tijdens de CoinJoin cycli, met name vanwege de Common-Input-Ownership-Heuristic (CIOH). Als het samengevoegd wordt met andere doxische veranderingen, loopt de gebruiker het risico privacy te verliezen, omdat dit de verschillende inputs van de CoinJoin cycli met elkaar verbindt. Daarom moet er voorzichtig mee worden omgegaan. De manier om met deze giftige UTXO om te gaan wordt in het laatste deel van dit artikel beschreven, en toekomstige tutorials zullen dieper ingaan op deze methodes op PlanB Network.


**Stap 3: De eerste mix**

Nadat de `Tx0` is voltooid, worden de geëgaliseerde UTXO's naar de **premix** rekening van onze Wallet gestuurd, klaar om te worden ingevoerd in hun eerste CoinJoin cyclus, ook wel "initiële mix" genoemd. Als, zoals in ons voorbeeld, de `Tx0` meerdere UTXO's genereert om te mengen, zal elk van hen worden geïntegreerd in een aparte initiële CoinJoin.


Aan het einde van deze eerste mixen zal de **premix** rekening leeg zijn, terwijl onze munten, die de Mining vergoedingen voor deze eerste CoinJoin hebben betaald, precies zullen worden aangepast aan het bedrag dat is gedefinieerd door de gekozen pool. In ons voorbeeld zijn onze initiële UTXO's van `108 000 Sats` teruggebracht tot precies `100 000 Sats`.

![coinjoin](assets/en/8.webp)

**Stap 4: De remixen**

Na de eerste mix worden de UTXO's overgebracht naar het **postmix** account. Dit account verzamelt de UTXO's die al gemengd zijn en de UTXO's die wachten om opnieuw gemengd te worden. Wanneer de Whirlpool client actief is, zijn de UTXO's in het **postmix** account automatisch beschikbaar voor remixen en worden willekeurig gekozen om deel te nemen aan deze nieuwe cycli.


Ter herinnering, de remixen zijn dan 100% gratis: er zijn geen extra servicekosten of Mining kosten nodig. Door de UTXO's in de **postmix** account te houden, blijft hun waarde intact en wordt tegelijkertijd hun anonset verbeterd. Daarom is het belangrijk om deze munten deel te laten nemen aan meerdere CoinJoin cycli. Het kost je strikt niets en het verhoogt hun anonimiteit.


Wanneer je besluit om gemengde UTXO's uit te geven, kun je dat rechtstreeks vanuit dit **postmix** account doen. Het is raadzaam om de gemengde UTXO's in dit account te houden om te kunnen profiteren van gratis remixen en om te voorkomen dat ze het Whirlpool circuit verlaten, wat hun privacy zou kunnen schaden.


Zoals we in de volgende tutorial zullen zien, is er ook de optie `mix to`, die de mogelijkheid biedt om je gemengde munten automatisch naar een andere Wallet te sturen, zoals een Cold Wallet, na een bepaald aantal coinjoins.

Na de theorie duiken we de praktijk in met een tutorial over het gebruik van Whirlpool via de Samourai Wallet Android app!


## Handleiding: CoinJoin Whirlpool op Samourai Wallet

Er zijn talloze opties om Whirlpool te gebruiken. Degene die ik hier wil introduceren is de Samourai Wallet optie (zonder Dojo), een open-source Bitcoin Wallet beheerapplicatie op Android.


Mixen op Samourai zonder Dojo heeft het voordeel dat het heel eenvoudig is, snel in te stellen en er is geen ander apparaat voor nodig dan een Android-telefoon en een internetverbinding.


Deze methode heeft echter twee opmerkelijke nadelen:


- Coinjoins vinden alleen plaats als Samourai op de achtergrond draait en verbonden is. Dit betekent dat als je 24/7 je bitcoins wilt mixen en remixen, je Samourai constant aan moet laten staan;
- Als je Whirlpool gebruikt met Samourai Wallet zonder je eigen Dojo aan te sluiten, dan zal je applicatie verbinding moeten maken met de server die onderhouden wordt door de Samourai teams, en geef je de `xpub` van je Wallet aan hen door. Deze anonieme stukjes informatie zijn nodig voor je applicatie om je transacties te vinden.


De ideale oplossing om deze beperkingen te omzeilen is om je eigen Dojo te gebruiken, geassocieerd met een Whirlpool CLI instantie op je persoonlijke Bitcoin knooppunt. Op deze manier vermijd je het lekken van informatie en bereik je volledige onafhankelijkheid. Hoewel de hieronder gepresenteerde tutorial nuttig is voor bepaalde doelen of voor beginners, is het gebruik van je eigen Dojo aanbevolen om je CoinJoin sessie echt te optimaliseren. Een gedetailleerde handleiding voor het opzetten van deze configuratie is binnenkort beschikbaar op PlanB Network.


### Installatie van Samourai Wallet

Om te beginnen heb je natuurlijk de Samourai Wallet app nodig. Je kunt hem rechtstreeks downloaden van de officiële website met de APK, van hun GitLab of van de Google Play Store.


### Een Software Wallet maken

Na het installeren van de software, moet je een Bitcoin Wallet aanmaken op Samourai. Als je er al een hebt, kun je direct naar de volgende stap gaan.


Druk bij het openen van de applicatie op de blauwe `Start` knop. Je wordt dan gevraagd om een locatie in de bestanden van je telefoon te selecteren waar de versleutelde back-up van je nieuwe Wallet wordt opgeslagen.


![samourai](assets/notext/9.webp)

Activeer Tor door op de bijbehorende inkeping te klikken. In dit stadium heb je ook de optie om een specifieke Dojo te selecteren. In deze tutorial gaan we echter verder met de standaard Dojo; je kunt de optie dus uitgeschakeld laten. Wanneer Tor verbonden is, druk je op de `Create a new Wallet` knop.

![samourai](assets/notext/10.webp)


Samourai Wallet vraagt je dan om een BIP39 passphrase in te stellen. Dit extra wachtwoord is erg belangrijk omdat het direct betrokken is bij de afleiding van je privésleutels. Een mogelijk verlies van deze passphrase zou resulteren in de onmogelijkheid om toegang te krijgen tot je bitcoins, waardoor ze onherroepelijk verloren gaan. Om je Samourai Wallet te herstellen, is het noodzakelijk om zowel je 12-woord herstelzin als de passphrase te hebben.


Het is daarom essentieel om een robuuste passphrase te kiezen en een of meer fysieke kopieën te maken, op papier of op een metalen drager, om de veiligheid van uw bitcoins te garanderen. Vink na het voltooien van deze taken het vakje `Ik ben me ervan bewust dat in geval van verlies...` aan en druk vervolgens op de knop `NEXT`.


![samourai](assets/notext/11.webp)


Vervolgens moet u een PIN-code van 5 tot 8 cijfers instellen. Deze code beveiligt de toegang tot uw Wallet op uw telefoon. Hij wordt elke keer gevraagd als u de Samourai-toepassing wilt openen. Kies voor een robuuste pincode en bewaar een reservekopie. Daarna kun je op de `NEXT` knop drukken.


![samourai](assets/notext/12.webp)


Samourai vraagt u nogmaals uw pincode in te voeren ter bevestiging. Voer deze in en druk vervolgens op `FINALIZE`.


![samourai](assets/notext/13.webp)


Je krijgt dan toegang tot je herstelzin die uit 12 woorden bestaat. Met deze zin kunt u uw Wallet herstellen met de eerder ingevoerde passphrase. Het wordt sterk aangeraden om een of meer kopieën van deze zin te maken op fysieke media, zoals papier of metaal, om de veiligheid van je bitcoins te garanderen in geval van een probleem.


Nadat je deze back-ups hebt gemaakt, word je doorgestuurd naar de Interface van je nieuwe Samourai Wallet.


![samourai](assets/notext/14.webp)


U krijgt een PayNym Bot aangeboden. Je kunt dit aanvragen als je wilt, maar het is niet essentieel voor onze tutorial.


![samourai](assets/notext/15.webp)

Voordat u bitcoins gaat ontvangen op deze nieuwe Wallet, wordt het sterk aangeraden om de geldigheid van uw Wallet back-ups opnieuw te controleren (de passphrase en de herstelzin). Om de passphrase te verifiëren, kunt u het icoon van uw PayNym Bot linksboven in het scherm selecteren en vervolgens het pad volgen:

```plaintext
Settings > Troubleshooting > Passphrase/backup test
```


Voer uw passphrase in om de verificatie uit te voeren.


![samourai](assets/notext/16.webp)


Samourai zal bevestigen of het geldig is.


![samourai](assets/notext/17.webp)


Om uw back-up van de herstelzin te verifiëren, gaat u naar het pictogram van uw PayNym Bot, linksboven in het scherm, en volgt u dit pad:

```plaintext
Settings > Wallet > Show 12-word recovery phrase
```


Samourai toont een venster met je herstelzin. Zorg ervoor dat deze exact overeenkomt met je fysieke back-up.


Om verder te gaan en een volledige hersteltest uit te voeren, noteert u een getuige-element van uw Wallet, zoals een van de `xpubs`, en verwijdert u vervolgens uw Wallet (op voorwaarde dat hij nog leeg is). Het doel is om te proberen deze lege Wallet te herstellen met alleen uw fysieke back-ups. Als het herstel succesvol is, geeft dit aan dat uw back-ups geldig en betrouwbaar zijn.


### Bitcoins ontvangen

Na het aanmaken van je Wallet, begin je met één account, geïdentificeerd met de index `0'`. Dit is de **deposit** account waar we het in de vorige delen over hebben gehad. Naar deze rekening moet je de bitcoins overmaken die bedoeld zijn voor coinjoins.


Klik hiervoor op het blauwe `+` symbool rechtsonder in het scherm.


![samourai](assets/notext/18.webp)


Klik dan op de Green `Ontvangen` knop.


![samourai](assets/notext/19.webp)


Samourai zal automatisch generate een nieuwe lege Address aanmaken om bitcoins te ontvangen.


![samourai](assets/notext/20.webp)


Je kunt de bitcoins daarheen sturen om ze te laten mengen.


![samourai](assets/notext/21.webp)


### De Tx0 maken

Wanneer de transactie is bevestigd, kunnen we het coinjoins-proces starten. Klik hiervoor op de blauwe `+` knop rechtsonder in het scherm.


![samourai](assets/notext/22.webp)


Klik vervolgens op `Whirlpool` in het blauw.


![samourai](assets/notext/23.webp)


Wacht terwijl Whirlpool initialiseert en Samourai de benodigde accounts aanmaakt.


![samourai](assets/notext/24.webp)


Je komt dan op de Whirlpool homepage. Klik op `Start`.

![samourai](assets/notext/25.webp)

Selecteer de UTXO van de **depositorekening** die u in CoinJoin cycli wilt verzenden en klik dan op `Volgende`.


![samourai](assets/notext/26.webp)


In de volgende stap moet je het vergoedingsniveau kiezen om toe te wijzen aan de `Tx0` en aan je eerste mix. Deze instelling bepaalt de snelheid waarmee je `Tx0` en je eerste CoinJoin (of eerste coinjoins) worden bevestigd. Houd in gedachten dat de Mining kosten voor de `Tx0` en de eerste mix jouw verantwoordelijkheid zijn, maar dat je geen Mining kosten hoeft te betalen voor de daaropvolgende remixen. Je hebt de keuze tussen `Low`, `Normal`, of `High` opties.


![samourai](assets/notext/27.webp)


In hetzelfde venster heb je de mogelijkheid om de pool te kiezen die je wilt invoeren. Aangezien ik in eerste instantie een UTXO van `454.258 Sats` heb gekozen, is mijn enige mogelijke keuze de `100.000 Sats` pool. Deze pagina laat je ook de servicekosten van de pool zien, naast de Mining kosten, zodat je de totale kosten voor deze CoinJoin cyclus weet. Als alles je bevalt, selecteer dan de juiste pool en ga verder door op de blauwe `VERIFY CYCLE DETAILS` knop te klikken.


![samourai](assets/notext/28.webp)


Je kunt dan alle details van je CoinJoin cyclus zien:


- het aantal UTXO's dat naar de pool gaat;
- de verschillende gemaakte kosten;
- de hoeveelheid doxische verandering...


Controleer de informatie en klik vervolgens op de Green `START CYCLE` knop.


![samourai](assets/notext/29.webp)


Er verschijnt een venster waarin je de giftige verandering die voortvloeit uit je invoer in de CoinJoin-cyclus kunt markeren als "niet besteedbaar". Door `JA` te kiezen, zal deze UTXO niet zichtbaar zijn in je Wallet en niet geselecteerd kunnen worden voor toekomstige transacties. Het blijft echter toegankelijk in de lijst met UTXO's in je Wallet, waar je de status handmatig kunt wijzigen. Het is aan te raden voor deze optie te kiezen om een afhandelingsfout te voorkomen die later je privacy in gevaar kan brengen. Als je `NO` kiest, blijft de giftige verandering beschikbaar voor gebruik in je Wallet. Als je meer wilt weten over het beheren en gebruiken van deze giftige wijziging, raad ik je aan het laatste deel van deze tutorial te lezen.


![samourai](assets/notext/30.webp)


Samourai zal dan je Tx0 uitzenden.


![samourai](assets/notext/31.webp)


### De muntverbindingen maken

Zodra de Tx0 is uitgezonden, kun je hem vinden op het tabblad `Transacties` van het Whirlpool-menu.


![samourai](assets/notext/32.webp)

Uw UTXO's die klaar zijn om gemengd te worden staan in het tabblad `Mixen bezig...`, dat overeenkomt met het **Premix** account.

![samourai](assets/notext/33.webp)


Zodra de `Tx0` is bevestigd, worden je UTXO's automatisch geregistreerd bij de coördinator en beginnen de eerste mixen automatisch.


![samourai](assets/notext/34.webp)


Door het tabblad `Remixing` te controleren, dat overeenkomt met de **Postmix** account, ziet u de UTXO's die het resultaat zijn van de eerste mixen. Deze munten blijven klaar voor latere remixen, die geen extra kosten met zich meebrengen. Ik raad aan dit andere artikel te raadplegen om meer te leren over het remixproces en de efficiëntie van een CoinJoin cyclus: [REMIX - Whirlpool](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)


![samourai](assets/notext/35.webp)


Je kunt het remixen van een UTXO tijdelijk onderbreken door op de pauzeknop rechts ervan te drukken. Om het opnieuw in aanmerking te laten komen voor remixen, klik je gewoon een tweede keer op dezelfde knop. Het is belangrijk om te weten dat er slechts één CoinJoin tegelijkertijd kan worden uitgevoerd per gebruiker en per pool. Dus, als je 6 UTXO's van `100 000 Sats` klaar hebt staan voor de CoinJoin, kan er maar één gemengd worden. Na het mixen van een UTXO, kiest Samourai Wallet willekeurig een nieuwe UTXO uit jouw beschikbaarheid, om het remixen van elke Coin te diversifiëren en in balans te brengen.


![samourai](assets/notext/36.webp)


Om de continue beschikbaarheid van je UTXO's voor remixen te garanderen, is het noodzakelijk om de Samourai-applicatie op de achtergrond actief te houden. Je zou een melding op je telefoon moeten zien die bevestigt dat Whirlpool actief is. Als je de applicatie sluit of je telefoon uitschakelt, worden de coinjoins onderbroken.


### De coinjoins voltooien

Om je gemixte bitcoins uit te geven, ga je naar de **Postmix** account waar `Remixing` staat in de Whirlpool menu tabs.


![samourai](assets/notext/37.webp)


Klik op het blauwe Whirlpool logo rechtsonder.


![samourai](assets/notext/38.webp)


Klik vervolgens op `Gemengde UTXO's uitgeven`.


![samourai](assets/notext/39.webp)


Je kunt dan de Address van de ontvanger en het te verzenden bedrag invoeren, op dezelfde manier als voor elke andere transactie die met Samourai Wallet wordt gedaan. De blauwe achtergrond geeft aan dat het geld wordt uitgegeven vanaf een Whirlpool rekening, en niet vanaf de **deposit** rekening.


![samourai](assets/notext/40.webp)


Door op de 3 kleine puntjes rechtsboven te klikken, kun je specifieke UTXO's selecteren.

![samourai](assets/notext/41.webp)

Door op het witte vierkantje rechtsboven in het venster te klikken, kun je de QR-code van de ontvangende Address scannen met je camera.


![samourai](assets/notext/42.webp)


Voer de benodigde informatie voor je bestedingstransactie in en klik vervolgens op de blauwe knop `VERIFIEER TRANSACTIE`.


![samourai](assets/notext/43.webp)


In de volgende stap heb je de mogelijkheid om het tarief te wijzigen dat aan je transactie is gekoppeld. U kunt ook de Stonewall-optie inschakelen door het betreffende vakje aan te vinken. Als de Stonewall-optie niet selecteerbaar is, betekent dit dat uw **Postmix**-account geen UTXO van voldoende grootte bevat om deze specifieke transactiestructuur te ondersteunen.


[-> Meer informatie over Stonewall-transacties](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


Als alles naar wens is, klik je op de Green `Verstuur ... BTC` knop.


![samourai](assets/notext/44.webp)


Samourai zal dan overgaan tot het ondertekenen van je transactie alvorens ze uit te zenden op het netwerk. Je hoeft alleen maar te wachten tot het wordt toegevoegd aan een blok door een Miner.


![samourai](assets/notext/45.webp)


### Een SCODE gebruiken

Soms bieden de Samourai Wallet teams "SCODE's" aan. Een SCODE is een promotiecode die korting geeft op de servicekosten van het zwembad. Samourai Wallet biedt af en toe zulke codes aan haar gebruikers tijdens speciale evenementen. Ik raad je aan [Samourai Wallet](https://twitter.com/SamouraiWallet) te volgen op sociale media om toekomstige SCODE's niet te missen.


Om een SCODE op Samourai toe te passen, voordat je een nieuwe CoinJoin cyclus start, ga je naar het Whirlpool menu en selecteer je de drie kleine puntjes rechtsboven in het scherm.


![samourai](assets/notext/46.webp)


Klik op `CODE (promotiecode) Whirlpool`.


![samourai](assets/notext/47.webp)


Voer de SCODE in het geopende venster in en bevestig door op `OK` te klikken.


![samourai](assets/notext/48.webp)


Whirlpool zal automatisch sluiten. Wacht tot Samourai klaar is met laden en open dan het Whirlpool-menu opnieuw.


![samourai](assets/notext/49.webp)


Controleer of je SCODE correct is geregistreerd door nogmaals op de drie kleine puntjes te klikken en vervolgens `SCODE (promo code) Whirlpool` te selecteren. Als alles in orde is, ben je klaar om een nieuwe Whirlpool cyclus te starten met korting op de servicekosten. Het is belangrijk om te weten dat deze SCODE's tijdelijk zijn: ze blijven een paar dagen geldig voordat ze vervallen.


## Hoe weet je de kwaliteit van onze CoinJoin cycli?

Wil een CoinJoin echt effectief zijn, dan is het essentieel dat deze een goede uniformiteit laat zien tussen de bedragen van inputs en outputs. Deze uniformiteit vergroot het aantal mogelijke interpretaties in de ogen van een externe waarnemer, waardoor de onzekerheid rond de transactie toeneemt. Om deze onzekerheid van een CoinJoin te kwantificeren, kan men de entropie van de transactie berekenen.


Voor een diepgaande verkenning van deze indicatoren (het Whirlpool model wordt erkend als het model dat de meeste homogeniteit in coinjoins brengt), verwijs ik je naar de tutorial: [BOLTZMANN CALCULATOR](https://planb.network/tutorials/privacy/analysis/boltzmann-entropy-738e45af-18a6-4ce6-af1a-1bf58e15f1fe)


Vervolgens wordt de prestatie van verschillende CoinJoin cycli geëvalueerd op basis van de omvang van de groepen waarin een Coin verborgen zit. De grootte van deze groepen bepaalt wat de anonsets genoemd worden. Er zijn twee soorten anonsets: de eerste beoordeelt de verkregen privacy ten opzichte van een retrospectieve analyse (van het heden naar het verleden) en de tweede ten opzichte van een prospectieve analyse (van het verleden naar het heden). Voor een gedetailleerde uitleg van deze twee indicatoren nodig ik je uit om de tutorial te raadplegen: [Whirlpool STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


## Hoe postmix beheren?

Na het uitvoeren van CoinJoin cycli is de beste strategie om je UTXO's in de **postmix** account te bewaren, wachtend op toekomstig gebruik. Het is zelfs aan te raden om ze onbeperkt te laten remixen totdat je ze nodig hebt om uit te geven.


Sommige gebruikers zouden kunnen overwegen om hun gemengde bitcoins over te zetten naar een Wallet beveiligd door een Hardware Wallet. Dit is mogelijk, maar het is belangrijk om de aanbevelingen van Samourai Wallet nauwgezet op te volgen om de verworven privacy niet in gevaar te brengen.


Het samenvoegen van UTXO's is de meest gemaakte fout. Het is noodzakelijk om het samenvoegen van gemengde UTXO's met ongemengde UTXO's in dezelfde transactie te vermijden, om de CIOH (*Common-Input-Ownership-Heuristic*) te vermijden. Dit vereist zorgvuldig beheer van je UTXO's binnen je Wallet, vooral wat betreft labeling. Buiten CoinJoin is het samenvoegen van UTXO's over het algemeen een slechte praktijk die vaak leidt tot verlies van privacy als het niet goed beheerd wordt.

Je moet ook waakzaam zijn over de consolidatie van gemengde UTXO's met elkaar. Gematigde consolidaties zijn mogelijk als je gemengde UTXO's aanzienlijke anonsets hebben, maar dit zal onvermijdelijk de privacy van je munten verminderen. Zorg ervoor dat consolidaties niet te groot zijn of na een onvoldoende aantal remixen worden uitgevoerd, omdat dit het risico met zich meebrengt dat er afleidbare verbanden ontstaan tussen je UTXO's voor en na de CoinJoin cycli. In geval van twijfel over deze operaties, is de beste praktijk om UTXO's na het mengen niet te consolideren en ze één voor één over te brengen naar je Hardware Wallet, waarbij je telkens een nieuwe lege Address genereert. Nogmaals, vergeet niet om elke ontvangen UTXO goed te labelen.


Het wordt ook afgeraden om je postmix UTXO's over te brengen naar een Wallet met behulp van ongebruikelijke scripts. Als je bijvoorbeeld Whirlpool binnenkomt vanuit een Multisig Wallet met behulp van `P2WSH` scripts, is de kans klein dat je gemengd wordt met andere gebruikers die oorspronkelijk hetzelfde type Wallet hebben. Als je je postmix verlaat naar dezelfde Multisig Wallet, zal het privacyniveau van je gemengde bitcoins sterk afnemen. Naast scripts zijn er nog veel meer Wallet fingerprints die je kunnen misleiden.


Net als bij elke Bitcoin transactie, is het ook hier beter om ontvangstadressen niet te hergebruiken. Elke nieuwe transactie moet worden ontvangen op een nieuwe blanco Address.


De eenvoudigste en veiligste oplossing is om je gemengde UTXO's te laten rusten in hun **postmix** account, ze te laten remixen en ze alleen aan te raken om uit te geven. Samourai en Sparrow wallets hebben extra beschermingen tegen al deze risico's gerelateerd aan ketenanalyse. Deze beschermingen helpen je fouten te voorkomen.


## Hoe ga je om met doxische verandering?

Vervolgens moet je voorzichtig zijn met het beheren van doxische verandering, de verandering die niet in de CoinJoin pool kon komen. Deze toxische UTXO's, die het gevolg zijn van het gebruik van Whirlpool, vormen een risico voor je privacy, omdat ze een verband leggen tussen jou en het gebruik van CoinJoin. Daarom is het noodzakelijk om er voorzichtig mee om te gaan en ze niet te combineren met andere UTXO's, vooral gemengde UTXO's. Hier zijn verschillende strategieën om te overwegen ze te gebruiken:


- Mengen in kleinere zwembaden:** Als je giftige UTXO groot genoeg is om alleen een kleiner zwembad in te gaan, overweeg dan om het te mengen. Dit is vaak de beste optie. Het is echter cruciaal dat je niet meerdere giftige UTXO's samenvoegt om toegang te krijgen tot een pool, omdat dit je verschillende ingangen kan koppelen.
- Markeer ze als "onbesteedbaar":** Een andere aanpak is om ze niet meer te gebruiken, ze te markeren als "onbesteedbaar" in hun speciale account en gewoon HODL te gebruiken. Dit zorgt ervoor dat je ze niet per ongeluk uitgeeft. Als de waarde van Bitcoin stijgt, kunnen er nieuwe pools ontstaan die geschikter zijn voor jouw giftige UTXO's;
- Donaties doen:** Overweeg om donaties te doen, zelfs bescheiden, aan ontwikkelaars die werken aan Bitcoin en de bijbehorende software. Je kunt ook doneren aan organisaties die BTC accepteren. Als het beheren van je giftige UTXO's te ingewikkeld lijkt, kun je er gewoon vanaf komen door een donatie te doen;
- Koop cadeaubonnen:** Platforms zoals [Bitrefill](https://www.bitrefill.com/) stellen je in staat om Exchange bitcoins te wisselen voor cadeaubonnen die je kunt gebruiken bij verschillende winkels. Dit kan een manier zijn om van je giftige UTXO's af te komen zonder de bijbehorende waarde te verliezen;
- Consolideer ze op Monero:** Samourai Wallet biedt nu een atomic swap service tussen BTC en XMR. Dit is ideaal voor het beheren van giftige UTXO's door ze te consolideren op Monero, zonder je privacy in gevaar te brengen via KYC, voordat je ze terugstuurt naar Bitcoin. Deze optie kan echter duur zijn in termen van Mining vergoedingen en de premie als gevolg van liquiditeitsbeperkingen;
- Stuur ze naar de Lightning Network:** Deze UTXO's naar de Lightning Network sturen om te profiteren van lagere transactiekosten is een optie die interessant kan zijn. Deze methode kan echter bepaalde informatie onthullen, afhankelijk van je gebruik van Lightning, en moet daarom met voorzichtigheid worden toegepast.


Gedetailleerde tutorials over het implementeren van deze verschillende technieken worden binnenkort aangeboden op PlanB Network.


**Toegevoegde bronnen:**

[Samourai Wallet video tutorial](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)


- [Samourai Wallet Documentatie - Whirlpool](https://docs.samourai.io/Whirlpool/basic-concepts);
- [Twitter thread over coinjoins](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Blogpost over coinjoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).