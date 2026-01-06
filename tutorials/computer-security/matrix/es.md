---
name: Matrix
description: Una guía para entender, configurar y utilizar Matrix, la plataforma de comunicaciones segura, abierta y descentralizada.
---

![cover](assets/cover.webp)



## ¿Qué es Matrix?



Matrix es un **protocolo de comunicación descentralizado** diseñado para permitir el intercambio de mensajes, archivos y llamadas de audio/vídeo entre usuarios y aplicaciones, sin depender de una empresa central. A diferencia de las plataformas de mensajería tradicionales, Matrix es una **infraestructura abierta**, comparable al correo electrónico: cualquiera puede elegir un servidor u operar uno por sí mismo, conservando la capacidad de intercambio con el resto de la red.



Matrix se distingue por tres principios fundamentales:



### Un protocolo, no una aplicación



Matrix no es una aplicación como WhatsApp o Telegram.


Es un lenguaje estandarizado que pueden utilizar muchas aplicaciones.


En otras palabras, una gran variedad de programas Element, FluffyChat, Cinny, Nheko y otros, proporcionan acceso a la misma red Matrix.



Esto garantiza una libertad total: cambio de aplicación sin pérdida de contactos, diversidad de interfaces, independencia de un único proveedor.



![capture](assets/fr/03.webp)



### Una red descentralizada y federada



La estructura de Matrix se basa en la **federación**, un modelo en el que varios servidores independientes cooperan entre sí.


Cada servidor (llamado _homeserver_) puede alojar usuarios, salas de chat y sincronizar mensajes con otros servidores de la red.


Así :





- ninguna entidad controla todo el sistema;
- un servidor puede desaparecer sin afectar al resto de la red;
- cada organización o individuo puede gestionar su propio espacio.



Este modelo garantiza **una gran resistencia** y refleja los valores de la soberanía tecnológica.



![capture](assets/fr/03.webp)



### Un sistema seguro y cifrado



Matrix admite el **cifrado de extremo a extremo (E2EE)** para intercambios privados y grupos cifrados.


Los mensajes sólo pueden ser leídos por los participantes, no por los servidores intermedios.


Este enfoque permite comunicarse sin exponer el contenido de los intercambios a terceros, conservando la transparencia del protocolo y la posibilidad de alojar un servidor propio.



![capture](assets/fr/05.webp)



### Interoperabilidad única



Una de las principales bazas de Matrix es su capacidad para actuar como **puente entre distintos sistemas de comunicación**. Gracias a los _puentes_, es posible conectar :





- Telegram
- WhatsApp
- Signal
- Mensajero
- Slack
- Discordia
- IRC, XMPP, etc.



Esto permite unificar comunidades dispersas en varias plataformas, manteniendo el control sobre la infraestructura.



![capture](assets/fr/06.webp)



## ¿Cómo funciona Matrix?



Esta sección presenta la estructura interna de la red Matrix para entender cómo interactúan los usuarios, los servidores y las aplicaciones dentro de este ecosistema descentralizado. Matrix se basa en tres elementos esenciales: _homeservers_, identidades y _clients_ utilizados para comunicarse.



### Servidores: homeservers



Matrix se ejecuta en servidores independientes llamados _homeservers_.


Cada servidor gestiona :





- las cuentas de usuario que aloja,
- conversaciones privadas y salones en los que participan estos usuarios,
- sincronización con otros servidores de la red.



Todos los servidores domésticos conectados a la red Matrix intercambian automáticamente mensajes y eventos de las salas de estar compartidas. Por ejemplo:





- un usuario registrado en el servidor A puede chatear con un usuario del servidor B,
- un salón puede repartirse entre decenas de servidores,
- nadie tiene el control de un salón ni de una comunidad en su conjunto.



Este modelo es muy resistente y permite a cada organización o individuo gestionar su propia infraestructura.



### Identificadores de matriz



Cada usuario tiene un identificador único, llamado **MXID** (_Matrix ID_), que se parece a una dirección:



```bash
@nomdutilisateur:serveur.xyz
```



Consta de :





- un nombre de usuario, precedido de **@**
- el nombre del servidor en el que se creó la cuenta, precedido de **:**



Ejemplos:





- `@alice:matrix.org`
- `@bened:monserveur.bj`



Este identificador permite la comunicación con cualquier otro usuario de Matrix, independientemente del servidor de origen.



### Clientes de matriz (aplicaciones)



