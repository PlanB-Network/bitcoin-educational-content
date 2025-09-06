---
name: Stonewall
description: Inzicht in en gebruik van Stonewall-transacties
---
![cover stonewall](assets/cover.webp)


***WAARSCHUWING:** Na de arrestatie van de oprichters van Samourai Wallet en de inbeslagname van hun servers op 24 april, vereist het gebruik van de Samourai Wallet app nu een verbinding met je eigen Dojo om goed te functioneren. Afgezien hiervan worden Stonewall-transacties helemaal niet beïnvloed en kunnen ze nog steeds zonder problemen worden uitgevoerd. Dit soort transacties worden namelijk autonoom uitgevoerd, zonder de noodzaak voor externe samenwerking of verbinding via Soroban.*


we volgen de ontwikkelingen van deze zaak en de ontwikkelingen met betrekking tot de bijbehorende tools op de voet. Wees gerust dat we deze handleiding zullen bijwerken zodra er nieuwe informatie beschikbaar is._


deze handleiding is alleen bedoeld voor educatieve en informatieve doeleinden. We keuren het gebruik van deze tools voor criminele doeleinden niet goed en moedigen dit ook niet aan. Het is de verantwoordelijkheid van elke gebruiker om te voldoen aan de wetten in hun rechtsgebied._


---

> *Doorbreek de aannames van Blockchain analyse met wiskundig bewijsbare twijfel tussen verzender en ontvanger van je transacties.*

## Wat is een Stonewall-transactie?

Stonewall is een specifieke vorm van Bitcoin transactie gericht op het verhogen van de privacy van gebruikers tijdens een transactie door een CoinJoin tussen twee partijen na te bootsen, zonder er daadwerkelijk een te zijn. In feite werkt deze transactie niet samen. Een gebruiker kan hem alleen maken, met alleen zijn eigen UTXO's als invoer. Daarom kun je voor elke gelegenheid een Stonewall transactie maken zonder dat je hoeft te coördineren met een andere gebruiker.


De werking van een Stonewall-transactie is als volgt: als invoer gebruikt de zender 2 UTXO's die bij hem horen. Als uitvoer produceert de transactie 4 uitgangen, waarvan er 2 precies hetzelfde bedrag zijn. De andere 2 zijn wisselgeld. Van de 2 uitgangen van hetzelfde bedrag gaat er slechts één daadwerkelijk naar de ontvanger van de betaling.


Er zijn slechts 2 rollen in een Stonewall-transactie:


- De verzender, die de betaling uitvoert;
- De ontvanger, die zich mogelijk niet bewust is van de specifieke aard van de transactie en gewoon een betaling verwacht van de verzender.


Laten we een voorbeeld nemen om deze transactiestructuur te begrijpen. Alice is bij de bakker om haar stokbrood te kopen, dat `4.000 Sats` kost. Ze wil in bitcoins betalen en toch een bepaalde mate van privacy behouden bij haar betaling. Daarom besluit ze een Stonewall-transactie aan te maken voor de betaling.

![transaction stonewall bakery](assets/en/1.webp)

Als we deze transactie analyseren, zien we dat de bakker inderdaad `4.000 Sats` ontving als betaling voor het stokbrood. Alice gebruikte 2 UTXO's als input: één van `10.000 Sats` en één van `15.000 Sats`. Als output ontving ze 3 UTXO's: één van `4.000 Sats`, één van `6.000 Sats` en één van `11.000 Sats`. Alice heeft een nettosaldo van `-4.000 Sats` in deze transactie, wat overeenkomt met de prijs van het stokbrood.


In dit voorbeeld heb ik opzettelijk de Mining kosten weggelaten voor een beter begrip. In werkelijkheid worden transactiekosten volledig gedekt door de verzender.


## Wat is het verschil tussen Stonewall en Stonewall x2?

De Stonewall-transactie werkt op dezelfde manier als de StonewallX2-transactie, met als enige verschil dat deze laatste samenwerking vereist, in tegenstelling tot de klassieke Stonewall-transactie, vandaar de "x2"-aanduiding. De Stonewall-transactie kan namelijk worden uitgevoerd zonder dat externe samenwerking vereist is: de verzender kan deze uitvoeren zonder de hulp van een andere persoon. Echter, voor een Stonewall x2 transactie, voegt een extra deelnemer, genaamd de "collaborator", zich bij het proces. De medewerker draagt zijn eigen bitcoins bij als input, naast die van de verzender, en ontvangt het hele bedrag als output (minus Mining kosten).


