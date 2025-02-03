---
term: BIP113

---
Se ha introducido un cambio en el cálculo de todas las operaciones de bloqueo de tiempo (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence`, y `OP_CHECKSEQUENCEVERIFY`). Especifica que para evaluar la validez de los timelocks, ahora deben compararse con el MTP (*Median Time Past*), que es la mediana de las marcas de tiempo de los últimos 11 bloques. Antes sólo se utilizaba la marca de tiempo del bloque anterior. Este método hace que el sistema sea más predecible y evita la manipulación de la referencia temporal por parte de los mineros. El BIP113 se introdujo mediante una bifurcación suave el 4 de julio de 2016, junto con el BIP68 y el BIP112, activados por primera vez mediante el método BIP9.