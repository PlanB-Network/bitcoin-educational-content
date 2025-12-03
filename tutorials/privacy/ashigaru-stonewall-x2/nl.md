---
name: Ashigaru - Stonewall x2
description: Inzicht in en gebruik van Stonewall x2 transacties op Ashigaru
---
![cover stonewall x2](assets/cover.webp)



> *Maak van elke uitgave een coinjoin

## Wat is een Stonewall x2-transactie?



Stonewall x2 is een specifieke vorm van Bitcoin transactie ontworpen om de vertrouwelijkheid van de gebruiker te verhogen bij uitgaven, door samen te werken met een derde partij die niet betrokken is bij de uitgave. Deze methode simuleert een mini-coinjoin tussen twee deelnemers, terwijl er een betaling wordt gedaan aan een derde partij. Stonewall x2 transacties zijn beschikbaar op de Ashigaru applicatie, een fork van Samourai Wallet (het team achter de creatie van dit type transactie).



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Hoe het werkt is relatief eenvoudig: je gebruikt een UTXO in je bezit om de betaling te doen, en roept de hulp in van een derde partij die ook bijdraagt met een UTXO van zichzelf. De transactie eindigt met vier uitgangen: twee van hen in gelijke bedragen, een bestemd voor het adres van de begunstigde, de andere voor een adres van de medewerker. Een derde UTXO wordt teruggestuurd naar een ander adres van de medewerker, waardoor hij het oorspronkelijke bedrag kan terugkrijgen (een neutrale actie voor hem, modulo de mining kosten), en een laatste UTXO keert terug naar een adres van ons, wat de betalingsuitwisseling vormt.



In Stonewall x2 transacties worden dus drie verschillende rollen gedefinieerd:




- De emittent, die de feitelijke betaling verricht ;
- De medewerker, die bitcoins beschikbaar stelt om de anonimiteit van de transactie te verbeteren, terwijl hij zijn geld aan het einde volledig terugkrijgt (een neutrale actie voor hem, modulo de mining kosten);
- De ontvanger, die zich mogelijk niet bewust is van de specifieke aard van de transactie en gewoon betaling verwacht van de verzender.



Laten we een voorbeeld nemen. Alice is bij de bakker om haar stokbrood te kopen, dat `4.000 sats` kost. Ze wil in bitcoins betalen, met behoud van enige vertrouwelijkheid over haar betaling. Dus doet ze een beroep op haar vriend Bob, die haar hierbij zal helpen.



![image](assets/fr/01.webp)



Als we deze transactie analyseren, zien we dat de bakker in werkelijkheid `4.000 sats` ontving als betaling voor het stokbrood. Alice gebruikte `10.000 sats` als input en ontving `6.000 sats` als output, wat een netto saldo geeft van `-4.000 sats`, wat overeenkomt met de prijs van het stokbrood. Bob gebruikte `15.000 sats` als input en ontving twee outputs: een van `4.000 sats` en de andere van `11.000 sats`, dus een saldo van `0`.



In dit voorbeeld heb ik met opzet de mining vergoedingen verwaarloosd om het begrijpelijker te maken. In werkelijkheid worden de transactiekosten gelijkelijk verdeeld tussen de uitgever van de betaling en de medewerker.



## Wat is het verschil tussen Stonewall en Stonewall x2?



Een StonewallX2 transactie werkt op precies dezelfde manier als een Stonewall transactie, behalve dat de eerste gezamenlijk is, terwijl de laatste dat niet is. Zoals we hebben gezien, is er bij een Stonewall x2 transactie sprake van de deelname van een derde partij, die buiten de betaling staat en die zijn of haar bitcoins beschikbaar stelt om de vertrouwelijkheid van de transactie te vergroten. In een klassieke Stonewall-transactie wordt de rol van de medewerker aangenomen door de verzender.



Laten we teruggaan naar ons voorbeeld van Alice bij de bakker. Als ze niet iemand als Bob had kunnen vinden om haar te vergezellen op haar uitgavenreis, had ze in haar eentje een Stonewall kunnen doen. Op die manier zouden de twee UTXO's op de heenweg van haar zijn geweest en zou ze er 3 hebben opgepikt op de terugweg.



![image](assets/fr/02.webp)




Vanuit het oogpunt van een buitenstaander zou de transactie hetzelfde zijn gebleven.



![image](assets/fr/05.webp)



De logica moet daarom als volgt zijn wanneer je een Ashigaru-uitgavenhulpmiddel wilt gebruiken:




