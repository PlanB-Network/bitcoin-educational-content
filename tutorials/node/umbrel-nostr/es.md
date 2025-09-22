---
name: Umbrel Nostr
description: Configuración y uso de aplicaciones Nostr en Umbrel
---

![cover](assets/cover.webp)



## Requisitos previos: Instalación de Umbrel



Umbrel es una plataforma de código abierto que te permite alojar fácilmente aplicaciones de Bitcoin y otros servicios en tu propio servidor personal. Es una solución todo en uno que simplifica enormemente el autoalojamiento de nodos Bitcoin y aplicaciones descentralizadas.



Asegúrate de haber instalado Umbrel siguiendo nuestra guía de instalación:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Introducción a Nostr



**Nostr** es un protocolo de red abierto y descentralizado diseñado para redes sociales. Su nombre significa _"Notas y Otras Cosas Transmitidas por Relés"_. Permite a cualquiera publicar mensajes (notas), gestionados como eventos JSON, y propagarlos a través de servidores de retransmisión en lugar de una plataforma centralizada. Cada usuario posee un par de claves criptográficas (privada/pública) que le sirven de identificador: la clave pública (npub) identifica al usuario, y la privada (nsec) permite firmar los mensajes. Gracias a esta arquitectura distribuida, **Nostr ofrece resistencia a la censura** y una gran flexibilidad: puede utilizar varios clientes y conectarse a tantos relés como desee, sin depender de un único servidor.



En resumen, Nostr es un protocolo de comunicación descentralizado en el que los **clientes** (aplicaciones de usuario) envían y reciben eventos a través de **relayers** (servidores). Este protocolo ha sido especialmente popular entre la comunidad Bitcoin desde 2023, debido a sus valores de descentralización y soberanía de datos.



**Nota:** Para utilizar Nostr, necesitarás tu clave privada (generada por un cliente Nostr o a través de una extensión dedicada). **Nunca compartas tu clave privada**, ya que permitiría a cualquiera hacerse pasar por ti. Guárdala en un lugar seguro y utiliza herramientas seguras de gestión de claves (ver Consejo más abajo).



## Aplicaciones para Nostr en Umbrel



Umbrel ofrece un ecosistema de aplicaciones integradas para aprovechar al máximo Nostr en tu nodo personal. Vamos a detallar el uso de las principales apps relacionadas con Nostr: **Nostr Relay**, **noStrudel**, **Snort** y **Nostr Wallet Connect**. Cada una de ellas responde a una necesidad específica: _Nostr Relay_ es un **servidor de retransmisión privado**, _noStrudel_ y _Snort_ son **clientes de Nostr** (interfaces para leer/publicar notas), mientras que _Nostr Wallet Connect_ es una herramienta para vincular tu **cartera de Lightning** a Nostr.



### Nostr Relay - Tu repetidor privado en Umbrel



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay** es la aplicación oficial de Umbrel para ejecutar tu **propio relé de Nostr** en tu nodo. El objetivo principal es tener un **relé privado** y fiable para **respaldar toda tu actividad en Nostr** en tiempo real. En otras palabras, utilizando este relé personal además de los relés públicos, te aseguras de que todas tus notas, mensajes y reacciones se copien en casa, a salvo de la censura o la pérdida de datos.



**Instalación:** Desde la App Store de Umbrel (categoría _Social_), instala _Nostr Relay_. Una vez lanzada, la aplicación se ejecuta en segundo plano (docker service).



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



Verás su web Interface a través de Umbrel: proporciona información básica y, sobre todo, la URL de tu repetidor (arriba a la derecha), que tendrás que copiar para su uso posterior. También dispone de un botón de sincronización (icono del globo terráqueo).



**Para aprovechar su relé Umbrel:**



**Añade el relé a tu cliente Nostr:** En tu aplicación cliente (por ejemplo, Damus en iOS, Amethyst en Android, Snort o noStrudel en Umbrel, etc.), añade la URL de tu relé privado que has copiado antes. Por defecto, el relé Umbrel escucha en el puerto **4848**. Si accedes a él en la red local, esto da una URL como: `ws://umbrel.local:4848` (o utiliza la IP local de Umbrel).



