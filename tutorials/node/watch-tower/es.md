---
name: Lightning Watchtower
description: Comprender y utilizar una Watchtower en su nodo Lightning
---
![cover](assets/cover.webp)



## ¿Cómo funcionan las Atalayas?



Parte esencial del ecosistema de Lightning Network, las _Watchtowers_ proporcionan un nivel extra de protección a los canales Lightning de los usuarios. Su función principal es supervisar el estado del canal e intervenir si una de las partes intenta estafar a la otra.



¿Cómo puede una Watchtower determinar si un canal se ha visto comprometido? Recibe del cliente (una de las partes del canal) la información necesaria para identificar y tratar correctamente cualquier infracción. Esta información incluye detalles de la transacción más reciente, el estado actual del canal y el Elements necesario para crear transacciones de penalización. Antes de transmitir estos datos a Watchtower, el cliente puede cifrarlos para preservar la confidencialidad. Así, aunque Watchtower reciba los datos, no podrá descifrarlos hasta que se haya producido realmente una infracción. Este mecanismo de cifrado protege la intimidad del cliente e impide que Watchtower acceda sin autorización a información sensible.



En este tutorial, veremos 3 formas de utilizar un **Watchtower** :




- primero, el método clásico en bruto a través de LND,
- luego otra aproximación con Ojo de Satoshi,
- y, por último, la configuración simplificada de un Watchtower en su nodo Lightning alojado con Umbrel.



## 1 - Configuración de un Watchtower o de un cliente a través de LND



*Este tutorial está tomado de [la documentación oficial de LND](https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md). Es posible que se hayan realizado algunos cambios en la versión original



Desde la v0.7.0, `LND` soporta la ejecución de una Watchtower altruista privada como subsistema totalmente integrado de `LND`. Las torres de vigilancia proporcionan una segunda línea de defensa contra escenarios de violación maliciosos o accidentales cuando el nodo cliente está fuera de línea o es incapaz de responder en el momento de la violación, ofreciendo un mayor grado de seguridad para los fondos del canal.



A diferencia de una _torre de vigilancia de recompensa_, que exige una parte de los fondos del canal a cambio de su servicio, una _torre de vigilancia altruista_ devuelve todos los fondos de la víctima (menos las tasas de On-Chain) sin cobrar comisión. Las atalayas de recompensa se activarán en una versión posterior; aún están en fase de pruebas y mejoras.



Además, `LND` puede configurarse ahora para funcionar como _cliente de atalaya_, guardando transacciones cifradas de reparación de infracciones (las llamadas "transacciones de justicia") de otras atalayas altruistas. La Watchtower almacena blobs encriptados de tamaño fijo y sólo puede desencriptar y publicar la transacción de justicia después de que la parte infractora haya emitido un estado Commitment revocado. Las comunicaciones cliente ↔ Watchtower se cifran y autentican mediante pares de claves efímeras, lo que limita la capacidad de Watchtower para rastrear a sus clientes mediante credenciales a largo plazo.



Tenga en cuenta que hemos optado por desplegar en esta versión un conjunto limitado de funciones que ya proporcionan una seguridad significativa a los usuarios de `LND`. Muchas otras funciones relacionadas con Watchtower están a punto de completarse o muy avanzadas; seguiremos ofreciéndolas a medida que las probemos, y tan pronto como se consideren seguras.



nota: por el momento, las torres de vigilancia sólo guardan la salida `to_local` y `to_remote` de los compromisos revocados; guardar la salida HTLC se implementará en una versión futura, ya que el protocolo puede ampliarse para incluir datos de firma adicionales en blobs cifrados._



### Configuración de un Watchtower



Para configurar una Watchtower, los usuarios de la línea de comandos deben compilar el subservidor opcional `watchtowerrpc`, que permite interactuar con la Watchtower a través de gRPC o `lncli`. Los binarios publicados incluyen el subservidor `watchtowerrpc` por defecto.



La configuración mínima para activar Watchtower es `Watchtower.active=1`.



Puede recuperar la información de configuración de su Watchtower con `lncli tower info` :



```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```



El conjunto completo de opciones de configuración de Watchtower está disponible a través de `LND -h` :



```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```



#### Interfaces de escucha



Por defecto, Watchtower escucha en `:9911`, que corresponde al puerto `9911` en todas las interfaces disponibles. Los usuarios pueden definir sus propias interfaces de escucha mediante la opción `--Watchtower.listen=`. Puede comprobar su configuración en el campo `"listeners"` de `lncli tower info`. Si tiene problemas para conectarse a su Watchtower, asegúrese de que el `<port>` está abierto o que su proxy está correctamente configurado para una Interface activa.



#### Direcciones IP externas



