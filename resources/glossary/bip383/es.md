---
term: BIP383

---
Introduce las funciones `multi(NUM, CLAVE, ..., CLAVE)` y `sortedmulti(NUM, CLAVE, ..., CLAVE)` para los descriptores. Estas funciones permiten la descripción de scripts multifirma en los descriptores, con `sortedmulti` ordenando las claves públicas en orden lexicográfico para asegurar la compatibilidad durante la importación. BIP383 fue implementado junto con todos los demás BIPs relacionados con descriptores (excepto BIP386) en la versión 0.17 de Bitcoin Core.