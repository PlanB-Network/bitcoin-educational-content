---
name: Inleiding tot Bitcoin mining
goal: Bitcoin mining en proof-of-work vanuit het niets begrijpen
objectives: 


  - proof-of-work en de rol ervan in Bitcoin begrijpen.
  - Analyseer het moeilijkheidsaanpassingsmechanisme.
  - Weten wat de technische termen in verband met mining eigenlijk betekenen.
  - De stappen beschrijven voor het bouwen van een Bitcoin blok en zijn componenten.
  - Belangrijke ontwikkelingen in de mining industrie identificeren.


---

# Ontdek de grondbeginselen van Bitcoin mining



De proof of work begrijpen is begrijpen hoe de Bitcoin werkt. Zonder deze uitvinding en het ingenieuze gebruik ervan, had Bitcoin eenvoudigweg niet kunnen bestaan. Deze cursus geeft je alle mining theorie die je nodig hebt voor je bitcoin-reis.



MIN 101 is vooral bedoeld voor beginners, omdat alle concepten precies vanaf nul worden uitgelegd. Als je echter al een gemiddeld kennisniveau hebt, kun je met deze cursus je begrip consolideren, enkele benaderende intuïties corrigeren en details verkennen die vaak ontbreken in de gangbare uitleg.



Aan het eind van deze cursus kun je op een eenvoudige en nauwkeurige manier uitleggen hoe proof-of-work werkt. MIN 101 is ook een ideale introductie voor alle andere meer geavanceerde cursussen over Bitcoin mining op Plan ₿ Academy, zowel theoretisch als praktisch.



+++


# Inleiding


<partId>041ff0fa-53c3-4d55-9888-d7840de283e9</partId>



## Cursusoverzicht


<chapterId>a82d49dc-d68a-4e3f-985e-bcef6643677e</chapterId>



Welkom bij de MIN 101 cursus, waarin je de fundamentele theoretische concepten van mining en Proof-of-Work binnen het Bitcoin systeem zult ontdekken. Deze cursus is de eerste stap in je Bitcoiner-reis om te begrijpen hoe mining werkt. Als je de cursus hebt afgerond, kun je doorstromen naar meer geavanceerde theoriecursussen, of zelf aan de slag gaan en een bitcoin miner worden!



In deze MIN 101 cursus gaan we niet terug naar de basisconcepten van Bitcoin, want we komen direct tot de kern van de zaak: mining. Als je nog nooit van Bitcoin hebt gehoord, of als de grondbeginselen ervan je nog niet helemaal duidelijk zijn, raad ik je sterk aan om te beginnen met onze inleidende BTC 101 cursus. Als je deze grondbeginselen eenmaal onder de knie hebt, kun je MIN 101 met vertrouwen aan:



https://planb.academy/courses/2b7dc507-81e3-4b70-88e6-41ed44239966


### Deel 1 - Inleiding



We beginnen deze cursus met een optioneel eerste hoofdstuk, waarin ik een zeer vereenvoudigde uitleg geef van mining, om je een duidelijk beeld te geven voordat we ingaan op de technische mechanismen.



Het doel is hier niet om je alle technische details te geven (die komen later in de cursus), maar om je een leidraad te geven. Als dit kader er eenmaal is, zal elk meer geavanceerd concept dat daarna wordt geïntroduceerd op natuurlijke wijze in deze structuur passen.



### Deel 2 - Hoe proof of work werkt



Na de inleiding is deel 2 de technische basis van het trainingsprogramma. Het doel is om stap voor stap uit te leggen hoe Bitcoin geldige blokken produceert. We beginnen met het ontdekken van de structuur van een blok, voordat we ingaan op het proof-of-work mechanisme: de rol van het doelwit, de nonce en de hashfunctie. Tenslotte zullen we zien hoe Bitcoin erin slaagt om een stabiele blokproductiesnelheid te behouden ondanks variaties in hashkracht, dankzij het moeilijkheidsaanpassingsmechanisme. Aan het eind van dit hoofdstuk heb je een volledig begrip van de fundamentele principes van Bitcoin's proof-of-work.



### Deel 3 - Het Bitcoin mining aanmoedigingssysteem



In het derde deel bekijken we waarom miners aangemoedigd worden om eerlijk deel te nemen aan mining. We gaan dieper in op het principe van de blokbeloning, de samenstelling en berekeningsmethode ervan, de evolutie in de tijd door middel van halvings en de specifieke rol van de coinbase transactie.



### Deel 4 - De Bitcoin mining industrie



Het vierde deel plaatst mining terug in de operationele realiteit. Het volgt de evolutie van mining machines, van het begin van Bitcoin tot het moderne ASIC, om de huidige hardwarebeperkingen te begrijpen. We kijken ook naar de basisprincipes van mining pools, om te begrijpen hoe mijnwerkers erin slagen de variatie van hun inkomsten te beperken.



### Deel 5 - Laatste deel



In het laatste deel van de cursus kun je je kennis van mining testen door je diploma te halen.



Het doel van deze MIN 101 cursus is dan ook om je te laten vertrekken met een duidelijk, gestructureerd en blijvend begrip van Bitcoin mining, zowel technisch als economisch.



Klaar om Bitcoin mining te ontdekken? Laten we beginnen!




## Bitcoin mining gemakkelijk gemaakt


<chapterId>278577a6-98bb-4659-86c7-f6c4f6d5fa3e</chapterId>



