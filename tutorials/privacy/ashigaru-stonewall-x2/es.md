---
name: Ashigaru - Stonewall x2
description: Comprender y utilizar las transacciones Stonewall x2 en Ashigaru
---
![cover stonewall x2](assets/cover.webp)



> *Hacer de cada gasto una coinjoin

## ¿Qué es una transacción Stonewall x2?



Stonewall x2 es una forma específica de transacción Bitcoin diseñada para aumentar la confidencialidad del usuario a la hora de gastar, colaborando con un tercero no implicado en el gasto. Este método simula un mini-coinjoin entre dos participantes, mientras se realiza un pago a un tercero. Las transacciones Stonewall x2 están disponibles en la aplicación Ashigaru, una fork de Samourai Wallet (el equipo detrás de la creación de este tipo de transacción).



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Su funcionamiento es relativamente sencillo: usted utiliza una UTXO que tiene en su poder para efectuar el pago, y consigue la ayuda de un tercero que también contribuye con una UTXO propia. La transacción termina con cuatro salidas: dos de ellas en cantidades iguales, una destinada a la dirección del beneficiario, la otra a una dirección perteneciente al colaborador. Una tercera UTXO se devuelve a otra dirección perteneciente al colaborador, lo que le permite recuperar la cantidad inicial (una acción neutra para él, modulada por los costes de la mining), y una última UTXO vuelve a una dirección perteneciente a nosotros, lo que constituye el intercambio de pagos.



Así pues, en las transacciones Stonewall x2 se definen tres papeles diferentes:




- El emisor, que realiza el pago efectivo ;
- El colaborador, que pone a disposición bitcoins para mejorar el anonimato de la transacción, al tiempo que recupera íntegramente sus fondos al final (una acción neutra para él, módulo los costes mining);
- El destinatario, que puede desconocer la naturaleza específica de la transacción y simplemente espera el pago del remitente.



Pongamos un ejemplo. Alice está en la panadería para comprar su baguette, que cuesta `4.000 sats`. Quiere pagar en bitcoins, manteniendo cierta confidencialidad sobre su pago. Así que llama a su amigo Bob, que le ayudará con esto.



![image](assets/fr/01.webp)



Analizando esta transacción, podemos ver que el panadero recibió realmente 4.000 sats` como pago por la baguette. Alice utilizó 10.000 sats` en insumos y recuperó 6.000 sats` en productos, lo que arroja un saldo neto de 4.000 sats`, que corresponde al precio de la baguette. Bob, por su parte, ha suministrado 15.000 sats` en entradas y ha recibido dos salidas: una de 4.000 sats` y otra de 11.000 sats`, lo que arroja un saldo de 0`.



En este ejemplo, he omitido intencionadamente las comisiones de mining para facilitar la comprensión. En realidad, las comisiones de transacción se reparten a partes iguales entre el emisor del pago y el colaborador.



## ¿Cuál es la diferencia entre Stonewall y Stonewall x2?



Una transacción StonewallX2 funciona exactamente igual que una transacción Stonewall, salvo que la primera es colaborativa, mientras que la segunda no lo es. Como hemos visto, una transacción Stonewall x2 implica la participación de un tercero, externo al pago, que pondrá a disposición sus bitcoins para aumentar la confidencialidad de la transacción. En una transacción Stonewall clásica, el papel de colaborador lo asume el remitente.



Volvamos al ejemplo de Alice en la panadería. Si no hubiera podido encontrar a alguien como Bob que la acompañara en su juerga de gastos, podría haber hecho un Stonewall ella sola. De ese modo, los dos UTXO de la entrada habrían sido suyos y habría conseguido 3 a la salida.



![image](assets/fr/02.webp)




Desde el punto de vista de una persona ajena, la transacción habría seguido siendo la misma.



![image](assets/fr/05.webp)



Por lo tanto, la lógica debería ser la siguiente cuando se desea utilizar una herramienta de gasto Ashigaru:




- Si el comerciante no es compatible con Payjoin Stowaway, puede realizar una transacción colaborativa con otra persona ajena al pago gracias a Stonewall x2 ;
- Si no encuentras a nadie que haga una transacción Stonewall x2, puedes hacer una transacción sólo Stonewall, que imitará el comportamiento de una transacción Stonewall x2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4

