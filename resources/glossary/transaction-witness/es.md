---
term: TRANSACTION WITNESS
---

Se refiere a un componente de las transacciones de Bitcoin que fue trasladado con el soft fork SegWit para abordar el problema de la maleabilidad de las transacciones. El testigo contiene las firmas y claves públicas necesarias para desbloquear los bitcoins gastados en una transacción. En las transacciones Legacy, el testigo representaba la suma de `scriptSig` de todas las entradas. En las transacciones SegWit, el testigo representa la suma de `scriptWitness` para cada entrada, y esta parte de la transacción ahora se mueve a un árbol de Merkle separado dentro del bloque.

Antes de SegWit, las firmas podían ser ligeramente alteradas sin ser invalidadas antes de que una transacción fuera confirmada, lo que cambiaba el identificador de la transacción. Esto dificultaba la construcción de varios protocolos, ya que una transacción no confirmada podía ver su identificador cambiar. Al separar los testigos, SegWit hace que las transacciones no sean maleables, ya que cualquier cambio en las firmas ya no afecta el identificador de la transacción (TXID), sino solo el identificador del testigo (WTXID). Además de resolver el problema de la maleabilidad, esta separación permite un aumento en la capacidad de cada bloque.

> ► *En inglés, "témoin" se traduce como "witness".*