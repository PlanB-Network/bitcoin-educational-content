---
term: P2SH-P2WPKH
---

P2SH-P2WPKH significa *Pay to Script Hash - Pay to Witness Public Key Hash*. Es un modelo de script estándar utilizado para establecer condiciones de gasto en un UTXO, también conocido como "Nested SegWit".

P2SH-P2WPKH fue introducido con la implementación de SegWit en agosto de 2017. Este script es un P2WPKH envuelto dentro de un P2SH. Bloquea bitcoins basados en el hash de una clave pública. La diferencia del clásico P2WPKH es que el script está envuelto en el `redeemScript` de un P2SH clásico.

Este script fue creado en el lanzamiento de SegWit para facilitar su adopción. Permite el uso de este nuevo estándar, incluso con servicios o carteras que aún no son compatibles de forma nativa con SegWit. Es una especie de script de transición hacia el nuevo estándar. Hoy en día, por lo tanto, ya no es muy relevante usar estos tipos de scripts SegWit envueltos, ya que la mayoría de las carteras han implementado SegWit nativo. Las direcciones P2SH-P2WPKH se escriben usando la codificación `Base58Check` y siempre comienzan con `3`, como cualquier dirección P2SH.

> ► *`P2SH-P2WPKH` también se llama a veces `P2WPKH-anidado-en-P2SH`.*