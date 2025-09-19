---
name: Neutrino
description: Guía de instalación de LND Neutrino
---
![image](assets/cover.webp)


## Configuración de Raspberry Pi con LND


### 1. Descargar Raspberry Pi OS Lite


Las instrucciones para descargar e instalar la imagen en una tarjeta micro SD en Windows, Mac y Linux se encuentran en [esta página](https://www.raspberrypi.org/software/operating-systems/).


### 2. Formatear la tarjeta SD


Utiliza Raspberry Pi Imager o balenaEtcher.


**Nota:** El símbolo `$` se utiliza como prompt y permite al usuario introducir comandos en el ordenador, los comandos serán interpretados por bash en Linux. El símbolo `#` al principio de una línea indica que el texto siguiente es un comentario.


### 3. Activar SSH


Antes de arrancar la Raspberry Pi con la memoria formateada, debemos insertarla en un ordenador y crear dos archivos que nos permitirán conectarnos remotamente. Usando el comando `touch`, creamos un archivo vacío en la partición /boot, habilitando la conexión SSH en el primer arranque de la tarjeta SD recién formateada.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4. Crear archivo para conexión Wi-Fi


Usando el comando nano creamos el fichero `wpa_supplicant.conf` y directamente empezamos a editarlo. En este fichero tenemos que copiar la configuración wifi, copiando el texto entre START y END, y modificando el SSID y la contraseña de la wifi a la que queremos conectarnos.


```
$ nano /boot/wpa_supplicant.conf

------ START -------
country=ar
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
ssid="MyNetworkSSID"
psk="password"
}
------ END -------
```


### 5. Conexión


A continuación, insertamos la tarjeta SD en la Raspberry Pi y conectamos la Pi a la fuente de alimentación para iniciar el sistema operativo. Necesitamos identificarla en la red, y es probable que el protocolo mDNS le asigne el nombre raspberrypi.local. Intentemos conectarnos a través de SSH.


```
$ ssh pi@raspberrypi.local
password: raspberry
```


Si no funciona, tenemos que averiguar la red. Vamos a averiguar la IP Address a la que estamos conectados.


```
$ ifconfig
```


Por ejemplo, si es 192.168.0.0, usa nmap para encontrar la Pi.


```
nmap -v 192.168.0.0/24
```


Suponiendo que encontramos una nueva IP en nuestra red, vamos a entrar a través de SSH.


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6. Configurar la Pi


```
$ sudo raspi-config
```


- Seleccione la opción (1) y cambie la contraseña del usuario pi.
- Seleccionamos la opción (8) para actualizar la herramienta de configuración a la última versión
- Seleccionamos la opción (4) para seleccionar nuestra zona horaria
- Seleccionamos la opción (7) y luego Expandir sistema de archivos
- Acabado


### 7. Ahora actualiza el sistema operativo


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8. Añadir el usuario Bitcoin


```
$ sudo adduser bitcoin
```


### 9. Asegurar el rpi


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


### 10. Instalar Go


Si no utiliza una raspberry pi, descargue go para su arquitectura [aquí](https://golang.org/dl/).


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11. Compilar e instalar LND


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


### 12. Crear archivo conf LND


Cree el archivo de configuración de LND, esto debe hacerse con el usuario 'Bitcoin'


```
$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf
```


```
[Application Options]
# enable spontaneous payments
accept-keysend=1

# Public name of the node
alias=YOUR_ALIAS
# Public color in hexadecimal
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


### 13. LND servicio autostart


Para hacer que LND arranque después del arranque de rpi, debemos crear el archivo .service en systemd. Si estamos logueados como usuario Bitcoin y queremos volver al usuario pi, simplemente escribimos 'exit'


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


Podemos ver los registros ejecutando el comando journalctl


```
$ sudo journalctl -f -u lnd
```


### 14. Ahora empezamos LND


```
$ sudo su - bitcoin
$ lncli create
```


### 15. Añadir fondos al nodo


```
$ lncli newaddress p2wkh
```

Ahora puede enviar btc al Address devuelto por LND.


con este comando, puede comprobar el saldo:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


Una vez confirmada la transacción, podemos abrir un canal. Si no sabes con qué nodo abrir el canal, puedes ir a 1ml.com y elegir un nodo.


Abrir una conexión con un nodo:


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


Entonces abre un canal:


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


Comprueba nuestros fondos:


```
$ lncli walletbalance
$ lncli channelbalance
```


Podemos ver los canales pendientes y activos:


```
$ lncli pendingchannels
$ lncli listchannels
```


Pagar un rayo Invoice:


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


Para recibir un pago, cree una Invoice por un importe determinado:


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


Para ver información sobre mi nodo:


```
$ lncli getinfo
```


La lista completa de comandos puede verse simplemente ejecutando el comando lncli:


```
$ lncli
```


Por último, para realizar llamadas a la API LND:


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


FIN de la guía