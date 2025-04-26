---
term: ENTROPÍA

---
La entropía, en el contexto de la criptografía y la información, es una medida cuantitativa de la incertidumbre o imprevisibilidad asociada a una fuente de datos o a un proceso aleatorio. La entropía desempeña un papel crucial en la seguridad de los sistemas criptográficos, especialmente en la generación de claves y números aleatorios. Una entropía elevada garantiza que las claves generadas sean suficientemente imprevisibles y resistentes a los ataques de fuerza bruta, en los que un atacante intenta todas las combinaciones posibles para adivinar la clave.

En el contexto de Bitcoin, la entropía se utiliza para generar claves privadas o semillas. Al crear un monedero determinista y jerárquico, la construcción de la frase mnemotécnica se realiza a partir de un número aleatorio, derivado a su vez de una fuente de entropía. A continuación, la frase se utiliza para generar múltiples claves privadas, de forma determinista y jerárquica, con el fin de crear condiciones de gasto en UTXOs.

Es esencial disponer de una fuente de entropía de calidad para garantizar la seguridad de los sistemas criptográficos. Las fuentes de entropía pueden ser procesos físicos, como el ruido electrónico o las variaciones térmicas, o procesos de software, como los generadores de números pseudoaleatorios.