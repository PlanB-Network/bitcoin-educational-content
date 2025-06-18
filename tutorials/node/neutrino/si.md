---
name: නියුට්‍රිනෝ
description: LND Neutrino ස්ථාපන මාර්ගෝපදේශය
---

# Raspberry Pi කන්ෆිගරේෂන් LND සමඟ


#### 1. Raspberry Pi OS Lite බාගන්න

Windows, Mac, සහ Linux මත මයික්‍රෝ SD කාඩ්පතක පින්තූරය බාගත කිරීම සහ ස්ථාපනය කිරීම සඳහා උපදෙස් [මෙම පිටුවේ](https://www.raspberrypi.org/software/operating-systems/) සොයා ගත හැක.


#### 2. SD කාඩ්පත ආකෘතිගත කරන්න

Raspberry Pi Imager හෝ balenaEtcher භාවිතා කරන්න.


**සටහන:** සංකේතය `$` යොදාගන්නේ පරිශීලකයාට පරිගණකයට විධාන ඇතුළත් කිරීමට ඉඩ දීම සඳහා වන අතර, එම විධාන Linux හි bash මඟින් විවරණය කෙරේ. පේළියක ආරම්භයේ ඇති සංකේතය `#` යොදා ඇත්තේ පසුපස ඇති පෙළ විවරණයක් බව සනිටුහන් කිරීම සඳහාය.


#### 3. SSH සක්‍රීය කරන්න


රැස්පබෙරි පයි ආරම්භ කිරීමට පෙර, ආකෘතිගත මතකය සමඟ, අපි එය පරිගණකයකට ඇතුල් කර, අපට දුරස්ථව සම්බන්ධ වීමට ඉඩ දෙන ගොනු දෙකක් සාදන්නෙමු. `touch` විධානය භාවිතා කරමින්, අපි /boot කොටසේ හිස් ගොනුවක් සාදන අතර, නව ආකෘතිගත කළ SD කාඩ්පතේ පළමු ආරම්භයේදී SSH සම්බන්ධතාවය සක්‍රීය කරයි.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

#### 4. Wi-Fi සම්බන්ධතාවය සඳහා ගොනුවක් සාදන්න

nano විධානය භාවිතා කරමින් අපි `wpa_supplicant.conf` ගොනුව නිර්මාණය කර එය සෘජුවම සංස්කරණය කිරීම ආරම්භ කරමු. මෙම ගොනුවේ, wifi වින්‍යාසය පිටපත් කිරීමට අපට අවශ්‍ය වන අතර, START සහ END අතර පෙළ පිටපත් කර, ඔබ සම්බන්ධ වීමට අවශ්‍ය wifi හි SSID සහ මුරපදය වෙනස් කරන්න.


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


#### 5. සම්බන්ධතාවය

Potem vstavimo kartico SD v Raspberry Pi in povežemo Pi na vir napajanja, da zaženemo operacijski sistem. Prepoznati ga moramo v omrežju, in protokol mDNS mu bo verjetno dodelil ime raspberrypi.local. Poskusimo se povezati prek SSH.

```
$ ssh pi@raspberrypi.local
password: raspberry
```

Če to ne deluje, moramo ugotoviti omrežje. Ugotovimo IP Address, na katerega smo povezani.


```
$ ifconfig
```


उदाहरण के लिए, यदि यह 192.168.0.0 है, तो Pi को खोजने के लिए nmap का उपयोग करें।


```
nmap -v 192.168.0.0/24
```


අපගේ ජාලයේ නව IP එකක් සොයා ගන්නා බව ප supon ා කර, SSH හරහා ඇතුල් විය යුතුය.


```
$ ssh pi@192.168.0.30
password: raspberry
```


#### 6. Pi සකසන්න

```
$ sudo raspi-config
```


- තේරීම (1) තෝරන්න සහ pi පරිශීලකයා සඳහා මුරපදය වෙනස් කරන්න.
- අපි නවතම අනුවාදයට වින්‍යාස මෙවලම යාවත්කාලීන කිරීමට විකල්පය (8) තෝරමු.
- අපගේ වේලා කලාපය තෝරා ගැනීමට විකල්පය (4) තෝරන්නෙමු
- අපි විකල්පය (7) තෝරාගෙන පසුව ගොනු පද්ධතිය විශාල කරමු
- අවසන් කරන්න


#### 7. දැන් මෙහෙයුම් පද්ධතිය යාවත්කාලීන කරන්න

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


#### 8. Bitcoin පරිශීලකයා එක් කරන්න

```
$ sudo adduser bitcoin
```


#### 9. rpi සුරක්ෂිත කරන්න


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


#### 10. Go ස්ථාපනය කරන්න

Če ne uporabljate raspberry pi, prenesite go za vašo arhitekturo [tukaj](https://golang.org/dl/)


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


#### 11. LND සංග්‍රහය සහ ස්ථාපනය කරන්න


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


#### 12. LND සංකේත ගොනුව සාදන්න

LND කන්ෆිගරේෂන් ගොනුව සාදන්න, මෙය 'Bitcoin' පරිශීලකයා සමඟ සිදු කළ යුතුය.


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


#### 13. LND सेवा स्वतःप्रारम्भ

Če želimo, da se LND zažene po zagonu rpi, moramo ustvariti .service datoteko v systemd. Če smo prijavljeni kot uporabnik Bitcoin in se želimo vrniti na uporabnika pi, preprosto vtipkamo 'exit'.


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


ලොග් බලන්න අපට journalctl විධානය ක්‍රියාත්මක කළ හැක.


```
$ sudo journalctl -f -u lnd
```


#### 14. දැන් අපි LND ආරම්භ කරමු


```
$ sudo su - bitcoin
$ lncli create
```


#### 15. නියුඩ් වෙත මුදල් එක් කරන්න


```
$ lncli newaddress p2wkh
```

Zdaj lahko pošljete btc na Address, ki ga je vrnil LND.


මෙම විධානය සමඟ, ඔබට ශේෂය පරීක්ෂා කළ හැක:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


ලෙදීම සනාථ වූ පසු, අපට නාලිකාවක් විවෘත කළ හැක. ඔබට කුමන නෝඩ් එක සමඟ නාලිකාව විවෘත කළ යුතුදැයි නොදන්නා නම්, 1ml.com වෙත ගොස් නෝඩ් එකක් තෝරා ගත හැක.


නෝඩ් එකකට සම්බන්ධතාවයක් විවෘත කරන්න:

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


පසුව නාලිකාවක් විවෘත කරන්න:

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


පිළිබඳව අපගේ අරමුදල් පරීක්ෂා කරන්න:

```
$ lncli walletbalance
$ lncli channelbalance
```


අපට බලාපොරොත්තු සහ සක්‍රීය නාලිකා බලන්න පුළුවන්:

```
$ lncli pendingchannels
$ lncli listchannels
```


Za plačilo strele Invoice:

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


භාණ්ඩයක් ලැබීමට, විශේෂිත මුදලක් සඳහා Invoice එකක් සාදන්න:

```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


මගේ නෝඩ් පිළිබඳ තොරතුරු බැලීමට:

```
$ lncli getinfo
```


lncli විධානය ක්‍රියාත්මක කිරීමෙන් සම්පූර්ණ විධාන ලැයිස්තුව දැකගත හැක:

```
$ lncli
```


අවසානයේ, LND API වෙත ඇමතුම් කිරීමට:

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


ගිඩ් එකේ අවසානය!