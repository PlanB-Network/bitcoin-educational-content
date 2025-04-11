---
term: TESTIGO DE GUIÓN

---
Un elemento en las entradas de transacciones SegWit que contiene las firmas y claves públicas necesarias para desbloquear los bitcoins enviados en la transacción. Similar al `scriptSig` de las transacciones Legacy, el `scriptWitness`, sin embargo, no se coloca en la misma ubicación. De hecho, es esta parte, denominada "testigo" (`*witness*` en inglés), la que se traslada a una base de datos independiente para resolver el problema de la maleabilidad de las transacciones. Cada entrada SegWit tiene su propio `scriptWitness`, y todos los elementos `scriptWitness` juntos forman el campo `Witness` de la transacción.

> ► *Ten cuidado de no confundir `scriptWitness` con `witnessScript`. Mientras que el `scriptWitness` contiene los datos del testigo para cualquier entrada SegWit, el `witnessScript` define las condiciones de gasto de un P2WSH o P2SH-P2WSH UTXO y constituye un script por derecho propio, similar al `redeemScript` para una salida P2SH.*