---
term: ÚČET
---

V HD (Hierarchicky Deterministických) peněženkách účet představuje vrstvu derivace na hloubce 3 podle BIP32. Každý účet je sekvenčně číslován počínaje od `/0'/` (pevná derivace, takže ve skutečnosti `/2^31/` nebo `/2 147 483 648/`). Právě na této hloubce derivace se nacházejí dobře známé `xpubs`. V současnosti se typicky v HD peněžence používá pouze jeden účet. Původně však byly koncipovány tak, aby segregovaly různé kategorie použití v rámci téže peněženky. Například, pokud vezmeme standardní cestu derivace pro externí Taproot (P2TR) přijímací adresu: `m/86'/0'/0'/0/0`, index účtu je druhý `/0'/`.

![](../../dictionnaire/assets/17.png)