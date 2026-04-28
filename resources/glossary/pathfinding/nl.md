---
term: Pathfinding
definition: Proces van het bepalen van het optimale pad voor het routeren van een betaling op het Lightning Netwerk.
---

Proces dat door een knooppunt wordt gebruikt om het optimale pad te bepalen voor het routeren van een betaling door het netwerk van Lightning-kanalen. Pathfinding wordt uitgevoerd door het knooppunt van de betaler, dat de meest geschikte tussenliggende knooppunten moet selecteren om de ontvanger te bereiken. Deze keuze is gebaseerd op een aantal criteria, zoals vergoedingen, kanaalcapaciteit en tijdsloten.


Pathfinding-algoritmen maken een grafiek van de netwerktopologie op basis van de roddelgegevens en evalueren de verschillende mogelijke routes tussen het knooppunt van de betaler en dat van de ontvanger. Deze routes worden gerangschikt van best naar slechtst volgens verschillende criteria. Het knooppunt test vervolgens deze routes tot het erin slaagt om de betaling via een van de routes uit te voeren.