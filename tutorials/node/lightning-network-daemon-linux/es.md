---
name: Lightning Network Daemon (Linux)
description: Instalación y ejecución de Lightning Network Daemon en Linux
---

![cover-lightning-network-daemon](assets/cover.webp)



La Red Lightning es una segunda capa de la red Bitcoin, lo que le permite adquirir dimensiones de relámpago, gracias sobre todo a la rapidez y el bajo coste de las transacciones que ofrece.



En este tutorial, instalaremos la implementación Lightning Network Daemon en nuestra máquina Linux (distribución Ubuntu 24.04).



## ¿Qué es la Lightning Network Daemon?



Lightning Network Daemon es una implementación Go completa de Lightning Network. Fue creada por Lightning Labs y te permite ejecutar una instancia completa de un nodo Lightning en tu máquina.


En otras palabras, con esta aplicación, podrás:





- **Interactuar con Lightning Network**: Podrás utilizar líneas de comandos para crear billeteras de Lightning Network, gestionar canales y rutas de pago, y mucho más, directamente desde el terminal de tu máquina.
- **Vincular un nodo remoto de Bitcoin o de tu propia instancia de Bitcoin Core**: LND te permite enlazar una instancia de Bitcoin y utilizarla como backend. Para usar esta implementación, no necesitarás ejecutar una instancia de Bitcoin Core en tu máquina.




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## ¿Por qué tener tu propio nodo Lightning?


Lightning es una superposición de Bitcoin que optimiza el proceso de transferencia y reduce los costes de transacción.



Al rotar tu nodo Lightning, ganas soberanía y autonomía. Tienes el control de tus fondos, así que tenlo en cuenta:



"No tus llaves, no tu bitcoin"



En este sentido, la ejecución de un nodo Lightning aumenta la seguridad e integridad de tus datos de las siguientes maneras:





- **Control total**: Gestiona tus propios canales de pago, conviértete en tu propio banco y sé dueño de tus activos.
- **Confidencialidad**: Realiza transacciones sin depender de terceros para proteger su privacidad.
- **Aprendizaje y autonomía**: Gracias a los comandos `lncli`, puedes comprender mejor los procesos subyacentes de Lightning aplicándote desde tu terminal.
- **Descentralización**: Participar activamente en el refuerzo y la descentralización del Bitcoin / Lightning Network.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


Tenemos dos opciones para ejecutar una instancia de la implementación de LND en nuestra máquina. Podemos configurar el entorno en nuestra propia máquina para que se ejecute localmente, o instalar LND desde un contenedor Docker. Aquí, nos concentraremos en la primera opción, y veremos cómo proceder con Docker en un tutorial posterior.


## Instalar LND a partir del código fuente



### Requisitos previos


Como LND está escrito en Go, necesitas asegurarte de que tienes el entorno GoLang y las dependencias necesarias en tu máquina Linux.





- **Requisitos de hardware:**


Para disfrutar de una experiencia fluida y sin problemas, tu máquina deberá tener la capacidad necesaria para ejecutar su nodo LND Lightning.



Necesitarás:


1. **8 GB de RAM** para una fluidez óptima,


2. **Un procesador multinúcleo (quad-core o más)** para gestionar eficazmente las acciones de tu nodo,


3. **Al menos 5 GB de espacio en disco** para el modo de nodo podado y 1 TB para ejecutar Bitcoin Core (opcional si se utiliza un nodo remoto)





- **Instalar dependencias útiles:**


El siguiente comando te permitirá instalar en tu máquina las herramientas necesarias para ejecutar LND. Entre otras cosas, necesitarás instalar `Git`, una herramienta de versionado, y `make`, que puede ejecutar y construir la implementación de LND desde el código fuente.



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- **Instala GoLang en tu máquina Linux**



A la fecha de este tutorial, LND requiere la ***versión 1.23.6 de Go*** para su instalación.



Si ya tenías instalada una versión anterior, elimínala para la nueva instalación de Go.


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- **Configuración del entorno Go**


En tu archivo `~/.bashrc`, inicializa las siguientes variables de entorno para añadir Go a tu sistema Linux.



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```

- **Comprobación de la instalación** (en francés)

```bash
go version
```

![go-version](assets/fr/03.webp)


### Clonar el repositorio GitHub de LND

Utiliza git para obtener una copia del código fuente de LND localmente en tu máquina


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### Construir e instalar



La herramienta `make`, previamente instalada, le permitirá construir un ejecutable a partir del código fuente de LND y proceder a su instalación.

```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



