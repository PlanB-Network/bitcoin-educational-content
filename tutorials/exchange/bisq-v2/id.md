---
name: Bisq 2
description: Panduan lengkap untuk menggunakan Bisq 2 dan menukar bitcoin P2P
---
![cover](assets/cover.webp)

## Pendahuluan

Pertukaran peer-to-peer (P2P) yang bebas KYC sangat penting untuk menjaga kerahasiaan dan otonomi keuangan pengguna. Bursa ini memungkinkan transaksi langsung antar individu tanpa memerlukan verifikasi identitas, yang sangat penting bagi mereka yang menghargai privasi. Untuk pemahaman yang lebih mendalam mengenai konsep teoretis, lihatlah kursus BTC204:

https://planb.network/courses/btc204
### Apa itu Bisq 2?

Bisq 2 adalah versi baru dari bursa Bisq terdesentralisasi yang populer, yang diluncurkan pada tahun 2024. Tidak seperti pendahulunya, Bisq 2 telah dikembangkan untuk mendukung berbagai protokol bursa, menawarkan fleksibilitas yang lebih besar kepada pengguna.

**Fitur-fitur utama yang baru:**


- Dukungan untuk beberapa jaringan privasi (Tor, I2P)
- Beberapa identitas untuk kerahasiaan yang lebih baik
- REST API untuk bot perdagangan
- Dukungan untuk beberapa jenis portofolio
- Sistem peran dengan setoran wajib di BSQ

Panduan ini berfokus secara eksklusif pada "Bisq Easy", satu-satunya protokol yang tersedia saat ini. Bisq Easy telah dirancang khusus untuk pengguna baru Bitcoin. Protokol ini memungkinkan pengguna untuk membeli dan menjual Bitcoin dengan mata uang fiat pada platform peer-to-peer yang terdesentralisasi. Transaksi dibatasi hingga setara dengan 600 USD (dengan minimal 6 USD), dan keamanan pertukaran bergantung pada reputasi penjual BTC. Bisq Easy tidak memiliki biaya perdagangan atau persyaratan uang jaminan. Bisq Easy diharapkan dapat menggantikan Bisq 1 untuk pertukaran uang tunai di bawah 600 USD (atau setara).

**Fitur utama:**


- Aplikasi desktop lintas platform
- Beberapa protokol pertukaran yang tersedia
- Jaringan P2P terdesentralisasi
- Fokus pada kerahasiaan (tidak ada KYC, penggunaan Tor)
- Non-kustodian (Anda tetap memegang kendali atas dana Anda)
- Sumber terbuka (AGPL)

### Perbedaan dengan Bisq 1

**Untuk pembeli:**


- Tidak diperlukan uang jaminan
- Tidak ada biaya perdagangan
- Tidak ada biaya penambangan
- Keamanan berdasarkan reputasi vendor
- Batas perdagangan yang lebih rendah (setara dengan USD 600)

**Untuk penjual:**


- Tidak diperlukan uang jaminan
- Membangun reputasi
- Kemungkinan membakar BSQ atau membuat obligasi BSQ
- Potensi premi penjualan yang lebih tinggi (10-15% di atas pasar)

**Catatan penting:** Setelah protokol Bisq Multisig diimplementasikan di Bisq 2, versi lama Bisq dapat dihapuskan. Akan tetapi, Bisq 1 akan terus digunakan sebagai alat manajemen untuk Bisq CAD dan pertukaran BSQ-BTC.

### Proses pertukaran


- Pembuat penawaran menentukan ketentuan pertukaran
- Setelah para pedagang menyetujui persyaratan (metode pembayaran dan harga), pertukaran dimulai
- Penjual mengirimkan detail banknya kepada pembeli, dan pembeli mengirimkan alamat Bitcoin-nya kepada penjual
- Pembeli melakukan pembayaran secara tunai dan memberi tahu penjual
- Setelah pembayaran diterima, penjual mengirim bitcoin ke alamat pembeli
- Pertukaran selesai ketika pembeli menerima bitcoin

### Aturan penting


