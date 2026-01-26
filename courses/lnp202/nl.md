---
name: Je eerste Lightning-node opzetten
goal: Een Lightning-node begrijpen, installeren, configureren en gebruiken
objectives: 


  - De rol en het doel van een Lightning-knooppunt begrijpen.
  - De verschillende beschikbare softwareoplossingen identificeren.
  - Installeer en configureer een Lightning-knooppunt (LND).
  - Sluit een onkostenrekening aan.
  - Ken de risico's van het gebruik van een Lightning-node.


---

# Je eerste stap naar autonomie op Lightning



Je hebt je eerste sats al aangeschaft, je eigen middelen veiliggesteld en een Bitcoin node ingezet om soeverein te zijn in je on-chain gebruik. De volgende stap is het verkrijgen van dezelfde autonomie op Lightning: dat is precies het doel van deze cursus.



LNP202 is gericht op gemiddelde gebruikers en leidt u stap voor stap door de implementatie van uw eerste Lightning-node, zonder geavanceerde technische vaardigheden.



Je leert hoe je LND op Umbrel installeert, je kanalen opent en beheert, toezicht houdt op je node en een mobiele wallet aansluit, zodat je kunt genieten van een ervaring die vergelijkbaar is met die van een custodial wallet, terwijl je de volledige controle over je fondsen behoudt.



+++


# Inleiding


<partId>5e77c17a-0853-4f36-a988-1b4a956f49e4</partId>



## Cursusoverzicht


<chapterId>e0871abf-af6d-4221-9389-1a996aea9b79</chapterId>



LNP202 is een praktijkgerichte cursus, ontworpen om je autonoom te maken op Lightning door je eigen node te bedienen. Het doel is eenvoudig: begin met een reeds bestaande Bitcoin node, zet LND in op Umbrel, beveilig het goed, open en beheer je eerste kanalen en gebruik je node vervolgens dagelijks vanaf een mobiele wallet. Deze cursus gaat ervan uit dat je BTC 202 al hebt gevolgd, omdat ik ervan uitga dat je Bitcoin node op Umbrel geïnstalleerd en gesynchroniseerd is. We zullen hier niet herhalen hoe je een Bitcoin node instelt.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Voor een beter begrip van de interne mechanica van Lightning, wordt de LNP 201 cursus ook sterk aanbevolen, hoewel het geen vereiste is voor deze cursus:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

In het eerste deel van deze LNP202 cursus kijken we naar wat een Lightning node werkelijk is, hoe het verschilt van een eenvoudige wallet, en waarom een persoonlijk node de enige manier is om Lightning te gebruiken zonder je sats te delegeren aan een vertrouwde derde partij. Dit deel eindigt met een strategische keuze: welke oplossing is geschikt voor jou, van de eenvoudigste benaderingen tot het klassieke Lightning-knooppunt, dat we in deze cursus zullen implementeren.



In deel 2 van de cursus installeer je LND op Umbrel, waarna je de elementen installeert die de duurste fouten voorkomen: een realistische back-upstrategie en bescherming tegen valsspelen via een uitkijktoren. Zodra deze basis is geïnstalleerd, open je je eerste kanaal, zodat je kunt beginnen met betalen op Lightning met je eigen infrastructuur.



Zo zie je maar: in deze LNP202 cursus gaan we een Lightning node opzetten in plug-and-play modus via Umbrel, in plaats van de klassieke commandoregel aanpak, om het geschikt te maken voor gemiddelde gebruikers. Als je de voorkeur geeft aan een opdrachtregelinstallatie, raad ik je aan de onderstaande tutorial te volgen. Andere, meer geavanceerde, opdrachtregel-georiënteerde Lightning-cursussen zijn ook in voorbereiding.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Deel 3 brengt je van een node die werkt naar een node die je kunt besturen. Je begint met het bepalen van het profiel van je Lightning-nodeoperator (consument, handelaar of router), waarna je een compleet softwarepakket voor beheer onder de knie krijgt om je kanalen te volgen en netjes te handelen in je topologie. Tot slot zul je een zeer belangrijk Lightning-punt aanpakken: hoe verkrijg je inkomende liquiditeit, via betaalde of coöperatieve oplossingen.



Deel 4 richt zich op dagelijks gebruik. Je zult een verbinding opzetten tussen je knooppunt en een mobiele klant, zodat je eenvoudig vanaf je smartphone kunt betalen en ophalen, zonder zelfbehoud op te geven. We kijken eerst naar een netwerkbenadering via *Tailscale*, dan naar een protocolbenadering via *Nostr Wallet Connect*, met hun respectievelijke voordelen en nadelen. De cursus wordt afgesloten met een laatste hoofdstuk dat je de juiste gewoonten zal geven om je zelfbehoud te ondersteunen, zowel operationeel als pedagogisch.



Als je deze LNP202 cursus in de juiste volgorde volgt, heb je aan het eind een complete configuratie voor je Lightning node, functioneel voor dagelijks gebruik en vooral onder controle.




## Lightning-knooppunten begrijpen


<chapterId>8275dfd8-7a72-48cc-bf7f-bc2a46063003</chapterId>



Voordat je je eigen knooppunt lanceert, wordt in dit hoofdstuk kort de basistheorie achter Lightning Network besproken. Het is inderdaad belangrijk om de betrokken mechanismen te begrijpen, omdat dit je in staat stelt om risico's te identificeren en goede praktijken toe te passen om ze te beperken. Ik zal hier echter niet in detail treden, omdat dit niet het hoofddoel van deze cursus is. Als je dieper op het onderwerp wilt ingaan, raad ik je ten zeerste aan om de LNP 201 cursus van Fanis Michalakis te raadplegen, die een referentie is op dit gebied:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Wat is een Lightning-knooppunt?



Laten we teruggaan naar de basis: voordat we definiëren wat een knooppunt is, moeten we begrijpen wat Lightning Network is. Het is een toplaagprotocol, gebouwd bovenop Bitcoin, ontworpen om offchain BTC transacties mogelijk te maken die snel (met bijna onmiddellijke finaliteit) en over het algemeen goedkoop zijn. "Offchain" betekent dat transacties die op Lightning worden uitgevoerd niet bedoeld zijn om op de hoofd-blockchain van Bitcoin te verschijnen. Lightning is ook een gedeeltelijke reactie op het toenemende gebruik van Bitcoin en op de congestie op de onchain, die zorgen baart over de schaalbaarheid van het systeem.



Om te kunnen werken, vertrouwt Lightning op het openen van betaalkanalen tussen deelnemers, waarbinnen transacties bijna ogenblikkelijk kunnen worden uitgevoerd, vaak met minimale kosten, zonder dat ze één voor één geregistreerd hoeven te worden op de Bitcoin blockchain. Deze kanalen kunnen zeer lang open blijven staan en vereisen alleen onchain-transacties wanneer ze geopend en gesloten worden.



Een Lightning-knooppunt is een deelnemer aan het Lightning-netwerk, die kanalen opent en betalingen doet met andere knooppunten. Concreet is een Lightning-knooppunt een stuk software dat op een computer draait en het Lightning Network-protocol implementeert. Voorbeelden zijn LND, Core Lightning of Eclair. De belangrijkste rol van deze software is:




- verbinding maken met een Bitcoin knooppunt om informatie te verkrijgen van de hoofdblokchain;
- bidirectionele betalingskanalen aanmaken en beheren met andere knooppunten;
- berichten uitwisselen met het hele Lightning-netwerk.



![Image](assets/fr/001.webp)



### Node vs. Lightning Wallet: een belangrijk onderscheid



Op Bitcoin (onchain) verwijst "*wallet*" naar software die je private sleutels beheert, je balans berekent uit je UTXO's en je transacties opbouwt. Deze wallet kan gebaseerd zijn op je eigen Bitcoin node of op die van iemand anders, maar vandaag de dag zijn de rol van de node en die van de onchain wallet duidelijk gescheiden.



Op Lightning is het moeilijker om dit soort woordenschat te hergebruiken zonder verwarring te scheppen. De term "*Lightning wallet*" is nogal vaag, omdat er in werkelijkheid niet zoiets bestaat als een echt zelfbehoudende Lightning wallet, tenzij het gebaseerd is op een knooppunt. Er zijn daarom slechts twee situaties mogelijk:



- Om een echt Lightning-knooppunt te hebben (d.w.z. niet-beveiligd): de software die je gebruikt (bijv. een mobiele app zoals Phoenix of een LND instantie op Umbrel) draait in feite een knooppunt, en jij hebt in feite de sleutels om je bitcoins op te halen. In dit geval is je "*Lightning wallet*" eigenlijk gewoon een gebruikersinterface bovenop een Lightning-node, of die nu ingebed is of op afstand.



- Een custodial service gebruiken: je gebruikt een applicatie die je een saldo laat zien in sats op Lightning, maar op de achtergrond bevinden de fondsen zich op het knooppunt van een provider (bijv. Wallet of Satoshi). Jij hebt noch de sleutels, noch de controle over de kanalen. Je saldo is slechts een boekhoudkundige invoer in de database van het bedrijf. Het is vergelijkbaar met het achterlaten van je bitcoins op een uitwisselingsplatform, met alle risico's van dien. In dit geval is je "*Lightning wallet*" slechts een toegang tot een rekening die beheerd wordt door een operator die op zijn beurt een echt Lightning knooppunt beheert.



Er is dus geen tussenweg bij Lightning: of je hebt een node (zelfs een embedded node), dus je bent in eigen beheer, of je hebt dat niet, dus een bedrijf is eigenaar van je sats. Maar zoals we in de volgende hoofdstukken zullen zien, zijn deze twee toepassingen soms moeilijk te onderscheiden. Phoenix is bijvoorbeeld een mobiele applicatie die een echt Lightning knooppunt integreert, maar de gebruiker is zich daar niet noodzakelijk van bewust, omdat de volledige complexiteit van zijn werking bijna volledig verborgen is.



### Een herinnering aan hoe de Lightning Network werkt



In dit gedeelte geef ik een korte uitleg over hoe Lightning werkt. Nogmaals, als je een meer diepgaande presentatie van de theoretische concepten wilt, nodig ik je uit om de speciale LNP 201 cursus te bekijken.



#### Betalingskanalen: openen, bijwerken en sluiten



Het hart van het Lightning-netwerk is gebaseerd op bidirectionele betalingskanalen. Een kanaal kan worden geopend (d.w.z. aangemaakt), bijgewerkt als Lightning-transacties plaatsvinden, en uiteindelijk worden gesloten. Vanuit het oogpunt van onchain is een kanaal niets meer dan een 2/2 multisignature-uitgang.



![Image](assets/fr/002.webp)



Vanuit het oogpunt van Lightning is het een betalingskanaal met liquiditeit verdeeld tussen de twee deelnemers.



![Image](assets/fr/003.webp)





- Een kanaal openen:**



Twee nodes besluiten een kanaal te openen. Een van hen commit bitcoins in een onchain transactie genaamd *funding transaction*. Deze transactie creëert een output gebaseerd op een 2-of-2 multisignature script, wat betekent dat het uitgeven van deze fondsen op Bitcoin de handtekening vereist van beide nodes in het kanaal. Alvorens deze transactie uit te geven, vraagt de partij die de fondsen verstrekt aan de andere partij om een *intrektransactie* te ondertekenen, die niet onchain wordt uitgegeven, maar die haar in staat stelt om haar fondsen terug te krijgen in het geval van een probleem.



![Image](assets/fr/004.webp)





- Commitment transacties:**



De toestand van het kanaal (d.w.z. de verdeling van sats tussen A en B) wordt vertegenwoordigd door een *commitment transaction*, bekend bij beide nodes maar niet onmiddellijk uitgezonden op de blockchain. Deze transactie beschrijft hoe de kanaalfondsen op de blockchain worden herverdeeld volgens de betalingen op Lightning.



Bij elke Lightning-betaling ondertekenen de twee knooppunten een nieuwe status die de vorige vervangt. De oude status wordt herroepen dankzij een revocatiesleutelmechanisme: als een van de deelnemers een oude status probeert uit te zenden, kan de andere als straf het volledige bedrag terugvorderen.



Het belangrijke idee hier is dat er altijd een ondertekende Bitcoin transactie is, niet onchain uitgezonden, die door de knooppunten wordt bijgehouden en die de herverdeling van elkaars sats mogelijk maakt volgens de betalingen die op Lightning Network zijn gedaan.



![Image](assets/fr/005.webp)





- Kanaalafsluiting:**



Een kanaal kan netjes worden gesloten via een coöperatieve sluiting, wanneer beide partijen het eens zijn over de laatste toestand van het kanaal, of eenzijdig (een gedwongen sluiting) als een van de deelnemers niet meer meewerkt of onbereikbaar wordt. In alle gevallen neemt de sluiting de vorm aan van een onchain transactie die de 2/2 output besteedt en de fondsen verdeelt tussen de deelnemers volgens de laatste geldige toestand van het kanaal.



![Image](assets/fr/006.webp)



Lightning functioneert dus als een secundaire laag die verankerd is op Bitcoin: alleen bepaalde gebeurtenissen (het openen en sluiten van kanalen) verschijnen op de hoofdblockchain. Tussenliggende betalingen blijven offchain.



Voordat we verder gaan, zijn hier twee essentiële concepten om te begrijpen hoe je een Lightning-kanaal beheert:




- Liquidity*: de hoeveelheid sats die beschikbaar is aan één kant van het kanaal;
- De *capaciteit*: dit is het totale bedrag dat is vergrendeld in de 2/2 multisig-uitgang, d.w.z. de som van de liquiditeit aan beide zijden van het kanaal.



#### Een netwerk van kanalen en liquiditeit



Een kanaal is niet alleen voor betalingen tussen twee knooppunten: het is onderdeel van een wereldwijd netwerk van onderling verbonden kanalen. Jouw knooppunt kan betalingen voor andere gebruikers routeren via zijn eigen kanalen, en jij kunt sats sturen naar een Lightning-knooppunt waarmee je geen direct kanaal hebt, zolang er een geldig pad kan worden gevonden tussen jouw twee knooppunten.



Elk knooppunt kent, via het roddelprotocol, een kaart van dit netwerk: welke kanalen er bestaan, welke knooppunten verbonden zijn door een tweerichtingskanaal en welke capaciteiten gepubliceerd zijn. Om een betaling naar een ontvanger zonder direct kanaal te sturen, berekent jouw knooppunt een route die uit verschillende hops bestaat: jouw knooppunt → knooppunt X → knooppunt Y → knooppunt van de ontvanger. Bij elke stap passeert de betaling een kanaal dat voldoende liquiditeit moet hebben in de richting van de betaling.



![Image](assets/fr/007.webp)



