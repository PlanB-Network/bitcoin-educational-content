---
name: Neutrino
description: Guida all'installazione del LND Neutrino
---
![image](assets/cover.webp)


## Configurazione di Raspberry Pi con LND


### 1. Scaricare Raspberry Pi OS Lite


Le istruzioni per scaricare e installare l'immagine su una scheda micro SD in Windows, Mac e Linux sono disponibili su [questa pagina](https://www.raspberrypi.org/software/operating-systems/).


### 2. Formattare la scheda SD


Utilizzare Raspberry Pi Imager o balenaEtcher.


**Nota:** Il simbolo `$` è usato come prompt e permette all'utente di inserire comandi nel computer; i comandi saranno interpretati da bash in Linux. Il simbolo `#` all'inizio di una riga indica che il testo seguente è un commento.


### 3. Abilitare SSH


Prima di avviare il Raspberry Pi con la memoria formattata, dobbiamo inserirlo in un computer e creare due file che ci permetteranno di connetterci da remoto. Utilizzando il comando `touch`, creiamo un file vuoto nella partizione /boot, consentendo la connessione SSH al primo avvio della scheda SD appena formattata.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4. Creare un file per la connessione Wi-Fi


Con il comando nano creiamo il file `wpa_supplicant.conf` e iniziamo direttamente a modificarlo. In questo file, dobbiamo copiare la configurazione del wifi, copiando il testo tra START e END e modificando l'SSID e la password del wifi a cui ci si vuole connettere.


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


### 5. Connessione


Quindi, inseriamo la scheda SD nel Raspberry Pi e colleghiamo il Pi all'alimentazione per avviare il sistema operativo. Dobbiamo identificarlo sulla rete e il protocollo mDNS probabilmente gli assegnerà il nome raspberrypi.local. Proviamo a connetterci tramite SSH.


```
$ ssh pi@raspberrypi.local
password: raspberry
```


Se non funziona, dobbiamo scoprire la rete. Scopriamo l'IP Address a cui siamo connessi.


```
$ ifconfig
```


Ad esempio, se è 192.168.0.0, usare nmap per trovare il Pi.


```
nmap -v 192.168.0.0/24
```


Supponendo di aver trovato un nuovo IP sulla nostra rete, entriamo tramite SSH.


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6. Configurare il Pi


```
$ sudo raspi-config
```


- Selezionare l'opzione (1) e modificare la password dell'utente pi.
- Selezioniamo l'opzione (8) per aggiornare lo strumento di configurazione alla versione più recente
- Selezioniamo l'opzione (4) per selezionare il nostro fuso orario
- Selezioniamo l'opzione (7) e poi Espandi filesystem
- Finitura


### 7. Ora aggiornate il sistema operativo


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8. Aggiungere l'utente Bitcoin


```
$ sudo adduser bitcoin
```


### 9. Proteggere l'rpi


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


### 10. Installare Go


Se non si utilizza un raspberry pi, scaricare Go for your architecture [qui](https://golang.org/dl/).


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11. Compilare e installare LND


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


### 12. Creare il file conf di LND


Creare il file di configurazione del LND; questa operazione deve essere eseguita con l'utente "Bitcoin"


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


### 13. LND servizio di avvio automatico


Per fare in modo che LND si avvii dopo l'avvio di rpi, dobbiamo creare il file .service in systemd. Se siamo connessi come utente Bitcoin e vogliamo tornare all'utente pi, dobbiamo semplicemente digitare 'exit'


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


È possibile visualizzare i registri eseguendo il comando journalctl


```
$ sudo journalctl -f -u lnd
```


### 14. Ora iniziamo il LND


```
$ sudo su - bitcoin
$ lncli create
```


### 15. Aggiungere fondi al nodo


```
$ lncli newaddress p2wkh
```

È ora possibile inviare btc al Address restituito dal LND.


con questo comando, è possibile controllare l'equilibrio:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


Una volta confermata la transazione, possiamo aprire un canale. Se non sapete con quale nodo aprire il canale, potete andare su 1ml.com e scegliere un nodo.


Aprire una connessione a un nodo:


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


Quindi aprire un canale:


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


Controllate i nostri fondi:


```
$ lncli walletbalance
$ lncli channelbalance
```


Possiamo visualizzare i canali in attesa e quelli attivi:


```
$ lncli pendingchannels
$ lncli listchannels
```


Per pagare un fulmine Invoice:


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


Per ricevere un pagamento, creare un Invoice per un importo specifico:


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


Per visualizzare le informazioni sul mio nodo:


```
$ lncli getinfo
```


L'elenco completo dei comandi può essere visualizzato semplicemente eseguendo il comando lncli:


```
$ lncli
```


Infine, per effettuare chiamate all'API LND:


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


Fine della guida!