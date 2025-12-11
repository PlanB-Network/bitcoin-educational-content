---
name: Ashigaru - Stonewall
description: Comprender y utilizar las transacciones Stonewall en Ashigaru
---
![cover stonewall](assets/cover.webp)



> *Rompa las suposiciones del análisis de blockchain con la duda matemáticamente demostrable entre el remitente y el destinatario de sus transacciones.*

## ¿Qué es una transacción Stonewall?



Stonewall es una forma específica de transacción Bitcoin diseñada para aumentar la confidencialidad de los usuarios a la hora de gastar imitando una coinjoin entre dos personas, sin serlo realmente. De hecho, esta transacción no es colaborativa. Un usuario puede construirla por su cuenta, utilizando únicamente los UTXOs que posee como entrada. Así, puede crear una transacción Stonewall para cualquier ocasión, sin tener que sincronizarse con otro usuario.



La transacción Stonewall funciona del siguiente modo: como entrada a la transacción, el emisor utiliza 2 UTXO que le pertenecen. Como salida, la transacción produce 4 salidas, 2 de las cuales son exactamente del mismo importe. Las otras 2 serán divisas. De las 2 salidas del mismo importe, sólo una irá al beneficiario.



Así que sólo hay 2 papeles en una transacción Stonewall:




- El emisor, que realiza el pago efectivo ;
- El destinatario, que puede desconocer la naturaleza específica de la transacción y simplemente espera el pago del remitente.



Pongamos un ejemplo para entender esta estructura de transacción. Alice está en la panadería para comprar su baguette, que cuesta `4.000 sats`. Ella quiere pagar en bitcoins, manteniendo algún tipo de confidencialidad sobre su pago. Así que decide crear una transacción Stonewall para el pago.



![image](assets/fr/01.webp)



