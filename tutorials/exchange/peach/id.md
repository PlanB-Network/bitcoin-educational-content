---
name: Peach
description: Panduan lengkap untuk menggunakan Peach dan menukar bitcoin P2P
---
![cover](assets/cover.webp)

![peach](https://youtu.be/ziwhv9KqVkM)

## Pendahuluan

Pertukaran peer-to-peer (P2P) yang bebas KYC sangat penting untuk menjaga kerahasiaan dan otonomi keuangan pengguna. Bursa ini memungkinkan transaksi langsung antar individu tanpa memerlukan verifikasi identitas, yang sangat penting bagi mereka yang menghargai privasi. Untuk pemahaman yang lebih mendalam mengenai konsep teoretis, lihatlah kursus BTC204:

https://planb.network/courses/btc204
### 1. Apa itu Peach?

Peach adalah platform pertukaran P2P yang memungkinkan pengguna untuk membeli dan menjual bitcoin tanpa KYC. Ini menawarkan antarmuka yang intuitif dan fitur keamanan tingkat lanjut. Dibandingkan dengan solusi lain seperti Bisq, HodlHodl, dan Robosat, Peach menonjol karena kemudahan penggunaan dan biaya yang rendah.

### 2. Privasi dan Pengumpulan Data

**Informasi apa yang dikumpulkan oleh Peach?

Peach berusaha untuk menyimpan data seminimal mungkin tentang para penggunanya. Berikut ini adalah ikhtisar data yang disimpan di servernya:


- Hash dari pengidentifikasi aplikasi unik Anda (AdID)
- Hash dari data pembayaran Anda
- Percakapan terenkripsi Anda
- Data transaksi untuk memastikan bahwa pengguna anonim tidak melebihi batas perdagangan (jenis metode pembayaran yang digunakan, jumlah pembelian dan penjualan)
- Alamat yang digunakan untuk mengirim dan menerima dari rekening escrow
- Data penggunaan (Firebase & Google Analytics), hanya dengan persetujuan Anda

Sebagai pengingat, hash adalah data yang tidak dapat dikenali, mirip dengan enkripsi. Data yang sama akan selalu menghasilkan hash yang sama, sehingga memungkinkan untuk mendeteksi duplikat tanpa mengetahui data aslinya.

*Untuk informasi lebih lanjut tentang hashing, Anda dapat mengikuti kursus ini:*

https://planb.network/courses/cyp201
**Siapa saja yang dapat melihat detail pembayaran saya?


- Hanya rekanan Anda yang dapat melihat detail pembayaran Anda
- Data ditransmisikan melalui server Peach tetapi sepenuhnya dienkripsi dari ujung ke ujung
- Jika terjadi perselisihan, detail pembayaran dan riwayat percakapan Anda akan terlihat oleh mediator Peach yang ditugaskan

## Instalasi dan konfigurasi

### 1. Instal aplikasi Peach

![Installation de Peach](assets/fr/01.webp)


- Unduh aplikasi dari [Peach Bitcoin] (https://peachbitcoin.com/fr/quick-start/).
- Ikuti petunjuk pemasangan pada perangkat Anda.
- Selama instalasi, Anda akan diminta untuk memilih apakah Anda ingin membagikan data tertentu untuk meningkatkan aplikasi Peach (gambar 1)
- Pada layar berikutnya (gambar 2), Anda memiliki dua opsi:
 - Jika Anda adalah pengguna baru, klik "Pengguna baru" untuk membuat profil baru
 - Jika Anda sudah memiliki akun, gunakan "Pulihkan" untuk memulihkan profil Anda yang sudah ada
- Jika Anda memiliki kode referral, Anda dapat memasukkannya di sini.
- Untuk memulihkan akun yang sudah ada (gambar 3), Anda memerlukan :
 - File cadangan Anda
 - Kata sandi untuk mendekripsi file ini

### 2. Gambaran Umum Layar Utama

Aplikasi Peach diatur di sekitar empat layar utama yang dapat diakses dari bilah navigasi bawah:

![Navigation dans l'application](assets/fr/02.webp)


- Beranda** : Layar utama untuk membeli dan menjual bitcoin. Di sinilah Anda dapat membuat transaksi baru dan mengakses penawaran yang tersedia.
- Dompet**: Dompet bitcoin terintegrasi Anda yang memungkinkan Anda untuk :
 - Periksa saldo Anda
 - Menerima bitcoin
 - Kirim bitcoin
 - Melihat riwayat transaksi Anda
- Perdagangan** : Pusat manajemen perdagangan Anda di mana Anda akan menemukan:
 - Transaksi Anda saat ini
 - Riwayat lengkap bursa Anda
 - Status setiap transaksi
- Pengaturan** : Pusat konfigurasi akun Anda untuk :
 - Mengelola metode pembayaran Anda
 - Konfigurasikan cadangan Anda
 - Menyesuaikan preferensi Anda
 - Akses ke bantuan dan dukungan

### 3. Mengonfigurasi metode pembayaran Anda

![Accès aux paramètres de paiement](assets/fr/03.webp)

Mengakses metode pembayaran melalui tab Pengaturan (gambar 8)

**Pembayaran online

![Configuration des paiements en ligne](assets/fr/04.webp)


- Klik tombol untuk menambahkan metode pembayaran baru
- Pilih mata uang Anda
- Pilih metode pembayaran pilihan Anda

*Jenis metode pembayaran yang tersedia:*

***Transfer bank tersedia: ***


- SEPA (standar atau instan)
- Isi detail bank SEPA Anda

***Dompet online diterima :***


- Beberapa opsi tersedia tergantung pada negara Anda (Revolut, Paypal, Wise, Strike, dll.)
- Ikuti petunjuk untuk menambahkan detail login Anda

***Kartu hadiah yang dapat digunakan :***


- Amazon
- Masukkan negara penerbit kartu dan informasi lain yang diperlukan

***Opsi pembayaran nasional:***

Sistem pembayaran khusus negara :


- Satispay (Italia)
- MB Way (Portugal)
- Bizum (Spanyol)
- Pembayaran Lebih Cepat (Inggris)

***Pembayaran secara langsung:***

![Configuration des paiements en personne](assets/fr/05.webp)


- Pilih "Pertemuan
- Kemudian pilih pertemuan Anda dari daftar

### Petunjuk penggunaan


- Anda dapat mengatur beberapa metode pembayaran secara bersamaan
- Semakin banyak metode yang Anda tambahkan, semakin luas jangkauan penawaran yang dapat Anda akses
- Harap periksa apakah informasi Anda sudah benar sebelum mendaftar
- Anda dapat mengubah atau menghapus metode pembayaran Anda kapan saja

**Catatan keamanan**: Informasi pembayaran Anda dienkripsi dan hanya dibagikan dengan mitra bursa Anda selama transaksi.

### 4. Cara mengamankan portofolio Anda

**Memahami akun Peach Anda

Akun Peach bukanlah akun login dan kata sandi tradisional. Akun ini adalah sebuah file yang disimpan secara lokal di ponsel Anda, yang berarti Peach tidak perlu menyimpan data Anda atau mengetahui identitas Anda: Anda yang memegang kendali. File ini berisi semua data Anda, mulai dari kunci dompet bitcoin hingga detail pembayaran.

Pendekatan ini menjamin kerahasiaan yang lebih besar, tetapi juga menyiratkan tanggung jawab yang lebih besar. Kehilangan ponsel tanpa cadangan berarti kehilangan akses ke akun dan dana Peach. Jadi, sangat penting untuk mencadangkan file ini dan melindunginya dengan kata sandi yang kuat.

**Buat cadangan Anda**

![Accéder aux sauvegardes](assets/fr/13.webp)


- Mengakses pengaturan dari tab di kanan bawah layar beranda
- Pilih opsi "cadangan" di menu pengaturan

![Processus de sauvegarde](assets/fr/06.webp)

Tersedia dua jenis cadangan yang tersedia:

**Simpan file akun (gambar 14)**


- Klik "Buat cadangan baru"
- Buat kata sandi yang kuat untuk mengenkripsi file cadangan Anda
- Simpan file ini di tempat yang aman

Cadangan file memulihkan akun Peach Anda secara lengkap, termasuk file :


- Portofolio Anda
- Metode pembayaran Anda
- Riwayat percakapan
- Data pembayaran
- Riwayat transaksi dengan detail rekanan

**Menyimpan frasa pemulihan (gambar 15)**


- Ikuti petunjuk untuk menampilkan frasa pemulihan Anda
- Tuliskan kata-kata dengan hati-hati dalam urutan yang benar
- Simpan cadangan ini di lokasi yang aman, idealnya berbeda dari file akun

Frasa pemulihan hanya memulihkan :


- Akses ke akun Anda
- Dana bitcoin Anda

Anda akan kalah :


- Riwayat percakapan
- Data pembayaran
- Informasi mitra pengimbang dalam riwayat transaksi

Untuk keamanan optimal, kami sarankan Anda melakukan kedua jenis pencadangan.

## Membeli dan Menjual Bitcoin

### 1. Cara membeli Bitcoin

![Création et vue des offres](assets/fr/07.webp)


- Pada layar beranda, klik tombol "Beli" (gambar 16)
- Konfigurasikan pembelian Anda sesuai dengan preferensi Anda (gambar 17)
- Jelajahi daftar penawaran yang tersedia (gambar 18)

![Sélection et confirmation d'achat](assets/fr/08.webp)


- Pilih penawaran yang tepat untuk Anda (gambar 19)
- Melakukan pembayaran dengan metode yang telah disepakati
- Konfirmasikan pembayaran dalam aplikasi dan evaluasi transaksi (gambar 20)

![Réception des bitcoins](assets/fr/09.webp)


- Melacak status transaksi Anda
- Periksa konfirmasi penerimaan bitcoin
- Dana akan tersedia dalam portofolio Peach Anda

### 2. Cara menjual Bitcoin

![Création d'un ordre de vente](assets/fr/10.webp)


- Konfigurasikan penawaran penjualan Anda (gambar 24)
- Membiayai transaksi dengan mengirimkan bitcoin ke alamat yang disediakan (gambar 25)
- Tunggu konfirmasi transaksi (gambar 26)
- Penawaran Anda sekarang dapat dilihat oleh pembeli (gambar 27)

![Attente du paiement](assets/fr/11.webp)


- Memantau status penawaran Anda
- Tunggu konfirmasi pembayaran dari pembeli
- Memeriksa detail transaksi

![Finalisation de la vente](assets/fr/12.webp)


- Memeriksa status pembayaran
- Konfirmasikan tanda terima pembayaran
- Mengevaluasi transaksi
- Bitcoin secara otomatis dilepaskan kepada pembeli

**Kiat agar transaksi berhasil**


- Menanggapi pesan dari rekanan Anda dengan cepat
- Periksa detail pembayaran dengan cermat
- Jangan ragu untuk menggunakan layanan mediasi jika Anda memiliki masalah

**Catatan keamanan**: Jangan pernah mengonfirmasi penerimaan pembayaran hingga Anda memverifikasi bahwa pembayaran tersebut telah diterima di akun Anda.

## Keuntungan dan kerugian

### Manfaat persik


- Tidak memerlukan KYC**: Menjaga kerahasiaan pengguna.
- Tidak ada akses ke detail bank**: Peach tidak memiliki akses ke detail bank atau identitas Anda.
- Antarmuka yang intuitif**: Mudah digunakan untuk pengguna tingkat menengah.
- Sumber Terbuka**: Kode sumber bersifat publik dan dapat diverifikasi oleh komunitas.

### Kerugian persik


- Likuiditas terbatas**: Volume perdagangan lebih sedikit dibandingkan platform yang lebih mapan.
- Risiko regulasi** : Aplikasi ini dikelola oleh perusahaan Swiss. Oleh karena itu, aplikasi ini tunduk pada peraturan Swiss, yang dapat berkembang dan berpotensi menyensor aplikasi.

## Sumber daya yang berguna


- Video penjelasan bahasa Prancis: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Panduan memulai dengan cepat: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)