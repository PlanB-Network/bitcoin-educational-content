---
name: Bitaxe Open Source Mining Meesterschap
goal: Beheers het volledige Bitaxe-ecosysteem, van hardware-assemblage tot geavanceerd maatwerk en prestatieoptimalisatie
objectives: 

  - De filosofie van open source Bitcoin mining hardware begrijpen
  - Bitaxe mining apparaten vanaf nul opbouwen
  - mining software configureren en optimaliseren, inclusief AxeOS en Public Pool
  - Geavanceerde prestatieoptimalisaties implementeren, waaronder overklokken en benchmarken

---

# Uw Bitaxe Mining gids


Welkom bij de uitgebreide Bitaxe cursus, waar je de revolutionaire open source Bitcoin mining hardware, die de toegang tot mining technologie democratiseert, onder de knie krijgt. Deze cursus neemt je mee van het begrijpen van de filosofische fundamenten van gedecentraliseerd mining tot de geavanceerde technieken voor het aanpassen van hardware en het optimaliseren van prestaties.


Het Bitaxe-project vertegenwoordigt een paradigmaverschuiving in Bitcoin mining en doorbreekt het monopolie van propriëtaire ASIC fabrikanten door volledig open-source ontwerpen, firmware en software aan te bieden. In deze praktijkgerichte hoofdstukken leer je praktische vaardigheden in hardware-assemblage, softwareconfiguratie, PCB-ontwerp en prestatieoptimalisatie.


Ervaring met mining is niet vereist, hoewel basiskennis van elektronica en bekendheid met GitHub nuttig zijn. De cursus verandert je van een nieuwsgierige toeschouwer in een bekwame Bitaxe bouwer en bijdrager.


+++


# Inleiding


<partId>6b3cd9f0-0063-40f0-a7bb-00a48f330d88</partId>


## Cursusoverzicht


<chapterId>1fac9579-0e1c-48e3-9bc5-e7a2960018c8</chapterId>


Welkom bij de cursus MIN 306 _**Bitaxe Open Source Mining Mastery**_, een uitgebreide reis door de wereld van Bitaxe mining. Deze cursus is ontworpen voor diegenen die hun eigen Bitaxe mining hardware willen begrijpen, bouwen en optimaliseren, terwijl ze de filosofische en technische fundamenten verkennen die dit project uniek maken binnen het Bitcoin ecosysteem.


### Bitaxe begrijpen


Het eerste deel legt de essentiële basis: u ontdekt de oorsprong van het Bitaxe-project, de evolutie ervan en de waarden van decentralisatie en transparantie die het definiëren. U leert wat een Bitaxe eigenlijk is, hoe het verschilt van propriëtaire ASIC's en waar u bronnen in de gemeenschap kunt vinden om uw kennis te verdiepen. Dit deel biedt de context die nodig is om te begrijpen waarom Bitaxe een keerpunt is in de geschiedenis van Bitcoin mining.


### Software en bedrijfsvoering


Het tweede deel richt zich op de softwareomgeving, met een gedetailleerde presentatie van *AxeOS*: het open-source besturingssysteem dat speciaal is ontworpen voor Bitaxe-apparaten. Je leert de belangrijkste functies en hoe je het apparaat configureert en ermee communiceert, zodat je voor het eerst mining kunt gebruiken.


### Gemeenschap en samenwerking


Het derde deel belicht het samenwerkingsaspect van het project. Je verkent de open-source filosofie die is toegepast op zowel de hardware- als softwareontwikkeling van Bitaxe. Door middel van praktische oefeningen leer je hoe je direct kunt bijdragen aan de broncode en ontdek je _Public Pool_, een gemeenschappelijk platform voor het bundelen van rekenkracht. Je leert ook hoe je het installeert op een Umbrel-node voor lokale en soevereine integratie.


### Hardware-assemblage en probleemoplossing


In het vierde deel duik je in de hardware zelf. Je leert de gereedschappen te identificeren die nodig zijn om een Bitaxe in elkaar te zetten, soldeerproblemen op te lossen en een volledige diagnose uit te voeren met behulp van *AxeOS* en USB-tools. In dit onderdeel ligt de nadruk op praktijkervaring en een goed begrip van de interactie tussen hardware- en softwarecomponenten.


### Geavanceerd aanpassen


Het vijfde deel is gewijd aan aanpassingen. Je leert hoe je de PCB (printed circuit board) aanpast, een fabrieksbestand aanmaakt en de _Bitaxe Web Flasher_ gebruikt. Deze sectie is gericht op degenen die verder willen gaan dan eenvoudige assemblage en echt aangepaste versies van hun eigen apparaat willen ontwerpen.


### Prestatieoptimalisatie


Het zesde deel tenslotte behandelt geavanceerde optimalisatietechnieken. U leert hoe u uw Bitaxe kunt benchmarken om de prestaties te evalueren en hoe u hem efficiënt kunt overklokken. Deze vaardigheden helpen je het maximale uit je hardware te halen met respect voor de fysieke beperkingen.


Zoals bij elke cursus op Plan ₿ Academy bevat het laatste deel een evaluatie om je kennis te versterken.


Duik meteen in dit technische avontuur - de toekomst van Bitcoin mining ligt in jouw handen!


# Bitaxe begrijpen

<partId>ba1cb4ea-6a77-54fd-916c-57285c8c2418</partId>


## De geschiedenis

<chapterId>73d928e5-72f0-5c17-a7a6-8b6ece7f9a30</chapterId>

:::video id=67d2529a-b7cb-4804-b02c-e56c12c9e66e:::

Het Bitaxe-project vertegenwoordigt een baanbrekende verschuiving in de ontwikkeling van Bitcoin mining hardware en brengt open source principes naar een industrie die gedomineerd wordt door gepatenteerde oplossingen. Deze educatieve serie verkent de uitgebreide geschiedenis, technische innovaties en gemeenschapsgedreven evolutie van Bitaxe, en geeft inzicht in hoe de visie van één ingenieur veranderde in een bloeiend ecosysteem van gedecentraliseerde mining hardware. Door de oorsprong, uitdagingen en prestaties van het project te onderzoeken, krijgen we een waardevol inzicht in zowel de technische complexiteit van ASIC ontwikkeling als de kracht van open source samenwerking in de Bitcoin ruimte.


### Het verhaal van de oorsprong: Van de ontdekking van de Zijderoute tot de Visie van Zonne-Mining


Skot, de oprichter van Bitaxe, begon zijn reis naar Bitcoin op een studentenfeestje waar hij voor het eerst over Bitcoin hoorde via iemand die artikelen kocht op de Zijderoute. Deze eerste kennismaking met Bitcoin voor ongeveer $20 per munt, wakkerde een nieuwsgierigheid aan die later zou uitgroeien tot een revolutionair mining project. De technische basis voor zijn toekomstige werk werd gelegd tijdens zijn studie aan de universiteit, waar hij toegang had tot uitgebreide FPGA-resources in een laboratoriumomgeving. Samen met zijn supervisor begon Skot te experimenteren met open source FPGA bitstreams voor Bitcoin mining, aanvankelijk met het bescheiden doel om mining genoeg Bitcoin te hebben om een pizza voor hun kantoor te kunnen kopen.


De overgang van academisch experimenteren naar serieuze ontwikkeling vond jaren later plaats toen Skot werkte aan gateways op zonne-energie voor het verzamelen van gegevens op afstand in Afrika. Deze professionele ervaring met zonne-energiesystemen leidde tot het besef dat Bitcoin mining ASIC's, die fundamenteel laagspanningsgelijkstroomapparaten zijn, perfect zouden combineren met zonnepanelen. Het concept leek natuurlijk en elegant. Toen Skot echter bestaande oplossingen begon te onderzoeken, ontdekte hij een belangrijk gat in de markt: in tegenstelling tot de begindagen van Bitcoin mining, toen FPGA-ontwerpen openlijk beschikbaar waren, had de komst van ASIC's de industrie in de richting van volledig gepatenteerde, gesloten oplossingen gestuurd.


Het gebrek aan open source mining hardware werd een grote frustratie voor Skot, vooral gezien zijn achtergrond in open source softwareontwikkeling en zijn overtuiging dat de open source aard van Bitcoin zich zou moeten uitstrekken tot de mining infrastructuur. Deze filosofische afstemming op open source-principes, gecombineerd met de technische uitdaging van reverse-engineering van propriëtaire ASIC-ontwerpen, vormde de basis voor wat het Bitaxe-project zou worden. De aanvankelijke visie was ambitieus maar praktisch: een Bitcoin mijnwerker op zonne-energie maken die onafhankelijk kon werken zonder een aparte computer nodig te hebben voor de besturing, waardoor hij geschikt was voor gebruik op afgelegen locaties onder zonnepanelen.


### Technische uitdagingen en doorbraken op het gebied van reverse engineering


De ontwikkeling van Bitaxe vereiste het overwinnen van aanzienlijke technische obstakels, die zich voornamelijk concentreerden rond het complete gebrek aan documentatie van Bitmain's ASIC chips. Skots aanpak van deze uitdaging was een voorbeeld van de vastberadenheid en vindingrijkheid die nodig zijn voor succesvolle reverse engineering. Zonder toegang tot officiële datasheets of technische specificaties, nam hij zijn toevlucht tot het onderzoeken van chips onder microscopen, het meten van pin pitches met schuifmaten en zelfs het scannen van chips om hun exacte footprint vereisten te bepalen. Dit nauwgezette proces resulteerde in meerdere mislukte prototypes, waarbij de eerste twee iteraties van de "day miner" niet goed functioneerden vanwege onjuiste voetafdrukberekeningen.


De doorbraak kwam met de derde iteratie in mei 2022, toen Skot met succes een werkend ontwerp met twee chips maakte met BM1387 chips geoogst van Antminer S9 eenheden. Deze prestatie markeerde de geboorte van de naam Bitaxe, geïnspireerd op het concept van een pikhouweel voor Bitcoin mining. Het succes van dit ontwerp valideerde de reverse engineering aanpak en toonde aan dat onafhankelijke ontwikkelaars functionele mining hardware konden maken zonder ondersteuning van de fabrikant. De technische uitdagingen reikten echter verder dan de chipinterfacing en omvatten ook het complexe ontwerp van de voeding, omdat de ASIC's een nauwkeurige spanningsregeling nodig hadden bij hoge stromen en vaak werkten bij spanningen van slechts 0,6 volt, terwijl ze veel stroom verbruikten.


De ontwikkeling van de firmware bracht nog een laag van complexiteit met zich mee, omdat het project het creëren van mining software vereiste die direct op een ESP32 microcontroller kon draaien in plaats van te vertrouwen op externe computers met software zoals CGMiner. Deze op zichzelf staande aanpak was essentieel voor Skot's visie van inzetbare, onafhankelijke mining eenheden. De combinatie van hardware reverse engineering en embedded firmware ontwikkeling creëerde een uitgebreide technische uitdaging die expertise vereiste over meerdere disciplines, van elektrotechniek en PCB-ontwerp tot embedded programmeren en netwerkprotocollen.


### Gemeenschapsvorming en open-sourcesamenwerking


De transformatie van Bitaxe van een soloproject naar een bloeiend gemeenschapsinitiatief is een van de belangrijkste aspecten van het succes. Aanvankelijk waren de pogingen van Skot om generate interesse te wekken via Bitcoin forums en sociale media beperkt en af en toe sceptisch. De doorbraak kwam toen leden van de gemeenschap, zoals SirVapesAlot, het potentieel van open source mining herkenden en de Open Source Miners United (OSMU) Discord server oprichtten. Dit platform bood de samenwerkingsomgeving die nodig was voor de bloei van het project, en trok medewerkers met verschillende achtergronden aan die een gemeenschappelijk belang deelden in het democratiseren van de Bitcoin mining technologie.


Het community-gedreven ontwikkelingsmodel bleek opmerkelijk effectief, met belangrijke medewerkers zoals johnny9 en Ben die opdoken om specifieke technische uitdagingen aan te pakken. Johnny9's expertise in firmware-ontwikkeling loste kritieke software-implementatieproblemen op, terwijl Ben's front-end ontwikkelingsvaardigheden het intuïtieve AxeOS dashboard creëerden dat apparaatconfiguratie en -monitoring vereenvoudigde. Bens aanvullende bijdragen bestonden onder andere uit het opzetten van productiemogelijkheden en het creëren van Public Pool, een open source mining pool die is geoptimaliseerd voor Bitaxe-apparaten. Deze gezamenlijke aanpak liet zien hoe open source-principes de ontwikkeling konden versnellen voorbij wat een individuele medewerker alleen zou kunnen bereiken.


De OSMU-gemeenschap bevorderde ook een inclusieve omgeving waar nieuwkomers konden leren en bijdragen, ongeacht hun aanvankelijke technische expertise. Bens eigen reis van beginnend soldeerder tot grote fabrikant is een voorbeeld van deze gastvrije benadering van het ontwikkelen van vaardigheden. De toewijding van de gemeenschap aan onderwijs en wederzijdse ondersteuning creëerde een opwaartse spiraal waarbij ervaren leden nieuwkomers begeleidden, die vervolgens zelf bijdragers werden. Dit model bleek essentieel voor het opschalen van het project buiten zijn oorspronkelijke bereik en het opzetten van een duurzaam ecosysteem voor voortdurende innovatie en groei.


### Visie voor gedecentraliseerd Mining en toekomstige impact


Skots langetermijnvisie voor Bitaxe gaat veel verder dan het creëren van nog een mining apparaat: het is een fundamentele transformatie van het mining landschap van Bitcoin. Het ambitieuze doel om één miljoen one-terahash miners te produceren zou een exahash van gedistribueerde mining energie creëren, wat een belangrijke stap is in de richting van mining decentralisatie. Deze visie gaat in op de bezorgdheid over centralisatie van mining, waarbij grote zwembaden en industriële operaties mogelijk onder druk komen te staan van de overheid of de wetgever. Door mining energie te verdelen over talloze thuismijnen, wordt het netwerk veerkrachtiger en meer in lijn met de gedecentraliseerde principes van Bitcoin.


Het economische model dat deze visie ondersteunt, is gebaseerd op de unieke kenmerken van thuis-mining, waar de infrastructuurkosten in wezen nul zijn en mijnwerkers met minimaal toezicht kunnen werken. In tegenstelling tot industriële mining operaties die enorme kapitaalinvesteringen vereisen in faciliteiten, energie-infrastructuur en koelsystemen, kunnen thuisminers apparaten gewoon aansluiten op bestaande stopcontacten en internetverbindingen. Deze aanpak zou theoretisch een aanzienlijke hash rate online kunnen brengen zonder de traditionele toegangsdrempels die grootschalige mining operaties kenmerken.


Het succes van het project is al begonnen met het beïnvloeden van het bredere Bitcoin mining ecosysteem, met het potentieel om andere fabrikanten te inspireren om open source ontwikkelingsmodellen te omarmen. De financiële levensvatbaarheid die Bitaxe fabrikanten hebben laten zien, bewijst dat open source hardware commercieel succesvol kan zijn met behoud van transparantie en betrokkenheid van de gemeenschap. Terwijl het project zich blijft ontwikkelen met nieuwe chipintegraties, verbeterde ontwerpen en uitgebreide productiepartnerschappen, dient het als een proof of concept van hoe Bitcoin mining kan terugkeren naar zijn gedecentraliseerde wortels terwijl het moderne ASIC technologie omarmt. Het uiteindelijke doel gaat verder dan alleen de distributie van hashrates en omvat ook educatieve impact, waardoor meer mensen in direct contact komen met het fundamentele mining proces van Bitcoin en een dieper begrip ontstaat van het veiligheidsmodel van het netwerk.


## Wat is de Bitaxe?

<chapterId>6a56af56-35ce-51af-999b-4bc7305e6464</chapterId>

:::video id=12b26c7a-74b1-4ea9-afc0-e3ef90cf5837:::

### Hardwareoverzicht en mogelijkheden


Het Bitaxe ecosysteem omvat meerdere hardware iteraties, elk ontworpen om verschillende aspecten van de mining ervaring te optimaliseren met behoud van de kernfilosofie van open-source toegankelijkheid. Deze apparaten dienen niet alleen als functionele mining hardware, maar ook als educatief gereedschap waarmee gebruikers de ingewikkelde relatie tussen ASIC chips, microcontrollers en het Bitcoin mining proces kunnen begrijpen. Inzicht in de ontwerpfilosofie en technische implementatie van de Bitaxe geeft waardevolle inzichten in hoe moderne mining hardware werkt op zowel component- als systeemniveau.



### Bitaxe Max, implementatie van de eerste generatie


De Bitaxe Max vertegenwoordigt de basisimplementatie van het Bitaxe-concept en maakt gebruik van de BM1397 ASIC chip die oorspronkelijk door Bitmain is ontwikkeld voor hun S17 mining serie. Deze chipintegratie laat zien hoe open-source hardware bestaande ASIC technologie kan hergebruiken om toegankelijke mining oplossingen te creëren. De Bitaxe Max levert een geschatte hashsnelheid tussen 300 en 400 gigahashes per seconde, waardoor het eerder een educatief en experimenteel mining platform is dan een oplossing op commerciële schaal.


De integratie van de BM1397 chip in de Bitaxe Max vereiste zorgvuldige overweging van stroombeheer, thermische controle en communicatieprotocollen. Het ontwerp van de printplaat voldoet aan de specifieke vereisten van deze ASIC en biedt tegelijkertijd de nodige ondersteunende circuits voor een stabiele werking. Deze implementatie laat zien hoe open-source hardwareontwikkeling gebruik kan maken van bestaande halfgeleidertechnologie om nieuwe toepassingen en leermogelijkheden te creëren binnen de mining gemeenschap.


### Bitaxe Ultra, geavanceerde chiptechnologie


De Bitaxe Ultra vertegenwoordigt de evolutie van het Bitaxe platform en bevat de meer geavanceerde BM1366 ASIC chip uit de S19 serie van Bitmain. Deze nieuwere chiptechnologie zorgt voor verbeterde efficiëntie en prestatiekenmerken van het Bitaxe platform, terwijl dezelfde fundamentele ontwerpfilosofie behouden blijft. De upgrade naar de BM1366 chip toont het aanpassingsvermogen van het platform en de toewijding van de gemeenschap om technologische vooruitgang te integreren in open-source mining oplossingen.


De overgang van de BM1397 naar de BM1366 chip vereiste aanpassingen aan de voedingssystemen, het thermisch beheer en de besturingsalgoritmen van de printplaat. Deze wijzigingen illustreren de iteratieve aard van hardwareontwikkeling en het belang van het behouden van compatibiliteit terwijl de prestaties worden verbeterd. De implementatie van de Bitaxe Ultra biedt gebruikers toegang tot recentere ASIC technologie terwijl het educatieve en experimentele karakter van het platform behouden blijft.


### Microcontroller en communicatiesystemen


