---
term: PROBLEMA DE LOS GENERALES BIZANTINOS
---

El problema fue formulado por primera vez por Leslie Lamport, Robert Shostak y Marshall Pease en la revista especializada *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["The Byzantine Generals Problem"](https://lamport.azurewebsites.net/pubs/byz.pdf) en julio de 1982. Se utiliza hoy en día para ilustrar los desafíos en términos de toma de decisiones cuando un sistema distribuido no puede confiar en ningún actor.

En esta metáfora, un grupo de generales bizantinos y sus respectivos ejércitos están acampados alrededor de una ciudad que desean atacar o sitiar. Los generales están geográficamente separados entre sí y deben comunicarse a través de mensajeros para coordinar su estrategia. No importa si deciden atacar o retirarse, siempre y cuando todos los generales alcancen un consenso.

Por lo tanto, podemos considerar los siguientes requisitos:
* Cada general debe tomar una decisión: atacar o retirarse (sí o no);
* Una vez tomada la decisión, no se puede cambiar;
* Todos los generales deben estar de acuerdo con la misma decisión y ejecutarla de manera sincronizada.

Además, un general solo puede comunicarse con otro a través de mensajes transmitidos por un mensajero, los cuales pueden ser retrasados, destruidos, alterados o perdidos. Y aun si un mensaje se entrega con éxito, uno o más generales pueden elegir (por cualquier razón) traicionar la confianza establecida y enviar un mensaje fraudulento, sembrando el caos.

Aplicando el dilema al contexto de la blockchain de Bitcoin, cada general representa un nodo en la red, necesitando alcanzar un consenso sobre el estado del sistema. En otras palabras, la mayoría de los participantes en una red distribuida deben estar de acuerdo y ejecutar la misma acción para evitar un fracaso total. La única manera de alcanzar un consenso en este tipo de sistema distribuido es tener al menos 2/3 de los nodos de la red confiables y honestos. Por lo tanto, si la mayoría de la red decide actuar maliciosamente, el sistema es vulnerable.

> ► *Este dilema a veces también se llama "El Problema de la Difusión Confiable".*