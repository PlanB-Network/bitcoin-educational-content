---
name: RGB CLI
description: ¿Cómo puedo crear e intercambiar contratos inteligentes en RGB?
---
![cover](assets/cover.webp)

En este tutorial, seguiremos paso a paso el proceso de escritura de un contrato, utilizando la herramienta de línea de comandos `rgb` creada por la asociación LNP/BP. El objetivo es mostrar cómo instalar y manipular la CLI, compilar un esquema, importar la interfaz y la implementación de la interfaz y, a continuación, emitir un activo RGB. También veremos la lógica subyacente, incluyendo la compilación y la validación del estado. Al final de este tutorial, deberías ser capaz de reproducir el proceso y crear tus propios contratos RGB.

## Recordatorio del protocolo RGB

RGB es un protocolo que se ejecuta sobre Bitcoin y emula la funcionalidad de los contratos inteligentes y la gestión de activos digitales, sin sobrecargar la cadena de bloques en la que se basa. A diferencia de los contratos inteligentes on-chain convencionales (como en Ethereum, por ejemplo), RGB se basa en un sistema de "*validación del lado del cliente*": la mayoría de los datos e historiales de estado son intercambiados y almacenados exclusivamente por los participantes implicados, mientras que la blockchain de Bitcoin sólo alberga pequeños compromisos criptográficos (a través de mecanismos como *Tapret* u *Opret*). Por lo tanto, en el protocolo RGB, la blockchain de Bitcoin sólo sirve como servidor de sellado de tiempo y sistema de protección contra el doble gasto.

Un contrato RGB se estructura como una máquina de estados evolutiva. Comienza con una Génesis que define el estado inicial (describiendo, por ejemplo, la oferta, el ticker u otros metadatos) según un Esquema estrictamente tipado y compilado. A continuación se aplican Transiciones de Estado y, si es necesario, Extensiones de Estado para modificar o ampliar este estado. Cada operación, ya sea la transferencia de activos fungibles (RGB20) o la creación de activos únicos (RGB21), implica *Sellos de un solo uso*. Estos vinculan los UTXO de Bitcoin a estados fuera de la cadena y evitan el doble gasto, al tiempo que garantizan la confidencialidad y la escalabilidad.

Para saber más sobre cómo funciona el protocolo RGB, te recomiendo que sigas este completo curso de formación:

https://planb.network/courses/csv402
La lógica interna de RGB se basa en bibliotecas Rust que ustedes, como desarrolladores, pueden importar a sus proyectos para gestionar la parte de *Validación del lado del cliente*. Además, el equipo de LNP/BP está trabajando en bindings para otros lenguajes, pero aún no se ha finalizado. Además, otras entidades como Bitfinex están desarrollando sus propias pilas de integración, pero hablaremos de ellas en otro tutorial. Por el momento, la CLI `rgb` es la referencia oficial, aunque siga estando relativamente sin pulir.

## Instalación y presentación de la herramienta rgb CLI

El comando principal se llama simplemente `rgb`. Está diseñado para recordar a `git`, con un conjunto de subcomandos para manipular contratos, invocarlos, emitir activos, etc. Bitcoin Wallet no está integrado actualmente, pero lo estará en una versión inminente (0.11). Esta próxima versión permitirá a los usuarios crear y gestionar sus monederos (a través de descriptores) directamente desde `rgb`, incluyendo la generación de PSBT, compatibilidad con hardware externo (por ejemplo, un monedero hardware) para firmar, e interoperabilidad con software como Sparrow. Esto simplificará todo el escenario de emisión y transferencia de activos.

### Instalación a través de Cargo

Instalamos la herramienta en Rust con :

```bash
cargo install rgb-contracts --all-features
```

(Nota: el crate se llama `rgb-contracts`, y el comando instalado se llamará `rgb`. Si ya existía un crate llamado `rgb`, podría haber habido una colisión, de ahí el nombre)

La instalación compila un gran número de dependencias (por ejemplo, análisis sintáctico de comandos, integración de Electrum, gestión de pruebas de conocimiento-cero, etc.).

Una vez finalizada la instalación, el archivo :

```bash
rgb
```

Al ejecutar `rgb` (sin argumentos) aparece una lista de subcomandos disponibles, como `interfaces`, `schema`, `import`, `export`, `issue`, `invoice`, `transfer`, etc. Puede cambiar el directorio de almacenamiento local (un alijo que contiene todos los registros, esquemas e implementaciones), elegir la red (testnet, mainnet) o configurar su servidor Electrum.

