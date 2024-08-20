---
term: NODOS SEMILLA
---

Lista estática de nodos públicos de Bitcoin, integrada directamente en el código fuente de Bitcoin Core (`bitcoin/src/chainparamsseeds.h`). Esta lista sirve como puntos de conexión para nuevos nodos de Bitcoin que se unen a la red, pero solo se utiliza si las semillas DNS no proporcionan una respuesta dentro de los 60 segundos de su solicitud. En este caso, el nuevo nodo de Bitcoin se conectará a estos nodos semilla para establecer una primera conexión con la red y solicitar direcciones IP de otros nodos. El objetivo final es adquirir la información necesaria para realizar la Descarga Inicial de Bloques (Initial Block Download, IBD) y sincronizarse con la cadena que tiene el mayor trabajo acumulado. La lista de nodos semilla incluye casi 1000 nodos, identificados de acuerdo con el estándar establecido por el BIP155. Así, los nodos semilla representan el tercer método de conexión a la red para un nodo de Bitcoin, después del posible uso del archivo `peers.dat`, creado por el propio nodo, y la solicitud de semillas DNS.

> ► *Nota, los nodos semilla no deben confundirse con "semillas DNS", que son el segundo método de establecimiento de conexiones.*