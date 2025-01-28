---
term: HUELLA MAESTRA

---
Una huella digital de 4 bytes (32 bits) de la clave privada maestra en un monedero Determinista Jerárquico (HD). Se obtiene calculando el hash `SHA256` de la clave privada maestra, seguido de un hash `RIPEMD160`, un proceso denominado `HASH160` en Bitcoin. La huella maestra se utiliza para identificar un monedero HD, independientemente de las rutas de derivación, pero teniendo en cuenta la presencia o ausencia de una frase de contraseña. Es una información concisa que permite referenciar el origen de un conjunto de claves, sin revelar información sensible sobre el monedero.