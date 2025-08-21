---
term: BIP0111
---

Stelt de toevoeging voor van een servicebit met de naam `NODE_BLOOM` om knooppunten in staat te stellen expliciet aan te geven dat ze Bloom Filters ondersteunen, zoals beschreven in BIP37. De introductie van `NODE_BLOOM` stelt knooppuntbeheerders in staat om deze dienst uit te schakelen om de risico's van DoS te verminderen. De BIP37 optie is standaard uitgeschakeld in Bitcoin core. Om het in te schakelen moet de parameter `peerbloomfilters=1` worden ingevoerd in het configuratiebestand.