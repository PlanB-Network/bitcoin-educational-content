---
term: OP_ENDIF (0X68)

---
Označuje konec podmíněné řídicí struktury iniciované příkazem `OP_IF` nebo `OP_NOTIF`, za kterým obvykle následuje jeden nebo více příkazů `OP_ELSE`. Označuje, že provádění skriptu by mělo pokračovat i po skončení podmíněné struktury, bez ohledu na to, která větev byla provedena. Jinými slovy, `OP_ENDIF` slouží k vymezení konce podmíněných bloků ve skriptech.