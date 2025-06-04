---
name: LNbits
description: Plataforma de contabilidad comercial
---
![presentation](assets/lnbits-intro.webp)

# Sistema contable

LNbits está repleto de herramientas para controlar y canalizar tus fondos entrantes y salientes, conectar tu tienda web o incluso dispositivos como una cartera de hardware o un cajero automático que hayas construido tú mismo. Los tipos de usuario incluyen:


- Los propietarios de carteras que deseen utilizar LNbits como interfaz para la gestión de sus fondos, así como sus funciones adicionales.
- Comerciantes o proveedores de servicios online y offline que quieran aceptar pagos con Bitcoin onchain y Lightning Network.
- Desarrolladores que quieran crear aplicaciones de la Red Lightning.
- Operadores de nodos que deseen integrar su nodo con el sistema LNbits a efectos contables.
- Todos ellos tienen necesidades diferentes. Construimos LNbits de forma modular para que cada usuario pueda utilizar nuestras funciones de la forma que más le convenga.

# Gestor de carteras

LNbits es un sistema de contabilidad gratuito y de código abierto, no un gestor de nodos. La gestión de canales es el dominio del nodo Lightning que está conectado a LNbits como fuente de financiación como LND o c-lightning. El superusuario o los usuarios administradores del sistema LNbits son los responsables de gestionar la accesibilidad general y la configuración de las funciones de contabilidad y las extensiones internas.

LNbits actúa como interfaz entre el usuario y el nodo Lightning, proporcionando una forma sencilla y fácil de manejar e interactuar con la red de pagos.

Piensa en LNbits como un "framework modular de wordpress" para tu nodo. Una plataforma fácil de gestionar, basada en extensiones que puedes combinar para numerosos casos de uso.

Piensa en LNbits como tu propio software de gestión financiera bancaria. Su nodo ofrece canales para pagar a través de LNbits y se extiende a su nodo para ser capaz de ejecutar más de una cartera relámpago su nodo viene con. Estos monederos no tienen por qué pertenecerte a ti. Digamos que tú, como gestor del nodo LN, ya tienes suficiente liquidez de canales y fondos y ahora quieres ofrecer algunos servicios bancarios bitcoin a tus amigos, familia, tienda propia u otros comerciantes habituales.

Les ofrecerás una forma sencilla de abrir una "cuenta bancaria" en tu nodo sin tener acceso a otros monederos de tu nodo y a toda la liquidez de tu nodo, sino sólo a su parte. Tu nodo (el banco) sólo actúa como proveedor de transporte para sus pagos (entrada/salida).

NOTA: todos los fondos que tus "clientes" depositen en sus cuentas bancarias de LNbits en tu nodo, irán directamente a los canales LN de tu nodo. Eso significa que TÚ eres el verdadero propietario de esos fondos. Tendrás una gran responsabilidad sobre sus fondos. No seas malvado y huyas con los fondos, no seas malvado y cobres altas comisiones. Queremos joder a los banqueros fiat, no joder a los demás (usuarios de bitcoin).

# Plataforma de demostración

La demo se puede encontrar en [https://legend.lnbits.com](https://legend.lnbits.com). Es totalmente funcional y se puede utilizar para aprender acerca de la Lightning Network y las características de LNbits y LNURL en general. Aunque no podemos impedírtelo, nos gustaría pedirte que no lo utilices para tu configuración de producción. No sólo estamos trabajando en los servidores a menudo para probar nuevas características, sino que también nos gustaría animarte a ejecutar tu propio nodo y LNbits de forma soberana. Si crees que gestionar un nodo es demasiado pedir por el momento puedes conectar LNbits a un servicio de custodia de fondos en la nube como Opennode, Luna o Votage o al Lightning Tipbot en Telegram sólo por nombrar algunos.

# Folleto LNbits

¿Quiere entregar información básica a un comerciante o a un amigo suyo de la construcción? Nos complace anunciar nuestro primer folleto para uso de todos. El tamaño es un flyerformato típico global con 6 páginas (2 pliegues) y una anchura de 3508 y una altura de 2480px.

LNbits para comerciantes: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)

LNbits para constructores: [EN](/assets/lnbits-builders-es.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)

