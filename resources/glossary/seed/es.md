---
term: SEMILLA

---
En el contexto específico de un monedero Bitcoin jerárquico determinista, una semilla es una pieza de información de 512 bits derivada de la aleatoriedad. Se utiliza para generar de forma determinista y jerárquica un conjunto de claves privadas, y sus correspondientes claves públicas, para un monedero Bitcoin. La semilla se confunde a menudo con la propia frase de recuperación. Sin embargo, se trata de información diferente. La semilla se obtiene aplicando la función `PBKDF2` a la frase mnemotécnica y a cualquier frase de contraseña potencial.

La semilla se inventó con la introducción de BIP32, que define las bases del monedero determinista jerárquico. En esta norma, la semilla era de 128 bits. Esto permite la derivación de todas las claves de un monedero a partir de una única pieza de información, a diferencia de los monederos JBOK (*Just a Bunch Of Keys*), que requieren nuevas copias de seguridad para cada clave generada. BIP39 introdujo posteriormente una codificación de esta semilla para simplificar su legibilidad por parte de los humanos. Esta codificación se realiza en forma de frase, comúnmente denominada frase mnemotécnica o frase de recuperación. Esta norma ayuda a evitar errores en la copia de seguridad de la semilla, en particular mediante el uso de una suma de comprobación.

De forma más general, en criptografía, una semilla es un dato aleatorio utilizado como punto de partida para generar claves criptográficas, cifrados o secuencias pseudoaleatorias. La calidad y la seguridad de muchos procesos criptográficos dependen de la aleatoriedad y la confidencialidad de la semilla.

> ► *La traducción inglesa de "graine" es "semilla". En francés, muchos utilizan directamente la palabra inglesa para referirse a la semilla.*