---
name: Configuración del primer nodo Lightning
goal: Comprender, instalar, configurar y utilizar un nodo Lightning
objectives: 


  - Comprender la función y la finalidad de un nodo Lightning.
  - Identifique las distintas soluciones informáticas disponibles.
  - Instale y configure un nodo Lightning (LND).
  - Conectar una cuenta de gastos.
  - Conoce los riesgos de utilizar un nodo Lightning.


---

# Tu primer paso hacia la autonomía en Lightning



Ya ha adquirido su primera sats, asegurado sus fondos de autocustodia y desplegado un nodo Bitcoin para ser soberano en su uso de on-chain. El siguiente paso es conseguir la misma autonomía en Lightning: ese es precisamente el objetivo de este curso.



LNP202 está dirigido a usuarios intermedios, y le guía paso a paso a través de la implantación de su primer nodo Lightning, sin necesidad de conocimientos técnicos avanzados.



Aprenderá a instalar LND en Umbrel, a abrir y gestionar sus canales, a supervisar su nodo y a conectar una wallet móvil, para que pueda disfrutar de una experiencia comparable a la de una wallet de custodia, manteniendo un control total sobre sus fondos.



+++


# Introducción


<partId>5e77c17a-0853-4f36-a988-1b4a956f49e4</partId>



## Resumen del curso


<chapterId>e0871abf-af6d-4221-9389-1a996aea9b79</chapterId>



LNP202 es un curso práctico diseñado para hacerte autónomo en Lightning operando tu propio nodo. El objetivo es sencillo: empieza con un nodo Bitcoin ya instalado, despliega LND en Umbrel, asegúralo correctamente, abre y gestiona tus primeros canales, y luego utiliza tu nodo a diario desde un wallet móvil. Este curso asume que ya has tomado BTC 202, ya que asumo que tu nodo Bitcoin en Umbrel está en su lugar y sincronizado. No volveremos sobre cómo configurar un nodo Bitcoin aquí.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Para comprender mejor la mecánica interna del Rayo, también es muy recomendable el curso LNP 201, aunque no es un requisito previo para este curso:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

En la primera parte de este curso LNP202, veremos qué es realmente un nodo Lightning, en qué se diferencia de un simple wallet y por qué operar un nodo personal es la única forma de utilizar Lightning sin delegar tu sats a un tercero de confianza. Esta sección concluye con una elección estratégica: qué solución es la adecuada para ti, desde los enfoques más sencillos hasta el nodo Lightning clásico, el que implementaremos en este curso.



En la segunda parte del curso, instalarás LND sobre Umbrel y, a continuación, pondrás en marcha los elementos que evitan los errores más costosos: una estrategia realista de copias de seguridad y protección contra trampas mediante una torre de vigilancia. Una vez instalados estos elementos básicos, abrirás tu primer canal, para poder empezar a pagar en Lightning con tu propia infraestructura.



Así que ya ves: en este curso LNP202, vamos a configurar un nodo Lightning en modo plug-and-play a través de Umbrel, en lugar del enfoque clásico de línea de comandos, para que sea adecuado para usuarios intermedios. Si prefieres una instalación desde la línea de comandos, te recomiendo que sigas el siguiente tutorial. También se están preparando otros cursos sobre Lightning más avanzados y orientados a la línea de comandos.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

La Parte 3 le llevará de un nodo que funciona a otro que sabe cómo controlar. Empezará por determinar el perfil de operador de su nodo Lightning (consumidor, comerciante o enrutador), luego se familiarizará con un paquete completo de software de gestión, para seguir sus canales y actuar limpiamente sobre su topología. Por último, abordará un punto muy importante de Lightning: cómo obtener liquidez entrante, ya sea mediante soluciones de pago o cooperativas.



La parte 4 se centrará en el uso cotidiano. Configurará una conexión entre su nodo y un cliente móvil, para que pueda pagar y cobrar simplemente desde su smartphone, sin renunciar a la autocustodia. Primero veremos un enfoque de red a través de *Tailscale*, y después un enfoque de protocolo a través de *Nostr Wallet Connect*, con sus respectivas ventajas y desventajas. El curso concluirá con un capítulo final que te proporcionará los hábitos adecuados para mantener la autocustodia, tanto desde el punto de vista operativo como pedagógico.



Si sigues este curso LNP202 en el orden correcto, al final del mismo tendrás una configuración completa para tu nodo Lightning, funcional para el uso diario y, sobre todo, bajo control.




## Comprender los nodos Lightning


<chapterId>8275dfd8-7a72-48cc-bf7f-bc2a46063003</chapterId>



Antes de poner en marcha tu propio nodo, este capítulo repasa brevemente la teoría básica que subyace a Lightning Network. En efecto, es importante comprender los mecanismos implicados, ya que esto le permitirá identificar los riesgos y adoptar buenas prácticas para limitarlos. Sin embargo, no entraré en detalles aquí, ya que no es el objetivo principal de este curso. Si desea profundizar en el tema, le recomiendo encarecidamente que consulte el curso LNP 201 de Fanis Michalakis, que es una referencia en la materia:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### ¿Qué es un nodo Lightning?



Volvamos a lo básico: antes de definir lo que es un nodo, tenemos que entender lo que es Lightning Network. Es un protocolo de capa superior construido sobre Bitcoin. Es un protocolo de capa superior, construido sobre Bitcoin, diseñado para permitir transacciones offchain BTC que son rápidas (con finalidad casi instantánea) y generalmente baratas. "Offchain" significa que las transacciones realizadas en Lightning no están destinadas a aparecer en la blockchain principal de Bitcoin. Lightning es también una respuesta parcial al creciente uso de Bitcoin y a la congestión de onchain, que está suscitando dudas sobre la escalabilidad del sistema.



Para funcionar, Lightning se basa en la apertura de canales de pago entre los participantes, dentro de los cuales se pueden realizar transacciones casi instantáneamente, a menudo con comisiones mínimas, sin necesidad de registrarlas una a una en la blockchain Bitcoin. Estos canales pueden permanecer abiertos durante mucho tiempo, requiriendo transacciones onchain sólo cuando se abren y se cierran.



Un nodo Lightning es un participante en la red Lightning, que abre canales y realiza pagos con otros nodos. En concreto, un nodo Lightning es un programa informático que se ejecuta en un ordenador e implementa el protocolo Lightning Network. Algunos ejemplos son LND, Core Lightning o Eclair. Algunos ejemplos son LND, Core Lightning o Eclair. La función principal de este software es:




- conectarse a un nodo Bitcoin para obtener información de la blockchain principal;
- crear y gestionar canales de pago bidireccionales con otros nodos;
- intercambiar mensajes con toda la red Lightning.



![Image](assets/fr/001.webp)



### Nodo frente a Lightning Wallet: una distinción importante



En Bitcoin (onchain), "*wallet*" se refiere al software que gestiona tus claves privadas, calcula tu saldo a partir de tus UTXO y construye tus transacciones. Este wallet puede estar basado en tu propio nodo Bitcoin o en el de otra persona, pero hoy en día, el papel del nodo y el del wallet onchain son claramente distintos.



En Lightning, es más difícil reutilizar este tipo de vocabulario sin crear confusión. El término "*Lightning wallet*" es bastante vago, porque en realidad no existe un wallet de Lightning verdaderamente autocustodiado, a menos que se base en un nodo. Por lo tanto, sólo son posibles dos situaciones:



- Para tener un nodo Lightning real (es decir, no custodio): el software que estás utilizando (por ejemplo, una aplicación móvil como Phoenix o una instancia de LND en Umbrel) está ejecutando realmente un nodo, y tú tienes realmente las claves para recuperar tus bitcoins. En este caso, tu "*Lightning wallet*" no es más que una interfaz de usuario sobre un nodo Lightning, ya sea integrado o remoto.



- Para utilizar un servicio de custodia: utilizas una aplicación que te muestra un saldo en sats en Lightning, pero en segundo plano, los fondos están en un nodo de un proveedor (por ejemplo, Wallet of Satoshi). No tienes ni las claves ni el control de los canales. Tu saldo no es más que un asiento contable en la base de datos de la empresa. Es comparable a dejar tus bitcoins en una plataforma de intercambio, con todos los riesgos asociados. En este caso, tu "*Lightning wallet*" no es más que un acceso a una cuenta gestionada por un operador que, a su vez, dirige un nodo Lightning real.



Así que no hay término medio en Lightning: o tienes un nodo (aunque sea integrado), por lo que estás en autocustodia, o no lo tienes, por lo que una empresa es propietaria de tu sats. Pero, como veremos en los capítulos siguientes, a veces es difícil distinguir estos dos usos. Por ejemplo, Phoenix es una aplicación móvil que incrusta un nodo Lightning real, pero el usuario no es necesariamente consciente de ello, ya que toda la complejidad de su funcionamiento está casi totalmente oculta.



### Recordatorio del funcionamiento de la Lightning Network



En esta sección, te haré un rápido recordatorio de cómo funciona Lightning. Una vez más, si deseas una presentación más profunda de los conceptos teóricos, te invito a que eches un vistazo al curso dedicado LNP 201.



#### Canales de pago: abrir, actualizar y cerrar



El corazón de la red Lightning se basa en canales de pago bidireccionales. Un canal puede abrirse (es decir, crearse), actualizarse a medida que se producen transacciones Lightning y, finalmente, cerrarse. Desde el punto de vista onchain, un canal no es más que una salida multifirma 2/2.



![Image](assets/fr/002.webp)



Desde el punto de vista de Lightning, se trata de un canal de pago con liquidez dividida entre los dos participantes.



![Image](assets/fr/003.webp)





- Abrir un canal:**



Dos nodos deciden abrir un canal. Uno de ellos compromete bitcoins en una transacción onchain llamada *transacción de financiación*. Esta transacción crea una salida basada en un script de multifirma 2-de-2, lo que significa que gastar estos fondos en Bitcoin requiere la firma de ambos nodos en el canal. Antes de emitir esta transacción, la parte que proporciona los fondos pide a la otra que firme una *transacción de retirada*, que no se emite onchain, pero que le permite recuperar sus fondos en caso de problema.



![Image](assets/fr/004.webp)





- Transacciones Commitment:**



El estado del canal (es decir, la distribución de sats entre A y B) está representado por un *commitment transaction*, conocido por ambos nodos pero no difundido inmediatamente en la blockchain. Esta transacción describe cómo redistribuir los fondos del canal onchain según los pagos realizados en Lightning.



Con cada pago relámpago, los dos nodos firman un nuevo estado que sustituye al anterior. El estado antiguo se revoca gracias a un mecanismo de clave de revocación: si uno de los participantes intenta difundir un estado antiguo, el otro puede recuperar el importe íntegro de los fondos como penalización.



La idea importante aquí es que siempre hay una transacción Bitcoin firmada, no difundida onchain, mantenida por los nodos, y que permite la redistribución de la sats de cada uno según los pagos realizados en la Lightning Network.



![Image](assets/fr/005.webp)





- Cierre del canal:**



Un canal puede cerrarse limpiamente mediante un cierre cooperativo, cuando ambas partes se ponen de acuerdo sobre el estado final del canal, o unilateralmente (un cierre forzado) si uno de los participantes deja de cooperar o se vuelve ilocalizable. En todos los casos, el cierre adopta la forma de una transacción onchain que gasta la salida 2/2 y distribuye los fondos entre los participantes según el último estado válido del canal.



![Image](assets/fr/006.webp)



Lightning funciona así como una capa secundaria anclada en Bitcoin: sólo ciertos eventos (la apertura y cierre de canales) aparecen en la blockchain principal. Los pagos intermedios permanecen fuera de la cadena.



Antes de seguir adelante, he aquí dos conceptos esenciales para entender cómo gestionar un canal Lightning:




- Liquididad*: la cantidad de sats disponible en un lado del canal;
- La *capacidad*: es la cantidad total bloqueada en la salida multisig 2/2, es decir, la suma de la liquidez a ambos lados del canal.



#### Una red de canales y liquidez



Un canal no es sólo para pagos entre dos nodos: forma parte de una red global de canales interconectados. Tu nodo puede enrutar pagos para otros usuarios a través de sus propios canales, y puedes enviar sats a un nodo Lightning con el que no tengas canal directo, siempre que se pueda encontrar una ruta válida entre tus dos nodos.



Cada nodo conoce, a través del protocolo de cotilleo, un mapa de esta red: qué canales existen, qué nodos están conectados por un canal bidireccional y qué capacidades están publicadas. Para enviar un pago a un destinatario sin canal directo, su nodo calcula una ruta que consta de varios saltos: su nodo → nodo X → nodo Y → nodo destinatario. En cada salto, el pago transita por un canal que debe tener suficiente liquidez en la dirección del pago.



![Image](assets/fr/007.webp)



Por tanto, la liquidez de un canal no es simétrica: un lado puede estar muy cargado, mientras que el otro está casi vacío. Gestionar esta liquidez, es decir, saber dónde están los sats y en qué dirección pueden fluir, es uno de los aspectos más importantes de la explotación de un nodo Lightning. Lo veremos con más detalle en los próximos capítulos prácticos.



#### HTLC: transportar el pago sin ser robado



