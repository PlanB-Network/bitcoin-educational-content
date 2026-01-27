---
name: Lightning Network Daemon (Linux)
description: Menginstal dan menjalankan Lightning Network Daemon di Linux
---

![cover-lightning-network-daemon](assets/cover.webp)



Lightning Network adalah layer kedua di atas Bitcoin yang bikin jaringan ini bisa beroperasi secepat kilat, terutama berkat transaksi yang cepat dan berbiaya rendah.

Di tutorial ini, kita akan menginstal implementasi Lightning Network Daemon di mesin Linux dengan distribusi Ubuntu 24.04.



## Apa itu Lightning Network Daemon?



Lightning Network Daemon adalah implementasi lengkap Lightning Network yang ditulis dengan Go. Ini dibuat oleh Lightning Labs dan memungkinkan kamu menjalankan satu instance penuh node Lightning di mesin kamu.

Dengan kata lain, dengan implementasi ini, kamu bisa :

- **Berinteraksi dengan Lightning Network**: Kamu bisa pakai baris perintah untuk bikin wallet Lightning, mengelola channel dan rute pembayaran, dan banyak hal lain, langsung dari terminal mesin kamu.
- **Menautkan node Bitcoin jarak jauh atau instance Bitcoin Core Anda sendiri**: LND memungkinkan kamu menautkan instance Bitcoin dan memakainya sebagai backend. Untuk pakai implementasi ini, kamu nggak harus menjalankan instance Bitcoin Core di mesin kamu.


https://planb.academy/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## Mengapa harus memiliki simpul Lightning Anda sendiri?


Lightning adalah layer di atas Bitcoin yang mengoptimalkan proses transfer dan menurunkan biaya transaksi.

Dengan menjalankan node Lightning kamu, kamu dapat kedaulatan dan otonomi penuh. Kamu pegang kendali atas dana kamu, jadi ingat:

"Bukan kunci kamu, bukan bitcoin kamu."

Dalam konteks ini, menjalankan node Lightning meningkatkan keamanan dan integritas data kamu lewat cara-cara berikut:





- **Kendali penuh**: Kelola saluran pembayaran kamu sendiri, jadilah bank kamu sendiri, dan jadilah penguasa aset milikmu.
- **Kerahasiaan**: Bertransaksi tanpa bergantung pada pihak ketiga untuk melindungi privasi kamu.
- **Pembelajaran dan otonomi**: Berkat perintah `lncli`, kamu bisa lebih memahami proses yang mendasari Lightning dengan menerapkannya sendiri dari terminal kamu.
- **Desentralisasi**: Berperan aktif dalam memperkuat dan mendesentralisasikan Bitcoin / Lightning Network.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c


Kamu punya dua opsi untuk menjalankan satu instance LND di mesin kita. Kita bisa nyiapin lingkungan langsung di mesin kita sendiri supaya jalan secara lokal, atau menginstal LND lewat kontainer Docker. Di sini, kita bakal fokus ke opsi pertama, dan bakal bahas cara lanjut pakai Docker di tutorial berikutnya.

## Instal LND dari kode sumber



### Prasyarat


Karena LND ditulis dengan Go, kamu perlu memastikan kalau lingkungan GoLang dan semua dependensi yang dibutuhin sudah ada di mesin Linux kamu.





- **Persyaratan perangkat keras:** 


Biar pengalaman tetap mulus, mesin kamu harus punya kapasitas yang cukup untuk menjalankan node LND Lightning kamu.


Kamu akan membutuhkan :


1. **RAM 8 GB** untuk kelancaran yang optimal,


2. **Prosesor multi-core (quad-core atau lebih)** untuk mengelola tindakan node kamu secara efisien,


3. **Ruang disk minimal 5GB** untuk mode pruned node dan 1TB untuk menjalankan Bitcoin Core (opsional kalau menggunakan remote node)





- Instal dependensi yang berguna:


Perintah di bawah ini bakal kasih kamu semua alat yang dibutuhin untuk jalanin LND di mesin kamu. Di antaranya, kamu perlu instal `Git` sebagai alat versi, dan `make` untuk ngejalanin dan membangun implementasi LND dari kode sumber.



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- **Instal GoLang pada mesin Linux kamu**



Pada tanggal tutorial ini, LND membutuhkan versi 1.23.6 dari **Go** untuk instalasi.



Kalau kamu sudah menginstal versi sebelumnya, hapus versi tersebut untuk instalasi Go yang baru.


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- **Konfigurasi lingkungan Go**


Pada berkas `~/.bashrc`, Inisialisasi variabel lingkungan berikut untuk nambahin Go ke sistem Linux kamu.



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- Memeriksa **instalasi** (dalam bahasa Prancis)


