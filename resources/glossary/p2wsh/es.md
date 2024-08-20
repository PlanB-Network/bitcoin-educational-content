---
term: P2WSH
---

P2WSH significa *Pay to Witness Script Hash* (Pago a Testigo de Hash de Script). Es un modelo de script estándar utilizado para establecer condiciones de gasto en un UTXO. P2WSH fue introducido con la implementación de SegWit en agosto de 2017.

Este script es similar a P2SH (*Pay to Public Script Hash*, Pago al Hash del Script Público), ya que también bloquea bitcoins basándose en el hash de un script. La diferencia radica en cómo se incluyen las firmas y los scripts en la transacción. Para gastar los bitcoins en este tipo de script, el destinatario debe proporcionar el script original, llamado `witnessScript` (equivalente a `redeemScript`), junto con las firmas requeridas. Este mecanismo permite la implementación de condiciones de gasto más sofisticadas, como multisigs.

En el contexto de P2WSH, la información del script de firma (el `scriptWitness`, equivalente a `scriptSig`) se mueve de la estructura tradicional de la transacción a una sección separada llamada `Witness`. Este cambio es una característica de la actualización SegWit (*Segregated Witness*, Testigo Segregado) que ayuda a prevenir la maleabilidad de firmas. Las transacciones P2WSH generalmente son menos costosas en términos de comisiones comparadas con las transacciones Legacy, ya que la parte en el testigo cuesta menos.

Las direcciones P2WSH se escriben usando la codificación `Bech32` con un código de verificación de suma de comprobación en forma de código BCH. Estas direcciones siempre comienzan con `bc1q`. P2WSH es una salida SegWit versión 0.