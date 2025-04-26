---
term: FUNCIÓN HASH

---
Función matemática que toma una entrada de tamaño variable (llamada mensaje) y produce una salida de tamaño fijo (llamada hash, hashing, digest o huella digital). Las funciones hash son primitivas muy utilizadas en criptografía. Presentan propiedades específicas que las hacen adecuadas para su uso en contextos seguros:


- Resistencia a la preimagen: debe ser muy difícil encontrar un mensaje que produzca un hash específico, es decir, encontrar una preimagen $m$ para un hash $h$ tal que $h = H(m)$, donde $H$ es la función hash;
- Segunda resistencia a la preimagen: dado un mensaje $m_1$, debe ser muy difícil encontrar otro mensaje $m_2$ (diferente de $m_1$) tal que $H(m_1) = H(m_2)$;
- Resistencia a la colisión: debe ser muy difícil encontrar dos mensajes distintos $m_1$ y $m_2$ tales que $H(m_1) = H(m_2)$;
- Resistencia a la manipulación: pequeños cambios en la entrada deben provocar cambios significativos e impredecibles en la salida.

En el contexto de Bitcoin, las funciones hash se utilizan para varios propósitos, incluyendo el mecanismo de prueba de trabajo (*Proof-of-Work*), identificadores de transacciones, generación de direcciones, cálculos de sumas de comprobación y la creación de estructuras de datos como los árboles de Merkle. En cuanto al protocolo, Bitcoin utiliza exclusivamente la función `SHA256d`, también llamada `HASH256`, que consiste en un hash doble `SHA256`. `HASH256` también se utiliza en el cálculo de ciertas sumas de comprobación, especialmente para claves extendidas (`xpub`, `xprv`...). Por lo que respecta a los monederos, también se utilizan los siguientes:


- Simple `SHA256` para sumas de comprobación de frases mnemónicas;
- `SHA512` dentro de los algoritmos `HMAC` y `PBKDF2` utilizados en el proceso de derivación de carteras deterministas y jerárquicas;
- `HASH160`, que describe un uso sucesivo de un `SHA256` y un `RIPEMD160`. hASH160` se utiliza en el proceso de generación de direcciones de recepción (excepto P2PK y P2TR) y en el cálculo de huellas digitales de claves principales para claves extendidas.

> ► *En inglés se denomina "hash function "*