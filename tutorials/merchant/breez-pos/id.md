---
name: Breez point of sales

description: Panduan untuk mulai menerima bitcoin menggunakan Breez POS
---

![cover](assets/cover.webp)

_Teks ini berasal dari situs dokumentasi Breez: https://doc.breez.technology/How-to-Get-Started-with-Breez-POS.html_

## Apa itu Breez POS?

**Breez** adalah aplikasi Lightning yang lengkap dan non-custodial. Mari kita uraikan:

- **Lightning** adalah jaringan pembayaran bitcoin yang mengurangi waktu transaksi dari menit menjadi milidetik dan biaya transaksi dari beberapa dolar menjadi beberapa sen atau kurang. Lightning mengubah bitcoin dari emas digital menjadi mata uang digital sambil mempertahankan semua keuntungan yang membuat bitcoin hebat.
- **Non-custodial** berarti Breez tidak mengambil kepemilikan uang pengguna. Banyak aplikasi Lightning mengambil kepemilikan uang pengguna mereka. Mereka pada dasarnya adalah bank bitcoin. Dengan aplikasi non-custodial seperti Breez, semua pengguna adalah bank mereka sendiri.
- **Full-service** berarti Breez mengurus hampir semua operasi teknis secara otomatis dan di latar belakang. Hal-hal seperti pembuatan channel, likuiditas masuk, dan routing tetap tersembunyi. (Namun, Breez juga bersifat open source, jadi mereka yang tertarik untuk mengaudit teknologinya dipersilakan untuk melakukannya!)

**Breez POS** adalah singkatan dari mode point-of-sale kami. Dengan kata lain, Breez berfungsi seperti kasir digital untuk bisnis dan pedagang yang ingin menerima pembayaran Lightning (selain dari mode "standar"nya, yang seperti versi digital dari dompet kulit untuk bitcoin, dan pemutar podcast generasi berikutnya). Sekarang mari kita lihat bagaimana cara mengatur Breez sebagai kasir Lightning untuk bisnis Anda.

## Bagaimana cara memulai dengan Breez?

1. Langkah pertama adalah mengunduh aplikasinya. Tersedia untuk Android dan iOS (instal TestFlight dan klik tautan dari perangkat Anda).
2. Breez dapat membackup dirinya sendiri secara otomatis ke Google Drive, iCloud, atau server WebDav apa pun.
   > Perhatikan bahwa setiap perangkat menjalankan node Lightningnya sendiri. Anda dapat menjalankan mode POS di sebanyak mungkin perangkat yang Anda inginkan, tetapi saldo akan tetap terpisah.
3. Dengan aplikasi terbuka, klik pada ikon di kiri atas untuk menemukan mode Point of Sale.

## Mengatur POS

1. Klik ikon di kiri atas itu, dan klik Point of Sale > Pengaturan POS.

### Kata Sandi Manajer

Di Pengaturan POS, Anda memiliki opsi untuk membuat kata sandi manajer. Kata sandi manajer membuatnya tidak mungkin untuk mengirim pembayaran keluar dari aplikasi Breez tanpa otorisasi. Staf penjualan hanya akan dapat menerima pembayaran dari perangkat. Perhatikan bahwa jika Anda menggunakan opsi ini, Anda mungkin juga ingin mencegah akses ke backup Breez, sehingga menggunakan akun WebDav eksternal (misalnya, Nextcloud) direkomendasikan untuk kasus penggunaan ini.

### Daftar Barang

Daftar barang adalah katalog item yang dijual dan harganya. Ada dua cara untuk menambahkan item ke daftar:

- Untuk memasukkan item satu per satu, klik pada Item di dekat bagian atas tampilan POS utama, lalu pada tanda "+" di kanan bawah. Di sini Anda dapat memasukkan nama dari satu jenis item, harga (ditampilkan dalam ekuivalen mata uang pilihan Anda), dan SKU (pengenal internal unik untuk jenis item tersebut; ini opsional).
- Untuk memasukkan banyak item sekaligus, klik pada ikon kalkulator di kiri atas, kemudian Point of Sale > Preferences > POS Settings, dan klik pada tiga titik di sebelah kanan Items List, lalu pada Import from CSV. Ini akan memungkinkan Anda untuk mengimpor file CSV yang telah Anda siapkan sebelumnya yang berisi nama-nama item, harga, dan SKU.

### Tampilan Fiat

