---
name: Sentinel Watch-Only
description: ¿Qué es una cartera Watch-Only y cómo usarla?
---
![cover](assets/cover.webp)

---

***ADVERTENCIA:** Tras la detención de los fundadores de Samourai Wallet y la incautación de sus servidores el 24 de abril, la aplicación Sentinel sigue funcionando, pero **es obligatorio utilizar su propio Dojo** para poder acceder a la información de la blockchain y difundir transacciones.*

_Estamos siguiendo de cerca la evolución de este caso así como los desarrollos relacionados con las herramientas asociadas. Ten la seguridad de que actualizaremos este tutorial a medida que estén disponibles nuevas informaciones._

_Este tutorial se proporciona únicamente con fines educativos e informativos. No respaldamos ni alentamos el uso de estas herramientas para fines criminales. Es responsabilidad de cada usuario cumplir con las leyes en su jurisdicción._

---

*"Mantén tus claves privadas, privadas."*

En este artículo, exploramos todo lo que necesitas saber sobre las carteras watch-only. Discutimos cómo funcionan y examinamos las diferentes aplicaciones disponibles en el mercado. Finalmente, ofrecemos un tutorial detallado sobre una de las aplicaciones de cartera watch-only más populares: Sentinel.

## ¿Qué es una Cartera Watch-Only?
Una cartera watch-only, o una cartera de solo lectura, es un tipo de software diseñado para permitir al usuario observar transacciones asociadas con una o más claves públicas de Bitcoin específicas, sin tener acceso a las claves privadas correspondientes.

Este tipo de aplicación solo retiene los datos necesarios para monitorear una cartera de Bitcoin, incluyendo ver su saldo e historial de transacciones, pero no tiene acceso a las claves privadas. Por lo tanto, es imposible gastar los bitcoins mantenidos en la cartera en la aplicación watch-only.
![watch-only](assets/es/1.webp)
Generalmente, se usa watch-only en conjunto con una cartera de hardware. Esto permite el almacenamiento de las claves privadas de la cartera en "frío", en un dispositivo no conectado a internet, que tiene una superficie de ataque mínima, aislando las claves privadas de entornos potencialmente vulnerables. La aplicación watch-only, por otro lado, almacena exclusivamente la clave pública extendida (`xpub`, `zpub`, etc.) de la cartera de Bitcoin. Esta clave principal no permite el descubrimiento de las claves privadas asociadas y, por lo tanto, no permite el gasto de bitcoins. Sin embargo, permite la derivación de claves públicas secundarias y direcciones de recepción. Con el conocimiento de las direcciones de la cartera asegurada por la cartera de hardware, la aplicación watch-only puede rastrear estas transacciones en la red de Bitcoin, ofreciendo al usuario la capacidad de monitorear su saldo y generar nuevas direcciones de recepción, sin tener que conectar su cartera de hardware cada vez.

