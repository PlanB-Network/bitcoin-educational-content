---
name: Neutrino
description: Vodič za instalaciju LND Neutrino
---

# Konfiguracija Raspberry Pi sa LND


#### 1. Preuzmite Raspberry Pi OS Lite

Uputstva za preuzimanje i instalaciju slike na micro SD karticu u Windows, Mac i Linux operativnim sistemima možete pronaći na [ovoj stranici](https://www.raspberrypi.org/software/operating-systems/).


#### 2. Formatiraj SD karticu

koristite Raspberry Pi Imager ili balenaEtcher.


**Napomena:** Simbol `$` se koristi kao prompt i omogućava korisniku da unosi komande u računar, komande će biti interpretirane od strane bash-a u Linux-u. Simbol `#` na početku linije označava da je sledeći tekst komentar.


#### 3. Omogući SSH


Pre nego što pokrenemo Raspberry Pi sa formatiranom memorijom, moramo je umetnuti u računar i kreirati dve datoteke koje će nam omogućiti daljinsko povezivanje. Koristeći komandu `touch`, kreiramo praznu datoteku u /boot particiji, omogućavajući SSH povezivanje pri prvom pokretanju sveže formatirane SD kartice.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

#### 4. Kreiraj datoteku za Wi-Fi konekciju

Koristeći nano komandu kreiramo `wpa_supplicant.conf` fajl i direktno počinjemo sa uređivanjem. U ovaj fajl treba da kopiramo wifi konfiguraciju, kopirajući tekst između START i END, i menjajući SSID i lozinku wifi mreže na koju želite da se povežete.


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


#### 5. Konekcija

Zatim, ubacujemo SD karticu u Raspberry Pi i povezujemo Pi sa izvorom napajanja kako bismo pokrenuli operativni sistem. Potrebno je da ga identifikujemo na mreži, a mDNS protokol će verovatno dodeliti ime raspberrypi.local. Pokušajmo da se povežemo putem SSH.

```
$ ssh pi@raspberrypi.local
password: raspberry
```

Ako ne radi, moramo saznati mrežu. Hajde da saznamo IP Address na koji smo povezani.


```
$ ifconfig
```


Na primer, ako je 192.168.0.0, koristi nmap da pronađeš Pi.


```
nmap -v 192.168.0.0/24
```


Pod pretpostavkom da pronađemo novi IP na našoj mreži, uđimo putem SSH.


```
$ ssh pi@192.168.0.30
password: raspberry
```


#### 6. Konfigurišite Pi

```
$ sudo raspi-config
```


- Odaberite opciju (1) i promenite lozinku za korisnika pi.
- Odabiremo opciju (8) za ažuriranje alata za konfiguraciju na najnoviju verziju.
- Biramo opciju (4) da bismo izabrali našu vremensku zonu
- Odaberemo opciju (7) i zatim Proširi datotečni sistem
- Završi


#### 7. Sada ažurirajte OS

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


#### 8. Dodaj korisnika Bitcoin

```
$ sudo adduser bitcoin
```


#### 9. Osiguraj rpi


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


#### 10. Instaliraj Go

Ako ne koristite Raspberry Pi, preuzmite Go za vašu arhitekturu [ovde](https://golang.org/dl/)


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


#### 11. Kompajliraj i instaliraj LND


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


#### 12. Kreiraj LND conf datoteku

Kreirajte LND konfiguracionu datoteku, ovo treba uraditi sa 'Bitcoin' korisnikom.


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


#### 13. LND servis automatsko pokretanje

Da bi LND počeo nakon pokretanja rpi, moramo kreirati .service datoteku u systemd. Ako smo prijavljeni kao korisnik Bitcoin i želimo se vratiti na pi korisnika, jednostavno upišemo 'exit'


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


Možemo pregledati logove pokretanjem komande journalctl


```
$ sudo journalctl -f -u lnd
```


#### 14. Sada počinjemo LND


```
$ sudo su - bitcoin
$ lncli create
```


#### 15. Dodajte sredstva čvoru


```
$ lncli newaddress p2wkh
```

Sada možete poslati btc na Address koji je vratio LND.


sa ovom komandom možete proveriti stanje:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


Kada transakcija bude potvrđena, možemo otvoriti kanal. Ako ne znate sa kojim čvorom da otvorite kanal, možete otići na 1ml.com i izabrati čvor.


Otvorite vezu sa čvorom:

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


Zatim otvorite kanal:

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


Proverite naša sredstva:

```
$ lncli walletbalance
$ lncli channelbalance
```


Možemo pregledati kanale na čekanju i aktivne kanale:

```
$ lncli pendingchannels
$ lncli listchannels
```


Da platite lightning Invoice:

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


Da biste primili uplatu, kreirajte Invoice za određeni iznos:

```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


Da biste videli informacije o mom čvoru:

```
$ lncli getinfo
```


Potpuna lista komandi može se videti jednostavnim pokretanjem komande lncli:

```
$ lncli
```


Konačno, za upućivanje poziva na LND API:

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


KRAJ vodiča!