Para utilizar Matrix, es necesario conectarse con una aplicación llamada **cliente Matrix**.



Los más conocidos son :





- Elemento (web, móvil, escritorio)
- FluffyChat (móvil)
- Cinny (web/escritorio minimalista)
- Nheko (escritorio)



Estas aplicaciones no son más que interfaces para :





- para ver los mensajes,
- enviar texto, imágenes o archivos,
- unirse o crear ferias comerciales,
- realizar llamadas de audio/vídeo.



Todas las aplicaciones se comunican con los servidores mediante el mismo protocolo estandarizado.



### Salas y mensajes privados (DM)



En Matrix, los intercambios tienen lugar en **salas** :





- una sala puede ser pública o privada
- puede albergar a dos personas o a miles
- puede compartirse entre varios servidores
- tiene un identificador único que empieza por **!**



Los mensajes privados son simplemente chats con dos participantes, a menudo denominados **MD (Mensajes Directos)**.



La sincronización de los salones tiene lugar en tiempo real entre los servidores participantes, lo que garantiza una experiencia fluida al tiempo que se mantiene la descentralización.



## ¿Por qué Matrix?



Matrix no es sólo una alternativa a los sistemas de mensajería centralizados: es una tecnología que responde a necesidades reales en términos de soberanía digital, seguridad e interoperabilidad. Hay muchas razones por las que cada vez más personas, empresas e instituciones eligen este protocolo para comunicarse.



### Recupere el control de sus comunicaciones



La mayoría de las plataformas de mensajería funcionan con un modelo centralizado: un único actor controla los servidores, el acceso, los datos y las normas de uso. Este modelo implica una dependencia total del proveedor.


Matrix adopta un enfoque diferente.


Cualquiera puede elegir dónde alojar su cuenta, o incluso instalar su propio servidor. Ninguna entidad está en condiciones de bloquear a un usuario, exigirle una identificación intrusiva o imponerle un cambio de política.


Esta arquitectura devuelve la autonomía tanto a los individuos como a las organizaciones. Las comunicaciones ya no se basan en la confianza en una empresa, sino en un protocolo abierto, documentado y verificable.



### Comunicación segura y cifrada



Matrix admite el cifrado de extremo a extremo para conversaciones y grupos privados. Este mecanismo garantiza que solo los participantes puedan leer los mensajes, aunque pasen por servidores de terceros en la federación.



El protocolo utiliza el algoritmo Megolm/Olm, diseñado específicamente para proporcionar una seguridad sólida en entornos distribuidos y multidispositivo.



Esto permite :





- proteger las conversaciones delicadas,
- impedir el acceso no autorizado (incluso desde el servidor anfitrión),
- mantener la confidencialidad a largo plazo.



El cifrado no es una opción: es un componente esencial del protocolo.



### Ya no depende de una sola aplicación



Matrix no es una aplicación, sino un protocolo.



Esta diversidad de clientes garantiza :





- una elección adaptada a las necesidades individuales,
- la posibilidad de utilizar Matrix en cualquier tipo de dispositivo,
- sin dependencia de un único programa informático.



Si un cliente no es apto o deja de mantenerse, basta con seleccionar otro: la cuenta sigue funcionando con normalidad.



### Federar e interconectar diferentes comunidades



La federación permite que distintos servidores trabajen juntos y se gestionen de forma independiente.


Así :





- una organización puede gestionar su propio servidor doméstico,
- las personas pueden unirse a servidores públicos,
- todos pueden comunicarse entre sí como si estuvieran en la misma plataforma.



Esta flexibilidad permite crear espacios de comunicación adaptados a cada necesidad: equipos, asociaciones, comunidades, instituciones o proyectos de código abierto.



Matrix es especialmente popular en círculos técnicos, colectivos activistas, investigadores, gobiernos y, cada vez más, en las comunidades Bitcoin.



### Interoperabilidad única en el panorama de la mensajería



Una de las principales bazas de Matrix es su capacidad para **ampliar** los intercambios gracias a puentes capaces de enlazar :





- WhatsApp
- Telegram
- Signal
- Slack
- Discordia
- IRC
- XMPP
- y muchas otras plataformas



Matrix se convierte así en una capa unificadora de las comunicaciones, que reúne a varias comunidades dispersas en diferentes aplicaciones.



Esta interoperabilidad reduce la fragmentación y simplifica la colaboración.



### Un protocolo libre, abierto y sostenible



El protocolo Matrix es totalmente de código abierto y de desarrollo transparente.


