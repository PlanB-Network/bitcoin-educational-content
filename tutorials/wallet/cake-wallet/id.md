---
name: Cake Wallet
description: Tutorial tentang Cake Wallet dan Pembayaran Diam
---

![cover](assets/cover.webp)


Panduan ini membahas [**Cake Wallet**] (https://cakewallet.com/): sebuah sumber terbuka, non-kustodian, multi-mata uang yang berfokus pada privasi yang tersedia untuk Android, iOS, macOS, Linux, dan Windows. Kita akan menyelami fitur privasi khusus Bitcoin, membahas pengiriman/penerimaan Bitcoin melalui **Silent Payments** (protokol privasi on-chain yang telah disempurnakan) dan akan melihat implementasi PayJoin v2 untuk transaksi asinkron.


## 🎉 Fitur Utama



- [**Pembayaran Senyap (BIP-352)**] (https://bips.dev/352/) meningkatkan kode pembayaran [BIP 47 sebelumnya] (https://silentpayments.xyz/docs/comparing-proposals/bip47/) yang juga disebut "PayNyms" dengan alamat siluman yang dapat digunakan kembali. Ketika pengirim menggunakan alamat Silent Payment Anda, wallet mereka akan mendapatkan alamat satu kali yang unik menggunakan kunci yang berbeda yang akan digabungkan ke dalam alamat satu kali Taproot yang unik. Catatan blockchain menunjukkan transaksi yang tidak terkait, mencegah keterkaitan pembayaran yang masuk. Silent Payment menawarkan berbagai manfaat, termasuk:
    - Alamat yang dapat digunakan kembali: Tidak perlu membuat alamat baru untuk setiap transaksi, memberikan pengalaman pengguna yang lebih baik dan meningkatkan privasi
    - Tidak ada kenaikan biaya: Pembayaran Senyap tidak meningkatkan ukuran atau biaya transaksi.
    - Anonimitas yang ditingkatkan: Pengamat dari luar tidak dapat menautkan transaksi ke alamat Pembayaran Senyap.
    - Tidak diperlukan interaksi pengirim-penerima: Transaksi dapat dilakukan tanpa komunikasi apa pun di antara kedua belah pihak.
    - Alamat unik untuk setiap pembayaran: Menghilangkan risiko penggunaan ulang alamat yang tidak disengaja.
    - Tidak memerlukan server: Pembayaran Senyap dapat dilakukan tanpa memerlukan server khusus.
- PayJoin v2** memitigasi analisis grafik transaksi dengan menggabungkan input dari pengirim dan penerima ke dalam satu transaksi. Cake Wallet mengimplementasikan dua kemajuan penting:
    - Transaksi Asinkron**: Pengirim dan penerima tidak perlu lagi online secara bersamaan untuk menyelesaikan transaksi pribadi.
    - Komunikasi Tanpa Server**: Kedua belah pihak tidak perlu menjalankan server Payjoin, sehingga menghilangkan hambatan teknis utama.
- Kontrol Coin** memungkinkan pemilihan UTXO secara manual selama transaksi. Hal ini mencegah penautan alamat yang tidak disengaja ketika membelanjakan beberapa UTXO dengan asal yang berbeda.
- Dukungan TOR**, memungkinkan pengguna untuk merutekan lalu lintas jaringan mereka melalui jaringan Tor
- RBF** (Ganti-Berdasarkan.Biaya) memungkinkan Anda menyesuaikan biaya setelah mengirim transaksi.


## 1️⃣ Menyiapkan Wallet Anda


Cake Wallet menawarkan berbagai macam dukungan platform. Anda dapat memilih antara `Android`, `iOS / macOS`, `Linux` dan `Windows`.  Untuk memulai, kunjungi https://docs.cakewallet.com/get-started/ dan pilih sistem operasi Anda.


![image](assets/en/01.webp)


Setelah pemasangan, tetapkan `PIN` (4 atau 6 digit). Anda kemudian akan melihat:


1. `Buat Wallet Baru` (untuk pengguna baru)

2. `Kembalikan Wallet` (untuk dompet yang ada)


![image](assets/en/02.webp)


Pada layar berikutnya, Anda dapat memilih dari berbagai macam mata uang kripto. Pilih `Bitcoin` dan ketuk `Next` dan berikan `Nama Wallet` untuk mengidentifikasi wallet. Dengan mengetuk `Pengaturan Lanjutan`, akan muncul serangkaian `Pengaturan Privasi`. Lakukan perubahan ini:



- Fiat API:** pilih `Hanya Tor` (rute permintaan harga melalui Tor)
- Tukar:** pilih `Tor Only` (menganonimkan lalu lintas pertukaran)


Tipe BIP-39 seed dihasilkan secara default, dengan opsi untuk mengubah ke tipe Electrum seed. Jalur Derivasi adalah sebagai berikut:



- Electrum: `m/0'`
- BIP-39: `m/84'/0'/0`


Jika Anda ingin menambahkan lapisan keamanan tambahan, Anda dapat mengatur `passphrase`.  Tujuan utama dari passphrase adalah untuk memberikan perlindungan tambahan terhadap serangan fisik. Bahkan jika penyerang menemukan frasa seed, mereka tidak dapat mengakses wallet Anda tanpa passphrase yang benar. Dengan kata lain, frasa seed sendiri mewakili satu wallet, sedangkan frasa seed ditambah passphrase menciptakan wallet yang sama sekali berbeda tanpa ada hubungannya dengan yang asli. Fitur ini juga memungkinkan `dompet rahasia` yang dilindungi oleh passphrase, dan memberi Anda penyangkalan yang masuk akal. Dalam situasi yang memaksa, Anda dapat mengungkapkan frasa seed sambil menjaga aset yang lebih besar tetap aman dalam wallet yang dilindungi passphrase.


Jika Anda sudah menjalankan node Anda sendiri, pilih `Tambahkan Node Kustom Baru` dan berikan `Node Address` untuk memvalidasi transaksi dan blok di dalam infrastruktur Anda. Setelah selesai, tekan `Lanjutkan` dan `Next` untuk membuat wallet Anda.


![image](assets/en/03.webp)


Pada layar berikutnya, Anda akan mendapatkan disclaimer:


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Untuk mempelajari praktik terbaik dalam menyimpan frasa mnemonik Anda, silakan baca tutorial ini:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ketuk `Saya mengerti. Tunjukkan seed saya dan simpan kata-kata ini di tempat yang aman! Kemudian ketuk `Verifikasi seed` dan setelah verifikasi `Buka Wallet`.


## 2️⃣ Pengaturan


Sebelum kita menyelam lebih dalam, mari kita lihat `Home Screen` dan `Settings`.


Pada Layar Awal, kita dapat melihat berbagai item yang ditampilkan:



- `Menu Hamburger` membawa kita ke `pengaturan`
- Saldo yang tersedia
- Kartu Pembayaran Senyap untuk Mulai memindai transaksi yang dikirim ke alamat Pembayaran Senyap Anda
- Kartu Payjoin untuk `Mengaktifkan` Payjoin sebagai fitur yang menjaga privasi dan menghemat biaya
- di bagian bawah adalah Pintasan ke `Wallet Ikhtisar`, `Menerima`, `Menukar` antara Bitcoin dan mata uang lainnya, `Mengirim` dan `Membeli`


![image](assets/en/11.webp)


Mengetuk ikon `Menu hamburger` akan membuka menu pengaturan. Mari kita tinjau pilihannya.


![image](assets/en/05.webp)


### A - Koneksi & sinkronisasi 🔗


Di sini, kita bisa menghubungkan kembali wallet, mengelola node, dan menghubungkan ke node kita sendiri (disarankan). Pemindaian Pembayaran Diam memungkinkan kita menyesuaikan pemindaian dengan menentukan `Pindai dari tinggi blok` atau `Pindai dari tanggal`.


![image](assets/en/06.webp)


Sebagai fitur `Alpha`, ada juga pilihan untuk `Enable built-in Tor` untuk merutekan lalu lintas melalui jaringan Tor.


### B - Pengaturan Pembayaran Senyap 🔈


Kita dapat mengaktifkan kartu Silent Payments pada layar Beranda untuk menampilkan fitur ini. Mengaktifkan `Selalu memindai` memungkinkan wallet untuk terus memantau blockchain untuk Pembayaran Senyap yang masuk. Kita dapat menentukan parameter pemindaian untuk menyesuaikan proses pemindaian dengan kebutuhan kita seperti yang dijelaskan di atas.


![image](assets/en/07.webp)


### C - Keamanan & pencadangan 🗝️


Untuk mengamankan wallet kita, kita dapat membuat cadangan dengan mengikuti petunjuk dalam aplikasi. Hal ini akan memastikan bahwa kita memiliki salinan kunci pribadi yang aman, sehingga kita dapat memulihkan wallet jika hilang atau dicuri. Selain itu, kita bisa melihat frasa seed dan kunci pribadi kita, mengubah PIN kita, mengaktifkan otentikasi biometrik, Sign/Verifikasi dan mengatur 2FA untuk lapisan perlindungan ekstra.


![image](assets/en/08.webp)


**Catatan**: Mulai September 2025, autentikasi biometrik sidik jari pada perangkat Android diharuskan berfungsi dengan setidaknya implementasi biometrik Kelas 2, untuk detail lebih lanjut, lihat [di sini] (https://source.android.com/docs/security/features/biometric/measure#biometric-classes). Namun, persyaratan ini dapat berubah di masa mendatang.


### D - Pengaturan Privasi 🔒


Kita juga dapat meningkatkan keamanan wallet kita dengan menggunakan Tor untuk mengenkripsi koneksi internet kita dan menjaga privasi kita saat mengakses sumber eksternal. Selain itu, kita dapat mencegah tangkapan layar untuk menjaga kerahasiaan informasi wallet kita, mengaktifkan alamat yang dibuat secara otomatis untuk membuat alamat baru untuk setiap transaksi, dan menonaktifkan tindakan jual/beli untuk mencegah transaksi yang tidak sah. Selain itu, kita dapat `Mengaktifkan PayJoin`, yang merupakan fitur privasi lain yang akan kita ulas nanti.


![image](assets/en/09.webp)


### E - Pengaturan lainnya 🔧


Pengaturan lainnya memungkinkan kami untuk mengelola prioritas biaya dan menetapkan tingkat biaya default untuk transaksi kami. Hal ini memungkinkan kami untuk mengontrol biaya transaksi yang terkait dengan Pembayaran Senyap, dengan mempertimbangkan pemanfaatan jaringan saat ini.


![image](assets/en/10.webp)


## 3️⃣ Menerima ₿itcoin menggunakan Pembayaran Senyap


Ada beberapa pilihan dan jenis alamat yang tersedia untuk menerima Bitcoin. `Segwit (P2WPKH)` *(dimulai dengan bc1q....)* adalah opsi default.  Mari kita pilih `Pembayaran Diam` dalam contoh ini.


Untuk menerima Pembayaran Diam, pertama-tama ketuk ikon `Terima` di Cake Wallet. Selanjutnya, masukkan jumlah yang ingin Anda terima. Untuk menentukan jenis alamat, ketuk `Terima` sekali lagi di bagian atas layar, lalu pilih `Pembayaran Senyap` dari pilihan.


Pada layar utama, kode QR dan alamat Silent Payment Anda yang dapat digunakan kembali akan ditampilkan. Seperti yang diharapkan, alamatnya cukup panjang:


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


Sekarang, gunakan wallet yang kompatibel dengan BIP-352 (seperti Wallet Biru) untuk memindai kode QR ini dan mengirim pembayaran. Anda akan melihat bahwa wallet akan mendapatkan alamat tujuan yang unik dari alamat diam Anda.


![image](assets/en/13.webp)


## 4️⃣ Mengirim ₿itcoin menggunakan Pembayaran Senyap


Karena Blue Wallet hanya dapat `Mengirim` Pembayaran Diam, kami akan menggunakan BIP 352 yang kompatibel dengan wallet lain sebagai pihak penerima. Proses ini sama dengan proses transaksi Bitcoin biasa.



- Ketuk `Kirim` pada Layar Awal
- baik dengan menempelkan alamat `sp1qq... ` yang dapat digunakan kembali atau memindai kode QR secara langsung di dalam aplikasi.
- Pilih jumlah yang ingin Anda belanjakan dari saldo yang tersedia
- Ketuk `Kirim` di bagian bawah layar untuk mengonfirmasi transaksi


Setelah kita memasukkan alamat `sp1qq...`, wallet secara otomatis mendapatkan alamat `bc1p...` Taproot (P2TR) di latar belakang, yang akan digunakan untuk Pembayaran Diam.


Secara opsional, kami dapat menulis catatan internal untuk setiap transaksi, menyesuaikan pengaturan biaya, atau memilih UTXO tertentu untuk transaksi menggunakan fitur `Coin Control`.


![image](assets/en/14.webp)


geser ke kanan untuk mengonfirmasi transaksi.


Setelah Anda mengirimkan transaksi, Anda akan ditanya apakah Anda ingin menambahkan kontak ini ke buku alamat Anda.


![image](assets/en/15.webp)


## 5️⃣ PayJoin


Mari kita tinjau kembali apa itu PayJoin (https://docs.cakewallet.com/cryptos/bitcoin/#payjoin):


_Payjoin v2 adalah fitur yang menjaga privasi dan penghematan biaya di Bitcoin yang memungkinkan pengirim dan penerima transaksi untuk bekerja sama untuk membuat satu transaksi. Transaksi ini memiliki input dari *kedua* pengirim dan penerima, mematahkan teknik pengawasan yang paling umum terhadap Bitcoin dan memungkinkan penskalaan yang lebih baik dan penghematan biaya dalam beberapa situasi


Untuk mengetahui lebih lanjut tentang PayJoin, Anda juga dapat mengunjungi tutorial berikut ini.


https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

Untuk menggunakan PayJoin, kedua belah pihak memerlukan wallet yang kompatibel dengan PayJoin, dan penerima harus memiliki setidaknya satu koin atau output dalam wallet mereka. Untuk memulai, silakan ikuti langkah-langkah berikut:


1. Ketuk `Menu Hamburger` dan ketuk tombol `Privasi`

2. Alihkan Opsi `Gunakan Payjoin`

3.  Ketuk `Terima` pada layar Beranda dan Anda akan disajikan dengan Kode QR PayJoin dan tombol salin (ketika memilih Segwit)


![image](assets/en/16.webp)


## 6️⃣ Fitur lainnya


Ada beberapa fitur lain seperti `Swap` multi mata uang, opsi `Beli dan Jual` dengan koneksi vendor yang berbeda dan program khusus Cake seperti `Cake Pay`, yang memungkinkan Anda membeli kartu prabayar atau kartu hadiah.


![image](assets/en/17.webp)


## 🎯 Kesimpulan


Ini adalah ulasan kami tentang Cake Wallet, yang menawarkan privasi Bitcoin yang praktis berkat fitur-fitur seperti Pembayaran Senyap (BIP-352) dan Payjoin v2.


Silent Payments menggantikan alamat sekali pakai dengan alamat siluman yang dapat digunakan kembali untuk mencegah hubungan on-chain dari transaksi yang masuk. Meskipun masalah sinkronisasi dari versi sebelumnya telah diperbaiki, ada beberapa peningkatan persyaratan komputasi untuk memindai dan mendeteksi Pembayaran Diam yang diperlukan, yang menuntut lebih banyak sumber daya dan bandwidth.


Payjoin v2 mengganggu analisis rantai dengan menggabungkan input pengirim dan penerima ke dalam satu transaksi tanpa biaya tambahan atau koordinasi pusat. Hal ini mematahkan heuristik kepemilikan input yang umum, yang merupakan keuntungan yang signifikan karena ini berarti Anda tidak dapat mengasumsikan bahwa semua input adalah milik pengirim.


Bagi pengguna yang memprioritaskan anonimitas keuangan, Cake Wallet adalah pilihan yang layak. Ini menggabungkan protokol privasi secara langsung ke dalam fungsionalitas intinya, membuatnya dapat diakses tanpa kerumitan teknis. Seiring dengan meningkatnya pengawasan pada blockchain publik, alat seperti ini membantu menjaga privasi transaksional di tempat yang paling penting. Implementasi yang lebih luas dari standar-standar ini dalam lanskap wallet akan menjadi perkembangan yang disambut baik.


## 📚 Sumber Daya


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://bips.dev/352/](https://bips.dev/352/)


https://payjoin.org/