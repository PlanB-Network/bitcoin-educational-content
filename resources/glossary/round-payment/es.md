---
term: ROUND PAYMENT
---

Una heurística interna para el análisis de cadenas en Bitcoin que permite formular una hipótesis sobre la naturaleza de los outputs de una transacción basada en cantidades redondas. Generalmente, cuando se enfrenta a un patrón de pago simple (1 input y 2 outputs), si uno de los outputs gasta una cantidad redonda, entonces representa el pago. Por eliminación, si un output representa el pago, el otro representa el cambio. Por lo tanto, se puede interpretar que es probable que el usuario que introduce la transacción todavía posea el output identificado como el cambio.

Cabe señalar que esta heurística no siempre es aplicable, ya que la mayoría de los pagos todavía se realizan en unidades de moneda fiat. De hecho, cuando un comerciante en Francia acepta bitcoin, generalmente, no muestran precios estables en sats. Preferirían optar por una conversión entre el precio en euros y la cantidad en bitcoins a pagar a través de su POS (como BTCPay Server, por ejemplo). Por lo tanto, no debería haber un número redondo en el output de la transacción. Sin embargo, un analista podría intentar hacer esta conversión teniendo en cuenta el tipo de cambio vigente cuando la transacción fue transmitida en la red. Si un día, bitcoin se convierte en la unidad de cuenta preferida en nuestros intercambios, esta heurística podría ser aún más útil para análisis.

![](../../dictionnaire/assets/11.png)