---
term: KONTO

---
HD (Hierarhical Deterministic) rahakottides esindab konto tuletuskihti 3. sügavusel vastavalt BIP32-le. Iga konto on nummerdatud järjestikku alates `/0'/` (karastatud tuletamine, seega tegelikult `/2^31/` või `/2 147 483 648/`). Selles tuletamissügavuses asuvad tuntud `xpubs`. Tänapäeval kasutatakse tavaliselt ainult ühte kontot HD rahakotis. Algselt olid need siiski mõeldud selleks, et eraldada eri kasutuskategooriaid ühe rahakoti sees. Näiteks kui võtame standardse tuletamise tee välise Taproot (P2TR) vastuvõtu aadressi jaoks: `m/86'/0'/0'/0/0`, on kontoindeksiks teine `/0'/`.

![](../../dictionnaire/assets/17.webp)