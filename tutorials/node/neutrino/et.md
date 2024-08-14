---
nimi: Neutrino
kirjeldus: LND Neutrino paigaldusjuhend
---

# Raspberry Pi seadistamine LND-ga

1. Laadi alla Raspberry Pi OS Lite

Laadi alla Raspberry Pi OS Lite, juhised pildi allalaadimiseks ja installimiseks mikro SD kaardile Windowsis, Macis ja Linuxis leiad [sellelt lehelt](https://www.raspberrypi.org/software/operating-systems/).

2. Formaadi SD kaart

Formaadi SD kaart kasutades Raspberry Pi Imagerit või balenaEtcherit.

> MÄRKUS: Sümbol `$` on kasutusel kui käsuviip, mis lubab kasutajal sisestada käsklusi arvutisse, käsklusi tõlgendab Linuxis bash. Sümbol `#` rea alguses näitab, et järgnev tekst on kommentaar.

3. Luba SSH

Enne Raspberry Pi käivitamist formaaditud mäluga, peame selle sisestama arvutisse ja looma kaks faili, mis lubavad meil ühenduda kaugteel. Kasutades `touch` käsku, loome tühja faili /boot partitsioonis, lubades SSH ühenduse esimesel käivitamisel värskelt formaaditud SD kaardil.

```
# MÄRKUS: Kui microSD kaart on monteeritud aadressil /media/microSD, peaks käsk olema
# $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

4. Kasutades nano käsku

loome faili wpa_supplicant.conf ja alustame selle otse redigeerimist. Selles failis peame kopeerima wifi seadistuse, kopeerides teksti alates START kuni END, ja muutes SSID ja parooli wifi võrgu jaoks, millega soovite ühenduda.

```
$ nano /boot/wpa_supplicant.conf

------ START -------
country=ar
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
 ssid="MinuVõrguSSID"
 psk="parool"
}
------ END -------
```

5. Ühendus

Seejärel sisestame SD kaardi Raspberry Pisse ja ühendame Pi toiteallikaga, et käivitada operatsioonisüsteem. Peame selle võrgus tuvastama, ja tõenäoliselt määrab mDNS protokoll sellele nime raspberrypi.local. Proovime ühenduda SSH kaudu.

```
$ ssh pi@raspberrypi.local
parool: raspberry
```

Kui see ei õnnestu, peame võrgu üles leidma. Uurime, millisele IP aadressile oleme ühendatud.

```
$ ifconfig
```

Näiteks, kui see on 192.168.0.0, kasutame Pi leidmiseks nmap'i.

```
nmap -v 192.168.0.0/24
```

Eeldades, et leiame oma võrgus uue IP, sisestame SSH kaudu.

```
$ ssh pi@192.168.0.30
parool: raspberry
```

1. Seadista Pi

```
$ sudo raspi-config
```

- Vali valik (1) ja muuda kasutaja pi parooli.
- Valime valiku (8), et uuendada seadistustööriista viimasele versioonile
- Valime valiku (4), et valida meie ajavöönd
- Valime valiku (7) ja seejärel Laienda failisüsteemi
- Lõpeta

  7.- Uuendame OS-i

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```

8.- Lisame bitcoin kasutaja

```
$ sudo adduser bitcoin
```

9.- Turvame rpi

```
$ sudo apt install ufw
```
```
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ sudo ufw allow 22 comment 'luba SSH LAN-ist'
$ sudo ufw allow 9735 comment 'luba Lightning'
$ sudo ufw allow 10009 comment 'Lightning gRPC'
$ sudo ufw enable
$ sudo systemctl enable ufw
$ sudo ufw status
$ sudo apt install fail2ban
```

