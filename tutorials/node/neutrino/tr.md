---
name: Neutrino
description: LND Neutrino Kurulum Kılavuzu
---
![image](assets/cover.webp)


## LND ile Raspberry Pi Yapılandırması


### 1. Raspberry Pi OS Lite İndir


Görüntüyü Windows, Mac ve Linux'ta bir mikro SD karta indirmek ve yüklemek için talimatlar [bu sayfada] (https://www.raspberrypi.org/software/operating-systems/) bulunabilir.


### 2. SD Kartı Biçimlendirme


Raspberry Pi Imager veya balenaEtcher kullanın.


**Not:** `$` sembolü komut istemi olarak kullanılır ve kullanıcının bilgisayara komut girmesini sağlar, komutlar Linux'ta bash tarafından yorumlanacaktır. Bir satırın başındaki `#` sembolü, takip eden metnin bir yorum olduğunu gösterir.


### 3. SSH'yi Etkinleştir


Raspberry Pi'yi biçimlendirilmiş bellekle başlatmadan önce, bilgisayara takmalı ve uzaktan bağlanmamızı sağlayacak iki dosya oluşturmalıyız. Touch` komutunu kullanarak, /boot bölümünde boş bir dosya oluşturuyoruz ve yeni biçimlendirilmiş SD kartın ilk açılışında SSH bağlantısını etkinleştiriyoruz.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4. Wi-Fi bağlantısı için dosya oluşturun


Nano komutunu kullanarak `wpa_supplicant.conf` dosyasını oluşturuyoruz ve doğrudan düzenlemeye başlıyoruz. Bu dosyada, wifi yapılandırmasını kopyalamamız, START ve END arasındaki metni kopyalamamız ve bağlanmak istediğiniz wifi'nin SSID'sini ve şifresini değiştirmemiz gerekiyor.


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


### 5. Bağlantı


Ardından, SD kartı Raspberry Pi'ye takıyoruz ve işletim sistemini başlatmak için Pi'yi güç kaynağına bağlıyoruz. Ağ üzerinde tanımlamamız gerekiyor ve mDNS protokolü muhtemelen ona raspberrypi.local adını atayacaktır. SSH üzerinden bağlanmayı deneyelim.


```
$ ssh pi@raspberrypi.local
password: raspberry
```


Eğer çalışmazsa, ağı bulmamız gerekir. Bağlı olduğumuz IP Address'yi bulalım.


```
$ ifconfig
```


Örneğin, 192.168.0.0 ise, Pi'yi bulmak için nmap kullanın.


```
nmap -v 192.168.0.0/24
```


Ağımızda yeni bir IP bulduğumuzu varsayarak SSH üzerinden giriş yapalım.


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6. Pi'yi Yapılandırma


```
$ sudo raspi-config
```


- (1) seçeneğini seçin ve pi kullanıcısı için parolayı değiştirin.
- Yapılandırma aracını en son sürüme güncellemek için (8) seçeneğini seçiyoruz
- Saat dilimimizi seçmek için (4) seçeneğini seçiyoruz
- (7) seçeneğini seçiyoruz ve ardından Dosya sistemini genişlet
- Bitirmek


### 7. Şimdi işletim sistemini güncelleyin


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8. Bitcoin kullanıcısını ekleyin


```
$ sudo adduser bitcoin
```


### 9. Rpi'yi güvence altına alın


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


### 10. Go'yu Yükle


Eğer bir raspberry pi kullanmıyorsanız, mimariniz için go'yu indirin [buradan](https://golang.org/dl/).


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11. LND'ü derleyin ve kurun


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


### 12. LND conf dosyası oluşturun


LND yapılandırma dosyasını oluşturun, bu işlem 'Bitcoin' kullanıcısı ile yapılmalıdır


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


### 13. LND servis otomatik başlatma


LND'un rpi açılışından sonra başlamasını sağlamak için systemd'de .service dosyasını oluşturmalıyız. Bitcoin kullanıcısı olarak oturum açtıysak ve pi kullanıcısına geri dönmek istiyorsak, sadece 'exit' yazmamız yeterlidir


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


Journalctl komutunu çalıştırarak günlükleri görüntüleyebiliriz


```
$ sudo journalctl -f -u lnd
```


### 14. Şimdi LND'e başlıyoruz


```
$ sudo su - bitcoin
$ lncli create
```


### 15. Düğüme fon ekleyin


```
$ lncli newaddress p2wkh
```

Artık LND tarafından döndürülen Address'ye btc gönderebilirsiniz.


bu komut ile bakiyeyi kontrol edebilirsiniz:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


İşlem onaylandıktan sonra bir kanal açabiliriz. Kanalı hangi node ile açacağınızı bilmiyorsanız, 1ml.com adresine gidebilir ve bir node seçebilirsiniz.


Bir düğüme bağlantı açın:


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


Sonra bir kanal açın:


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


Fonlarımızı kontrol edin:


```
$ lncli walletbalance
$ lncli channelbalance
```


Bekleyen ve aktif kanalları görüntüleyebiliyoruz:


```
$ lncli pendingchannels
$ lncli listchannels
```


Bir yıldırım Invoice ödemek için:


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


Bir ödeme almak için, belirli bir tutar için bir Invoice oluşturun:


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


Düğümüm hakkındaki bilgileri görüntülemek için:


```
$ lncli getinfo
```


Komutların tam listesi sadece lncli komutu çalıştırılarak görülebilir:


```
$ lncli
```


Son olarak, LND API'sine çağrı yapmak için:


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


Rehberin sonu!