![RGB-CLI](assets/fr/01.webp)

### Primera visión general de los controles

Cuando ejecutes el siguiente comando, verás que ya viene integrada por defecto una interfaz `RGB20`:

```bash
rgb interfaces
```

Si esta interfaz no está integrada, clone el archivo :

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Compílalo:

```bash
cargo run
```

A continuación, importe la interfaz que desee:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-CLI](assets/fr/02.webp)

Sin embargo, nos dicen que todavía no se ha importado ningún esquema al programa. Tampoco hay ningún contrato en el almacén. Para verlo, ejecute el comando :

```bash
rgb schemata
```

A continuación, puede clonar el repositorio para recuperar determinados esquemas:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-CLI](assets/fr/03.webp)

Este repositorio contiene, en su directorio `src/`, varios archivos Rust (por ejemplo `nia.rs`) que definen esquemas (NIA para "*Activo No Inflable*", UDA para "*Activo Digital Único*", etc.). Para compilar, puede ejecutar :

```bash
cd rgb-schemata
cargo run
```

Esto genera varios archivos `.rgb` y `.rgba` correspondientes a los esquemas compilados. Por ejemplo, encontrarás `NonInflatableAsset.rgb`.

### Importación de esquemas e interfaces

Ahora puede importar el esquema en `rgb` :

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-CLI](assets/fr/04.webp)

Esto lo añade al almacén local. Si ejecutamos el siguiente comando, veremos que ahora aparece el esquema:

```bash
rgb schemata
```

## Creación de contratos (emisión)

Existen dos enfoques para crear un nuevo activo:


- O bien utilizamos un script o código en Rust que construye un Contrato rellenando los campos del esquema (estado global, Estados Propios, etc.) y produce un archivo `.rgb` o `.rgba`;
- O utilice directamente el subcomando `issue`, con un archivo YAML (o TOML) que describa las propiedades del token.

Puedes encontrar ejemplos en Rust en la carpeta `examples`, que ilustran cómo se construye un `ContractBuilder`, se rellena el `global state` (nombre del activo, ticker, suministro, fecha, etc.), se define el Owned State (a qué UTXO está asignado), y luego se compila todo esto en una *contratación de consignación* que puedes exportar, validar e importar a un alijo.

La otra forma es editar manualmente un archivo YAML para personalizar el `ticker`, el `name`, el `supply`, etc. Supongamos que el archivo se llama `RGB20-demo.yaml`. Puede especificar :


- `spec`: ticker, nombre, precisión ;
- `terms`: un campo para avisos legales ;
- `issuedSupply` : la cantidad de fichas emitidas ;
- `assignments`: indica el precinto de un solo uso (*definición del precinto*) y la cantidad desbloqueada.

He aquí un ejemplo de archivo YAML a crear:

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-CLI](assets/fr/05.webp)

A continuación, basta con ejecutar el comando :

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-CLI](assets/fr/06.webp)

En mi caso, el identificador único del esquema (que debe ir entre comillas simples) es `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` y no he puesto ningún emisor. Así que mi orden es :

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

Si no conoce el ID del esquema, ejecute el comando :

```bash
rgb schemata
```

La CLI responde que se ha emitido un nuevo contrato y se ha añadido al alijo. Si tecleamos el siguiente comando, veremos que ahora hay un contrato adicional, correspondiente al que se acaba de emitir:

```bash
rgb contracts
```

![RGB-CLI](assets/fr/07.webp)

A continuación, el siguiente comando muestra los estados globales (nombre, ticker, suministro...) y la lista de estados propios, es decir, asignaciones (por ejemplo, 1 millón de fichas `PBN` definidas en UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-CLI](assets/fr/08.webp)

## Exportación, importación y validación

Para compartir este contrato con otros usuarios, puede exportarse desde el alijo a un archivo :

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-CLI](assets/fr/09.webp)

El archivo `myContractPBN.rgb` puede pasarse a otro usuario, que puede añadirlo a su alijo con el comando :

```bash
rgb import myContractPBN.rgb
```

En la importación, si se trata de un simple *envío de contrato*, obtendremos un mensaje "`Importing consignment rgb`". Si se trata de un *envío de transición de estado* más grande, el comando será diferente (`rgb accept`).

Para garantizar la validez, también puede utilizar la función de validación local. Por ejemplo, puede ejecutar :

```bash
rgb validate myContract.rgb
```

### Uso, verificación y visualización del alijo

Como recordatorio, el alijo es un inventario local de esquemas, interfaces, implementaciones y contratos (Génesis + transiciones). Cada vez que ejecutas "importar", añades un elemento al alijo. Este alijo puede verse en detalle con el comando :

