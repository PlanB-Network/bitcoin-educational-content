---
name: Bouwen met Elements en Liquid Network
goal: Leren gebruiken en ontwikkelen met het Elements open-source Blockchain platform en de belangrijkste functies ervan
objectives: 

  - De basisconcepten van het Elements Blockchain platform en Liquid zijketens begrijpen.
  - Elements nodes leren opzetten en gebruiken voor standalone en Sidechain configuraties.
  - Praktijkervaring opdoen met de federatieve block signing en de Federated 2-Way Peg.
  - Veilige, efficiënte Blockchain-omgevingen opzetten en beheren voor echte gebruikssituaties.

---

# Voortbouwen op Liquid en Elements


Ontdek de geavanceerde functies en mogelijkheden van Liquid en Elements, en leer hoe je deze tools effectief kunt gebruiken om je ontwikkelingsprojecten te verbeteren. Deze training biedt een complete theoretische en praktische basis, zodat je functies als Confidential Transactions, Issued Assets en Federated block signing onder de knie krijgt.


Liquid, gebaseerd op het Elements framework, is ontworpen om privacy, schaalbaarheid en functionaliteit voor financiële en technische oplossingen te verbeteren. In deze cursus doe je praktijkervaring op met de uitgifte en het beheer van activa, Federated 2-Way Peg en het gebruik van tools zoals elementsd en elements-cli, zodat je innovatieve oplossingen op maat kunt maken.


Deze cursus is op maat gemaakt voor ontwikkelaars van alle ervaringsniveaus. Beginners en gemiddelde gebruikers vinden toegankelijke uitleg en praktische voorbeelden, terwijl gevorderde gebruikers dieper kunnen ingaan op technische details en minder bekende functies van Liquid en Elements.


Doe mee om je vaardigheden te verbeteren, het volledige potentieel van Liquid en Elements te ontsluiten en impactvolle tools te creëren voor de toekomst van de Liquid innovatie.

+++

# Inleiding


<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>


## Cursus Overzicht


<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>


:::video id=e0166470-5561-4b3b-9d0d-4edee69b64d8:::


Welkom bij de SID202-cursus!


Het doel van *Elements Academy* is het introduceren en uitleggen van de belangrijkste concepten van *Elements*, het open-source platform waarop Liquid Sidechain is gebouwd. Tegen het einde van deze cursus zou je een goed begrip moeten hebben van de belangrijkste kenmerken van Elements, zoals Confidential Transactions en Issued Assets, en van de processen die komen kijken bij het gebruik van Elements Core. Elk deel van de cursus bevat lessen met verklarende teksten en video's, gevolgd door een quiz.


Deze training leert je hoe je het open-source Elements platform kunt gebruiken en ermee kunt ontwikkelen, met een focus op de Liquid Network. U zult ontdekken hoe deze technologieën de privacy, schaalbaarheid en functionaliteit van uw ontwikkelingsprojecten kunnen verbeteren. Of u nu een beginner of een ervaren ontwikkelaar bent, deze cursus biedt u een sterke basis voor het beheersen van de fundamentele concepten van Elements en Liquid, en hun praktische toepassingen.


**Deel 1: Inleiding**

We beginnen met een uitgebreid overzicht van Elements concepten. Je zult leren hoe dit platform is ontworpen om een modulaire en flexibele basis te bieden voor het maken van sidechains zoals Liquid. Het doel is om de structuur van Elements te begrijpen voordat we in de praktische toepassingen duiken.


**Deel 2: Elements**

Dit hoofdstuk gaat over hoe Elements werkt. Je leert hoe je een Elements knooppunt configureert, in standalone modus bedient, of als Sidechain gebruikt.


**Deel 3: Elements gebruiken - Praktijkvoorbeelden**

Zodra je de theoretische basis onder de knie hebt, behandelen we de praktische toepassingen van Elements. Je leert hoe je Confidential Transactions uitvoert, activa uitgeeft en de heruitgifte van activa beheert.


**Deel 4: Elements Federatie**

Hier zullen we geavanceerde mechanismen onderzoeken, waaronder gefedereerde block signing, Elements gebruiken als Sidechain en onafhankelijke blockchains creëren. Deze sectie zal je helpen te begrijpen hoe je de veiligheid, integriteit en interoperabiliteit van Elements-gebaseerde blockchains kunt waarborgen.


Klaar om het potentieel van Elements en de Liquid Sidechain te verkennen? Laten we beginnen!



## Elements Overzicht


<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>


:::video id=eae666b4-eddc-4e00-adea-2a5f94396044:::


