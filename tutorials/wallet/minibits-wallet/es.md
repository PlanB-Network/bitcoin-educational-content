---
name: Minibits Wallet
description: Guía para Minibits Wallet
---

![cover](assets/cover.webp)


En este tutorial, te guiaré a través de la configuración de Minibits Wallet para utilizar ecash. Una potente tecnología de pago centrada en la privacidad que funciona junto con Bitcoin. Minibits es una Wallet de ecash y Lightning que permite transferencias de valor instantáneas, baratas y privadas, por lo que es ideal para transacciones cotidianas en las que la privacidad importa.


Antes de sumergirnos en los Minibits, vamos a aclarar qué es y qué no es el ecash. Mucha gente confunde ecash con la tecnología Bitcoin o Blockchain, pero son conceptos fundamentalmente diferentes.


Ecash NO es Bitcoin. No sustituye a su Bitcoin Wallet autocustodiada, sino que la complementa. Ecash NO es una Blockchain y NO vive en ninguna Ledger pública. Curiosamente, ecash NO es una tecnología nueva, de hecho es anterior a la web mundial, con conceptos desarrollados en los años 80 y 90.


Qué ES ecash: increíblemente privado (las transacciones no dejan rastro), peer-to-peer (transferencias directas sin intermediarios), y funciona como un instrumento digital al portador (si lo posees, lo controlas). Una ventaja clave es que el ecash PUEDE utilizarse sin conexión: tanto el emisor como el receptor pueden desconectarse de Internet durante las transacciones. Ecash PUEDE ser acuñado por una sola parte o por una federación de entidades de confianza, y ES una tecnología complementaria perfecta de Bitcoin, que gestiona transacciones pequeñas y frecuentes mientras Bitcoin sirve como Layer de liquidación.


Tenga en cuenta que esta configuración de Minibits representa una `solución de custodia`, lo que significa que está confiando en el operador Mint para gestionar sus fondos. Esto introduce riesgos específicos que debes entender antes de proceder.


El proyecto muestra este importante descargo de responsabilidad:


- Esta Wallet debe utilizarse únicamente con fines de investigación.
- La Wallet es una versión beta con funciones incompletas y errores conocidos y desconocidos.
- No lo utilice con grandes cantidades de ecash.
- El ecash almacenado en la Wallet es emitido por la Fábrica de la Moneda
- confías en que la ceca lo respalde con Bitcoin hasta que transfieras tus participaciones a otro Bitcoin relámpago Wallet.
- El protocolo Cashu que aplica la Wallet aún no ha sido objeto de un examen o prueba exhaustivos.


Trate los Minibits como un Wallet cotidiano, no como una cuenta de ahorros, y nunca almacene en ellos un valor significativo.


## 1️⃣ Configuración de su Wallet


