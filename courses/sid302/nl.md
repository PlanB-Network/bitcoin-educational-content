---
name: Liquid Essentials Bootcamp
goal: Krijg een uitgebreid begrip van het Liquid Network en Elements project en leer hoe je geavanceerde oplossingen kunt implementeren in vertrouwelijke transacties, tokenisatie en gedecentraliseerde netwerkarchitectuur.
objectives: 

  - De grondbeginselen van Liquid architectuur en de relatie met Bitcoin begrijpen.
  - Liquid nodes leren configureren en bedienen met de Elements software.
  - Verken het gebruik van vertrouwelijke transacties en uitgifte van activa op de Liquid Network.
  - Begrijp de zakelijke en technische aspecten van Liquid voor toepassingen in kapitaalmarkten.

---

# Kennismaking met het Liquid netwerk


Ga op een educatieve reis die ontworpen is om een diepgaand begrip te geven van het Liquid Network en Elements project. Dit bootcamp combineert theorie en praktijk om je de technische, architecturale en zakelijke fundamenten te leren die nodig zijn om de mogelijkheden van Liquid te implementeren en te benutten. Van vertrouwelijke transacties tot het ontwerpen van ecosystemen, deze cursus is ideaal voor diegenen die hun kennis van geavanceerde tools binnen het Bitcoin ecosysteem willen uitbreiden.


Met presentaties door industrie-experts behandelt de cursus onderwerpen zoals Liquid architectuur, tokenization toepassingen, technische concepten van Elements, en innovatieve use cases zoals de Breez SDK. Ontworpen om toegankelijk te zijn voor beginners en gevorderde gebruikers, biedt de cursus ook waarde voor ervaren ontwikkelaars die Liquid onder de knie willen krijgen als platform voor het optimaliseren van hun projecten.

+++

# Inleiding


<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>


## Cursusoverzicht


<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>


Welkom bij het Liquid Bootcamp, een uitgebreide training ontworpen om u uit te rusten met de kennis en vaardigheden om effectief gebruik te maken van het Liquid Network en Elements project. Deze cursus biedt een uitgebreide verkenning van de onderscheidende kenmerken van Liquid, waaronder Confidential Transactions, uitgifte van activa en de federatieve netwerkarchitectuur, terwijl ook de basisconcepten van Elements, de software die Liquid aanstuurt, worden geïntroduceerd.


Tijdens de bootcamp verken je de praktische toepassingen van de Liquid Network, van het opzetten en bedienen van nodes tot het begrijpen van het gebruik in de Bitcoin kapitaalmarkten en tokenisatie. Met presentaties van industrie-experts krijg je ook inzicht in geavanceerde onderwerpen zoals HTLC's, de Breez SDK en het Blockstream AMP-project.


Dit bootcamp werd oorspronkelijk uitgevoerd als een in-person evenement, volgens een gestructureerd schema (zoals te zien in de afbeelding) dat is ontworpen voor live sessies. Voor deze aanpassing van de cursus is de inhoud echter gereorganiseerd om beter te passen bij een online format en het begrip door studenten te vergemakkelijken. De nieuwe volgorde zorgt voor een logische progressie van basisconcepten naar meer geavanceerde en technische onderwerpen, waardoor de leerervaring wordt gemaximaliseerd.


Deze reis is gestructureerd om deelnemers met verschillende expertiseniveaus tegemoet te komen en biedt een mix van theoretische kennis en praktijkervaring. Aan het einde van deze bootcamp heeft u een goed begrip van de architectuur van Liquid, de integratie met Bitcoin en hoe u de innovatieve functies kunt gebruiken om financiële oplossingen te bouwen en te optimaliseren.


Duik in de wereld van de Liquid sidechain en ontketen nu zijn volledige potentieel!

# Grondbeginselen


<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>


## Liquid Architectuur


<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>


:::video id=ff6899d2-b47f-4c3d-983d-3bd66d2be59d:::

### Liquid Network Architectuur en Consensusmodel


De Liquid Network is een gefedereerde sidechain gebouwd op de Elements codebase, ontworpen om de mogelijkheden van Bitcoin uit te breiden terwijl het vertrouwt op zijn fundamentele veiligheid. In tegenstelling tot Bitcoin's [Proof-of-Work](https://planb.academy/resources/glossary/proof-of-work), werkt Liquid op een Federated [Consensus](https://planb.academy/resources/glossary/consensus) model. Het netwerk wordt onderhouden door een wereldwijd verspreide groep leden, waaronder beurzen, handelsdesks en infrastructuuraanbieders. Uit deze leden worden vijftien "functionarissen" geselecteerd om op te treden als blokondertekenaars.


