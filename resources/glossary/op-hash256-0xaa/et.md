---
term: OP_HASH256 (0XAA)

definition: Opcode, mis räsib ülemise elemendi kahe järjestikuse SHA256-ga.
---
Võtab virnast ülemise elemendi ja asendab selle oma hashiga, kasutades kaks korda funktsiooni `SHA256`. Sisend on üks kord hashitud `SHA256`-ga ja seejärel hashitakse digesti teist korda `SHA256`-ga. See kaheastmeline protsess genereerib 256-bitise sõrmejälje.