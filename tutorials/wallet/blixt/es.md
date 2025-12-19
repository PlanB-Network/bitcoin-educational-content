---
name: Blixt Wallet
description: ¿Cómo empezar a utilizar un potente nodo LN en tu móvil?
---
![cover](assets/cover.webp)


Esta guía está dedicada a todos aquellos nuevos usuarios que quieran empezar a usar Bitcoin Lightning Network (LN) de una manera LIBRE, OPEN SOURCE, COMPLETAMENTE NO-CUSTODIAL.


Con [Blixt Wallet](https://blixtwallet.com/), un nodo LN completo en su móvil, esté donde esté.


Si nunca ha utilizado Bitcoin Lightning Network, antes de empezar, [por favor, lea esta sencilla analogía explicativa sobre Lightning Network (LN)](https://darth-coin.github.io/beginner/LN-airport-analogy-en.html).


## ASPECTOS IMPORTANTES:



- Blixt es un nodo privado, ¡NO un nodo de enrutamiento! Tenga esto en cuenta: Esto significa que todos los canales de LN en Blixt no serán anunciados al gráfico de LN (los llamados canales privados). Esto significa que este nodo no enrutará los pagos de otros a través del nodo Blixt. Este nodo Blixt NO es para enrutar, repito. Es principalmente para poder gestionar sus propios canales LN y hacer sus pagos LN de forma privada, siempre que lo necesite. Este nodo Blixt, es necesario que esté online y sincronizado SOLO ANTES de que vayas a hacer tus transacciones. Por eso verás un icono en la parte superior que indica el estado de la sincronización. Sólo tarda unos instantes, dependiendo del tiempo que lo haya mantenido desconectado.



- Blixt esta usando LND (aezeed) como Wallet backend, asi que no intentes importar otros tipos de monederos Bitcoin en el. [Aquí tiene explicados los tipos de Wallet Mnemonic seeds](https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). Y aquí hay [una lista más extensa de todos los tipos de monederos](https://walletsrecovery.org/). Así que si usted tenía previamente un nodo LND, puede importar el seed y el backup.channels en Blixt, [como se explica en esta guía](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html).



- Al final de esta guía encontrarás una sección especial con ["trucos y consejos"](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#tips)



- Blixt enlaces importantes - verlos al final de esta guía, por favor marcarlos.


---

## Blixt - Primer contacto


Así que... la madre de Darth decidió empezar a usar LN con Blixt. Hard decisión, pero sabio. Blixt es sólo para gente inteligente y aquellos que realmente quieren aprender más, el uso profundo de LN.


![blixt](assets/en/01.webp)


Darth avisa a su madre:


"*Mamá, si empiezas a usar el Nodo Blixt LN, primero necesitarás saber qué es Lightning Network y cómo funciona, al menos a nivel básico. [Aquí he reunido una sencilla lista de recursos sobre Lightning Network](https://blixtwallet.github.io/faq#what-is-LN). Por favor, léalos primero.*"


La mamá de Darth leyó los recursos e hizo su primer paso: instalar Blixt en su flamante dispositivo Android. Blixt también está disponible para iOS y macOS (escritorio). Pero esos no son para la mamá de Darth... Sin embargo, se recomienda utilizar una versión más reciente de Android, al menos 9 o 10 para una mejor compatibilidad y experiencia. Ejecutar un nodo LN completo en un dispositivo móvil no es tarea fácil y podría ocupar algo de espacio (mínimo 600MB) y memoria.


Una vez que abras Blixt, la pantalla de "Bienvenida" te dará algunas opciones:


![blixt](assets/en/02.webp)


En la esquina superior derecha, verás 3 puntos que activan un menú con:



- "habilitar Tor" - el usuario puede empezar con la red Tor, en especial si quiere restaurar un antiguo nodo LND que estaba funcionando sólo con pares Tor.
- "Set Bitcoin node" - si el usuario quiere conectarse a su propio nodo directamente, para sincronizar los bloques a través de Neutrino, puede hacerlo directamente desde la pantalla de bienvenida. Esta opción también es buena en caso de que su conexión a Internet o Tor, no es tan estable para conectarse al nodo Bitcoin por defecto (node.blixtwallet.com).
- Pronto se añadirá el idioma allí, para que el usuario pueda empezar directamente con un idioma que le resulte cómodo. Si quieres contribuir a este proyecto de código abierto con traducciones a otros idiomas, [únete aquí](https://explore.transifex.com/blixt-Wallet/blixt-Wallet/).


### OPCIÓN A - Crear un nuevo Wallet


Si elige "crear un nuevo Wallet", será redirigido directamente a la pantalla principal del Blixt Wallet.


Esta es su "cabina" y también es la "Principal LN Wallet", así que tenga en cuenta, que sólo le mostrará el balance de su LN Wallet. El Wallet en cadena se muestra por separado (ver C).


![blixt](assets/en/03.webp)


A - Icono indicador de sincronización de bloques Blixt. Esto es lo más importante para un nodo LN: estar sincronizado con la red. Si ese icono sigue ahí funcionando, significa que tu nodo ¡NO ESTÁ LISTO! Así que ten paciencia, en especial para la primera sincronización inicial. Puede tardar hasta 6-8 min, dependiendo de tu dispositivo y conexión a internet.


Podrías hacer clic en él y ver el estado de la sincronización:


![blixt](assets/en/04.webp)


También puede hacer clic en el botón "Mostrar registro LND" (A) si desea ver y leer más detalles técnicos del registro LND, en tiempo real. Es muy útil para depurar y aprender más sobre el funcionamiento de LN.


B - Aquí puedes acceder a todos los Ajustes de Blixt, ¡y son muchos! Blixt ofrece muchas características y opciones para gestionar su nodo LN como un profesional. Todas esas opciones se explican en detalle en la "[Página de Características de Blixt](https://blixtwallet.github.io/features#blixt-options) - Menú de Opciones".


C - Aquí tienes el menú "Magic Drawer", [también explicado en detalle aquí](https://blixtwallet.github.io/features#blixt-drawer). Aquí está el "Onchain Wallet" (B), Canales Lightning (C), Contactos, icono de estado de Canales (A), Keysend (D).


![blixt](assets/en/05.webp)


D - Es el menú de ayuda, con enlaces a la página de FAQ / Guías, contacto con el desarrollador, página de Github y grupo de soporte de Telegram.


E - Indique su primer BTC Address, donde puede depositar su primera prueba Sats. ¡ESTO ES OPCIONAL! Si depositas directamente en esa Address, es abrir un canal LN hacia el Nodo Blixt. Eso significa que verás tu Sats depositado, entrando en otra transacción onchain (tx), para abrir ese canal LN. Puede comprobarlo en Blixt onchain Wallet (ver punto C), pulsando en el menú TX arriba a la derecha.


![blixt](assets/en/06.webp)


Como se puede ver en el registro de transacciones de Onchain, los pasos son muy detallados indicando a dónde van los Sats (depósito, apertura, cierre del canal).


RECOMENDACIÓN:


Tras probar varias situaciones, hemos llegado a la conclusión de que es mucho más eficaz abrir canales de entre 1 y 5 M Sats. Los canales más pequeños tienden a agotarse rápidamente y a pagar un mayor porcentaje de tasas en comparación con los canales más grandes.


F - Indica tu saldo principal de Wallet de Lightning. Este NO es tu saldo total de Wallet Blixt, representa sólo la Sats que tienes en Canales Lightning, disponible para enviar. Como se indicó antes, la Onchain Wallet es independiente. Ten en cuenta este aspecto. La Wallet onchain está separada por una razón importante: se utiliza principalmente para abrir/cerrar canales LN.


Ok así que ahora la mamá de Darth depositó un poco de Sats en ese onchain Address que se muestra en la pantalla principal. Se recomienda que cuando usted hace eso, para mantener su aplicación Blixt en línea y activa durante un tiempo, hasta que el BTC tx es tomada por los mineros en el primer bloque.


Después de eso podría tomar hasta 20-30 min hasta que esté completamente confirmado y el canal esté abierto y lo verás en el Cajón Mágico - Canales de Rayos como activo. También el pequeño punto de color en la parte superior del cajón, si es Green indicará que su canal LN está en línea y listo para ser utilizado para enviar Sats sobre LN.


El Address y el mensaje de bienvenida que se muestra desaparecerán. Ya no es necesario abrir un canal automático. También puede desactivar la opción en el menú Configuración.


Es hora de seguir adelante, probando otras funciones y opciones para abrir canales LN.


Ahora, vamos a abrir otro canal con otro nodo peer. La comunidad Blixt ha elaborado [una lista de buenos nodos para empezar a usar Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033).


**Procedimiento para abrir un canal LN en Blixt**


Esto es muy sencillo, sólo requiere unos pocos pasos y un poco de paciencia:



- Ha entrado en la lista de compañeros de la [Comunidad Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- Seleccione un nodo y haga clic en el enlace del título de su nombre, se abrirá su página Amboss
- Haga clic para mostrar el código QR del nodo URI Address


![blixt](assets/en/07.webp)


Abra Blixt y vaya al cajón superior - Canales Lightning y haga clic en el botón "+"


![blixt](assets/en/08.webp)


Ahora, haz clic en la cámara (A) para escanear el código QR de la página de Amboss y se rellenarán los datos del nodo. Añade el importe del Sats para el canal que desees y a continuación selecciona la tarifa para el tx. Puedes dejarlo en automático (B) para una confirmación más rápida o ajustarlo manualmente deslizando el botón. También puedes pulsar prolongadamente el número y editarlo a tu gusto.


¡No pongas menos de 1 sat/vbyte ! Normalmente es mejor consultar las [Mempool tarifas](https://Mempool.space/) antes de abrir un canal y seleccionar una tarifa conveniente.


Hecho, ahora sólo tienes que pulsar el botón "abrir canal" y esperar 3 confirmaciones, que suelen tardar 30 min (1 bloque aprox cada 10min).


Una vez confirmado, verás el canal activo en tu sección "Canales Lightning".


---

## Blixt - Segundo contacto


Ok, ahora tenemos un canal LN con solo liquidez OUTBOUND. Eso significa que sólo podemos ENVIAR, todavía no podemos RECIBIR Sats sobre LN.


![blixt](assets/en/09.webp)


¿Por qué? ¿Leíste las guías indicadas al principio? ¿No? Vuelve atrás y léelas. Es muy importante entender cómo funcionan los canales LN.


![blixt](assets/en/10.webp)


Como puede ver en este ejemplo, el canal abierto con el primer depósito, no tiene demasiada liquidez INBOUND ("Puede recibir") pero tiene mucha liquidez OUTBOUND ("Puede enviar").


¿Qué opciones tienes si quieres recibir más Sats que LN?



- Gaste Sats del canal existente. Sí, LN es una red de pago de Bitcoin, utilizada principalmente para gastar tu Sats de forma más rápida, barata, privada y fácil. LN NO es una forma de hodling, para eso tienes el onchain Wallet.



- Intercambia algunos Sats, de vuelta a tu Wallet onchain, utilizando un servicio de intercambio submarino. De esta manera no gastas tu Sats, sino que lo devuelves a tu propia Wallet onchain. Aquí puedes ver en detalle algunos métodos, en la [Página de Guías Blixt](https://blixtwallet.github.io/guides).



- Abrir un canal INBOUND desde cualquier proveedor de LSP. Aquí hay un vídeo de demostración sobre cómo utilizar LNBig LSP para abrir un canal de entrada. Esto significa que pagará una pequeña cuota por un canal VACÍO (por su parte) y podrá recibir más Sats en ese canal. Si usted es un comerciante que recibe más de lo que gasta, es una buena opción. También si estás comprando Sats sobre LN, usando Robosats o cualquier otro LN Exchange.



- Abra un canal Dunder, con el nodo Blixt o cualquier otro proveedor de LSP Dunder. Un canal Dunder es una forma sencilla de obtener liquidez INBOUND, pero al mismo tiempo deposita Sats en ese canal. También es bueno porque abrirá el canal con un [UTXO](https://en.Bitcoin.it/wiki/UTXO) que no es de su Wallet Blixt. Eso añade algo de privacidad. También es bueno porque, si no tienes Sats en un Wallet onchain, para abrir un canal normal LN, pero los tienes en otro LN Wallet, puedes simplemente pagar desde ese otro Wallet a través de LN la apertura y el depósito (por tu parte) de ese canal Dunder. [Más detalles de cómo funciona Dunder y cómo gestionar tu propio servidor aquí](https://github.com/hsjoberg/dunder-lsp).


![blixt](assets/en/11.webp)


Estos son los pasos para activar la apertura de un canal Dunder:



- Vaya a Configuración, en la sección "Experimentos" active la casilla de "Activar Dunder LSP".
- Una vez hecho esto, vuelve a la sección "Lightning Network" y verás que aparece la opción "Set Dunder LSP Server". Ahí, por defecto está puesto "https://dunder.blixtwallet.com" pero puedes cambiarlo por cualquier otro proveedor de Dunder LSP Address. [Aquí hay una lista de la comunidad Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033) con nodos que pueden proporcionar canales Dudner LSP para su Blixt.
- Ahora puede ir a la pantalla principal y hacer clic en el botón "Recibir". A continuación, sigue este procedimiento [explicado en esta guía](https://blixtwallet.github.io/guides#guide-lsp).


OK, así que después de confirmar el canal Dunder (tardará unos minutos) acabarás teniendo 2 canales LN: uno abierto inicialmente con piloto automático (canal A) y otro con más liquidez entrante, abierto con Dunder (canal B).


![blixt](assets/en/12.webp)


Bien, ahora ya puede enviar y recibir suficientes Sats sobre LN


¡FELIZ RELÁMPAGO Bitcoin!


---

## Blixt - Tercer contacto


Recuerda que en el capítulo uno "Primer contacto" había 2 opciones en la pantalla de bienvenida:


- [Opción A](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#option-a) - Crear un nuevo Wallet
- Opción B - Restaurar Wallet


Así que ahora vamos a discutir acerca de cómo restaurar un Blixt Wallet o cualquier otro nodo LND se estrelló. Esto es un poco más técnico, pero por favor preste atención. No es que Hard.


### OPCIÓN B - Restaurar Wallet


En el pasado escribí una guía dedicada sobre [cómo restaurar un nodo Umbrel caído](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), donde mencioné también el método de usar Blixt como proceso de restauración rápida, usando el archivo seed + channel.backup de Umbrel.


También escribí una guía sobre cómo restaurar tu nodo Blixt o migrar tu Blixt a otro dispositivo, [aquí](https://blixtwallet.github.io/faq#blixt-restore).


![blixt](assets/en/13.webp)


Pero vamos a explicar en sencillos pasos este proceso. Como puedes ver en la imagen de arriba, hay 2 cosas que debes hacer para restaurar tu nodo Blixt/LND anterior:



- la casilla superior es donde tienes que rellenar con las 24 palabras de tu seed (nodo viejo / muerto)
- abajo hay dos opciones de botón para insertar / cargar el archivo channel.backup, previamente guardado de su antiguo nodo Blixt/LND. Puede ser de un archivo local (que subirlo a su dispositivo previamente) o puede ser de una unidad de Google / iCloud ubicación remota. Blixt tiene esta opción para guardar la copia de seguridad de sus canales directamente en una unidad de Google / iCloud. Ver más detalles en [Blixt Features Page](https://blixtwallet.github.io/features#blixt-options).


Sin embargo, si antes no tenías ningún canal LN abierto, no hace falta que cargues ningún archivo channels.backup. Simplemente inserta las 24 palabras seed y pulsa el botón restaurar.


No olvides activar Tor, desde el menú superior de 3 puntos, como explicamos en la sección Opción A. Ese es el caso cuando SOLO tienes pares Tor y no puedes ser contactado por clearnet (dominio/IP). De lo contrario no es necesario.


Otra característica útil es la de establecer un nodo Bitcoin específico desde el menú superior. Por defecto sincroniza bloques desde node.blixtwallet.com (modo neutrino) pero puedes configurar cualquier otro nodo Bitcoin que proporcione sincronización neutrino.


Así que una vez que rellene esas opciones, y pulse el botón restaurar, Blixt empezará primero a sincronizar los bloques a través de Neutrino como explicamos en el capítulo Primer Contacto. Así que ten paciencia y observa el proceso de restauración en la pantalla principal, haciendo clic en el icono de sincronización.


![blixt](assets/en/14.webp)


Como puede ver en este ejemplo, muestra que los bloques Bitcoin están 100% sincronizados (A) y el proceso de recuperación está en curso (B). Eso significa que los canales LN que tenía anteriormente, serán cerrados y los fondos restaurados en su Blixt onchain Wallet.


Este proceso lleva su tiempo Así que, por favor, sea paciente e intente mantener su Blixt activo y en línea. La sincronización inicial puede tardar hasta 6-8 min y los canales de cierre pueden tardar hasta 10-15 min. Así que es mejor que tengas el dispositivo bien cargado.


Una vez iniciado este proceso, podrá comprobar en el Magic Drawer - Lightning Channels, el estado de cada uno de sus canales anteriores, mostrando que están en estado "pendiente de cerrar". Una vez cerrado cada canal, podrás ver el tx de cierre en la Wallet onchain (ver Magic Drawer - Onchain), y abrir el log del menú tx.


![blixt](assets/en/15.webp)


También será bueno para comprobar y añadir si no están allí, sus pares previamente que tenía en su antiguo nodo LN. Así que vaya al menú Configuración, hasta "Lightning Network" y entrar en la opción "Mostrar Lightning Peers".


![blixt](assets/en/16.webp)


Dentro de la sección verás los peers a los que estás conectado en ese momento y podrás añadir más, mejor añadir los que tenías canales antes. Solo tienes que ir a [Amboss page](https://amboss.space/), buscar los alias o nodeID de tus nodos peer y escanear su node URI.


![blixt](assets/en/17.webp)


Como se puede en la imagen de arriba, son 3 aspectos:


A - representa el nodo de clearnet Address URI (dominio/IP)


B - representa el nodo Tor onion Address URI (.onion)


C - es el código QR para escanear con su cámara Blixt o el botón de copiar.


Este nodo Address URI tienes que añadirlo a tu lista de compañeros. Así que tenga en cuenta que no es suficiente sólo el nombre del nodo alias o nodeID.


Ahora puedes ir a Magic Drawer (menú superior izquierdo) - Lightning Channels, y podrás ver a qué altura de bloque de vencimiento se devolverán los fondos a tu onchain Address.


![blixt](assets/en/18.webp)


Ese bloque número 764272 es cuando los fondos serán utilizables en tu Bitcoin onchain Address. Y podría tomar hasta 144 bloques desde el 1er bloque de confirmación hasta que sean liberados. [Así que compruébalo en la Mempool](https://Mempool.space/).


Y eso es todo. Sólo tiene que esperar pacientemente hasta que todos los canales se cierran y los fondos de nuevo en su onchain Wallet.


👉 **Método secreto de restauración :**


Hay otro método para restaurar su nodo Blixt LND sin ni siquiera cerrar los canales. Pero está oculto para los usuarios noob habituales, porque este método es SOLO para aquellos que saben lo que están haciendo.


En caso de que necesite migrar su nodo Blixt existente (en funcionamiento) a otro dispositivo nuevo, sin cerrar los canales LN existentes, tendrá que realizar estos pasos:



- Suponemos que ya ha guardado el Blixt Wallet seed (24 palabras aezeed)
- En el dispositivo antiguo, vaya a "Configuración" - sección de depuración - "Compactar base de datos LND". Este paso es opcional pero recomendado si quieres un tamaño más pequeño del archivo channel.db. Normalmente es bastante grande, dependiendo de la actividad de tu nodo. Esto reiniciará Blixt y compactará el tamaño del archivo db.
- Una vez reiniciado, ve a "Configuración" y cambia tu nombre de alias habitual por "Hampus". Esto activará las opciones ocultas, sólo para usuarios avanzados.
- Baja hasta la sección "Depurar" y verás una nueva opción "Exportar archivo channel.db". ¡ATENCIÓN! Una vez que realice esta exportación, el nodo Blixt LN existente se desactivará en este dispositivo antiguo y exportará toda la base de datos del nodo (channel.db) lista para ser importada a un nuevo dispositivo.
- Este archivo db se guardará en una carpeta designada de tu antiguo dispositivo (Documentos o Descargas) y desde ahí tendrás que moverlo tal cual a tu nuevo dispositivo. Puedes utilizar por ejemplo [LocalSend FOSS app](https://github.com/localsend/localsend) para transferir el archivo directamente entre dispositivos.
- En este momento su antiguo Blixt DEBE permanecer apagado. ¡NO VUELVA A ABRIRLO!
- Una vez transferido el archivo channel.db al nuevo dispositivo, inicie la nueva instalación de Blixt y elija "Restaurar Wallet" en la primera pantalla.
- En el botón donde dice "Seleccionar archivo SCB" haz una pulsación larga (¡NO un simple click!) y entonces verás la opción de seleccionar un archivo channel.db donde guardarlo localmente en el nuevo dispositivo. Si usted simplemente pulsa ese botón se utilizará por defecto un archivo SCB (con canales de cierre), no funciona para la copia de seguridad completa de canales en vivo.
- Pon las 24 palabras seed y haz clic en "Restaurar"
- Verás que Blixt empezará a sincronizarse con Neutrino. También puede ver los registros de sincronización.
- TENGA EN CUENTA Intenta mantener Blixt abierto todo el tiempo en esta fase No dejes que entre en reposo ni cierres la pantalla de la aplicación. Eso podría interrumpir la sincronización inicial y tendrás que hacerlo de nuevo. Espera pacientemente, no tardará más de unos minutos.
- Una vez finalizada la sincronización inicial de bloques, escaneará rápidamente tus direcciones Wallet anteriores y tus canales volverán a estar en línea, vivitos y coleando.
- Lamentablemente, el historial de pagos y los contactos anteriores no se pueden restaurar (todavía). Pero eso no es tan importante de todos modos.


Y ¡LISTO! Ahora tienes un nodo Blixt LN completamente restaurado. Podría funcionar también con otras copias de seguridad de LND (Umbrel, Raspiblitz etc) si previamente guardaste correctamente el fichero channel.db. Así que Blixt puede literalmente salvar cualquier nodo muerto de LND.


---

## Blixt - Cuarto Contacto


Este capítulo trata sobre la personalización y conocer mejor tu Nodo Blixt. No voy a describir todas las características disponibles, son demasiadas y ya fueron explicadas en la [Página de Características de Blixt](https://blixtwallet.github.io/features).


Pero voy a señalar algunos de los necesarios para seguir adelante utilizando su Blixt y tener una gran experiencia.


### A - Nombre (NombreDesc)


![blixt](assets/en/19.webp)


[NamDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) es un estándar para indicar el "nombre del receptor" en las facturas BOLT11.


Puede ser cualquier nombre y puede cambiarse en cualquier momento.


Esta opción es realmente útil en varios casos, cuando se quiere enviar un nombre junto con la descripción de la Invoice, para que el receptor pueda tener una pista de quién recibió esas Sats. Esto es totalmente opcional y también en la pantalla de pago, el usuario tiene que marcar la casilla que indica enviar el nombre de alias.


He aquí un ejemplo de cómo aparecería al utilizar [chat.blixtwallet.com](https://chat.blixtwallet.com/)


![blixt](assets/en/20.webp)


Este es otro ejemplo de envío a otra aplicación Wallet que soporta NameDesc:


![blixt](assets/en/21.webp)


### B - Caja de relámpagos


A partir de la nueva v0.6.9-420 [anunciada recientemente](https://github.com/hsjoberg/blixt-Wallet/releases/tag/v0.6.9-420), Blixt introdujo una nueva y potente función para Lightning Address en Blixt.


Esta nueva función es opcional, no está activada por defecto


Por el momento el LN Box por defecto es ejecutado por el servidor Blixt y ofrecer un @blixtwallet.com LN Address. Pero CUALQUIERA con un nodo público LND puede ejecutar el servidor Lightning Box y ofrecer LN Address para su propio dominio, auto-custodia.


En este momento, el servidor Blixt sólo reenvía los pagos enviados a las direcciones LN @blixtwallet.com a los usuarios Blixt que pusieron su LN Address. Los usuarios deben poner su nodo Blixt Wallet en "modo persistente" para recibir estos pagos a sus direcciones LN @blixtwallet.com.


Vea en las notas de la versión el vídeo de demostración sobre cómo configurar su LN Address en Blixt.


Este LN Address implementado en la aplicación Blixt Wallet, es como un chat sobre LN, instantáneo y divertido, también soporta [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (añadir un nombre alias a un pago). Puedes añadir en la lista de contactos todas las direcciones LN que utilizas habitualmente y tenerlas a mano para chatear. Ahora Blixt puede considerarse una aplicación de chat LN completa 😂😂.


Otra característica útil es el soporte completo para LUD-18 (que también [Stacker.News](https://stacker.news/r/DarthCoin) y otros lo soportan).


![blixt](assets/en/22.webp)


Como se puede ver en la captura de pantalla de arriba, enviando desde una cuenta de Stacker News, se muestra muy bien el logotipo + LN Address + mensaje. De la misma manera funciona para el envío de Blixt, puede adjuntar su Blixt LN Address o simplemente añadir el nombre de alias (previamente establecido en la configuración de Blixt) o incluso ambos.


Esta opción de LUD-18 podría ser útil también para servicios de suscripción, donde el usuario puede enviar un alias específico (¡NO es su alias de nodo ni su nombre real!) y en base a eso podría ser registrado o recibir de vuelta un mensaje específico o cualquier otra cosa. Adjuntar un nombre de alias ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md))+ comentario ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) a un pago LN puede tener múltiples usos


Aquí tienes el código de [Lightning Box](https://github.com/hsjoberg/lightning-box) si lo ejecutas para ti, para tu familia y amigos, en tu propio nodo.


Aquí también puede ejecutar el [servidor LSP Dunder](https://github.com/hsjoberg/dunder-lsp) para nodos móviles Blixt y ofrecer liquidez a los usuarios de Blixt si dispone de un buen nodo público LN (sólo funciona con LND).


### C - Copia de seguridad de canales LN y palabras seed


Se trata de una función muy importante


Después de abrir o cerrar un canal LN debe hacer una copia de seguridad. Puede hacerse manualmente guardando un pequeño archivo en el dispositivo local (carpeta de descargas normalmente) o usando una cuenta de Google Drive o iCloud.


![blixt](assets/en/23.webp)


Vaya a Ajustes Blixt - sección Wallet. Allí tiene las opciones para guardar todos los datos importantes para su Blixt Wallet:



- "Mostrar Mnemonic" - mostrará las 24 palabras seed para escribirlas
- "Remover Mnemonic del dispositivo" - esto es opcional y úsalo sólo si realmente quieres remover las palabras seed de tu dispositivo. Esto NO borrará tu Wallet, sólo la seed. ¡Pero tenga en cuenta ! No hay manera de recuperarlos si usted no los escribió primero.
- "Exportar copia de seguridad del canal": esta opción guardará un pequeño archivo en tu dispositivo local, normalmente en la carpeta "descargas", desde donde podrás cogerlo y moverlo fuera de tu dispositivo, para guardarlo de forma segura.
- "Verificar copia de seguridad del canal" - esta es una buena opción si utiliza Google drive o iCloud para comprobar la integridad de la copia de seguridad realizada de forma remota.
- " Google drive channel backup" - guardará el archivo de copia de seguridad en tu Google drive personal. El archivo está encriptado y se almacena en un repositorio separado de sus archivos habituales de Google. Así que no hay preocupaciones que pueden ser leídos por cualquier persona. De todos modos ese archivo es totalmente inútil sin las palabras seed, por lo que nadie puede tomar sus fondos de ese archivo solamente.


Yo recomendaría para esta sección lo siguiente:



- utilizar un gestor de contraseñas para almacenar de forma segura su seed y el archivo de copia de seguridad. KeePass o Bitwarden son muy buenos para eso y se pueden utilizar en multiplataforma y auto alojado o fuera de línea.
- HAZ EL BACKUP CADA VEZ que abras o cierres un canal. Ese archivo se actualiza con la información de los canales. No hay necesidad de hacerlo después de cada transacción que has hecho en LN. La copia de seguridad del canal no almacena esa información, sólo almacena el estado del canal.


![blixt](assets/en/24.webp)


---

## Blixt - Trucos y consejos


### CASO 1 - PROBLEMAS DE SINCRONIZACIÓN


"_Mi Blixt no se sincroniza... Mi Blixt no muestra el saldo... Mi Blixt no puede abrir canales... He intentado restaurarlo en otro dispositivo... etc_"


Todos estos problemas comienzan porque SU DISPOSITIVO NO SE SINCRONIZA CORRECTAMENTE. Por favor, comprenda este importante aspecto: Blixt es un nodo móvil LND, que utiliza Neutrino para sincronizar / leer los bloques.



- He aquí una explicación menos técnica de [Bitcoin Magazine](https://bitcoinmagazine.com/technical/why-Bitcoin-wallets-need-block-filters)
- Aquí tiene más recursos técnicos de [Bitcoin Optech](https://bitcoinops.org/en/topics/compact-block-filters/)
- He aquí cómo puede activar Neutrino en su propio nodo doméstico y servir filtros de bloques para su nodo móvil, de [Docs Lightning Engineering](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core)


RECORDATORIO: Usar Neutrino sobre clearnet es totalmente seguro, tu IP o xpub no se filtran. Sólo estás leyendo bloques de un nodo remoto con neutrino. Eso es todo. Todo el resto se hace en tu dispositivo local.


Así que NO HAY NECESIDAD de usarlo con Tor. Tor añadirá una latencia enorme en tu proceso de sincronización y hará que tu Blixt sea muy inestable. Si realmente quieres usarlo sobre Tor, asegúrate de lo que estás haciendo y de tener una buena conexión y paciencia. El mismo caso para el uso de una VPN. Ten cuidado con la latencia que te da esa VPN.


Puedes probar la latencia de un servidor de neutrinos simplemente haciéndole ping, desde un PC o desde tu móvil.


![blixt](assets/en/25.webp)


Este es un ping habitual al servidor neutrino europe.blixtwallet.com, esto muestra que la conexión es muy buena con un tiempo de respuesta de 50ms de media y un TTL de 51. El tiempo de respuesta puede variar pero no demasiado. El TTL debe ser estable.


Si estos valores son superiores a 100-150ms entonces tu proceso de sincronización se estancará o incluso peor, ¡podría causar el cierre de canales por parte de los peers! No ignore este aspecto.


Sin una sincronización adecuada, tampoco podrá ver el balance correcto o sus canales LN no estarán en línea y operativos. No importa cuantos giga ultra terra mbps tengas la velocidad de descarga NO IMPORTA. Importa el tiempo de respuesta y TTL (time to live).


Esto es como un caso general para los usuarios de LATAM. No sé lo que pasa allí, pero ustedes tienen una conexión terrible con pings de más de 200ms que pueden interrumpir cualquier sincronización.


Entonces, ¿cuál es la solución para estos usuarios desesperados?



- deja de usar Blixt con Tor. Es totalmente inútil
- puedes utilizar una VPN, pero elígela bien y controla todo el tiempo el ping. Utiliza una que esté más cerca de tu ubicación geográfica. La distancia significa más tiempo de respuesta ms, recuerda.
- selecciona sabiamente tus pares neutrinos, aquí tienes una lista de servidores neutrinos públicos bien conocidos:


```txt
For US region
btcd1.lnolymp.us | btcd2.lnolymp.us
btcd-mainnet.lightning.computer
swest.blixtwallet.com (Seattle)
node.eldamar.icu
noad.sathoarder.com
bb1.breez.technology | bb2.breez.technology
neutrino.shock.network
For EU region
europe.blixtwallet.com (Germany)
For Asia region
sg.lnolymp.us
asia.blixtwallet.com
```


Otra forma es seleccionar uno de esta lista de nodos anunciando los "filtros compactos" (BIP157 / neutrino) - [Bitnodes Page Neutrino filter](https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS). Elija uno que esté más cerca de su ubicación geográfica.


Otra forma (la mejor) es conectarse a un nodo de la comunidad local, dirigido por un amigo o grupo que los conozca, y que esté ofreciendo conexión neutrino. [Aquí están las instrucciones de cómo hacerlo](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) Su nodo no se verá afectado de ninguna manera, sólo necesitan una conexión estable y pública.


Hay una necesidad de más servidores neutrino en la región LATAM, para una mejor y rápida sincronización. Asi que por favor organizate, con tu comunidad local de Bitcoin y decide quien y donde esta corriendo un Bitcoin Core + Neutrino para tu propio uso. Con una IP pública es suficiente. Si no tienes acceso a una IP publica, puedes usar una IP VPS y hacer un tunel wireguard a tu nodo casero. De esa forma rediriges todo el trafico a tu IP VPS local, sin revelar ninguna informacion privada sobre tu nodo de origen.


### CASO 2 - NUNCA TERMINA LA SINCRONIZACIÓN


"_Mi Blixt tiene buena conexión con el servidor neutrino pero se atasca la sincronización._"


#### Servidor horario


A veces la gente utiliza varios dispositivos antiguos o no están conectados correctamente a un servidor de tiempo. Neutrino se sincroniza correctamente hasta que se alcanzan los bloques reales que no corresponden a la hora local real. Verá en los registros de Blixt LND un error diciendo que "la marca de tiempo del bloque está lejos del futuro" o algo relacionado con "la cabecera no pasa la comprobación de sanidad".


Solución rápida: ajuste la fecha y hora correctas de su dispositivo y reinicie Blixt.


#### Poco espacio en el dispositivo


A veces usando un dispositivo viejo, con poco espacio, puede llegar a un umbral límite y atascarse. De hecho, cuanto más se utiliza este nodo LND móvil, los archivos de neutrinos se hacen más grandes y también el archivo channel.db.


Solución rápida: Ve a Opciones de Blixt - sección Depuración - Selecciona "detener LND y borrar archivos de neutrinos". Se reiniciará la aplicación y comenzará una nueva sincronización. A veces esta solución rápida puede reparar también los datos dañados. Tenga en cuenta que tomará algún tiempo, entre 1 y 3 minutos para resincronizar completamente. NO se borran los fondos o canales existentes, pero sí, después de la resincronización se podría activar un nuevo escaneo de las direcciones de su Bitcoin y eso podría tomar más tiempo.


El siguiente paso es comprobar cuántos datos están todavía ocupados. Puedes verlo en Android App info - data. Si todavía es mayor de 400-500MB, puede compactar los archivos LND. Para ello vaya a Opciones Blixt - sección Depuración - Seleccione "Compactar DB LND". Reinicie la aplicación Blixt si no lo hace automáticamente. La compactación se realiza al inicio y sólo una vez. Ahora verá que los datos de Blixt están menos ocupados.


#### Modo persistente


A veces la gente no abre Blixt durante mucho tiempo, por lo que es demasiado antigua la sincronización. Pero esperan que se sincronice al instante cuando lo abren.


Por favor, tenga paciencia y mire la rueda giratoria superior. Opcionalmente puede ir a Opciones - Ver Información del Nodo y ver si está sincronizado con la cadena y sincronizado con el gráfico marcado como "true". Sin esa mención "true" no puedes usar correctamente Blixt, no puedes ver correctamente el balance, no puedes ver los canales LN online, no puedes hacer pagos.


Solución rápida: Hay una potente opción para "mantener vivo" tu nodo Blixt. Ve a Opciones - Experimentos - Selecciona "Activar Modo Persistente". Eso reiniciará tu Blixt y pondrá el servicio LND en modo persistente, es decir, siempre estará activo y mantendrá online tu sincronización, incluso si cambias a otra app o simplemente cierras Blixt (no fuerces el cierre o mates la tarea). Puedes mantenerlo así todo el día si estás en una conexión estable y necesitas usar Blixt varias veces. No consumirá demasiada batería.


### CASO 3 - QUIERO MIGRAR A OTRO DISPOSITIVO


OK sobre este escenario escribí una extensa guía en la [página de preguntas frecuentes](https://blixtwallet.github.io/faq#blixt-restore): con 2 opciones, rápida (cierre cooperativo de canales antes de la migración) y lenta (forzar el cierre de canales porque el dispositivo antiguo está muerto).


Pero quiero reiterar aquí algunos aspectos importantes y añadir un nuevo procedimiento "secreto".


RECORDATORIO:



- Haga siempre una copia de seguridad del estado de sus canales (SCB) DESPUÉS de cada vez que abra o cierre un canal. Se tarda sólo unos segundos para hacerlo.
- No guarde los archivos SCB antiguos, para no confundirse y restaurarlos. Son totalmente inútiles y podrían desencadenar un procedimiento sancionador si se los queda. Utilice siempre la última versión del fichero SCB si procede a restaurar.
- Guarda el archivo SCB (es un texto encriptado con la extensión .bin) fuera de tu dispositivo, en un lugar seguro. Puede utilizar [LocalSend](https://github.com/localsend/localsend) para mover este archivo a un PC u otro dispositivo.
- Guarde también el seed de su Blixt Wallet en un lugar seguro, por ejemplo un gestor de contraseñas offline / USB encriptado.


Método secreto: Cómo migrar el nodo Blixt sin cerrar los canales existentes. Para ello es necesario leer atentamente la sección anterior "Tercer Contacto" de esta guía sobre "Restaurar Wallet".


Este procedimiento NO ES PARA NOOBS, ¡es sólo para usuarios avanzados! Es por eso que no es ampliamente abierto y recomiendo hacerlo sólo con la asistencia de Blixt devs o mi apoyo. Por favor, no ignore este consejo.


### CASO 4 - ¿QUÉ COMPAÑEROS UTILIZAR PARA ABRIR CANALES?


Como escribí en [Blixt guides page](https://blixtwallet.github.io/guides) hay muchas maneras de abrir canales con este nodo móvil LND. Pero algunos aspectos importantes que me gustaría recordar aquí:



- abierto con nodos LSP bien conocidos y con pares avalados por la comunidad. [Vea aquí una lista](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- no abra con nodos Tor al azar. Esos no valen nada y sólo conseguirás problemas de no poder hacer pagos. No importa lo bueno que sea tu amigo "el corredor de nodos" con un nodo Tor en la jungla, nunca te dará las mejores rutas para un nodo móvil privado. No abres canales con alguien porque es tu amigo. Esto no es Facebook Abres un canal por: buenas rutas, tarifas bajas, disponibilidad.
- no hay necesidad de abrir una tonelada de mierda de canales pequeños, 2-3 o máximo 4, pero con una buena cantidad de Sats. No abras canales pequeños, son totalmente inútiles. Menores de 200k para un móvil no tienen mucha utilidad.
- ten en cuenta los PSL que ofrecen canales de entrada y canales JIT (just in time). Estos son muy útiles porque no necesitas usar ninguno de tus UTXOs, puedes pagar el canal de apertura con fondos que ya tienes en otras carteras LN, apilándolos y preparándolos para que se abra un canal mayor. Deberías usar estos canales JIT a tu favor. [He explicado en esta guía](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) más opciones de peers para nodos privados como Blixt. También [aquí en esta guía publicada en SN](https://stacker.news/items/679242/r/DarthCoin) expliqué cómo gestionar la liquidez de los nodos móviles privados.


---

## Conclusión


OK, hay muchas otras funciones increíbles que Blixt ofrece, te dejaré descubrirlas una por una y diviértete.


Esta aplicación está realmente infravalorada, sobre todo porque no está respaldada por ningún fondo de capital riesgo, está impulsada por la comunidad, construida con amor y pasión por Bitcoin y Lightning Network.


Este nodo móvil LN, Blixt es una herramienta muy poderosa en manos de muchos usuarios, si saben utilizarlo bien. Imagina que vas por el mundo con un nodo LN en tu bolsillo y nadie lo sabe.


Y no hablemos de todas las otras características ricas que vienen con, que muy pocos o ninguno otras aplicaciones Wallet podría ofrecer.


Mientras tanto, aquí tienes todos los enlaces sobre este asombroso Nodo de Rayos Bitcoin:



- [Página oficial de Blixt](https://blixtwallet.com/)
- [Página Github de Blixt](https://github.com/hsjoberg/blixt-Wallet/)
- [Página de características de Blixt](https://blixtwallet.github.io/features) - explica una por una cada característica y funcionalidad.
- [Blixt FAQ page](https://blixtwallet.github.io/faq) - Lista de preguntas y respuestas y solución de problemas de Blixt
- [Página de guías de Blixt](https://blixtwallet.github.io/guides): demos, tutoriales en vídeo, guías adicionales y casos de uso de Blixt
- Descarga: [Android Play Store](https://play.google.com/store/apps/details?id=com.blixtwallet) | [iOS](https://testflight.apple.com/join/EXvGhRzS) | [APK descarga directa](https://github.com/hsjoberg/blixt-Wallet/releases)
- [Grupo de Telegram para apoyo directo](https://t.me/blixtwallet)
- [Twitter](https://twitter.com/BlixtWallet)
- [Geyser crowdfunding page](https://geyser.fund/project/blixt) - dona Sats como quieras para apoyar el proyecto
- [LNURL Chat Blixt](https://chat.blixtwallet.com/) - chat anónimo LN
- [Blixt presentation - promo video](https://lightning.video/06fdf68f99e246a6ec6ba1470677b9e632faaad4aa0ca9773c38714b682a4ac1)
- [Blixt Girls Calendar](https://lightning.video/eeb744202ad3f14c18bf6d719970ebd9c53f0f13b79c94d299c6be623fba64b6) - vídeo promocional (puede probar el primer uso de LN)
- [Folleto A4 imprimible con los primeros pasos para utilizar Blixt, en varios idiomas](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer).
- [Blixt también ofrece una demo completamente funcional](https://blixt-Wallet-git-master-hsjoberg.vercel.app/) directamente en su sitio web o en una versión web dedicada, para tener una experiencia completa de prueba, antes de empezar a usar en el mundo real.


---
**DISCLAIMER:**


*Los desarrolladores de esta aplicación no me pagan ni me apoyan de ninguna manera. Escribí esta guía porque vi que el interés en esta aplicación Wallet está aumentando y los nuevos usuarios todavía no entienden cómo empezar con ella. También para ayudar a Hampus (el desarrollador principal) con la documentación sobre el uso de este nodo Wallet.*


*No tengo ningún otro interés en promover esta aplicación LN, aparte de impulsar la adopción de Bitcoin y LN. Esta es la única manera!*


---