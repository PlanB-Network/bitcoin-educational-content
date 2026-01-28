---
term: Byzantijnse generaals probleem
definition: Probleem dat de uitdagingen van coördinatie illustreert in een gedistribueerd systeem waar actoren elkaar niet kunnen vertrouwen.
---

Het probleem werd voor het eerst geformuleerd door Leslie Lamport, Robert Shostak en Marshall Pease in het gespecialiseerde tijdschrift *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["The Byzantine Generals Problem"](https://lamport.azurewebsites.net/pubs/byz.pdf) in juli 1982. Het wordt vandaag de dag gebruikt om de uitdagingen te illustreren in termen van besluitvorming wanneer een gedistribueerd systeem geen enkele actor kan vertrouwen.


In deze metafoor kampeert een groep Byzantijnse generaals met hun legers rond een stad die ze willen aanvallen of belegeren. De generaals zijn geografisch van elkaar gescheiden en moeten via een boodschapper communiceren om hun strategie te coördineren. Het maakt niet uit of ze aanvallen of zich terugtrekken, zolang alle generaals maar tot een consensus komen.


Daarom kunnen we de volgende vereisten overwegen:


- Elke generaal moet een beslissing nemen: aanvallen of terugtrekken (ja of nee);
- Als de beslissing eenmaal is genomen, kan deze niet meer worden gewijzigd;
- Alle generaals moeten het eens zijn over dezelfde beslissing en deze synchroon uitvoeren.


Bovendien kan een generaal alleen met een andere generaal communiceren via berichten die door een koerier worden verzonden en die kunnen worden vertraagd, vernietigd, gewijzigd of verloren gaan. En zelfs als een bericht succesvol wordt afgeleverd, kunnen een of meer generaals ervoor kiezen (om welke reden dan ook) om het gevestigde vertrouwen te beschamen en een frauduleus bericht te sturen, waardoor chaos wordt gezaaid.


Als we het dilemma toepassen op de context van de Bitcoin Blockchain, dan vertegenwoordigt elke generaal een knooppunt in het netwerk, dat een consensus moet bereiken over de toestand van het systeem. Met andere woorden, de meerderheid van de deelnemers in een gedistribueerd netwerk moet het eens zijn en dezelfde actie uitvoeren om een totale mislukking te voorkomen. De enige manier om een consensus te bereiken in dit type gedistribueerd systeem is om minstens 2/3 van de netwerkknooppunten betrouwbaar en eerlijk te laten zijn. Daarom is het systeem kwetsbaar als de meerderheid van het netwerk besluit om kwaadwillig te handelen.


> ► *Dit dilemma wordt soms ook "Het probleem van betrouwbaar uitzenden" genoemd*