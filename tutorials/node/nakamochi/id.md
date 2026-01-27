---
name: Nakamochi
description: Menjalankan Node Jadi Mudah - Cara mengonfigurasi dan menggunakan node Nakamochi Bitcoin dan Lightning.
---
![image](assets/cover.webp)

Menjalankan node penuh Bitcoin dan Lightning kamu sendiri sekarang nggak lagi jadi tugas rumit yang cuma bisa dilakukan para ahli teknis. Secara tradisional, menyiapkan dan mengelola node butuh pengetahuan yang dalam soal kriptografi, jaringan, dan pengembangan perangkat lunak. Nakamochi mengubah itu dengan membuat node jadi bisa diakses semua orang, tanpa peduli latar belakang teknisnya.

Dengan Nakamochi, siapa pun bisa mengatur dan mengoperasikan sebuah node dari rumah, yang bikin kamu punya privasi penuh dan kemandirian finansial. Menjalankan node penuh bukan cuma mengamankan transaksi kamu sendiri, tapi juga ikut memperkuat jaringan Bitcoin. Jaringan Bitcoin yang terdesentralisasi dan tangguh bergantung pada distribusi node yang luas untuk menjaga keamanan dan kemandiriannya.

### Daftar Isi


- Apa itu Nakamochi dan Bagaimana Cara Kerjanya?
- Menyiapkan Nakamochi
- Tentang Jaringan Lightning
- Membuka Saluran dan Melakukan Transaksi di Jaringan Lightning

## Apa itu Nakamochi dan Bagaimana Cara Kerjanya?

Nakamochi adalah node penuh khusus Bitcoin yang mendukung jaringan Bitcoin dan Lightning. Perangkat ini sudah termasuk dompet Bitcoin dan Lightning yang terintegrasi, yang memungkinkan kamu menjalankan node Bitcoin kamu sendiri dengan aman dan berdaulat sambil tetap menikmati kecepatan Lightning Network dan biaya transaksi yang rendah.

