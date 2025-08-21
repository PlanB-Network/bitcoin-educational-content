---
name: Ricochet
description: Ricochet-transacties begrijpen en gebruiken
---
![cover ricochet](assets/cover.webp)


***WAARSCHUWING:** Na de arrestatie van de oprichters van Samourai Wallet en de inbeslagname van hun servers op 24 april, is de tool Ricochet niet langer beschikbaar. Het is echter mogelijk dat deze tool in de komende weken weer beschikbaar komt. In de tussentijd kun je Ricochet alleen handmatig uitvoeren. Het theoretische deel van dit artikel blijft relevant om de werking ervan te begrijpen en te leren hoe je het handmatig kunt doen.*


we volgen de ontwikkelingen van deze zaak en de ontwikkelingen met betrekking tot de bijbehorende tools op de voet. Wees gerust dat we deze handleiding zullen bijwerken zodra er nieuwe informatie beschikbaar is._


deze handleiding is alleen bedoeld voor educatieve en informatieve doeleinden. We keuren het gebruik van deze tools voor criminele doeleinden niet goed en moedigen dit ook niet aan. Het is de verantwoordelijkheid van elke gebruiker om te voldoen aan de wetten in hun rechtsgebied._


---

> Een eersteklas tool die extra geschiedenis toevoegt aan je transactie. Stuit de zwarte lijsten tegen de borst en bescherm je tegen onterechte sluitingen van accounts van derden.

## Wat is Ricochet?


Ricochet is een techniek waarbij je meerdere fictieve transacties naar jezelf uitvoert om een overdracht van Bitcoin Ownership te simuleren. Dit hulpmiddel verschilt van andere Samourai-transacties, omdat het geen prospectieve anonimiteit biedt, maar eerder een vorm van retrospectieve anonimiteit. Ricochet helpt de specifieke kenmerken te vervagen die de fungibiliteit van een Bitcoin Coin in gevaar kunnen brengen.


Als je bijvoorbeeld een CoinJoin uitvoert, zal je Coin uitvoer uit de mix als zodanig geïdentificeerd worden. Ketenanalysetools zijn in staat om patronen van CoinJoin transacties te detecteren en de munten die daaruit voortkomen te labelen. CoinJoin is er inderdaad op gericht om de historische links van een Coin te verbreken, maar zijn doorgang door coinjoins blijft detecteerbaar. Om een analogie te maken, dit fenomeen is vergelijkbaar met het versleutelen van een tekst: ook al hebben we geen toegang tot de originele klare tekst, het is gemakkelijk te identificeren dat versleuteling is toegepast.


Dit label van "CoinJoin output Coin" kan de fungibiliteit van een UTXO beïnvloeden. Gereguleerde entiteiten, zoals Exchange platforms, kunnen weigeren een UTXO te accepteren die een CoinJoin heeft ondergaan, of zelfs uitleg vragen aan de eigenaar, met het risico dat hun account wordt geblokkeerd of fondsen worden bevroren. In sommige gevallen kan het platform je gedrag zelfs rapporteren aan de staatsautoriteiten.


Dit is waar de Ricochet-methode om de hoek komt kijken. Om de voetafdruk van een CoinJoin te vervagen, voert Ricochet vier opeenvolgende transacties uit waarbij de gebruiker zijn geld naar zichzelf overmaakt op verschillende adressen. Na deze reeks transacties routeert de Ricochet-tool de bitcoins uiteindelijk naar hun eindbestemming, zoals een Exchange platform. Het doel is om afstand te creëren tussen de oorspronkelijke CoinJoin transactie en de uiteindelijke bestedingshandeling. Op deze manier zullen ketenanalysetools denken dat er waarschijnlijk een overdracht van Ownership heeft plaatsgevonden na de CoinJoin, en dat het daarom niet nodig is om actie te ondernemen tegen de verzender.


![ricochet diagram](assets/en/1.webp)


