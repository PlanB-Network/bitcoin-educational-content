# Raspberry Pi-konfiguration med LND

1. Ladda ner Raspberry Pi OS Lite

Ladda ner Raspberry Pi OS Lite. Instruktioner för nedladdning och installation av bilden på ett micro SD-kort för Windows, Mac och Linux finns på [den här sidan](https://www.raspberrypi.org/software/operating-systems/).

2. Formatera SD-kortet

Formatera SD-kortet med hjälp av Raspberry Pi Imager eller balenaEtcher.

> OBS: Symbolen `$` används som en prompt och låter användaren mata in kommandon i datorn. Kommandona tolkas av bash i Linux. Symbolen `#` i början av en rad indikerar att följande text är en kommentar.

3. Aktivera SSH

Innan vi startar Raspberry Pi med det formaterade minnet måste vi sätta in det i en dator och skapa två filer som gör att vi kan ansluta oss på distans. Med hjälp av kommandot `touch` skapar vi en tom fil i /boot-partitionen, vilket aktiverar SSH-anslutning vid första uppstarten av det nyformaterade SD-kortet.

```
# OBS: Om microSD-kortet har monterats på /media/microSD ska kommandot vara
# $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

4. Använda kommandot nano

Vi skapar filen wpa_supplicant.conf och börjar redigera den direkt. I denna fil måste vi kopiera wifi-konfigurationen genom att kopiera texten mellan START och END, och ändra SSID och lösenord för det wifi-nätverk du vill ansluta till.

```
$ nano /boot/wpa_supplicant.conf

------ START -------
country=se
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
 ssid="MittNätverkSSID"
 psk="lösenord"
}
------ END -------
```

5. Anslutning

Sätt sedan in SD-kortet i Raspberry Pi och anslut Pi till strömkällan för att starta operativsystemet. Vi behöver identifiera den på nätverket, och sannolikt kommer mDNS-protokollet att tilldela namnet raspberrypi.local till den. Låt oss försöka ansluta via SSH.

```
$ ssh pi@raspberrypi.local
lösenord: raspberry
```

Om det inte fungerar måste vi ta reda på nätverket. Låt oss ta reda på IP-adressen vi är anslutna till.

```
$ ifconfig
```

Om det till exempel är 192.168.0.0 använder vi nmap för att hitta Pi.

```
nmap -v 192.168.0.0/24
```

Antag att vi hittar en ny IP-adress i vårt nätverk, låt oss ansluta via SSH.

```
$ ssh pi@192.168.0.30
lösenord: raspberry
```

6. Konfigurera Pi

```
$ sudo raspi-config
```

- Välj alternativ (1) och ändra lösenordet för användaren pi.
- Välj alternativ (8) för att uppdatera konfigurationsverktyget till den senaste versionen.
- Välj alternativ (4) för att välja vår tidszon.
- Välj alternativ (7) och sedan Expandera filsystem.
- Slutför

7. Uppdatera operativsystemet

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```

8. Lägg till användaren bitcoin

```
$ sudo adduser bitcoin
```

9. Säkra rpi

```
$ sudo apt install ufw
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ sudo ufw allow 22 comment 'tillåt SSH från LAN'
$ sudo ufw allow 9735 comment 'tillåt Lightning'
$ sudo ufw allow 10009 comment 'Lightning gRPC'
$ sudo ufw enable
$ sudo systemctl enable ufw
$ sudo ufw status
$ sudo apt install fail2ban

10.- Vi installerar go: om du inte använder en Raspberry Pi, ladda ner go för din arkitektur här (https://golang.org/dl/)

$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # bör visa följande meddelande 'go version go1.13.5 linux/arm'

11.- Vi kompilerar och installerar lnd

$ git clone https://github.com/lightningnetwork/lnd.git
$ cd lnd
$ make
$ make install tags="autopilotrpc chainrpc experimental invoicesrpc routerrpc signrpc walletrpc watchtowerrpc wtclientrpc"
$ sudo cp $GOPATH/bin/lnd /usr/local/bin/
$ sudo cp $GOPATH/bin/lncli /usr/local/bin/
$ lncli --version
lncli version 0.11.0-beta commit=v0.11.0-beta-61-g6055b00dbbcedf45cd60f12e57dc5c1a7b97746f

12.- Vi skapar konfigurationsfilen för lnd, detta bör göras med användaren 'bitcoin'

$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf

[Application Options]
# aktivera spontana betalningar
accept-keysend=1

# Offentligt namn på noden
alias=DITT_ALIAS
# Offentlig färg i hexadecimalt format
color=#000000
debuglevel=info
maxpendingchannels=5
listen=localhost
# gRPC-socket
rpclisten=0.0.0.0:10009

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=neutrino

[neutrino]
neutrino.connect=bb2.breez.technology

13.- För att få LND att starta efter rpi-start måste vi skapa .service-filen i systemd.
Om vi är inloggade som användaren 'bitcoin' och vill byta tillbaka till användaren 'pi', skriver vi helt enkelt 'exit'

$ exit
$ sudo nano /etc/systemd/system/lnd.service

[Unit]
Description=LND Lightning Network Daemon
After=network.target

[Service]

# Körning av tjänsten
###################

ExecStart=/usr/local/bin/lnd


# Processhantering
####################

Type=simple
Restart=always
RestartSec=30
TimeoutSec=240
LimitNOFILE=128000

# Skapande av kataloger och behörigheter
####################################

# Kör som bitcoin:bitcoin
User=bitcoin
Group=bitcoin

# /run/lightningd
RuntimeDirectory=lightningd
RuntimeDirectoryMode=0710

# Härdat skydd
####################

# Tillhandahåll en privat /tmp och /var/tmp.
PrivateTmp=true
# Montera /usr, /boot/ och /etc som skrivskyddade för processen.
ProtectSystem=full

# Förhindra att processen och alla dess barn får
# nya privilegier genom execve().
NoNewPrivileges=true

# Använd ett nytt /dev-utrymme som bara är fyllt med API-pseudoenheter
# som /dev/null, /dev/zero och /dev/random.
PrivateDevices=true

# Förneka skapandet av minnesmappningar som är skrivbara och körbara.
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

14. Nu startar vi lnd

```
$ sudo su - bitcoin
$ lncli create
```

15. Lägg till medel till vår nod

```
$ lncli newaddress p2wkh
```

Skicka btc till adressen som returneras av lnd

För att kontrollera saldot

```
$ lncli walletbalance
{
    "total_balance": "500000",
    "confirmed_balance": "0",
    "unconfirmed_balance": "500000"
}
```

När transaktionen har bekräftats kan vi öppna en kanal. Om du inte vet vilken nod du ska öppna kanalen med kan du gå till 1ml.com och välja en nod.

Öppna en anslutning till en nod:

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```

Öppna sedan en kanal

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```

Kontrollera våra medel

```
$ lncli walletbalance
$ lncli channelbalance
```

Vi kan visa de väntande och aktiva kanalerna

```
$ lncli pendingchannels
$ lncli listchannels
```

För att betala en lightning-faktura

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```

För att ta emot en betalning, skapa en faktura för en specifik summa

```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```

För att visa information om min nod

```
$ lncli getinfo
```

Den kompletta listan över kommandon kan ses genom att helt enkelt köra lncli

```
$ lncli
```

Slutligen, för att göra anrop till lnd API

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```

> SLUT
