---
term: TRANSACCIÓN CRUDO
---

Una transacción de Bitcoin que se construye y firma, existiendo en su forma binaria. Una transacción cruda (*raw TX*) es la representación final de una transacción, justo antes de ser transmitida en la red. Esta transacción contiene toda la información necesaria para su inclusión en un bloque:
* La versión;
* La bandera;
* Las entradas;
* Las salidas;
* El tiempo de bloqueo;
* El testigo.

Lo que se refiere como una "*transacción cruda*" representa los datos crudos que se pasan por la función hash SHA256 dos veces para generar el TXID de la transacción. Estos datos se utilizan luego en el árbol de Merkle del bloque para integrar la transacción en la blockchain.

> ► *Este concepto también se llama a veces "Transacción Serializada". En francés, estos términos podrían traducirse respectivamente como "transaction brute" y "transaction sérialisée".*