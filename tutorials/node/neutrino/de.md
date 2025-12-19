---
name: Neutrino
description: LND Neutrino Installationsanleitung
---
![image](assets/cover.webp)


## Raspberry Pi Konfiguration mit LND


### 1. Raspberry Pi OS Lite herunterladen


Die Anweisungen zum Herunterladen und Installieren des Images auf einer Micro-SD-Karte unter Windows, Mac und Linux finden Sie auf [dieser Seite](https://www.raspberrypi.org/software/operating-systems/).


### 2. Formatieren der SD-Karte


Verwenden Sie Raspberry Pi Imager oder balenaEtcher.


**Hinweis:** Das Symbol `$` wird als Eingabeaufforderung verwendet und erlaubt dem Benutzer, Befehle in den Computer einzugeben, die von der Bash in Linux interpretiert werden. Das Symbol `#` am Anfang einer Zeile zeigt an, dass der folgende Text ein Kommentar ist.


### 3. SSH aktivieren


Bevor wir den Raspberry Pi mit dem formatierten Speicher starten, müssen wir ihn in einen Computer einstecken und zwei Dateien erstellen, die uns eine Fernverbindung ermöglichen. Mit dem Befehl `touch` erstellen wir eine leere Datei in der /boot-Partition, die beim ersten Start der frisch formatierten SD-Karte eine SSH-Verbindung ermöglicht.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4. Datei für Wi-Fi-Verbindung erstellen


Mit dem Befehl nano erstellen wir die Datei `wpa_supplicant.conf` und beginnen direkt mit der Bearbeitung. In dieser Datei müssen wir die WLAN-Konfiguration kopieren, indem wir den Text zwischen START und END kopieren und die SSID und das Passwort des WLANs ändern, mit dem wir uns verbinden wollen.


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


### 5. Verbindung


Dann setzen wir die SD-Karte in den Raspberry Pi ein und schließen den Pi an die Stromquelle an, um das Betriebssystem zu starten. Wir müssen ihn im Netzwerk identifizieren, und das mDNS-Protokoll wird ihm wahrscheinlich den Namen raspberrypi.local zuweisen. Versuchen wir, eine Verbindung über SSH herzustellen.


```
$ ssh pi@raspberrypi.local
password: raspberry
```


Wenn es nicht funktioniert, müssen wir das Netzwerk herausfinden. Lassen Sie uns herausfinden, mit welchem IP Address wir verbunden sind.


```
$ ifconfig
```


Wenn er beispielsweise 192.168.0.0 lautet, verwenden Sie nmap, um den Pi zu finden.


```
nmap -v 192.168.0.0/24
```


Angenommen, wir finden eine neue IP in unserem Netzwerk, dann können wir uns über SSH einloggen.


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6. Konfigurieren Sie den Pi


```
$ sudo raspi-config
```


- Wählen Sie Option (1) und ändern Sie das Passwort für den Benutzer pi.
- Wir wählen die Option (8), um das Konfigurationstool auf die neueste Version zu aktualisieren
- Wir wählen die Option (4), um unsere Zeitzone auszuwählen
- Wir wählen Option (7) und dann Dateisystem erweitern
- Oberfläche


### 7. Aktualisieren Sie nun das Betriebssystem


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8. Hinzufügen des Bitcoin-Benutzers


```
$ sudo adduser bitcoin
```


### 9. Sichern Sie die rpi


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


### 10. Installieren gehen


Wenn Sie keinen Raspberry Pi verwenden, laden Sie go for your architecture [hier](https://golang.org/dl/) herunter.


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11. LND kompilieren und installieren


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


### 12. LND-Konf-Datei erstellen


Erstellen Sie die LND-Konfigurationsdatei, dies sollte mit dem Benutzer "Bitcoin" geschehen


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


### 13. LND-Dienst Autostart


Um LND nach dem rpi-Boot zu starten, müssen wir die .service-Datei in systemd erstellen. Wenn wir als Bitcoin-Benutzer eingeloggt sind und zurück zum pi-Benutzer wechseln wollen, geben wir einfach 'exit' ein


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


Wir können die Protokolle anzeigen, indem wir den Befehl journalctl


```
$ sudo journalctl -f -u lnd
```


### 14. Jetzt beginnen wir LND


```
$ sudo su - bitcoin
$ lncli create
```


### 15. Mittel zum Knoten hinzufügen


```
$ lncli newaddress p2wkh
```

Sie können jetzt btc an den Address senden, der von LND zurückgeschickt wurde.


mit diesem Befehl können Sie den Kontostand überprüfen:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


Sobald die Transaktion bestätigt wurde, können wir einen Kanal öffnen. Wenn Sie nicht wissen, mit welchem Knotenpunkt Sie den Kanal öffnen sollen, können Sie auf 1ml.com gehen und einen Knotenpunkt auswählen.


Öffnen Sie eine Verbindung zu einem Knoten:


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


Dann öffnen Sie einen Kanal:


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


Prüfen Sie unsere Fonds:


```
$ lncli walletbalance
$ lncli channelbalance
```


Wir können die ausstehenden und aktiven Kanäle anzeigen:


```
$ lncli pendingchannels
$ lncli listchannels
```


Um einen blitzschnellen Invoice zu bezahlen:


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


Um eine Zahlung zu erhalten, erstellen Sie eine Invoice für einen bestimmten Betrag:


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


Um Informationen über meinen Knoten anzuzeigen:


```
$ lncli getinfo
```


Die vollständige Liste der Befehle kann durch einfaches Ausführen des Befehls lncli angezeigt werden:


```
$ lncli
```


Und schließlich, um die LND-API aufzurufen:


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


ENDE des Leitfadens!