---
term: OP_ENDIF (0X68)
definition: Opcode marking the end of a conditional structure in a script.
---

Marks the end of a conditional control structure initiated by an `OP_IF` or an `OP_NOTIF`, usually followed by one or more `OP_ELSE`. It indicates that the execution of the script should continue beyond the conditional structure, regardless of which branch was executed. In other words, `OP_ENDIF` serves to delineate the end of conditional blocks in scripts.

