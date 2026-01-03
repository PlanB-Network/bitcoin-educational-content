---
name: Umbrel
description: Temukan dan instal Umbrel - Node Bitcoin dan server rumah kamu
---

![cover](assets/cover.webp)



## Pendahuluan



### Apa yang dimaksud dengan node Bitcoin?



Node Bitcoin adalah komputer yang ikut berpartisipasi di jaringan Bitcoin dengan menjalankan perangkat lunak Bitcoin Core atau klien alternatif. Perannya sangat penting untuk operasi dan keamanan jaringan.

- **Penyimpanan Blockchain**: Menyimpan salinan Blockchain Bitcoin yang lengkap dan terbaru
- **Verifikasi transaksi**: memvalidasi setiap transaksi dan blokir sesuai dengan aturan protokol
- **Penyebaran informasi**: Membagikan transaksi dan blok baru dengan node lain
- **Membangun konsensus**: Berkontribusi pada penerapan aturan jaringan

Menjalankan node Bitcoin kamu sendiri adalah langkah penting menuju kedaulatan finansial, yang menawarkan beberapa manfaat utama:

- **Kerahasiaan**: Bagikan transaksi kamu tanpa mengungkapkan informasimu sendiri kepada pihak ketiga
- **Ketahanan terhadap sensor**: Tidak ada yang bisa menghentikan kamu menggunakan Bitcoin
- **Verifikasi independen**: Tidak perlu mempercayai node orang lain untuk memverifikasi transaksi kamu
- **Membangun konsensus**: Berkontribusi pada penerapan aturan jaringan Bitcoin
- **Dukungan jaringan**: Menjadi peserta aktif dalam distribusi dan desentralisasi jaringan

### Payung: Solusi sederhana untuk menjalankan node Bitcoin

Umbrel adalah sistem operasi sumber terbuka yang menyederhanakan instalasi dan manajemen node Bitcoin. Sistem ini juga mengubah komputer kamu menjadi server rumah yang pribadi dan mudah dihosting, sehingga semuanya lebih sederhana buat kamu.

- Node Bitcoin yang lengkap
- Bitcoin aplikasi penting (Electrs, Mempool.space)
- Layanan pribadi lainnya (penyimpanan awan, streaming, VPN, dll.)

Dengan antarmuka yang elegan dan intuitif, Umbrel bikin layanan self hosted bisa diakses semua orang sambil tetap menjaga kontrol penuh atas data kamu.


## Opsi pemasangan payung



Umbrel menawarkan dua cara utama untuk menggunakan solusi mereka: opsi siap pakai (Umbrel Home) dan versi sumber terbuka gratis (UmbrelOS).



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### Umbrel Home: Solusi siap pakai

Umbrel Home adalah server rumah yang sudah dikonfigurasi sebelumnya dan dirancang khusus buat pengalaman yang optimal. Solusi perangkat keras all in one ini mencakup:

**Fitur perangkat keras**


- Prosesor berkinerja tinggi yang dioptimalkan untuk hosting mandiri
- Penyimpanan SSD berkecepatan tinggi yang sudah terpasang sebelumnya
- Sistem pendingin yang tenang
- Desain yang ringkas dan elegan
- Port USB dan Ethernet terintegrasi



**Manfaat eksklusif**




- Instalasi plug-and-play: colokkan dan gunakan
- Dukungan premium dengan bantuan khusus
- Pembaruan otomatis yang terjamin
- Panduan migrasi terintegrasi
- Garansi perangkat keras penuh
- Dukungan penuh untuk semua fungsi



**Harga**: €399 (harga dapat bervariasi tergantung musim)



### UmbrelOS: Versi sumber terbuka



UmbrelOS adalah versi sumber terbuka gratis dari sistem operasi Umbrel. Solusi yang fleksibel ini memungkinkan kamu memakai perangkat keras kamu sendiri sambil tetap menikmati fitur fitur utama Umbrel.


