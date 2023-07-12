---
name: Blixt

description: Cartera multifunción LN
---

![presentación](activos/1.jpeg)

# Blixt BTC ⚡️ Cartera/Nodo LN

## Un potente nodo BTC/Lightning en tu bolsillo, estés donde estés

**Texto traducido por asi0 - 01/11/2022**

Me gustaría presentarles un nuevo e interesante nodo y monedero móvil de BTC/LN - Blixt. El nombre viene del sueco y significa "relámpago".

## ¿Cómo descubrí esta joya?

Tengo un nodo Umbrel LND y quería tener un plan de copia de seguridad para restaurar rápidamente mi nodo en caso de SHTF1. Así que encontré esta billetera móvil que me permite restaurar todos los fondos del nodo desde copias de seguridad SCB. Luego, empecé a probarlo con más detalle y descubrí que ES UN NODO COMPLETO EN TU PROPIO BOLSILLO.

¡No lo olvides porque es muy importante!

> Al final de este artículo, encontrarás algunos tutoriales sencillos y rápidos sobre cómo usarla y cómo conectarte a otros nodos.

Esta es una increíble aplicación en Android e iOS que te permite ejecutar un nodo BTC-LND en tu propio bolsillo. Increíble, ¿verdad? En tu propio teléfono, puedes tener un nodo BTC LN listo en menos de 10 minutos, con características ricas para usuarios experimentados, pero también para nuevos usuarios o aquellos que no son tan conocedores de la tecnología, porque el uso es simple y sin problemas.

Blixt Wallet es un proyecto de código abierto bajo la licencia MIT y se centra en un nicho de usuarios que quieren empezar con BTC/LN pero no tienen los medios para ejecutar una máquina completa o simplemente quieren ejecutar un nodo móvil.

Enlaces

Aquí hay algunos enlaces sobre esta nueva aplicación nodo/monedero:

> Página web oficial - con una bonita demo interactiva también
> Repositorio GitHub - para comprobar el estado de desarrollo y/o descargar el código fuente
>
> Grupo de soporte en Telegram - donde puedes hacer preguntas directamente al desarrollador y a la comunidad

> Descargar la aplicación Blixt para Android

> Descarga la aplicación Testflight para iOS

> Twitter feed con demos

![imagen principal](assets/2.JPEG)

# Principales características disponibles

## Nodo Neutrino

Blixt se conecta por defecto al servidor Blixt para sincronizar bloques y el índice con Neutrino (modo SPV para Simplified Payment Verification), pero el usuario también puede conectarse a su propio nodo. Sorprende ver que sincronizando un nodo SPV se tarda menos de 5 minutos, en mi caso en Android 11, en estar listo para usar el monedero completo del nodo (on-chain y LN).

**Nœud Complet Non-Custodial**

El usuario puede gestionar sus propios canales con una interfaz fácil y con suficiente información mostrada para tener una buena experiencia. En el menú desplegable en la parte superior izquierda, puedes ir a los canales Lightning para comenzar a abrir con otros nodos, como desees. No olvides activar Tor en la configuración. Es mucho mejor para la privacidad y también porque como nodo móvil, si cambias mucho tu conexión a Internet / IP de clearnet, tus pares pueden verse afectados. Con el URI del nodo Tor, siempre tendrás el mismo identificador privado sin importar tu ubicación / IP.

## Sauvegarder/Restaurer un nœud LND

Una característica poderosa, fácil de gestionar y útil es la restauración de otros nodos LND muertos, solo con la lista de 24 palabras de recuperación y el archivo channels.backup.

> Aquí tienes una guía sobre cómo restaurar los nodos muertos de Umbrel en Blixt en caso de SHTF.

El usuario también tiene la opción de guardar la copia de seguridad de los canales de Blixt en Google Drive y / o almacenamiento local en su propio móvil (para luego moverlo a un lugar seguro, fuera de tu teléfono).

El procedimiento de restauración es bastante sencillo: ingresa la semilla de 24 palabras, agrega el archivo de copia de seguridad (previamente copiado en la memoria del móvil) y haz clic en restaurar. Esto tomará un tiempo para sincronizar y escanear todos los bloques para tus transacciones pasadas. Los canales se cerrarán automáticamente y los fondos se devolverán a tu billetera onchain (ver el menú desplegable en la parte superior izquierda - onchain).

