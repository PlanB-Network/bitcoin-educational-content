---
term: OP_NUMEQUALVERIFY (0X9D)
---

Kombinuje operace `OP_NUMEQUAL` a `OP_VERIFY`. Číselně porovnává dva nejvyšší prvky na zásobníku. Pokud jsou hodnoty rovné, `OP_NUMEQUALVERIFY` odstraní z zásobníku pravdivý výsledek a pokračuje v provádění skriptu. Pokud hodnoty nejsou rovné, výsledek je nepravdivý a skript okamžitě selže.