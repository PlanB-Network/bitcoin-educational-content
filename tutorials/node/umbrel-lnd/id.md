---
name: Umbrel LND
description: Tutorial lanjutan tentang cara menginstal dan mengonfigurasi Lightning Network Daemon (LND) pada Umbrel
---
![cover](assets/cover.webp)




## Pendahuluan



Tutorial tingkat lanjut ini akan memandu kamu langkah demi langkah melalui instalasi, konfigurasi, dan penggunaan aplikasi Lightning Node (LND) pada node Umbrel kamu. Kamu akan belajar cara membuka channel, mengelola likuiditas, dan menyinkronkan node kamu dengan aplikasi seluler.


## 1. Prasyarat: simpul Bitcoin Umbrel yang fungsional


Sebelum menggunakan Lightning, kamu harus memiliki node Bitcoin yang beroperasi penuh pada Umbrel. Ini melibatkan pemasangan Umbrel (pada Raspberry Pi, NAS, atau mesin lain) dan menyinkronkan blockchain Bitcoin sepenuhnya.

Untuk menginstal Umbrel dan mengonfigurasi node Bitcoin kamu, aku sarankan kamu mengikuti tutorial khusus kami:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Pastikan node Bitcoin kamu sudah diperbarui dan berfungsi dengan baik, karena Lightning Network bergantung pada node ini untuk semua transaksi off-chain.


## 2. Pengantar ke Lightning Network



Lightning Network adalah protokol Layer kedua yang dirancang untuk mempercepat dan mengurangi biaya transaksi Bitcoin dengan melaksanakannya di luar blockchain utama.

Secara konkret, Lightning menggunakan jaringan channel pembayaran antar node: dua pengguna membuka channel dengan mengunci BTC on-chain (transaksi awal), lalu bisa langsung melakukan pembayaran di dalam channel ini. Transaksi off-chain ini tidak dicatat pada blockchain, sehingga kecepatannya dan biayanya hampir nol.

Pembayaran bisa disalurkan melalui berbagai channel (berkat node perantara) untuk menjangkau penerima mana pun di jaringan, memungkinkan skala transaksi instan yang hampir tak terbatas. Dengan demikian, Lightning menawarkan transaksi yang sangat cepat dan berbiaya rendah, ideal untuk pembayaran sehari-hari atau transaksi mikro, sekaligus meringankan beban pada blockchain Bitcoin.

Untuk beroperasi, node Lightning harus terhubung secara permanen ke jaringan dan berinteraksi dengan node Lightning lainnya. Berbagai implementasi perangkat lunak tersedia (LND, Core Lightning, Eclair, dll.), yang semuanya kompatibel satu sama lain. Umbrel menggunakan LND (Lightning Network Daemon) sebagai bagian dari aplikasi Lightning Node resminya. Tutorial ini berfokus pada LND.

Untuk pengenalan teoretis yang lengkap mengenai Lightning Network, aku sarankan kamu mengikuti kursus khusus kami:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Kursus ini akan memberi kamu dasar yang menyeluruh dalam konsep dasar Lightning Network, sebelum lanjut ke praktik dengan node LND kamu.



## 3. Mengapa menjadi tuan rumah sendiri LND?



Mengoperasikan Lightning node (LND) kamu sendiri di Umbrel memberi kamu kedaulatan penuh atas dana dan channel kamu, dibandingkan dengan solusi kustodian atau semi-kustodian.


### Perbandingan solusi Lightning :



**Solusi kustodian (contoh: Wallet dari Satoshi)**:



- Bitcoin Lightning kamu dikelola oleh pihak ketiga yang tepercaya
- Mudah digunakan, tanpa kerumitan teknis
- Operator menyimpan dana kamu dan bisa melacak transaksi kamu
- Kamu mengorbankan kontrol dan kerahasiaan


**Portofolio konsumen non-komoditas (mis. Phoenix, Breez)**:




- Pengguna mempertahankan kunci pribadi mereka dan dengan demikian Ownership dari BTC mereka
- Tidak ada manajemen node yang lengkap - aplikasi mengelola saluran di latar belakang
- Kompromi antara kesederhanaan dan kedaulatan
- Ketergantungan pada infrastruktur pemasok untuk likuiditas
- Keterbatasan teknis (satu ponsel pintar tidak dapat merutekan pembayaran untuk orang lain)



