---
name: Nakamochi
description: Menjalankan Node Menjadi Mudah - Cara mengatur dan menggunakan Nakamochi Bitcoin dan Lightning node.
---
Menjalankan node penuh Bitcoin dan Lightning Anda sendiri tidak perlu lagi menjadi tugas yang rumit dan hanya dapat dilakukan oleh para ahli teknis. Secara tradisional, menyiapkan dan mengelola node membutuhkan pengetahuan yang mendalam mengenai kriptografi, jaringan, dan pengembangan perangkat lunak. Nakamochi mengubah hal tersebut dengan membuat node dapat diakses oleh semua orang, terlepas dari latar belakang teknisnya.

Dengan Nakamochi, siapa pun dapat mengatur dan mengoperasikan sebuah node dari rumah, sehingga memungkinkan privasi penuh dan kemandirian finansial. Menjalankan sebuah node penuh tidak hanya mengamankan transaksi Anda sendiri, tetapi juga berkontribusi pada kekuatan jaringan Bitcoin. Jaringan Bitcoin yang terdesentralisasi dan tangguh bergantung pada distribusi node yang luas untuk memastikan keamanan dan kemandiriannya.

### Daftar Isi


- Apa itu Nakamochi dan Bagaimana Cara Kerjanya?
- Menyiapkan Nakamochi
- Tentang Jaringan Lightning
- Membuka Saluran dan Melakukan Transaksi di Jaringan Lightning

## Apa itu Nakamochi dan Bagaimana Cara Kerjanya?

Nakamochi adalah sebuah node penuh khusus Bitcoin yang mendukung jaringan Bitcoin dan Lightning. Ini termasuk dompet Bitcoin dan Lightning yang terintegrasi, memungkinkan pengguna untuk menjalankan simpul Bitcoin yang aman dan berdaulat sendiri sambil mendapatkan keuntungan dari kecepatan Jaringan Lightning dan biaya transaksi yang rendah.