Instala LND en tu máquina

```bash
# installer LND
make install
```

![make-lnd](assets/fr/06.webp)


- Comprobación de la instalación** (en francés)



Para asegurarte de que todo ha ido bien, ejecuta este comando que te dará la versión de LND que estás ejecutando actualmente.



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)


- Mantenimiento y actualizaciones

```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **IMPORTANTE**: Las actualizaciones de LND pueden requerir versiones más recientes de Go, así que asegúrate de actualizar tu sistema para evitar problemas de dependencia durante la instalación.

### Configuración de Lightning Network Daemon


La configuración de un nodo Lightning LND es similar a la de Bitcoin, y se realiza en un archivo de configuración que contiene todos los parámetros del nodo. Para ello, en la raíz de tu máquina crea una carpeta oculta `.LND` y luego crea un archivo de configuración `LND.conf` en esta carpeta.



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```



En el archivo de configuración, configura tu nodo LND.

```
noseedbackup=0
debuglevel=debug

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=bitcoind

[Bitcoind]
bitcoind.rpcuser=<UTILISATEUR_BITCOIN>
bitcoind.rpcpassword=<MOT_DE_PASSE_BITCOIN>
bitcoind.zmqpubrawblock=tcp://127.0.0.1:28332
bitcoind.zmqpubrawtx=tcp://127.0.0.1:28333

```

## Comprender la configuración

Es importante que conozcas la configuración mínima que necesitas para una correcta y completa instalación de tu nodo LND.

Basándonos en el contenido del fichero `~/.LND/LND.conf`, aquí están los detalles de los campos:


- noseedbackup**: Permite elegir si deseas que LND realice copias de seguridad automáticas de tus billeteras.  Establecer esta propiedad a `0` te permite guardar manualmente la información de restauración en una ubicación segura elegida personalmente.





- **debuglevel**: Permite definir el nivel de detalle de los errores y registros en caso de que se produzcan errores durante una acción.





- **Bitcoin.activo**: Ordena a LND que opere como nodo Bitcoin e interactúe con la red Bitcoin.

- **Bitcoin.Mainnet**: Especifica que LND se conecte a la red principal de Bitcoin (Mainnet), puedes establecer los valores `bitcoind.signet` y `bitcoind.regtest` respectivamente para las redes Bitcoin Signet y Bitcoin Regtest
  
- **Bitcoin.nodo**: Especifica el tipo de nodo Bitcoin al que debe conectarse LND.

- **Bitcoin.rpcuser** y **Bitcoin.rpcpassword**: Representan respectivamente los nombres de usuario (usuario, contraseña) para conectarse a su nodo Bitcoin

- **bitcoind.zmqpubrawblock** y **bitcoind.zmqpubrawtx**: Definen respectivamente puntos finales ZeroMQ para recibir notificaciones sobre nuevos bloques y transacciones en la red Bitcoin.

## Comprobación de la instalación con LND

Probablemente querrás asegurarte de que el proceso se ha realizado correctamente y de que se está sincronizando con Lightning Network para mantener actualizada la información de los nodos.

Para iniciar la implementación de LND y obtener información sobre tu nodo, simplemente escribe el comando:

```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## Realizando acciones en LND



Una vez finalizada y comprobada la instalación, puedes empezar a utilizarlo.


Aquí tienes los comandos esenciales para empezar.

### Crear una billetera
584 lines (466 loc) · 16.2 KB
name 	description
LAPP bitcoin
	
Tutorial para desarrollar tu primera LApp

Aprende a programar tu primera lightning app

Requisitos:

    NodeJs >= 8
    LND >= 9


Una billetera Lightning es el primer paso para gestionar tus fondos.

⚠️ **IMPORTANTE**: Toma nota de tu frase de 24 palabras **seed**. La necesitarás para recuperar tus fondos en caso de problemas.

Guarda también la contraseña de tu billetera para poder desbloquearla con el comando `lncli unlock` cuando reinicies su nodo LND.

```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### Comprueba tu saldo

