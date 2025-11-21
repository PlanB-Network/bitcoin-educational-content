---
name: Neutrino
description: Installasjonsveiledning for LND Neutrino
---
![image](assets/cover.webp)


## Raspberry Pi-konfigurasjon med LND


### 1. Last ned Raspberry Pi OS Lite


Du finner instruksjoner for nedlasting og installasjon av avbildningen på et micro SD-kort i Windows, Mac og Linux på [denne siden] (https://www.raspberrypi.org/software/operating-systems/).


### 2. Formater SD-kortet


Bruk Raspberry Pi Imager eller balenaEtcher.


**Symbolet `$` brukes som en ledetekst og gjør det mulig for brukeren å skrive inn kommandoer på datamaskinen, og kommandoene tolkes av bash i Linux. Symbolet `#` i begynnelsen av en linje indikerer at den følgende teksten er en kommentar.


### 3. Aktiver SSH


Før vi starter Raspberry Pi med det formaterte minnet, må vi sette den inn i en datamaskin og opprette to filer som gjør at vi kan koble oss til eksternt. Ved hjelp av kommandoen `touch` oppretter vi en tom fil i /boot-partisjonen, noe som muliggjør SSH-tilkobling ved første oppstart av det nyformaterte SD-kortet.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4. Opprett fil for Wi-Fi-tilkobling


Ved hjelp av nano-kommandoen oppretter vi filen `wpa_supplicant.conf` og begynner å redigere den direkte. I denne filen må vi kopiere wifi-konfigurasjonen, kopiere teksten mellom START og END, og endre SSID og passord for det wifi-nettverket du vil koble til.


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


### 5. Tilkobling


Deretter setter vi SD-kortet inn i Raspberry Pi og kobler Pi til strømkilden for å starte operativsystemet. Vi må identifisere den i nettverket, og mDNS-protokollen vil sannsynligvis tildele den navnet raspberrypi.local. La oss prøve å koble til via SSH.


```
$ ssh pi@raspberrypi.local
password: raspberry
```


Hvis det ikke fungerer, må vi finne ut av nettverket. La oss finne ut hvilken IP Address vi er koblet til.


```
$ ifconfig
```


Hvis det for eksempel er 192.168.0.0, bruker du nmap til å finne Pi.


```
nmap -v 192.168.0.0/24
```


Hvis vi finner en ny IP på nettverket vårt, kan vi gå inn via SSH.


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6. Konfigurer Pi


```
$ sudo raspi-config
```


- Velg alternativ (1) og endre passordet for brukeren pi.
- Vi velger alternativ (8) for å oppdatere konfigurasjonsverktøyet til den nyeste versjonen
- Vi velger alternativ (4) for å velge tidssone
- Vi velger alternativ (7) og deretter Utvid filsystem
- Avslutt


### 7. Oppdater nå operativsystemet


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8. Legg til Bitcoin-brukeren


```
$ sudo adduser bitcoin
```


### 9. Sikre rpi


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


### 10. Installer Go


Hvis du ikke bruker en raspberry pi, kan du laste ned go for your architecture [her] (https://golang.org/dl/).


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11. Kompilere og installere LND


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


### 12. Opprett LND conf-fil


Opprett LND-konfigurasjonsfilen, dette bør gjøres med brukeren 'Bitcoin'


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


### 13. LND-tjenesten autostart


For å få LND til å starte etter oppstart av rpi, må vi opprette .service-filen i systemd. Hvis vi er logget inn som Bitcoin-bruker og ønsker å bytte tilbake til pi-brukeren, skriver vi ganske enkelt "exit


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


Vi kan se loggene ved å kjøre kommandoen journalctl


```
$ sudo journalctl -f -u lnd
```


### 14. Nå starter vi LND


```
$ sudo su - bitcoin
$ lncli create
```


### 15. Legg til midler i noden


```
$ lncli newaddress p2wkh
```

Du kan nå sende btc til Address som returneres av LND.


med denne kommandoen kan du sjekke saldoen:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


Når transaksjonen er bekreftet, kan vi åpne en kanal. Hvis du ikke vet hvilken node du skal åpne kanalen med, kan du gå til 1ml.com og velge en node.


Åpne en tilkobling til en node:


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


Deretter åpner du en kanal:


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


Sjekk fondene våre:


```
$ lncli walletbalance
$ lncli channelbalance
```


Vi kan se ventende og aktive kanaler:


```
$ lncli pendingchannels
$ lncli listchannels
```


For å betale en lyn Invoice:


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


For å motta en betaling oppretter du en Invoice for et bestemt beløp:


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


For å se informasjon om noden min:


```
$ lncli getinfo
```


Den fullstendige listen over kommandoer kan du se ved å kjøre kommandoen lncli:


```
$ lncli
```


Til slutt, for å gjøre anrop til LND API:


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


Slutt på guiden!