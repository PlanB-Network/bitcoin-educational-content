---
term: HASH160
---

Función criptográfica utilizada en Bitcoin, notablemente para generar direcciones de recepción Legacy y SegWit v0. Combina dos funciones hash que se ejecutan sucesivamente en la entrada: primero SHA256, luego RIPEMD160. Por lo tanto, la salida de esta función es de 160 bits.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$