Los usuarios también pueden especificar la IP externa de Watchtower Address(es) con `Watchtower.externalip=`, que expone el URI completo de Watchtower (pubkey@host:port) a través de RPC o `lncli tower info` :



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



Las URI de Watchtower pueden comunicarse a los clientes para que se conecten y las utilicen con el siguiente comando:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Si los clientes de Watchtower necesitan acceder a ella a distancia, asegúrese de :




- Abra el puerto 9911 (o un puerto definido mediante `Watchtower.listen`).
- Utilice un proxy para redirigir el tráfico de un puerto abierto al Watchtower de escucha.



#### Servicios ocultos de Tor



Watchtowers soporta los servicios ocultos Tor y puede automáticamente generate uno al inicio con las siguientes opciones:



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



El .onion Address aparece entonces en el campo `"uris"` durante una consulta `lncli tower info`:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



nota: la clave pública de Watchtower es distinta de la clave pública del nodo `LND`. Por el momento, actúa como una "lista blanca de Soft", ya que los clientes necesitan conocer la clave pública de Watchtower para utilizarla como copia de seguridad, a la espera de mecanismos de lista blanca más avanzados. Recomendamos NO revelar esta clave pública abiertamente, a menos que esté preparado para exponer su Watchtower a todo Internet._



#### Directorio de la base de datos Watchtower



La base de datos Watchtower puede moverse utilizando la opción `Watchtower.towerdir=`. Tenga en cuenta que se añadirá un sufijo `/Bitcoin/Mainnet/Watchtower.db` a la ruta elegida para aislar las bases de datos por cadena. Así, si se define `Watchtower.towerdir=/path/to/towerdir`, se creará una base de datos en `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`.



En Linux, por ejemplo, la base de datos por defecto de Watchtower se encuentra en :


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### Configuración de un cliente Watchtower



Para configurar un cliente Watchtower, necesita dos elementos:





- Active el cliente Watchtower con la opción `--wtclient.active`.



```shell
$  lnd --wtclient.active
```





- URI de un Watchtower activo.



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Puede configurar varias torres de vigilancia de este modo.



#### Tarifas de las operaciones jurídicas



Los usuarios pueden establecer opcionalmente la tarifa de las transacciones de justicia mediante la opción `wtclient.sweep-fee-rate`, que acepta valores en sat/byte. El valor por defecto es 10 sat/byte, pero es posible aspirar a tasas más altas para conseguir una mayor prioridad durante los picos de carga. El cambio de `sweep-fee-rate` se aplica a todas las nuevas actualizaciones tras el reinicio de daemon.



#### Supervisión



Con el comando `lncli wtclient`, los usuarios pueden ahora interactuar directamente con el cliente Watchtower para obtener o modificar información sobre todas las torres de vigilancia registradas.



Por ejemplo, con `lncli wtclient tower`, puede averiguar el número de sesiones negociadas actualmente con el Watchtower añadido anteriormente y determinar si se está utilizando para copias de seguridad gracias al campo `active_session_candidate`.



```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```



Para obtener información sobre las sesiones de Watchtower, utilice la opción `--include_sessions`.



```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```



Todas las opciones de configuración del cliente Watchtower están disponibles a través de `lncli wtclient -h` :



```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```




## 2 - Instalación de su propio Ojo de Satoshi



