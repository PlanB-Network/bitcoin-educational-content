---
name: Bitcoin Knots
description: ¿Cómo correr un nodo con el cliente alternativo Bitcoin Knots?
---
![cover](assets/cover.webp)

Bitcoin Knots es una implementación alternativa del protocolo Bitcoin, derivado de Bitcoin Core. Diseñado y mantenido por Luke Dashjr, ofrece algunas características adicionales y ajustes de reglas de Mempool, sin dejar de ser compatible con otros nodos de la red. Bitcoin Knots integra una billetera Bitcoin, aunque también puede ser usado como un simple nodo Bitcoin y conectar una billetera compatible.

## ¿Por qué utilizar Knots en lugar de Core?

Actualmente, Core es la implementación mayoritaria del protocolo Bitcoin en la red. El protocolo Bitcoin es sólo un conjunto de reglas. Requiere un software que las aplique. Una máquina que ejecuta el software de el protocolo Bitcoin se llama nodo, y todos estos nodos juntos forman la red Bitcoin.

A lo largo de la historia de Bitcoin, han surgido numerosos clientes derivados del software inicial desarrollado por Satoshi Nakamoto. En la actualidad (Junio de 2025), Bitcoin Core es la abrumadora mayoría, con casi el 88% de los nodos de la red Bitcoin utilizando este cliente.

Sin embargo, también existe software alternativo. No se trata de nodos vinculados a Altcoins como Bitcoin Cash, sino de clientes alternativos compatibles con la red Bitcoin real. De ellos, Bitcoin Knots es el más conocido. Actualmente representa alrededor del 11,7% de la red. Otros clientes alternativos siguen siendo muy minoritarios.

![Image](assets/fr/01.webp)

Hay dos razones principales para utilizar un cliente alternativo como Knots en lugar de Core:


- **Técnico**: Estos clientes suelen ofrecer diferentes opciones a Core, sobre todo en términos de gestión de Mempool, determinando qué transacciones son aceptadas y difundidas por su nodo.
- **Política**: Algunas personas prefieren utilizar clientes alternativos como Knots por razones no técnicas, en particular para apoyar una alternativa a Core y reducir así su monopolio. Si alguna vez Core se viera comprometido, sería útil no sólo disponer de clientes alternativos sólidos y bien mantenidos, sino también saber cómo utilizarlos. Otros utilizan Bitcoin Knots con fines de protesta, porque han perdido la confianza en los desarrolladores de Core o desaprueban la gestión del cliente mayoritario.

## ¿Cómo instalar Bitcoin Knots?