Breez hanya mengirim dan menerima bitcoin, dan untuk sebagian besar transaksi di Lightning, yang cenderung untuk jumlah yang lebih kecil, jumlahnya biasanya ditampilkan dalam Satoshis, alias sats (1 BTC = 100,000,000 sats). Namun, banyak pedagang merasa praktis untuk dapat melihat (dan memberitahu pelanggan) nilai pembelian yang ditampilkan dalam mata uang fiat lokal.

Di tampilan POS utama, mata uang yang saat ini ditampilkan terlihat di sisi kanan (default adalah SAT). Ada juga daftar drop-down dari mata uang lain yang tersedia untuk ditampilkan. Untuk menambah atau menghapus mata uang dari daftar drop-down ini, klik pada Point of Sale > Preferences > Fiat Currencies. Kemudian cukup centang mata uang yang ingin Anda masukkan ke dalam menu drop-down Anda dan hilangkan centang pada mata uang yang ingin Anda hilangkan.

Nilai yang ditampilkan berasal dari yadio, outlet terhormat untuk data nilai tukar, dan diperbarui hampir secara real-time. Namun ingat: apa pun nilai mata uang yang saat ini ditampilkan, pembayaran itu sendiri adalah dalam bitcoin.

### Memproses Pesanan

Untuk menyusun pesanan, tambahkan item dari daftar item atau cukup masukkan jumlah di keypad. Kemudian klik pada Charge di bagian atas tampilan POS utama. Anda kemudian akan melihat kode QR yang dapat dipindai oleh pelanggan dengan aplikasi Lightning mereka, yang dapat Anda bagikan langsung dari aplikasi lain di perangkat Anda, atau yang dapat Anda salin dan tempel jika perlu.

Saat memindai kode tersebut atau mengklik pada invoice yang dibagikan/ditempel, pelanggan akan melihat invoice di aplikasi Lightning mereka dan memiliki opsi untuk membayarnya dan menyelesaikan transaksi segera.

Setelah Anda melihat animasi Payment approved! di aplikasi Breez pada perangkat pedagang, Anda dapat klik pada ikon printer untuk menghasilkan tanda terima untuk pelanggan. Untuk menggunakan printer tanda terima di Android, coba gunakan driver ini. Catatan bahwa Anda juga dapat mencetak transaksi sebelumnya melalui layar Transactions.

### Laporan Penjualan

Untuk melihat laporan harian/mingguan/bulanan dari penjualan Anda (untuk tujuan akuntansi atau lainnya), klik pada ikon di kiri atas, kemudian klik pada Transactions. Klik pada ikon Report untuk menampilkan laporan dan ikon Calendar untuk mengubah rentang tanggal yang dipilih.

### Mengekspor Transaksi

Untuk melihat daftar pembayaran yang diterima di Breez, klik pada ikon di kiri atas, kemudian klik pada Transactions. Klik pada tiga titik di kanan atas, kemudian pada Export untuk mengekspor daftar pembayaran masuk dalam format CSV. Untuk membatasi daftar ke periode waktu tertentu, klik pada ikon kalender untuk menetapkan rentang tanggal.

### Mencetak Tanda Terima

Untuk mencetak tanda terima penjualan, klik pada ikon print di kanan atas dialog konfirmasi pembayaran. Atau, klik pada ikon di kiri atas, kemudian klik pada Transactions. Temukan penjualan yang ingin dicetak, bukalah, dan klik ikon print di kanan atas.

> Catatan: gunakan driver ini untuk mencetak pada printer termal Bluetooth/USB portabel 58mm/80mm.

## Saya ingin belajar lebih lanjut

- Untuk informasi lebih lanjut tentang Lightning dan Breez, cek blog kami [di sini](https://breez.technology/blog).
- Untuk tips teknis lebih lanjut tentang cara memaksimalkan penggunaan aplikasi dan melakukan operasi umum, silakan lihat [dokumentasi](https://breez.technology/documentation) kami.
- Jika Anda mengalami kesulitan dan tidak dapat menemukan jawaban dalam literatur bantuan kami, Anda dapat menemukan kami di [Telegram](https://t.me/breez_labs) atau mengirimkan kami sebuah [email](mailto:support@breez.technology).
- Jika Anda ingin melihat beberapa video demonstrasi dari mode POS Breez yang dibuat oleh penggemar dan pengguna kami, [di sini](https://www.youtube.com/watch?v=xxxx) ada satu yang singkat dan bagus, dan [di sini](https://www.youtube.com/watch?v=xxxx) ada yang lebih panjang dan lebih detail.