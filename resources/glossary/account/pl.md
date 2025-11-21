---
term: KONTO
---

W portfelach HD (Hierarchical Deterministic) konto reprezentuje pochodną Layer na głębokości 3 zgodnie z BIP32. Każde konto jest kolejno numerowane, zaczynając od `/0'/` (utwardzona derywacja, więc w rzeczywistości `/2^31/` lub `/2 147 483 648/`). To właśnie na tej głębokości derywacji znajdują się dobrze znane `xpubs`. Obecnie, zazwyczaj tylko jedno konto jest używane w HD Wallet. Jednak pierwotnie zostały one stworzone w celu oddzielenia różnych kategorii użytkowania w ramach tego samego Wallet. Na przykład, jeśli weźmiemy standardową ścieżkę derywacji dla zewnętrznego Taproot (P2TR) odbierającego Address: `m/86'/0'/0'/0/0`, indeks konta jest drugim `/0'/`.


![](../../dictionnaire/assets/17.webp)