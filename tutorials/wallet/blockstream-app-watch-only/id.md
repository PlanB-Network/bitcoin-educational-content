---
name: Aplikasi Blockstream - Hanya untuk Ditonton
description: Bagaimana cara mengkonfigurasi Watch-only wallet di Aplikasi Blockstream?
---

![cover](assets/cover.webp)


## 1. Pendahuluan


### 1.1 Tujuan dari tutorial ini





- Tutorial ini menjelaskan cara mengatur dan menggunakan fitur **Watch-Only** pada aplikasi seluler **Blockstream App** untuk memonitor Bitcoin Wallet tanpa mengakses kunci privatnya.
- Ini mencakup instalasi, konfigurasi awal, mengimpor kunci publik yang diperluas, dan menggunakannya untuk melacak saldo dan alamat penerima generate.
- Catatan: Tutorial lainnya, yang disediakan dalam lampiran, mencakup Onchain, Liquid, dan versi desktop.



### 1.2. Target audiens





- Pemula**: Pengguna yang ingin memantau portofolio Bitcoin (sering dikaitkan dengan Hardware Wallet) melalui aplikasi seluler yang intuitif.
- Pengguna tingkat menengah**: Orang yang ingin mengelola portofolio hanya-baca sambil menggunakan opsi privasi seperti Tor atau SPV.
- Pemilik Hardware Wallet**: Untuk memeriksa saldo dan alamat generate mereka tanpa menghubungkan perangkat mereka.
- Bisnis dan pertokoan** :
 - Lacak transaksi Anda untuk tujuan akuntansi tanpa mengekspos kunci pribadi Anda.
 - Verifikasi transaksi yang diterima tanpa memasukkan kunci pribadi mereka dalam sistem pembayaran online.
 - Memungkinkan karyawan untuk generate alamat penerimaan baru tanpa memiliki akses ke kunci pribadi.
- Organisasi dan urun dana**: Menampilkan saldo secara transparan kepada donatur tanpa mengizinkan akses ke dana.



### 1.3. Memperkenalkan Watch-Only



Wallet **Watch-Only** memungkinkan Anda untuk memonitor transaksi dan saldo Bitcoin Wallet tanpa memiliki akses ke private key. Tidak seperti Wallet konvensional, Wallet hanya menyimpan data publik, seperti **kunci publik **yang diperluas** (yang memunculkan "**xpub**", kemudian "zpub", "ypub", dll.), yang memungkinkannya untuk mendapatkan alamat penerima dan melacak riwayat transaksi pada Blockchain Bitcoin. Tidak adanya kunci privat membuat tidak mungkin untuk mencairkan dana dari aplikasi, menjamin keamanan yang lebih baik.



![image](assets/fr/10.webp)



**Mengapa menggunakan Watch-only wallet?





- Keamanan**: Ideal untuk memantau portofolio yang diamankan oleh **Hardware Wallet** tanpa mengekspos kunci privat pada perangkat yang terhubung.
- Kenyamanan**: Memungkinkan Anda untuk memeriksa saldo dan alamat penerima baru generate tanpa menghubungkan Hardware Wallet.
- Kerahasiaan**: Kompatibel dengan opsi seperti **Tor** atau **SPV** untuk membatasi ketergantungan pada server pihak ketiga.
- Kasus penggunaan**: Melacak dana saat bepergian, membuat alamat untuk menerima pembayaran, atau memverifikasi transaksi tanpa mempertaruhkan kunci pribadi.



![image](assets/fr/01.webp)



### 1.4. Kunci publik yang diperluas



Sebuah **kunci publik yang diperluas** (xpub, ypub, zpub, dll.) adalah sebuah data yang berasal dari Bitcoin Wallet yang menghasilkan semua kunci publik anak dan alamat penerimaan terkait, tanpa memberikan akses ke kunci privat.





