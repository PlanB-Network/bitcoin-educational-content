---
term: OP_VER (0X62)

definition: Deaktivierter Opcode, der früher die Client-Version pushte; wurde in OP_SUCCESS umgewandelt.
---
Erlaubte das Pushen der Client-Version auf den Stack. Dieser Opcode wurde deaktiviert, weil jede Aktualisierung zu einem Hard Fork geführt hätte. BIP342 änderte diesen Opcode in `OP_SUCCESS`.