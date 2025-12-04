---
name: Ashigaru - Polizón
description: ¿Cómo realizo una transacción Payjoin en Ashigaru?
---
![cover](assets/cover.webp)



> *Obliga a los espías de blockchain a replantearse todo lo que creen saber

Payjoin es una estructura de transacción Bitcoin diseñada para mejorar la confidencialidad del usuario mediante la colaboración directa con el receptor del pago. Existen varias implementaciones para facilitar su aplicación y automatizar el proceso. La más conocida es sin duda Stowaway, desarrollada inicialmente por el equipo Samurai Wallet y ahora integrada en su fork Ashigaru.



## ¿Cómo funciona el Polizón?



Como se mencionó anteriormente, Ashigaru integra una herramienta PayJoin llamada `Stowaway`. Está disponible en la aplicación Ashigaru para Android. Para que un Payjoin se lleve a cabo, el destinatario (que también asume el papel de colaborador) debe estar utilizando un software compatible con Stowaway, es decir, sólo Ashigaru por el momento.



Stowaway se basa en una categoría de transacciones que Samurai denomina "Cahoots". Un Cahoot es una transacción colaborativa entre varios usuarios, que implica un intercambio de información fuera de la blockchain Bitcoin. Ashigaru ofrece actualmente dos herramientas de Cahoots: Stowaway (Payjoins) y StonewallX2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

Las transacciones Cahoots requieren el intercambio de transacciones parcialmente firmadas entre usuarios. Este proceso puede ser largo y tedioso, especialmente cuando se realiza a distancia. Sin embargo, aún es posible hacerlo manualmente, si los colaboradores se encuentran en el mismo lugar. En concreto, se trata de escanear sucesivamente cinco códigos QR intercambiados entre los dos participantes.



A distancia, este método se vuelve demasiado complejo. Para remediarlo, Samourai ha desarrollado un protocolo de comunicación encriptado basado en Tor llamado "*Soroban*". Gracias a Soroban, los intercambios necesarios para un Payjoin se automatizan y tienen lugar en segundo plano.



Estas comunicaciones cifradas requieren una conexión y una autentificación entre los participantes en Cahoot. Por eso Soroban se basa en los Paynyms de los usuarios. Si aún no estás familiarizado con el funcionamiento de Paynyms, echa un vistazo a este tutorial dedicado para aprender más:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

En pocas palabras, un Paynym es un identificador único asociado a su wallet, que le permite activar diversas funciones, incluidos los intercambios cifrados. Adopta la forma de un identificador acompañado de una ilustración. He aquí, por ejemplo, el que utilizo en la Testnet:



![Image](assets/fr/01.webp)



**En resumen:**





- payjoin" = Estructura de transacción colaborativa específica;





- `Stowaway` = Implementación de Payjoin disponible en Ashigaru ;





- `Cahoots` = Nombre dado por Samourai a todos sus tipos de transacciones colaborativas, en particular el Payjoin `Stowaway`, asumido hoy en Ashigaru ;





- soroban = Protocolo de comunicación encriptado establecido en Tor que permite la colaboración con otros usuarios en una transacción `Cahoots`;





- paynym" = Identificador único wallet utilizado para establecer comunicación con otro usuario en "Soroban", con el fin de realizar una transacción "Chahoots".



Para conocer más a fondo cómo funcionan los Payjoins y su utilidad en la privacidad onchain, recomiendo este otro tutorial:



https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## ¿Cómo puedo establecer una conexión entre Paynyms?



Para empezar, necesitará instalar Ashigaru y crear un archivo :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Para llevar a cabo una transacción remota de Cahoots, incluyendo un PayJoin (*Stowaway*) a través de Ashigaru, primero debes "seguir" al usuario con el que deseas colaborar, utilizando su Paynym. En el caso de un Stowaway, esto significa seguir a la persona a la que deseas enviar bitcoins. Si aún no sabes cómo seguir a otro Paynym, encontrarás el procedimiento detallado en este tutorial :



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## ¿Cómo hago un Payjoin en Ashigaru?



Para realizar una transacción de Stowaway, haga clic en la imagen de su Paynym en la esquina superior izquierda de la pantalla y abra el menú `Colaborar`. La persona que participa en la transacción con usted debe hacer lo mismo, a menos que intercambien códigos QR en persona.



![Image](assets/fr/02.webp)



Tiene dos opciones: seleccionar "Iniciar" si es el remitente del pago, o "Participar" si es el beneficiario de este pago conjunto.



![Image](assets/fr/03.webp)



Si usted es el destinatario, el procedimiento es muy sencillo. Para colaborar a distancia a través de la red Soroban, haga clic en `Participar`, elija la cuenta que desea utilizar y, a continuación, pulse `ESPERAR SOLICITUDES DE COBRO` para esperar la solicitud enviada por el pagador.