- Als de winkelier Payjoin Stowaway niet ondersteunt, kunt u een gezamenlijke transactie maken met een andere persoon buiten de betaling dankzij Stonewall x2 ;
- Als je niemand kunt vinden die een Stonewall x2 transactie wil doen, kun je een Stonewall only transactie doen, die het gedrag van een Stonewall x2 transactie nabootst.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4

## Wat is het nut van een Stonewall x2-transactie?



De Stonewall x2 structuur voegt een enorme hoeveelheid entropie toe aan de transactie, waardoor de ketenanalyse in de war raakt. Van buitenaf gezien zou zo'n transactie geïnterpreteerd kunnen worden als een kleine Coinjoin tussen twee mensen. Maar in werkelijkheid is het een betaling. Deze methode zorgt dus voor onzekerheden in de ketenanalyse, of leidt zelfs tot valse leads.



Laten we het voorbeeld nemen van Alice, Bob en de Boulanger. De transactie op de blockchain zou er als volgt uitzien:



![image](assets/fr/03.webp)



Een buitenstaander die vertrouwt op de heuristiek van gewone ketenanalyse zou ten onrechte kunnen concluderen dat "*Alice en Bob een kleine coinjoin hebben gemaakt, met elk een UTXO in en twee UTXO's elk uit*".



![image](assets/fr/04.webp)



Deze interpretatie is onjuist omdat, zoals je weet, een UTXO naar de Boulanger werd gestuurd, Alice slechts één wisseluitgang heeft en Bob er twee heeft.



![image](assets/fr/01.webp)



Zelfs als de externe waarnemer erin slaagt om de paterne van de Stonewall x2 transactie te identificeren, zal hij niet alle informatie hebben. Hij zal niet kunnen bepalen welke van de twee UTXO's met dezelfde bedragen overeenkomt met de betaling. Hij zal ook niet kunnen bepalen of Alice of Bob de betaling deed. Ten slotte zal hij niet kunnen bepalen of de twee ingevoerde UTXO's van twee verschillende personen zijn, of dat ze toebehoren aan één persoon die ze heeft samengevoegd. Dit laatste is te wijten aan het feit dat de klassieke Stonewall transacties, die hierboven zijn besproken, precies dezelfde paterne volgen als de Stonewall x2 transacties. Van buitenaf gezien en zonder aanvullende contextuele informatie is het onmogelijk om een Stonewall-transactie te onderscheiden van een Stonewall x2-transactie. De eerste zijn geen collaboratieve transacties, terwijl de laatste dat wel zijn. Dit voegt nog meer twijfel toe aan de kosten.



![image](assets/fr/05.webp)




## Hoe maak ik een verbinding tussen Paynyms?



Net als bij andere collaboratieve transacties op Ashigaru (*Cahoots*), omvat Stonewall x2 de uitwisseling van gedeeltelijk ondertekende transacties tussen de verzender en de medewerker. Deze uitwisseling kan handmatig worden uitgevoerd, als je fysiek aanwezig bent bij je medewerker, of automatisch met behulp van het Soroban communicatieprotocol.



Als je voor de tweede optie kiest, moet je een verbinding tussen Paynyms tot stand brengen voordat je een Stonewall x2 kunt uitvoeren. Om dit te doen, moet jouw Paynym de Paynym van je collega "*volgen*" en vice versa. Om erachter te komen hoe je dit doet, kun je het begin van deze andere tutorial volgen:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Hoe maak ik een Stonewall x2 transactie op Ashigaru?



Om een Stonewall x2 transactie uit te voeren, klik je op de afbeelding van je Paynym in de linkerbovenhoek van het scherm en open je het `Samenwerken` menu. De persoon die met jou deelneemt aan de transactie moet hetzelfde doen, tenzij je persoonlijk QR codes uitwisselt.



![Image](assets/fr/06.webp)



Je hebt twee opties: selecteer `Initiate` als je de verzender van de betaling bent, of `Participate` als je de persoon bent die meewerkt aan de transactie maar noch de betaler noch de daadwerkelijke ontvanger bent.



![Image](assets/fr/07.webp)



Als je de rol van medewerker hebt, is de procedure heel eenvoudig. Voor samenwerking op afstand via het Soroban-netwerk klik je op `Deelnemen`, kies je de account die je wilt gebruiken en druk je op `LISTEN FOR CAHOOTS REQUESTS` om te wachten op de aanvraag die de betaler stuurt.



![Image](assets/fr/08.webp)



Aan de andere kant, voor in-person samenwerking via het scannen van QR-codes, ga je naar de startpagina van je wallet, druk je op het QR-codepictogram bovenaan het scherm en scan je de QR-code van de betaler die de transactie initieert.



