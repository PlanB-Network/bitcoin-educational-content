---
term: OP_HASH160 (0XA9)

definition: Opcode băm phần tử trên cùng bằng SHA256 sau đó là RIPEMD160.
---
Takes the top element from the stack and replaces it with its hash, using both `SHA256` and `RIPEMD160` functions simultaneously. This two-step process generates a 160-bit fingerprint.