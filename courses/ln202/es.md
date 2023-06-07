---
name: Implementación de un nodo Bitcoin y Lightning
goal: Desplegar un nodo Bitcoin y Lightning a través de Umbrel
objectives:
  - Instalar un nodo Bitcoin
  - Gestionar un nodo Bitcoin
  - Utilizar un nodo de la Red Lightning
---

# Un viaje al lado técnico de Bitcoin

![Cartel del curso](Formation\courses\btc101\assets\affiche\BTC101_vignette-presentation-front.png)

Esta formación resulta ser más técnica y será aún más beneficiosa si ya tienes conocimientos sobre Bitcoin, en particular la comprensión del funcionamiento de las carteras Bitcoin y el principio de transacción, minería y blockchain. No es necesario saber programar, tu curiosidad y tu voluntad de aprender son las únicas habilidades necesarias. Recuerda, cada experto alguna vez fue un principiante. Así que, respira profundamente y sumérgete en el emocionante universo de Bitcoin. Estás a punto de comenzar un viaje emocionante y enriquecedor. ¡Buena suerte!

+++

# Convertirse en un Bitcoiner soberano

![Lanzamiento del curso](https://youtu.be/NF3SHhE1PFw?list=PLinTFKehfR4zoKvBcncHPr-ZTh1enuEhr)

Con el fin de participar plenamente en la filosofía de Bitcoin y encarnar el lema "No confíes, verifica", buscamos convertirnos en usuarios soberanos de los nodos Bitcoin. En este proceso, nos apoyaremos en la interfaz de Umbrel para configurar nuestro propio nodo. Las herramientas necesarias para esta tarea incluyen una Raspberry Pi, un disco duro externo, una tarjeta SD, un ventilador y una caja, para una inversión total estimada de alrededor de 200€.

Al adoptar Umbrel como nuestra base operativa, podremos integrar la Red Lightning, explorar la mempool y descubrir soluciones de multisig. Al final de este viaje, no solo nos habremos afirmado como Bitcoiners soberanos, sino que también tendremos la satisfacción de haber contribuido activamente a la red Bitcoin.

# ¿Qué es un nodo Bitcoin?

![¿Qué es un nodo?](https://youtu.be/19YgL9vkHh4)

Un nodo Bitcoin es simplemente un dispositivo que ejecuta el software Bitcoin, la piedra angular de la existencia y comunicación de la red. Estos nodos constituyen la base de la descentralización de Bitcoin, adoptando diferentes formas y asumiendo diversas responsabilidades. Entre ellas, se encuentran la recepción y transmisión de transacciones, la visualización de transacciones salientes y el establecimiento de conexiones con otros nodos.
Tres roles principales se asignan a estos nodos: establecer el consenso de Bitcoin, validar transacciones e interactuar con la red. Gracias a esta descentralización, Bitcoin cuenta con una mayor resiliencia, con una privacidad reforzada al no depender de un servidor de terceros. Según [Bitnodes](https://bitnodes.io/nodes/all/), alrededor de 43,000 nodos en todo el mundo forman la red de Bitcoin.

Ahora exploremos las funciones específicas de estos nodos dentro de la red de Bitcoin. Un nodo no es solo un software; también es una puerta de enlace al consenso de la red de Bitcoin y al acceso al historial de la cadena de bloques. Por ejemplo, los comerciantes utilizan su propio nodo para validar las transacciones entrantes y salientes.

La ventaja de gestionar su propio nodo radica en mejorar la privacidad y lograr la soberanía financiera. De hecho, ejecutar su propio nodo refuerza su contribución a la red y lo convierte en su propio banco. Esto le permite verificar las transacciones en tiempo real, lo que le brinda una mejor toma de decisiones sobre sus finanzas.

En conclusión, hacer funcionar su propio nodo en la red de Bitcoin ofrece muchas ventajas. No solo contribuye a la descentralización de la red, fortaleciendo así la resiliencia del sistema, sino que también asegura una mayor privacidad y autonomía financiera. Al realizar este proceso, podrá autenticar las transacciones en tiempo real, tomar decisiones financieras informadas y evitar la dependencia de un servidor de terceros, garantizando así su privacidad. Más allá de todo esto, ejecutar su propio nodo es una forma concreta de contribuir al ecosistema de Bitcoin y encarnar verdaderamente el papel de su propio banco.

# Tutorial de nodo Bitcoin a través de Umbrel

![Tutorial de Umbrel](https://youtu.be/mr4iTzdTczI)

En este capítulo, desplegaremos nuestro propio nodo de Bitcoin, abriremos canales lightning y probaremos una billetera multi-firma.
Esto tiene un costo material significativo para algunas personas. Tenga en cuenta que toda la formación se puede seguir SIN el material. No se perderá si no tiene su propio nodo.
Si desea comenzar, aquí están los productos (enlace de afiliación):

- Tarjeta SD de 16 GB - https://amzn.to/3Qi2Opm
- Raspberry Pi 4 - https://amzn.to/3qoSUYl
- SSD de 1 TB - https://amzn.to/3jSvjLC​
- Caja externa para disco duro - https://amzn.to/3x5R02S
- Alimentación RASPBERRY - https://amzn.to/3D36zvM
- Raspberry Pi FLIRC Case - https://amzn.to/3TNllgi
  Si has pasado por los enlaces de afiliados, ¡gracias por tu apoyo! Permites que este proyecto sobreviva y ofrezca cada vez más formaciones y contenidos educativos.

¿Qué se necesita para hacer funcionar un nodo Bitcoin?

- La blockchain ocupa alrededor de 500 GB, por lo que se debe prever espacio.
- La conexión a internet debe ser constante con alrededor de 5 GB de ancho de banda por mes.
- Se necesita RAM para hacer funcionar BTC Core.
- Se necesita más RAM si se hace funcionar Umbrel y un nodo LN (mínimo 4 GB).

Por lo tanto, se puede hacer funcionar el nodo Bitcoin directamente en el ordenador o utilizar un sistema como el de la video con una Raspberry Pi.

¡Existen otras soluciones ya hechas!

Sigue estos pasos para crear un nodo completo con una Raspberry Pi y Umbrel. Antes de empezar, ten en cuenta que necesitarás alrededor de 200 euros para comprar el material necesario, aunque el software es gratuito.

1. **Preparación de las herramientas**: Ve a [Umbrel](https://umbrel.com/), una solución de código abierto conocida por su excelente interfaz de usuario y buen servicio, para descargar el software necesario. Además, necesitarás Benella Itcher para flashear la tarjeta SD.
2. **Montaje de la Raspberry Pi**: Ensambla tu Raspberry Pi. Asegúrate de instalar el ventilador y los pequeños componentes de refrigeración incluidos en el kit.
3. **Flasheo de la tarjeta SD**: Usa el dispositivo proporcionado en el kit para flashear la tarjeta SD. Si tienes dificultades, intenta reformatear la tarjeta o desconectar y volver a conectar el dispositivo.
4. **Conexión del material**: Una vez que la tarjeta SD esté flasheada, conecta el SSD a la Raspberry Pi a través de un puerto 3.0. Luego, conecta la Raspberry Pi a tu router y a una fuente de alimentación eléctrica.
5. **Configuración de Umbrel**: Después de unos 5 minutos, podrás acceder a la interfaz de Umbrel en tu ordenador. Se recomienda usar un gestor de contraseñas para crear y guardar una contraseña segura para acceder a tu nodo Umbrel.
6. **Aseguramiento de tu seed (frase mnemotécnica)**: Tu seed es la clave privada que te da acceso a tus bitcoins. Por lo tanto, asegúrate de guardarla en un lugar seguro. Evita tomar fotos o capturas de pantalla de tu seed. También se recomienda guardar el enlace TOR en tu gestor de contraseñas para un acceso fácil posterior.
7. **Exploración del panel de control de Umbrel**: Umbrel tiene un panel de control claro y una tienda de aplicaciones innovadora para descargar otras aplicaciones. El tutorial de Umbrel está disponible para todos, solo necesitas comprar el material y seguir los pasos.

# Visión general de Umbrel

![vista general de Umbrel](https://youtu.be/cwEa61BgemM)

Estamos a punto de examinar exhaustivamente esta interfaz que facilita la gestión de su cartera de Bitcoin y Lightning Network.

Para empezar, nos identificaremos en la cuenta utilizando una contraseña segura y un gestor de contraseñas dedicado. Luego, emprenderemos una exploración detallada de la interfaz, familiarizándonos con las características distintivas de la cartera de Bitcoin y de la red Lightning.

El nodo se comunicará con otros nodos en la red peer-to-peer de Bitcoin de forma aleatoria y bajo seudónimo. Esta característica esencial permite descargar toda la cadena de bloques (también llamada timechain) sin depender de una entidad central. Sin embargo, hay que tener en cuenta que la descarga inicial de la timechain puede durar varios días, ya que representa un volumen de más de 500 GB para recibir.

Luego realizaremos transacciones dentro de la cartera de Bitcoin, incluyendo una transferencia de prueba a una cartera multisig. A continuación, abriremos canales de Lightning Network y utilizaremos conexiones activas en la cartera de Lightning Network. La apertura de canales requiere cierta exploración visual.

Después de realizar estas operaciones, Bitcoin Core se vuelve operativo. Entonces, puede conectar algunas de sus carteras a su nodo para verificar el estado de sus cuentas.

Es posible vincular sus carteras de Bitcoin como [Green Wallet](https://blockstream.com/green/), [Samouraï](https://samouraiwallet.com/), [Spectre](https://specter.solutions/), [Sparrow](https://sparrowwallet.com/) a su nodo de Bitcoin a través de una interfaz dedicada. Al conectar su cartera a su propio nodo, puede confirmar la recepción de fondos sin tener que confiar en un servidor externo, lo que es especialmente recomendable para los comerciantes.
Umbrel también propone una tienda de aplicaciones que agrupa exploradores, múltiples servicios relacionados con Bitcoin, Lightning o el alojamiento de sus propios datos. Nuevas aplicaciones se agregan regularmente a su [appstore](https://apps.umbrel.com/).

Para obtener más información y soporte, no dude en consultar su sitio web, el chat de Telegram, Discord, Github y Reddit. En resumen, gracias a Umbrel, tiene la oportunidad de recuperar el control de su soberanía financiera gracias a Bitcoin y convertirse en su propio banco mientras contribuye a la red. Lo alentamos a profundizar y aprender esta tecnología para integrarla en su tienda, comercio electrónico, vida personal o simplemente por curiosidad.

# Análisis de la MemPool

![mempool](https://youtu.be/0xS859IoMh8)

La MemPool, intrínsecamente, funciona como un espacio de tránsito para las transacciones de Bitcoin que esperan ser validadas en la cadena de bloques. Para examinar la MemPool de manera efectiva, Umbrel es la herramienta de elección. La aplicación [Mempool.space](https://mempool.space/), accesible a través de la interfaz de Umbrel, proporciona una representación clara de las transacciones pendientes, los costos asociados y varias otras características relevantes.

La cadena de bloques de Bitcoin es esencialmente una base de datos que incorpora bloques de transacciones a intervalos regulares de aproximadamente 10 minutos. Después de cada serie de 2016 bloques, la dificultad de minería se ajusta para mantener este intervalo promedio. Si los mineros deciden retirar su energía de la red de Bitcoin, el tiempo promedio necesario para encontrar nuevos bloques aumenta, lo que lleva a una disminución en la dificultad de minería y permite que otros mineros vuelvan a ser competitivos.

Además de la dificultad de minería, el costo actual de una transacción de Bitcoin es visible en el panel de control, así como la cadena de bloques con su cadena de bloques. Las tarifas para una transacción de Bitcoin son actualmente de 40 sats/vbytes. Las tarifas de transacción en Bitcoin se basan en la complejidad de la transacción, que se considera proporcional al peso virtual (los vbytes) de la transacción. Los vbytes, o bytes virtuales, son una unidad de medida utilizada en Bitcoin para evaluar el tamaño de una transacción teniendo en cuenta la tecnología SegWit. Por lo tanto, el uso de vbytes permite una medición más precisa de la eficiencia del espacio en un bloque.

Cada usuario es libre de determinar las tarifas asociadas con su transacción, que tienden a reflejar la urgencia de la validación de la transacción: cuanto más rápido el usuario desea que se valide su transacción, más aumentan las tarifas. Por lo tanto, como el volumen de un bloque está limitado a 4 MB (aunque el tamaño promedio de los bloques es de aproximadamente 1,5 MB), cuando la demanda aumenta, las tarifas para aumentar la probabilidad de que nuestra transacción se incluya en el próximo bloque pueden aumentar significativamente.
Bitcoin tiene varias capas: el Mainnet (la cadena principal), el Testnet y el Signet (cadenas dedicadas a la experimentación y validación de nuevas funcionalidades), la Red Lightning (una red de pagos) y Liquid (una sidechain donde los bloques se validan cada minuto). Cada una de estas capas tiene su propia utilidad y casos de uso específicos.

Los bloques que contienen transacciones son construidos por los pools de minería, y su nivel de llenado varía según la demanda y el tiempo transcurrido desde la minería del último bloque. Capas superiores, como la Red Lightning, permiten transacciones más rápidas y menos costosas que en la blockchain principal, pero aún dependen de Bitcoin para su modelo de seguridad.

En conclusión, los exploradores de bloques permiten seguir las transacciones en tiempo real o rastrearlas en el pasado. Estas transacciones pueden presentar niveles de complejidad variables. Mempool ofrece una solución efectiva para visualizar la blockchain, seguir las transacciones y analizar las tarifas y la congestión de la red.

# Explorador de Bloques y Análisis de Estadísticas

![explorador de bloques y análisis de estadísticas](https://youtu.be/Qe9VaUhUS0E)

Vamos a emprender un viaje de exploración a través de la blockchain de Bitcoin, utilizando herramientas poderosas como los exploradores de bloques y la aplicación BTC Explorer en el nodo Umbrel. Los exploradores de bloques nos dan la capacidad de analizar en detalle la blockchain de Bitcoin. Con BTC Explorer, una aplicación en Umbrel, puede verificar toda la información relacionada con la blockchain de Bitcoin que se encuentra en su disco duro, lo que le permite no depender de la confianza de un tercero.

Nos referimos a una transacción específica, la misma que se examinó en la lección anterior, para demostrar las características y la importancia de estas herramientas. También ilustraremos los últimos bloques minados y detallaremos la información sobre su contenido. Luego, haremos una comparación detallada entre dos bloques distintos, analizando su contenido y el tiempo que se tardó en minarlos.

El explorador de bloques nos permite visualizar los detalles de un bloque minado, como el hash, el resumen, los outputs, las tarifas, el tiempo y las transacciones. En cuanto a Bitcoin Explorer, ofrece herramientas más sofisticadas para el análisis de la blockchain. La primera herramienta permite, por ejemplo, examinar en detalle su nodo (sincronización, índice, tamaño de la blockchain, BIP aceptados).

Las Propuestas de Mejora de Bitcoin (BIP) son propuestas de mejora del protocolo Bitcoin. Podemos observar la activación de Segwit y el número de conexiones de red. Además, los Blockstats proporcionan estadísticas detalladas sobre tarifas, transacciones, inputs y outputs.
El análisis de datos de Segwit ofrece una visión general de la evolución de Bitcoin a lo largo de los años. Las estadísticas de transacciones, volúmenes, bloques, UTXO y timestamps están disponibles de forma gratuita. La interpretación de estos datos es crucial para la investigación financiera y para verificar la adopción de Bitcoin.

Es importante tomar el control de la soberanía financiera y buscar los datos por uno mismo. El análisis de bloques permite estudiar los datos de un bloque específico, como el primer bloque minado por Satoshi en 2009, donde destruyó voluntariamente sus primeros 50 bitcoins para un lanzamiento honesto.

Los datos de transacciones de Bitcoin son transparentes y consultables por todos, incluidos los analistas y profesionales del sector. Esta información es vital porque proporciona valiosas indicaciones sobre la actividad de la red Bitcoin, la dinámica del mercado y las tendencias actuales, lo que es esencial para una toma de decisiones informada y la implementación de estrategias financieras sólidas. Además, estos datos se utilizan para el seguimiento de transacciones, lo que garantiza la trazabilidad y transparencia de la red Bitcoin.

Una transacción Bitcoin "pesada", como una que contiene 673 inputs y 1 output, ilustra el compromiso entre el número de UTXO (Unspent Transaction Outputs) y la cantidad de Bitcoin en una dirección. Los UTXO representan los fondos no gastados de una transacción anterior, que se convierten en los inputs de las transacciones futuras. El aumento del número de UTXO en una transacción la hace más compleja y costosa. Por lo tanto, es esencial agrupar los UTXO para minimizar las tarifas de transacción y optimizar el uso del espacio en un bloque de la cadena de bloques de Bitcoin.

La minería, pivote central del protocolo Bitcoin, desempeña un papel fundamental en la seguridad de las transacciones. El proceso está regulado por un ajuste de la dificultad cada 2016 bloques para mantener un intervalo medio de 10 minutos entre los bloques. Al mismo tiempo, la tasa de hash, reflejo de la potencia de cálculo de la red, está en constante aumento.

Dentro de la red, los mineros se agrupan en pools de minería. Estas entidades no tienen el poder de controlar toda la red porque los mineros tienen el privilegio de poder cambiar entre los pools a su conveniencia. Tecnologías innovadoras como Stratum V2 dan más poder a los mineros dentro de los pools de minería. Además, soluciones técnicas como MimbleWimble y Dandelion se presentan como mejoras prometedoras para las transacciones.
Par ailleurs, la riqueza histórica de la blockchain reside en el hecho de que archiva todas las transacciones, desde el bloque génesis hasta las transacciones más recientes. Incluye la primera transacción Bitcoin realizada por Satoshi a Hal Finney en el bloque 170 y la famosa transacción de 10,000 bitcoins por dos pizzas en el bloque 57043, evento que dio origen a la celebración anual del "Día de la Pizza" el 22 de mayo.

Para fortalecer su soberanía financiera y evitar la dependencia de terceros para recibir y enviar sus bitcoins, es crucial conectar sus billeteras a su propio nodo Bitcoin. Las transacciones son validadas primero por los nodos de la red durante su propagación, y luego una segunda vez cuando son incorporadas en un bloque.

En conclusión, compartir e iniciar a su entorno en Bitcoin es una acción loable. Al explotar su propio nodo y contribuir a la red, puede convertirse en su propio banco. El objetivo final es ser completamente autónomo.

# Conectar su billetera a su nodo

![conectar su billetera a su nodo](https://youtu.be/HOV3bVcram4)

En el mundo digital de hoy, proteger sus criptomonedas y su privacidad es primordial. Es en este contexto que lo guiaré en la conexión de sus billeteras móviles y de escritorio a nuestro nodo Bitcoin. Este procedimiento aumenta significativamente su seguridad y aumenta su control sobre sus activos.

Existen una multitud de billeteras disponibles: Bitbox App, Blue Wallet, Blockstream Green, Samouraï, Phoenix, Sparrow, Wasabi, Electrum y muchas más. Cada una tiene sus especificidades, fortalezas y debilidades. Para hoy, nuestro enfoque se centrará en Sparrow, una alternativa interesante a Ledger Live, conocida por su facilidad de gestión y creación de billeteras.

En cuanto a seguridad y privacidad, se puede dar un paso adicional: el uso de un servidor privado en lugar de un servidor público. Este proceso, aunque más complejo, asegura un nivel superior de control y protección. Encontrará la información necesaria para conectarse a un servidor privado en Umbrel.

Recuerde, mantener sus billeteras actualizadas es un gesto esencial. Las actualizaciones corrigen errores, combaten vulnerabilidades, mejoran el producto y a veces agregan nuevas funciones útiles. Umbrel, en particular, asegura la actualización automática de todas sus aplicaciones. Por lo tanto, es inteligente mantener su Umbrel actualizado.
Para concluir, conectar tus carteras directamente a nuestro nodo de Bitcoin es un paso hacia la independencia financiera. Esto te brinda un nivel superior de privacidad y seguridad, al mismo tiempo que te permite mantener un control total sobre tus activos digitales. La soberanía financiera significa tener la plena posesión y control de tu dinero, sin intermediarios. Al diversificar tus carteras y mantenerlas actualizadas, das un paso más hacia esta autonomía.

# Carteras multi-sig a través de Specter

![carteras multi-sig](https://youtu.be/mV1KS-Uwjew)

Te proponemos dar un nuevo paso hacia la autonomía financiera. Nuestro objetivo es establecer una cartera multi-sig con la aplicación Specter, integrada en Umbrel. Conectaremos la aplicación de escritorio a nuestro nodo, haciendo que este tutorial sea accesible para todos.

El concepto de multi-sig es simple: garantizar un nivel excepcional de seguridad para cantidades importantes. Para ello, utilizaremos tres claves privadas para asegurar nuestra nueva cartera de Bitcoin. Existen varios niveles de seguridad: cartera móvil, cartera física, frase de contraseña, multi-sig 2 de 3, multi-sig 3 de 5, o incluso una combinación de todos estos elementos con open dimes. No es necesario ser un experto en tecnología para seguir este tutorial, pero se requiere cierta familiaridad con el sistema de claves privadas y públicas.

Prepárate, porque el tutorial es rápido. Una vez que los dispositivos hayan sido inicializados, debería llevarnos unos 15 minutos. Para seguirlo, necesitarás tres dispositivos inicializados, un nodo para conectar la aplicación Specter, así como una unidad USB y una impresora. Utilizaremos la aplicación Specter para nuestra solución multi-sig. Puedes descargarla a través de Umbrel o directamente desde el sitio web de Specter Solutions. No olvides verificar la firma antes de descargarla. También puedes hacer tu multi-sig con Sparrow o Electrum. No dudes en investigar y tomarte el tiempo para familiarizarte con estas herramientas antes de usarlas para gestionar cantidades importantes.

Ahora pasemos a la práctica. Aquí, hemos realizado un 2 de 3 con una ledger y 2 trezor (blanco y negro) y Specter Desktop, que es la interfaz de cartera que nos permite interactuar con nuestras carteras, y que está conectada a Bitcoin Core a través de Umbrel.
Créeremos primero una billetera simple para interactuar con Ledger sin Ledger Live. Esto nos permitirá generar nuevas direcciones y enviar Bitcoins. Luego agregaremos otros dispositivos (tesoros) para crear el multisig. Comencemos eligiendo el segundo dispositivo (el Tesoro blanco) que conectaremos a través de USB. Después de usar el PIN para activarlo, extraeremos las claves públicas y crearemos una segunda billetera. Luego agregaremos un tercer dispositivo (el Trezor Negro) y lo usaremos para crear una billetera multisig. Crearemos una billetera multisig eligiendo los tres dispositivos, usando Signet para probar y no perder fondos en caso de una mala manipulación (sin embargo, el proceso es el mismo para el mainnet).

Luego crearemos la billetera combinando las claves públicas. La copia de seguridad de una billetera multisig contiene varios elementos. De hecho, para recrear la billetera, necesitaremos las tres claves públicas y dos claves privadas para gastar el dinero. Por lo tanto, es crucial almacenar las claves públicas con la copia de seguridad de cada una de las claves privadas en un lugar seguro.

Se recomienda escribir en papel o metal las frases mnemónicas (lista de 24 palabras) de las 3 claves privadas en varias copias (al menos 2). Además, se recomienda escribir información precisa y detallada que permita recuperar su dinero en caso de problemas o para un plan de herencia. Estas instrucciones también deben almacenarse en un lugar seguro.

Así, habrá dado un paso más en el camino hacia la soberanía de Bitcoin. Al dominar su seguridad y utilizar herramientas como el multisig, fortalece su autonomía financiera y protege sus activos de manera óptima. No olvide que la prudencia y el aprendizaje continuo son las claves del éxito en el mundo de Bitcoin.
Si desea practicar con bitcoins de Testnet, puede obtenerlos a través de este [faucet](https://bitcoinfaucet.uo1.net/).

# Apertura de canales Lightning

![ouverture de canaux](https://youtu.be/bAZJn0AH1yU)

Ahora abordemos la parte Lightning del nodo Umbrel. Usaremos ThunderHub, una aplicación entre varias que sirven como administrador de nodo Lightning, como Lightning Terminal y RideTheLightning (RTL). Estas aplicaciones nos brindan una visión precisa del estado de nuestros canales, sirviendo como interfaz entre nosotros y nuestros canales de Lightning Network (LN).
En este punto, nuestro objetivo principal es abrir un nuevo canal. Cuando descargue ThunderHub, se proporciona una contraseña predeterminada que puede encontrar directamente en la tienda de aplicaciones. Es esencial cambiarla y guardar cuidadosamente esta nueva contraseña en un administrador de contraseñas dedicado.

Cuando esté considerando abrir un canal con otro nodo Lightning en la red, surgirán algunas preguntas. Por ejemplo, ¿cuánta liquidez desea asignar a un canal? ¿Con qué partes desea abrir un canal? Las respuestas a estas preguntas son cruciales para optimizar sus transacciones y evitar posibles problemas.

Hablemos del tamaño de los canales. No sería prudente comenzar abriendo canales con una cantidad baja, como 20k, 50k o 100k sats. Sería insuficiente y no cubriría los costos de apertura y cierre del canal. Un canal de baja cantidad sería más perjudicial que útil para usted y para el resto de la red. Por ejemplo, si tiene un canal de 20k abierto con mi nodo, apenas cubriría los costos de apertura y cierre (+ reserva). Solo le quedarían migajas para gastar.

Por eso se recomienda abrir canales de al menos 500k-1M sats. Esto ofrecería un enrutamiento mejor, beneficioso para usted y para todos los demás que enrutan transacciones a través de su nodo. Es importante tener en cuenta que la idea de "más grande es mejor" no se aplica aquí. Sería mejor tener entre 5 y 6 canales salientes, cada uno con entre 500k y 1M sats, y, según sus necesidades, de 4 a 5 canales entrantes de capacidad similar.

Ahora que está familiarizado con el tamaño de los canales, pasemos a su gestión. En cuanto a la liquidez saliente (de su lado), su nodo LN le permite hacer pagos LN, comprar cosas, enviar dinero a amigos, pagar servicios, etc. Intente abrir canales LN con los comerciantes con los que planea intercambiar. En cuanto a la liquidez entrante (del lado de sus pares), encuentre pares dispuestos a abrir canales hacia su nodo. Esta liquidez entrante es necesaria para recibir pagos en LN.
La pregunta de con quién abrir canales es primordial. En primer lugar, con los comerciantes con los que planea realizar transacciones, podrá aprovechar un enrutamiento directo y evitar tarifas. En segundo lugar, piense en amigos y usuarios experimentados de LN que conoce y que pueden crear un anillo de nodos (ring of fire) con una cierta cantidad de sats para estos canales. Esto es perfecto para equilibrar la liquidez mientras se reducen las tarifas entre los nodos del anillo. En tercer lugar, su anillo de nodos puede tener conexiones o canales "externos" con otros buenos nodos, lo que facilita y acelera el enrutamiento hacia cualquier destinatario.

Para establecer estas conexiones, deberá obtener las direcciones públicas de las otras partes. Puede hacerlo preguntándoles directamente o a través de sitios como [1ML](https://1ml.com/) o [Amboss](https://amboss.space/). La apertura de un canal implica tarifas de transacción en cadena, por lo que aproveche los momentos en que la Mempool esté vacía para abrir canales. Una vez que se abre un canal, la liquidez queda bloqueada en un lado del canal. Para moverla al otro lado, debe realizar transacciones para pagos o realizar lo que se llama un "submarine swap" (veremos esto en la próxima parte). Es importante tener en cuenta que en la Lightning Network hay tarifas de enrutamiento. Si un canal se vacía demasiado rápido debido al enrutamiento, puede aumentar estas tarifas.

Antes de concluir, es importante señalar que hay otra decisión crucial que tomar al abrir canales Lightning: elegir entre un canal público o un canal privado. Cada uno tiene sus ventajas e inconvenientes, según sus necesidades y preferencias.

Un canal público se anuncia a toda la red Lightning y se puede utilizar para el enrutamiento de pagos. Es una excelente opción si desea participar activamente en la red y ayudar a facilitar las transacciones de otros usuarios. También puede generar ingresos (muy bajos) gracias a las tarifas de enrutamiento que puede percibir. Sin embargo, tenga en cuenta que dado que un canal público es visible para todos, no es adecuado si busca mantener un alto nivel de privacidad.

Por otro lado, un canal privado no se anuncia en la red y no se utilizará para el enrutamiento de pagos. Es una buena opción si valora la privacidad y planea utilizar el canal principalmente para sus propias transacciones. Es importante tener en cuenta que aunque un canal privado no ofrece las mismas oportunidades de ingresos por tarifas de enrutamiento que un canal público, puede ofrecer una mayor tranquilidad en términos de seguridad y privacidad.
En última instancia, la elección entre un canal público y un canal privado depende de su propia situación y prioridades. Evalúe cuidadosamente sus necesidades y objetivos antes de tomar una decisión.

En conclusión, la apertura de canales en la Red Lightning es un paso técnico esencial para optimizar sus transacciones. La elección del tamaño de sus canales, la elección entre un canal público o privado y la selección cuidadosa de las partes con las que abrir canales son factores determinantes para un enrutamiento eficiente y económico. En nuestra próxima sección, nos centraremos en la gestión efectiva de estos canales. Así que pase a la siguiente sección para obtener más detalles sobre esta importante faceta de la Red Lightning.

# Gestión de canales LN

![gestión de canales LN](https://youtu.be/CgBnGQLar4o)

Ahora que hemos cubierto la apertura de canales en la Red Lightning, centrémonos en su gestión. Una gestión efectiva de los canales puede marcar una gran diferencia en la optimización de su experiencia en la Red Lightning.

El primer elemento esencial de la gestión de canales es el equilibrio. Los canales de la Red Lightning tienen lo que se llama "liquidez", que se distribuye entre las dos partes del canal. El equilibrio de esta liquidez es crucial para asegurarse de que las transacciones puedan ser enrutadas eficientemente por su nodo. Demasiada liquidez de un lado o del otro puede hacer que el canal sea menos útil para el enrutamiento. Afortunadamente, existen varias estrategias para equilibrar los canales, incluyendo el uso de servicios como Lightning Loop de Lightning Labs, que permite mover la liquidez dentro y fuera de la red Bitcoin.

El segundo elemento a considerar es la supervisión de sus canales. Es importante verificar regularmente el estado de sus canales y monitorear el rendimiento de su nodo. Herramientas como ThunderHub y RTL ofrecen grandes funcionalidades para ayudar a monitorear su nodo y gestionar sus canales. Le proporcionan información sobre el estado de sus canales, incluyendo su liquidez, sus tarifas y su capacidad. Además, ofrecen funcionalidades para cerrar canales, abrir nuevos canales y equilibrar la liquidez entre los canales.

En tercer lugar, hay que tener en cuenta el cierre de los canales. A veces, puede encontrarse con un canal que ya no es útil o que ya no funciona bien. En ese caso, querrá cerrar el canal. Sin embargo, es importante tener en cuenta que cerrar un canal implica una transacción en la cadena de bloques de Bitcoin, lo que puede generar tarifas. Por lo tanto, es recomendable cerrar los canales durante períodos de baja congestión en la cadena de bloques para minimizar las tarifas.
En conclusión, la gestión de los canales de la Red Lightning es un elemento importante para mantener un nodo Lightning eficiente y económico. Con una buena estrategia de equilibrio, una supervisión regular y una gestión inteligente de la apertura y cierre de canales, se puede optimizar la experiencia con la Red Lightning. En el próximo segmento, abordaremos otro aspecto crucial de la Red Lightning: la seguridad.

# Renombrar su nodo LN

![renombrar su nodo LN](https://youtu.be/HnK1_TDYXsY)

Personalizar el alias de su nodo Lightning Network es una excelente manera de destacarse en la red. No solo es práctico, sino que también es una forma de personalizar su experiencia. Para cambiar el alias de su nodo, usaremos la interfaz de línea de comandos. Para aquellos menos familiarizados con esta interfaz, no se preocupen, esta guía los ayudará paso a paso.

Para comenzar, debe abrir la terminal de su sistema. La terminal es una interfaz de comando que permite interactuar directamente con su sistema operativo. Una vez abierta la terminal, escriba el comando `ssh -t umbrel@umbrel.local` y presione Enter. Este comando establecerá una conexión segura con su Umbrel.

Luego, se le pedirá que ingrese la contraseña de su Umbrel. Tenga en cuenta que, por razones de seguridad, la contraseña no se muestra en la pantalla al escribirla. Después de ingresar su contraseña, accederá a la interfaz de su Umbrel.

Una vez conectado, escriba el comando `sudo nano umbrel/lnd/lnd.conf` en la terminal y presione Enter. Esto lo llevará a un editor de texto llamado Nano donde puede modificar el archivo de configuración de su nodo Lightning.

Nuevamente, deberá escribir su contraseña. Luego, navegue por el archivo hasta la sección titulada "Opciones de aplicación". En esta sección, agregue la línea `alias=SOMENAME`, reemplazando "SOMENAME" por el alias que desea para su nodo. Tenga en cuenta que el uso del mouse es inútil en esta interfaz, por lo que debe usar las flechas para navegar.

Para guardar los cambios, presione `Ctrl-X`, luego `Y` y finalmente `Enter`. Esto cerrará el editor y guardará sus cambios. Para que estos cambios surtan efecto, debe reiniciar su Umbrel. Para hacerlo, acceda al menú de configuración de la interfaz de Umbrel y elija la opción de reinicio.

¡Y listo! ¡Ha logrado cambiar el alias de su nodo Lightning Network! Ahora puede reclamar su nodo en sitios como 1ML o Amboss. En la próxima sección, discutiremos otros métodos para personalizar y optimizar su nodo Lightning Network.

### ¡Apóyanos!

Este curso, así como todo el contenido presente en esta universidad, ha sido ofrecido gratuitamente por nuestra comunidad. Para apoyarnos, puedes compartirlo con tus amigos, convertirte en miembro de la universidad e incluso contribuir a su desarrollo a través de GitHub. ¡En nombre de todo el equipo, gracias!

### Nota sobre la formación

¡Pronto se integrará un sistema de calificación para la formación en esta nueva plataforma de E-learning! Mientras tanto, muchas gracias por seguir el curso y si lo ha disfrutado, piense en compartirlo con sus amigos.

# Uso lúdico de LN

![uso de LN](https://youtu.be/6yekAvH13E0)

Ahora que ha configurado su nodo, es hora de usarlo. Para este primer uso, nos interesaremos en [Satoshi's Place](https://satoshis.place/), un servicio fascinante que le permite gastar satoshis, la unidad más pequeña de Bitcoin, para hacer arte de píxeles en un lugar público en línea. Cada píxel cambia de color por un satoshi. Es libre de dar rienda suelta a su creatividad, ¡yo mismo creé una pokeball por 166 satoshis! Los pagos se realizan a través de "facturas" o "invoices" en la red Lightning. Estas facturas se pueden representar en forma de código QR, lo que hace que el pago sea fácil e instantáneo.

Cuando una transacción atraviesa varios nodos, generalmente se involucran tarifas de enrutamiento. Por lo tanto, es crucial estar bien conectado al centro de la red para reducir estos costos. Una alternativa sería abrir un canal directamente con el comerciante. Esto presenta varias ventajas, como tarifas de transacción más bajas y una velocidad de transacción más rápida.

A modo de ejemplo, crearemos un canal con Satoshi's Place para futuros pagos. Después de crear el canal, se requiere una espera de aproximadamente 30 minutos para que el canal se vuelva operativo. Una vez creado el canal, puede realizar pagos directos. Por ejemplo, puede enviar un satoshi de forma gratuita a través de la red Lightning sin un intermediario de confianza.

La red Lightning tiene varias ventajas, como su bajo costo y la capacidad de realizar pagos regulares. Para comenzar, se recomienda utilizar billeteras como Wallet of Satoshi o Alby. Estas billeteras permiten pagar facturas utilizando la red Lightning. Para obtener más información, puede leer este [artículo](https://asi0.substack.com/p/comparatif-des-portefeuilles-ln) de Darthcoin.

En conclusión, la red Lightning demuestra la capacidad de Bitcoin para evolucionar. No solo permite transacciones de bajo costo, sino que también ofrece una solución a los problemas de escala que Bitcoin ha experimentado en el pasado.

# Aceptar Bitcoin con BTCpay server

![aceptar bitcoin en su negocio](https://youtu.be/zpCMlLfiRgg)
En este último capítulo, exploraremos las diferentes formas de aceptar Bitcoin para su negocio. Revisaremos tres opciones principales: BTCPay Server a través de su nodo Umbrel, BTCPay a través de un nodo externo Luna y finalmente a través de OpenNode. Es esencial tener en cuenta que cada opción tiene sus matices, y es crucial elegir la que mejor se adapte a sus necesidades específicas.

Imaginemos que usted es propietario de un restaurante y tiene un nodo Umbrel en su establecimiento. En este caso, puede utilizar BTCpay directamente bajo Tor. Es una solución ideal para operaciones físicas donde los clientes pagan en persona.

Por otro lado, para un comercio electrónico, el uso de BTCPay bajo Tor desde su nodo Umbrel no es factible. En este caso, es preferible utilizar un nodo externo en clearnet, como Luna Node. Esto ofrece más flexibilidad y permite una integración más fluida con su plataforma de comercio en línea.

Para aquellos que buscan una solución todo en uno y fácil de manejar, OpenNode es una excelente opción. Sin embargo, su configuración y uso pueden ser bastante complejos. Es por eso que planeamos cubrir esta solución con más detalle en una formación dedicada por completo.

A continuación, encontrará los enlaces a los diferentes servicios mencionados:

- [OpenNode](https://www.opennode.com/)
- [BTCPay Server](https://btcpayserver.org/)
- [Luna Node](https://www.lunanode.com/) y la guía sobre [BTCPay Server con Luna Node](https://docs.btcpayserver.org/Deployment/LunaNode/)

Además, tuve la oportunidad de entrevistar a Nicolas Dorier, el creador de BTCPay Server. Si está interesado, no dude en ver nuestra conversación haciendo clic [aquí](https://www.youtube.com/watch?v=XR6qB76hCL0&pp=ygUoaW50ZXJ2aWV3IG5pY29sYSBkb3JpZXIgZGVjb3V2cmUgYml0Y29pbg%3D%3D). Descubrirá mucha información interesante y valiosos consejos para optimizar el uso de BTCPay Server en su negocio.

En resumen, aceptar Bitcoin puede ofrecer una multitud de ventajas para su negocio. Ya sea que sea un restaurante local o un comercio electrónico global, existe una solución adecuada para sus necesidades. Tómese el tiempo para examinar las diferentes opciones y no dude en embarcarse en esta nueva aventura de Bitcoin.

# Resumen de la formación

![conclusión](https://youtu.be/QrKbagtUE1s)
Aquí estamos, llegando al final de nuestra exploración profunda de la red Lightning de Bitcoin. Hemos recorrido un camino complejo, lleno de innovaciones tecnológicas y nuevas perspectivas sobre cómo interactuamos con nuestro dinero digital. Desde la exploración inicial de Umbrel hasta la apertura y gestión de canales Lightning, cada paso ha sido un avance hacia una mejor comprensión y dominio de esta tecnología revolucionaria.

Comenzamos con una vista general de Umbrel, familiarizándonos con la interfaz y las características clave. Luego nos sumergimos en la Mempool, aprendiendo a analizar las transacciones pendientes para obtener una visión más profunda de la red Bitcoin. Después, exploramos los exploradores de bloques y las estadísticas de la red, herramientas esenciales para monitorear el estado de la red.

Luego abordamos el aspecto más personal de la red Bitcoin: la billetera. Aprendimos a conectar nuestra billetera a nuestro nodo y descubrimos la importancia y seguridad de las billeteras multisig gracias a Specter.

Después, nos sumergimos en el mundo de la red Lightning. Exploramos la apertura y gestión de canales Lightning, dos aspectos cruciales para un funcionamiento óptimo de nuestro nodo. También aprendimos a renombrar nuestro nodo para facilitar su identificación en la red.

También tuvimos una visión divertida del uso de Lightning Network gracias a Satoshi's Place, un ejemplo concreto de cómo LN puede ser utilizado para microtransacciones de bajo costo.

Finalmente, abordamos el aspecto comercial de Bitcoin. Exploramos cómo aceptar Bitcoin en nuestro negocio a través de BTCpay server, teniendo en cuenta diferentes configuraciones según las necesidades.

Dicho esto, dominar la red Lightning no es una tarea que se logre en un día. Es una tecnología en constante evolución, compleja y matizada. Se necesitará tiempo, práctica y voluntad de aprender para realmente dominar esta herramienta. Al igual que Bitcoin en sí mismo, Lightning Network es una aventura, una exploración de lo que es posible en el campo de las finanzas digitales. Pero con paciencia, perseverancia y voluntad de aprender, pronto podrás navegar por la red Lightning con facilidad y confianza.

En resumen, el viaje que emprendimos juntos a través de la red Lightning es solo el comienzo. Dominar esta tecnología ofrece muchas oportunidades y beneficios. Así que sigue explorando, aprendiendo y experimentando con Lightning Network. El futuro de las finanzas está al alcance de tu mano.
Para concluir, es importante destacar que esta formación, al igual que las demás que ofrecemos, es completamente gratuita. Creemos firmemente en la importancia de compartir el conocimiento y hacer que el acceso a la información sea lo más libre y abierto posible. Es en este espíritu que hemos decidido compartir con ustedes todo lo que hemos aprendido sobre la red Lightning.

Sin embargo, si ha encontrado valor en esta formación y desea apoyarnos, lo invitamos a visitar nuestro sitio de comercio electrónico en la siguiente dirección: https://thebitcoinrabbithole.myshopify.com/. Al realizar compras en nuestro sitio, no solo contribuye a apoyar nuestro trabajo, sino que también nos ayuda a seguir brindando formaciones gratuitas y de alta calidad.

Gracias por tomarse el tiempo de seguir esta formación. Su apoyo e interés en nuestro trabajo significan mucho para nosotros.

# Agradecimientos y sigan excavando la madriguera del conejo

¡Felicitaciones por completar esta formación LN 202! Espero de todo corazón que le haya gustado y abierto puertas. Su descubrimiento de Bitcoin apenas comienza y lo invito a descubrir todas las demás formaciones disponibles en la universidad.

- ECON 201 abordará la economía austriaca
- SECU 101 le permitirá actualizar su seguridad
- MINAGE 201 para saber más sobre la minería
- (y muchos más)

¡Besos y hasta pronto!
