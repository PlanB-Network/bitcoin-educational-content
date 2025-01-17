---
term: PEER DISCOVERY

---
Proceso por el que los nodos de la red Bitcoin se conectan a otros nodos para obtener información. Cuando un nodo Bitcoin se lanza por primera vez, no tiene información sobre otros nodos de la red. Sin embargo, debe establecer conexiones para sincronizarse con la blockchain que tenga más trabajo acumulado. Para descubrir a estos pares se utilizan varios mecanismos, por orden de prioridad:


- El nodo comienza consultando su archivo local `peers.dat`, que almacena información sobre los nodos con los que ha interactuado previamente. Si el nodo es nuevo, este archivo estará vacío, y el proceso pasará al siguiente paso;
- En ausencia de información en el archivo `peers.dat` (lo que es normal para un nodo recién lanzado), el nodo realiza consultas DNS a las semillas DNS. Estos servidores proporcionan una lista de direcciones IP de nodos presumiblemente activos para establecer conexiones. Las direcciones de las semillas DNS están codificadas en el código de Bitcoin Core. Este paso suele ser suficiente para completar el descubrimiento de pares;
- Si las semillas DNS no responden en 60 segundos, el nodo puede entonces recurrir a los nodos semilla. Se trata de nodos Bitcoin públicos listados en una lista estática de casi mil entradas integrada directamente en el código fuente de Bitcoin Core. El nuevo nodo utilizará esta lista para establecer una primera conexión a la red y obtener direcciones IP de otros nodos;
- En el caso muy improbable de que fallen todos los métodos anteriores, el operador del nodo siempre tiene la opción de añadir manualmente las direcciones IP de los nodos para establecer una primera conexión.