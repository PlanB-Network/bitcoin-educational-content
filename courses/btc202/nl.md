---
name: Je eerste Bitcoin knooppunt opzetten
goal: Een Bitcoin node begrijpen, installeren, configureren en gebruiken
objectives: 


  - De rol en het doel van een Bitcoin knooppunt begrijpen.
  - De verschillende beschikbare hardware- en softwareoplossingen identificeren.
  - Installeer en configureer een Full node (Bitcoin core).
  - Gebruik de Interface paraplu en voeg nuttige toepassingen toe.
  - Verbind een persoonlijke Wallet met zijn eigen node.
  - Verken geavanceerde instellingen en de beste beveiligingspraktijken.


---
# Word een soevereine bitcoiner



Je bent waarschijnlijk bekend met het adagium "Niet je sleutels, niet je munten", dat zelfbewaarneming van je bitcoins aanmoedigt. Het hebben van je eigen sleutels is inderdaad een essentiële eerste stap, maar het is niet genoeg. Om echte monetaire soevereiniteit te bereiken, moet je ook je eigen Bitcoin node installeren en gebruiken. Deze cursus is ontworpen om je te begeleiden bij deze fundamentele stap in je Bitcoin reis!



BTC 202 is een toegankelijke cursus die is ontworpen om je te leren je eigen Bitcoin knoop te spinnen, zelfs als je geen technisch expert bent. We beginnen met te definiëren wat een Bitcoin knoop is, waar hij voor dient en waarom het absoluut essentieel is om er zelf een te draaien. Daarna begeleid ik je stap voor stap bij het kiezen van je hardware, het installeren van de benodigde software, het aansluiten van je Wallet en het maken van de eerste mogelijke optimalisaties om verder te komen.



Het draaien van een Bitcoin node is niet alleen een optie voor experts, het is een noodzaak. Het is een weerbaarheidstool die elke gebruiker moet begrijpen en implementeren. Deze cursus is je startpunt om een soevereine bitcoiner te worden!




+++




# Inleiding


<partId>fc46ccd7-5d6d-40c3-9e9f-fbbb323c760a</partId>




## Cursusoverzicht


<chapterId>916b1f86-38a4-4ede-bdb7-83841d5a7abe</chapterId>



Welkom bij BTC 202, waar je leert hoe je gemakkelijk en zelfstandig een Bitcoin node kunt installeren, configureren en gebruiken. Maar dat is niet alles: je leert ook meer over de plaats en functie van nodes in het Bitcoin systeem. De cursus wisselt af tussen theoretische uitleg en begeleide hands-on praktijk.



### Deel 1 - Inleiding



In dit eerste deel van de cursus zullen we de basisbegrippen verduidelijken en vervolgens overgaan tot meer precieze definities. Wat is een knooppunt? Wat zijn de verschillen tussen node, Wallet en Miner? Daarna leer je over Bitcoin core en de implementaties van het protocol. Het doel is om dezelfde taal te spreken, verwarring te voorkomen en een solide theoretische basis te leggen.



### Deel 2 - Een soevereine bitcoiner worden



In dit tweede deel leg ik eerst uit waarom het belangrijk is om je eigen Bitcoin node te hebben. Daarna verkennen we de verschillende typen nodes die er zijn (compleet, pruned, SPV...), hoe ze werken en hun technische implicaties.



Daarna geven we een overzicht van de software die beschikbaar is om een Bitcoin node te draaien, inclusief de voor- en nadelen. Tot slot geven we een aantal praktische aanbevelingen voor het kiezen van de juiste hardware voor jouw behoeften en budget.



Deze sectie illustreert daarom het pad van de soevereine bitcoiner: begrijpen waarom het nodig is om een node te draaien, het type node kiezen, op basis van deze keuze de software kiezen en, afhankelijk van de gekozen software, de geschikte hardware bepalen.



### Deel 3 - Eenvoudig een Bitcoin node installeren



Zodra deze voorbereiding klaar is, is het tijd om praktisch aan de slag te gaan met Deel 3 gewijd aan Umbrel: het home cloud OS dat zelf-hosting en de installatie van een Bitcoin en Lightning node vereenvoudigt.



Na een korte introductie tot Umbrel, geven we een gedetailleerde tutorial om je door het installatie- en configuratieproces op je eigen doe-het-zelf machine te leiden. Het doel van dit deel is duidelijk: uw eerste volledig functionele en gesynchroniseerde Bitcoin knooppunt.



### Deel 4 - Uw Wallet aansluiten op uw knooppunt



Nu je een Bitcoin knooppunt hebt opgezet, is het tijd om het te gebruiken! In dit gedeelte leer je hoe je je Wallet beheersoftware (zoals Sparrow wallet) kunt verbinden met je eigen Address indexer (Electrs of Fulcrum), of direct met Bitcoin core, zodat je niet meer afhankelijk bent van publieke servers.



We onderzoeken ook de rol van indexers en de verschillende methoden om verbinding te maken met je node (LAN, Tor, Tailscale, etc.). Tot slot, in het laatste hoofdstuk, bespreken we de meest nuttige toepassingen die beschikbaar zijn op Umbrel voor de alledaagse bitcoiner.



### Deel 5 - Geavanceerde concepten en best practices



In dit laatste deel van BTC 202 is het de bedoeling om je kennis te verdiepen. Eerst kijken we naar de best practices voor uw nieuwe Bitcoin node en hoe u deze op lange termijn kunt onderhouden.



We nemen dan de tijd om wat van de theorie die eerder in de cursus is behandeld door te nemen, waaronder het IBD proces en peer discovery in detail begrijpen, de anatomie van een knooppunt onderzoeken en tenslotte leren we hoe je het `Bitcoin.conf` bestand kunt gebruiken om je instellingen te fine-tunen.



### Deel 6 - Laatste deel



Zoals bij alle Plan ₿ Network cursussen, vind je in het laatste deel een eindexamen om je kennis van Bitcoin knooppunten te testen.



Dus, ben je klaar om je eerste Bitcoin knooppunt aan te zetten? Zet koers naar soevereiniteit!



## Wat is een Bitcoin knooppunt?


<chapterId>0a9fd4e0-94ab-405e-924c-023397393027</chapterId>



Zoals beschreven door de maker, Satoshi Nakamoto, presenteert Bitcoin zichzelf als een peer-to-peer elektronisch geldsysteem. Deze eenvoudige zin, de titel van het witboek, bevat veel aanwijzingen over de aard van Bitcoin:




- Ten eerste beschrijft Satoshi Bitcoin als een "systeem", met andere woorden, een samenhangend geheel van hardware- en softwarecomponenten die samenwerken om een specifieke dienst te verlenen of een specifieke functie uit te voeren;
- Vervolgens legt hij uit dat dit systeem het gebruik van elektronisch geld mogelijk maakt, een vorm van immateriële valuta;
- Tot slot wijst hij erop dat dit systeem niet afhankelijk is van een centrale entiteit: het is "peer-to-peer", wat betekent dat het de gebruikers zelf zijn die het systeem bedienen.



Omdat Bitcoin een systeem is, moet het noodzakelijkerwijs op computers draaien. En, vanwege het peer-to-peer karakter, zijn het de gebruikers zelf die verantwoordelijk zijn voor het draaien van deze machines. Wat wij een "Bitcoin node" noemen, is precies die computer waarop software draait die het Bitcoin protocol implementeert (net als Bitcoin core, maar daar komen we later op terug). Dit is wat Bitcoin in staat stelt om zonder centrale autoriteit te werken: validatie wordt gedistribueerd uitgevoerd, door duizenden onafhankelijke machines van duizenden gebruikers.



![Image](assets/fr/047.webp)



Nakamoto, S. (2008). *Bitcoin: Een Peer-to-Peer elektronisch geldsysteem*. https://Bitcoin.org/Bitcoin.pdf



Het zijn juist deze gebruikers die de veiligheid van Bitcoin garanderen. Zoals Eric Voskuil uitlegt in zijn boek *Cryptoeconomics*, berust de veiligheid van Bitcoin niet op Blockchain, noch op hashingkracht, noch op validatie, decentralisatie, cryptografie, open source of speltheorie. De veiligheid van Bitcoin hangt voornamelijk af van de individuen die bereid zijn zichzelf bloot te stellen aan persoonlijk risico. Decentralisatie maakt het mogelijk dit risico te spreiden over een groot aantal individuen en alleen hun vermogen om weerstand te bieden garandeert de robuustheid van het systeem.



Dit principe is eenvoudig te begrijpen: als Bitcoin afhankelijk zou zijn van één enkel knooppunt van één enkele persoon, zou het opsluiten van die persoon voldoende zijn om het netwerk uit te schakelen, omdat hij alleen alle risico's op zich zou nemen. Met tienduizenden knooppunten verspreid over de hele wereld is het risico verspreid: elk van deze operators zou geneutraliseerd moeten worden om Bitcoin uit te schakelen.



![Image](assets/fr/048.webp)



We kunnen dus verschillende concepten onderscheiden en benoemen om dingen te verduidelijken voor de rest van deze cursus:




- Bitcoin valuta: de rekeneenheid die gebruikt wordt voor transacties binnen dit systeem;
- Het Bitcoin netwerk: de verzameling van alle verbonden knooppunten;
- Bitcoin knooppunten: machines waarop een implementatie van Bitcoin draait;
- Bitcoin implementaties: software die het protocol vertaalt in uitvoerbare instructies;
- Bitcoin protocol: de verzameling regels voor de werking van het systeem;
- Het Bitcoin systeem: de coherente combinatie van al deze Elements.



### De rol van het Bitcoin knooppunt



De Bitcoin nodes vormen samen het zogenaamde Bitcoin netwerk. Ze maken het mogelijk dat het hele systeem autonoom werkt, zonder tussenkomst van een centrale autoriteit of hiërarchie van servers.



Vanaf het begin was Bitcoin ontworpen om elke gebruiker een persoonlijk knooppunt te laten beheren. Dit geldt nog steeds voor de huidige Bitcoin core software, die de rollen van Wallet en node combineert. Maar tegenwoordig wordt deze functie vaak losgekoppeld: veel moderne Bitcoin wallets zijn gewoon wallets die verbinding maken met externe nodes (al dan niet eigendom van dezelfde persoon).



### Blockchain houden



De eerste taak van een knooppunt is om een lokale kopie van Blockchain te onderhouden. Om Double-spending op Bitcoin te voorkomen zonder een centrale autoriteit in te schakelen, moet elke gebruiker controleren of er geen transactie in het systeem bestaat. De enige manier om hier zeker van te zijn, is door alle transacties op Bitcoin te kennen. Daarom worden alle transacties voorzien van een tijdstempel en gegroepeerd in blokken, en slaat elk knooppunt het volledige Blockchain op.



> De enige manier om de afwezigheid van een transactie te bevestigen is door op de hoogte te zijn van alle transacties.

Nakamoto, S. (2008). *Bitcoin: Een Peer-to-Peer elektronisch geldsysteem*. https://Bitcoin.org/Bitcoin.pdf



Blockchain is daarom een evoluerend register: elke keer dat een nieuw blok wordt gepubliceerd door een Miner, controleert het knooppunt de geldigheid ervan voordat het het toevoegt aan zijn eigen lokale kopie van de keten. Op dit moment (juli 2025) is de volledige Blockchain groter dan 675 GB en deze grootte blijft groeien, omdat er gemiddeld elke 10 minuten een nieuw blok wordt toegevoegd.



![Image](assets/fr/049.webp)



Het knooppunt houdt ook een lokaal overzicht bij van alle UTXO's die op een bepaald moment bestaan, bekend als de **UTXO set**. Deze database bevat alle ongebruikte Bitcoin fragmenten. We komen hier in detail op terug in het laatste deel van de cursus.



### Transacties verifiëren en distribueren



De tweede rol van een knooppunt is het verifiëren en verspreiden van transacties. Wanneer een nieuwe transactie het knooppunt bereikt (via Wallet software of een ander knooppunt), controleert het of het voldoet aan een set regels (consensusregels en relaisregels). Bijvoorbeeld:




- uitgegeven bitcoins moeten bestaan in de UTXO set (de database van niet-uitgegeven uitgangen);
- de handtekening moet geldig zijn en aan alle bestedingsvoorwaarden moet zijn voldaan (geldig script);
- de totale hoeveelheid outputs mag niet groter zijn dan de totale hoeveelheid inputs, wat betekent dat de kosten niet negatief kunnen zijn.



![Image](assets/fr/050.webp)



Na validatie wordt de transactie opgeslagen in de Mempool van het knooppunt, een tijdelijke geheugenruimte die gereserveerd is voor onbevestigde transacties, en vervolgens doorgestuurd naar de andere netwerkpeers waarmee het verbonden is. Dit distributie- en validatiemechanisme gaat door van knooppunt tot knooppunt. Op deze manier wordt de transactie verspreid over het Bitcoin netwerk en elk knooppunt slaat het op in Mempool totdat het wordt opgenomen in een geldig blok door een Miner, die dan handelt op basis van de eerste bevestiging.



### Blokken controleren en verdelen



De derde rol van het knooppunt is het beheren van gemijnde blokken. Wanneer een Miner een nieuw blok met een geldige Proof of Work ontdekt, wordt het uitgezonden op het netwerk. De knooppunten ontvangen het, controleren of het voldoet aan alle protocolregels en integreren het in hun eigen lokale kopie van de Blockchain als het geldig is. Net als bij transacties worden nieuw gevalideerde blokken vervolgens doorgestuurd naar alle peers die verbonden zijn met het knooppunt. Dit proces gaat door totdat alle knooppunten op het Bitcoin netwerk op de hoogte zijn van het nieuwe blok.



![Image](assets/fr/051.webp)



## Wat is het verschil tussen een boog en een Wallet?


<chapterId>de5af634-a628-4b90-b869-468c208e178b</chapterId>



Het is essentieel om onderscheid te maken tussen twee verschillende soorten software bij het gebruik van Bitcoin: de node en de Wallet.



Een Bitcoin knooppunt is, zoals hierboven genoemd, een stuk software dat actief deelneemt aan het peer-to-peer netwerk. Het voert drie hoofdtaken uit:




- back-up van Blockchain,
- transactievalidatie en -relais,
- blokvalidatie en relais.



Een Bitcoin Wallet, aan de andere kant, is een stuk software dat ontworpen is om je privésleutels op te slaan en te beheren. Met deze sleutels kun je je bitcoins uitgeven door te voldoen aan de vergrendelingsscripts (meestal door middel van een handtekening). Een Wallet kan verbinding maken met een knooppunt (lokaal of op afstand) om de status van de Blockchain te raadplegen en de transacties die het bouwt uit te zenden, maar het is als zodanig geen deelnemer aan het netwerk.



In sommige gevallen bestaan deze twee functies naast elkaar in dezelfde software, zoals het geval is bij Bitcoin core, dat zowel als Full node en als Wallet dient. Veel populaire Wallet programma's (Sparrow, BlueWallet, etc.) vereisen echter een verbinding met een extern knooppunt (van jezelf of van een derde partij) om transacties uit te zenden en het Wallet saldo te bepalen.



![Image](assets/fr/052.webp)



## Wat is het verschil tussen een knooppunt en een Miner?


<chapterId>d2992614-7ab7-4bf9-81b1-f548cda67257</chapterId>



De begrippen knooppunt en Miner worden vaak met elkaar verward. Toch vervullen deze twee Elements radicaal verschillende functies binnen het systeem.



Aanvankelijk, toen Bitcoin in 2009 door Satoshi Nakamoto werd gelanceerd, werd van elke gebruiker verwacht dat hij deelnam aan het netwerk als geheel. De oorspronkelijke Bitcoin software combineerde dus meerdere functies tegelijk: het fungeerde als een Wallet, een knooppunt, en ook als een Miner, in staat om nieuwe blokken te genereren. In die tijd was de moeilijkheidsgraad van Mining erg laag. Je hoefde alleen maar de Bitcoin software op je computer te draaien om blokken te vinden en bitcoins als beloning te ontvangen.



Maar met de geleidelijke popularisering van Bitcoin en de toename van het aantal mijnwerkers, heeft het concurrentielandschap in Mining een radicale verandering ondergaan. Vandaag de dag is Mining een extreem competitieve activiteit geworden, gedomineerd door industriële spelers met gespecialiseerde infrastructuren. De kracht die nodig is om een nieuw blok te delven is nu zo groot dat het vrijwel onmogelijk is voor een individuele gebruiker om dit te bereiken met alleen een conventionele computer. Als gevolg hiervan wordt Mining nu voornamelijk uitgevoerd met behulp van gespecialiseerde machines die ASIC's (*Application-Specific Integrated Circuits*) worden genoemd. Deze chips zijn uitsluitend geoptimaliseerd om dubbele SHA-256 uit te voeren, het algoritme dat gebruikt wordt voor Mining op Bitcoin.



![Image](assets/fr/053.webp)



Door deze evolutie zijn de rollen van het Bitcoin knooppunt en het Miner knooppunt duidelijk gescheiden. Zoals hierboven getoond, is de rol van een Bitcoin knooppunt puur informatief en gebaseerd op validatie. De rol van het Miner knooppunt is anders:




- Het selecteert lopende transacties in de Mempool.
- Het bouwt een kandidaatblok dat deze transacties integreert.
- Hij zoekt met vallen en opstaan naar een geldige Proof of Work.
- Als het een geldig bewijs vindt, zendt het het blok via zijn knooppunt uit naar de andere knooppunten.



Een Miner heeft een Bitcoin knooppunt nodig voor interactie met het netwerk.



De rol van de Miner wordt soms ook onderscheiden van die van de hakker. Een hakker is een machine wiens taak het is om Hash sjabloonblokken aan te leveren door de server van een pool, op zoek naar hashes die voldoen aan de moeilijkheidsdoelstelling gedefinieerd voor aandelen, en niet die van Bitcoin. De rest van het Mining proces, dat de eigenlijke blokconstructie, transactieselectie of Proof-of-Work zoeken volgens Bitcoin's eigen moeilijkheidsgraad en distributie omvat, wordt direct door de pools uitgevoerd.



![Image](assets/fr/054.webp)



Tenslotte is er een belangrijk verschil in economische stimulans tussen de Miner en het knooppunt. Het runnen van een Bitcoin node levert geen direct geldelijk voordeel op. Aan de andere kant levert deelname aan Mining beloningen op (subsidies en transactiekosten) voor elk gevonden blok.



In deel 2 gaan we dieper in op de praktische en persoonlijke voordelen van het installeren en gebruiken van een Bitcoin node, naast de puur financiële.



## Bitcoin core en protocolimplementaties


<chapterId>72381876-9317-4faa-8d41-2b252a945b8a</chapterId>



Het Bitcoin protocol is geen software: het is een verzameling stilzwijgende regels die gedeeld worden tussen netwerkgebruikers. Het definieert voorwaarden voor de geldigheid van transacties, mechanismen om geld te creëren, blokformaat, Proof-of-Work voorwaarden en vele andere specificaties. Om met dit protocol te communiceren, moeten gebruikers software draaien die deze regels implementeert: dit staat bekend als een **implementatie** van Bitcoin.



Een implementatie is daarom knooppuntsoftware: een programma dat in staat is om te communiceren met andere machines op het Bitcoin netwerk, blokken en transacties te downloaden, te verifiëren, op te slaan en te propageren, en lokaal consensus en relay regels af te dwingen. Elke implementatie is een concrete interpretatie van het protocol, geschreven in een bepaalde programmeertaal, met zijn eigen architectuur, prestaties en ergonomie. Elke implementatie heeft ook zijn eigen ontwikkelingsorganisatie, met zijn eigen verdeling van verantwoordelijkheden.



Van deze implementaties domineert er één veruit: **Bitcoin core**.



![Image](assets/fr/055.webp)



### Een historische implementatie die een benchmark is geworden



Bitcoin core is de referentiesoftware voor het Bitcoin protocol. Het is afgeleid van de originele code geschreven door Satoshi Nakamoto in 2008-2009, en is er een directe voortzetting van. Aanvankelijk bekend als "*Bitcoin*", daarna "*Bitcoin QT*" (vanwege de toevoeging van een grafische Interface via de Qt bibliotheek), werd het in 2014 hernoemd naar "*Bitcoin core*" om de software duidelijk te onderscheiden van het netwerk. Sinds versie 0.5 wordt het gedistribueerd met twee componenten: `Bitcoin-qt` (de grafische Interface) en `bitcoind` (de opdrachtregel Interface).



In theorie vertegenwoordigt Bitcoin core niet het Bitcoin protocol, maar is het slechts één implementatie onder vele. Het onderscheidt zich echter door zijn massale adoptie, zijn leeftijd, de robuustheid van zijn code en de nauwgezetheid van zijn ontwikkelingsproces. Bijgevolg zijn in de praktijk de regels toegepast door Bitcoin core de facto die van het Bitcoin protocol: gebruikers, ontwikkelaars, mijnwerkers en ecosysteemdiensten verwijzen er bijna uitsluitend naar.



### Huidige verdeling van implementaties



