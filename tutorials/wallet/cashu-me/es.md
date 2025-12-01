---
name: Cashu.me
description: Guía de Cashu.me para utilizar ecash
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=LIPw1c74LBU)


*Aquí tienes un videotutorial de BTC Sessions, una guía en vídeo que te explica cómo configurar y utilizar la Bitcoin Wallet de Cashu.me, que te da acceso a transacciones Bitcoin sencillas, baratas y privadas - ¡sin necesidad de una tienda de aplicaciones!*


En este tutorial exploraremos Cashu.me, un Wallet basado en navegador para pagos privados Bitcoin usando Chaumian ecash. Antes de entrar en materia, hagamos una breve introducción sobre ecash y su funcionamiento.


## Introducción a ecash


Imagine disponer de dinero digital que funcione exactamente igual que los billetes físicos que lleva en el bolsillo: privado, instantáneo y utilizable de igual a igual sin intermediarios. Eso es lo que permite ecash: un método de pago digital que devuelve la privacidad del dinero físico al mundo digital. A diferencia de onchain-Bitcoin, que registra todas las transacciones en una Ledger pública visible para cualquiera, ecash crea tokens privados que representan un valor real de Bitcoin al tiempo que mantiene la confidencialidad de tus hábitos de gasto.


Piense en el ecash como un instrumento digital al portador almacenado en su dispositivo: si lo tiene, es de su propiedad, igual que el dinero físico. Estos tokens son emitidos por servicios de confianza llamados `Mints` que mantienen las reservas subyacentes de Bitcoin. Cuando utilizas ecash, no transmites tus transacciones a toda la red. En su lugar, intercambia fichas privadas directamente con otras personas, creando una experiencia de pago que se parece más a entregar dinero en efectivo a alguien que a realizar un pago digital tradicional.


Cashu es un protocolo Chaumian ecash libre y de código abierto construido para Bitcoin. La tecnología se basa en la investigación criptográfica pionera de David Chaum en los años 80, que utiliza "firmas ciegas" para garantizar la privacidad. Cuando recibes tokens de ecash, la casa de la moneda los firma sin saber dónde se gastarán después, una característica crucial que impide el seguimiento de las transacciones. Es importante destacar que ecash no sustituye a la Bitcoin, sino que la complementa resolviendo algunos problemas críticos que plantean los requisitos de arquitectura de la Bitcoin. Proporciona la privacidad que ofrece el dinero físico (de la que carece la transparente Ledger de Bitcoin) y permite microtransacciones instantáneas sin comisiones de Blockchain ni retrasos en la confirmación.


Ecash se integra perfectamente con la Lightning Network. Utiliza Lightning para depositar Bitcoin en una ceca (convirtiendo su valor de Bitcoin en tokens de Ecash) y para retirarlos más tarde (convirtiendo de nuevo los tokens en saldo gastable de Lightning). Juntos forman una potente combinación: Bitcoin proporciona la liquidación segura Layer, Lightning permite transacciones rápidas e interoperabilidad de red y ecash añade la privacidad Layer que hace que los pagos digitales vuelvan a ser realmente privados.


## Cashu.me


Cashu.me es una `Aplicación Web Progresiva (PWA)` que implementa el protocolo Cashu - una implementación específica de Chaumian ecash diseñada para Bitcoin. Como PWA, funciona directamente en tu navegador sin necesidad de instalación desde tiendas de aplicaciones, aunque puedes `instalarla` en tu dispositivo para facilitar el acceso. Este enfoque basado en la web garantiza una amplia compatibilidad entre sistemas operativos, al tiempo que mantiene la seguridad a través de protocolos criptográficos en lugar de restricciones de plataforma.


## características principales


Vamos a sumergirnos en las características y explorar lo que Cashu.me tiene que ofrecer:



