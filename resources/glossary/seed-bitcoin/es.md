---
term: SEED (BITCOIN)
---

En el contexto de Bitcoin, una semilla es un valor de 512 bits utilizado para derivar todas las claves privadas y públicas asociadas con una cartera HD (Determinista Jerárquica). Técnicamente, la semilla es un valor diferente de la frase de recuperación (o mnemónica). La frase, que típicamente está compuesta de 12 o 24 palabras, se genera de manera pseudoaleatoria a partir de una fuente de entropía y se completa con un checksum. Esta frase facilita la copia de seguridad humana al proporcionar una representación textual del valor en la base de la cartera.

Para obtener la semilla real, la frase de recuperación, posiblemente acompañada por una frase de paso opcional, se procesa a través del algoritmo PBKDF2 (*Password-Based Key Derivation Function 2*). El resultado de este cálculo es una semilla de 512 bits. Es esta semilla la que se utiliza para generar de manera determinista la clave maestra, y luego el conjunto completo de claves para la cartera HD, de acuerdo con BIP32.

![](../../dictionnaire/assets/31.png)

> ► *Sin embargo, en el lenguaje común, la mayoría de los bitcoiners se refieren a la frase mnemónica cuando hablan de la "semilla", y no al estado intermedio de derivación que yace entre la frase mnemónica y la clave maestra.*