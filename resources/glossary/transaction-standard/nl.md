---
term: TRANSACTIESTANDAARD
---

Een Bitcoin transactie die, naast het naleven van de consensusregels, ook binnen de standaard standaardisatie regels valt die zijn ingesteld op Bitcoin core knooppunten. Deze standaardisatieregels worden individueel opgelegd door elk Bitcoin knooppunt, naast de consensusregels, om de structuur van onbevestigde transacties te definiëren die het accepteert in zijn Mempool en uitzendt naar zijn peers.


Deze regels worden dus door elk knooppunt lokaal geconfigureerd en uitgevoerd en kunnen per knooppunt verschillen. Ze zijn uitsluitend van toepassing op onbevestigde transacties. Daarom zal een knooppunt een transactie die het als niet-standaard beschouwt alleen accepteren als deze al is opgenomen in een geldig blok.


Opgemerkt wordt dat de meerderheid van de knooppunten de standaardconfiguraties zoals vastgesteld in Bitcoin core laat staan, waardoor een uniformiteit van standaardisatieregels over het netwerk ontstaat. Een transactie die, hoewel in overeenstemming met de consensusregels, deze standaardisatieregels niet respecteert, zal moeite hebben om zich door het netwerk te verspreiden. Het kan echter nog steeds worden opgenomen in een geldig blok als het een Miner bereikt. In de praktijk worden deze transacties, die als niet-standaard worden gekwalificeerd, vaak direct naar een Miner verzonden via externe middelen naar het Bitcoin peer-to-peer netwerk. Dit is vaak de enige manier om een dergelijke transactie te bevestigen. Bijvoorbeeld, een transactie die geen vergoedingen toekent is zowel geldig volgens de consensusregels als niet-standaard, omdat het standaardbeleid van Bitcoin core voor de `minRelayTxFee` parameter `0.00001` is (in BTC/kB).