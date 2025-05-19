---
name: Lightning Network Daemon (Linux)
description: Menginstal dan menjalankan Lightning Network Daemon di Linux
---

![cover-lightning-network-daemon](assets/cover.webp)



Lightning Network adalah Layer kedua dari Bitcoin, yang memungkinkannya untuk mengambil dimensi kilat, khususnya berkat kecepatan dan biaya rendah dari transaksi yang ditawarkannya.



Dalam tutorial ini, kita akan menginstal implementasi Lightning Network Daemon pada mesin Linux (distribusi Ubuntu 24.04).



## Apa itu Lightning Network Daemon?



Lightning Network Daemon adalah implementasi Go yang lengkap dari Lightning Network. Ini dibuat oleh Lightning Labs dan memungkinkan Anda menjalankan contoh penuh dari node Lightning pada mesin Anda.


Dengan kata lain, dengan implementasi ini, Anda dapat :





- Berinteraksi dengan Lightning Network**: Anda dapat menggunakan baris perintah untuk membuat portofolio Lightning, mengelola saluran dan rute pembayaran, dan masih banyak lagi, langsung dari terminal mesin Anda.
- Menautkan node Bitcoin jarak jauh atau instance Bitcoin Core Anda sendiri**: LND memungkinkan Anda menautkan instance Bitcoin dan menggunakannya sebagai backend. Untuk menggunakan implementasi ini, Anda tidak perlu menjalankan instance Bitcoin Core di mesin Anda.




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## Mengapa harus memiliki simpul Lightning Anda sendiri?


Lightning adalah hamparan Bitcoin yang mengoptimalkan proses transfer dan mengurangi biaya transaksi.



Dengan memutar simpul Lightning Anda, Anda mendapatkan kedaulatan dan otonomi. Anda memegang kendali atas dana Anda, jadi ingatlah:



"Bukan kunci Anda, bukan bitcoin Anda."



Dalam hal ini, menjalankan node Lightning meningkatkan keamanan dan integritas data Anda dengan cara-cara berikut:





- Kendali penuh**: Kelola saluran pembayaran Anda sendiri, jadilah bank Anda sendiri, dan jadilah penguasa aset Anda.
- Kerahasiaan**: Bertransaksi tanpa bergantung pada pihak ketiga untuk melindungi privasi Anda.
- Pembelajaran dan otonomi**: Berkat perintah `lncli`, Anda dapat lebih memahami proses yang mendasari Lightning dengan menerapkannya sendiri dari terminal Anda.
- Desentralisasi**: Berperan aktif dalam memperkuat dan mendesentralisasikan Bitcoin / Lightning Network.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


Anda memiliki dua opsi untuk menjalankan sebuah instans implementasi LND pada mesin kita. Kita dapat menyiapkan lingkungan pada mesin kita sendiri untuk berjalan secara lokal, atau menginstal LND dari kontainer Docker. Di sini, kita akan berkonsentrasi pada opsi pertama, dan melihat cara melanjutkan dengan Docker di tutorial selanjutnya.


## Instal LND dari kode sumber



### Prasyarat


Karena LND ditulis dalam bahasa Go, Anda harus memastikan bahwa Anda memiliki lingkungan GoLang dan ketergantungan yang diperlukan pada mesin Linux Anda.





- Persyaratan perangkat keras:** Persyaratan perangkat keras


Untuk pengalaman yang mulus dan lancar, mesin Anda harus memiliki kapasitas yang diperlukan untuk menjalankan node LND Lightning Anda.



Anda akan membutuhkan :


1. **RAM 8 GB** untuk kelancaran yang optimal,


2. **Prosesor multi-core (quad-core atau lebih)** untuk mengelola tindakan node Anda secara efisien,


3. **Ruang disk minimal 5GB** untuk mode pruned node dan 1TB untuk menjalankan Bitcoin Core (opsional jika menggunakan remote node)





- Instal dependensi yang berguna:**


Perintah di bawah ini akan memungkinkan Anda untuk menginstal pada mesin Anda alat yang Anda butuhkan untuk menjalankan LND. Di antaranya, Anda perlu menginstal `Git`, sebuah alat bantu versi, dan `make`, yang dapat menjalankan dan membangun implementasi LND dari kode sumber.



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- Instal GoLang pada mesin Linux Anda**



Pada tanggal tutorial ini, LND membutuhkan versi 1.23.6 dari Go*** untuk instalasi.



Jika Anda sudah menginstal versi sebelumnya, hapus versi tersebut untuk instalasi Go yang baru.


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- Konfigurasi lingkungan Go**


