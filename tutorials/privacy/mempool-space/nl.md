---
name: Mempool
description: Verken het hele Bitcoin ecosysteem.
---

![cover](assets/cover.webp)



Het Bitcoin protocol is een pseudoniem, gedecentraliseerd netwerk dat openstaat voor raadpleging. Leden (nodes), dat wil zeggen computers met een instantie van de Bitcoin software, hebben onbeperkte toegang tot alle gegevens die op Bitcoin gepubliceerd zijn. In de beginjaren van Bitcoin was het protocol echter niet zo breed toegankelijk als tegenwoordig.


In de begindagen van Bitcoin was het nodig om een Bitcoin knooppunt te draaien om toegang te krijgen tot de juiste gereedschappen (bitcoin-cli) om het netwerk vanaf commandoregels te ondervragen.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Daarom zijn er projecten gestart om de Bitcoin gemeenschap uit te breiden en toegankelijker te maken voor iedereen die geen node bezit en/of niet over de vereiste technische vaardigheden beschikt.



In deze tutorial bekijken we het **Mempool.space** project, de mogelijkheden en de impact die het heeft gehad op het Bitcoin ecosysteem.



## Wat is Mempool.space?



**Mempool.space** is een open-source verkenner die nuttige informatie geeft over transacties, transactiekosten, blokken en miners op de verschillende Bitcoin protocolnetwerken. Het is gelanceerd in 2020 en brengt een aanzienlijke verbetering in de gebruikerservaring door middel van representatieve afbeeldingen, vloeiende animaties en overzichtelijke interfaces.



Om het project te begrijpen, een Mempool (geheugenpool) is een virtuele ruimte waarin alle transacties die wachten op bevestiging op het Bitcoin netwerk worden opgeslagen. Een Mempool is als een "wachtkamer" waar Bitcoin transacties wachten om bevestigd te worden. Elke computer op het netwerk (node) heeft zijn eigen wachtkamer, wat verklaart waarom niet alle transacties tegelijkertijd voor iedereen zichtbaar zijn.



De belangrijkste impact van het platform in het Bitcoin ecosysteem is dat je toegang hebt tot de gevarieerde informatie in de geheugengebieden van de meeste knooppunten die op Bitcoin aanwezig zijn, zonder dat je er een hoeft te draaien. Mempool.space is een opslagplaats voor het bekijken en doorzoeken van Bitcoin protocolnetwerken.



Door het toenemende gebruik in het ecosysteem en het feit dat Mempool.space open source is, is het in steeds meer persoonlijke hostingsystemen geïntegreerd. U kunt nu uw eigen instantie van Mempool.space direct op uw persoonlijke node hebben. Bekijk hieronder onze tutorial over het configureren van Mempool.space op uw Umbrel node.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## De basis van Mempool.space



