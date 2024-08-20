---
term: HUELLA DIGITAL MAESTRA
---

Una huella digital de 4 bytes (32 bits) de la clave privada maestra en una billetera Determinista Jerárquica (HD). Se obtiene calculando el hash `SHA256` de la clave privada maestra, seguido de un hash `RIPEMD160`, un proceso al que se hace referencia como `HASH160` en Bitcoin. La Huella Digital Maestra se utiliza para identificar una billetera HD, independientemente de los caminos de derivación, pero teniendo en cuenta la presencia o ausencia de una frase de paso. Es información concisa que permite hacer referencia al origen de un conjunto de claves, sin revelar información sensible sobre la billetera.