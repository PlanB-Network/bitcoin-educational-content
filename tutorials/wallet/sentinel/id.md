---
name: Sentinel Watch-Only
description: Apa itu dompet Watch-Only dan bagaimana cara menggunakannya?
---
![cover](assets/cover.webp)

---

***PERINGATAN:** Menyusul penangkapan pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, aplikasi Sentinel terus berfungsi, namun **wajib menggunakan Dojo milik sendiri** untuk mengakses informasi blockchain dan menyiarkan transaksi.*

_Kami terus mengikuti perkembangan kasus ini serta perkembangan terkait alat-alat yang berhubungan. Yakinlah bahwa kami akan memperbarui tutorial ini seiring dengan tersedianya informasi baru._

_Tutorial ini disediakan hanya untuk tujuan pendidikan dan informasi. Kami tidak mendukung atau mendorong penggunaan alat-alat ini untuk tujuan kriminal. Tanggung jawab setiap pengguna adalah untuk mematuhi hukum di yurisdiksi mereka._

---

*"Jaga kunci privat Anda, tetap privat."*

Dalam artikel ini, kami menjelajahi segala hal yang perlu Anda ketahui tentang dompet watch-only. Kami membahas cara kerjanya dan mengkaji berbagai aplikasi yang tersedia di pasar. Akhirnya, kami menawarkan tutorial terperinci tentang salah satu aplikasi dompet watch-only paling populer: Sentinel.

## Apa itu Dompet Watch-Only?
Dompet watch-only, atau dompet hanya-baca, adalah jenis perangkat lunak yang dirancang untuk memungkinkan pengguna mengamati transaksi yang terkait dengan satu atau lebih kunci publik Bitcoin tertentu, tanpa memiliki akses ke kunci privat yang bersesuaian.

Jenis aplikasi ini hanya menyimpan data yang diperlukan untuk memantau dompet Bitcoin, termasuk melihat saldo dan riwayat transaksi, tetapi tidak memiliki akses ke kunci privat. Oleh karena itu, mustahil untuk menghabiskan bitcoin yang ada di dompet pada aplikasi watch-only.
![watch-only](assets/en/1.webp)
Watch-only umumnya digunakan bersama dengan dompet perangkat keras. Ini memungkinkan penyimpanan kunci privat dompet secara "dingin," pada perangkat yang tidak terhubung ke internet, yang memiliki permukaan serangan minimal, mengisolasi kunci privat dari lingkungan yang berpotensi rentan. Aplikasi watch-only, di sisi lain, secara eksklusif menyimpan kunci publik yang diperluas (`xpub`, `zpub`, dll.) dari dompet Bitcoin. Kunci induk ini tidak memungkinkan untuk menemukan kunci privat yang terkait dan, akibatnya, tidak memungkinkan pengeluaran bitcoin. Namun, ini memungkinkan untuk derivasi kunci publik anak dan alamat penerima. Dengan mengetahui alamat dompet yang diamankan oleh dompet perangkat keras, aplikasi watch-only dapat melacak transaksi ini di jaringan Bitcoin, menawarkan pengguna kemampuan untuk memantau saldo mereka dan menghasilkan alamat penerima baru, tanpa harus menghubungkan dompet perangkat keras mereka setiap waktu.

