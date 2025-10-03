---
name: Stonewall x2
description: Stonewall x2-transacties begrijpen en gebruiken
---
![cover stonewall x2](assets/cover.webp)


***WAARSCHUWING:** Na de arrestatie van de oprichters van Samourai Wallet en de inbeslagname van hun servers op 24 april, functioneren Stonewallx2 transacties alleen nog door handmatig PSBT's uit te wisselen tussen de betrokken partijen, mits beide gebruikers verbonden zijn met hun eigen Dojo. Het is echter mogelijk dat deze tools in de komende weken opnieuw worden gelanceerd. In de tussentijd kun je nog steeds dit artikel raadplegen om de theoretische werking van Stonewallx2 te begrijpen en te leren hoe je ze handmatig kunt uitvoeren.*


als je overweegt om handmatig een Stonewallx2 uit te voeren, dan lijkt de procedure erg op de procedure die in deze handleiding wordt beschreven. Het belangrijkste verschil zit in de keuze van het type Stonewallx2 transactie: in plaats van `Online` te selecteren, klik je op `In Person / Manual`. Vervolgens moet u handmatig Exchange de PSBT's om de Stonewallx2 transactie te construeren. Als je fysiek dicht bij je medewerker bent, kun je de QR-codes achtereenvolgens scannen. Als je op afstand bent, kunnen JSON-bestanden worden uitgewisseld via een beveiligd communicatiekanaal. De rest van de tutorial blijft ongewijzigd._


we volgen de ontwikkelingen van deze zaak en de ontwikkelingen met betrekking tot de bijbehorende tools op de voet. Wees gerust dat we deze handleiding zullen bijwerken zodra er nieuwe informatie beschikbaar is._


deze handleiding is alleen bedoeld voor educatieve en informatieve doeleinden. We keuren het gebruik van deze tools voor criminele doeleinden niet goed en moedigen dit ook niet aan. Het is de verantwoordelijkheid van elke gebruiker om te voldoen aan de wetten in hun rechtsgebied._


---

> *Maak van elke uitgave een CoinJoin.*

## Wat is een Stonewall x2 transactie?


Stonewall x2 is een specifieke vorm van Bitcoin transactie gericht op het verhogen van de privacy van gebruikers tijdens een uitgave, door samen te werken met een derde partij die niet betrokken is bij die uitgave. Deze methode simuleert een mini-CoinJoin tussen twee deelnemers, terwijl er een betaling wordt gedaan aan een derde partij. Stonewall x2 transacties zijn beschikbaar op zowel de Samourai Wallet applicatie als de Sparrow wallet software. Beide zijn interoperabel.


De werking is relatief eenvoudig: we gebruiken een UTXO in ons bezit om de betaling te doen en roepen de hulp in van een derde partij die ook bijdraagt met een UTXO van zichzelf. De transactie resulteert in vier uitgangen: twee van gelijke bedragen, één bestemd voor de Address van de ontvanger van de betaling, de andere voor een Address van de medewerker. Een derde UTXO wordt teruggestuurd naar een andere Address van de medewerker, zodat zij het oorspronkelijke bedrag kunnen ophalen (een neutrale actie voor hen, modulo Mining kosten), en een laatste UTXO gaat terug naar een Address van ons, die het wisselgeld van de betaling vormt.


Er worden dus drie verschillende rollen gedefinieerd in Stonewall x2 transacties:


- De verzender, die de betaling uitvoert;
- De medewerker, die bitcoins levert om de algehele anonimiteit van de transactie te verbeteren, terwijl hij zijn geld aan het einde volledig terugkrijgt (een neutrale actie voor hen, modulo Mining vergoedingen);
- De ontvanger, die zich mogelijk niet bewust is van de specifieke aard van de transactie en gewoon een betaling verwacht van de verzender.


Laten we een voorbeeld nemen om het beter te begrijpen. Alice is bij de bakker om haar stokbrood te kopen, dat `4.000 Sats` kost. Ze wil in bitcoins betalen en toch een zekere mate van privacy voor haar betaling behouden. Daarom doet ze een beroep op haar vriend Bob, die haar hierbij zal helpen.

![schema stonewall x2](assets/en/1.webp)

Door deze transactie te analyseren, kunnen we zien dat de bakker inderdaad `4.000 Sats` heeft ontvangen als betaling voor het stokbrood. Alice gebruikte `10.000 Sats` als input en ontving `6.000 Sats` als output, wat resulteerde in een netto saldo van `-4.000 Sats`, wat overeenkomt met de prijs van het stokbrood. Bob gebruikte `15.000 Sats` als input en ontving twee outputs: een van `4.000 Sats` en de andere van `11.000 Sats`, resulterend in een saldo van `0`.

In dit voorbeeld heb ik opzettelijk de Mining kosten verwaarloosd voor een beter begrip. In werkelijkheid worden transactiekosten gelijkelijk verdeeld tussen de verzender van de betaling en de medewerker.


