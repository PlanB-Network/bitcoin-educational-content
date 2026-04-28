---
term: OP_ENDIF (0X68)

definition: Opcode, der das Ende einer bedingten Struktur in einem Script markiert.
---
Markiert das Ende einer bedingten Kontrollstruktur, die durch ein `OP_IF` oder ein `OP_NOTIF` eingeleitet wurde, normalerweise gefolgt von einem oder mehreren `OP_ELSE`. Es zeigt an, dass die Ausführung des Skripts über die bedingte Struktur hinaus fortgesetzt werden soll, unabhängig davon, welcher Zweig ausgeführt wurde. Mit anderen Worten: `OP_ENDIF` dient dazu, das Ende von bedingten Blöcken in Skripten abzugrenzen.