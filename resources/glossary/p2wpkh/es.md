---
term: P2WPKH
---

P2WPKH significa *Pay to Witness Public Key Hash* (Pago al Hash de la Clave Pública Testigo). Es un modelo de script estándar utilizado para establecer condiciones de gasto en un UTXO. P2WPKH fue introducido con la implementación de SegWit en agosto de 2017.

Este script es similar a P2PKH (*Pay to Public Key Hash*, Pago al Hash de la Clave Pública), ya que también bloquea bitcoins basándose en el hash de una clave pública, es decir, una dirección de recepción. La diferencia radica en cómo se incluyen las firmas y los scripts en la transacción. En el caso de P2WPKH, la información del script de firma (`scriptSig`) se mueve de la estructura tradicional de la transacción a una sección separada llamada `Witness` (Testigo). Este cambio es una característica de la actualización SegWit (*Segregated Witness*, Testigo Segregado) que ayuda a prevenir la maleabilidad de firmas. Las transacciones P2WPKH generalmente son menos costosas en términos de comisiones comparadas con las transacciones Legacy, ya que la parte en el testigo cuesta menos.

Las direcciones P2WPKH se escriben usando la codificación `Bech32` con un código de verificación de suma de comprobación en forma de código BCH. Estas direcciones siempre comienzan con `bc1q`. P2WPKH es una salida SegWit versión 0.