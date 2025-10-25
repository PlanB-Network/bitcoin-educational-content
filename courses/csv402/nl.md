---
name: RGB-programmering
goal: De vaardigheden verwerven die nodig zijn om RGB te begrijpen en te gebruiken
objectives:
- De fundamentele concepten van het RGB protocol begrijpen
- De principes van Client-side Validation en Bitcoin verplichtingen beheersen
- Leren hoe je RGB contracten aanmaakt, beheert en overdraagt
- Hoe een RGB-compatibel Lightning-knooppunt te bedienen
---
# Het RGB protocol ontdekken


Duik in de wereld van RGB, een protocol ontworpen om digitale rechten te implementeren en af te dwingen, in de vorm van contracten en activa, gebaseerd op de consensusregels en operaties van Bitcoin Blockchain. Deze uitgebreide training leidt je door de technische en praktische fundamenten van RGB, van de concepten van "Client-side Validation" en "Single-use Seals", tot de implementatie van geavanceerde slimme contracten.


Via een gestructureerd, stap-voor-stap programma ontdek je de mechanismen van Client-side Validation, deterministische verbintenissen op Bitcoin en interactiepatronen tussen gebruikers. Leer hoe je RGB tokens kunt maken, beheren en overdragen op Bitcoin of Lightning Network.


Of u nu een ontwikkelaar, Bitcoin enthousiasteling of gewoon nieuwsgierig bent om meer te leren over deze technologie, deze training geeft u de tools en kennis die u nodig heeft om RGB te beheersen en innovatieve oplossingen op Bitcoin te bouwen.


De cursus is gebaseerd op een live seminar georganiseerd door Fulgur'Ventures en gegeven door drie gerenommeerde docenten en RGB experts.


+++
# Inleiding


<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>


## Cursus presentatie


<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>


Hallo allemaal, en welkom bij deze training over RGB, een Smart contract systeem dat aan de clientzijde gevalideerd is en op Bitcoin en Lightning Network draait. De structuur van deze cursus is ontworpen om diepgaande verkenning van dit complexe onderwerp mogelijk te maken. Dit is hoe de cursus is georganiseerd:


**Deel 1: Theorie**


Het eerste deel is gewijd aan de theoretische concepten die nodig zijn om de grondbeginselen van Client-side Validation en RGB te begrijpen. Zoals je in deze cursus zult ontdekken, introduceert RGB een groot aantal technische concepten die gewoonlijk niet voorkomen in Bitcoin. In dit deel vind je ook een verklarende woordenlijst met definities van alle termen die specifiek zijn voor het RGB protocol.


**Deel 2: Praktijk**


Het tweede deel richt zich op de toepassing van de theoretische concepten uit deel 1. We leren hoe we RGB contracten kunnen maken en manipuleren. We zullen ook zien hoe je kunt programmeren met deze tools. Deze eerste twee secties worden gepresenteerd door Maxim Orlovsky.


**Sectie 3: Toepassingen**


Het laatste deel wordt geleid door andere sprekers die concrete toepassingen op basis van RGB presenteren, om zo praktijkvoorbeelden te belichten.


