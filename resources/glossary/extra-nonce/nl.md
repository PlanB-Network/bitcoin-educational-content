---
term: Extra-nonce
definition: Veld in de coinbase waarmee de zoekruimte voor mining kan worden uitgebreid buiten de klassieke nonce.
---

Veld gebruikt in de `scriptSig` van de Coinbase Transaction van een blok, waardoor een groter aantal mogelijkheden getest kan worden om een Hash te hebben die lager is dan de moeilijkheidsdoelstelling, naast de klassieke Nonce, die direct in de kop van elk blok staat.


Het wijzigen van de extra-Nonce in de Coinbase Transaction verandert de identifier van deze transactie, en daarmee de Merkle Root van alle transacties in het blok, wat ook de koptekst van het blok wijzigt. Hierdoor kan de Miner doorgaan met het zoeken naar hashes als het bereik van de klassieke Nonce al is uitgeput, zonder de structuur van zijn kandidaat-blok te veranderen.


In Mining pools wordt de extra-Nonce vaak verdeeld in twee delen: een gegenereerd door de pool om elke chopper te identificeren en een ander gemodificeerd door de chopper op zoek naar een geldig aandeel. Hierdoor kunnen de verschillende choppers in de pool gelijktijdig werken aan hetzelfde kandidaatblok met het hele noncesbereik, zonder hetzelfde werk op poolniveau te dupliceren.