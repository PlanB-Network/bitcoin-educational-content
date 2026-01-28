---
term: Índice de bloques

definition: Estructura LevelDB en Bitcoin Core que cataloga los metadatos y las ubicaciones de los bloques.
---
Una estructura de datos LevelDB en Bitcoin Core que cataloga metadatos sobre todos los bloques. Cada entrada de este índice proporciona detalles como el identificador del bloque, su altura en la cadena de bloques, el puntero al bloque en la base de datos y otros metadatos. Esta indexación permite recuperar rápidamente un bloque almacenado en memoria.