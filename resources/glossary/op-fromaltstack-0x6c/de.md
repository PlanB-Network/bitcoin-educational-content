---
term: OP_FROMALTSTACK (0X6C)

definition: Opcode, der ein Element vom Alternate-Stack auf den Haupt-Stack verschiebt.
---
Entfernt das oberste Element aus dem alternativen Stapel (*alt stack*) und legt es oben auf dem Hauptstapel (*main stack*) ab. Dieser Opcode wird verwendet, um Daten abzurufen, die vorübergehend auf dem alternativen Stack gespeichert sind. Einfach ausgedrückt, ist es die umgekehrte Operation von `OP_TOALTSTACK`.