---
term: BIP0065

definition: Introducción del código de operación OP_CHECKLOCKTIMEVERIFY que permite bloquear bitcoins hasta una fecha o altura de bloque específica.
---
Se ha introducido un nuevo opcode denominado `OP_CHECKLOCKTIMEVERIFY` que permite inutilizar un UTXO hasta un momento futuro especificado. La implementación de este BIP requirió una bifurcación suave, que se produjo el 14 de diciembre de 2015. También introdujo la versión 4 de los bloques.