---
name: Blockstream Green - Watch-Only
description: Configuración de la cartera de sólo vigilancia
---
![cover](assets/cover.webp)

En este tutorial, descubrirás cómo configurar fácilmente una cartera de "sólo vigilancia" en el móvil utilizando la aplicación Blockstream Green.

## ¿Qué es un monedero Watch-Only?

Un monedero de sólo lectura, o "monedero de vigilancia", es un tipo de software diseñado para permitir al usuario observar transacciones asociadas a una o más claves públicas Bitcoin específicas, sin tener acceso a las claves privadas correspondientes.

Este tipo de aplicación sólo almacena los datos necesarios para supervisar un monedero Bitcoin, en particular para ver su saldo y el historial de transacciones, pero no tiene acceso a las claves privadas. Como resultado, es imposible gastar Bitcoins que tenga el monedero en la aplicación de solo vigilancia.

![GREEN-WATCH-ONLY](assets/fr/01.webp)

Watch-only se utiliza generalmente junto con un monedero de hardware. Esto permite almacenar las claves privadas del monedero de forma segura, en un hardware que no está conectado a Internet y que tiene una superficie de ataque muy pequeña, aislando así las claves privadas de entornos potencialmente vulnerables. La aplicación watch-only, por otro lado, almacena exclusivamente la clave pública extendida (`xpub`, `zpub`, etc.) del monedero Bitcoin. Esta clave principal no puede ser utilizada para encontrar las claves privadas asociadas, y por lo tanto no puede ser utilizada para gastar Bitcoins. Sin embargo, sí permite derivar claves públicas hijas y recibir direcciones. Gracias a que el monedero físico conoce las direcciones seguras del monedero, la aplicación watch-only puede rastrear estas transacciones en la red Bitcoin, permitiendo al usuario monitorizar su saldo y generar nuevas direcciones receptoras, sin tener que conectar su monedero físico cada vez.

En este tutorial, me gustaría presentarte una de las soluciones de monedero móvil para relojes más populares: **Blockstream Green**.

![GREEN-WATCH-ONLY](assets/fr/02.webp)

## Presentación de Blockstream Green

Blockstream Green es una aplicación informática disponible en móviles y ordenadores de sobremesa. Anteriormente conocida como Green Address, esta cartera se convirtió en un proyecto de Blockstream tras su adquisición en 2016.

Green es una aplicación muy fácil de usar, lo que la hace especialmente adecuada para principiantes. Ofrece una serie de funciones, como la gestión de hot wallets, hardware wallets y Liquid sidechain wallets.

En este tutorial, nos centraremos únicamente en la creación de una cartera sólo para relojes. Para explorar otros usos de Green, consulta nuestros otros tutoriales dedicados:

https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da
https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143
## Instalación y configuración de la aplicación Blockstream Green

El primer paso es, por supuesto, descargar la aplicación Green. Ve a tu tienda de aplicaciones:

