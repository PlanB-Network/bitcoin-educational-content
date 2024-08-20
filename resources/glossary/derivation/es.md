---
term: DERIVATION
---

Se refiere al proceso de generar pares de claves hijas a partir de un par de claves padre (clave privada y clave pública) y un código de cadena dentro de una billetera determinista y jerárquica (HD). Este proceso permite la segmentación de ramas y la organización de una billetera en diferentes niveles con numerosos pares de claves hijas, los cuales pueden ser recuperados conociendo solo la información básica de recuperación (la frase mnemotécnica y cualquier frase de paso potencial). Para derivar una clave hija, se utiliza la función `HMAC-SHA512` con el código de cadena padre y la concatenación de la clave padre y un índice de 32 bits. Hay dos tipos de derivaciones:
* Derivación normal, que utiliza la clave pública padre como base de la función `HMAC-SHA512`;
* Derivación reforzada, que utiliza la clave privada padre como base de la función `HMAC-SHA512`;

El resultado de HMAC-SHA512 se divide en dos: los primeros 256 bits se convierten en la clave hija (privada o pública después de procesarse a través de ECDSA), y los 256 bits restantes se convierten en el código de cadena hijo.