## Dompet Watch-Only Mana yang Harus Digunakan?
Saat ini, aplikasi watch-only yang paling komprehensif adalah [Sentinel](https://sentinel.watch/), yang dikembangkan oleh tim di Samourai Wallet. Ini mencakup semua fitur penting untuk dompet watch-only yang baik:
- Dukungan untuk kunci yang diperluas, kunci publik, dan alamat;
- Kemampuan untuk mengorganisir beberapa akun atau dompet ke dalam koleksi;
- Generasi alamat untuk menerima bitcoin pada dompet perangkat keras seseorang tanpa memerlukan penggunaannya secara langsung;
- Kemampuan untuk membangun dan menyiarkan transaksi secara offline;
- Opsi untuk terhubung ke node Bitcoin milik sendiri;
- Integrasi Tor untuk privasi yang ditingkatkan.
Kelemahan unik dari Sentinel terletak pada fakta bahwa aplikasi ini secara eksklusif tersedia untuk Android dan tidak mendukung dompet multi-tanda tangan. Oleh karena itu, jika Anda memiliki perangkat Android dan dompet Anda adalah tanda tangan tunggal klasik, saya merekomendasikan Sentinel.
Bagi mereka yang ingin melacak dompet multi-tanda tangan, Blue Wallet adalah satu-satunya aplikasi yang saya ketahui yang menawarkan mode watch-only untuk jenis dompet ini, dan dapat diakses di Android dan iOS.
Untuk pengguna iOS yang mencari alternatif untuk Sentinel, [Green Wallet](https://blockstream.com/green/) atau [Blue Wallet](https://bluewallet.io/watch-only/) mungkin menjadi pilihan, meskipun fungsionalitas watch-only mereka tidak sekomprehensif Sentinel. ![watch-only](assets/notext/2.webp)
## Bagaimana Cara Menggunakan Dompet Watch-Only Sentinel?
### Instalasi dan Pengaturan
Mulailah dengan menginstal aplikasi Sentinel. Anda dapat melakukan ini baik dari Google Play Store atau dengan menggunakan [APK yang tersedia untuk diunduh di situs web resmi](https://sentinel.watch/download/).

![watch-only](assets/notext/3.webp)

Saat pertama kali membuka aplikasi, Anda diberi pilihan antara:
- `Connect to Dojo`;
- `Connect to Samourai's server`.

Dojo, dikembangkan oleh tim Samourai, adalah versi node Bitcoin penuh yang dapat diinstal secara mandiri atau ditambahkan dalam satu klik ke solusi node-in-box seperti [Umbrel](https://umbrel.com/) dan [RoninDojo](https://ronindojo.io/).

[**-> Temukan cara menginstal RoninDojo v2 di Raspberry Pi.**](https://planb.network/fr/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8)

Jika Anda memiliki Dojo sendiri, Anda dapat menghubungkannya pada tahap ini. Dengan melakukan ini, Anda akan mendapatkan tingkat privasi tertinggi saat memeriksa informasi transaksi jaringan Bitcoin Anda.

![watch-only](assets/notext/4.webp)

Jika tidak, Anda dapat memilih server default Samourai. Anda juga dapat memilih apakah akan terhubung melalui Tor atau tidak.

![watch-only](assets/notext/5.webp)

Anda kemudian akan tiba di halaman utama Sentinel.

![watch-only](assets/notext/6.webp)

Untuk memulai, Anda dapat mengatur aplikasi. Klik pada tiga titik kecil di sudut kanan atas, kemudian pada `Settings`.

![watch-only](assets/notext/7.webp)
Dengan memilih `User PIN code`, Anda memiliki opsi untuk menetapkan kata sandi untuk mengamankan akses ke dompet watch-only Anda. Anda juga memiliki kemampuan untuk mengubah mata uang referensi untuk mengonversi saldo Anda ke mata uang fiat, atau bahkan untuk menyembunyikan nilai fiat dengan mengaktifkan opsi `Hide fiat values`. Untuk keamanan yang lebih tinggi, Anda dapat mengaktifkan `Disable Screenshots`, yang mencegah tangkapan layar aplikasi Sentinel Anda dan dengan demikian menghindari pengungkapan informasi di layar eksternal.
![watch-only](assets/notext/8.webp)

Di menu pengaturan ini, Anda juga memiliki opsi untuk membackup Sentinel Anda.

### Menggunakan Dompet Watch-Only
Dari halaman utama, tekan tombol biru `NEW` untuk menambahkan kunci publik ekstensi baru untuk dilacak. Kemudian Anda memiliki opsi untuk memindai kode QR dari kunci Anda, atau langsung menempelkan kunci (`xpub`, `zpub`...) dengan memilih `Paste Pubkey`.

![watch-only](assets/notext/9.webp)

Umumnya, `xpub` dari dompet Anda dapat diakses langsung melalui perangkat lunak manajemen dompet yang Anda gunakan. Misalnya, jika Anda mengelola dompet perangkat keras Anda dengan Sparrow, informasi ini ditemukan di tab `Settings`, di bawah bagian `Keystore`.

![watch-only](assets/notext/10.webp)
Setelah memasukkan kunci publik terperluas (extended public key) di Sentinel, aplikasi ini menawarkan Anda untuk membuat koleksi baru. Sebuah koleksi mewakili sekumpulan kunci publik terperluas yang disusun bersama. Opsi ini memberi Anda kemungkinan tidak hanya untuk mencantumkan semua `xpubs` Anda, tetapi juga untuk mengklasifikasikannya secara teratur. Misalnya, jika Anda memiliki Samourai Wallet dengan beberapa akun (deposit, premix, postmix...), Anda dapat mengumpulkan semua akun ini di bawah koleksi `Samourai`. Untuk dompet yang dikelola untuk keluarga Anda, Anda mungkin membuat koleksi bernama `Family`.

Pilih `Create new collection`. Kemudian masukkan nama untuk kunci terperluas yang baru saja Anda integrasikan. Misalnya, jika saya memindai akun deposit dari dompet Samourai saya, saya akan menamai kunci ini `Deposit`. Klik pada `SAVE` untuk menyelesaikan.

![watch-only](assets/notext/11.webp)

Selanjutnya, beri nama pada koleksi ini dan tekan ikon validasi yang terletak di pojok kanan atas layar untuk menyimpan koleksi. Koleksi Anda sekarang terlihat di layar utama Sentinel.

![watch-only](assets/notext/12.webp)

Jika Anda ingin menambahkan kunci publik terperluas lainnya, klik pada `NEW` lagi dan masukkan kunci Anda.

![watch-only](assets/notext/13.webp)
Anda kemudian akan diminta untuk memilih koleksi yang ingin Anda integrasikan kunci ini ke dalamnya, atau untuk membuat yang baru. Misalnya, dalam kasus saya, saya telah menyiapkan koleksi khusus untuk dompet Ledger saya.
![watch-only](assets/notext/14.webp)

Untuk melihat kunci terperluas dari sebuah koleksi secara detail, cukup klik pada koleksi tersebut. Anda kemudian dapat menavigasi melalui tab yang berbeda untuk melihat riwayat transaksi.

![watch-only](assets/notext/15.webp)

Dari sebuah koleksi, dengan mengetuk tiga titik kecil di pojok kanan atas, kemudian pada `View Unspent Outputs`, Anda dapat mengakses daftar UTXOs yang dipegang oleh dompet yang dilacak.

![watch-only](assets/notext/16.webp)

### Mengirim dan Menerima Bitcoin dari Sentinel
Seperti halnya dompet hanya-pantau yang baik, Sentinel memungkinkan Anda untuk menghasilkan alamat penerimaan untuk menerima bitcoin pada dompet yang dilacak. Namun, Sentinel juga menawarkan fitur lanjutan lainnya: pembuatan dan penyiaran transaksi Bitcoin yang ditandatangani sebagian (PSBT). Dengan demikian, dompet yang memegang kunci privat dapat menandatangani transaksi ini, yang, setelah ditandatangani, dapat disiarkan di jaringan Bitcoin oleh Sentinel. Mari kita lihat cara melakukan semua ini.

**Perhatian, tidak disarankan untuk menerima bitcoin pada alamat penerimaan yang tidak diverifikasi oleh dompet itu sendiri.** Jika dompet yang memegang kunci privat, seperti dompet perangkat keras, tidak secara eksplisit mengonfirmasi bahwa alamat tertentu berafiliasi dengannya, mengirim bitcoin ke alamat ini adalah praktik berisiko. Memang, tanpa konfirmasi ini, tidak ada jaminan bahwa alamat tersebut benar-benar milik dompet Anda. Oleh karena itu, fungsionalitas penerimaan dari dompet hanya-pantau harus digunakan dengan hati-hati, dengan mempertimbangkan bahwa dana yang dikirim berpotensi hilang.

Untuk menerima bitcoin melalui Sentinel, pilih koleksi yang diminati, kemudian klik pada tab yang sesuai dengan kunci publik terperluas yang ingin Anda transfer dana kepadanya.

![watch-only](assets/notext/17.webp)

Akhirnya, klik pada ikon panah di pojok kiri bawah layar. Sentinel kemudian menghasilkan alamat penerimaan kosong untuk Anda. Anda dapat menyalinnya, atau memindainya menggunakan kode QR.

![watch-only](assets/notext/18.webp)
Untuk menghasilkan PSBT dari Sentinel, dan dengan demikian memulai transaksi pengeluaran, pergilah ke kunci ekstensi dompet dari mana Anda ingin melakukan pembayaran. Mari kita ambil, sebagai contoh, akun deposit saya di dompet Samourai saya. Kemudian klik pada ikon panah yang terletak di bagian bawah kanan layar.
![watch-only](assets/notext/19.webp)

Masukkan semua parameter yang terkait dengan transaksi Anda:
- Masukkan alamat penerima (dengan mengklik ikon kode QR, Anda memiliki opsi untuk memindai alamat ini);
- Tentukan jumlah yang akan dikirim ke alamat ini;
- Tentukan biaya transaksi.

Setelah Anda mengisi semua bidang yang diperlukan untuk transaksi Anda, tekan tombol `COMPOSE UNSIGNED TRANSACTION`.

![watch-only](assets/notext/20.webp)

Anda kemudian akan mengakses PSBT, yang merupakan transaksi Bitcoin yang dibangun tetapi belum ditandatangani, karena Sentinel tidak memiliki akses ke kunci pribadi Anda. Anda memiliki opsi untuk menyalin transaksi ini, mengekspornya sebagai file `.psbt`, atau memindainya melalui kode QR animasi.

![watch-only](assets/notext/21.webp)

Kemudian, pergilah ke dompet Anda yang memiliki kunci pribadi untuk menandatangani transaksi (Samourai, dompet perangkat keras...).

![watch-only](assets/notext/22.webp)

Setelah transaksi ditandatangani, Anda dapat kembali ke Sentinel untuk menyiarkannya. Untuk melakukan ini, dari menu utama, klik pada tiga titik kecil di bagian atas kanan, kemudian pada `Broadcast transaction`.

![watch-only](assets/notext/23.webp)

Anda memiliki opsi untuk memasukkan PSBT yang telah ditandatangani Anda dengan tiga cara berbeda:
- Dengan menempelkannya langsung dari clipboard Anda;
- Dengan mengimpor dari file `.psbt`;
- Dengan memindainya melalui kode QR.

![watch-only](assets/notext/24.webp)

Setelah transaksi yang ditandatangani dimasukkan dalam bingkai abu-abu, Anda dapat mengklik tombol hijau `BROADCAST TRANSACTION` untuk menyiarkannya di jaringan Bitcoin. Sentinel akan memberi Anda TXID-nya.

![watch-only](assets/notext/25.webp)