- Bagaimana cara kerjanya** : Kunci publik yang diperluas dihasilkan dari frasa seed melalui proses deterministik (BIP-32). Proses ini menciptakan sebuah pohon hirarkis dari kunci publik anak, yang masing-masing dapat dikonversi menjadi Address yang diterima. Dengan menggunakan jalur derivasi yang sama (contoh: `m/44'/0'/0'`) dengan Wallet yang ditonton, Watch-only wallet menghasilkan alamat yang sama, sehingga memungkinkan dana untuk dilacak dan alamat penerima baru dapat dibuat.



![image](assets/fr/11.webp)





- Jenis kunci publik yang diperluas
 - xpub**: Digunakan untuk portofolio Legacy (alamat yang dimulai dengan "1", BIP-44) dan portofolio Taproot (alamat yang dimulai dengan "bc1p", BIP-86).
 - ypub**: Didesain untuk dompet SegWit yang kompatibel (alamat yang dimulai dengan "3", BIP-49).
 - zpub**: Terkait dengan portofolio SegWit asli (alamat yang dimulai dengan "bc1q", BIP-84).
 - Lainnya (tpub, upub, vpub, dll.)**: Digunakan untuk jaringan alternatif (seperti Testnet) atau standar tertentu. Misalnya, tpub untuk jaringan Testnet.





- Perbedaan** : Pilihan antara xpub, ypub, atau zpub bergantung pada tipe Address (legacy, SegWit, Taproot, atau SegWit bersarang) dan standar BIP yang digunakan oleh Wallet. Periksa format yang diperlukan oleh portofolio sumber Anda untuk memastikan kompatibilitas dengan Blockstream App.





- Keamanan dan kerahasiaan**: Kunci publik yang diperluas tidak sensitif dalam hal keamanan, karena tidak mengizinkan dana dibelanjakan (tidak ada akses ke kunci pribadi). Akan tetapi, kunci ini sensitif dalam hal kerahasiaan, karena kunci ini mengungkapkan semua alamat publik dan riwayat transaksi yang terkait.



**Rekomendasi**: Lindungi kunci publik Anda yang diperluas sebagai informasi sensitif.



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5. Pengingat Hot Wallet





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: semua nama untuk aplikasi yang diinstal pada ponsel cerdas, komputer, atau perangkat apa pun yang terhubung ke Internet, yang memungkinkan kunci privat dari Bitcoin Wallet dikelola dan diamankan.
- Tidak seperti **dompet perangkat keras**, juga dikenal sebagai **dompet Cold**, yang mengisolasi kunci secara offline, dompet perangkat lunak beroperasi di lingkungan yang terhubung, sehingga lebih rentan terhadap serangan cyber.





- Penggunaan yang disarankan** :
    - Ideal untuk mengelola Bitcoin dalam jumlah sedang, terutama untuk transaksi harian.
    - Cocok untuk pemula atau pengguna dengan aset terbatas, yang mungkin menganggap Hardware Wallet tidak berguna.





- Keterbatasan**: Kurang aman untuk menyimpan dana besar atau tabungan jangka panjang. Dalam hal ini, pilihlah Hardware Wallet.




## 2. Memperkenalkan Aplikasi Blockstream





