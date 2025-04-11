---
term: OP_TOALTSTACK (0X6B)

---
Nimmt den obersten Punkt des Hauptstapels (*main stack*) und verschiebt ihn auf den alternativen Stapel (*alt stack*). Dieser Opcode wird verwendet, um Daten für die spätere Verwendung im Skript vorübergehend beiseite zu legen. Das verschobene Element wird somit aus dem Hauptstapel entfernt. der Opcode `OP_FROMALTSTACK` wird dann verwendet, um es wieder auf den Hauptstapel zu legen.