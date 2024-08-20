---
term: BIP143
---

Introduce una nueva forma de hashear la transacción para la verificación de la firma en scripts post-SegWit. El objetivo es minimizar las operaciones redundantes durante la verificación e incluir el valor de los UTXOs en la entrada en la firma. Esto resuelve dos problemas principales con el algoritmo de hash de transacción original:
* El crecimiento cuadrático del hash de datos con el número de firmas;
* La ausencia de incluir el valor de entrada en la firma, lo que representaba un riesgo para las carteras de hardware, especialmente en lo que respecta al conocimiento de las comisiones de transacción incurridas.
Desde la actualización de SegWit, explicada en BIP141, se introduce una nueva forma de transacciones cuyo script no será verificado por nodos antiguos, BIP143 aprovecha esta oportunidad para abordar este problema sin requerir un hard fork. Por lo tanto, BIP143 es parte del soft fork de SegWit.