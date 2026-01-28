---
name: Nunchuk
description: Ponsel Wallet cocok untuk semua orang
---
![cover](assets/cover.webp)



## Wallet yang kuat


Nunchuk hadir pada akhir tahun 2020 dengan filosofi yang jelas: menjadikan multi-signature sebagai standar. Oleh karena itu, Nunchuk dirancang untuk menjalankan fungsi yang sangat canggih, dengan pilihan berharga untuk membangun desain langsung pada Bitcoin Core, perangkat lunak referensi untuk ekosistem Bitcoin.



Setelah lebih dari 4 tahun pengembangan dan penggunaan, Nunchuk siap untuk dicoba dalam skala besar. Jika Anda seorang pemula dan tidak terbiasa dengan Nunchuk, panduan ini akan membantu Anda mengambil langkah pertama dan menemukan perangkat lunak ini, yang fungsi-fungsi lanjutannya dapat Anda pelajari setelah Anda berhasil melewati dampak pertama. Tutorial ini didedikasikan untuk pengguna tingkat menengah yang memiliki keterampilan yang diperlukan untuk mengikuti semua langkah, tetapi dapat menjadi inspirasi bagi semua orang untuk mengetahui cara meningkatkan keterampilan. Kita akan mulai dengan versi seluler, dan hal ini penting, karena Nunchuk memiliki perangkat lunak yang dapat dijalankan di komputer juga.



## Unduh


