---
term: OP_CODESEPARATOR (0XAB)

definition: Opcode, der ein Skript segmentiert, um unabhängige Signaturen für jeden Teil zu ermöglichen.
---
Ändert das aktuelle Ausgabeskript und gibt an, dass nur die auf diesen Opcode folgenden Operationen bei der Überprüfung der Signaturen für die entsprechenden Eingaben berücksichtigt werden. Auf diese Weise kann ein komplexes Skript in mehrere Teile unterteilt werden, wobei jedes Segment unabhängig signiert werden kann.