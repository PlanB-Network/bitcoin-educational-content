---
name: Umbrel
description: Temukan dan instal Umbrel - Node Bitcoin dan server rumah Anda
---

![cover](assets/cover.webp)



## Pendahuluan



### Apa yang dimaksud dengan node Bitcoin?



Node Bitcoin adalah komputer yang berpartisipasi dalam jaringan Bitcoin dengan menjalankan perangkat lunak Bitcoin Core atau klien alternatif. Perannya sangat penting untuk pengoperasian dan keamanan jaringan:





- **Penyimpanan Blockchain**: Menyimpan salinan Blockchain Bitcoin yang lengkap dan terbaru
- **Verifikasi transaksi**: memvalidasi setiap transaksi dan blokir sesuai dengan aturan protokol
- **Penyebaran informasi**: Membagikan transaksi dan blok baru dengan node lain
- **Membangun konsensus**: Berkontribusi pada penerapan aturan jaringan



Menjalankan node Bitcoin Anda sendiri merupakan langkah penting menuju kedaulatan finansial, yang menawarkan beberapa manfaat utama:





- **Kerahasiaan**: Bagikan transaksi Anda tanpa mengungkapkan informasi Anda kepada pihak ketiga
- **Ketahanan terhadap sensor**: Tidak ada yang bisa menghentikan Anda menggunakan Bitcoin
- **Verifikasi independen**: Tidak perlu mempercayai node orang lain untuk memverifikasi transaksi Anda
- **Membangun konsensus**: Berkontribusi pada penerapan aturan jaringan Bitcoin
- **Dukungan jaringan**: Menjadi peserta aktif dalam distribusi dan desentralisasi jaringan



### Payung: Solusi sederhana untuk menjalankan node Bitcoin



Umbrel adalah sistem operasi sumber terbuka yang menyederhanakan instalasi dan manajemen node Bitcoin. Sistem ini juga mengubah komputer Anda menjadi server rumah pribadi dan pribadi, sehingga mudah untuk dihosting:





- Node Bitcoin yang lengkap
- Bitcoin aplikasi penting (Electrs, Mempool.space)
- Layanan pribadi lainnya (penyimpanan awan, streaming, VPN, dll.)



Dengan pengguna Interface yang elegan dan intuitif, Umbrel membuat layanan yang di-host sendiri dapat diakses oleh semua orang, sambil tetap mempertahankan kontrol penuh atas data Anda.



## Opsi pemasangan payung



Umbrel menawarkan dua cara utama untuk menggunakan solusi mereka: opsi siap pakai (Umbrel Home) dan versi sumber terbuka gratis (UmbrelOS).



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### Umbrel Home: Solusi siap pakai



Umbrel Home adalah server rumah yang telah dikonfigurasi sebelumnya, yang dirancang khusus untuk pengalaman yang optimal. Solusi perangkat keras all-in-one ini mencakup:



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



UmbrelOS adalah versi sumber terbuka gratis dari sistem operasi Umbrel. Solusi fleksibel ini memungkinkan Anda menggunakan perangkat keras Anda sendiri sambil memanfaatkan fitur-fitur penting Umbrel.



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




