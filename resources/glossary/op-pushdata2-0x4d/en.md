---
term: OP_PUSHDATA2 (0X4D)
definition: Opcode pushing up to 65 KB of data onto the stack.
---

Allows pushing a large amount of data onto the stack. It is followed by two bytes (little-endian) that specify the length of the data to be pushed (up to about 65 KB). It is used to insert larger data into scripts.