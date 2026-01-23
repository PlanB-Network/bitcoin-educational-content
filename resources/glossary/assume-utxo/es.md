---
term: Assume utxo

definition: Un parámetro de Bitcoin Core que permite la sincronización rápida de un nuevo nodo utilizando una instantánea del conjunto UTXO presumido válido, antes de verificar el historial en segundo plano.
---
Parámetro de configuración en el cliente mayoritario Bitcoin Core que permite a un nodo que acaba de ser inicializado (pero que aún no ha realizado el IBD) posponer la verificación de transacciones y del conjunto UTXO antes de un snapshot determinado. El concepto se basa en el uso de un conjunto UTXO (lista de todos los UTXOs existentes en un momento dado) proporcionado por Core y presuntamente exacto, lo que permite que el nodo se sincronice muy rápidamente en la cadena con el mayor trabajo acumulado. Dado que el nodo se salta la larga etapa del IBD, resulta funcional para su usuario muy rápidamente.

Assume UTXO divide la sincronización (IBD) en dos partes: Primero, el nodo realiza el Header First Sync (verificación de encabezados solamente) y considera válido el conjunto UTXO proporcionado por Core; Luego, una vez que es funcional, el nodo verificará el historial completo de bloques en segundo plano, actualizando un nuevo conjunto UTXO que él mismo habrá verificado. Si este último no coincide con el conjunto UTXO proporcionado por Core, mostrará un mensaje de error.

Assume UTXO permite, por tanto, acelerar la preparación de un nuevo nodo Bitcoin posponiendo el proceso de verificación de las transacciones y del conjunto UTXO gracias a un snapshot actualizado proporcionado en Core.





