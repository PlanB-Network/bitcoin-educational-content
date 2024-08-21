---
term: P2SH
---

P2SH znamená *Pay to Script Hash* (Platba na skriptový hash). Jedná se o standardní skriptový model používaný k určení podmínek výdaje pro UTXO. Na rozdíl od skriptů P2PK a P2PKH, kde jsou podmínky výdaje předem definovány, P2SH umožňuje integraci libovolných podmínek výdaje a dalších funkcionalit do transakčního skriptu.

Technicky, v transakci P2SH, `scriptPubKey` obsahuje kryptografický hash `redeemScriptu`, namísto explicitních podmínek výdaje. Tento hash je získán pomocí hashovací funkce `SHA256`. Při posílání bitcoinů na adresu P2SH není podkladový `redeemScript` odhalen. V transakci je zahrnut pouze jeho hash. Adresy P2SH jsou zakódovány v `Base58Check` a začínají číslem `3`. Když příjemce chce utratit přijaté bitcoiny, musí poskytnout `redeemScript`, který odpovídá hashi přítomnému v `scriptPubKey`, spolu s nezbytnými daty pro splnění podmínek tohoto `redeemScriptu`. Například v multisignaturním skriptu P2SH může skript vyžadovat podpisy z více soukromých klíčů.

Použití P2SH nabízí větší flexibilitu, protože umožňuje konstrukci libovolných skriptů, aniž by odesílatel znal detaily. P2SH bylo zavedeno v roce 2012 s BIP16.