In het hart van elk Bitaxe-apparaat zit een ESP-microcontroller die dient als primaire interface tussen de gebruiker en de ASIC-chip. Op deze microcontroller draait speciale software, ontwikkeld door de Open Source Miners United (OSMU) gemeenschap, waarmee nauwkeurige controle over de werkingsparameters van de ASIC mogelijk is. De communicatie tussen de microcontroller en de ASIC verloopt via zorgvuldig ontworpen seriële communicatielijnen die als zichtbare sporen direct op de printplaat zijn geëtst.


De rol van de microcontroller gaat verder dan eenvoudige besturing van de ASIC: hij omvat energiebeheer, temperatuurbewaking en gebruikersinterfacefuncties. Via het geïntegreerde scherm kunnen gebruikers kritieke operationele parameters controleren, zoals temperatuur, hash rate, IP-adres en andere relevante mining-statistieken. Dit real-time feedbacksysteem biedt waardevolle inzichten in de prestaties van het apparaat en helpt gebruikers hun mining operaties te optimaliseren, terwijl ze leren over het onderliggende gedrag van de hardware.


### Energiebeheer en veiligheidsoverwegingen


Het Bitaxe platform werkt op een strikte 5-volt voeding, waardoor een juiste selectie van de voeding essentieel is voor de levensduur en veiligheid van het apparaat. Het energiebeheersysteem op de Bitaxe-kaarten bevat geavanceerde schakelingen die zijn ontworpen om de spanningstoevoer naar de ASIC chip te regelen en tegelijkertijd het stroomverbruik in verschillende operationele modi te bewaken. Dankzij dit energiebeheer kan het apparaat efficiënt werken bij een reeks interne frequenties en spanningen, waarbij afhankelijk van de configuratie tussen de 5 en 25 watt wordt verbruikt.


Het begrijpen van de stroomvereisten wordt cruciaal als je bedenkt dat een onjuiste spanningstoepassing het apparaat permanent kan beschadigen. De relatie tussen frequentie, spanning, stroomverbruik en hashsnelheid toont fundamentele principes van de ASIC werking die van toepassing zijn op alle mining hardware. Gebruikers kunnen experimenteren met verschillende stroominstellingen om de efficiëntieafwegingen te begrijpen die inherent zijn aan mining bewerkingen, en praktische ervaring opdoen met concepten die van toepassing zijn op mining implementaties op grotere schaal.


### Solo Mining Focus en netwerkdeelname


Het Bitaxe platform richt zich specifiek op solo mining toepassingen, waarbij individuele miners Bitcoin blokken onafhankelijk proberen op te lossen in plaats van deel te nemen aan grote mining pools. Hoewel de hash rate van Bitaxe-apparaten een succesvolle ontdekking van blokken statistisch onwaarschijnlijk maakt, dient deze aanpak belangrijke educatieve en filosofische doeleinden binnen de Bitcoin gemeenschap. Solo mining met Bitaxe-apparaten helpt gebruikers de fundamentele mechanica van het proof-of-work systeem van Bitcoin te begrijpen, terwijl het bijdraagt aan de decentralisatie van het netwerk.


De nadruk op solo mining weerspiegelt het streven van de OSMU-gemeenschap om individuele deelname aan het beveiligingsmodel van Bitcoin aan te moedigen. Door toegankelijke hardware aan te bieden die onafhankelijk kan werken, stelt het Bitaxe platform gebruikers in staat om hun eigen mining operaties uit te voeren zonder afhankelijk te zijn van de infrastructuur van de pool. Deze aanpak bevordert een beter begrip van het consensusmechanisme van Bitcoin en ondersteunt het gedecentraliseerde karakter van het netwerk door een grotere diversiteit aan mijnwerkers.


### Hardware-evolutie en productieverbeteringen


Het Bitaxe platform blijft zich ontwikkelen door feedback uit de gemeenschap en productieoptimalisatie, waarbij nieuwere versies verbeteringen bevatten die de maakbaarheid en gebruikerservaring verbeteren. Versie-updates richten zich meestal op productie-efficiëntie in plaats van fundamentele prestatiewijzigingen, zodat bestaande gebruikers niet te maken krijgen met verouderingsdruk. Functies zoals de overgang van micro-USB naar USB-C connectoren en verbeterde voedingsaansluitsystemen weerspiegelen de aandacht van de community voor praktische bruikbaarheidsverbeteringen.


Deze evolutionaire aanpak demonstreert de voordelen van open-source hardwareontwikkeling, waarbij de inbreng van de gemeenschap zorgt voor incrementele verbeteringen waar alle gebruikers van profiteren. De filosofie van "if it hashes, it hashes" benadrukt de focus van het platform op functionaliteit in plaats van constante upgrades, waardoor gebruikers worden aangemoedigd om hun apparaten te onderhouden en te gebruiken in plaats van de nieuwste versies na te jagen. Deze benadering ondersteunt duurzame hardwarepraktijken terwijl de educatieve waarde van Bitaxe behouden blijft.


## Waar kan ik meer te weten komen?

<chapterId>706f2fff-fa1c-5d8e-b14c-ece6e42c016f</chapterId>

:::video id=90088397-3a16-485f-bbd2-89cdbb844e4a:::

Het Bitaxe project vertegenwoordigt een uitgebreid open-source mining initiatief dat veel verder gaat dan een enkel apparaat. Weten waar je betrouwbare informatie, technische bronnen en ondersteuning van de gemeenschap kunt vinden, is cruciaal voor iedereen die betrokken wil raken bij dit ecosysteem. Dit hoofdstuk biedt een complete gids voor de essentiële platforms en bronnen die de basis vormen van de Bitaxe en Open Source Miners United (OSMU) gemeenschap.


### Bitaxe.org, de centrale hub


De Bitaxe.org website is de primaire toegangspoort tot alle projectgerelateerde informatie en bronnen. Dit gecentraliseerde platform fungeert als uw eerste referentiepunt wanneer u meer wilt weten over Bitaxe-apparaten of andere projecten binnen de OSMU-gemeenschap wilt verkennen. Het ontwerp van de website geeft prioriteit aan toegankelijkheid en organisatie, waarbij bezoekers zorgvuldig samengestelde links krijgen aangeboden die verwijzen naar verschillende gespecialiseerde bronnen binnen het ecosysteem.


Het belang van deze centrale hub kan niet genoeg worden benadrukt, omdat het de verwarring wegneemt die vaak gepaard gaat met gedecentraliseerde open source-projecten. In plaats van te zoeken op meerdere platforms of te vertrouwen op mogelijk verouderde informatie van onofficiële bronnen, kunnen gebruikers erop vertrouwen dat Bitaxe.org actuele, geverifieerde links biedt naar alle essentiële bronnen. Deze aanpak zorgt ervoor dat zowel nieuwkomers als ervaren leden van de gemeenschap efficiënt de specifieke informatie kunnen vinden die ze nodig hebben voor hun projecten.


### Technische hulpmiddelen en ontwikkelingsmateriaal


De repository met hardwareontwerpbestanden op GitHub is een van de meest waardevolle bronnen voor iedereen die geïnteresseerd is in het begrijpen of bouwen van Bitaxe-apparaten. Deze openbare opslagplaats bevat uitgebreide documentatie over elk aspect van het hardwareontwerpproces, van de eerste concepten tot de uiteindelijke productiespecificaties. De repository bevat gedetailleerde afbeeldingen, projectdoelen, functiebeschrijvingen en uitleg over ingebouwde componenten die zowel technische diepgang als praktische richtlijnen bieden.


Voor degenen die geïnteresseerd zijn in de productie van hun eigen apparaten, bevat het archief specifieke documentatiebestanden zoals building.md, dat stapsgewijze instructies geeft voor het hele productieproces. Deze documentatie behandelt de softwaretools die nodig zijn voor het PCB-ontwerp, de procedures voor het verzenden van bestanden naar fabrikanten en de stappen die nodig zijn voor het ontvangen en valideren van geproduceerde PCB's. Dit detailniveau zorgt ervoor dat individuen of kleine organisaties met succes door het productieproces kunnen navigeren zonder uitgebreide voorafgaande ervaring in hardwareproductie.


De ESP-Miner repository dient als centrale locatie voor alle firmwaregerelateerde code en documentatie. Deze GitHub repository bevat elke regel code die is geschreven voor de Bitaxe-firmware, samen met uitgebreide documentatie waarin de systeemvereisten, hardwarespecificaties en configuratieopties worden uitgelegd. De structuur van de repository is ontworpen voor zowel gebruikers die de voorkeur geven aan voorgecompileerde binaire bestanden als ontwikkelaars die de firmware vanaf de broncode willen bouwen.


De documentatie in deze repository bevat gedetailleerde secties over hardwarevereisten, voorconfiguratie-opties en aanbevolen waarden voor verschillende instellingen. Deze informatie blijkt van onschatbare waarde te zijn voor gebruikers die hun apparaten willen aanpassen of specifieke problemen willen oplossen. Daarnaast bevat de repository informatie over nieuwere ontwikkelingen, zoals Raspberry Pi integratie, zodat de documentatie actueel blijft met de voortdurende evolutie van het project.


### Tools voor apparaatbeheer en -onderhoud


De Bitaxe webflasher is een praktische oplossing voor apparaatonderhoud en updates. Met deze webgebaseerde tool kunnen gebruikers firmware flashen naar hun apparaten zonder dat daarvoor gespecialiseerde software of complexe commandoregelprocedures nodig zijn. De flasher ondersteunt meerdere apparaatvarianten, waaronder de Bitaxe Ultra met verschillende poortversies en de oudere Bitaxe Max-modellen. Gebruikers kunnen kiezen tussen het updaten van bestaande firmware via de webinterface of het uitvoeren van complete fabrieksresets via USB-verbindingen.


Deze tool richt zich op een van de meest voorkomende uitdagingen voor hardwareliefhebbers: het onderhouden en bijwerken van de firmware van apparaten. Door een gebruiksvriendelijke webinterface te bieden, elimineert de flasher veel van de technische obstakels die gebruikers er anders van zouden kunnen weerhouden om hun apparaten up-to-date te houden met de nieuwste firmwarereleases. Het ontwerp van de tool geeft prioriteit aan eenvoud, terwijl de flexibiliteit die nodig is voor verschillende apparaatconfiguraties en updatescenario's behouden blijft.


### Gemeenschapsplatforms en communicatiekanalen


De Discord-server vormt het hart van de real-time interactie en ondersteuning binnen het Bitaxe-ecosysteem. De organisatie van de server weerspiegelt de verschillende interesses en behoeften van de leden van de community, met zorgvuldig gestructureerde kanalen die gerichte discussies over specifieke onderwerpen mogelijk maken. Nieuwe leden krijgen te maken met een verificatieproces waarbij ze de communityregels moeten lezen en accepteren, zodat alle deelnemers de verwachtingen voor respectvolle en productieve interactie begrijpen.


De kanaalstructuur van de server bevat algemene discussiegebieden met onderwerpen als zonne-energie-integratie, mining-pools en Bitcoin-gerelateerde discussies. Meer gespecialiseerde secties richten zich op specifieke apparaten, waaronder speciale kanalen voor de Bitaxe Ultra, Hex en Supra varianten. Het firmware-kanaal biedt een gerichte ruimte voor technische discussies over softwareontwikkeling en probleemoplossing, terwijl het officiële release-kanaal ervoor zorgt dat leden van de community tijdig bericht krijgen over nieuwe ontwikkelingen.


Er is ook een abonneegedeelte dat extra voordelen biedt voor leden van de gemeenschap die ervoor kiezen het project financieel te steunen. Deze gelaagde aanpak stelt de community in staat om verbeterde diensten aan te bieden en tegelijkertijd open toegang te houden tot essentiële informatie en ondersteuningskanalen. Het helpkanaal dient als een speciale ruimte voor het oplossen van problemen en technische ondersteuning, zodat gebruikers snel ondersteuning kunnen krijgen als ze problemen ondervinden.



De Open Source Miners United wiki (osmu.wiki) biedt uitgebreide documentatie als aanvulling op de real-time discussies op Discord. In tegenstelling tot chatgebaseerde platforms biedt de wiki gestructureerde, doorzoekbare documentatie over alle aspecten van het Bitaxe-project en verwante initiatieven. De organisatie weerspiegelt de structuur van het project, met speciale secties voor verschillende apparaatseries en uitgebreide installatiegidsen.


Dankzij het open-source karakter van de wiki kunnen leden van de gemeenschap rechtstreeks bijdragen aan de documentatie. Gebruikers kunnen pagina's bewerken, correcties indienen en nieuwe informatie toevoegen via GitHub-integratie, waardoor de kennisbank actueel en transparant blijft. Deze gezamenlijke aanpak maakt gebruik van de collectieve expertise van de gemeenschap, terwijl de kwaliteitscontrole behouden blijft door middel van een beoordelingsproces voor ingediende wijzigingen.


De wiki bevat praktische hulpmiddelen zoals PDF installatiegidsen met stapsgewijze instructies voor de configuratie en het gebruik van apparaten. Deze gidsen dienen als waardevolle referenties voor zowel nieuwe gebruikers als ervaren communityleden die snel toegang nodig hebben tot specifieke procedures of configuratiedetails.


### Informatie over inkoop en leveranciers


De Bitaxe legitieme lijst voorziet in een kritieke behoefte binnen de open-source hardware gemeenschap: het identificeren van betrouwbare verkopers en het vermijden van frauduleuze verkopers. Deze lijst bevat geverifieerde verkopers en fabrikanten die voldoen aan specifieke criteria voor legitimiteit en ondersteuning door de gemeenschap. Elke lijst bevat directe links naar websites van verkopers, regionale informatie en bedrijfsbeschrijvingen die gebruikers helpen om weloverwogen aankoopbeslissingen te nemen.


Belangrijk is dat de lijst aangeeft of elke verkoper bijdraagt aan de OSMU-gemeenschap, hetzij financieel of via andere vormen van ondersteuning. Deze transparantie helpt leden van de gemeenschap te begrijpen welke leveranciers de ontwikkeling en duurzaamheid van het project actief ondersteunen. De lijst dient ook als bescherming tegen veelvoorkomende zwendel, zoals ongeautoriseerde voorbestellingen voor niet-uitgebrachte producten, die in het verleden problemen hebben veroorzaakt binnen de gemeenschap.


De nadruk op niet-aangesloten links toont de toewijding van de community om onbevooroordeelde aanbevelingen voor leveranciers te doen. Gebruikers kunnen erop vertrouwen dat de aanbevelingen gebaseerd zijn op de legitimiteit van de leverancier en de bijdrage van de gemeenschap in plaats van op financiële prikkels, zodat aankoopbeslissingen zowel de individuele behoeften als de duurzaamheid van de gemeenschap ondersteunen.



# Software en bedrijfsvoering

<partId>04b302a9-42ba-5ad4-834c-6979950c2948</partId>


## Wat is AxeOS?

<chapterId>a0cdf10d-e007-58e2-a17b-b588fd393b5e</chapterId>

:::video id=de7bcbf2-f9ac-4057-ad40-29dc223b4798:::

AxeOS is een firmware- en webinterface voor Bitaxe mining apparaten, die gebruikers volledige controle- en bewakingsmogelijkheden biedt via een intuïtief browsergebaseerd dashboard. Dit systeem transformeert de complexe taak van ASIC beheer in een toegankelijke ervaring, waardoor mijnwerkers prestaties kunnen controleren, instellingen kunnen aanpassen en meerdere apparaten kunnen beheren vanuit een enkele interface. Het begrijpen van AxeOS is essentieel voor het maximaliseren van het potentieel van je Bitaxe apparaat en het behouden van optimale mining operaties.


### Dashboardoverzicht en kerngegevens


Het AxeOS dashboard dient als uw primaire venster op de prestaties van uw Bitaxe apparaat en presenteert kritieke mining meetgegevens in een overzichtelijk, real-time formaat. Wanneer u navigeert naar het IP-adres van uw Bitaxe-apparaat, krijgt u onmiddellijk vier belangrijke prestatie-indicatoren te zien die de huidige status van uw mining bepalen. De weergave van de hashsnelheid toont de werkelijke rekensnelheid die uw ASIC chip produceert bij het verwerken van het huidige bloksjabloon, waardoor u onmiddellijk feedback krijgt over de kernfunctionaliteit van uw apparaat.


Naast de hashsnelheid houdt de aandelenteller elke geldige oplossing bij die uw Bitaxe-apparaat indient bij de mining pool. Hij wordt verhoogd bij elke succesvolle indiening en is een directe maatstaf voor de bijdrage van uw apparaat aan de mining inspanningen van de pool. De efficiëntiemeter geeft een cruciaal inzicht in de energieprestaties van uw apparaat door de verhouding tussen hashsnelheid en stroomverbruik te berekenen, zodat u de winstgevendheid van uw operatie kunt optimaliseren. De beste moeilijkheidsgraad indicator bewaart een record van het hoogste moeilijkheidsaandeel dat je apparaat ooit heeft gevonden, en behoudt deze prestatie zelfs door reboots en updates, en wordt alleen gereset wanneer je een complete fabrieks-flash uitvoert.


Het uitbreidbare menusysteem van het dashboard, bediend door een toggle-knop, biedt toegang tot alle AxeOS-functionaliteit met behoud van een strakke interface. De live hash rate grafiek is een van de meest waardevolle functies en toont real-time prestatiegegevens die nauwkeuriger en informatiever worden naarmate je je sessie langer volhoudt. De energie-, warmte- en prestatiesecties bieden uitgebreide bewaking van de operationele status van je apparaat, inclusief waarschuwingen voor ingangsspanning die je waarschuwen voor mogelijke problemen met de voeding en zorgen voor een continue werking binnen veilige parameters.


### Geavanceerde bewaking en systeeminformatie


De bewakingsmogelijkheden van AxeOS gaan veel verder dan het bijhouden van de basis hash rate, en bieden gedetailleerd inzicht in elk aspect van de werking van uw Bitaxe-apparaat. De energiesectie toont berekend stroomverbruik afgeleid van geïntegreerde circuits aan boord, metingen van de ingangsspanning van uw voedingsaansluiting en gevraagde ASIC spanningsniveaus. Als het voltage daalt, geeft AxeOS onmiddellijk waarschuwingen, hoewel deze meestal geen invloed hebben op de werking van de mining en alleen wijzen op mogelijkheden om de voeding te optimaliseren.


Temperatuurbewaking richt zich op het thermisch beheer van de ASIC chip, met metingen vanaf strategische locaties op het apparaat om nauwkeurige thermische gegevens te leveren met de juiste offsets voor nauwkeurigheid op chipniveau. De frequentie- en spanningsdisplays bieden real-time terugkoppeling over uw ASIC afstemparameters, waarbij het gemeten voltage de nauwkeurigste beschikbare aflezing is, direct genomen op de locatie van de ASIC chip. Deze precisie maakt fijnafstelling van prestatieparameters mogelijk met behoud van veilige bedrijfsomstandigheden.


De sectie Verbindingsstatus geeft direct inzicht in uw mining poolconfiguratie en toont de huidige stratum URL, poort en gebruikersidentificatie. Voor apparaten die zijn aangesloten op openbare pools genereert AxeOS handige snelkoppelingen die u rechtstreeks naar de webinterface van uw pool brengen, waar u toegang hebt tot gedetailleerde statistieken, apparaatoverzichten en historische prestatiegegevens. Deze integratie stroomlijnt het monitoringproces door informatie op apparaatniveau en poolniveau te verbinden in een naadloze workflow.


