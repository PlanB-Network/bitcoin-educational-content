---
term: P2MS

---
P2MS je zkratka pro *Pay to Multisig*, což v překladu znamená "platba za více podpisů". Jedná se o standardní model skriptu, který se používá pro stanovení podmínek výdajů na UTXO. Umožňuje uzamčení bitcoinů pomocí více veřejných klíčů. K utrácení těchto bitcoinů je zapotřebí podpis s předem definovaným počtem přidružených soukromých klíčů. Například `P2MS 2/3` zahrnuje `3` veřejné klíče s `3` přidruženými tajnými soukromými klíči. K utracení bitcoinů uzamčených tímto skriptem P2MS je zapotřebí podpis s alespoň `2` z `3` soukromých klíčů. Jedná se o prahový bezpečnostní systém.

Tento skript vymyslel v roce 2011 Gavin Andresen, když převzal údržbu hlavního klienta Bitcoinu. Dnes se P2MS používá jen okrajově v některých aplikacích. Drtivá většina moderních multisignatur používá jiné skripty, například P2SH nebo P2WSH. Ve srovnání s nimi je P2MS extrémně triviální. Veřejné klíče, ze kterých se skládá, jsou odhaleny při přijetí transakce. Použití P2MS je také dražší než jiné skripty pro multisignatury.

> ► *P2MS se často nazývají "bare-multisig", což by se dalo přeložit jako "nahý multisignature" nebo "surový multisignature". Na začátku roku 2023 se skripty P2MS ocitly v centru kontroverze kvůli jejich nesprávnému použití v rámci protokolu Stamps. Bylo poukázáno zejména na jejich dopad na sadu UTXO*