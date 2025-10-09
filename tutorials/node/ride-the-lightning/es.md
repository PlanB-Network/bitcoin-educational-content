---
name: Ride The Lightning (RTL)
description: Utiliza Ride The Lightning (RTL) para gestionar tu nodo Lightning
---
![cover](assets/cover.webp)


## 1. Introducción



**Ride The Lightning (RTL)** es una aplicación web completa para gestionar un nodo Lightning Network. Esta aplicación web autoalojada ofrece una **"cabina" de Lightning** accesible desde el navegador. RTL funciona con las principales implementaciones de Lightning (LND, Core Lightning/CLN y Eclair) y te ofrece un control total sobre tu nodo y tus canales. De código abierto (licencia MIT) y gratuito, RTL está integrado por defecto en muchas soluciones de nodo llave en mano (RaspiBlitz, MyNode, Umbrel, etc.).



**Por qué utilizar RTL ?** Sin una Interface gráfica, los nodos Lightning sólo pueden gestionarse mediante comandos CLI fáciles de usar. RTL simplifica estas operaciones con una Interface ergonómica. Éstas son las **principales aplicaciones**:





- **Ve tus canales y tu nodo** - El panel de control muestra el saldo On-Chain, la liquidez de Lightning (local/remoto), el estado de sincronización, el alias del nodo y mucho más. Puedes ver tu lista de canales, capacidad, distribución local/remota y estado. RTL ofrece cuadros de mando sensibles al contexto para analizar la actividad desde distintos ángulos.





- **Gestión de canales Lightning** - Abre/cierra canales en unos pocos clics. RTL permite conectarte a un par y abrir un canal sin necesidad de un comando. Puedes ajustar las comisiones de enrutamiento, ver la puntuación del saldo o iniciar un reequilibrio circular para reequilibrar los fondos entre canales.





- **Seguimiento y realización de pagos** - RTL gestiona las transacciones Lightning: envía pagos a través de facturas, genera facturas a recibir, seguimiento de transacciones (pagos, enrutamiento) con historial detallado. Su Interfaz también analiza el enrutamiento para ver qué pagos pasan por tu nodo.





- **Gestión y copia de seguridad de Wallet On-Chain** - La pestaña On-Chain te permite generar direcciones y enviar transacciones. RTL facilita el guardado de canales exportando el archivo SCB para LND, con actualización automática para cada modificación de canal.



En resumen, RTL es un **poderoso cuadro de mandos para la Lightning Network**, que ofrece una Interfaz educativa para operar tu nodo a diario. Este tutorial te guiará a través de su instalación y uso para gestionar tus canales y pagos.



## 2. Funcionamiento técnico de RTL



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



Antes de entrar en materia, es útil comprender brevemente **cómo interactúa RTL con tu nodo Lightning** a nivel técnico.



**Arquitectura general:** RTL es una aplicación web construida con Node.js (backend) y Angular (frontend). En concreto, RTL se ejecuta como un pequeño servidor web local (en el puerto 3000 por defecto) que dialoga con tu implementación de Lightning a través de sus APIs. Dependiendo del tipo de implementación:





- Con **LND**, RTL utiliza la API REST de LND (puerto 8080) para ejecutar comandos Lightning. La conexión está protegida por TLS y requiere el archivo **admin macaroon** de LND para la autenticación.





- Con **Core Lightning (CLN)**, RTL utiliza la API REST proporcionada por *c-lightning-REST*, o una **runa de acceso** a través del plugin `commando`. Soluciones como Umbrel configuran automáticamente estos elementos.





- Con **Eclair**, RTL se conecta a la API REST de Eclair utilizando la contraseña de autenticación configurada.



**Configuración y seguridad:** RTL se configura a través de un archivo JSON (`RTL-Config.json`) donde se define el puerto web, la contraseña de acceso y la información de conexión a tu nodo. La interfaz web está protegida por un login/password (por defecto `password` a cambiar) y soporta 2FA. Por defecto, RTL se ejecuta como HTTP local (`http://localhost:3000`), pero para el acceso remoto, utiliza siempre una conexión segura (HTTPS a través de proxy inverso, Tor, o VPN).



