---
term: ASSUME UTXO
---

Un parámetro de configuración en el cliente principal de Bitcoin Core que permite a un nodo que acaba de ser inicializado (pero que aún no ha pasado por el IBD) posponer la verificación de transacciones y el conjunto de UTXO hasta un snapshot dado. El concepto se basa en el uso de un conjunto de UTXO (una lista de todos los UTXOs existentes en un momento dado) proporcionado por Core y considerado preciso, lo que permite que el nodo se sincronice muy rápidamente con la cadena con el trabajo más acumulado. Dado que el nodo omite el largo paso del IBD, se vuelve operativo para su usuario muy rápidamente. Assume UTXO divide la sincronización (IBD) en dos partes:
* Primero, el nodo realiza la Sincronización Primero de Cabeceras (verificación solo de cabeceras) y considera el conjunto de UTXO proporcionado por Core como válido;
* Luego, una vez que es operativo, el nodo verificará el historial completo de bloques en segundo plano, actualizando un nuevo conjunto de UTXO que ha verificado por sí mismo. Si este nuevo conjunto de UTXO no coincide con el proporcionado por Core, producirá un mensaje de error.

Por lo tanto, Assume UTXO acelera la preparación de un nuevo nodo de Bitcoin posponiendo el proceso de verificación de transacciones y el conjunto de UTXO a través de un snapshot actualizado proporcionado en Core.