## Wat is het verschil tussen Stonewall en Stonewall x2?


Een StonewallX2 transactie werkt precies hetzelfde als een Stonewall transactie, behalve dat de eerste gezamenlijk is en de laatste niet. Zoals we hebben gezien, is er bij een StonewallX2-transactie een derde partij betrokken die buiten de betaling staat en die zijn bitcoins ter beschikking stelt om de privacy van de transactie te verbeteren. In een typische Stonewall-transactie wordt de rol van medewerker gespeeld door de verzender.


Laten we ons voorbeeld van Alice in de bakkerij nog eens bekijken. Als ze niet iemand als Bob kon vinden om haar te vergezellen in haar uitgave, had ze in haar eentje een Stonewall-transactie kunnen doen. Zo zouden de twee UTXO's aan de ingang van haar zijn geweest en zou ze er 3 hebben ontvangen aan de uitgang.

![transaction stonewall](assets/en/2.webp)


Vanuit extern oogpunt zou het transactiepatroon hetzelfde zijn gebleven.

![Stonewall or Stonewall x2?](assets/en/5.webp)

Daarom moet de logica er als volgt uitzien bij het gebruik van een Samourai-bestedingstool:


- Als de handelaar PayJoin Stowaway niet ondersteunt, kan een gezamenlijke transactie worden gedaan met een andere persoon buiten de betaling met behulp van Stonewall x2.
- Als niemand wordt gevonden om een Stonewall x2 transactie te doen, kan een Stonewall transactie alleen worden gedaan, waarbij het gedrag van een Stonewall x2 transactie wordt nagebootst.
- De laatste optie zou zijn om een transactie te doen met JoinBot, een server die wordt onderhouden door Samourai, die op verzoek kan optreden als de medewerker in een Stonewall x2 transactie.


