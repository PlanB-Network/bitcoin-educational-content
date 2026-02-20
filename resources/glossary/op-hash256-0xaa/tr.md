---
term: OP_HASH256 (0XAA)
definition: En üstteki öğeyi birbirini izleyen iki SHA256 ile özetleyen opcode.
---

Yığından en üst öğeyi alır ve `SHA256` işlevini iki kez kullanarak Hash ile değiştirir. Girdi bir kez `SHA256` ile hash edilir ve ardından özet ikinci kez `SHA256` ile hash edilir. Bu iki adımlı işlem 256 bitlik bir parmak izi oluşturur.