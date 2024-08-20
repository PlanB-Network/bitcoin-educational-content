---
term: FUNCIÓN HASH
---

Una función matemática que toma una entrada de tamaño variable (llamada mensaje) y produce una salida de tamaño fijo (llamada hash, hashing, digest o huella digital). Las funciones hash son primitivas ampliamente utilizadas en criptografía. Exhiben propiedades específicas que las hacen adecuadas para su uso en contextos seguros:
* Resistencia a la preimagen: debe ser muy difícil encontrar un mensaje que produzca un hash específico, es decir, encontrar una preimagen $m$ para un hash $h$ tal que $h = H(m)$, donde $H$ es la función hash;
* Resistencia a la segunda preimagen: dado un mensaje $m_1$, debe ser muy difícil encontrar otro mensaje $m_2$ (diferente de $m_1$) tal que $H(m_1) = H(m_2)$;
* Resistencia a colisiones: debe ser muy difícil encontrar dos mensajes distintos $m_1$ y $m_2$ tal que $H(m_1) = H(m_2)$;
* Resistencia a la manipulación: pequeños cambios en la entrada deben causar cambios significativos e impredecibles en la salida.

En el contexto de Bitcoin, las funciones hash se utilizan para varios propósitos, incluyendo el mecanismo de prueba de trabajo (*Proof-of-Work*), identificadores de transacciones, generación de direcciones, cálculos de checksum y la creación de estructuras de datos como árboles de Merkle. En el lado del protocolo, Bitcoin utiliza exclusivamente la función `SHA256d`, también denominada `HASH256`, que consiste en un doble hash `SHA256`. `HASH256` también se utiliza en el cálculo de ciertos checksums, notablemente para claves extendidas (`xpub`, `xprv`...). En el lado de la billetera, también se utilizan los siguientes:
* `SHA256` simple para checksums de frases mnemotécnicas;
* `SHA512` dentro de los algoritmos `HMAC` y `PBKDF2` utilizados en el proceso de derivación de billeteras deterministas y jerárquicas;
* `HASH160`, que describe un uso sucesivo de un `SHA256` y un `RIPEMD160`. `HASH160` se utiliza en el proceso de generación de direcciones de recepción (excepto P2PK y P2TR) y en el cálculo de huellas digitales de claves padres para claves extendidas.

> ► *En inglés, se le denomina "hash function".*