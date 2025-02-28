---
term: OBJETIVO DE DIFICULTAD

---
El factor de dificultad, también conocido como objetivo de dificultad, es un parámetro utilizado en el mecanismo de consenso por prueba de trabajo (Proof of Work, PoW) en Bitcoin. El objetivo representa un valor numérico que determina la dificultad para que los mineros resuelvan un problema criptográfico específico, denominado prueba de trabajo, al crear un nuevo bloque en la blockchain.

El objetivo de dificultad es un número ajustable de 256 bits (64 bytes) que determina un límite de aceptabilidad para el hash de las cabeceras de los bloques. En otras palabras, para que un bloque sea válido, el hash de su cabecera con `SHA256d` (doble `SHA256`) debe ser numéricamente inferior o igual al objetivo de dificultad. La prueba de trabajo consiste en modificar el campo `nonce` de la cabecera del bloque o de la transacción coinbase hasta que el hash resultante sea inferior al valor objetivo.

Este objetivo se ajusta cada 2016 bloques (aproximadamente cada dos semanas), durante un evento llamado "ajuste" El factor de dificultad se recalcula en función del tiempo que se tardó en minar los bloques de 2016 anteriores. Si el tiempo total es inferior a dos semanas, la dificultad aumenta ajustando el objetivo a la baja. Si el tiempo total es superior a dos semanas, la dificultad disminuye ajustando el objetivo al alza. El objetivo es mantener un tiempo medio de extracción de 10 minutos por bloque. Este tiempo entre cada bloque ayuda a prevenir divisiones de la red Bitcoin, resultando en un desperdicio de potencia de cálculo. El objetivo de dificultad se encuentra en la cabecera de cada bloque, dentro del campo `nBits`. Como este campo se reduce a 32 bits y el objetivo es en realidad de 256 bits, el objetivo se compacta en un formato científico menos preciso.

![](../../dictionnaire/assets/34.webp)

> ► *El objetivo de dificultad a veces también se denomina "factor de dificultad" Por extensión, se puede hacer referencia a él con su codificación en las cabeceras de bloque con el término "nBits. "*