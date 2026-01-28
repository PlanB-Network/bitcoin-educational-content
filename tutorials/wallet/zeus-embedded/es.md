---
name: Zeus Embedded
description: Cómo utilizar Lightning Zeus Embedded Wallet
---
![cover-zeus-embedded](assets/cover.webp)



ZEUS es inicialmente una aplicación móvil para la gestión remota de nodos de rayos, que le permite controlar su nodo instalado en un servidor remoto


Pero la aplicación también cuenta con un "Nodo incrustado".



**Es esta faceta de la aplicación la que exploraremos en este tutorial.** Esto permite a cualquiera tener su propio nodo de rayos en el móvil, sin necesidad de un servidor dedicado, del mismo modo que ACINQ ofrece su increíble Wallet lightning Phoenix.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

*Como recordatorio, Lightning es una red que funciona en paralelo con Bitcoin, lo que permite intercambiar bitcoins sin tener que realizar sistemáticamente transacciones On-Chain. El resultado son transacciones casi instantáneas, sin necesidad de esperar 10 minutos a que se valide un bloque. El resultado son transacciones casi instantáneas, sin necesidad de esperar 10 minutos a que se valide un bloque. Esto resulta especialmente útil a la hora de pagar a un comerciante en el mundo físico. Además, Lightning proporciona un notable nivel de **confidencialidad** que la red Bitcoin no posee de forma nativa*.



**Zeus "Integrado "** está dirigido a Bitcoiners que quieren maximizar su privacidad y autonomía.


En resumen, es **potencialmente** el Wallet móvil de los sueños de los cypherpunks. Aunque todavía está en pañales (versión alfa) y sujeto a algunos bugs, sus características son legión, y no hay duda de que hará las delicias de los más intrépidos entre nosotros, que quieren el máximo control y opcionalidad.



Por otro lado, no creo que actualmente sea adecuado para principiantes que no estén familiarizados con Bitcoin y simplemente quieran una forma sencilla de enviar/recibir satoshis. Aunque esto puede cambiar en el futuro, ya que se está implementando una función de custodia a través del protocolo Cashu (chaumian Ecash) para principiantes...



## Instalar la aplicación