Esto garantiza varias ventajas:





- una evolución continua de la norma,
- la posibilidad de que cualquiera compruebe el código,
- independencia de los cambios comerciales o políticos,
- resiliencia a largo plazo.



A diferencia de los sistemas de mensajería propietarios, el futuro de Matrix no depende de una sola empresa, sino de una comunidad global y un estándar abierto.



## ¿Cómo se crea una cuenta Matrix?



Crear una cuenta en Matrix es sencillo y no requiere conocimientos técnicos. Los usuarios pueden unirse a un servidor existente, crear un nombre de usuario y empezar a chatear inmediatamente. En esta sección se describen los pasos esenciales.



### Elija un servidor (público o privado)



Matrix es una red federada: hay numerosos servidores (homeservers) gestionados por diferentes organizaciones, comunidades o individuos. La elección del servidor sólo determina _dónde_ se aloja la cuenta, pero no impide la comunicación con toda la red.


**Dos opciones disponibles:**



### - Utilizar un servidor público



Esta es la solución más sencilla.


Ejemplos de servidores populares:





- _matrix.org_ (la más conocida)
- _envs.net_
- servidores comunitarios temáticos (tecnología, privacidad, código abierto...)



Estos servidores son adecuados para usuarios principiantes que desean registrarse rápidamente.



### - Utilizar un servidor privado



Ideal para :





- una organización,
- una familia,
- un proyecto de código abierto,
- un equipo de trabajo,
- o para uso soberano, autoalojado.



En este caso, alguien tiene que administrar el servidor (Synapse, Dendrite, Conduit...).


Independientemente del servidor que elijas, los usuarios pueden hablar entre sí gracias a la federación.



### Crear una cuenta paso a paso



Como Matrix es un protocolo abierto, varias aplicaciones pueden acceder a él.


Como ya se ha descrito, ofrecen distintas interfaces y funcionalidades en función de las necesidades:





- Element**: el cliente más completo, disponible en todas las plataformas.
- FluffyChat**: sencillo, moderno e ideal para móviles.
- Nheko**: cliente ligero y ergonómico para PC.
- SchildiChat**: Variante de Element con mejoras ergonómicas.
- NeoChat**: integrado en el ecosistema KDE.



La elección del cliente no influye en la cuenta: todos funcionan con cualquier servidor Matrix.



### Pasos clásicos :





- Abre la aplicación elegida. En nuestro caso, lo haremos con [Element](app.element.io).
- Seleccione "Crear una cuenta".



![cover-kali](assets/fr/10.webp)



Para simplificar, puede crear una cuenta de Matrix utilizando **Google, Facebook, Apple, GitHub o GitLab**. Estos servicios solo sabrán que su cuenta se ha utilizado para acceder a Matrix: esto se conoce como **conexión social**.



Para mayor confidencialidad, también puede registrarse manualmente eligiendo un **nombre de usuario**, una **contraseña** y una **dirección de correo electrónico**.



Dependiendo del servidor elegido, puede ser necesario un **captcha**, así como la aceptación de las **condiciones de uso**.



Una vez validada la inscripción, se envía un correo electrónico de confirmación.


Sólo tiene que hacer clic en el enlace para activar su cuenta y acceder a la aplicación web (Element) para participar en sus primeras conversaciones de Matrix.



![cover-kali](assets/fr/11.webp)



Ya tienes una cuenta y utilizas la versión web de Element.



## Añada su primer contacto



Para comunicarte con alguien en Matrix, todo lo que necesitas saber es su identificador completo, llamado **ID de Matrix**.



Ejemplo:



`@alice:matrix.org @bened:monserveur.bj`



### Añadir un contacto



Para invitar a tus amigos al chat de grupo, haz clic en el círculo `i` de la esquina superior derecha. Se abrirá el panel de la derecha. Haz clic en "Personas" para ver la lista de miembros de esta sala: tú deberías ser el único presente en este momento.



![cover-kali](assets/fr/12.webp)



Haz clic en "Invitar a esta sala" en la parte superior de la lista de personas y se abrirá una ventana para que puedas invitar a tus amigos a unirse a ti en Matrix. Si ya están conectados a Matrix, introduce su ID de Matrix. Si no lo están, introduce su dirección de correo electrónico y serán invitados a unirse a nosotros.



No existe un sistema de "amigos": un contacto es simplemente una persona con la que se ha abierto una conversación.



![cover-kali](assets/fr/13.webp)



