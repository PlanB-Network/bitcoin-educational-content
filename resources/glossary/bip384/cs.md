---
term: BIP384
---

Zavádí funkci `combo(KEY)` pro popisovače. Tato funkce popisuje sadu možných výstupních skriptů pro daný veřejný klíč. Pokrývá tak současně více typů skriptů, včetně P2PK, P2PKH, P2WPKH a P2SH-P2WPKH. Pokud je daný klíč komprimovaný, jsou testovány všechny 4 typy skriptů, a pokud není, testují se pouze 2 typy Legacy skriptů. Cílem je zjednodušit reprezentaci klíčů v popisovačích tím, že poskytne jedinou metodu pro generování různých variant výstupních skriptů na základě stejného veřejného klíče. BIP384 byl implementován společně se všemi ostatními s BIP souvisejícími s popisovači (kromě BIP386) ve verzi 0.17 Bitcoin Core.