Consulta tus cuentas directamente desde tu terminal:


```bash
lncli walletbalance
```

![solde](assets/fr/09.webp)


### Información sobre tu nodo

Utiliza el siguiente comando para averiguar qué canales están activos en tu nodo.



```bash
lncli listchannels
```



También puedes obtener una lista de los nodos a los que está conectado.

```bash
lncli listpeers
```
### Gestión de canales

Un canal Lightning te permite tener una **conexión directa, par a par, con otro nodo de la Lightning Network**. En este canal, puedes libremente intercambiar Satoshis hasta la capacidad del canal.



### Conectarse a un nodo



Conectarse a otros nodos Lightning es una acción fundamental si quieres participar activamente y beneficiarte de la potencia de Lightning.



Para conectarte a un peer (nodo Lightning), necesitarás tres datos:




- **La clave pública del nodo**: Es el identificador único del nodo en la red Bitcoin;
- **IP**: La IP de la máquina en la que está instalado el nodo;
- **PUERTO**:  El puerto abierto en la máquina que permite la comunicación con este nodo.



Puedes encontrar nodos a los que conectarte en [amboss](https://amboss.space/), una plataforma que ofrece información sobre los nodos Lightning.



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple: Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




Asegúrate de conectarte a **nodos fiables** para preservar la integridad de tu propio sistema. Aquí tienes algunas recomendaciones para elegir las conexiones adecuadas.





- **Diversificación geográfica**: Conéctate a nodos de diferentes regiones.





- **Reputación**: Elije nodos con buena disponibilidad.





- **Capacidad**: Elije nodos con buena liquidez.





- **Cargos**: Comisiones por enrutamiento.


### Abrir un canal de pago


Para abrir un canal de pago, asegúrate de que estáa **conectado** al nodo par, luego define la **capacidad** (la cantidad de satoshis) que deseas bloquear en este canal.



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### Crear un cobro



Un cobro Lightning representa una cadena de caracteres que expresa tu deseo de recibir satoshis en tu billetera Lightning.


Crear cobros Lightning con tu propio nodo te permite proteger tus datos (geográficos y personales) y te da un 100% de autonomía sobre la gestión de tus fondos.



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### Realizar un pago en Lightning



```bash
lncli payinvoice <FACTURE>
```


### Cerrar un canal



Hay dos formas de cerrar un canal activo en el nodo actual.





- **Cierre cooperativo**: Señala el deseo de tu nodo de retirarse del canal de pago, asegurando que se completan las tareas en curso y que se realiza una copia de seguridad de los datos para evitar la pérdida de fondos.


```
lncli closechannel <ID_CANAL>
```




- **Cierre forzoso**: ⚠️ Debe evitarse en la medida de lo posible, esta acción interrumpe los procesos en curso en tu canal de pago y aumenta el riesgo de pérdida de fondos.


```
lncli closechannel --force <ID_CANAL>
```


## Buenas prácticas y seguridad para tu nodo LND.


La seguridad es primordial cuando se utiliza un nodo Bitcoin/ Lightning. He aquí algunos puntos para reforzar la seguridad de tu instalación:


- Guarda tu frase `seed` en un lugar seguro y fuera de línea.


- Haz copias de seguridad periódicas del archivo `~/.LND/channel.backup`: Este archivo guarda los estados de tus canales cada vez que se abre un nuevo canal (o se cierra uno antiguo) en tu nodo.


⚠️ Permite restaurar canales y recuperar fondos bloqueados en canales de pago en caso de pérdida de datos o fallo de un nodo



Puedes restaurar tus fondos con el siguiente comando especificando la ruta de la copia de seguridad de este archivo:


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Asegúrate de haber guardado las palabras de restauración y la contraseña de tu billetera Lightning.
- Manten tu sistema actualizado.



## Solución de problemas actuales


### Problemas frecuentes


- **bitcoind error de conexión**: Comprueba tus datos de conexión RPC
- **Sincronización bloqueada**: Comprueba tu conexión a Internet
- **Error de permisos**: Comprueba los derechos de la carpeta `~/.LND`




Así que has llegado al final de este tutorial. Si quieres saber más sobre Lightning, te ofrecemos este curso introductorio para que conozcas mejor los conceptos y prácticas que hay detrás de la Lightning Network.




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