Analizando esta transacción, podemos ver que el panadero ha recibido efectivamente `4.000 sats` como pago por la baguette. Alice ha utilizado 2 UTXO como entradas: una de `10.000 sats` y otra de `15.000 sats`. Por el lado de la producción, ha recuperado 3 UTXO: uno de `4.000 sats`, uno de `6.000 sats` y uno de `11.000 sats`. Alice tiene, por tanto, un saldo neto de 4.000 sats` en esta transacción, que se corresponde bien con el precio de la baguette.



En este ejemplo, he omitido intencionadamente las comisiones de mining para facilitar la comprensión. En realidad, los costes de transacción corren totalmente a cargo del emisor.



## ¿Cuál es la diferencia entre Stonewall y Stonewall x2?



La transacción Stonewall funciona de forma idéntica a la transacción StonewallX2, salvo que esta última requiere colaboración, a diferencia de la transacción Stonewall clásica, de ahí el nombre "x2". Esto se debe a que la transacción Stonewall se ejecuta sin necesidad de colaboración externa: el emisor puede llevarla a cabo sin ayuda de otra persona. En cambio, para una transacción Stonewall x2, un participante adicional, conocido como "colaborador", se une al proceso. Aporta sus propios bitcoins a la transacción, junto con los del remitente, y se hace cargo de la totalidad del importe al final (modulo los costes de mining).



Volvamos a nuestro ejemplo con Alice en la panadería. Si hubiera querido hacer una transacción Stonewall x2, Alice habría tenido que colaborar con Bob (un tercero) al establecer la transacción. Cada uno de ellos habría aportado un UTXO. Bob habría recibido entonces la totalidad de su aportación. El panadero habría recibido el pago por su baguette del mismo modo que en la transacción Stonewall, mientras que Alice habría recuperado su saldo inicial, menos el coste de la baguette.



![image](assets/fr/02.webp)



Desde el punto de vista de una persona ajena, la transacción habría seguido exactamente igual.



![image](assets/fr/03.webp)



En resumen, las transacciones Stonewall y Stonewall x2 comparten una estructura idéntica. La distinción entre ambas radica en su carácter colaborativo o no colaborativo. La transacción Stonewall se desarrolla individualmente, sin necesidad de colaboración. La transacción Stonewall x2, en cambio, se basa en la cooperación entre dos individuos para ponerla en marcha.



[**-> Más información sobre las transacciones de Stonewall x2**](https://planb.academy/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## ¿Para qué sirve una transacción Stonewall?



La estructura Stonewall añade una enorme cantidad de entropía a la transacción, desdibujando las líneas del análisis de la cadena. Vista desde fuera, una transacción de este tipo puede interpretarse como una pequeña coinjoin entre dos personas. Pero en realidad, como la transacción Stonewall x2, es un pago. Por lo tanto, este método genera incertidumbres en el análisis de la cadena, o incluso conduce a pistas falsas.



Tomemos el ejemplo de Alice en la panadería. La transacción en la blockchain tendría este aspecto:



![image](assets/fr/04.webp)



Un observador externo que se base en la heurística común del análisis en cadena podría concluir erróneamente que "**dos personas han hecho un pequeño coinjoin, con un UTXO cada uno como entrada y dos UTXOs cada uno como salida**".



![image](assets/fr/05.webp)



Esta interpretación es inexacta, porque, como usted sabe, un UTXO fue enviado al panadero, los 2 UTXOs entrantes vinieron de Alices, y ella recuperó 3 salidas de cambio.



![image](assets/fr/01.webp)



Aunque el observador externo consiga identificar al pater de la transacción Stonewall, no dispondrá de toda la información. No podrá determinar cuál de los dos UTXO de los mismos importes corresponde al pago. Además, no podrá determinar si los dos UTXO introducidos son de dos personas diferentes o si pertenecen a una sola persona que los ha fusionado. Este último punto se debe al hecho de que las transacciones Stonewall x2, mencionadas anteriormente, siguen exactamente el mismo patrón que las transacciones Stonewall. Visto desde fuera, y sin información contextual adicional, es imposible distinguir entre una transacción Stonewall y una transacción Stonewall x2. Las primeras no son transacciones en colaboración, mientras que las segundas sí lo son. Esto añade aún más dudas al gasto.



![image](assets/fr/03.webp)



## ¿Cómo hago una transacción Stonewall en Ashigaru?



Originalmente desarrollado por el equipo de Samourai Wallet, las transacciones de Stonewall han sido tomadas por la aplicación Ashigaru, un fork del wallet original creado tras el arresto de los desarrolladores de Samourai. Tendrás que instalar Ashigaru y crear una wallet:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

A diferencia de las transacciones Stowaway o Stonewall x2 (*cahoots*), las transacciones Stonewall no requieren el uso de Paynyms. Pueden ejecutarse directamente, sin preparación previa ni colaboración con otro usuario.



De hecho, realmente no necesitas un tutorial para hacer transacciones Stonewall, ya que Ashigaru las genera automáticamente cada vez que gastas, tan pronto como tu wallet contenga suficientes UTXOs.



Pulse el botón `+` en la parte inferior derecha de la pantalla y seleccione `Enviar`.



![Image](assets/fr/06.webp)



Seleccione la cuenta desde la que desea realizar el gasto.



![Image](assets/fr/07.webp)



A continuación, introduzca los datos de la transacción: la dirección del destinatario y el importe a enviar, y pulse la flecha para confirmar.



![Image](assets/fr/08.webp)



Aquí puede, por supuesto, ajustar las comisiones de transacción por defecto en función de las condiciones del mercado. Sin embargo, el elemento más interesante de esta página es el tipo de transacción. Observará que Ashigaru ha seleccionado automáticamente `STONEWALL`. Haga clic en el botón `PREVIEW` para obtener más información.



![Image](assets/fr/09.webp)



Puede ver que la transacción es efectivamente del tipo Stonewall: comprende 2 entradas del mismo importe, 2 salidas del mismo importe, así como las salidas de intercambio y, en mi caso, una entrada adicional para satisfacer la suma de pago.



![Image](assets/fr/10.webp)



Si no desea realizar una transacción Stonewall, sino que prefiere un pago convencional, haga clic en el icono del lápiz situado en la parte superior derecha de la pantalla y, a continuación, seleccione `Simple` en lugar de `STONEWALL`.



![Image](assets/fr/11.webp)



Cuando hayas comprobado todos los detalles, arrastra la flecha verde de la parte inferior de la pantalla para firmar y liberar la transacción.



![Image](assets/fr/12.webp)



Ahora ya sabes cómo realizar una transacción Stonewall, y lo que es más importante, cómo funciona. Si quieres saber más, echa un vistazo a mi tutorial sobre Ashigaru Terminal, que explica cómo hacer coinjoins a través de Whirlpool.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add