### Zwermbeheer en besturing met meerdere apparaten


De Swarm-functionaliteit vertegenwoordigt AxeOS' oplossing voor de complexiteit van het beheren van meerdere Bitaxe-apparaten in een netwerk, waardoor het niet meer nodig is om talloze IP-adressen te onthouden en daarnaar te navigeren. Met dit gecentraliseerde beheersysteem kunt u apparaten toevoegen door simpelweg hun IP-adres in te voeren, automatisch actieve Bitaxe-miners te detecteren en ze op te nemen in een uniform controledashboard. Eenmaal geconfigureerd, biedt Swarm uitgebreide controle over uw gehele mining operatie vanuit één enkele interface.


Via de Zwerm-interface kun je kritieke beheertaken uitvoeren op meerdere apparaten tegelijk of afzonderlijk, inclusief poolconfiguratiewijzigingen, herstarten van apparaten, frequentieaanpassingen en prestatiebewaking. Deze gecentraliseerde aanpak vermindert de administratieve overhead van het beheer van grote mining operaties aanzienlijk en zorgt voor een consistente configuratie op alle apparaten. Het systeem behoudt de individuele apparaatidentiteit terwijl het collectieve beheermogelijkheden biedt, waardoor een optimale balans wordt gevonden tussen granulaire controle en operationele efficiëntie.


Het Swarm-dashboard toont elk beheerd apparaat de huidige status, prestatiecijfers en snel toegankelijke besturingselementen, zodat snel kan worden gereageerd op prestatieproblemen of wijzigingen in de configuratie. Deze functionaliteit is vooral waardevol voor mijnwerkers die meerdere apparaten op verschillende locaties gebruiken of die vaak mining parameters aanpassen op basis van marktomstandigheden of poolprestaties.


### Configuratiebeheer en systeeminstellingen


Het Instellingen gedeelte van AxeOS biedt uitgebreide controle over elk configureerbaar aspect van uw Bitaxe apparaat, van netwerkverbindingen tot mining parameters en hardware optimalisatie. Netwerkconfiguratie begint met Wi-Fi setup, waar u uw netwerknaam en wachtwoord opgeeft, waarbij AxeOS netwerknamen van één woord zonder spaties aanbeveelt om een betrouwbare verbinding te garanderen. Het systeem handelt het volledige draadloze configuratieproces af en maakt beheer en monitoring op afstand mogelijk.


Mining configuratie concentreert zich op stratum instellingen, waar u de URL van de door u gekozen mining pool specificeert zonder protocol prefixen of poortnummers, die in aparte velden worden behandeld. Het stratum gebruikersveld ondersteunt verschillende poolvereisten, zowel Bitcoin adressen voor solo mining als gebruikersnaamsystemen voor pool mining, met de mogelijkheid om apparaat-id's toe te voegen voor operaties met meerdere apparaten. De recent toegevoegde stratum wachtwoord functionaliteit ondersteunt pools die authenticatie vereisen, hoewel de meeste publieke pools zonder deze vereiste werken.


Hardware optimalisatie door aanpassing van frequentie en kernspanning vertegenwoordigt AxeOS' krachtigste prestatie tuning mogelijkheid. Afhankelijk van uw apparaatversie en browser kunnen deze instellingen verschijnen als vervolgkeuzemenu's met vooraf ingestelde configuraties of als open velden voor aangepaste waarden. De standaardinstellingen van 485 MHz frequentie en 1200 mV kernspanning bieden een stabiele werking voor de eerste tests, terwijl geavanceerde gebruikers deze parameters kunnen optimaliseren voor maximale prestaties of efficiëntie op basis van hun specifieke vereisten en bedrijfsomstandigheden.


### Systeemonderhoud en geavanceerde functies


AxeOS bevat geavanceerde mogelijkheden voor systeemonderhoud die zijn ontworpen om uw Bitaxe-apparaat optimaal te laten presteren en diagnostische informatie te bieden voor probleemoplossing en optimalisatie. Het updatesysteem stroomlijnt het firmwarebeheer door de nieuwste release direct in de interface weer te geven en directe downloadkoppelingen naar officiële firmwarebestanden te bieden. Dankzij deze integratie is het niet langer nodig om handmatig door GitHub repositories te navigeren of bestandsdownloads te beheren, waardoor het updateproces wordt vereenvoudigd tot een paar klikken.


De update-interface accepteert firmwarebestanden met de juiste naam, met name esp-miner.bin en www.bin, waardoor compatibiliteit wordt gegarandeerd en installatiefouten worden voorkomen. Voor gebruikers die problemen ondervinden met het standaard updateproces, biedt AxeOS verwijzingen naar uitgebreide factory flash procedures die apparaten kunnen herstellen naar hun oorspronkelijke functionaliteit. Deze dubbele aanpak is geschikt voor zowel routine-updates als herstelscenario's.


Het logsysteem geeft real-time inzicht in de werking van het apparaat en toont gedetailleerde informatie over ASIC chipmodellen, systeem uptime, Wi-Fi verbindingsstatus, beschikbaar geheugen, firmwareversies en printplaatrevisies. Deze logbestanden zijn van onschatbare waarde voor ontwikkelaars en geavanceerde gebruikers die het gedrag van het apparaat willen begrijpen, problemen willen diagnosticeren of prestaties willen optimaliseren. De real-time logviewer presenteert live operationele gegevens, waaronder nonce-verwerking, moeilijkheidsberekeningen en mining aanmeldingsparameters, en biedt een ongekend inzicht in het mining proces zelf.


Extra systeemfuncties omvatten schermoriëntatieregeling voor apparaten die in aangepaste behuizingen worden gebruikt, ompoling van de ventilator voor speciale koelconfiguraties en automatische ventilatorregeling die de koeling aanpast op basis van de ASIC temperatuur. Handmatige ventilatorsnelheidsregeling biedt nauwkeurig koelbeheer wanneer automatische systemen niet voldoen aan specifieke vereisten. Alle configuratiewijzigingen moeten worden opgeslagen en het apparaat moet opnieuw worden opgestart om van kracht te worden. Dit zorgt voor een stabiele werking en voorkomt gedeeltelijke configuratietoestanden die de prestaties van de mining kunnen beïnvloeden.



# Gemeenschap en samenwerking

<partId>eed1ce48-6752-5744-91f7-91e4e20ff6b2</partId>


## Overzicht Open-Source Bijdragen

<chapterId>715d026e-cebc-536e-a34e-728f5653b999</chapterId>

:::video id=7298ba19-28d2-4a7c-ac0b-44ad0c4770cf:::

### GitHub en zijn rol in softwareontwikkeling


GitHub vertegenwoordigt een fundamentele verschuiving in de manier waarop softwareontwikkelingsprojecten worden beheerd en gedeeld binnen de wereldwijde programmeergemeenschap. Als een cloudgebaseerd platform dat softwareontwikkelingsprojecten host met Git, een gedistribueerd versiebeheersysteem, stelt GitHub ontwikkelaars in staat om naadloos samen te werken aan projecten, ongeacht hun fysieke locatie. Het platform dient als zowel een technisch hulpmiddel als een sociaal netwerk voor programmeurs, waardoor ze wijzigingen kunnen volgen, updates kunnen samenvoegen, verschillende versies van hun code kunnen onderhouden en kunnen bijdragen aan open-source initiatieven zoals het BitX-project van Open Source Miners United.


De kracht van GitHub ligt in het vermogen om het complexe proces van gezamenlijke ontwikkeling te vereenvoudigen. Wanneer meerdere ontwikkelaars aan hetzelfde project werken, biedt GitHub de infrastructuur om bijdragen te beheren, wijzigingen te beoordelen, projectproblemen af te handelen en uitgebreide documentatie te onderhouden. Deze gezamenlijke aanpak heeft GitHub een essentieel onderdeel gemaakt van moderne software ontwikkel workflows, en heeft de manier veranderd waarop zowel individuele ontwikkelaars als grote organisaties project management en het delen van code benaderen.


### Navigeren door de GitHub Interface en Repository Structuur


Het begrijpen van de GitHub interface begint met het herkennen van de belangrijkste elementen waaruit elke repository pagina bestaat. De bovenste navigatiebalk bevat verschillende belangrijke secties, inclusief Code, Issues, Pull Requests, Discussies, Acties, Projecten, Beveiliging en Inzichten. Elke sectie dient een specifiek doel in het ecosysteem van projectbeheer, waarbij de sectie Code de eigenlijke bestanden en mappen weergeeft waaruit het project bestaat.


De structuur van het archief weerspiegelt de organisatorische aanpak van de beheerders van het project. Sommige archieven bevatten slechts een enkel bestand, misschien een eenvoudig shellscript, terwijl andere, zoals het BitX hardwareproject, een groot aantal bestanden in mappen en submappen bevatten. De naam van het archief verschijnt prominent en dient als identificatie en een korte beschrijving van het doel van het project. Essentiële interactieve elementen zijn de Watch-knop voor het ontvangen van meldingen over updates van het archief, de Fork-knop voor het maken van persoonlijke kopieën van het archief en de Star-knop die functioneert als een community-ondersteuningssysteem vergelijkbaar met een "duim omhoog"-functie.


De Over sectie geeft cruciale projectinformatie in een beknopt formaat, inclusief een eenregelige beschrijving, licentie-informatie en belangrijke projectdetails. Voor het BitX project identificeert dit gedeelte het als "open source ASIC Bitcoin mijnbouw hardware" en specificeert de GPL 3.0 licentie. Het begrijpen van licenties is vooral belangrijk omdat GitHub werkt als een open source platform waar publieke repositories toegankelijk zijn voor de hele gemeenschap, maar de inhoud alleen gebruikt en gedistribueerd kan worden volgens de regels van elke licentie.


### Werken met branches en projectversies


Het concept van branches vertegenwoordigt een van GitHub's krachtigste functies voor het beheren van verschillende versies en ontwikkelsporen binnen een enkel project. Een branch creëert in wezen een kopie of aangepaste versie van de hoofdcodebase, waardoor ontwikkelaars aan specifieke features, bugfixes of experimentele veranderingen kunnen werken zonder de primaire ontwikkellijn te beïnvloeden. De master branch dient meestal als de standaard en meest stabiele versie van het project, terwijl extra branches verschillende iteraties, testfases of compleet verschillende productvarianten accommoderen.


In het BitX-hardwareproject bestaan meerdere takken om verschillende hardwareversies en configuraties te beheren. Bijvoorbeeld, de Ultra v2 tak bevat bestanden die specifiek zijn voor die hardware iteratie, terwijl de Super 401 tak zich richt op implementaties die de S21 ASIC chip gebruiken voor verbeterde efficiëntie. Elke branch kan meerdere commits voor of achter de master branch liggen, wat de omvang van de veranderingen en ontwikkelactiviteit aangeeft. Bij het onderzoeken van verschillende takken, zullen gebruikers compleet verschillende bestandsstructuren, documentatie en zelfs visuele representaties opmerken, die de unieke vereisten en specificaties van elke hardwarevariant weerspiegelen.


Het branchesysteem voorkomt verwarring onder bijdragers en gebruikers door verschillende ontwikkelsporen duidelijk te scheiden. In plaats van het mengen van experimentele functies met stabiele releases, of het combineren van verschillende hardwareversies op een enkele locatie, zorgen takken voor een duidelijke scheiding met behoud van de mogelijkheid om succesvolle wijzigingen samen te voegen in de hoofdontwikkellijn wanneer dat nodig is. Deze organisatorische aanpak zorgt ervoor dat gebruikers gemakkelijk de specifieke versie kunnen vinden die ze nodig hebben, terwijl ontwikkelaars aan verbeteringen kunnen werken zonder het primaire project te verstoren.


### Bijdragen door problemen


De Issues sectie dient als het primaire communicatiekanaal tussen gebruikers en projectbeheerders voor het melden van problemen, het voorstellen van verbeteringen en het documenteren van bugs. Het is echter cruciaal om te begrijpen dat de Issues sectie specifiek bedoeld is voor legitieme technische problemen in plaats van algemene vragen of ondersteuningsverzoeken. Wanneer gebruikers echte storingen of onverwacht gedrag tegenkomen, of potentiële verbeteringen identificeren, helpt het maken van een goed gedocumenteerd probleem de hele gemeenschap door de aandacht te vestigen op problemen die meerdere gebruikers kunnen treffen.


Effectieve probleemrapportage vereist gedetailleerde documentatie van het probleem, inclusief de omstandigheden die tot het probleem hebben geleid, stappen om het probleem te reproduceren en alle relevante technische details. Het BitX-project demonstreert dit principe door middel van verschillende gesloten problemen die het oplossingsproces laten zien, van de eerste probleemidentificatie via discussie in de gemeenschap tot de uiteindelijke oplossing. Sommige problemen resulteren in hardwareverbeteringen, zoals het toevoegen van montagegaten om de koelopties te vergroten, terwijl andere kunnen worden opgelost door gebruikerseducatie of software-updates.


Het onderscheid tussen Issues en Discussions is belangrijk voor het onderhouden van georganiseerde interactie binnen de gemeenschap. Terwijl Issues zich richten op specifieke technische problemen, biedt het Discussions gedeelte een forum-achtige omgeving voor vragen, ideeën en algemene community betrokkenheid. Hoewel de Discord server het primaire communicatiekanaal is geworden voor de BitX gemeenschap, blijft de GitHub Discussions sectie beschikbaar voor meer formele of doorzoekbare conversaties die baat hebben bij permanente documentatie en gemakkelijke referentie.


### Pull-aanvragen begrijpen


Pull requests vertegenwoordigen het mechanisme waarmee externe medewerkers wijzigingen voorstellen aan een projectrepository. Wanneer iemand een verbetering, bugfix of nieuwe functie ziet waar het project baat bij zou hebben, kan hij een pull request aanmaken om zijn wijzigingen ter beoordeling en mogelijke integratie in de hoofdcodebase in te dienen. Dit proces zorgt ervoor dat alle wijzigingen worden beoordeeld voordat ze deel gaan uitmaken van het officiële project, waardoor de kwaliteit van de code en de samenhang van het project behouden blijven en bijdragen van de gemeenschap mogelijk worden.


De pull request workflow begint meestal wanneer een bijdrager het repository forkt, zijn eigen kopie maakt waar hij wijzigingen in kan aanbrengen en deze wijzigingen vervolgens terugstuurt naar het originele project door middel van een pull request. Projectbeheerders kunnen dan de voorgestelde wijzigingen bekijken, wijzigingen bespreken met de bijdrager en uiteindelijk beslissen of de wijzigingen worden samengevoegd in het hoofdproject. Dit gezamenlijke reviewproces helpt om de projectstandaarden te behouden terwijl het de deelname en verbetering van de gemeenschap aanmoedigt.


Inzicht in tags en releases voegt nog een laag toe aan projectbeheer en versiebeheer. Tags dienen als markering in de ontwikkeltijdlijn en geven specifieke punten aan die staan voor bepaalde versies of mijlpalen. In hardwareprojecten zoals BitX komen tags vaak overeen met specifieke modelnummers of hardwarerevisies, wat duidelijke referentiepunten biedt voor gebruikers die op zoek zijn naar bepaalde versies. Releases, vaker gebruikt in softwareprojecten, vertegenwoordigen formele distributies van voltooide functies en bugfixes, vaak vergezeld van gedetailleerde release notes en downloadbare pakketten.


Het GitHub ecosysteem creëert een uitgebreide omgeving voor open-source samenwerking die veel verder gaat dan alleen het delen van bestanden. Door deze verschillende componenten en hun juiste gebruik te begrijpen, kunnen bijdragers effectief deelnemen aan projecten, software- en hardwareontwerpen helpen verbeteren en profiteren van de collectieve kennis en inspanning van de wereldwijde ontwikkelgemeenschap. Of je nu problemen rapporteert, verbeteringen voorstelt of code bijdraagt, GitHub biedt de tools en structuur die nodig zijn voor zinvolle samenwerking in de open source wereld.


## Open-Source bijdrage in de praktijk

<chapterId>84d033f5-7182-584f-b1a5-697172bc7a1c</chapterId>

:::video id=7d318fd0-6f0b-422a-9f30-2c470b56951d:::

Voortbouwend op de basis van het maken van issues en het verkennen van open source projecten, richt dit hoofdstuk zich op de praktische aspecten van het leveren van directe bijdragen door middel van pull requests en repository beheer. Begrijpen hoe je fork repositories beheert, wijzigingen aanbrengt en pull requests indient is een cruciale vaardigheid voor elke ontwikkelaar die zinvol wil bijdragen aan open source projecten, of het nu gaat om softwareontwikkeling of hardwareontwerp.


Het proces van het bijdragen van codewijzigingen volgt een gestandaardiseerde workflow die de integriteit van het project waarborgt en tegelijkertijd gezamenlijke ontwikkeling mogelijk maakt. Deze werkwijze houdt in dat je je eigen kopie maakt van een project repository, wijzigingen aanbrengt in een gecontroleerde omgeving en deze wijzigingen vervolgens voorstelt aan het originele project door middel van een formeel review proces. Hoewel de voorbeelden in dit hoofdstuk voornamelijk gericht zijn op softwarebijdragen, zijn dezelfde principes en procedures ook van toepassing op hardwareprojecten met PCB-ontwerpen, schema's en andere technische documentatie.


### Vork- en archiefstructuur begrijpen


De basis van het bijdragen aan elk open source project begint met het maken van een fork, die dient als je persoonlijke kopie van het originele repository. Als je naar een GitHub repository navigeert en op de "fork" knop klikt, creëer je een onafhankelijke kopie onder je eigen GitHub account die een duidelijke verbinding met de originele bron behoudt. Dit gevorkte repository verschijnt in je account met een duidelijke indicatie van zijn oorsprong, met tekst als "gevorkt van [oorspronkelijke-eigenaar]/[repository-naam]" onder de titel van het repository.


Je forked repository werkt onafhankelijk van het origineel, waardoor je wijzigingen kunt maken zonder het hoofdproject te beïnvloeden. Het blijft echter wel op de hoogte van updates aan het originele repository door GitHub's synchronisatie functies. Als het originele repository updates ontvangt die jouw fork mist, toont GitHub statusinformatie zoals "Deze branch loopt X commits achter" of "X commits voor", wat duidelijk inzicht geeft in de relatie tussen jouw fork en het upstream repository. Je kunt je fork op elk moment synchroniseren met de originele repository door op de "Sync fork" knop te klikken, die de laatste wijzigingen van de upstream bron binnenhaalt.


De relatie tussen jouw fork en het originele repository wordt vooral belangrijk als je wijzigingen begint aan te brengen. Als je wijzigingen implementeert en vastlegt op je fork, houdt GitHub deze verschillen bij en toont ze als commits voor het originele repository. Dit volgsysteem maakt het pull request proces mogelijk, waarbij je je wijzigingen kunt voorstellen voor opname in het hoofdproject, terwijl je een duidelijke geschiedenis behoudt van wat er gewijzigd is.


