---
name: Neutrino
description: LND Neutrino Installasjonsguide
---

# Raspberry Pi Konfigurasjon med LND

1. Last ned Raspberry Pi OS Lite

Last ned Raspberry Pi OS Lite, instruksjonene for nedlasting og installasjon av bildet på et micro SD-kort i Windows, Mac og Linux kan finnes på [denne siden](https://www.raspberrypi.org/software/operating-systems/).

2. Formater SD-kortet

Formater SD-kortet ved hjelp av Raspberry Pi Imager eller balenaEtcher.

> MERK: Symbolet `$` brukes som en ledetekst og lar brukeren skrive inn kommandoer i datamaskinen, kommandoene vil bli tolket av bash i Linux. Symbolet `#` i begynnelsen av en linje indikerer at den følgende teksten er en kommentar.

3. Aktiver SSH

Før vi starter Raspberry Pi med det formaterte minnet, må vi sette det inn i en datamaskin og opprette to filer som vil tillate oss å koble til eksternt. Ved å bruke `touch`-kommandoen, oppretter vi en tom fil i /boot-partisjonen, som aktiverer SSH-tilkobling ved første oppstart av det nylig formaterte SD-kortet.

```
# MERK: Hvis microSD-kortet har blitt montert på /media/microSD, bør kommandoen
# være $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

4. Ved å bruke nano-kommandoen

oppretter vi wpa_supplicant.conf-filen og begynner direkte å redigere den. I denne filen må vi kopiere wifi-konfigurasjonen, kopiere teksten mellom START og SLUTT, og endre SSID og passord for wifi-nettverket du ønsker å koble til.

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
------ SLUTT -------
```

5. tilkobling

Deretter setter vi SD-kortet inn i Raspberry Pi og kobler Pi til strømkilden for å starte operativsystemet. Vi trenger å identifisere det på nettverket, og mDNS-protokollen vil sannsynligvis tildele navnet raspberrypi.local til den. La oss prøve å koble til via SSH.

```
$ ssh pi@raspberrypi.local
password: raspberry
```

Hvis det ikke fungerer, må vi finne ut av nettverket. La oss finne ut IP-adressen vi er koblet til.

```
$ ifconfig
```

For eksempel, hvis det er 192.168.0.0, bruk nmap for å finne Pi.

```
nmap -v 192.168.0.0/24
```

Antar vi finner en ny IP på nettverket vårt, la oss gå inn via SSH.

```
$ ssh pi@192.168.0.30
password: raspberry
```

1. Konfigurer Pi

```
$ sudo raspi-config
```

- Velg alternativ (1) og endre passordet for brukeren pi.
- Vi velger alternativ (8) for å oppdatere konfigurasjonsverktøyet til den nyeste versjonen
- Vi velger alternativ (4) for å velge vår tidssone
- Vi velger alternativ (7) og deretter Utvid filsystem
- Avslutt

  7.- Vi oppdaterer OS

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```

8.- Vi legger til bitcoin-brukeren

```
$ sudo adduser bitcoin
```

9.- Vi sikrer rpi

```
$ sudo apt install ufw
```
```
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ sudo ufw tillate 22 kommentar 'tillate SSH fra LAN'
$ sudo ufw tillate 9735 kommentar 'tillate Lightning'
$ sudo ufw tillate 10009 kommentar 'Lightning gRPC'
$ sudo ufw aktiver
$ sudo systemctl aktiver ufw
$ sudo ufw status
$ sudo apt install fail2ban
```

```
10.- Vi installerer go: hvis du ikke bruker en raspberry pi, last ned go for din arkitektur her (https://golang.org/dl/)

```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # skal vise følgende melding 'go version go1.13.5 linux/arm'
```

11.- Vi kompilerer og installerer lnd

```
$ git clone https://github.com/lightningnetwork/lnd.git
$ cd lnd
$ make
$ make install tags="autopilotrpc chainrpc experimental invoicesrpc routerrpc signrpc walletrpc watchtowerrpc wtclientrpc"
$ sudo cp $GOPATH/bin/lnd /usr/local/bin/
$ sudo cp $GOPATH/bin/lncli /usr/local/bin/
$ lncli --version
lncli versjon 0.11.0-beta commit=v0.11.0-beta-61-g6055b00dbbcedf45cd60f12e57dc5c1a7b97746f
```

12.- Vi oppretter lnd konfigurasjonsfilen, dette bør gjøres med 'bitcoin' brukeren

```
$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf
```

```
[Application Options]
# aktiver spontane betalinger
accept-keysend=1

# Offentlig navn på noden
alias=DITT_ALIAS
# Offentlig farge i heksadesimal
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

13.- For å få LND til å starte etter rpi boot, må vi opprette .service-filen i systemd.
Hvis vi er logget inn som en bitcoin-bruker og ønsker å bytte tilbake til pi-brukeren, skriver vi bare 'exit'

```
$ exit
$ sudo nano /etc/systemd/system/lnd.service
```

```
[Unit]
Description=LND Lightning Network Daemon
After=network.target

[Service]

# Tjenesteutførelse
###################

ExecStart=/usr/local/bin/lnd


# Prosesshåndtering
####################

Type=simple
Restart=always
RestartSec=30
TimeoutSec=240
LimitNOFILE=128000

# Oppretting av katalog og tillatelser
####################################

# Kjør som bitcoin:bitcoin
User=bitcoin
Group=bitcoin

# /run/lightningd
RuntimeDirectory=lightningd
RuntimeDirectoryMode=0710

# Sikkerhetstiltak
####################

# Tilby et privat /tmp og /var/tmp.
```
```
PrivateTmp=true
# Monter /usr, /boot/ og /etc skrivebeskyttet for prosessen.
ProtectSystem=full

# Forby prosessen og alle dens barn å oppnå
# nye privilegier gjennom execve().
NoNewPrivileges=true

# Bruk et nytt /dev navnerom kun befolket med API pseudo-enheter
# som /dev/null, /dev/zero og /dev/random.
PrivateDevices=true

# Nekt opprettelsen av skrivbare og kjørbare minnekartlegginger.
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

14. Nå starter vi lnd

```
$ sudo su - bitcoin
$ lncli create
```

15. Legg til midler på vår node

```
$ lncli newaddress p2wkh
```

Send btc til adressen returnert av lnd

For å sjekke saldoen

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

Deretter åpner du en kanal

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```

Sjekk våre midler

```
$ lncli walletbalance
$ lncli channelbalance
```

Vi kan se de ventende og aktive kanalene

```
$ lncli pendingchannels
$ lncli listchannels
```

For å betale en lightning-faktura

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```

For å motta en betaling, opprett en faktura for et spesifikt beløp

```
$ lncli addinvoice --memo 'min første betaling på LN' --amt 100
```

For å se informasjon om min node

```
$ lncli getinfo
```

Den komplette listen over kommandoer kan sees ved å enkelt kjøre lncli

```
$ lncli
```

Til slutt, for å gjøre kall til lnd API

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```

> SLUTT