```bash
rgb dump
```

![RGB-CLI](assets/fr/10.webp)

Esto generará una carpeta con los detalles de todo el alijo.

## Transferencia y PSBT

Para realizar una transferencia, necesitará manipular un monedero Bitcoin local para gestionar los compromisos `Tapret` u `Opret`.

### Generar una factura

En la mayoría de los casos, la interacción entre los participantes en un contrato (por ejemplo, Alice y Bob) tiene lugar a través de la generación de una factura. Si Alice quiere que Bob ejecute algo (una transferencia de tokens, una reemisión, una acción en un DAO, etc.), Alice crea una factura detallando sus instrucciones a Bob. Así tenemos :


- Alice** (el emisor de la factura) ;
- Bob** (que recibe y ejecuta la factura).

A diferencia de otros ecosistemas, una factura RGB no se limita a la noción de pago. Puede incluir cualquier solicitud vinculada al contrato: revocar una clave, votar, crear un grabado (*grabado*) en una NFT, etc. La operación correspondiente puede describirse en la interfaz del contrato. La operación correspondiente puede describirse en la interfaz del contrato.

El siguiente comando genera una factura RGB:

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

Con :


- `$CONTRACT`: Identificador del contrato (*ContractId*) ;
- `$INTERFACE`: la interfaz que debe utilizarse (por ejemplo, `RGB20`) ;
- `$ACTION`: el nombre de la operación especificada en la interfaz (para una simple transferencia de token fungible, podría ser "Transfer"). Si la interfaz ya proporciona una acción por defecto, no es necesario volver a introducirla aquí;
- `$STATE`: los datos de estado que se van a transferir (por ejemplo, una cantidad de tokens si se transfiere un token fungible);
- `$SEAL`: el sello de un solo uso del beneficiario (Alice), es decir, una referencia explícita a un UTXO. Bob utilizará esta información para construir la transacción testigo, y la salida correspondiente pertenecerá entonces a Alice (en forma *de UTXO cegado* o sin cifrar).

Por ejemplo, con los siguientes comandos

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

La CLI generará una factura como :

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

Puede transmitirse a Bob a través de cualquier canal (texto, código QR, etc.).

### Realizar una transferencia

Para transferir desde esta factura :


- Bob (que tiene los tokens en su alijo) tiene un monedero Bitcoin. Necesita preparar una transacción Bitcoin (en forma de PSBT, por ejemplo `tx.psbt`) que gaste los UTXOs donde se encuentran los tokens RGB necesarios, más un UTXO para la moneda (intercambio) ;
- Bob ejecuta el siguiente comando:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- Esto genera un archivo `consignment.rgb` que contiene :
 - El historial de transición prueba a Alice que las fichas son auténticas;
 - La nueva transición que transfiere fichas al Sello de un solo uso de Alice ;
 - Una transacción testigo (sin firma).
- Bob envía este archivo `consignment.rgb` a Alice (por correo electrónico, un servidor de intercambio o un protocolo RGB-RPC, Storm, etc.);
- Alice recibe `consigna.rgb` y lo acepta en su propio alijo :

```bash
alice$ rgb accept consignment.rgb
```


- La CLI comprueba la validez de la transición y la añade al alijo de Alice. Si no es válida, el comando falla con mensajes de error detallados. De lo contrario, tiene éxito, e informa de que la transacción de muestra aún no se ha emitido en la red Bitcoin (Bob está esperando la luz verde de Alice);
- A modo de confirmación, el comando `accept` devuelve una firma (*ficha de pago*) que Alice puede enviar a Bob para demostrarle que ha validado la *consignación* ;
- Bob puede entonces firmar y publicar (`--publish`) su transacción Bitcoin:

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- Tan pronto como esta transacción se confirma en la cadena, la propiedad del activo se considera transferida a Alice. El monedero de Alice, monitorizando el minado de la transacción, ve aparecer en su alijo el nuevo Owned State.

Ahora ya sabes cómo emitir y transferir un contrato RGB. Si este tutorial te ha resultado útil, te agradecería mucho que pusieras un pulgar verde abajo. No dudes en compartir este artículo en tus redes sociales. Muchas gracias

También recomiendo este otro tutorial en el que explico cómo lanzar un nodo Lightning compatible con RGB para intercambiar tokens de forma casi instantánea:

https://planb.network/tutorials/node/rgb/rln-ffc02528-329b-4e16-bd83-873d0299feea