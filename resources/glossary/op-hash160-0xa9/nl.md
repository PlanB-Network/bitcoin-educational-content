---
term: OP_HASH160 (0XA9)
definition: Opcode die het bovenste element hasht met SHA256 en vervolgens RIPEMD160.
---

Neemt het bovenste element van de stack en vervangt het door zijn Hash, door gelijktijdig de `SHA256` en `RIPEMD160` functies te gebruiken. Dit proces in twee stappen genereert een 160-bits vingerafdruk.