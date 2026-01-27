---
name: RGB
description: Introducción y creación de activos en RGB
---

![cover](assets/cover.webp)

## Introducción

El 3 de enero de 2009, Satoshi Nakamoto lanzó el primer nodo de Bitcoin, a partir de ese momento se unieron nuevos nodos y Bitcoin comenzó a comportarse como si fuera una nueva forma de vida, una forma de vida que no ha dejado de evolucionar, poco a poco se ha convertido en la red más segura del mundo como resultado de su diseño único, muy bien pensado por Satoshi, ya que atrae a los usuarios comúnmente llamados mineros a invertir en energía y potencia informática, lo que contribuye a la seguridad de la red.

A medida que Bitcoin continúa creciendo y siendo adoptado, se enfrenta a problemas de escalabilidad, la red de Bitcoin permite que se mine un nuevo bloque con transacciones en un tiempo aproximado de 10 minutos, suponiendo que tengamos 144 bloques en un día con valores máximos de 2700 transacciones por bloque, Bitcoin solo permitiría 4.5 transacciones por segundo, Satoshi era consciente de esta limitación, podemos verlo en un correo electrónico1 enviado a Mike Hearn en marzo de 2011 donde explica cómo funciona lo que hoy conocemos como un canal de pago. micropagos de forma rápida y segura sin esperar confirmaciones. Aquí es donde entran en juego los protocolos fuera de la cadena.

Según Christian Decker2, los protocolos fuera de la cadena suelen ser sistemas en los que los usuarios utilizan datos de una cadena de bloques y los gestionan sin tocar la cadena de bloques en sí hasta el último minuto. Basándose en este concepto, nació la Lightning Network, una red que utiliza protocolos fuera de la cadena para permitir pagos de Bitcoin casi instantáneos y, dado que no todas estas operaciones se escriben en la cadena de bloques, permite miles de transacciones por segundo y escala Bitcoin.

La investigación y el desarrollo en el área de los protocolos fuera de la cadena en Bitcoin han abierto una caja de Pandora, hoy sabemos que podemos lograr mucho más que la transferencia de valor de manera descentralizada, la Asociación de Normas LNP/BP sin ánimo de lucro se centra en el desarrollo de protocolos de capa 2 y 3 en Bitcoin y la Lightning Network, entre estos proyectos destaca RGB.

## ¿Qué es RGB?

RGB ha surgido de la investigación de Peter Todd3 sobre sellos de un solo uso y validación del lado del cliente, que fue acuñado en 2016-2019 por Giacomo Zucco y la comunidad en un mejor protocolo de activos para Bitcoin y la red Lightning. La evolución posterior de estas ideas llevó al desarrollo de RGB en un sistema de contratos inteligentes completamente funcional por Maxim Orlovsky, quien lidera su implementación desde 2019 con la participación de la comunidad.

Podemos definir RGB como un conjunto de protocolos de código abierto que nos permite ejecutar contratos inteligentes complejos de manera escalable y confidencial. No es una red en particular (como Bitcoin o Lightning); cada contrato inteligente es simplemente un conjunto de participantes del contrato que pueden interactuar utilizando diferentes canales de comunicación (con la opción predeterminada de la red Lightning). RGB utiliza la cadena de bloques de Bitcoin como una capa de compromiso de estado y mantiene el código del contrato inteligente y los datos fuera de la cadena, lo que lo hace escalable, aprovechando las transacciones de Bitcoin (y Script) como un sistema de control de propiedad para los contratos inteligentes; mientras que la evolución del contrato inteligente está definida por un esquema fuera de la cadena, finalmente es importante destacar que todo se valida en el lado del cliente.

