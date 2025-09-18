---
name: Blockstream App - Desktop
description: Bagaimana cara menggunakan Hardware Wallet Anda dengan Aplikasi Blockstream di komputer?
---
![cover](assets/cover.webp)



## 1. Pendahuluan



### 1.1 Tujuan tutorial





- Tutorial ini menjelaskan cara menggunakan **Aplikasi Blockstream** di komputer untuk mengelola **onchain** Bitcoin Wallet dengan **Hardware Wallet**, memungkinkan transaksi aman yang direkam pada Blockchain Bitcoin utama.
- Ini mencakup instalasi, konfigurasi awal, menghubungkan Hardware Wallet, dan menerima dan mengirim bitcoin onchain.
- Catatan: Tutorial lain dalam Lampiran mencakup Liquid, Watch-Only dan aplikasi seluler.



### 1.2 Target audiens





- **Pemula**: Pengguna yang ingin mengelola bitcoin mereka dengan perangkat lunak desktop yang aman dan Hardware Wallet.
- **Pengguna tingkat menengah**: Orang-orang yang ingin memahami cara menggunakan Hardware Wallet untuk transaksi onchain dan opsi privasi seperti Tor atau SPV.



### 1.3. Latar belakang dompet perangkat keras





- **Hardware Wallet**, **Cold Wallet**: Perangkat fisik yang menyimpan kunci pribadi secara offline, menawarkan keamanan tingkat tinggi terhadap serangan siber, tidak seperti **Dompet Hot** (dompet perangkat lunak pada perangkat yang terhubung).
- **Penggunaan yang disarankan**:
    - Ideal untuk mengamankan dana dalam jumlah besar atau tabungan jangka panjang.
    - Cocok untuk pengguna yang berfokus pada keamanan yang ingin melindungi dana mereka dari risiko yang terkait dengan perangkat yang terhubung.
- **Keterbatasan**: Membutuhkan perangkat lunak seperti Blockstream App untuk melihat saldo, alamat generate, dan menyiarkan transaksi yang ditandatangani Hardware Wallet.



## 2. Memperkenalkan Aplikasi Blockstream





- **Blockstream App** adalah aplikasi seluler (iOS, Android) dan desktop untuk mengelola dompet dan aset Bitcoin di Liquid Network. Diakuisisi oleh Blockstream pada tahun 2016, aplikasi ini bernama *GreenAddress*, berganti nama menjadi *Blockstream Green* (2019), dan sekarang bernama *Blockstream app* (2025).
- **Fitur-fitur utama**:
- **Transaksi Onchain** pada Blockchain Bitcoin.
    - Transaksi di jaringan **Liquid** (Sidechain untuk pertukaran yang cepat dan rahasia).
- **Portfolio watch-only** untuk memantau dana tanpa akses ke kunci.
    - Opsi privasi: koneksi melalui **Tor**, koneksi ke **simpul pribadi** melalui Electrum, atau verifikasi **SPV** untuk mengurangi ketergantungan pada simpul pihak ketiga.
    - Berfungsi **Replace-by-fee (RBF)** untuk mempercepat transaksi yang belum dikonfirmasi.
- **Kompatibilitas**: Mengintegrasikan dompet perangkat keras seperti **Blockstream Jade**.
- **Interface**: Intuitif untuk pemula, dengan opsi tingkat lanjut untuk para ahli.
- **Catatan**: Panduan ini berfokus pada penggunaan onchain dengan Hardware Wallet pada versi desktop. Tutorial lain yang disediakan sebagai lampiran mencakup penggunaan pada aplikasi seluler, untuk onchain, Liquid, dan fitur Watch-Only.



## 3. Menginstal dan mengatur Desktop Aplikasi Blockstream



### 3.1. Unduh