### Je ontwikkelomgeving instellen


Het creëren van een effectieve ontwikkelomgeving vereist zorgvuldige aandacht voor zowel algemene ontwikkeltools als projectspecifieke vereisten. Visual Studio Code is een uitstekende geïntegreerde ontwikkelomgeving (IDE) voor de meeste open source bijdragen en biedt essentiële functies voor codebewerking, versiebeheerintegratie en projectbeheer. Het eerste kritieke onderdeel is het installeren en configureren van de Git extensie, die naadloze integratie met GitHub repositories direct vanuit je ontwikkelomgeving mogelijk maakt.


Moderne versies van Visual Studio Code bevatten standaard ondersteuning voor Git, maar je moet je authenticeren met je GitHub account om volledige functionaliteit mogelijk te maken. Dit authenticatieproces houdt in dat je je aanmeldt bij GitHub via de IDE, waarmee je direct vanuit je ontwikkelomgeving repositories kunt clonen, wijzigingen kunt vastleggen en updates kunt pushen. De GitHub-integratie verschijnt als een pictogram in de linker zijbalk en biedt toegang tot het klonen van repositories, branchbeheer en synchronisatiefuncties zonder dat commandoregelbewerkingen nodig zijn.


Voor projecten met embedded systemen of specifieke hardwareplatforms zijn extra tools nodig. De ESP-IDF uitbreiding is een cruciale component voor projecten die gericht zijn op ESP32 microcontrollers en vereist specifieke versiecompatibiliteit om de juiste functionaliteit te garanderen. Het installatieproces omvat het selecteren van de juiste ESP-IDF versie, het configureren van toolpaden en het opzetten van de ontwikkelcontaineromgeving. Versie 5.1.3 vertegenwoordigt momenteel de aanbevolen configuratie voor veel ESP32-gebaseerde projecten, hoewel deze vereisten kunnen veranderen als projecten hun afhankelijkheden en toolchains bijwerken.


### Wijzigingen maken en Commits beheren


Zodra je ontwikkelomgeving goed is geconfigureerd, begint het proces om zinvolle bijdragen te leveren met het downloaden of klonen van je gevorkte repository naar je lokale machine. Je kunt dit doen door een ZIP-bestand van de inhoud van de repository te downloaden of door de geïntegreerde kloonfunctionaliteit van Visual Studio Code te gebruiken, die een meer gestroomlijnde workflow voor doorlopende ontwikkeling biedt. Het kloonproces creëert een lokale kopie van je repository die gesynchroniseerd blijft met je GitHub fork, zodat je offline kunt werken met behoud van versiebeheer.


Als je met de lokale repository werkt, krijg je toegang tot de volledige projectstructuur, inclusief broncodebestanden, configuratiebestanden, documentatie en eventuele hardwareontwerpbestanden. De meeste firmwareprojecten maken gebruik van programmeertalen zoals C voor de kernfunctionaliteit, met aanvullende componenten geschreven in TypeScript voor gebruikersinterfaces of Java voor specifieke hulpprogramma's. Inzicht in de projectstructuur helpt u bij het identificeren van de juiste bestanden om aan te passen en zorgt ervoor dat uw wijzigingen in lijn zijn met de architectuurpatronen en coderingsstandaarden van het project.


Het commit proces vertegenwoordigt een fundamenteel aspect van versiebeheer dat zorgvuldige aandacht vereist voor zowel technische nauwkeurigheid als communicatieve duidelijkheid. Voordat je wijzigingen aanbrengt, moet je de bestaande code grondig begrijpen en alle wijzigingen in je lokale omgeving testen. De kardinale regel van open source bijdragen benadrukt dat je nooit ongeteste code moet publiceren, omdat dit bugs of veiligheidslekken kan introduceren die de hele projectgemeenschap kunnen beïnvloeden. Daarnaast mag je nooit gevoelige informatie zoals wachtwoorden, API tokens of persoonlijke gegevens in openbare repositories plaatsen, omdat deze informatie permanent toegankelijk is voor iedereen met toegang tot de repository.


### Pull-aanvragen aanmaken en beheren


Het hoogtepunt van je bijdrage is het maken van een pull request, wat dient als een formeel voorstel om je wijzigingen samen te voegen in het originele project repository. Dit proces begint in je GitHub fork, waar je de verschillen tussen jouw repository en de upstream broncode kunt bekijken. GitHub's interface laat duidelijk het aantal commits voor of achter zien, wat direct inzicht geeft in de reikwijdte van je voorgestelde wijzigingen. Voordat je een pull request aanmaakt, moet je ervoor zorgen dat je fork gesynchroniseerd is met de laatste upstream wijzigingen om potentiële conflicten te minimaliseren.


Het maken van een effectief pull request vereist meer dan alleen het indienen van je codewijzigingen. De beschrijving van het pull-verzoek is jouw kans om het doel, de reikwijdte en de impact van je wijzigingen te communiceren naar de beheerders van het project en de gemeenschap. Een goed geschreven beschrijving legt uit welke problemen je wijzigingen aanpakken, hoe je de oplossing hebt geïmplementeerd en wat de mogelijke implicaties zijn voor andere delen van het project. Deze documentatie is vooral belangrijk bij complexe wijzigingen die misschien niet direct duidelijk zijn als je alleen naar de verschillen in de code kijkt.


Het reviewproces vertegenwoordigt een gezamenlijk aspect van open source ontwikkeling waarbij projectbeheerders en ervaren medewerkers uw voorgestelde wijzigingen evalueren. Je kunt specifieke reviewers vragen die expertise hebben in de gebieden waar je wijzigingen invloed op hebben, zodat je er zeker van kunt zijn dat goed geïnformeerde leden van de gemeenschap je werk bekijken. Het reviewproces kan meerdere iteraties inhouden, waarbij reviewers feedback geven, wijzigingen vragen of om extra testen vragen. Dit gezamenlijke verfijningsproces helpt de kwaliteit van de code te behouden en biedt waardevolle leermogelijkheden voor medewerkers van alle ervaringsniveaus.


Begrijpen dat niet alle pull requests worden geaccepteerd helpt om de juiste verwachtingen te stellen aan het bijdrageproces. Projectbeheerders kunnen pull requests om verschillende redenen afwijzen, waaronder het niet aansluiten bij de projectdoelen, onvoldoende testen of het bestaan van alternatieve oplossingen die al in ontwikkeling zijn. In plaats van een afwijzing te zien als een mislukking, moet het worden gezien als een kans om te leren van de feedback, de aanpak te verfijnen en mogelijk alternatieve oplossingen bij te dragen die beter voldoen aan de behoeften van het project. De open source gemeenschap gedijt op dit iteratieve proces van voorstellen, beoordeling en verfijning dat uiteindelijk projecten vooruit stuwt door collectieve inspanning en gedeelde expertise.



## Wat is Public-Pool?

<chapterId>b461bf94-4a90-5bb8-ba3f-976d5d57be0d</chapterId>


:::video id=d4652496-1ed4-4415-8048-0b6871b9ed51:::

Public Pool vertegenwoordigt een revolutionaire benadering van Bitcoin mining die veel van de zorgen wegneemt die mijners hebben met traditionele mining pools. Als een volledig open-source solo Bitcoin mining pool, verandert Public Pool fundamenteel het beloningsdistributiemodel waaraan mijners gewend zijn geraakt. In tegenstelling tot conventionele mining pools waar deelnemers beloningen delen wanneer een miner in de pool een blok vindt, werkt Public Pool volgens het solo mining principe waar individuele miners 100% van hun blokbeloningen behouden wanneer ze met succes een blok mijnen.


De meest aantrekkelijke eigenschap van Public Pool is de gratis structuur. Wanneer miners succesvol een blok vinden met behulp van Public Pool, ontvangen ze de volledige blokbeloning samen met alle bijbehorende transactiekosten, zonder enige aftrek voor operationele poolkosten. Dit staat in schril contrast met traditionele mining pools die doorgaans kosten in rekening brengen variërend van 1-3% van mining beloningen. Het zero-fee model maakt Public Pool bijzonder aantrekkelijk voor miners die hun potentiële opbrengsten willen maximaliseren en toch de volledige controle over hun mining operaties willen behouden.


Om de unieke positie van Public Pool te begrijpen, is het belangrijk om het fundamentele verschil tussen solo mining en gepoold mining te begrijpen. Echt solo mining betekent dat je onafhankelijk mijnt en de volledige blokbeloning (momenteel 3,125 BTC + kosten) ontvangt als je een blok vindt, maar de waarschijnlijkheid is evenredig met jouw hashsnelheid ten opzichte van het hele netwerk, wat extreme variantie creëert die maanden of jaren kan duren tussen beloningen. Traditionele pools combineren hashkracht om vaker blokken te vinden, verdelen de beloningen evenredig en zorgen voor een vast, voorspelbaar inkomen. Voor miners met een aanzienlijk kapitaal geïnvesteerd in hardware en operationele kosten, is pure solo mining meestal onpraktisch, ongeacht de filosofische voordelen - de variantie maakt het bijna onmogelijk om de elektriciteitskosten te dekken en investeringen terug te verdienen. Deze economische realiteit betekent dat de meeste mijnbouwers om praktische financiële redenen voor gepoold mining zullen kiezen. Public Pool werkt als een solo mining pool, wat betekent dat je nog steeds te maken hebt met de variantie van solo mining (je wordt alleen beloond als je persoonlijk een blok vindt), maar je profiteert van de infrastructuur van de pool en de transparante, gratis werking.


### Het Open Source Voordeel en Technische Implementatie


Public Pool's toewijding aan open-source ontwikkeling biedt mijnwerkers ongekende transparantie en controle over hun mining operaties. De volledige codebase is beschikbaar op GitHub, waardoor mijnwerkers precies kunnen zien hoe de software werkt, deze kunnen aanpassen aan hun behoeften en zelfs kunnen bijdragen aan de ontwikkeling ervan. Deze transparantie pakt een belangrijke zorg in de mining gemeenschap aan over de onbekende configuraties en praktijken van traditionele mining pools.


De softwarearchitectuur omvat zowel de kernfunctionaliteit van mining Pool als een aparte repository voor de gebruikersinterface, die beide vrij te downloaden en aan te passen zijn. Mijnwerkers kunnen Public Pool in verschillende configuraties draaien, waaronder Docker-containers, waardoor het kan worden aangepast aan verschillende hardwareopstellingen en technische voorkeuren. De uitgebreide documentatie in de GitHub repositories biedt gedetailleerde installatiegidsen, configuratieopties en wijzigingsinstructies, waardoor het toegankelijk is voor mijnwerkers met verschillende niveaus van technische expertise.


Verbinding maken met Public Pool vereist minimale configuratie in vergelijking met traditionele mining setups. Mijnwerkers hoeven alleen hun mining apparaten te configureren met de Stratum verbindingsgegevens en hun Bitcoin adres als gebruikersnaam op te geven. Een optionele werkersnaam kan worden toegevoegd na een puntscheidingsteken voor organisatorische doeleinden.


### Gemeenschapskenmerken en duurzaamheidsmodel


Public Pool bevat verschillende innovatieve functies die de Bitcoin mining gemeenschap versterken, terwijl de gratis werking gehandhaafd blijft. Het platform toont uitgebreide statistieken, waaronder de totale hashsnelheid van aangesloten miners, die in 2024 varieerde tussen 1 en 2 PetaHash per seconde en rond 40 PH/s in november 2025, en geeft gedetailleerde informatie over aangesloten mining apparaten. Bijzonder opmerkelijk is de nadruk van het platform op open-source mining hardware, met apparaten gemarkeerd met sterren die volledig open-source ontwerpen aangeven, compleet met links naar hun respectievelijke GitHub repositories.


De duurzaamheid van Public Pool's zero-fee operatie is gebaseerd op een creatief affiliate programma partnerschap met mining hardwareleveranciers. Wanneer miners apparatuur kopen van partnerbedrijven met de kortingscode "SOLO", ondersteunt vijftig procent van de affiliate-inkomsten de operationele kosten van Public Pool, terwijl de resterende vijftig procent wordt uitgekeerd als beloning aan miners die elke maand de hoogste moeilijkheidsgraad halen. Dit model creëert een symbiotische relatie waarbij miners korting krijgen op de aankoop van apparatuur, leveranciers klanten winnen en Public Pool zijn activiteiten onderhoudt zonder directe kosten in rekening te brengen.


### Decentralisatiefilosofie en beste praktijken


Hoewel Public Pool een uitstekend alternatief biedt voor traditionele mining pools, is het belangrijk om de rol ervan te begrijpen binnen de bredere context van Bitcoin decentralisatie. Het platform dient als een opstapje naar het uiteindelijke doel van individuele miners die hun eigen mining pools runnen. Het runnen van je eigen mining pool vertegenwoordigt het hoogste niveau van decentralisatie, omdat het de afhankelijkheid van infrastructuur of software van derden elimineert, ongeacht hoe transparant of goedbedoeld die derde partij ook mag zijn.


De open-source aard van Public Pool maakt het een ideaal leerplatform voor mijnwerkers die de werking van de pool willen begrijpen voordat ze hun eigen oplossingen implementeren. De beschikbaarheid van installatiegidsen voor meerdere besturingssystemen en de uitgebreide documentatie voorzien mijnwerkers van de kennis die nodig is om over te stappen van het gebruik van Public Pool naar het beheren van hun eigen mining infrastructuur. Dit educatieve aspect is in lijn met Bitcoin's fundamentele principes van zelfsoevereiniteit en decentralisatie, waardoor individuele mijnwerkers volledige controle krijgen over hun mining operaties, terwijl ze bijdragen aan de algemene veiligheid en decentralisatie van het Bitcoin netwerk.


De gebruikersinterface van het platform biedt miners gedetailleerde bewakingsmogelijkheden, waaronder de status van werkers, statistieken over de hashsnelheid en prestatiecijfers. Deze functies helpen mijnwerkers hun activiteiten te optimaliseren terwijl ze leren over poolbeheerprincipes die ze later kunnen toepassen op hun eigen mining poolimplementaties.


## Hoe installeer ik Public-Pool op Umbrel?

<chapterId>7f6d0307-7715-5581-89ea-f13cf8754f9a</chapterId>


:::video id=3a4fe0a9-bbf5-458a-8ec1-52c3b83afd87:::

Je eigen Bitcoin mining pool thuis beheren is steeds toegankelijker geworden met moderne hardware en vereenvoudigde softwareoplossingen. Dit hoofdstuk onderzoekt de praktische implementatie van een openbaar zwembad thuis met behulp van betaalbare mini PC hardware en gestroomlijnde node management software. Aan het einde van deze gids zult u de hardwarevereisten, het software-instelproces en de basisconfiguratie begrijpen die nodig zijn om uw eigen mining poolinfrastructuur op te zetten.


### Hardwarevereisten en installatie


De basis van elke mining zwembadinstallatie thuis begint met het kiezen van geschikte hardware die prestaties, kosten en energie-efficiëntie in balans brengt. Een mini PC is een ideale oplossing voor deze toepassing, die voldoende rekenkracht biedt terwijl hij compact blijft en een redelijk energieverbruik heeft. De aanbevolen configuratie omvat een Intel N100 processor, die voldoende rekenkracht biedt voor pooloperaties, in combinatie met ten minste één terabyte NVMe-opslag om de Bitcoin blockchain en bijbehorende gegevens te huisvesten.


De opslagvereisten zijn bijzonder kritisch omdat het draaien van een mining pool het onderhouden van een volledig gesynchroniseerde Bitcoin node vereist. De NVMe schijf van één terabyte zorgt voor snelle lees/schrijfbewerkingen die essentieel zijn voor blockchain synchronisatie en lopende transactieverwerking. Bovendien ondersteunt voldoende RAM-toewijzing een soepele werking van zowel het onderliggende Linux-besturingssysteem als de nodebeheersoftware die de poolactiviteiten coördineert.


### Softwarearchitectuur en knooppuntbeheer


De softwarestack voor een mining pool bouwt voort op een Linux basis, die de stabiliteit en veiligheid biedt die nodig is voor Bitcoin operaties. Bovenop dit basissysteem creëert gespecialiseerde nodebeheersoftware zoals Umbrel een intuïtieve interface voor het beheren van de Bitcoin infrastructuur. Deze aanpak abstraheert veel van de complexiteit die traditioneel geassocieerd wordt met het draaien van Bitcoin nodes, waardoor de werking van de pool toegankelijk wordt voor gebruikers zonder uitgebreide technische achtergrond.


Umbrel dient als een uitgebreid platform voor knooppuntbeheer dat de installatie, synchronisatie en het lopende onderhoud van Bitcoin Core afhandelt via een webgebaseerde interface. Het app store model van het platform maakt eenvoudige installatie van aanvullende diensten mogelijk, waaronder mining pool software, door middel van eenvoudige point-and-click operaties. Deze architectuur zorgt ervoor dat gebruikers zich kunnen richten op het gebruik van de pool in plaats van op systeembeheer, terwijl ze toch volledige controle houden over hun Bitcoin infrastructuur.


### Openbare zwembadinstallatie en -configuratie


Het installeren van openbare zwembadsoftware via het Umbrel-platform demonstreert de gestroomlijnde aard van de moderne Bitcoin infrastructuurimplementatie. Het proces begint met toegang tot de Umbrel app store via de webinterface, waar een eenvoudige zoekopdracht naar "public pool" de beschikbare mining poolsoftware laat zien. De installatie vereist slechts een paar klikken: de toepassing selecteren, de installatie bevestigen en wachten tot het geautomatiseerde installatieproces is voltooid.


Het installatieproces configureert automatisch de nodige verbindingen tussen de publieke poolsoftware en het onderliggende Bitcoin knooppunt. Deze integratie zorgt ervoor dat de pool transacties kan valideren, blokkensjablonen kan maken en werk kan verdelen onder aangesloten miners zonder dat er handmatige configuratie van complexe netwerkparameters nodig is. Zodra de installatie is voltooid, wordt de poolinterface onmiddellijk toegankelijk via het lokale netwerk, waardoor realtime monitoring- en beheermogelijkheden worden geboden.


### Mijnwerkers aansluiten en netwerkoverwegingen


mining hardware verbinden met uw nieuw opgerichte pool vereist het configureren van de poolinstellingen van de miner om naar uw lokale infrastructuur te wijzen. Dit houdt in dat u het standaard pooladres vervangt door uw lokale IP-adres en het juiste poortnummer dat tijdens de openbare poolinstallatie werd toegewezen. Deze configuratiewijziging leidt de rekeninspanningen van uw mining hardware om van externe pools naar uw thuisgebaseerde infrastructuur, waardoor u de volledige controle behoudt over de mining activiteiten en potentiële beloningen.