Pada berkas `~/.bashrc`, inisialisasi variabel lingkungan berikut ini untuk menambahkan Go pada sistem Linux Anda.



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- Memeriksa instalasi** (dalam bahasa Prancis)


```bash
go version
```



![go-version](assets/fr/03.webp)


### Mengkloning repositori GitHub LND



Gunakan git untuk mendapatkan salinan kode sumber LND secara lokal di mesin Anda


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### Membangun dan memasang



Alat `make`, yang telah terinstal sebelumnya, akan memungkinkan Anda untuk membuat eksekusi dari kode sumber LND dan melanjutkan instalasi.



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



Instal LND pada mesin Anda



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- Memeriksa instalasi Anda** (dalam bahasa Prancis)



Untuk memastikan semuanya berjalan dengan lancar, jalankan perintah ini dan Anda akan mendapatkan versi LND yang sedang Anda jalankan.



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


⚠️ **PENTING**: Pembaruan LND mungkin memerlukan versi Go yang lebih baru, jadi pastikan untuk memperbarui sistem Anda untuk menghindari masalah ketergantungan selama instalasi.


### Mengkonfigurasi Lightning Network Daemon



Konfigurasi node Lightning LND mirip dengan Bitcoin, dan dilakukan dalam file konfigurasi yang berisi semua parameter node Anda. Untuk melakukan ini, pada root mesin Anda, Anda dapat membuat folder tersembunyi `.LND` dan kemudian membuat file konfigurasi `LND.conf` dalam folder ini.



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





Dalam file konfigurasi, Anda dapat mengatur node LND Anda.



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



## Memahami konfigurasi Anda



Penting bagi Anda untuk memahami konfigurasi minimum yang Anda perlukan untuk pemasangan yang benar dan lengkap dari node LND Anda.



Berdasarkan isi file `~/.LND/LND.conf`, berikut ini adalah rincian bidangnya:





- pencadangan otomatis**: Memungkinkan Anda memilih apakah Anda ingin LND melakukan pencadangan otomatis pada portofolio Anda.  Mengatur properti ini ke `0` memungkinkan Anda menyimpan informasi pemulihan secara manual di lokasi aman yang dipilih secara pribadi.





- debuglevel**: Memungkinkan Anda menentukan tingkat detail kesalahan dan log jika terjadi kesalahan selama suatu tindakan.





- Bitcoin.active**: Menginstruksikan LND untuk beroperasi sebagai node Bitcoin dan berinteraksi dengan jaringan Bitcoin.





- Bitcoin.Mainnet**: Menentukan LND untuk menyambung ke jaringan utama Bitcoin (Mainnet), Anda dapat menetapkan nilai `bitcoind.signet` dan `bitcoind.regtest` masing-masing untuk jaringan Bitcoin Signet dan Bitcoin Regtest





- Bitcoin.node**: Menentukan jenis node Bitcoin yang akan disambungkan ke LND.





- Bitcoin.rpcuser** dan **Bitcoin.rpcpassword**: Mewakili.


masing-masing login (pengguna, kata sandi) untuk terhubung ke node Bitcoin Anda





- bitcoind.zmqpubrawblock** dan **bitcoind.zmqpubrawtx**: masing-masing mendefinisikan titik akhir ZeroMQ untuk menerima notifikasi tentang blok dan transaksi baru di jaringan Bitcoin.




## Memeriksa instalasi Anda dengan LND



Anda mungkin ingin memastikan bahwa prosesnya telah berhasil, dan Anda melakukan sinkronisasi dengan Lightning Network untuk menjaga agar informasi node Anda tetap mutakhir.



Untuk memulai implementasi LND dan mendapatkan informasi tentang node Anda, cukup ketik perintah :


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## Melakukan tindakan pada LND



Setelah instalasi selesai dan diperiksa, Anda dapat mulai menggunakannya.


Berikut ini adalah perintah-perintah penting untuk membantu Anda memulai.



### Membuat portofolio


Portofolio Lightning Anda adalah langkah pertama dalam tindakan apa pun untuk mengelola dana Anda.



⚠️ **PENTING**: Catatlah dengan cermat 24 kata **frase seed** Anda. Anda akan membutuhkannya untuk memulihkan dana Anda jika terjadi masalah.



Juga simpan kata sandi Wallet Anda sehingga Anda dapat membukanya dengan perintah `lncli unlock` ketika Anda me-restart node LND Anda.



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### Periksa saldo Anda



Konsultasikan akun Anda langsung dari terminal Anda:



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### Informasi tentang node Anda



Gunakan perintah di bawah ini untuk mengetahui saluran mana yang aktif pada node Anda.



