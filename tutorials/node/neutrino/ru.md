---
name: Neutrino
description: Руководство по установке LND Neutrino
---
![image](assets/cover.webp)


## Конфигурация Raspberry Pi с LND


### 1. Скачать Raspberry Pi OS Lite


Инструкции по загрузке и установке образа на карту micro SD в Windows, Mac и Linux можно найти на [этой странице](https://www.raspberrypi.org/software/operating-systems/).


### 2. Форматирование SD-карты


Используйте Raspberry Pi Imager или balenaEtcher.


**Примечание:** Символ `$` используется в качестве подсказки и позволяет пользователю вводить команды в компьютер, которые будут интерпретированы bash в Linux. Символ `#` в начале строки означает, что следующий текст является комментарием.


### 3. Включить SSH


Прежде чем запустить Raspberry Pi с отформатированной памятью, мы должны вставить ее в компьютер и создать два файла, которые позволят нам подключаться удаленно. С помощью команды `touch` мы создадим пустой файл в разделе /boot, что позволит подключаться по SSH при первой загрузке свежеотформатированной SD-карты.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4. Создание файла для подключения к Wi-Fi


С помощью команды nano создаем файл `wpa_supplicant.conf` и приступаем непосредственно к его редактированию. В этом файле нам нужно скопировать конфигурацию wifi, скопировав текст между START и END, а также изменив SSID и пароль wifi, к которому вы хотите подключиться.


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


### 5. Соединение


Затем мы вставляем SD-карту в Raspberry Pi и подключаем Pi к источнику питания, чтобы запустить операционную систему. Нам нужно определить его в сети, и протокол mDNS, скорее всего, присвоит ему имя raspberrypi.local. Давайте попробуем подключиться через SSH.


```
$ ssh pi@raspberrypi.local
password: raspberry
```


Если он не работает, нужно выяснить сеть. Давайте выясним IP Address, к которому мы подключены.


```
$ ifconfig
```


Например, если это 192.168.0.0, используйте nmap, чтобы найти Pi.


```
nmap -v 192.168.0.0/24
```


Предполагая, что мы нашли новый IP в нашей сети, давайте войдем в систему через SSH.


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6. Настройте Pi


```
$ sudo raspi-config
```


- Выберите опцию (1) и измените пароль для пользователя pi.
- Мы выбираем опцию (8), чтобы обновить инструмент конфигурации до последней версии
- Выбираем опцию (4) для выбора часового пояса
- Выбираем опцию (7) и затем Расширить файловую систему
- Отделка


### 7. Теперь обновите ОС


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8. Добавьте пользователя Bitcoin


```
$ sudo adduser bitcoin
```


### 9. Обеспечьте безопасность rpi


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


### 10. Установите Go


Если вы не используете raspberry pi, скачайте программу go for your architecture [здесь](https://golang.org/dl/).


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11. Скомпилируйте и установите LND


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


### 12. Создание файла LND conf


Создайте файл конфигурации LND, это нужно сделать под пользователем 'Bitcoin'


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


### 13. LND сервис автозапуска


Чтобы заставить LND запускаться после загрузки rpi, мы должны создать файл .service в systemd. Если мы вошли в систему как пользователь Bitcoin и хотим переключиться обратно на пользователя pi, мы просто набираем 'exit'


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


Мы можем просмотреть журналы, выполнив команду journalctl


```
$ sudo journalctl -f -u lnd
```


### 14. Теперь мы начинаем LND


```
$ sudo su - bitcoin
$ lncli create
```


### 15. Добавьте средства на узел


```
$ lncli newaddress p2wkh
```

Теперь вы можете отправлять btc на Address, возвращенные LND.


с помощью этой команды вы можете проверить баланс:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


Как только транзакция подтверждена, можно открывать канал. Если вы не знаете, на каком узле открыть канал, вы можете зайти на сайт 1ml.com и выбрать узел.


Откройте соединение с узлом:


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


Затем откройте канал:


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


Проверьте наши фонды:


```
$ lncli walletbalance
$ lncli channelbalance
```


Мы можем просматривать отложенные и активные каналы:


```
$ lncli pendingchannels
$ lncli listchannels
```


Заплатить за молнию Invoice:


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


Чтобы получить платеж, создайте Invoice на определенную сумму:


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


Чтобы просмотреть информацию о моем узле:


```
$ lncli getinfo
```


Полный список команд можно увидеть, просто выполнив команду lncli:


```
$ lncli
```


Наконец, для выполнения вызовов API LND:


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


Конец путеводителя!