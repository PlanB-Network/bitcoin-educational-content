---
term: HASH160
---

Kryptografická funkce používaná v Bitcoinu, zejména pro generování adres pro příjem Legacy a SegWit v0. Kombinuje dvě hashovací funkce, které jsou na vstupu spuštěny postupně: nejprve SHA256, poté RIPEMD160. Výstup této funkce je tedy 160 bitů.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$