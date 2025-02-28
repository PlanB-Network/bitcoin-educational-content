---
term: STONEWALL

---
Una forma específica de transacción Bitcoin destinada a aumentar la privacidad del usuario durante un gasto imitando un coinjoin entre dos personas, sin serlo realmente. De hecho, esta transacción no es colaborativa. Un usuario puede construirla solo, involucrando sólo sus propios UTXOs como entradas. Por lo tanto, puede crear una transacción Stonewall para cualquier ocasión, sin necesidad de sincronizarse con otro usuario.

El funcionamiento de la transacción Stonewall es el siguiente: a la entrada de la transacción, el emisor utiliza 2 UTXOs que le pertenecen. La transacción produce entonces 4 salidas, 2 de las cuales serán exactamente la misma cantidad. Las otras 2 constituirán el cambio. Entre las 2 salidas del mismo importe, sólo una irá realmente al receptor del pago.

Por lo tanto, sólo hay 2 papeles en una transacción Stonewall:


- El remitente, que realiza el pago efectivo;
- El destinatario, que puede desconocer la naturaleza específica de la transacción y simplemente espera el pago del remitente.

![](../../dictionnaire/assets/33.webp)

Las transacciones Stonewall están disponibles tanto en la aplicación Samourai Wallet como en el software Sparrow Wallet.

La estructura Stonewall añade mucha entropía a la transacción y oscurece el rastro para el análisis de la cadena. Desde fuera, una transacción de este tipo puede interpretarse como una pequeña coinjoin entre dos personas. Pero en realidad, al igual que la transacción Stonewall x2, se trata de un pago. Así pues, este método genera incertidumbres en el análisis de la cadena, o incluso conduce a pistas falsas. Aunque un observador externo consiga identificar el patrón de la transacción Stonewall, no dispondrá de toda la información. No podrá determinar a cuál de los dos UTXO de los mismos importes corresponde el pago. Además, no podrán determinar si los dos UTXO de entrada proceden de dos personas distintas o si pertenecen a una única persona que los fusionó. Esto último se debe a que las transacciones Stonewall x2 siguen exactamente el mismo patrón que las transacciones Stonewall. Desde fuera y sin información contextual adicional, es imposible diferenciar una transacción Stonewall de una transacción Stonewall x2. Sin embargo, las primeras no son transacciones en colaboración, mientras que las segundas sí lo son. Esto añade aún más dudas sobre este gasto.