---
term: NODOS DE SEMILLAS

---
Lista estática de nodos Bitcoin públicos, integrada directamente en el código fuente de Bitcoin Core (`bitcoin/src/chainparamsseeds.h`). Esta lista sirve como puntos de conexión para los nuevos nodos Bitcoin que se unan a la red, pero sólo se utiliza si las semillas DNS no proporcionan una respuesta en los 60 segundos siguientes a su solicitud. En este caso, el nuevo nodo Bitcoin se conectará a estos nodos semilla para establecer una primera conexión a la red y solicitar direcciones IP de otros nodos. El objetivo final es adquirir la información necesaria para realizar la Descarga Inicial de Bloques (IBD) y sincronizarse con la cadena que tenga más trabajo acumulado. La lista de nodos semilla incluye cerca de 1000 nodos, identificados de acuerdo con el estándar establecido por BIP155. Así, los nodos semilla representan el tercer método de conexión a la red para un nodo Bitcoin, tras el posible uso del fichero `peers.dat`, creado por el propio nodo, y la solicitud de semillas DNS.

> ► *Nota, los nodos semilla no deben confundirse con las "semillas DNS", que son el segundo método para establecer conexiones.*