Volgens [gegevens verzameld in augustus 2025 door Luke Dashjr](https://luke.dashjr.org/programs/Bitcoin/files/charts/software.html) (een bekende ontwikkelaar in het ecosysteem) is de verdeling van implementaties over de openbare knooppunten van het netwerk als volgt:




- Bitcoin core**: 87.3% van knooppunten
- Bitcoin Knots**: 12.5
- Andere cumulatieve implementaties**: 0.2% (btcsuite, Bcoin, BTCD...)



![Image](assets/fr/056.webp)



Met andere woorden, ongeveer 9 van de 10 publieke knooppunten draaien Bitcoin core. De rest van het netwerk vertrouwt op meer marginale clients (hoewel het aandeel van Knots de laatste maanden sterk is gestegen, niet in het minst in de nasleep van discussies over de `OP_RETURN` grootte limiet). Deze alternatieve implementaties worden vaak onderhouden door één persoon of een klein team.



**Noot:** Deze cijfers zijn echter nog steeds schattingen, omdat ze voornamelijk gebaseerd zijn op *luisterende knooppunten*, d.w.z. knooppunten die inkomende verbindingen accepteren (met poort 8333 open). Niet-luisterende knooppunten* zijn veel complexer om te tellen, omdat het onmogelijk is om direct verbinding met ze te maken: je moet wachten tot het initiatief van hen komt, in de vorm van een uitgaande verbinding. De site van Luke Dashjr beweert dat hij deze *niet-luisterende knooppunten* ook probeert te tellen, maar het blijft onmogelijk om er perfect nauwkeurige gegevens over te verkrijgen en het bijwerken van deze statistieken loopt onvermijdelijk achter op de realiteit.



### Interne werking van Bitcoin core



Bitcoin core is geschreven in C++. Het is ook een open source project dat wordt onderhouden door een gemeenschap van ontwikkelaars die vrijwillig werken of worden betaald door verschillende entiteiten (vaak door bedrijven in het ecosysteem die een gevestigd belang hebben in de ontwikkeling van Core). [De code wordt gehost op GitHub](https://github.com/Bitcoin/Bitcoin), en de ontwikkeling volgt een rigoureus:




- Contributors** dienen voorstellen in in de vorm van _pull requests_ (PR). In principe kan iedereen een verandering voorstellen, maar het moet getest en gedocumenteerd worden en door een peer review proces gaan.
- De **beheerders** hebben het recht om PR's goed te keuren en samen te voegen. Zij zijn degenen die de samenhang en stabiliteit van het project garanderen. In juli 2025 zijn er vijf van hen: Hennadii Stepanov, Michael Ford, Andrew Chow, Gloria Zhao en Ryan Ofsky.
- Sinds februari 2023 is er geen **hoofdbeheerder** meer geweest. Deze rol werd aanvankelijk vervuld door Satoshi Nakamoto bij de lancering van Bitcoin, daarna door Gavin Andresen na het vertrek van Nakamoto begin 2011, en ten slotte door Wladimir J. Van Der Laan van 2014 tot 2023.



![Image](assets/fr/057.webp)



De ontwikkeling van Bitcoin core volgt een meritocratische logica: nieuwe bijdragers worden aangemoedigd om de code te bekijken en te testen voordat ze zelf wijzigingen voorstellen. Beslissingen zijn gebaseerd op technische consensus, en grote wijzigingen (vooral in gebieden waar consensus over bestaat) vereisen upstream discussies op openbare kanalen, zoals mailinglijsten of PR review clubs.



### Andere Bitcoin implementaties



Hoewel het aantal gebruikers marginaal is, bestaan er andere clients. De belangrijkste is Bitcoin Knots, ontwikkeld door Luke Dashjr, een Fork van Bitcoin core met extra opties en een conservatievere benadering van ontwikkeling. Deze omvatten strengere beperkingen voor transactieformaten.



![Image](assets/fr/058.webp)



We kunnen ook vermelden:




- Libbitcoin**: een modulaire C++ bibliotheek ontwikkeld door Amir Taaki en onderhouden door Eric Voskuil;
- Bcoin**: een JavaScript-implementatie, niet langer actief onderhouden;
- BTCD/btcsuit**e: een implementatie in Go.



Deze projecten dragen bij aan de diversiteit van het ecosysteem, maar hun toepassing blijft zeer beperkt, waardoor Bitcoin core moeilijk onafhankelijk kan evolueren.



### De kracht van Core-ontwikkelaars



Je zou kunnen denken dat Bitcoin core ontwikkelaars directe controle hebben over Bitcoin, maar dat is niet het geval. Ze kunnen geen verandering aan het protocol opleggen. Hun rol is om code voor te stellen. Het is aan elke gebruiker, via zijn knooppunt, om te beslissen of hij deze code al dan niet gebruikt.



Dit betekent dat als er geen consensus is over een verandering in Bitcoin core, deze genegeerd kan worden door de knooppunten, door Bitcoin core niet bij te werken of door simpelweg de implementatie te veranderen. Omgekeerd, als een door gebruikers gewenste functie geblokkeerd wordt in het ontwikkelproces van Core, is het altijd mogelijk om over te stappen op een andere implementatie of Fork het project te verlaten.



Zoals we later in deze cursus zullen bespreken, zijn het de knooppunten, op basis van hun economisch gewicht (de handelaren), die een versie van het protocol (en dus de bijbehorende valuta) nut geven door eenheden te accepteren die de regels respecteren. De echte bestuurlijke macht over Bitcoin ligt daarom bij deze handelaren, niet bij de ontwikkelaars.




# Word een soevereine bitcoiner


<partId>df64cad2-e92d-4949-9cca-14394aad0bc6</partId>




## Waarom je eigen knoop doorhakken?


<chapterId>39c0cd19-67f9-4c64-bfb3-dbd6eec0bf42</chapterId>



Er heerst een wijdverspreid geloof dat het runnen van een Bitcoin node een zuiver altruïstische daad is, zonder persoonlijk gewin, uitsluitend in dienst van de decentralisatie van het netwerk. Sommigen beschouwen het als een soort plicht voor bitcoiners om het systeem te ondersteunen en hun dankbaarheid te tonen aan Bitcoin.



Zoals we in de vorige hoofdstukken al aangaven, is er geen direct financieel voordeel verbonden aan het leggen van een knoop. Je zou daarom kunnen denken dat er geen persoonlijk belang bij is. Toch brengt het runnen van je eigen knoop veel individuele voordelen met zich mee. Om je hiervan te overtuigen, ga ik in dit hoofdstuk alle redenen presenteren, zowel technische als strategische, waarom je je eigen Bitcoin node zou moeten installeren en gebruiken.



### Vertrouwelijkere verspreiding van transacties



Wanneer Wallet software verbinding maakt met een extern knooppunt, stuurt het zijn transacties door naar een infrastructuur die niet onder jouw controle staat. Dit brengt voor de hand liggende risico's van toezicht met zich mee: de operator van het externe knooppunt kan de details van jouw transacties analyseren, inclusief bedragen en frequenties, en door het kruislings controleren van bepaalde metadata (zoals IP-adressen, tijden en locaties), deze mogelijk in verband brengen met jouw identiteit.



Zoals we in een vorig hoofdstuk al aangaven, communiceren wallets niet zomaar met het Bitcoin netwerk; ze moeten verbinding maken met een node om balansen te raadplegen of transacties uit te zenden. Als je nooit je eigen node hebt opgezet, betekent dit dat je Wallet afhankelijk is van de infrastructuur van een derde partij (meestal het bedrijf achter de software). Deze derde partij, vooral als het een bedrijf is, kan deze gegevens observeren, exploiteren of zelfs openbaar maken: om commerciële redenen, onder wettelijke dwang of als gevolg van piraterij.



![Image](assets/fr/059.webp)



Door je eigen node te gebruiken, verstuur je je transacties rechtstreeks naar het netwerk, zonder tussenpersonen. Op voorwaarde dat je je knooppunt goed beveiligt (wat we later zullen bespreken) of aan bepaalde standaarden voldoet, wordt er geen informatie blootgesteld: noch je IP Address, noch de details van je transacties gaan door een entiteit waar jij geen controle over hebt. Dit is een basisvoorwaarde om je vertrouwelijkheid op Bitcoin te bewaren.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Niet-censureerbare transacties



Om dezelfde redenen die hierboven genoemd zijn, is Wallet software gebaseerd op een knooppunt van een derde partij kwetsbaar voor censuurrisico's: de operator van het knooppunt op afstand kan om verschillende redenen weigeren om bepaalde transacties door te geven. Hij kan ze verdacht vinden of in strijd met zijn beleid. De transactie kan ook worden geblokkeerd als deze niet voldoet aan de doorgeefregels van het knooppunt. Tot slot kan de operator zich specifiek richten op jouw IP Address om de uitzending van jouw transacties te blokkeren.



Omgekeerd, door je eigen node te gebruiken, zorg je voor de verspreiding van je transacties binnen het peer-to-peer netwerk. Dit betekent dat je volledige controle behoudt over de verspreiding van je transacties, zonder afhankelijkheid van een tussenpersoon. Zolang de transactie voldoet aan de consensus- en relayregels van de knooppunten die met het jouwe verbonden zijn, zal ze worden uitgezonden op het netwerk en vervolgens, op voorwaarde dat er voldoende vergoedingen zijn, door een Miner in een blok worden geïntegreerd. Een eigen node garandeert een neutrale, toestemmingsvrije bevestiging van je transacties.



### Onafhankelijke gegevensverificatie



Zonder een persoonlijk knooppunt blijft u afhankelijk van een derde partij voor toegang tot informatie, zoals uw Address saldo, transactiebevestigingsstatus en blokgeldigheid. Dit impliceert een impliciet vertrouwen in de nauwkeurigheid en integriteit van het externe knooppunt.



![Image](assets/fr/060.webp)



Met een Full node kun je alle protocolregels zelf controleren, voor elke transactie en elk blok. Het resultaat is dat het saldo dat je Wallet weergeeft geen gegevens zijn die je ontvangt van een externe server, maar een resultaat dat lokaal berekend is uit een complete kopie van de Blockchain, die blok voor blok gevalideerd is. Deze benadering geeft de volledige betekenis aan de stelregel van bitcoiners:



> Vertrouw niet, maar controleer.

### Betere verdeling van systeembeveiliging



Elk knooppunt dat zich bij het netwerk aansluit, versterkt de redundantie en veerkracht van Bitcoin. Het vergemakkelijkt de verspreiding van informatie en stelt nieuwe peers in staat om zich met elkaar te verbinden. Zonder de knooppunten zou het systeem simpelweg onbruikbaar zijn.



Zoals we hebben gezien is de veiligheid van Bitcoin niet gebaseerd op decentralisatie, Mining of cryptografie: zoals bij elk systeem is het afhankelijk van individuen. Om precies te zijn, het hangt af van het vermogen van knooppuntbeheerders om dwang te weerstaan.



Wat gedecentraliseerde systemen zoals Bitcoin onderscheidt, is de verdeling van het risico over alle betrokkenen. Je eigen Bitcoin node beheren betekent een deel van dit risico accepteren door de veiligheid van jouw instantie te garanderen; door dit te doen, verlicht je ook de risicolast voor andere nodebeheerders.



Het is dus geen direct persoonlijk voordeel: een node runnen maakt je medeverantwoordelijk voor de veiligheid van het netwerk. Het is vooral een collectief voordeel, omdat jouw betrokkenheid helpt om het risico te spreiden. Op uw beurt vergroot u uw eigen vermogen om Bitcoin betrouwbaar te gebruiken.



### Verdiep uw begrip van het systeem



Het installeren van een Full node is geen sinecure. Het omvat het installeren van software, het begrijpen van de basiswerking, het controleren van synchronisatie, het onderzoeken van logboeken in geval van problemen en zelfs het gebruik van de terminal. Dit leidt noodzakelijkerwijs tot een beter begrip van het protocol. Dit is een indirect, maar niet onbelangrijk voordeel.



Het verwerven van deze kennis versterkt je vertrouwen in het gereedschap en kan het risico op fouten of blootstelling aan oplichterij verminderen. Je eigen knoop leggen is ook een vorm van leren.



### Kiezen welke regels je wilt toepassen



Een belangrijk aspect, dat vaak verkeerd begrepen wordt, is dat je met een knooppunt kunt kiezen welke regels je lokaal toepast. Er zijn twee hoofdtypen regels:





- Consensusregels**:



Dit zijn de fundamentele regels van het Bitcoin protocol, die de integriteit van het systeem waarborgen en de criteria vaststellen voor het valideren van transacties en blokken. Een transactie die niet voldoet aan deze consensusregels kan nooit worden opgenomen in een geldig blok. Een transactie met een ongeldige handtekening op één van de gegevens wordt bijvoorbeeld systematisch uitgesloten.



Het veranderen van deze regels staat gelijk aan het veranderen van het protocol en dus de valuta (Hard Fork). Maar zelfs zonder te proberen om ze te wijzigen, geeft het simpele feit van het strikt toepassen van de bestaande regels een zekere macht: als een blok de regels overtreedt, wijst de node het onmiddellijk af.





- Estafette-regels**:



Dit zijn regels die specifiek zijn voor elk Bitcoin knooppunt en die toegevoegd worden aan de consensusregels om de structuur van onbevestigde transacties te definiëren die geaccepteerd worden in de Mempool en doorgegeven worden aan peers. Elk knooppunt configureert en past deze regels lokaal toe, wat verklaart waarom ze van knooppunt tot knooppunt kunnen verschillen. Ze zijn alleen van toepassing op onbevestigde transacties: een transactie die door een knooppunt als "niet-standaard" wordt beschouwd, wordt alleen geaccepteerd als deze al in een geldig blok voorkomt. Het veranderen van deze regels sluit het knooppunt niet uit van het Bitcoin systeem.



Bijvoorbeeld, een transactie zonder kosten is, volgens de consensusregels, volkomen geldig, maar wordt standaard afgewezen volgens het Bitcoin core relaybeleid, omdat de `minRelayTxFee` parameter is ingesteld op `0.00001` (in BTC/kB). Het is echter mogelijk, op uw eigen node, om deze drempel te verlagen om transacties met lagere vergoedingen door te geven, of, omgekeerd, om de limiet te verhogen, bijvoorbeeld tot 2 Sats/vB, om het doorgeven van transacties met lage vergoedingen te vermijden.



Je eigen knoop doorhakken betekent dat je beweert: "Ik valideer wat ik verkies te valideren, volgens de regels die ik zelf heb aangenomen"*. Je wordt zo een actor in het beheer van het systeem, in staat om een evolutie die je onaanvaardbaar lijkt af te wijzen of om een update goed te keuren volgens je eigen criteria.



We kunnen dus snel proberen te begrijpen hoeveel macht je hebt over de regels dankzij je knooppunt. En de omvang van deze macht hangt af van het type regel.



#### Voor relaisregels



Wat de regels voor het doorgeven van transacties betreft, is het belangrijkste gewoon dat je een knooppunt bezit, ongeacht de economische activiteit ervan. Waar het hier om gaat is of je wel of niet akkoord gaat met het doorgeven van bepaalde soorten transacties.



Als je bijvoorbeeld van mening bent dat transacties met vergoedingen van minder dan 1 sat/vB geaccepteerd moeten worden op Bitcoin, dan kun je deze regel op je knooppunt aanpassen zodat het deze transacties uitzendt en zo hun verspreiding op het netwerk vergemakkelijkt totdat een Miner ze uiteindelijk opneemt in een geldig blok. In wezen is het dus een kwestie van macht over de verspreiding van transacties: elk knooppunt heeft beslissingsbevoegdheid, omdat ermee instemmen om een type transactie door te geven gelijk staat aan het bevorderen van de acceptatie ervan op het Bitcoin netwerk. Als je meerdere knooppunten beheert, heb je dus meer invloed op het doorgeefbeleid, omdat elk knooppunt zijn eigen verbindingen en invloedssferen op het netwerk heeft.



Het hebben van een of meer knooppunten die geconfigureerd zijn met specifieke relaisregels betekent dat bepaald wordt welk deel van het netwerk een bepaald type transactie accepteert om te verspreiden. Het verspreiden van een bericht in een peer-to-peer grafiek, zoals het geval is voor Bitcoin transacties, volgt de logica van de percolatietheorie. Stel je elk knooppunt voor als een site die actief (`p` = het doorgeeft) of inactief (`1-p`) kan zijn. Zodra het aandeel `p` een kritieke drempel overschrijdt (`p_c`), ontstaat er een gigantische component: de transactie slaagt erin het netwerk te doorkruisen en heeft alle kans om een Miner te bereiken. In een netwerk zoals Bitcoin, waar elk knooppunt gemiddeld 8 uitgaande verbindingen onderhoudt, wordt de `p_c` drempel over het algemeen ingesteld op slechts enkele procenten, zelfs lager als sommige knooppunten een zeer groot aantal verbindingen hebben.



![Image](assets/fr/061.webp)



Zolang `p` onder `p_c` blijft, blijft een transactie beperkt tot geïsoleerde pockets en bereikt geen Miner. Zodra deze drempel wordt overschreden, verspreidt het zich vrijwel onmiddellijk door het hele netwerk. Zodra deze drempel wordt overschreden, verspreidt de transactie zich vrijwel onmiddellijk over het hele netwerk.



Uiteindelijk zijn het altijd de miners die beslissen of een transactie al dan niet wordt opgenomen in een blok. De knooppunten interveniëren echter stroomopwaarts door de distributie van transacties te beïnvloeden: zij bepalen of de miners al dan niet op de hoogte zullen zijn van een bepaalde transactie. Als een transactie niet wordt doorgegeven aan de miners, is het uiteraard onmogelijk voor hen om deze in een blok op te nemen.



Het toevoegen van een paar extra nodes zal daarom slechts een marginale impact hebben als het netwerk zich al in de percolatiefase bevindt voor een bepaald type transactie, maar het kan doorslaggevend zijn als de percolatiedrempel nadert. Het bezitten of beïnvloeden van meerdere nodes, vooral als ze goed verbonden zijn, kan de waarde van `p` verhogen of verlagen en dus indirect de relay regels sturen die bepalen welke transacties worden gezien en uiteindelijk geaccepteerd door miners.



#### Voor consensusregels



Als het gaat om de invloed van jouw node op de consensusregels, is vooral het economische gewicht doorslaggevend. Dit is een cruciaal concept: de waarde van een valuta is direct gerelateerd aan het vermogen om Exchange te faciliteren. Inderdaad, als een voorwerp door niemand in Exchange geaccepteerd wordt voor goederen of diensten, heeft het theoretisch geen monetair nut. Als bijvoorbeeld geen enkele handelaar kiezelstenen accepteert als betaalmiddel, hebben ze geen nut als geld. Natuurlijk blijft nut een subjectief begrip op individuele schaal, maar hoe groter het aantal handelaren in een bepaald gebied dat een voorwerp accepteert als betaalmiddel in Exchange, hoe waarschijnlijker het is dat dit voorwerp een monetair nut heeft voor de mensen die in dit gebied wonen.



Laten we het voorbeeld nemen van een dorp waar veel kooplieden goud in Exchange accepteren voor goederen: de kans is groot dat goud een monetair nut heeft voor de dorpelingen. Dit geeft aan dat het nut van een valuta direct afhangt van de beslissingen van handelaren om het te accepteren of af te wijzen.



Dit concept is cruciaal voor het begrijpen van de machtsdynamiek die speelt in het Bitcoin systeem. Satoshi maakt het duidelijk: Bitcoin is een elektronisch geldsysteem; met andere woorden, het levert een dienst die een vorm van valuta biedt, Bitcoin (of BTC). Wanneer de protocolregels gewijzigd worden op een manier die niet achterwaarts compatibel is (Hard Fork), komt dit neer op het creëren van een nieuw systeem en dus een nieuwe valuta. Het succes of falen van deze Fork hangt dan af van de omvang van de economie, die op zijn beurt wordt bepaald door het aantal handelaren dat deze nieuwe vorm van valuta accepteert.



![Image](assets/fr/062.webp)



Laten we een voorbeeld nemen: stel dat Bitcoin lijdt onder Hard Fork. Er zouden dan 2 verschillende vormen van valuta zijn: BTC-1 (de originele, ongewijzigde versie) en BTC-2 (de nieuwe munt met andere consensusregels). Als alle handelaars die BTC-1 aanvaardden dit blijven doen, maar BTC-2 verwerpen, dan zal deze laatste in theorie een zeer beperkt monetair nut hebben. Als gebruiker zou ik er geen belang bij hebben om BTC-2 te houden en te gebruiken, wetende dat geen enkele handelaar het zou willen in Exchange voor goederen of diensten. Omgekeerd, als 50% van de handelaars ervoor kiest om enkel BTC-2 te aanvaarden en de overige 50% enkel BTC-1, dan zal het nut van BTC-1 in theorie gehalveerd zijn. Ik gebruik de term "in theorie" omdat het nut subjectief blijft op individueel niveau en afhangt van een veelheid aan factoren (zoals territorium en consumptiegewoonten) die moeilijk van geval tot geval te begrijpen zijn.



Op Bitcoin omvat de rol van "handelaar", opgevat als elke entiteit met een bepaald economisch gewicht, natuurlijk bedrijven (fysieke winkels, online verkoopsites, dienstverleners, etc.), maar ook Exchange platforms, omdat ze Bitcoin accepteren in Exchange voor andere valuta, en miners, omdat ze Bitcoin accepteren via vergoedingen in Exchange voor de dienst van het opnemen van een transactie in een blok.



Wat de consensusregels betreft, kun je met je knooppunt je economische activiteit richten op de ene of de andere valuta. Als je bijvoorbeeld 10 volle nodes thuis hebt, maar geen significante economische activiteit, zal je invloed tijdens een Fork bijna nihil zijn. Omgekeerd geeft één enkel knooppunt, dat gebruikt wordt om een keten van 200 winkels te beheren die Bitcoin accepteren, een aanzienlijk economisch gewicht.



Het gaat dus niet om het aantal knooppunten, maar om het belang van de economische activiteit die ze ondersteunen. Bovendien, als je economische activiteit afhangt van een knooppunt waar je geen controle over hebt, zal de eigenaar ervan beslissen welke valuta je gebruikt, zolang je verbonden blijft met dat knooppunt. Daarom is het runnen en gebruiken van je eigen node bijzonder belangrijk in de context van systeembeheer:



> Niet jouw knoop, niet jouw regels.


## De verschillende typen Bitcoin knooppunten


<chapterId>be8f0baa-41f2-4b54-b011-092f4ccc93aa</chapterId>



Een Bitcoin knooppunt is dus een machine waarop een implementatie van het Bitcoin protocol draait. Achter deze algemene definitie van knooppunten bestaan verschillende mogelijke configuraties, die niet allemaal hetzelfde niveau van autonomie, resourceverbruik en bruikbaarheid voor het netwerk bieden. In dit hoofdstuk proberen we deze verschillen te begrijpen om je te helpen een knooppuntarchitectuur te kiezen die past bij jouw gebruik en hardwarebeperkingen.



### De volledige knoop



Een Full node is simpelweg een Bitcoin knooppunt dat het volledige Blockchain van het Genesis blok downloadt, elk blok onafhankelijk valideert en de geschiedenis van al dat Blockchain lokaal opslaat. Dit is de "normale" vorm van een Bitcoin knooppunt, zoals voorgesteld door Satoshi Nakamoto.



![Image](assets/fr/063.webp)



De Full node hoeft niemand te vertrouwen omdat hij alle informatie in het systeem valideert en kent. Het is het type node dat je de meeste garanties geeft: je weet, zonder afhankelijk te zijn van een derde partij, of een betaling geldig is, of een blok geldig is, of een reorganisatie legitiem is, enzovoort.



In de praktijk vereist een Full node niet-triviale middelen, waaronder enkele honderden gigabytes voor blokbestanden, een processor die scripts kan valideren, RAM voor de Mempool en caches, en een stabiele bandbreedte. De eerste synchronisatie (*IBD*) leest en verifieert de complete geschiedenis: het is intensief, maar gebeurt maar één keer. Een Full node neemt actief deel aan het netwerk, geeft blokken en transacties door en kan binnenkomende verbindingen accepteren om andere peers te helpen.



Afhankelijk van je behoeften kun je een indexer toevoegen aan je Full node. Bitcoin core biedt transactie-indexering als een optionele functie (standaard uitgeschakeld), die nuttig kan zijn voor specifieke doeleinden. Het bevat echter geen Address indexer, wat vaak de meest gewilde functie is voor individuele gebruikers. Om dit te verhelpen kun je speciale software op je knooppunt installeren, zoals Electrs of Fulcrum, om Address balansverificatie queries van geassocieerde UTXO's te versnellen. We zullen in een apart hoofdstuk dieper ingaan op de rol van de indexeerder.



### De pruned knoop



Het pruned knooppunt valideert alles als een Full node, van het Genesis blok tot de kop van de keten met het meeste werk, maar **behoudt alleen het meest recente deel van de blokbestanden**. Zodra de oude blokken gecontroleerd zijn, worden ze geleidelijk verwijderd om onder een ruimtelimiet te blijven die je kunt instellen. Deze configuratie is ideaal als u beperkte schijfruimte hebt: u behoudt de onafhankelijkheid van de blokvalidatie, zonder het complete Blockchain geschiedenisarchief op te slaan. Deze optie is vooral handig als u de Bitcoin core op uw pc wilt installeren, zonder een speciale machine te gebruiken.



![Image](assets/fr/064.webp)



De technische implicaties van deze optie zijn vrij eenvoudig: het pruned knooppunt is perfect in staat om uw transacties uit te zenden, deel te nemen aan de relay, blokken en transacties te verifiëren en de keten te volgen. Aan de andere kant kan het niet dienen als een bron van historische gegevens buiten zijn grenzen voor andere toepassingen (bv. volledige verkenners, indexeerders, wallets). Functies die het archief (of een globale index) nodig hebben, zullen daarom niet beschikbaar zijn.



Praktisch gezien kunt u een pruned knooppunt gebruiken om Wallet beheersoftware zoals Sparrow wallet aan te sluiten. Je zult echter geen transacties op je Wallet kunnen scannen die van voor de snoeilimiet dateren. Als je bijvoorbeeld een transactie geregistreerd hebt in blok 901 458, maar je node bewaart alleen blokken vanaf 905 402 (omdat de oudste pruned zijn), dan kun je deze transactie niet scannen. Aan de andere kant, als je het al had gescand toen je knooppunt deze blokhoogte nog had, dan zal je Wallet beheersoftware de informatie opslaan en het saldo van de corresponderende UTXO's correct weergeven.



Kortom, Wallet traceren werkt probleemloos op een pruned knooppunt als je een nieuwe Wallet aanmaakt terwijl je software al verbonden is met dat knooppunt. Aan de andere kant kunt u problemen ondervinden als u een oude Wallet herstelt, omdat transacties uit het verleden die niet meer door het knooppunt worden bewaard, natuurlijk niet meer terug te vinden zijn.



### De lichte knoop / SPV



Een SPV (*Simplified Payment Verification*) node, of lichtgewicht node, bewaart alleen blokkoppen, geen transactiedetails, en vertrouwt op andere volledige nodes om bewijs te verkrijgen dat een transactie in een blok zit (Merkle bewijzen via bomen) waarvoor het de kop heeft. Het concept van vereenvoudigde betalingsverificatie is niet nieuw, het werd voorgesteld door Satoshi Nakamoto zelf in deel 8 van het Witboek.



![Image](assets/fr/066.webp)



Nakamoto, S. (2008). *Bitcoin: Een Peer-to-Peer elektronisch geldsysteem*. https://Bitcoin.org/Bitcoin.pdf



Dit type knooppunt is duidelijk veel lichter in termen van opslag en CPU-gebruik dan een Full node of zelfs een pruned knooppunt. De SPV node is daarom zeer geschikt voor kleinere apparaten en intermitterende verbindingen. In feite wordt het vaak direct geïntegreerd in de Wallet, vooral mobiele software zoals de Blockstream App.



De afweging is vertrouwen en vertrouwelijkheid: een SPV client controleert zelf geen scripts of validatiebeleid; hij gaat ervan uit dat de keten met het meeste werk geldig is en is afhankelijk van een of meer volledige knooppunten voor antwoorden. Het gebruik van dit type knooppunt is daarom een betere optie dan verbinding maken met een knooppunt van een derde partij; het is echter nog steeds minder voordelig dan een Full node of zelfs een pruned knooppunt.



![Image](assets/fr/065.webp)



### Welk knooppunt voor welke behoefte?





- Mobiel / beginnende gebruiker



Voor een beginnende gebruiker met alleen een Wallet op een mobiele app, is het gebruik van een SPV node zeker de beste manier om aan de slag te gaan. De installatie is snel, vereist weinig middelen en de ervaring is eenvoudig en vloeiend. Dit betekent dat je bepaalde informatie zelf kunt verifiëren en dus minder afhankelijk bent van nodes van derden, terwijl je tegelijkertijd onafhankelijker bent als het gaat om het uitzenden van transacties.





- PC / gemiddelde gebruiker



Een gemiddelde gebruiker met een PC kan een pruned node installeren om te profiteren van bijna alle voordelen van een Full node, zonder zijn machine dagelijks te overbelasten: volledige validatie, matig schijfgebruik en eenvoudig onderhoud. Het is een ideale oplossing om je desktop wallets aan te sluiten en onafhankelijk te blijven in de distributie van je transacties, zonder te investeren in een speciale machine of je schijfruimte te overbelasten.





- Soevereine Bitcoiner / gevorderd



Een Full node blijft de beste oplossing als je volledig onafhankelijk wilt zijn in het gebruik van Bitcoin en jezelf later niet wilt beperken tot geavanceerd gebruik zoals een indexer, een Lightning node of zelfs een Block explorer. Dat is precies wat we in deze cursus gaan onderzoeken!



## Overzicht van softwareoplossingen


<chapterId>0d48b89a-e8b5-441e-a707-537a035fc15e</chapterId>



Aan de softwarekant zijn er 2 manieren om een Bitcoin node te gebruiken:




- installeer direct een protocolimplementatie, zoals Bitcoin core (aanbevolen), of Bitcoin Knots,
- of gebruik een kant-en-klare distributie (vaak "_node-in-a-box_" genoemd) die op dezelfde manier een Bitcoin implementatie integreert, maar ook een Interface beheersysteem, een applicatiewinkel en kant-en-klare hulpmiddelen bevat (Lightning, browsers, indexservers, zelfs zelf-hostende toepassingen buiten Bitcoin...).



Beide benaderingen leiden tot hetzelfde doel: het hebben van je eigen node, maar ze verschillen in termen van Interface installatie en gebruik, onderhoud, uitbreidbaarheid en kosten. Dat is wat we in dit hoofdstuk zullen onderzoeken.



### Ruwe Bitcoin knooppuntimplementaties



Het installeren van een ruwe implementatie betekent direct gebruik maken van de software van een Bitcoin protocolimplementatie (zoals Core), zonder aanvullende Layer software. Je beheert de configuratie, updates en bijbehorende diensten (indexering, API, Lightning, back-ups, enz.) zelf, afhankelijk van je behoeften.



Dit is de meest soevereine en flexibele aanpak: je weet precies wat er draait, waar de gegevens zijn en hoe alles werkt. Aan de andere kant wordt het complexer zodra je verder wilt gaan dan de eenvoudige werking van een Bitcoin node. Als je gewoon een node wilt hebben, is de complexiteit vergelijkbaar met die van een node-in-a-box, of zelfs minder, omdat het gewoon een kwestie is van software installeren.



#### Bitcoin core (klant met ultrameerderheid)



[Bitcoin core is de ultra-majority client van het netwerk] (https://bitcoincore.org/). Het downloadt, valideert en onderhoudt de Blockchain, biedt RPC/REST API's en kan een Wallet integreren. Als je de voorkeur geeft aan standaard tools en je comfortabel voelt om zelf diensten toe te voegen (zoals Electrum server, verkenner en LND), dan kun je Core beter gebruiken zoals het is.



**Voordelen:** Maximale stabiliteit, voorspelbaar gedrag, ruwe ervaring, eenvoudig te installeren en te configureren.



**Nadelen:** Je moet de rest van de stack handmatig bouwen om een complete applicatie-omgeving te maken, in plaats van alleen een Bitcoin knooppunt.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

#### Bitcoin Knots (belangrijkste alternatieve klant)



[Bitcoin Knots is een Fork van Bitcoin core](https://bitcoinknots.org/), onderhouden door Luke Dashjr. Het is de belangrijkste alternatieve client voor Core voor het implementeren van het Bitcoin protocol. Het is volledig compatibel met de rest van het netwerk (het is in geen geval een Hard Fork zoals Bitcoin Cash), maar biedt desondanks extra mogelijkheden, inclusief opties voor het relaybeleid die in Core ontbreken, of standaard strenger worden toegepast om wat sommigen als spam beschouwen te beperken.



Er zijn 2 mogelijke redenen om Knots boven Core te kiezen:




- Technieken**: Andere opties dan Core, met name op het gebied van relaisbeheer, door te bepalen welke transacties worden geaccepteerd en uitgezonden door je knooppunt.
- Beleid**: Sommige mensen gebruiken alternatieve clients zoals Knots om niet-technische redenen, met name om een alternatief voor Core te ondersteunen en zo zijn monopolie te verkleinen. Als Core ooit gecompromitteerd zou worden, zou het niet alleen handig zijn om solide, goed onderhouden alternatieve clients te hebben, maar ook om te weten hoe deze effectief gebruikt kunnen worden. Anderen gebruiken Knots uit protest, omdat ze het vertrouwen in de ontwikkelaars van Core hebben verloren of het merendeel van het beheer van de client afkeuren.


https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Persoonlijk raad ik je aan om Core te kiezen, vooral om sneller te kunnen profiteren van beveiligingspatches. Sommige kwetsbaarheden die in Knots zijn ontdekt, worden namelijk met vertraging gecorrigeerd. Meer in het algemeen is het ontwikkelproces van Core goed gestructureerd en wordt het ondersteund door een groot aantal bijdragers, terwijl Knots wordt onderhouden door één persoon en een veel kleinere gemeenschap heeft. Aan de andere kant hebben relaisregels de neiging om vandaag de dag hun nut te verliezen, vooral als ze worden toegepast door slechts een klein deel van het netwerk (zoals percolatietheorie).



### Node-in-a-box distributies



De _node-in-a-box_ combineert Bitcoin core (of Knots) met een voorgeconfigureerd besturingssysteem, een Interface Web, en een App Store van zelf-hostende diensten (Lightning, explorers, Electrum server, Mempool, BTCPay Server, Nextcloud, etc.). Met slechts één klik kun je deze verschillende modules installeren, bijwerken en onderling verbinden.



Het is een veel eenvoudigere oplossing voor het dagelijks opstarten en beheren van talloze nevenapplicaties. Het nadeel is dat wanneer er een probleem optreedt (bijv. Docker image conflict, foutieve update, beschadigde database), het debuggen erg complex kan worden, omdat je afhankelijk bent van de eigen integratie van de distributie. Bovendien is community of officiële ondersteuning vaak ingewikkeld.



Een node-in-a-box is dus heel gemakkelijk te gebruiken zolang alles goed werkt, maar in het geval van een bug moet je bereid zijn om lang te zoeken, op hulp te wachten en je handen vuil te maken.



De meeste van deze oplossingen zijn verkrijgbaar in twee formaten:




- Voorgemonteerde machine: een volledige computer met het besturingssysteem al geïnstalleerd. Deze pay-as-you-go machines hoeven alleen maar op het lichtnet te worden aangesloten en met het internet te worden verbonden om operationeel te zijn. Als je budget het toelaat, heeft deze optie het voordeel dat ze heel eenvoudig op te zetten is, vaak prioritaire ondersteuning biedt en bijdraagt aan de financiering van de ontwikkeling, aangezien het bedrijfsmodel van deze bedrijven meestal gebaseerd is op de verkoop van hardware.
- Doe-het-zelf: installeer het distributiebesturingssysteem op je eigen machine (oude pc, NUC, Raspberry Pi, thuisserver...). Dit is de voordeligste oplossing, omdat je een oude machine kunt recyclen of hardware kunt kiezen die precies past bij je behoeften en budget. Het is ook de meest flexibele optie en de meest bevredigende om te configureren. Het is deze aanpak die we zullen verkennen in het praktische deel van de cursus.



Hier volgt een overzicht van de belangrijkste beschikbare node-in-a-box oplossingen (in 2025):



### Umbrel (umbrelOS & Umbrel Home)



[Vandaag de dag is Umbrel de leider in node-in-a-box oplossingen (https://umbrel.com/). Het succes is grotendeels te danken aan de eenvoud van de installatie (toen het werd gelanceerd op een eenvoudige Raspberry Pi), de elegante en intuïtieve Interface en een ecosysteem van toepassingen dat snel is gegroeid en nu zeer uitgebreid is.



![Image](assets/fr/067.webp)



Umbrel werd in 2020 gelanceerd als een eenvoudig Bitcoin knooppunt met een paar aanvullende toepassingen, maar heeft zich geleidelijk ontwikkeld tot een moderne cloud met alle functies.



Ik zal hier niet dieper ingaan op hoe het werkt en wat de specifieke mogelijkheden zijn, omdat we daar dieper op in zullen gaan in het eerste hoofdstuk van het volgende deel. Voor deze BTC 202 cursus heb ik ervoor gekozen om UmbrelOS te gebruiken, wat volgens mij de beste huidige node-in-a-box oplossing is voor beginnende en gemiddelde gebruikers.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

### Start9 (StartOS)



[Start9 biedt StartOS (https://start9.com/), een systeem dat is ontworpen voor "sovereign computing": het doel is dat iedereen zijn eigen privé-server kan bezitten en beheren, versterkt door een marktplaats van zelf gehoste applicaties. Je kunt een Start9 server kopen (Server One voor $619, Server Pure voor $899) of je eigen server samenstellen in DIY-modus op je eigen machine.



Aan de Bitcoin kant kun je met StartOS een Full node, een Lightning node, BTCPay Server, Electrs en vele andere diensten installeren. De aantrekkingskracht van Start9 gaat echter verder: het biedt de mogelijkheid om verschillende software (bestandscloud, messaging, monitoring) op een uniforme manier te ontdekken, configureren en bloot te stellen, met volledige controle. Het project is daarom gericht op gebruikers die een robuust self-hosting platform willen, niet alleen een eenvoudige Bitcoin node. Het is waarschijnlijk het meest complete ecosysteem na Umbrel.



![Image](assets/fr/068.webp)



Het grootste verschil met Umbrel zit in de Interface. Umbrel vertrouwt op een zeer gepolijste UX, terwijl Start9 een ruwere, meer functionele Interface biedt. Het applicatie-ecosysteem van Start9 is minder rijk dan dat van Umbrel, maar het compenseert dit met een aantal technische voordelen: de toegang tot geavanceerde applicatie-instellingen is vereenvoudigd, terwijl Umbrel al snel beperkend wordt als de gewenste optie niet wordt geleverd door de Interface. Start9 blinkt ook uit in back-upbeheer: behalve de efficiënte oplossing van Umbrel voor LND is er geen uniform mechanisme, in tegenstelling tot Start9. Bovendien biedt het meer toegankelijke bewakingstools en een versleutelde verbinding op afstand (`https`), terwijl lokale toegang tot Umbrel via `http` gaat.



Kortom, als je gewoon de essentiële toepassingen voor Bitcoin nodig hebt, zonder bijzondere interesse in het zeer rijke ecosysteem van Umbrel, en de Interface gebruiker is geen prioriteit, dan is Start9 een betere optie. Anders is Umbrel de betere keuze.



https://planb.network/tutorials/node/bitcoin/start9-8c8b6827-8423-4929-bcba-89057670ed6a

### MijnNode



[MyNode is een distributie die zich uitsluitend richt op Bitcoin en Lightning](https://mynodebtc.com/), en biedt een web Interface, een marktplaats voor toepassingen en upgrades met één klik. Je kunt kant-en-klare hardware kopen (*Model Two* verkrijgbaar voor $ 549) of MyNode gratis installeren op je eigen machine. Het project biedt ook een *Premium* versie van de software ($94), die ondersteuning met prioriteit en geavanceerde functies bevat.



![Image](assets/fr/069.webp)



In de praktijk brengt MyNode alle basisbouwstenen samen die nodig zijn om een Full node te laten werken, evenals de toepassingen die essentieel zijn voor Bitcoin gebruikers. Daarom is het een geschikte oplossing als je geen applicaties nodig hebt die buiten het Bitcoin ecosysteem vallen, zoals zelf gehoste apps die je kunt vinden in Start9 en Umbrel systemen.



https://planb.network/tutorials/node/bitcoin/mynode-a481fef3-2fd3-4df3-91c0-112cffa094eb

### RaspiBlitz



[RaspiBlitz is een 100% open source project](https://docs.raspiblitz.org/) (MIT-licentie) voor het monteren van een Bitcoin node en een Lightning node op een Raspberry Pi. Download het image, start het op en volg de wizard om een werkende node-in-a-box op je Raspberry Pi te krijgen. Voorgemonteerde kits zijn ook verkrijgbaar bij derde partijen, meestal tussen de $300 en $400, afhankelijk van de hardware. RaspiBlitz biedt ook een reeks aanvullende, eenvoudig te installeren applicaties.



![Image](assets/fr/070.webp)



Als je een Raspberry Pi hebt, is dit een uitstekende optie, aangezien meer complete systemen zoals Umbrel steeds zwaarder worden voor dit type mini-pc.



https://planb.network/tutorials/node/bitcoin/raspiblitz-d8cdba2e-a682-46cf-9fdc-d8602fbeac02

### RoninDojo



[RoninDojo is een privacy-gerichte node-in-a-box](https://wiki.ronindojo.io/en/home) die de inzet van Samurai Dojo en Whirlpool automatiseert, met een speciale Interface en plugins die speciaal zijn ontworpen voor het Samurai-ecosysteem.



Het principe is eenvoudig: als je Ashigaru Wallet gebruikt (de Fork opvolger van Samurai Wallet, na de arrestatie van de ontwikkelaars) of als je wilt profiteren van geavanceerde privacytools, dan is RoninDojo iets voor jou.



![Image](assets/fr/071.webp)



Het project bood eerder een voorgeconfigureerde machine genaamd de Tanto, maar deze is momenteel niet beschikbaar. Het is mogelijk dat deze op een later tijdstip terugkeert. In de tussentijd is het mogelijk om RoninDojo eenvoudig te installeren op een Rock5B+ of Rockpro64, of zelfs indirect op een Raspberry Pi.



https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

### Nodl



Een andere [node-in-a-box-oplossing is Nodl](https://www.nodl.eu/). Net als bij de vorige projecten kun je de voorgeconfigureerde hardware kopen (tussen €599 en €799, afhankelijk van het model) of zelf installeren.



Aan de softwarekant integreert Nodl Bitcoin core, LND, BTCPay Server, Electrs, Dojo, Whirlpool, Lightning Terminal, RTL, evenals BTC RPC Explorer, allemaal met een geïntegreerde updateketen en open-source code onder de MIT-licentie.



![Image](assets/fr/072.webp)



Na het verkennen van de verschillende softwareoplossingen is het nu tijd om de machine te kiezen die je node zal hosten!




## Overzicht van hardwareoplossingen


<chapterId>245d6add-9cda-46b9-9343-31dcdd70456e</chapterId>



Nu we alle softwaremogelijkheden hebben bekeken, gaan we ons richten op de hardware die nodig is voor je node. Ik zal je concreet advies geven over het kiezen van je componenten, samen met configuraties die passen bij verschillende budgetten. Natuurlijk is dit mijn persoonlijke mening en feedback: er zijn zeker andere relevante alternatieven naast de alternatieven die hier worden gepresenteerd. Verder ga ik niet in op de voorgemonteerde machines die worden aangeboden door node-in-a-box projecten, die we al hebben behandeld in het vorige hoofdstuk. Hier richten we ons uitsluitend op doe-het-zelf oplossingen.



### Heb je echt een speciale machine nodig?



De afgelopen jaren zijn bitcoiners zich steeds meer bewust geworden van een veelvoorkomende misvatting, vooral met de popularisering van node-in-a-box begin jaren 2020: een Bitcoin node moet noodzakelijkerwijs draaien op een machine die uitsluitend voor dit doel is bedoeld. Maar dit is niet waar. Je hebt niet per se een speciale computer nodig om een Bitcoin node te draaien: Bitcoin core kan prima op een gewone PC draaien. Als je voldoende schijfruimte hebt voor Blockchain of snoeien inschakelt, kun je de keten valideren, je Wallet aansluiten en zelfs het programma afsluiten als je klaar bent met het gebruik ervan. Het voordeel van deze aanpak is aanzienlijk: geen initiële investering en minimale complexiteit.



![Image](assets/fr/074.webp)



Dat gezegd hebbende, is het gebruik van een dedicated machine vaak comfortabeler. Deze kan continu draaien (24/7), altijd op afstand toegankelijk zijn, de bronnen van je hoofdmachine niet monopoliseren en, bovenal, het gebruik isoleren (een goede beveiligingspraktijk: als je persoonlijke PC een probleem ondervindt, blijft je node functioneren en vice versa). De vraag is dus niet "Moet ik een speciale machine hebben?", maar eerder "Heb ik een node nodig die constant online is, toegankelijk is voor andere apparaten en kan evolueren? Als het antwoord ja is, zal de keuze voor een aparte machine alles veel eenvoudiger maken.



### 3 aankoopmethoden: recycling, tweedehands en nieuw



#### Een oude pc recyclen



Het is de meest economische oplossing. De meesten van ons hebben thuis, of bij vrienden en familie, wel een oude PC staan die Dust verzamelt: dit is de perfecte gelegenheid om hem weer in gebruik te nemen! Om hem aan te passen voor gebruik als Bitcoin node, voeg je gewoon een 2TB SSD toe en, afhankelijk van je behoeften, vervang of voeg je RAM-bars toe om het RAM-geheugen te vergroten. Reken op een prijs tussen €100 en €200 voor een volledig functionele machine.



Controleer voordat je hardware aanschaft het aantal beschikbare schijfsleuven, het type aansluiting (M.2 of SATA), het RAM-formaat (SODIMM of DIMM) en de generatie (DDR4, enz.). Maak ook van de gelegenheid gebruik om de machine schoon te maken, vooral de ventilator, om optimale prestaties te garanderen.



Wees echter voorzichtig als je een laptop gebruikt: de batterij kan na verloop van tijd een probleem worden (meer hierover verderop in dit hoofdstuk).



#### Gereviseerd of gebruikt



De markt zit vol met gereviseerde zakelijke mini-pc's zoals *Lenovo ThinkCentre Tiny*, *HP EliteDesk Mini* of *Dell OptiPlex Micro*. Deze machines zijn solide, compact, stil en energiezuinig. Hun prijs ligt ver onder nieuw, en het is gemakkelijk om modellen te vinden die zijn uitgerust met 6e tot 10e generatie i5/i7 processors en 8 tot 16 GB RAM, allemaal voor zeer aantrekkelijke prijzen, over het algemeen tussen €70 en €200, afhankelijk van de configuratie. Naar mijn mening is dit waarschijnlijk de beste optie als je op zoek bent naar een dedicated machine voor je Bitcoin node.



![Image](assets/fr/075.webp)



Het is ook mogelijk om gebruikte pc's en laptops van een paar jaar geleden te vinden, met interessante configuraties en een uitstekende prijs-kwaliteitverhouding.



**Noot:** machines uit bedrijfswagenparken, zoals het *ThinkCentre Tiny*, zijn vaak alleen uitgerust met een *DisplayPort* (DP) poort voor het scherm, zonder HDMI-uitgang. Vergeet dus niet om een adapter of een DP-naar-HDMI kabel mee te nemen als je die nodig hebt.



#### Nieuw kopen



Als je budget het toelaat, kun je ook kiezen voor een nieuwe machine. Dit is een goede optie als je recente hardware met goede prestaties wilt hebben, vooral als je van plan bent om Umbrel of Start9 te gebruiken met aanvullende applicaties buiten het Bitcoin ecosysteem voor zelf-hosting.



### Welk type machine moet ik kiezen?



#### Mini-PC "NUC" / barebone



Mini-PC's bieden naar mijn mening het beste compromis om thuis een Bitcoin node te hosten. Ze zijn ruimtebesparend, passen gemakkelijk op een plank, verbruiken minimale stroom en lenen zich voor eenvoudige hardware-aanpassingen, zoals het toevoegen van RAM of het vervangen van de SSD.



Persoonlijk geef ik de voorkeur aan de *Lenovo ThinkCentre Tiny*, die zeer wijdverspreid is op de tweedehandsmarkt (van bedrijfswagenparken); ze zijn bijzonder robuust en gemakkelijk aan te passen. Er zijn natuurlijk veel equivalenten van andere fabrikanten: *Dell OptiPlex Micro*, *HP ProDesk / EliteDesk Mini / Micro*, *Intel NUC*, *Gigabyte BRIX*, *MSI Cubi*....



![Image](assets/fr/001.webp)



**Highlights:** kleine voetafdruk, matig stroomverbruik, laag geluidsniveau, schaalbaarheid (afhankelijk van model) en betrouwbaarheid.



**Zwakke punten:** iets duurder dan een Raspberry Pi-type SBC, geen ingebouwd scherm (toegang op afstand of via externe monitor), geen batterij (plotselinge uitschakeling bij stroomuitval).



#### Speciale laptop



Het is een uitstekend goedkoop alternatief voor de mini-pc: tegenwoordig kun je gebruikte of zelfs nieuwe laptops vinden tegen lage prijzen, uitgerust met fatsoenlijke processors, talloze poorten en een geïntegreerd scherm en toetsenbord (erg praktisch voor de eerste installatie). Bovendien werkt de batterij als een natuurlijke UPS: in het geval van een stroomstoring wordt het knooppunt niet abrupt uitgeschakeld en kan het zelfs enkele uren operationeel blijven.



![Image](assets/fr/076.webp)



**Highlights:** Alles-in-één oplossing, de batterij werkt als een UPS (geen black-outs), vereenvoudigde installatie dankzij een geïntegreerd scherm en toetsenbord, een geïntegreerde Wi-Fi-kaart en een ruime keuze aan gebruikte en nieuwe markten (wat vaak betekent dat je kunt onderhandelen over de prijzen).



**Zwakke punten:** iets hoger stroomverbruik dan een kale Mini-PC, geleidelijke slijtage van de batterij bij 24/7 gebruik met capaciteitsverlies, zeldzaam maar reëel risico van opzwellen van de batterij of thermal runaway bij het ouder worden. Het is vooral dit aspect waardoor ik de mini-PC een betere optie vind dan de laptop: de geleidelijke slijtage van de batterij en de bijbehorende risico's.



Als je voor deze oplossing kiest, raad ik je aan de conditie van de batterij goed in de gaten te houden om gevaar te voorkomen. Let op overmatige hitte, ongewone geuren, instabiliteit of een vervormd omhulsel. In het geval van een alarm, moet je de computer onmiddellijk uitschakelen en de stekker uit het stopcontact halen.



**Tip:** Als BIOS/UEFI of de tool van de fabrikant het toestaat, stel dan een belastingslimiet in (bijvoorbeeld 60% of 80%) om de levensduur van de batterij te verlengen.



#### Raspberry Pi en andere SBC's: het verkeerde idee



In het begin van de jaren 2020, met de opkomst van node-in-a-box software, kwam ook de Raspberry Pi rage op als een manier om een Bitcoin node te draaien. Het idee leek aantrekkelijk: goedkoop, compact en toegankelijk.



![Image](assets/fr/073.webp)



In de praktijk, als je doel alleen is om een Bitcoin node te draaien zonder extra toepassingen, kan een Raspberry Pi voldoende zijn. Maar zodra je Umbrel, Start9 of een rijker ecosysteem (Block explorer, Address indexer, Lightning node, zelf-hostende apps...) wilt gebruiken, bereikt de machine al snel zijn grenzen.



De Raspberry Pi heeft een aantal nadelen:




- processors die te slank zijn, met een ARM-architectuur die soms niet compatibel is met bepaalde software of meer handelingen vereist;
- Gesoldeerd RAM, onmogelijk te upgraden, met beperkte configuraties (vaak maximaal 8 GB);
- externe dozen voor SSD's die met een kabel zijn verbonden, frequente bronnen van bugs, waardoor de aanschaf van een specifieke kaart nodig is voor een stabiele SSD;
- de neiging om snel warm te worden en problemen met de juiste koeling;
- extra hardware moet aanschaffen (behuizing, ventilator, SSD-kaart, enz.);
- zeer beperkte connectiviteit.



Historisch gezien was het grote voordeel van SBC's zoals de Raspberry Pi hun prijs: voor enkele tientallen euro's kon je een speciale machine krijgen. Vandaag de dag zijn de prijzen echter sterk gestegen en als je alle essentiële extra hardware hebt toegevoegd, komen de kosten in de buurt van die van de eerste gebruikte of opgeknapte x86 mini-pc's, die naar mijn mening veel meer voordelen bieden. Daarom raad ik af om voor een SBC te kiezen.



### Componenten selecteren



#### Schijfopslag: SSD verplicht, minimaal 2 TB



Technisch gezien is het mogelijk om een Bitcoin node op een HDD te draaien. Het probleem is dat alles aanzienlijk langzamer zal gaan, vooral de IBD, die extreem lang zal worden door Bitcoin core's intensieve gebruik van de schijf als cache (vooral voor de UTXO set). Dit is de reden waarom ik het gebruik van een HDD sterk afraad: het creëert een echte bottleneck, beperkt de toekomstige evolutie ernstig (bijvoorbeeld voor een Lightning node) en kan zelfs leiden tot een synchronisatie mismatch met de Blockchain kop. Bovendien verhoogt de constante stress op de mechanische schijf het risico op vroegtijdige slijtage.



SSD's veranderen je gebruikerservaring radicaal: alles wordt sneller en soepeler, met een veel grotere betrouwbaarheid. Het gebruik van een SSD is daarom (bijna) verplicht voor je node, en je zult er geen spijt van krijgen, vooral omdat modellen met een hoge capaciteit nu relatief betaalbaar zijn.



![Image](assets/fr/077.webp)



Wat capaciteit betreft, wordt 2 TB geleidelijk het nieuwe redelijke minimum. In de zomer van 2025 nadert Blockchain al de 700 GB, en als je Umbrel, een Address indexer en een paar toepassingen toevoegt, zal een SSD van 1 TB snel verzadigd zijn. Met 2 TB heb je een comfortabele marge voor de komende jaren (in een brede schatting tussen 5 en 15 jaar). Je kunt ook kiezen voor 4TB als je van plan bent om veel applicaties te gebruiken op Umbrel, grote bestanden opslaat in self-hosting, of als je sterk wilt anticiperen op je behoefte aan schijfruimte.



![Image](assets/fr/078.webp)



Het formaat hangt af van de beschikbare poorten op je machine, maar indien mogelijk raad ik aan om een NVMe M.2 SSD te gebruiken.



#### Geheugen (RAM): 8 tot 16 GB



Voor Bitcoin core alleen (zonder Umbrel overlay), geven de aanbevelingen van de ontwikkelaar een minimum van 256 MB RAM aan met instellingen aangepast aan de laagste instelling, 512 MB met standaardinstellingen en 1 GB voor normaal gebruik.



Aan de andere kant, als je een node-in-a-box systeem zoals Umbrel of Start9 gebruikt, zijn de RAM vereisten aanzienlijk hoger. De ontwikkelaars van Umbrel raden minimaal 4 GB RAM aan. Dit kan genoeg zijn om alleen Core te draaien, maar je zult al snel beperkt zijn. Ze raden daarom 8 GB aan, wat ik ook beschouw als het minimum voor een basisconfiguratie rond Bitcoin (Core, LND, indexer en een paar applicaties). In mijn ervaring, met Umbrel en een paar extra diensten, is 8 GB nog steeds een beetje krap. Om echt comfortabel te zijn en wat marge te hebben, zou ik 16 GB RAM aanraden.



#### Processor (CPU)



Voor een Umbrel node is de minimale vereiste een dual-core 64-bit processor van Intel of AMD. Als je naast Bitcoin core nog een paar andere toepassingen wilt gebruiken, zal een quad-core (of hoger) echt een verschil maken in de vloeiendheid. Processoren van de 6e tot 10e generatie i5/i7 zijn bijvoorbeeld uitstekende opties op de tweedehandsmarkt.



### Voorbeelden van concrete configuraties



Hieronder stel ik drie concrete configuraties voor, aangepast aan verschillende budgetten en behoeften, met precieze modellen om ze te ondersteunen. Deze keuzes worden als voorbeeld gegeven om de informatie in dit hoofdstuk te illustreren; u bent niet verplicht om precies deze modellen te kiezen. Omdat ik van mening ben dat de Mini-PC op de lange termijn de beste optie is, zal ik dit formaat gebruiken voor de drie voorgestelde configuraties.



*Onderstaande prijzen zijn slechts indicatief en kunnen per regio, verkoper en periode verschillen*



Eerst en vooral heb je een SSD nodig die groot genoeg is om de Blockchain te huisvesten, terwijl er nog steeds manoeuvreerruimte overblijft. SSD's hebben een beperkte levensduur als het gaat om schrijfcycli en het totale volume aan gegevens dat wordt geschreven. Een Bitcoin node belast de schijf echter aanzienlijk bij het schrijven. Daarom raad ik de instapmodellen niet aan; in plaats daarvan stel ik een NVMe SSD voor, die aanzienlijk betere prestaties biedt.



Als voorbeeld voor deze cursus heb ik het volgende model gekozen: *Samsung 990 EVO Plus NVMe M.2 SSD 2Tb*, verkrijgbaar voor ongeveer €120 op Amazon. Je kunt ook kiezen voor andere bekende merken zoals Crucial, Western Digital of Kingston.



![Image](assets/fr/046.webp)



#### Low-budget configuratie



Als je budget erg beperkt is (minder dan €200), raad ik je natuurlijk aan niet te investeren in een speciale machine, maar Bitcoin core direct op je gewone PC te installeren (in pruned modus als je weinig schijfruimte hebt).



Voor een klein budget raad ik de *HP EliteDesk 800 G2 Mini* aan. Ik vond een refurbished model voor €96 op Amazon, uitgerust met een 6e generatie Intel Core i5 processor en 8 GB RAM. Dit is een bijzonder interessante optie voor beginners: deze processor en deze hoeveelheid geheugen zijn meer dan genoeg om Core op Umbrel te draaien, evenals meerdere applicaties tegelijk, zoals een Electrs indexer, een Lightning node en een Mempool instance, op voorwaarde dat je niet te veel cache aan Core toekent. Bovendien is het met dit type mini-pc eenvoudig om het RAM-geheugen uit te breiden naar bijvoorbeeld 16 GB, mocht dat nodig zijn (reken op ongeveer €30-40 extra voor één of twee kwaliteitsgeheugensticks).



![Image](assets/fr/045.webp)



Voeg dan gewoon de SSD toe aan het budget. Beginnend met de Samsung 2TB van €120, komen we op een totale kostprijs van €216 voor een complete, functionele machine.



#### Configuratie met gemiddeld budget



Als je een gemiddeld budget hebt van rond de €300 voor de machine die je node zal hosten, raad ik je bijvoorbeeld een *Lenovo ThinkCentre Tiny* aan, uitgerust met een krachtige processor en voldoende RAM. Ik vond een refurbished model op Amazon voor €180, met een 6e generatie Intel Core i7 processor en 16GB RAM. Met de 2TB SSD erbij voor €120, komen de totale kosten op €300.



![Image](assets/fr/044.webp)



Met deze machine heb je een comfortabele configuratie: een snelle IBD en de mogelijkheid om zonder problemen talloze toepassingen op je Umbrel of Start9 te draaien. Dit is precies de configuratie die ik gebruik voor deze BTC 202-cursus.



#### High-end configuratie



Met een groter budget worden de mogelijkheden aanzienlijk groter. Je kunt kiezen voor een doe-het-zelfconfiguratie of zelfs voor een voorgemonteerde machine die rechtstreeks wordt aangeboden door een node-in-a-box project.



De *ASUS NUC 14 Pro* is bijvoorbeeld nieuw verkrijgbaar bij Amazon voor €540. Voor deze prijs krijg je een Intel Core Ultra 5 processor (recent en bijzonder krachtig), vergezeld van 16 GB DDR5 RAM. Met zo'n configuratie kun je een IBD in recordtijd voltooien en probleemloos veeleisende toepassingen installeren.



Dit is een extreem comfortabele configuratie, zelfs overkill als het aanvankelijke doel eenvoudigweg is om een Bitcoin node te draaien. Aan de andere kant, als je ten volle wilt profiteren van alle zelf-hostende toepassingen die beschikbaar zijn op Umbrel en Start9, dan is dit vermogensniveau precies goed voor jou.



![Image](assets/fr/043.webp)



Afhankelijk van je beoogde gebruik kun je kiezen voor een 2TB SSD, zoals in de andere configuraties, of direct voor een 4TB SSD voor €260 als je ook persoonlijke bestanden wilt opslaan en je self-hosting gebruik wilt uitbreiden. Met een 2TB SSD bedragen de totale kosten van de configuratie €660, terwijl dit met een 4TB SSD €800 is.



### Nog een paar tips





- Als je tweedehands apparatuur wilt kopen en in bitcoins wilt betalen, kom dan naar een meetup bij jou in de buurt! Door met andere deelnemers te praten, vind je zeker geschikte apparatuur voor een goede prijs, terwijl je helpt om de circulaire economie rond Bitcoin levend te houden. Het is ook een kans om te profiteren van goed advies uit de community.





- Voor de internetverbinding heb je natuurlijk een RJ45 Ethernetkabel nodig, tenminste voor de installatie van het systeem.





- Sommige omgevingen, zoals Umbrel, staan je dan toe om Wi-Fi te gebruiken, maar de prestaties zullen over het algemeen slechter zijn (vooral als je je Lightning-node op afstand wilt gebruiken, want dat kan invloed hebben). Als je kiest voor Wi-Fi, zorg er dan voor dat je machine een ingebouwde kaart heeft of voeg een compatibele dongle toe.





- Gebruik altijd de originele Supply voeding van de fabrikant voor uw machine. Dit is cruciaal om schade aan uw apparatuur te voorkomen en het risico op brand te vermijden.





- Als je machine geen ingebouwde accu heeft, is het een goed idee om te investeren in een omvormer om plotseling uitschakelen te voorkomen.





- Afhankelijk van de waarde van je apparatuur en je geografische locatie kan een bliksemafleider ook geschikt zijn, hetzij direct op het schakelbord of op de gebruikte stekkerdoos.





- Vergeet tot slot niet om de koeling van je machine te optimaliseren: maak hem regelmatig schoon en installeer hem op een koele, goed geventileerde, onoverzichtelijke plek om oververhitting te voorkomen, wat kan leiden tot throttling (vrijwillige beperking van de snelheid van je processor).



# Eenvoudig een Bitcoin knooppunt installeren


<partId>ca6cf2a5-0bcc-41d9-b556-0d38865bf98f</partId>




## Umbrel: veel meer dan een Bitcoin knooppunt


<chapterId>dd4c04f1-924a-43e1-94f3-ea9fbc83dd43</chapterId>



Umbrel is een persoonlijk serverbesturingssysteem ontworpen om zelf-hosting toegankelijk te maken: je installeert Umbrel, opent een browser op `umbrel.local`, en beheert alles via een eenvoudige Interface op afstand.



Het project populariseerde eerst het idee van een Bitcoin- en Lightning-knooppunt met één klik en breidde daarna uit tot een echte "thuiswolk": bestands- en foto-opslag, multimediastreaming, netwerktools, domotica, lokale AI en honderden apps die geïnstalleerd kunnen worden vanuit een geïntegreerde App Store.



In Umbrel draait elke applicatie in een Docker container (isolatie, atomaire updates, onafhankelijke start/stop). De Interface centraliseert de toegang tot al deze apps en biedt single sign-on (met optioneel 2FA), one-click updates voor OS en apps, live monitoring van de machine (CPU, RAM, temperatuur, opslag), rechtenbeheer tussen apps en een overzicht van hun verbruik.



Het doel van Umbrel is dan ook om u de controle en vertrouwelijkheid over uw gegevens terug te geven, zonder afhankelijk te zijn van cloud-diensten, buiten het simpelweg bedienen van een Bitcoin node.



### Umbrel Home vs umbrelOS



Umbrel biedt twee verschillende benaderingen:





- [**Umbrel Home**](https://umbrel.com/umbrel-home): dit is een gebruiksklare miniserver, speciaal ontworpen en geoptimaliseerd voor umbrelOS. Hij is compact, stil, heeft een ethernetverbinding en is uitgerust met een NVMe SSD (optioneel tot 4TB), 16GB RAM en een quad-core CPU. Je bestelt hem, sluit hem aan en gaat naar `umbrel.local`. Je kunt binnen enkele minuten een operationele Umbrel hebben. Dat is de plug-and-play optie.



![Image](assets/fr/081.webp)





- [**umbrelOS**](https://umbrel.com/umbrelos): dit is het besturingssysteem dat je zelf kunt installeren op je eigen hardware (mini-PC, NUC, tower, dedicated laptop...). Je hebt dezelfde Interface en dezelfde App Store als op Umbrel Home.



![Image](assets/fr/080.webp)



In beide gevallen is de gebruikerservaring aan de softwarekant identiek: browsergebaseerd beheer, updates met één klik, applicatie-installatie op aanvraag... De doe-het-zelf oplossing is vaak voordeliger dan het kopen van een Umbrel Home (afhankelijk van de gebruikte machine). Ik zou je echter niet per se aanraden om altijd voor de doe-het-zelf optie te kiezen, want **een Umbrel Home kopen draagt direct bij aan de financiering van de ontwikkeling van het project**, omdat het bedrijfsmodel gebaseerd is op de verkoop van hardware. En eerlijk gezegd, met €389 voor 2TB aan opslag blijft de prijs zeer redelijk gezien de kwaliteit van de aangeboden machine.



![Image](assets/fr/079.webp)



In het volgende hoofdstuk gaan we kijken hoe je umbrelOS DIY op je eigen machine kunt installeren. U kunt deze BTC 202-cursus echter op dezelfde manier volgen als u voor een Umbrel Home hebt gekozen.



### Gebruikssituatie: van het Bitcoin knooppunt naar de thuiscloud



Umbrel kan heel minimalistisch blijven en zich alleen richten op Bitcoin, of evolueren naar een echte multifunctionele persoonlijke server, afhankelijk van je behoeften. Dit zijn de belangrijkste gebruiksmogelijkheden van Umbrel:





- Eenvoudig Bitcoin knooppunt**: dit is het eerste gebruik waarop Umbrel vanaf het begin heeft vertrouwd. Je kunt Bitcoin core (of Knots) draaien, je wallets direct op je node aansluiten, een Electrum server ontsluiten, je Mempool Block explorer hosten om de Blockchain te bekijken, en kosten schatten... Het zijn deze toepassingen waar we ons in deze cursus op zullen richten.



![Image](assets/fr/082.webp)





- Lightning Network**: Umbrel laat je ook LND of Core Lightning, twee implementaties van de Lightning Network, inzetten om je eigen Lightning node te beheren. Je zult in staat zijn om kanalen te openen, je liquiditeit te beheren, betalingen te doen, balancering te automatiseren, diensten aan te bieden, een Wallet op afstand aan te sluiten of te profiteren van geavanceerd Interface beheer dankzij de vele beschikbare toepassingen. We bekijken deze specifieke use case in onze volgende LNP 202 cursus.



![Image](assets/fr/083.webp)





- Algemene zelf-hosting**: met Nextcloud, Immich, Jellyfin/Plex, DNS-brede advertentieblokkers (Pi-hole/AdGuard), VPN's (WireGuard, Tailscale), domotica (Home Assistant), back-ups, notitiebeheer, kantoortools, lokale AI (Ollama + Open WebUI)... Umbrel kan je persoonlijke server worden, zodat je weer controle hebt over je gegevens. Je host de diensten die je elke dag gebruikt zelf, met een gepolijste gebruikerservaring die sterk lijkt op externe oplossingen, terwijl je de volledige controle behoudt over je gegevens en privacy.



Door applicaties in containers te implementeren, kun je Umbrel vormgeven zoals jij dat wilt: begin met een eenvoudige Bitcoin node en een paar apps die gekoppeld zijn aan zijn ecosysteem, installeer dan een Lightning node naast je Bitcoin node, en verrijk je instantie geleidelijk met de zelf-hostende applicaties die je nodig hebt.



### Gemeenschap en wederzijdse hulp



Een van de belangrijkste voordelen van Umbrel ten opzichte van de concurrentie is de enorme en zeer actieve gebruikersgemeenschap. Je kunt ze voornamelijk bereiken via [hun Discord](https://discord.gg/efNtFzqtdx) en [hun online forum](https://community.umbrel.com/). Hier vind je niet alleen praktisch advies, maar vooral oplossingen om problemen op te lossen of bugs te repareren. Het is een geweldige plek om te beginnen, vooruitgang te boeken en uiteindelijk andere gebruikers te helpen, zodat je niet alleen achterblijft met je Coin.



![Image](assets/fr/084.webp)



### Licentie UmbrelOS



Umbrel's code is openbaar beschikbaar (je kunt het bekijken, Fork, en aanpassen), maar het valt niet onder een echte open-source licentie. In feite wordt umbrelOS gedistribueerd onder de [*PolyForm Noncommercial 1.0*] licentie (https://polyformproject.org/licenses/noncommercial/1.0.0/), hoewel sommige bijbehorende ontwikkeltools beschikbaar zijn onder de MIT licentie.



Praktisch gezien kun je zo'n beetje alles doen met umbrelOS wat je wilt, zolang het maar voor persoonlijk, niet-commercieel gebruik is: modificatie, herdistributie voor non-profit doeleinden, het maken van afgeleiden voor jezelf of voor non-profit organisaties, op voorwaarde dat je de wettelijke vermeldingen respecteert.



Het is echter verboden om Umbrel of afgeleiden daarvan (bijvoorbeeld een voorgemonteerde machine met umbrelOS voorgeïnstalleerd) te verkopen, Umbrel-gerelateerde diensten commercieel aan te bieden of de code ervan met winstoogmerk in een product te integreren.



Technisch gezien beperkt deze licentie niet de installatie, controle of aanpassing van Umbrel voor persoonlijk gebruik. Juridisch gezien beschermt het project tegen ongeoorloofde wederverkoop of commerciële hosting, met name door cloud providers. Umbrel is daarom niet open source, hoewel de code openbaar toegankelijk blijft.



Elke toepassing in de Store behoudt echter zijn eigen licentie, vaak open source.




## Een Full node met paraplu installeren


<chapterId>61bc09c7-787d-4649-b142-457ec018b0f4</chapterId>



Nu we alle benodigde informatie hebben, is het tijd om in de details te duiken. In deze tutorial laten we zien hoe je een compleet Bitcoin knooppunt installeert met UmbrelOS.



### Benodigde materialen



Hier gebruiken we het UmbrelOS x86 image (meer precies, de x86_64 versie). Je kunt deze handleiding volgen op elke machine die je kiest, zolang deze niet is uitgerust met een ARM-architectuur processor (geen Apple Silicon, Raspberry Pi, etc.). Dit betekent dat elke computer met een Intel of AMD 64-bits processor volstaat, zolang deze voldoet aan de minimale vereisten, afhankelijk van hoe je je Umbrel wilt gebruiken (ten minste een dual-core processor wordt aanbevolen).



Als je hebt gekozen voor een Raspberry Pi 5 (een optie die ik niet aanraad, zoals vermeld in de vorige sectie), dan is de installatie iets anders. Je kunt dan deze speciale tutorial volgen en terugkeren naar mijn cursus op het Interface web `http://umbrel.local`:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Zoals vermeld in de vorige sectie, heb ik ervoor gekozen om deze tutorial te draaien op een kleine refurbished PC die ik voor een goede prijs vond: een *Lenovo ThinkCentre M900 Tiny* uitgerust met een Intel Core i7 processor en 16 GB RAM. Dit is een erg comfortabele configuratie voor het draaien van Umbrel, vooral voor een Bitcoin node. Ik heb echter voor deze configuratie gekozen omdat ik later een Lightning node en andere veeleisende toepassingen wil installeren. Ik heb ook een 2TB SSD toegevoegd aan mijn ThinkCentre om de volledige Blockchain te behouden en nog steeds een comfortabele marge te hebben. Met deze configuratie zijn de totale kosten €270, inclusief alle kosten.



![Image](assets/fr/001.webp)



Ik ben vooral dol op de ThinkCentre Tiny-serie van Lenovo, omdat het compacte, stille en zeer robuuste machines zijn. Deze computers zijn erg populair bij bedrijven en zijn daarom overvloedig aanwezig op de tweedehandsmarkt, waar je interessante configuraties kunt vinden tussen €70 en €200.



Als je, zoals ik, hebt gekozen voor een pc zonder monitor, **moet je alleen voor de duur van de installatie een monitor en toetsenbord** aansluiten. Daarna heb je toegang op afstand vanaf een andere computer in hetzelfde netwerk (of via andere methoden die we in latere hoofdstukken behandelen). Je hebt ook een RJ45 Ethernetkabel nodig om je machine aan te sluiten op het lokale netwerk en een USB-sleutel van minstens 4 GB om het installatie-image op te slaan.



Dit zijn de vereisten voor de uitrusting:




- Computer met x86_64-processor (minimaal Dual-core, aanbevolen Quad-core);
- RAM-geheugen (minimaal 4 GB, 8 GB aanbevolen of meer voor langdurig gebruik);
- SSD (aanbevolen + 2 TB);
- USB-sleutel (+ 4 GB) voor installatie van UmbrelOS-image;
- Monitor en toetsenbord (alleen handig voor de eerste installatie als de pc er geen heeft);
- RJ45 Ethernetkabel.



### Stap 1 - De computer monteren



Afhankelijk van de hardware die je hebt gekozen, is de eerste stap het monteren van de verschillende onderdelen van je computer. In mijn geval had de originele SSD bijvoorbeeld een capaciteit van slechts 256 GB, dus die ga ik recyclen voor een ander gebruik en vervangen door een SSD van 2 TB. Als je ook de RAM-modules wilt vervangen, is dit het moment om dat te doen.



### Stap 2: Een opstartbare USB-sleutel voorbereiden



Voordat u UmbrelOS op uw machine installeert, moet u een opstartbare USB-sleutel maken die het besturingssysteem bevat. Alle stappen in stap 2 moeten worden uitgevoerd op uw eigen computer (en niet direct op de computer die uw node wordt).





- Begin met het downloaden van de nieuwste versie van UmbrelOS in USB-formaat:



Ga naar [de officiële Umbrel website om het ISO-image te downloaden](https://download.umbrel.com/release/latest/umbrelos-amd64-usb-installer.iso) voor installatie via een USB-sleutel. Zorg ervoor dat je de versie selecteert die compatibel is met de x86_64 architectuur (bestand met de naam `umbrelos-amd64-usb-installer.iso`). Het downloaden kan even duren, omdat de image vrij groot is.



![Image](assets/fr/002.webp)





- Installeer Balena Etcher:



Om de opstartbare USB-stick te maken, gebruik je een eenvoudig, platformonafhankelijk hulpprogramma genaamd [Balena Etcher] (https://www.balena.io/etcher/). Download en installeer het op je computer.



![Image](assets/fr/003.webp)





- Plaats een lege USB-sleutel van minstens 4 GB:



Steek een USB-sleutel in je computer (degene waarop je zojuist het UmbrelOS en Balena Etcher image hebt gedownload). **Waarschuwing: alle gegevens op de sleutel worden verwijderd**. Zorg ervoor dat er geen belangrijke bestanden op staan.





- Brand de ISO-image op de USB-stick met Balena Etcher:



Start Balena Etcher en selecteer het `umbrelos-amd64-usb-installer.iso` ISO-bestand dat je zojuist hebt gedownload door op de knop "*Flash from file*" te klikken. Selecteer vervolgens de USB-sleutel als doelapparaat en klik op "*Flash!*" om te beginnen met schrijven.



![Image](assets/fr/004.webp)



Zodra de bewerking voltooid is, hebt u een opstartbare USB-sleutel met UmbrelOS, klaar om op te starten en Umbrel op uw machine te installeren.



![Image](assets/fr/005.webp)



### Stap 3: De computer opstarten vanaf de USB-stick



Nu uw opstartbare USB-stick met UmbrelOS klaar is, kunt u uw computer erop opstarten om de systeeminstallatie te starten. Haal de USB-stick uit uw hoofdcomputer en steek deze in het apparaat waarop u Umbrel en uw Bitcoin knooppunt wilt installeren.



Zoals uitgelegd aan het begin van dit hoofdstuk, heb je een beeldscherm en een invoerapparaat nodig om de installatie te voltooien. Sluit een beeldscherm aan via HDMI (of een andere poort, afhankelijk van uw PC) en sluit een toetsenbord aan via USB op uw machine. Deze apparaten zijn alleen nodig voor de installatie; je hebt ze daarna niet meer nodig, omdat Umbrel op afstand toegankelijk is vanaf een andere computer. Sluit deze twee apparaten aan op uw pc.



**Tip:** Als je thuis geen randscherm hebt, kun je je tv gebruiken. Met zijn HDMI-ingang (of een andere ingang) kan hij worden gebruikt als tijdelijk scherm terwijl je het besturingssysteem installeert.



Umbrel heeft uiteraard een internetverbinding nodig. Sluit de RJ45 Ethernetkabel aan tussen je apparaat en je router.



![Image](assets/fr/006.webp)



Zet je machine aan. In de meeste gevallen wordt de USB-sleutel automatisch gedetecteerd en wordt er van opgestart. Je ziet dan het UmbrelOS Interface installatiescherm verschijnen.



Als het apparaat opstart op een ander systeem of een foutmelding geeft, betekent dit waarschijnlijk dat het niet automatisch opstart vanaf de USB-stick. Start in dit geval opnieuw op en ga naar de BIOS/UEFI-instellingen (meestal toegankelijk door op `DEL`, `F2`, `F12` of `ESC` te drukken, afhankelijk van de computerfabrikant). Wijzig vervolgens de opstartvolgorde om prioriteit te geven aan de USB-sleutel. Start vervolgens het apparaat opnieuw op om UmbrelOS te starten.



### Stap 4: Installeer UmbrelOS op uw computer



Zodra het apparaat is opgestart vanaf de USB-stick, wordt u begroet door de Interface UmbrelOS installatie. In deze stap wordt het systeem direct op de interne Hard schijf van de machine geïnstalleerd.



Het scherm dat verschijnt geeft een lijst weer van alle interne opslagapparaten die door de computer zijn gedetecteerd. Bij elke schijf staat een nummer, een naam en een opslagcapaciteit. Zoek de schijf waarop u Umbrel wilt installeren. **Waarschuwing: alle bestanden op deze schijf worden permanent verwijderd.**



![Image](assets/fr/007.webp)



Als je eenmaal de juiste schijf hebt geïdentificeerd (meestal de schijf met de grootste capaciteit voor de Blockchain), noteer dan het nummer dat eraan is toegewezen. Als de schijf die je hebt gekozen bijvoorbeeld onder het nummer `2` verschijnt, voer dan gewoon `2` in en druk vervolgens op de `Enter` toets op het toetsenbord.



![Image](assets/fr/008.webp)



Het programma zal de geselecteerde schijf formatteren, UmbrelOS installeren en het systeem automatisch configureren. Dit kan enkele minuten duren. Laat het proces zonder onderbreking verlopen.



![Image](assets/fr/009.webp)



Wanneer de installatie voltooid is, wordt u gevraagd om het apparaat uit te schakelen. Druk op een willekeurige toets om de computer uit te schakelen.



![Image](assets/fr/010.webp)



U kunt nu de USB-stekker, het toetsenbord en het scherm verwijderen, omdat deze niet langer nodig zijn voor uw Umbrel. Het enige dat overblijft van je knooppunt is de Supply en de RJ45 Ethernetkabel.



![Image](assets/fr/011.webp)



Controleer de volgende twee punten voordat u het apparaat opnieuw opstart:





- De USB-stekker is losgekoppeld**: als deze aangesloten blijft, kan het systeem hierop herstarten in plaats van op de interne schijf;
- Ethernetkabel is aangesloten**: het apparaat moet verbonden zijn met je router om te kunnen werken.



Druk op de aan/uit-knop. Het systeem start automatisch op vanaf de interne schijf waarop UmbrelOS werd geïnstalleerd. De eerste keer opstarten kan ongeveer **5 minuten** duren. Gedurende deze tijd initialiseert Umbrel haar diensten en Interface.



Open vanaf een andere computer (uw gewone pc) die is aangesloten op hetzelfde lokale netwerk**, een webbrowser (Firefox, Chrome...) en ga naar:



```
http://umbrel.local
```



Deze Address wordt gebruikt om op afstand toegang te krijgen tot de Umbrel Interface grafische gebruiker Interface en te beginnen met de configuratie.



Als de Address `http://umbrel.local` niet werkt op je browser na minstens 5 minuten wachten, probeer het dan gewoon:



```
http://umbrel
```



Als dit nog steeds niet werkt, voer dan het lokale IP Address van uw Umbrel rechtstreeks in de browser in. Bijvoorbeeld (vervang `42` door het nummer van uw machine die Umbrel host op het lokale netwerk):



```
http://192.168.1.42
```



Om de IP Address van uw Umbrel te identificeren, zijn er verschillende methoden, van de eenvoudigste tot de meest geavanceerde:





- Ga naar de Interface administratie van uw router en zoek het IP Address van het Umbrel-apparaat op het lokale netwerk.





- Gebruik netwerkscansoftware zoals Angry IP Scanner om aangesloten apparaten te detecteren en de IP Address van uw Umbrel te lokaliseren.



![Image](assets/fr/012.webp)



https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d



- Als laatste redmiddel sluit je opnieuw een monitor en toetsenbord aan op het apparaat, log je in (standaard login: `umbrel`, wachtwoord: `umbrel`) en typ je het volgende commando:



```
hostname -I
```



Nu ben je klaar om Umbrel te gebruiken!



### Stap 5: Aan de slag met Umbrel



Om te beginnen met het configureren van uw Umbrel, klikt u op de knop "*Start*".



![Image](assets/fr/013.webp)



#### Een account aanmaken



Kies een pseudoniem of voer uw naam in en stel dan een sterk wachtwoord in. Wees voorzichtig: dit wachtwoord is de enige barrière voor toegang tot uw Umbrel vanaf uw netwerk (en dus mogelijk ook tot uw bitcoins als u een Lightning-node op Umbrel draait). Het beschermt ook toegang op afstand via Tor of VPN, als deze diensten zijn ingeschakeld.



Kies een sterk wachtwoord en zorg ervoor dat je minstens één back-up bijhoudt (een wachtwoordmanager wordt aanbevolen).



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Zodra je je wachtwoord hebt ingevoerd, klik je op de knop "*Create*".



![Image](assets/fr/014.webp)



Uw Umbrel-configuratie is nu voltooid.



![Image](assets/fr/015.webp)



#### Ontdekking van Interface



De Interface van Umbrel is behoorlijk intuïtief:





- Op de startpagina kun je je geïnstalleerde applicaties en widgets bekijken.



![Image](assets/fr/016.webp)





- In de "*App Store*" kun je nieuwe applicaties installeren,



![Image](assets/fr/017.webp)





- Het menu "*Bestanden*" centraliseert alle documenten die op uw Umbrel zijn opgeslagen.



![Image](assets/fr/018.webp)





- In het menu "*Instellingen*" kunt u de instellingen van uw Umbrel wijzigen en informatie opvragen, zoals:
    - Update, herstart of stop je machine;
    - Raadpleeg de beschikbare opslagruimte, het RAM-gebruik en de temperatuur van de processor;
    - Verander de achtergrond;
    - Beheer toegang op afstand via Tor, activeer Wi-Fi of 2FA.



![Image](assets/fr/019.webp)



#### Beveiliging en verbindingsinstellingen



Eerst en vooral raad ik sterk aan om twee-factor authenticatie (2FA) in te schakelen. Dit voegt een extra Layer beveiliging toe aan je wachtwoord. Het is bijna onmisbaar als je van plan bent om je Umbrel te gebruiken om persoonlijke bestanden op te slaan, een Lightning node te draaien of andere gevoelige activiteiten uit te voeren.



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Klik hiervoor op het overeenkomstige vakje in de instellingen.



![Image](assets/fr/020.webp)



Scan vervolgens de QR-code die wordt weergegeven met uw verificatietoepassing. Voer vervolgens de 6-cijferige dynamische code in het daarvoor bestemde veld op uw Umbrel in.



Vanaf nu vereist elke nieuwe verbinding met je Umbrel zowel het wachtwoord als de 6-cijferige code die wordt gegenereerd door je twee-factor authenticatie (2FA) applicatie.



![Image](assets/fr/021.webp)



Wat betreft toegang op afstand via Tor, als je het niet nodig hebt, raad ik aan om deze optie uit te schakelen om het aanvalsoppervlak van je Umbrel te beperken. Standaard is je knooppunt alleen toegankelijk vanaf een machine die verbonden is met hetzelfde lokale netwerk. Als je toegang via Tor inschakelt, kun je je Umbrel toch onderweg beheren.



Als je deze functie inschakelt, wordt het theoretisch mogelijk voor elke machine in de wereld om een verbinding met jouw node te proberen, mits het de Tor Address kent. Je wachtwoord en 2FA zullen je echter nog steeds beschermen.



Als je deze optie activeert, zorg er dan voor dat je twee-factor authenticatie (2FA) hebt ingeschakeld, een sterk wachtwoord hebt en nooit je Tor-verbinding Address onthult.



Voer gewoon deze Tor Address in je Tor browser in om toegang te krijgen tot Umbrel's Interface vanaf elk netwerk.



![Image](assets/fr/026.webp)



Tot slot kunt u op deze instellingenpagina ook de Wi-Fi-verbinding activeren. Als uw machine die Umbrel host een Wi-Fi-netwerkkaart of een Wi-Fi-dongle heeft, kunt u hiermee toegang krijgen tot het internet zonder de RJ45-kabel te gebruiken. Afhankelijk van je configuratie kan deze oplossing echter de verbinding vertragen, wat invloed kan hebben op de initiële synchronisatie (IBD) en toekomstig gebruik van het knooppunt (bijvoorbeeld voor Lightning-transacties). Persoonlijk raad ik deze optie niet aan, omdat een knooppunt niet bedoeld is voor mobiel gebruik: het wordt altijd op afstand benaderd, dus je kunt het net zo goed aangesloten laten.



### Stap 6: Installeer een Bitcoin knooppunt op Umbrel



Nu UmbrelOS correct geïnstalleerd en geconfigureerd is op uw machine, kunt u verder gaan met de installatie van uw Bitcoin node. Niets is eenvoudiger: ga naar de App Store, open de categorie "*Bitcoin*" en selecteer dan de applicatie "*Bitcoin Node*" (het is eigenlijk Bitcoin core).



![Image](assets/fr/022.webp)



Klik vervolgens op de knop "*Installeren*".



![Image](assets/fr/023.webp)



Zodra de installatie is voltooid, zal uw Bitcoin node zijn IBD (*Initial Block Download*) starten: het zal alle transacties en blokken downloaden en valideren sinds Bitcoin werd opgericht in 2009.



![Image](assets/fr/024.webp)



Deze fase is bijzonder tijdrovend, omdat de duur afhangt van verschillende factoren, waaronder de hoeveelheid RAM die is toegewezen aan de cache van het knooppunt, de snelheid van de schijf, de snelheid van de internetverbinding en de kracht van de processor. Het bereik van de duur is daarom erg groot, afhankelijk van de configuratie. Met een krachtige pc (NVMe SSD, +32 GB RAM, krachtige processor en goede internetverbinding) kan IBD in ongeveer tien uur voltooid worden. Aan de andere kant kan een oude processor, weinig RAM of, nog erger, een mechanische Hard schijf (sterk afgeraden) deze operatie verlengen tot enkele weken.



Met een pc met een normale configuratie (een fatsoenlijke processor, 8 tot 16 GB RAM en een SSD) kun je ongeveer 2 tot 7 dagen werken.



Om IBD iets te versnellen, kun je het RAM-geheugen dat is toegewezen aan de node-cache (die voornamelijk wordt gebruikt voor de UTXO set, waar we later in de cursus op terug zullen komen) verhogen via de `dbcache` parameter. Op Umbrel wordt deze wijziging aangebracht in de node parameters, op het tabblad "*Optimization*".



![Image](assets/fr/025.webp)



Standaard is de waarde van de `dbcache` parameter in Bitcoin core ingesteld op 450 MiB, of ongeveer 472 MB. Door deze waarde te verhogen, kun je IBD iets versnellen. Ik zou echter niet per se aanraden om deze parameter te hoog in te stellen: zelfs het instellen op 4 GiB zal de synchronisatie slechts ongeveer 10% sneller maken, en kan ervoor zorgen dat je tijd verliest in het geval van een onderbreking tijdens IBD.



Wees voorzichtig dat u geen waarde toewijst die te groot is voor uw machine. Als het beschikbare RAM-geheugen voor UmbrelOS opraakt, kan uw knooppunt abrupt stoppen, waardoor de IBD onderbroken wordt en u het handmatig opnieuw moet opstarten, wat resulteert in een aanzienlijk tijdverlies.



Om meer te weten te komen over de invloed van de `dbcache` parameter op initiële synchronisatie, raad ik deze analyse van Jameson Lopp aan: [*Effects of DBcache Size on Bitcoin Node Sync Speed*](https://blog.lopp.net/effects-dbcache-size-Bitcoin-node-sync-speed/)



Zodra de IBD van je knooppunt is voltooid (100% synchronisatie), heb je nu een volledig operationeel Bitcoin knooppunt. Gefeliciteerd, je bent nu een integraal onderdeel van het Bitcoin netwerk!



![Image](assets/fr/027.webp)



In het volgende deel verkennen we het praktische gebruik van je nieuwe node: hoe je je Wallet erop aansluit en welke applicaties je moet installeren om een soevereine Bitcoiner te worden.





# Uw Wallet aansluiten op uw knooppunt


<partId>418d0afd-3a61-4b5a-9db4-203c0335fd29</partId>



## Indexers: rol, werking en oplossingen


<chapterId>4f93c07a-f0cb-435f-8b68-162f316d7039</chapterId>



Als je Bitcoin knooppunten al verkend hebt voordat je deze cursus volgde, ben je misschien de term "indexer" tegengekomen. Dit zijn tools zoals Electrs of Fulcrum, die toegevoegd kunnen worden aan een Bitcoin core knooppunt. Maar wat is precies hun rol? Hoe werken ze in de praktijk? En moet je er een installeren op je nieuwe Bitcoin node? Dat is wat we in dit hoofdstuk gaan onderzoeken.



### Wat is een indexer?



Over het algemeen is een indexer een programma dat een set ruwe gegevens scant, relevante sleutels (zoals woorden, identificaties en adressen) eruit haalt en een hulpbestand opbouwt, een "index" genaamd, waarin elke sleutel verwijst naar de exacte locatie van de gegevens in het corpus. Deze voorbewerkingsfase kost CPU-tijd en vereist enige schijfruimte, maar het elimineert de noodzaak om het hele corpus te verwerken elke keer dat de database wordt opgevraagd.



In lekentaal is het hetzelfde principe als een index in een boek: als je op zoek bent naar een specifiek stukje informatie, in plaats van het hele boek te herlezen, raadpleeg je de index om direct de pagina te vinden waar de informatie die je zoekt staat.



In een Bitcoin knooppunt, zoals Bitcoin core, worden Blockchain gegevens in hun ruwe, chronologische vorm opgeslagen. Elk blok bevat transacties, die op hun beurt inputs en outputs bevatten, zonder een bepaalde classificatie per Address, identifier of Wallet. Deze lineaire organisatie is geoptimaliseerd voor blokvalidatie, maar ongeschikt voor gericht zoeken. Als je bijvoorbeeld alle transacties wilt vinden die gekoppeld zijn aan een specifieke Address in een niet-geïndexeerd knooppunt, moet je handmatig de hele Blockchain doornemen, blok voor blok en transactie voor transactie. Dit is precies waar de indexer op je Bitcoin knooppunt om de hoek komt kijken.



![Image](assets/fr/085.webp)



Een indexer is een gespecialiseerd softwareprogramma dat deze massa ruwe gegevens analyseert (Blockchain, Mempool, UTXO set) en sleutels extraheert, zoals transactie-ID's, adressen en blokhoogtes. Uit deze sleutels stelt het zijn index samen, waarbij elke sleutel geassocieerd wordt met de exacte locatie van de informatie in de opslag van het knooppunt.



![Image](assets/fr/086.webp)



Met indexering kun je snel, nauwkeurig en efficiënt naar informatie op je node zoeken. Als je bijvoorbeeld een Wallet zoals Sparrow op je knooppunt aansluit, kan het vrijwel direct de balans van een Address weergeven. Concreet: het bevraagt de indexer met een verzoek als: "_Welke UTXO's zijn geassocieerd met dit script-Hash?_" De indexer antwoordt vrijwel onmiddellijk, zonder de hele Blockchain opnieuw te hoeven lezen, omdat deze gegevens al in de database staan.



### Heeft Bitcoin core een indexer?



Zonder de noodzaak van aanvullende software, biedt Bitcoin core strikt genomen geen complete Address indexer vergelijkbaar met die gevonden in software zoals Electrs of Fulcrum. Niettemin bevat het verschillende interne indexeringsmechanismen, evenals optionele opties voor het uitbreiden van de zoekmogelijkheden. Om de situatie volledig te begrijpen, moeten we een omweg maken naar de geschiedenis van het project.



Tot Bitcoin core versie 0.8.0 was transactievalidatie gebaseerd op een globale transactie-index, bekend als de `txindex`. Deze index refereerde aan alle Blockchain transacties en hun uitvoer. Wanneer een knooppunt een nieuwe transactie ontving, raadpleegde het deze index om te controleren of de verbruikte outputs (in inputs) werkelijk bestonden en niet al waren uitgegeven. `txindex` was daarom destijds onmisbaar voor transactievalidatie.



Deze aanpak had echter zijn beperkingen: het was langzaam, kostbaar in termen van opslag en overbodig in termen van informatie. Om dit te verhelpen, introduceert versie 0.8.0 een herziening van het validatiemodel genaamd ***Ultraprune***. In plaats van alles op te slaan in de vorm van transactie-indexen, onderhoudt Bitcoin core een eenvoudige database die alleen gewijd is aan UTXO's, genaamd `chainstate` (in gewone taal staat dit bekend als "UTXO set"), en werkt de lijst bij als uitgangen worden verbruikt en gecreëerd.



Deze methode is veel sneller en slaat alleen de huidige staat van het register op, waardoor de `txindex` indexer overbodig wordt. Echter, in plaats van de `txindex` code te verwijderen, hebben de ontwikkelaars ervoor gekozen om deze functionaliteit achter een eenvoudige parameter te houden (`txindex=1`). Door deze optie in te schakelen op je knooppunt, kun je elke transactie opvragen vanuit zijn `txid`.



In tegenstelling tot wat vaak wordt gedacht, biedt Bitcoin core geen Address-gebaseerde indexering zoals Electrs of Fulcrum. Er zijn verschillende redenen voor deze keuze:





- De rol van Bitcoin core is niet om een complete Block explorer te worden, noch om een API op maat te maken voor elk gebruik. Het integreren van een Address-gebaseerde index zou een Commitment onderhoud op lange termijn impliceren dat verder gaat dan de initiële reikwijdte van de software.





- De meeste gebruikssituaties kunnen al op andere manieren worden opgelost. Om bijvoorbeeld de balans van een Address te schatten, kun je het `scantxoutset` commando gebruiken, dat direct de UTXO set bevraagt zonder een volledige index nodig te hebben.





- Elk softwareprogramma heeft specifieke eisen met betrekking tot het formaat of type gegevens dat geïndexeerd moet worden (Address, Hash script, eigen tag, enz.). Het is flexibeler en logischer om deze programma's hun eigen aangepaste indexen te laten maken, dan een generieke oplossing in Bitcoin core vast te leggen.



Bitcoin core heeft een optionele transactie indexer (`txindex`), een overblijfsel van de historische werking, maar het biedt geen Address index, noch een directe Interface voor complexe zoekopdrachten. In sommige gevallen kan het daarom nuttig zijn om een externe indexer toe te voegen.



### Moet je een Address indexer toevoegen aan je knooppunt?



Het toevoegen van een Address indexer, zoals Electrs of Fulcrum, is niet verplicht; het hangt af van je specifieke behoeften.



Als je gewoon een Wallet, zoals Sparrow, op je knooppunt wilt aansluiten om saldi te bekijken en transacties uit te zenden, dan is dat heel goed mogelijk direct via Interface RPC van Bitcoin core, lokaal of op afstand via Tor.



Aan de andere kant, om meer geavanceerde software te gebruiken, zoals het draaien van een Mempool.Lokaal wordt de installatie van een Address indexer onontbeerlijk voor de ruimte Block explorer.



De indexer vereist een bepaalde hoeveelheid synchronisatietijd (minder dan de IBD) en zal extra schijfruimte innemen. Als je SSD nog genoeg vrije ruimte heeft na het downloaden van Blockchain, kun je eenvoudig een indexer toevoegen.



### Welke indexer moet ik kiezen?



Twee softwareprogramma's worden vaak gebruikt om dit type Address index op te bouwen en toegankelijk te maken: **Electrs** en **Fulcrum**. Deze tools indexeren de Blockchain volgens script-Hash (adressen) en stellen vervolgens een gestandaardiseerde Interface voor (het Electrum-protocol), waarmee talloze wallets, zoals Electrum Wallet, Sparrow of Phoenix, verbinding maken.



![Image](assets/fr/087.webp)



Simpel gezegd is Electrs vrij compact: het indexeert Blockchain sneller en neemt minder schijfruimte in, maar presteert iets minder goed dan Fulcrum bij zoekopdrachten. Fulcrum daarentegen verbruikt meer schijfruimte en doet er langer over om te indexeren, maar biedt superieure queryprestaties.



Voor individueel gebruik raad ik Electrs aan: het verbruikt minder ruimte, wordt goed onderhouden en, hoewel het iets langzamer is op bepaalde verzoeken dan Fulcrum, is het nog steeds meer dan voldoende voor dagelijks gebruik. Als je de tijd en schijfruimte hebt, kun je ook Fulcrum uitproberen, dat aanzienlijk beter zal presteren, vooral op wallets met veel te verifiëren adressen.



Concreet betekent dit dat Electrs in augustus 2025 ongeveer 56 GB opslagruimte nodig zal hebben, vergeleken met ongeveer 178 GB voor Fulcrum. Je keuze voor een indexer hangt dus ook af van je opslagcapaciteit:




- Als je schijfruimte erg beperkt is, moet je het doen met Bitcoin core zonder een externe Address indexer.
- Als je een indexer wilt gebruiken, maar nog steeds beperkt wordt door capaciteit, kies dan voor Electrs.
- Als je een comfortabele hoeveelheid schijfruimte hebt, is Fulcrum misschien precies wat je zoekt.



Voor de rest van deze BTC 202 cursus zal ik Electrs gebruiken, maar je kunt gemakkelijk meelopen met Fulcrum: de installatieprocedure is identiek, net als de Interface verbinding met de Wallet, aangezien beide een Electrum server ontsluiten.



### Hoe installeer ik een indexer op Umbrel?



Om Electrs (of Fulcrum) op je Umbrel te installeren, is de procedure eenvoudig: ga naar de App Store, zoek naar de relevante toepassing (te vinden in de Bitcoin tab), en klik vervolgens op de "*Install*" knop.



![Image](assets/fr/028.webp)



Zodra de installatie voltooid is, zal Electrs overgaan tot een synchronisatiefase (indexering), die enkele uren in beslag kan nemen.



![Image](assets/fr/029.webp)



Zodra de synchronisatie voltooid is, kunt u uw Wallet software verbinden met uw Electrum server, die gehost wordt op Umbrel.



## Hoe sluit ik mijn Wallet aan op mijn Bitcoin-knooppunt?


<chapterId>35519b1a-f681-4a69-a652-9fbe510cd17f</chapterId>



Nu je een compleet Bitcoin knooppunt hebt, is het tijd om het goed te gebruiken! In het volgende hoofdstuk zullen we andere gebruiksmogelijkheden van je Umbrel instantie verkennen. Laten we echter beginnen met de basis: uw Wallet software aansluiten om informatie van uw eigen Blockchain te gebruiken en transacties via uw eigen knooppunt te distribueren.



Zoals hierboven vermeld, zijn er twee belangrijke verbindingsinterfaces:




- Directe verbinding met Bitcoin core via RPC;
- Of maak verbinding met een Electrum-server (Electrs of Fulcrum).



In deze tutorial concentreren we ons op het verbinden met je node via Tor, omdat dit zowel een eenvoudige als veilige oplossing is voor beginners. Ik raad ten zeerste af om de RPC poort van je node vrij te geven, omdat een verkeerde configuratie een aanzienlijk risico vormt voor de veiligheid en vertrouwelijkheid van je gegevens. Het grootste nadeel van communicatie via Tor is de traagheid. In het volgende hoofdstuk verkennen we een snel en veilig alternatief voor Tor voor toegang op afstand tot je knooppunt: VPN.



We gebruiken Sparrow als voorbeeld in dit hoofdstuk, maar de procedure is hetzelfde voor alle andere Wallet beheersoftware die verbindingen met Electrum servers accepteert. Zoek gewoon de corresponderende instelling in de parameters van je toepassing (meestal in "*Server*", "*Netwerk*", "*Node*"...).



Open op Sparrow het tabblad "*Bestand*" en ga naar het menu "Instellingen".



![Image](assets/fr/030.webp)



Klik vervolgens op "*Server*" om toegang te krijgen tot de verbindingsparameters.



![Image](assets/fr/031.webp)



Vervolgens ontdek je drie mogelijkheden om je software aan een Bitcoin knooppunt te koppelen:




- Publieke server* (geel): standaard, als u geen Bitcoin knooppunt bezit, verbindt deze optie u met een publiek knooppunt dat u niet bezit (meestal van een bedrijf). Deze optie is hier niet relevant, aangezien je je eigen knooppunt op Umbrel hebt.
- Bitcoin core* (Green): deze optie komt overeen met verbinding via Interface RPC, d.w.z. rechtstreeks met Bitcoin core.
- Private Electrum* (blauw): met deze optie kun je verbinding maken via de Interface Electrum Server van je indexer (Electrs of Fulcrum).



### Aansluiting op Bitcoin core RPC



Als je Umbrel knooppunt geen indexer heeft, is dit de optie die je moet selecteren. Klik op Sparrow op "*Bitcoin core*".



![Image](assets/fr/032.webp)



U moet dan verschillende gegevens invoeren om de verbinding met uw knooppunt tot stand te brengen. Al deze gegevens zijn toegankelijk vanuit de "*Bitcoin Node*" toepassing op Umbrel door te klikken op de "*Connect*" knop in de rechter bovenhoek van de Interface.



![Image](assets/fr/033.webp)



Het tabblad "*RPC Details*" toont alle benodigde informatie voor de verbinding. Kies om verbinding te maken via Tor Address (in `.onion`).



![Image](assets/fr/034.webp)



Voer deze gegevens in de overeenkomstige velden op de Sparrow wallet in en klik dan op de knop "*Test verbinding*".



![Image](assets/fr/035.webp)



Als de verbinding succesvol is, verschijnt er een Green vinkje en een bevestigingsbericht.



![Image](assets/fr/036.webp)



Het vinkje rechtsonder Interface Sparrow wallet zal nu Green zijn (wat een directe verbinding met Bitcoin core aangeeft).



**Noot:** Om de verbinding te laten slagen, moet je node 100% gesynchroniseerd zijn. Als dit niet het geval is, wacht dan tot het einde van de IBD.



### Verbinding maken met Electrs



Als je node een indexer heeft, is het beter om daar verbinding mee te maken dan om Bitcoin core direct te gebruiken, omdat je zoekopdrachten dan sneller verwerkt worden.



Ga op Sparrow naar de tab "*Private Electrum*".



![Image](assets/fr/037.webp)



U moet dan een aantal gegevens invoeren om de verbinding met uw indexer tot stand te brengen. U vindt deze gegevens in de toepassing "*Electrs*" (of, indien van toepassing, "*Fulcrum*") op Umbrel.



Selecteer het tabblad "*Tor*" om de `.onion` verbinding Address te verkrijgen. Als u een mobiele Wallet-software wilt aansluiten, kunt u ook direct de QR-code scannen.



![Image](assets/fr/038.webp)



Voer gewoon de Tor Address van je Electrum server in het "*URL*" veld in en klik dan op de "*Test verbinding*" knop.



![Image](assets/fr/039.webp)



Als de verbinding succesvol is, worden een vinkje en een bevestigingsbericht weergegeven.



![Image](assets/fr/040.webp)



Het vinkje rechtsonder op de Interface Sparrow wallet wordt blauw (de kleur die hoort bij verbinding met een Electrum-server).



**Noot:** Om de verbinding te laten werken, moet je indexer 100% gesynchroniseerd zijn. Als dit niet het geval is, wacht dan tot het indexeringsproces voltooid is.



Nu weet je hoe je je Wallet op je Bitcoin node kunt aansluiten! In het volgende hoofdstuk laat ik je kennismaken met een aantal extra toepassingen die beschikbaar zijn op Umbrel, waar ik bijzonder enthousiast over ben, en die je in staat zullen stellen om je dagelijks gebruik van Bitcoin via je node te verbeteren.




## Overzicht van beschikbare toepassingen


<chapterId>2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594</chapterId>



Umbrel biedt een uitgebreide applicatiewinkel. Zoals je zult zien, zijn er veel tools die gerelateerd zijn aan Bitcoin, maar ook een grote verscheidenheid aan applicaties op zeer verschillende gebieden: zelf-hosting oplossingen voor diensten en bestanden, productiviteitstoepassingen, meer algemene financiële tools, mediabeheer, netwerkbeveiliging en -beheer, ontwikkeling, kunstmatige intelligentie, sociale netwerken en zelfs domotica.



In deze BTC 202 cursus concentreren we ons uitsluitend op Bitcoin-gerelateerde toepassingen. Voel je echter vrij om de rest van de catalogus te verkennen voor tools die je van pas kunnen komen.



Natuurlijk zou het onmogelijk zijn om alle Bitcoin toepassingen hier op te sommen. In dit hoofdstuk wil ik u kennis laten maken met de essentiële hulpmiddelen die uw dagelijks gebruik van Bitcoin zullen vergemakkelijken en verrijken.



### Mempool.ruimte



Als er één hulpmiddel is dat echt onmisbaar is bij het dagelijks gebruik van Bitcoin, dan is het Block explorer. Of het nu online toegankelijk is of lokaal geïnstalleerd, het zet de ruwe gegevens van Blockchain om in een gestructureerd, duidelijk en gemakkelijk te lezen formaat. Het heeft ook een zoekmachine waarmee gebruikers snel een specifiek blok, transactie of Address kunnen vinden.



Concreet kun je met de verkenner een schatting maken van de vergoedingen die nodig zijn om je transactie op te nemen in een blok, vervolgens de voortgang ervan volgen: uitzoeken of het waarschijnlijk is dat de transactie in de nabije toekomst wordt opgenomen, afhankelijk van de vergoedingenmarkt, en ten slotte bevestigen dat de transactie inderdaad is opgenomen in een blok. Het biedt ook de mogelijkheid om je eerdere transacties te analyseren en hun geschiedenis te raadplegen. Kortom, het is het Zwitserse zakmes van de bitcoiner.



Zoals eerder vermeld, kan een verkenner online worden gehost op een website of lokaal op je computer worden uitgevoerd. Een groot nadeel van online diensten is dat ze je privacy in gevaar kunnen brengen. Zonder VPN of Tor kan de server die de verkenner host je IP Address koppelen aan de transacties die je bekijkt, wat een ideaal ingangspunt kan zijn voor ketenanalyse.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Bovendien kan uw Internet Service Provider (ISP) weten dat u een bepaalde transactie bekijkt via de Block explorer site. Dit werpt ook een vertrouwenskwestie op: je moet erop vertrouwen dat de online dienst je accurate informatie over je transacties geeft, zonder dat je zelf de juistheid ervan kunt controleren.



Daarom is het altijd het beste om je eigen lokale Block explorer te gebruiken. Op deze manier lekken er geen gegevens uit over uw zoekactiviteiten, omdat alle zoekopdrachten direct worden verwerkt op een machine die u beheert, zonder via het internet te gaan. Bovendien vertrouwt een lokale verkenner op gegevens van je eigen Bitcoin node, die je zelf hebt gevalideerd, volgens je eigen regels, en die je kunt vertrouwen.



Umbrel biedt verschillende blokverkenners:




- Mempool.Ruimte
- Bitfeed
- BTC RPC Verkenner



Ik ben vooral dol op Mempool.Space, die ik op mijn node heb geïnstalleerd. Let op: om de meeste blokverkenners op Umbrel te gebruiken, is een Address indexer nodig. Je hebt dus de Bitcoin Node (of Bitcoin Knots) applicatie nodig, die een 100% gesynchroniseerde Blockchain heeft, evenals een indexer zoals Electrs of Fulcrum, die ook 100% gesynchroniseerd is.



Zodra de toepassing is geïnstalleerd, open je deze gewoon om toegang te krijgen tot je eigen verkenner.



![Image](assets/fr/041.webp)



Om meer te leren over het gebruik van de Mempool.Space verkenner, raad ik deze uitgebreide tutorial aan:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

### Bliksemknooppunt



Nu je je eigen Bitcoin knooppunt hebt, kun je ook je eigen Lightning knooppunt opzetten om off-chain transacties uit te voeren, zonder afhankelijk te zijn van een infrastructuur van derden.



Umbrel biedt een aantal toepassingen om je te helpen je Lightning-node aan de praat te krijgen. Je kunt al kiezen tussen twee hoofdimplementaties:




- LND, via de applicatie *Lightning Node*;
- Kern Bliksem.



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Je kunt je node dan beheren vanaf de hoofd Interface, of, voor nog meer functionaliteit en geavanceerde opties, installeer *Ride The Lightning* of *ThunderHub*. Deze tools bieden u een veel uitgebreider webgebaseerd Interface beheersysteem voor uw node.



https://planb.network/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.network/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

![Image](assets/fr/088.webp)



Tot slot raad ik de applicatie *Lightning Network+* aan, waarmee je collega's kunt vinden met wie je kanalen kunt openen, zodat je zowel uitgaande als inkomende geldtransacties kunt doen.



![Image](assets/fr/089.webp)



Dankzij Umbrel is het beheren van een persoonlijke Lightning-node sterk vereenvoudigd, maar het is nog steeds relatief complex. Daarom zullen we in een toekomstige cursus die volledig aan dit gebruik is gewijd dieper op dit onderwerp ingaan.



### Staartschaal



Een andere applicatie die ik erg leuk vind op Umbrel is Tailscale. Het is een VPN-applicatie die is ontworpen om het creëren van veilige netwerken tussen meerdere apparaten te vereenvoudigen, waar ze zich ook bevinden in de wereld. In tegenstelling tot traditionele VPN's, die afhankelijk zijn van gecentraliseerde servers, maakt Tailscale gebruik van het WireGuard protocol om end-to-end versleutelde verbindingen op te zetten tussen je verschillende machines. Dit betekent dat u een werkend VPN kunt implementeren in slechts een paar minuten, zonder de noodzaak voor ingewikkelde netwerkconfiguraties.



Op Umbrel verbindt de installatie van Tailscale uw Bitcoin node met uw eigen virtuele privé-netwerk. Eenmaal geconfigureerd, krijgt uw node een privé Tailscale IP Address, alleen toegankelijk vanaf andere apparaten die verbonden zijn met hetzelfde Tailscale netwerk (zoals computers, smartphones en tablets). Deze verbinding is end-to-end versleuteld en gaat niet door een onbeschermd publiek netwerk, waardoor de beveiliging aanzienlijk wordt verbeterd ten opzichte van een onversleutelde verbinding.



![Image](assets/fr/090.webp)



Concreet biedt Tailscale je verschillende voordelen bij het gebruik van je Umbrel:





- U kunt de Interface Umbrel beheren of toegang krijgen tot de applicaties die aan uw knooppunt zijn gekoppeld (zoals Mempool, Ride The Lightning, ThunderHub...) vanaf elke locatie, alsof u zich op hetzelfde lokale netwerk bevindt, zonder poorten bloot te stellen op het internet en zonder door Tor te gaan, wat erg traag is;





- Je kunt verbinding maken met je Electrum server (Electrs of Fulcrum) of direct met Bitcoin core via je VPN, waarbij je Tor omzeilt. Dit zorgt voor een veilige verbinding, vergelijkbaar met het gebruik van Tor, maar met een veel hogere snelheid en minder latentie. Kortom, u behoudt de privacy- en veiligheidsvoordelen van Tor terwijl u geniet van de snelheid van een Clearnet-verbinding. Voor een On-Chain Wallet lijkt deze winst misschien marginaal, maar als je van plan bent om later je eigen Lightning-node op te zetten, is het verschil aanzienlijk. Inderdaad, betalingen doen via je node onderweg op Tor is extreem traag door de vele uitwisselingen die nodig zijn, terwijl het met Tailscale perfect werkt.





- Je hoeft geen NAT-regels te configureren, poorten te openen of een conventionele VPN-server op te zetten. Zodra de toepassing op Umbrel en uw apparaten is geïnstalleerd, wordt het netwerk automatisch tot stand gebracht.



Tailscale op Umbrel is daarom een zeer interessante oplossing als je overal ter wereld op een veilige, krachtige en eenvoudig te configureren manier toegang wilt krijgen tot je node, zonder in te leveren op privacy of beveiliging.



Voor het installeren en configureren van Tailscale op uw Umbrel, zie deze tutorial, sectie 4: "*Gebruik van Tailscale op Umbrel*":



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Nostr



Nostr, een acroniem voor "*Notes and Other Stuff Transmitted by Relays*", is een open, gedecentraliseerd protocol dat is ontworpen om berichten te publiceren en uit te wisselen op het internet zonder afhankelijk te zijn van een gecentraliseerd platform. Elke gebruiker heeft een paar cryptografische sleutels: de publieke sleutel (`npub`), die dient als identificatie, en de private sleutel (`nsec`), die wordt gebruikt om berichten te ondertekenen en hun authenticiteit te garanderen.



Berichten worden verzonden via een netwerk van onafhankelijke relais. Deze gedistribueerde architectuur maakt Nostr bestand tegen censuur: geen enkele server controleert de toegang of distributie en een gebruiker kan verbinding maken met zoveel relais als hij wil.



Dit protocol is erg populair binnen de Bitcoin gemeenschap omdat Nostr, net als Bitcoin, kwesties van digitale soevereiniteit en gegevenscontrole aanpakt. De maker ervan, Fiatjaf, is een ontwikkelaar die al erkend is in het ecosysteem voor zijn talrijke bijdragen.



Met uw Umbrel kunt u uw gebruik van Nostr optimaliseren. Door de applicatie ***Nostr Relay*** te installeren, kunt u uw eigen privérelais rechtstreeks op uw machine hosten, zodat al uw berichten en interacties op Nostr lokaal worden opgeslagen en niet verloren kunnen gaan door verwijdering door openbare relais.



Nostr clients ***noStrudel*** of ***Snort*** zijn ook beschikbaar op Umbrel. Dankzij deze applicaties kun je publiceren, lezen, profielen zoeken en interageren met het Nostr ecosysteem, rechtstreeks vanaf het Interface web op je Umbrel.



Tot slot is er de ***Nostr Wallet Connect*** app op Umbrel, die native Lightning-betalingen in Nostr mogelijk maakt. Concreet kun je je toekomstige Lightning-knooppunt koppelen aan je Nostr-klanten om microbetalingen, "*zaps*" genoemd, te versturen om inhoud te belonen of op een gemonetariseerde manier te interageren, zonder dat je daarvoor een dienst van derden hoeft te gebruiken. Deze betalingen worden rechtstreeks vanaf uw persoonlijke knooppunt via uw kanalen verzonden.



Om uit te vinden hoe je al deze toepassingen gebruikt, raad ik je aan deze complete tutorial te bekijken:



https://planb.network/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

### BTCPay server



BTCPay Server is een gratis, open-source betalingsverwerker die u in staat stelt betalingen via Bitcoin en Lightning Network te accepteren zonder tussenpersonen, met behoud van eigen bewaring van fondsen.



De architectuur van BTCPay Server is gebaseerd op een Bitcoin node en, voor Lightning, op een compatibele implementatie (LND, Core Lightning...), waardoor het een van de weinige PoS-oplossingen is die niet onder toezicht staat. Het is ook de meest uitgebreide software voor tracking en accounting.



![Image](assets/fr/091.webp)



Als u een bedrijf hebt en Bitcoin betalingen rechtstreeks via uw Umbrel knooppunt wilt aanvaarden, dan is de BTCPay Server toepassing ideaal voor u. Om meer te weten te komen over dit onderwerp, raad ik u aan de volgende bronnen te raadplegen:





- De BIZ 101-cursus over het gebruik van Bitcoin in uw bedrijf:



https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a



- De POS 305 cursus over het gebruik van BTCPay Server:



https://planb.network/courses/6fc12131-e464-4515-9d3f-9255365d5fa1



- De BTCPay Server handleiding:



https://planb.network/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


# Geavanceerde concepten en best practices


<partId>fc77a62a-8d9f-4144-9080-3057b04db2c6</partId>



## Uw parapluknoop onderhouden


<chapterId>06d77d09-bf24-4555-b2ba-c08bbda477c7</chapterId>



Om deze laatste sectie af te trappen, en voordat we verder gaan met meer geavanceerde theorie, wil ik in dit korte hoofdstuk de best practices en concrete acties bekijken die je kunt ondernemen zodra je Umbrel node geïnstalleerd, gesynchroniseerd en correct geconfigureerd is. Hoe onderhoudt u het dagelijks?



### Apparatuur gezond houden



Een betrouwbaar knooppunt begint met stabiele hardware. Zorg ervoor dat de machine waar je node op staat goed geventileerd, Dust-vrij en geïnstalleerd is in een droge omgeving, uit de buurt van warmte- en vochtbronnen. Vermijd het proppen in een kleine ruimte en kies voor een goed geventileerde locatie.



Op Raspberry Pi en mini-PC's verstopt Dust uiteindelijk de koellichamen, waardoor de temperatuur stijgt en throttling (vrijwillige beperking van het gebruik van bronnen) optreedt, wat weer resulteert in een daling van de efficiëntie van je node. Daarom raad ik aan om de luchtinlaat en ventilator regelmatig te reinigen, idealiter om de paar maanden.



Zorg ervoor dat u een Supply-voeding van hoge kwaliteit gebruikt, want een onstabiele spanning kan leiden tot systeembeschadiging en zelfs brandgevaar opleveren. In het ideale geval gebruikt u de originele voeding Supply die door de fabrikant van uw machine is geleverd. Pas ook op voor oververhitting door het Joule-effect op stekkerdozen: respecteer altijd het maximaal toegelaten vermogen en sluit nooit meerdere stekkerdozen in cascade aan.



Ik raad ook aan om te investeren in een UPS. Dit beschermt je node tegen plotselinge uitschakelingen, stelt Umbrel in staat om netjes af te sluiten in het geval van een storing en verzekert de continuïteit van de werking tijdens micro-onderbrekingen of kortdurende storingen.



Houd aan de opslagkant de voortgang in de gaten: als de schijf verzadigd dreigt te raken, overweeg dan ruimte vrij te maken (ongebruikte apps verwijderen, de instellingen van de indexer aanpassen) of migreer naar een grotere SSD. Het nadeel van een vol Bitcoin knooppunt is dat de opslagvereisten continu toenemen, omdat er elke 10 minuten een nieuw blok wordt gegenereerd en oude blokken niet kunnen worden verwijderd (tenzij het knooppunt pruned is). Ik raad je daarom aan om bij de aanschaf van je hardware een voldoende grote capaciteit te plannen (minimaal 2 TB).



### Update



Node-updates zijn belangrijk om drie belangrijke redenen: ten eerste beveiliging (kwetsbaarheidspatches, netwerkverharding en DoS-bescherming); ten tweede compatibiliteit (wijzigingen in het relaisbeleid, formaatwijzigingen en protocolupgrades); en ten derde betrouwbaarheid en prestaties (bugfixes, resourceverbruik en andere verbeteringen). Controleer dus regelmatig of UmbrelOS en je apps up-to-date zijn:





- Om het systeem bij te werken: Open het instellingenmenu en klik vervolgens op de knop "*Check for Update*" naast de parameter "*UmbrelOS*".



![Image](assets/fr/042.webp)





- Applicaties bijwerken: Ga naar de App Store. Als een van uw toepassingen moet worden bijgewerkt, verschijnt er een knop met een rode bel in de rechterbovenhoek van de Interface. Klik erop en werk elke applicatie bij.



Voer deze handeling regelmatig uit om je besturingssysteem en applicaties up-to-date te houden.



### Back-ups



Als je alleen je Bitcoin node gebruikt om je transacties te valideren en te distribueren, maar je wallets worden buiten Umbrel beheerd (bijvoorbeeld met een Hardware Wallet en Sparrow wallet), dan is er niets om direct naar Umbrel te back-uppen. In dit geval blijft de essentiële back-up die van de herstel-zin en Descriptor van je externe Wallet, en dit geldt ongeacht of je je eigen node gebruikt of niet. Er verandert dus niets ten opzichte van je vorige configuratie.



Aan de andere kant, afhankelijk van de extra applicaties die je gebruikt op Umbrel, kunnen er meer back-ups nodig zijn. Dit is met name het geval als u een Lightning-node op Umbrel gebruikt. In dit geval is het absoluut noodzakelijk om een back-up te maken van de seed die u bij de installatie van uw Lightning-node hebt gekregen. Naast de seed hebt u een up-to-date ***Static Channel Backup (SCB)*** nodig om uw Lightning-node te kunnen herstellen in het geval van een probleem. Met SCB kunt u uw fondsen herstellen door kanalen geforceerd af te sluiten. Als de seed of de SCB ontbreekt, is het onmogelijk om een Lightning-knooppunt te herstellen.



Umbrel biedt ook de optie om automatisch en dynamisch een back-up te maken van deze SCB op hun servers, via Tor, zodat er altijd een up-to-date bestand beschikbaar is. In dit geval is alleen de seed nodig om het knooppunt te herstellen.



We zullen deze aspecten in detail bespreken in de volgende LNP202 cursus.



### Dagelijkse operationele veiligheid



Gebruik een lang, uniek en willekeurig wachtwoord voor Interface Umbrel en vergeet niet om twee-factor authenticatie (2FA) te activeren. Voor toepassingen die zowel wachtwoord- als 2FA-beveiliging bieden, activeer altijd beide en wijzig de standaardwachtwoorden.



Stel het dashboard nooit bloot aan het internet zonder een beveiligde gateway te gebruiken (zoals een VPN, Tor of alleen lokale toegang). Beperk het aantal applicaties dat je installeert en verwijder regelmatig de applicaties die je niet meer nodig hebt om het aanvalsoppervlak te verkleinen.



Om je kennis van computerbeveiliging in het algemeen te verdiepen, raad ik je ten zeerste aan deze andere gratis cursus te bekijken:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Diagnose en zelfhulp



In het geval van een bug op uw Umbrel, generate eerst een diagnosebundel via de probleemoplossingssectie van UmbrelOS of de betreffende toepassing en start de toepassing vervolgens opnieuw op. Probeer indien nodig ook een volledige herstart van het systeem.



Als het probleem zich blijft voordoen, raad ik je aan [lid te worden van de Umbrel gebruikersgemeenschap op hun Discord](https://discord.gg/efNtFzqtdx). Begin met zoeken om te zien of iemand hetzelfde probleem al heeft ondervonden en een oplossing heeft gevonden. Zo niet, dan kun je een bericht plaatsen in het `general-support` kanaal. Je kunt ook [het Umbrel forum](https://community.umbrel.com/) gebruiken.



Deze gebieden stellen u niet alleen in staat om beveiligingsaankondigingen en -updates te volgen, maar ook om vragen te stellen en uiteindelijk om andere gebruikers te helpen. Het is vaak in deze uitwisselingen dat best practices worden ontdekt.



Met deze eenvoudige gewoontes blijft uw Umbrel node stabiel, veilig en nuttig, zowel voor u als voor het Bitcoin netwerk.




## IBD en het intercollegiale ontdekkingsproces begrijpen


<chapterId>175ac9d1-ea23-45d9-9918-d3e7352435cd</chapterId>



Je Bitcoin node start op zonder enige voorkennis van de transactiegeschiedenis. In eerste instantie is het gewoon een computer met software (Bitcoin core of vergelijkbaar). Om een volledig gesynchroniseerd en operationeel Bitcoin knooppunt te worden, moet het lokaal de toestand van Ledger reconstrueren door alle blokken te controleren die gepubliceerd zijn sinds het Genesis blok (blok 0, gepubliceerd door Satoshi Nakamoto op 3 januari 2009). Deze stap heet **IBD (_Initial Block Download_)**.



IBD bestaat uit het downloaden en verifiëren van elk blok en elke transactie afzonderlijk, waarbij de consensusregels worden toegepast, om een eigen versie van de Blockchain te bouwen. Het doel is niet simpelweg om een kopie van niet-geverifieerde gegevens op te halen, maar om volledig onafhankelijk tot dezelfde conclusie te komen, net als de eerlijke meerderheid van het netwerk.



![Image](assets/fr/092.webp)



### IBD mijlpalen



De synchronisatie begint met de stap _**headers-first**_. Uw knooppunt vraagt de reeks block headers op bij verschillende peers en controleert voor elk ervan de Proof of Work, moeilijkheidsaanpassing, syntaxis, evenals de Timestamp en versienummerregels. Kortom, het zorgt ervoor dat elke ontvangen header voldoet aan de consensusregels.



![Image](assets/fr/093.webp)



Ter herinnering, een Bitcoin blok bestaat uit een header van 80 bytes en een lijst van transacties. De vingerafdruk van het blok wordt verkregen door een dubbele SHA-256 Hash toe te passen op deze header, die 6 velden bevat:




- versie
- Hash van vorig blok
- Merkle Root van transacties
- Timestamp (langer dan de mediane tijd van de voorgaande 11 blokken)
- moeilijkheidsdoel
- Nonce



![Image](assets/fr/094.webp)



Transacties worden vastgelegd in een Merkle Tree. Dit is een structuur die een grote set gegevens samenvat (in dit geval, alle transacties in het blok) door hun hashes progressief twee aan twee samen te voegen tot een enkele "root", en zo te bewijzen dat een element bij de set hoort (en elke wijziging te detecteren). Op deze manier wijzigt elke wijziging aan een transactie ook de root van de Merkle Tree en dus de fingerprint van de block header. SegWit heeft een aparte extra Commitment geïntroduceerd voor cookies (handtekeningen), geplaatst in de coinbase.



![Image](assets/fr/095.webp)



Deze _**headers-first**_ stap stelt het knooppunt in staat om de tak met het meeste werk (ongeacht het aantal blokken) te identificeren, wat de tak is waarop Bitcoin knooppunten synchroniseren. Zodra deze tak is geïdentificeerd, downloadt het knooppunt de inhoud van de blokken parallel van verschillende verbindingen en valideert dan elke transactie: formaat, geldigheid van scripts (behalve `assumevalid=1`), bedragen en afwezigheid van dubbele uitgaven. Bij elke succesvolle controle wordt de huidige staat van onuitgegeven munten (UTXO set) bijgewerkt in de `chainstate/` database: uitgegeven uitgangen worden verwijderd, terwijl nieuwe geldige uitgangen worden toegevoegd.



Mempool, aan de andere kant, komt alleen in het spel als je de top van de keten nadert: zolang het knooppunt te laat is, heeft het geen lopende transacties om op te slaan.



Zodra de IBD voltooid is, gaat het knooppunt zijn normale fase in: het valideert nieuwe blokken als ze gepubliceerd worden, onderhoudt zijn Mempool met hangende transacties volgens zijn relaisregels, geeft transacties en blokken door en beheert eventuele reorganisaties van de keten.



### VeronderstelValid



Bitcoin core bevat een mechanisme dat ontworpen is om de tijd te verkorten die nodig is voordat een knooppunt volledig operationeel is, terwijl de essentie van het autonome verificatieprincipe behouden blijft: AssumeValid.



De `assumevalid` parameter is gebaseerd op een referentieblok uit het verleden, waarvan Hash in elke softwareversie geïntegreerd is. Tijdens IBD, als je knooppunt vindt dat dit blok inderdaad op de tak met het meeste werk zit, kan het script verificatie voor alle transacties voorafgaand aan dit punt negeren.



Alle andere regels (blokstructuur, Proof of Work, omvanglimieten, transactiebedragen, UTXO's, etc.) blijven volledig geverifieerd. Alleen de berekening van scripts voorafgaand aan dit referentieblok wordt genegeerd. De prestatiewinst is aanzienlijk op de IBD, omdat handtekeningverificatie een groot deel van de CPU-belasting voor zijn rekening neemt. Na dit referentieblok keert de verificatie terug naar de normale toestand.



Je kunt volledige validatie van alle scripts forceren door dit mechanisme uit te schakelen, ten koste van een veel langere IBD, door de `assumevalid=0` parameter in het `Bitcoin.conf` bestand te gebruiken.



### StelUTXO



`assumeutxo` is een andere bestaande parameter, maar in tegenstelling tot `assumevalid` is deze niet standaard geactiveerd. Dit mechanisme stelt de software in staat om een momentopname van de UTXO set te laden, samen met de metadata, en deze voorlopig te beschouwen als een referentietoestand, nadat geverifieerd is dat de headers inderdaad leiden naar de Blockchain met het meeste werk.



Het knooppunt wordt dus snel operationeel voor algemeen gebruik (RPC, wallets verbinden, etc.), terwijl het tegelijkertijd de volledige, geverifieerde reconstructie van zijn eigen UTXO set op de achtergrond start. Zodra deze fase is voltooid, wordt de initiële momentopname vervangen door de lokaal gereconstrueerde toestand. Deze aanpak scheidt snelle levering van knooppunten van volledige verificatie, zonder de laatste in gevaar te brengen.



### Peer zoeken: Hoe vindt jouw node het Bitcoin netwerk?



Wanneer een knooppunt voor het eerst opstart, kent het nog geen peers. Het moet echter andere Bitcoin knooppunten op het Internet vinden om headers aan te vragen, en vervolgens blokken, om zijn IBD te voltooien. Om deze verbindingen te initiëren, volgt Bitcoin core een geprioriteerde logica.



![Image](assets/fr/096.webp)



Wanneer het knooppunt opnieuw opstart nadat het al eerder is gebruikt, probeert Core eerst opnieuw verbinding te maken met uitgaande peers die voor de uitschakeling zijn geregistreerd, informatie die is opgeslagen in het `anchors.dat` bestand. Daarna raadpleegt hij zijn IP Address boek **`peers.dat`**, waarin de lijst van eerder gevonden peers is opgeslagen, om opnieuw verbinding met ze te maken. Dit is gewoon een lokaal bestand, bijgewerkt en bewaard door Core. Aan de andere kant, voor een nieuwe node die net gelanceerd is, zijn deze 2 bestanden leeg, omdat deze nog nooit met andere Bitcoin nodes heeft gecommuniceerd.



In dit geval bevraagt de software _**DNS seeds**_. Dit zijn [servers onderhouden door erkende ontwikkelaars van ecosystemen](https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp), die een lijst met IP-adressen van vermoedelijk actieve knooppunten terugsturen. Met deze adressen kan het nieuwe knooppunt zijn eerste verbindingen starten en de benodigde gegevens opvragen bij de IBD. Hier is de lijst van *DNS seeds* die tot nu toe actief zijn (augustus 2025):




- Pieter Wuille: `seed.Bitcoin.sipa.be.`
- Matt Corallo: `dnsseed.bluematt.me.`
- Luke Dashjr: `dnsseed.Bitcoin.dashjr-lijst-van-P2P-nodes.us.`
- Jonas Schnelli: `seed.Bitcoin.jonasschnelli.ch.`
- Peter Todd: `seed.btc.petertodd.net.`
- Sjors Provoost: `seed.Bitcoin.sprovoost.nl.`
- Stephan Oeste: `dnsseed.emzy.de.`
- Jason Maurice: `seed.Bitcoin.wiz.biz.`
- Ava Chow: gW-568.Mainnet.achownodes.xyz.`



In de meeste gevallen is de stap *DNS seeds* voldoende om de eerste verbindingen met andere knooppunten tot stand te brengen. Als deze servers bij uitzondering niet binnen 60 seconden reageren, schakelt het knooppunt over op een andere methode: [een statische lijst van meer dan 1000 adressen](https://github.com/Bitcoin/Bitcoin/blob/master/src/chainparamsseeds.h) van _zaadknooppunten_ is ingebouwd in de code van Bitcoin core en wordt regelmatig bijgewerkt. Als de eerste twee methoden om IP-adressen te verkrijgen mislukken, brengt deze laatste oplossing een initiële verbinding tot stand, van waaruit de node vervolgens nieuwe IP-adressen kan aanvragen.



![Image](assets/fr/097.webp)



Als laatste redmiddel kun je handmatig Supply IP adressen instellen via het `peers.dat` bestand om specifieke verbindingen te forceren.



Eenmaal opgestart, diversifieert de interne Address manager de bronnen (aparte autonome netwerken, clearnet en Tor, evenals verschillende geografische gebieden) om het risico van topologische isolatie te verminderen. Het knooppunt maakt deze uitgaande verbindingen (verbindingen die het zelf selecteert en die daarom veiliger zijn).



Als je knooppunt luistert op een open poort (standaard 8333), dan accepteert het binnenkomende verbindingen. Deze versterken de algehele veerkracht van het netwerk door een contactpunt voor nieuwe knooppunten te bieden, zonder dat dit een bijzonder voordeel oplevert voor je eigen IBD. Als je node op Tor draait, blijft de logica hetzelfde, maar de gebruikte adressen zijn `.onion` diensten.




## Anatomie van uw Bitcoin knoop


<chapterId>b420bd9d-7e2a-4984-bc70-2b732a94c8ce</chapterId>



Wanneer je node zijn initiële synchronisatie heeft voltooid, slaat het lokaal verschillende complementaire gegevenssets op, waardoor het blokken en transacties kan valideren, netwerkpeers kan bedienen en snel opnieuw kan opstarten met behoud van zijn status. 3 belangrijke bouwstenen zijn essentieel op een knooppunt:




- gW-402 **blokken** opgeslagen op schijf,
- de **UTXO set** die wordt bijgehouden in een sleutelwaardedatabase,
- en de **Mempool** wordt opgeslagen in RAM en periodiek geserialiseerd.



Daarnaast maken verschillende hulpbestanden (peers, schattingen van honoraria, uitsluitingslijsten, portefeuilles, enz.) het plaatje compleet. Laten we de rol van al deze bestanden ontdekken.



### Waar bevinden de gegevens van het knooppunt zich eigenlijk?



Standaard slaat Bitcoin core zijn gegevens op in een specifieke werkmap. Onder GNU/Linux is dit meestal in `~/.Bitcoin/`, onder Windows in `%APPDATA%Bitcoin/`, en onder macOS in `~/Library/Application Support/Bitcoin/`. Als je een verpakte oplossing gebruikt (bijvoorbeeld binnen een node distributie), dan kan deze map ergens anders aangekoppeld zijn, maar de structuur blijft hetzelfde. De belangrijke submappen en bestanden die hieronder worden beschreven, bevinden zich nog steeds hier.



![Image](assets/fr/098.webp)



### De blokken



Blockchain is daarom een verzameling blokken. Een Full node slaat deze blokken op als sequentiële platte bestanden en onderhoudt een parallelle index voor snel terugvinden. Wanneer het nodig is (reorganisatie, Wallet rescan, peer service), wordt deze data opnieuw gelezen zoals het is.



**Noot:** Een reorganisatie, of resynchronisatie, is een fenomeen waarbij de Blockchain een verandering van zijn structuur ondergaat door de aanwezigheid van concurrerende blokken op dezelfde hoogte. Dit gebeurt wanneer een deel van de Blockchain wordt vervangen door een andere keten met een grotere hoeveelheid geaccumuleerd werk. Deze hersynchronisaties zijn een natuurlijk onderdeel van de werking van Bitcoin, waar verschillende miners bijna gelijktijdig nieuwe blokken kunnen vinden, waardoor het Bitcoin netwerk in tweeën wordt gedeeld. In zulke gevallen kan het netwerk zich tijdelijk opsplitsen in concurrerende ketens. Uiteindelijk, als één van deze ketens meer werk verzamelt, worden de andere ketens verlaten door de nodes en worden hun blokken bekend als "verouderde blokken" of "weesblokken" Dit proces van het vervangen van een keten door een andere wordt resynchronisatie genoemd.



#### Blk*.dat-bestanden (ruwe blokgegevens)



Ontvangen en gevalideerde blokken worden geschreven naar opeenvolgende containers met de naam `blkNNN.dat`, opgeslagen in de map `blocks/`. Elk bestand wordt op volgorde gevuld totdat de maximale grootte van 128 MB is bereikt, waarna Core het volgende bestand opent. Binnenin wordt elk blok geserialiseerd in netwerkformaat, voorafgegaan door een magische identifier en een lengte. Deze organisatie maakt snel schrijven naar schijf mogelijk en vergemakkelijkt blokservice om peers te synchroniseren.



![Image](assets/fr/099.webp)



In pruned modus bewaart het knooppunt alleen een recent venster van deze bestanden om de schijfruimte te beperken. De oudste `blk*.dat` containers worden verwijderd zodra de geconfigureerde ruimtedoelstelling is bereikt, terwijl er voldoende geschiedenis wordt bewaard om consistent te blijven met de best bekende keten. De index en UTXO set blijven normaal, waardoor de volgende transacties en blokken gevalideerd kunnen worden.



#### Rev*.dat-bestanden (annuleringsgegevens)



Om terug te kunnen gaan in de tijd tijdens een reorganisatie, slaat Core, parallel aan elk `blk` bestand, een `revNNN.dat` bestand op in `blocks/`. Dit bestand bevat de informatie die nodig is om het effect van een blok op de UTXO set ongedaan te maken: voor elke uitgang die door het blok wordt verbruikt, wordt de vorige toestand van de corresponderende UTXO opgeslagen (hoeveelheid, script, hoogte...). Als een blok wordt afgebroken, kan het knooppunt de vorige toestand snel herstellen zonder dat de hele keten opnieuw hoeft te worden gescand.



![Image](assets/fr/100.webp)



#### Blokindex (blokken/index)



Direct zoeken naar een blok in de flat files zou te tijdrovend zijn. Core onderhoudt daarom een LevelDB database in `blocks/index/` die voor elk bekend blok metadata zoals Hash, hoogte, validatiestatus, `blk` bestand en offset waar het zich bevindt opsomt. Wanneer een peer een blok opvraagt, of wanneer een interne component een specifiek blok moet benaderen, biedt deze index snelle toegang. Zonder deze index zouden er te veel handelingen nodig zijn.



![Image](assets/fr/101.webp)



#### Optionele indexen (indexen/)



Sommige indexen zijn optioneel en standaard uitgeschakeld, omdat ze de schijfruimte vergroten:




- `indexes/txindex/`, die we al genoemd hebben, biedt een transactie → locatie mapping tabel, waardoor het mogelijk is om elke bevestigde transactie op te halen zonder het blok te kennen dat het bevat. Dit is handig voor buiten Wallet `getrawtransaction` type RPC queries, maar is vrij duur.
- indexes/blockfilter/` die compacte blokfilters (BIP157/158) kunnen bevatten voor thin clients. Deze structuren versnellen verificatie aan de cliëntkant ten koste van extra opslag op het indexeerknooppunt.



### UTXO set (chainstate)



Het UTXO (*Onbestede Transactie Output*) model is de boekhoudkundige representatie van Bitcoin: elke onbestede output is een beschikbaar "Coin" dat gebruikt kan worden als input voor een toekomstige transactie.



![Image](assets/fr/102.webp)



De totaliteit van al deze onderdelen op een gegeven moment T vormt de UTXO set: een grote lijst van alle onderdelen die nu beschikbaar zijn. Het is deze staat die het knooppunt raadpleegt om te beslissen of een transactie legitieme eenheden uitgeeft die nog niet gebruikt zijn in een eerdere transactie (om Double-spending te vermijden).



![Image](assets/fr/103.webp)



De UTXO set wordt opgeslagen in de `chainstate/` map als een compacte LevelDB database. Elk deel associeert een sleutel die is afgeleid van de Hash van de transactie en de uitvoerindex met een waarde die het volgende bevat: het bedrag, het `scriptPubKey` slot, de hoogte van het aanmaakblok en een coinbase indicator.



![Image](assets/fr/104.webp)



Het knooppunt onderhoudt een geheugencache boven LevelDB om frequente lees- en schrijfbewerkingen op te vangen. De `dbcache` parameter kan worden gebruikt om de grootte van deze cache aan te passen: hoe groter deze is, hoe meer geheugentoegang de IBD en de huidige validatie profiteren, ten koste van een hoger RAM-verbruik. Wanneer een nieuw blok wordt gevonden door een Miner, verwijdert het knooppunt uit de UTXO set de uitgangen die zijn uitgegeven (of verbruikt) door de transacties in het blok en voegt de nieuw gecreëerde uitgangen toe.



Theoretisch zouden we een transactie kunnen valideren door de blokgeschiedenis opnieuw te scannen om te controleren of een uitgang nooit is uitgegeven. In de praktijk zou dit echter veel te tijdrovend zijn, omdat de hele Blockchain gescand zou moeten worden voor elke nieuwe transactie. De UTXO set biedt daarom het minimale zicht dat nodig is om lokaal en in een redelijke tijd de afwezigheid van Double-spending aan te tonen.



Merk op dat de UTXO set vaak de kern vormt van de bezorgdheid over de decentralisatie van Bitcoin, omdat de omvang ervan natuurlijk snel toeneemt. Dit komt deels door de stijgende prijs van Bitcoin, die fragmentatie van onderdelen aanmoedigt, en deels door de groeiende adoptie van het systeem: hoe meer gebruikers, hoe groter de vraag naar UTXO's.



![Image](assets/fr/105.webp)



De groei van de UTXO set komt ook voort uit de structuur van eenvoudige betalingstransacties op Bitcoin. Wanneer je een betaling doet, verbruik je een enkele UTXO als input en creëer je 2 nieuwe UTXO's als output (één voor de betaling en de andere voor de Exchange). Tenslotte geeft een heuristische ketenanalyse, genaamd CIOH (*Common Input Ownership Heuristic*), een verdere stimulans om Coin consolidatie te vermijden.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Omdat een deel ervan in het RAM moet worden bewaard om transacties binnen een redelijke tijd te kunnen verifiëren, kan de UTXO set de werking van een Full node geleidelijk aan te duur maken. Om dit probleem op te lossen bestaan er al enkele voorstellen, met name [Utreexo](https://planb.network/resources/glossary/utreexo).



### De Mempool



De Mempool is de lokale verzameling geldige transacties die zijn ontvangen, maar nog niet bevestigd. Ter herinnering, een "bevestigde transactie" is een transactie die is opgenomen in een geldig blok. Elk knooppunt onderhoudt zijn eigen Mempool, die kan verschillen van die van andere knooppunten in het netwerk, afhankelijk van:




- de grootte die is toegewezen aan de Mempool via de `maxmempool` parameter: een knooppunt met een grotere Mempool zal meer transacties kunnen bevatten dan een knooppunt met een kleinere Mempool (tenzij de laatste leeg raakt);
- gW-433 regels: deze zijn een subset van de relaisregels van het knooppunt en definiëren de kenmerken waaraan een onbevestigde transactie moet voldoen om in Mempool geaccepteerd te worden;
- transactie percolatie: door verschillende factoren kan een bepaalde transactie gedistribueerd zijn naar een deel van het netwerk, maar een ander deel nog niet bereikt hebben.



Het is belangrijk om op te merken dat node mempools geen consensuswaarde hebben. Bitcoin werkt perfect, zelfs als elk knooppunt een andere Mempool heeft. Uiteindelijk zijn de gezaghebbende blokken altijd die blokken die zijn toegevoegd aan de Blockchain. Bijvoorbeeld, zelfs als een node in eerste instantie een bepaalde transactie afwijst in zijn Mempool (geldig volgens de consensusregels), zal het verplicht zijn om het te accepteren als het uiteindelijk wordt opgenomen in een blok met een geldige Proof of Work. Als het dit niet doet en dit blok verwerpt, ook al voldoet het aan de consensusregels, zou het een Hard Fork veroorzaken, d.w.z. de aanmaak van een nieuwe, aparte Bitcoin waarop het alleen zou staan.



#### Geheugenbeleid en -beheer



Wanneer een transactie wordt ontvangen, past Core een reeks controles toe op consensusregels (syntaxis, geldige scripts, geen dubbele uitgaven, etc.) en Mempool regels, die een lokaal beleid zijn (RBF, drempels voor minimale kosten, datalimiet in `OP_RETURN`, etc.). Als de transactie aan deze regels voldoet, wordt deze in het geheugen opgeslagen.



De grootte van de Mempool wordt beperkt door de `maxmempool` parameter in het `Bitcoin.conf` bestand (meer hierover in het volgende hoofdstuk). Standaard is de limiet 300 MB. Als deze vol is, verhoogt de node dynamisch zijn minimale laaddrempel en zet de minst winstgevende transacties het eerst uit (dat wil zeggen, het behoudt transacties die het eerst gemined zouden moeten worden). Te oude transacties kunnen ook verlopen na een ingestelde vertraging.



#### Mempool persistentie op schijf



Om het herstarten te versnellen, serialiseert Core periodiek de toestand van de Mempool in het `Mempool.dat` bestand wanneer de node wordt afgesloten. Naast de eigenlijke Mempool, die in het geheugen blijft, slaat Core dit `Mempool.dat` bestand op schijf op. De volgende keer dat het knooppunt wordt gestart, wordt deze momentopname opnieuw geladen en wordt alles verwijderd dat niet langer geldig is voor de huidige Blockchain.



### Hulpbestanden en databases



Verschillende andere bestanden op hetzelfde niveau als `blocks/`, `chainstate/`, en `indexes/` dragen bij aan de goede werking van de:




- `peers.dat` houdt een IP Address boek bij van potentiële peers, gevoed door initiële DNS ontdekking, netwerkuitwisselingen en handmatige toevoegingen. Wanneer het knooppunt opstart, kan het uit dit bestand putten om uitgaande verbindingen tot stand te brengen.
- Als het knooppunt wordt uitgeschakeld, bewaart `anchors.dat` de adressen van uitgaande peers, zodat je ze de volgende keer dat je opstart snel weer kunt proberen te bereiken.
- `banlist.json` bevat lokale verboden die zijn ingesteld door de operator of door het knooppunt (herhaaldelijk ongeldig gedrag), om te voorkomen dat het knooppunt opnieuw verbinding maakt of verbindingen accepteert van deze specifieke peers.
- `fee_estimates.dat` bewaart statistieken over de tijdshorizon van waargenomen bevestigingen, die door de tariefschatter worden gebruikt om tariefpercentages voor te stellen die overeenkomen met de vertragingsdoelstellingen die zijn gekozen bij het aanmaken van een transactie.
- gW-446.conf` bevat de configuratieparameters van je knooppunt. Hier kun je de relaisregels aanpassen. Ik vertel je hier meer over in het volgende hoofdstuk.
- `settings.json` bevat aanvullende parameters voor `Bitcoin.conf`.
- `debug.log` is het diagnostische tekstlogboek, dat kan worden gebruikt om de activiteit van een knooppunt te begrijpen in het geval van een bug.
- gW-448.pid` slaat de identificatiecode van het proces tijdens runtime op, zodat andere toepassingen of scripts bitcoind (*Bitcoin daemon*) gemakkelijk kunnen identificeren en ermee kunnen communiceren indien nodig. Het wordt aangemaakt bij het opstarten van het knooppunt en verwijderd bij het afsluiten.
- `ip_asn.map` is een IP → ASN mapping tabel (standalone systeem) gebruikt voor bucketing en peer diversificatie (`-asmap` optie).
- `onion_v3_private_key` slaat de private sleutel van de Tor v3 dienst op wanneer de `-listenonion` optie is ingeschakeld, om een stabiele onion Address te behouden tussen reboots.
- `i2p_private_key` slaat de privé-sleutel van I2P op wanneer `-i2psam=` wordt gebruikt, om uitgaande en mogelijk inkomende verbindingen op I2P te maken.
- `.cookie` bevat een kortstondige RPC authenticatie token (aangemaakt bij het opstarten, verwijderd bij het afsluiten) wanneer cookie-authenticatie wordt gebruikt. Dit kan bijvoorbeeld worden gebruikt om Wallet software te verbinden.
- `.lock` is de data directory lock, die voorkomt dat meerdere instanties tegelijkertijd naar dezelfde datadir schrijven.
- `guisettings.ini.bak` is het automatisch opslaan van GUI instellingen (*Bitcoin Qt*) wanneer de `-resetguisettings` optie is gebruikt.



Zoals we zagen in de eerste delen van deze BTC 202-cursus, is Bitcoin core zowel Bitcoin node-software als Wallet. Het is echter niet per se de oplossing die ik zou aanraden voor het beheren van je wallets, aangezien Interface nog steeds basis is en de functionaliteiten beperkt zijn vergeleken met moderne software zoals Sparrow of Liana. Core bevat ook bestanden voor het beheren van je wallets:





- `wallets/` is de standaardmap die een of meer;
- `wallets/<name>/Wallet.dat` is de SQLite database van de Wallet (sleutels, descriptors, transactie metadata, etc.);
- wallets/<name>/Wallet.dat-journal` is het SQLite rollback logboek.



Samengevat is dit de Bitcoin core bestandsstructuur:



```
~/.bitcoin/
├── bitcoin.conf
├── blocks/
│   ├── blk00000.dat
│   ├── blk00001.dat
│   ├── rev00000.dat
│   ├── rev00001.dat
│   └── index/
├── chainstate/
├── indexes/
│   ├── txindex/
│   ├── blockfilter/
│   │   └── basic/
│   │       ├── db/
│   │       └── fltrNNNNN.dat
│   └── coinstats/
│       └── db/
├── wallets/
│   └── <wallet_name>/
│       ├── wallet.dat
│       └── wallet.dat-journal
├── peers.dat
├── anchors.dat
├── banlist.json
├── mempool.dat
├── fee_estimates.dat
├── bitcoind.pid
├── debug.log
├── ip_asn.map
├── onion_v3_private_key
├── i2p_private_key
├── settings.json
├── guisettings.ini.bak
├── .cookie
└── .lock
```



### Het validatiepad voor een nieuw blok



Bij ontvangst van een nieuw blok controleert je knooppunt de Proof of Work en, meer in het algemeen, de naleving van de consensusregels. Als alles goed is, past het de veranderingen transactie voor transactie toe op zijn UTXO set: het controleert of elke entry bestaande UTXO's met een geldig script spendeert, verwijdert deze UTXO's en voegt de nieuwe exits toe. Als alles geldig is, worden de wijzigingen vastgelegd op `chainstate/`.



Parallel worden ongedaan gemaakte gegevens naar `rev*.dat` geschreven en metadata naar de `blocks/index/` index. Het blok wordt dan geserialiseerd naar het juiste `blk*.dat` bestand. In het geval van een reorganisatie leest de node `rev*.dat` in omgekeerde volgorde om de verlaten blokken netjes los te koppelen, de UTXO set te herstellen en vervolgens de blokken van de nieuwe beste keten te verbinden.





## Bitcoin.conf begrijpen


<chapterId>c54a629a-ddb1-41cb-9a88-21dfd9be50ca</chapterId>



Het `Bitcoin.conf` bestand is het belangrijkste Interface configuratiebestand voor Bitcoin core. Hiermee kun je het gedrag en de parameters van je knooppunt aanpassen zonder dat je de broncode opnieuw hoeft te compileren of commandoregel aanpassingen hoeft te maken. Concreet is het een platte tekst bestand gestructureerd in sleutel-waarde paren, wat betekent dat elke regel van het bestand verwijst naar een specifieke parameter (de sleutel) en de bijbehorende waarde, die gewijzigd kan worden om die parameter aan te passen.



Netwerk, transactierelais, prestaties, indexering, logging en RPC toegangsparameters kunnen worden gedefinieerd in `Bitcoin.conf`. Dit configuratiebestand wijzigt echter nooit de consensusregels van het protocol: het stelt alleen het lokale beleid van de node in (regels voor het doorgeven), de manier waarop het verbindt, indexeert en diensten blootstelt.



### Locatie en prioriteit



Standaard staat `Bitcoin.conf` in de Bitcoin core datamap. Dit is de beroemde directory waar we het in het vorige hoofdstuk over hadden. Dit bestand wordt echter niet automatisch aangemaakt door Bitcoin core, behalve in bepaalde omgevingen, zoals Umbrel. Als het nog niet bestaat, moet je het zelf generate aanmaken door simpelweg een bestand met de naam `Bitcoin.conf` te maken en het vervolgens in een tekstverwerker te openen om je wijzigingen aan te brengen.



De parameters die zijn gedefinieerd in `Bitcoin.conf` kunnen worden overschreven door 2 lagen:




- `settings.json` (dynamisch geschreven door Interface graphics of sommige RPC),
- en opties gewijzigd via opdrachtregels.



Merk op dat elke wijziging aan `Bitcoin.conf` een herstart van het knooppunt vereist om van kracht te worden.



### Formaat en structuur



Het formaat van `Bitcoin.conf` is daarom erg eenvoudig: één regel per optie, in de vorm `optie=waarde`. Onnodige spaties en lege regels worden genegeerd en code-commentaar begint met `#`.



Bijna alle Booleaanse opties kunnen worden uitgeschakeld met een `no` voorvoegsel. Bijvoorbeeld, `luisteren=0` en `nolisten=1` zijn gelijkwaardig afhankelijk van de versie.



Om de configuratie per netwerk te segmenteren, kun je secties gebruiken: `[main]`, `[test]` (testnet3), `[testnet4]`, `[bookmark]`, `[regtest]`. Als alternatief kun je de naam van de optie vooraf laten gaan door `regtest.maxmempool=100`.



### Wat Bitcoin.conf wel en niet kan doen



Zoals hierboven uitgelegd zijn consensusregels uiteraard niet configureerbaar in `Bitcoin.conf`, omdat dit een Hard Fork zou kunnen creëren. Aan de andere kant zijn veel andere aspecten wel configureerbaar. Er zijn 3 nuttige klassen om in gedachten te houden:




- Puur lokale parameters. Deze hebben alleen invloed op jouw node: cache grootte (`dbcache`), pruned modus (`prune`), optionele indexen... Ze beïnvloeden de prestaties van jouw machine, maar niet die van het netwerk.
- Relay- en Mempool-beleid. Deze bepalen wat je node accepteert, bewaart en doorstuurt voor bevestiging: minimumtariefdrempel (`minrelaytxfee`), Mempool grootte en bewaartijd (`maxmempool`, `mempoolexpiry`), transactievervanging (RBF)... Deze regels maken geen deel uit van de consensus, dus twee verschillende nodes kunnen een verschillend beleid hebben en toch volledig compatibel zijn. Aan de andere kant zullen deze parameters wel invloed hebben op het Bitcoin netwerk (zoals uitgelegd in het eerste deel, met name met percolatietheorie).
- Netwerkconnectiviteit. Deze opties bepalen hoe je knooppunt peers vindt, luistert, een NAT doorkruist, Tor of een proxy gebruikt of zijn bandbreedte beperkt. Ze geven vorm aan je topologie, maar veranderen niets aan het doorgeven van transacties.



Het begrijpen van deze scheiding is cruciaal: als een transactie niet voldoet aan de consensusregels, zal je knooppunt deze hoe dan ook weigeren. Maar een strenger lokaal beleid kan weigeren om een transactie door te geven die geldig is in de consensus zin.



### Netwerk en topologie



Allereerst is het belangrijk om duidelijk onderscheid te maken tussen de 2 soorten verbindingen die een Bitcoin knooppunt kan hebben:




- Uitgaande verbindingen, die door ons knooppunt naar een ander knooppunt worden geïnitieerd;



![Image](assets/fr/106.webp)





- Inkomende verbindingen, geïnitieerd door een ander knooppunt naar het onze.



![Image](assets/fr/107.webp)



Deze twee soorten verbindingen zijn perfect in staat om dezelfde gegevens in beide richtingen uit te wisselen; het is geen kwestie van het beperken van de richting van de stroom, maar alleen van een verschil in de initiator van de verbinding. Vanuit het oogpunt van ons knooppunt worden uitgaande verbindingen over het algemeen als veiliger beschouwd, omdat we ze initiëren en precies kiezen met welk knooppunt we een verbinding maken, waardoor het onwaarschijnlijk is dat de verbinding kwaadaardig is. Standaard onderhoudt Bitcoin core 10 uitgaande verbindingen (8 "*full-relay*" + 2 "*block-relay-only*").



Een Full node voegt meer waarde toe aan het netwerk door inkomende verbindingen te accepteren. De `listen=1` parameter schakelt het luisteren op de standaard poort 8333 van het betreffende netwerk in, waardoor deze inkomende verbindingen op het clearnet ontvangen kunnen worden. Om dit te laten werken moet deze poort ook open staan op je router. Als dat niet het geval is, zal je node alleen met uitgaande verbindingen blijven werken, wat geen invloed heeft op je persoonlijke gebruik van Bitcoin. De keuze om inkomende verbindingen toe te staan is aan jou; er is geen "beste keuze"



Als je liever geen poort opent op je router, maar toch inkomende verbindingen accepteert, kun je de `listenonion=1` parameter activeren. Dit zal hetzelfde resultaat bereiken, maar alleen via het Tor netwerk in plaats van clearnet.



Op netwerkniveau hebben we ook:




- `addnode`: voegt een vriendelijke peer toe om contact mee op te nemen naast de gebruikelijke ontdekking (kan meerdere keren gespecificeerd worden).
- connect`: beperkt verbindingen strikt tot het Address knooppunt (kan meerdere keren gespecificeerd worden). Core maakt geen verbinding met andere knooppunten.
- `seednode`: wordt alleen gebruikt om het boek-Address in te vullen als er verbinding wordt gemaakt met een knooppunt en daarna de verbinding wordt verbroken.
- `maxconnections`: bepaalt het globale plafond voor inkomende + uitgaande verbindingen. Standaard is deze parameter ingesteld op 125, wat betekent dat je knooppunt nooit meer dan 125 verbindingen zal accepteren.
- maxuploadtarget`: begrenst uploads om bandbreedte te beperken over een glijdend venster van 24 uur. Deze limiet gaat niet ten koste van de verspreiding van essentiële recente Elements.
- `onlynet`: beperkt uitgaande verbindingen tot alleen geselecteerde netwerken (`ipv4`, `ipv6`, `onion`, `i2p`, `cjdns`). Als je bijvoorbeeld wilt dat je node alleen via Tor verbinding maakt met het Bitcoin netwerk, dan kun je de `onlynet=onion` parameter inschakelen en inkomende verbindingen uitschakelen (of ook alleen verbindingen via Tor toestaan).
- `dnsseed`: staat toe of weigert _DNS seeds_ om peers aan te vragen wanneer je lokale Address pool laag is (standaard: `1`, tenzij `-connect` of `-maxconnections=0`).
- `forcednsseed`: verplicht _DNS seeds_ aan te vragen bij het opstarten, zelfs als je al adressen op voorraad hebt (standaard: `0`).
- `fixedseeds`: Sta het gebruik toe van *seed nodes* (hardcoded Address lijst) als _DNS seeds_ falen of uitgeschakeld zijn (standaard: `1`).
- `dns`: Geeft toestemming voor DNS-resoluties in het algemeen (bijvoorbeeld voor `-addnode`/`-seednode`/`-connect`).



Standaard communiceert je node over clearnet, Tor en I2P. Dit betekent dat de peers waarmee het verbinding maakt op clearnet je publieke IP Address kunnen zien, en je ISP zal waarschijnlijk kunnen detecteren dat je een Bitcoin node gebruikt (hoewel P2P Transport V2 het moeilijker maakt voor een ISP om af te luisteren). Dit is niet per se een probleem, maar als je wilt voorkomen dat deze informatie uitlekt, kun je je node uitsluitend via het Tor netwerk verbinden.



Om volledig Tor-enabled te zijn, moet je Bitcoin core dwingen om alleen dit netwerk te gebruiken en een verborgen service te maken voor inkomende verbindingen (als je die wilt inschakelen). In `Bitcoin.conf`, moet je deze configuratie toevoegen:




- `onlynet=onion`,
- `proxy=127.0.0.1:9050`,
- `luisteronion=1`,
- `torcontrol=127.0.0.1:9051`,
- `proxyrandomize=1`,
- `luisteren=1`,
- bind=127.0.0.1`,
- `upnp=0`,
- `natpmp=0`.



Al je P2P verbindingen gaan via Tor. Je node ontvangt een `.onion` Address voor inkomende verbindingen, dus er hoeven geen poorten geopend te worden op de router. Je ISP ziet alleen Tor verkeer en je peers zijn niet op de hoogte van je werkelijke publieke IP Address.



Om DNS-resolutie in het niets te vermijden, kun je `dnsseed=0` en `dns=0` aan je configuratie toevoegen. Je moet dan handmatig `.onion` peers opgeven via `seednode=` of `addnode=`, omdat het anders moeilijk is om nieuwe nodes te vinden.



Als je een beginner bent, raad ik je natuurlijk aan om al deze netwerkinstellingen voorlopig met rust te laten. De standaardconfiguratie is vaak voldoende.



### Mempool en relaisbeleid



#### Basisparameters



Hier zijn de basisparameters die je kunt wijzigen in je `Bitcoin.conf` met betrekking tot het beheer van je Mempool en het doorgeven van onbevestigde transacties:





- `maxmempool=<n>`: Beperkt de maximale grootte van de lokale Mempool tot `<n>` megabytes (standaard: `300`). Als de limiet is bereikt, verhoogt het knooppunt dynamisch de effectieve vergoedingsdrempel en geeft het prioriteit aan de minst winstgevende transacties (gebaseerd op het vergoedingspercentage, niet de absolute waarde) om onder de limiet te blijven. Je kunt deze instelling als standaard laten staan. Verhogen kan handig zijn als je Mining solo bent, of als je een nauwkeuriger beeld wilt krijgen van Mempool congestie en de schatting van de kosten wilt verbeteren. Verlagen bespaart RAM en, in mindere mate, andere systeembronnen.





- `mempoolexpiry=<n>`: Maximale bewaartijd voor onbevestigde transacties in Mempool (in uren, standaard: `336`). Na deze tijd worden transacties verwijderd, zelfs als er nog ruimte beschikbaar is.





- `persistmempool=1`: Slaat een momentopname op van de Mempool bij stilstand en laadt deze opnieuw bij het herstarten (standaard: `1`). Dit versnelt het herstel na een herstart en voorkomt de noodzaak om de toestand opnieuw te leren via het netwerk.





- `maxorphantx=<n>`: Maximum aantal behouden wees-transacties (afhankelijke ingangen van UTXO's die nog niet gezien zijn in de UTXO set, standaard: `100`). Boven deze drempel worden de oudste transacties verwijderd om ongecontroleerde groei van de cache te voorkomen.





- blocksonly=1`: Hiermee wordt het accepteren en opnieuw verzenden van onbevestigde transacties van peers uitgeschakeld (tenzij speciale toestemmingen zijn verleend). Het knooppunt uploadt en adverteert nu alleen blokken. Lokaal aangemaakte transacties kunnen nog steeds worden uitgezonden (om je knooppunt met je Wallet software te gebruiken). Dit vermindert de bandbreedte en RAM vereisten enorm, zij het ten koste van verminderde bruikbaarheid voor het relais en totale onbekendheid met de Mempool.





- `minrelaytxfee=<n>`: Minimumtarief (in BTC/kvB) waaronder transacties niet worden geaccepteerd in de Mempool van het knooppunt en niet worden doorgegeven aan peers (standaard: `0.00001` = 1 sat/vB). Hoe hoger deze waarde, hoe agressiever je node goedkope transacties filtert.





- `mempoolfullrbf=1`: Accepteer RBF transacties zelfs zonder expliciete RBF signalering in de vervangen transactie. Met dit "*full-RBF*" beleid kan een transactie met een hogere vergoeding een andere in Mempool vervangen als aan de andere vervangingsvoorwaarden wordt voldaan.



Ter herinnering, RBF is een transactiemechanisme waarmee de verzender een transactie kan vervangen door een transactie met een hogere vergoeding om de bevestiging te versnellen. Als een transactie met een te lage vergoeding geblokkeerd blijft, kan de verzender *Replace-by-fee* gebruiken om de vergoeding te verhogen en prioriteit te geven aan zijn vervangende transactie in mempools en bij miners.



#### Geavanceerde en specifieke instellingen



Hier zijn de geavanceerde instellingen voor Mempool en relay policy. Als u een beginner bent, hoeft u deze instellingen niet aan te passen:





- datacarrier=1`: Maakt het mogelijk om transacties met niet-financiële gegevens door te sturen en (indien Mining via knooppunt) op te nemen via een `OP_RETURN` uitgang (standaard: `1`). Het deactiveren van deze parameter verkleint de oppervlakte voor niet-financiële data spam enigszins, ten koste van verminderde compatibiliteit met bepaalde toepassingen. In alle gevallen moet je gedolven `OP_RETURN` accepteren.





- `datacarriersize=<n>`: Maximale grootte (in bytes) van de `OP_RETURN` die het knooppunt doorgeeft (standaard: `83`). Het verlagen van deze waarde beperkt de payloads die via `OP_RETURN` getransporteerd worden. Merk op dat deze limiet standaard zal worden verwijderd in een toekomstige versie van Bitcoin core.





- `bytespersigop=<n>`: Parameter die handtekeningtransacties omzet in equivalente bytes voor evaluatie van de relaallimiet (standaard: `20`). Dit beïnvloedt de acceptatie van `sigops` rijke transacties volgens lokale beleidsregels.





- `permitbaremultisig=1`: Staat het doorsturen van *bare-Multisig* P2MS transacties toe (standaard: `1`). Dit is het oudste scriptsjabloon voor het instellen van multisignature condities op een UTXO (uitgevonden in 2011 door Gavin Andresen).





- `whitelistrelay=1`: Verleent automatisch relay-toestemming aan inkomende peers op de witte lijst (standaard: `1`). Van deze peers worden de transacties geaccepteerd door de relay, zelfs als het knooppunt niet in algemene relaymodus staat.





- `whitelistforcerelay=1`: Wijst "*forcerelay*" permissie toe aan whitelisted peers met standaard permissie (standaard: `0`). Het knooppunt stuurt dan hun transacties door, zelfs als ze al aanwezig zijn in Mempool, en omzeilt zo anti-redundantie mechanismen.





- `whitebind=<[permissions@]addr>` / `whitelist=<[permissions@]CIDR>`: Bindt een Interface of Address bereik en kent fijnkorrelige rechten toe aan de corresponderende peers: `relay`, `forcerelay`, `Mempool` (Mempool inhoud verzoek), `noban`, `download`, `addr`, `bloomfilter`. Dit kan handig zijn voor het toekennen van geprivilegieerde behandeling aan vertrouwde peers (zoals gateways, LANs en interne diensten).





- peerbloomfilters=1`: Schakel ondersteuning in voor Bloom filters (BIP37) om gefilterde blokken/transacties te serveren aan thin clients (standaard: `0`). Waarschuwing: dit verhoogt de belasting van uw bronnen.





- peerblockfilters=1`: Geeft BIP157 (*Neutrino*) compacte filters aan peers (standaard: `0`).





- `blockreconstructionextratxn=<n>`: Extra aantal transacties dat in het geheugen wordt vastgehouden om compacte blokken te herbouwen (standaard: `100`). Verbetert het succes van reconstructies tijdens compacte synchronisaties, ten koste van een beetje geheugen.



Ter herinnering, al deze relaisregels hebben geen invloed op de geldigheid van transacties in een geldig blok. Ze dienen om je bijdrage aan de relay aan te passen, je bronnen te beschermen en je node voorspelbaar te maken in beperkte omgevingen, maar ze staan je nooit toe om blokken te weigeren die de consensusregels respecteren.



### Portemonnees



Je kunt ook de manier waarop je wallets beheerd worden aanpassen in het `Bitcoin.conf` bestand. Als je Wallet niet direct in Core gebruikt, maar liever externe beheersoftware zoals Sparrow of Liana, dan zijn deze parameters van weinig belang:





- addresstype=<legacy|P2SH-SegWit|bech32|bech32m>`: Definieert het formaat van Wallet gegenereerde adressen voor ontvangst.





- `changetype=<legacy|P2SH-SegWit|bech32|bech32m>`: Exchange Address formaat forceren (rest van een invoer op een enkele betaling).





- `Wallet=<pad>`: Laadt een bestaande Wallet bij het opstarten (kan herhaald worden om meerdere wallets te laden).





- `walletdir=<dir>`: Directory die wallets bevat (standaard: `<datadir>/wallets` als deze bestaat, anders `<datadir>`). Dit kan handig zijn als je wallets op een speciaal of versleuteld volume wilt opslaan.





- `walletbroadcast=1`: Zendt automatisch transacties uit die zijn aangemaakt door geladen portemonnees (standaard: `1`). Stel in op `0` als je het uitzenden via een ander kanaal wilt beheren.





- `walletrbf=1`: Schakelt RBF opt-in in om RBF op alle transacties te signaleren (standaard: `1`). Hiermee kunt u de kosten later verhogen in het geval van een geblokkeerde transactie.





- `txconfirmtarget=<n>`: Bevestigingsdoel voor de transactie (in aantal blokken, standaard: `6`). De Wallet stelt automatisch de vergoeding in voor de transactie die binnen dit aantal blokken moet worden bevestigd.





- `paytxfee=<amt>`: Vast tarief (BTC/kvB) toegepast op Wallet transacties. Vermijd in het algemeen: gebruik adaptieve schatting via `txconfirmtarget`.





- fallbackfee=<amt>`: Terugvalsnelheid (BTC/kvB) die wordt gebruikt als de schatter geen gegevens meer heeft (standaard: `0,00`). Als dit op 0 wordt gezet, wordt fallback volledig uitgeschakeld.





- `mintxfee=<amt>`: Minimum drempel (BTC/kvB) voor Wallet om transacties aan te maken (standaard: `0.00001`). Wallet zal weigeren een transactie onder deze drempel aan te maken.





- `maxtxfee=<amt>`: Absolute limiet op de totale kosten voor een Wallet transactie (standaard: `0.10` BTC). Beschermt tegen abnormaal hoge kosten die bitcoins onnodig zouden vernietigen.





- `avoidpartialspends=1`: Selecteert UTXO's door Address clusters om gedeeltelijke uitgaven te vermijden.





- `spendzeroconfchange=1`: Staat toe dat een onbevestigde UTXO Exchange wordt hergebruikt als invoer in een nieuwe transactie (standaard: `1`).





- `consolidatefeerate=<amt>`: Maximale snelheid (BTC/kvB) waarboven Wallet vermijdt om meer inputs toe te voegen dan nodig is om te consolideren. Dit maakt opportunistische consolidaties tegen lage prijzen mogelijk en verlaagt de kosten wanneer de kosten hoog zijn.





- `maxapsfee=<n>`: Budget voor extra kosten (BTC, absolute waarde) die de Wallet bereid is te betalen om de optie "*vermijd gedeeltelijke uitgaven*" te activeren.





- `discardfee=<amt>`: Tarief (BTC/kvB) dat je tolerantie aangeeft om de Exchange weg te gooien door het toe te voegen aan de vergoeding. Uitgangen die meer dan een derde van hun waarde zouden kosten tegen dit tarief, worden verwijderd.





- `keypool=<n>`: Grootte van de vooraf gegenereerde Address pool (standaard: `1000`). Te kleine waarden vergroten het risico op onvolledige terugzettingen.





- `disablewallet=1`: Start Bitcoin core zonder het Wallet subsysteem en schakelt geassocieerde RPC's uit. Vermindert het aanvalsoppervlak en de footprint als het knooppunt alleen wordt gebruikt voor validatie/vrijgave.



### Opslag, indexering en prestaties



Met het configuratiebestand kun je ook de parameters voor je machine aanpassen. Dit kan vooral relevant zijn als je beperkte middelen hebt, of juist een grote hoeveelheid beschikbare capaciteit:





- `datadir=<dir>`: Stelt de hoofdgegevensmap van Bitcoin core in.





- `blocksdir=<dir>`: Ontkoppelt de locatie van de blocks bestanden (`blocks/blk*.dat` en `blocks/rev*.dat`) van de `datadir`. Dit kan handig zijn om bijvoorbeeld het blokken archief op een ander volume te plaatsen, terwijl de state base (`chainstate/`) op een sneller medium blijft staan.





- `dbcache=<n>`: Wijst `<n>` MiB toe aan de database cache (*LevelDB*) die wordt gebruikt door de blokindex en `chainstate` (standaard: `450`). Hoe hoger de waarde, hoe sneller de IBD en de huidige validatie, ten koste van een hoger RAM-verbruik.





- `prune=<n>`: Schakelt het snoeien van blokbestanden in en stelt een schijfruimte doel in MiB in (standaard: `0` = uitgeschakeld; `1` = handmatig snoeien via RPC; `>=550` = automatisch snoeien onder het doel). Niet compatibel met `txindex=1`. Het knooppunt blijft een volledig validerend knooppunt, maar kan niet langer de oude geschiedenis leveren. Deze optie is vooral handig als je schijfruimte beperkt is, bijvoorbeeld als je een knooppunt op je thuiscomputer installeert.





- txindex=1`: Bouwt en onderhoudt een globale index van bevestigde transacties. Essentieel voor bepaalde queries (`getrawtransaction` niet-Wallet) en voor verkenningsdoeleinden, maar vergroot de schijfruimte aanzienlijk. Niet compatibel met pruned modus.





- `assumevalid=<hex>`: Geeft een blok aan waarvan wordt aangenomen dat het geldig is, waardoor je scriptcontroles voor zijn voorouders kunt overslaan (stel `0` in om alles te controleren). Zie het vorige hoofdstuk voor meer informatie.





- `reindex=1`: Reconstrueert blokindexen en status (`chainstate`) van `blk*.dat` bestanden op schijf. Herbouwt ook optionele actieve indexen. Dit is een tijdrovende operatie om te gebruiken om een corrupte database te repareren of om zware indexen netjes te activeren/deactiveren.





- `reindex-chainstate=1`: Herbouwt alleen de `chainstate` van de huidige blokindex. Voorkeur als blokbestanden gezond zijn.





- `blockfilterindex=<type>`: Onderhoudt indexen van compacte blokfilters (bijvoorbeeld `basic`) die worden gebruikt door thin clients (BIP157/158) en sommige RPC's. Standaard uitgeschakeld (`0`). Neemt extra schijfruimte en indexeer tijd in beslag.





- `coinstatsindex=1`: Onderhoudt een UTXO set statistieken index die bediend wordt door de `gettxoutsetinfo` aanroep. Nuttig voor audits en statistieken, waardoor kostbare herberekeningen niet meer nodig zijn. Standaard uitgeschakeld.





- `loadblock=<bestand>`: Importeert blokken bij het opstarten uit een extern `blk*.dat` bestand. Gebruikt om geschiedenis vooraf te laden van een offline bron (lokale kopie, externe media) om initialisatie te versnellen.





- `par=<n>`: Stelt het aantal scriptverificatie-threads in (van `-10` tot `15`, `0` = auto, `<0` = laat dit aantal cores vrij). Hiermee kun je het CPU-parallellisme tijdens de validatie aanpassen. De automatische modus is in de meeste gevallen geschikt.





- `debuglogfile=<bestand>`: Specificeert de locatie van het `debug.log` logboek.





- `shrinkdebugfile=1`: Verkleint de grootte van `debug.log` bij het opstarten (standaard: `1` als `-debug` niet actief is).





- `settings=<bestand>`: Pad naar dynamisch instellingenbestand `settings.json`.



### RPC toegang en operationele veiligheid



Tenslotte kun je in het `Bitcoin.conf` bestand ook de toegangsparameters voor je knooppunt instellen. Wees voorzichtig met deze instellingen, vooral als je net begint: verander ze niet zonder een grondig begrip van de implicaties, omdat dit kwetsbaarheden kan introduceren.





- `server=1`: Activeert de JSON-RPC server. Essentieel als je `bitcoind` aanstuurt via `bitcoin-cli` of een toepassing van derden. Uitschakelen (`0`) op een zuiver validerend knooppunt dat geen API beschikbaar stelt of al een Electrum-server gebruikt.





- `rpcbind=<addr>[:port]`: RPC server luistert Address/poort. Standaard wordt alleen lokaal geluisterd (`127.0.0.1` en `::1`). Deze parameter wordt genegeerd als `rpcallowip` niet ook is gedefinieerd. Gebruik deze om Interface expliciet te beperken.





- `rpcport=<poort>`: RPC poort (standaard: `8332` op Mainnet, `18332` op Testnet, `38332` op bookmark, `18443` op regtest).





- `rpcallowip=<ip|cidr>`: Staat RPC-clients toe van een gegeven IP of subnet (kan worden herhaald). Gebruik in combinatie met `rpcbind` om de API alleen bloot te stellen aan een vertrouwd segment (LAN/VPN).





- `rpcauth=<USERNAME>:<SALT>$<Hash>`: Aanbevolen RPC authenticatiemethode (gehasht wachtwoord). Staat meerdere ingangen toe en vermijdt het opslaan van een geheim in platte tekst.





- `rpccookiefile=<pad>`: Pad naar authenticatiecookie (standaard: `.cookie` bestand onder `datadir/`). Dit wordt gebruikt voor lokale toegang door dezelfde gebruiker zonder persistente wachtwoorden te beheren. U kunt het bijvoorbeeld gebruiken om de Liana Wallet met uw Bitcoin core op dezelfde machine te verbinden.





- `rpcuser=<user>` / `rpcpassword=<pw>`: Klassieke RPC authenticatie met een wachtwoord in platte tekst. Vermijd het gebruik hiervan ten gunste van `rpcauth` of een cookie.





- `rpcthreads=<n>`: Aantal threads voor RPC oproepen (standaard: `4`). Verhoog dit als u hoge pieken in oproepen hebt aan de kant van de monitoring/externe tool.





- `rpcwhitelist=<USERNAME>:<rpc1>,<rpc2>,...`: Whitelist van geautoriseerde API's. Vermindert het aanvalsoppervlak door toegankelijke methoden te beperken.





- `rpcwhitelistdefault=1|0`: Standaard whitelist gedrag: indien ingeschakeld en een whitelist wordt gebruikt, worden niet-genoteerde oproepen geweigerd. Dit kan ook een standaard lege set forceren (geen oproepen toegestaan) zolang er niets expliciet op de lijst staat.





- `rest=1`: Schakel openbare REST API in (standaard uitgeschakeld). Alleen blootstellen op een vertrouwd netwerk (zelfde voorzichtigheid als met JSON-RPC).





- `conf=<bestand>`: Geeft, alleen op de commandoregel, een alleen-lezen configuratiebestand op. Nuttig voor het bevriezen van een uitvoeringsprofiel (onveranderlijk) aan de ops kant.





- `includeconf=<bestand>`: Laadt een extra configuratiebestand (pad relatief aan `datadir/`). Maakt scheiding van rollen mogelijk: gemeenschappelijke basis + gevoelige lokale overbelasting.





- `daemon=1` / `daemonwait=1`: Start `bitcoind` op de achtergrond en wacht, met `daemonwait`, tot de initialisatie voltooid is alvorens het over te dragen. Dit vergemakkelijkt de integratie met supervisors (systemd, runit).





- `pid=<bestand>`: Locatie van PID-bestand.





- `sandbox=<log-and-abort|abort>`: Schakelt experimentele syscalls sandboxing in: alleen verwachte syscalls zijn toegestaan.





- `startupnotify=<cmd>` / `shutdownnotify=<cmd>`: Voert een commando uit bij het opstarten of afsluiten.





- `alertnotify=<cmd>`: Triggert een commando bij ontvangst van een waarschuwing.





- `blocknotify=<cmd>`: Voert een commando uit voor elk nieuw blok.





- `debug=<category>|1` / `debugexclude=<category>`: Schakelt gedetailleerde logcategorieën in of uit (bijvoorbeeld `net`, `Mempool`, `RPC`, `validatie`...).





- `logips=1`: Logt IP-adressen.





- `logsourcelocations=1` / `logthreadnames=1` / `logtimestamps=1`: Voegt respectievelijk bronlocaties, threadnamen en precieze tijdstempels toe aan logs.





- `printtoconsole=1`: Stuurt sporen/debugs naar de console (*stdout*).





- `help-debug=1`: Geeft de debug-optie help weer en sluit af.





- `uacomment=<cmt>`: Voegt een commentaar toe aan User-Agent P2P.



We zijn nu klaar met het opsommen van de meeste configuratieparameters. Dit `Bitcoin.conf` bestand vormt dus het echte dashboard van je node: het definieert netwerk configuratie, Mempool beheer, schijf- en geheugengebruik, indexering en algemeen beheer. Als je meer wilt weten over dit bestand en er een op maat wilt maken, raad ik je aan om [Jameson Lopp's generator](https://jlopp.github.io/Bitcoin-core-config-generator/) te gebruiken.



We zijn aan het einde gekomen van deze BTC 202-cursus, die u niet alleen in staat heeft gesteld de basisprincipes te begrijpen van hoe nodes werken en hoe ze samenwerken binnen het systeem, maar ook om uw eigen node op te zetten. U bent nu een soevereine Bitcoiner, met uw eigen Wallet, die uw transacties uitzendt via uw eigen node. Gefeliciteerd!



Je kunt nu overgaan naar het laatste deel van de cursus, waar je BTC 202 kunt evalueren en vervolgens je diploma kunt halen om te controleren of je alle behandelde concepten onder de knie hebt.



U hebt nu verschillende opties voor u open. De volgende logische stap is het opzetten van je eigen Lightning node, zodat je volledig onafhankelijk bent voor je off-chain transacties. Dit zal het onderwerp zijn van een komende cursus, die dit najaar zal worden gepubliceerd in 2025 over Plan ₿ Network.



Ondertussen nodig ik u uit om de BTC 204 training te ontdekken, die u in staat zal stellen om de principes van privacybescherming te begrijpen en te beheersen bij uw gebruik van Bitcoin:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


# Laatste deel


<partId>679169f5-b990-47e1-9a00-45098ba8096b</partId>





## Beoordelingen


<chapterId>c18f672d-1074-427e-9505-eecd7ae43e71</chapterId>




<isCourseReview>true</isCourseReview>


## Eindexamen


<chapterId>a4c97701-996c-4cc5-81fa-37d2dc4ee856</chapterId>




<isCourseExam>true</isCourseExam>


## Conclusie


<chapterId>28c5cf1f-7b9c-4b68-8b8f-eee109629764</chapterId>




<isCourseConclusion>true</isCourseConclusion>