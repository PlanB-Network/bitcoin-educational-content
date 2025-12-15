---
name: Sparrow Wallet - Stonewall
description: Comprender y utilizar las transacciones Stonewall en Sparrow
---

![cover](assets/cover.webp)




> *Rompa las suposiciones del análisis de blockchain con la duda matemáticamente demostrable entre el remitente y el destinatario de sus transacciones.*

## ¿Qué es una transacción Stonewall?



Stonewall es una forma específica de transacción Bitcoin diseñada para aumentar la confidencialidad de los usuarios a la hora de gastar imitando una coinjoin entre dos personas, sin serlo realmente. De hecho, esta transacción no es colaborativa. Un usuario puede construirla por su cuenta, utilizando únicamente los UTXOs que le pertenecen como entrada. Así, puede crear una transacción Stonewall para cualquier ocasión, sin tener que sincronizarse con otro usuario.



La transacción Stonewall funciona del siguiente modo: como entrada a la transacción, el emisor utiliza 2 UTXO que le pertenecen. Como salida, la transacción produce 4 salidas, 2 de las cuales son exactamente del mismo importe. Las otras 2 serán divisas. De las 2 salidas del mismo importe, sólo una irá al beneficiario.



Así que sólo hay 2 papeles en una transacción Stonewall:




- El emisor, que realiza el pago efectivo ;
- El destinatario, que puede desconocer la naturaleza específica de la transacción y simplemente espera el pago del remitente.



Pongamos un ejemplo para entender esta estructura de transacción. Alice está en la panadería para comprar su baguette, que cuesta `4.000 sats`. Ella quiere pagar en bitcoins, manteniendo algún tipo de confidencialidad sobre su pago. Así que decide crear una transacción Stonewall para el pago.



![image](assets/fr/01.webp)



