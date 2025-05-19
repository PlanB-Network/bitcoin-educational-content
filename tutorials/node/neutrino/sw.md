---
name: Neutrino
description: Mwongozo wa Ufungaji wa LND Neutrino
---

# Usanidi wa Raspberry Pi na LND


#### 1. Pakua Raspberry Pi OS Lite

Maagizo ya kupakua na kusakinisha picha kwenye kadi ndogo ya SD katika Windows, Mac, na Linux yanaweza kupatikana kwenye [ukurasa huu](https://www.raspberrypi.org/software/operating-systems/).


#### 2. Fomati Kadi ya SD

tumia Raspberry Pi Imager au balenaEtcher.


**Kumbuka:** Alama ya `$` inatumika kama kidokezo na inaruhusu mtumiaji kuingiza amri kwenye kompyuta, amri zitafasiriwa kwa bash katika Linux. Alama `#` mwanzoni mwa mstari inaonyesha kuwa maandishi yafuatayo ni maoni.


#### 3. Wezesha SSH


Kabla ya kuanza Raspberry Pi na kumbukumbu iliyopangwa, lazima tuiweke kwenye kompyuta na kuunda faili mbili ambazo zitaturuhusu kuunganisha kwa mbali. Kwa kutumia amri ya `gusa`, tunaunda faili tupu katika kizigeu cha /boot, kuwezesha muunganisho wa SSH kwenye buti ya kwanza ya kadi ya SD iliyoumbizwa upya.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

#### 4. Unda faili kwa uunganisho wa Wi-Fi

Kwa kutumia amri ya nano tunaunda faili ya `wpa_supplicant.conf` na kuanza kuihariri moja kwa moja. Katika faili hii, tunahitaji kunakili usanidi wa wifi, kunakili maandishi kati ya START na END, na kurekebisha SSID na nenosiri la wifi unayotaka kuunganisha.


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


#### 5. Muunganisho

Kisha, tunaingiza kadi ya SD kwenye Raspberry Pi na kuunganisha Pi kwenye chanzo cha nguvu ili kuanza mfumo wa uendeshaji. Tunahitaji kuitambua kwenye mtandao, na itifaki ya mDNS itawezekana kuipa jina raspberrypi.local kwake. Wacha tujaribu kuunganishwa kupitia SSH.

```
$ ssh pi@raspberrypi.local
password: raspberry
```

Ikiwa haifanyi kazi, tunahitaji kujua mtandao. Wacha tujue IP Address ambayo tumeunganishwa nayo.


```
$ ifconfig
```


Kwa mfano, ikiwa ni 192.168.0.0, tumia nmap kupata Pi.


```
nmap -v 192.168.0.0/24
```


Kwa kudhani tunapata IP mpya kwenye mtandao wetu, wacha tuingie kupitia SSH.


```
$ ssh pi@192.168.0.30
password: raspberry
```


#### 6. Sanidi Pi

```
$ sudo raspi-config
```


- Chagua chaguo (1) na ubadilishe nenosiri la mtumiaji pi.
- Tunachagua chaguo (8) kusasisha zana ya usanidi hadi toleo jipya zaidi
- Tunachagua chaguo (4) ili kuchagua eneo letu la saa
- Tunachagua chaguo (7) na kisha Panua mfumo wa faili
- Maliza


#### 7. Sasa sasisha OS

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


#### 8. Ongeza mtumiaji wa Bitcoin

```
$ sudo adduser bitcoin
```


#### 9. Salama rpi


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


#### 10. Sakinisha Go

Ikiwa hutumii raspberry pi, pakua nenda kwa usanifu wako [hapa](https://golang.org/dl/)


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


#### 11. Kukusanya na kufunga LND


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


#### 12. Unda faili ya LND ya conf

Unda faili ya usanidi ya LND, hii inapaswa kufanywa na mtumiaji wa 'Bitcoin'


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


#### 13. LND huduma autostart

Ili kufanya LND ianze baada ya rpi boot, lazima tuunda faili ya .service katika systemd. Ikiwa tumeingia kama mtumiaji wa Bitcoin na tunataka kurejea kwa mtumiaji wa pi, tunaandika tu 'toka'.


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


Tunaweza kutazama kumbukumbu kwa kuendesha jarida la amri


```
$ sudo journalctl -f -u lnd
```


#### 14. Sasa tunaanza LND


```
$ sudo su - bitcoin
$ lncli create
```


#### 15. Ongeza fedha kwenye node


```
$ lncli newaddress p2wkh
```

Sasa unaweza kutuma btc kwa Address iliyorejeshwa na LND.


na amri hii, unaweza kuangalia usawa:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


Baada ya muamala kuthibitishwa, tunaweza kufungua kituo. Ikiwa hujui ni nodi gani ya kufungua chaneli, unaweza kwenda kwa 1ml.com na uchague nodi.


Fungua unganisho kwa nodi:

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


Kisha fungua kituo:

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


Angalia fedha zetu:

```
$ lncli walletbalance
$ lncli channelbalance
```


Tunaweza kutazama vituo vinavyosubiri na vinavyotumika:

```
$ lncli pendingchannels
$ lncli listchannels
```


Kulipa umeme Invoice:

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


Ili kupokea malipo, unda Invoice kwa kiasi mahususi:

```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


Ili kuona habari kuhusu nodi yangu:

```
$ lncli getinfo
```


Orodha kamili ya amri inaweza kuonekana kwa kuendesha tu lncli amri:

```
$ lncli
```


Mwishowe, kupiga simu kwa LND API:

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


MWISHO wa mwongozo!