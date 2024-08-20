---
term: SCRIPTWITNESS
---

Un elemento en las entradas de transacción SegWit que contiene las firmas y claves públicas necesarias para desbloquear los bitcoins enviados en la transacción. Similar al `scriptSig` de las transacciones Legacy, el `scriptWitness` no se coloca, sin embargo, en la misma ubicación. De hecho, es esta parte, referida como el "testigo" (`*witness*` en inglés), la que se mueve a una base de datos separada con el fin de resolver el problema de maleabilidad de las transacciones. Cada entrada SegWit tiene su propio `scriptWitness`, y todos los elementos `scriptWitness` juntos forman el campo `Witness` de la transacción.

> ► *Ten cuidado de no confundir `scriptWitness` con `witnessScript`. Mientras que el `scriptWitness` contiene los datos de testigo para cualquier entrada SegWit, el `witnessScript` define las condiciones de gasto de un UTXO P2WSH o P2SH-P2WSH y constituye un script por derecho propio, similar al `redeemScript` para una salida P2SH.*