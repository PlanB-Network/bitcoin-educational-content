---
term: SIMPLE PAYMENT
---

Patrón de transacción (o modelo) utilizado en análisis de cadena caracterizado por el consumo de uno o más UTXOs en las entradas y la producción de 2 UTXOs en las salidas. Por lo tanto, este modelo se verá así:

![](../../dictionnaire/assets/5.png)

Este modelo de pago simple indica que probablemente estamos en presencia de una transacción de envío o pago. El usuario ha consumido su propio UTXO en las entradas para satisfacer en las salidas un UTXO de pago y un UTXO de cambio (cambio devuelto al mismo usuario). Por lo tanto, sabemos que el usuario observado probablemente ya no está en posesión de uno de los dos UTXOs en las salidas (el de pago), pero todavía está en posesión del otro UTXO (el de cambio).