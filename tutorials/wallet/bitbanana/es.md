---
name: BitBanana
description: Gestor móvil para su nodo Lightning
---

![cover](assets/cover.webp)



En este tutorial, aprenderás a instalar y configurar BitBanana en Android para controlar tu nodo Lightning desde tu smartphone. Veremos cómo conectar la aplicación a tu infraestructura existente (Umbrel, RaspiBlitz, myNode o cualquier nodo Lightning LND/Core), realizar pagos Lightning, gestionar tus canales de forma remota, ver tus ingresos por enrutamiento y realizar copias de seguridad de tus configuraciones. También aprenderá sobre las mejores prácticas de seguridad para proteger el acceso a su nodo, y cómo se compara con Zeus, una alternativa popular.



## Presentación de BitBanana



BitBanana es una aplicación móvil Android de código abierto que convierte tu smartphone en un completo cuadro de mandos para el control remoto de tu nodo Lightning. A diferencia de los monederos Lightning, que incrustan un nodo local en el teléfono, BitBanana adopta una filosofía de control remoto al 100%: la app no alberga satoshi y se conecta únicamente a tu infraestructura existente.



Desarrollada por Michael Wünsch bajo licencia MIT, la aplicación garantiza total transparencia con cero recopilación de datos personales y compilaciones reproducibles verificadas. BitBanana soporta de forma nativa LND y Core Lightning a través de URIs estándar (`lndconnect://` y `clngrpc://`), simplificando drásticamente la configuración inicial. La aplicación también reconoce LndHub y Nostr Wallet Connect para usuarios sin nodo personal, aunque estos modos operan de forma custodiada con funcionalidad limitada.



La interfaz ofrece acceso completo a todas las funciones críticas de su nodo: envío y recepción de pagos (BOLT11, Lightning Address, LNURL, BOLT12, Keysend), gestión de canales Lightning (apertura, cierre, ajuste de tarifas, reequilibrio), control avanzado de monedas y gestión de torres de vigilancia. BitBanana también implementa varias capas de seguridad robustas: bloqueo biométrico, modo oculto, PIN de emergencia y soporte nativo de Tor para anonimizar las conexiones.



## Plataformas compatibles e instalación



### Instalación



BitBanana está disponible exclusivamente para Android 8.0 o superior. La aplicación no existe en iOS, y no hay ninguna versión prevista. Esta limitación se explica por la historia del proyecto: BitBanana es el sucesor directo de Zap Android, desarrollado originalmente por Michael Wünsch, que decidió continuar su trabajo bajo su propia marca. Zap era una familia de aplicaciones separadas (Zap Android, Zap iOS, Zap Desktop) desarrolladas por diferentes colaboradores con bases de código separadas. BitBanana persigue únicamente la rama de Android.



Además, el ecosistema iOS presenta importantes limitaciones normativas y técnicas para las aplicaciones Lightning no custodiadas. En 2023, Apple rechazó una actualización de Zeus por "infracciones de licencia", y en 2024, Phoenix Wallet abandonó la App Store estadounidense ante las incertidumbres normativas relativas a los proveedores de servicios Lightning. Estos obstáculos explican por qué muchos desarrolladores de Lightning prefieren Android, que ofrece una política más abierta para las aplicaciones no custodiadas.



Hay tres métodos de instalación disponibles para Android: Google Play Store (más de 5000 instalaciones, actualizaciones automáticas), F-Droid (compilaciones reproducibles, verificación del código fuente) o APK manual desde GitHub.



![BitBanana](assets/fr/01.webp)



La página oficial de bitbanana.app (izquierda) presume de ser "100% autocustodiable con CERO recopilación de datos". La pantalla central muestra las tres opciones de descarga: F-Droid (recomendada), Google Play y APK. La pantalla de la derecha muestra el permiso de notificaciones para alertas de pago.



La aplicación solicita permisos: red (conexión de nodo), cámara (códigos QR), NFC (LNURL), servicios en segundo plano (notificaciones), biometría (seguridad) y VPN WireGuard. Sin rastreadores, sin recopilación de datos. Habilita el bloqueo por contraseña o biométrico para asegurar el acceso.



## Configuración inicial



### Conexión a un nodo LND



Para conectar BitBanana a su nodo LND (Umbrel, RaspiBlitz, myNode), obtenga un URI `lndconnect` o un código QR que contenga la dirección, el certificado TLS y el macarrón de autenticación.



Para este tutorial, vamos a utilizar un nodo LND a través de umbrel. Para más detalles, consulta nuestro tutorial dedicado :



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)



En la aplicación Lightning Node, accede al menú de la parte superior derecha y selecciona "Conectar wallet".



![BitBanana](assets/fr/04.webp)



Seleccione **gRPC (Tor)** para conectarse a través de Tor (recomendado). Aparecen el código QR y los detalles (Host .onion, Puerto 10009, Macaroon).



![BitBanana](assets/fr/02.webp)



En BitBanana, pulsa "CONECTAR NODO", escanea el código QR o pega la URI. Autoriza el acceso a la cámara y comprueba la dirección .onion que aparece antes de confirmar.



