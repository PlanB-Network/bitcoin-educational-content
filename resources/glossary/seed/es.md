---
term: GRANO
---

En el contexto específico de una cartera determinista jerárquica Bitcoin, una seed es una pieza de información de 512 bits derivada de un evento aleatorio. Se utiliza para generate de forma determinista y jerárquica un conjunto de claves privadas, y sus correspondientes claves públicas, para una cartera Bitcoin. La seed se confunde a menudo con la propia frase de recuperación. Pero no es lo mismo. La seed se obtiene aplicando la función `PBKDF2` a la frase Mnemonic y a cualquier passphrase.


La seed se inventó con BIP32, que definía las bases de la cartera determinista jerárquica. En esta norma, la seed medía 128 bits. Esto permite que todas las claves de una cartera se deriven de una única pieza de información, a diferencia de las carteras JBOK (*Just a Bunch Of Keys*), que requieren nuevas copias de seguridad para cada clave generada. El BIP39 propuso entonces una codificación de este seed, para simplificar su lectura por los humanos. Esta codificación adopta la forma de una frase, denominada generalmente frase Mnemonic o frase de recuperación. Esta norma evita los errores al guardar la seed, gracias en particular a la utilización de una suma de comprobación.


Fuera del contexto de Bitcoin, en criptografía en general, un seed es un valor inicial utilizado para generate claves criptográficas, o más ampliamente, cualquier tipo de datos producidos por un generador de números pseudoaleatorios. Este valor inicial debe ser aleatorio e impredecible para garantizar la seguridad del sistema criptográfico. En efecto, seed introduce entropía en el sistema, pero el proceso de generación que sigue es determinista.


> ► *En el lenguaje común, la mayoría de los bitcoiners se refieren a la frase Mnemonic cuando hablan de la "seed", y no al estado de derivación intermedio que se encuentra entre la frase Mnemonic y la clave maestra.*