Si usas Tailscale (ver más abajo), puedes incluso usar el alias DNS de MagicDNS (normalmente `umbrel` o un nombre autogenerado) para acceder desde cualquier lugar, siempre en el puerto 4848.



Si prefieres Tor, obten la dirección .onion de Umbrel y utilízalo con el puerto 4848 a través de un navegador o cliente compatible con Tor (consulta la sección Tor)



Una vez añadida la URL a la configuración de relés de tu cliente Nostr, conéctate a este relé. Deberías ver en tu cliente que el relé Umbrel está conectado (normalmente indicado por un punto verde o similar).



**Sincronizar historial (opcional)**: En la Interface web de _Nostr Relay_ en Umbrel, haz clic en el icono **globo** 🌐 (en la parte superior de la página). Esta acción obligará a tu relé Umbrel a conectarse a tus otros relés (los configurados en tu cliente) para **importar tus actividades públicas** antiguas. Esto significa que las notas anteriores que hayas publicado o leído a través de los repetidores públicos también se descargarán y almacenarán en tu repetidor privado. Por favor, espera a que se realice la sincronización.



**Utiliza Nostr como de costumbre:** A partir de ahora, cualquier nueva actividad (notas publicadas, reacciones, mensajes privados encriptados, etc.) que realices en Nostr será reenviada como de costumbre a los relés públicos **y en paralelo a tu relé Umbrel**. Si tu cliente Nostr está correctamente configurado, enviará cada evento a todos los repetidores (incluido el tuyo). Tu repetidor privado actuará como respaldo en tiempo real. Incluso en caso de desconexión temporal, sus clientes podrán resincronizar posteriormente los datos que falten gracias a este relé. esto le proporciona un control total sobre sus datos de Nostr



En segundo plano, el _Nostr Relay_ de Umbrel se basa en el proyecto de código abierto **nostr-rs-relay** (implementación del protocolo Rust). Es compatible con todo el protocolo Nostr y con numerosos NIP estándar (NIP-01, 02, 03, 09, 11, 12, 15, 16, 20, 22, 26, 28, 33, etc.), lo que garantiza la máxima compatibilidad con los clientes.



### noStrudel - Cliente Nostr para exploradores



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel** es un cliente web de Nostr orientado a usuarios avanzados, ideal para entender y explorar la red Nostr en detalle. Es una especie de caja de arena para inspeccionar eventos y relés, y para experimentar con las características avanzadas del protocolo. La Interface está en inglés y es relativamente técnico, por lo que resulta ideal para usuarios experimentados que sientan curiosidad por el funcionamiento interno de Nostr.



**Instalación:** Instala _noStrudel_ desde la App Store de Umbrel (categoría _Social_). Una vez lanzado, se puede acceder a través de tu navegador en la dirección de Umbrel (por ejemplo, `http://umbrel.local` o a través de .onion/Tailscale, consulta la sección de acceso externo).



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**Configurar relés:** Cuando abras noStrudel, verás un botón "Configurar relés" en la esquina superior derecha. Haz clic en él para configurar tus relés.



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



En esta página, pega la URL de tu relé Umbrel que copiaste anteriormente. También puedes añadir otros relés propuestos por defecto por la aplicación. Una vez que hayas configurado tus relés, haz clic en "Iniciar sesión" en la parte inferior izquierda para continuar.



![Options de connexion dans noStrudel](assets/fr/06.webp)



**Conexión:** noStrudel te ofrece varias opciones de conexión. En nuestro caso, elegiremos "Private Key" y pegaremos tu clave privada de Nostr generada previamente. Si aún no tienes una clave, puedes instalar la extensión [Nostr Connect] (https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj) para crear y/o guardar tus claves de Nostr y así comunicarte de forma más segura con las distintas aplicaciones de Nostr.



![Interface principale de noStrudel](assets/fr/07.webp)



Una vez conectado, ya puedes utilizar noStrudel para compartir tus notas a través de Nostr. La interfaz te da acceso a:





- Mneú completo de Nostr con cronología de notas, notificaciones, mensajería, búsqueda de perfiles
- Gestión de relés y estado de las conexiones
- Herramientas avanzadas para examinar eventos y su contenido JSON
- Opciones de configuración de los filtros temporales y los PIN



**Consejo:** En _noStrudel_, puedes configurar _filtros de línea de tiempo_ o probar diferentes _NIPs (Nostr Implementation Possibilities)_. Por ejemplo, comprobar la compatibilidad con NIP-05 (identificadores descentralizados) o características más recientes. Esto convierte a _noStrudel_ en una herramienta excelente para experimentar en un entorno controlado.



### Snort - Cliente moderno de Nostr en Umbrel



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort** es otro cliente web de Nostr disponible en Umbrel, que ofrece una **Interfaz** moderna, rápida y despejada para interactuar con la red social descentralizada. A diferencia de noStrudel, que apunta a usuarios avanzados, _Snort_ apunta a la simplicidad de uso sin sacrificar la funcionalidad. Está construido en React, y ofrece una UX limpia que recuerda a las redes sociales clásicas, por lo que es adecuado para el uso diario.



**Instalación:** Instala _Snort_ desde la App Store de Umbrel (categoría _Social_).



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



Cuando abras Snort, verás un botón de "Registro" en la esquina inferior izquierda.



![Options de connexion dans Snort](assets/fr/10.webp)



Puedes elegir registrarte o conectarte a una cuenta existente (que es lo que vamos a hacer para este tutorial).