Visite [el sitio web del proyecto](https://zeusln.com/) para descargar la aplicación para el sistema operativo de su smartphone:



![image](assets/fr/01.webp)



![image](assets/fr/02.webp)



## Creación de carteras



Una vez iniciada la aplicación, pulse el botón "Inicio rápido" para empezar a crear la Wallet.



![image](assets/fr/03.webp)





A continuación, aparecerá una serie de pantallas de inicialización. Espere unos instantes y, a continuación, espere unos minutos hasta que el nodo esté sincronizado al 100% a través de Neutrino.



Esto puede tardar unos minutos. A título informativo, neutrino es una forma de que los monederos móviles accedan a la información de Blockchain Bitcoin, sin necesidad de ejecutar un Full node.



![image](assets/fr/04.webp)





Después de unos momentos, ya está listo.



![image](assets/fr/05.webp)




## Configuración de la aplicación



Listo, bueno no del todo, porque no hace falta decir que un usuario de Zeus digno de ese nombre navega por su Wallet con clase y estilo. Así que vamos a tener que cambiar su avatar.



Haz clic en tu avatar en la esquina superior derecha de la pantalla:



![image](assets/fr/06.webp)





Haga clic en la rueda dentada y, a continuación, en el signo más "+" :



![image](assets/fr/07.webp)





Selecciona la foto más bonita de Zeus para representar este Wallet y haz clic en "ELEGIR FOTO" en la parte inferior de la pantalla, luego vuelve atrás haciendo clic en la flecha de arriba a la derecha.



![image](assets/fr/08.webp)





Por último, asigne un apodo a su Wallet y haga clic en "GUARDAR CONFIG Wallet" para que el cambio surta efecto. Por último, haga clic en la flecha hacia atrás situada en la esquina superior izquierda para volver a la pantalla de inicio.



![image](assets/fr/09.webp)





Esta vez sí que podemos empezar.



![image](assets/fr/10.webp)



### Biometría



Para proteger el acceso a tu Wallet, puedes añadir un PIN/contraseña y activar la biometría.



Para ello, vaya al menú principal de Wallet haciendo clic en los guiones horizontales de la parte superior izquierda.



![image](assets/fr/11.webp)





Seleccione "Ajustes", luego "Seguridad" y, por último, "Establecer/cambiar PIN".



![image](assets/fr/12.webp)





Cree su PIN, confírmelo y active la biometría pulsando el botón "Biometría" correspondiente.  Vuelve al menú principal, utilizando la flecha de arriba a la izquierda.



![image](assets/fr/13.webp)




### Salvar la frase Mnemonic



Una vez de vuelta en el menú principal, haz clic en "Copia de seguridad de Wallet", y luego lee el texto de advertencia que te informa de que perder las 24 palabras que estás a punto de recibir equivale a perder el acceso a tus fondos, y que cualquiera que tenga estas palabras además de ti puede acceder a tus fondos. Nunca se las des a nadie.



Selecciona "ENTIENDO" en la parte inferior de la pantalla. A continuación, haz clic en cada una de las 24 palabras para que aparezcan y anótalas con atención.



Puede escribirlo en papel o, para mayor seguridad, grabarlo en acero inoxidable para protegerlo de incendios, inundaciones o derrumbes. La elección del soporte para tu Mnemonic dependerá de tu estrategia de seguridad, pero si utilizas Zeus como cartera de gastos con importes moderados, el papel debería ser suficiente.



Para más información sobre la forma correcta de guardar y gestionar tu frase Mnemonic, te recomiendo encarecidamente que sigas este otro tutorial, especialmente si eres principiante:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![image](assets/fr/14.webp)



Una vez terminado, pulsamos en "HE HECHO UNA RESERVA DE MIS 24 PALABRAS" en la parte inferior de la pantalla, y ya estamos de nuevo en la pantalla de inicio, listos para recibir nuestros primeros bitcoins.




## Opción 1 - Recibir On-Chain bitcoins y abrir un canal Lightning



**Zeus Embedded** está diseñado principalmente como nodo de rayos embebido, pero también puede utilizarse como Wallet On-Chain.



Para recibir bitcoins On-Chain, haga clic en el botón "On-Chain" y luego en "Recibir".


Por último, escanee el código QR o copie el Bitcoin Address para depositar fondos.



![image](assets/fr/15.webp)





Una vez que los fondos han sido confirmados y acreditados en tu Wallet, puedes utilizarlos para abrir un **canal Lightning**. Tu canal Lightning es tu puerta de entrada a la Lightning Network, permitiéndote Exchange bitcoins de una forma mucho más confidencial y rápida.





- Para ello, haga clic en "MOVE On-Chain FUNDS TO LIGHTNING"



En la pantalla siguiente, se le pide que abra un canal en colaboración con **"Olympus by Zeus "**, el LSP (Lightning Service Provider) preferido por Wallet.


Para este tutorial, elegiremos esta opción por simplicidad, pero es perfectamente posible abrir canales con cualquier nodo de la red.


Incluso es posible abrir varios canales en una sola transacción seleccionando "ABRIR CANAL ADICIONAL". *Pero esto lo veremos en una versión "avanzada" del tutorial* **Zeus Embedded**.





- A continuación, seleccione la cantidad que desea dedicar a este canal. En nuestro caso, se utilizarán todos nuestros fondos de On-Chain, por lo que activamos el botón "Utilizar todos los fondos posibles".





- Por último, selecciona el botón "ABRIR CANAL" en la parte inferior de la pantalla.



![image](assets/fr/16.webp)





En cuestión de segundos, el canal está establecido y estamos listos para realizar nuestras primeras transacciones Lightning. En la pantalla de inicio, podemos ver un pequeño reloj junto a nuestro saldo Wallet. Esto se debe a que aún tendremos que esperar 3 confirmaciones On-Chain antes de que el canal sea realmente funcional.



![image](assets/fr/17.webp)





Después de las 3 confirmaciones, observamos que nuestro saldo se ha abonado en la inserción Rayo.



![image](assets/fr/18.webp)



Un pequeño detalle: cuando hacemos clic en el menú de la parte inferior de la pantalla para ver el estado de nuestros canales relámpago, vemos que una pequeña parte de nuestro saldo no está disponible para gastar: sólo podemos gastar 208253 satoshis en lugar de los 210370 que realmente tenemos. Esto es normal, ya que es específico del protocolo relámpago.



Por último, hay que tener en cuenta que nuestro partner Olympus se reserva el derecho de cerrar el canal a su discreción, si no se está utilizando, por ejemplo. Para asegurarnos de que nuestro canal se mantiene, tendremos que pagar al LSP (Lightning Service Provider), como veremos en el siguiente párrafo, a través de la 2ª vía de apertura de un canal.





## Enviar bitcoins a través de Lightning



Ahora que ya tenemos nuestro canal en marcha, vamos a ver cómo podemos utilizarlo para pagar un rayo Invoice (Invoice).



Para ello, haga clic en el botón "Lightning" y, a continuación, en "Enviar".



![image](assets/fr/19.webp)





En la siguiente pantalla, copie su Invoice en el campo correspondiente, o escanéelo haciendo clic en el icono de la parte superior derecha. Por último, deslice el botón "Deslizar para pagar" hacia la derecha para pagar.



![image](assets/fr/20.webp)






Espera unos segundos y el Invoice estará pagado, y tus satoshis habrán viajado a la velocidad de la luz.



![image](assets/fr/21.webp)





Zeus te permite añadir una nota para denominar tu pago, o ver la ruta que siguieron tus satoshis antes de llegar a su destino (y los cargos cobrados por todos los nodos intermedios). Este es el tipo de funcionalidad que nos encanta de Wallet.



![image](assets/fr/22.webp)



Ten en cuenta que, a diferencia de una Wallet como [Phoenix]([Plan ₿ Academy - Phoenix](https://planb.academy/fr/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf)), con Zeus la ruta se calcula localmente y no se delega en un tercero (ACINQ en el caso de Phoenix). Así que tú eres el único que conoce al destinatario del pago. Perdemos un poco de eficacia (los pagos tardan un poco más en completarse, pero ganamos mucho en términos de privacidad).





Haciendo clic en la flechita de la parte inferior de la pantalla de inicio, también podemos ver nuestro historial de pagos. Aquí vemos en Green los 212.121 Sats recibidos por On-Chain, luego en rojo respectivamente los 211.756 Sats utilizados para abrir nuestro canal, luego los 121.212 satoshis utilizados para pagar nuestro relámpago Invoice.



![image](assets/fr/23.webp)





## Opción 2 - Recibir bitcoins directamente en Lightning



En lugar de abrir un canal manualmente, como acabamos de ver, es posible recibir fondos directamente a través de Lightning, incluso sin un canal preexistente, utilizando Olympus, el PSL Zeus.




- Para ello, haga clic en el botón "Lightning" de la pantalla de inicio y, a continuación, en "Recibir".
- A continuación, elija el importe que desea recibir en la casilla "Importe" y seleccione el botón "CREAR Invoice" en la parte inferior de la pantalla.



![image](assets/fr/24.webp)





La siguiente pantalla muestra los Invoice que hay que pagar para recibir los satoshis. Se nos indica que el PSL retendrá 10.000 Sats si el pago se realiza por Lightning. Veremos más adelante cómo se justifican estas tasas de apertura de canal.



Paga el Invoice o haz que otro lo pague, y el canal se abrirá automáticamente, pero descontando los 10.000 Sats según lo acordado.



![image](assets/fr/25.webp)





Ahora estamos a la cabeza de 2 canales de rayos, cuyo estado puede comprobarse pulsando el botón indicado por la flecha blanca en la parte inferior de la pantalla de inicio.



Podemos ver que, a diferencia del canal abierto desde nuestra báscula On-Chain, el abierto directamente a través de un rayo no muestra ninguna advertencia.


Como has pagado por configurar este canal, el Proveedor de Servicios de Rayos (PSL) se compromete a mantenerlo durante 3 meses y te ofrece "liquidez entrante". En el canal inferior, puede ver que la capacidad de recepción es de 96383 satoshis. Por tanto, el PSL ha inmovilizado capital para que usted pueda recibir pagos directamente tras la apertura del canal.



Así pues, los 10.000 Satoshi de derechos pagados cubren: el coste de apertura del canal (transacción Bitcoin On-Chain, la garantía de mantenimiento del canal durante 3 meses y la inmovilización del capital).



![image](assets/fr/26.webp)





Enhorabuena, ya estás listo para utilizar Zeus Embedded, el sistema de iluminación móvil Wallet con las funciones más avanzadas del mercado.





Para saber más sobre el funcionamiento técnico de Lightning Network, puede consultar la excelente formación gratuita de Fanis Michalakis sobre Plan ₿ Academy:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb