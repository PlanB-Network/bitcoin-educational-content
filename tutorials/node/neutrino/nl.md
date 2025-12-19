---
name: Neutrino
description: LND Neutrino Installatiegids
---
![image](assets/cover.webp)


## Raspberry Pi configuratie met LND


### 1. Raspberry Pi OS Lite downloaden


De instructies voor het downloaden en installeren van het image op een micro SD-kaart in Windows, Mac en Linux zijn te vinden op [deze pagina](https://www.raspberrypi.org/software/operating-systems/).


### 2. De SD-kaart formatteren


Gebruik Raspberry Pi Imager of balenaEtcher.


**Noot:** Het symbool `$` wordt gebruikt als prompt en stelt de gebruiker in staat om commando's in te voeren in de computer, de commando's zullen worden geïnterpreteerd door bash in Linux. Het symbool `#` aan het begin van een regel geeft aan dat de volgende tekst commentaar is.


### 3. SSH inschakelen


Voordat we de Raspberry Pi opstarten met het geformatteerde geheugen, moeten we het in een computer plaatsen en twee bestanden aanmaken waarmee we op afstand verbinding kunnen maken. Met het `touch` commando maken we een leeg bestand aan in de /boot partitie, waardoor SSH-verbinding mogelijk wordt bij de eerste keer opstarten van de pas geformatteerde SD-kaart.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4. Bestand maken voor Wi-Fi-verbinding


Met het commando nano maken we het bestand `wpa_supplicant.conf` aan en beginnen we direct met bewerken. In dit bestand moeten we de wifi-configuratie kopiëren, de tekst tussen START en END kopiëren en het SSID en wachtwoord wijzigen van de wifi waarmee je verbinding wilt maken.


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


### 5. Aansluiting


Vervolgens plaatsen we de SD-kaart in de Raspberry Pi en sluiten we de Pi aan op de stroombron om het besturingssysteem te starten. We moeten de Pi identificeren op het netwerk en het mDNS-protocol zal er waarschijnlijk de naam raspberrypi.local aan toewijzen. Laten we proberen verbinding te maken via SSH.


```
$ ssh pi@raspberrypi.local
password: raspberry
```


Als het niet werkt, moeten we het netwerk achterhalen. Laten we eens kijken met welk IP Address we verbonden zijn.


```
$ ifconfig
```


Als het bijvoorbeeld 192.168.0.0 is, gebruik dan nmap om de Pi te vinden.


```
nmap -v 192.168.0.0/24
```


Ervan uitgaande dat we een nieuw IP-adres op ons netwerk vinden, gaan we naar binnen via SSH.


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6. De Pi configureren


```
$ sudo raspi-config
```


- Selecteer optie (1) en wijzig het wachtwoord voor de gebruiker pi.
- We selecteren optie (8) om de configuratietool bij te werken naar de nieuwste versie
- We selecteren optie (4) om onze tijdzone te selecteren
- We selecteren optie (7) en vervolgens Bestandssysteem uitvouwen
- Afwerking


### 7. Werk nu het OS bij


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8. De Bitcoin gebruiker toevoegen


```
$ sudo adduser bitcoin
```


### 9. De rpi beveiligen


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


### 10. Installeer Go


Als je geen raspberry pi gebruikt, download dan go voor jouw architectuur [hier](https://golang.org/dl/).


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11. LND compileren en installeren


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


### 12. LND conf-bestand aanmaken


Maak het LND configuratiebestand, dit moet gedaan worden met de 'Bitcoin' gebruiker


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


### 13. LND service autostart


Om LND te laten starten na het opstarten van de rpi, moeten we het .service bestand in systemd aanmaken. Als we ingelogd zijn als Bitcoin gebruiker en terug willen naar de pi gebruiker, typen we simpelweg 'exit'


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


We kunnen de logs bekijken door het commando journalctl uit te voeren


```
$ sudo journalctl -f -u lnd
```


### 14. Nu beginnen we met LND


```
$ sudo su - bitcoin
$ lncli create
```


### 15. Geld toevoegen aan het knooppunt


```
$ lncli newaddress p2wkh
```

Je kunt nu btc sturen naar Address, teruggestuurd door LND.


met dit commando kun je de balans controleren:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


Zodra de transactie is bevestigd, kunnen we een chatroom openen. Als je niet weet met welk knooppunt je de chatroom moet openen, kun je naar 1ml.com gaan en een knooppunt kiezen.


Open een verbinding met een knooppunt:


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


Open dan een kanaal:


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


Bekijk onze fondsen:


```
$ lncli walletbalance
$ lncli channelbalance
```


We kunnen de in behandeling zijnde en actieve kanalen bekijken:


```
$ lncli pendingchannels
$ lncli listchannels
```


Een bliksemschicht Invoice betalen:


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


Om een betaling te ontvangen, maak je een Invoice aan voor een specifiek bedrag:


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


Om informatie over mijn knooppunt te bekijken:


```
$ lncli getinfo
```


De volledige lijst met commando's kan worden bekeken door simpelweg het commando lncli uit te voeren:


```
$ lncli
```


Tot slot, om aanroepen te doen naar de LND API:


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


EINDE van de gids!