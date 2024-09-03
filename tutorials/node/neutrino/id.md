---
name: Neutrino
description: Panduan Instalasi LND Neutrino
---

# Konfigurasi Raspberry Pi dengan LND

1. Unduh Raspberry Pi OS Lite

Unduh Raspberry Pi OS Lite, instruksi untuk mengunduh dan menginstal gambar pada kartu micro SD di Windows, Mac, dan Linux dapat ditemukan di [halaman ini](https://www.raspberrypi.org/software/operating-systems/).

2. Format Kartu SD

Format kartu SD menggunakan Raspberry Pi Imager atau balenaEtcher.

> CATATAN: Simbol `$` digunakan sebagai prompt dan memungkinkan pengguna untuk memasukkan perintah ke dalam komputer, perintah akan diinterpretasikan oleh bash di Linux. Simbol `#` di awal baris menunjukkan bahwa teks berikut adalah komentar.

3. Aktifkan SSH

Sebelum memulai Raspberry Pi dengan memori yang telah diformat, kita harus memasukkannya ke dalam komputer dan membuat dua file yang akan memungkinkan kita untuk terhubung secara remote. Menggunakan perintah `touch`, kita membuat file kosong di partisi /boot, mengaktifkan koneksi SSH pada boot pertama dari kartu SD yang baru diformat.

```
# CATATAN: Jika kartu microSD telah dipasang di /media/microSD, perintahnya
# harusnya $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

4. Menggunakan perintah nano

kita membuat file wpa_supplicant.conf dan langsung mulai mengeditnya. Dalam file ini, kita perlu menyalin konfigurasi wifi, menyalin teks antara START dan END, dan memodifikasi SSID dan password dari wifi yang ingin Anda sambungkan.

```
$ nano /boot/wpa_supplicant.conf

------ MULAI -------
country=ar
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
 ssid="MyNetworkSSID"
 psk="password"
}
------ AKHIR -------
```

5. Koneksi

Kemudian, kita masukkan kartu SD ke dalam Raspberry Pi dan menghubungkan Pi ke sumber daya untuk memulai sistem operasi. Kita perlu mengidentifikasinya di jaringan, dan protokol mDNS kemungkinan akan menetapkan nama raspberrypi.local kepadanya. Mari kita coba terhubung via SSH.

```
$ ssh pi@raspberrypi.local
password: raspberry
```

Jika tidak berhasil, kita perlu mencari tahu jaringannya. Mari kita cari tahu alamat IP yang kita terhubung kepadanya.

```
$ ifconfig
```

Misalnya, jika itu adalah 192.168.0.0, gunakan nmap untuk menemukan Pi.

```
nmap -v 192.168.0.0/24
```

Dengan asumsi kita menemukan IP baru di jaringan kita, mari kita masuk via SSH.

```
$ ssh pi@192.168.0.30
password: raspberry
```

1. Konfigurasi Pi

```
$ sudo raspi-config
```

- Pilih opsi (1) dan ubah password untuk pengguna pi.
- Kita pilih opsi (8) untuk memperbarui alat konfigurasi ke versi terbaru
- Kita pilih opsi (4) untuk memilih zona waktu kita
- Kita pilih opsi (7) lalu Expand filesystem
- Selesai

  7.- Kita perbarui OS

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```

8.- Kita tambahkan pengguna bitcoin

```
$ sudo adduser bitcoin
```

9.- Kita amankan rpi

```
$ sudo apt install ufw
```
```
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ sudo ufw allow 22 comment 'izinkan SSH dari LAN'
$ sudo ufw allow 9735 comment 'izinkan Lightning'
$ sudo ufw allow 10009 comment 'Lightning gRPC'
$ sudo ufw enable
$ sudo systemctl enable ufw
$ sudo ufw status
$ sudo apt install fail2ban
```

10.- Kami menginstal go: jika Anda tidak menggunakan raspberry pi, unduh go untuk arsitektur Anda di sini (https://golang.org/dl/)

```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # seharusnya menampilkan pesan berikut 'go version go1.13.5 linux/arm'
```

11.- Kami mengkompilasi dan menginstal lnd

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

12.- Kami membuat file konfigurasi lnd, ini harus dilakukan dengan pengguna 'bitcoin'

```
$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf
```

```
[Application Options]
# mengaktifkan pembayaran spontan
accept-keysend=1

# Nama publik dari node
alias=YOUR_ALIAS
# Warna publik dalam heksadesimal
color=#000000
debuglevel=info
maxpendingchannels=5
listen=localhost
# soket gRPC
rpclisten=0.0.0.0:10009

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=neutrino

[neutrino]
neutrino.connect=bb2.breez.technology
```

13.- Untuk membuat LND mulai setelah boot rpi, kita harus membuat file .service di systemd.
Jika kita masuk sebagai pengguna bitcoin dan ingin kembali ke pengguna pi, kita cukup mengetik 'exit'

```
$ exit
$ sudo nano /etc/systemd/system/lnd.service
```

```
[Unit]
Description=LND Lightning Network Daemon
After=network.target

[Service]

# Eksekusi layanan
###################

ExecStart=/usr/local/bin/lnd


# Manajemen proses
####################

Type=simple
Restart=always
RestartSec=30
TimeoutSec=240
LimitNOFILE=128000

# Pembuatan direktori dan izin
####################################

# Jalankan sebagai bitcoin:bitcoin
User=bitcoin
Group=bitcoin

# /run/lightningd
RuntimeDirectory=lightningd
RuntimeDirectoryMode=0710

# Langkah-langkah pengerasan
####################

# Menyediakan /tmp dan /var/tmp yang privat.
```
```
PrivateTmp=true
# Pasang /usr, /boot/, dan /etc hanya-baca untuk proses.
ProtectSystem=full

# Melarang proses dan semua anaknya untuk mendapatkan
# hak istimewa baru melalui execve().
NoNewPrivileges=true

# Gunakan namespace /dev baru yang hanya diisi dengan perangkat pseudo API
# seperti /dev/null, /dev/zero, dan /dev/random.
PrivateDevices=true

# Tolak pembuatan pemetaan memori yang dapat ditulis dan dijalankan.
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

14. Sekarang kita mulai lnd

```
$ sudo su - bitcoin
$ lncli create
```

15. Tambahkan dana ke node kita

```
$ lncli newaddress p2wkh
```

Kirim btc ke alamat yang dikembalikan oleh lnd

Untuk memeriksa saldo

```
$ lncli walletbalance
{
    "total_balance": "500000",
    "confirmed_balance": "0",
    "unconfirmed_balance": "500000"
}
```

Setelah transaksi dikonfirmasi, kita dapat membuka saluran. Jika Anda tidak tahu node mana yang akan dibuka salurannya, Anda dapat pergi ke 1ml.com dan memilih node.

Buka koneksi ke node:

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```

Kemudian buka saluran

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```

Periksa dana kita

```
$ lncli walletbalance
$ lncli channelbalance
```

Kita dapat melihat saluran yang tertunda dan aktif

```
$ lncli pendingchannels
$ lncli listchannels
```

Untuk membayar faktur kilat

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```

Untuk menerima pembayaran, buat faktur untuk jumlah tertentu

```
$ lncli addinvoice --memo 'pembayaran pertama saya di LN' --amt 100
```

Untuk melihat informasi tentang node saya

```
$ lncli getinfo
```

Daftar lengkap perintah dapat dilihat dengan hanya menjalankan lncli

```
$ lncli
```

Akhirnya, untuk melakukan panggilan ke API lnd

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```

> AKHIR