- [Para Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [Para Apple](https://apps.apple.com/us/app/green-bitcoin-wallet/id1402243590).
![GREEN-WATCH-ONLY](assets/fr/03.webp)

Los usuarios de Android también pueden instalar la aplicación a través del archivo `.apk` [disponible en GitHub de Blockstream](https://github.com/Blockstream/green_android/releases).

![GREEN-WATCH-ONLY](assets/fr/04.webp)

Inicie la aplicación y marque la casilla "Acepto las condiciones...*".

![GREEN-WATCH-ONLY](assets/fr/05.webp)

Al abrir Green por primera vez, aparece la pantalla de inicio sin ninguna cartera configurada. Más adelante, si creas o importas carteras, aparecerán en esta interfaz. Antes de pasar a crear una cartera, te aconsejo que ajustes la configuración de la aplicación para adaptarla a tus necesidades. Haga clic en "Configuración de la aplicación".

![GREEN-WATCH-ONLY](assets/fr/06.webp)

La opción "*Privacidad mejorada*", disponible solo en Android, mejora la privacidad desactivando las capturas de pantalla y ocultando las vistas previas de las aplicaciones. También bloquea automáticamente el acceso a las aplicaciones en cuanto se bloquea el teléfono, lo que dificulta la exposición de tus datos.

![GREEN-WATCH-ONLY](assets/fr/07.webp)

Para aquellos que deseen mejorar su privacidad, la aplicación ofrece la opción de enrutar tu tráfico a través de Tor, una red que encripta todas tus conexiones y dificulta el rastreo de tus actividades. Aunque esta opción puede ralentizar ligeramente el funcionamiento de la aplicación, es muy recomendable para proteger tu privacidad, especialmente si no utilizas tu propio nodo completo.

![GREEN-WATCH-ONLY](assets/fr/08.webp)

Para los usuarios que dispongan de su propio nodo completo, Green Wallet ofrece la posibilidad de conectarse a él a través de un servidor Electrum, garantizando un control total sobre la información de la red Bitcoin y la distribución de las transacciones.

![GREEN-WATCH-ONLY](assets/fr/09.webp)

Otra función alternativa es la opción "*SPV Verification*", que permite verificar directamente determinados datos del blockchain y reducir así la necesidad de confiar en el nodo predeterminado de Blockstream, aunque este método no ofrece todas las garantías de un nodo completo.

![GREEN-WATCH-ONLY](assets/fr/10.webp)

Una vez que hayas ajustado estos parámetros a tus necesidades, pulsa el botón "*Guardar*" y reinicia la aplicación.

![GREEN-WATCH-ONLY](assets/fr/11.webp)

## Crear una cartera de vigilancia en Blockstream Green

Ya está listo para crear una cartera de sólo vigilancia. Haga clic en el botón "*Comenzar*".

![GREEN-WATCH-ONLY](assets/fr/12.webp)

Podrás elegir entre varios tipos de cartera. Para este tutorial, queremos crear una cartera solo para relojes, así que haz clic en el botón correspondiente.

![GREEN-WATCH-ONLY](assets/fr/13.webp)

Elija la opción "Firma única".

![GREEN-WATCH-ONLY](assets/fr/14.webp)

A continuación, seleccione "*Bitcoin*". Por mi parte, estoy haciendo este tutorial en una billetera testnet, pero el procedimiento sigue siendo idéntico en la mainnet.

![GREEN-WATCH-ONLY](assets/fr/15.webp)

Se le pedirá que proporcione una clave pública extendida (`xpub`, `zpub`, etc.) o un descriptor de script de salida.

![GREEN-WATCH-ONLY](assets/fr/16.webp)

Por lo tanto, tendrá que recuperar esta información del monedero que desea rastrear a través de su monedero de sólo vigilancia. La clave pública extendida no es sensible en términos de seguridad, ya que no permite acceder a las claves privadas, pero sí lo es para su confidencialidad, ya que revela todas sus claves públicas y, por tanto, todas sus transacciones de Bitcoin.

Digamos que estás usando Sparrow Wallet para gestionar tu monedero en un monedero hardware, encontrarás esta información en la sección "*Configuración*". Encontrar esta información dependerá del software de gestión de monederos que utilices, pero normalmente está en los ajustes.

![GREEN-WATCH-ONLY](assets/fr/17.webp)

Copia tu clave pública extendida e introdúcela en la aplicación Verde, después haz clic en "Conectar".

![GREEN-WATCH-ONLY](assets/fr/18.webp)

A continuación, podrá ver el saldo asociado a esta clave, así como el historial de transacciones.

![GREEN-WATCH-ONLY](assets/fr/19.webp)

Haciendo clic en "*Recibir*", puedes generar una dirección de recepción para recibir bitcoins en tu monedero hardware. Sin embargo, desaconsejaría utilizar esta opción sin comprobar primero en la pantalla del monedero hardware que tiene la clave privada asociada a la dirección generada, antes de utilizarla para bloquear bitcoins. Esta es una buena práctica a seguir.

![GREEN-WATCH-ONLY](assets/fr/20.webp)

La opción "*Billetera*" te permite introducir manualmente una clave privada para gastar fondos directamente desde tu aplicación Green. Salvo en casos muy concretos, no recomiendo utilizar esta función, ya que requiere que reveles tu clave privada en un teléfono, que es mucho más vulnerable a ataques informáticos que tu monedero de hardware.

![GREEN-WATCH-ONLY](assets/fr/21.webp)

¡Así que ya sabes cómo configurar fácilmente un monedero sólo para relojes en tu smartphone! Es una herramienta práctica para controlar un monedero en un monedero de hardware sin tener que conectarlo y desbloquearlo cada vez.

Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar verde a continuación. No dudes en compartir este artículo en tus redes sociales. ¡Muchas gracias!

También te recomiendo que eches un vistazo a este otro tutorial completo sobre la aplicación Blockstream Green para configurar un monedero caliente:

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143