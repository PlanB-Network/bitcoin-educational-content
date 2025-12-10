---
name: Neutrino
description: LND Neutrino Ръководство за инсталиране
---
![image](assets/cover.webp)


## Конфигурация на Raspberry Pi с LND


### 1. Изтегляне на Raspberry Pi OS Lite


Инструкциите за изтегляне и инсталиране на изображението на микро SD карта в Windows, Mac и Linux можете да намерите на [тази страница](https://www.raspberrypi.org/software/operating-systems/).


### 2. Форматиране на SD картата


Използвайте Raspberry Pi Imager или balenaEtcher.


**Забележка:** Символът `$` се използва като подкана и позволява на потребителя да въвежда команди в компютъра, които ще бъдат интерпретирани от bash в Linux. Символът `#` в началото на реда показва, че следващият текст е коментар.


### 3. Активиране на SSH


Преди да стартирате Raspberry Pi с форматираната памет, трябва да го поставите в компютър и да създадете два файла, които ще ни позволят да се свързваме отдалечено. С помощта на командата `touch` създаваме празен файл в дяла /boot, който позволява SSH връзка при първото зареждане на прясно форматираната SD карта.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4. Създаване на файл за Wi-Fi връзка


С помощта на командата nano създаваме файла `wpa_supplicant.conf` и започваме да го редактираме. В този файл трябва да копираме конфигурацията на wifi, като копираме текста между START и END, и да променим SSID и паролата на wifi, към който искате да се свържете.


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


### 5. Връзка


След това поставяме SD картата в Raspberry Pi и свързваме Pi към източника на захранване, за да стартираме операционната система. Трябва да го идентифицираме в мрежата и протоколът mDNS вероятно ще му присвои името raspberrypi.local. Нека се опитаме да се свържем чрез SSH.


```
$ ssh pi@raspberrypi.local
password: raspberry
```


Ако не работи, трябва да открием мрежата. Нека да открием IP адреса, към който сме свързани.


```
$ ifconfig
```


Например, ако е 192.168.0.0, използвайте nmap, за да намерите Pi.


```
nmap -v 192.168.0.0/24
```


Ако приемем, че сме намерили нов IP адрес в нашата мрежа, нека да влезем чрез SSH.


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6. Конфигуриране на Pi


```
$ sudo raspi-config
```


- Изберете опция (1) и променете паролата за потребителя pi.
- Избираме опция (8), за да актуализираме инструмента за конфигуриране до най-новата версия
- Избираме опция (4), за да изберем часовата зона
- Избираме опция (7) и след това Разширяване на файловата система
- Завършете


### 7. Сега актуализирайте операционната система


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8. Добавяне на потребителя на Bitcoin


```
$ sudo adduser bitcoin
```


### 9. Защита на rpi


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


### 10. Инсталиране на Go


Ако не използвате Raspberry Pi, изтеглете Go за вашата архитектура [тук](https://golang.org/dl/).


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11. Компилиране и инсталиране на LND


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


### 12. Създаване на lnd conf файл


Създаване на конфигурационния файл lnd, това трябва да се направи с потребителя 'bitcoin'


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


### 13. LND услугата autostart


За да накараме LND да се стартира след зареждане на rpi, трябва да създадем файла .service в systemd. Ако сме влезли в системата като потребител bitcoin и искаме да се върнем към потребителя pi, просто въвеждаме 'exit'


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


Можем да прегледаме дневниците, като изпълним командата journalctl


```
$ sudo journalctl -f -u lnd
```


### 14. Сега започваме LND


```
$ sudo su - bitcoin
$ lncli create
```


### 15. Добавяне на средства към възела


```
$ lncli newaddress p2wkh
```

Вече можете да изпращате btc на адреса, върнат от LND.


с тази команда можете да проверите баланса:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


След като транзакцията бъде потвърдена, можем да отворим канал. Ако не знаете с кой възел да отворите канала, можете да отидете на 1ml.com и да изберете възел.


Откриване на връзка към възел:


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


След това отворете канал:


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


Проверете нашите фондове:


```
$ lncli walletbalance
$ lncli channelbalance
```


Можем да видим чакащите и активните канали:


```
$ lncli pendingchannels
$ lncli listchannels
```


За да платите фактура за светкавица:


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


За да получите плащане, създайте фактура за определена сума:


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


За да видите информация за моя възел:


```
$ lncli getinfo
```


Пълният списък на командите може да се види, като се изпълни командата lncli:


```
$ lncli
```


И накрая, за да се обаждате към LND API:


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


Край на ръководството!