Node Nakamochi Anda dikelola melalui aplikasi seluler, [BitBanana (Android)] (https://bitbanana.app) dan [Zeus (iOS)] (https://bitbanana.app), yang memungkinkan Anda untuk mengontrolnya dengan nyaman dari mana saja. Aplikasi-aplikasi ini bertindak sebagai kendali jarak jauh untuk node Anda, memungkinkan Anda untuk membayar secara langsung dengan Bitcoin atau Lightning, mengelola transaksi, membuka atau menutup saluran, memeriksa saldo, dan memantau kinerja node Anda, semuanya dengan mudah.

## Menyiapkan Nakamochi hanya membutuhkan waktu 5 menit

### Langkah 1: Hubungkan dan Mulai

1. Hubungkan Nakamochi ke daya dan Wi-Fi.

2. Klik **"Siapkan Dompet Baru "** dan simpan frasa pemulihan 24 kata Anda dengan aman.

3. Gunakan aplikasi manajemen node (Zeus atau BitBanana) untuk menyambungkan ke Nakamochi Anda:

4. Buka aplikasi dan pindai kode QR yang ditampilkan pada Nakamochi Anda.

5. Untuk keamanan tambahan, tetapkan kode PIN pada perangkat Anda.

![image](assets/en/01.webp)

hubungkan ke daya dan tuliskan frasa benih 24 kata Anda_

![image](assets/en/02.webp)

tunggu sampai Blockchain berhasil mengejar ketertinggalannya

![image](assets/en/03.webp)

mengatur dompet baru di Tab Lightning_

![image](assets/en/04.webp)

pindai Kode QR dengan Aplikasi Manajemen Node_

![image](asset/en/05.webp)

untuk keamanan tambahan, tetapkan kode PIN_

**Catatan:** _Izinkan node Nakamochi Anda untuk melakukan sinkronisasi dengan blockchain. Proses ini mungkin membutuhkan waktu, tergantung pada koneksi internet Anda._

## Tentang Jaringan Lightning

Bitcoin Lightning Network merevolusi transaksi Bitcoin dengan membuatnya lebih cepat, lebih murah, dan lebih efisien. Ini sempurna untuk penggunaan sehari-hari, memungkinkan pembayaran hampir instan dengan biaya minimal, ideal untuk transaksi mikro seperti membeli kopi atau menangani pembelian kecil yang sering dilakukan.

Dengan beroperasi secara off-chain, Lightning didesain untuk meningkatkan skala, mendukung ribuan transaksi per detik tanpa membebani blockchain utama Bitcoin. Hal ini menjadikannya pemain kunci dalam evolusi Bitcoin menjadi sistem pembayaran global yang praktis.

Privasi adalah keuntungan lainnya, karena transaksi di Lightning disalurkan melalui saluran pembayaran pribadi dan bukannya dicatat secara langsung di blockchain. Hal ini memastikan cara yang lebih rahasia untuk bertransaksi dengan tetap menjaga keamanan Bitcoin yang kuat.

#### Penjelasan Saluran Pembayaran

Lightning Network beroperasi melalui saluran pembayaran, yang merupakan koneksi antara dua pihak yang memungkinkan banyak transaksi tanpa berinteraksi langsung dengan blockchain. Ketika sebuah saluran terbuka, saldo antara kedua belah pihak diperbarui pada solusi Lightning lapisan kedua ini untuk setiap transaksi, memastikan pembayaran yang cepat dan berbiaya rendah. Hanya pembukaan dan penutupan saluran yang dicatat secara on-chain, sehingga mengurangi kemacetan pada blockchain Bitcoin, desain ini memastikan skalabilitas dan privasi, karena transaksi individu tetap tidak tercatat pada buku besar publik.

**Contoh:** Alice dan Bob membuka sebuah saluran dengan mengirimkan Bitcoin ke saluran tersebut. Alice mengirimkan Bitcoin ke Bob, dan saldo off-chain mereka langsung diperbarui tanpa catatan on-chain. Jika Alice kemudian membayar Charlie, dan Alice tidak memiliki saluran langsung ke Charlie, pembayaran dapat dialihkan melalui saluran Bob untuk mencapai Charlie. Perutean melalui node perantara memastikan pembayaran bahkan tanpa koneksi langsung, membuat jaringan menjadi sangat efisien.

## Membuka Saluran dan Melakukan Transaksi di Jaringan Lightning

Setelah Nakamochi Anda diatur dan terhubung ke aplikasi manajemen node, Anda dapat mulai menggunakan Lightning Network dengan membuka saluran dan melakukan transaksi.

### Membuka Saluran di Zeus (iOS):

1. Buka tab **"Saluran "** (menu bagian bawah).

2. Klik tanda **"+"** untuk membuka saluran baru.

3. Pindai atau masukkan pubkey node yang ingin Anda sambungkan.

4. Masukkan jumlah yang dikunci (pilih dengan rekan Anda atau gunakan jumlah tetap minimum untuk node yang terkenal).

5. Klik **"Buka Saluran "**.

![image](asset/en/06.webp)

tangkapan Layar _ZEUS_

Untuk informasi lebih lanjut: [Saluran | Dokumentasi Zeus](https://docs.zeusln.app/)

### Membuka Saluran di BitBanana (Android):

1. Buka menu hamburger (kiri).

2. Buka **"Saluran "**.

3. Klik tanda **"+"** untuk menambah/membuka saluran baru.

4. Pindai atau tempelkan pubkey.

5. Masukkan jumlah yang dikunci (pilih dengan rekan Anda atau gunakan jumlah tetap minimum untuk node yang terkenal).

![image](asset/en/07.webp)

tangkapan Layar Bitbanana

Untuk informasi lebih lanjut: [BitBanana](https://bitbanana.com)

Setelah saluran Anda terbuka, pembayaran dapat disalurkan melalui saluran tersebut ke peserta lain dalam jaringan. Saldo menyesuaikan secara off-chain, memastikan transaksi hampir instan dan dikenakan biaya minimal.

Jika Anda tidak lagi membutuhkan sebuah channel, Anda dapat menutupnya. Tindakan ini akan menyelesaikan saldo akhir antara Anda dan peer Anda dan mencatatnya secara on-chain. Idealnya, kedua belah pihak setuju dan online untuk "penutupan kooperatif" (lebih cepat dan lebih sedikit biaya vs "penutupan paksa" dengan peer yang tidak responsif/offline).

Secara umum, kami menyarankan untuk membiarkan saluran tetap terbuka untuk mengurangi biaya dan meningkatkan keandalan dan efisiensi jaringan. Dengan membiarkan saluran tetap terbuka, Anda dapat meminimalkan biaya transaksi on-chain, menghindari waktu henti untuk penyambungan kembali saluran, dan mempertahankan kapasitas perutean yang stabil untuk pemrosesan pembayaran yang lancar. Pendekatan ini mendorong jaringan yang kuat dan tangguh sekaligus meningkatkan pengalaman pengguna secara keseluruhan dan mengurangi biaya operasional.

### Tautan Berguna


- [Tentang Nakamochi](https://nakamochi.io/)
- [Berlangganan Buletin Nakamochi](https://90c7addc.sibforms.com/serve/MUIFAHG7H5YBPpm-kZ8G6TuS-nmL4uaq85rlpBfI__S79tZ5jheIJfF3kJYudycgs_6_RUdDBkt8Sd7OyNL_JDTTJvOb36ifF6vcQoabBXKp4cbefzh1DYqnok_jItexICcQL13ucd2aS581ngqy7jr0Q1H3HhxV3z2eWKE5-Z-YMasj-MMotQeDvdorMCSi0XgCWDqs8rEMQC7E)