---
name: Nodo de rayos RGB
description: ¿Cómo lanzo un nodo Lightning compatible con RGB con RLN?
---
![cover](assets/cover.webp)

En este tutorial paso a paso, aprenderás a configurar un nodo Lightning RGB en un entorno Regtest. Veremos cómo crear tokens RGB y hacerlos circular en canales.

## El proyecto RLN

El equipo RGB de Bitfinex lleva trabajando desde 2022 para enriquecer el ecosistema RGB mediante el desarrollo de una pila tecnológica completa. En lugar de aspirar a un único producto comercial, sus esfuerzos se centran en poner a disposición ladrillos de software de código abierto, contribuir a las especificaciones del protocolo RGB y crear referencias de implementación.

Entre las notables contribuciones de Bitfinex al ecosistema RGB se encuentra [la biblioteca *RGBlib*](https://github.com/RGB-Tools/rgb-lib), escrita en Rust y accesible mediante bindings en Kotlin y Python, que simplifica enormemente el desarrollo de aplicaciones RGB al encapsular complejos mecanismos de validación y compromiso.

El equipo de Bitfinex también ha diseñado un monedero móvil RGB, llamado "[*Iris Wallet*](https://iriswallet.com/)", disponible en Android. Este monedero integra el uso de un servidor proxy RGB para gestionar fácilmente intercambios de datos fuera de la cadena (*consignaciones*) para *Client-side Validation* en RGB.

Bitfinex también ha desarrollado el proyecto `rgb-lightning-node` (RLN). Se trata de un demonio Rust basado en un fork de `rust-lightning` (LDK), modificado para tener en cuenta la existencia de activos RGB en un canal. Cuando se abre un canal, se puede especificar la presencia de tokens RGB, y cada vez que se actualiza el estado del canal, se crea una transición de estado que refleja la distribución de tokens en las salidas de Lightning. Esto permite :


- Abrir canales Lightning en USDT, por ejemplo;
- Encaminar estas fichas a través de la red, siempre que las vías de encaminamiento tengan suficiente liquidez;
- Explotar la lógica de castigo y timelock de Lightning sin modificaciones: basta con anclar la transición RGB en una salida adicional de la transacción de compromiso.

El código RLN aún está en fase alfa: recomendamos utilizarlo únicamente en **regtest** o en la **testnet**.

## Recordatorio del protocolo RGB

RGB es un protocolo que se ejecuta sobre Bitcoin y emula la funcionalidad de los contratos inteligentes y la gestión de activos digitales, sin sobrecargar la cadena de bloques en la que se basa. A diferencia de los contratos inteligentes on-chain convencionales (como en Ethereum, por ejemplo), RGB se basa en un sistema de "*validación del lado del cliente*": la mayoría de los datos e historiales de estado son intercambiados y almacenados exclusivamente por los participantes implicados, mientras que la blockchain de Bitcoin sólo alberga pequeños compromisos criptográficos (a través de mecanismos como *Tapret* u *Opret*). Por lo tanto, en el protocolo RGB, la blockchain de Bitcoin sólo sirve como servidor de sellado de tiempo y sistema de protección contra el doble gasto.

Un contrato RGB se estructura como una máquina de estados evolutiva. Comienza con una Génesis que define el estado inicial (describiendo, por ejemplo, la oferta, el ticker u otros metadatos) según un Esquema estrictamente tipado y compilado. A continuación se aplican Transiciones de Estado y, si es necesario, Extensiones de Estado para modificar o ampliar este estado. Cada operación, ya sea la transferencia de activos fungibles (RGB20) o la creación de activos únicos (RGB21), implica *Sellos de un solo uso*. Estos vinculan los UTXO de Bitcoin a estados fuera de la cadena y evitan el doble gasto, al tiempo que garantizan la confidencialidad y la escalabilidad.

Para saber más sobre cómo funciona el protocolo RGB, te recomiendo que sigas este completo curso de formación:

https://planb.network/courses/csv402
## Instalación del nodo Lightning compatible con RGB

Para compilar e instalar el binario `rgb-lightning-node`, comenzamos clonando el repositorio y sus submódulos, luego ejecutamos el archivo :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RLN](assets/fr/01.webp)


- La opción `--recurse-submodules` también clona los subdispositivos necesarios (incluida la versión modificada de `rust-lightning`);
- La opción `--shallow-submodules` restringe la profundidad del clon para acelerar la descarga, al tiempo que proporciona acceso a los commits esenciales.

