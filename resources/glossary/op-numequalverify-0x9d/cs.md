---
term: OP_NUMEQUALVERIFY (0X9D)

---
Kombinuje operace `OP_NUMEQUAL` a `OP_VERIFY`. Číselně porovnává dva nejvyšší prvky na zásobníku. Pokud se hodnoty rovnají, `OP_NUMEQUALVERIFY` odstraní pravdivý výsledek ze zásobníku a pokračuje ve vykonávání skriptu. Pokud se hodnoty nerovnají, je výsledkem false a skript okamžitě selže.