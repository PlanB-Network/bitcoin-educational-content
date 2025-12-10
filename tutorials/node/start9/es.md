---
name: Start9

description: Tutorial sobre la creación de un servidor privado Start9

---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=DzikmY4S42Y)


*Aquí hay un video tutorial de Southern Bitcoiner, una guía de vídeo que muestra cómo configurar y utilizar un servidor personal Start9 / StartOS, y cómo ejecutar un nodo bitcoin.*


## 1️⃣ Introducción


### ¿Qué es exactamente Start9?


Start9 es una empresa fundada en 2020, más conocida por desarrollar [**StartOS**,](https://github.com/Start9Labs/start-os) un sistema operativo basado en Linux diseñado para servidores personales. Permite a los usuarios autoalojar fácilmente una amplia gama de servicios de software, como nodos Bitcoin y Lightning, aplicaciones de mensajería o gestores de contraseñas, manteniendo el control total sobre sus datos y eliminando la dependencia de plataformas tecnológicas centralizadas. StartOS cuenta con una interfaz fácil de usar basada en navegador, un Marketplace para instalar servicios y herramientas de privacidad integradas, como la integración con Tor y el cifrado HTTPS en todo el sistema. Start9 también proporciona dispositivos de hardware precargados con el SO, aunque el software puede instalarse en hardware compatible o en máquinas virtuales (VM).


### ¿Qué opciones hay?


Start9 ofrece opciones de despliegue preconstruidas y DIY. El [**Server One**](https://store.start9.com/collections/servers/products/server-one) y el [**Server Pure** ](https://store.start9.com/collections/servers/products/server-pure) son dispositivos de hardware oficiales que cuentan con componentes de alto rendimiento: el Server One utiliza un procesador **AMD Ryzen 7 5825U** con RAM configurable (16 GB-64 GB) y almacenamiento (SSD NVMe de 2 TB-4 TB), mientras que el Server Pure está equipado con un **Intel i7-10710U**, que también ofrece opciones configurables de RAM y almacenamiento. Ambos incluyen **soporte técnico de por vida** cuando se compran directamente a Start9. Para los usuarios que prefieran flexibilidad, StartOS puede instalarse gratuitamente en una amplia gama de hardware existente, incluidos portátiles, ordenadores de sobremesa, mini PC y ordenadores de placa única, o dentro de máquinas virtuales.


![image](assets/en/01.webp)


### ¿Qué diferencias hay con Umbrel?


StartOS y Umbrel simplifican la instalación de servicios autoalojados, pero difieren en arquitectura y características. Umbrel funciona como una capa de aplicación en sistemas Debian/Ubuntu o máquinas virtuales, mientras que Start9 es un sistema operativo dedicado que requiere la instalación directa en hardware o máquina virtual. Umbrel presenta una interfaz pulida, inspirada en macOS, mientras que Start9 prioriza un diseño funcional y minimalista. Umbrel ofrece una mayor [selección de aplicaciones](https://apps.umbrel.com/), mientras que [Start9 Marketplace](https://marketplace.start9.com/) compensa con capacidades técnicas avanzadas. Start9 simplifica el acceso a los ajustes avanzados mediante formularios de interfaz de usuario validados, reduciendo la necesidad de interactuar con la línea de comandos. También destaca en la gestión de copias de seguridad con copias de seguridad del sistema cifradas con un solo clic, una característica de la que Umbrel carece de forma nativa. StartOS proporciona herramientas de supervisión integradas e impone el cifrado HTTPS para el acceso a la red local, lo que mejora la seguridad. Umbrel utiliza HTTP sin cifrar localmente, aunque ambas plataformas soportan el acceso remoto seguro a través de Tor. Umbrel es adecuado para los usuarios que dan prioridad a un rico ecosistema de aplicaciones y una interfaz de usuario pulida. Start9 es una buena opción para quienes valoran la seguridad, la capacidad de configuración, la fiabilidad de las copias de seguridad y la gestión avanzada de servicios sin necesidad de conocimientos de línea de comandos. Para saber más sobre Umbrel y las diferencias con Start9, visita este curso:


https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

## 2️⃣ Requisitos previos para el bricolaje: Especificaciones mínimas y recomendadas


Para un uso básico con servicios mínimos, las **especificaciones mínimas** son: **1 vCPU core (2.0GHz+ boost), 4GB RAM, 64GB de almacenamiento**, y un puerto Ethernet. Dicho esto, yo recomendaría ir mucho más allá de eso, especialmente si está ejecutando un nodo Bitcoin. Personalmente, empecé con 1 TB y me quedé rápidamente sin espacio. Mejor apunta a **al menos 2 TB de almacenamiento**, junto con una ** CPU de núcleo cuádruple (2,5 GHz+)** y **8 GB+ de RAM**. Supone una gran diferencia en rendimiento y longevidad. Si quieres profundizar, aquí tienes un hilo actualizado de la comunidad sobre [Hardware capaz de ejecutar StartOS](https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/229).


## 3️⃣ Descarga y Flasheo del Firmware


Para comenzar la configuración, utilice otro ordenador para visitar el [sitio web de Start9](https://start9.com/), y navegue hasta la sección de documentación haciendo clic en `DOCS`. Desde allí, acceda a las `Guías de Flasheo` para encontrar la versión apropiada de StartOS. Hay dos opciones disponibles:



- StartOS (Raspberry Pi)
- StartOS (X86/ARM)


Este tutorial cubre la opción `x86/ARM`.


La última versión del sistema operativo puede descargarse de la [página de versiones de Github](https://github.com/Start9Labs/start-os/releases/latest). también hay versiones [Pre-release](https://github.com/Start9Labs/start-os/releases) disponibles para los usuarios que deseen probar nuevas funciones. En la parte inferior de la página, en `Assets`, descarga `x86_64` o `x86_64-nonfree.iso`.  La imagen `x86_64-nonfree.iso` contiene software no libre (de código cerrado) necesario para el Server One y la mayoría del hardware DIY, particularmente para gráficos y soporte de dispositivos de red.


Se recomienda verificar la integridad del archivo comparando su hash SHA256 con el que aparece en GitHub. Para Linux, puede utilizarse el comando `sha256sum startos-0.3.4.2-efc56c0-20230525_x86_64.iso`, mientras que otros sistemas operativos se tratan en la documentación.


Después de descargar y verificar la imagen de StartOS, hay que flashearla en una unidad USB. el software recomendado para esta tarea es `BalenaEtcher`. Se trata de una herramienta gratuita y de código abierto para grabar archivos de imagen del sistema operativo en unidades USB y tarjetas SD, disponible para Windows, macOS y Linux. Descarga la versión adecuada de la página oficial [Balena Etcher website](https://www.balena.io/etcher/) y ejecuta el instalador. Conecta la unidad USB o tarjeta SD de destino, abre Balena Etcher y haz clic en `Flash from file` para seleccionar la imagen del sistema operativo descargada. Etcher detectará automáticamente las unidades conectadas; seleccione la unidad correcta si hay varias. Haga clic en "Flash" para comenzar a escribir la imagen. Etcher valida automáticamente el proceso de escritura al finalizar. Una vez finalizado, extraiga la unidad de forma segura y utilícela para arrancar el dispositivo.


![image](assets/en/19.webp)


## 4️⃣ Configuración inicial


Para la configuración inicial, consulte la página Start9 [documentation](https://docs.start9.com/0.3.5.x/) en `USER MANUAL` seguido de `Getting Started - Initial Setup`.  Esta guía oficial debe consultarse para obtener la información más actualizada.


Se presentan dos opciones:



- Empezar de cero
- Opciones de recuperación


Para una nueva instalación del servidor, seleccione "Empezar de cero". En primer lugar, conecte el servidor a la corriente y a un cable Ethernet. Asegúrese de que el ordenador utilizado para la instalación está en la misma red local. Extraiga la unidad USB recién flasheada del ordenador e insértela en el servidor.


Puede controlar el servidor a distancia desde cualquier ordenador de la misma red. Abra un navegador web y navegue hasta `http://start.local`.


**Nota**: Si se producen problemas de conexión con esta dirección, suele deberse a que las redes domésticas no resuelven los nombres de dominio `.local`. El problema puede resolverse accediendo al servidor directamente a través de su dirección IP. La IP puede encontrarse accediendo a la interfaz de administración del router (normalmente en `192.168.1.1` o una dirección similar), y localizando el dispositivo en la lista de clientes DHCP o mapa de red. A continuación, introduzca la dirección IP completa (por ejemplo, `http://192.168.1.105`) en el navegador. Esto evita la resolución DNS. Si el problema persiste, consulta la [página de problemas comunes](https://docs.start9.com/0.3.5.x/support/common-issues.html#setup-troubleshoot) o [ponte en contacto con su servicio de asistencia técnica](https://start9.com/contact/)


Aparecerá la pantalla de configuración de StartOS. Haga clic en `Start Fresh` para iniciar la configuración del nuevo servidor.


![image](assets/en/03.webp)


El siguiente paso es seleccionar la unidad de almacenamiento donde se guardarán los datos de StartOS.


![image](assets/en/04.webp)


Establezca una `Contraseña` segura para el servidor. Regístrela como le aconseja Start9 y haga clic en `FINISH`.


![image](assets/en/05.webp)


Una pantalla mostrará que StartOS se está inicializando y configurando el servidor. El siguiente paso es `Download address info` ya que la dirección `start.local` es sólo para propósitos de configuración y no funcionará después.


![image](assets/en/06.webp)


El archivo de configuración contiene dos direcciones de acceso críticas: una para la `red local (LAN)` y otra para el acceso seguro a través de `Tor`. Ambas direcciones deben guardarse en un gestor de contraseñas seguro. El siguiente paso es `Confiar en su CA Raíz`. Abra una nueva pestaña del navegador y siga las instrucciones para confiar en la CA Raíz e iniciar sesión. También puede descargar el certificado de la CA raíz haciendo clic en "Descargar certificado" en el archivo descargado.


## 5️⃣ Confíe en su CA raíz


Después de descargar el certificado, el sistema operativo debe confiar en la CA raíz del servidor. Haga clic en "Ver instrucciones" y encontrará las directrices para el sistema operativo específico.


![image](assets/en/07.webp)


Para un sistema Linux, se utilizan los siguientes comandos. En primer lugar, abra un Terminal e instale los paquetes necesarios:


```shell
sudo apt update

sudo apt install -y ca-certificates p11-kit
```


Navegue hasta el directorio donde se descargó el certificado, normalmente `~/Downloads` . Ejecute estos comandos para añadir el certificado al almacén de confianza del sistema operativo. Cambie a la carpeta de descargas con `cd ~/Downloads`. Cree el directorio necesario con `sudo mkdir -p /usr/share/ca-certificates/start9`. Copie el archivo del certificado, sustituyendo `su-nombre.crt` por el nombre real del archivo, utilizando `sudo cp "su-nombre.crt" /usr/share/ca-certificates/start9/`. Registre el certificado de forma permanente añadiendo su ruta a la configuración del sistema con `sudo bash -c "echo 'start9/su-nombre-de-archivo.crt' >> /etc/ca-certificates.conf"`. Por último, reconstruya el almacén de confianza con `sudo update-ca-certificates`. Es crucial utilizar el nombre de archivo real del certificado y verificar todas las rutas antes de ejecutar estos comandos. Este proceso establece una confianza permanente para las conexiones HTTPS del servidor Start9.


Si la instalación se realiza correctamente, aparecerá el mensaje "1 added" (1 añadido). La mayoría de las aplicaciones podrán conectarse de forma segura a través de `https`. Si utiliza Firefox, se requiere un [paso final] adicional (https://docs.start9.com/0.3.5.x/misc-guides/ca-ff.html#ca-ff). Para Chrome o Brave, se necesita otro [paso final](https://docs.start9.com/0.3.5.x/misc-guides/ca-chrome.html#ca-chrome) para configurar el navegador para que respete la CA raíz. Pruebe la conexión actualizando la página. Si el problema persiste, cierre y vuelva a abrir el navegador antes de volver a visitar la página.


![image](assets/en/08.webp)


## 6️⃣ Primeros pasos con StartOS


Ahora debería ser posible iniciar sesión utilizando una conexión HTTPS segura. Introduzca la `Contraseña` para acceder a la `Pantalla de Bienvenida`.


![image](assets/en/09.webp)


Esta pantalla proporciona accesos directos útiles para empezar. La barra lateral izquierda contiene los principales elementos del menú de navegación.


## 7️⃣ Sistema


La pestaña Sistemas de StartOS proporciona acceso a las funciones básicas del sistema para gestionar el servidor personal. Ofrece herramientas para el mantenimiento, la seguridad, el diagnóstico y la configuración del sistema sin necesidad de conocimientos de línea de comandos.


La sección `Copias de seguridad` permite crear copias de seguridad completas del sistema, incluidos servicios, configuraciones y datos, que pueden restaurarse posteriormente. Esto es esencial para la recuperación de desastres o la migración a un nuevo hardware. Las copias de seguridad pueden almacenarse en unidades externas y se cifran mediante la contraseña maestra.


La sección "Gestionar" de la pestaña Sistemas permite controlar las principales funciones del sistema. Los usuarios pueden buscar y aplicar manualmente actualizaciones de StartOS, manteniendo el control sobre el proceso de actualización del sistema. Es posible cargar servicios personalizados o de terceros no disponibles en el mercado oficial. Si el servidor no está conectado a través de Ethernet, los ajustes Wi-Fi se pueden configurar desde esta sección. Los usuarios avanzados pueden habilitar el acceso SSH para la gestión del sistema a nivel de terminal.


![image](assets/en/10.webp)


La sección `Insights` proporciona monitorización en tiempo real del rendimiento y la salud del servidor, mostrando el uso de CPU, RAM y disco a través de gráficos. También muestra la temperatura del sistema, que es útil para dispositivos como la Raspberry Pi que carecen de refrigeración activa. Las métricas de tiempo de actividad y carga media ayudan a evaluar la estabilidad del sistema, y los registros en tiempo real están disponibles para solucionar problemas de servicio o del sistema.


La sección `Soporte` ofrece acceso a las preguntas frecuentes integradas, a la documentación oficial y a los canales de soporte de la comunidad. Los registros de depuración pueden descargarse desde esta sección para compartirlos con el servicio de asistencia de Start9 y agilizar la resolución de problemas.


![image](assets/en/11.webp)


## 8️⃣ Mercado


El `Marketplace` se utiliza para descubrir, instalar y gestionar servicios en el servidor personal. Proporciona acceso a software como Bitcoin Core, BTCPay Server, y electrs. StartOS soporta múltiples marketplaces, incluyendo el Registro oficial de Start9 y los registros gestionados por la comunidad. Estos pueden ser añadidos haciendo clic en `CHANGE` y cambiando al `Community Registry`, que proporciona acceso a una gama más amplia de servicios.


![image](assets/en/12.webp)


## 9️⃣ Instalación de un nodo completo Bitcoin


La instalación de un full node de Bitcoin en StartOS proporciona plena soberanía sobre la experiencia de Bitcoin. Permite la validación de transacciones y mejora la privacidad y la seguridad al eliminar la dependencia de servicios externos que pueden registrar la actividad. Se obtiene un control total sobre las transacciones, lo que permite emitirlas directamente a la red. La opción por defecto es `Bitcoin Core`, que se integra de forma nativa con StartOS y permite la conexión con monederos como Specter, Sparrow o Electrum para una configuración de autocustodia. Una alternativa, `Bitcoin Knots`, también está disponible a través del Registro de la Comunidad.


Para instalar Bitcoin Core, vaya a Marketplace. En el registro por defecto, busque e instale el servicio Bitcoin Core. Tras la instalación, aparecerá el mensaje "Necesita configuración", que requiere que se complete la configuración antes de que el servicio pueda ejecutarse. Esto suele ocurrir después de actualizaciones o nuevas instalaciones y requiere una revisión de la "configuración de RPC". Continúe con la configuración predeterminada y haga clic en "Guardar".


![image](assets/en/13.webp)


Una vez totalmente sincronizado, tu nodo puede servir como backend privado para monederos como Sparrow, proporcionando una mayor privacidad y validación de las transacciones. Sin embargo, para los usuarios que almacenan cantidades significativas, es fundamental comprender las ventajas y desventajas de esta conexión directa para la seguridad. Cuando una wallet se conecta directamente a Bitcoin Core, puede exponer datos confidenciales, ya que Bitcoin Core almacena claves públicas (xpubs) y saldos de wallet sin cifrar en la máquina anfitriona. Un sistema comprometido podría permitir que un atacante descubriera sus participaciones y se dirigiera a usted.


Para mitigar este riesgo y conseguir un modelo de seguridad más robusto, puedes configurar un Electrum Server privado. Este servidor actúa como intermediario, indexando la blockchain sin almacenar ninguna información específica de wallet. Al conectar tu wallet a tu propio servidor Electrum en lugar de directamente al Bitcoin Core, evitas que el wallet acceda a los datos sensibles del nodo.


![image](assets/en/14.webp)


## 🔟 Configurar electrs


electrs` (Electrum Rust Server) es un indexador rápido y eficiente que se conecta a su nodo Bitcoin Core y permite a los monederos compatibles con Electrum consultar el historial de transacciones y los saldos en tiempo real. Al ejecutar electrs en StartOS, se elimina la dependencia de servidores Electrum de terceros, lo que mejora significativamente la privacidad y la seguridad: sus consultas wallet van directamente a su nodo autoalojado.


Para configurarlo, primero instale el servicio electrs desde StartOS Marketplace. El sistema requerirá que Bitcoin Core esté completamente sincronizado antes de proceder. Después de la instalación, confirma la configuración `Needs Config` con los valores predeterminados recomendados y electrs comienza a indexar la blockchain, lo que puede tardar hasta un día dependiendo de tu hardware.


![image](assets/en/15.webp)


Una vez completado, puedes conectar monederos como Sparrow o Specter. Una conexión exitosa permite que tu wallet se sincronice directamente con tu nodo, proporcionando una experiencia Bitcoin segura, privada y autoalojada.


## 1️⃣1️⃣ Conectar Sparrow Wallet


Para conectar `Sparrow Wallet` a su nodo StartOS usando la implementación electrs, primero asegúrese de que Bitcoin Core está completamente sincronizado y electrs está instalado y funcionando. Abra Sparrow Wallet en su dispositivo y navegue a `Archivo` -> `Configuración` -> `Servidor`. A continuación, elija `Private Electrum Server`. En el campo URL, introduce el `Tor hostname` y el `Port` para electrs, que puedes encontrar en StartOS en `Services` -> `electrs` -> `Properties` (normalmente terminando en `.onion:50001`).


![image](assets/en/16.webp)


Luego, habilita Tor marcando `Usar Proxy`, configurando la dirección proxy a `127.0.0.1` y el puerto a `9050`. Haga clic en `Test Connection` y espere unos momentos. Una conexión exitosa mostrará un mensaje de confirmación como `Connected to electrs`. Una vez verificado, cierre la configuración y proceda a crear o restaurar su wallet. Esta configuración asegura que su wallet consulte su propio nodo a través de electrs, proporcionando total privacidad y un funcionamiento sin confianza.


![image](assets/en/17.webp)


## 🎯 Conclusión


StartOS de Start9 es una plataforma fácil de usar, centrada en la privacidad y diseñada para autoalojar servicios esenciales como nodos Bitcoin y Lightning, monederos y aplicaciones personales. Elimina la necesidad de conocimientos de línea de comandos al ofrecer una interfaz gráfica limpia, copias de seguridad automatizadas, monitorización de la salud y acceso seguro a Tor, por lo que es ideal para usuarios sin conocimientos técnicos. Su arquitectura modular permite una integración perfecta con herramientas como electrs o Sparrow, dándole un control total sobre su soberanía financiera y digital. Con un fuerte enfoque en la transparencia, el control local y la extensibilidad, StartOS permite a los usuarios reclamar la propiedad de las plataformas centralizadas y ejecutar su propia infraestructura privada y resistente.
