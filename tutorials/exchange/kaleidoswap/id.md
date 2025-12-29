---
name: KaleidoSwap
description: Panduan lanjutan untuk perdagangan aset RGB di Lightning Network dengan KaleidoSwap
---

![cover](assets/cover.webp)


KaleidoSwap adalah aplikasi desktop open-source canggih yang menjembatani kesenjangan antara Protokol RGB dan Lightning Network. Aplikasi ini berfungsi sebagai antarmuka yang komprehensif untuk mengelola RGB Lightning Nodes, berinteraksi dengan Penyedia Layanan Lightning (LSP) RGB melalui spesifikasi LSPS1, dan mengeksekusi pertukaran atomik aset RGB.


Sebagai solusi non-kustodian, KaleidoSwap memberdayakan pengguna untuk mempertahankan kontrol penuh atas kunci dan data mereka. Dengan memanfaatkan paradigma validasi sisi klien dari RGB, solusi ini memungkinkan kontrak pintar yang privat dan dapat diskalakan di atas Bitcoin. Tutorial ini membahas fitur-fitur canggih KaleidoSwap, memandu Anda melalui seluk-beluk manajemen UTXO "Berwarna", menyalurkan likuiditas untuk aset tertentu, dan model perdagangan pengambil-pembuat, memastikan Anda dapat sepenuhnya memanfaatkan protokol pertukaran terdesentralisasi yang kuat ini.


## Instalasi


KaleidoSwap menyediakan binari yang sudah dibuat sebelumnya untuk sistem operasi utama, tetapi untuk pengguna tingkat lanjut, membangun dari sumber memastikan Anda menjalankan kode terbaru dengan konfigurasi spesifik Anda.


### Unduh Binari


