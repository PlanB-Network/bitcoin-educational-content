---
term: P2SH-P2WSH
---

P2SH-P2WSH significa *Pay to Script Hash - Pay to Witness Script Hash*. Es un modelo de script estándar utilizado para establecer condiciones de gasto en un UTXO, también conocido como "Nested SegWit".

P2SH-P2WSH fue introducido con la implementación de SegWit en agosto de 2017. Este script describe un P2WSH envuelto dentro de un P2SH. Bloquea bitcoins basados en el hash de un script. La diferencia de un P2WSH clásico es que el script está envuelto en el `redeemScript` de un P2SH clásico.

Este script fue creado en el lanzamiento de SegWit para facilitar su adopción. Permite el uso de este nuevo estándar, incluso con servicios o carteras que aún no son compatibles de manera nativa con SegWit. Hoy en día, por lo tanto, ya no es muy relevante usar estos tipos de scripts SegWit envueltos, ya que la mayoría de las carteras han implementado SegWit de forma nativa. Las direcciones P2SH-P2WSH se escriben usando la codificación `Base58Check` y siempre comienzan con `3`, como cualquier dirección P2SH.