Deze functionarissen produceren blokken op een deterministische round-robin manier, waarbij elke minuut een nieuw [blok](https://planb.academy/resources/glossary/block) wordt gegenereerd. Deze precieze timing staat in contrast met de probabilistische tien-minuten-intervallen van Bitcoin. Om een blok geldig te laten zijn, zijn handtekeningen nodig van minstens 11 van de 15 functionarissen (een drempel van tweederde plus één). Dit mechanisme geeft Liquid "twee-blokken finaliteit", wat betekent dat zodra een [transactie](https://planb.academy/resources/glossary/transaction-tx) twee bevestigingen heeft (ongeveer twee minuten), het mathematisch onmogelijk is om de keten te reorganiseren. Deze snelheid en zekerheid zijn cruciaal voor arbitrage, geautomatiseerde handel en snelle vereffening tussen beurzen.


De federatie is dynamisch. Via het Dynamic Federation (Dynafed) protocol kan het netwerk functionarissen roteren of parameters bijwerken zonder dat er een [harde fork](https://planb.academy/resources/glossary/fork) nodig is. Hierdoor kan het systeem naadloos evolueren en hardware of leden vervangen met behoud van continue werking.


### Confidential Transactions en vermogensbeheer


Een bepalende eigenschap van Liquid is de ondersteuning voor Confidential Transactions (CT) en meerdere activa. Op de hoofdketen van Bitcoin zijn alle transactiedetails - verzender, ontvanger en bedrag - openbaar. In Liquid gebruikt CT cryptografische verplichtingen om het type activa en het bedrag te verbergen voor het openbare grootboek, terwijl het netwerk nog steeds kan verifiëren dat de transactie geldig is (d.w.z. dat er geen [inflatie](https://planb.academy/resources/glossary/inflation) heeft plaatsgevonden). Alleen de deelnemers met de verblindsleutels kunnen de specifieke waarden zien, wat een niveau van commerciële privacy biedt dat essentieel is voor instellingen die grote posities verplaatsen.


Liquid behandelt alle activa als "native" burgers van de [blockchain](https://planb.academy/resources/glossary/blockchain). Dit omvat Liquid Bitcoin (LBTC), stablecoins zoals USDT en veiligheidstokens. Voor de uitgifte van activa zijn geen complexe smart contracts nodig; het is een basisfunctie van het protocol.


#### Gereguleerde activa en AMP

Voor activa die compliance vereisen, zoals veiligheidstokens, gebruikt Liquid het Blockstream Asset Management Platform (AMP). Dit introduceert een toestemmingslaag waarbij transacties een tweede handtekening van een autorisatieserver vereisen. Dit stelt emittenten in staat om regels af te dwingen, zoals whitelisting of KYC-vereisten, op een granulair niveau, waarbij de efficiëntie van een blockchain wordt gecombineerd met de regelgevende controles van de traditionele financiële sector.


### De tweerichtingscommunicatie- en beveiligingsinfrastructuur


De verbinding tussen Liquid en Bitcoin wordt onderhouden door een tweewegkoppeling. Om te "pinnen", stuurt een gebruiker Bitcoin naar een gegenereerd adres op mainchain. Deze fondsen worden gedurende 102 bevestigingen (ruwweg 17 uur) vergrendeld om risico's van reorganisatie uit te sluiten. Eenmaal bevestigd, wordt een gelijkwaardige hoeveelheid LBTC geslagen op de Liquid sidechain.


Het "peg-out" proces stelt gebruikers in staat om LBTC in te wisselen voor Bitcoin. Hiervoor is het verbranden van LBTC en een cryptografische autorisatie van de federatie vereist. Om diefstal te voorkomen, worden peg-outs strikt gecontroleerd door Peg-out Authorization Keys (PAK's) die in het bezit zijn van federatieleden. Daarnaast kunnen fondsen direct worden geswapt via derde partijen zoals SideSwap, waarbij de settlement vertraging wordt omzeild voor snellere liquiditeit.


#### Hardwarebeveiligingsmodules (HSM's)

Beveiliging wordt strikt door hardware afgedwongen. Functionarissen bewaren geen [privésleutels](https://planb.academy/resources/glossary/private-key) op standaardservers, maar gebruiken Hardware Security Modules (HSM's). Deze apparaten zijn air-gapped van de logica van de hostserver en zijn geprogrammeerd met strikte regels. Een HSM zal bijvoorbeeld weigeren om een blok te ondertekenen als de hoogte niet groter is dan de vorige, waardoor herschrijven van de geschiedenis wordt voorkomen. Dit "vijandige" beveiligingsmodel gaat ervan uit dat de hostserver gecompromitteerd kan worden, waardoor de sleutels veilig blijven, zelfs als de fysieke locatie wordt gekraakt.


## Grondbeginselen van Elements


<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>


:::video id=5652dcb2-4303-484c-8be5-d98063b39c1c:::

### Elements: De fundering van Liquid


Elements is een open-source, blockchain platform afgeleid van de Bitcoin Core codebase. Het breidt de functionaliteit van Bitcoin uit door sidechains-onafhankelijke blockchains mogelijk te maken, die activa van en naar Bitcoin kunnen overbrengen. Terwijl Bitcoin Core het Bitcoin netwerk aandrijft, is Elements de software engine achter Liquid Network en andere aangepaste sidechains.


De relatie is duidelijk: Liquid is een specifieke "instantie" van een Elements zijketen, geconfigureerd voor productiegebruik met een gefedereerd consensusmodel. Ontwikkelaars die bekend zijn met Bitcoin zullen Elements intuïtief vinden, omdat het dezelfde RPC (Remote Procedure Call) interface en commandoregelstructuur behoudt (`elements-cli`, `elements-d`, `elements-qt`). Het belangrijkste verschil zit in de configuratie: door `chain=liquidv1` in te stellen wordt een node verbonden met het hoofdnetwerk Liquid, terwijl `chain=elementsregtest` een lokale regressietestomgeving opstart waar ontwikkelaars generate blokken direct kunnen testen zonder externe afhankelijkheden.


#### Uitgifte van activa

Een opvallend kenmerk van Elements is de uitgifte van eigen activa. In tegenstelling tot Ethereum, waar tokens complexe slimme contracten zijn, zijn activa in Elements eersteklas burgers die gecreëerd worden via een eenvoudig RPC commando (`issueasset`).


- Unieke identificatie:** Elk onderdeel krijgt een unieke hexadecimale ID van 64 tekens.
- Reissuance Tokens:** Uitgevers kunnen optioneel reissuance tokens aanmaken, die de houder het recht geven om later meer van het activum te slaan (nuttig voor stablecoins of security tokens).
- Activa Register:** Omdat hex ID's niet menselijk leesbaar zijn, brengt het Blockstream activa register deze ID's in kaart in namen en tickers (bijvoorbeeld "USDT"), vergelijkbaar met een DNS voor activa.


### Privacy via Confidential Transactions


Elements pakt een van de belangrijkste beperkingen van openbare blockchains aan: het gebrek aan commerciële privacy. Op Bitcoin is elk transactiebedrag zichtbaar voor de wereld. Elements introduceert **Confidential Transactions (CT)**, die het bedrag en het type activa cryptografisch verbergt, terwijl het netwerk nog steeds de geldigheid van de transactie kan verifiëren.


Dit wordt bereikt met **Pedersen Commitments** en **Range Proofs**.


- Pedersen Commitments** vervangen het zichtbare bedrag door een cryptografische verbintenis. Dankzij homomorfe codering kunnen validators controleren of *Input Commitments = Output Commitments + Fees* zonder ooit de werkelijke waarden te zien.
- Range Proofs** voorkomen dat een gebruiker uit het niets geld creëert (bijvoorbeeld door negatieve getallen te gebruiken) door wiskundig te bewijzen dat de verborgen waarde een positief geheel getal is binnen een geldig bereik.


Voor een buitenstaander toont een Vertrouwelijke Transactie geldige invoer en uitvoer, maar wordt *wat* er wordt verzonden en *hoeveel* verborgen. Alleen de verzender en ontvanger (die de vercijferingssleutels bezitten) kunnen de gegevens in klare tekst zien.


### Ontwikkeling en RPC-workflow


Interactie met een Elements knooppunt gebeurt voornamelijk via de JSON-RPC interface. Hierdoor kunnen applicaties geschreven in Python, JavaScript of Go communiceren met de blockchain.



- Setup:** Een ontwikkelaar start meestal in de `regtest` modus. Dit maakt het mogelijk om direct blokken te genereren (`generateblock`) om transacties onmiddellijk te bevestigen, waarbij de bloktijd van 1 minuut van het live netwerk wordt omzeild.
- Commando's:** Standaard Bitcoin commando's zoals `getblockchaininfo` zijn beschikbaar, naast Elements-specifieke commando's zoals `dumpblindingkey` (voor het controleren van CT's) of `pegin` (voor het verplaatsen van BTC naar de sidechain).
- Aliassen:** Om meerdere [nodes](https://planb.academy/resources/glossary/node) te beheren (bijvoorbeeld een "zender" en "ontvanger" voor testen), gebruiken ontwikkelaars vaak shell aliassen zoals `e1-cli` en `e2-cli` die naar verschillende gegevensmappen wijzen, waarmee een [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p) netwerk op een enkele machine wordt gesimuleerd.


Deze architectuur stelt ontwikkelaars in staat om geavanceerde financiële toepassingen te bouwen, zoals effectenplatforms of privégateways voor betalingen, met behulp van de robuuste en vertrouwde tools van het Bitcoin ecosysteem.


## Bitcoin lagen verbinden


<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>


:::video id=31368c02-b979-44d7-b217-ceed96c7ca5c:::

### Dwars-Layer-infrastructuur en HTLC's


Het Bitcoin ecosysteem heeft zich ontwikkeld tot een architectuur met meerdere lagen, waarbij de Mainchain voor afwikkeling zorgt, Lightning voor snelheid en Liquid voor geavanceerde vermogensmogelijkheden. Het verplaatsen van waarde tussen deze lagen zonder gecentraliseerde tussenpersonen vereist een cryptografische primitieve zonder vertrouwen: [Hash](https://planb.academy/resources/glossary/hash-function) Time Locked Contract ([HTLC](https://planb.academy/resources/glossary/htlc)).


Een HTLC creëert een voorwaardelijk [betalingskanaal](https://planb.academy/resources/glossary/payment-channel) dat onafhankelijke systemen atomisch verbindt. Het functioneert via twee primaire beperkingen: een **hash lock** en een **time lock**.


- Het Hash slot:** Gelden kunnen direct worden uitgegeven als de ontvanger een geheime "preimage" onthult die overeenkomt met een specifieke cryptografische hash.
- Het tijdslot:** Als de ontvanger het geheim niet binnen een bepaalde tijd (blokhoogte) onthult, kan de oorspronkelijke verzender het geld terugvorderen.


Deze dual-path structuur zorgt voor veiligheid. Bij een cross-layer swap wordt hetzelfde hashslot gebruikt op beide netwerken. Wanneer de ontvanger het geheim onthult om geld op te eisen op de ene laag (bijv. Liquid), wordt dat geheim zichtbaar voor de verzender, die het vervolgens kan gebruiken om het wederkerige geld op te eisen op de andere laag (bijv. Lightning). Deze cryptografische binding garandeert dat de ruil voor beide partijen succesvol verloopt of voor beide partijen mislukt, waardoor het risico dat de ene partij geld verliest terwijl de andere het ontvangt, wordt geëlimineerd.


### De Taproot en MuSig2 upgrade


Oude HTLC's ([SegWit](https://planb.academy/resources/glossary/segwit) v0) functioneerden goed, maar hadden nadelen op het gebied van privacy en efficiëntie. Ze vereisten het publiceren van de volledige [scriptlogica](https://planb.academy/resources/glossary/script) on-chain, waardoor swaptransacties gemakkelijk identificeerbaar waren voor blockchainanalisten en duurder waren vanwege de datagrootte. De introductie van [Taproot](https://planb.academy/resources/glossary/taproot) (SegWit v1) en het MuSig2 protocol heeft deze architectuur gerevolutioneerd.


Taproot maakt **Key Aggregation** mogelijk via MuSig2. In plaats van een complex script met meerdere [publieke sleutels](https://planb.academy/resources/glossary/public-key) te onthullen, laat MuSig2 de swapdeelnemers hun sleutels combineren in een enkele geaggregeerde publieke sleutel.


- Coöperatief "Sleutelpad":** Als beide partijen akkoord gaan met de ruil (het "gelukkige pad"), ondertekenen ze de transactie mede. Voor het netwerk ziet dit er identiek uit als een standaard betaling met één handtekening. Het verbruikt minimale blokruimte en onthult absoluut geen informatie over de ruilvoorwaarden.
- Adversarial "Script Path":** Als een partij niet meer reageert of kwaadwillend is, wordt het onderliggende script (dat de hash/tijdsloten bevat) alleen dan onthuld. Dit is georganiseerd in een [Merkle-boom](https://planb.academy/resources/glossary/merkle-tree), waardoor de eerlijke partij alleen de specifieke tak onthult die nodig is om geld terug te krijgen en de rest van de contractlogica verborgen blijft.


### Praktische implementatie: Liquid Bliksem Wissels


In de praktijk maken deze protocollen een naadloze uitwisseling tussen de Bitcoin lagen mogelijk. Een typische Liquid-naar-Lightning swap begint met een cliënt die een swap aanvraagt bij een dienstverlener. De cliënt levert een [Lightning-factuur](https://planb.academy/resources/glossary/invoice-lightning) en de provider vergrendelt de equivalente Bitcoin1 (L-BTC) in een Taproot HTLC adres.


De atomiciteit wordt afgedwongen wanneer de betaling wordt vereffend. Om de L-BTC te claimen, moet de dienstverlener het preimage hebben. Ze krijgen dit preimage alleen wanneer ze de Lightning-factuur van de klant met succes betalen. Op het moment dat de Lightning betaling is afgerond, wordt het preimage onthuld, waardoor de dienstverlener de Liquid fondsen kan ontgrendelen.


#### Wallet abstractie en UTXO beheer

Voor eindgebruikers is deze complexiteit volledig geabstraheerd. Moderne [wallets](https://planb.academy/resources/glossary/wallet) zoals Aqua handelen het genereren van sleutels, het aanmaken van facturen en het ondertekenen af op de achtergrond. De gebruiker "betaalt" gewoon een Lightning-factuur met zijn Liquid saldo. Achter de schermen beheert de service de [UTXO](https://planb.academy/resources/glossary/utxo) consolidatie, waarbij kleine, niet-opgeëiste of terugbetaalde uitgangen periodiek worden opgeveegd om de wallet efficiëntie te behouden en de impact op de kosten tijdens drukke periodes te minimaliseren.


## Liquid Network Overzicht


<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>


:::video id=0bac0a62-90f2-41da-ac7c-330c0604bc61:::

### Liquid Network Architectuur en consensus


De Liquid Network werkt als een gefedereerde zijketen, gebouwd op de **Elements** codebase. Terwijl Elements - een fork van Bitcoin Core - de softwarebasis levert, is Liquid de implementatie van het productienetwerk. In tegenstelling tot Bitcoin's Proof-of-Work, die vertrouwt op concurrerend [mining](https://planb.academy/resources/glossary/mining), gebruikt Liquid een **Federated Consensus** model.


Het netwerk wordt onderhouden door vijftien wereldwijd verspreide "functionarissen" Deze entiteiten beheren gespecialiseerde servers die twee cruciale rollen vervullen:

1.  **Blokproductie:** Functionarissen maken om beurten blokken in een deterministisch round-robin schema, waarbij precies elke minuut een nieuw blok wordt gegenereerd.

2.  **Blok ondertekenen:** Een blok is pas geldig als het door minstens 11 van de 15 functionarissen is ondertekend.


Deze 11-of-15 drempel zorgt ervoor dat het netwerk het falen van maximaal vier knooppunten kan verdragen zonder te stoppen. Het primaire voordeel van deze afweging is **deterministische finaliteit**. Terwijl Bitcoin handelt in waarschijnlijkheden, bereikt Liquid afwikkelingszekerheid na twee blokken (ongeveer twee minuten). Zodra een blok een enkele bevestiging heeft, kan de keten niet meer gereorganiseerd worden, waardoor het zeer effectief is voor arbitrage en snelle vereffening.


### Confidential Transactions en inheemse activa


Liquid kenmerkt zich door het standaard gebruik van **Confidential Transactions (CT)**. Op Bitcoin mainchain zijn de afzender, ontvanger en het bedrag openbaar. Liquid verbetert dit door het bedrag en het activatype cryptografisch te verbergen, terwijl het adres van de verzender en ontvanger zichtbaar blijven voor verificatie.


Om ervoor te zorgen dat een gebruiker geen geld kan drukken (bijvoorbeeld door negatieve bedragen te sturen), gebruikt Liquid **Pedersen Commitments** en **Range Proofs**. Met deze cryptografische primitieven kan het netwerk verifiëren dat *Inputs = Outputs + Fees* en dat alle waarden positieve gehele getallen zijn, zonder ooit de specifieke getallen aan het openbare grootboek te onthullen. Alleen de deelnemers met de vercijferingssleutels kunnen de ontcijferde gegevens bekijken.


#### Uitgifte van activa

Liquid behandelt alle activa als "native" Of het nu Liquid Bitcoin (L-BTC) is, een stablecoin zoals USDT, of een waardepapier token, ze delen allemaal dezelfde architectuur. Voor de uitgifte van een activum zijn geen slimme contracten nodig, alleen een eenvoudige RPC oproep.


- Ongereguleerde activa:** Kunnen door iedereen zonder toestemming worden uitgegeven.
- Gereguleerde activa:** Met behulp van het Blockstream Asset Management Platform (AMP) kunnen emittenten naleving van regels afdwingen (zoals KYC/AML) door een tweede handtekening van een autorisatieserver te vereisen voordat een activum kan worden verplaatst.


### De Two-Way Peg en Dynamische Federatie


De brug tussen Bitcoin en Liquid is de **Two-Way Peg**. Hiermee kunnen gebruikers BTC verplaatsen naar de zijketen (Peg-in) en terug naar de mainchain (Peg-out).


**Het pinnen:**

Dit is zonder toestemming. Een gebruiker stuurt BTC naar een door de federatie gecontroleerd adres. Om te beschermen tegen Bitcoin blockchain reorganisaties, moeten deze fondsen wachten op **102 bevestigingen** (ongeveer 17 uur) voordat de equivalente L-BTC wordt geslagen op de sidechain.


**Het uitknijpproces:**

Om terug te keren naar Bitcoin, wordt L-BTC verbrand. Om diefstal van de onderliggende Bitcoin reserves te voorkomen, zijn peg-outs echter niet volledig geautomatiseerd. Ze vereisen toestemming van een lid met een **Peg-Out Authorization Key (PAK)**. De Bitcoin fondsen zelf zijn beveiligd in een 11-of-15 wallet met meerdere handtekeningen, met sleutels in Hardware Security Modules (HSM's) die air-gapped zijn van de hoofdservers van de functionarissen.


**Dynamische Federatie (Dynafed):**

Om een lange levensduur te garanderen, maakt Liquid gebruik van Dynafed, een protocol dat het netwerk in staat stelt om functionarissen te roteren of parameters bij te werken zonder dat er een harde fork nodig is. Als een functionaris moet worden vervangen, zendt het netwerk een overgangstransactie uit. Na een overlapperiode van twee weken neemt de nieuwe configuratie het over, waardoor de federatie naadloos kan evolueren met behoud van continue uptime.


## Ecosysteem en kapitaalmarkten


<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>


:::video id=07e0b82f-2d60-4eb3-9b5d-2ccb7ad06e8a:::

### Liquid Network: Bedrijfsstrategie en ecosysteem


Liquid is meer dan een technische sidechain; het is een bedrijfsgerichte infrastructuurlaag die ontworpen is om de complexe vereisten van kapitaalmarkten aan te kunnen die Bitcoin mainchain niet efficiënt kan ondersteunen. Terwijl [Lightning Network](https://planb.academy/resources/glossary/lightning-network) geoptimaliseerd is voor hoogfrequente betalingen met een lage waarde, richt Liquid zich op overdrachten met een hoge waarde, uitgifte van activa en settlement tussen beurzen.


Het ecosysteem wordt aangestuurd door de **Liquid Federation**, een consortium van ~73 bedrijven, waaronder beurzen, handelsdesks en infrastructuurleveranciers. Dit samenwerkingsmodel weerspiegelt de traditionele financiële clearinghouses, maar werkt met een grotere transparantie en aanzienlijk kortere afwikkelingstijden (2 minuten vs T+2 dagen).


### De tokenisering van real-world activa (RWA)


De kern van de business case voor Liquid is "Tokenization" - het vertegenwoordigen van echte waarde (aandelen, obligaties, mining contracten) als digitale tokens op de blockchain. Dit biedt drie primaire voordelen:

1.  **24/7 Global Markets:** Opheffing van bankuren en geografische beperkingen.

2.  **Operationele efficiëntie:** Het elimineren van afstemmingsfouten door middel van een gedeeld, onveranderlijk grootboek.

3.  **Atomic Settlement:** Vermindert het tegenpartijrisico door ervoor te zorgen dat de levering gelijktijdig met de betaling plaatsvindt.


#### Gereguleerde activa en AMP

De meeste institutionele activa kunnen niet rechtenvrij worden verhandeld vanwege wettelijke vereisten. Het **Asset Management Platform (AMP)** is de technische standaard die deze regels afdwingt.


- Whitelisting:** Emittenten kunnen het aanhouden en verhandelen beperken tot KYC-gecontroleerde adressen.
- Multisig Controle:** Nalevingsacties (zoals het bevriezen van gestolen geld of het opnieuw uitgeven van verloren tokens) worden beheerd via autorisatie met meerdere handtekeningen, zodat geen enkele werknemer eenzijdig kan handelen.


Deze infrastructuur is vandaag live. Platforms zoals **Stalker** bieden end-to-end tokenization diensten in Europa, terwijl **Sideswap** fungeert als een gedecentraliseerde beurs en niet-custodial wallet, waardoor peer-to-peer handel in activa zoals de **Blockstream Mining Note (BMN)** en tokenized MicroStrategy aandelen (CMSTR) mogelijk wordt.


### Succes in de echte wereld: De Mayfell Praktijkstudie


Het meest overtuigende bewijs van het nut van Liquid komt van **Mayfell** in Mexico. In een markt waar traditionele financiering afhankelijk is van papieren promesses, die gevoelig zijn voor verlies, fraude en trage verwerking, schakelde Mayfell de hele infrastructuur over op Liquid.



- Omvang:** Meer dan 25.000 uitgegeven promesses, goed voor **$1,5 miljard** aan waarde.
- Privacy:** Door Liquid's Confidential Transactions te gebruiken, zijn de leenbedragen alleen zichtbaar voor de kredietverstrekker en kredietnemer, waardoor de commerciële privacy behouden blijft en auditors de integriteit van het grootboek kunnen controleren.
- Impact:** Door niet-bancaire kredietverstrekkers te verbinden met wereldwijde kapitaalmarkten via blockchain, verlaagde Mayfell de kosten en werd de toegang tot krediet voor Mexicaanse KMO's vergroot, wat aantoont dat Liquid's waardepropositie veel verder gaat dan speculatieve handel.


### Strategische positionering vs. andere ketens


Liquid concurreert in een overvolle markt van tokenisatieplatforms (Ethereum, Solana, etc.), maar het heeft duidelijke strategische voordelen:


- Duidelijkheid over regelgeving:** Liquid gebruikt Bitcoin (L-BTC) als zijn eigen activa. Het heeft geen voorgedolven token of een ICO, waardoor de risico's van "ongeregistreerde waardepapieren" die andere L1 blockchains plagen, worden vermeden.
- Stabiliteit:** In tegenstelling tot het accountmodel van Ethereum waar mislukte transacties nog steeds gas kosten, is het Liquid model deterministisch en betrouwbaar voor bedrijfskritische financiële gegevens.
- Privacy:** Standaard vertrouwelijkheid is een vereiste voor de meeste financiële instellingen, een functie die Liquid van nature biedt en die publieke ketens moeilijk kunnen implementeren zonder complexe add-ons.


Voor ontwikkelaars biedt dit ecosysteem een duidelijke kans: het bouwen van de tools (dashboards, wallets, compliance-integraties) die een brug slaan tussen traditionele financiën en de veilige afwikkelingslaag van Bitcoin.


## Blokstroom AMP


<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>


:::video id=f00822b4-dc1a-46ff-adfc-ff7c97a0024d:::

### Blockstream AMP: Toegelaten activabeheer op Liquid


Blockstream AMP (Asset Management Platform) dient als een kritieke infrastructuurlaag op de Liquid Network, speciaal ontworpen voor uitgevers van gereguleerde digitale effecten en stablecoins. Terwijl de Liquid een toestemmingsvrije basislaag biedt met native uitgifte van activa, hebben gereguleerde entiteiten vaak strikt toezicht en nalevingsmogelijkheden nodig. AMP overbrugt deze kloof door een toestemmingsvrije controlelaag over specifieke activa te introduceren zonder de privacyvoordelen van Confidential Transactions van Liquid op te offeren.


De kern van de waardepropositie van het platform berust op twee primaire mogelijkheden: uitgebreide zichtbaarheid voor de emittent en autorisatie van transacties. In tegenstelling tot standaard Liquid activa waar bedragen en typen blinded voor iedereen zichtbaar zijn behalve voor de deelnemers, stellen AMP-activa de emittent in staat om een volledig unblinded controlespoor bij te houden. Deze transparantie is essentieel voor regelgevingsrapportage en interne audits. Bovendien dwingt AMP een strikt autorisatiemodel af via een medeondertekeningsmechanisme. Elke overdracht van een AMP-activa vereist een handtekening van de AMP-server. Hierdoor kunnen emittenten complexe regels off-chain afdwingen, zoals het bevriezen van accounts, het goedkeuren van geaccrediteerde investeerders of het opleggen van transferlimieten.


#### Operationele afwegingen

Deze architectuur introduceert specifieke compromissen. Het systeem is afhankelijk van de beschikbaarheid van de AMP-server; als de server als medeondertekenaar optreedt en offline gaat, wordt de liquiditeit van activa onderbroken. Bovendien, terwijl de privacy van gebruiker tot gebruiker behouden blijft, moeten beleggers accepteren dat de uitgever volledig inzicht heeft in hun bezit. Dit model is ideaal voor security tokens die aan de regels voldoen, maar ongeschikt voor censuurbestendige [cryptocurrencies](https://planb.academy/resources/glossary/cryptocurrency).


### Evolutie van architectuur en integratietrajecten


Het AMP ecosysteem is momenteel bezig met de overgang van de eerste iteratie naar een meer flexibele, interoperabele "Versie 2" architectuur. Het oude systeem vereiste van emittenten dat ze volledig gesynchroniseerde Elements nodes onderhielden en dwong ontwikkelaars om sterk te vertrouwen op de monolithische Green SDK. Hoewel dit functioneel was, zorgde het voor hoge technische toetredingsdrempels en beperkte wallet keuzemogelijkheden.


De volgende generatie architectuur vereenvoudigt deze vereisten fundamenteel door de complexiteit naar de server te verschuiven. In dit nieuwe model zorgt de AMP-server voor het zware werk van transactieconstructie, UTXO selectie en kostenberekening. Hij presenteert de emittent een Gedeeltelijk Ondertekende Elements Transactie (PSET) waarvoor alleen een handtekening nodig is. Deze "slimme server, domme wallet" benadering elimineert de noodzaak voor emittenten om volledige nodes te draaien en maakt het gebruik van hardware wallets en standaard multihandtekening setups voor treasury management mogelijk.


Voor ontwikkelaars betekent deze evolutie dat ze overstappen van propriëtaire SDK's naar standaard descriptors en PSET-workflows. Portefeuilles kunnen nu multisignature descriptors registreren bij de AMP-server om autorisatierechten vast te stellen. Dit brengt AMP-ontwikkeling op één lijn met bredere Bitcoin wallet standaarden, waardoor integratie toegankelijk wordt voor elke applicatie die PSBT/PSET formaten kan verwerken. Ontwikkelaars die vandaag bouwen, worden aangemoedigd om tools zoals de Liquid Wallet Kit (LWK) te gebruiken, die deze moderne, descriptor-gebaseerde architecturen ondersteunt, zodat hun toepassingen klaar zijn voor de nieuwe AMP-standaarden.


### Het Liquid Wallet ecosysteem en vertrouwelijkheid


Het bouwen van toepassingen op Liquid vereist het navigeren door een complexere stack dan standaard Bitcoin ontwikkeling vanwege functies zoals native assets en Confidential Transactions. Het ecosysteem wordt ondersteund door een gelaagde architectuur: bibliotheken op laag niveau zoals `secp256k1-zkp` handelen cryptografische primitieven af, terwijl toolkits op hoger niveau de wallet logica beheren.


Historisch gezien bood de Green Ontwikkelingskit (GDK) een uitgebreide maar starre oplossing. Het moderne alternatief is de Liquid Wallet Kit (LWK), die een modulaire aanpak biedt. LWK scheidt zorgen in verschillende kratten en behandelt onafhankelijk descriptors, ondertekening en hardware communicatie, wat ontwikkelaars de flexibiliteit geeft om aangepaste oplossingen te bouwen zonder de overhead van een monolithische bibliotheek.


#### Omgaan met Confidential Transactions

De grootste uitdaging in dit ecosysteem is het beheren van de levenscyclus van de blindering. In Liquid worden transactie-uitgangen versleuteld met behulp van Elliptic Curve Diffie-Hellman (ECDH) sleuteluitwisseling. Een verzender gebruikt de publieke vercijferingssleutel van de ontvanger om bedragen en soorten activa te versleutelen, waardoor een bewijs van de reikwijdte wordt gegenereerd dat de geldigheid van de transactie verifieert zonder waarden te onthullen.


Om te kunnen functioneren, moet een wallet dit proces succesvol omkeren. Wanneer een wallet een inkomende transactie detecteert, probeert hij de uitgang te ontsleutelen met behulp van zijn privé-blindsleutel. Als het gedeelde geheim overeenkomt, kan de wallet de waarde ontcijferen en toevoegen aan het saldo van de gebruiker. Dit proces is rekenintensief en vereist nauwkeurig beheer van verblindingsfactoren om ervoor te zorgen dat transacties wiskundig in balans zijn, een complexiteit die tools zoals LWK proberen weg te abstraheren voor de ontwikkelaar.


# Technisch


<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>

<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>


## Breez SDK - Nodeloos


<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>


:::video id=1a6289b5-fdae-4320-b5b1-41925150108c:::

### Inleiding tot Breez Liquid SDK


De Breez Liquid SDK is een zelfcustodiale, open-source toolkit ontworpen om de kloof tussen de Liquid Network en het bredere Bitcoin ecosysteem te overbruggen. De primaire missie is om de complexiteit van Lightning Network node management en atomic swaps te abstraheren, zodat ontwikkelaars wrijvingsloze financiële toepassingen kunnen bouwen.


Gebouwd met een "mobile-first" filosofie, is de kernlogica geschreven in Rust voor prestaties en veiligheid, maar het maakt gebruik van UniFFI (Unified Foreign Function Interface) om native bindingen te bieden voor Kotlin, Swift, Python, C#, Dart en Flutter. Dit zorgt ervoor dat ontwikkelaars Bitcoin functionaliteit kunnen integreren in hun voorkeursomgeving zonder dat ze cryptografische operaties op laag niveau hoeven te beheren.


**Ondersteunde transactietypen:**

De SDK werkt met Liquid als "thuisbasis" Het blinkt uit in drie specifieke operaties:

1.  **Liquid-naar-Liquid:** Directe on-chain overdracht.

2.  **Liquid-naar-Lightning:** Facturen van Lightning betalen met Liquid-middelen.

3.  **Liquid-naar-Bitcoin:** Geld rechtstreeks omwisselen naar de Bitcoin mainchain.


*Opmerking: De SDK ondersteunt geen directe Lightning-naar-Lightning of Bitcoin-naar-Bitcoin-transacties. Het is strikt een Liquid-gerichte tool.*


### Betalingsarchitecturen: Onderzeese swaps


Om interoperabiliteit te bereiken tussen Liquid, Lightning en Bitcoin zonder gecentraliseerde custodians, vertrouwt Breez op **Submarine Swaps**. Dit zijn atomaire operaties waarbij een transactie ofwel succesvol wordt afgerond op beide netwerken of mislukt op beide netwerken, zodat fondsen nooit verloren gaan tijdens het transport.


#### Bliksem sturen (onderzeeër verwisselen)

Wanneer een gebruiker een Lightning-factuur betaalt, zendt de SDK een "lock-up" transactie op de Liquid Network uit. Hierdoor wordt het geld in escrow geplaatst. De swapaanbieder (Boltz) detecteert dit, betaalt de Lightning-factuur en gebruikt vervolgens het preimage van de betaling (het cryptografische ontvangstbewijs) om de vergrendelde Liquid-fondsen op te eisen.


#### Bliksem ontvangen (omgekeerde duikbootruil)

Lightning ontvangen is het omgekeerde proces. De gebruiker genereert een factuur en de swapprovider vergrendelt fondsen op de Lightning Network. De SDK bewaakt dit proces via WebSockets. Zodra de vergrendeling is bevestigd, voert de SDK automatisch een claimtransactie uit om de equivalente fondsen naar de Liquid wallet van de gebruiker te verplaatsen.


#### Cross-Chain Bitcoin

Voor Liquid-naar-Bitcoin overdrachten gebruikt de architectuur een "dual-swap" mechanisme. Lock-up transacties vinden gelijktijdig plaats op beide ketens. De verzender claimt geld op Bitcoin, terwijl de ontvanger geld claimt op Liquid. Dit maakt vertrouwensloze overbrugging mogelijk zonder afhankelijkheid van federated peg-outs of gecentraliseerde uitwisselingen.


### Ontwikkelaar Interface en geautomatiseerd beheer


De Breez SDK vereenvoudigt de ervaring van ontwikkelaars door complexe financiële stromen samen te vatten in een gestandaardiseerd proces van drie stappen: **Aansluiten, voorbereiden en uitvoeren**.


1.  **Connect:** Initialiseert de wallet, synchroniseert met de blockchain met behulp van de Liquid Wallet Kit (LWK) en maakt WebSocket verbindingen voor real-time monitoring.

2.  **Voorbereiden:** Voordat u geld vastlegt, berekent en retourneert deze stap alle bijbehorende netwerkkosten en swapkosten, zodat de UI een duidelijk totaal aan de gebruiker kan presenteren.

3.  **Uitvoeren:** Deze stap construeert de transactie, zendt deze uit en initieert de ruil.


#### Geautomatiseerde veiligheidsmechanismen

Een van de belangrijkste functies van de SDK is **Geautomatiseerd restitutiebeheer**. In het geval van een netwerkstoring of een tegenpartij die niet meewerkt, kunnen fondsen theoretisch vast komen te zitten in een contract met tijdslot. De SDK abstraheert de herstellogica volledig. Het controleert de status van elke swap; als een swap mislukt of een time-out heeft, stelt de SDK automatisch de restitutietransactie samen en zendt deze uit om geld terug te sturen naar de wallet van de gebruiker.


Daarnaast behandelt de SDK **Metadata Resolutie**. Het voegt off-chain swapgegevens (geleverd door de Boltz swapper) samen met on-chain transactiegeschiedenis. Dit zorgt ervoor dat de transactiegeschiedenis van de gebruiker leesbaar is voor mensen, en factuurgegevens en betalingscontext weergeeft in plaats van alleen ruwe hexadecimale transactiehashes.


# Laatste Sectie


<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>


## Beoordelingen


<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>


<isCourseReview>true</isCourseReview>

## Eindexamen


<chapterId>b13c4aa8-ced6-11f0-8515-afd3f381a001</chapterId>

<isCourseExam>true</isCourseExam>

## Conclusie


<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>

<isCourseConclusion>true</isCourseConclusion>