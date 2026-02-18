---
term: OP_NUMNOTEQUAL (0X9E)

definition: Opcode kontrolující, zda jsou oba prvky na vrcholu zásobníku číselně odlišné.
---
Porovná dva nejvyšší prvky na zásobníku a zkontroluje, zda se číselně nerovnají. Pokud se hodnoty nerovnají, vloží na zásobník `1` (true), jinak vloží `0` (false). Toto je opak funkce `OP_NUMEQUAL`.