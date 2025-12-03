---
name: Ashigaru - Ricochet
description: Ricochet-transacties begrijpen en gebruiken
---
![cover ricochet](assets/cover.webp)



> *Een hoogwaardige tool die extra geschiedenis toevoegt aan je transactie. Stomp de blacklists en help te beschermen tegen onterechte sluitingen van accounts van derden.*

## Wat is een Ricochet?



Ricochet is een techniek die bestaat uit het uitvoeren van verschillende fictieve transacties naar zichzelf om een overdracht van bitcoin-eigendom te simuleren. Deze tool verschilt van Ashigaru's andere transacties (geërfd van Samurai Wallet) omdat het geen prospectieve anonimiteit biedt, maar eerder een vorm van retrospectieve anonimiteit. In feite vervaagt Ricochet de specifieke kenmerken die de fungibiliteit van een Bitcoin deel in gevaar kunnen brengen.



Als je bijvoorbeeld een coinjoin uitvoert, wordt het onderdeel dat uit de mix komt als zodanig geïdentificeerd. Tools voor ketenanalyse zijn in staat om de paterns van coinjoin-transacties te detecteren en een label toe te kennen aan de stukken die eruit komen. In feite is coinjoin erop gericht om de historische verbanden van een munt te verbreken, maar zijn doorgang door coinjoins blijft detecteerbaar. Bij wijze van analogie is dit fenomeen verwant aan de versleuteling van een tekst: hoewel de originele tekst niet toegankelijk is in onbewerkte tekst, is het eenvoudig om vast te stellen dat er versleuteling is toegepast.



Het label "coinjoined" kan de fungibiliteit van een UTXO beïnvloeden. Gereguleerde entiteiten, zoals exchange platforms, kunnen weigeren om een coinjoined UTXO te accepteren, of zelfs uitleg eisen van de eigenaar, met het risico dat je account wordt geblokkeerd of je fondsen worden bevroren. In sommige gevallen kan het platform je gedrag zelfs rapporteren aan de overheidsinstanties.



Dit is waar de Ricochet-methode om de hoek komt kijken. Om de afdruk van een coinjoin te vervagen, voert Ricochet vier opeenvolgende transacties uit waarbij de gebruiker zijn geld naar zichzelf overmaakt op verschillende adressen. Na deze reeks transacties routeert de Ricochet-tool de bitcoins uiteindelijk naar hun eindbestemming, zoals een uitwisselingsplatform. Het doel is om afstand te creëren tussen de oorspronkelijke coinjoin-transactie en de uiteindelijke besteding. Op deze manier gaan blockchain analysetools ervan uit dat er waarschijnlijk een eigendomsoverdracht heeft plaatsgevonden na de coinjoin, en dat er daarom geen actie hoeft te worden ondernomen tegen de uitgever.



![image](assets/fr/01.webp)



Bij de Ricochet-methode zou je kunnen denken dat software voor ketenanalyse het onderzoek zou verdiepen tot meer dan vier stuiters. Deze platforms staan echter voor een dilemma bij het optimaliseren van de detectiedrempel. Ze moeten een drempelaantal hops bepalen waarna ze accepteren dat er waarschijnlijk een verandering van eigenaar heeft plaatsgevonden en dat de link naar een eerdere coinjoin moet worden genegeerd. Het bepalen van deze drempel is echter riskant: elke uitbreiding van het aantal waargenomen sprongen verhoogt exponentieel het aantal fout-positieven, d.w.z. individuen die ten onrechte worden gemarkeerd als deelnemers aan een coinjoin, terwijl de operatie in feite door iemand anders werd uitgevoerd. Dit scenario vormt een groot risico voor deze bedrijven, omdat fout-positieven tot ontevredenheid leiden, waardoor getroffen klanten naar de concurrentie kunnen overstappen. Op de lange termijn leidt een te ambitieuze detectiedrempel ertoe dat een platform meer klanten verliest dan zijn concurrenten, wat zijn levensvatbaarheid in gevaar kan brengen. Daarom is het voor deze platforms ingewikkeld om het aantal waargenomen bounces te verhogen, en 4 is vaak voldoende om hun analyses tegen te gaan.



