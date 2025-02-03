---
term: HASH160

---
Kryptografická funkce používaná v Bitcoinu, zejména pro generování přijímacích adres Legacy a SegWit v0. Kombinuje dvě hashovací funkce, které se postupně provádějí na vstupu: nejprve SHA256 a poté RIPEMD160. Výstupem této funkce je tedy 160 bitů.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$