---
name: Servidor LNbits
description: Instalación y configuración de un servidor LNbits autoalojado en Ubuntu VPS con PHOENIXD o en Umbrel
---

![cover](assets/cover.webp)



LNbits es una aplicación web Interface de código abierto que transforma cualquier backend Lightning (LND, Core Lightning, PHOENIXD) en una completa plataforma de servicios. Esta solución autoalojada le permite gestionar varias carteras Lightning de forma aislada, desplegar puntos de venta, crear sistemas de donaciones o servicios de facturación, conservando el control total de sus fondos.



Este tutorial cubre dos enfoques de instalación: **VPS Ubuntu con PHOENIXD** (solución ligera sin un nodo Bitcoin completo) y **Umbrel** (integración con su nodo LND existente). A diferencia del tutorial general de LNbits de Plan B Network, que cubre conceptos y extensiones, esta guía se centra en los procedimientos técnicos de instalación paso a paso.



## ¿Qué es LNbits?



LNbits es un sistema de contabilidad Lightning desarrollado en Python (FastAPI) que se conecta a un backend existente (LND, Core Lightning, PHOENIXD). A diferencia de los nodos Lightning tradicionales, LNbits ofrece una Interface accesible, que te permite gestionar varias carteras aisladas con sus propias claves API. Puede crear subcuentas para su familia, empleados o proyectos, sin darles acceso a todos sus fondos.



La arquitectura desacoplada almacena la información en SQLite (por defecto) o PostgreSQL (producción), mientras que los fondos siguen siendo gestionados por su backend Lightning. Esta separación garantiza la portabilidad: puedes migrar de PHOENIXD a LND sin perder los datos de tus usuarios.



## Características principales



LNbits ofrece un versátil **sistema de extensiones**: TPoS (punto de venta), Paywall (monetización de contenidos), Eventos (venta de entradas), LndHub (servidor para BlueWallet), Bolt Cards (pagos NFC), Split Payments (distribución automática) y User Manager (gestión de usuarios con autenticación).



El **cuadro de mandos** muestra los saldos en tiempo real, el historial de transacciones y las herramientas de facturación. Cada Wallet tiene una URL única que contiene sus claves API, lo que permite el acceso sin un inicio de sesión tradicional. El sistema de claves API** de tres niveles (admin, Invoice, sólo lectura) ofrece un control granular de los permisos para integraciones seguras.



LNbits implementa de forma nativa **LNURL** (LNURL-pay, LNURL-Withdraw, LNURL-auth) y soporta **Lightning Address**, garantizando la compatibilidad con los monederos Lightning modernos y facilitando el despliegue de servicios profesionales.



## Plataformas compatibles



**Ubuntu VPS**: Solución ligera sin nodo Bitcoin completo. Requisitos previos: 1 vCPU, 1-2 GB RAM, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + nombre de dominio requerido para exposición pública (servicios LNURL).



**Umbrel**: Fácil instalación desde la App Store. Requisito previo: nodo Umbrel funcional con LND sincronizados y canales abiertos. Configuración automática.



A continuación encontrará enlaces a nuestros tutoriales sobre Umbrel y Umbrel LND:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Instalación en Ubuntu VPS con PHOENIXD



### Paso 1: Proteger el servidor VPS



**Antes de cualquier instalación**, necesitas asegurar tu servidor Ubuntu VPS según las reglas del arte. Este paso es **crítico** para proteger su infraestructura y sus fondos Lightning.



