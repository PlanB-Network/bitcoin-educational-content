---
name: Neutrino
description: Inyigisho yo gushiramwo LND Neutrino
---
![image](assets/cover.webp)


## Itunganywa rya Raspberry Pi na LND.


### 1. Gukuraho Raspberry Pi OS Lite


Amabwirizwa yo gukura no gushiramwo ishusho ku ikarita ya micro SD muri Windows, Mac, na Linux urashobora kuyasanga kuri [iyi paji](https://www.raspberrypi.org/porogarama/imirongo-ikoreshwa/).


### 2. Guhindura ikarita SD


Koresha igishushanyo ca Raspberry Pi canke balenaEtcher.


**Iciyumviro:** Ikimenyetso `$` gikoreshwa nk'ikimenyetso kandi kiremerera uwukoresha kwinjiza amabwirizwa muri mudasobwa, amabwirizwa azosobanurwa na bash muri Linux. Ikimenyetso `#` kiri mu ntango y'umurongo kigaragaza ko icanditswe gikurikira ari igisobanuro.


### 3. Gushoboza SSH


Imbere yo gutangura Raspberry Pi n’ubuhinga bwo kwibuka bufise ubuhinga, dutegerezwa kuyishira muri mudasobwa maze tugakora amadosiye abiri azotuma dushobora gukorana kure. Dukoresheje itegeko rya `touch`, dukora dosiye y'ubusa mu gice ca /boot, bishoboza gukorana na SSH ku gutangura kwa mbere kw'ikarita SD iherutse guhindurwa.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4. Rema dosiye yo guhuza Wi-Fi


Dukoresheje itegeko rya nano dukora dosiye `wpa_supplicant.conf` maze tugatangura kuyihindura. Muri iyi dosiye, turakeneye gukopa configuration ya wifi, gukopa umwandiko uri hagati ya START na END, no guhindura SSID na password ya wifi ushaka kwifatanya nayo.


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


### 5. Uguhuza


Hanyuma, twinjiza ikarata SD muri Raspberry Pi maze tugafatanya Pi n’inkomoko y’ububasha kugira ngo dutangure gukoresha. Turakeneye kuyimenya ku rubuga, kandi mDNS porotokole izoshobora kuyiha izina raspberrypi.local. Reka tugerageze gufatanya biciye kuri SSH.


```
$ ssh pi@raspberrypi.local
password: raspberry
```


Nivyaba bitagenda neza, turakeneye kumenya uruja n’uruza. Reka tumenye IP Address dufatanye nayo.


```
$ ifconfig
```


Nk’akarorero, nimba ari 192.168.0.0, koresha nmap kugira uronke Pi.


```
nmap -v 192.168.0.0/24
```


Dufate ko turonka IP nshasha ku rubuga rwacu, reka twinjire biciye kuri SSH.


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6. Gutegura Pi .


```
$ sudo raspi-config
```


- Hitamwo uburyo (1) maze uhindure ijambobanga ry’ukoresha pi.
- Duhitamwo uburyo (8) kugira ngo duhindure igikoresho co gutunganya kuri verisiyo nshasha
- Duhitamwo uburyo (4) kugira ngo duhitemwo isaha yacu
- Duhitamwo uburyo (7) hanyuma tugaca twagura urutonde rw'amadosiye
- Guheraheza


### 7. Ubu rero hindura OS .


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8. Wongereko umukoresha wa Bitcoin


```
$ sudo adduser bitcoin
```


### 9. Gukingira rpi .


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


### 10. Shiraho Go


Niba udakoresha pi y’umukara, fungura genda ku bw’ubwubatsi bwawe [hano](https://golang.org/dl/).


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11. Gukoranya no gushiramwo LND.


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


### 12. Rema dosiye ya conf ya LND


Rema dosiye y'imiterere ya LND, ibi bikwiye gukorwa n'ukoresha 'Bitcoin'


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


### 13. LND igikorwa gitangura ubwaco


Kugira ngo LND itangure inyuma y’ugufungura kwa rpi, dutegerezwa gukora dosiye .service muri systemd. Iyo twinjiye nk'umukoresha wa Bitcoin kandi dushaka gusubira ku mukoresha wa pi, twandika gusa 'exit'.


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


Turashobora kubona inyandiko dukoresheje itegeko journalctl


```
$ sudo journalctl -f -u lnd
```


### 14. Ubu rero turatangura LND.


```
$ sudo su - bitcoin
$ lncli create
```


### 15. Wongere amafaranga ku nzira


```
$ lncli newaddress p2wkh
```

Ubu ushobora kohereza btc kuri Address yagaruwe na LND.


n'iri tegeko, ushobora kugenzura umubare:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


Iyo amafaranga yemejwe, turashobora gufungura umurongo. Niba utazi node yo gufungura umurongo, ushobora kuja kuri 1ml.com ugahitamwo node.


Gufungura ihuriro ku nzira:


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


Hanyuma ufungure umurongo:


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


Suzuma amafranga yacu:


```
$ lncli walletbalance
$ lncli channelbalance
```


Turashobora kubona imirongo irindiriye n'ikora:


```
$ lncli pendingchannels
$ lncli listchannels
```


Kugira ngo wishyure umuravyo Invoice:


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


Kugira ngo uronke amahera, nushireho Invoice y’amahera yihariye:


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


Kugira ngo ubone amakuru yerekeye urudodo rwanje:


```
$ lncli getinfo
```


Urutonde rw'amabwirizwa rwose rushobora kubonwa mu gukoresha gusa itegeko rya lncli:


```
$ lncli
```


Ubwa nyuma, kugira ngo uhamagare kuri LND API:


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


IMPERUKA y’uburongozi!