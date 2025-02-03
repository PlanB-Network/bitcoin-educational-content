---
term: NODO PODADO

---
Un nodo podado, en inglés "Pruned Node", es un nodo completo que realiza la poda de la blockchain. Se trata de eliminar progresivamente los bloques más antiguos, tras haberlos verificado debidamente, para conservar sólo los bloques más recientes. El límite de retención se especifica en el archivo `bitcoin.conf` mediante el parámetro `prune=n`, donde `n` es el tamaño máximo que ocupan los bloques en megabytes (MB). Si se anota `0` después de este parámetro, se desactiva la poda y el nodo retiene la cadena de bloques en su totalidad.

Los nodos podados se consideran a veces tipos de nodos diferentes de los nodos completos. El uso de un nodo podado puede ser especialmente interesante para los usuarios con limitaciones de capacidad de almacenamiento. Actualmente, un nodo completo debe tener casi 600 GB sólo para almacenar la cadena de bloques. Un nodo podado puede limitar el almacenamiento necesario a 550 MB. Aunque utiliza menos espacio en disco, un nodo podado mantiene un nivel de verificación y validación similar al de un nodo completo. Por tanto, los nodos podados ofrecen más confianza a sus usuarios en comparación con los nodos ligeros (SPV).