![Image](assets/fr/09.webp)



Als je de rol van betaler hebt, dus degene die de transactie initieert, ga dan naar het menu `Samenwerken` en selecteer vervolgens `Initieer`.



![Image](assets/fr/10.webp)



Kies deze optie voor het transactietype, aangezien we een Stonewall x2 willen uitvoeren.



![Image](assets/fr/11.webp)



Je kunt dan kiezen tussen online samenwerking (*Cahoots* via *Soroban*) of face-to-face samenwerking, met QR-code uitwisselingen.



![Image](assets/fr/12.webp)



### Cahoots online



Als je de `Online` optie hebt gekozen, selecteer dan je medewerker van de Paynyms die je volgt.



![Image](assets/fr/13.webp)



Klik op `Transactie instellen` en kies vervolgens de rekening waarvan je de uitgave wilt doen.



![Image](assets/fr/14.webp)



Voer op de volgende pagina de transactiegegevens in: het adres van de ontvanger van de betaling, het te verzenden bedrag en het tarief. Klik vervolgens op `Review transactie setup`.



![Image](assets/fr/15.webp)



Controleer de informatie zorgvuldig, zorg ervoor dat je medewerker luistert naar de *Cahoots* verzoeken en klik dan op de groene `BEGIN TRANSACTIE` knop om de uitwisseling van PSBTs via Soroban te starten.



![Image](assets/fr/16.webp)



Wacht tot beide deelnemers de transactie hebben ondertekend en zend deze dan uit op het Bitcoin netwerk.



![Image](assets/fr/17.webp)



### Persoonlijke gesprekken



Als u de inwisseling persoonlijk wilt uitvoeren, selecteer dan het transactietype `STONEWALL X2` en kies vervolgens de optie `In persoon / handmatig`.



![Image](assets/fr/18.webp)



Klik op `Transactie instellen` en kies vervolgens de rekening waarvan je de uitgave wilt doen.



![Image](assets/fr/19.webp)



Voer op de volgende pagina de transactiegegevens in: het adres van de ontvanger van de betaling, het te verzenden bedrag en het tarief. Klik vervolgens op `Review transactie setup`.



![Image](assets/fr/20.webp)



Controleer de details en druk vervolgens op de groene knop `BEGIN TRANSACTION` om te beginnen met het uitwisselen van PSBT's via het scannen van QR-codes.



![Image](assets/fr/21.webp)



De uitwisseling gebeurt door afwisselend te scannen met de medewerker: klik op `SHOW QR CODE` om je QR code aan je medewerker te tonen, die hem zal scannen. Hij zal dan klikken op `SHOW QR CODE` om de zijne weer te geven, en u scant het met `LAUNCH QR Scanner`. Herhaal dit proces tot alle vijf uitwisselingsstappen voltooid zijn.



![Image](assets/fr/22.webp)



Zodra alle uitwisselingen zijn voltooid, controleer je de details van de transactie en geef je deze vrij door de groene pijl onder aan het scherm te slepen.



![Image](assets/fr/23.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/9082f3d989728aacd290535a1ac374ab8c04a241a1d798b378db626dabea7a24). De structuur is als volgt:



![Image](assets/fr/24.webp)



*Krediet: [mempool.space](https://mempool.space/)*



We zien twee inputs uit mijn portefeuille, respectievelijk `91.869 sats` en `64.823 sats`, terwijl de andere twee inputs uit de wallet van mijn medewerker komen. Aan de uitvoerzijde wordt een UTXO van `100.000 sats` naar de huidige begunstigde gestuurd, en twee UTXO's van `100.000 sats` en `159.578 sats` gaan terug naar de portefeuille van mijn medewerker. Voor hem is de operatie neutraal, omdat hij het volledige bedrag terugkrijgt van de fondsen die hij had geïnvesteerd in de input (exclusief de mining kosten waaraan hij bijdroeg). Tenslotte ontvang ik een UTXO uitwisseling van `56.270 sats`, wat overeenkomt met het verschil tussen mijn totale input en de betaling van `100.000 sats` die naar de ontvanger is gestuurd.



Uiteraard kan ik deze structuur beschrijven omdat ik de transactie zelf heb gebouwd. Maar voor een waarnemer van buitenaf is het over het algemeen onmogelijk om te bepalen welke UTXO's bij welke deelnemer horen, zowel bij de invoer als bij de uitvoer.



Om je kennis van onchain privacybeheer op Bitcoin te verdiepen, raad ik je aan mijn BTC 204 training te volgen op Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c