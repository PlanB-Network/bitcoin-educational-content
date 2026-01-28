---
name: Umbrel LND
description: Tutorial avanzado de instalación y configuración de Lightning Network Daemon (LND) en Umbrel
---
![cover](assets/cover.webp)




## Introducción



Este tutorial avanzado te lleva paso a paso a través de la instalación, configuración y uso de la aplicación Lightning Node (LND) en tu nodo Umbrel. Aprenderás a abrir canales, gestionar tu liquidez y sincronizar tu nodo con una aplicación móvil.



## 1. Requisito: nodo Umbrel Bitcoin funcional



Antes de desplegar Lightning, necesitas tener un nodo Bitcoin completamente operativo en Umbrel. Esto implica instalar Umbrel (en Raspberry Pi, NAS u otra máquina) y sincronizar completamente la Blockchain de Bitcoin.



Para instalar Umbrel y configurar tu nodo Bitcoin, te recomendamos que sigas nuestro tutorial dedicado:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Asegúrate de que tu nodo Bitcoin está actualizado y funciona correctamente, ya que Lightning Network depende de él para todas las transacciones de off-chain.



## 2. Introducción a Lightning Network



Lightning Network es un protocolo de segunda capa diseñado para acelerar y reducir el coste de las transacciones de Bitcoin realizándolas fuera de la Blockchain principal.



En concreto, Lightning utiliza una red de canales de pago entre nodos: dos usuarios abren un canal bloqueando Bitcoin On-Chain (transacción inicial), y luego pueden efectuar pagos instantáneos dentro de este canal. Estas transacciones off-chain no se registran en la Blockchain, de ahí su rapidez y su coste prácticamente nulo.



Los pagos pueden enrutarse a través de múltiples canales (gracias a nodos intermediarios) para llegar a cualquier destinatario de la red, lo que permite una escala casi ilimitada de transacciones instantáneas. Lightning ofrece así transacciones muy rápidas y de bajo coste, ideales para pagos cotidianos o microtransacciones, al tiempo que aligera la carga de la red Bitcoin.



Para funcionar, un nodo Lightning debe estar permanentemente conectado a la red e interactuar con otros nodos Lightning. Existen varias implementaciones de software (LND, Core Lightning, Eclair, etc.), todas ellas compatibles entre sí. Umbrel utiliza LND (Lightning Network Daemon) como parte de su aplicación oficial Lightning Node. Este tutorial se centra en LND.



Para una introducción teórica completa a Lightning Network, te recomendamos que sigas nuestro curso específico:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Este curso te proporcionará una base completa de los conceptos fundamentales de Lightning Network, antes de pasar a la práctica con tu nodo LND.



## 3. ¿Por qué autoalojar LND?



Operar tu propio nodo Lightning (LND) en Umbrel te proporciona una soberanía total sobre tus fondos y canales, en comparación con las soluciones de custodia o semicustodia.



### Comparación de soluciones Lightning:



**Soluciones custodiales (ej: Wallet de Satoshi)**:




- Tu bitcoin en Lightning es gestionado por un tercero de confianza
- Fácil de usar, sin complejidad técnica
- El operador retiene tus fondos y puede rastrear tus transacciones
- Se sacrifica el control y la confidencialidad



**Billeteras de consumo de productos no básicos (por ejemplo, Phoenix, Breez)**:




- Los usuarios conservan sus claves privadas y, por tanto, la propiedad de su Bitcoin
- No hay gestión completa de nodos: la aplicación gestiona los canales en segundo plano
- Compromiso entre simplicidad y soberanía
- Dependencia de la infraestructura de proveedores para obtener liquidez
- Limitaciones técnicas (un smartphone no puede encaminar pagos para otros)



**Nodo LND autoalojado (Umbrel)**:




- Máxima soberanía: tu BTC On-Chain y off-chain está totalmente bajo tu control
- No intervienen terceros en la apertura de canales ni en la gestión de tus pagos
- Mayor confidencialidad (tus canales y transacciones sólo son conocidos por ti y tus interlocutores directos)
- Libertad de uso: conéctate a tus propios servicios y monederos
- Posibilidad de enrutar transacciones por cuenta ajena (micro-remuneración)
- Mayores responsabilidades técnicas (mantenimiento, gestión de la liquidez, copias de seguridad)



En resumen, el autoalojamiento de LND nos ofrece el máximo control, pero requiere más conocimientos técnicos. Es un compromiso entre comodidad y soberanía.



## 4. Tutorial paso a paso



### 4.1 Instalación y configuración de la aplicación Lightning Node en Umbrel



Una vez sincronizado su nodo Umbrel (Bitcoin), sige estos pasos:



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



Instala la aplicación Lightning Node desde la sección "App Store" de Interface Umbrel.



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



