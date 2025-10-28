---
name: ThunderHub
description: Interfaz Web de gestión de nodo Lightning LND
---
![cover](assets/cover.webp)



## Introducción



ThunderHub es un **gestor de código abierto para nodos Lightning (LND)**, que ofrece una interfaz intuitiva accesible desde cualquier dispositivo o navegador.



**Características principales:**




- **Seguimiento**: Vista global de saldos, canales, transacciones, estadísticas de enrutamiento
- **Gestión**: Apertura/cierre de canales, pagos entrantes/salientes, balance de canales
- **Integraciones**: Compatibilidad con LNURL, intercambios a través de Boltz, copia de seguridad de Amboss
- **Interface responsive**: Compatible con dispositivos móviles, tabletas y ordenadores de sobremesa con temas oscuros o claros



ThunderHub se integra fácilmente con **Umbrel**, **Voltage**, **RaspiBlitz** y **MyNode**, simplificando la gestión diaria de tu nodo.



**ThunderHub** es especialmente adecuado para los operadores que buscan una Interfaz ergonómica para gestionar sus canales, controlar la liquidez (reequilibrio), supervisar las transacciones e integrar servicios de terceros como Amboss. La seguridad está garantizada mediante una conexión local o Tor.



Si aún no tienes un nodo Lightning, te recomendamos que sigas nuestro tutorial LND Umbrel:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Instalación



ThunderHub puede instalarse de varias formas diferentes, dependiendo de tu entorno de alojamiento de nodos Lightning. Tanto si utilizas una solución llave en mano (Umbrel, Voltage, RaspiBlitz, MyNode, Start9, etc.) como una instalación manual, ThunderHub suele estar disponible sin mayor esfuerzo. A continuación, describimos dos enfoques comunes: A través de Umbrel App Store, y a través de la instalación manual (aplicable a un servidor o a una distribución autoalojada).



### Instalación a través de Umbrel



Umbrel integra ThunderHub en su **App Store**, lo que hace que la instalación sea extremadamente sencilla. No hace falta línea de comandos ni configuración manual: todo se hace a través de a Interfaz de Umbrel. Sólo tienes que seguir estos pasos:





- **Abre el panel de Umbrel**: Conéctate a la interfaz web de tu nodo Umbrel (por ejemplo, `http://umbrel.local` en tu red local, o a través de su dirección `.onion` si estás usando Tor).
- **Accede a la App Store**: En el menú principal de Umbrel, haz clic en "App Store" (o "App"). Busca **ThunderHub** en la lista de aplicaciones disponibles.



![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)





- **Instala ThunderHub**: Haz clic en la aplicación ThunderHub y, a continuación, en el botón de instalación. Confirma si es necesario. Umbrel descargará y desplegará automáticamente ThunderHub en tu nodo.





- **Inicia la aplicación**: Una vez finalizada la instalación (unas decenas de segundos), ThunderHub aparecerá en tu página de inicio. Haz clic en el icono para abrirlo. ThunderHub se inicia en tu navegador.



![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)



**Importante:** Cuando ThunderHub se abre por primera vez, muestra automáticamente la **contraseña predeterminada** necesaria para iniciar sesión. La opción "No mostrar esto de nuevo" te permite ocultar esta pantalla para futuras conexiones. **Te recomendamos que:**




- **Guardes esta contraseña inmediatamente** en tu gestor de contraseñas
- **Cópialo** para utilizarlo en el siguiente paso
- Marca "No volver a mostrar esto" una vez guardada la contraseña



![Page de connexion de ThunderHub](assets/fr/03.webp)



A continuación, accederás a la página de inicio de sesión, donde deberás introducir la contraseña que copiaste en el paso anterior para desbloquear la interfaz.



![Interface de connexion complète à ThunderHub](assets/fr/04.webp)



Umbrel se encarga de proporcionar a ThunderHub la información de conexión LND (certificado TLS, macarrón de administración, etc.) en segundo plano, por lo que no necesitas realizar ninguna configuración adicional. En unos pocos clics, tendrás ThunderHub funcionando en tu nodo Umbrel.



### Instalación manual (autoalojado, excluido Umbrel)



