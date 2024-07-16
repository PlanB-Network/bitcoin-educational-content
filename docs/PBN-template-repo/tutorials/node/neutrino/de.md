---
name: Neutrino
description: LND Neutrino Installationsanleitung
---

# Raspberry Pi Konfiguration mit LND

1. Raspberry Pi OS Lite herunterladen

Lade Raspberry Pi OS Lite von [dieser Seite](https://www.raspberrypi.org/software/operating-systems/) herunter. Dort findest du Anweisungen zum Herunterladen und Installieren des Images auf einer microSD-Karte unter Windows, Mac und Linux.

2. SD-Karte formatieren

Formatiere die SD-Karte mit Raspberry Pi Imager oder balenaEtcher.

> HINWEIS: Das Symbol `$` wird als Prompt verwendet und ermöglicht es dem Benutzer, Befehle auf dem Computer einzugeben. Die Befehle werden von bash in Linux interpretiert. Das Symbol `#` am Anfang einer Zeile zeigt an, dass der folgende Text ein Kommentar ist.

3. SSH aktivieren

Bevor du den Raspberry Pi mit der formatierten Speicherkarte startest, musst du sie in einen Computer einlegen und zwei Dateien erstellen, die eine Remoteverbindung ermöglichen. Mit dem Befehl `touch` erstellen wir eine leere Datei und aktivieren damit die SSH-Verbindung beim ersten Start der frisch formatierten SD-Karte in der /boot-Partition.

```
# HINWEIS: Wenn die microSD-Karte unter /media/microSD eingebunden ist, sollte der Befehl
# lauten: $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

4.- Mit dem Befehl nano erstellen wir die Datei wpa_supplicant.conf und beginnen direkt mit der Bearbeitung. In dieser Datei müssen wir die WLAN-Konfiguration kopieren, kopiere den Text zwischen BEGINN und ENDE und ändere die SSID und das Passwort des WLANs, mit dem du dich verbinden möchtest.

```
$ nano /boot/wpa_supplicant.conf

------ BEGINN -------
country=ar
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
 ssid="MyNetworkSSID"
 psk="password"
}
------ ENDE -------
```

5.- Lege dann die SD-Karte in den Raspberry Pi ein und verbinde den Pi mit der Stromquelle, um das Betriebssystem zu starten. Du musst ihn im Netzwerk identifizieren, wahrscheinlich weist ihm das mDNS-Protokoll den Namen raspberrypi.local im Netzwerk zu. Versuchen wir uns per SSH zu verbinden.

```
$ ssh pi@raspberrypi.local
Passwort: raspberry
```

Wenn es nicht funktioniert, müssen wir das Netzwerk herausfinden. Lassen wir uns die IP-Adresse anzeigen, mit der wir verbunden sind.

```
$ ifconfig
```

Wenn es zum Beispiel 192.168.0.0 ist, führen wir nmap aus, um den Raspberry Pi zu finden.

```
nmap -v 192.168.0.0/24
```

Angenommen, wir finden eine neue IP-Adresse in unserem Netzwerk: 192.168.0.30

Verbinde dich per SSH.

```
$ ssh pi@192.168.0.30
Passwort: raspberry
```

6.- Konfiguriere den Raspberry Pi

```
$ sudo raspi-config
```

- Wähle die Option (1) und ändere das Passwort für den Benutzer "pi".
- Wir wählen die Option (8), um das Konfigurationstool auf die neueste Version zu aktualisieren.
- Wir wählen die Option (4), um unsere Zeitzone auszuwählen.
- Wir wählen die Option (7) und dann "Expand filesystem".
- Fertig.

  7.- Wir aktualisieren das Betriebssystem.

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```

8.- Wir fügen den Benutzer "bitcoin" hinzu.

```
$ sudo adduser bitcoin
```

9.- Wir sichern die RPi.

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

10.- Wir installieren Go: Wenn Sie keinen Raspberry Pi verwenden, laden Sie Go für Ihre Architektur hier herunter (https://golang.org/dl/).

```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # sollte die folgende Meldung anzeigen: 'go version go1.13.5 linux/arm'
```

11.- Wir kompilieren und installieren lnd.

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

12.- Wir erstellen die lnd-Konfigurationsdatei. Dies muss mit dem Benutzer 'bitcoin' erfolgen.

```
$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf
```

```
[Application Options]
# ermöglicht spontane Zahlungen
accept-keysend=1

# Öffentlicher Name des Knotens
alias=DEIN_ALIAS
# Öffentliche Farbe in Hexadezimal
color=#000000
debuglevel=info
maxpendingchannels=5
listen=localhost
# gRPC-Socket
rpclisten=0.0.0.0:10009

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=neutrino

[neutrino]
neutrino.connect=bb2.breez.technology
```

13.- Um sicherzustellen, dass LND nach dem Booten der RPi gestartet wird, müssen wir die .service-Datei in systemd erstellen.
'Si wir als Bitcoin-Benutzer angemeldet sind und zum Pi-Benutzer zurückkehren möchten, geben wir einfach "exit" ein.

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

Wir können die Protokolle anzeigen, indem wir den Befehl journalctl ausführen.

```
$ sudo journalctl -f -u lnd
```

14. Jetzt starten wir lnd.

```
$ sudo su - bitcoin
$ lncli create
```

15. Fügen Sie Geld zu unserem Knoten hinzu.

```
$ lncli newaddress p2wkh
```

Senden Sie BTC an die Adresse, die uns von lnd zurückgegeben wird.

Um den Kontostand abzufragen.

```
$ lncli walletbalance
{
    "total_balance": "500000",
    "confirmed_balance": "0",
    "unconfirmed_balance": "500000"
}
```

Nachdem die Transaktion bestätigt wurde, können wir einen Kanal öffnen. Wenn Sie noch nicht wissen, mit welchem Knoten Sie den Kanal öffnen möchten, können Sie zu 1ml.com gehen und einen Knoten auswählen.

Wir öffnen eine Verbindung zu einem Knoten:

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```

Dann öffnen wir einen Kanal.

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```

Wir überprüfen unsere Geldmittel.

```
$ lncli walletbalance
$ lncli channelbalance
```

Wir können ausstehende und aktive Kanäle anzeigen.

```
$ lncli pendingchannels
$ lncli listchannels
```

Um eine Lightning-Rechnung zu bezahlen.

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```

Um eine Zahlung zu erhalten, erstellen wir eine Rechnung für einen bestimmten Betrag.

````
$ lncli addinvoice --memo 'mi primer pago en LN' --amt 100```
````

Um Informationen über meinen Knoten anzuzeigen:

```
$ lncli getinfo
```

Die vollständige Liste der Befehle kann nur durch Ausführung von lncli angezeigt werden:

```
$ lncli
```

Schließlich, um Anrufe an die lnd-API zu tätigen:

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```

> ENDE
