---
name: Neutrino
description: Guida all'installazione di LND Neutrino
---

Guida all'installazione di LND Neutrino [https://grunch.dev/guides/rpi-neutrino/](https://grunch.dev/guides/rpi-neutrino/)
Francisco Calderón pubblicato il 14 giugno 2021

# Configurazione di Raspberry Pi con LND

1. Scarica Raspberry Pi OS Lite

Scarica Raspberry Pi OS Lite, [in questa pagina](https://www.raspberrypi.org/software/operating-systems/) troverai le istruzioni per scaricare e installare l'immagine su una micro SD su Windows, Mac e Linux.

2. Formatta la scheda SD

Formatta la scheda SD con Raspberry Pi Imager o con balenaEtcher.

> NOTA: Il simbolo `$` viene utilizzato come prompt e consente all'utente di inserire comandi nel computer, i comandi verranno interpretati da bash in Linux. Il simbolo `#` all'inizio di una riga indica che il testo successivo è un commento.

3. Abilita SSH

Prima di avviare Raspberry Pi con la scheda di memoria formattata, inseriscila in un computer e crea due file che ci consentiranno di connetterci in remoto. Utilizzando il comando `touch` creiamo un file vuoto nella partizione /boot, in questo modo abilitiamo la connessione SSH al primo avvio della scheda SD appena formattata.

```
# NOTA: Se la microSD è stata montata in /media/microSD, il comando
# dovrebbe essere $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

4.- Utilizzando il comando nano, creiamo il file wpa_supplicant.conf e iniziamo immediatamente a modificarlo, in questo file dobbiamo copiare la configurazione del wifi, copia il testo compreso tra INIZIO e FINE e modifica l'SSID e la password del wifi a cui desideri connetterti.

```
$ nano /boot/wpa_supplicant.conf

------ INIZIO -------
country=ar
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
 ssid="MyNetworkSSID"
 psk="password"
}
------ FINE -------
```

5.- Successivamente inseriamo la scheda SD nella Raspberry Pi e colleghiamo la rpi all'alimentatore per avviare il sistema operativo, dovremo identificarla nella rete, probabilmente il protocollo mDNS le assegnerà questo nome nella rete raspberrypi.local, proviamo a connetterci tramite ssh.

```
$ ssh pi@raspberrypi.local
password: raspberry
```

Se non funziona, dobbiamo scoprire la rete, scopriamo l'indirizzo IP a cui siamo connessi.

```
$ ifconfig
```

Ad esempio, se è 192.168.0.0, eseguiamo nmap per trovare la rpi

```
nmap -v 192.168.0.0/24
```

Supponendo di aver trovato un nuovo IP nella nostra rete 192.168.0.30

Accediamo tramite ssh.

```
$ ssh pi@192.168.0.30
password: raspberry
```

6.- Configuriamo la rpi

```
$ sudo raspi-config
```

- Selezioniamo l'opzione (1) e cambiamo la password dell'utente pi'
- Seleccionamos la opción (8) per aggiornare lo strumento di configurazione all'ultima versione
- Seleccionamos la opción (4) per selezionare il nostro fuso orario
- Seleccionamos la opción (7) e poi Expand filesystem
- Finish

  7.- Aggiorniamo il sistema operativo

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```

8.- Aggiungiamo l'utente bitcoin

```
$ sudo adduser bitcoin
```

9.- Assicuriamo la rpi

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

10.- Installiamo go: se non si sta utilizzando una raspberry pi, scaricare go per la propria architettura qui (https://golang.org/dl/)

```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # dovrebbe mostrare il seguente messaggio 'go version go1.13.5 linux/arm'
```

11.- Compiliamo e installiamo lnd

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

12.- Creiamo il file di configurazione di lnd, questo deve essere fatto con l'utente 'bitcoin'

```
$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf
```

```
[Application Options]
# permette pagamenti spontanei
accept-keysend=1

# Nome pubblico del nodo
alias=TU_ALIAS
# Colore pubblico in esadecimale
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

13.- Per far sì che LND si avvii dopo il boot della rpi, dobbiamo creare il file .service in systemd.
'Se siamo loggati come utente bitcoin e vogliamo tornare a utilizzare l'utente pi, basta scrivere "exit"

```
$ exit
$ sudo nano /etc/systemd/system/lnd.service
```

```
[Unit]
Description=LND Lightning Network Daemon
After=network.target

[Service]

# Esecuzione del servizio
###################

ExecStart=/usr/local/bin/lnd


# Gestione del processo
####################

Type=simple
Restart=always
RestartSec=30
TimeoutSec=240
LimitNOFILE=128000

# Creazione delle directory e impostazioni dei permessi
####################################

# Esegui come bitcoin:bitcoin
User=bitcoin
Group=bitcoin

# /run/lightningd
RuntimeDirectory=lightningd
RuntimeDirectoryMode=0710

# Misure di sicurezza
####################

# Fornisci una /tmp e /var/tmp private.
PrivateTmp=true

# Monta /usr, /boot/ e /etc in sola lettura per il processo.
ProtectSystem=full

# Impedisce al processo e a tutti i suoi figli di ottenere
# nuovi privilegi tramite execve().
NoNewPrivileges=true

# Utilizza un nuovo namespace /dev popolato solo con dispositivi pseudo API
# come /dev/null, /dev/zero e /dev/random.
PrivateDevices=true

# Negare la creazione di mappature di memoria scrivibili ed eseguibili.
MemoryDenyWriteExecute=true

[Install]
WantedBy=multi-user.target
```

```
$ sudo systemctl enable lnd
$ sudo systemctl start lnd
$ systemctl status lnd
```

Possiamo visualizzare i log eseguendo il comando journalctl

```
$ sudo journalctl -f -u lnd
```

14. Ora avviamo lnd

```
$ sudo su - bitcoin
$ lncli create
```

15. Aggiungiamo fondi al nostro nodo

```
$ lncli newaddress p2wkh
```

Inviare btc all'indirizzo restituito da lnd

Per controllare il saldo

```
$ lncli walletbalance
{
    "total_balance": "500000",
    "confirmed_balance": "0",
    "unconfirmed_balance": "500000"
}
```

Dopo che la transazione è stata confermata, possiamo aprire un canale, se non sai ancora con quale nodo aprire il canale, puoi andare su 1ml.com e scegliere un nodo.

Apriamo una connessione a un nodo:

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```

Poi apriamo un canale

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```

Controlliamo i nostri fondi

```
$ lncli walletbalance
$ lncli channelbalance
```

Possiamo vedere i canali in sospeso e attivi

```
$ lncli pendingchannels
$ lncli listchannels
```

Per pagare una fattura lightning

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```

Per ricevere un pagamento, creo una fattura per un importo specifico

```
$ lncli addinvoice --memo 'mi primer pago en LN' --amt 100
```

Per visualizzare le informazioni sul mio nodo

```
$ lncli getinfo
```

È possibile visualizzare l'elenco completo dei comandi eseguendo semplicemente lncli

```
$ lncli
```

Infine, per effettuare chiamate all'API di lnd

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```

> FINE, https://grunch.dev/guides/rpi-neutrino/