## ¿Para qué sirve una transacción Stonewall x2?



La estructura Stonewall x2 añade una enorme cantidad de entropía a la transacción, confundiendo el análisis de la cadena. Vista desde fuera, una transacción de este tipo podría interpretarse como un pequeño Coinjoin entre dos personas. Pero en realidad, es un pago. Por lo tanto, este método crea incertidumbres en el análisis de la cadena, o incluso conduce a pistas falsas.



Tomemos el ejemplo de Alice, Bob y el Boulanger. La transacción en la blockchain tendría este aspecto:



![image](assets/fr/03.webp)



Un observador externo que se base en la heurística común de análisis de cadenas podría concluir erróneamente que "*Alice y Bob han hecho un pequeño coinjoin, con un UTXO cada uno entrando y dos UTXOs cada uno saliendo*".



![image](assets/fr/04.webp)



Esta interpretación es incorrecta porque, como usted sabe, se envió una UTXO al Boulanger, la Alice sólo tiene una salida de cambio y la Bob tiene dos.



![image](assets/fr/01.webp)



Aunque el observador externo consiga identificar al pater de la transacción Stonewall x2, no dispondrá de toda la información. No podrá determinar a cuál de los dos UTXO de los mismos importes corresponde el pago. Tampoco podrá determinar si fue Alice o Bob quien efectuó el pago. Por último, no podrá determinar si los dos UTXO introducidos son de dos personas diferentes o si pertenecen a una única persona que los ha fusionado. Este último punto se debe al hecho de que las transacciones Stonewall clásicas, comentadas anteriormente, siguen exactamente la misma paternidad que las transacciones Stonewall x2. Vistas desde fuera y sin información contextual adicional, es imposible diferenciar una transacción Stonewall de una transacción Stonewall x2. Las primeras no son transacciones en colaboración, mientras que las segundas sí lo son. Esto añade aún más dudas al gasto.



![image](assets/fr/05.webp)




## ¿Cómo puedo establecer una conexión entre Paynyms?



Como en otras transacciones colaborativas en Ashigaru (*Cahoots*), Stonewall x2 implica el intercambio de transacciones parcialmente firmadas entre el emisor y el colaborador. Este intercambio puede realizarse manualmente, si estás físicamente presente con tu colaborador, o automáticamente utilizando el protocolo de comunicación Soroban.



Si eliges la segunda opción, tendrás que establecer una conexión entre Paynyms antes de poder realizar un Stonewall x2. Para ello, tu Paynym debe "*seguir*" al Paynym de tu colaborador, y viceversa. Para saber cómo hacerlo, puedes seguir el principio de este otro tutorial:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## ¿Cómo hago una transacción Stonewall x2 en Ashigaru?



Para realizar una transacción Stonewall x2, haz clic en la imagen de tu Paynym en la esquina superior izquierda de la pantalla y, a continuación, abre el menú `Colaborar`. La persona que participe en la transacción contigo debe hacer lo mismo, a menos que intercambiéis códigos QR en persona.



![Image](assets/fr/06.webp)



Tiene dos opciones: seleccionar `Iniciar` si es el remitente del pago, o `Participar` si es la persona que colabora en la transacción pero no es ni el pagador ni el destinatario real.



![Image](assets/fr/07.webp)



Si tiene el rol de colaborador, el procedimiento es muy sencillo. Para la colaboración a distancia a través de la red Soroban, haga clic en `Participar`, elija la cuenta que desea utilizar y, a continuación, pulse `ESPERAR SOLICITUDES DE COBRO` para esperar la solicitud enviada por el pagador.



![Image](assets/fr/08.webp)



Por otro lado, para la colaboración en persona mediante el escaneado de códigos QR, vaya a la página de inicio de su wallet, pulse el icono de código QR en la parte superior de la pantalla y, a continuación, escanee el código QR facilitado por el ordenante que inicia la transacción.



![Image](assets/fr/09.webp)



Si usted es el pagador, es decir, el que inicia la transacción, vaya al menú "Colaborar" y seleccione "Iniciar".



