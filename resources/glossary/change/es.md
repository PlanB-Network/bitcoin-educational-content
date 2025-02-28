---
term: CAMBIAR

---
En el contexto de las transacciones Bitcoin, se refiere al UTXO creado con los fondos restantes después de que el pago real haya sido satisfecho. Cuando se utilizan UTXOs con una cantidad de bitcoins superior a la necesaria para el pago real y las tasas de transacción, el excedente es un UTXO devuelto a una dirección interna del monedero, denominada dirección de cambio. El cambio representa este UTXO. Por ejemplo, si quieres pagar una baguette que cuesta `4.000 sats` con un UTXO de `10.000 sats`, crearás un cambio de `6.000 sats` en tu transacción (si no tenemos en cuenta las tasas de transacción).

![](../../dictionnaire/assets/16.webp)

> ► *Aunque se usa poco, también podríamos referirnos a ella como "moneda" (cambio dado) para hablar del cambio.*