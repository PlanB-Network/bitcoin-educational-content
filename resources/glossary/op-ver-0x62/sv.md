---
term: OP_VER (0X62)
definition: Inaktiverad opcode som sköt in klientversionen, konverterad till OP_SUCCESS.
---

Tillät att klientversionen lades på stacken. Denna opcode var inaktiverad eftersom om den hade använts skulle varje uppdatering ha lett till en Hard Fork. BIP342 modifierade denna opcode till `OP_SUCCESS`.