Analizando esta transacción, podemos ver que el panadero ha recibido efectivamente `4.000 sats` como pago por la baguette. Alice ha utilizado como entradas 2 UTXOs: uno de `10.000 sats` y otro de `15.000 sats`. A la salida, ha recuperado 3 UTXO: uno de `4.000 sats`, otro de `6.000 sats` y otro de `11.000 sats`. Alice tiene, por tanto, un saldo neto de 4.000 sats` en esta transacción, que se corresponde bien con el precio de la baguette.



En este ejemplo, he omitido intencionadamente las comisiones de mining para facilitar la comprensión. En realidad, los costes de transacción corren íntegramente a cargo del emisor.



## ¿Cuál es la diferencia entre Stonewall y Stonewall x2?



La transacción Stonewall funciona de forma idéntica a la transacción StonewallX2, salvo que esta última requiere colaboración, a diferencia de la transacción Stonewall clásica, de ahí el nombre "x2". Esto se debe a que la transacción Stonewall se ejecuta sin necesidad de colaboración externa: el emisor puede llevarla a cabo sin ayuda de otra persona. En cambio, para una transacción Stonewall x2, un participante adicional, conocido como "colaborador", se une al proceso. Él o ella aporta sus propios bitcoins a la transacción, junto con los del remitente, y se hace cargo de la totalidad del importe al final (menos los costes de mining).



Volvamos a nuestro ejemplo con Alice en la panadería. Si hubiera querido hacer una transacción Stonewall x2, Alice habría tenido que colaborar con Bob (un tercero) al establecer la transacción. Cada uno de ellos habría aportado un UTXO. Bob habría recibido entonces el importe íntegro de su aportación a la salida. El panadero habría recibido el pago por su baguette del mismo modo que en la transacción Stonewall, mientras que Alice habría recuperado su saldo inicial, menos el coste de la baguette.



![image](assets/fr/02.webp)



Desde el punto de vista de una persona ajena, la transacción habría seguido exactamente igual.



![image](assets/fr/03.webp)



En resumen, las transacciones Stonewall y Stonewall x2 comparten una estructura idéntica. La distinción entre ambas radica en su carácter colaborativo o no colaborativo. La transacción Stonewall se desarrolla individualmente, sin necesidad de colaboración. La transacción Stonewall x2, en cambio, se basa en la cooperación entre dos individuos para ponerla en marcha.



[**-> Más información sobre las transacciones de Stonewall x2**](https://planb.academy/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## ¿Para qué sirve una transacción Stonewall?



La estructura Stonewall añade una enorme cantidad de entropía a la transacción, desdibujando las líneas del análisis de la cadena. Vista desde fuera, una transacción de este tipo puede interpretarse como una pequeña coinjoin entre dos personas. Pero en realidad, al igual que la transacción Stonewall x2, se trata de un pago. Por lo tanto, este método genera incertidumbres en el análisis de la cadena, o incluso conduce a pistas falsas.



Tomemos el ejemplo de Alice en la panadería. La transacción en la blockchain tendría este aspecto:



![image](assets/fr/04.webp)



Un observador externo que se base en la heurística común de análisis de cadenas podría concluir erróneamente que "*dos personas han hecho un pequeño coinjoin, con un UTXO cada uno como entrada y dos UTXOs cada uno como salida*".



![image](assets/fr/05.webp)



Esta interpretación es inexacta, porque, como usted sabe, un UTXO fue enviado al panadero, los 2 UTXOs entrantes vinieron de Alices, y ella recuperó 3 salidas de intercambio.



![image](assets/fr/01.webp)



Aunque el observador externo consiga identificar al pater de la transacción Stonewall, no dispondrá de toda la información. No podrá determinar cuál de los dos UTXO de los mismos importes corresponde al pago. Además, no podrá determinar si las dos entradas UTXO proceden de dos personas diferentes o si pertenecen a una única persona que las ha fusionado. Esto último se debe a que las transacciones Stonewall x2, mencionadas anteriormente, siguen exactamente el mismo patrón que las transacciones Stonewall. Visto desde fuera y sin información contextual adicional, es imposible distinguir entre una transacción Stonewall y una transacción Stonewall x2. Las primeras no son transacciones en colaboración, mientras que las segundas sí lo son. Esto añade aún más dudas al gasto.



![image](assets/fr/03.webp)



## ¿Cómo hago una transacción Stonewall en Sparrow?



Originalmente desarrollado por el equipo de Samurai Wallet, las transacciones Stonewall fueron tomadas por la aplicación Ashigaru, un fork de la cartera original creada tras la detención de los desarrolladores de Samurai, y también en Sparrow Wallet.



Tendrás que instalar Sparrow y crear un archivo :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

A diferencia de las transacciones Stowaway o Stonewall x2 (*cahoots*), las transacciones Stonewall no requieren el uso de Paynyms. Pueden realizarse directamente, sin ninguna preparación especial ni colaboración con otro usuario.



Para realizar una transacción Stonewall en Sparrow, el procedimiento es muy sencillo: comience creando una transacción como de costumbre, ya sea a través del menú `Enviar`, o desde el menú `UTXOs` si desea hacer *Coin Control*.



![Image](assets/fr/06.webp)



A continuación, introduzca los datos de la transacción: la dirección del destinatario, una etiqueta, el importe a enviar y la cuantía o tarifa de los gastos, según las condiciones del mercado.



![Image](assets/fr/07.webp)



Antes de confirmar, aquí es donde puede seleccionar la estructura Stonewall. En la parte inferior de la interfaz, sustituya "Eficiencia" por "Privacidad". Si esta opción no aparece, significa que su cartera no tiene un número suficiente de UTXOs para construir este tipo de operación.



![Image](assets/fr/08.webp)



Tras seleccionar la opción `Privacidad`, observará que la estructura de la transacción se modifica por completo: se convierte en una transacción Stonewall, consumiendo varios de sus UTXOs como entradas y produciendo dos salidas de idénticas cantidades, una de las cuales corresponde al pago real de `100.000 sats`, además de las salidas de intercambio.



![Image](assets/fr/09.webp)



Si todo es correcto, haga clic en `Crear transacción`.



A continuación, puede comprobar los detalles de la transacción por última vez y hacer clic en "Finalizar transacción para firmar".



![Image](assets/fr/10.webp)



A continuación, firme la transacción según el método específico de su cartera y haga clic en `Broadcast Transaction` para difundirla en la red Bitcoin, a la espera de confirmación.



![Image](assets/fr/11.webp)



Ahora ya sabes cómo funciona una transacción Stonewall en Sparrow Wallet y cómo crear una. Para profundizar en el dominio de estas herramientas diseñadas para reforzar tu confidencialidad onchain, te invito a seguir mi formación BTC 204 en Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c