Visita [el sitio web oficial de Bitcoin Knots](https://bitcoinknots.org/#download) para descargar la versión para tu sistema operativo. No olvides descargar la huella digital y las firmas para verificar el software. Estos archivos también están disponibles [en el repositorio GitHub de Bitcoin Knots](https://github.com/bitcoinknots/Bitcoin).

![Image](assets/fr/02.webp)

Antes de instalar el software en tu máquina, te recomendamos encarecidamente que compruebes su autenticidad e integridad. Si no sabes cómo, echa un vistazo a este otro tutorial:

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Una vez verificado el software, instálalo siguiendo los pasos indicados en el panel de instalación.

![Image](assets/fr/03.webp)

## Abrir IBD

La primera vez que inicies Bitcoin Knots, podrás elegir el directorio local donde se almacenarán los datos de tus nodos (incluyendo Blockchain, UTXO set y parámetros).

![Image](assets/fr/04.webp)

También puedes elegir podar los datos de de la red para conservar sólo los bloques más recientes. Esta opción permite que tu nodo compruebe cada bloque en su totalidad dentro de un límite de almacenamiento establecido, eliminando así gradualmente los bloques más antiguos. Si dispones de suficiente espacio en disco (actualmente unos 650 GB, pero esta cifra va en aumento), deja esta opción sin marcar. Si tu espacio en disco es limitado, activa la poda y especifíca la capacidad máxima permitida.

Nota: Si tu nodo está podado y lo utilizas para sincronizar una billetera recuperada, no podrás recuperar transacciones anteriores al bloque más antiguo almacenado localmente.

![Image](assets/fr/05.webp)

Otra opción disponible es "*Asumir válido*". Acelera la sincronización inicial al omitir la verificación de firma de las transacciones incluidas en bloques anteriores a un bloque específico.

El objetivo de "*Asumir Válido*" es acelerar la primera sincronización del nodo sin reducir significativamente la seguridad, asumiendo que estas transacciones ya han sido validadas masivamente por la red de antemano. El único compromiso importante es que tu nodo no detectará ningún robo previo de Bitcoin, pero seguirá garantizando la exactitud del número total de bitcoins emitidos. Tu nodo verificará todas las firmas de transacciones después del bloque especificado. Este enfoque se basa en la suposición de que una transacción que ha sido aceptada por la red durante mucho tiempo sin impugnación es muy probablemente válida.

Por ejemplo, aquí, "*Assume Valid*" se establece en el bloque nº. 855 000 `00000000000000000000000233ea80aa10d38aa4486cd7033fffc2c4df556d0b9138`, publicado el 1 de agosto de 2024. Por lo tanto, durante el IBD, mi nodo sólo iniciará la verificación completa de la firma a partir de este bloque.

![Image](assets/fr/06.webp)

A continuación, haz clic en el botón "*OK*" para iniciar la *Descarga inicial de bloques*. Tendrás que ser paciente durante la sincronización inicial de tu nodo. Si deseas reanudar la sincronización más tarde, sólo tienes que cerrar el software y apagar el ordenador. La sincronización se reanudará sin problemas la próxima vez que abras el programa.

![Image](assets/fr/07.webp)

## Configuración de Bitcoin Knots

Haz clic en la pestaña "*Configuración*" y selecciona "*Opciones*".

![Image](assets/fr/08.webp)

En la pestaña "*Main*" se accede a los parámetros principales del nodo:


- "*Iniciar...*" inicia automáticamente el nodo al arrancar el ordenador para comenzar la sincronización inmediatamente;
- "*Prune...*" ajusta el límite de almacenamiento si has elegido podar la red para reducir el espacio en tu disco;
- "*Caché de base de datos...*" establece la cantidad máxima de RAM permitida a tu nodo;
- Por último, active "*Habilitar servidor RPC*" si deseas conectar tu nodo Bitcoin Knots a otro software de billetera, como Sparrow Wallet o Liana, por ejemplo.

![Image](assets/fr/09.webp)

En la pestaña "*Wallet*" encontrarás la configuración de la billetera integrada que podrás crear más adelante en Knots. Te recomendamos que actives RBF y el control de monedas. También puedes definir el tipo de script a utilizar.

![Image](assets/fr/10.webp)

La pestaña "*Network*" contiene parámetros de red que puedes adaptar a tus necesidades específicas.

![Image](assets/fr/11.webp)

La pestaña "*Mempool*" permite configurar el *Memory Pool*, es decir, la gestión de las transacciones no confirmadas almacenadas en memoria, y el tamaño máximo asignado a esta funcionalidad (300 MB por defecto).

![Image](assets/fr/12.webp)

La pestaña "Spam filtering" es una función de Bitcoin Knots. Aquí encontrarás una serie de ajustes que te permitirán elegir qué transacciones aceptará o rechazará transmitir. El objetivo principal es limitar ciertos usos marginales de Bitcoin, en particular los metaprotocolos, para luchar contra estas prácticas evitando al mismo tiempo sobrecargar tu nodo. Es una elección política, dependiendo de tu visión personal de Bitcoin.

También encontrarás parámetros clásicos como la definición del umbral "*Dust*".

Sin embargo, estos parámetros sólo influyen en las reglas de normalización. Tu nodo seguirá aceptando transacciones no confirmadas sólo cuando estén incluidas en un bloque, para seguir siendo compatible con el resto de la red Bitcoin. Estos parámetros sólo modifican la forma en que tu nodo procesa y distribuye las transacciones no confirmadas a sus pares. En la práctica, como Knots es minoritario, son las reglas establecidas por defecto en Bitcoin Core las que definen la estandarización en la red.

![Image](assets/fr/13.webp)

La pestaña "*Mining*" le permite configurar la posible participación de tu nodo en la minería, si deseas activar esta función.

![Image](assets/fr/14.webp)

Por último, la pestaña "*Window*" se refiere a los parámetros relativos a los gráficos de Interface, incluido el idioma del software.

![Image](assets/fr/15.webp)

## Crear una billetera Bitcoin

Una vez completada la sincronización inicial, tu nodo de Bitcoin Knots es totalmente funcional. Ahora tienes la opción de conectar este nodo a otro software de billetera, o utilizar directamente la "Hot Wallet" incorporada. Para ello, haz clic en el botón "*Crear una nueva Wallet*".

![Image](assets/fr/16.webp)

Dale un nombre a tu billetera. También puedes protegerla con un BIP39 de passphrase haciendo clic en "*Encriptar Wallet*". Una vez listo, haz clic en el botón "*Crear*".

![Image](assets/fr/17.webp)

La passphrase BIP39 es una contraseña opcional que puedes elegir libremente, además de tu frase Mnemonic, para aumentar la seguridad de tu billetera. Antes de configurar esta característica, te recomendamos encarecidamente leer el siguiente artículo, que explica en detalle cómo funciona en teoría la passphrase, y cómo evitar errores que podrían conducir a la pérdida permanente de tu Bitcoin:

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Si has activado la opción passphrase, elige una robusta y guárdala cuidadosamente en uno o varios soportes físicos seguros.

![Image](assets/fr/18.webp)

Tu billetera Bitcoin ya está creada.

![Image](assets/fr/19.webp)

## Copia de seguridad de tu billetera Bitcoin

Incluso antes de recibir tu primer Bitcoin, es esencial hacer una copia de seguridad de tu billetera para poder recuperar tus fondos en caso de pérdida o fallo informático. Para ello, haz clic en la pestaña "*Archivo*" y luego en "*Copia de seguridad Wallet*".

![Image](assets/fr/20.webp)

Esta operación genera un único archivo que puede ser utilizado para restaurar todos tu Bitcoin. Así que ten mucho cuidado y guárdalo en un medio externo seguro.

## Recibir Bitcoin

Para recibir Bitcoin directamente en tu billetera de Knots, haz clic en el botón "*Recibir*".

![Image](assets/fr/21.webp)

Asigna una "*etiqueta*" a tu dirección para identificar fácilmente su finalidad y facilitar el uso futuro de *Coin Control*. También puedes definir de antemano una cantidad precisa a recibir en esta dirección, o añadir un mensaje para el pagador. Una vez establecidos los parámetros, haz clic en "*Solicitar pago*".

![Image](assets/fr/22.webp)

Bitcoin Knots muestra entonces una dirección de recepción, que puedes copiar o escanear y enviar al pagador.

![Image](assets/fr/23.webp)

Una vez emitida una transacción, puedes seguir su estado directamente en el menú "*Transacciones*".

![Image](assets/fr/24.webp)

## Enviar Bitcoin

Ahora que tienes Bitcoin en tu billetera Knots, puedes realizar envíos. Para ello, haz clic en el botón "*Enviar*".

![Image](assets/fr/25.webp)

Pulsa el botón "*Inputs...*" para seleccionar los UTXO exactos que deseas enviar en esta transacción.

![Image](assets/fr/26.webp)

Introduce la dirección Bitcoin del destinatario.

![Image](assets/fr/27.webp)

Añade una etiqueta para recordar el propósito de esta transacción.

![Image](assets/fr/28.webp)

Introduce el importe que deseas enviar a esta dirección.

![Image](assets/fr/29.webp)

Haz clic en el botón "*Elegir...*" para seleccionar la tarifa adecuada para su transacción, en función del estado actual de la red.

![Image](assets/fr/30.webp)

Si todo es de tu agrado, pulsa el botón "*Enviar*". Si utilizas un passphrase, se te pedirá que lo introduzcas en esta fase.

![Image](assets/fr/31.webp)

Comprueba los parámetros de la transacción una última vez y, si todo es correcto, pulsa de nuevo el botón "*Enviar*" para firmar y distribuir tu transacción.

![Image](assets/fr/32.webp)

Tu transacción pendiente de confirmación aparece ahora en la pestaña "*Transacciones*".

![Image](assets/fr/33.webp)

## Conectar el nodo a otro programa

Bitcoin Knots integrado para gestionar tu cartera Bitcoin no es necesariamente el más intuitivo, y su funcionalidad sigue siendo relativamente limitada. Sin embargo, puedes conectar tu nodo Bitcoin Knots a un software especializado de gestión de carteras para acceder fácilmente a los datos de Blockchain Bitcoin y difundir sus transacciones.

El procedimiento dependerá del software utilizado, pero hay dos escenarios principales: o bien Bitcoin Knots se instala en el mismo ordenador que el software de tu cartera, o bien se ejecuta en una máquina independiente.

### Con Bitcoin Knots local:

Si Bitcoin Knots está instalado en tu ordenador, localiza el archivo `Bitcoin.conf` entre los archivos de software. Si este archivo no existe, puedes crearlo. Ábrelo con un editor de texto e inserta la siguiente línea:

```ini
server=1
```

A continuación, guarda los cambios.

También puedes hacerlo a través de la Interface gráfica de Bitcoin-QT navegando a "*Configuración*" > "*Opciones...*" y activando la opción "*Habilitar servidor RPC*".

No olvides reiniciar el programa después de realizar estos cambios.

![Image](assets/fr/34.webp)

A continuación, ve a tu software de gestión de carteras (por ejemplo, Sparrow Wallet o Liana) e introduce la ruta a tu archivo cookie, normalmente ubicado en la misma carpeta que el `Bitcoin.conf`, dependiendo de tu sistema operativo:

|**macOS**|~/Library/Application Support/Bitcoin|
|---|---|
|**Windows**|%APPDATA%\Bitcoin|
|**Linux**|~/.bitcoin|

![Image](assets/fr/35.webp)

Deja los demás parámetros por defecto, URL `127.0.0.1` y puerto `8332`, y haz clic en "*Test Connection*".

![Image](assets/fr/36.webp)

### Con Bitcoin Knots en remoto:

Si Bitcoin Knots está instalado en otra máquina conectada a la misma red, localiza primero el archivo `Bitcoin.conf` entre los archivos de software. Si este archivo aún no existe, puedes crearlo. Abre este archivo con un editor de texto y añade la siguiente línea:

```ini
server=1
```

Después de editar el archivo, asegúrate de guardarlo en la carpeta adecuada para tu sistema operativo:

|**macOS**|~/Library/Application Support/Bitcoin|
|---|---|
|**Windows**|%APPDATA%\Bitcoin|
|**Linux**|~/.bitcoin|

Esta operación también puede realizarse a través de la Interface gráfica de Bitcoin-QT. Ve al menú "*Configuración*", luego a "*Opciones...*", y activa la opción "*Habilitar servidor RPC*" marcando la casilla correspondiente. Si el archivo `Bitcoin.conf` no existe, puedes crearlo directamente desde ésta Interface pulsando "*Abrir archivo de configuración*".

![Image](assets/fr/37.webp)

Encuentra la dirección IP de la máquina que aloja Bitcoin Knots en tu red local. Para ello, puedes utilizar una herramienta como [Angry IP Scanner](https://angryip.org/). Supongamos que la dirección IP de tu nodo es `192.168.1.18`.

En el archivo `Bitcoin.conf`, añade las siguientes líneas, configurando `rpcbind=192.168.1.18` para que coincida con la dirección IP de tu nodo.

```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```

![Image](assets/fr/38.webp)

Añade también un nombre de usuario y una contraseña para conexiones remotas al archivo `Bitcoin.conf`. Asegúrate de reemplazar `loic` con tu nombre de usuario y `my_password` con una contraseña segura:

```ini
rpcuser=loic
rpcpassword=my_password
```

![Image](assets/fr/39.webp)

Después de modificar y guardar el archivo, reinicia Bitcoin Knots.

Ahora puedes ir a su software de gestión de billeteras (por ejemplo, Sparrow Wallet o Liana). En Sparrow, ve a la pestaña "*User / Pass*". Introduce el nombre de usuario y la contraseña que has configurado en el archivo `Bitcoin.conf`. Deja el resto de parámetros por defecto, es decir, URL "127.0.0.1" y puerto "8332". A continuación, haz clic en "*Probar conexión*".

![Image](assets/fr/40.webp)

Se establece la conexión.

Ahora ya lo sabes todo sobre la implementación alternativa de Bitcoin Knots.

Si este tutorial te ha resultado útil, te agradeceríamos que dejaras un Me gusta en verde a continuación. No dudes en compartirlo en tus redes sociales. Muchas gracias!

También te recomendamos este otro tutorial en el que explicamos cómo configurar tu propio nodo Lightning:

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a
