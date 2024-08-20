---
term: PBKDF2
---

`PBKDF2` significa *Password-Based Key Derivation Function 2* (Función de Derivación de Clave Basada en Contraseña 2). Es un método para crear claves criptográficas a partir de una contraseña utilizando una función de derivación. Toma como entrada una contraseña, una sal criptográfica y aplica iterativamente una función predeterminada (a menudo una función hash como `SHA256` o un `HMAC`) a estos datos. Este proceso se repite muchas veces para generar una clave criptográfica.

En el contexto de Bitcoin, `PBKDF2` se utiliza en conjunto con la función `HMAC-SHA512` para crear la semilla de una cartera determinista y jerárquica (seed) a partir de una frase de recuperación de 12 o 24 palabras. La sal criptográfica utilizada en este caso es la frase de paso BIP39, y el número de iteraciones es `2048`.