La persona a la que has invitado puede aceptar o rechazar la invitación. Si acepta, debería entrar en la sala. Cuantos más seamos, mejor



![cover-kali](assets/fr/14.webp)



### Configurar su propio servidor



Matrix es realmente útil cuando se utiliza junto con un servidor personal.


Desplegar tu propio servidor doméstico te permite :





- mantener un control total sobre los datos,
- definir sus propias normas de uso,
- alojar varias cuentas (amigos, equipo, comunidad),
- y garantizar la máxima resistencia en caso de restricciones o censura.



**Soluciones disponibles:**





- Synapse**: la aplicación histórica y más completa.
- Dendrite**: más ligero, más potente y diseñado para el futuro del protocolo.
- Conduit**: una variante minimalista y fácil de desplegar.



**Requisitos previos:**





- un nombre de dominio,
- una máquina o un VPS,
- conocimientos mínimos de administración de sistemas.



Aunque requiera un poco de configuración, gestionar tu propio servidor convierte a Matrix en una herramienta soberana y duradera.



### Participar en sus primeras ferias



Matrix se basa en gran medida en _rooms_ (salas de estar).


Hay ferias públicas, privadas, comunitarias, técnicas, locales e internacionales.



**Tres maneras de unirse a un salón:**



1. **A través de un enlace de invitación** (a menudo en forma de URL `matrix.to`).


2. **Buscar el nombre del salón** en la aplicación.


3. **Ingresando el ID completo del espectáculo**, por ejemplo :


`#bitcoin:matrix.org`


`#communauté-bénin:monsrv.bj`



Una vez unido, el chat se comporta como un grupo de noticias clásico, con historial, encriptación, archivos, reacciones y llamadas de audio/vídeo, según el cliente utilizado.



![capture](assets/fr/09.webp)



## Ir más lejos



Una vez que domines lo básico, Matrix te ofrece un sinfín de posibilidades avanzadas. Si quieres conectar otros sistemas de mensajería, alojar tu propio servidor u organizar una comunidad, el ecosistema es muy rico.



### Puentes (WhatsApp, Telegram, Signal, etc.)



Un puente conecta Matrix con otros sistemas de mensajería.


Con él, puedes enviar y recibir mensajes de :





- WhatsApp
- Telegram**
- Signal**
- Facebook Messenger
- Discordia
- Slack**
- IRC** (IRC)
- y muchos otros



### Qué pueden hacer los puentes





- Centralice todas sus conversaciones en Matrix
- Proporcionar una interfaz abierta para interactuar con servicios propietarios
- Gestione una comunidad multiplataforma desde un único lugar



Algunos puentes son oficiales, otros comunitarios.


Dependiendo del departamento, pueden requerir :





- un servidor personal,
- una configuración adicional,
- o la utilización de un puente público existente.



### Utilización de Matrix para una organización, comunidad o proyecto de Bitcoin



Matrix no es sólo una herramienta personal.


Puede utilizarse para estructurar grupos de trabajo, organizar comunidades locales o gestionar la comunicación de proyectos.



**Ejemplos de uso:**





- Comunidades de código abierto
- Bitcoin y proyectos del ecosistema Lightning
- Grupos de estudiantes o promotores
- Organizaciones ciudadanas
- Medios de comunicación independientes
- Agrupaciones y asociaciones locales



**¿Por qué es esto interesante?





- herramienta 100% de código abierto
- Comunicación soberana y descentralizada**
- Espacios organizados en **salones**, **subgrupos**, **salones privados**, etc.
- Integración con Nextcloud, GitLab, Mattermost o bots personalizados
- Gestión más precisa de los permisos y la moderación



Matrix se convierte así en un pilar de comunicación para cualquier estructura que desee mantenerse independiente de las grandes plataformas centralizadas.



## Conclusión



Matrix representa una solución moderna, abierta y segura para la comunicación en tiempo real, ofreciendo una alternativa descentralizada a las plataformas tradicionales. Gracias a su arquitectura federada y a sus avanzados protocolos de cifrado, permite a los usuarios conservar el control de sus datos al tiempo que disfrutan de una experiencia fluida e interoperable. Ya sea para uso personal, profesional o comunitario, Matrix ofrece un marco robusto y escalable para construir entornos de comunicación adaptados a las necesidades actuales.



Para saber más y descubrir todas las funciones que ofrece Matrix, puede consultar la documentación oficial disponible aquí :


[https://matrix.org/docs/](https://matrix.org/docs/)