**Conexión *Core Lightning



Si utiliza Core Lightning (CLN) en lugar de LND, el proceso sigue siendo idéntico, con el URI `clngrpc://` que contiene los certificados TLS mutuos. Core Lightning admite de forma nativa BOLT12 (ofertas), lo que permite facturas reutilizables y pagos periódicos no disponibles en LND.



**Conexión sin nodo personal (LNbits/hosted)**



Si no tienes un nodo Lightning, BitBanana puede conectarse a servicios alojados a través de LndHub (el protocolo utilizado por BlueWallet y LNbits) o Nostr Wallet Connect (NWC). Ten en cuenta: estos modos operan en modo custodia (el servicio aloja tus fondos) con funcionalidad limitada. No podrás gestionar canales ni configurar tarifas de enrutamiento, y sólo podrás enviar y recibir pagos Lightning.



Para más detalles sobre LNbits o Nostr Wallet Connect, consulte nuestros diversos tutoriales:



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Uso diario



### Interface principal



La pantalla de inicio muestra su saldo Lightning, con el menú de la parte superior izquierda que da acceso a las siguientes secciones: Canales, Enrutamiento, Firmar/Verificar, Nodos, Contactos, Configuración, Copia de seguridad. El icono del reloj (arriba a la derecha) abre el historial de transacciones. Los botones "Enviar" y "Recibir" de la parte inferior le permiten enviar y recibir sus satoshis.



![BitBanana](assets/fr/05.webp)



### Pagos por rayos y on-chain



![BitBanana](assets/fr/10.webp)



**Enviar un pago:** Pulsa el botón "Enviar" desde la pantalla de inicio. La pantalla de pago (izquierda) te ofrece pegar una dirección o datos de pago en el campo "Address o datos de pago", con un escáner QR en la parte superior derecha para escanear códigos. También puede seleccionar un contacto guardado en la sección Contactos para evitar tener que escanear cada vez.



BitBanana reconoce inteligentemente todos los formatos de pago: facturas Lightning clásicas (cadenas de caracteres que empiezan por `lnbc`), Lightning Address (formato de correo electrónico como `utilisateur@domaine.com`), códigos LNURL-pay para pagos dinámicos, LNURL-withdraw para retirar fondos, e incluso pagos Keysend directamente a una clave pública Lightning sin factura previa. La aplicación realiza automáticamente las resoluciones LNURL necesarias en segundo plano.



Una vez cargada la factura, BitBanana muestra todos los detalles: importe exacto, tasas de enrutamiento estimadas, descripción del pago (si la proporciona el destinatario) y fecha de caducidad de la factura. Tras la confirmación, el pago se enruta a través de tus canales Lightning. A continuación, puedes ver la ruta tomada salto a salto y los cargos realmente pagados en los detalles de la transacción.



**Recibir pago:** Pulsa el botón "Recibir". Un selector (pantalla derecha) le permite elegir entre Lightning (pago instantáneo a través de sus canales) y On-Chain. Para un recibo Lightning, introduce el importe deseado en satoshis (o déjalo en 0 para crear una factura sin importe fijo que el pagador deberá completar), y añade una descripción opcional que aparecerá en la factura. BitBanana genera instantáneamente una factura Lightning con código QR para escanear. También puedes copiar la factura como texto y enviarla por correo electrónico. En cuanto se recibe el pago, una notificación push te avisa y la transacción aparece inmediatamente en el historial con todos sus detalles.



### Canales y enrutamiento



![BitBanana](assets/fr/06.webp)



La sección "Canales" muestra sus capacidades de envío/recepción y enumera sus canales con avatares únicos. Cada canal muestra su liquidez dividida entre saldo local y remoto. Toque un canal para ver todos los detalles y acciones (cierre, cambio de tarifas de enrutamiento). Los tres puntos de la parte superior derecha dan acceso a la opción "Reequilibrar" para reequilibrar la liquidez de sus canales. El botón "+" abre un nuevo canal.



La sección Enrutamiento (pantalla central) muestra los ingresos por reenvío por periodo (1D, 1W, 1M, 3M, 6M, 1Y) con un historial detallado de los reenvíos para optimizar su estrategia.



Firmar/Verificar (pantalla derecha) permite firmar/verificar criptográficamente los mensajes para demostrar el control del nodo.



### Multinodos y parámetros



![BitBanana](assets/fr/07.webp)



**Gestionar nodos**: enumera tus nodos, con botones para añadir manualmente, escanear QR o alternar entre nodos. En particular, puedes configurar diferentes tipos de conexión al mismo nodo: LAN, VPN o Tor.



**Gestionar contactos**: almacena tus contactos Lightning para pagos rápidos.



**Configuración**: personaliza la moneda, el idioma y los avatares. Sección de seguridad y privacidad: App Lock (PIN/biometría), Ocultar saldo (modo oculto), Tor (anonimización de IP). Configuración de oráculos de precios, exploradores de bloques, estimadores de tarifas personalizados.



## Ventajas y limitaciones



**Highlights:**




