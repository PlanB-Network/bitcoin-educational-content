---
name: OXT - Ketenanalyse
description: Beheers de basis van ketenanalyse op Bitcoin
---
![cover](assets/cover.webp)


***WAARSCHUWING:** Na de arrestatie van de oprichters van Samourai Wallet en de inbeslagname van hun servers op 24 april, is **de website OXT.me momenteel ontoegankelijk**. Het blijft echter mogelijk dat deze tool in de komende weken opnieuw gelanceerd wordt. In de tussentijd kun je nog steeds je voordeel doen met deze tutorial om de basis van ketenanalyse op Bitcoin te begrijpen. Alle hier gepresenteerde heuristieken en patronen blijven van toepassing op Bitcoin transacties. Hoewel deze tools minder geoptimaliseerd zijn dan OXT, kun je tijdelijk [Mempool.space](https://Mempool.space/) of [Bitcoin Explorer](https://bitcoinexplorer.org/) gebruiken om de theoretische concepten van dit artikel in de praktijk te brengen.*


we volgen de ontwikkelingen van deze zaak en de ontwikkelingen met betrekking tot de bijbehorende tools op de voet. Wees gerust dat we deze handleiding zullen bijwerken zodra er nieuwe informatie beschikbaar is._


deze handleiding is alleen bedoeld voor educatieve en informatieve doeleinden. We keuren het gebruik van deze tools voor criminele doeleinden niet goed en moedigen dit ook niet aan. Het is de verantwoordelijkheid van elke gebruiker om te voldoen aan de wetten in hun rechtsgebied._


---

In dit artikel leer je de essentiële theoretische fundamenten die nodig zijn om te beginnen met basale ketenanalyses op Bitcoin, en nog belangrijker, om te begrijpen hoe degenen die je observeren te werk gaan. Hoewel dit artikel geen praktische tutorial is over de OXT-tool (een onderwerp dat we in een toekomstige tutorial zullen behandelen), verzamelt het een verzameling cruciale kennis voor het gebruik ervan. Voor elk model, elke metriek en elke indicator wordt een link gegeven naar een voorbeeldtransactie op OXT, zodat je het gebruik ervan beter kunt begrijpen en naast het lezen kunt oefenen.


## Inleiding

Een van de functies van geld is het oplossen van het probleem van het dubbel samenvallen van behoeften. In een systeem dat gebaseerd is op ruilhandel, vereist het voltooien van een Exchange niet alleen het vinden van een individu dat een goed aanbiedt dat aan mijn behoefte voldoet, maar ook dat ik hen een goed van gelijke waarde geef dat hun eigen behoefte bevredigt. Het vinden van deze balans blijkt complex. Daarom nemen we onze toevlucht tot geld, waarmee we waarde zowel in de ruimte als in de tijd kunnen verplaatsen.


Wil geld dit probleem oplossen, dan is het essentieel dat de partij die een goed of dienst levert overtuigd is van zijn vermogen om dat bedrag later uit te geven. Elk rationeel individu dat bereid is om een stuk geld te accepteren, of het nu digitaal of fysiek is, zal er dus voor zorgen dat het aan twee fundamentele criteria voldoet:


- De Coin moet intact en authentiek zijn;
- en het mag niet dubbel worden uitgegeven.


Als we fysiek geld gebruiken, is het eerste kenmerk het meest complex om te bevestigen. In verschillende perioden in de geschiedenis werd de integriteit van metalen munten vaak aangetast door praktijken zoals knippen of boren. In het oude Rome was het bijvoorbeeld gebruikelijk dat burgers de randen van gouden munten afschraapten om een beetje edelmetaal te verzamelen, terwijl ze de munten toch bewaarden voor toekomstige transacties. Dit is met name de reden waarom er later groeven werden gestempeld op de rand van munten. Authenticiteit is ook een moeilijk te verifiëren kenmerk van een fysieke monetaire drager. Tegenwoordig worden de technieken om valsemunterij tegen te gaan steeds complexer, waardoor handelaren gedwongen worden om te investeren in dure verificatiesystemen.


Aan de andere kant is dubbele besteding vanwege hun aard geen probleem voor fysieke valuta. Als ik je een biljet van €10 geef, verlaat het onherroepelijk mijn bezit om het jouwe binnen te gaan, waardoor elke mogelijkheid van meervoudige besteding van de monetaire eenheden die het vertegenwoordigt wordt uitgesloten.

Voor digitale valuta is de uitdaging anders. Het waarborgen van de authenticiteit en integriteit van een Coin is vaak eenvoudiger, maar het waarborgen van de afwezigheid van dubbele uitgaven is complexer. Elk digitaal goed is in wezen informatie. In tegenstelling tot fysieke goederen verdeelt informatie zich niet tijdens uitwisselingen, maar verspreidt het zich door vermenigvuldiging. Als ik je bijvoorbeeld een document stuur via e-mail, wordt het gedupliceerd. Aan jouw kant kun je niet met zekerheid controleren of ik het originele document heb verwijderd.


De enige manier om deze duplicatie van een digitaal goed te vermijden, is op de hoogte te zijn van alle uitwisselingen op het systeem. Op die manier kan men weten wie wat bezit en ieders rekeningen bijwerken op basis van de gemaakte transacties. Dit wordt bijvoorbeeld gedaan met giraal geld. Wanneer je met een creditcard €10 aan een winkelier betaalt, noteert de bank deze Exchange en werkt de Ledger bij.


Op Bitcoin wordt het voorkomen van dubbele uitgaven op dezelfde manier gedaan. Er wordt gekeken of er geen transactie heeft plaatsgevonden waarbij de betreffende munten al zijn uitgegeven. Als deze nooit zijn gebruikt, kunnen we er zeker van zijn dat er geen dubbele uitgaven zullen plaatsvinden. Dit is de beroemde zin van Satoshi Nakamoto in het Witboek: "*De enige manier om de afwezigheid van een transactie te bevestigen, is door op de hoogte te zijn van alle transacties.*"


In tegenstelling tot het bankmodel willen we op Bitcoin geen centrale entiteit hoeven vertrouwen. Daarom moeten alle gebruikers deze afwezigheid van dubbele uitgaven kunnen bevestigen, zonder afhankelijk te zijn van een derde partij. Iedereen moet dus op de hoogte zijn van alle Bitcoin transacties.


Het is precies deze publieke verspreiding van informatie die de bescherming van privacy op Bitcoin bemoeilijkt. In het traditionele banksysteem is in theorie alleen de financiële instelling op de hoogte van de gemaakte transacties. Maar op Bitcoin zijn alle gebruikers op de hoogte van alle transacties, via hun respectievelijke nodes.


Door deze beperking op verspreiding verschilt het privacymodel van Bitcoin van dat van het banksysteem. In dat laatste systeem worden transacties geassocieerd met de identiteit van de gebruiker, maar wordt de informatiestroom tussen de vertrouwde derde partij en het publiek afgesneden. Met andere woorden, je bankier weet dat je elke ochtend je stokbrood koopt bij de plaatselijke bakker, maar je buurman is niet op de hoogte van al deze transacties. In het geval van Bitcoin, aangezien de informatiestroom niet verbroken kan worden tussen transacties en het publieke domein, berust het privacymodel op het scheiden van de identiteit van de gebruiker en de transacties zelf.

![analysis](assets/en/1.webp)

*Diagram geïnspireerd op dat van Satoshi Nakamoto in het witboek: Bitcoin: Een Peer-to-Peer Elektronisch Geldsysteem, hoofdstuk 10 "Privacy".*

Aangezien Bitcoin-transacties openbaar worden gemaakt, wordt het mogelijk om verbanden te leggen tussen deze transacties om informatie af te leiden over de betrokken partijen. Deze activiteit vormt zelfs een specialisme op zich, dat gewoonlijk "ketenanalyse" wordt genoemd. In dit artikel nodig ik je uit om de grondbeginselen van ketenanalyse te verkennen om te begrijpen hoe jouw bitcoins worden gevolgd.


De meeste bedrijven die gespecialiseerd zijn in ketenanalyse werken als black boxes en maken hun methodologieën niet bekend. Daarom is het moeilijk om informatie over deze praktijk te verkrijgen. Voor het schrijven van dit artikel heb ik voornamelijk vertrouwd op de weinige open bronnen die beschikbaar zijn:


- Het grootste deel van mijn artikel komt uit de serie van vier artikelen met de naam: [Understanding Bitcoin Privacy with OXT](https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923), geproduceerd door Samourai Wallet in 2021;
- Ik heb ook verschillende rapporten van [OXT Research] (https://medium.com/oxt-research) gebruikt, evenals hun gratis tool voor ketenanalyse;
- Meer in het algemeen komt mijn kennis van de verschillende tweets en inhoud van [@LaurentMT](https://twitter.com/LaurentMT) en [@ErgoBTC](https://twitter.com/ErgoBTC);
- Ik werd ook geïnspireerd door [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) waaraan ik deelnam samen met [@louneskmt](https://twitter.com/louneskmt), [@TheoPantamis](https://twitter.com/TheoPantamis), [@Sosthene___](https://twitter.com/Sosthene___), en [@LaurentMT](https://twitter.com/LaurentMT).


Ik wil hun auteurs, ontwikkelaars en producenten bedanken. Zonder hun verschillende inhoud en software zou dit artikel niet bestaan. Ik bedank ook de recensenten die deze tekst nauwgezet hebben gecorrigeerd en mij verblijdden met hun deskundig advies:


- [Gilles Cadignan](https://twitter.com/gillesCadignan);
- [Ludovic Lars](https://twitter.com/lugaxker) ([https://viresinnumeris.fr/](https://viresinnumeris.fr/)).


*Ter informatie heb ik aan het einde van het artikel een technische woordenlijst toegevoegd om bepaalde termen te definiëren. Als je een woord ziet dat je niet begrijpt met een sterretje, staat de definitie onderaan de pagina.*


## Wat is ketenanalyse?

Ketenanalyse is een praktijk die alle methoden voor het traceren van Bitcoin stromen op de Blockchain omvat. Over het algemeen is ketenanalyse gebaseerd op het observeren van kenmerken in steekproeven van eerdere transacties. Vervolgens worden dezelfde kenmerken geïdentificeerd in een transactie die men wil analyseren en worden plausibele interpretaties afgeleid. Deze probleemoplossingsmethode, gebaseerd op een praktische benadering om een voldoende goede oplossing te vinden, wordt een heuristiek genoemd.


Ter vereenvoudiging wordt de ketenanalyse in twee stappen uitgevoerd:

1. De identificatie van bekende kenmerken;

2. De deductie van hypothesen.


Eén van de doelstellingen van ketenanalyse is het groeperen van verschillende activiteiten op Bitcoin om de uniciteit van de gebruiker die ze uitvoerde te bepalen. Vervolgens kan geprobeerd worden om deze bundel activiteiten te koppelen aan een echte identiteit.


Denk aan mijn inleiding. Ik heb uitgelegd waarom het privacymodel van Bitcoin oorspronkelijk gebaseerd was op het scheiden van de identiteit van de gebruiker en zijn transacties. Het zou daarom verleidelijk zijn om te denken dat ketenanalyse overbodig is, omdat zelfs als men erin slaagt om On-Chain activiteiten te groeperen, ze niet geassocieerd kunnen worden met een echte identiteit. Theoretisch klopt deze bewering. Cryptografische sleutelparen worden gebruikt om voorwaarden te stellen aan de UTXO's. In essentie geven deze sleutelparen geen informatie vrij over de identiteit van hun houders. Dus zelfs als het lukt om activiteiten te groeperen die geassocieerd zijn met verschillende sleutelparen, zegt dit niets over de entiteit achter deze activiteiten.


De praktische realiteit is echter veel complexer. Er is een veelheid aan gedragingen die een echte identiteit kunnen koppelen aan een On-Chain activiteit. In de analyse wordt dit een ingangspunt genoemd, en er zijn er veel. De meest voorkomende is natuurlijk KYC (Know Your Customer). Als je bitcoins opneemt van een gereguleerd platform naar een van je persoonlijke ontvangstadressen, dan kunnen sommige mensen jouw identiteit linken aan deze Address. In bredere zin kan een ingangspunt elke vorm van interactie zijn tussen jouw echte leven en een Bitcoin transactie. Als je bijvoorbeeld een ontvangende Address publiceert op je sociale netwerken, kan dit een ingang zijn voor analyse. Als je een betaling in bitcoins doet aan je bakker, kunnen ze je gezicht (dat deel uitmaakt van je identiteit) associëren met een Bitcoin Address.

Deze ingangspunten zijn bijna onvermijdelijk bij het gebruik van Bitcoin. Hoewel je kunt proberen hun bereik te beperken, zullen ze aanwezig blijven. Daarom is het cruciaal om methodes te combineren die gericht zijn op het beschermen van je privacy. Hoewel het onderhouden van een acceptabele scheiding tussen je echte identiteit en je transacties een prijzenswaardige aanpak is, blijft het onvoldoende. Immers, als al je On-Chain activiteiten kunnen worden gegroepeerd, dan kan zelfs het kleinste toegangspunt de enige Layer van privacy die je had ingesteld in gevaar brengen.


Daarom is het ook nodig om ons bezig te houden met ketenanalyse in ons gebruik van Bitcoin. Door dit te doen, kunnen we de samenvoeging van onze activiteiten minimaliseren en de impact van een toegangspunt op onze privacy beperken. Precies, om ketenanalyse beter tegen te gaan, is er geen betere aanpak dan jezelf vertrouwd te maken met de methodes die gebruikt worden bij ketenanalyse? Als je wilt weten hoe je je privacy op Bitcoin kunt verbeteren, moet je deze methoden begrijpen. Zo kun je technieken als [CoinJoin](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef) of [PayJoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f) beter begrijpen en de fouten die je zou kunnen maken, beperken.


Hierin kunnen we een analogie trekken met cryptografie en cryptoanalyse. Een goede cryptograaf is eerst en vooral een goede cryptanalist. Om een nieuw versleutelingsalgoritme te bedenken, moet men weten welke aanvallen het zal ondervinden en ook bestuderen waarom vorige algoritmen gebroken werden. Hetzelfde principe geldt voor privacy op Bitcoin. Het begrijpen van de methodes van ketenanalyse is de sleutel tot bescherming ertegen. Daarom bied ik je dit artikel aan.


Het is cruciaal om te begrijpen dat ketenanalyse geen exacte wetenschap is. Het is gebaseerd op heuristieken die zijn afgeleid van eerdere waarnemingen of logische interpretaties. Deze regels maken redelijk betrouwbare resultaten mogelijk, maar nooit met absolute precisie. Met andere woorden, ketenanalyse omvat altijd een dimensie van waarschijnlijkheid in de getrokken conclusies. We kunnen met meer of minder zekerheid schatten dat twee adressen tot dezelfde entiteit behoren, maar volledige zekerheid zal altijd buiten bereik blijven.


Het hele doel van ketenanalyse ligt precies in het samenvoegen van verschillende heuristieken om het risico op fouten te minimaliseren. Het is in zekere zin een opeenstapeling van bewijzen die ons dichter bij de werkelijkheid brengt.


Deze beroemde heuristieken kunnen worden gegroepeerd in verschillende categorieën die we samen in detail zullen bespreken:


- Transactiepatronen (of transactiemodellen);
- Interne heuristieken voor de transactie;
- Externe heuristieken voor de transactie.


Het is vermeldenswaard dat de eerste twee heuristieken op Bitcoin werden geformuleerd door Satoshi Nakamoto zelf. Hij bespreekt ze in deel 10 van het witboek. Zoals we later zullen zien, is het interessant om te zien dat deze twee heuristieken vandaag de dag nog steeds de overhand hebben in ketenanalyse. Deze zijn:


- de Common Input Ownership Heuristic (CIOH);
- en hergebruik van Address.


Laten we samen de waarneembare kenmerken verkennen en de interpretaties die kunnen worden getrokken om een analyse uit te voeren.


## Transactiepatronen (of transactiemodellen)

Een transactiepatroon is simpelweg een typisch transactiemodel dat gevonden kan worden op de Blockchain, waarvan de interpretatie waarschijnlijk bekend is. Bij het bestuderen van patronen richten we ons op een enkele transactie die we op een hoog niveau analyseren. Met andere woorden, we kijken alleen naar het aantal in- en uitgangen, zonder in te gaan op de meer specifieke details of de omgeving. Aan de hand van het geobserveerde model kunnen we de aard van de transactie interpreteren. Vervolgens gaan we op zoek naar kenmerken van de structuur en leiden daaruit een interpretatie af.


### De eenvoudige verzending (of eenvoudige betaling)

Dit model wordt gekenmerkt door het verbruik van een of meer UTXO's als input en de productie van twee UTXO's als output.


![analysis](assets/en/2.webp)


De interpretatie van dit model is dat we in de aanwezigheid zijn van een verzend- of betalingstransactie. De gebruiker heeft zijn eigen UTXO's verbruikt als input om in output te voldoen aan een betaling UTXO en een verandering UTXO (verandering die terugkomt naar dezelfde gebruiker). We weten daarom dat de waargenomen gebruiker waarschijnlijk niet langer in het bezit is van één van de twee UTXO's in output (de betaling), maar nog wel in het bezit is van de andere UTXO (de verandering).


Op dit moment is het onmogelijk voor ons om te specificeren welke output welke UTXO vertegenwoordigt, omdat dat niet het doel is van dit model. We kunnen dit doen door te vertrouwen op de heuristieken die we in het volgende deel zullen bestuderen. In dit stadium is ons doel beperkt tot het identificeren van de aard van de transactie in kwestie, in dit geval een eenvoudige verzending.


Hier is bijvoorbeeld een Bitcoin transactie die het eenvoudige verzendpatroon gebruikt:

### Sweep ("sweep" in het Engels)

Dit model wordt gekenmerkt door het verbruik van een enkele UTXO als input en de productie van een enkele UTXO als output.


![analysis](assets/en/3.webp)


De interpretatie van dit model is dat we te maken hebben met een zelfoverdracht. De gebruiker heeft zijn bitcoins aan zichzelf overgedragen, naar een andere Address die hij bezit. Aangezien er geen verandering is in de transactie, is het zeer onwaarschijnlijk dat we te maken hebben met een betaling. We weten dan dat de waargenomen gebruiker waarschijnlijk nog steeds in het bezit is van deze UTXO.


Hier is bijvoorbeeld een Bitcoin transactie die het veegpatroon gebruikt:

[35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d](https://Mempool.space/tx/35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d)


Dit type patroon kan echter ook een zelfoverboeking naar een Exchange rekening (cryptocurrency Exchange platform) onthullen. Het zal de studie van bekende adressen en de context van de transactie zijn die ons in staat zal stellen om te weten of het een sweep is naar een zelfbewaard Wallet of een opname naar een platform.


### Consolidatie

Dit model wordt gekenmerkt door het verbruik van meerdere UTXO's als invoer en de productie van een enkele UTXO als uitvoer.


![analysis](assets/en/4.webp)


De interpretatie van dit model is dat we te maken hebben met een consolidatie. Dit is een veelvoorkomende praktijk onder Bitcoin gebruikers, die erop gericht is om verschillende UTXO's samen te voegen in afwachting van een mogelijke verhoging van de transactiekosten. Door deze operatie uit te voeren in een periode waarin de vergoedingen laag zijn, is het mogelijk om te besparen op toekomstige vergoedingen.


We kunnen hieruit afleiden dat de gebruiker achter deze transactie waarschijnlijk in het bezit was van alle UTXO's in de invoer en nog steeds in het bezit is van de UTXO in de uitvoer. Daarom is het zeker een zelf-overdracht.


Net als de sweep kan dit type patroon ook een zelfoverboeking naar een Exchange rekening onthullen. Het is de studie van bekende adressen en de context van de transactie die ons in staat zal stellen om te weten of het een consolidatie is naar een zelfbewaarde Wallet of een opname naar een platform.


Hier is bijvoorbeeld een Bitcoin-transactie die het consolidatiepatroon volgt:

[77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94](https://Mempool.space/tx/77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94)

### Het batch-uitgavenmodel

Dit model wordt gekenmerkt door het verbruik van een paar UTXO's als input (vaak maar één) en de productie van veel UTXO's als output.


![analysis](assets/en/5.webp)


De interpretatie van dit model is dat we in de aanwezigheid zijn van een batch-uitgave. Dit is een praktijk die waarschijnlijk een significante economische activiteit onthult, zoals een Exchange bijvoorbeeld. Met batchuitgaven kunnen deze entiteiten besparen op kosten door hun uitgaven in één transactie te combineren.


We kunnen afleiden dat de UTXO input afkomstig is van een bedrijf met significante economische activiteit en dat de output van UTXO's verspreid zal zijn. Sommige zullen toebehoren aan de klanten van het bedrijf. Andere kunnen naar partnerbedrijven gaan. Ten slotte zal er zeker een verandering zijn die terugkeert naar het uitgevende bedrijf.


Hier is bijvoorbeeld een Bitcoin transactie die het batchuitgavenpatroon volgt:

[8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43](https://Mempool.space/tx/8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43)


### Protocol-specifieke transacties

Onder de transactiepatronen kunnen we ook modellen identificeren die het gebruik van een specifiek protocol onthullen. Bijvoorbeeld, Whirlpool coinjoins hebben een gemakkelijk herkenbare structuur waarmee ze onderscheiden kunnen worden van andere klassieke transacties.


![analysis](assets/en/6.webp)


De analyse van dit patroon suggereert dat we ons waarschijnlijk in de aanwezigheid van een collaboratieve transactie bevinden. Het is ook mogelijk om een CoinJoin te observeren. Als deze laatste hypothese juist blijkt te zijn, dan kan het aantal uitgangen ons een schatting geven van het aantal deelnemers.


Hier is bijvoorbeeld een Bitcoin transactie die het patroon van het collaboratieve transactietype CoinJoin overneemt:

[00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea](https://Mempool.space/tx/00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea)


Er zijn veel andere protocollen die hun eigen specifieke structuren hebben. Zo kunnen we bijvoorbeeld transacties van het type Wabisabi of Stamps onderscheiden.


## Interne transactie heuristieken

Een interne heuristiek is een specifiek kenmerk dat binnen een transactie zelf wordt geïdentificeerd, zonder dat de omgeving hoeft te worden onderzocht, waardoor we conclusies kunnen trekken. In tegenstelling tot patronen die zich richten op de algemene structuur van de transactie, zijn interne heuristieken gebaseerd op de set van extraheerbare gegevens. Dit omvat:


- De hoeveelheden van verschillende UTXO's, zowel inkomend als uitgaand;
- Alles met betrekking tot scripts: ontvangstadressen, versiebeheer, locktijden...


Over het algemeen stelt dit type heuristiek ons in staat om de verandering in een specifieke transactie te identificeren. Door dit te doen, kunnen we vervolgens doorgaan met het traceren van een entiteit in meerdere verschillende transacties.


Ik herinner je er nogmaals aan dat deze heuristieken niet absoluut nauwkeurig zijn. Afzonderlijk stellen ze ons alleen in staat om plausibele scenario's te identificeren. Het is de opeenstapeling van verschillende heuristieken die bijdraagt aan het verminderen van onzekerheid, zonder deze ooit volledig weg te nemen.


### Interne overeenkomsten

Deze heuristiek bestaat uit het bestuderen van de overeenkomsten tussen de inputs en outputs van dezelfde transactie. Als dezelfde eigenschap wordt waargenomen op de inputs en op slechts één van de outputs van de transactie, dan is het waarschijnlijk dat deze output de verandering vormt.


Het meest voor de hand liggende kenmerk is het hergebruik van een ontvangende Address in dezelfde transactie.


![analysis](assets/en/7.webp)


Deze heuristiek laat weinig ruimte voor twijfel. Tenzij hun private sleutel gecompromitteerd is, onthult dezelfde ontvangende Address onvermijdelijk de activiteit van een enkele gebruiker. De interpretatie die volgt is dat de verandering van de transactie de uitvoer is met dezelfde Address als de invoer. Dit stelt ons in staat om het individu te blijven traceren vanaf deze verandering.


Hier is bijvoorbeeld een transactie waarbij deze heuristiek waarschijnlijk kan worden toegepast:

[54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0](https://Mempool.space/tx/54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0)


Deze overeenkomsten tussen de inputs en outputs stoppen niet bij het hergebruik van Address. Elke overeenkomst in het gebruik van scripts kan de toepassing van een heuristiek mogelijk maken. Soms kan bijvoorbeeld dezelfde versionering tussen een input en een van de outputs van de transactie worden waargenomen.


![analysis](assets/en/8.webp)

In dit diagram kunnen we zien dat ingang nummer 0 een P2WPKH script opent (SegWit V0 beginnend met "bc1q"). Uitgang nummer 0 gebruikt hetzelfde type script. Uitvoer nummer 1 gebruikt echter een P2TR script (SegWit V1 beginnend met "bc1p"). De interpretatie van dit kenmerk is dat het waarschijnlijk is dat het Address met dezelfde versie als de invoer, het wisselgeld Address is. Het zou daarom nog steeds toebehoren aan dezelfde gebruiker.

Hier is een transactie waarbij deze heuristiek waarschijnlijk kan worden toegepast:

[db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578](https://Mempool.space/tx/db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578)


In deze transactie kunnen we zien dat ingang nummer 0 en uitgang nummer 1 P2WPKH scripts gebruiken (SegWit V0), terwijl uitgang nummer 0 een ander scripttype gebruikt, P2PKH (Legacy).


### Betalingen met ronde getallen

Een andere interne heuristiek die ons kan helpen de verandering te identificeren is die van het ronde getal. In het algemeen geldt dat als een eenvoudig betalingspatroon (1 invoer en 2 uitgangen) een rond bedrag uitgeeft aan een van de uitgangen, dit de betaling vertegenwoordigt.


![analysis](assets/en/9.webp)


Bij wijze van eliminatie, als de ene uitgang de betaling vertegenwoordigt, vertegenwoordigt de andere de wijziging. Daarom kunnen we interpreteren dat het waarschijnlijk is dat de gebruiker bij invoer nog steeds de uitvoer bezit die is geïdentificeerd als de wijziging.


Opgemerkt moet worden dat deze heuristiek niet altijd van toepassing is, omdat de meeste betalingen nog steeds in fiatvaluta worden gedaan. Sterker nog, wanneer een winkelier in Frankrijk Bitcoin accepteert, geven ze over het algemeen geen stabiele prijzen in Sats weer. Ze kiezen liever voor een omrekening tussen de prijs in euro's en het te betalen bedrag in bitcoins. Daarom zou er geen rond getal in de transactieoutput moeten staan. Toch zou een analist kunnen proberen om deze conversie uit te voeren, rekening houdend met de Exchange koers die van kracht was toen de transactie werd uitgezonden op het netwerk.


Als Bitcoin op een dag de favoriete rekeneenheid wordt in onze uitwisselingen, kan deze heuristiek nog nuttiger worden voor analyse.


Hier is bijvoorbeeld een transactie waarbij deze heuristiek waarschijnlijk kan worden toegepast:

### De grote uitgaven


Als er een voldoende groot verschil wordt waargenomen tussen twee transactieoutputs in een eenvoudig betalingsmodel, kan worden geschat dat de grotere output waarschijnlijk de verandering is.


![analysis](assets/en/10.webp)


Deze heuristiek van de grootste uitvoer is waarschijnlijk de meest onnauwkeurige van allemaal. Als hij alleen wordt geïdentificeerd, is hij vrij zwak. Dit kenmerk kan echter worden gecombineerd met andere heuristieken om de onzekerheid van onze interpretatie te verminderen.


Als we bijvoorbeeld een transactie onderzoeken met een output met een rond bedrag en een andere output met een groter bedrag, stelt de gezamenlijke toepassing van de ronde betalingen heuristiek en die met betrekking tot de grootste output ons in staat om onze mate van onzekerheid te verminderen.


Hier is bijvoorbeeld een transactie waarbij deze heuristiek waarschijnlijk kan worden toegepast:

[b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf](https://Mempool.space/tx/b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf)


## Externe heuristieken voor de transactie

De studie van externe heuristieken is de analyse van overeenkomsten, patronen en kenmerken van bepaalde Elements die niet inherent zijn aan de transactie zelf. Met andere woorden, waar we ons voorheen beperkten tot het benutten van Elements die intrinsiek zijn aan de transactie met interne heuristieken, breiden we nu ons analysegebied uit naar de omgeving van de transactie dankzij externe heuristieken.


### Address hergebruik

Dit is een van de bekendste heuristieken onder Bitcoiners. Hergebruik van Address maakt het mogelijk een verband te leggen tussen verschillende transacties en verschillende UTXO's. Het wordt waargenomen wanneer een Bitcoin ontvangende Address meerdere keren wordt gebruikt.


De interpretatie van hergebruik van Address is dat alle UTXO's die op deze Address zijn vergrendeld tot dezelfde entiteit behoren (of hebben behoord). Deze heuristiek laat weinig ruimte voor onzekerheid. Als het geïdentificeerd wordt, heeft de interpretatie die volgt een grote kans om overeen te komen met de werkelijkheid.

Zoals uitgelegd in de inleiding, werd deze heuristiek ontdekt door Satoshi Nakamoto zelf. In het witboek noemt hij specifiek een oplossing om te voorkomen dat gebruikers deze heuristiek produceren, namelijk door simpelweg een nieuwe Address te gebruiken voor elke nieuwe transactie: "*Als extra firewall zou voor elke transactie een nieuw sleutelpaar gebruikt kunnen worden om ze niet te koppelen aan een gemeenschappelijke eigenaar.*"


Hier is bijvoorbeeld een Address hergebruikt in meerdere transacties:

[bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0](https://Mempool.space/Address/bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0)


### De gelijkenis van scripts en Wallet vingerafdrukken

Naast hergebruik van Address zijn er veel andere heuristieken die acties kunnen linken aan dezelfde Wallet of aan een cluster van adressen.


Ten eerste kan een analist overeenkomsten in scriptgebruik gebruiken. Bepaalde minderheidsscripts zoals Multisig kunnen bijvoorbeeld gemakkelijker worden gespot dan SegWit V0-scripts. Hoe groter de groep waarin we ons verbergen, hoe moeilijker het is om ons te herkennen. Dit is met name de reden waarom in het CoinJoin Whirlpool protocol alle deelnemers precies hetzelfde type script gebruiken.


Meer in het algemeen kan een analist zich ook richten op de karakteristieke vingerafdrukken van een Wallet. Dit zijn specifieke processen van een gebruik die men zou kunnen proberen te identificeren om ze te gebruiken als opsporingstheuristiek. Met andere woorden, als men een opeenstapeling van dezelfde interne kenmerken ziet bij transacties die worden toegeschreven aan de getraceerde entiteit, kan men proberen deze zelfde kenmerken te identificeren bij andere transacties.


Er kan bijvoorbeeld worden vastgesteld dat de getraceerde gebruiker zijn wijzigingen systematisch naar P2TR* adressen stuurt (bc1p...). Als dit proces zich herhaalt, kan het worden gebruikt als een heuristiek voor het vervolg van onze analyse. Andere vingerafdrukken kunnen ook gebruikt worden, zoals de volgorde van de UTXO's, de plaatsing van de wijziging in de uitgangen, de signalering van RBF (Replace-by-fee), of zelfs het versienummer en de locktijd.

Zoals @LaurentMT](https://twitter.com/LaurentMT) aangeeft in [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) (een Franstalige podcast), neemt het nut van Wallet fingerprints in ketenanalyse in de loop der tijd aanzienlijk toe. Het groeiende aantal scripttypes en de steeds geleidelijkere toepassing van deze nieuwe functies door Wallet software accentueren de verschillen. Het komt zelfs voor dat de software die door de getraceerde entiteit wordt gebruikt, nauwkeurig kan worden geïdentificeerd. Daarom is het belangrijk om te begrijpen dat het bestuderen van de vingerafdruk van een Wallet bijzonder relevant is voor recente transacties, meer dan voor transacties die begin 2010 zijn gestart.

Samengevat kan een vingerafdruk elke specifieke handeling zijn, automatisch uitgevoerd door de Wallet of handmatig door de gebruiker, die gevonden kan worden op andere transacties om te helpen bij onze analyse.


### De CIOH

De CIOH, voor "Common Input Ownership Heuristic," wat vertaald zou kunnen worden als "heuristiek van gemeenschappelijke Ownership van inputs" of "co-spending heuristic," is een heuristiek die stelt dat wanneer een transactie meerdere inputs heeft, deze waarschijnlijk allemaal van één entiteit afkomstig zijn. Daarom is hun Ownership gemeenschappelijk.


Om het CIOH toe te passen, observeert men eerst een transactie die meerdere inputs heeft. Dit kunnen twee ingangen zijn, maar ook dertig ingangen. Zodra dit kenmerk is opgemerkt, controleert men of de transactie niet in een bekend patroon past. Als het bijvoorbeeld 5 ingangen heeft met ongeveer hetzelfde bedrag en 5 uitgangen met precies hetzelfde bedrag, weten we dat het de structuur van een CoinJoin Whirlpool is. Daarom kan de CIOH niet worden toegepast.


Als de transactie echter niet past in een bekend patroon van samenwerkende transacties, dan kan worden geïnterpreteerd dat alle invoer waarschijnlijk van dezelfde entiteit afkomstig is. Dit kan erg nuttig zijn om een reeds bekend cluster uit te breiden of om verder te gaan met traceren.


![analysis](assets/en/11.webp)


De CIOH werd ontdekt door Satoshi Nakamoto. Hij bespreekt het in deel 10 van het White Paper: "*[...] de koppeling is onvermijdelijk bij transacties met meerdere ingangen, die noodzakelijkerwijs onthullen dat hun ingangen eigendom waren van dezelfde eigenaar. Het risico is dat als de eigenaar van een sleutel wordt onthuld, de koppelingen andere transacties kunnen onthullen die van dezelfde eigenaar waren.*"

Het is bijzonder fascinerend om te zien dat Satoshi Nakamoto, zelfs voor de officiële lancering van Bitcoin, al de twee belangrijkste privacykwetsbaarheden voor gebruikers had geïdentificeerd, namelijk de CIOH en Address hergebruik. Zo'n vooruitziende blik is heel opmerkelijk, omdat deze twee heuristieken zelfs vandaag de dag nog het nuttigst zijn bij ketenanalyse.


### off-chain gegevens

Uiteraard is ketenanalyse niet beperkt tot On-Chain gegevens. Alle gegevens van een eerdere analyse of toegankelijk op het internet kunnen ook worden gebruikt om een analyse te verfijnen.


Als bijvoorbeeld wordt waargenomen dat de getraceerde transacties systematisch worden uitgezonden vanaf hetzelfde Bitcoin knooppunt en het IP Address kan worden geïdentificeerd, is het misschien mogelijk om andere transacties van dezelfde entiteit te vinden.


De analist heeft ook de optie om te vertrouwen op analyses die eerder open source zijn gemaakt, of op hun eigen eerdere analyses. Misschien vindt men een uitvoer die wijst naar een cluster van adressen die al geïdentificeerd waren. Soms is het ook mogelijk om te vertrouwen op uitvoer die wijst naar een Exchange, omdat de adressen van deze platformen algemeen bekend zijn.


Op dezelfde manier kan een analyse worden uitgevoerd door eliminatie. Als bijvoorbeeld tijdens de analyse van een transactie met twee uitgangen, een van hen is gekoppeld aan een bekende maar verschillende cluster van adressen van de entiteit die wordt getraceerd, dan kan worden geïnterpreteerd dat de andere uitgang waarschijnlijk de wijziging vertegenwoordigt.


Ketenanalyse omvat ook een deel van OSINT (Open Source Intelligence) dat wat algemener is met zoeken op internet. Daarom wordt afgeraden om ontvangende adressen rechtstreeks op sociale media of op een website te plaatsen, al dan niet onder een pseudoniem.


### Temporele modellen

Je zou er misschien niet meteen aan denken, maar bepaalde menselijke gedragingen zijn herkenbaar On-Chain. Het meest bruikbare in een onderzoek is je slaappatroon! Ja, als je slaapt, zend je waarschijnlijk geen Bitcoin transacties uit. Omdat je over het algemeen op ongeveer dezelfde uren slaapt, is het gebruikelijk om temporele analyses te gebruiken bij On-Chain analyse. Hierbij worden simpelweg de tijden geregistreerd waarop de transacties van een bepaalde entiteit naar het Bitcoin netwerk worden uitgezonden. Door deze temporele patronen te analyseren, kunnen we veel informatie afleiden.

Eerst en vooral kan een temporele analyse soms de aard van de getraceerde entiteit identificeren. Als men ziet dat transacties consistent over 24 uur worden uitgezonden, kan dit duiden op een sterke economische activiteit. De entiteit achter deze transacties is waarschijnlijk een bedrijf, mogelijk internationaal en misschien met intern geautomatiseerde procedures.


Ik had dit patroon bijvoorbeeld een paar weken geleden herkend toen ik een transactie analyseerde die per ongeluk 19 bitcoins aan kosten had toegewezen. Een eenvoudige temporele analyse stelde me in staat om te veronderstellen dat we te maken hadden met een geautomatiseerde service, en dus waarschijnlijk met een grote entiteit zoals een Exchange: https://twitter.com/Loic_Pandul/status/1701127409712452072


Een paar dagen later werd inderdaad ontdekt dat het geld toebehoorde aan PayPal, via de Paxos Exchange.


Omgekeerd, als je ziet dat het temporele patroon nogal verspreid is over 16 specifieke uren, dan kun je schatten dat we te maken hebben met een individuele gebruiker, of misschien een lokaal bedrijf, afhankelijk van de uitgewisselde volumes.


Naast de aard van de waargenomen entiteit, kan het temporele patroon ons ook een geschatte locatie van de gebruiker geven. We kunnen dus andere transacties correleren en de Timestamp hiervan gebruiken als een extra heuristiek die kan worden toegevoegd aan onze analyse.


Op de Address die ik eerder noemde en die meerdere keren hergebruikt is, kun je bijvoorbeeld zien dat de transacties, zowel inkomend als uitgaand, geconcentreerd zijn in een interval van 13 uur.

![analysis](assets/notext/12.webp)

*Krediet: OXT*


Dit interval komt waarschijnlijk overeen met Europa, Afrika of het Midden-Oosten. Daarom kan worden geïnterpreteerd dat de gebruiker achter deze transacties daar woont.


In een ander register is het ook een temporele analyse van dit type die de hypothese mogelijk maakte dat Satoshi Nakamoto niet opereerde vanuit Japan, maar wel vanuit de Verenigde Staten: [https://medium.com/@insearchofsatoshi/the-time-zones-of-Satoshi-nakamoto-aa40f035178f](https://medium.com/@insearchofsatoshi/the-time-zones-of-Satoshi-nakamoto-aa40f035178f)


### De analyse van volumes

Een andere externe heuristiek die gebruikt kan worden is de analyse van handelsvolumes. Op basis van de bedragen in elke transactie die aan een entiteit wordt toegeschreven, kan deze informatie worden gebruikt als een aanvullende heuristiek voor de rest van de analyse.

Deze heuristiek is duidelijk erg zwak, maar kan helpen om onzekerheid te verminderen als hij wordt toegevoegd aan andere heuristieken.


## Hoe bescherm je jezelf tegen ketenanalyse?

Als Bitcoin gebruiker heb je het recht om je privacy te beschermen. Dit komt voort uit je natuurlijke rechten om jezelf te bezitten en over jezelf te beschikken, die inherent zijn aan elk individu, ongeacht enige wettelijke beperking.


Dit natuurlijke recht op bescherming van de persoonlijke levenssfeer is ook omgezet in een claimrecht, vastgelegd in artikel 12 van de Universele Verklaring van de Rechten van de Mens, waarin staat: "*Niemand zal onderworpen worden aan willekeurige inmenging in zijn persoonlijke aangelegenheden, in zijn gezin, zijn tehuis of zijn briefwisseling, noch aan aanslagen op zijn eer en goede naam. Een ieder heeft recht op bescherming door de wet tegen dergelijke inmenging of aantasting.*".


De kernactiviteit van bedrijven die gespecialiseerd zijn in ketenanalyse bestaat er echter juist in om je privésfeer binnen te dringen en zo de privacy van je correspondentie te schenden. Terwijl je zou hopen dat, in overeenstemming met het bovengenoemde claimrecht, staten onze privacy krachtig zouden verdedigen, verzuimen ze niet alleen dit te doen, maar financieren ze ook substantieel de financiering van deze analysebedrijven. Het zou ook tevergeefs zijn om te hopen op steun van brancheorganisaties, die bereid lijken alle concessies te doen tegenover de wetgever.


De facto bestaat dit recht op privacy op Bitcoin niet. Het is daarom aan u, de gebruiker, om uw natuurlijke recht te doen gelden en de privacy van uw correspondentie te beschermen. Dit houdt in dat u verschillende technieken en gebruikspraktijken toepast, waarmee u de heuristiek die wordt gebruikt voor ketenanalyse kunt voorkomen of omzeilen.


### Vermijden te vervallen in heuristieken

Allereerst is het raadzaam om, voordat we radicalere methoden overwegen, de heuristieken die gebruikt worden voor ketenanalyse zoveel mogelijk te beperken. Zoals eerder vermeld, zijn de twee krachtigste heuristieken Address hergebruik en CoinJoin.


Het basisprincipe voor het waarborgen van je privacy op Bitcoin ligt in het gebruik van een nieuwe, schone Address voor elke inkomende transactie naar je Wallet. Hergebruik van Address is echt de grootste bedreiging voor de privacy op Bitcoin.

Voor een individuele gebruiker is het genereren van een nieuwe Address voor elke inkomende betaling heel eenvoudig. Moderne wallets doen dit automatisch zodra je op "Ontvangen" klikt. Dus, als je ook maar het minste belang hecht aan de privacy van je transacties, is het gebruik van nieuwe adressen het absolute minimum. Als je ooit een statisch contactpunt op het internet nodig hebt, kun je in plaats van een ontvangende Address, oplossingen gebruiken [zoals PayNym die BIP47 implementeren](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093).

Vervolgens, als je wilt optreden tegen ketenanalyse, vermijd dan het samenvoegen van UTXO's bij de invoer van een transactie. Als je echt moet samenvoegen, geef dan op zijn minst de voorkeur aan UTXOs die dezelfde bron hebben. Deze aanbeveling impliceert een goed beheer van je UTXO's. Als je bitcoins koopt, geef dan de voorkeur aan transfers met grote bedragen om het aantal betalingen dat je kunt doen zonder samen te voegen te maximaliseren. Ik adviseer je ook om je UTXO's te labelen in je software om hun oorsprong te identificeren en samenvoegen van verschillende bronnen te voorkomen.


Meer in het algemeen geldt voor alle andere heuristieken dat je ze moet kennen om te proberen er niet in te vervallen:


- Gebruik geen minderheidsscripts. Geef de voorkeur aan SegWit V0 of mogelijk SegWit V1;
- Doe betalingen niet in ronde getallen. Als je bijvoorbeeld 100k Sats naar een vriend moet sturen, stuur hem dan 114.486 Sats. In ruil kopen ze een drankje voor je;
- Probeer niet altijd een verandering te hebben die veel groter is dan de betalingsuitvoer;
- Post je ontvangstadressen niet op sociale media;
- Gebruik je eigen node onder Tor om je transacties uit te zenden;
- Probeer je Bitcoin transacties niet altijd tegelijkertijd uit te zenden..


### Privacytools gebruiken

Je kunt ook methoden gebruiken die je gebruik van Bitcoin dubbelzinnig maken om ketenanalyse te voorkomen of te misleiden.


De populairste techniek is zeker CoinJoin, een collaboratieve transactiestructuur die meerdere UTXO's van dezelfde bedragen mobiliseert. Het doel is hier om deterministische links te verbreken en zo analyses van het heden naar het verleden en van het verleden naar het heden te voorkomen. CoinJoin maakt plausibele ontkenning mogelijk door je munten te verbergen in een grote groep niet van echt te onderscheiden munten. Als je meer wilt leren over CoinJoin, zowel technisch als praktisch, raad ik je aan deze andere artikelen en tutorials te lezen:


- [CoinJoin - SAMOURAI Wallet](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef);
- [CoinJoin - Sparrow wallet](https://planb.network/tutorials/privacy/on-chain/coinjoin-sparrow-wallet-84def86d-faf5-4589-807a-83be60720c8b);
- [Whirlpool STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375).

![analysis](assets/en/13.webp)


CoinJoin is een uitstekend hulpmiddel voor het creëren van plausibele ontkenning voor munten, maar het is niet geoptimaliseerd voor alle privacybehoeften van gebruikers. CoinJoin is niet ontworpen als betaalmiddel. Het is erg rigide over de bedragen die uitgewisseld worden om de productie van plausibele ontkenning te perfectioneren. Omdat men niet vrij is in de keuze van het transactiebedrag, kan CoinJoin niet gebruikt worden om betalingen in bitcoins te doen.


Stel je bijvoorbeeld voor dat ik mijn stokbrood in bitcoins wil betalen terwijl ik mijn privacy optimaliseer. Gezien de onmogelijkheid om het bedrag van de resulterende UTXO te selecteren uit de CoinJoin, zou ik niet in staat zijn om het bedrag van mijn uitgave aan te passen aan de prijs die de bakker heeft vastgesteld. Daarom is CoinJoin niet geschikt voor betalingstransacties.


Andere hulpmiddelen zijn ontwikkeld om te voldoen aan privacybehoeften in meer specifieke gebruikssituaties. We hebben bijvoorbeeld [PayJoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f), een soort mini-CoinJoin, met slechts twee deelnemers en gebaseerd op een structuur die betaling mogelijk maakt.


Het unieke van PayJoin ligt in de mogelijkheid om een transactie te produceren die er gewoon uitziet, terwijl het eigenlijk een mini-CoinJoin tussen twee gebruikers is. In deze structuur neemt de ontvanger van de transactie deel aan de inputs naast de eigenlijke verzender. De ontvanger voegt dus een betaling aan zichzelf toe aan de transactie die de eigenlijke betaling vergemakkelijkt.


Als je bijvoorbeeld een stokbrood koopt bij je bakker voor 6.000 Sats uit een UTXO van 10.000 Sats, en je wilt een PayJoin doen, dan zal je bakker een UTXO van 15.000 Sats die van hen is toevoegen als invoer aan je oorspronkelijke transactie, die ze volledig zullen terugwinnen als uitvoer, om de heuristiek te misleiden:


![analysis](assets/en/14.webp)


Transactiekosten worden verwaarloosd om het begrip van de regeling te vereenvoudigen.


Het doel van PayJoin is tweeledig. Ten eerste is het bedoeld om een externe waarnemer te misleiden door een lokvogel te creëren via de COH. Immers, wanneer een analist deze transactie observeert, zal hij denken dat hij de COH kan toepassen, en dus een gemeenschappelijke Ownership van de verschillende ingangen veronderstellen. In werkelijkheid is deze aanname onjuist, omdat de ene ingang toebehoort aan de verzender, terwijl de andere eigendom is van de ontvanger. Daarom corrumpeert PayJoin de ketenanalyse door de analist op het verkeerde pad te leiden.

Het tweede doel van PayJoin is om de analist te misleiden over het werkelijke bedrag van de transactie, dankzij de specifieke structuur van de uitvoer. PayJoin valt dus onder steganografie. Het maakt het mogelijk om het werkelijke bedrag van de transactie te verbergen in een bedrieglijke transactie.


Als we ons voorbeeld van het gebruik van PayJoin om een stokbrood te kopen nog eens bekijken, zou een externe waarnemer kunnen denken dat we te maken hebben met een betaling van 4.000 Sats of 21.000 Sats. In werkelijkheid is de betaling voor het stokbrood 6.000 Sats: 21.000 - 15.000 = 6.000. In werkelijkheid is de betaling voor het stokbrood 6.000 Sats: 21.000 - 15.000 = 6.000. De werkelijke waarde van de betaling is dus 6.000 Sats. De echte waarde van de betaling zit dus verborgen in een nepbetaling die als lokkertje dient voor ketenanalyse.


Naast PayJoin en CoinJoin zijn er vele andere Bitcoin transactiestructuren die ofwel de analyse van de blokketen blokkeren of deze misleiden. Ik zou hier de [Stonewall](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4) en [StonewallX2](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b) transacties kunnen noemen, die het mogelijk maken om een flexibele mini CoinJoin te maken of om een flexibele mini CoinJoin te imiteren. Er zijn ook [Ricochet](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589) transacties die een verandering van Ownership van bitcoins simuleren door een veelvoud aan valse overschrijvingen naar zichzelf te doen.


Al deze tools zijn beschikbaar op Samourai Wallet op mobiel en Sparrow wallet op PC. Als je meer wilt leren over deze specifieke transactiestructuren, raad ik je aan mijn tutorials te ontdekken:


- [PayJoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f);
- [PayJoin - SAMOURAI Wallet](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab);
- [PayJoin - Sparrow wallet](https://planb.network/tutorials/privacy/on-chain/payjoin-sparrow-wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62);
- [STONEWALL](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4);
- [STONEWALL X2](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b);
- [RICOCHET](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).


## Conclusie

Ketenanalyse is een praktijk waarbij wordt geprobeerd om de stroom van bitcoins On-Chain te traceren. Om dit te doen, zoeken analisten naar patronen en kenmerken om min of meer plausibele hypotheses en interpretaties op te stellen.


De nauwkeurigheid van deze heuristieken varieert: sommige geven een hogere mate van zekerheid dan andere, maar geen enkele heuristiek kan claimen onfeilbaar te zijn. De opeenstapeling van verschillende convergerende heuristieken kan echter deze inherente twijfel verminderen, hoewel het onmogelijk blijft om deze volledig uit te sluiten.

We kunnen deze methoden in drie verschillende hoofdcategorieën indelen:


- Patronen, gericht op de algemene structuur van elke transactie;
- Interne heuristieken, die het mogelijk maken om alle details van een transactie uitputtend te onderzoeken, zonder uit te breiden naar de context;
- Externe heuristiek, die de analyse van de transactie in haar omgeving omvat, evenals alle externe gegevens die inzicht kunnen verschaffen.


Als gebruiker van Bitcoin is het essentieel om de fundamentele principes van ketenanalyse te beheersen om het effectief tegen te gaan en zo je privacy te beschermen.


## Technische woordenlijst:

**P2PKH:** acroniem voor Pay to Public Key Hash. Het is een standaard scriptmodel dat gebruikt wordt om bestedingsvoorwaarden op een UTXO vast te stellen. Het maakt het mogelijk bitcoins vast te zetten op een Hash van een publieke sleutel, dat wil zeggen, op een ontvangende Address. Dit script wordt geassocieerd met de Legacy-standaard en werd geïntroduceerd in de eerste versies van Bitcoin door Satoshi Nakamoto. In tegenstelling tot P2PK, waar de openbare sleutel expliciet in het script is opgenomen, gebruikt P2PKH een cryptografische afdruk van de openbare sleutel, met wat metadata, ook wel een "ontvangende Address" genoemd. Dit script bevat de RIPEMD160 Hash van de SHA256 van de openbare sleutel en bepaalt dat, om toegang te krijgen tot het geld, de ontvanger een openbare sleutel moet leveren die overeenkomt met deze Hash, evenals een geldige digitale handtekening die is gegenereerd uit de bijbehorende privésleutel. P2PKH-adressen zijn gecodeerd met het Base58Check-formaat, waardoor ze bestand zijn tegen typografische fouten door het gebruik van een controlesom. Deze adressen beginnen altijd met het getal 1.

**P2TR:** acroniem voor Pay to Taproot ("betalen aan de wortel"). Het is een standaard scriptmodel dat wordt gebruikt om bestedingsvoorwaarden op een UTXO vast te stellen. P2TR werd geïntroduceerd met de implementatie van Taproot in november 2021. Het maakt gebruik van het Schnorr protocol om cryptografische sleutels samen te voegen, evenals Merkle bomen voor alternatieve scripts, bekend als MAST (Merkelized Alternative Script Tree). In tegenstelling tot traditionele transacties waarbij de bestedingsvoorwaarden openbaar zijn (soms bij ontvangst, soms bij besteding), maakt P2TR het mogelijk om complexe scripts te verbergen achter een enkele ogenschijnlijke openbare sleutel. Technisch gezien vergrendelt een P2TR script bitcoins op een unieke Schnorr publieke sleutel, aangeduid als K. Deze K sleutel is echter eigenlijk een aggregaat van een publieke sleutel P en een publieke sleutel M, de laatste wordt berekend uit de Merkle Root van een lijst van ScriptPubKeys. Sleutelaggregatie wordt uitgevoerd met het Schnorr-handtekeningprotocol. Bitcoins die vergrendeld zijn met een P2TR script kunnen op twee verschillende manieren uitgegeven worden: ofwel door een handtekening te publiceren voor de openbare sleutel P, ofwel door te voldoen aan één van de scripts die in de Merkle Tree staan. De eerste optie wordt "sleutelpad" genoemd en de tweede "scriptpad" P2TR stelt gebruikers dus in staat om bitcoins te sturen naar een publieke sleutel of naar meerdere scripts van hun keuze. Een ander voordeel van dit script is dat, hoewel er meerdere manieren zijn om een P2TR uit te geven, alleen de manier die gebruikt wordt onthuld hoeft te worden bij het uitgeven, waardoor de ongebruikte alternatieven privé blijven. Bijvoorbeeld, dankzij Schnorr sleutelaggregatie kan de publieke sleutel P zelf een geaggregeerde sleutel zijn, die mogelijk een Multisig voorstelt. P2TR is een versie 1 SegWit uitgang, wat betekent dat handtekeningen voor P2TR ingangen opgeslagen worden in de getuige van een transactie, en niet in de ScriptSig. P2TR adressen gebruiken Bech32m codering en beginnen met bc1p.

**P2WPKH:** Acroniem voor Pay to Witness Openbare Sleutel Hash. Het is een standaard scriptmodel dat wordt gebruikt om bestedingsvoorwaarden op een UTXO vast te stellen. P2WPKH werd geïntroduceerd met de implementatie van SegWit in augustus 2017. Dit script is vergelijkbaar met P2PKH (Pay to Public Key Hash), in die zin dat het ook bitcoins vergrendelt op basis van de Hash van een publieke sleutel, dat wil zeggen een ontvangende Address. Het verschil zit in de manier waarop handtekeningen en scripts in de transactie worden opgenomen. In het geval van P2WPKH is de scriptinformatie voor handtekeningen (ScriptSig) verplaatst van de traditionele transactiestructuur naar een aparte sectie genaamd Witness. Deze verplaatsing is een kenmerk van de SegWit (Segregated Witness) update. Deze techniek heeft het voordeel dat de transactiegegevens in het hoofdgedeelte kleiner worden, terwijl de benodigde scriptinformatie voor validatie in een apart gedeelte blijft. Hierdoor zijn P2WPKH transacties over het algemeen goedkoper in termen van kosten in vergelijking met Legacy transacties. P2WPKH adressen worden geschreven met Bech32 codering, wat bijdraagt aan een beknopter en minder foutgevoelig schrijven dankzij de BCH checksum. Deze adressen beginnen altijd met bc1q, waardoor ze gemakkelijk te onderscheiden zijn van Legacy ontvangstadressen. P2WPKH is een versie 0 SegWit uitvoer.


**UTXO:** Acroniem voor Niet-uitgegeven Transactie Output. Een UTXO is een transactie-output die nog niet is uitgegeven of gebruikt als input voor een nieuwe transactie. UTXO's vertegenwoordigen de fractie bitcoins die een gebruiker bezit en die momenteel beschikbaar zijn om te worden uitgegeven. Elke UTXO is geassocieerd met een specifiek uitvoer-script, dat de noodzakelijke voorwaarden definieert om de bitcoins uit te geven. Transacties in Bitcoin consumeren deze UTXO's als input en creëren nieuwe UTXO's als output. Het UTXO model is fundamenteel voor Bitcoin, omdat het een gemakkelijke verificatie mogelijk maakt dat transacties niet proberen bitcoins uit te geven die niet bestaan of al uitgegeven zijn. In wezen is een UTXO een stuk van Bitcoin.