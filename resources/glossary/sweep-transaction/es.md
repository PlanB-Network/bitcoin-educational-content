---
term: SWEEP TRANSACTION
---

Modelo de patrón o transacción utilizado en el análisis de cadena para determinar la naturaleza de la transacción. Este modelo se caracteriza por la consumición de un único UTXO como entrada y la producción de un único UTXO como salida. La interpretación de este modelo es que estamos ante un auto-transferencia. El usuario ha transferido sus bitcoins a sí mismo, a otra dirección que posee. Dado que no hay cambio en la transacción, es muy poco probable que estemos tratando con un pago. De hecho, cuando se realiza un pago, es casi imposible que el pagador tenga un UTXO que coincida exactamente con el monto requerido por el vendedor, además de las comisiones de la transacción. Generalmente, el pagador por lo tanto se ve obligado a producir una salida de cambio. Entonces sabemos que el usuario observado probablemente aún esté en posesión de este UTXO. En el contexto de un análisis de cadena, si sabemos que el UTXO utilizado como entrada en la transacción pertenece a Alice, podemos asumir que el UTXO en salida también le pertenece.

![](../../dictionnaire/assets/6.png)

> ► *En francés, "sweep transaction" podría traducirse como "transaction de balayage".*