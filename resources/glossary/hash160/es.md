---
term: HASH160

---
Función criptográfica utilizada en Bitcoin, especialmente para generar direcciones de recepción Legacy y SegWit v0. Combina dos funciones hash que se ejecutan sucesivamente en la entrada: primero SHA256, después RIPEMD160. La salida de esta función es por tanto de 160 bits.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$