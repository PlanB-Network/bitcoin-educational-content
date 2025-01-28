---
term: DNS SEMILLAS

---
Puntos de conexión iniciales para los nuevos nodos Bitcoin que se unen a la red. Estas semillas, que en realidad son servidores DNS específicos, tienen su dirección permanentemente incrustada en el código Bitcoin Core. Cuando un nuevo nodo se inicia, contacta con estos servidores para obtener una lista aleatoria de direcciones IP de nodos Bitcoin presumiblemente activos. El nuevo nodo puede entonces establecer conexiones con los nodos de esta lista para obtener la información necesaria para realizar su Descarga Inicial de Bloques (IBD) y sincronizarse con la cadena que tenga más trabajo acumulado. A partir de 2024, esta es la lista de semillas DNS de Bitcoin Core y los individuos responsables de su mantenimiento (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):


- seed.bitcoin.sipa.be: Pieter Wuille;
- dnsseed.bluematt.me: Matt Corallo;
- dnsseed.bitcoin.dashjr-lista-de-nodos-p2p.us: Luke Dashjr;
- seed.bitcoinstats.com: Christian Decker;
- seed.bitcoin.jonasschnelli.ch: Jonas Schnelli;
- seed.btc.petertodd.net: Peter Todd;
- seed.bitcoin.sprovoost.nl: Sjors Provoost;
- dnsseed.emzy.de: Stephan Oeste;
- seed.bitcoin.wiz.biz: Jason Maurice;
- seed.mainnet.achownodes.xyz: Ava Chow.

Las semillas DNS son el segundo método, en orden de prioridad, para que un nodo Bitcoin establezca conexiones. El primer método consiste en utilizar el archivo peers.dat que el propio nodo ha creado. Este archivo está naturalmente vacío en el caso de un nodo nuevo, a menos que el usuario lo haya modificado manualmente.

> ► *Nota, las semillas DNS no deben confundirse con los "nodos semilla", que son la tercera forma de establecer conexiones.*