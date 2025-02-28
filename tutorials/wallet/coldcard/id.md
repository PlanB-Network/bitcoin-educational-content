---
name: Cold Card

description: Membuat, membackup, dan menggunakan kunci privat Bitcoin dengan perangkat Coldcard dan Bitcoin Core
---

![cover](assets/cover.webp)

Membuat, membackup, dan menggunakan kunci privat Bitcoin dengan perangkat Coldcard dan Bitcoin Core

## Panduan lengkap untuk menghasilkan kunci privat menggunakan Coldcard dan menggunakannya melalui antarmuka node Bitcoin Core Anda!

Di inti penggunaan jaringan Bitcoin terletak konsep kriptografi asimetris: sepasang kunci - satu privat dan satu publik - yang mengenkripsi dan mendekripsi data, sebuah konsep yang menjamin kerahasiaan komunikasi.

Dalam kasus Bitcoin, dengan menghasilkan sepasang kunci privat dan publik tersebut, kita dapat menyimpan bitcoin (UTXO atau Unspent Transaction Output) dan menandatangani transaksi untuk menghabiskannya.

Hari ini, ada banyak alat yang tersedia untuk memfasilitasi generasi acak dari kunci privat dan backupnya dalam bentuk teks menggunakan BIP 39 - standar yang menentukan bagaimana dompet mengasosiasikan frasa mnemonik (frasa benih) dengan kunci enkripsi. Lebih sering daripada tidak, frasa mnemonik terdiri dari 12 atau 24 kata, yang harus di-backup dengan aman agar dapat memulihkan dompet dan bitcoinnya.

Dalam artikel ini, kita akan belajar cara menghasilkan kunci privat menggunakan Coldcard Mk4, salah satu perangkat yang paling banyak digunakan dan aman di dunia Bitcoin, menggunakan metode lemparan dadu untuk memastikan entropi maksimum, dan bagaimana menggunakannya dengan Bitcoin Core secara terisolasi!

> 🧰| Dapatkan alat berikut untuk mengikuti panduan:
>
> - Perangkat Coldcard (Mk3 atau Mk4)
> - Kartu MicroSD (4GB sudah cukup)
> - Kabel USB magnetik hanya untuk daya (mini-usb untuk Mk3, usb-c untuk Mk4)
> - Satu atau lebih dadu berkualitas

## Menghasilkan frasa mnemonik baru dengan Coldcard

Kita akan memulai proses membuat kunci privat dari awal, dengan asumsi Coldcard yang baru dibuka dari kemasannya dan PIN sudah diatur (ikuti langkah-langkah pada Coldcard selama inisialisasi perangkat).

> 🚨 | Untuk mereset kunci privat Coldcard yang sudah dikonfigurasi, ikuti langkah-langkah ini:
> Advanced/Tools > Danger Zone > Seed Functions > Destroy Seed> ✓
> _Perhatian_: Coldcard Anda akan melupakan kunci privat setelah langkah-langkah ini. Pastikan Anda telah membackup frasa mnemonik Anda dengan benar jika Anda ingin dapat memulihkannya nanti.

## Langkah-langkah yang harus diikuti:

Hubungkan ke Coldcard dengan PIN > New Seed Words > 24 Word Dice Roll

Lakukan 100 lemparan dadu, catat hasil yang diperoleh dari 1 hingga 6 pada Coldcard setelah setiap lemparan. Dengan mempraktikkan metode ini, Anda menciptakan 256 byte entropi, sehingga mendukung penciptaan kunci privat yang sepenuhnya acak. Coinkite juga menyediakan dokumentasi yang diperlukan untuk verifikasi independen dari sistem generasi entropi mereka.

![Visual Cold Card Screenshot](assets/guide-agora/1.webp)

Setelah 100 lemparan dadu selesai, tekan ✓ dan kemudian tulis 24 kata yang diperoleh secara berurutan. Verifikasi dua kali dan tekan ✓. Akhirnya, yang tersisa hanyalah menyelesaikan tes verifikasi dari 24 kata pada Coldcard, dan voila, kunci privat baru Anda telah dibuat!

