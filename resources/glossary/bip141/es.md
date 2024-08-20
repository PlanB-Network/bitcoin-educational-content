---
term: BIP141
---

Introdujo el concepto de Testigo Segregado (SegWit) que dio nombre al soft fork SegWit. BIP141 introduce una modificación importante en el protocolo de Bitcoin con el objetivo de resolver el problema de la maleabilidad de las transacciones. SegWit separa el testigo (datos de firma) del resto de los datos de la transacción. Esta separación se logra insertando los testigos en una estructura de datos separada, comprometida en un nuevo árbol de Merkle, que a su vez se referencia en el bloque a través de la transacción coinbase, haciendo que SegWit sea compatible con versiones anteriores del protocolo.