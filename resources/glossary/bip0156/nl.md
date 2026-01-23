---
term: BIP0156
definition: Dandelion, een protocol dat de privacy van transactierouting verbetert door de verzendende node te maskeren.
---

Voorstel, bekend als Dandelion, dat tot doel heeft de privacy van transactierouting in het Bitcoin netwerk te verbeteren om deanonimisering tegen te gaan. In de standaard operatie van Bitcoin, worden transacties onmiddellijk uitgezonden naar meerdere knooppunten. Als een waarnemer in staat is om elke transactie te zien die door elk knooppunt op het netwerk wordt doorgegeven, zou hij kunnen aannemen dat het eerste knooppunt dat een transactie verstuurt ook het knooppunt van herkomst van die transactie is, en dus dat de transactie afkomstig is van de operator van het knooppunt. Dit fenomeen zou waarnemers in staat kunnen stellen om transacties, die normaal gesproken anoniem zijn, te koppelen aan IP-adressen.


Het doel van BIP156 is om Address te maken van dit probleem. Om dit te doen, introduceert het een extra fase in de broadcast om de anonimiteit te bewaren voor de publieke verspreiding. Dus, Dandelion gebruikt eerst een "stam" fase waar de transactie door een willekeurig pad van knooppunten wordt gestuurd, voordat het wordt uitgezonden naar het hele netwerk in de "fluff" fase. De stam en pluis zijn verwijzingen naar het gedrag van de verspreiding van de transactie door het netwerk en lijken op de vorm van een paardenbloem (*a dandelion* in het Engels).


Deze routeringsmethode versluiert het spoor terug naar het bronknooppunt, waardoor het moeilijk wordt om een transactie door het netwerk terug te traceren naar de oorsprong. Dandelion verbetert dus de privacy door het vermogen van tegenstanders om het netwerk te deanonimiseren te beperken. Deze methode is nog effectiever als de transactie tijdens de "steel"-fase een knooppunt kruist dat zijn netwerkcommunicatie versleutelt, zoals met Tor of *P2P Transport V2*. BIP156 is nog niet toegevoegd aan Bitcoin core.