Para permitir que los pagos pasen por nodos intermedios sin necesidad de confianza, Lightning utiliza contratos inteligentes denominados *HTLC* (*Hashed Time-Locked Contracts*). En términos sencillos, un HTLC condiciona la transferencia de fondos a la revelación de un secreto, e incorpora una limitación temporal para proteger al remitente en caso de fallo de la transacción. Por tanto, cada pago está sujeto a la presentación de una imagen previa (un secreto cuyo hash corresponde a un valor acordado). Si el destinatario final proporciona esta imagen previa, puede reclamar los fondos, lo que a su vez permite a cada nodo intermediario recuperar sus propios fondos.



![Image](assets/fr/008.webp)



Le ahorraré los detalles técnicos del funcionamiento de las HTLC, ya que no son esenciales para los fines de este curso. Encontrará una explicación detallada en el curso teórico LNP 201. Sólo recuerde que las HTLC permiten intercambios atómicos: o bien la transferencia se completa y nadie sale perjudicado en el enrutamiento, o bien falla y cada participante recupera sus fondos iniciales. No hay término medio.



### Las principales implantaciones de nodos Lightning



Como en el caso de Bitcoin, existen varias implementaciones del protocolo Lightning. Varios equipos independientes están desarrollando sus propias versiones, todas ellas interoperables ya que se adhieren a las mismas especificaciones (los BOLT). Estas son las principales implementaciones que se utilizan actualmente.



#### LND (*Lightning Network Daemon*)



LND es una implementación completa del protocolo Lightning, escrita en Go y desarrollada por Lightning Labs.



![Image](assets/fr/009.webp)



#### Núcleo Rayo (*CLN*)



Core Lightning (antes *C-Lightning*) es la implementación desarrollada por Blockstream. Está escrita en C, con algunos componentes en Rust.



![Image](assets/fr/010.webp)



#### Eclair



Eclair es una implementación escrita en Scala y desarrollada por la empresa francesa ACINQ. ACINQ opera uno de los nodos de enrutamiento más importantes de la red Lightning con Eclair, y utiliza esta implementación como base de software para sus propios productos, como la aplicación Phoenix.



![Image](assets/fr/011.webp)



#### LDK (*Kit de desarrollo de iluminación*)



LDK (*Lightning Development Kit*) es un kit de desarrollo de Rust, mantenido por Spiral (Block, ex-Square). No es un daemon listo para usar como LND o CLN, sino una biblioteca para desarrolladores que deseen integrar Lightning directamente en sus aplicaciones.



![Image](assets/fr/012.webp)



En este curso LNP202, nos centraremos principalmente en LND: la implementación más utilizada en soluciones llave en mano para clientes privados, como Umbrel.



Hasta aquí este breve recordatorio de cómo funciona Lightning. Una vez más, si hay algún concepto que no entiendas, o si quieres profundizar un poco más antes de ponerlo en práctica, el curso de Fanis Michalakis es la referencia imprescindible sobre el tema:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


## ¿Por qué dirigir tu propio nodo Lightning?


<chapterId>421db24e-511c-41ed-ad68-69b0662042ea</chapterId>



Responder a esta pregunta es bastante sencillo, ya que es retórica: sin su propio nodo, ya no está utilizando realmente Lightning, sino sólo la ilusión de Lightning a través de la infraestructura de una empresa.



Utilizar un wallet custodio de Lightning significa que los bitcoins pertenecen técnicamente a la empresa que opera el nodo. Usted no tiene las claves privadas, y usted no controla los canales. Tu saldo de wallet no es más que una línea en la base de datos de un proveedor de servicios. Esta situación es sin duda muy cómoda para los principiantes, y la experiencia del usuario suele ser fluida, pero la pregunta fundamental es: ¿qué ventaja tiene utilizar Bitcoin y Lightning si acabas renunciando a los mismos aspectos que los diferencian de las monedas y los bancos tradicionales?



Las dos principales propuestas de valor de Bitcoin son la soberanía monetaria (dejar de depender de una autoridad central para emitir y custodiar) y la resistencia a la censura (imposibilidad de que un tercero impida o filtre los pagos). Un sistema de custodia en Lightning va frontalmente en contra de estos dos objetivos: no se puede comprobar la masa monetaria interna de la plataforma y, por definición, un operador que posee todos los fondos y todos los canales puede censurar, retrasar, priorizar o bloquear tus pagos. En estas condiciones, podemos preguntarnos legítimamente, **qué sentido tiene utilizar bitcoin a través de Lightning si va a reproducir los mismos patrones de confianza y dependencia que con los sistemas monetarios estatales tradicionales**.



> Lo que se necesita es un sistema de pago electrónico basado en pruebas criptográficas en lugar de en la confianza, que permita a dos partes cualesquiera realizar transacciones directamente entre sí sin necesidad de un tercero de confianza.
*Satoshi Nakamoto, Bitcoin Libro Blanco


Dejando a un lado la filosofía, las desventajas más concretas para usted son las siguientes. En primer lugar, no tiene forma de verificar que la empresa posee realmente los bitcoins correspondientes a los saldos mostrados. Puede operar con reserva fraccionaria, ser pirateada, quebrar o simplemente desaparecer. En este caso, usted es un acreedor más, sin ninguna garantía real de que vaya a recuperar su dinero.



En segundo lugar, la empresa está sujeta a riesgos reglamentarios: medidas cautelares, congelación de fondos, solicitudes de bloqueo de usuarios o transacciones, vigilancia reforzada o incluso prohibición total de actividad en determinadas jurisdicciones. Cada restricción que pesa sobre el proveedor de servicios se refleja mecánicamente en usted.



En términos de confidencialidad, la situación no es mejor. Un operador de custodia ve todos sus flujos: importes, frecuencias, destinatarios, saldos, hábitos de gasto. Combinada con la información proporcionada por la aplicación y posiblemente el análisis de la cadena subyacente en Bitcoin, esta información puede proporcionar un perfil muy preciso de su actividad financiera. Una vez más, está muy lejos del objetivo de Bitcoin de reducir la vigilancia financiera.



La buena noticia es que, hoy en día, operar tu propio nodo Rayo ya no es cosa de expertos técnicos, como podía ser a finales de la década de 2010. Existen soluciones relativamente sencillas para los usuarios domésticos, que explicaremos en detalle en el próximo capítulo.




## Elegir la solución adecuada para el trabajo


<chapterId>615870e3-741d-4ec1-875d-a483e70f39d4</chapterId>



Hoy en día, es posible tener una experiencia de usuario muy cercana a la de un wallet custodiado por Rayo, sin dejar de estar en autocustodia. El objetivo de este capítulo es ayudarte a elegir el camino que mejor se adapte a tu perfil.



### Opción 1: No utilizar Lightning directamente



La primera solución es simplemente no utilizar Lightning de forma nativa, sino utilizar una Bitcoin o Liquid wallet que incorpore swaps atómicos. Por ejemplo, las aplicaciones Aqua o Bull Bitcoin Wallet utilizan este método, permitiéndole pagar facturas Lightning sin operar un nodo Lightning usted mismo, permaneciendo en autocustodia.



El principio es sencillo: tus fondos permanecen en la Bitcoin, ya sea en la on-chain o en la Liquid, y accedes a ellos a través de una wallet donde tienes las claves de la manera tradicional. Cuando escaneas una factura Lightning, tu wallet inicia una transacción (on-chain o Liquid) a un servicio de intercambio atómico. Este servicio gestiona entonces el pago Lightning a través de su propio nodo, utilizando los bitcoins que proporcionaste on-chain o a través de Liquid. Como resultado, no tienes que gestionar ningún canal Lightning tú mismo, pero puedes liquidar facturas Lightning sin problemas.



![Image](assets/fr/013.webp)



La mayor ventaja de este enfoque, en comparación con una custodia convencional Lightning wallet, es que usted permanece en posesión del 100% de sus fondos en todo momento. Los bitcoins están en su onchain o Liquid wallet, con su propia frase mnemotécnica. Incluso durante el intercambio, sigues en posesión de tus fondos, porque el intercambio es atómico. Se basa en un mecanismo criptográfico que garantiza que sólo haya dos resultados posibles: o bien el canje tiene éxito por completo, o bien falla y el servicio no puede apropiarse de tus fondos.