En términos simples, RGB es un sistema que permite al usuario auditar un contrato inteligente, ejecutarlo y verificarlo individualmente en cualquier momento sin tener un costo adicional, ya que no utiliza una cadena de bloques como lo hacen los sistemas "tradicionales". Los sistemas de contratos inteligentes complejos fueron pioneros en Ethereum, pero debido a que requieren que el usuario gaste cantidades significativas de gas para cada operación, nunca lograron la escalabilidad que prometieron, por lo tanto, nunca fue una opción para bancarizar a los usuarios excluidos del sistema financiero actual.
Actualmente, la industria de la cadena de bloques promueve que tanto el código de los contratos inteligentes como los datos deben almacenarse en la cadena de bloques y ser ejecutados por cada nodo de la red, sin importar el aumento excesivo de tamaño o el mal uso de los recursos computacionales. El esquema propuesto por RGB es mucho más inteligente y eficiente, ya que rompe con el paradigma de la cadena de bloques al tener contratos inteligentes y datos separados de la cadena de bloques, evitando así la saturación de la red que se ve en otras plataformas. Además, no obliga a cada nodo a ejecutar cada contrato, sino a las partes involucradas, lo que agrega confidencialidad a un nivel nunca antes visto.

![RGB vs Ethereum](assets/1.webp)

## Contratos inteligentes en RGB

En RGB, el desarrollador de contratos inteligentes define un esquema que especifica las reglas de cómo evoluciona el contrato con el tiempo. El esquema es el estándar para la construcción de contratos inteligentes en RGB, y tanto un emisor al definir un contrato para la emisión como una billetera o intercambio deben adherirse a un esquema particular contra el cual deben validar el contrato. Solo si la validación es correcta, cada parte puede aceptar solicitudes y trabajar con el activo.

Un contrato inteligente en RGB es un grafo acíclico dirigido (DAG) de cambios de estado, donde solo una parte del grafo siempre es conocida y no hay acceso al resto. El esquema RGB es un conjunto de reglas básicas para la evolución de este grafo con el que comienza el contrato inteligente. Cada participante del contrato puede agregar reglas a esas reglas (si esto está permitido por el esquema) y el grafo resultante se construye a partir de la aplicación iterativa de esas reglas.

## Activos fungibles

Los activos fungibles en RGB siguen la especificación LNPBP RGB-20, cuando se define un RGB-20, los datos del activo conocidos como "datos de génesis" se distribuyen a través de la red Lightning, que contiene lo necesario para utilizar el activo. La forma más básica de los activos no permite emisión secundaria, quema de tokens, renominación o reemplazo.

A veces, el emisor necesitará emitir más tokens en el futuro, es decir, stablecoins como USDT, que mantiene el valor de cada token vinculado al valor de una moneda inflacionaria como el USD. Para lograr esto, existen esquemas RGB-20 más complejos, y además de los datos de génesis, requieren que el emisor produzca envíos, que también circularán en la red Lightning; con esta información podemos conocer la oferta circulante total del activo. Lo mismo se aplica a los activos quemados o al cambio de su nombre.

La información relacionada con el activo puede ser pública o privada: si el emisor requiere confidencialidad, puede optar por no compartir información sobre el token y realizar operaciones en total privacidad, pero también tenemos el caso contrario en el que el emisor y los titulares necesitan que todo el proceso sea transparente. Esto se logra compartiendo los datos del token.

## Procedimientos RGB-20

El procedimiento de quema deshabilita los tokens, los tokens quemados ya no se pueden utilizar.

El procedimiento de reemplazo ocurre cuando se queman tokens y se crea una nueva cantidad del mismo token. Esto ayuda a reducir el tamaño de los datos históricos del activo, lo cual es importante para mantener la velocidad del activo.

Para admitir el caso de uso en el que es posible quemar activos sin tener que reemplazarlos, se utiliza un subesquema de RGB-20 que solo permite quemar activos.

## Activos no fungibles

