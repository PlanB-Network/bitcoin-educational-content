---
term: OP_HASH160 (0XA9)
definition: En üstteki öğeyi önce SHA256, ardından RIPEMD160 ile özetleyen (hashing) opcode.
---

Yığından en üstteki öğeyi alır ve aynı anda hem `SHA256` hem de `RIPEMD160` işlevlerini kullanarak Hash ile değiştirir. Bu iki adımlı işlem 160 bitlik bir parmak izi oluşturur.