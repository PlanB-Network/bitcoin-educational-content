---
name: Bitfeed
description: Verken de hoofdketen van het Bitcoin protocol.
---

![cover](assets/cover.webp)



Bitfeed is een platform voor het visualiseren van de onchainlaag van het Bitcoin protocol. Het is opgezet door een van de bijdragers aan het Mempool.space project en valt vooral op door zijn minimalistische uiterlijk en gebruiksgemak.



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

In deze tutorial bekijken we deze tool, waarmee je alle transacties en blokken op het netwerk kunt verkennen.



## Aan de slag met Bitfeed



Bitfeed is een platform dat zich richt op drie belangrijke punten:





- Blockchain raadpleging**,
- Transactie zoeken**,
- De mempool** visualiseren.



### De blockchain raadplegen



Op de startpagina van Bitfeed vind je voornamelijk :





- De zoekbalk: Dit gedeelte is het ingangspunt voor blockchain zoekopdrachten. Hier kunt u naar een specifiek blok zoeken aan de hand van het nummer of de hash. U kunt ook zoeken naar specifieke transacties en Bitcoin adressen om bepaalde transactie-informatie op het netwerk te verifiëren.



![searchBar](assets/fr/01.webp)



In de linkerbovenhoek zie je de huidige prijs van bitcoin, geschat in Amerikaanse dollars (USD).



![price](assets/fr/02.webp)



Aan de rechterkant vind je het platformmenu. Vanuit dit menu kun je de interface van het platform naar wens aanpassen, items toevoegen of verwijderen en weergavefilters aanpassen. Bekijk bijvoorbeeld de grootte van elk blok op waarde of op gewicht in virtuele bytes (vBytes).



![menu](assets/fr/03.webp)



In het midden van de pagina staat het laatst gemijnde blok, met een overzicht van alle transacties in dat blok. Dit gedeelte geeft informatie over de tijdstempel, het totale aantal bitcoins dat betrokken is bij het blok, de grootte van het blok in bytes, het aantal transacties en de gemiddelde transactiekostenratio per virtuele byte in het blok.



![block](assets/fr/04.webp)



Je kunt teruggaan in de geschiedenis van het kanaal door te zoeken naar een specifiek blok in de zoekbalk, en het bekijken aan de hand van jouw criteria.



We willen bijvoorbeeld de transacties in blok `879488` bekijken.



![bloc](assets/fr/05.webp)



De eerste transactie van dit blok vertegenwoordigt de **coinbase** transactie die de miner van dit blok in staat stelt om de mining beloning te verdienen, die alleen kan worden uitgegeven nadat 100 blokken zijn gemined, bestaande uit de inbegrepen transactiekosten en de bloktoelage. Deze transactie is degene die de uitgifte van nieuwe bitcoins op het systeem mogelijk maakt.



![coinbase](assets/fr/06.webp)



https://planb.academy/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f

Standaard worden transacties in een blok weergegeven volgens twee criteria:




- De grootte, die kan variëren tussen de waarde en het gewicht (vBytes) ;
- De kleur kan variëren tussen leeftijd en de verhouding van transactiekosten per virtuele byte.



![options](assets/fr/07.webp)



We kunnen daarom concluderen dat alle transacties in hetzelfde blok hetzelfde aantal bevestigingen hebben in de blockchain. De grootste kubussen vertegenwoordigen de transacties die de grootste hoeveelheid bitcoins bevatten.



Deze interpretatie wordt verder bevestigd door de menuoptie **"Info"**, die ons informeert over de vertaling van de kleur en grootte van de transacties van het blok.



![infos](assets/fr/08.webp)



Je kunt ook de transacties van een blok bekijken op basis van virtuele bytes en kostenratio. Deze weergave kan verschillen van de vorige, omdat de bitcoinwaarde in een transactie niet de grootte ervan bepaalt.



![visualisation](assets/fr/09.webp)



### Transacties bekijken



Via de zoekbalk kun je een transactie zoeken aan de hand van de bijbehorende identificatie. Je kunt ook op een blokje klikken om de informatie over die transactie te bekijken.



In ons geval nemen we de transactie die de grootste ruimte inneemt in blok `879488`.



![biggest](assets/fr/10.webp)



Je zult zien dat deze transactie `42.989` heeft, wat het verschil is tussen het laatste blok dat gemined werd en ons gekozen blok. Deze bevestigingen helpen de veiligheid van het Bitcoin netwerk te versterken, want om deze transactie kwaadaardig te wijzigen, zouden aanvallers de equivalente rekenkracht moeten hebben om de hele hoofdblokketen te herschrijven.



De omvang van deze transactie is `57.088 vBytes`, voornamelijk door het grote aantal UTXO's dat gebruikt is bij de constructie (842 entries). Verrassend genoeg blijft de toegepaste vergoedingsratio relatief laag (slechts 4 sats/vByte) vergeleken met het totale blokgemiddelde van 5,82 sats/vByte.



De transactie die de meeste ruimte in beslag neemt, is daarom niet noodzakelijkerwijs de transactie met de hoogste transactiekostenratio.



![transaction](assets/fr/11.webp)



Als je de schaal in het **Info** menu volgt, is de transactie met de hoogste transactiekostenratio de paarse. Dit is de transactie [bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35](https://bitfeed.live/tx/bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35) met een transactiekostenratio van `147.49 sats/vBytes`.



![mostfeerate](assets/fr/12.webp)



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Mempool visualisatie



De mempool is de virtuele locatie waar Bitcoin transacties die wachten om opgenomen te worden in een blok gegroepeerd zijn. Bitfeed maakt het mogelijk om de [mempool](https://planb.academy/resources/glossary/mempool) van verschillende Bitcoin miners te raadplegen, wat een breed scala aan transactie-tracking biedt.



![mempool](assets/fr/13.webp)



In deze sectie kun je alle geldige en nog onbevestigde transacties op de hoofdketen van het Bitcoin netwerk volgen.



![unconfirmed](assets/fr/14.webp)



Je hebt nu een handleiding voor het gebruik van het Bitfeed-platform voor het analyseren van blokken en transacties om de informatie die beschikbaar is op de hoofdketen van het Bitcoin-netwerk te visualiseren, terwijl je profiteert van een minimalistische, eenvoudig te gebruiken interface. Als je deze tutorial leuk vond, raden we je aan de volgende stap te nemen: ontdek Lightning Network via het Amboss project.



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017