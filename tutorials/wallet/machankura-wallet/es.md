---
name: Machankura
description: Utiliza Bitcoin en cualquier teléfono, sin Internet.
---

![cover](assets/cover.webp)




África avanza, innova y construye, pero sigue enfrentándose a numerosos retos, en particular la conectividad a Internet y el acceso a los servicios financieros básicos.


Según la Unión Internacional de Telecomunicaciones, en 2024 el índice de penetración de Internet en África (la relación entre el número de personas que utilizan Internet y la población total del continente) era del 38%, frente al 68% mundial.



En cuanto al acceso a los servicios financieros, los servicios de transferencia de dinero (dinero móvil) han experimentado un auge en el continente, tras las dificultades de acceso a los servicios de crédito bancario.


Ante esta situación, Kgothatso Ngako, un desarrollador sudafricano, ha creado una solución revolucionaria que permite a este segmento de la sociedad africana sin servicios bancarios ni Internet beneficiarse de la Bitcoin con su proyecto llamado **Machankura**.



## ¿QUÉ ES MACHANKURA?



Machankura, que en argot sudafricano significa "dinero", es un proyecto cuya visión es conectar el África rural con el ecosistema Bitcoin.



Es un Wallet custodiado que permite enviar y recibir bitcoins en el Lightning Network mediante tecnología USSD. Machankura funciona en todos los teléfonos, incluso los más básicos (teléfono Symbian), que utilicen la red GSM tradicional.


El **8333.mobi** que suele aparecer en la parte inferior del logotipo es un guiño sutil. En efecto, **8333** es el puerto por defecto que utilizan los nodos Bitcoin para comunicarse entre sí. Machankura demuestra que África no está al margen de esta revolución y es tierra de innovación en este campo.



El dominio **.mobi** está diseñado para servicios móviles que funcionan en teléfonos básicos a través de USSD. Por tanto, **8333.mobi** resume las particularidades de la solución Machankura.



Antes de continuar con este tutorial, echemos un vistazo a USSD, la tecnología que permite utilizar Machankura sin Internet.



## USSD



La tecnología USSD (*Unstructured supplementary Service Data*) es utilizada generalmente por los operadores de telefonía móvil GSM. Es una función que permite comunicarse con un servicio remoto, incluso sin Internet, utilizando códigos específicos y seleccionando una opción según las posibilidades que ofrezca el servicio.



En un proceso de comunicación USSD, imagine que teclea un código especial como `*123#` en su teléfono. Al ejecutar este código USSD, envías una solicitud específica a tu red GSM para acceder al servicio vinculado a este código.



Por lo tanto, puede utilizar el USSD para realizar acciones como consultar su paquete de Internet, el saldo del crédito de llamadas, etc.



A través de este mismo sistema de comunicación se han desarrollado en el continente la banca móvil y las transferencias de dinero por móvil, como M-PESA, MTN Mobile Money, etc.


Como decíamos antes, desarrollado específicamente para África, este servicio funciona en todos los teléfonos, sin necesidad de configuraciones técnicas complejas ni de conexión a Internet.



## Innovación en Machankura



A diferencia de una solución Wallet convencional, Machankura pudo utilizar la tecnología USSD para Address un problema real al que se enfrenta la población de África: la cobertura de Internet.



Machankura es un servicio desarrollado y posteriormente vinculado a un código GSM para permitir a los usuarios recibir y enviar bitcoins sin Internet. Puede utilizar el servicio en los siguientes países utilizando el código USSD asociado:



| PAYS           | CODE USSD              |
| -------------- | ---------------------- |
| Ghana          | `*920*8333#`           |
| Kenya          | `*483*8333#`           |
| Malawi         | `*384*8333#`           |
| Namibie        | `*142*8333#`           |
| Nigeria        | `*347*8333#`           |
| Afrique du Sud | `54052.co.za`          |
| Tanzanie       | `SMS +255 679 066 977` |
| Ouganda        | `SMS +256 744 830 624` |
| Zambie         | `*384*8333#`           |
| Côte d’Ivoire  | `*9141#`               |

