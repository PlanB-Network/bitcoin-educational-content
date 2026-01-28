---
term: OP_ENDIF (0X68)
definition: Opcode oznaczający koniec struktury warunkowej w skrypcie.
---

Oznacza koniec warunkowej struktury kontrolnej zainicjowanej przez `OP_IF` lub `OP_NOTIF`, po której zwykle następuje jeden lub więcej `OP_ELSE`. Wskazuje, że wykonywanie skryptu powinno być kontynuowane poza strukturą warunkową, niezależnie od tego, która gałąź została wykonana. Innymi słowy, `OP_ENDIF` służy do wyznaczania końca bloków warunkowych w skryptach.