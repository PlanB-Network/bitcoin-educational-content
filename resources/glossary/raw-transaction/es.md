---
term: TRANSACCIÓN BRUTA

---
Una transacción Bitcoin construida y firmada, existente en su forma binaria. Una transacción en bruto (*raw TX*) es la representación final de una transacción, justo antes de que se difunda en la red. Esta transacción contiene toda la información necesaria para su inclusión en un bloque:


- La versión;
- La bandera;
- Las entradas;
- Las salidas;
- El tiempo de cierre;
- El testigo.

Lo que se conoce como "*transacción en bruto*" representa los datos en bruto que se pasan dos veces por la función hash SHA256 para generar el TXID de la transacción. A continuación, estos datos se utilizan en el árbol de Merkle del bloque para integrar la transacción en la cadena de bloques.

> ► *Este concepto también se denomina a veces "transacción serializada". En francés, estos términos podrían traducirse respectivamente por "transaction brute" y "transaction sérialisée".*