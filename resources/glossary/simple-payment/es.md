---
term: PAGO SIMPLE

---
Patrón (o modelo) de transacción utilizado en el análisis de la cadena caracterizado por el consumo de uno o más UTXOs en las entradas y la producción de 2 UTXOs en las salidas. Por lo tanto, este modelo tendrá el siguiente aspecto

![](../../dictionnaire/assets/5.webp)

Este sencillo modelo de pago indica que probablemente estamos en presencia de una transacción de envío o pago. El usuario ha consumido su propio UTXO en entradas para satisfacer en salidas un UTXO de pago y un UTXO de cambio (cambio devuelto al mismo usuario). Por lo tanto, sabemos que es probable que el usuario observado ya no esté en posesión de uno de los dos UTXOs en salidas (el de pago), pero sigue en posesión del otro UTXO (el de cambio).