De liquiditeit van een kanaal is daarom niet symmetrisch: de ene kant kan zwaar belast zijn, terwijl de andere kant bijna leeg is. Het beheren van deze liquiditeit, d.w.z. weten waar de sats zich bevinden en in welke richting ze kunnen stromen, is een van de belangrijkste aspecten van het beheren van een Lightning knooppunt. We zullen hier dieper op ingaan in de komende praktische hoofdstukken.



#### HTLC: betaling transporteren zonder beroofd te worden



Om betalingen via tussenliggende knooppunten te laten verlopen zonder dat er vertrouwen nodig is, gebruikt Lightning slimme contracten genaamd *HTLC* (*Hashed Time-Locked Contracts*). Eenvoudig gezegd maakt een HTLC de overdracht van fondsen afhankelijk van de onthulling van een geheim en bevat het een tijdsbeperking om de verzender te beschermen in het geval van een mislukte transactie. Elke betaling is daarom afhankelijk van de presentatie van een pre-image (een geheim waarvan de hash overeenkomt met een afgesproken waarde). Als de uiteindelijke ontvanger deze pre-image levert, kan hij of zij het geld opeisen, wat op zijn beurt elk tussenliggend knooppunt in staat stelt om zijn eigen geld terug te krijgen.



![Image](assets/fr/008.webp)



Ik zal je de technische details over de werking van HTLC's besparen, want die zijn niet essentieel voor deze cursus. Je vindt een uitgebreide uitleg in de LNP 201 theoriecursus. Onthoud alleen dat HTLC's atomaire uitwisselingen mogelijk maken: of de overdracht wordt voltooid en niemand wordt geschaad in de routing, of het mislukt en elke deelnemer krijgt zijn of haar oorspronkelijke fondsen terug. Er is geen tussenweg.



### De belangrijkste implementaties van Lightning-knooppunten



