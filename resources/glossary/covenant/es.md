---
term: PACTO

---
Mecanismo que permite imponer condiciones específicas sobre cómo puede gastarse una determinada moneda, incluso en transacciones futuras. Más allá de las condiciones normalmente permitidas por el lenguaje de script en un UTXO, el pacto impone restricciones adicionales sobre cómo puede gastarse este Bitcoin en transacciones posteriores. Técnicamente, el establecimiento de un pacto se produce cuando la `scriptPubKey` de un UTXO define restricciones sobre la `scriptPubKey` de las salidas de una transacción que gasta dicho UTXO. Al ampliar el alcance del script, los covenants permitirían numerosos desarrollos en Bitcoin como el anclaje bilateral de drivechains, la implementación de vaults, o la mejora de sistemas overlay como Lightning. Las propuestas de pacto se diferencian en función de tres criterios:


- Su ámbito de aplicación;
- Su aplicación;
- Su recursividad.

Hay muchas propuestas que permitirían el uso de pactos sobre Bitcoin. Las más avanzadas en el proceso de implementación son `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO), y `OP_VAULT`. Entre otras propuestas, se encuentran: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT`, etc.

Para entender mejor el concepto de pacto, considere esta analogía: imagine una caja fuerte que contiene 500 euros en billetes pequeños. Si consigue abrir esta caja fuerte con la llave correcta, entonces es libre de utilizar este dinero como desee. Esta es la situación normal con Bitcoin. Ahora, imagine que la misma caja fuerte no contiene 500€ en billetes, sino vales de comida de valor equivalente. Si consigue abrir esta caja fuerte, podrá utilizar esta suma. Sin embargo, su libertad para gastar está restringida, ya que sólo puede utilizar estos vales para pagar en determinados restaurantes. Así, hay una primera condición para gastar este dinero, que es conseguir abrir la caja fuerte con la llave adecuada. Pero también hay una condición adicional en cuanto al uso futuro de esta suma: debe gastarse exclusivamente en restaurantes asociados, y no libremente. Este sistema de restricciones sobre las transacciones futuras es lo que se denomina un pacto.

> ► *En francés, no existe ningún término que recoja con precisión el significado de la palabra "covenant". Se podría hablar de "cláusula", "pacto" o "compromiso", pero no se corresponderían exactamente con el término "covenant". Este término se ha tomado prestado de la terminología jurídica que permite describir una cláusula contractual que impone obligaciones persistentes sobre una propiedad*