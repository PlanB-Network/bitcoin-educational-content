---
term: ÚČET

---
V peněženkách HD (Hierarchical Deterministic) představuje účet derivační vrstvu v hloubce 3 podle BIP32. Každý účet je postupně číslován od `/0'/` (zpevněná derivace, takže ve skutečnosti `/2^31/` nebo `/2 147 483 648/`). V této hloubce odvození se nacházejí známé `xpuby`. V dnešní době se v rámci jedné HD peněženky obvykle používá pouze jeden účet. Původně však byly koncipovány tak, aby oddělovaly různé kategorie použití v rámci jedné peněženky. Vezmeme-li například standardní derivační cestu pro externí adresu příjmu Taproot (P2TR): když si vezmeme za příklad adresu `m/86'/0'/0'/0/0`, je indexem účtu druhé `/0'/`.

![](../../dictionnaire/assets/17.webp)