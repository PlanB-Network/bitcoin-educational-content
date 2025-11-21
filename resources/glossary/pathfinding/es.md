---
term: PATHFINDING
---

Proceso utilizado por un nodo para determinar la ruta óptima para encaminar un pago a través de la red de canales Lightning. La búsqueda de la ruta la realiza el nodo pagador, que debe seleccionar los nodos intermedios más adecuados para llegar al destinatario. Esta elección se basa en una serie de criterios, como las tarifas, la capacidad del canal y los plazos.


Los algoritmos de búsqueda de rutas construyen un gráfico de la topología de la red a partir de los datos de cotilleo y evalúan las distintas rutas posibles entre el nodo pagador y el receptor. Estas rutas se clasifican de mejor a peor según diversos criterios. A continuación, el nodo prueba estas rutas hasta que consigue realizar el pago en una de ellas.