## ¿Qué Cartera Watch-Only usar?
Actualmente, la aplicación watch-only más completa es [Sentinel](https://sentinel.watch/), desarrollada por los equipos de Samourai Wallet. Abarca todas las características esenciales para una buena cartera watch-only:
- Soporte para claves extendidas, claves públicas y direcciones;
- La capacidad de organizar múltiples cuentas o carteras en colecciones;
- Generación de direcciones para recibir bitcoins en la cartera de hardware sin requerir su uso directo;
- La capacidad de construir y transmitir transacciones de forma offline;
- Opción para conectarse a su propio nodo de Bitcoin;
- Integración de Tor para una mayor privacidad.
Los únicos inconvenientes de Sentinel radican en el hecho de que la aplicación está disponible exclusivamente para Android y no admite carteras multi-firma. Por lo tanto, si posees un dispositivo Android y tu cartera es una clásica de firma única, recomiendo Sentinel.
Para aquellos que buscan rastrear una cartera multi-firma, Blue Wallet es la única aplicación que conozco que ofrece un modo watch-only para estos tipos de carteras, y es accesible tanto en Android como en iOS.

Para los usuarios de iOS que buscan una alternativa a Sentinel, [Green Wallet](https://blockstream.com/green/) o [Blue Wallet](https://bluewallet.io/watch-only/) pueden ser opciones, aunque su funcionalidad watch-only no es tan completa como la de Sentinel.
![watch-only](assets/notext/2.webp)
## ¿Cómo Usar la Cartera Watch-Only de Sentinel?
### Instalación y Configuración
Comienza instalando la aplicación Sentinel. Puedes hacerlo ya sea desde Google Play Store o utilizando el [APK disponible para descargar en el sitio web oficial](https://sentinel.watch/download/).

![watch-only](assets/notext/3.webp)

Al abrir la aplicación por primera vez, se te da la opción entre:
- `Conectar a Dojo`;
- `Conéctate al servidor de Samourai`.

Dojo, desarrollado por el equipo de Samourai, es una versión de nodo completo de Bitcoin que puede instalarse de manera independiente o añadirse en un clic a soluciones de nodo en caja como [Umbrel](https://umbrel.com/) y [RoninDojo](https://ronindojo.io/).

[**-> Descubre cómo instalar RoninDojo v2 en un Raspberry Pi.**](https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8)

Si tienes tu propio Dojo, puedes conectarlo en esta etapa. Al hacerlo, te beneficiarás del nivel más alto de privacidad al verificar la información de tus transacciones en la red Bitcoin.

![watch-only](assets/notext/4.webp)

De lo contrario, es posible optar por el servidor predeterminado de Samourai. También puedes elegir si conectarte a través de Tor o no.

![watch-only](assets/notext/5.webp)

Luego llegarás a la página principal de Sentinel.

![watch-only](assets/notext/6.webp)

Para comenzar, puedes configurar la aplicación. Haz clic en los tres pequeños puntos en la esquina superior derecha, luego en `Settings`.

![watch-only](assets/notext/7.webp)
Al seleccionar `User PIN code`, tienes la opción de establecer una contraseña para asegurar el acceso a tu billetera de solo visualización. También tienes la capacidad de cambiar la moneda de referencia para convertir tus saldos a moneda fiduciaria, o incluso ocultar los valores en moneda fiduciaria activando la opción `Hide fiat values`. Para una mayor seguridad, puedes activar `Disable Screenshots`, lo que impide cualquier captura de pantalla de tu aplicación Sentinel y así evita cualquier divulgación de información en una pantalla externa.
![watch-only](assets/notext/8.webp)

En este menú de configuración, también tienes la opción de hacer una copia de seguridad de tu Sentinel.

### Usando la Billetera de Solo Visualización
Desde la página de inicio, presiona el botón azul `NEW` para agregar una nueva clave pública extendida para rastrear. Luego tienes la opción de escanear el código QR de tu clave, o pegar directamente la clave (`xpub`, `zpub`...) seleccionando `Paste Pubkey`.

![watch-only](assets/notext/9.webp)

Generalmente, el `xpub` de tu billetera es accesible directamente a través del software de gestión de billetera que usas. Por ejemplo, si gestionas tu billetera de hardware con Sparrow, esta información se encuentra en la pestaña `Settings`, bajo la sección `Keystore`.

![watch-only](assets/notext/10.webp)

Después de ingresar la clave pública extendida en Sentinel, la aplicación te ofrece crear una nueva colección. Una colección representa un conjunto de claves públicas extendidas organizadas juntas. Esta opción te da la posibilidad no solo de listar todos tus `xpubs`, sino de clasificarlos de manera ordenada. Por ejemplo, si tienes una Samourai Wallet con múltiples cuentas (depósito, premix, postmix...), puedes reunir todas estas cuentas bajo la colección `Samourai`. Para billeteras gestionadas para tu familia, podrías crear una colección llamada `Family`.

Selecciona `Create new collection`. Luego ingresa un nombre para la clave extendida que acabas de integrar. Por ejemplo, si escaneo la cuenta de depósito de mi billetera Samourai, nombraría esta clave `Deposit`. Haz clic en `SAVE` para finalizar.

![watch-only](assets/notext/11.webp)

A continuación, asigna un nombre a esta colección y presiona el icono de validación ubicado en la parte superior derecha de la pantalla para guardar la colección. Tu colección ahora es visible en la pantalla de inicio de Sentinel.

![watch-only](assets/notext/12.webp)
Si deseas agregar otra clave pública extendida, haz clic en `NEW` nuevamente e introduce tu clave.
![watch-only](assets/notext/13.webp)
Luego, se te pedirá que elijas la colección en la que deseas integrar esta clave, o que crees una nueva. Por ejemplo, en mi caso, he configurado una colección específicamente para mi billetera Ledger.
![watch-only](assets/notext/14.webp)

Para ver las claves extendidas de una colección en detalle, simplemente haz clic en ella. Luego puedes navegar a través de las diferentes pestañas para ver el historial de transacciones.

![watch-only](assets/notext/15.webp)

Desde una colección, tocando los tres pequeños puntos en la parte superior derecha, luego en `View Unspent Outputs`, puedes acceder a una lista de UTXOs mantenidos por la billetera rastreada.

![watch-only](assets/notext/16.webp)

### Enviando y Recibiendo Bitcoins desde Sentinel
Como con cualquier buena billetera de solo visualización, Sentinel te permite generar direcciones de recepción para recibir bitcoins en la billetera rastreada. Pero Sentinel también ofrece otra característica avanzada: la creación y transmisión de una transacción de Bitcoin parcialmente firmada (PSBT). Así, la billetera que posee las claves privadas puede firmar esta transacción, que, una vez firmada, puede ser transmitida en la red Bitcoin por Sentinel. Veamos cómo hacer todo esto.

**Precaución, no se recomienda recibir bitcoins en una dirección de recepción no verificada por la billetera misma.** Si la billetera que posee las claves privadas, como una billetera de hardware, no ha confirmado explícitamente que cierta dirección está afiliada a ella, enviar bitcoins a esta dirección es una práctica arriesgada. De hecho, sin esta confirmación, no hay garantía de que la dirección pertenezca realmente a tu billetera. Por lo tanto, la funcionalidad de recepción de una billetera de solo visualización debe usarse con precaución, teniendo en cuenta que los fondos enviados podrían potencialmente perderse.

Para recibir bitcoins a través de Sentinel, selecciona la colección de interés, luego haz clic en la pestaña correspondiente a la clave pública extendida hacia la cual deseas transferir fondos.

![watch-only](assets/notext/17.webp)

Finalmente, haz clic en el icono de flecha en la parte inferior izquierda de la pantalla. Sentinel entonces genera una dirección de recepción en blanco para ti. Puedes copiarla, o escanearla usando el código QR.

![watch-only](assets/notext/18.webp)

Para generar un PSBT desde Sentinel, y así iniciar una transacción de gasto, ve a la clave extendida de la billetera desde la cual deseas realizar el pago. Tomemos, por ejemplo, mi cuenta de depósito en mi billetera Samourai. Luego haz clic en el icono de flecha ubicado en la parte inferior derecha de la pantalla.

![watch-only](assets/notext/19.webp)

Introduce todos los parámetros relacionados con tu transacción:
- Introduce la dirección del destinatario (haciendo clic en el icono del código QR, tienes la opción de escanear esta dirección);
- Especifica la cantidad a enviar a esta dirección;
- Determina las tarifas de la transacción.

Una vez que hayas completado todos los campos necesarios para tu transacción, presiona el botón `COMPOSE UNSIGNED TRANSACTION`.

![watch-only](assets/notext/20.webp)

Luego accederás al PSBT, que representa una transacción de Bitcoin construida pero no firmada, ya que Sentinel no tiene acceso a tus claves privadas. Tienes la opción de copiar esta transacción, exportarla como un archivo `.psbt`, o escanearla a través del código QR animado.

![watch-only](assets/notext/21.webp)

Luego, ve a tu billetera que tiene las claves privadas para firmar la transacción (Samourai, billetera de hardware...).

![watch-only](assets/notext/22.webp)
Una vez que la transacción esté firmada, puedes regresar a Sentinel para transmitirla. Para hacer esto, desde el menú principal, haz clic en los tres pequeños puntos en la parte superior derecha, luego en `Broadcast transaction`.
![watch-only](assets/notext/23.webp)

Tienes la opción de ingresar tu PSBT firmado de tres maneras diferentes:
- Pegándolo directamente desde tu portapapeles;
- Importándolo desde un archivo `.psbt`;
- Escaneándolo a través de un código QR.

![watch-only](assets/notext/24.webp)

Una vez que la transacción firmada esté ingresada en el marco gris, puedes hacer clic en el botón verde `BROADCAST TRANSACTION` para transmitirla en la red de Bitcoin. Sentinel te proporcionará su TXID.

![watch-only](assets/notext/25.webp)