Het meest voorkomende gebruik van Ricochet doet zich dus voor wanneer het nodig is om een eerdere deelname aan een coinjoin op een UTXO waarvan u de eigenaar bent, te verbergen.** Idealiter is het het beste om te voorkomen dat bitcoins die een coinjoin hebben ondergaan, worden overgedragen aan gereguleerde entiteiten. Niettemin, in het geval dat er geen andere optie overblijft, met name in de dringende noodzaak om bitcoins in staatsvaluta te liquideren, biedt Ricochet een effectieve oplossing.



## Hoe werkt Ricochet op Ashigaru?



Ricochet is simpelweg een methode om bitcoins naar jezelf te versturen, oorspronkelijk uitgevonden door de ontwikkelaars van Samurai Wallet. Het is daarom heel goed mogelijk om handmatig een Ricochet te simuleren, zonder dat daar een gespecialiseerde tool voor nodig is. Voor degenen die het proces echter willen automatiseren en tegelijkertijd willen genieten van een meer gepolijst resultaat, is de Ricochet-tool die beschikbaar is via de Ashigaru-toepassing (die een Samourai fork is) een goede oplossing.



Omdat Ashigaru geld vraagt voor zijn service, kost een Ricochet `100.000 sats` als servicekosten, plus een mining vergoeding. Het gebruik ervan wordt daarom aanbevolen voor overdrachten van grote bedragen.



De Ashigaru-toepassing biedt twee Ricochet-varianten:





- Versterkte Ricochet, of "gespreide levering", die het voordeel biedt van het spreiden van Ashigaru's servicekosten over de vijf opeenvolgende transacties. Deze optie zorgt er ook voor dat elke transactie op een apart tijdstip wordt uitgezonden en in een ander blok wordt vastgelegd, waardoor het gedrag van een verandering van eigenaar zo goed mogelijk wordt nagebootst. Hoewel deze methode langzamer is, verdient ze de voorkeur voor mensen die geen haast hebben, omdat ze de efficiëntie van Ricochet maximaliseert door de weerstand tegen ketenanalyse te versterken;





- De klassieke Ricochet, die is ontworpen om de operatie snel uit te voeren, zendt alle transacties uit in een kort tijdsinterval. Deze methode biedt daarom minder vertrouwelijkheid en minder weerstand tegen analyse dan de versterkte methode. Deze methode mag alleen worden gebruikt voor dringende zendingen.



## Hoe maak je een Ricochet op Ashigaru?



Het maken van een ricochet op Ashigaru is heel eenvoudig: activeer gewoon de corresponderende optie bij het maken van een verzendtransactie. Om te beginnen klik je op de `+` knop, dan op `Versturen`, en selecteer je de rekening waarvan je het geld wilt versturen.



![Image](assets/fr/02.webp)



Vul de transactiegegevens in: het te verzenden bedrag en het uiteindelijke adres van de ontvanger na de Ricochet-sprongen. Vink dan de optie `Ricochet` aan.



![Image](assets/fr/03.webp)



Je kunt dan kiezen tussen de twee Ricochet-modi die in het theoriegedeelte zijn besproken: ofwel klassiek Ricochet, waarbij alle transacties in hetzelfde blok worden opgenomen, of gespreide levering, wat de Ricochet-kwaliteit verbetert ten koste van een langere vertraging.



Zodra je je keuze hebt gemaakt, druk je op de pijl onderaan het scherm om te bevestigen.



![Image](assets/fr/04.webp)



Op het volgende scherm zie je een volledige samenvatting van je transactie. Hier kun je ook het tarief voor je Ricochet-transacties aanpassen aan de marktomstandigheden. Als alles naar wens is, sleep je de groene pijl om Ricochet-transacties te ondertekenen en te verdelen.



![Image](assets/fr/05.webp)



Wacht terwijl de verschillende sprongen automatisch worden uitgevoerd.



![Image](assets/fr/06.webp)



Je transacties zijn succesvol uitgezonden.



![Image](assets/fr/07.webp)



Je bent nu volledig vertrouwd met de Ricochet-optie die beschikbaar is in de Ashigaru-applicatie. Om verder te gaan, raad ik je aan mijn BTC 204 training te volgen, die je in detail zal leren hoe je je onchain vertrouwelijkheid kunt versterken.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c