> Si anteriormente tenías canales abiertos con tu antiguo nodo detrás de Tor, primero debes activar la opción Tor (y reiniciar la aplicación) desde la configuración del menú. De esta manera, el procedimiento de cierre no fallará y / o no se utilizará la opción de cierre forzado.

No olvides hacer una copia de seguridad de tus canales LN después de abrir y / o cerrar canales. Solo lleva unos segundos estar seguro. Más tarde, podrás mover el archivo de copia de seguridad a un lugar seguro fuera de tu móvil.
Para probar tu semilla en un escenario de restauración, antes de agregar fondos, simplemente usa la misma semilla de 24 palabras (aezeed) en BlueWallet. Si la dirección BTC generada es la misma en Blixt, estás listo. No es necesario usar BlueWallet después de eso, simplemente puedes eliminar la billetera de prueba para la restauración.

Tor integrado

Una vez que lo hayas activado, la aplicación se reiniciará detrás de la red Tor. A partir de ese momento, puedes ver en la configuración del menú tu ID de nodo con una dirección onion, de modo que otros nodos puedan abrir canales hacia tu pequeño nodo móvil de Blixt. O digamos que tienes tu propio nodo en casa y quieres tener pequeños canales con tu nodo móvil de Blixt. Una combinación perfecta.

## Dunder LSP — Liquidity Service Provider o Proveedor de Servicios de Liquidez

Una característica simple y fantástica que ofrece a los nuevos usuarios la posibilidad de comenzar a aceptar BTC en la Lightning Network de inmediato, sin necesidad de depositar fondos en la billetera on-chain para luego abrir canales LN.

Para los nuevos usuarios, esta es una excelente noticia, ya que se supone que pueden comenzar desde cero, directamente en LN. Para ello, simplemente deben crear una factura (o invoice) LN desde la pantalla principal en el botón "recibir", ingresar el monto, la descripción, etc. y pagar desde otra billetera. Blixt abrirá un canal de hasta 500k sats por transacción recibida. Puedes abrir varios, si es necesario.

Un caso interesante y útil es el siguiente: supongamos que tu primer monto recibido es de 200k. Blixt abrirá un canal de 500k sats y ya tendrás 200k (menos los gastos de apertura) de tu lado, pero como aún tienes 300k de "espacio" disponible, puedes recibir más. Entonces, el próximo pago, digamos, de 100k llegará directamente por este canal, sin más gastos, y seguirás teniendo 200k de espacio para recibir más.

Pero si eliges recibir, por ejemplo, 300k para el tercer pago, se creará otro nuevo canal de 500k y se agregarán esos 300k de tu lado.

Si hay demasiadas solicitudes, el nodo de Blixt puede ajustar la capacidad del canal al abrirlo.

## Apertura automática de canal

En la configuración, el usuario puede activar esta opción y tener un servicio automatizado que abre canales con los mejores nodos y rutas a partir del saldo disponible en la billetera onchain de la aplicación Blixt. Es una función ventajosa para los nuevos usuarios que no saben con qué nodo hacer un canal y/o cómo abrir un canal LN. Es como un piloto automático para LN.

> Recuerda: esta opción se utiliza solo una vez, al crear tu nueva billetera Blixt, y está activada de forma predeterminada. Por lo tanto, si el nuevo usuario escanea el código QR on-chain en la pantalla principal y deposita sus primeros sats en esa dirección, Blixt abrirá automáticamente un canal con esos sats, con el nodo público de Blixt.

## Servicios de liquidez entrantes

**Funcionalidad dedicada a los comerciantes que necesitan más liquidez ENTRANTE, fácil de usar. Para ello, simplemente seleccione uno de los proveedores de liquidez de la lista, pague la cantidad que desee para el canal y proporcione la ID de su nodo y a partir de ahí, se abrirá un canal hacia su nodo Blixt.**

## Listas de contactos

