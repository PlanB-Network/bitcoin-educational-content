---
term: BIP34
---

Soft fork aplicado en marzo de 2013, a partir del bloque 227,930, que introdujo la versión 2 para los bloques de Bitcoin. Esta nueva versión requiere que cada bloque incluya en el `scriptSig` de la transacción coinbase la altura del bloque que se está creando. Este cambio sirve para aclarar la manera en que la red acuerda modificar la estructura de los bloques y las reglas de consenso. Adicionalmente, garantiza la unicidad de cada bloque y cada transacción coinbase.