Node Nakamochi kamu dikelola melalui aplikasi seluler, [BitBanana (Android)](https://bitbanana.app) dan [Zeus (iOS)](https://bitbanana.app), yang memungkinkan Anda untuk mengontrolnya dengan nyaman dari mana saja. Aplikasi-aplikasi ini bertindak sebagai kendali jarak jauh untuk node Anda, memungkinkan Anda untuk membayar secara langsung dengan Bitcoin atau Lightning, mengelola transaksi, membuka atau menutup saluran, memeriksa saldo, dan memantau kinerja node Anda, semuanya dengan mudah.

## Menyiapkan Nakamochi hanya membutuhkan waktu 5 menit

### Langkah 1: Hubungkan dan Mulai

1. Hubungkan Nakamochi ke listrik dan Wi-Fi.

2. Klik **"Siapkan Dompet Baru "** dan simpan frasa pemulihan 24 kata Anda dengan aman.

3. Gunakan aplikasi manajemen node (Zeus atau BitBanana) untuk menyambungkan ke Nakamochi:

4. Buka aplikasi dan pindai kode QR yang ditampilkan pada Nakamochi.

5. Untuk keamanan tambahan, tetapkan kode PIN pada perangkat kamu.

![image](assets/en/01.webp)

_Hubungkan ke listrik dan tulis seedphrase 24 kata Anda_

![image](assets/en/02.webp)

_Tunggu sampai Blockchain menyusul_

![image](assets/en/03.webp)

_Siapkan dompet baru di Tab Lightning_

![image](assets/en/04.webp)

_Pindai Kode QR dengan Aplikasi Manajemen Node_

![image](assets/en/05.webp)

_Untuk keamanan tambahan, atur kode PIN_

**Catatan:** _Izinkan node Nakamochi kamu untuk sinkron dengan blockchain. Proses ini mungkin memerlukan waktu tergantung pada koneksi internet Anda._

## Tentang Jaringan Lightning

https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Bitcoin Lightning Network merevolusi transaksi Bitcoin dengan bikin semuanya lebih cepat, lebih murah, dan lebih efisien. Jaringan ini cocok untuk penggunaan sehari-hari karena memungkinkan pembayaran hampir instan dengan biaya yang sangat rendah, ideal untuk transaksi mikro seperti beli kopi atau pembelian kecil yang sering kamu lakukan.

Dengan beroperasi secara off-chain, Lightning didesain untuk bisa diskalakan, mendukung ribuan transaksi per detik tanpa membebani blockchain utama Bitcoin. Ini menjadikannya pemain penting dalam perkembangan Bitcoin sebagai sistem pembayaran global yang praktis.

Privasi juga jadi keuntungan besar, karena transaksi di Lightning lewat channel pembayaran pribadi, bukan dicatat langsung di blockchain. Cara ini bikin transaksi lebih tertutup sambil tetap mempertahankan keamanan kuat dari Bitcoin.

#### Penjelasan Saluran Pembayaran

Lightning Network beroperasi lewat channel pembayaran, yaitu koneksi antara dua pihak yang memungkinkan banyak transaksi tanpa harus berinteraksi langsung dengan blockchain. Saat sebuah channel dibuka, saldo antara kedua pihak diperbarui di solusi Lightning layer dua ini untuk setiap transaksi, memastikan pembayaran yang cepat dan berbiaya rendah. Hanya pembukaan dan penutupan channel yang dicatat on-chain, sehingga mengurangi kemacetan di blockchain Bitcoin. Desain ini memastikan skalabilitas dan privasi karena transaksi individual tetap tidak tercatat di buku besar publik.

**Contoh:** Alice dan Bob membuka sebuah channel dengan mengirimkan Bitcoin ke channel tersebut. Alice mengirim Bitcoin ke Bob, dan saldo off-chain mereka langsung diperbarui tanpa catatan on-chain. Kalau Alice kemudian membayar Charlie dan Alice tidak punya channel langsung ke Charlie, pembayaran bisa dialihkan lewat channel Bob untuk mencapai Charlie. Perutean lewat node perantara memastikan pembayaran tetap bisa dilakukan tanpa koneksi langsung, yang bikin jaringan jadi sangat efisien.

## Membuka Saluran dan Melakukan Transaksi di Jaringan Lightning

Setelah Nakamochi kamu selesai diatur dan terhubung ke aplikasi manajemen node, kamu bisa mulai memakai Lightning Network dengan membuka channel dan melakukan transaksi.

### Membuka Saluran di Zeus (iOS):

1. Buka tab **"Saluran "** (menu bagian bawah).

2. Klik tanda **"+"** untuk membuka saluran baru.

3. Pindai atau masukkan pubkey node yang ingin kamu sambungkan.

4. Masukkan jumlah yang dikunci (pilih dengan rekan kamu atau gunakan jumlah tetap minimum untuk node yang terkenal).

5. Klik **"Buka Saluran "**.

![image](assets/en/06.webp)

tangkapan Layar _ZEUS_

Untuk informasi lebih lanjut: [Saluran | Dokumentasi Zeus](https://docs.zeusln.app/)

### Membuka Saluran di BitBanana (Android):

1. Buka menu hamburger (kiri).

2. Buka **"Saluran "**.

3. Klik tanda **"+"** untuk menambah/membuka saluran baru.

4. Pindai atau tempelkan pubkey.

5. Masukkan jumlah yang dikunci (pilih dengan rekan Anda atau gunakan jumlah tetap minimum untuk node yang terkenal).

![image](assets/en/07.webp)

tangkapan Layar Bitbanana

Untuk informasi lebih lanjut: [BitBanana](https://bitbanana.com)

Setelah channel kamu terbuka, pembayaran bisa disalurkan lewat channel itu ke peserta lain di jaringan. Saldo akan menyesuaikan secara off-chain, jadi transaksi hampir instan dan biayanya sangat kecil.

Kalau kamu sudah nggak butuh sebuah channel, kamu bisa menutupnya. Tindakan ini akan menyelesaikan saldo akhir antara kamu dan peer kamu lalu mencatatnya on-chain. Idealnya, kedua pihak setuju dan sama-sama online untuk melakukan cooperative close yang lebih cepat dan lebih murah dibanding force close dengan peer yang nggak responsif atau offline.

Secara umum, kami menyarankan untuk membiarkan channel tetap terbuka supaya biaya lebih rendah dan keandalan serta efisiensi jaringan tetap tinggi. Dengan membiarkan channel tetap terbuka, kamu bisa meminimalkan biaya transaksi on-chain, menghindari downtime untuk membuka ulang channel, dan mempertahankan kapasitas routing yang stabil untuk pemrosesan pembayaran yang lancar. Pendekatan ini bikin jaringan lebih kuat dan tangguh sekaligus meningkatkan pengalaman pengguna dan menurunkan biaya operasional.

### Tautan Berguna


- [Tentang Nakamochi](https://nakamochi.io/)
- [Berlangganan Buletin Nakamochi](https://90c7addc.sibforms.com/serve/MUIFAHG7H5YBPpm-kZ8G6TuS-nmL4uaq85rlpBfI__S79tZ5jheIJfF3kJYudycgs_6_RUdDBkt8Sd7OyNL_JDTTJvOb36ifF6vcQoabBXKp4cbefzh1DYqnok_jItexICcQL13ucd2aS581ngqy7jr0Q1H3HhxV3z2eWKE5-Z-YMasj-MMotQeDvdorMCSi0XgCWDqs8rEMQC7E)