Los activos no fungibles en RGB siguen la especificación RGB-21 del LNPBP5, cuando trabajamos con NFTs también tenemos un esquema principal y un subesquema. Estos esquemas tienen un procedimiento de grabado, que nos permite adjuntar datos personalizados por parte del propietario del token, el ejemplo más común que vemos en los NFTs hoy en día es el arte digital vinculado al token. El emisor del token puede prohibir este grabado de datos utilizando el subesquema RGB-21. A diferencia de otros sistemas blockchain de NFT, RGB permite distribuir datos de token de medios de gran tamaño de manera completamente descentralizada y resistente a la censura, utilizando una extensión a la red P2P Lightning llamada Bifrost, que también se utiliza para construir muchas otras formas de funcionalidades de contratos inteligentes específicos de RGB.

Además de los activos fungibles y los NFTs, RGB y Bifrost se pueden utilizar para producir otras formas de contratos inteligentes, incluyendo DEXes, pools de liquidez, monedas estables algorítmicas, etc., de los cuales hablaremos en futuros artículos.

## NFT de RGB vs NFT de otras plataformas

- No se necesita un almacenamiento costoso en la blockchain
- No se necesita IPFS, en su lugar se utiliza una extensión de la red Lightning (llamada Bifrost) que está completamente cifrada de extremo a extremo
- No se necesita una solución especial de gestión de datos, nuevamente, Bifrost cumple ese papel
- No se necesita confiar en sitios web para mantener los datos de los tokens NFT o sobre los activos / contratos ABIs
- Cifrado DRM incorporado y gestión de propiedad
- Infraestructura para copias de seguridad utilizando la Red Lightning (Bifrost)
- Formas de monetizar contenido (no solo vendiendo el NFT en sí, sino también el acceso al contenido, varias veces)

## Conclusiones

Desde el lanzamiento de Bitcoin, hace casi 13 años, ha habido mucha investigación y experimentación en el área, tanto los éxitos como los errores nos han permitido entender un poco más cómo se comportan los sistemas descentralizados en la práctica, qué los hace realmente descentralizados y qué acciones tienden a llevarlos a la centralización, todo esto nos ha llevado a concluir que la descentralización real es un fenómeno raro y difícil de lograr, la descentralización real solo se ha logrado con Bitcoin y es por esta razón que enfocamos nuestros esfuerzos en construir sobre él.

RGB tiene su propio agujero de conejo dentro del agujero de conejo de Bitcoin, mientras caigo a través de ellos, publicaré lo que he aprendido, en el próximo artículo tendremos una introducción a los nodos LNP y RGB y cómo usarlos.

- 1 https://plan99.net/~mike/satoshi-emails/thread4.html
- 2 https://btctranscripts.com/chaincode-labs/chaincode-residency/2018-10-22-christian-decker-history-of-lightning/
- 3 https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2016-June/012773.html
- 4 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0020.md
- 5 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0021.md

## Tutorial de RGB-node

### Introducción

En este tutorial explicamos cómo usar RGB-node para crear un token fungible y cómo transferirlo, este documento se basa en la demostración de RGB-node y difiere en que este tutorial utiliza datos reales de la testnet y para eso, debemos construir nuestra propia Transacción Parcialmente Firmada de Bitcoin, psbt a partir de ahora.

### Requisitos

Se recomienda el uso de una distribución de Linux, este tutorial fue escrito usando Pop!/\_OS, que está basado en Ubuntu y necesitarás:

- cargo
- Bitcoin core
- git

Nota: Este tutorial muestra la ejecución de comandos en una terminal de Linux, para diferenciar lo que escribe el usuario y la respuesta que obtiene en la terminal, incluimos el símbolo $ que simboliza el indicador de bash.

Necesitarás instalar algunas dependencias:

```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```

Compilar y ejecutar

RGB-node está en progreso (WIP), por eso debemos ubicarnos en un commit específico (3f3c520c19d84c66d430e76f0fc68c5a66d79c84) para poder compilarlo y usarlo correctamente, para esto ejecutamos los siguientes comandos.

```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```