# Algunos aspectos básicos

LNbits funciona basándose en el protocolo LNURL, lo que significa que las solicitudes son válidas de dos formas: como enlace https:// clearnet (no se permiten certificados autofirmados) o como enlace http:// v2/v3 onion. Para ofrecer servicios LNbits como los códigos QR LNURLp/w o las tarjetas NFC, que se pueden utilizar in the wild, tendrás que abrir LNbits a clearnet (https).

Antes de instalar LNbits asegúrese de haber leído y comprendido las siguientes guías generales sobre qué es LNbits y qué posibilidades le ofrece.


- [Guía LND](https://docs.lightning.engineering/) | Instalación de LND
- [Ejemplo de configuración LND](https://github.com/lightningnetwork/lnd/blob/master/sample-lnd.conf) | Configuración LND
- [Guía de CLN](https://docs.corelightning.org/docs/installation) | Instalación de CLN
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips) Nostr Spec
- [Dirige una torre de vigilancia](https://docs.lightning.engineering/lightning-network-tools/lnd/watchtower) | ¡Muy importante!

Aquí encontrará guías más detalladas sobre el uso de LNbits en casos concretos:


- [Guía de iniciación a LNbits](https://darthcoin.substack.com/p/getting-started-lnbits) | Substack guide
- [ToDos para su seguridad con LNbits](https://youtu.be/i5FQf96e6zg) | Youtube Video
- [Bancos privados en Lightning Network](https://darthcoin.substack.com/p/bitcoin-private-banks-over-lightning) | Guía de subapilamiento
- [Ejecutar carteras custodio para sus amigos y familiares](https://darthcoin.substack.com/p/the-bank-of-lnbits) | Guía Substack
- [LNbits para un pequeño restaurante / hotel](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Guía Substack
- [Uso del copiloto Streamer de LNbits](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Guía de Substack
- [Inicie su Mercado NOSTR con LNbits](https://darthcoin.substack.com/p/lnbits-nostr-market) | Guía de Substack
- [Utilización de LNbits en proyectos escolares o festivales](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) Guía de subapilamiento

# Instalar LNbits

## Guía básica de instalación

LNbits puede instalarse en cualquier máquina con sistema operativo Linux. No requiere una máquina o servidor potente, sólo suficiente memoria RAM y algo de espacio en disco para la base de datos. Se puede ejecutar por separado de un nodo BTC/LN (PC local o VPS remoto) o juntos en la misma máquina con el nodo o ya instalado en una máquina de software de nodo de paquete.

Puedes elegir entre los gestores de paquetes más comunes como poetry y nix. Por defecto, LNbits utilizará SQLite como base de datos. También puedes usar PostgreSQL, que se recomienda para aplicaciones con mucha carga. [Aquí hay una guía para la instalación básica usando poetry o nix](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).

Para todos aquellos que sean nuevos en esto, encontrarán guías paso a paso más detalladas para conseguir que sus LNbits funcionen en entornos específicos:


- [LNbits en clearnet](https://ereignishorizont.xyz/lnbits-server/en/) por Axel
- [LNbits en un VPS](https://github.com/TrezorHannes/vps-lnbits) por Hannes
- [LNbits en cloudflare](https://www.nodeacademy.org/lnbits) por Leo

También puede encontrar un video en el [dockerised Configuración en un VPS con PostgreSQ, LightningTipBot como fuente de financiación utilizando nginx](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/).

[Más escenarios de instalación aquí](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).

Para los nodos de software de paquetes, consulte su documentación específica sobre LNbits: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)

## LNbits SaaS

Cuando no te interesan los aspectos técnicos y no quieres alojar tu fuente de financiación ni tus lnbits tú mismo, existe una [versión LNbits SaaS](https://saas.lnbits.com) (Software-as-a-service) que puedes utilizar. Es básicamente como LNbits en una nube, pero puedes definir la fuente de financiación (por ejemplo, tu Nodo, una cartera LNbits, el LNtipbot, fakewallet, etc.) y las variables de entorno tú mismo, lo que no suele ser el caso en otras soluciones en la nube.

[Aquí encontrará una guía detallada sobre cómo utilizar LNbits SaaS para casos de uso específicos](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).

## Fuentes de financiación

LNbits no es un software de gestión de nodos, sino un sistema de contabilidad centrado en LN sobre una fuente de financiación LND o CLN. Después de la primera instalación puedes visitar tu LNbits en http://localhost:5000/.

Para modificar la fuente de financiación vaya a su URL de superusuario y seleccione una fuente de financiación dentro de "Gestionar servidor" o edite el archivo .env modificando `LNBITS_BACKEND_WALLET_CLASS` a su fuente necesaria si establece `adminUI=TRUE` en el `.env`.

Encontrarás el archivo .env dentro de tu carpeta lnbits/ o lnbits/apps/data extendiendo el comando para listar archivos en tu directorio mediante `ls -a`.

Es posible que también tenga que instalar paquetes adicionales o realizar pasos de configuración adicionales, seleccionando la fuente de financiación deseada. Tras un reinicio, su nueva configuración estará activa.

¿Qué fuentes de financiación puedo utilizar para LNbits?

LNbits puede funcionar sobre muchas fuentes de financiación de redes de rayos. Actualmente hay soporte para CoreLightning, LND, LNbits, LNPay, OpenNode, y se añaden más regularmente.

Es importante elegir una fuente que tenga una buena liquidez y buenos pares conectados. Si utilizas LNbits para servicios públicos, los pagos de tus usuarios sólo podrán fluir alegremente en ambas direcciones.

Un monedero backend (fuente de fondos) puede configurarse utilizando las siguientes variables de entorno de LNbits en el archivo `.env` o dentro de su cuenta de superusuario en la sección Manage-Server.

Si desea utilizar la versión .env puede encontrar los parámetros aquí:

### CoreLightning


- CLN
  - `LNBITS_BACKEND_WALLET_CLASS`: **CoreLightningWallet**
  - `CORELIGHTNING_RPC`: /archivo/ruta/lightning-rpc
- Chispa (c-relámpago)
  - `LNBITS_BACKEND_WALLET_CLASS`: **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/rpc
   - `SPARK_TOKEN`: clave_de_acceso_secreta

### Daemon de la Red del Rayo


- LND (RESTO)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `LND_REST_CERT`: /archivo/ruta/tls.cert
  - `LND_REST_MACAROON`: /archivo/ruta/admin.macaroon o Bech64/Hex
  - `LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndWallet**
  - `LND_GRPC_ENDPOINT`: dirección_ip
  - `LND_GRPC_PORT`: puerto
  - `LND_GRPC_CERT`: /archivo/ruta/tls.cert
  - `LND_GRPC_MACAROON`: /archivo/ruta/admin.macaroon o Bech64/Hex

También puede utilizar en su lugar un macarrón cifrado con AES (más información) utilizando


  - `LND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

Para cifrar tu macaroon, ejecuta `./venv/bin/python lnbits/wallets/macaroon/macaroon.py`.

### LNbits (otra instancia de LNbits)


- Instancia de LNbits alojada en un servidor en la nube o en su propio servidor doméstico
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- Servidor de demostración de LNbits Legend (!! ¡¡¡NO utilices éste para producción / fines comerciales, sólo para pruebas!!)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://legend.lnbits.com
  - `LNBITS_KEY`: legend-lnbits-AdminKey

### Rayo TipBot

Para conectar tu [Lightning Tipbot](https://t.me/LightningTipBot) desde Telegram necesitarás configurar el siguiente parámetro:


  - `LNBITS_BACKEND_WALLET_CLASS`: **LnTipsWallet**
  - `LNBITS_ENDPOINT`: https://ln.tips
  - `LNBITS_KEY`: Para obtener la Clave tendrás que ejecutar /api en un chat privado con el LightningTipbot en Telegram una vez.

También ver este tutorial cómo instalar [LNbits con LightningTipBot a través de vps](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)

### IBEX HUB

Regístrese [aquí](https://ibexpay.ibexmercado.com/onboard) y obtenga sus claves/tokens desde allí, el punto final es https://ibexpay-api.ibexmercado.com.

Más información en [IBEX API-Documentation](https://ibexpay-api.readme.io/reference/getting-started-with-your-api).

### LNPay

Para que el receptor de facturas funcione, debes tener una URL de acceso público en tu LNbits y configurar un [LNPay webhook](https://dashboard.lnpay.co/webhook/) que apunte a `<tu host LNbits>/wallet/webhook` con el evento "Wallet Receive" y sin indicar ningún secreto. La configuración `https://mylnbits/wallet/webhook` será la url del endpoint que recibirá la notificación de cualquier pago.


  - `LNBITS_BACKEND_WALLET_CLASS`: **LNPayWallet**
  - `LNPAY_API_ENDPOINT`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey

### OpenNode

Para que la factura funcione, necesitas tener una URL accesible públicamente en tu LNbits. La configuración del webhook es opcional.


  - `LNBITS_BACKEND_WALLET_CLASS`: **OpenNodeWallet**
  - `OPENNODE_API_ENDPOINT`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey

### Alby

Alby es una extensión del navegador con funcionalidades de monedero LN y cuenta LNDHUB que puede utilizarse como fuente de financiación para LNbits. [Más información aquí](https://getalby.com/).

Para que la factura funcione debes tener una URL accesible públicamente en tu LNbits. No es necesario configurar manualmente el webhook. Puede generar un token de acceso Alby aquí: https://getalby.com/developer/access_tokens/new


- `LNBITS_BACKEND_WALLET_CLASS`: AlbyWallet
- `ALBY_API_ENDPOINT`: https://api.getalby.com/
- `ALBY_ACCESS_TOKEN`: AlbyAccessToken

## Guías adicionales / de solución de problemas

Aquí tienes algunas instrucciones adicionales en caso de que las necesites. Haga clic en la flecha para ampliar la descripción.

### The Killswitch 🚨

Últimamente se han producido tantos fallos peligrosos no sólo en todo el espacio, sino también en LNbits, que hemos decidido hacer algo al respecto. Ahora puedes optar por recibir advertencias y/o tomar medidas directas, cuando una vulnerabilidad o un error que podría conducir a la pérdida de fondos se produce de nuevo.

![killswitchn](assets/lnbits-killswitch.webp)

Si se cambia a void-wallet todos los tipos de usuario de la instancia verán un banner amarillo donde normalmente se encontraría el aviso "LNbits está en Beta" junto al área de tema/idioma a la derecha - y es la pista más obvia de que algo ha pasado. Echa un vistazo a tu nueva pestaña de servidor resaltada en verde en la parte izquierda de la ventana.

¿Cómo funciona? Cuando el killswitch está activado, un repositorio secreto de github sólo disponible para el equipo central de LNbits será comprobado en un intervalo de X minutos (que puede ser especificado). Si se publica un error vulnerable en este repositorio, sirve como una señal que activa el killswitch en todas las instalaciones que se suscribieron y las transiciones de su instancia lnbits para utilizar el monedero vacío. Si las nubes se han despejado y has instalado la actualización de seguridad puedes establecer tu fuente de financiación a tu nodo, monedero o lo que estés usando de nuevo también a través de la sección Gestionar Servidor. Esta wiki tiene una sección sobre cómo cambiar las fuentes de financiación si no sabes qué configurar.

### Diferencia entre admin y superusuario

La interfaz de administración de LNbits le permite cambiar la configuración de LNbits a través del frontend de LNbits. Está desactivado por defecto y la primera vez que se establece la variable de entorno `LNBITS_ADMIN_UI=true` en el archivo `.env`, la configuración se inicializa y se utilizará. A partir de ese momento se utilizarán los ajustes de la base de datos en lugar de los del archivo .env.

### Superusuario

Con la interfaz de administración hemos introducido el superusuario, que tiene acceso al servidor, por lo que puede cambiar la configuración que puede bloquear el servidor o hacer que no responda a través de frontend y api, como por ejemplo cambiar la fuente de financiación. El superusuario sólo se almacena dentro de la tabla de configuración de la base de datos. Después de que la configuración se "restablezca a los valores predeterminados" y se reinicie, se crea un nuevo superusuario. También hemos añadido un decorador para las rutas API para comprobar la existencia de un superusuario. Su ID nunca se envía a través de la api y el frontend y sólo recibe un bool (sí/no) si es superusuario o no.

Sólo el superusuario está autorizado a brrrr satoshis a diferentes monederos a través de la sección "Recargar".

También puede publicar el superusuario a través de webhook a otro servicio cuando se crea. Más información aquí https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`

En el frontend también encontrará la posibilidad de cambiar la imagen de la tienda que se muestra en la página "crear monedero" abriendo la sección Gestionar Servidor y eligiendo Tema -> Logotipo Personalizado.

### Usuarios administradores

Variable de entorno: `LNBITS_ADMIN_USERS`, lista de identificadores de usuario separados por comas. Los usuarios administradores pueden cambiar la configuración en la interfaz de administración - con la excepción de la configuración de la fuente de financiación, porque esto requeriría un reinicio del servidor y potencialmente podría hacer que el servidor inaccesible. También tienen acceso a todas las extensiones dedicadas a ellos en `LNBITS_ADMIN_EXTENSIONS`.

### Usuarios permitidos

Variable de entorno: `LNBITS_ALLOWED_USERS`, lista de IDs de usuarios separados por comas. Al definir estos usuarios, LNbits ya no podrá ser utilizado por el público. Sólo los usuarios definidos y los administradores podrán acceder al frontend de LNbits.

#### Actualizar LNbits

Una actualización normal de su instancia local de LNbits es simplemente copiando y pegando los siguientes comandos CLI:

```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```

Si ejecuta Raspiblitz o MyNode puede que necesite adicionalmente un

```
sudo systemctl restart lnbits
```

al final, porque ejecuta LNbits como un servicio.

En Umbrel/Citadel los comandos serían

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```

#### Migración de SQLite a PostgreSQL

Si ya tiene LNbits instalado y funcionando en una base de datos SQLite, le recomendamos encarecidamente que migre a Postgres si está planeando utilizar LNbits a gran escala.

Hay un script incluido que puede hacer la migración fácilmente. Necesitas tener Postgres ya instalado y debería haber una contraseña para el usuario (ver la guía de instalación de Postgres más arriba). Además, su instancia de LNbits necesita ejecutarse una vez en Postgres para implementar el esquema de la base de datos antes de que la migración pueda funcionar:

```
# STOP LNbits
# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit
# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

Esperemos que ahora todo funcione y se migre... Inicie LNbits de nuevo y compruebe que todo funciona correctamente.

#### Copia de seguridad y restauración de la base de datos

Consulte [esta guía muy detallada sobre el proceso de copia de seguridad y restauración](https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore).

#### Financiar mi monedero LNbits desde mi nodo no funciona

Si quieres enviar sats desde el mismo nodo que es la fuente de financiación de tus LNbits, tendrás que editar el archivo lnd.conf.

Los parámetros a incluir son: `allow-circular-route=1`

Hágalo en la sección Opciones de aplicación de su lnd.conf. De lo contrario, el inicio de LND podría fallar en algún nodo del paquete.

NOTA: Se recomienda utilizar la nueva extensión adminUI con la opción "TopUp" para añadir fondos a una cuenta de LNbits.

#### Error 426

Recibí el error "lnurl necesita ser entregado sobre dominio https de acceso público o tor. 426 upgrade required"</summary>

Este error generalmente se debe a que su LNbits detrás de un túnel ngnix no está reenviando la dirección LNURL correctamente. Detén tu LNbits y edita el archivo .env añadiendo esta línea:

`FORWARDED_ALLOW_IPS=*`

Además, si utiliza una configuración ngnix, asegúrese de tener estos encabezados en la configuración ngnix:

```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```

#### Error de red

Obtengo "error https", error de red" u otros al escanear un QR</summary>

Malas noticias, se trata de un error de enrutamiento que puede tener bastantes razones. Primero comprueba el LNURL del QR con el [Lightning Decoder](https://lightningdecoder.com/) si puedes encontrar algo raro ahí. Vamos a probar algunos de los problemas más posibles y sus soluciones.

LNbits funciona sólo a través de Tor, no puedes abrirlo en un dominio público como lnbits.tudominio.com


- Dado que quieres que tu configuración permanezca así abre tu monedero LNbits usando el .onion URI y créalo de nuevo. De esta manera el QR se genera para ser accesible a través de este .onion URI así que sólo a través de tor. No generes ese QR desde un URI .local, porque no será accesible a través de internet - sólo desde dentro de tu LAN.
- Abre la aplicación del monedero LN que utilizaste para escanear el QR y esta vez utiliza tor (consulta la configuración de la aplicación del monedero). Si la aplicación no ofrece tor, puedes usar Orbot (Android) en su lugar. Consulte la sección de instalación para obtener instrucciones detalladas sobre cómo abrir sus LNbits para clearnet/https.

#### Evitar que otros generen monederos en mis LNbits

Cuando ejecutas tus LNbits en clearnet básicamente todo el mundo puede generar una cartera en él. Dado que los fondos de tu nodo están ligados a estos monederos es posible que quieras evitarlo. Hay dos maneras de hacerlo:

Configure los usuarios y extensiones permitidos en el archivo `.env` ([vea el ejemplo de env aquí](https://github.com/lnbits/lnbits/blob/main/.env.example)). Esto solo funciona si usas la opción `adminUI=FALSE` en el archivo .env, de lo contrario necesitas hacerlo en la sección Administrar Servidor -> Usuarios -> Usuarios Permitidos. Todos los demás no serán permitidos después.

#### Personalizar el plazo de vencimiento de las facturas

Ahora puede generar facturas con una caducidad personalizada. Compatible con backends: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet ¡hasta ahora!

Puede establecer `LIGHTNING_INVOICE_EXPIRY` en su archivo .env o utilizar la AdminUI para cambiar el valor por defecto para todas las facturas. También hay un nuevo campo en el punto final /api/v1/payments donde puede establecer la caducidad en los datos JSON.

## Cartera-URL suprimida

### Cartera en el servidor de demostración legend.lnbits

Guarde siempre una copia de su wallet-URL, Export2phone-QR o LNDhub para sus propios wallets en un lugar seguro. LNbits NO PUEDE ayudarle a recuperarlos cuando los pierda.

### Monedero en su propia fuente/nodo de financiación

Guarde siempre una copia de su wallet-URL, Export2phone-QR o LNDhub para sus propios wallets en un lugar seguro. Puedes encontrar todos los usuarios de LNbits y wallet-IDs en tu extensión LNbits user manager o en tu base de datos sqlite. Para editar o leer la base de datos de LNbits, ve a la carpeta LNbits /data y busca el archivo llamado sqlite.db. Puedes abrirlo y editarlo con excel o con un editor SQL dedicado como [SQLite browser](https://sqlitebrowser.org/).

También puede volcar las carteras a través de cli y ver cada cartera dentro de su base de datos.

```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```

El resultado será algo parecido a esto

```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

y quieres poner estos valores en una url como esta

```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```

Sustituye f8a43fc363ea428db5c53b3559935f1f por el valor que aparece antes del nombre (en nuestro ejemplo f8a43fc363ea428db5c53b3559935f1f) y 1280ff5910a9c485a782a2376f338b6c es tu usuario y debería convertirse en el valor que aparece después del nombre. Para salir de sqlite3 pon

```
.quit
```

#### LNURL para una dirección lightning viceversa

Prueba este [codificador](https://lnurl-codec.netlify.app/) de fiatjaf o [este](https://lightningdecoder.com/). Para pagar o comprobar un LNURLp también puede utilizar [LNurlpay](https://wwww.lnurlpay.com/). Debe indicar HTTPS NO HTTP.

#### Configurar un comentario que la gente ve cuando paga a mi LNURLp QR

Cuando se crea una LNURL-p, por defecto no se rellena la casilla de comentarios. Eso significa que no se permite adjuntar comentarios a los pagos.

Para permitir comentarios, añada la longitud de caracteres de la casilla, de 1 a 250. Una vez que ponga un número, la caja de comentarios se mostrará en el proceso de pago. También puede editar un LNURL-p ya creado y añadir ese número.

![lnbits comments](assets/lnbits-comments.webp)

#### Depositar onchain BTC a LNbits

Hay dos maneras de intercambiar sats de onchain BTC a LN BTC (resp. a LNbits).

##### A través de un servicio de intercambio externo.

Otros usuarios que no tengan acceso a tu LNb its pueden utilizar un servicio de intercambio como [Boltz](https://boltz.exchange/), [FixedFloat](https://fixedfloat.com/), [DiamondHands](https://swap.diamondhands.technology/) o [ZigZag](https://zigzag.io/). Esto es útil si sólo proporcionas facturas LNURL/LN desde tu instancia de LNbits, pero un pagador sólo tiene saturaciones onchain, por lo que tendrá que intercambiar primero esas saturaciones por su parte. El procedimiento es sencillo: el usuario envía btc onchain al servicio de intercambio y proporciona la factura LNURL / LN de LNbits como destino del intercambio.

##### Uso de la extensión LNbits de Onchain y Boltz.

Ten en cuenta que se trata de un monedero independiente, no del monedero de LN btc que LNbits representa como "tu monedero" en tu fuente de financiación de LN. Este monedero onchain también se puede utilizar para intercambiar btc LN a (por ejemplo, su hardwarewallet) mediante el uso de la extensión LNbits Boltz o Deezy. Si tienes una tienda online que está vinculada a tu LNbits para pagos LN, es muy útil drenar regularmente toda la saturación de LN en onchain. Así tendrás más espacio en tus canales LN para poder recibir nuevos sats frescos.

Procedimiento para quienes no disponen de un monedero físico de bitcoin:


- Utiliza Electrum o Sparrow wallet para crear un nuevo monedero onchain y guarda la semilla de copia de seguridad en un lugar seguro.
- Ve a la información de la cartera y copia el xpub.
- Ve a LNbits - Extensión Onchain y crea un nuevo monedero sólo para relojes con ese xpub.
- Ve a LNbits - Extensión Tipjar y crea un nuevo Tipjar. Selecciona también la opción onchain además del monedero LN.
- Opcional - Ve a la extensión LNbits - SatsPay y crea un nuevo cargo para onchain btc. Puedes elegir entre onchain y LN o ambos. A continuación, creará una factura que se puede compartir.
- Opcional - Si utilizas tus LNbits vinculados a una página de Wordpress + Woocommerce, una vez que crees/vincules un monedero sólo para relojes a tu monedero de la tienda LN btc, el cliente tendrá ambas opciones para pagar en la misma pantalla.

Cuando reciba un pago en LNbits, el registro de transacciones sólo mostrará un tipo reanudado de la transacción.

![lnbits payment details](assets/lnbits-payment-details.webp)

En su resumen de transacciones encontrará una pequeña flecha verde para los fondos recibidos y una flecha roja para los fondos enviados.

Si haces clic en esas flechas, una ventana emergente de detalles muestra los mensajes adjuntos, así como el nombre del remitente, si se indica.

Configurar un nombre para que aparezca en los pagos, en LNbits actualmente no es posible hacerlo - pero sí recibirlo. Esto sólo es posible si el monedero LN del remitente soporta [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) como [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents).

A continuación, verá un alias/pseudónimo en la sección de detalles de sus transacciones de LNbits (haga clic en las flechas). Tenga en cuenta que puede dar cualquier nombre allí y puede que no esté relacionado con el nombre del remitente real si recibe tal.

![lnbits namedesc](assets/lnbits-namedesc.webp)

Para importar tu cuenta LNbits en una aplicación de monedero, abre tu LNbits con la cuenta / monedero que quieras utilizar, ve a "gestionar extensiones" y activa la extensión LNDHUB. Abre la extensión LNDHUB, elige el monedero que quieres usar y escanea el QR de "admin" o "sólo factura", dependiendo del nivel de seguridad que quieras para ese monedero.

Puede utilizar [Zeus](https://zeusln.app/) o [Bluewallet](https://bluewallet.io/) como aplicaciones de monedero para una cuenta de lndhub, ya que BW admite más de un monedero.

Al hacer esto, recomendamos también establecer el URI de la red LN al de tu propio nodo. Si tu instancia de LNbits es sólo Tor, también tienes que usar esas aplicaciones con Tor activado. También en este caso necesitas abrir la página de LNbits a través de tu dirección Tor .onion.

Si tiene un Error "unsupported hash type" cuando usa un ypub en la extensión On-chain, compruebe si su instancia de LNbits está usando python 3.10 podría estar afectada por [este problema](https://stackoverflow.com/questions/72409563/unsupported-hash-type-ripemd160-with-hashlib-in-python). Edite el openssl.cnf como se describe en la respuesta de stackoverflow y reinicie su LNbits.

## Herramientas y construcción con LNbits

LNbits tiene todo tipo de [APIs abiertas](https://legend.lnbits.com/docs) y herramientas para programar y conectarse a un montón de dispositivos diferentes para un gazillion de casos de uso.

Si eres nuevo en el mundo de la construcción, empieza con estas [presentaciones MakerBits](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) de Ben Arc sobre la construcción de gadgets basados en LNbits.

### IMPORTANTE:


- LNbits funciona basado en el protocolo LNURL cuyas peticiones son válidas de dos formas: como enlace https:// clearnet (no se permiten certificados autofirmados) o como enlace http:// v2/v3 onion. Para ofrecer servicios LNbits como los códigos QR LNURLp/w o las tarjetas NFC, que se pueden utilizar in the wild, tendrás que abrir LNbits a clearnet (https).
- Utilice sólo cables de DATOS para alimentar su esp32. No todos los cables soportan datos además de alimentar el esp. No serías el primero si el cable que viene con el esp es de sólo alimentación
- Asegúrate de no usar un USB-Hub con otros dispositivos conectados. Esto puede provocar efectos extraños difíciles de depurar (por ejemplo, que no se inicie o se detenga).
- Para realizar proyectos esp con un MacOS necesitará un UART Bridge Driver. Si tienes problemas con el driver en sistemas Mac o Linux, puedes encontrarlos aquí o, si se trata de un TTGO Display este. Si está en Windows y tiene problemas para conectarse asegúrese de descargar la versión ANTIGUA 11.1.0 porque la nueva no funciona También puedes encontrar un terminal serie aquí para comprobar tu conexión - configurado a 115200 baudios.
- Aunque es mucho más cómodo utilizar Platform.io (por ejemplo, las dependencias se instalan automáticamente) recomendamos el uso de Arduino para todos los nuevos en la construcción.
- Pantalla TT-Go S3: El color de la lengüeta de la lámina protectora de pantalla te indica qué controlador exactamente (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ..) se ha utilizado para construirla. Guárdelo para poder depurar si se programa y la pantalla no muestra los gráficos correctamente, por ejemplo, colores incorrectos, imágenes reflejadas o píxeles desviados en los bordes. Si alguna vez necesita hacer esto, hay una guía épica sobre el ajuste para diferentes pantallas
- Utilice siempre lnurl239xx en minúsculas en lugar de LNURLl239xx
- Añadir lightning:lnurl1234xyz creará un QR que solicita abrir la cartera del usuario para esta factura al escanearla (última aplicación de lightning instalada en iOS, configuración en Android)
- Si estás flasheando un esp32 vía web sólo funcionará con estos navegadores (TL:DR Chrome, Edge & Opera).
- Tenga en cuenta esta referencia PIN-OUT para el esp
- Cuando utilices FOSSoftware o FOSGuides, enlaza siempre al autor. A todo el mundo le gusta ver crecer a su bebé y también se inicia una cadena de construcción que es bastante impresionante de ver :)

Ven al [Grupo de Telegram de Makerbits](https://t.me/makerbits) si necesitas ayuda con un proyecto: ¡te tenemos!

![lnbits hackathlon](assets/lnbits-hackathlon.webp)

Aquí tienes algunas categorías de proyectos que puedes construir con LNbits:


- [Dispositivo de firma Nostr](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Máquina Archade](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Lámpara Nostr Zap](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Lightning Piggy](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Hardware Wallet](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-wallet)
- [Bitcoin Switch](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-switch)
- [Máquina expendedora](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora y la red de malla](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)
- [AYUDAS Y RECURSOS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [Más ejemplos de proyectos "Powered by LNbits" aquí](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [Casos prácticos de LNbits](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)