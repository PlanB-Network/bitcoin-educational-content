---
term: PAGO REDONDO

---
Una heurística interna para el análisis de cadenas en Bitcoin que permite formular una hipótesis sobre la naturaleza de las salidas de una transacción basada en importes redondos. Generalmente, ante un patrón de pago simple (1 entrada y 2 salidas), si una de las salidas gasta una cantidad redonda, entonces representa el pago. Por eliminación, si una salida representa el pago, la otra representa el cambio. Por lo tanto, se puede interpretar que es probable que el usuario que introduce la transacción aún posea la salida identificada como el cambio.

Hay que señalar que esta heurística no siempre es aplicable, ya que la mayoría de los pagos se siguen realizando en unidades de moneda fiduciaria. De hecho, cuando un comerciante en Francia acepta bitcoin, por lo general, no muestra precios estables en sats. Prefieren optar por una conversión entre el precio en euros y el importe en bitcoins a pagar a través de su TPV (como el servidor BTCPay, por ejemplo). Por lo tanto, no debería haber un número redondo en la salida de la transacción. No obstante, un analista podría intentar hacer esta conversión teniendo en cuenta el tipo de cambio vigente cuando la transacción se emitió en la red. Si algún día el bitcoin se convierte en la unidad de cuenta preferida en nuestros intercambios, esta heurística podría resultar aún más útil para los análisis.

![](../../dictionnaire/assets/11.webp)