Ahora lo compilamos, no olvides usar la bandera --locked porque hay un cambio importante introducido en una versión de clap.

```
$ cargo install --path . --all-features --locked

....
....
    Finished release [optimized] target(s) in 2m 14s
  Installing /home/user/.cargo/bin/fungibled
  Installing /home/user/.cargo/bin/rgb-cli
  Installing /home/user/.cargo/bin/rgbd
  Installing /home/user/.cargo/bin/stashd
   Installed package `rgb_node v0.4.2 (/home/user/dev/rgb-node)` (executables `fungibled`, `rgb-cli`, `rgbd`, `stashd`)

```

Como nos indica el compilador de Rust, los binarios se copiaron al directorio $HOME/.cargo/bin, si tu compilador los copió a un lugar diferente, debes asegurarte de que ese directorio esté incluido en $PATH.

Entre los binarios instalados podemos ver tres daemons o servicios (los archivos que terminan en d) y una interfaz de línea de comandos (cli), la cli nos permite interactuar con el daemon principal rgbd. Como en este tutorial vamos a ejecutar dos nodos, también necesitaremos dos clientes, cada uno debe conectarse a su propio nodo, para eso creamos dos alias.

```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```

Podemos simplemente ejecutar los alias o agregarlos al final del archivo $HOME/.bashrc y ejecutar source $HOME/.bashrc.
Premisa

RGB-node no maneja ninguna funcionalidad relacionada con la billetera, simplemente realiza tareas específicas de RGB en los datos que serán proporcionados por una billetera externa como bitcoin core. En particular, para demostrar un flujo de trabajo básico con emisión y transferencia, necesitaremos:

- Un issuance_utxo al que rgb-node-0 vinculará el nuevo activo emitido
- Un receive_utxo donde rgb-node-1 recibirá el activo
- Un change_utxo donde rgb-node-0 recibirá el cambio del activo
- Una transacción de Bitcoin parcialmente firmada (tx.psbt), cuya clave pública de salida se ajustará para incluir un compromiso con la transferencia.
  Usaremos la interfaz de línea de comandos de Bitcoin Core, necesitamos tener el daemon bitcoind ejecutándose en testnet, esto nos dará interoperabilidad y al final podremos enviar nuestros propios activos a otros usuarios de RGB que hayan seguido este tutorial.
  Para simplificar, agregaremos este alias al final de nuestro archivo ~/.bashrc.

```
alias bcli="bitcoin-cli -testnet"
```

Vamos a listar nuestras transacciones de salida no gastadas y seleccionar dos, una será la issuance_utxo y la otra será la change_utxo, no importa cuál sea cuál, lo importante es que el emisor tenga el control de estos dos UTXO.

```
$ bcli listunspent
[
  {
    "txid": "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893",
    "vout": 1,
    "address": "tb1qn4w9u5x0hxgm30hx6q2rhdwz58xr4ekqdq0vgm",
    "label": "",
    "scriptPubKey": "00149d5c5e50cfb991b8bee6d0143bb5c2a1cc3ae6c0",
    "amount": 0.01703963,
    "confirmations": 62432,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([ec924f82/0'/0'/5']031e0fc9a03e69326c3deeabfd749a7f7b094e3151ada90cd13019efac663c5663)#dj7rhpdt",
    "safe": true
  },
  {
    "txid": "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f",
    "vout": 1,
    "address": "tb1qyd537gf0xmm9ehmhaf3nv0a230crg56mhp9ap3",
    "scriptPubKey": "001423691f212f36f65cdf77ea63363faa8bf034535b",
    "amount": 0.02877504,
    "confirmations": 189184,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([ec924f82/0'/1'/0']03ae333417e86840145e95ab2852c8f7ca8b8f82cd910883f7ce0c69649403cef2)#jlcj23vw",
    "safe": true
  }
]
```