Para usuarios externos a Umbrel (por ejemplo, en un servidor personal, una Raspberry Pi con RaspiBlitz o una instalación *stand-alone*), la instalación de ThunderHub requiere algunos pasos adicionales. A continuación describimos la instalación desde el código fuente y la configuración, según la [documentación oficial de ThunderHub](https://docs.thunderhub.io).



#### Instalación



**Requisitos previos:** Asegúrate de que tu sistema cumple los requisitos mínimos según [documentation setup](https://docs.thunderhub.io/setup):




- **Node.js** versión 18 o superior
- **npm** instalado
- **Acceso a los archivos de autenticación de LND**:
  - LND Certificado TLS (`tls.cert`)
  - Macarrones de administración LND (`admin.macarrones`)
  - LND gRPC servicio Address (hostname:port) (por defecto `127.0.0.1:10009` localmente)



**1. Recuperar código ThunderHub:** Clonar el repositorio GitHub del proyecto tal y como se describe en la [documentación de instalación](https://docs.thunderhub.io/installation):



```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```



**2. instalar dependencias y compilar la aplicación:**



```bash
npm install
npm run build
```



Estos comandos instalan todos los módulos necesarios y luego compilan la aplicación (ThunderHub está escrito en TypeScript/React).



**3. Actualizar más tarde:** ThunderHub ofrece varios métodos para futuras actualizaciones:



```bash
# Méthode rapide
npm run update

# Ou méthode manuelle
git pull
npm install
npm run build
```



#### Configuración (Setup)



**1. Archivo de configuración principal:** Crea un archivo `.env.local` en la raíz de la carpeta ThunderHub para personalizar la configuración (esto evitará que sus ajustes se sobrescriban durante las actualizaciones). Variables principales según [documentación de configuración](https://docs.thunderhub.io/setup):



```bash
# -----------
# Server Configs
# -----------
LOG_LEVEL='info' # 'error' | 'warn' | 'info' | 'http' | 'verbose' | 'debug' | 'silly'
PORT=3000
NODE_ENV=production

# -----------
# Interface Configs
# -----------
THEME='dark' # 'dark' | 'light' | 'night'
CURRENCY='sat' # 'sat' | 'btc' | 'fiat'

# -----------
# Privacy Configs
# -----------
FETCH_PRICES=true # Récupération des prix BTC/fiat depuis Blockchain.com
FETCH_FEES=true # Récupération des frais on-chain depuis Earn.com
DISABLE_LINKS=false # Liens vers 1ml.com et Blockchain.com
NO_VERSION_CHECK=false # Vérification de version depuis GitHub

# -----------
# TOR (optionnel)
# -----------
TOR_PROXY_SERVER='socks://127.0.0.1:9050' # Pour proxifier via TOR

# -----------
# Account Configs
# -----------
ACCOUNT_CONFIG_PATH='/chemin/vers/thubConfig.yaml' # Fichier de comptes
```



**2. Configuración de cuentas de servidor:** Crea el archivo YAML especificado en `ACCOUNT_CONFIG_PATH` :



```yaml
masterPassword: 'votre_mot_de_passe_principal'
accounts:
- name: 'Mon Nœud LND'
serverUrl: '127.0.0.1:10009'
macaroonPath: '/home/user/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'
certificatePath: '/home/user/.lnd/tls.cert'
password: 'mot_de_passe_compte_specifique'
# Optionnel : compte avec macaroon en hexadécimal
- name: 'Nœud Distant'
serverUrl: 'ip.distante:10009'
macaroon: '0201056c6e6402f8...' # Macaroon en HEX ou Base64
certificate: '0202045c7365...' # Certificat en HEX ou Base64
```



**3. Acceso remoto:** Para conectarse a un nodo LND remoto, añade a `LND.conf` :



```bash
# Option 1 : accès par IP
tlsextraip=<ip-externe-accessible>
rpclisten=0.0.0.0:10009

# Option 2 : accès par domaine
tlsextradomain=<domaine-externe-accessible>
rpclisten=0.0.0.0:10009
```



**4. Seguridad:** En el primer inicio, ThunderHub **automáticamente** oculta la `masterPassword` y todas las contraseñas de las cuentas en el archivo YAML, para evitar tener contraseñas en texto claro en el servidor.



**5. Iniciar ThunderHub:**



```bash
npm start
```



Por defecto, el servidor escucha en el puerto 3000. Accede a `http://localhost:3000` (o `http://ip-serveur:3000` desde la red local).



**6. Alternativa Docker:** ThunderHub proporciona imágenes Docker oficiales:



```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Image avec base path /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```



Aparecerá la página de inicio de sesión de ThunderHub. Selecciona la cuenta configurada e introduce la contraseña para acceder al panel de control.



**Instalación en otras distribuciones:** Las distribuciones de nodos pre-empaquetadas (RaspiBlitz, MyNode, Start9, etc.) generalmente ofrecen soporte nativo para ThunderHub a través de sus respectivas interfaces de administración.



**Para más información:** Consulta la documentación oficial completa:




- **Instalación:** [docs.thunderhub.io/installation](https://docs.thunderhub.io/installation)
- **Configuración:** [docs.thunderhub.io/setup](https://docs.thunderhub.io/setup)



Estos recursos detallan opciones avanzadas como cuentas SSO, macarrones encriptados, configuración de TOR y mucho más.



Una vez que ThunderHub esté instalado y accesible, estará listo para explotar todas sus funciones. En la siguiente sección, echaremos un vistazo a la interfaz de ThunderHub y a sus distintas pestañas, para guiarte en su uso.



## Presentación de la Interfaz



La Interfaz de ThunderHub está estructurada en torno a un menú principal (que suele aparecer en la columna lateral izquierda) compuesto por varias secciones clave. Cada una de ellas corresponde a un aspecto de la gestión de tu nodo Lightning. Vamos a repasarlas una a una:





- **Inicio** - Pestaña de inicio con panel general (visión general del nodo y acciones rápidas).
- **Cuadro de mandos** - Cuadro de mandos personalizable con widgets y métricas avanzadas.
- **Peers** - Gestión de peers de Lightning (conexiones con otros nodos).
- **Canales** - Gestión detallada de los canales Lightning.
- **Reequilibrio** - Herramienta de equilibrado de canales (pagos circulares).
- **Transacciones** - Historial de pagos Lightning (transacciones LN).
- **Forwards** - Estadísticas de enrutamiento (pagos retransmitidos por su nodo).
- **Cadena** - Billetera On-Chain de Node (On-Chain BTC: UTXOs, transacciones).
- **Amboss** - Integración con Amboss (supervisión de nodos, copias de seguridad, etc.).
- **Herramientas** - Herramientas varias (copias de seguridad, mensajes firmados, macarrones, informes, etc.).
- **Intercambio** - Funciones de intercambio On-Chain/Lightning a través de Boltz.
- **Estadísticas** - Estadísticas avanzadas y métricas de rendimiento de los nodos.



*(Nota: Dependiendo de la versión de ThunderHub, algunas secciones pueden tener títulos ligeramente diferentes o características adicionales, pero los principios generales siguen siendo los mismos)*



### Inicio (Panel de control general)



La pestaña **Inicio** de ThunderHub es la página de inicio que aparece después de iniciar sesión. Contiene el **Panel general**, que ofrece una **visión general** del estado de tu nodo Lightning y sugiere **acciones rápidas** para operaciones rutinarias. Esto es lo que encontrarás normalmente:



![Tableau de bord principal de ThunderHub](assets/fr/05.webp)





- **Saldos y capacidades:** En la parte superior de la página, ThunderHub muestra tus saldos disponibles. Aquí verás normalmente el saldo de On-Chain (Bitcoin On-Chain en la billetera del nodo, simbolizado por un ancla ⚓) y el saldo de Lightning (las capacidades de tus canales, simbolizadas por un Bolt ⚡ Lightning). Esto te da una idea inmediata de los fondos que tienes en On-Chain y Lightning. Si tienes varias cuentas o canales, asegúrate de que estás en el correcto (por ejemplo, Mainnet frente a Testnet).





- **Estadísticas clave:** El panel de control puede mostrar algunas métricas globales para tu nodo - por ejemplo, número de canales abiertos, número de pares conectados, tarifas de enrutamiento ganadas (si procede), etc. Es un resumen de la actividad reciente y la salud del nodo.





- **Acciones rápidas:** El panel cuenta con botones para ejecutar rápidamente las tareas más comunes, sin tener que navegar por los menús. Estas acciones rápidas incluyen:





  - **Ghost**: Configura una dirección Lightning personalizada a través de Amboss.
  - **Donar**: Haz una donación a través de Lightning.
  - **Conectarse/Ir a**: Conéctate a tu cuenta de Amboss (Quick Connect) y ve directamente a amboss.space para ver la información de tu nodo.
  - **Address**: Introduce una dirección Lightning para realizar un pago.
  - **Abrir**: Abre un nuevo canal Lightning. Al hacer clic se abre un formulario para introducir el URI del nodo remoto al que abrir el canal, el importe y, si procede, la tarifa On-Chain máxima que se utilizará.
  - **Descodificar**: Descodifica un Invoice o LNURL de Lightning para ver los detalles antes del pago.
  - **LNURL**: Procesar LNURLs para pagos o retiros de Lightning.
  - **Inicio de sesión en LnMarkets**: Inicia sesión en LnMarkets para operar.



Estas acciones rápidas permiten realizar las operaciones más frecuentes directamente desde la página de inicio, sin tener que navegar por las distintas pestañas de la Interfaz.



En resumen, el panel de control de ThunderHub te ofrece una **mirada rápida** a tu nodo y te permite realizar las operaciones más frecuentes (enviar/recibir, abrir un canal) con un solo clic. Es el punto de partida ideal para la administración diaria.



### Cuadro de mandos



La sección **Panel de control** está separada de la pestaña Inicio y ofrece un panel de control más avanzado y personalizable. Esta sección te permite crear una vista personalizada con widgets específicos según tus necesidades como operador de nodo.





- **Widgets personalizables:** A diferencia de la página de inicio, que tiene un diseño fijo, el panel de control te permite elegir exactamente qué Elements mostrar y cómo organizarlos.



![Dashboard sans widgets activés](assets/fr/06.webp)



Si no hay widgets habilitados, verás un mensaje "¡No hay widgets habilitados!" con un botón "Configuración" para acceder a los parámetros de personalización.



![Paramètres des widgets du Dashboard](assets/fr/07.webp)



En los ajustes, puedes elegir entre una amplia gama de widgets organizados en categorías: "Lightning - Información", "Lightning - Tabla", "Lightning - Gráfico", etc. Cada widget puede activarse o desactivarse individualmente con los botones "Mostrar/Ocultar".



![Bas de la page des paramètres](assets/fr/08.webp)



En la parte inferior de la configuración, encontrarás el botón "Al panel" para volver al panel y el botón "Restablecer widgets" para restablecer la visualización predeterminada.



![Dashboard personnalisé avec widgets](assets/fr/09.webp)



Una vez configurado, el panel de control puede mostrar varios gráficos y métricas: Gráficos de pagos Lightning, número de facturas emitidas, estadísticas de reenvíos, saldos detallados, etc.





- **Métricas avanzadas:** Accede a estadísticas más detalladas sobre el rendimiento de tu nodo, con gráficos y datos en tiempo real.





- **Visión general configurable:** Adapta la pantalla para que se adapte a ti, ya seas un usuario ocasional o un operador profesional que gestiona varios canales de enrutamiento.





- **Interfaz modular:** Añade o elimina widgets según sea necesario: Gráficos de avance, métricas de liquidez, alertas de estado de los nodos, etc.



Esta sección es especialmente útil para usuarios avanzados que deseen supervisar métricas específicas u obtener una visión más técnica de su nodo Lightning. Complementa la sección Inicio ofreciendo mayor flexibilidad y control sobre cómo se muestra la información.



### Pares



La sección **Peers** enumera todos los nodos Lightning conectados actualmente al tuyo como peers. Un **peer** es una conexión directa de nodo a nodo en la Lightning Network. Tu nodo puede estar conectado a peers incluso sin un canal abierto (por ejemplo, sólo a la información de cotilleo de intercambio en la red), o por supuesto cada canal abierto implica automáticamente un peer conectado.



![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)



En la pestaña Pares, verás:





- **Columnas de información:** Muestra detalles útiles como el estado de sincronización, el tipo de conexión (clearnet o Tor), el ping, los satoshis recibidos/enviados y el volumen de datos intercambiados.
- **Añadir un peer:** ThunderHub te permite conectarte manualmente a un nuevo peer a través del botón **"Añadir "** de la esquina superior derecha. Tendrás que introducir el URI del nodo (formato `<clave_pública>@<socket>`). Una vez validado, ThunderHub envía el correspondiente comando `lncli connect`. Si el nodo está en línea y accesible, se añadirá a tu lista de pares.



### Canales



La pestaña **Canales** es el corazón de la gestión de canales de Lightning. Probablemente sea la sección que consultes con más frecuencia. Presenta **todos tus canales Lightning** con sus detalles, y te permite realizar acciones de gestión en estos canales.



![Vue d'ensemble des channels ouverts](assets/fr/11.webp)



Esto es lo que encontrarás en la página Canales:





- **Vista de la lista de canales:** Se enumera cada canal abierto (o que se abre/cierra), normalmente con el alias del nodo remoto, la capacidad total del canal y una barra de color que ilustra la distribución de la liquidez local frente a la remota. ThunderHub utiliza un código de colores (a menudo azul/verde) o un porcentaje para indicar el equilibrio del canal: por ejemplo, azul para su cuota local, verde para la cuota remota. Si un canal está perfectamente equilibrado (50/50), la barra tendrá la mitad de cada color. Esto permite identificar de un vistazo qué canales están desequilibrados (todo azul = casi todo local, todo verde = casi todo remoto).





- **Columnas de información:** Muestra columnas detalladas que incluyen Estado, Acciones disponibles, Información de pares, ID de canal, Capacidad, Actividad, Tasas y Saldo con visualización gráfica de liquidez.





- **Configuración de la pantalla:** Una rueda dentada situada en la esquina superior derecha te permite personalizar la visualización de los canales según tus preferencias.





- **Estado:** También verás indicadores de estado - por ejemplo, `Active` (el canal está abierto y operativo), `Offline` (el peer está desconectado, por lo que el canal está momentáneamente inutilizable), `Pending` (para aperturas o cierres a la espera de confirmación On-Chain).





- **Acciones en un canal:** Para cada canal, ThunderHub proporciona botones de acción (a menudo en forma de iconos):



![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)





  - **Editar tarifas:** La opción "Actualizar política de canales" de la Interfaz permite ajustar todos los parámetros de los canales: Tarifa Base, Tarifa (en ppm), Delta CLTV, HTLC Max y HTLC Min. Esto te permite ajustar tus políticas de tarifas individualmente por canal, con el objetivo de atraer (o desincentivar) el tráfico de enrutamiento. *(Nota: ThunderHub no sustituye a una herramienta de gestión automática de tarifas, pero para el ajuste manual es muy eficaz)*
  - **Cierra de Canal (*Cierre*)**: El "Cierre de canal" te permite elegir entre un **cierre cooperativo** (por defecto) o un **cierre forzado** (*Force Close*) definiendo los cargos (en Sats/vByte). **Importante:** prefiere siempre el cierre cooperativo cuando sea posible, para evitar retrasos en la liquidación On-Chain y cargos más altos. ThunderHub te indicará si el peer está en línea (cooperativo posible) o no. En caso de cierre forzado, asegúrate de confirmar ya que es irreversible y desencadenará una transacción de barrido con un bloqueo temporal (generalmente 144 bloques o ~1 día en Bitcoin Mainnet).
  - **Abrir un nuevo canal:** Para abrir un nuevo canal, haz clic en la rueda dentada situada en la parte superior derecha de la página Canales y selecciona "Abrir". A continuación, puedes iniciar un canal hacia un peer nuevo o ya existente. La ventaja de utilizar esta página es que tienes ante ti una lista de tus canales existentes, lo que puede ayudarte a decidir dónde abrir un nuevo canal.



En resumen, la sección Canales ofrece un **control preciso de cada canal**. Aquí es donde manejas la asignación de liquidez, decides qué canales mantener o cerrar, y estableces tus parámetros de enrutamiento por canal. ThunderHub ofrece una interfaz clara para estas operaciones cruciales de gestión de nodos.



### Reequilibrar



La pestaña **Reequilibrio** está dedicada al **equilibrio de canales**. Equilibrar (o *reequilibrar*) consiste en reajustar la distribución de fondos entre tus canales salientes y entrantes, realizando un **pago circular** de uno de tus canales a otro de tus canales, a través del Lightning Network. Esto te permite, sin aportar nuevos fondos, desplazar liquidez de un canal demasiado lleno a otro demasiado vacío, haciendo que tus canales sean más útiles (un canal equilibrado puede tanto enviar como recibir pagos).



![Interface de rebalance des canaux](assets/fr/13.webp)



ThunderHub facilita enormemente esta operación, que de otro modo sería tediosa en la línea de comandos. A continuación explicaremos cómo utilizar la sección Reequilibrar:





- **Vista inicial del canal:** Al entrar en Rebalance, ThunderHub muestra una lista de tus canales, con un indicador de balance para cada uno (similar al de la página Canales). Puedes ver inmediatamente qué canales están desequilibrados. ThunderHub puede ordenar los canales en orden creciente de balance, de forma que los canales más desequilibrados aparezcan al principio de la lista (0.0 significa totalmente local o remoto).





- **Selección de pares:** facilita la selección de pares salientes y entrantes para el reequilibrado.





- **Configuración de parámetros:** Puedes configurar:
  - La **tasa máxima** (en Sats y ppm) que estás dispuesto a pagar
  - El **importe a reequilibrar** con la opción "Fijo" o "Objetivo
  - **Nodos a evitar** en el enrutamiento
  - **Tiempo máximo de prueba** para encontrar la ruta





- Selecciona el canal **source****: Seleccione primero el **canal saliente (fuente)**, es decir, el canal en el que tienes demasiada liquidez local para desplazarse. En la práctica, se trata de un canal en el que su cuota local es elevada (> 50%). Imaginemos un canal A con 1.000.000 de Satss, 900.000 de los cuales son locales - un buen candidato para enviar Satss a otra parte. Al hacer clic en este canal A como "saliente", ThunderHub lo marca como fuente.





- Elije **canal objetivo****: A continuación, elije el **canal entrante (objetivo)** que necesita recibir liquidez. Normalmente, éste será un canal en el que ocurre al revés: la mayoría de los fondos están en el lado más alejado (por ejemplo, sólo 100.000 Satss locales de 1.000.000). ThunderHub, una vez seleccionado el canal de origen, ordenará los demás canales en orden inverso (saldo decreciente) para ayudar a identificar los canales más complementarios. Selecciona un canal B que tenga espacio en el lado local. ThunderHub mostrará entonces claramente qué dos canales han sido seleccionados (fuente A y destino B).





- **Establece el importe de la tasa y la tolerancia:** Un formulario te permite introducir:





  - La **cantidad** a reequilibrar (en Sats). A menudo, elegimos una cantidad igual a la que equilibraría ambos canales en \~50/50. ThunderHub puede pre-llenar la mitad del exceso de capacidad del canal de origen, por ejemplo.
  - La **tarifa máxima** que estás dispuesto a pagar por esta operación (opcional). Esta tarifa se expresa en Sats (coste total del enrutamiento circular). Si lo dejas en blanco, ThunderHub buscará una ruta independientemente del coste, lo que no suele ser aconsejable (es mejor establecer un límite, por ejemplo, 10 Sats para un reequilibrio pequeño, o una ppm máxima).





- **Encontrar ruta:** Haz clic en el botón para encontrar una ruta. ThunderHub consulta a LND para calcular una ruta desde tu canal de origen a través de la red hasta su propio canal de destino. Si encuentra una posible ruta que cumpla sus criterios de tarifa, la muestra con los detalles de los saltos y el coste de la tarifa. Por ejemplo, podría indicar que ha encontrado una ruta de 3 saltos con un total de 2 Sats en cargos.





- **Iniciar reequilibrio:** Si estás conforme con la ruta propuesta, haz clic en **Reequilibrar canal**. ThunderHub iniciará entonces el pago circular a través de LND. Si el pago se realiza correctamente, verás una notificación de éxito, y los canales A y B verán modificados sus saldos en tiempo real. ThunderHub actualizará el indicador de saldo de estos canales (idealmente serán más verdes que antes, indicando un mejor saldo).





- **Ajustes e iteraciones:** Si no se encuentra ninguna ruta en el primer intento (o si es demasiado cara), puedes ajustar los parámetros:





  - Prueba con una cantidad más pequeña (a veces un reequilibrio parcial funciona mientras que uno grande falla).
  - Aumenta la cuota máxima gradualmente, pero ten cuidado de no pagar más de lo que vale.
  - Utiliza el botón **Obtener otra ruta**, si está disponible, para probar una alternativa.
  - Prueba con otro par de canales si las cosas se ponen realmente difíciles.



ThunderHub hace que el proceso sea muy **intuitivo y visual**. En sólo 4 pasos (seleccionar canal saliente, seleccionar canal entrante, importe, validar), puede hacer lo que antes requería complejos comandos manuales. La herramienta es inestimable para mantener un nodo bien equilibrado, mejorar el rendimiento y la experiencia de enrutamiento (mayor facilidad para enviar y recibir pagos a través de todos sus canales).



Por último, ten en cuenta que un reequilibrio consume costes de enrutamiento (pagados a los nodos intermedios), por lo que es una **inversión** para que tu nodo sea más fluido. Utilízalo con prudencia, por ejemplo para dar soporte a un canal hacia un servicio que utilizas a menudo (liquidez entrante) o para equilibrar un canal de enrutamiento grande. ThunderHub te permite hacer esto **de forma sencilla y eficiente**.



### Transacciones



La sección **Transacciones** de ThunderHub corresponde al historial de transacciones **Lightning** de tu nodo, es decir, los pagos y facturas pagados o recibidos a través de los canales. Es una especie de estado de cuenta de tus operaciones en LN.



![Historique des transactions Lightning](assets/fr/14.webp)



En esta pestaña encontrarás :





- **Gráfico Cobros:** En la esquina superior derecha, un gráfico muestra la evolución de los cobros recibidos a lo largo del tiempo, lo que permite visualizar la actividad de tu nodo.





- Una lista cronológica de todas las transacciones Lightning realizadas *desde* o *hacia* tu nodo. Cada entrada puede mostrar:





  - Tipo de operación: **pago enviado** (pago saliente) o **pago recibido** (entrante, a través de un cobro pagado).
  - El importe en Sats.
  - Fecha/hora.
  - ID de pago (Hash o RHash preimage) o comentario (si has añadido una nota en el cobro).
  - Estado: **completed**, o posiblemente **in progress**/*failed* (por ejemplo, un pago pendiente de resolución, pero generalmente LND procesa esto rápidamente, por lo que hay poco "pendiente" aquí en comparación con las transacciones On-Chain).



En resumen, la sección Transacciones sirve como tu **registro de actividad de LN**. Es muy útil para comprobar que un pago se ha realizado, cuántas comisiones ha costado o rastrear el historial de tus intercambios Lightning. Junto con la sección Forwards (descrita a continuación), tendrás una visión completa del dinero que ha pasado por tu nodo.



### Forwards



La pestaña **Envíos** está dedicada a la actividad de **enrutamiento** de tu nodo, es decir, los pagos que **transitan** a través de sus canales (cuando actúa como nodo intermediario en la Lightning Network). Si operas tu nodo como nodo de enrutamiento, ésta es una sección importante para el seguimiento de tu rendimiento.



![Statistiques de routage Lightning](assets/fr/15.webp)



En Forwards, ThunderHub presenta:





- **Filtros y opciones de visualización:** En la parte superior derecha, los filtros te permiten ordenar los datos por día/semana/mes/año, y elegir entre visualización gráfica o tabular.





- **Mensaje de actividad:** Si no se ha realizado ningún enrutamiento durante el periodo seleccionado, la interfaz muestra "No forwards for this period", como se muestra en este ejemplo.





- Una **tabla de envíos recientes**: cada entrada corresponde a un pago que ha sido **enviado** a través de tu nodo. Para cada reenvío, generalmente vemos:





  - Timestamp,
  - La cantidad encaminada (en Sats),
  - La **comisión ganada** en este reenvío (en Sats, es la diferencia entre lo recibido en el canal de entrada y lo enviado en el de salida),
  - Los canales entrantes y salientes utilizados (a menudo identificados por el alias del par o el ID del canal).
  - Estado (normalmente *completado*, o fallo si un reenvío falló en ruta).





- **Estadísticas agregadas**: ThunderHub calcula y muestra en la parte superior de la página totales y estadísticas durante un periodo determinado (por ejemplo, las últimas 24 horas, o 7 días, etc., a veces configurable).



En resumen, la sección Reenvíos ofrece una **visión general en tiempo real de la actividad de enrutamiento** de tu nodo Lightning. Junto con las secciones Canales y Reequilibrio, forma un paquete completo para optimizar tu nodo: Canales/Requilibrio para la liquidez, Forwards para observar los resultados (flujos y beneficios).



### Cadena



La sección **Cadena** corresponde a la gestión de la billetera Bitcoin On-Chain de tu nodo LND. Esta Interfaz te permite ver y gestionar los fondos Bitcoin, que se utilizan para abrir canales o recibir fondos de canales cerrados.



![Gestion du portefeuille on-chain](assets/fr/16.webp)



En Cadena, encontrarás:





- **Saldo On-Chain :** Muestra el saldo total de BTC disponible en Wallet LND.





- **Lista de UTXOs:** Ver todas las salidas no gastadas (UTXO) con importe, confirmaciones, Address y formato para cada salida.





- **Historial de transacciones:** Tabla detallada de todas las transacciones Bitcoin con tipo (entrada/salida), fecha, importe, cargos, confirmaciones, bloque de inclusión, direcciones y txid.



### Amboss



ThunderHub se integra con la plataforma **Amboss** (amboss.space), que ofrece información detallada sobre los nodos Lightning, un mercado de liquidez y funciones útiles como la copia de seguridad de canales cifrados y la supervisión de la disponibilidad.



![Intégration Amboss avec ses options](assets/fr/17.webp)



En ThunderHub, la sección Amboss te permite **vincular** tu nodo a tu cuenta Amboss:





- **Dirección fantasma:** Configura una **Dirección Lightning personalizada** para tu nodo, facilitando los pagos entrantes.





- **Copias de seguridad automáticas de canales:** Característica estrella para las **copias de seguridad encriptadas de canales** (archivos SCB) en Amboss. Activa **Amboss Auto Backup = Sí** en los ajustes para enviar automáticamente actualizaciones de copias de seguridad cifradas cada vez que cambies de canal. En caso de fallo, podrás recuperar tus fondos gracias a esta copia de seguridad externa.





- Health Checks:** Activa **Amboss Healthcheck = Yes** para que tu nodo envíe pings regulares a Amboss. Recibirás alertas si tu nodo parece estar fuera de línea.





- **Otras características:** Envío automático de saldo, integración con **Magma/Hydro** (mercado de liquidez) y acceso a estadísticas detalladas de rendimiento.



La integración de Amboss añade una **capa de seguridad** esencial con copia de seguridad externa automática y supervisión de disponibilidad, accesible directamente desde ThunderHub.



### Herramientas



La sección **Herramientas** agrupa varias herramientas avanzadas para gestionar tu nodo. Estos son los principales elementos:



![Interface des outils disponibles](assets/fr/18.webp)





- **Copias de seguridad:** Gestiona manualmente las copias de seguridad de tus canales (SCB). ThunderHub te permite **descargar el archivo de copia de seguridad completo** de tus canales (opción "Copia de seguridad de todos los canales -> Descargar"). Guarda este archivo `channel-all.bak` en un lugar seguro - es esencial para recuperar tus fondos en caso de caída. También puedes **importar** un archivo de copia de seguridad cuando vuelvas a desplegar un nodo.





- **Contabilidad:** Herramienta de exportación de informes financieros que incluye las comisiones devengadas/pagadas y los volúmenes enrutados durante un periodo determinado.
- **Mensajes firmados:** **Firma o verifica mensajes** con tu nodo para demostrar la propiedad de tu nodo Lightning mediante firma criptográfica.
- **Macarrones (sección "Panadería"):**Gestiona los macarrones LND** para crear accesos personalizados. La Interface "Panadería" le permite seleccionar con precisión cada permiso: "Añadir o eliminar Peers", "Crear Direcciones de Cadena", "Crear Facturas", "Crear Macarrones", "Derivar Claves", "Obtener Claves de Acceso", "Obtener Transacciones de Cadena", "Obtener Facturas", "Obtener Info Wallet", "Obtener pagos", "Obtener pares", "Pagar facturas", "Revocar identificadores de acceso", "Enviar a direcciones de cadena", "Firmar bytes", "Firmar mensajes", "Detener daemon", "Verificar firma de bytes", "Verificar mensajes", etc. Cada permiso puede activarse individualmente con los botones "Sí/No" para crear un macarrón a medida.
- **Información del sistema:** Visualización de la versión de Wallet y de los RPC activados.



En resumen, la sección Herramientas reúne las funciones avanzadas de administración -copias de seguridad, contabilidad, seguridad y gestión de accesos- en una Interfaz unificada.



### Intercambiar



La pestaña **Swap** de ThunderHub permite intercambiar satoshis Lightning a Bitcoin On-Chain a través del servicio Boltz. Esta función es útil para "volcar" el exceso de liquidez de Lightning al canal sin cerrar un canal.



![Interface de swap via Boltz](assets/fr/19.webp)



El proceso es sencillo:





- **Importe**: Define el importe a canjear
- **Address**: Introduce la dirección Bitcoin de recepción
- **Ejecución**: ThunderHub se comunica con Boltz para procesar automáticamente el intercambio



**Beneficios:**




- Servicio sin custodia (sin custodia en efectivo)
- Conserva tus canales existentes
- Interfaz integrada fácil de usar



Boltz cobra una pequeña comisión y tu pagas la tarifa de transacción estándar Bitcoin. ThunderHub muestra todos los costes antes de la confirmación.



### Estadísticas



La sección **Stats** de ThunderHub ofrece **estadísticas avanzadas** de tu nodo Lightning para analizar el rendimiento y optimizar el enrutamiento.



![Statistiques du nœud via Amboss](assets/fr/20.webp)



Esta sección es esencial para optimizar  tus costes, identificar los canales de éxito y planificar la expansión de tu nodo.



## Conclusión



**ThunderHub** se ha consolidado como la herramienta esencial para administrar fácilmente un nodo Lightning **LND**. Esta interfaz ofrece todas las funciones esenciales: gestión de canales, pagos, supervisión, con funciones avanzadas como el reequilibrio automatizado y la integración de Amboss.



**Principales ventajas**




- Interfaz elegante e intuitiva
- Herramientas potentes (reequilibrio, intercambios Boltz, copias de seguridad automáticas)
- Compatible con Umbrel, Voltage, RaspiBlitz y otras distribuciones



ThunderHub democratiza la gestión avanzada de nodos Lightning, haciendo accesible lo que antes requería complejos comandos técnicos. Tanto si eres un principiante como un operador experimentado, ThunderHub te permite gestionar eficazmente tu nodo Lightning a través de una Interfaz moderna y completa.



## Recursos



**Enlaces oficiales**




- **Página web oficial:** [thunderhub.io](https://thunderhub.io)
- **Documentación:** [docs.thunderhub.io](https://docs.thunderhub.io)
- **Código fuente GitHub:** [github.com/apotdevin/thunderhub](https://github.com/apotdevin/thunderhub)
