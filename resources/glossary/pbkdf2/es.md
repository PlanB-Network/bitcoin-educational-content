---
term: PBKDF2

---
pBKDF2" son las siglas de "Password-Based Key Derivation Function 2". Es un método para crear claves criptográficas a partir de una contraseña utilizando una función de derivación. Toma como entrada una contraseña, una sal criptográfica y aplica iterativamente una función predeterminada (a menudo una función hash como `SHA256` o una `HMAC`) a estos datos. Este proceso se repite muchas veces para generar una clave criptográfica.

En el contexto de Bitcoin, `PBKDF2` se utiliza junto con la función `HMAC-SHA512` para crear la semilla de un monedero determinista y jerárquico (seed) a partir de una frase de recuperación de 12 o 24 palabras. La sal criptográfica utilizada en este caso es la frase de contraseña BIP39, y el número de iteraciones es `2048`.