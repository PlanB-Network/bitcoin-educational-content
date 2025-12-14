---
name: Zeus Embedded - Avanzado
description: Billetera Lightning auto-custodiada multinodo
---

![Zeus](assets/cover.webp)


## Introducción a ZEUS Wallet


ZEUS es una aplicación móvil de Bitcoin Wallet y gestión de nodos con todas las funcionalidades de una Bitcoin Lightning Wallet que simplifica los pagos de Bitcoin, ofrece a los usuarios un control completo de sus finanzas y permite a los usuarios más avanzados gestionar sus nodos Lightning desde la palma de su mano.


### ¿Para quién es ZEUS?

Actualmente ZEUS está destinado a personas que ejecutan sus propios nodos domésticos / comerciales de [Lightning Network Daemon (LND)](https://lightning.engineering/) o [Core Lightning (CLN)](https://blockstream.com/lightning/) y los gestionan de forma remota a través de Zeus.


Los comerciantes que usan [BTCPay](https://btcpayserver.org/), [LNBits](https://lnbits.com/) o [Alby](https://getalby.com/) (o cualquier otra cuenta de LNDhub) también pueden conectarse, usar y administrar sus nodos / cuentas desde ZEUS.


[A partir de la v0.8](https://blog.zeusln.com/zeus-v0-8-0-open-beta/), ZEUS comenzará a atender a los usuarios promedio que solo desean una forma sencilla de realizar pagos de bitcoin rápidos y económicos desde su dispositivo móvil, mediante un [nodo Lightning móvil integrado](https://docs.zeusln.app/category/embedded-node) con un [Proveedor de Servicios Lightning (LSP)](https://docs.zeusln.app/lsp/intro) incorporado.


### Recursos importantes de Zeus:


- Página oficial de Zeus - [https://zeusln.app/](https://zeusln.app/)
- Documentación Zeus - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Repositorio de Zeus en Github](https://github.com/ZeusLN/zeus)
- [Grupo de soporte de Zeus en Telegram](https://t.me/ZeusLN)
- [Zeus en NOSTR](https://iris.to/zeus@zeusln.app)
- [Anuncios en el blog de Zeus](https://blog.zeusln.com)


### Características de Zeus

#### Características generales:


- Autocustodia, sólo Bitcoin y Lightning Wallet
- Sin gastos de tramitación, sin CSC
- Código abierto (APGLv3)
- Compatible con varios nodos/cuentas (puede gestionar su(s) propio(s) nodo(s) doméstico(s), ejecutar un nodo LND integrado y conectarse a varias cuentas LNDhub)
- Menú de actividades fácil de usar
- Encriptación PIN o passphrase, Modo privacidad: oculta tus datos confidenciales
- Agenda de contactos, multitemática, multilingüe


#### Características técnicas


- Conectarse a través de Tor
- Compatibilidad total con LNURL (pago, retirada, autenticación, canal), envío a direcciones Lightning
- Gestión detallada de canales de iluminación, compatibilidad con MPP/AMP, Keysend, gestión de tarifas de encaminamiento
- Ayudas Replace-by-fee (RBF) e Hijo-paga-por-padre (CPFP)
- Pagos y solicitudes NFC, Firma y verificación de mensajes
- Soporte SegWit y Taproot
- Canales simples Taproot
- Direcciones de rayos autocustodiados (@zeuspay.com)
- Punto de venta de Square (próximamente PoS abierto)


### Guías y tutoriales en vídeo

Para poder utilizar Zeus y gestionar los canales Lightning, la liquidez, las comisiones, etc., es mejor leer primero algunas guías importantes sobre Lightning Network.


#### Guías:


- [LND - Documentación de Lightning Network Daemon](https://docs.lightning.engineering/)
- [CLN - Documentación de Core Lightning](https://lightning.readthedocs.io/index.html)
- [Guía de Lightning para principiantes](https://bitcoiner.guide/lightning/) – por Bitcoin Q&A
- [Gestión de nodos Lightning](https://www.lightningnode.info/) – por openoms
- [La Red Lightning y la analogía del aeropuerto](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Gestión de la liquidez de nodos Lightning](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Mantenimiento de nodos Lightning](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### Videotutorial de BTC Sessions


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## Guía práctica para empezar a usar Zeus LN embedded node en tu dispositivo móvil


![Image](assets/en/01.webp)


Dedico esta guía a todos aquellos nuevos usuarios de Lightning Network (LN) que quieran comenzar una nueva andadura soberana utilizando un nodo de autocustodia Wallet en sus dispositivos móviles.


Consideremos que ya pasas por toda esa plétora de carteras LN de custodia, pero aún no estás preparado para empezar a gestionar un nodo LN de enrutamiento PÚBLICO, sólo quieres apilar más Sats sobre LN de forma más autocustodiada y hacer tus pagos regulares sobre LN.


Aquí llega Zeus, comenzando con la [versión v0.8.0 anunciada en su blog](https://blog.zeusln.com/new-release-zeus-v0-8-0/), que ahora ofrece un nodo LND integrado en la aplicación. Hasta ahora Zeus era una aplicación de gestión de nodos remotos + cuentas de LNDhub. ¡Pero ahora… el nodo está en el teléfono!


![Image](assets/en/02.webp)


### Resumen rápido de las principales características de Zeus Node:



- **Nodo LND privado** - Esto significa que este nodo NO hará enrutamiento público de otros pagos a través de su nodo. El nodo y los canales no se anuncian (privados, no visibles en el gráfico público LN). Para recibir y realizar pagos se hará a través de sus pares LSP conectados. RECUERDA: ¡Zeus Embedded Node NO hará enrutamiento público!
- **Servicio LND persistente** - el usuario puede activar esta función y mantener el servicio LND activo continuamente como cualquier nodo LN normal. La aplicación no tiene que estar abierta, el servicio persistente mantendrá toda la comunicación en línea.
-   **Filtros de bloques Neutrino** - la sincronización de bloques se realiza mediante [filtros de bloques y el protocolo Neutrino](https://bitcoinops.org/en/topics/compact-block-filters/) (sin proporcionar información sobre los fondos en cadena de nuestros usuarios). Recordatorio: para conexiones a internet de alta latencia / lentas, esta sincronización de bloques basada en Neutrino a veces puede fallar. Intentar cambiar a un servidor Neutrino cercano podría ayudar a restaurar la sincronización. ¡Sin esta sincronización, su nodo LND no podría iniciarse!
- **Canales Taproot simples** - Al cerrar estos canales, los usuarios incurren en menos gastos y se les da más privacidad, ya que parecen como cualquier otro gasto Taproot al examinar su huella On-Chain.
- **LSP integrado** - Olympus es el nuevo nodo LSP para Zeus. Los usuarios pueden volver a recibir Sats a través de LN directamente, sin tener que configurar previamente canales LN. Simplemente tendrán que crear una LN Invoice y pagar desde cualquier otra LN Wallet, con el servicio de canales 0-conf de Zeus. Más información sobre Zeus LSP aquí. El LSP también proporciona privacidad añadida a nuestros usuarios, proporcionándoles facturas envueltas que ocultan las claves públicas de sus nodos a los pagadores.
- **Libreta de contactos** - puedes guardar contactos manualmente o importarlos desde NOSTR, para enviar pagos fácilmente a tus destinos habituales.
- Soporte completo para LNURL, LN Address enviar y recibir - ahora puedes configurar tu propio LN Address autocustodiado con @zeuspay.com. Recordatorio: También puede utilizar Zeus para LN-auth en los sitios donde se puede iniciar sesión con una autenticación LN. Es muy práctico.
- **Punto de Venta** - Ahora los usuarios comerciantes pueden configurar sus propios artículos de producto y vender directamente desde Zeus, con PoS integrado. Por el momento contiene las necesidades básicas, pero en el futuro contendrá características ampliadas.
- **LND logs** - el usuario puede leer en tiempo real los logs del servicio LND y utilizarlos para depurar posibles problemas (principalmente para malas conexiones)
- **Copias de Seguridad Automatizadas** - los canales del nodo LN son automáticamente respaldados en el servidor Olympus. Esta copia de seguridad automatizada se codifica con su nodo Wallet seed (sin el seed es totalmente inútil). El usuario también puede exportar manualmente un SCB (copia de seguridad estática de los canales) para una recuperación en caso de desastre.


### Cómo embarcarse en el nodo Zeus LN (LND integrado)


En esta guía hablaré únicamente sobre el nodo LND integrado, y no sobre las otras formas de usar esta magnífica aplicación (gestión de nodos remotos y cuentas LNDhub). Para los otros tipos de conexiones, por favor consulte la [página de documentación de Zeus](https://docs.zeusln.app/category/getting-started), que está muy bien explicada y no necesita una guía dedicada.


#### PASO 1 - CONFIGURACIÓN INICIAL


Debido al hecho de que Zeus es un nodo completo LND voy a tener algunas recomendaciones iniciales:



- No utilice un dispositivo antiguo, ya que podría afectar al uso de esta potente aplicación. Especialmente en el período de sincronización la aplicación podría utilizar intensivamente la CPU y la RAM. La falta de estos podría incluso hacer imposible el uso de la aplicación Zeus.
- Utilice al menos Android 11 como sistema operativo móvil y actualizado tanto como sea posible. Para iOS lo mismo, trate de usar una versión mucho más alta del sistema operativo.
- Necesitará al menos 1 GB de espacio en disco para almacenar los datos. Con el tiempo podría crecer más, pero hay una funcionalidad para compactar la base de datos a un nivel de MBs.
- NO hay necesidad de usar Zeus con Tor o el servicio Orbot. Por favor, no compliques las cosas más de lo necesario. Tor en este caso no te ofrecerá más privacidad sino que sólo empeorará las cosas para la sincronización inicial. También ten cuidado con qué VPNs estás usando y comprueba la latencia de la conexión hacia los servidores de neutrino. Ten en cuenta que los filtros de bloqueo de Neutrino no filtran ni rastrean la identidad de tu dispositivo, sólo sirven bloqueos. El tráfico LN también está detrás de un LSP con canales privados por lo que muy poca información sale, no hay razón para asustarse por la privacidad.
-   Tenga paciencia con la sincronización inicial, podría tardar varios minutos. Intente estar conectado a una conexión de internet de banda ancha con buena latencia. Si ejecuta su propio nodo de Bitcoin, [puede activar el servicio neutrino](https://docs.lightning.engineering/lightning-network-tools/lnd/enable-neutrino-mode-in-bitcoin-core) y conectar su Zeus a su propio nodo, incluso utilizando la LAN interna, para tener la máxima velocidad.


Una vez que hayas configurado el tipo de conexión "Nodo incrustado", la aplicación empezará a sincronizarse durante un rato. Espera pacientemente a que termine esa parte y luego entra en la página principal de Configuración.


![Image](assets/en/03.webp)


Brevemente, vamos a sumergirnos en cada una de las secciones de Configuración y entender algunas de las principales características, antes de empezar a utilizar Zeus:


**A - AJUSTES**


Esta es una sección con ajustes generales para toda la aplicación


**1 - Lightning Service Provider (LSP)**


Aquí se presentan dos servicios LSP:



- _Canales justo a tiempo_ - cuando no tengas ningún canal abierto o liquidez entrante disponible, si el servicio está activado abrirá un canal sobre la marcha para ti. Esta opción puede desactivarse si no desea abrir más canales de este tipo.
- _Solicitar canales por adelantado_ - puedes comprar canales entrantes del LSP de Olympus directamente en la app con múltiples opciones e importes (para entrantes y salientes).


El LSP ayuda a conectar a los usuarios con la red Lightning abriendo canales de pago a sus nodos. [Lea más sobre LSP aquí](https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992). ZEUS tiene un nuevo LSP integrado llamado [OLYMPUS by ZEUS](https://mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581), que está disponible para todos los usuarios que utilizan el nuevo nodo integrado.


En esta sección, por defecto es el LSP de Olympus (https://0conf.lnolymp.us), pero próximamente también se podrá configurar otro LSP 0conf que soporte este protocolo.


ten en cuenta:_

cuando abres un canal con Olympus LSP utilizando las facturas LN envueltas, ¡también obtienes una liquidez de entrada de 100k! Esta es una muy buena opción en caso de que necesite recibir inmediatamente más Sats._

ejemplo: depositas 400k Sats para abrir un canal LSP, entonces el LSP está abriendo un canal de 500k Sats de capacidad hacia tu nodo Zeus y empuja los 400k Sats que depositas hacia tu lado

"Liquidez entrante" = más "espacio" en tu canal para recibir


En el futuro esperamos poder tener muchos otros LSP que puedan integrarse en Zeus y utilizar alternativamente cada uno de ellos. Es sólo cuestión de tiempo que los nuevos LSP adopten un estándar abierto para este tipo de canales 0conf.


Si no desea abrir nuevos canales "sobre la marcha", puede desactivar esta opción.


En esta misma sección, también tienes la opción de elegir "solicitar Canales Simples Taproot" cuando el LSP abra un canal hacia tu nodo Zeus. Estos Canales Simples Taproot ofrecen una mejor privacidad On-Chain y menores tasas en el cierre del canal. Sólo hay dos razones por las que no querrías usarlos:



- Son nuevos, y aún puede haber fallos en LND al utilizarlos.
- Tu contraparte no los admite. Incluso los nodos LND tienen que optar explícitamente por ellos, por ahora.


**2 - Opciones de pago**


Esta función le ofrecerá la posibilidad de establecer sus propias tarifas preferidas para los pagos, a través de LN u onchain. También proporcionará la opción de aumentar o disminuir el tiempo de espera para sus facturas.


Si algunos de tus pagos LN fallan, podrías aumentar la tasa para encontrar una ruta mejor. Además, si realiza txs en cadena, puede establecer una tasa específica para que su tx no acabe atascado en la Mempool durante mucho tiempo, en caso de que las tasas sean elevadas.


**3 - Configuración de las facturas**


En esta sección hay algunas opciones para generate facturas:



- Configure una nota estándar para que se muestre en la Invoice usted generate
- Tiempo de expiración en segundos, en caso de que desee un tiempo específico, más largo o más corto para que su Invoice sea pagado
- Incluir pistas de ruta: proporciona información para encontrar canales no publicitados o privados. Esto permite enrutar los pagos a nodos que no son visibles públicamente en la red. Una sugerencia de ruta proporciona una ruta parcial entre el nodo privado del receptor y un nodo público. Esta sugerencia de ruta se incluye en el Invoice generado por el receptor y proporcionado al pagador. Sugiero que esté activada por defecto, de lo contrario los pagos entrantes podrían fallar (no se encuentra la ruta).
- AMP Invoice - Atomic Multi-path Payments son un nuevo tipo de pagos Lightning implementados por LND que permiten recibir Sats sin un Invoice específico, usando [keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend). Es prácticamente un código de pago estático. [Más información aquí](https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- Mostrar campo personalizado en la preimagen - utilice esta opción sólo en casos muy concretos en los que realmente desee utilizar campos personalizados en la preimagen. [Más información aquí](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


Otra opción en esta sección es cómo establecer el tipo de onchain Address que desea utilizar: SegWit anidado, SegWit, Taproot.


![Image](assets/en/04.webp)


Pulsa el botón de la rueda superior y aparecerá una pantalla emergente para elegir el tipo de Address deseado. Una vez que lo hayas configurado, la próxima vez que pulses el botón de recepción de onchain, se generate el tipo de Address seleccionado. Puedes cambiarlo en cualquier momento.


**4 - Configuración de canales**


En esta sección se preajustan algunas características de los canales de apertura como:



- número de confirmaciones
- Anunciar canal (por defecto está desactivado), eso significa que serán canales no anunciados
- Canales simples Taproot
- Mostrar botón de compra de canales


**5 - Ajustes de privacidad**


Aquí encontrarás algunos ajustes básicos para añadir más privacidad usando la aplicación Zeus:



- Block explorer para abrir detalles de tx (Mempool.space, blockstream.info o personalizados)
- Leer portapapeles: activa/desactiva si quieres que Zeus lea el portapapeles de tu dispositivo
- Modo Lurker - activar/desactivar si quieres ocultar información sensible específica de tu aplicación Zeus. Es una buena opción cuando haces demos o capturas de pantalla.
- Sugerencia de tasas Mempool - active esta opción si desea utilizar los niveles de tasas recomendados en [Mempool.space](https://Mempool.space/)


**6 - Seguridad**


Esta sección sólo tiene dos opciones para proteger la aplicación al abrirla: establecer una contraseña o un PIN.


Una vez que haya establecido un PIN para abrir la aplicación, también podrá establecer un "PIN de coacción". Este PIN secreto adicional se utilizará SÓLO en caso de situación de coacción, si usted está amenazado. Si usted pone este PIN, la configuración será todo WIPE OUT. Así que mejor mantenga actualizadas sus copias de seguridad. Las copias de seguridad automáticas están activadas por defecto, pero es bueno tener sus propias copias de seguridad también, fuera del dispositivo.


**7 - Moneda**


Activar o desactivar la opción de mostrar una conversión de moneda fiduciaria en el uso de la aplicación Zeus. Actualmente es compatible con más de 30 monedas fiduciarias en todo el mundo.


**8 - Lengua**


Puedes cambiar entre varios idiomas de traducción, revisados por la comunidad Zeus con hablantes nativos.


**9 - Pantalla**


En esta sección puedes personalizar la pantalla de tu Zeus, seleccionando varios temas de color, pantalla por defecto (teclado o balanza), mostrar tu alias de nodo, activar botones grandes del teclado, mostrar más decimales.


**10 - Punto de venta**


Esta es una característica especial para activar / desactivar un sistema PoS integrado en Zeus. Usted podría ejecutar un PoS independiente o vinculado a un sistema PoS Square. Actualmente está soportando funcionalidades básicas como un PoS, pero suficiente para un buen comienzo y podría ayudar a los pequeños comerciantes (bares / restaurantes, tiendas de comestibles) para empezar a aceptar BTC de una manera nativa.


Dentro de esta configuración, encontrará varias opciones para configurar su PoS:



- Tipo de pago de confirmación: Sólo LN, 0-conf, 1-conf
- Activar / desactivar las propinas para los empleados que operan el TPV
- Mostrar / ocultar teclado
- Porcentaje de impuestos a aplicar en el billete
- Crear productos y categorías de productos
- Un simple listado de todas las ventas


Aquí hay un video de demostración en vivo de cómo utilizar Zeus PoS:


**B - Copia de seguridad Wallet**


El nodo incrustado en ZEUS está basado en LND y utiliza el [formato aezeed seed](https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md). Esto es diferente del típico [formato BIP39](https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki) que se ve en la mayoría de los monederos Bitcoin, aunque pueda parecer similar. Aezeed incluye algunos datos extra incluyendo la fecha de nacimiento de la Wallet que ayudará a que los re-escaneados durante la recuperación se realicen de forma más eficiente.


El formato de clave aezeed debería ser compatible con los siguientes monederos móviles: Blixt, BlueWallet y Breez. ¡Tenga en cuenta que la seed por sí sola será insuficiente para recuperar todos sus saldos si tiene canales abiertos o pendientes de cierre !


Más información sobre el proceso de copia de seguridad y restauración en [Zeus Docs page](https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery).


CONSEJO DE POTENCIA: Cuando guardes tu seed, por favor guarda también la pubkey del nodo A veces es bueno tenerla a mano, junto con tu seed y SCB (Static Channels Backup) en caso de que necesites verificar la recuperación.


SCB es necesario sólo si tienes canales LN abiertos. En caso de que sólo tenga fondos onchain, no es necesario.


Si ves que después de mucho tiempo sigue sin mostrar el historial de txs antiguos, ve a Nodo incrustado - Peers y desactiva la opción de usar la lista de peers seleccionados (por defecto es el btcd.lnolymp.us). Eso activará un reinicio y se conectará al primer nodo neutrino disponible con un mejor tiempo de respuesta. O utiliza los peers de neutrino que se mencionan a continuación.


Si quieres ver más opciones de recuperación para un nodo LND, [por favor lee mi guía anterior](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), donde puedes encontrar los pasos de cómo importar un seed aezeed a Sparrow Wallet u otros métodos.


**C - Nodo integrado**


En esta sección encontraremos algunas herramientas básicas para gestionar el nodo integrado:



- disaster Recovery_ - Copias de seguridad automatizadas y manuales para los canales LN. Por favor, lea más cómo utilizar esta función en la página Zeus Docs.
- express Graph Sync_ - Zeus app descargará el gráfico de datos de cotilleo LN desde un servidor dedicado, para una sincronización más rápida y mejor, ofreciendo las mejores rutas de pago. Usted puede elegir también para borrar los datos de gráficos anteriores en el arranque.
- peers_ - sección para gestionar los neutrino peers y 0-conf peers. Si tiene problemas con la sincronización inicial, los canales no vienen en línea, es porque su dispositivo tiene alta latencia con el neutrino peer configurado. Intenta cambiar la lista de pares preferidos o añade un par específico que sepas que tiene mejor latencia para la sincronización. Los servidores neutrino más conocidos son:



 - btcd1.lnolymp.us | btcd2.lnolymp.us - para la región de EE.UU
 - sg.lnolymp.us - para la región de Asia
 - btcd-Mainnet.lightning.computer - para la región de EE.UU
 - uswest.blixtwallet.com (Seattle) - para la región de EE.UU
 - europe.blixtwallet.com (Alemania) - para la región de la UE
 - asia.blixtwallet.com - para la región de Asia
 - node.eldamar.icu - para la región de EE.UU
 - noad.sathoarder.com - para la región de EE.UU
 - bb1.breez.technology | bb2.breez.technology - para la región de EE.UU
 - neutrino.shock.network - Región de EE.UU



- _LND logs_ - herramienta muy útil para depurar los problemas de su nodo LN y controlar en profundidad lo que ocurre con un nivel más técnico.
- configuración avanzada: más herramientas para controlar el uso de su nodo LND:



 - _Modo pathfinding_ - bimodal o apriori, formas de encontrar una ruta mejor para sus pagos LN y también el restablecimiento de la información de enrutamiento anterior. Por favor, lee estas muy buenas guías sobre pathfinding: [Pathfinding](https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - por Docs Lightning Engineering y [LN Payment Pathfinding](https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - por Voltage
 - _Persistent LND_ - activa este modo si quieres que el servicio LND se ejecute continuamente en segundo plano y mantenga tu nodo online 24/7. Esto es muy útil si usas Zeus como PoS en una pequeña tienda o estás recibiendo muchas puntas LN sobre la LN Address.
 - _Rescan wallet_ - esta opción activará al reiniciar un escaneo completo de todos los txs onchain de su Wallet. Actívala sólo en caso de que te falten algunos txs en tu Wallet. La tarea de reescaneo llevará tiempo, varios minutos, así que sea paciente y compruebe siempre los registros para ver más detalles sobre el progreso.
 - _Compact Database_ - esta opción es muy útil si tu aplicación Zeus está ocupando mucho espacio en el dispositivo (ver detalles de la aplicación en la configuración de tu dispositivo). Si tienes mucha actividad usando Zeus, te recomendaría hacer esta compactación más a menudo. Una vez que veas que tienes más de 1-1.5GB de datos para la aplicación Zeus, realiza la compactación. Se reiniciará y tardará algún tiempo, así que ten paciencia.
 - _Delete Neutrino files_ - esta opción para borrar los archivos de neutrino (con un reinicio) reducirá mucho el uso de almacenamiento de datos. Reducir el uso de datos tambien tiene un gran impacto en el uso de bateria, reduciendo el uso de bateria, especialmente si usas Zeus en modo persistente.


**D - Información del nodo**


En esta sección, encontrará más detalles sobre el estado de su nodo Zeus como:



- Alias - ID corto del nodo
- Clave Pública - la clave pública completa de tu nodo necesaria para que otros nodos encuentren la ruta hacia tu nodo. Recuerda que esta pubkey NO es visible en los Exploradores regulares de LN (Mempool, Amboss, 1ML etc). Esta pubkey es accesible SOLO a través de tus peers y canales LN conectados.
- Versión de aplicación de LN
- Versión de la aplicación Zeus
- Estado Sincronizado con la cadena y Sincronizado con el gráfico - muy importantes, muestran el estado correcto de tu nodo. Si estos dos no muestran "true" significa que tu nodo todavía se está sincronizando o está teniendo algunos problemas de sincronización. Así que se sugiere mirar en los logs de tu LND o esperar un poco más.
- Altura del bloque y Hash - muestra el último bloque y Hash que su nodo vio y sincronizó.


**E - Información de la red**


Esta sección muestra más detalles sobre el estado general de Lightning Network, extraídos de los datos de sincronización del gráfico: número de canales públicos disponibles, número de nodos, número de canales zombis (desconectados o muertos), diámetro del gráfico, grado medio y grado máximo del gráfico.


Estos datos de información podrían ser útiles para depurar o simplemente utilizarse para estadísticas.


**F - Rayo Address**


En esta sección el usuario podrá configurar su propia autocustodia LN Address @zeuspay.com.


ZEUS PAY aprovecha los hashes de preimagen generados por los usuarios, las facturas HODL y el esquema de atestación Zaplocker Nostr para permitir a los usuarios que no estén conectados 24 horas al día, 7 días a la semana, recibir pagos a una Address de iluminación estática. Los usuarios sólo tienen que iniciar sesión en sus monederos ZEUS en un plazo de 24 horas para reclamar los pagos, de lo contrario serán devueltos al remitente.


Si activa el "modo persistente" todos los pagos a su LN Address se recibirán al instante.


Aprenda cómo funcionan los pagos [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) y más sobre [ZeusPay Fees here](https://docs.zeusln.app/lightning-Address/fees).


**G - Direcciones Onchain**


En esta sección podrá consultar las direcciones onchain generadas para un mejor control de las monedas


**H - Contactos**


En Zeus v 0.8.0 se ha introducido una nueva agenda de contactos que puedes utilizar para enviar pagos rápidamente a tus amigos y familiares, también con la posibilidad de importar tus contactos de Nostr.


Sólo tienes que introducir tu Nostr npub o NIP-05 Address legible por humanos, y ZEUS consultará a Nostr todos tus contactos. Desde allí puedes enviar un pago rápido a un contacto, o importar todos o algunos contactos a tu agenda local


Aquí tienes un breve vídeo sobre cómo configurar y utilizar tus contactos Zeus:


**I - Herramientas**


Aquí tenemos varias subsecciones con más herramientas:



- cuentas_ - aquí puedes importar cuentas externas / monederos, monederos Cold, monederos Hot, para controlar o utilizar como fuente de financiación externa para tus canales de nodos Zeus. Esta característica es todavía experimental.
- acelerar la transacción_ - Esta función podría ser útil cuando se tiene un tx atascado en Mempool y desea aumentar la tasa. Tendrás que proporcionar la salida del tx desde los detalles del tx y seleccionar la nueva tarifa que deseas utilizar. Debe ser más alta que la anterior y requiere que tengas más fondos disponibles en tu Wallet onchain.


![Image](assets/en/05.webp)


Tienes que ir a tu tx pendiente y copiar el punto de salida txid. A continuación, vaya a esta sección y pegarlo, a continuación, seleccione la nueva tasa que desea utilizar para golpearlo. Aparecerá una nueva pantalla con las tasas recomendadas en ese momento, o puedes establecer una personalizada. Recuerda que DEBE ser superior a la anterior.


Siempre es mejor mantener un UTXO con un máximo de 100k Sats en su Zeus onchain Wallet, para poder utilizarlo para golpear las tasas cuando sea necesario.



- _Firmar o verificar_ - Con esta función puede firmar un mensaje específico con sus claves Wallet. También se puede utilizar para verificar un mensaje para demostrar que proviene de un específico Wallet claves.
- conversor de divisas_ - una herramienta sencilla para calcular la conversión de tasas entre BTC y otras monedas fiduciarias.


**J - Mercancía y Apoyo**


Aquí encontrarás más información y enlaces sobre Zeus, tienda online, patrocinadores y redes sociales.


**K - Ayuda**


En esta última sección encontrarás enlaces a la página de documentación de Zeus, a las incidencias de Github (si quieres enviar un error o una solicitud directamente a los desarrolladores de la aplicación) y a la asistencia por correo electrónico.



### PASO 2 - EMPEZAR A UTILIZAR EL NODO ZEUS



Recuerde, Zeus es principalmente para ser utilizado como un LN Wallet, para pagos fáciles y rápidos sobre LN. Por supuesto, también contiene un onchain Wallet, pero que uno debe ser utilizado exclusivamente para la apertura / cierre de canales LN y no para los pagos regulares de un café.


Por favor, lea mi otra guía sobre [cómo ser su propio banco utilizando los 3 niveles de Stash](https://darth-coin.github.io/beginner/be-your-own-bank-en.html).


En este momento el usuario tiene 2 formas de empezar a utilizar Zeus:



- Directamente sobre LN, usando el canal 0-conf de Olympus LSP
- Deposita primero en onchain Wallet y luego abre un canal normal LN con el peer que desees.


#### Método A - Utilizando Olympus LSP


Esta es una forma muy fácil y directa de incorporar un nuevo usuario de LN a Zeus. Podría ser un usuario totalmente nuevo Bitcoin que no tienen Sats en absoluto, a bordo por un amigo, o un nuevo comerciante a partir de su 1er pago LN.


Por defecto, Zeus utilizará su propio LSP, Olympus. Pero más adelante puede cambiar también a otros LSP que soporten este protocolo 0-conf para abrir canales.


Simplemente creando una Invoice en tu Zeus (pon el importe y pulsa el botón "solicitar"), podrás recibir esas Sats inmediatamente.


La Invoice que generate será [envuelta](https://docs.zeusln.app/lsp/wrapped-invoices) y se te presentarán las tarifas asociadas al servicio si se pagan. Este Invoice envuelto contiene pistas de ruta hacia tu nodo Zeus, por lo que el LSP podría encontrar tu nuevo nodo y abrir un canal con los nuevos fondos que estás depositando.


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


Para obtener un canal LN del LSP con los fondos que quieres recibir la 1ª vez, este Invoice debe ser pagado desde otro LN Wallet y esperar unos momentos hasta que el LSP esté abriendo el canal hacia tu nodo Zeus, deducir la comisión y empujar la cantidad restante del pago en tu lado del canal.


Todo lo que tienes que hacer es pagar el Invoice generado para ti en ZEUS con otro Wallet relámpago, y tu canal se abrirá al instante. [Consulta las tarifas de Zeus LSP](https://docs.zeusln.app/lsp/fees).


Otra ventaja de pagar por un canal es el enrutamiento sin comisiones. Esto significa que cuando se enrutan pagos, el primer salto a través de OLYMPUS by ZEUS no incurre en gastos de enrutamiento. Tenga en cuenta, que los saltos más allá de OLYMPUS by ZEUS todavía le cobrará.


Una vez que el canal esté listo, haz clic en el botón derecho de la parte inferior de la pantalla, que muestra los canales de Zeus.


![Image](assets/en/08.webp)


Y verás un canal como este, mostrando tu lado del balance del canal:


![Image](assets/en/09.webp)


Cuanto más gastes de este canal, más liquidez entrante tendrás. Por más Sats que recibas en este canal, menos espacio de liquidez entrante tendrás.


He aquí una sencilla demostración visual (realizada por René Pickhardt) del funcionamiento de los canales LN:


En este momento, teniendo en cuenta la pantalla de demostración de canales, haz clic en el nombre del canal y verás más detalles sobre él.


Tienes un único canal con Olympus, de una capacidad total de 490 000 Sats, con un saldo de 378k Sats por tu parte y 88k Sats por parte de Olympus. Eso significa que podrías recibir un máximo de 88k Sats más en el mismo canal.


Si necesitas recibir más de 88k Sats (la liquidez entrante disponible en este caso), digamos otros 500k Sats, simplemente creando un nuevo LN Invoice con esa cantidad, activará una nueva petición de canal al LSP Olympus. Por lo que obtendrá un 2º canal.


Por eso, para evitar pagar más comisiones por abrir varios canales, se recomienda abrir primero un canal más grande, digamos 1-2M Sats. Una vez abierto, puedes cambiar a onchain parte de esos Sats, digamos el 50%, utilizando cualquier servicio de intercambio externo descrito en esta guía.


Una vez que cambies de ese canal digamos el 50% y vuelvas a tener el Sats en tu propio Zeus onchain Wallet, estarás listo para pasar al siguiente método de apertura de un nuevo canal - de balance onchain.


#### Método B - Utilizar su saldo onchain


Con este método puede abrir canales hacia cualquier otro nodo LN, incluyendo el mismo LSP Olympus. Pero si ya tienes un canal con Olympus es recomendable tenerlo también con otro nodo, para mayor fiabilidad y además podrías utilizar MPP (pago multiparte).


![Image](assets/en/10.webp)


Arriba se muestra un ejemplo de pago de un LN Invoice utilizando MPP. Como puede ver en la parte inferior de la pantalla tiene "ajustes" y se está abriendo una página desplegable con más detalles para el pago que está a punto de hacer. En esa pantalla, si tienes al menos 2 canales abiertos, la función MPP estará activada por defecto. También puedes activar AMP (atomic multi-path) y establecer las partes específicas que desees. Es una función muy potente


Para un nodo privado como Zeus, recomendaría tener 2-3 buenos canales (max. 4-5), con buenos LSPs y buena liquidez para cubrir todas tus necesidades de pagar o recibir Sats sobre LN. [Ver más consejos sobre liquidez en nodos LN en esta guía](/nodes/managing-lightning-node-liquidity-es.html). También aquí otra [guía general sobre la liquidez de LN](https://Bitcoin.design/guide/how-it-works/liquidity/) del equipo de diseño de Bitcoin.


Elegir los peers adecuados, lo sé, no es una tarea fácil, incluso para usuarios experimentados. [Así que te daré algunas opciones para empezar](https://github.com/ZeusLN/zeus/discussions/2265), estos son nodos peer que probé yo mismo usando Zeus (intenté conectarme sólo a nodos LND para evitar problemas de incompatibilidad)


Aquí también hay una lista de pares de nodos avalados para Zeus. Si conoces alguno bueno, puedes añadirlo a la lista.


Puedes abrir un canal en Zeus accediendo a la vista Canales haciendo clic en el icono del canal situado en la esquina inferior derecha de la vista principal y, a continuación, pulsando el icono + situado en la esquina superior derecha.


![Image](assets/en/11.webp)


Si quieres abrir un canal con un nodo específico, pulsa en la esquina superior (A) para escanear el QR nodeID del nodo (en Mempool, Amboss, 1ML puedes obtener ese QR) y se rellenarán todos los detalles del peer.


RECORDATORIO:


- ¡Los nodos incrustados Zeus no utilizan el servicio Tor ! ¡Así que por favor no intentes abrir canales con nodos que estén bajo Tor! Te estás haciendo más daño a ti mismo que añadiendo más privacidad. Tor para LN no ofrece más privacidad sino que añade más problemas.
- elige sabiamente a tus compañeros, mejor que sean buenos LSPs, buenos nodos de enrutamiento, no nodos plebeyos aleatorios que podrían cerrar tus canales y no podrían ofrecer buena liquidez. [Aquí escribí una guía dedicada](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) sobre liquidez y ejemplos de nodos.


Si hace clic directamente en el botón "Abrir canal a Olympus" se rellenarán los campos necesarios para abrir un canal a [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581).


A diferencia de los canales LSP de pago, tu canal requerirá la confirmación On-Chain, utilizando tus fondos onchain (puedes seleccionar entre tus UTXOs en la vista de canal abierto); no se abrirá instantáneamente. Por favor, consulta primero las tarifas reales de Mempool y ajústalas en consecuencia, dependiendo de lo rápido que quieras abrir ese canal.


Antes de pulsar el botón para abrir el canal, desliza hacia abajo las opciones avanzadas:


![Image](assets/en/12.webp)


También tendrás que asegurarte de que el canal no está anunciado (privado). Por defecto la opción está desactivada para canales anunciados. No se recomienda activar esta opción para el nodo incrustado Zeus, es útil sólo cuando se utiliza Zeus con su nodo remoto, como un nodo de enrutamiento público.


A diferencia de los canales LSP de pago, no se beneficiará del enrutamiento sin comisiones al abrir canales con este método.


Y listo, sólo tienes que pulsar el botón "Abrir Canal", esperar a que el tx sea confirmado por los mineros. Una vez abierto el canal puedes realizar las transacciones que desees con el Sats desde tus canales.


Ten en cuenta que estos canales tendrán todo el saldo de TU lado, por lo que no tendrás liquidez entrante. Como dije antes, intercambia o gasta algo de Sats comprando cosas sobre LN para "hacer más espacio" para recibir.


Piense en sus canales LN como en un vaso de agua. Viertes un poco de agua (Sats) en un vaso vacío (tu canal) hasta llenarlo. No puedes verter más agua hasta que bebas un poco (gastar / cambiar). Cuando el vaso esté casi vacío, vierte más agua (Sats) en él utilizando un swap in. [Más información sobre los servicios externos de intercambio aquí](https://darth-coin.github.io/nodes/lightning-submarine-swaps-en.html).


También hay otros servicios de PSL como venderte canales de entrada: LNBig o Bitrefill. Creo que hay más servicios como estos pero ahora mismo no los recuerdo.


Así que si necesitas prácticamente un canal LN vacío (el saldo es 100% del lado del par desde el principio), para recibir más pagos de los que puedes manejar en tus canales existentes llenos, esta podría ser una muy buena opción. Pagarás una tarifa específica por abrir estos canales y obtendrás mucho espacio de entrada.



## TRUCOS Y CONSEJOS


### Límites de las reservas de entrada


Ahora mismo, debido a algunas limitaciones del código LN no es posible recibir exactamente la cantidad que se muestra en "Entrada". Tenga siempre en cuenta que debe hacer sus facturas con una cantidad ligeramente inferior, respectivamente la cantidad de "Reserva Local del Canal".


![Image](assets/en/13.webp)


Como se puede ver en la imagen de arriba, la "entrada" muestra que todavía puedo recibir 5101 Sats, pero de hecho en este momento es imposible recibir más. Y se puede observar que es la misma cantidad que la "reserva local".


Así que ten en cuenta que, cuando hagas facturas a cobrar, echa también un vistazo a la liquidez de tus canales y deduce la reserva local de esa cantidad, si quieres llevar al límite la cantidad a cobrar.


### Un consejo rápido para los nuevos usuarios que empiezan con el nodo Zeus:



- Aproveche correctamente sus nuevos canales.


Por ejemplo, si sabe que en una semana recibirá, digamos, 1M Sats, abra un canal de 2M Sats e intercambie en onchain Wallet o en otra cuenta (temporal) de custodia LN el 50-60% de su liquidez de salida. Esté siempre preparado con más liquidez. Una vez que necesites más liquidez en tus canales Zeus, puedes volver a moverla desde las cuentas de custodia.


Si sabes que vas a enviar por ejemplo 500k Sats/semana, entonces abre un canal de 1M Sats. De esta forma seguirás teniendo una reserva hasta que vuelvas a llenarla.



- Si usted es comerciante y siempre va a recibir más de lo que gasta regularmente, compre un canal de entrada dedicado. Es la forma más barata. Pagas una cuota mínima y obtienes un canal "vacío".



- No abras pequeños canales sin sentido de 50-100-300-500k Sats. Los llenarás en cuestión de días, aunque sólo los uses para zaps. Abre canales más grandes y diferentes, NO sólo un canal.


Una vez que abras un canal más grande, siempre puedes usar swaps submarinos externos para mover Sats a tus carteras onchain (incluso de vuelta a Zeus onchain). Mantener un equilibrio entre la liquidez entrante y saliente es bueno y también puedes "reutilizar" esos Sats para abrir más canales si quieres.


### Invoice envuelto


Si quieres añadir más privacidad a la recepción, puedes utilizar el método "Invoice envuelto". Recordatorio: para poder hacer esto, necesitas un canal con Olympus LSP. Las facturas envueltas "ocultarán" el destino final (tu nodo Zeus) y mostrarán tu nodo LSP como destino al pagador.


Para obtener una Invoice envuelta, vaya a la pantalla principal del teclado, ponga el importe y pulse solicitar. Aparecerá un código QR normal para tu Invoice. Ahora, pulsa el botón "X" de arriba a la derecha y serás redirigido a más opciones para la Invoice.


![Image](assets/en/14.webp)


Ahora tendrás que activar esa opción en la parte superior "Habilitar LSP" y darle al botón "Crear Invoice". Esa opción creará el Invoice envuelto y recuerda, cobrará una pequeña comisión.


### Facturas con indicaciones de ruta


Se trata de una función muy útil si desea gestionar la liquidez de varios canales de entrada. Prácticamente puede indicar a qué canal de entrada desea recibir la Sats de una Invoice.


Esta función también se puede utilizar para el reequilibrio circular, cuando se desea mover liquidez de un canal lleno a otro vacío.


¿Cómo crear un Invoice con indicaciones de ruta?



- En la pantalla principal, deslice hacia la derecha el cajón LN y haga clic en "Recibir"
- En la configuración de Invoice ve a la parte inferior y activa el botón "Insertar pistas de ruta", luego selecciona la pestaña "Personalizada". Se abrirá una pantalla con todos los canales disponibles. Selecciona el que quieras recibir.
- Rellene todos los demás datos del Invoice, importe, nota, etc. y haga clic en "crear Invoice".
- Al pagar ese Invoice, el Sats entrará en el canal indicado.


Si quieres pagarte a ti mismo ese Invoice (reequilibrio circular), cuando lo pagues desde tu mismo nodo Zeus, en la pantalla de pago, selecciona el canal de salida (uno con más liquidez) que quieres que se utilice como envío del pago.


### Pagar con Keysend


Keysend es una función muy infravalorada de LN y los usuarios deberían utilizarla más a menudo.


[Keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend) permite a los usuarios de Lightning Network enviar pagos a otros, directamente a su clave pública, siempre que su nodo disponga de canales públicos y tenga keysend activado. Keysend no requiere que el beneficiario emita una Invoice.


¿Y cómo puedes hacer eso con Zeus?


Simplemente escanea o copia el nodeID de destino (o utiliza los contactos de Zeus para guardar tus nodos de destino habituales como contactos) y luego, desde la pantalla principal de Zeus, haz clic en el botón "Enviar". En esa pantalla, pegue el nodeID o selecciónelo de sus contactos.


Pon la cantidad de Sats, un mensaje si es necesario (sí, puedes usarlo también como chat secreto sobre LN) y pulsa el botón "Enviar". Listo


![Image](assets/en/15.webp)


Si tienes un canal directo con el par de destino, NO habrá comisiones de por medio.


Si no tienes un canal directo con el peer de destino, entonces el pago keysend pagará las tasas como un pago LN Invoice normal, enrutado en una ruta regulada como cualquier otro pago. Sólo que, recuerde, no quedará ningún rastro como LN Invoice.


## Conlusión


Recomiendo leer la guía de seguimiento [Uso avanzado de Zeus](https://darth-coin.github.io/wallets/zeus-node-advanced-usage-en.html) con más instrucciones y casos de uso.


Y... ¡ya está! A partir de ahora sólo tienes que usar Zeus Node como un BTC/LN Wallet normal en tu móvil. La interfaz de usuario es bastante sencilla y fácil de usar, intuitiva para cualquier tipo de usuario, no creo que tenga que entrar en más detalles sobre cómo hacer y recibir pagos.


En conclusión, he aquí una tabla comparativa de privacidad :


![Image](assets/en/16.webp)