**Node LND yang dihosting sendiri (Umbrel)**:




- Kedaulatan maksimum: On-Chain dan off-chain BTC sepenuhnya berada di bawah kendali kamu
- Tidak ada pihak ketiga yang terlibat dalam membuka saluran atau mengelola pembayaran kamu
- Kerahasiaan yang lebih tinggi (saluran dan transaksi kamu hanya diketahui oleh kamu dan rekan-rekan)
- Kebebasan penggunaan: terhubung ke layanan dan dompet Anda sendiri
- Kemungkinan merutekan transaksi untuk orang lain (remunerasi biaya mikro)
- Peningkatan tanggung jawab teknis (pemeliharaan, manajemen likuiditas, pencadangan)



Singkatnya, self-hosting LND memberi Anda kontrol maksimum, tetapi membutuhkan lebih banyak keterampilan teknis. Ini adalah pertukaran antara kenyamanan dan kedaulatan.



## 4. Tutorial langkah demi langkah



### 4.1 Menginstal dan mengonfigurasi aplikasi Lightning Node pada Umbrel



Setelah node Umbrel (Bitcoin) kamu disinkronkan, ikuti langkah-langkah berikut:



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



Instal aplikasi Lightning Node dari bagian "App Store" pada Payung Interface.



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



LND (Lightning Network Daemon) akan digunakan pada Umbrel kamu sebagai aplikasi. Saat pertama kali membukanya, kamu akan melihat pesan peringatan yang memberitahukan bahwa Lightning adalah teknologi eksperimental.



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



Kamu bisa memilih antara membuat node baru atau memulihkan node dari cadangan/seed. Untuk pemasangan pertama kali, pilih untuk membuat node baru. Aplikasi Lightning Node akan generate mnemonic 24 kata (seed Lightning kamu): tulis dengan sangat hati-hati (idealnya secara offline, di atas kertas), karena ini akan digunakan untuk memulihkan dana Lightning kamu jika diperlukan.



**Catatan: Pada versi terbaru Umbrel, instalasi aplikasi Lightning menyediakan seed 24 kata ini (simpul Bitcoin Umbrel itu sendiri tidak).**



![Interface principale de Lightning Node](assets/fr/04.webp)



Setelah inisialisasi, kamu akan mengakses Interface utama Lightning Node.



