---
term: ASUMIR UTXO

---
Un parámetro de configuración en el cliente líder Bitcoin Core que permite a un nodo que acaba de ser inicializado (pero que aún no se ha sometido al IBD) aplazar la verificación de transacciones y del conjunto de UTXO hasta una instantánea determinada. El concepto se basa en el uso de un conjunto de UTXO (una lista de todos los UTXO existentes en un momento dado) proporcionado por Core y presuntamente exacto, que permite al nodo sincronizarse muy rápidamente con la cadena con más trabajo acumulado. Como el nodo se salta el largo paso del IBD, pasa a estar operativo para su usuario muy rápidamente. Supongamos que UTXO divide la sincronización (IBD) en dos partes:


- En primer lugar, el nodo realiza la Header First Sync (verificación sólo de cabeceras) y considera válido el conjunto UTXO proporcionado por Core;
- A continuación, una vez operativo, el nodo verificará el historial completo de bloques en segundo plano, actualizando un nuevo conjunto UTXO que ha verificado él mismo. Si este nuevo conjunto UTXO no coincide con el proporcionado por Core, producirá un mensaje de error.

Por lo tanto, Assume UTXO acelera la preparación de un nuevo nodo Bitcoin posponiendo el proceso de verificación de transacciones y el conjunto UTXO a través de una instantánea actualizada proporcionada en Core.