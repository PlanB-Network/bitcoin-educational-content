---
term: Unix-tijd
definition: Aantal seconden verstreken sinds 1 januari 1970 om middernacht UTC, gebruikt voor tijdbeheer op Bitcoin.
---

Unix Time of Unix Timestamp staat voor het aantal seconden dat is verstreken sinds 1 januari 1970, om middernacht UTC (Unix Epoch). Dit systeem wordt gebruikt in Unix besturingssystemen en afgeleiden om de tijd op een universele en gestandaardiseerde manier aan te geven. Het maakt de synchronisatie van klokken en het beheer van tijdgebaseerde gebeurtenissen mogelijk, ongeacht tijdzones.


In de context van Bitcoin wordt het gebruikt voor de lokale klok van knooppunten en dus voor de berekening van NAT (Network-Adjusted Time). De voor het netwerk gecorrigeerde tijd is een mediaan van de knooppunttijden die lokaal door elk knooppunt zijn berekend, en deze referentie wordt dan gebruikt om de geldigheid van bloktijdstempels te verifiëren. Om een blok door een knooppunt te laten accepteren, moet de Timestamp tussen de MTP (Median Time Past van de laatste 11 gemijnde blokken) en de NAT plus 2 uur liggen:


```text
MTP < Valid Timestamp < (NAT + 2h)
```


Unix Time wordt ook gebruikt om timelocks te maken als ze gebaseerd zijn op de echte tijd in plaats van op een aantal blokken.