---
name: Blockstream App - Onchain
description: Mengatur Aplikasi Blockstream di ponsel dan mengelola transaksi onchain
---
![cover](assets/cover.webp)


## 1. Pendahuluan


### 1.1 Tujuan tutorial





- Tutorial ini menjelaskan cara menggunakan aplikasi seluler **Blockstream App** untuk mengelola **onchain** Bitcoin Wallet, yaitu transaksi yang direkam langsung pada Blockchain Bitcoin utama.
- Ini mencakup instalasi, konfigurasi awal, pembuatan Software Wallet, dan operasi untuk menerima dan mengirim bitcoin.
- Catatan: Tutorial lain dalam Lampiran mencakup Liquid, Watch-Only dan versi desktop.



![image](assets/fr/01.webp)



### 1.2 Target audiens





- **Pemula**: Pengguna yang ingin mengelola bitcoin mereka dengan aplikasi seluler yang intuitif.
- **Pengguna tingkat menengah**: Orang-orang yang ingin memahami fungsi onchain dan opsi privasi seperti Tor atau SPV.



### 1.3. Pengingat tentang dompet Hot





- **Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: semua nama untuk aplikasi yang diinstal pada ponsel cerdas, komputer, atau perangkat apa pun yang terhubung ke Internet, yang memungkinkan kunci privat dari Bitcoin Wallet dikelola dan diamankan.
- Tidak seperti **dompet perangkat keras**, juga dikenal sebagai **dompet Cold**, yang mengisolasi kunci secara offline, dompet perangkat lunak beroperasi di lingkungan yang terhubung, sehingga lebih rentan terhadap serangan cyber.





- **Penggunaan yang disarankan**:
    - Ideal untuk mengelola Bitcoin dalam jumlah sedang, terutama untuk transaksi harian.
    - Cocok untuk pemula atau pengguna dengan aset terbatas, yang mungkin menganggap Hardware Wallet tidak berguna.





- **Keterbatasan**: Kurang aman untuk menyimpan dana besar atau tabungan jangka panjang. Dalam hal ini, pilihlah Hardware Wallet.




## 2. Memperkenalkan Aplikasi Blockstream





