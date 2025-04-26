---
term: OP_PUSHDATA4 (0X4E)

---
Ermöglicht das Schieben einer sehr großen Datenmenge auf den Stack. Es folgen vier Bytes (Little-Endian), die die Länge der zu schiebenden Daten angeben (bis zu etwa 4,3 GB). Dieser Opcode wird verwendet, um sehr große Daten in Skripte einzufügen, obwohl seine Verwendung aufgrund praktischer Beschränkungen der Transaktionsgröße äußerst selten ist.