- Buka [situs web resmi] (https://blockstream.com/app/) dan klik "_Unduh Sekarang_". Unduh versi yang sesuai dengan sistem operasi Anda (Windows, macOS, Linux).
- **Catatan**: Pastikan untuk mengunduh dari sumber resmi untuk menghindari perangkat lunak palsu.



### 3.2. konfigurasi awal





- **Layar beranda**: Ketika pertama kali dibuka, aplikasi menampilkan layar tanpa Wallet yang dikonfigurasi. Portofolio yang dibuat atau diimpor akan muncul di sini nanti.



![image](assets/fr/02.webp)





- **Menyesuaikan pengaturan**: Klik ikon pengaturan di kiri bawah, sesuaikan opsi di bawah ini, kemudian keluar dari Interface untuk melanjutkan.



![image](assets/fr/03.webp)



#### 3.2.1. Parameter umum





- Pada menu Pengaturan, klik "**Umum**".
- **Fungsi**: Mengubah bahasa perangkat lunak dan mengaktifkan fungsi eksperimental jika diperlukan.



![image](assets/fr/04.webp)



#### 3.2.2. Koneksi melalui Tor





- Pada menu Pengaturan, klik "**Jaringan**".
- **Fungsi**: Merutekan lalu lintas jaringan melalui **Tor**, sebuah jaringan anonim yang mengenkripsi koneksi Anda.
- Mengapa? Menyembunyikan IP Address Anda dan melindungi privasi Anda, ideal jika Anda tidak mempercayai jaringan Anda (Wi-Fi publik, misalnya).
- **Kerugian**: Dapat memperlambat aplikasi karena enkripsi.
- **Rekomendasi**: Aktifkan Tor jika kerahasiaan adalah prioritas, tetapi uji kecepatan koneksi.



![image](assets/fr/05.webp)



#### 3.2.3. Menghubungkan ke simpul pribadi





- Pada menu Pengaturan, klik "**Server khusus dan validasi**".
- **Fungsi**: Menghubungkan aplikasi ke **node Bitcoin lengkap** milik Anda sendiri melalui **server Electrum**.
- Mengapa? Memberikan kontrol penuh atas data Blockchain, menghilangkan ketergantungan pada server Blockstream.
- **Prasyarat**: Node Bitcoin yang telah dikonfigurasi.
- **Rekomendasi**: Pengguna tingkat lanjut yang menginginkan kedaulatan maksimum.



![image](assets/fr/06.webp)



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4. Verifikasi SPV





- Pada menu Pengaturan, klik "**Server khusus dan validasi**".
- **Fungsi**: Menggunakan **Verifikasi Pembayaran Sederhana (SPV)** yang mengunduh tajuk blok dan memverifikasi transaksi Anda dengan bukti penyertaan (Merkle), tanpa menyimpan Blockchain yang lengkap.
- Mengapa? Mengurangi ketergantungan pada node default Blockstream, namun tetap ringan untuk perangkat.
- **Kerugian**: Kurang aman dibandingkan Full node, karena bergantung pada node pihak ketiga untuk beberapa informasi.
- **Rekomendasi**: Aktifkan SPV jika Anda tidak dapat menggunakan simpul pribadi, tetapi lebih memilih Full node untuk keamanan optimal.



![image](assets/fr/07.webp)



## 4. Menghubungkan Hardware Wallet ke Aplikasi Blockstream



### 4.1. Pertimbangan awal



#### 4.1.1. Untuk pengguna Ledger





- Blockstream Green hanya mendukung aplikasi **Bitcoin Legacy** pada perangkat Ledger (Nano S, Nano X).
- Langkah-langkah yang harus diikuti dalam **Ledger Live** sebelum menghubungkan perangkat Anda:


1. Buka **"Pengaturan "** → **"Fitur eksperimental "** dan aktifkan **mode pengembang**.


2. Buka **"My Ledger"** → **"Katalog Aplikasi "**, lalu instal aplikasi **Bitcoin Legacy**


3. Buka aplikasi **Bitcoin Legacy** pada Ledger Anda sebelum meluncurkan Blockstream Green untuk membuat koneksi.




- **Catatan**: Pastikan Ledger Anda tidak terkunci dengan kode PIN Anda dan aplikasi Bitcoin Legacy aktif saat Anda terhubung.



#### 4.1.2 Menginisialisasi Hardware Wallet





- Jika Hardware Wallet (Ledger, Trezor, atau Blockstream Jade) Anda belum pernah digunakan (baik dengan Blockstream Green, atau dengan perangkat lunak lain seperti Ledger Live), pertama-tama Anda harus menginisialisasi terlebih dahulu. Langkah ini dilakukan di lingkungan yang aman, tanpa kamera atau pengamat:


1. **Pembuatan frasa seed / frasa Mnemonic** (12, 18 atau 24 kata): Tuliskan dengan cermat pada selembar kertas.


2. **Verifikasi frasa seed**: Menguji impor Wallet dari kata-kata yang dicatat, misalnya dengan memverifikasi kunci publik yang diperluas. Harus dilakukan sebelum mengirim dana ke Wallet dan mengamankan frasa seed secara permanen.


3. **Mengamankan frasa seed**: Simpan frasa pada media fisik (kertas atau logam) dan di tempat yang aman. Jangan pernah menyimpannya secara digital (tidak ada tangkapan layar, cloud, atau email).




- **Penting**: Frasa seed adalah satu-satunya cara untuk memulihkan dana Anda jika perangkat hilang atau mengalami kerusakan. Siapa pun yang memiliki akses dapat mencuri bitcoin Anda.
- **Sumber daya** untuk mencadangkan dan memeriksa kalimat seed :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3. Konfigurasi untuk tutorial ini :





- Kami akan mengasumsikan bahwa Hardware Wallet telah diinisialisasi dengan frasa seed dan kode PIN pengunci.
- Kami mengasumsikan bahwa Hardware Wallet belum pernah terhubung ke Blockstream App, yang memerlukan pembuatan akun baru. Jika Hardware Wallet sudah pernah digunakan dengan Aplikasi Blockstream, akun akan secara otomatis muncul ketika aplikasi dibuka.



### 4.2. Memulai koneksi





- Dari layar beranda, klik "**Persiapkan Wallet Baru**", lalu validasi syarat dan ketentuan dan klik "**Mulai**":



![image](assets/fr/08.webp)





- Pilih opsi "**Pada Hardware Wallet**":



![image](assets/fr/09.webp)





- Jika Anda menggunakan **Blockstream Jade**, klik tombol yang sesuai. Jika tidak, pilih "**Hubungkan Perangkat Perangkat Keras yang berbeda**":



![image](assets/fr/10.webp)





- Hubungkan Hardware Wallet Anda ke komputer melalui USB dan pilih di Aplikasi Blockstream:



![image](assets/fr/22.webp)





- Mohon tunggu sementara Aplikasi Blockstream mengimpor informasi portofolio Anda:



![image](assets/fr/23.webp)



### 4.3. Membuat akun





- Jika Hardware Wallet Anda telah digunakan dengan Aplikasi Blockstream, akun Anda akan secara otomatis muncul di Interface setelah impor. Jika tidak, buat akun dengan mengklik "**Buat Akun**":



![image](assets/fr/24.webp)





- Pilih "**Standard**" untuk mengonfigurasi portofolio Bitcoin klasik:



![image](assets/fr/25.webp)





- Setelah akun Anda dibuat, Anda dapat mengakses portofolio Interface utama Anda:



![image](assets/fr/26.webp)





## 5. Menggunakan onchain Wallet dengan Hardware Wallet



### 5.1. Menerima bitcoin





- Dari layar portofolio utama, klik "**Terima**" :



![image](assets/fr/27.webp)





- Aplikasi menampilkan **penerimaan kosong Address**. Menggunakan Address baru untuk setiap penerimaan akan meningkatkan kerahasiaan Anda. Klik "**Salin Address**" untuk menyalin Address, atau biarkan pengirim memindai kode QR yang ditampilkan:



![image](assets/fr/12.webp)



**Opsi** :




- (1) Klik tanda panah ke generate Address baru yang terhubung ke portofolio Anda.
- (2) Untuk meminta jumlah tertentu, klik "**Opsi lain**" lalu "**Jumlah Permintaan**". QR akan diperbarui, dan Address akan diganti dengan URI pembayaran Bitcoin seperti: `Bitcoin:bc1q...?amount=0.00001`



![image](assets/fr/13.webp)





- (3) Untuk menggunakan kembali Address sebelumnya, klik "**Opsi lainnya**" kemudian pada "**Daftar alamat**" :



![image](assets/fr/14.webp)





- **Verifikasi**: Periksa dengan cermat Address yang dibagikan untuk menghindari kesalahan atau serangan (misalnya malware yang memodifikasi clipboard).
- Setelah transaksi disiarkan di jaringan, transaksi tersebut akan muncul di Wallet Anda. Tunggu 1 hingga 6 konfirmasi untuk menganggap transaksi tidak dapat diubah.



![image](assets/fr/28.webp)



### 5.2. mengirim bitcoin





- Dari layar portofolio utama, klik "**Kirim**".



![image](assets/fr/29.webp)





- Masukkan **detail**:
    - (1) Pastikan aset yang dipilih adalah **Bitcoin** (onchain).
    - (2) Masukkan **Address penerima ** dengan menempelkannya atau memindai kode QR dengan webcam Anda.
    - (3) Tunjukkan **jumlah** yang akan dikirim (dalam BTC, satoshi, atau unit lainnya).




![image](assets/fr/16.webp)





- Pilih **biaya transaksi** (opsional):
 - Pilih dari opsi yang disarankan (cepat, sedang, lambat) sesuai dengan urgensi, dengan perkiraan waktu konfirmasi.
 - Untuk biaya yang disesuaikan, sesuaikan secara manual jumlah satoshi per vbyte. Hal ini ditampilkan pada layar beranda. Lihat juga [Mempool.space](https://Mempool.space/).



![image](assets/fr/17.webp)





- **Pemilihan UTXO secara manual** (opsional): Klik "**Pemilihan Coin secara manual**" untuk memilih UTXO tertentu yang akan digunakan dalam transaksi.



![image](assets/fr/18.webp)





- **Verifikasi awal**: Periksa Address, jumlah dan biaya pada layar ringkasan, lalu klik "**Konfirmasi transaksi**". Pada kenyataannya, transaksi tidak akan dirilis ke jaringan sampai Anda menandatanganinya dengan Hardware Wallet Anda, yang hanya memiliki kunci rahasia yang terkait dengan alamat tempat UTXO (satoshi) akan didebit.



![image](assets/fr/19.webp)





- **Pemeriksaan akhir dan tanda tangan**: Pastikan semua parameter transaksi sudah benar **pada layar Hardware Wallet** Anda, lalu tandatangani transaksi dengan menggunakan layar tersebut. Kesalahan pada Address dapat mengakibatkan hilangnya dana yang tidak dapat dikembalikan.





- **Siaran**: Setelah ditandatangani, Aplikasi Blockstream secara otomatis menyiarkan transaksi di jaringan Bitcoin.



![image](assets/fr/20.webp)





- **Tindak lanjut** :
 - Transaksi akan muncul di layar beranda Wallet sebagai "tertunda" hingga dikonfirmasi.
 - Selama transaksi belum dikonfirmasi, fungsi **Replace-by-fee (RBF)** dapat digunakan untuk mempercepat konfirmasi dengan menambah biaya (lihat Lampiran).



![image](assets/fr/21.webp)



## Lampiran



### A1. Tutorial Blockstream lainnya





- Menggunakan Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Mengimpor dan melacak portofolio dalam "Hanya Untuk Dipantau" :



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb



- Menggunakan Aplikasi Blockstream pada ponsel (Hot Wallet) :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2. Penjelasan tentang Replace-by-fee (RBF)





- **Definisi**: Replace-by-fee (RBF) adalah fitur jaringan Bitcoin yang memungkinkan pengirim untuk mempercepat konfirmasi transaksi **onchain** dengan meningkatkan biaya.
- **Batas** :
    - RBF tidak tersedia untuk transaksi Liquid atau Lightning.
    - Transaksi awal harus ditandai sebagai kompatibel dengan RBF, yang dilakukan secara otomatis oleh Aplikasi Blockstream.
- Untuk informasi lebih lanjut, lihat [daftar istilah kami](https://planb.network/resources/glossary/RBF-replacebyfee).



### A3. Praktik terbaik





- **Amankan frasa pemulihan Anda** :
    - Simpan frasa Hardware Wallet Mnemonic Anda pada media fisik (kertas, logam) di tempat yang aman.
    - Jangan pernah menyimpannya secara digital (cloud, email, tangkapan layar).
    - Tutorial: Simpan frasa Mnemonic Anda:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Lindungi privasi Anda** :





    - generate Address baru untuk setiap penerimaan onchain.
    - Aktifkan **Tor** atau **SPV** untuk membatasi pelacakan.
    - Hubungkan ke node Bitcoin Anda sendiri melalui Electrum untuk kedaulatan maksimum.
- **Selalu periksa alamat pengiriman**:





    - Periksa Address pada layar Hardware Wallet Anda sebelum menandatangani.
    - Gunakan salin/tempel atau kode QR untuk menghindari kesalahan manual.
- **Mengoptimalkan biaya**:





    - Sesuaikan biaya sesuai dengan urgensi dan kepadatan jaringan (lihat [Mempool.space](https://Mempool.space/)).
    - Gunakan Liquid atau Lightning untuk transaksi cepat dan murah yang tidak memerlukan keamanan onchain.
- **Perbarui perangkat lunak** :





    - Selalu perbarui Aplikasi Blockstream dan firmware Hardware Wallet Anda dengan fitur-fitur terbaru dan patch keamanan.



### A4. Sumber daya tambahan





- **Tautan resmi** :
    - [Situs web resmi](https://blockstream.com/)
    - [Dukungan untuk Aplikasi Blockstream](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): dokumentasi dan obrolan
    - [GitHub](https://github.com/Blockstream/green_qt)





- **Penjelajah Blok** :
    - Onchain: [Mempool.space](https://Mempool.space/)
    - Liquid: [Info Blockstream](https://blockstream.info/Liquid)
    - Petir: [1ML (Lightning Network)] (https://1ml.com/)





- **Mengamankan frasa pemulihan Anda:**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Liquid Network**:



[Glosarium](https://planb.network/fr/resources/glossary/Liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- **Lightning Network**:



[Glosarium](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb