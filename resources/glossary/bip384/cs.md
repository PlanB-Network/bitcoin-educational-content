---
term: BIP384

---
Zavádí funkci `combo(KEY)` pro deskriptory. Tato funkce popisuje sadu možných výstupních skriptů pro daný veřejný klíč. Pokrývá tedy více typů skriptů najednou, včetně P2PK, P2PKH, P2WPKH a P2SH-P2WPKH. Pokud je daný klíč komprimovaný, testují se všechny 4 typy skriptů, pokud komprimovaný není, testují se pouze 2 typy skriptů Legacy. Cílem je zjednodušit reprezentaci klíčů v deskriptorech poskytnutím jediné metody pro generování různých variant výstupních skriptů na základě stejného veřejného klíče. BIP384 byl implementován spolu se všemi ostatními BIP souvisejícími s deskriptory (kromě BIP386) ve verzi 0.17 Bitcoin Core.