![Paramètres de l'application](assets/fr/05.webp)



Dalam pengaturan aplikasi, kamu akan menemukan sejumlah opsi penting:




   - Lihat ID Node (pengenal unik node kamu)
   - Menghubungkan Wallet eksternal (Menghubungkan Wallet)
   - Lihat kata-kata rahasia
   - Mengakses Pengaturan Lanjutan
   - Memulihkan saluran
   - Unduh file cadangan saluran
   - Mengaktifkan pencadangan otomatis
   - Konfigurasikan pencadangan melalui Tor (Pencadangan melalui Tor)



Opsi-opsi ini sangat penting untuk keamanan dan manajemen node Lightning kamu. Pastikan kamu mengaktifkan pencadangan otomatis dan menyimpan kata-kata rahasia kamu dengan aman.


**Sumber daya yang berguna:**




- [Komunitas Umbrel](https://community.umbrel.com) - Forum diskusi bagi pengguna untuk berbagi masalah dan solusi mengenai Umbrel dan ekosistemnya


> - [Umbrel App Store - Lightning Node (LND)](https://apps.umbrel.com/app/lightning) - Deskripsi fitur aplikasi Lightning Node di Umbrel
> - [LND Docs - Quickstart](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - Dokumentasi resmi LND

### 4.2 Membuka saluran Lightning



Setelah LND aktif dan berjalan, kamu bisa membuka channel Lightning pertama kamu. Untuk menemukan node berkualitas untuk disambungkan:


![Page d'accueil Amboss.space](assets/fr/06.webp)



[Amboss.space](https://amboss.space/) adalah penjelajah untuk menemukan node yang dapat diandalkan untuk membuka saluran.



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



Sebagai contoh, [ACINQ node](https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f) adalah sebuah node yang diakui dengan statistik ketersediaan dan likuiditas yang sangat baik.



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



Untuk tutorial ini, kita akan membuka saluran dengan [Swiss Bitcoin Pay](https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca). Informasi yang diperlukan untuk koneksi (pubkey@ip:port) diberikan pada halaman Amboss mereka.



Untuk membuka saluran :



![Bouton d'ouverture de canal](assets/fr/09.webp)



Pada halaman beranda Lightning Node, klik tombol "+ BUKA SALURAN"



![Configuration du canal](assets/fr/10.webp)



Di halaman konfigurasi saluran :




   - Rekatkan ID simpul yang disalin dari Amboss (format: pubkey@ip:port)
   - Tentukan jumlah kapasitas saluran (beberapa node seperti ACINQ memiliki jumlah minimum, misalnya 400k Sats)
   - Sesuaikan biaya transaksi pembukaan jika perlu



![Canal en cours d'ouverture](assets/fr/11.webp)



Setelah transaksi terkirim, saluran akan muncul sebagai "pembukaan" di halaman beranda. Tunggu konfirmasi transaksi On-Chain.



![Détails du canal](assets/fr/12.webp)



Klik pada saluran untuk melihat detailnya:




   - Status saat ini
   - Kapasitas total
   - Perincian likuiditas (masuk/keluar)
   - Kunci publik dari node jarak jauh
   - Dan informasi teknis lainnya



### Menggunakan Lightning Network+ untuk mendapatkan likuiditas yang masuk



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



Lightning Network+ tersedia di Umbrel App Store untuk memudahkan kamu mendapatkan inbound liquidity.


![Interface principale de LN+](assets/fr/14.webp)



Interface utama menawarkan tiga opsi penting:




- "Swap likuiditas: jelajahi penawaran swap yang tersedia
- "Open For Me": menyaring swap yang memenuhi syarat untuk Anda
- "Ke Dokumen": mengakses dokumentasi



![Message d'erreur LN+](assets/fr/15.webp)



Catatan: JJika kamu belum membuka channel, kamu akan melihat pesan kesalahan ini saat mengklik "Buka Untuk Saya".


![Liste des swaps disponibles](assets/fr/16.webp)



Halaman "Liquidity Swaps" menunjukkan semua penawaran swap yang tersedia di jaringan.



![Swaps éligibles](assets/fr/17.webp)



"Open For Me" hanya menyaring swap yang simpulnya memenuhi persyaratan yang diperlukan.



![Détails d'un swap](assets/fr/18.webp)



Contoh detail pertukaran :




- Konfigurasi Pentagon (5 peserta)
- Kapasitas 300k Sats per saluran
- Prasyarat: minimal 10 saluran terbuka dengan kapasitas total 1M Sats
- Tempat yang tersedia: 4/5



### 4.3 Sinkronisasi dengan aplikasi seluler (Zeus)



Untuk mengontrol node Lightning dari jarak jauh (smartphone), kamu bisa menggunakan Zeus (aplikasi sumber terbuka yang tersedia di iOS/Android).


**Konfigurasi Zeus dengan Umbrel :**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



Pastikan node Umbrel kamu dapat diakses (secara default melalui Tor).


Pada Interface Umbrel, buka aplikasi Lightning Node, lalu klik tombol "Hubungkan Wallet" seperti yang ditunjukkan oleh panah.



![Page de connexion avec QR code](assets/fr/20.webp)



Kode QR muncul, berisi data akses LND kamu dalam format lndconnect. Kode QR ini sangat padat dengan informasi, jadi jangan ragu untuk memperbesarnya biar lebih mudah dibaca.


![Configuration initiale de Zeus](assets/fr/21.webp)



Di ponsel Anda :




   - Buka Zeus
   - Di halaman beranda, klik "Pengaturan lanjutan" untuk menyambungkan simpul Lightning kamu sendiri
   - Dalam parameter, pilih "Buat atau sambungkan Wallet"



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



Dalam Zeus:




   - Pilih "LND (REST)" sebagai jenis koneksi
   - Kamu bisa memindai kode QR (metode yang disarankan) atau memasukkan informasi secara manual. (Jangan ragu untuk memperbesar kode QR Umbrel, karena sangat padat)
   - Penting: aktifkan opsi "Gunakan Tor" jika Umbrel kamu hanya dapat diakses melalui Tor (default)
   - Menyimpan konfigurasi



Zeus kamu sekarang terhubung ke node Umbrel kamu dan memungkinkan kamu melakukan pembayaran Lightning, melihat channel, saldo, dan lainnya, sambil tetap sepenuhnya self-custodial.


**Opsi koneksi tingkat lanjut:**



Secara default, koneksi Zeus ↔ Umbrel adalah melalui Tor. Untuk koneksi yang lebih cepat, ada dua alternatif:



**Lightning Node Connect (LNC)**:




   - Mekanisme koneksi terenkripsi Lightning Labs
   - Instal aplikasi Lightning Terminal pada Umbrel (termasuk akses LNC)
   - generate kode QR koneksi di Lightning Terminal (Hubungkan → Hubungkan Zeus melalui LNC)
   - Pindai ke dalam Zeus (pilih "LNC" sebagai jenis koneksi)



**Skala Ekor VPN**:




   - VPN mesh yang mudah dikonfigurasi
   - Instal Tailscale di Umbrel (App Store) dan di ponsel kamu
   - Hubungkan Zeus melalui IP pribadi Tailscale, bukan Tor Address



Opsi-opsi ini tidak wajib, dan solusi Tor + Zeus bekerja dengan baik dalam banyak kasus.



> **Sumber daya yang berguna:**
> - [Dokumentasi Zeus - Koneksi Umbrel](https://community.umbrel.com/t/zeus-LN-mobile/7619) - Panduan resmi untuk menghubungkan Zeus ke Umbrel
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) - Proyek sumber terbuka Zeus
> - [Komunitas Umbrel - Menghubungkan Zeus melalui Tailscale](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - Panduan untuk menghubungkan Zeus ke Umbrel menggunakan Tailscale

## 5. Keselamatan dan praktik terbaik



Mengelola simpul Lightning yang dihosting sendiri memerlukan perhatian khusus pada keamanan.



### Pencadangan dan keamanan untuk node Anda



**Jenis-jenis pencadangan yang penting**



Node Lightning Umbrel kamu memerlukan dua jenis cadangan:



**Kalimat seed (24 kata)**




- Memulihkan dana On-Chain
- Diperlukan untuk membuat ulang Wallet Lightning kamu
- Untuk penyimpanan yang sangat aman (offline, di atas kertas)



**file Cadangan Saluran Statis (SCB)**




- Berisi informasi saluran Lightning
- Memungkinkan penutupan saluran secara paksa jika terjadi kerusakan
- **Penting:** Jangan pernah menyimpan file `channel.db` secara manual (berisiko terkena penalti)



**Prosedur pencadangan manual**



Untuk menyimpan saluran kamu secara manual :


1. Akses menu Lightning Node (tiga titik "⋮" di sebelah "+ Open Channel")


2. Unduh file cadangan saluran


3. Ekspor SCB baru setelah setiap modifikasi saluran


4. Menyimpan SCB dengan aman (media terenkripsi, salinan di luar lokasi)



*sistem pencadangan otomatis* **Umbrel**



Umbrel dilengkapi sistem pencadangan otomatis canggih yang memastikan:



*Perlindungan data:*




- Enkripsi sisi klien sebelum transmisi
- Mengirim melalui jaringan Tor
- Data dilengkapi dengan pengisian acak
- Kunci enkripsi yang unik untuk perangkat kamu



*Keamanan yang ditingkatkan:*




- Pencadangan instan pada perubahan status
- Cadangan "umpan" pada interval acak
- Menyembunyikan perubahan ukuran cadangan
- Perlindungan terhadap analisis waktu



*Proses pemulihan:*




- Pengenal dan kunci yang berasal dari Payung seed kamu
- Pemulihan lengkap hanya dapat dilakukan dengan frasa Mnemonic saja
- Pemulihan otomatis dari cadangan terbaru
- Memulihkan pengaturan saluran dan data



### Pemulihan kerusakan



Jika node kamu hilang (kegagalan perangkat keras, kartu SD rusak):




- Pasang Kembali Umbrel
- Masukkan 24 kata seed kamu di aplikasi Lightning
- Impor file SCB selama pemulihan



LND akan menghubungi setiap mitra dari channel lama kamu untuk menutupnya dan mengembalikan bagian dana on-chain kamu. Channel akan ditutup secara permanen (akan dibuka kembali jika perlu).


### Ketersediaan dan perlindungan penipuan



Idealnya, biarkan node kamu online sesering mungkin. Dalam kasus ketidakhadiran yang berkepanjangan:




- Rekan yang berbahaya dapat mencoba menyiarkan status saluran yang lama
- Lightning menyediakan "periode protes" (sekitar 2 minggu pada LND)
- Kalau kamu akan pergi untuk waktu yang lama, siapkan Watchtower



**konfigurasi Watchtower:**




- Dalam pengaturan lanjutan LND, tambahkan URL server Watchtower tepercaya
- Kamu bisa menggunakan layanan publik atau memasang Watchtower sendiri




Untuk mengetahui lebih lanjut tentang cara mengonfigurasi dan menggunakan menara pengawas, kami sarankan kamu melihat tutorial khusus kami:



https://planb.academy/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### Praktik terbaik lainnya





- **Pembaruan perangkat lunak:** Selalu perbarui Umbrel dan LND (perbaikan keamanan)
- **Perlindungan perangkat keras:** Gunakan sistem yang stabil (Raspberry Pi dengan SSD, mini-PC) dan UPS
- **Keamanan jaringan:** Pertahankan konfigurasi Tor default, ubah kata sandi admin Umbrel (default: "moneyprintergobrrr")
- **Enkripsi:** Aktifkan enkripsi disk jika memungkinkan



## 6. Alat tambahan



Aplikasi Lightning Node dari Umbrel menyediakan hal-hal penting untuk mengelola saluran kamu, tetapi alat pihak ketiga menawarkan fungsionalitas tingkat lanjut.



### ThunderHub



Interface sistem manajemen node Lightning berbasis web modern yang dapat diinstal melalui Umbrel App Store.



**Fitur:**




- Visualisasi saluran secara real-time (kapasitas, saldo)
- Alat penyeimbangan ulang terintegrasi
- Dukungan untuk penagihan multi jalur (MPP)
- Pembuatan kode QR LNURL
- Manajemen transaksi On-Chain



ThunderHub sangat ideal untuk memantau simpul perutean aktif dan melakukan penyeimbangan ulang sederhana.



### Ride The Lightning (RTL)



Interface web kompatibel dengan beberapa implementasi Lightning (LND, Core Lightning, Eclair).



**Sorotan:**




- Manajemen multi-simpul
- Dasbor yang peka terhadap konteks
- Dukungan untuk pertukaran kapal selam (Lightning Loop)
- autentikasi 2 faktor
- Pencadangan saluran ekspor/impor



RTL adalah "pisau tentara Swiss" yang lengkap untuk mengelola simpul Lightning dengan pendekatan yang lebih berorientasi pada pakar.



### Alat bantu berguna lainnya





- **Cangkang Petir** : Baris perintah (lncli) melalui browser
- **BTC RPC Explorer & Mempool**: Memantau Blockchain
- **LNmetrics & Torq**: Analisis kinerja perutean
- **Amboss & 1ML**: manajemen "sosial" dari node Anda (alias, kontak, analisis jaringan)



Alat-alat ini dapat diinstal hanya dalam beberapa klik melalui Umbrel App Store, tanpa konfigurasi yang rumit.



**Sumber daya alat tambahan:**




- [ThunderHub.io - Fitur](https://thunderhub.io) - Ikhtisar fitur ThunderHub
- [Info Ride The Lightning (RTL)](https://www.ridethelightning.info/) - Dokumentasi RTL
- [David Kaspar - Rebalance via ThunderHub](https://blog.davidkaspar.com) - Panduan praktis untuk menyeimbangkan kembali
- [Panduan "Mengelola Simpul Petir"](https://github.com/openoms/lightning-node-management) - Dokumentasi lanjutan untuk pengguna daya



## Kesimpulan



Menjalankan node LND kamu sendiri di Umbrel adalah langkah penting menuju kedaulatan finansial. Meskipun membutuhkan lebih banyak keterlibatan teknis daripada solusi kustodian, manfaatnya dalam hal kontrol, kerahasiaan, dan partisipasi aktif dalam Lightning Network cukup besar.

Dengan mengikuti panduan ini, kamu sekarang bisa menginstal LND, membuka channel, mengelola likuiditas, dan mengakses node kamu dari jarak jauh. Jangan ragu untuk menjelajahi fitur-fitur canggih dan alat tambahan secara bertahap setelah kamu makin terbiasa dengan ekosistem.

Ingatlah bahwa keamanan dana kamu bergantung pada perlindungan dan praktik kamu. Luangkan waktu untuk memahami setiap aspek sebelum melakukan transaksi dalam jumlah besar.