**Manfaat**




- Benar-benar gratis
- Kode sumber yang terbuka dan dapat diverifikasi
- Kebebasan memilih
- Opsi penyesuaian lanjutan



**Platform yang didukung**




- Raspberry Pi 5: Solusi yang populer dan terjangkau
- Sistem X86: Untuk PC atau server standar
- Mesin virtual: Untuk pengujian atau penggunaan pada infrastruktur yang ada



**Keterbatasan**




- Hanya dukungan komunitas
- Beberapa fitur canggih yang disediakan untuk Umbrel Home
- Konfigurasi awal yang lebih teknis
- Performa tergantung pada perangkat keras yang dipilih



Versi ini ideal untuk :




- Pengguna teknis
- Mereka yang sudah memiliki peralatan yang kompatibel
- Orang yang ingin belajar dan bereksperimen
- Pengembang yang ingin berkontribusi pada proyek



Tautan instalasi resmi :




- [Instalasi pada Raspberry Pi 5](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [Instalasi pada sistem x86 (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [Instalasi mesin virtual](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



Dalam tutorial ini, kita akan fokus ke instalasi UmbrelOS di Raspberry Pi 5, tapi prinsip dasarnya sama untuk platform lain.



## Menginstal Umbrel OS di Raspberry Pi 5



### Komponen yang diperlukan



Untuk instalasi ini, Anda memerlukan :





- Raspberry Pi 5 (RAM 4 GB atau 8 GB)
- Daya resmi Raspberry Pi Supply (sangat penting untuk stabilitas!)
- Kartu microSD (minimal 32 GB)
- Pembaca kartu microSD
- SSD eksternal untuk penyimpanan data
- Kabel Ethernet
- Kabel USB untuk menyambungkan SSD



### Langkah-langkah instalasi



**Unduh UmbrelOS**



![Téléchargement UmbrelOS](assets/fr/01.webp)




- Kunjungi [situs web resmi](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- Unduh versi terbaru UmbrelOS untuk Raspberry Pi 5



*pemasangan **Balena Etcher***



![Téléchargement Balena Etcher](assets/fr/02.webp)




- Unduh dan instal [Balena Etcher](https://www.balena.io/etcher/) di komputer kamu



**Mempersiapkan kartu microSD**



![Insertion carte microSD](assets/fr/03.webp)




- Masukkan kartu microSD ke pembaca kartu komputer kamu



**Gambar berkedip**



![Flashage UmbrelOS](assets/fr/04.webp)




- Luncurkan Balena Etcher
- Pilih gambar UmbrelOS yang diunduh
- Pilih kartu microSD kamu sebagai tujuan
- Klik "Flash!" dan tunggu sampai prosesnya selesai
- Mengeluarkan kartu dengan aman



**Pemasangan kartu microSD**



![Installation microSD](assets/fr/05.webp)




- Masukkan kartu microSD ke dalam Raspberry Pi 5 kamu



**Sambungan periferal ** Sambungan periferal



![Connexion périphériques](assets/fr/06.webp)




- Sambungkan SSD eksternal ke port USB yang tersedia
- Sambungkan kabel Ethernet antara Pi dan router kamu



**Nyalakan**



![Démarrage du Pi](assets/fr/07.webp)




- Hubungkan daya Raspberry Pi resmi Supply
- Tunggu beberapa menit hingga sistem memulai



**Akses pertama**



![Accès interface web](assets/fr/08.webp)




- Pada perangkat yang terhubung ke jaringan yang sama, buka browser kamu
- Akses situs web Interface Umbrel di: `http://umbrel.local`



![Page d'accueil Umbrel](assets/fr/09.webp)



Jika `umbrel.local` tidak berfungsi, kamu harus menemukan IP Address Raspberry Pi Anda di jaringan lokal kamu. Anda bisa:




- Konsultasikan dengan Interface router kamu
- Menggunakan pemindai jaringan seperti nmap
- Gunakan perintah `arp -a` di terminal komputer kamu



## Langkah pertama pada Umbrel



Setelah Umbrel kamu berjalan dan bisa diakses lewat browser, ikuti langkah langkah berikut untuk memulai:


### Konfigurasi awal



**Buat akun kamu**



![Création compte](assets/fr/10.webp)




- Memilih nama pengguna
- Mengatur kata sandi yang aman
- Kamu akan memerlukan kredensial ini untuk mengakses Umbrel kamu



**Konfirmasi akun**



![Confirmation compte](assets/fr/11.webp)




- Klik "Berikutnya" untuk mengakses dasbor kamu



**Penemuan Interface**



![Interface Umbrel](assets/fr/12.webp)




- Mengakses Toko Aplikasi Umbrel
- Temukan banyak aplikasi yang tersedia
- Mari kita mulai dengan menginstal aplikasi penting untuk Bitcoin



### Menginstal aplikasi Bitcoin



**Simpul Bitcoin**



![Bitcoin Node](assets/fr/13.webp)




- Aplikasi pertama yang dipasang
- Unduh dan periksa seluruh Blockchain Bitcoin



**Listrik**



![Installation Electrs](assets/fr/14.webp)




- Server Electrum untuk menghubungkan dompet Bitcoin
- Sinkronisasi dengan node Bitcoin kamu



** Mempool**



![Installation Mempool](assets/fr/15.webp)




- Tampilan Interface untuk Blockchain
- Melacak transaksi dan blokir secara real time



## Melacak transaksi dengan Mempool.space



Mempool.space adalah penjelajah blockchain sumber terbuka yang menyediakan visualisasi real time dari jaringan Bitcoin. Ini memungkinkan kamu melacak transaksi kamu dan memahami bagaimana transaksi menyebar di jaringan.


### Memahami Mempool dan konfirmasi



“Mempool” adalah ruang tunggu virtual tempat semua transaksi Bitcoin yang belum dikonfirmasi disimpan sebelum dimasukkan ke dalam blok. Begini cara sebuah transaksi diproses:


1. **Disiarkan**: Ketika kamu mengirim transaksi, transaksi tersebut pertama kali disiarkan di jaringan Bitcoin


2. **Menunggu di Mempool**: Menunggu untuk dipilih oleh Miner berdasarkan biaya


3. **Konfirmasi pertama**: Anak di bawah umur memasukkannya ke dalam blok (konfirmasi pertama)


4. **Konfirmasi tambahan**: Setiap blok baru yang ditambang setelah blok yang berisi transaksi Anda akan menambahkan konfirmasi



Jumlah konfirmasi yang direkomendasikan tergantung pada jumlahnya:




- Untuk jumlah kecil: 1-2 kali konfirmasi sudah cukup
- Untuk jumlah besar: 6 konfirmasi umumnya dianggap sangat aman



### Jelajahi Interface dari Mempool.space



1. **Halaman beranda** memberikan gambaran umum tentang jaringan Bitcoin:




   - Blok yang baru saja ditambang
   - Perkiraan biaya untuk prioritas yang berbeda
   - Kondisi Mempool saat ini



![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)



2. **Mencari transaksi**: Untuk melacak transaksi tertentu, tempelkan pengenalnya (txid) ke dalam bilah pencarian di bagian atas halaman.



![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)



### Menganalisis detail transaksi



Setelah transaksi kamu ditemukan, Mempool.space menyajikan analisis lengkap ke kamu:



1. **Informasi penting** :




   - Status (dikonfirmasi atau tidak)
   - Biaya yang dibayarkan (dalam Sats/vB)
   - Perkiraan waktu konfirmasi



![Détails des frais et statut de la transaction](assets/fr/25.webp)



2. **Struktur transaksi** :




   - Representasi visual dari input dan output
   - Daftar detail alamat yang terlibat
   - Jumlah yang ditransfer



3. **Data teknis**:




   - Bobot transaksi
   - Ukuran virtual
   - Format dan versi yang digunakan
   - Metadata spesifik lainnya



![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)



### Keuntungan menggunakan Mempool.space pada Umbrel



1. **Kerahasiaan**: Permintaan kamu melalui simpul Anda sendiri


2. **Kemandirian**: Tidak perlu bergantung pada layanan pihak ketiga


3. **Keandalan**: Akses ke data bahkan ketika browser publik sedang down



Dengan aplikasi ini, kamu bisa memantau transaksi kamu dengan efisien, memahami bagaimana biaya memengaruhi kecepatan konfirmasi, dan dapat pemahaman yang lebih baik tentang cara kerja jaringan Bitcoin.


## Menghubungkan Wallet Bitcoin ke node Anda



### Konfigurasi elektron



**Koneksi lokal**



![Connexion locale](assets/fr/18.webp)




- Untuk digunakan pada jaringan lokal kamu
- Lebih cepat dan lebih mudah diatur



**Koneksi jarak jauh melalui Tor**



![Connexion Tor](assets/fr/19.webp)




- Untuk mengakses node dari mana saja
- Lebih aman dan pribadi



### Koneksi dengan Sparrow Wallet



**Akses ke parameter**



![Paramètres Sparrow](assets/fr/20.webp)




- Open Sparrow Wallet
- Buka Preferensi > Server
- Klik "Ubah koneksi yang ada"



**Pilihan jenis koneksi**



Sparrow menawarkan tiga mode koneksi:



***Server Publik***




- Sambungan ke server publik (mis. blockstream.info, Mempool.space)
- Sederhana namun tidak terlalu pribadi



*** Inti Bitcoin***




- Koneksi langsung ke node Bitcoin
- Pribadi tetapi lebih lambat



**Private Electrum**




- Sambungkan ke server Electrs kamu
- Memadukan kerahasiaan dan kinerja



*konfigurasi* **Electrs**



Pilih jenis koneksi kamu dengan memakai informasi yang ditampilkan di aplikasi Electrs yang sudah kita lihat sebelumnya.


Pada kedua kasus tersebut, biarkan opsi "Gunakan SSL" dan "Gunakan proxy" tidak dicentang.



**Koneksi lokal**


Host: umbrel.local


Nomor port: 50001



**Sambungan jarak jauh (Tor)**


Tuan rumah: [your-Address-bawang]


Nomor port: 50001



Koneksi Tor diperlukan kalau kamu ingin mengakses node kamu dari luar jaringan lokal kamu.


![Configuration connexion](assets/fr/21.webp)


Untuk informasi lebih lanjut mengenai perangkat lunak Sparrow Wallet, kami memiliki tutorial yang komprehensif:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## Kesimpulan



Umbrel kamu sekarang siap dipakai. Kamu ikut berpartisipasi aktif di jaringan Bitcoin sambil tetap pegang kendali penuh atas data kamu. Jangan ragu buat jelajahi banyak aplikasi lain yang tersedia di Umbrel App Store untuk memperluas kemampuan server rumah kamu.


## Sumber daya yang berguna



### Dokumentasi resmi




- [Situs web resmi Umbrel](https://umbrel.com)
- [Dokumentasi payung](https://github.com/getumbrel/umbrel/wiki)
- [Payung App Store](https://apps.umbrel.com)



### Aplikasi Bitcoin




- [Bitcoin Core](https://Bitcoin.org/fr/)
- [Electrs](https://github.com/romanz/electrs)
- [Mempool](https://Mempool.space)
- [Sparrow Wallet](https://sparrowwallet.com)



### Komunitas




- [Forum Umbrel](https://community.getumbrel.com)
- [GitHub Umbrel](https://github.com/getumbrel)
- [Payung Twitter](https://twitter.com/umbrel)
