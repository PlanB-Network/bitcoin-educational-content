---
name: Neutrino
description: LND Neutrino paigaldusjuhend
---
![image](assets/cover.webp)


## Raspberry Pi konfiguratsioon koos LND-ga


### 1. Lae alla Raspberry Pi OS Lite


Juhised kujutise allalaadimiseks ja paigaldamiseks micro SD-kaardile Windowsis, Macis ja Linuxis leiate [sellel leheküljel](https://www.raspberrypi.org/software/operating-systems/).


### 2. SD-kaardi vormindamine


Kasutage Raspberry Pi Imager või balenaEtcher.


**Märkus:** Sümbolit `$` kasutatakse käsureana ja see võimaldab kasutajal sisestada arvutisse käske, mida Linuxis tõlgendab bash. Sümbol `#` rea alguses näitab, et järgnev tekst on kommentaar.


### 3. SSH lubamine


Enne Raspberry Pi käivitamist koos vormindatud mäluga peame selle arvutisse sisestama ja looma kaks faili, mis võimaldavad meil kaugühendust luua. Kasutades käsku `touch`, loome tühja faili partitsiooni /boot, mis võimaldab SSH-ühendust värskelt vormindatud SD-kaardi esimesel käivitamisel.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4. Wi-Fi ühenduse faili loomine


Kasutades käsku nano, loome faili `wpa_supplicant.conf` ja hakkame seda otse redigeerima. Selles failis peame kopeerima wifi konfiguratsiooni, kopeerides teksti START ja END vahele ning muutes selle wifi SSID ja parooli, millega soovite ühendust luua.


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


### 5. Ühendus


Seejärel sisestame SD-kaardi Raspberry Pi-sse ja ühendame Pi vooluallikaga, et käivitada operatsioonisüsteem. Me peame selle võrgus identifitseerima ja mDNS-protokoll määrab sellele tõenäoliselt nime raspberrypi.local. Proovime ühendust luua SSH kaudu.


```
$ ssh pi@raspberrypi.local
password: raspberry
```


Kui see ei tööta, peame välja selgitama võrgu. Uurime välja IP Address, millega oleme ühendatud.


```
$ ifconfig
```


Näiteks kui see on 192.168.0.0, siis kasutage nmap, et leida Pi.


```
nmap -v 192.168.0.0/24
```


Eeldades, et leiame uue IP-aadressi meie võrgus, siseneme SSH kaudu.


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6. Pi seadistamine


```
$ sudo raspi-config
```


- Valige valik (1) ja muutke kasutaja pi parool.
- Valime võimaluse (8), et uuendada konfiguratsioonivahend viimasele versioonile
- Valime võimaluse (4), et valida meie ajavöönd
- Valime valiku (7) ja seejärel laiendame failisüsteemi
- Lõpeta


### 7. Nüüd värskendage operatsioonisüsteemi


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8. Bitcoin kasutaja lisamine


```
$ sudo adduser bitcoin
```


### 9. Tagada rpi


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


### 10. Paigalda Go


Kui te ei kasuta raspberry pi-d, laadige alla oma arhitektuuri jaoks [siin](https://golang.org/dl/).


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11. LND kompileerimine ja paigaldamine


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


### 12. LND conf faili loomine


Luua LND konfiguratsioonifail, seda tuleks teha kasutajaga "Bitcoin"


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


### 13. LND teenuse automaatne käivitamine


Selleks, et LND käivituks pärast rpi käivitamist, peame looma süsteemisüsteemis .service faili. Kui me oleme sisse logitud Bitcoin kasutajana ja tahame minna tagasi pi kasutajaks, siis kirjutame lihtsalt 'exit'


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


Me saame vaadata logisid, käivitades käsu journalctl


```
$ sudo journalctl -f -u lnd
```


### 14. Nüüd alustame LND


```
$ sudo su - bitcoin
$ lncli create
```


### 15. Lisage sõlme rahalised vahendid


```
$ lncli newaddress p2wkh
```

Nüüd saate saata btc-d Address-le, mille LND on tagastanud.


selle käsuga saate kontrollida tasakaalu:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


Kui tehing on kinnitatud, saame avada kanali. Kui te ei tea, millise sõlme kaudu kanal avada, võite minna veebilehele 1ml.com ja valida sõlme.


Avage ühendus sõlme jaoks:


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


Seejärel avage kanal:


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


Kontrollige meie vahendeid:


```
$ lncli walletbalance
$ lncli channelbalance
```


Saame vaadata ootavaid ja aktiivseid kanaleid:


```
$ lncli pendingchannels
$ lncli listchannels
```


Tasuda välk Invoice:


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


Makse saamiseks looge Invoice konkreetse summa jaoks:


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


Minu sõlme kohta käiva teabe vaatamiseks:


```
$ lncli getinfo
```


Täieliku käskude nimekirja saab näha, kui käivitada käsk lncli:


```
$ lncli
```


Lõpuks, et teha kutsed LND API-le:


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


Juhendi lõpp!