---
term: CHANGE
---

En el contexto de las transacciones de Bitcoin, se refiere al UTXO creado con los fondos restantes después de que el pago real ha sido satisfecho. Al usar UTXOs con una cantidad de bitcoins mayor que la cantidad necesaria para el pago real y las comisiones de la transacción, el excedente es un UTXO devuelto a una dirección interna de la billetera, llamada la dirección de cambio. El cambio representa este UTXO. Por ejemplo, si quieres pagar por una baguette que cuesta `4,000 sats` con un UTXO de `10,000 sats`, crearás un cambio de `6,000 sats` en tu transacción (si no tenemos en cuenta las comisiones de la transacción).

![](../../dictionnaire/assets/16.png)

> ► *Aunque raramente se usa, también podríamos referirnos a él como "moneda" (cambio dado) para hablar sobre el cambio.*