---
term: OP_HASH160 (0XA9)
definition: Opcode haszujący górny element za pomocą SHA256, a następnie RIPEMD160.
---

Pobiera górny element ze stosu i zastępuje go swoim Hash, używając jednocześnie funkcji `SHA256` i `RIPEMD160`. Ten dwuetapowy proces generuje 160-bitowy odcisk palca.