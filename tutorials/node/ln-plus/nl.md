---
name: Lightning Network+
description: Ontvang gratis inkomende liquiditeit met coöperatieve openingen op je Lightning-knooppunt
---

![cover](assets/cover.webp)



## Inleiding



[LN+ (Lightning Network Plus)](https://lightningnetwork.plus/) is een gemeenschapsplatform dat ontworpen is om de samenwerking tussen Lightning Network knooppuntbeheerders te vergemakkelijken. Het belangrijkste doel is om de connectiviteit, liquiditeit en decentralisatie van het Lightning-netwerk te verbeteren, zonder dat er gecentraliseerde tussenpersonen nodig zijn.



Deze tutorial richt zich op de **"Swaps"** dienst, die vandaag de dag de meest gebruikte en structurerende functie van LN+ is. De andere diensten die het platform aanbiedt, worden ook gepresenteerd.



## LN+ overzicht



### Wat is Lightning Network Plus?



Lightning Network Plus (LN+) is een gemeenschapsplatform voor exploitanten van Lightning-knooppunten die direct en vrijwillig willen samenwerken. Het heeft als doel de creatie van nuttige, evenwichtige en duurzame Lightning-kanalen te vergemakkelijken, terwijl de noodzaak voor gecentraliseerde oplossingen of opgelegde hubs wordt vermeden.



LN+ is gebaseerd op een fundamenteel principe: peer-to-peer samenwerking, gebaseerd op transparantie, wederkerigheid en reputatie.



### LN+ diensten in een oogopslag



LN+ biedt verschillende diensten om de topologie en liquiditeit van het Lightning-netwerk te verbeteren, waaronder :





- Swaps**: wederzijdse opening van kanalen tussen exploitanten (hoofddienst).
- Ringen**: cirkelvormige kanaalopeningen tussen verschillende deelnemers.
- Op vertrouwen gebaseerde swaps**: varianten die meer vertrouwen stellen in het verleden van de deelnemers.
- Sociale functies**: profielen, commentaar en reputatiesysteem.



In de rest van deze tutorial concentreren we ons uitsluitend op de **Swaps** dienst, die de kern vormt van het huidige LN+ gebruik.



## LN+ "Wisseldienst



### Definitie van een LN+ ruil



Een LN+ **swap** is een vrijwillige overeenkomst tussen twee exploitanten van Lightning-knooppunten om wederzijds Lightning-kanalen van gelijkwaardige (of vooraf overeengekomen) capaciteit te openen. In tegenstelling tot een conventionele eenzijdige kanaalopening, is de swap gebaseerd op **expliciete wederkerigheid**.



In de praktijk :





- Je opent een kanaal naar het knooppunt van je partner.
- Je partner opent een kanaal naar je knooppunt.
- Beide partijen leggen beslag op een vergelijkbare hoeveelheid on-chain bitcoins.



### Wat is het doel van swaps voor knooppuntbeheerders?



De Swaps-service pakt verschillende belangrijke problemen aan waarmee Lightning-exploitanten worden geconfronteerd:





- Verbeterde connectiviteit**: creatie van bruikbare bidirectionele kanalen zodra ze worden geopend.
- Beter liquiditeitsbeheer**: elke partij heeft zowel inkomende als uitgaande capaciteit.
- Minder risico op onnodige kanalen**: de partner wordt aangemoedigd om het kanaal open te houden.
- Meer decentralisatie**: directe verbindingen tussen operatoren, zonder opgelegde hubs.



### Voor welke knooppuntprofielen zijn swaps nuttig?



Swaps zijn vooral nuttig voor :





- Nieuwe knooppunten die hun routeerbaarheid snel willen verbeteren.
- Intermediaire operators die de dichtheid van hun kanaalgrafiek willen vergroten.
- Knooppunten die gericht zijn op routering en hun topologie willen optimaliseren.



## Verbind uw Lightning-knooppunt met de LN+



### Technische vereisten



Voordat je begint, heb je het volgende nodig:





- Een werkend Lightning-knooppunt (LND, Core Lightning of Eclair).
- Toegang tot de beheerinterface van je node.
- Voldoende on-chain capaciteit om kanalen te openen.



Ga naar de [Lightning Network](https://lightningnetwork.plus/) Plus website en klik op de `Login` knop rechtsboven in de interface.



![capture](assets/fr/03.webp)



### Authenticatie door berichthandtekening



Om uzelf te authenticeren, moet u het bericht ondertekenen met de privésleutel van uw Lightning-knooppunt. Met ThunderHub is dit heel eenvoudig.



Begin met het kopiëren van het bericht dat LN+ weergeeft.



![capture](assets/fr/04.webp)



Ga in ThunderHub naar het tabblad `Tools` en klik vervolgens op de knop `Teken` in de sectie `Messages`.



![capture](assets/fr/05.webp)



Plak het authenticatiebericht van LN+ en klik op `Teken`.



![capture](assets/fr/06.webp)



ThunderHub ondertekent dit bericht dan met de private sleutel van jouw knooppunt. Kopieer de gegenereerde handtekening.



![capture](assets/fr/07.webp)



Plak deze handtekening in het corresponderende veld op de LN+ site en klik vervolgens op `Aanmelden`.



![capture](assets/fr/08.webp)



Je bent nu verbonden met LN+ met je Lightning-knooppunt. Dit proces stelt LN+ in staat om te verifiëren dat jij de rechtmatige eigenaar bent van het knooppunt dat je claimt op hun platform.



![capture](assets/fr/09.webp)



Als je wilt, kun je je LN+ profiel personaliseren, bijvoorbeeld door een korte biografie toe te voegen.



## Deelnemen aan een bestaande swap



### Toegang tot ruilaanbiedingen



Om deel te nemen aan je eerste kanaalopening ga je naar het `Swaps` menu bovenaan de interface. Hier vind je alle swaps die momenteel beschikbaar zijn, afhankelijk van de eigenschappen van je node.



![capture](assets/fr/10.webp)



### Voorwaarden om in aanmerking te komen



Om deel te nemen aan een bestaande swapaanbieding, selecteer je gewoon de bijbehorende advertentie en registreer je. LN+ staat de maker van de swap echter toe om bepaalde **gerechtigdheidsvoorwaarden** te definiëren, zoals :





- een minimum aantal kanalen al open ;
- minimale totale knooppuntcapaciteit ;
- bepaalde soorten verbindingen geaccepteerd.



### Recente knooppunten



Als gevolg hiervan is het, vooral in de beginfase van het gebruik, mogelijk dat er **weinig of geen aanbiedingen beschikbaar** zijn voor je knooppunt. Dit is een veel voorkomende situatie voor nieuwe of nog niet aangesloten nodes.



In mijn geval voldeed geen van de aanbiedingen aan de vereiste criteria, ondanks het bestaan van een paar open kanalen.



## Maak je eigen ruilaanbieding



### Wanneer moet je je eigen swap maken?



Als er geen bestaand aanbod beschikbaar is, is het maken van je eigen swap vaak de beste oplossing. Zo behoud je ook de controle over de parameters van de swap.



### Wisselconfiguratie



Klik op **Start Liquidity Swap** en configureer vervolgens je aanbiedingsparameters:





- selecteer het totale aantal deelnemers (3, 4 of 5);
- geven de capaciteit van de te openen kanalen aan;
- de verbintenisperiode definiëren waarin deelnemers ermee instemmen hun kanalen niet af te sluiten;
- eventuele beperkingen voor deelnemers specificeren (minimumaantal kanalen, minimale totale capaciteit, type verbinding dat wordt geaccepteerd).



![capture](assets/fr/11.webp)



### Publicatie en verwachtingen van deelnemers



Zodra alle parameters zijn ingevoerd, klik je op **Start Liquidity Swap** om je aanbieding te publiceren. Nu hoef je alleen nog maar te wachten tot andere operators zich aanmelden.



![capture](assets/fr/12.webp)



## Een ruil afronden



### Effectieve kanaalopening



Nu alle wisselposities zijn ingenomen, kan elke deelnemer op zijn LN+ interface zien naar welk knooppunt hij een Lightning-kanaal moet openen.



![capture](assets/fr/13.webp)



Aan uw kant opent u het kanaal met behulp van de Node ID die LN+ heeft verstrekt en met inachtneming van de aangegeven hoeveelheid. Deze handeling kan worden uitgevoerd via ThunderHub, een andere Lightning-knooppuntmanager of rechtstreeks via de basisinterface van uw knooppunt.



![capture](assets/fr/14.webp)



Zodra het kanaal is geopend, verschijnt het in het gedeelte met wachtende kanalen.



![capture](assets/fr/15.webp)



### Bevestiging in LN+



Ga dan terug naar LN+ om te bevestigen dat u de kanaalopening hebt gestart, door te klikken op de knop `Channel Opening Started`.



![capture](assets/fr/16.webp)



### Einde ruil



Als alle deelnemers de kanalen hebben geopend waartoe ze zich hebben verbonden, wordt de swap als compleet beschouwd.



## Reputatie en goede communicatiepraktijken



### Het LN+ reputatiesysteem



LN+ bevat een reputatiesysteem dat gebaseerd is op de meningen die deelnemers achterlaten na afloop van swaps. Deze meningen zijn openbaar en hebben een directe invloed op de mogelijkheid van een operator om deel te nemen aan toekomstige swaps of deze aan te maken.



![capture](assets/fr/17.webp)



### Aanbevolen best practices



Om een goede reputatie te behouden en ervoor te zorgen dat swaps soepel verlopen, wordt aanbevolen om :





- deadlines voor kanaalopening respecteren ;
- snel communiceren in geval van een probleem of vertraging;
- gebruik het commentaargedeelte om van gedachten te wisselen met andere deelnemers;
- een kanaal niet te sluiten voor het einde van de verbintenisperiode.




![capture](assets/fr/18.webp)



### Waarom reputatie centraal staat bij LN+



LN+ is gebaseerd op een model van vrijwillige samenwerking, zonder sterke technische beperkingen. Reputatie is daarom de belangrijkste stimulans om de betrouwbaarheid van de deelnemers te garanderen.



## Andere LN+ diensten



Naast Swaps biedt LN+ andere diensten die ontworpen zijn om de connectiviteit en coördinatie tussen Lightning-knooppuntoperators te verbeteren. Ringen** stellen meerdere deelnemers in staat om een lus van kanaalopeningen te creëren, waardoor de redundantie van routingpaden en de dichtheid van de Lightning-grafiek worden versterkt. Trust-based swaps** zijn gebaseerd op vergelijkbare principes als klassieke swaps, maar bieden meer flexibiliteit aan deelnemers die al een gevestigde reputatie hebben op het platform.



LN+ integreert ook sociale functies zoals openbare knooppuntprofielen, ruilcommentaren en een reputatiesysteem. Deze tools zijn op zich geen technische diensten, maar spelen een centrale rol in de soepele werking van het platform en vergemakkelijken de communicatie, coördinatie en het vertrouwen tussen de operatoren.



## Conclusie



De Swapsdienst van LN+ is een effectief hulpmiddel voor het verbeteren van de connectiviteit, liquiditeit en decentralisatie in het Lightning-netwerk. Door wederzijdse, gecoördineerde kanaalopeningen te bevorderen, stelt LN+ knooppuntbeheerders in staat om hun topologie te versterken en tegelijkertijd verantwoordelijke, gedecentraliseerde samenwerking te bevorderen.