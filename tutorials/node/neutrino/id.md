---
name: Neutrino
description: Panduan Instalasi Neutrino LND
---
![image](assets/cover.webp)


## Konfigurasi Raspberry Pi dengan LND


### 1. Unduh Raspberry Pi OS Lite


Petunjuk untuk mengunduh dan menginstal gambar pada kartu micro SD pada Windows, Mac, dan Linux dapat ditemukan di [halaman ini](https://www.raspberrypi.org/software/operating-systems/).


### 2. Memformat Kartu SD


Gunakan Raspberry Pi Imager atau balenaEtcher.


**Catatan:** Simbol `$` digunakan sebagai prompt dan memungkinkan pengguna untuk memasukkan perintah ke dalam komputer, perintah tersebut akan diinterpretasikan oleh bash di Linux. Simbol `#` pada awal baris menunjukkan bahwa teks berikut adalah sebuah komentar.


### 3. Mengaktifkan SSH


Sebelum memulai Raspberry Pi dengan memori yang telah diformat, kita harus memasukkannya ke dalam komputer dan membuat dua file yang memungkinkan kita untuk terhubung dari jarak jauh. Dengan menggunakan perintah `touch`, kami membuat file kosong di partisi /boot, memungkinkan koneksi SSH pada boot pertama dari kartu SD yang baru saja diformat.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4. Membuat file untuk koneksi Wi-Fi


Dengan menggunakan perintah nano kita membuat berkas `wpa_supplicant.conf` dan langsung mulai mengeditnya. Dalam file ini, kita perlu menyalin konfigurasi wifi, menyalin teks antara START dan END, dan memodifikasi SSID dan kata sandi wifi yang ingin Anda sambungkan.


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


### 5. Koneksi


Kemudian, kami memasukkan kartu SD ke dalam Raspberry Pi dan menghubungkan Pi ke sumber listrik untuk memulai sistem operasi. Kita perlu mengidentifikasinya di jaringan, dan protokol mDNS kemungkinan akan memberikan nama raspberrypi.local padanya. Mari kita coba terhubung melalui SSH.


```
$ ssh pi@raspberrypi.local
password: raspberry
```


Jika tidak berhasil, kita perlu mencari tahu jaringannya. Mari kita cari tahu IP Address yang terhubung dengan kita.


```
$ ifconfig
```


Sebagai contoh, jika 192.168.0.0, gunakan nmap untuk menemukan Pi.


```
nmap -v 192.168.0.0/24
```


Dengan asumsi kita menemukan IP baru di jaringan kita, mari kita masuk melalui SSH.


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6. Konfigurasikan Pi


```
$ sudo raspi-config
```


- Pilih opsi (1) dan ubah kata sandi untuk pengguna pi.
- Kami memilih opsi (8) untuk memperbarui alat konfigurasi ke versi terbaru
- Kami memilih opsi (4) untuk memilih zona waktu kami
- Kami memilih opsi (7) dan kemudian Perluas sistem file
- Selesai


### 7. Sekarang perbarui OS


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8. Menambahkan pengguna Bitcoin


```
$ sudo adduser bitcoin
```


### 9. Mengamankan rpi


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


### 10. Instal Go


Jika Anda tidak menggunakan raspberry pi, unduh go untuk arsitektur Anda [di sini](https://golang.org/dl/).


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11. Mengkompilasi dan menginstal LND


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


### 12. Membuat file conf LND


Buat berkas konfigurasi LND, ini harus dilakukan dengan pengguna 'Bitcoin'


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


### 13. Mulai otomatis layanan LND


Untuk membuat LND memulai setelah boot rpi, kita harus membuat file .service di systemd. Jika kita masuk sebagai pengguna Bitcoin dan ingin kembali ke pengguna pi, kita cukup mengetikkan 'exit'


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


Kita dapat melihat log dengan menjalankan perintah journalctl


```
$ sudo journalctl -f -u lnd
```


### 14. Sekarang kita mulai LND


```
$ sudo su - bitcoin
$ lncli create
```


### 15. Menambahkan dana ke node


```
$ lncli newaddress p2wkh
```

Anda sekarang dapat mengirim BTC ke Address yang dikembalikan oleh LND.


dengan perintah ini, Anda dapat memeriksa saldo:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


Setelah transaksi dikonfirmasi, kita dapat membuka channel. Jika Anda tidak tahu node mana yang akan digunakan untuk membuka saluran, Anda dapat mengunjungi 1ml.com dan memilih node.


Buka koneksi ke sebuah node:


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


Kemudian buka saluran:


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


Periksa dana kami:


```
$ lncli walletbalance
$ lncli channelbalance
```


Kita dapat melihat saluran yang tertunda dan saluran yang aktif:


```
$ lncli pendingchannels
$ lncli listchannels
```


Untuk membayar petir Invoice:


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


Untuk menerima pembayaran, buatlah Invoice dengan jumlah tertentu:


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


Untuk melihat informasi tentang node saya:


```
$ lncli getinfo
```


Daftar lengkap perintah dapat dilihat hanya dengan menjalankan perintah lncli:


```
$ lncli
```


Terakhir, untuk melakukan panggilan ke API LND:


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


AKHIR panduan!