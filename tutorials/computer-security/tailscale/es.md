---
name: Tailscale
description: Tutorial avanzado de Tailscale
---
![cover](assets/cover.webp)



## 1. Introducción



Tailscale es una VPN de nueva generación que crea una red mallada encriptada entre tus dispositivos. Te permite conectar máquinas remotas como si estuvieran en la misma red local, sin configuraciones complejas ni apertura de puertos.



Para el autoalojamiento, Tailscale asigna a cada dispositivo una IP privada fija en una red virtual, ofreciendo un acceso estable a tus servicios incluso cuando tu IP pública cambia. Esto significa que puedes gestionar tus servidores de forma remota, sin exponer tus servicios directamente a Internet.



**Aplicaciones principales:**




- Gestionar un servidor personal desde el exterior
- Gestionar nodos Umbrel/Lightning más rápido que Tor
- Acceso seguro a una Raspberry Pi o NAS
- Conectarte a tus servicios a través de SSH o HTTP sin una configuración de red compleja



Este enfoque centrado en la simplicidad permite a los autoalojadores acceder a sus servicios de forma segura, evitando los escollos de las VPN tradicionales.



## 2. Cómo funciona Tailscale



A diferencia de las VPN tradicionales, que dirigen todo el tráfico a través de un servidor central, Tailscale crea una red en malla en la que los dispositivos se comunican directamente entre sí. El servidor central solo se encarga de la autenticación y la distribución de claves, sin ver los datos de los usuarios.



![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)


*Figura 1: VPN tradicional con arquitectura hub-and-spoke en la que todo el tráfico pasa por un servidor central*



Basándose en WireGuard, cada dispositivo genera sus propias claves criptográficas. El servidor de coordinación distribuye las claves públicas a los nodos, que establecen entonces túneles cifrados de extremo a extremo directamente entre ellos. Para atravesar los cortafuegos, Tailscale utiliza NAT traversal y, como último recurso, repetidores DERP que mantienen el cifrado.



![VPN maillé (mesh)](assets/fr/02.webp)


*Figura 2: Red mallada a escala de cola en la que los dispositivos se comunican directamente entre sí*



Todas las comunicaciones se cifran con WireGuard. Tailscale sólo ve los metadatos (conexiones), pero nunca el contenido de los intercambios. Para una mayor soberanía, Headscale permite que el servidor de coordinación sea autoalojado.



**Seguridad y confidencialidad:** Gracias a WireGuard, todas las comunicaciones en Tailscale están encriptadas de extremo a extremo. Tailscale no puede leer tu tráfico: sólo tus dispositivos tienen las claves privadas necesarias. El servicio sólo ve metadatos: Direcciones IP, nombres de dispositivos, marcas de tiempo de conexión y registros de conexión peer-to-peer (sin contenido).



Sin embargo, esta arquitectura depende de Tailscale Inc. para la coordinación de la red. Para eliminar esta dependencia, Headscale ofrece una alternativa de código abierto que permite autoalojar el servidor de control mientras utiliza los clientes oficiales de Tailscale, garantizando así una soberanía total sobre su infraestructura de red, a costa de una configuración más técnica.



