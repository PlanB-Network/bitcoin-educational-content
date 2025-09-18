---
name: Neutrino
description: راهنمای نصب LND Neutrino
---
![image](assets/cover.webp)


## پیکربندی Raspberry Pi با LND


### ۱. دانلود Raspberry Pi OS Lite


دستورالعمل‌های دانلود و نصب تصویر بر روی کارت micro SD در ویندوز، مک و لینوکس را می‌توانید در [این صفحه](https://www.raspberrypi.org/software/operating-systems/) پیدا کنید.


### ۲. کارت SD را فرمت کنید


از Raspberry Pi Imager یا balenaEtcher استفاده کنید.


**توجه:** نماد `$` به عنوان یک اعلان استفاده می‌شود و به کاربر اجازه می‌دهد تا دستورات را در کامپیوتر وارد کند، این دستورات توسط bash در لینوکس تفسیر خواهند شد. نماد `#` در ابتدای یک خط نشان می‌دهد که متن بعدی یک توضیح است.


### ۳. SSH را فعال کنید


قبل از راه‌اندازی Raspberry Pi با حافظه فرمت شده، باید آن را در یک کامپیوتر قرار دهیم و دو فایل ایجاد کنیم که به ما اجازه می‌دهد به صورت از راه دور متصل شویم. با استفاده از دستور `touch`، یک فایل خالی در پارتیشن /boot ایجاد می‌کنیم که اتصال SSH را در اولین بوت کارت SD تازه فرمت شده فعال می‌کند.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4. ایجاد فایل برای اتصال Wi-Fi


با استفاده از دستور nano، فایل `wpa_supplicant.conf` را ایجاد کرده و مستقیماً شروع به ویرایش آن می‌کنیم. در این فایل، باید تنظیمات وای‌فای را کپی کنیم، متن بین START و END را کپی کرده و SSID و رمز عبور وای‌فای که می‌خواهید به آن متصل شوید را تغییر دهیم.


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


### ۵. اتصال


سپس، کارت SD را در Raspberry Pi قرار می‌دهیم و Pi را به منبع تغذیه متصل می‌کنیم تا سیستم‌عامل راه‌اندازی شود. باید آن را در شبکه شناسایی کنیم و پروتکل mDNS احتمالاً نام raspberrypi.local را به آن اختصاص خواهد داد. بیایید سعی کنیم از طریق SSH متصل شویم.


```
$ ssh pi@raspberrypi.local
password: raspberry
```


اگر کار نمی‌کند، باید شبکه را پیدا کنیم. بیایید بفهمیم به IP Address متصل هستیم.


```
$ ifconfig
```


به عنوان مثال، اگر 192.168.0.0 است، از nmap برای پیدا کردن Pi استفاده کنید.


```
nmap -v 192.168.0.0/24
```


فرض کنیم یک IP جدید در شبکه خود پیدا کنیم، بیایید از طریق SSH وارد شویم.


```
$ ssh pi@192.168.0.30
password: raspberry
```


### ۶. پیکربندی Pi


```
$ sudo raspi-config
```


- گزینه (1) را انتخاب کنید و رمز عبور کاربر pi را تغییر دهید.
- ما گزینه (8) را برای به‌روزرسانی ابزار پیکربندی به آخرین نسخه انتخاب می‌کنیم.
- ما گزینه (4) را برای انتخاب منطقه زمانی خود انتخاب می‌کنیم.
- ما گزینه (7) را انتخاب می‌کنیم و سپس فایل‌سیستم را گسترش می‌دهیم.
- پایان دهید


### ۷. اکنون سیستم‌عامل را به‌روزرسانی کنید


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8. کاربر Bitcoin را اضافه کنید


```
$ sudo adduser bitcoin
```


### ۹. رزبری پای را ایمن کنید


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


### ۱۰. نصب Go


اگر از رزبری پای استفاده نمی‌کنید، Go را برای معماری خود از [اینجا](https://golang.org/dl/) دانلود کنید.


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11. کامپایل و نصب LND


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


### 12. ایجاد فایل پیکربندی LND


فایل پیکربندی LND را ایجاد کنید، این کار باید با کاربر 'Bitcoin' انجام شود.


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


### ۱۳. راه‌اندازی خودکار سرویس LND


برای شروع LND پس از بوت شدن rpi، باید فایل .service را در systemd ایجاد کنیم. اگر به عنوان کاربر Bitcoin وارد شده‌ایم و می‌خواهیم به کاربر pi برگردیم، به سادگی 'exit' را تایپ می‌کنیم.


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


ما می‌توانیم با اجرای دستور journalctl لاگ‌ها را مشاهده کنیم.


```
$ sudo journalctl -f -u lnd
```


### 14. اکنون ما LND را شروع می‌کنیم.


```
$ sudo su - bitcoin
$ lncli create
```


### ۱۵. افزودن وجه به نود


```
$ lncli newaddress p2wkh
```

اکنون می‌توانید btc را به Address که توسط LND بازگردانده شده است، ارسال کنید.


با این دستور، می‌توانید موجودی را بررسی کنید:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


به محض تأیید تراکنش، می‌توانیم یک کانال باز کنیم. اگر نمی‌دانید با کدام نود کانال باز کنید، می‌توانید به 1ml.com بروید و یک نود انتخاب کنید.


اتصال به یک گره را باز کنید:


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


سپس یک کانال باز کنید:


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


صندوق‌های ما را بررسی کنید:


```
$ lncli walletbalance
$ lncli channelbalance
```


می‌توانیم کانال‌های در انتظار و فعال را مشاهده کنیم:


```
$ lncli pendingchannels
$ lncli listchannels
```


برای پرداخت یک Invoice صاعقه:


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


برای دریافت پرداخت، یک Invoice برای مبلغ مشخصی ایجاد کنید:


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


برای مشاهده اطلاعات در مورد نود من:


```
$ lncli getinfo
```


فهرست کامل دستورات را می‌توان با اجرای ساده دستور lncli مشاهده کرد:


```
$ lncli
```


در نهایت، برای برقراری تماس با API LND:


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


پایان راهنما!