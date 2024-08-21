---
term: BIP383
---

Zavádí funkce `multi(NUM, KEY, ..., KEY)` a `sortedmulti(NUM, KEY, ..., KEY)` pro popisovače. Tyto funkce umožňují popis multisignaturních skriptů v popisovačích, přičemž `sortedmulti` řadí veřejné klíče v lexikografickém pořadí, aby zajistila kompatibilitu při importu. BIP383 byl implementován společně se všemi ostatními s BIP souvisejícími s popisovači (kromě BIP386) ve verzi 0.17 Bitcoin Core.