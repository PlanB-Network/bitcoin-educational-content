---
term: TESTIGO DE TRANSACCIONES

---
Se refiere a un componente de las transacciones de Bitcoin que se trasladó con la bifurcación suave SegWit para abordar el problema de la maleabilidad de las transacciones. El testigo contiene las firmas y claves públicas necesarias para desbloquear los bitcoins gastados en una transacción. En las transacciones Legacy, el testigo representaba la suma de `scriptSig` de todas las entradas. En las transacciones SegWit, el testigo representa la suma de `scriptWitness` de cada entrada, y esta parte de la transacción se traslada ahora a un árbol Merkle separado dentro del bloque.

Antes de SegWit, las firmas podían alterarse ligeramente sin ser invalidadas antes de que se confirmara una transacción, lo que cambiaba el identificador de la transacción. Esto dificultaba la construcción de diversos protocolos, ya que una transacción no confirmada podía ver modificado su identificador. Al separar los testigos, SegWit hace que las transacciones no sean maleables, ya que cualquier cambio en las firmas ya no afecta al identificador de la transacción (TXID), sino sólo al identificador del testigo (WTXID). Además de resolver el problema de la maleabilidad, esta separación permite aumentar la capacidad de cada bloque.

> ► *En inglés, "témoin" se traduce como "witness "*