LND (Lightning Network Daemon) se desplegará en tu Umbrel como una aplicación. Cuando la abras por primera vez, verás un mensaje de advertencia informándote de que Lightning es una tecnología experimental.



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



Puedes elegir entre crear un nodo nuevo o restaurar uno a partir de una copia de seguridad/seed. Para una primera instalación, elije crear un nuevo nodo. La aplicación Lightning Node generará una frase de 24 palabras Mnemonic (tu seed Lightning): escríbela con mucho cuidado (idealmente sin conexión, en papel), ya que se utilizará para restaurar tus fondos Lightning en caso necesario.



**Nota:** En versiones recientes de Umbrel, la instalación de la aplicación Lightning proporciona este seed de 24 palabras (no así el propio nodo Bitcoin de Umbrel).



![Interface principale de Lightning Node](assets/fr/04.webp)



Tras la inicialización, accederás al Interface principal de Lightning Node.



![Paramètres de l'application](assets/fr/05.webp)



En los ajustes de la aplicación, encontrarás varias opciones importantes:




   - Consulta tu Node ID (identificador único de su nodo)
   - Conexión de una billetera externa (Conectar Wallet)
   - Ver palabras secretas
   - Acceder a la configuración avanzada
   - Recuperar canales
   - Descargar archivo de copia de seguridad del canal
   - Activar copias de seguridad automáticas
   - Configurar copia de seguridad a través de Tor (Backup over Tor)



Estas opciones son esenciales para la seguridad y la gestión de tu nodo Lightning. Asegúrate de activar las copias de seguridad automáticas y de mantener a salvo tus palabras secretas.



**Recursos útiles**




- [Comunidad Umbrel](https://community.umbrel.com) - Foro de debate para que los usuarios compartan problemas y soluciones relacionados con Umbrel y su ecosistema


- [Umbrel App Store - Lightning Node (LND)](https://apps.umbrel.com/app/lightning) - Descripción de las características de la aplicación
- Lightning Node en Umbrel
- [LND Docs - Quickstart](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - Documentación oficial de LND

### 4.2 Abrir un canal Lightning



Una vez que LND esté en funcionamiento, podrás abrir tu primer canal Lightning. Para encontrar nodos de calidad a los que conectarse:



![Page d'accueil Amboss.space](assets/fr/06.webp)



[Amboss.space](https://amboss.space/) es un explorador para encontrar nodos fiables para abrir canales.



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



Por ejemplo, el [nodo ACINQ](https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f) es un nodo reconocido con excelentes estadísticas de disponibilidad y liquidez.



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



Para este tutorial, abriremos un canal con [Swiss Bitcoin Pay](https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca). La información necesaria para la conexión (pubkey@ip:port) figura en su página Amboss.



Para abrir el canal:



![Bouton d'ouverture de canal](assets/fr/09.webp)



En la página de inicio del Nodo Lightning, haz clic en el botón "+ ABRIR CANAL"



![Configuration du canal](assets/fr/10.webp)



En la página de configuración del canal:




   - Pega el ID de nodo copiado de Amboss (formato: pubkey@ip:port)
   - Define la cantidad de capacidad del canal (algunos nodos como ACINQ tienen mínimos, por ejemplo 400k Sats)
   - Ajusta las comisiones de apertura si es necesario



![Canal en cours d'ouverture](assets/fr/11.webp)



Una vez enviada la transacción, el canal aparecerá como "abierto" en la página de inicio. Espera la confirmación de la transacción On-Chain.



![Détails du canal](assets/fr/12.webp)



Haz clic en el canal para ver sus detalles:




   - Situación actual
   - Capacidad total
   - Desglose de la liquidez (entradas/salidas)
   - Clave pública del nodo remoto
   - Y otra información técnica



### Utilización de Lightning Network+ para obtener liquidez entrante



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



Lightning Network+ está disponible en la App Store de Umbrel para facilitar la obtención de efectivo entrante.



![Interface principale de LN+](assets/fr/14.webp)



La Interface principal ofrece tres opciones importantes:




- "Swaps de liquidez": explora las ofertas de swaps disponibles
- "Abrir para mí": filtra los swaps a los que puedes optar
- "To Docs": acceso a la documentación



![Message d'erreur LN+](assets/fr/15.webp)



Nota: Si aún no tienes ningún canal abierto, verás este mensaje de error cuando hagas clic en "Abrir para mí".



![Liste des swaps disponibles](assets/fr/16.webp)



La página "Swaps de liquidez" muestra todas las ofertas de swaps disponibles en la red.



![Swaps éligibles](assets/fr/17.webp)



"Abrir para mí" filtra sólo los intercambios con los que tu nodo cumple las condiciones requeridas.



![Détails d'un swap](assets/fr/18.webp)



Ejemplo de datos de intercambio:




- Configuración del Pentágono (5 participantes)
- Capacidad de 300 000 Sats por canal
- Requisito: un mínimo de 10 canales abiertos con una capacidad total de 1M Sats
- Plazas disponibles: 4/5



### 4.3 Sincronización con una aplicación móvil (Zeus)



Para controlar tu nodo Lightning a distancia (smartphone), puedes utilizar Zeus (aplicación de código abierto disponible en iOS/Android).



**Configuración de Zeus con Umbrel:**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



Asegúrate de que tu nodo Umbrel es accesible (por defecto a través de Tor).


En la Interfaz de Umbrel, abre la aplicación Lightning Node y, a continuación, haz clic en el botón "Conectar Wallet", como indica la flecha.



![Page de connexion avec QR code](assets/fr/20.webp)



Aparecerá un código QR con los datos de acceso a LND en formato lndconnect. Este código QR es especialmente denso en información, así que no dudes en ampliarlo para facilitar su lectura.



![Configuration initiale de Zeus](assets/fr/21.webp)



En tu teléfono:




   - Abre Zeus
   - En la página de inicio, haz clic en "Configuración avanzada" para conectar tu propio nodo Lightning
   - En los parámetros, seleccione "Crear o conectar una Wallet"



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



En Zeus:




   - Elije "LND (REST)" como tipo de conexión
   - Puedes escanear el código QR (método recomendado) o introducir la información manualmente. (No dudes en ampliar el código QR de Umbrel, ya que es muy denso)
   - Importante: activa la opción "Usar Tor" si tu Umbrel sólo es accesible a través de Tor (por defecto)
   - Guardar configuración



Tu billetera Zeus está ahora conectada a tu nodo Umbrel y te permite realizar pagos Lightning, ver tus canales, saldos, etc., sin dejar de ser completamente autogestionada.



**Opciones de conexión avanzadas:**



Por defecto, la conexión Zeus ↔ Umbrel es vía Tor. Para una conexión más rápida, hay dos alternativas:



**Lightning Node Connect (LNC)**:




   - Mecanismo de conexión cifrada de Lightning Labs
   - Instalar la aplicación Lightning Terminal en Umbrel (incluye acceso a LNC)
   - genera un código QR de conexión en Lightning Terminal (Conectar → Conectar Zeus a través de LNC)
   - Escanéalo en Zeus (elige "LNC" como tipo de conexión)



**VPN Tailscale**:




   - VPN en malla fácil de configurar
   - Instala Tailscale en Umbrel (App Store) y en tu móvil
   - Conecta Zeus a través de Tailscale IP privada en lugar de Tor Address



Estas opciones no son obligatorias, y la solución Tor + Zeus funciona bien en la mayoría de los casos.



> **Recursos útiles**
> - [Documentación de Zeus - Conexión a Umbrel](https://community.umbrel.com/t/zeus-LN-mobile/7619) - Guía oficial para conectar Zeus a Umbrel
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) - Proyecto de código abierto Zeus
> - [Umbrel Community - Connecting Zeus via Tailscale](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - Guía para conectar Zeus a Umbrel usando Tailscale

## 5. Seguridad y buenas prácticas



La gestión de un nodo Lightning autoalojado requiere una especial atención a la seguridad.



### Copias de seguridad para tu nodo



**Tipos esenciales de copias de seguridad**



Tu nodo Lightning Umbrel requiere dos tipos de copias de seguridad:



**La frase seed (24 palabras)**




- Recupera los fondos de On-Chain
- Necesario para recrear tu billetera Lightning
- Para un almacenamiento ultraseguro (sin conexión, en papel)



**archivo Static Channel Backup (SCB)**




- Contiene información sobre el canal de Lightning
- Permite el cierre forzado del canal en caso de colisión
- **Importante:** Nunca guardes el archivo `channel.db` manualmente (riesgo de sanciones)



**Procedimiento de copia de seguridad manual**



Para guardar tus canales manualmente:


1. Accede al menú del Nodo Lightning (tres puntos"⋮ "junto a" + Abrir canal")


2. Descarga el archivo de copia de seguridad del canal


3. Exporta un nuevo SCB después de cada modificación de canal


4. Almacena el SCB de forma segura (medios encriptados, copia externa)



**Sistema de copia de seguridad automática**



Umbrel cuenta con un sofisticado sistema de copia de seguridad automática que garantiza:



**Protección de datos**




- Cifrado del lado del cliente antes de la transmisión
- Envío a través de la red Tor
- Datos complementados con relleno aleatorio
- Clave de cifrado exclusiva de tu dispositivo



*Seguridad mejorada:*




- Copias de seguridad instantáneas en caso de cambio de estado
- Copias de seguridad "señuelo" a intervalos aleatorios
- Ocultar los cambios de tamaño de las copias de seguridad
- Protección contra el análisis temporal



*Proceso de restauración:*




- Identificador y clave derivados de tu seed Umbrel
- Restauración completa posible sólo con la frase Mnemonic
- Recuperación automática de las últimas copias de seguridad
- Restaurar la configuración y los datos del canal



### Restauración de accidentes



Si se pierde el nodo (fallo de hardware, tarjeta SD dañada):




- Reinstalar Umbrel
- Introduce tu seed de 24 palabras en la aplicación Lightning
- Importa el archivo SCB durante la restauración



LND se pondrá en contacto con cada uno de los socios de sus antiguos canales para cerrarlos y recuperar su parte de los fondos de On-Chain. Los canales se cerrarán permanentemente (para reabrirlos si es necesario).



### Disponibilidad y protección contra el fraude



Lo ideal es dejar el nodo en línea lo más a menudo posible. En caso de ausencia prolongada:




- Un peer malicioso podría intentar difundir un estado de canal antiguo
- Lightning prevé un "plazo de protesta" (unas 2 semanas en LND)
- Si vas a estar fuera mucho tiempo, prepara un Watchtower



**Configuración Watchtower:**




- En la configuración avanzada de LND, añade la URL de un servidor Watchtower de confianza
- Puedes utilizar un servicio público o instalar tu propia Watchtower




Para saber más sobre la configuración y el uso de las torres de vigilancia, te recomendamos que eches un vistazo a nuestro tutorial dedicado:



https://planb.academy/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2

### Otras buenas prácticas


- **Actualizaciones de software:** Mantener Umbrel y LND al día (correcciones de seguridad)
- **Protección del hardware:** Utiliza un sistema estable (Raspberry Pi con SSD, mini-PC) y un SAI
- **Seguridad de la red:** Mantener configuración Tor por defecto, cambiar contraseña admin Umbrel (por defecto: "moneyprintergobrrr")
- **Cifrado:** Activa el cifrado de disco si es posible



## 6. Herramientas adicionales



La aplicación Lightning Node de Umbrel proporciona lo esencial para gestionar tus canales, pero las herramientas de terceros ofrecen funcionalidades avanzadas.



### ThunderHub



Interface moderno sistema de gestión de nodos Lightning basado en web instalable a través de la tienda de aplicaciones Umbrel.



**Características:**




- Visualización en tiempo real de los canales (capacidades, saldos)
- Herramientas de reequilibrio integradas
- Soporte para facturación multitrayecto (MPP)
- Generación de código QR LNURL
- Gestión de transacciones On-Chain



ThunderHub es ideal para supervisar un nodo de enrutamiento activo y realizar un reequilibrio sencillo.



### Ride The Lightning (RTL)



Interface web compatible con varias implementaciones de Lightning (LND, Core Lightning, Eclair).



**Highlights:**




- Gestión multinodo
- Cuadros de mando sensibles al contexto
- Soporte para intercambios de submarinos (Lightning Loop)
- autenticación de 2 factores
- Exportación/importación de copias de seguridad de canales



RTL es una completa "navaja suiza" para administrar un nodo Lightning con un enfoque más orientado a los expertos.



### Otras herramientas útiles





- **Lightning Shell**: Línea de comandos (lncli) a través del navegador
- **Explorador BTC RPC y Mempool**: Supervisión Blockchain
- **LNmetrics y Torq**: Análisis del rendimiento de las rutas
- **Amboss y 1ML**: gestión "social" de tu nodo (alias, contactos, análisis de redes)



Estas herramientas pueden instalarse en unos pocos clics a través de la App Store de Umbrel, sin ninguna configuración compleja.



**Recursos de herramientas adicionales:**




- [ThunderHub.io - Características](https://thunderhub.io) - Descripción general de las características de ThunderHub
- [Ride The Lightning (RTL) info](https://www.ridethelightning.info/) - Documentación RTL
- [David Kaspar - Reequilibrio a través de ThunderHub](https://blog.davidkaspar.com) - Guía práctica del reequilibrio
- [Guía "Gestión de los nodos Rayo"](https://github.com/openoms/lightning-node-management) - Documentación avanzada para usuarios avanzados



## Conclusión



Ejecutar tu propio nodo LND en Umbrel es un paso importante hacia la soberanía financiera. Aunque requiere una mayor implicación técnica que una solución de custodia, los beneficios en términos de control, confidencialidad y participación activa en el Lightning Network son considerables.



Siguiendo esta guía, ahora deberías ser capaz de instalar LND, abrir canales, gestionar tu liquidez y acceder a tu nodo de forma remota. No dudes en explorar gradualmente las funciones avanzadas y las herramientas adicionales a medida que te familiarices con el ecosistema.



Recuerda que la seguridad de tus fondos depende de tus salvaguardas y prácticas. Tómate tu tiempo para comprender todos los aspectos antes de comprometer grandes sumas de dinero.