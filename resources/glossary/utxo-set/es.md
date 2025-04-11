---
term: UTXO SET

---
Se refiere a la colección de todos los UTXOs existentes en un momento dado. En otras palabras, es una gran lista de todas las diferentes piezas de bitcoins a la espera de ser gastadas. Si se suman las cantidades de todos los UTXOs en el conjunto de UTXOs, nos da la masa monetaria total de bitcoins en circulación. Cada nodo de la red Bitcoin mantiene su propio conjunto UTXO en tiempo real. Lo actualiza a medida que se confirman nuevos bloques válidos, con las transacciones que incluyen, que consumen algunos UTXOs del conjunto UTXO, y crean otros nuevos a cambio.

Cada nodo conserva este conjunto de UTXO para verificar rápidamente si los UTXO gastados en las transacciones son realmente legítimos. Esto les permite detectar y rechazar intentos de doble gasto. El conjunto UTXO es a menudo el centro de las preocupaciones sobre la descentralización de Bitcoin, ya que su tamaño aumenta de forma natural muy rápidamente. Dado que una parte debe mantenerse en RAM para verificar las transacciones en un tiempo razonable, el conjunto UTXO podría hacer gradualmente que operar un nodo completo fuera demasiado costoso. El conjunto UTXO también tiene un impacto significativo en el IBD (*Descarga Inicial de Bloques*). Cuanto más del conjunto UTXO pueda colocarse en la RAM, más rápido será el IBD. En Bitcoin Core, el conjunto UTXO se almacena en la carpeta llamada `/chainstate`.

> ► *En inglés, "UTXO set" podría traducirse como "UTXO set".*