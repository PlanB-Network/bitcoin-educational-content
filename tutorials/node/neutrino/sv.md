---
name: Neutrino
description: Installationshandbok för LND Neutrino
---

# Konfiguration av Raspberry Pi med LND


#### 1. Ladda ner Raspberry Pi OS Lite

Instruktioner för att ladda ner och installera bilden på ett micro SD-kort i Windows, Mac och Linux finns på [den här sidan] (https://www.raspberrypi.org/software/operating-systems/).


#### 2. Formatera SD-kortet

använd Raspberry Pi Imager eller balenaEtcher.


**Symbolen `$` används som en prompt och gör det möjligt för användaren att skriva in kommandon i datorn, kommandona tolkas av bash i Linux. Symbolen `#` i början av en rad anger att den följande texten är en kommentar.


#### 3. Aktivera SSH


Innan vi startar Raspberry Pi med det formaterade minnet måste vi sätta in det i en dator och skapa två filer som gör att vi kan fjärransluta. Med kommandot `touch` skapar vi en tom fil i /boot-partitionen, vilket möjliggör SSH-anslutning vid den första starten av det nyformaterade SD-kortet.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

#### 4. Skapa fil för Wi-Fi-anslutning

Med hjälp av kommandot nano skapar vi filen `wpa_supplicant.conf` och börjar direkt redigera den. I den här filen måste vi kopiera wifi-konfigurationen, kopiera texten mellan START och END och ändra SSID och lösenord för det wifi du vill ansluta till.


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


#### 5. Anslutning

Sedan sätter vi in SD-kortet i Raspberry Pi och ansluter Pi till strömkällan för att starta operativsystemet. Vi måste identifiera den i nätverket, och mDNS-protokollet kommer sannolikt att tilldela den namnet raspberrypi.local. Låt oss försöka ansluta via SSH.

```
$ ssh pi@raspberrypi.local
password: raspberry
```

Om det inte fungerar måste vi ta reda på nätverket. Låt oss ta reda på vilken IP Address vi är anslutna till.


```
$ ifconfig
```


Om det t.ex. är 192.168.0.0 använder du nmap för att hitta Pi.


```
nmap -v 192.168.0.0/24
```


Förutsatt att vi hittar en ny IP i vårt nätverk, låt oss gå in via SSH.


```
$ ssh pi@192.168.0.30
password: raspberry
```


#### 6. Konfigurera Pi

```
$ sudo raspi-config
```


- Välj alternativ (1) och ändra lösenordet för användaren pi.
- Vi väljer alternativ (8) för att uppdatera konfigurationsverktyget till den senaste versionen
- Vi väljer alternativ (4) för att välja vår tidszon
- Vi väljer alternativ (7) och sedan Expand filesystem
- Avsluta


#### 7. Uppdatera nu operativsystemet

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


#### 8. Lägg till Bitcoin-användaren

```
$ sudo adduser bitcoin
```


#### 9. Säkra rpi


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


#### 10. Installera Go

Om du inte använder en raspberry pi kan du ladda ner go for your architecture [här] (https://golang.org/dl/)


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


#### 11. Kompilera och installera LND


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


#### 12. Skapa LND conf-fil

Skapa konfigurationsfilen för LND, detta bör göras med användaren "Bitcoin


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


#### 13. LND tjänst autostart

För att få LND att starta efter rpi-start måste vi skapa .service-filen i systemd. Om vi är inloggade som Bitcoin-användare och vill byta tillbaka till pi-användaren skriver vi helt enkelt "exit


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


Vi kan visa loggarna genom att köra kommandot journalctl


```
$ sudo journalctl -f -u lnd
```


#### 14. Nu börjar vi LND


```
$ sudo su - bitcoin
$ lncli create
```


#### 15. Tillför medel till noden


```
$ lncli newaddress p2wkh
```

Du kan nu skicka btc till Address som returneras av LND.


med det här kommandot kan du kontrollera saldot:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


När transaktionen har bekräftats kan vi öppna en kanal. Om du inte vet vilken nod du ska öppna kanalen med, kan du gå till 1ml.com och välja en nod.


Öppna en anslutning till en nod:

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


Öppna sedan en kanal:

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


Kontrollera våra fonder:

```
$ lncli walletbalance
$ lncli channelbalance
```


Vi kan se de väntande och aktiva kanalerna:

```
$ lncli pendingchannels
$ lncli listchannels
```


För att betala en blixt Invoice:

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


För att ta emot en betalning skapar du en Invoice för ett visst belopp:

```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


För att se information om min nod:

```
$ lncli getinfo
```


Den fullständiga listan över kommandon kan ses genom att köra kommandot lncli:

```
$ lncli
```


Slutligen, för att göra anrop till LND API:

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


Slut på guiden!