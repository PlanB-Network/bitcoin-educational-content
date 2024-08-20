---
term: BIP113
---

Introdujo un cambio en el cálculo de todas las operaciones de bloqueo temporal (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence`, y `OP_CHECKSEQUENCEVERIFY`). Especifica que para evaluar la validez de los bloqueos temporales, ahora deben compararse con el MTP (*Median Time Past*, que es la mediana de los tiempos de los últimos 11 bloques). Anteriormente, solo se utilizaba el tiempo del bloque anterior. Este método hace el sistema más predecible y previene la manipulación de la referencia temporal por parte de los mineros. BIP113 fue introducido mediante un soft fork el 4 de julio de 2016, junto con BIP68 y BIP112, activados por primera vez utilizando el método BIP9.