Als je een medewerker wilt vinden die bereid is om je te helpen bij een Stonewall X2-transactie, kun je ook deze Telegram-groep (onofficieel) bezoeken die wordt onderhouden door Samourai-gebruikers om verzenders en medewerkers met elkaar in contact te brengen: [Maak van elke uitgave een CoinJoin](https://t.me/EverySpendACoinjoin).


[**-> Meer informatie over Stonewall-transacties**](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


## Wat is het doel van een Stonewall x2 transactie?


De Stonewall x2 structuur voegt een aanzienlijke hoeveelheid entropie toe aan de transactie en verwart de ketenanalyse. Van buitenaf kan zo'n transactie worden geïnterpreteerd als een kleine CoinJoin tussen twee individuen. Maar in werkelijkheid is het een betaling. Deze methode genereert onzekerheden in de ketenanalyse en leidt zelfs tot valse aanwijzingen.


Laten we teruggaan naar het voorbeeld van Alice, Bob en de Baker. De transactie op de Blockchain zou er als volgt uitzien:

![stonewall x2 public](assets/en/3.webp)

Een externe waarnemer die vertrouwt op algemene ketenanalyse heuristieken zou ten onrechte kunnen concluderen dat "Alice en Bob een kleine CoinJoin uitvoerden, met elk een UTXO als invoer en elk twee UTXO's als uitvoer."![misinterpretatie stonewall x2](assets/nl/4.webp)

Deze interpretatie is onjuist omdat, zoals je weet, een UTXO naar de Baker werd gestuurd, Alice slechts één wisseluitgang heeft en Bob er twee heeft.

![transaction stonewall x2](assets/en/1.webp)

Zelfs als de externe waarnemer erin slaagt om het patroon van de Stonewall x2 transactie te identificeren, zal hij niet over alle informatie beschikken. Ze kunnen niet bepalen welke van de twee UTXO's met dezelfde bedragen overeenkomt met de betaling. Bovendien kunnen ze niet weten of Alice of Bob de betaling heeft gedaan. Ten slotte zullen ze niet kunnen bepalen of de twee ingevoerde UTXO's van twee verschillende personen afkomstig zijn of dat ze toebehoren aan één persoon die ze heeft samengevoegd. Dit laatste is te wijten aan het feit dat klassieke Stonewall transacties, die we hierboven hebben besproken, precies hetzelfde patroon volgen als Stonewall x2 transacties. Van buitenaf en zonder aanvullende informatie over de context is het onmogelijk om een Stonewall transactie te onderscheiden van een Stonewall x2 transactie. De eerstgenoemde zijn echter geen collaboratieve transacties, terwijl de laatstgenoemde dat wel zijn. Dit geeft nog meer twijfels over deze uitgave.

![Stonewall or Stonewall x2 ?](assets/en/5.webp)



## Hoe maak je een verbinding tussen Paynyms om te kunnen samenwerken via Soroban?


Net als bij andere collaboratieve transacties op Samourai (*Cahoots*), omvat het uitvoeren van een Stonewall x2 de Exchange van gedeeltelijk ondertekende transacties tussen de verzender en de collaborator. Deze Exchange kan handmatig worden gedaan, als je fysiek bij je medewerker bent, of automatisch via het Soroban communicatieprotocol.


Als je voor de tweede optie kiest, moet je een verbinding tussen Paynyms tot stand brengen voordat je een Stonewall x2 kunt uitvoeren. Om dit te doen, moet jouw Paynym de Paynym van je collega "volgen" en vice versa.


**Toegang krijgen tot het Paynym van de medewerker:**


Om te beginnen is het nodig om de betaalcode van de Paynym van je medewerker te verkrijgen. In de Samourai Wallet applicatie, moet je medewerker op het icoontje van zijn Paynym (het robotje) linksboven in het scherm drukken, klik dan op zijn Paynym nickname, beginnend met `+...`. De mijne is bijvoorbeeld `+namelessmode0aF`.


![samourai paynym](assets/notext/6.webp)

Als je medewerker Sparrow wallet gebruikt, moet hij klikken op het tabblad 'Extra' en dan op 'PayNym weergeven'.![paynym Sparrow](assets/notext/7.webp)

**Volg de PayNym van je medewerker uit Samourai Wallet:**


Als je Samourai Wallet gebruikt, start dan de applicatie en ga op dezelfde manier naar het menu 'PayNyms'. Als dit de eerste keer is dat u uw PayNym gebruikt, moet u de identificatie ervan verkrijgen.


![request paynym samourai](assets/notext/8.webp)


Klik vervolgens op de blauwe '+' rechtsonder in het scherm.

![add collaborator paynym](assets/notext/9.webp)

Je kunt dan de betaalcode van je medewerker plakken door 'PASTE PAYMENT CODE' te selecteren, of de camera openen om hun QR-code te scannen door op 'SCAN QR CODE' te drukken.

![paste paynym identifier](assets/notext/10.webp)


Klik op de knop 'VOLG'.

![follow paynym](assets/notext/11.webp)

Bevestig door op 'YES' te klikken.

![confirm follow paynym](assets/notext/12.webp)

De software zal je dan een knop 'CONNECT' aanbieden. Voor onze handleiding is het niet nodig om op deze knop te klikken. Deze stap is alleen nodig als je van plan bent om betalingen te doen aan de andere PayNym als onderdeel van de BIP47, wat niet gerelateerd is aan onze handleiding.

![connect paynym](assets/notext/13.webp)

Zodra je PayNym de PayNym van je medewerker volgt, herhaal je dit proces in omgekeerde richting zodat je medewerker jou ook kan volgen. U kunt dan een Stonewall x2 transactie uitvoeren.


**Volg de PayNym van je medewerker van Sparrow wallet:**


Als u Sparrow wallet gebruikt, open dan uw Wallet en ga naar het menu 'Toon PayNym'. Als u uw PayNym voor de eerste keer gebruikt, moet u een identifier verkrijgen door op 'Retrieve PayNym' te klikken.

![request paynym sparrow](assets/notext/14.webp)

Voer vervolgens de PayNym-identificatie van uw medewerker in (hun bijnaam '+...' of hun betalingscode 'PM...') in het vak 'Contactpersoon zoeken' en klik op de knop 'Contactpersoon toevoegen'.

![add contact paynym](assets/notext/15.webp)

De software biedt je dan een knop 'Link Contact'. Voor onze handleiding is het niet nodig om op deze knop te klikken. Deze stap is alleen nodig als je van plan bent om betalingen te doen aan de aangegeven PayNym als onderdeel van de BIP47, wat niets te maken heeft met onze handleiding.


Zodra je PayNym de PayNym van je medewerker volgt, herhaal je dit proces in omgekeerde richting zodat je medewerker jou ook kan volgen. U kunt dan een Stonewall x2 transactie uitvoeren.

## Hoe maak je een Stonewall x2 transactie op Samourai Wallet?


Als je de vorige stappen van het verbinden van Paynyms hebt voltooid, ben je eindelijk klaar om de Stonewall x2 transactie te doen! Volg hiervoor onze video tutorial over Samourai Wallet:

![Stonewall x2 Tutorial - Samourai Wallet](https://youtu.be/89oYE1Hw3Fk?si=QTqUZ6IypiR6PPMr)


## Hoe maak je een Stonewall x2 transactie op Sparrow wallet?


Als je de vorige stappen van het aansluiten van Paynyms hebt voltooid, ben je eindelijk klaar om de Stonewall x2 transactie te doen! Volg hiervoor onze video tutorial op Sparrow wallet:

![Stonewall x2 Tutorial - Sparrow Wallet](https://youtu.be/mO3Xpp34Hhk?si=bfYiTl0Gxjs9sNQq)


**Externe bronnen:**


- https://sparrowwallet.com/docs/spending-privately.html;
- https://docs.samourai.io/en/spend-tools#stonewallx2.