- [Instalasi pada Raspberry Pi 5] (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [Instalasi pada sistem x86 (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [Instalasi mesin virtual](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



Dalam tutorial ini, kita akan berkonsentrasi untuk menginstal UmbrelOS di Raspberry Pi 5, tetapi prinsip-prinsip dasarnya tetap sama untuk platform lain.



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




- Unduh dan instal [Balena Etcher](https://www.balena.io/etcher/) di komputer Anda



**Mempersiapkan kartu microSD**



![Insertion carte microSD](assets/fr/03.webp)




- Masukkan kartu microSD ke pembaca kartu komputer Anda



**Gambar berkedip**



![Flashage UmbrelOS](assets/fr/04.webp)




- Luncurkan Balena Etcher
- Pilih gambar UmbrelOS yang diunduh
- Pilih kartu microSD Anda sebagai tujuan
- Klik "Flash!" dan tunggu sampai prosesnya selesai
- Mengeluarkan kartu dengan aman



**Pemasangan kartu microSD**



![Installation microSD](assets/fr/05.webp)




- Masukkan kartu microSD ke dalam Raspberry Pi 5 Anda



**Sambungan periferal ** Sambungan periferal



![Connexion périphériques](assets/fr/06.webp)




- Sambungkan SSD eksternal ke port USB yang tersedia
- Sambungkan kabel Ethernet antara Pi dan router Anda



**Nyalakan**



![Démarrage du Pi](assets/fr/07.webp)




- Hubungkan daya Raspberry Pi resmi Supply
- Tunggu beberapa menit hingga sistem memulai



**Akses pertama**



![Accès interface web](assets/fr/08.webp)




- Pada perangkat yang terhubung ke jaringan yang sama, buka browser Anda
- Akses situs web Interface Umbrel di: `http://umbrel.local`



![Page d'accueil Umbrel](assets/fr/09.webp)



Jika `umbrel.local` tidak berfungsi, Anda harus menemukan IP Address Raspberry Pi Anda di jaringan lokal Anda. Anda bisa:




- Konsultasikan dengan Interface router Anda
- Menggunakan pemindai jaringan seperti nmap
- Gunakan perintah `arp -a` di terminal komputer Anda



## Langkah pertama pada Umbrel



Setelah Umbrel Anda dijalankan dan dapat diakses melalui browser Anda, ikuti langkah-langkah berikut untuk memulai:



### Konfigurasi awal



**Buat akun Anda**



![Création compte](assets/fr/10.webp)




- Memilih nama pengguna
- Mengatur kata sandi yang aman
- Anda akan memerlukan kredensial ini untuk mengakses Umbrel Anda



**Konfirmasi akun**



![Confirmation compte](assets/fr/11.webp)




- Klik "Berikutnya" untuk mengakses dasbor Anda



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
- Sinkronisasi dengan node Bitcoin Anda



** Mempool**



![Installation Mempool](assets/fr/15.webp)




- Tampilan Interface untuk Blockchain
- Melacak transaksi dan blokir secara real time



## Melacak transaksi dengan Mempool.space



Mempool.space adalah penjelajah Blockchain sumber terbuka yang menyediakan visualisasi real-time dari jaringan Bitcoin. Ini memungkinkan Anda melacak transaksi Anda dan memahami bagaimana transaksi menyebar di jaringan.



### Memahami Mempool dan konfirmasi



"Mempool" (kumpulan memori) adalah seperti ruang tunggu virtual di mana semua transaksi Bitcoin yang belum dikonfirmasi disimpan sebelum dimasukkan ke dalam blok. Berikut adalah bagaimana sebuah transaksi diproses:



1. **Disiarkan**: Ketika Anda mengirim transaksi, transaksi tersebut pertama kali disiarkan di jaringan Bitcoin


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



Setelah transaksi Anda ditemukan, Mempool.space menyajikan analisis lengkap kepada Anda:



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



1. **Kerahasiaan**: Permintaan Anda melalui simpul Anda sendiri


2. **Kemandirian**: Tidak perlu bergantung pada layanan pihak ketiga


3. **Keandalan**: Akses ke data bahkan ketika browser publik sedang down



Dengan aplikasi ini, Anda dapat memantau transaksi Anda secara efisien, memahami bagaimana biaya memengaruhi kecepatan konfirmasi, dan mendapatkan pemahaman yang lebih baik tentang cara kerja jaringan Bitcoin.



## Menghubungkan Wallet Bitcoin ke node Anda



### Konfigurasi elektron



**Koneksi lokal**



![Connexion locale](assets/fr/18.webp)




- Untuk digunakan pada jaringan lokal Anda
- Lebih cepat dan lebih mudah diatur



**Koneksi jarak jauh melalui Tor**



![Connexion Tor](assets/fr/19.webp)




- Untuk mengakses node Anda dari mana saja
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




- Sambungkan ke server Electrs Anda
- Memadukan kerahasiaan dan kinerja



*konfigurasi* **Electrs**



Pilih jenis koneksi Anda menggunakan informasi yang ditampilkan di aplikasi Electrs yang telah kita lihat sebelumnya:



Pada kedua kasus tersebut, biarkan opsi "Gunakan SSL" dan "Gunakan proxy" tidak dicentang.



**Koneksi lokal**


Host: umbrel.local


Nomor port: 50001



**Sambungan jarak jauh (Tor)**


Tuan rumah: [your-Address-bawang]


Nomor port: 50001



Sambungan Tor diperlukan jika Anda ingin mengakses node Anda di luar jaringan lokal Anda.



![Configuration connexion](assets/fr/21.webp)


Untuk informasi lebih lanjut mengenai perangkat lunak Sparrow Wallet, kami memiliki tutorial yang komprehensif:


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## Kesimpulan



Umbrel Anda sekarang siap digunakan. Anda berpartisipasi secara aktif dalam jaringan Bitcoin dengan tetap memegang kendali penuh atas data Anda. Jangan ragu untuk menjelajahi banyak aplikasi lain yang tersedia di Umbrel App Store untuk memperluas kemampuan server rumah Anda.



## Sumber daya yang berguna



### Dokumentasi resmi




- [Situs web resmi Umbrel](https://umbrel.com)
- [Dokumentasi payung](https://github.com/getumbrel/umbrel/wiki)
- [Payung App Store](https://apps.umbrel.com)



### Aplikasi Bitcoin




- [Bitcoin Core](https://Bitcoin.org/fr/)
- [Electrs](https://github.com/romanz/electrs)
- [Mempool] (https://Mempool.space)
- [Sparrow Wallet] (https://sparrowwallet.com)



### Komunitas




- [Forum Umbrel](https://community.getumbrel.com)
- [GitHub Umbrel](https://github.com/getumbrel)
- [Payung Twitter](https://twitter.com/umbrel)