Antes de continuar, necesitamos hablar sobre los outpoints, una transacción única puede incluir múltiples salidas, el outpoint incluye tanto un TXID de 32 bytes como un número de índice de salida de 4 bytes (vout) para referirse a una salida específica separada por dos puntos :. En nuestra salida de listunspent podemos encontrar dos UTXOs, en cada uno podemos ver txid y vout, esos son los outpoints de issuance_utxo y change_utxo.
'receive_utxo' es un UTXO controlado por el receptor, en este caso usaremos e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 que es un outpoint de otra billetera.

- issuance_utxo: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- receive_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Ahora vamos a crear una transacción parcialmente firmada (tx.psbt) cuya salida se ajustará para incluir una transferencia comprometida, recuerda reemplazar el txid y vout con los tuyos, la dirección de destino no importa realmente, puede ser tuya o puede ser de otra persona, no importa a dónde vayan esos sats, lo que importa es que usemos issuance_utxo.

```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
  "psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
  "fee": 0.00000280,
  "changepos": 0'
```

El resultado nos dio un psbt en codificación base64 que usaremos para crear tx.psbt.

```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt
```

Creemos un nuevo directorio llamado rgbdata en el cual se almacenarán los directorios de datos de cada nodo.

```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```

Ya ubicados en $HOME/rgbdata, iniciamos cada nodo en diferentes terminales, donde ~/.cargo/bin es el directorio donde cargo copió todos los binarios después de la instalación de rgb-node.

```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```

### Emisión

Para emitir un activo, ejecutamos rgb0-cli con los subcomandos de emisión fungible, luego los argumentos, el ticker USDT, el nombre "USD Tether" y en la asignación usaremos la cantidad de emisión y el issuance_utxo como se muestra a continuación:

```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```

Activo emitido exitosamente. Utilice esta información para compartir:
Información del activo:

```
'genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
  - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    amount: 1000
    origin: ~
knownInflation: {}
knownAllocations:
  - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    index: 0
    outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
    revealedAmount:
      value: 1000
      blinding: "0000000000000000000000000000000000000000000000000000000000000001"'
```

Obtenemos el assetId, lo necesitamos para transferir el activo.

```
$ rgb0-cli fungible list

- name: USD Tether
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
```

### Generar UTXO cegado

Para recibir el nuevo USDT, rgb-node-1 necesita generar un UTXO cegado correspondiente a receive_utxo para mantener el activo.

```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Blinded outpoint: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Outpoint blinding secret: 1679197189805229975
```

Para poder aceptar transferencias relacionadas con este UTXO, necesitaremos el receive_utxo original y el blinding_factor.

### Transferencia

Para transferir una cierta cantidad del activo a rgb-node-1, necesitamos enviarlo al UTXO cegado, rgb-node-0 necesita crear un consignment y una disclosure, y comprometerlo en una transacción de bitcoin. Luego necesitaremos un psbt que modificaremos para incluir el compromiso. Además, las opciones -i y -a nos permiten proporcionar un outpoint de entrada que sería el origen del activo y una asignación donde recibiremos el cambio, debemos indicarlo de la siguiente manera @<change_utxo>.

```
'$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
La transferencia se realizó correctamente, los envíos y la divulgación se escriben en "consignment.rgb" y "disclosure.rgb", la transacción de testigo parcialmente firmada en "witness.psbt"'
Datos de consignación para compartir: consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e'
```

Esto escribirá tres archivos nuevos, consignment, disclosure y el psbt que incluye el ajuste, este psbt se llama transacción de testigo, el consignment se envía a rgb-node-1.

### Testigo

La transacción de testigo debe ser firmada y transmitida, para esto necesitamos codificarla nuevamente en base64.

```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```

Fírmalo con el subcomando walletprocesspsbt.

```
`$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="{'`

`$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="{'`