Met het oog op de Ricochet-methode zou men zich kunnen voorstellen dat software voor ketenanalyse hun onderzoek zou verdiepen tot meer dan vier stuiters. Deze platforms staan echter voor een dilemma bij het optimaliseren van de detectiedrempel. Ze moeten een grens stellen aan het aantal hops waarna ze toegeven dat er waarschijnlijk een verandering van eigenschap heeft plaatsgevonden en dat de link met een eerdere CoinJoin genegeerd moet worden. Het bepalen van deze drempel is echter riskant: elke uitbreiding van het waargenomen aantal hops verhoogt exponentieel het aantal valse positieven, d.w.z. individuen die ten onrechte gemarkeerd worden als deelnemers aan een CoinJoin, terwijl de operatie in werkelijkheid door iemand anders werd uitgevoerd. Dit scenario vormt een groot risico voor deze bedrijven, omdat fout-positieven tot ontevredenheid leiden, wat getroffen klanten naar de concurrentie kan drijven. Op de lange termijn leidt een te ambitieuze drempel ertoe dat een platform meer klanten verliest dan zijn concurrenten, wat zijn levensvatbaarheid in gevaar kan brengen. Het is daarom ingewikkeld voor deze platforms om het aantal waargenomen bounces te verhogen, en 4 is vaak voldoende om hun analyses te weerleggen.


Het meest voorkomende gebruik van Ricochet doet zich dus voor wanneer het nodig is om een eerdere deelname aan een CoinJoin te verbergen op een UTXO die van jou is**. Idealiter is het het beste om te voorkomen dat bitcoins die een CoinJoin hebben ondergaan, worden overgedragen aan gereguleerde entiteiten. Maar in het geval dat er geen andere optie is, vooral als er dringend bitcoins moeten worden omgezet in fiatvaluta, biedt Ricochet een effectieve oplossing.


## Hoe werkt Ricochet op Samourai Wallet?

Ricochet is simpelweg een methode waarbij men bitcoins naar zichzelf stuurt. Het is daarom heel goed mogelijk om handmatig een Ricochet te simuleren zonder een gespecialiseerde tool te gebruiken. Echter, voor degenen die het proces willen automatiseren en tegelijkertijd willen profiteren van een meer gepolijst resultaat, is de Ricochet-tool die beschikbaar is via de Samourai Wallet applicatie een goede oplossing.


Omdat de dienst wordt betaald in Samourai, kost een Ricochet `100.000 Sats` als dienstverleningskosten, bovenop de Mining kosten. Het gebruik ervan wordt dus meer aanbevolen voor transfers van aanzienlijke bedragen.


De applicatie Samourai biedt twee varianten van Ricochet:


- De versterkte Ricochet, of "gespreide levering", biedt het voordeel van het spreiden van de Samourai servicekosten over vijf opeenvolgende transacties. Deze optie zorgt er ook voor dat elke transactie op een ander tijdstip wordt uitgezonden en in een ander blok wordt opgenomen, wat het gedrag van een verandering van Ownership goed nabootst. Hoewel deze methode langzamer is, verdient ze de voorkeur voor mensen die geen haast hebben, omdat ze de efficiëntie van Ricochet maximaliseert door de weerstand tegen ketenanalyse te vergroten.
- De klassieke Ricochet, die is ontworpen om de operatie snel uit te voeren door alle transacties binnen een kort tijdsinterval uit te zenden. Deze methode biedt daarom minder privacy en minder weerstand tegen analyse in vergelijking met de versterkte methode. Deze methode verdient alleen de voorkeur bij dringende overdrachten.


## Hoe voer je een Ricochet uit op Samourai Wallet?

Om een Ricochet transactie uit te voeren vanuit de Samourai Wallet applicatie, volg je onze video tutorial:

![Ricochet YouTube video tutorial](https://youtu.be/Gsz0zuVo3N4)


Als je de Ricochet-transacties wilt bestuderen die in deze tutorial zijn uitgevoerd, zie je ze hier:


- De eerste Ricochet-transactie: [8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc](https://Mempool.space/fr/Testnet/tx/8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc)
- De laatste Ricochet-transactie: [27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777](https://Mempool.space/fr/Testnet/tx/27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777)


**Externe bronnen:**


- https://docs.samourai.io/en/Wallet/features/ricochet