```
10.- Paigaldame go: kui te ei kasuta raspberry pi-d, laadige alla go teie arhitektuurile siit (https://golang.org/dl/)

```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # peaks kuvama järgmise sõnumi 'go version go1.13.5 linux/arm'
```

11.- Kompileerime ja paigaldame lnd

```
$ git clone https://github.com/lightningnetwork/lnd.git
$ cd lnd
$ make
$ make install tags="autopilotrpc chainrpc experimental invoicesrpc routerrpc signrpc walletrpc watchtowerrpc wtclientrpc"
$ sudo cp $GOPATH/bin/lnd /usr/local/bin/
$ sudo cp $GOPATH/bin/lncli /usr/local/bin/
$ lncli --version
lncli versioon 0.11.0-beta commit=v0.11.0-beta-61-g6055b00dbbcedf45cd60f12e57dc5c1a7b97746f
```

12.- Loome lnd konfiguratsioonifaili, see tuleks teha 'bitcoin' kasutajana

```
$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf
```

```
[Application Options]
# luba spontaansed maksed
accept-keysend=1

# Sõlme avalik nimi
alias=TEIE_ALIAS
# Avalik värv heksadesimaalkoodis
color=#000000
debuglevel=info
maxpendingchannels=5
listen=localhost
# gRPC sokkel
rpclisten=0.0.0.0:10009

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=neutrino

[neutrino]
neutrino.connect=bb2.breez.technology
```

13.- Et LND käivituks pärast rpi taaskäivitust, peame looma .service faili systemd-s.
Kui oleme sisse logitud bitcoin kasutajana ja soovime tagasi lülituda pi kasutajale, tippige lihtsalt 'exit'

```
$ exit
$ sudo nano /etc/systemd/system/lnd.service
```

```
[Unit]
Description=LND Lightning Network Daemon
After=network.target

[Service]

# Teenuse täitmine
###################

ExecStart=/usr/local/bin/lnd


# Protsessi haldamine
####################

Type=simple
Restart=always
RestartSec=30
TimeoutSec=240
LimitNOFILE=128000

# Kaustade loomine ja õigused
####################################

# Käivita bitcoin:bitcoin kasutajana
User=bitcoin
Group=bitcoin

# /run/lightningd
RuntimeDirectory=lightningd
RuntimeDirectoryMode=0710

# Turvameetmed
####################

# Paku privaatset /tmp ja /var/tmp.
```
```
PrivateTmp=true
# Paigalda /usr, /boot/ ja /etc ainult-loetavaks protsessile.
ProtectSystem=full

# Keela protsessil ja kõigil selle lastel uute privileegide saamine
# läbi execve().
NoNewPrivileges=true

# Kasuta uut /dev nimeruumi, mis on täidetud ainult API pseudo-seadmetega
# nagu /dev/null, /dev/zero ja /dev/random.
PrivateDevices=true

# Keela kirjutatavate ja käivitatavate mälukaartide loomine.
MemoryDenyWriteExecute=true

[Install]
WantedBy=multi-user.target
```

```
$ sudo systemctl enable lnd
$ sudo systemctl start lnd
$ systemctl status lnd
```

Logide vaatamiseks käivita käsk journalctl

```
$ sudo journalctl -f -u lnd
```

14. Nüüd käivitame lnd

```
$ sudo su - bitcoin
$ lncli create
```

15. Lisame meie sõlmele vahendeid

```
$ lncli newaddress p2wkh
```

Saada btc aadressile, mille lnd tagastas

Saldo kontrollimiseks

```
$ lncli walletbalance
{
    "total_balance": "500000",
    "confirmed_balance": "0",
    "unconfirmed_balance": "500000"
}
```

Kui tehing on kinnitatud, saame avada kanali. Kui sa ei tea, millise sõlmega kanali avada, võid minna 1ml.com ja valida sõlme.

Loo ühendus sõlmega:

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```

Seejärel ava kanal

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```

Kontrolli meie vahendeid

```
$ lncli walletbalance
$ lncli channelbalance
```

Saame vaadata ootel ja aktiivseid kanaleid

```
$ lncli pendingchannels
$ lncli listchannels
```

Maksmiseks lightning arvega

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```

Makse vastuvõtmiseks loo arve kindla summa jaoks

```
$ lncli addinvoice --memo 'minu esimene makse LN-s' --amt 100
```

Minu sõlme kohta informatsiooni vaatamiseks

```
$ lncli getinfo
```

Kõigi käskude täielikku nimekirja saab näha lihtsalt käsku lncli käivitades

```
$ lncli
```

Lõpuks, et teha kõnesid lnd API-le

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```

> LÕPP
```