Netwerkconfiguratie speelt een cruciale rol in de toegankelijkheid en functionaliteit van de pool. Lokale netwerkinstellingen bestaan meestal uit standaard IP-adressering, maar gebruikers kunnen te maken krijgen met variaties in DNS-omzetting, afhankelijk van hun routerconfiguratie. Sommige routers bieden lokale DNS-diensten die vriendelijke namen aanmaken voor lokale diensten, terwijl andere routers directe IP-adrestoegang vereisen. Voor bredere toegankelijkheid buiten het lokale netwerk kan het nodig zijn om port forwarding op de router te configureren, hoewel dit extra veiligheidsoverwegingen met zich meebrengt die een zorgvuldige evaluatie van de bijbehorende risico's en voordelen vereisen.


De succesvolle oprichting van een mining thuispool betekent een belangrijke stap in de richting van een gedecentraliseerde Bitcoin infrastructuur, die zowel educatieve waarde als praktische mining mogelijkheden biedt, terwijl u volledige controle houdt over uw Bitcoin activiteiten.


# Hardware-assemblage en probleemoplossing

<partId>f6987088-5ba4-52e2-b2d0-aa122080940c</partId>


## Welke hulpmiddelen moet ik gebruiken?

<chapterId>733935b5-0171-5a22-838c-e192df6f7ccf</chapterId>


:::video id=bddd0e47-7b43-4685-ba2e-bf3a8ff653c9:::

In de wereld van SMD-solderen, vooral bij Bitaxe-projecten, maakt het hebben van het juiste gereedschap het verschil tussen frustratie en succes. Deze uitgebreide gids behandelt de essentiële apparatuur die nodig is om SMD-soldeerprojecten effectief aan te pakken, van basishandgereedschap tot gespecialiseerde apparatuur die uw soldeervaardigheden zal verbeteren.


Als je documentatie over de schema's wilt bekijken, kijk dan eens naar deze [GitHub repo](https://github.com/skot/bitaxe-doc/tree/main).


### Basis handgereedschap en precisie-instrumenten


De basis van elke SMD-soldeerinstallatie begint met een pincet van goede kwaliteit, dat dient als uw belangrijkste gereedschap voor het plaatsen van componenten. Twee soorten pincetten zijn hierbij het meest waardevol: de standaardpincetten met rechte punten en pincetten met een licht gebogen punt. De pincet met rechte punten kan de meeste SMD-componenten aan die te vinden zijn in Bitaxe-kits, terwijl de pincet met gebogen punten uitblinkt bij het werken met extreem kleine componenten die nauwkeurig geplaatst moeten worden. Deze gereedschappen worden vaak meegeleverd met reparatiesets, zoals iFixit-sets voor telefoonreparaties, waardoor ze voor de meeste hobbyisten gemakkelijk verkrijgbaar zijn.


Als aanvulling op de pincet is een goede schaar onmisbaar voor het knippen van isolatietape, dat meerdere doelen dient bij elektronicaprojecten. Isolatietape is essentieel voor de isolatie van kabels en componenten en als je kwaliteitstape bij de hand hebt, stroomlijn je het soldeerproces. Deze basisbenodigdheden kunnen worden gekocht bij bouwmarkten of online retailers zonder dat er gespecialiseerde elektronicaleveranciers nodig zijn.


### Soldeerpasta toepassing en beheer


Het aanbrengen van soldeerpasta is een van de meest kritische aspecten van SMD-solderen en de juiste hulpmiddelen maken dit proces zowel nauwkeurig als plezierig. Kleine, niet scherpe injectiespuiten gevuld met soldeerpasta bieden uitzonderlijke controle over de plaatsing van de pasta. Deze methode maakt het mogelijk om precies de hoeveelheid soldeerpasta aan te brengen die nodig is voor elke verbinding en de meeste mensen ontwikkelen snel de juiste techniek voor het controleren van druk en stroomsnelheid door praktische oefening.


De keuze van de soldeerpasta zelf is van grote invloed op het soldeersucces. ChipQuik TS391SNL50 onderscheidt zich als een uitzonderlijke soldeerpasta voor Bitaxe-projecten en algemeen SMD-werk. Deze pasta behoudt de juiste consistentie en smeltkenmerken en voorkomt de problemen van goedkopere alternatieven met een te laag smeltpunt. Soldeerpasta's van lage kwaliteit kunnen problemen veroorzaken waarbij eerder gesoldeerde verbindingen weer vloeibaar worden bij verhitting van aangrenzende gebieden, wat leidt tot verplaatsing van componenten en slechte verbindingen. Hoewel soldeerpasta van hoge kwaliteit een hogere initiële investering betekent, rechtvaardigen de verbeterde resultaten en verminderde frustratie de kosten.


### Tools voor probleemoplossing en opruimen


Zelfs ervaren soldeerders komen problemen tegen die gecorrigeerd moeten worden, waardoor desoldeerapparatuur essentieel is voor elke complete gereedschapskist. Een desoldeerinstallatie, in wezen een verwarmd vacuümgereedschap, verwijdert overtollig soldeer en corrigeert overbrugde verbindingen tussen pinnen van componenten. Dit gereedschap werkt het meest effectief in combinatie met vloeimiddel, waardoor het soldeer beter vloeit en het desoldeerproces efficiënter verloopt.


Vloeimiddel is er in verschillende vormen, waaronder vaste en vloeibare varianten, en dient meerdere doelen naast hulp bij het desolderen. Wanneer soldeerpasta zijn effectiviteit begint te verliezen tijdens lange werksessies, herstelt het aanbrengen van extra vloeimiddel de juiste vloei-eigenschappen en zorgt het voor betrouwbare verbindingen. Een klein lepelvormig gereedschap, vaak te vinden in precisiereparatiesets, vergemakkelijkt het nauwkeurig aanbrengen van vloeimiddel op specifieke plaatsen zonder de omringende componenten te vervuilen.


Het schoonmaken van het bord is de laatste stap in het werk van professionele kwaliteit en vereist isopropanol alcohol en een speciale reinigingsborstel. Een oude tandenborstel werkt perfect voor dit doel en met een knijpfles met isopropanol kan de reinigingsoplossing gecontroleerd worden aangebracht. Deze combinatie verwijdert fluxresten en pastaresten, waardoor de printplaat er schoon en professioneel uitziet en de inspectie van soldeerverbindingen wordt vergemakkelijkt.


### Gespecialiseerde apparatuur en geavanceerd gereedschap


Voor projecten met complexe geïntegreerde schakelingen, in het bijzonder ASIC's, transformeren sjablonen het soldeerproces van moeizame handplaatsing naar het efficiënt en nauwkeurig aanbrengen van pasta. Deze nauwkeurig gesneden sjablonen zorgen voor een consistente dikte en plaatsing van de pasta, waardoor de tijd die nodig is voor complexe componenten drastisch wordt verkort en de betrouwbaarheid wordt verbeterd. De investering in kwaliteitsstencils betaalt zich terug in zowel tijdsbesparing als verbeterde resultaten.


Thermisch beheer wordt cruciaal bij het werken met vermogenscomponenten, waardoor thermische pasta of thermisch vet essentiële benodigdheden worden. Deze materialen zorgen voor een goede warmteoverdracht tussen koellichamen en geïntegreerde schakelingen, waardoor thermische schade wordt voorkomen en een betrouwbare werking wordt gegarandeerd. Thermische interfacematerialen van hoge kwaliteit zijn een kleine investering die veel duurdere componenten beschermen.


Het hart van elke SMD-soldeerinstallatie is het hetelucht-reworkstation, dat de gecontroleerde warmte levert die nodig is voor oppervlakte-montagewerk. Hoewel budgetstations van $30-50 voldoende kunnen presteren, missen ze vaak de betrouwbaarheid en precisie van duurdere apparatuur. Deze basisstations werken meestal effectief bij 355°C en hebben een automatische temperatuurverlaging wanneer het handstuk terug in de houder wordt geplaatst. Hun betrouwbaarheid kan echter inconsistent zijn en sommige apparaten gaan voortijdig stuk. Voor het serieuze werk biedt een investering in apparatuur van hogere kwaliteit van gespecialiseerde elektronicaleveranciers een betere waarde op lange termijn door een betere betrouwbaarheid en een nauwkeurigere temperatuurregeling.


De combinatie van deze gereedschappen zorgt voor een complete SMD-soldeercapaciteit die veel verder gaat dan Bitaxe-projecten en ook geschikt is voor algemeen elektronicawerk. Als u de rol van elk gereedschap begrijpt en kwaliteitsapparatuur kiest die past bij uw vaardigheidsniveau en projectvereisten, bent u verzekerd van succesvolle resultaten en een plezierige soldeerervaring.



## Problemen met solderen oplossen

<chapterId>96663744-b4f7-5154-930f-a68ba7954603</chapterId>


:::video id=9286c0dc-acd6-44d9-b34e-59cfb2da9748:::


De Bitaxe transceiverkit stelt ons voor unieke uitdagingen tijdens de assemblage, waarbij we zorgvuldig moeten letten op de oriëntatie van de componenten, het voorkomen van soldeerbruggen en de juiste warmtehuishouding. Inzicht in deze veel voorkomende problemen en hun oplossingen is essentieel voor het succesvol bouwen van kits en het voorkomen van kostbare schade aan componenten. In dit hoofdstuk worden de meest voorkomende soldeerproblemen tijdens de assemblage van Bitaxe besproken en worden praktische technieken gegeven om ze te identificeren en op te lossen.


### Componentoriëntatie en -identificatie


De juiste oriëntatie van componenten is een van de belangrijkste aspecten van succesvolle Bitaxe-assemblage, vooral bij MOSFET's Q1 en Q2. Deze componenten hebben opvallende oriëntatiemarkeringen die zorgvuldig in acht moeten worden genomen tijdens de installatie. Elke MOSFET heeft een kleine puntmarkering die overeenkomt met specifieke pad-rangschikkingen op de printplaat. De sleutel tot de juiste oriëntatie ligt in het begrijpen van de fysieke structuur van deze componenten, die vier pinnen hebben met één groot pad en drie kleinere pads die geen verbinding hebben met het grote pad.


Bij het installeren van Q1 en Q2 moet u zowel de component als de printplaat zorgvuldig onderzoeken. De lay-out van de printplaat toont duidelijk de bedoelde oriëntatie door de padconfiguratie, met vier pinnen die zo gepositioneerd zijn dat ze overeenkomen met de MOSFET-structuur. Voordat u een grote component soldeert, moet u altijd de oriëntatie controleren door de fysieke markeringen van de component te vergelijken met de padindeling op de printplaat. Deze eenvoudige controlestap voorkomt de frustratie van het desolderen en opnieuw installeren van verkeerd georiënteerde componenten.


De gevolgen van onjuiste oriëntatie reiken verder dan eenvoudige functionaliteitsproblemen. Verkeerd georiënteerde MOSFET's kunnen storingen in het circuit veroorzaken die moeilijk te diagnosticeren zijn en waarvoor mogelijk complete vervanging van onderdelen nodig is. Als u de tijd neemt om de oriëntatie te controleren voordat u de warmte toepast, zorgt u ervoor dat het circuit goed werkt en voorkomt u onnodige probleemoplossing later in het assemblageproces.


### Soldeerbruggen en soldeeroverschotten beheren


Soldeerbruggen vormen een andere veelvoorkomende uitdaging bij Bitaxe-assemblage, vooral rond componenten met een fijne steek zoals U10. Deze ongewenste verbindingen tussen aangrenzende pinnen kunnen circuitstoringen veroorzaken en vereisen zorgvuldige verwijderingstechnieken. De meest effectieve aanpak is het gebruik van desoldeerlitze, een gevlochten kopermateriaal dat overtollig soldeer absorbeert bij verhitting. Deze techniek vereist geduld en de juiste keuze van gereedschap om beschadiging van kwetsbare componenten te voorkomen.


Gebruik bij soldeerbruggen op geïntegreerde schakelingen een printplaathouder of scharnierklem om het onderdeel tijdens het werk stevig vast te houden. Breng zachte hitte aan op het aangetaste gebied en trek de desoldeerlitze voorzichtig over de overbrugde verbindingen. De koperen vlecht absorbeert op natuurlijke wijze het overtollige soldeer en scheidt de ongewenste verbindingen. Dit proces kan meerdere pogingen vereisen, maar volharding levert schone, goed gescheiden verbindingen op.


Preventie blijft de beste aanpak van soldeerbrugvorming. Het gebruik van de juiste hoeveelheden soldeerpasta en een vaste hand tijdens het plaatsen van componenten vermindert de vorming van bruggen aanzienlijk. Als er toch bruggen ontstaan, pak ze dan onmiddellijk aan in plaats van te hopen dat ze de werking van het circuit niet beïnvloeden. Zelfs schijnbaar kleine bruggen kunnen aanzienlijke functionaliteitsproblemen veroorzaken die moeilijk te diagnosticeren zijn zodra de printplaat volledig geassembleerd is.


### Kritische onderdelen en speciale overwegingen


De buck converter U9 verdient bijzondere aandacht vanwege zijn kritieke rol in het omzetten van 5 volt naar 1,2 volt voor de ASIC chip. Deze component vormt een unieke uitdaging vanwege de vijf kleine aansluitingen en de neiging tot defecten. Correcte installatie vereist nauwkeurig aanbrengen van soldeerpasta en zorgvuldige warmtehuishouding. Onvoldoende soldeerpasta onder U9 kan resulteren in slechte verbindingen die een goede spanningsomzetting verhinderen, terwijl een teveel aan pasta bruggen kan creëren die circuitstoringen veroorzaken.


U9 produceert kenmerkende audiosignalen wanneer er problemen zijn met de soldeerbrug, door hoogfrequente ruis te genereren die afwijkt van de normale werking van de ASIC. Deze auditieve diagnosetechniek kan helpen bij het identificeren van problemen, maar vereist een goed gehoor voor hoge frequenties. Deze auditieve diagnosetechniek kan helpen bij het identificeren van problemen, maar vereist een goed gehoor voor hoge frequenties. Wanneer audiodiagnose niet mogelijk is, is visuele inspectie essentieel. Onderzoek alle aansluitingen zorgvuldig, zoek naar bruggen of onvoldoende soldeerdekking.


Als U9 er niet in slaagt de vereiste 1,2 volt uit te sturen ondanks dat hij goed gesoldeerd lijkt te zijn, beschouw dan onvoldoende soldeerpasta als de waarschijnlijke oorzaak. Verwijder het onderdeel, breng een kleine hoeveelheid extra soldeerpasta aan en installeer het opnieuw. Als afzonderlijke pinnen onvoldoende soldeer bevatten, breng dan voorzichtig met een pincet kleine hoeveelheden soldeerpasta aan op specifieke locaties. De soldeerpasta vloeit vanzelf onder de component wanneer deze wordt verwarmd, waardoor de juiste verbindingen ontstaan door capillaire werking.


### Hittebeheer en onderdelenbescherming


Goed warmtebeheer beschermt gevoelige componenten tegen thermische schade en zorgt voor betrouwbare soldeerverbindingen. Componenten zoals de kristaloscillator Y1 en U1 zijn bijzonder gevoelig voor langdurige blootstelling aan hitte en vereisen een zorgvuldige temperatuurregeling. Houd de temperatuur van de soldeerbout op 350 graden Celsius, maar minimaliseer de tijd dat de warmte wordt toegepast om schade aan de componenten te voorkomen. Snelle, efficiënte soldeertechnieken beschermen deze gevoelige componenten en zorgen voor betrouwbare verbindingen.


De ASIC chip vereist speciale behandelingstechnieken vanwege de complexe pinstructuur en gevoeligheid voor mechanische spanning. Wanneer u stencils gebruikt voor het aanbrengen van soldeerpasta, zorg dan voor een gelijkmatige dekking over alle pinnen om ongelijkmatige plaatsing van componenten te voorkomen. Als te veel soldeerpasta ervoor zorgt dat de ASIC ongelijk zit, laat de assemblage dan volledig afkoelen voordat u correcties aanbrengt. Oefen alleen lichte druk uit op de gelabelde randen van de component, nooit op het centrale matrijsgebied, tijdens het opnieuw opwarmen om de juiste plaatsing te bereiken.


Component U8 vormt een unieke uitdaging vanwege het grote aantal pennen en de kans op verbogen aansluitdraden. Als de pennen tijdens het hanteren worden verbogen, gebruikt u een printplaathouder of een beweegbare klem om het onderdeel vast te zetten en trekt u de betreffende pennen voorzichtig recht. Werk langzaam en geduldig om te vermijden dat de delicate draden breken. Begrijpen dat bepaalde pingroepen op U8 intern verbonden zijn, kan het oplossen van problemen vereenvoudigen, aangezien bruggen tussen deze specifieke pinnen de werking van het circuit niet beïnvloeden. Bruggen tussen andere pinnen moeten echter voorzichtig verwijderd worden om een goede werking te garanderen.


## Uw Bitaxe debuggen met AxeOS

<chapterId>603f5c0d-4b7c-51e1-9bad-318a8b8e9db7</chapterId>

:::video id=d23d748b-510e-4748-9617-b875da757031:::

Bij het werken met Bitaxe mining apparaten kunnen hardwarestoringen zich op verschillende manieren manifesteren die niet onmiddellijk duidelijk zijn. Als u begrijpt hoe u deze problemen systematisch kunt diagnosticeren met behulp van het AxeOS besturingssysteem, kunt u veel tijd besparen en onnodige vervanging van onderdelen voorkomen. Dit hoofdstuk verkent de diagnosetechnieken en probleemoplossingsmethoden die ervaren technici gebruiken om specifieke hardwareproblemen te identificeren via softwareanalyse.


### Indicatoren voor stroomverbruik begrijpen


De eerste en meest kritische diagnostische indicator in AxeOS is de controle van het stroomverbruik. Normale Bitaxe apparaten, waaronder de Bitaxe Ultra en Bitaxe Supra modellen, verbruiken tussen de 10 en 17 watt tijdens standaard gebruik. Deze basismeting dient als primaire gezondheidsindicator voor het hele systeem. Wanneer het stroomverbruik aanzienlijk daalt onder dit bereik, met name onder de 3 watt, duidt dit op een fundamenteel probleem met de ASIC chip of de ondersteunende circuits.


Scenario's met laag stroomverbruik vereisen onmiddellijke aandacht omdat ze aangeven dat de mining chip ofwel helemaal niet functioneert of in een ernstig gedegradeerde toestand werkt. Deze meting alleen al kan u helpen om snel een onderscheid te maken tussen prestatieproblemen en volledige hardwarestoringen. De vermogensmeting in AxeOS biedt real-time feedback waarmee je de effectiviteit van reparatiepogingen aan het apparaat kunt controleren.


### ASIC spanningsmetingen analyseren


De ASIC spanningsmeetfunctie in AxeOS biedt cruciale diagnostische informatie die helpt de exacte aard van hardwareproblemen vast te stellen. Bij het onderzoeken van spanningsmetingen, moet u de relatie tussen gemeten spanning en gevraagde spanning begrijpen om een juiste diagnose te stellen. Het systeem toont zowel de spanning die wordt geleverd aan de ASIC chip als de spanning die de chip vraagt van het energiebeheersysteem.