Funcionalidad útil si desea tener una lista duradera de destinatarios con los que comerciar la mayor parte del tiempo. Esta lista puede estar compuesta por LNURL, direcciones Lightning o futuras informaciones de pago estáticas/facturas. Por el momento, esta lista no se puede guardar fuera de la aplicación, pero se planea tener una opción para exportarla.

## Enviar a una dirección Lightning

Puede enviar a cualquier dirección LN si no está en su lista de contactos. Próximamente, tal vez haya una opción para tener su propia dirección LN de tipo @blixtwallet.com.

Soporte de LNURL

Puede escanear/pagar/conectarse con LNURL, pero por el momento no funciona si el LNURL está detrás de Tor.

## Keysend

Una funcionalidad muy poderosa que pocos monederos móviles tienen. Puede enviar/enviar fondos directamente a través de un canal o apuntar a otro nodo, agregando un mensaje si es necesario. Esta funcionalidad es muy útil para mostrar mensajes en el panel de Amboss.space (aquí hay una guía sobre este panel de Amboss).

## Firma de mensajes

Herramienta muy útil para firmar mensajes con su clave privada del nodo Blixt, mensajes de autenticación de inicio de sesión, etc. Muy pocos monederos móviles tienen esta funcionalidad, prácticamente ninguno.

## Pagos multi-canales - Pagos de múltiples rutas (MPP)

Funcionalidad útil para los pagos LN, que permite dividir un pago LN en varias partes, a través de varios canales. Es una buena manera de equilibrar la liquidez en la red y mejorar la privacidad.

## Navegador Lightning

Una serie de servicios de terceros con LN, organizados en un navegador simple, accesible y al alcance del usuario. También es una buena manera de promover las empresas que aceptan BTC en LN. Esta es una funcionalidad que se desarrollará más en el futuro. Por el momento, no funciona detrás de Tor, por lo que la navegación en estas aplicaciones se realizará en claro (clearnet).

## Exploradores de registros

Es una herramienta poderosa para verificar los registros LND y el estado general de su nodo. Hay una opción para guardar el archivo de registros. Es muy útil tener estos registros a mano en caso de que necesite la ayuda del desarrollador para identificar ciertos problemas.

## Seguridad

Puedes configurar en la configuración de la aplicación, para una mayor seguridad de tu billetera/nodo, la posibilidad de iniciar la aplicación con un código PIN y/o huella digital.

## Billetera On-chain

Esta función está un poco oculta, en el menú desplegable en la parte superior izquierda. Como no se utiliza con frecuencia por un usuario de LN, no es visible en la pantalla principal. Pero no importa, puedes tenerlo en una billetera separada donde puedes administrar las direcciones y ver el registro de transacciones, importando tu semilla en Sparrow, por ejemplo. Tal vez en el futuro, Blixt wallet también incluirá una función para administrar los UTxO. Pero por ahora, utiliza ÚNICAMENTE esta billetera on-chain para abrir o cerrar canales en LN.

"Huevos de Pascua"

Sí, en la aplicación Blixt, hay algunas características ocultas, pequeñas cosas que hacen que la aplicación sea encantadora, activando acciones y respuestas divertidas/interesantes.
Pista: intenta hacer clic dos veces en el logotipo de Blixt en el menú desplegable 🙂 Te dejo descubrir el resto.

# Mini guía para casos de uso típicos con Blixt

A. Apertura de canales hacia tu mini-nodo Blixt desde tu nodo umbrel

## Para usuarios de Android:

1. Ve a la configuración de Blixt - activa Tor - reinicia la aplicación (ciérrala forzosamente si no se reinicia automáticamente).

2. Espera a que Blixt se abra detrás de Tor y sincronice los últimos bloques.

3. Ve a la configuración - haz clic en "Mostrar servicio de cebolla Tor", cópialo, es la URI de tu nodo Blixt.

4a. Ve a tu aplicación Umbrel RideTheLightning o ThunderHub (prefiero este último) - agrega un par y pega la dirección de cebolla, la URI de Blixt.

4b. Ve al panel de control de tu nodo Umbrel o RTL/TH - abre un canal y selecciona un par conocido de la lista buscando tu ID de nodo Blixt.

5. Ingresa la cantidad de sats para el canal, haz clic en abrir.

