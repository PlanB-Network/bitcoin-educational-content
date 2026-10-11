---
name: Sentinel
description: Apa itu dompet Watch-Only dan bagaimana cara menggunakannya?
---
![cover](assets/cover.webp)

---

***PERINGATAN:** Menyusul penangkapan pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, aplikasi Sentinel terus berfungsi, namun **wajib menggunakan Dojo milik sendiri** untuk mengakses informasi blockchain dan menyiarkan transaksi.*



---

*"Jaga kunci privat kamu, tetap privat."*

Dalam artikel ini, kita bakal mengulas semua hal yang perlu kamu tahu tentang dompet watch-only. Kita bahas cara kerjanya dan lihat berbagai aplikasi yang tersedia di pasar. Terakhir, kita kasih tutorial lengkap tentang salah satu aplikasi dompet watch-only paling populer: Sentinel.

## Apa itu Dompet Watch-Only?
Dompet watch-only, atau dompet hanya-baca, adalah perangkat lunak yang memungkinkan kamu memantau transaksi yang terhubung ke satu atau beberapa kunci publik Bitcoin, tanpa punya akses ke kunci privat yang terkait.

Jenis aplikasi ini cuma menyimpan data yang diperlukan untuk memantau dompet Bitcoin, termasuk melihat saldo dan riwayat transaksi, tapi tidak bisa mengakses kunci privat. Karena itu, tidak mungkin menghabiskan bitcoin yang ada di dompet lewat aplikasi watch-only.
![watch-only](assets/en/1.webp)
Watch-only biasanya dipakai bareng dompet perangkat keras. Ini memungkinkan penyimpanan kunci privat dompet secara "dingin", di perangkat yang tidak tersambung ke internet dan punya permukaan serangan yang kecil, sehingga kunci privat lebih terisolasi dari lingkungan yang berisiko.

Aplikasi watch-only, di sisi lain, cuma menyimpan kunci publik yang diperluas (`xpub`, `zpub`, dan sejenisnya) dari dompet Bitcoin. Kunci induk ini tidak bisa dipakai untuk menemukan kunci privat yang terkait dan karena itu tidak bisa digunakan untuk mengeluarkan bitcoin. Namun, kunci ini tetap memungkinkan derivasi kunci publik anak dan alamat penerima. Dengan mengetahui alamat dompet yang diamankan oleh dompet perangkat keras, aplikasi watch-only bisa memantau transaksi di jaringan Bitcoin, sehingga kamu bisa memantau saldo dan membuat alamat penerima baru tanpa harus terus menghubungkan dompet perangkat keras.