Según esta tabla, podemos ver que países como Tanzania, Uganda y Sudáfrica no tienen un código USSD específico para el servicio.



Sin embargo, Machankura está abordando este problema ampliando su funcionalidad a través de su sitio web, mensajería SMS y WhatsApp.



Para estar informado de los nuevos países en los que estará disponible el servicio, consulte regularmente su [sitio web](https://8333.mobi).



Este tutorial explica paso a paso cómo utilizar Machankura, primero en un teléfono básico sin Internet y después en un smartphone.



## Funcionamiento sin smartphone (mediante USSD)



### Cree su cartera



Para su primera conexión :




- Introduzca el código USSD correspondiente a su país;
- Pulsa el botón de llamada para empezar.



El sistema le pedirá que cree un código PIN de 5 dígitos




- Elija un código PIN seguro (5 dígitos).
- Confirme su código PIN.
- Su cartera Bitcoin se crea al instante.



Esta Bitcoin Wallet está asociada a su número de teléfono. El código PIN cuidadosamente elegido codificará su Wallet y también se utilizará para confirmar todas sus futuras transacciones en Machankura.


Una vez creada su cartera, accederá al menú principal con las siguientes opciones:



1. Enviar bitcoins


2. Recibir bitcoins


3. Datos de la cuenta


4. Compra de bienes/servicios


5. Cambiar/restablecer código PIN


6. Salida



Para acceder a cualquier opción del menú principal, basta con pulsar el número de secuencia al que está asociada.


Para acceder a los "detalles de la cuenta", seleccione la opción **3** y pulse la tecla de llamada para iniciarla.



### Seguridad y buenas prácticas



Machankura es un Lightning Wallet de custodia, por lo que tus bitcoins se gestionan a través de los nodos de Machankura. Tu cuenta está protegida por el código PIN que elijas.





- No establezcas un código PIN en relación con una fecha importante de tu vida.
- Nunca compartas tu código PIN con nadie.
- Memoriza tu código PIN.
- Compruebe siempre los números de teléfono antes de enviarlos.
- Mantenga un equilibrio razonable para el uso diario.



Tu Wallet está vinculado a tu número de teléfono:




- Si pierdes tu teléfono, ponte en contacto con el servicio de asistencia de Machankura;
- Lleve un registro de sus transacciones importantes.



### Recibir bitcoins





- Seleccione el número de orden de la opción "Recibir Bitcoins" en el menú principal.
- Su número de teléfono es su Address público.
- Comparte tu número con la persona que quiere enviarte bitcoins.



#### Rayo personalizado Address



A cada cuenta Machankura se le asigna un Address Lightning basado en su número Machankura


`votrenumero@8333.mobi`


Ejemplo: un número +2371234567890 se convertirá en `+2371234567890@8333.mobi`


Sin embargo, puede elegir un nombre de usuario personalizado para sustituir el número (por ejemplo, `Satoshi@8333.mobi`).


Cualquiera que tenga tu Address de Lightning puede enviarte bitcoins sin saber tu número de teléfono.



#### Recargue su cartera Machankura



Además de recibir bitcoins de otra Wallet Lightning, puede reponer su Wallet Machankura con **Azteco** y **1Voucher** del **Grupo Flash**.



**Azteco** y **Flash Group** son dos empresas que ofrecen **vales** de Bitcoin, es decir, servicios de vales prepago que puede comprar en línea o a revendedores para obtener Bitcoin sin pasar por una plataforma de Exchange. Estos vales funcionan como **tarjetas regalo**. Existen **vales On-Chain** y **vales Lightning**.



![azteco](assets/fr/01.webp)



El proceso es sencillo:





- Usted compra un vale por un importe fijo;
- Recibirá un código de 16 dígitos por correo electrónico o en un pequeño Invoice.



![bonazteco](assets/fr/02.webp)





- Introduzca en su teléfono el código USSD MACHANKURA de su país.
- Espere a que aparezca el menú principal.
- Seleccione el número de orden de la opción ''Recibir bitcoins''.
- Introduzca el código de 16 dígitos (el código de referencia del vale Azteco que figura en la parte inferior del vale o el código PIN de 1Voucher que aparece en el Invoice).



Los bitcoins equivalentes al importe del vale adquirido se añaden directamente a su Wallet de Machankura.



### Enviar Bitcoins





- Ir al menú principal.
- Seleccione la opción "Enviar Bitcoin" introduciendo su número de pedido.
- Introduzca el número de teléfono del destinatario, el nombre de usuario Lightning Address o Machankura.
- A continuación, introduzca el importe a enviar en Sats.
- Confirme con su código PIN.



A continuación, Machankura envía los bitcoins por Lightning Network en cuestión de segundos. El remitente también puede enviar bitcoins en otras monedas, incluidas las locales.



Si el número del destinatario aún no se ha registrado como usuario, Machankura realizará un registro previo y, a continuación, un abono en la cuenta del destinatario.



Se envía automáticamente un mensaje al número prerregistrado, y el usuario recibe sus bitcoins una vez que ha confirmado su registro en el servicio.



Puedes ver el [vídeo de demostración de envío](https://www.linkedin.com/posts/activity-7351143606121820162-Ua3T?utm_source=share&utm_medium=member_android&rcm=ACoAAAeTubUB8GuaMia5yNBlBg4WhZpGOeVLY0w) de bitcoins por PIO TARAS (Lead Machankura Afrique Francophone) a través de Machankura en un teléfono básico.



*Vídeo de Vladimir FOMENE, desarrollador de Bitcoin :*



![video](https://youtu.be/rrovhcpg7ao)



### Compruebe su saldo





- Seleccione el número de orden de la opción "Saldo" del menú principal.
- Su saldo se muestra en satoshis y equivalentes en moneda local.



### Historial de transacciones





- Seleccione el número de secuencia de la opción ''Historial'' del menú principal.
- Consulte sus últimas transacciones (envíos y recibos).
- Compruebe los detalles de cada transacción.



### Características adicionales



Machankura no es sólo una Wallet. Puedes Exchange tus satoshis por bienes y servicios (por ejemplo, tarjetas regalo Bitrefill o Lightning Watts) directamente desde la app.



https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

También dispone de la función "**Clan**", que le permite gestionar un sistema cooperativo multi-firma: los miembros del clan deben aprobar cada gasto, y usted puede distribuir automáticamente los fondos entre ellos.



## Uso con smartphone



Machankura ha elegido WhatsApp como plataforma intermediaria para el uso de smartphones.



Hay dos razones principales para ello. La primera es hacer la solución más accesible a los africanos, sin obligarles a instalar una aplicación: una aplicación que podrían desinstalar fácilmente si su teléfono se quedara sin memoria de almacenamiento.



La segunda, que es una extensión lógica de la primera, es ser una solución inclusiva y local, utilizando una aplicación muy utilizada por los africanos en sus intercambios diarios: WhatsApp.



### Cree su cartera



Para empezar, tienes que escribir un mensaje al bot de WhatsApp de Machankura (un simple "Hola" es más que suficiente). Su número de WhatsApp es [+27 73 762 5720](https://wa.me/+27737625720).



Te pedirá que elijas el idioma en el que quieres chatear.



![wallet](assets/fr/03.webp)



Una vez elegido el idioma, accederás al menú principal.




- Respuesta **1** que corresponde a la opción "**Crear una cuenta**".
- Introduzca un correo electrónico único Address.



![wallet](assets/fr/04.webp)



Su cuenta Machankura se crea automáticamente. Vuelva al menú para definir su nombre de usuario.



Para hacerlo:




- Responda **0**, que corresponde a la opción ''**Parámetros**'';
- A continuación, responda **1**, que corresponde a la opción ''**Nombre de usuario**''.



![wallet](assets/fr/05.webp)



A continuación, el bot te enviará un código de **6 dígitos** que deberás introducir y elegir tu nombre de usuario. Una vez que hayas actualizado tu nombre de usuario, vuelve al menú para aprovechar las ventajas de enviar y recibir bitcoins a través de Machankura.



![wallet](assets/fr/06.webp)



### Enviar bitcoins



Machankura te permite enviar tus bitcoins a través de diferentes opciones:




- número de teléfono ;
- rayo Address, este formato de lectura humana Bitcoin Address se utiliza mucho más para evitar errores de mecanografía al efectuar los pagos;
- nombre de usuario del receptor, para pagos a una cuenta Machankura;
- gW-15 Invoice, un Lightning Invoice estándar;
- gW-16 Address, a través del servicio Boltz.



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

Machankura permite la interoperabilidad entre diferentes monederos Lightning. En esta demostración, enviamos bitcoins desde nuestro WhatsApp Machankura Wallet a un Wallet de Satoshi Wallet.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Para enviar, introduzca el número 1, correspondiente a la opción "ENVIAR BTC". A continuación, seleccione la opción de envío "Lightning Address", luego introduzca el Address al que se enviarán los bitcoins. Por último, seleccione la medida de valor "Sats", indique el número de satoshis que desea enviar y confirme el envío.



![wallet](assets/fr/07.webp)



![wallet](assets/fr/08.webp)



![wallet](assets/fr/09.webp)



Enhorabuena Acabas de enviar satoshis a tu destinatario.



### Recibir bitcoins



Una vez en el menú, selecciona **2**, que corresponde a la opción ''**Recibir BTC**''. El bot mostrará tu Lightning Address.



También ofrece diversas opciones, como :




- USAR BTC;
- Proyecto de ley LN (Bolt11);
- El código QR ;
- On-Chain Address.



Opción 1 ''USE BTC'' le permite recargar su cuenta con un vale Azteco.



![wallet](assets/fr/10.webp)



La opción 4 ''Una Address de un solo uso'' le permite obtener una nueva On-Chain Address de un solo uso para un mayor anonimato.



![wallet](assets/fr/11.webp)



Las demás opciones le redirigen a una página web vinculada a su Lightning Address.



![wallet](assets/fr/12.webp)



![wallet](assets/fr/13.webp)



Puede comprar :




- o el código QR de su Wallet ;



![wallet](assets/fr/14.webp)





- o generate a Lightning Invoice en esta página web.



Para obtener una Invoice exacta, indique la unidad de cuenta y la cantidad de bitcoins en esa unidad de cuenta que desea recibir.


Tras introducir el importe en esta unidad de cuenta, el sistema se encarga de convertir el equivalente en Bitcoin, y viceversa.



![wallet](assets/fr/15.webp)



![wallet](assets/fr/16.webp)



![wallet](assets/fr/17.webp)



Tenga en cuenta que también puede obtener su On-Chain Address en la página web vinculada a su cartera.



![wallet](assets/fr/18.webp)



![wallet](assets/fr/19.webp)



Además, Machankura hace posible que cualquier persona que desee enviarle bitcoins pueda hacerlo desde su sitio web, utilizando su Wallet dedicada. Todo lo que tienes que hacer es enviarles el enlace a la página web asociada a tu Address Lightning. Una vez que hayan accedido a esta página web, podrán abrir tu código QR o Invoice directamente en su Wallet.



![wallet](assets/fr/20.webp)



![wallet](assets/fr/21.webp)



https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/wallet/mobile/bitkit-a7224674-85c4-4045-9baf-37018d89550c

### Comprobación de saldo



Puede consultar el saldo de su cartera Machankura seleccionando la opción 3, que corresponde a la opción "Saldo e historial".



![wallet](assets/fr/22.webp)



¡Enhorabuena! Ya puedes utilizar Machankura para recibir y gastar bitcoins.



Si has encontrado este tutorial útil, por favor déjame un pulgar Green abajo. Muchas gracias