- Chaumian ecash en Lightning**: Utiliza firmas ciegas para que las casas de moneda no puedan rastrear saldos de usuarios o historiales de transacciones
- Autocustodia de fichas**: Controlas los tokens de ecash localmente con tu frase seed
- Frase de recuperación seed**: frase de recuperación de 12 palabras para la restauración de Wallet
- Independencia de la casa de la moneda**: Funciona con múltiples casas de la moneda independientes, no estás atado a un solo proveedor
- Transacciones instantáneas y gratuitas**: En la misma ceca, los pagos finalizan en segundos sin comisiones
- Arquitectura que preserva la privacidad**: Las cecas no pueden ver quién realiza transacciones con quién
- Ecash sin conexión**: Enviar/recibir tokens a través de un protocolo de transmisión local, como NFC, código QR, Bluetooth, etc. sin conexión a Internet
- Descubra las casas de moneda de ecash a través de Nostr**: Encuentre y verifique mentas de confianza a través del protocolo Nostr
- Intercambia ecash entre monedas**: Todas las casas de moneda hablan Lightning, lo que significa que puedes transferir valor entre ellas.
- Controla a distancia tu Wallet con Nostr Wallet Connect (NWC)**: Conéctate a otras aplicaciones como Nostr Client y empieza a hacer zapping a través de NWC


El equilibrio crítico es la "confianza": mientras que usted controla los propios tokens, debe confiar en las casas de la moneda para custodiar las reservas subyacentes de Bitcoin. Como dice la documentación de Cashu:


> ...la Fábrica de la Moneda gestiona la infraestructura de Lightning y custodia los satoshis para los usuarios de ecash de la Fábrica de la Moneda. Los usuarios deben confiar en la casa de la moneda para Redeem su ecash una vez que quieren cambiar a Lightning.