## Dompet Watch-Only Mana yang Harus Dipakai?
Saat ini, aplikasi watch-only yang paling lengkap adalah [Sentinel](https://github.com/wanderingking072/sentinel-android), yang awalnya dikembangkan oleh tim Samourai Wallet dan sekarang dipelihara oleh komunitas. Aplikasi ini menggabungkan semua fitur penting untuk dompet watch-only yang baik:

- Dukungan untuk kunci yang diperluas, kunci publik, dan alamat;
- Kemampuan mengelola beberapa akun atau dompet ke dalam koleksi;
- Pembuatan alamat untuk menerima bitcoin di dompet perangkat keras tanpa perlu menggunakannya secara langsung;
- Kemampuan membangun dan menyiarkan transaksi secara offline;
- Opsi untuk terhubung ke node Bitcoin milik sendiri;
- Integrasi Tor untuk privasi yang lebih kuat.

Kekurangan utama Sentinel ada pada fakta bahwa aplikasi ini cuma tersedia untuk Android dan tidak mendukung dompet multi-signature. Jadi kalau kamu pakai perangkat Android dan dompetmu tipe tanda tangan tunggal klasik, aku sarankan pakai Sentinel.

Bagi yang ingin melacak dompet multi-signature, BlueWallet adalah satu-satunya aplikasi yang aku tahu yang menyediakan mode watch-only untuk jenis dompet ini, dan bisa dipakai di Android maupun iOS.

Untuk pengguna iOS yang mencari alternatif untuk Sentinel, [Green Wallet](https://blockstream.com/green/) atau [Blue Wallet](https://bluewallet.io/watch-only/) mungkin menjadi pilihan, meskipun fungsionalitas watch-only mereka tidak sekomprehensif Sentinel. ![watch-only](assets/notext/2.webp)
## Bagaimana Cara Menggunakan Dompet Watch-Only Sentinel?
### Instalasi dan Pengaturan
Mulailah dengan menginstal aplikasi Sentinel. Kamu dapat melakukannya menggunakan [APK yang tersedia untuk diunduh di repositori github proyek](https://github.com/wanderingking072/sentinel-android/releases).






Kamu kemudian harus terhubung secara wajib ke Dojo Anda sendiri, karena server Samourai Wallet tidak lagi tersedia. Jika kamu belum memiliki Dojo sendiri, kamu dapat menggunakan Dojo yang disediakan oleh komunitas di situs [The Dojo Bay](https://dojobay.pw/), atau mengikuti tutorial kami untuk menginstal milik Anda sendiri :

https://planb.academy/tutorials/wallet/mobile/sentinel-9876f960-e964-4d20-8a6e-36231de1f4d9

![watch-only](assets/notext/4.webp)



Kemudian kamu akan tiba di halaman utama Sentinel.

![watch-only](assets/notext/6.webp)

Untuk memulai, kamu dapat mengatur aplikasi. Klik pada tiga titik kecil di sudut kanan atas, kemudian pada `Settings`.

![watch-only](assets/notext/7.webp)
Dengan pilih `User PIN code`, kamu bisa menetapkan kata sandi untuk mengamankan akses ke dompet watch-only kamu.

Kamu juga bisa mengubah mata uang referensi untuk mengonversi saldo ke mata uang fiat, atau bahkan menyembunyikan nilai fiat dengan mengaktifkan opsi `Hide fiat values`.

Untuk keamanan yang lebih tinggi, kamu bisa mengaktifkan `Disable Screenshots`, yang mencegah tangkapan layar di aplikasi Sentinel dan membantu menghindari kebocoran informasi yang tampil di layar.
![watch-only](assets/notext/8.webp)

Di menu pengaturan ini, Anda juga memiliki opsi untuk membackup Sentinel Anda.

### Menggunakan Dompet Watch-Only
Dari halaman utama, tekan tombol biru `NEW` untuk menambahkan kunci publik ekstensi baru untuk dilacak. Kemudian kamu memiliki opsi untuk memindai kode QR dari kunci Anda, atau langsung menempelkan kunci (`xpub`, `zpub`...) dengan memilih `Paste Pubkey`.

![watch-only](assets/notext/9.webp)

Umumnya, `xpub` dari dompet kamu dapat diakses langsung melalui perangkat lunak manajemen dompet yang kamu gunakan. Misalnya, jika kamu mengelola dompet perangkat keras kamu dengan Sparrow, informasi ini ditemukan di tab `Settings`, di bawah bagian `Keystore`.

![watch-only](assets/notext/10.webp)
Setelah memasukkan extended public key (`xpub`) di Sentinel, aplikasi bakal menawarin kamu untuk membuat koleksi baru.

Sebuah koleksi mewakili sekumpulan extended public key yang dikelompokkan bersama. Fitur ini bikin kamu tidak cuma bisa mencantumkan semua `xpub` milikmu, tapi juga mengelolanya secara lebih rapi.

Misalnya, kalau kamu punya Samourai Wallet dengan beberapa akun seperti deposit, premix, dan postmix, kamu bisa menggabungkan semua akun itu dalam satu koleksi bernama `Samourai`. Kalau dompet itu kamu kelola untuk keluarga, kamu bisa buat koleksi dengan nama `Family`.

Pilih `Create new collection`, lalu masukkan nama untuk kunci terperluas yang baru saja kamu tambahkan. Misalnya, kalau kamu memindai akun deposit dari dompet Samourai, kamu bisa beri nama `Deposit`. Setelah itu, klik `SAVE` untuk menyelesaikan prosesnya.

![watch-only](assets/notext/11.webp)

Selanjutnya, beri nama pada koleksi ini dan tekan ikon validasi yang terletak di pojok kanan atas layar untuk menyimpan koleksi. Koleksi kamu sekarang terlihat di layar utama Sentinel.

![watch-only](assets/notext/12.webp)

Jika kamu ingin menambahkan kunci publik terperluas lainnya, klik pada `NEW` lagi dan masukkan kunci kamu.

![watch-only](assets/notext/13.webp)
Setelah itu, kamu bakal diminta memilih koleksi tempat kamu ingin memasukkan kunci ini, atau langsung membuat koleksi baru kalau belum ada.

Misalnya, aku sudah menyiapkan koleksi khusus untuk dompet Ledger milikku, jadi setiap kunci baru dari Ledger langsung aku masukkan ke koleksi tersebut agar lebih rapi dan terorganisir.

![watch-only](assets/notext/14.webp)

Untuk melihat kunci terperluas dari sebuah koleksi secara detail, cukup klik pada koleksi tersebut. Kamu kemudian dapat menavigasi melalui tab yang berbeda untuk melihat riwayat transaksi.

![watch-only](assets/notext/15.webp)

Dari sebuah koleksi, dengan mengetuk tiga titik kecil di pojok kanan atas, kemudian pada `View Unspent Outputs`, kamu dapat mengakses daftar UTXOs yang dipegang oleh dompet yang dilacak.

![watch-only](assets/notext/16.webp)

## Mengirim dan Menerima Bitcoin dari Sentinel

Seperti dompet watch-only yang baik, Sentinel memungkinkan kamu membuat alamat penerima untuk menerima bitcoin di dompet yang kamu pantau.

Selain itu, Sentinel juga menyediakan fitur lanjutan seperti pembuatan dan penyiaran transaksi Bitcoin dalam bentuk partially signed Bitcoin transaction (PSBT). Artinya, dompet yang memegang kunci privat bisa menandatangani transaksi tersebut, lalu setelah ditandatangani, transaksi itu bisa disiarkan ke jaringan Bitcoin lewat Sentinel.

Mari kita lihat cara melakukannya.

**Perhatian, sebaiknya kamu tidak menerima bitcoin ke alamat yang belum diverifikasi langsung oleh dompet yang memegang kunci privat.** Kalau dompet perangkat keras atau dompet yang menyimpan kunci privat tidak secara eksplisit mengonfirmasi bahwa alamat tertentu memang miliknya, mengirim bitcoin ke alamat itu jadi berisiko. Tanpa konfirmasi tersebut, tidak ada jaminan alamat itu benar-benar terhubung ke dompetmu. Jadi, fitur penerimaan di dompet watch-only harus dipakai dengan hati-hati, karena dana yang dikirim tanpa verifikasi bisa saja hilang.

Untuk menerima bitcoin lewat Sentinel, pilih koleksi yang kamu inginkan, lalu buka tab yang sesuai dengan extended public key yang mau kamu pakai untuk menerima dana.

![watch-only](assets/notext/17.webp)

Akhirnya, klik pada ikon panah di pojok kiri bawah layar. Sentinel kemudian menghasilkan alamat penerimaan kosong untuk kamu. Kamu dapat menyalinnya, atau memindainya menggunakan kode QR.

![watch-only](assets/notext/18.webp)
Untuk membuat PSBT di Sentinel dan mulai transaksi pengeluaran, buka extended public key dari dompet yang ingin kamu pakai untuk melakukan pembayaran.

Misalnya, kita ambil contoh akun deposit di dompet Samourai milikku. Setelah masuk ke akun tersebut, klik ikon panah yang ada di bagian kanan bawah layar.

![watch-only](assets/notext/19.webp)

Masukkan semua parameter yang terkait dengan transaksi Anda:
- Masukkan alamat penerima (dengan mengklik ikon kode QR, kamu memiliki opsi untuk memindai alamat ini);
- Tentukan jumlah yang akan dikirim ke alamat ini;
- Tentukan biaya transaksi.

Setelah kamu mengisi semua bidang yang diperlukan untuk transaksi kamu, tekan tombol `COMPOSE UNSIGNED TRANSACTION`.

![watch-only](assets/notext/20.webp)

Setelah itu, kamu akan masuk ke bagian PSBT, yaitu transaksi Bitcoin yang sudah dibangun tapi belum ditandatangani, karena Sentinel tidak punya akses ke kunci privat kamu.

Di tahap ini, kamu bisa menyalin transaksi tersebut, mengekspornya sebagai file `.psbt`, atau memindainya lewat kode QR animasi.

![watch-only](assets/notext/21.webp)

Kemudian, pergilah ke dompet Anda yang memiliki kunci pribadi untuk menandatangani transaksi (Samourai, dompet perangkat keras...).

![watch-only](assets/notext/22.webp)

Setelah transaksi ditandatangani, Anda dapat kembali ke Sentinel untuk menyiarkannya. Untuk melakukan ini, dari menu utama, klik pada tiga titik kecil di bagian atas kanan, kemudian pada `Broadcast transaction`.

![watch-only](assets/notext/23.webp)

Kamu memiliki opsi untuk memasukkan PSBT yang telah ditandatangani kamu dengan tiga cara berbeda:
- Dengan menempelkannya langsung dari clipboard Anda;
- Dengan mengimpor dari file `.psbt`;
- Dengan memindainya melalui kode QR.

![watch-only](assets/notext/24.webp)

Setelah transaksi yang ditandatangani dimasukkan dalam bingkai abu-abu, kamu dapat mengklik tombol hijau `BROADCAST TRANSACTION` untuk menyiarkannya di jaringan Bitcoin. Sentinel akan memberi Anda TXID-nya.

![watch-only](assets/notext/25.webp)

