---
term: BIP143

---
Introduce una nueva forma de hashing de la transacción para la verificación de la firma en scripts post-SegWit. El objetivo es minimizar las operaciones redundantes durante la verificación e incluir el valor de los UTXO de la entrada en la firma. Esto resuelve dos problemas importantes con el algoritmo hash de transacción original:


- El crecimiento cuadrático del hashing de datos con el número de firmas;
- La ausencia de inclusión del valor de entrada en la firma, lo que suponía un riesgo para los monederos físicos, especialmente en lo relativo al conocimiento de las comisiones de transacción incurridas.

Dado que la actualización de SegWit, explicada en el BIP141, introduce una nueva forma de transacciones cuya escritura no será verificada por los nodos antiguos, el BIP143 aprovecha esta oportunidad para solucionar este problema sin necesidad de un hard fork. Por lo tanto, el BIP143 forma parte del soft fork de SegWit.