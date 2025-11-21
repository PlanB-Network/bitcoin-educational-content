---
term: CISA
---

Acrónimo de "Cross-Input Signature Aggregation". Se trata de una propuesta técnica diseñada para optimizar el tamaño de las transacciones Bitcoin reduciendo el número de firmas necesarias para validarlas.


Actualmente, en Bitcoin, cada entrada de una transacción debe tener una firma individual antes de poder ser consumida. Esto prueba que el propietario de la UTXO en cuestión ha autorizado la transacción. Con CISA, el objetivo es combinar las firmas de todas las entradas de una misma transacción en una sola firma que abarque todas las entradas. Esto permitiría reducir el tamaño de las transacciones con muchas entradas y, por tanto, también sus costes. Esto sería especialmente útil para quienes realizan coinjoins o consolidaciones, al tiempo que permitiría confirmar más transacciones en Bitcoin sin alterar el tamaño de los bloques ni los intervalos. CISA se basa en el protocolo Schnorr, que permite la agregación lineal de firmas. Esto significa que una sola firma puede demostrar la posesión de varias claves independientes.


Sin embargo, implantar CISA en Bitcoin es muy complejo, ya que requiere cambios profundos en el funcionamiento de los scripts. Actualmente, la verificación de scripts en Bitcoin se hace entrada por entrada. Pasar a un modelo en el que toda una transacción se comprueba a la vez, como propone CISA, no es ni mucho menos un cambio trivial.