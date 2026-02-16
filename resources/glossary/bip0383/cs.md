---
term: BIP0383

definition: Funkce multi() a sortedmulti() pro popis multisig skriptů v deskriptorech.
---
Zavádí funkce `multi(NUM, KEY, ..., KEY)` a `sortedmulti(NUM, KEY, ..., KEY)` pro deskriptory. Tyto funkce umožňují popis víceznakových skriptů v deskriptorech, přičemž `sortedmulti` seřadí veřejné klíče v lexikografickém pořadí, aby byla zajištěna kompatibilita při importu. BIP383 byl implementován spolu se všemi ostatními BIP souvisejícími s deskriptory (kromě BIP386) ve verzi 0.17 Bitcoin Core.