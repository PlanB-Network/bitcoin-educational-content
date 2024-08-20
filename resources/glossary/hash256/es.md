---
term: HASH256
---

Función criptográfica utilizada para diversas aplicaciones en Bitcoin. Implica aplicar la función SHA256 dos veces sobre los datos de entrada. El mensaje se pasa por SHA256 una vez, y el resultado de esta operación se utiliza como entrada para una segunda pasada a través de SHA256. Por lo tanto, la salida de esta función es de 256 bits.

$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$