- Blockstream App** adalah aplikasi seluler (iOS, Android) dan desktop untuk mengelola portofolio dan aset Bitcoin pada Liquid Network. Diakuisisi oleh [Blockstream] (https://blockstream.com/) pada tahun 2016, sebelumnya bernama *Green Address* dan kemudian *Blockstream Green*.
- Fitur-fitur utama** :
    - Transaksi Onchain** pada Blockchain Bitcoin.
    - Transaksi di jaringan **Liquid** (Sidechain untuk pertukaran yang cepat dan rahasia).
    - Portofolio watch-only** untuk memantau dana tanpa akses ke kunci.
    - Opsi privasi: koneksi melalui **Tor**, koneksi ke **simpul pribadi** melalui Electrum, atau verifikasi **SPV** untuk mengurangi ketergantungan pada simpul pihak ketiga.
    - Berfungsi **Replace-by-fee (RBF)** untuk mempercepat transaksi yang belum dikonfirmasi.
- Kompatibilitas**: Mengintegrasikan dompet perangkat keras seperti **Blockstream Jade**.
- Interface**: Intuitif untuk pemula, dengan opsi tingkat lanjut untuk para ahli.
- Catatan**: Panduan ini berfokus pada penggunaan onchain. Tutorial lain dalam Lampiran mencakup Onchain, Watch-Only, dan versi desktop.




## 3. Menginstal dan mengonfigurasi Aplikasi Blockstream



### 3.1. Unduh





- Untuk Android** :
    - Unduh [Aplikasi Blockstream](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) dari Google Play Store.
    - Alternatif: Instal melalui file APK yang tersedia di [GitHub resmi Blockstream](https://github.com/Blockstream/green_android).
- Untuk iOS** :
    - Unduh [Aplikasi Blockstream](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) dari App Store.
- Catatan**: Pastikan untuk mengunduh dari sumber resmi untuk menghindari aplikasi palsu.



### 3.2. konfigurasi awal





- Layar beranda**: Saat pertama kali dibuka, aplikasi menampilkan layar tanpa Wallet yang dikonfigurasi. Portofolio yang dibuat atau diimpor akan muncul di sini nanti.



![image](assets/fr/02.webp)





- Menyesuaikan pengaturan**: Klik "Pengaturan aplikasi", sesuaikan opsi di bawah ini, klik "Simpan", mulai ulang aplikasi dan buat portofolio Anda.



![image](assets/fr/03.webp)



#### 3.2.1. Privasi yang ditingkatkan (hanya untuk Android)





- Fungsi**: Menonaktifkan tangkapan layar, menyembunyikan pratinjau aplikasi di pengelola tugas, dan mengunci akses saat ponsel terkunci.
- Mengapa? Melindungi data Anda dari akses fisik yang tidak sah atau malware penangkap layar.



#### 3.2.2. Koneksi melalui Tor





- Fungsi**: Merutekan lalu lintas jaringan melalui **Tor**, sebuah jaringan anonim yang mengenkripsi koneksi Anda.
- Mengapa? Menyembunyikan IP Anda Address dan melindungi privasi Anda, ideal jika Anda tidak mempercayai jaringan Anda (Wi-Fi publik, misalnya).
- Kerugian**: Dapat memperlambat aplikasi karena enkripsi.
- Rekomendasi**: Aktifkan Tor jika kerahasiaan adalah prioritas, tetapi uji kecepatan koneksi.



#### 3.2.3. Menghubungkan ke simpul pribadi





- Fungsi**: Menghubungkan aplikasi ke **node Bitcoin lengkap** milik Anda sendiri melalui **server Electrum**.
- Mengapa? Memberikan kontrol penuh atas data Blockchain, menghilangkan ketergantungan pada server Blockstream.
- Prasyarat**: Node Bitcoin yang telah dikonfigurasi.
- Rekomendasi**: Pengguna tingkat lanjut yang menginginkan kedaulatan maksimum.



#### 3.2.4. Verifikasi SPV





- Fungsi**: Menggunakan **Verifikasi Pembayaran Sederhana (SPV)** untuk memverifikasi data Blockchain tertentu secara langsung tanpa mengunduh seluruh rantai.
- Mengapa? Mengurangi ketergantungan pada node default Blockstream, namun tetap ringan untuk perangkat seluler.
- Kerugian**: Kurang aman dibandingkan Full node, karena bergantung pada node pihak ketiga untuk beberapa informasi.
- Rekomendasi**: Aktifkan SPV jika Anda tidak dapat menggunakan simpul pribadi, tetapi lebih memilih Full node untuk keamanan optimal.





## 4. Membuat portofolio "Khusus Jam Tangan" Bitcoin



### 4.1. Memulihkan kunci publik yang diperpanjang



Untuk menyiapkan Watch-only wallet, Anda harus terlebih dahulu mendapatkan kunci publik yang diperluas (xpub, ypub, zpub, dll.) dari Wallet yang akan dimonitor. Informasi ini umumnya tersedia di bagian pengaturan atau "informasi Wallet" pada perangkat lunak Anda atau Hardware Wallet.





- Contoh dengan Aplikasi Blockstream: Dari layar beranda Wallet, buka "Pengaturan", lalu "Rincian Wallet", dan salin zpub :



![image](assets/fr/09.webp)





- Alternatif 1: generate kode QR yang berisi kunci publik yang diperluas untuk pemindaian pada langkah berikutnya.
- Alternatif 2: Gunakan output descriptor jika Wallet Anda menyediakannya.



### 4.2. impor Wallet khusus jam tangan





- Perhatian**: Siapkan portofolio Anda di lingkungan pribadi, tanpa kamera atau pengamat.
- Dari layar beranda, klik "Siapkan portofolio baru" dan kemudian pada "Memulai" :



![image](assets/fr/04.webp)





- Layar berikutnya muncul:



![image](assets/fr/06.webp)






- (1) **"Setup Mobile Wallet"**: Membuat Hot Wallet yang baru. Lihat tutorial "Aplikasi Blockstream - Onchain" di lampiran.
- (2) **"Pulihkan dari Cadangan "**: Mengimpor portofolio yang sudah ada dengan menggunakan frasa Mnemonic (12 atau 24 kata). Perhatian: Jangan mengimpor frasa dari Cold Wallet, karena frasa tersebut akan terekspos pada perangkat yang terhubung, dan membatalkan keamanannya.
- (3) **"Hanya-Tonton "**: opsi yang kami minati untuk tutorial ini.





- Kemudian pilih "**Tanda tangan tunggal**" dan jaringan "**Bitcoin**":



![image](assets/fr/12.webp)





- Rekatkan kunci publik yang diperluas (xpub, ypub, zpub, dll.), pindai kode QR yang sesuai, atau masukkan output descriptor. Meskipun aplikasi menetapkan "xpub", kunci ypub, zpub, dll. juga disahkan. Kemudian klik "Hubungkan":



![image](assets/fr/13.webp)




### 4.3. Menggunakan Wallet Watch-only



Setelah diimpor, Watch-only wallet menampilkan total saldo dan riwayat transaksi dari alamat yang berasal dari public key yang diperluas. Hanya transaksi onchain yang terlihat (transaksi Liquid diabaikan). Untuk memonitor Liquid Wallet, ulangi impor dengan memilih "Liquid" pada langkah sebelumnya.





- Lihat saldo dan riwayat**: dari layar beranda, lihat saldo total dan riwayat transaksi onchain:



![image](assets/fr/14.webp)





- generate adalah Address yang sedang menerima**: Klik "Transaksikan", lalu "Terima", untuk membuat Address onchain baru. Bagikan melalui kode QR atau salin untuk menerima dana:



![image](assets/fr/15.webp)





- Kirim dana**: Klik **"Bertransaksi "**, lalu **"Kirim "**. Anda dapat memasukkan :
 - Penerima Address.
 - Jumlah transaksi.
 - Biaya transaksi.



Namun, karena Watch-only wallet tidak menyimpan private key, Anda tidak dapat mengirim dana secara langsung. Untuk menandatangani transaksi, hubungkan Hardware Wallet atau Exchange PSBT Anda dengan memindai kode QR (opsi yang tersedia pada Coldcard Q, misalnya).



![image](assets/fr/16.webp)





- Catatan**: Selalu periksa Address yang diterima dan detail transaksi untuk menghindari kesalahan. Dana yang dikirim ke Address yang salah tidak dapat dikembalikan.




## Lampiran



### A1. Tutorial Aplikasi Blockstream lainnya





- Menggunakan jaringan Onchain :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143



- Menggunakan Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Versi desktop :



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Kunci publik yang diperluas





- Daftar Istilah :
 - [Kunci publik yang diperluas] (https://planb.network/fr/resources/glossary/extended-key)
 - [xpub](https://planb.network/fr/resources/glossary/xpub)
 - [ypub](https://planb.network/fr/resources/glossary/ypub)
 - [zpub](https://planb.network/fr/resources/glossary/zpub)
- Tentu saja:
 - [Les clés publiques étendues](https://planb.network/fr/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/les-cles-etendues-8dcffce1-31bd-5e0b-965b-735f5f9e4602)




### A3. Praktik terbaik



Untuk menggunakan **Aplikasi Blockstream** dengan aman dan efisien, ikuti rekomendasi berikut ini. Rekomendasi ini akan membantu Anda melindungi dana, mengoptimalkan transaksi, dan menjaga kerahasiaan Anda di jaringan **Bitcoin (onchain)**, **Liquid**, dan **Lightning**.





- Amankan frasa pemulihan Anda** :
 - Tutorial: Menyimpan frasa Mnemonic Anda



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Gunakan autentikasi yang aman** :
 - Aktifkan **PIN yang kuat** atau **otentikasi biometrik** (sidik jari atau pengenalan wajah) untuk melindungi akses ke aplikasi.
 - Jangan pernah membagikan PIN atau data biometrik Anda.





- Lindungi privasi Anda** :
 - generate Address baru untuk setiap penerimaan onchain atau Liquid untuk membatasi penelusuran pada Blockchain.
 - Aktifkan fungsi "Privasi yang Ditingkatkan", "Tor", dan "SPV".
 - Untuk kerahasiaan maksimum, sambungkan Wallet Anda ke node Bitcoin Anda sendiri melalui server Electrum alih-alih menggunakan node publik





- Pilih jaringan yang paling sesuai dengan kebutuhan Anda**:
 - Onchain**: Lebih disukai untuk penyimpanan jangka panjang atau transaksi bernilai besar (biaya dapat diabaikan dalam kaitannya dengan jumlah).
 - Liquid**: Digunakan untuk transfer cepat dan berbiaya rendah dengan kerahasiaan yang ditingkatkan.
 - Kilat**: Pilih transfer instan dan berbiaya rendah untuk jumlah kecil.





- Selalu periksa alamat pengiriman**:
 - Sebelum mengirim dana, periksa Address dengan cermat. Dana yang dikirim ke Address yang salah akan hilang selamanya. Gunakan salin/tempel atau pemindaian kode QR, jangan pernah menyalin/memodifikasi Address dengan tangan.





- Mengoptimalkan biaya**:
 - Untuk transaksi onchain, pilih biaya yang sesuai (lambat, sedang, cepat) sesuai dengan urgensi dan kepadatan jaringan.
 - Gunakan Liquid, atau Lightning untuk jumlah kecil.





- Selalu perbarui aplikasi




### A4. Sumber daya tambahan





- Tautan resmi Blockstream:** Tautan resmi
 - [Situs web resmi](https://blockstream.com/)**
 - [Dukungan untuk aplikasi seluler](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)**: dokumentasi dan obrolan
 - [GitHub](https://github.com/Blockstream/green_android)**





- Penjelajah Blok: ** Penjelajah Blok
 - Onchain: **[Mempool.space](https://Mempool.space/)**
 - Liquid : ** [Info Blockstream] (https://blockstream.info/Liquid) **
 - Petir: **[1ML (Lightning Network)](https://1ml.com/)**





 - Pembelajaran dan tutorial:** **[Plan ₿ Network](https://planb.network/)** :
  - Mengamankan frasa pemulihan Anda



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network**:
 - [Glosarium](https://planb.network/fr/resources/glossary/Liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network**:
 - [Glosarium](https://planb.network/fr/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb