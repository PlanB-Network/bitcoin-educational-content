---
name: Alby

description: Extensión del navegador para Bitcoin y Lightning Network
---

![cover](assets/cover.webp)




Facilitar cada vez más los pagos con bitcoin es el reto al que se enfrentan muchas empresas del sector. Alby destaca entre la multitud con su extensión Alby wallet para navegadores. Esta extensión pretende establecer un marco fluido que detecte automáticamente las direcciones y permita realizar pagos con bitcoin sin fricciones. En este tutorial, descubrimos la extensión Alby y probamos cómo facilita los pagos desde el navegador.




![video](https://youtu.be/nd5fX2vHuDw)




## Ampliación Alby



La extensión Alby es una herramienta que permite a su navegador web interactuar de forma fácil y segura con la red Bitcoin y su capa Lightning Network. Se caracteriza por tres aspectos:




- Lightning Network wallet: Vincule su nodo o cuenta Alby para enviar y recibir bitcoin de forma rápida y económica a través de la capa Lightning Network.
- Pagos fluidos a través de la Web: Elimina la necesidad de escanear códigos QR o cambiar entre aplicaciones para realizar pagos con bitcoin en sitios web compatibles con Lightning. Permite realizar transacciones fluidas con un solo clic, o sin confirmación si has establecido un presupuesto.
- Un gestor de Nostr: La extensión gestiona tus claves Nostr, facilitando la conexión e interacción con aplicaciones Nostr actuando como firmante seguro sin exponer tu clave privada a todas las plataformas.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Conectarse a la extensión



En este tutorial, utilizaremos la extensión Alby en el navegador Firefox bajo un sistema operativo Ubuntu. Sin embargo, también está disponible en Windows y con navegadores como Chrome.



Puede añadir la extensión Alby a su navegador visitando la tienda de extensiones [Firefox](https://addons.mozilla.org/fr/firefox/addon/alby/) o la tienda de extensiones [Chrome](https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe).



![firefox](assets/fr/01.webp)



![chrome](assets/fr/02.webp)



ℹ️ Es importante comprobar que el autor de la extensión es efectivamente la cuenta oficial de Alby, para evitar cualquier forma de piratería o robo de tus bitcoins.



Añada la extensión a su navegador haciendo clic en el botón de la derecha.


Conceda los permisos necesarios para instalar y utilizar la extensión y, a continuación, fíjela a la barra de herramientas para recuperarla fácilmente.



![pin](assets/fr/03.webp)



También debe definir un código de desbloqueo (muy importante), que le garantizará un acceso seguro a su Lightning wallet desde su navegador. Le sugerimos que establezca una contraseña alfanumérica fuerte.



ℹ️ Guarde esta contraseña en un lugar seguro para poder acceder a ella en caso de olvido, ya que puede cambiarse pero no recuperarse.



https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)



Alby demuestra su adaptabilidad ofreciéndole dos opciones:




- Continúa con una cuenta Alby si quieres disfrutar de las aplicaciones manteniendo el control de tus bitcoins.
- Conecte su propio nodo wallet o Lightning si ya dispone de uno compatible con la extensión.



https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


En este tutorial, elegimos continuar con la cuenta Alby para aprovechar las características del ecosistema Alby.



https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Accede a tu cuenta Alby, o crea una si aún no la tienes.



![signup](assets/fr/05.webp)



## Efectuar los primeros pagos



Una vez conectado, puede hacer clic en la extensión Alby de la barra de herramientas para acceder a su cartera.



![buzzin](assets/fr/06.webp)



Una vez que haya creado su cuenta Alby, tendrá que conectarla a una wallet para poder gastar satoshis. Para vincular la wallet bitcoin a su cuenta Alby, le sugerimos que utilice un nodo Alby Hub, que puede configurar en su ordenador o suscribirse a un plan ofrecido por Alby.



![hubplan](assets/fr/13.webp)




En este tutorial, nuestra cuenta Alby se apoya en una instalación local en nuestra máquina.


Para construir tu propio nodo Alby, te recomendamos nuestro tutorial Alby Hub.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Este nodo te permite crear carteras Lightning autocustodiadas y gestionar eficazmente tus canales Lightning para enviar y recibir satoshis.



![channels](assets/fr/14.webp)



Abra canales de recepción que definan el número total de satoshis que puede recibir.



![receivechanal](assets/fr/15.webp)



Abre canales de envío bloqueando satoshis en una dirección bitcoin onchain. Los satoshis que has bloqueado definen el total de satoshis que puedes gastar.



![spend](assets/fr/16.webp)



Ya puedes enviar y recibir satoshis a través de la extensión Alby.



![exchange](assets/fr/08.webp)



A partir de este momento, la extensión Alby es capaz de detectar las direcciones Lightning y las facturas disponibles en las páginas web que visites, y te sugerirá que las pagues en bitcoin o Lightning directamente desde tu extensión.



![suggest](assets/fr/09.webp)



![pay](assets/fr/10.webp)




## Proteger las claves de recuperación con la clave maestra



La llave maestra que ofrece la extensión Alby actúa como una capa protectora que le permite comunicarse de forma segura con la capa de red principal Bitcoin (Onchain), el sistema Nostr y le permite activar la conexión Lightning con las aplicaciones Nostr.



![masterKey](assets/fr/11.webp)



Esta clave maestra tiene la forma de 12 palabras similares a su frase de recuperación. Por lo tanto, te recomendamos que la almacenes utilizando métodos seguros para garantizar que se pueda acceder a ella en cualquier momento.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)



Ahora puedes experimentar pagos bitcoin y Lightning sin fricciones con la extensión Alby. Si te ha gustado este tutorial, te recomendamos nuestro tutorial Alby Hub para configurar tu propio nodo Alby y controlar todos los aspectos de tus monederos Alby desde una interfaz fluida y potente.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a