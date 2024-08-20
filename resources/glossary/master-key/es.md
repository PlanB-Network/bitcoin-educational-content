---
term: LLAVE MAESTRA
---

En el contexto de las billeteras HD (Deterministas Jerárquicas), la llave privada maestra es una llave privada única derivada de la semilla de la billetera. Para obtener la llave maestra, se aplica la función `HMAC-SHA512` a la semilla, utilizando las palabras "*Bitcoin seed*" literalmente como la clave. El resultado de esta operación produce una salida de 512 bits, con los primeros 256 bits constituyendo la llave maestra, y los 256 bits restantes formando el código de cadena maestro. La llave maestra y el código de cadena maestro sirven como el punto de partida para derivar todas las llaves privadas y públicas hijas en la estructura de árbol de la billetera HD. Por lo tanto, la llave privada maestra está en la profundidad 0 de derivación.

![](../../dictionnaire/assets/19.png)