---
term: P2SH

---
P2SH znamená *Pay to Script Hash*. Jedná se o standardní model skriptu, který se používá pro stanovení podmínek výdajů na UTXO. Na rozdíl od skriptů P2PK a P2PKH, kde jsou podmínky výdajů předem definovány, P2SH umožňuje integrovat libovolné podmínky výdajů a další funkce v rámci transakčního skriptu.

Technicky vzato, v transakci P2SH obsahuje `scriptPubKey` spíše kryptografický hash `redeemScriptu` než explicitní podmínky utrácení. Tento hash se získá pomocí hashe `SHA256`. Při odesílání bitcoinů na adresu P2SH není základní `redeemScript` odhalen. Do transakce je zahrnuta pouze jeho hash. Adresy P2SH jsou kódovány v `Base58Check` a začínají číslem `3`. Když chce příjemce obdržené bitcoiny utratit, musí poskytnout `redeemScript`, který odpovídá hash přítomnému v `scriptPubKey`, spolu s potřebnými údaji, které splňují podmínky tohoto `redeemScriptu`. Například ve skriptu P2SH s více podpisy může skript vyžadovat podpisy z více soukromých klíčů.

Použití P2SH nabízí větší flexibilitu, protože umožňuje sestavení libovolných skriptů, aniž by odesílatel znal podrobnosti. P2SH byl představen v roce 2012 s protokolem BIP16.