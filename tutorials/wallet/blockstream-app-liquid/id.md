---
name: Blockstream App - Liquid
description: Cara mengonfigurasi Aplikasi Blockstream dan menggunakan Liquid Network
---
![cover](assets/cover.webp)


## 1. Pendahuluan


### 1.1 Tujuan tutorial





- Tutorial ini menjelaskan cara menggunakan aplikasi seluler **Blockstream App** untuk mengelola portofolio **Bitcoin Liquid**, yaitu transaksi yang dicatat secara langsung pada rantai samping Bitcoin "Liquid".
- Ini mencakup instalasi, konfigurasi awal, pembuatan Software Wallet, dan operasi untuk menerima dan mengirim bitcoin pada Liquid.
- Catatan: Tutorial lain dalam Lampiran mencakup Onchain, Watch-Only, dan versi desktop.



### 1.2 Target audiens





- **Pemula**: Pengguna yang ingin mengelola bitcoin mereka dengan aplikasi seluler yang intuitif, yang mengintegrasikan Liquid Network.
- **Pengguna tingkat menengah**: Orang-orang yang ingin memahami fungsi onchain dan opsi privasi seperti Tor atau SPV.



### 1.3 Memperkenalkan Liquid



**Liquid** adalah **Sidechain** dari Bitcoin, yang dikembangkan oleh **[Blockstream](https://blockstream.com/Liquid/)**, yang dirancang untuk menawarkan fungsionalitas yang lebih cepat, lebih banyak Confidential Transactions, dan lebih canggih, namun tetap terhubung ke Blockchain Bitcoin yang utama.



Sidechain adalah Blockchain independen yang beroperasi secara paralel dengan Bitcoin, menggunakan mekanisme yang dikenal sebagai **two-way peg**. Sistem ini mengunci bitcoin ke Blockchain utama untuk menciptakan **Liquid-Bitcoins (L-BTC) **, token yang beredar di Liquid Network dengan tetap mempertahankan paritas nilai dengan bitcoin asli. Dana dapat dikembalikan ke Blockchain Bitcoin kapan saja.



![image](assets/fr/17.webp)






- (1) **Peg-in**: Bitcoin (BTC) dikunci ke Blockchain utama oleh federasi Liquid. Sebagai gantinya, jumlah yang setara dengan Liquid-Bitcoin (L-BTC), yang memastikan keseimbangan antara kedua rantai, diterbitkan pada Blockchain Liquid dan dikirim ke pengguna.





- (2) **Transaksi independen**: Transaksi dapat berjalan secara bersamaan dan independen di Blockchain (BTC) dan Sidechain Liquid (L-BTC) utama, tergantung pada kebutuhan pengguna.





- (3) **Peg-out**: Pengguna mengirimkan Liquid-Bitcoins (L-BTC) kembali ke federasi Liquid. Federasi kemudian membuka jumlah bitcoin (BTC) yang setara di Blockchain utama dan mentransfernya ke pengguna.



Liquid bergantung pada **federasi** peserta tepercaya (bursa, perusahaan Bitcoin yang diakui) yang mengelola validasi blok dan penahan bilateral. Tidak seperti Blockchain dan Bitcoin yang terdesentralisasi dan bergantung pada penambang, Liquid merupakan jaringan **federasi**, yang berarti keamanan dan tata kelolanya bergantung pada para partisipan. Meskipun ini menyiratkan kompromi pada desentralisasi, ini memungkinkan kinerja yang dioptimalkan dan fungsionalitas tingkat lanjut.



![image](assets/fr/18.webp)



##### Mengapa menggunakan Liquid?





- **Kecepatan**: Transaksi di Liquid dikonfirmasi dalam waktu sekitar **1 menit**, dibandingkan dengan 10 menit atau lebih untuk transaksi onchain, berkat blok yang dihasilkan setiap menit oleh federasi validator.
- **Kerahasiaan yang ditingkatkan**: Liquid menggunakan **Confidential Transactions**, yang menyembunyikan jumlah dan jenis aset yang ditransfer, membuat transaksi lebih privat (meskipun alamat tetap terlihat).
- **Biaya rendah**: Transaksi di Liquid umumnya lebih murah, sehingga ideal untuk transfer yang sering atau dalam jumlah kecil.
- **Beberapa aset**: Selain L-BTC, Liquid mendukung penerbitan aset digital lainnya, seperti stablecoin atau token, untuk digunakan dalam aplikasi tertentu.
- **Kasus penggunaan**: Liquid sangat cocok untuk pertukaran lintas platform, pembayaran cepat, atau aplikasi yang membutuhkan kontrak pintar, namun tetap terhubung dengan keamanan Bitcoin.



**Catatan:** Tutorial ini berfokus pada penggunaan Liquid melalui Aplikasi Blockstream. Untuk pemahaman mendalam tentang Liquid Network, Anda akan menemukan sumber daya di lampiran.



### 1.4. Pengingat Hot Wallet





- **Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: semua nama untuk aplikasi yang diinstal pada ponsel cerdas, komputer, atau perangkat apa pun yang terhubung ke Internet, yang memungkinkan kunci privat dari Bitcoin Wallet dikelola dan diamankan.
- Tidak seperti **dompet perangkat keras**, juga dikenal sebagai **dompet Cold**, yang mengisolasi kunci secara offline, dompet perangkat lunak beroperasi di lingkungan yang terhubung, sehingga lebih rentan terhadap serangan cyber.





- **Penggunaan yang disarankan**:
    - Ideal untuk mengelola Bitcoin dalam jumlah sedang, terutama untuk transaksi harian.
    - Cocok untuk pemula atau pengguna dengan aset terbatas, yang mungkin menganggap Hardware Wallet tidak berguna.





- **Keterbatasan**: Kurang aman untuk menyimpan dana besar atau tabungan jangka panjang. Dalam hal ini, pilihlah Hardware Wallet.




## 2. Memperkenalkan Aplikasi Blockstream





- **Blockstream App** adalah aplikasi seluler (iOS, Android) dan desktop untuk mengelola dompet dan aset Bitcoin di Liquid Network. Diakuisisi oleh [Blockstream] (https://blockstream.com/) pada tahun 2016, sebelumnya bernama *Green Address* dan kemudian *Blockstream Green*.
- **Fitur-fitur utama**:
- **Transaksi Onchain** pada Blockchain Bitcoin.
    - Transaksi di jaringan **Liquid** (Sidechain untuk pertukaran yang cepat dan rahasia).
- **Portfolio watch-only** untuk memantau dana tanpa akses ke kunci.
    - Opsi privasi: koneksi melalui **Tor**, koneksi ke **simpul pribadi** melalui Electrum, atau verifikasi **SPV** untuk mengurangi ketergantungan pada simpul pihak ketiga.
    - Berfungsi **Replace-by-fee (RBF)** untuk mempercepat transaksi yang belum dikonfirmasi.
- **Kompatibilitas**: Mengintegrasikan dompet perangkat keras seperti **Blockstream Jade**.
- **Interface**: Intuitif untuk pemula, dengan opsi tingkat lanjut untuk para ahli.
- **Catatan**: Panduan ini berfokus pada penggunaan onchain. Tutorial lain dalam Lampiran mencakup Onchain, Watch-Only, dan versi desktop.




## 3. Menginstal dan mengonfigurasi Aplikasi Blockstream



### 3.1. Unduh





- Untuk **Android** :
    - Unduh [Aplikasi Blockstream](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) dari Google Play Store.
    - Alternatif: Instal melalui file APK yang tersedia di [GitHub resmi Blockstream](https://github.com/Blockstream/green_android).
- Untuk **iOS** :
    - Unduh [Aplikasi Blockstream](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) dari App Store.
- **Catatan**: Pastikan untuk mengunduh dari sumber resmi untuk menghindari aplikasi palsu.



### 3.2. konfigurasi awal





- **Layar beranda**: Saat pertama kali dibuka, aplikasi menampilkan layar tanpa Wallet yang dikonfigurasi. Portofolio yang dibuat atau diimpor akan muncul di sini nanti.



![image](assets/fr/02.webp)





- **Menyesuaikan pengaturan**: Klik "Pengaturan aplikasi", sesuaikan opsi di bawah ini, klik "Simpan", mulai ulang aplikasi dan buat portofolio Anda.



![image](assets/fr/03.webp)



#### 3.2.1. Privasi yang ditingkatkan (hanya untuk Android)





- **Fungsi**: Menonaktifkan tangkapan layar, menyembunyikan pratinjau aplikasi di pengelola tugas, dan mengunci akses saat ponsel terkunci.
- Mengapa? Melindungi data Anda dari akses fisik yang tidak sah atau malware penangkap layar.



#### 3.2.2. Koneksi melalui Tor





- **Fungsi**: Merutekan lalu lintas jaringan melalui **Tor**, sebuah jaringan anonim yang mengenkripsi koneksi Anda.
- Mengapa? Menyembunyikan IP Address Anda dan melindungi privasi Anda, ideal jika Anda tidak mempercayai jaringan Anda (Wi-Fi publik, misalnya).
- **Kerugian**: Dapat memperlambat aplikasi karena enkripsi.
- **Rekomendasi**: Aktifkan Tor jika kerahasiaan adalah prioritas, tetapi uji kecepatan koneksi.



#### 3.2.3. Menghubungkan ke simpul pribadi





- **Fungsi**: Menghubungkan aplikasi ke **node Bitcoin lengkap** milik Anda sendiri melalui **server Elektrum**.
- Mengapa? Memberikan kontrol penuh atas data Blockchain, menghilangkan ketergantungan pada server Blockstream.
- **Prasyarat**: Node Bitcoin yang telah dikonfigurasi.
- **Rekomendasi**: Pengguna tingkat lanjut yang menginginkan kedaulatan maksimum.



#### 3.2.4. Verifikasi SPV





- **Fungsi**: Menggunakan **Verifikasi Pembayaran Sederhana (SPV)** untuk memverifikasi secara langsung data Blockchain tertentu tanpa mengunduh seluruh rantai.
- Mengapa? Mengurangi ketergantungan pada node default Blockstream, namun tetap ringan untuk perangkat seluler.
- **Kerugian**: Kurang aman dibandingkan Full node, karena bergantung pada node pihak ketiga untuk beberapa informasi.
- **Rekomendasi**: Aktifkan SPV jika Anda tidak dapat menggunakan simpul pribadi, tetapi lebih memilih Full node untuk keamanan optimal.





## 4. Membuat portofolio onchain Bitcoin



### 4.1. Memulai pembuatan





- **Perhatian**: Siapkan portofolio Anda di lingkungan pribadi, tanpa kamera atau pengamat.
- Dari layar beranda, klik "Memulai" :



![image](assets/fr/04.webp)





- Jika Anda ingin mengelola **Cold Wallet** (Wallet offline): klik **"Hubungkan Jade "** untuk menggunakan Hardware Wallet Blockstream Jade atau dompet Cold lainnya yang kompatibel.



![image](assets/fr/05.webp)






- Layar berikutnya muncul:



![image](assets/fr/06.webp)






- (1) **"Setup Mobile Wallet"**: Membuat Hot Wallet baru (Hot Wallet).
- (2) **"Pulihkan dari Cadangan "**: Mengimpor portofolio yang sudah ada dengan menggunakan frasa Mnemonic (12 atau 24 kata). Peringatan: Jangan mengimpor frasa dari Cold Wallet, karena frasa tersebut akan terekspos pada perangkat yang terhubung, dan membatalkan keamanannya.
- (3) **"Hanya-Baca "**: Mengimpor portofolio hanya-baca yang sudah ada, untuk melihat saldo (mis. dari Cold Wallet Anda) tanpa mengekspos frasa Mnemonic. Lihat tutorial "Watch Only" di lampiran.



**Dalam tutorial ini**: Klik **"Setup Mobile Wallet"** untuk membuat Hot Wallet.


Wallet Anda secara otomatis dibuat dan halaman beranda Wallet, di sini disebut "My Wallet 5", ditampilkan:



![image](assets/fr/07.webp)



**Penting**: Aplikasi Blockstream telah menyederhanakan pembuatan Wallet dengan tidak secara otomatis menampilkan frasa seed yang terdiri dari 12 kata. *Meskipun portofolio sekarang dibuat dalam satu klik, Anda berisiko kehilangan akses ke dana Anda jika Anda tidak menyimpan frasa seed Anda*.



### 4.2. Menyimpan frasa seed





- Pada layar beranda Wallet, klik tab "Keamanan", lalu pada prompt "Cadangkan" atau menu "Frasa Pemulihan":



![image](assets/fr/08.webp)



Frasa 12 kata seed akan ditampilkan untuk Anda simpan.





- Tuliskan frasa pemulihan Anda dengan sangat hati-hati. Tuliskan di atas kertas atau logam dan simpan di tempat yang aman (lokasi yang aman dan offline). Frasa ini merupakan satu-satunya cara Anda untuk mengakses bitcoin jika perangkat Anda hilang atau aplikasi dihapus.
- Penting juga untuk diperhatikan bahwa siapa pun yang memiliki frasa ini dapat mencuri semua bitcoin Anda. Jangan pernah menyimpannya secara digital:
 - Tidak ada tangkapan layar
 - Tidak ada cadangan awan, email, atau pesan
 - Tidak ada salin/tempel (risiko menyimpan ke clipboard)



**! Poin ini sangat penting**. Untuk informasi lebih lanjut mengenai pencadangan :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Periksa kalimat seed



Sebelum mengirim dana ke Address yang terkait dengan frasa seed ini, Anda harus menguji cadangan 12 kata Anda.


Untuk melakukan ini, kita akan menuliskan referensi, menghapus Wallet, mengembalikannya dengan cadangan, dan memeriksa bahwa referensi tidak berubah.





- Pada layar beranda Wallet, klik pada tab "Pengaturan", lalu pada "Detail Wallet", dan salin zPub ([kunci publik yang diperluas](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f):



![image](assets/fr/09.webp)



Catatan: zpub Address dapat diimpor ke dalam aplikasi Blockstream Anda untuk fungsi "Watch Only" (lihat Lampiran).





- Hapus aplikasi, lalu pulihkan Wallet melalui **"Pulihkan dari Cadangan "** dengan memasukkan frasa Mnemonic, dan periksa apakah zpub tidak berubah. Jika ya, maka cadangan Anda sudah benar, dan Anda dapat mengirim dana ke Wallet.





- Untuk mempelajari lebih lanjut tentang cara melakukan tes pemulihan, berikut ini adalah tutorial khusus:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.4. Mengamankan akses ke aplikasi



Mengunci akses ke aplikasi dengan kode PIN yang kuat:




- Dari layar beranda Wallet, buka **"Keamanan "** lalu klik **"PIN "**
- Masukkan dan konfirmasikan **kode PIN 6 digit acak**.



**Opsi biometrik**: Tersedia untuk menambah kenyamanan, tetapi kurang aman dibandingkan dengan kode PIN yang kuat (risiko akses yang tidak sah, misalnya pemindaian sidik jari atau wajah saat tidur).



**Catatan**: PIN mengamankan perangkat, tetapi hanya frasa seed yang dapat digunakan untuk memulihkan dana.





## 5. Menggunakan Liquid Wallet



### 5.1. Menerima bitcoin "L-BTC"



Untuk menerima Liquid-Bitcoin (L-BTC), ada beberapa opsi yang tersedia. Anda bisa meminta seseorang untuk mengirimkannya secara langsung dengan cara membagikan Liquid dan menerima Address, yang akan dijelaskan di bawah ini.



Atau, Exchange bitcoin Anda di blockchain atau melalui Lightning Network untuk L-BTC menggunakan [jembatan seperti Boltz] (https://boltz.Exchange/): masukkan Liquid Anda yang menerima Address, lakukan pembayaran sesuai keinginan, dan terima L-BTC Anda.





- Dari layar beranda portofolio, klik '"**Transaksi**" lalu **"Terima "**.



![image](assets/fr/19.webp)





- Secara default, aplikasi menampilkan **tanda terima kosong Address, onchain** (format SegWit v0, dimulai dengan `bc1q...`). Klik "Bitcoin" untuk memilih **Liquid Bitcoin**:



![image](assets/fr/20.webp)





- **Opsi** :
 - (1) Klik tanda panah untuk memilih Address baru lainnya yang terkait dengan kalimat seed ini.
    - (2) Anda juga dapat memilih Address dari antara yang sudah digunakan/ditampilkan, dengan mengeklik tiga titik di kanan atas dan kemudian pada "Daftar Alamat"
    - (3) Untuk meminta jumlah tertentu, klik pada tiga titik di kanan atas, pilih "Minta jumlah", dan masukkan jumlah yang diinginkan. QR akan diperbarui, dan Address akan diganti dengan URI pembayaran Bitcoin.



![image](assets/fr/21.webp)





- Bagikan Address/URI dengan mengeklik "**Bagikan**", menyalin teks, atau memindai kode QR.
- **Verifikasi**: Periksa Address yang dibagikan kepada penerima sejauh mungkin untuk menghindari kesalahan atau serangan (misalnya malware yang memodifikasi clipboard).



### 5.2. mengirim bitcoin





- Dari layar beranda portofolio, klik "**Transaksi**" kemudian **"Kirim "**:



![image](assets/fr/22.webp)





- Masukkan **detail**:
    - (1) Masukkan **Address penerima** dengan menempelkannya atau memindai kode QR.
    - (2) Periksa aset dan rekening tujuan pengiriman dana.
    - (3) Tunjukkan **jumlah** yang akan dikirim. Anda dapat memilih unit: L-BTC, L-satoshi, USD, ...



![image](assets/fr/23.webp)





- Centang **:**
    - Periksa Address, jumlah dan biaya pada layar ringkasan.
    - Kesalahan Address dapat mengakibatkan hilangnya dana yang tidak dapat dipulihkan. Waspadai malware yang memodifikasi papan klip.



![image](assets/fr/24.webp)





- **Konfirmasi**: Geser tombol "Kirim" untuk menandatangani dan mendistribusikan transaksi.
- **Tindak lanjut**: Pada tab "Transaksi" di Wallet, transaksi akan muncul sebagai "Belum Dikonfirmasi", kemudian "Dikonfirmasi", lalu "Selesai":



![image](assets/fr/25.webp)





- Waktu antara 2 blok adalah 1 menit pada Liquid, sehingga transaksi dapat dengan cepat dikonfirmasi dan diselesaikan.




## Lampiran



### A1. Tutorial Aplikasi Blockstream lainnya



Menggunakan jaringan Onchain



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Mengimpor dan melacak Wallet dalam mode "Hanya Menonton"



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Versi desktop



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da



### A2. Praktik terbaik



Untuk menggunakan **Aplikasi Blockstream** dengan aman dan efisien, ikuti rekomendasi berikut ini. Rekomendasi ini akan membantu Anda melindungi dana, mengoptimalkan transaksi, dan menjaga kerahasiaan Anda di jaringan **Bitcoin (onchain)**, **Liquid**, dan **Lightning**.





- **Amankan frasa pemulihan Anda** :
 - Tutorial: Menyimpan frasa Mnemonic Anda



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Gunakan autentikasi yang aman** :
 - Aktifkan **PIN yang kuat** atau **otentikasi biometrik** (sidik jari atau pengenalan wajah) untuk melindungi akses ke aplikasi.
 - Jangan pernah membagikan PIN atau data biometrik Anda.





- **Lindungi privasi Anda** :
 - generate sebuah Address baru untuk setiap penerimaan onchain atau Liquid untuk membatasi penelusuran pada Blockchain.
 - Aktifkan fungsi "Privasi yang Ditingkatkan", "Tor", dan "SPV".
 - Untuk kerahasiaan maksimum, sambungkan Wallet Anda ke node Bitcoin Anda sendiri melalui server Electrum alih-alih menggunakan node publik





- **Pilih jaringan yang paling sesuai dengan kebutuhan Anda**:
- **Onchain**: Lebih disukai untuk penyimpanan jangka panjang atau transaksi bernilai besar (biaya dapat diabaikan dalam kaitannya dengan jumlah).
- **Liquid**: Digunakan untuk transfer cepat dan berbiaya rendah dengan kerahasiaan yang ditingkatkan.
- **Kilat**: Pilih transfer instan dan berbiaya rendah untuk jumlah kecil.





- **Selalu periksa alamat pengiriman**:
 - Sebelum mengirim dana, periksa Address dengan cermat. Dana yang dikirim ke Address yang salah akan hilang selamanya. Gunakan salin/tempel atau pemindaian kode QR, jangan pernah menyalin/memodifikasi Address dengan tangan.





- **Mengoptimalkan biaya**:
 - Untuk transaksi onchain, pilih biaya yang sesuai (lambat, sedang, cepat) sesuai dengan urgensi dan kepadatan jaringan.
 - Gunakan Liquid, atau Lightning untuk jumlah kecil.





- Selalu perbarui aplikasi




### A3. Sumber daya tambahan





- **Tautan resmi:** Tautan resmi
- [Situs web resmi](https://blockstream.com/)
- [Dukungan untuk aplikasi seluler](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): **dokumentasi dan obrolan**
- [GitHub](https://github.com/Blockstream/green_android)





- Penjelajah Blok: **Penjelajah Blok**
 - on chain: **[Mempool.space](https://Mempool.space/)**
 - Liquid: **[Info Blockstream](https://blockstream.info/Liquid)**
 - Petir: **[1ML (Lightning Network)](https://1ml.com/)**





- **Pembelajaran dan tutorial:** [Plan ₿ Network](https://planb.network/) :
 - Mengamankan frasa pemulihan Anda



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network**:
- [Glosarium](https://planb.network/fr/resources/glossary/liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- **Lightning Network**:
- [Glosarium](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb