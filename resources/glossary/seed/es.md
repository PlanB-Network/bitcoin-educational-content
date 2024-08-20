---
term: SEED
---

Dentro del contexto específico de una cartera Bitcoin determinista jerárquica, una semilla (seed) es un fragmento de información de 512 bits derivado de la aleatoriedad. Se utiliza para generar de manera determinista y jerárquica un conjunto de claves privadas y sus correspondientes claves públicas para una cartera Bitcoin. La semilla a menudo se confunde con la frase de recuperación en sí. Sin embargo, es información diferente. La semilla se obtiene aplicando la función `PBKDF2` a la frase mnemotécnica y cualquier frase de paso potencial.

La semilla fue inventada con la introducción de BIP32, que define los fundamentos de la cartera determinista jerárquica. En este estándar, la semilla era de 128 bits. Esto permite la derivación de todas las claves en una cartera a partir de una sola pieza de información, a diferencia de las carteras JBOK (*Just a Bunch Of Keys*), que requieren nuevas copias de seguridad para cada clave generada. BIP39 introdujo más tarde una codificación de esta semilla para simplificar su legibilidad por humanos. Esta codificación se realiza en forma de una frase, comúnmente referida como frase mnemotécnica o frase de recuperación. Este estándar ayuda a evitar errores en la copia de seguridad de la semilla, notablemente a través del uso de un checksum.

Más generalmente, en criptografía, una semilla es un fragmento de datos aleatorios utilizado como punto de partida para generar claves criptográficas, encriptaciones o secuencias pseudoaleatorias. La calidad y seguridad de muchos procesos criptográficos dependen de la aleatoriedad y confidencialidad de la semilla.

> ► *La traducción al inglés de "graine" es "seed". En francés, muchos utilizan directamente la palabra inglesa para referirse a la semilla.*