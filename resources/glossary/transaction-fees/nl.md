---
term: TRANSACTIEKOSTEN
---

Transactievergoedingen vertegenwoordigen een bedrag dat bedoeld is om miners te compenseren voor hun deelname aan het Proof of Work mechanisme. Deze vergoedingen moedigen miners aan om transacties op te nemen in de blokken die ze creëren. Ze komen voort uit het verschil tussen de totale hoeveelheid inputs en de totale hoeveelheid outputs in een transactie:


```text
fees = inputs - outputs
```


Ze worden uitgedrukt in `Sats/vBytes`, wat betekent dat de vergoedingen niet afhangen van de hoeveelheid verzonden bitcoins, maar van het gewicht van de transactie. Ze worden vrij gekozen door de verzender van een transactie en bepalen de snelheid van opname in een blok door middel van een veilingmechanisme. Laten we bijvoorbeeld zeggen dat ik een transactie doe met een input van `100.000 Sats`, een output van `40.000 Sats`, en een andere output van `58.500 Sats`. Het totaal van de uitvoer is `98.500 Sats`. De vergoedingen voor deze transactie zijn `1.500 Sats`. De Miner die mijn transactie meerekent, kan `1.500 Sats` creëren in hun Coinbase Transaction in Exchange voor de `1.500 Sats` die ik niet heb teruggekregen in mijn outputs.


Transacties met hogere vergoedingen, in verhouding tot hun grootte, worden door miners met voorrang behandeld, wat het bevestigingsproces kan versnellen. Omgekeerd kunnen transacties met lagere vergoedingen worden vertraagd tijdens perioden van grote congestie. Het is goed om op te merken dat de Bitcoin transactiekosten los staan van de blokkensubsidie, die een extra stimulans is voor miners. De Block reward bestaat uit nieuwe bitcoins die worden gecreëerd bij elk gemined blok (bloksubsidie), evenals de verzamelde transactievergoedingen. Terwijl de bloksubsidie na verloop van tijd afneemt vanwege de totale Supply limiet van bitcoins, zullen transactievergoedingen een cruciale rol blijven spelen in het aanmoedigen van miners om deel te nemen.


Op protocolniveau verhindert niets gebruikers om transacties zonder kosten in een blok op te nemen. In werkelijkheid is dit type transactie zonder vergoedingen uitzonderlijk. Standaard geven Bitcoin nodes geen transacties door met vergoedingen lager dan `1 sat/vBytes`. Als sommige transacties zonder vergoedingen zijn gepasseerd, is dat omdat ze direct zijn geïntegreerd door de winnende Miner, zonder het netwerk van knooppunten te doorlopen. De volgende transactie bevat bijvoorbeeld geen vergoedingen:


```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```


In dit specifieke voorbeeld was het een transactie geïnitieerd door de directeur van de F2Pool Mining pool. Als gewone gebruiker is de huidige ondergrens daarom `1 sat/vBytes`.

Het is ook nodig om de limieten van purging te overwegen. Tijdens periodes van hoge congestie zuiveren de mempools van nodes hun lopende transacties onder een bepaalde drempel, om hun toegewezen RAM-limiet te respecteren. Deze limiet is vrij te kiezen door de gebruiker, maar velen laten de standaardwaarde van Bitcoin core op 300 MB staan. Het kan worden aangepast in het `Bitcoin.conf` bestand met de `maxmempool` parameter.

> ► *In het Engels noemen we dit "transaction fees".*