```bash
lncli listchannels
```



Anda juga dapat memperoleh daftar node yang terhubung dengan Anda.



```bash
lncli listpeers
```



### Manajemen saluran



Saluran Lightning memungkinkan Anda untuk memiliki **sambungan langsung, berpasangan dengan node lain pada Lightning Network**. Di saluran ini, Anda dapat dengan bebas menggunakan Exchange Satoshi hingga kapasitas saluran.



### Menghubungkan ke sebuah simpul



Menghubungkan ke node Lightning lainnya adalah tindakan mendasar jika Anda ingin berpartisipasi aktif dan mendapatkan manfaat dari kekuatan Lightning.



Untuk menyambung ke peer (simpul Lightning), Anda memerlukan tiga informasi:




- Kunci publik node**: Ini adalah pengenal unik node dalam jaringan Bitcoin;
- IP** : IP mesin tempat node dipasang;
- PORT** :  Port yang terbuka pada mesin yang memungkinkan komunikasi dengan node ini.



Anda dapat menemukan node yang dapat disambungkan di [amboss](https://amboss.space/), sebuah platform yang mencantumkan informasi tentang node Lightning.



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




Pastikan Anda tersambung ke **simpul yang dapat diandalkan** untuk menjaga integritas sistem Anda. Berikut adalah beberapa rekomendasi untuk memilih koneksi yang tepat.





- Diversifikasi geografis**: Terhubung ke node di berbagai wilayah.





- Reputasi**: Pilih node dengan ketersediaan yang baik.





- Kapasitas**: Pilihlah simpul dengan likuiditas yang baik.





- Biaya**: Memeriksa biaya perutean.


### Buka saluran pembayaran


Untuk membuka saluran pembayaran, pastikan Anda **terhubung** ke peer node, lalu tentukan **kapasitas** (jumlah satoshi) yang ingin Anda blokir di saluran ini.



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### Membuat Lightning Invoice



Lightning Invoice mewakili serangkaian karakter yang mengekspresikan keinginan Anda untuk menerima satoshi dalam Lightning Wallet Anda.


Membuat faktur Lightning dengan node Anda sendiri memungkinkan Anda untuk melindungi data Anda (geografis dan pribadi) dan memberi Anda otonomi 100% atas pengelolaan dana Anda.



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### Membayar Lightning Invoice



```bash
lncli payinvoice <FACTURE>
```


### Menutup saluran



Ada dua cara untuk menutup saluran aktif pada node Anda saat ini.





- Penutupan koperasi**: Ini menandakan keinginan node Anda untuk menarik diri dari saluran pembayaran, memastikan bahwa tugas-tugas yang sedang berjalan telah selesai dan data dicadangkan untuk menghindari hilangnya dana.


```
lncli closechannel <ID_CANAL>
```




- Penutupan paksa**: ⚠️ Sebisa mungkin dihindari, karena tindakan ini akan mengganggu proses yang sedang berlangsung di saluran pembayaran Anda dan meningkatkan risiko kehilangan dana.


```
lncli closechannel --force <ID_CANAL>
```


## Praktik terbaik dan keamanan untuk node LND Anda.


Keamanan adalah hal yang paling penting ketika menggunakan Bitcoin/ Lightning node. Berikut adalah beberapa poin untuk memperkuat keamanan instalasi Anda:





- Simpanlah `frase seed` Anda di lokasi yang aman dan tidak terhubung.





- Buatlah cadangan secara teratur dari file `~/.LND/channel.backup`: File ini menyimpan status saluran anda setiap kali saluran baru dibuka (atau saluran lama ditutup) pada node anda.


⚠️ Memungkinkan Anda memulihkan saluran dan memulihkan dana yang diblokir di saluran pembayaran jika terjadi kehilangan data atau kegagalan node



Anda dapat memulihkan dana Anda dengan perintah di bawah ini dengan menentukan jalur cadangan file ini:


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Pastikan Anda telah menyimpan kata pemulihan dan kata sandi Lightning Wallet Anda.
- Selalu perbarui sistem Anda.



## Pemecahan masalah saat ini


### Masalah yang sering terjadi




- Kesalahan koneksi bitcoind **: Periksa detail login RPC Anda
- Sinkronisasi diblokir** : Memeriksa koneksi Internet Anda
- Kesalahan izin**: Periksa hak folder `~/.LND`




Jadi, Anda telah sampai pada akhir tutorial ini. Jika Anda ingin mempelajari lebih lanjut tentang Lightning, kami menawarkan kursus pengantar ini untuk memberi Anda pemahaman yang lebih baik tentang konsep dan praktik di balik Lightning Network.




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb