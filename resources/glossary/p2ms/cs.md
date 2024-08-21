---
term: P2MS
---

P2MS znamená *Pay to Multisig*, což se překládá jako "platba na více podpisů". Jedná se o standardní skriptový model používaný k určení podmínek výdaje pro UTXO. Umožňuje uzamčení bitcoinů s více veřejnými klíči. Pro výdaj těchto bitcoinů je vyžadován podpis s předem definovaným počtem souvisejících soukromých klíčů. Například `P2MS 2/3` zahrnuje `3` veřejné klíče s `3` přidruženými tajnými soukromými klíči. Pro výdaj bitcoinů uzamčených tímto P2MS skriptem je potřeba podpis s alespoň `2` ze `3` soukromých klíčů. Jedná se o systém zabezpečení na základě prahu.

Tento skript byl vynalezen v roce 2011 Gavinem Andresenem, když převzal údržbu hlavního klienta Bitcoinu. Dnes je P2MS používán jen okrajově některými aplikacemi. Většina moderních multisignatur využívá jiné skripty, jako jsou P2SH nebo P2WSH. Ve srovnání s těmito je P2MS extrémně triviální. Veřejné klíče, které obsahuje, jsou odhaleny při přijetí transakce. Použití P2MS je také dražší než u ostatních multisignaturních skriptů.

> ► *P2MS jsou často nazývány "bare-multisig", což by se dalo přeložit jako "nahá multisignatura" nebo "surová multisignatura". Na začátku roku 2023 byly skripty P2MS středem kontroverze kvůli jejich zneužití v rámci protokolu Stamps. Byl zvláště poukázán na jejich dopad na soubor UTXO.*