---
term: OP_VER (0X62)
definition: Disabled opcode that pushed the client version, converted to OP_SUCCESS.
---

Allowed pushing the client version onto the stack. This opcode was disabled because if it had been used, each update would have led to a hard fork. BIP342 modified this opcode to `OP_SUCCESS`.