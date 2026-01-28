---
term: OP_PUSHDATA1 (0X4C)
definition: Opcode som skjuter in upp till 255 byte data på stacken.
---

Skjuter upp en viss mängd data på stacken. Den följs av en byte som anger längden på de data som ska skjutas (upp till 255 byte). Denna opcode används för att inkludera data av varierande storlek i skript.