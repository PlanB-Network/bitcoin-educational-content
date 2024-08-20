---
term: OBJETIVO DE DIFICULTAD
---

El factor de dificultad, también conocido como objetivo de dificultad, es un parámetro utilizado en el mecanismo de consenso por prueba de trabajo (Proof of Work, PoW) en Bitcoin. El objetivo representa un valor numérico que determina la dificultad para los mineros de resolver un problema criptográfico específico, llamado prueba de trabajo, al crear un nuevo bloque en la blockchain.

El objetivo de dificultad es un número ajustable de 256 bits (64 bytes) que determina un límite de aceptabilidad para el hash de los encabezados de bloque. En otras palabras, para que un bloque sea válido, el hash de su encabezado con `SHA256d` (doble `SHA256`) debe ser numéricamente inferior o igual al objetivo de dificultad. La prueba de trabajo consiste en modificar el campo `nonce` del encabezado del bloque o la transacción coinbase hasta que el hash resultante sea menor que el valor objetivo.

Este objetivo se ajusta cada 2016 bloques (aproximadamente cada dos semanas), durante un evento llamado "ajuste". El factor de dificultad se recalcula basándose en el tiempo que tomó minar los 2016 bloques anteriores. Si el tiempo total es menor a dos semanas, la dificultad aumenta ajustando el objetivo hacia abajo. Si el tiempo total es más de dos semanas, la dificultad disminuye ajustando el objetivo hacia arriba. El objetivo es mantener un tiempo promedio de minería de 10 minutos por bloque. Este tiempo entre cada bloque ayuda a prevenir divisiones de la red Bitcoin, resultando en un desperdicio de poder computacional. El objetivo de dificultad se encuentra en cada encabezado de bloque, dentro del campo `nBits`. Dado que este campo se reduce a 32 bits y el objetivo es en realidad de 256 bits, el objetivo se compacta en un formato científico menos preciso.

![](../../dictionnaire/assets/34.png)

> ► *El objetivo de dificultad a veces también se llama "factor de dificultad". Por extensión, se puede referir con su codificación en los encabezados de bloque con el término "nBits".*