'"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",  "complete": true
}
```

Ahora finalízalo y obtén el hexadecimal.

```
'$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="{
  "hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
  "complete": true
}
```

### Transmitir

Transmítelo usando el subcomando sendrawtransaction para que se confirme en la cadena de bloques.

### Aceptar

Para aceptar una transferencia entrante, rgb-node-1 debe haber recibido el archivo de consignación de rgb-node-0, tener el receive_utxo y el blinding_factor correspondiente generado durante la generación de UTXO con cegamiento.

```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

Transferencia de activos aceptada exitosamente.
```

Ahora podemos ver (en el campo knownAllocations) la nueva asignación de 100 unidades de activos en <receive_utxo> ejecutando:

```
$ rgb1-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT'
name: USD Tether
description: ~
circulación conocida: 1000
se emitió conocido: ~
límite de emisión: 0
cadena: testnet
precisión decimal: 0
fecha: "2022-02-23T20:53:26"
problemas conocidos:
  - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    cantidad: 1000
    origen: ~
inflación conocida: {}
asignaciones conocidas:
  - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    índice: 0
    outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
    cantidad revelada:
      valor: 1000
      cegamiento: "0000000000000000000000000000000000000000000000000000000000000001"
  - nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
    índice: 1
    outpoint: "e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0"
    cantidad revelada:
      valor: 100
      cegamiento: 224561f10229eb9ebbdf05f497132d2b8344d70971c80510eddc607d615ee2a0
```

Dado que receive_utxo estaba cegado cuando se realizó la transferencia, el pagador rgb-node-0 no tiene información sobre dónde se envió el USDT de 100, por lo que la ubicación no se muestra en las asignaciones conocidas.

````
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
'id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6  ticker: USDT\n  name: USD Tether\n  description: ~\n  knownCirculating: 1000\n  isIssuedKnown: ~\n  issueLimit: 0\n  chain: testnet\n  decimalPrecision: 0\n  date: "2022-02-23T20:53:26"\n  knownIssues:\n    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f\n      amount: 1000\n      origin: ~\n  knownInflation: {}\n  knownAllocations:\n    - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f\n      index: 0\n      outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"\n      revealedAmount:\n        value: 1000\n        blinding: "0000000000000000000000000000000000000000000000000000000000000001"\n\nPero como puedes ver, rgb-node-0 no puede ver el cambio de 900 activos que proporcionamos al comando de transferencia con el argumento -a. Para registrar el cambio, rgb-node-0 necesita aceptar la divulgación.\n\n```\n$ rgb0-cli fungible enclose disclosure.rgb\n\nDatos de divulgación cerrados con éxito.\n```\n\nSi rgb-node-0 tuvo éxito, puedes ver el cambio al listar el activo.\n\n```\n$ rgb0-cli fungible list -l\n\n- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0\n  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6\n  ticker: USDT\n  name: USD Tether'
'description: ~  knownCirculating: 1000
  isIssuedKnown: ~
  issueLimit: 0
  chain: testnet
  decimalPrecision: 0
  date: "2022-02-23T20:53:26"
  knownIssues:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      amount: 1000
      origin: ~
  knownInflation: {}
  knownAllocations:
    - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      index: 0
      outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      revealedAmount:
        value: 1000
        blinding: "0000000000000000000000000000000000000000000000000000000000000001"
    - nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
      index: 0
      outpoint: "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1"
      revealedAmount:
        value: 900
        blinding: ddba9e0efdd614614420fa0b68ecd2d3376a05dd3d809b2ad1f5fe0f6ed75ea2
````

### Conclusiones

Hemos podido crear un activo fungible y moverlo de una transacción a otra de manera privada, si verificamos la transacción confirmada en un explorador de bloques no encontraríamos nada diferente de una transacción regular, esto se debe a que RGB utiliza sellos de un solo uso para ajustar las transacciones. En esta publicación, hago una introducción a cómo funciona RGB.

Esta publicación puede tener errores, si encuentras algo, por favor avísame para mejorar esta guía, también se aceptan sugerencias y críticas, ¡feliz hacking! 🖖