6. Espera 3 confirmaciones para tener un nuevo canal con tu "mini nodo" Blixt.

## Para usuarios de iOS:

1. Ve a la configuración de Blixt - activa Tor - reinicia la aplicación.

2. Espera a que Blixt se abra detrás de Tor y sincronice los últimos bloques.

3. Ve a tu nodo Umbrel, copia la URI de Tor o muestra el código QR.

4. En Blixt Wallet, ve a Configuración - Mostrar pares de Lightning - Agregar par y escanea o pega la URI de tu nodo Umbrel. Se agregará como un par conocido.
5. Vuelve a la aplicación Umbrel Thunderhub, abre el menú de canales y selecciona un peer de la lista desplegable de peers existentes.
6. Rellena el resto de datos para abrir el canal, haz clic en Abrir.

7. Espere 3 confirmaciones de que ha abierto este canal y ya está, ahora tiene más liquidez entrante a su lado Blixt.

## B. Abrir canales a un nodo Umbrel

Esta vez, vamos a abrir un canal DESDE tu nodo Blixt, hacia tu propio nodo Umbrel (por ejemplo), para probar la conexión y el uso de Tor. Más tarde, una vez abierto, puede equilibrar este canal empujando la mitad o la cantidad deseada hacia el lado Umbrel. Esto también se puede utilizar como una "válvula de escape" cuando su nodo Umbrel principal necesite más dinero.

1. Vaya a su nodo Umbrel y copie la URI de su nodo, o simplemente muestre el código QR de la URI de la dirección cebolla.

2. Ve a Blixt - Configuración - Lightning Peers - añade un nuevo peer.

3. Escanea el código QR de tu nodo Umbrel o pega el URI de la cebolla y tu nodo Umbrel se añadirá como peer.

4. Vuelve a la pantalla principal - cajón superior izquierdo - canales Lightning.

5. Haz clic en el signo "+" para abrir un nuevo canal y pega el URI o escanea el código QR de tu nodo Umbrel. Añade el número de saturaciones para el canal, los cargos y haz clic en abrir.

6. 6. ¡Ya está! El canal tardará 3 confirmaciones en abrirse y ... Feliz Rayo con tu propio nodo Umbrel.

C. Recibir fondos directamente en la cartera LN

Es una experiencia tan simple y agradable recibir fondos directamente en tu cartera de nodos Blixt recién abierta, sin necesidad de depositar fondos primero y abrir manualmente canales con nodos específicos.

1. Una vez que haya creado la cartera y guardado la semilla, vaya a la configuración y habilite la funcionalidad Dunder LSP.
2. Volver a la pantalla principal - haga clic en recibir, introduzca la cantidad, he probado con 200k saturación.

3. Creará una factura LN para pagar desde otro monedero LN.

4. El servicio Dunder LSP creará un canal de máximo 500k sats y empujará los fondos que enviaste (200k en nuestro caso) al lado de tu canal. De esta manera, tendrás un bonito canal listo para enviar y recibir.
5. Si quieres recibir más, los próximos pagos se recibirán en el mismo canal hasta que se alcance el límite máximo de 500k. Si no hay más "espacio" para recibir en el mismo canal, Dunder LSP creará un nuevo canal siguiendo el mismo procedimiento.
6. Haz una copia de seguridad de tus nuevos canales abiertos. Siempre hazlo después de abrir o cerrar un nuevo canal. Es muy fácil y rápido y puede evitar muchos problemas.

Este es un caso de uso perfecto para nuevos comerciantes que deseen comenzar a aceptar BTC.

Notas importantes