Voordat we overgaan tot een gedetailleerde en meer technische uitleg van Bitcoin [mining](https://planb.academy/resources/glossary/mining), wil ik je een overzicht geven van het principe, dat opzettelijk eenvoudig en schematisch is gehouden. Als je al wat basiskennis hebt, kun je in het volgende hoofdstuk, na het beantwoorden van de quizvragen, meteen door naar de kern van de zaak. Dit hoofdstuk is vooral bedoeld voor beginners, om je een zachte start te geven.



Stel je Bitcoin voor als een groot openbaar notitieblok, dat door iedereen gedeeld wordt, waarin we opschrijven wie er bitcoins naar wie heeft gestuurd. Dit notitieboek wordt de [blockchain](https://planb.academy/resources/glossary/blockchain) genoemd. Het kan niet in het bezit zijn van slechts één persoon, anders zou het vertrouwd moeten worden. In plaats daarvan werkt Bitcoin collectief: duizenden computers verifiëren en onderhouden dezelfde versie van dit notitieblok.



![Image](assets/fr/049.webp)



In Bitcoin maak je een [transactie](https://planb.academy/resources/glossary/transaction-tx) aan wanneer je een betaling doet. Deze transactie wordt niet meteen toegevoegd aan het notitieboek. Hij wordt eerst naar het netwerk gestuurd en wacht dan om in het volgende transactiepakket geïntegreerd te worden. Dit pakket wordt een [blok](https://planb.academy/resources/glossary/block) genoemd.



![Image](assets/fr/050.webp)



Een blok is gewoon een verzameling transacties die gegroepeerd zijn. Als een blok klaar is, is het niet genoeg om het te publiceren. Je moet het netwerk bewijzen dat het blok het waard is om toegevoegd te worden aan de pool. Dit is waar mining om de hoek komt kijken.



Mining is het valideren van een blok door energie te verbruiken. Actoren genaamd [miners](https://planb.academy/resources/glossary/miner) gebruiken gespecialiseerde computers. Deze machines verbruiken elektriciteit om een zeer groot aantal tests uit te voeren, in een lus, totdat ze een bewijs vinden dat door het netwerk wordt geaccepteerd. Wanneer een miner dit bewijs vindt, wordt zijn blok als geldig beschouwd.



Zodra het blok gevalideerd is, wordt het uitgezonden naar het netwerk. De andere [knooppunten](https://planb.academy/resources/glossary/node) controleren snel of het aan de regels voldoet en voegen het dan toe aan de reeks vorige blokken. Daarom wordt het een "blockchain" genoemd: elk nieuw blok komt na de anderen, in opeenvolgende volgorde, en deze keten groeit beetje bij beetje.



![Image](assets/fr/051.webp)



Kortom, transacties worden eerst aangemaakt. Daarna worden ze gegroepeerd in een blok. Vervolgens valideert een miner dit blok door elektriciteit te verbruiken. Ten slotte wordt dit blok toegevoegd aan de blockchain en worden de transacties die het bevat [bevestigd](https://planb.academy/resources/glossary/confirmation).



Als mijnwerkers elektriciteit verbruiken, is dat niet omdat ze vrijwilligers zijn. Ze doen het omdat er een beloning tegenover staat. Wanneer een miner een blok valideert, ontvangt hij twee soorten inkomsten. Aan de ene kant ontvangt hij nieuw gecreëerde bitcoins. Anderzijds int hij de [vergoedingen](https://planb.academy/resources/glossary/transaction-fees) die gebruikers betalen voor de transacties in het blok. Met andere woorden, de miner wordt zowel gecompenseerd door geprogrammeerde monetaire uitgifte als door transactievergoedingen die door een markt worden bepaald.



In dit stadium krijg je opzettelijk een heel eenvoudig beeld van mining. Er wordt nog niet in detail uitgelegd hoe het blok in elkaar zit, of hoe het bewijs waar miners naar op zoek zijn precies werkt, of hoe Bitcoin een constant tempo aanhoudt, of hoe de beloning precies berekend wordt, of hoe het geclaimd wordt. Dat is niet erg, dat is alles wat we gaan zien in de rest van deze MIN 101 cursus!



Het doel van dit hoofdstuk was gewoon om je een duidelijke mentale structuur te geven: transacties → blokken → mining → blockchain → beloning. Houd deze ideeënketen in gedachten. In de rest van de cursus zal elk hoofdstuk een laag technische details toevoegen over een van deze elementen, totdat je niet alleen begrijpt wat er aan de hand is, maar ook hoe en waarom het betrouwbaar werkt, op schaal, zonder baas en zonder dat je vertrouwen nodig hebt.



# Hoe proof of work werkt


<partId>e917e8e3-37f2-46fb-91b2-6a5ce6f0f5c3</partId>



## Het Bitcoin transactiepad


<chapterId>3b7a3502-4814-4554-8de1-86ac961a2958</chapterId>



Om te begrijpen waar Bitcoin mining allemaal om draait, moeten we eerst het pad van een typische Bitcoin transactie volgen. Dit zal je precies laten zien waar het blok om de hoek komt kijken, en waarom het de kern van het systeem is. Dat is wat ik je in dit eerste hoofdstuk wil laten ontdekken.



In Bitcoin is een transactie een datastructuur die het eigendom van bitcoins overdraagt van de ene gebruiker naar de andere. Concreet verbruikt het `outputs` van eerdere transacties (zogenaamde [UTXO's](https://planb.academy/resources/glossary/utxo)), verwijst ernaar als `inputs`, en creëert vervolgens nieuwe `outputs` die bepalen aan wie deze bitcoins nu toebehoren en onder welke voorwaarden ze later kunnen worden uitgegeven.



![Image](assets/fr/001.webp)



Een belangrijk punt bij Bitcoin is de machtiging om uit te geven. Bitcoin's staan niet op een rekening, zoals uw geld op de bank, maar zijn vergrendeld door bestedingsvoorwaarden. Wanneer een [wallet](https://planb.academy/resources/glossary/wallet) een UTXO als [invoer](https://planb.academy/resources/glossary/input) wil gebruiken, moet het cryptografisch bewijs leveren dat het het recht heeft om het te ontgrendelen. Dit bewijs neemt vaak de vorm aan van een [digitale handtekening](https://planb.academy/resources/glossary/digital-signature) generated van een [private sleutel](https://planb.academy/resources/glossary/private-key). Daarom dringen bitcoiners aan op het beveiligen van je privésleutels: deze ontgrendelen de toegang tot je bitcoins en stellen je dus in staat om ze uit te geven.



![Image](assets/fr/002.webp)



De digitale handtekening in Bitcoin speelt twee belangrijke rollen:




- Uitgave autoriseren: dit bewijst dat de gebruiker de privésleutel bezit die wordt verwacht door de UTXO uitgavevoorwaarde;
- Integriteitsbescherming: koppelt autorisatie aan de precieze details van de transactie (ontvangers, bedragen, kosten, enz.). Als iemand de transactie achteraf wijzigt, is de handtekening niet langer geldig.



Nadat de transactie correct is opgebouwd en ondertekend door de Bitcoin wallet van de gebruiker, moet deze worden uitgezonden op het Bitcoin netwerk.



### De rol van het Bitcoin knooppunt in de distributie



Bitcoin is een [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p) netwerk: er is geen centrale server die alle transacties ontvangt en verwerkt. Deze rol wordt collectief gespeeld door de nodes. Een Bitcoin knooppunt is een stuk software (bijv. [Bitcoin Core](https://planb.academy/resources/glossary/bitcoin-core)) dat verbonden is met andere knooppunten in het Bitcoin netwerk, met als belangrijkste missie het verifiëren, opslaan en doorgeven van transacties en blokken.



Wanneer je een transactie verstuurt vanaf een wallet, stuurt de wallet deze door naar een knooppunt (jouw eigen knooppunt, of dat van een service). Dit knooppunt controleert eerst of de transactie voldoet aan verschillende regels, zoals:




- handtekeningen geldig zijn;
- de ingangen verwijzen naar bestaande UTXO's (d.w.z. bitcoins die bestaan);
- deze UTXO niet al elders zijn uitgegeven;
- de hoeveelheid [outputs](https://planb.academy/resources/glossary/output) is kleiner dan of gelijk aan de hoeveelheid inputs (bitcoins worden niet uit het niets gecreëerd);
- enz.



Als de transactie al deze controles doorstaat, verspreidt het knooppunt de transactie naar de andere knooppunten in het netwerk waarmee het verbonden is. Zij controleren het op hun beurt en geven het door, enzovoort. Binnen een paar seconden is de transactie verspreid en bekend bij het hele, of in ieder geval een groot deel, van het Bitcoin netwerk.



![Image](assets/fr/003.webp)



### De mempool: de wachtkamer voor transacties



Tussen het moment dat een transactie wordt uitgezonden en het moment dat het wordt bevestigd in een blok, moet het wachten. Deze wachtruimte wordt **de [mempool](https://planb.academy/resources/glossary/mempool)** genoemd (samentrekking van `memory` en `pool`). Een mempool is dus een tijdelijke opslagruimte voor geldige, maar nog onbevestigde transacties.



Belangrijk punt: er bestaat niet zoiets als een enkele mempool, alleen mempools. Elk knooppunt onderhoudt zijn eigen mempool, met zijn eigen lokale beperkingen. Dit betekent dat twee knooppunten op elk moment een lichtjes verschillende mempoolinhoud kunnen hebben (afhankelijk van wat ze hebben ontvangen, wat ze hebben geweigerd of wat ze hebben verwijderd).



![Image](assets/fr/004.webp)



In dit stadium is het netwerk op de hoogte van de transactie, heeft het deze geverifieerd en houdt het deze in het geheugen totdat deze wordt bevestigd. Maar deze transactie wordt pas bevestigd als een miner het in een blok invoegt en dit blok door het netwerk wordt geaccepteerd.



### Blockchain: een openbaar tijdstempelregister



Omdat bitcoin een immateriële valuta is, moet het één probleem aanpakken: het voorkomen van [dubbele uitgaven](https://planb.academy/resources/glossary/double-spending-attack) zonder een centrale autoriteit. Als twee transacties hetzelfde UTXO proberen uit te geven, moet iedereen kunnen convergeren naar één coherente staat. Satoshi Nakamoto vat dit probleem samen met deze beroemde zin:



> De enige manier om de afwezigheid van een transactie te bevestigen is door op de hoogte te zijn van alle transacties.

Met andere woorden, om te weten of een bitcoin nog niet is uitgegeven, heb je een algemeen overzicht nodig van uitgaven in het verleden.



Dit is de rol van de blockchain: een openbaar register dat de geschiedenis van transacties bevat. Maar in plaats van elke transactie op te schrijven op het moment dat deze plaatsvindt, groepeert Bitcoin ze in blokken. Elk blok fungeert als een geschiedenispagina en het systeem functioneert dus als een tijdstempelserver: het ordent transacties in de tijd op een verifieerbare manier.



Dit register kan niet herschreven worden dankzij een eenvoudig principe: elk blok bevat de cryptografische vingerafdruk ([hash](https://planb.academy/resources/glossary/hash-function)) van het vorige blok. Blokken zijn dus aan elkaar gekoppeld: als je een blok uit het verleden wijzigt, verandert de hash, waardoor de koppeling met het volgende blok verbroken wordt, waardoor de koppeling met het blok daarna verbroken wordt, enzovoort. Het is deze keten van afhankelijkheden die de "*blockchain*" zijn naam geeft.



![Image](assets/fr/005.webp)



Zodra we deze basisprincipes van Bitcoin begrijpen, kunnen we het doel van een miner in concretere termen beschrijven: een nieuw blok bouwen dat de bestaande keten uitbreidt, door hangende transacties in te schrijven, en dan proberen het geldig te maken (dit is het beroemde "[proof of work](https://planb.academy/resources/glossary/proof-of-work)" dat we in een later hoofdstuk zullen bestuderen). Maar laten we eerst in het volgende hoofdstuk samen ontdekken hoe een kandidaatblok wordt opgebouwd.



## Een Bitcoin blok bouwen


<chapterId>2b5cd04b-d400-4865-b0a0-e70fa7e67c17</chapterId>



Je hebt nu begrepen hoe een Bitcoin transactie werkt en wat de rol van de blockchain is. Maar voordat we dieper ingaan op hoe proof-of-work werkt, is er nog één essentiële stap die de miner moet uitvoeren: de constructie van een [kandidaatblok](https://planb.academy/resources/glossary/candidate-block). Laten we samen uitzoeken wat een kandidaatblok is en hoe de miner het construeert, voordat we op zoek gaan naar een geldig bewijs.



### Het kandidaat-blok



Miner's moeten hun blokken zelf bouwen voordat ze ze proberen te mijnen. Elke miner bouwt op zijn beurt een zogenaamd kandidaatblok uit de transacties die in zijn mempool staan te wachten. Het bouwen van een kandidaatblok bestaat dus uit:




- kiezen welke transacties je wilt opnemen;
- deze transacties organiseren op een manier die compatibel is met de Bitcoin regels;
- de metadata van het blok produceren, opgeslagen in de [koptekst](https://planb.academy/resources/glossary/block-header).



De keuze van transacties volgt een eenvoudige economische logica: een blok heeft een capaciteit die beperkt wordt door het Bitcoin protocol, dus de miner probeert te maximaliseren wat hij voor deze ruimte verdient. Hij selecteert als prioriteit de transacties die de hoogste vergoedingen bieden in verhouding tot de ruimte die ze innemen in het blok (dit staat bekend als de "vergoedingsvoet", uitgedrukt in sats/vB). De details van vergoedingen worden later behandeld; onthoud alleen het idee van sorteren op ruimte-efficiëntie.



Een Bitcoin blok bestaat daarom uit twee hoofdonderdelen:




- een lijst met transacties;
- een blokkop, die in zekere zin dient als identiteitskaart van het blok.



![Image](assets/fr/006.webp)



De header is essentieel, want deze wordt gebruikt als basis voor proof-of-work: in Bitcoin wordt niet direct een heel blok gemijnd, maar alleen de header van een blok, die de informatie samenvat die nodig is om het blok aan de keten te koppelen en de inhoud vast te leggen. Om de header in staat te stellen alle transacties te vertegenwoordigen, gebruikt Bitcoin een cryptografisch hulpmiddel: de [Merkle boom](https://planb.academy/resources/glossary/merkle-tree).



### De Merkle-boom: een grote reeks transacties samenvatten



Het zou onmogelijk zijn om alle transacties in de header op te sommen: een blok kan duizenden transacties bevatten, terwijl de header een vaste grootte heeft (80 bytes). De oplossing is daarom om een unieke hash te berekenen die afhankelijk is van alle transacties in het blok: dit is de [Merkle root](https://planb.academy/resources/glossary/merkle-root).



Het principe is als volgt:




- wordt de cryptografische vingerafdruk (hash) van elke transactie berekend;
- deze hashes worden gekoppeld, samengevoegd en dan opnieuw gehasht om een nieuwe laag hashes te vormen;
- dit proces wordt herhaald totdat een enkele hash is verkregen: de Merkle root.



![Image](assets/fr/007.webp)



Dus als een enkele transactie verandert, zelfs met een enkele bit, is het resultaat een wijziging van de vingerafdruk, die wordt doorgegeven aan de Merkle root. Deze root is opgenomen in de koptekst van het blok. Dus het wijzigen van een transactie uit het verleden betekent het wijzigen van de koptekst van het blok waarin het is opgenomen, en dus de voetafdruk van het blok, en vervolgens de koppeling met volgende blokken.



Sinds [SegWit](https://planb.academy/resources/glossary/segwit) hebben we de handtekeningen gescheiden van de rest. Dus in werkelijkheid zijn er 2 Merkle bomen genest in elk blok. Deze scheiding heeft gevolgen voor de manier waarop we de grootte van een blok tellen en voor bepaalde cryptografische vastleggingen, maar het basisidee blijft hetzelfde: de header moet op een compacte manier de hele inhoud van het blok vastleggen.



### Kopregel blok



De header van het blok is 80 bytes lang en bevat precies 6 velden. Het zijn deze zes elementen die gehasht worden bij het zoeken naar een proof of work (zie volgende hoofdstuk):





- De versie (`version`): Dit geeft aan aan welke regels of update signalen het blok voldoet. Het dient als een mechanisme voor het onderhouden van protocolcompatibiliteit en evolutie.




- Vorige blok hash (`previousblockhash`): Dit is de hash van de header van het vorige blok. Dit is wat de blokken met elkaar verbindt. Zonder dit veld zouden we onafhankelijke blokken hebben. Door de hash van de header van het vorige blok op te nemen, krijgen we een keten, waarbij elk nieuw blok voortbouwt op het vorige.





- Merkle root (`merkleroot`): Dit is de vingerafdruk van alle transacties in het blok (via de Merkle-boom). Het verbindt de header met de inhoud: als de miner de selectie of volgorde van transacties wijzigt, verandert de root.





- [Tijdstempel](https://planb.academy/resources/glossary/timestamp): Dit is een tijdstempel (Unix-tijd) gekozen door de miner (met geldigheidsbeperkingen), die moet aangeven wanneer het blok werd gemined. Het hoeft niet tot op de seconde nauwkeurig te zijn, maar het moet aan bepaalde voorwaarden voldoen om acceptabel te blijven voor het netwerk.





- Gecodeerd [moeilijkheidsdoel](https://planb.academy/resources/glossary/difficulty-target) (`nbits`): Dit veld codeert het huidige moeilijkheidsdoel. We zullen meer in detail treden in het hoofdstuk over moeilijkheid, maar onthoud dat deze parameter deel uitmaakt van de header.





- [Nonce](https://planb.academy/resources/glossary/nonce) (`nonce`): Dit is een waarde die de mijnwerker vrij kan aanpassen. Het dient als een instelbare variabele tijdens proof-of-work. Ik zal de rol in meer detail uitleggen in het volgende hoofdstuk, maar het is belangrijk om te begrijpen dat de nonce deel uitmaakt van de block header en ontworpen is om opeenvolgende pogingen mogelijk te maken.



Om dit gemakkelijker te visualiseren is hier een voorbeeld van een block header in hexadecimaal formaat (80 bytes):



```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```



Hier is een uitsplitsing per veld:



```text
version: 00e0ff3f
previousblockhash: 5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
merkleroot: 206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
time: bcb13a64
nbits: b2e00517
nonce: 43f09a40
```



Deze kandidaat block header, geconstrueerd door de miner, vormt de basis van hun werk. Bij het zoeken naar een geldige proof-of-work, is het niet de hele lijst van transacties die direct gehashed wordt in een lus, maar eerder dit 80-byte blok, dat alles bevat wat nodig is om het blok te linken aan het verleden en de inhoud vast te leggen, terwijl het ook de parameters bevat die nodig zijn voor het mining mechanisme, dat we in het volgende hoofdstuk zullen onderzoeken.



## De hash, het doel en de nonce


<chapterId>d054323b-16bd-4556-bac5-4878654e59a3</chapterId>



In de vorige hoofdstukken volgde je het pad van een Bitcoin transactie: gecreëerd en ondertekend door een wallet, doorgegeven door nodes, opgeslagen in mempools, en dan bevestigd wanneer een miner het opneemt in een blok dat door het netwerk aanvaard wordt. Maar we hebben nog niet gezien hoe een miner zijn blok kan toevoegen aan de blockchain. Wat is het proces achter mining?



Het begrijpen van het mining proces is vrij eenvoudig. Het komt neer op 3 concepten die hand in hand gaan: een hashfunctie, een doelwaarde en een variabele die de miner kan aanpassen. Laten we eens kijken hoe het allemaal werkt.



### De hashfunctie



Een hashfunctie is een hulpmiddel dat een bericht als invoer neemt en een uitvoer van vaste grootte produceert, genaamd "*fingerprint*" of "*hash*".



![Image](assets/fr/010.webp)



De hashfunctie is interessant in computersystemen omdat het bepaalde eigenschappen heeft:





- Als je ook maar één bit van de invoer verandert, dan verandert de resulterende uitvoerhash volledig en onvoorspelbaar;



![Image](assets/fr/011.webp)





- Het is onmogelijk om van de uitgang naar de ingang te gaan: de functie is onomkeerbaar;



![Image](assets/fr/012.webp)





- Het is onmogelijk om twee verschillende berichten te vinden die precies dezelfde hash geven.



![Image](assets/fr/013.webp)



De hashfunctie gebruikt in Bitcoin voor mining is `SHA256`, twee keer achter elkaar toegepast. Dit staat bekend als dubbel [SHA256](https://planb.academy/resources/glossary/sha256), of `SHA256d`. Het is deze dubbele hashing die de vingerafdruk van het blok produceert.



```text
hash = SHA256(SHA256(message))
```



In ons geval komt de `message` in feite overeen met de block header, die je in het vorige hoofdstuk hebt gezien. Ter herinnering, de header is een kleine structuur die alles in het blok samenvat.



![Image](assets/fr/014.webp)



### Werkbewijs: een hash vinden die kleiner is dan het doel



Proof-of-Work wordt vaak beschreven als het oplossen van een complex probleem. In werkelijkheid is het niet zozeer een probleem als wel een trial-and-error zoektocht: de miner moet een versie van de header vinden waarvan de hash (na het passeren van de `SHA256d` hashfunctie) voldoet aan een eenvoudige voorwaarde: hij moet kleiner zijn dan een bepaald doel.



Deze voorwaarde wordt als volgt geformuleerd:




- de hash van de blokkop wordt berekend met een hashfunctie;
- interpreteren we deze hash als een getal;
- voor een geldig blok moet dit getal kleiner of gelijk zijn aan een waarde genaamd "*moeilijkheidsdoel*".



Met andere woorden, een blok is geldig als:



```text
SHA256d(block_header) <= target
```



![Image](assets/fr/015.webp)



Het doel is een 256-bits getal. Aangezien de hash geproduceerd door `SHA256d` ook 256 bits is, kunnen ze vergeleken worden als twee getallen. Hoe lager het doel, hoe moeilijker de voorwaarde, omdat er minder mogelijke resultaten onder deze drempel zijn. Omgekeerd geldt: hoe hoger het doel, hoe makkelijker de voorwaarde te vervullen is en hoe makkelijker het wordt om een blok te mijnen. We zullen in latere hoofdstukken nader bekijken hoe dit doel wordt bepaald.



In dit systeem is de hashfunctie interessant. Onthoud dat het makkelijk is om de output te berekenen uit de input, maar onmogelijk om een input te vinden door alleen de output van de functie te kennen. In mining worden mijners niet gevraagd om een precieze hash te vinden, maar eerder om een hash onder een doelwaarde te vinden. De enige manier om dit te bereiken is door een zeer groot aantal pogingen te doen, totdat een bepaalde header van hun kandidaatblok, wanneer gehasht, een hash produceert die kleiner is dan dit doel.



Zodra het doel laag genoeg is, wordt dit proces duur. De miner berekent de hash van de header van zijn kandidaatblok, controleert het resultaat en als de voorwaarde niet vervuld is, wijzigt hij de header en herhaalt hij de berekening. Deze lus wordt herhaald tot een geldige header is gevonden. Wanneer de hash van de header uiteindelijk aan de voorwaarde voldoet, is de proof of work vastgesteld, wordt het blok als geldig beschouwd en kan het uitgezonden worden op het Bitcoin netwerk zodat knooppunten het aan hun blockchain kunnen toevoegen. De winnende miner ontvangt dan de bijbehorende beloning (we zullen de samenstelling ervan later in detail bespreken), terwijl alle miners onmiddellijk op zoek gaan naar een nieuwe, geldige header voor het volgende blok.



Het fundamentele voordeel van dit mechanisme ligt in de asymmetrie. Het produceren van een proof of work is kostbaar voor miners, omdat het een groot aantal hashberekeningen vereist. Aan de andere kant is de verificatie voor verifieerders, d.w.z. netwerkknooppunten, extreem eenvoudig: het enige wat ze hoeven te doen is de block header, geleverd door de miner, te hashen en te controleren of de resulterende hash inderdaad lager is dan het doel. Het vinden van een bewijs vereist dus veel werk en middelen, terwijl het verifiëren van de geldigheid ervan snel en goedkoop is. Het is precies deze eigenschap die een efficiënt proof-of-work systeem definieert.



### De nonce



Een praktische vraag blijft: als de header van het kandidaatblok die door de miner geconstrueerd is geen geldige hash geeft, hoe kan de miner het dan opnieuw proberen? Hij moet iets in de header wijzigen om een andere hash te verkrijgen. Dit is precies de rol van de nonce.



Onthoud de eerste eigenschap van een hashfunctie: het veranderen van een enkele bit van de invoer is genoeg om een totaal verschillende en onvoorspelbare uitvoer hash te produceren. Elke hashberekening is daarom verwant aan een willekeurige trekking.



![Image](assets/fr/016.webp)



Om zijn geluk opnieuw te beproeven, hoeft de miner niet de hele header van zijn kandidaatblok aan te passen: hij hoeft er maar een heel klein stukje van te veranderen, want zelfs een enkel ander bitje zal resulteren in een compleet nieuwe hash, mogelijk geldig als deze kleiner is dan het doel.



Dit is precies waarom de koptekst van het blok een nonce bevat. De nonce is een 32-bits waarde, die één keer wordt gebruikt en daarna wordt vervangen. Praktisch gezien kan een miner voor hetzelfde kandidaat-blok ongeveer 4,29 miljard mogelijke waarden testen (van `0` tot `2^32 - 1`). Elke variatie van de nonce wijzigt de koptekst van het blok en dus ook de hash die geproduceerd wordt na het toepassen van de `SHA256d` hashfunctie.



Het mining proces is heel eenvoudig:




- bouwt de miner een kandidaatblok (transacties + koptekst);
- berekent dan de hash van de `SHA256d(header)`;
- als het resultaat groter is dan het doel, wordt de nonce gewijzigd;
- begint opnieuw;
- enz.



![Image](assets/fr/017.webp)



In feite is de nonce niet het enige veld dat gewijzigd kan worden. Elke wijziging binnen de transacties van een blok resulteert in een wijziging van de stam van de Merkle boom, en dus een wijziging van de kop van dat blok. Met moderne rekenkracht kunnen de 4,29 miljard mogelijke waarden van de nonce relatief snel worden doorlopen. Daarom is er nog een veld, meestal aangeduid als "*[extra-nonce](https://planb.academy/resources/glossary/extra-nonce)*", dat de mogelijkheden voor headervariatie verder vermenigvuldigt. We zullen in een later hoofdstuk meer in detail op dit mechanisme terugkomen.



### Wat is het nut van proof of work?



We noemen het "bewijs" omdat het resultaat onmiddellijk verifieerbaar is: zodra een blok geproduceerd is, kan elk knooppunt in een fractie van een seconde controleren of de cryptografische hash van zijn header inderdaad onder het vereiste doel ligt. We noemen het "werk" omdat het bereiken van deze hash een groot aantal pogingen vereist, en dus echte kosten met zich meebrengt in termen van rekenkracht en energie.



In het Bitcoin [witboek](https://planb.academy/resources/glossary/white-paper) noemt Satoshi Nakamoto twee voordelen van het gebruik van een proof-of-work systeem in Bitcoin:





- Sealing van de economische geschiedenis:**



Als de rekenlast eenmaal opgebruikt is, is het blok vergrendeld: om het te wijzigen zou de proof of work van dat blok opnieuw gedaan moeten worden. En omdat de blokken aan elkaar gekoppeld zijn, zou het wijzigen van een oud blok ook betekenen dat alle volgende blokken opnieuw berekend moeten worden, om vervolgens het lopende werk van de eerlijke keten in te halen en te overtreffen.



Met andere woorden, de proof-of-work dient als de ruggengraat van het tijdstempelsysteem, waardoor het steeds kostbaarder wordt om het verleden te vervalsen naarmate de blokken zich opstapelen. Wanneer een nieuw blok wordt gedolven, wordt de beveiliging die door de proof of work wordt geleverd, gelijktijdig en uniform toegepast op alle bestaande UTXO's. Bij elk blok dat wordt toegevoegd, accumuleert elke UTXO dus extra tijd. Met elk blok dat wordt toegevoegd, accumuleert elke UTXO dus een extra hoeveelheid beveiliging van de Proof-of-Work.





- Definieer meerderheidsregel ([consensus](https://planb.academy/resources/glossary/consensus)) en neutraliseer Sybil:**



Proof-of-Work stelt Bitcoin ook in staat om consensus te bereiken zonder te vertrouwen op de "één ID = één stem" stemregel, die gemakkelijk vervalst zou kunnen worden door de massale aanmaak van identiteiten (IP's, knooppunten, sleutels...).



In Bitcoin is de "*meerderheid*" niet het grootste aantal deelnemers, maar de **keten die het meeste werk verzamelt**. Zoals Satoshi het zegt, is dit een "één CPU = één stem" principe, d.w.z. een stem gewogen door de werkelijke rekenkracht die wordt gebruikt om geldige blokken te produceren. Dus het inzetten van duizenden nodes levert geen voordeel op ten opzichte van Bitcoin. Zonder extra rekenkracht worden er geen werkbewijzen meer verzameld en wordt de [Sybil-aanval](https://planb.academy/resources/glossary/sybil-attack) nutteloos, terwijl de beslisregel objectief blijft en geen identificatie van deelnemers vereist.



![Image](assets/fr/018.webp)



[Nakamoto, S. (2008). *Bitcoin: Een Peer-to-Peer elektronisch geldsysteem.*](https://bitcoin.org/bitcoin.pdf)



De principes met betrekking tot het nut en de bevoegdheden van minderjarigen zijn een zeer complex onderwerp, waar ik in deze cursus niet dieper op in zal gaan. In toekomstige MIN 201 trainingen zullen we echter dieper ingaan op dit onderwerp.



Op dit moment kun je samenvatten hoe mining als volgt werkt: miners bouwen een kandidaatblok met de transacties die in behandeling zijn in de mempools en zoeken dan naar een hash van de header (via `SHA256d`) die kleiner is dan of gelijk is aan een doel. Ze bereiken dit door nonces te testen met vallen en opstaan.



In het volgende hoofdstuk maken we een korte historische omweg naar het proof-of-work principe om de achtergrond ervan te begrijpen en dan kijken we hoe de moeilijkheidsgraad wordt bepaald door het systeem.



## De geschiedenis van proof of work


<chapterId>919d9f3e-8b3b-41d9-b45a-54df4f3c31a3</chapterId>



Proof-of-work werd niet uitgevonden voor Bitcoin. [Satoshi Nakamoto](https://planb.academy/resources/glossary/nakamoto-satoshi) heeft verschillende oudere ideeën overgenomen en samengevoegd, die al in verschillende contexten waren onderzocht.



### Hashcash



Eind jaren 1990 werd het probleem van e-mailspam groot. Als het versturen van een e-mail bijna niets kost, kan een spammer er miljoenen versturen. Maar als elk bericht een kleine rekenkundige inspanning vereist, blijft het verzenden van een enkel legitiem bericht eenvoudig voor een normale gebruiker, terwijl het verzenden van miljoenen berichten erg duur wordt.



Dit is het doel van [Hashcash](https://planb.academy/resources/glossary/hashcash), voorgesteld door Adam Back in 1997, dat beschouwd wordt als de uitvinding van het proof-of-work principe. Het Hashcash principe lijkt erg op mining: produceer een hash die aan een voorwaarde voldoet (met een bepaald aantal nullen aan het begin van de hash). Het bewijs vergezelt dan het bericht en kan zeer snel geverifieerd worden door de ontvanger. Als een e-mail wordt ontvangen die dit bewijs niet bevat, kan deze onmiddellijk als spam worden beschouwd en dus worden gefilterd. Spammers zijn dan gedwongen om een aanzienlijke hoeveelheid energie te steken in het verzenden van miljoenen berichten, wat de winstgevendheid van dit soort operaties, of het nu gaat om marketing of fraude, drastisch vermindert (of zelfs helemaal teniet doet).



Tegenwoordig wordt Hashcash niet meer gebruikt voor e-mail. Het filteren van spam is nu grotendeels gebaseerd op gecentraliseerde systemen. Het voordeel van Hashcash ten opzichte van de huidige oplossingen ligt in het feit dat er geen gecentraliseerde filtering nodig is: iedereen kan de parameters aanpassen volgens zijn eigen criteria. Het vereist ook geen identificatie, omdat een hashzoekopdracht anoniem kan worden uitgevoerd. Bovendien is het niet afhankelijk van een reputatiesysteem, dat de neiging heeft om subjectieve vormen van filtering te introduceren.



Hashcash ging niet over het creëren van geld. Het wilde marginale kosten opleggen aan een eenvoudig te automatiseren digitale actie.



![Image](assets/fr/008.webp)



### Bit Goud



Eind jaren 1990 en begin jaren 2000 verkende Nick Szabo het idee van digitale schaarste gebaseerd op proof of work. Zijn conceptuele project, Bit Gold genaamd, voorziet in de creatie van waarde-eenheden door het oplossen van een kostbare proof of work en deze bewijzen vervolgens op te nemen in een register om een vorm van eigendom vast te stellen.



Bit Gold resulteerde niet in een ingezet systeem zoals Bitcoin, maar het bevat wel een aantal belangrijke inzichten: het idee dat computatie schaarste kan produceren en het idee om elementen in de loop van de tijd te timen om een geschiedenis te creëren die moeilijk te herschrijven is.



### RPOW



In 2004 stelde Hal Finney RPOW (*Reusable Proofs of Work*) voor. Het idee was om werkbewijzen te produceren die vervolgens konden worden uitgewisseld, in plaats van simpelweg geconsumeerd. RPOW wilde digitale token's maken op basis van proof of work, met een systeem om deze token's te verifiëren en over te dragen zonder ze te dupliceren. Ook RPOW loste het probleem van een volledig gedecentraliseerd register niet bevredigend op, zoals Bitcoin later zou doen, maar het blijft een van de grote voorlopers van Bitcoin.



![Image](assets/fr/009.webp)



Hashcash, Bit Gold en RPOW gebruiken proof-of-work om kosten op te leggen en een vorm van schaarste te creëren. Bitcoin neemt dit mechanisme over, maar geeft het een centrale en collectieve rol: proof-of-work wordt niet alleen gebruikt om iets te creëren, het wordt ook gebruikt om te beslissen wie het recht heeft om de volgende pagina van het register (het volgende blok) te schrijven, en om dit register duur te maken om te vervalsen.



## De moeilijkheidsdoelstelling aanpassen


<chapterId>528bcaa8-351e-4eae-887a-426a78a223e3</chapterId>



In de vorige hoofdstukken zag je het hart van proof-of-work: miners hashen de header van hun kandidaat-blok met `SHA256d`, en het blok wordt alleen als geldig beschouwd als de resulterende hash numeriek kleiner of gelijk is aan een referentiewaarde genaamd het doel. De vraag blijft dan: waar komt dit doel vandaan en hoe zorgt het systeem ervoor dat het consistent blijft in de tijd?



Bitcoin streeft naar een gemiddelde snelheid van één gevonden blok per 10 minuten. Uiteraard is dit tempo niet tot op de seconde gegarandeerd. In de praktijk worden sommige blokken een paar seconden na de vorige gevonden, terwijl andere pas na meer dan een uur worden gevonden. Waar het hier om gaat is het gemiddelde over een voldoende lange periode.



![Image](assets/fr/019.webp)



Deze variabiliteit komt voort uit de probabilistische aard van mining: elke hash is een onafhankelijke poging, met een constante waarschijnlijkheid (ervan uitgaande dat het doel onveranderd blijft) om een resultaat onder het doel te produceren. Het kan daarom vergeleken worden met een loterij met een continue trekking: hoe meer hashes mijners per seconde maken, hoe korter de verwachte vertraging voor het verschijnen van een geldig blok, maar zonder ooit de willekeurigheid van de ene trekking naar de volgende te elimineren.



### Waarom streven naar 10 minuten tussen de blokken?



Hoewel hier geen bewijs voor is, heeft Satoshi Nakamoto zeker voor 10 minuten gekozen als praktisch compromis tussen efficiëntie en veiligheid. Een korter interval zou frequentere bevestigingen geven, maar zou meer tijdelijke netwerksplitsingen veroorzaken. Om dit punt te begrijpen, moeten we teruggaan naar de manier waarop een blok zich voortplant.



Wanneer een miner een geldig blok vindt, verdeelt hij het onmiddellijk onder zijn peers. De knooppunten die het ontvangen, controleren de geldigheid ervan (transacties, proof of work, consensusregels, enz.) en geven het dan op hun beurt door. Deze verspreiding neemt een bepaalde tijd in beslag, die beperkt wordt door de latentie van het internet, de bandbreedte en het vermogen van elke node om het blok te verifiëren.



![Image](assets/fr/020.webp)



Als tijdens deze verspreidingsvertraging een andere mijnwerker ook een geldig blok ontdekt op dezelfde hoogte, kan het netwerk tijdelijk gesplitst worden: een deel van de knooppunten en mijnwerkers vertrouwt op blok A, terwijl het andere deel vertrouwt op blok B. Dit is een tijdelijke opsplitsing van het netwerk.



![Image](assets/fr/021.webp)



Deze verdeeldheid is niet catastrofaal. De Nakamoto consensus voorspelt dat op de lange termijn slechts één tak zal overheersen: degene die het meeste werk verzamelt. Zodra er bijvoorbeeld een nieuw blok wordt gedolven bovenop blok A, zal het hele netwerk opnieuw synchroniseren op deze tak en blok B verlaten, dat dan een "*[stale blok](https://planb.academy/resources/glossary/stale-block)*" wordt, in het dagelijks taalgebruik soms ten onrechte een "*orphan blok*" genoemd.



![Image](assets/fr/022.webp)



Aan de andere kant hebben ze een prijs: een fractie van de miners werkt een paar minuten aan een tak die zal worden verlaten. Dit werk is dan verspild vanuit het oogpunt van algemene veiligheid, omdat het niet heeft bijgedragen aan de uiteindelijke keten. Hoe sneller het interval tussen elk blok, hoe groter de kans op zulke splitsingen, aangezien de propagatietijd een groter deel van de tijd tussen elk blok vertegenwoordigt.



Het interval van 10 minuten geeft het winnende blok over het algemeen genoeg tijd om zich wijd te verspreiden voordat een concurrerend blok op dezelfde hoogte wordt gevonden. Het is een compromis dat splitsingen beperkt, verspilling van rekenkracht vermindert en het netwerk helpt om wereldwijd gesynchroniseerd te blijven.



### hashrate begrijpen



*"[Hashrate](https://planb.academy/resources/glossary/hashrate)*" verwijst naar de hoeveelheid hashberekeningen die per seconde geproduceerd worden, door een enkele mijnwerker, een groep mijnwerkers of alle mijnwerkers in Bitcoin. Het wordt uitgedrukt in `H/s` (hashes per seconde), met veelvouden als `TH/s` (terahashes per seconde) of `EH/s` (exahashes per seconde). Dit staat voor het aantal pogingen dat miners per seconde kunnen doen om te proberen een hash te krijgen die lager is dan het doel.



Als het doel vast blijft staan, dan:




- elke poging heeft een vaste kans op succes;
- meer pogingen per seconde doen verhoogt de kans dat een winnende poging snel verschijnt


Met andere woorden, als het Bitcoin netwerk van morgen zijn rekenkracht verdubbelt door twee keer zoveel mining machines aan te sluiten, zouden zonder een correctiemechanisme blokken gemiddeld twee keer zo snel gevonden worden. De doelstelling moet daarom worden aangepast om hashrate variaties te compenseren.



### De moeilijkheidsdoelstelling aanpassen



Bitcoin lost dit probleem op met een periodiek doelaanpassingsmechanisme, dat de moeilijkheidsgraad van mining aanpast. Het principe is als volgt: elke 2016 blokken (ongeveer elke 2 weken), herberekent elk knooppunt de moeilijkheidsdoelstelling door te observeren hoeveel tijd er daadwerkelijk nodig was om deze 2016 blokken te produceren.



Het doel van dit mechanisme is om de gemiddelde productietijd van een blok terug te brengen tot ongeveer 10 minuten, terwijl de totale hashrate van het netwerk constant verandert doordat machines worden losgekoppeld of juist nieuwe machines worden toegevoegd.



![Image](assets/fr/023.webp)



De berekening is gebaseerd op de waargenomen tijd voor de verstreken periode:




- als de laatste blokken van 2016 te snel werden gevonden, betekent dit dat hashrate in deze periode toenam; Bitcoin maakt de voorwaarde dan moeilijker door het doel voor de volgende periode te verlagen;
- als de blokken van 2016 te langzaam werden gevonden, betekent dit dat hashrate is afgenomen; Bitcoin verlicht de toestand door het doel te verhogen.



De formule is als volgt:



```txt
Tn = To * (Ta / Tt)
```



Met:




- `tn`: nieuw doel
- `naar`: oud doel
- `Ta`: verstreken echte tijd voor de laatste 2016 blokken
- `Tt`: doeltijd (in seconden)



Met een doeltijd van twee weken, dus `Tt = 1.209.600` seconden:



```txt
Tn = To * (Ta / 1 209 600)
```



Om te begrijpen hoe je de moeilijkheidsgraad van Bitcoin mining kunt aanpassen, is hier een voorbeeld met fictieve waarden:



```txt
Tn = To * (Ta / 1 209 600)
Tn = 18 045 755 102 * (1 000 000 / 1 209 600)
Tn = 14 918 779 020
```


Met:



- `**To = 18.045.755.102**`: Oud doel, d.w.z. de referentiewaarde vóór aanpassing.
- `**ta = 1.000.000 seconden**`: Tijd die daadwerkelijk is besteed aan het produceren van de laatste 2016 blokken. Aangezien deze tijd minder is dan de doeltijd, heeft het netwerk te snel gemined.
- `**1.209.600 seconden**`: Richttijd die overeenkomt met 10 minuten per blok voor blokken van 2016, gebruikt als referentie voor aanpassing.
- `**tn = 14.918.779.020**`: Nieuw doel berekend na [moeilijkheidsaanpassing](https://planb.academy/resources/glossary/difficulty-adjustment).



Hier is de nieuwe doelstelling lager dan de oude, wat betekent dat mining moeilijker wordt om de blokproductie in de volgende periode af te remmen.


*De doelwaarden in dit voorbeeld zijn vereenvoudigd en geschaald voor onderwijsdoeleinden; het werkelijke doel dat in Bitcoin wordt gebruikt is een 256-bits geheel getal van een heel andere orde van grootte.*



Deze berekening wordt lokaal uitgevoerd door elk knooppunt, op basis van de tijdstempels die in de blokken zijn ingevoerd. Omdat alle knooppunten dezelfde regels toepassen, komen ze op hetzelfde resultaat uit en wordt het nieuwe doel de gemeenschappelijke referentie voor de volgende blokken van 2016.



Er is een belangrijk detail om op te merken over deze aanpassing: **Ze is beperkt**. Bitcoin beperkt de variatie in moeilijkheid per periode om te abrupte veranderingen te vermijden die de aanpassing zouden kunnen blokkeren. In feite is de werkelijke tijd waarmee rekening wordt gehouden beperkt om binnen een bereik te blijven dat gelijk is aan een factor 4 (minimaal een kwart van het oude doel, maximaal vier keer het oude doel). Dit voorkomt extreme retargeting als tijdstempels zeer atypisch of gemanipuleerd zijn.



### Doel vertegenwoordiging



In de block header verschijnt het doel niet in zijn volledige 256-bit vorm, omdat dit te veel ruimte in beslag zou nemen. In plaats daarvan codeert het 32-bits `nBits` veld het doel in een compact formaat, vergelijkbaar met wetenschappelijke notatie op basis 256: een exponent (1 byte) en een coëfficiënt (3 bytes). Het volledige doel wordt dan gereconstrueerd uit deze twee waarden. We zullen hier niet in detail treden, omdat het onderwerp relatief complex is en niets toevoegt aan het begrip van mining. Onthoud alleen dat het doel niet in ruwe vorm wordt opgeslagen in de block header, maar in compacte vorm.



Met dit laatste hoofdstuk van Deel I, hebben we een rondleiding genomen van hoe proof-of-work werkt in Bitcoin: de miner bouwt een kandidaatblok door transacties te selecteren uit zijn mempool, berekent de kandidaatblokkop, hasht deze, vergelijkt de resulterende hash met het periodedoel en begint dan opnieuw door de nonce te wijzigen totdat een geldige hash is verkregen. Tot slot berekent het netwerk elke 2016 blokken een nieuw doel om een gemiddelde tijd van ongeveer 10 minuten per blok te handhaven, ondanks de constante variaties in hashrate.




# Het Bitcoin mining stimuleringssysteem


<partId>27fb10c1-d53b-4dc2-90fa-3cb0309b74c1</partId>



## Block reward


<chapterId>b316fb89-9c18-417e-917b-ab98f1722646</chapterId>



Zoals je je kunt voorstellen, is Bitcoin mining geen altruïstische activiteit. Miner's hebben echte kosten: elektriciteit om hun mining computers te laten werken, de aankoop van gespecialiseerde apparatuur, lonen voor onderhoud, soms gebouwen en koelsystemen. Om het Bitcoin systeem te laten werken, moeten de privébelangen van de mijnwerkers afgestemd zijn op de collectieve belangen van het netwerk. Dit is precies de rol van de mining beloning. Het moedigt miners aan om in proof of work te investeren, geldige transacties op te nemen en de regels van het protocol te respecteren in plaats van te proberen het te corrumperen.



Deze logica is gebaseerd op speltheorie: het protocol maakt eerlijkheid rationeel. Een miner verdient geld als hij een geldig blok produceert dat door de nodes wordt geaccepteerd. Omgekeerd, als hij probeert vals te spelen, wordt zijn blok door de knooppunten afgekeurd en krijgt hij niets. Aangezien het produceren van een blok kosten met zich meebrengt, betekent een afgekeurd blok een direct verlies. In een competitieve omgeving waar duizenden spelers tegelijkertijd op zoek zijn naar een geldig blok, is de meest winstgevende strategie daarom meestal om de regels strikt te volgen en je inkomen eerlijk te maximaliseren.



Om dit te bereiken, bepaalt het Bitcoin protocol dat de miner die een geldig blok vindt, het recht wint om er een bepaalde transactie in op te nemen, waardoor de miner een bepaalde som BTC krijgt. Dit staat bekend als **[blokbeloning](https://planb.academy/resources/glossary/block-reward)**. In dit eerste hoofdstuk is het de bedoeling om te begrijpen waaruit het bestaat en hoe het wordt bepaald. Later zullen we zien hoe het geldscheppingsgedeelte in de loop van de tijd evolueert (met halvings) en hoe het eigenlijk technisch wordt geïnd (via de coinbase transactie).



### Waaruit bestaat de blokbeloning?



In de vorige hoofdstukken zagen we hoe mijners erin slagen een geldig blok te vinden. Zodra een miner een header heeft gevonden waarvan de hash kleiner is dan het doel, wordt zijn kandidaatblok als geldig beschouwd. Hij kan het dan verdelen over het hele Bitcoin netwerk. Het blok wordt toegevoegd aan de rest van de blockchain en bevestigt de transacties die het bevat.



Het is precies deze gebeurtenis (de eigenlijke toevoeging van het blok aan de blockchain) die aanleiding geeft tot het geven van een beloning aan de winnende miner. Deze beloning bestaat uit twee verschillende elementen die bij elkaar opgeteld worden:




- [bloksubsidie](https://planb.academy/resources/glossary/block-subsidy)**;
- transactiekosten**.



![Image](assets/fr/024.webp)



Laten we eens kijken waar deze twee delen van de beloning mee overeenkomen.



### Groepssubsidie



De bloksubsidie komt overeen met het monetaire creatiegedeelte van de beloning. Als een miner een geldig blok produceert, geeft het protocol hem toestemming om een bepaald aantal nieuwe bitcoins te creëren en deze als beloning aan zichzelf toe te wijzen. Deze bitcoins worden ex nihilo gecreëerd. Ze bestonden niet eerder.



De hoeveelheid nieuw gecreëerde bitcoins is echter geenszins willekeurig. Het is strikt gedefinieerd door de Bitcoin protocolregels en is identiek voor alle miners. We zullen dit mechanisme nader bekijken in het volgende hoofdstuk, omdat de subsidie niet voor onbepaalde tijd een vaste waarde is: het wordt periodiek verdeeld volgens een nauwkeurig schema. Voor nu, onthoud gewoon dat:




- de bloksubsidie is een van de twee componenten van de blokbeloning;
- het wordt afgetopt en bepaald door het protocol, niet door de miner (hoewel de miner technisch gezien minder dan het maximumbedrag kan aanvragen);
- het creëert bitcoins uit het niets.



Deze subsidie speelt twee belangrijke rollen binnen het Bitcoin protocol. De eerste is spelers aanmoedigen om deel te nemen aan mining. In de beginjaren van Bitcoin (en soms nog steeds) waren de transactiekosten erg laag. De subsidie garandeerde daarom voldoende compensatie om miners aan te trekken en een veiligheidsniveau voor het systeem te handhaven.



De tweede rol heeft te maken met de distributie van valuta. Elke nieuwe munteenheid wordt geconfronteerd met de vraag hoe de munteenheden eerlijk verdeeld kunnen worden onder de bevolking. De bloksubsidie biedt een antwoord op dit probleem. Door bitcoins te creëren via mining, maakt het hun initiële distributie op een open en neutrale manier mogelijk: iedereen kan ze verkrijgen, op voorwaarde dat ze deelnemen aan mining, zonder voorafgaande toestemming of identificatie.



Aan de andere kant, omdat deze bitcoins uit het niets worden gecreëerd, is hun waarde niet zonder basis. Door de hoeveelheid geld in omloop te verhogen, verwatert de subsidie mechanisch de waarde van bestaande bitcoins. Het introduceert dus een vorm van monetaire inflatie. In het volgende hoofdstuk zullen we echter zien dat deze subsidie geleidelijk zal verdwijnen en dat de inflatie uiteindelijk zal ophouden.



![Image](assets/fr/025.webp)



### Transactiekosten



De tweede component van de blokbeloning is gekoppeld aan het systeemgebruik: wanneer een gebruiker een transactie plaatst, wil hij dat deze bevestigd wordt. De blokruimte is echter beperkt en blokken verschijnen gemiddeld slechts om de 10 minuten of zo. Blokruimte is dus een schaars goed. Als de vraag groter is dan het aanbod, stijgt de prijs: dit is de markt voor transactievergoedingen. Elke miner die erin slaagt om een geldig blok te produceren, krijgt het recht om voor eigen rekening de volledige transactiekosten te innen die verbonden zijn aan alle transacties die hij in zijn blok heeft opgenomen.



Je kunt het zien als een veilingsysteem: elke transactie stelt een bedrag voor, en miners geven voorrang aan de transacties die hun inkomsten maximaliseren, onder ruimtebeperkingen. Dit mechanisme brengt de belangen op een natuurlijke manier op één lijn:




- gebruikers met haast betalen meer om snel te worden opgenomen;
- miners worden aangemoedigd om transacties op te nemen die de hoogste vergoedingen voor blokruimte betalen.
- het netwerk spam voorkomt, omdat het publiceren van een transactie kosten met zich meebrengt.



#### Hoe worden transactiekosten berekend?



In tegenstelling tot wat vaak wordt gedacht, zijn vergoedingen geen output in een Bitcoin transactie. In feite geeft een transactie inputs uit en creëert outputs. Inputs vertegenwoordigen de bron van de gebruikte bitcoins, terwijl outputs de bestemming van de betalingen vertegenwoordigen. Transactievergoedingen zijn simpelweg **het verschil tussen de totale inputs en de totale outputs**.



Met andere woorden, de bitcoin-input van de gebruiker, die van hem is, creëert output voor de ontvangers, maar reproduceert niet het volledige bedrag dat door de input is verbruikt. Het verschil tussen de twee vertegenwoordigt de transactiekosten die de miner kan innen.



Laten we een voorbeeld nemen. Een transactie verbruikt twee inputs, één van `100.000 sats` en de andere van `150.000 sats`, en creëert drie outputs van `35.000 sats`, `42.000 sats` en `170.000 sats`.



![Image](assets/fr/027.webp)



De som van de inputs is dus `250.000 sats`, terwijl de som van de outputs `247.000 sats` is. Dit betekent dat `3.000 sats` is verbruikt aan inputs zonder te worden gerecreëerd aan outputs: dit bedrag komt overeen met de vergoedingen die deze transactie voorstelt.



![Image](assets/fr/028.webp)



Als een miner deze transactie in een geldig blok opneemt, heeft hij het recht om deze `3.000 sats` te innen, naast de vergoedingen van alle andere transacties die in het blok zijn opgenomen. Er is echter geen direct on-chain verband tussen de transactie die de vergoeding betaalt en de sats die daadwerkelijk door de miner wordt geïnd. Technisch gezien worden de `3.000 sats` aan vergoedingen vernietigd, en in ruil daarvoor krijgt de miner het recht om hetzelfde bedrag opnieuw voor zichzelf te creëren.



#### De kostenratio



Een blok wordt niet beperkt door het aantal transacties, maar door de totale capaciteit (tegenwoordig, in de praktijk, door het gewicht van het blok). Sommige transacties nemen meer ruimte in dan andere: een transactie met veel inputs en outputs zal groter zijn dan een eenvoudige transactie met één input en twee outputs. De gebruikte scripts hebben ook invloed op de grootte.



![Image](assets/fr/026.webp)



Twee transacties kunnen daarom in absolute zin hetzelfde bedrag aan vergoedingen betalen, maar economisch gezien niet gelijkwaardig zijn vanuit het oogpunt van de mijnwerker. Als de ene twee keer zo groot is, kost het twee keer zoveel ruimte in het blok. Ruimte is schaars, dus de miner probeert zijn inkomsten per eenheid ruimte te maximaliseren.



Daarom drukken we in de praktijk het concurrentievermogen van een transactie uit met een vergoedingsratio, meestal in `sats/vB` ([satoshis](https://planb.academy/resources/glossary/satoshi-sat) per virtuele byte). Het berekenen van deze verhouding is eenvoudig:



```text
fee rate = fee / weight (in vB)
```



Als we bijvoorbeeld een transactie hebben met een gewicht van `141 vB` en een toewijzing van `1.974 sats` aan vergoedingen, dan zal deze een tarief van `14 sats/vB` hebben.



```text
1 974 / 141 ≈ 14 sats/vB
```



Deze verhouding verklaart de economische keuzes die mijnwerkers maken: bij een vaste capaciteit maximaliseert het opnemen van transacties met een hoge prijs de totale vergoedingen van het blok, en dus de vergoeding van de mijnwerker. Het verklaart ook waarom transacties met lage kosten lang in de wachtrij in mempools blijven staan: ze concurreren met andere transacties die meer betalen per eenheid ruimte.



### Netwerkbeveiliging tegen spam



Vergoedingen dienen ook een operationeel veiligheidsdoel: ze brengen kosten met zich mee voor het vermenigvuldigen van transacties. Als het publiceren van een transactie gratis zou zijn, zou het gemakkelijk zijn om het netwerk te overspoelen met nutteloze transacties en mempools te verzadigen, waardoor de belasting op knooppunten toeneemt.



In de praktijk passen knooppunten een lokaal doorgeefbeleid toe (mempool regels) en stellen vaak een minimumtariefdrempel in waaronder ze een transactie niet doorgeven (standaard `0.1 sat/vB` in Bitcoin Core via `minRelayTxFee`). Een transactie kan geldig zijn in de strikte zin van de consensusregels, maar wordt door de meeste knooppunten niet doorgegeven als de vergoedingen te laag zijn. Als gevolg daarvan circuleert het niet, bereikt het de miners niet en heeft het weinig kans om bevestigd te worden.



Op dit punt heb je de essentie van de blokbeloning: het komt overeen met de compensatie voor de winnende miner en bestaat uit twee verschillende elementen. Aan de ene kant een bloksubsidie, gedefinieerd door de protocolregels, die ex nihilo nieuwe bitcoins creëert. En aan de andere kant de vergoedingen voor transacties die zijn opgenomen in het gemijnde blok.



In het volgende hoofdstuk gaan we dieper in op de bloksubsidie, om precies te begrijpen hoe die wordt berekend en hoe die in de loop van de tijd evolueert volgens de regels van het Bitcoin-protocol.



## Halving


<chapterId>7cdca211-7300-48f8-a1e4-53e5c2678cd8</chapterId>



In het vorige hoofdstuk zagen we dat miners die een geldig blok produceren een beloning ontvangen die bestaat uit de vergoedingen voor de transacties in het blok, plus een blokkensubsidie. We hebben echter nog niet uitgelegd hoe het bedrag van deze subsidie wordt bepaald. Het mechanisme dat deze waarde bepaalt en evolueert staat bekend als ***[halving](https://planb.academy/resources/glossary/halving)***.



### Wat is halveren?



Halving is een gebeurtenis die in het Bitcoin protocol is geprogrammeerd en die de bloksubsidie halveert, dat wil zeggen de maximale hoeveelheid nieuwe bitcoins die de winnende miner bij elk blok mag creëren. Het heeft geen invloed op transactiekosten: deze kosten bestaan onafhankelijk en blijven bepaald door gebruikersactiviteit en concurrentie voor blokruimte.



Toen Bitcoin in 2009 werd gelanceerd, werd de bloksubsidie vastgesteld op 50 BTC voor elk gedolven blok. Sindsdien is deze subsidie verschillende keren gehalveerd.



![Image](assets/fr/029.webp)



Halving wordt niet getriggerd door een datum, maar door blokhoogte. Het wordt elke 210.000 blokken** uitgevoerd. Aangezien Bitcoin mikt op een gemiddeld interval van ongeveer 10 minuten per blok, komen 210.000 blokken overeen met ruwweg vier jaar.



```cpp
CAmount GetBlockSubsidy(int nHeight, const Consensus::Params& consensusParams)
{
int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;
// Force block reward to zero when right shift is undefined.
if (halvings >= 64)
return 0;

CAmount nSubsidy = 50 * COIN;
// Subsidy is cut in half every 210,000 blocks which will occur approximately every 4 years.
nSubsidy >>= halvings;
return nSubsidy;
}
```



Dus, als we `n` het aantal halvingen noteren dat al heeft plaatsgevonden, kan de bloksubsidie in BTC als volgt worden berekend:



```text
subsidy(n) = 50 / 2^n
```



### Halvingen verleden tijd



Hier is een overzichtstabel van halvingen die al hebben plaatsgevonden, met hun blokhoogte, datum en de nieuwe bloksubsidie die van toepassing is na de gebeurtenis:



| Event               |   Height  | Date                        | Subsidy    |
| ------------------- | --------: | --------------------------- | ---------: |
| Halving 1           |   210 000 | 28 novembre 2012            |     25 BTC |
| Halving 2           |   420 000 | 9 july 2016                 |   12,5 BTC |
| Halving 3           |   630 000 | 11 may 2020                 |   6,25 BTC |
| Halving 4           |   840 000 | 20 april 2024               |  3,125 BTC |
| Halving 5 (upcoming) | 1 050 000 | Spring   2028 (estimation) | 1,5625 BTC |

### Wanneer en hoe eindigt de subsidie?



Halving wordt herhaald zolang de subsidie kan worden uitgedrukt in de minimumeenheid van het systeem: satoshi.



```text
1 BTC = 100 000 000 sats
```



Als de subsidie wordt gehalveerd, bereiken we uiteindelijk fracties van een bitcoin die zo klein zijn dat ze minder dan 1 satoshi worden. Op dit punt is het niet langer mogelijk om een halve eenheid satoshi te creëren. De creatie van geld via de blokkensubsidie stopt en miners worden alleen nog gecompenseerd op basis van transactiekosten. Vanaf dit punt zijn alle bitcoins in omloop en is het niet langer mogelijk om nieuwe eenheden te produceren.



Het definitieve einde van de bloksubsidies komt op blokniveau 6.930.000, dat wil zeggen bij de 33e en laatste halvering. Deze gebeurtenis zal naar verwachting rond het jaar 2140 plaatsvinden, hoewel het onmogelijk is om een exacte datum te geven, omdat het zal afhangen van de werkelijke snelheid waarmee blokken worden gevonden tussen nu en dan.



Aangezien de bloksubsidie een geometrische opeenvolging volgt met een ratio van 1/2 bij elke halvering, was de geldcreatie extreem hoog in de begindagen van Bitcoin, om daarna zeer snel af te nemen. Bij de 7e halvering zal al meer dan 99% van de bitcoins in omloop zijn gebracht. De drempel van 99% zal naar verwachting worden overschreden tussen 2032 en 2036. Dit betekent dat het dan meer dan 100 jaar zal duren om de laatste resterende 1% bitcoins te delven. Terwijl de monetaire inflatie erg hoog was toen Bitcoin werd gelanceerd, om wijdverspreide distributie van de valuta mogelijk te maken, is het nu erg laag en zal het blijven dalen, totdat het het niveau bereikt van een echte harde valuta, waarvan de circulerende voorraad niet meer kan toenemen.



![Image](assets/fr/030.webp)



### Waarom zullen er nooit 21 miljoen BTC's zijn?



De maximale geldvoorraad van Bitcoin wordt vaak voorgesteld als 21 miljoen BTC. Dit is een goede benadering om het monetaire beleid te begrijpen, maar strikt technisch gezien zal de totale voorraad nooit precies 21.000.000 bitcoins bereiken.



De belangrijkste reden is mechanisch. Door opeenvolgende halvingen valt de bloksubsidie uiteindelijk onder de minimumwaarde van 1 sat, waardoor de uitgifte eindigt voordat het exacte theoretische totaal wordt bereikt. Als gevolg van deze minimale granulariteit en de afrondingsregels is het totale aantal bitcoins dat door de subsidie is gecreëerd iets minder dan 21 miljoen.



Daarnaast kunnen marginale protocolgerelateerde afwijkingen hier ook aan bijdragen. In zeldzame gevallen kan het bijvoorbeeld voorkomen dat sommige miners niet hun volledige subsidie hebben geclaimd, waardoor de hoeveelheid Bitcoins die daadwerkelijk zijn uitgegeven definitief afneemt. We kunnen ook het [genesisblok](https://planb.academy/resources/glossary/genesis-block) noemen, geproduceerd door Satoshi op 3 januari 2009, waarvan de gecreëerde bitcoins geen deel uitmaken van [UTXO set](https://planb.academy/resources/glossary/utxo-set), evenals bepaalde historische gebeurtenissen die zijn gekoppeld aan bugs, zoals dubbele coinbase transactie-identifiers.



Tot slot moeten we ook rekening houden met alle bitcoins die vernietigd of geblokkeerd zijn:




- bitcoins opgesloten in onoplosbare scripts;
- die opzettelijk zijn vernietigd door `OP_RETURN` scripts;
- of verlies van privésleutels op applicatieniveau.



In theorie is de voorraad Bitcoin daarom beperkt tot 21 miljoen. In de praktijk zullen er echter nooit 21 miljoen bitcoins in omloop zijn.



## De coinbase transactie


<chapterId>69476700-3616-4aab-b006-367aba059de9</chapterId>



In de vorige hoofdstukken presenteerden we twee belangrijke punten. Ten eerste ontvangt de miner die erin slaagt een geldig blok te produceren en te distribueren een beloning. Aan de andere kant zagen we dat deze beloning bestaat uit twee verschillende elementen:




- een bloksubsidie (bitcoins die ex nihilo worden aangemaakt, waarvan de maximale hoeveelheid wordt ingesteld door het protocol en geleidelijk wordt afgebouwd via halvings);
- alle transactiekosten die betaald zijn door gebruikers van wie de transacties in het blok zijn opgenomen.



Er blijft echter één vraag over: via welk mechanisme int de miner deze beloning in Bitcoin? Dit is precies de rol van een bepaalde transactie die een "coinbase" wordt genoemd.



### Hoe de coinbase transactie werkt



Zoals we in het eerste deel van de cursus zagen, bevat elk Bitcoin blok een lijst van transacties die het zal bevestigen. De allereerste is altijd de [coinbase transactie](https://planb.academy/resources/glossary/coinbase-transaction). Hiermee kan de winnende miner zijn beloning ontvangen.



![Image](assets/fr/031.webp)



Op het eerste gezicht lijkt het een klassieke Bitcoin transactie: het heeft een [TXID](https://planb.academy/resources/glossary/txid-transaction-identifier), output en is opgenomen in de Merkle tree van het blok. Ze verschilt echter in één belangrijk opzicht: ze geeft geen bestaande UTXO uit.



In een klassieke Bitcoin transactie verwijzen `inputs` naar eerdere, nog niet uitgegeven outputs (UTXOs), die de inputwaarde leveren. Uitgangen herverdelen deze waarde vervolgens naar nieuwe UTXO's, met nieuwe bestedingsvoorwaarden. Met andere woorden, om bitcoins te versturen, moet je ze al bezitten. De coinbase transactie daarentegen verbruikt geen bitcoins als input: het creëert bitcoins als output direct vanuit het niets.



Het is precies dit mechanisme dat het mogelijk maakt om nieuwe bitcoins in omloop te brengen via de bloksubsidie, en dat de miner crediteert met de vergoedingen voor de transacties in het blok. De coinbase transactie kan niet verwijzen naar een echt bestaand UTXO (in feite verwijst het naar een fictief UTXO), omdat het juist zijn rol is om een deel van de waarde (de subsidie) te creëren en het andere deel (de vergoedingen) terug te krijgen, zonder deze te ontvangen van een eerdere transactie. Om het hele systeem consistent te houden, moet het deel dat overeenkomt met de vergoedingen precies gelijk zijn aan de som van de bitcoins die zijn verbruikt als inputs, maar niet zijn gerecreëerd als outputs in de andere transacties van het blok.



![Image](assets/fr/032.webp)



Deze transactie is niet optioneel. Een blok dat geen coinbase transactie bevat is ongeldig en wordt systematisch geweigerd door netwerkknooppunten.



⚠️ Let op: de term "*coinbase*" heeft geen verband met het gelijknamige exchange platform. In Bitcoin verwijst "*coinbase*" historisch naar de transactie die de blokbeloning creëert. Het bedrijf heeft deze term gewoon overgenomen voor zijn naam.



De coinbase transactie vervult eigenlijk meerdere rollen tegelijkertijd:




- De eerste is degene die we zojuist hebben beschreven: het wijst de miner de beloning toe waar hij recht op heeft voor het produceren van een geldig blok.
- De tweede, meer technische, rol is het verankeren van de cryptografische verbintenis met de getuigen (handtekeningen) van de SegWit transacties die in het blok zitten.
- Een derde rol, deze keer niet direct protocolgerelateerd, maar verbonden met de moderne industrialisatie van mining, is dat de coinbase nu vaak gebruikt wordt om willekeurige technische gegevens te verankeren. Deze gegevens zijn meestal gekoppeld aan de werking van mining pools en hun interne organisatie.



Om je te helpen deze verschillende toepassingen te begrijpen, zullen we nu de structuur van de coinbase transactie nader bekijken.



### De basisstructuur van de coinbase transactie



Een coinbase transactie moet precies één input bevatten. Voor het gemak zeggen we soms dat het geen input heeft, omdat deze input geen echte UTXO uitgeeft. In werkelijkheid is er wel een input met een gerefereerde bron, maar deze wijst bewust naar een niet-bestaande UTXO.



Zoals we al gezien hebben, moet elke Bitcoin transactie UTXO's als invoer gebruiken om geldige uitgangen te creëren. In de Bitcoin transactie neemt deze consumptie de vorm aan van het verwijzen naar een bestaande UTXO als invoer. Dit verwijzen gebeurt eenvoudigweg door de identifier van de vorige transactie aan te geven (die waarin de UTXO werd gecreëerd), evenals de index ervan bij de uitgangen van deze transactie. Concreet wordt een UTXO gedefinieerd door een hash (de vorige TXID) en een index.



Maar in het geval van de coinbase transactie, in plaats van te verwijzen naar een echte bestaande UTXO, moet de input noodzakelijkerwijs verwijzen naar deze specifieke nep UTXO, met een TXID vol nullen, die niet overeenkomt met een echte TXID:



```text
0000000000000000000000000000000000000000000000000000000000000000
```


Direct gevolgd door de valse index:


```text
0xffffffff
```


![Image](assets/fr/033.webp)



In het basisprotocol van Bitcoin, zoals beschreven in Satoshi Nakamoto, is deze valse invoer de enige beperking die wordt opgelegd aan de coinbase transactie.



Zoals elke UTXO waarnaar verwezen wordt in de invoer van een transactie, is het geassocieerd met een `scriptSig` veld. In een conventionele transactie bevat dit `scriptSig` veld de elementen die nodig zijn om te voldoen aan de `scriptPubKey` en dus de uitgegeven UTXO te ontgrendelen. Maar in het specifieke geval van coinbase, omdat de UTXO waarnaar verwezen wordt opzettelijk fictief is, is het `scriptSig`-veld volledig vrij. Miner's kunnen dus alle gegevens invoeren die ze maar willen. We zullen later bekijken hoe deze vrijheid wordt gebruikt.


Naast deze valse invoer, zijn er een of meer perfect standaard uitgangen, die de miner in staat stellen de bitcoins van de beloning op te halen op een van hun Bitcoin adressen. Deze uitgangen zijn UTXO's die vergrendeld zijn door een `scriptPubKey` (bijvoorbeeld een script dat wijst naar een adres dat gecontroleerd wordt door de miner of de pool). De enige bijzonderheid hier ligt in de regel voor het berekenen van hun waarde: de totale som van de outputs van de coinbase mag nooit hoger zijn dan de maximaal toegestane subsidie, waarbij de block fees worden opgeteld.



Historisch gezien komt de coinbase transactie neer op dit eenvoudige schema: een valse input die verwijst naar een niet-bestaande UTXO, en één of meer outputs die ontworpen zijn om de block reward te verdelen onder de winnende miner. Vandaag de dag is de coinbase echter niet langer beperkt tot deze distributierol. Zijn speciale positie in het blok en de grote flexibiliteit van zijn structuur hebben geleid tot nieuwe toepassingen, zowel in het protocol zelf als in mining poolbeheermechanismen.



### Andere coinbase toepassingen



In de loop der tijd is de coinbase transactie een bijzonder handig invoegpunt geworden voor het integreren van een verscheidenheid aan informatie die nuttig is voor mining en voor de blokstructuur zelf. Laten we ze eens bekijken om de algemene organisatie van coinbase beter te begrijpen.



#### De BIP-34



[BIP-34](https://planb.academy/resources/glossary/bip0034) is een fork soft die in maart 2013 werd ingezet, beginnend met blok 227.930, dat versie 2 van Bitcoin blokken introduceerde. Deze nieuwe versie vereist dat elk blok, in de `scriptSig` van de coinbase transactie, de hoogte van het blok dat wordt aangemaakt bevat.



Enerzijds verduidelijkt deze evolutie de manier waarop het netwerk instemt met de evolutie van de blokstructuur en de consensusregels. Ten tweede verzekert het de uniciteit van elk blok en elke coinbase transactie.



Het `scriptSig` van coinbase is dus niet helemaal vrij. Sinds de activering van BIP-34, is het gewoon beperkt om te beginnen met de hoogte van het blok waarin deze coinbase transactie is opgenomen.



![Image](assets/fr/035.webp)



#### De extra-nonce



Zoals we in de eerste hoofdstukken van deze cursus zagen, heeft de miner een 32-bits nonce veld in de block header, dat hij met vallen en opstaan aanpast om een hash te vinden die kleiner of gelijk is aan het doel. Deze 32-bits ruimte maakt het al mogelijk om een zeer groot aantal combinaties te onderzoeken, maar wanneer de mining moeilijkheidsgraad hoog is, kan dit bereik volledig uitgeput raken in een relatief korte tijd en dus geen enkele combinatie opleveren die een geldige hash produceert. Als alle mogelijke waarden van de `nonce` zonder succes getest zijn, moet de miner een ander element wijzigen om de block header te veranderen en een nieuwe reeks pogingen beginnen.



Aangezien de coinbase-transactie een vrij veld biedt via de `scriptSig` van zijn invoer, is de oplossing die wordt gebruikt om de ruimte van de nonce uit te breiden het exploiteren van een deel van deze `scriptSig`. Dit wordt over het algemeen de extra-nonce genoemd. Door de extra-nonce te wijzigen, wijzigt de miner de `scriptSig` van coinbase, dat wil zeggen de transactie-identifier, vervolgens de Merkle root van het blok en ten slotte de block header zelf. Op deze manier krijgen ze een nieuwe zoekruimte van hashes om te onderzoeken, zonder dat ze de andere componenten van hun kandidaatblok hoeven te wijzigen.



![Image](assets/fr/036.webp)



#### Het identificeren van pools en miners



Tegenwoordig is een zeer groot deel van de hashrate van de wereld georganiseerd in mining pools. Deze structuren brengen individuele mijnwerkers samen om hun werk te combineren en de variatie in hun inkomen te verminderen.



Om operationele redenen gebruiken mining pools ook het vrije veld van de `scriptSig` van de coinbase input om verschillende stukjes informatie in te voegen. Deze variëren van pool tot pool en van netwerkprotocol tot netwerkprotocol, maar omvatten over het algemeen een unieke identifier (vaak een extra nonce gestructureerd in verschillende subdelen) toegewezen aan elke miner, om dubbel werk binnen de pool te voorkomen. Een poolidentificatietag wordt meestal toegevoegd, gebruikt voor publieke toewijzing van gevonden blokken, mining statistieken en andere traceringsdoeleinden.



![Image](assets/fr/037.webp)



#### Toezegging van SegWit



Sinds de SegWit zachte fork in 2017 werd ingeschakeld, zijn de getuigegegevens (d.w.z. over het algemeen handtekeningen) gescheiden van de transactiestamgegevens, met name om het probleem van de [vervormbaarheid van Bitcoin transacties](https://planb.academy/resources/glossary/malleability-transaction) te corrigeren. Deze scheiding introduceert daarom een nieuw element dat in het blok moet worden vastgelegd.



Om dit te doen, worden de getuigen gegroepeerd in een andere speciale Merkle-boom, waarvan de root vervolgens wordt gecommit in de coinbase transactie via een `OP_RETURN` uitvoer.



![Image](assets/fr/038.webp)



Ik zal in deze cursus niet dieper ingaan op dit mechanisme, omdat het buiten het bestek van dit artikel valt, maar onthoud gewoon dat sinds de introductie van SegWit, de coinbase transactie dient als vehikel om in het blok een vingerafdruk te verankeren die alle SegWit getuigen samenvat. De getuigen worden in een onafhankelijke Merkle tree geplaatst, de root van deze tree wordt geschreven naar een output van de coinbase transactie, en deze coinbase transactie wordt zelf opgenomen in de hoofd Merkle tree, samen met alle andere transacties, waarvan de root verschijnt in de block header. Op deze manier worden de getuigen, die apart van de hoofd transactiegegevens worden opgeslagen, nog steeds gecommit in de block header.



![Image](assets/fr/039.webp)



#### Willekeurige berichten



Omdat de `scriptSig` vrije invoeging van willekeurige informatie toelaat, gekozen door de mijnwerker, hebben sommigen gebruik gemaakt van de mogelijkheid om berichten van meer persoonlijke aard toe te voegen, in plaats van technische. Het beroemdste geval is natuurlijk Satoshi Nakamoto, met zijn nu iconische boodschap:



> The Times 03/Jan/2009 Kanselier op rand van tweede reddingsoperatie voor banken

Dit bericht, dat aanwezig is in het Genesis blok (het allereerste blok van Bitcoin), is feitelijk hexadecimaal gecodeerd in het `scriptSig` van de coinbase transactie:



```text
5468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73
```


![Image](assets/fr/034.webp)



### De looptijd


Zodra het blok gemined en gedistribueerd is, verschijnt de coinbase transactie op de blockchain zoals elke andere transactie. Het creëert UTXO's voor de winnende miner, zodat hij zijn beloning kan innen. Deze UTXO's zijn echter niet onmiddellijk besteedbaar: ze zijn onderhevig aan een [looptijd](https://planb.academy/resources/glossary/maturity-period). Deze looptijd is vastgesteld op 100 blokken na het blok dat de coinbase bevat. Concreet moet de coinbase transactie dus 101 bevestigingen hebben om door de winnende miner uitgegeven te kunnen worden.


![Image](assets/fr/040.webp)


Het doel van deze regel is om de impact van ketenreorganisaties op de economie te beperken. Zoals we in vorige hoofdstukken hebben gezien, kan het gebeuren dat op dezelfde hoogte twee verschillende geldige blokken bijna gelijktijdig door verschillende miners worden gevonden. Voor een kort moment kan het netwerk splitsen: sommige nodes ontvangen eerst blok A, terwijl andere eerst blok B zien. Dan, in de loop van de volgende blokken, verzamelt één van de twee takken meer werk en wordt de referentietak. De andere tak wordt verlaten en zijn blokken worden verouderd. De transacties die het bevatte kunnen dan, in theorie, terugkeren naar de mempools in afwachting van bevestiging.



In de praktijk gebeurt dit zelden, omdat de fee-markt er vaak toe leidt dat bijna dezelfde transacties in twee concurrerende blokken op dezelfde hoogte verschijnen. Dit is een van de redenen waarom een Bitcoin transactie meestal als onveranderlijk wordt beschouwd na zes bevestigingen: reorganisaties van meer dan zes blokken zijn zo onwaarschijnlijk dat ze redelijkerwijs als onmogelijk kunnen worden beschouwd.



![Image](assets/fr/041.webp)



Het probleem met deze reorganisaties in het geval van de coinbase-transactie is dat het geen gewone transactie is. Er worden gloednieuwe bitcoins in omloop gebracht. Als de blokbeloning onmiddellijk zou kunnen worden uitgegeven, zou er een problematische cascadesituatie kunnen ontstaan:




- een miner geeft bitcoins uit vanuit een coinbase,
- deze bitcoins circuleren in de economie,
- toen werd het oorspronkelijke blok uiteindelijk verlaten tijdens een reorganisatie.



De bitcoins in omloop zouden dan nooit hebben bestaan in de uiteindelijke keten, en een reeks transacties die geldig waren op het moment van uitgifte zouden a posteriori ongeldig worden.



De looptijd legt een tijdsbestek op dat lang genoeg is om dit scenario onrealistisch te maken. Een reorganisatie van 101 blokken wordt in de praktijk als onmogelijk beschouwd (ook al blijft er een infinitesimale kans). We weten niet precies waarom Satoshi zo'n hoge waarde voor looptijd heeft gekozen, maar het is waarschijnlijk dat dit is gedaan zodat het mechanisme functioneel zou blijven, zelfs in het geval van grote netwerkstoringen.



Deze regel voorkomt dat nieuw gecreëerd blokbeloningsgeld begint te circuleren voordat het blok dat het generated veilig begraven is onder een grote hoeveelheid geaccumuleerd werk.



---

We zijn nu aan het einde gekomen van onze uitleg over de werking van Bitcoin mining. Je zou nu een duidelijk beeld moeten hebben van de betrokken basismechanismen.



In het laatste deel van de cursus keren we terug naar meer concrete aspecten, om je te laten zien hoe Bitcoin mining in de echte wereld tot stand komt: de industrialisatie, de gebruikte machines, de groepering van spelers, enzovoort. Het doel is om je een algemeen beeld te geven van Bitcoin mining, zowel vanuit het theoretische en protocolaire perspectief dat we net gezien hebben, als vanuit de praktische en operationele kant.



# De Bitcoin mining-industrie


<partId>906a6e18-4718-4a1f-85f5-18854cebdf7c</partId>



## De evolutie van mining machines


<chapterId>2d2f9055-75fd-4630-b493-a577d708a39f</chapterId>



In de begindagen van Bitcoin was mining geen industriële activiteit. Het was onderdeel van de Bitcoin software, gelanceerd op een personal computer, vaak uit nieuwsgierigheid, soms om het netwerk te ondersteunen en in tweede instantie om bitcoins te verkrijgen, die toen vrijwel geen marktwaarde hadden.



In de loop der jaren heeft deze activiteit een transformatie ondergaan: de machines zijn veranderd, de moeilijkheidsgraad is geëxplodeerd en mining is een industrie op zich geworden. Laten we eens kijken naar de operationele aspecten van Bitcoin mining.



### Aan de slag: mining met een CPU



In 2009 en in de beginjaren werd mining voornamelijk uitgevoerd met behulp van de CPU van een conventionele computer. Bitcoin was toen slechts een eenvoudig stuk software, dat dienst deed als wallet, een knooppunt en een mijnwerker. Simpelweg de software van Satoshi Nakamoto starten op je persoonlijke computer was voldoende om deel te nemen aan het mining proces en, in veel gevallen, om blokken te vinden.



Een CPU kan alles, maar is nergens voor geoptimaliseerd. Hij voert zeer algemene instructies uit, met complexe logica. Voor een taak als het herhaaldelijk hashen van block headers is het niet het ideale gereedschap, maar bij het opstarten van een netwerk is de moeilijkheidsgraad zo laag dat het meer dan genoeg is om blokken te vinden.



Deze periode is belangrijk, omdat het ons herinnert aan een belangrijk punt: proof of work is niet afhankelijk van een bepaalde categorie apparatuur. Wat telt is de mogelijkheid om hashes sneller te berekenen dan anderen, tegen een gegeven kostprijs. Zodra een technisch voordeel verschijnt, wordt het automatisch omgezet in een economisch voordeel. Maar in absolute termen is het vandaag de dag nog steeds mogelijk om te proberen Bitcoin blokken te vinden met een conventionele CPU. Dit is bijvoorbeeld de aanpak van het NerdMiner project. De kans om een blok te vinden is vrijwel nihil, maar er is nog steeds een oneindig kleine kans.



https://planb.academy/tutorials/mining/hardware/nerdminer-c9826fd9-c2b4-4d1e-8c78-809122de1654

### Overschakelen naar GPU's



Al snel realiseerden mijnwerkers zich dat de bottleneck niet het vermogen was, maar de mogelijkheid om een enorm aantal gelijksoortige bewerkingen parallel uit te voeren. Dit was precies wat grafische verwerkingseenheden (GPU's) konden doen. Oorspronkelijk was een GPU ontworpen om dezelfde bewerkingen uit te voeren op grote hoeveelheden gegevens. Deze architectuur was perfect geschikt voor een taak als herhaaldelijk hashen: in plaats van een paar zeer veelzijdige kernen, heb je honderden, dan duizenden eenheden die dezelfde instructies tegelijkertijd kunnen uitvoeren.



Met vergelijkbaar stroomverbruik kan een GPU veel meer hashes per seconde produceren dan een CPU. Tegelijkertijd kreeg bitcoin een wisselkoers ten opzichte van de dollar, steeg de waarde ervan en verschenen er ruilplatforms. Vanaf dat moment begon de aard van mining te veranderen. Het ging niet langer alleen om meedoen, maar ook om geld verdienen. Er verschenen dedicated configuraties: machines gebouwd rond verschillende grafische kaarten, soms zonder scherm, met een minimaal systeem en gespecialiseerde software, met als enige doel om te mijnen.



Op dat moment begon de moeilijkheidsgraad van mining te exploderen. Tussen medio 2010 en medio 2011 steeg de moeilijkheidsgraad zelfs met een factor 1000. Mechanisch gezien begint de specialisatie, net als bij de vroege vormen van industrialisatie, en gewone gebruikers - die genoegen nemen met het draaien van de Bitcoin software op hun pc - hebben nu nog maar een heel kleine kans om een geldig blok te vinden.



![Image](assets/fr/044.webp)



*Bron: [CoinWarz.com](https://www.coinwarz.com/mining/bitcoin/hashrate-chart)*



Tussen het GPU tijdperk en het moderne [ASIC](https://planb.academy/resources/glossary/asic) tijdperk was er een tussenfase: het gebruik van FPGA's. Een FPGA is een herprogrammeerbaar component: het kan worden geconfigureerd om direct een logische schakeling te implementeren die is toegewijd aan een bepaalde berekening, in dit geval `SHA256d`. Het idee was om nog verder weg te gaan van de algemene hardware (CPU/GPU) om energiezuiniger te worden. Maar al snel zouden de verbeteringen die virtueel op FPGA's zijn aangebracht fysiek worden toegepast op de chips zelf: dat is de komst van ASIC.



### De komst van ASIC



De laatste fase in de specialisatie van mining hardware was het verschijnen van ASIC's (*Application-Specific Integrated Circuits*). Een ASIC is een chip ontworpen voor een enkele taak. In het geval van Bitcoin mining is deze taak precies het uitvoeren van `SHA256d` op maximale snelheid en met optimale energie-efficiëntie. In tegenstelling tot een GPU wordt een ASIC niet gebruikt voor games, 3D rendering of AI. Het is voor hashing, en dat is alles.



![Image](assets/fr/045.webp)



*ASIC S21 XP vervaardigd door Bitmain*



Deze specialisatie heeft twee belangrijke gevolgen:




- De eerste is een sprong in prestatie en efficiëntie. Voor apparaten van vergelijkbare generatie produceert een ASIC veel meer hashes per seconde dan een GPU, terwijl het minder stroom verbruikt. Mining met een GPU werd al snel niet meer concurrerend: ook al werkte het technisch, de elektriciteitskosten waren in de meeste contexten veel hoger dan de verwachte inkomsten;
- De tweede is een verandering van model: de investering is voornamelijk verschoven naar industriële hardware. Mining houdt nu in dat je machines koopt die voor dit doel ontworpen zijn, ze continu van energie voorziet, ze koelt, onderhoudt en hun veroudering absorbeert. Want een ASIC is economisch niet eeuwigdurend: als er een nieuwe, efficiëntere generatie op de markt komt, worden de oude machines steeds minder rendabel, zelfs als ze blijven functioneren.



Vanaf dat moment hebben we het niet meer alleen over een hobby. We hebben het over een sector waar het concurrentievermogen afhangt van een vergelijking:




- kosten van elektriciteit;
- kosten van apparatuur en afschrijvingen;
- vermogen om op grote schaal te koelen en te werken;
- beschikbaarheid en betrouwbaarheid van de machine;
- snelheid van communicatie;
- enz.



### Mining boerderijen



Een geïsoleerde machine kan mijnen, maar door honderden, later duizenden ASIC's op één locatie te groeperen, delen we de vaste kosten, optimaliseren we de logistiek en komen we dichter bij een gespecialiseerd datacentermodel.



Een [mining farm](https://planb.academy/resources/glossary/mining-farm), in zijn eenvoudigste vorm, is een gebouw (of verzameling containers) gevuld met ASIC's die 24/7 draaien. De uitdaging is nu om stabiele bedrijfsomstandigheden te handhaven:




- grote hoeveelheden goedkope, stabiele elektrische energie leveren;
- warmte beheren om smoren te voorkomen, aangezien de energiedichtheid aanzienlijk is;
- stof filteren, vochtigheid regelen, schoonmaken;
- real-time bewaking van machineprestaties (temperaturen, hardwarefouten, hashrate druppels, enz.).



![Image](assets/fr/043.webp)



*Een van de zeven gebouwen gewijd aan Bitcoin mining op de Rockdale site van Riot Platforms, vlakbij Austin, Texas. Deze is specifiek gewijd aan onderdompeling mining*



Mining wordt nu gedreven door industriële spelers, waarvan sommige beursgenoteerd zijn, die zeer grootschalige boerderijen bouwen en exploiteren. Dit zijn onder andere MARA Holdings (Nasdaq: `MARA`) en Riot Platforms (Nasdaq: `RIOT`).



![Image](assets/fr/042.webp)



Zelfs zonder in te gaan op de details van de winstmodellen, is het belangrijk om te begrijpen waarom mining deze vorm heeft aangenomen. Proof-of-work is een competitief mechanisme: de kans dat je een blok vindt, en dus geld verdient, is evenredig met het aandeel hashrate dat je inzet. Als gevolg daarvan is er een constante druk om de rekenkracht te verhogen, de kosten per rekeneenheid te verlagen en de verliezen te beperken. Als gevolg daarvan worden omgevingen met goedkopere elektriciteit, een klimaat dat bevorderlijk is voor koeling of een overvloedige energie-infrastructuur natuurlijk aantrekkelijker.



Mining Bitcoin is dus geëvolueerd van een activiteit die in de begindagen voor iedereen toegankelijk was, naar een activiteit die gedomineerd wordt door gespecialiseerde apparatuur en professionele operaties. Dit verandert niets aan de regels van het protocol. In theorie kan iedereen mijnen met elke machine. Maar in de praktijk heeft de moeilijkheidsgraad en efficiëntie van ASIC de binnenlandse mining grotendeels onconcurrerend gemaakt in de meeste contexten.



Natuurlijk zijn er nog steeds situaties waarin thuis mining interessant kan zijn, bijvoorbeeld als je profiteert van zeer goedkope elektriciteit, of als je de generated warmte van je mijnwerker gebruikt om je huis in de winter te verwarmen. Maar in elk geval moet je nog steeds een machine kopen die uitgerust is met een ASIC chip. Bovendien, aangezien je mining vermogen extreem klein zal blijven ten opzichte van het Bitcoin netwerk, zul je een manier moeten vinden om de variatie van je inkomen te verminderen: dit is precies de rol van mining pools, die we in het volgende hoofdstuk zullen bespreken.



Als je thuis mining oplossingen met warmteterugwinning wilt onderzoeken, hebben we tutorials over verschillende hulpmiddelen, zowel kant-en-klaar als doe-het-zelf:



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

https://planb.academy/tutorials/mining/hardware/attakai-0d177e6b-e167-4b25-8e38-4ec74213d1fb

## Groeperen in mining-pools


<chapterId>c871bece-eebe-4ef4-9789-d47251f16c8b</chapterId>



Mining Bitcoin brengt lopende en onvermijdelijke kosten met zich mee, waarvan het stroomverbruik van de machine de belangrijkste is. Deze kosten worden onafhankelijk van de resultaten gemaakt, ook al zijn de inkomsten uit mining van nature zeldzaam en willekeurig. De ontdekking van een blok hangt uitsluitend af van het aandeel van de mijnwerker in hashrate, wat de inkomsten des te onvoorspelbaarder maakt naarmate dat aandeel kleiner is. Het is precies dit praktische probleem dat snel leidde tot het wijdverspreide gebruik van [mining pools](https://planb.academy/resources/glossary/pool-mining). In dit laatste hoofdstuk van de MIN 101 cursus geef ik een introductie tot de principes en werking van mining pools in Bitcoin.



### Wat is een mining zwembad?



Een mining pool is een organisatie (vaak een online dienst) die de rekenkracht van vele onafhankelijke miners samenvoegt om de frequentie te verhogen waarmee hun groep blokken vindt. Wanneer de pool een blok vindt, wordt de blokbeloning herverdeeld onder de deelnemers volgens interne poolregels (die behandeld zullen worden in de MIN 201 cursus, aangezien ze te complex zijn voor MIN 101).



Deelnemers aan een mining pool worden dan vaak "[hashers](https://planb.academy/resources/glossary/hasher)" genoemd, in plaats van "miners", omdat ze niet langer al het mining werk uitvoeren, maar alleen de gegevens hashen die hen door de pool worden doorgegeven.



Verwar de mining pool niet met de mining farm. Dit zijn twee verschillende concepten. Zoals we in het vorige hoofdstuk zagen, is een farm een fysieke locatie waar een enkele entiteit meerdere mining machines beheert. Een pool daarentegen is vooral een virtuele groepering: duizenden machines, vaak geografisch verspreid, werken onder een gemeenschappelijke coördinatie. Een farm kan echter wel deelnemen aan een pool, en doet dat ook vaak.



![Image](assets/fr/048.webp)



### Inkomensverschillen verkleinen



Dus waarom lid worden van een pool? Simpelweg omdat het resultaat van mining activiteit probabilistisch is: bij elke hashpoging is er een zeer kleine kans dat deze de moeilijkheidsdoelstelling haalt en dus een geldig blok produceert.



Op de zeer lange termijn zouden je gemiddelde verdiensten evenredig moeten zijn met jouw aandeel in het totale hashrate. Dit principe volgt direct uit de wetten van waarschijnlijkheid: elke hashberekening is een onafhankelijke willekeurige trekking, en door de wet van de grote getallen convergeert de frequentie waarmee je blokken ontdekt wiskundig naar jouw fractie van de totale hashrate van het netwerk. Op de korte tot middellange termijn kunnen je werkelijke verdiensten echter zeer onregelmatig zijn. Deze discrepantie tussen theoretisch gemiddelde en willekeurige realiteit noemen we **variantie** in de wiskunde.



Hier is een eenvoudig voorbeeld om het principe te illustreren:




- Het Bitcoin netwerk produceert gemiddeld 144 blokken per dag (ongeveer één blok per 10 minuten);
- Als je `0,0001 %` van het totale hashrate hebt, is je verwachting `144 × 0,000001`, of `0,000144` blok/dag;
- Met andere woorden, je zou gemiddeld elke `1 / 0,000144` dagen een blok moeten vinden, dus elke 6.944 dagen, of ongeveer 19 jaar.



Maar deze waarde komt alleen overeen met een wiskundige verwachting: de verdeling van ontdekkingstijden volgt een willekeurige wet, dus het is in de praktijk heel goed mogelijk om nooit één blok te ontdekken, zelfs niet over een heel lange periode. Je kunt pech hebben en heel lang niets vinden, terwijl je wel terugkerende kosten betaalt (elektriciteit, onderhoud, afschrijving van apparatuur...).



De mining pool verandert de aard van dit probleem: door hashrates te combineren, vindt de pool vaker blokken. Elke deelnemer stemt er dan mee in om slechts een fractie van elk gevonden blok te ontvangen, maar wel veel vaker. Het is een transformatie van een zeer volatiel, wijd gespreid inkomen naar een regelmatiger inkomen, ten koste van het delen van de beloningen en het betalen van servicekosten.



### Waarom daalt de variantie als je samenvoegt?



Hoe hoger je rekenkracht, hoe hoger de verwachte frequentie van gevonden blokken. Belangrijker is dat hoe frequenter de gebeurtenissen zijn, hoe dichter de waargenomen resultaten het statistische gemiddelde over een bepaalde periode benaderen.



Op solobasis kan een kleinschalige mijnwerker jaren doorbrengen zonder een enkel blok, dan op een dag een grote uitbetaling krijgen en daarna niets. In een pool is dezelfde probabilistische realiteit nog steeds van toepassing, maar het wordt gladgestreken op collectieve schaal: de pool vindt vaker blokken en herverdeling zet deze gebeurtenissen om in regelmatiger uitbetalingen voor elke deelnemer. **De mining pool verkoopt daarom voorspelbaarheid op de mining activiteit**.



### Historische monumenten



Zoals we in het vorige hoofdstuk zagen, kon mining in het begin solo worden gedaan met een conventionele computer, omdat de moeilijkheidsgraad erg laag was. Maar toen hashrate wereldwijd explodeerde (GPU, daarna ASIC), werd solo mining een zeer tijdrovende gok voor de meeste deelnemers.



De eerste pools ontstonden precies als antwoord op deze nieuwe realiteit. Braiins Pool (voorheen Slush Pool / Bitcoin.cz) is de eerste Bitcoin mining pool: het heeft zijn eerste blok gedolven op 16 december 2010. Het succes van deze eerste mining pool was snel, want in slechts een paar dagen veroverde het bijna 3,5% van de wereldwijde hashrate.



![Image](assets/fr/047.webp)



Aan de technische kant werden pools vervolgens gestructureerd rond gespecialiseerde communicatieprotocollen tussen de pool en de miners (bijv. [Stratum](https://planb.academy/resources/glossary/stratum), daarna Stratum V2), om gedistribueerd werk efficiënt te orkestreren. We gaan dieper in op deze concepten in onze MIN 201 training.



### De moderne situatie



Op het moment van schrijven (begin 2026) is de wereldwijde Bitcoin hashrate op een orde van grootte van zetta-hash per seconde (= 1.000 EH/s = 1.000.000.000.000.000 hashes per seconde), en bijna alle gevonden blokken komen uit mining pools.



Hier is een rangschikking, tot nu toe, van de belangrijkste mining pools en hun respectievelijke aandeel in hashrate. Deze ranglijst zal waarschijnlijk veranderen tegen de tijd dat je deze cursus leest. Ga voor actuele gegevens naar [mempool.space](https://mempool.space/graphs/mining/pools).



![Image](assets/fr/046.webp)



| Ranking    | Pool           | Blocks found  | Hashrate share   |
| ---------: | -------------- | ------------: | ---------------: |
|          1 | Foundry USA    |          1297 |           29.57% |
|          2 | AntPool        |           755 |           17.21% |
|          3 | ViaBTC         |           514 |           11.72% |
|          4 | F2Pool         |           467 |           10.65% |
|          5 | SpiderPool     |           349 |            7.96% |
|          6 | MARA Pool      |           229 |            5.22% |
|          7 | SECPOOL        |           197 |            4.49% |
|          8 | Luxor          |           128 |            2.92% |
|          9 | Binance Pool   |           105 |            2.39% |
|         10 | OCEAN          |            78 |            1.78% |
|         11 | SBI Crypto     |            70 |            1.60% |
|         12 | Braiins Pool   |            54 |            1.23% |
|         13 | WhitePool      |            33 |            0.75% |
|         14 | Mining Squared |            26 |            0.59% |
|         15 | BTC.com        |            16 |            0.36% |
|         16 | Poolin         |            14 |            0.32% |
|         17 | ULTIMUSPOOL    |            14 |            0.32% |
|         18 | GDPool         |            12 |            0.27% |
|         19 | Innopolis Tech |            11 |            0.25% |
|         20 | NiceHash       |             8 |            0.18% |
|         21 | RedRock Pool   |             8 |            0.18% |
|         22 | Unknown        |             2 |            0.05% |
|         23 | Public Pool    |             1 |            0.02% |

*Bron [mempool.space](https://mempool.space/graphs/mining/pools), gegevens voor één maand, 16 december 2025 tot 16 januari 2025.*



In een meer gevorderde cursus gaan we dieper in op de interne werking van de pools (aandelen, netwerkprotocollen, betalingsmethodes...), want hier komen de details aan bod die zowel de winstgevendheid van de miner als de mogelijke implicaties voor Bitcoin bepalen.



---

We zijn nu aan het einde gekomen van MIN 101. Bedankt dat je de cursus tot het einde hebt gevolgd. Als je de vaardigheden die je tijdens de cursus hebt opgedaan wilt beoordelen, kun je in het volgende onderdeel een eindexamen doen.



Met de basiskennis die je zojuist hebt opgedaan, kun je nu meer geavanceerde cursussen over mining volgen op Plan ₿ Academy, of het nu gaat om theorie, zoals deze, of meer praktische cursussen, zodat ook jij kunt gaan deelnemen aan Bitcoin mining!



# Laatste deel


<partId>eced8ca1-971d-4a22-9254-dbf8bce15d1b</partId>



## Beoordelingen


<chapterId>dc005a96-f4b4-42be-ab72-d4624c110716</chapterId>


<isCourseReview>true</isCourseReview>

## Eindexamen


<chapterId>959f06cf-fd66-4f29-b7ee-665bfedfea0d</chapterId>


<isCourseExam>true</isCourseExam>

## Conclusie


<chapterId>f16a4e42-c16e-466b-ad16-f42b5360f510</chapterId>


<isCourseConclusion>true</isCourseConclusion>