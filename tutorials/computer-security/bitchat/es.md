---
name: Bitchat
description: Mensajería descentralizada y sin Internet para una comunicación libre
---

![cover](assets/cover.webp)


![video](https://youtu.be/WfzcKAzgB9s)


*Este tutorial de vídeo de BTC Sessions te guía a través del proceso de configuración y uso de Bitchat*


Bitchat surgió de un rápido esfuerzo de creación de prototipos en el que [@jack](https://primal.net/jack) desarrolló el concepto inicial durante una sesión de codificación de fin de semana. [@calle](https://primal.net/calle) se unió al proyecto poco después para codesarrollar la implementación en Android. Jack dirige actualmente el desarrollo de la versión iOS, mientras que calle supervisa la versión Android con el apoyo de muchos otros colaboradores.


## Introducción: Chatear libremente, sin red


Imagina enviar mensajes cuando se cae Internet, durante una catástrofe natural o en lugares donde la comunicación está restringida. Bitchat lo hace posible. Se trata de una aplicación de mensajería descentralizada y entre iguales que prescinde de los servidores centrales y permite que los dispositivos hablen directamente entre sí, sin conexión alguna, mediante Bluetooth y redes malladas. Diseñada pensando en la privacidad y la resistencia, Bitchat es ideal para su uso en zonas donde la conectividad tradicional no es fiable o no está disponible, como en situaciones de catástrofe, en lugares remotos o para quienes quieren evitar la vigilancia. En esencia, Bitchat utiliza la criptografía para garantizar que cada mensaje esté cifrado de extremo a extremo, verificado y a prueba de manipulaciones.


En este tutorial, te mostraremos cómo funciona Bitchat y cómo puedes utilizarlo para una comunicación verdaderamente privada y sin conexión.


## características principales


Bitchat permite enviar mensajes sin conexión a través de estas [funciones](https://github.com/permissionlesstech/bitchat-android?tab=readme-ov-file#features):



- Compatible entre plataformas**: Compatibilidad total de protocolos entre iOS y Android.
- Red mallada descentralizada**: Descubrimiento automático de pares y retransmisión de mensajes multisalto a través de Bluetooth Low Energy (BLE)
- Cifrado de extremo a extremo**: Intercambio de claves X25519 + AES-256-GCM para mensajes privados
- Chats basados en canales**: Mensajería de grupo basada en temas con protección por contraseña opcional
- Almacenamiento y reenvío**: Los mensajes se almacenan en caché para los usuarios desconectados y se envían cuando vuelven a conectarse
- La privacidad es lo primero**: Sin cuentas, sin números de teléfono, sin identificadores persistentes
- Comandos estilo IRC: Interfaz familiar estilo `/join, /msg, /who`.
- Retención de mensajes**: Guardado opcional de mensajes en todo el canal controlado por los propietarios del canal
- Borrado de emergencia**: Pulsa tres veces el logotipo para borrar todos los datos al instante
- Moderna interfaz de usuario Android**: Jetpack Compose con Material Design 3
- Temas oscuros/claros**: Estética inspirada en el terminal a juego con la versión de iOS
- Optimización de la batería**: Exploración adaptativa y gestión de la energía


## 1️⃣ Cómo funciona Bitchat - simplemente


Bitchat te permite enviar mensajes a teléfonos cercanos directamente a través de Bluetooth (`BLE` como se indica a continuación), sin necesidad de Internet ni señal de móvil. Cuando inicias un chat, los teléfonos realizan un apretón de manos seguro para crear una clave de cifrado única y temporal para la conversación. Cada mensaje se protege con un cifrado de extremo a extremo, y se utiliza una nueva clave para cada uno, con el fin de garantizar que los mensajes anteriores permanezcan seguros incluso si tu teléfono se ve comprometido más tarde. Por último, la aplicación divide los mensajes en pequeños fragmentos y los mezcla con datos ficticios aleatorios para ocultar tu actividad de mensajería. Para los chats directos entre dispositivos, sólo funciona dentro de un rango de unos 100 metros. Es como pasar notas encriptadas en una habitación llena de gente: los dispositivos se susurran directamente entre sí, destruyendo las claves después de cada mensaje.


Bitchat también te permite unirte a salas de chat basadas en la localización utilizando el protocolo Nostr y `#geohashes`. Un geohash es un código corto, como `#u33d`, que representa un área geográfica específica, desde un barrio hasta una ciudad o región entera. Puedes "teletransportarte" a cualquier sala de chat geohash del mundo simplemente introduciendo su etiqueta. Sus mensajes se envían a través de una red descentralizada de repetidores, que protege su ubicación exacta. Además, cada vez que te unes a una sala geohash, se te asigna una nueva identidad temporal, lo que añade un nivel adicional de privacidad a tus conversaciones basadas en la ubicación.


Para obtener detalles técnicos más precisos, consulte el [Libro Blanco oficial](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md).


## 2️⃣ Instalación y configuración


### Dónde conseguir Bitchat


Puedes instalar Bitchat a través de:



- [Apple App Store](https://apps.apple.com/us/app/bitchat-mesh/id6748219622) (para dispositivos iOS)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bitchat.droid) (para dispositivos Android)


Los usuarios de Android también tienen opciones alternativas:



- Descarga el APK directamente desde la página [GitHub Releases](https://github.com/permissionlesstech/bitchat-android/releases) o
- Instalación a través de [Zapstore] compatible con Nostr (https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqgkxmmd9e3xjarrdpshgtnywfhkjeqxtfkcr)


![image](assets/en/01.webp)


**Nota**: _Este tutorial se centra principalmente en la implementación de Android. La versión de iOS puede diferir._


### Proceso de configuración


Después de la instalación, abre Bitchat para ver esta pantalla inicial de permisos. Esto es lo que tienes que hacer:


1. **Otorgar estos permisos requeridos:**


   - Acceso Bluetooth** (para descubrir a los usuarios de Bitchat cercanos)
   - Localización precisa** (Android lo requiere para la funcionalidad Bluetooth)
   - Notificaciones** (para recibir alertas de mensajes privados)

2. **Desactivar la optimización de la batería**:


   - Esto permite que Bitchat se ejecute en segundo plano
   - Mantiene continuamente las conexiones de la red mallada


Pulse sobre `Grant Permissions` , siga los `prompts` y `Disable Battery Optimization` para pasar a la siguiente pantalla.


![image](assets/en/02.webp)


Bienvenido a la pantalla principal de Bitchat. Vamos a orientarnos:


### Ajustes


Lo primero es lo primero. El menú de ajustes se abre tocando el logo de `Bitchat`.  Las siguientes opciones están disponibles:



- Ajuste la `apariencia` (sistema/luz/oscuridad).
- habilitar la "Prueba de trabajo" en geohash para disuadir el spam (opcional)
- Activa `Tor` para mejorar la privacidad.


![image](assets/en/16.webp)


### Establezca su identidad


Toca el campo `bitchat/anonXXXX` de la parte superior para elegir tu nombre de usuario. Así es como te verán los demás tanto en el modo Bluetooth como en Internet. Por ejemplo, puedes cambiar "anon2022" por un nombre de usuario de tu elección.


![image](assets/en/03.webp)


### Seleccionar canales de red


Utilice el menú `#canales de localización` (a la derecha del nombre de usuario) para cambiar de tipo de conexión:



- BLE Mesh***: Modo Bluetooth por defecto (sin Internet, de 10 a 50 metros de alcance)
- #geohashes**: Comunidades geográficas habilitadas para Internet mediante el protocolo [Nostr](https://nostr.com/)


Cuando seleccionas el modo `#geohashes`, Bitchat se integra con el protocolo Nostr para permitir comunidades geográficas. Tus mensajes se publican en "retransmisores descentralizados Nostr" en lugar de en la red peer-to-peer de Bitchat, lo que permite conversaciones más amplias pero filtradas por ubicación. Las claves de identidad de Bitchat firman criptográficamente todos los eventos de Nostr para mantener la autenticación, mientras que las etiquetas geohash (como `#u4pruyd` para un barrio) filtran los mensajes al nivel de precisión que elijas. Esto significa que puedes participar en discusiones locales sin revelar coordenadas exactas, aunque se requiere acceso a Internet.


![image](assets/en/04.webp)


### Supervisar a los compañeros

licencia: CC-BY-SA-V4

El contador de pares muestra los usuarios:



- Cercano (BLE Mesh) o
- En tu zona geohash (#geohashes)


![image](assets/en/05.webp)


## 3️⃣ Chat global y mensajes privados


Bitchat ofrece dos modos de comunicación distintos que se adaptan a diferentes necesidades:



- Canales públicos:** Para conversaciones abiertas con otras personas. Puede conectarse a través de la red de malla BLE local para usuarios cercanos o a través de un #geohash global para comunidades basadas en la ubicación y habilitadas para Internet.
- Mensajes privados:** Para conversaciones seguras e individuales. Establecen una conexión directa y cifrada para mantener la confidencialidad de los intercambios.


Comprender ambos modos le ayudará a navegar por sus conversaciones.


### Canales públicos: El Centro Comunitario


El menú `#canales de localización` (arriba a la derecha) controla tu visibilidad pública. Si seleccionas "malla", te conectarás a todos los usuarios cercanos a través de la malla BLE, normalmente dispositivos situados a una distancia de entre 10 y 50 metros. Esto crea un foro abierto donde los mensajes se difunden a todos los que están dentro del alcance, ideal para anuncios de eventos o alertas locales.


Para un mayor alcance geográfico, elige cualquier etiqueta `#geohash` para unirte a comunidades de Internet filtradas por ubicación. Estos canales utilizan el protocolo de retransmisión Nostr, que permite la comunicación entre ciudades o regiones manteniendo la relevancia de la localización. Tus mensajes aparecerán en directo para los que estén en el mismo canal, y los nuevos participantes verán automáticamente el historial de mensajes recientes al unirse.


![image](assets/en/06.webp)


### Conversaciones privadas: Seguras y encriptadas


Para iniciar una conversación privada, pulsa directamente sobre cualquier "nombre de usuario" que aparezca en "Información general". También puedes pulsar sobre el "icono de la estrella" para marcar a este usuario como favorito, lo que lo mantendrá visible en tu lista de contactos incluso cuando no esté conectado.


![image](assets/en/07.webp)


Bitchat inicia automáticamente su `security handshake` cuando empiezas un chat privado. Los dispositivos intercambian claves efímeras para crear un túnel cifrado específico para tu conversación. Este proceso garantiza la confidencialidad de todos tus mensajes y archivos compartidos gracias al cifrado continuo de extremo a extremo. Los mensajes privados permiten compartir texto y archivos.


![image](assets/en/08.webp)


## 4️⃣ Características adicionales


Puedes acceder instantáneamente al panel de acciones escribiendo `/` en cualquier lugar de Bitchat. Esto revela un menú de comandos para acciones rápidas.



- Gestionar conexiones**: `Bloquear usuarios` o `Desbloquear pares`
- Controles de canal**: `Mostrar canales` o `Unirse/crear canal`
- Interacciones sociales**: `Enviar abrazo cariñoso` o `golpear con la trucha` 🎣
- Mantenimiento del chat**: `Limpiar mensajes de chat`
- Herramientas de privacidad**: `Ver quién está conectado` o `Enviar mensaje privado`


Los comandos se ejecutan inmediatamente, como `/block Satoshi` para silenciar a los críticos o `/hug Hal` para difundir positividad 🫂.


![image](assets/en/09.webp)


## 5️⃣ Crear un canal


Los canales en Bitchat permiten una comunicación organizada en torno a temas, lugares o comunidades. Para crear el tuyo, sigue este flujo de trabajo:


### Paso 1: Crear un canal


Para crear un canal, escribe `/j` o `/join` seguido del `nombre del canal` en cualquier chat (por ejemplo, `/j <nombredelcanal>`). Tras la creación aparece un nuevo `icono ⧉` indicando el nuevo canal. Otros usuarios pueden unirse escribiendo el mismo comando (por ejemplo, `/j bitchat_tutorial`).


![image](assets/en/10.webp)


### Paso 2: Configurar los ajustes


Además de los comandos por defecto, dentro de un canal están disponibles los siguientes ajustes:



- `/save` para guardar mensajes localmente
- `/transfer` para transferir la propiedad del canal y
- `/pass` para cambiar la contraseña del canal.


Para comunidades privadas, este comando activa la protección por contraseña, requiriendo que los miembros aprobados introduzcan una contraseña personalizada antes de unirse.


## 6️⃣ Modo Pánico


Ahora, hablemos del "modo pánico": al tocar tres veces el logotipo de "Bitchat", se inicia un borrado completo de todos los mensajes y datos locales de la aplicación. Esta es la última salvaguarda de tu privacidad, perfecta para situaciones que requieren discreción inmediata.


**Recordatorio importante:** _El modo pánico es permanente. Una vez activado, los datos no se pueden recuperar. Utilícelo con precaución._


![image](assets/en/11.webp)


## 7️⃣ Geohashes


Los canales Geohash permiten conversaciones específicas basadas en "ubicaciones geográficas" en lugar de en conexiones de red tradicionales. Esta función convierte a bitchat en una herramienta de comunicación basada en la ubicación, ideal para la coordinación local, la creación de comunidades y los debates sobre ubicaciones específicas.


### Cómo funciona `#geohashes


El sistema divide el mundo en cuadrículas utilizando el [sistema Geohash](https://en.wikipedia.org/wiki/Geohash), donde cada carácter del hash representa una mayor precisión:



- Nivel 4** (por ejemplo, `u33d`): Abarca aproximadamente 25 km × 25 km: ideal para debates en toda la ciudad
- Nivel 6** (por ejemplo, `u33d8z`): Cubre aproximadamente 1,2 km × 1,2 km - precisión de vecindad
- Nivel 8** (por ejemplo, `u33d8z1k`): Cubre aproximadamente 150 m × 150 m - precisión de segmento de calle


La selección de precisión equilibra la privacidad con la utilidad: los niveles más altos crean zonas más exclusivas pero revelan tu ubicación con mayor precisión.


### Unirse a los canales `#geohash


1. Accede al menú `#canales de localización`.

2. Seleccione el nivel de precisión deseado e introduzca el `#geohash` (por ejemplo, #u33d)

3. Toca el botón `Teleport` para unirte al `#canal de localización`.


![image](assets/en/12.webp)


También puede pulsar el icono del mapa para utilizar la vista del mapa para determinar el nivel de precisión y pulsar Seleccionar para unirse al canal de localización.


![image](assets/en/13.webp)


**Recordatorio importante**: la funcionalidad geohash requiere una conexión activa a Internet, a diferencia de la malla BLE, que funciona sin conexión a través de Bluetooth


## 8️⃣ Mapas de calor


Los mapas de calor son una forma genial de descubrir eventos y canales de Bitchat en todo el mundo. [Bitmap](https://bitmap.lat/) visualiza y rastrea mensajes anónimos basados en la localización a través de la red Nostr, mostrando eventos efímeros de Nostr. Echa un vistazo y únete a los canales y chats específicos de tu ubicación.


![image](assets/en/15.webp)


## 🎯 Conclusión


Bitchat permite una comunicación segura y descentralizada en situaciones en las que falla la mensajería tradicional. Es capaz de funcionar sin infraestructura de Internet mediante redes de malla BLE, lo que la hace adecuada para protestas, zonas catastróficas y áreas remotas donde la conectividad es limitada o está censurada. La aplicación garantiza la privacidad mediante cifrado de clave efímera, canales de localización basados en geohash y borrado de datos en modo de pánico.


La aplicación está aún en sus primeras fases de desarrollo, pero ya promete. Los usuarios deben esperar errores ocasionales y notificar los problemas a través de [GitHub](https://github.com/permissionlesstech/bitchat-android/issues). Se prevén mejoras, como la integración de `ecash` para transacciones privadas dentro de la aplicación mediante el protocolo Cashu.


![image](assets/en/14.webp)


## 📚 Recursos de Bitchat


[Github](https://github.com/permissionlesstech) | [Sitio web ](https://bitchat.free/)| [Libro blanco](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)