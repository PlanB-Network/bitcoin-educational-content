---
term: STONEWALL X2

---
Una forma específica de transacción Bitcoin destinada a aumentar la privacidad del usuario durante un gasto, colaborando con un tercero no implicado en el gasto. Este método simula un minijunto de bitcoins entre dos participantes, al tiempo que se realiza un pago a un tercero. Las transacciones Stonewall x2 están disponibles tanto en la aplicación Samourai Wallet como en el software Sparrow Wallet (ambos son interoperables).

Su funcionamiento es relativamente sencillo: utiliza un UTXO en nuestro poder para realizar el pago y solicita la ayuda de un tercero que también contribuye con un UTXO de su propiedad. La transacción finaliza con cuatro salidas: dos de ellas de igual importe, una destinada a la dirección del receptor del pago, la otra a una dirección perteneciente al colaborador. Un tercer UTXO se devuelve a otra dirección del colaborador, lo que le permite recuperar la cantidad inicial (una acción neutra para él, menos las tasas de minería), y un último UTXO vuelve a una dirección de nuestra propiedad, que constituye el cambio del pago. Así, en las transacciones Stonewall x2 se definen tres roles diferentes:


- El remitente, que realiza el pago efectivo;
- El colaborador, que aporta bitcoins para mejorar el anonimato general de la transacción, al tiempo que recupera íntegramente sus fondos al final;
- El destinatario, que puede desconocer la naturaleza específica de la transacción y simplemente espera el pago del remitente.

![](../../dictionnaire/assets/3.webp)

La estructura Stonewall x2 añade mucha entropía a la transacción y enturbia las pistas del análisis de la cadena. Desde fuera, una transacción de este tipo puede interpretarse como una pequeña coinjoin entre dos personas. Pero en realidad, es un pago. Así pues, este método genera incertidumbres en el análisis de la cadena, o incluso conduce a pistas falsas. Aunque un observador externo consiga identificar el patrón de la transacción Stonewall x2, no dispondrá de toda la información. No podrá determinar cuál de los dos UTXO de igual importe corresponde al pago. Además, no podrán saber quién realizó el pago. Por último, no podrán determinar si los dos UTXO de entrada proceden de dos personas diferentes o si pertenecen a una única persona que los fusionó. Este último punto se debe al hecho de que las transacciones Stonewall clásicas siguen exactamente el mismo patrón que las transacciones Stonewall x2. Desde fuera y sin información adicional sobre el contexto, es imposible diferenciar una transacción Stonewall de una transacción Stonewall x2. Sin embargo, las primeras no son transacciones en colaboración, mientras que las segundas sí lo son. Esto añade aún más dudas sobre el gasto.