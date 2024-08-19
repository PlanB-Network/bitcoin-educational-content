---
term: OP_TOALTSTACK (0X6B)
---

Nimmt das oberste Element des Hauptstapels (*main stack*) und verschiebt es auf den alternativen Stapel (*alt stack*). Dieser Opcode wird verwendet, um Daten vorübergehend zur späteren Verwendung im Skript beiseite zu legen. Das verschobene Element wird somit vom Hauptstapel entfernt. `OP_FROMALTSTACK` wird dann verwendet, um es wieder oben auf den Hauptstapel zu legen.