Selanjutnya, pilih apakah akan mengaktifkan fungsi NFC (Mk4) dan USB dengan mengikuti langkah-langkah yang ditampilkan. Setelah berada di menu utama, sekarang saatnya untuk memperbarui firmware perangkat. Pergi ke Advanced/Tools > Upgrade Firmware > Show Version, dan periksa situs resmi untuk memvalidasi dan mengunduh versi terbaru yang tersedia. Disarankan untuk memperbarui Coldcard agar mendapatkan keamanan maksimum.
Sebelum melanjutkan, disarankan untuk mencatat Sidik Jari Kunci Utama (XFP) yang terkait dengan kunci privat. Data ini memungkinkan validasi cepat jika Anda berada di dompet yang benar dalam kasus pemulihan, misalnya. Pergi ke Advanced/Tools > View Identity > Master Key Fingerprint (XFP) dan tuliskan seri delapan karakter alfanumerik yang diperoleh. XFP dapat dicatat di tempat yang sama dengan frasa mnemonik, ini bukan data sensitif.
> 💡 Disarankan untuk menguji cadangan frasa mnemonik Anda di perangkat lunak yang berbeda. Untuk melakukan ini dengan aman, konsultasikan artikel kami Verifikasi cadangan dompet Bitcoin dengan Tails dalam waktu kurang dari 5 menit.

## Bonus Keamanan: "Frasa Rahasia" (opsional)

'Passphrase (frasa rahasia) adalah elemen hebat yang dapat ditambahkan ke konfigurasi dompet untuk menambah lapisan keamanan dalam melindungi bitcoin Anda. Passphrase berfungsi sebagai semacam kata ke-25 untuk frasa mnemonik. Setelah ditambahkan, dompet yang sepenuhnya baru dibuat bersama dengan kunci privat dan frasa mnemonik yang terkait. Tidak perlu menuliskan frasa mnemonik baru, karena dompet ini dapat diakses dengan menggabungkan frasa mnemonik awal dengan passphrase yang dipilih.

Tujuannya adalah untuk mencatat passphrase secara terpisah dari frasa mnemonik karena penyerang yang memiliki akses ke kedua item tersebut akan memiliki akses ke dana. Di sisi lain, penyerang yang hanya memiliki akses ke salah satu item tersebut tidak akan memiliki akses ke dana, dan inilah keuntungan spesifik yang mengoptimalkan tingkat keamanan konfigurasi dompet.

![Menambahkan passphrase mengarah pada dompet yang sepenuhnya berbeda](assets/guide-agora/2.webp)

## Langkah-langkah menambahkan passphrase dengan Coldcard:

Passphrase > Add Words (disarankan) > Apply. Perangkat akan menampilkan XFP dari dompet yang baru dibuat dengan passphrase, yang harus dicatat bersama dengan passphrase untuk alasan yang sama seperti disebutkan sebelumnya.

> 💡 Sumber daya tambahan terkait dengan passphrase:

    https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af
    https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/
    https://armantheparman.com/passphrase/

## Mengekspor dompet ke Bitcoin Core

Dompet sekarang siap untuk diekspor ke perangkat lunak untuk berinteraksi dengan jaringan Bitcoin. Dalam panduan ini, kami akan menggunakan Bitcoin Core (v24.1).

Lihat panduan instalasi dan konfigurasi kami untuk Bitcoin Core:

> Menjalankan node Anda sendiri dengan Bitcoin Core - https://agora256.com/faire-tourner-son-propre-noeud-avec-bitcoin-core/
>
> Mengonfigurasi Tor untuk node Bitcoin Core - https://agora256.com/configuration-tor-bitcoin-core/

Pertama, masukkan kartu micro SD ke dalam Coldcard, kemudian ekspor dompet untuk Bitcoin Core dengan mengikuti langkah-langkah ini: Advanced/Tools > Export Wallet > Bitcoin Core. Dua file akan ditulis ke kartu micro SD: bitcoin-core.sig & bitcoin-core.txt. Masukkan kartu micro SD ke dalam komputer tempat Bitcoin Core diinstal, dan buka file .txt. Anda akan melihat baris "For wallet with master key fingerprint." Verifikasi bahwa sidik jari XFP delapan karakter cocok dengan yang Anda catat saat membuat kunci privat Anda.
Sebelum mengikuti instruksi dalam file, mari kita mulai dengan mempersiapkan dompet di antarmuka Bitcoin Core dengan mengikuti langkah-langkah ini: pergi ke tab File > Buat dompet. Pilih nama untuk dompet Anda (istilah yang dapat dipertukarkan dengan "porte-monnaie" di Core) dan centang opsi Nonaktifkan kunci pribadi, Buat dompet kosong, dan Deskriptor dompet seperti yang ditunjukkan pada gambar di bawah ini. Kemudian, tekan tombol Buat.
![buat dompet](assets/guide-agora/3.webp)

Setelah dompet dibuat di Bitcoin Core, pergi ke tab Window > Konsol dan pastikan bahwa dompet yang dipilih di bagian atas halaman menampilkan nama dari yang Anda buat.

Sekarang, di file .txt yang dihasilkan oleh Coldcard sebelumnya, salin baris yang dimulai dengan importdescriptors, lalu tempelkan ke konsol Bitcoin Core. Sebuah respons termasuk baris "success": true seharusnya dikembalikan.

