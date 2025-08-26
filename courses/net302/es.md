---
name: Redes IP, de la teoría a la práctica
goal: Domine los fundamentos de las redes IP para configurarlas mejor y solucionar sus problemas.
objectives: 


  - Comprender la arquitectura y el funcionamiento del protocolo TCP/IP
  - Explicar las diferencias, ventajas y limitaciones de IPv4 e IPv6
  - Identificar y distinguir los distintos tipos de IP Address
  - Configurar y verificar el direccionamiento IP en sistemas Unix/Linux
  - Utilizar las principales herramientas de diagnóstico para analizar y resolver problemas de red


---

# Habilidades esenciales para navegar por el mundo de la PI


Sumérjase en el corazón del mundo IP y equípese con los conocimientos necesarios para comprender y gestionar eficazmente sus redes. En este curso aprenderás todo lo que necesitas saber sobre redes informáticas de forma clara y práctica.


Aprenderá cómo funcionan las redes y el direccionamiento IP, a distinguir entre IPv4 e IPv6, a identificar y utilizar las distintas categorías Address y a comprender toda la importancia del protocolo TCP/IP y los vínculos que establece entre direcciones IP, direcciones físicas y nombres DNS.


NET 302 está dirigido principalmente a estudiantes, usuarios de Linux o simplemente curiosos que deseen comprender los fundamentos de las redes y reforzar su autonomía en la gestión, resolución de problemas y optimización de infraestructuras.


Únase a nosotros y convierta sus conocimientos en experiencia operativa real


___


