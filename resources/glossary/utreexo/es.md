---
term: UTREEXO

---
Protocolo diseñado por Tadge Dryja para compactar el conjunto UTXO de los nodos Bitcoin utilizando un acumulador basado en árboles de Merkle. A diferencia del conjunto UTXO clásico, que requiere un espacio de almacenamiento significativo, Utreexo reduce drásticamente la memoria necesaria almacenando únicamente las raíces del árbol de Merkle. Esto permite al nodo verificar la existencia de UTXOs utilizados en las entradas de transacciones, sin tener que guardar el conjunto completo de UTXOs. Al utilizar Utreexo, cada nodo sólo conserva una huella criptográfica llamada raíz Merkle. Cuando se realiza una transacción, el usuario proporciona las pruebas de propiedad de los UTXO y las rutas Merkle correspondientes. Así, el nodo puede verificar las transacciones sin almacenar todo el conjunto de UTXO. Veamos un ejemplo con un diagrama para entender este mecanismo:

![](../../dictionnaire/assets/15.webp)

En este ejemplo, he reducido intencionadamente el conjunto de UTXOs a 4 UTXOs para facilitar la comprensión. En realidad, es importante imaginar que hay casi 140 millones de UTXOs en Bitcoin en el momento de escribir estas líneas. En este diagrama, el nodo Utreexo sólo necesitaría mantener la Raíz Merkle en RAM. Si recibe una transacción gastando el UTXO nº 3 (en negro), la prueba consistiría en los siguientes elementos:


- UTXO 3;
- HASH 4;
- HASH 1-2.

Con esta información transmitida por el emisor de la transacción, el nodo Utreexo realiza las siguientes comprobaciones:


- Calcula la huella de UTXO 3, que le da HASH 3;
- Concatena HASH 3 con HASH 4;
- Calcula su huella, que le da HASH 3-4;
- Concatena HASH 3-4 con HASH 1-2;
- Calcula su huella, que le da la raíz de Merkle.

Si la raíz de Merkle que obtiene a través de su proceso es la misma que la raíz de Merkle que almacenó en su memoria RAM, entonces está convencido de que el UTXO nº 3 forma parte efectivamente del conjunto UTXO.

Este método reduce los requisitos de RAM de los operadores de nodos completos. Sin embargo, Utreexo tiene limitaciones, como el aumento del tamaño del bloque debido a las pruebas adicionales y la posible dependencia de los nodos Utreexo de los nodos puente para obtener las pruebas que faltan. Los nodos puente son nodos completos tradicionales que proporcionan las pruebas necesarias a los nodos Utreexo, permitiendo así una verificación completa. Este enfoque ofrece un compromiso entre eficiencia y descentralización, haciendo la validación de transacciones más accesible a usuarios con recursos limitados.