---
Deze training kwam oorspronkelijk voort uit een twee weken durend bootcamp voor geavanceerde ontwikkeling in Viareggio, Toscane, georganiseerd door [Fulgur'Ventures](https://fulgur.ventures/). De eerste week, gericht op Rust en SDK's, is te vinden in deze andere cursus:


https://planb.network/courses/9fbd8b57-f278-4304-8d88-a2d384eaff58

In deze cursus richten we ons op de tweede week van het bootcamp, waarin RGB centraal staat.


**Week 1 - LNP402:**


![RGB-Bitcoin](assets/en/001.webp)


**Week 2 - Huidige opleiding CSV402:**


![RGB-Bitcoin](assets/en/002.webp)


Hartelijk dank aan de organisatoren van deze live cursussen en aan de 3 docenten die hebben deelgenomen:




- Maxim Orlovsky: *Ex Tenebrae sententia sapiens dominabitur astris. Cypher, AI, robotica, transhumanisme. Schepper van RGB, Prime, Radiant en lnp_bp, mycitadel_io & cyphernet_io*;
- Jager Trujilo: *Ontwikkelaar, Rust, Bitcoin, Bliksem, RGB*;
- Federico Tenga: *Ik draag mijn steentje bij om de wereld te veranderen in een Cypherpunk dystopie. Werk momenteel aan RGB bij Bitfinex*.


De schriftelijke versie van deze training is opgesteld met behulp van 2 belangrijke bronnen:




- Video's van het seminar van Maxim Orlovsky, Hunter Trujilo en Frederico Tenga op Lightning Bootcamp;
- De RGB documentatie, waarvan de productie werd gesponsord door [Bitfinex](https://www.bitfinex.com/).


Klaar om in de complexe en fascinerende wereld van RGB te duiken? Laten we gaan!


# RGB in theorie


<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>


## Inleiding tot concepten van gedistribueerd computergebruik


<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>


:::video id=f27338bc-4210-4a2e-9b27-30278ed3282c:::


RGB is een protocol dat ontworpen is om digitale rechten (in de vorm van contracten en activa) toe te passen en af te dwingen op een schaalbare en vertrouwelijke manier, gebaseerd op de consensusregels en operaties van Bitcoin Blockchain. Het doel van dit eerste hoofdstuk is om de basisconcepten en terminologie rond het RGB protocol te presenteren, waarbij in het bijzonder de nauwe verbanden met basisconcepten voor gedistribueerd computergebruik zoals Client-side Validation en enkelvoudige zegels worden benadrukt.


In dit hoofdstuk verkennen we de grondbeginselen van **gedistribueerde consensus systemen** en kijken we hoe RGB in deze familie van technologieën past. We introduceren ook de belangrijkste principes die ons helpen te begrijpen waarom RGB uitbreidbaar en onafhankelijk wil zijn van Bitcoin's eigen consensus mechanisme, terwijl het erop vertrouwt wanneer dat nodig is.


### Inleiding


Distributed computing, een specifieke tak van computerwetenschap, bestudeert de protocollen die gebruikt worden om informatie te laten circuleren en verwerken op een netwerk van knooppunten. Samen vormen deze knooppunten en de protocolregels wat bekend staat als een gedistribueerd systeem. Enkele van de essentiële eigenschappen die een dergelijk systeem karakteriseren zijn:




- De **mogelijkheid tot onafhankelijke verificatie en validatie** van bepaalde gegevens door elk knooppunt;
- De mogelijkheid voor knooppunten om (afhankelijk van het protocol) een volledige of gedeeltelijke weergave van de informatie te construeren. Deze weergaven zijn de **staten** van het gedistribueerde systeem;
- De **chronologische volgorde** van bewerkingen, zodat gegevens betrouwbaar van een tijdstempel zijn voorzien en er een consensus is over de volgorde van gebeurtenissen (volgorde van toestanden).


Het begrip **consensus** in een gedistribueerd systeem omvat twee aspecten:




- Erkenning van de **geldigheid** van toestandsveranderingen (volgens protocolregels);
- De **overeenkomst over de volgorde** van deze toestandsveranderingen, die het onmogelijk maakt om achteraf gevalideerde operaties te herschrijven of terug te draaien (dit staat in Bitcoin ook bekend als "double-spend protection").


De eerste functionele, toestemmingsvrije implementatie van een gedistribueerd consensusmechanisme werd geïntroduceerd door Satoshi Nakamoto met Bitcoin, dankzij het gecombineerde gebruik van een Blockchain datastructuur en een Proof-of-Work (PoW) algoritme. In dit systeem hangt de geloofwaardigheid van de blokgeschiedenis af van de rekenkracht die de nodes (miners) eraan besteden. Bitcoin is daarom een belangrijk en historisch voorbeeld van een gedistribueerd consensus systeem dat open staat voor iedereen (*permissionless*).


In de wereld van Blockchain en distributed computing kunnen we twee fundamentele paradigma's onderscheiden: ***Blockchain*** in de traditionele zin, en ***state channels***, waarvan het beste voorbeeld in productie de Lightning Network is. Het Blockchain wordt gedefinieerd als een register van chronologisch geordende gebeurtenissen, gerepliceerd door consensus binnen een open, toestemmingsvrij netwerk. State channels, aan de andere kant, zijn peer-to-peer kanalen die twee (of meer) deelnemers in staat stellen om een bijgewerkte toestand off-chain te onderhouden, waarbij de Blockchain alleen gebruikt wordt bij het openen en sluiten van deze kanalen.


In de context van Bitcoin bent u ongetwijfeld bekend met de principes van Mining, decentralisatie en finaliteit van transacties op Blockchain en hoe betalingskanalen werken. Met RGB introduceren we een nieuw paradigma, genaamd **Client-side Validation**, dat, in tegenstelling tot Blockchain of Lightning, bestaat uit het lokaal (client-side) opslaan en valideren van de toestandsovergangen van een Smart contract. Dit verschilt ook van andere "Decentralisatie" systemen, zoals Blockchain en Lightning. Dit verschilt ook van andere "DeFi" technieken (_rollups_, _plasma_, _ARK_, etc.), waarbij de Client-side Validation vertrouwt op de Blockchain om Double-spending te voorkomen en om een tijdstempelsysteem te hebben, terwijl het register van off-chain toestanden en overgangen alleen bij de betreffende deelnemers blijft.


![RGB-Bitcoin](assets/en/003.webp)


Later zullen we ook een belangrijke term introduceren: het begrip "**Stash**", dat verwijst naar de set client-side gegevens die nodig zijn om de toestand van een Contract te bewaren, omdat deze gegevens niet wereldwijd over het netwerk worden gerepliceerd. Tenslotte bekijken we de grondgedachte achter RGB, een protocol dat voordeel haalt uit Client-side Validation, en waarom het een aanvulling is op bestaande benaderingen (Blockchain en toestandkanalen).


### Trilemma's in gedistribueerd computergebruik


Om te begrijpen hoe Client-side Validation en RGB Address problemen oplossen die Blockchain en Lightning niet oplossen, laten we 3 belangrijke "trilemma's" in gedistribueerd computergebruik ontdekken:




- **Schaalbaarheid, Decentralisatie, Privacy**;
- **CAP** Stelling (Consistentie, Beschikbaarheid, Partitietolerantie);
- **CIA** trilemma (Vertrouwelijkheid, Integriteit, Beschikbaarheid).


#### 1. Schaalbaarheid, decentralisatie en vertrouwelijkheid




- **Blockchain (Bitcoin)**


Blockchain is zeer gedecentraliseerd, maar niet erg schaalbaar. Bovendien, omdat alles in een globaal, publiek register staat, is de vertrouwelijkheid beperkt. We kunnen proberen de vertrouwelijkheid te verbeteren met zero-knowledge technologieën (Confidential Transactions, mimblewimble schema's, etc.), maar de publieke keten kan de transactiegrafiek niet verbergen.




- **Bliksem/staatskanalen**


Staatskanalen (zoals Lightning Network) zijn schaalbaarder en meer privé dan Blockchain, omdat transacties off-chain plaatsvinden. Echter, de verplichting om bepaalde Elements (financieringstransacties, netwerktopologie) openbaar te maken en het monitoren van netwerkverkeer kan de vertrouwelijkheid deels in gevaar brengen. Decentralisatie lijdt er ook onder: routing is geld-intensief, en grote knooppunten kunnen centralisatiepunten worden. Dit is precies het fenomeen dat we op Lightning beginnen te zien.




- **Client-side Validation (RGB)**


Dit nieuwe paradigma is nog schaalbaarder en vertrouwelijker, omdat we niet alleen zero-disclosure proof-of-knowledge technieken kunnen integreren, maar er is ook geen globale grafiek van transacties, omdat niemand het hele register bezit. Aan de andere kant impliceert het ook een zeker compromis over decentralisatie: de uitgever van een Smart contract kan een centrale rol hebben (zoals een "Contract deployer" in Ethereum). In tegenstelling tot Blockchain, worden bij Client-side Validation echter alleen de contracten waarin je geïnteresseerd bent opgeslagen en gevalideerd, wat de schaalbaarheid ten goede komt, omdat je niet alle bestaande toestanden hoeft te downloaden en te verifiëren.


![RGB-Bitcoin](assets/en/004.webp)


#### 2. CAP Stelling (Consistentie, Beschikbaarheid, Partitietolerantie)


De CAP stelling benadrukt dat het onmogelijk is voor een gedistribueerd systeem om gelijktijdig te voldoen aan *consistentie*,*beschikbaarheid* en *partitietolerantie*.




- **Blockchain**


De Blockchain is voorstander van consistentie en beschikbaarheid, maar doet het niet goed met netwerkpartitionering: als je een blok niet kunt zien, kun je niet handelen en hetzelfde zicht hebben als het hele netwerk.




- **Bliksem**


Een systeem van toestandskanalen heeft tolerantie voor beschikbaarheid en partitionering (omdat twee knooppunten met elkaar verbonden kunnen blijven, zelfs als het netwerk gefragmenteerd is), maar de algehele consistentie hangt af van het openen en sluiten van kanalen op de Blockchain.




- **Client-side Validation (RGB)**


Een systeem als RGB biedt consistentie (elke deelnemer valideert zijn gegevens lokaal, zonder dubbelzinnigheid) en partitioneringstolerantie (je bewaart je gegevens autonoom), maar garandeert geen wereldwijde beschikbaarheid (iedereen moet ervoor zorgen dat ze de relevante stukken geschiedenis hebben, en sommige deelnemers publiceren misschien niets of stoppen met het delen van bepaalde informatie).


![RGB-Bitcoin](assets/en/005.webp)


#### 3. CIA trilemma (Vertrouwelijkheid, Integriteit, Beschikbaarheid)


Dit trilemma herinnert ons eraan dat vertrouwelijkheid, integriteit en beschikbaarheid niet allemaal tegelijk geoptimaliseerd kunnen worden. Blockchain, Lightning en Client-side Validation vallen op verschillende manieren binnen deze balans. Het idee is dat geen enkel systeem alles kan bieden; het is nodig om verschillende benaderingen te combineren (Blockchain's tijdstempeling, Lightning's synchrone benadering, en lokale validatie met RGB) om een samenhangend pakket te krijgen dat goede garanties biedt in elke dimensie.


![RGB-Bitcoin](assets/en/006.webp)


### De rol van Blockchain en het begrip sharding


De Blockchain (in dit geval, Bitcoin) dient voornamelijk als een _time-stamping_ mechanisme en bescherming tegen dubbele uitgaven. In plaats van de volledige gegevens van een Smart contract of gedecentraliseerd systeem in te voegen, voegen we gewoon **cryptografische toezeggingen** aan transacties toe (in de zin van Client-side Validation, die we "toestandsovergangen" zullen noemen). Dus:




- We bevrijden de Blockchain van een grote hoeveelheid gegevens en logica;
- Elke gebruiker slaat alleen de geschiedenis op die nodig is voor zijn eigen deel van de Contract (zijn "*Shard*"), in plaats van de Global State te kopiëren.


Sharding is een concept dat zijn oorsprong vindt in gedistribueerde databases (bijv. MySQL voor sociale netwerken zoals Facebook of Twitter). Om het probleem van gegevensvolume en synchronisatievertragingen op te lossen, wordt de database gesegmenteerd in _shards_ (VS, Europa, Azië, enz.). Elk segment is lokaal consistent en wordt slechts gedeeltelijk gesynchroniseerd met de andere.


Voor RGB-type slimme contracten, gebruiken we Shard volgens de contracten zelf. Elke Contract is een onafhankelijke _shard_. Als je bijvoorbeeld alleen USDT tokens bezit, hoef je niet de hele geschiedenis van een andere token zoals USDC op te slaan of te valideren. Op Bitcoin doet de Blockchain niet aan _sharding_: je hebt een globale set UTXO's. Met Client-side Validation behoudt elke deelnemer alleen de Contract gegevens die hij bezit of gebruikt.


We kunnen ons het ecosysteem dus als volgt voorstellen:




- De **Blockchain (Bitcoin)** als basis die zorgt voor een volledige replicatie van een minimaal register en dient als tijdstempel Layer;
- De **Lightning Network** voor snel, Confidential Transactions, nog steeds gebaseerd op de zekerheid en definitieve regeling van de Bitcoin Blockchain;
- **RGB en Client-side Validation** om complexere Smart contract logica toe te voegen, zonder de Blockchain te vervuilen of vertrouwelijkheid te verliezen.


![RGB-Bitcoin](assets/en/007.webp)


Deze drie Elements vormen een driehoekig geheel, in plaats van een lineaire stapel van "Layer 2", "Layer 3" enzovoort. Lightning kan direct verbinding maken met Bitcoin, of geassocieerd worden met Bitcoin transacties die RGB gegevens bevatten. Op dezelfde manier kan een "BiFi" (financiering op Bitcoin) samenwerken met Blockchain, met Lightning en met RGB, afhankelijk van de behoefte aan vertrouwelijkheid, schaalbaarheid of Contract logica.


![RGB-Bitcoin](assets/en/008.webp)


### Het begrip toestandsovergangen


In elk gedistribueerd systeem is het doel van het validatiemechanisme om **de geldigheid en chronologische volgorde van toestandsveranderingen** te kunnen bepalen. Het doel is om te controleren of de protocolregels zijn nageleefd en om te bewijzen dat deze toestandsveranderingen elkaar opvolgen in een definitieve, onaantastbare volgorde.


Om te begrijpen hoe deze validatie werkt in de context van **Bitcoin** en, meer in het algemeen, om de filosofie achter Client-side Validation te begrijpen, laten we eerst eens terugkijken naar de mechanismen van Bitcoin Blockchain, voordat we zien hoe Client-side Validation daarvan verschilt en welke optimalisaties het mogelijk maakt.


![RGB-Bitcoin](assets/en/009.webp)


In het geval van de Bitcoin Blockchain is de transactievalidatie gebaseerd op een eenvoudige regel:




- Alle netwerkknooppunten downloaden elk blok en elke transactie;
- Ze valideren deze transacties om de correcte evolutie van de UTXO set (alle niet-uitgegeven uitgangen) te verifiëren;
- Ze slaan deze gegevens op (in de vorm van blokken) zodat de geschiedenis opnieuw kan worden afgespeeld als dat nodig is.


![RGB-Bitcoin](assets/en/010.webp)


Dit model heeft echter twee grote nadelen:




- **Schaalbaarheid**: omdat elk knooppunt ieders transacties moet verwerken, verifiëren en archiveren, is er een duidelijke limiet aan de transactiecapaciteit, met name gekoppeld aan de maximale blokgrootte (gemiddeld 1 MB over 10 minuten voor Bitcoin, exclusief cookies);
- **Privacy**: alles wordt openbaar uitgezonden en opgeslagen (bedragen, bestemmingsadressen, enz.), wat de vertrouwelijkheid van uitwisselingen beperkt.


![RGB-Bitcoin](assets/en/012.webp)


In de praktijk werkt dit model voor Bitcoin als basis Layer (Layer 1), maar het kan onvoldoende worden voor complexere toepassingen die tegelijkertijd een hoge transactiedoorvoer en een zekere mate van vertrouwelijkheid vereisen.


Client-side Validation is gebaseerd op het tegenovergestelde idee: in plaats van het hele netwerk te verplichten om alle transacties te valideren en op te slaan, zal elke deelnemer (cliënt) alleen het deel van de geschiedenis valideren dat hem of haar aangaat:




- Wanneer een persoon een goed (of een ander digitaal eigendom) ontvangt, hoeft hij alleen maar de keten van operaties (toestandsovergangen) die tot dat goed hebben geleid te kennen en te verifiëren en de legitimiteit ervan te bewijzen;
- Deze opeenvolging van operaties, van de ***Genesis*** (eerste uitgifte) tot de meest recente transactie, vormt een acyclische gerichte grafiek (DAG) of Shard, d.w.z. een fractie van de totale geschiedenis.


![RGB-Bitcoin](assets/en/013.webp)


Tegelijkertijd, zodat de rest van het netwerk (of meer precies, de onderliggende Layer, zoals Bitcoin) de uiteindelijke toestand kan vergrendelen zonder de details van deze gegevens te zien, vertrouwt Client-side Validation op het begrip ***Commitment***.


Een *Commitment* is een cryptografische Commitment, meestal een _hash_ (SHA-256 bijvoorbeeld) die wordt ingevoegd in een Bitcoin transactie, die bewijst dat er privégegevens zijn opgenomen, zonder deze gegevens te onthullen.


Dankzij deze _verbintenissen_ kunnen we bewijzen:




- Het bestaan van informatie (omdat het is vastgelegd in een Hash);
- De anterioriteit van deze informatie (omdat het is verankerd en van een tijdstempel voorzien in de Blockchain, met een datum en blokvolgorde).


De exacte inhoud wordt echter niet onthuld, zodat de vertrouwelijkheid behouden blijft.


Concreet werkt een RGB State Transition als volgt:




- U bereidt een nieuwe State Transition voor (bijv. de overdracht van een RGB token);
- Je generate een cryptografische Commitment aan deze overgang en voegt het in een Bitcoin transactie (deze verbintenissen worden "*anchors*" genoemd in het RGB protocol);
- De tegenpartij (de ontvanger) haalt de klantgeschiedenis op die aan dit activum is gekoppeld en valideert de end-to-end consistentie, van de Genesis van de Smart contract tot de transitie die je naar haar verzendt.


![RGB-Bitcoin](assets/en/014.webp)


Client-side Validation biedt twee belangrijke voordelen:




- **Schaalbaarheid:**


De *opdrachten* in de Blockchain zijn klein (in de orde van enkele tientallen bytes). Dit zorgt ervoor dat de blokruimte niet verzadigd raakt, omdat alleen de Hash opgenomen hoeft te worden. Het zorgt er ook voor dat het off-chain protocol kan evolueren, omdat elke gebruiker alleen zijn of haar geschiedenisfragment hoeft op te slaan (zijn of haar _stash_).




- **Privacy:**


Transacties zelf (d.w.z. hun gedetailleerde inhoud) worden niet gepubliceerd On-Chain. Alleen hun vingerafdrukken (*Hash*). Bedragen, adressen en Contract logica blijven dus privé en de ontvanger kan lokaal de geldigheid van zijn Shard controleren door alle voorgaande overgangen te inspecteren. Er is geen reden voor de ontvanger om deze gegevens openbaar te maken, behalve in geval van een geschil of wanneer bewijs nodig is.


In een systeem als RGB kunnen meerdere toestandsovergangen van verschillende contracten (of verschillende activa) worden samengevoegd in een enkele Bitcoin transactie via een enkele _commitment_. Dit mechanisme legt een deterministische, van een tijdstempel voorziene link tussen de On-Chain transactie en de off-chain gegevens (de door de klant gevalideerde overgangen), en maakt het mogelijk om meerdere shards tegelijkertijd op te nemen in een enkel Anchor punt, waardoor de On-Chain kosten en voetafdruk verder worden verminderd.


In de praktijk, wanneer deze Bitcoin transactie gevalideerd wordt, wordt de toestand van de onderliggende contracten permanent "vergrendeld", omdat het onmogelijk wordt om de Hash die al in de Blockchain staat te wijzigen.


![RGB-Bitcoin](assets/en/015.webp)


### Het Stash concept


Een **Stash** is de verzameling client-side gegevens die een deelnemer absoluut moet bewaren om de integriteit en geschiedenis van een RGB Smart contract te behouden. In tegenstelling tot een Lightning-kanaal, waar bepaalde toestanden lokaal gereconstrueerd kunnen worden uit gedeelde informatie, wordt de Stash van een RGB Contract niet elders gerepliceerd: als je hem verliest, zal niemand hem kunnen herstellen, omdat jij verantwoordelijk bent voor jouw deel van de geschiedenis. Daarom moet je in RGB een systeem met betrouwbare back-upprocedures gebruiken.


![RGB-Bitcoin](assets/en/016.webp)


### Single-Use Seal: ontstaan en werking


Bij het accepteren van een activum zoals een valuta zijn twee garanties essentieel:




- De authenticiteit van het ontvangen artikel;
- De uniciteit van het ontvangen artikel, om dubbele kosten te voorkomen.


Voor fysieke activa, zoals een bankbiljet, is fysieke aanwezigheid voldoende om te bewijzen dat het niet gedupliceerd is. In de digitale wereld, waar activa puur informatief zijn, is deze verificatie echter complexer, omdat informatie gemakkelijk kan worden vermenigvuldigd en gedupliceerd.


Zoals we eerder zagen, stelt de openbaring door de verzender van de geschiedenis van toestandsovergangen ons in staat om de authenticiteit van een RGB token te verzekeren. Door toegang te hebben tot alle transacties sinds de Genesis transactie, kunnen we de authenticiteit van de token bevestigen. Dit principe is vergelijkbaar met dat van Bitcoin, waar de geschiedenis van munten kan worden getraceerd naar het oorspronkelijke Coinbase Transaction om hun geldigheid te verifiëren. Maar, in tegenstelling tot Bitcoin, is deze geschiedenis van toestandsovergangen in RGB privé en wordt bewaard aan de cliëntzijde.


Om Double-spending van RGB tokens te voorkomen, gebruiken we een mechanisme genaamd "**Single-Use Seal**". Dit systeem zorgt ervoor dat elke token, eenmaal gebruikt, niet een tweede keer frauduleus hergebruikt kan worden.


Single-use Seals zijn cryptografische primitieven, voorgesteld in 2016 door Peter Todd, verwant aan het concept van fysieke zegels: zodra een Seal op een container is geplaatst, wordt het onmogelijk om deze te openen of aan te passen zonder de Seal onomkeerbaar te verbreken.


![RGB-Bitcoin](assets/en/018.webp)


Deze benadering, getransponeerd naar de digitale wereld, maakt het mogelijk om te bewijzen dat een opeenvolging van gebeurtenissen inderdaad heeft plaatsgevonden en dat deze achteraf niet meer gewijzigd kan worden. Verzegelingen voor eenmalig gebruik gaan dus verder dan de eenvoudige logica van `Hash + Timestamp` en voegen het begrip Seal toe dat **eenmalig** gesloten kan worden.


![RGB-Bitcoin](assets/en/017.webp)


Om zegels voor eenmalig gebruik te laten werken, heb je een medium nodig dat het bestaan of de afwezigheid van een publicatie kan bewijzen en dat moeilijk (zo niet onmogelijk) te vervalsen is als de informatie eenmaal verspreid is. Een **Blockchain** (zoals Bitcoin) kan deze rol vervullen, net als bijvoorbeeld een papieren krant met een publieke oplage. Het idee is als volgt:




- We willen bewijzen dat een bepaalde Commitment op een bericht `h(m)` is gepubliceerd aan een publiek zonder de inhoud van het bericht `m` te onthullen;
- We willen bewijzen dat er geen ander concurrerend `h(m')` bericht Commitment is gepubliceerd in plaats van `h(m)`;
- We willen ook kunnen controleren of bericht `m` voor een bepaalde datum bestaat.


Een Blockchain leent zich ideaal voor deze rol: zodra een transactie is opgenomen in een blok, heeft het hele netwerk hetzelfde onvervalsbare bewijs van het bestaan en de inhoud ervan (tenminste gedeeltelijk, omdat de _commitment_ de details kan verbergen terwijl het de authenticiteit van het bericht bewijst).


Een Single-Use Seal kan daarom gezien worden als een formele belofte om een bericht (dat in dit stadium nog onbekend is) eenmalig te publiceren, op een manier die geverifieerd kan worden door alle geïnteresseerde partijen.


In tegenstelling tot eenvoudige _commitments_ (Hash) of tijdstempels, die getuigen van een bestaansdatum, biedt een Single-Use Seal de extra garantie dat **geen alternatieve Commitment** naast elkaar kan bestaan: je kunt niet twee keer dezelfde Seal sluiten, of proberen het verzegelde bericht te vervangen.


De volgende vergelijking helpt om dit principe te begrijpen:




- **Cryptografische Commitment (Hash)**: Met een Hash functie kun je een stuk data (een getal) vastleggen door de Hash ervan te publiceren. De data blijft geheim totdat je de pre-image onthult, maar je kunt bewijzen dat je het van tevoren wist;
- **Timestamp (Blockchain)**: Door deze Hash in de Blockchain in te voegen, bewijzen we ook dat we het op een precies moment wisten (dat van opname in een blok);
- **Single-Use Seal**: Met zegels voor eenmalig gebruik gaan we een stap verder door de Commitment uniek te maken. Met een enkele Hash kun je meerdere tegenstrijdige toezeggingen tegelijk doen (het probleem van de dokter die "*Het is een jongen*" aan de familie vertelt en "*Het is een meisje*" in zijn persoonlijke dagboek). De Single-Use Seal elimineert deze mogelijkheid door de Commitment te verbinden met een bewijs-van-publicatie medium, zoals de Bitcoin Blockchain, zodat een uitgave van UTXO de Commitment definitief verzegelt. Eenmaal uitgegeven, kan dezelfde UTXO niet opnieuw uitgegeven worden om de Commitment te vervangen.
- **Cryptografische Commitment (Hash)**: Met een Hash functie kun je een stuk data (een getal) vastleggen door de Hash ervan te publiceren. De data blijft geheim totdat je het pre-image onthult, maar je kunt bewijzen dat je het van te voren wist;
- **Timestamp (Blockchain)**: Door deze Hash in de Blockchain in te voegen, bewijzen we ook dat we het op een precies moment wisten (dat van opname in een blok);
- **Single-Use Seal**: Met afdichtingen voor eenmalig gebruik gaan we nog een stap verder door de Commitment uniek te maken. Met één Hash kun je meerdere tegenstrijdige toezeggingen tegelijk doen (het probleem van de dokter die "*Het is een jongen*" aan de familie vertelt en "*Het is een meisje*" in zijn persoonlijke dagboek). De Single-Use Seal elimineert deze mogelijkheid door de Commitment te verbinden met een bewijs-van-publicatie medium, zoals de Bitcoin Blockchain, zodat een uitgave van UTXO de Commitment definitief verzegelt. Eenmaal uitgegeven, kan dezelfde UTXO niet opnieuw uitgegeven worden om de Commitment te vervangen.


|                                                                                  | Simple commitment (digest/hash) | Timestamps | Single-use seals |
| -------------------------------------------------------------------------------- | ------------------------------- | ---------- | ---------------- |
| Publishing the commitment does not reveal the message                           | Yes                             | Yes        | Yes              |
| Proof of the commitment date / existence of the message before a certain date  | Impossible                      | Possible   | Possible         |
| Proof that no alternative commitment can exist                                 | Impossible                      | Impossible | Possible         |

Afdichtingen voor eenmalig gebruik werken in drie hoofdfasen:


**Seal Definition:**




- Alice definieert vooraf de regels voor het publiceren van de Seal (wanneer, waar en hoe het bericht wordt gepubliceerd);
- Bob aanvaardt of erkent deze voorwaarden.


![RGB-Bitcoin](assets/en/021.webp)


**Seal Sluiting:**




- Tijdens runtime sluit Alice de Seal door het eigenlijke bericht te publiceren (gewoonlijk in de vorm van een _commitment_, bijvoorbeeld een Hash);
- Het levert ook een **getuige** (cryptografisch bewijs) die bewijst dat de Seal gesloten en onherroepelijk is.


![RGB-Bitcoin](assets/en/019.webp)


**Seal Verificatie:**




- Als Seal eenmaal gesloten is, kan Bob hem niet meer openen: hij kan alleen controleren of hij gesloten is;
- Bob verzamelt de Seal, de **getuige** en het bericht (of zijn Commitment) om er zeker van te zijn dat alles overeenkomt en dat er geen concurrerende zegels of verschillende versies zijn.


Het proces kan als volgt worden samengevat:


```txt
# Defined by Alice, validated or accepted by Bob
seal <- Define()
# Seal is closed by Alice with the message
witness <- Close(seal, message)
# Verification by Bob
bool <- Verify(seal, witness, message)
```


Client-side Validation gaat echter nog een stap verder: als de definitie van een Seal zelf buiten de Blockchain blijft, is het (in theorie) mogelijk voor iemand om het bestaan of de legitimiteit van de Seal in kwestie aan te vechten. Om dit probleem op te lossen, wordt een keten van in elkaar grijpende Single-use Seals gebruikt:




- Elke gesloten Seal bevat de definitie van de volgende Seal;
- We registreren deze afsluitingen (met hun _commitments_) binnen de Blockchain (in een Bitcoin transactie);
- Elke poging om een eerdere Seal te wijzigen zou dus in tegenspraak zijn met de geschiedenis die in Bitcoin besloten ligt.


Dit is precies wat het RGB systeem doet:




- Gepubliceerde berichten zijn _vastleggingen_ van gevalideerde gegevens aan de cliëntzijde;
- De Seal Definition wordt geassocieerd met een Bitcoin UTXO;
- De Seal sluit wanneer deze UTXO is uitgegeven of wanneer een nieuwe uitgang wordt bijgeschreven op dezelfde Commitment;
- De transactieketen die deze UTXO's uitgeeft komt overeen met het bewijs van publicatie: elke overgang of toestandsverandering op RGB is dus verankerd in Bitcoin.


Samengevat:




- De _verzegelingsdefinitie_ is de UTXO die je wilt Seal een toekomstige Commitment;
- De _seal closing_ vindt plaats wanneer je deze UTXO uitgeeft, waardoor een transactie ontstaat die de Commitment bevat;
- De _getuige_ is de transactie zelf, die bewijst dat je de Seal met deze inhoud hebt afgesloten;
- Je kunt niet bewijzen dat een Seal niet gesloten is (je kunt er niet absoluut zeker van zijn dat een UTXO niet al uitgegeven is of uitgegeven zal worden in een blok dat je nog niet gezien hebt), maar je kunt wel bewijzen dat het inderdaad gesloten is.


Deze uniekheid is belangrijk voor Client-side Validation: wanneer je een State Transition valideert, controleer je of het overeenkomt met een unieke UTXO, die niet eerder uitgegeven is in een concurrerende Commitment. Dit garandeert de afwezigheid van dubbele uitgaven in off-chain slimme contracten.


### Meerdere verplichtingen en wortels


Een RGB Smart contract kan meerdere Verzegelingen voor eenmalig gebruik (meerdere UTXO's) tegelijk moeten uitgeven. Bovendien kan een enkele Bitcoin transactie verwijzen naar meerdere verschillende contracten, die elk hun eigen State Transition verzegelen. Dit vereist een **multi-Commitment** mechanisme om deterministisch en uniek te bewijzen dat geen van de verplichtingen dubbel bestaat. Dit is waar het begrip **Anchor** in RGB om de hoek komt kijken: een speciale structuur die een Bitcoin transactie en één of meer client-side commitments (toestandovergangen) verbindt, elk mogelijk behorend tot een andere Contract. We zullen dit concept nader bekijken in het volgende hoofdstuk.


![RGB-Bitcoin](assets/en/023.webp)


Twee van de belangrijkste GitHub repositories van het project (onder de LNPBP organisatie) groeperen de basisimplementaties van deze concepten die in het eerste hoofdstuk zijn bestudeerd:




- **client_side_validation**: Bevat Rust primitieven voor lokale validatie;
- **single_use_seals**: Implementeert de logica om deze afdichtingen veilig te definiëren en te sluiten.


![RGB-Bitcoin](assets/en/020.webp)


Merk op dat deze software bouwstenen Bitcoin agnostisch zijn; in theorie zouden ze toegepast kunnen worden op elk ander proof-of-publication medium (een ander register, een tijdschrift, etc.). In de praktijk vertrouwt RGB op Bitcoin voor zijn robuustheid en brede consensus.


![RGB-Bitcoin](assets/en/021.webp)


### Vragen van het publiek


#### Naar een breder gebruik van afdichtingen voor eenmalig gebruik


Peter Todd creëerde ook het _Open Timestamps_ protocol, en het Single-Use Seal concept is een natuurlijke uitbreiding van deze ideeën. Naast RGB zijn er andere gebruikssituaties denkbaar, zoals de constructie van _sidechains_ zonder gebruik te maken van _merge mining_ of drivechain-gerelateerde voorstellen zoals BIP300. Elk systeem dat een enkele Commitment nodig heeft, kan in principe deze cryptografische primitieve gebruiken. Vandaag de dag is RGB de eerste grote full-scale implementatie.


#### Problemen met de beschikbaarheid van gegevens


Omdat in Client-side Validation elke gebruiker zijn of haar eigen deel van de geschiedenis opslaat, is de beschikbaarheid van gegevens niet wereldwijd gegarandeerd. Als een Contract emittent bepaalde informatie achterhoudt of intrekt, kan het zijn dat u niet op de hoogte bent van de werkelijke evolutie van het aanbod. In sommige gevallen (zoals stablecoins) wordt van de emittent verwacht dat hij openbare gegevens bijhoudt om het volume in omloop aan te tonen, maar er is geen technische verplichting om dit te doen. Het is dus mogelijk om opzettelijk ondoorzichtige contracten te ontwerpen met onbeperkte Supply, wat vragen oproept over vertrouwen.


#### Sharding en Contract isolatie


Elke Contract vertegenwoordigt een geïsoleerde _shard_: USDT en USDC hoeven bijvoorbeeld hun geschiedenis niet te delen. Atomic swaps zijn nog steeds mogelijk, maar dit houdt niet in dat hun registers worden samengevoegd. Alles wordt gedaan door cryptografische Commitment, zonder de hele geschiedenisgrafiek aan elke deelnemer vrij te geven.


### Conclusie


We hebben gezien waar het concept van Client-side Validation past in Blockchain en _staatskanalen_, hoe het reageert op gedistribueerde computertrilemma's en hoe het Bitcoin Blockchain uniek gebruikt om Double-spending te vermijden en voor *time-stamping*. Het idee is gebaseerd op het begrip **Single-Use Seal**, waarmee unieke verplichtingen kunnen worden aangemaakt die je niet naar believen opnieuw kunt uitgeven. Op deze manier uploadt elke deelnemer alleen de geschiedenis die strikt noodzakelijk is, wat de schaalbaarheid en vertrouwelijkheid van slimme contracten vergroot, terwijl de veiligheid van Bitcoin als achtergrond behouden blijft.


De volgende stap zal zijn om in meer detail uit te leggen hoe dit Single-Use Seal mechanisme wordt toegepast in Bitcoin (via UTXO's), hoe ankers worden gecreëerd en gevalideerd, en vervolgens hoe complete slimme contracten worden gebouwd in RGB. In het bijzonder zullen we kijken naar het probleem van meervoudige verbintenissen, de technische uitdaging om te bewijzen dat een Bitcoin transactie tegelijkertijd meerdere toestandsovergangen in verschillende contracten verzegelt, zonder kwetsbaarheden of dubbele verbintenissen te introduceren.


Voel je vrij om de belangrijkste definities (Client-side Validation, Single-Use Seal, ankers, etc.) te herlezen voordat je in de meer technische details van het tweede hoofdstuk duikt, en houd de algemene logica in gedachten: we zijn op zoek naar een combinatie van de sterke punten van Bitcoin Blockchain (beveiliging, decentralisatie, tijdstempeling) met die van off-chain oplossingen (snelheid, vertrouwelijkheid, schaalbaarheid), en dit is precies wat RGB en Client-side Validation proberen te bereiken.


## De Commitment Layer


<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>


:::video id=73ddea2d-c243-479d-a3dc-12d7db8eef70:::


In dit hoofdstuk bekijken we de implementatie van Client-side Validation en eenmalige afsluitingen binnen Bitcoin Blockchain. We presenteren de hoofdprincipes van RGB's **Commitment Layer** (Layer 1), met speciale aandacht voor het **TxO2** schema, dat RGB gebruikt om een Seal te definiëren en te sluiten in een Bitcoin transactie. Vervolgens bespreken we twee belangrijke punten die nog niet in detail zijn behandeld:




- De _deterministische Bitcoin verplichtingen_;
- Multi-protocol verbintenissen.


Het is de combinatie van deze concepten die ons in staat stelt om verschillende systemen of contracten bovenop één UTXO en dus één Blockchain te plaatsen.


We mogen niet vergeten dat de beschreven cryptografische operaties in absolute termen kunnen worden toegepast op andere blockchains of publicatiemedia, maar de kenmerken van Bitcoin (in termen van decentralisatie, weerstand tegen censuur en openheid voor iedereen) maken het de ideale basis voor het ontwikkelen van geavanceerde programmeerbaarheid zoals vereist door **RGB**.


### Commitment schema's in Bitcoin en hun gebruik door RGB


Zoals we in het eerste hoofdstuk van de cursus zagen, zijn Single-use Seals een algemeen concept: we maken een belofte om een Commitment (_commitment_) op te nemen op een specifieke locatie van een transactie, en deze locatie gedraagt zich als een Seal die we sluiten op een bericht. Echter, op de Bitcoin Blockchain, zijn er verschillende opties om te kiezen waar deze _commitment_ geplaatst moet worden.


Om de logica te begrijpen, herinneren we ons het basisprincipe: om een _single-use seal_ te sluiten, geven we het verzegelde gebied uit door de _commitment_ op een bepaald bericht in te voegen. In Bitcoin kan dit op een aantal manieren:




- Gebruik een openbare sleutel of **Address**


We kunnen besluiten dat een bepaalde publieke sleutel of Address de _single-use seal_ is. Zodra deze sleutel of Address On-Chain verschijnt in een transactie, betekent dit dat de Seal is afgesloten met een bepaald bericht.




- Gebruik een **Bitcoin** transactie-uitgang


Dit betekent dat een zegel voor eenmalig gebruik wordt gedefinieerd als een nauwkeurig _uitgangspunt_ (een txid + uitgangsnummerpaar). Zodra dit _uitgangspunt_ opgebruikt is, wordt de Seal gesloten.


Terwijl we aan RGB werkten, identificeerden we minstens 4 verschillende manieren om deze zegels op Bitcoin te implementeren:




- Definieer de Seal via een publieke sleutel en sluit hem af in een _output_;
- Definieer de Seal met een _outpoint_ en sluit hem af met een _output_;
- Definieer de Seal via de waarde van een publieke sleutel, en sluit deze af in een _input_;
- Definieer de Seal via een _outpoint_, en sluit hem af in een _input_.


| Schema Name | Seal Definition           | Seal Closure              | Additional Requirements                                        | Main Application            | Possible Commitment Schemes     |
| ----------- | ------------------------- | ------------------------- | -------------------------------------------------------------- | --------------------------- | -------------------------------- |
| PkO         | Public Key Value          | Transaction Output        | P2(W)PKH                                                       | None at the moment          | Keytweak, taptweak, opret       |
| TxO2        | Transaction Output        | Transaction Output        | Requires deterministic commitments on Bitcoin                  | RGBv1 (universal)           | Keytweak, tapret, opret         |
| PkI         | Public Key Value          | Transaction Input         | Taproot only & not compatible with legacy wallets              | Bitcoin-based identities    | Sigtweak, witweak               |
| TxO1        | Transaction Output        | Transaction Input         | Taproot only & not compatible with legacy wallets              | None at the moment          | Sigtweak, witweak               |


We zullen niet in detail treden over elk van deze configuraties, omdat we er in RGB voor gekozen hebben om **een _outpoint_ te gebruiken als definitie van de Seal**, en om de _commitment_ te plaatsen in de uitvoer van de transactie die dit _outpoint_ uitgeeft. We kunnen daarom de volgende concepten introduceren voor het vervolg:




- **"Seal Definition"**: Een bepaald _uitgangspunt_ (geïdentificeerd door txid + uitgangsnr.);
- **"Seal sluiten"**: De transactie die dit _outpoint_ uitgeeft, waarin een _commitment_ aan een bericht wordt toegevoegd.


Dit schema is gekozen vanwege de compatibiliteit met de RGB architectuur, maar andere configuraties kunnen nuttig zijn voor verschillende toepassingen.


De "O2" in "TxO2" herinnert ons eraan dat zowel definitie als afsluiting gebaseerd zijn op de uitgave (of creatie) van een transactie-uitgang.


### Voorbeeld TxO2-diagram


Ter herinnering, het definiëren van een zegel voor eenmalig gebruik vereist niet noodzakelijkerwijs het publiceren van een On-Chain transactie. Het is voldoende voor Alice, bijvoorbeeld, om al een onuitgegeven UTXO te hebben. Ze kan beslissen: "Dit _uitgangspunt_ (reeds bestaand) is nu mijn Seal". Ze noteert dit lokaal (_client-side_), en totdat deze UTXO is uitgegeven, wordt de Seal als open beschouwd.


![RGB-Bitcoin](assets/en/024.webp)


Op de dag dat het Seal wil sluiten (om een gebeurtenis te signaleren, of om Anchor een bepaald bericht te geven), geeft het deze UTXO uit in een nieuwe transactie (deze transactie wordt vaak de "_wit transactie_" genoemd (niet gerelateerd aan _segwit_, het is gewoon de term die wij er aan geven). Deze nieuwe transactie zal de _commitment_ voor het bericht bevatten.


![RGB-Bitcoin](assets/en/025.webp)


Merk op dat in dit voorbeeld:




- Niemand anders dan Bob (of de mensen aan wie Alice kiest om het volledige bewijs te onthullen) zal weten dat er een bepaalde boodschap verborgen zit in deze transactie;
- Iedereen kan zien dat het _uitgangspunt_ uitgegeven is, maar alleen Bob heeft het bewijs dat het bericht daadwerkelijk verankerd is in de transactie.


Om dit TxO2-schema te illustreren, kunnen we een _single-use seal_ gebruiken als mechanisme om een PGP-sleutel in te trekken. In plaats van een herroepingscertificaat te publiceren op servers, kan Alice zeggen: "Deze Bitcoin uitvoer, indien uitgegeven, betekent dat mijn PGP-sleutel is ingetrokken".


Alice heeft daarom een specifieke UTXO, waaraan een bepaalde toestand of gegevens (die alleen bij haar bekend zijn) lokaal (aan de kant van de cliënt) zijn gekoppeld.


Alice informeert Bob dat als deze UTXO wordt uitgegeven, een bepaalde gebeurtenis geacht wordt te hebben plaatsgevonden. Van buitenaf zien we alleen een Bitcoin transactie; maar Bob weet dat deze uitgave een verborgen betekenis heeft.


![RGB-Bitcoin](assets/en/026.webp)


Als Alice deze UTXO uitgeeft, sluit ze de Seal op een bericht dat haar nieuwe sleutel aangeeft, of simpelweg de intrekking van de oude. Op deze manier zal iedereen die On-Chain controleert zien dat de UTXO is uitgegeven, maar alleen degenen met het volledige bewijs zullen weten dat het precies de intrekking van de PGP-sleutel is.


![RGB-Bitcoin](assets/en/027.webp)


Om Bob of iemand anders het verborgen bericht te laten controleren, moet Alice hem informatie van off-chain geven.


![RGB-Bitcoin](assets/en/028.webp)


Alice moet Bob daarom het volgende verstrekken:




- Het bericht zelf (bijvoorbeeld de nieuwe PGP-sleutel);
- Cryptografisch bewijs dat het bericht betrokken was bij de transactie (bekend als _extra transactiebewijs_ of _anker_).


![RGB-Bitcoin](assets/en/029.webp)


Derden hebben deze informatie niet. Ze zien alleen dat er een UTXO is uitgegeven. Vertrouwelijkheid is dus gegarandeerd.


Om de structuur te verduidelijken, vatten we het proces samen in twee transacties:




- **Transactie 1**: Dit bevat de _seal definitie_, d.w.z. het _uitgangspunt_ dat zal dienen als de Seal.


![RGB-Bitcoin](assets/en/031.webp)




- **Transactie 2**: Geeft dit _outpoint_ uit. Dit sluit de Seal en voegt in dezelfde transactie de _commitment_ in op het bericht.


![RGB-Bitcoin](assets/en/033.webp)


Daarom noemen we de tweede transactie de "_getuigentransactie_".


Om dit op een andere manier te illustreren, kunnen we twee lagen voorstellen:




- De bovenste Layer (Blockchain, openbaar): iedereen ziet de transactie en weet dat er een *outpoint* is uitgegeven;
- De lagere Layer (client-side, privé): alleen Alice (of de persoon in kwestie) weet dat deze uitgave overeenkomt met een dergelijk bericht, via het cryptografische bewijs en het bericht dat ze lokaal bewaart.


![RGB-Bitcoin](assets/en/034.webp)


Maar bij het sluiten van de Seal rijst de vraag waar de _commitment_ moet worden ingevoegd.


In het vorige deel hebben we kort vermeld hoe het Client-side Validation model kan worden toegepast op RGB en andere systemen. Hier behandelen we het gedeelte over **deterministische Bitcoin verplichtingen** en hoe deze te integreren in een transactie. Het idee is om te begrijpen waarom we een enkele Commitment proberen in te voegen in de _witness transactie_, en vooral hoe we ervoor kunnen zorgen dat er geen andere niet-openbaar gemaakte concurrerende verplichtingen kunnen zijn.


### Commitment locaties in een transactie


Wanneer je iemand het bewijs geeft dat een bepaalde boodschap in een transactie zit, moet je kunnen garanderen dat er niet nog een andere vorm van Commitment (een tweede, verborgen boodschap) in dezelfde transactie zit die niet aan jou onthuld is. Om Client-side Validation robuust te houden, heb je een **deterministisch** mechanisme nodig voor het plaatsen van een enkele _commitment_ in de transactie die de _single-use seal_ sluit.


De _witness transactie_ geeft de beroemde UTXO (of _seal definition_) uit en deze uitgave komt overeen met het sluiten van de Seal. Technisch gesproken weten we dat elk outpoint maar één keer kan worden uitgegeven. Dit is precies wat ten grondslag ligt aan Bitcoin's weerstand tegen dubbele uitgaven. Maar de bestedingstransactie kan meerdere _inputs_, meerdere _outputs_ hebben, of op een complexe manier samengesteld zijn (coinjoins, Lightning channels, etc.). Daarom moeten we duidelijk definiëren waar de _verbintenis_ in deze structuur moet worden ingevoegd, ondubbelzinnig en uniform.


Ongeacht de methode (PkO, TxO2, enz.) kan de _commitment_ worden ingevoegd:




- In een **Invoer** via:
- **Sigtweak** (wijzigt de `r` component van de ECDSA handtekening, vergelijkbaar met het "Sign-to-Contract" principe);
- **Witweak** (de _segregated witness_ gegevens van de transactie zijn gewijzigd).
- In een **Uitvoer** via:
- **Keytweak** (de openbare sleutel van de ontvanger wordt "getweakt" met het bericht);
- **Opret** (het bericht wordt in een niet-besteedbare uitvoer `OP_RETURN` geplaatst);
- **Tapret** (of _Taptweak_), dat vertrouwt op Taproot om Commitment in te voegen in het scriptgedeelte van een Taproot sleutel, waardoor de openbare sleutel deterministisch gewijzigd wordt.


![RGB-Bitcoin](assets/en/035.webp)


Hier volgen de details van elke methode:


![RGB-Bitcoin](assets/en/038.webp)


***Sig tweak (sign-to-Contract):***


Een eerder schema maakte gebruik van het willekeurige deel van een handtekening (ECDSA of Schnorr) om de _commitment_ in te sluiten: dit is de techniek die bekend staat als "**Sign-to-Contract**". Je vervangt de willekeurig gegenereerde Nonce door een Hash die de gegevens bevat. Op deze manier onthult de handtekening impliciet jouw Commitment, zonder extra ruimte in de transactie. Deze aanpak heeft een aantal voordelen:




- Geen On-Chain overbelasting (je gebruikt dezelfde plaats als de basis Nonce);
- In theorie kan dit heel discreet zijn, omdat de Nonce in eerste instantie een willekeurig gegeven is.


Er zijn echter 2 grote nadelen naar voren gekomen:




- Multisig voor Taproot: wanneer je meerdere ondertekenaars hebt, moet je beslissen welke handtekening de _commitment_ zal dragen. Handtekeningen kunnen verschillend gerangschikt worden, en als een ondertekenaar weigert, verlies je de controle over het resultaat van de _commitment_;
- MuSig en de gedeelde Nonce: met Schnorr Multisig (*MuSig*) is het genereren van Nonce een meerpartijenalgoritme en wordt het vrijwel onmogelijk om de Nonce individueel te tweaken.


In de praktijk is **sig tweak** ook niet erg compatibel met bestaande hardware (hardware wallets) en formaten (Lightning, etc.). Dus dit geweldige idee is Hard om in de praktijk te brengen.


***Key tweak (pay-to-Contract):***


De **key tweak** neemt het historische concept van _pay-to-contract_ over. We nemen de publieke sleutel `X` en passen deze aan door de waarde `H(message)` toe te voegen. Als `X = x * G` en `h = H(message)`, dan wordt de nieuwe sleutel `X' = X + h * G`. Deze aangepaste sleutel verbergt de Commitment van het `bericht`. De houder van de originele privésleutel kan, door `h` toe te voegen aan zijn privésleutel `x`, bewijzen dat hij de sleutel heeft om de uitvoer uit te geven. In theorie is dit elegant, omdat:




- De _commitment_ wordt ingevoerd zonder extra velden toe te voegen;
- Je slaat geen extra On-Chain gegevens op.


In de praktijk stuiten we echter op de volgende problemen:




- Portemonnees herkennen de standaard publieke sleutel niet meer, omdat deze "getweakt" is, zodat ze UTXO niet gemakkelijk kunnen associëren met je gebruikelijke sleutel;
- Hardware wallets zijn niet ontworpen om te ondertekenen met een sleutel die niet is afgeleid van hun standaard afleiding;
- Je moet je scripts, descriptors, enz. aanpassen.


In de context van RGB was dit pad voorzien tot 2021, maar het bleek te ingewikkeld om het te laten werken met de huidige normen en infrastructuur.


***Tweak: ***


Een ander idee, dat bepaalde protocollen zoals _inscriptions Ordinals_ in de praktijk hebben gebracht, is om de gegevens direct in de `getuige`-sectie van de transactie te plaatsen (vandaar de uitdrukking "witness tweak"). Deze methode:




- Maakt betrokkenheid direct zichtbaar (je plakt de ruwe gegevens letterlijk in de getuige);
- Kan onderhevig zijn aan censuur (miners of nodes kunnen weigeren om door te geven als het te groot is of een ander willekeurig kenmerk);
- Neemt ruimte in beslag in de blokken, in tegenstelling tot de doelstelling van discretie en lichtheid van RGB.


Bovendien is witness zo ontworpen dat het in bepaalde contexten snoeibaar is, wat het hebben van robuuste bewijzen ingewikkelder kan maken.


***Open-return (opret):***


Met een `OP_RETURN` kun je heel eenvoudig een Hash of bericht opslaan in een speciaal veld van de transactie. Maar het is direct detecteerbaar: iedereen ziet dat er een _commitment_ in de transactie zit, en het kan gecensureerd of weggegooid worden, en voegt extra uitvoer toe. Aangezien dit de transparantie en omvang vergroot, wordt het als minder bevredigend beschouwd vanuit het oogpunt van een Client-side Validation oplossing.


```txt
34-byte_Opret_Commitment =
OP_RETURN   OP_PUSHBYTE_32   <mpc::Commitment>
|_________| |______________| |_________________|

1-byte       1-byte         32 bytes
```


### Tapret


De laatste optie is het gebruik van **Taproot** (geïntroduceerd met BIP341) met het *Tapret* schema. *Tapret* is een complexere vorm van deterministische Commitment, die verbeteringen brengt in termen van footprint op de Blockchain en vertrouwelijkheid voor Contract operaties. Het hoofdidee is om de Commitment te verbergen in het `Script Path Spend` gedeelte van een [Taproot transactie] (https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki).


![RGB-Bitcoin](assets/en/036.webp)


Voordat we beschrijven hoe de Commitment wordt ingevoegd in een Taproot transactie, kijken we naar de **exacte vorm** van de Commitment, die **imperatief** moet overeenkomen met een 64-byte string [geconstrueerd] (https://github.com/BP-WG/bp-core/blob/master/dbc/src/tapret/mod.rs#L179-L196) als volgt:


```txt
64-byte_Tapret_Commitment =

OP_RESERVED ...  ... .. OP_RESERVED   OP_RETURN   OP_PUSHBYTE_33  <mpc::Commitment>  <Nonce>
|___________________________________| |_________| |______________| |_______________|  |______|
OP_RESERVED x 29 times = 29 bytes      1 byte         1 byte          32 bytes        1 byte
|________________________________________________________________| |_________________________|

TAPRET_SCRIPT_COMMITMENT_PREFIX = 31 bytes                    MPC commitment + NONCE = 33 bytes
```




- De 29 bytes `OP_RESERVED`, gevolgd door `OP_RETURN`, dan `OP_PUSHBYTE_33`, vormen het 31 bytes tellende _prefix_ gedeelte;
- Daarna komt een 32 bytes lange _commitment_ (meestal de Merkle Root van **MPC**), waaraan we 1 byte **Nonce** toevoegen (een totaal van 33 bytes voor dit tweede deel).


Dus de 64-byte `Tapret` methode ziet eruit als een `Opret` waaraan we 29 bytes `OP_RESERVED` hebben toegevoegd en een extra byte als Nonce.


Om flexibiliteit te behouden op het gebied van implementatie, vertrouwelijkheid en schaalbaarheid, houdt het Tapret-schema rekening met verschillende gebruikssituaties, afhankelijk van de vereisten:




- Unieke integratie van een Tapret Commitment in een Taproot transactie zonder een reeds bestaande Script Path structuur;
- Integratie van een Tapret Commitment in een Taproot transactie die al is uitgerust met een Script Path.


Laten we deze twee scenario's eens nader bekijken.


#### Tapret inbouwen zonder bestaand Scriptpad


In dit eerste geval gaan we uit van een Taproot output key (*Taproot Output Key*) `Q` die alleen de interne publieke sleutel `P` bevat *(Internal Key*), zonder bijbehorend scriptpad (*Script Path*):


![RGB-Bitcoin](assets/en/047.webp)




- `P`: de interne openbare sleutel voor de _Key Path Spend_.
- `G`: het voortbrengend punt van de elliptische kromme [secp256k1](https://en.Bitcoin.it/wiki/Secp256k1).

-`t = tH_TWEAK(P)` is de tweak factor, berekend via een _tagged hash_ (bijvoorbeeld `SHA-256(SHA-256(TapTweak) || P)`), in overeenstemming met [BIP86](https://github.com/Bitcoin/bips/blob/master/bip-0086.mediawiki#Address-derivation). Dit bewijst dat er geen verborgen script is.


Om een **Tapret** Commitment op te nemen, voeg je een **Script Path Uitgeven** toe met een **uniek script**, als volgt:


![RGB-Bitcoin](assets/en/048.webp)




- `t = tH_TWEAK(P || Script_root)` wordt dan de nieuwe tweak factor, inclusief de **Script_root**.
- `Script_root = tH_BRANCH(64-byte_Tapret_Commitment)` vertegenwoordigt de root van dit **script**, dat eenvoudigweg een Hash van het type `SHA-256(SHA-256(TapBranch) || 64-byte_Tapret_Commitment)` is.


Het bewijs van inclusie en uniciteit in de Taproot tree komt hier neer op de enkele interne publieke sleutel `P`.


#### Tapret-integratie in een reeds bestaand Scriptpad


Het tweede scenario betreft een complexere `Q` **Taproot** uitvoer, die al meerdere scripts bevat. We hebben bijvoorbeeld een boom van 3 scripts:


![RGB-Bitcoin](assets/en/049.webp)




- `tH_LEAF(x)` geeft de genormaliseerde getagde Hash functie van een bladscript aan.
- `A, B, C` staan voor scripts die al zijn opgenomen in de Taproot structuur.


Om de Tapret Commitment toe te voegen, moeten we een *onbruikbaar script* invoegen op het eerste niveau van de boom en de bestaande scripts een niveau naar beneden verschuiven. Visueel wordt de boom:


![RGB-Bitcoin](assets/en/050.webp)




- `tHABC` vertegenwoordigt de Hash met tags van de bovenste groepering `A, B, C`.
- `tHT` vertegenwoordigt de Hash van het script dat overeenkomt met de 64-byte `Tapret`.


Volgens de Taproot regels moet elke tak/blad gecombineerd worden volgens een lexicografische Hash volgorde. Er zijn twee mogelijke gevallen:




- `tHT` > `tHABC`: de Tapret Commitment beweegt naar rechts in de boom. Het bewijs van uniciteit heeft alleen `tHABC` en `P` nodig;
- `tHT` < `tHABC`: de Tapret Commitment is links geplaatst. Om te bewijzen dat er geen andere Tapret Commitment aan de rechterkant is, moeten `tHAB` en `tHC` onthuld worden om de afwezigheid van een dergelijk schrift aan te tonen.


Visueel voorbeeld voor het eerste geval (`tHABC < tHT`):


![RGB-Bitcoin](assets/en/051.webp)


Voorbeeld voor het tweede geval (`tHABC > tHT`):


![RGB-Bitcoin](assets/en/052.webp)


#### Optimalisatie met de Nonce


Om de vertrouwelijkheid te verbeteren, kunnen we de waarde van de `<Nonce>` (de laatste byte van de 64-byte `Tapret`) "delven" (een nauwkeurigere term zou zijn "bruteforcen") in een poging om een Hash `tHT` te verkrijgen zodat `tHABC < tHT`. In dit geval wordt de Commitment aan de rechterkant geplaatst, waardoor de gebruiker niet de hele inhoud van bestaande scripts hoeft te onthullen om de uniciteit van de Tapret aan te tonen.


Samengevat biedt de `Tapret` een discrete en deterministische manier om een Commitment in een Taproot transactie op te nemen, met inachtneming van de eis van uniciteit en ondubbelzinnigheid die essentieel is voor RGB's Client-side Validation en Single-Use Seal logica.


#### Geldige uitgangen


Voor RGB Commitment transacties is de belangrijkste vereiste voor een geldige Bitcoin Commitment regeling als volgt: De transactie (*Witness Transaction*) moet aantoonbaar één Commitment bevatten. Deze eis maakt het onmogelijk om een alternatieve geschiedenis te construeren voor aan de cliëntzijde gevalideerde gegevens binnen dezelfde transactie. Dit betekent dat het bericht waaromheen de _single-use seal_ sluit uniek is.


Om aan dit principe te voldoen, en ongeacht het aantal uitgangen in een transactie, vereisen we dat **één en slechts één uitgang** een Commitment kan bevatten. Voor elk van de gebruikte schema's (*Opret* of *Tapret*), zijn de enige geldige uitgangen die een RGB _commitment_ kunnen bevatten de volgende:




- De eerste uitvoer `OP_RETURN` (indien aanwezig) voor het *Opret* schema;
- De eerste Taproot uitgang (indien aanwezig) voor het *Tapret* schema.


Merk op dat het heel goed mogelijk is dat een transactie een enkele `Opret` Commitment en een enkele `Tapret` Commitment bevat in twee afzonderlijke uitgangen. Dankzij de deterministische aard van Seal Definition, komen deze twee verbintenissen dan overeen met twee verschillende stukken data die gevalideerd zijn aan de kant van de cliënt.


### Analyse en praktische keuzes in RGB


Toen we RGB begonnen, hebben we al deze methoden bekeken om te bepalen waar en hoe we een _commitment_ in een transactie op een deterministische manier konden plaatsen. We definieerden enkele criteria:




- Compatibiliteit met verschillende scenario's (bijv. Multisig, Lightning, hardware wallets, etc.);
- Invloed op On-Chain ruimte;
- Moeilijke implementatie en onderhoud;
- Vertrouwelijkheid en verzet tegen censuur.


| Method                                             | On-chain trace & size | Client-side size | Wallet Integration | Hardware Compatibility | Lightning Compatibility | Taproot Compatibility |
| -------------------------------------------------- | --------------------- | ---------------- | ------------------ | ---------------------- | ---------------------- | --------------------- |
| Keytweak (deterministic P2C)                      | 🟢                     | 🟡                 | 🔴                   | 🟠                     | 🔴 BOLT, 🔴 Bifrost     | 🟠 Taproot, 🟢 MuSig  |
| Sigtweak (deterministic S2C)                      | 🟢                     | 🟢                 | 🟠                   | 🔴                     | 🔴 BOLT, 🔴 Bifrost     | 🟠 Taproot, 🔴 MuSig  |
| Opret (OP_RETURN)                                 | 🔴                     | 🟢                 | 🟢                   | 🟠                     | 🔴 BOLT, 🟠 Bifrost     | -                     |
| Tapret Algorithm: top-left node                   | 🟠                     | 🔴                 | 🟠                   | 🟢                     | 🔴 BOLT, 🟢 Bifrost     | 🟢 Taproot, 🟢 MuSig  |
| Tapret Algorithm #4: any node + proof             | 🟢                     | 🟠                 | 🟠                   | 🟢                     | 🔴 BOLT, 🟢 Bifrost     | 🟢 Taproot, 🟢 MuSig  |
| Deterministic Commitment Scheme                               | Standard       | On-Chain Cost                                                                                                          | Proof Size on Client Side                                                                                       |
| ------------------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Keytweak (Deterministic P2C)                                  | LNPBP-1, 2     | 0 bytes                                                                                                                | 33 bytes (non-tweaked key)                                                                                       |
| Sigtweak (Deterministic S2C)                                  | WIP (LNPBP-39) | 0 bytes                                                                                                                | 0 bytes                                                                                                          |
| Opret (OP_RETURN)                                             | -              | 36 (v)bytes (additional TxOut)                                                                                         | 0 bytes                                                                                                          |
| Tapret Algorithm: top-left node                               | LNPBP-6        | 32 bytes in the witness (8 vbytes) for any n-of-m multisig and spending through script path                           | 0 bytes on scriptless scripts taproot ~270 bytes in a single script case, ~128 bytes if multiple scripts       |
| Tapret Algorithm #4: any node + uniqueness proof              | LNPBP-6        | 32 bytes in the witness (8 vbytes) for single script cases, 0 bytes in the witness in most other cases                | 0 bytes on scriptless scripts taproot, 65 bytes until the Taptree contains a dozen scripts                      |


| Layer                          | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) |
| ------------------------------ | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| **Type**                       | **Tapret**                   | **Tapret #4**                | **Keytweak**                 | **Sigtweak**                 | **Opret**                    | **Tapret**               | **Tapret #4**            | **Keytweak**             | **Sigtweak**             | **Opret**                |
| Single-sig                     | 0                            | 0                            | 0                            | 0                            | 32                           | 0                        | 0                        | 32                       | 0?                       | 0                        |
| MuSig (n-of-n)                 | 0                            | 0                            | 0                            | 0                            | 32                           | 0                        | 0                        | 32                       | ? > 0                    | 0                        |
| Multi-sig 2-of-3               | 32/8                         | 32/8 or 0                    | 0                            | n/a                          | 32                           | ~270                     | 65                       | 32                       | n/a                      | 0                        |
| Multi-sig 3-of-5               | 32/8                         | 32/8 or 0                    | 0                            | n/a                          | 32                           | ~340                     | 65                       | 32                       | n/a                      | 0                        |
| Multi-sig 2-of-3 with timeouts | 32/8                         | 0                            | 0                            | n/a                          | 32                           | 64                       | 65                       | 32                       | n/a                      | 0                        |


| Layer                            | On-Chain Cost (vbytes) | On-Chain Cost (vbytes) | On-Chain Cost (vbytes) | Client-Side Cost (bytes) | Client-Side Cost (bytes) |
| -------------------------------- | ---------------------- | ---------------------- | ---------------------- | ------------------------ | ------------------------ |
| **Type**                         | **Base**               | **Tapret #2**          | **Tapret #4**          | **Tapret #2**            | **Tapret #4**            |
| MuSig (n-of-n)                   | 16.5                   | 0                      | 0                      | 0                        | 0                        |
| FROST (n-of-m)                   | ?                      | 0                      | 0                      | 0                        | 0                        |
| Multi_a (n-of-m)                 | 1+16n+8m               | 8                      | 8                      | 33 * m                   | 65                       |
| Branch MuSig / Multi_a (n-of-m)  | 1+16n+8n+8xlog(n)      | 8                      | 0                      | 64                       | 65                       |
| With timeouts (n-of-m)           | 1+16n+8n+8xlog(n)      | 8                      | 0                      | 64                       | 65                       |
| Method                                    | Privacy & Scalability | Interoperability | Compatibility | Portability | Complexity |
| ----------------------------------------- | ---------------------- | ---------------- | ------------- | ----------- | ---------- |
| Keytweak (Deterministic P2C)              | 🟢                      | 🔴               | 🔴            | 🟡          | 🟡         |
| Sigtweak (Deterministic S2C)              | 🟢                      | 🔴               | 🔴            | 🟢          | 🔴         |
| Opret (OP_RETURN)                         | 🔴                      | 🟠               | 🔴            | 🟢          | 🟢         |
| Algo Tapret: Top-left node                | 🟠                      | 🟢               | 🟢            | 🔴          | 🟠         |
| Algo Tapret #4: Any node + proof          | 🟢                      | 🟢               | 🟢            | 🟠          | 🔴         |






In de loop van het onderzoek werd het duidelijk dat geen van de Commitment schema's volledig compatibel was met de huidige Lightning standaard (die geen Taproot, _muSig2_ of aanvullende _commitment_ ondersteuning gebruikt). Er wordt aan gewerkt om de kanaalconstructie van Lightning (*BiFrost*) aan te passen zodat RGB verplichtingen kunnen worden ingevoegd. Dit is nog een gebied waar we de transactiestructuur, de sleutels en de manier waarop kanaalupdates worden ondertekend, moeten herzien.


Uit de analyse bleek dat andere methoden (key tweak, sig tweak, witness tweak, etc.) in feite andere vormen van complicatie met zich meebrachten:




- Ofwel hebben we een groot On-Chain volume;
- Ofwel is er een radicale incompatibiliteit met de bestaande Wallet code;
- Ofwel is de oplossing niet uitvoerbaar in niet-coöperatieve Multisig.


Voor RGB vallen twee methoden in het bijzonder op: ***Opret*** en ***Tapret***, beide geclassificeerd als "Transaction Output" en compatibel met de TxO2 modus die door het protocol wordt gebruikt.


### Multi protocol verbintenissen - MPC


In dit gedeelte bekijken we hoe **RGB** omgaat met het samenvoegen van meerdere contracten (of, meer precies, hun _transitiebundels_) binnen een enkele Commitment (*Commitment*) vastgelegd in een Bitcoin transactie via een deterministisch schema (volgens `Opret` of `Tapret`). Om dit te bereiken, vindt de volgorde van Merkelization van de verschillende contracten plaats in een structuur genaamd **MPC Tree** (_Multi Protocol Commitment Tree_). In deze sectie bekijken we de constructie van deze MPC Tree, hoe we de wortel ervan verkrijgen en hoe meerdere contracten vertrouwelijk en ondubbelzinnig dezelfde transactie kunnen delen.


Multi Protocol Commitment (MPC) is ontworpen om aan twee behoeften te voldoen:




- De constructie van de `mpc::Commitment` Hash: deze wordt opgenomen in de Bitcoin Blockchain volgens een `Opret` of `Tapret` schema, en moet alle toestandsveranderingen weergeven die gevalideerd moeten worden;
- Gelijktijdige opslag van meerdere contracten in een enkele _commitment_, waardoor afzonderlijke updates van meerdere activa of RGB contracten kunnen worden beheerd in een enkele Bitcoin transactie.


Concreet behoort elke _overgangsbundel_ tot een bepaalde Contract. Al deze informatie wordt ingevoegd in een **MPC Boom**, waarvan de wortel (`mpc::Root`) weer gehasht wordt om de `mpc::Commitment` te geven. Het is deze laatste Hash die geplaatst wordt in de Bitcoin transactie (_witness transactie_), volgens de gekozen deterministische methode.


![RGB-Bitcoin](assets/en/042.webp)


#### MPC Wortel Hash


De werkelijk geschreven waarde On-Chain (in `Opret` of `Tapret`) heet `mpc::Commitment`. Dit wordt berekend in de vorm van [BIP-341](https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki), volgens de formule:


```txt
mpc::Commitment = SHA-256(SHA-256(mpc_tag) || SHA-256(mpc_tag) || depth || cofactor || mpc::Root )
```


waar:




- `mpc_tag` is een tag: `urn:ubideco:mpc:Commitment#2024-01-31`, gekozen volgens [RGB tagging conventions] (https://github.com/RGB-WG/RGB-core/blob/master/doc/Commitments.md);
- `depth` (1 byte) geeft de diepte van de *MPC Tree* aan;
- cofactor` (16 bits, in Little Endian) is een parameter die gebruikt wordt om de uniciteit van de posities toegewezen aan elke Contract in de boom te bevorderen;
- `mpc::Root` is de wortel van *MPC Tree*, berekend volgens het proces dat in de volgende sectie wordt beschreven.


![RGB-Bitcoin](assets/en/044.webp)


#### MPC Boomconstructie


Om deze MPC-boom op te bouwen, moeten we ervoor zorgen dat elke Contract overeenkomt met een unieke bladpositie. Stel we hebben:




- `c` op te nemen contracten geïndexeerd door `i` in `i` = {0,1,..,C-1};
- Voor elke Contract `c_i` hebben we een identifier `ContractId(i) = c_i`.


We construeren dan een boom van breedte `w` en diepte `d` zo dat `2^d = w`, met `w > C`, zodat elke Contract in een apart _blad_ geplaatst kan worden. De positie `pos(c_i)` van elke Contract in de boom wordt bepaald door:


```txt
pos(c_i) = c_i mod (w - cofactor)
```


waarbij `cofactor` een geheel getal is dat de kans op het verkrijgen van verschillende posities voor elke Contract vergroot. In de praktijk volgt de constructie een iteratief proces:




- We beginnen met een minimale diepte (`d=3` volgens afspraak om het exacte aantal contracten te verbergen);
- We proberen verschillende `cofactoren` (tot `w/2`, of maximaal 500 om prestatieredenen);
- Als het niet lukt om alle contracten zonder botsing te positioneren, verhogen we `d` en beginnen we opnieuw.


Het doel is om te hoge bomen te vermijden en het risico op botsingen zo klein mogelijk te houden. Merk op dat het botsingsfenomeen een willekeurige distributielogica volgt, gekoppeld aan de [Anniversary Paradox] (https://en.wikipedia.org/wiki/Birthday_problem).


#### Bewoonde bladeren


Zodra `C` verschillende posities `pos(c_i)` zijn verkregen voor contracten `i = {0,1,..,C-1}`, wordt elk blad gevuld met een Hash functie (*getagd Hash*):


```txt
tH_MPC_LEAF(c_i) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x10 || c_i || BundleId(c_i))
```


waar:




- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, wordt altijd gekozen volgens de Merkle-conventies van RGB;
- `0x10` identificeert een _contractblad_;
- `c_i` is de 32-bytes Contract identificator (afgeleid van de Genesis Hash);
- bundleId(c_i)` is een Hash van 32 bytes die de verzameling `State Transitions` beschrijft met betrekking tot `c_i` (verzameld in een *Transition Bundle*).


#### Onbewoonde bladeren


De resterende bladeren, die niet zijn toegewezen aan een Contract (d.w.z. `w - C` bladeren), worden gevuld met een "dummy" waarde (_entropie blad_):


```txt
tH_MPC_LEAF(j) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x11 || entropy || j )
```


waar:




- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, wordt altijd gekozen volgens de Merkle-conventies van RGB;
- `0x11` geeft een _entropieblad_ aan;
- `entropie` is een willekeurige waarde van 64 bytes, gekozen door de persoon die de boom bouwt;
- `j` is de positie (in 32 bits Little Endian) van dit blad in de boom.


#### MPC-knooppunten


Na het genereren van de `w` bladeren (bewoond of niet), gaan we over tot merkelisatie. Alle interne knooppunten worden als volgt gehasht:


```txt
tH_MPC_BRANCH(tH1 || tH2) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || b || d || w || tH1 || tH2)
```


waar:




- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, wordt altijd gekozen volgens de Merkle-conventies van RGB;
- b` is de _vertakkingsfactor_ (8 bits). Meestal is `b=0x02` omdat de boom binair en compleet is;
- d` is de diepte van de knoop in de boom;
- `w` is de breedte van de boom (in 256-bits Little Endian binair);
- tH1` en `tH2` zijn de hashes van de child nodes (of bladeren), die al berekend zijn zoals hierboven getoond.


Op deze manier verkrijgen we de wortel `mpc::Root`. We kunnen dan `mpc::Commitment` berekenen (zoals hierboven uitgelegd) en het invoegen in On-Chain.


Laten we, om dit te illustreren, een voorbeeld nemen waarbij `C=3` (drie contracten). Hun posities worden verondersteld `pos(c_0)=7`, `pos(c_1)=4`, `pos(c_2)=2` te zijn. De andere bladeren (posities 0, 1, 3, 5, 6) zijn _entropie bladeren_. Het diagram hieronder toont de opeenvolging van hashes naar de root met:




- `BUNDLE_i` die staat voor `BundleId(c_i)`;
- `tH_MPC_LEAF(A)` enzovoort, die bladeren voorstellen (sommige voor contracten, andere voor entropie);
- Elke vertakking `tH_MPC_BRANCH(...)` combineert de hashes van zijn twee kinderen.


Het uiteindelijke resultaat is de **mpc::Root**, dan de `mpc::Commitment`.


![RGB-Bitcoin](assets/en/053.webp)


#### MPC ascontrole


Wanneer een verificateur er zeker van wil zijn dat een `c_i` Contract (en zijn `BundleId`) is opgenomen in de uiteindelijke `mpc::Commitment`, ontvangt hij eenvoudigweg een Merkle bewijs. Dit bewijs geeft de knooppunten aan die nodig zijn om de bladeren (in dit geval `c_i`'s _contract blad_) terug te leiden naar de root. Het is niet nodig om de hele *MPC Tree* vrij te geven: dit beschermt de vertrouwelijkheid van andere contracten.


In het voorbeeld heeft een `c_2` verificateur alleen een tussenliggende Hash nodig (`tH_MPC_LEAF(D)`), twee `tH_MPC_BRANCH(...)`, het `pos(c_2)` positie bewijs en de `cofactor` waarde. Het kan dan lokaal de wortel reconstrueren, vervolgens de `mpc::Commitment` herberekenen en vergelijken met degene die geschreven is in de Bitcoin transactie (binnen `Opret` of `Tapret`).


![RGB-Bitcoin](assets/en/054.webp)


Dit mechanisme zorgt ervoor dat:




- De status met betrekking tot `c_2` is inderdaad opgenomen in het aggregate informatieblok (client-side);
- Niemand kan een alternatieve geschiedenis opbouwen met dezelfde transactie, omdat de On-Chain _commitment_ naar een enkele MPC root wijst.


#### Overzicht van de MPC-structuur


Multi Protocol Commitment (MPC) is het principe dat RGB in staat stelt om meerdere contracten samen te voegen in een enkele Bitcoin transactie, met behoud van de uniciteit van de verplichtingen en vertrouwelijkheid ten opzichte van andere deelnemers. Dankzij de deterministische constructie van de boom krijgt elke Contract een unieke positie toegewezen en de aanwezigheid van "dummy" bladeren (*Entropy Leaves*) verhult gedeeltelijk het totale aantal contracten dat deelneemt aan de transactie.


De hele Merkle Tree wordt nooit opgeslagen op de client. We generate gewoon een _Merkle pad_ voor elke Contract in kwestie, dat doorgestuurd wordt naar de ontvanger (die dan de Commitment kan valideren). In sommige gevallen heb je meerdere assets die door dezelfde UTXO zijn gegaan. Je kunt dan meerdere _Merkle paden_ samenvoegen in een zogenaamd _multi-protocol Commitment blok_, om te voorkomen dat je teveel gegevens dupliceert.


Elk _Merkle bewijs_ is daarom licht, vooral omdat de boomdiepte niet meer dan 32 zal zijn in RGB. Er is ook een begrip van "Merkle blok", dat meer informatie bevat (doorsnede, entropie, enz.), handig voor het combineren of scheiden van verschillende takken.


Daarom duurde het zo lang om RGB af te ronden. We hadden de algemene visie vanaf 2019: alles aan client-side zetten, tokens off-chain laten circuleren. Maar voor details zoals sharding voor meerdere contracten, de structuur van Merkle Tree, hoe om te gaan met collisions en merge proofs... dit alles vereiste iteraties.


### Ankers: een wereldwijde assemblage


Na de constructie van onze verplichtingen (`Opret` of `Tapret`) en onze MPC (*Multi Protocol Commitment*), moeten we Address het begrip **Anchor** in het RGB protocol gebruiken. Een Anchor is een client-side gevalideerde structuur die de Elements samenbrengt die nodig zijn om te verifiëren dat een Bitcoin Commitment daadwerkelijk specifieke contractuele informatie bevat. Met andere woorden, een Anchor vat alle gegevens samen die nodig zijn om de hierboven beschreven _verbintenissen_ te valideren.


Een Anchor bestaat uit drie geordende velden:




- gW-541
- `MPC Bewijs`
- extra transactie bewijs - ETP


Elk van deze velden speelt een rol in het validatieproces, of het nu gaat om het reconstrueren van de onderliggende Bitcoin transactie of het bewijzen van het bestaan van een verborgen Commitment (vooral in het geval van `Tapret`).


#### txid


Het `txid` veld komt overeen met de 32 bytes identifier van de Bitcoin transactie die de `Opret` of `Tapret` Commitment bevat.


In theorie zou het mogelijk zijn om deze `txid` te vinden door de keten van toestandsovergangen te volgen die zelf naar elke Witness Transaction wijzen, volgens de logica van Single-use Seals. Echter, om de verificatie te vergemakkelijken en te versnellen, is deze `txid` simpelweg opgenomen in de Anchor, zodat de validator niet de hele off-chain geschiedenis hoeft te doorlopen.


#### MPC Bewijs


Het tweede veld, `MPC Proof`, verwijst naar het bewijs dat deze specifieke Contract (bijv. `c_i`) is opgenomen in de _Multi Protocol Commitment_. Het is een combinatie van:




- `pos_i`, de positie van deze Contract in de MPC-structuur;
- cofactor`, de waarde die is gedefinieerd om positiebotsingen op te lossen;
- het `Merkle bewijs`, d.w.z. de verzameling knooppunten en hashes die gebruikt worden om de MPC root te reconstrueren en te verifiëren dat de Contract identifier en zijn `Transition Bundle` gecommitteerd zijn aan de root.


Dit mechanisme werd beschreven in de vorige sectie over het bouwen van de *MPC Tree*, waar elke Contract een uniek blad krijgt dankzij:


```txt
pos(c_i) = c_i mod (w - cofactor)
```


Daarna wordt een deterministisch merkelisatie schema gebruikt om alle bladeren samen te voegen (contracten + entropie). Uiteindelijk kan met de `MPC Proof` de wortel lokaal worden gereconstrueerd en vergeleken met de `mpc::Commitment` opgenomen On-Chain.


#### Extra transactiebewijs - ETP


Het derde veld, de **ETP**, is afhankelijk van het gebruikte type Commitment. Als de Commitment van het type `Opret` is, is er geen extra bewijs nodig. De validator inspecteert de eerste `OP_RETURN` uitvoer van de transactie en vindt daar direct de `mpc::Commitment`.


**Als de Commitment van het type `Tapret`** is, moet er een extra bewijs worden geleverd, genaamd *Extra Transactie Bewijs - ETP*. Het bevat:




- De interne openbare sleutel (`P`) van de Taproot uitgang waarin de *Commitment* is ingebed;
- De partnerknooppunten van de `Script Path Spend` (wanneer de Tapret *Commitment* in een script wordt ingevoegd), om de exacte locatie van dit script in de Taproot boom aan te tonen:
 - Als de `Tapret` *Commitment* zich op de rechtertak bevindt, onthullen we de linkerknoop (bijvoorbeeld `tHABC`),
 - Als de `Tapret` *Commitment* aan de linkerkant staat, moet je 2 knooppunten onthullen (bijvoorbeeld `tHAB` en `tHC`) om te bewijzen dat er geen andere *Commitment* aan de rechterkant staat.
- De `Nonce` kan worden gebruikt om de beste configuratie te "ontginnen", waardoor de *Commitment* aan de rechterkant van de boom kan worden geplaatst (bewijsoptimalisatie).


Dit extra bewijs is essentieel omdat, in tegenstelling tot `Opret`, de `Tapret` Commitment geïntegreerd is in de structuur van een Taproot script, wat het onthullen van een deel van de Taproot boom vereist om de locatie van de *Commitment* correct te valideren.


![RGB-Bitcoin](assets/en/045.webp)


De **Anchors** bevatten daarom alle informatie die nodig is om een Bitcoin Commitment in de context van RGB te valideren. Ze geven zowel de relevante transactie (`txid`) als het bewijs van Contract positionering (`MPC Bewijs`) aan, en beheren het aanvullende bewijs (`ETP`) in het geval van `Tapret`. Op deze manier beschermt een Anchor de integriteit en uniciteit van de off-chain-status door ervoor te zorgen dat dezelfde transactie niet opnieuw geïnterpreteerd kan worden voor andere contractuele gegevens.


### Conclusie


In dit hoofdstuk hebben we het volgende behandeld:




- Hoe het concept van eenmalige afdichtingen toe te passen in Bitcoin (in het bijzonder via een _uitgangspunt_);
- De verschillende methoden voor het deterministisch invoegen van een _commitment_ in een transactie (Sig tweak, Key tweak, witness tweak, OP_RETURN, Taproot/Tapret);
- De redenen waarom RGB zich richt op Tapret-verplichtingen;
- Multi-Contract beheer via _multi-protocol commitments_, essentieel als je niet een hele staat of andere contracten wilt blootgeven wanneer je een specifiek punt wilt bewijzen;
- We hebben ook de rol van _Anchors_ gezien, die alles samenbrengen (transactie txid, Merkle Tree bewijs en Taproot bewijs) in één pakket.


In de praktijk is de technische implementatie verdeeld over verschillende toegewijde Rust _crates_ (in _client_side_validation_, _commit-verify_, _bp_core_, etc.). De fundamentele begrippen zijn er:


![RGB-Bitcoin](assets/en/046.webp)


In het volgende hoofdstuk kijken we naar de zuivere off-chain component van RGB, namelijk Contract logica. We zullen zien hoe RGB contracten, georganiseerd als gedeeltelijk gerepliceerde _finite state machines_, een veel hogere expressiviteit bereiken dan Bitcoin scripts, terwijl de vertrouwelijkheid van hun gegevens behouden blijft.


## Inleiding tot smart contracts en hun statussen


<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>


:::video id=db4ee09f-1352-4ad1-9f7a-c962df7ea9fa:::


In dit en het volgende hoofdstuk kijken we naar het begrip **Smart contract** binnen de RGB omgeving en verkennen we de verschillende manieren waarop deze contracten hun *staat* kunnen definiëren en evolueren. We zullen zien waarom de RGB architectuur, gebruikmakend van de geordende opeenvolging van Single-use Seals, het mogelijk maakt om verschillende soorten ***Contract Operaties*** uit te voeren op een schaalbare manier en zonder via een gecentraliseerd register te gaan. We kijken ook naar de fundamentele rol van ***Business Logic*** in de evolutie van Contract State.


### Slimme contracten en digitale rechten aan toonder


Het doel van RGB is om een infrastructuur te bieden voor het implementeren van slimme contracten op Bitcoin. Met "Smart contract" bedoelen we een overeenkomst tussen meerdere partijen die automatisch en computationeel wordt afgedwongen, zonder menselijke tussenkomst om de clausules af te dwingen. Met andere woorden, de wet van Contract wordt afgedwongen door de software, niet door een vertrouwde derde partij.


Deze automatisering roept de vraag van decentralisatie op: hoe kunnen we ons bevrijden van een gecentraliseerd register (bijv. een centraal platform of database) om de prestaties van Ownership en Contract te beheren? Het oorspronkelijke idee, overgenomen door RGB, is om terug te keren naar een modus van Ownership die bekend staat als "instrumenten aan toonder". Historisch gezien werden bepaalde effecten (obligaties, aandelen, etc.) uitgegeven aan toonder, zodat iedereen die het document fysiek bezat zijn of haar rechten kon afdwingen.


![RGB-Bitcoin](assets/en/055.webp)


RGB past dit concept toe op de digitale wereld: rechten (en plichten) worden ingekapseld in gegevens die off-chain gemanipuleerd worden, en de status van deze gegevens wordt gevalideerd door de deelnemers zelf. Dit maakt a priori een veel grotere mate van vertrouwelijkheid en onafhankelijkheid mogelijk dan andere benaderingen op basis van openbare registers.


### Inleiding tot Smart contract RGB status


Een Smart contract in RGB kan gezien worden als een toestandsmachine, gedefinieerd door:




- Een **State**, d.w.z. de set informatie die de huidige configuratie van de Contract weergeeft;
- Een **Business Logic** (set regels), die beschrijft onder welke voorwaarden en door wie de toestand gewijzigd kan worden.


![RGB-Bitcoin](assets/en/056.webp)


Het is belangrijk om te begrijpen dat deze contracten niet beperkt zijn tot de eenvoudige overdracht van tokens. Ze kunnen een breed scala aan toepassingen belichamen: van traditionele activa (tokens, aandelen, obligaties) tot complexere mechanismen (gebruiksrechten, commerciële voorwaarden, etc.). In tegenstelling tot andere blockchains, waar de Contract-code voor iedereen toegankelijk en uitvoerbaar is, wordt bij RGB de toegang tot en de kennis van Contract gecompartimenteerd voor deelnemers ("***Contract-deelnemers***"). Er zijn verschillende rollen:




- De **verstrekker** of maker van de Contract, die de Genesis van de Contract en zijn initiële variabelen definieert;
- Partijen met **rechten** (*Ownership*) of andere handhavingsmogelijkheden;
- **Waarnemers**, die mogelijk beperkt zijn tot het zien van bepaalde informatie, maar die geen wijzigingen kunnen teweegbrengen.


Deze scheiding van rollen draagt bij aan censuurbestendigheid, door ervoor te zorgen dat alleen geautoriseerde personen kunnen communiceren met de contractuele staat. Het geeft RGB ook de mogelijkheid om horizontaal te schalen: de meeste validaties vinden plaats buiten Blockchain, en alleen cryptografische ankers (de *commitments*) worden op Bitcoin vastgelegd.


### Status en Business Logic in RGB


Praktisch gezien neemt de **Business Logic** van de Contract de vorm aan van regels en scripts, gedefinieerd in wat de RGB een **Schema** noemt. De Schema codeert:




- Staatsstructuur (welke velden zijn openbaar? Welke velden zijn eigendom van welke partijen?
- Geldigheidsvoorwaarden (wat moet worden gecontroleerd voordat een statusupdate wordt geautoriseerd?);
- Autorisaties (wie mag een *State Transition* initiëren? Wie mag alleen observeren?).


Tegelijkertijd valt de **Contract State** vaak uiteen in twee componenten:




- A **Global State**: openbaar deel, mogelijk waarneembaar door iedereen (afhankelijk van configuratie);
- **Eigen Staten**: private delen, specifiek toegewezen aan eigenaars via UTXO's waarnaar verwezen wordt in de Contract logica.


Zoals we in de volgende hoofdstukken zullen zien, moet elke statusupdate (*Contract Operation*) aansluiten op een Bitcoin _commitment_ (via `Opret` of `Tapret`) en voldoen aan de *Business Logic* scripts om als geldig beschouwd te worden.


### Contract Operaties: ontstaan en evolutie van de staat


In het RGB universum is een ***Contract Operation*** elke gebeurtenis die de Contract verandert van een **oude toestand** in een **nieuwe toestand**. Deze operaties volgen de volgende logica:




- We nemen kennis van de huidige status van de Contract;
- We passen de regel of bewerking toe (een ***State Transition***, een ***Genesis*** als het de allereerste status is, of een ***State Extension*** als er een openbare *Valency* is om opnieuw te triggeren);
- We Anchor de wijziging via een nieuwe _commitment_ op de Blockchain, waarbij we een _single-use seal_ sluiten en een andere aanmaken;
- De betrokken rechthebbenden valideren lokaal (*client-side*) dat de overgang conform de *Schema* is en dat de bijbehorende Bitcoin transactie On-Chain is geregistreerd.


![RGB-Bitcoin](assets/en/057.webp)


Het eindresultaat is een bijgewerkte Contract, nu met een andere toestand. Bij deze overgang hoeft het hele Bitcoin netwerk zich niet met de details bezig te houden, omdat alleen een kleine cryptografische vingerafdruk (de _commitment_) in de Blockchain wordt vastgelegd. De opeenvolging van eenmalige verzegelingen voorkomt Double-spending of dubbel gebruik van de toestand.


### Operatieketen: van Genesis tot Eindtoestand


Om dit in perspectief te zetten, een RGB Smart contract begint met een **Genesis**, de allereerste toestand. Daarna volgen verschillende Contract operaties elkaar op, die een DAG (*Directed Acyclic Graph*) van operaties vormen:




- Elke overgang is gebaseerd op een vorige toestand (of meerdere, in het geval van convergente overgangen);
- De chronologische volgorde wordt gegarandeerd door de opname van elke overgang in een Bitcoin Anchor, voorzien van een tijdstempel en onveranderbaar dankzij de consensus van Proof-of-Work;
- Wanneer er geen bewerkingen meer worden uitgevoerd, wordt een **Terminal State** bereikt: de meest recente en volledige toestand van de Contract.


![RGB-Bitcoin](assets/en/012.webp)


Deze DAG-topologie (in plaats van een eenvoudige lineaire keten) weerspiegelt de mogelijkheid dat verschillende delen van Contract parallel kunnen evolueren, zolang ze elkaar niet tegenspreken. RGB zorgt er dan voor dat eventuele inconsistenties worden vermeden door *client-side* verificatie van elke betrokken deelnemer.


### Samenvatting


Slimme contracten in RGB introduceren een model van digitale toonderinstrumenten, gedecentraliseerd maar verankerd in Bitcoin voor tijdstempeling en het garanderen van de volgorde van transacties. De geautomatiseerde uitvoering van deze contracten is gebaseerd op:




- Een **Contract State**, die de huidige configuratie van de Contract aangeeft (rechten, saldi, variabelen, enz.);
- Een **Business Logic** (*Schema*), die definieert welke overgangen zijn toegestaan en hoe ze moeten worden gevalideerd;
- **Contract Operaties**, die deze toestand stap voor stap bijwerken, dankzij vastleggingen die verankerd zijn in Bitcoin transacties.


In het volgende hoofdstuk gaan we dieper in op de concrete representatie van deze ***staten*** en ***staatovergangen*** op off-chain-niveau, en hoe ze zich verhouden tot de UTXO's en Enkelvoudige Verzegelingen die zijn ingebed in Bitcoin. Dit zal een gelegenheid zijn om te zien hoe de interne mechanica van RGB, gebaseerd op Client-side Validation, erin slaagt om de consistentie van slimme contracten te handhaven met behoud van de vertrouwelijkheid van gegevens.


## RGB Contract operaties


<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>


:::video id=1caec34d-f214-425b-a1a4-0a40ae7d3e0e:::


In dit hoofdstuk bekijken we hoe operaties in slimme contracten en toestandsovergangen werken, opnieuw binnen het RGB protocol. Het doel is ook om te begrijpen hoe meerdere deelnemers samenwerken om Ownership van een goed over te dragen.


### Toestandsovergangen en hun mechanica


Het algemene principe is nog steeds dat van Client-side Validation, waarbij de staatsgegevens in handen zijn van de eigenaar en gevalideerd worden door de ontvanger. De specificiteit hier met RGB ligt echter in het feit dat Bob, als ontvanger, Alice vraagt om bepaalde informatie op te nemen in de Contract gegevens om echte controle te hebben over het ontvangen goed, via een verborgen verwijzing naar een van zijn UTXO's.


Om het proces van een *State Transition* (dat een van de fundamentele ***Contract Operaties*** in RGB is) te illustreren, nemen we een stap-voor-stap voorbeeld van een vermogensoverdracht tussen Alice en Bob:


**Initiële situatie:**


Alice heeft een ***Stash RGB*** van lokaal gevalideerde gegevens (*client-side*). Deze Stash verwijst naar een van haar UTXO's op Bitcoin. Dit betekent dat een _seal definition_ in deze gegevens wijst naar een UTXO die bij Alice hoort. Het idee is om haar in staat te stellen bepaalde digitale rechten gekoppeld aan een goed (bijv. RGB tokens) over te dragen aan Bob.


![RGB-Bitcoin](assets/en/058.webp)


**Bob heeft ook UTXO's:**


Bob daarentegen heeft minstens één eigen UTXO, zonder directe verbinding met die van Alice. In het geval dat Bob geen UTXO heeft, is het nog steeds mogelijk om de overdracht naar hem te maken met behulp van de *Witness Transaction* zelf: de uitvoer van deze transactie zal dan de Commitment (_commitment_) bevatten en impliciet Ownership van de nieuwe Contract associëren met Bob.


![RGB-Bitcoin](assets/en/059.webp)


**Bouw van de nieuwe woning (*Nieuwe staat*):**


Bob stuurt Alice informatie gecodeerd in de vorm van een ***Invoice*** (we zullen in latere hoofdstukken dieper ingaan op de constructie van Invoice), en vraagt haar een nieuwe toestand te creëren die voldoet aan de regels van de Contract. Deze toestand zal een nieuwe *Seal Definition* bevatten die naar een van Bob's UTXO's wijst. Op deze manier krijgt Bob Ownership van de activa die in deze nieuwe toestand zijn gedefinieerd, bijvoorbeeld een bepaalde hoeveelheid RGB tokens.


![RGB-Bitcoin](assets/en/060.webp)


**Voorbereiding van de voorbeeldtransactie:**


Alice creëert dan een Bitcoin transactie om de UTXO uit te geven waarnaar verwezen werd in de vorige Seal (degene die haar legitimeerde als de houder). In de uitvoer van deze transactie wordt een *Commitment* (via `Opret` of `Tapret`) ingevoegd om Anchor de nieuwe RGB toestand te geven. De `Opret` of `Tapret` verplichtingen zijn afgeleid van een *MPC tree* (zoals gezien in voorgaande hoofdstukken), die meerdere overgangen van verschillende contracten kan samenvoegen.


**Transmissie van *Consignment* naar Bob:**


Alvorens de transactie uit te zenden, stuurt Alice Bob een ***Consignment*** met alle benodigde *client-side* gegevens (zijn *Stash*) en de nieuwe toestandsinformatie in het voordeel van Bob. Op dit moment past Bob de RGB consensusregels toe:




- Het valideert alle RGB gegevens die in de *Consignment* staan, inclusief de nieuwe status die het Ownership van het bedrijfsmiddel geeft;
- Vertrouwend op de *Anchors* in de *Consignment*, controleert het de chronologie van de getuigentransacties (van Genesis tot de meest recente overgang) en valideert het de overeenkomstige verbintenissen in de Blockchain.


**Overgang voltooiing:**


Als Bob tevreden is, kan hij zijn goedkeuring geven (bijvoorbeeld door de *Consignment* te ondertekenen). Alice kan dan de voorbereide voorbeeldtransactie uitzenden. Eenmaal bevestigd, sluit dit de Seal die eerder in handen was van Alice en formaliseert Ownership door Bob. De beveiliging tegen Double-spending is dan gebaseerd op hetzelfde mechanisme als bij Bitcoin: de UTXO wordt uitgegeven, wat bewijst dat Alice hem niet meer kan hergebruiken.


![RGB-Bitcoin](assets/en/061.webp)


De nieuwe toestand verwijst nu naar UTXO van Bob, waardoor Bob de Ownership krijgt die voorheen in het bezit was van Alice. De Bitcoin uitgang waar de RGB gegevens verankerd zijn, wordt het onherroepelijke bewijs van de overdracht van Ownership.


Een voorbeeld van een minimale DAG (*Directed Acyclic Graph*) bestaande uit twee Contract operaties (een **Genesis** dan een ***State Transition***) kan illustreren hoe de RGB toestand (*client-side* Layer, in rood) verbindt met de Bitcoin Blockchain (*Commitment* Layer, in oranje).


![RGB-Bitcoin](assets/en/062.webp)


Het laat zien dat een Genesis een Seal definieert (*Seal Definition*), vervolgens sluit een *State Transition* deze Seal om een nieuwe te maken in een andere UTXO.


In deze context volgen hier enkele terminologische herinneringen:




- Een ***Assignment*** combineert het volgende:
    - Een ***Seal Definition*** (wat wijst op een UTXO);
- **Owned States**, d.w.z. gegevens gekoppeld aan Ownership (bijvoorbeeld de hoeveelheid overgedragen tokens).
- Een **Global State** brengt de algemene eigenschappen van de Contract samen, zichtbaar voor iedereen, en verzekert de globale consistentie van evoluties.


**State Transitions**, beschreven in het vorige hoofdstuk, zijn de hoofdvorm van Contract Operation. Ze verwijzen naar één of meer voorgaande toestanden (van Genesis of een andere State Transition) en werken deze bij naar een nieuwe toestand.


![RGB-Bitcoin](assets/en/063.webp)


Dit diagram laat zien hoe, in een *State Transition Bundle*, meerdere seals kunnen worden gesloten in een enkele voorbeeldtransactie, terwijl tegelijkertijd nieuwe seals worden geopend. Een interessante eigenschap van het RGB protocol is de mogelijkheid om te schalen: verschillende overgangen kunnen samengevoegd worden tot een Transition Bundle, waarbij elke samenvoeging geassocieerd wordt met een apart blad van de *MPC boom* (een unieke bundel identifier). Dankzij het *Deterministic Bitcoin Commitment* (DBC) mechanisme wordt het gehele bericht ingevoegd in een `Tapret` of `Opret` uitgang, terwijl voorgaande zegels worden gesloten en mogelijk nieuwe worden gedefinieerd. De `Anchor` dient als directe link tussen de Commitment opgeslagen in de Blockchain en de Client-side Validation structuur (*client-side*).


In de volgende hoofdstukken bekijken we alle componenten en processen die betrokken zijn bij het bouwen en valideren van een State Transition. De meeste van deze Elements maken deel uit van de RGB consensus, geïmplementeerd in de **RGB Core Library**.


### Transition Bundle


Op RGB is het mogelijk om verschillende toestandsovergangen te bundelen die behoren tot dezelfde Contract (d.w.z. ze delen dezelfde **ContractId**, afgeleid van de Genesis **OpId**). In het eenvoudigste geval, zoals tussen Alice en Bob in het bovenstaande voorbeeld, bevat een **Transition Bundle** slechts één overgang. Maar ondersteuning voor operaties met meerdere spelers (zoals coinjoins, Lightning channel openingen, etc.) betekent dat meerdere gebruikers hun State Transitions kunnen combineren in een enkele bundel.


Eenmaal verzameld, worden deze overgangen verankerd (door het MPC + DBC mechanisme) in een enkele Bitcoin transactie:




- Elke State Transition wordt gehasht en gegroepeerd in een Transition Bundle;
- De Transition Bundle wordt zelf gehasht en ingevoegd in het MPC tree blad dat overeenkomt met deze Contract (een BundleId);
- De MPC-boom wordt uiteindelijk ingeschakeld via `Opret` of `Tapret` in de Witness Transaction, waardoor de verbruikte zegels worden gesloten en de nieuwe zegels worden gedefinieerd.


Technisch gesproken wordt de **BundleId** die wordt ingevoegd in het MPC-blad verkregen uit een Hash met tags die wordt toegepast op de strikte serialisatie van het *InputMap* veld van de bundel:


```txt
BundleId = SHA256( SHA256(bundle_tag) || SHA256(bundle_tag) || InputMap )
```


Waarbij `bundle_tag = urn:lnp-bp:RGB:bundle#2024-02-03` bijvoorbeeld.


De *InputMap* is een datastructuur die voor elke invoer `i` van de voorbeeldtransactie de verwijzing naar de *OpId* van het overeenkomstige State Transition opsomt. Bijvoorbeeld:


```txt
InputMap =
N               input_0    OpId(input_0)    input_1    OpId(input_1)   ...    input_N-1  OpId(input_N-1)
|____________________| |_________||______________| |_________||______________|       |__________||_______________|
16-bit Little Endian   32-bit LE   32-byte hash
|_________________________| |_________________________|  ...  |___________________________|

MapElement1                MapElement2                       MapElementN
```




- `N` is het totale aantal items in de transactie die verwijzen naar een `OpId`;
- opId(input_j)` is de operatie-identifier van een van de staatsovergangen in de bundel.


Door slechts één keer en op een geordende manier naar elke invoer te verwijzen, voorkomen we dat hetzelfde Seal twee keer wordt uitgegeven in twee gelijktijdige toestandsovergangen.


### Staat genereren en actieve staat


State Transitions kunnen daarom gebruikt worden om Ownership van een goed over te dragen van de ene persoon naar de andere. Dit zijn echter niet de enige mogelijke operaties in het RGB protocol. Het protocol definieert drie **Contract operaties**:




- **State Transition**;
- **Genesis**;
- State **Extension**.


Hiervan worden **Genesis** en **State Extension** soms "*State Generation Operations*" genoemd, omdat ze nieuwe toestanden creëren zonder er meteen een te sluiten. Dit is een zeer belangrijk punt: **Genesis** en **State Extension** gaan niet over het sluiten van een Seal. In plaats daarvan definiëren ze een nieuwe Seal, die dan uitgegeven moet worden door een volgende **State Transition** om echt gevalideerd te worden in de Blockchain geschiedenis.


![RGB-Bitcoin](assets/en/064.webp)


De **Actieve toestand** van een Contract wordt vaak gedefinieerd als de verzameling laatste toestanden die het resultaat zijn van de geschiedenis (de DAG) van transacties, beginnend met de Genesis en volgend op alle ankers in de Bitcoin Blockchain. Alle oude toestanden die al verouderd zijn (d.w.z. verbonden met verbruikte UTXO's) worden niet langer als actief beschouwd, maar blijven essentieel voor het controleren van de consistentie van de historie.


### Genesis


De Genesis is het startpunt van elke RGB Contract. Het wordt aangemaakt door de Contract verstrekker en definieert de initiële parameters, in overeenstemming met de **Schema**. In het geval van een RGB token kan de Genesis bijvoorbeeld specificeren:




- Het aantal tokens dat oorspronkelijk is aangemaakt en hun eigenaren;
- Totaal mogelijk uitgifteplafond;
- Eventuele regels voor heruitgifte en welke deelnemers in aanmerking komen.


Omdat het de eerste transactie in de Contract is, verwijst de Genesis niet naar een vorige status, noch sluit het een Seal. Om in de geschiedenis te verschijnen en gevalideerd te worden, moet de Genesis echter **verbruikt** (gesloten) worden door een eerste State Transition (vaak een scan/auto-uitgave transactie naar de uitgever zelf, of de initiële distributie naar gebruikers).


### State Extension


**State Extensions** bieden een originele functie voor slimme contracten. Ze maken het mogelijk om Redeem bepaalde digitale rechten (*Valencies*), voorzien in de Contract definitie, te Seal sluiten zonder de Seal onmiddellijk te sluiten. Meestal betreft dit:




- Gedistribueerde token problemen;
- Mechanismen voor activaswaps;
- Voorwaardelijke heruitgaven (die de vernietiging van andere activa, enz. kunnen inhouden).


Technisch gesproken verwijst een State Extension naar een *Redeem* (een bepaald type RGB invoer) die overeenkomt met een eerder gedefinieerde *Valency* (bijvoorbeeld in Genesis of een andere State Transition). Het definieert een nieuwe Seal, beschikbaar voor de persoon of aandoening die ervan profiteert. Om deze Seal effectief te laten worden, moet hij worden uitgegeven door een volgende State Transition.


![RGB-Bitcoin](assets/en/065.webp)


Bijvoorbeeld: de Genesis creëert een recht van uitgifte (*Valency*). Dit kan worden uitgeoefend door een bevoegde actor, die vervolgens een State Extension bouwt:




- Het verwijst naar de Valency (Redeem);
- Het creëert een nieuwe *Assignment* (nieuwe *Owned State* gegevens) die naar een UTXO wijst;
- Een toekomstige State Transition, uitgegeven door de eigenaar van deze nieuwe UTXO, zal de nieuw uitgegeven tokens daadwerkelijk overdragen of verdelen.


### Onderdelen van een Contract Operation


Ik wil nu in detail kijken naar elk van de samenstellende Elements van een **Contract Operation** in RGB. Een Contract Operation is de actie die de toestand van een Contract wijzigt en die aan de kant van de client op deterministische wijze wordt gevalideerd door de legitieme ontvanger. We zullen in het bijzonder zien hoe de Contract Operation rekening houdt met enerzijds de **oude toestand** van de Contract, en anderzijds de definitie van een **nieuwe toestand**.


```txt
+---------------------------------------------------------------------------------------------------------------------+
|  Contract Operation                                                                                                 |
|                                                                                                                     |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|  | Ffv |     | ContractId | SchemaId |      | TransitionType | ExtensionType |      | Testnet |     | AltLayers1 |  |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Metadata                                      |  | Global State                                               |  |
|  |                                               |  | +----------------------------------+                       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  | |          Structured Data            |       |  | | |  GlobalStateType  | |  Data  | |     ...     ...       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  |                                               |  | +----------------------------------+                       |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|                                                                                                                     +---------> OpId |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|  | Inputs                                        |  | Assignments                                                |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #1                                  | |  | | Assignment #1                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ + ---------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #2                                  | |  | | Assignment #2                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  |       ...           ...          ...          |  |     ...          ...             ...                       |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Redeems                                       |  | Valencies                                                  |  |
|  |                                               |  |                                                            |  |
|  | +------------------------------+              |  |                                                            |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
| OpId +--------------> PrevOpId | | ValencyType | |  ...   ...   |  |  | ValencyType |  | ValencyType |         ...              |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
|  | +------------------------------+              |  |                                                            |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |

+---------------------------------------------------------------------------------------------------------------------+
```


Als we naar het bovenstaande diagram kijken, zien we dat een Contract Operation Elements bevat die verwijst naar de **Nieuwe staat** en andere die verwijst naar de bijgewerkte **Oude staat**.


De Elements van de **Nieuwe Staat** zijn:




- **Opdrachten**, waarin zijn gedefinieerd:
 - De **Seal Definition**;
 - De **Owned State**.
- De **Global State**, die kan worden aangepast of verrijkt;
- **Valenties**, mogelijk gedefinieerd in een State Transition of Genesis.


Naar de **Old State** wordt verwezen via:




- **Inputs**, die wijzen naar *Assignments* van vorige toestandsovergangen (niet aanwezig in Genesis);
- **Terugbetalingen**, die verwijzen naar eerder gedefinieerde valenties (alleen in uitbreidingen van staten).


Daarnaast bevat een Contract Operation meer algemene velden die specifiek zijn voor de operatie:




- `ffv` (*Snel vooruit versie*): 2-byte geheel getal dat de Contract versie aangeeft;
- `transitionType` of `ExtensionType`: 16-bits geheel getal dat het Overgangs- of Uitbreidingstype specificeert, volgens Business Logic;
- `ContractId`: 32-bytes getal dat verwijst naar de *OpId* van de Contract Genesis. Opgenomen in Overgangen en Uitbreidingen, maar niet in Genesis;
- schemaId: alleen aanwezig in Genesis, dit is de 32-bytes Hash die de structuur (*Schema*) van de Contract weergeeft;
- `Testnet`: Booleaans die aangeeft of u zich op het Testnet of Mainnet netwerk bevindt. Alleen Genesis;
- `altlayers1`: variabele die het alternatieve Layer (Sidechain of ander) aangeeft dat gebruikt is voor Anchor gegevens in aanvulling op Bitcoin. Alleen aanwezig in Genesis;
- `metadata`: veld dat tijdelijke informatie kan opslaan, handig voor het valideren van een complexe Contract, maar dat niet mag worden opgenomen in de uiteindelijke statusgeschiedenis.


Tenslotte worden al deze velden samengevoegd door een aangepast hashing proces, om een unieke vingerafdruk te produceren, de `OpId`. Deze `OpId` wordt dan geïntegreerd in de Transition Bundle, waardoor het kan worden geverifieerd en gevalideerd binnen het protocol.


Elke *Contract Operation* wordt daarom geïdentificeerd door een Hash van 32 bytes met de naam `OpId`. Deze Hash wordt berekend door een SHA256 Hash van alle Elements waaruit de operatie bestaat. Met andere woorden, elke *Contract Operation* heeft zijn eigen cryptografische Commitment, die alle gegevens bevat die nodig zijn om de authenticiteit en consistentie van de operatie te verifiëren.


Een RGB Contract wordt dan geïdentificeerd door een `ContractId`, afgeleid van de Genesis `OpId` (aangezien er geen pre-Genesis bewerking is). Concreet nemen we de Genesis `OpId`, keren de byte volgorde om en passen een Base58 codering toe. Deze codering maakt de `ContractId` eenvoudiger te hanteren en te herkennen.

### Methoden en regels voor statusupdates


De **Contract State** vertegenwoordigt de set informatie die het RGB protocol moet bijhouden voor een bepaalde Contract. Deze bestaat uit:




- Een enkele **Global State**: dit is het openbare, globale deel van de Contract, zichtbaar voor iedereen;
- Een of meer **Eigen Staten**: elke Owned State is geassocieerd met een unieke Seal (en dus een UTXO op Bitcoin). Er wordt onderscheid gemaakt tussen:
    - De **publieke** staten,
    - De **private** staten in eigendom.


![RGB-Bitcoin](assets/en/066.webp)


De *Global State* is direct opgenomen in de *Contract Operation* als een enkel blok. De *Owned States* zijn gedefinieerd in elke *Assignment*, naast de *Seal Definition*.


Een belangrijk kenmerk van RGB is de manier waarop de Global State en Eigen Staten worden gewijzigd. Er zijn over het algemeen twee soorten gedrag:




- **Mutable**: wanneer een toestandselement wordt beschreven als muteerbaar, vervangt elke nieuwe operatie de vorige toestand door een nieuwe toestand. De oude gegevens worden dan als verouderd beschouwd;
- **Accumuleren**: wanneer een toestandselement is gedefinieerd als accumuleren, voegt elke nieuwe bewerking nieuwe informatie toe aan de vorige toestand, zonder deze te overschrijven. Het resultaat is een soort geaccumuleerde geschiedenis.


Als een toestandselement in de Contract niet gedefinieerd is als muteerbaar of cumulatief, blijft dit element leeg voor volgende bewerkingen (met andere woorden, er zijn geen nieuwe versies voor dit veld). Het is de Contract Schema (d.w.z. de gecodeerde Business Logic) die bepaalt of een toestand (Globaal of Eigendom) muteerbaar, cumulatief of vast is. Als de Genesis eenmaal is gedefinieerd, kunnen deze eigenschappen alleen worden gewijzigd als de Contract dat zelf toestaat, bijvoorbeeld via een specifieke State Extension.


De tabel hieronder laat zien hoe elk type Contract Operation de Global State en Owned State kan manipuleren (of niet):


|                              | Genesis | State Extension | State Transition |
| ---------------------------- |:-----: |:-------------: |:--------------: |
| **Addition of Global State** |    +    |        -        |        +         |
| **Mutation of Global State** |   n/a   |        -        |        +         |
| **Addition of Owned State**  |    +    |        -        |        +         |
| **Mutation of Owned State**  |   n/a   |       No        |        +         |
| **Addition of Valencies**    |    +    |        +        |        +         |


**`+`**: actie mogelijk als de Contract's Schema dit toestaan.


**`-`**: de bewerking moet worden bevestigd door een volgende State Transition (de State Extension alleen sluit de Single-Use Seal niet).


Daarnaast kunnen de temporele reikwijdte en updaterechten van elk type gegevens worden onderscheiden in de volgende tabel:


|                        | Metadata                                | Global State                                     | Owned State                                                                                              |
| ---------------------- | --------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| **Scope**              | Defined for a single Contract Operation | Defined globally for the contract                | Defined for each seal (*Assignment*)                                                                     |
| **Who can update it?** | Non-updatable (ephemeral data)          | Operation issued by actors (issuer, etc.)        | Depends on the legitimate holder who owns the seal (the one who can spend it in a following transaction) |
| **Temporal Scope**     | Only for the current operation          | State is established at the end of the operation | State is defined before the operation (by the *Seal Definition* of the previous operation)               |


### Global State


De Global State wordt vaak omschreven als "nobody owns, everybody knows". Het bevat algemene informatie over de Contract, die openbaar zichtbaar is. Bijvoorbeeld, in een token-uitgevende Contract, bevat het mogelijk:




- De ticker (symbolische afkorting van de token): `ticker`;
- De volledige naam van de token: `naam`;
- Precisie (aantal decimale plaatsen): `precisie`;
- Oorspronkelijke aanbieding (en/of maximale token limiet): `issuedSupply`;
- Uitgiftedatum: `aangemaakt`;
- Juridische gegevens of andere openbare informatie: `data`.


Deze Global State kan op openbare bronnen geplaatst worden (websites, IPFS, Nostr, Torrent, enz.) en verspreid worden onder de gemeenschap. Ook de economische prikkel (de noodzaak om deze tokens te bewaren en over te dragen, etc.) drijft Contract gebruikers er natuurlijk toe om deze gegevens zelf te onderhouden en te verspreiden.


### Opdrachten


De *Assignment* is de basisstructuur voor het definiëren:




- De Seal (*Seal Definition*), die verwijst naar een specifieke UTXO;
- De *Owned State*, d.w.z. de eigenschap of gegevens geassocieerd met deze Seal.


Een *Assignment* kan worden gezien als de analogie van een Bitcoin transactie-uitgang, maar met meer flexibiliteit. Hierin ligt de logica van eigendomsoverdracht: de *Assignment* associeert een bepaald type goed of recht (`AssignmentType`) met een Seal. Wie de private sleutel bezit van de UTXO die gelinkt is aan deze Seal (of wie deze UTXO kan uitgeven) wordt beschouwd als de eigenaar van deze *Owned State*.


Een van de sterke punten van RGB is de mogelijkheid om de *Seal Definition* en *Owned State* velden naar believen te *openbaaren* of te verbergen (*verbergen*). Dit biedt een krachtige combinatie van vertrouwelijkheid en selectiviteit. Je kunt bijvoorbeeld bewijzen dat een overgang geldig is zonder alle gegevens vrij te geven, door de geopenbaarde versie te verstrekken aan degene die de overgang moet valideren, terwijl derden alleen de verborgen versie zien (een Hash). In de praktijk wordt de `OpId` van een overgang altijd berekend uit de *verborgen* gegevens.


![RGB-Bitcoin](assets/en/067.webp)


#### Seal Definition


De *Seal Definition* heeft in zijn onthulde vorm vier basisvelden: `txptr`, `vout`, `blinding` en `method`:




- **txptr**: dit is een verwijzing naar een UTXO op Bitcoin:
    - In het geval van een **Genesis Seal**, verwijst het direct naar een bestaande UTXO (degene die geassocieerd is met de Genesis);
    - In het geval van een **Graph Seal**, kunnen we hebben:
        - Een eenvoudige `txid`, als deze verwijst naar een specifieke UTXO,
        - Of een `WitnessTx`, die een zelfverwijzing aangeeft: de Seal wijst naar de transactie zelf. Dit is vooral handig als er geen externe UTXO beschikbaar is, bijvoorbeeld bij Lightning channel opening transacties, of als de ontvanger geen UTXO heeft.
- **vout**: het uitvoernummer van de transactie aangegeven door `txptr`. Alleen aanwezig voor een standaard Graph Seal (niet voor `WitnessTx`);
- **blindering**: een willekeurig getal van 8 bytes, om de vertrouwelijkheid te versterken en brute force pogingen op de identiteit van de UTXO te voorkomen;
- **methode**: geeft de gebruikte verankeringsmethode aan (`Tapret` of `Opret`).


De *verborgen* vorm van de Seal Definition is een SHA256 Hash (getagd) van de aaneenschakeling van deze 4 velden, met een tag specifiek voor RGB.


![RGB-Bitcoin](assets/en/068.webp)


#### Eigendom van staten


De tweede component van *Assignment* is de Owned State. In tegenstelling tot de Global State, kan deze bestaan in publieke of private vorm:




- **Publieke Owned State**: iedereen kent de gegevens die geassocieerd zijn met de Seal. Bijvoorbeeld een openbare afbeelding;
- **Privé Owned State**: de gegevens zijn verborgen, alleen bekend bij de eigenaar (en eventueel de validator). Bijvoorbeeld het aantal tokens in bezit.


RGB definieert vier mogelijke toestandsvormen (*StateTypes*) voor een Owned State:




- **Declaratief**: bevat geen numerieke gegevens, alleen een declaratief recht (bijv. stemrecht). De verborgen en onthulde vormen zijn identiek;
- **Fungible**: vertegenwoordigt een fungibele hoeveelheid (zoals tokens). In onthulde vorm hebben we `bedrag` en `blindering`. In verborgen vorm hebben we een enkele *Pedersen commitment* die het bedrag en de blindering verbergt;
- **Structured**: slaat gestructureerde gegevens op (tot 64 kB). In geopenbaarde vorm is het de blob met gegevens. In verborgen vorm is het een Hash van deze blob:


```txt
SHA-256(SHA-256(tag_data) || SHA-256(tag_data) || blob)
```


Bijvoorbeeld:


```txt
tag_data = urn:lnp-bp:rgb:state-data#2024-02-12
```




- **Attachments**: koppelt een bestand (audio, afbeelding, binair, enz.) aan de Owned State, waarbij het Hash `file_hash`, het MIME type `media type` en een cryptografische salt `salt` worden opgeslagen. Het bestand zelf wordt elders gehost. In verborgen vorm is het een Hash getagd met de drie voorgaande gegevensitems:


```txt
SHA-256(SHA-256(tag_attachment) || SHA-256(tag_attachment) || file_hash || media_type || salt)
```


Bijvoorbeeld:


```txt
tag_attachment = urn:rgb:state-attach#2024-02-12
```


Samengevat zijn hier de 4 mogelijke toestandsvormen in de openbare en verborgen vorm:


```txt
State                      Concealed form                              Revealed form

+---------------------------------------------------------------------------------------------------------

+--------------------------------------------------------------------------------+
|                                                                                |
Declarative        |                              < void >                                          |
|                                                                                |
+--------------------------------------------------------------------------------+

+---------------------------------------------------------------------------------------------------------

+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------+ +----------+       |
Fungible           | | Pedersen Commitement | | <========== |         | Amount | | Blinding |       |
| +----------------------+ |             |         +--------+ +----------+       |
+--------------------------+             +---------------------------------------+

+---------------------------------------------------------------------------------------------------------

+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------------------+        |
Structured         | |     Tagged Hash      | | <========== |         |     Data Blob      |        |
| +----------------------+ |             |         +--------------------+        |
+--------------------------+             +---------------------------------------+

+---------------------------------------------------------------------------------------------------------

+--------------------------+             +---------------------------------------+
| +----------------------+ |             | +-----------+ +------------+ +------+ |
Attachments        | |     Tagged Hash      | | <========== | | File Hash | | Media Type | | Salt | |
| +----------------------+ |             | +-----------+ +------------+ +------+ |

+--------------------------+             +---------------------------------------+

```



| **Element**     | **Declarative** | **Fungible**                      | **Structured**       | **Attachments**        |
| --------------- | --------------- | --------------------------------- | -------------------- | ---------------------- |
| **Data**        | None            | Signed or unsigned 64-bit integer | Any strict data type | Any file               |
| **Info Type**   | None            | Signed or unsigned                | Strict types         | MIME Type              |
| **Privacy**     | Not required    | Pedersen commitment               | Hash with blinding   | Hashed file identifier |
| **Size Limits** | N/A             | 256 bytes                         | Up to 64 KB          | Up to ~500 GB          |


### Ingangen


De ingangen van een *Contract Operation* verwijzen naar de *toewijzingen* die in deze nieuwe bewerking worden uitgegeven. Een ingang geeft aan:




- `prevOpId`: de identifier (`OpId`) van de vorige operatie waar de *Assignment* zich bevond;
- `assignmentType`: het type *Assignment* (bijvoorbeeld `assetOwner` voor een token);
- `Index`: de index van de *Assignment* in de lijst die hoort bij de vorige `OpId`, bepaald na een lexicografische sortering van de verborgen zegels.


Inputs verschijnen nooit in Genesis, omdat er geen eerdere Assignments zijn. Ze verschijnen ook niet in Statenuitbreidingen (omdat Statenuitbreidingen geen zegels sluiten, maar nieuwe zegels herdefiniëren op basis van Valencies).


Wanneer we Eigen Staten van het type `Fungible` hebben, controleert de validatielogica (via het AluVM script dat in de Schema wordt geleverd) de consistentie van de sommen: de som van de binnenkomende tokens (*Inputs*) moet gelijk zijn aan de som van de uitgaande tokens (in de nieuwe *Assignments*).


### Metagegevens


Het **Metadata** veld kan tot 64 KiB groot zijn en wordt gebruikt om tijdelijke gegevens op te slaan die nuttig zijn voor validatie, maar niet geïntegreerd zijn in de permanente toestand van de Contract. Bijvoorbeeld, tussenliggende berekeningsvariabelen voor complexe scripts kunnen hier worden opgeslagen. Het is niet de bedoeling dat deze ruimte wordt opgeslagen in de globale geschiedenis, daarom valt het buiten het bereik van Owned States of Global State.


### Valenties


**Valencies** zijn een origineel RGB protocol mechanisme. Ze kunnen gevonden worden in Genesis, State Transitions of State Extensions. Ze vertegenwoordigen numerieke rechten die kunnen worden geactiveerd door een State Extension (via *Redeems*), en vervolgens gefinaliseerd door een volgende Transitie. Elke Valency wordt geïdentificeerd door een `ValencyType` (16 bits). De semantiek (heruitgifterecht, token-ruil, verbrandingsrecht, enz.) wordt gedefinieerd in de Schema.


Concreet zouden we ons kunnen voorstellen dat een Genesis een "recht op heruitgifte" Valency definieert. Een State Extension zal het consumeren (*Redeem*) als aan bepaalde voorwaarden is voldaan, om een nieuwe hoeveelheid tokens te introduceren. Vervolgens kan een State Transition, afkomstig van de houder van de zo gecreëerde Seal, deze nieuwe tokens overdragen.


### Verlost


Terugbetalingen zijn het Valency equivalent van ingangen voor toewijzingen. Ze verschijnen alleen in Staatsuitbreidingen, omdat hier een eerder gedefinieerde Valency wordt geactiveerd. Een Redeem bestaat uit twee velden:




- `PrevOpId`: de `OpId` van de operatie waar de Valency werd gespecificeerd;
- `ValencyType`: het type Valency dat je wilt activeren (elk `ValencyType` kan maar één keer gebruikt worden door State Extension).


Voorbeeld: een Redeem kan overeenkomen met een CoinSwap uitvoering, afhankelijk van wat er in de Valency is gecodeerd.


### RGB statuskenmerken


We gaan nu kijken naar verschillende fundamentele toestandskenmerken in RGB. In het bijzonder zullen we kijken naar:




- Het **Strict Type System**, dat een precieze en getypeerde organisatie van gegevens oplegt;
- Het belang van het scheiden van **validatie** en **Ownership**;
- Het **consensus evolutie** systeem in RGB, dat de begrippen *fast-forward* en *push-back* bevat.


Houd er zoals altijd rekening mee dat alles wat te maken heeft met de Contract status gevalideerd wordt aan de kant van de cliënt volgens de consensusregels die in het protocol staan, en waarvan de uiteindelijke cryptografische referentie verankerd is in Bitcoin transacties.


#### Strikt typesysteem


RGB gebruikt een *Strict Type System* en een deterministische serialisatiemodus (*Strict Encoding*). Deze organisatie is ontworpen om perfecte reproduceerbaarheid en precisie te garanderen in de definitie, behandeling en validatie van Contract gegevens.


In veel programmeeromgevingen (JSON, YAML...) kan de datastructuur flexibel zijn, zelfs te permissief. In RGB daarentegen worden de Structuur en Types van elk veld gedefinieerd met expliciete beperkingen. Bijvoorbeeld:




- Elke variabele heeft een specifiek type (bijvoorbeeld een 8-bits unsigned integer `u8`, of een 16-bits signed integer, enzovoort);
- Types kunnen worden samengesteld (geneste types). Dit betekent dat je een type kunt definiëren op basis van andere types (bijvoorbeeld een geaggregeerd type dat een `u8` veld, een `bool` veld, enz. bevat);
- Verzamelingen kunnen ook gespecificeerd worden: lijsten (*list*), sets (*set*) of woordenboeken (*map*), met een deterministische volgorde;
- Elk veld is begrensd (*ondergrens* / *bovengrens*). We leggen ook beperkingen op aan het aantal Elements in verzamelingen (containment);
- Gegevens worden per byte uitgelijnd en serialisatie is strikt gedefinieerd en ondubbelzinnig.


Dankzij dit strikte coderingsprotocol:




- De volgorde van de velden is altijd hetzelfde, ongeacht de implementatie of de gebruikte programmeertaal;
- De hashes die berekend zijn op dezelfde dataset zijn daarom reproduceerbaar en identiek (strikt deterministische *commitments*);
- Grenzen voorkomen ongecontroleerde groei in gegevensgrootte (bijv. te veel velden);
- Deze vorm van codering vergemakkelijkt cryptografische verificatie, omdat elke deelnemer precies weet hoe de gegevens moeten worden geserialiseerd en Hash.


In de praktijk worden de structuur (*Schema*) en de resulterende code (*Interface* en bijbehorende logica) gecompileerd. Er wordt een beschrijvende taal gebruikt om de Contract te definiëren (typen, velden, regels) en generate een strikt binair formaat. Bij het compileren is het resultaat:




- Een *geheugenindeling* voor elk veld;
- Semantische identifiers (die aangeven of het veranderen van een variabelenaam invloed heeft op de logica, zelfs als de geheugenstructuur hetzelfde blijft).


Het strikte typesysteem maakt ook nauwkeurige controle van wijzigingen mogelijk: elke wijziging in de structuur (zelfs een wijziging in de veldnaam) is detecteerbaar en kan leiden tot een wijziging in de totale footprint.


Tenslotte produceert elke compilatie een vingerafdruk, een cryptografische identificatie die de exacte versie van de code (gegevens, regels, validatie) bevestigt. Bijvoorbeeld, een identifier van de vorm:


```txt
BEiLYE-am9WhTW1-oK8cpvw4-FEMtzMrf-mKocuGZn-qWK6YF#ginger-parking-nirvana
```


Dit maakt het mogelijk om consensus- of implementatie-updates te beheren, terwijl gedetailleerde traceerbaarheid van de in het netwerk gebruikte versies wordt gegarandeerd.


Om te voorkomen dat de toestand van een RGB Contract te omslachtig wordt om te valideren aan de cliëntzijde, legt een consensusregel een maximale grootte op van `2^16` bytes (64 Kio) voor alle gegevens die betrokken zijn bij validatieberekeningen. Dit geldt voor elke variabele of structuur: niet meer dan 65536 bytes, of het equivalent in getallen (32768 16-bit gehele getallen, etc.). Dit geldt ook voor verzamelingen (lijsten, sets, maps), die niet groter mogen zijn dan `2^16` Elements.


Deze limiet garandeert:




- Bepaalt de maximale grootte van gegevens die gemanipuleerd worden tijdens een State Transition;
- Compatibiliteit met de virtuele machine (*AluVM*) die wordt gebruikt om de validatiescripts uit te voeren.


#### Het validatie != Ownership paradigma


Een van de belangrijkste innovaties van RGB is de strikte scheiding tussen twee concepten:




- **Validatie**: controleren of een State Transition de regels van de Contract respecteert (Business Logic, geschiedenis, enz.);
- De **Ownership** (Ownership, of controle): het feit dat je de Bitcoin UTXO bezit, waardoor de Single-Use Seal kan worden uitgegeven (of gesloten), en dus de State Transition kan plaatsvinden.


**Validatie** vindt plaats op het niveau van de RGB software stack (bibliotheken, *commitments* protocol, etc.). De rol hiervan is te verzekeren dat de interne regels van de Contract (bedragen, toestemmingen, enz.) worden gerespecteerd. Waarnemers of andere deelnemers kunnen ook de datageschiedenis valideren.


**Ownership** daarentegen vertrouwt volledig op de beveiliging van Bitcoin. Het bezitten van de private sleutel van een UTXO betekent het beheersen van de mogelijkheid om een nieuwe transitie te starten (het sluiten van de Single-Use Seal). Dus, zelfs als iemand de gegevens kan zien of valideren, kunnen ze de toestand niet veranderen als ze de betreffende UTXO niet bezitten.


![RGB-Bitcoin](assets/en/069.webp)


Deze benadering beperkt de klassieke kwetsbaarheden die we tegenkomen in complexere blockchains (waar alle code van een Smart contract openbaar is en door iedereen gewijzigd kan worden, wat soms tot hacks heeft geleid). Op RGB kan een aanvaller niet zomaar interageren met de On-Chain toestand, omdat het recht om te handelen op de toestand (*Ownership*) beschermd wordt door Bitcoin Layer.


Bovendien laat deze ontkoppeling de RGB op natuurlijke wijze integreren met de Lightning Network. Lightning kanalen kunnen gebruikt worden om RGB activa te activeren en te verplaatsen zonder telkens On-Chain *commitments* te activeren. In latere hoofdstukken van deze cursus gaan we dieper in op deze integratie van RGB in Lightning.


#### Consensus ontwikkelingen in RGB


Naast het versiebeheer van semantische code bevat RGB een systeem om de consensusregels van een Contract in de loop van de tijd te evolueren of bij te werken. Er zijn twee hoofdvormen van evolutie:




- **Snel vooruit**
- **Push-back** (in het Frans)


Een fast-forward treedt op wanneer een voorheen ongeldige regel geldig wordt. Bijvoorbeeld, als de Contract evolueert om een nieuw type `AssignmentType` of een nieuw veld toe te staan:




- Dit is niet te vergelijken met een klassieke Blockchain hardfork, omdat RGB in Client-side Validation werkt en de algehele compatibiliteit van Blockchain niet beïnvloedt;
- Praktisch gezien wordt dit type verandering aangegeven door het `Ffv` (*fast-forward versie*) veld in de Contract Operation;
- De huidige houders worden niet benadeeld: hun status blijft geldig;
- Nieuwe begunstigden (of nieuwe gebruikers) daarentegen moeten hun software (hun Wallet) bijwerken om de nieuwe regels te herkennen.


Een push-back betekent dat een voorheen geldige regel ongeldig wordt. Het is daarom een "verharding" van de regels, maar strikt genomen geen softfork:




- Bestaande houders kunnen worden beïnvloed (zij kunnen te maken krijgen met activa die verouderd of ongeldig zijn in de nieuwe versie);
- We kunnen stellen dat we in feite een nieuw protocol creëren: wie de nieuwe regel aanneemt, wijkt af van de oude;
- De uitgever kan besluiten om activa opnieuw uit te geven in dit nieuwe protocol, waardoor gebruikers gedwongen worden om twee aparte wallets te onderhouden (één voor het oude protocol, de andere voor het nieuwe), als ze beide versies willen beheren.


In dit hoofdstuk over RGB Contract operaties, hebben we de fundamentele principes die aan dit protocol ten grondslag liggen verkend. Zoals je gemerkt zult hebben, vereist de inherente complexiteit van het RGB protocol het gebruik van veel technische termen. Dus in het volgende hoofdstuk geef ik je een verklarende woordenlijst die alle concepten uit dit eerste theoretische deel samenvat, met definities van alle technische termen die met RGB te maken hebben. Daarna, in het volgende deel, zullen we een praktische blik werpen op de definitie en implementatie van RGB contracten.


## Woordenlijst RGB


<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>


Als je terug moet komen op deze korte woordenlijst van belangrijke technische termen die gebruikt worden in de RGB wereld (alfabetisch gerangschikt), zul je het handig vinden. Dit hoofdstuk is niet essentieel als je alles al begrepen hebt wat we in het eerste deel behandeld hebben.


#### AluVM


De afkorting AluVM staat voor "_Algorithmic logic unit Virtual Machine_", een op registers gebaseerde virtuele machine ontworpen voor Smart contract validatie en gedistribueerd computergebruik. Het wordt gebruikt (maar niet exclusief gereserveerd) voor de validatie van RGB contracten. Scripts of bewerkingen in een RGB Contract kunnen dus worden uitgevoerd in de AluVM omgeving.


Voor meer informatie: [AluVM officiële website](https://www.AluVM.org/)


#### Anchor


Een Anchor vertegenwoordigt een set client-side gegevens die gebruikt worden om de opname van een unieke _commitment_ in een transactie aan te tonen. In het RGB protocol bestaat een Anchor uit de volgende Elements:




- De Bitcoin transactie-identificatiecode (txid) van de **Witness Transaction**;
- De **Multi Protocol Commitment (MPC)**;
- De **Deterministic Bitcoin Commitment (DBC)**;
- Het **Extra Transactie Bewijs (ETP)** als het **Tapret** Commitment mechanisme wordt gebruikt (zie de sectie gewijd aan dit model).


Een Anchor dient dus om een verifieerbare link te leggen tussen een specifieke Bitcoin transactie en privégegevens die door het RGB protocol gevalideerd zijn. Het garandeert dat deze gegevens inderdaad in de Blockchain zijn opgenomen, zonder dat de exacte inhoud openbaar wordt gemaakt.


#### Assignment


In de logica van RGB is een Assignment het equivalent van een transactie-uitgang die bepaalde eigenschappen in de toestand van een Contract wijzigt, bijwerkt of creëert. Een Assignment bestaat uit twee Elements:




- A **Seal Definition** (verwijzing naar een specifieke UTXO);
- Een **Owned State** (gegevens die de staat beschrijven die bij deze nieuwe eigenaar hoort).


Een Assignment geeft dus aan dat een deel van de staat (bijvoorbeeld een activum) nu is toegewezen aan een bepaalde houder, geïdentificeerd via een Single-Use Seal gekoppeld aan een UTXO.


#### Business Logic


De Business Logic groepeert alle regels en interne operaties van een Contract, beschreven door de **Schema** (d.w.z. de structuur van de Contract zelf). Het dicteert hoe de toestand van de Contract kan evolueren, en onder welke condities.


#### Client-side Validation


Client-side Validation verwijst naar het proces waarbij elke partij (cliënt) een set van privé uitgewisselde gegevens verifieert volgens de regels van een protocol. In het geval van RGB worden deze uitgewisselde gegevens gegroepeerd in zogenaamde **consignaties**. In tegenstelling tot het Bitcoin protocol, dat vereist dat alle transacties On-Chain gepubliceerd worden, staat RGB alleen toe dat _commitments_ (verankerd in Bitcoin) publiekelijk opgeslagen worden, terwijl de essentiële Contract informatie (overgangen, attestaties, bewijzen) off-chain blijft, alleen gedeeld tussen de betrokken gebruikers.


#### Commitment


Een Commitment (in cryptografische zin) is een wiskundig object, aangeduid met `C`, deterministisch afgeleid van een bewerking op gestructureerde gegevens `m` (het bericht) en een willekeurige waarde `r`. We schrijven:


$$
C = \text{commit}(m, r)
$$


Dit mechanisme bestaat uit twee hoofdbewerkingen:




- **Commit**: een cryptografische functie wordt toegepast op een bericht `m` en een willekeurig getal `r` om `C` te produceren;
- **Verify**: we gebruiken `C`, het `m` bericht en de `r` waarde om te controleren of deze Commitment correct is. De functie retourneert `True` of `False`.


Een Commitment moet twee eigenschappen respecteren:




- **Binding**: het moet onmogelijk zijn om twee verschillende berichten te vinden die dezelfde `C` produceren:


$$
m': \, | \,: m' \neq m \quad \text{and} \quad r': \, | \,: r' \neq r \quad
$$


Zoals:


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- **Verbergen**: kennis van `C` mag de inhoud van `m` niet onthullen.


In het RGB protocol wordt een Commitment opgenomen in een Bitcoin transactie om het bestaan van een bepaald stuk informatie op een bepaald moment te bewijzen, zonder de informatie zelf te onthullen.


#### Consignment


Een **Consignment** groepeert de gegevens die tussen de partijen worden uitgewisseld, onderhevig aan Client-side Validation in RGB. Er zijn twee hoofdcategorieën Consignment:




- **Contract Consignment**: geleverd door de *emittent* (Contract emittent), het bevat initialisatie-informatie zoals Schema, Genesis, Interface en Interface Implementation.
- **Consignment**: Geleverd door de betalende partij (*betaler*). Het bevat de hele geschiedenis van toestandsovergangen die leiden tot Terminal Consignment (d.w.z. de uiteindelijke toestand ontvangen door de betaler).


Deze zendingen worden niet openbaar geregistreerd op de Blockchain; ze worden rechtstreeks uitgewisseld tussen de betrokken partijen via het communicatiekanaal van hun keuze.


#### Contract


Een Contract is een set rechten die digitaal wordt uitgevoerd tussen verschillende actoren via het RGB protocol. Het heeft een actieve status en een Business Logic, gedefinieerd door een Schema, die specificeert welke operaties geautoriseerd zijn (overdrachten, uitbreidingen, enz.). De toestand van een Contract, evenals de geldigheidsregels, worden uitgedrukt in de Schema. Op elk gegeven moment evolueert de Contract alleen in overeenstemming met wat is toegestaan door deze Schema en door validatiescripts (die bijvoorbeeld in AluVM worden uitgevoerd).


#### Contract Operation


Een Contract Operation is een Contract statusupdate uitgevoerd volgens Schema regels. De volgende bewerkingen bestaan in RGB:




- **State Transition**;
- **Genesis**;
- State **Extension**.


Elke bewerking wijzigt de toestand door bepaalde gegevens toe te voegen of te vervangen (Global State, Owned State...).


#### Contract Participant


Een Contract Participant is een actor die deelneemt aan operaties met betrekking tot de Contract. In RGB wordt onderscheid gemaakt tussen:




- De uitgever van de Contract, die de Genesis creëert (de oorsprong van de Contract);
- De Contract partijen, d.w.z. de houders van rechten op de staat Contract;
- Publieke partijen, die Staatsuitbreidingen kunnen bouwen als de Contract Valencies biedt die toegankelijk zijn voor het publiek.


#### Contract Rights


Contract Rights verwijzen naar de verschillende rechten die kunnen worden uitgeoefend door degenen die betrokken zijn bij een RGB Contract. Ze vallen uiteen in verschillende categorieën:




- **Ownership-rechten**, geassocieerd met de Ownership van een bepaalde UTXO (via een _Seal Definition_);
- **Uitvoeringsrechten**, d.w.z. de mogelijkheid om een of meer overgangen (State Transitions) te bouwen in overeenstemming met de Schema;
- **Openbare rechten**, wanneer de Schema bepaalde openbare toepassingen toestaat, bijvoorbeeld de creatie van een State Extension via de inwisseling van een Valency.


#### Contract State


De Contract State komt overeen met de huidige toestand van een Contract op een bepaald moment. Het kan bestaan uit zowel openbare als privégegevens, die de toestand van de Contract weergeven. RGB maakt onderscheid tussen:




- De **Global State**, die de openbare eigenschappen van de Contract bevat (ingesteld in Genesis of toegevoegd via geautoriseerde updates);
- **Owned States**, die toebehoren aan specifieke eigenaars, geïdentificeerd door hun UTXO.


#### Deterministic Bitcoin Commitment - DBC


Deterministic Bitcoin Commitment (DBC) is de verzameling regels die gebruikt wordt om aantoonbaar en uniek een _commitment_ te registreren in een Bitcoin transactie. In het RGB protocol zijn er twee hoofdvormen van DBC:




- **Opret**
- **Tapret**


Deze mechanismen definiëren precies hoe de _commitment_ wordt gecodeerd in de uitvoer of structuur van een Bitcoin transactie, om ervoor te zorgen dat deze Commitment deterministisch traceerbaar en verifieerbaar is.


#### Directed Acyclic Graph - DAG


Een DAG (of *Acyclic Guided Graph*) is een cyclusvrije grafiek, die topologische planning mogelijk maakt. Blockchains, zoals de _shards_ van RGB contracten, kunnen worden weergegeven door DAG's.


Voor meer informatie: [Directed Acyclic Graph] (https://en.wikipedia.org/wiki/Directed_acyclic_graph)


#### Graveren


Gravering is een optionele gegevensreeks die opeenvolgende eigenaren van een Contract kunnen invoeren in de geschiedenis van de Contract. Deze functie bestaat bijvoorbeeld in de **RGB21** Interface en maakt het mogelijk herdenkings- of beschrijvende informatie toe te voegen aan de geschiedenis van de Contract.


#### Extra transactiebewijs - ETP


De ETP (*Extra Transaction Proof*) is het deel van de Anchor dat de extra gegevens bevat die nodig zijn om een **Tapret** *Commitment* (in de context van _taproot_) te valideren. Het bevat onder andere de interne publieke sleutel van het Taproot script (_internal PubKey_) en informatie die specifiek is voor de _Script Path Spend_.


#### Genesis


Genesis verwijst naar de verzameling gegevens, bestuurd door een Schema, die de begintoestand vormt van elke Contract in RGB. Het kan vergeleken worden met Bitcoin's _Genesis Block_ concept, of met het Coinbase Transaction concept, maar hier op het _client-side_ en RGB token niveau.


#### Global State


Global State is de verzameling openbare eigenschappen in Contract State. Het is gedefinieerd op Genesis en kan, afhankelijk van de Contract regels, bijgewerkt worden door geautoriseerde overgangen. In tegenstelling tot Staten van Eigendom, behoort het Global State niet toe aan een bepaalde entiteit; het ligt dichter bij een openbaar register binnen het Contract.


#### Interface


De Interface is de verzameling instructies die wordt gebruikt om de binaire gegevens te decoderen die zijn samengesteld in een Schema of in Contract bewerkingen en hun toestanden, om ze leesbaar te maken voor de gebruiker of zijn Wallet. Het fungeert als een Layer interpretatie.


#### Interface Implementation


Interface Implementation is de verzameling declaraties die een **Interface** verbindt met een **Schema**. Het maakt de semantische vertaling door de Interface zelf mogelijk, zodat de ruwe gegevens van een Contract begrepen kunnen worden door de gebruiker of de betrokken software (de wallets).


#### Invoice


Een Invoice heeft de vorm van een URL gecodeerd in [base58] (https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58), die de gegevens bevat die nodig zijn voor de constructie van een **State Transition** (door de betaler). Met andere woorden, het is een Invoice die de tegenpartij (*betaler*) in staat stelt de bijbehorende overgang te creëren om het activum over te dragen of de status van de Contract bij te werken.


#### Lightning Network


De Lightning Network is een gedecentraliseerd netwerk van betaalkanalen (of _staatskanalen_) op Bitcoin, bestaande uit 2/2 multi-handtekening wallets. Het maakt snelle, goedkope _off-chain_ transacties mogelijk, terwijl het vertrouwt op Bitcoin's Layer 1 voor arbitrage (of sluiting) wanneer nodig.


Voor meer informatie over hoe Lightning werkt, raad ik je aan deze andere cursus te volgen:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

#### Multi Protocol Commitment - MPC


Multi Protocol Commitment (MPC) verwijst naar de Merkle Tree structuur die gebruikt wordt in RGB om, binnen een enkele Bitcoin transactie, verschillende **Overgangsbundels** van verschillende contracten op te nemen. Het idee is om verschillende verbintenissen (die mogelijk overeenkomen met verschillende contracten of verschillende activa) te groeperen in een enkel Anchor punt om de bezetting van de blokruimte te optimaliseren.


#### Owned State


Een Owned State is het deel van een Contract State dat ingesloten is in een Assignment en geassocieerd is met een bepaalde houder (via een Single-Use Seal die naar een UTXO wijst). Dit vertegenwoordigt bijvoorbeeld een digitaal actief of een specifiek contractueel recht dat aan die persoon is toegewezen.


#### Ownership


Ownership verwijst naar de mogelijkheid om een UTXO waarnaar een Seal Definition verwijst, te controleren en uit te geven. Wanneer een Owned State is gekoppeld aan een UTXO, heeft de eigenaar van deze UTXO het recht, mogelijk, om de geassocieerde staat over te dragen of te evolueren, volgens de regels van de Contract.


#### Partially Signed Bitcoin Transaction - PSBT


Een PSBT (_Partially Signed Bitcoin Transaction_) is een Bitcoin transactie die nog niet volledig ondertekend is. Het kan gedeeld worden tussen verschillende entiteiten, die elk bepaalde Elements (handtekeningen, scripts...) kunnen toevoegen of verifiëren, totdat de transactie klaar geacht wordt voor On-Chain distributie.


Voor meer informatie: [BIP-0174] (https://github.com/Bitcoin/bips/blob/master/bip-0174.mediawiki)


#### Pedersen commitment


Een Pedersen commitment is een type cryptografische Commitment met de eigenschap **homorf** te zijn met betrekking tot de opteloperatie. Dit betekent dat het mogelijk is om de som van twee toezeggingen te valideren zonder de individuele waarden te onthullen.


Formeel, als:


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


dan:


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Deze eigenschap is bijvoorbeeld handig om de hoeveelheden ingewisselde tokens te verbergen, terwijl de totalen toch gecontroleerd kunnen worden.


Verdere informatie: [Pedersen commitment](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)


#### Redeem


In een State Extension verwijst een Redeem naar de actie van het terugvorderen (of exploiteren) van een eerder aangegeven **Valency**. Omdat een Valency een publiek recht is, staat de Redeem een geautoriseerde deelnemer toe om een specifieke Contract State Extension te claimen.


#### Schema


Een Schema in RGB is een declaratief stuk code dat de verzameling variabelen, regels en Business Logic (*Business Logic*) beschrijft die de werking van een Contract bepalen. De Schema definieert de toestandsstructuur, de toegestane soorten overgangen en de validatievoorwaarden.


#### Seal Definition


De Seal Definition is het deel van een Assignment dat de _verbintenis_ associeert met een UTXO die eigendom is van de nieuwe houder. Met andere woorden, het geeft aan waar de voorwaarde zich bevindt (in welke UTXO), en vestigt Ownership van een actief of recht.


#### Shard


Een Shard vertegenwoordigt een tak in de DAG van de Staatstransitiegeschiedenis van een RGB Contract. Met andere woorden, het is een samenhangende subset van de totale geschiedenis van de Contract, die bijvoorbeeld overeenkomt met de opeenvolging van overgangen die nodig zijn om de geldigheid van een bepaald actief te bewijzen sinds de _Genesis_.


#### Single-Use Seal


Een Single-Use Seal is een cryptografische belofte van Commitment aan een nog onbekend bericht, dat slechts één keer in de toekomst onthuld zal worden en bekend moet zijn bij alle leden van een specifiek publiek. Het doel is om de creatie van meerdere concurrerende toezeggingen voor dezelfde Seal te voorkomen.


#### Stash


De Stash is de verzameling client-side gegevens die een gebruiker opslaat voor een of meer RGB contracten, ten behoeve van validatie (*Client-side Validation*). Dit omvat de transitiegeschiedenis, zendingen, geldigheidsbewijzen, enz. Elke houder bewaart alleen de delen van de geschiedenis die hij nodig heeft (*shards*).


#### State Extension


Een State Extension is een Contract Operation die gebruikt wordt om toestandupdates opnieuw te triggeren door eerder gedeclareerde **Valencies** in te wisselen. Om effectief te zijn, moet een State Extension afgesloten worden door een State Transition (die de uiteindelijke toestand van de Contract bijwerkt).


#### State Transition


State Transition is de bewerking die de toestand van een RGB Contract verandert in een nieuwe toestand. Ze kan Global State en/of Owned State gegevens wijzigen. In de praktijk wordt elke overgang geverifieerd door Schema regels en verankerd in de Bitcoin Blockchain via een _commitment_.


#### Taproot


Verwijst naar Bitcoin's SegWit v1 transactieformaat, geïntroduceerd door [BIP341](https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki) en [BIP342](https://github.com/Bitcoin/bips/blob/master/bip-0342.mediawiki). Taproot verbetert de vertrouwelijkheid en flexibiliteit van scripts, in het bijzonder door transacties compacter te maken en moeilijker van elkaar te onderscheiden.


#### Terminal Consignment - Consignment Endpoint


De Terminal Consignment (of _Consignment Endpoint_) is een *overdracht Consignment* die de uiteindelijke toestand van de Contract bevat, inclusief de State Transition die gemaakt is van de Invoice van de ontvanger (*betaler*). Het is daarom het eindpunt van een overdracht, met de benodigde gegevens om te bewijzen dat Ownership of toestand is overgedragen.


#### Transition Bundle


Een Transition Bundle is een verzameling RGB toestandsovergangen (behorend tot dezelfde Contract) die allemaal bezig zijn met dezelfde ***Witness Transaction*** Bitcoin. Dit maakt het mogelijk om meerdere updates of overdrachten te bundelen in een enkele On-Chain Anchor.


#### UTXO


Een Bitcoin UTXO (*Unspent Transaction Output*) wordt gedefinieerd door de Hash van een transactie en de uitvoerindex (*vout*). Het wordt ook wel eens een _outpoint_ genoemd. In het RGB protocol maakt verwijzing naar een UTXO (via een **Seal Definition**) de locatie mogelijk van de **Owned State**, dat wil zeggen de eigenschap die wordt bewaard op de Blockchain.


#### Valency


Een Valency is een publiek recht dat als zodanig geen opslag in de staat vereist, maar dat kan worden ingewisseld via een **State Extension**. Het is dus een mogelijkheid die open staat voor iedereen (of bepaalde spelers), aangegeven in de logica van de Contract, om op een later tijdstip een bepaalde uitbreiding uit te voeren.


#### Witness Transaction


De Witness Transaction is de Bitcoin transactie die de Single-Use Seal sluit rond een bericht dat een Multi Protocol Commitment (MPC) bevat. Deze transactie spendeert een UTXO of creëert er een, zodat Seal de Commitment gekoppeld aan het RGB protocol. Het fungeert als een On-Chain bewijs dat de toestand op een bepaald tijdstip is ingesteld.


# Programmeren op RGB


<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>


## RGB contracten implementeren


<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>


:::video id=97d81b85-5a82-40a5-b111-7d96be5afd0f:::


In dit hoofdstuk bekijken we hoe een RGB Contract gedefinieerd en geïmplementeerd wordt. We zullen zien wat de componenten van een RGB Contract zijn, wat hun rol is en hoe ze zijn opgebouwd.


### De onderdelen van een RGB Contract


Tot nu toe hebben we het al gehad over de **Genesis**, die het beginpunt vormt van een Contract, en we hebben gezien hoe het past in de logica van een *Contract Operation* en de toestand van het protocol. De volledige definitie van een RGB Contract is echter niet beperkt tot de Genesis alleen: er zijn drie complementaire componenten bij betrokken die samen het hart van de implementatie vormen.


De eerste component heet de **Schema**. Dit is een bestand dat de fundamentele structuur en Business Logic (*Business Logic*) van de Contract beschrijft. Het specificeert de gebruikte gegevenstypen, de validatieregels, de toegestane bewerkingen (bijv. initiële token uitgifte, overdrachten, speciale voorwaarden, enz.


De tweede component is de **Interface**. Deze richt zich op de manier waarop gebruikers (en bij uitbreiding portfoliosoftware) zullen interageren met deze Contract. Het beschrijft de semantiek, d.w.z. de leesbare weergave van de verschillende velden en acties. Dus, terwijl de Schema definieert hoe de Contract technisch werkt, definieert de Interface hoe deze functionaliteiten moeten worden gepresenteerd en weergegeven: namen van methoden, weergave van gegevens, enz.


De derde component is de **Interface Implementation**, die de vorige twee aanvult door als een soort brug te fungeren tussen de Schema en de Interface. Met andere woorden, het associeert de semantiek uitgedrukt door de Interface met de onderliggende regels gedefinieerd in de Schema. Het is deze implementatie die bijvoorbeeld de conversie beheert tussen een parameter die wordt ingevoerd in de Wallet en de binaire structuur die wordt opgelegd door het protocol, of de compilatie van validatieregels in machinetaal.


Deze modulariteit is een interessante eigenschap van RGB, omdat verschillende groepen ontwikkelaars afzonderlijk aan deze aspecten kunnen werken (*Schema*, *Interface*, *Implementatie*), zolang ze de consensusregels van het protocol volgen.


Samengevat bestaat elke Contract uit:




- **Genesis**, dat is de begintoestand van de Contract (en kan worden vergeleken met een speciale transactie die de eerste Ownership van een activum, een recht of een ander parametriseerbaar gegeven definieert);
- **Schema**, die de Business Logic van de Contract beschrijft (gegevenstypen, validatieregels, enzovoort);
- **Interface**, die een semantische Layer biedt voor zowel portemonnees als menselijke gebruikers, die het lezen en uitvoeren van transacties verduidelijkt;
- **Implementatie Interface**, die de kloof overbrugt tussen Business Logic en presentatie, om ervoor te zorgen dat de definitie van Contract consistent is met de gebruikerservaring.


![RGB-Bitcoin](assets/en/070.webp)


Het is belangrijk op te merken dat voor een Wallet om een RGB actief te beheren (of het nu een fungibele token of een recht van welke aard dan ook is), het al deze Elements moet hebben: *Schema*, *Interface*, *Interface Implementation* en *Genesis*. Dit wordt doorgegeven via een ***Contract Consignment***, d.w.z. een gegevenspakket dat alles bevat wat nodig is om de Contract aan de clientzijde te valideren.


Om deze begrippen te verduidelijken, is hier een samenvattende tabel die de componenten van een RGB Contract vergelijkt met concepten die al bekend zijn in objectgeoriënteerd programmeren (OOP) of in het Ethereum ecosysteem:


| RGB Contract Component       | Meaning                        | OOP Equivalent                                     | Ethereum Equivalent                |
| ---------------------------- | ------------------------------ | -------------------------------------------------- | ---------------------------------- |
| **Genesis**                  | Initial state of the contract  | Class constructor                                  | Contract constructor               |
| **Schema**                   | Business logic of the contract | Class                                              | Contract                           |
| **Interface**                | Semantics of the contract      | Interface (Java) / Trait (Rust) / Protocol (Swift) | ERC Standard                       |
| **Interface Implementation** | Mapping semantics and logic    | Impl (Rust) / Implements (Java)                    | Application Binary Interface (ABI) |


De linkerkolom toont de Elements specifiek voor het RGB protocol. De middelste kolom toont de concrete functie van elke component. Vervolgens vinden we in de kolom "OOP equivalent" de equivalente term in object-georiënteerd programmeren:




- De **Genesis** speelt een rol vergelijkbaar met die van een *klasse constructor*: hier wordt de toestand van de Contract geïnitialiseerd;
- De **Schema** is de beschrijving van een klasse, d.w.z. de definitie van de eigenschappen, methoden en onderliggende logica;
- De **Interface** komt overeen met *interfaces* (Java), *traits* (Rust) of *protocollen* (Swift): dit zijn de publieke definities van functies, gebeurtenissen, velden...;
- De **Interface Implementation** komt overeen met *Impl* in Rust of *Implements* in Java, waar we specificeren hoe de code feitelijk de methoden zal uitvoeren die in de Interface zijn aangekondigd.


In de Ethereum-context staat de Genesis dichter bij de *Contract constructor*, de Schema bij de Contract definitie, de Interface bij een standaard zoals ERC-20 of ERC-721, en de Interface Implementation bij de ABI (*Application Binary Interface*), die het formaat van interacties met de Contract specificeert.


Het voordeel van de modulariteit van RGB ligt ook in het feit dat verschillende belanghebbenden bijvoorbeeld hun eigen Interface Implementation kunnen schrijven, zolang ze de logica van de *Schema* en de semantiek van de *Interface* respecteren. Een emittent zou dus een nieuw, gebruiksvriendelijker front-end (Interface) kunnen ontwikkelen, zonder de logica van de Contract aan te passen, of omgekeerd zou men de Schema kunnen uitbreiden om functionaliteit toe te voegen, en een nieuwe versie van de aangepaste Interface Implementation kunnen leveren, terwijl de oude implementaties geldig blijven voor de basisfunctionaliteit.


Wanneer we een nieuwe Contract compileren, generate we een Genesis (de eerste stap in het uitgeven of distribueren van het activum), evenals zijn componenten (Schema, Interface, Interface Implementation). Hierna is de Contract volledig operationeel en kan het verspreid worden naar wallets en gebruikers. Deze methode, waarbij Genesis wordt gecombineerd met deze drie componenten, garandeert een hoge mate van maatwerk (elke Contract kan zijn eigen logica hebben), decentralisatie (iedereen kan bijdragen aan een bepaald component) en veiligheid (validatie blijft strikt gedefinieerd door het protocol, zonder afhankelijk te zijn van willekeurige on-chain code zoals vaak het geval is op andere blockchains).


Ik wil nu elk van deze componenten nader bekijken: de **Schema**, de **Interface** en de **Interface Implementation**.


### Schema


In de vorige paragraaf zagen we dat in het RGB ecosysteem, een Contract is opgebouwd uit verschillende Elements: de Genesis, die de initiële toestand vaststelt, en verschillende andere complementaire componenten. Het doel van de Schema is het declaratief beschrijven van alle Business Logic van de Contract, d.w.z. de datastructuur, de gebruikte typen, de toegestane operaties en hun voorwaarden. Het is daarom een zeer belangrijk element in het operationeel maken van een Contract aan de kant van de cliënt, omdat elke deelnemer (een Wallet, bijvoorbeeld) moet controleren of de toestandsovergangen die hij ontvangt voldoen aan de logica gedefinieerd in de Schema.


Een Schema kan vergeleken worden met een "klasse" in object-georiënteerd programmeren (OOP). Over het algemeen dient het als een model dat de componenten van een Contract definieert, zoals:




- De verschillende soorten Eigen Staten en Opdrachten;
- Valenties, d.w.z. speciale rechten die kunnen worden geactiveerd (*terugbetaald*) voor bepaalde bewerkingen;
- Global State velden, die globale, openbare en gedeelde eigenschappen van de Contract beschrijven;
- De Genesis structuur (de allereerste handeling die de Contract activeert);
- De toegestane vormen van staatsovergangen en staatsuitbreidingen en hoe deze operaties de;
- Metagegevens gekoppeld aan elke bewerking, om tijdelijke of aanvullende informatie op te slaan;
- Regels die bepalen hoe interne Contract gegevens kunnen evolueren (bijvoorbeeld of een veld muteerbaar of cumulatief is);
- Opeenvolgingen van handelingen die als geldig worden beschouwd: bijvoorbeeld een volgorde van overgangen die moet worden gerespecteerd of een reeks logische voorwaarden waaraan moet worden voldaan.


![RGB-Bitcoin](assets/en/071.webp)


Wanneer de *uitgever* van een activum op RGB een Contract publiceert, levert hij de Genesis en Schema die erbij horen. Gebruikers of wallets die willen interageren met het activum, halen deze Schema op om de logica achter de Contract te begrijpen en om later te kunnen verifiëren of de transities waaraan ze deelnemen legitiem zijn.


De eerste stap voor iedereen die informatie ontvangt over een RGB bedrijfsmiddel (bijvoorbeeld een token overdracht), is om deze informatie te valideren met de Schema. Dit houdt in dat de Schema compilatie wordt gebruikt om:




- Controleer of Owned States, Assignments en andere Elements correct gedefinieerd zijn en of ze de opgelegde types respecteren (het zogenaamde *strict type system*);
- Controleren of aan de overgangsregels (validatiescripts) is voldaan. Deze scripts kunnen worden uitgevoerd via AluVM, die aan de klantzijde aanwezig is en verantwoordelijk is voor het valideren van de consistentie van Business Logic (transferbedrag, speciale voorwaarden, enz.).


In de praktijk is Schema geen uitvoerbare code, zoals te zien is in blockchains die opslaan op chain code (EVM op Ethereum). Integendeel, RGB scheidt Business Logic (declaratief) van uitvoerbare code op Blockchain (die beperkt is tot cryptografische ankers). De Schema bepaalt dus de regels, maar de toepassing van deze regels vindt plaats buiten de Blockchain, bij elke deelnemer, volgens het Client-side Validation principe.


Een Schema moet gecompileerd worden voordat het gebruikt kan worden door RGB toepassingen. Deze compilatie produceert een binair bestand (bijvoorbeeld `.RGB`) of een gecodeerd binair bestand (`.rgba`). Wanneer de Wallet dit bestand importeert, weet het:




- Hoe elk gegevenstype (integers, structuren, arrays...) eruit ziet dankzij het strikte type-systeem;
- Hoe Genesis gestructureerd moet worden (om de activainitialisatie te begrijpen);
- De verschillende soorten operaties (toestandsovergangen, toestandsuitbreidingen) en hoe ze de toestand kunnen wijzigen;
- De scriptregels (geïntroduceerd in de Schema) die de AluVM engine zal toepassen om de geldigheid van bewerkingen te controleren.


Zoals uitgelegd in de vorige hoofdstukken, geeft het *strict type system* ons een stabiele, deterministische coderingsindeling: alle variabelen, of het nu Owned States, Global States of Valencies zijn, worden nauwkeurig beschreven (grootte, onder- en bovengrenzen indien nodig, signed of unsigned type, etc.). Het is ook mogelijk om geneste structuren te definiëren, bijvoorbeeld om complexe gebruikssituaties te ondersteunen.


Optioneel kan de Schema verwijzen naar een root `SchemaId`, wat het hergebruik van een bestaande basisstructuur (een sjabloon) vergemakkelijkt. Op deze manier kun je een Contract evolueren of variaties maken (bijvoorbeeld een nieuw type token) vanuit een reeds bewezen sjabloon. Deze modulariteit voorkomt de noodzaak om hele contracten opnieuw te maken en bevordert de standaardisatie van best practices.


Een ander belangrijk punt is dat de logica van de toestandsontwikkeling (overdrachten, updates, enz.) wordt beschreven in de Schema in de vorm van scripts, regels en voorwaarden. Dus, als de Contract ontwerper een heruitgave wil autoriseren of een verbrandingsmechanisme (vernietiging van tokens) wil opleggen, kan hij de corresponderende scripts voor AluVM specificeren in het validatiegedeelte van de Schema.


#### Verschil met programmeerbare On-Chain blockchains


In tegenstelling tot systemen als Ethereum, waar de Smart contract code (uitvoerbaar) in de Blockchain zelf is geschreven, slaat RGB de Contract (haar logica) off-chain op, in de vorm van een gecompileerd declaratief document. Dit impliceert dat:




- Er draait geen Turing-complete VM op elk knooppunt van het Bitcoin netwerk. De regels van een RGB Contract worden niet uitgevoerd op de Blockchain, maar in elke gebruiker die een toestand wil valideren;
- Contract gegevens vervuilen de Blockchain niet: alleen cryptografisch bewijs (*verbintenissen*) is ingebed in Bitcoin transacties (via `Tapret` of `Opret`);
- De Schema kan bijgewerkt of geweigerd worden (*fast-forward*, *push-back*, enz.), zonder dat er een Fork op de Bitcoin Blockchain nodig is. Portemonnees hoeven alleen maar de nieuwe Schema te importeren en zich aan te passen aan de wijzigingen in de consensus.


#### Gebruik door de uitgever en door gebruikers


Wanneer een *emittent* een actief creëert (bijvoorbeeld een niet-inflatoire fungibele token), bereidt hij dit voor:




- Een Schema met de regels voor emissie, overdracht, enz;
- Een Genesis aangepast aan deze Schema (met het totale aantal uitgegeven tokens, de identiteit van de oorspronkelijke eigenaar, eventuele speciale Valencies voor heruitgifte, etc.).


Het maakt dan de gecompileerde Schema (een `.RGB` bestand) beschikbaar voor gebruikers, zodat iedereen die een overdracht van deze token ontvangt, de consistentie van de operatie lokaal kan controleren. Zonder deze Schema zou een gebruiker niet in staat zijn om de statusgegevens te interpreteren of te controleren of ze voldoen aan de Contract regels.


Dus wanneer een nieuwe Wallet een asset wil ondersteunen, moet het gewoon de relevante Schema integreren. Dit mechanisme maakt het mogelijk om compatibiliteit toe te voegen aan nieuwe RGB activa types, zonder de softwarebasis van de Wallet ingrijpend te veranderen: het enige dat nodig is, is om de Schema binary te importeren en de structuur ervan te begrijpen.


De Schema definieert de Business Logic in RGB. Het vermeldt de evolutieregels van een Contract, de structuur van de gegevens (Eigen Staten, Global State, Valenties) en de bijbehorende validatiescripts (uitvoerbaar door AluVM). Dankzij dit declaratieve document is de definitie van een Contract (samengesteld bestand) duidelijk gescheiden van de daadwerkelijke uitvoering van de regels (client-side). Deze ontkoppeling geeft RGB een grote flexibiliteit en maakt een breed scala aan use cases mogelijk (fungibele tokens, NFT, meer geavanceerde contracten), terwijl de complexiteit en gebreken die typisch zijn voor programmeerbare On-Chain blockchains vermeden worden.


#### Schema voorbeeld


Laten we eens kijken naar een concreet voorbeeld van Schema voor een RGB Contract. Dit is een uittreksel in Rust uit het bestand `nia.rs` (initialen voor "*Non-Inflatable Assets*"), dat een model definieert voor fungibele tokens die niet opnieuw kunnen worden uitgegeven voorbij hun initiële Supply (een niet-inflatoir actief). Dit type token kan worden gezien als het equivalent, in het RGB-universum, van de ERC20 op Ethereum, d.w.z. fungibele tokens die bepaalde basisregels respecteren (bv. over transfers, Supply initialisatie, enz.).


Voordat we in de code duiken, is het de moeite waard om de algemene structuur van een RGB Schema in herinnering te brengen. Er is een reeks declaraties omkaderd:




- Een mogelijke `SchemaId` die het gebruik van een andere basis Schema als sjabloon aangeeft;
- De **wereldwijde staten** en **eigen staten** (met hun strikte types);
- **Valencies** (indien van toepassing);
- De **Operaties** (Genesis, toestandsovergangen, toestandsuitbreidingen) die naar deze toestanden en valenties kunnen verwijzen;
- Het **Strict Type System** dat wordt gebruikt om gegevens te beschrijven en te valideren;
- **Validatiescripts** (uitgevoerd via AluVM).


![RGB-Bitcoin](assets/en/072.webp)


De code hieronder toont de volledige definitie van de Rust Schema. We zullen het deel voor deel becommentariëren, volgens de annotaties (1) tot (9) hieronder:


```rust
// ===== PART 1: Function Header and SubSchema =====
fn nia_schema() -> SubSchema {

// definitions of libraries and variables

// ===== PART 2: General Properties (ffv, subset_of, type_system) =====
Schema {
ffv: zero!(),
subset_of: None,
type_system: types.type_system(),

// ===== PART 3: Global States =====
global_types: tiny_bmap! {
GS_NOMINAL => GlobalStateSchema::once(types.get("RGBContract.DivisibleAssetSpec")),
GS_DATA => GlobalStateSchema::once(types.get("RGBContract.ContractData")),
GS_TIMESTAMP => GlobalStateSchema::once(types.get("RGBContract.Timestamp")),
GS_ISSUED_SUPPLY => GlobalStateSchema::once(types.get("RGBContract.Amount")),
},

// ===== PART 4: Owned Types =====
owned_types: tiny_bmap! {
OS_ASSET => StateSchema::Fungible(FungibleType::Unsigned64Bit),
},

// ===== PART 5: Valencies =====
valency_types: none!(),

// ===== PART 6: Genesis: Initial Operations =====
genesis: GenesisSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: tiny_bmap! {
GS_NOMINAL => Occurrences::Once,
GS_DATA => Occurrences::Once,
GS_TIMESTAMP => Occurrences::Once,
GS_ISSUED_SUPPLY => Occurrences::Once,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
},

// ===== PART 7: Extensions =====
extensions: none!(),

// ===== PART 8: Transitions: TS_TRANSFER =====
transitions: tiny_bmap! {
TS_TRANSFER => TransitionSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: none!(),
inputs: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
}
},

// ===== PART 9: Script AluVM and Entry Points =====
script: Script::AluVM(AluScript {
libs: confined_bmap! { alu_id => alu_lib },
entry_points: confined_bmap! {
EntryPoint::ValidateGenesis => LibSite::with(FN_GENESIS_OFFSET, alu_id),
EntryPoint::ValidateTransition(TS_TRANSFER) => LibSite::with(FN_TRANSFER_OFFSET, alu_id),
},
}),
}
}
```




- (1) - **Functie-header en SubSchema**


De `nia_schema()` functie retourneert een `SubSchema`, wat aangeeft dat deze Schema gedeeltelijk kan erven van een meer generieke Schema. In het RGB ecosysteem maakt deze flexibiliteit het mogelijk om bepaalde standaard Elements van een master Schema te hergebruiken, en dan regels te definiëren die specifiek zijn voor de Contract in kwestie. Hier kiezen we ervoor om overerving niet mogelijk te maken, omdat `subset_of` `None` zal zijn.




- (2) - Algemene eigenschappen: ffv, subset_of, **type_system**


De `ffv` eigenschap komt overeen met de *fast-forward* versie van de Contract. Een waarde van `nul!()` hier geeft aan dat we bij versie 0 zijn of de initiële versie van deze Schema. Als je later nieuwe functionaliteiten wilt toevoegen (nieuw type bewerking, enz.), kun je deze versie verhogen om een consensus wijziging aan te geven.


De eigenschap `subset_of: None` eigenschap bevestigt de afwezigheid van overerving. Het `type_system` veld verwijst naar het strikte type systeem dat al gedefinieerd is in de `types` bibliotheek. Deze regel geeft aan dat alle gegevens die gebruikt worden door de Contract de strikte serialisatie-implementatie gebruiken die geleverd wordt door de bibliotheek in kwestie.




- (3) - Wereldwijde staten


In het `global_types` blok declareren we vier Elements. We gebruiken de sleutel, zoals `GS_NOMINAL` of `GS_ISSUED_SUPPLY`, om er later naar te verwijzen:




- `GS_NOMINAL` verwijst naar een `DivisibleAssetSpec` type, dat verschillende velden van de aangemaakte token beschrijft (volledige naam, ticker, precisie...);
- `GS_DATA` staat voor algemene gegevens, zoals een disclaimer, metagegevens of andere tekst;
- `GS_TIMESTAMP` verwijst naar een uitgiftedatum;
- `GS_ISSUED_SUPPLY` stelt het totaal Supply in, d.w.z. het maximum aantal tokens dat kan worden aangemaakt.


Het sleutelwoord `once(...)` betekent dat elk van deze velden maar één keer kan voorkomen.




- (4) - Types in eigendom


In `owned_types` declareren we `OS_ASSET`, dat een fungibele status beschrijft. We gebruiken `StateSchema::Fungible(FungibleType::Unsigned64Bit)`, wat aangeeft dat de hoeveelheid activa (tokens) wordt opgeslagen als een 64-bit unsigned integer. Elke transactie zal dus een bepaald aantal eenheden van deze token verzenden, die gevalideerd zullen worden volgens deze strikt getypeerde numerieke structuur.




- (5) - **Valencies**


We geven `valency_types: none!()` aan, wat betekent dat er geen Valencies zijn in dit Schema, met andere woorden geen speciale of extra rechten (zoals heruitgifte, voorwaardelijk branden, enz.). Als een Schema Valencies bevat, zouden ze in deze sectie gedeclareerd worden.




- (6) - Genesis: eerste operaties


Hier komen we in het gedeelte dat Contract Operations verklaart. De Genesis wordt beschreven door:




- De afwezigheid van `metadata` (veld `metadata: Ty::<SemId>::UNIT.id(None)`);
- Wereldwijde staten die elk één keer aanwezig moeten zijn (`Once`);
- Een Toewijzingslijst waar `OS_ASSET` `EénmaalMeer` moet voorkomen. Dit betekent dat Genesis minstens één `OS_ASSET` Assignment (een initiële houder) nodig heeft;
- Geen Valency: `valencies: none!()`.


Dit is hoe we de definitie van de initiële token uitgifte beperken: we moeten de uitgegeven Supply declareren (`GS_ISSUED_SUPPLY`), plus ten minste één houder (een Owned State van het type `OS_ASSET`).




- (7) - Uitbreidingen


Het `extensies: geen!()` veld geeft aan dat er geen State Extension is voorzien in deze Contract. Dit betekent dat er geen bewerking is om Redeem een digitaal recht (Valency) te geven of om een State Extension voor een Overgang uit te voeren. Alles gebeurt via Genesis of State Transitions.




- (8) - Overgangen: TS_TRANSFER


In `overgangen` definiëren we het `TS_TRANSFER` type operatie. We leggen uit dat:




- Het heeft geen metadata;
- Het wijzigt Global State niet (dat is al gedefinieerd in Genesis);
- Het neemt een of meer `OS_ASSETs` als invoer. Dit betekent dat het bestaande Owned States moet uitgeven;
- Het creëert (`toewijzingen`) ten minste één nieuwe `OS_ASSET` (met andere woorden, de ontvanger of ontvangers ontvangen tokens);
- Het genereert geen nieuwe Valency.


Dit modelleert het gedrag van een basisoverdracht, die tokens verbruikt op een UTXO, vervolgens nieuwe Eigen Staten creëert ten gunste van de ontvangers en zo de gelijkheid van het totale bedrag tussen inputs en outputs behoudt.




- (9) - **AluVM script en ingangspunten** (in het Frans)


Tenslotte declareren we een AluVM script (`Script::AluVM(AluScript { ... })`). Dit script bevat:




- Een of meer externe bibliotheken (`libs`) die gebruikt moeten worden tijdens de validatie;
- Entry points die wijzen naar functie offsets in de AluVM code, corresponderend met validatie van de Genesis (`ValidateGenesis`) en elke gedeclareerde Transitie (`ValidateTransition(TS_TRANSFER)`).


Deze validatiecode is verantwoordelijk voor het toepassen van Business Logic. Hij controleert bijvoorbeeld:




- Dat de `GS_ISSUED_SUPPLY` niet wordt overschreden tijdens Genesis;
- Dat de som van `inputs` (uitgegeven tokens) gelijk is aan de som van `assignments` (ontvangen tokens) voor `TS_TRANSFER`.


Als deze regels niet worden nageleefd, wordt de overgang als ongeldig beschouwd.


Dit voorbeeld van een "*Niet-opblaasbare fungibele activa*" Schema geeft ons een beter begrip van de structuur van een eenvoudige RGB fungibele token Contract. We kunnen duidelijk de scheiding zien tussen de gegevensbeschrijving (Globale en Eigendomstoestanden), de declaratie van de bewerking (Genesis, Overgangen, Uitbreidingen) en de implementatie van de validatie (AluVM scripts). Dankzij dit model gedraagt een token zich als een klassieke fungibele token, maar blijft het gevalideerd aan de kant van de cliënt en is het niet afhankelijk van de On-Chain infrastructuur om zijn code uit te voeren. Alleen cryptografische verplichtingen zijn verankerd in de Bitcoin Blockchain.


### Interface


De Interface is de Layer die ontworpen is om een Contract leesbaar en manipuleerbaar te maken, zowel door gebruikers (menselijk lezen) als door portfolio's (software lezen). De Interface speelt daarom een rol die vergelijkbaar is met die van een Interface in een objectgeoriënteerde programmeertaal (Java, Rust trait, enz.), in die zin dat het de functionele structuur van een Contract blootlegt en verduidelijkt, zonder noodzakelijkerwijs de interne details van de Business Logic te onthullen.


In tegenstelling tot Schema, dat puur declaratief is en gecompileerd in een binair bestand dat moeilijk te gebruiken is zoals het is, levert Interface de leessleutels die nodig zijn om:




- Maak een lijst en beschrijf de Globale Staten en Eigen Staten die zijn opgenomen in de Contract;
- Krijg toegang tot de namen en waarden van elk veld, zodat ze kunnen worden weergegeven (bijv. voor een token, zoek de ticker, het maximumbedrag, enz. uit);
- Interpreteer en construeer Contract Bewerkingen (Genesis, State Transition of State Extension) door gegevens te associëren met begrijpelijke namen (bijvoorbeeld, voer een overboeking uit door duidelijk "bedrag" te specificeren in plaats van een binaire identifier).


![RGB-Bitcoin](assets/en/073.webp)


Dankzij de Interface kun je bijvoorbeeld code schrijven in een Wallet die, in plaats van velden te manipuleren, direct labels manipuleert zoals "aantal tokens", "activanaam", enz. Op deze manier wordt het beheren van een Contract intuïtiever. Op deze manier wordt het beheren van een Contract intuïtiever.


#### Algemene werking


Deze methode heeft veel voordelen:




- **Standaardisatie:**


Hetzelfde type Contract kan ondersteund worden door een standaard Interface, gedeeld door verschillende Wallet implementaties. Dit vergemakkelijkt compatibiliteit en hergebruik van code.




- Duidelijke scheiding tussen Schema en Interface:


In het RGB ontwerp zijn Schema (Business Logic) en Interface (presentatie en manipulatie) twee onafhankelijke entiteiten. De ontwikkelaars die de Contract logica schrijven, kunnen zich concentreren op Schema, zonder zich zorgen te maken over ergonomie of datarepresentatie, terwijl een ander team (of hetzelfde team, maar op een andere tijdlijn) Interface kan ontwikkelen.




- **Flexibele evolutie:**


De Interface kan worden gewijzigd of aangevuld nadat het middel is uitgegeven, zonder dat de Contract zelf hoeft te worden gewijzigd. Dit is een groot verschil met sommige On-Chain Smart contract systemen, waar de Interface (vaak gemengd met de uitvoeringscode) bevroren is in de Blockchain.




- Multi-Interface mogelijkheid


Dezelfde Contract kan blootgesteld worden via verschillende interfaces, aangepast aan verschillende behoeften: een eenvoudige Interface voor de eindgebruiker, een meer geavanceerde voor de uitgever die complexe configuratieoperaties moet beheren. De Wallet kan dan kiezen welke Interface hij importeert, afhankelijk van zijn gebruik.


![RGB-Bitcoin](assets/en/074.webp)


In de praktijk, wanneer de Wallet een RGB Contract ophaalt (via een `.RGB` of `.rgba` bestand), importeert het ook de bijbehorende Interface, die ook gecompileerd wordt. Tijdens runtime kan de Wallet bijvoorbeeld:




- Blader door de lijst met staten en lees hun namen, om Ticker, Initieel Bedrag, Uitgiftedatum, enz. weer te geven op de gebruiker Interface, in plaats van een onleesbare numerieke identificatiecode;
- Bouw een bewerking (zoals een overboeking) met behulp van expliciete parameternamen: in plaats van `opdrachten { OS_ASSET => 1 }` te schrijven, kan het de gebruiker een "Bedrag" veld in een formulier aanbieden, en deze informatie vertalen naar de strikt getypte velden die Contract verwacht.


#### Verschil met Ethereum en andere systemen


Op Ethereum is de Interface (beschreven via de ABI, *Application Binary Interface*) over het algemeen afgeleid van On-Chain opgeslagen code (de Smart contract). Het kan kostbaar of ingewikkeld zijn om een specifiek deel van de Interface aan te passen zonder de Contract zelf aan te raken. RGB is echter gebaseerd op een volledig off-chain logica, met gegevens verankerd in *commitments* op Bitcoin. Dit ontwerp maakt het mogelijk om de Interface (of de implementatie ervan) te wijzigen zonder de fundamentele veiligheid van de Contract te beïnvloeden, aangezien de validatie van de bedrijfsregels in de Schema en de AluVM code waarnaar verwezen wordt, blijft.


#### Interface compilatie


Net als Schema wordt de Interface gedefinieerd in broncode (vaak in Rust) en gecompileerd in een `.RGB` of `.rgba` bestand. Dit binaire bestand bevat alle informatie die de Wallet nodig heeft om:




- Identificeer velden op naam;
- Koppel elk veld (en de waarde ervan) aan het strikte systeemtype dat is gedefinieerd in de Contract;
- Ken de verschillende toegestane operaties en hoe je ze bouwt.


Zodra de Interface geïmporteerd is, kan de Wallet de Contract correct weergeven en de gebruiker interacties voorstellen.


### Interfaces gestandaardiseerd door de LNP/BP associatie


In het RGB ecosysteem wordt een Interface gebruikt om een leesbare en manipuleerbare betekenis te geven aan de gegevens en bewerkingen van een Contract. De Interface vult dus de Schema aan, die de Business Logic intern beschrijft (strikte types, validatiescripts, enz.). In dit hoofdstuk bekijken we de standaard Interfaces die door de LNP/BP associatie zijn ontwikkeld voor veel voorkomende Contract types (fungibele tokens, NFT, etc.).


Ter herinnering, het idee is dat elke Interface beschrijft hoe een Contract op de Wallet moet worden weergegeven en gemanipuleerd, waarbij de velden duidelijk worden benoemd (zoals `spec`, `ticker`, `issuedSupply`...) en de mogelijke operaties worden gedefinieerd (zoals `Transfer`, `Burn`, `Rename`...). Verschillende interfaces zijn al operationeel, maar er zullen er in de toekomst meer en meer komen.


#### Enkele kant-en-klare interfaces


**RGB20** is de Interface voor fungibele activa, die kan worden vergeleken met de ERC20-standaard van Ethereum. Het gaat echter een stap verder en biedt uitgebreidere functionaliteit:




- Bijvoorbeeld de mogelijkheid om de naam van het activum te wijzigen (verandering van *ticker* of volledige naam) nadat het is uitgegeven, of om de nauwkeurigheid ervan aan te passen (*stock splits*);
- Het kan ook mechanismen beschrijven voor secundaire heruitgifte (beperkt of onbeperkt) en voor verbranding en vervolgens vervanging, om de emittent toe te staan activa te vernietigen en vervolgens opnieuw te creëren onder bepaalde voorwaarden;


Het RGB20 Interface kan bijvoorbeeld gekoppeld worden aan het **Non-Inflatable Asset (NIA)-schema**, dat een niet-opblaasbare initiële Supply oplegt, of aan andere, meer geavanceerde schema's zoals vereist.


**RGB21** heeft betrekking op contracten van het NFT-type, of ruimer gezien, op alle unieke digitale inhoud, zoals de weergave van digitale media (afbeeldingen, muziek, enz.). Naast het beschrijven van de uitgifte en overdracht van een enkel actief, bevat het kenmerken zoals:




- Geïntegreerde ondersteuning voor het direct opnemen van een bestand (tot 16 MB) in de Contract (voor ophalen op de client);
- De mogelijkheid voor de eigenaar om een "*gravure*" in de geschiedenis in te voeren om Ownership van een NFT uit het verleden te bewijzen.


**RGB25** is een hybride standaard die fungibele en niet-fungibele aspecten combineert. Het is ontworpen voor gedeeltelijk fungibele activa, zoals vastgoed tokenization, waar je een eigendom wilt opsplitsen met behoud van een link naar een enkele root asset (met andere woorden, je hebt fungibele stukken van een huis, gelinkt aan een niet-fungibel huis). Technisch gezien kan deze Interface gekoppeld worden aan de **Collectible Fungible Asset (CFA)** Schema, die rekening houdt met de notie van opsplitsen terwijl het oorspronkelijke actief getraceerd wordt.


#### Interfaces in ontwikkeling


Andere interfaces zijn gepland voor meer gespecialiseerd gebruik, maar zijn nog niet beschikbaar:




- **RGB22**, gewijd aan digitale identiteiten, voor het beheren van identifiers en On-Chain profielen in het RGB ecosysteem;
- **RGB23**, voor geavanceerde tijdstempels, gebruikmakend van enkele ideeën van *Opentimestamps*, maar met traceerbaarheidsfuncties;
- **RGB24**, dat streeft naar het equivalent van een gedecentraliseerd domeinnaamsysteem (DNS) vergelijkbaar met de *Ethereum Name Service*;
- **RGB26**, ontworpen om DAO's (*Gedecentraliseerde Autonome Organisatie*) in een complexere vorm te beheren (bestuur, stemmen, enz.);
- **RGB30**, zeer vergelijkbaar met RGB20, maar met de bijzonderheid dat er rekening wordt gehouden met gedecentraliseerde initiële uitgifte en dat er gebruik wordt gemaakt van staatsuitbreidingen. Dit zou worden gebruikt voor activa waarvan de heruitgifte wordt beheerd door verschillende entiteiten, of waarvoor fijnere voorwaarden gelden.


Natuurlijk kunnen deze interfaces, afhankelijk van de datum waarop je deze cursus raadpleegt, al operationeel en toegankelijk zijn.


#### Interface voorbeeld


Dit Rust codefragment toont een [RGB20](https://github.com/RGB-WG/RGB-std/blob/master/src/Interface/rgb20.rs) Interface (fungibel actief). Deze code komt uit het `rgb20.rs` bestand in de standaard RGB bibliotheek. Laten we er eens naar kijken om de structuur van een Interface te begrijpen en hoe het een brug vormt tussen, aan de ene kant, de Business Logic (gedefinieerd in de Schema) en, aan de andere kant, de functionaliteiten blootgesteld aan wallets en gebruikers.


```rust
// ...
fn rgb20() -> Iface {
let types = StandardTypes::with(rgb20_stl());

Iface {
version: VerNo::V1,
name: tn!("RGB20"),
global_state: tiny_bmap! {
fname!("spec") => GlobalIface::required(types.get("RGBContract.DivisibleAssetSpec")),
fname!("data") => GlobalIface::required(types.get("RGBContract.ContractData")),
fname!("created") => GlobalIface::required(types.get("RGBContract.Timestamp")),
fname!("issuedSupply") => GlobalIface::one_or_many(types.get("RGBContract.Amount")),
fname!("burnedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
fname!("replacedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
},
assignments: tiny_bmap! {
fname!("inflationAllowance") => AssignIface::public(OwnedIface::Amount, Req::NoneOrMore),
fname!("updateRight") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnEpoch") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnRight") => AssignIface::public(OwnedIface::Rights, Req::NoneOrMore),
fname!("assetOwner") => AssignIface::private(OwnedIface::Amount, Req::NoneOrMore),
},
valencies: none!(),
genesis: GenesisIface {
metadata: Some(types.get("RGBContract.IssueMeta")),
global: tiny_bmap! {
fname!("spec") => ArgSpec::required(),
fname!("data") => ArgSpec::required(),
fname!("created") => ArgSpec::required(),
fname!("issuedSupply") => ArgSpec::required(),
},
assignments: tiny_bmap! {
fname!("assetOwner") => ArgSpec::many(),
fname!("inflationAllowance") => ArgSpec::many(),
fname!("updateRight") => ArgSpec::optional(),
fname!("burnEpoch") => ArgSpec::optional(),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_RESERVES
},
},
transitions: tiny_bmap! {
tn!("Transfer") => TransitionIface {
optional: false,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("previous") => ArgSpec::from_non_empty("assetOwner"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_non_empty("assetOwner"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Issue") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.IssueMeta")),
globals: tiny_bmap! {
fname!("issuedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_non_empty("inflationAllowance"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_many("inflationAllowance"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
ISSUE_EXCEEDS_ALLOWANCE,
INSUFFICIENT_RESERVES
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("OpenEpoch") => TransitionIface {
optional: true,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnEpoch"),
},
assignments: tiny_bmap! {
fname!("next") => ArgSpec::from_optional("burnEpoch"),
fname!("burnRight") => ArgSpec::required()
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("burnRight")),
},
tn!("Burn") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("burnedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: None,
},
tn!("Replace") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("replacedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS,
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Rename") => TransitionIface {
optional: true,
metadata: None,
globals: tiny_bmap! {
fname!("new") => ArgSpec::from_required("spec"),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("updateRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("updateRight"),
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("future")),
},
},
extensions: none!(),
error_type: types.get("RGB20.Error"),
default_operation: Some(tn!("Transfer")),
type_system: types.type_system(),
}
}
```


In deze Interface zien we overeenkomsten met de Schema structuur: we vinden een declaratie van Global State, Owned States, Contract Operations (Genesis en Transitions), evenals foutafhandeling. Maar de Interface richt zich op de presentatie en manipulatie van deze Elements voor een Wallet of een andere toepassing.


Het verschil met Schema zit in de aard van de types. Schema gebruikt strikte types (zoals `FungibleType::Unsigned64Bit`) en meer technische identifiers. Interface gebruikt veldnamen, macro's (`fname!()`, `tn!()`) en verwijzingen naar argumentklassen (`ArgSpec`, `OwnedIface::Rights`...). Het doel hier is om het functioneel begrijpen en organiseren van Elements voor Wallet te vergemakkelijken.


Daarnaast kan de Interface extra functionaliteit toevoegen aan de basis Schema (bijvoorbeeld het beheer van een `burnEpoch` recht), zolang dit consistent blijft met de uiteindelijke gevalideerde client-side logica. Het AluVM "script" gedeelte in de Schema zorgt voor de cryptografische geldigheid, terwijl de Interface beschrijft hoe de gebruiker (of Wallet) interageert met deze toestanden en overgangen.


#### Global State en toewijzingen


In de `global_state` sectie vinden we velden zoals `spec` (asset beschrijving), `data`, `created`, `issuedSupply`, `burnedSupply`, `replacedSupply`. Dit zijn velden die de Wallet kan lezen en presenteren. Bijvoorbeeld:




- `spec` geeft de token configuratie weer;
- `issuedSupply` of `burnedSupply` geven ons het totale aantal uitgegeven of verbrande tokens, etc.


In het gedeelte `toewijzingen` definiëren we verschillende rollen of rechten. Bijvoorbeeld:




- `assetOwner` komt overeen met het houden van tokens (het is de fungibele *Owned State*);
- `burnRight` komt overeen met de mogelijkheid om tokens te verbranden;
- updateRight` komt overeen met het recht om de naam van het actief te wijzigen.


Het `public` of `private` sleutelwoord (bijv. `AssignIface::public(...)`) geeft aan of deze toestanden zichtbaar (`public`) of vertrouwelijk (`private`) zijn. Wat betreft `Req::NoneOrMore`, `Req::Optional`, deze geven het verwachte voorkomen aan.


#### Genesis en overgangen


Het `Genesis` gedeelte beschrijft hoe de asset wordt geïnitialiseerd:




- De velden `spec`, `data`, `created`, `issuedSupply` zijn verplicht (`ArgSpec::required()`);
- Toewijzingen zoals `assetOwner` kunnen aanwezig zijn in meerdere kopieën (`ArgSpec::many()`), waardoor tokens verdeeld kunnen worden onder meerdere initiële houders;
- Velden zoals `inflationAllowance` of `burnEpoch` kunnen (of mogen niet) worden opgenomen in Genesis.


Vervolgens definieert de Interface voor elke Overgang (`Overdracht`, `Uitgave`, `Verbranden`...) welke velden de bewerking als invoer verwacht, welke velden de bewerking als uitvoer produceert en welke fouten er kunnen optreden. Bijvoorbeeld:


**Overgang:**




- Ingangen: `previous` → moet een `assetOwner` zijn;
- Toewijzingen: `begunstigde` → wordt een nieuwe `assetOwner`;
- Fout: `NON_EQUAL_AMOUNTS` (de Wallet kan dus gevallen verwerken waarin de ingangssom niet overeenkomt met de uitgangssom).


**Overgang `Issue`:**




- Optioneel (`optioneel: waar`), omdat extra emissie niet noodzakelijk wordt geactiveerd;
- Ingangen: `used` → een `inflationAllowance`, d.w.z. toestemming om meer tokens toe te voegen;
- Toewijzingen: `begunstigde` (ontvangen nieuwe tokens) en `toekomstige` (resterende `inflationAllowance`);
- Mogelijke fouten: `SUPPLY_MISMATCH`, `ISSUE_EXCEEDS_ALLOWANCE`, enz.


**Brandovergang:**




- Ingangen: `gebruikt` → een `burnRight`;
- Globals: `burnedSupply` vereist;
- Opdrachten: `future` → een mogelijke voortzetting van de `burnRight` als we niet alles hebben verbrand;
- Fouten: `SUPPLY_MISMATCH`, `INVALID_PROOF`, `INSUFFICIENT_COVERAGE`.


Elke bewerking wordt daarom beschreven op een manier die leesbaar is voor een Wallet. Dit maakt het mogelijk om een grafische Interface weer te geven waar de gebruiker duidelijk kan zien: "Je hebt het recht om te verbranden. Wilt u een bepaalde hoeveelheid verbranden? De code weet een `burnedSupply` veld in te vullen en controleert of het `burnRight` geldig is.


Samenvattend is het belangrijk om in gedachten te houden dat een Interface, hoe compleet ook, op zichzelf niet de interne logica van de Contract definieert. Het hart van het werk wordt gedaan door de **Schema**, die strikte types, Genesis structuur, overgangen enzovoort omvat. De Interface stelt deze Elements eenvoudigweg bloot op een meer intuïtieve en benoemde manier, voor gebruik in een applicatie.


Dankzij de modulariteit van RGB kan de Interface geüpgrade worden (bijvoorbeeld door een `Rename` overgang toe te voegen, de weergave van een veld te corrigeren, etc.) zonder dat de hele Contract herschreven hoeft te worden. Gebruikers van deze Interface kunnen dan direct profiteren van deze verbeteringen, zodra ze het `.RGB` of `.rgba` bestand bijwerken.


Maar als je eenmaal een Interface hebt gedeclareerd, moet je het koppelen aan de overeenkomstige Schema. Dit wordt gedaan via de ***Interface Implementation***, die specificeert hoe elk genoemd veld (zoals `fname!("assetOwner")`) moet worden toegewezen aan de strikte ID (zoals `OS_ASSET`) gedefinieerd in de Schema. Dit zorgt er bijvoorbeeld voor dat wanneer een Wallet een `burnRight` veld manipuleert, dit de toestand is die in de Schema de mogelijkheid beschrijft om tokens te verbranden.


### Interface Implementation


In de RGB architectuur hebben we gezien dat elk component (Schema, Interface, enz.) onafhankelijk ontwikkeld en gecompileerd kan worden. Er is echter nog één onmisbaar element dat deze verschillende bouwstenen met elkaar verbindt: de ***Interface Implementation***. Dit is wat expliciet de identifiers of velden gedefinieerd in de Schema (aan de Business Logic kant) koppelt aan de namen gedeclareerd in de Interface (aan de presentatie en gebruikersinteractie kant). Dus wanneer een Wallet een Contract laadt, kan het precies begrijpen welk veld overeenkomt met wat, en hoe een operatie die in de Interface genoemd wordt, verband houdt met de logica van de Schema.


Een belangrijk punt is dat Interface Implementation niet noodzakelijkerwijs bedoeld is om alle Schema-functionaliteiten bloot te leggen, noch alle Interface-velden: het kan beperkt worden tot een subset. In de praktijk maakt dit het mogelijk om bepaalde aspecten van de Schema te beperken of te filteren. Je zou bijvoorbeeld een Schema kunnen hebben met vier soorten bewerkingen, maar een Implementatie Interface die er slechts twee in kaart brengt in een bepaalde context. Omgekeerd, als een Interface extra eindpunten voorstelt, kunnen we ervoor kiezen om ze hier niet te implementeren.


Hier is een klassiek voorbeeld van Interface Implementation, waarbij we een *Non-Inflatable Asset* (NIA) Schema associëren met de RGB20 Interface:


```rust
fn nia_rgb20() -> IfaceImpl {
let schema = nia_schema();
let iface = Rgb20::iface();

IfaceImpl {
version: VerNo::V1,
schema_id: schema.schema_id(),
iface_id: iface.iface_id(),
script: none!(),
global_state: tiny_bset! {
NamedField::with(GS_NOMINAL, fname!("spec")),
NamedField::with(GS_DATA, fname!("data")),
NamedField::with(GS_TIMESTAMP, fname!("created")),
NamedField::with(GS_ISSUED_SUPPLY, fname!("issuedSupply")),
},
assignments: tiny_bset! {
NamedField::with(OS_ASSET, fname!("assetOwner")),
},
valencies: none!(),
transitions: tiny_bset! {
NamedType::with(TS_TRANSFER, tn!("Transfer")),
},
extensions: none!(),
}
}
```


In deze implementatie Interface:




- We verwijzen expliciet naar de Schema, via `nia_schema()`, en de Interface, via `Rgb20::iface()`. De aanroepen `Schema.schema_id()` en `iface.iface_id()` worden gebruikt om Anchor de Interface Implementation te compileren (dit associeert de cryptografische identifiers van deze twee componenten);
- Er wordt een mapping gemaakt tussen Schema Elements en Interface Elements. Bijvoorbeeld, het veld `GS_NOMINAL` in de Schema wordt gekoppeld aan de string `"spec"` in de Interface (`NamedField::with(GS_NOMINAL, fname!("spec"))`). We doen hetzelfde voor bewerkingen, zoals `TS_TRANSFER`, die we koppelen aan `"Transfer"` in de Interface...;
- We kunnen zien dat er geen valencies (`valencies: none!()`) of extensies (`extensions: none!()`) zijn, wat aangeeft dat deze NIA Contract deze functies niet gebruikt.


Het resultaat na compilatie is een apart `.RGB` of `.rgba` bestand, dat geïmporteerd moet worden in de Wallet naast de Schema en Interface. De software weet dus hoe deze NIA Contract (waarvan de logica beschreven wordt door zijn Schema) concreet verbonden moet worden met de "RGB20" Interface (die menselijke namen en een interactiemodus voor fungibele tokens levert), waarbij deze Interface Implementation gebruikt wordt als gateway tussen de twee.


#### Waarom Interface Implementation scheiden?


Scheiding vergroot de flexibiliteit. Een enkele Schema zou verschillende Interface implementaties kunnen hebben, die elk een andere set functionaliteiten toewijzen. Bovendien kan de Interface Implementation zelf evolueren of herschreven worden zonder dat er een verandering nodig is in Schema of Interface. Dit behoudt het principe van modulariteit van RGB: elk component (Schema, Interface, Interface Implementation) kan onafhankelijk in versie worden gebracht en bijgewerkt, zolang de compatibiliteitsregels die door het protocol worden opgelegd, worden gerespecteerd (dezelfde identifiers, consistentie van types, etc.).


Bij concreet gebruik moet de Wallet een Contract laden:




- Laad de gecompileerde **Schema** (om de structuur van de Business Logic te kennen);
- Gecompileerde **Interface** laden (om namen en bewerkingen aan de gebruikerskant te begrijpen);
- Laad gecompileerd **Interface Implementation** (om Schema logica te koppelen aan Interface namen, bewerking per bewerking, veld per veld).


Deze modulaire architectuur maakt gebruiksscenario's mogelijk zoals:




- Beperk bepaalde bewerkingen voor bepaalde gebruikers: bied een gedeeltelijke implementatie Interface aan die alleen toegang geeft tot basisoverdrachten, zonder bijvoorbeeld brand- of updatefuncties aan te bieden;
- Wijzigingspresentatie: ontwerp een Interface Implementation die een veld in de Interface een andere naam geeft of anders in kaart brengt, zonder de basis van de Contract te wijzigen;
- Ondersteuning van meerdere schema's: een Wallet kan meerdere Interface implementaties laden voor hetzelfde Interface type, om verschillende schema's (verschillende token logica's) af te handelen, mits hun structuur compatibel is.


In het volgende hoofdstuk bekijken we hoe een Contract overboeking werkt en hoe RGB facturen worden gegenereerd.


## Contract overdrachten


<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>


:::video id=75eb5a8d-1910-4155-b5e3-81204c9a8901:::


In dit hoofdstuk gaan we het proces van een Contract overdracht in het RGB ecosysteem analyseren. Om dit te illustreren, kijken we naar Alice en Bob, onze gebruikelijke hoofdrolspelers, die Exchange een RGB goed willen overbrengen. We laten ook wat commando fragmenten zien van de `RGB` command-line tool, om te zien hoe het in de praktijk werkt.


### RGB Contract overdracht begrijpen


Laten we een voorbeeld nemen van een overdracht tussen Alice en Bob. In dit voorbeeld nemen we aan dat Bob net RGB begint te gebruiken, terwijl Alice al RGB-activa in haar Wallet heeft. We zullen zien hoe Bob zijn omgeving instelt, de relevante Contract importeert, dan een overdracht aanvraagt van Alice, en tenslotte hoe Alice de eigenlijke transactie uitvoert op Bitcoin Blockchain.


#### 1) De RGB Wallet installeren


Allereerst moet Bob een RGB Wallet installeren, d.w.z. software die compatibel is met het protocol. Deze bevat in het begin geen contracten. Bob heeft ook nodig:




- Een Bitcoin Wallet om je UTXO's te beheren;
- Een verbinding met een Bitcoin knooppunt (of met een Electrum server), zodat je je UTXO's kunt identificeren en je transacties op het netwerk kunt propageren.


Ter herinnering, **Eigen Staten** in RGB verwijzen naar Bitcoin UTXO's. We moeten dus altijd UTXO's kunnen beheren en uitgeven in een Bitcoin transactie die cryptografische verplichtingen (`Tapret` of `Opret`) bevat die verwijzen naar RGB gegevens.


#### 2) Contract informatieverwerving


Bob moet dan de gegevens van Contract ophalen waarin hij geïnteresseerd is. Deze gegevens kunnen via elk kanaal circuleren: website, e-mail, berichtentoepassing... In de praktijk worden ze gegroepeerd in een ***Consignment***, d.w.z. een klein pakketje gegevens dat het volgende bevat:




- De **Genesis**, die de begintoestand van de Contract definieert;
- De **Schema**, die de Business Logic beschrijft (strikte types, validatiescripts, enz.);
- De **Interface**, die de presentatie Layer definieert (veldnamen, toegankelijke bewerkingen);
- De **Interface Implementation**, die de Schema concreet verbindt met de Interface.


![RGB-Bitcoin](assets/en/075.webp)


De totale grootte is vaak in de orde van een paar kilobytes, omdat elk onderdeel over het algemeen minder dan 200 bytes weegt. Het kan ook mogelijk zijn om deze Consignment uit te zenden in Base58, via censuurbestendige kanalen (zoals Nostr of via de Lightning Network bijvoorbeeld), of als QR-code.


#### 3) Contract importeren en valideren


Zodra Bob de Consignment heeft ontvangen, importeert hij deze in zijn RGB Wallet. Dit zal dan:




- Controleer of de Genesis en Schema geldig zijn;
- Laad Interface en Interface Implementation;
- Werk je client-side gegevens Stash bij.


Bob kan nu het goed zien in zijn Wallet (zelfs als hij het nog niet bezit) en begrijpen welke velden beschikbaar zijn, welke bewerkingen mogelijk zijn... Vervolgens moet hij contact opnemen met een persoon die daadwerkelijk eigenaar is van het goed dat moet worden overgedragen. In ons voorbeeld is dat Alice.


Het proces om te ontdekken wie een bepaald RGB activum bezit, is vergelijkbaar met het vinden van een Bitcoin betaler. De details van deze verbinding hangen af van het gebruik (marktplaatsen, privé chatkanalen, facturering, verkoop van goederen en diensten, salaris...).


#### 4) Een Invoice uitgeven


Om de overdracht van een RGB goed te initiëren, moet Bob eerst een Invoice uitgeven. Deze Invoice wordt gebruikt om:




- Vertel Alice het type bewerking dat moet worden uitgevoerd (bijvoorbeeld een `Transfer` van een RGB20 Interface);
- Geef Alice de *Seal Definition* van Bob (d.w.z. de UTXO waar hij het goed wil ontvangen);
- Specificeer de benodigde hoeveelheid werkzame stof (bijv. 100 eenheden).


Bob gebruikt de `RGB` tool op de commandoregel. Stel, hij wil 100 eenheden van een token waarvan de `ContractId` bekend is, wil vertrouwen op `Tapret`, en specificeert zijn UTXO (`456e3..dfe1:0`):


```bash
bob$ rgb invoice RGB20 100 <ContractId> tapret1st:456e3..dfe1:0
```


Aan het einde van dit hoofdstuk gaan we dieper in op de structuur van RGB facturen.


#### 5) Invoice overdracht


De gegenereerde Invoice (bijvoorbeeld als URL: `RGB:2WBcas9.../RGB20/100+utxob:...`) bevat alle informatie die Alice nodig heeft om de overdracht voor te bereiden. Net als bij de Consignment kan het compact worden gecodeerd (Base58 of een ander formaat) en worden verzonden via een berichtentoepassing, e-mail, Nostr...


![RGB-Bitcoin](assets/en/076.webp)


#### 6) Voorbereiding van de transactie aan de Alice-zijde


Alice ontvangt Bob's Invoice. In haar RGB Wallet heeft ze een Stash die het over te dragen goed bevat. Om de UTXO met het actief uit te geven, moet ze eerst een PSBT (*Partially Signed Bitcoin Transaction*) generate doen, dus een onvolledige Bitcoin transactie, met behulp van de UTXO die ze heeft:


```bash
alice$ wallet construct tx.psbt
```


Deze basistransactie (voorlopig ongetekend) wordt gebruikt om Anchor de cryptografische Commitment te geven die gekoppeld is aan de overdracht naar Bob. UTXO van Alice wordt dus uitgegeven, en in de uitvoer plaatsen we de `Tapret` of `Opret` Commitment voor Bob.


#### 7) Genereren van overdracht Consignment


Vervolgens bouwt Alice de ***Terminal Consignment*** (soms "transfer Consignment" genoemd) via het commando:


```bash
alice$ rgb transfer tx.psbt <invoice> consignment.rgb
```


Dit nieuwe `Consignment.RGB` bestand bevat:




- De volledige geschiedenis van staatsovergangen die nodig zijn om de activa te valideren tot op dit moment (sinds Genesis);
- De nieuwe State Transition die activa overdraagt van Alice naar Bob, volgens de Invoice die Bob heeft uitgegeven;
- De incomplete Bitcoin transactie (*Witness Transaction*) (`tx.PSBT`), die Alice's Single-Use Seal uitgeeft, gewijzigd om de cryptografische Commitment naar Bob op te nemen.


In dit stadium wordt de transactie nog niet uitgezonden op het Bitcoin netwerk. De Consignment is groter dan een basis Consignment, omdat het de hele geschiedenis (*proof chain*) bevat om de legitimiteit van het activum te bewijzen.


#### 8) Bob controleert en accepteert de Consignment


Alice zendt deze **Terminal Consignment** naar Bob. Bob zal dan:




- Controleer de geldigheid van de State Transition (zorg ervoor dat de geschiedenis consistent is, dat de Contract regels worden nageleefd, enz;)
- Voeg het toe aan je lokale Stash;
- Mogelijk generate een handtekening (`sig:...`) op de Consignment, om aan te tonen dat het is onderzocht en goedgekeurd (soms een "*payslip*" genoemd).


```bash
bob$ rgb accept consignment.rgb
sig:DbwzvSu4BZU81jEpE9FVZ3xjcyuTKWWy2gmdnaxtACrS
```


![RGB-Bitcoin](assets/en/077.webp)


#### 9) Optie: Bob stuurt bevestiging terug naar Alice (*strookje*)


Als Bob dit wenst, kan hij deze handtekening terugsturen naar Alice. Dit geeft aan:




- Dat het de overgang als geldig erkent;
- Dat hij ermee instemt dat de Bitcoin transactie wordt uitgezonden.


Dit is niet verplicht, maar het kan Alice de zekerheid geven dat er later geen geschillen over de overdracht zullen ontstaan.


#### 10) Alice ondertekent en publiceert de transactie


Alice kan dan:




- Controleer de handtekening van Bob (`RGB check <sig>`);
- Teken de *Witness Transaction* die nog steeds een PSBT is (`Wallet sign`);
- Publiceer de Witness Transaction op het Bitcoin netwerk (`-publish`).


```bash
alice$ rgb check <sig>
alice$ wallet sign —publish tx.psbt
```


![RGB-Bitcoin](assets/en/078.webp)


Eenmaal bevestigd, markeert deze transactie de afsluiting van de overdracht. Bob wordt de nieuwe eigenaar van het goed: hij heeft nu een Owned State die wijst naar de UTXO die hij controleert, wat bewezen wordt door de aanwezigheid van de Commitment in de transactie.


Samengevat is dit het volledige overdrachtsproces:


![RGB-Bitcoin](assets/en/079.webp)


### Voordelen van RGB overdrachten




- **Vertrouwelijkheid**:


Alleen Alice en Bob hebben toegang tot alle State Transition gegevens. Zij Exchange deze informatie buiten de Blockchain, via zendingen. De cryptografische vastleggingen in de Bitcoin transactie onthullen het type activa of het bedrag niet, wat een veel grotere vertrouwelijkheid garandeert dan andere On-Chain token systemen.




- **Klantzijdige validatie**:


Bob kan de consistentie van de overdracht controleren door de *Consignment* te vergelijken met de *ankers* in de Bitcoin Blockchain. Hij heeft geen validatie door derden nodig. Alice hoeft niet de volledige geschiedenis op de Blockchain te publiceren, wat de belasting van het basisprotocol vermindert en de vertrouwelijkheid verbetert.




- **Vereenvoudigde atomiciteit**:


Complexe uitwisselingen (atomaire swaps tussen BTC en een RGB activum, bijvoorbeeld) kunnen worden uitgevoerd binnen een enkele transactie, waardoor er geen HTLC of PTLC scripts nodig zijn. Als de overeenkomst niet wordt uitgezonden, kan iedereen zijn UTXO's op andere manieren hergebruiken.


### Overzichtsdiagram overdracht


Voordat we de facturen in meer detail bekijken, volgt hier een samenvattend schema van de algemene stroom van een RGB overboeking:




- Bob installeert een RGB Wallet en verkrijgt de initiële Contract Consignment;
- Bob geeft een Invoice uit waarin de UTXO wordt vermeld waar het actief moet worden ontvangen;
- Alice ontvangt de Invoice, bouwt de PSBT en genereert de Terminal Consignment;
- Bob accepteert het, controleert het, voegt de gegevens toe aan zijn Stash en ondertekent (*betaalbrief*) indien nodig;
- Alice publiceert de transactie op het Bitcoin netwerk;
- Bevestiging van de transactie maakt de overdracht officieel.


![RGB-Bitcoin](assets/en/080.webp)


De overdracht illustreert alle kracht en flexibiliteit van het RGB protocol: een private Exchange, gevalideerd aan de cliëntzijde, minimaal en discreet verankerd op de Bitcoin Blockchain, en met behoud van het beste van de veiligheid van het protocol (geen risico van Double-spending). Dit maakt RGB een veelbelovend ecosysteem voor waardeoverdrachten die vertrouwelijker en schaalbaarder zijn dan On-Chain programmeerbare blockchains.


### Facturen RGB


In dit deel zullen we in detail uitleggen hoe **facturen** werken in het RGB ecosysteem en hoe ze het mogelijk maken om operaties (in het bijzonder overschrijvingen) uit te voeren met een Contract. Eerst kijken we naar de identifiers die gebruikt worden, dan naar hoe ze gecodeerd worden en tenslotte naar de structuur van een Invoice uitgedrukt als een URL (een formaat dat handig genoeg is voor gebruik in wallets).


#### Identificatiemiddelen en codering


Er is een unieke identifier gedefinieerd voor elk van de volgende Elements:




- Een RGB Contract;
- Het is Schema (Business Logic);
- Het zijn Interface en Interface Implementation;
- Haar activa (tokens, NFT, enz.),


Deze uniciteit is erg belangrijk, want elk onderdeel van het systeem moet te onderscheiden zijn. Een Contract X mag bijvoorbeeld niet verward worden met een andere Contract Y, en twee verschillende interfaces (RGB20 vs. RGB21, bijvoorbeeld) moeten verschillende identificaties hebben.


Om deze identifiers zowel efficiënt (klein formaat) als leesbaar te maken, gebruiken we:




- Base58 codering, die het gebruik van verwarrende karakters (bijvoorbeeld `0` en de letter `O`) vermijdt en relatief korte strings oplevert;
- Een voorvoegsel dat de aard van de identifier aangeeft, meestal in de vorm van `RGB:` of een vergelijkbare URN.


Een `ContractId` kan bijvoorbeeld worden weergegeven door iets als:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```


Het `RGB:` voorvoegsel bevestigt dat dit een RGB identificatie is en geen HTTP link of ander protocol. Dankzij dit voorvoegsel kunnen wallets de string correct interpreteren.


#### Segmentatie van identificatoren


RGB identifiers zijn vaak erg lang, omdat de onderliggende (cryptografische) beveiliging velden van 256 bits of meer kan vereisen. Om het lezen en verifiëren door mensen te vergemakkelijken, *verdelen* we deze strings in verschillende blokken, gescheiden door een koppelteken (`-`). Dus in plaats van een lange, ononderbroken tekenreeks, verdelen we deze in kortere blokken. Deze praktijk is gebruikelijk voor creditcard- of telefoonnummers, en is hier ook van toepassing voor verificatiegemak. Een gebruiker of partner kan bijvoorbeeld te horen krijgen: "*Controleer of het derde blok `9GEgnyMj7`* is", in plaats van alles in één keer te moeten vergelijken. Het laatste blok wordt vaak gebruikt als een **checksum**, om een fout- of tikfoutdetectiesysteem te hebben.


Als voorbeeld zou een `ContractId` in base58 gecodeerd en gesegmenteerd kunnen zijn:


```txt
2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```


Elk van de streepjes breekt de string op in secties. Dit heeft geen invloed op de semantiek van de code, alleen op de presentatie.


#### URL's gebruiken voor facturen


Een RGB Invoice wordt gepresenteerd als een URL. Dit betekent dat het kan worden aangeklikt of gescand (als een QR-code), en een Wallet kan het direct interpreteren om een transactie uit te voeren. Deze eenvoudige interactie verschilt van sommige andere systemen waarbij je verschillende gegevens moet kopiëren en plakken in verschillende velden van de software.


Een Invoice voor een vervangbare token (bijvoorbeeld een RGB20 token) zou er zo uit kunnen zien:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```


Laten we deze URL analyseren:




- `RGB:`** (prefix): geeft een link aan die het RGB protocol aanroept (analoog aan `http:` of `Bitcoin:` in andere contexten);
- `2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX`: vertegenwoordigt de `ContractId` van de token die je wilt manipuleren;
- `/RGB20/100`: geeft aan dat de `RGB20` Interface wordt gebruikt en dat 100 eenheden van het goed worden gevraagd. De syntaxis is: `/Interface/bedrag`;
- `+utxob:`**: geeft aan dat informatie over de ontvanger UTXO (of, preciezer, de definitie van de Single-Use Seal) wordt toegevoegd;**
- `egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb`: dit is de *blinded* UTXO (of Seal Definition). Met andere woorden, Bob heeft zijn exacte UTXO gemaskeerd, dus de afzender (Alice) weet niet wat de exacte Address is. Ze weet alleen dat er een geldige Seal is, die verwijst naar een UTXO die Bob controleert.


Het feit dat alles in één URL past, maakt het leven van de gebruiker eenvoudiger: een simpele klik of scan in de Wallet en de bewerking is klaar om uitgevoerd te worden.


Je zou je systemen kunnen voorstellen waarbij een eenvoudige ticker (bijv. `USDT`) wordt gebruikt in plaats van de `ContractId`. Dit zou echter grote vertrouwens- en veiligheidsproblemen opleveren: een ticker is geen unieke referentie (verschillende contracten zouden kunnen claimen `USDT` te heten). Met RGB willen we een unieke, ondubbelzinnige cryptografische identificatiecode. Vandaar de keuze voor de 256-bits string, gecodeerd in base58 en gesegmenteerd. De gebruiker weet dat hij precies de Contract manipuleert wiens ID `2WBcas9-yjz...` is en niet een andere.


#### Extra URL-parameters


Je kunt ook extra parameters toevoegen aan de URL, op dezelfde manier als bij HTTP, zoals:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb?sig=6kzbKKffP6xftkxn9UP8gWqiC41W16wYKE5CYaVhmEve
```




- `?sig=...`: staat bijvoorbeeld voor een handtekening verbonden aan de Invoice, die sommige wallets kunnen verifiëren;
- Als een Wallet deze handtekening niet beheert, wordt deze parameter gewoon genegeerd.


Laten we het geval nemen van een NFT via de RGB21 Interface. We zouden bijvoorbeeld kunnen hebben:


```txt
rgb:7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK/RGB21/DbwzvSu-4BZU81jEp-E9FVZ3xj-cyuTKWWy-2gmdnaxt-ACrS+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```


Hier zien we:




- **gW-1917**: URL prefix;
- **`7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK`**: Contract ID (NFT);
- **rGB21**: Interface voor niet-vluchtige activa (NFT);
- `DbwzvSu-4BZU81jEp-...`: **een expliciete verwijzing naar het unieke deel van de NFT, bijvoorbeeld een Hash van de gegevensblob (media, metagegevens...);**
- **`+utxob:egXsFnw-...`**: de Seal Definition.


Het idee is hetzelfde: zend een unieke link die de Wallet kan interpreteren en die duidelijk het unieke goed identificeert dat moet worden overgedragen.


#### Andere bewerkingen via URL


RGB URL's worden niet alleen gebruikt om een overdracht aan te vragen. Ze kunnen ook meer geavanceerde operaties coderen, zoals het uitgeven van nieuwe tokens (*issuance*). Bijvoorbeeld:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/issue/100000+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```


Hier vinden we:




- gW-1924:`: protocol;
- `2WBcas9-...`: Contract ID;
- `/RGB20/issue/100000`: geeft aan dat je de "*Issue*" overgang wilt aanroepen om 100.000 extra tokens te maken;
- `+utxob:`: de Seal Definition.


Op de Wallet zou bijvoorbeeld kunnen staan: "Ik ben gevraagd om een `uitgifte` operatie uit te voeren van de `RGB20` Interface, op die en die Contract, voor 100.000 eenheden, ten voordele van die en die Single-Use Seal."


Nu we de belangrijkste Elements van RGB programmering hebben bekeken, neem ik je mee door het volgende hoofdstuk over hoe je een RGB Contract opstelt.


## Slimme contracten opstellen


<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>


:::video id=a3ad6dcd-90b8-4272-9dfc-76c85c859167:::


In dit hoofdstuk gaan we stap voor stap een Contract schrijven met behulp van de command-line tool `RGB`. Het doel is om te laten zien hoe je de CLI installeert en manipuleert, een **Schema** compileert, de **Interface** en de **Interface Implementation** importeert en vervolgens een asset uitgeeft (*issue*). We kijken ook naar de onderliggende logica, inclusief compilatie en toestandsvalidatie. Aan het eind van dit hoofdstuk zou je het proces moeten kunnen reproduceren en je eigen RGB contracten moeten kunnen maken.


Ter herinnering, de interne logica van RGB is gebaseerd op Rust bibliotheken die je als ontwikkelaar kunt importeren in je projecten om het Client-side Validation deel te beheren. Daarnaast werkt het LNP/BP Association team aan bindingen voor andere talen, maar dit is nog niet afgerond. Daarnaast ontwikkelen andere entiteiten zoals Bitfinex hun eigen integratiestacks (we zullen het hierover hebben in de laatste 2 hoofdstukken van de cursus). Voorlopig is daarom de `RGB` CLI de officiële referentie, ook al is deze nog relatief ongepolijst.


### Installatie en presentatie van het RGB gereedschap


Het hoofdcommando heet simpelweg `RGB`. Het is ontworpen om te lijken op `git`, met een set sub-commando's voor het manipuleren van contracten, het aanroepen ervan, het uitgeven van activa enzovoort. Bitcoin Wallet is momenteel nog niet geïntegreerd, maar dat zal wel gebeuren in een volgende versie (0.11). Deze volgende versie zal gebruikers in staat stellen om hun wallets te creëren en te beheren (via descriptors) direct vanuit `RGB`, inclusief PSBT generatie, compatibiliteit met externe hardware (bijv. een Hardware Wallet) voor ondertekening, en interoperabiliteit met software zoals Sparrow. Dit zal het hele scenario van uitgifte en overdracht van activa vereenvoudigen.


#### Installatie via Cargo


We installeren het gereedschap in Rust met:


```bash
cargo install rgb-contracts --all-features
```


(Opmerking: het krat heet `RGB-contracten`, en het geïnstalleerde commando zal `RGB` heten. Als er al een krat met de naam `RGB` bestond, kan er een botsing zijn geweest, vandaar de naam)


De installatie compileert een groot aantal afhankelijkheden (bijv. commandoparsing, Electrum-integratie, beheer van zero-knowledge bewijzen, enz.)


Zodra de installatie is voltooid, wordt de:


```bash
rgb
```


Het uitvoeren van `RGB` (zonder argumenten) toont een lijst met beschikbare sub-commando's, zoals `interfaces`, `Schema`, `import`, `export`, `issue`, `Invoice`, `transfer`, enz. Je kunt de lokale opslagmap wijzigen (een Stash die alle logs, schema's en implementaties bevat), het netwerk kiezen (Testnet, Mainnet) of je Electrum server configureren.


![RGB-Bitcoin](assets/en/081.webp)


#### Eerste overzicht van controles


Als je het volgende commando uitvoert, zul je zien dat er standaard al een `RGB20` Interface is geïntegreerd:


```bash
rgb interfaces
```


Als deze Interface niet geïntegreerd is, kloon dan de:


```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```


Compileer het:


```bash
cargo run
```


Importeer dan de Interface van je keuze:


```bash
rgb import interfaces/RGB20.rgb
```


![RGB-Bitcoin](assets/en/082.webp)


Aan de andere kant wordt ons verteld dat er nog geen Schema in de software is geïmporteerd. Er is ook geen Contract in de Stash. Voer het commando uit om het te zien:


```bash
rgb schemata
```


Je kunt dan het archief klonen om bepaalde schema's op te halen:


```bash
git clone https://github.com/RGB-WG/rgb-schemata
```


![RGB-Bitcoin](assets/en/083.webp)


Dit archief bevat in zijn `src/` map verschillende Rust bestanden (bijvoorbeeld `nia.rs`) die schema's definiëren (NIA voor "*Non Inflatable Asset*", UDA voor "*Unique Digital Asset*", enz.) Om te compileren kun je vervolgens uitvoeren:


```bash
cd rgb-schemata
cargo run
```


Dit genereert verschillende `.RGB` en `.rgba` bestanden die overeenkomen met de gecompileerde schema's. Je vindt hier bijvoorbeeld `NonInflatableAsset.RGB`.


#### Schema en Interface Implementation importeren


Je kunt nu het schema importeren in `RGB`:


```bash
rgb import schemata/NonInflatableAssets.rgb
```


![RGB-Bitcoin](assets/en/084.webp)


Dit voegt het toe aan de lokale Stash. Als we het volgende commando uitvoeren, zien we dat de Schema nu verschijnt:


```bash
rgb schemata
```


### Contract creatie (uitgifte)


Er zijn twee manieren om een nieuw bedrijfsmiddel te maken:




- Ofwel gebruiken we een script of code in Rust die een Contract bouwt door Schema velden in te vullen (Global State, Owned States, enz.) en een `.RGB` of `.rgba` bestand produceert;
- Of gebruik het `issue` subcommando direct, met een YAML (of TOML) bestand dat de eigenschappen van de token beschrijft.


Je kunt voorbeelden vinden in Rust in de `examples` map, die illustreren hoe je een `ContractBuilder` bouwt, de `Global State` invult (asset naam, ticker, Supply, datum, etc.), de Owned State definieert (aan welke UTXO het wordt toegewezen), en dit alles vervolgens compileert in een *Contract Consignment* die je kunt exporteren, valideren en importeren in een Stash.


De andere manier is om handmatig een YAML-bestand te bewerken om de `ticker`, de `naam`, de `Supply`, enzovoort aan te passen. Stel dat het bestand `RGB20-demo.yaml` heet. Je kunt opgeven:




- `spec`: ticker, naam, precisie;
- `terms`: een veld voor juridische kennisgevingen;
- `issuedSupply`: de hoeveelheid token die is uitgegeven;
- `toewijzingen`: geeft de Single-Use Seal (*Seal Definition*) en de ontgrendelde hoeveelheid aan.


Hier is een voorbeeld van een YAML-bestand om aan te maken:


```yaml
interface: RGB20Fixed

globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000

assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```


![RGB-Bitcoin](assets/en/085.webp)


Voer dan gewoon de opdracht uit:


```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```


![RGB-Bitcoin](assets/en/086.webp)


In mijn geval is de unieke Schema identifier (tussen enkele aanhalingstekens) `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` en ik heb geen emittent ingevuld. Dus mijn bestelling is:


```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```


Als je de Schema ID niet weet, voer dan het commando uit:


```bash
rgb schemata
```


De CLI antwoordt dat er een nieuwe Contract is uitgegeven en toegevoegd aan de Stash. Als we het volgende commando intypen, zien we dat er nu een extra Contract is, die overeenkomt met de zojuist uitgegeven Contract:


```bash
rgb contracts
```


![RGB-Bitcoin](assets/en/087.webp)


Dan toont het volgende commando de globale toestanden (naam, ticker, Supply...) en de lijst van Owned States, d.w.z. toewijzingen (bijvoorbeeld 1 miljoen `PBN` tokens gedefinieerd in UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).


```bash
rgb state '<ContractId>'
```


![RGB-Bitcoin](assets/en/088.webp)


### Exporteren, importeren en valideren


Om deze Contract te delen met andere gebruikers, kan deze worden geëxporteerd van de Stash naar een:


```bash
rgb export '<ContractId>' myContractPBN.rgb
```


![RGB-Bitcoin](assets/en/089.webp)


Het `myContractPBN.RGB` bestand kan worden doorgegeven aan een andere gebruiker, die het kan toevoegen aan zijn Stash met het commando:


```bash
rgb import myContractPBN.rgb
```


Bij het importeren, als het een eenvoudige *Contract Consignment* is, krijgen we een "`Importing Consignment RGB`" boodschap. Als het een grotere *State Transition Consignment* is, zal het commando anders zijn (`RGB accepteren`).


Om de geldigheid te garanderen, kun je ook de lokale validatiefunctie gebruiken. Je kunt bijvoorbeeld uitvoeren:


```bash
rgb validate myContract.rgb
```


#### Stash gebruik, verificatie en weergave


Ter herinnering, de Stash is een lokale inventaris van schema's, interfaces, implementaties en contracten (Genesis + overgangen). Elke keer dat je "import" uitvoert, voeg je een element toe aan de Stash. Deze Stash kan in detail bekeken worden met het commando:


```bash
rgb dump
```


![RGB-Bitcoin](assets/en/090.webp)


Hierdoor krijgt generate een map met details van de hele Stash.


### Overdracht en PSBT


Om een overdracht uit te voeren, moet je een lokale Bitcoin Wallet manipuleren om de `Tapret` of `Opret` verplichtingen te beheren.


#### generate en Invoice


In de meeste gevallen vindt interactie tussen de deelnemers aan een Contract (bijvoorbeeld Alice en Bob) plaats via het genereren van een Invoice. Als Alice wil dat Bob iets uitvoert (een token overdracht, een heruitgifte, een actie in een DAO, etc.), dan creëert Alice een Invoice met haar instructies aan Bob. Dus we hebben:




- **Alice** (de emittent van de Invoice);
- **Bob** (die de Invoice ontvangt en uitvoert).


In tegenstelling tot andere ecosystemen is een RGB Invoice niet beperkt tot het begrip betaling. Het kan elk verzoek inhouden dat gekoppeld is aan de Contract: een sleutel intrekken, stemmen, een gravure (*gravure*) maken op een NFT, enz. De overeenkomstige operatie kan worden beschreven in de Contract Interface. De overeenkomstige operatie kan beschreven worden in de Contract Interface.


Het volgende commando genereert een RGB Invoice:


```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```


Met:




- `$Contract`: Contract identificator (*ContractId*);
- `$Interface`: de Interface die moet worden gebruikt (bijvoorbeeld `RGB20`);
- `$ACTIE`: de naam van de operatie die in de Interface is gespecificeerd (voor een eenvoudige fungibele token overdracht kan dit "Transfer" zijn). Als de Interface al een standaard actie geeft, hoef je die hier niet opnieuw in te voeren;
- `$STATE`: de statusgegevens die moeten worden overgedragen (bijvoorbeeld een aantal tokens als een fungibele token wordt overgedragen);
- `$Seal`: de Single-Use Seal van de begunstigde (Alice), d.w.z. een expliciete verwijzing naar een UTXO. Bob zal deze informatie gebruiken om de Witness Transaction te bouwen, en de overeenkomstige uitvoer zal dan toebehoren aan Alice (in *blinded UTXO* of ongecodeerde vorm).


Bijvoorbeeld met de volgende commando's


```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```


De CLI lijkt op de generate en Invoice:


```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```


Het kan naar Bob worden verzonden via elk kanaal (tekst, QR-code, enz.).


#### Een overdracht doen


Om over te stappen van deze Invoice:




- Bob (die de tokens in zijn Stash heeft) heeft een Bitcoin Wallet. Hij moet een Bitcoin transactie voorbereiden (in de vorm van een PSBT, bijvoorbeeld `tx.PSBT`) die de UTXO's uitgeeft waar de benodigde RGB tokens zich bevinden, plus één UTXO voor valuta (Exchange);
- Bob voert het volgende commando uit:


```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```




- Dit genereert een `Consignment.RGB` bestand dat bevat:
 - De transitiegeschiedenis bewijst Alice dat de penningen echt zijn;
 - De nieuwe overgang die tokens overbrengt naar Alice's Single-Use Seal;
 - Een Witness Transaction (niet ondertekend).
- Bob stuurt dit `Consignment.RGB` bestand naar Alice (via e-mail, een sharing server of een RGB-RPC protocol, Storm, etc.);
- Alice ontvangt `Consignment.RGB` en accepteert het in zijn eigen Stash:


```bash
alice$ rgb accept consignment.rgb
```




- De CLI controleert de geldigheid van de overgang en voegt deze toe aan de Stash van de Alice. Als het commando ongeldig is, mislukt het met gedetailleerde foutmeldingen. Anders slaagt het en meldt dat de voorbeeldtransactie nog niet is uitgezonden op het Bitcoin netwerk (Bob wacht op Alice's Green licht);
- Ter bevestiging retourneert het `accept` commando een handtekening (*betaalbrief*) die Alice naar Bob kan sturen om hem te laten zien dat ze de *Consignment* heeft gevalideerd;
- Bob kan dan zijn Bitcoin-transactie ondertekenen en publiceren (`--publiceren`):


```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```




- Zodra deze transactie is bevestigd On-Chain, wordt Ownership van het actief beschouwd als overgedragen aan Alice. Wallet van Alice, die de Mining van de transactie controleert, ziet de nieuwe Owned State verschijnen in haar Stash.


In het volgende hoofdstuk gaan we dieper in op de integratie van RGB in de Lightning Network.


## RGB op de Lightning Network


<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>


:::video id=be25a165-6e23-488c-91d8-3dcfccc6eca1:::


In dit hoofdstuk stel ik voor om te onderzoeken hoe RGB gebruikt kan worden binnen Lightning Network, om RGB activa (tokens, NFT's, etc.) te integreren en te verplaatsen via off-chain betalingskanalen.


Het basisidee is dat de RGB State Transition (*State Transition*) kan worden gecommit in een Bitcoin transactie die op zijn beurt off-chain kan blijven totdat het Lightning kanaal wordt gesloten. Dus, elke keer dat het kanaal wordt bijgewerkt, kan een nieuwe RGB State Transition worden opgenomen in de nieuwe committende transactie, die dan de oude overgang ongeldig maakt. Op deze manier kunnen Lightning-kanalen worden gebruikt om RGB activa over te dragen, en kunnen ze op dezelfde manier worden gerouteerd als conventionele Lightning-betalingen.


### Creëren en financieren van kanalen


Om een Lightning-kanaal te maken dat RGB activa draagt, hebben we twee Elements nodig:




- Bitcoin financiering om de 2/2 Multisig van het kanaal te maken (de basis UTXO voor het kanaal);
- RGB financiering, die activa naar dezelfde Multisig stuurt.


In Bitcoin termen moet de financieringstransactie bestaan om de UTXO referentie te definiëren, zelfs als het slechts een kleine hoeveelheid Sats bevat (het is gewoon een kwestie van elke output in toekomstige Commitment transacties die toch boven de Dust limiet blijft). Alice kan bijvoorbeeld besluiten om 10k Sats en 500 USDT te leveren (uitgegeven als RGB activa). Op de financieringstransactie voegen we een Commitment (`Opret` of `Tapret`) toe, die de RGB State Transition verankert.


![RGB-Bitcoin](assets/en/091.webp)


Zodra de financieringstransactie is voorbereid (maar nog niet uitgezonden), worden Commitment transacties aangemaakt, zodat elke partij het kanaal op elk moment eenzijdig kan sluiten. Deze transacties lijken op de klassieke Commitment transacties van Lightning, behalve dat we een extra uitgang toevoegen met RGB Anchor (OP_RETURN of Taproot) gekoppeld aan de nieuwe State Transition.


De RGB State Transition verplaatst dan de activa van de 2/2 Multisig van de financiering naar de uitgangen van de Commitment Transaction. Het voordeel van dit proces is dat de veiligheid van de RGB toestand precies overeenkomt met de strafmechanismen van Lightning: als Bob een oude kanaaltoestand uitzendt, kan Alice hem straffen en de output uitgeven, om zowel de Sats als de RGB tokens terug te krijgen. De prikkel is daarom nog sterker dan in een Lightning kanaal zonder RGB activa, omdat een aanvaller niet alleen Sats kan verliezen, maar ook de RGB activa van het kanaal.


Een Commitment Transaction ondertekend door Alice en verzonden naar Bob zou er dus zo uitzien:


![RGB-Bitcoin](assets/en/092.webp)


En de begeleidende Commitment Transaction, ondertekend door Bob en verzonden naar Alice, ziet er als volgt uit:


![RGB-Bitcoin](assets/en/093.webp)


### Update kanaal


Wanneer er een betaling plaatsvindt tussen twee kanaaldeelnemers (of wanneer ze de toewijzing van de activa willen wijzigen), creëren ze een nieuw paar Commitment transacties. Het bedrag in Sats op elke uitgang kan al dan niet onveranderd blijven, afhankelijk van de implementatie, omdat de belangrijkste rol ervan is de constructie van geldige UTXO's mogelijk te maken. Aan de andere kant moet de OP_RETURN (of Taproot) uitgang worden gewijzigd om de nieuwe RGB Anchor te bevatten, die de nieuwe verdeling van activa in het kanaal weergeeft.


Als Alice bijvoorbeeld 30 USDT overmaakt naar Bob in het kanaal, zal de nieuwe State Transition een saldo weergeven van 400 USDT voor Alice en 100 USDT voor Bob. De vastlegtransactie wordt toegevoegd aan (of gewijzigd door) OP_RETURN/Taproot Anchor om deze overgang op te nemen. Merk op dat, vanuit het oogpunt van RGB, de input voor de overgang het initiële Multisig blijft (waar On-Chain activa feitelijk worden toegewezen totdat het kanaal sluit). Alleen de output van RGB (toewijzingen) verandert, afhankelijk van de herverdeling waartoe besloten is.


De Commitment Transaction getekend door Alice, klaar om gedistribueerd te worden door Bob:


![RGB-Bitcoin](assets/en/094.webp)


De Commitment Transaction ondertekend door Bob, klaar om gedistribueerd te worden door Alice:


![RGB-Bitcoin](assets/en/095.webp)


### HTLC beheer


In werkelijkheid maakt de Lightning Network het mogelijk om betalingen via meerdere kanalen te routeren, met behulp van HTLC's (*Hashed Time-Locked Contracts*). Hetzelfde geldt voor de RGB: voor elke betaling die door het kanaal gaat, wordt een HTLC uitgang toegevoegd aan de transactie en een RGB toewijzing gekoppeld aan deze HTLC. Dus, wie de HTLC uitgang uitgeeft (dankzij het geheim of na afloop van de tijdslot) krijgt zowel de Sats als de bijbehorende RGB activa terug. Aan de andere kant moet je natuurlijk wel genoeg geld op de weg hebben in de vorm van zowel Sats als RGB activa.


![RGB-Bitcoin](assets/en/096.webp)


De werking van de RGB op Lightning moet daarom parallel worden bekeken met die van de Lightning Network zelf. Als je dieper op dit onderwerp wilt ingaan, raad ik je van harte aan om deze andere uitgebreide training te bekijken:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### RGB code kaart


Tot slot wil ik, voordat we naar het volgende deel gaan, een overzicht geven van de code die gebruikt wordt in RGB. Het protocol is gebaseerd op een set Rust bibliotheken en open source specificaties. Hier is een overzicht van de belangrijkste repositories en kratten:


![RGB-Bitcoin](assets/en/097.webp)


#### Client-side Validation




- **Archief**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- **Kratten**: [client_side_validation](https://crates.io/crates/client_side_validation), [single_use_seals](https://crates.io/crates/single_use_seals)


Beheer van off-chain validatie en Single Use Seals logica.


#### Deterministische Bitcoin toezeggingen (DBC)




- **Archief**: [bp-kern](https://github.com/BP-WG/bp-core)
- **Krat**: [bp-dbc](https://crates.io/crates/bp-dbc)


Beheer van deterministische verankering in Bitcoin transacties (Tapret, OP_RETURN, enz.).


#### Multi Protocol Commitment (MPC)




- **Archief**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- **Krat**: [commit_verify](https://crates.io/crates/commit_verify)


Meerdere inschakelcombinaties en integratie met verschillende protocollen.


#### Strikte types & strikte codering




- **Specificaties**: [website strict-types.org](https://www.strict-types.org/)
- **Repositories**: [strikte types](https://github.com/strict-types/strict-types), [strikte codering](https://github.com/strict-types/strict-encoding)
- **Kratten**: [strikte_typen](https://crates.io/crates/strict_types), [strikte_codering](https://crates.io/crates/strict_encoding)


Het strikte typeringssysteem en de deterministische serialisatie gebruikt voor Client-side Validation.


#### RGB Kern




- **Archief**: [RGB-core](https://github.com/RGB-WG/RGB-core)
- **Krat**: [RGB-core](https://crates.io/crates/RGB-core)


De kern van het protocol, die de hoofdlogica van de RGB validatie omvat.


#### RGB-standaardbibliotheek & Wallet




- **Archief**: [RGB-std](https://github.com/RGB-WG/RGB-std)
- **Krat**: [RGB-std](https://crates.io/crates/RGB-std)


Standaard implementaties, Stash en Wallet beheer.


#### RGB CLI




- **Archief**: [RGB](https://github.com/RGB-WG/RGB)
- **Kratten**: [RGB-CLI](https://crates.io/crates/RGB-CLI), [RGB-Wallet](https://crates.io/crates/RGB-Wallet)


De `RGB` CLI en crate Wallet, voor commandoregelmanipulatie van contracten.


#### RGB Schema




- **Archief**: [RGB-schemata](https://github.com/RGB-WG/RGB-schemata/)


Bevat voorbeelden van schema's (NIA, UDA, enz.) en hun implementaties.


#### AluVM




- **Info**: [AluVM.org](https://www.AluVM.org/)
- **Repositories**: [AluVM-spec](https://github.com/AluVM/AluVM-spec), [alure](https://github.com/AluVM/alure)
- **Kratten**: [AluVM](https://crates.io/crates/AluVM), [aluasm](https://crates.io/crates/aluasm)


Op register gebaseerde virtuele machine die wordt gebruikt om validatiescripts uit te voeren.


#### Bitcoin-protocol - BP




- **Repositories**: [bp-kern](https://github.com/BP-WG/bp-core), [bp-std](https://github.com/BP-WG/bp-std), [bp-Wallet](https://github.com/BP-WG/bp-Wallet)


Toevoegingen om het Bitcoin protocol te ondersteunen (transacties, bypasses, enz.).


#### Ubiquitair deterministisch computergebruik - UBIDECO




- **Archief**: [UBIDECO](https://github.com/UBIDECO)


Ecosysteem gekoppeld aan open-source deterministische ontwikkelingen.


# Voortbouwen op RGB


<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>


## DIBA en het Bitmask-project


<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>


:::video id=2ec9a181-a8b0-4da2-b7b5-9dfaaaeb10ba:::


Dit laatste deel van de cursus is gebaseerd op presentaties van verschillende sprekers tijdens het RGB bootcamp. Het bevat getuigenissen en reflecties over RGB en zijn ecosysteem, en presentaties van tools en projecten gebaseerd op het protocol. Dit eerste hoofdstuk wordt gemodereerd door Hunter Beast, en de volgende twee door Frederico Tenga.


### Van JavaScript naar Rust en naar het Bitcoin ecosysteem


In het begin werkte Hunter Beast voornamelijk in JavaScript. Toen ontdekte hij **Rust**, waarvan de syntax in eerste instantie onaantrekkelijk en frustrerend leek. Hij begon echter de kracht van de taal te waarderen, de controle over het geheugen (*heap* en *stack*) en de veiligheid en prestaties die ermee gepaard gaan. Hij benadrukt dat Rust een uitstekende training is voor een diepgaand begrip van hoe een computer werkt.


Hunter Beast vertelt over zijn achtergrond in verschillende projecten in het *Altcoin* ecosysteem, zoals Ethereum (met Solidity, TypeScript, enz.), en later Filecoin. Hij legt uit dat hij aanvankelijk onder de indruk was van sommige protocollen, maar uiteindelijk gedesillusioneerd raakte door de meeste ervan, niet in de laatste plaats vanwege hun tokenomics. Hij hekelt de dubieuze financiële prikkels, de inflatoire creatie van tokens waardoor investeerders verwateren, en het potentieel uitbuitende aspect van deze projecten. Uiteindelijk nam hij een **Bitcoin Maximalist** standpunt in, niet in het minst omdat sommige mensen hem de ogen openden voor de gezondere economische mechanismen van Bitcoin en voor de robuustheid van dit systeem.


### De aantrekkingskracht van RGB en bouwen op lagen


Wat hem definitief overtuigde van de relevantie van Bitcoin, was volgens hem de ontdekking van RGB en het concept van lagen. Hij gelooft dat bestaande functionaliteiten op andere blockchains gereproduceerd kunnen worden op hogere lagen, boven Bitcoin, zonder het basisprotocol te veranderen.


In februari 2022 kwam hij bij **DIBA** om specifiek aan RGB te werken, en in het bijzonder aan de **Bitmask** Wallet. Bitmask zat toen nog op versie 0.01 en draaide RGB op versie 0.4, alleen voor het beheer van losse tokens. Hij merkt op dat dit minder op zichzelf gericht was dan tegenwoordig, omdat de logica deels op de server gebaseerd was. Sindsdien is de architectuur geëvolueerd naar dit model, dat zeer gewaardeerd wordt door bitcoiners.


### De fundamenten van het RGB protocol


Het **RGB** protocol is de meest recente en meest geavanceerde belichaming van het _gekleurde munten_ concept, dat al rond 2012-2013 werd onderzocht. Destijds zochten verschillende teams naar mogelijkheden om verschillende Bitcoin waarden te koppelen aan UTXO's, wat leidde tot verschillende verspreide implementaties. Dit gebrek aan standaardisatie en de lage vraag op dat moment zorgden ervoor dat deze oplossingen geen blijvende voet aan de grond kregen.


RGB onderscheidt zich tegenwoordig door zijn conceptuele robuustheid en uniforme specificaties via de LNP/BP associatie. Het principe is gebaseerd op Client-side Validation. Bitcoin Blockchain slaat alleen cryptografische verbintenissen op (_commitments_, via Taproot of OP_RETURN), terwijl de meerderheid van de gegevens (Contract definities, overdrachtsgeschiedenissen, etc.) wordt opgeslagen door de betrokken gebruikers. Op deze manier wordt de opslagbelasting verdeeld en de vertrouwelijkheid van uitwisselingen versterkt, zonder de Blockchain te belasten. Deze aanpak maakt de creatie van fungibele activa (**RGB20** standaard) of unieke activa (**RGB21** standaard) mogelijk, binnen een modulair en schaalbaar kader.


### De token-functie (RGB20) en unieke activa (RGB21)


Met **RGB20** definiëren we een fungibele token op Bitcoin. De uitgever kiest een _levering_, een _precisie_, en creëert een _contract_ waarin hij vervolgens overboekingen kan doen. Elke overboeking wordt doorverwezen naar een Bitcoin UTXO, die fungeert als een *Single-Use Seal*. Deze logica zorgt ervoor dat de gebruiker hetzelfde goed niet twee keer kan uitgeven, omdat alleen de persoon die in staat is de UTXO uit te geven, de sleutel bezit om de toestand van de Contract aan de cliëntzijde bij te werken.


**RGB21** richt zich op unieke activa (of "NFT"). De asset heeft een Supply van 1, en kan geassocieerd worden met metadata (afbeeldingsbestand, audio, enz.) beschreven via een specifiek veld. In tegenstelling tot NFT's op openbare blockchains, kunnen gegevens en hun MIME-identifiers privé blijven, gedistribueerd peer-to-peer naar goeddunken van de eigenaar.


### De Bitmask-oplossing: een Wallet voor RGB


Om de mogelijkheden van RGB in de praktijk te benutten, heeft het **DIBA** project een Wallet ontworpen genaamd [Bitmask](https://bitmask.app/). Het idee is om een niet-custodiaal, op Taproot gebaseerd hulpmiddel aan te bieden, dat toegankelijk is als webapplicatie of browserextensie. Bitmask beheert zowel RGB20 als RGB21 middelen en integreert verschillende beveiligingsmechanismen:




- De kerncode is geschreven in Rust en vervolgens gecompileerd in WebAssembly om te draaien in een JavaScript-omgeving (React);
- Sleutels worden lokaal gegenereerd en vervolgens versleuteld lokaal opgeslagen;
- Toestandsgegevens (Stash) worden in het geheugen bewaard, geserialiseerd en versleuteld via de **Carbonado** bibliotheek, die compressie, foutcorrectie, versleuteling en streamverificatie uitvoert met Blake3.


Dankzij deze architectuur vinden alle activatransacties plaats aan de kant van de klant. Van buitenaf is de Bitcoin transactie niets meer dan een klassieke Taproot bestedingstransactie, waarvan niemand zou vermoeden dat het ook een overdracht van fungibele tokens of NFT's betreft. De afwezigheid van On-Chain overloading (geen publiek opgeslagen metadata) garandeert een zekere mate van discretie en maakt het makkelijker om mogelijke censuurpogingen te weerstaan.


### Beveiliging en gedistribueerde architectuur


Aangezien het RGB protocol vereist dat elke deelnemer zijn transactiegeschiedenis bewaart (om de geldigheid van de ontvangen transfers te bewijzen), rijst de vraag over opslag. Bitmask stelt voor om deze Stash lokaal te serialiseren en vervolgens naar verschillende servers of clouds te sturen (optioneel). De gegevens blijven versleuteld door de gebruiker via **Carbonado**, zodat een server ze niet kan lezen. In het geval van gedeeltelijke corruptie kan de foutcorrectie Layer de inhoud opnieuw samenstellen.


Het gebruik van CRDT (_Conflict-free replicated data type_) maakt het mogelijk om verschillende versies van de Stash samen te voegen, mochten ze uiteenlopen. Iedereen is vrij om deze gegevens te hosten waar ze maar willen, omdat geen enkele Full node alle informatie bevat die aan het object is gekoppeld. Dit weerspiegelt precies de *Client-side Validation* filosofie, waar elke eigenaar verantwoordelijk is voor het opslaan van bewijs van de geldigheid van hun RGB bezit.


### Naar een breder ecosysteem: marktplaats, interoperabiliteit en nieuwe functies


Het bedrijf achter Bitmask beperkt zich niet tot de eenvoudige ontwikkeling van een Wallet. DIBA is van plan om te ontwikkelen:




- Een **marktplaats** voor het uitwisselen van tokens, vooral in **RGB21** vorm;
- Compatibiliteit met andere portemonnees (zoals *Iris Wallet*);
- **Transfer batching** technieken, d.w.z. de mogelijkheid om meerdere opeenvolgende RGB transfers in een enkele transactie op te nemen.


Tegelijkertijd werken we aan **WebBTC** of **WebLN** (standaarden waarmee websites de Wallet kunnen vragen om Bitcoin- of Lightning-transacties te ondertekenen), evenals aan de mogelijkheid om Ordinals-items te "telebranden" (als we Ordinals willen repatriëren naar een discreter en flexibeler RGB-formaat).


### Conclusie


Het hele proces laat zien hoe het RGB ecosysteem kan worden ingezet en toegankelijk gemaakt voor eindgebruikers door middel van robuuste technische oplossingen. De overgang van een Altcoin-perspectief naar een meer Bitcoin-gerichte visie, gekoppeld aan de ontdekking van *Client-side Validation*, illustreert een vrij logisch pad: we begrijpen dat het mogelijk is om verschillende functionaliteiten te implementeren (fungibele tokens, NFT, slimme contracten...) zonder de Blockchain te forken, simpelweg door gebruik te maken van cryptografische verplichtingen op Taproot transacties of OP_RETURNs.


De **Bitmask** Wallet maakt deel uit van deze benadering: aan de Blockchain kant zie je alleen een gewone Bitcoin transactie; aan de gebruikerskant manipuleer je een web Interface waar je allerlei off-chain activa creëert, Exchange en opslaat. Dit model scheidt de monetaire infrastructuur (Bitcoin) duidelijk van de uitgifte- en overdrachtslogica (RGB), terwijl het een hoog niveau van vertrouwelijkheid en betere schaalbaarheid garandeert.


## Bitfinex' werk aan RGB


<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>


:::video id=04555813-516f-4eea-9767-7082c2ea6f01:::


In dit hoofdstuk, gebaseerd op een presentatie van Frederico Tenga, kijken we naar een verzameling gereedschappen en projecten die gemaakt zijn door het Bitfinex team, gewijd aan RGB, met als doel het bevorderen van de opkomst van een rijk en divers ecosysteem rond dit protocol. Het oorspronkelijke doel van het team is niet om een specifiek commercieel product uit te brengen, maar om softwarebouwstenen te leveren, bij te dragen aan het RGB-protocol zelf en concrete implementatiereferenties voor te stellen, zoals een mobiele Wallet (*Iris Wallet*) of een RGB-compatibele Lightning-node.


### Achtergrond en doelstellingen


Sinds ongeveer 2022 concentreert het RGB-team van Bitfinex zich op de ontwikkeling van de technologiestack waarmee RGB efficiënt kan worden geëxploiteerd en getest. Er zijn verschillende bijdragen geleverd:




- Deelname aan broncode en protocolspecificaties, inclusief het schrijven van verbetervoorstellen, oplossen van bugs, etc;
- Tools voor ontwikkelaars om de integratie van RGB in hun toepassingen te vereenvoudigen;
- Ontwerp van een mobiele Wallet met de naam [Iris] (https://iriswallet.com/) om te experimenteren en best practices voor het gebruik van RGB te illustreren;
- Creatie van een aangepast Lightning-knooppunt dat kanalen met RGB-activa kan beheren;
- Ondersteunen van andere teams die oplossingen bouwen voor RGB, om diversiteit en een sterk ecosysteem aan te moedigen.


Deze aanpak is erop gericht om de hele keten van behoeften te dekken: van de low-level bibliotheek (*[RGBlib](https://github.com/RGB-Tools/RGB-lib)*), die de implementatie van een Wallet mogelijk maakt, tot het productie-aspect (een Lightning node, een Wallet voor Android, enz.).


### De RGBlib bibliotheek: vereenvoudiging van de ontwikkeling van RGB toepassingen


Een belangrijk punt bij het democratiseren van het maken van RGB wallets en applicaties is het beschikbaar maken van een abstractie die eenvoudig genoeg is, zodat ontwikkelaars niet alles hoeven te leren over de interne logica van het protocol. Dit is precies het doel van **RGBlib**, geschreven in Rust.


RGBlib fungeert als een brug tussen de zeer flexibele (maar soms complexe) vereisten van RGB die we in voorgaande hoofdstukken hebben kunnen bestuderen, en de concrete behoeften van een applicatieontwikkelaar. Met andere woorden, een Wallet (of dienst) die token overdrachten, uitgifte van activa, verificatie, enz. wil beheren, kan vertrouwen op RGBlib zonder elk cryptografisch detail of elke aanpasbare RGB parameter te kennen.


De boekwinkel biedt:




- Kant-en-klare functies voor het uitgeven (_uitgeven_) van activa (fungibel of niet);
- De mogelijkheid om activa over te dragen (verzenden/ontvangen) door eenvoudige objecten te manipuleren (adressen, bedragen, UTXO's, enz.);
- Een mechanisme voor het opslaan en laden van de statusinformatie (*consignments*) die nodig is voor Client-side Validation.


RGBlib vertrouwt daarom op complexe noties die specifiek zijn voor RGB (Client-side Validation, Tapret/Opret ankers), maar kapselt ze in zodat de uiteindelijke toepassing niet alles opnieuw hoeft te programmeren of riskante beslissingen hoeft te nemen. Bovendien is RGBlib al ingebed in verschillende talen (Kotlin en Python), wat de deur opent naar toepassingen die verder gaan dan een eenvoudig Rust-universum.


### Iris Wallet: een voorbeeld van een RGB Wallet op Android


Om de effectiviteit van RGBlib te bewijzen, heeft het Bitfinex-team **Iris Wallet** ontwikkeld, in dit stadium uitsluitend voor Android. Het is een mobiele Wallet die een gebruikerservaring laat zien die vergelijkbaar is met die van een gewone Wallet: je kunt een activum uitgeven, verzenden, ontvangen en de geschiedenis ervan bekijken, terwijl je op een self-custody model blijft.


Iris heeft een aantal interessante functies:


**Een Electrum-server gebruiken:**


Net als elke Wallet moet Iris op de hoogte zijn van transactiebevestigingen op de Blockchain. In plaats van een compleet knooppunt in te bouwen, gebruikt Iris standaard een Electrum-server die wordt onderhouden door het Bitfinex-team. Gebruikers kunnen echter hun eigen server of een andere service van derden configureren. Op deze manier kunnen Bitcoin transacties worden gevalideerd en informatie worden opgehaald (indexering) op een modulaire manier.


**De RGB proxyserver:**


In tegenstelling tot Bitcoin vereist RGB de Exchange van off-chain metadata (*consignments*) tussen zender en ontvanger. Om dit proces te vereenvoudigen, biedt Iris een oplossing waarbij de communicatie plaatsvindt via een proxyserver. De ontvangende Wallet genereert een *Invoice* die vermeldt waar de verzender de *client-side* gegevens naartoe moet sturen. Standaard wijst de URL naar een proxy gehost door het Bitfinex team, maar je kunt deze proxy wijzigen (of je eigen proxy hosten). Het idee is om terug te keren naar een vertrouwde gebruikerservaring waarbij de ontvanger een QR-code toont en de verzender deze code scant voor de transactie, zonder ingewikkelde extra manipulaties.


**Continue back-up:**


In een strikt Bitcoin context is een back-up van je seed over het algemeen voldoende (hoewel we tegenwoordig aanraden om in plaats daarvan een back-up te maken van de seed en de descriptors). Met RGB is dit niet genoeg: je moet ook de lokale geschiedenis bewaren (de *consignments*) die bewijzen dat je echt een RGB bezit. Elke keer dat u een ontvangstbewijs ontvangt, slaat het apparaat nieuwe gegevens op, die essentieel zijn voor latere uitgaven. Iris beheert automatisch een versleutelde back-up in de Google Drive van de gebruiker. Dit vereist geen speciaal vertrouwen in Google, omdat de back-up versleuteld is, en er zijn robuustere opties (zoals een persoonlijke server) gepland voor de toekomst om elk risico op censuur of verwijdering door een derde partij te vermijden.


**Andere kenmerken:**




- Maak een Faucet om snel tokens te testen of uit te delen voor experimenten of promotie;
- Een certificeringssysteem (momenteel gecentraliseerd) om een legitieme token te onderscheiden van een valse die een bekende ticker kopieert. In de toekomst kan deze certificering meer gedecentraliseerd worden (via DNS of andere mechanismen).


Al met al biedt Iris een gebruikerservaring die dicht in de buurt komt van die van een klassieke Bitcoin Wallet, waarbij de extra complexiteit (Stash beheer, *Consignment* geschiedenis, etc.) wordt gemaskeerd dankzij RGBlib en het gebruik van een proxyserver.


### Proxyserver en gebruikerservaring


De hierboven geïntroduceerde proxyserver verdient het om nader beschreven te worden, omdat het de sleutel is tot een soepele gebruikerservaring. In plaats van dat de verzender de *zendingen* handmatig naar de ontvanger moet sturen, vindt de RGB transactie op de achtergrond plaats via een:




- De ontvanger genereert een *Invoice* (die onder andere de proxy Address bevat);
- De verzender stuurt (via een HTTP-verzoek) een overgangsproject (de *Consignment*) naar de proxy;
- De ontvanger haalt dit project op, voert de *client-side* validatie lokaal uit;
- De ontvanger publiceert dan, via de proxy, de acceptatie (of mogelijk afwijzing) van de State Transition;
- De verzender kan de validatiestatus bekijken en, indien geaccepteerd, de Bitcoin transactie uitzenden om de overdracht te voltooien.


Op deze manier gedraagt de Wallet zich bijna als een normale Wallet. De gebruiker is zich niet bewust van alle tussenstappen. Toegegeven, de huidige proxy is niet versleuteld of geauthenticeerd (waardoor er zorgen blijven bestaan over vertrouwelijkheid en integriteit), maar deze verbeteringen zijn mogelijk in latere versies. Het proxy-concept blijft uiterst nuttig voor het nabootsen van de "ik stuur een QR-code, jij scant om te betalen"-ervaring.


### RGB integratie op de Lightning Network


Een ander belangrijk aandachtspunt van het Bitfinex-team is om de Lightning Network compatibel te maken met RGB activa. Het doel is om Lightning-kanalen in USDT (of elke andere token) mogelijk te maken en te profiteren van dezelfde voordelen als Bitcoin op Lightning (bijna onmiddellijke transacties, routing, enz.). Concreet houdt dit in dat er een Lightning-knooppunt wordt gemaakt dat is aangepast om:




- Open een kanaal door niet alleen satoshi's, maar ook een of meer RGB activa in de financiering UTXO Multisig te plaatsen;
- generate Lightning Commitment transacties (Bitcoin kant) vergezeld van overeenkomstige RGB toestandsovergangen. Elke keer dat het kanaal wordt bijgewerkt, herdefinieert een RGB overgang de activadistributie in de Lightning uitgangen;
- Eenzijdige afsluiting mogelijk maken, waarbij het goed wordt opgehaald in een exclusieve UTXO, in overeenstemming met Lightning Network regels (HTLC, tijdslot, straf, enz.).


Deze oplossing, genaamd "**RGB Lightning Node**", gebruikt LDK (*Lightning Dev Kit*) als basis en voegt de mechanismen toe die nodig zijn om RGB tokens in de kanalen te injecteren. Lightning verbintenissen behouden de klassieke structuur (punctureerbare uitgangen, timelock...), en daarnaast Anchor en RGB State Transition (via `Opret` of `Tapret`). Voor de gebruiker opent dit de weg naar Lightning-kanalen in stablecoins of in elk ander activum dat via RGB wordt geëmitteerd.


### DEX-potentieel en invloed op Bitcoin


Zodra meerdere activa worden beheerd via Lightning, wordt het mogelijk om een **atomische Exchange** voor te stellen op een enkel Lightning routingpad, met behulp van dezelfde logica van geheimen en timelocks. Bijvoorbeeld, gebruiker A heeft Bitcoin op een Lightning-kanaal, en gebruiker B heeft USDT RGB op een ander Lightning-kanaal. Ze kunnen een pad bouwen dat hun twee kanalen verbindt en tegelijkertijd Exchange BTC voor USDT, zonder dat er vertrouwen nodig is. Dit is niets meer dan een **atomische swap** die plaatsvindt in verschillende hops, waardoor externe deelnemers zich bijna niet bewust zijn van het feit dat ze een transactie uitvoeren, en niet alleen een routering. Deze aanpak biedt:




- Zeer lage latency, want alles blijft off-chain op Lightning.
- Een superieure **privacy**: niemand weet dat het een trade is en geen normale routing;
- Frontrunning vermijden, een terugkerend probleem voor On-Chain DEX;
- Lagere kosten (je betaalt geen blockspace, alleen Lightning routing fees).


We kunnen ons dan een ecosysteem voorstellen waar Lightning-knooppunten ruilprijzen aanbieden (door liquiditeit te verschaffen). Elk knooppunt kan, indien gewenst, de rol van _marktmaker_ spelen en verschillende activa op Lightning kopen en verkopen. Dit vooruitzicht van een _layer-2_ DEX versterkt het idee dat het niet nodig is om Fork of blockchains van derden te gebruiken om gedecentraliseerde asset exchanges te verkrijgen.


De impact op Bitcoin zou positief kunnen zijn: De infrastructuur van Lightning (nodes, kanalen en diensten) zou vollediger benut worden dankzij de volumes die gegenereerd worden door deze *stablecoins*, derivaten en andere tokens. Handelaars die geïnteresseerd zijn in USDT-betalingen op Lightning zouden mechanisch BTC-betalingen op Lightning ontdekken (beheerd door dezelfde stack). Het onderhoud en de financiering van de Lightning Network infrastructuur zou ook kunnen profiteren van de vermenigvuldiging van deze niet-BTC stromen, wat indirect ten goede zou komen aan Bitcoin gebruikers.


### Conclusie en bronnen


Het Bitfinex-team dat zich bezighoudt met RGB illustreert met zijn werk de diversiteit van wat er gedaan kan worden bovenop het protocol. Aan de ene kant is er RGBlib, een bibliotheek die het ontwerpen van wallets en toepassingen vergemakkelijkt. Aan de andere kant hebben we Iris Wallet, een praktische demonstratie op Android van een nette eindgebruiker Interface. Tot slot laat de integratie van RGB met Lightning zien dat stablecoin-kanalen mogelijk zijn en opent het de weg naar een potentiële gedecentraliseerde DEX op Lightning.


Deze aanpak blijft grotendeels experimenteel en blijft in ontwikkeling: de RGBlib bibliotheek wordt gaandeweg verfijnd, Iris Wallet krijgt regelmatig verbeteringen en de speciale Lightning node is nog geen mainstream Lightning client.


Voor degenen die meer willen weten of een bijdrage willen leveren, zijn er verschillende bronnen beschikbaar, waaronder:




- [GitHub RGB Tools repositories](https://github.com/RGB-Tools);
- [Een informatiesite gewijd aan de Iris Wallet](https://iriswallet.com/) om de Wallet op Android te testen.


In het volgende hoofdstuk bekijken we hoe we een RGB Lightning knooppunt kunnen lanceren.


## RLN - RGB Bliksemknooppunt


<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>


:::video id=d1e9753e-6093-4a47-bcdc-da1aebaefffc:::


In dit laatste hoofdstuk neemt Frederico Tenga je stap-voor-stap mee door het opzetten van een Lightning RGB knooppunt op een Regtest omgeving, en laat hij zien hoe je RGB tokens daarop kunt creëren. Door twee aparte knooppunten te lanceren, ontdek je ook hoe je een Lightning-kanaal kunt openen tussen deze knooppunten en Exchange RGB assets.


Deze video dient als een tutorial, vergelijkbaar met wat we in een vorig hoofdstuk hebben behandeld, maar deze keer specifiek gericht op Lightning!


De belangrijkste bron voor deze video is de Github-repository [RGB Lightning Node] (https://github.com/RGB-Tools/RGB-lightning-node), die het je gemakkelijk maakt om deze configuratie in Regtest te starten.


### Een RGB-compatibel Lightning knooppunt inzetten


In dit proces worden alle concepten uit de voorgaande hoofdstukken opgenomen en in praktijk gebracht:




- Het idee dat **UTXO** geblokkeerd op een 2/2 Multisig van een Lightning-kanaal niet alleen bitcoins kan ontvangen, maar ook een Single-Use Seal van RGB activa (fungibel of niet) kan zijn;
- De toevoeging, in elke Lightning engagement transactie, van een uitgang (`Tapret` of `Opret`) gewijd aan het verankeren van de RGB State Transition;
- De bijbehorende infrastructuur (bitcoind/indexer/proxy) om Bitcoin transacties en Exchange *client-side* gegevens te valideren.


### RGB-lightning-node introduceren


Het **`RGB-lightning-node``** project is een Rust daemon gebaseerd op een `Rust-lightning` (LDK) Fork aangepast om rekening te houden met het bestaan van RGB activa in een kanaal. Wanneer een kanaal wordt geopend, kan de aanwezigheid van activa worden gespecificeerd, en elke keer dat de kanaaltoestand wordt bijgewerkt, wordt een RGB overgang gecreëerd, die de verdeling van de activa in de Lightning-uitgangen weergeeft. Dit maakt het mogelijk:




- Open bijvoorbeeld Lightning-kanalen in USDT;
- Routeer deze tokens door het netwerk, op voorwaarde dat de routepaden voldoende liquiditeit hebben;
- Maak gebruik van Lightning's straf- en tijdslotlogica zonder aanpassingen: gewoon Anchor de RGB overgang in een extra uitgang van de Commitment Transaction.


De code is nog in het alfa stadium: we raden aan om het alleen te gebruiken in **regtest** of op de **Testnet**.


### Node-installatie


Om de `RGB-lightning-node` binary te compileren en installeren, beginnen we met het klonen van het archief en zijn submodules, daarna draaien we de:


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RGB-Bitcoin](assets/en/098.webp)




- De `--recurse-submodules` optie kloont ook de benodigde sub-devices (inclusief de gewijzigde versie van `Rust-lightning`);
- De `--shallow-submodules` optie beperkt de diepte van de kloon om het downloaden te versnellen, terwijl het nog steeds toegang geeft tot essentiële commits.


Voer vanuit de project root het volgende commando uit om de binary te compileren en te installeren:


```bash
cargo install --locked --debug --path .
```


![RGB-Bitcoin](assets/en/099.webp)




- `--locked` zorgt ervoor dat de versie van afhankelijkheden strikt wordt gerespecteerd;
- `--debug` is niet verplicht, maar kan je helpen focussen (je kunt `--release` gebruiken als je dat liever hebt);
- `--path .` vertelt `cargo install` om te installeren vanuit de huidige map.


Aan het einde van dit commando zal een `RGB-lightning-node` executable beschikbaar zijn in je `$CARGO_HOME/bin/`. Zorg ervoor dat dit pad in je `$PATH` staat zodat je het commando vanuit elke map kunt aanroepen.


### Prestatie-eisen


Om te kunnen functioneren, vereist de `RGB-lightning-node` daemon de aanwezigheid en configuratie van:




- Een **`bitcoind`** knooppunt


Elke RLN instantie zal moeten communiceren met `bitcoind` om zijn On-Chain transacties uit te zenden en te monitoren. Authenticatie (login/wachtwoord) en URL (host/poort) moeten worden verstrekt aan de daemon.




- Een **indexer** (Electrum of Esplora)


De daemon moet On-Chain transacties kunnen oplijsten en verkennen, in het bijzonder om de UTXO te vinden waarop een actief is verankerd. Je moet de URL van je Electrum server of Esplora specificeren.




- Een **RGB** proxy


Zoals in de vorige hoofdstukken, is de **proxyserver** een component (optioneel, maar ten zeerste aanbevolen) om de Exchange van *opdrachten* tussen Lightning peers te vereenvoudigen. Ook hier moet een URL worden opgegeven.


ID's en URL's worden ingevoerd wanneer de daemon _ontgrendeld_ wordt via de API. Hierover later meer.


### Start Regtest


Voor eenvoudig gebruik is er een `regtest.sh` script dat automatisch, via Docker, een set services start: `bitcoind`, `electrs` (indexer), `RGB-proxy-server`.


![RGB-Bitcoin](assets/en/100.webp)


Hiermee kun je een lokale, geïsoleerde, vooraf geconfigureerde omgeving starten. Het creëert en vernietigt containers en datamappen bij elke herstart. We beginnen met het starten van de:


```bash
./regtest.sh start
```


Dit script zal:




- Maak een `docker/` map om op te slaan;
- Voer `bitcoind` uit in regtest, evenals de indexer `electrs` en de `RGB-proxy-server`;
- Wacht tot alles klaar is voor gebruik.


![RGB-Bitcoin](assets/en/101.webp)


Vervolgens zullen we verschillende RLN nodes starten. Voer in aparte shells bijvoorbeeld het volgende uit (om 3 RLN nodes te starten):


```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```


![RGB-Bitcoin](assets/en/102.webp)




- De `--netwerk regtest` parameter geeft het gebruik van de regtest configuratie aan;
- `--daemon-luisteren-poort` geeft aan op welke REST-poort het Lightning knooppunt zal luisteren voor API-aanroepen (JSON);
- `--ldk-peer-listening-port` specificeert op welke Lightning P2P poort geluisterd moet worden;
- `dataldk0/`, `dataldk1/` zijn de paden naar de opslagmappen (elk knooppunt slaat zijn info apart op).


U kunt ook opdrachten uitvoeren op uw RLN nodes vanuit uw browser:


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


Om een kanaal te kunnen openen, moet een node eerst bitcoins hebben op een Address die gegenereerd is met het volgende commando (bijvoorbeeld voor node n°1):


```bash
curl -X POST http://localhost:3001/address
```


Het antwoord geeft je een Address.


![RGB-Bitcoin](assets/en/103.webp)


Op de `bitcoind` Regtest gaan we een paar bitcoins delven. Uitvoeren:


```bash
./regtest.sh mine 101
```


![RGB-Bitcoin](assets/en/104.webp)


Stuur geld naar het hierboven gegenereerde knooppunt Address:


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RGB-Bitcoin](assets/en/105.webp)


Mijn dan een blok om de transactie te bevestigen:


```bash
./regtest.sh mine 1
```


![RGB-Bitcoin](assets/en/106.webp)


### Testnet lancering (zonder Docker)


Als je een realistischer scenario wilt testen, kun je 3 RLN nodes lanceren op de Testnet in plaats van in Regtest, wijzend naar publieke diensten:


```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```


Als er standaard geen configuratie wordt gevonden, zal de daemon proberen de:




- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-RPC`


Met aanmelding:




- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `wachtwoord`


Je kunt deze Elements ook aanpassen via de `init`/`unlock` API.


### Afgifte van een RGB token


Om een token uit te geven, beginnen we met het maken van "kleurbare" UTXO's:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```


![RGB-Bitcoin](assets/en/107.webp)


Je kunt de bestelling natuurlijk aanpassen. Om de transactie te bevestigen, mijnen we een:


```bash
./regtest.sh mine 1
```


We kunnen nu een RGB asset aanmaken. Het commando hangt af van het type asset dat je wilt maken en de parameters. Hier maak ik een NIA (*Non Inflatable Asset*) token genaamd "PBN" met een Supply van 1000 eenheden. Met `precision` kun je de deelbaarheid van de eenheden bepalen.


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```


![RGB-Bitcoin](assets/en/108.webp)


Het antwoord bevat de ID van het nieuw aangemaakte onderdeel. Vergeet niet om deze identificatie te noteren. In mijn geval is het:


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RGB-Bitcoin](assets/en/109.webp)


Je kunt het dan On-Chain overdragen, of toewijzen in een Lightning-kanaal. Dat is precies wat we in de volgende paragraaf gaan doen.


### Een kanaal openen en een RGB-medium overdragen


Je moet eerst je node verbinden met een peer op de Lightning Network met het `/connectpeer` commando. In mijn voorbeeld bestuur ik beide nodes. Dus ik vraag de publieke sleutel van mijn tweede Lightning-node op met dit commando:


```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```


Het commando geeft de openbare sleutel van mijn knooppunt nr. 2:


```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```


![RGB-Bitcoin](assets/en/110.webp)


Vervolgens openen we het kanaal door de relevante asset (`PBN`) te specificeren. Met het `/openchannel` commando kun je de grootte van het kanaal in satoshis bepalen en ervoor kiezen om de RGB asset toe te voegen. Het hangt af van wat je wilt maken, maar in mijn geval is het commando:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```


Lees hier meer:




- `peer_pubkey_en_opt_addr`: Identificatie van de peer waarmee we willen verbinden (de publieke sleutel die we eerder hebben gevonden);
- capaciteit_sat`: Totale kanaalcapaciteit in satoshis;
- `push_msat`: Hoeveelheid in millisatoshis die in eerste instantie wordt overgemaakt naar de peer wanneer het kanaal wordt geopend (hier maak ik direct 10.000 Sats over zodat hij later een RGB overboeking kan doen);
- `asset_amount`: Bedrag aan RGB activa dat moet worden toegewezen aan het kanaal;
- `asset_id`: Uniek identificatienummer van het RGB apparaat in het kanaal;
- `public`: Geeft aan of het kanaal openbaar moet worden gemaakt voor routering op het netwerk.


![RGB-Bitcoin](assets/en/111.webp)


Om de transactie te bevestigen, worden 6 blokken gedolven:


```bash
./regtest.sh mine 6
```


![RGB-Bitcoin](assets/en/112.webp)


Het Lightning-kanaal is nu open en bevat ook 500 `PBN`-tokens aan de kant van knooppunt n°1. Als knooppunt n°2 `PBN` tokens wil ontvangen, moet het generate en Invoice. Zo doe je dat:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```


Met:




- `amt_msat`: Invoice hoeveelheid in millisatoshis (minimaal 3000 Sats);
- `expiry_sec`: Invoice vervaltijd in seconden;
- `asset_id`: Identificatiesymbool van het RGB bedrijfsmiddel dat geassocieerd is met de Invoice;
- `asset_amount`: Bedrag van het RGB activum dat moet worden overgedragen met deze Invoice.


Als antwoord krijg je een RGB Invoice (zoals beschreven in de vorige hoofdstukken):


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RGB-Bitcoin](assets/en/113.webp)


We betalen deze Invoice nu vanaf het eerste knooppunt, dat het benodigde geld heeft met de `PBN` token:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RGB-Bitcoin](assets/en/114.webp)


De betaling is uitgevoerd. Dit kan worden gecontroleerd door het commando uit te voeren:


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RGB-Bitcoin](assets/en/115.webp)


Hier wordt uitgelegd hoe je een Lightning-knooppunt kunt inzetten dat is aangepast om RGB-middelen te vervoeren. Deze demonstratie is gebaseerd op:




- Een regtest-omgeving (via `./regtest.sh`) of Testnet;
- Een Lightning-node (`RGB-lightning-node`) gebaseerd op een `bitcoind`, een indexer en een `RGB-proxy-server`;
- Een reeks JSON REST API's voor het openen/sluiten van kanalen, het uitgeven van tokens, het overdragen van activa via Lightning, enz.


Dankzij dit proces:




- Lightning engagement transacties bevatten een extra uitgang (OP_RETURN of Taproot) met de verankering van een RGB overgang;
- Overschrijvingen worden op precies dezelfde manier gedaan als traditionele Lightning-betalingen, maar met de toevoeging van een RGB token;
- Meerdere RLN-knooppunten kunnen worden gekoppeld om betalingen over meerdere knooppunten te routeren en ermee te experimenteren, op voorwaarde dat er voldoende liquiditeit is in zowel bitcoins als RGB activa op het pad.


Het project bevindt zich nog in het alfa stadium. Het wordt daarom sterk aangeraden om je te beperken tot testomgevingen (regtest, Testnet).


De mogelijkheden die deze LN-RGB compatibiliteit biedt, zijn aanzienlijk: stablecoins op Lightning, DEX Layer-2, overdracht van fungibele tokens of NFT's tegen zeer lage kosten... De vorige hoofdstukken hebben de conceptuele architectuur en validatielogica geschetst. Nu hebt u een praktische kijk op hoe u zo'n knooppunt aan de praat krijgt, voor uw toekomstige ontwikkelingen of tests.


# Laatste Sectie


<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>


## Beoordelingen


<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>


<isCourseReview>true</isCourseReview>

## Conclusie


<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>


<isCourseConclusion>true</isCourseConclusion>