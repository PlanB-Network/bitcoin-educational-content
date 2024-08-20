---
term: UTXO SET
---

Se refiere a la colección de todos los UTXOs existentes en un momento dado. En otras palabras, es una gran lista de todas las diferentes piezas de bitcoins esperando ser gastadas. Si sumas las cantidades de todos los UTXOs en el conjunto de UTXO, nos da la masa monetaria total de bitcoins en circulación. Cada nodo en la red de Bitcoin mantiene su propio conjunto de UTXO en tiempo real. Lo actualiza a medida que se confirman nuevos bloques válidos, con las transacciones que incluyen, las cuales consumen algunos UTXOs del conjunto de UTXO, y crean nuevos a cambio.

Este conjunto de UTXO es mantenido por cada nodo para verificar rápidamente si los UTXOs gastados en las transacciones son de hecho legítimos. Esto les permite detectar y rechazar intentos de doble gasto. El conjunto de UTXO a menudo está en el centro de las preocupaciones sobre la descentralización de Bitcoin, ya que su tamaño naturalmente aumenta muy rápidamente. Dado que una parte de él debe mantenerse en RAM para verificar transacciones en un tiempo razonable, el conjunto de UTXO podría gradualmente hacer que operar un nodo completo sea demasiado costoso. El conjunto de UTXO también tiene un impacto significativo en el IBD (*Initial Block Download*). Cuanto más del conjunto de UTXO pueda colocarse en RAM, más rápido es el IBD. En Bitcoin Core, el conjunto de UTXO se almacena en la carpeta denominada `/chainstate`.

> ► *En inglés, "UTXO set" podría traducirse como "conjunto de UTXO".*