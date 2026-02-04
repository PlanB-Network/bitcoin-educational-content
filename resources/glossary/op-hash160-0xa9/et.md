---
term: OP_HASH160 (0XA9)

definition: Opcode, mis räsib ülemise elemendi SHA256-ga ja seejärel RIPEMD160-ga.
---
Võtab korstnast ülemise elemendi ja asendab selle oma hashiga, kasutades samaaegselt nii `SHA256` kui ka `RIPEMD160` funktsioone. See kaheastmeline protsess genereerib 160-bitise sõrmejälje.