```bash
go version
```



![go-version](assets/fr/03.webp)


### Mengkloning repositori GitHub LND



Gunakan git untuk dapatkan salinan kode sumber LND secara lokal di mesin kamu.


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### Membangun dan memasang



Alat `make` yang sudah kamu instal sebelumnya bakal ngebantu kamu bikin file eksekusi dari kode sumber LND dan lanjut ke proses instalasinya.



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



Instal LND pada mesin kamu



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- **Memeriksa instalasi Anda** (dalam bahasa Prancis)



Untuk memastikan semuanya berjalan lancar, jalankan perintah ini dan kamu bakal lihat versi LND yang lagi kamu pakai.


```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- Pemeliharaan dan peningkatan



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **PENTING**: Pembaruan LND kadang butuh versi Go yang lebih baru, jadi pastikan kamu memperbarui sistem kamu biar nggak kena masalah dependensi waktu instalasi.

### Mengkonfigurasi Lightning Network Daemon



Konfigurasi node Lightning LND mirip dengan Bitcoin dan dilakukan lewat file konfigurasi yang berisi semua parameter node kamu. Untuk itu, di root mesin kamu, kamu bisa bikin folder tersembunyi `.LND`, lalu bikin file konfigurasi `LND.conf` di dalam folder itu.



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





Di file konfigurasi itu, kamu bisa ngatur semua parameter untuk node LND kamu.


```
noseedbackup=0
debuglevel=debug

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=bitcoind

[Bitcoind]
bitcoind.rpcuser=<UTILISATEUR_BITCOIN>
bitcoind.rpcpassword=<MOT_DE_PASSE_BITCOIN>
bitcoind.zmqpubrawblock=tcp://127.0.0.1:28332
bitcoind.zmqpubrawtx=tcp://127.0.0.1:28333

```



## Memahami konfigurasi kamu



Penting buat kamu paham konfigurasi minimum yang dibutuhin supaya pemasangan node LND kamu berjalan dengan benar dan lengkap.


Berdasarkan isi file `~/.LND/LND.conf`, berikut ini adalah rincian bidangnya:





- **pencadangan otomatis**: Ini memungkinkan kamu milih apakah LND mau bikin backup otomatis untuk wallet kamu. Kalau diatur ke `0`, kamu bisa nyimpen informasi pemulihan secara manual di lokasi aman yang kamu pilih sendiri.





- **debuglevel**: Ini memungkinkan kamu nentuin tingkat detail untuk kesalahan dan log kalau terjadi masalah saat suatu aksi dijalankan.




- **Bitcoin.active**: Menginstruksikan LND untuk beroperasi sebagai node Bitcoin dan berinteraksi dengan jaringan Bitcoin.





- **Bitcoin.Mainnet**: Buat nentuin LND supaya tersambung ke jaringan utama Bitcoin (Mainnet), kamu bisa atur `bitcoind.signet` dan `bitcoind.regtest` untuk masing-masing jaringan Bitcoin Signet dan Bitcoin Regtest.





- **Bitcoin.node**: Menentukan jenis node Bitcoin yang akan disambungkan ke LND.





- **Bitcoin.rpcuser** dan **Bitcoin.rpcpassword**: Mewakili.


masing-masing login (username dan password) untuk tersambung ke node Bitcoin kamu




- **bitcoind.zmqpubrawblock** dan **bitcoind.zmqpubrawtx**: masing-masing mendefinisikan endpoint ZeroMQ untuk menerima notifikasi tentang blok dan transaksi baru di jaringan Bitcoin.




## Memeriksa instalasi Anda dengan LND



Kamu mungkin mau memastikan prosesnya berhasil, dan node kamu tersinkronisasi dengan Lightning Network supaya informasi tetap up-to-date.

Buat memulai implementasi LND dan melihat informasi tentang node kamu, cukup ketik perintah berikut:

```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## Melakukan tindakan pada LND



Setelah instalasi selesai dan dicek, kamu bisa langsung mulai menggunakannya.

Berikut beberapa perintah penting untuk bantu kamu memulai.


### Membuat portofolio


Wallet Lightning kamu adalah langkah pertama dalam setiap tindakan untuk ngelola dana kamu.


⚠️ **PENTING**: Catatlah dengan cermat 24 kata **seedphrase** kamu. Kamu bakal butuhin ini buat memulihkan dana kamu kalau terjadi masalah.


Jangan lupa simpan juga password wallet kamu supaya bisa dibuka dengan perintah `lncli unlock` saat kamu me-restart node LND kamu.


