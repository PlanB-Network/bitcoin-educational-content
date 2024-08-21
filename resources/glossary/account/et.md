---
term: KONTO
---

HD (Hierarhiliselt Määratud) rahakottides tähistab konto tuletuskihti sügavusel 3 vastavalt BIP32-le. Iga konto on järjestikku nummerdatud alates `/0'/` (kõvasti tuletatud, seega tegelikkuses `/2^31/` või `/2 147 483 648/`). Just selles tuletussügavuses asuvad tuntud `xpubid`. Tänapäeval kasutatakse HD rahakotis tavaliselt ainult ühte kontot. Siiski, algselt olid need loodud erinevate kasutuskategooriate eraldamiseks samas rahakotis. Näiteks, kui võtame standardse tuletustee välise Taprooti (P2TR) vastuvõtu aadressi jaoks: `m/86'/0'/0'/0/0`, siis konto indeks on teine `/0'/`.

![](../../dictionnaire/assets/17.png)