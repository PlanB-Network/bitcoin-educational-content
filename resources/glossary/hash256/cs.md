---
term: HASH256

---
Kryptografická funkce používaná pro různé aplikace v Bitcoinu. Zahrnuje dvojí použití funkce SHA256 na vstupní data. Zpráva jednou projde funkcí SHA256 a výsledek této operace se použije jako vstup pro druhý průchod funkcí SHA256. Výstupem této funkce je tedy 256 bitů.

$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$