Wanneer u een ASIC spanningsmeting van precies 1,2 volt ziet in combinatie met een stroomverbruik van minder dan 3 watt, duidt deze specifieke combinatie op een soldeerprobleem met de ASIC chip of een volledig defecte ASIC. Deze spanningsmeting suggereert dat de chip wel stroom krijgt, maar dat de chip zelf niet goed functioneert. Fysieke inspectie van de ASIC chip kan scheurtjes of andere zichtbare schade aantonen die dit gedragspatroon zouden kunnen verklaren.


Een ander diagnostisch scenario verschijnt wanneer je een laag stroomverbruik gekoppeld ziet aan zeer lage spanningswaarden, zoals 100 millivolt of 0,5 volt. Dit patroon geeft aan dat de ASIC chip niet voldoende spanning krijgt, wat typisch wijst op problemen met de U9 buck converter component. De buck converter is verantwoordelijk voor de precieze spanningsregeling die ASIC chips nodig hebben voor een goede werking.


### Loggegevens interpreteren en communicatie ASIC


Het AxeOS logsysteem biedt een waardevol inzicht in of uw ASIC chip communiceert met het besturingssysteem. Wanneer u de logs opent via de "show logs" functie, bevestigt de aanwezigheid van "ASIC resultaten" dat de chip niet alleen van stroom wordt voorzien, maar ook actief werk verwerkt en resultaten terugstuurt. Deze communicatie geeft aan dat de ASIC correct gesoldeerd is en de verbinding met het besturingscircuit in stand houdt.


De afwezigheid van ASIC resultaten in de logs, vooral in combinatie met andere symptomen, helpt om het probleem te beperken tot specifieke componenten of verbindingsproblemen. Met deze diagnostische aanpak kunt u onderscheid maken tussen chips die helemaal niet reageren en chips die intermitterende verbindingsproblemen kunnen hebben. De logboekanalyse is vooral waardevol bij het oplossen van complexe problemen waarbij meerdere symptomen verschillende hoofdoorzaken kunnen suggereren.


### Systematisch problemen oplossen


Bij het diagnosticeren van Bitaxe hardwareproblemen voorkomt een systematische aanpak dat kritieke problemen over het hoofd worden gezien en zorgt voor efficiënte reparatieprocessen. Begin met het documenteren van het stroomverbruik en de spanningsmetingen. Correleer deze metingen vervolgens met de loggegevens om een volledig beeld te krijgen van het gedrag van het systeem. Deze methodische aanpak helpt te identificeren of de problemen te maken hebben met de ASIC chip zelf, het voedingssysteem of de communicatiepaden tussen de componenten.


In gevallen waar de U9 buck converter het probleem lijkt te zijn, kan fysieke inspectie en eventueel opnieuw solderen nodig zijn. De U9-component is bijzonder gevoelig voor soldeerproblemen, vooral bij nieuwe assemblages. Als er problemen met de spanningsregeling worden vermoed, kun je met een multimeter controleren of er daadwerkelijk 1,2 volt aanwezig is op de ASIC pinnen. Als er wel spanning op de pinnen staat, maar de ASIC nog steeds niet functioneert, en er bij fysieke inspectie geen schade te zien is, is het vervangen van de ASIC chip de volgende logische stap. Als de problemen zelfs na het vervangen van de ASIC aanhouden, kan de U2 component, die de ASIC chip aanstuurt, aandacht nodig hebben als laatste element in de probleemoplossing.


## Hoe debuggen via USB?

<chapterId>f3182763-e1ef-5460-8bc0-f2ea53e3a410</chapterId>


:::video id=fe1b4b48-5f8a-4fd7-9417-ca03a36bce9f:::


Bij het oplossen van problemen met Bitaxe mining apparaten biedt directe toegang tot het interne logsysteem van het apparaat inzichten van onschatbare waarde die webgebaseerde interfaces niet kunnen bieden. In dit hoofdstuk wordt onderzocht hoe een directe seriële USB-verbinding met uw Bitaxe-apparaat tot stand gebracht kan worden met behulp van het ESP-IDF-framework, waardoor systeemlogs, opstartprocedures en foutmeldingen in real-time gecontroleerd kunnen worden. Deze debuggingbenadering is vooral cruciaal bij apparaten die vaak opnieuw worden opgestart of hardwarestoringen vertonen, omdat alle diagnostische informatie die verloren zou kunnen gaan tijdens het opnieuw opstarten van het systeem wordt vastgelegd.


Voor het debuggen is Visual Studio Code met de ESP-IDF-extensie nodig, hoewel elke compatibele IDE kan worden gebruikt. Deze methode werkt met alle Bitaxe-varianten met een USB-poort, inclusief de Bitaxe Ultra 204 en andere modellen uit de serie. De directe seriële verbinding omzeilt mogelijke beperkingen van de webinterface en biedt ongefilterde toegang tot de interne statusinformatie van het apparaat.


### Seriële communicatie instellen


De communicatie met uw Bitaxe-apparaat begint met het aansluiten van de USB-kabel en het openen van de ESP-IDF-terminal in uw ontwikkelomgeving. Het commando `idf.py monitor` start het verbindingsproces en scant automatisch de beschikbare COM-poorten om UART-communicatie tot stand te brengen met de ESP32-chip op uw Bitaxe-apparaat. Het systeem doorloopt de beschikbare poorten (COM3, COM4, COM16, enz.) totdat het de juiste verbinding vindt.


Zodra de terminal is aangesloten, toont deze de volledige opstartprocedure en lopende logbestanden. Het initiële verbindingsproces kan enkele ogenblikken duren omdat het systeem de juiste communicatiepoort moet identificeren. Als de automatische poortdetectie mislukt, kun je de COM-poort handmatig opgeven via de poortkeuze-interface van de IDE. Dit directe communicatiekanaal blijft actief tijdens de werking van het apparaat en biedt continue toegang tot systeemdiagnoses en prestatiegegevens.


### Bootsequentie en logboeken over normale werking interpreteren


De opstartprocedure geeft belangrijke informatie over de hardwareconfiguratie en het initialisatieproces van uw Bitaxe-apparaat. Normale opstartlogs beginnen met informatie over de ESP-IDF-versie, gevolgd door de kenmerkende "Welkom bij de Bitaxe. Hack the planet" dat bevestigt dat de firmware met succes is geladen. Daarna toont het systeem de ASIC frequentieconfiguratie, identificatie van het apparaatmodel en details over de kaartversie.


Een goed werkend apparaat toont een succesvolle I2C-initialisatie en ASIC spanningsregeling ingesteld op 1,2 volt. De logs tonen GPIO-statusinformatie en Wi-Fi initialisatiesequenties, gevolgd door DHCP-serverconfiguratie en IP-adrestoewijzing. Een van de meest cruciale indicatoren is het ASIC chipdetectiebericht, dat "één ASIC chip gedetecteerd" moet melden voor een apparaat met één chip. Deze bevestiging bevestigt dat de mining hardware goed is aangesloten en communiceert met de ESP32 controller.


De operationele logboeken laten meerdere gelijktijdige taken zien die op het apparaat draaien, waaronder stratum API communicatie, hoofdtaakcoördinatie, ASIC taakbeheer en stratum taakverwerking. Deze verschillende taakaanduidingen helpen problemen te isoleren naar specifieke systeemcomponenten. Normale werking omvat het opzetten van poolverbindingen, berichten voor moeilijkheidsaanpassingen, taak in de wachtrij zetten en uit de wachtrij halen, en rapportage over het genereren van nonce. Succesvolle mining operaties tonen ASIC resultaten met moeilijkheidsberekeningen en mining verzendbevestigingen wanneer aandelen de vereiste drempel halen.


### Hardwarefouten en foutpatronen identificeren


Hardwarestoringen verschijnen in de logboeken door specifieke foutpatronen die aangeven welke componenten defect zijn. De meest voorkomende foutmodus betreft I2C-communicatiefouten met specifieke geïntegreerde circuits op het Bitaxe-bord. Communicatiestoringen met de DS4432U worden bijvoorbeeld weergegeven als "ESP_ERROR_CHECK failed"-berichten met time-outindicatoren, die wijzen op problemen met de spanningsregeling of soldeerproblemen met de U10-component die verantwoordelijk is voor de displaycommunicatie.


Deze foutmeldingen bevatten gedetailleerde foutopsporingsinformatie zoals het specifieke bronbestand (main_ds4432u.c), de falende functieaanroep en de processorkern die de taak uitvoert. De backtrace-informatie biedt extra context voor geavanceerde probleemoplossing. Vergelijkbare foutpatronen kunnen optreden bij de EMC2101 temperatuur- en ventilatorregelchip, die elk kenmerkende loghandtekeningen genereren die helpen bij het identificeren van de falende component.


Fysieke hardwareproblemen treden vaak op als herhaalde foutcycli gevolgd door herstarten van het systeem. Als uw apparaat hoorbare ruis produceert tijdens het gebruik, duidt dit meestal op soldeerproblemen zoals bruggen tussen de pinnen van componenten of ondeugdelijke soldeerverbindingen. Hoewel deze mechanische problemen niet altijd generate specifieke logboekvermeldingen opleveren, zorgen ze voor onstabiele werkomstandigheden die zich manifesteren als frequente crashes en herstartcycli in de monitoruitvoer.


### Strategieën voor geavanceerde probleemoplossing


Seriële monitoring biedt verschillende voordelen ten opzichte van webgebaseerde debugging interfaces, met name voor intermitterende storingen of apparaten die vaak opnieuw worden opgestart. De continue logging zorgt ervoor dat er geen diagnostische informatie verloren gaat tijdens het herstarten van het systeem, in tegenstelling tot webinterfaces waarbij gegevens verloren kunnen gaan tijdens het verbreken van de verbinding. Deze uitgebreide logging maakt het mogelijk om patronen in storingen te identificeren en specifieke foutcondities te correleren met hardware of omgevingsfactoren.


Richt u bij het analyseren van problematische apparaten op de opeenvolging van gebeurtenissen die tot storingen leiden in plaats van op geïsoleerde foutmeldingen. Succesvolle ASIC communicatie zou regelmatige jobverwerking, nonce generatie en share indieningscycli moeten laten zien. Ontbrekende ASIC resultaten in de logs wijzen op communicatiestoringen tussen de ESP32 en de mining chip, vaak veroorzaakt door problemen met de voeding, beschadigde sporen of defecte componenten.


Voor systematische probleemoplossing documenteert u foutpatronen en component-specifieke storingen voordat u de hulp van de gemeenschap inroept. De gedetailleerde foutenlogboeken, inclusief specifieke chipaanduidingen en foutmodi, stellen ervaren gebruikers in staat om gerichte reparatiebegeleiding te bieden, zoals procedures voor het vervangen van componenten of soldeercorrecties. Deze methodische aanpak voor het debuggen van hardware verbetert het succespercentage van reparaties aanzienlijk en verkort de tijd voor het oplossen van problemen bij complexe problemen.


# Geavanceerd aanpassen

<partId>8d333102-ecb5-5f05-bfb5-03a27b2d0d70</partId>


## De printplaat aanpassen

<chapterId>ca08d2a4-2b34-575b-aecc-7482a03c190e</chapterId>


:::video id=30fb0010-f560-4e96-a05b-c21dc172746e:::

KiCad is een van de krachtigste open-source tools voor printplaatontwerp en routing. Met deze software van professionele kwaliteit kunnen ingenieurs en hobbyisten complexe elektronische ontwerpen maken door componenten op virtuele printplaten te plaatsen en de ingewikkelde sporen te frezen die deze componenten met elkaar verbinden. Wat KiCad bijzonder waardevol maakt voor onderwijs- en ontwikkelingsdoeleinden is het volledig open-source karakter, waardoor gebruikers bestaande ontwerpen kunnen wijzigen, aanpassen en ervan kunnen leren zonder licentiebeperkingen.


Het Bitaxe-project is een voorbeeld van de kracht van open-source hardwareontwikkeling en biedt een compleet PCB-ontwerp dat gebruikers kunnen onderzoeken, aanpassen en aanpassen aan hun specifieke behoeften. Deze toegankelijkheid creëert een uitstekende leeromgeving waar studenten en praktijkmensen echte PCB-ontwerpen kunnen verkennen terwijl ze hun begrip van elektronische systemen ontwikkelen. De mogelijkheid om visuele elementen zoals logo's aan te passen biedt een laagdrempelige instap voor gebruikers die geïntimideerd zijn door de technische complexiteit van elektronisch ontwerp.


### Je KiCad-omgeving instellen


Voordat je begint met aanpassingen, is het essentieel dat je ontwikkelomgeving goed is ingesteld. De Bitaxe repository moet gedownload worden naar je lokale machine, wat meestal gebeurt via GitHub's ZIP download functionaliteit. Deze repository bevat alle benodigde projectbestanden, inclusief de KiCad projectbestanden, componentbibliotheken en ontwerpdocumentatie die nodig zijn voor succesvolle aanpassing.


De installatie van KiCad moet worden voltooid met behulp van de officiële distributie van de KiCad-website, zodat compatibiliteit met de projectbestanden en toegang tot de nieuwste functies is gegarandeerd. Zodra zowel de repository als KiCad correct zijn geïnstalleerd, moet je voor het openen van het project navigeren naar het Bitaxe Ultra KiCad projectbestand in de gedownloade repositorystructuur. Dit projectbestand dient als centrale hub die alle gekoppelde ontwerpbestanden, componentbibliotheken en configuratie-instellingen koppelt.


De eerste aanblik van een complex PCB-ontwerp kan overweldigend lijken, met talloze componenten, sporen en lagen die een dicht visueel landschap creëren. De 3D-viewer van KiCad is echter van onschatbare waarde om de fysieke lay-out en ruimtelijke relaties binnen het ontwerp te begrijpen. Dit driedimensionale perspectief transformeert de abstracte schematische weergave in een realistische visualisatie van het uiteindelijke product, waardoor het eenvoudiger wordt om de plaatsing van componenten en de algehele esthetiek van het ontwerp te begrijpen.


### Aanpassingsproces logo


Het aanpassen van logo's op PCB-ontwerpen is een van de meest toegankelijke aanpassingen voor gebruikers die nieuw zijn met KiCad, omdat het minimale technische kennis vereist en toch direct visuele resultaten oplevert. Het proces begint met de image converter tool, die standaard afbeeldingsbestanden omzet in footprintformaten die compatibel zijn met PCB ontwerpsoftware. Dit conversieproces vereist zorgvuldige aandacht voor de grootteparameters, meestal gemeten in millimeters om de juiste schaalverdeling op de uiteindelijke printplaat te garanderen.


De workflow voor het converteren van afbeeldingen omvat verschillende kritieke stappen die het uiteindelijke uiterlijk en de plaatsing van aangepaste logo's bepalen. De selectie van bronafbeeldingen moet voorrang geven aan contrastrijke ontwerpen die zich goed laten vertalen naar het zeefdrukproces dat wordt gebruikt bij de PCB-productie. De specificatie van de grootte wordt cruciaal, aangezien logo's groot genoeg moeten zijn om leesbaar te blijven na de productie terwijl ze niet interfereren met de plaatsing of functionaliteit van componenten. De keuze tussen voorste en achterste zeefdruklagen beïnvloedt zowel de zichtbaarheid als de productieoverwegingen.


Het beheer van footprintbibliotheken is een fundamenteel aspect van KiCad-aanpassingen, waarbij gebruikers moeten begrijpen hoe de software ontwerpelementen organiseert en toegankelijk maakt. Voor het toevoegen van aangepaste logo's moeten nieuwe footprintbibliotheken worden gemaakt of bestaande worden aangepast, waarna deze bibliotheken op de juiste manier worden gekoppeld binnen de projectstructuur. Dit proces zorgt ervoor dat aangepaste elementen toegankelijk blijven tijdens verschillende ontwerpsessies en gemakkelijk kunnen worden gedeeld met andere teamleden of medewerkers.


### Verkenning en begrip van geavanceerd ontwerp


Naast het eenvoudig aanpassen van logo's biedt KiCad krachtige hulpmiddelen voor het verkennen en begrijpen van complexe PCB-ontwerpen. Met het lagenbeheersysteem kunnen gebruikers selectief verschillende aspecten van het ontwerp bekijken, van componentplaatsing en routing tot productiespecificaties en assemblage-informatie. Deze gelaagde aanpak maakt een gedetailleerde analyse van specifieke ontwerpelementen mogelijk zonder visuele rommel van ongerelateerde componenten.


Sporenanalyse is een van de meest leerzame aspecten van PCB-onderzoek, omdat het laat zien hoe elektrische verbindingen tussen componenten en subsystemen lopen. Door individuele sporen of groepen gerelateerde signalen te volgen, kunnen gebruikers inzicht krijgen in de functionaliteit van circuits en ontwerpbeslissingen. Het onderzoeken van stroomverdelingsnetwerken laat bijvoorbeeld zien hoe spanningsregeling en filtercomponenten samenwerken om gevoelige elektronische componenten van schone en stabiele stroom te voorzien.


De relatie tussen schematisch ontwerp en fysieke layout wordt duidelijk door zorgvuldig onderzoek naar de plaatsing van componenten en routeringsbeslissingen. Begrijpen waarom specifieke componenten op bepaalde locaties worden geplaatst, hoe thermische overwegingen de beslissingen over de lay-out beïnvloeden en hoe de vereisten voor signaalintegriteit de routingkeuzes bepalen, biedt waardevolle inzichten in professionele PCB-ontwerppraktijken. Deze kennis is van onschatbare waarde voor gebruikers die hun eigen ontwerpen ontwikkelen of bestaande ontwerpen aanpassen voor specifieke toepassingen.


De uitgebreide controle- en verificatietools voor ontwerpregels van KiCad zorgen ervoor dat wijzigingen elektrische en fabricagecompatibiliteit behouden. Deze geautomatiseerde systemen helpen veelvoorkomende ontwerpfouten te voorkomen en leren gebruikers tegelijkertijd over industriestandaarden en best practices. De integratie van 3D-visualisatie met elektrische ontwerpgegevens creëert een krachtige leeromgeving waarin theoretische concepten tastbaar worden door visuele weergave en interactieve verkenning.


## Hoe maak je een fabrieksbestand?

<chapterId>e9da631c-e6d1-50c1-bb59-bc8455c29d3e</chapterId>


:::video id=07f980bf-6052-4ed4-bf7b-75e8aba585df:::

Het bouwen van aangepaste firmware voor ESP-gebaseerde mining apparaten vereist zorgvuldige aandacht voor configuratie, afhankelijkheden en het juiste bouwproces. Deze uitgebreide handleiding doorloopt het volledige proces van het maken van zowel standaard firmware als fabrieksbestanden met voorgeconfigureerde instellingen, waardoor de implementatie efficiënter wordt en de insteltijd voor eindgebruikers wordt verkort.


Merk op dat dit hoofdstuk vrij technisch is en dat je er gewoon doorheen kunt bladeren als je er nieuwsgierig naar bent.


### De ontwikkelomgeving instellen