Langkah pertama tentu saja memutuskan di mana Anda akan mengunduh aplikasi ini. Kunjungi [situs resmi](https://nunchuk.io/) di mana Anda bisa menemukan beberapa dokumentasi (tidak banyak tetapi ini merupakan permulaan), presentasi fitur serta, di bagian akhir halaman, semua tautan unduhan.



📌 Untuk tutorial ini, saya memutuskan untuk menunjukkan kepada Anda cara mengunduh Software Wallet dari repositori Github dan cara memverifikasi rilisnya sebelum memasangnya di ponsel Anda. **Prosedur berikut ini hanya dapat dilakukan dari komputer Anda**, jadi saya sarankan Anda melakukan semua langkah ini dari desktop atau laptop Anda dan - setelah semua verifikasi - mentransfer file `.apk` ke ponsel Anda.



![image](assets/en/01.webp)



Jika kemampuan Anda belum terlalu mahir, Anda dapat memutuskan untuk mengunduh `.apk` dari toko resmi dan langsung melompat ke bagian konfigurasi tutorial ini. Sebaliknya, jika Anda ingin mencoba, ikuti terus langkah demi langkah.



Jadi, dari komputer desktop Anda, klik _Kunjungi repositori sumber terbuka kami_



Tautan ini akan membawa Anda ke halaman Github Nunchuk, di mana Anda akan menemukan sejumlah repo. Kami akan fokus pada yang _nunchuk-android_



![image](assets/en/02.webp)



Pada layar berikutnya, cari di sebelah kanan bagian _Releases_ dan pilih _Latest_



![image](assets/en/03.webp)



Di bawah _Assets_, unduh rilis (dalam contoh ini 1.67.apk), bersama dengan file SHA256SUMS dan SHA256SUMS.asc.



![image](assets/en/04.webp)



Untuk menemukan kunci GPG pengembang, kembali ke bagian _Releases_ pada repositori dan cari 1.9.53 (atau sebelumnya) yang memiliki tautan untuk mendapatkan dan mengunduh _Kunci GPG_



![image](assets/en/05.webp)



Kami akan melanjutkan dengan verifikasi melalui alat praktis yang ditawarkan oleh Sparrow wallet, yang memiliki jendela khusus untuk tujuan ini dan mendukung tanda tangan PGP dan Manifes SHA256.



Kemudian jalankan Sparrow dan dari menu _Tools_ pilih _Verify Download_.



![image](assets/en/06.webp)



Pada jendela yang muncul, Anda akan menemukan kolom-kolom untuk "diisi": pilih tombol _Browse_ di sebelah kanan dan pilih, untuk setiap kolom, file yang sesuai yang baru saja Anda unduh dari Github. Ketika Anda telah menyelesaikan semua langkah, jendela akan terlihat sebagai berikut, dengan tanda centang Green dan konfirmasi Hash pada manifes.



![image](assets/en/07.webp)


**N.B. tangkapan layar berasal dari PC Windows, praktik yang sama dapat digunakan untuk sistem operasi apa pun di komputer Anda, cukup dengan menginstal Sparrow wallet. Dan terverifikasi!**



Anda dapat menemukan panduan untuk Sparrow wallet untuk mengunduh Software Wallet ini


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Anda kemudian dapat mentransfer file `.apk` dari komputer ke ponsel Anda



![image](assets/en/08.webp)



dan menginstal Nunchuk



![image](assets/en/09.webp)



Sebelum meluncurkan Nunchuk di ponsel Anda, buka Orbot dan letakkan pendatang baru di daftar aplikasi yang akan dirutekan di bawah Tor.



![image](assets/en/11.webp)



Sekarang jalankan Nunchuk. Untuk fitur-fitur proyek-yang bukan merupakan pokok bahasan dalam tutorial ini-Nunchuk, setelah dibuka, akan mengundang Anda untuk masuk melalui email atau profil Google. Sampai Anda berencana untuk memanfaatkan paket lanjutan Nunchuk Inc, **hindari login** dan lanjutkan dengan memilih opsi _Continue as guest_.



![image](assets/en/12.webp)



## Pengaturan


Nunchuk menampilkan jendela presentasi _Home_, di mana mudah untuk memahami filosofi pengoperasiannya dan yang akan kami uraikan sebentar lagi.



Di bagian bawah, Anda dapat menemukan menu, dan sebagai langkah pertama, pilih _Profile_ untuk mengakses pengaturan.



![image](assets/en/10.webp)



Kemudian pilih _Pengaturan tampilan_, terus abaikan undangan untuk membuat akun.



![image](assets/en/14.webp)



Pada layar di bawah ini Anda dapat memeriksa apakah Wallet online dan Anda dapat menghubungkan server Anda, dengan memperhatikan instruksi pada tautan yang ditawarkan dengan mengklik _guide_.



![image](assets/en/15.webp)



Simpan pengaturan dengan perintah _Save network settings (Simpan pengaturan jaringan), kembali ke menu _Profile (Profil) dan pilih _Security settings (Pengaturan keamanan).



![image](assets/en/16.webp)



Dari menu ini Anda dapat mengatur cara mempertahankan pembukaan aplikasi. Untuk mencegah akses yang tidak diinginkan, Anda dapat melindungi Nunchuk dengan biometrik ponsel, dan/atau menambahkan PIN keamanan.



![image](assets/en/17.webp)



Lihat juga menu _Tentang_, yang akan selalu Anda temukan di jendela _Profil_



![image](assets/en/18.webp)



yang memungkinkan Anda memeriksa versi aplikasi, atau menghubungi pengembang jika diperlukan.



![image](assets/en/19.webp)



## Generasi Kunci dan Wallet


Seperti yang mudah ditebak dari filosofi Nunchuk, perangkat lunak ini dimaksudkan sebagai alat yang berguna untuk mengelola Dompet multi-tanda tangan. Untuk menjalankan fungsi ini, Nunchuk mengizinkan pembuatan Wallet dengan memisahkannya dari kunci yang diperlukan untuk mengatur tanda tangan digital.



Faktanya, pengoperasian Nunchuk yang ideal melibatkan pembuatan Dompet yang hanya dapat ditonton, bergantung pada kunci yang dapat "masuk angin."



Pada layar sebelumnya, Anda mungkin telah memperhatikan bahwa ada sebuah menu di bagian bawah yang disebut _Keys_. Jika Anda baru saja mengunduh Nunchuk, di _Home_ dan _Keys_, Anda akan melihat tombol besar yang mengundang Anda untuk menambahkan kunci, _Add Key_.



![image](assets/en/20.webp)


![image](assets/en/21.webp)



**Beginilah cara kerja Nunchuk:** Pertama-tama Anda mengimpor kunci generate dan kemudian Anda membuat Wallet, mengkonfigurasinya untuk memilih kunci mana yang akan mengotorisasi pembukaan kunci dana yang tersimpan di dalamnya.



Bahkan dalam kasus Wallet singlesig, Anda membuat kuncinya terlebih dahulu dan baru kemudian Wallet. Dan itulah yang akan kita lakukan sekarang, dimulai dengan Wallet singlesig untuk mencairkan suasana dan menemukan fungsi-fungsi Nunchuk.



Klik _Tambahkan Kunci_



![image](assets/en/22.webp)



Nunchuk menampilkan sejumlah perangkat tanda tangan yang didukung, tetapi untuk memulai, pilih _Software_.



![image](assets/en/23.webp)



Nunchuk akan membuat generate menjadi Mnemonic yang akan disimpan pada perangkat. Anda kemudian perlu menuliskan urutan kata untuk pencadangan, menciptakan kondisi lingkungan terbaik dan memastikan Anda memiliki waktu untuk melakukannya dengan baik dan tenang. Perangkat lunak ini hanya menampilkan Mnemonic satu kali, apakah Anda memilih untuk menampilkannya sekarang atau nanti, jadi pilihlah _Create and backup now_.



![image](assets/en/24.webp)



Nunchuk menghasilkan kalimat Mnemonic 24 kata, yang langsung muncul di layar berikutnya



![image](assets/en/25.webp)



dan kemudian melanjutkan untuk melakukan pemeriksaan cepat, meminta Anda untuk memilih kata yang benar, dari 3 pilihan, sesuai dengan nomor dalam urutan Mnemonic.


Jika Anda telah menulis Mnemonic dengan benar, tombol _Lanjutkan_ akan beroperasi. Tekan untuk melanjutkan.



![image](assets/en/26.webp)



Beri nama kunci Anda dan tekan _Lanjutkan_.



![image](assets/en/27.webp)



Pada akhir langkah ini, Anda akan ditanya apakah akan menambahkan [passphrase](https://planb.academy/en/resources/glossary/passphrase-bip39) pada frasa Mnemonic Anda. Jika Anda tidak memiliki pengetahuan yang diperlukan tentang cara menggunakan passphrase, mengatur cadangannya, atau bagaimana cara kerjanya, saya sarankan Anda memilih _Saya tidak memerlukan frasa sandi_.



![image](assets/en/28.webp)



Kunci akhirnya dibuat dan ditampilkan kepada Anda dalam menu:




- Dengan _Key Spec_, sidik jari utama ditunjukkan
- Anda memiliki pengaturan, tiga titik di kanan atas, di mana Anda dapat menghapus kunci atau menandatangani pesan
- Di samping nama tuts, Anda akan menemukan ikon pena, dengan mengekliknya Anda dapat mengedit nama tuts, misalnya untuk menertibkan tuts Anda di masa mendatang.
- Sebagai perintah terakhir, Anda dapat memeriksa status kesehatan kunci: dengan menekan _Run health check_, Anda dapat meminta aplikasi untuk memeriksa apakah ada kunci yang terganggu.



Setelah Anda merasa puas, klik _Selesai_



![image](assets/en/29.webp)



Pada menu _Keys_, Anda akan melihat tombol pertama Anda muncul.



![image](assets/en/30.webp)



Dengan masuk ke menu _Home_, opsi untuk membuat Wallet akan muncul. Klik _Buat dompet baru_.



![image](assets/en/31.webp)



Nunchuk menunjukkan kepada Anda sejumlah kemungkinan yang sebagian besar berkaitan dengan layanan yang ditawarkan perusahaan yang bukan merupakan subjek dari tutorial ini.



Dalam panduan ini kita akan membuat _Hot Wallet dan _Dompet khusus_ dengan merinci detailnya.


Mari kita mulai dengan _Custom wallet_.



![image](assets/en/32.webp)



Secara sederhana, aplikasi ini akan meminta Anda untuk menamai Wallet yang baru ini dan memilih skrip untuk alamatnya. Untuk tutorial ini, saya memilih untuk membiarkan pengaturan default, _Native segwit_. Setelah Anda selesai, pilih _Lanjutkan_



![image](assets/en/33.webp)



Konfigurasi Wallet selanjutnya meminta Anda untuk mengatur dengan kunci mana dana Wallet ini akan dibuka. Jika terdapat beberapa kunci, Anda akan diperlihatkan daftar yang dapat dipilih. Untuk saat ini kami hanya membuat satu kunci, jadi kami memilih untuk memberi tanda centang pada kunci tersebut. Pada sudut kanan bawah, anda dapat melihat bagaimana Nunchuk akan meminta anda untuk mengatur multi-signature Wallet yang akan anda buat, dengan menambah jumlah _Kunci yang dibutuhkan_.



![image](assets/en/34.webp)



Karena kita sedang membuat single, kita tinggalkan `1` dan klik _Continue_.



Terakhir, layar verifikasi muncul, di mana Anda dapat memeriksa fitur-fitur Wallet:




- nama
- tage `1/1 Multisig`, yang merupakan cara Nunchuk menamai singleig Wallet
- jenis skrip, `Native SegWit`
- tombol `Keys`, dengan sidik jari dan jalur turunannya



Setelah Anda puas, tekan _Buat dompet_



![image](assets/en/35.webp)



Wallet telah dibuat dan Anda dapat mengunduh file [.BSMS](https://github.com/Bitcoin/bips/blob/master/bip-0129.mediawiki) sebagai cadangan. Untuk kembali ke menu utama, klik tanda panah di sudut kiri atas.



![image](assets/en/36.webp)



Anda berada di _Home_, di mana Anda diperlihatkan Wallet yang baru saja dibuat yang melaporkan saldo dan status koneksi. Dengan mengklik di ruang biru, Anda dapat mengakses fungsi utama Wallet.



![image](assets/en/37.webp)





- Ikon lensa di sudut kanan atas memungkinkan Anda melakukan pencarian transaksi;
- `Lihat konfigurasi Wallet` memberikan akses ke menu konfigurasi, di mana Anda dapat mengedit nama Wallet dan mengaktifkan opsi lanjutan, di kanan atas (di mana Anda tidak dapat mengambil tangkapan layar). Di sini Anda dapat mengekspor konfigurasi Wallet, label, mengganti kunci, mengubah [gap limit](https://planb.academy/en/resources/glossary/gap-limit) dan banyak lagi.



## Transaksi dengan Nunchuk



Penghargaan _Menerima_



![image](assets/en/38.webp)



Aplikasi ini diprogram untuk menampilkan QR Code dari Address atau menyalin/membagikan scriptPubKey untuk menerima dana onchain.



![image](assets/en/39.webp)



Kami memiliki UTXO yang tiba pada Address pertama ini,



![image](assets/en/40.webp)



tetapi kita masih mengklik _Receive_ untuk menerima yang lain.



![image](assets/en/41.webp)



Tujuannya adalah agar Anda mengetahui bahwa Nunchuk melaporkan Address baru ini kepada Anda sebagai _Alamat yang tidak digunakan_, tetapi juga menunjukkan kepada Anda bahwa Anda memiliki _Alamat yang digunakan_ dan jumlahnya.



### Transaksi pembelanjaan dengan kontrol koin



Ketika UTXO kedua ini juga telah tiba, kembali ke layar utama Wallet untuk memeriksa status dua transaksi yang masuk dan, yang paling penting, klik opsi _Lihat koin_



![image](assets/en/42.webp)



di mana Anda akan diperlihatkan masing-masing UTXO. Di sini Anda dapat memilih untuk melihat satu per satu dengan mengklik panah kecil di sebelah jumlah



![image](assets/en/43.webp)



dan periksa kapan tiba, deskripsinya, blokir UTXO agar tidak dibelanjakan, dan lainnya.



![image](assets/en/44.webp)



Tetapi jika Anda kembali ke menu _Coins_ dengan mengklik panah di sudut kanan atas, Anda dapat mengaktifkan "Coin Control" untuk membelanjakan UTXO Anda dengan cara yang lebih terkontrol.



Dalam contoh berikut ini, saya memilih untuk memilih UTXO dari 21.000 Sats, kemudian klik simbol di sudut kiri bawah.



![image](assets/en/45.webp)



Nunchuk secara otomatis membuka jendela _New transaction_ untuk membelanjakan UTXO ini. Dalam transaksi pembelanjaan, pertama-tama, Anda harus mengatur jumlahnya secara manual atau dengan memilih _Send all selected_ untuk mengirim semua saldo kontrol koin, tanpa menghasilkan sisa. Setelah jumlahnya ditetapkan, pilih _Lanjutkan_



![image](assets/en/46.webp)



Sekarang Nunchuk menunjukkan ke mana harus menempelkan Address untuk mentransfer dana ini, merinci deskripsi, dan menyelesaikan transaksi.



![image](assets/en/47.webp)



Memilih _Buat transaksi_ akan mendelegasikan biaya otomatis dan manajemen transaksi ke aplikasi. Saya sarankan untuk memilih _Custom transaction_ untuk kontrol yang lebih besar.



Pada layar baru ini, penting untuk memilih




- kurangi biaya dari jumlah pengiriman, untuk mencegah biaya dibayarkan oleh UTXO lain yang ada di Wallet, membelanjakannya dan menghasilkan sisa (yang merupakan hilangnya privasi yang dapat dihindari);
- dan kemudian mengatur biaya secara manual setelah memeriksa pada penjelajah.



Setelah melakukan semua langkah ini, klik _Continue_



![image](assets/en/48.webp)



Layar berikutnya adalah ringkasan lengkap dari transaksi. Jika semuanya baik-baik saja, konfirmasikan dengan memilih _Konfirmasi dan buat transaksi_.



![image](assets/en/49.webp)



Dengan _Tanda tangan tertunda_, Nunchuk memberi tahu Anda bahwa transaksi sedang menunggu tanda tangan Anda untuk menyetujui pengeluaran, yang Anda lampirkan dengan mengeklik _Tanda tangan_.



![image](assets/en/50.webp)



Perintah _Broadcast_ muncul di bagian bawah untuk menyebarkan transaksi yang telah diselesaikan dan ditandatangani.



![image](assets/en/51.webp)



### Transaksi pengeluaran dari menu _Kirim_



Sementara di halaman utama Wallet kita melihat transaksi keluar dan menunggu konfirmasi, kita menggunakan menu _Kirim_ untuk mensimulasikan pengeluaran harian.



![image](assets/en/52.webp)



Mengklik _Kirim_, pada kenyataannya, akan memunculkan layar untuk mengirim transaksi, yang sama dengan yang baru saja dilihat tetapi tanpa melalui kontrol koin.



Pada contoh kedua ini, saya memutuskan untuk memilih _Transaksi khusus_ dan mengirimkan seluruh jumlah, tetapi saya bisa saja mengaturnya secara manual. Setelah Anda memutuskan jumlah yang akan dikirim, tekan _Continue_.



![image](assets/en/53.webp)



Kemudian selalu tentukan apakah biaya dikurangi dari UTXO yang bersangkutan (dalam contoh ini pilihannya dipaksakan, karena hanya ada satu), sesuaikan biaya secara manual sesuai dengan situasi pada saat itu di Mempool, dan tekan _Lanjutkan_.



![image](assets/en/54.webp)



Jika layar ringkasan memuaskan, pilih _Confirm and create transaction_.



![image](assets/en/55.webp)



Tanda tangani transaksi dengan _Tanda Tangan_



![image](assets/en/56.webp)



dan menyebarkannya ke jaringan.



![image](assets/en/57.webp)



Wallet pada saat ini berada pada titik ini dengan saldo nol dan riwayat sedang diperbarui.



![image](assets/en/58.webp)



## Penciptaan "Hot Wallet"



Terakhir dan tanpa meninggalkan apa pun dari tahap awal Nunchuk mobile, mari kita lihat bagaimana hal ini menciptakan apa yang disebut aplikasi sebagai "Hot Wallet."



Pada menu _Home_ Nunchuk, di mana daftar Dompet muncul, klik `+` di sudut kanan atas.



![image](assets/en/59.webp)



Pilih _Dompet panas_ dari opsi



![image](assets/en/60.webp)



Nunchuk memberikan beberapa saran untuk menangani Dompet Hot di halaman presentasi, di mana Anda akan memilih _Continue_ untuk melanjutkan.



![image](assets/en/61.webp)



Setelah beberapa saat, Wallet akan dibuat dan muncul dalam daftar dengan warna kecoklatan. Ini adalah warna yang digunakan Nunchuk untuk memperingatkan Anda bahwa Anda belum mencadangkan Wallet.



![image](assets/en/62.webp)



Klik pada nama Wallet, untuk mengakses konfigurasinya, dan Anda mungkin akan melihat undangan untuk segera mencadangkan frasa Mnemonic.



![image](assets/en/63.webp)



Prosedurnya sama seperti yang telah kita lihat sebelumnya, jadi kita tidak akan mengulanginya lagi. Setelah selesai, Nunchuk akan membawa Anda ke halaman kunci yang relevan, yang dapat Anda edit seperti yang Anda buat dengan prosedur _Custom_.



![image](assets/en/64.webp)



Coba juga _Periksa kesehatan_



![image](assets/en/65.webp)



atau untuk melihat cara menampilkan semua Dompet Anda di _Home_ aplikasi.



![image](assets/en/66.webp)



## Agar selalu ingat untuk melanjutkan secara mandiri


Sama seperti urutan pembuatannya, yaitu pertama-tama membuat kunci dan kemudian Wallet, Anda harus mempertahankan urutan sebaliknya untuk menghapus item ini dari aplikasi Anda.



Jika Anda ingin menghapus salah satu kunci, Anda harus terlebih dahulu menghapus Wallet, atau Dompet, yang menggunakan salah satu kunci tanda tangan untuk transaksi: pertama-tama Anda harus menghapus Dompet, baru kemudian kuncinya. Jika Anda tidak mengikuti urutan ini, Anda tidak akan dapat menghapus kunci tersebut.



Sekarang setelah Anda mengetahui cara memulai dengan Nunchuk, Anda dapat terus mempelajari aplikasi ini dan menemukan rahasianya. Dalam tutorial ini, kami hanya mengambil langkah pertama, tetapi ada aplikasi yang lebih canggih dan kebutuhan tingkat lanjut yang dapat Anda penuhi dengan Software Wallet ini.