Para empezar, visita el [Sitio web de Minibits](https://www.minibits.cash/), donde encontrarás opciones de descarga para las principales plataformas. Los usuarios de iOS pueden descargarla desde la [App Store](https://testflight.apple.com/join/defJQgTD), mientras que los usuarios de iOS de la UE tienen la opción adicional de instalarla desde la [Freedom Store](https://freedomstore.io/). Los usuarios de Android pueden obtener la aplicación desde [Google Play Store](https://play.google.com/store/apps/details?id=com.minibits_wallet) o descargar el archivo APK directamente desde la página [GitHub Releases](https://github.com/minibits-cash/minibits_wallet/releases).


Al instalar Minibits, verás pantallas introductorias que explican los conceptos básicos; puedes leerlas o saltártelas si ya estás familiarizado con la tecnología. Una vez que haya completado estos pasos iniciales, se le pedirá que elija entre:


- `Lo tengo, llévame a la Wallet` para los nuevos usuarios o
- `Recupera Wallet perdidos` si estás restaurando a partir de una copia de seguridad.


![image](assets/en/01.webp)

Después de completar la configuración inicial, llegará a la pantalla de inicio, que tiene varios Elements importantes a tener en cuenta. ① El icono de perfil en la esquina superior te lleva a la página de tu perfil, donde puedes acceder a tus Minibits Wallet Address y seleccionar las opciones de `recepción por lotes`. ② En el centro de la pantalla, verá las mentas que puede utilizar, con la menta Minibits seleccionada por defecto. ③ La fila de acciones de abajo ofrece opciones para enviar pagos con ecash o lightning, escanear un código QR y recibir pagos. ④ Por último, la barra de navegación inferior contiene accesos directos a la pantalla de inicio, al historial de transacciones, a los contactos y a los ajustes.


![image](assets/en/02.webp)


## 2️⃣ Administrar mentas


Por defecto, la moneda Minibits está activada al iniciar la aplicación. Sin embargo, uno de los puntos fuertes de ecash es la posibilidad de utilizar múltiples monedas para aumentar la descentralización y la seguridad. Para añadir otra acuñación, vaya a "Configuración", seleccione "Gestionar acuñaciones" y, por último, pulse "Añadir acuñación".


[Bitcoinmints.com](Bitcoinmints.com) proporciona una lista completa de las casas de la moneda disponibles con valoraciones de los usuarios para ayudarle a elegir opciones fiables. Utilizar varias casas de la moneda reduce el riesgo. Si una casa de la moneda tiene problemas, sus fondos en otras casas de la moneda siguen siendo accesibles.


![image](assets/en/04.webp)


## 3️⃣ Crear una copia de seguridad


La copia de seguridad es posiblemente el paso más crítico de todo el proceso de configuración. Para acceder a las opciones de copia de seguridad, vaya a `Configuración`-> `Copia de seguridad` Aquí encontrará dos opciones esenciales:

1. su frase seed, que contiene 12 palabras, le permite recuperar su saldo de ecash en caso de pérdida del dispositivo. Esta frase seed es tu llave maestra para todo el ecash de todas las cecas que hayas añadido. Escríbala en un soporte físico (papel o metal) y guárdela de forma segura en varias ubicaciones. Nunca almacene su frase seed digitalmente donde pueda estar en peligro. Considere visitar este [tutorial](https://planb.network/en/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270) para conocer las mejores prácticas para salvaguardar su Wallet.

2. `Wallet backup` que contiene una larga cadena de copia de seguridad.


**Atención**: Seguirá necesitando su frase seed cuando utilice esta copia de seguridad para recuperar su Wallet.


![image](assets/en/05.webp)


## 4️⃣ Crear Minibits Wallet Address


A continuación, vaya a `Contactos` en la parte inferior y personalice su `Minibits Wallet Address` pulsando `Cambiar` -> `Cambiar Wallet Address`. Introduzca su Address preferido y compruebe la disponibilidad.


![image](assets/en/07.webp)


Después de configurar tu Address, se te pedirá una pequeña "donación" para apoyar el proyecto. Aunque es opcional, te recomiendo encarecidamente que la consideres si piensas utilizar el servicio con regularidad. Los proyectos de código abierto como Minibits dependen del apoyo de la comunidad para continuar su desarrollo y mantenimiento. Incluso una pequeña contribución ayuda a asegurar la longevidad del proyecto.


![image](assets/en/08.webp)


## 5️⃣ Configuración de Nostr


Si quieres dar propinas a las personas que sigues en Nostr, puedes `Añadir tu clave npub` seleccionando `Contactos` y luego `Público`. Esto conecta tu Minibits Wallet a la red social Nostr, lo que permite dar propinas sin problemas.


También tienes la opción de `Utilizar tu propio perfil` yendo a `Configuración` y luego a `Privacidad` para importar tu propia Address y clave de Nostr. Sin embargo, ten en cuenta que al hacer esto tu Wallet dejará de comunicarse con los servidores Address de minibits.cash Nostr y LNURL, lo que desactiva las funciones de Address lightning para recibir zaps y pagos.


![image](assets/en/09.webp)


## 6️⃣ Recibir fondos


Para recibir fondos inicialmente, necesita recargar su Wallet a través de una Invoice relámpago. Este proceso es sencillo: pulse en "Recargar", introduzca el "Importe" que desea añadir, añada opcionalmente un "Memo" y, a continuación, pulse "Crear Invoice". A continuación, tendrá que pagar esta Invoice utilizando otra Wallet Lightning, esto convierte los pagos Bitcoin Lightning en tokens ecash dentro de su Wallet Minibits.


![image](assets/en/10.webp)


## 7️⃣ Enviar fondos


Ahora que ha financiado su Wallet, puede enviar fondos de dos formas distintas.


### Enviar ecash


La primera opción es enviar ecash directamente. Pulse `Enviar`, seleccione `Enviar ecash`, introduzca el `Importe` y pulse `Crear token.` Esto creará generate un código QR que puede compartir con el destinatario o hacer que lo escanee directamente con su dispositivo. El destinatario verá las fichas aparecer en su Wallet casi al instante, sin Blockchain comisiones ni retrasos en la confirmación.


![image](assets/en/11.webp)


### Pague con Lightning


La segunda opción es pagar a través de Lightning. Pulsa en "Enviar" y selecciona "Pagar con Lightning". Puedes elegir entre tus `contactos` de Nostr (si has conectado tu npub), o introducir/pegar un código de pago Lightning Address, Invoice, o LNURL usando la opción `Pegar` o `escanear`. Tras confirmar el destinatario, se te pedirá que introduzcas el importe a pagar, que añadas una nota si lo deseas y que pulses "Confirmar" seguido de "Pagar ahora" para completar la transacción Lightning.


![image](assets/en/12.webp)


## 8️⃣ Crear una conexión NWC


Otra potente función de Minibits es la posibilidad de crear conexiones `Nostr Wallet Connect (NWC)`, que permiten a otras aplicaciones solicitar pagos a su Wallet sin exponer sus claves privadas.


Para configurarlo, vaya a "Ajustes", seleccione "Nostr Wallet Connect" y pulse "Añadir conexión". Ponga a su conexión un nombre descriptivo que identifique tanto la aplicación como la cuenta de usuario asociada. Establezca un límite diario máximo razonable para controlar cuánto se puede gastar a través de esta conexión y, a continuación, pulse "Guardar" para completar la configuración.


Esta función es especialmente útil para servicios como Nostr Clients, en los que desea habilitar las propinas automáticas sin tener que aprobar manualmente cada transacción.


![image](assets/en/12.webp)


## 🎯 Conclusión


Minibits proporciona un punto de entrada accesible en el mundo del ecash, ofreciendo pagos centrados en la privacidad que complementan sus tenencias de Bitcoin. Recuerde mantener siempre copias de seguridad adecuadas, considere la posibilidad de utilizar varias casas de la moneda por redundancia y almacene únicamente las cantidades adecuadas en esta solución de custodia.


Para más información, consulta el repositorio GitHub de Minibits, la página web oficial y su canal de Telegram, donde la comunidad debate activamente sobre los avances y soluciona problemas


- [Github](https://github.com/minibits-cash/minibits_wallet)
- [Sitio web](https://www.minibits.cash/)
- [Telegrama](https://t.me/MinibitsWallet)


El ecosistema ecash aún está evolucionando, pero herramientas como Minibits están haciendo que esta potente tecnología de privacidad sea cada vez más accesible para los usuarios de a pie.