Aquí tienes una guía detallada para ayudarte a empezar: **[Configuración inicial del servidor Ubuntu - Guía paso a paso](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** por Daniel P. Costas.



Esta guía cubre la configuración de usuario, SSH seguro, cortafuegos (UFW), fail2ban, actualizaciones automáticas y buenas prácticas de seguridad del sistema.



### Paso 2: Instalación de PHOENIXD



Una vez que su servidor esté seguro, deberá instalar y configurar PHOENIXD. Plan B Network ofrece un completo tutorial dedicado que cubre la instalación, la generación de seed y la configuración del servicio systemd:



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Una vez que PHOENIXD esté funcionando (compruébalo con `./Phoenix-CLI getinfo`), anota la **contraseña HTTP** en `~/.Phoenix/Phoenix.conf` - la necesitarás para conectar LNbits a PHOENIXD.



### Despliegue de LNbits



Instalar UV y clonar LNbits :


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Configure el backend PHOENIXD:


```bash
cp .env.example .env && nano .env
```



Añadir a `.env` :


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



Pruebe con `uv run lnbits --host 0.0.0.0 --port 5000` y cree un servicio systemd con `Wants=PHOENIXD.service`.



## Configuración inicial y primer uso



### Activación de superusuario



Activar el administrador Interface en `.env` :


```
LNBITS_ADMIN_UI=true
```



Reinicie LNbits (`sudo systemctl restart lnbits`) y recupere el ID de SuperUser:


```bash
cat ~/lnbits/data/.super_user
```



Vaya a `http://<IP-VPS>:5000/Wallet?usr=<SuperUserID>` para acceder al panel de administración. El menú "Servidor" permite configurar las fuentes de financiación, las extensiones y las cuentas de usuario.



### Creación segura de cuentas



**Importante para la exposición pública**: Si estás exponiendo tu instancia de LNbits en un nombre de dominio público accesible desde Internet, es **crítico** deshabilitar la creación libre de cuentas de usuario.



Desde la administración de SuperUser Interface, ve a "Configuración" y luego a la sección "Gestión de usuarios". Encontrarás la opción "Permitir la creación de nuevos usuarios".



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**Para una exposición pública con nombre de dominio** :




- Debe desactivar** la opción "Permitir la creación de nuevos usuarios"
- Sin esta protección, cualquiera en Internet puede crear una cuenta en su instancia
- Un atacante podría crear cuentas y utilizar la liquidez de su LIGHTNING NODE sin su conocimiento
- Tendrá que crear cuentas de usuario manualmente desde el SuperUsuario Interface



**Sólo para uso local** :




- Esta opción es menos crítica si su instancia sólo es accesible localmente (http://localhost:5000)
- Sin embargo, desactivar esta opción es una buena práctica general de seguridad



Una vez configurado, sólo el administrador SuperUser puede crear nuevas cuentas de usuario a través de la Interface "Usuarios". Este enfoque garantiza un control total sobre quién puede acceder a su infraestructura Lightning y utilizar sus fondos.



### Abrir el primer canal



PHOENIXD gestiona automáticamente los canales mediante auto-liquidez. generate un Invoice relámpago de ~30.000 Sats de LNbits y lo paga desde otro Wallet. PHOENIXD abre automáticamente un canal a ACINQ. Se deduce la comisión de apertura (~20-23k Sats), el saldo restante (~7-10k Sats) aparece tras la confirmación de On-Chain.



Comprueba el estado con `./Phoenix-CLI getinfo`. A continuación, considere la posibilidad de desactivar la liquidez automática (`auto-liquidity=off` en `Phoenix.conf`) para controlar la apertura de canales.



### Visualización pública y HTTPS



**Importante**: HTTPS obligatorio para visualización pública (seguridad de clave API + compatibilidad con LNURL). Omita este paso solo para uso local.



**Caddy (recomendado)**: SSL automático. `sudo apt install -y caddy`, editar `/etc/caddy/Caddyfile` :


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


Reinicie: `sudo systemctl restart caddy`.



**Nginx** : Más control. Instalar `nginx certbot python3-certbot-nginx`, crear `/etc/nginx/sites-available/lnbits` :


```nginx
server {
listen 80;
server_name votre-domaine.com;
location / {
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
}
}
```


Activar: `sudo LN -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d sudominio.com`



Añadir a `.env`: `FORWARDED_ALLOW_IPS=*`



## Instalación de paraguas



### Implantación desde App Store



Ve a la App Store de Umbrel, busca "LNbits" y haz clic en "Instalar".



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel comprueba automáticamente las dependencias necesarias. LNbits requiere LIGHTNING NODE (LND) para funcionar. Si su LIGHTNING NODE ya está operativo, haga clic en "Instalar LNbits" para confirmar.



![Dépendances LNbits](assets/fr/02.webp)



Umbrel descarga la imagen Docker, configura automáticamente las conexiones con LND e inicia el contenedor (2-5 minutos). La instalación se realiza completamente en segundo plano.



### Configuración inicial SuperUser



En el primer inicio, LNbits le pide que cree la cuenta de administrador SuperUser. Introduzca un nombre de usuario y establezca una contraseña segura para proteger el acceso al sistema de administración de Interface.



![Configuration SuperUser](assets/fr/03.webp)



**Importante**: Esta cuenta de SuperUsuario tiene todos los privilegios en su instancia de LNbits. Elija una contraseña segura y manténgala a salvo.



Una vez que haya creado una cuenta, accederá automáticamente al área de administración principal de Interface. Umbrel ya ha configurado LND como tu fuente de financiación: todos los pagos de Lightning irán a través de tus canales existentes.



### Acceso al administrador de Interface



En el menú de la izquierda, haga clic en "Configuración" para acceder al panel de administración completo.



![Interface Settings](assets/fr/04.webp)



La sección "Gestión de carteras" muestra información clave sobre su configuración:




- Fuente de financiación** : LndBtcRestWallet (conexión directa a su nodo LND Umbrel)
- Saldo de nodo** : Liquidez total disponible en sus canales Lightning
- Saldo LNbits**: Fondos asignados al sistema LNbits (inicialmente 0 Sats)



Ahora puedes explotar directamente la liquidez de tu nodo Umbrel para todos los monederos LNbits que crees. No se requiere ninguna configuración adicional - LNbits está en marcha y funcionando.



### Gestión de usuarios



Una de las características más potentes de LNbits es su capacidad para crear múltiples usuarios independientes, cada uno con autenticación por contraseña y monederos aislados. Esta arquitectura permite aprovechar la liquidez de su nodo Umbrel al tiempo que ofrece subcuentas totalmente aisladas para diferentes usos: empresa, familia, empleados, proyectos, etc.



En el menú lateral, haga clic en "Usuarios" para acceder a la gestión de usuarios. Haz clic en "CREAR CUENTA" para añadir un nuevo usuario.



![Gestion des utilisateurs](assets/fr/05.webp)



Rellene el formulario de creación de usuarios:




- Nombre de usuario**: Nombre de usuario de inicio de sesión (ejemplo: "Satoshi")
- Establecer contraseña**: Active esta opción para establecer una contraseña de autenticación
- Contraseña** y **Contraseña repetida**: Establecer la contraseña para este usuario



![Création utilisateur satoshi](assets/fr/06.webp)



Los campos opcionales (Clave Pública Nostr, Email, Nombre, Apellidos) pueden dejarse en blanco para una configuración mínima. Haga clic en "CREAR CUENTA" para confirmar.



![Confirmation utilisateur créé](assets/fr/07.webp)



Su nuevo usuario aparece ahora en la lista de usuarios con su identificador único y su nombre de usuario.



![Liste des utilisateurs](assets/fr/08.webp)



**Punto importante**: Cada usuario puede conectarse de forma totalmente independiente con su propia contraseña. El administrador SuperUser conserva el control total a través de la herramienta de administración de Interface.



### Gestión de usuarios Wallet



Una vez creado el usuario "Satoshi", hay que asignarle un Wallet Lightning. Haga clic en el icono Wallet (segundo icono) del usuario en cuestión y, a continuación, en "CREAR NUEVO Wallet".



![Gestion des wallets](assets/fr/09.webp)



Un cuadro de diálogo le pedirá que asigne un nombre a la Wallet. Introduzca un nombre descriptivo (por ejemplo, "Wallet De Satoshi") y seleccione la moneda de visualización (CUC, USD, EUR, etc.).



![Création wallet](assets/fr/10.webp)



Haga clic en "CREAR". LNbits genera instantáneamente un Wallet Lightning funcional para este usuario.



![Confirmation wallet créé](assets/fr/11.webp)



Ahora verá las dos carteras existentes: la Wallet por defecto "LNbits Wallet" creada automáticamente, y la nueva "Wallet Of Satoshi". Para simplificar la experiencia del usuario, puede eliminar la Wallet por defecto haciendo clic en el icono de eliminar (papelera roja).



![Wallet final unique](assets/fr/12.webp)



El usuario "Satoshi" dispone ahora de una única Wallet claramente identificada. Cada usuario Wallet opera de forma completamente autónoma, mientras utiliza la liquidez de su nodo LND subyacente.



**Concepto clave**: Todos estos monederos comparten la liquidez global de tu nodo Umbrel. No creas nuevos canales Lightning para cada Wallet - LNbits actúa como un Layer contable inteligente que gestiona la asignación de fondos dentro de tu infraestructura Lightning existente. Ese es el poder del sistema multi-Wallet de LNbits.



### Inicio de sesión de usuario



Salga de la cuenta de SuperUsuario (icono superior derecho) y vuelva a la página de inicio de sesión de LNbits. Ahora puede iniciar sesión con las credenciales del nuevo usuario.



![Connexion utilisateur satoshi](assets/fr/13.webp)



Introduzca el nombre de usuario ("Satoshi") y la contraseña previamente definidos, y haga clic en "LOGIN". El usuario accede directamente a su Wallet personal, totalmente aislado de la Interface de administración.



### Interface del usuario Wallet



Una vez conectado, el usuario accede a su Interface desde Wallet Lightning.



![Interface wallet utilisateur](assets/fr/14.webp)



Características de la Interface :




- Saldo actual**: Se muestra en Sats y en la moneda elegida (CUC en este ejemplo)
- Acciones principales**: "PEGAR SOLICITUD" (pegar una factura para pagar), "CREAR Invoice" (generate un recibo), icono QR (escaneo rápido)
- Historial de transacciones** : Lista completa de todos los pagos y cobros
- Panel lateral derecho**: Opciones de configuración y acceso



### Acceso móvil Wallet



El panel lateral derecho ofrece una función especialmente práctica: el acceso móvil a Wallet. Despliegue la sección "Acceso móvil" para descubrir las opciones disponibles.



![Mobile Access](assets/fr/15.webp)



LNbits ofrece varias formas de utilizar esta Wallet en un smartphone:



**Opción 1: Aplicaciones móviles compatibles




- Descarga **Zeus** o **BlueWallet** de App Store o Google Play
- Activar la extensión **LndHub** en LNbits para este Wallet
- Escanee el código QR de LndHub con la aplicación móvil para conectar el Wallet



**Opción 2: Acceso directo a través del navegador del móvil**




- El código QR que aparece en "Exportar a teléfono con código QR" contiene la URL completa del Wallet con autenticación integrada
- Escanee este código QR desde su smartphone para abrir Wallet directamente en su navegador móvil
- Añadir una página a la pantalla de inicio para un acceso rápido



**Importante seguridad**: Esta URL contiene las claves de API para el acceso completo a Wallet. Nunca la compartas públicamente. Trata este código QR como lo harías con tus claves privadas de Bitcoin: cualquiera que escanee este código QR obtendrá acceso completo a Wallet.



Esta función móvil convierte tu instancia de LNbits Umbrel en un auténtico servidor Lightning Wallet para ti y tus amigos, al tiempo que conservas la soberanía total sobre tus fondos gracias a tu nodo autoalojado.



### Acceso compartido de usuarios



El principal caso de uso para esta configuración multiusuario es **compartir monederos con tu familia o círculo cercano**. Una vez que hayas creado un usuario con una Wallet dedicada (como "Satoshi" en nuestro ejemplo), puedes compartir estas credenciales de inicio de sesión con miembros de confianza de tu hogar.



**Seguridad de acceso en Umbrel**: El acceso a tu instancia de LNbits en Umbrel está naturalmente protegido, ya que sólo se puede acceder :




- En su red local** : Los miembros de tu hogar conectados a la misma red WiFi/Ethernet pueden acceder a la instancia
- A través de VPN**: Si utiliza una VPN como Tailscale configurada en su servidor Umbrel, los usuarios autorizados pueden obtener acceso remoto seguro



Esta doble Layer de protección (acceso a la red + autenticación del usuario) hace que la opción "Permitir la creación de nuevos usuarios" sea menos crítica en Umbrel. Solo las personas que ya tienen acceso a tu red o VPN pueden llegar al inicio de sesión Interface.



**Escenario típico**: Creas una cuenta "papá", una cuenta "mamá", una cuenta "empresa" y así sucesivamente. Cada miembro de la familia tiene su propio Wallet Lightning aislado, mientras se beneficia de la liquidez compartida de tu nodo Umbrel. Simplemente comparte el nombre de usuario y la contraseña - el usuario puede entonces conectarse desde cualquier dispositivo de tu red local o a través de tu VPN Tailscale. Consulta nuestro tutorial dedicado a Tailscale para obtener más información:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Explorar las extensiones disponibles



Vuelva a Interface SuperUser y acceda al menú "Extensiones" del panel lateral izquierdo para descubrir todo el ecosistema de extensiones de LNbits.



![Extensions disponibles](assets/fr/16.webp)



LNbits ofrece un amplio catálogo de extensiones que transforman su instancia en una auténtica plataforma de servicios Lightning:





- Jukebox**: Sistema de jukebox alimentado por Sats (pagos Spotify)
- Tickets de soporte**: Sistema de soporte de pago (recibe Satss para responder preguntas)
- TPoS**: Terminal punto de venta móvil y seguro para minoristas
- User Manager**: gestión avanzada de usuarios y Wallet (que acabamos de utilizar)
- Eventos**: Venta y validación de entradas para eventos
- Dispositivos LNUR**: Gestión de puntos de venta, cajeros automáticos, conmutadores conectados
- SMTP**: Permite a los usuarios enviar correos electrónicos y ganar Satss
- Boltcards**: Programación de tarjetas NFC para pagos Lightning tap-to-pay
- NostrNip5**: Cree direcciones NIP5 para sus dominios
- Pagos divididos**: Distribución automática de pagos entre varios monederos



Cada extensión se activa con un solo clic desde esta Interface. Las extensiones marcadas con "FREE" son gratuitas, mientras que algunas están disponibles como versiones "PAID". Explore el catálogo para identificar las que se ajustan a sus necesidades, ya sea para los negocios, la gestión familiar o para experimentar con las capacidades de Lightning Network.



## Ventajas y limitaciones



**Beneficios**: Soberanía financiera (control total sobre fondos/claves/datos), flexibilidad arquitectónica (migración VPS→Full node sin pérdidas), sistema de ampliación profesional, Interface intuitivo.



**Limitaciones** : Software en beta (precaución sobre las cantidades), seguridad bajo responsabilidad del administrador, URLs que contienen claves sensibles API (HTTPS obligatorio), la gestión multiusuario implica responsabilidad de custodia.



## Buenas prácticas



**Copias de seguridad**: seed PHOENIXD/credenciales LND, base de datos LNbits, archivos `.env`. Automatizar diariamente, mantener fuera del servidor de producción, encriptadas. Restauraciones de prueba periódicas.



**Mantenimiento**: Comprueba regularmente si hay actualizaciones (LNbits, Lightning backend, sistema operativo). Compruebe siempre las notas de la versión antes de realizar actualizaciones importantes.





- En Umbrel**: App Store le notifica automáticamente las nuevas versiones. Sincroniza las extensiones a través de "Gestionar extensiones" > "Actualizar todo". Comprueba la inclusión de la base de datos SQLite en las copias de seguridad automáticas de Umbrel.
- En VPS**: Actualice manualmente con `cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits`. Supervise los registros del sistema: `sudo journalctl -u lnbits -f`.



## Conclusión



El autoalojamiento de LNbits ofrece un camino concreto hacia la soberanía financiera de Lightning. VPS+PHOENIXD ofrece una solución ligera para servicios rápidos, Umbrel plena integración con el nodo Bitcoin existente. La arquitectura escalable permite evolucionar desde la sencilla Wallet multiusuario hasta sofisticados casos de uso empresarial.



El autoalojamiento implica responsabilidad: hacer copias de seguridad de las semillas, proteger el acceso, empezar con cantidades modestas. Con estas precauciones, LNbits se convierte en una solución robusta para la economía Lightning, al tiempo que preserva la descentralización y la autonomía.



## Recursos



### Documentación oficial




- [Documentación de LNbits](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [PHOENIXD GitHub](https://github.com/ACINQ/PHOENIXD)
- [Guía oficial de instalación](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### Guías comunitarias




- [Configuración inicial del servidor Ubuntu](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) por Daniel P. Costas (seguridad VPS paso a paso)
- [LNbits + PHOENIXD instalación en Ubuntu VPS](https://danielpcostas.dev/install-lnbits-PHOENIXD-vps-ubuntu/) por Daniel P. Costas (guía completa)
- [Servidor LNbits en Clearnet](https://ereignishorizont.xyz/lnbits-server/en/) por Axel
- [LNbits en VPS](https://github.com/TrezorHannes/vps-lnbits) por Hannes