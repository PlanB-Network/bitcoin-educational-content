---
term: UTREEXO
---

Protocolo diseñado por Tadge Dryja para compactar el conjunto de UTXO de los nodos de Bitcoin utilizando un acumulador basado en árboles de Merkle. A diferencia del conjunto de UTXO clásico que requiere un espacio de almacenamiento significativo, Utreexo reduce drásticamente la memoria necesaria al almacenar solo las raíces de los árboles de Merkle. Esto permite que el nodo verifique la existencia de UTXOs utilizados en las entradas de transacciones, sin tener que mantener el conjunto completo de UTXOs. Al usar Utreexo, cada nodo solo retiene una huella criptográfica llamada raíz de Merkle. Cuando se realiza una transacción, el usuario proporciona las pruebas de propiedad de los UTXOs y los caminos de Merkle correspondientes. Así, el nodo puede verificar transacciones sin almacenar el conjunto completo de UTXO. Tomemos un ejemplo con un diagrama para entender este mecanismo:

![](../../dictionnaire/assets/15.png)

En este ejemplo, reduje intencionalmente el conjunto de UTXO a 4 UTXOs para facilitar la comprensión. En realidad, es importante imaginar que hay casi 140 millones de UTXOs en Bitcoin en el momento de escribir estas líneas. En este diagrama, el nodo Utreexo solo necesitaría mantener la Raíz de Merkle en RAM. Si recibe una transacción que gasta el UTXO No. 3 (en negro), la prueba consistiría en los siguientes elementos:
* UTXO 3;
* HASH 4;
* HASH 1-2.

Con esta información transmitida por el remitente de la transacción, el nodo Utreexo realiza las siguientes verificaciones:
* Calcula la huella de UTXO 3, lo que le da HASH 3;
* Concatena HASH 3 con HASH 4;
* Calcula su huella, lo que le da HASH 3-4;
* Concatena HASH 3-4 con HASH 1-2;
* Calcula su huella, lo que le da la raíz de Merkle.

Si la raíz de Merkle que obtiene a través de su proceso es la misma que la raíz de Merkle que almacenó en su RAM, entonces está convencido de que el UTXO No. 3 es de hecho parte del conjunto de UTXO.
Este método reduce los requisitos de RAM para los operadores de nodos completos. Sin embargo, Utreexo tiene limitaciones, incluyendo un aumento en el tamaño del bloque debido a pruebas adicionales y la dependencia potencial de los nodos Utreexo en los Nodos Puente para obtener pruebas faltantes. Los Nodos Puente son nodos completos tradicionales que proporcionan las pruebas necesarias a los nodos Utreexo, permitiendo así la verificación completa. Este enfoque ofrece un compromiso entre eficiencia y descentralización, haciendo la validación de transacciones más accesible para usuarios con recursos limitados.