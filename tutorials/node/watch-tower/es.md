---
name: Watch Tower
description: Comprender y utilizar una torre de vigilancia
---

## ¿Cómo funcionan las torres de vigilancia?

Parte esencial del ecosistema de la Lightning Network, las torres de vigilancia brindan un grado adicional de protección a los canales de rayos de los usuarios. Su principal responsabilidad es vigilar la salud de los canales e intervenir si una de las partes del canal intenta defraudar a la otra.

Entonces, ¿cómo puede una torre de vigilancia determinar si un canal ha sido comprometido? La torre de vigilancia recibe la información que necesita del cliente, una de las partes del canal, para identificar y responder adecuadamente a cualquier violación. Los detalles de la transacción más reciente, la condición actual del canal y la información necesaria para crear transacciones de penalización se incluyen con frecuencia en esta información. Antes de transmitir los datos a la torre de vigilancia, el cliente puede cifrarlos para proteger la privacidad y el secreto. Esto evita que la torre de vigilancia descifre los datos cifrados a menos que realmente se haya producido una violación, incluso si obtiene los datos. Este sistema de cifrado protege la privacidad del cliente y también impide que la torre de vigilancia acceda a datos privados sin autorización.

## Cómo configurar tu propio Ojo de Satoshi y comenzar a contribuir

El Ojo de Satoshi ([RUST-TEOS](https://github.com/talaia-labs/rust-teos?ref=blog.summerofbitcoin.org)) es una torre de vigilancia de Lightning no custodial compatible con [BOLT 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Tiene dos componentes principales:

1. teos: incluye una interfaz de línea de comandos (CLI) y la funcionalidad principal del lado del servidor de la torre. Se generarán dos binarios, teosd y teos-cli, al construir esta caja.

2. teos-common: incluye funcionalidad compartida del lado del servidor y del lado del cliente (útil para crear un cliente).

Para ejecutar la torre con éxito, necesitarás tener bitcoind en funcionamiento antes de ejecutar la torre con el comando teosd. Antes de ejecutar ambos comandos, debes configurar tu archivo bitcoin.conf. Aquí tienes los pasos sobre cómo hacerlo:

1. Instala Bitcoin Core desde la fuente o descárgalo. Después de descargarlo, coloca el archivo bitcoin.conf en el directorio de usuario de Bitcoin Core. Consulta este enlace para obtener más información sobre dónde colocar el archivo, ya que depende del sistema operativo que estés utilizando.

2. Después de identificar el lugar donde se debe crear el archivo, agrega estas opciones:

```
#RPC
server=1
rpcuser=<tu-usuario>
rpcpassword=<tu-contraseña>

#chain
regtest=1
```

- server: para solicitudes RPC
- rpcuser y rpcpassword: los clientes RPC pueden autenticarse con el servidor
- regtest: no es necesario, pero útil si estás planeando para desarrollo.

rpcuser y rpcpassword deben ser elegidos por ti. Deben escribirse sin comillas. Ejemplo:

```
rpcuser=aniketh
rpcpassword=strongpassword
```

Ahora, si ejecutas bitcoind, debería comenzar a ejecutar el nodo.

1. Para la parte de la torre, primero debes instalar teos desde la fuente. Sigue las instrucciones que se dan en este enlace.
2. Después de instalar teos correctamente en tu sistema y ejecutar las pruebas, puedes proceder con el último paso que es configurar el archivo teos.toml en el directorio de usuario de teos. El archivo debe colocarse en una carpeta llamada .teos (presta atención al punto) dentro de tu carpeta de inicio. Es decir, por ejemplo, /home/<tu-nombre-de-usuario>/.teos para Linux. Una vez que hayas encontrado el lugar, crea un archivo teos.toml y configura estas opciones correspondientes a las cosas que hemos cambiado en bitcoind.

```
#bitcoind
btc_network = "regtest"
btc_rpc_user = <tu-usuario>
btc_rpc_password = <tu-contraseña>
```

Ten en cuenta que aquí el nombre de usuario y la contraseña deben escribirse entre comillas, es decir, para el mismo ejemplo anterior:

```
btc_rpc_user = "aniketh"
btc_rpc_password = "contraseñafuerte"
```

Una vez que hayas hecho eso, deberías estar listo para ejecutar la torre. Dado que estamos ejecutando en regtest, es probable que no se hayan minado bloques en nuestra red de prueba de bitcoin la primera vez que la torre se conecta a ella (si los hay, algo está definitivamente mal). La torre construye una caché interna de los últimos 100 bloques de bitcoind, por lo que al ejecutarla por primera vez es posible que obtengamos el siguiente error:

> ERROR [teosd] No hay suficientes bloques para iniciar la torre (se requieren 100). Mina al menos 100 más.

Dado que estamos ejecutando en regtest, podemos minar un bloque emitiendo un comando RPC, sin necesidad de esperar los 10 minutos de tiempo medio que normalmente vemos en otras redes (como mainnet o testnet). Consulta la ayuda de bitcoin-cli y busca cómo minar bloques. Si necesitas ayuda, puedes consultar este artículo.

![image](assets/2.webp)

Eso es todo, has ejecutado la torre con éxito. ¡Felicidades! 🎉
