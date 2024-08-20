---
term: DNS SEEDS
---

Puntos de conexión iniciales para nuevos nodos de Bitcoin que se unen a la red. Estas semillas, que son en realidad servidores DNS específicos, tienen su dirección permanentemente incrustada en el código de Bitcoin Core. Cuando un nuevo nodo comienza, contacta a estos servidores para obtener una lista aleatoria de direcciones IP de nodos de Bitcoin presumiblemente activos. El nuevo nodo puede entonces establecer conexiones con los nodos en esta lista para obtener la información necesaria para realizar su Descarga Inicial de Bloque (Initial Block Download, IBD) y sincronizarse con la cadena que tiene el trabajo más acumulado. A partir de 2024, aquí está la lista de semillas DNS de Bitcoin Core y las personas responsables de su mantenimiento (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):
* seed.bitcoin.sipa.be: Pieter Wuille;
* dnsseed.bluematt.me: Matt Corallo;
* dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us: Luke Dashjr;
* seed.bitcoinstats.com: Christian Decker;
* seed.bitcoin.jonasschnelli.ch: Jonas Schnelli;
* seed.btc.petertodd.net: Peter Todd;
* seed.bitcoin.sprovoost.nl: Sjors Provoost;
* dnsseed.emzy.de: Stephan Oeste;
* seed.bitcoin.wiz.biz: Jason Maurice;
* seed.mainnet.achownodes.xyz: Ava Chow.

Las DNS seeds son el segundo método, en orden de prioridad, para que un nodo de Bitcoin establezca conexiones. El primer método implica usar el archivo peers.dat que el propio nodo ha creado. Este archivo está naturalmente vacío en el caso de un nuevo nodo, a menos que el usuario lo haya modificado manualmente.

> ► *Nota, las DNS seeds no deben confundirse con "nodos semilla", que son la tercera forma de establecer conexiones.*