En resumen, RTL es un componente adicional que se conecta a tu nodo a través de API seguras, requiere tokens de acceso adecuados y ofrece su propia capa de seguridad. Esta arquitectura modular permite incluso gestionar **varios nodos Lightning con una única instancia de RTL**.



## 3. Instalación RTL



Como RTL se distribuye como software de código abierto, hay varias maneras de instalarlo en su sistema. En esta sección, vamos a cubrir dos enfoques principales: la instalación manual y la instalación a través de Umbrel.



### Método manual



La instalación manual es adecuada si deseas mantener un control detallado, o si estás integrando RTL en una configuración personalizada. Los siguientes pasos son para un nodo LND con Linux (por ejemplo, Raspberry Pi o VPS con Ubuntu/Debian), pero son similares para CLN/Eclair.



**Requisito:** asegúrate de que tienes un nodo Bitcoin **sincronizado** y un nodo Lightning en funcionamiento (LND, CLN o Eclair) en la máquina. RTL no contiene un nodo Lightning per se, se conecta a un nodo existente. También necesitas tener instalado **Node.js** (se recomienda la versión 14+). Puedes comprobarlo con `node -v` o instalar Node desde el sitio oficial (https://nodejs.org/en/download/) o tu gestor de paquetes.



Las principales fases de instalación son :



**Descarga el código RTL**: Clona el repositorio oficial RTL GitHub en el directorio de tu elección. Por ejemplo:



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**Instalar dependencias**: RTL es una aplicación Node.js, por lo que necesitas instalar sus módulos requeridos. En la carpeta RTL, ejecuta :



```bash
npm install --omit=dev --legacy-peer-deps
```



Este comando instala los paquetes NPM necesarios (ignorando las dependencias de desarrollo). Se recomienda la opción `--legacy-peer-deps` para evitar posibles conflictos de dependencias de Node.



**RTL-Config**: Una vez que las dependencias están en su lugar, preparar el archivo de configuración. Copia/renombra el archivo `Sample-RTL-Config.json` en la raíz del proyecto a `RTL-Config.json`. Ábrelo en:





   - **UI password**: Elije una contraseña segura e introducela en `multiPass` (en lugar de la predeterminada `"password"`).
   - **Puerto**: Por defecto `3000`. Puedes cambiarlo si este puerto ya está ocupado en tu máquina.
   - **Nodo**: En la sección `nodos[0]`, ajusta los parámetros para tu nodo:
     - `lnNode`: un nombre descriptivo para tu nodo (por ejemplo, `"LND Node Maison"`).
     - lnImplementation`: `"LND"` (o `"CLN"`/`"ECL"` según corresponda).
     - En "autenticación":
       - macaroonPath`: Especifica la ruta completa a la carpeta que contiene el macaroon admin de LND.
       - `configPath`: Ruta al archivo de configuración del nodo (`LND.conf` para LND).
     - En `configuración`:
       - `fiatConversion`: Establecer a `true` si deseas la conversión a moneda fiduciaria.
       - `unannouncedChannels`: Establece `true` para ver los canales no anunciados.
       - themeColor` y `themeMode`: Personaliza la Interfaz.
       - channelBackupPath`: Ruta para las copias de seguridad del canal LND.
       - `lnServerUrl`: URL de tu nodo Lightning (por ejemplo, `https://127.0.0.1:8080`).



**Iniciar el servidor RTL**: En la carpeta RTL, ejecuta:



```bash
node rtl
```



La aplicación se inicia y se puede acceder a ella en `http://localhost:3000`.



**(Opcional) Ejecutar RTL como un servicio**: Para el inicio automático, crear un systemd :



Para ello:




- Abre un terminal en tu máquina.
- Crea un nuevo archivo de servicio con el siguiente comando (sustituye `nano` por tu editor favorito):


```bash
sudo nano /etc/systemd/system/RTL.service
```




- Copia y pega el contenido de abajo en este archivo:



```ini
[Unit]
Description=Ride The Lightning web UI
Wants=lnd.service
After=lnd.service

[Service]
ExecStart=/usr/bin/node /chemin/vers/RTL/rtl
User=<votre_user>
Restart=always
TimeoutSec=120
RestartSec=30

[Install]
WantedBy=multi-user.target
```





- Sustituye `ruta/al/RTL/rtl` por la ruta real al archivo `rtl` en tu máquina, y `<su_usuario>` por tu nombre de usuario de Linux.
- Guarda y cierra el archivo.
- Recarga la configuración de systemd:


```bash
sudo systemctl daemon-reload
```




- Activa e inicia el servicio RTL:


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



RTL se iniciará automáticamente cada vez que se reinicie la máquina. Puedes comprobar su estado con :


```bash
sudo systemctl status RTL
```



### Instalación a través de Umbrel



Si utilizas 

![Umbrel](https://getumbrel.com)

la instalación RTL es mucho más sencilla:





- Accede a la interfaz de Umbrel (normalmente a través de `http://umbrel.local`)
- Ve a la **App Store**
- Busca "Ride The Lightning" (en inglés)



**Nota importante: hay dos aplicaciones RTL distintas en la App Store de Umbrel:**




- **Ride The Lightning** (para LND): para usar con el nodo Lightning predeterminado de Umbrel (LND).
- **Ride The Lightning (Core Lightning)**: utilízalo sólo si has instalado la aplicación *Core Lightning* en Umbrel y deseas gestionar este nodo con RTL.



*Cada versión RTL está preconfigurada para dialogar con la implementación correspondiente (LND o Core Lightning). Si no has cambiado tu nodo Lightning, elije simplemente la versión clásica LND*



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- Haz clic en **Instalar**



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**Importante:** Después de la instalación, RTL muestra una pantalla con la contraseña por defecto. **Copia y guarda esta contraseña** - la necesitarás para iniciar sesión en RTL. Esta contraseña se mostrará cada vez que RTL se inicie hasta que marque la opción "No mostrarla de nuevo".



Umbrel se encarga automáticamente de :




- Descargar y configurar RTL
- Configuración del acceso al nodo Lightning
- Gestionar las actualizaciones
- Acceso seguro a Interface



Una vez instalada, la aplicación aparece en el menú *Aplicaciones* de Umbrel. Haz clic en **Ride The Lightning** para iniciarla.



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



En la pantalla de inicio de sesión, introduce la contraseña que copiaste anteriormente. Una vez iniciada la sesión, la interfaz web de RTL será accesible directamente desde el panel de control de Umbrel, ¡Sin necesidad de configuración adicional!



## 4. Introducción y uso de la Interfaz RTL



Ahora que RTL está en marcha, vamos a explorar su interfaz web y sus principales características. Recorreremos las distintas secciones de la aplicación para ofrecerte una visión completa.



### El panel de control principal



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



En cuanto te conectes, accederás al **panel de control principal**, que te ofrece una visión general de tu nodo Lightning. Esta página centraliza la información esencial:




- Saldo total en Lightning
- Saldo disponible On-Chain
- El desglose de tu liquidez (entrante/saliente)
- Acceso rápido para enviar y recibir Satss a través de tu nodo Lightning



### Gestión de fondos On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



La pestaña **On-Chain** te permite gestionar tu Bitcoin directamente en la cadena principal:




- Visualización del saldo en diferentes unidades (Sats, BTC, USD)
- Lista completa de transacciones
- Generación de direcciones Taproot (P2TR), P2SH (NP2WKH) o Bech32 (P2WKH)
- Gestión de UTXO, recepción y envío de Bitcoin



### Lightning: presentación detallada de los submenús



La Interfaz de RTL dispone de un menú lateral dedicado a Lightning Network, que reúne todas las funciones esenciales para la gestión de tu nodo. Aquí están los detalles de cada submenú, en orden de la captura de pantalla:



#### 1. Pares/Canales



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



Este submenú te permite:




- Consultar la lista de tus peers conectados y los canales Lightning abiertos o en espera.
- Añade un nuevo peer (conéctate a otro nodo Lightning).
- Abrir, cerrar o gestionar canales existentes.
- Ver los detalles de cada canal: capacidad, saldos locales/remotos, estado, historial de operaciones, puntuación de saldos, etc.



#### 2. Transacciones



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



En este submenú, podrás:




- Enviar pagos Lightning (a través de facturas).
- Generar y gestionar las facturas para recibir los pagos.
- Ver el historial completo de los pagos enviados y recibidos, con detalles (importe, fecha, estado, gastos, número de saltos, etc.).



#### 3. Enrutamiento



Este submenú muestra:




- Pagos enrutados por tu nodo para otros usuarios de Lightning Network.
- Estadísticas de enrutamiento: Número de transacciones retransmitidas, comisiones cobradas, errores encontrados.
- Historial exportable para análisis avanzados.



#### 4. Aplazamientos



Este submenú ofrece:




- Informes detallados sobre la actividad de tu nodo Lightning.
- Gráficos y cuadros sobre canales, pagos, tasas, capacidad, etc.
- Herramientas para comprender mejor el rendimiento de tu nodo.



#### 5. Búsqueda de gráficos



Este submenú te permite:




- Explorar la topología de la Lightning Network.
- Búsqueda de nodos o canales específicos.
- Obtener información sobre la conectividad y la capacidad global de la red.



#### 6. Firmar/Verificar



Este submenú ofrece:




- La capacidad de firmar un mensaje con la clave de tu nodo (prueba de propiedad).
- Verificación de firmas para autenticar mensajes de otros nodos.



#### 7. Copia de seguridad



Este submenú está dedicado a las copias de seguridad:




- Exportar archivo de copia de seguridad del canal (SCB para LND).
- Restaura la configuración o los canales si es necesario.
- Consejos para proteger tus copias de seguridad.



#### 8. Nodo/Red



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



En este submenú encontrarás:




- Un resumen completo del estado de tu nodo Lightning: Alias, versión, color, estado de sincronización.
- Estadísticas sobre canales (activos, en espera, cerrados), capacidad total, conectividad.
- Información sobre el Lightning Network global y la posición de tu nodo en él.



### Servicios: Boltz Swaps



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltz es un servicio de intercambio no custodiado que convierte Bitcoin entre Lightning Network y Blockchain Bitcoin (On-Chain). Ofrece dos tipos de operación: Reverse Submarine Swap (**Swap Out**) y Submarine Swap (**Swap In**).



#### Swap Out (intercambio submarino inverso)



Swap Out convierte los Satss disponibles en Lightning Network en Bitcoin On-Chain. Este mecanismo es útil cuando un nodo se queda sin capacidad de entrada, o cuando se desea recuperar fondos de una dirección On-Chain. El proceso funciona de la siguiente manera:




- El usuario selecciona el importe que desea canjear
- El nodo envía un pago Lightning a Boltz
- En intercambio, Boltz bloquea una cantidad equivalente en bitcoins On-Chain
- Una vez confirmada la transacción, el usuario puede reclamar los fondos revelando un secreto utilizado en el canje



Se trata de un proceso sin custodia, en el que Boltz nunca retiene los fondos del usuario.


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### Swap In (Intercambio de submarinos)



Swap In, por su parte, permite reinyectar fondos de On-Chain en Lightning Network. Esto resulta especialmente útil para restablecer la capacidad de salida de tus canales. El procedimiento es el siguiente:




- El usuario envía Bitcoin a una dirección específica generada por Boltz
- Boltz sólo puede liberar estos fondos si paga un cobro Lightning generado por el nodo del usuario
- Una vez pagado el cobro, los fondos están disponibles en el canal Lightning, lo que aumenta la capacidad de producción del nodo



![Configuration d'un swap-in](assets/fr/12.webp)



Estos dos mecanismos permiten gestionar eficazmente la liquidez del canal Lightning, manteniendo al mismo tiempo la soberanía del usuario sobre sus fondos.



### Configuración y personalización



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



La pestaña **Configuración de nodo** te permite personalizar tu experiencia:




- Activación de canales no anunciados
- Personalizar el expositor de venta
- Configuración Block explorer
- Ajuste de la Interfaz



### Documentación y ayuda



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



Por último, la sección **Ayuda** ofrece documentación completa sobre:




- Configuración inicial
- Gestión de pares y canales
- Pagos y transacciones
- Copias de seguridad y restauración
- Informes y estadísticas
- Firmas y verificaciones
- Parámetros del nodo y de la aplicación



Esta completa Interfaz te permite gestionar tu nodo Lightning de forma eficaz, desde las operaciones básicas hasta las funciones avanzadas, todo ello en una Interface intuitiva y bien organizada.



## 5. Casos de uso avanzados y seguridad



En esta sección, te explicamos lo que necesitas saber para ir más allá con RTL y asegurar tu nodo Lightning:



### Supervisión y resolución de problemas



Para monitorizar tu nodo, puedes exportar datos RTL (logs, CSV) y visualizarlos en herramientas como Grafana. En caso de problema (pago bloqueado, canal inactivo), consulta los logs de LND/CLN y utiliza los comandos de diagnóstico (`lncli listchannels`, `lncli pendingchannels`, etc.). RTL también ofrece registros de Interfaz para supervisar los eventos de enrutamiento.



### Acceso remoto seguro



Nunca expongas RTL directamente en Internet. Dále preferencia a:




- **VPN** (por ejemplo, Tailscale) para un acceso privado y cifrado
- **Tor** para un acceso seguro y anónimo
- **Proxy inverso HTTPS** (Nginx/Caddy) sólo si sabes configurarlo



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Buenas prácticas de seguridad





- **Protege tu acceso**: Nunca compartas admin.macaroon ni tu contraseña RTL. Limita los permisos de los archivos sensibles.
- **Copias de seguridad periódicas**: Exportar el archivo de copia de seguridad del canal (SCB) después de cada modificación y almacenarlo fuera del nodo.
- **Actualizaciones**: Mantén RTL, tu nodo y Umbrel al día con las últimas correcciones de seguridad.
- **Confidencialidad**: Anonimiza los registros y las capturas de pantalla antes de compartirlos. Nunca compartas públicamente tus balances o listas de peers.
- **Acceso único**: RTL no es multiusuario. No compartas el acceso de administrador. Para el acceso de solo lectura, utiliza un macarron dedicado si es necesario.



Aplicando estos principios, limitarás en gran medida los riesgos y mantendrás el control sobre tu nodo Lightning.



## 7. Conclusión



**Ride The Lightning** es una herramienta esencial para gestionar eficazmente un nodo Bitcoin/Lightning, tanto si eres un principiante como un usuario avanzado. Proporciona una Interfaz clara para controlar tus canales, pagos y la salud del nodo, a la vez que profundiza en tu comprensión de Lightning Network.



RTL destaca por su compatibilidad multiimplementación, sus funciones avanzadas (reequilibrado, swaps, informes) y su enfoque pedagógico. Para necesidades sencillas, bastará con la Interfaz Umbrel o una billetera movil, pero RTL tiene mucho sentido para una gestión activa y optimizada de nodos.



Más información :




- **Página web oficial de RTL:** https://www.ridethelightning.info/
- **GitHub RTL:** https://github.com/Ride-The-Lightning/RTL
- **Reddit r/lightningnetwork**: [r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - Debates técnicos, anuncios de proyectos, comentarios y recursos educativos
- **Foro de la comunidad Umbrel**: [community.getumbrel.com](https://community.getumbrel.com) - Foro oficial con sección dedicada a Bitcoin/Lightning, guías y soluciones a problemas comunes
- **Desarrolladores de Lightning Network**: [github.com/lightning](https://github.com/lightning) - Repositorio oficial de GitHub para seguir el desarrollo y contribuir con el código fuente
- **Bitcoin Stack Exchange** : [Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - Preguntas y respuestas técnicas con desarrolladores y usuarios avanzados



En resumen, RTL ofrece un control total sobre tu nodo Lightning, en una Interfaz moderna y con todas las funciones.



**Fuentes:** Sitio web oficial de RTL; RTL GitHub; Umbrel App Store; Umbrel Community; Plan B Network resources.



Para profundizar en el conocimiento del funcionamiento del Lightning Network, también te recomendamos que sigas este curso gratuito:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
