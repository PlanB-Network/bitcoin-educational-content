---
term: P2WSH

---
P2WSH significa *Pay to Witness Script Hash*. Es un modelo de script estándar utilizado para establecer condiciones de gasto en un UTXO. P2WSH se introdujo con la implementación de SegWit en agosto de 2017.

Este script es similar a P2SH (*Pay to Public Script Hash*), ya que también bloquea bitcoins basándose en el hash de un script. La diferencia radica en cómo se incluyen las firmas y los scripts en la transacción. Para gastar los bitcoins en este tipo de script, el receptor debe proporcionar el script original, llamado `witnessScript` (equivalente a `redeemScript`), junto con las firmas requeridas. Este mecanismo permite implementar condiciones de gasto más sofisticadas, como multisigs.

En el contexto de P2WSH, la información del script de firma (el `scriptWitness`, equivalente a `scriptSig`) se traslada de la estructura tradicional de transacciones a una sección separada llamada `Witness`. Este movimiento es una característica de la actualización SegWit (*Segregated Witness*) que ayuda a prevenir la falsificación de firmas. Las transacciones P2WSH son generalmente menos costosas en términos de tasas en comparación con las transacciones Legacy, ya que la parte en el testigo cuesta menos.

Las direcciones P2WSH se escriben utilizando la codificación `Bech32` con una suma de comprobación en forma de código BCH. Estas direcciones siempre empiezan por `bc1q`. P2WSH es una salida SegWit de la versión 0.