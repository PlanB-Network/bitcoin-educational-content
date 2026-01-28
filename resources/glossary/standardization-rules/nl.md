---
term: Standardisatieregels
definition: Lokale regels die de structuur definiëren van onbevestigde transacties die een node in zijn mempool accepteert.
---

Standaardisatieregels worden individueel aangenomen door elk Bitcoin knooppunt, naast de consensusregels, om de structuur van onbevestigde transacties te definiëren die het accepteert in zijn Mempool en uitzendt naar zijn peers. Deze regels worden dus lokaal door elk knooppunt geconfigureerd en uitgevoerd en kunnen van knooppunt tot knooppunt verschillen. Ze zijn uitsluitend van toepassing op onbevestigde transacties. Daarom zal een knooppunt een transactie die het als niet-standaard beschouwt alleen accepteren als deze al is opgenomen in een geldig blok.


Opgemerkt wordt dat de meerderheid van de knooppunten de standaardconfiguraties zoals vastgesteld in Bitcoin core laat staan, waardoor een uniformiteit van standaardisatieregels over het netwerk ontstaat. Een transactie die weliswaar voldoet aan de consensusregels, maar niet aan deze standaardisatieregels, zal moeite hebben om uitgezonden te worden over het netwerk. Het kan echter nog steeds worden opgenomen in een geldig blok als het een Miner bereikt. In de praktijk worden deze transacties, die "niet-standaard" worden genoemd, vaak rechtstreeks naar een Miner verzonden via externe middelen buiten het Bitcoin peer-to-peer netwerk. Dit is vaak de enige manier om dit soort transacties te bevestigen.


Bijvoorbeeld, een transactie die geen vergoedingen toekent is zowel geldig volgens de consensusregels als niet-standaard omdat het standaardbeleid van Bitcoin core voor de `minRelayTxFee` parameter `0.00001` is (in BTC/kB).


> ► *De term "Mempool regels" wordt soms ook gebruikt om te verwijzen naar de standaardisatieregels.*