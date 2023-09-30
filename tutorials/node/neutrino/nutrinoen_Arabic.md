# إعداد Raspberry Pi مع LND

1. قم بتنزيل Raspberry Pi OS Lite

قم بتنزيل Raspberry Pi OS Lite، يمكن العثور على تعليمات التنزيل والتثبيت للصورة على بطاقة micro SD في نظام التشغيل Windows و Mac و Linux على [هذه الصفحة](https://www.raspberrypi.org/software/operating-systems/).

2. قم بتهيئة بطاقة SD

قم بتهيئة بطاقة SD باستخدام Raspberry Pi Imager أو balenaEtcher.

> ملاحظة: يتم استخدام الرمز `$` كمؤشر ويسمح للمستخدم بإدخال الأوامر في الكمبيوتر، وسيتم تفسير الأوامر بواسطة bash في Linux. يشير الرمز `#` في بداية السطر إلى أن النص التالي هو تعليق.

3. تمكين SSH

قبل بدء Raspberry Pi بالذاكرة المهيأة، يجب علينا إدخالها في الكمبيوتر وإنشاء ملفين سيسمحان لنا بالاتصال عن بُعد. باستخدام أمر `touch`، نقوم بإنشاء ملف فارغ في قسم /boot، مما يتيح اتصال SSH في أول تشغيل لبطاقة SD المهيأة حديثًا.

```
# ملاحظة: إذا تم تركيب بطاقة microSD في /media/microSD، يجب أن يكون الأمر
# $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

4. باستخدام أمر nano

نقوم بإنشاء ملف wpa_supplicant.conf وبدء تحريره مباشرة. في هذا الملف، نحتاج إلى نسخ تكوين الواي فاي، عن طريق نسخ النص بين START و END، وتعديل اسم SSID وكلمة المرور للواي فاي الذي ترغب في الاتصال به.

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

5. الاتصال

ثم، نقوم بإدخال بطاقة SD في Raspberry Pi ونوصل الجهاز بمصدر الطاقة لبدء نظام التشغيل. نحتاج إلى تحديد الجهاز على الشبكة، ومن المرجح أن يُسند له بروتوكول mDNS اسم raspberrypi.local. دعنا نحاول الاتصال عبر SSH.

```
$ ssh pi@raspberrypi.local
password: raspberry
```

إذا لم يعمل، فإننا بحاجة إلى معرفة الشبكة. لنحدد عنوان IP الذي نحن متصلون به.

```
$ ifconfig
```

على سبيل المثال، إذا كان 192.168.0.0، استخدم nmap للعثور على Pi.

```
nmap -v 192.168.0.0/24
```

في افتراض أننا وجدنا عنوان IP جديد على شبكتنا، دعنا ندخل عبر SSH.

```
$ ssh pi@192.168.0.30
password: raspberry
```

1. قم بتكوين Pi

```
$ sudo raspi-config
```

- حدد الخيار (1) وقم بتغيير كلمة المرور للمستخدم pi.
- نحدد الخيار (8) لتحديث أداة التكوين إلى أحدث إصدار
- نحدد الخيار (4) لتحديد منطقة الوقت الخاصة بنا
- نحدد الخيار (7) ثم نوسع نظام الملفات
- انتهاء

  7.- نقوم بتحديث النظام الأساسي

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```

8.- نضيف مستخدم البيتكوين

```
$ sudo adduser bitcoin
```

9.- نؤمن rpi

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

10.- نقوم بتثبيت Go: إذا لم تكن تستخدم Raspberry Pi، قم بتنزيل Go للهندسة المعمارية الخاصة بك هنا (https://golang.org/dl/)

```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # يجب أن يعرض الرسالة التالية 'go version go1.13.5 linux/arm'
```

11.- نقوم بتجميع وتثبيت lnd

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

12.- نقوم بإنشاء ملف تكوين lnd، يجب أن يتم ذلك باستخدام مستخدم 'bitcoin'

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

13.- لجعل LND يبدأ بعد تشغيل rpi، يجب علينا إنشاء ملف .service في systemd.
إذا كنا مسجلين كمستخدم bitcoin ونرغب في العودة إلى مستخدم pi، نكتب ببساطة 'exit'

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
# قم بتركيب /usr و /boot/ و /etc بصلاحية القراءة فقط للعملية.
ProtectSystem=full

# منع العملية وجميع أطفاله من اكتساب
# امتيازات جديدة من خلال execve ().
NoNewPrivileges=true

# استخدم مساحة أسماء /dev جديدة تحتوي فقط على أجهزة وهمية للواجهة البرمجية
# مثل /dev/null و /dev/zero و /dev/random.
PrivateDevices=true

# رفض إنشاء تطبيقات قابلة للكتابة والتنفيذ في الذاكرة.
MemoryDenyWriteExecute=true

[Install]
WantedBy=multi-user.target
```

```
$ sudo systemctl enable lnd
$ sudo systemctl start lnd
$ systemctl status lnd
```

يمكننا عرض السجلات عن طريق تشغيل أمر journalctl

```
$ sudo journalctl -f -u lnd
```

14. الآن نبدأ lnd

```
$ sudo su - bitcoin
$ lncli create
```

15. إضافة أموال إلى العقد الخاص بنا

```
$ lncli newaddress p2wkh
```

أرسل btc إلى العنوان الذي يتم إرجاعه بواسطة lnd

للتحقق من الرصيد

```
$ lncli walletbalance
{
    "total_balance": "500000",
    "confirmed_balance": "0",
    "unconfirmed_balance": "500000"
}
```

بمجرد تأكيد العملية ، يمكننا فتح قناة. إذا كنت لا تعرف أي عقدة لفتح القناة معها ، يمكنك الانتقال إلى 1ml.com واختيار عقدة.

افتح اتصالًا بعقدة:

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```

ثم افتح قناة

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```

تحقق من أموالنا

```
$ lncli walletbalance
$ lncli channelbalance
```

يمكننا عرض القنوات المعلقة والنشطة

```
$ lncli pendingchannels
$ lncli listchannels
```

لدفع فاتورة البرق

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```

لتلقي دفعة ، أنشئ فاتورة بمبلغ محدد

```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```

لعرض معلومات حول عقدتي

```
$ lncli getinfo
```

يمكن رؤية القائمة الكاملة للأوامر ببساطة عن طريق تشغيل lncli

```
$ lncli
```

أخيرًا ، لإجراء مكالمات لواجهة برمجة التطبيقات lnd

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```

> النهاية