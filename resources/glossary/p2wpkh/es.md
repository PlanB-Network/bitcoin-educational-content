---
term: P2WPKH

---
P2WPKH son las siglas de *Pay to Witness Public Key Hash*. Es un modelo de escritura estándar utilizado para establecer condiciones de gasto en un UTXO. P2WPKH se introdujo con la implementación de SegWit en agosto de 2017.

Este script es similar a P2PKH (*Pay to Public Key Hash*), ya que también bloquea bitcoins basándose en el hash de una clave pública, es decir, una dirección receptora. La diferencia radica en cómo se incluyen las firmas y los scripts en la transacción. En el caso de P2WPKH, la información del script de firma (`scriptSig`) se traslada de la estructura de transacción tradicional a una sección separada llamada `Witness`. Este movimiento es una característica de la actualización SegWit (*Segregated Witness*) que ayuda a prevenir la falsificación de firmas. Las transacciones P2WPKH son generalmente menos costosas en términos de tasas en comparación con las transacciones Legacy, ya que la parte en el testigo cuesta menos.

Las direcciones P2WPKH se escriben utilizando la codificación `Bech32` con una suma de comprobación en forma de código BCH. Estas direcciones siempre empiezan por `bc1q`. P2WPKH es una salida SegWit de la versión 0.