- Sebelum menukar detail pembayaran, pertukaran dapat dibatalkan tanpa alasan
- Setelah rincian telah dipertukarkan, kegagalan untuk memenuhi kewajiban dapat mengakibatkan pengusiran
- Untuk transfer bank, **jangan pernah menggunakan istilah "Bisq" atau "Bitcoin "** dalam alasan pembayaran (ini dapat menyebabkan dana dibekukan atau bahkan menyebabkan rekening bank penerima atau pembayar diblokir)
- Trader harus login setidaknya sekali sehari untuk mengikuti proses ini
- Jika terjadi masalah, trader dapat meminta bantuan mediator

## Instalasi dan konfigurasi

### 1. Unduh dan Verifikasi Bisq 2

![Téléchargement de Bisq 2](assets/fr/01.webp)


- Buka [bisq.network](https://bisq.network/downloads/)
- Unduh versi Bisq 2 yang sesuai dengan sistem operasi Anda (gulir ke bawah halaman)
- Verifikasi keaslian file yang diunduh (sangat disarankan). Untuk panduan terperinci tentang verifikasi tanda tangan, lihat tutorial berikut:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
### 2. Pemasangan sesuai dengan sistem Anda

Ikuti langkah-langkah instalasi yang sesuai untuk sistem operasi Anda. Jika Anda mengalami kesulitan selama instalasi, Anda dapat membaca panduan terperinci di [wiki resmi Bisq](https://bisq.wiki/Downloading_and_installing).

### 3. Start-up pertama


- Luncurkan Bisq 2 dan terima persyaratan penggunaan

![Conditions d'utilisation](assets/fr/01.webp)


- Buat profil baru dengan memilih nama dan avatar

![Création du profil](assets/fr/02.webp)


- Anda kemudian dibawa ke dasbor utama aplikasi, di mana Anda dapat meluncurkan Bisq Easy untuk membeli atau menjual bitcoin pertama Anda

![Page d'accueil de Bisq 2](assets/fr/03.webp)

### 4. Menyiapkan metode pembayaran


- Akses bagian akun pembayaran dari menu utama

![Liste des comptes de paiement](assets/fr/04.webp)


- Tambahkan metode pembayaran baru dengan mengisi informasi yang diperlukan

![Création d'un nouveau compte de paiement](assets/fr/05.webp)

Pra-konfigurasi metode pembayaran bersifat opsional, tetapi disarankan untuk menghemat waktu saat bertransaksi. Anda juga bisa mengonfigurasi metode pembayaran secara langsung saat jual beli dengan menghubungi mitra bursa.

### 5. Keamanan akun

**Pencadangan data:**

Tidak seperti Bisq 1, Bisq 2 saat ini tidak mengintegrasikan dompet Bitcoin: oleh karena itu, transaksi dilakukan melalui dompet eksternal Anda sendiri. Namun demikian, kami menyarankan anda untuk membuat cadangan folder data Bisq 2 anda secara teratur. Untuk menemukan folder data Anda, lihatlah [wiki resmi Bisq](https://bisq.wiki/Backing_up_application_data#Back_up_the_entire_Bisq_data_directory).

**Manajemen identitas:**

Bisq 2 memungkinkan Anda membuat beberapa identitas. Setiap identitas dapat digunakan untuk berbagai jenis transaksi. Identitas Anda disimpan dalam folder data.

## Membeli dan Menjual Bitcoin

### Cara membeli Bitcoin

**Opsi 1: Manfaatkan penawaran yang sudah ada**


- Di layar utama, pilih "Bisq Easy", tab "Memulai", lalu klik "Mulai wizard perdagangan"

![Lancer trade wizard](assets/fr/06.webp)


- Pilih "Beli Bitcoin" dan pilih mata uang Anda

![Sélection achat Bitcoin](assets/fr/07.webp)

![Choix de la devise](assets/fr/08.webp)


- Siapkan metode pembayaran pilihan Anda (SEPA, Revolut, dll.)

![Configuration méthodes de paiement](assets/fr/09.webp)


- Pada titik ini, Anda memiliki daftar penawaran yang sesuai dengan kriteria Anda sebelumnya, atau Anda perlu membuka "Buku Penawaran"

![Liste des offres](assets/fr/10.webp)


- Dalam kasus kedua, Anda dapat menampilkan dan memfilter penawaran menggunakan tombol di kanan atas antarmuka

![Filtres des offres](assets/fr/11.webp)


- Setelah Anda memilih penawaran, Anda tinggal memilih metode pembayaran, lalu memvalidasi ringkasan jual beli

![Choix modalités de paiement](assets/fr/12.webp)

![Configuration du trade](assets/fr/13.webp)

![Récapitulatif du trade](assets/fr/14.webp)

**Opsi 2: Buat penawaran Anda sendiri**


- Pilih "Bisq Easy" lalu "Offerbook"
- Pilih pasangan trading Anda (misalnya BTC/EUR)
- Klik "Buat penawaran
- Ikuti wizard pembuatan penawaran: Tentukan jumlah (tetap atau kisaran)

![Configuration du montant](assets/fr/20.webp)


- Pilih metode pembayaran yang diterima

![Sélection méthodes de paiement](assets/fr/21.webp)


  - Periksa ringkasan dan publikasikan penawaran

![Récapitulatif et publication](assets/fr/22.webp)

Setelah pertukaran dimulai :


- Kirim alamat Bitcoin atau faktur Lightning Anda ke penjual

![Envoi adresse Bitcoin](assets/fr/15.webp)


- Menerima detail bank penjual

![Réception coordonnées bancaires](assets/fr/16.webp)

![Détails coordonnées bancaires](assets/fr/17.webp)


- Lakukan pembayaran (tanpa menyebutkan "Bisq" atau "Bitcoin")
- Memberitahukan pembayaran Anda kepada penjual

![Notification paiement](assets/fr/18.webp)


- Tunggu hingga bitcoin tiba

![Attente réception](assets/fr/19.webp)

### Bagaimana cara menjual Bitcoin?

Proses penjualan di Bisq 2 mengikuti logika yang sama dengan proses pembelian, dengan langkah-langkah utama yang sama tetapi dalam urutan terbalik. Anda bisa membuat penawaran sendiri untuk menjual, atau merespons penawaran yang sudah ada untuk membeli. Berikut ini adalah rincian berbagai opsi dan tahapan dalam prosesnya:

**Opsi 1: Buat penawaran untuk menjual**


- Pilih "Bisq Easy" lalu "Offerbook"
- Klik "Buat penawaran" dan pilih "Jual Bitcoin"
- Konfigurasikan penawaran Anda :
 - Pilih mata uang (EUR, USD, dll.)
 - Pilih metode pembayaran yang diterima
 - Tetapkan jumlahnya (antara 6 hingga 600 USD)
 - Tetapkan harga Anda (tetap atau % dari pasar)
- Periksa detail dan publikasikan penawaran

**Opsi 2: Mengambil penawaran yang sudah ada**


- Jelajahi penawaran di tab "Buku Penawaran"
- Filter berdasarkan mata uang dan metode pembayaran
- Pilih penawaran yang sesuai untuk Anda
- Periksa detail dan terima penawaran

**Proses penjualan:**

Setelah pertukaran dimulai :


   - Kirim detail bank Anda ke pembeli
   - Tunggu alamat Bitcoin pembeli
   - Periksa apakah alamat tersebut valid

Setelah pemberitahuan pembayaran:


   - Periksa apakah pembayaran telah diterima di akun Anda
   - Konfirmasikan bahwa jumlah dan rinciannya sesuai
   - Kirim bitcoin ke alamat yang diberikan
   - Tandai transaksi sebagai selesai

Finalisasi :


   - Tunggu konfirmasi dari pembeli
   - Tinggalkan umpan balik tentang transaksi
   - Bangun reputasi Anda untuk penjualan di masa depan

**Catatan penting:** Sebagai penjual, Anda harus waspada terhadap risiko tolak bayar. Pilihlah metode pembayaran yang aman, dan selalu periksa apakah pembayaran sudah diterima sebelum mengirim bitcoin.

## Praktik yang Baik dan Keselamatan

### Kiat Keselamatan

**Untuk pembeli:**


- Mulailah dengan jumlah kecil
- Periksa reputasi penjual (skor minimum 30.000)
- Gunakan hanya metode pembayaran yang disarankan
- Pastikan penjual aktif sebelum mengirim pembayaran
- Gunakan hanya detail bank yang disediakan dalam obrolan pertukaran
- Jangan pernah berkomunikasi di luar platform Bisq 2
- Menyimpan bukti pembayaran
- Jangan pernah mengirim informasi sensitif

**Untuk penjual:**


- Berhati-hatilah dengan akun baru
- Hindari metode pembayaran yang sensitif terhadap tolak bayar (PayPal, Venmo)
- Periksa apakah detail akun sesuai dengan pembeli
- Batasi komunikasi untuk mengobrol Bisq 2
- Buka mediasi jika ada keraguan

### Membangun reputasi (untuk tenaga penjualan)

Untuk meningkatkan reputasi Anda di Bisq sebagai penjual, lakukan transaksi secara teratur dan pertahankan komunikasi profesional dengan pembeli. Tanggapi permintaan pembeli dengan cepat untuk memastikan pengalaman yang positif. Anda juga dapat membuat obligasi BSQ untuk menunjukkan komitmen Anda terhadap platform. Tindakan ini akan membangun kepercayaan dan menarik lebih banyak pembeli.

### Penyelesaian Sengketa


- Hubungi rekan Anda melalui obrolan
- Jika perlu, buka sengketa
- Berikan semua bukti yang diminta
- Ikuti instruksi mediator

### Kebijakan privasi :


- Tidak perlu registrasi atau verifikasi identitas terpusat
- Semua koneksi melalui jaringan Tor (dan segera I2P)
- Tidak ada server pusat untuk menyimpan data
- Detail transaksi hanya dapat dibaca oleh pihak-pihak yang terlibat

### Perlindungan terhadap penyensoran :


- Jaringan P2P yang terdistribusi sepenuhnya
- Menggunakan jaringan Tor (dan segera I2P) untuk menolak sensor
- Proyek sumber terbuka yang dikelola oleh DAO, tanpa badan hukum terpusat

## Keuntungan dan kerugian

### Manfaat Bisq 2


- Kerahasiaan maksimum**: Tanpa KYC, penggunaan Tor
- Desentralisasi**: Tidak ada server pusat
- Keamanan**: Sumber terbuka, kode non-kustodian
- Antarmuka yang intuitif**: lebih sederhana dari Bisq 1
- Fleksibilitas**: Beberapa protokol pertukaran

### Kekurangan Bisq 2


- Likuiditas terbatas** (untuk saat ini):
 - Protokol baru dalam tahap permulaan
 - Beberapa penawaran penjualan yang tersedia
 - Waktu tunggu yang berpotensi lama untuk menemukan pembeli
- Batas perdagangan**: Maksimum USD 600 per transaksi (dengan Bisq easy)
- Hanya untuk desktop**: Tidak ada aplikasi seluler

## Protokol Masa Depan

Meskipun Bisq Easy saat ini merupakan satu-satunya protokol yang tersedia, beberapa protokol lain sedang dikembangkan untuk Bisq 2:


- Bisq Lightning**: Protokol pertukaran berdasarkan sistem escrow menggunakan kriptografi komputasi multipartai pada jaringan Lightning.
- Bisq MuSig**: Migrasi protokol utama dari Bisq 1 ke Bisq 2, menggunakan multisig 2-on-2 dengan uang jaminan.
- Pertukaran BSQ**: Pertukaran atomik instan antara BSQ dan BTC.
- Liquid Swaps**: Pertukaran aset di jaringan Liquid (USDT, BTC-L) melalui swap atom.
- Pertukaran Monero**: Pertukaran atom antara Bitcoin dan Monero.
- Liquid MuSig**: Versi protokol multisig yang menggunakan L-BTC untuk biaya yang lebih rendah dan kerahasiaan yang lebih tinggi.
- Submarine Swap**: Pertukaran antara Bitcoin di jaringan Lightning dan Bitcoin on-chain.
- Pertukaran Stablecoin**: Pertukaran atomik antara stablecoin Bitcoin dan USD.
- Opsi Multisig**: Pembuatan opsi jual dan beli P2P dengan pemblokiran BTC dalam transaksi multisig on-chain.
- Kontrak Terbuka Multisig**: Memungkinkan pembuatan kontrak bersyarat yang disesuaikan menggunakan sistem multisig 2-on-3 dengan arbitrase.

Protokol-protokol ini saat ini sedang dalam pengembangan dan akan diintegrasikan secara progresif ke dalam Bisq 2, menawarkan fleksibilitas yang lebih besar kepada pengguna sesuai dengan kebutuhan spesifik mereka.

## Sumber Daya yang Berguna


- Situs web resmi: [bisq.network](https://bisq.network)
- Dokumentasi: [Bisq Wiki](https://bisq.wiki)
- Dukungan: [Forum Bisq](https://bisq.community)
- Kode sumber : [GitHub](https://github.com/bisq-network)