- Documentación de Cashu, [Preguntas generales sobre seguridad y privacidad](https://docs.cashu.space/faq#general-safety-and-privacy-questions)


Esto convierte a ecash en una solución de custodia para el propio Bitcoin, aunque usted conserva el control total de los tokens.


## 1️⃣ Configuración inicial


① Empieza visitando [Wallet.cashu.me](https://Wallet.cashu.me) en tu navegador. Como Cashu.me es una `PWA`, no necesitas descargarla de las tiendas de aplicaciones, simplemente abre el sitio directamente en tu navegador. Para un acceso más fácil, puedes instalarlo opcionalmente en la pantalla de inicio de tu dispositivo.


para instalar la PWA, pulsa el botón de menú ⋮ de tu navegador y selecciona "Añadir a la pantalla de inicio". Una vez instalada, cierra la pestaña del navegador e inicia Cashu.me desde la pantalla de inicio de tu dispositivo. En la pantalla de bienvenida, pulsa "Siguiente" para continuar.


③ La seguridad es fundamental. Guarda tu frase seed de forma segura en un gestor de contraseñas o, mejor aún, escríbela en papel. Esta frase de recuperación de 12 palabras es tu única forma de recuperar fondos si pierdes el acceso a este dispositivo. Toque el icono 👁️ para mostrar su frase seed, escriba cuidadosamente las 12 palabras en orden y, a continuación, marque la casilla "La he escrito". Pulse "Siguiente" para continuar y marque la casilla para confirmar que acepta los "términos" en la siguiente pantalla.


![image](assets/en/01.webp)


Tras completar la configuración, tendrás que conectarte a una `Menta`. Pulsa sobre `ADD MINT` seguido de `DISCOVER MINTS` para ver las cecas recomendadas por la comunidad de Nostr. Para una verificación adicional, puedes revisar las valoraciones de las cecas en [bitcoinmints.com](bitcoinmints.com).


A continuación, pulse sobre `Haga clic para buscar caramelos de menta` para ver la lista completa. Seleccione un caramelo de menta copiando su URL, pegándola en el campo URL y dándole un nombre reconocible. Para este ejemplo, usaremos:


URL: `https://mint.minibits.cash/Bitcoin`

Nombre: `Minibits`


![image](assets/en/02.webp)


Pulse "AÑADIR MENTA" para completar el proceso. En la pantalla de confirmación, compruebe que confía en el operador de este caramelo de menta y, a continuación, pulse de nuevo "Añadir caramelo de menta". El Minibits aparecerá en tu pantalla de inicio. Una vez configurada tu Wallet, tendrás que depositar fondos en ella antes de realizar transacciones.


![image](assets/en/03.webp)


## 2️⃣ Financiación de su Wallet


Cashu.me ofrece dos métodos distintos para financiar tu Wallet. Cuando pulses "Recibir" en la pantalla de inicio, verás opciones para recibir fondos a través de "Efectivo" o a través de "Iluminación".


![image](assets/en/04.webp)


### Financiación a través de LIGHTNING


La primera opción es financiar la Wallet a través de la Invoice relámpago. seleccione una ceca si ha añadido diferentes cecas y defina el importe (Sats) que desea recibir. A continuación, pulse en `CREAR Invoice.` Ahora obtendrá un código QR que puede escanear con otro Wallet Lightning o simplemente puede `Copiar` el Invoice y pegarlo en otro Wallet para pagar y financiar su Wallet de cashu.me.


![image](assets/en/05.webp)


### Recibir ecash


El método ecash te permite recibir fichas directamente de otro Wallet ecash. Comienza tocando el botón "Recibir" y selecciona la opción "ECASH". Podrá `Pegar` o `Escanear` o utilizar `NFC` para enviar una token de Cashu desde otra Wallet. Si elige pegar, introduzca la cadena token que ha copiado de otra Wallet, el "Importe" y la "Moneda" se mostrarán automáticamente. Pulse "RECIBIR" para completar la transacción y la Sats aparecerá en su Wallet. Observe que su saldo está ahora distribuido en varias monedas. Por ejemplo, puede tener 1.000 Sats en su "Casa de la Moneda" de Minibits y otros 1.000 Sats en una "Casa de la Moneda" de Coinos. Esta separación entre diferentes monedas es un aspecto importante de la arquitectura de Cashu.


![image](assets/en/06.webp)


### Intercambio entre caramelos de menta


Si ya no confías en alguna de las casas de la moneda que has añadido, cashu.me te ofrece la posibilidad de `Intercambiar` fondos de una casa de la moneda a otra. Navega hasta la pestaña "Casas de la Moneda" y desplázate hacia abajo hasta que veas "Canje de Múltiples Casas de la Moneda". Seleccione la casa de la moneda "DE" y "A" en los menús desplegables e introduzca el importe que desea transferir. Pulse `SWAP` para mover los tokens entre las casas de la moneda. Esto se ejecutará a través de una transacción Lightning, por lo que debes dejar espacio para posibles tasas Lightning. En mi ejemplo, 1 sat fue suficiente.


![image](assets/en/07.webp)


## 3️⃣ Envío de fondos


Para enviar Sats, Cashu.me ofrece dos opciones. Enviar vía `ecash` o vía `lightning`. Echemos un vistazo a ambas opciones.


### Envío a través de Lightning


Para enviar a través de Lightning, siga estos pasos:


1. Pulse sobre `ENVIAR` en la pantalla de inicio y seleccione `Rayo`

2. La aplicación te pedirá que introduzcas un `Lightning Invoice` o `-Address`. Puedes pegar el Invoice/Address directamente, o utilizar la opción de escanear código QR para capturarlo visualmente, y luego confirmar con `ENTRAR`

3. Seleccione la Casa de la Moneda desde la que desea pagar utilizando el campo desplegable y pulse "PAGAR" para confirmar. **Nota**: también existe la opción de utilizar `Multinut` en `Configuración` -> `Experimental`, que le permite pagar facturas de varias casas de la moneda a la vez.

4. Una vez completado con éxito, verá la confirmación del pago y el importe deducido de su saldo.


![image](assets/en/08.webp)


### Envío a través de ecash


El envío de ecash es igualmente sencillo.


1. Pulse sobre `ENVIAR` y esta vez seleccione la opción `ECASH`.

2. `Seleccione una ceca` e introduzca el `Importe` que desea enviar en Sats y pulse `ENVIAR` para confirmar

3. Esto crea un `Código QR Animado` que puedes personalizar ajustando los parámetros de Velocidad y Tamaño. Cualquiera puede escanear este Código QR para Redeem la Sats inmediatamente, o puede pulsar COPIAR para enviar la cadena token a otra persona a través de canales alternativos como Bluetooth, NFC o mensajería estándar.

4. Abro otra Wallet. Pega desde el portapapeles y selecciona `Recibir ecash` en la otra Wallet.


![image](assets/en/09.webp)


## 4️⃣ Características adicionales


Más allá de la funcionalidad básica de envío y recepción, Cashu.me ofrece potentes funciones adicionales que mejoran su experiencia Bitcoin dentro del ecosistema Nostr.


### Nostr Wallet Conectar


Nostr Wallet Connect (`NWC`) transforma la forma de interactuar con las aplicaciones de Nostr creando una conexión perfecta entre tu Wallet y las aplicaciones sociales. Este protocolo permite a aplicaciones como [Damus](https://damus.io/) o [Primal](https://primal.net/home) solicitar pagos directamente a través de los relés de Nostr sin necesidad de salir de la aplicación.


Para configurar `NWC` en Cashu.me:


1. Vaya a `Configuración` en el menú hamburguesa de la parte superior izquierda

2. Desplácese hasta la sección "NOSTR Wallet CONNECT" y pulse el botón "Activar"

3. A continuación, fijará una asignación para establecer la cantidad máxima que las aplicaciones pueden gastar de su Wallet.

4. Una vez configurada, puede copiar la cadena de conexión y pegarla en cualquier cliente Nostr que admita `NWC`, lo que permite la funcionalidad instantánea de zapping y tipping.


![image](assets/en/10.webp)


### Rayo Address vía npub.cash


Cashu.me se integra con [npub.cash](https://npub.cash/) para proporcionarte un Address Lightning que funciona perfectamente con el protocolo Nostr. Aquí puedes registrarte y reclamar tu nombre de usuario proporcionando tu Nostr `nsec`, que cuesta 5.000 Sats y apoya el proyecto npub.cash, o puedes usar cualquier clave pública de Nostr (`npub`) sin registrarte.


En primer lugar, vaya a `Configuración` y pulse `Activar` Rayo Address con npub.cash. Esto generate un Address npub.cash utilizando una cadena `npub` derivada de su Wallet seed frase por defecto.


También puedes visitar [esta página web](https://npub.cash/username) para solicitar un nombre de usuario personalizado utilizando tu propio Nostr `nsec`, lo que te proporcionará un Lightning Address personalizado como username@npub.cash.


![image](assets/en/11.webp)


## 🎯 Conclusión


Cashu.me ofrece pagos privados Bitcoin que funcionan como dinero físico, al instante y entre iguales, sin exponer tu historial de transacciones. Personalmente, aprecio su arquitectura PWA porque funciona sin las restricciones de las tiendas de aplicaciones. Al combinar la seguridad de Bitcoin, la velocidad de Lightning y la privacidad de ecash, Wallet ofrece casos de uso que podrían mejorar la adopción cotidiana de Bitcoin.


Aunque usted tiene pleno control sobre sus tokens ecash a través de la autocustodia, recuerde que las casas de moneda actúan como terceros de confianza que mantienen las reservas subyacentes de Bitcoin. La posibilidad de utilizar varias casas de la moneda e intercambiar entre ellas proporciona flexibilidad al tiempo que mantiene la privacidad.


Gracias a características como las direcciones NWC y npub.cash, Cashu.me es una opción Wallet atractiva para los clientes sociales que valoran la privacidad y la soberanía por encima de las restricciones políticas de las grandes tecnológicas.


## 📚 Recursos


[https://github.com/cashubtc/cashu.me](https://github.com/cashubtc/cashu.me)


[https://github.com/cashubtc](https://github.com/cashubtc)


[https://github.com/cashubtc/awesome-cashu](https://github.com/cashubtc/awesome-cashu)


[https://cashu.space/](https://cashu.space/)