Om te beginnen met de ontwikkeling van ESP-Miner firmware moet je de juiste ontwikkelomgeving opzetten in Visual Studio Code, idealiter op een Linux-distributie. De ESP-IDF-extensie dient als hoeksteen van deze setup en biedt de nodige tools en frameworkintegratie voor ESP32-ontwikkeling. Bij de eerste installatie van de ESP-IDF-uitbreiding krijgen gebruikers een installatiegids te zien die het configuratieproces vergemakkelijkt.


Een kritische overweging in het installatieproces is het kiezen van de juiste ESP-IDF versie. Voorheen werd versie 5.1.3 aanbevolen, maar in de praktijk is gebleken dat deze versie bouwproblemen kan veroorzaken die het ontwikkelingsproces bemoeilijken. De aanbevolen aanpak is nu het gebruik van ESP-IDF versie 5.3 Beta 1. Deze versie heeft bewezen deze bouwproblemen op te lossen en zorgt ervoor dat Bitaxe apparaten goed functioneren. Het installatieproces vereist het selecteren van de Express installatieoptie en het specifiek kiezen van versie 5.3 Beta 1 uit de beschikbare opties.


Het opzetten van de ontwikkelomgeving gaat verder dan de installatie van ESP-IDF en omvat ook een juiste terminalconfiguratie. Visual Studio Code biedt meerdere methoden voor toegang tot ESP-IDF-functionaliteit, waaronder de opdrachtpaletoptie om een ESP-IDF-terminal te openen of het gebruik van het speciale terminalpictogram in de interface. Deze gespecialiseerde terminalomgeving zorgt ervoor dat alle ESP-IDF commando's correct werken en biedt toegang tot de complete toolchain.


### De ESP-Miner-instellingen configureren


Het configuratiebestand vormt het hart van het ESP-Miner aanpassingsproces en bevat alle essentiële parameters die bepalen hoe het apparaat in de doelomgeving zal werken. Deze configuratie omvat netwerkinstellingen, mining poolverbindingen en hardwarespecifieke parameters die moeten worden aangepast aan het specifieke implementatiescenario.


Netwerkconfiguratie vormt het belangrijkste onderdeel van het installatieproces, waarbij Wi-Fi referenties inclusief SSID en wachtwoord moeten worden gespecificeerd. In plaats van het gebruik van tijdelijke waarden zoals "test", moeten productieconfiguraties de werkelijke netwerkgegevens bevatten die het apparaat in de operationele omgeving zal gebruiken. De configuratie is ook geschikt voor verschillende mining pool setups en ondersteunt zowel private pool configuraties met specifieke IP-adressen als publieke pools zoals public-pool.io met de bijbehorende poortinstellingen.


Mining-specifieke configuratieparameters omvatten de stratum gebruikersinstelling, die typisch overeenkomt met het Bitcoin adres waar mining beloningen naartoe gestuurd moeten worden. Aanvullende hardwareparameters zoals frequentie-instellingen, spanningsconfiguraties en ASIC type specificaties moeten overeenkomen met het doelhardwareplatform. De GitHub repository biedt voorgeconfigureerde voorbeelden voor verschillende hardware varianten, zoals de BM1368 configuratie ontworpen voor Super apparaten en BM1366 instellingen voor Ultra varianten. Boardversie specificaties, zoals het instellen van de poortversie op 401 voor nieuwere hardware revisies, zorgen voor compatibiliteit met de specifieke eigenschappen van het doelapparaat.


### Bouwen van de Web Interface en kernfirmware


Het ESP-Miner project bevat een geavanceerde webinterface die apart gecompileerd moet worden voordat het hoofdfirmware bouwproces kan beginnen. Deze webinterface, waarnaar wordt verwezen als de AxeOS firmware, biedt gebruikers een uitgebreide beheerinterface voor het bewaken en bedienen van hun mining apparaten.


Het bouwen van de webinterface begint door te navigeren naar de HTTP-server directory binnen de hoofdrepository structuur, specifiek de AxeOS subdirectory. Deze locatie bevat de op Node.js gebaseerde webapplicatie die een installatie van afhankelijkheden vereist via het commando npm install. Het bouwsysteem gaat ervan uit dat Node.js correct is geïnstalleerd op het ontwikkelsysteem, aangezien dit een fundamentele vereiste is voor het compilatieproces van de webinterface.


Na de installatie van de afhankelijkheden compileert de opdracht npm run build de onderdelen van de webinterface en maakt de benodigde bestanden aan die in de ESP32-firmware worden opgenomen. Dit compilatieproces genereert geoptimaliseerde webelementen die de functionaliteit van de gebruikersinterface bieden met behoud van efficiënt geheugengebruik op het beperkte ESP32-platform. De succesvolle voltooiing van deze compilatiestap is essentieel voordat u verder gaat met de hoofdcompilatie van de firmware, aangezien de ESP-Miner-firmware deze webinterfacecomponenten als integrale functionaliteit bevat.


### Fabrieksbestanden maken met geïntegreerde configuratie


Het maken van fabrieksbestanden is een geavanceerde implementatiestrategie die configuratie-instellingen direct in de binaire firmware insluit, waardoor handmatige configuratie tijdens het instellen van het apparaat niet meer nodig is. Deze aanpak is vooral waardevol voor grootschalige implementaties of situaties waarin consistente configuratie op meerdere apparaten essentieel is.


Het aanmaken van het fabrieksbestand begint met het genereren van een binaire configuratie uit het CSV-configuratiebestand met behulp van de NVS-partitiegenerator van ESP-IDF. Deze tool, die zich in de ESP-IDF components directory onder nvs-flash/nvs-partition-generator bevindt, converteert de door mensen leesbare configuratie naar een binair formaat dat geschikt is voor directe flashgeheugenopslag. Het nvs-partition-gen.py script verwerkt het config.csv bestand en genereert een config.binary bestand dat zich richt op de 0x6000 geheugenadresruimte.


De uiteindelijke assemblage van fabrieksbestanden maakt gebruik van gespecialiseerde samenvoeg scripts die de kern firmware binaries combineren met de configuratie gegevens. Het archief biedt meerdere samenvoeg opties, waaronder een standaard samenvoeg script voor basis fabrieksbestanden en een configuratie-inclusief samenvoeg script voor uitgebreide fabrieksbestanden. Het merge-bin-with-config.sh script creëert fabrieksbestanden die zowel de firmwarefunctionaliteit als de vooraf geconfigureerde instellingen bevatten, wat resulteert in een compleet implementatiepakket. Deze aanpak maakt het mogelijk om apparaat-specifieke fabrieksbestanden te maken, zoals versies op maat voor Bitaxe Ultra apparaten met specifieke board revisies, terwijl de flexibiliteit behouden blijft om generate generieke fabrieksbestanden te maken zonder ingesloten configuraties voor scenario's die handmatige instelflexibiliteit vereisen.


De voltooide fabrieksbestanden voorzien implementatieteams van kant-en-klare binaries die alle benodigde firmwarecomponenten en configuratie-instellingen bevatten, waardoor het provisioneringsproces van het apparaat wordt gestroomlijnd en consistente operationele parameters voor alle ingezette mining apparaten worden gegarandeerd.


## Hoe gebruik je de Bitaxe Web Flasher?

<chapterId>8c3e2d4c-c038-53ec-93cb-cc30a29e4394</chapterId>


:::video id=291757b9-f459-48f6-8766-56387f907859:::

De Bitaxe Web Installer staat voor een gestroomlijnde aanpak van firmwarebeheer voor Bitaxe apparaten en biedt gebruikers meerdere installatieopties via een webgebaseerde interface. Dit uitgebreide hulpprogramma maakt een einde aan de complexiteit die traditioneel gepaard gaat met firmware-updates en nieuwe installaties en maakt apparaatbeheer toegankelijk voor gebruikers, ongeacht hun technische expertise. Inzicht in het juiste gebruik van dit installatieprogramma is cruciaal voor het behouden van optimale apparaatprestaties en het vermijden van veelvoorkomende valkuilen die apparaten tijdelijk buiten werking kunnen stellen.


### Vereisten voor toegang en browsercompatibiliteit


