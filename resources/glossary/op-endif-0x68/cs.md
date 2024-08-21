---
term: OP_ENDIF (0X68)
---

Označuje konec podmíněné řídící struktury zahájené pomocí `OP_IF` nebo `OP_NOTIF`, obvykle následované jedním nebo více `OP_ELSE`. Udává, že vykonávání skriptu by mělo pokračovat za podmíněnou strukturou, bez ohledu na to, která větev byla provedena. Jinými slovy, `OP_ENDIF` slouží k vymezení konce podmíněných bloků ve skriptech.