Net als bij Bitcoin zijn er verschillende implementaties van het Lightning protocol. Een aantal onafhankelijke teams ontwikkelen hun eigen versies, die allemaal interoperabel zijn omdat ze dezelfde specificaties volgen (de BOLT's). Dit zijn de belangrijkste implementaties die momenteel in gebruik zijn.



#### LND (*Lightning Network Daemon*)



LND is een complete implementatie van het Lightning protocol, geschreven in Go en ontwikkeld door Lightning Labs.



![Image](assets/fr/009.webp)



#### Kernbliksem (*CLN*)



Core Lightning (voorheen *C-Lightning*) is de implementatie ontwikkeld door Blockstream. Het is geschreven in C, met enkele componenten in Rust.



![Image](assets/fr/010.webp)



#### Eclair



Eclair is een implementatie geschreven in Scala en ontwikkeld door het Franse bedrijf ACINQ. ACINQ beheert een van de belangrijkste routeringsknooppunten in het Lightning-netwerk met Eclair en gebruikt deze implementatie als softwarebasis voor zijn eigen producten, zoals de Phoenix-toepassing.



![Image](assets/fr/011.webp)



#### LDK (*Lightning Development Kit*)



LDK (*Lightning Development Kit*) is een Rust ontwikkelkit, onderhouden door Spiral (Block, ex-Square). Het is geen kant-en-klare daemon zoals LND of CLN, maar een bibliotheek voor ontwikkelaars die Lightning direct in hun applicaties willen integreren.



![Image](assets/fr/012.webp)



In deze LNP202 cursus zullen we ons voornamelijk concentreren op LND: de implementatie die het meest gebruikt wordt in kant-en-klare oplossingen voor particuliere klanten, zoals Umbrel.



Tot zover deze korte herinnering aan hoe Lightning werkt. Nogmaals, als er concepten zijn die je niet begrijpt, of als je wat dieper wilt graven voordat je ze in de praktijk brengt, dan is de cursus van Fanis Michalakis de essentiële referentie over dit onderwerp:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


## Waarom je eigen Lightning-node beheren?


<chapterId>421db24e-511c-41ed-ad68-69b0662042ea</chapterId>



Het antwoord op deze vraag is vrij eenvoudig, omdat het retorisch is: zonder je eigen node gebruik je Lightning niet meer echt, maar alleen de illusie van Lightning over de infrastructuur van een bedrijf.



Het gebruik van een Lightning custodial wallet betekent dat de bitcoins technisch gezien toebehoren aan het bedrijf dat het knooppunt beheert. Jij hebt de privésleutels niet en je hebt geen controle over de kanalen. Jouw wallet saldo is gewoon een regel in de database van een serviceprovider. Deze situatie is zeker erg handig voor beginners, en de gebruikerservaring is vaak vloeiend, maar de fundamentele vraag is: wat is het voordeel van het gebruik van Bitcoin en Lightning als je uiteindelijk juist die aspecten opgeeft die hen onderscheiden van traditionele valuta en banken?



De twee belangrijkste waardeproposities van Bitcoin zijn monetaire soevereiniteit (niet langer afhankelijk van een centrale autoriteit voor het uitgeven en vasthouden) en censuurbestendigheid (onmogelijkheid voor een derde partij om betalingen te voorkomen of te filteren). Een custodial systeem op Lightning gaat regelrecht in tegen deze twee doelstellingen: je kunt de interne geldvoorraad van het platform niet controleren en per definitie kan een operator die alle fondsen en kanalen in handen heeft je betalingen censureren, vertragen, prioriteren of blokkeren. Onder deze omstandigheden kunnen we ons terecht afvragen, **wat heeft het voor zin om bitcoin via Lightning te gebruiken als het dezelfde patronen van vertrouwen en afhankelijkheid gaat reproduceren als bij traditionele staatsvalutasystemen**.



> Wat nodig is, is een elektronisch betalingssysteem dat gebaseerd is op cryptografisch bewijs in plaats van vertrouwen, waardoor twee partijen direct met elkaar kunnen handelen zonder dat er een vertrouwde derde partij nodig is.
*Satoshi Nakamoto, Bitcoin Witboek


Afgezien van de filosofie zijn de meer concrete nadelen voor jou als volgt. Ten eerste kun je op geen enkele manier controleren of het bedrijf daadwerkelijk de bitcoins bezit die overeenkomen met de weergegeven tegoeden. Het kan met fractionele reserve werken, gehackt worden, failliet gaan of gewoon verdwijnen. In dit geval ben je gewoon een andere schuldeiser, zonder echte garantie dat je je geld terugkrijgt.



Ten tweede is het bedrijf onderhevig aan regelgevingsrisico's: rechterlijke bevelen, bevriezing van tegoeden, verzoeken om gebruikers of transacties te blokkeren, verscherpt toezicht of zelfs een volledig verbod op activiteiten in bepaalde rechtsgebieden. Elke beperking die op de serviceprovider weegt, heeft automatisch gevolgen voor jou.



Op het gebied van vertrouwelijkheid is de situatie niet beter. Een custodial operator ziet al uw stromen: bedragen, frequenties, ontvangers, saldi, bestedingsgewoonten. Gecombineerd met informatie uit de applicatie en eventueel de onderliggende ketenanalyse op Bitcoin, kan deze informatie een zeer nauwkeurig profiel van uw financiële activiteit opleveren. Nogmaals, dit is ver verwijderd van het doel van Bitcoin om financiële controle te verminderen.



Het goede nieuws is dat het beheren van je eigen Lightning node vandaag de dag niet meer voorbehouden is aan technische experts, zoals het misschien wel was aan het eind van de jaren 2010. Er zijn relatief eenvoudige oplossingen beschikbaar voor thuisgebruikers, die we in detail zullen uitleggen in het volgende hoofdstuk.




## De juiste oplossing voor de klus kiezen


<chapterId>615870e3-741d-4ec1-875d-a483e70f39d4</chapterId>



Vandaag de dag is het mogelijk om een gebruikerservaring te hebben die heel dicht bij die van een Lightning custodial wallet ligt, terwijl je zelf in bewaring blijft. Het doel van dit hoofdstuk is om je te helpen het pad te kiezen dat het beste bij jouw profiel past.



### Optie 1: Bliksem niet rechtstreeks gebruiken



De eerste oplossing is simpelweg om Lightning niet natively te gebruiken, maar om een Bitcoin of Liquid wallet te gebruiken die atomic swaps integreert. Bijvoorbeeld Aqua of Bull Bitcoin Wallet toepassingen gebruiken deze methode, door je in staat te stellen Lightning-facturen te betalen zonder zelf een Lightning-node te bedienen, terwijl je in self-custody blijft.



Het principe is eenvoudig: je geld blijft in Bitcoin, on-chain of Liquid, en je hebt er toegang toe via een wallet waar je op de traditionele manier de sleutels bewaart. Wanneer je een Lightning-factuur scant, initieert je wallet een transactie (on-chain of Liquid) naar een atomaire swapservice. Deze dienst beheert vervolgens de Lightning-betaling via zijn eigen knooppunt, met behulp van de bitcoins die je on-chain of via Liquid hebt verstrekt. Hierdoor hoef je zelf geen Lightning-kanalen af te handelen, maar kun je toch naadloos Lightning-facturen vereffenen.



![Image](assets/fr/013.webp)



Het grote voordeel van deze aanpak, vergeleken met een conventionele Lightning wallet custodial, is dat je te allen tijde 100% eigenaar blijft van je fondsen. De bitcoins zitten in je onchain of Liquid wallet, met je eigen mnemonische zin. Zelfs tijdens de ruil blijft u in het bezit van uw fondsen, omdat de ruil atomair is. Het vertrouwt op een cryptografisch mechanisme dat ervoor zorgt dat er slechts twee mogelijke uitkomsten zijn: of de swap slaagt volledig, of het mislukt en de dienst kan zich uw fondsen niet toe-eigenen.



De meeste portefeuilles die dit type functionaliteit bieden, vertrouwen op [Boltz](https://boltz.exchange/) voor het technische gedeelte van de ruil.



Deze oplossing biedt ook interessante voordelen op het gebied van vertrouwelijkheid, vooral in combinatie met Liquid. Voor een beginner is het ook heel eenvoudig in te stellen en op te slaan: een klassieke ezelsbruggetje, geen kanalen, geen liquiditeit om te balanceren...



Aan de andere kant heeft deze aanpak zijn beperkingen. Ten eerste is het niet onbetaalbaar: u bent afhankelijk van de beschikbaarheid en goodwill van de ruildienst. Als deze je account niet meer wil verwerken of ophoudt te werken, kun je niet langer Bliksemfacturen via deze dienst betalen. Dan zijn er nog de niet onaanzienlijke kosten: u betaalt zowel de onchain of Liquid transactiekosten, als de commissie van de swapdienst. Als de onchainkosten sterk stijgen, kan het erg duur worden om Lightning te gebruiken.



Dus voor incidenteel gebruik is het nog steeds acceptabel, maar voor een zeer actieve Lightning-gebruiker is het beter om het goed te doen met een echte Lightning-node.



### Optie 2: On-board Lightning-knooppunten



De tweede categorie oplossingen is gebaseerd op Lightning nodes die direct in een mobiele toepassing zijn ingebed. Phoenix Wallet pionierde met dit model en blijft een benchmark. Tegenwoordig bieden andere projecten vergelijkbare benaderingen, zoals Zeus (in ingebedde modus) of BitKit.



Het idee is eenvoudig: de applicatie draait eigenlijk een Lightning-node, maar alle complexe operaties worden automatisch op de achtergrond afgehandeld. Je hebt een "*Lightning wallet*" interface met een mnemonische zin voor back-up, je ziet een saldo en betaalt facturen, maar je beheert geen kanalen, liquiditeit of de meeste parameters.



![Image](assets/fr/014.webp)



Deze oplossingen zijn altijd self-custodial. De sleutels die de fondsen beheren zijn generated en opgeslagen op je telefoon, en back-up gebeurt via een seed of gelijkwaardig mechanisme. Je hebt niet gewoon een rekening bij een serviceprovider, je bezit bitcoins die opgesloten zitten in kanalen die van jou zijn en niet gestolen kunnen worden.



De voordelen van LN boordknooppunten zijn talrijk:




- uiterst eenvoudig te installeren en te gebruiken;
- gebruikerservaring die lijkt op die van een Lightning wallet, maar dan met zelfbehoud;
- geen handmatig beheer van kanalen of liquiditeit;
- relatief eenvoudige back-up.



Maar deze embedded wallet's hebben ook belangrijke beperkingen. Ten eerste, in termen van vertrouwelijkheid, heeft de service operator (bijv. ACINQ in het geval van Phoenix) een vrij gedetailleerd beeld van de stromen die door jouw node gaan: hoeveelheden, frequenties, ontvangers, ook al zal dit zeker verbeteren, vooral met de geleidelijke invoering van *Trampoline Nodes*. Ten tweede ben je sterk afhankelijk van deze operator als je belangrijkste Lightning peer. Als het ACINQ-knooppunt onbeschikbaar wordt (in het geval van Phoenix), als het bedrijf onder druk komt te staan door regelgeving of zijn bedrijfsmodel verandert, kan uw gebruikerservaring ernstig verslechteren of zelfs in gevaar komen.



Aan deze eenvoud hangt een prijskaartje. Embedded LN node services brengen over het algemeen specifieke kosten in rekening voor stortingen, opnames of bepaalde kanaalbeheertransacties. Naar mijn mening is dit model zinvol als het gaat om de geboden service, maar voor intensief gebruik kan het veel duurder zijn dan een goed beheerd conventioneel Lightning-knooppunt.



### Optie 3: het klassieke Lightning-knooppunt



De derde oplossing, waar we in deze LNP202 cursus dieper op in zullen gaan, is het gebruik van een conventioneel Lightning knooppunt op een speciale server of apparaat.



Met "klassiek" bedoel ik dat je zelf een Lightning-implementatie (bijv. LND) installeert en configureert bovenop je eigen Bitcoin-knooppunt. Je kiest je peers, opent je kanalen, beheert je inkomende en uitgaande liquiditeit en stelt je routeringskostenbeleid in.



In termen van soevereiniteit is het de beste oplossing. Je bent niet langer afhankelijk van een specifiek bedrijf voor je kanalen of betalingen: als een peer je censureert of een kanaal sluit, kun je een ander openen met een andere node. Als een dienst verdwijnt, blijven je sats in de kanalen die jij beheert en kun je ze onchain repatriëren. Je kunt ook je langetermijnkosten optimaliseren: als je kanalen eenmaal de juiste grootte hebben en goed worden beheerd, kunnen de totale kosten van betalingen erg laag worden.



In termen van vertrouwelijkheid ben je natuurlijk onderworpen aan de beperkingen van Lightning's eigen model, maar je geeft niet je hele bedrijf uit handen aan één enkele operator.



Daarentegen is het opzetten van een klassiek Lightning knooppunt duidelijk complexer: je moet installeren, configureren, onderhouden, updates controleren, de logica van kanalen en laadbeleid begrijpen, kanalen en cashflow beheren, enzovoort. Een verkeerde configuratie, slordige back-up of onzorgvuldig beheer kan gemakkelijker leiden tot het verlies van sats. Het knooppunt moet ook continu draaien.



Dit is precies het pad dat ik je voorstel te volgen in deze cursus, waarbij ik je bij elke stap begeleid om risico's te beperken en je aanpak te structureren.



### Welke oplossing voor welk gebruikersprofiel?



Om de juiste oplossing voor jouw Lightning-gebruikersprofiel te kiezen, moet je rekening houden met twee factoren: hoe vaak je Lightning gebruikt en je behoefte aan technisch beheer.



Als je af en toe niet veel Lightning-betalingen doet, maar toch af en toe LN-facturen wilt kunnen vereffenen vanaf je telefoon, zonder zelfbehoud op te geven: dan is een Bitcoin of Liquid wallet met swapfunctie waarschijnlijk de beste optie. Je behoudt het eigendom van je fondsen, beheert geen nodes en accepteert iets hogere kosten in ruil voor eenvoud.



https://planb.academy/tutorials/wallet/mobile/bull-bitcoin-2c72127c-a228-4f50-b833-c6183d56aaf6

https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Als u Lightning op vrij regelmatige basis gebruikt en de voordelen van een echt knooppunt wilt, maar geen tijd wilt besteden aan het beheren van kanalen, vergoedingen of infrastructuur, is een mobiel ingebed Lightning-knooppunt een goede oplossing. Je behoudt het beheer over je fondsen, de UX blijft zeer toegankelijk en alle complexiteit is verborgen, tegen de prijs van een sterke afhankelijkheid van een operator.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

https://planb.academy/tutorials/wallet/mobile/bitkit-a7224674-85c4-4045-9baf-37018d89550c

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Als je een gemiddelde of gevorderde gebruiker bent, bereid bent om tijd te investeren in het begrijpen en beheren van je infrastructuur, en maximale controle wilt over je kanalen, liquiditeit en kosten: dan is een klassieke servergebaseerde Lightning-node de beste oplossing. Het is de meest veeleisende oplossing, maar ook de meest consistente met Bitcoin's idee van soevereiniteit.




# Je eerste Lightning-knooppunt maken


<partId>b6db225e-61ab-437a-bccb-33d07503da15</partId>



## LND installeren met Umbrel


<chapterId>a0014bf3-1bd3-4311-b15b-5ef2354ec744</chapterId>



Nu we de basisprincipes van Lightning en de beschikbare oplossingen hebben besproken, is het tijd om aan de slag te gaan. Om deze cursus te volgen, heb je een Bitcoin node nodig die gesynchroniseerd is met Umbrel. Deze LNP202 training is een vervolg op BTC 202; als je nog geen Bitcoin node hebt, nodig ik je uit om deze andere training te volgen voordat je hier terugkomt, zodra je node is gesynchroniseerd. Ik raad je sterk aan deze te raadplegen, omdat ik niet in detail zal treden over de werking, configuratie en beveiligingsmaatregelen.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

In dit eerste hoofdstuk bekijken we hoe je LND installeert op je Umbrel. De manier waarop Umbrel werkt, maakt deze stap erg eenvoudig, omdat je alleen maar een toepassing hoeft te installeren.



Open vanaf de startpagina de `App Store` onderaan de interface.



![Image](assets/fr/015.webp)



Voer in de zoekbalk `Lightning Node` in en klik vervolgens op de toepassing.



![Image](assets/fr/016.webp)



Klik vervolgens op de knop `Installeren` om de installatie te starten.



![Image](assets/fr/017.webp)



Klik op de startpagina op de toepassing om deze te openen en selecteer vervolgens `Een nieuw knooppunt instellen`.



![Image](assets/fr/018.webp)



Je krijgt een geheugensteun van 24 woorden. Bewaar deze op een veilige plaats. We zullen in het volgende hoofdstuk dieper ingaan op hoe je opnieuw toegang krijgt tot je Lightning knooppunt (dit is een veel complexer proces dan voor een eenvoudige Bitcoin wallet), maar onthoud voor nu dat deze zin een cruciale rol speelt en met de grootste zorg moet worden bewaard.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Sla deze zin op dezelfde manier op als een conventionele geheugensteunzin: op een fysieke drager (papier of metaal) die op een veilige plaats is opgeslagen en klik vervolgens op de knop `NEXT`.



![Image](assets/fr/019.webp)



Voer vervolgens de woorden van je zin in om te controleren of je ze goed hebt opgeschreven.



![Image](assets/fr/020.webp)



Een waarschuwingsbericht herinnert je eraan dat de applicatie zich in een bètaversie bevindt en dat Lightning Network een experimentele technologie blijft. Leg uiteraard nooit bedragen vast op je Lightning node die je niet bereid bent te verliezen.



Je komt dan op de hoofdinterface van je Lightning-knooppunt. Aan de linkerkant ziet u uw Bitcoin onchain wallet gehost op uw knooppunt. Dit is de generated van de 24-woorden zin die je zojuist hebt opgeslagen.



In het midden staat je Lightning wallet. Het vertegenwoordigt eigenlijk je uitgaande geld, d.w.z. de bitcoins die je bezit binnen je Lightning-kanalen.



Aan de rechterkant zie je een aantal belangrijke stukjes informatie over je knooppunt:




- Het aantal verbindingen en open kanalen;
- Je totale uitgaande geldstroom, d.w.z. wat je in theorie kunt uitgeven aan Lightning;
- Je totale inkomende liquiditeit, d.w.z. wat je in theorie kunt ontvangen op Lightning.



![Image](assets/fr/021.webp)



Laten we beginnen met het aanpassen van onze node. Klik op de drie kleine puntjes rechtsboven in de interface en vervolgens op `Geavanceerde instellingen`. In het submenu `Personalisatie` kun je een publieke naam voor je knooppunt instellen (gebruik niet je echte naam) en de kleur kiezen.



![Image](assets/fr/046.webp)



Klik vervolgens op de groene knop `SAVE AND RESTART` om je node opnieuw op te starten en deze wijzigingen toe te passen.



Uw Lightning-knooppunt is nu klaar om de eerste kanalen voor het doen van betalingen te openen. Maar laten we eerst eens kijken hoe we uw sats kunnen beschermen!



## Je Lightning-knooppunt opslaan


<chapterId>638fa75d-62af-4bf3-ab4a-b7d10ea75815</chapterId>



Voordat je je eerste sats naar je node stuurt, is het belangrijk om te begrijpen hoe de back-up werkt en wat de bijbehorende risico's zijn. In tegenstelling tot een eenvoudige Bitcoin onchain portefeuille, is het back-uppen van een Lightning node behoorlijk complex: de verkeerde strategie kan leiden tot het permanente verlies van je fondsen. In dit hoofdstuk bekijken we wat er echt gebackupt moet worden, en hoe Umbrel dit proces afhandelt met LND.



In deze cursus gebruiken we de LND (*Lightning Network Daemon*) implementatie. Hoewel de principes vergelijkbaar zijn met de andere implementaties, zijn de herstelbestanden en procedures waar ik het over ga hebben specifiek voor LND.



### Wat moet ik opslaan op een Lightning-node?



Op een Lightning node is het niet voldoende om de seed op te slaan en te hopen dat alles weer normaal wordt. Verschillende elementen spelen verschillende rollen, dus het is belangrijk om ze van elkaar te onderscheiden.



#### De seed (*aezeed*)



Wanneer je LND initialiseert, ontvang je een seed met 24 woorden. Dit is een LND-specifiek formaat genaamd "*aezeed*". Het is geen klassieke seed BIP39, hoewel het er veel op lijkt. Uit deze seed leidt LND de private sleutels af van je onchain wallet geassocieerd met het Lightning knooppunt, d.w.z. de adressen waarop je bitcoins kunt ontvangen of waarnaar je bitcoins kunt repatriëren na kanaalsluitingen.



![Image](assets/fr/019.webp)



Deze seed kan daarom gebruikt worden om de wallet op de keten, die aan uw knooppunt gekoppeld is, opnieuw aan te maken, en om fondsen terug te halen die al op de keten gerepatrieerd zijn (bijvoorbeeld na een kanaalsluiting). Aan de andere kant is de seed alleen niet voldoende om uw Lightning-kanalen die nog open zijn te herstellen, omdat het niet de nodige informatie bevat over de status van uw kanalen.



#### De kanaaldatabase (`channel.db`)



LND slaat de gedetailleerde status van uw kanalen op in een database met de naam `kanaal.db`. Deze database bevat:




- de lijst van je open kanalen;
- je collega's en hun identifiers;
- de laatste commitment transaction's voor elk kanaal (de opeenvolgende staten die bepalen wie wat bezit in het kanaal en die het mogelijk maken om onchain-gelden terug te krijgen in het geval van een probleem);
- de informatie die nodig is om een collega te straffen die een oud rapport probeert uit te zenden.



Het probleem met deze database is dat hij constant verandert: elke betaling, elke routering, elke opening of sluiting van een kanaal wijzigt de inhoud. Daarom is een conventionele back-up (bijvoorbeeld een periodieke kopie van je `kanaal.db`) gevaarlijk. Als je een te oude versie van `channel.db` terugzet en de node opnieuw samenstelt met deze verouderde toestand, kunnen je medespelers denken dat je een oude kanaaltoestand uitzendt. In dit geval voorziet het protocol in een straf: je medespeler kan het volledige bedrag van het kanaal terugvorderen, alsof je hebt geprobeerd vals te spelen.



In de praktijk is `channel.db` dus niet echt een back-up medium. Het is de levende staat van je knooppunt. De enige situatie waarin het zinvol is om het te gebruiken om je knooppunt te herstellen, is wanneer je deze database direct herstelt van een machine die zojuist is uitgevallen (bijvoorbeeld een schijf die nog leesbaar is). In dit geval herstel je de meest recente staat en kun je LND herstarten op een andere machine gebaseerd op deze database, in de veilige wetenschap dat deze staat zo up-to-date mogelijk is, aangezien de oude machine niet meer draait. Een andere situatie waarin deze methode kan dienen als relevante back-up is in een configuratie met twee schijven, met een dynamische, permanente kopie van de ene naar de andere. Dit type opstelling is echter complexer om te implementeren.



Maar het maken van periodieke kopieën van `channel.db` en deze opslaan als back-ups om later terug te zetten is een heel slecht idee: op de dag dat je ze gebruikt, loop je het risico jezelf te straffen en al je sats te verliezen.



#### Statische kanaalback-up (SCB)



Om noodherstel mogelijk te maken, heeft LND het *Static Channel Backup* (SCB) mechanisme geïntroduceerd. Dit is een speciaal bestand, vaak `channel.backup` genoemd, dat statische informatie bevat over je kanalen: wie je peers zijn, hoe je ze kunt bereiken en wat je kanalen zijn.



Dit bestand bevat geen gedetailleerde kanaalstatus of updategeschiedenis. Het staat je niet toe kanalen te heropenen in de staat waarin ze waren, noch om deze Lightning node te blijven gebruiken. De rol van dit bestand is eerder om als ankerpunt te fungeren om je collega's te vragen je te helpen al je kanalen netjes af te sluiten, en zo je sats onchain te ontvangen, op sleutels die je kunt ophalen dankzij de seed. Dus, in tegenstelling tot het `channel.db` bestand, dat wordt aangepast bij elke betaling of routering, wordt het SCB bestand alleen bijgewerkt wanneer een kanaal wordt geopend of gesloten.



Bij herstel via SCB verloopt het proces als volgt:




- Je herstelt je seed (*aezeed*), die je onchain wallet verbonden met het Lightning knooppunt opnieuw creëert;
- Je geeft LND je meest recente SCB;
- LND gebruikt de SCB om de lijst van je collega's te vinden en de kanalen die je met hen hebt;
- Het neemt contact op met elke peer, vertelt hen dat u een gegevensverlies hebt geleden en vraagt hen om uw kanaal met hen "geforceerd te sluiten", zodat u uw onchain-aandeel kunt herstellen.



Het idee is dat je peers, die merken dat je een verlies van gegevens rapporteert, hun laatste commitment transaction uitzenden en het force channel sluiten. Zodra deze transacties zijn bevestigd, verschijnen je fondsen weer in je onchain portefeuille (gekoppeld aan de seed).



Dit herstelmechanisme is echter niet perfect. Ten eerste herstelt het niet echt je Lightning-knooppunt, aangezien alle kanalen worden gesloten. Je zult dan een nieuwe Lightning-node vanaf nul moeten opbouwen. Ten tweede garandeert het geen 100% herstel, hoewel het de kans op het herstellen van je onchain balansen aanzienlijk vergroot in het geval van een probleem. Dit herstelprotocol is namelijk afhankelijk van de medewerking en beschikbaarheid van je peers: als een van hen offline is, zijn eigen gegevens kwijt is of weigert mee te werken, kunnen je tegoeden geblokkeerd blijven of zelfs permanent verloren gaan. Daarom is het belangrijk om op je Lightning-node geen kanalen open te houden met onbereikbare peers voor lange perioden. Als je op dat moment gegevens verliest en de peer onbereikbaar blijft, is herstel via SCB onmogelijk en blijven je fondsen verloren totdat die peer weer online komt (misschien wel voor altijd).



Samengevat rust een goede back-upstrategie voor Lightning op LND op drie pijlers:




- Je seed (*aezeed*), voor de onchain laag;
- Betrouwbare automatische SCB-back-up;
- Goed kanaalbeheer door betrouwbare peers te kiezen en peers die vaak onbereikbaar zijn preventief af te sluiten.



### Hoe beheert Umbrel de back-up van uw LND knooppunt?



Umbrel biedt een vereenvoudigd back-upmechanisme voor het LND knooppunt, precies gebaseerd op de SCB. Het idee is om je de moeite te besparen om dit bestand zelf te manipuleren, er een back-up van te maken en het proces zoveel mogelijk te automatiseren.



Wanneer je je knooppunt op Umbrel aanmaakt, ontvang je een seed die een dubbele rol speelt:




- het leidt je Bitcoin af op de wallet-keten die geassocieerd is met je Lightning-knooppunt;
- het wordt gebruikt om een back-up-ID en coderingssleutel af te leiden die worden gebruikt voor externe SCB-back-ups.



Dankzij dit mechanisme maakt Umbrel automatisch een versleutelde back-up van je SCB en slaat deze op zijn servers op via Tor. De SCB wordt versleuteld opgeslagen, dankzij een sleutel die is afgeleid van je seed. Dus, in het geval van gegevensverlies, hoef je alleen maar een Bitcoin en Lightning node op Umbrel te maken, op dezelfde of een andere machine, en dan je seed in te voeren. U kunt dan de laatste SCB-status ophalen van de Umbrel-servers, deze ontsleutelen en beginnen met het herstellen van uw fondsen.



Deze back-ups worden lokaal versleuteld door uw node voordat ze worden verzonden, wat de vertrouwelijkheid van uw gegevens garandeert: Umbrel kan de inhoud van de SCB niet lezen. De verzending vindt plaats via Tor, waardoor je IP-adres niet kan uitlekken. Bovendien voegt jouw Umbrel ruis toe aan het verkeer (willekeurige opvulling en valse back-ups die met onregelmatige tussenpozen worden verstuurd) om te voorkomen dat de server precies kan afleiden wanneer je een kanaal opent of sluit.



Het belangrijkste voordeel van deze methode is dat het de back-up van je Lightning-node aanzienlijk vereenvoudigt: je hoeft maar één keer een back-up te maken van je seed tijdens de node-initialisatie. Dit brengt wel wat risico met zich mee, aangezien het alleen een back-up van de SCB is, maar voor redelijke hoeveelheden is het een acceptabel compromis.



### Beste praktijken om het risico op verlies te beperken



Zelfs met een Umbrel back-up kunnen een paar eenvoudige goede praktijken het risico op verlies van sats sterk verminderen:





- Controleer de beschikbaarheid van je collega's:



Als een belangrijk kanaal vaak geassocieerd wordt met een onbereikbare of instabiele "peer", dan is het veiliger om het netjes af te sluiten terwijl je knooppunt nog werkt. Een preventieve coöperatieve of geforceerde sluiting elimineert een potentiële bron van problemen in het geval van SCB herstel.





- Concentreer niet te veel liquiditeit op onbekende peers:



Hoe groter het kanaal dat een peer met je heeft, hoe belangrijker het is om betrouwbaar te zijn. Kies serieuze, goed verbonden en actieve nodes, zodat toekomstig herstel via SCB soepel kan verlopen.





- Vul Umbrel aan met lokale back-ups:



Naast de automatische back-up van Umbrel, kun je ook een versleutelde kopie van je SCB-bestand (`kanaal.back-up`) op externe media bewaren en deze regelmatig bijwerken. Idealiter zou je het elke keer moeten vernieuwen als je een kanaal opent of sluit. Dit geeft je een back-up oplossing als, om wat voor reden dan ook, Umbrel's automatische back-up service niet beschikbaar is.





- Uw seed op de juiste manier beheren



Jouw seed Umbrel herstelt niet alleen jouw onchain wallet, maar ontleent ook de coderingssleutel voor back-ups. Een aanvaller met toegang daartoe zou dus een herstel kunnen lanceren en jouw geld naar zijn eigen wallet overmaken, zonder zelfs fysieke toegang tot jouw node te hebben.



Als je dus je node moet herstellen, maar je seed niet meer hebt, kun je niets herstellen: al je sats is verloren. Het is dus erg belangrijk om je seed met de grootste zorg te bewaren, alleen op fysieke media (papier of metaal), en om het op een veilige plaats te bewaren. Voor meer informatie over het beheren van een seed, raadpleeg deze tutorial:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### Hoe sla ik mijn Lightning-knooppunt op Umbrel op?



Nu je weet hoe de theorie werkt, gaan we over tot de kern van de zaak. Klik vanuit je Lightning Node-toepassing (die eigenlijk LND is) op de drie kleine puntjes in de rechterbovenhoek.



![Image](assets/fr/022.webp)



Er zijn hier drie elementen van belang voor de back-up:




- Controleer of de optie `Automatische back-ups` is ingeschakeld. Hierdoor wordt uw versleutelde SCB automatisch naar de servers van Umbrel gestuurd.
- Je kunt dan kiezen of je via Tor of clearnet wilt verzenden, door de `Backup over Tor` optie te gebruiken. Zoals uitgelegd in de vorige secties, raad ik je sterk aan om Tor te gebruiken om je vertrouwelijkheid te bewaren.
- Tenslotte is er een `Download kanaal backup bestand` knop, waarmee je een `kanaal.backup` bestand, d.w.z. een versleutelde momentopname van je SCB, kunt downloaden naar je computer. Hiermee kun je van tijd tot tijd extra lokale back-ups maken, naast de back-ups die automatisch naar de Umbrel servers worden gestuurd.



Nu weet je hoe je de sats van je Lightning knooppunt kunt beschermen tegen gegevensverlies. In het volgende hoofdstuk bekijken we hoe je je knooppunt kunt beveiligen tegen pogingen tot valsspelen.




## Watchtower: rol en opzet


<chapterId>e6c654dd-26c5-4e4d-8d11-a215bac37812</chapterId>



In Lightning is elk kanaal gebaseerd op een opeenvolging van opeenvolgende toestanden, voorgesteld door ongepubliceerde commitment transactions. Bij elke Lightning-betaling of -routering bouwen de 2 deelnemers in het kanaal een nieuw paar commitment transaction's op, die de huidige verdeling van fondsen in het kanaal weergeven. Oude commitment transactions raken verouderd.



Als een van de partijen een verouderde status publiceert, heeft de andere partij het recht om dit te bestraffen en het volledige bedrag van het kanaal terug te vorderen. In dit hoofdstuk kijken we kort naar hoe dit mechanisme werkt en leggen we uit hoe je een ***watchtower*** opzet: een systeem om je Lightning knooppunt te beschermen tegen mogelijke valsspeel pogingen.



### Begrijpen hoe uitkijktorens werken


Op elk moment heeft elke partij in het kanaal een commitment transaction die, indien gepubliceerd, hen in staat zou stellen het kanaal te sluiten en hun deel van de fondsen terug te krijgen. Dit proces staat bekend als *gedwongen afsluiting*. Maar als ze proberen een oudere commitment transaction te publiceren, die overeenkomt met een vorige toestand van het kanaal waar het meer sats had, dan wordt deze transactie beschouwd als een poging tot valsspelen. In dit geval kan de tegenpartij de revocatiesleutel gebruiken die hoort bij deze oudere toestand om het volledige bedrag aan fondsen in het kanaal terug te krijgen, terwijl de bedrieger tijdelijk wordt geblokkeerd door het tijdslot.


Dit systeem betekent dat het publiceren van een oude status, d.w.z. een poging om vals te spelen, erg riskant is: als de andere partij deze transactie ziet op de mempool of op de blockchain voordat de tijdslot verloopt, kunnen ze de herroepingssleutel gebruiken en al het geld terugkrijgen. **Daarom hangt de veiligheid van je Lightning-kanaal af van je vermogen om een poging tot valsspelen te detecteren binnen het tijdsvenster dat wordt opgelegd door de tijdslot**.



#### Waarom zijn wachttorens nodig?



Het boetemechanisme werkt alleen als de benadeelde partij daartoe in staat is:




- controleert elk nieuw Bitcoin blok om te zien of een kanaal commitment transaction gepubliceerd is;
- bepalen of deze transactie overeenkomt met de laatste geldige status of met een herroepen status;
- in het geval van een herroepen status, om de legale transactie op tijd uit te zenden, waarbij de herroepingssleutel wordt gebruikt om alle fondsen terug te krijgen voordat de tijdslot verloopt.



![Image](assets/fr/023.webp)



In een ideaal scenario is je Lightning-node 24/7 online, is het gesynchroniseerd en controleert het continu de blockchain. Daarom kan het in zijn eentje een poging tot valsspelen detecteren en reageren. In de praktijk kan een persoonlijke Lightning-node echter uitvallen, vooral in het geval van een langdurige stroomstoring of een storing in de internetverbinding.



Juist tijdens deze periodes van downtime wordt het risico echt: als een oneerlijke peer een oude status publiceert terwijl jouw node offline is en de tijdslot verloopt zonder dat jij reageert, dan wordt het valsspelen effectief. Je verliest sommige of al je fondsen in het kanaal.



Watchtower's werden geïntroduceerd om dit risico te verminderen. Een wachttoren is een externe dienst die namens u de blockchain bewaakt, scant op de mogelijke publicatie van een oude status op een van uw kanalen en, indien nodig, automatisch de straftransactie namens u uitzendt. Dus zelfs als je Lightning node offline blijft voor een langere periode, zolang de wachttoren die je gebruikt operationeel is, zal het in staat zijn om je fondsen te beschermen door het monitoren van eventuele valsspeel pogingen en het toepassen van de bijbehorende straf, zodra het er een detecteert.



#### Hoe een wachttoren werkt



Een uitkijktoren is ontworpen om de informatie die het over je kanalen te weten komt tot een minimum te beperken, terwijl het de middelen heeft om te handelen in het geval van een probleem:




- Voor elke nieuwe kanaalstatus met een peer bereidt je node van tevoren een potentiële straftransactie voor. In het geval dat deze peer vals speelt, zou deze transactie je in staat stellen om al het geld in het kanaal terug te krijgen;
- Je knooppunt versleutelt dan deze straftransactie met behulp van de TXID van de corresponderende commitment transaction (degene die gebruikt zou worden als de bedrieger een poging tot bedrog zou doen). Zolang er geen afsluiting plaatsvindt, kan de wachttoren deze transactie niet ontsleutelen, omdat hij de TXID van de frauduleuze transactie niet volledig kent;
- Je knooppunt stuurt de wachttoren een pakket dat de versleutelde straftransactie en de helft van de TXID van de potentiële valsspeeltransactie bevat.



Aangezien de TXID die naar de wachttoren is verzonden onvolledig is, kan het de justitietransactie niet ontsleutelen. Het kan echter de blockchain controleren op een TXID die overeenkomt met het deel dat het bezit. Als het zo'n transactie detecteert, probeert het vervolgens de volledige TXID van die transactie te gebruiken om je straftransactie te decoderen. Als de ontcijfering slaagt, weet het dat het een valsspeel poging is en publiceert het onmiddellijk de straftransactie voor jou.



![Image](assets/fr/024.webp)



De wachttoren heeft daarom geen zicht op de details van je kanalen: noch de identiteit van je peers, noch de saldi, noch de structuur van de transacties. Het ziet alleen versleutelde pakketten. De enige informatie die het kan afleiden is de snelheid waarmee je kanalen worden bijgewerkt, aangezien het een pakket ontvangt voor elke nieuwe status, maar niet in staat is om de inhoud te kennen. In het geval van valsspelen, zal het zeker de kanaalinformatie ontdekken door de straftransactie te ontsleutelen, maar in ieder geval zal je sats gered worden.



Dit mechanisme is gebaseerd op een compromis: je delegeert de mogelijkheid om een vooraf ondertekende boete-transactie te publiceren aan de wachttoren, maar deze transactie blijft volledig ondoorzichtig voor de wachttoren totdat er bedrog plaatsvindt. De wachttoren kan noch de ontvangers wijzigen, noch de fondsen omleiden, aangezien het enkel een transactie heeft die al ondertekend is, met de uitvoerkanalen bevroren in jouw voordeel. Het kan ook niet de details weten van een kanaal in een legitieme gedwongen of coöperatieve afsluiting, omdat de TXID's niet overeenkomen. Aan de andere kant blijft Watchtower een minimaal vertrouwde derde partij: je moet erop vertrouwen dat het online is en dat het je rechtvaardigheidstransactie op de juiste manier uitzendt wanneer je het nodig hebt.



#### Een wachttoren worden



In theorie kan elk Lightning knooppunt fungeren als een wachttoren voor andere knooppunten (als ze dezelfde implementatie gebruiken, bijvoorbeeld LND), terwijl het zelf beschermd wordt door andere knooppunten die deze rol voor hem spelen. In de volgende praktische secties laat ik zien hoe je dit eenvoudige mechanisme op je LND onder Umbrel kunt instellen.


Daarom zou het een interessante strategie kunnen zijn om met betrouwbare bitcoiner-vrienden af te spreken om als elkaars uitkijkpost op te treden. Jij bewaakt hun kanalen en zij de jouwe.



### Zoek een altruïstische wachttoren



Als je niemand in je omgeving kent die een wachttorendienst kan aanbieden, zijn er een aantal altruïstische openbare wachttorens waarmee je verbinding kunt maken. In deze LNP202 cursus bijvoorbeeld, stel ik voor dat je verbinding maakt met de wachttorendienst die gezamenlijk wordt aangeboden door LN+ en Voltage, wat een wachttoren is voor LND.


Hier heb je de inloggegevens:



- Via Tor:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



- Via clearnet:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@34.216.52.158:9911
```

Om hen te bedanken voor het leveren van deze gratis wachttorenservice, [kun je een donatie doen via Lightning](https://lightningnetwork.plus/donation).


Nu we een altruïstische wachttorendienst gebruiken, laten we eens kijken hoe we die kunnen configureren op ons LND knooppunt onder Umbrel.


### Een wachttoren opzetten


Klik in de `Lightning Node`-toepassing op de drie puntjes rechtsboven in de interface en selecteer vervolgens `Geavanceerde instellingen`.


![Image](assets/fr/025.webp)


Ga dan naar het `Watchtower` menu.


![Image](assets/fr/026.webp)



Activeer de optie `Watchtower Client` en klik dan op de knop `SAVE AND RESTART NODE`. Wacht tot LND opnieuw is opgestart.


![Image](assets/fr/027.webp)


Zodra de herstart is voltooid, ga je terug naar hetzelfde menu en voer je de ID van de altruïstische wachttoren van je keuze in het daarvoor bestemde veld in. Klik dan op de `ADD` knop om te bevestigen. Je kunt ook de parameter `Watchtower Client Sweep Fee Rate` aanpassen: dit is de vergoeding die je bereid bent te betalen voor een mogelijke rechtvaardigheidstransactie die door de wachttoren wordt uitgezonden. Het is niet nodig om een te hoog tarief te kiezen, maar je moet ook een te laag tarief vermijden, anders wordt de rechtshandeling niet op tijd bevestigd.


Start je node opnieuw op met de knop `SAVE AND RESTART NODE` om deze wijzigingen toe te passen.


![Image](assets/fr/028.webp)



Als je terugkeert naar ditzelfde menu, zie je dat je Lightning-knooppunt nu wordt beschermd door de wachttoren die je zojuist hebt toegevoegd.



![Image](assets/fr/029.webp)



Een altruïstische wachttoren is over het algemeen voldoende, vooral als je geen grote bedragen op je Lightning-knooppunt zet en als je je knooppunt goed beheert (laat hem niet te lang uit staan). Voor nog meer veiligheid kun je er ook meerdere toevoegen door hetzelfde proces te herhalen.



## Open je eerste Lightning-kanaal


<chapterId>00642af7-8f3d-4a25-96d7-34e85de7bd5d</chapterId>



Als je zover bent gekomen, weet je al dat een Lightning-knooppunt zonder kanaal een beetje is als een lege wallet: het bestaat, maar is nutteloos. Om betalingen te kunnen verzenden of ontvangen, moet je node via een kanaal verbonden zijn met minstens één ander node in het Lightning-netwerk. In de toekomst raden we sterk aan om meerdere kanalen te openen, om redenen van veerkracht en routeringsefficiëntie. In de volgende hoofdstukken bekijken we ook hoe u uw liquide middelen beheert, uw kanaal topologie optimaliseert en meer geavanceerde tools gebruikt dan de basis LND interface op Umbrel.



Maar in dit inleidende hoofdstuk is het gewoon de bedoeling om te begrijpen hoe je een goede Lightning-peer kiest, waar je de informatie vindt die je nodig hebt om je peers te selecteren en tenslotte hoe je je eerste kanaal opent via de basis interface van LND.



### Hoe kies je een goede Lightning peer?



Wanneer je een kanaal opent, moet je een peer kiezen: een ander Lightning-knooppunt waarmee je knooppunt direct verbonden zal zijn via een kanaal. De keuze van deze peer is belangrijk, omdat het een directe invloed heeft op:




- het gemak waarmee je betalingen hun weg vinden;
- de betrouwbaarheid van je kanalen na verloop van tijd;
- uw routeringskosten.



Er bestaat niet zoiets als een perfecte match voor iedereen, maar er zijn een aantal betrouwbare criteria om goede kandidaten te identificeren.



#### 1. Knooppuntconnectiviteit



Een goede peer is een knooppunt dat goed verbonden is met het Lightning-netwerk. Dit betekent niet alleen een groot aantal kanalen hebben (hoewel dit een indicator kan zijn), maar vooral verbonden zijn met andere betrouwbare knooppunten en een voldoende centrale positie innemen in de netwerkgrafiek.



Een goed verbonden knooppunt verhoogt je kansen om een efficiënte route te vinden naar de meeste betalingsbestemmingen. Er zijn ook minder tussenliggende knooppunten nodig, wat de kosten drukt.



Omgekeerd kan het openen van je eerste kanaal naar een geïsoleerd of zwak verbonden knooppunt je mogelijkheden beperken: je kunt deze peer wel betalen, maar het zal veel moeilijker zijn om de rest van het netwerk te betalen.



#### 2. Kapitalisatie en kanaalcapaciteit



Een goede peer is ook een voldoende gekapitaliseerd knooppunt. Dit kun je zien aan de totale kanaalcapaciteit (de som van sats gecommitteerd aan al zijn kanalen) en de gemiddelde kanaalcapaciteit (het is vaak beter om maar een paar goed gekapitaliseerde kanalen te hebben dan veel kleine).



Een node met een belachelijke capaciteit, of waarvan alle kanalen piepklein zijn, zal niet in staat zijn om betalingen met grote bedragen te routeren, wat resulteert in falende routering voor jou.



#### 3. Onkostenbeleid



Elk knooppunt bepaalt zijn eigen routeringskosten (`basiskosten` en `tarief`). Een goede peer zal geen exorbitante fees vragen voor strategische kanalen. Voor een eerste kanaal kun je het beste een node kiezen met gematigde tarieven, om je eigen betalingen niet te belemmeren.



Vergeet niet dat je eigen routeringskosten ook invloed hebben op hoe anderen je zien als een peer: een knooppunt dat voortdurend zijn kosten wijzigt of absurde kosten oplegt, wordt zelden gewaardeerd.



#### 4. Stabiliteit en anciënniteit



Peer stabiliteit is een heel belangrijk criterium. Een goede node heeft een hoge uptime (is zelden offline), houdt zijn kanalen lang open en opent/sluit niet constant kanalen zonder reden.



Oude en nog steeds actieve kanalen zijn een goed signaal: ze suggereren dat de relatie winstgevend is voor de peer, dat het knooppunt weet hoe het zijn kapitaal moet beheren en dat het niet op elk moment wordt gesloten, zodat je niet steeds onchain fees hoeft te betalen voor het sluiten en heropenen.



Omgekeerd kan een collega die vaak offline is, of die snel kanalen sluit, een bron van problemen voor je zijn, en van extra kosten voor het openen van nieuwe kanalen.



Zelfs met deze criteria zul je niet meteen een perfecte keuze maken. Dat is normaal: de echte kwaliteit van een peer wordt onthuld door het gebruik ervan. Het is dus belangrijk om:




- de kanaalactiviteit monitoren (gerouteerde volumes, beschikbaarheid, enz.);
- sluit kanalen die geen doel dienen of waarvan de peers te vaak offline zijn;
- heralloceer je kapitaal na verloop van tijd naar betere peers.



Het idee is niet om elke dag kanalen te openen en te sluiten (wat duur zou zijn in onchain kosten), maar om geleidelijk je topologie te laten convergeren naar een verzameling betrouwbare, goed verbonden peers die compatibel zijn met je behoeften.



### Hoe vind ik een leeftijdsgenoot?



Om deze criteria toe te passen, heb je tools nodig die het Lightning-netwerk zichtbaar maken. Er zijn verschillende verkenners en diensten beschikbaar om dit te doen. De bekendste Lightning-verkenners zijn [1ML](https://1ml.com/) en [Amboss](https://amboss.space/).



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017

https://planb.academy/tutorials/node/lightning-network/1ml-37ada2ab-7a24-4473-87fd-007cb7640e7b

Hier raad ik je echter aan om [de Lightning Terminal tool van Lightning Labs](https://terminal.lightning.engineering/) te gebruiken, die een rangschikking geeft (weliswaar gebaseerd op deels subjectieve criteria) van de Lightning-knooppunten die het meest relevant worden geacht voor het openen van een kanaal.



![Image](assets/fr/030.webp)



Het probleem met de zeer grote Lightning-knooppunten bovenaan deze ranglijst is dat de meeste geen kanaalopeningen accepteren onder zeer hoge bedragen. Velen hanteren ook een strikt peer management beleid, wat ertoe kan leiden dat je kanaal wordt gesloten. Aan de andere kant hebben deze knooppunten over het algemeen geen behoefte aan inkomende liquiditeit, gezien hun aantal verbindingen.



Ik raad je daarom aan om naar beneden te werken in de ranglijst om een knooppunt te vinden dat goed verbonden, betrouwbaar en voldoende centraal in de netwerkgrafiek is, zonder buitensporig groot te zijn. Hier heb ik bijvoorbeeld het knooppunt Lightning op stacker.news geïdentificeerd, dat zeer goed verbonden is, een hoge capaciteit heeft en een centrale positie inneemt in de netwerkgrafiek.



![Image](assets/fr/031.webp)



Een andere interessante benadering is om een kanaal te openen naar een knooppunt dat inkomende liquiditeit nodig heeft, zoals een handelaar die je kent, een vereniging of een gemeenschap. Deze strategie heeft drie voordelen:




- Aangezien de gekozen entiteit inkomende liquiditeit nodig heeft, zal deze logischerwijs minder geneigd zijn om jouw kanaal zonder reden te sluiten;
- Zijn economische activiteit verhoogt de kans op routering via dit kanaal en dus op het innen van bepaalde vergoedingen;
- Je doet het ecosysteem een plezier en levert een waardevolle bijdrage aan andere bitcoiners.



Als je eenmaal een relevant knooppunt hebt geïdentificeerd, kun je zijn knooppunt-ID ophalen. Dit is simpelweg een aaneenschakeling van de publieke sleutel van het knooppunt, een `@` scheidingsteken, het IP- of Tor-adres en de gebruikte poort. Deze ID is eenvoudig toegankelijk via het profiel van het knooppunt in elke Lightning-verkenner.



### Open je eerste kanaal via LND



Nu we de node hebben geïdentificeerd waarmee we ons eerste kanaal openen, moeten we sats erop laten aansluiten. Om dit te doen, moet je Bitcoin onchain wallet koppelen aan je LND.



In de hoofdinterface van LND, zoek je `Bitcoin Wallet`, klik dan op de `Stort` knop. Een onchain ontvangstadres is dan generated: stuur sats daarheen. De hoeveelheid die je moet overmaken hangt af van de capaciteit die je wilt toewijzen aan je eerste kanaal, maar houd er rekening mee dat je iets meer moet sturen dan de beoogde capaciteit. Als je bijvoorbeeld een kanaal van 500.000 sats wilt openen, stuur dan niet precies 500.000 sats, maar een hogere hoeveelheid.



![Image](assets/fr/032.webp)



Zodra de transactie is uitgezonden, verschijnt deze in de interface. Wacht op bevestiging voordat je de chatroom opent. Je ziet een groene pijl naast de transactie wanneer deze is bevestigd.



![Image](assets/fr/033.webp)



Scroll naar beneden naar de hoofdinterface en klik vervolgens op `+ OPEN CHANNEL`.



![Image](assets/fr/034.webp)



Voer de `Node ID` in van de node waarmee u een kanaal wilt openen, geef het bedrag aan dat u wilt vastzetten en pas vervolgens de kosten voor de openingstransactie aan volgens de stand van de onchain fee markt. Zorg er natuurlijk wel voor dat je van tevoren voldoende geld in je LND onchain portefeuille hebt.



Zodra alle parameters zijn ingesteld, klik je op de knop `OPEN CHANNEL`.



![Image](assets/fr/035.webp)



Wacht tot de openingstransactie onchain is bevestigd. Je eerste kanaal is nu officieel operationeel: gefeliciteerd!



Je kunt zien dat op dit moment 100% van de liquiditeit van het kanaal aan mijn kant zit: dat is normaal, want ik ben degene die het kanaal heeft geopend. Naarmate betalingen en routing evolueren, zal deze verdeling veranderen, maar de totale capaciteit van het kanaal zal altijd hetzelfde blijven.



![Image](assets/fr/036.webp)



Nu je een kanaal hebt, kun je je eerste Lightning-betalingen doen, op voorwaarde dat het gekozen knooppunt goed verbonden is met het netwerk. Natuurlijk zullen we in latere hoofdstukken bekijken hoe je een handigere methode instelt om Lightning-facturen vanaf je mobiel te betalen. Maar voor nu proberen we een eerste betaling rechtstreeks van LND naar Umbrel.



Om dit te doen, klik je in de `Lightning Wallet` sectie op de `Verstuur` knop en plak je de factuur die ingesteld moet worden.



![Image](assets/fr/037.webp)



Het factuurbedrag wordt weergegeven. Bevestig de betaling door op de knop `Verstuur` te klikken.



![Image](assets/fr/038.webp)



Als er een geldige route is gevonden, zou je eerste Lightning-betaling succesvol moeten zijn.



![Image](assets/fr/039.webp)



Als we dan kijken naar de verdeling van liquiditeit in het kanaal, zien we dat mijn gelijke nu 5.002 sats aan zijn kant heeft. Dit komt overeen met de 5.000 sats van de betaling die ik zojuist heb gedaan en die hij heeft doorgestuurd naar het knooppunt van de ontvanger. De extra 2 sats vertegenwoordigen de routeringskosten die ik heb betaald, omdat de ontvanger precies 5.000 sats heeft ontvangen.



![Image](assets/fr/040.webp)



Om de betrouwbaarheid van onze betalingen te verbeteren, zullen we natuurlijk andere kanalen moeten openen. Afhankelijk van onze doelstellingen zullen we ook een manier moeten vinden om inkomende liquiditeit beschikbaar te maken, zodat we betalingen op Lightning kunnen ontvangen. Dit is het onderwerp van de volgende paragraaf.



# Uw Lightning-knooppunt beheren


<partId>e27c3e1e-487b-4414-ad6b-d67bdb91c7c5</partId>



## Je knooppuntoperatorprofiel definiëren


<chapterId>d3b2e163-50f6-4d1d-a5fc-8fd177dfac76</chapterId>



Nu uw Lightning-node draait, is de volgende stap het definiëren van uw handelsprofiel. Dit is een belangrijke keuze, want het bepaalt uw strategie voor het openen van kanalen, het type peers waaraan u de voorkeur geeft en de manier waarop u liquiditeit beheert.



Op Lightning heb je liquiditeit in de juiste richting nodig om dit te laten werken. Uitgaande liquiditeit komt overeen met uw vermogen om te betalen (sats beschikbaar aan uw kant van de kanalen). Inkomende liquiditeit komt overeen met uw vermogen om te ontvangen (sats beschikbaar aan de kant van uw peers). Met andere woorden, je profiel komt neer op een eenvoudige vraag: verlaat je sats meestal je knooppunt of komt het binnen?



### De consument



Dit is het profiel van de overgrote meerderheid van de gebruikers. Je gebruikt je node om Lightning-betalingen te doen: om goederen en diensten te kopen, rekeningen te betalen, fooien te sturen - kortom, om Lightning te gebruiken als een snel betaalmiddel. Aan de andere kant ontvangt u weinig of slechts marginaal van Lightning, bijvoorbeeld een paar donaties, terugbetalingen tussen vrienden of een paar microbetalingen.



Dit profiel is het gemakkelijkst te beheren, omdat je belangrijkste behoefte is om te kunnen betalen. Praktisch gezien betekent dit dat je uitgaande liquiditeit nodig hebt. Zodra je één of meer kanalen van de juiste grootte hebt geopend naar stabiele, goed verbonden knooppunten, zullen je uitgaande betalingen automatisch liquiditeit verplaatsen naar de andere kant van je kanalen. Het is precies deze beweging die op natuurlijke wijze een redelijke hoeveelheid inkomende liquiditeit creëert. Als gevolg hiervan zul je, zelfs als je niet op regelmatige basis wilt ontvangen, toch van tijd tot tijd kunnen ontvangen zonder een complexe strategie te implementeren. Je hoeft je dus geen zorgen te maken over je inkomende liquiditeit.



In deze LNP202 cursus gaan we ons richten op dit "consumenten" node operator profiel, omdat dit overeenkomt met bijna alle Bitcoin gebruikers op Lightning.



### De winkelier



De handelaar is in zekere zin het tegenovergestelde van de consument. Hier is het hoofddoel niet om te betalen, maar om te innen. Een bedrijf, dienstverlener, online winkel of verkooppunt dat Lightning accepteert, zal veel inkomende betalingen ontvangen en relatief weinig uitgaande betalingen doen vanaf dit knooppunt.



Dit profiel is veeleisender, omdat een geweigerde betaling op Lightning mogelijk een verloren verkoop betekent. De prioriteit wordt daarom inkomende liquiditeit. Als je node niet genoeg inkomende liquiditeit heeft, zullen je klanten zien dat hun betalingen mislukken, zelfs als ze het geld hebben, simpelweg omdat er geen route is om de liquiditeit in de juiste richting naar je toe te krijgen.



De grootste uitdaging voor de handelaar komt ook voort uit de natuurlijke evolutie van kanalen. Als je alleen maar ontvangt, zullen je kanalen zich geleidelijk aan aan jouw kant vullen. Je hebt dus mechanismen nodig om je inkomende liquiditeit te onderhouden en te vernieuwen.



Er is echter een eenvoudiger geval: het gemengde consumer/merchant-profiel. Als u verzamelt op Lightning, maar ook uitgeeft op Lightning (zakelijke uitgaven, betalingen aan leveranciers of zelfs persoonlijke uitgaven), dan vormen uw uitgaande betalingen op natuurlijke wijze een nieuwe inkomende stroom. Het beheer wordt soepeler, omdat de stromen elkaar compenseren en u minder uw toevlucht hoeft te nemen tot kunstmatige mechanismen die alleen zijn ontworpen om inkomende liquiditeit terug te winnen.



### De router



De router is een specifiek profiel. Het gebruikt zijn Lightning-knooppunt niet om te betalen of te innen, maar om de betalingen van anderen te routeren en vergoedingen te innen. Het doel is om een nuttige, betrouwbare en economisch concurrerende route te zijn binnen de Lightning-grafiek.



Om eerlijk te zijn, een router zijn op Lightning is complexer dan het lijkt en winstgevendheid is moeilijk te bereiken. Ten eerste is het openen en sluiten van kanalen duur in ketenkosten. Om efficiënt te routeren, moet je vaak je topologie aanpassen, testen, slecht presterende kanalen sluiten, nieuwe openen en regelmatig je liquiditeit opnieuw in evenwicht brengen. Ten tweede is de concurrentie hevig: grote, gevestigde knooppunten nemen van nature een groot deel van het verkeer voor hun rekening en het is moeilijk om voet aan de grond te krijgen zonder veel kapitaal vast te leggen in grote kanalen.



Er zijn ook hoge operationele eisen. Een routeringsknooppunt moet extreem stabiel zijn, bewaakt worden, een goede back-up hebben en rigoureus beheerd worden. Je moet de kanaalprestaties in de gaten houden, je vergoedingsbeleid aanpassen, een gebalanceerde liquiditeit handhaven, peers beheren en technische problemen snel oplossen. Dit niveau van betrokkenheid kan interessant zijn als technische hobby of als bijdrage aan de infrastructuur, maar als het je doel is om Lightning op een soevereine manier te gebruiken, is het zelden relevant om aan routing te doen om geld te verdienen. Daarom gaat deze LNP202 cursus niet dieper in op dit profiel.



### Jezelf duidelijk situeren voordat je verder gaat



Als je in het consumentenprofiel past, is je prioriteit om betrouwbaar te kunnen betalen met eenvoudig beheer. Als je een handelaar bent, is je prioriteit om te kunnen cashen zonder falen, wat een strategie impliceert om inkomende liquiditeit te verwerven. Als je routing overweegt, moet je het benaderen als een veeleisende, economisch onzekere en tijdrovende activiteit.



Door dit profiel nu te definiëren, kunt u een klassieke valkuil vermijden: een kanaalstrategie toepassen die is ontworpen voor een handelaar of router, terwijl u gewoon een gebruiker bent die wil betalen.



## Een Lightning-knooppuntmanager gebruiken


<chapterId>02eb4c09-d14b-4ff0-8b04-b90de3307d34</chapterId>



In het vorige deel van deze LNP202 training gebruikten we de basisinterface van de `Lightning Node` toepassing op Umbrel. Deze interface is voldoende voor essentiële operaties (saldi controleren, geldverdeling bekijken, kanalen openen en sluiten), maar is opzettelijk erg vereenvoudigd. Deze eenvoud beperkt de beschikbare opties en geeft geen toegang tot veel van de geavanceerde functies van uw LND knooppunt. Daarom gebruiken we nu een andere, uitgebreidere Lightning node management software.



Deze extra software is gewoon een aanvullende beheerinterface voor je node. Dit betekent dat je de `Lightning Node` interface parallel kunt blijven gebruiken, en zelfs verschillende als je dat wilt. Dit zijn gewoon verschillende manieren van interactie met hetzelfde Lightning knooppunt.



Enkele van de bekendste softwareprogramma's zijn:




- [Alby Hub](https://albyhub.com/);
- [Ride The Lightning](https://www.ridethelightning.info/);
- [ThunderHub](https://thunderhub.io/).



Alle drie zijn goede oplossingen. Als je wilt, kun je ze alle drie testen met je node voordat je degene kiest die het beste bij je past. Persoonlijk gebruik ik ThunderHub uit gewoonte en omdat het completer lijkt dan de anderen. Dit is de tool die ik in deze training presenteer, maar je kunt ook een van de andere twee alternatieven kiezen. Voor elk van deze programma's hebben we een specifieke tutorial op Plan ₿ Academy.



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

### ThunderHub installeren



Deze programma's kunnen allemaal heel eenvoudig worden geïnstalleerd vanuit de Umbrel App Store. Zoals ik al zei, gebruiken we hier ThunderHub, maar als je later een andere wilt testen, is de procedure vergelijkbaar.



![Image](assets/fr/041.webp)



Umbrel geeft u een standaardwachtwoord voor toegang tot ThunderHub. Kopieer het: je hebt het meteen nodig. Vergeet niet om het op te slaan in je wachtwoordmanager, want je zult er elke keer om gevraagd worden als je de software opent.



![Image](assets/fr/042.webp)



Klik op `Login` en plak het wachtwoord dat door Umbrel is verstrekt om in te loggen.



![Image](assets/fr/043.webp)



Je komt dan op de ThunderHub startpagina, die de belangrijkste informatie over je Lightning-knooppunt weergeeft.



![Image](assets/fr/044.webp)



Om te beginnen raad ik je aan om twee-factor authenticatie (2FA) te activeren. Klik in de instellingen gewoon op `Enable` naast `Enable 2FA` en volg dan het gebruikelijke proces.



![Image](assets/fr/045.webp)



### Gebruik ThunderHub



ThunderHub is relatief eenvoudig te leren. Alle menu's zijn toegankelijk via de linkerkolom van de interface. Samengevat is dit wat elk menu doet:




- home: knooppuntenoverzicht, balansen en snelle acties;
- dashboard: aanpasbaar dashboard met widgets en statistieken;
- peers: verbindingen met andere Lightning-nodes bekijken en beheren;
- kanalen': volledig kanaalbeheer (liquiditeit, vergoedingen, afsluiting, enz.);
- rebalance": een tool voor het herbalanceren van kanalen via circulaire betalingen;
- transacties: geschiedenis van verzonden en ontvangen Lightning-betalingen;
- forwards`: routeringsstatistieken en kosten generated door uw knooppunt;
- chain': Bitcoin onchain portefeuille (UTXOs en transacties);
- gW-201 integratie voor bewaking en back-up;
- `Tools`: geavanceerde tools (back-ups, rapporten, macarons, handtekeningen, etc.);
- ruil: Lightning/onchain swaps via Boltz;
- statistieken: algemene statistieken en prestaties van je Lightning-knooppunt.



Met deze set functies heb je alle tools in handen om je Lightning-node efficiënt te beheren. Het is niet essentieel om elke optie meteen in detail te beheersen: we zullen ze in de loop van deze cursus geleidelijk verkennen. Als je de software echter diepgaander wilt leren kennen, bekijk dan onze ThunderHub tutorial:



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

Het menu waarin we hier het meest geïnteresseerd zijn is `Kanalen`. Het biedt een gedetailleerd overzicht van alle kanalen in je knooppunt, met hun liquiditeitsverdeling. In het bijzonder kun je zien welke kanalen open zijn in `Open`, welke wachten om geopend of gesloten te worden in `Pending`, en welke al gesloten zijn in `Closed`.



![Image](assets/fr/047.webp)



Voor een gegeven kanaal kun je op de naam of het kanaal-ID van de peer klikken om de Amboss pagina te openen en meer informatie te krijgen. Je kunt ook op het potloodpictogram klikken om de parameters van de chatroom aan te passen, inclusief het vergoedingenbeleid dat op die chatroom wordt toegepast als je knooppunt betalingen doorstuurt naar het knooppunt van je peer.



![Image](assets/fr/048.webp)



Als je je Lightning-node voornamelijk als "consument" gebruikt, hoef je deze kosten niet aan te passen: je kunt de standaardwaarden behouden. Aan de andere kant, als je beter wilt begrijpen hoe routeringskosten werken op Lightning, raad ik LNP 201 training aan, en in het bijzonder hoofdstuk 4.1:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Door op het kruisje naast een leeftijdsgenoot te klikken, kun je een kanaal sluiten. Als je bijvoorbeeld merkt dat een leeftijdsgenoot regelmatig inactief is, kan het gepast zijn om dit kanaal te sluiten om je kapitaal toe te wijzen aan een betrouwbaardere leeftijdsgenoot.



Je hebt dan twee opties. De eerste, en altijd te verkiezen, is coöperatief sluiten. Door deze actie te bevestigen, vraagt je node aan je gelijke om het kanaal gezamenlijk te sluiten. Als hij accepteert, kunt u de onchain sluitingstransactie uitzenden en uw deel van het geld terugkrijgen. De voordelen van deze methode zijn dat je de onchain kosten voor de transactie kiest, waardoor je onnodige kosten vermijdt, en dat het geld sneller wordt teruggevorderd, zonder tijdslot.



![Image](assets/fr/049.webp)



De tweede optie is gedwongen afsluiting. In dit geval vraag je de peer niet om toestemming en zend je direct de laatste commitment transaction uit die je in je bezit hebt. Ik zou deze methode niet aanraden tenzij het een laatste redmiddel is, bijvoorbeeld als de peer systematisch coöperatieve afsluitingen weigert of niet meer reageert. Gedwongen afsluiting heeft twee grote nadelen: de vergoedingen zijn vaak erg hoog, omdat ze van tevoren zijn ingesteld om te anticiperen op een stijging van de onchain vergoedingen, en er is een vertraging in het terugkrijgen van de fondsen, omdat ze worden geblokkeerd door een tijdslot. Dit tijdslot geeft je peer de tijd om te reageren in het geval van een poging tot valsspelen (wat hier natuurlijk niet het geval is, maar je moet nog steeds wachten).



![Image](assets/fr/050.webp)



Om een nieuw kanaal te openen, ga je naar het `Home` menu en klik je op `Open a Channel` in de `Liquidity` sectie. Je kunt dan het ID van het gekozen knooppunt, de kanaalcapaciteit, de gewenste Lightning-routeringskosten en de onchainkosten voor de openingstransactie invoeren.



![Image](assets/fr/051.webp)



Dit zijn de belangrijkste handelingen die u moet uitvoeren op ThunderHub. We zullen gaandeweg deze LNP202 cursus andere functies ontdekken.



## Het verkrijgen van inkomende liquiditeit


<chapterId>b740c656-a897-4d95-af4b-116b718447cd</chapterId>



Zoals je kunt zien, is het hebben van uitgaande liquiditeit om betalingen te doen op Lightning niet bijzonder ingewikkeld. Open gewoon op eigen initiatief kanalen naar andere knooppunten en begin sats te versturen. Aan de andere kant is het hebben van inkomende liquiditeit om betalingen op Lightning te ontvangen ingewikkelder, omdat je ofwel andere knooppunten nodig hebt om kanalen voor je te openen, of je moet de liquiditeit zelf verplaatsen door betalingen te doen.



Als je een "consumenten"-profiel aanneemt, hoef je je over het algemeen geen zorgen te maken over inkomende liquiditeit. Uw gebruik van het Lightning-knooppunt zal voornamelijk gericht zijn op betalingen, in plaats van cash-in. Door simpelweg een paar Lightning-betalingen te doen, creëer je na verloop van tijd vanzelf inkomende liquiditeit.



Aan de andere kant, als je een "merchant" profiel hebt, is de situatie omgekeerd: je zult voornamelijk betalingen innen en er maar weinig doen. Je kunt dus niet alleen vertrouwen op je eigen betalingen voor inkomende liquiditeit. Daarom is het noodzakelijk dat andere Lightning-knooppunten kanalen openen naar die van jou. Maar hoe kan dat? Hoe zorg je ervoor dat andere operators kapitaal voor je vastleggen? Dat is precies wat we in dit hoofdstuk zullen onderzoeken.



### Inkomende liquiditeit kopen



Zoals je zou verwachten, is de meest effectieve manier om iemand te laten handelen hem te betalen. Voor inkomende liquiditeit naar je Lightning-knooppunt is het principe precies hetzelfde. De eenvoudigste manier om kanalen naar je knooppunt te krijgen is door te betalen voor de dienst en het kapitaal dat ermee gemoeid is.



Als je een bedrijf of detailhandelaar bent, betekent deze aanpak dat je snel betrouwbare kanalen kunt verkrijgen om zonder wrijving betalingen van je klanten te innen.



Er zijn veel manieren om inkomende liquiditeit te kopen. Degene die ik persoonlijk gebruik en aanbeveel is Amboss's [Magma](https://magma.amboss.tech/) platform. Het is heel gemakkelijk te gebruiken, het openen van een kanaal gaat snel en de tarieven zijn over het algemeen redelijk. Magma werkt als een marktplaats met makers en nemers, maar versie 2 heeft de ervaring sterk vereenvoudigd: maak gewoon een aanvraag aan, betaal de prijs via Lightning en Magma matcht automatisch met het beste beschikbare aanbod. Na zes onchain bevestigingen is je kanaal met inkomende liquiditeit klaar. Zo werkt het:



Ga naar [de Magma website](https://magma.amboss.tech/buy), naar de `Koop Kanalen` sectie.



![Image](assets/fr/052.webp)



Als u wilt, kunt u een account aanmaken om uw aankopen te volgen, maar dit is niet verplicht. Als u geen account aanmaakt, zal Magma u simpelweg een sessie-ID geven waarmee u uw aankopen op een later tijdstip kunt terugvinden.



Vul op de site de informatie in die nodig is om liquiditeiten te kopen. Selecteer `Eenmalig` voor een eenmalige aankoop en voer dan het bedrag in dat je bereid bent te betalen voor inkomende liquiditeit. Hoe hoger het betaalde bedrag, hoe groter de capaciteit van het kanaal dat voor jouw node wordt geopend. Hieronder zie je een schatting van de capaciteit van het kanaal: dit is een benadering, omdat het uiteindelijke bedrag afhangt van het beste aanbod dat Magma heeft gevonden, en dat is soms hoger, soms lager.



![Image](assets/fr/053.webp)



Voer dan je knooppunt-ID in. Je kunt het bijvoorbeeld vinden in het `Node ID` menu van de `Lightning Node` toepassing op Umbrel.



![Image](assets/fr/054.webp)



Zodra alle informatie is ingevuld, klikt u op de knop `Bekijken & bestelling openen`.



![Image](assets/fr/055.webp)



Als u nog geen account heeft aangemaakt, krijgt u van Magma een sessiesleutel en een back-upbestand. Bewaar deze twee items op een veilige plek, want hiermee kunt u de bestelling op een later tijdstip ophalen of de status ervan volgen in het geval van een probleem. Zodra u het bestand hebt opgeslagen, klikt u op de knop `Betalen met Lightning`.



![Image](assets/fr/056.webp)



Magma stuurt dan een Lightning-factuur voor het bedrag dat je hebt gekozen. Die moet je betalen. Als je al kanalen op je Lightning-knooppunt hebt, kun je direct vanaf dat knooppunt betalen, of een andere externe Lightning wallet gebruiken.



![Image](assets/fr/057.webp)



Zodra de betaling is verricht, wordt de transactie als verwerkt weergegeven in de Magma-interface.



![Image](assets/fr/058.webp)



Na een paar minuten wordt het verzoek verwerkt: er wordt een kanaal met sats geopend naar uw Lightning-node. Zodra de openingstransactie onchain is bevestigd, heb je toegang tot de bijbehorende inkomende liquiditeit.



![Image](assets/fr/059.webp)



Magma is ook direct geïntegreerd in ThunderHub. Scroll in de `Home` tab naar beneden naar de `Liquidity` sectie en klik op `Koop Inkomende Liquidity`. U hoeft alleen het gewenste bedrag in te voeren en te bevestigen. U hoeft geen facturen handmatig te betalen, want ThunderHub zorgt automatisch voor de betaling vanaf uw knooppunt.



![Image](assets/fr/060.webp)



Als je een handelaar bent, is dit type dienst bijzonder geschikt, omdat het je in staat stelt om snel een grote hoeveelheid inkomende liquiditeit te verkrijgen van betrouwbare knooppunten, zodat je klanten je zonder problemen kunnen betalen. Aan de andere kant, als je een privépersoon bent, of als je niet wilt betalen voor inkomende liquiditeit, zijn er ook gratis oplossingen. Laten we eens kijken.



### Coöperatieve inkomende liquiditeit



Als je geen handelaar bent, maar toch wat inkomende liquiditeit nodig hebt (bijvoorbeeld om je node op te starten terwijl je wacht op betalingen), dan hoef je daar niet per se voor te betalen. Een van mijn voorkeursoplossingen is om samen te werken met andere nodebeheerders die ook inkomende liquiditeit nodig hebben, om Lightning-kanalen voor elkaar te openen. Op deze manier brengt het openen van een kanaal u uitgaande liquiditeit, terwijl het u tegelijkertijd voorziet van inkomende liquiditeit, gratis (modulo onchain kosten voor het openen).



Je kunt dit natuurlijk rechtstreeks met mede-bitcoiners regelen. Er is echter een platform speciaal voor dit soort circulaire openingen: [Lightning Network +](https://lightningnetwork.plus/). Het principe is niet om twee kanalen te openen tussen dezelfde mensen, maar om circulaire openingen op te zetten met minimaal drie deelnemers, of zelfs meer.



Laten we een voorbeeld nemen om te begrijpen hoe Lightning Network + werkt:




- Een node operator, genaamd `A`, publiceert een aankondiging waarin staat dat hij een 1 miljoen sats kanaal wil openen met twee andere mensen;
- De advertentie blijft actief tot er nieuwe deelnemers worden toegevoegd;
- Later voegen twee operators, `B` en `C`, zich bij de aankondiging van het `A` knooppunt. De driehoek is nu compleet en de openingsfase kan beginnen.
- Knooppunt `A` opent een kanaal naar knooppunt `B`;
- Knooppunt `B` opent een kanaal naar knooppunt `C`;
- Knooppunt `C` opent een kanaal naar knooppunt `A`.



Aan het einde van de transactie heeft elk knooppunt 1 miljoen sats aan uitgaande liquiditeit en 1 miljoen sats aan inkomende liquiditeit. Deze regeling kan worden uitgebreid tot vier of vijf deelnemers.



Natuurlijk is er geen technisch mechanisme om te garanderen dat een deelnemer het kanaal dat hij heeft toegezegd ook daadwerkelijk opent. Daarom heeft het platform een reputatiesysteem opgezet, gebaseerd op positieve beoordelingen als operators hun toezeggingen nakomen. En in het ergste geval, als je iemand tegenkomt die niet meewerkt, heb je geen geld verloren: je hebt gewoon een kans op binnenkomende liquiditeit gemist.



Deze oplossing is met name geschikt voor een "consumenten" profiel, omdat het je in staat stelt om gratis inkomende liquiditeit te verkrijgen, terwijl je je knooppunt verbindt met andere kleine operators. Aan de andere kant, als je een handelaar bent, is deze aanpak over het algemeen niet relevant: elke sat van inkomende liquiditeit vereist het blokkeren van een sat van uitgaande liquiditeit, en je grote behoefte aan inkomende liquiditeit zou dan betekenen dat je te veel kapitaal vastlegt.



Om Lightning Network + te gebruiken, heb je twee opties: ofwel gebruik je de toepassing die geïntegreerd is in Umbrel, ofwel gebruik je de klassieke website en maak je een account aan door in te loggen vanaf je knooppunt. Ik raad het laatste aan, omdat de geïntegreerde toepassing niet alle beschikbare functies biedt.



Ga naar de [Lightning Network +](https://lightningnetwork.plus/) website en klik op de `Login` knop rechtsboven in de interface.



![Image](assets/fr/061.webp)



Om jezelf te authenticeren, moet je het verstrekte bericht ondertekenen met de privésleutel van je Lightning-knooppunt. Met ThunderHub is dit heel eenvoudig. Kopieer eerst het bericht dat LN+ weergeeft.



![Image](assets/fr/062.webp)



Ga in ThunderHub naar het tabblad `Tools` en klik dan op de knop `Tekenen` in de sectie `Messages`.



![Image](assets/fr/063.webp)



Plak het authenticatiebericht van LN+ en klik op `Teken`.



![Image](assets/fr/064.webp)



ThunderHub ondertekent dit bericht dan met de private sleutel van jouw knooppunt. Kopieer de generated handtekening.



![Image](assets/fr/065.webp)



Plak deze handtekening in het corresponderende veld op de LN+ site en klik dan op `Aanmelden`.



![Image](assets/fr/066.webp)



U bent nu verbonden met LN+ met uw Lightning-knooppunt. Dit proces stelt LN+ in staat om te verifiëren dat u de rechtmatige eigenaar bent van het knooppunt dat u claimt op hun platform.



![Image](assets/fr/067.webp)



Als je wilt, kun je je LN+ profiel personaliseren, bijvoorbeeld door een korte biografie toe te voegen.



Om deel te nemen aan je eerste ronde kanaalopening ga je naar het `Swaps` menu bovenaan de interface. Hier vind je alle swaps die momenteel beschikbaar zijn, afhankelijk van de eigenschappen van je knooppunt.



![Image](assets/fr/068.webp)



Om deel te nemen aan een bestaande ruilaanbieding, klik je er gewoon op en registreer je. Op LN+ kan de maker van een ruil echter bepaalde voorwaarden stellen aan deelnemers, zoals een minimum aantal kanalen of een minimum totale knooppuntcapaciteit. Het is daarom mogelijk, vooral in het begin, dat er weinig aanbiedingen beschikbaar zijn voor jouw node. In mijn geval waren er, ondanks dat er al een paar kanalen open waren, geen aanbiedingen beschikbaar voor mijn knooppunt. Dus heb ik mijn eigen swap gemaakt en jij kunt hetzelfde doen als je in dezelfde situatie zit.



Klik op `Start Liquidity Swap` en voer vervolgens je aanbiedingsparameters in:




- Kies het totale aantal deelnemers (3, 4 of 5);
- Geef het aantal te openen kanalen aan (zorg ervoor dat je minstens dit aantal in je wallet-ketting hebt);
- Bepaal de open tijd van het kanaal. Dit is de periode waarin deelnemers afspreken om het kanaal niet te sluiten;
- Aan de rechterkant kun je beperkingen instellen voor deelnemers: minimaal aantal kanalen, minimale totale capaciteit en type verbinding dat wordt geaccepteerd.



Zodra alle parameters zijn ingesteld, klik je op de knop `Start Liquidity Swap`.



![Image](assets/fr/069.webp)



Je ruilaanbod is nu aangemaakt. Nu hoef je alleen nog maar te wachten tot andere knooppuntbeheerders zich aanmelden. Als je voorwaarden niet te beperkend zijn, zou dit niet al te lang moeten duren. Vergeet niet om de status van je ruil in de gaten te houden in de uren of dagen die volgen.



![Image](assets/fr/070.webp)



Alle wisselplaatsen zijn bezet: we gaan nu verder met de fase van kanaalopening. Elke deelnemer kan op zijn LN+ interface zien naar welk knooppunt hij een Lightning-kanaal moet openen.



![Image](assets/fr/084.webp)



Aan jouw kant open je het kanaal met de Node ID die LN+ je geeft en respecteer je de aangegeven hoeveelheid. Zoals we in eerdere hoofdstukken hebben gezien, kun je dit doen via ThunderHub, met een andere Lightning-knooppuntmanager of rechtstreeks vanuit de basisinterface van de Lightning-knooppunttoepassing.



![Image](assets/fr/085.webp)



Zodra de opening is gestart, zie je het verschijnen in de wachtende kanalen sectie. In mijn geval is dat het kanaal met het knooppunt `Plebian_fr`.



![Image](assets/fr/086.webp)



U kunt dan terugkeren naar LN+ om te bevestigen dat u de kanaalopening hebt gestart. Klik gewoon op de knop `Kanaal openen gestart`.



![Image](assets/fr/087.webp)



Wanneer alle andere deelnemers ook het kanaal hebben geopend waaraan ze zich hebben gecommitteerd, vergeet dan niet om een positieve recensie achter te laten.



![Image](assets/fr/088.webp)



Bij problemen of vertragingen kun je rechtstreeks contact opnemen met je collega's via het commentaargedeelte onderaan de pagina.



![Image](assets/fr/089.webp)



Sommige deelnemers willen de circulaire kanalen vanaf het begin opnieuw in evenwicht brengen door een betaling aan zichzelf te doen. Dit zorgt voor een evenwichtige verdeling van contant geld in elk kanaal. Als je in een "consumenten" profiel zit, is dit niet essentieel, maar je kunt deze herbalancering zelf doen als je dat wilt, of tijdelijk je kanaalkosten op nul zetten om het makkelijker te maken voor de gelijke die het wil doen. Soms wil niemand het doen.



![Image](assets/fr/090.webp)




# Het potentieel van uw Lightning-knooppunt benutten


<partId>8dcc24b1-6eb9-4a5f-a56b-8a823e5ac0fd</partId>



## Verbind een mobiele wallet via Tailscale


<chapterId>5fefb222-3f50-4f9d-a170-2ea628be4437</chapterId>



Dat is het, je hebt nu een goed verbonden Lightning-knooppunt, met zowel inkomende als uitgaande liquiditeit. Je bent dus helemaal klaar om je Lightning-knooppunt in het echte leven te gebruiken. Tot nu toe gebruikten we altijd interfaces direct op Umbrel, ofwel de `Lightning Node` applicatie of de `ThunderHub` interface. Deze tools werken voor het verzenden en ontvangen van betalingen, maar zijn duidelijk niet geoptimaliseerd voor alledaagse Lightning-betalingen. De interface is ontworpen voor gebruik op een computer, onpraktisch op een smartphone, en vereist ook een verbinding met hetzelfde netwerk om goed te functioneren (hoewel het technisch mogelijk is om op afstand verbinding te maken via Tor).



In de praktijk zijn we als bitcoiners op zoek naar een klassieke Lightning wallet interface op een smartphone: de mogelijkheid om facturen te scannen via QR codes, en een eenvoudige interface voor het betalen en uitbetalen van sats. Dit is precies wat we in dit hoofdstuk en het volgende zullen implementeren. Het algemene idee is om een mobiele Lightning wallet applicatie op je smartphone te hebben, die overal gebruikt kan worden (niet alleen op je lokale netwerk), maar die op de achtergrond vertrouwt op je eigen Lightning node om betalingen te versturen en te ontvangen.



### Wat zijn de oplossingen om een mobiele klant aan te sluiten?



Tegenwoordig zijn er verschillende manieren om dit te doen, zowel wat betreft de mobiele applicatie als het type verbinding tussen je node en deze applicatie. De drie belangrijkste verbindingsmodi zijn:




- via ***Tor***;
- via VPN ***Tailscale***;
- via ***Nostr Wallet Connect***.



Een paar jaar geleden maakte ik verbinding via ***Tor***, maar daar ben ik al snel mee gestopt: het aantal storingen en de communicatievertragingen waren veel te groot. In theorie werkt het, maar in de praktijk was de gebruikerservaring rampzalig. Ik raad deze aanpak dan ook af.



Het alternatief dat ik toen koos was om een ***Tailscale*** VPN te gebruiken om de communicatie tussen de mobiele applicatie en het knooppunt te garanderen. Deze oplossing werkt erg goed: zelfs op mobiele netwerken met een lage doorvoer, komen mijn betalingen altijd zonder problemen door. Dit is de methode die ik als eerste in dit hoofdstuk ga introduceren, met de Zeus applicatie.



In het volgende hoofdstuk bekijken we een andere, meer recente oplossing, die ook erg goed werkt: ***Nostr Wallet Connect***. Deze keer gebruiken we de Alby Go toepassing om je een alternatief te presenteren, hoewel Zeus ook compatibel is met NWC als je dat wilt.



### Tailscale installeren en configureren



Voor deze eerste methode hebben we Tailscale nodig. Dit is een VPN-oplossing gebaseerd op WireGuard, waarmee je apparaten verspreid over het internet veilig met elkaar kunt verbinden, terwijl encryptie, authenticatie en NAT traversal automatisch beheerd worden. Simpel gezegd is het alsof al je apparaten verbonden zijn met hetzelfde LAN als je router, ook al kunnen ze zich overal op het internet bevinden.



Om het te gebruiken, moet je eerst een account aanmaken. Ga naar de Tailscale website en klik op de `Get Started` knop.



![Image](assets/fr/071.webp)



Kies dan een identiteitsprovider voor je Tailscale account. Persoonlijk gebruikte ik een van mijn GitHub accounts om in te loggen.



![Image](assets/fr/072.webp)



Zodra je bent ingelogd, worden je een paar vragen gesteld over je gebruik. Beantwoord ze kort om verder te gaan.



![Image](assets/fr/073.webp)



Tailscale biedt dan aan om een client op je machine te installeren. Daar zijn we nu niet in geïnteresseerd: ga direct naar Umbrel en installeer de Tailscale applicatie uit de App Store.



![Image](assets/fr/074.webp)



Wanneer de applicatie opent, klikt u op `Log In` en volgt u het verificatieproces, waarbij u dezelfde methode gebruikt als bij het aanmaken van uw account.



![Image](assets/fr/075.webp)



Klik op `Connect` om te bevestigen. Uw Umbrel is nu verbonden met uw VPN-netwerk.



![Image](assets/fr/076.webp)



Download vervolgens de Tailscale-applicatie op je smartphone en log in met hetzelfde account. Let op: op Android is het niet mogelijk om twee VPN's tegelijkertijd te gebruiken. Om Tailscale te laten werken, moet je elke andere actieve VPN uitschakelen. Bovendien, elke keer dat je je Lightning-node via Zeus wilt gebruiken, moet je de Tailscale VPN activeren, anders wordt de verbinding niet tot stand gebracht.



![Image](assets/fr/077.webp)



Op de Tailscale site, nu er tenminste twee clients verbonden zijn, kunt u de beheerconsole openen met een lijst van alle apparaten die verbonden zijn met het netwerk en hun Tailscale IP-adressen.



![Image](assets/fr/078.webp)



### Verbind Zeus



Installeer de Zeus-toepassing op uw telefoon. Wanneer het opent, selecteer dan `Geavanceerde instellingen` en vervolgens `Een wallet maken of aansluiten`.



![Image](assets/fr/079.webp)



Kies `LND (REST)` in het gedeelte `Wallet interface`. Voer vervolgens het Tailscale adres van uw Umbrel in, welke u kunt vinden op uw Tailscale dashboard of direct in de Tailscale applicatie op Umbrel. Voer voor de poort `8080` in.



![Image](assets/fr/080.webp)



Zeus vraagt je dan om een `Macaroon`. Dit is een token autorisatie waarmee je precies kunt definiëren welke rechten een applicatie (in dit geval Zeus) heeft om te communiceren met je Lightning knooppunt. Het is mogelijk om generate een macaron te maken vanuit ThunderHub, in het `Tools` menu, `Bakery` submenu, maar voor dit doel is de makkelijkste manier om het direct vanuit de `Lightning Node` applicatie op te halen.



Klik op de drie kleine puntjes rechtsboven in de interface en vervolgens op `Connect Wallet`. Kies `REST (Lokaal Netwerk)`. Je kunt dan een macaron kopiëren met de juiste rechten.



![Image](assets/fr/081.webp)



Plak het in het overeenkomstige veld in Zeus en klik dan op de knop `SAVE WALLET CONFIG`.



![Image](assets/fr/082.webp)



Je hebt nu toegang tot je Lightning-knooppunt vanuit de Zeus-app. Dit betekent dat je generate facturen direct op je Lightning-node kunt ontvangen vanaf je smartphone, en ook Lightning-facturen kunt betalen waar je ook bent.



![Image](assets/fr/083.webp)



Tip: Tailscale is niet beperkt tot het op afstand gebruiken van uw Lightning-node. Het geeft u toegang tot alle tools van uw Umbrel vanuit andere software, zelfs op afstand. Je kunt bijvoorbeeld het Tailscale IP-adres van je Umbrel gebruiken om je Bitcoin node (via Electrs of Fulcrum) te verbinden met Sparrow Wallet, zonder via Tor te gaan. Nogmaals, dit vermijdt de traagheid die inherent is aan Tor. Installeer gewoon de Tailscale client op je computer en verbind hem met je netwerk.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

In het volgende hoofdstuk bekijken we een andere, even effectieve manier om een mobiele client met je Lightning-node te verbinden: Nostr Wallet Connect. We gebruiken een andere toepassing dan Zeus (hoewel Zeus ook compatibel is met NWC), namelijk Alby Go.



## Verbind een mobiele wallet via NWC


<chapterId>f5c97e43-e66e-4ba3-bcc9-fee1a04fc7f4</chapterId>



Als je niet overtuigd bent door de Tailscale verbinding, of als het beheren van een dubbel VPN te veel gedoe lijkt, dan stelt dit hoofdstuk een andere manier voor om een mobiele client op afstand te gebruiken om sats te betalen en te ontvangen via je Lightning knooppunt: ***Nostr Wallet aansluiten***.



Voor dit voorbeeld gebruiken we de Alby Go mobiele toepassing, die zeer goed ontworpen is en bijzonder eenvoudig te leren. Je kunt echter ook Zeus of een andere mobiele applicatie die compatibel is met NWC gebruiken. Je vindt een lijst met compatibele toepassingen op [de `awesome-nwc` GitHub repository] (https://github.com/getAlby/awesome-nwc).



### Hoe werkt Nostr Wallet Connect?



Nostr Wallet Connect is een gestandaardiseerd protocol waarmee een toepassing of website acties kan activeren op een Lightning-knooppunt op afstand, zonder een directe netwerkverbinding met dat knooppunt tot stand te brengen (geen API LND blootgesteld, geen VPN, geen `.onion`-service...). NWC definieert hoe een toepassing een intentie formuleert (bijvoorbeeld `betaal_factuur`) en het resultaat ontvangt.



Het werkt heel eenvoudig. Je initialiseert een sessie door een QR-code te scannen of via een deeplink `nostr+walletconnect:`. Deze string bevat de sessieparameters en een autorisatiegeheim. Wanneer de applicatie vervolgens wil betalen, serialiseert het de aanvraag, versleutelt het en publiceert het als een gebeurtenis op een Nostr relais. Het knooppunt leest de gebeurtenis op het relais, ontcijfert het, controleert of de autorisator geautoriseerd is voor deze sessie, voert de betaling uit en stuurt vervolgens een versleuteld antwoord terug (succes met preimage of fout). Het relais fungeert alleen als een transport tussenpersoon: het kan de inhoud niet lezen, maar het kan wel de timing en frequentie van verzoeken observeren.



Vergeleken met een verbinding via Tailscale of Tor is het belangrijkste voordeel van NWC dat je knooppunt niet direct van buitenaf bereikbaar is. Dit vereenvoudigt mobiel gebruik enorm: je knooppunt hoeft geen inkomende verbindingen te accepteren, het hoeft alleen maar te kunnen communiceren met een relais. Aan de andere kant introduceer je een functionele afhankelijkheid van Nostr relais: als ze niet beschikbaar zijn, verslechtert de ervaring. En zelfs als berichten versleuteld zijn, kan het relais een bepaald niveau van activiteitsmetadata waarnemen.



Het verschil in beveiligingsmodellen is ook belangrijk. Met Tailscale of Tor geef je directe toegang tot je knooppunt (via API of LND) beschermd door zeer gevoelige geheimen. Dit is krachtig, omdat je alles kunt beheren, maar het is ook een aanvalsoppervlak van een lagere laag. Met NWC is toegang meer toepasselijk: je delegeert een sessie token die alleen bepaalde acties autoriseert.



### Installeer Alby Hub op uw Lightning-knooppunt



Voorheen was er een applicatie speciaal voor NWC-verbindingen in de Umbrel App Store, maar deze is helaas niet langer beschikbaar. U zult nu Alby Hub moeten gebruiken om dit type verbinding tot stand te brengen. Om dit te doen, installeert u eerst de Alby Hub-toepassing rechtstreeks vanuit de Store.



![Image](assets/fr/091.webp)



Sla bij het openen de introductieschermen over en klik dan op de `Get Started (LND)` knop. Het is belangrijk om te controleren of er tussen haakjes `LND` staat en niet `LDK`. Als `LND` verschijnt, betekent dit dat Alby Hub het bestaande Lightning knooppunt correct heeft gedetecteerd en zichzelf zal configureren als de interface ervoor. Aan de andere kant, als `LDK` wordt weergegeven, betekent dit dat Alby Hub uw knooppunt niet heeft gedetecteerd en op het punt staat een nieuw knooppunt aan te maken, wat hier niet de bedoeling is.



![Image](assets/fr/092.webp)



U wordt dan gevraagd om een Alby account aan te maken. Voor gebruik dat beperkt is tot NWC, is dit niet nodig, maar u wilt dit misschien wel doen als u gebruik wilt maken van de specifieke diensten van Alby. Zo niet, klik dan op `Misschien later` om verder te gaan.



![Image](assets/fr/093.webp)



Kies vervolgens een sterk, uniek wachtwoord. Dit beschermt de toegang tot Alby Hub op jouw knooppunt. Vergeet niet om het op te slaan in je wachtwoordmanager.



![Image](assets/fr/094.webp)



Dit brengt je naar de Alby Hub interface. Je hoeft niet het hele configuratieproces te doorlopen, tenzij je het wilt gebruiken als de hoofdbeheerder van je Lightning knooppunt. Zoals we eerder zagen, kan Alby Hub in feite het gebruik van ThunderHub voor het beheer van je node vervangen. Als je meer wilt weten over de mogelijkheden van Alby Hub, bekijk dan onze speciale tutorial:



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Ga naar het menu `Connections`.



![Image](assets/fr/095.webp)



Hier zie je alle toepassingen die via NWC verbinding kunnen maken met je Lightning-node. Hiertoe behoort ook Zeus, dat al in het vorige hoofdstuk werd genoemd. Hier gebruiken we Alby Go. Klik op Alby Go en vervolgens op de knop `Connect to Alby Go` om het verbindingsproces te starten.



![Image](assets/fr/096.webp)



### Alby Go installeren en aansluiten



Installeer de Alby Go-toepassing op uw smartphone:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Apple App Store](https://apps.apple.com/us/app/alby-go/id6471335774);
- [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq3jhml5fvklgnq9fxpete767txn9zfzqdkc0sxfptmnchfrexje7qqfxxmmd9enk2arpd338jtndda3xjmr9pzj5tk).



Configureer in Alby Hub de rechten die u wilt toekennen aan de Alby Go-toepassing op uw Lightning-knooppunt. U kunt bijvoorbeeld uitgavenlimieten per periode instellen, een vervaldatum voor de NWC-koppeling, of de volledige controle overlaten. Zodra u de parameters hebt ingesteld, klikt u op de knop `Volgende`.



![Image](assets/fr/097.webp)



Alby Hub generates dan een QR-code om de NWC-verbinding tussen je Lightning-knooppunt en Alby Go tot stand te brengen.



![Image](assets/fr/098.webp)



Klik op de Alby Go-toepassing, wanneer deze voor het eerst wordt geopend, op `Garage-382 aansluiten` en scan vervolgens de QR-code die door Alby Hub wordt geleverd.



![Image](assets/fr/099.webp)



Kies een naam om deze wallet te identificeren. Je hebt nu op afstand toegang tot je Lightning-knooppunt via Alby Go. Je kunt generate facturen ontvangen sats op je knooppunt, of Lightning facturen er direct mee instellen.



![Image](assets/fr/100.webp)



Ik stuurde bijvoorbeeld 1543 sats vanaf de Alby Go interface.



![Image](assets/fr/101.webp)



Als ik naar de basisinterface van mijn Lightning-knooppunt op Umbrel ga, kan ik zien dat deze betaling inderdaad door mijn knooppunt is gedaan.



![Image](assets/fr/102.webp)



Nu weet je hoe je je Lightning-node gemakkelijk vanaf elke plek kunt gebruiken.



## Langdurige autonomie op Lightning


<chapterId>691a0942-b46d-482a-8fbc-fe19b3814992</chapterId>



We zijn nu aan het einde gekomen van deze LNP202 hands-on cursus. Je hebt nu de basis die je nodig hebt om Lightning Network soeverein te gebruiken: je begrijpt de echte rol van een node, de afwegingen van verschillende benaderingen, en je hebt een LND instantie op Umbrel opgezet met een consistente back-up en beschermingsstrategie. Je hebt ook je eerste kanalen geopend, geleerd hoe je liquiditeit beheert en je betalingen dagelijks betrouwbaar maakt.



Vanuit operationeel oogpunt zou je node nu in een onderhoudsritme moeten komen. Het belangrijkste is om het in de gaten te houden (uptime, synchronisatie, kanaalstatus, betalingsproblemen, etc.), de updates toe te passen die Umbrel aanbiedt als er stabiele versies beschikbaar zijn, en regelmatig te controleren of je back-ups en wachttorenconfiguratie nog actief zijn.



Als het op kanalen aankomt, kies dan voor een pragmatische aanpak: houd de kanalen die nuttig voor je zijn, sluit de kanalen die permanent inactief zijn of geassocieerd worden met onstabiele peers en heralloceer geleidelijk je kapitaal naar een robuustere topologie.



**Een van de meest voorkomende valkuilen in dit stadium is het toewijzen van te veel kapitaal aan je Lightning node. Houd er rekening mee dat je Lightning node veel minder veilig is dan een hardware wallet, en dat de beschikbaarheid van fondsen die zijn toegewezen aan je kanalen afhankelijk is van back-up mechanismen die onvolmaakt blijven. Het is daarom erg belangrijk om redelijke bedragen aan te houden, die je je kunt veroorloven te verliezen in het geval van een probleem, en altijd het grootste deel van je sats op een onchain hardware wallet te houden.



Wat tools betreft, raad ik je aan om nieuwsgierig en aandachtig te blijven naar nieuwe ontwikkelingen. In deze trainingssessie hebben we er verschillende ontdekt, of het nu gaat om het beheer van je knooppunt, de connectiviteit ervan of het gebruik op afstand om betalingen te doen. Lightning is echter een bijzonder dynamisch veld. Elk jaar duiken er nieuwe en relevante tools op, en ook op Umbrel verschijnen er veel nieuwe toepassingen. Als je op de hoogte blijft van deze nieuwe ontwikkelingen, ontdek je misschien krachtigere of praktischer oplossingen dan die in deze cursus.



Als je het nog niet gedaan hebt, raad ik je ten zeerste aan om de LNP 201 theoriecursus van Fanis Michalakis te volgen, die gewijd is aan de werking van de Lightning Network. Het zal je helpen om de manipulaties in deze LNP202 cursus beter te begrijpen en je meer vertrouwen geven in het dagelijkse beheer van je node. Het zal je helpen de manipulaties in deze LNP202 cursus beter te begrijpen en je meer vertrouwen geven in het dagelijkse beheer van je knooppunt.



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

In een andere trant, maar net zo essentieel voor je bitcoinreis, raad ik ook de uitstekende cursus van Ludovic Lars aan over de geschiedenis van de creatie van Bitcoin.



https://planb.academy/courses/a51c7ceb-e079-4ac3-bf69-6700b985a082

Maar voordat je verder gaat, kun je een beoordeling schrijven over deze LNP202 cursus en natuurlijk het diploma halen om te bevestigen dat je de volledige inhoud hebt begrepen.



# Laatste deel


<partId>683c998f-ba0a-4ffb-a7e8-4cd8369cb9b3</partId>



## Beoordelingen


<chapterId>aec048c7-7130-425d-8eca-9cd7f90c27f3</chapterId>



<isCourseReview>true</isCourseReview>

## Eindexamen


<chapterId>3951ccbb-14a3-4322-b81b-8dd2a6da19cb</chapterId>



<isCourseExam>true</isCourseExam>

## Conclusie


<chapterId>30cd6309-5139-40d9-8927-92de0f76414a</chapterId>



<isCourseConclusion>true</isCourseConclusion>