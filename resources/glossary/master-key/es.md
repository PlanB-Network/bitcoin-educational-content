---
term: LLAVE MAESTRA

---
En el contexto de los monederos HD (Hierarchical Deterministic), la clave privada maestra es una clave privada única derivada de la semilla del monedero. Para obtener la clave maestra, se aplica la función `HMAC-SHA512` a la semilla, utilizando las palabras "*Bitcoin seed*" literalmente como clave. El resultado de esta operación produce una salida de 512 bits, de los cuales los 256 primeros constituyen la clave maestra y los 256 restantes forman el código de la cadena maestra. La clave maestra y el código de la cadena maestra sirven como punto de partida para derivar todas las claves privadas y públicas secundarias en la estructura de árbol del monedero HD. Por lo tanto, la clave privada maestra se encuentra en la profundidad 0 de derivación.

![](../../dictionnaire/assets/19.webp)