![Image](assets/fr/10.webp)



Para el tipo de transacción, dado que deseamos realizar una Stonewall x2, elija esta opción.



![Image](assets/fr/11.webp)



A continuación, puedes elegir entre la colaboración en línea (*Cahoots* a través de *Soroban*) o la colaboración cara a cara, con intercambios de códigos QR.



![Image](assets/fr/12.webp)



### Cahoots en línea



Si ha elegido la opción `Online`, seleccione su colaborador entre los Paynyms que sigue.



![Image](assets/fr/13.webp)



Haga clic en "Establecer transacción" y, a continuación, seleccione la cuenta desde la que desea realizar el gasto.



![Image](assets/fr/14.webp)



En la página siguiente, introduzca los detalles de la transacción: la dirección del destinatario real del pago, el importe a enviar y la tarifa de gastos. A continuación, haga clic en `Revisar la configuración de la transacción`.



![Image](assets/fr/15.webp)



Compruebe cuidadosamente la información, asegúrese de que su colaborador está escuchando las solicitudes de *Cahoots* y, a continuación, haga clic en el botón verde `BEGIN TRANSACTION` para iniciar el intercambio de PSBTs a través de Soroban.



![Image](assets/fr/16.webp)



Espere a que ambos participantes hayan firmado la transacción y, a continuación, difúndala en la red Bitcoin.



![Image](assets/fr/17.webp)



### Debates cara a cara



Si desea realizar el canje en persona, seleccione el tipo de operación `STONEWALL X2` y, a continuación, elija la opción `En persona / Manual`.



![Image](assets/fr/18.webp)



Haga clic en "Establecer transacción" y, a continuación, seleccione la cuenta desde la que desea realizar el gasto.



![Image](assets/fr/19.webp)



En la página siguiente, introduzca los detalles de la transacción: la dirección del destinatario real del pago, el importe a enviar y la tarifa de gastos. A continuación, haga clic en `Revisar la configuración de la transacción`.



![Image](assets/fr/20.webp)



Compruebe los datos y pulse el botón verde "INICIAR TRANSACCIÓN" para empezar a intercambiar PSBT mediante el escaneado del código QR.



![Image](assets/fr/21.webp)



El intercambio se realiza alternando el escaneo con el colaborador: haz clic en "MOSTRAR CÓDIGO QR" para mostrar tu código QR a tu colaborador, que lo escaneará. A continuación, él hará clic en "MOSTRAR CÓDIGO QR" para mostrar el suyo, y tú lo escanearás con "LANZAR ESCÁNER QR". Repita este proceso hasta completar los cinco pasos de intercambio.



![Image](assets/fr/22.webp)



Una vez completados todos los intercambios, compruebe los detalles de la transacción y, a continuación, libérela arrastrando la flecha verde situada en la parte inferior de la pantalla.



![Image](assets/fr/23.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/9082f3d989728aacd290535a1ac374ab8c04a241a1d798b378db626dabea7a24). Su estructura es la siguiente:



![Image](assets/fr/24.webp)



*Crédito: [mempool.space](https://mempool.space/)*



Podemos observar dos entradas de mi cartera, respectivamente `91.869 sats` y `64.823 sats`, mientras que las otras dos entradas proceden de la wallet de mi colaborador. Por el lado de la salida, una UTXO de `100.000 sats` se envía al beneficiario real, y dos UTXOs de `100.000 sats` y `159.578 sats` vuelven a la cartera de mi colaborador. Para él, la operación es neutra, ya que recupera la totalidad de los fondos que había invertido en entrada (excluidos los gastos mining a los que contribuyó). Por último, yo recibo a cambio una UTXO de `56.270 sats`, correspondiente a la diferencia entre el total de mis aportaciones y el pago de `100.000 sats` enviado al beneficiario.



Obviamente, puedo describir esta estructura porque yo mismo he construido la transacción. Pero para un observador externo, generalmente es imposible determinar qué UTXOs pertenecen a cada participante, ya sea en las entradas o en las salidas.



Para profundizar en la gestión de la privacidad onchain en Bitcoin, te recomiendo que tomes mi formación BTC 204 en Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c