---
name: Neutrino
description: LND Neutrino asennusopas
---

# Raspberry Pi -konfigurointi LND:n kanssa

1. Lataa Raspberry Pi OS Lite

Lataa Raspberry Pi OS Lite, ohjeet kuvatiedoston lataamiseen ja asentamiseen microSD-kortille Windowsissa, Macissa ja Linuxissa löytyvät [tältä sivulta](https://www.raspberrypi.org/software/operating-systems/).

2. Alusta SD-kortti

Alusta SD-kortti käyttäen Raspberry Pi Imageria tai balenaEtcheria.

> HUOM: Symbolia `$` käytetään kehotteena, joka sallii käyttäjän syöttää komentoja tietokoneeseen, komentoja tulkitaan bashissa Linuxissa. Rivin alussa oleva symboli `#` osoittaa, että seuraava teksti on kommentti.

3. Ota SSH käyttöön

Ennen kuin aloitamme Raspberry Pin käyttämisen alustetulla muistilla, meidän on lisättävä siihen kaksi tiedostoa, jotka mahdollistavat etäyhteyden muodostamisen. Käyttämällä `touch`-komentoa, luomme tyhjän tiedoston /boot-osioon, joka mahdollistaa SSH-yhteyden ensimmäisellä käynnistyksellä tuoreesti alustetulle SD-kortille.

```
# HUOM: Jos microSD-kortti on liitetty kohteeseen /media/microSD, komennon
# tulisi olla $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

4. Käyttäen nano-komentoa

luomme wpa_supplicant.conf-tiedoston ja aloitamme sen muokkaamisen suoraan. Tähän tiedostoon meidän on kopioitava wifi-konfiguraatio, kopioimalla teksti START ja END väliltä, ja muokkaamalla haluamasi wifin SSID ja salasana.

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

5. Yhteys

Tämän jälkeen asetamme SD-kortin Raspberry Pi:hin ja yhdistämme Pi:n virtalähteeseen käynnistääksemme käyttöjärjestelmän. Meidän on tunnistettava se verkossa, ja mDNS-protokolla todennäköisesti antaa sille nimen raspberrypi.local. Yritetään yhdistää SSH:n kautta.

```
$ ssh pi@raspberrypi.local
salasana: raspberry
```

Jos se ei toimi, meidän on selvitettävä verkko. Selvitetään mihin IP-osoitteeseen olemme yhdistetty.

```
$ ifconfig
```

Esimerkiksi, jos se on 192.168.0.0, käytä nmapia löytääksesi Pi:n.

```
nmap -v 192.168.0.0/24
```

Olettaen, että löydämme uuden IP:n verkostamme, yritetään kirjautua sisään SSH:n kautta.

```
$ ssh pi@192.168.0.30
salasana: raspberry
```

1. Konfiguroi Pi

```
$ sudo raspi-config
```

- Valitse vaihtoehto (1) ja vaihda käyttäjän pi salasana.
- Valitsemme vaihtoehdon (8) päivittääksemme konfigurointityökalun uusimpaan versioon
- Valitsemme vaihtoehdon (4) valitaksemme aikavyöhykkeemme
- Valitsemme vaihtoehdon (7) ja sitten Laajenna tiedostojärjestelmä
- Lopeta

  7.- Päivitämme käyttöjärjestelmän

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```

8.- Lisäämme bitcoin-käyttäjän

```
$ sudo adduser bitcoin
```

9.- Turvaamme rpi:n

```
$ sudo apt install ufw
```
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ sudo ufw allow 22 comment 'salli SSH LAN:sta'
$ sudo ufw allow 9735 comment 'salli Lightning'
$ sudo ufw allow 10009 comment 'Lightning gRPC'
$ sudo ufw enable
$ sudo systemctl enable ufw
$ sudo ufw status
$ sudo apt install fail2ban
```

```
10.- Asennamme go:n: jos et käytä raspberry pi:tä, lataa go arkkitehtuurillesi täältä (https://golang.org/dl/)

```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # pitäisi näyttää seuraava viesti 'go version go1.13.5 linux/arm'
```

```
11.- Käännämme ja asennamme lnd:n

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

```
12.- Luomme lnd:n konfiguraatiotiedoston, tämä tulisi tehdä 'bitcoin'-käyttäjänä

```
$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf
```

```
[Application Options]
# ota vastaan spontaanit maksut
accept-keysend=1

# solmun julkinen nimi
alias=SINUN_ALIAS
# julkinen väri heksadesimaalina
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

```
13.- Jotta LND käynnistyisi rpi:n bootin jälkeen, meidän täytyy luoda .service-tiedosto systemd:lle.
Jos olemme kirjautuneet sisään bitcoin-käyttäjänä ja haluamme vaihtaa takaisin pi-käyttäjään, kirjoitamme vain 'exit'

```
$ exit
$ sudo nano /etc/systemd/system/lnd.service
```

```
[Unit]
Description=LND Lightning Network Daemon
After=network.target

[Service]

# Palvelun suoritus
###################

ExecStart=/usr/local/bin/lnd


# Prosessinhallinta
####################

Type=simple
Restart=always
RestartSec=30
TimeoutSec=240
LimitNOFILE=128000

# Hakemiston luonti ja oikeudet
################################

# Suorita bitcoin:bitcoin käyttäjänä
User=bitcoin
Group=bitcoin

# /run/lightningd
RuntimeDirectory=lightningd
RuntimeDirectoryMode=0710

# Turvatoimet
#############

# Tarjoa yksityinen /tmp ja /var/tmp.
```
```
PrivateTmp=true
# Liitä /usr, /boot/ ja /etc vain luku -tilassa prosessille.
ProtectSystem=full

# Estä prosessia ja sen kaikkia lapsiprosesseja saamasta
# uusia oikeuksia execve()-komennon kautta.
NoNewPrivileges=true

# Käytä uutta /dev nimiavaruutta, joka sisältää vain API:n pseudo-laitteita
# kuten /dev/null, /dev/zero ja /dev/random.
PrivateDevices=true

# Kiellä kirjoitettavien ja suoritettavien muistialueiden luominen.
MemoryDenyWriteExecute=true

[Install]
WantedBy=multi-user.target
```

```
$ sudo systemctl enable lnd
$ sudo systemctl start lnd
$ systemctl status lnd
```

Lokien tarkastelu komennolla journalctl

```
$ sudo journalctl -f -u lnd
```

14. Nyt käynnistämme lnd:n

```
$ sudo su - bitcoin
$ lncli create
```

15. Lisää varoja solmuun

```
$ lncli newaddress p2wkh
```

Lähetä btc osoitteeseen, jonka lnd palauttaa

Tarkista saldo

```
$ lncli walletbalance
{
    "total_balance": "500000",
    "confirmed_balance": "0",
    "unconfirmed_balance": "500000"
}
```

Kun siirto on vahvistettu, voimme avata kanavan. Jos et tiedä, minkä solmun kanssa kanavan avaisit, voit mennä osoitteeseen 1ml.com ja valita solmun.

Avaa yhteys solmuun:

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```

Avaa sen jälkeen kanava

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```

Tarkista varat

```
$ lncli walletbalance
$ lncli channelbalance
```

Voimme tarkastella odottavia ja aktiivisia kanavia

```
$ lncli pendingchannels
$ lncli listchannels
```

Maksamaan lightning-laskun

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```

Vastaanottaaksesi maksun, luo lasku tiettyä summaa varten

```
$ lncli addinvoice --memo 'ensimmäinen maksuni LN:ssä' --amt 100
```

Nähdäksesi tietoja solmustani

```
$ lncli getinfo
```

Koko komentolista näkyy yksinkertaisesti suorittamalla lncli

```
$ lncli
```

Lopuksi, tehdäksesi kutsuja lnd API:lle

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```

> LOPPU