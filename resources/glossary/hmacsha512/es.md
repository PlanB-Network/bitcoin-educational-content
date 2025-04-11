---
term: HMAC-SHA512

---
hMAC-SHA512" son las siglas de "Hash-based Message Authentication Code - Secure Hash Algorithm 512". Se trata de un algoritmo criptográfico utilizado para verificar la integridad y autenticidad de los mensajes intercambiados entre dos partes. Combina la función hash criptográfica `SHA512` con una clave secreta compartida para generar un Código de Autenticación de Mensaje (MAC) único para cada mensaje.

En el contexto de Bitcoin, el uso natural de `HMAC-SHA512` es ligeramente derivado. Este algoritmo se utiliza en el proceso de derivación determinista y jerárquica del árbol de claves criptográficas de un monedero. el algoritmo "HMAC-SHA512" se utiliza principalmente para ir de la semilla a la clave maestra, y después para cada derivación de un par padre a pares hijos. Este algoritmo también se encuentra en otro algoritmo de derivación llamado "PBKDF2", que se utiliza para ir de la frase de recuperación y la frase de contraseña a la semilla.