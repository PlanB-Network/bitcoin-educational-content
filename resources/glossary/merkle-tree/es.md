---
term: MERKLE TREE
---

Un Merkle Tree es un acumulador criptográfico. Es un método para probar la membresía de un dato específico dentro de un conjunto más grande. Es una estructura de datos que facilita la verificación de información en un formato compacto. En el sistema de Bitcoin, los Merkle Trees se utilizan para agrupar y condensar las transacciones de un bloque en un único hash, llamado la Raíz de Merkle (o "*Root Hash*"). Cada transacción se hashea, luego los hashes adyacentes se hashean juntos jerárquicamente hasta obtener la Raíz de Merkle.

![](../../dictionnaire/assets/1.png)

Esta estructura permite la verificación rápida de si una transacción específica está incluida en un bloque dado sin tener que analizar todas las transacciones. Por ejemplo, si solo tengo la Raíz de Merkle y quiero verificar que `TX 7` es realmente parte del árbol, solo necesitaría las siguientes pruebas:
* `TX 7`;
* `HASH 8`;
* `HASH 5-6`;
* `HASH 1-2-3-4`.
Con estas piezas de información, soy capaz de calcular los nodos intermedios hasta la Raíz de Merkle.

![](../../dictionnaire/assets/2.png)

Los Merkle Trees se utilizan notablemente para nodos ligeros (conocidos como "SPV") que solo mantienen los encabezados de los bloques, pero no las transacciones. Esta estructura también se encuentra en el protocolo UTREEXO, un protocolo que permite condensar el conjunto de UTXO de los nodos, y en el MAST Taproot.

> ► *El Merkle Tree lleva el nombre de Ralph Merkle, un criptógrafo que diseñó esta estructura en 1979. Un Merkle Tree también puede llamarse "árbol de hash". En francés, se le conoce como "Arbre de Merkle" o "arbre de hachage".*