Anda dapat mengunduh rilis terbaru untuk sistem operasi Anda dari [situs web resmi](https://kaleidoswap.com/) atau [halaman rilis GitHub](https://github.com/kaleidoswap/desktop-app/releases).


### Metode Instalasi


1.  **Windows**: Unduh penginstalasi `.exe` dan jalankan.

2.  **macOS**: Unduh file `.dmg`, buka, dan seret KaleidoSwap ke folder Aplikasi Anda.

3.  **Linux**: Unduh file `.AppImage` atau `.deb` dan instal/jalankan.



## Opsi Pengaturan Node


Ketika Anda pertama kali meluncurkan KaleidoSwap, Anda akan dihadapkan pada **Layar Koneksi**. Ini adalah langkah pertama dalam mengonfigurasi lingkungan Anda.


![Node Selection Screen](assets/en/01.webp)


Anda harus memilih cara menghubungkan ke RGB Lightning Network. Pilihan ini berdampak pada tingkat kontrol dan privasi Anda.


### Opsi 1: Node Lokal (Direkomendasikan untuk Penitipan Mandiri)


**Untuk kontrol penuh dan privasi**, jalankan node secara langsung di mesin Anda, lihat keuntungannya di bawah ini:


- Penitipan Mandiri**: Anda memegang kuncinya. Tidak ada pihak ketiga yang dapat membekukan dana Anda atau menyensor transaksi Anda.
- Privasi**: Data Anda tetap berada di perangkat Anda.
- Kemandirian**: Tidak ada ketergantungan pada penyedia layanan eksternal.


Jika Anda memilih **Local Node**, Anda akan dibawa ke layar pengaturan di mana Anda dapat membuat wallet baru atau memulihkan yang sudah ada.


![Local Node Setup Screen](assets/en/02.webp)


### Opsi 2: Node Jarak Jauh


Sambungkan ke RGB Lightning Node jarak jauh (dihosting sendiri pada VPS atau penyedia yang dihosting).


- Keuntungan**: Tidak ada penggunaan sumber daya lokal, ketersediaan 24/7.
- Pertukaran**: Memerlukan kepercayaan pada host atau mengelola server jarak jauh.


![Remote Node Setup Screen](assets/en/03.webp)


**KaleidoSwap dirancang untuk memberdayakan penyimpanan mandiri (self-custody) ** Kami sangat menyarankan untuk menjalankan node Anda sendiri-baik secara lokal (Opsi 1) atau dengan menghosting node jarak jauh sendiri-untuk sepenuhnya memanfaatkan sifat tahan sensor Bitcoin dan RGB.


## Membuat Wallet


KaleidoSwap mengelola aset Bitcoin dan RGB. Proses pembuatan wallet menginisialisasi keystore yang mengamankan dana on-chain dan status saluran Lightning Anda.


Berikut ini prosesnya secara rinci:

1. Buka KaleidoSwap dan pilih **Simpul Lokal**.

2. Klik **Buat Wallet Baru**.

3. **Penyiapan Akun**: Masukkan **Nama Rekening** dan pilih **Jaringan** (mis., Bitcoin Mainnet, Testnet, Signet).

4. **Konfigurasi Lanjutan** (Opsional): Jika Anda adalah pengguna yang memiliki kuasa, Anda dapat mengonfigurasi titik akhir RPC, URL Pengindeks, atau pengaturan Proksi khusus pada "Pengaturan Lanjutan".

5. Klik **Lanjutkan**.

6. **Kata Sandi**: Tetapkan kata sandi yang kuat untuk mengenkripsi file wallet Anda secara lokal.

7. **Frasa Pemulihan**: Tuliskan frasa seed Anda dan simpan dengan aman.


    - Kritis**: Frasa ini diperlukan untuk memulihkan dana on-chain dan identitas node Anda.
    - Peringatan**: **Status saluran petir tidak dapat dipulihkan sepenuhnya dari seed saja**. Anda juga harus memelihara Cadangan Saluran Statis (SCB) untuk memulihkan dana yang terkunci di saluran.


![Wallet Creation Screen](assets/en/04.webp)



## Ikhtisar Dasbor


Setelah wallet Anda dibuat, Anda akan diarahkan ke **Dashboard** utama.


![KaleidoSwap Dashboard](assets/en/05.webp)


catatan: Tangkapan layar di atas menunjukkan wallet yang telah didanai dan memiliki saluran aktif. wallet yang baru akan menunjukkan saldo nol dan tidak ada saluran aktif sampai Anda mendanainya._


## Mendanai Wallet Anda


Untuk beroperasi dengan aset RGB, Anda perlu mendanai wallet Anda. KaleidoSwap mendukung penyetoran aset Bitcoin dan RGB melalui transaksi on-chain atau Lightning Network.


### Menyetorkan Bitcoin


1. Klik **Deposit** di menu Tindakan Cepat.

2. Pilih **BTC** dari daftar aset.


![Select BTC Asset](assets/en/06.webp)


3. Pilih metode deposit Anda: **On-chain** atau **Kilat**.


![BTC Deposit Options](assets/en/07.webp)



- Secara berantai**: Pindai kode QR atau salin alamat untuk mengirim Bitcoin dari wallet lainnya.
- Petir**: Membuat faktur untuk jumlah yang diinginkan.


![BTC On-chain Deposit](assets/en/08.webp)


### Menyimpan Aset RGB & UTXO Berwarna


Untuk menerima aset RGB (seperti USDT), Anda memerlukan UTXO tertentu yang tersedia untuk "diwarnai" (diberi aset).


1. Klik **Deposit** dan pilih aset RGB (mis., USDT). **Penting**: Jika ini adalah **pertama kalinya** node Anda menerima aset tertentu, **kosongkan kolom ID Aset**. Memasukkan ID untuk aset yang tidak dikenal akan menyebabkan node mengembalikan kesalahan karena belum mengenalinya.

2. Pilih **On-chain** atau **Lightning**.


![USDT Deposit Options](assets/en/09.webp)


#### Mode Penerimaan On-chain: Saksi vs. Dibutakan


Saat menerima aset RGB on-chain, Anda memiliki dua mode privasi:



- Terima Buta (Direkomendasikan untuk Privasi)**: Anda memberikan UTXO "blinded" kepada pengirim. Anda meminta pengirim untuk mengirimkan aset ke UTXO yang sudah ada yang Anda miliki, tetapi Anda menyamarkan pengenal UTXO yang sebenarnya. Ini menawarkan privasi yang lebih baik.
- Saksi Menerima**: Anda memberikan alamat Bitcoin standar. Anda meminta pengirim untuk membuat UTXO *baru* untuk Anda dengan mengirimkan aset ke alamat tersebut. Hal ini memungkinkan aset RGB dilampirkan langsung ke UTXO baru yang dibuat oleh transaksi.


#### Deposit Petir


Untuk setoran Lightning, cukup dengan generate faktur. Aset RGB akan disalurkan kepada Anda melalui saluran terbuka Anda.


![USDT Lightning Invoice](assets/en/10.webp)



## Membuka Saluran dengan Aset RGB


Untuk merutekan aset RGB melalui Lightning Network, Anda memerlukan saluran dengan likuiditas dan alokasi aset yang memadai. Cara termudah untuk memulai adalah dengan **Beli Saluran** dari LSP (Penyedia Layanan Lightning).


### Membeli Saluran dari Kaleido LSP


1. Buka tab **Saluran**. Anda akan melihat pilihan untuk "Buka Saluran" (manual) atau "Beli Saluran" (LSP).

2. Klik **Beli Saluran**.


![Channels Dashboard](assets/en/11.webp)


3. **Hubungkan ke LSP**: Aplikasi ini akan terhubung ke LSP Kaleido default. Penyedia ini menawarkan likuiditas masuk dan mendukung perutean aset RGB.


![Connect to LSP](assets/en/12.webp)


4. **Konfigurasi Saluran**:


    - Kapasitas**: Pilih total kapasitas Bitcoin untuk saluran tersebut.
    - Alokasi RGB**: Pilih aset RGB (mis., USDT) yang ingin Anda terima atau kirim. LSP akan memastikan saluran dikonfigurasikan untuk mendukung aset ini.


![Configure Channel](assets/en/13.webp)



    - Alokasi RGB**: Pilih aset RGB (mis., USDT) yang ingin Anda terima atau kirim. LSP akan memastikan saluran dikonfigurasikan untuk mendukung aset ini.


![RGB Allocation](assets/en/14.webp)


5.  **Pembayaran**: Anda harus membayar biaya kepada LSP untuk membuka saluran dan menyediakan likuiditas. Anda dapat membayar menggunakan **Lightning** atau **On-chain** Bitcoin. Pembayaran dapat dilakukan dari KaleidoSwap wallet internal Anda atau wallet eksternal.


![Complete Payment](assets/en/15.webp)


6. Setelah pembayaran dikonfirmasi, LSP akan memulai transaksi pembukaan saluran. Anda akan melihat layar **Pesanan Selesai**.


![Order Completed](assets/en/16.webp)


7. Setelah konfirmasi di blockchain, saluran Anda akan aktif dan siap untuk transfer RGB.



## Perdagangan: Model Pengambil-Pembuat


Mesin perdagangan KaleidoSwap beroperasi pada model **Taker-Maker**. Anda dapat menukar aset secara manual dengan rekan atau menggunakan Pembuat Pasar (LSP).


### Bertukar dengan Pembuat Pasar (LSP)


Ini adalah cara yang paling umum untuk berdagang. Anda bertindak sebagai **Taker**, mengeksekusi order terhadap likuiditas yang tersedia yang disediakan oleh LSP (**Maker**).


1. Buka tab **Trade** dan pilih **Pembuat Pasar**.

2. **Masukkan Jumlah**: Masukkan jumlah Bitcoin yang ingin Anda kirim (atau aset yang ingin Anda terima). Antarmuka akan menampilkan perkiraan nilai tukar dan biaya.


![Market Maker Swap](assets/en/17.webp)


3. **Konfirmasi Penukaran**: Tinjau detailnya, termasuk nilai tukar dan jumlah pasti yang akan Anda terima. Klik **Konfirmasi Swap**.


![Confirm Swap](assets/en/18.webp)


4. **Pemrosesan**: Swap dieksekusi secara atomik pada Lightning Network. Anda akan melihat layar status yang mengindikasikan bahwa swap sedang menunggu.


![Swap Pending](assets/en/19.webp)


5. **Berhasil**: Setelah HTLC diselesaikan, swap selesai, dan aset berada di saluran Anda.


![Swap Success](assets/en/20.webp)



## Pengembang API


Untuk pengembang yang membangun di atas KaleidoSwap, aplikasi ini memperlihatkan API yang mendukung:



- RGB LSPS1**: Untuk layanan likuiditas otomatis.
- Tukar API**: Untuk perdagangan terprogram dan pembuatan pasar.
- WebSocket**: Untuk langganan data pasar real-time.


Lihat [Dokumentasi API] (https://docs.kaleidoswap.com/api/introduction) untuk titik akhir dan spesifikasi lengkap.


## Kesimpulan


KaleidoSwap memberdayakan Anda untuk memanfaatkan privasi dan skalabilitas aset RGB pada Lightning Network. Dengan memahami UTXO Berwarna dan alokasi aset saluran, Anda dapat sepenuhnya memanfaatkan protokol pertukaran terdesentralisasi yang kuat ini.