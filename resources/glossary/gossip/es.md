---
term: GOSSIP
---

Gossip es un algoritmo distribuido peer-to-peer (P2P) para difundir información de forma epidémica a todos los agentes de la red. Para Bitcoin, Lightning y otros sistemas distribuidos, este protocolo permite intercambiar y sincronizar los Global State de los nodos en unos pocos ciclos. Cada nodo propaga información a uno o varios vecinos aleatorios o no aleatorios, que a su vez propagan la información a otros vecinos, y así sucesivamente, hasta alcanzar un estado sincronizado globalmente.


En Lightning, el cotilleo es un protocolo de comunicación entre nodos para compartir información sobre el estado actual y la topología de la red. El protocolo de cotilleo permite a los nodos conocer el estado dinámico de los canales de pago y de otros nodos, para facilitar el enrutamiento de las transacciones a través de la red sin necesidad de conexiones directas entre todos los nodos.


> ► *En francés, "gossip protocol" podría traducirse como "protocole de bavardage". Fuente : https://dl.acm.org/doi/pdf/10.1145/41840.41841.*