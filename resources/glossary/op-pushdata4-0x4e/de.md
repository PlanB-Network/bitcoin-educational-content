---
term: OP_PUSHDATA4 (0X4E)
---

Ermöglicht das Pushen einer sehr großen Datenmenge auf den Stack. Ihm folgen vier Bytes (Little-Endian), die die Länge der zu pushenden Daten angeben (bis zu etwa 4,3 GB). Dieser Opcode wird verwendet, um sehr große Daten in Skripte einzufügen, obwohl seine Verwendung aufgrund praktischer Beschränkungen der Transaktionsgröße extrem selten ist.