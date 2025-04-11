---
term: ÁRBOL MERKLE

---
Un árbol de Merkle es un acumulador criptográfico. Es un método para demostrar la pertenencia de una determinada información a un conjunto mayor. Es una estructura de datos que facilita la verificación de información en un formato compacto. En el sistema Bitcoin, los Árboles de Merkle se utilizan para agrupar y condensar las transacciones de un bloque en un único hash, llamado Raíz de Merkle (o "*Root Hash*"). Se hace un hash de cada transacción, y luego los hashes adyacentes se juntan jerárquicamente hasta obtener la Raíz de Merkle.

![](../../dictionnaire/assets/1.webp)

Esta estructura permite verificar rápidamente si una transacción concreta está incluida en un bloque determinado sin tener que analizar todas las transacciones. Por ejemplo, si sólo dispongo de la raíz Merkle y quiero verificar que `TX 7` efectivamente forma parte del árbol, sólo necesitaría las siguientes pruebas:


- `TX 7`;
- `HASH 8`;
- `HASH 5-6`;
- `HASH 1-2-3-4`.

Con estos datos, puedo calcular los nodos intermedios hasta la raíz de Merkle.

![](../../dictionnaire/assets/2.webp)

Los árboles de Merkle se utilizan sobre todo para los nodos ligeros (conocidos como "SPV") que sólo conservan las cabeceras de bloque, pero no las transacciones. Esta estructura también se encuentra en el protocolo UTREEXO, un protocolo que permite condensar el conjunto de nodos UTXO, y en el MAST Taproot.

> ► *El Árbol de Merkle debe su nombre a Ralph Merkle, un criptógrafo que diseñó esta estructura en 1979. Un Árbol de Merkle también puede denominarse "árbol de hash". En francés, se denomina "Arbre de Merkle" o "arbre de hachage"