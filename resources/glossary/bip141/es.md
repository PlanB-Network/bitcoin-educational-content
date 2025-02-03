---
term: BIP141

---
Introdujo el concepto de Testigo Segregado (SegWit) que dio nombre a la bifurcación suave SegWit. BIP141 introduce una importante modificación en el protocolo Bitcoin destinada a resolver el problema de la maleabilidad de las transacciones. SegWit separa el testigo (datos de la firma) del resto de los datos de la transacción. Esta separación se consigue insertando los testigos en una estructura de datos separada, comprometida en un nuevo árbol Merkle, que a su vez es referenciada en el bloque a través de la transacción coinbase, haciendo SegWit compatible con versiones anteriores del protocolo.