---
term: P2SH-P2WPKH

---
P2SH-P2WPKH son las siglas de *Pay to Script Hash - Pay to Witness Public Key Hash*. Es un modelo de script estándar utilizado para establecer condiciones de gasto en un UTXO, también conocido como "Nested SegWit".

P2SH-P2WPKH se introdujo con la implementación de SegWit en agosto de 2017. Este script es un P2WPKH envuelto dentro de un P2SH. Bloquea bitcoins basándose en el hash de una clave pública. La diferencia con el P2WPKH clásico es que el script está envuelto en el `redeemScript` de un P2SH clásico.

Este script fue creado en el lanzamiento de SegWit para facilitar su adopción. Permite el uso de este nuevo estándar, incluso con servicios o monederos que aún no son compatibles de forma nativa con SegWit. Es una especie de script de transición hacia el nuevo estándar. Hoy en día, por lo tanto, ya no es muy relevante utilizar este tipo de scripts SegWit envueltos, ya que la mayoría de los monederos han implementado SegWit nativo. Las direcciones P2SH-P2WPKH se escriben utilizando la codificación `Base58Check` y siempre empiezan por `3`, como cualquier dirección P2SH.

> ► *`P2SH-P2WPKH` también se denomina a veces `P2WPKH-nested-in-P2SH`.*