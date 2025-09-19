---
name: Wallet of Satoshi
description: El Wallet de custodia más sencillo para empezar
---
![cover](assets/cover.webp)

_Este tutorial ha sido escrito por_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## Descarga, configuración y uso de Wallet de Satoshi


Wallet de Satoshi es un Lightning Network Wallet, de custodia, y muy fácil de usar.

A efectos del curso [BTC105 - Finding Now](https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5), se utiliza para Redeem Lightning Network vales.


**Siempre recuerda**: _ni tus llaves, ni tus monedas_


Los monederos custodiados no permiten a los usuarios un control total sobre sus fondos. Normalmente no se recomiendan, excepto para principiantes. WoS debe utilizarse como Wallet de transición o para guardar dinero de bolsillo, no para acumular fondos a largo plazo.


---

Wallet de Satoshi (WoS) es un producto de custodia, pero tiene cierta reputación. Podemos recurrir razonablemente a una herramienta como WoS, por ejemplo, para aumentar nuestra capacidad de recibir liquidez. Delegamos temporalmente en WoS el "trabajo sucio" de gestionar la liquidez de los canales por nosotros. Una vez alcanzada cierta cantidad, vaciaremos el On-Chain de WoS a nuestro Wallet no custodiado.


**WARNING⚠️: Se recomienda leer el tutorial en su totalidad antes de continuar**


### Descarga de Wallet de Satoshi


Ve a Play Store y descarga WoS


![image](assets/it/01.webp)


**Nota:** WoS solo se descarga desde tiendas oficiales. Si el sistema operativo del dispositivo está programado, antes de abrir WoS hay una parte de verificación por parte del propio SO. Después de la fase de verificación, elija _Abrir_.


![image](assets/it/02.webp)


Wallet de Satoshi se abre con la siguiente pantalla, y es necesario pulsar sobre _Start_


![image](assets/it/03.webp)


### Registrar una cuenta en WoS


En este punto, la Wallet ya está operativa, pero para mayor seguridad, procedemos a configurar un login: será necesario para recuperar fondos en caso de mal funcionamiento o pérdida del dispositivo. Por lo tanto, seleccione el menú en la parte superior izquierda.


![image](assets/it/04.webp)


Se abre toda la ventana del menú, en la que debe configurar exclusivamente la moneda (Wallet de Satoshi presenta por defecto el dólar estadounidense como moneda de referencia) y el color del tema (claro/oscuro), según su gusto. No utilice los demás comandos.


Al ser WoS una herramienta de custodia, no podemos hacer una copia de seguridad de la Wallet con la frase Mnemonic, pero podemos habilitar WoS para recuperar nuestros fondos, en caso de pérdida o no uso del dispositivo móvil, haciendo clic en _Inicio de sesión/Registro_

Aparece una ventana que nos pide que introduzcamos un correo electrónico Address. Puede ser **un correo Proton** (recomendado), pero debe ser funcional, ya que nos permitirá recuperar los fondos en el Wallet en caso de pérdida/robo o deterioro del móvil.


![image](assets/it/08.webp)


Wallet de Satoshi ha enviado un mensaje a la bandeja de entrada de correo electrónico indicada.


![image](assets/it/09.webp)


En el buzón, encontraremos dos palabras, que deberemos introducir, reescribiéndolas, en el espacio que nos proporciona la app.


- no active el traductor: las palabras están y deben permanecer en inglés
- reescribe las dos palabras prestando atención a las mayúsculas/minúsculas


![image](assets/it/10.webp)


Después de transcribir las dos palabras, haga clic en _OK_.


![image](assets/it/11.webp)


El resultado debería ser una imagen que aparece en la parte superior, con el símbolo de la marca de verificación.


![image](assets/it/12.webp)


mientras que en la sección de configuración, la barra roja _Login/Register_ muestra ahora el correo electrónico Address del usuario.


![image](assets/it/13.webp)


### Recepción de pagos