Este curso NET 302 es una adaptación del curso *Fundamentos de redes: TCP/IP, IPv4 e IPv6*, redactado en francés por Philippe Pierre y publicado en [IT-Connect](https://www.it-connect.fr/cours/les-bases-du-reseau-tcpip-ipv4-et-ipv6/), bajo la licencia Creative Commons Attribution-NonCommercial 4.0 International ([CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)).



Se han introducido cambios sustanciales en la versión original de Loïc Morel: el texto se ha reescrito, ampliado y enriquecido por completo para ofrecer un contenido actualizado y profundo, conservando al mismo tiempo el espíritu pedagógico de la obra original de Philippe Pierre. También se han revisado los esquemas.


+++


# Introducción


<partId>a52b996d-1e23-470f-a9df-7ad88790099a</partId>



## Resumen del curso


<chapterId>9f238ecd-c9bb-4886-a205-2beba609fb13</chapterId>


Este curso proporciona una introducción completa a los fundamentos de las redes IP. Está estructurado en cuatro secciones principales, cada una de las cuales cubre un aspecto esencial para comprender, configurar y diagnosticar problemas en una red informática.


### Protocolo TCP/IP


En esta primera parte, sentaremos las bases explorando el concepto de red y la historia del protocolo TCP/IP. Estudiaremos sus principales componentes: IP, TCP, junto con un breve vistazo al protocolo QoS de IPv5. También trataremos las primitivas de servicio para comprender mejor la lógica de Exchange de datos.


### Direccionamiento IPv4


A continuación, pasaremos a un módulo dedicado al direccionamiento IPv4. Aprenderá cómo se utiliza IPv4 en la práctica, sus diferentes tipos de Address (privada, pública, broadcast, etc.), el papel fundamental del DNS, así como el funcionamiento de las direcciones Ethernet y del protocolo ARP. También descubrirá NAT (Network Address Translation) y los fundamentos de la configuración de redes.


### Direccionamiento IPv6


La tercera parte se centra en el direccionamiento IPv6, necesario para Address las limitaciones de IPv4. Repasaremos sus normas y definiciones, Address Assignment dentro de una red local, Address gestión de bloques y la relación entre IPv6 y DNS.


### Herramientas de diagnóstico de red


Por último, concluiremos con una presentación de las principales herramientas de diagnóstico de redes. Éstas le permitirán analizar, controlar y solucionar averías. Esta parte se estructurará por capas: Acceso a la red, Red, Transporte y Capas superiores.


Al finalizar este curso, dispondrá de los conocimientos fundamentales para administrar eficazmente una infraestructura de red y diagnosticar posibles problemas.


¿Listo para sumergirte en el mundo de las redes informáticas? Vamos allá


**NOTA**: Las descripciones se basan en un sistema GNU/Linux CentOS 7. Sin embargo, las configuraciones de red son en gran medida las mismas cuando se compara un sistema Debian con uno CentOS. Por tanto, no haremos ninguna distinción. Cuando haya alguna, la precederemos con un logotipo específico.


**N.B.**: Si durante el curso encuentra algún término que no le resulte familiar, consulte [el glosario](https://planb.network/resources/glossary) para obtener las definiciones.



# Protocolos TCP/IP


<partId>53fd4b73-cdf1-4865-ba29-1ac8ec3e9e9a</partId>



## ¿Qué es una red?


<chapterId>7370904f-f8f5-4ad4-a63a-5931d94c3b3b</chapterId>



En este primer módulo profundizaremos en el protocolo TCP/IP, piedra angular de las comunicaciones digitales modernas. Hablaremos de sus orígenes, sus principios fundamentales y el sistema de direccionamiento que utiliza, esencial para garantizar el flujo de información entre dispositivos conectados.


También detallaremos los principales componentes que estructuran este modelo y explicaremos cómo interactúan para formar una red operativa, fiable y escalable. Pero antes, es esencial volver al concepto de red.


Etimológicamente, una red se refiere a un conjunto de puntos conectados entre sí, formando una estructura interconectada. En telecomunicaciones e informática, esta definición se traduce en un conjunto de dispositivos (ordenadores, encaminadores, conmutadores, puntos de acceso, etc.) capaces de intercambiar datos a través de medios físicos o inalámbricos. Una red permite así el flujo continuo o intermitente de información, en función de las necesidades, de los protocolos utilizados y de la naturaleza de la arquitectura desplegada.


Con el tiempo, se han desarrollado varias topologías clásicas para satisfacer diferentes necesidades de coste, rendimiento, resistencia y facilidad de mantenimiento. Entre ellas figuran:


- red en anillo,
- red de árboles,
- red de autobuses,
- red de estrellas,
- red de malla.



### Red en anillo


En una topología en anillo, los dispositivos están conectados en un bucle cerrado: cada estación está enlazada con la siguiente, y la última se vuelve a conectar con la primera. En esta configuración, cada dispositivo actúa como un relé, pasando los datos al siguiente enlace. Según el tipo de red, la información puede circular en un solo sentido o en ambos.


La ventaja de esta disposición reside en la sencillez de su cableado y la ausencia de dependencia de cualquier equipo central. Sin embargo, la continuidad de toda la red depende de la salud de cada elemento individual: el fallo de una sola estación puede interrumpir todo el sistema de comunicación. Por eso se suelen establecer mecanismos de redundancia o derivación.



![Image](assets/fr/001.webp)



### Red de árboles


La red en árbol, o topología jerárquica, sigue el modelo de la estructura de un árbol genealógico. Consta de niveles sucesivos: un nodo raíz en la parte superior conecta con varios nodos de nivel inferior, que a su vez pueden conectar con otros nodos, y así sucesivamente.


Esta disposición jerárquica funciona especialmente bien en redes grandes que necesitan una clara división de responsabilidades y una gestión segmentada. Sin embargo, también hace que la red sea vulnerable al fallo de los nodos de nivel superior: la pérdida de la raíz o de una rama principal puede cortar secciones enteras de la infraestructura.



![Image](assets/fr/002.webp)



### Red de autobuses


En una topología de bus, todos los dispositivos comparten el mismo medio de transmisión, normalmente una línea coaxial o fibra óptica. Cada unidad está conectada de forma pasiva, es decir, no modifica activamente la señal, y puede enviar o recibir datos a través de este canal compartido.


La principal ventaja de la topología de bus es su bajo coste de instalación, gracias a la simplificación del cableado.  Sin embargo, en las antiguas implementaciones basadas en coaxial (Ethernet 10BASE2/10BASE5), la desconexión o pérdida de una sola estación podría interrumpir o incluso detener todo el tráfico, ya que la continuidad eléctrica del bus y la impedancia de terminación ya no se mantendrían. Disponer de un único medio físico es también una debilidad crítica: cualquier rotura o fallo interrumpe la comunicación de toda la red.



![Image](assets/fr/003.webp)



### Red de estrellas


La topología en estrella, también conocida como "hub and spoke", es la más común hoy en día, sobre todo en redes Ethernet domésticas y de oficina. En ella, todos los dispositivos se conectan a un único dispositivo central.


Esta disposición facilita la gestión y el mantenimiento: si falla un periférico, el resto de la red no se ve afectado. El inconveniente es que el dispositivo central es un único punto de fallo: si se cae, la comunicación se interrumpe en todas partes. La calidad de los cables y la longitud de los enlaces también deben tenerse muy en cuenta para mantener un buen rendimiento.



![Image](assets/fr/004.webp)



**Nota**: todavía existen redes organizadas en una topología lineal, tipo bus, en la que los equipos se conectan uno detrás de otro. Esta solución, aunque poco costosa de desplegar, tiene el gran inconveniente de que una sola rotura aísla algunos de los hosts, dividiendo la red en subconjuntos independientes.


### Red mallada


La red mallada está diseñada para ofrecer la máxima redundancia: todos los dispositivos están conectados directamente entre sí. Esto garantiza la continuidad del servicio aunque fallen varios enlaces o dispositivos, ya que el tráfico puede redirigirse por rutas alternativas.


La contrapartida es que el número de conexiones que hay que establecer aumenta rápidamente con el número de terminales. Para `N` puntos de conexión, se necesitan `N × (N-1) / 2` enlaces independientes, lo que hace que esta topología sea cara y compleja de desplegar. Por eso se utiliza principalmente en redes críticas que requieren una disponibilidad muy alta, como ciertas partes de Internet o sistemas industriales sensibles.



![Image](assets/fr/005.webp)



Existen otras variantes, como las redes grid o hipercubo, diseñadas para necesidades especializadas de computación distribuida o procesamiento paralelo.


A escala mundial, Internet es una interconexión masiva de redes que utilizan topologías diversas, unificadas por un direccionamiento común (IPv4 e IPv6) y un conjunto de protocolos normalizados definidos por el IETF (*Internet Engineering Task Force*). Esta diversidad hace que Internet no siga una topología única: su estructura es flexible, escalable e independiente del esquema de direccionamiento lógico que la hace utilizable.



## Los orígenes de TCP/IP


<chapterId>266b6864-8789-48d7-bc85-001cb9f1651f</chapterId>



Los orígenes del protocolo TCP se remontan a **ARPA** (*Agencia de Proyectos de Investigación Avanzada*, rebautizada "DARPA" en 1972), que lanzó el proyecto **ARPANET** en 1966. El primer segmento de ARPANET se puso en marcha en octubre de 1969, interconectando las universidades de UCLA y Stanford. El objetivo era enlazar los centros de investigación mediante una red de conmutación de paquetes que pudiera mantener las comunicaciones incluso en caso de fallo parcial de la infraestructura.


Como parte de esta dinámica, ARPA financió a la Universidad de Berkeley para que integrara los primeros protocolos TCP/IP en su sistema Unix BSD. Esto desempeñó un papel fundamental en la difusión y normalización del protocolo, primero en el mundo académico y más tarde en la industria.


**Nota**: en aquella época, los informáticos aún no disponían de Linux (que no aparecería hasta principios de los 90), ni de Minix, el sistema educativo diseñado por Andrew Tanenbaum.  Las principales opciones eran Unix o, a veces, mainframes propietarios como OpenVMS. Gracias a su flexibilidad y apertura, Unix fue decisivo para difundir los primeros conceptos de red.


En sentido estricto, TCP/IP no es un único protocolo, sino un conjunto de protocolos construidos en torno a TCP e IP. Alcanzó la fama porque ofrecía un Interface de programación estandarizado para el intercambio de datos entre máquinas de una misma red. Este Interface, basado en primitivas denominadas "sockets", permitía crear conexiones fiables y flexibles al tiempo que integraba protocolos de aplicación esenciales.


ARPANET es, por tanto, la base histórica de la actual Internet. En efecto, Internet es una red mundial basada en el principio de la conmutación de paquetes, en la que la información circula utilizando un conjunto de protocolos normalizados que garantizan la compatibilidad y la interoperabilidad entre sistemas heterogéneos. Esta arquitectura abierta ha permitido el desarrollo y despliegue de innumerables servicios y aplicaciones, entre ellos:


- correos electrónicos,
- la World Wide Web (www),
- transferencia e intercambio de archivos...


La gobernanza y evolución de estos protocolos están supervisadas por el ***Consejo de Arquitectura de Internet*** (IAB).

Esta organización coordina las direcciones técnicas a través de dos estructuras principales:


- IRTF** (_Internet Research Task Force_), que investiga a largo plazo la evolución y mejora de los protocolos.
- IETF** (_Internet Engineering Task Force_), que desarrolla, normaliza y documenta los protocolos operativos utilizados en Internet


La distribución de los recursos de red (rangos IP Address, números de sistema autónomo, nombres de dominio raíz, etc.) está coordinada internacionalmente por **IANA/ICANN**. La gestión operativa depende de **RIR** (*Regional Internet Registries*): **RIPE NCC** (Europa, Oriente Medio, Asia Central), **ARIN**, **APNIC**, **LACNIC** y **AFRINIC**.


Todas las especificaciones del protocolo TCP/IP se recogen en documentos denominados **RFC** (_Request For Comments_), que sirven como referencias técnicas autorizadas. Las RFC se actualizan y numeran continuamente para reflejar la evolución del conjunto de protocolos.


La pila TCP/IP suele representarse como una pila de cuatro capas funcionales, a menudo comparada con el modelo **OSI** (_Open Systems Interconnection_) de siete capas desarrolladas por la **ISO** (_International Standards Organization_), que sirve de referencia conceptual para las redes.


Las cuatro capas del modelo TCP/IP son:


- el NETWORK ACCESS Layer, que proporciona el enlace físico y los protocolos de control de acceso al medio;
- iNTERNET Layer, que gestiona el enrutamiento y el direccionamiento IP;
- el Layer TRANSPORTE, que garantiza la fiabilidad y la gestión de los flujos de datos que utilizan protocolos como TCP o UDP ;
- el Layer de APLICACIÓN, que agrupa protocolos de usuario y software como HTTP, FTP, SMTP y DNS.



![Image](assets/fr/006.webp)



Hoy en día, la versión más utilizada de IP es IPv4, pero su espacio Address de 32 bits tiene claras limitaciones. Esto llevó a la creación de IPv6, que utiliza un direccionamiento de 128 bits y ofrece una capacidad prácticamente ilimitada: esencial para soportar el crecimiento explosivo de los dispositivos conectados y afrontar los retos del Internet de las cosas, la movilidad y la seguridad.


Cada Layer de la pila TCP/IP proporciona servicios específicos, lo que hace posible Address diferentes necesidades de red de forma modular: transmisión física, direccionamiento lógico, integridad de datos y servicios a nivel de aplicación.


| Device example    | Description                                                                               | 	TCP/IP layer |
| ---------------------- | ----------------------------------------------------------------------------------------- | ----------------------- |
| Web server            | Application services closest to end users                                      | Application             |
| Gateway or proxy    | 	Encodes, encrypts, compresses useful data                                              | Application             |
| Session switch | Establishes sessions between applications                                               | Application             |
| Firewall or L4 router | Establishes, maintains, and terminates sessions between endpoint devices                  | Transport               |
| Router                | Globally addresses interfaces and determines optimal paths through a network | Network                  |
| Switch   | Locally addresses interfaces and forwards traffic via MAC                            | Network Access         |
| Network Interface Card (NIC)     | Signal encoding, cabling, connectors, physical specifications                        | Network Access         |

https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864

## Protocolo QoS IPv5


<chapterId>570ded19-be61-4005-844e-9490570a6455</chapterId>



La cabecera de un paquete IP es una estructura de datos esencial, dividida en varios campos, cada uno con una función específica para garantizar que los paquetes se transmiten y procesan correctamente mientras viajan por la red. Estos campos incluyen el IP Address de destino (necesario para encaminar el paquete a su destinatario), la longitud de la cabecera indicada por el campo IHL (*Internet Header Length*), la longitud total del paquete registrada en el campo *Total Length*, información de control y verificación, y otros parámetros para gestionar el flujo y la calidad de la comunicación.


El primer campo de la cabecera se denomina Versión. Este valor de 4 bits especifica qué versión del protocolo IP sigue el paquete. Es importante porque indica a cada enrutador o dispositivo intermedio cómo interpretar y manejar los datos encapsulados.


**Nota**: La gestión y asignación de las versiones de protocolos IP corresponde a la **IANA**. Un campo de 4 bits permite 16 combinaciones binarias (valores de 0 a 15). A día de hoy, su asignación es la siguiente:



| Version Number | Protocol   | Version Description         | Reference               |
| -------------- | ---------- | --------------------------- | ----------------------- |
| 0–1            | Reserved   | Reserved                    |                         |
| 2–3            | Unassigned | Unassigned                  |                         |
| 4              | IP         | Internet Protocol           | RFC 791                 |
| **5**          | **ST**     | **ST Datagram mode**        | **RFC 1190** / RFC 1819 |
| 6              | IPv6       | Internet Protocol version 6 | RFC 8200                |
| 7              | TP/IX      | The Next Internet           | RFC 1475                |
| 8              | PIP        | The P Internet Protocol     | RFC 1621                |
| 9              | TUBA       | Tuba                        | RFC 1347                |
| 10–14          | Unassigned | Unassigned                  |                         |
| 15             | Reserved   | Reserved                    |                         |

Entre ellos está IPv5, que, aunque en gran medida desconocido para el público, ya existía como ST (_Stream Protocol_). Desarrollado en los años 80, IPv5 se diseñó para Address una necesidad creciente en aquella época: proporcionar "_Calidad de Servicio_" (QoS) a determinados flujos de datos que requerían una transmisión continua y estable, como la Voz sobre IP o los flujos multimedia. Su objetivo era garantizar ancho de banda y prioridad de extremo a extremo, un concepto similar al que hoy ofrece el RSVP (_Protocolo de Reserva de Recursos_) para reservar dinámicamente recursos de red en los routers modernos.


Sin embargo, IPv5 siguió siendo experimental y sólo se implantó en un pequeño número de dispositivos de red. Su escasa adopción, unida a la creciente necesidad de más espacio Address, llevó a los diseñadores de Internet a pasar directamente de IPv4 a IPv6. Así se evitaron tanto las limitaciones de Address de IPv4 como cualquier riesgo de confusión o incompatibilidad con las especificaciones experimentales de IPv5.


Aunque IPv5 nunca llegó a utilizarse de forma generalizada, desempeñó un papel importante en las primeras ideas sobre calidad de servicio y gestión del tráfico. Hoy es más un marcador histórico que un estándar operativo.


**Recordatorio** - Un protocolo es un conjunto de reglas de comunicación: estructuras de datos, algoritmos, formatos de paquetes y convenciones que permiten que diferentes dispositivos Exchange información de forma fiable y comprensible. Un servicio es la implementación concreta de un protocolo a través de programas específicos (clientes, servidores) que siguen estas reglas y ponen la funcionalidad a disposición de usuarios y aplicaciones.


Ahora podemos examinar más de cerca la estructura y el funcionamiento del protocolo IP, la base esencial de toda comunicación en red.



## El protocolo IP


<chapterId>758fddbd-b652-4c18-bd1e-d038bd2e4d05</chapterId>



### Definiciones e información general


El protocolo IP, o "***Protocolo de Internet***", es la columna vertebral del modelo TCP/IP. Transporta paquetes de datos de un host a otro dentro de una red, ya sea local o mundial. Tiene dos funciones clave: gestionar el direccionamiento lógico de los dispositivos y garantizar el encaminamiento de los paquetes a través de redes a menudo heterogéneas e interconectadas.


A nivel físico, la transmisión se basa en interfaces de hardware para establecer conexiones punto a punto entre nodos. Sin embargo, es el protocolo IP el que hace posible la comunicación de extremo a extremo, dando a cada paquete la información que necesita para navegar por múltiples caminos posibles hasta su destino.


Tres Elements de configuración de red determinan cómo se envía un paquete en su camino:


- IP Address**: identifica unívocamente el host de destino en la red.
- Máscara de subred**: especifica qué parte de la Address identifica la red y qué parte identifica el host, lo que permite la división lógica en subredes.
- La pasarela**: indica el encaminador intermedio por el que debe pasar el paquete para llegar a una red externa o a otro segmento de la red local.


En Internet, los datos no fluyen como un flujo continuo, sino que se envían como **datagramas**: bloques independientes de datos, cada uno encapsulado con toda la información necesaria para su entrega. Este es el principio de la **conmutación de paquetes**, en la que la información se divide en unidades autónomas que pueden tomar distintos caminos para llegar al mismo destinatario.


Además de la carga útil (*payload*), cada datagrama IP contiene una cabecera estructurada con campos como el Address de destino, el Address de origen, el tipo de servicio, el número de versión del protocolo y otra información de control necesaria para gestionar la transmisión.


El tamaño máximo teórico de un datagrama IP es de **65.536 octetos**, límite fijado por el campo de longitud total de la cabecera. En la práctica, rara vez se alcanza este tamaño, ya que las redes físicas que transportan los paquetes (Ethernet, Wi-Fi, fibra óptica...) suelen imponer unos límites más estrictos conocidos como **MTU** (_Unidad Máxima de Transmisión_). Si un datagrama supera la MTU del enlace físico, debe dividirse en paquetes más pequeños, cada uno enviado por separado y reensamblado a su llegada.


Esta adaptabilidad hace del IP un protocolo robusto y flexible, capaz de funcionar con una amplia variedad de tecnologías subyacentes, manteniendo al mismo tiempo la compatibilidad universal entre sistemas y redes heterogéneos.



### Fragmentación de datagramas IP


Cuando un datagrama IP tiene que pasar por una red cuya capacidad de transmisión es menor que la del propio datagrama, hay que **fragmentarlo** para que pueda viajar sin problemas. Este límite de tamaño físico se denomina **MTU** (Unidad de Transmisión Máxima): el mayor tamaño de trama que puede pasar por una red determinada sin dividirse.


Cada tecnología de red impone su propia MTU, determinada por sus características de hardware y protocolo. Los valores comunes incluyen:


- ARPANET**: 1000 bytes
- Ethernet**: 1500 bytes
- FDDI**: 4470 bytes


Cuando un datagrama supera la MTU de un segmento de red que debe atravesar, el equipo de encaminamiento lo dividirá en **fragmentos** más pequeños que cumplan el límite. Esto suele ocurrir cuando se pasa de una red con una MTU alta a otra con una capacidad menor. Por ejemplo, un datagrama procedente de una red FDDI puede necesitar ser fragmentado antes de ser enviado a través de un segmento Ethernet.



![Image](assets/fr/008.webp)



El proceso de fragmentación funciona así:


- El router divide el datagrama en fragmentos que no superan la MTU de la red de destino.
- El tamaño de cada fragmento es múltiplo de 8 bytes, ya que el protocolo IP utiliza esta unidad para codificar el offset de reensamblado.
- Cada fragmento recibe su propia cabecera IP, que contiene la información que necesita el destinatario final para reensamblarlos en el orden correcto.


Una vez fragmentados, los trozos viajan independientemente por la red. Pueden tomar rutas diferentes, dependiendo de las tablas de enrutamiento, las cargas de los enlaces o las interrupciones. No hay garantía de que lleguen en el orden en que se enviaron.


A su llegada, la máquina receptora se encarga del **reensamblaje**. Utilizando la información de las cabeceras (identificador compartido, desplazamiento y banderas de fragmentación), vuelve a colocar los fragmentos en el orden correcto para reconstruir el datagrama original antes de transmitirlo al siguiente Layer. Si se pierde o corrompe aunque sólo sea un fragmento, normalmente se descarta todo el datagrama. Si se pierde o corrompe un solo fragmento, normalmente se descarta todo el datagrama, ya que sin cada uno de ellos el resultado sería incompleto o inutilizable.


Aunque eficaces, la fragmentación y el reensamblado tienen sus inconvenientes: procesamiento adicional para routers y hosts, y mayor probabilidad de pérdida de paquetes, lo que puede aumentar las retransmisiones. Por eso es importante gestionar con cuidado las MTU y optimizar el tamaño de los paquetes para que la comunicación IP sea fluida y eficiente.



### Encapsulación de datos


Para garantizar que los datos se encaminan correctamente a través de las capas del modelo TCP/IP, el proceso de **encapsulación** desempeña un papel clave. En cada etapa del viaje de un mensaje desde la aplicación del remitente hasta la máquina del destinatario, se añade información adicional, conocida como cabeceras. Estas cabeceras dan a los dispositivos intermedios y a las capas de software las instrucciones que necesitan para procesar, entregar y, si es necesario, volver a ensamblar los datos.


Cuando se envía un mensaje, éste pasa por las cuatro capas de la pila TCP/IP. En cada Layer, se añade una nueva cabecera delante de los datos existentes: cada cabecera contiene metadatos específicos, como direcciones lógicas o físicas, puertos de comunicación, números de secuencia, indicadores de control de errores y cualquier información necesaria para gestionar la transmisión y el enrutamiento.


La transmisión sigue así un proceso estructurado:


- La Aplicación Layer crea el **mensaje** inicial, que contiene los datos en bruto.
- El Layer de transporte lo encapsula en un **segmento**, añadiendo puertos de origen y destino, números de secuencia y mecanismos de control de flujo.
- Internet Layer añade al segmento una cabecera IP para formar un **datagrama**, especificando las direcciones IP de origen y destino.
- Network Access Layer envuelve el datagrama en una **trama**, añadiendo direcciones MAC y códigos de comprobación de integridad (CRC).



![Image](assets/fr/009.webp)



Este proceso de encapsulación garantiza tanto la integridad y trazabilidad de los datos como su adaptabilidad: al pasar de una red a otra, las cabeceras proporcionan a los dispositivos la información necesaria para elegir la ruta, comprobar la validez o realizar la fragmentación si es necesario.


A su llegada, el proceso se invierte: la máquina receptora recibe la trama en la Layer de Acceso a Red, que lee y elimina la cabecera correspondiente. A continuación, el datagrama pasa a la Layer de Internet, que lee la cabecera IP y la elimina a su vez para entregar el segmento a la Layer de Transporte. La Layer de Transporte procesa las cabeceras de transporte, comprueba la integridad del flujo y, finalmente, entrega el **mensaje** a la aplicación de destino en su estado original.



![Image](assets/fr/010.webp)



La transformación de los datos en cada Layer puede resumirse así:


- Mensaje**: bloque de información en la Aplicación Layer.
- Segmento**: unidad de datos una vez encapsulada por el Layer de transporte.
- Datagrama**: forma adoptada tras la adición de la cabecera IP por el Layer de Internet.
- Trama**: bloque final listo para su transmisión a través del medio físico por el Layer de acceso a la red.



![Image](assets/fr/011.webp)



Este proceso, esencial para la fiabilidad y universalidad de las comunicaciones por Internet, garantiza que cada dato, por fragmentado o complejo que sea, pueda transportarse de extremo a extremo sin dejar de ser comprensible y utilizable por la máquina receptora.



### Direccionamiento IP


Incluso con la conmutación de paquetes, la fragmentación y la encapsulación, una red no podría funcionar sin un sistema de direccionamiento fiable. Para garantizar que cada paquete de datos llega al destinatario correcto, Internet Layer utiliza un identificador único: el **IP Address**.

En IPv4, una IP Address se codifica en **32 bits** y se escribe como cuatro números decimales separados por puntos, en el conocido formato N1.N2.N3.N4 (por ejemplo: 192.168.1.12).


Una IP Address consta de dos partes:


- _netid_**: identifica la red a la que pertenece el host
- _hostid_**: identifica el host específico dentro de esa red

Esta separación permite estructurar lógicamente la Internet global en muchas redes interconectadas.


Históricamente, el sistema IPv4 se basaba en un esquema de clases, etiquetadas de la A a la E, que definían el rango de Address y su uso previsto. Cada clase asignaba un número determinado de bits al _netid_ y al _hostid_, lo que afectaba directamente al número posible de redes y hosts.



| **Class** | **IPv4 Address Range**            | **Usage**                    |
| --------- | --------------------------------- | ---------------------------- |
| A         | 1.x.x.x to 126.x.x.x              | Unicast addresses            |
|           | (127.x.x.x reserved for loopback) | Local loopback               |
| B         | 128.0.x.x to 191.255.x.x          | Unicast addresses            |
| C         | 192.0.0.x to 223.255.255.x        | Unicast addresses            |
| D         | 224.0.0.0 to 239.255.255.255      | IP Multicast                 |
| E         | 240.0.0.0 to 255.255.255.255      | Reserved for experimentation |

No todos los valores posibles pueden asignarse a los hosts. Por ejemplo, en una **clase C** Address, el último byte ofrece 8 bits (256 valores). Pero dos de ellos están reservados:


- 0: identifica la propia red
- 255: es el **broadcast** Address, utilizado para enviar un paquete a todos los hosts de la red a la vez.

Eso deja 254 direcciones utilizables para los dispositivos.


El número de direcciones disponibles varía mucho de una clase a otra: desde grandes redes públicas en la clase A, pasando por redes corporativas en la clase B, hasta redes locales más pequeñas en la clase C.



![Image](assets/fr/013.webp)



Algunos rangos de Address están reservados para uso privado y nunca se enrutan directamente en Internet. Se conocen como **direcciones privadas** y se utilizan dentro de organizaciones, empresas u hogares, y requieren la traducción de Address, normalmente NAT (*Network Address Translation*), para llegar a la Internet pública. Éstas son:


- Clase A**: de 10.0.0.0 a 10.255.255.255
- Clase B**: de 172.16.0.0 a 172.31.255.255
- Clase C**: de 192.168.0.0 a 192.168.255.255


Cuando un dispositivo con una Address privada accede a Internet, un router o pasarela con NAT la sustituye por una Address pública válida.


Ejemplo: Si un host tiene el Address **192.168.7.5**, podemos deducir:


- 192.168.7.0: red Address
- 192.168.7.1: a menudo el router local
- 192.168.7.5: el propio host


Otro caso especial es **127.0.0.1**, conocido como "***loopback***".

En sistemas Linux, está asociada a la Interface **lo**. Esta Address permite que una máquina se Address a sí misma para pruebas o diagnósticos locales, sin pasar por una Interface física. Todo el rango **127.0.0.0/8** está reservado para este propósito.


Para optimizar el uso de Address y diseñar redes complejas, la **máscara de subred** (_netmask_) es esencial. Esta máscara binaria separa el _netid_ del _hostid_ en una IP Address.

Cada clase tiene una máscara por defecto:


- 255.0,0,0** para la clase A,
- 255.255.0.0** para la clase B,
- 255.255.255.0** para la clase C.


Un buen diseño de red sigue una regla básica: los dispositivos que deben comunicarse directamente deben estar en la misma red o subred. Para segmentar una red, utilizamos la subred, dividiendo una red en subredes más pequeñas mediante el uso de una máscara más específica.


Ejemplo de subredes:

Una red **clase C**: 192.168.1.0/24 con una máscara por defecto de 255.255.255.0.

Queremos 4 subredes de hasta 60 hosts cada una.


**Paso 1**: Número de direcciones necesarias por subred = 60 + 2 direcciones reservadas (red + difusión) = 62.


**Paso 2**: Hallar la potencia más cercana de 2 ≥ 62. -> 2⁶ = 64.


**Paso 3: Ajuste la máscara. Mantener los bits _netid_ y reservar los bits _hostid_ necesarios. Obtenemos una máscara binaria que, una vez convertida, da **255.255.255.192**.


```
11111111 11111111 11111111 11000000
```


**Paso 4**: Calcular los rangos de Address para cada subred, variando los bits reservados para el host.



| Subnet ID (bits) | Subnet Address   | Subnet Mask     | Address Range                 | Broadcast Address |
| ---------------- | ---------------- | --------------- | ----------------------------- | ----------------- |
| 00               | 192.168.1.0/26   | 255.255.255.192 | 192.168.1.1 – 192.168.1.62    | 192.168.1.63      |
| 01               | 192.168.1.64/26  | 255.255.255.192 | 192.168.1.65 – 192.168.1.126  | 192.168.1.127     |
| 10               | 192.168.1.128/26 | 255.255.255.192 | 192.168.1.129 – 192.168.1.190 | 192.168.1.191     |
| 11               | 192.168.1.192/26 | 255.255.255.192 | 192.168.1.193 – 192.168.1.254 | 192.168.1.255     |


**Paso 5**: Esto crea cuatro subredes, cada una soportando hasta 62 máquinas, mientras se mantiene el esquema de direccionamiento global eficiente. La parte _hostid_ se divide en una parte _subnetid_ y una parte host.



![Image](assets/fr/016.webp)



Este principio fundamental de la división en subredes sigue siendo indispensable en la ingeniería de redes moderna, ya que permite una asignación IP precisa, un mejor control del tráfico, un fuerte aislamiento de segmentos y una gestión de red escalable.



### Direccionamiento CIDR


A principios de los 90, cuando Internet se extendió rápidamente por empresas y organizaciones, el sistema tradicional de direccionamiento IP basado en clases (A, B, C) empezó a mostrar sus límites.

Su rígida estructura provocaba un importante desperdicio de direcciones IP y hacía que las tablas de enrutamiento fueran cada vez más grandes, complejas y difíciles de mantener.

Para Address estos problemas, se introdujo un método más flexible y eficaz: **CIDR** (_Classless Inter-Domain Routing_). CIDR se ha convertido gradualmente en el estándar, sustituyendo en gran medida al antiguo sistema basado en clases.


La idea central de CIDR es la capacidad de agrupar varias redes adyacentes, especialmente bloques de clase C, en una única unidad lógica denominada **superred** (_supernet_). Con esta agregación, una sola entrada en la tabla de encaminamiento puede representar varias subredes, lo que reduce el número de rutas que deben manejar los encaminadores y mejora su rendimiento.


Aunque inicialmente las redes de clase C eran las que más necesitaban la agregación debido a su menor capacidad, el principio también se ha aplicado a las redes de clase B y, en teoría, incluso a las de clase A, aunque estas últimas se ven menos afectadas gracias a su gran alcance Address.


Con CIDR, el concepto de clases fijas desaparece. El espacio Address se trata como un rango continuo que puede dividirse o agregarse según sea necesario. Los bloques CIDR se definen mediante máscaras de subred que no se limitan a las clases A, B o C predeterminadas. Un bloque CIDR puede representar una única red o un conjunto contiguo de subredes que comparten el mismo prefijo.


Un bloque CIDR se escribe con el formato "Address/prefijo", en el que el número después de la barra indica cuántos bits componen la parte de red. Por ejemplo, /17 significa que los primeros 17 bits identifican la red, mientras que los 15 bits restantes identifican los hosts.


Ejemplo:

Un bloque /17 contiene 2^(32-17) direcciones, por lo que 2^15 = 32.768 direcciones totales. Restando las dos direcciones reservadas (red y difusión) quedan 32.766 direcciones host utilizables. Esto permite a los administradores de red dimensionar sus subredes con precisión para que se ajusten a las necesidades del mundo real, evitando derroches innecesarios.


Para que el dimensionamiento CIDR sea más fácil de entender, aquí tienes una tabla de prefijos comunes y sus equivalentes máscaras de subred y direcciones utilizables:


| CIDR Prefix | Available Host Bits | Subnet Mask     | Usable Host Addresses         |
| ----------- | ------------------- | --------------- | ----------------------------- |
| /8          | 24                  | 255.0.0.0       | 2^24 - 2 = 16,777,214         |
| /12         | 20                  | 255.240.0.0     | 2^20 - 2 = 1,048,574          |
| /16         | 16                  | 255.255.0.0     | 2^16 - 2 = 65,534             |
| /20         | 12                  | 255.255.240.0   | 2^12 - 2 = 4,094              |
| /24         | 8                   | 255.255.255.0   | 2^8 - 2 = 254                 |
| /26         | 6                   | 255.255.255.192 | 2^6 - 2 = 62                  |
| /27         | 5                   | 255.255.255.224 | 2^5 - 2 = 30                  |
| /28         | 4                   | 255.255.255.240 | 2^4 - 2 = 14                  |
| /29         | 3                   | 255.255.255.248 | 2^3 - 2 = 6                   |
| /30         | 2                   | 255.255.255.252 | 2^2 - 2 = 2                   |
| /31         | 1                   | 255.255.255.254 | 2^1 = 2 (point-to-point only) |
| /32         | 0                   | 255.255.255.255 | 1 (host address only)         |


**NOTA**: Históricamente, el RFC 950 desaconsejaba el uso de la subred cero, principalmente para evitar confusiones en el encaminamiento.  Esta restricción quedó obsoleta con el RFC 1878, que permite plenamente su uso. La antigua limitación se debía principalmente a la incompatibilidad con hardware antiguo que no podía manejar CIDR correctamente. Los equipos modernos no tienen ese problema.


Por ejemplo, la subred **1.0.0.0** con la máscara de subred **255.255.0.0**, antes ambigua con el identificador de red de clase A, es ahora perfectamente válida y utilizable.


**TIP**: para calcular subredes sin errores y convertir rápidamente las direcciones a la notación CIDR, existen herramientas muy prácticas como ***ipcalc***. Esta "calculadora de redes" muestra claramente los desgloses de Address, los rangos disponibles y las máscaras asociadas, ideal tanto para administradores como para estudiantes que aprenden CIDR.


```shell
sudo apt install ipcalc
```


https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d

## El protocolo TCP


<chapterId>860bf7d5-a502-4d10-a12c-9827f6c2d393</chapterId>



El protocolo **TCP** (_Transmission Control Protocol_) desempeña un papel central en el Layer de TRANSPORTE del modelo TCP/IP. Actúa como puente entre las aplicaciones e Internet Layer, garantizando la transferencia fiable de datos entre dos máquinas distantes.

Mientras que el protocolo IP se limita a enviar paquetes sin garantizar la entrega ni el orden, TCP asegura la integridad y coherencia del flujo de datos, entregándolos sin pérdidas, en el orden correcto y sin duplicados.


Entre las principales responsabilidades de TCP se incluyen:


- Reordenación de los segmentos recibidos;
- Supervisión del flujo de datos para evitar congestiones;
- Dividir o reensamblar bloques de datos en unidades adecuadas (segmentos);
- Gestionar el establecimiento y la finalización de las conexiones entre ambos extremos de la comunicación.


TCP es un protocolo orientado a la conexión, lo que significa que establece una relación explícita y continua entre cliente y servidor. Para ello, utiliza **números de secuencia** y **acuses de recibo**: a cada segmento enviado se le asigna un identificador único para que la máquina receptora pueda comprobar tanto el orden como la integridad de los datos. A continuación, el receptor devuelve un segmento de acuse de recibo con el indicador **ACK** a 1, confirmando la recepción e indicando el siguiente número de secuencia previsto.



![Image](assets/fr/018.webp)



Para mejorar la fiabilidad, TCP utiliza un temporizador: una vez enviado un segmento, se inicia una cuenta atrás. Si no llega un acuse de recibo dentro del tiempo de espera, el remitente retransmite automáticamente el segmento, suponiendo que se ha perdido en tránsito. Este mecanismo de retransmisión automática compensa las pérdidas inherentes a las redes IP, que pueden producirse en casos de congestión, errores de encaminamiento o fallos de hardware.



![Image](assets/fr/019.webp)



TCP es capaz de detectar y manejar duplicados. Si llega un segmento retransmitido pero también aparece el original, el receptor utiliza los números de secuencia para identificar el duplicado y quedarse sólo con la copia correcta, eliminando cualquier ambigüedad.


Para que este proceso funcione, ambas máquinas deben tener en común sus números de secuencia iniciales. Esto se garantiza siguiendo un estricto procedimiento de conexión: por un lado, el **servidor** escucha en un puerto específico, a la espera de una solicitud entrante (modo pasivo); por otro, el **cliente** inicia activamente la conexión enviando una solicitud al servidor en el mismo puerto de servicio.


**NOTA**: Un "puerto" es un identificador numérico (de 0 a 65.535) asignado a una aplicación de red en un ordenador. Se utiliza para diferenciar varios servicios que se ejecutan simultáneamente en la misma IP Address. Cuando un cliente envía datos, especifica el número de puerto para que el sistema operativo del servidor sepa qué programa debe recibirlos (por ejemplo, 80 para HTTP, 443 para HTTPS, 25 para SMTP). Los puertos actúan como puertas dedicadas, dirigiendo el tráfico de entrada y salida, evitando la confusión entre servicios y permitiendo un control de acceso detallado mediante cortafuegos o reglas de filtrado.


La sincronización de secuencias Exchange se basa en el famoso mecanismo **"*three-way handshake*"**, similar a la forma en que dos personas se saludan para establecer contacto. Esta fase de inicialización, que garantiza la fiabilidad de TCP, tiene lugar en 3 etapas:

1. **SYN:** El cliente envía un segmento de sincronización inicial (**SYN**) con el indicador apropiado activado y un número de secuencia inicial (por ejemplo, C);

2. **SYN-ACK:** El servidor receptor responde con un segmento de acuse de recibo (**SYN-ACK**), reconoce el número de secuencia del cliente y proporciona su propio número de secuencia inicial;

3. **ACK:** El cliente envía un acuse de recibo final (**ACK**) confirmando la recepción del número de secuencia del servidor, finalizando la sincronización. La bandera SYN está ahora desactivada y la bandera ACK permanece activada indicando que la conexión está establecida.



![Image](assets/fr/020.webp)



Este protocolo Exchange garantiza que ambas partes comparten la misma base de numeración antes de transmitir los datos de la carga útil. Una vez completada esta sincronización, se abre la sesión: ahora los segmentos pueden viajar en ambas direcciones, cada uno con acuse de recibo, lo que garantiza la máxima fiabilidad del flujo de datos.


Este ***handshake de tres vías*** sólo afecta al establecimiento de la conexión. Para el cierre, TCP utiliza un *handshake de cuatro vías*: FIN → ACK → FIN → ACK, que garantiza que no se pierda ningún segmento en tránsito antes de que se libere completamente la conexión.


Aunque diseñado para ser robusto y fiable, este proceso también ha dado lugar a vulnerabilidades explotables. Por ejemplo, ataques como el **IP Spoofing** pretenden eludir o corromper esta relación de confianza haciéndose pasar por una máquina autorizada mediante números de secuencia falsificados, creando una brecha que permite interceptar o manipular el flujo de datos.


Para limitar los riesgos de secuestro de la sincronización de secuencias y gestionar la carga de la red, el protocolo TCP utiliza una técnica de gestión de flujos conocida como "**_Sliding Window_**". Este sistema regula la cantidad de datos que pueden enviarse sin exigir un acuse de recibo inmediato para cada segmento, reduciendo así la sobrecarga innecesaria de la red y manteniendo al mismo tiempo una buena fiabilidad.


En la práctica, la ventana deslizante define un rango de números de secuencia que pueden circular libremente entre el emisor y el receptor sin que se acuse recibo de cada segmento individual. A medida que el sistema emisor recibe acuses de recibo, la ventana "se desliza": se desliza hacia la derecha dejando espacio para que se envíen nuevos segmentos. El tamaño de esta ventana (fundamental para optimizar el rendimiento y evitar la congestión) se especifica en el campo "*Window*" de la cabecera TCP.


**Ejemplo**: si el número de secuencia inicial es 3 y la ventana se extiende hasta la secuencia 5, los segmentos numerados del 3 al 5 pueden enviarse sin esperar acuses de recibo individuales.



![Image](assets/fr/021.webp)



El tamaño de la ventana deslizante no es fijo; se ajusta dinámicamente a las condiciones de la red y a la capacidad de procesamiento del receptor.  Si el receptor puede manejar un mayor volumen de datos, lo indica a través del campo Ventana, incitando al emisor a ampliar su ventana. A la inversa, en caso de sobrecarga o riesgo de saturación, el receptor puede solicitar una reducción, el emisor esperará a que la ventana avance para enviar segmentos adicionales.


El protocolo proporciona un procedimiento simétrico para cerrar una conexión TCP con el fin de garantizar un cierre limpio y ordenado. Cualquiera de las máquinas puede iniciar el cierre enviando un segmento con la bandera **FIN** a 1, señalando su intención de terminar la comunicación. A continuación, espera hasta que se hayan recibido todos los segmentos en tránsito e ignora cualquier dato adicional.


Al recibir este segmento, la otra máquina envía un acuse de recibo, también marcado con la bandera FIN. A continuación, termina de enviar los datos restantes antes de informar a la aplicación local de que la conexión se ha cerrado. Esta doble confirmación garantiza un cierre ordenado y minimiza el riesgo de pérdida de datos.


Esta gestión precisa, que combina el encaminamiento flexible de IP con el control estricto de TCP, se ilustra a menudo mediante un diagrama que contrasta la velocidad del protocolo IP (que funciona sobre una base de **"mejor esfuerzo "**, sin garantía de entrega) frente a la fiabilidad del protocolo TCP (que gestiona la transmisión mediante acuses de recibo y secuencias negociadas).



![Image](assets/fr/022.webp)



En algunos casos, sin embargo, la fiabilidad absoluta no es la prioridad: lo son la velocidad y la sencillez. Es el caso de aplicaciones como el streaming en directo o la VoIP, que pueden tolerar cierta pérdida de paquetes sin afectar gravemente a la experiencia del usuario. En estos casos, se prefiere el **UDP** (_Protocolo de Datagramas de Usuario_).


UDP funciona según un principio fundamentalmente distinto de TCP: es **sin conexión**, lo que significa que no se establece ninguna relación previa entre emisor y receptor. Cuando una máquina envía paquetes a través de UDP, éstos se transmiten en un solo sentido; el receptor no envía acuses de recibo, y el emisor no tiene confirmación de que el mensaje haya llegado. La cabecera UDP es intencionadamente mínima, conteniendo sólo el puerto de origen, el puerto de destino, la longitud del segmento y una suma de comprobación, sin acuse de recibo incorporado ni mecanismo de control de estado. Como siempre, las direcciones IP son transportadas por la cabecera IP subyacente.


Una analogía común es que TCP es como una **llamada telefónica**, donde se establece un circuito, que se sigue y controla a lo largo de la conversación. Mientras que el protocolo UDP es como **enviar un correo**, donde el remitente desliza una carta en un buzón sin prueba inmediata de entrega ni respuesta sistemática.


Esta complementariedad entre TCP y UDP permite a las redes modernas adaptarse a diversas necesidades, optando por la máxima fiabilidad o priorizando la velocidad, según la aplicación.



## Primitivas de servicio


<chapterId>4480afb7-e950-4ccb-88fa-d132f9dc3479</chapterId>



### Arquitectura por capas y organización de Exchange


Como hemos visto, los **servicios** son la implementación concreta de los protocolos que hemos descrito hasta ahora. Aunque el modelo TCP/IP difiere del modelo **OSI**, adopta el mismo enfoque por capas: cada Layer está diseñada para realizar una función específica y para proporcionar **servicios** a la Layer directamente superior, lo que resulta en una arquitectura modular, robusta y fácil de mantener.


Cada Layer se basa en las capacidades de la capa inferior y, a su vez, proporciona a la Layer superior una Interface coherente para gestionar los datos. En esta arquitectura, cada Layer tiene sus propias **estructuras de datos**, cuidadosamente definidas para garantizar una compatibilidad perfecta con las demás capas. Esta compatibilidad es esencial para una comunicación fluida, fiable y clara de un extremo a otro.


Dos aspectos clave rigen estos intercambios:


- Aspecto vertical**: la relación entre una Layer y la que está por encima o por debajo de ella (de Layer N a Layer N+1, y viceversa).



![Image](assets/fr/023.webp)




- Aspecto horizontal**: la interacción entre aplicaciones remotas, es decir, el diálogo entre un **cliente** y un **servidor**, en cualquier dirección.



![Image](assets/fr/024.webp)



La arquitectura por capas sigue el principio de que cada Layer procesa sólo la información que entra dentro de su ámbito: las estructuras de datos, las cabeceras y los mecanismos de control varían de una Layer a otra, pero juntas forman un sistema coherente, que garantiza que los datos se encaminan gradualmente hacia su destino final.


**Recordatorio**: Se utiliza una terminología específica para describir las unidades de datos intercambiadas entre capas:


- mensaje** para la Aplicación Layer,
- segmento** para el transporte Layer (TCP),
- datagrama** para Internet Layer (IP),
- para el acceso a la red Layer.


La siguiente tabla resume los términos para los contextos TCP y UDP:


| TCP/IP Layer         | Unit Name (TCP) | Unit Name (UDP) |
|----------------------|------------------|------------------|
| Application Layer    | Stream           | Message          |
| Transport Layer      | Segment          | Packet           |
| Internet Layer       | Datagram         | Datagram         |
| Network Access Layer | Frame            | Frame            |

### Primitivas de servicio y unidades de datos


En el núcleo de este sistema se encuentran las **primitivas de servicio**, que actúan como interfaces de comunicación. Estas primitivas funcionan como escritorios de servicio, escuchando en **puertos** específicos reservados y permitiendo a los procesos establecer, mantener y terminar conexiones de red de forma controlada. Mientras que los protocolos organizan el formato y la transmisión de datos a través de la red, son los **servicios y sus primitivas** los que proporcionan el enlace vertical entre las capas.


Al combinar el aspecto horizontal (comunicación entre aplicaciones distribuidas) con el vertical (interacciones internas entre capas), el modelo TCP/IP ofrece una arquitectura completa y escalable. La superposición de estas dos perspectivas ofrece una visión clara de cómo se intercambian los datos en la comunicación estructurada en red.



![Image](assets/fr/026.webp)



### Resumen parcial


En esta primera gran sección, hemos explorado la arquitectura central que rige la configuración y el funcionamiento de las redes actuales conectadas a Internet. Esta arquitectura se basa en un **modelo de cuatro Layer**, inspirado en el modelo OSI, y construido en torno al conjunto de protocolos **TCP/IP**, columna vertebral de las comunicaciones modernas. Hemos visto que TCP, con su enfoque orientado a la conexión, garantiza transferencias fiables, mientras que UDP, más ligero y rápido, se prefiere cuando la velocidad es más importante que la fiabilidad.


El correcto funcionamiento de este modelo se basa en la implementación de protocolos a través de **primitivas de servicio**. Éstas garantizan el enlace entre capas, permitiendo adaptar el tratamiento de los datos a las necesidades específicas de cada nivel, desde el transporte hasta la aplicación, pasando por Internet y el acceso a la red. Este enfoque modular hace que el sistema sea a la vez flexible y robusto.


El direccionamiento IP es otra piedra angular de esta infraestructura. Cada dispositivo conectado se identifica mediante una **Address** IP única, tomada de un espacio Address organizado en **clases** (de la A a la E). Algunas de estas direcciones se reservan para fines especiales, como loopback local o multidifusión, mientras que otras, conocidas como "direcciones privadas", no se encaminan por Internet sin traducción (NAT). Esta clasificación permite una organización lógica y jerárquica de las redes.


También hemos examinado el concepto de **subredes**, que permite dividir una red en segmentos para gestionar mejor los recursos IP y optimizar el flujo de datos. Aunque la subdivisión manual mediante máscaras de subred sigue siendo un principio importante, se ha modernizado en gran medida gracias a **CIDR** (_Classless Inter-Domain Routing_). Este método ha transformado la gestión de Address al permitir una asignación más flexible y racional de los rangos IP, reduciendo al mismo tiempo el tamaño de las tablas de enrutamiento.


Al dominar estos conceptos -capas, protocolos, primitivos de servicio, direccionamiento y subredes- se adquiere una base sólida para comprender el funcionamiento técnico de las redes modernas y configurar eficazmente una infraestructura de red que satisfaga las necesidades actuales.


En la siguiente sección, veremos más de cerca el direccionamiento IPv4.



# Direccionamiento IPv4


<partId>83f3c3e5-378c-440f-a095-df210842efde</partId>



## Uso de IPv4


<chapterId>79e4dd18-446a-435b-9f25-c88a00f8bec6</chapterId>



En esta sección, profundizaremos y veremos cómo se implementan realmente las direcciones **IPv4** en una red del mundo real. Desglosaremos su formato, la lógica que hay detrás de ellas y cómo se conectan con otras Elements clave de la red como **nombres DNS**, **direcciones MAC**, **subredes** y **técnicas de traducción**.


Un Address IP es un identificador numérico único asignado a cada **Interface** de red de un dispositivo. Permite localizar este dispositivo dentro de una red y llegar a él para transmitir datos. Por ejemplo, un router, un servidor, una estación de trabajo, una impresora de red o incluso una cámara de vigilancia tienen al menos una IP Address propia. La IP Address hace posible el **enrutamiento**, es decir, mover paquetes del punto A al punto B, aunque estén físicamente muy alejados.


Las direcciones IP pueden asignarse de dos formas principales:


- Estático**: Configurado manualmente en el dispositivo.
- Dinámico**: Asignados automáticamente a petición por un servidor DHCP (_Protocolo de configuración dinámica de host_). DHCP simplifica la gestión de la red, eliminando la necesidad de configuración manual al tiempo que permite un control preciso a través de reservas y duraciones de arrendamiento.


**Las direcciones IPv4** se escriben en un formato de 32 bits dividido en cuatro bytes. Cada byte contiene 8 bits y representa un número decimal de 0 a 255. Los 4 bytes están separados por puntos para formar una notación clara y legible.


ejemplo: Address 172.16.254.1_



![Image](assets/fr/027.webp)



Cada bit de un byte tiene un valor (o "peso"): el bit de la izquierda (el más significativo) vale 128, el siguiente 64, luego 32, 16, 8, 4, 2 y 1 para el bit de la derecha (el menos significativo). De este modo, la escritura binaria se convierte en decimal por la simple suma de los pesos establecidos.


El cuadro siguiente ilustra esta correspondencia:



| Binary Code | Activated Bit Values          | Decimal Value |
|-------------|-------------------------------|---------------|
| 00000000    | 0                             | 0             |
| 00000001    | 1                             | 1             |
| 00000011    | 1 + 2                         | 3             |
| 00000111    | 1 + 2 + 4                     | 7             |
| 00001111    | 1 + 2 + 4 + 8                 | 15            |
| 00011111    | 1 + 2 + 4 + 8 + 16            | 31            |
| 00111111    | 1 + 2 + 4 + 8 + 16 + 32       | 63            |
| 01111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64  | 127           |
| 11111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 | 255      |

Para convertir binario a decimal, suma los pesos de los bits que están a 1.


| Binary     | Decimal Value |
| ---------- | ------------- |
| `10101100` | 172           |
| `00010000` | 16            |
| `11111110` | 254           |
| `00000001` | 1             |

Una IP Address identifica una sola **red Interface**, no todo el dispositivo. Un router o firewall multipuerto tiene múltiples interfaces, cada una con su propia IP Address. Una Interface puede incluso tener varias direcciones IP (por ejemplo, para dar servicio a varias redes o servicios virtuales).


Cada paquete IP contiene dos direcciones IP en su cabecera:


- La fuente Address (**remitente**)
- El Address de destino (**receptor**)

Los enrutadores leen estas direcciones para averiguar cuál es la mejor ruta para enviar el paquete hasta que llegue a su destino. Sin reglas estrictas de direccionamiento, el tráfico de red no podría encaminarse correctamente y la interconexión global de redes sería imposible.


Un Address IPv4 tiene dos partes:


- NetID**: identifica la red
- HostID**: identifica un dispositivo dentro de esa red

La **máscara de subred** determina dónde termina el NetID y dónde empieza el HostID, especificando cuántos bits pertenecen a cada parte. Cuanto más larga sea la NetID, mayor será el número de subredes posibles, pero el número de hosts por subred disminuye en consecuencia.


Originalmente, las redes IPv4 se dividían en cinco **clases**: (A, B, C, D y E). Cada clase corresponde a un rango NetID específico y define una granularidad fija:


- Clase A: redes muy extensas con un gran número de hosts
- Clase B: redes medianas
- Clase C: redes pequeñas
- Clase D: direcciones reservadas a la multidifusión (_multicast_)
- Clase E: direcciones experimentales, no utilizadas para el direccionamiento convencional



| Class | Leading Bits | First Byte Range | Default Subnet Mask | Purpose                          |
| ----- | ------------ | ---------------- | ------------------- | -------------------------------- |
| A     | 0            | 0 – 127          | 255.0.0.0           | Very large networks              |
| B     | 10           | 128 – 191        | 255.255.0.0         | Medium-sized networks            |
| C     | 110          | 192 – 223        | 255.255.255.0       | Small networks                   |
| D     | 1110         | 224 – 239        | N/A                 | Multicast addresses              |
| E     | 1111         | 240 – 255        | N/A                 | Experimental (not publicly used) |

Direcciones especiales:


- Red Address**: Identifica la propia red (se utiliza en las tablas de enrutamiento).
- Emisión Address**: Envía datos a todos los dispositivos de la subred a la vez (todos los bits HostID a 1).


Los siguientes rangos están reservados para uso interno:


- 10.0.0.0/8** (Clase A privada)
- 127.0.0.0/8** (loopback local o _loopback_)
- 172.16.0.0 a 172.31.255.255** (clase B privada)
- 192.168.0.0 a 192.168.255.255** (clase C privada)


Las direcciones **127.0.0.1** y, de forma más general, todo el rango 127.0.0.0/8 se utiliza para pruebas internas: cualquier petición que se le envíe nunca sale de la máquina. Esto es útil para comprobar que un servicio de red local funciona sin involucrar a la red más amplia.


Para aprovechar mejor el espacio Address, los administradores suelen dividir las redes en **subredes** utilizando máscaras de subred o la notación **CIDR** (_Classless Inter-Domain Routing_). CIDR permite una gestión más precisa y ayuda a evitar el desperdicio de direcciones. Hoy en día, CIDR es esencial para afinar los rangos IP y reducir el tamaño de las tablas de enrutamiento.


En las redes modernas, el direccionamiento IP suele ir acompañado de otros identificadores:



- nombre de dominio** registrado en un **DNS** (_Domain Name System_): Asocia una IP numérica Address a un nombre amigable.
- MAC Address**: identificador físico grabado en la tarjeta de red, utilizado para el transporte local (_Ethernet_). Cuando es necesario transmitir físicamente un paquete IP, la tabla ARP hace coincidir el Address IP con el Address MAC del destino.


Para hacer frente a la escasez de Address IPv4 y añadir un Layer de seguridad, las redes suelen utilizar la traducción de Address (_NAT_). NAT permite que muchos dispositivos privados compartan una única IP Address pública cuando acceden a Internet.


**Nota**: Las herramientas en línea e integradas en el sistema operativo, como la [Calculadora CRIC de Grenoble](http://cric.grenoble.cnrs.fr/Administrateurs/Outils/CalculMasque/), facilitan enormemente los cálculos de subredes y máscaras.

Estas utilidades ayudan a planificar eficazmente la división de la red.


En conclusión, el Address de difusión sigue siendo una función práctica para enviar el mismo mensaje a todos los dispositivos conectados a un segmento: esto se consigue poniendo todos los bits de la parte HostID a 1 para que todos los hosts sean el objetivo.



## Los diferentes tipos de IPv4 Address


<chapterId>2adfad24-a90d-45b5-b808-3d2f6598bebf</chapterId>



Las direcciones IPv4 se dividen en dos categorías principales: direcciones públicas, directamente accesibles en Internet, y direcciones privadas, destinadas a uso interno dentro de una red local.


Una IPv4 Address pública es globalmente única y enrutable en Internet. La asignan las autoridades oficiales y es necesaria para servicios públicos como sitios web, servidores de correo electrónico o infraestructuras en la nube.

La unicidad mundial de estas direcciones es esencial para evitar cualquier conflicto o colisión de enrutamiento.


La **IANA** (_Internet Assigned Numbers Authority_), dependiente de la **ICANN** (_Internet Corporation for Assigned Names and Numbers_), gestiona la distribución de estos rangos IP. Concretamente, IANA divide el espacio IPv4 en 256 bloques de tamaño /8, según la notación CIDR. Cada bloque representa algo más de 16,7 millones de direcciones (2³² / 2⁸).


Estos bloques unicast Address son confiados por IANA a los **Regional Internet Registries** (RIRs). Estos RIR se encargan de redistribuir las direcciones a nivel regional, en función de las necesidades reales de los proveedores de acceso, empresas o administraciones. El espacio unicast Address se extiende desde los bloques **1/8 a 223/8**, con porciones reservadas para usos especiales (investigación, documentación, pruebas) o asignadas directamente a una red o RIR para su redistribución.


Para comprobar quién es el propietario de una IP Address pública, puede consultar las bases de datos de los RIR utilizando el comando **whois**, o utilizando las interfaces web proporcionadas por cada registro. Estas herramientas pueden utilizarse para rastrear la Address hasta la organización o el proveedor que la declaró.


A la inversa, existen direcciones IPv4 privadas, una respuesta práctica a la escasez de direcciones públicas. Estas direcciones, que no son enrutables en Internet, se reservan para entornos locales: redes corporativas, LAN domésticas, centros de datos o clusters informáticos. No son únicas en todo el mundo: muchas redes privadas pueden reutilizar los mismos rangos IP sin interferencias, siempre que permanezcan aisladas o utilicen un dispositivo de traducción Address de red para acceder a Internet.


Para que un dispositivo con una IP Address privada pueda acceder a Internet, las redes utilizan NAT (Network Address Translation). NAT sustituye dinámicamente la Address privada por una pública, lo que permite que docenas (o incluso cientos) de dispositivos compartan una única Address IP pública. Este método optimiza el uso del espacio IPv4 y también añade un Layer de seguridad al ocultar la estructura interna de la red.


Otra categoría especial son las direcciones **no especificadas**. La notación IPv4 **0.0.0.0** o su versión IPv6 **::/128** significa "sin Address específico". Una Address de este tipo no es válida como destino de Address de red, pero puede ser utilizada localmente por un host para indicar "todas las interfaces" o "ninguna Address asignada todavía". Esto es común en Assignment dinámicos DHCP o para escuchar en todas las interfaces del servidor.


IPv6 también soporta direccionamiento privado, pero el estándar generalmente recomienda el direccionamiento público para evitar apilar múltiples capas NAT. Las **direcciones locales de sitio** (_site-local_) del bloque **fec0::/10** fueron obsoletas por **RFC 3879** por razones de consistencia y seguridad. Se sustituyeron por **Direcciones Locales Únicas** (_ULA_) ubicadas en el bloque **fc00::/7**. Las ULA permiten la creación de redes IPv6 privadas con enrutamiento interno limpio, utilizando un identificador de 40 bits generado aleatoriamente para garantizar la unicidad local.


El agotamiento de IPv4 se confirmó oficialmente en 2011. Para prolongar su vida útil, la comunidad de Internet adoptó varias estrategias:


- Migración gradual a **IPv6**
- Uso generalizado de **NAT**
- Políticas de asignación más estrictas de los RIR, que exigen una justificación y gestión precisas de las necesidades de Address
- Recuperación de bloques Address no utilizados o devueltos voluntariamente por las empresas


Estas medidas demuestran que el direccionamiento IP no es sólo un reto técnico, sino también una cuestión de gobernanza mundial, fundamental para la continua expansión de Internet.



## DNS, un directorio Address


<chapterId>511244ec-ba43-44ac-b4c3-b41579a15cff</chapterId>



Seamos sinceros, a los humanos no se nos da bien memorizar largas cadenas de números, ya sea en forma binaria o decimal. Este reto se hace aún mayor con las direcciones IP, que pueden ser complejas y una sola IP Address a veces puede enmascarar varias direcciones, sobre todo cuando intervienen técnicas como NAT o el alojamiento virtual.


Para facilitar las cosas, la Aplicación Layer utiliza un sistema que vincula una IP Address a un nombre lógico, legible por humanos. Esta es la función de **DNS** (*Domain Name System*), un directorio masivo, jerárquico y distribuido que relaciona nombres de dominio legibles con direcciones IP. El sistema se basa en un conjunto de protocolos y servicios. El software de servidor DNS más utilizado es **BIND** (_Berkeley Internet Name Domain_), un paquete de software de código abierto que hace referencia a gran parte de la infraestructura DNS de Internet.


La idea central del DNS es sencilla: para cualquier servicio conectado, ya sea un sitio web, un servidor de correo u otro servicio de red, existe un registro que asigna un nombre de dominio a una o varias direcciones IP. Esto funciona en dos direcciones:


- Forward resolution: traducir un nombre en una IP Address.
- Resolución inversa: encontrar el nombre de dominio asociado a una IP Address dada.

Esto hace que el direccionamiento de red sea utilizable para los humanos, al tiempo que preserva la precisión que necesitan los enrutadores para mover los datos correctamente.


Un nombre de dominio siempre se estructura jerárquicamente, con cada nivel separado por un punto: el nombre completo se denomina **FQDN** (_Fully Qualified Domain Name_). La parte más a la derecha es el **TLD** (_Top Level Domain_) como `.com`, `.org` o `.fr`. La parte más a la izquierda designa el host, es decir, la máquina o servicio específico vinculado a la IP Address.


El sistema DNS está diseñado como un **árbol de zonas**. Una **zona** es una sección del espacio de nombres de dominio gestionada por un servidor DNS específico. Una misma zona puede contener múltiples **subdominios**, que a su vez pueden ser delegados a otras zonas gestionadas por diferentes servidores. Los administradores son responsables del mantenimiento de sus zonas: gestión de actualizaciones, delegaciones y gestión general.


Esta estructura permite no sólo apuntar a un dominio principal (por ejemplo, `ejemplo.com`), sino también ajustar registros para hosts individuales (`www`, `mail`, `ftp`, etc.). En los primeros tiempos de las redes, esta asignación se gestionaba con archivos estáticos como (`/etc/hosts` en sistemas Unix), pero este método pronto se volvió poco práctico para una Internet interconectada y en rápido crecimiento.


Es importante entender que un **servidor DNS** puede tener un alcance limitado. Por ejemplo, el servidor DNS interno de una empresa puede no ser directamente accesible desde Internet. Si este DNS no está configurado para reenviar consultas, o no tiene una relación de confianza con otros servidores, algunas consultas fallarán: ni el nombre ni la IP Address podrán entonces resolverse fuera de la zona definida.


El DNS también desempeña un papel en el enrutamiento del correo electrónico. Por ejemplo, un registro **MX** (_Mail Exchange_) especifica los servidores de correo responsables de recibir los correos electrónicos de un dominio determinado. Estos registros definen prioridades (factor de ponderación) y soluciones de conmutación por error. El archivo de zona de un servidor DNS debe contener un registro **SOA** (_Start Of Authority_), que designa al servidor como fuente oficial de información para esa zona.


Gracias a su estructura jerárquica y distribuida, el DNS sigue siendo una piedra angular de Internet, que permite a los usuarios acceder a los servicios a través de nombres de dominio claros y memorizables en lugar de largas y técnicas direcciones IP.


En el próximo capítulo, exploraremos otro concepto fundamental: **Direcciones Ethernet**, también conocidas como **Direcciones MAC**, que garantizan la entrega de datos en el Layer físico de las redes locales.



## Descubrimiento de direcciones Ethernet y ARP


<chapterId>d02109f6-9bf9-4261-a8f9-e1aa4398b949</chapterId>



### Definiciones


Para que el protocolo de enrutamiento de datos funcione de forma fiable y coherente, es esencial un componente clave. Como humanos, podemos identificar fácilmente una máquina por su Address IP o por su nombre recuperado a través de DNS. Una máquina, sin embargo, debe ser capaz de reconocer inequívocamente el dispositivo de destino para entregar los paquetes. Para ello, se basa en un identificador de hardware específico, utilizado directamente por su Interface de red: el Address MAC (_Media Access Control_).


**Nota**: Esto no tiene nada que ver con una "Address física" en la arquitectura de memoria. En informática, una Address de memoria física se refiere a una ubicación específica en el bus de memoria, a diferencia de una Address virtual gestionada por el sistema operativo. En cambio, una Address MAC se refiere estrictamente al hardware de red.


Una MAC Address es asignada de forma permanente y única por el fabricante del equipo. La MAC Address identifica inequívocamente la tarjeta de red, ya sea un ordenador, un smartphone, una impresora o cualquier otro dispositivo conectado. A diferencia de una IP Address, que puede cambiar dinámicamente (a través de un servidor DHCP o una configuración manual), la MAC Address normalmente permanece igual durante toda la vida útil del dispositivo, a menos que se altere deliberadamente.


Cada red Interface, cableada o inalámbrica, tiene su propia MAC Address. Esta Address se utiliza dentro del enlace de datos Layer (Layer 2 del modelo OSI) para insertar y gestionar el hardware Address en cada trama de red intercambiada. A veces se denomina _dirección Ethernet_ o _UAA_ (_Universally Administered Address_). Estandarizada en una longitud de 48 bits, o 6 bytes, se escribe en notación hexadecimal, generalmente en forma de bytes separados por `:` o `-`.


Por ejemplo: `5A:BC:17:A2:AF:15`


En esta estructura, los tres primeros bytes identifican al fabricante de la tarjeta de red: es lo que se conoce como **OUI** (*Organisationally Unique Identifier*). Estos prefijos, asignados por el IEEE, también se utilizan en otros esquemas de direccionamiento de hardware, como Bluetooth y LLDP, para garantizar la unicidad mundial.


### Cambio de una MAC Address (MAC Spoofing)


En teoría, la MAC Address está diseñada para permanecer fija, pero existen formas de modificarla, sobre todo para satisfacer necesidades particulares o eludir ciertas restricciones. Esta operación, a menudo denominada _spoofing MAC_, consiste en sustituir la Address hardware original por un valor diferente, definido a nivel de software. Algunos sistemas operativos facilitan esta modificación, sobre todo cuando la Address Ethernet real no es utilizada directamente por el controlador.


Los motivos de un cambio de este tipo son variados. Puede ser la necesidad de que una determinada aplicación requiera una Address Ethernet específica para funcionar correctamente, o para resolver un conflicto de direcciones idénticas entre dos dispositivos que comparten la misma red local.


El cambio de la MAC Address también puede estar motivado por consideraciones de privacidad: al ocultar el identificador único grabado en la tarjeta, los usuarios reducen la posibilidad de que su dispositivo sea rastreado por redes o servicios de vigilancia. Sin embargo, esta práctica no está exenta de consecuencias. Cambiar una MAC Address puede perturbar ciertos dispositivos de filtrado, o exigir que se reconfiguren los cortafuegos para autorizar el nuevo hardware.


Algunas redes, especialmente las Wi-Fi, utilizan el filtrado MAC Address para permitir sólo dispositivos con direcciones aprobadas. Aunque esto añade un nivel básico de control, no es seguro por sí solo. Un atacante puede capturar una MAC Address válida ya autorizada en la red y clonarla para saltarse las restricciones. Por esta razón, el filtrado MAC siempre debe combinarse con medidas de seguridad más fuertes.


### Correspondencia MAC/IP


Para que una red local funcione eficientemente, debe existir un claro mapeo entre las direcciones físicas (direcciones MAC) y las direcciones lógicas (direcciones IP). Sin este vínculo, un ordenador podría conocer la Address IP de un destino pero no sabría cómo enviarle físicamente datos en la red local.

Esta asignación la gestiona automáticamente el ARP (_Address Resolution Protocol_).


En la práctica, cuando un usuario desea conocer la MAC Address correspondiente a una IP Address específica, puede utilizar la utilidad `arp`. Esta herramienta comprueba la tabla ARP local de la máquina para mostrar las coincidencias conocidas entre direcciones IP y direcciones MAC en la red local. De este modo, es posible verificar rápidamente el enlace efectivo entre las capas lógica y física.


Ejemplo práctico: si desea comprobar qué tarjeta de red corresponde a la IP Address `192.168.1.5`, utilice el siguiente comando:


```bash
arp –a 192.168.1.5
```


La salida mostrará la Address física asociada (MAC), la naturaleza de la entrada (estática o dinámica) y la Interface en cuestión.


```
Interface: 192.168.1.5 --- 0x5
IP Address            MAC Address                Type
192.168.1.5           00:54:BC:17:14:6E          D
```


Es importante recordar que la MAC Address y la IP Address son dos identificadores completamente diferentes, aunque estrechamente complementarios. La MAC Address está grabada de forma única en cada Interface de red por el fabricante y se utiliza para identificar físicamente el dispositivo en la red local. La IP Address, por otro lado, es una Address lógica asignada de forma dinámica o estática, que permite a la máquina unirse a la red IP y Exchange paquetes más allá de su red local.



- Ejemplo visual de MAC Address:


![Image](assets/fr/032.webp)




- Ejemplo visual de una IP Address:


![Image](assets/fr/027.webp)



En un entorno corporativo, estos dos niveles de direccionamiento no pueden funcionar por separado. Por ejemplo, cuando un servidor DHCP asigna automáticamente una IP Address, se utiliza la MAC Address del equipo como punto de partida. El equipo envía una solicitud de difusión DHCP que contiene su MAC Address para que el servidor pueda asignar una IP Address disponible al dispositivo correcto. Sin esta identificación de hardware, el servidor DHCP no sabría a qué dispositivo entregar el Address.


El protocolo ARP es, por tanto, fundamental: proporciona el enlace entre las direcciones IP y las direcciones físicas, permitiendo a las máquinas traducir un destino lógico en un destino físico real. Cuando un ordenador necesita enviar un paquete a una máquina de la misma red, primero consulta su tabla ARP para comprobar si ya conoce la Address MAC del destinatario. Si no es así, emite una solicitud ARP a todas las máquinas de la red local. El equipo que reconoce la IP Address de destino en esta solicitud responde especificando su MAC Address. A continuación, el remitente escribe este par IP/MAC en su caché ARP, para evitar tener que repetir la operación cada vez que se envía la solicitud.


Esta tabla ARP actúa como un mini directorio de mapeo, actualizado dinámicamente de forma similar a como DNS asocia nombres de dominio con direcciones IP. Sin ARP, no sería posible una Exchange local, ya que la Layer de enlace de datos necesita conocer la Address MAC para encapsular correctamente las tramas Ethernet.


Por el contrario, el protocolo RARP (_Reverse Address Resolution Protocol_) se diseñó para la situación opuesta: permitir que una máquina que sólo conoce su Address MAC descubra su Address IP. Este era el caso habitual de las estaciones de trabajo más antiguas sin un disco Hard local, que tenían que arrancar a través de la red y solicitar una Address IP. RARP fue eventualmente reemplazado por **BOOTP** y luego **DHCP**, que son más flexibles y automatizados.


Estos protocolos de asociación desempeñan un papel importante en el encaminamiento. Un encaminador es esencialmente una máquina con múltiples interfaces de red, que conecta diferentes segmentos. Cuando un router recibe una trama, la procesa para extraer el datagrama IP y examina la cabecera IP para determinar el destino. Si el destino está en una red conectada directamente, el datagrama se entrega directamente tras actualizar la cabecera. Si el destino pertenece a otra red, el router consulta su tabla de encaminamiento para identificar la mejor ruta, o _siguiente salto_, hacia el destino.


Esto divide la ruta en segmentos más cortos y manejables. Cada encaminador intermedio sólo conoce el siguiente paso, no necesariamente el destino final.


**Recordatorio:** La entrega directa se produce cuando el remitente y el destinatario se encuentran en la misma red física. En caso contrario, la entrega es indirecta y pasa por uno o varios routers.


La tabla de encaminamiento, gestionada manualmente (encaminamiento estático) o dinámicamente (encaminamiento dinámico), contiene la información necesaria para decidir qué ruta tomar. En redes pequeñas, basta con una configuración estática. En infraestructuras más grandes, el encaminamiento dinámico es esencial para ajustar automáticamente las rutas cuando cambia la topología o se cae un enlace.


La tabla de enrutamiento actúa como una tabla de mapeo entre las direcciones IP de destino y las siguientes pasarelas. Normalmente almacena identificadores de red (_network ID_) en lugar de cada Address host individual, lo que reduce enormemente su tamaño.


| Destination Address | Next-Hop Router Address | Interface |
| ------------------- | ----------------------- | --------- |

Utilizando estas entradas, el router puede determinar rápidamente a través de qué Interface y a qué nodo debe enviarse cada datagrama. Combinado con ARP para resolver las direcciones MAC coincidentes, esto asegura una transferencia de datos eficiente y fiable a través de la red.


Por último, los protocolos de encaminamiento dinámico incluyen estándares como RIP (_Routing Information Protocol_), basado en el algoritmo de la distancia, y OSPF (_Open Shortest Path First_), que calcula las rutas más cortas en topologías complejas. Estos protocolos actualizan constantemente Exchange para optimizar las rutas, reducir los costes de transmisión y mejorar la resistencia frente a cortes o congestiones.



## NAT: Traducción Address


<chapterId>4f984d5d-f2e0-4faf-b703-ff315f32cef4</chapterId>



### Definición


Network Address Translation_ (NAT) es una técnica desarrollada para Address el agotamiento gradual de las direcciones IPv4 disponibles. Diseñada como solución provisional antes de la adopción generalizada de IPv6, NAT permitía a empresas y particulares seguir conectando un gran número de máquinas utilizando sólo un conjunto limitado de direcciones IP públicas.


**Recordatorio importante:** el paso de IPv4 a IPv6 resuelve teóricamente el problema del agotamiento al ampliar el espacio Address de 32 bits a 128 bits, proporcionando un número casi ilimitado de direcciones (2^128). En la práctica, sin embargo, la transición es aún incompleta, y NAT sigue siendo ampliamente utilizado hoy en día.


El principio en el que se basa NAT es sencillo pero muy eficaz: en lugar de asignar una única IP Address pública a cada dispositivo de la red interna, se utiliza una única Address enrutable (o un pequeño grupo de direcciones) para todos los dispositivos privados. La pasarela NAT, a menudo integrada en el router o cortafuegos, traduce entonces dinámicamente la IP Address interna junto con la información necesaria para enrutar correctamente el tráfico hacia el exterior, y garantiza que las respuestas se devuelvan al remitente original.


Este enfoque tiene una ventaja inmediata: oculta completamente la arquitectura interna de la red. Para un observador externo, todas las peticiones de estaciones de trabajo, servidores o impresoras parecen proceder de la misma identidad pública. Las direcciones privadas, normalmente tomadas de rangos reservados (por ejemplo, 192.168.x.x o 10.x.x.x), permanecen invisibles desde Internet.


Además de hacer frente a la escasez de IPv4, NAT también refuerza la seguridad al crear una primera barrera lógica entre la red interna y la pública. Las comunicaciones entrantes no solicitadas se bloquean de forma natural, ya que sólo las conexiones iniciadas desde el interior de la red se benefician de la traducción necesaria para recibir respuestas.



![Image](assets/fr/035.webp)



### Tipos de traducción


NAT puede implementarse de diferentes maneras para adaptarse a necesidades específicas. Los dos modos principales de funcionamiento son la traducción estática y la traducción dinámica.


**La traducción estática** crea una asignación fija entre una IP Address privada y una IP Address pública. Cada equipo interno está permanentemente vinculado a su Address pública dedicada. Por ejemplo, un equipo interno configurado como 192.168.20.1 podría estar asociado a la Address enrutable 157.54.130.1. Cuando un paquete saliente sale de la red local, el enrutador sustituye el Address de origen del paquete por el Address público, y realiza la operación inversa para el tráfico entrante. Esta traducción bidireccional es transparente para el usuario.


**Atención:** Aunque este método aísla la red interna, no resuelve la escasez de direcciones IP públicas, ya que se siguen necesitando tantas direcciones públicas como máquinas haya que exponer. Por lo tanto, la traducción estática se utiliza principalmente cuando ciertos recursos internos deben permanecer accesibles desde el exterior (servidor web, servidor de correo...).


**La traducción dinámica**, por otro lado, utiliza un conjunto de direcciones IP públicas. Cuando un host interno inicia una conexión, el router asigna temporalmente una de estas direcciones públicas a la Address privada del host mientras dure la sesión. El enlace es 1 a 1, pero temporal: una vez finalizada la conexión, la Address pública pasa a estar disponible para otro dispositivo. Por tanto, la NAT dinámica reduce el número de direcciones públicas necesarias cuando no todos los equipos están conectados al mismo tiempo, pero sigue necesitando un bloque de direcciones externas al menos tan grande como el número máximo de conexiones simultáneas.


*la *traducción de puertos** (PAT), también conocida como *sobrecarga de NAT* o *enmascaramiento de IP*, va un paso más allá: todos los dispositivos privados comparten una única IP pública Address (o un número muy pequeño). Para distinguir las sesiones, la pasarela modifica no sólo el Address de origen, sino también el puerto de origen. Mantiene una tabla que vincula cada par *(Address privada, puerto privado)* a un único par *(Address pública, puerto público)*. Esta forma de NAT se utiliza en casi todos los routers domésticos, permitiendo que docenas de dispositivos (ordenadores, smartphones, objetos conectados, etc.) compartan la misma IP Address pública, manteniendo una comunicación fluida.


Por tanto, NAT prolonga la vida útil de IPv4, al tiempo que añade un valioso Layer de segmentación y seguridad. Sin embargo, a medida que aumente la adopción de IPv6 y se generalice el uso de su vasto espacio Address, es probable que el papel de NAT disminuya, aunque por motivos de compatibilidad y control, seguirá utilizándose en algunos entornos para segmentar y filtrar el tráfico.


### Implantación de NAT


Para garantizar el correcto funcionamiento de la traducción Address, el router o pasarela NAT debe mantener un registro preciso de los mapeos establecidos entre cada Address privada de la red interna y la Address pública que utiliza para comunicarse con el mundo exterior. Esta información se almacena en lo que se conoce como "tabla de traducción NAT", que desempeña un papel fundamental en la gestión del tráfico de red.


Cada entrada de esta tabla vincula al menos un par: la IP Address interna de la máquina remitente y la IP Address externa que se expondrá en Internet. Cuando se envía un paquete desde la red privada a un destino público, el router NAT intercepta la trama, analiza las cabeceras IP y TCP/UDP y, a continuación, sustituye el Address de origen privado por el Address público de la pasarela. En la ruta de retorno, la misma pasarela captura el paquete entrante, comprueba la tabla de asignación y realiza la operación inversa para redirigir el flujo a la IP interna Address original.


Este principio de traducción dinámica se basa en una gestión precisa de la tabla: cada entrada sigue siendo válida mientras haya tráfico activo que la justifique. Tras un periodo de inactividad configurable, la entrada se borra y puede reutilizarse para nuevas conexiones.


_Ejemplo de tabla de traducción NAT simplificada:_


| Internal IP   | External IP    | Duration (sec) | Reusable? |
| ------------- | -------------- | -------------- | --------- |
| 10.101.10.20  | 193.48.100.174 | 1,200          | no        |
| 10.100.54.251 | 193.48.101.8   | 3,601          | yes       |
| 10.100.0.89   | 193.48.100.46  | 0              | no        |

En este ejemplo, si no ha pasado ningún paquete por la segunda entrada en más de una hora (3.600 segundos), se marca como reutilizable. Por el contrario, una duración de cero indica una comunicación activa, con el mapeo bloqueado.


Aunque NAT funciona de forma transparente para los usos más comunes (navegación web, correo electrónico, transferencia de archivos, etc.), puede crear retos adicionales para ciertas aplicaciones de red. Algunas tecnologías se basan en el intercambio explícito de direcciones IP o puertos dentro de la carga útil del paquete. Tras pasar por una pasarela NAT, esta información se vuelve incoherente.


Algunos ejemplos típicos de limitaciones son:


- Los protocolos peer-to-peer (P2P), que requieren conexiones directas entre dispositivos, se ven obstaculizados por la barrera NAT, ya que todas las máquinas internas comparten la misma IP externa Address y no se puede llegar a ellas directamente sin una configuración específica (como *port forwarding* o UPnP);
- El protocolo IPSec, utilizado para proteger las comunicaciones de red, cifra las cabeceras de los paquetes. Dado que NAT debe modificar estas cabeceras para sustituir las direcciones IP, el cifrado lo hace imposible sin mecanismos de adaptación como NAT-T (*NAT Traversal*);
- El protocolo X Window, que permite la visualización remota de aplicaciones gráficas en Unix/Linux, funciona de forma que el servidor X envía activamente conexiones TCP a los clientes. Esta inversión del sentido habitual de las conexiones puede bloquearse mediante NAT.


En general, cualquier protocolo que incluya explícitamente la IP interna Address en la carga útil del paquete se verá afectado, ya que esa Address ya no coincidirá con la Address real visible en Internet después de la traducción.


**Nota importante:** Para Address estos problemas, algunos routers NAT ofrecen _Inspección Profunda de Paquetes_ (DPI) o _Ayudantes de Protocolo_ , que inspeccionan el contenido de los paquetes para identificar y sustituir dinámicamente las direcciones o números de puerto dentro de los datos de las aplicaciones. Esto requiere un conocimiento profundo del formato del protocolo, y puede crear vulnerabilidades de seguridad o aumentar el uso de recursos.


**Precaución:** Aunque NAT ayuda a ocultar la red interna y a controlar el tráfico entrante, no sustituye a un cortafuegos dedicado. La traducción por sí sola no es una barrera de seguridad completa: siempre debe complementarse con reglas de filtrado claras para bloquear el tráfico no solicitado o no deseado.


para ilustrar cómo funciona esto en la práctica, considere el siguiente ejemplo:_



![Image](assets/fr/037.webp)



En este escenario, una estación de trabajo interna puede acceder al servidor web interno simplemente llamando a la URL `http://192.168.1.20:80`. Especificar el puerto es opcional aquí, ya que `80` es el puerto HTTP estándar. Especificar el puerto es opcional en este caso, ya que `80` es el puerto HTTP estándar.Por el contrario, si se inicia una solicitud desde el exterior, el usuario introducirá la Address pública `http://85.152.44.14:80`. El router NAT recibe la petición, consulta su tabla de mapeo y traduce automáticamente la Address pública en privada, redirigiendo la conexión a `http://192.168.1.20:80`.


El mismo principio se aplica a cualquier otro servidor autorizado a recibir conexiones a Internet, como el servidor Extranet (circuito azul en el diagrama).


**Nota práctica:** en entornos virtualizados, las interfaces de red llamadas _virbrX_ (por _Puente Virtual X_) se utilizan comúnmente. Estos puentes virtuales, proporcionados en particular por la biblioteca libvirt o el hipervisor Xen, conectan la red interna virtual de las máquinas huésped a la red física aplicando NAT. Generalmente se configuran mediante scripts en `/etc/sysconfig/network-scripts/`, como se muestra a continuación para `virbr0`:


```ini
NAME=""
BOOTPROTO=none
MACADDR=""
TYPE=Bridge
DEVICE=virbr0
NETMASK=255.255.255.0
MTU=""
BROADCAST=192.168.0.255
IPADDR=192.168.0.1
NETWORK=192.168.0.0
ONBOOT=yes
```


Una vez instalado el puente virtual, es necesario activar el enrutamiento IP y configurar la traducción de puertos con `iptables`:


```shell
echo 1 > /proc/sys/net/ipv4/ip_forward
```


```shell
iptables -t nat -A POSTROUTING -o <WAN> -s 192.168.0.0/24 -j MASQUERADE
```


Con esta configuración, el tráfico saliente se enruta y se aplica la traducción NAT, lo que permite a las máquinas virtuales comunicarse con el mundo exterior sin exponer directamente sus direcciones IP internas.


En el próximo capítulo, veremos en detalle la configuración de IP Address en Linux, cubriendo métodos simples y avanzados adaptados a diferentes contextos de administración.



https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864


## ¿Cómo configuro la red con `ip`?


<chapterId>8ba7e946-d2a0-4841-8d54-e85ba96baa25</chapterId>



### Configuración estándar


Después de cubrir los fundamentos teóricos de las redes y entender cómo funcionan juntas las direcciones IP, las máscaras, el enrutamiento y la traducción, es hora de pasar a la configuración práctica. En GNU/Linux, la configuración de red se maneja ahora con el comando **`ip`** (paquete _iproute2_), que reemplaza al antiguo `ifconfig`.


`ip` le permite asignar o cambiar una IP Address, cambiar una máscara, iniciar o detener una Interface, o comprobar su estado en cualquier momento.


**TIPS:** para mostrar todas las interfaces (activas o no): `ip addr show`


Ejemplo: asignación de un Address estático y activación de Interface


Añade Address `192.168.1.2/24` a Interface `eth0`:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Activar Interface:


```shell
ip link set dev eth0 up
```


Desactive la misma Interface:


```shell
ip link set dev eth0 down
```


Muestra el estado de una Interface específica:


```shell
ip addr show dev eth2
```


**Consejo práctico:** con `ip`, añadir una Address adicional a una Interface ya no requiere un sufijo `:1`. Basta con añadir otra línea `ip add add ...`:


```shell
ip addr add 172.18.2.39/24 dev eth2
```


### Scripts de activación: ifup / ifdown


Las utilidades `ifup` y `ifdown` leen archivos de configuración estáticos de `/etc/sysconfig/network-scripts/` (en RHEL, CentOS, Rocky Linux, AlmaLinux...) o `/etc/network/interfaces` (en Debian/Ubuntu) para subir o bajar interfaces de forma limpia.


```shell
ifup eth1
ifdown eth2
```


Archivos de configuración (tipo RHEL):


- /etc/sysconfig/network**: configuración global (NETWORKING, HOSTNAME, GATEWAY...).
- ifcfg-**: ajustes específicos para cada Interface.


Ejemplo estático (ifcfg-eth0):


```ini
DEVICE=eth0
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.2.5
NETMASK=255.255.255.0
GATEWAY=192.168.2.1
```


Ejemplo de DHCP:


```ini
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
```


Esta estructura modular sigue siendo válida y puede automatizarse fácilmente en los sistemas actuales.


### Configuración avanzada: enlace


En entornos profesionales, el objetivo es garantizar la continuidad del servicio y/o agregar ancho de banda. *Los mecanismos Bonding* (o *teaming* con _teamd_) responden a estas necesidades: varias interfaces físicas funcionan como una única Interface lógica, a menudo denominada `bond0` o `team0`.



![Image](assets/fr/039.webp)



Requisitos previos:


- Carga el módulo `bonding` (o utiliza `teamd`) ;
- Disponga de al menos dos interfaces físicas.


#### Los distintos métodos de unión habituales:


|Mode|Name|Principle|
|---|---|---|
|0|balance-rr|Round-robin, cyclic distribution of frames|
|1|active-backup|Single active interface with hot failover |
|2|balance-xor|Selection based on XOR of src/dst MAC addresses|
|3|broadcast|Broadcast simultaneously on all interfaces   |
|4|802.3ad (LACP)|Standardized dynamic aggregation; requires compatible switch|
|5|tlb (Transmit Load Balancing)|Balancing based on transmit load|
|6|alb (Adaptive Load Balancing)|Adaptive balancing; also balances receive via ARP|

#### Configuración con `ip link



- Desactivar interfaces físicas:


```shell
ip link set eth0 down
ip link set eth1 down
```



- Crea el Interface unido:


```shell
ip link add bond0 type bond mode balance-alb
```



- Configurar opciones tras la creación


```shell
ip link set bond0 type bond miimon 100
```



- Asignar direcciones MAC e IP:


```shell
ip link set dev bond0 address 00:17:56:BC:02:3A
ip addr add 192.168.2.3/24 dev bond0
ip route add default via 192.168.2.1
```



- Adjuntar interfaces esclavas:


```shell
ip link set eth0 master bond0
ip link set eth1 master bond0
```



- Vuelve a subir todo:


```shell
ip link set bond0 up
ip link set eth0 up
ip link set eth1 up
```


**Consejo:** para separar un esclavo sin quitar el enlace: `ip link set eth1 nomaster`


#### Configuración permanente (tipo RHEL)


Crea tres ficheros en `/etc/sysconfig/network-scripts`:


_ifcfg-bond0_


```ini
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=none
IPADDR=192.168.2.3
NETMASK=255.255.255.0
BROADCAST=192.168.2.255
GATEWAY=192.168.2.1
BONDING_OPTS="mode=balance-alb miimon=100"
```


_ifcfg-eth0_


```ini
DEVICE=eth0
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


_ifcfg-eth1_


```ini
DEVICE=eth1
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


Entonces:


```shell
systemctl restart network
```


#### IP adicional Address (alias moderno)


Con `ip`, basta con añadir una segunda Address al mismo dispositivo:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Para que este alias persista tras un reinicio, añada un segundo bloque `IPADDR2=...` / `PREFIX2=...` a `ifcfg-eth0`, o cree una nueva conexión *NetworkManager* mediante `nmcli`.


Gracias a `ip` y los comandos relacionados (`ip link`, `ip addr`, `ip route`), la configuración de red es más coherente, scriptable y clara. El enlace es un componente clave de las arquitecturas de alta disponibilidad, y la asignación de varias direcciones a una única Interface se ha simplificado mucho.


En el próximo capítulo, veremos los detalles y la implementación del direccionamiento IPv6.


# Direccionamiento IPv6


<partId>9b1d87f1-2a68-496e-b5dd-76cf74fb8cde</partId>


## IPv6: Normas y definiciones


<chapterId>d1f16f0a-1104-460d-8d67-f725665f8e3f</chapterId>



Pasamos ahora a la siguiente generación de direccionamiento IP: el protocolo IPv6, conocido originalmente como IPng (_IP Next Generation_). Diseñado para superar las limitaciones estructurales de IPv4, este protocolo introduce una arquitectura de direccionamiento enormemente ampliada, así como numerosas optimizaciones técnicas.


Las motivaciones de la adopción de IPv6 son variadas y Address necesidades críticas para la evolución de Internet. En primer lugar, la función de IPv6 es soportar el crecimiento exponencial del número de dispositivos conectados (objetivo inalcanzable con el limitado Address espacio de IPv4). En segundo lugar, el protocolo pretende reducir el tamaño de las tablas de encaminamiento, lo que hará más eficaces los intercambios y reducirá a largo plazo la carga de trabajo de los encaminadores.


IPv6 también pretende simplificar ciertos aspectos del manejo de paquetes, mejorando el flujo de datagramas y optimizando la velocidad de transferencia entre redes. Desde el punto de vista de la seguridad, las cabeceras AH/ESP del protocolo *IPsec* están incluidas en la especificación base, y todos los nodos IPv6 deben ser capaces de soportarlas (RFC 6434). Sin embargo, su uso sigue siendo opcional: corresponde al administrador habilitarlas en función del contexto.


Otros objetivos son una gestión más precisa de los tipos de servicio, sobre todo para garantizar una mejor calidad de las aplicaciones en tiempo real (VoIP, videoconferencia, etc.). IPv6 también está pensado para permitir una gestión más flexible de la movilidad: un dispositivo puede cambiar de punto de acceso sin modificar su Address de forma visible para sus pares.


Por último, IPv6 se diseñó para coexistir con protocolos heredados. Aunque no es directamente compatible en binario con IPv4, sigue siendo plenamente interoperable con protocolos superiores a Layer como TCP, UDP, ICMPv6 y DNS, así como con protocolos de encaminamiento como OSPF y BGP, con ciertos ajustes. Para la gestión de multidifusión, IPv6 utiliza el protocolo MLD (*Multicast Listener Discovery*), que es el equivalente funcional de IGMP en el entorno IPv4.


### Reglas de notación


Uno de los cambios más significativos de IPv6 es el formato de la propia Address IP. Para paliar la escasez crónica de direcciones IPv4, se ha aumentado su longitud de 32 a 128 bits, es decir, 16 bytes. En teoría, esto arroja un espacio Address posible de:


$$3.4 \times 10^{38}$$


Esto garantiza una capacidad prácticamente ilimitada para todos los equipos actuales y futuros.


Las direcciones IPv6 se escriben de forma muy diferente a la conocida notación decimal con puntos. Una Address IPv6 se compone de ocho grupos de 16 bits, escritos en hexadecimal y separados por dos puntos `:`.


Por ejemplo:


```
1987:0c02:0000:84c2:0000:0000:cf2a:9077
```


Para simplificar la notación, pueden omitirse los ceros a la izquierda de cada grupo. El ejemplo anterior se convierte entonces en:


```
1987:c02:0:84c2:0:0:cf2a:9077
```


Además, una única secuencia continua de grupos cero puede sustituirse por::, acortando aún más la Address:


```
1987:c02:0:84c2::cf2a:9077
```


**Atención:** esta regla es estricta: sólo se puede sustituir una secuencia de ceros consecutivos por `::`. Si una Address contiene varias secuencias de ceros, sólo se condensa la más larga. Esto garantiza tanto la unicidad como la legibilidad.


**Detalle importante:** el carácter `:` utilizado para separar bloques hexadecimales puede causar ambigüedad en las URL, ya que `:` también se utiliza para indicar un puerto de servicio. Para evitar confusiones, las direcciones IPv6 en URL deben ir entre corchetes `[ ]`.


Ejemplo de acceso HTTP a un puerto específico para la Address `2002:400:2A41:378::34A2:36`:


```
http://[2002:400:2A41:378::34A2:36]:8080
```


Al representar un Address IPv4 en un contexto IPv6, puede utilizar una notación mixta en forma decimal con puntos, precedida de`::`:


```
::192.168.1.5
```


Esta compatibilidad facilita la transición entre ambos protocolos al permitir incluir bloques IPv4 en el espacio IPv6 Address.


**Nota:** Para estandarizar la forma de escribir las direcciones, el RFC 5952 define un formato canónico con reglas de abreviación para evitar múltiples representaciones de la misma Address. Seguir estas recomendaciones ayuda a reducir las interpretaciones erróneas y garantiza configuraciones de red coherentes.


### Tipos de IPv6 Address


IPv6 se diferencia de su predecesor por una amplia gama de categorías de Address, cada una diseñada para usos específicos, al tiempo que permite un encaminamiento y una gestión de red flexibles. Como en IPv4, las direcciones pueden ser globales, locales, reservadas o específicas de determinados mecanismos de transición.


Una Address IPv6 no especificada se representa mediante `::` o, más explícitamente, `::0.0.0.0`. Esta forma especial se utiliza durante la adquisición de Address, o como valor por defecto para indicar la ausencia de un Address.



| IPv6 Address Prefix | Description                                 |
| ------------------- | ------------------------------------------- |
|::/8                | Reserved addresses                          |
| 2000::/3            | Unicast addresses, routable on the Internet |
| fc00::/7            | Unique local addresses (1)                  |
| fe80::/10           | Link-local addresses                        |
| ff00::/8            | Multicast addresses                         |

(1): *En una LAN privada, el prefijo `fd00::/8` es preferible para asignar direcciones internas que no son enrutables en Internet.*


#### Direcciones reservadas


Ciertos rangos IPv6 están explícitamente reservados y no deben utilizarse como direcciones globales. Tienen fines técnicos específicos:


- `::/128`**: Address no especificado, nunca asignado permanentemente a un dispositivo, pero utilizado como Address de origen por una máquina en espera de configuración.
- `::1/128`**: el _loopback_ Address, el equivalente directo de `127.0.0.1` en IPv4, que permite a una máquina Address a sí misma.
- `64:ff9b::/96`**: Reservado para traductores de protocolo que permitan la interconexión IPv4/IPv6, como se define en RFC 6052.
- `::ffff:0:0/96`**: bloque de compatibilidad para representar un Address IPv4 en una estructura IPv6 específica, a menudo utilizado internamente por las aplicaciones.


Estos bloques garantizan la interoperabilidad y facilitan la migración entre las dos versiones del protocolo.


#### Direcciones unicast globales


Las direcciones de unidifusión global constituyen la mayor parte del espacio IPv6 enrutable públicamente y representan aproximadamente 1/8 del espacio Address. Desde 1999, IANA ha asignado estos bloques, como el prefijo `2001::/16`, en bloques CIDR (de `/23` a `/12`) a registros regionales, que luego los redistribuyen a proveedores y organizaciones.


Algunos rangos tienen usos especiales documentados:


- `2001:2::/48`**: Reservado para pruebas de rendimiento e interoperabilidad (RFC 5180).
- `2001:db8::/32`**: Reservado para documentación y ejemplos (RFC 3849).
- `2002::/16`**: Se utiliza para el mecanismo 6to4, que permite que el tráfico IPv6 viaje a través de una infraestructura IPv4 (útil durante la fase de transición entre ambos protocolos).


**Nota:** una gran proporción de direcciones globales permanecen sin utilizar, sirviendo de reserva para el futuro crecimiento de Internet.


#### Direcciones locales únicas (ULA)


Las direcciones locales únicas (`fc00::/7`) son el equivalente IPv6 de las direcciones privadas IPv4 (RFC1918). Permiten crear redes internas aisladas sin riesgo de conflictos con el direccionamiento público. En la práctica, el prefijo efectivo es `fd00::/8`, con el 8º bit a 1 para indicar el uso local. Cada bloque ULA incluye un identificador pseudoaleatorio de 40 bits, lo que minimiza las colisiones Address al conectar redes privadas separadas.


#### Direcciones link-local


Las direcciones link-local (`fe80::/64`) se utilizan exclusivamente para la comunicación dentro del mismo segmento Layer 2 (misma VLAN o switch). Nunca se enrutan más allá del enlace local. Cada Interface de red genera automáticamente una Address link-local, a menudo derivada de su Address MAC utilizando el esquema EUI-64.


**Característica especial**: la misma máquina puede utilizar el mismo Address link-local en varias interfaces, pero debe especificarse el Interface al comunicarse para evitar ambigüedades.


#### Direcciones multidifusión


En IPv6, la difusión ha sido sustituida por la multidifusión, una forma más eficaz de entregar paquetes a un grupo definido de destinatarios. El rango de multidifusión lleva el prefijo `ff00::/8`. Esto incluye direcciones como `ff02::1`, que se dirige a todos los nodos del enlace local. Aunque conveniente, esta Address ya no se recomienda para aplicaciones, ya que puede generate difusiones incontroladas.


Un uso común de la multidifusión es el _Neighbor Discovery Protocol_ (NDP), que sustituye a ARP en IPv6. NDP utiliza direcciones multicast específicas, como `ff02::1:ff00:0/104`, para descubrir automáticamente otros hosts conectados al mismo enlace.


Al combinar estos tipos de Address, IPv6 proporciona un conjunto completo de opciones para satisfacer las necesidades de enrutamiento global, comunicaciones locales, migración IPv4/IPv6 y configuración automática de dispositivos, al tiempo que mejora la eficacia de la transmisión.


### Alcance Address


El ámbito de una Address IPv6 define el dominio exacto en el que es válida y única. Entender este concepto es clave para dominar el enrutamiento de paquetes y la organización lógica de una red IPv6. Las direcciones IPv6 se agrupan generalmente en tres categorías principales basadas en su alcance y uso: unicast, anycast y multicast.


**Las direcciones unicast** son las más comunes e incluyen varios subtipos distintos.

Entre ellos se incluye el _loopback_ (`::1`) Address, cuyo alcance se limita al host que lo utiliza, y que se usa para probar la pila de red internamente sin enviar tráfico a través de la red física.

Luego están las direcciones de enlace local (_link-local_), cuyo ámbito se restringe a un único segmento de red: se utilizan para comunicaciones directas entre dispositivos del mismo enlace físico o lógico (por ejemplo, un único conmutador o VLAN).

Por último, las direcciones locales únicas (_ULA_, por _Unique Local Addresses_) son internas a una red privada. Pueden enrutarse entre varios segmentos privados, pero nunca son visibles en Internet.


Conceptualmente, las direcciones IPv6 suelen representarse como una estructura binaria en la que la primera mitad (los primeros 64 bits) identifica el prefijo de red, y la segunda mitad (también de 64 bits) identifica de forma única la Interface del dispositivo en esa red. Esta división facilita la autoconfiguración Address mediante mecanismos como SLAAC (_Stateless Address Autoconfiguration_), que permiten a las máquinas generate automáticamente una Address estable basada en la MAC Address o en un identificador pseudoaleatorio.


| Field     | Prefix | L | Global ID | Subnet | Interface ID |
|-----------|--------|---|-----------|--------|---------------|
| Bits      | 7      | 1 | 40        | 16     | 64            |

La arquitectura IPv6 sigue el modelo de enrutamiento global jerárquico de la Internet actual. La partición de prefijos permite a los registros regionales y a los operadores de red gestionar la asignación de Address de forma descentralizada, garantizando al mismo tiempo la unicidad global. Dentro de este marco, el mismo host puede tener simultáneamente una Address de unidifusión global para la comunicación por Internet y una Address de enlace local para interacciones locales, por ejemplo, con el vecindario inmediato o para mensajes de descubrimiento de enrutadores.


| Field     | Prefix | Zero | Interface ID |
|-----------|--------|------|--------------|
| Bits      | 10     | 54   | 64           |

**Las direcciones anycast** representan un concepto intermedio que se basa en el modelo unicast pero que puede comportarse como multicast en ciertos casos. Una Address anycast es, en esencia, una Address unicast asignada a varias interfaces distribuidas en diferentes nodos de red. Cuando se envía un paquete a una Address anycast, el protocolo IPv6 intenta entregarlo a uno de los hosts que comparten esa Address, normalmente el más cercano en términos de topología de encaminamiento. Este enfoque optimiza la velocidad de procesamiento de las consultas y mejora la resistencia de los servicios distribuidos. Un ejemplo clásico son los servidores DNS raíz, donde el direccionamiento anycast dirige automáticamente las consultas al punto de presencia más cercano.



| Field     | Prefix | Subnet | Interface ID |
|-----------|--------|--------|--------------|
| Bits      | 48     | 16     | 64           |

En IPv6, las **direcciones de multidifusión** sustituyen al mecanismo de difusión, que se consideraba demasiado costoso e inadecuado para una red de escala global. Una Address de multidifusión identifica a un grupo de interfaces, normalmente a través de varios hosts, que desean recibir los mismos paquetes simultáneamente.

Cada Address multicast incluye un campo especial _scope_ de 4 bits, que define el límite geográfico o lógico de la difusión:


- Un ámbito de `1` significa que el paquete es sólo para el dispositivo local.
- Un ámbito de `2` restringe el paquete al enlace local: todos los dispositivos del mismo segmento físico o virtual pueden recibirlo.
- Un ámbito de "5" amplía el alcance a un sitio, normalmente toda una red corporativa.
- Un ámbito de `8` amplía el alcance a una organización, permitiendo la entrega en todas las subredes de la misma entidad.
- Un ámbito "e" (14 en hexadecimal) indica un alcance global, lo que hace que el grupo multicast sea accesible desde cualquier punto de Internet si la infraestructura de enrutamiento lo admite.


La estructura de una multidifusión IPv6 Address incluye:


- un campo _Flag_ (4 bits) especifica si el grupo es permanente o temporal,
- un campo _Scope_ (4 bits) define el ámbito,
- un campo de identificación (112 bits) que identifica el número de grupo de multidifusión.


| Field      | Prefix | Flags | Scope | Group ID |
|------------|--------|--------|--------|----------|
| Bits       | 8      | 4      | 4      | 112      |

Un ejemplo bien conocido de multidifusión IPv6 en acción es el _Neighbor Discovery Protocol_ (NDP). En lugar de utilizar ARP como en IPv4, NDP se basa en direcciones multicast como `ff02::1:ff00:0/104` para difundir solicitudes de descubrimiento de vecinos, dirigiéndose sólo a los hosts relevantes en el mismo enlace.


Al definir los ámbitos Address con tanta precisión, IPv6 estructura cómo se envían, reciben y enrutan los flujos de datos. Esta granularidad hace que el protocolo sea más flexible y eficiente para gestionar comunicaciones locales y globales, al tiempo que evita los inconvenientes de la difusión generalizada.


## Address Assignment en una red local


<chapterId>4c9c3e52-59bc-499a-af0a-6dd369a9e029</chapterId>


En este capítulo veremos uno de los aspectos más prácticos del despliegue de IPv6: la asignación de direcciones IP a los hosts de una red local. La arquitectura IPv6 ha sido diseñada para ser flexible, permitiendo a cada dispositivo generate su propia Address automáticamente, a la vez que permite una configuración totalmente manual cuando sea necesario.


Una red local IPv6 divide sistemáticamente la Address en dos partes:


- los primeros 64 bits representan el prefijo de subred, normalmente proporcionado por un router o una autoridad Address;
- los 64 bits restantes son utilizados por el host para identificarse de forma única en ese segmento.

Este modelo simplifica enormemente la agregación de rutas y la gestión de bloques Address.


Para asignar direcciones a los dispositivos se utilizan dos enfoques principales:


- Configuración manual, en la que el administrador especifica el Address exacto de cada Interface;
- Configuración automática, en la que los dispositivos generate u obtienen sus propias direcciones de forma dinámica.


En la configuración manual, el administrador asigna a cada Interface la IPv6 Address completa. Algunos valores permanecen reservados:


- `::/128`: Address no especificado, nunca asignado permanentemente ;
- `::1/128`: loopback Address (_loopback_), equivalente IPv4: `127.0.0.1`.


A diferencia de IPv4, no existe el concepto _broadcast_; las combinaciones "todos ceros" o "todos unos" en la parte de host no tienen ningún significado especial.

La configuración manual sigue siendo útil en entornos controlados, pero resulta difícil de mantener a gran escala.


Para la configuración automática, existen varios métodos:


- El protocolo **NDP** (_Neighbor Discovery Protocol_), especificado por RFC4862, permite la autoconfiguración *sin estado*. En este modo, el host recibe un prefijo de red de un router local, y completa él mismo la Address con un identificador basado en su MAC Address. Este método es sencillo de implantar y no requiere un servidor central.
- Implementaciones como las de Windows pueden generate la parte del host de forma pseudoaleatoria para mejorar la privacidad evitando la exposición directa de la MAC Address. Revelar la MAC Address en los paquetes IPv6 puede plantear problemas de privacidad, ya que permite el seguimiento de un dispositivo a través de diferentes redes.
- Protocolo DHCPv6: Definido en RFC3315 y similar al DHCP utilizado para IPv4, permite una configuración más controlada y centralizada, incluyendo la gestión de arrendamientos, opciones extra (DNS, MTU...) y registro de bases de datos. DHCPv6 puede funcionar solo o junto a la configuración sin estado para proporcionar parámetros adicionales sin asignar la propia IP Address.


**Nota importante:** En el método basado en MAC, el MAC Address se convierte en un identificador de 64 bits utilizando el formato EUI-64. Este mecanismo inserta los bytes `FF:FE` en medio del MAC Address original (en 48 bits), e invierte el 7º bit para indicar la unicidad global. El resultado es un identificador Interface estable, utilizado en el Address IPv6 completo.


He aquí un ejemplo de cómo transformar una MAC Address en EUI-64:


![Image](assets/fr/045.webp)



Sin embargo, debido a la creciente preocupación por el rastreo de dispositivos, los sistemas operativos modernos (en particular Linux, Windows 10+, macOS, Android) ahora habilitan extensiones de privacidad por defecto. Estas utilizan identificadores Interface generados aleatoriamente que se renuevan periódicamente para las conexiones salientes, al tiempo que mantienen un identificador estable para las comunicaciones internas (como DNS o DHCPv6).


Al igual que con DHCP en IPv4, las direcciones IPv6 asignadas automáticamente pueden tener dos tiempos de vida, definidos por los routers o servidores DHCPv6:


- Vida útil preferida*: tras este periodo, la Address sigue siendo válida, pero ya no se utiliza para iniciar nuevas conexiones;
- Tiempo de vida válido*: cuando expira este tiempo, la Address se elimina completamente de la configuración de la Interface.


Este sistema permite gestionar dinámicamente los cambios en la red, por ejemplo, garantizando una transición fluida de un ISP a otro. Actualizando el prefijo anunciado por los routers y ajustando los registros DNS en paralelo, la migración a IPv6 puede llevarse a cabo sin interrupción perceptible del servicio.


**Consejo:** El uso combinado de los ciclos de vida de Address y DNS permite aplicar una estrategia de transición gradual, en la que las nuevas conexiones pasan a una nueva topología, mientras que las conexiones existentes continúan hasta su fin natural.


En resumen, IPv6 ofrece una amplia gama de flexibilidad para Address Assignment: configuración manual, autoconfiguración con o sin estado, DHCPv6 o generación aleatoria. Cada enfoque tiene sus propias ventajas y limitaciones, y puede adaptarse según el nivel de control requerido, el tamaño de la red o las necesidades de privacidad.


## Asignación de bloques IPv6 Address


<chapterId>45cce866-1b58-4888-b3fe-15c922180839</chapterId>


### Distribución Address


El esquema de asignación de Address IPv6 se ha estructurado para cumplir dos objetivos: garantizar la unicidad global de Address y permitir una jerarquía lógica que favorezca la agregación y simplificación de las tablas de enrutamiento.

Al igual que con IPv4, la *Internet Assigned Numbers Authority* (IANA) se sitúa en la cima de esta jerarquía. Gestiona el espacio Address de unidifusión global y delega bloques Address en los cinco registros regionales de Internet (_RIR_).


Los cinco RIR existentes son:


- ARIN (Norteamérica),
- RIPE NCC (Europa, Oriente Medio y Asia Central),
- APNIC (Asia-Pacífico),
- AFRINIC (África),
- LACNIC (América Latina y el Caribe).


IANA asigna bloques IPv6 de tamaño variable a cada RIR, generalmente entre /23 y /12. Este enfoque ofrece flexibilidad al tiempo que garantiza la escalabilidad a largo plazo. Los RIR, a su vez, redistribuyen estos bloques entre los proveedores de servicios de Internet (ISP), las grandes empresas y las instituciones públicas.


Desde 2006, cada RIR recibe de IANA un bloque IPv6 /12, un tamaño fijo diseñado para garantizar una reserva estable y suficientemente grande para el crecimiento futuro. Los RIR suelen subdividirlos en bloques /23, /26 o /29. Los ISP suelen recibir bloques /32, aunque este tamaño puede variar en función del tamaño y la zona geográfica del ISP. Suelen asignar bloques /48 a los clientes. Cada /48 proporciona 65.536 subredes /64 distintas (una capacidad enorme en comparación con IPv4).


**Nota importante:** un bloque /32 contiene exactamente 65.536 sub-bloques /48. Esto significa que cada ISP puede dar servicio a decenas de miles de clientes sin agotar su asignación. Gracias a su /48, cada cliente dispondrá entonces de una gigantesca cantidad de espacio para estructurar su propia red interna con tantos segmentos /64 como desee.


La jerarquía de asignación típica tiene este aspecto:


| IANA | RIR | LIR | Customer | Subnet | Interface |
|------|-----|-----|----------|--------|-----------|
|  3   | 20  |  9  |    16    |   16   |     64    |

Con esta abundancia de direcciones, NAT (*Network Address Translation*), antaño esencial en IPv4 para hacer frente a la escasez de Address, ya no es necesario. Cada host puede tener una Address pública, única y enrutable globalmente, lo que simplifica la conectividad de extremo a extremo y facilita el uso de protocolos como IPSec, VoIP o conexiones entrantes.


Para comprobar a qué organización pertenece un Address IPv6, puede utilizar el comando `whois` para consultar las bases de datos RIR públicas. Esta transparencia permite identificar la organización propietaria de un prefijo, lo que puede ser útil para fines de red, análisis o seguridad.


### Direccionamiento PA vs PI


Originalmente, el modelo de asignación IPv6 se basaba únicamente en bloques PA (*Provider Aggregatable*), es decir, vinculados al ISP. En este modelo, una organización recibe su prefijo de su ISP, lo que significa que cambiar de proveedor requiere renumerar toda la infraestructura.


Aunque las funciones de autoconfiguración de IPv6 y la vida útil de Address facilitan la renumeración, sigue siendo un inconveniente para las organizaciones con infraestructuras críticas o múltiples conexiones de proveedores por necesidades de redundancia.


Desde 2009, las políticas de asignación permiten bloques PI (*Provider Independent*). Estos bloques (generalmente de tamaño /48) son asignados directamente a una empresa o institución por un RIR, independientemente de cualquier ISP. Este modelo es especialmente adecuado para las organizaciones que practican el *multihoming*, (es decir, que están conectadas a varios operadores simultáneamente). Por ejemplo, en Europa, RIPE-512 describe la política de asignación de PI.


### Notación de máscara de subred


Como en IPv4, IPv6 utiliza CIDR (*Classless Inter-Domain Routing*). Consiste en indicar el número de bits que componen el prefijo después del Address, mediante el carácter `/`.


Tomemos el siguiente ejemplo:


```
2001:db8:1:1a0::/59
```


Esto significa que los primeros 59 bits son fijos e identifican la red. Todos los bits restantes (aquí 69 bits) pueden utilizarse para identificar subredes o hosts.


Así, esta notación cubre direcciones desde `2001:db8:1:1a0:0:0:0:0` hasta `2001:db8:1:1bf:ffff:ffff:ffff:ffff`.


Este bloque abarca, por tanto, un conjunto de 8 subredes /64, cada una de ellas capaz de albergar un número masivo de dispositivos.


La notación CIDR permite una planificación precisa del espacio Address, desde redes a gran escala hasta configuraciones domésticas y entornos virtualizados, y fomenta la agregación de rutas, reduciendo la carga de los routers y mejorando la escalabilidad.


### Paquetes y cabeceras IPv6


El formato de los paquetes IPv6 difiere del de IPv4 en que es a la vez más sencillo y más extensible. Un datagrama IPv6 comienza siempre con una cabecera de tamaño fijo de 40 bytes que contiene toda la información esencial de encaminamiento. Este enfoque simplificado, comparado con la longitud variable de la cabecera de IPv4 (de 20 a 60 bytes), permite un procesamiento más rápido y eficiente de los paquetes por parte de los routers.


Sin embargo, IPv6 no elimina funcionalidades: en lugar de integrar numerosos campos opcionales en la cabecera principal, introduce un sistema de cabeceras de extensión, situadas inmediatamente después de la cabecera básica. Estas cabeceras opcionales permiten añadir datos o instrucciones específicos de determinadas funciones, sin sobrecargar innecesariamente los paquetes ordinarios.


Algunas cabeceras de extensión siguen una estructura fija, mientras que otras pueden contener un número variable de opciones. En Estas opciones se codifican como tripletas `{Tipo, Longitud, Valor}`:


- El campo "Tipo" (1 byte) indica la naturaleza de la opción;
- Los dos primeros bits del "Tipo" especifican qué deben hacer los routers si no se reconoce la opción:
 - Ignore la opción y continúe con el tratamiento,
 - Suelta el datagrama,
 - Drop y envía un error ICMP a la fuente.
 - Arrojar el datagrama sin notificación (en el caso de paquetes multidifusión).
- El campo "Longitud" (1 byte) especifica el tamaño del campo "Valor", de 0 a 255 bytes;
- El campo "Valor" contiene los datos asociados a la opción.


He aquí un resumen de los diferentes tipos de cabeceras de extensión definidas por IPv6.


#### Cabecera Hop-by-Hop


Esta cabecera, si está presente, siempre se coloca inmediatamente después de la cabecera base. Contiene información que debe ser procesada por cada enrutador a lo largo de la ruta del paquete, a diferencia de la mayoría de las otras cabeceras, que normalmente son manejadas sólo por el nodo de destino. Los usos típicos incluyen la señalización de parámetros globales o la solicitud de pasos de procesamiento específicos a medida que el paquete viaja a través de la red.


![Image](assets/fr/047.webp)


#### Cabecera de enrutamiento


La cabecera de enrutamiento especifica una lista de direcciones intermedias por las que debe pasar el paquete. Existen dos modos principales de enrutamiento:


- Enrutamiento estricto: la ruta exacta está predefinida
- Enrutamiento flexible: sólo se especifican algunos pasos obligatorios.


Los cuatro primeros campos de esta cabecera de enraizamiento son:


- Siguiente cabecera**: identifica el tipo de la siguiente cabecera;
- Routing Type**: define el método de enrutamiento (normalmente `0`);
- Segmentos restantes**: número de segmentos que quedan por recorrer ;
- Address[n]**: lista de direcciones intermedias.


El campo "Segmentos restantes" comienza con el número total de segmentos restantes y se decrementa en uno en cada salto.


![Image](assets/fr/048.webp)


#### Cabecera de fragmentación


En IPv6, sólo el host de origen puede fragmentar un datagrama, a diferencia de IPv4, donde los routers también podían hacerlo. Todos los nodos IPv6 deben ser capaces de manejar paquetes de al menos 1280 bytes. Si un router encuentra un paquete mayor que la MTU del siguiente enlace, envía un mensaje *ICMPv6 Packet Too Big* de vuelta a la fuente, que entonces ajusta el tamaño de sus transmisiones.


La cabecera de fragmentación contiene los siguientes campos:


- Identificación**: identificador único de datagrama para el reensamblaje.
- Fragment Offset**: posición del fragmento dentro del datagrama original.
- Bandera M**: indica si siguen más fragmentos.


![Image](assets/fr/049.webp)


#### Cabecera de autenticación (AH)


Esta cabecera está diseñada para proteger las comunicaciones verificando tanto la autenticidad del remitente como la integridad de los datos. Se utiliza habitualmente con el protocolo IPsec. Mediante un código de autenticación, el destinatario puede confirmar que el mensaje procede realmente del remitente esperado y que no ha sido alterado en tránsito.


En caso de intento de modificación fraudulenta, el código de autenticación dejará de coincidir y el datagrama podrá ser rechazado. Este mecanismo también protege contra los ataques de repetición al detectar duplicaciones no autorizadas.


![Image](assets/fr/050.webp)


#### Cabecera de opciones de destino


Esta cabecera está destinada únicamente al destinatario final del datagrama. Puede utilizarse para añadir opciones o metadatos específicos de la aplicación, sin que los encaminadores intermedios los tengan en cuenta.


Inicialmente, esta opción no estaba definida en el protocolo. Sin embargo, esta cabecera se introdujo cuando se diseñó IPv6, para permitir que se añadieran futuras extensiones sin modificar la estructura general del paquete. La opción null, por ejemplo, sólo se utiliza para rellenar la cabecera con un múltiplo de 8 bytes con fines de alineación de memoria.


![Image](assets/fr/051.webp)


El diseño de los paquetes IPv6 se basa en una clara separación entre una cabecera base mínima y las cabeceras de extensión modulares. Esta arquitectura garantiza tanto un rendimiento de procesamiento estándar como la flexibilidad necesaria para hacer evolucionar el protocolo e integrar mecanismos de seguridad, encaminamiento complejo o calidad de servicio, manteniendo al mismo tiempo la compatibilidad con futuras infraestructuras.


## Relación entre IPv6 y DNS


<chapterId>421eacb8-b80b-4aee-910f-e069ed805f00</chapterId>


En las redes modernas, el DNS (*Sistema de Nombres de Dominio*) traduce los nombres de dominio en direcciones IP que las máquinas pueden utilizar. Con la introducción de IPv6, el DNS tuvo que adaptarse para admitir direcciones de 128 bits manteniendo la compatibilidad con IPv4. Esta coexistencia es especialmente importante en entornos dual-stack, donde ambas versiones de IP funcionan simultáneamente.


### Registros DNS específicos para IPv6


Para asociar un nombre de dominio a una Address IPv6, DNS utiliza un registro AAAA (*cuadrado-A*), análogo al registro "A" para direcciones IPv4. El registro AAAA asigna explícitamente un nombre de dominio a una IPv6 Address.

Ejemplo:


```shell
ipv6.mydmn.org.         IN      AAAA    2001:66c:2a8:22::c100:68b
```


Este registro indica que el dominio `ipv6.mydmn.org` resuelve a la Address IPv6 `2001:66c:2a8:22::c100:68b`. Es posible, e incluso recomendable para una compatibilidad máxima, asociar el mismo nombre de dominio a varias direcciones IP, ya sean IPv4 (mediante un registro A) o IPv6 (mediante un registro AAAA). Esto permite a los clientes compatibles con IPv6 preferir IPv6, al tiempo que garantiza que los clientes sólo IPv4 sigan siendo compatibles.


Además, el DNS admite la resolución inversa, lo que significa que puede buscar el nombre de dominio asociado a una IP Address determinada. En el caso de IPv6, esta operación utiliza registros PTR colocados en la zona `ip6.arpa`. Esta zona está reservada específicamente para la resolución inversa IPv6. Para IPv4, es la zona `in-addr.arpa`.


### Resolución inversa


La resolución inversa de un Address IPv6 sigue un proceso estricto:

1) Despliegue la Address en notación hexadecimal completa (16 bytes, es decir, 32 dígitos hexadecimales).

Ejemplo:


```shell
2001:66c:2a8:22::c100:68b
```


Se convierte:


```shell
2001:066c:02a8:0022:0000:0000:c100:068b
```


2) Invierte el orden de cada dígito hexadecimal (nibble), sepáralos con puntos y añade `ip6.arpa`:


```shell
b.8.6.0.0.0.1.c.0.0.0.0.0.0.0.0.2.2.0.0.8.a.2.0.c.6.6.0.1.0.0.2.ip6.arpa  IN PTR  ipv6.mydmn.org
```


Esta estructura garantiza búsquedas inversas estandarizadas y únicas en el espacio IPv6 Address.


**Nota**: Las consultas DNS pueden viajar a través de IPv4 o IPv6. El protocolo de transporte utilizado no afecta al tipo de registros devueltos.

Por ejemplo:


- Un cliente conectado a través de IPv6 puede solicitar un registro IPv4.
- Un cliente conectado a través de IPv4 puede solicitar un registro IPv6.

El servidor DNS simplemente responde con los registros que tiene, independientemente del protocolo de transporte de la consulta.


Cuando un nombre de host se asigna tanto a IPv4 como a IPv6, la elección de qué Address utilizar se rige por el RFC 6724, que define un algoritmo de selección de Address basado en factores como la preferencia de prefijo, el ámbito y la alcanzabilidad. Por defecto, generalmente se prefiere IPv6 a menos que se anule por configuración del sistema o de la red.


**Recordatorio importante**: al incrustar un IPv6 Address en una URL (*Uniform Resource Locator*), debe ir entre corchetes (`[]`). De este modo se evita la confusión entre los dos puntos (`:`) dentro de la IPv6 Address y los dos puntos que separan el nombre de host del puerto en la URL.


Ejemplo válido:


```shell
http://[2001:db8::1]:8080
```


Esto garantiza que la URL sea procesada correctamente tanto por los navegadores como por los servidores web.


Por tanto, la integración de IPv6 en el sistema DNS requiere nuevos tipos de registro, un método estricto de resolución inversa y reglas precisas de selección y formato para garantizar la compatibilidad y coherencia del enrutamiento.


### Resumen parcial


En esta sección hemos explorado los principios fundamentales del direccionamiento IPv6. Comenzamos examinando la estructura de IPv6 Address: su longitud de 128 bits, su notación hexadecimal y las reglas de simplificación utilizadas para acortar las secuencias repetitivas de ceros. Este diseño permite a IPv6 superar las limitaciones del espacio Address de IPv4, al tiempo que garantiza la escalabilidad y una jerarquía eficiente.


A continuación examinamos las distintas categorías de direcciones IPv6: unicast, anycast y multicast, detallando su alcance, uso típico y representación en el espacio Address.


A continuación, revisamos los métodos de asignación de direcciones IPv6 dentro de una red local, ya sea mediante configuración manual, a través del protocolo DHCPv6, o utilizando mecanismos de autoconfiguración sin estado como los que ofrece NDP. Estos enfoques permiten a los dispositivos generate automáticamente su propia Address a partir del prefijo proporcionado y su Address MAC (a través de EUI-64), al tiempo que ofrecen flexibilidad en términos de gestión del tiempo de vida y privacidad.


También hemos detallado cómo se asignan los bloques Address, empezando por IANA, que los distribuye a los cinco RIR (*Registros Regionales de Internet*), y luego a los ISP, que los redistribuyen a sus clientes como subredes (a menudo en /48, lo que permite 65536 subredes /64). La distinción entre bloques _Provider Aggregatable_ (PA) y _Provider Independent_ (PI) ayuda a gestionar el _multihoming_ o los escenarios de cambio de proveedor.


Hemos visto que DNS se ha adaptado a IPv6 con la introducción del registro AAAA, y que los mecanismos de resolución inversa se basan ahora en la zona `ip6.arpa`. Es importante destacar que el DNS sigue siendo independiente del protocolo de transporte utilizado (IPv4 o IPv6), lo que garantiza una interoperabilidad sin fisuras en un entorno de doble pila.


Por tanto, IPv6 no es sólo una mejora incremental sobre IPv4, sino un rediseño completo del sistema de direccionamiento, construido para responder a los retos actuales y futuros de la Internet global.


En la parte final de este curso NET 302, pasaremos a la práctica y nos centraremos en las herramientas de diagnóstico de redes.



# Herramientas de diagnóstico de red


<partId>368a5c6f-ec48-4b28-970f-3a770788ad37</partId>


## Acceso a la red Herramientas Layer


<chapterId>1d25a21d-6900-4fbe-a438-e06c8afb9e02</chapterId>


En este primer capítulo de la sección final sobre diagnóstico de redes, nos centramos en las herramientas de análisis del Layer de acceso a la red del modelo TCP/IP. Este Layer es responsable de la comunicación directa entre dispositivos de la misma red física, en particular mediante el uso de direcciones MAC e interfaces de red físicas como tarjetas Ethernet o interfaces Wi-Fi.


El objetivo aquí es proporcionar a los administradores herramientas prácticas para inspeccionar, probar y optimizar esta Layer esencial de la conectividad de bajo nivel. Estas herramientas pueden utilizarse para verificar el correcto funcionamiento de las interfaces, solucionar problemas de configuración de las tarjetas de red o detectar anomalías como colisiones, pérdida de paquetes o errores de enlace.


### Utilidades vecinales IP/MAC


#### herramienta `Arp


Una de las herramientas de diagnóstico más antiguas de Network Access Layer es el comando `arp`. Aunque cada vez más reemplazado por alternativas modernas como `ip neigh` (que descubriremos en breve). `Arp` todavía está presente en muchos sistemas para ver o manipular la caché ARP (*Address Resolution Protocol*). Esta caché almacena los mapeos entre direcciones IP y direcciones MAC conocidas localmente en una máquina. En otras palabras, permite determinar qué Address física (MAC) corresponde a una Address IP dada en la red local.


En la práctica, cuando un host desea enviar un paquete a una IP Address dentro de la misma subred, primero debe conocer la MAC Address de la máquina de destino. Esta asignación se gestiona mediante ARP, que difunde una solicitud en la red local y recibe una respuesta con el Address MAC correspondiente. Este resultado se almacena temporalmente en una tabla local denominada "caché ARP", para evitar repetir las solicitudes con cada nuevo paquete.


Para ver el contenido de esta caché y comprobar las entradas actualmente conocidas por la máquina, utilice:


```bash
arp -a
```


Este comando lista todos los mapeos IP/MAC registrados localmente, a través de todas las interfaces. Cada línea proporciona el nombre de host (si se puede resolver), la IP Address, la MAC Address correspondiente y la Interface donde se observa el mapeo.


Para filtrar la visualización a una IP Address específica, basta con especificarla:


```bash
arp -a 192.168.1.5
```


Esto facilita la comprobación de si una determinada IP Address está presente en la caché, lo que puede ayudar a diagnosticar fallos de comunicación entre dos hosts de la misma red.


Del mismo modo, para mostrar sólo las entradas ARP asociadas con una red específica Interface (por ejemplo una tarjeta Ethernet llamada `eth0`), puede utilizar:


```bash
arp -a -i eth0
```


Esto es especialmente útil en entornos multi-Interface (cableados, inalámbricos, VPN, etc.), donde un host puede tener varios adaptadores de red.


El comando `arp` no está limitado a un uso de sólo lectura. También se puede utilizar para editar manualmente la caché ARP, una característica muy valiosa en ciertos escenarios avanzados de solución de problemas o cuando se simulan condiciones específicas. Por ejemplo, puedes añadir manualmente un mapeo IP/MAC:


```bash
arp -s 192.168.1.7 00:17:BC:56:4F:25 -i eth2
```


Este comando crea una entrada estática en la tabla ARP local, asociando la IP Address `192.168.1.7` con la MAC Address `00:17:BC:56:4F:25` en la Interface `eth2`.Si no se especifica ninguna Interface, el sistema utiliza automáticamente la primera aplicable.


También puede eliminar una entrada de la caché ARP, ya sea para corregir un error o para forzar un redescubrimiento:


```bash
arp -d 192.168.1.7
```


Esto borra la entrada, asegurando que el siguiente intento de comunicación desencadena una nueva petición ARP.


**NOTA**: La opción de eliminación también acepta un nombre Interface, lo que le permite dirigir la eliminación de una entrada específica con mayor precisión.


En resumen, la herramienta `arp` proporciona diagnósticos de bajo nivel, especialmente útiles en redes locales, donde los problemas de conectividad a menudo pueden deberse a una resolución Address incorrecta u obsoleta. Sin embargo, en sistemas recientes, especialmente con distribuciones Linux modernas, esta herramienta está siendo sustituida cada vez más por el comando `ip neigh`, del conjunto de herramientas `iproute2`, que ofrece una funcionalidad similar en un marco más unificado.


#### herramienta "IP neigh


En los sistemas modernos, especialmente en las distribuciones recientes de Linux, el comando `ip neigh` es la herramienta de referencia para inspeccionar y gestionar los mapeos entre direcciones IP y MAC. Este comando forma parte de la suite `iproute2`, que está sustituyendo gradualmente a herramientas más antiguas como `arp`, proporcionando un marco más coherente y flexible para el diagnóstico en el enlace de datos Layer.


El comando `ip neigh` consulta la caché local de vecinos IP, que es equivalente a la caché ARP para IPv4 y a la caché NDP (_Neighbor Discovery Protocol_) para IPv6. Esta caché almacena las asociaciones conocidas entre direcciones IP (v4 o v6) y direcciones MAC, junto con su estado (válido, pendiente, expirado...).


El comando básico para mostrar la caché es:


```bash
ip neigh
```


Esto genera una lista de entradas, mostrando la IP de destino Address, la red relevante Interface, la MAC asociada Address (si está disponible), y el estado de la entrada (por ejemplo, `REACHABLE`, `STALE`, `DELAY`, `FAILED`...).


Ejemplo de salida:


```bash
192.168.1.5 dev eth0 lladdr 00:17:BC:56:4F:25 REACHABLE
```


Esta línea indica que la máquina conoce un mapeo válido entre IP Address `192.168.1.5` y MAC Address `00:17:BC:56:4F:25` vía Interface `eth0`.


También puede filtrar las entradas por criterios como IP Address, Interface o estado. Por ejemplo, para consultar sólo Address `192.168.1.7`:


```bash
ip neigh show 192.168.1.7
```


O para mostrar todas las entradas para Interface `eth1`:


```bash
ip neigh show dev eth1
```


Más allá de la consulta, `ip neigh` también puede utilizarse para editar manualmente la caché. Por ejemplo, para añadir una entrada estática:


```bash
ip neigh add 192.168.1.7 lladdr 00:17:BC:56:4F:25 dev eth1 nud permanent
```


Esto asocia permanentemente la IP Address `192.168.1.7` con la MAC Address especificada en Interface `eth1`. La opción `nud permanent` (para _Neighbor Unreachability Detection_) asegura que la entrada no será invalidada automáticamente.


A la inversa, para borrar una entrada de la caché:


```bash
ip neigh del 192.168.1.7 dev eth1
```


Esto obliga al sistema a volver a resolver la asignación la próxima vez que se comunique con esa Address.


**NOTA**: La herramienta `ip neigh` funciona tanto para IPv4 como para IPv6. Para IPv4, interactúa con ARP; para IPv6, interactúa con NDP. Esto proporciona una aproximación unificada y consistente a la gestión de relaciones IP/MAC a través de familias de protocolos, haciendo de `ip neigh` el estándar moderno para la gestión de vecinos en sistemas Linux.


### Herramientas de análisis de paquetes


Para analizar a fondo lo que ocurre en una red informática, los administradores necesitan herramientas capaces de capturar los paquetes intercambiados entre máquinas. Dos utilidades destacan como referentes: `tcpdump` y `Wireshark`. Estas herramientas son esenciales para diagnosticar comportamientos anómalos, auditar intercambios de protocolos o estudiar la seguridad de la red inspeccionando el contenido de las tramas.


#### `ttcpdump`: análisis de línea de comandos


`tcpdump` es una herramienta de línea de comandos muy potente diseñada para capturar y mostrar los paquetes que viajan a través de una red Interface. Funciona en tiempo real y, gracias a su diseño ligero, puede utilizarse en sistemas sin Interface gráfica o con recursos limitados. Se basa en la librería `libpcap`, que proporciona funciones de captura de bajo nivel independientes del hardware.


Un uso común de `tcpdump` es monitorizar la actividad de red de una máquina o segmento de red, filtrando paquetes según criterios específicos. Los resultados pueden redirigirse a un archivo, lo que permite archivar el tráfico para su posterior análisis o reproducirlo en otra herramienta, como Wireshark.


La sintaxis general del comando es:


```bash
tcpdump -w <file.cap> -i <interface> -s <snapshot_length> -n <filters>
```



- `-w` escribe los paquetes capturados en un archivo con formato `libpcap` (extensión `.cap` o `.pcap`);
- `-i` especifica la red Interface a monitorizar (por ejemplo `eth0`, `wlan0`);
- s` establece la cantidad máxima de datos capturados por paquete. Si se especifica `0` se capturan todos los paquetes;
- `-n` desactiva DNS y la resolución de nombres de servicio, mejorando el rendimiento.


Los filtros de expresión al final del comando le permiten restringir las capturas a un subconjunto de tráfico. Puede combinar las palabras clave `host`, `port`, `src`, `dst`, etc., para refinar la selección.


Ejemplo: capturar paquetes HTTP (puerto 80) hacia o desde el servidor `192.168.25.24`, y guardarlos en un archivo `fichier.cap`:


```bash
tcpdump -w fichier.cap -i eth0 -s 0 -n port 80 and host 192.168.25.24
```


El archivo resultante puede analizarse posteriormente en una herramienta gráfica o reproducirse en otro sistema.


#### Wireshark: análisis visual avanzado


Wireshark, antes conocido como *Ethereal*, es un completo programa de análisis de redes con un Interface gráfico. A diferencia de `tcpdump`, proporciona una visualización estructurada y detallada de los paquetes, incluyendo disección de protocolos, gráficos de flujo, estadísticas de tráfico y filtros interactivos. También se basa en `libpcap`, lo que significa que puede abrir y procesar archivos de captura generados por `tcpdump`.


Wireshark está disponible en muchos sistemas operativos, incluidos Linux y Windows. Su instalación requiere privilegios de administrador para acceder a las interfaces de captura. Una vez iniciado, puede seleccionar una red Interface en el menú *Capture*. Haciendo clic en *Start* comienza la grabación de paquetes en tiempo real. La pantalla se divide en tres paneles:


- la lista de fotogramas capturados ;
- detalles descifrados por el protocolo,
- datos hexadecimales en bruto.



![Image](assets/fr/052.webp)



Wireshark destaca en situaciones en las que es necesario observar el comportamiento de protocolos complejos, reconstruir diálogos de aplicaciones (como una sesión HTTP o DNS) o estudiar los tiempos de respuesta de los servicios. También admite filtros de visualización muy específicos que utilizan su sintaxis específica (diferente de la de `tcpdump`) para centrarse únicamente en los paquetes relevantes.


#### Herramientas complementarias


Es importante tener en cuenta que `tcpdump` y Wireshark no son intercambiables: cada uno tiene sus propios puntos fuertes. `tcpdump` es más adecuado para entornos de línea de comandos, scripts automatizados e intervenciones en servidores remotos, mientras que Wireshark es ideal para análisis de tráfico detallados, interactivos y educativos.


Las dos herramientas se pueden combinar: se puede hacer una captura en un sistema remoto con `tcpdump`, y luego se transfiere el archivo `.cap` para analizarlo con Wireshark en una máquina local. Este método se utiliza mucho en la práctica.


### Herramientas de análisis de Interface


En Network Access Layer, a menudo es necesario consultar y configurar las interfaces físicas de red para diagnosticar averías, optimizar el rendimiento o verificar la integridad de la conexión. Una de las herramientas más potentes disponibles en Linux para este fin es `ethtool`, una utilidad de línea de comandos que no sólo proporciona información técnica detallada sobre una Ethernet Interface, sino que también permite ajustar algunos de sus parámetros en tiempo real.


#### Ver especificaciones de Interface


Una de las principales características de `ethtool` es su capacidad para consultar un Interface y mostrar sus características actuales. Esto le permite comprobar:


- velocidad del enlace (por ejemplo, 100 Mbit/s, 1 Gbit/s o 10 Gbit/s) ;
- modo de negociación (semidúplex o dúplex completo) ;
- si está activada la autonegociación;
- el tipo de puerto (cobre, fibra, etc.) ;
- estado del enlace (activo o no) ;
- compatibilidad con funciones avanzadas como *Wake-on-LAN*.


Esta información es especialmente útil para diagnosticar problemas relacionados con la conectividad física o ajustes de negociación no coincidentes entre la tarjeta de red del host y el equipo al que se conecta (conmutador, enrutador, etc.).


Para obtener esta información, basta con ejecutar


```bash
ethtool enp0s3
```


Este comando genera un informe detallado sobre `enp0s3` Interface, una convención de nomenclatura común en sistemas basados en CentOS o RHEL.



![Image](assets/fr/053.webp)



#### Modificación dinámica de los parámetros de Interface


`ethtool` no se limita a la observación: también permite ajustar ciertos parámetros de Interface sin reiniciar la máquina. Esto permite, por ejemplo, forzar una velocidad de enlace específica o habilitar funciones según las necesidades de la red local.


La opción `-s` se utiliza para configurar dinámicamente parámetros como:


- velocidad de enlace (`speed`), establecida explícitamente (por ejemplo, 1000 para 1 Gbit/s) ;
- modo dúplex (`duplex`), ya sea `half` o `full` ;
- activar o desactivar la autonegociación (`autoneg`) ;
- activación de *Wake-on-LAN* (`wol`) ;
- tipo de puerto.


Ejemplo 1: activar la autonegociación en un Interface:


```bash
ethtool -s enp0s3 autoneg on
```


Ejemplo 2: activar la función *Wake-on-LAN* (para permitir que la máquina se despierte remotamente a través de un paquete mágico):


```bash
ethtool -s enp0s3 wol p
```


En este ejemplo, la opción `p` especifica que el wake-up se producirá tan pronto como se detecte un paquete *Wake-on-LAN*. Esta configuración se utiliza a menudo en entornos empresariales para realizar actualizaciones nocturnas o mantenimiento remoto.


#### Instalación de herramientas


Es importante tener en cuenta que `ethtool` no siempre se instala por defecto. En las distribuciones Red Hat/CentOS, puede instalarse con el comando:


```bash
yum install -y ethtool
```


En Debian y Ubuntu, el comando equivalente es:


```bash
sudo apt install ethtool
```


**ADVERTENCIA**: en todos los comandos `ethtool`, el nombre de la red Interface debe especificarse inmediatamente después de la opción (como `-s`). Cualquier error de sintaxis en la colocación de los parámetros hará que el comando sea inválido o ineficaz.



## Herramientas de red Layer


<chapterId>d2c5bf35-4284-4af8-8e8b-049c696a511b</chapterId>


### Herramientas de análisis del tráfico


En el diagnóstico de redes, el comando `ping` sigue siendo una de las herramientas más sencillas y potentes para comprobar la conectividad entre dos máquinas. Comprueba si se puede acceder a un host remoto en un momento dado, al tiempo que proporciona información sobre la latencia, la estabilidad del enlace y la resolución DNS.


El comando `ping` se basa en el protocolo ICMP (*Internet Control Message Protocol*). Cuando un usuario envía una petición `ping`, el sistema envía un paquete ICMP "Echo Request" a una IP Address o nombre de host. Si la máquina de destino está en línea y la ruta de red es válida, responde con un paquete ICMP "Echo Reply". Este sencillo mecanismo puede utilizarse para medir la latencia y detectar problemas de conectividad o de resolución de nombres.


Ejemplo de comando clásico:


```bash
ping 172.17.18.19
```


Respuesta típica:


```bash
mydmn.org (172.17.18.19): 56 data bytes
64 bytes from 172.17.18.19: icmp_seq=0 ttl=56 time=7.7 ms
64 bytes from 172.17.18.19: icmp_seq=1 ttl=56 time=6.0 ms
64 bytes from 172.17.18.19: icmp_seq=2 ttl=56 time=5.5 ms
```


En este ejemplo, la resolución de nombres se ha realizado automáticamente: el dominio `mydmn.org` está asociado a la IP Address `172.17.18.19`, lo que confirma que la resolución DNS funciona correctamente. El comando también proporciona detalles técnicos como:


- número de secuencia iCMP (`icmp_seq`), útil para comprobar el orden de las respuestas;
- TTL (*Time-To-Live*), que indica el número de saltos restantes antes de que el paquete sea descartado;
- tiempo/retraso de ida y vuelta (`time`), expresado en milisegundos, que proporciona una estimación de la latencia del enlace.


#### Análisis más detallado de los parámetros ICMP


El TTL es un campo crítico en el protocolo IP. El remitente inicializa cada datagrama con un valor TTL (a menudo 64, 128 o 255). Cada enrutador a lo largo de la ruta disminuye este valor en 1. Si el TTL llega a 0 antes de alcanzar su destino, el paquete se descarta y se devuelve un error ICMP al remitente. Este mecanismo evita los bucles de enrutamiento infinitos.


El tiempo de propagación (*retardo de ida y vuelta/tiempo*) mide el tiempo que tarda un paquete en salir del emisor, llegar al destino y volver. En la práctica, un retraso inferior a 200 ms se considera aceptable para un enlace estable. Retardos anormalmente altos pueden indicar congestión en la red, enrutamiento ineficiente o mala calidad del enlace.


#### Uso avanzado de `ping


`ping` proporciona opciones para refinar las pruebas y observar comportamientos específicos de la red.


Para enviar solicitudes de difusión, puede utilizar la opción `-b` para dirigirse a todos los hosts de una subred:

```bash
ping -b 192.168.1.255
```


Esto es útil en redes locales para detectar rápidamente hosts activos o probar cómo maneja la red las peticiones de difusión. Sin embargo, en muchas configuraciones, los routers y cortafuegos bloquean los pings de difusión para evitar ataques de amplificación.


También puede especificar un intervalo personalizado entre peticiones con la opción `-i` (por defecto: 1 segundo):


```bash
ping -i 0.2 -c 10 192.168.1.7
```


Esto envía 10 peticiones ICMP a intervalos de 0,2 segundos. Este tipo de pruebas son útiles para detectar fluctuaciones de latencia durante un periodo corto o para someter a un enlace a una ligera tensión para evaluar su estabilidad.


### Herramientas de análisis de tablas de rutas


El comando `ip route`, parte de la suite `iproute2`, es la herramienta recomendada y estándar en los sistemas Linux modernos para inspeccionar y gestionar la tabla de enrutamiento IP del kernel. Reemplaza al obsoleto comando `route`, ofreciendo una sintaxis más clara, mayor consistencia y soporte extendido para características modernas (IPv6, múltiples tablas, espacios de nombres, etc.).


#### Visualización de la tabla de enrutamiento


Para visualizar la tabla de enrutamiento actual:


```bash
ip route show
```


Esta salida enumera todas las rutas conocidas por el núcleo, es decir, los caminos que toman los paquetes salientes en función de su destino.


Ejemplo de salida:


```bash
default via 192.168.1.1 dev eth0 proto dhcp metric 100
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```


Cada línea representa una ruta. Los campos clave incluyen:


- default**: la ruta por defecto, utilizada cuando no coincide ninguna ruta más específica.
- via**: la pasarela utilizada para llegar al destino.
- dev**: la red Interface utilizada.
- proto**: cómo se creó la ruta (manual, DHCP, kernel, etc.).
- metric**: coste de la ruta, utilizado para priorizar múltiples rutas posibles.
- scope**: ámbito de la ruta (por ejemplo, `link` para una ruta conectada directamente).
- src**: la IP Address de origen utilizada para los paquetes salientes en esta Interface.


#### Añadir y eliminar rutas


También puede modificar la tabla de enrutamiento de forma dinámica, por ejemplo, añadiendo o eliminando rutas estáticas.


Añadir una ruta estática:


```bash
ip route add 192.168.1.0/24 via 192.168.1.1 dev eth0
```


Esto configura una ruta a la red `192.168.1.0/24`, a través de la pasarela `192.168.1.1` en Interface `eth0`.


Elimina esta ruta:


```bash
ip route del 192.168.1.0/24
```


Este comando borra la ruta previamente definida.


#### Comandos útiles


He aquí algunas variantes útiles para el análisis o el scripting:


- `ip -4 route`: muestra sólo las rutas IPv4;
- ip -6 route`: muestra sólo las rutas IPv6;
- `ip route list table main`: muestra la tabla de enrutamiento principal (valor por defecto) ;
- ip route get <Address>`: muestra qué Interface y pasarela utilizaría un paquete dirigido a la Address dada.


Ejemplo:


```bash
ip route get 8.8.8.8
```


Muestra la ruta exacta que seguiría un paquete para llegar a `8.8.8.8`.


### Herramientas de seguimiento


Una de las herramientas más eficaces para analizar la ruta seguida por los paquetes IP entre un host de origen y un destino es el comando `traceroute`. Muestra, paso a paso, la ruta seguida por los paquetes e identifica los routers intermedios que atraviesan. En caso de mal funcionamiento de un enlace de red o de interrupción del servicio, `traceroute` ayuda a localizar con precisión el problema.


Al igual que con el comando `ping`, el destino puede especificarse por su nombre de dominio completo (FQDN) o por su Address IP. Por ejemplo:


```bash
traceroute mydmn.org
```


#### Principio de funcionamiento


`traceroute` se basa en el campo TTL (*Time To Live*) de la cabecera de los paquetes IP. Como se ha explicado anteriormente, este campo es un contador decrementado por cada router a lo largo de la ruta. Cuando el TTL llega a cero, el paquete es descartado, y el router devuelve un mensaje ICMP "Time Exceeded" al remitente. Este mecanismo evita bucles infinitos en caso de enrutamiento erróneo.


`traceroute` aprovecha este comportamiento para mapear los routers entre emisor y receptor:


- Primero envía una serie de paquetes UDP (normalmente tres), con un TTL de 1. El primer router encuentra un TTL de 0 por lo que descarta el paquete y luego responde con un mensaje ICMP, revelando su IP Address y tiempo de respuesta.
- A continuación, envía otra serie de paquetes con un TTL de 2, revelando el segundo router.
- El proceso se repite hasta que se alcanza el destino, momento en el que el host responde con un mensaje ICMP Port Unreachable, indicando que se ha alcanzado el punto final.


Por defecto, `traceroute` utiliza paquetes UDP enviados a puertos no utilizados (normalmente empezando por 33434), pero también puede configurarse para utilizar ICMP (como `ping`) o incluso TCP, dependiendo de los sistemas o las variantes del comando.


Ejemplo de salida:


```bash
traceroute to www.google.fr (216.58.210.35), 64 hops max, 52 byte packets

1  par81-024.ff.avast.com (62.210.189.205)   25.107 ms  24.235 ms  24.383 ms
2  62-210-189-1.rev.poneytelecom.eu (62.210.189.1)  27.341 ms  27.119 ms  28.184 ms
3  a9k1-45x-s43-1.dc3.poneytelecom.eu (195.154.1.92)  25.910 ms  25.040 ms  25.558 ms
4  72.14.218.182 (72.14.218.182)  36.234 ms  39.907 ms  38.130 ms
5  108.170.244.177 (108.170.244.177)  25.880 ms
108.170.244.240 (108.170.244.240)  25.791 ms
108.170.244.177 (108.170.244.177)  26.449 ms
6  216.239.62.143 (216.239.62.143)  26.491 ms
216.239.43.157 (216.239.43.157)  26.414 ms
216.239.62.139 (216.239.62.139)  26.400 ms
...
9  108.170.246.161 (108.170.246.161)  33.174 ms
108.170.246.129 (108.170.246.129)  34.342 ms
108.170.246.161 (108.170.246.161)  33.707 ms
10  108.170.232.105 (108.170.232.105)  33.845 ms  33.846 ms
108.170.232.103 (108.170.232.103)  34.206 ms
11  lhr25s11-in-f35.1e100.net (216.58.210.35)  34.094 ms  33.353 ms  33.718 ms
```


Cada línea corresponde a un enrutador atravesado, con hasta tres mediciones de tiempo (en milisegundos) que indican la latencia del viaje de ida y vuelta a ese enrutador. Estos valores ayudan a evaluar el rendimiento de cada segmento de la red.


#### Interpretación de los resultados


Si un router no responde o filtra mensajes ICMP, se muestran asteriscos `*` en lugar del tiempo de respuesta. Esto puede indicar:


- un cortafuegos que bloquea las respuestas ICMP,
- un dispositivo configurado para no responder, o
- un problema temporal de conectividad a lo largo de la ruta.


Así, `traceroute` no sólo identifica la ruta seguida, sino que también pone de relieve los puntos de latencia anormal o las interrupciones.


En algunos sistemas, se puede utilizar el comando equivalente `tracepath`, que no requiere privilegios de root. Para IPv6, utilice `traceroute6` o `tracepath6`.


Ejemplo de rastreo IPv6:


```bash
traceroute6 ipv6.google.com
```


### Herramientas para comprobar las conexiones activas


Para diagnosticar conexiones de red activas y monitorizar la actividad de red en un sistema Linux, el comando `ss` (abreviatura de _socket statistics_) es la herramienta moderna de referencia. Parte de la suite `iproute2`, sustituye al ya obsoleto `netstat`, ofreciendo un mejor rendimiento y resultados más precisos.


`ss` muestra las conexiones TCP y UDP activas, los puertos de escucha, las direcciones locales y remotas, los estados de las conexiones y los procesos asociados.


#### Uso general


Cuando se ejecuta sin opciones, el comando `ss` muestra las conexiones TCP activas. Sintaxis básica:


```bash
ss [options]
```


Algunas opciones habituales para refinar el análisis:


- `-t`: mostrar sólo conexiones TCP;
- `-u`: mostrar sólo conexiones UDP;
- `-l`: mostrar sólo sockets a la escucha;
- `-n`: desactivar la resolución de nombres (IPs brutas y números de puerto) ;
- `-p`: muestra los procesos asociados a cada socket (PID y nombre del programa),
- `-a`: muestra todas las conexiones, incluidas las inactivas,
- `-s`: muestra estadísticas de socket de alto nivel.


#### Casos prácticos


Para visualizar todas las conexiones activas que utilizan el puerto TCP 80 (HTTP):


```bash
ss -ant | grep ':80'
```


Muestra las conexiones TCP activas del puerto 80. Estados como `LISTEN`, `ESTABLISHED`, `TIME-WAIT` indican el estado actual de cada Exchange.


Ejemplo de salida:

```
ESTAB 0 0 192.168.1.10:54321  93.184.216.34:80
```


Para visualizar todas las conexiones de red con los procesos asociados:


```bash
ss -tulnp
```


Para obtener un resumen general del uso de los enchufes:

```bash
ss -s
```


Para filtrar sólo conexiones UDP:

```bash
ss -unp
```


Estos comandos son especialmente útiles para detectar conexiones sospechosas, puertos de escucha inesperados o supervisar la actividad de un servicio concreto.


## Transporte y herramientas superiores Layer


<chapterId>bce47931-930e-4288-b0fd-666c9a1066b5</chapterId>


### Herramientas de consulta DNS


En las capas superiores del modelo TCP/IP, especialmente en la Layer de Aplicación, es importante entender cómo funciona la resolución de nombres. Las herramientas de consulta DNS permiten comprobar si un nombre de dominio está correctamente asociado a una Address IP, y también ayudan a diagnosticar problemas del servidor DNS como errores de configuración, retrasos en la propagación o falta de disponibilidad. Estas herramientas son esenciales para cualquier administrador de red o cualquier usuario que desee una comprensión más profunda de los intercambios DNS en un entorno IP.


#### El comando `nslookup


La herramienta de consulta DNS más sencilla es `nslookup`. Envía una consulta a un servidor DNS y devuelve la IP Address asociada a un nombre de dominio (o viceversa). Por defecto, consulta el servidor DNS configurado en el sistema, pero también se puede especificar un servidor directamente en el comando.


Ejemplo de búsqueda directa:

```bash
nslookup mydmn.org
```


Consulta de un servidor DNS específico:

```bash
nslookup mydmn.org 192.6.23.4
```


La petición solicita al servidor DNS en `192.6.23.4` que resuelva el nombre `mydmn.org`. Esto es especialmente útil para comprobar si un servidor DNS determinado reconoce un nombre de dominio o para verificar que el servidor funciona correctamente.


#### El comando `dig


`dig` (*Domain Information Groper*) es una herramienta más moderna, completa y flexible que `nslookup`. Soporta consultas complejas y proporciona información detallada sobre el proceso de resolución, la jerarquía de servidores implicados, el tipo de registro devuelto (A, AAAA, MX, TXT, etc.) y cualquier error encontrado.


Ejemplo de consulta básica:

```bash
dig mydmn.org
```


Consulta de un servidor DNS específico:

```bash
dig @192.6.23.4 mydmn.org
```


Este comando comprueba la disponibilidad de un registro DNS en un servidor determinado.

Una de las principales ventajas de `dig` es que muestra los detalles de la respuesta DNS, lo que lo hace muy útil para diagnosticar errores de configuración.


#### Configuración manual de los resolvedores DNS


A veces es necesario anular los servidores DNS utilizados localmente, por ejemplo, en entornos de prueba o para forzar el uso de servidores específicos. Esto puede hacerse editando el fichero `/etc/resolv.conf`, que define la configuración de resolución DNS del sistema.


Ejemplo de configuración:


```bash
vi /etc/resolv.conf

search mydmn.org
nameserver 192.168.1.10
nameserver 192.168.1.11
```



- El campo `search` especifica un dominio para añadir automáticamente al resolver nombres cortos.
- Las entradas `nameserver` definen los servidores DNS a utilizar, por orden de prioridad.


En muchas distribuciones modernas (especialmente aquellas que usan `systemd-resolved`), los cambios en `/etc/resolv.conf` son temporales y pueden ser sobreescritos al reiniciar o al reconectar la red. Métodos más permanentes incluyen usar `resolvconf`, `systemd-resolved`, o modificar las configuraciones de *NetworkManager*.


#### El comando `host


Otra herramienta DNS sencilla pero eficaz es `host`. Resuelve nombres de dominio en direcciones IP (o a la inversa) y puede ayudar a diagnosticar fallos de DNS o errores de configuración en una red Interface.


Ejemplos:

```bash
host mydmn.org
```


Búsqueda inversa:

```bash
host 192.6.23.4
```


es especialmente útil para comprobaciones rápidas, sobre todo cuando se utiliza en scripts de línea de comandos.


Las consultas repetidas o intensivas a servidores DNS de terceros sin permiso pueden interpretarse como intentos de intrusión o actividad maliciosa. Utilizados de forma inadecuada, o contra redes que no controlas, estos comandos pueden parecerse a escaneos de reconocimiento, que a menudo son el primer paso de un ataque. Restringe siempre su uso a entornos que administres o en los que tengas autorización explícita.


### Herramientas de exploración de redes


A la hora de supervisar o proteger una red local o de área extensa, es fundamental identificar los dispositivos activos y los servicios a los que dan acceso. Esto es exactamente lo que hace la herramienta `nmap` (*Network Mapper*).


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

#### Presentación de `nmap


`nmap` permite escanear uno o varios hosts para detectar los puertos abiertos, los servicios disponibles (HTTP, SSH, DNS, etc.) y, en ocasiones, incluso el tipo de sistema operativo utilizado. Gracias a sus numerosas opciones, `nmap` proporciona una visión precisa de la superficie de exposición de una red, esencial durante las fases de auditoría o de endurecimiento de la gestión de infraestructuras.


Al igual que el comando `host`, `nmap` nunca debe utilizarse en redes o infraestructuras que no sean de tu propiedad, o sin autorización explícita. Los escaneos de puertos no autorizados pueden ser marcados como intentos de reconocimiento maliciosos, a menudo son detectados por los sistemas de seguridad (cortafuegos, IDS/IPS), e incluso pueden acarrear consecuencias legales.


#### Uso básico


Para escanear un host específico y ver sus puertos abiertos:

```bash
nmap 192.168.0.1
```


Este comando escanea los 1000 puertos más comunes en el host `192.168.0.1` y muestra los servicios accedidos y los protocolos utilizados. Si la resolución DNS está configurada, también puede utilizar el nombre de host en lugar de la IP Address.


#### Exploración completa de la red


Una de las ventajas de `nmap` es su capacidad para escanear un rango completo de direcciones con un solo comando. Esto facilita, por ejemplo, inventariar rápidamente todas las máquinas activas de una red:


```bash
nmap 192.168.0.0/24
```


En este caso, se consultarán todos los hosts en el rango de `192.168.0.0` a `192.168.0.255`. Para cada IP Address, los resultados enumeran los puertos abiertos, su estado (abierto, filtrado, etc.) y, cuando es posible, el nombre del servicio correspondiente.



![Image](assets/fr/055.webp)



Un administrador puede confiar en `nmap` para varias tareas:


- Detectar hosts activos**: identificar qué máquinas responden dentro de una subred;
- Inventario de servicios**: garantizar que sólo se pueda acceder a los puertos necesarios (principio del menor privilegio);
- Comprobación del cumplimiento**: compara los puertos abiertos con la política de seguridad de la organización;
- Prevención de vulnerabilidades**: detectar servicios inseguros o anticuados que se ejecutan en máquinas críticas.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

### Herramientas de interrogación de procesos


Para analizar en profundidad los procesos activos y los archivos abiertos, especialmente en un contexto de red, los administradores de Linux suelen recurrir al comando `lsof` (*List Open Files*). A pesar de su nombre, `lsof` no se limita a los archivos tradicionales: en los sistemas UNIX, todo se considera un archivo, incluidos los sockets de red, los dispositivos y los canales de comunicación.


Por lo tanto, esta herramienta proporciona una visión transversal del sistema correlacionando los procesos activos, los puertos de red abiertos, los archivos a los que se ha accedido y los usuarios implicados.


#### Análisis de redes con `lsof


La opción `-i` restringe la salida a las conexiones de red (TCP, UDP, IPv4 o IPv6). Esto facilita ver qué procesos se están comunicando a través de la red:


```bash
lsof -i
```


Este comando lista todos los procesos en ejecución que utilizan un socket de red, mostrando el puerto en uso, el protocolo (TCP/UDP), el estado de la conexión, así como el PID y el usuario asociado.


#### Filtrado por IP Address o puerto


Puede refinar las búsquedas especificando una IP Address y un puerto, aislando un flujo de red concreto. Por ejemplo, para comprobar una sesión SMTP (puerto 25) con un host específico:


```bash
lsof -n -i @192.168.2.1:25
```


Esto mostrará sólo las conexiones de red activas con el host `192.168.2.1` en el puerto 25, útil para diagnosticar actividad sospechosa o problemas de flujo SMTP.


#### Seguimiento del acceso a los dispositivos


Otro punto fuerte de `lsof` es el seguimiento de archivos especiales como particiones de disco. Por ejemplo, para comprobar qué procesos han abierto archivos en `/dev/sda1`:


```bash
lsof /dev/sda1
```


Esto es útil cuando un intento de desmontaje falla porque el dispositivo todavía está en uso, o cuando se investiga qué aplicaciones están accediendo a una partición.


#### Análisis cruzado: proceso y red


Las opciones pueden combinarse para obtener información precisa. Por ejemplo, para ver todos los puertos de red abiertos por un proceso con PID 1521:


```bash
lsof -i -a -p 1521
```


La opción `-a` interseca los criterios (`-i` y `-p`), restringiendo la salida sólo a las conexiones de red de ese proceso.


#### Seguimiento multiusuario


`lsof` también puede utilizarse para analizar la actividad de usuarios específicos, listando todos los archivos que han abierto, opcionalmente filtrados por PID:


```bash
lsof -p 1521 -u 500,phil
```


Esto muestra los archivos o conexiones de red utilizados por el usuario `phil` o UID 500, limitado al proceso 1521.


### Resumen de la sección


En esta sección final, hemos explorado una amplia gama de herramientas indispensables para diagnosticar, analizar y administrar redes informáticas. Estructurado en torno a las capas del modelo TCP/IP, este estudio no sólo aclara cómo funcionan las comunicaciones de red, sino que también establece una metodología rigurosa para identificar, aislar y resolver posibles problemas.


Estas herramientas ofrecen a los administradores un conjunto coherente de palancas técnicas para supervisar la salud de la red, analizar el tráfico, auditar las conexiones e intervenir rápidamente en equipos o servicios defectuosos.


#### Acceso a la red Layer


Herramientas que proporcionan visibilidad directa de interfaces y tramas:


- arp / ip neigh**: inspeccionar y modificar la caché ARP/NDP para comprobar o corregir las asociaciones IP-MAC;
- tcpdump**: captura de paquetes por línea de comandos, filtrable y exportable;
- Wireshark**: análisis gráfico de paquetes con descodificación profunda de protocolos;
- ethtool**: consulta y ajuste de los parámetros físicos de la tarjeta Ethernet (velocidad, dúplex, WoL, etc.).


#### Red Layer


Herramientas para evaluar la conectividad IP, el enrutamiento y el tráfico de paquetes:


- ping**: prueba la alcanzabilidad y mide la latencia con ICMP;
- ip route**: inspeccionar y modificar la tabla de enrutamiento para controlar las rutas de los paquetes;
- traceroute**: identificación salto a salto de los routers a lo largo de la ruta hacia un destino;
- ss**: inventario detallado de sockets TCP/UDP y procesos asociados (sucesor de netstat).


#### Capas de transporte y aplicación


Herramientas de diagnóstico de servicios y procesos:


- nslookup / dig / host**: Consultas DNS para validar la resolución de nombres y analizar registros;
- nmap**: explora los puertos abiertos y los servicios expuestos para evaluar la superficie de ataque;
- lsof**: lista archivos y sockets abiertos por procesos, correlacionando la actividad del sistema y de la red.


El dominio de estas herramientas, cada una alineada con una etapa específica del modelo TCP/IP, permite un enfoque metódico: empezando por el Layer físico, pasando por el enrutamiento y hasta los servicios de aplicación. Esta cadena de conocimientos equipa a los administradores para diagnosticar, asegurar y optimizar su infraestructura, garantizando tanto el rendimiento como la disponibilidad de la red.


# Parte final


<partId>09d5393c-63bc-42fc-bf79-c65e380211bd</partId>


## Opiniones y valoraciones


<chapterId>114c33c0-9831-4d74-affd-f5d37adc53c3</chapterId>


<isCourseReview>true</isCourseReview>

## Examen final


<chapterId>b99e005e-8dd0-4fa4-b302-f940c27a30ac</chapterId>


<isCourseExam>true</isCourseExam>

## Conclusión


<chapterId>3b449814-78f3-41c0-8138-0a04f3682719</chapterId>


<isCourseConclusion>true</isCourseConclusion>