*Este tutorial está extraído en parte de un artículo del [Blog Summer of Bitcoin](https://blog.summerofbitcoin.org/). Se han hecho modificaciones a la versión original*



El Ojo de Satoshi ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos)) es un Watchtower Lightning no depositario, conforme a [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Consta de dos componentes principales:





- teos**: incluye un Interface de línea de comandos (CLI) y las características esenciales de servidor de Watchtower. Se producen dos binarios - **teosd** y **teos-CLI** - cuando se compila este _crate_.





- teos-common**: incluye funcionalidad compartida del lado del servidor y del lado del cliente (útil para crear un cliente).



Para ejecutar Watchtower correctamente, necesita ejecutar **bitcoind** antes de lanzar Watchtower con el comando **teosd**. Antes de ejecutar estos dos comandos, necesitas configurar tu archivo **Bitcoin.conf**. He aquí cómo hacerlo:





- Instale Bitcoin core desde el código fuente o descárguelo. Después de descargarlo, coloque el archivo **Bitcoin.conf** en el directorio de usuario de Bitcoin core. Consulte este enlace para obtener más información sobre dónde colocar el archivo, ya que esto depende del sistema operativo utilizado.





- Una vez identificada la ubicación, añada las siguientes opciones:



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- servidor**: para solicitudes RPC





- rpcuser** y **rpcpassword**: autenticar clientes RPC en el servidor





- regtest**: no es necesario, pero es útil si está planeando el desarrollo.



Los valores de **rpcuser** y **rpcpassword** los eliges tú. Deben escribirse sin comillas. Por ejemplo:



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



Ahora, si ejecutas **bitcoind**, el nodo debería arrancar.





- Para la parte Watchtower, primero debes instalar **teos** desde el código fuente. Siga las instrucciones dadas en este enlace.





- Una vez que hayas instalado correctamente **teos** en tu sistema y realizado las pruebas, puedes pasar al último paso: configurar el archivo **teos.toml** en el directorio de usuario de teos. El archivo debe colocarse en una carpeta llamada **.teos** (nótese el punto) bajo tu directorio personal. Por ejemplo, **/home//.teos** en Linux. Una vez encontrada la ubicación, cree un archivo **teos.toml** y configure estas opciones de acuerdo con los cambios realizados en **bitcoind** :



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



Tenga en cuenta que aquí, el nombre de usuario y la contraseña deben escribirse **entre comillas**. Utilizando el ejemplo anterior :



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



Una vez hecho esto, debería estar listo para iniciar la Watchtower. Dado que estamos ejecutando **regtest**, es probable que no haya bloques minados en nuestra red de prueba Bitcoin cuando Watchtower se conecte por primera vez (si los hay, algo va mal). Watchtower construye una caché interna de los últimos 100 bloques de **bitcoind**; por lo que, en el primer lanzamiento, es posible que obtenga el siguiente error:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



Dado que estamos utilizando **regtest**, podemos Miner bloques mediante la emisión de un comando RPC, sin tener que esperar a que el retraso medio de 10 minutos visto en otras redes (como Mainnet o Testnet). Consulta la ayuda de **bitcoin-cli** para obtener más información sobre cómo realizar bloqueos Miner.



![Image](assets/fr/01.webp)



Eso es todo: has ejecutado con éxito el Watchtower. Enhorabuena. 🎉




## 3 - Configuración de un Watchtower en Umbrel



En Umbrel, conectarse a una Watchtower para proteger tu nodo Lightning es extremadamente sencillo, ya que todo se hace a través de la Interface gráfica. Tras conectarte remotamente a tu nodo, abre la aplicación "**Nodo Lightning**".



![Image](assets/fr/02.webp)



Haz clic en los tres puntitos de la parte superior derecha del Interface y selecciona "**Configuración avanzada**".



![Image](assets/fr/03.webp)



En el menú "**Watchtower**" hay dos opciones disponibles:





- Servicio Watchtower**: esta opción te permite operar un Watchtower, es decir, un servicio que monitoriza los canales de otros nodos para detectar cualquier intento de fraude. En caso de infracción, su Watchtower publica una transacción en el Blockchain, lo que permite a los usuarios recuperar sus fondos bloqueados. Una vez activado, aparece el URI de su Watchtower y puede comunicarse a otros nodos para que lo añadan a su cliente Watchtower;





- Cliente Watchtower**: esta opción le permite conectarse a torres de vigilancia externas para proteger sus propios canales. Una vez activada, podrá añadir servicios Watchtower a los que su nodo transmitirá la información necesaria sobre sus canales. Estas torres de vigilancia controlarán entonces su estado e intervendrán en caso de intento de fraude.



La prioridad para ti es, por supuesto, activar el *Cliente Watchtower* para proteger tu nodo, pero también te recomiendo que actives el *Servicio Watchtower* para contribuir a cambio a la seguridad de otros usuarios.



![Image](assets/fr/04.webp)



A continuación, haga clic en el botón "**Guardar y reiniciar nodo**" de Green. Su LND se reiniciará.



En el mismo menú, también encontrará el URI de su servicio Watchtower si lo ha activado. También puede añadir el URI de un Watchtower externo para proteger sus canales. Haga clic en "**ADD**" para confirmar.



![Image](assets/fr/05.webp)



Hay varias Atalayas disponibles en línea. Por ejemplo, [LN+ y Voltage ofrecen una Watchtower altruista](https://lightningnetwork.plus/Watchtower) a la que puedes conectarte:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



Otra opción es Exchange su Watchtower URI con sus compañeros bitcoiners, para que cada uno proteja el nodo del otro.



También te recomiendo que instales varias Atalayas para reducir los riesgos en caso de que una de ellas deje de estar disponible.



Por último, puede ajustar el parámetro "**Tasa de comisión por barrido de clientes Watchtower**". Define la tasa máxima que está dispuesto a pagar para que una transacción de castigo por emisión Watchtower se incluya en un bloque. Asegúrese de establecer un valor suficientemente alto, adaptado a las cantidades bloqueadas en sus canales.