- **Blockstream App** adalah aplikasi seluler (iOS, Android) dan desktop untuk mengelola portofolio dan aset Bitcoin pada Liquid Network. Diakuisisi oleh [Blockstream] (https://blockstream.com/) pada tahun 2016, sebelumnya bernama *Green Address* dan kemudian *Blockstream Green*.
- **Fitur-fitur utama**:
- **Transaksi Onchain** pada Blockchain Bitcoin.
    - Transaksi jaringan **Liquid** (Sidechain untuk pertukaran yang cepat dan rahasia).
- **Portfolio watch-only** untuk memantau dana tanpa akses ke kunci.
    - Opsi privasi: koneksi melalui **Tor**, koneksi ke **simpul pribadi** melalui Electrum, atau verifikasi **SPV** untuk mengurangi ketergantungan pada simpul pihak ketiga.
    - Berfungsi **Replace-by-fee (RBF)** untuk mempercepat transaksi yang belum dikonfirmasi.
- **Kompatibilitas**: Mengintegrasikan dompet perangkat keras seperti **Blockstream Jade**.
- **Interface**: Intuitif untuk pemula, dengan opsi tingkat lanjut untuk para ahli.
- **Catatan**: Panduan ini berfokus pada penggunaan onchain. Tutorial lain dalam Lampiran mencakup Liquid, Watch-Only, dan versi desktop.



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





- **Fungsi**: Menghubungkan aplikasi ke **node Bitcoin lengkap** Anda sendiri melalui server **Electrum**.
- Mengapa? Memberikan kontrol penuh atas data Blockchain, menghilangkan ketergantungan pada server Blockstream.
- **Prasyarat**: Node Bitcoin yang telah dikonfigurasi.
- **Rekomendasi**: Pengguna tingkat lanjut yang mencari kedaulatan maksimum.


#### 3.2.4. Verifikasi SPV





- **Fungsi**: Menggunakan **Verifikasi Pembayaran Sederhana (SPV)** untuk memverifikasi data Blockchain tertentu secara langsung tanpa mengunduh seluruh rantai.
- Mengapa? Mengurangi ketergantungan pada node default Blockstream, namun tetap ringan untuk perangkat seluler.
- **Kerugian**: Kurang aman dibandingkan Full node, karena bergantung pada node pihak ketiga untuk beberapa informasi.
- **Rekomendasi**: Aktifkan SPV jika Anda tidak dapat menggunakan simpul pribadi, tetapi lebih memilih Full node untuk keamanan optimal.





## 4. Membuat portofolio onchain Bitcoin



### 4.1. Memulai pembuatan





- **Perhatian**: Siapkan portofolio Anda di lingkungan pribadi, tanpa kamera atau pengamat.
- Dari layar beranda, klik "Memulai" :



![image](assets/fr/04.webp)





- Jika Anda ingin mengelola **Cold Wallet** (Wallet offline): klik **"Hubungkan Jade "** untuk menggunakan Hardware Wallet Blockstream Jade atau dompet Cold lain yang kompatibel.



![image](assets/fr/05.webp)





- Layar berikutnya muncul:



![image](assets/fr/06.webp)





- (1) **"Setup Mobile Wallet"**: Membuat Hot Wallet baru (Hot Wallet).
- (2) **"Pulihkan dari Cadangan "**: Mengimpor portofolio yang sudah ada dengan menggunakan frasa Mnemonic (12 atau 24 kata). Perhatian: Jangan mengimpor frasa Cold Wallet, karena akan terekspos pada perangkat yang terhubung, sehingga membatalkan keamanannya.
- (3) **"Hanya-Baca "**: Mengimpor portofolio hanya-baca yang sudah ada, untuk melihat saldo (mis. dari Cold Wallet Anda) tanpa mengekspos frasa Mnemonic. Lihat tutorial Watch Only di lampiran.



**Dalam tutorial ini**: Klik **"Setup Mobile Wallet"** untuk membuat Hot Wallet.


Wallet Anda secara otomatis dibuat dan halaman beranda Wallet, di sini disebut "My Wallet 5", ditampilkan:



![image](assets/fr/07.webp)



**Penting**: Aplikasi Blockstream telah menyederhanakan pembuatan Wallet dengan tidak secara otomatis menampilkan frasa seed yang terdiri dari 12 kata. *Meskipun portofolio sekarang dibuat dalam satu klik, Anda berisiko kehilangan akses ke dana Anda jika Anda tidak menyimpan frasa seed Anda*.



### 4.2. Simpan kalimat seed





- Pada layar beranda Wallet, klik tab "Keamanan", lalu pada prompt "Cadangkan" atau menu "Frasa Pemulihan":



![image](assets/fr/08.webp)



Frasa 12 kata seed akan ditampilkan untuk Anda simpan.





- Tuliskan frasa pemulihan Anda dengan sangat hati-hati. Tuliskan di atas kertas atau logam dan simpan di tempat yang aman (lokasi yang aman dan offline). Frasa ini adalah satu-satunya cara untuk mengakses bitcoin Anda jika perangkat Anda hilang atau aplikasi dihapus.
- Penting juga untuk diperhatikan bahwa siapa pun yang memiliki frasa ini dapat mencuri semua bitcoin Anda. Jangan pernah menyimpannya secara digital:
 - Tidak ada tangkapan layar
 - Tidak ada cadangan awan, email, atau pesan
 - Tidak ada salin/tempel (risiko menyimpan ke clipboard)



**! Poin ini sangat penting**. Untuk informasi lebih lanjut mengenai pencadangan :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Konfirmasikan kalimat seed



Sebelum mengirim dana ke Address yang terkait dengan kalimat seed ini, Anda harus menguji cadangan 12 kata Anda.



Untuk melakukan ini, kita akan menuliskan referensi, menghapus Wallet, mengembalikannya dengan cadangan, dan memeriksa bahwa referensi tidak berubah.





- Pada layar beranda Wallet, klik pada tab "Pengaturan", lalu pada "Detail Wallet", dan salin zPub ([kunci publik yang diperluas](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8dcffce1-31bd-5e0b-965b-735f5f9e4602):



![image](assets/fr/09.webp)



Catatan: zpub Address dapat diimpor ke dalam aplikasi Blockstream Anda untuk fungsi "Watch Only" (lihat Lampiran).





- Hapus aplikasi, lalu pulihkan Wallet melalui **"Pulihkan dari Cadangan "** dengan memasukkan frasa Mnemonic, dan periksa apakah zpub tidak berubah. Jika ya, maka cadangan Anda sudah benar, dan Anda dapat mengirim dana ke Wallet.





- Untuk mempelajari lebih lanjut tentang cara melakukan tes pemulihan, berikut ini adalah tutorial khusus:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.5. Mengamankan akses ke aplikasi



Mengunci akses ke aplikasi dengan kode PIN yang kuat:




- Dari layar beranda Wallet, buka **"Keamanan "** lalu klik **"PIN "**
- Masukkan dan konfirmasikan **kode PIN 6 digit acak**.



**Opsi biometrik**: Tersedia untuk menambah kenyamanan, tetapi kurang aman dibandingkan dengan kode PIN yang kuat (risiko akses yang tidak sah, misalnya pemindaian sidik jari atau wajah saat tidur).



**Catatan**: PIN mengamankan perangkat, tetapi hanya frasa seed yang dapat digunakan untuk mengambil dana.





## 5. Menggunakan onchain Wallet



### 5.1. Menerima bitcoin





- Dari layar beranda portofolio, klik '"**Transaksi**" lalu **"Terima "**.



![image](assets/fr/10.webp)





- Aplikasi menampilkan **penerimaan kosong Address** (format SegWit v0, dimulai dengan `bc1q...`). Menggunakan Address baru setiap kali Anda menerima Bitcoin akan meningkatkan kerahasiaan Anda.





- **Opsi** :
    - (1) "Bitcoin": klik untuk memilih pengiriman onchain atau Liquid, dan pilih aset.
    - (2) Klik tanda panah untuk memilih Address baru lainnya yang terkait dengan kalimat seed ini.
    - (3) Anda juga dapat memilih Address dari antara yang sudah digunakan/ditampilkan, dengan mengeklik tiga titik di kanan atas dan kemudian pada "Daftar Alamat"
    - (4) Untuk meminta jumlah tertentu, klik pada tiga titik di kanan atas, pilih "Minta jumlah", dan masukkan jumlah yang diinginkan. QR akan diperbarui, dan Address akan diganti dengan URI pembayaran Bitcoin.




![image](assets/fr/11.webp)





- Bagikan Address/URI dengan mengeklik "**Bagikan**", menyalin teks, atau memindai kode QR.
- **Verifikasi**: Periksa Address yang dibagikan kepada penerima sejauh mungkin untuk menghindari kesalahan atau serangan (misalnya malware yang memodifikasi clipboard).



### 5.2. mengirim bitcoin





- Dari layar beranda portofolio, klik "**Transaksi**" kemudian **"Kirim "**:



![image](assets/fr/12.webp)





- Masukkan **detail**:
    - (1) Masukkan **Address penerima** dengan menempelkannya atau memindai kode QR.
    - (2) Periksa aset dan rekening tujuan pengiriman dana.
    - (3) Tunjukkan **jumlah** yang akan dikirim. Anda dapat memilih unit: BTC, satoshi, USD, ...


Jumlah minimum (batas dush) pada tanggal 03/08/2025 adalah 546 Sats.




    - (4) Pilih **biaya transaksi** :
        - Pilih dari opsi yang disarankan (misalnya cepat, sedang, lambat) tergantung pada urgensi, dan perkiraan waktu transfer akan ditampilkan.
        - Untuk biaya yang disesuaikan, sesuaikan secara manual jumlah Satoshi per vbytes (lihat [Mempool.space](https://Mempool.space/) untuk harga pasar).




![image](assets/fr/13.webp)





- Centang **:**
    - Periksa Address, jumlah dan biaya pada layar ringkasan.
    - Kesalahan Address dapat mengakibatkan hilangnya dana yang tidak dapat dipulihkan. Waspadai malware yang memodifikasi clipboard.



![image](assets/fr/14.webp)





- **Konfirmasi**: Geser tombol "Kirim" untuk menandatangani dan mendistribusikan transaksi.
- **Tindak lanjut**: Pada tab "Transact" di Wallet, transaksi akan muncul sebagai "pending" hingga konfirmasi (1 hingga 6 konfirmasi):



![image](assets/fr/15.webp)





- Selama transaksi belum dikonfirmasi, fungsi "Replace by fee" (lihat Lampiran) memungkinkan Anda untuk mempercepat penanganannya dengan meningkatkan biaya transaksi:



![image](assets/fr/16.webp)




## Lampiran



### A1. Tutorial Blockstream lainnya



Menggunakan Liquid Network



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Mengimpor dan melacak Wallet dalam mode "Hanya Menonton"



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Versi desktop



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Penjelasan tentang Replace-by-fee (RBF)



**Definisi**: Replace-by-fee (RBF) adalah fitur jaringan Bitcoin yang memungkinkan pengirim untuk mempercepat konfirmasi transaksi **onchain** dengan menyetujui untuk membayar biaya yang lebih tinggi.



**Batas** :




- RBF tidak tersedia untuk transaksi Liquid atau Lightning.
- Transaksi awal harus ditandai sebagai kompatibel dengan RBF saat dibuat, yang dilakukan oleh Aplikasi Blockstream secara otomatis.



**Info lebih lanjut:**




- [Glosarium](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Praktik terbaik



Untuk menggunakan **Aplikasi Blockstream** dengan aman dan efisien, ikuti rekomendasi berikut ini. Rekomendasi ini akan membantu Anda melindungi dana, mengoptimalkan transaksi, dan menjaga kerahasiaan Anda di jaringan **Bitcoin (onchain)**, **Liquid**, dan **Lightning**.





- **Amankan frasa pemulihan Anda** :
 - Tutorial: Menyimpan frasa Mnemonic Anda



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Gunakan autentikasi yang aman** :
 - Aktifkan **PIN yang kuat** atau **otentikasi biometrik** (sidik jari atau pengenalan wajah) untuk melindungi akses ke aplikasi.
 - Jangan pernah membagikan PIN atau data biometrik Anda.





- **Lindungi privasi Anda** :
 - generate Address baru untuk setiap penerimaan onchain atau Liquid untuk membatasi penelusuran pada Blockchain.
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




### A4. Sumber daya tambahan





- **Tautan resmi:** Tautan resmi
- [Situs web resmi](https://blockstream.com/)
- [Dukungan untuk aplikasi seluler](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): **dokumentasi dan obrolan**
- [GitHub](https://github.com/Blockstream/green_android)





- Penjelajah Blok: **Penjelajah Blok**
 - on chain: **[Mempool.space](https://Mempool.space/)**
 - Liquid : ** [Info Blockstream] (https://blockstream.info/Liquid) **
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