La mayoría de las carteras que ofrecen este tipo de funcionalidad se basan en [Boltz](https://boltz.exchange/) para la parte técnica del canje.



Esta solución también ofrece interesantes ventajas en términos de confidencialidad, sobre todo si se combina con la Liquid. Para un principiante, también es muy fácil de configurar y guardar: una frase mnemotécnica clásica, sin canales, sin liquidez que equilibrar...



Por otro lado, este enfoque tiene sus limitaciones. En primer lugar, no es incensurable: dependes de la disponibilidad y buena voluntad del servicio de intercambio. Si ya no desea procesar su cuenta, o deja de operar, ya no podrá pagar facturas de Rayo a través de él. A esto hay que añadir unas comisiones nada desdeñables: usted paga tanto las comisiones de transacción onchain o Liquid como la comisión del servicio de intercambio. Además, si las comisiones onchain suben mucho, puede resultar muy caro utilizar Lightning.



Así que para un uso ocasional, sigue siendo aceptable, pero para un usuario muy activo de Lightning, es mejor hacer las cosas bien con un nodo Lightning real.



### Opción 2: Nodos Lightning integrados



La segunda categoría de soluciones se basa en nodos Rayo integrados directamente en una aplicación móvil. Phoenix Wallet fue pionero en este modelo y sigue siendo una referencia. En la actualidad, otros proyectos ofrecen enfoques comparables, como Zeus (en modo incrustado) o BitKit.



La idea es sencilla: la aplicación ejecuta realmente un nodo Lightning, pero todas las operaciones complejas se gestionan automáticamente en segundo plano. Tienes una interfaz "*Lightning wallet*" con una frase mnemotécnica de respaldo, ves un saldo y pagas facturas, pero no gestionas canales, liquidez ni la mayoría de parámetros.



![Image](assets/fr/014.webp)



Estas soluciones son siempre de autocustodia. Las claves que controlan los fondos son generated y se almacenan en tu teléfono, y la copia de seguridad se realiza a través de una seed o un mecanismo equivalente. No eres simplemente titular de una cuenta en un proveedor de servicios, en realidad posees bitcoins bloqueados en canales que te pertenecen y no pueden ser robados.



Las ventajas de los nodos embarcados LN son numerosas:




- extremadamente fácil de instalar y utilizar;
- experiencia de usuario cercana a la de un Lightning wallet custodial, pero con autocustodia;
- sin gestión manual de los canales ni de la liquidez;
- copia de seguridad relativamente sencilla.



Pero estas wallet integradas también tienen limitaciones importantes. En primer lugar, en términos de confidencialidad, el operador del servicio (por ejemplo, ACINQ en el caso de Phoenix) tiene una visión bastante detallada de los flujos que pasan a través de su nodo: cantidades, frecuencias, destinatarios, incluso si esto está destinado a mejorar, en particular con la adopción gradual de *Trampoline Nodes*. En segundo lugar, usted depende en gran medida de este operador como su principal par Lightning. Si el nodo ACINQ deja de estar disponible (en el caso de Phoenix), si la empresa se ve sometida a presiones normativas o cambia su modelo de negocio, su experiencia de usuario puede verse gravemente degradada, o incluso comprometida.



Por último, esta simplicidad tiene un precio. Los servicios de los nodos LN integrados suelen cobrar comisiones específicas sobre depósitos, retiradas o determinadas operaciones de gestión de canales. En mi opinión, este modelo tiene sentido en cuanto al servicio ofrecido, pero para un uso intensivo, puede resultar mucho más caro que un nodo Lightning convencional bien gestionado.



### Opción 3: el nodo Lightning clásico



La tercera solución, en la que profundizaremos en este curso LNP202, consiste en operar un nodo Lightning convencional en un servidor o dispositivo dedicado.



Por "clásico" me refiero a que tú mismo instalas y configuras una implementación de Lightning (por ejemplo, LND) sobre tu propio nodo Bitcoin. Eliges tus pares, abres tus canales, gestionas tu liquidez entrante y saliente y estableces tus políticas de tarifas de enrutamiento.



En términos de soberanía, es la mejor solución. Ya no dependes de una empresa específica para tus canales o pagos: si un peer te censura o cierra un canal, puedes abrir otro con un nodo diferente. Si un servicio desaparece, tus sats permanecen en los canales que controlas, y puedes repatriarlos onchain. También puedes optimizar tus costes a largo plazo: una vez que tus canales estén correctamente dimensionados y gestionados, el coste global de los pagos puede llegar a ser muy bajo.



En términos de confidencialidad, obviamente estás sujeto a las limitaciones del propio modelo de Lightning, pero no estás entregando todo tu negocio a un único operador.



En cambio, configurar un nodo Lightning clásico es obviamente más complejo: hay que instalar, configurar, mantener, supervisar las actualizaciones, comprender la lógica de los canales y las políticas de cobro, gestionar los canales y el flujo de caja, etc. Una mala configuración, una copia de seguridad chapucera o una gestión descuidada pueden llevar más fácilmente a la pérdida de sats. Además, el nodo debe funcionar continuamente.



Este es precisamente el camino que te propongo seguir en este curso, acompañándote en cada paso del camino para limitar los riesgos y estructurar tu enfoque.



### ¿Qué solución para qué perfil de usuario?



Para elegir la solución adecuada para su perfil de usuario de Lightning, debe tener en cuenta dos factores: la frecuencia con la que utiliza Lightning y su apetito por la gestión técnica.



Si no realiza muchos pagos Lightning de forma ocasional, pero aún así quiere poder liquidar facturas LN desde su teléfono de vez en cuando, sin renunciar a la autocustodia: una Bitcoin o Liquid wallet con funcionalidad swap es probablemente la mejor opción. Usted conserva la propiedad de sus fondos, no gestiona ningún nodo y acepta unas comisiones ligeramente superiores a cambio de simplicidad.



https://planb.academy/tutorials/wallet/mobile/bull-bitcoin-2c72127c-a228-4f50-b833-c6183d56aaf6

https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Si utilizas Lightning con bastante regularidad y quieres las ventajas de un nodo real, pero no quieres dedicar tiempo a gestionar canales, comisiones o infraestructuras, un nodo Lightning embebido en móvil es una buena solución. Conservas la custodia de tus fondos, la UX sigue siendo muy accesible y toda la complejidad queda oculta, al precio de una marcada dependencia de un operador.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

https://planb.academy/tutorials/wallet/mobile/bitkit-a7224674-85c4-4045-9baf-37018d89550c

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Si eres un usuario intermedio o avanzado, dispuesto a invertir tiempo en comprender y gestionar tu infraestructura, y quieres el máximo control sobre tus canales, liquidez y costes: un nodo Lightning clásico basado en servidor es el camino a seguir. Es la solución más exigente, pero también la más coherente con la idea de soberanía de Bitcoin.




# Creación de su primer nodo Lightning


<partId>b6db225e-61ab-437a-bccb-33d07503da15</partId>



## Instalación de LND con Umbrel


<chapterId>a0014bf3-1bd3-4311-b15b-5ef2354ec744</chapterId>



Ahora que hemos repasado los conceptos básicos de Lightning y las soluciones disponibles, es hora de ponerse manos a la obra. Para realizar este curso, necesitará un nodo Bitcoin sincronizado con Umbrel. Este curso de formación LNP202 es una continuación de BTC 202; si aún no dispone de un nodo Bitcoin, le invito a realizar este otro curso de formación antes de volver aquí una vez sincronizado su nodo. Te recomiendo encarecidamente que lo consultes, ya que no entraré en detalles sobre su funcionamiento, configuración y medidas de seguridad.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

En este primer capítulo, veremos cómo instalar LND en su Umbrel. La forma en que funciona Umbrel hace que este paso sea muy sencillo, ya que todo lo que tiene que hacer es instalar una aplicación.



Desde la página de inicio, abre la `App Store` en la parte inferior de la interfaz.



![Image](assets/fr/015.webp)



En la barra de búsqueda, introduzca `Lightning Node` y, a continuación, haga clic en la aplicación.



![Image](assets/fr/016.webp)



A continuación, haga clic en el botón "Instalar" para iniciar la instalación.



![Image](assets/fr/017.webp)



En la página de inicio, haga clic en la aplicación para abrirla y, a continuación, seleccione `Crear un nuevo nodo`.



![Image](assets/fr/018.webp)



Se le da una frase mnemotécnica de 24 palabras. Guárdela en un lugar seguro. En el próximo capítulo veremos con más detalle cómo recuperar el acceso a su nodo Rayo (se trata de un proceso mucho más complejo que para un simple Bitcoin wallet), pero recuerde por ahora que esta frase desempeña un papel crucial y debe guardarla con sumo cuidado.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Guarde esta frase del mismo modo que una frase mnemotécnica convencional: en un soporte físico (papel o metal) almacenado en un lugar seguro y, a continuación, pulse el botón `NEXT`.



![Image](assets/fr/019.webp)



A continuación, introduce las palabras de tu frase para comprobar que las has escrito correctamente.



![Image](assets/fr/020.webp)



Un mensaje de advertencia te recordará que la aplicación está en versión beta y que Lightning Network sigue siendo una tecnología experimental. Obviamente, nunca comprometas cantidades en tu nodo Lightning que no estés dispuesto a perder.



A continuación, llegará a la interfaz principal de su nodo Lightning. A la izquierda, encontrará su Bitcoin onchain wallet alojada en su nodo. Esta es la generated de la frase de 24 palabras que acabas de guardar.



En el centro, encontrarás tu wallet de Lightning. En realidad representa tu efectivo saliente, es decir, los bitcoins que posees dentro de tus canales Lightning.



A la derecha, verás varios datos importantes sobre tu nodo:




- El número de conexiones y canales abiertos;
- Su flujo de salida total, es decir, lo que teóricamente puede gastar en iluminación;
- Su liquidez total entrante, es decir, lo que teóricamente puede recibir en Lightning.



![Image](assets/fr/021.webp)



Empecemos por personalizar nuestro nodo. Haz clic en los tres puntitos de la parte superior derecha de la interfaz y luego en `Configuración avanzada`. En el submenú `Personalización`, puedes definir un nombre público para tu nodo (evita usar tu nombre real) y elegir su color.



![Image](assets/fr/046.webp)



A continuación, haga clic en el botón verde "GUARDAR Y REINICIAR" para reiniciar el nodo y aplicar los cambios.



Tu nodo Lightning ya está listo para abrir sus primeros canales para realizar pagos. Pero antes, veamos cómo proteger tu sats



## Guardar el nodo Lightning


<chapterId>638fa75d-62af-4bf3-ab4a-b7d10ea75815</chapterId>



Antes de enviar su primera sats a su nodo, es importante entender cómo funciona su copia de seguridad y cuáles son los riesgos asociados. A diferencia de una simple cartera onchain Bitcoin, hacer una copia de seguridad de un nodo Lightning es bastante complejo: una estrategia equivocada puede provocar la pérdida permanente de tus fondos. En este capítulo, veremos qué es lo que realmente necesita una copia de seguridad, y cómo Umbrel gestiona este proceso con LND.



En este curso, utilizaremos la implementación LND (*Lightning Network Daemon*). Aunque los principios son similares en las otras implementaciones, los archivos de recuperación y los procedimientos de los que voy a hablar son específicos de LND.



### ¿Qué debo guardar en un nodo Lightning?



En un nodo Lightning, no basta con salvar la seed y esperar que todo vuelva a la normalidad. Varios elementos desempeñan papeles diferentes, por lo que es importante distinguirlos.



#### El seed (*aezeed*)



Al inicializar LND, recibe un seed de 24 palabras. Se trata de un formato específico de LND llamado "*aezeed*". No es un seed BIP39 clásico, aunque se parece mucho a uno. A partir de esta seed, LND obtiene las claves privadas de tus wallet onchain asociadas al nodo Lightning, es decir, las direcciones en las que puedes recibir o a las que puedes repatriar bitcoins tras el cierre de canales.



![Image](assets/fr/019.webp)



Por lo tanto, esta seed puede utilizarse para volver a crear la wallet onchain asociada a tu nodo, y para recuperar los fondos que ya han sido repatriados onchain (por ejemplo, tras el cierre de un canal). Por otro lado, la seed por sí sola no es suficiente para restaurar tus canales Lightning que siguen abiertos, ya que no contiene la información necesaria sobre el estado de tus canales.



#### La base de datos de canales (`channel.db`)



LND almacena el estado detallado de sus canales en una base de datos llamada `channel.db`. Esta base de datos contiene:




- la lista de sus canales abiertos;
- tus compañeros y sus identificadores;
- los últimos commitment transaction de cada canal (los estados sucesivos que definen quién posee qué en el canal y permiten recuperar los fondos onchain en caso de problema);
- la información necesaria para sancionar a un compañero que intente difundir un informe antiguo.



El problema de esta base de datos es que cambia constantemente: cada pago, cada enrutamiento, cada apertura o cierre de un canal modifica su contenido. Por eso, una copia de seguridad convencional (por ejemplo, una copia periódica de tu `channel.db`) es peligrosa. Si restauras una versión demasiado antigua de `channel.db` y reensamblas el nodo con este estado obsoleto, tus pares pueden considerar que estás transmitiendo un estado de canal antiguo. En este caso, el protocolo prevé una penalización: tu par puede recuperar la totalidad de los fondos del canal, como si hubieras intentado hacer trampas.



En la práctica, pues, `channel.db` no es un medio de copia de seguridad como tal. Es el estado vivo de tu nodo. La única situación en la que tiene sentido usarlo para restaurar tu nodo es cuando recuperas esta base de datos directamente de una máquina que acaba de fallar (por ejemplo, un disco que todavía se puede leer). En este caso, recuperas el estado más reciente y puedes reiniciar LND en otra máquina basándote en esta base de datos, con la seguridad de que este estado está lo más actualizado posible, ya que la máquina antigua ya no funciona. Otra situación en la que este método puede servir como copia de seguridad relevante es en una configuración de dos discos, con una copia dinámica y permanente de uno a otro. Sin embargo, este tipo de configuración es más compleja de implementar.



Pero hacer copias periódicas de `channel.db` y almacenarlas como copias de seguridad para restaurarlas más tarde es una muy mala idea: el día que las utilices, corres el riesgo de penalizarte y perder todo tu sats.



#### Canal estático de reserva (SCB)



Para hacer posible la recuperación de desastres, LND ha introducido el mecanismo *Static Channel Backup* (SCB). Se trata de un archivo especial, a menudo llamado `channel.backup`, que contiene información estática sobre tus canales: quiénes son tus compañeros, cómo contactar con ellos y cuáles son tus canales.



Este archivo no contiene el estado detallado del canal ni el historial de actualizaciones. No te permite reabrir canales en el estado exacto en el que estaban, ni continuar operando este nodo Lightning. Más bien, su papel es actuar como punto de anclaje para pedir a tus compañeros que te ayuden a cerrar limpiamente todos tus canales, y así recibir tu sats onchain, en claves que puedes recuperar gracias al seed. Así, a diferencia del archivo `channel.db`, que se modifica con cada pago o enrutamiento, el archivo SCB sólo se actualiza cuando se abre o cierra un canal.



Cuando se recupera a través de SCB, el proceso es el siguiente:




- Restauras tu seed (*aezeed*), que recrea tu wallet onchain asociado al nodo Lightning;
- Proporcione a LND su SCB más reciente;
- LND utiliza el SCB para encontrar la lista de tus compañeros y los canales que tienes con ellos;
- Se pone en contacto con cada peer, les dice que has sufrido una pérdida de datos y les pide que "fuercen el cierre" de tu canal con ellos, para que puedas recuperar tu parte de onchain.



La idea es que tus compañeros, al darse cuenta de que estás informando de una pérdida de datos, emitirán su último commitment transaction y cerrarán el canal de fuerza. Una vez confirmadas estas transacciones, tus fondos reaparecen en tu cartera onchain (vinculada a la seed).



Sin embargo, este mecanismo de recuperación no es perfecto. En primer lugar, no restaura el nodo Lightning, ya que se cierran todos los canales. Tendrás que construir un nuevo nodo Lightning desde cero. En segundo lugar, no garantiza una recuperación del 100%, aunque aumenta considerablemente las posibilidades de recuperar tus saldos onchain en caso de problema. En efecto, este protocolo de recuperación depende de la cooperación y disponibilidad de tus pares: si uno de ellos está desconectado, ha perdido sus propios datos o se niega a cooperar, tus fondos pueden permanecer bloqueados, o incluso perderse definitivamente. Por eso es importante no mantener canales abiertos en tu nodo Lightning con peers inalcanzables durante largos periodos de tiempo. Si sufres una pérdida de datos en ese momento y el peer permanece inalcanzable, la recuperación a través de SCB será imposible, y tus fondos permanecerán perdidos hasta que ese peer vuelva a estar en línea (quizás para siempre).



En resumen, una buena estrategia de copia de seguridad de Lightning en LND se basa en tres pilares:




- Su seed (*aezeed*), para la capa onchain;
- Copia de seguridad automática y fiable del SCB;
- Una buena gestión de los canales, eligiendo pares fiables y cerrando preventivamente los que suelen ser inalcanzables.



### ¿Cómo gestiona Umbrel la copia de seguridad de su nodo LND?



Umbrel ofrece un mecanismo simplificado de copia de seguridad para el nodo LND, basado precisamente en el SCB. La idea es ahorrarte el trabajo de manipular tú mismo este fichero, hacer una copia de seguridad del mismo y automatizar el proceso en la medida de lo posible.



Cuando creas tu nodo en Umbrel, recibes un seed que desempeña una doble función:




- deriva su Bitcoin onchain wallet asociado a su nodo Lightning;
- se utiliza para derivar un identificador de copia de seguridad y una clave de cifrado utilizada para las copias de seguridad remotas de SCB.



Gracias a este mecanismo, Umbrel realiza automáticamente una copia de seguridad encriptada de su SCB y la almacena en sus servidores a través de Tor. El SCB se almacena cifrado, gracias a una clave derivada de su seed. Así, en caso de pérdida de datos, todo lo que tienes que hacer es volver a crear un nodo Bitcoin y Lightning en Umbrel, en la misma máquina o en otra, y luego entrar en tu seed. Entonces podrás recuperar el último estado SCB de los servidores Umbrel, desencriptarlo e iniciar el proceso de recuperación de tus fondos.



Estas copias de seguridad son encriptadas localmente por su nodo antes de ser enviadas, lo que garantiza la confidencialidad de sus datos: Umbrel no puede leer el contenido del SCB. La transmisión se realiza a través de Tor, lo que impide que se filtre tu dirección IP. Además, tu Umbrel añade ruido al tráfico (relleno aleatorio y copias de seguridad falsas enviadas a intervalos irregulares) para impedir que el servidor deduzca con precisión cuándo abres o cierras un canal.



La principal ventaja de este método es que simplifica considerablemente la copia de seguridad de su nodo Lightning: sólo tiene que hacer una copia de seguridad de su seed una vez durante la inicialización del nodo. Esto conlleva cierto riesgo, ya que sólo es una copia de seguridad del SCB, pero para cantidades razonables es un compromiso aceptable.



### Buenas prácticas para limitar el riesgo de pérdidas



Incluso con una copia de seguridad de Umbrel, unas sencillas buenas prácticas pueden reducir en gran medida el riesgo de perderla:





- Controla la disponibilidad de tus compañeros:



Si un canal importante se asocia frecuentemente con un peer inalcanzable o inestable, es más seguro cerrarlo limpiamente mientras su nodo sigue funcionando. Un cierre cooperativo o forzado preventivo elimina una fuente potencial de problemas en caso de recuperación de SCB.





- Evite concentrar demasiada liquidez en pares desconocidos:



Cuanto mayor sea el canal que un peer tiene contigo, más importante es que sea fiable. Elige nodos serios, bien conectados y activos, para que cualquier recuperación futura a través de SCB pueda desarrollarse sin problemas.





- Complemente Umbrel con copias de seguridad locales:



Además de la copia de seguridad automática de Umbrel, también puede guardar una copia encriptada de su archivo SCB (`channel.backup`) en un medio externo y actualizarla periódicamente. Lo ideal es que lo renueves cada vez que abras o cierres un canal. Esto le da una solución de respaldo si, por alguna razón, el servicio de respaldo automático de Umbrel deja de estar disponible.





- Cómo gestionar correctamente su seed



Tu seed Umbrel no sólo restaura tu wallet onchain, sino que también obtiene la clave de cifrado para las copias de seguridad. Por tanto, un atacante con acceso a ella podría lanzar una recuperación y transferir tus fondos a su propia wallet, sin ni siquiera tener acceso físico a tu nodo.



Por lo tanto, si necesitas restaurar tu nodo pero ya no tienes tu seed, no podrás recuperar nada: toda tu sats se perderá. Por lo tanto, es muy importante que guardes tu seed con el máximo cuidado, sólo en soportes físicos (papel o metal), y que la conserves en un lugar seguro. Para más información sobre la gestión de una seed, consulta este tutorial:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### ¿Cómo guardo mi nodo Lightning en Umbrel?



Ahora que ya has entendido cómo funciona la teoría, vamos al grano. Desde tu aplicación Lightning Node (que en realidad es LND), haz clic en los tres puntitos de la esquina superior derecha.



![Image](assets/fr/022.webp)



Aquí hay tres elementos de interés para la copia de seguridad:




- Compruebe que la opción "Copias de seguridad automáticas" está activada. Esto enviará automáticamente tu SCB encriptado a los servidores de Umbrel.
- A continuación, puede elegir si desea enviar a través de Tor o clearnet, utilizando la opción `Backup over Tor`. Como se explica en las secciones anteriores, le recomiendo encarecidamente que utilice Tor para preservar su confidencialidad.
- Por último, hay un botón `Download channel backup file`, que le permite descargar a su ordenador un archivo `channel.backup`, es decir, una instantánea encriptada de su SCB. Esto le permite hacer copias de seguridad locales adicionales de vez en cuando, además de las que se envían automáticamente a los servidores de Umbrel.



Ahora ya sabe cómo proteger el sats de su nodo Lightning contra la pérdida de datos. En el próximo capítulo, veremos cómo proteger tu nodo contra intentos de engaño.




## Watchtower: función y configuración


<chapterId>e6c654dd-26c5-4e4d-8d11-a215bac37812</chapterId>



En Lightning, cada canal se basa en una secuencia de estados sucesivos, representados por commitment transaction inéditos. Con cada pago o enrutamiento Lightning, los 2 participantes en el canal construyen un nuevo par de commitment transaction, reflejando la distribución actual de fondos en el canal. Los commitment transaction antiguos quedan obsoletos.



Si una de las partes publica un estado desactualizado, la otra tiene derecho a sancionarla y recuperar la totalidad de los fondos del canal. En este capítulo, veremos brevemente cómo funciona este mecanismo y, a continuación, explicaremos cómo configurar una ***watchtower***: un sistema para proteger tu nodo Lightning de posibles intentos de engaño.



### Cómo funcionan las torres de vigilancia


En un momento dado, cada parte del canal dispone de un commitment transaction que, de publicarse, le permitiría cerrar el canal y recuperar su parte de los fondos. Este proceso se conoce como *cierre forzoso*. Pero si intentaran publicar una commitment transaction más antigua, correspondiente a un estado anterior del canal en el que tuviera más sats, entonces esta transacción se consideraría un intento de engaño. En este caso, la contraparte puede utilizar la clave de revocación asociada a este estado más antiguo para recuperar la totalidad de los fondos del canal, mientras que el tramposo queda temporalmente bloqueado por el bloqueo temporal.


Este sistema significa que publicar un estado antiguo, es decir, intentar hacer trampas, es muy arriesgado: si la otra parte ve esta transacción en el mempool o en la blockchain antes de que expire el timelock, puede utilizar la clave de revocación y recuperar todos los fondos. **Por lo tanto, la seguridad de tu canal Lightning depende de tu capacidad para detectar un intento de engaño dentro de la ventana de tiempo impuesta por el bloqueo de tiempo**.



#### ¿Por qué son necesarias las torres de vigilancia?



El mecanismo sancionador sólo funciona si la parte perjudicada puede hacerlo:




- controlar cada nuevo bloque Bitcoin para ver si se ha publicado un canal commitment transaction;
- determinar si esta transacción corresponde al último estado válido o a un estado revocado;
- en caso de revocación, emitir la transacción legal a tiempo, utilizando la clave de revocación para recuperar todos los fondos antes de que expire el bloqueo temporal.



![Image](assets/fr/023.webp)



En un escenario ideal, su nodo Lightning está en línea 24/7, está sincronizado y monitoriza continuamente la blockchain. Por esta razón, puede detectar por sí solo un intento de engaño y reaccionar. En la práctica, sin embargo, un nodo Lightning personal puede apagarse, sobre todo en caso de un corte de luz prolongado o un fallo de la conexión a Internet.



Es precisamente durante estos periodos de inactividad cuando el riesgo se hace real: si un peer deshonesto publica un estado antiguo mientras tu nodo está desconectado, y el timelock se agota sin ninguna reacción por tu parte, la trampa se hace efectiva. Pierdes parte o la totalidad de tus fondos en el canal.



Las Watchtower se introdujeron para reducir este riesgo. Una watchtower es un servicio externo que, monitoriza la blockchain en tu nombre, escaneando la posible publicación de un estado antiguo en uno de tus canales y, si es necesario, difunde automáticamente la transacción de penalización en tu nombre. Por lo tanto, incluso si su nodo Lightning permanece fuera de línea durante un período prolongado, siempre y cuando la torre de vigilancia que esté utilizando esté operativa, podrá proteger sus fondos supervisando cualquier intento de engaño y aplicando la penalización correspondiente, tan pronto como lo detecte.



#### Funcionamiento de una torre de vigilancia



Una torre de vigilancia está diseñada para minimizar la información que obtiene sobre sus canales, al tiempo que le proporciona los medios para actuar en caso de problema:




- Para cada nuevo estado de canal con un peer, tu nodo prepara por adelantado una transacción de penalización potencial. En caso de que este peer haga trampas, esta transacción te permitiría recuperar todos los fondos del canal;
- A continuación, su nodo encripta esta transacción de penalización utilizando el TXID de la commitment transaction correspondiente (la que se utilizaría si el tramposo intentara un fraude). Mientras no se produzca un cierre, la torre de vigilancia no puede descifrar esta transacción, ya que desconoce por completo el TXID de la transacción tramposa;
- Tu nodo envía a la torre de vigilancia un paquete que contiene la transacción de penalización encriptada y la mitad del TXID de la transacción potencialmente tramposa.



Como el TXID transmitido a la torre de vigilancia está incompleto, no puede descifrar la transacción de justicia. Sin embargo, puede monitorizar la blockchain en busca de un TXID que coincida con la parte que le pertenece. Si detecta una transacción de este tipo, entonces intenta utilizar el TXID completo de esa transacción para descifrar tu transacción de penalización. Si el descifrado tiene éxito, sabe que se trata de un intento de engaño y publica inmediatamente la transacción de penalización por ti.



![Image](assets/fr/024.webp)



Por tanto, la torre de vigilancia no tiene visibilidad de los detalles de tus canales: ni la identidad de tus pares, ni los saldos, ni la estructura de las transacciones. Sólo ve paquetes encriptados. La única información que puede deducir es el ritmo al que se actualizan tus canales, ya que recibe un paquete por cada nuevo estado, pero no puede conocer su contenido. En caso de trampas, seguramente descubrirá la información del canal descifrando la transacción de penalización, pero al menos tu sats se salvará.



Este mecanismo se basa en un compromiso: usted delega en la atalaya la capacidad de publicar una transacción de penalización previamente firmada, pero esta transacción permanece totalmente opaca a la atalaya hasta que se produce algún engaño. La atalaya no puede modificar los destinatarios ni desviar los fondos, ya que sólo dispone de una transacción ya firmada, con las salidas congeladas a tu favor. Tampoco puede conocer los detalles de un canal en un cierre legítimo forzado o cooperativo, ya que los TXID no coinciden. Por otro lado, watchtower sigue siendo un tercero de confianza mínima: tienes que confiar en que esté en línea y emita correctamente tu transacción de justicia cuando lo necesites.



#### Convertirse en una atalaya



En teoría, cualquier nodo Lightning puede actuar como torre de vigilancia para otros nodos (si utilizan la misma implementación, por ejemplo LND), mientras que él mismo está protegido por otros nodos que desempeñan este papel por él. En las siguientes secciones prácticas, te mostraré cómo configurar este sencillo mecanismo en tu LND bajo Umbrel.


En consecuencia, una estrategia interesante podría ser ponerse de acuerdo con amigos bitcoiners de confianza para que actúen como atalayas los unos de los otros. Tú vigilas sus canales y ellos los tuyos.



### Encontrar una atalaya altruista



Si no conoces a nadie a tu alrededor que pueda ofrecerte un servicio de atalaya, hay una serie de atalayas públicas altruistas a las que puedes conectarte. Por ejemplo, en este curso LNP202, te sugiero que te conectes al servicio de atalaya ofrecido conjuntamente por LN+ y Voltage, que es una atalaya para LND.


Aquí tienes los datos de acceso:



- Vía Tor:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



- A través de clearnet:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@34.216.52.158:9911
```

Para agradecerles que presten este servicio gratuito de vigilancia, [puede hacer una donación a través de Lightning](https://lightningnetwork.plus/donation).


Ahora que estamos utilizando un servicio de vigilancia altruista, vamos a ver cómo configurarlo en nuestro nodo LND bajo Umbrel.


### Instalar una torre de vigilancia


Desde la aplicación `Lightning Node`, haz clic en los tres puntos de la parte superior derecha de la interfaz y selecciona `Advanced Settings`.


![Image](assets/fr/025.webp)


A continuación, vaya al menú "Watchtower".


![Image](assets/fr/026.webp)



Active la opción `Watchtower Client` y pulse el botón `SAVE AND RESTART NODE`. Espere a que LND se reinicie.


![Image](assets/fr/027.webp)


Una vez completado el reinicio, vuelva al mismo menú e introduzca el ID de la atalaya altruista de su elección en el campo correspondiente. A continuación, pulse el botón `ADD` para confirmar. También puedes ajustar el parámetro `Watchtower Client Sweep Fee Rate`: es la tarifa que estás dispuesto a pagar por una posible transacción de justicia emitida por la atalaya. No es necesario elegir una tarifa excesivamente alta, pero también debe evitar una tarifa demasiado baja, ya que de lo contrario la transacción judicial no se confirmará a tiempo.


Reinicie su nodo utilizando el botón `SAVE AND RESTART NODE` para aplicar estos cambios.


![Image](assets/fr/028.webp)



Si vuelves a este mismo menú, verás que tu nodo Lightning está ahora protegido por la torre de vigilancia que acabas de añadir.



![Image](assets/fr/029.webp)



Una torre de vigilancia altruista suele ser suficiente, sobre todo si no colocas grandes cantidades de dinero en tu nodo Lightning y si gestionas bien tu nodo (no lo dejes apagado demasiado tiempo). Para una seguridad aún mayor, también puedes añadir varias repitiendo el mismo proceso.



## Abra su primer canal Lightning


<chapterId>00642af7-8f3d-4a25-96d7-34e85de7bd5d</chapterId>



Si has llegado hasta aquí, ya sabes que un nodo Lightning sin canal es un poco como una wallet vacía: existe, pero no sirve para nada. Para poder enviar o recibir pagos, tu nodo debe estar conectado al menos a otro nodo de la red Lightning a través de un canal. En el futuro, recomendamos encarecidamente abrir varios canales, por razones de resiliencia y eficacia de enrutamiento. En los siguientes capítulos, también veremos cómo gestionar tus activos líquidos, optimizar la topología de tus canales y utilizar herramientas más avanzadas que la interfaz básica de LND en Umbrel.



Pero en este capítulo introductorio, el objetivo es simplemente comprender cómo elegir un buen peer Lightning, dónde encontrar la información necesaria para seleccionar tus peers y, por último, cómo abrir tu primer canal a través de la interfaz básica de LND.



### ¿Cómo elegir un buen compañero Lightning?



Cuando abres un canal, tienes que elegir un peer: otro nodo Lightning con el que tu nodo estará directamente conectado, a través de un canal. Esta elección de peer es importante, ya que tendrá un impacto directo en:




- la facilidad para que sus pagos encuentren su camino;
- la fiabilidad de sus canales a lo largo del tiempo;
- sus costes de encaminamiento.



No existe la pareja perfecta para todo el mundo, pero hay una serie de criterios fiables para identificar a los buenos candidatos.



#### 1. Conectividad de nodos



Un buen peer es un nodo que está bien conectado a la red Lightning. Esto significa no sólo tener un gran número de canales (aunque esto puede ser un indicador), sino sobre todo estar conectado a otros nodos fiables y ocupar una posición suficientemente central en el grafo de la red.



Un nodo bien conectado aumenta las posibilidades de encontrar una ruta eficiente a la mayoría de los destinos de pago. También reduce el número de nodos intermediarios necesarios, lo que mantiene los costes bajos.



Por el contrario, abrir tu primer canal a un nodo aislado o débilmente conectado puede restringir tus posibilidades: podrás pagar a este peer, pero será mucho más difícil pagar al resto de la red.



#### 2. Capitalización y capacidad del canal



Un buen peer es también un nodo suficientemente capitalizado. Esto se demuestra por su capacidad total de canales (la suma de sats comprometidos en todos sus canales) y su capacidad media de canales (a menudo es mejor tener unos pocos canales bien capitalizados que muchos canales pequeños).



Un nodo con una capacidad ridícula, o cuyos canales sean todos minúsculos, no podrá enrutar pagos con importes elevados, lo que provocará fallos de enrutamiento para usted.



#### 3. Políticas de gastos



Cada nodo fija sus propias tarifas de enrutamiento (`tarifa base` y `tarifa de tarifa`). Un buen peer no cobrará tarifas exorbitantes por canales estratégicos. Para un primer canal, es mejor elegir un nodo con tarifas más bien moderadas, para no perjudicar tus propios pagos.



Recuerda que tus propias tarifas de enrutamiento también influyen en cómo te perciben los demás como par: un nodo que cambia constantemente sus tarifas o impone costes absurdos rara vez es apreciado.



#### 4. Estabilidad y antigüedad



La estabilidad de los nodos es un criterio muy importante. Un buen nodo tiene un tiempo de actividad alto (rara vez está fuera de línea), mantiene sus canales abiertos durante mucho tiempo y no abre/cierra canales constantemente sin motivo.



Los canales antiguos y aún activos son una buena señal: sugieren que la relación es rentable para el peer, que el nodo sabe gestionar su capital y que no cierra en cualquier momento, por lo que no hay que seguir pagando comisiones onchain por cierre y reapertura.



Por el contrario, un colega que a menudo está desconectado, o que cierra canales rápidamente, puede ser una fuente de problemas para usted, y de costes adicionales para abrir nuevos canales.



Incluso con estos criterios, no hará una elección perfecta a la primera. Es normal: la verdadera calidad de un compañero se revela con su uso. Por eso es importante:




- supervisar la actividad de los canales (volúmenes enrutados, disponibilidad, etc.);
- cerrar canales que no sirven para nada o cuyos compañeros están demasiado a menudo desconectados;
- reasignar su capital a pares mejores con el tiempo.



La idea no es abrir y cerrar canales todos los días (lo que resultaría caro en costes onchain), sino hacer evolucionar gradualmente tu topología hasta converger en un conjunto de pares fiables, bien conectados y compatibles con tus necesidades.



### ¿Cómo encuentro a un compañero?



Para aplicar estos criterios, necesitará herramientas que le proporcionen visibilidad de la red Lightning. Hay varios exploradores y servicios disponibles para ello. Entre los exploradores de Lightning más conocidos se encuentran [1ML](https://1ml.com/) y [Amboss](https://amboss.space/).



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017

https://planb.academy/tutorials/node/lightning-network/1ml-37ada2ab-7a24-4473-87fd-007cb7640e7b

En este caso, sin embargo, te sugiero que utilices [la herramienta Lightning Terminal de Lightning Labs](https://terminal.lightning.engineering/), que proporciona una clasificación (es cierto que basada en criterios parcialmente subjetivos) de los nodos Lightning considerados más relevantes para abrir un canal.



![Image](assets/fr/030.webp)



El problema con los nodos Lightning muy grandes que encabezan esta clasificación es que la mayoría no aceptan aperturas de canales por debajo de cantidades muy elevadas. Muchos también aplican estrictas políticas de gestión de pares, lo que puede provocar el cierre de tu canal. Por otro lado, estos nodos no suelen tener necesidad de liquidez entrante, dado su número de conexiones.



Por lo tanto, te aconsejo que vayas bajando en la clasificación hasta encontrar un nodo que esté bien conectado, sea fiable y ocupe una posición suficientemente central en el grafo de la red, sin ser excesivamente grande. Por ejemplo, aquí he identificado el nodo Lightning en stacker.news, que está muy bien conectado, tiene una gran capacidad y ocupa una posición central en el grafo de la red.



![Image](assets/fr/031.webp)



Otro enfoque interesante es abrir un canal hacia un nodo que necesite liquidez entrante, como un comerciante conocido, una asociación o una comunidad. Esta estrategia tiene tres ventajas:




- Dado que la entidad elegida necesita liquidez entrante, lógicamente tendrá menos incentivos para cerrar su canal sin motivo;
- Su actividad económica aumenta las posibilidades de encaminarse por este canal y, por tanto, de cobrar algunas tasas;
- Estás haciendo un favor al ecosistema y una valiosa contribución a otros bitcoiners.



Una vez que haya identificado un nodo relevante, puede recuperar su ID de Nodo. Esto es simplemente una concatenación de la clave pública del nodo, un separador `@`, su dirección IP o Tor, y el puerto utilizado. Este ID es fácilmente accesible desde el perfil del nodo en cualquier explorador Lightning.



### Abra su primer canal a través de LND



Ahora que hemos identificado el nodo con el que abrir nuestro primer canal, necesitamos que sats se bloquee en él. Para ello, es necesario alimentar el Bitcoin onchain wallet asociado con su LND.



Desde la interfaz principal de LND, localice su `Bitcoin Wallet`, luego haga clic en el botón `Depositar`. Una dirección receptora onchain es entonces generated: envíale sats. La cantidad que necesitas transferir depende de la capacidad que quieras asignar a tu primer canal, pero ten en cuenta que necesitas enviar algo más de la capacidad prevista. Por ejemplo, si quieres abrir un canal de 500.000 sats, no envíes exactamente 500.000 sats, sino una cantidad superior.



![Image](assets/fr/032.webp)



Una vez emitida la transacción, aparece en la interfaz. Espere la confirmación antes de abrir el canal. Verás una flecha verde al lado cuando esté confirmada.



![Image](assets/fr/033.webp)



Desplázate hasta la interfaz principal y haz clic en `+ ABRIR CANAL`.



![Image](assets/fr/034.webp)



Introduzca el `Node ID` del nodo con el que desea abrir un canal, indique la cantidad que desea bloquear y, a continuación, ajuste la comisión de apertura de la transacción según el estado del mercado de comisiones onchain. Por supuesto, asegúrate de tener fondos suficientes en tu cartera onchain LND de antemano.



Una vez configurados todos los parámetros, pulse el botón `OPEN CHANNEL`.



![Image](assets/fr/035.webp)



Espere a que la transacción de apertura se confirme onchain. Tu primer canal ya está oficialmente operativo: ¡enhorabuena!



Puedes ver que, por el momento, el 100% de la liquidez del canal está de mi parte: es normal, ya que soy yo quien ha abierto el canal. A medida que evolucionen los pagos y el enrutamiento, esta distribución cambiará, pero la capacidad total del canal seguirá siendo siempre la misma.



![Image](assets/fr/036.webp)



Ahora que ya tienes un canal, puedes realizar tus primeros pagos Lightning, siempre que el nodo elegido esté correctamente conectado a la red. Por supuesto, en capítulos posteriores veremos cómo configurar un método más cómodo para pagar facturas Lightning desde el móvil. Pero por ahora, vamos a intentar hacer un primer pago directamente desde LND a Umbrel.



Para ello, en la sección `Lightning Wallet`, haga clic en el botón `ENVIAR` y, a continuación, pegue la factura que desea configurar.



![Image](assets/fr/037.webp)



Aparecerá el importe de la factura. Confirme el pago pulsando el botón `ENVIAR`.



![Image](assets/fr/038.webp)



Si se encuentra una ruta válida, su primer pago relámpago debería tener éxito.



![Image](assets/fr/039.webp)



Si observamos la distribución de liquidez en el canal, vemos que mi par tiene ahora 5.002 sats en su lado. Esto corresponde a los 5.000 sats del pago que acabo de hacer, que él enrutó al nodo del destinatario. Los 2 sats adicionales representan las tasas de enrutamiento que pagué, ya que el receptor recibió exactamente 5.000 sats.



![Image](assets/fr/040.webp)



Para mejorar la fiabilidad de nuestros pagos, obviamente será necesario abrir otros canales. En función de nuestros objetivos, también tendremos que encontrar la manera de disponer de liquidez entrante para poder recibir pagos en Lightning. Este será el tema de la próxima sección.



# Gestión de su nodo Lightning


<partId>e27c3e1e-487b-4414-ad6b-d67bdb91c7c5</partId>



## Defina su perfil de operador de nodo


<chapterId>d3b2e163-50f6-4d1d-a5fc-8fd177dfac76</chapterId>



Ahora que su nodo Lightning está en funcionamiento, el siguiente paso es definir su perfil de operador. Se trata de una elección importante, ya que determina tu estrategia de apertura de canales, el tipo de pares que prefieres y la forma en que gestionas la liquidez.



En Lightning, para que esto funcione, necesitas liquidez en la dirección correcta. La liquidez saliente corresponde a tu capacidad de pago (sats disponible en tu lado de los canales). La liquidez entrante corresponde a tu capacidad de recibir (sats disponible en el lado de tus pares). En otras palabras, tu perfil se reduce a una simple pregunta: la mayor parte del tiempo, ¿tus sats salen de tu nodo o entran en él?



### El consumidor



Este es el perfil de la gran mayoría de usuarios. Utilizas tu nodo para realizar pagos con Lightning: para comprar bienes y servicios, pagar facturas, enviar propinas... en definitiva, para utilizar Lightning como medio de pago rápido. Por otro lado, recibes poco de Lightning, o sólo marginalmente, por ejemplo algunas donaciones, reembolsos entre amigos o algunos micropagos.



Este perfil es el más fácil de gestionar, porque su principal necesidad es poder pagar. En la práctica, esto significa que necesitas liquidez saliente. Una vez que hayas abierto uno o más canales del tamaño correcto a nodos estables y bien conectados, tus pagos salientes moverán mecánicamente liquidez al otro lado de tus canales. Es precisamente este movimiento el que crea de forma natural una cantidad razonable de liquidez entrante. Como resultado, incluso si no estás buscando recibir de forma regular, podrás recibir de vez en cuando sin necesidad de implementar una estrategia compleja. Así que no tiene que preocuparse por la liquidez entrante.



En este curso de LNP202, vamos a centrarnos en este perfil de operador de nodo "consumidor", ya que es el que corresponde a casi todos los usuarios de Bitcoin en Lightning.



### El minorista



El comerciante es, en cierto modo, lo contrario del consumidor. Aquí, el objetivo principal no es pagar, sino cobrar. Una empresa, proveedor de servicios, tienda online o punto de venta que acepte Lightning recibirá muchos pagos entrantes y realizará relativamente pocos pagos salientes desde este nodo.



Este perfil es más exigente, ya que un pago rechazado en Lightning representa potencialmente una venta perdida. Por tanto, la prioridad pasa a ser la liquidez entrante. Si tu nodo no tiene suficiente inbound, tus clientes verán cómo sus pagos fallan, aunque tengan los fondos, simplemente porque no hay una ruta para que la liquidez te llegue en la dirección correcta.



El mayor reto para el comerciante procede también de la evolución natural de los canales. Si todo lo que haces es recibir, tus canales se irán llenando poco a poco por tu parte. Así que necesita mecanismos para mantener y renovar su liquidez entrante.



Sin embargo, existe un caso más sencillo: el perfil mixto consumidor/comerciante. Si cobra en Lightning, pero también gasta en Lightning (gastos de empresa, pagos a proveedores, o incluso gastos personales), entonces sus pagos salientes recrean naturalmente los entrantes. La gestión se vuelve más fluida, ya que los flujos se compensan mutuamente, y tiene menos necesidad de recurrir a mecanismos artificiales diseñados únicamente para recuperar la liquidez entrante.



### El router



El enrutador es un perfil específico. No utiliza su nodo Lightning para pagar o cobrar, sino para encaminar los pagos de otras personas y cobrar comisiones. El objetivo es ser una ruta útil, fiable y económicamente competitiva dentro del grafo Lightning.



Para serte sincero, ser un router en Lightning es un negocio más complejo de lo que parece, y la rentabilidad es difícil de conseguir. En primer lugar, abrir y cerrar canales es caro en costes onchain. Para enrutar con eficacia, a menudo hay que ajustar la topología, hacer pruebas, cerrar canales de bajo rendimiento, abrir otros nuevos y reequilibrar periódicamente la liquidez. En segundo lugar, la competencia es feroz: los nodos grandes y consolidados acaparan gran parte del tráfico y es difícil hacerse un hueco sin invertir un capital considerable en canales de buen tamaño.



También hay un alto requisito operativo. Un nodo de enrutamiento debe ser extremadamente estable, estar supervisado, contar con copias de seguridad adecuadas y ser gestionado con rigor. Hay que vigilar el rendimiento de los canales, adaptar su política de tarifas, mantener una liquidez equilibrada, gestionar los pares y resolver rápidamente los problemas técnicos. Este nivel de implicación puede ser interesante como pasatiempo técnico o como contribución a la infraestructura, pero si tu objetivo es simplemente utilizar Lightning de forma soberana, meterte en el enrutamiento para ganar dinero rara vez es relevante. Por eso este curso LNP202 no cubre este perfil en profundidad.



### Sitúese claramente antes de seguir adelante



Si encajas en el perfil de consumidor, tu prioridad será poder pagar de forma fiable con una gestión sencilla. Si es usted comerciante, su prioridad será cobrar sin fallos, lo que implica una estrategia de adquisición de liquidez entrante. Si te planteas el encaminamiento, tendrás que enfocarlo como una actividad exigente, económicamente incierta y que requiere mucho tiempo.



Definir este perfil ahora le ayudará a evitar un escollo clásico: aplicar una estrategia de canal diseñada para un comerciante o un enrutador, cuando usted es simplemente un usuario que quiere pagar.



## Uso de un gestor de nodos Lightning


<chapterId>02eb4c09-d14b-4ff0-8b04-b90de3307d34</chapterId>



En la parte anterior de este curso de formación sobre LNP202, utilizamos la interfaz básica de la aplicación `Lightning Node` en Umbrel. Esta interfaz es suficiente para las operaciones esenciales (consulta de saldos, visualización de la distribución de efectivo, apertura y cierre de canales), pero está deliberadamente muy simplificada. Esta simplicidad limita las opciones disponibles y no da acceso a muchas de las funciones avanzadas de su nodo LND. Por este motivo, a continuación utilizaremos otro software de gestión de nodos Lightning más completo.



Este software adicional será simplemente una interfaz de gestión complementaria para su nodo. Esto significa que puede seguir utilizando la interfaz `Lightning Node` en paralelo, e incluso utilizar varias diferentes si lo desea. Se trata simplemente de distintas formas de interactuar con el mismo nodo Lightning.



Entre los programas informáticos más conocidos se encuentran:




- [Alby Hub](https://albyhub.com/);
- [Ride The Lightning](https://www.ridethelightning.info/);
- [ThunderHub](https://thunderhub.io/).



Las tres son buenas soluciones. Si lo desea, puede probar las tres con su nodo antes de elegir la que más le convenga. Personalmente, utilizo ThunderHub por costumbre y porque me parece más completa que las otras. Esta es la herramienta que presentaré en este curso de formación, pero también puedes elegir una de las otras dos alternativas. Tenemos un tutorial dedicado a cada uno de estos programas en Plan ₿ Academy.



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

### Instalar ThunderHub



Todos estos programas se pueden instalar muy fácilmente desde la App Store de Umbrel. Como he dicho, vamos a utilizar ThunderHub aquí, pero si desea probar otro más tarde, el procedimiento será similar.



![Image](assets/fr/041.webp)



Umbrel le proporciona una contraseña por defecto para acceder a ThunderHub. Cópiala: la necesitarás enseguida. Acuérdate también de guardarla en tu gestor de contraseñas, ya que te la pedirá cada vez que abras el programa.



![Image](assets/fr/042.webp)



Haga clic en `Iniciar sesión` y, a continuación, pegue la contraseña suministrada por Umbrel para iniciar sesión.



![Image](assets/fr/043.webp)



A continuación, accederá a la página de inicio de ThunderHub, que muestra la información principal sobre su nodo Lightning.



![Image](assets/fr/044.webp)



Para empezar, te recomiendo que actives la autenticación de dos factores (2FA). En los ajustes, solo tienes que hacer clic en "Activar" junto a "Activar 2FA" y seguir el proceso habitual.



![Image](assets/fr/045.webp)



### Utilizar ThunderHub



ThunderHub es relativamente fácil de aprender. Todos los menús son accesibles desde la columna izquierda de la interfaz. Para resumir, esto es lo que hace cada uno:




- inicio: visión general del nodo, balances y acciones rápidas;
- cuadro de mandos: cuadro de mandos personalizable con widgets y métricas;
- peers: ver y gestionar las conexiones con otros nodos Lightning;
- canales": gestión completa de los canales (liquidez, comisiones, cierre, etc.);
- rebalance": una herramienta para reequilibrar los canales mediante pagos circulares;
- transacciones: historial de los pagos relámpago enviados y recibidos;
- forwards`: estadísticas de enrutamiento y costes generated por su nodo;
- cadena Cartera onchain Bitcoin (UTXOs y transacciones);
- integración de gW-201 para supervisión y copia de seguridad;
- `Herramientas`: herramientas avanzadas (copias de seguridad, informes, macarrones, firmas, etc.);
- intercambio: Intercambio relámpago/en cadena a través de Boltz;
- `Stats`: estadísticas generales y rendimiento de tu nodo Lightning.



Con este conjunto de funciones, dispones de todas las herramientas necesarias para gestionar tu nodo Lightning de forma eficiente. No es imprescindible dominar todas las opciones en detalle de inmediato: las iremos explorando progresivamente a lo largo de este curso. Sin embargo, si quieres profundizar en el manejo del software, echa un vistazo a nuestro tutorial ThunderHub:



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

El menú que más nos interesa es "Canales". Ofrece una vista detallada de todos los canales de su nodo, con su distribución de liquidez. En concreto, puedes ver qué canales están abiertos en `Open`, cuáles están a la espera de ser abiertos o cerrados en `Pending`, y cuáles ya están cerrados en `Closed`.



![Image](assets/fr/047.webp)



Para un canal determinado, puedes hacer clic en el nombre del peer o en el ID del canal para abrir su página Amboss y obtener más información. También puedes hacer clic en el icono del lápiz para modificar los parámetros del canal, incluida la política de tarifas aplicada a ese canal si tu nodo enruta los pagos al nodo de tu peer.



![Image](assets/fr/048.webp)



Si utilizas tu nodo Lightning principalmente como "consumidor", no necesitas cambiar estos cargos: puedes mantener los valores por defecto. Por otro lado, si quieres entender mejor cómo funcionan los cargos de enrutamiento en Lightning, te recomiendo la formación LNP 201, y en particular el capítulo 4.1:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Haciendo clic en la pequeña cruz que aparece junto a un peer, puedes iniciar el cierre de un canal. Si observas, por ejemplo, que un peer está regularmente inactivo, puede ser conveniente cerrar este canal para reasignar tu capital a un peer más fiable.



Entonces tiene dos opciones. La primera, y siempre preferible, es el cierre cooperativo. Al confirmar esta acción, tu nodo pide a tu par que cierre el canal conjuntamente. Si acepta, puedes emitir la transacción de cierre onchain y recuperar tu parte de los fondos. Las ventajas de este método son que tú eliges las tarifas onchain de la transacción, evitando así costes innecesarios, y que los fondos se recuperan más rápidamente, sin ningún timelock.



![Image](assets/fr/049.webp)



La segunda opción es el cierre forzado. En este caso, no pides el acuerdo del peer y emites directamente la última commitment transaction en tu poder. Yo no recomendaría este método a menos que sea el último recurso, por ejemplo si el par rechaza sistemáticamente los cierres cooperativos o ya no responde. El cierre forzado tiene dos grandes desventajas: las comisiones suelen ser muy altas, ya que se han fijado de antemano para anticipar un aumento de las comisiones en la cadena, y hay un retraso en la recuperación de los fondos, ya que están bloqueados por un bloqueo temporal. Este timelock da a tu peer el tiempo necesario para reaccionar en caso de intento de engaño (que obviamente no es el caso aquí, pero aún así tienes que esperar).



![Image](assets/fr/050.webp)



Por último, para abrir un nuevo canal, vaya al menú "Inicio" y haga clic en "Abrir un canal" en la sección "Liquidity". A continuación, podrás introducir el ID del nodo elegido, la capacidad del canal, la tarifa de enrutamiento Lightning deseada y la tarifa onchain para la transacción de apertura.



![Image](assets/fr/051.webp)



Estas son las principales acciones que tendrá que realizar en ThunderHub. Descubriremos otras funciones a medida que avancemos en este curso LNP202.



## Obtención de liquidez entrante


<chapterId>b740c656-a897-4d95-af4b-116b718447cd</chapterId>



Como ves, disponer de liquidez saliente para realizar pagos en Lightning no es especialmente complejo. Basta con abrir canales por iniciativa propia a otros nodos y empezar a enviar sats. En cambio, disponer de liquidez entrante para recibir pagos en Lightning es más complicado, ya que o bien necesitas que otros nodos te abran canales, o bien tienes que mover tú mismo la liquidez realizando pagos.



Si adopta un perfil de "consumidor", por lo general no tendrá que preocuparse por la liquidez entrante. Su uso del nodo Lightning estará predominantemente orientado a los pagos, en lugar de a la entrada de efectivo. Simplemente realizando algunos pagos Lightning, crearás liquidez entrante de forma natural con el tiempo.



En cambio, si tiene un perfil de "comerciante", la situación es la inversa: se dedicará principalmente a cobrar pagos y a realizar pocos. Así que no puedes depender únicamente de tus propios pagos para recibir liquidez. Por lo tanto, se hace necesario que otros nodos Lightning abran canales a los tuyos. Pero, ¿cómo se consigue esto? ¿Cómo conseguir que otros operadores amarren capital para usted? Eso es precisamente lo que exploraremos en este capítulo.



### Compra de liquidez entrante



Como era de esperar, la forma más eficaz de conseguir que alguien actúe es pagarle. Para la entrada de liquidez en su nodo Lightning, el principio es exactamente el mismo. La forma más sencilla de conseguir canales para tu nodo es pagar por el servicio y la vinculación de capital que conlleva.



Si usted es una empresa o un minorista, este enfoque significa que puede obtener rápidamente canales fiables para cobrar los pagos de sus clientes sin fricciones.



Hay muchas formas de comprar liquidez entrante. La que yo personalmente utilizo y recomiendo es la plataforma [Magma](https://magma.amboss.tech/) de Amboss. Es muy fácil de usar, abrir un canal es rápido y las tarifas suelen ser razonables. Magma funciona como un mercado con creadores y tomadores, pero la versión 2 ha simplificado mucho la experiencia: basta con crear una solicitud, pagar el precio mediante Lightning y Magma la empareja automáticamente con la mejor oferta disponible. Tras seis confirmaciones onchain, tu canal con liquidez entrante está en marcha. Así es como funciona:



Vaya a [la página web de Magma](https://magma.amboss.tech/buy), en la sección `Comprar canales`.



![Image](assets/fr/052.webp)



Si lo desea, puede crear una cuenta para hacer un seguimiento de sus compras, pero no es obligatorio. Si no crea una cuenta, Magma simplemente le proporcionará un identificador de sesión, que le permitirá recuperar sus compras más adelante.



Una vez en el sitio, rellene la información necesaria para comprar liquidez. Seleccione "Una sola vez" para una compra única y, a continuación, introduzca la cantidad que está dispuesto a pagar por la liquidez entrante. Cuanto mayor sea la cantidad pagada, mayor será la capacidad del canal abierto a su nodo. A continuación aparece una estimación de la capacidad del canal: se trata de una aproximación, ya que el importe final dependerá de la mejor oferta encontrada por Magma, que a veces es mayor, a veces menor.



![Image](assets/fr/053.webp)



A continuación, introduzca su ID de nodo. Puede encontrarlo, por ejemplo, en el menú `Node ID` de la aplicación `Lightning Node` en Umbrel.



![Image](assets/fr/054.webp)



Una vez completada toda la información, haga clic en el botón "Revisar y abrir pedido".



![Image](assets/fr/055.webp)



Si no ha creado una cuenta, Magma le proporcionará una clave de sesión y un archivo de copia de seguridad. Guarde estos dos elementos en un lugar seguro, ya que le permitirán recuperar el pedido más adelante o seguir su estado en caso de problema. Una vez que haya guardado el archivo, haga clic en el botón "Pagar con Lightning".



![Image](assets/fr/056.webp)



A continuación, Magma emite una factura relámpago por el importe que hayas elegido. Debes pagarla. Si ya tienes canales en tu nodo Lightning, puedes pagar directamente desde él o utilizar otro wallet Lightning externo.



![Image](assets/fr/057.webp)



Una vez efectuado el pago, la transacción aparece como procesada en la interfaz Magma.



![Image](assets/fr/058.webp)



Transcurridos unos minutos, se procesará la solicitud: se abrirá un canal con sats a tu nodo Lightning. Una vez que la transacción de apertura haya sido confirmada onchain, tendrás acceso a la liquidez entrante correspondiente.



![Image](assets/fr/059.webp)



Magma también está integrado directamente en ThunderHub. En la pestaña `Home`, desplácese hasta la sección `Liquidity` y haga clic en `Buy Inbound Liquidity`. Todo lo que tiene que hacer es introducir la cantidad deseada y confirmar. No necesita pagar ninguna factura manualmente, ya que ThunderHub se encarga automáticamente del pago desde su nodo.



![Image](assets/fr/060.webp)



Si es usted comerciante, este tipo de servicio le conviene especialmente, ya que le permite obtener rápidamente una gran cantidad de liquidez entrante procedente de nodos fiables, lo que le garantiza que sus clientes podrán pagarle sin dificultad. Por otro lado, si usted es un particular, o si no desea pagar por la liquidez entrante, también existen soluciones gratuitas. Echemos un vistazo.



### Liquidez entrante cooperativa



Si no eres un operador, pero necesitas liquidez entrante (por ejemplo, para cebar tu nodo en el arranque, mientras esperas a que se realicen algunos pagos) no tienes por qué pagar por ella. Una de mis soluciones preferidas es cooperar con otros operadores de nodos que también necesiten liquidez entrante, para abrir canales Lightning entre ellos. De esta forma, la apertura de un canal te aporta liquidez saliente, al tiempo que te proporciona liquidez entrante, de forma gratuita (modulo comisiones onchain por apertura).



Por supuesto, puedes organizarlo directamente con otros bitcoiners. Sin embargo, existe una plataforma dedicada a este tipo de aperturas circulares: [Lightning Network +](https://lightningnetwork.plus/). El principio no es abrir dos canales entre las mismas personas, sino establecer aperturas circulares que impliquen a un mínimo de tres participantes, o incluso más.



Pongamos un ejemplo para entender cómo funciona Lightning Network +:




- Un operador de nodos, llamado `A`, publica un anuncio en el que afirma que desea abrir un canal sats de 1 millón con otras dos personas;
- El anuncio permanecerá activo hasta que se añadan más participantes;
- Más tarde, dos operadores, `B` y `C`, se unen al anuncio del nodo `A`. El triángulo ya está completo y puede comenzar la fase de apertura.
- El nodo "A" abre un canal al nodo "B";
- El nodo `B` abre un canal al nodo `C`;
- El nodo "C" abre un canal al nodo "A".



Al final de la operación, cada nodo tiene 1 millón de sats de liquidez saliente y 1 millón de sats de liquidez entrante. Este esquema puede ampliarse a cuatro o cinco participantes.



Por supuesto, no existe ningún mecanismo técnico que garantice que un participante abra realmente el canal que se ha comprometido a crear. Por eso la plataforma ha puesto en marcha un sistema de reputación, basado en valoraciones positivas cuando los operadores cumplen sus compromisos. Y en el peor de los casos, si te encuentras con alguien que no coopera, no habrás perdido dinero: simplemente habrás perdido una oportunidad de entrada de liquidez.



Esta solución es especialmente adecuada para un perfil de "consumidor", ya que le permite obtener liquidez entrante gratuitamente, al tiempo que conecta su nodo a otros pequeños operadores. En cambio, si eres un operador, este enfoque no suele ser pertinente: cada sáb de liquidez entrante requiere bloquear un sáb de liquidez saliente, y tus grandes necesidades de liquidez entrante implicarían entonces inmovilizar demasiado capital.



Para utilizar Lightning Network +, tiene dos opciones: o bien utilizar la aplicación integrada en Umbrel, o bien utilizar el sitio web clásico y crear una cuenta conectándose desde su nodo. Le recomiendo esta última opción, ya que la aplicación integrada no ofrece todas las funciones disponibles.



Vaya al sitio web [Lightning Network +](https://lightningnetwork.plus/) y haga clic en el botón `Login` situado en la parte superior derecha de la interfaz.



![Image](assets/fr/061.webp)



Para autenticarse, debe firmar el mensaje proporcionado utilizando la clave privada de su nodo Lightning. Con ThunderHub, esta operación es muy sencilla. Empieza por copiar el mensaje que muestra LN+.



![Image](assets/fr/062.webp)



En ThunderHub, vaya a la pestaña `Herramientas` y, a continuación, haga clic en el botón `Firmar` de la sección `Mensajes`.



![Image](assets/fr/063.webp)



Pegue el mensaje de autenticación proporcionado por LN+ y, a continuación, haga clic en `Firmar`.



![Image](assets/fr/064.webp)



A continuación, ThunderHub firma este mensaje utilizando la clave privada de tu nodo. Copia la firma de generated.



![Image](assets/fr/065.webp)



Pegue esta firma en el campo correspondiente del sitio LN+ y, a continuación, haga clic en `Iniciar sesión`.



![Image](assets/fr/066.webp)



Ahora está conectado a LN+ con su nodo Lightning. Este proceso permite a LN+ verificar que eres el propietario legítimo del nodo que estás reclamando en su plataforma.



![Image](assets/fr/067.webp)



Si lo desea, puede personalizar su perfil LN+, por ejemplo añadiendo una breve biografía.



Para participar en tu primera apertura de canal circular, ve al menú `Swaps` en la parte superior de la interfaz. Aquí encontrarás todos los intercambios disponibles en función de las características de tu nodo.



![Image](assets/fr/068.webp)



Para unirse a una oferta de intercambio existente, basta con hacer clic en ella y registrarse. Sin embargo, en LN+, el creador de un swap puede imponer ciertas condiciones a los participantes, como un número mínimo de canales o una capacidad total mínima del nodo. Por tanto, es posible, sobre todo en los primeros días, que haya pocas ofertas disponibles para tu nodo. En mi caso, a pesar de que ya había algunos canales abiertos, no había ofertas disponibles para mi nodo. Así que creé mi propio intercambio, y tú puedes hacer lo mismo si te encuentras en la misma situación.



Haga clic en "Iniciar Liquidity Swap" e introduzca los parámetros de su oferta:




- Elija el número total de participantes (3, 4 o 5);
- Indique la cantidad de canales que desea abrir (asegúrese de tener al menos esta cantidad en su wallet onchain);
- Define el tiempo de apertura de los canales. Es el periodo durante el cual los participantes acuerdan no cerrarlos;
- A la derecha, puede establecer restricciones para los participantes: número mínimo de canales, capacidad total mínima y tipo de conexión aceptada.



Una vez configurados todos los parámetros, pulse el botón `Start Liquidity Swap`.



![Image](assets/fr/069.webp)



Su oferta de intercambio ya está creada. Ahora sólo tienes que esperar a que se apunten otros operadores de nodos. Si sus condiciones no son demasiado restrictivas, no debería tardar demasiado. No olvide controlar el estado de su intercambio en las horas o días siguientes.



![Image](assets/fr/070.webp)



Ya se han ocupado todas las plazas de intercambio: ahora pasamos a la fase de apertura de canales. Cada participante puede ver, desde su interfaz LN+, hacia qué nodo tiene que abrir un canal Lightning.



![Image](assets/fr/084.webp)



Por tu parte, abre el canal utilizando el ID de nodo suministrado por LN+ y respetando la cantidad indicada. Como hemos visto en capítulos anteriores, puedes hacerlo a través de ThunderHub, con otro gestor de nodos Lightning o directamente desde la interfaz básica de la aplicación Lightning Node.



![Image](assets/fr/085.webp)



Una vez lanzada la apertura, podrás verla aparecer en la sección de canales en espera. En mi caso, es el canal con el nodo `Plebian_fr`.



![Image](assets/fr/086.webp)



A continuación, puede volver a LN+ para confirmar que ha iniciado la apertura de canales. Basta con hacer clic en el botón `Apertura de canal iniciada`.



![Image](assets/fr/087.webp)



Cuando todos los demás participantes hayan abierto también el canal al que se han comprometido, acuérdate de dejarles una reseña positiva.



![Image](assets/fr/088.webp)



En caso de dificultades o retrasos, puede ponerse en contacto directamente con sus compañeros a través de la sección de comentarios al final de la página.



![Image](assets/fr/089.webp)



Algunos participantes pueden desear reequilibrar los canales circulares desde el principio, haciéndose un pago a sí mismos. Esto garantiza una distribución equilibrada del efectivo en cada canal. Si estás en un perfil de "consumidor", esto no es esencial, pero puedes hacer este reequilibrio tú mismo si lo deseas, o poner temporalmente a cero las comisiones de tus canales para facilitar la tarea al compañero que quiera hacerlo. A veces nadie quiere hacerlo.



![Image](assets/fr/090.webp)




# Libere el potencial de su nodo Lightning


<partId>8dcc24b1-6eb9-4a5f-a56b-8a823e5ac0fd</partId>



## Conectar un wallet móvil a través de Tailscale


<chapterId>5fefb222-3f50-4f9d-a170-2ea628be4437</chapterId>



Eso es todo, ahora tienes un nodo Lightning bien conectado, con liquidez entrante y saliente. Así que ya está todo listo para utilizar su nodo Lightning en la vida real. Hasta ahora, siempre hemos utilizado interfaces directamente en Umbrel, ya sea la aplicación `Lightning Node` o la interfaz `ThunderHub`. Estas herramientas funcionan para enviar y recibir pagos, pero está claro que no están optimizadas para los pagos diarios con Lightning. La interfaz está diseñada para su uso en un ordenador, poco práctico en un smartphone, y además requiere una conexión a la misma red para funcionar correctamente (aunque técnicamente es posible conectarse remotamente a través de Tor).



En la práctica, lo que buscamos como bitcoiners es una interfaz Lightning wallet clásica en un smartphone: la posibilidad de escanear facturas mediante código QR, y una interfaz sencilla para pagar y cobrar sats. Esto es precisamente lo que implementaremos en este capítulo y en el siguiente. La idea general es tener una aplicación móvil Lightning wallet en tu smartphone, que pueda ser utilizada desde cualquier lugar (no sólo desde tu red local) pero que, en segundo plano, dependa de tu propio nodo Lightning para enviar y recibir pagos.



### ¿Cuáles son las soluciones para conectar a un cliente móvil?



Hoy en día, existen varios modos de hacerlo, tanto en lo que se refiere a la aplicación móvil como al tipo de conexión entre tu nodo y esta aplicación. Los tres principales modos de conexión son:




- vía ***Tor***;
- a través de VPN ***Tailscale***;
- a través de ***Nostr Wallet Connect***.



Hace unos años, solía conectarme a través de ***Tor***, pero dejé de hacerlo rápidamente: el número de fallos y los retrasos en la comunicación eran demasiado grandes. En teoría, funciona, pero en la práctica, la experiencia del usuario era catastrófica. Por tanto, desaconsejo este método.



La alternativa que adopté entonces fue utilizar una VPN ***Tailscale*** para garantizar la comunicación entre la aplicación móvil y el nodo. Esta solución funciona muy bien: incluso en redes móviles con bajo rendimiento, mis pagos siempre pasan sin dificultad. Este es el método que voy a presentar primero en este capítulo, con la aplicación Zeus.



En el próximo capítulo, veremos otra solución más reciente, que también funciona muy bien: ***Nostr Wallet Connect***. En esta ocasión, utilizaremos la aplicación Alby Go para presentarte una alternativa, aunque Zeus también es compatible con NWC si lo deseas.



### Instalación y configuración de Tailscale



Para este primer método, necesitaremos Tailscale. Se trata de una solución VPN basada en WireGuard, que permite conectar de forma segura dispositivos repartidos por Internet, al tiempo que gestiona automáticamente el cifrado, la autenticación y el cruce de NAT. En pocas palabras, es como si todos tus dispositivos estuvieran conectados a la misma LAN que tu router, aunque pudieran estar en cualquier lugar de Internet.



Para utilizarlo, cree primero una cuenta. Vaya al sitio web de Tailscale y haga clic en el botón "Empezar".



![Image](assets/fr/071.webp)



A continuación, elige un proveedor de identidad para tu cuenta Tailscale. Personalmente, utilicé una de mis cuentas de GitHub para iniciar sesión.



![Image](assets/fr/072.webp)



Una vez que te hayas conectado, se te harán algunas preguntas sobre tu uso. Respóndelas brevemente para continuar.



![Image](assets/fr/073.webp)



A continuación, Tailscale le ofrece instalar un cliente en su máquina. Por el momento, eso no es lo que nos interesa: vaya directamente a Umbrel e instale la aplicación Tailscale desde la App Store.



![Image](assets/fr/074.webp)



Cuando se abra la aplicación, haz clic en `Iniciar sesión` y sigue el proceso de autenticación, utilizando el mismo método que cuando creaste tu cuenta.



![Image](assets/fr/075.webp)



Haga clic en "Conectar" para confirmar. Su Umbrel está ahora conectado a su red VPN.



![Image](assets/fr/076.webp)



A continuación, descarga la aplicación Tailscale en tu smartphone e inicia sesión con la misma cuenta. Nota: en Android, no es posible utilizar dos VPN simultáneamente. Para que Tailscale funcione, tendrás que desactivar cualquier otra VPN activa. Además, cada vez que quieras utilizar tu nodo Lightning a través de Zeus, tendrás que activar la VPN Tailscale, de lo contrario no se establecerá la conexión.



![Image](assets/fr/077.webp)



En el sitio Tailscale, ahora que al menos dos clientes están conectados, puede acceder a la consola de administración con una lista de todos sus dispositivos conectados a la red y sus direcciones IP Tailscale.



![Image](assets/fr/078.webp)



### Conectar Zeus



Instale la aplicación Zeus en su teléfono. Cuando se abra, seleccione `Configuración avanzada` y, a continuación, `Crear o conectar una wallet`.



![Image](assets/fr/079.webp)



En la sección "Interfaz Wallet", seleccione "LND (REST)". A continuación, introduzca la dirección Tailscale de su Umbrel, que puede encontrar desde su panel Tailscale o directamente en la aplicación Tailscale en Umbrel. Para el puerto, introduzca "8080".



![Image](assets/fr/080.webp)



A continuación, Zeus te pide que le proporciones un `Macaroon`. Se trata de una autorización token que le permite definir con precisión los derechos concedidos a una aplicación (en este caso Zeus) para interactuar con su nodo Lightning. Es posible generate un macaroon desde ThunderHub, en el menu `Tools`, sub-menu `Bakery`, pero para este proposito, la manera mas facil es recuperarlo directamente desde la aplicacion `Lightning Node`.



Haga clic en los tres puntitos de la parte superior derecha de la interfaz y, a continuación, en `Conectar Wallet`. Elija `REST (Red local)`. A continuación, podrá copiar un macarrón con los derechos adecuados.



![Image](assets/fr/081.webp)



Pégalo en el campo correspondiente de Zeus y, a continuación, haz clic en el botón `SAVE WALLET CONFIG`.



![Image](assets/fr/082.webp)



Ahora puedes acceder a tu nodo Lightning desde la aplicación Zeus. Esto significa que puede generate facturas para recibir pagos directamente en su nodo Lightning desde su smartphone, y también pagar facturas Lightning donde quiera que esté.



![Image](assets/fr/083.webp)



Consejo: Tailscale no se limita a utilizar su nodo Lightning de forma remota. Le permite acceder a todas las herramientas de su Umbrel desde otro software, incluso de forma remota. Por ejemplo, puedes usar la dirección IP de Tailscale de tu Umbrel para conectar tu nodo Bitcoin (vía Electrs o Fulcrum) a Sparrow Wallet, sin pasar por Tor. Una vez más, esto evita la lentitud inherente a Tor. Simplemente instala el cliente Tailscale en tu ordenador y conéctalo a tu red.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

En el próximo capítulo, veremos otra forma igualmente eficaz de conectar un cliente móvil a su nodo Lightning: Nostr Wallet Connect. Utilizaremos una aplicación distinta de Zeus (aunque Zeus también es compatible con NWC), a saber, Alby Go.



## Conectar un wallet móvil a través de NWC


<chapterId>f5c97e43-e66e-4ba3-bcc9-fee1a04fc7f4</chapterId>



Si no te convence la conexión Tailscale, o si gestionar una VPN doble te parece demasiado engorroso, en este capítulo te proponemos otra forma de utilizar un cliente móvil remoto para pagar y recibir sats a través de tu nodo Lightning: ***Nostr Wallet Connect***.



Para este ejemplo, utilizaremos la aplicación móvil Alby Go, que está muy bien diseñada y es especialmente fácil de aprender. Dicho esto, también puedes utilizar Zeus o cualquier otra aplicación móvil compatible con NWC. Encontrarás una lista de aplicaciones compatibles en [el repositorio `awesome-nwc` GitHub](https://github.com/getAlby/awesome-nwc).



### ¿Cómo funciona Nostr Wallet Connect?



Nostr Wallet Connect es un protocolo estandarizado que permite a una aplicación o sitio web desencadenar acciones en un nodo remoto Lightning, sin establecer una conexión de red directa con ese nodo (sin API LND expuesta, sin VPN, sin servicio `.onion`...). NWC define cómo una aplicación formula una intención (por ejemplo, `pay_intece`) y recibe el resultado.



Su funcionamiento es bastante sencillo. Se inicia una sesión escaneando un código QR o mediante un enlace profundo `nostr+walletconnect:`. Esta cadena contiene los parámetros de la sesión y un secreto de autorización. A continuación, cuando la aplicación quiere pagar, serializa la solicitud, la cifra y la publica como un evento en un relé Nostr. El nodo lee el evento en el relé Nostr y lo envía a la aplicación. El nodo lee el evento en el relé, lo descifra, comprueba que el autor está autorizado para esta sesión, ejecuta el pago y devuelve una respuesta cifrada (éxito con preimagen o error). El relé sólo actúa como intermediario de transporte: no puede leer el contenido, pero sí observar el calendario y la frecuencia de las solicitudes.



Comparado con una conexión a través de Tailscale o Tor, la principal ventaja de NWC es que tu nodo no es directamente accesible desde el exterior. Esto simplifica enormemente el uso móvil: tu nodo no necesita aceptar conexiones entrantes, sólo necesita poder comunicarse con un relé. Por otro lado, introduce una dependencia funcional de los relés Nostr: si no están disponibles, la experiencia se degrada. Además, aunque los mensajes estén cifrados, el relé puede observar cierto nivel de metadatos de actividad.



La diferencia en los modelos de seguridad también es importante. Con Tailscale o Tor, expones el acceso directo a tu nodo (a través de API de LND) protegido por secretos altamente sensibles. Esto es potente, porque puedes administrarlo todo, pero también es una superficie de ataque de capa inferior. Con NWC, el acceso es más aplicativo: delegas una sesión token que autoriza sólo ciertas acciones.



### Instale Alby Hub en su nodo Lightning



Anteriormente, había una aplicación dedicada específicamente a las conexiones NWC en la App Store de Umbrel, pero lamentablemente ya no está disponible. Ahora tendrá que utilizar Alby Hub para establecer este tipo de conexión. Para ello, comience por instalar la aplicación Alby Hub directamente desde la tienda.



![Image](assets/fr/091.webp)



Al abrirlo, sáltate las pantallas introductorias y haz clic en el botón `Get Started (LND)`. Es importante comprobar que entre paréntesis pone `LND` y no `LDK`. Si aparece `LND`, significa que Alby Hub ha detectado correctamente el nodo Lightning existente y se configurará como interfaz para él. Por otro lado, si aparece `LDK`, esto indica que Alby Hub no ha detectado tu nodo y está a punto de crear uno nuevo, que no es el objetivo aquí.



![Image](assets/fr/092.webp)



A continuación, se le pedirá que cree una cuenta Alby. Para el uso limitado a NWC, esto no es necesario, pero puede que desee hacerlo si desea aprovechar los servicios específicos de Alby. Si no, haga clic en "Tal vez más tarde" para continuar.



![Image](assets/fr/093.webp)



A continuación, elija una contraseña fuerte y única. Esto protegerá el acceso a Alby Hub en su nodo. Recuerde guardarla en su gestor de contraseñas.



![Image](assets/fr/094.webp)



Esto le lleva a la interfaz Alby Hub. No necesita pasar por todo el proceso de configuración, a menos que quiera utilizarlo como administrador principal de su nodo Lightning. Como vimos antes, Alby Hub puede de hecho reemplazar el uso de ThunderHub para la administración de su nodo. Si quieres saber más sobre las opciones de Alby Hub, echa un vistazo a nuestro tutorial dedicado:



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Vaya al menú "Conexiones".



![Image](assets/fr/095.webp)



Aquí puede ver todas las aplicaciones que pueden conectarse a su nodo Lightning a través de NWC. Entre ellas se encuentra Zeus, ya mencionado en el capítulo anterior. Aquí usaremos Alby Go. Haga clic en Alby Go, luego en el botón `Connect to Alby Go` para iniciar el proceso de conexión.



![Image](assets/fr/096.webp)



### Instalación y conexión de Alby Go



En tu smartphone, instala la aplicación Alby Go:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Apple App Store](https://apps.apple.com/us/app/alby-go/id6471335774);
- [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq3jhml5fvklgnq9fxpete767txn9zfzqdkc0sxfptmnchfrexje7qqfxxmmd9enk2arpd338jtndda3xjmr9pzj5tk).



En Alby Hub, configure los derechos que desea conceder a la aplicación Alby Go en su nodo Lightning. Puede, por ejemplo, establecer límites de gasto por periodo, una fecha de caducidad para el enlace NWC, o dejar el control total. Una vez configurados los parámetros, pulse el botón `Siguiente`.



![Image](assets/fr/097.webp)



Alby Hub entonces generates un código QR para establecer la conexión NWC entre su nodo Lightning y Alby Go.



![Image](assets/fr/098.webp)



En la aplicación Alby Go, cuando se abra por primera vez, haga clic en `Conectar Wallet` y, a continuación, escanee el código QR suministrado por Alby Hub.



![Image](assets/fr/099.webp)



Elija un nombre para identificar esta wallet. Ahora tiene acceso remoto a su nodo Lightning a través de Alby Go. Puede generate facturas para recibir sats en su nodo, o establecer facturas Lightning directamente con él.



![Image](assets/fr/100.webp)



Por ejemplo, envié 1543 sats desde la interfaz Alby Go.



![Image](assets/fr/101.webp)



Si voy a la interfaz básica de mi nodo Lightning en Umbrel, puedo ver que este pago ha sido efectivamente realizado por mi nodo.



![Image](assets/fr/102.webp)



Ahora ya sabes cómo utilizar fácilmente tu nodo Lightning desde cualquier lugar.



## Autonomía de larga duración en Lightning


<chapterId>691a0942-b46d-482a-8fbc-fe19b3814992</chapterId>



Hemos llegado al final de este curso práctico LNP202. Ya tiene los conocimientos básicos que necesita para utilizar Lightning Network de forma soberana: comprende la función real de un nodo, las ventajas y desventajas de los distintos enfoques, y ha configurado una instancia de LND en Umbrel con una estrategia coherente de copia de seguridad y protección. También has abierto tus primeros canales, has aprendido a gestionar la liquidez, a hacer que tus pagos sean fiables a diario.



Desde un punto de vista operativo, tu nodo debería entrar ahora en un ritmo de mantenimiento. Lo principal es monitorizarlo (tiempo de actividad, sincronización, estado de los canales, fallos de pago, etc.), aplicar las actualizaciones que ofrece Umbrel cuando haya versiones estables disponibles y comprobar periódicamente que sus copias de seguridad y la configuración de la torre de vigilancia siguen activas.



En cuanto a los canales, adopte un enfoque pragmático: conserve los que le sean útiles, cierre los que estén permanentemente inactivos o asociados a pares inestables y reasigne gradualmente su capital hacia una topología más sólida.



**Uno de los errores más comunes en esta fase es asignar demasiado capital al nodo Lightning. Ten en cuenta que tu nodo Lightning es mucho menos seguro que un wallet de hardware, y que la disponibilidad de los fondos comprometidos en tus canales depende de mecanismos de respaldo que siguen siendo imperfectos. Por lo tanto, es muy importante que mantengas unas cantidades razonables, que puedas permitirte perder en caso de problema, y que mantengas siempre la mayor parte de tu sats en una wallet hardware onchain.



En cuanto a las herramientas, te recomiendo que sigas siendo curioso y atento a las novedades. En esta sesión de formación, hemos descubierto varias de ellas, ya sea para gestionar su nodo, su conectividad o su uso a distancia para realizar pagos. Sin embargo, Lightning es un campo especialmente dinámico. Cada año surgen herramientas nuevas y relevantes, y también aparecen muchas aplicaciones nuevas en Umbrel. Mantenerse al corriente de estas novedades puede permitirle descubrir soluciones más potentes o más prácticas que las presentadas en este curso.



En el plano educativo, si aún no lo ha hecho, le aconsejo encarecidamente que siga el curso teórico LNP 201 de Fanis Michalakis, dedicado al funcionamiento de la Lightning Network. Le ayudará a comprender mejor las manipulaciones realizadas en este curso LNP202 y le dará mayor confianza en la gestión cotidiana de su nodo. Le ayudará a comprender mejor las manipulaciones realizadas en este curso LNP202, y le dará mayor confianza en la gestión cotidiana de su nodo.



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

En otro orden de cosas, pero igual de esencial para tu viaje bitcoin, también recomiendo el excelente curso de Ludovic Lars sobre la historia de la creación del Bitcoin.



https://planb.academy/courses/a51c7ceb-e079-4ac3-bf69-6700b985a082

Pero antes de seguir adelante, puedes escribir una reseña de este curso LNP202 y, por supuesto, hacer el diploma para confirmar que has entendido todo su contenido.



# Parte final


<partId>683c998f-ba0a-4ffb-a7e8-4cd8369cb9b3</partId>



## Opiniones y valoraciones


<chapterId>aec048c7-7130-425d-8eca-9cd7f90c27f3</chapterId>



<isCourseReview>true</isCourseReview>

## Examen final


<chapterId>3951ccbb-14a3-4322-b81b-8dd2a6da19cb</chapterId>



<isCourseExam>true</isCourseExam>

## Conclusión


<chapterId>30cd6309-5139-40d9-8927-92de0f76414a</chapterId>



<isCourseConclusion>true</isCourseConclusion>