Laten we ons voorbeeld met Alice in de bakkerij nog eens bekijken. Als ze een Stonewall x2-transactie had willen doen, had Alice bij het maken van de transactie moeten samenwerken met Bob (een derde partij). Ze zouden elk een input UTXO hebben gegeven. Bob zou dan het volledige bedrag van zijn input als output hebben ontvangen. De bakker zou op dezelfde manier als bij de Stonewall-transactie betaald zijn voor zijn stokbrood, terwijl Alice haar oorspronkelijke saldo zou hebben teruggekregen, minus de kosten van het stokbrood.

![transaction stonewall x2](assets/en/2.webp)


Vanuit een extern perspectief zou het patroon van de transactie precies hetzelfde zijn gebleven.

![Stonewall or Stonewall x2 ?](assets/en/3.webp)


Samengevat hebben Stonewall- en Stonewall x2-transacties een identieke structuur. Het verschil tussen de twee ligt in hun samenwerkingskarakter. De Stonewall-transactie wordt individueel ontwikkeld, zonder dat samenwerking nodig is. De Stonewall x2-transactie daarentegen is afhankelijk van samenwerking tussen twee individuen voor de uitvoering ervan.


[**-> Meer informatie over Stonewall x2 transacties**](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)


## Wat is het doel van een Stonewall-transactie?

De Stonewall-structuur voegt een aanzienlijke hoeveelheid entropie toe aan de transactie en vertroebelt de ketenanalyse. Vanuit een extern perspectief kan zo'n transactie worden geïnterpreteerd als een kleine CoinJoin tussen twee mensen. Maar in werkelijkheid is het, net als de Stonewall x2 transactie, een betaling. Deze methode creëert daarom onzekerheden in de ketenanalyse en kan zelfs leiden tot valse aanwijzingen.


Laten we het voorbeeld van Alice bij de bakkerij nog eens bekijken. De transactie op de Blockchain zou er als volgt uitzien:

![Stonewall or Stonewall x2 ?](assets/en/4.webp)

Een externe waarnemer die vertrouwt op de heuristiek van gewone ketenanalyse zou ten onrechte kunnen concluderen dat "*twee mensen hebben een kleine CoinJoin uitgevoerd, met elk een UTXO als invoer en elk twee UTXO's als uitvoer*".

![Stonewall or Stonewall x2 ?](assets/en/5.webp)

Deze interpretatie is onjuist omdat, zoals je weet, een UTXO naar de bakker werd gestuurd, de 2 UTXO's in de invoer afkomstig zijn van Alice, en ze 3 wisseluitgangen ontving.


![transaction stonewall baker](assets/en/1.webp)

Zelfs als een buitenstaander erin slaagt om het patroon van de Stonewall-transactie te identificeren, zal hij niet over alle informatie beschikken. Ze zullen niet kunnen bepalen welke van de twee UTXO's met dezelfde bedragen overeenkomt met de betaling. Bovendien kunnen ze niet bepalen of de twee UTXO's in de invoer afkomstig zijn van twee verschillende personen of dat ze toebehoren aan één persoon die ze heeft samengevoegd. Dit laatste is te wijten aan het feit dat Stonewall x2 transacties, waar we het hierboven over hadden, precies hetzelfde patroon volgen als Stonewall transacties. Van buitenaf en zonder aanvullende informatie over de context is het onmogelijk om een Stonewall transactie te onderscheiden van een Stonewall x2 transactie. De eerstgenoemde zijn echter geen collaboratieve transacties, terwijl de laatstgenoemde dat wel zijn. Dit geeft nog meer twijfels over deze uitgave.

![Stonewall or Stonewall x2 ?](assets/en/3.webp)

## Hoe maak je een Stonewall-transactie op Samourai Wallet?

In tegenstelling tot Stowaway of Stonewall x2 (cahoots) transacties, vereist de Stonewall transactie niet het gebruik van Paynyms. Het kan direct worden gedaan, zonder voorbereidende stappen. Volg hiervoor onze video tutorial op Samourai Wallet:

![Stonewall Tutorial - Samourai Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)


## Hoe maak je een Stonewall-transactie op Sparrow wallet?

In tegenstelling tot Stowaway of Stonewall x2 (cahoots) transacties, vereist de Stonewall transactie niet het gebruik van Paynyms. Het kan direct worden gedaan, zonder voorbereidende stappen. Volg hiervoor onze videotutorial op Sparrow wallet:

![Stonewall Tutorial - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)



**Externe bronnen:**


- https://docs.samourai.io/en/spend-tools#stonewall.