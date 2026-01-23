---
term: BIP0385

definition: Funkce addr() a raw() pro popis výstupních skriptů podle adresy nebo v hexadecimálním formátu v deskriptorech.
---
Zavádí deskriptorové funkce `addr(ADDR)` a `raw(HEX)`. Funkce `addr(ADDR)` umožňuje popsat výstupní skript pomocí přijímací adresy, zatímco funkce `raw(HEX)` umožňuje specifikovat výstupní skript pomocí surové hexadecimální reprezentace tohoto skriptu. BIP385 byl implementován spolu se všemi ostatními BIP souvisejícími s deskriptory (kromě BIP386) ve verzi 0.17 jádra bitcoinu.