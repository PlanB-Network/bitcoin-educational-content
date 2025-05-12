---
name: Sats.mobi

description: Una custodia accesible por telegrama Wallet
---

![cover](assets/cover.webp)


_Este tutorial ha sido escrito por_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## Sats.Mobi

SatsMobi es un Wallet que opera en Telegram, presentando todas las funcionalidades de un Lightning Network (custodio) Wallet, además de una serie de características muy entretenidas. Se originó a partir de un Fork del ya descatalogado LightningTipBot, heredando todas sus funcionalidades a la vez que añadiendo otras más actuales, haciéndolo así más moderno. Al igual que LNTipBot, Sats.Mobi también adopta la filosofía del código abierto. El Wallet se puede configurar y gestionar de forma independiente clonándolo desde este [repositorio](https://github.com/massmux/SatsMobiBot).


Si prefieres usarlo de forma sencilla, al iniciar un chat en Telegram te revelará que se trata de un bot.


## Ajustes

Desde la barra de búsqueda de Telegram, busca "satsmobi" y aparecerá el enlace al [bot](@SatsMobiBot).


**Atención**: Si no estás seguro de buscar a través de Telegram, accede al bot de forma segura utilizando el siguiente [enlace](https://t.me/SatsMobiBot)


![image](assets/it/01.webp)


Para empezar, sólo tienes que pulsar _START_


![image](assets/it/02.webp)


Para explorar el Wallet, puedes seleccionar _Menu_ en la parte inferior izquierda.


![image](assets/it/03.webp)


Ahora opta por _/help_ entre los comandos principales.


![image](assets/it/04.webp)


Sats.Mobi nos da la bienvenida mostrando un mensaje, enumerando las principales funcionalidades. Al iniciarse, el bot también crea un LN Address, vinculado al handle elegido en Telegram (que es único por defecto). Los comandos para enviar y recibir Sats con este Wallet son visibles, así como otras funciones que veremos más adelante. Es interesante también echar un vistazo al menú _/advanced_


![image](assets/it/05.webp)


Llama la atención que Sats.Mobi también ha creado un LN Address anónimo, que se utilizará para ganar privacidad. El bot funciona con comandos: basta con hacer clic en la palabra correspondiente, o escribir la barra "/" en la barra de mensajes, seguida del comando que se desea ejecutar. Incluso si el Wallet acaba de ser creado, elige por ejemplo _/transactions_


![image](assets/it/06.webp)


Este comando muestra la lista de las últimas transacciones, en este caso concreto igual a cero.


![image](assets/it/07.webp)


## Recepción de Sats

El comando para crear una Invoice y recibir Sats es _/factura_. Sats.Mobi opera exclusivamente en Satoshi, la unidad más pequeña de Bitcoin; por lo tanto, para crear la Invoice, es necesario escribir la cantidad en Sats en la barra de mensajes y luego enviarla en el chat con el bot.

![image](assets/it/08.webp)


En el siguiente ejemplo, se ha optado por recibir un importe de 210 Sats.


![cover](assets/it/09.webp)


Tras unos instantes de espera, la Invoice está disponible como texto y como código QR. Al pagar la Invoice, la Wallet muestra el saldo. Si por alguna razón no se actualiza el total, escriba _/saldo_ y pulse la tecla `enter`.


![image](assets/it/10.webp)


## Envío de Sats


Aunque los Sats son un activo muy valioso, del que no hay que desprenderse a la ligera, Sats.Mobi hace que esta parte sea atractiva, realizar algunas pruebas breves (es decir, un par de transacciones de prueba) no supondrá ningún problema.


### Pagar un Invoice


La forma más sencilla de pagar un Invoice es copiar la cadena de mensajes `lnbc1xxxxx` y pegarla en la barra de mensajes después de teclear el comando _/pay_. **La sintaxis correcta** requiere dejar un espacio después del comando.


![image](assets/it/11.webp)


La Wallet envía un mensaje pidiendo confirmación. Al hacer clic en _Pay_, la Invoice recibe el pago.


![image](assets/it/12.webp)


Sats.Mobi puede confiar en un nodo Rayo eficiente y bien conectado, rara vez fallan los pagos porque siempre consigue encontrar la ruta correcta.


### Pagar cómodamente desde el móvil


Navegando por Telegram, Sats.Mobi también está disponible en el móvil. La función más cómoda para pagar con el móvil es escanear un código QR, pero esta Wallet carece de ella por diseño, ya que no es una app independiente, sino que está contenida en una red social. Por ello, Sats.Mobi está programada para facilitar al máximo la experiencia móvil: de hecho, puede descodificar una imagen, como una fotografía tomada del código QR de la Invoice que se desea pagar.


Supongamos, por ejemplo, que quiere pagar un Invoice de 50 Sats.


![image](assets/it/20.webp)


Cuando se nos muestre, podemos hacer una foto del código QR relacionado.


![image](assets/it/21.webp)


A continuación, abrimos Telegram en el móvil y, en el chat con Sats.Mobi, adjuntamos la foto que acabamos de hacer del código QR


![cover](assets/it/22.webp)


Una vez seleccionada, la enviamos al bot:


![image](assets/it/23.webp)

Sats.Mobi descodifica la foto y **presenta inmediatamente la solicitud de pago**, con la descripción correcta. El chat pide confirmación, para proceder hay que pulsar _/pay_

![image](assets/it/24.webp)


Espere un momento para que se procese el pago.


![image](assets/it/25.webp)


Se ha pagado la Invoice por 50 Sats, un resultado conseguido sin utilizar una cámara y su función de escaneado integrada.


### Sats.Mobi en Grupos de Telegramas


![image](assets/it/27.webp)


Entre las características que hicieron famoso a LNTipBot y que Sats.Mobi aporta a Telegram, está la de hacer que la experiencia sea divertida e interactiva para los miembros de un grupo.

Los propietarios pueden invitar al bot a unirse al chat del grupo y, a continuación, nombrar a Sats.Mobi como administrador. A partir de ese momento, empieza la diversión, porque los miembros pueden empezar a recompensar a otros usuarios por su contribución al grupo.


- _/tip_ añade un consejo respondiendo a un mensaje;
- _/send_ envía fondos especificando una LN Address o una asa de Telegram como destinatario;
- _/faucet_ (en el menú _/advanced_) permite crear una serie de propinas que los miembros más rápidos del grupo pueden recoger haciendo clic en _/collect_;
- _/tipjar_ (en el menú _/avanzado_) crea otro tipo de distribución que se puede enviar a los usuarios del grupo.


Cada uno de estos comandos tiene su sintaxis, que se explica en el menú principal de comandos.


¿Y si no somos el propietario de un grupo? No hay problema: basta con pedir al fundador que invite a Sats.Mobi, añadirlo como administrador del grupo, ¡y listo!


## Punto de venta (TPV)


Cuando Sats.Mobi se lanza por primera vez, el bot también crea otra función para el usuario: **el TPV**. El "dispositivo" es activado por el usuario con el comando _/pos_ o haciendo clic en el botón relacionado de la consola en la parte inferior derecha. De hecho, el TPV es una aplicación web que se abre como una ventana emergente en el chat de Telegram


![image](assets/it/14.webp)


La Interface muestra el mango personal de Telegram del usuario en la parte superior izquierda y se utiliza simplemente como se utilizan todos los TPV: tecleando la cantidad en el teclado. Supongamos ahora que queremos cobrar 21 céntimos de euro por un servicio. Sabiendo que Sats.Mobi sólo gestiona nativamente Sats, no es fácil hacer la conversión mentalmente. Por el contrario, el TPV muestra el euro como unidad de cuenta, mostrando al mismo tiempo el equivalente en Satoshi.


![image](assets/it/15.webp)

Al hacer clic en _/OK_ aparece la Invoice que se puede mostrar al cliente mediante un código QR, o que se puede enviar como una cadena a través de mensajería instantánea, para que pueda pagarla.

![image](assets/it/16.webp)

![image](assets/it/17.webp)


Naturalmente, el TPV también está disponible en los teléfonos móviles, a los que se accede de la misma forma que en el caso anterior.


![image](assets/it/18.webp)


También se visualiza bien en la pantalla del móvil:


![image](assets/it/19.webp)


## Características adicionales


Hay otras características que completan la oferta de la Sats.Mobi Wallet, que, como hemos visto, amplía el concepto de una Wallet más allá de las operaciones de recepción y envío de pagos:


- _/nostr_: para conectar la Wallet a tu propio usuario Nostr para recibir zaps;
- _/cashback_: muestra un código que se puede presentar a un comerciante para obtener cashback en una compra;
- _/buy_: inicia un procedimiento guiado dentro del bot, que permite comprar Sats por euros;
- _/activatecard_: para solicitar la activación de una tarjeta de débito NFC, recargable a través de la Sats.Mobi Wallet y para la que se pueden activar notificaciones;
- _/link_: crea un enlace para tu propio Zeus o Blue Wallet, que pueden utilizarse como mandos a distancia para este Wallet.


## Conclusión

Sats.Mobi es un Wallet agradable y divertido de usar, que recuerda las experiencias vividas con LNTipBot utilizando las funciones más avanzadas de LNBits. Sin embargo, es importante recordar que **es un servicio de custodia**. Por lo tanto, debe ser utilizado para mantener muy pocos Sats, no es un Wallet principal para sus fondos Lightning Network. También existe un límite de capacidad intrínseca, igual a 500.000 Sats, límite que se aconseja no sobrepasar.


Si busca carteras Lightning Network no custodiadas, sin duda es aconsejable que busque otros productos.


---
### Documentación


- [Github](https://github.com/massmux/SatsMobiBot)
- Lista de reproducción de [vídeos](https://www.youtube.com/results?search_query=Sats.mobi) demo