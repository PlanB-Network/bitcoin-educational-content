LND Neutrino Installation Guide

https://grunch.dev/guides/rpi-neutrino/
Francisco Calderón published on
June 14, 2021

# Configuración de Raspberry Pi con LND

## 1. Descargar Raspberry Pi OS Lite

Descargar Raspberry Pi OS Lite, en [esta página](https://www.raspberrypi.org/software/operating-systems/) están las instrucciones para descargar e instalar la imagen en una micro SD en Windows, Mac y Linux.

## 2. Formatear la SD Card

Formatear la SD card con Raspberry Pi Imager o con balenaEtcher.

> NOTA: El símbolo `$` se utiliza como prompt y permite al usuario ingresar órdenes al computador, los comandos serán interpretados por bash en Linux. El símbolo `#` al principio de una línea indica que el texto a continuación es un comentario.

## 3. Habilitar SSH

Antes de iniciar la Raspberry Pi con la memoria formateada, debemos insertarla en una computadora y crear dos archivos que nos permitirán conectarnos remotamente. Con el comando `touch` creamos un archivo vacío y con esto en la partición /boot, con esto habilitamos conexión por SSH en el primer inicio de la SD card recién formateada.

```
# NOTA: Si la microSD ha sido montada en /media/microSD, el comando
# debería ser $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

4.- Con el comando nano creamos el archivo wpa_supplicant.conf y directamente comenzamos editarlo, en este archivo debemos copiar la configuración del wifi, copia el texto contenido entre INICIO y FIN, y modifca la SSID y contraseña de la wifi a la que te desees conectar.

```
$ nano /boot/wpa_supplicant.conf

------ INICIO -------
country=ar
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
 ssid="MyNetworkSSID"
 psk="password"
}
------ FIN -------
```

5.- Luego introducimos la sd card en la Raspberry pi y la conectamos la rpi a la fuente de poder para que inicie el sistema operativo, necesitaremos identificarla en la red, probablemente el protocolo mDNS le asigne este nombre en la red raspberrypi.local, intentemos conectarnos por ssh.

```
$ ssh pi@raspberrypi.local
password: raspberry
```

Si no funciona hay que averiguar la red, averiguemos la dirección IP a la que estamos conectados.

```
$ ifconfig
```

Si por ejemplo, es 192.168.0.0, hacer nmap para encontrar la rpi

```
nmap -v 192.168.0.0/24
```

Suponiendo que encontramos una nueva IP en nuestra red 192.168.0.30

Entrar por ssh.

```
$ ssh pi@192.168.0.30
password: raspberry
```

6.- Configuramos la rpi

```
$ sudo raspi-config
```

- Seleccionamos la opción (1) y cambiamos el password del usuario pi
- Seleccionamos la opción (8) para actualizar la herramienta de configuración a la última versión
- Seleccionamos la opción (4) para seleccionar nuestra zona horaria
- Seleccionamos la opción (7) y luego Expand filesystem
- Finish

  7.- Actualizamos el SO

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```

8.- Agregamos el usuario bitcoin

```
$ sudo adduser bitcoin
```

9.- Aseguramos la rpi

```
$ sudo apt install ufw
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ sudo ufw allow 22 comment 'allow SSH from LAN'
$ sudo ufw allow 9735 comment 'allow Lightning'
$ sudo ufw allow 10009 comment 'Lightning gRPC'
$ sudo ufw enable
$ sudo systemctl enable ufw
$ sudo ufw status
$ sudo apt install fail2ban
```