> Antes de comenzar a utilizar tus canales a través de Tor y si la aplicación Blixt ha estado cerrada o no sincronizada durante mucho tiempo, espera a que desaparezca el ícono de sincronización en la parte superior de la pantalla y verifica que todos tus canales estén activos. Si es así, continúa y realiza tus transacciones.
>
> Si los canales aún no están activos, vuelve a agregar la clave pública (URI) de tus pares en las opciones de Blixt - Mostrar pares. También puedes intentar actualizar esta lista, si el gossip bajo Tor encuentra a tus pares, los canales volverán a estar activos. Si no, agrégalos nuevamente, lo que impulsará la comunicación del gossip.
>
> Pero recuerda: no realices una transacción de forma ciega inmediatamente después de abrir la aplicación Blixt. Se necesita un momento para verificar si tus canales están activos y te alertará si hay algún error en la ruta de pago o falta de liquidez en la ruta.
>
> Abrir canales LN con Blixt tiene un costo, al igual que cualquier otro nodo LN que abra canales. Esto se llama "commit_fees" (o tarifas de compromiso) que funcionan como una reserva para cerrar los canales y poder pagar las tarifas de los mineros. Por lo tanto, ten en cuenta que cuando deposites en tu billetera on-chain Blixt y abras canales (ya sea que uses LSP Dunder, apertura automática de canales o manualmente), la cantidad disponible será ligeramente menor que la cantidad total con la que abriste el canal. Por esta razón, NO SE RECOMIENDA abrir canales muy pequeños como 20-50-100k sats.
>
> Además, cada transacción LN tiene pequeñas tarifas para la red. No son tarifas de Blixt, son un costo que hace que tus transacciones sean seguras y protegidas por la red. Pero son muy pequeñas, a veces incluso en milli-sats, a menudo menos del 0.5% del monto de tu transacción.
>
> Siendo un nodo LN, se desaconseja encarecidamente utilizar la misma semilla en dos dispositivos diferentes. Este procedimiento solo se puede realizar en caso de que esté en un proceso de recuperación. Cuando la billetera on-chain se genera a partir de la semilla, comenzará a sincronizar las transacciones anteriores y los saldos. Si no tienes la copia de seguridad LN de tus canales, no se iniciará el proceso de restauración completa. Así que sí, verás la misma billetera on-chain en ambos dispositivos, pero NO el saldo de LN. Y sobre todo, NO INTENTES restaurar los mismos canales LN en ambos dispositivos, ¡porque perderías todos tus fondos LN!

Ten en cuenta que cerrar los canales lleva tiempo, hasta que los fondos sean liberados. Así es como funciona LN (para obtener más información, ve aquí). Por lo tanto, en general, si tienes un cierre cooperativo (normal), tomará al menos 40 bloques hasta que los fondos sean liberados en tu billetera on-chain. Para los canales cerrados forzosamente, este bloqueo es de 144 bloques o incluso más a veces. Así que ten paciencia y no te preocupes, los fondos están seguros.

## Conclusión

Bueno, aquí tienes algunas de las principales características (¡para una billetera móvil, es mucho, ¿verdad?) entre muchas otras y pronto habrá aún más.

La experiencia con esta aplicación de billetera/nodo LN es muy agradable y fácil de usar, una aplicación muy receptiva, sin problemas importantes, solo pequeñas cosas que deben agregarse (pero no tan importantes). Aún es una aplicación joven y necesita muchas pruebas en condiciones reales. Así que no dudes en probarla e informar al desarrollador de cualquier problema que se pueda corregir o mejorar.

Tampoco olvidemos que este es un proyecto de código abierto y que su mantenimiento lo realiza un solo desarrollador, ¡que hace todo el trabajo! Así que, por favor, ayúdalo con pruebas y comentarios y lo más importante, sé paciente y repórtale con muchos detalles si encuentras problemas o si la aplicación necesita más mejoras.

Espero que disfrutes usándola. Personalmente, me encanta y me resulta muy útil (ver aquí un caso de uso donde esta billetera es una herramienta fantástica).

¡Que ₿ITCOIN esté contigo!

> Si aprecias el trabajo de DarthCoin, puedes enviar algunos satoshis a través de LN: utilizando la página de Telegram @LNtxBot DarthCoin LNURL o simplemente utilizando la dirección Lightning darthcoin@lntxbot.com
> '> LNURL1DP68GURN8GHJ7MRWW3UXYMM59E3K7MF09EMK2MRV944KUMMHDCHKCMN4WFK8QTMYV9E8G6RRDA5KULQ3NJF'

> LNURL1DP68GURN8GHJ7MRWW3UXYMM59E3K7MF09EMK2MRV944KUMMHDCHKCMN4WFK8QTMYV9E8G6RRDA5KULQ3NJF
