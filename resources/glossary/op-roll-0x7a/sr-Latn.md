---
term: OP_ROLL (0X7A)
definition: Opcode koji prebacuje element sa određene dubine stack-a na vrh.
---

Pomerera stavku sa steka na vrh steka, na osnovu dubine specificirane vrednošću na vrhu steka pre operacije. Na primer, ako je vrednost na vrhu steka `4`, `OP_ROLL` će izabrati četvrtu stavku od vrha steka i premestiće ovu vrednost na vrh. `OP_ROLL` ima istu funkciju kao `OP_PICK`, osim što uklanja stavku sa njene originalne pozicije.