Desde la raíz del proyecto, ejecute el siguiente comando para compilar e instalar el binario :

```bash
cargo install --locked --debug --path .
```

![RLN](assets/fr/02.webp)


- `--locked` garantiza que se respete la versión de las dependencias;
- `--debug` no es obligatorio, pero puede ayudarle a centrarse (puede utilizar `--release` si lo prefiere) ;
- `--path .` indica a `cargo install` que instale desde el directorio actual.

Al final de este comando, un ejecutable `rgb-lightning-node` estará disponible en su `$CARGO_HOME/bin/`. Asegúrese de que esta ruta está en su `$PATH` para que pueda invocar el comando desde cualquier directorio.

## Requisitos previos

Para funcionar, el demonio `rgb-lightning-node` necesita la presencia y configuración de :


- Un nodo `bitcoind`**

Cada instancia de RLN deberá comunicarse con `bitcoind` para difundir y supervisar sus transacciones en la cadena. Será necesario proporcionar al demonio la autenticación (nombre de usuario/contraseña) y la URL (host/puerto).


- Un indexador** (Electrum o Esplora)

El demonio debe ser capaz de listar y explorar transacciones en la cadena, en particular para encontrar el UTXO en el que se ha anclado un activo. Deberá especificar la URL de su servidor Electrum o Esplora.


- Un proxy RGB

El servidor proxy es un componente (opcional, pero muy recomendable) para simplificar el intercambio de *consignaciones* RGB entre pares Lightning. Una vez más, debe especificarse una URL.

Los ID y las URL se introducen cuando el demonio se *desbloquea* a través de la API.

## Lanzamiento de Regtest

Para un uso sencillo, hay un script `regtest.sh` que inicia automáticamente, a través de Docker, un conjunto de servicios: `bitcoind`, `electrs` (indexador), `rgb-proxy-server`.

![RLN](assets/fr/03.webp)

Permite lanzar un entorno local, aislado y preconfigurado. Crea y destruye contenedores y directorios de datos en cada reinicio. Comenzaremos iniciando el :

```bash
./regtest.sh start
```

Este script :


- Crea un directorio `docker/` para almacenar los archivos ;
- Ejecute `bitcoind` en regtest, así como el indexador `electrs` y el `rgb-proxy-server` ;
- Espere hasta que todo esté listo para usar.

![RLN](assets/fr/04.webp)

A continuación, lanzaremos varios nodos RLN. En shells separados, ejecute, por ejemplo (para lanzar 3 nodos RLN) :

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RLN](assets/fr/05.webp)


- El parámetro `--network regtest` indica el uso de la configuración regtest;
- `--daemon-listening-port` indica en qué puerto REST escuchará el nodo Lightning las llamadas a la API (JSON);
- `--ldk-peer-listening-port` especifica en qué puerto Lightning p2p escuchar;
- `dataldk0/`, `dataldk1/` son las rutas a los directorios de almacenamiento (cada nodo almacena su información por separado).

Ahora puede ejecutar comandos en sus nodos RLN desde su navegador, gracias a la API. En particular, aquí es donde puedes *desbloquear* demonios. Simplemente abre un navegador en el mismo ordenador que tus nodos, e introduce la URL :

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

Para que un nodo abra un canal, primero debe tener bitcoins en una dirección generada con el siguiente comando (para el nodo n°1, por ejemplo):

```bash
curl -X POST http://localhost:3001/address
```

La respuesta le proporcionará una dirección.

![RLN](assets/fr/06.webp)

En el Regtest `bitcoind`, vamos a minar algunos bitcoins. Ejecutar :

```bash
./regtest.sh mine 101
```

![RLN](assets/fr/07.webp)

Envíe los fondos a la dirección del nodo generada anteriormente:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RLN](assets/fr/08.webp)

Luego minar un bloque para confirmar la transacción:

```bash
./regtest.sh mine 1
```

![RLN](assets/fr/09.webp)

## Lanzamiento de Testnet (sin Docker)

Si desea probar un escenario más realista, puede lanzar nodos RLN en la Testnet en lugar de en Regtest, apuntando a servicios públicos, o a servicios que usted controle:

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

Por defecto, si no se encuentra ninguna configuración, el demonio intentará utilizar el archivo :


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

