---
term: HASH256
---

Kryptografická funkce používaná pro různé aplikace na Bitcoinu. Zahrnuje dvojité použití funkce SHA256 na vstupní data. Zpráva je nejprve zpracována pomocí SHA256, a výsledek této operace je použit jako vstup pro druhé zpracování SHA256. Výstup této funkce je tedy 256 bitů.

$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$