Elements is een open source, Sidechain-geschikt [Blockchain](https://planb.academy/resources/glossary/blockchain) platform, dat toegang biedt tot krachtige functies ontwikkeld door leden van de gemeenschap, zoals Confidential Transactions en Issued Assets.


Elements is in de kern een protocol dat het mogelijk maakt [consensus](https://planb.academy/resources/glossary/consensus) te vormen rond de [transactiegeschiedenis](https://planb.academy/resources/glossary/transaction-tx) en regels die de overdracht en creatie van activa regelen die zijn opgeslagen in een gedistribueerd Blockchain Ledger.


Meer achtergrondinformatie over Elements is te vinden op de Elements Project website (https://elementsproject.org/), de officiële Liquid blog (https://blog.Liquid.net/) en het ontwikkelaarsportaal (https://Liquid.net/devs).


### Elements


Elements, gelanceerd in 2015, verlaagt de interne ontwikkelings- en onderzoekskosten en maakt gebruik van de allernieuwste Blockchain technologie, waardoor veel nieuwe gebruikssituaties mogelijk worden. Een Blockchain op basis van Elements kan werken als een zelfstandige Blockchain of gekoppeld worden aan een andere Blockchain en als een Sidechain worden gebruikt. Elements draaien als een Sidechain maakt het mogelijk om activa verifieerbaar over te dragen tussen verschillende blockchains.


Gebouwd op de Bitcoin codebase en deze uitgebreid, kunnen ontwikkelaars die bekend zijn met de bitcoind API snel en kosteneffectief werkende blockchains maken en proof-of-concept projecten testen. Omdat het gebouwd is op de Bitcoin codebase, kan Elements ook functioneren als een testbed voor veranderingen aan het Bitcoin protocol zelf.


Enkele van de belangrijkste kenmerken van Elements worden hierna opgesomd.


#### Confidential Transactions


Standaard zijn alle adressen in Elements blinded met Confidential Transactions. Blindering is het proces waarbij het bedrag en type van het vermogen dat wordt overgedragen cryptografisch voor iedereen verborgen blijft, behalve voor de deelnemers en degenen aan wie ze het Blinding key willen openbaren.


#### Issued Assets


Issued Assets op Elements maakt het mogelijk om meerdere soorten activa uit te geven en over te dragen tussen netwerkdeelnemers. Een uitgegeven activum profiteert ook van Confidential Transactions en kan opnieuw uitgegeven of vernietigd worden door iedereen die het relevante reissuance token bezit.


#### Federated 2-Way Peg


Elements is een Blockchain platform voor algemeen gebruik, dat ook "gekoppeld" kan worden aan een bestaande Blockchain (zoals Bitcoin) om de overdracht van activa van de ene keten naar de andere in twee richtingen mogelijk te maken. Door Elements te implementeren als een Sidechain kun je om sommige inherente eigenschappen van de hoofdketen heen werken, terwijl je een goede mate van veiligheid behoudt, die wordt geboden door activa die zijn beveiligd op de hoofdketen.


#### Getekende blokken


Elements gebruikt een Strong Federation van ondertekenaars, Block Signers genaamd, die [blokken](https://planb.academy/resources/glossary/block) op een betrouwbare en tijdige manier ondertekenen en aanmaken. Dit verwijdert de transactielatentie van het PoW Mining proces, dat onderhevig is aan grote variatie in bloktijd vanwege de willekeurige poisson verdeling. Het Federated block signing proces bereikt betrouwbare blokcreatie zonder de noodzaak van vertrouwen van derden of computationele `algoritme` gebaseerde Mining.


Elements voegt al deze functies toe aan de Bitcoin Core codebase, breidt de mogelijkheden van het mainchain protocol uit en maakt nieuwe zakelijke gebruikssituaties mogelijk wanneer het wordt ingezet als een Sidechain of als een zelfstandige Blockchain oplossing.


# Element


<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>


## Hoe Elements werkt


<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>


:::video id=7c8c7981-11e5-47a2-a257-ef998f4892f5:::


Elements biedt een technische oplossing voor problemen waar Blockchain gebruikers dagelijks mee te maken hebben; transactietraagheid, gebrek aan privacy en risico op [fungibiliteit](https://planb.academy/resources/glossary/fungibility).


Elements overwint deze problemen door het gebruik van Federated block signing en Confidential Transactions.


In tegenstelling tot het Bitcoin netwerk, is het proces van block signing binnen Elements niet afhankelijk van Dynamic Membership Multiparty Signatures (DMMS) en Proof of Work (PoW). In plaats daarvan gebruikt Elements een Strong Federation van ondertekenaars, Block Signers genaamd, die blokken op een betrouwbare en tijdige manier kunnen ondertekenen en aanmaken. Dit verwijdert de transactielatentie van het PoW Mining proces, dat onderhevig is aan grote variatie in bloktijd vanwege de willekeurige poisson verdeling. Het Federated block signing proces bereikt betrouwbare blokaanmaak zonder de noodzaak voor vertrouwen van derden.


Elements kan draaien als een Sidechain naar een andere Blockchain, zoals Bitcoin, of als een zelfstandige Blockchain zonder afhankelijkheden van andere netwerken.


Bij gebruik als Sidechain bevat de Strong Federation ook leden die de veilige en gecontroleerde overdracht van activa tussen een hoofdketen en een Elements Sidechain mogelijk maken. De gecontroleerde overdracht van activa wordt Federated 2-Way Peg genoemd en de leden die de rol van activaoverdracht vervullen, worden watchmen genoemd.


De processen die betrokken zijn bij het runnen van een Elements netwerk en de rollen van de deelnemers in het netwerk zijn belangrijk om te begrijpen hoe Elements werkt.


Of het nu geïmplementeerd is als een Sidechain of een zelfstandige Blockchain, Elements maakt gebruik van sterke federaties van blokondertekenaars om blokken te produceren.


### Sterke federaties


Elements gebruikt een consensusmodel dat voor het eerst werd voorgesteld door Blockstream, genaamd Strong Federations. Een Strong Federation heeft geen Proof of Work (PoW) nodig en vertrouwt in plaats daarvan op de collectieve acties van een groep wederzijds wantrouwende deelnemers, Functionarissen genaamd.


De rollen die een Functionaris kan vervullen binnen een Strong Federation zijn: Block Signers en watchmen. Block Signers zijn nodig als je Elements in Sidechain of standalone Blockchain modus draait, terwijl watchmen alleen nodig zijn in een Sidechain opstelling.


De acties die een lid van een Strong Federation kan uitvoeren zijn verdeeld over twee verschillende rollen om de veiligheid te verbeteren en de schade die een aanvaller kan aanrichten te beperken.


De combinatie van de rollen van deze deelnemers stelt Elements in staat om zowel snelle blokcreatie (snellere en definitieve transactiebevestiging) als verzekerde, overdraagbare activa (gekoppelde activa die direct aan een andere Blockchain gekoppeld kunnen worden) te leveren.


Je kunt de [whitepaper](https://planb.academy/resources/glossary/white-paper) over sterke federaties hier lezen: https://blockstream.com/strong-federations.pdf


### Blok Ondertekenaars


Een Blockchain zoals die van Bitcoin wordt uitgebreid wanneer iemand die deel uitmaakt van een dynamische groep van blokondertekenaars de keten uitbreidt door Proof of Work aan te tonen. De dynamische aard van de set introduceert de latentieproblemen die inherent zijn aan zulke systemen.


Door gebruik te maken van een vaste set ondertekenaars vervangt een Federated model de dynamische set door een bekende set, schema met meerdere handtekeningen. Het verminderen van het aantal deelnemers dat nodig is om de Blockchain uit te breiden verhoogt de snelheid en schaalbaarheid van het systeem, terwijl validatie door alle partijen de integriteit van de transactiegeschiedenis garandeert.


Federated block signing bestaat uit verschillende fasen:



- Stap 1 - Blokondertekenaars stellen kandidaat-blokken voor in een round-robin mode aan alle andere deelnemende Blokondertekenaars.



- Stap 2 - Elke block signer signaleert zijn intentie door vooraf toe te zeggen het gegeven kandidaat-blok te ondertekenen.



- Stap 3 - Als de opgegeven drempel voor pre-Commitment wordt gehaald, ondertekent elke block signer het blok.



- Stap 4 - Als aan de handtekeningdrempel (die kan verschillen van die van stap 3) is voldaan, wordt het blok geaccepteerd en naar het netwerk gestuurd. De Strong Federation heeft consensus bereikt over het laatste blok transacties.



- Stap 5 - Het volgende blok wordt dan voorgesteld door de volgende block signer in de round-robin en het proces herhaalt zich.


Omdat het genereren van een Strong Federation blok niet probabilistisch is en gebaseerd is op een vaste set ondertekenaars, zal het nooit onderhevig zijn aan multi-blok reorganisaties. Dit zorgt voor een aanzienlijke vermindering van de wachttijd die gepaard gaat met het bevestigen van transacties. Het verwijdert ook de stimulans om te mijnen voor winst (d.w.z. de blokbeloningen) en vervangt deze door een stimulans om productief deel te nemen aan een netwerk waar alle deelnemers hetzelfde gedeelde doel hebben; ervoor zorgen dat het netwerk blijft functioneren op een manier die voordelig is voor iedereen. Het doet dit zonder een single point of failure of hogere vertrouwensvereisten te introduceren.


### Elements als Sidechain - watchmen en de Federated 2-Way Peg


Wanneer je als Sidechain draait, hebben sommige leden van de Strong Federation een extra rol te vervullen, die van de watchmen. watchmen zijn verantwoordelijk voor de overdracht van activa in en uit een Elements Sidechain, processen die bekend staan als `Peg-In` en `Peg-Out`.


Om een Sidechain op een betrouwbare manier te laten werken, moeten deelnemers kunnen verifiëren dat de Supply van activa gecontroleerd en verifieerbaar is. Een Elements Sidechain gebruikt een 2-weg federated peg om de overdracht van activa in en uit een Elements Blockchain in twee richtingen mogelijk te maken. Dit voldoet aan de eisen van bewijsbare uitgifte en overdrachten tussen ketens.


De Federated 2-Way Peg functie maakt het mogelijk dat een activum interoperabel is met andere blockchains en representatief is voor het native activum van een andere Blockchain. Door uw Blockchain aan een andere te koppelen, kunt u de mogelijkheden van de mainchain uitbreiden en enkele van zijn inherente beperkingen overwinnen.


Op hoog niveau vinden overdrachten naar de Sidechain plaats wanneer iemand tegoeden van de mainchain naar een Address stuurt, die gecontroleerd wordt door een watchmen [Wallet](https://planb.academy/resources/glossary/wallet) met meerdere handtekeningen. Hierdoor worden de tegoeden op de mainchain bevroren. watchmen valideert dan de transactie en geeft hetzelfde bedrag van de bijbehorende activa vrij binnen de Sidechain. De vrijgegeven activa worden naar een Sidechain Wallet gestuurd, die aanspraak kan maken op de oorspronkelijke mainchain activa. Dit proces verplaatst activa van de moederketen naar de Sidechain.


Om activa terug te sturen naar de mainchain, maakt een gebruiker een speciale peg-out transactie op de Sidechain. Deze transactie wordt gecontroleerd door watchmen, die vervolgens een transactie-uitgave ondertekenen van de Wallet met meerdere handtekeningen, die ze controleren op de mainchain. Een drempelaantal deelnemers in de federatie moet tekenen voordat de mainchain transactie geldig wordt. Wanneer de watchmen een activum terugsturen naar de mainchain vernietigen ze ook het corresponderende bedrag op de Sidechain, waardoor de activa effectief worden overgedragen tussen blockchains.


## Elements instellen en uitvoeren


<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>


:::video id=1f73dfee-3623-483b-ab42-07d9286ed999:::


Aangezien Elements gebaseerd is op de Bitcoin codebase, zijn de componenten waaruit een werkend netwerk bestaat zeer vergelijkbaar.


De Elements node software zelf heet `elementsd` en draait als een daemon op de machine van een gebruiker. Een daemon (of service in Windows) is een programma dat op de achtergrond draait zonder dat een ingelogde gebruiker er direct controle over heeft.


Opmerking: In dit document zullen we altijd verwijzen naar elementsd als de daemon versie, maar alles zou gedaan kunnen worden met Elements-qt, mits de serveroptie is ingeschakeld.


De Elements daemon maakt verbinding met andere [knooppunten](https://planb.academy/resources/glossary/node) op het netwerk zodat het Exchange transactie- en blokgegevens kan valideren en zijn lokale kopie van de Blockchain van het netwerk kan uitbreiden.


De Elements software bestaat ook uit een clientprogramma genaamd `elements-cli` waarmee u Remote Procedure Call (RPC) commando's naar elementsd kunt sturen vanaf de commandoregel. Dit kan bijvoorbeeld gebruikt worden om een Wallet balans op te vragen, transactie- of blokgegevens te bekijken of een transactie uit te zenden. Deze opzet zou bekend moeten zijn bij iedereen die de Bitcoin equivalenten, bitcoind en bitcoin-cli, heeft gebruikt.


Omdat een Elements node geconfigureerd kan worden door parameters door te geven bij het opstarten of via een configuratiebestand, is het mogelijk om meer dan één instantie op dezelfde machine te laten draaien. Dit is handig voor test- en ontwikkelingsdoeleinden, omdat je je eigen lokale netwerk kunt opzetten op een enkele machine, waarbij elk Elements knooppunt zijn eigen kopie heeft van de Blockchain data, zijn eigen pool van onbevestigde geldige transacties beheert en luistert naar RPC verzoeken op verschillende poorten.


### De Elements Codeopslagplaats en gemeenschap


Elements is een open-source project en de broncode ervan kan gevonden worden in de Elements GitHub repository op https://github.com/ElementsProject/Elements. De repository bevat de broncode voor de elementsd en elements-cli programma's, samen met ondersteunende installatie- en bouwtools, een reeks tests en wat instructiedocumentatie.


Als aanvulling op de code repository, is er ook de https://elementsproject.org website, een community-gerichte bron met uitleg over wat Elements is, hoe het werkt en een uitgebreide tutorial sectie. De tutorial richt zich op het leren over Elements door het volgen van commandoregelvoorbeelden en laat zien hoe je er eenvoudige desktop- en webapplicaties op kunt bouwen. De site bevat ook populaire Elements discussieforums uit de gemeenschap en wordt zelf gehost op GitHub, zodat de gemeenschap bijdragen kan leveren aan de inhoud van de site.


Om Elements op uw machine te draaien, moet u eerst de broncode klonen (een kopie downloaden), alle afhankelijkheden van de code installeren en tenslotte de daemon en client executables bouwen. De Elements software is dan klaar om geconfigureerd en gedraaid te worden.


## Nodes en netwerken configureren


<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>


Configuratie-instellingen kunnen worden doorgegeven aan een Elements knooppunt bij het opstarten om de manier te veranderen waarop het draait, gegevens valideert, verbinding maakt met andere knooppunten en zijn Blockchain gegevens initialiseert.


Instellingen worden geladen uit het aangewezen `Elements.conf` bestand of doorgegeven als parameters via de commandoregel.


Sommige dingen kunnen worden gewijzigd met deze parameters:



- De naam van de default asset die gebruikt wordt in een standalone Blockchain implementatie.
- Het nummer van het oorspronkelijk aangemaakte actief.
- Het activum dat moet worden gebruikt bij het betalen van transactiekosten op het netwerk.
- De opslaglocatie van de Blockchain databestanden.
- De RPC referenties die gebruikt worden om verbinding te maken met een Bitcoin knooppunt.
- De `n of m` drempel waaraan moet worden voldaan en de geldige [openbare sleutels](https://planb.academy/resources/glossary/public-key) die blokken kunnen ondertekenen.
- Het [script](https://planb.academy/resources/glossary/script) dat moet worden uitgevoerd om activa in en uit een Sidechain te verplaatsen.
- Of een Bitcoin-knooppunt al dan niet als Sidechain moet worden verbonden.


Veel van deze regels maken deel uit van de consensusregels van het netwerk, dus is het belangrijk dat ze worden toegepast op alle knooppunten bij het opstarten. Sommige kunnen veranderd worden nadat een keten geïnitialiseerd is, maar sommige moeten gerepareerd worden nadat ze gebruikt zijn om een keten te initialiseren.


Het gebruik van parameters wordt later in de cursus behandeld als en wanneer ze betrekking hebben op elke sectie.


### Basisbewerkingen met de opdrachtregel


Deze cursus laat voorbeelden zien die het `elements-cli` programma gebruiken om RPC aanroepen te doen naar één of meer Elements knooppunten. Dit wordt gedaan vanaf een terminal sessie en om de commando's korter te maken wordt een `alias` gebruikt. Door deze conventie zie je zoiets als de volgende commando's:


```bash
e1-dae

e1-cli getnewaddress
```


De `e1-dae` en `e1-CLI` zijn eigenlijk een typografische snelkoppeling die gebruik maakt van de `alias` functie van de terminal. De `e1-dae` en `e1-CLI` worden daadwerkelijk vervangen wanneer het commando wordt uitgevoerd en het commando dat wordt uitgevoerd is vergelijkbaar met:


```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1

$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```


Wat we hierboven zien is een aanroep om de Elements daemon te starten en een aanroep naar de elements-cli programma's in de `$HOME/Elements/src` directory en een waarde voor de `datadir` parameter. Met de `datadir` parameter kunnen we de daemon en client instanties vertellen waar ze hun configuratiebestanden moeten plaatsen en, in het geval van de daemon, waar ze hun kopie van de Blockchain moeten opslaan. Omdat ze een configuratiebestand delen, kan de client RPC aanroepen doen naar de daemon.


Door het bovenstaande commando opnieuw uit te voeren, maar met een andere `datadir` waarde, kunnen we meer dan één instantie van Elements starten, elk met zijn eigen aparte kopie van Blockchain en configuratie-instellingen. Volgens deze conventie zullen we in de cursus de alias `e2-dae` en `e2-CLI` gebruiken om te verwijzen naar een andere datadir directory dan die van e1. Dus het bovenstaande voorbeeld voor onze tweede `e2` instantie zou zijn:


```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2

$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```


Hiermee kunnen we allerlei operaties uitvoeren, zoals het verhandelen van activa tussen knooppunten, het uitgeven van activa en het controleren van het gebruik van blindering in Confidential Transactions tussen verschillende knooppunten op hetzelfde netwerk.


# Element gebruiken Praktisch gebruik


<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>


## Confidential Transactions


<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>


:::video id=ea2121b6-24a8-458d-91e6-0c92eaf4dc65:::


In dit hoofdstuk leert u hoe u de Confidential Transactions functie van Elements kunt gebruiken.


Alle adressen in Elements zijn standaard blinded met Confidential Transactions, die de hoeveelheid en het type overgedragen activa alleen zichtbaar houden voor deelnemers aan de transactie (en degenen aan wie ze de Blinding key willen openbaren), terwijl ze nog steeds cryptografisch garanderen dat er niet meer munten kunnen worden uitgegeven dan er beschikbaar zijn.


### Vertrouwelijke adressen en Confidential Transactions


Standaard wordt een nieuwe Address in Elements aangemaakt met het `getnewaddress` commando als een Confidential Address.


Om Confidential Transactions te demonstreren, laten we e2 zichzelf wat geld sturen en dan proberen de transactie van e1 te bekijken. Dit demonstreert de vertrouwelijke aard van transacties in Elements.


Elke nieuwe Address gegenereerd door een Elements knooppunt is standaard vertrouwelijk. We kunnen dit demonstreren door e2 een nieuwe Address te laten generate-en.


```
e2-cli getnewaddress
```


Merk op dat de Address begint met e1. Dit identificeert het als een Confidential Address. Als je de Address in meer detail bekijkt met het getaddressinfo commando, zie je meer details van de Address.


```
e2-cli getaddressinfo <address>
```


Je kunt zien dat er een confidential_key eigenschap is die ons vertelt dat het een Confidential Address is.


De confidential_key is de publieke Blinding key, die aan de Confidential Address zelf wordt toegevoegd. Dit is de reden waarom een Confidential Address zo lang is.


Het heeft ook een bijbehorende Unconfidential address. Als je gewone, niet-vertrouwelijke transacties wilt gebruiken binnen Elements, moeten activa naar deze Address worden gestuurd in plaats van naar degene met de lq1 prefix.


We kunnen nu e2 wat geld laten sturen naar de Address die hij heeft gegenereerd. Dit zal later aantonen dat e1, omdat het niet een van de transactiepartijen is, de details van de transactie niet kan zien.


```
e2-cli sendtoaddress <address>
```


Noteer de transaction ID. Bevestig de transactie.


```
e2-cli -generate 101
```


Als we kijken naar de transactie waarbij e2 geld naar zichzelf stuurde vanuit het perspectief van e2 zelf.


```
e2-cli gettransaction <txid>
```


Als je naar boven scrollt door de transactiedetails, kun je zien dat e2 de verzonden en ontvangen bedragen kan zien, evenals de activa van de transactie. Je kunt ook de eigenschappen amountblinder en assetblinder zien, die worden gebruikt om de details af te schermen voor andere knooppunten die niet betrokken zijn bij de transactie.


Om de details van dezelfde transactie van e1 te controleren, moeten we eerst de onbewerkte transactiegegevens ophalen.


```
e1-cli getrawtransaction <txid>
```


Dat geeft ruwe transactiegegevens. Als je in de vout-sectie kijkt, zie je dat er drie instanties zijn. De eerste twee instanties zijn de ontvangst- en wisselbedragen en de derde is de transactiekosten. Van deze drie bedragen is de vergoeding de enige waarin je een waarde kunt zien, omdat de vergoeding zelf altijd unblinded binnen Elements is.


### Verblindende toetsen


Wat de eerste twee voutsecties laten zien zijn "Blinded ranges" van de waardebedragen en de Commitment gegevens die fungeren als bewijs van het werkelijke bedrag en type activa dat is verhandeld.


Zelfs als we de [private sleutel](https://planb.academy/resources/glossary/private-key) van e2 in de Wallet van e1 zouden importeren, zou het nog steeds niet in staat zijn om de bedragen en het type activa dat verhandeld is te zien, omdat het nog steeds geen kennis heeft van de Blinding key die door e2 gebruikt wordt. We zullen dit bewijzen door de private sleutel die gebruikt wordt door e2's Wallet te importeren in die van e1. Eerst moeten we de sleutel van e2 exporteren


```
e2-cli dumpprivkey <address>
```


Importeer het vervolgens in e1.


```
e1-cli importprivkey <privkey>
```


Nu kunnen we bewijzen dat e1 de waarden nog steeds niet kan zien.


```
e1-cli gettransaction <txid>
```


Het toont inderdaad 0 als de tx hoeveelheid terwijl het eigenlijk 1 was.


Om de werkelijke, onbelijnde waarde te kunnen zien, hebben we de Blinding key nodig. Om dit te doen exporteren we eerst de Blinding key uit e2.


```
e2-cli dumpblindingkey <address>
```


Importeer het vervolgens in e1.


```
e1-cli importblindingkey <address> <blinding key>
```


Als we nu de transactiegegevens van e1 krijgen.


```
e1-cli gettransaction <txid>
```


Het laat zien dat we met de geïmporteerde Blinding key nu de werkelijke waarde van 1 in de transactie kunnen zien.


In dit gedeelte hebben we gezien dat het gebruik van een Blinding key de hoeveelheid en soort activa in een transactie verbergt, en dat we door het importeren van de juiste Blinding key deze waarden kunnen onthullen. In de praktijk kan een Blinding key bijvoorbeeld aan een accountant worden gegeven, als er behoefte is om de bedragen en soorten activa van een partij te verifiëren. De Confidential Transactions eigenschap van Elements maakt het ook mogelijk om "bereikbewijzen" uit te voeren. Met bereikbewijzen kan worden aangetoond dat een bedrag van een actief binnen een bepaald bereik wordt aangehouden, zonder dat het werkelijke bedrag zelf bekend hoeft te worden gemaakt.


We hebben ook gezien dat Confidential Transactions optioneel zijn, maar standaard worden ingeschakeld wanneer een nieuwe Address wordt gegenereerd.


Dat was het voor deze les; succes met de quiz en tot de volgende!


## Issued Assets


<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>


:::video id=7ac63148-d730-496d-85d4-0032aaf09be1:::


In dit hoofdstuk leer je hoe je de Issued Assets functie van Elements kunt gebruiken.


Issued Assets maakt het mogelijk om meerdere soorten activa uit te geven en over te dragen tussen Elements netwerkdeelnemers. Elk knooppunt op het netwerk kan zijn eigen activa uitgeven. Uitgiften kunnen fungibele Ownership activa vertegenwoordigen, waaronder vouchers, coupons, valuta, deposito's, obligaties, aandelen, enz. Issued Assets opent de deur voor het bouwen van Trustless uitwisselingen, opties en andere geavanceerde slimme contracten waarbij zelf-Issued Assets betrokken is.


Een uitgegeven activum profiteert ook van Confidential Transactions en kan opnieuw worden uitgegeven door iedereen die de bijbehorende token bezit.


De eerste stap is dat we toegang nodig hebben tot twee Elements nodes, die we e1 en e2 zullen noemen. De nodes hebben hun blockchains gereset en de default asset tussen hen verdeeld.


De twee nodes bevinden zich op hetzelfde lokale netwerk en zijn met elkaar verbonden, en delen daarom dezelfde transacties in hun transactie [Mempool](https://planb.academy/resources/glossary/mempool) en identieke blockchains. Hoewel ze op dezelfde machine draaien, is het de moeite waard om op te merken dat ze niet dezelfde Blockchain bestanden delen. Elke node beheert zijn eigen lokale kopie van de Blockchain, die dezelfde transactiegeschiedenis bevat omdat ze in consensus zijn en zich aan dezelfde protocolregels houden als elkaar.


Laten we beginnen met het controleren van het beeld dat elk knooppunt heeft van de bestaande activa-uitgiftes op het netwerk.


Dit wordt gedaan met het listissuances commando.


```
e1-cli listissuances

e2-cli listissuances
```


Zoals je kunt zien, tonen beide knooppunten dezelfde uitgiftegeschiedenis. Ze laten beide één goed zien, de initiële uitgifte van 21 miljoen Bitcoin die on chain initialisatie werd gecreëerd. Je kunt de hexadecimale id van de activa zien in de resultaten van het uitvoeren van het bovenstaande commando en ook het label dat aan de activa is toegewezen, namelijk 'Bitcoin'.


Het is vermeldenswaard dat de default asset altijd een label krijgt wanneer de keten wordt geïnitialiseerd. Als je je eigen goederen uitgeeft, kun je zelf labels voor ze instellen, wat we binnenkort zullen doen. Voordat we dat kunnen doen, moeten we ons eigen object uitgeven.


We laten e1 de nieuwe asset uitgeven. Dit wordt gedaan met het issueasset commando.


```
e1-cli issueasset 100 1 false
```


`issueasset` accepteert 3 parameters.


Het aantal nieuwe activa dat moet worden uitgegeven, we hebben 100 gebruikt. Het aantal te creëren tokens (tokens worden gebruikt om hoeveelheden van een activum opnieuw uit te geven), waarvan we 1 hebben gekozen. De laatste parameter vertelt Elements om de uitgifte van activa te creëren als blinded of unblinded. We gebruiken unblinded, omdat we zo meteen de uitgiftebedragen van e2 willen bekijken, dus we voeren false in.


Het commando geeft gegevens over de uitgifte. Deze omvatten de transaction ID, waarvan je een kopie kunt maken voor later gebruik, de unieke hexadecimale waarde van het goed en de unieke hexadecimale waarde van de token van het goed.


generate een blok om de uitgiftetransactie te bevestigen.


```
e1-cli -generate 1
```


Voer het `listissuances` commando opnieuw uit tegen e1.


```
e1-cli listissuances
```


Hieruit blijkt dat e1 nu op de hoogte is van 2 uitgiftes, de initiële uitgifte van Bitcoin en ons nieuw uitgegeven actief, waarvan we er 100 kunnen zien. Let op de hexadecimale waarde van het nieuwe activum en dat er geen bijbehorend activalabel is, zoals bij de uitgifte van Bitcoin.


Controleer de lijst met bekende emissies van e2 opnieuw.


```
e2-cli listissuances
```


Hieruit blijkt dat e2 zich niet bewust is van de uitgifte van activa door e1. Het ziet alleen de initiële uitgifte van Bitcoin die het al kon zien.


Dit komt omdat e2 niet op de hoogte is van, en niet kijkt naar, de Address waar het nieuwe bedrijfsmiddel naartoe werd gestuurd toen het werd uitgegeven door e1.


Het is vermeldenswaard dat ook al kan e2 de uitgifte zelf niet zien, e1 toch een deel van het activum naar e2 zou kunnen sturen. Het nieuwe activum zou dan verschijnen als een beschikbaar saldo in e2's Wallet, ook al is het zich niet bewust van de oorspronkelijke uitgifte.


Om e2 in staat te stellen de werkelijke uitgifte (en dus het uitgegeven bedrag) te zien, moeten we de Address aan e2 toevoegen als een bekeken Address.


Om dit te doen, moeten we achterhalen naar welke Address het activum is gestuurd. Hiervoor gebruiken we de transaction ID die we eerder hebben gekopieerd en laten e1 de details van die transactie ophalen, zodat we de juiste Address kunnen vinden om toe te voegen aan de Wallet volglijst van e2.


```
e1-cli gettransaction <the-issuance-transaction-id>
```


Als je voorbij de hexadecimale waarde van de transactiegegevens scrolt, zie je de Address die 100 van onze nieuwe goederen heeft ontvangen, geïdentificeerd aan de hand van de hexadecimale waarde.


Neem het Address en kopieer het zodat we het kunnen importeren in e2.


Laten we nu die Address importeren in e2. Hiervoor gebruiken we het importaddress commando.


```
e2-cli importaddress <the-issued-to-address>
```


Als we nu de lijst met uitgiften van e2 bekijken.


```
e2-cli listissuances
```


Je kunt zien dat ons nieuw uitgegeven activum nu is opgenomen in de lijst. Het e2 knooppunt kan ook het bedrag van het uitgegeven goed bepalen, samen met het bedrag van de bijbehorende token, omdat de uitgifte een unblinded uitgifte was. Om het gebruik van asset ID naar naam mapping binnen Elements mogelijk te maken, moet eerst Elements gestopt worden.


```
e1-cli stop
```


Start het dan opnieuw met een extra parameter die de hex van een asset koppelt aan het opgegeven label. Dit stelt het knooppunt in staat om gegevens over het asset in een meer menselijk leesbaar formaat weer te geven. Je kunt dit toevoegen aan het einde van Elements.conf als je dat wilt, dan hoef je het argument niet elke keer toe te voegen aan de daemon als je hem start. Bijvoorbeeld:


```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```


Maar we zullen hier de argumentenmethode gebruiken.


```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```


Het knooppunt opnieuw vragen om een lijst met uitgiften.


```
e1-cli listissuances
```


Dit laat zien dat de toewijzing van de hexadecimale waarde van het activum aan het label werkt. We controleren nogmaals de lijst met uitgiften van het e2-knooppunt.


```
e2-cli listissuances
```


Je kunt zien dat het knooppunt e2 geen toegang heeft tot dit label, omdat labels alleen beschikbaar zijn voor het knooppunt dat ze heeft ingesteld. We kunnen inderdaad een ander label toekennen aan dezelfde asset hex op e2 dan we deden op e1. Stop eerst het knooppunt e2.


```
e2-cli stop
```


Opnieuw starten met een ander label toegewezen aan de hex van ons nieuwe object.


```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```


Lijst met uitgiften van e2.


```
e2-cli listissuances
```


Labels van bedrijfsmiddelen zijn lokaal voor elk knooppunt, alleen de hexadecimale waarde van het bedrijfsmiddel wordt herkend door andere knooppunten op het netwerk.


De toewijzing van label naar activum hex is handig bij het uitvoeren van acties zoals transacties en Wallet saldo opvragen, omdat het een steno manier is om naar een activum te verwijzen. Als we bijvoorbeeld een deel van onze nieuwe activa (een bedrag van 10) van e1 naar e2 willen sturen zonder het label te gebruiken.


Eerst hebben we een Address nodig om de asset naartoe te sturen.


```
e2-cli getnewaddress
```


Gebruik dan het sendtoaddress commando.


```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```


Bevestig de transactie door een blok te genereren.


```
generate 1
```


Controleren of het activum is ontvangen op e2.


```
e2-cli getwalletinfo
```


We kunnen zien dat het activum inderdaad is ontvangen.


Merk op dat e2 de hex van het ontvangen object in kaart brengt en weergeeft met zijn eigen label. Een eenvoudigere manier om hetzelfde te doen zou zijn om het asset-label van e1 te gebruiken bij het verzenden.


```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```


Achter de schermen mapt Elements lokale labels naar hex waarden om het gebruik van Issued Assets te vereenvoudigen.


In dit gedeelte hebben we gezien hoe je activa kunt uitgeven en labelen. In de volgende sectie zullen we kijken naar het opnieuw uitgeven en vernietigen van hoeveelheden van een uitgegeven activum.


## Heruitgifte van activa


<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>


:::video id=7df967b0-ffff-42e1-b1d5-868e76289faf:::


In dit gedeelte leer je hoe je meer van een reeds uitgegeven activum kunt uitgeven en ook hoe je een bepaalde hoeveelheid van een uitgegeven activum kunt vernietigen.


De noodzaak om een activum opnieuw uit te geven (meer te creëren) of een hoeveelheid activum te vernietigen zal zich waarschijnlijk voordoen als het activum iets vertegenwoordigt dat geen vaste Supply heeft. Dit zou bijvoorbeeld van toepassing kunnen zijn op activa die goud vertegenwoordigen dat in een kluis ligt; als eenheden goud in en uit de kluis bewegen, moet het actief dat de Supply van de kluis vertegenwoordigt overeenkomstig omhoog of omlaag worden bijgesteld.


De heruitgifte van een bedrag van een actief vereist Ownership van de bijbehorende token die samen met het actief werd gecreëerd toen het oorspronkelijk werd uitgegeven.


Bij het maken van meer van een asset maakt het niet uit welk knooppunt de asset in eerste instantie heeft uitgegeven, zolang het knooppunt dat een hoeveelheid van een asset opnieuw uitgeeft in het bezit is van wat gewoonlijk de reissuance token van de asset wordt genoemd. We zullen kijken hoe je initieel een reissuance token aanmaakt, hoe je het gebruikt om een hoeveelheid van een asset opnieuw uit te geven en ook hoe je de reissuance token overdraagt aan andere nodes, zodat zij ook toestemming hebben om de asset opnieuw uit te geven.


We hebben toegang nodig tot twee Elements nodes, die we e1 en e2 zullen noemen. De knooppunten hebben hun blockchains gereset en de default asset tussen hen verdeeld.


We laten e1 een hoeveelheid van 100 van een nieuw activum uitgeven en creëren 1 reissuance token voor datzelfde activum. We maken de uitgifte aan als unblinded om het voorbeeld te vereenvoudigen. Dus laten we beginnen met de uitgifte van het activum en de bijbehorende reissuance token.


```
e1-cli issueasset 100 1 false
```


Noteer het ID van het goed en ook dat van de (heruitgave) token.


Omdat we later meer activa opnieuw zullen uitgeven vanuit e2, moeten we een notitie maken van de transaction ID waarin de activa is uitgegeven en die gebruiken om de Address te importeren waarnaar de activa is verzonden.


Bevestig de transactie.


```
e1-cli -generate 1
```


We controleren nu de details van de transactie met het gettransaction commando:


```
e1-cli gettransaction <txid>
```


Als je naar boven scrolt voorbij de hexadecimale gegevens van de transactie, zie je dat e1 in de transactie 1 reissuance token en 100 van de bijbehorende activa heeft ontvangen.


Neem een kopie van de Address, zodat we die in e2 kunnen importeren.


En nu de Address importeren in de Wallet van e2.


```
e2-cli importaddress <address>
```


We kunnen nu zien dat zowel e1 als e2 op de hoogte zijn van de uitgifte van activa.


```
e1-cli listissuances

e2-cli listissuances
```


Momenteel heeft e1 een bedrag van het actief en de 1 reissuance token, maar e2 niet.


```
e1-cli getwalletinfo
```


Merk ook op dat e1 minder default asset heeft dan voorheen, omdat het een klein bedrag heeft betaald om de transactiekosten te dekken. Dit bedrag moet door e1 worden geïnd wanneer het aangemaakte blok meer dan 100 blokken diep is.


```
e2-cli getwalletinfo
```


Als e1 de reissuance token vasthoudt, kan het er meer van uitgeven. Dit wordt gedaan met het reissueasset commando. Laten we e1 nog eens 100 van deze activa opnieuw uitgeven.


```
e1-cli reissueasset <asset-id> 100
```


Het controleren van de heruitgave werkte.


```
e1-cli getwalletinfo
```


Je kunt zien dat e1 nu 200 van het actief bezit, zoals verwacht.


Omdat e2 geen bedrag van de reissuance token heeft, krijgen ze een foutmelding als ze proberen het activum opnieuw uit te geven.


```
e2-cli reissueasset <asset-id> 100
```


Let op de foutmelding.


We kunnen de details van de heruitgave van e1 bekijken met het listissuances commando.


```
e1-cli listissuances
```


Let op de vlag `is_reissuance`.


Als we e2 nu een bedrag van de reissuance token sturen, kunnen ze zelf een bedrag van het activum opnieuw uitgeven. Eerst hebben we een Address nodig om het naar toe te sturen. Het is vermeldenswaard dat de reissuance token hetzelfde wordt behandeld als elk ander actief binnen Elements bij het verzenden en weergeven van saldi en dat het ook kan worden opgesplitst in kleinere waarden zoals elk ander actief, dus we hoeven niet 1 reissuance token naar e2 te sturen om het actief opnieuw te kunnen uitgeven. Elke denominatie is voldoende. Een Address genereren voor e2 om de reissuance token te ontvangen.


```
e2-cli getnewaddress
```


Stuur dan een fractie van de RIT van e1 naar e2.


```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```


Bevestig de transactie.


```
e1-cli -generate 1
```


We kunnen nu zien dat e2 de verzonden 0,1 vasthoudt.


```
e2-cli getwalletinfo
```


Dit betekent dat e2 nu meer activa kan uitgeven van de RIT die het in zijn Wallet heeft. We laten e2 500 van de activa opnieuw uitgeven.


```
e2-cli reissueasset <asset-id> 500
```


Controleer het resultaat van de heruitgifte.


```
e2-cli getwalletinfo
```


Je kunt zien dat e2 nu het heruitgegeven bedrag in zijn Wallet balans heeft en dat de RIT zelf niet wordt verbruikt tijdens het proces van heruitgifte van activa.


Het vernietigen van een hoeveelheid activa is iets wat iedereen kan doen die ten minste de hoeveelheid bezit die vernietigd wordt, het wordt niet geregeld door de reissuance token.


```
e2-cli destroyamount <asset-id>

e2-cli getwalletinfo
```


In dit gedeelte hebben we gezien hoe je een activum uitgeeft, samen met hoe je gebruik maakt van de reissuance token die optioneel wordt aangemaakt als onderdeel van de uitgifte van het activum. We hebben ook gezien hoe het overdragen van een reissuance token net zo eenvoudig is als het overdragen van elk ander activum, en dat het bezit van een willekeurige hoeveelheid reissuance token de houder het recht geeft om meer van het geassocieerde activum uit te geven. Het is daarom erg belangrijk om te controleren wie toegang heeft tot heruitgifte tokens in je netwerk. We hebben ook gezien hoe een hoeveelheid van een goed vernietigd kan worden en dat dit proces niet gecontroleerd wordt door het bezit van de reissuance token.


# Element Federatie


<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>


## block signing


<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>


:::video id=c5a81820-77d7-4a0c-9a4e-9323386a74ac:::


Elements ondersteunt een federatief ondertekeningsmodel waarmee u het aantal Strong Federation leden kunt specificeren die een voorgesteld blok moeten ondertekenen om een geldig blok te produceren.


Voorheen, en voor het gemak van het voorbeeld, hebben we blokken aangemaakt met het `generate` commando, dat niet hoefde te voldoen aan een multisignature vereiste om de aangemaakte blokken als geldig te laten accepteren door het netwerk.


We zullen onze knooppunten zo instellen dat ze 2-van-2 Multisig blokken moeten aanmaken. Dit wordt ingesteld met de signblockscript parameter, die kan worden toegevoegd aan het configuratiebestand of kan worden doorgegeven aan de node bij het opstarten. Om een keten met deze parameter te initialiseren, moeten we eerst het script bouwen waaruit het bestaat.


We doen dit met een aantal bestaande knooppunten, slaan de gegevens op die ze uitvoeren en wissen dan de keten zodat we hem opnieuw kunnen starten met onze signblockscript parameter. Dit is nodig omdat het script deel uitmaakt van de consensusregels van het netwerk en on chain geïnitialiseerd moet worden. Het kan niet op een later tijdstip worden toegevoegd aan een al bestaande keten.


We hebben toegang nodig tot twee Elements nodes, die we e1 en e2 zullen noemen. De nodes hebben hun blockchains gereset en de default asset tussen hen verdeeld.


Zorg ervoor dat de con_max_block_sig_size parameter op een hoge waarde is ingesteld in uw Elements.conf bestand, anders zal block signing verderop in deze sectie mislukken. Voor deze tutorial hebben we con_max_block_sig_size=2000 ingesteld.


Omdat we Blockchain resetten en de portemonnees van e1 en e2 wissen, moeten we een kopie maken van de adressen, publieke sleutels en privé sleutels die we gebruiken in generate het block signing script, zodat we ze later kunnen gebruiken.


Eerst hebben we elk van wat de block signing knooppunten zullen zijn nodig om generate een nieuwe Address te maken, waar je een kopie van moet maken.


```
e1-cli getnewaddress

e2-cli getnewaddress
```


Daarna moeten we de publieke sleutels uit de adressen halen en ze noteren voor later gebruik.


```
e1-cli getaddressinfo <e1-address>

e2-cli getaddressinfo <e2-address>
```


Pak dan de privésleutels, die we later weer importeren zodat de knooppunten de blokken kunnen ondertekenen nadat we onze Blockchain en Wallet gegevens opnieuw hebben geïnitialiseerd.


```
e1-cli dumpprivkey <e1-address>

e2-cli dumpprivkey <e2-address>
```


Nu moeten we generate een Redeem script maken met een 2 van 2 multi-handtekening vereiste. We doen dit door het createmultisig commando te gebruiken en de eerste parameter als 2 door te geven en dan twee publieke sleutels op te geven. Het zijn deze sleutels die Ownership later moet bewijzen wanneer het blok wordt aangemaakt.


Elk knooppunt, e1 of e2, kan generate de Multisig.


```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```


Dat geeft ons onze redeemscript, die je kunt kopiëren voor later gebruik.


Nu moeten we de bestaande Blockchain en Wallet gegevens wissen, zodat we opnieuw kunnen beginnen met de nieuwe signblockscript als onderdeel van de consensusregels van de keten. Daarom moesten we eerder een kopie maken van sommige gegevens, zoals de private sleutels die in de nieuwe keten gebruikt zullen worden om blokken te ondertekenen. U moet dit doen voordat u verder gaat.


Met onze bestaande Wallet en ketengegevens verwijderd, kunnen we nu onze knooppunten starten en ze een nieuwe keten laten initialiseren met behulp van de signblockscript parameter. Laten we -evbparams=dynafed:0:: doorgeven om dynafed activering uit te schakelen, omdat we die geavanceerde functie niet nodig hebben voor dit voorbeeld.


```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::

e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```


Nu moeten we de privésleutels importeren die we eerder hebben opgeslagen, zodat onze nodes kunnen ondertekenen en helpen bij het voltooien van voorgestelde blokken.


```
e1-cli importprivkey <e1-priv-key>

e2-cli importprivkey <e2-priv-key>
```


Het gebruik van het generate commando zou nu een foutmelding moeten geven, omdat het niet voldoet aan de vereiste block signing regels die nu door onze knooppunten worden afgedwongen.


```
e1-cli -generate 1
```


Om een nieuw blok voor te stellen kan elk knooppunt het getnewblockhex commando oproepen. Dit geeft de hex van een nieuw blok dat ondertekend moet worden voordat het door knooppunten op ons netwerk wordt geaccepteerd.


```
e1-cli getnewblockhex
```


Onthoud dat het commando alleen een voorgesteld blok maakt, het generate er geen.


Om dit te bevestigen kunnen we zien dat er momenteel geen blokken zijn in onze Blockchain.


```
e1-cli getblockcount
```


Als we de blok hex proberen in te dienen zonder deze eerst te ondertekenen.


```
e1-cli submitblock <block-hex>
```


We krijgen een melding dat het blokbewijs ongeldig is. Dit komt omdat het nog niet is ondertekend door 2 van de vereiste 2 partijen.


Dus laten we e1 het voorgestelde blok laten ondertekenen.


```
e1-cli signblock <block-hex>
```


Laat e2 de hex ondertekenen.


```
e2-cli signblock <block-hex>
```


Merk op dat e2 de uitvoer die ontstaat door het tekenen van het voorgestelde blok door e1 niet ondertekent. Ze ondertekenen allebei het voorgestelde blok hex onafhankelijk van elkaars resultaten.


Nu moeten we de blokhandtekeningen van e1 en e2 combineren. Elk knooppunt kan dit doen, ze hebben alleen de ondertekende blokhex van het andere knooppunt nodig.


```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```


Je kunt zien dat het combineblocksigs commando de hex van het getekende blok uitvoert, evenals de status complete, die ons vertelt dat de hex van het blok klaar is om verzonden te worden.


Nu kan elk knooppunt het voltooide blok hex indienen. We laten e1 dit doen.


```
e1-cli submitblock <combined-signed-hex>
```


Controleren of de inzending geldig was.


```
e1-cli getblockcount

e2-cli getblockcount
```


Je kunt zien dat zowel e1 als e2 het blok als geldig hebben geaccepteerd en het hebben toegevoegd aan het uiteinde van hun lokale kopieën van de Blockchain.


Om het proces samen te vatten. In deze sectie hebben we:


- Een blok voorgesteld.
- Liet elk knooppunt het ondertekenen.
- De handtekeningen gecombineerd.
- Gecontroleerd of de handtekeningen geldig zijn en voldoen aan de redeemscript drempelwaarde van de keten.
- Het blok ingediend.


Elk knooppunt op het netwerk valideerde het blok en voegde het toe aan hun lokale kopie van de Blockchain.


### block signing


Hoewel het proces in eerste instantie complex lijkt, is de volgorde van block signing in Elements altijd hetzelfde en hoeft de initiële instelling maar één keer te worden uitgevoerd:


1. Eerste installatie (eenmalig uitgevoerd)

2. Een Address met meerdere handtekeningen wordt aangemaakt onder de naam `signblockscript` met behulp van de publieke sleutels van Federated Block Signers.

3. Het Redeem script hiervan wordt gebruikt om een nieuwe Blockchain te starten.

4. Blokproductie (lopend)

5. Voorgestelde blokken worden gegenereerd en uitgewisseld voor ondertekening.


Zodra een drempelaantal ondertekenaars het voorgestelde blok heeft ondertekend, wordt het gecombineerd en ingediend bij het netwerk. Als het voldoet aan de criteria van de `signblockscript` van de keten, accepteren de knooppunten het als een geldig blok.


## Element als zijketen


<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>


:::video id=c15e7eaf-9b5d-4696-bb36-bd10e7b56967:::


Elements is een open-source, algemeen doel Blockchain platform dat ook `gekoppeld` kan worden aan een bestaande Blockchain, zoals Bitcoin. Wanneer Elements gekoppeld is aan een andere Blockchain, wordt gezegd dat het werkt als een `Sidechain`. Sidechains maken de overdracht in twee richtingen mogelijk van activa van de ene keten naar de andere. Door Elements als een Sidechain te implementeren, kun je om enkele van de inherente beperkingen van de mainchain heen werken, terwijl je een goede mate van veiligheid behoudt, die wordt geboden door activa die zijn beveiligd op de mainchain.


Terwijl een Sidechain zich bewust is van de mainchain en zijn transactiegeschiedenis, is de mainchain zich niet bewust van de Sidechain en is er geen nodig voor zijn werking. Hierdoor kunnen sidechains innoveren zonder beperkingen of vertragingen die geassocieerd worden met voorstellen voor verbetering van het mainchain protocol. In plaats van te proberen het direct te veranderen, zorgt het uitbreiden van het hoofdprotocol ervoor dat het mainchain zelf veilig en gespecialiseerd blijft, wat de soepele werking van het Sidechain ondersteunt.


Door de functionaliteit van Bitcoin uit te breiden en gebruik te maken van de onderliggende beveiliging, kan een Sidechain gebaseerd op Elements nieuwe functionaliteit bieden die voorheen niet beschikbaar was voor gebruikers van mainchain. Een voorbeeld van een Sidechain gebaseerd op Elements in productiegebruik is de Liquid Network.


Om een Elements Blockchain te initialiseren als een Sidechain, moeten we de federated peg script parameter gebruiken. Deze parameter kan worden ingesteld in het configuratiebestand van een node of worden doorgegeven bij het opstarten.


De federated peg script definieert welke leden van de Strong Federation peg-in en peg-out functies kunnen uitvoeren. Deze functionarissen worden `watchmen` genoemd, omdat ze de mainchain en Sidechain in de gaten houden voor geldige peg-in en peg-out transacties en actie ondernemen als ze geldig zijn. Pinnen" betekent dat gepinde activa uit de Sidechain naar de mainchain worden verplaatst en "pinnen" betekent dat gepinde activa van de mainchain naar de Sidechain worden verplaatst. Als we zeggen `verplaatsen naar de Sidechain`, bedoelen we eigenlijk dat de fondsen worden vergrendeld in een Address met meerdere handtekeningen op de mainchain en dat een overeenkomstig bedrag aan activa wordt gecreëerd op de Elements Sidechain. Als we zeggen 'uit de Sidechain halen', bedoelen we dat activa worden vernietigd op Elements Sidechain en dat het corresponderende bedrag wordt vrijgegeven van de vergrendelde tegoeden op mainchain. Toestemming om de peg-in en peg-out functies uit te voeren vereist dat functionarissen Ownership bewijzen van de publieke sleutels die in de federated peg script zijn gebruikt. Dit wordt gedaan met behulp van de corresponderende privésleutels.


Om een federated peg script aan te maken, moeten we dus eerst voor elk van onze knooppunten een generate publieke sleutel hebben. We moeten ook de bijbehorende private sleutels opslaan voor later gebruik, omdat we alle bestaande ketengegevens moeten wissen en een nieuwe keten moeten initialiseren met de federated peg script. Dit komt omdat de federated peg script deel uitmaakt van de consensusregels van een Sidechain, en het kan niet worden toegepast op een bestaande, niet-gepaarde, Blockchain op een later tijdstip.


Dus laten we generate een Address maken met elk van onze knooppunten, de relevante gegevens opslaan voor later gebruik en generate de federated peg script die we later zullen gebruiken om onze Sidechain te initialiseren.


Eerst moeten we elk van onze knooppunten, die zullen fungeren als watchmen in ons netwerk, generate een nieuwe Address laten maken.


```
e1-cli getnewaddress

e2-cli getnewaddress
```


Daarna valideren we de Address om de publieke sleutels te verkrijgen.


```
e1-cli getaddressinfo <e1-address>

e2-cli getaddressinfo <e2-address>
```


En dan de privésleutels ophalen die bij elke Address horen.


```
e1-cli dumpprivkey <e1-address>

e2-cli dumpprivkey <e2-address>
```


Sla de private en publieke sleutels op voor later gebruik.


Nu moeten we de bestaande Blockchain en Wallet gegevens wissen, omdat we een nieuwe keten gaan initialiseren met een federated peg script. Je kunt dit nu doen. Vergeet niet de Bitcoin daemon te starten, die we moeten pinnen.


Nu kunnen we een nieuwe keten initialiseren met een federated peg script, gemaakt met de publieke sleutels die we eerder hebben opgeslagen. De getallen die we invoeren en die onze publieke sleutels omringen, definiëren en begrenzen het aantal gebruikte sleutels en de Ownership sleutel die bewezen moet worden om in en uit onze Sidechain te pinnen.


```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae

e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```


Nu importeren we de privésleutels die we eerder hebben opgeslagen, zodat onze knooppunten later de overdracht van activa tussen ketens kunnen ondertekenen en voltooien en voldoen aan de vereisten van federated peg script.


```
e1-cli importprivkey <priv-key-1>

e2-cli importprivkey <priv-key-1>
```


We moeten nu een aantal blokken rijpen op beide ketens. De rijpheid van blokken is een vereiste van het koppelingproces, omdat het beschermt tegen blokherschikkingen op mainchain die leiden tot een [inflatie](https://planb.academy/resources/glossary/inflation) van pegged asset Supply binnen Sidechain.


Om dit hoofdstuk gericht te houden op de federated peg, zullen we blokken genereren zonder gebruik te maken van het block signing model dat we in het vorige hoofdstuk bekeken, en terugkeren naar het gebruik van het 'generate' commando om nieuwe blokken te maken.


```
b-cli generate 101

e1-cli generate 1
```


We hoeven nu niet per se generate blokken te maken voor Elements. Maar laten we er toch één generate maken. Het is een goede gewoonte om mogelijke inconsistenties te vermijden.


Nu is onze ketting klaar om in te pinnen. Om te peg-in moeten we generate een speciaal soort Address genereren met het getpeginaddress commando. Merk op dat de tijd tussen het genereren van een peg-in Address met getpeginaddress en het claimen ervan met claimpegin zo klein mogelijk gehouden moet worden. peg-in adressen zijn niet duurzaam op de lange termijn en moeten niet hergebruikt worden.


```
e1-cli getpeginaddress
```


Je kunt zien dat het commando een nieuwe mainchain Address aanmaakt, evenals een nieuw script dat bevredigd moet worden om de peg-in fondsen op te eisen. De mainchain Address is een `betaal aan script Hash` Address die gebruikt zal worden door functionarissen die de watchmen rol vervullen binnen het Elements netwerk.


Net als getnewaddress, voegt getpeginaddress een nieuw geheim toe aan de Wallet van het aanroepende knooppunt, dus het is belangrijk om een back-up van het Wallet bestand mee te nemen in je knooppuntbeheerproces.


We sturen nu wat Bitcoin van de mainchain naar de Sidechain. Onze mainchain regressietest Wallet bevat al wat geld.


```
b-cli getwalletinfo
```


We zien dat de Wallet 50 Bitcoin kan bevatten. We sturen één Bitcoin van de mainchain naar de Sidechain. We moeten geld sturen naar de mainchain Address die ons knooppunt eerder genereerde.


```
b-cli sendtoaddress <e1-pegin-address>
```


We moeten de ID van deze transactie bewaren omdat we die later nodig hebben als bewijs van financiering.


We kunnen nu zien dat het saldo van mainchain Wallet is afgenomen met het bedrag dat we hebben verzonden, plus een klein extra bedrag om de transactiekosten te dekken.


```
b-cli getwalletinfo
```


We moeten de transactie opnieuw laten rijpen.


```
b-cli generate 101
```


Om onze Elements node de peg-in fondsen te laten claimen, hebben we het `bewijs` nodig dat de peg-in transactie is gedaan. Het cryptografische bewijs gebruikt de financiering transaction ID om het merkelpad te berekenen en bewijst dat de transactie aanwezig is in een bevestigd blok.


```
b-cli gettxoutproof '["<tx-id>"]'
```


We hebben ook de ruwe transactiegegevens nodig.


```
b-cli getrawtransaction <tx-id>
```


Met het bewijs en de onbewerkte gegevens voor de peg-in transactie, kan ons Elements knooppunt nu de peg-in claimen met behulp van de onbewerkte transactie en het transactiebewijs.


```
e1-cli claimpegin <raw> <proof>
```


Merk op dat er een optioneel derde argument is dat we claimpegin hadden kunnen geven. Deze derde parameter kan gebruikt worden om de Sidechain Address op te geven waar het opgeëiste geld naartoe gestuurd moet worden. Dit was in ons voorbeeld niet nodig, omdat we het commando aanroepen vanaf hetzelfde knooppunt dat eigenaar is van de Address waar het opgeëiste geld naartoe gaat.


De balans van e1 controleren.


```
e1-cli getwalletinfo
```


Een blok genereren om de claim te bevestigen.


```
e1-cli generate 1
```


De balans van e1 controleren.


```
e1-cli getwalletinfo
```


We kunnen zien dat de peg-in met succes is geclaimd.


Om te pinnen is het proces vergelijkbaar. Er wordt een Address aangemaakt, geld wordt er naartoe gestuurd en het geld wordt vrijgegeven als de transactie geldig is. We zullen niet het hele peg-out proces behandelen, omdat het werk aan de mainchain inhoudt, wat buiten het bereik van deze cursus valt. De stappen in termen van de Elements gebeurtenissen zijn dat er een Address wordt gegenereerd op de mainchain.


```
b-cli getnewaddress
```


Gelden worden naar de mainchain Address gestuurd vanaf een Elements knooppunt met behulp van het sendtomainchain commando.


```
e1-cli sendtomainchain <new-address> 1
```


Een blok genereren om de transactie te bevestigen.


```
e1-cli generate 1
```


Controleer de balans van de Wallet van het knooppunt.


```
e1-cli getwalletinfo
```


En zie dat het saldo is afgenomen.


In dit gedeelte hebben we gezien hoe:


- generate a federated peg script.
- Initialiseer een nieuwe keten die het script gebruikt als een netwerk consensus parameter regel.
- Stuur geld van de mainchain naar de Sidechain.
- Vorder de fondsen binnen de Elements Sidechain.
- Begrijp hoe het terugsturen van geld naar de mainchain wordt gestart.


### FederatedPegScript



Om Elements als Sidechain te laten werken, moet het [Genesis blok](https://planb.academy/resources/glossary/genesis-block) in zijn Blockchain worden aangemaakt met een `fedpegscript` op zijn plaats. Dit wordt gedaan door bij het opstarten van het knooppunt de `fedpegscript` parameter door te geven. Het script maakt dan deel uit van de consensusregels van Elements Blockchain en zorgt ervoor dat peg-in en peg-out verzoeken gevalideerd en uitgevoerd kunnen worden.


Het `fedpegscript` bestaat uit publieke sleutels die beheerd worden door degenen die geautoriseerd zijn om de peg-acties uit te voeren. Het volgende toont het voorbeeldformaat van een 2-of-2 fedpegscript met meerdere handtekeningen:


```
fedpegscript=5221<public key 1>21<public key 2>52ae
```


Opmerking: De karakters buiten de publieke sleutels zijn scheidingstekens die de publieke sleutel en `n van m` vereisten aangeven. De sjabloon voor een 1-of-1 fedpegscript zou bijvoorbeeld '5121<pub key 1>51ae' zijn.


### Inprikken


Voordat een peg-in kan worden geaccepteerd door een Elements Sidechain, moet deze voldoende bevestigingen hebben op de mainchain. Dit is nodig om inflatie in de Supply van de pegged asset op de Elements Sidechain te voorkomen, die veroorzaakt zou kunnen worden door een reorganisatie van de mainchain.


Korte reorganisaties van het uiteinde van Bitcoin Blockchain worden verwacht als onderdeel van de normale werking van het Proof of Work (PoW) consensusmechanisme. Elements accepteert daarom alleen een peg-in als geldig, wanneer deze voldoende diepte heeft binnen Bitcoin Blockchain. Dit dient om te voorkomen dat Elements dezelfde peg-in meer dan eens accepteert.


### Uitsparing


Een peg-out vindt plaats wanneer een Elements knooppunt het `sendtomainchain` commando oproept, dat als invoer een mainchain Address (de bestemming van de peg-out) en het bedrag van de pegged asset dat moet worden `opgenomen` meeneemt. Dit creëert een peg-out transactie op de Sidechain. Zodra de Functionarissen die als watchmen optreden, zien dat de peg-out transactie op de Sidechain is bevestigd, zorgen zij ervoor dat het activum op de mainchain daadwerkelijk wordt vrijgegeven aan de peg-out bestemming, zoals we in eerdere hoofdstukken van de cursus hebben geleerd.


## Elements als zelfstandige Blockchain


<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>


:::video id=4955306b-4be3-429c-9d30-068f7644ea73:::


Tot nu toe hebben we bekeken hoe Elements als Sidechain gebruikt kan worden. Het kan echter ook werken als een zelfstandige Blockchain oplossing met zijn eigen standaard native asset. In deze opzet behoudt een Elements Blockchain nog steeds alle functies van een Sidechain implementatie, zoals Confidential Transactions en Issued Assets, maar heeft geen peg-in of peg-out nodig om default asset bedragen in omloop te brengen of te verwijderen.


In dit hoofdstuk zullen we:


Initialiseer een nieuwe Elements Blockchain met een default asset met de naam `newasset`.


Geef op dat er 1.000.000 `newasset` moet worden aangemaakt samen met 2 heruitgiftetokens ervoor.


Claim alle anyone-can-spend `newasset` munten.


Claim alle anyone-can-spend heruitgifte tokens voor 'newasset'.


Stuur het object en de reissuance token naar de Wallet van een ander knooppunt.


Geef meer 'newasset' uit beide knooppunten.


Om een Elements netwerk te initialiseren om als zelfstandige Blockchain te werken, moet elk knooppunt gestart worden met een aantal basisparameters. Deze worden gebruikt om het knooppunt te vertellen dat het geen peg-ins van een andere Blockchain mag valideren, de naam van de default asset van het netwerk en de hoeveelheid default asset en bijbehorende reissuance token die aangemaakt moeten worden.


We starten nu een nieuwe keten met deze parameters op onze twee verbonden Elements knooppunten. We noemen de default asset `newasset` en geven er één miljoen van uit en twee `newasset` heruitgiftetokens.


```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000

e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```


Merk op dat de bedragen die hier worden gebruikt in de kleinste denominatie zijn die het netwerk kan accepteren, dus de tweehonderd miljoen heruitgifte tokens zijn eigenlijk gelijk aan twee hele tokens. Hetzelfde geldt voor de waarde van de initiële gratis munten.


Bekijk de huidige Wallet balansen van ons knooppunt.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


We kunnen zien dat de initialisatie correct is verlopen.


Aangezien de initiële uitgifte van activa wordt gecreëerd als `iedereen kan uitgeven`, laten we e1 ze allemaal opeisen zodat we e2's toegang ertoe kunnen verwijderen.


```
e1-cli getnewaddress

e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```


Merk op dat we 'newasset' niet hoeven te specificeren als het te verzenden goed, omdat het al de default asset is. en dus ook de default asset die wordt gebruikt om netwerkkosten te betalen.


Binnen Elements kun je meerdere soorten activa naar dezelfde Address sturen, dus we kunnen de Address die we net hebben gegenereerd om de default asset te ontvangen, opnieuw gebruiken als de bestemmings-Address voor de heruitgifte tokens.


```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```


Bevestig de transacties.


```
e1-cli generate 101
```


We zullen nu controleren of e1 de enige houder is van het actief en zijn reissuance token.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


We zien dat dit inderdaad het geval is.


Nu sturen we een deel van de 'newasset' naar e2, die momenteel een saldo van nul heeft.


```
e2-cli getnewaddress

e1-cli sendtoaddress <e2-address> 500 "" "" false
```


Merk op dat we het type asset dat verzonden moet worden niet hoefden op te geven, omdat `newasset` is aangemaakt als default asset van het netwerk


Laten we ook enkele van de heruitgiftetokens voor `newasset` naar e2 sturen.


```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```


Bevestig de transacties.


```
e1-cli generate 101
```


We kunnen controleren of de portemonnees dienovereenkomstig zijn bijgewerkt.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


Nu zullen we een aantal default asset van e1 opnieuw uitgeven. Merk op dat de mogelijkheid om dit te doen wordt ingeschakeld door de initialreissuancetokens opstartparameter. Als deze wordt weggelaten of op nul wordt gezet, resulteert dit in een default asset die later niet opnieuw kan worden uitgegeven.


```
e1-cli reissueasset newasset 100
```


We konden het label `newasset` gebruiken in plaats van de hex id waarde, omdat een Elements keten altijd zijn default asset labelt.


Controleren of de heruitgave van de default asset werkte:


```
e1-cli generate 101

e1-cli getwalletinfo
```


We zullen nu bewijzen dat omdat e2 een aantal `newasset` heruitgiftetokens bezit, het ook de default asset opnieuw kan uitgeven.


```
e2-cli reissueasset newasset 100
```


Controleren of de heruitgave van de default asset door e2 werkte.


```
e2-cli generate 101

e2-cli getwalletinfo
```


In dit hoofdstuk hebben we de Elements ingesteld als een zelfstandige Blockchain en gecontroleerd of de basisfunctionaliteit werkt zoals we zouden verwachten.


We gebruikten opstartparameters om:


Initialiseer een nieuwe Elements Blockchain met een default asset met de naam 'newasset'.


Geef de hoeveelheid default asset op om on chain initialisatie te creëren.


Maak een aantal heruitgiftetokens voor de default asset en geef meer default asset's uit op beide knooppunten.


Op ons standalone Blockchain Elements netwerk zullen alle andere transactionele operaties op dezelfde manier werken als de voorbeelden die in de hoofdsecties van de cursus behandeld worden, maar ze zullen 'newasset' gebruiken in plaats van `Bitcoin` als het standaard en kosten activum.


### Node-opstart- en keteninitialisatieparameters


Om een Elements node te laten werken als een standalone Blockchain moeten een aantal parameters samen worden gebruikt. We zullen nu naar elke parameter kijken en ontdekken wat ze doen.


#### `validatepegin=0`

Omdat een standalone Blockchain geen peg-in of peg-out transacties hoeft te valideren, moeten we deze controles uitschakelen. Met deze instelling hoeft u de Bitcoin clientsoftware niet uit te voeren of een kopie van de Bitcoin Blockchain op te slaan, aangezien het Elements netwerk onafhankelijk zal werken.


#### `defaultpeggedassetname`

Hiermee kunt u de naam opgeven van de default asset die bij de Blockchain initialisatie wordt aangemaakt.


#### `initiëlevrije munten`

Het aantal (in het equivalent van de Bitcoin's Satoshi eenheid) van de default asset om aan te maken.


#### `initialreissuancetokens`

Het aantal (in het equivalent van Bitcoin's Satoshi eenheid) van de heruitgifte tokens voor de default asset om te maken. Zonder dit is het onmogelijk om meer van de default asset te maken. Als je niet wilt dat er meer default asset's gemaakt kunnen worden, kun je dit op nul zetten of weglaten.


Met behulp van deze parameters zou de common om een knooppunt te starten er ongeveer zo uitzien:


```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```


### Basisbewerkingen


De parameter `defaultpeggedassetname` geeft de default asset een label. Zonder deze instelling krijgt de default asset automatisch de naam `Bitcoin`. In vorige secties, toen we assets die we zelf hadden uitgegeven naar een ander knooppunt stuurden, moesten we of de asset hex of het lokaal toegepaste asset label opgeven om Elements te vertellen welk asset we stuurden. Omdat `defaultpeggedassetname` voor alle knooppunten geldt, hoeven we het geen naam te geven als we het versturen, ook al is de naam niet `Bitcoin`. Elke functie die voorheen standaard `Bitcoin` verstuurde, zal nu versturen als wat je gekozen hebt om de default asset te labelen.


Dus 10 van de nieuwe default asset naar een Address sturen is zo simpel als:


```
e1-cli sendtoaddress <destination address> 10 "" "" true
```


Als je het knooppunt ook hebt voorzien van een waarde voor `initialreissuancetokens` groter dan nul, dan kun je ook meer default asset's opnieuw uitgeven, iets wat niet mogelijk is als je Elements als Sidechain uitvoert.


Om dit te doen hoeft elk knooppunt dat een hoeveelheid token bezit die geassocieerd is met default asset alleen maar een commando in de vorm te geven:


```
e1-cli reissueasset <default asset name> <amount>
```


Door bovenstaande parameters te gebruiken, kun je Elements gebruiken als een zelfstandige Blockchain met een eigen default asset, losgekoppeld van Bitcoin en andere blockchains.


## Conclusie


<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>


:::video id=bd5167d5-edba-40b0-a8b1-ba8b74493a08:::


In deze cursus hebben we geleerd dat Elements een open-source netwerkprotocol is dat geïmplementeerd kan worden als een Sidechain naar een andere Blockchain, of als een zelfstandige Blockchain oplossing.


We hebben gezien dat de broncode en website voor Elements (https://github.com/ElementsProject/Elements) gehost worden op GitHub en dat er community discussieforums zijn, zoals Build On L2(https://community.Liquid.net/c/developers/), of de Liquid Developers Telegram (https://t.me/liquid_devel), die gebruikt kunnen worden om meer te leren over het inzetten en ontwikkelen van toepassingen op Elements en Liquid. Belangrijke functies zoals Confidential Transactions en Issued Assets werden behandeld, samen met hoe leden van een Strong Federation gefedereerde block signing en het 2-Weg Peg mechanisme mogelijk maken.


De volgende stap is om jezelf uit te dagen met een cumulatieve quiz die alle voorgaande secties beslaat, om daarna je Elements reis te beginnen... veel succes!


# Laatste Sectie


<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>


## Beoordelingen


<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusie


<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>

<isCourseConclusion>true</isCourseConclusion>