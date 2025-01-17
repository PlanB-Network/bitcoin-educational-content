---
term: PROBLEMA DE LOS GENERALES BIZANTINOS

---
El problema fue formulado por primera vez por Leslie Lamport, Robert Shostak y Marshall Pease en la revista especializada *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["The Byzantine Generals Problem"](https://lamport.azurewebsites.net/pubs/byz.pdf) en julio de 1982. Se utiliza hoy para ilustrar los retos en términos de toma de decisiones cuando un sistema distribuido no puede confiar en ningún actor.

En esta metáfora, un grupo de generales bizantinos y sus respectivos ejércitos acampan en torno a una ciudad que desean atacar o asediar. Los generales están separados geográficamente entre sí y deben comunicarse a través de mensajeros para coordinar su estrategia. No importa si atacan o se retiran, siempre que todos los generales lleguen a un consenso.

Por lo tanto, podemos considerar los siguientes requisitos:


- Cada general debe tomar una decisión: atacar o retirarse (sí o no);
- Una vez tomada la decisión, no puede cambiarse;
- Todos los generales deben estar de acuerdo en la misma decisión y ejecutarla de forma sincronizada.

Además, un general sólo puede comunicarse con otro a través de mensajes transmitidos por un mensajero, que pueden retrasarse, destruirse, alterarse o perderse. E incluso si un mensaje se entrega con éxito, uno o varios generales pueden decidir (por la razón que sea) traicionar la confianza establecida y enviar un mensaje fraudulento, sembrando el caos.

Aplicando el dilema al contexto de la blockchain de Bitcoin, cada general representa un nodo de la red, que necesita alcanzar un consenso sobre el estado del sistema. En otras palabras, la mayoría de los participantes en una red distribuida deben ponerse de acuerdo y ejecutar la misma acción para evitar un fracaso total. La única forma de alcanzar un consenso en este tipo de sistema distribuido es que al menos 2/3 de los nodos de la red sean fiables y honestos. Por lo tanto, si la mayoría de la red decide actuar maliciosamente, el sistema es vulnerable.

> ► *Este dilema a veces también se denomina "El problema de la difusión fiable "*