- Movilidad total: controle su nodo Lightning desde cualquier lugar
- Funcionalidad completa: pagos (LNURL, Lightning Address, BOLT 12), gestión de canales, control de monedas, torres de vigilancia, multinodos
- Seguridad: PIN/biometría, modo oculto, PIN de emergencia, Tor nativo, bloqueo de capturas de pantalla
- Gratis, código abierto (MIT), cero comisiones, cero recogida de datos



**Limitaciones:**




- Requiere un nodo Rayo activo (o LNbits en modo custodia)
- No está prevista una versión para iOS
- Asegurar el acceso al teléfono es fundamental (macaroon admin = acceso total al nodo)



## Buenas prácticas



**Seguridad:**




- Activar el bloqueo PIN/biométrico (impide el acceso no autorizado al nodo)
- Establecer un PIN de emergencia (borra los datos sensibles en caso de coacción)
- Nunca compartas tu URI de inicio de sesión ni tu macarrón
- Modo oculto en entornos hostiles



**Inicio de sesión:**




- VPN en malla (Tailscale, ZeroTier): el mejor compromiso entre velocidad y seguridad
- Tor: máxima confidencialidad, mayor latencia
- Clearnet: evitar a menos que sea necesario (exposición IP, puertos abiertos)



### Copia de seguridad y restauración



Por último, está el menú "Copia de seguridad", que te permite guardar tus configuraciones para migrar el teléfono o reinstalarlo.



![BitBanana](assets/fr/08.webp)



**Importante:** La copia de seguridad NO contiene copias de seguridad de seed ni de canales (a realizar en el nodo). Contiene: configuraciones del nodo (direcciones, certificados, macarrones), etiquetas, contactos, parámetros. El botón Restaurar permite importar una copia de seguridad existente. Se requiere confirmación antes de guardar.



![BitBanana](assets/fr/09.webp)



Introduzca una contraseña de cifrado (pantalla derecha). El sistema abre el selector de archivos (pantalla izquierda) para guardar `BitBananaBackup_2025-XX-XX.dat`. Confirmación "Copia de seguridad creada".



**Seguridad:** Almacena la copia de seguridad encriptada (nube personal, USB, NAS). Nunca compartas archivos o contraseñas. Prueba la restauración con regularidad. La copia de seguridad recupera conexiones, no fondos.



## BitBanana vs Zeus: ¿Cuál es la diferencia?



Si estás explorando aplicaciones móviles para gestionar un nodo Lightning, es probable que te encuentres con Zeus, una popular alternativa a BitBanana. A diferencia de BitBanana, que se centra exclusivamente en el control remoto de un nodo existente, Zeus adopta un enfoque más completo, ofreciendo dos modos de funcionamiento: un nodo Lightning incrustado directamente en la aplicación (modo incrustado con LND integrado) y conexión remota a un nodo externo, al igual que BitBanana.



Esta doble funcionalidad hace que Zeus resulte especialmente atractivo para los principiantes que deseen experimentar con Lightning sin infraestructura previa. El modo integrado permite la puesta en marcha inmediata con un nodo móvil completo, mientras que los usuarios avanzados pueden cambiar a la conexión remota una vez configurado su nodo personal. Zeus también es compatible con LND y Core Lightning para conexión remota, como BitBanana.



Otra gran ventaja de Zeus es su disponibilidad multiplataforma (iOS y Android), mientras que BitBanana sigue estando basada exclusivamente en Android. Zeus también incorpora la infraestructura LSP de Olympus para facilitar la recepción de pagos Lightning a través de canales just-in-time, un sistema de punto de venta para comerciantes y una funcionalidad de swap integrada para gestionar la liquidez.



Sin embargo, BitBanana conserva sus puntos fuertes específicos: una interfaz más sencilla y ágil, una mejor experiencia de usuario (UX) gracias a su enfoque exclusivo en el control remoto, y un enfoque educativo con explicaciones contextuales. Zeus ofrece más funcionalidades, pero a costa de una interfaz más compleja. La aplicación sigue siendo especialmente adecuada para los usuarios que desean controlar un nodo exclusivamente a distancia, sin funciones de custodia.



Para saber más sobre Zeus, echa un vistazo a los siguientes tutoriales:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## Conclusión



BitBanana convierte tu smartphone Android en un completo panel de control Lightning, ofreciendo una movilidad sin precedentes a los operadores de nodos. La aplicación cubre todas las funcionalidades: pagos (todos los formatos), gestión de canales, control de monedas, torres de vigilancia, multi-nodos, con seguridad mejorada (PIN/biometría, Tor, PIN de emergencia).



Totalmente soberano, BitBanana no recoge ningún dato y no compromete ni la confidencialidad ni el control de sus fondos. El código fuente abierto (MIT) garantiza la transparencia.



## Recursos



### Documentación oficial




- [Sitio web de BitBanana](https://bitbanana.app)
- [Documentación completa](https://docs.bitbanana.app)
- [Código fuente GitHub](https://github.com/michaelWuensch/BitBanana)



### Instalación




- [Google Play Store](https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Cold](https://f-droid.org/packages/app.michaelwuensch.bitbanana)