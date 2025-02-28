---
term: SEMILLA (BITCOIN)

---
En el contexto de Bitcoin, una semilla es un valor de 512 bits utilizado para derivar todas las claves privadas y públicas asociadas a un monedero HD (Determinista Jerárquico). Técnicamente, la semilla es un valor diferente de la frase de recuperación (o mnemotécnica). La frase, que suele estar compuesta por 12 o 24 palabras, se genera de forma pseudoaleatoria a partir de una fuente de entropía y se completa con una suma de comprobación. Esta frase facilita la copia de seguridad humana al proporcionar una representación textual del valor en la base del monedero.

Para obtener la semilla real, la frase de recuperación, posiblemente acompañada de una frase de contraseña opcional, se procesa a través del algoritmo PBKDF2 (*Función de Derivación de Clave Basada en Contraseña 2*). El resultado de este cálculo es una semilla de 512 bits. Esta semilla se utiliza para generar de forma determinista la clave maestra y, a continuación, todo el conjunto de claves del monedero HD, de acuerdo con BIP32.

![](../../dictionnaire/assets/31.webp)

> ► *Sin embargo, en el lenguaje común, la mayoría de los bitcoiners se refieren a la frase mnemotécnica cuando hablan de la "semilla", y no al estado intermedio de derivación que se encuentra entre la frase mnemotécnica y la clave maestra.*