**Para una explicación detallada del funcionamiento interno de Tailscale, incluyendo la gestión del plano de control, NAT traversal y DERP relays, recomendamos el excelente artículo [How Tailscale Works](https://tailscale.com/blog/how-tailscale-works) en el blog oficial. Este artículo explica en profundidad los conceptos técnicos que hacen que Tailscale sea tan potente.



## 3. Instalación de Tailscale



Tailscale funciona en los sistemas operativos **más comunes** (Windows, macOS, Linux, iOS, Android). Se dice que la instalación es "rápida y sencilla" en todas las plataformas. Empecemos echando un vistazo a su Interfaz y a cómo crear una cuenta, para pasar después a los procedimientos de instalación para distintos entornos.



### 3.1 Creación de una cuenta Tailscale



Dirígete a [https://tailscale.com/](https://tailscale.com/) y haz clic en el botón "Empezar" en la parte superior derecha de la página.




![Page d'accueil Tailscale](assets/fr/03.webp)


*La página de inicio de Tailscale explica el concepto y ofrece un inicio gratuito*



Para utilizar Tailscale, primero tienes que crear una cuenta a través de un proveedor de identidades:



![Page de connexion Tailscale](assets/fr/04.webp)


*Elección del proveedor de identidad para conectarse a Tailscale (Google, Microsoft, GitHub, Apple, etc.)*



Después de iniciar sesión, Tailscale te pedirá información sobre el uso que le vas a dar:



![Questionnaire d'utilisation](assets/fr/05.webp)


*Formulario para comprender mejor tu caso de uso (personal o profesional)*



Una vez creada tu cuenta, puedes instalar Tailscale en tus dispositivos:



![Ajout du premier appareil](assets/fr/07.webp)


*Tailscale te permite instalar la aplicación en diferentes sistemas*



### 3.2 Instalación en distintas plataformas





- **En Windows y MacOS:** Sólo tienes que descargar la aplicación gráfica desde el sitio web oficial de Tailscale e instalarla (archivo .msi en Windows, archivo .dmg en Mac). Una vez instalada, la aplicación lanza una Interfaz gráfica que te permite conectarte (a través de un navegador) a tu cuenta de Tailscale para autenticar la máquina.



![Connexion d'un appareil macOS](assets/fr/08.webp)


*Conecta un MacBook a la red trasera*



![Connexion réussie](assets/fr/09.webp)


*Confirmación de que el dispositivo está conectado a la red Tailscale*





- **En Linux (Debian, Ubuntu, etc.):** Tienes varias opciones. El método más sencillo es ejecutar el script de instalación oficial: por ejemplo, en Debian/Ubuntu :



```bash
curl -fsSL https://tailscale.com/install.sh | sh
```



Este script añadirá el repositorio oficial de Tailscale e instalará el paquete. También puedes [añadir manualmente el repositorio APT](https://pkgs.tailscale.com) o usar paquetes regulares Snap o APT. Una vez instalado, daemon `tailscaled` se ejecutará en segundo plano. Entonces necesitarás **autenticar el nodo** (ver Interfaz CLI vs web más abajo). En otras distribuciones (Fedora, Arch...), el paquete también está disponible a través de los repositorios estándar o el script de instalación universal. Para un servidor headless, utiliza CLI: por ejemplo `sudo tailscale up --auth-key <key>` si utilizas una clave de autenticación pregenerada, o simplemente `tailscale up` para un login interactivo (que proporcionará una URL a visitar para autenticar el dispositivo).





- **En sistemas basados en ARM (Raspberry Pi, etc.):** Generalmente estamos en Linux, así que el mismo enfoque que el anterior (script o paquete). Ten en cuenta que Tailscale soporta arquitectura ARM32/ARM64 sin problemas. Muchos usuarios instalan Tailscale en Raspberry Pi OS vía apt o en distribuciones ligeras (DietPi, etc.) para acceder a su Pi en cualquier lugar.





- **En iOS y Android:** Tailscale proporciona aplicaciones móviles **oficiales**. Solo tienes que instalar *Tailscale* desde la [App Store](https://apps.apple.com/us/app/tailscale/id1470499037?ls=1) (iOS) o la [Play Store](https://play.google.com/store/apps/details?id=com.tailscale.ipn) (Android).



![Installation sur iPhone](assets/fr/11.webp)


*Pasos para instalar Tailscale en iPhone: bienvenida, privacidad, notificaciones, VPN*



![Connexion sur iPhone](assets/fr/12.webp)


*Conéctate a tailnet, selecciona la cuenta y valídala en el iPhone*



Una vez instalada la aplicación, en el primer inicio te pedirá que te autentiques a través del proveedor elegido (Google, Apple ID, Microsoft, etc., dependiendo de lo que estés usando para Tailscale) - es el mismo procedimiento que en otras plataformas, normalmente una redirección a una página web OAuth. Después, la aplicación móvil crea la VPN (en iOS tendrás que aceptar el complemento de configuración de VPN). A continuación, la aplicación puede ejecutarse en segundo plano, dándote acceso a tu tailnet desde cualquier lugar. *Ten en cuenta que:* en el móvil, sólo puedes tener **una VPN activa a la vez** - así que asegúrate de que no tienes otra VPN conectada al mismo tiempo, o Tailscale no podrá establecer la suya propia. En Android, puedes configurar un perfil de trabajo separado si quieres aislar ciertos usos (por ejemplo, un perfil con Tailscale activo para una app determinada).



### 3.3 Añadir varios dispositivos y validación



Una vez que tu primer dispositivo esté conectado, Tailscale te pedirá que añadas otros dispositivos a tu red:



![Ajout d'appareils supplémentaires](assets/fr/10.webp)


*Interfaz mostrando el primer dispositivo conectado y a la espera de otros dispositivos*



Una vez que hayas añadido varios dispositivos, puedes comprobar que pueden comunicarse entre sí:



![Test de connectivité entre appareils](assets/fr/13.webp)


*Confirmación de que los dispositivos pueden comunicarse entre sí mediante ping*



A continuación, Tailscale sugiere configuraciones adicionales para mejorar tu experiencia:



![Suggestions de configuration](assets/fr/14.webp)


*Sugerencias para configurar el DNS, compartir dispositivos y gestionar el acceso*



### 3.4 Panel de administración



La consola de administración web te permite ver y gestionar todos los dispositivos conectados:



![Tableau de bord des machines](assets/fr/15.webp)


*Lista de dispositivos conectados con sus características y estado*



**Interface Web vs Interface CLI:** Tailscale ofrece dos formas complementarias de interactuar con la red: la **Interfaz web de administración** y el **Cliente de línea de comandos (CLI)**.





- Interfaz Web (Admin Console)** : Accesible en [https://login.tailscale.com](https://login.tailscale.com), esta consola web es el panel central para tu red Tailscale. Lista todos los dispositivos (*Máquinas*), su estado online/offline, sus direcciones IP Tailscale, y más. Aquí puedes **gestionar dispositivos** (renombrar, expirar claves, autorizar rutas, deshabilitar un nodo), **gestionar usuarios** (en un contexto organizativo), y definir reglas de seguridad (ACLs). Aquí también se configuran opciones globales como MagicDNS, etiquetas o claves de autenticación (claves de autenticación pre-generate para la adición automática de dispositivos). La Interfaz web es muy útil para obtener una visión general y aplicar cambios que se propagarán a través del servidor de coordinación a todos los nodos. *Ejemplo:* Activar una **ruta de subred** o un **nodo de salida** se hace con un solo clic en la consola, una vez que el nodo en cuestión se ha anunciado como tal.





- Línea de comandos Interface (CLI):** El comando `tailscale` está disponible en CLI en cada dispositivo donde Tailscale esté instalado. Este CLI te permite hacer todo localmente: Conectar (`tailscale up`), inspeccionar el estado (`tailscale status` para ver qué peers están conectados), depurar (`tailscale ping <ip>`), etc. Algunas características son incluso **exclusivas de CLI** o más avanzadas, por ejemplo:





  - `tailscale up --advertise-routes=192.168.0.0/24` para anunciar una ruta de subred,
  - `tailscale up --advertise-exit-node` para proponer tu máquina como nodo de salida,
  - `tailscale set --accept-routes=true` (o `--exit-node=<IP>`) para consumir una ruta o utilizar un nodo de salida,
  - `tailscale ip -4` para mostrar la IP Tailscale del dispositivo,
  - `bloqueo/desbloqueo de la red de cola` (si se utiliza *bloqueo de la red de cola*, función de seguridad avanzada),
  - o `tailscale file send <node>` para utilizar **Taildrop** (transferencia de archivos entre dispositivos).


CLI es muy útil en servidores sin Interfaz gráfica, y para scripting de ciertas acciones. **Diferencias en el uso:** La mayoría de las configuraciones básicas se pueden hacer a través de la Web o a través de la CLI. Por ejemplo, añadir un dispositivo se puede hacer a través de la consola, o ejecutando `tailscale up` en el dispositivo y validando a través de la web. Del mismo modo, cambiar el nombre de un dispositivo se puede hacer a través de la consola o con `tailscale set --hostname`. **En resumen**, la consola web es ideal para la administración global de la red (especialmente con múltiples máquinas/usuarios), mientras que la CLI es útil para el control detallado de una máquina dada, scripts de automatización, o el uso en un sistema sin GUI.



## 4. Uso de Tailscale en Umbrel



Umbrel es una popular plataforma de autoalojamiento (utilizada especialmente para los nodos Bitcoin/Lightning y otros servicios autoalojados, a través de su App Store). Para instalar y configurar Umbrel, te recomendamos que sigas nuestro tutorial dedicado :



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

El uso conjunto de Umbrel y Tailscale es un caso de uso especialmente interesante, ya que Umbrel integra de forma nativa un módulo de Tailscale fácil de desplegar. A continuación te explicamos cómo se integra Tailscale con Umbrel y qué aporta:



### 4.1 Instalación y configuración de Umbrel





- Instalación de Tailscale en Umbrel:** Umbrel tiene una aplicación oficial de Tailscale en su App Store. La instalación no puede ser más sencilla:



![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)


*Página de la aplicación Tailscale en la Umbrel App Store*



Desde el Interface Web Umbrel, abre la App Store, busca **Tailscale** y pulsa *Instalar*. Unos segundos después, la aplicación se instala en el Umbrel. Al abrirla, Umbrel muestra una página que te permite vincular tu nodo a Tailscale.



![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)


*Pantalla de conexión Tailscale en el Interface* de Umbrel



Sólo tienes que **hacer clic en "Iniciar sesión "**, que te redirigirá a la página de autenticación de Tailscale:



![Page d'authentification Tailscale](assets/fr/18.webp)


*Conectarse a Tailscale a través de un proveedor de identidades*



Puedes autenticarte a través de tu cuenta de Tailscale (Google/GitHub/etc.) o introducir tu correo electrónico. Normalmente, en Umbrel, la Interfaz te pide que visites [https://login.tailscale.com](https://login.tailscale.com) e inicies sesión - esto autentica la aplicación Umbrel Tailscale.



![Confirmation de connexion réussie](assets/fr/19.webp)


*Confirmación de que el dispositivo Umbrel está conectado a la red Tailscale*



Una vez hecho esto, tu Umbrel está "dentro" de tu red Tailscale y aparece en tu consola con un nombre (por ejemplo *umbrel*). A continuación, puedes hacer clic en la IP Address de tus dispositivos para copiarla, recuperar la dirección IPv6 o tu MagicDNS asociada a tu dispositivo.



![Console Tailscale avec appareils connectés](assets/fr/20.webp)


*Consola de administración de Tailscale mostrando varios dispositivos conectados, incluido Umbrel*




### 4.2 Acceso remoto a los servicios de Umbrel



Una vez que Umbrel está conectado a Tailscale, **puedes acceder a la Interfaz Umbrel y a las aplicaciones que se ejecutan en él, desde cualquier lugar, como si estuvieras en la red local**. Esta es una de las principales ventajas sobre Tor.



El acceso es extraordinariamente sencillo: en lugar de utilizar `umbrel.local` (que solo funciona en tu red local), utilizas la IP Address de tu Tailscale Umbrel (`http://100.x.y.z`) directamente desde cualquier dispositivo conectado a tu tailnet. Esto funciona sin importar dónde estés o qué conexión a Internet estés utilizando (4G, Wi-Fi pública, red corporativa).



**Ejemplos de aplicaciones alojadas en Umbrel accesibles a través de Tailscale:**





- **Interfaz Umbrel principal**: Acceda a tu panel de Umbrel simplemente escribiendo `http://100.x.y.z` en tu navegador
- **Nodo Bitcoin**: Gestiona tu nodo Bitcoin sin latencia, ve la sincronización y las estadísticas
- **Nodo Lightning**: Utiliza ThunderHub, RTL u otras interfaces de gestión de Lightning con capacidad de respuesta inmediata
- **Mempool**: Ve las transacciones de Bitcoin y Mempool sin retrasos de Tor
- **NoStrudel**: Accede a tus servicios Nostr alojados en Umbrel



**Conecta monederos externos a tus nodos Bitcoin o lightning a través de Tailscale :**



Tailscale también permite que tus monederos Bitcoin y Lightning instalados en otros dispositivos se conecten directamente a tu nodo Umbrel:





- **Sparrow wallet (Bitcoin)**: Esta Wallet Bitcoin externa puede conectarse directamente al servidor Electrum de su Umbrel utilizando la dirección IP Tailscale:



![Configuration Electrum dans Sparrow](assets/fr/21.webp)


*Configuración de un servidor Electrum privado en Sparrow wallet utilizando la dirección IP Tailscale de Umbrel*



![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)


*Lista de alias del servidor Electrum en Sparrow con la dirección IP Tailscale de Umbrel*



Lee nuestra guía completa para configurar Sparrow wallet con tu nodo Bitcoin:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d




- **Zeus (Lightning)**: Esta billetera móvil Lightning puede conectarse a tu nodo Lightning en Umbrel. En lugar de configurar el endpoint como `.onion', simplemente configura la IP Tailscale de tu Umbrel y el puerto Lightning API. La conexión será instantánea en comparación con Tor.



![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)


*Configuración de Zeus para conectarse al nodo Lightning a través de la dirección IP Tailscale*



Para configurar Zeus con tu nodo Lightning, consulta nuestro tutorial detallado :



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Para saber más sobre la Lightning Network y su funcionamiento en Umbrel, visita :



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16



### 4.3 Ventajas sobre Tor



Umbrel ofrece de forma nativa acceso remoto a través de Tor (proporcionando direcciones `.onion` para sus servicios web). Aunque Tor tiene la ventaja de la confidencialidad (anonimato) y no requiere registro, muchos usuarios encuentran **Tor lento e inestable** para el uso diario (las páginas se cargan lentamente, tiempos de espera, etc.) - *"Umbrel vía Tor es tan lento "* se quejan algunos.



Tailscale ofrece una conexión generalmente **más rápida y de baja latencia**, ya que el tráfico pasa directamente (o a través de un relé rápido) en lugar de rebotar a través de 3 nodos Tor. Lo que es más, Tailscale proporciona una experiencia de "red local": se utilizan IPs privadas, y las aplicaciones se pueden mapear directamente (por ejemplo, unidad de red SMB en \100.x.y.z).



Dicho esto, Tor tiene la ventaja de estar descentralizado y "fuera de la caja" en Umbrel, mientras que Tailscale implica confiar en un tercero (o alojar headscale). Tor también es útil para el acceso sin cliente (desde cualquier navegador Tor, puedes consultar la UI de Umbrel, mientras que Tailscale requiere el cliente instalado en el dispositivo de acceso).



**En resumen**, para un uso interactivo (billeteras Lightning, interfaces web frecuentes), Tailscale ofrece una comodidad y velocidad apreciables en comparación con Tor, al precio de una ligera dependencia externa. Mucha gente elige usar *ambos*: Tailscale en el día a día, y Tor como alternativa o para compartir el acceso con alguien sin invitarle a su VPN.



### 4.4 Seguridad



Al utilizar Tailscale con Umbrel, evitas exponer Umbrel a Internet. El nodo Umbrel solo es accesible para tus otros dispositivos autenticados en la tailnet, lo que reduce considerablemente la superficie de ataque (ningún puerto abierto a extraños, ningún riesgo de ataque al servicio web a través de Internet).



Las comunicaciones se cifran (WireGuard) además de cualquier cifrado que tus servicios ya estén haciendo (por ejemplo, incluso el HTTP interno está en el túnel). Aún puedes aplicar ACLs de Tailscale para, por ejemplo, evitar que un dispositivo tailnet en particular acceda a Umbrel si quieres particionar la red. Umbrel en sí no ve la diferencia - piensa que está en un servidor local.



---

Para concluir esta sección, la integración de Tailscale en Umbrel sólo requiere unos pocos clics y **mejora enormemente la accesibilidad** de tu nodo autoalojado. Podrás administrar Umbrel y sus servicios desde cualquier lugar, de forma segura y eficiente, como si estuvieras en casa. Esta es una solución particularmente útil para aplicaciones en tiempo real (Lightning) que sufren la latencia de Tor, o más generalmente para cualquier auto-alojado que busque una simple conexión privada. **Todo ello sin exponer un solo puerto** en su caja, y sin complicadas configuraciones de red.



## 5. Gestión avanzada y casos de uso



### 5.1 Funciones avanzadas de Tailscale



**Gestión de red:** La consola de administración (login.tailscale.com) te permite gestionar tus dispositivos, ver las conexiones y configurar las reglas de acceso.



**MagicDNS:** Resuelve automáticamente nombres de dispositivos (por ejemplo `raspberrypi.tailnet.ts.net`) para evitar memorizar direcciones IP.



**ACL y control de acceso:** Define con precisión quién puede acceder a qué en tu red mediante reglas JSON, ideales para aislar determinados dispositivos o restringir el acceso a servicios específicos.



**Compartir dispositivos te permite invitar a alguien a acceder a un equipo concreto sin darle acceso a toda tu red.



**Router de subred:** Una máquina Tailscale puede actuar como portal para toda una subred, permitiendo el acceso a dispositivos no Tailscale (IoT, impresoras, etc.) a través de una única máquina configurada.



**Nodo de salida:** Utiliza una máquina como puerta de acceso a Internet para salir con tu IP. Útil para Wi-Fi públicas o para saltarse restricciones geográficas.



**Taildrop:** Una alternativa segura a AirDrop, que te permite transferir archivos entre tus dispositivos Tailscale, sea cual sea su plataforma o ubicación. A diferencia de AirDrop, que se limita al ecosistema Apple y a la proximidad física, Taildrop funciona entre todos tus dispositivos (Windows, Mac, Linux, Android, iOS), incluso si están en países diferentes. Los archivos se transfieren directamente entre dispositivos con cifrado de extremo a extremo, sin pasar por un servidor central. Utiliza la línea de comandos `tailscale file cp` o la aplicación gráfica en función de tu sistema operativo.



### 5.2 Comparación con otras soluciones



**Vs OpenVPN:** Tailscale es mucho más sencillo de configurar (no hay que abrir puertos, ni gestionar certificados) pero implica depender de un servicio de terceros. OpenVPN es totalmente controlable, pero requiere más experiencia.



**Como competidor directo, ZeroTier opera en Layer 2 (Ethernet), permitiendo broadcast/multicast, mientras que Tailscale opera en Layer 3 (IP). ZeroTier ofrece mayor flexibilidad de red, mientras que Tailscale favorece la sencillez de uso.



**Tor ofrece un anonimato que Tailscale no ofrece, pero es mucho más lento. Tor está descentralizado y no requiere una cuenta, mientras que Tailscale es más rápido y ofrece una experiencia similar a la de una LAN.



**Vs WireGuard manual:** Tailscale automatiza toda la gestión de claves y conexiones que WireGuard raw requiere que manejes manualmente. Es esencialmente WireGuard + una capa de gestión simplificada.



En conclusión, Tailscale se posiciona como una solución moderna y orientada a la simplicidad, ideal para uso personal y pequeños equipos. Para los puristas del control total, Headscale ofrece una alternativa de autoalojamiento.



## 6. Conclusión



**Ventajas de Tailscale:** Tailscale ofrece varias ventajas para el autoalojamiento:





- **Simplicidad y rendimiento** - Instalación rápida en todas las plataformas sin necesidad de una configuración de red compleja. El tráfico sigue la ruta más directa entre sus máquinas (malla P2P), con el rendimiento del protocolo WireGuard y sin servidor central que limite el caudal.
- **Seguridad y flexibilidad** - Cifrado de extremo a extremo, superficie de ataque reducida y funciones avanzadas (ACL, autenticación SSO/MFA). Funciona incluso detrás de NATs o en movimiento, con routers de subred y nodos de salida para adaptar la red a sus necesidades.



**Límites:** Tenlo también en cuenta:





- **Dependencia externa** - En su versión estándar, el servicio depende de la infraestructura de Tailscale Inc. Esta dependencia puede evitarse mediante Headscale (alternativa de autoalojamiento).
- **Otras limitaciones** - Código fuente parcialmente cerrado, limitaciones de la versión gratuita para ciertos usos avanzados, no es compatible con Layer 2 (difusión/multidifusión) y necesita acceso a Internet para establecer conexiones.



**Para qué tipo de perfil?** Tailscale es ideal para autoalojamientos individuales y equipos pequeños, desarrolladores que necesitan acceso a recursos dispersos, principiantes en VPN y usuarios móviles. Para las empresas que requieren un control total, pueden ser preferibles otras soluciones como Headscale o WireGuard directamente.



**Ve mas allá** Explora Headscale para un autoalojamiento completo, API e integraciones DevOps (Terraform), o alternativas como Innernet (similar pero totalmente autoalojado) y Netmaker.



Tailscale es una herramienta esencial para el autoalojamiento, gracias a su simplicidad y eficiencia, haciendo tu infraestructura privada tan accesible como si estuviera en la nube, mientras mantienes el control en casa.



## 7. Recursos útiles



### Documentación oficial





- **Centro de documentación de Tailscale**: [docs.tailscale.com](https://docs.tailscale.com) - Documentación completa en inglés, guías de instalación, tutoriales y referencias técnicas.
- **Cómo funciona Tailscale**: [Cómo funciona Tailscale](https://tailscale.com/blog/how-tailscale-works) - Artículo detallado que explica el funcionamiento interno de Tailscale.
- **Registro de cambios**: [tailscale.com/changelog](https://tailscale.com/changelog) - Seguimiento de actualizaciones y nuevas funciones.



### Guías prácticas





- **Tutoriales Homelab**: [tailscale.com/kb/1310/homelab](https://tailscale.com/kb/1310/homelab) - Guías específicas para el autoalojamiento.
- **Configuración de un Nodo de Salida** : [tailscale.com/kb/1103/exit-nodes](https://tailscale.com/kb/1103/exit-nodes) - Guía detallada para configurar Nodos de Salida.
- **Utiliza Taildrop**: [tailscale.com/kb/1106/taildrop](https://tailscale.com/kb/1106/taildrop) - Transfiere archivos entre dispositivos Tailscale.



### Comparaciones





- **Tailscale frente a otras soluciones**: [tailscale.com/compare](https://tailscale.com/compare) - Comparaciones detalladas con otras soluciones VPN y de red (ZeroTier, OpenVPN, etc.).



### Comunidad





- **Reddit**: [r/Tailscale](https://www.reddit.com/r/tailscale/) - Debates, preguntas y comentarios.
- **GitHub**: [github.com/tailscale/tailscale](https://github.com/tailscale/tailscale) - Código fuente del cliente, donde seguir el desarrollo e informar de problemas.
- **Discord**: [discord.gg/tailscale](https://discord.gg/tailscale) - Comunidad de usuarios y desarrolladores.



Tailscale ofrece regularmente nuevos contenidos y funciones. Echa un vistazo a su [blog oficial](https://tailscale.com/blog/) para conocer las últimas noticias y casos prácticos.