Zoals hierboven vermeld, is [Mempool.space](https://Mempool.space) een Bitcoin protocolverkenner waarmee je je transacties en hun propagatie op het gekozen Bitcoin netwerk in realtime kunt volgen, vanuit een grafische Interface.



Mempool.space ondersteunt vele Bitcoin protocolnetwerken.


In de menubalk vind je de volgende netwerken:




- **Mainnet**: Het belangrijkste Bitcoin netwerk waar echte Bitcoin transacties plaatsvinden.
- **Signet**: Een testnetwerk dat digitale handtekeningen gebruikt om blokken te valideren zonder de middelen nodig te hebben die het hoofdnetwerk nodig heeft.
- **Testnet 3**: Een risicovrij test- en ontwikkelingsnetwerk op het Bitcoin protocol.
- **Testnet 4**: De nieuwe versie van Testnet 3 brengt meer stabiliteit en nieuwe consensusregels naar de testomgeving.



![reseaux](assets/fr/01.webp)



Op de startpagina, links in Green, zie je de mogelijke toekomstige blokken (groepen transacties) die klaar zijn om gevalideerd en geïntegreerd (gemined) te worden in het Bitcoin netwerk. Gemiddeld wordt er elke tien minuten een blok gemined: bewaar deze informatie, want het zal later van pas komen bij onze ontwikkeling.


In het paars, aan de rechterkant, vind je de recente blokken gedolven op Bitcoin, waarbij het nummer van het laatst gedolven blok de huidige hoogte van het netwerk weergeeft.



![blocs](assets/fr/02.webp)



De **Transactiekosten** sectie is een schatter voor transactiekosten. Hoe hoger de vergoedingen die aan je transactie zijn toegewezen, hoe waarschijnlijker het is dat je transactie wordt toegevoegd aan het volgende blok dat klaar is om gemijnd te worden.


Transactiekosten vertegenwoordigen de kosten die een Miner van je vraagt om jouw transactie in een kandidaatblok voor Mining in te voegen. Het wordt gedefinieerd door een verhouding van sat/vB (Satoshi/virtuele bytes) die het aantal satoshis weergeeft dat je betaalt voor de ruimte die jouw transactie inneemt in het kandidaat-blok.



⚠️ BELANGRIJK: In het geval van Mempool verzadiging, geven miners voorrang aan transacties met de beste Satoshi/vByte verhouding. Hoe zwaarder (groter) uw transactie, hoe meer satoshis deze nodig heeft om snel te worden opgenomen.



![fees-visualizer](assets/fr/03.webp)



Met het **Mempool Goggles** gedeelte kunt u de ruimte visualiseren die door een transactie wordt ingenomen.



![mempool](assets/fr/04.webp)



Een blok wordt ongeveer elke tien minuten gemined vanwege de moeilijkheidsgraad van de Proof of Work die miners moeten leveren om hun kandidaat-blok toe te voegen aan de keten van gemijnde blokken. Deze moeilijkheid varieert elke **2016 blokken**, gelijk aan ongeveer **2 weken**. Je kunt de evolutie van deze moeilijkheid hier zien.



![difficulty](assets/fr/05.webp)



De toevoeging van een nieuw blok aan de hoofdketen geeft de Miner van het gevalideerde blok recht op een beloning die bestaat uit een vast deel (gehalveerd om de 210.000 blokken**, gelijk aan ongeveer 4 jaar** tijdens de halvings) en transactiekosten.



![halving](assets/fr/06.webp)



## Toegang tot je transactiegegevens



In de zoekbalk van Mempool.space kun je je Bitcoin Address of je transaction ID invoeren om meer te weten te komen over je geschiedenis.



![search](assets/fr/07.webp)



Op de pagina met transactiegegevens vind je algemene informatie over je transactie:




- **Status**: Bevestigd wanneer toegevoegd aan een blok, onbevestigd wanneer wachtend in een Mempool.
- **Transactiekosten**.
- **Geschatte aankomsttijd (ETA)**: De geschatte tijd die het duurt voordat uw transactie is toegevoegd aan een blok. Het wordt berekend op basis van de ratio die de kosten vormt die aan deze transactie zijn verbonden.



![general-txinfo](assets/fr/08.webp)



Het **Flow** gedeelte toont een grafiek van je transactiecomponenten.



Inputs (vorige UTXO), gebruikt voor je transactie, en outputs die ontvangers het recht geven om de bitcoins van elke output te gebruiken door de handtekening voor te leggen die vereist is voor hun uitgave.



![flow](assets/fr/09.webp)



Meer details over de gebruikte adressen zijn te vinden in het gedeelte **Inputs & Outputs**.



![address](assets/fr/10.webp)



Ontdek de verschillende Bitcoin transactieschema's om uw vertrouwelijkheid te verbeteren.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Versnel je transacties



In het Bitcoin ecosysteem is het aspect van transactievalidatie door miners intrinsiek verbonden met de transactiekosten die aan die transactie verbonden zijn. Miners geven voorrang aan transacties met een hogere vergoedingsratio (satoshis/vBytes), wat de geldigheid van jouw transactie kan beïnvloeden als je geen redelijke vergoedingen betaalt die door miners worden geaccepteerd. Je transactie zou vast komen te zitten in Mempool, wachtend op een blok dat zijn vergoedingsratio aanvaardt.



Gelukkig zijn er twee methoden beschikbaar op het Bitcoin netwerk om de bevestiging van je transactie te versnellen.





- **RBF** - Vervanging door kosten: Een methode waarmee je dezelfde invoer kunt uitgeven als je transactie met lage fee, maar nu door de transactiekosten te verhogen om de validatie te versnellen. Je nieuwe transactie wordt sneller gevalideerd en opgenomen in een blok, waardoor de transactie met lage fee ongeldig wordt.



Je kunt een kostenvervangende actie uitvoeren met portemonnees die dit mechanisme accepteren. Zie bijvoorbeeld ons artikel over de Blue Wallet Wallet.



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- **CPFP** - Child pay for parent: Een benadering geïnspireerd op RBF, maar dan aan de kant van de ontvanger. Wanneer de transactie waarbij jij de ontvanger bent, wordt geblokkeerd in een Mempool, heb je de optie om de uitvoer (UTXO's) van deze transactie uit te geven, ondanks het feit dat deze nog niet is bevestigd, door meer vergoedingen aan deze nieuwe transactie toe te wijzen, zodat de gemiddelde vergoedingen - van de transactie waarbij jij de ontvanger bent en de geïnitieerde transactie - mijnwerkers aanmoedigen om beide transacties in een blok op te nemen.



⚠️ De eerste transactie moet worden opgenomen in een blok om de tweede transactie te kunnen bevestigen.



Als al deze termen een beetje te technisch lijken, raad ik je aan om [onze woordenlijst te raadplegen](https://planb.network/resources/glossary), die definities bevat van alle technische termen die te maken hebben met Bitcoin en haar ecosysteem.



Naast deze methoden kunt u met Mempool.space, dankzij de connecties met meer dan 80% van de miners die aanwezig zijn op het Bitcoin netwerk, ook al uw **onbevestigde** transacties versnellen, zelfs degenen die RBF niet activeren, door een vergoeding te betalen aan de miners in Exchange voor het invoegen van uw goedkope transactie in het volgende blok dat klaar is om gemined te worden.



Klik op de pagina met transactiedetails op de knop **Versnel** en ga verder met het betalen van uw tegenpartij aan de miners.



![accelerate-section](assets/fr/11.webp)


## Minderjarigen



Een Miner verwijst naar een persoon die een mijn beheert, d.w.z. een computer die betrokken is bij het Mining proces, dat bestaat uit deelname aan Proof-of-Work. De Miner groepeert de lopende transacties in zijn Mempool om een kandidaatblok te vormen. De Miner groepeert de lopende transacties in zijn Mempool om een kandidaatblok te vormen. Hij zoekt dan naar een geldige Hash, kleiner dan of gelijk aan het doel, voor de header van dit blok door de verschillende nonces aan te passen. Als hij een geldige Hash vindt, zendt hij zijn blok uit naar het Bitcoin netwerk en strijkt de bijbehorende geldelijke beloning op, bestaande uit de bloksubsidie (ex-nihilo creëren van nieuwe bitcoins) en de transactiekosten.



https://planb.network/courses/ce272232-0d97-4482-884a-0f77a2ebc036

miners zijn een soort "validators" die transacties verifiëren en groeperen in blokken. Om een nieuw blok aan het Bitcoin netwerk toe te voegen, moeten ze een complexe wiskundige puzzel oplossen (de Proof-of-Work). De eerste Miner die de puzzel oplost, wint een Bitcoin beloning (bloktoelage + vergoedingen voor transacties in het blok).



De moeilijkheidsgraad van deze Proof of Work wordt bijgehouden, zodat je de evolutie van de benodigde rekenkracht voor miners kunt visualiseren. Je vindt in de onderstaande secties :





- Een schatting van de totale beloningen die mijnwerkers hebben geoogst tijdens de laatste moeilijkheidsgraad aanpassing, evenals schattingen van de volgende Halving van de bloktoekenning, die elke 210.000 blokken voorkomt (ongeveer 04 jaar).



![rewards](assets/fr/12.webp)



Deze moeilijkheidsgraad wordt elke 2016 blocks (ongeveer twee weken) aangepast. Het is omgekeerd evenredig met de gemiddelde tijd die mijnwerkers nodig hebben om Miner elke 2016 blokken te maken.


Wanneer de gemiddelde tijd die mijnwerkers nodig hebben minder dan 10 minuten is, neemt de moeilijkheidsgraad toe, wat bewijst dat het voor mijnwerkers makkelijker was om Miner blokken te valideren. Omgekeerd, wanneer de gemiddelde tijd meer dan 10 minuten bedraagt, neemt de moeilijkheidsgraad af.



![mining-pool](assets/fr/13.webp)





- Groepen mijnwerkers: Gezien de moeilijkheidsgraad werkt een groep miners samen om Proof of Work te helpen vinden op Bitcoin, in wat we een **pool** noemen. Wanneer een blok wordt gedolven door de groep, wordt de verkregen beloning verdeeld volgens het percentage van succes in elke Miner's gedeeltelijke oplossing zoeken, d.w.z. de bijdrage in rekenkracht in de zoektocht naar Proof-of-Work, of volgens de beloningsmethode overeengekomen door de samenwerking.





![mining](assets/fr/14.webp)



## Lightning Network infrastructuur



Mempool geeft niet alleen informatie over Bitcoin's netwerkinfrastructuur (hoofdketen). Het integreert ook visualisatie- en verkenningstools voor Bitcoin's Lightning overlay.



In het **Lightning** gedeelte kun je alle bestaande verbindingen tussen Lightning nodes bekijken.



![network-stats](assets/fr/15.webp)



Deze Interface geeft informatie over :





- Lightning Network statistieken.



![distribution](assets/fr/16.webp)




⚠️ **BELANGRIJK**: De capaciteit van een betalingskanaal geeft het maximale bedrag aan dat een knooppunt naar een ander knooppunt kan sturen tijdens een Lightning-transactie.





- Lightning-nodes worden toegewezen op basis van de internetprovider (hostingdienst) en optioneel op basis van de capaciteit van het betalingskanaal.



![distribution](assets/fr/17.webp)





- De geschiedenis van de totale capaciteit van de Lightning Network.


Je vindt ook een rangschikking van deze knooppunten volgens de capaciteit van hun betaalkanalen.



![ranking](assets/fr/18.webp)



## Meer afbeeldingen



Mempool.space is het ideale platform om te genieten van interactie met Bitcoin protocolnetwerken. De grafieken bieden niet alleen visuele gegevens om je te helpen beslissen wanneer je transacties moet uitvoeren, maar ook precieze parameters waarmee je in realtime de kracht en gezondheid van het Bitcoin netwerk en de bijbehorende Lightning-infrastructuren kunt visualiseren.



In het **Grafieken** gedeelte kun je essentiële gegevens over het Bitcoin netwerk bekijken:




- Mempool grootte evolutie: U kunt observeren hoe de grootte van de Mempool fluctueert, wat kan duiden op perioden van hoge of lage activiteit op het netwerk.



![graphs](assets/fr/19.webp)






- De evolutie van transacties en transactiekosten op het gekozen netwerk: Door variaties in transacties per seconde bij te houden, kun je anticiperen op perioden van congestie of lage activiteit en je transactiekosten optimaliseren. Deze grafiek geeft je een idee van de capaciteit van het netwerk om het volume aan transacties te verwerken.



![graphs](assets/fr/20.webp)



Nu je het einde van je reis op Mempool.space hebt bereikt, kun je je eigen verkenner worden en je transacties in realtime volgen. Hieronder vind je ons artikel over de Bitcoin **Publieke Pool** verkenner.



https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1