Con inicio de sesión :


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`

También puedes personalizar estos elementos a través de la API `init`/`unlock`.

## Emisión de una ficha RGB

Para emitir un token, empezaremos creando UTXOs "coloreables":

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RLN](assets/fr/10.webp)

Por supuesto, puede adaptar el pedido. Para confirmar la transacción, minamos un :

```bash
./regtest.sh mine 1
```

Ahora podemos crear un activo RGB. El comando dependerá del tipo de activo que desee crear y sus parámetros. Aquí estoy creando un token NIA (*Non Inflatable Asset*) llamado "PBN" con un suministro de 1000 unidades. La `precisión` le permite definir la divisibilidad de las unidades.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RLN](assets/fr/11.webp)

La respuesta incluye el identificador del activo recién creado. No olvide anotar este identificador. En mi caso, es :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RLN](assets/fr/12.webp)

A continuación, puedes transferirlo a la cadena o asignarlo a un canal Lightning. Eso es exactamente lo que vamos a hacer en la siguiente sección.

## Abrir un canal y transferir un activo RGB

Primero debe conectar su nodo a un peer de la red Lightning mediante el comando `/connectpeer`. En mi ejemplo, controlo ambos nodos. Así que recuperaré la clave pública de mi segundo nodo Lightning con este comando:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

El comando devuelve la clave pública de mi nodo n°2 :

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RLN](assets/fr/13.webp)

A continuación, abriremos el canal especificando el activo correspondiente (`PBN`). El comando `/openchannel` permite definir el tamaño del canal en satoshis y optar por incluir el activo RGB. Depende de lo que quieras crear, pero en mi caso, el comando es :

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

Más información aquí:


- `peer_pubkey_and_opt_addr`: Identificador del peer al que queremos conectarnos (la clave pública que encontramos antes);
- `capacidad_sat`: Capacidad total del canal en satoshis ;
- `push_msat`: Cantidad en milisatoshis transferida inicialmente al par cuando se abre el canal (aquí transfiero inmediatamente 10.000 sats para que él pueda hacer una transferencia RGB más tarde) ;
- `asset_amount`: Cantidad de activos RGB a comprometer en el canal ;
- `asset_id` : Identificador único del activo RGB involucrado en el canal;
- público Indica si el canal debe hacerse público para su enrutamiento en la red.

![RLN](assets/fr/14.webp)

Para confirmar la transacción, se minan 6 bloques:

```bash
./regtest.sh mine 6
```

![RLN](assets/fr/15.webp)

El canal Lightning ya está abierto y también contiene 500 tokens `PBN` por parte del nodo n°1. Si el nodo n°2 desea recibir tokens `PBN`, debe generar una factura. He aquí cómo hacerlo:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

Con :


- `amt_msat`: Importe de la factura en milisatoshis (mínimo 3000 sats) ;
- `expiry_sec` : Tiempo de expiración de la factura en segundos ;
- `asset_id` : Identificador del activo RGB asociado a la factura ;
- `importe_activo`: Importe del activo RGB que se va a transferir con esta factura.

En respuesta, obtendrá una factura RGB:

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RLN](assets/fr/16.webp)

Ahora pagaremos esta factura desde el primer nodo, que tiene el efectivo necesario con el token `PBN`:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RLN](assets/fr/17.webp)

Se ha efectuado el pago. Esto puede verificarse ejecutando el comando :

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RLN](assets/fr/18.webp)

He aquí cómo desplegar un nodo Lightning modificado para transportar activos RGB. Esta demostración se basa en :


- Un entorno regtest (mediante `./regtest.sh`) o testnet ;
- Un nodo Lightning (`rgb-lightning-node`) basado en un `bitcoind`, un indexador y un `rgb-proxy-server` ;
- Una serie de API REST JSON para abrir/cerrar canales, emitir tokens, transferir activos a través de Lightning, etc.

Gracias a este proceso :


- Las transacciones de compromiso relámpago incluyen una salida adicional (OP_RETURN o Taproot) con el anclaje de una transición RGB;
- Las transferencias se realizan exactamente igual que los pagos Lightning tradicionales, pero añadiendo un token RGB;
- Múltiples nodos RLN pueden estar vinculados para enrutar y experimentar con pagos a través de múltiples nodos, siempre que haya suficiente liquidez tanto en bitcoins como en activos RGB en el camino.

Si este tutorial te ha resultado útil, te agradecería mucho que pusieras un pulgar verde abajo. No dudes en compartir este artículo en tus redes sociales. ¡Muchas gracias!

También recomiendo este otro tutorial en el que explico cómo utilizar la herramienta RGB CLI desarrollada por la asociación LNP/BP para crear un contrato RGB:

https://planb.network/tutorials/node/rgb/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4