Para recibir en WoS, haz clic en _Recibir_ y aparecerán una serie de comandos.


![image](assets/it/14.webp)


Puede recibir


- a través de LN-Address **a**
- a través de LN, ajustando el Invoice **b**
- on chain (WoS apoya la red Bitcoin pero con intercambios submarinos de pago) **c**
- escaneando el código QR de un LNurl-p **d**


![image](assets/it/15.webp)


### Creación de una Invoice


Haga clic en _Recibir_ y elija el comando con el símbolo Lightning Network.


![image](assets/it/16.webp)


Aparece el menú de creación de Invoice, donde hacemos clic en _Add Amount_ para escribir el importe exacto y añadir una descripción, en este ejemplo, "Mi primer Invoice".


![image](assets/it/17.webp)


Con el teclado, fijamos la cantidad.


![image](assets/it/18.webp)


para luego cobrar el Invoice. El pago recibido aparece así:


![image](assets/it/19.webp)


### Recogida en TPV


Wallet de Satoshi tiene una característica por defecto, que lo hace especialmente adecuado para los comerciantes: el TPV. Veamos cómo activarlo.


En la pantalla principal, seleccione el menú de la parte superior derecha.


![image](assets/it/20.webp)


A continuación, seleccione _Punto de venta_.


![image](assets/it/21.webp)


Con la última versión de WoS, asegúrate de seleccionar el _Teclado_.


![image](assets/it/22.webp)

y a continuación teclee el importe en el teclado, en el ejemplo que sigue igual a 10 céntimos / 118 Sats. Añada una descripción para la recaudación, en este caso "mi segunda con TPV". Se enciende un botón grande Green, y hay que pulsarlo

![image](assets/it/23.webp)


para generate la Invoice y mostrársela, por ejemplo, a un cliente.


![image](assets/it/24.webp)


¡Este pago también se cobra!


![image](assets/it/25.webp)


### Envío de pagos


La simplicidad es un punto fuerte de la pantalla principal de WoS. Para pagar un Invoice, haga clic en _Enviar_


![image](assets/it/26.webp)


En el primer uso, WoS pide permiso para acceder a la cámara


![image](assets/it/27.webp)


A partir de este momento la cámara se activa


![image](assets/it/28.webp)


Enmarcando la Invoice, vemos que se ha solicitado un pago de 210 Sats. También se lee una descripción, si el solicitante la ha establecido. Esta pantalla es el resumen y también una solicitud de confirmación: WoS "pide autorización" para enviar el pago, que se concede pulsando el botón Green _Enviar_


![image](assets/it/29.webp)


Cuando el pago llega a su destino, WoS notifica con esta pantalla


![image](assets/it/30.webp)


Desde la pantalla principal, pulsando en _Historial_ (justo debajo del saldo) aparece la lista de transacciones


![image](assets/it/31.webp)


#### Recuperación de la cuenta WoS


Ahora, veremos cómo instalar WoS en un nuevo dispositivo; esto también será útil en casos de robo, pérdida o imposibilidad de operar el teléfono móvil en el que el Wallet estaba previamente instalado. Una vez reinstalado, deberás volver a realizar el procedimiento de registro de cuenta que acabamos de explicar, con una única variante: al final de la solicitud de inicio de sesión con el correo electrónico previamente configurado, WoS aparecerá así:


![image](assets/it/33.webp)


Un mensaje nos avisa de que se ha enviado un correo electrónico con el procedimiento para reactivar la cuenta. Debe abrir la bandeja de entrada de su correo electrónico.


**IMPORTANTE**: abrir el correo electrónico desde un PC o, en todo caso, desde un dispositivo distinto de aquel en el que se va a recuperar la cuenta WoS. En la bandeja de entrada, encontramos un mensaje que nos muestra un código QR para enmarcar


![image](assets/it/34.webp)


Una vez enmarcado el código QR, en la página principal de WoS aparecerá la cuenta recuperada, con el saldo y el historial.