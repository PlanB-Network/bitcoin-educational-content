---
term: STONEWALL
---

Una forma específica de transacción de Bitcoin destinada a aumentar la privacidad del usuario durante un gasto al imitar un coinjoin entre dos personas, sin ser realmente uno. De hecho, esta transacción no es colaborativa. Un usuario puede construirla solo, involucrando únicamente sus propios UTXOs como entradas. Por lo tanto, puedes crear una transacción Stonewall para cualquier ocasión, sin necesidad de sincronizarte con otro usuario.

El funcionamiento de la transacción Stonewall es el siguiente: en la entrada de la transacción, el remitente utiliza 2 UTXOs que le pertenecen. La transacción luego produce 4 salidas, 2 de las cuales serán exactamente del mismo monto. Las otras 2 constituirán el cambio. Entre las 2 salidas del mismo monto, solo una irá realmente al destinatario del pago.

Así, solo hay 2 roles en una transacción Stonewall:
* El remitente, quien realiza el pago real;
* El destinatario, quien puede desconocer la naturaleza específica de la transacción y simplemente espera un pago del remitente.

![](../../dictionnaire/assets/33.png)
Las transacciones Stonewall están disponibles tanto en la aplicación Samourai Wallet como en el software Sparrow Wallet.

La estructura de Stonewall añade mucha entropía a la transacción y oscurece el rastro para el análisis de cadena. Desde el exterior, tal transacción puede interpretarse como un pequeño coinjoin entre dos personas. Pero en realidad, al igual que la transacción Stonewall x2, es un pago. Este método genera incertidumbres en el análisis de cadena, o incluso lleva a pistas falsas. Incluso si un observador externo logra identificar el patrón de la transacción Stonewall, no tendrá toda la información. No podrán determinar cuál de los dos UTXOs de los mismos montos corresponde al pago. Además, no podrán determinar si los dos UTXOs en la entrada provienen de dos personas diferentes o si pertenecen a una sola persona que los fusionó. Este último punto se debe a que las transacciones Stonewall x2 siguen exactamente el mismo patrón que las transacciones Stonewall. Desde el exterior y sin información de contexto adicional, es imposible diferenciar una transacción Stonewall de una transacción Stonewall x2. Sin embargo, las primeras no son transacciones colaborativas, mientras que las segundas sí lo son. Esto añade aún más duda sobre este gasto.