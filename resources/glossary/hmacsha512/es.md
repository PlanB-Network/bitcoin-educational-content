---
term: HMAC-SHA512
---

`HMAC-SHA512` significa "Código de Autenticación de Mensajes basado en Hash - Algoritmo de Hash Seguro 512". Es un algoritmo criptográfico utilizado para verificar la integridad y autenticidad de los mensajes intercambiados entre dos partes. Combina la función de hash criptográfico `SHA512` con una clave secreta compartida para generar un Código de Autenticación de Mensajes (MAC) único para cada mensaje.

En el contexto de Bitcoin, el uso natural de `HMAC-SHA512` es ligeramente derivado. Este algoritmo se utiliza en el proceso de derivación determinista y jerárquica del árbol de clave criptográfica de una cartera. `HMAC-SHA512` se utiliza notablemente para pasar de la semilla a la clave maestra, y luego para cada derivación de un par padre a pares hijos. Este algoritmo también se encuentra dentro de otro algoritmo de derivación denominado `PBKDF2`, utilizado para pasar de la frase de recuperación y la contraseña a la semilla.