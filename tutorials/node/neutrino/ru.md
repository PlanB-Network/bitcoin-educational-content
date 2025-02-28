---
name: Neutrino
description: Руководство по установке LND Neutrino
---

# Настройка Raspberry Pi с LND

1. Скачайте Raspberry Pi OS Lite

Скачайте Raspberry Pi OS Lite, инструкции по скачиванию и установке образа на microSD-карту для Windows, Mac и Linux можно найти на [этой странице](https://www.raspberrypi.org/software/operating-systems/).

2. Форматирование SD-карты

Форматируйте SD-карту с помощью Raspberry Pi Imager или balenaEtcher.

> ПРИМЕЧАНИЕ: Символ `$` используется как приглашение к вводу команд в компьютер, команды будут интерпретироваться bash в Linux. Символ `#` в начале строки указывает на то, что следующий текст является комментарием.

3. Включение SSH

Перед тем как начать работу с Raspberry Pi с отформатированной памятью, мы должны вставить её в компьютер и создать два файла, которые позволят нам подключаться удалённо. Используя команду `touch`, мы создаём пустой файл в разделе /boot, включая SSH-соединение при первом запуске свежеформатированной SD-карты.

```
# ПРИМЕЧАНИЕ: Если microSD-карта была смонтирована в /media/microSD, команда
# должна быть $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

4. Используя команду nano

мы создаём файл wpa_supplicant.conf и сразу же начинаем его редактировать. В этот файл нам нужно скопировать конфигурацию wifi, копируя текст между START и END, и изменяя SSID и пароль wifi, к которому вы хотите подключиться.

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

5. Подключение

Затем вставляем SD-карту в Raspberry Pi и подключаем Pi к источнику питания для запуска операционной системы. Нам нужно идентифицировать его в сети, и протокол mDNS, скорее всего, присвоит ему имя raspberrypi.local. Давайте попробуем подключиться через SSH.

```
$ ssh pi@raspberrypi.local
password: raspberry
```

Если это не работает, нам нужно узнать сеть. Давайте выясним IP-адрес, к которому мы подключены.

```
$ ifconfig
```

Например, если это 192.168.0.0, используйте nmap для поиска Pi.

```
nmap -v 192.168.0.0/24
```

Предполагая, что мы находим новый IP в нашей сети, давайте войдем через SSH.

```
$ ssh pi@192.168.0.30
password: raspberry
```

1. Настройка Pi

```
$ sudo raspi-config
```

- Выбираем опцию (1) и меняем пароль для пользователя pi.
- Выбираем опцию (8) для обновления инструмента конфигурации до последней версии
- Выбираем опцию (4) для выбора нашего часового пояса
- Выбираем опцию (7) и затем Расширить файловую систему
- Завершаем

  7.- Обновляем ОС

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```

8.- Добавляем пользователя bitcoin

```
$ sudo adduser bitcoin
```

9.- Обеспечиваем безопасность rpi

```
$ sudo apt install ufw
```
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ sudo ufw allow 22 comment 'разрешить SSH из LAN'
$ sudo ufw allow 9735 comment 'разрешить Lightning'
$ sudo ufw allow 10009 comment 'Lightning gRPC'
$ sudo ufw enable
$ sudo systemctl enable ufw
$ sudo ufw status
$ sudo apt install fail2ban
```

10.- Мы устанавливаем Go: если вы не используете Raspberry Pi, скачайте Go для вашей архитектуры здесь (https://golang.org/dl/)

```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # должно отобразить сообщение 'go version go1.13.5 linux/arm'
```

11.- Мы компилируем и устанавливаем lnd

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

12.- Мы создаем файл конфигурации lnd, это должно быть сделано с пользователем 'bitcoin'

```
$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf
```

```
[Application Options]
# включить спонтанные платежи
accept-keysend=1

# Публичное имя узла
alias=ВАШ_ПСЕВДОНИМ
# Публичный цвет в шестнадцатеричном формате
color=#000000
debuglevel=info
maxpendingchannels=5
listen=localhost
# gRPC сокет
rpclisten=0.0.0.0:10009

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=neutrino

[neutrino]
neutrino.connect=bb2.breez.technology
```

13.- Чтобы LND запускался после загрузки RPi, мы должны создать файл .service в systemd.
Если мы залогинены как пользователь bitcoin и хотим вернуться к пользователю pi, просто вводим 'exit'

```
$ exit
$ sudo nano /etc/systemd/system/lnd.service
```

```
[Unit]
Description=LND Lightning Network Daemon
After=network.target

[Service]

# Выполнение службы
###################

ExecStart=/usr/local/bin/lnd


# Управление процессом
####################

Type=simple
Restart=always
RestartSec=30
TimeoutSec=240
LimitNOFILE=128000

# Создание директории и управление правами
####################################

# Запуск от имени bitcoin:bitcoin
User=bitcoin
Group=bitcoin

# /run/lightningd
RuntimeDirectory=lightningd
RuntimeDirectoryMode=0710

# Меры по усилению безопасности
####################

# Обеспечение приватности /tmp и /var/tmp.
```
```
PrivateTmp=true
# Монтирование /usr, /boot/ и /etc только для чтения для процесса.
ProtectSystem=full

# Запрет процессу и всем его дочерним процессам получать
# новые привилегии через execve().
NoNewPrivileges=true

# Использование нового пространства имен /dev, заполненного только API псевдоустройствами
# такими как /dev/null, /dev/zero и /dev/random.
PrivateDevices=true

# Запрет на создание записываемых и исполняемых отображений памяти.
MemoryDenyWriteExecute=true

[Install]
WantedBy=multi-user.target
```

```
$ sudo systemctl enable lnd
$ sudo systemctl start lnd
$ systemctl status lnd
```

Мы можем просмотреть логи, выполнив команду journalctl

```
$ sudo journalctl -f -u lnd
```

14. Теперь мы запускаем lnd

```
$ sudo su - bitcoin
$ lncli create
```

15. Добавляем средства на наш узел

```
$ lncli newaddress p2wkh
```

Отправляем btc на адрес, возвращенный lnd

Для проверки баланса

```
$ lncli walletbalance
{
    "total_balance": "500000",
    "confirmed_balance": "0",
    "unconfirmed_balance": "500000"
}
```

После подтверждения транзакции мы можем открыть канал. Если вы не знаете, с каким узлом открыть канал, вы можете перейти на 1ml.com и выбрать узел.

Открываем соединение с узлом:

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```

Затем открываем канал

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```

Проверяем наши средства

```
$ lncli walletbalance
$ lncli channelbalance
```

Мы можем просмотреть ожидающие и активные каналы

```
$ lncli pendingchannels
$ lncli listchannels
```

Чтобы оплатить счет Lightning

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```

Чтобы получить платеж, создайте счет на определенную сумму

```
$ lncli addinvoice --memo 'мой первый платеж в LN' --amt 100
```

Для просмотра информации о моем узле

```
$ lncli getinfo
```

Полный список команд можно увидеть, просто выполнив lncli

```
$ lncli
```

Наконец, для вызова API lnd

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```

> КОНЕЦ