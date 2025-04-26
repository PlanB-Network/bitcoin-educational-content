---
term: P2SH-P2WSH

---
P2SH-P2WSH son las siglas de *Pay to Script Hash - Pay to Witness Script Hash*. Se trata de un modelo de script estándar utilizado para establecer condiciones de gasto en un UTXO, también conocido como "Nested SegWit".

P2SH-P2WSH se introdujo con la implementación de SegWit en agosto de 2017. Este script describe un P2WSH envuelto dentro de un P2SH. Bloquea bitcoins basándose en el hash de un script. La diferencia con un P2WSH clásico es que el script está envuelto en el `redeemScript` de un P2SH clásico.

Este script fue creado en el lanzamiento de SegWit para facilitar su adopción. Permite el uso de este nuevo estándar, incluso con servicios o monederos que aún no son compatibles de forma nativa con SegWit. Hoy en día, por lo tanto, ya no es muy relevante utilizar este tipo de scripts SegWit envueltos, ya que la mayoría de los monederos han implementado SegWit nativo. Las direcciones P2SH-P2WSH se escriben utilizando la codificación `Base58Check` y siempre empiezan por `3`, como cualquier dirección P2SH.