---
term: HASH256

---
Función criptográfica utilizada para diversas aplicaciones en Bitcoin. Consiste en aplicar la función SHA256 dos veces sobre los datos de entrada. El mensaje se pasa una vez por SHA256, y el resultado de esta operación se utiliza como entrada para una segunda pasada por SHA256. La salida de esta función es, por tanto, de 256 bits.

$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$