![Image](assets/fr/04.webp)



Por otra parte, para la colaboración en persona mediante el escaneado de códigos QR, vaya a la página de inicio de su wallet, pulse el icono de código QR en la parte superior de la pantalla y, a continuación, escanee el código QR facilitado por el ordenante que inicia la transacción.



![Image](assets/fr/05.webp)



Si usted es el pagador, es decir, el que inicia la transacción, vaya al menú "Colaborar" y seleccione "Iniciar".



![Image](assets/fr/06.webp)



Para el tipo de transacción, dado que deseamos realizar un Stowaway Payjoin, elija esta opción.



![Image](assets/fr/07.webp)



A continuación, puedes elegir entre la colaboración en línea (*Cahoots* a través de *Soroban*) o la colaboración cara a cara, con intercambios de códigos QR.



![Image](assets/fr/08.webp)



### Cahoots en línea



Si ha elegido la opción `Online`, seleccione el destinatario de los Paynyms que está siguiendo.



![Image](assets/fr/09.webp)



Haga clic en "Establecer transacción" y, a continuación, seleccione la cuenta desde la que desea realizar el gasto.



![Image](assets/fr/10.webp)



En la página siguiente, introduzca los detalles de la transacción: el importe que se enviará al destinatario y la tarifa de cobro. No es necesario introducir una dirección de recepción, ya que el destinatario la transmitirá él mismo durante los intercambios PSBT.



A continuación, haga clic en `Revisar la configuración de la transacción`.



![Image](assets/fr/11.webp)



Compruebe cuidadosamente la información, asegúrese de que su colaborador está escuchando las solicitudes de *Cahoots* y, a continuación, haga clic en el botón verde `BEGIN TRANSACTION` para iniciar el intercambio de PSBTs a través de Soroban.



![Image](assets/fr/12.webp)



Espere a que ambos participantes hayan firmado la transacción y, a continuación, difúndala en la red Bitcoin.



![Image](assets/fr/13.webp)



### Debates cara a cara



Si desea realizar el canje en persona, seleccione el tipo de transacción `STONEWALL X2` y, a continuación, elija la opción `En persona / Manual`.



![Image](assets/fr/14.webp)



Haga clic en "Establecer transacción" y, a continuación, seleccione la cuenta desde la que desea realizar el gasto.



![Image](assets/fr/15.webp)



En la página siguiente, introduzca los detalles de la transacción: el importe que se enviará al destinatario y la tasa de cargo. No es necesario introducir una dirección de recepción, ya que el propio destinatario la transmitirá durante los intercambios PSBT.



A continuación, haga clic en `Revisar la configuración de la transacción`.



![Image](assets/fr/16.webp)



Compruebe los datos y pulse el botón verde "INICIAR TRANSACCIÓN" para empezar a intercambiar PSBT mediante el escaneado del código QR.



![Image](assets/fr/17.webp)



El intercambio se realiza alternando el escaneo con el colaborador: haz clic en "MOSTRAR CÓDIGO QR" para mostrar tu código QR a tu colaborador, que lo escaneará. A continuación, él hará clic en "MOSTRAR CÓDIGO QR" para mostrar el suyo, y tú lo escanearás con "LANZAR ESCÁNER QR". Repita este proceso hasta completar los cinco pasos de intercambio.



![Image](assets/fr/18.webp)



Una vez completados todos los intercambios, compruebe los detalles de la transacción y, a continuación, libérela arrastrando la flecha verde situada en la parte inferior de la pantalla.



![Image](assets/fr/19.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96). Su estructura es la siguiente:



![Image](assets/fr/20.webp)



*Crédito: [mempool.space](https://mempool.space/)*



Si analizamos esta transacción, vemos mi UTXO de 164.211 sats` en el lado de entrada, así como el UTXO de 190.002 sats` perteneciente al receptor real del pago. En el lado de la salida, recibo una UTXO de intercambio de 63.995 sats`, mientras que el receptor recibe una UTXO de 290.002 sats`. Comparando inputs y outputs, podemos ver que el receptor ha ganado 100.000 sats`, que corresponde a la cantidad de mi pago real, y que yo he perdido 100.000 sats`, a los que he añadido los costes de mining.



Obviamente, puedo describir esta estructura porque yo mismo he construido la transacción. Pero para un observador externo, generalmente es imposible determinar qué UTXOs pertenecen a cada participante, ya sea en las entradas o en las salidas.



Para profundizar en la gestión de la privacidad onchain en Bitcoin, te recomiendo que tomes mi formación BTC 204 en Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c