![jendela node](assets/guide-agora/4.webp)

Jika respons berisi "message": "Ranged descriptors should not have a label", hapus entri "label": "Coldcard xxxx0000" dalam baris yang disalin dari file .txt, lalu tempelkan kembali baris lengkapnya ke konsol Bitcoin Core.

Bantuan: [https://github.com/Coldcard/firmware/blob/master/docs/bitcoin-core-usage.md](https://github.com/Coldcard/firmware/blob/master/docs/bitcoin-core-usage.md)

## Validasi impor dompet di Bitcoin Core

Untuk memastikan bahwa operasi berhasil, perlu untuk memvalidasi bahwa dompet yang diinginkan telah diimpor ke Bitcoin Core. Metode sederhana untuk mengonfirmasi ini adalah dengan memverifikasi bahwa alamat yang dihasilkan di Coldcard sesuai dengan alamat yang dihasilkan di Bitcoin Core.

Bitcoin Core: Terima > Buat alamat penerimaan baru
Coldcard: Penjelajah Alamat > Pilih alamat yang dimulai dengan bc1q. Alamat Coldcard 'bc1q' harus cocok dengan alamat yang ditampilkan di Bitcoin Core.
Menerima dan mengirim transaksi dalam mode 'air-gapped'

Menerima transaksi sangat sederhana; cukup tekan Terima, labeli transaksi (opsional tapi disarankan), dan Buat alamat penerimaan baru. Kemudian, yang tersisa hanyalah berbagi alamat dengan pengirim.

Sekarang, elemen kunci dari pengaturan Coldcard + Bitcoin Core ini adalah mengirim transaksi tanpa Coldcard dan kunci pribadinya terhubung ke internet, sebuah metode yang disebut air-gapped yang menggunakan fungsi TBSP (PSBT - Partially Signed Bitcoin Transactions) dari Bitcoin.
Pada dasarnya, kita menggunakan antarmuka Bitcoin Core untuk membangun transaksi, yang kemudian akan kita ekspor melalui kartu micro SD ke Coldcard untuk ditandatangani, dan kemudian mengembalikan file transaksi yang telah ditandatangani ke Bitcoin Core dan menyiarkan transaksi ke jaringan. Kita harus melakukannya dengan cara ini karena dompet yang diimpor ke Bitcoin Core tidak memiliki kunci pribadi, hanya kunci publik (yang memungkinkan kita untuk menghasilkan alamat penerimaan kita), sehingga tidak mungkin bagi kita untuk menandatangani transaksi langsung di perangkat lunak untuk menghabiskan bitcoin kita.

Sebelum melanjutkan, pastikan opsi berikut diaktifkan di Pengaturan > Dompet:

> - Aktifkan fitur kontrol koin
> - Habiskan koin yang belum dikonfirmasi (Opsional)
> - Aktifkan pemeriksaan TBPS

![opsi](assets/guide-agora/5.webp)

### Langkah-langkah untuk mengirim dalam mode air-gapped:
Kirim > Input > pilih utxo yang diinginkan, kemudian masukkan alamat penerima di Bagian Bayar ke. Biaya transaksi: Pilih... > Kustom > Masukkan biaya transaksi (Bitcoin Core menghitung dalam sats/kilobyte bukan sat/byte seperti kebanyakan solusi dompet alternatif. Jadi, 4000 sats/kilobyte = 4 sats/byte). Buat transaksi yang belum ditandatangani > simpan file ke kartu micro SD Anda dan masukkan ke dalam Coldcard.
Di Coldcard, tekan Siap untuk menandatangani, verifikasi detail transaksi, kemudian tekan ✓ dan masukkan kembali kartu micro SD ke dalam komputer setelah file yang ditandatangani tercipta.

Kembali di Bitcoin Core, pergi ke tab File > Muat TBSP dari file, dan masukkan file transaksi yang telah ditandatangani .psbt. Kotak Operasi PSBT akan muncul di layar, mengonfirmasi bahwa transaksi telah sepenuhnya ditandatangani dan siap untuk disiarkan. Yang tersisa hanyalah menekan Siarkan transaksi.

![Operasi PSBT](assets/guide-agora/6.webp)

### Kesimpulan

Kombinasi perangkat Coldcard dengan Bitcoin Core, di mana Anda menjalankan node Anda sendiri, sangat kuat. Tambahkan kunci privat yang dihasilkan dengan 100 lemparan dadu dan frasa rahasia, dan konfigurasi dompet Anda menjadi benteng yang canggih dan kuat.

Jangan ragu untuk menghubungi kami untuk berbagi komentar dan pertanyaan Anda! Tujuan kami adalah berbagi pengetahuan dan meningkatkan pemahaman kita dari hari ke hari.