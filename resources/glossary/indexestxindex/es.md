---
term: ÍNDICES/TXINDEX/

---
Archivos en Bitcoin Core que se dedican a indexar todas las transacciones presentes en el blockchain. Esta indexación permite buscar rápidamente información detallada sobre una transacción utilizando su identificador (TXID), sin tener que recorrer todo el blockchain. La creación de estos archivos de indexación es una opción no habilitada por defecto en Bitcoin Core. Si esta característica no está habilitada, su nodo sólo indexará las transacciones asociadas a los monederos adjuntos a su nodo. Para habilitar la indexación de todas las transacciones, debe establecer el parámetro `-txindex=1` en el archivo `bitcoin.conf`. Esta opción es particularmente útil para aplicaciones y servicios que buscan frecuentemente en el historial de transacciones de Bitcoin.