De Bitaxe Web Installer is toegankelijk via de speciale URL [https://bitaxeorg.github.io/bitaxe-web-flasher/](https://bitaxeorg.github.io/bitaxe-web-flasher/) (de URL in de video is nu niet meer beschikbaar) en dient als centraal punt voor alle installatieactiviteiten van firmware. Voor een succesvolle werking van dit webgebaseerde hulpprogramma is echter browsercompatibiliteit vereist, omdat het installatieprogramma afhankelijk is van specifieke webtechnologieën die niet door alle browsers worden ondersteund. Chrome is de aanbevolen browser voor het installatieprogramma en biedt volledige compatibiliteit met alle functies. Hoewel andere Chromium-gebaseerde browsers vergelijkbare functionaliteit kunnen bieden, ontbreekt het populaire alternatieven zoals Brave en Firefox aan de noodzakelijke API ondersteuning, waardoor ze niet compatibel zijn met de kernactiviteiten van het installatieprogramma.


Deze beperking van de browser komt voort uit de afhankelijkheid van het installatieprogramma van directe seriële communicatie met Bitaxe-apparaten via de webinterface. Het seriële web API, dat deze communicatie mogelijk maakt, is een relatief nieuwe webstandaard die nog niet door alle browsers wordt ondersteund. Gebruikers die het installatieprogramma proberen te openen via browsers die niet worden ondersteund, krijgen te maken met verbindingsfouten en kunnen niet communiceren met hun apparaten.


### Stroomvereisten en voorbereiding van het apparaat


Bitaxe-apparaten hebben verschillende stroomvereisten, afhankelijk van het specifieke model en de versie, waardoor een goed energiebeheer essentieel is voor een succesvolle installatie van de firmware. Apparaten die werken met versie 204 of lager kunnen alleen werken via USB-voeding en trekken voldoende stroom van de aangesloten computer om te blijven werken tijdens het flashproces. Deze vereenvoudigde stroomregeling maakt deze eerdere versies bijzonder geschikt voor firmware-updates, omdat gebruikers slechts een enkele USB-kabel hoeven aan te sluiten om het installatieproces te starten.


Apparaten met versie 205 en hoger hebben echter externe voedingsbronnen nodig naast de USB-aansluiting, als gevolg van veranderingen in het stroomverbruik en het circuitontwerp in nieuwere hardwareversies. Deze apparaten kunnen niet voldoende stroom krijgen via USB alleen, waardoor ze tijdens de installatie van de firmware op hun standaard stroomvoorziening moeten worden aangesloten. Als deze nieuwere apparaten niet voldoende stroom krijgen, mislukt de installatie en kan het firmware-updateproces verstoord raken.


Het fysieke verbindingsproces vereist een specifieke timing en knopmanipulatie om een goede communicatie tussen het installatieprogramma en het apparaat te garanderen. Gebruikers moeten de opstartknop op hun Bitaxe-apparaat ingedrukt houden voordat ze de USB-C-kabel aansluiten op hun computer. Hierdoor komt het apparaat in bootloader-modus en kan het installatieprogramma direct communiceren met de firmware-opslag van het apparaat. Als u de USB-kabel aansluit voordat u de opstartknop hebt ingedrukt, werkt het apparaat normaal in plaats van in de bootloadermodus die nodig is voor de installatie van de firmware, waardoor het installatieprogramma niet het benodigde communicatiekanaal tot stand kan brengen.


### Installatieopties en hun toepassingen


Het Bitaxe Web Installer biedt vier verschillende installatieopties, elk ontworpen voor specifieke gebruikssituaties en apparaatconfiguraties. Het Bitaxe Superboard versie 4.0.1 vertegenwoordigt de meest recente firmware voor Super model apparaten, met versie 4.0.2 gepland voor toekomstige release. Deze optie omvat zowel fabrieks- als updatevarianten en biedt flexibiliteit in de installatieaanpak op basis van gebruikersbehoeften en apparaatstatus.


Fabrieksinstallaties vertegenwoordigen volledige firmwarevervangingen die het originele fabricageproces weerspiegelen, inclusief uitgebreide zelftestprocedures die de functionaliteit van het apparaat op alle systemen verifiëren. Wanneer gebruikers kiezen voor een fabrieksinstallatie, verwijdert de installateur de bestaande firmware en configuratiegegevens volledig en vervangt deze door een nieuwe, schone installatie die identiek is aan de installatie die tijdens de fabricage is toegepast. Dit proces omvat geautomatiseerde zelftests die de goede werking van de hardware valideren, waarbij gebruikers hun apparaten na voltooiing opnieuw moeten opstarten voordat de normale werking kan worden hervat. Fabrieksinstallaties zijn vooral waardevol wanneer apparaten hardnekkige problemen ondervinden of wanneer gebruikers hun apparaten willen terugzetten naar de oorspronkelijke fabrieksspecificaties.


Update-installaties bieden een conservatievere aanpak, waarbij bestaande configuratiegegevens behouden blijven en alleen de kerncomponenten van de firmware worden bijgewerkt. Deze optie is ideaal voor gebruikers die hun apparaatinstellingen hebben aangepast en hun persoonlijke configuraties willen behouden terwijl ze profiteren van verbeteringen in de firmware en bugfixes. Het updateproces richt zich alleen op de firmwarecomponenten die gewijzigd moeten worden en laat gebruikersspecifieke instellingen, WiFi-gegevens en Bitcoin adressen intact tijdens het installatieproces.


### Kritische installatieoverwegingen en gegevensbescherming


Het onderscheid tussen fabrieksinstallaties en update-installaties heeft belangrijke gevolgen voor de configuratie van het apparaat en het behoud van gebruikersgegevens. Fabrieksinstallaties wissen het apparaat volledig, waarbij alle door de gebruiker geconfigureerde instellingen worden verwijderd, inclusief WiFi-gegevens, Bitcoin-adressen en alle gepersonaliseerde apparaatparameters. Na een fabrieksinstallatie moeten gebruikers opnieuw verbinding maken met het standaard WiFi-netwerk van het apparaat en alle persoonlijke instellingen opnieuw configureren.


Bij het installeren van updates moet goed worden opgelet bij de optie Apparaat wissen tijdens het installatieproces. Het installatieprogramma vraagt gebruikers "Wilt u het apparaat wissen voordat u Bitaxe Flasher installeert?" en waarschuwt dat alle gegevens op het apparaat verloren zullen gaan. Gebruikers die update-installaties uitvoeren moeten deze optie weigeren door op "Volgende" te klikken in plaats van de wisbewerking te bevestigen. Als de wisoptie tijdens een update-installatie wordt geaccepteerd, wordt het configuratiebestand van het apparaat verwijderd, waardoor het apparaat mogelijk niet meer functioneert totdat de juiste configuratie is hersteld. Hoewel deze situatie het apparaat niet permanent beschadigt, zorgt het voor onnodige complicaties en zijn er extra configuratiestappen nodig om de normale werking te herstellen.


Het installatieproces zelf verloopt automatisch zodra gebruikers hun keuzes hebben gemaakt en bevestigd. Het installatieprogramma handelt alle technische aspecten van de firmwareoverdracht en -verificatie af en geeft tijdens het hele proces voortgangsindicatoren en statusupdates. Dankzij deze geautomatiseerde aanpak hoeven gebruikers geen complexe firmware-installatieprocedures te begrijpen en zijn de resultaten betrouwbaar en consistent voor verschillende apparaatmodellen en firmwareversies.


## Hoe maak en bestel ik de PCB?

<chapterId>566f5e06-9ec9-55c0-84f6-101d6ca4c2ff</chapterId>


:::video id=9a56ad84-d9cf-4f85-ab98-301fb3101228:::

Dit hoofdstuk richt zich op het praktische proces van het genereren van productiebestanden van KiCad projecten en het bestellen van professionele printplaten bij online fabrikanten. Met het Bitaxe project als voorbeeld doorlopen we de complete workflow van het genereren van bestanden tot het plaatsen van een bestelling bij een printplaatfabrikant.


### Het PCB productieproces begrijpen


De reis van een voltooid KiCad-ontwerp naar een fysieke printplaat omvat een aantal kritieke stappen die de kloof tussen digitaal ontwerp en fysieke productie overbruggen. Wanneer u werkt met complexe projecten zoals de Bitaxe, biedt de PCB-editor in KiCad een uitgebreide weergave van uw ontwerp, waarbij alle componenten en hun onderlinge verbindingen worden weergegeven door middel van gekleurde sporen. De rode en blauwe lijnen die u ziet, vertegenwoordigen de elektrische verbindingen tussen de verschillende geïntegreerde circuits en componenten op de printplaat. Met de 3D-viewerfunctie van KiCad kunt u visualiseren hoe de uiteindelijk geassembleerde printplaat eruit zal zien, wat een waardevol inzicht geeft in de plaatsing van componenten en mogelijke mechanische conflicten.


Het productieproces vereist specifieke bestandsformaten die PCB-fabrikanten kunnen interpreteren en gebruiken om uw printplaten te fabriceren. Deze bestanden bevatten precieze informatie over koperlagen, boorgaten, plaatsing van componenten en andere productiespecificaties. Inzicht in deze workflow is essentieel, of u nu werkt met het standaard Bitaxe-ontwerp of wijzigingen aanbrengt zoals het toevoegen van aangepaste logo's, het wijzigen van componentwaarden of het aanpassen van de printplaatlay-out om te voldoen aan specifieke vereisten.


### Gerber-bestanden genereren voor productie


Gerber-bestanden zijn de industriestandaard voor het communiceren van PCB-ontwerpinformatie naar fabrikanten. Deze bestanden bevatten alle noodzakelijke gegevens voor de fabricage van uw PCB, inclusief koperlaagpatronen, soldeermaskerdefinities en boorgatlocaties. Om generate deze bestanden in KiCad te maken, navigeert u naar de PCB-editor en opent u de fabricage-uitgangen via het menu Bestanden. De software configureert automatisch de juiste instellingen voor standaard fabricageprocessen, inclusief de juiste structuur van de uitvoermap, meestal georganiseerd als "fabricagebestanden/gerbers"


Het generatieproces creëert meerdere Gerber-bestanden die elk verschillende aspecten van uw PCB-ontwerp vertegenwoordigen. Deze bestanden werken samen om fabrikanten te voorzien van volledige fabricage-instructies. Eenmaal gegenereerd moeten deze bestanden worden gecomprimeerd in een ZIP-archief, omdat dit het standaardformaat is dat door de meeste printplaatfabrikanten wordt verwacht. Het ZIP-bestand bevat alle noodzakelijke productiegegevens en zorgt ervoor dat er geen bestanden verloren gaan of beschadigd raken tijdens het uploadproces naar de website van de fabrikant.


Het is vermeldenswaard dat veel open-source projecten, waaronder de Bitaxe, vaak vooraf gegenereerde productiebestanden in hun repositories hebben. Het is echter cruciaal om te weten hoe je deze bestanden zelf generate kunt maken als je ontwerpaanpassingen maakt of met verschillende versies van de printplaat werkt. Deze kennis is vooral waardevol bij het aanpassen van ontwerpen of het oplossen van fabricageproblemen.


### PCB-fabrikanten selecteren en opties begrijpen


Het landschap van PCB-productie biedt verschillende gerenommeerde opties, waarbij JLCPCB en PCBWay tot de populairste keuzes behoren voor zowel hobbyisten als professionals. Beide fabrikanten bieden vergelijkbare diensten met concurrerende prijzen en betrouwbare kwaliteit, hoewel elk van hen specifieke voordelen heeft, afhankelijk van uw projectvereisten. JLCPCB trekt vaak beginnende gebruikers aan met promotieprijzen en gebruiksvriendelijke interfaces, terwijl PCBWay verschillende materiaalopties of gespecialiseerde diensten kan aanbieden.


Wanneer u uw Gerber-bestanden uploadt naar de website van een fabrikant, analyseert het systeem automatisch uw ontwerp en presenteert het verschillende productieopties. De standaardinstellingen van deze platforms zijn meestal geschikt voor de meeste standaardontwerpen en het wordt over het algemeen aanbevolen om deze instellingen te behouden tenzij u specifieke eisen hebt. De belangrijkste parameters zijn de dikte van de printplaat, het kopergewicht, de oppervlakteafwerking en de minimumhoeveelheden. De meeste fabrikanten vereisen minimumbestellingen van vijf printplaten, wat eigenlijk goed werkt voor hobbyistenprojecten waarbij het voordelig is om reserveprintplaten te hebben of om ze met vrienden te delen.


Kleuropties zijn een van de weinige esthetische keuzes die beschikbaar zijn tijdens het productieproces. Hoewel groen de traditionele en meest kosteneffectieve optie blijft, bieden fabrikanten meestal alternatieven zoals blauw, rood, geel, paars en zwart. De kleurkeuze is puur esthetisch en heeft geen invloed op de elektrische prestaties van uw PCB, hoewel sommige kleuren kleine gevolgen kunnen hebben voor de kosten of een langere productietijd.


### Opties voor geavanceerde productie en assemblage


Naast de basis PCB fabricage bieden moderne fabrikanten extra diensten aan die de voltooiing van uw project aanzienlijk kunnen stroomlijnen. Stencils zijn een van de meest waardevolle extra diensten, vooral voor ontwerpen met fijne pitch componenten zoals de ASIC chips in Bitcoin mining projecten. Een stencil is in wezen een met precisie gesneden aluminium sjabloon met openingen die exact overeenkomen met de soldeerpadlocaties op uw PCB. Deze tool maakt een consistente en nauwkeurige toepassing van soldeerpasta mogelijk, wat de assemblagekwaliteit aanzienlijk verbetert en de kans op soldeerfouten vermindert.


De sjabloonopties bestaan meestal uit enkele sjablonen met zowel boven- als onderpatronen, of aparte sjablonen voor elke kant van het bord. Voor de meeste projecten is een gecombineerde sjabloon handiger en kosteneffectiever. De dikte van het stencil wordt zorgvuldig berekend om de juiste hoeveelheid soldeerpasta te deponeren voor uw specifieke componenttypes en padafmetingen. Het gebruik van een stencil verandert wat een vervelend en foutgevoelig handmatig proces zou kunnen zijn in een snelle en professionele assemblagestap.


Hoewel sommige fabrikanten gedeeltelijke of volledige assemblage aanbieden, moeten deze opties zorgvuldig worden overwogen voor complexe projecten zoals de Bitaxe. De beschikbaarheid van componenten, de kosten en de educatieve waarde van zelfassemblage spelen allemaal een rol bij deze beslissing. Veel gespecialiseerde componenten die nodig zijn voor Bitcoin mining-projecten zijn niet direct beschikbaar via standaard PCB-assemblagediensten, waardoor het vinden van componenten en handmatige assemblage de meest praktische aanpak is. Toekomstige afleveringen in deze serie zullen gaan over strategieën voor het vinden van componenten en assemblagetechnieken om u te helpen uw Bitaxe-project succesvol af te ronden, van kale PCB tot functioneel apparaat.


Het productie- en assemblageproces vormt een cruciale brug tussen digitaal ontwerp en fysieke implementatie. Als je deze workflows begrijpt, kun je de controle over je projecten nemen, kosten besparen en waardevolle praktijkervaring opdoen met professionele productieprocessen. Of je nu een enkel prototype bouwt of een kleine productierun plant, het beheersen van deze vaardigheden opent nieuwe mogelijkheden om je elektronische ontwerpen tot leven te brengen.


# Prestatieoptimalisatie

<partId>87b8790f-b7a9-5286-a7f8-328176ef7cb5</partId>


## Uw Bitaxe benchmarken

<chapterId>7259a4b1-93c1-5956-87d3-baaee58115af</chapterId>


:::video id=2491a783-9750-4ea5-a40c-1d1d611784d5:::

Het streven naar optimale mining prestaties vereist een systematische benadering van de hardwareconfiguratie die hashrate, efficiëntie en thermisch beheer in balans brengt. De Bitaxe biedt talloze configuratieparameters die de prestaties aanzienlijk kunnen beïnvloeden, maar het handmatig testen van elke combinatie van instellingen zou onpraktisch en tijdrovend zijn. In dit hoofdstuk wordt onderzocht hoe u geautomatiseerde benchmarktools kunt gebruiken om de prestaties van uw Bitaxe wetenschappelijk te optimaliseren met behoud van veilige werkomstandigheden.


### Bitaxe prestatiecijfers en basislijnconfiguratie begrijpen


Voordat we ons gaan verdiepen in optimalisatietechnieken, is het essentieel om de belangrijkste prestatie-indicatoren te begrijpen die de operationele efficiëntie van uw Bitaxe bepalen. De belangrijkste indicatoren zijn hashrate gemeten in terahash per seconde, energie-efficiëntie uitgedrukt in joules per terahash, ASIC frequentie in megahertz en kernspanning in volt. Een goed geconfigureerde Bitaxe zou ongeveer 1,1 terahash kunnen bereiken met een efficiëntie van ongeveer 17 joules per terahash, werkend op 550 megahertz met een gemeten ASIC voltage van 1,14 volt. Deze basiscijfers bieden een referentiepunt voor het begrijpen van de potentiële verbeteringen die beschikbaar zijn door systematische optimalisatie.


De relatie tussen deze meetgegevens is complex en onderling afhankelijk. Hogere frequenties verhogen doorgaans hashrate, maar verhogen ook het stroomverbruik en de warmteontwikkeling. Op dezelfde manier beïnvloeden spanningsaanpassingen zowel de prestaties als de thermische kenmerken. De uitdaging ligt in het vinden van de optimale balans die hashrate of efficiëntie maximaliseert met behoud van een stabiele werking binnen veilige temperatuurgrenzen. Dit optimalisatieproces vereist methodisch testen van meerdere parametercombinaties, waardoor geautomatiseerde hulpmiddelen van onschatbare waarde zijn voor het bereiken van optimale resultaten.


### De architectuur van het Bitaxe Hashrate-benchmarkhulpmiddel


De [Bitaxe Hashrate Benchmark](https://github.com/mrv777/Bitaxe-Hashrate-Benchmark/) tool vertegenwoordigt een geavanceerde op Python gebaseerde oplossing die oorspronkelijk is ontwikkeld door WhiteCookie en vervolgens is verbeterd door mrv777. Deze open-source tool, gedistribueerd onder de GPLv3 licentie, automatiseert het complexe proces van het testen van meerdere configuratiecombinaties om de optimale instellingen voor je specifieke hardware te identificeren. De belangrijkste kracht van de tool ligt in de systematische benadering van het testen van parameters, waarbij de instellingen voor frequentie en spanning stapsgewijs worden aangepast terwijl de prestatiegegevens en thermische omstandigheden continu worden gecontroleerd.


Het benchmarkingproces neemt gewoonlijk 30 tot 40 minuten in beslag, waarin de tool methodisch verschillende combinaties van ASIC frequentie- en voltage-instellingen test. De tool begint met conservatieve basisinstellingen, meestal beginnend bij 1,15 volt en 500 megahertz, en verhoogt dan stapsgewijs deze parameters terwijl hashrate, temperatuur en stabiliteit worden gecontroleerd. Belangrijk is dat de tool prioriteit geeft aan veilige werking boven maximale prestaties en automatisch terugschakelt naar instellingen die overmatige warmteontwikkeling of instabiliteit veroorzaken. Deze conservatieve aanpak zorgt ervoor dat het optimalisatieproces de levensduur of betrouwbaarheid van de hardware niet in gevaar brengt.


### Installatie- en installatievereisten


Het implementeren van de Bitaxe Hashrate Benchmark tool vereist verschillende vereiste softwarecomponenten op uw lokale computer. De belangrijkste vereisten zijn Python voor het uitvoeren van de benchmarkscripts, Git voor repositorybeheer en optioneel Visual Studio Code voor een verbeterde ontwikkelomgeving. Hoewel de tool via commandoregelinterfaces kan worden bediend, biedt het gebruik van een geïntegreerde ontwikkelomgeving zoals VS Code een beter inzicht in het benchmarkproces en de resultatenanalyse.


Het installatieproces volgt de standaard Python ontwikkelingspraktijken, te beginnen met het klonen van de repository van GitHub naar je lokale machine. Zodra de repository is gedownload, moet je een virtuele omgeving maken om de afhankelijkheden van de tool te isoleren van de Python-installatie van je systeem. Deze isolatie voorkomt mogelijke conflicten met andere Python-toepassingen en zorgt voor een consistente werking. Nadat u de virtuele omgeving hebt geactiveerd, installeert u de vereiste afhankelijkheden met behulp van het meegeleverde bestand met vereisten, dat automatisch alle benodigde bibliotheken en modules configureert voor een goede werking van het hulpprogramma.


### Benchmarks uitvoeren en resultaten interpreteren


Om de benchmark uit te voeren, hoeft u slechts één Python-commando uit te voeren met het IP-adres van uw Bitaxe als parameter. De tool maakt automatisch verbinding met de webinterface van uw miner en begint het systematische testproces. Tijdens de uitvoering geeft de tool gedetailleerde logboekinformatie over de huidige test iteratie, toegepaste spanning en frequentie-instellingen, resulterende hashrate, ingangsspanning, temperatuurmetingen en thermische gegevens van kritieke componenten zoals de buck converter. Met deze real-time feedback kun je de voortgang van de benchmarking controleren en begrijpen hoe verschillende instellingen de prestaties van je miner beïnvloeden.


Het intelligente thermische beheer van de tool wordt duidelijk wanneer de temperaturen de veiligheidsdrempel van 66 graden Celsius naderen. In plaats van de veilige bedrijfslimieten te overschrijden, verlaagt de benchmark automatisch de instellingen om de thermische stabiliteit te behouden. Deze conservatieve aanpak zorgt ervoor dat het optimalisatieproces prioriteit geeft aan de betrouwbaarheid van de hardware op de lange termijn boven prestatiewinst op de korte termijn. Na voltooiing genereert de tool uitgebreide resultaten in JSON-formaat, die de top vijf configuraties rangschikken voor zowel maximale hashrate als optimale efficiëntie. Deze resultaten bieden duidelijke richtlijnen voor het selecteren van de configuratie die het beste past bij uw operationele prioriteiten, of deze nu gericht zijn op maximale output of energie-efficiëntie.


De benchmarktool biedt ook aanpassingsopties voor geavanceerde gebruikers die de testparameters willen wijzigen. Met commandoregelargumenten kunt u aangepaste startspanningen en frequenties opgeven, zodat u gerichter kunt optimaliseren voor specifieke gebruikssituaties. Als u bijvoorbeeld al weet dat uw hardware goed presteert bij hogere frequenties, kunt u de benchmark starten bij hogere instellingen in plaats van te beginnen bij de conservatieve standaardinstellingen. Deze flexibiliteit maakt de tool waardevol voor zowel beginnende gebruikers die op zoek zijn naar geautomatiseerde optimalisatie als ervaren miners die specifieke prestatiekenmerken nauwkeurig willen afstellen.


## Overklokken van uw Bitaxe

<chapterId>6b48c0c6-51c3-51a3-b317-850a374ae61e</chapterId>


:::video id=46c7a442-cd72-477c-8c91-b2c489ada1e6:::

Overklokken van een Bitaxe-apparaat vereist zorgvuldige overweging van zowel hardwarebeperkingen als koelvereisten. Hoewel veel gebruikers hun apparaten liever onderklokken voor een stillere werking, is inzicht in de juiste overkloktechnieken essentieel voor diegenen die maximale prestaties willen zonder hun hardware te beschadigen. Het proces omvat het verhogen van de frequentie en mogelijk het aanpassen van de voltage-instellingen buiten de fabrieksspecificaties, waardoor de warmteontwikkeling en de belasting van de componenten toenemen.


De basis voor succesvol overklokken ligt in een goede koelinfrastructuur. Voordat u frequentieaanpassingen uitvoert, moet u ervoor zorgen dat uw Bitaxe de juiste warmteafvoer heeft. Een Bitaxe Gamma met een goede koelplaat en ventilator biedt het noodzakelijke thermische beheer voor veilig overklokken. Apparaten met kleine koellichamen en ontoereikende ventilatoren mogen niet worden overklokt. Slechte koelprestaties leiden tot thermische throttling en mogelijke schade aan de hardware. De relatie tussen warmte en de levensduur van componenten is cruciaal om te begrijpen. Te veel warmte creëert stress die elektronische componenten na verloop van tijd aantast, waardoor de operationele levensduur van je apparaat aanzienlijk wordt verkort.


### Strategische plaatsing koellichaam


Het meest kritieke onderdeel waarvoor extra koeling nodig is, is de buck converter, een klein zwart onderdeel aan de achterkant van de Bitaxe in de buurt van de grote spoel. Dit apparaat converteert de binnenkomende 5V voeding naar de juiste spanning voor de ASIC chip, meestal rond de 1,2V. De buck converter, ook wel TPS genoemd, genereert aanzienlijke warmte tijdens het gebruik en vormt een thermisch knelpunt dat het overklokpotentieel beperkt. Het installeren van een klein zelfklevend koellichaam op deze component zorgt niet alleen voor een hogere overklok headroom, maar verbetert ook de algehele efficiëntie door thermische verliezen te verminderen.


De plaatsing van extra koellichamen kan andere delen van de printplaat met een hoge stroomsterkte ten goede komen. Het spanningsregelcircuit wordt zwaar belast doordat de stroom van het ingangsgedeelte via verschillende printsporen naar de ASIC-chip gaat. Veel ervaren overklokkers plaatsen koellichamen aan de voorkant van de Bitaxe in deze gebieden met hoge stroom om de thermische dissipatie te verbeteren. Hoewel dit niet strikt noodzakelijk is voor gematigd overklokken, worden deze extra koelmaatregelen belangrijk als de frequenties tot extreme niveaus worden opgedreven.


### Overwegingen en beperkingen van het koelsysteem


De ESP32-controller, zichtbaar als het zilverkleurige onderdeel op het bord, heeft doorgaans geen extra koeling nodig. Deze component genereert zelfstandig minimale warmte en wordt alleen warm door warmteoverdracht van omliggende componenten. Het installeren van koellichamen in de buurt van de ESP32 kan de aangrenzende Wi-Fi-antenne verstoren, waardoor de draadloze connectiviteit en signaalkwaliteit afnemen. Richt de koeling op de stroomregelingscomponenten en het ASIC-gebied in plaats van op het besturingscircuit.


Dubbele ventilatorconfiguraties hebben zowel mogelijkheden als beperkingen. Hoewel het toevoegen van een tweede ventilator om lucht over de achterkant van de Bitaxe te blazen de koelprestaties kan verbeteren, kan de firmware van het apparaat slechts één ventilator goed aansturen. De Bitaxe heeft twee ventilatorheaders maar slechts één fancontroller, wat betekent dat het aansluiten van twee ventilatoren de firmware in verwarring brengt omdat deze tegenstrijdige RPM-signalen ontvangt. Deze configuratie werkt wel, maar kan leiden tot onvoorspelbaar gedrag van de ventilatorregeling.


### Beoordeling van basisprestaties


Voordat u overklokaanpassingen uitvoert, moet u de basisprestaties vaststellen door uw Bitaxe enkele uren te laten draaien met de standaardinstellingen. Controleer de temperatuur van de ASIC, de temperatuur van de spanningsregelaar en het percentage ventilatorsnelheid via de webinterface. Bij optimale bedrijfstemperaturen moet de ASIC onder 60°C blijven en de spanningsregelaar onder 60°C onder normale omstandigheden. Als uw apparaat al werkt boven 65°C op de ASIC of 70-80°C op de spanningsregelaar bij standaardinstellingen, is extra koelhardware verplicht voordat u verder gaat met overklokken.


De systematische aanpak voor frequentieverhogingen bestaat uit stapsgewijze stappen met behulp van de voorgedefinieerde frequentieopties in het instellingenmenu. Begin met het selecteren van de volgende beschikbare frequentiestap boven je huidige instelling, terwijl je de standaard kernspanning behoudt. Met deze conservatieve aanpak kunt u de thermische en stabiliteitsimpact evalueren voordat u extra wijzigingen aanbrengt. Laat het apparaat ten minste 30 minuten tot een uur werken op elke nieuwe frequentie-instelling, waarbij je de temperatuurtrends en de stabiliteit van de hashsnelheid gedurende de evaluatieperiode in de gaten houdt.


### Geavanceerde aangepaste configuratie


Toegang tot aangepaste frequentie- en voltage-instellingen vereist het inschakelen van de geavanceerde overklokinterface door "?OC" toe te voegen aan de URL van de webinterface van het apparaat. Dit ontgrendelt handmatige invoervelden voor nauwkeurige frequentie- en spanningsregeling, vergezeld van toepasselijke waarschuwingen over de risico's van het werken buiten de ontworpen parameters. De aangepaste interface maakt fijnafstelling buiten de standaard frequentiestappen mogelijk, zodat ervaren gebruikers de prestaties voor hun specifieke koelconfiguraties kunnen optimaliseren.


Wanneer u aangepaste instellingen gebruikt, moet u conservatieve stappen van 10-15 MHz per aanpassingsstap aanhouden. Deze methodische aanpak voorkomt plotselinge thermische pieken en maakt het mogelijk om de stabiliteit op elk frequentieniveau goed te testen. Sommige geavanceerde gebruikers bereiken frequenties rond 700 MHz met kernspanningen die zijn ingesteld op 1,175 V of vergelijkbare waarden, maar deze extreme instellingen vereisen uitgebreide koelingaanpassingen en zorgvuldig toezicht. De spanningsregelaar kan werken bij temperaturen tot 100°C zonder directe schade, maar hogere temperaturen verminderen de efficiëntie en betrouwbaarheid op de lange termijn. Succesvol overklokken vereist geduld, systematisch testen en voortdurend controleren om stabiele prestatieverbeteringen te bereiken met behoud van hardware-integriteit.


# Laatste Sectie

<partId>33367393-17a7-58d4-8359-79fffc6221fb</partId>


## Deze cursus evalueren

<chapterId>785f8b92-c8a6-5a65-aa39-e9753a7edf51</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusie

<chapterId>758baee6-2404-56fb-b534-6a39e441ae29</chapterId>

<isCourseConclusion>true</isCourseConclusion>