---
term: OPERACIÓN DE BARRIDO

---
Modelo de patrón o transacción utilizado en el análisis de la cadena para determinar la naturaleza de la transacción. Este modelo se caracteriza por el consumo de un único UTXO como entrada y la producción de un único UTXO como salida. La interpretación de este modelo es que estamos en presencia de una autotransferencia. El usuario se ha transferido sus bitcoins a sí mismo, a otra dirección de su propiedad. Dado que no hay ningún cambio en la transacción, es muy poco probable que estemos ante un pago. De hecho, cuando se realiza un pago, es casi imposible que el pagador tenga un UTXO que coincida exactamente con la cantidad requerida por el vendedor, además de las tasas de transacción. Generalmente, el pagador se ve por tanto obligado a producir una salida de cambio. Entonces sabemos que es probable que el usuario observado siga en posesión de este UTXO. En el contexto de un análisis en cadena, si sabemos que el UTXO utilizado como input en la transacción pertenece a Alice, podemos suponer que el UTXO en output también le pertenece.

![](../../dictionnaire/assets/6.webp)

> ► *En francés, "sweep transaction" podría traducirse como "transaction de balayage".*