```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### Periksa saldo kamu



Konsultasikan akun kamu langsung dari terminal:



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### Informasi tentang node Anda



Gunakan perintah di bawah ini untuk lihat channel mana yang sedang aktif di node kamu.


```bash
lncli listchannels
```



Kamu juga bisa dapetin daftar node yang tersambung dengan node kamu.


```bash
lncli listpeers
```



### Manajemen saluran


Channel Lightning memungkinkan kamu punya **koneksi langsung, berpasangan dengan node lain di Lightning Network.** Di channel ini, kamu bisa bebas pakai Satoshi Exchange sampai kapasitas channel tercapai.



### Menghubungkan ke sebuah simpul


Menyambung ke node Lightning lain adalah langkah dasar kalau kamu mau berpartisipasi aktif dan merasakan manfaat dari kekuatan Lightning.

Buat tersambung ke peer (node Lightning), kamu butuh tiga informasi berikut:




- **Kunci publik node**: Ini adalah pengenal unik node dalam jaringan Bitcoin;
- **IP** : IP mesin tempat node dipasang;
- **PORT** :  Port yang terbuka pada mesin yang memungkinkan komunikasi dengan node ini.



Kamu bisa menemukan node yang dapat disambungkan di [amboss](https://amboss.space/), sebuah platform yang mencantumkan informasi tentang node Lightning.



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




Pastikan kamu tersambung ke **simpul yang dapat diandalkan** untuk menjaga integritas sistem kamu. Berikut adalah beberapa rekomendasi untuk memilih koneksi yang tepat.





- **Diversifikasi geografis**: Terhubung ke node di berbagai wilayah.





- **Reputasi**: Pilih node dengan ketersediaan yang baik.





- **Kapasitas**: Pilihlah simpul dengan likuiditas yang baik.





- **Biaya**: Memeriksa biaya perutean.


### Buka saluran pembayaran


Untuk membuka saluran pembayaran, pastikan kamu **terhubung** ke peer node, lalu tentukan **kapasitas** (jumlah satoshi) yang ingin kamu blokir di saluran ini.



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### Membuat Lightning Invoice



Lightning Invoice adalah rangkaian karakter yang mengekspresikan permintaan kamu untuk menerima satoshi di Lightning Wallet kamu.

Bikin invoice Lightning lewat node kamu sendiri memungkinkan kamu melindungi data kamu (lokasi dan pribadi) serta memberi otonomi penuh 100% atas pengelolaan dana kamu.


```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### Membayar Lightning Invoice



```bash
lncli payinvoice <FACTURE>
```


### Menutup saluran



Ada dua cara buat menutup channel yang sedang aktif di node kamu saat ini.




- **Penutupan koperasi**: Ini menandakan keinginan node kamu untuk menarik diri dari channel pembayaran, memastikan semua transaksi yang sedang berjalan selesai dan data dicadangkan supaya dana kamu tidak hilang.


```
lncli closechannel <ID_CANAL>
```




- **Penutupan paksa**: ⚠️ Sebaiknya dihindari, karena tindakan ini bakal mengganggu proses yang sedang berlangsung di channel pembayaran kamu dan menambah risiko kehilangan dana.

```
lncli closechannel --force <ID_CANAL>
```


## Praktik terbaik dan keamanan untuk node LND Anda.


Keamanan adalah hal paling penting saat pakai node Bitcoin atau Lightning. Berikut beberapa tips buat memperkuat keamanan instalasi kamu:





- Simpanlah 'seedphrase` kamu di lokasi yang aman dan tidak terhubung.





- Buatlah cadangan secara teratur dari file `~/.LND/channel.backup`: File ini nyimpen status channel kamu setiap kali channel baru dibuka atau channel lama ditutup di node kamu.


⚠️ Ini memungkinkan kamu memulihkan channel dan dana yang terkunci di channel pembayaran kalau terjadi kehilangan data atau kegagalan node.



Kamu bisa memulihkan dana kamu dengan perintah di bawah ini dengan menentukannya ke jalur file backup ini:

```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Pastikan kamu sudah menyimpan kata pemulihan dan password Lightning Wallet kamu.
- Selalu perbarui sistem kamu.



## Pemecahan masalah saat ini


### Masalah yang sering terjadi




- **Kesalahan koneksi bitcoind**: Periksa detail login RPC 
- **Sinkronisasi diblokir**: Memeriksa koneksi Internet 
- **Kesalahan izin**: Periksa hak folder `~/.LND`




Jadi, kamu sudah sampai di akhir tutorial ini. Kalau mau belajar lebih lanjut tentang Lightning, kami menyediakan kursus pengantar yang bakal memberi kamu pemahaman lebih dalam tentang konsep dan praktik di balik Lightning Network.



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