![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snort ofrece varios métodos de conexión. Puedes utilizar la extensión Nostr Connect previamente instalada u otros métodos disponibles. Una vez conectado, podrás utilizar la aplicación al máximo.



La Interfaz de _Snort_ ofrece:





- Una pantalla **Posts/Conversaciones/Global** para navegar entre tus notas, los hilos de discusión o el feed global
- Pestañas para **Notificaciones**, **Mensajes** (DM), **Búsqueda**, **Perfil**, etc.
- Un botón **+** o _Escribir_ para publicar una nueva nota
- Gestión de **suscripciones (siguientes)** y **listas**
- Menú de gestión de relés para añadir/eliminar relés y hacer un seguimiento de su disponibilidad



**Configuración recomendada del relé:** Para añadir tu relé Umbrel, ve a Configuración - Relés. Introduce la URL de tu relé (`ws://umbrel:4848` u otra URL dependiendo de tu configuración) en la lista de relés de Snort. De esta forma, Snort publicará tus notas en tu relé privado además de en los públicos.



### Nostr Wallet Connect - Enlaza tu billetera Lightning a Nostr



**Nostr Wallet Connect (NWC)** es una aplicación que **conecta tu nodo Umbrel (Lightning)** a aplicaciones Nostr compatibles para realizar pagos Lightning (por ejemplo, enviar _zaps_, esos micropagos por "gustar" contenido). En este tutorial, veremos cómo conectar noStrudel a tu nodo Lightning para realizar pagos directamente desde la Interfaz.



**Instalación y configuración:**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



Instala _Nostr Wallet Connect_ de la tienda Alby en Umbrel.



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



En noStrudel, haz clic en tu perfil en la esquina superior derecha y, a continuación, en el botón "Gestionar".



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



Haz clic en "Lightning" y luego en "connect Wallet".



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



Entre las opciones de conexión disponibles, selecciona "Umbrel".



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



Haz clic en "Conectar" para ser redirigido automáticamente a tu sesión de Umbrel Nostr Wallet Connect.



![Page de configuration des autorisations NWC](assets/fr/17.webp)



En la página Nostr Wallet Connect, puedes:




   - Definir tu presupuesto máximo
   - Validar autorizaciones
   - Establecer un tiempo de caducidad para la conexión


Haz clic en "conectar" para finalizar.



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



Se te redigirá a noStrudel con un mensaje de confirmación: ¡ya puedes zappear el mundo entero desde tu nodo Wallet/LND!



Gracias a NWC, tus **pagos Lightning a través de Nostr** (zaps a puestos de recompensa, pagos _Valor por Valor_, etc.) parten de **tu propio nodo**. Ya no tienes que dirigir tus transacciones a través de servicios externos o escanear un QR desde tu teléfono cada vez. La experiencia del usuario mejora enormemente, sin dejar de ser _no custodial_ y respetuosa con la privacidad.



Si quieres saber cómo configurar tu propio nodo Lightning en Umbrel, te recomiendo que eches un vistazo a este otro completo tutorial:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Configuración y seguridad avanzadas



Utilizar Umbrel y Nostr juntos a un nivel avanzado requiere especial atención a la **seguridad** y la **conectividad**. Aquí tienes algunos consejos para proteger tu configuración y acceder a ella de forma óptima, estés donde estés.



### Acceso externo seguro: Tor y Tailscale



Por razones de seguridad, tu Umbrel sólo es accesible por defecto en tu red local (y a través de Tor). Para interactuar con Nostr fuera de casa, tienes dos soluciones preferidas: **Tor** (acceso anónimo vía red Onion) y **Tailscale** (malla VPN privada).





- **Acceso vía Tor:** Umbrel configura automáticamente un **servicio Tor (.onion)** para su Interfaz web y sus aplicaciones. Esto significa que puedes acceder a la Interfaz de Umbrel (incluyendo _noStrudel_ o _Snort_) desde cualquier lugar, usando el navegador Tor, sin exponer tu IP pública. _Tor se utiliza para acceder a tus servicios Umbrel desde fuera de tu red local, sin exponer tu dispositivo a Internet ([Configura Tor en tu sistema - Guías - Comunidad Umbrel](https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Official%20website%3A%20https%3A%2F%2Fwww))._ Para utilizar esta opción, ve a la configuración de Umbrel y recupera la URL .onion de tu Umbrel (o escanea el código QR proporcionado). En un navegador Tor, accede a esta dirección .onion: Obtendrás la misma Interfaz que localmente. Entonces podrás usar tus aplicaciones Nostr como en casa.


**Relé Nostr a través de Tor:** Si quieres que tus clientes (o amigos autorizados) puedan acceder a tu relé Nostr a través de Tor, es posible. Umbrel no proporciona la dirección .onion del relé directamente, pero como se ejecuta en el puerto 4848, puedes:





    - Utilizar la dirección .onion de UI Umbrel y configurar tu cliente para que se conecte a través de esta Interfaz (poco práctico para WebSocket),





    - **O** exponer el puerto 4848 como un servicio .Onion separado. Esto requiere jugar con la configuración de Tor en Umbrel (reservado para usuarios avanzados cómodos con SSH). Alternativamente, considera un **túnel Tor** en otro servidor que redirija a Umbrel: sin embargo, para uso personal, es más fácil usar Tailscale.





- **Acceso a través de Tailscale:** [Tailscale](https://tailscale.com/) es una solución VPN en malla que crea una red privada virtual entre tus dispositivos y Umbrel. La ventaja: funciona como si estuvieras en una LAN, pero a través de Internet, encriptada y sin configuraciones complejas. **Tailscale asigna a tu Umbrel una IP fija y un nombre de dominio privado, independientemente de su ubicación en la red ([Tailscale | Umbrel App Store](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,reviewed%20and%20trusted%20standard))**. En la práctica, una vez que hayas instalado Tailscale en Umbrel (desde la App Store de Umbrel, categoría _Redes_) **y** en tus dispositivos (móvil, PC...), podrás llegar a Umbrel a través de una dirección del tipo `100.x.y.z` (IP de Tailscale) o un nombre como `umbrel.tailnet123.ts.net`.


para Nostr_, Tailscale es extremadamente útil: tu móvil, si tiene Tailscale activo, podrá conectarse a `ws://umbrel:4848` (gracias a MagicDNS) o directamente a la IP y puerto 4848 de Tailscale para usar el relé. Clientes como Damus o Amethyst verán tu Umbrel como si estuviera en la misma red local. **Consejo:** Habilita la opción **MagicDNS** en Tailscale para usar el nombre de host `umbrel` en lugar de memorizar la IP. Esto asegura una conexión fluida con tu relé incluso cuando estás en movimiento ([Nostr Relay | Umbrel App Store](https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past)).


Es más, Tailscale te permite acceder al Interface Umbrel (y por tanto a los clientes web _noStrudel/Snort_) a través de un simple navegador, usando la IP privada o el nombre de dominio asignado. No hay necesidad de un Navegador Tor, y las velocidades de transferencia de datos son generalmente mejores que a través de la red Tor.




**Nota:** Tor y Tailscale no son mutuamente excluyentes. Puedes mantener Tor activo para acceso anónimo o servicios específicos, y usar Tailscale en el día a día por su simplicidad. En ambos casos, no necesitas abrir un puerto en tu router, lo que refuerza la seguridad.



### Protección de tu repetidor Nostr (prácticas recomendadas)



Si alojas un repetidor Nostr en Umbrel, especialmente en un contexto avanzado, asegúrate de aplicar algunas buenas prácticas:





- **Relé privado o restringido:** Por defecto, tu relé Umbrel es privado (no se anuncia públicamente) y, si sólo accedes a él a través de Tailscale o de tu LAN, seguirá siendo inaccesible para extraños. **Mantén la confidencialidad del enlace ** No lo difundas en redes Nostr públicas a no ser que quieras alojar voluntariamente a otros usuarios, lo cual es otro tema (moderación, ancho de banda, etc.). Para uso personal, recomendamos limitar el acceso a ti mismo y, si es necesario, a unos pocos amigos y familiares de confianza.





- **Lista blanca / Autenticación**: La implementación de nostr-rs-relay soporta un mecanismo de autenticación **NIP-42** así como _listas blancas_ de claves públicas. Activando estas opciones, puedes restringir tu relé para que **sólo acepte eventos firmados por ciertas claves (las tuyas)**, o que los clientes deban autenticarse para publicar. configurar esto requiere editar el archivo de configuración `config.toml` del relé en Umbrel (vía SSH en el contenedor Docker)._ Es una manipulación avanzada, pero por ejemplo puedes listar los anuncios permitidos (`pubkey_whitelist`). De esta forma, aunque alguien descubra tu repetidor, no podrá publicar nada allí si no está en la lista.





- **Actualizaciones y mantenimiento:** Mantén tu Umbrel y la aplicación _Nostr Relay_ al día. Las actualizaciones pueden incluir mejoras de rendimiento (por ejemplo, mejor gestión del spam) y correcciones de seguridad. En Umbrel, comprueba regularmente en el App Store si hay actualizaciones de _Nostr Relay_ y aplícalas cuando sea necesario.





- **Monitorización y límites:** Vigila cómo se utiliza tu relé. Si lo abres a otros, vigila la carga (CPU/almacenamiento RAM) de tu Umbrel, ya que un relé puede acumular rápidamente muchos datos. nostr-rs-relay ofrece **límites de tasa y almacenamiento** configurables (`limits` en la configuración, por ejemplo, número de eventos por segundo, tamaño máximo de evento, purga de eventos antiguos...). Para uso privado, es probable que no necesites tocarlos, pero ten en cuenta que estos parámetros existen por si los necesitas ([nostr-rs-relay/config.toml at master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.toml#:~:text=)).





- **Asegurar las claves de Nostr:** Este punto ya se ha mencionado, pero es crucial: nunca introduzcas tus claves privadas de Nostr en una Interfaz en el que no confíes plenamente. En su lugar, utiliza extensiones de navegador o dispositivos externos (como _signers_ de Nostr en teléfonos independientes) para firmar acciones sensibles. En Umbrel, tus clientes web como _Snort_ y _noStrudel_ pueden funcionar sin conocer tu clave secreta, a través de NIP-07. Aproveche esta oportunidad para combinar comodidad y seguridad.




Siguiendo estos consejos, tu integración de un nodo Umbrel con Nostr será a la vez potente **y** segura. Tendrás un entorno completo: un nodo Bitcoin para pagos Lightning, un relé Nostr privado para la soberanía de datos y clientes web Nostr de alto rendimiento para navegar por esta nueva red social descentralizada. ¡Disfruta explorando Nostr con Umbrel!