10.- Instalamos go: si no se está utilizando una raspberry pi descargue go para su arquitectura aquí (https://golang.org/dl/)

```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # debe mostrar el siguiente mensaje 'go version go1.13.5 linux/arm'
```

11.- Compilamos y instalamos lnd

```
$ git clone https://github.com/lightningnetwork/lnd.git
$ cd lnd
$ make
$ make install tags="autopilotrpc chainrpc experimental invoicesrpc routerrpc signrpc walletrpc watchtowerrpc wtclientrpc"
$ sudo cp $GOPATH/bin/lnd /usr/local/bin/
$ sudo cp $GOPATH/bin/lncli /usr/local/bin/
$ lncli --version
lncli version 0.11.0-beta commit=v0.11.0-beta-61-g6055b00dbbcedf45cd60f12e57dc5c1a7b97746f
```

12.- Creamos el archivo de configuración de lnd, esto se debe realizar con el usuario 'bitcoin'

```
$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf
```

```
[Application Options]
# permite pagos espontáneos
accept-keysend=1

# Nombre público del nodo
alias=TU_ALIAS
# Color público en hexadecimal
color=#000000
debuglevel=info
maxpendingchannels=5
listen=localhost
# gRPC socket
rpclisten=0.0.0.0:10009

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=neutrino

[neutrino]
neutrino.connect=bb2.breez.technology
```

13.- Para que LND se inicie luego del booteo de la rpi debemos crear el archivo .service en systemd

Si estamos como usuario bitcoin y queremos volver a utilizar el usuario pi solo escribimos exit

```
$ exit
$ sudo nano /etc/systemd/system/lnd.service
```

```
[Unit]
Description=LND Lightning Network Daemon
After=network.target

[Service]

# Service execution
###################

ExecStart=/usr/local/bin/lnd


# Process management
####################

Type=simple
Restart=always
RestartSec=30
TimeoutSec=240
LimitNOFILE=128000

# Directory creation and permissions
####################################

# Run as bitcoin:bitcoin
User=bitcoin
Group=bitcoin

# /run/lightningd
RuntimeDirectory=lightningd
RuntimeDirectoryMode=0710

# Hardening measures
####################

# Provide a private /tmp and /var/tmp.
PrivateTmp=true

# Mount /usr, /boot/ and /etc read-only for the process.
ProtectSystem=full

# Disallow the process and all of its children to gain
# new privileges through execve().
NoNewPrivileges=true

# Use a new /dev namespace only populated with API pseudo devices
# such as /dev/null, /dev/zero and /dev/random.
PrivateDevices=true

# Deny the creation of writable and executable memory mappings.
MemoryDenyWriteExecute=true

[Install]
WantedBy=multi-user.target
```

```
$ sudo systemctl enable lnd
$ sudo systemctl start lnd
$ systemctl status lnd
```

Podemos ver los logs ejecutando el comando journalctl

```
$ sudo journalctl -f -u lnd
```

14. Ahora iniciamos lnd

```
$ sudo su - bitcoin
$ lncli create
```

15. Agregar fondos a nuestro nodo

```
$ lncli newaddress p2wkh
```

Enviar btc a la dirección que nos devuelve lnd

Para consultar el balance

```
$ lncli walletbalance
{
    "total_balance": "500000",
    "confirmed_balance": "0",
    "unconfirmed_balance": "500000"
}
```

Luego de que haya sido confirmada la transacción podemos abrir algún canal, si no sabes aún con qué nodo abrir el canal puedes ir a 1ml.com y elegir un nodo.

Abrimos una conexión a un nodo:

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```

Luego abrimos un canal

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```

Chequeamos nuestros fondos

```
$ lncli walletbalance
$ lncli channelbalance
```

Podemos ver los canales pendientes y los activos

```
$ lncli pendingchannels
$ lncli listchannels
```

Para pagar una invoice lightning

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```

Para recibir un pago creo una invoice por un monto específico

```
$ lncli addinvoice --memo 'mi primer pago en LN' --amt 100
```

Para ver información sobre mi nodo

```
$ lncli getinfo
```

La lista completa de comandos la podemos ver solo ejecutando lncli

```
$ lncli
```

Finalmente para hacer llamadas a la api de lnd

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```

FIN, https://grunch.dev/guides/rpi-neutrino/
