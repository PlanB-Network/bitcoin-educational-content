---
name: Green Wallet

description: Panduan Pengaturan dan Penggunaan (CC Bistack)
---

![cover](assets/cover.webp)

Dompet Seluler Panas - Pemula - Gratis - Untuk mengamankan dari 0 hingga 1.000 €

Untuk mengamankan jumlah di bawah 1.000€, dompet panas gratis (terhubung ke internet) sangat cocok untuk pemula. Pengaturannya mudah dan antarmukanya dirancang untuk pemula.

Jika Anda ingin mengunjungi situs web mereka, klik di sini (https://blockstream.com/green/)!

## Video Tutorial

![video tutorial green wallet](https://www.youtube.com/watch?v=lONbCS31am4)

## Tutorial Tertulis

> Panduan ini diproduksi dan dimiliki oleh Bitstack. Bitstack adalah neo bank bitcoin yang berbasis di Paris yang memungkinkan DCA pada bitcoin. Panduan ditulis oleh Loic Morel pada 15/02/2023. Ini milik mereka. https://www.bitstack-app.com/blog/installer-portefeuille-bitcoin-green-wallet

![image](assets/0.webp)

Bagaimana Cara Menginstal Dompet Bitcoin Pertama Anda? Tutorial Green Wallet

Jika Anda ingin mendapatkan banyak keuntungan dari sistem Bitcoin, termasuk ketidakmampuan sensor dan ketidakmampuan penyitaan dana Anda, Anda harus secara pribadi menyimpan kunci yang memberi akses ke bitcoin Anda.

Dalam tutorial ini, saya akan menjelaskan cara mengatur dompet pertama Anda dengan Green Wallet. Perangkat lunak ini sangat cocok untuk pengguna pemula. Sangat mudah digunakan, bahkan jika Anda tidak memiliki pengetahuan lanjutan tentang Bitcoin.

Green Wallet tersedia di semua jenis perangkat. Dalam tutorial ini, kita akan melihat cara menggunakannya di ponsel, tetapi Anda juga dapat mengunduhnya di komputer.

Langkah pertama adalah tentu saja mengunduh perangkat lunak atau aplikasi Green Wallet. Jika Anda di ponsel, Anda dapat dengan mudah mengunduhnya dari toko Anda. Pastikan Anda berada di halaman unduhan aplikasi resmi. Berikut adalah halaman tergantung pada sistem Anda:

> - Google Play Store
>
> - Apple App Store

Jika Anda mengunduh perangkat lunak di komputer, saya sangat menyarankan Anda untuk memverifikasi keaslian dan integritas biner sebelum menginstalnya di mesin Anda. Saya akan menjelaskan cara melakukan operasi ini dalam tutorial mendatang.

## Memilih Pengaturan Aplikasi

Saat meluncurkan aplikasi, Anda akan tiba di layar beranda. Saat ini, Anda tidak memiliki dompet. Nanti, jika Anda telah membuat beberapa dompet, Anda dapat menemukannya di sini.

Tindakan pertama yang harus diambil sebelum membuat dompet Anda adalah membuka pengaturan aplikasi untuk memilih yang paling cocok untuk Anda.

![image](assets/1.webp)

- "Enhanced Privacy" memungkinkan Anda untuk menonaktifkan kemampuan mengambil tangkapan layar pada aplikasi. Opsi ini juga akan menyembunyikan pratinjau dan secara otomatis mengamankan aplikasi saat Anda mengunci ponsel Anda. Opsi ini hanya tersedia di Android;
- Anda kemudian dapat memilih untuk merutekan lalu lintas Anda melalui Tor sehingga semua koneksi Anda dienkripsi. Ini sedikit memperlambat operasi aplikasi Anda, tetapi saya menyarankan mengaktifkannya untuk menjaga privasi Anda;

- Opsi "Testnet" memungkinkan Anda untuk membuat dompet di Testnet. Ini adalah jaringan yang bertindak persis seperti sistem Bitcoin, kecuali bahwa bitcoin yang ditukar di dalamnya sama sekali tidak memiliki nilai. Jaringan Testnet terpisah ini disukai oleh pengguna atau pengembang yang ingin menguji aplikasi tanpa mengambil risiko keuangan. Jika Anda ingin menggunakan Green Wallet pada sistem Bitcoin yang sebenarnya, Anda dapat meninggalkan opsi ini tidak dicentang;

- Opsi "Help Green" memungkinkan Anda untuk mengirimkan informasi rahasia ke Blockstream sehingga mereka dapat meningkatkan aplikasi mereka;

- Opsi "Personal Electrum Server" memungkinkan Anda untuk menghubungkan node Bitcoin jarak jauh Anda sendiri untuk memiliki akses ke informasi jaringan dan menyiarkan transaksi Anda;
- Opsi "Verifikasi SPV" memungkinkan Anda untuk mengunduh dan memverifikasi informasi tertentu dari Blockchain secara mandiri. Ini mengurangi kebutuhan untuk mempercayai node Blockstream. Harap dicatat bahwa opsi ini tidak memberikan semua jaminan dari node Bitcoin yang sebenarnya, tetapi jika Anda tidak memilikinya, ini bisa menjadi opsi yang baik untuk diaktifkan.
Setelah Anda memilih pengaturan Anda, Anda dapat mengklik tombol "Simpan" dan kemudian memulai ulang aplikasi Anda.

## Membuat Dompet Bitcoin

Langkah selanjutnya adalah membuat dompet Bitcoin Anda. Untuk melakukan ini, klik pada:

> - Tambah dompet;
> - Dompet baru;
> - Bitcoin.

![image](assets/3.webp)

Opsi "Pulihkan dompet" memungkinkan Anda untuk mendapatkan kembali akses ke dompet yang sudah ada menggunakan frasa mnemoniknya. Opsi "Dompet Hanya-Lihat" memungkinkan Anda untuk mengimpor kunci publik yang diperluas (xpub) untuk melihat pergerakan dompet tanpa dapat menghabiskan dananya.

> "Dompet Hanya-Lihat sangat berguna jika Anda memiliki dompet perangkat keras. Anda dapat mengimpor xpub ke ponsel Anda untuk membuat alamat penerimaan dan melacak saldo dompet yang dihosting di dompet perangkat keras."
> Opsi jaringan memungkinkan Anda untuk menghubungkan dompet Anda ke sistem yang berbeda. Jaringan "Liquid" adalah sidechain Bitcoin. Jaringan "Testnet" adalah salinan dari jaringan Bitcoin, tetapi dengan bitcoin yang tidak memiliki nilai. Akhirnya, jaringan "Testnet Liquid" adalah setara dengan Testnet untuk sidechain Liquid. Dalam tutorial ini, kita hanya ingin membuat dompet Bitcoin, jadi kita memilih jaringan "Bitcoin".

Selanjutnya, Anda akan ditanya jenis dompet apa yang ingin Anda buat. Opsi termudah adalah membuat dompet "Single Sig". Dalam kasus ini, setiap UTXO (potongan bitcoin) yang milik kita hanya akan dikunci oleh satu pasangan kunci.

Pilih "Tanda Tangan Tunggal".

Anda kemudian dapat memilih untuk memiliki frasa mnemonik 12 kata atau 24 kata. Frasa ini akan memungkinkan Anda untuk memulihkan akses ke dompet Anda dari perangkat lunak apa pun yang kompatibel dalam kasus kehilangan, pencurian, atau kerusakan pada ponsel Anda.

Frasa 24 kata lebih aman dari serangan brute force dibandingkan dengan frasa 12 kata. Namun, saat ini, frasa 12 kata masih cukup aman. Dalam praktiknya, jika Anda memilih frasa 12 kata, Anda akan berada di atas batas minimum yang direkomendasikan oleh NIST. Ini berarti bahwa frasa Anda aman hari ini, tetapi mungkin tidak di masa depan karena kemajuan dalam komputasi (kecuali Anda juga menggunakan passphrase BIP39). Secara default, saya merekomendasikan memilih frasa 24 kata, tetapi terserah Anda untuk membuat pilihan Anda sendiri.

![image](assets/6.webp)

Perangkat lunak kemudian akan memberikan Anda frasa pemulihan Anda. Anda harus menyimpannya dengan benar dengan menuliskannya pada media fisik yang sesuai. Sangat disarankan untuk tidak menyimpan frasa ini pada media digital, bahkan jika dienkripsi. Sebaiknya ditulis di atas kertas atau logam tergantung pada nilai yang disimpan.

Frasa ini sangat penting karena memungkinkan akses ke kunci dompet Anda tanpa batasan. Jika Anda kehilangannya, Anda tidak akan lagi dapat mengakses bitcoin Anda jika ponsel Anda berhenti bekerja. Jika frasa mnemonik ini dicuri, penyerang dapat mencuri semua dana Anda secara tidak dapat dibalikkan.

Kata-kata dalam frasa ini harus ditulis bersama-sama. Jangan pisahkan frasa Anda! Selain itu, juga penting untuk menuliskan setiap kata dalam urutan yang ditentukan, bersama dengan nomornya. Frasa yang tidak teratur tidak berguna.

Untuk mempelajari lebih lanjut tentang mengamankan frasa pemulihan, saya sangat merekomendasikan membaca artikel khusus saya tentang topik ini.

![image](assets/7.webp)
Green Wallet kemudian meminta Anda untuk mengonfirmasi beberapa kata dari frasa Anda untuk memastikan bahwa Anda telah menuliskannya dengan benar.
![image](assets/10.webp)

Anda kemudian dapat memilih nama untuk dompet Anda untuk membedakannya dari yang lain jika Anda membuat beberapa dompet nanti. Pada tahap ini, nama tidak penting karena kita akan menghapus dompet ini untuk memverifikasi validitas frasa mnemonik pada langkah selanjutnya.

Anda juga diminta untuk menetapkan PIN. PIN ini digunakan untuk mengunci akses ke dompet Anda. Disarankan untuk menetapkan kata sandi yang kompleks dan acak, terutama untuk melindungi dompet Anda dalam kasus ponsel Anda dicuri.

PIN ini tidak ada hubungannya dengan dompet Bitcoin itu sendiri. Sebenarnya, hanya dengan frasa pemulihan, Anda akan dapat mendapatkan kembali akses ke semua bitcoin Anda. PIN hanya menghalangi akses ke dompet Anda di ponsel Anda. Oleh karena itu, mencadangkan frasa tersebut jauh lebih penting daripada mencadangkan PIN ini.

Anda dapat menambahkan opsi kunci biometrik nanti untuk menghindari memasukkan PIN setiap kali Anda menggunakannya. Secara umum, biometrik jauh kurang aman daripada PIN itu sendiri. Dengan demikian, secara default, saya menyarankan melawan penerapan opsi pembukaan ini.

Anda harus memasukkan PIN yang dipilih untuk kedua kalinya di aplikasi Green untuk mengonfirmasinya.

![image](assets/12.webp)

Selamat! Anda telah menyelesaikan pembuatan dompet Bitcoin Anda.

![image](assets/14.webp)

Jika Anda ingin menambahkan frasa sandi BIP39 ke dompet Bitcoin ini, Anda harus mengklik tiga titik di pojok kanan atas layar saat memasukkan PIN Anda untuk membuka kunci dompet. Hati-hati, saya sangat menyarankan melawan penggunaan frasa sandi jika Anda tidak memahami mekanisme derivasi yang bermain. Anda bisa kehilangan akses ke bitcoin Anda.

## Simulasi pemulihan dompet Bitcoin Anda

Sebelum mengirim bitcoin ke dompet baru Anda, sangat penting untuk melakukan tes pemulihan untuk memastikan bahwa cadangan frasa mnemonik Anda berfungsi. Dalam praktiknya, kita akan menghapus dompet sementara masih kosong dan mencoba memulihkannya hanya menggunakan frasa pemulihan, seolah-olah kita telah kehilangan akses ke ponsel kita.

Selain memverifikasi validitas frasa, praktik ini juga memungkinkan Anda untuk berlatih memulihkan dompet Bitcoin. Jadi, jika Anda pernah menemukan diri Anda dalam situasi darurat, Anda akan tahu persis langkah apa yang harus diambil untuk mendapatkan kembali akses ke dana Anda.

Untuk melakukan ini, sebelum menghapus dompet Anda, Anda harus mengambil informasi referensi yang akan memungkinkan Anda untuk mengenalinya nanti. Oleh karena itu, Anda akan menyalin 8 karakter terakhir dari alamat pertama yang diusulkan kepada Anda.
Untuk mengakses informasi ini, klik tombol "Receive". Dompet akan menampilkan alamat. Tulis 8 karakter terakhir dari alamat pada selembar kertas terpisah. Ini sesuai dengan checksum alamat.

Misalnya, pada dompet saya, 8 karakter yang harus dicatat adalah: JTbP4482.

![image](assets/16.webp)

Setelah Anda mencatat informasi ini, Anda dapat menghapus dompet Anda. Dari layar utama dompet, klik pada ikon pengaturan, lalu klik pada "Disconnect".

> "Saya ingin menekankan sekali lagi bahwa operasi ini harus dilakukan dengan dompet yang kosong, sebelum mengirim bitcoin apa pun ke dalamnya. Jika tidak, Anda berisiko kehilangan mereka."

![image](assets/19.webp)

Anda kemudian akan dibawa ke layar pembukaan kunci dompet. Klik pada tiga titik di pojok kanan atas layar, lalu klik pada "Delete Wallet", dan konfirmasi.

![image](assets/21.webp)
Anda sekarang berada di layar utama aplikasi Green Wallet, dan tidak ada dompet yang tersedia. Anda saat ini berada dalam situasi yang sama seperti jika Anda kehilangan atau merusak ponsel Anda dan mencoba memulihkan dompet Anda hanya dari frasa mnemonik.

Sekarang klik pada "Tambah Dompet", kemudian "Pulihkan Dompet", dan akhirnya "Bitcoin".

![image](assets/23.webp)

Kemudian, perangkat lunak akan menanyakan apakah kita ingin memulihkan dari kode QR atau dari frasa mnemonik. Dalam kasus kita, itu adalah frasa.

Selanjutnya, kita diminta untuk memasukkan frasa pemulihan. Ini adalah frasa yang kita tulis saat membuat dompet. Jika Anda menggunakan frasa 24 kata, ingat untuk mengklik kotak kecil "24".

Setelah semua kata dimasukkan, jika perangkat lunak memberitahu Anda ada kesalahan, itu berarti checksum dari frasa Anda salah. Dalam kasus ini, itu berarti cadangan kertas dari frasa mnemonik Anda tidak valid. Anda harus memulai tutorial ini lagi dari awal dan pastikan untuk menuliskan frasa dengan benar saat diberikan kepada Anda.

Jika tidak, Anda dapat mengklik "Lanjutkan".

![image](assets/26.webp)

Perangkat lunak akan menunjukkan "Dompet tidak ditemukan". Ini sepenuhnya normal karena, untuk saat ini, kita belum mengirimkan bitcoin apa pun ke dalamnya. Oleh karena itu, itu tidak dapat mendeteksi transaksi apa pun di blockchain yang terkait dengan dompet ini.

Klik pada "Pulihkan Secara Manual" di bagian bawah layar, kemudian klik pada "Tanda Tangan Tunggal".

![image](assets/28.webp)

Akhirnya, Anda akan diminta untuk memberi nama dompet ini dan menetapkan PIN. Anda dapat memberikannya nama dan PIN yang sama seperti dompet awal.
Sebagai pengingat, PIN ini hanya berfungsi untuk membuka kunci dompet di aplikasi ini dan di ponsel spesifik ini. Berbeda dengan frasa pemulihan, itu tidak memungkinkan Anda untuk meregenerasi dompet Anda di perangkat lunak atau perangkat keras lain.
![image](assets/30.webp)

Setelah PIN divalidasi, Anda akan dibawa kembali ke halaman utama dompet Anda. Saatnya untuk memeriksa apakah frasa pemulihan Anda berfungsi dengan mengamati alamat turunan pertama. Untuk melakukan ini, sekali lagi, klik pada "Terima" untuk mengakses alamat pertama.

Jika 8 karakter terakhir persis sama dengan yang Anda catat sebagai saksi di kertas Anda sebelum menghapus dompet, maka frasa Anda valid. Dalam kasus saya, kita dapat melihat bahwa checksum dari alamat pertama saya memang sama dengan nilai yang sebelumnya dicatat: JTbP4482.

![image](assets/32.webp)

Saya tahu bahwa praktik verifikasi ini melelahkan, tetapi itu benar-benar penting untuk memastikan keamanan yang tepat dari dompet Bitcoin Anda. Saya sangat menyarankan Anda untuk mengembangkan kebiasaan ini saat membuat dompet, baik itu di perangkat lunak maupun perangkat keras.

Dengan Green Wallet, saya menggunakan alamat pertama untuk melakukan proses ini. Namun, Anda juga dapat mengambil kunci publik yang diperluas (xpub/zpub) atau sidik jari induk dari kunci privat sebagai informasi saksi.

## Menggunakan Dompet Bitcoin Green Wallet

Setelah dompet Anda disiapkan dan diverifikasi, Anda dapat mulai menggunakannya.

Untuk memulai, saya sarankan menyesuaikan pengaturan dompet Anda. Untuk melakukan ini, klik pada ikon pengaturan di sudut kanan atas layar.

- Opsi "Satuan yang Ditampilkan" memungkinkan Anda untuk menyesuaikan satuan yang digunakan di dompet Anda. Jika Anda memiliki jumlah dana yang kecil, mungkin relevan untuk menampilkan dompet Anda dalam sats daripada bitcoin. Satoshi (sat) setara dengan satu ratus juta bagian dari bitcoin: 1 BTC = 100.000.000 sats.
- Opsi "Default Fee Amount" memungkinkan Anda untuk menyesuaikan biaya yang dialokasikan untuk transaksi Anda secara default. Semakin tinggi biaya per vbyte (byte virtual), semakin cepat transaksi Anda akan dikonfirmasi. Anda dapat kemudian memodifikasi tarif biaya ini untuk setiap transaksi yang dikeluarkan berdasarkan kemacetan jaringan Bitcoin.
- Opsi "Biometric Connection" memungkinkan Anda untuk membuka kunci dompet Anda dengan sidik jari Anda daripada PIN. Secara umum, saya menyarankan untuk tidak mengaktifkan opsi ini. Biometrik jauh lebih kurang aman daripada kode PIN.

![image](assets/34.webp)
Secara default, Green Wallet menetapkan Anda sebuah akun BIP49 "Nested SegWit" dengan alamat P2SH (Pay to Script Hash). Beberapa tahun yang lalu, menggunakan jenis akun ini relevan karena belum semua orang mendukung alamat SegWit asli. Hari ini, mayoritas besar layanan terkait Bitcoin mendukung SegWit, sehingga tidak ada lagi alasan untuk menggunakan akun "Nested SegWit".

Kita akan sekarang membuat akun BIP84 "Native SegWit" baru untuk memanfaatkan semua manfaatnya, dan juga untuk memiliki alamat P2WPKH (Pay to Witness Public Key Hash). Untuk melakukan ini, klik pada "Legacy SegWit Account" Anda dan kemudian pada "Add a new account", dan akhirnya pada "SegWit Account". Anda kemudian dapat memberi nama pada akun ini jika Anda inginkan.

![image](assets/36.webp)

Di masa depan, jika Anda perlu membuat akun baru pada dompet ini, saya merekomendasikan memilih akun SegWit V0 BIP84 secara default, atau SegWit V1 BIP86 (ketika tersedia).

Di halaman utama dompet Anda, Anda dapat melihat akun-akun Anda yang berbeda, termasuk akun SegWit baru Anda.

Selanjutnya, operasi aplikasi Green Wallet sangat sederhana. Untuk menerima bitcoin di dompet Anda, klik pada tombol "Receive". Dompet menampilkan alamat penerimaan. Sebuah alamat memungkinkan Anda untuk menerima bitcoin di dompet Anda. Anda dapat menyalinnya dalam format teks untuk mengirimkannya ke pembayar Anda, atau memindai kode QR dengan dompet Bitcoin lain untuk membayar alamat tersebut.

![image](assets/38.webp)

Jenis alamat ini tidak menunjukkan kepada pembayar jumlah yang harus mereka kirimkan kepada Anda. Anda juga dapat membuat alamat yang akan secara otomatis meminta jumlah tertentu dari pembayar. Untuk melakukan ini, klik pada "More options" dan masukkan jumlah yang diinginkan.

Karena Anda menggunakan akun SegWit V0 BIP84, alamat Anda seharusnya dimulai dengan awalan "bc1q". Dalam contoh saya, saya menggunakan dompet Testnet, jadi awalannya sedikit berbeda dari milik Anda.

Sebuah alamat penerimaan sebaiknya tidak digunakan berulang kali. Ini adalah praktik buruk yang menimbulkan risiko terhadap privasi Anda. Secara default, dompet Green akan menghasilkan alamat baru untuk Anda ketika Anda klik pada "Receive" dan yang sebelumnya sudah digunakan. Anda juga dapat mengklik pada ikon panah berputar untuk meminta alamat kosong baru yang terkait dengan dompet Anda.

> "Tip: Saat menyalin dan menempelkan alamat penerimaan, Anda tidak perlu memverifikasi bahwa setiap karakter dari alamat tersebut benar. Faktanya, alamat-alamat tersebut mencakup checksum untuk mendeteksi kesalahan ketik kecil. Hanya perlu memeriksa karakter pertama dan terakhir dari alamat untuk memastikan validitasnya."
> Pada tangkapan layar di bawah ini, Anda dapat melihat bahwa saya mengirim 0.02 btc ke alamat saya. Transaksi muncul di Green, awalnya sebagai "unconfirmed" sambil menunggu untuk dimasukkan ke dalam blockchain oleh penambang. Setelah transaksi telah menerima beberapa konfirmasi, Anda telah berhasil menerima bitcoin Anda di dompet Anda sendiri.

![image](assets/40.webp)
Jika Anda ingin mengirim bitcoin, Anda perlu mengambil alamat penerima ke mana Anda ingin mengirim dana dan klik tombol "Kirim". Di halaman berikutnya, Anda perlu memasukkan alamat tujuan. Anda bisa memasukkannya secara manual atau memindai kode QR dengan mengklik ikon yang sesuai. Kemudian pilih jumlah transaksi. Anda bisa memasukkan jumlah dalam bitcoin atau jumlah dalam dolar AS dengan mengklik panah ganda putih.
![image](assets/43.webp)

Di tengah layar, Anda dapat memilih tarif biaya yang dialokasikan untuk transaksi ini. Anda bisa mengikuti rekomendasi aplikasi atau menyesuaikan biaya Anda sendiri. Semakin tinggi biaya yang Anda tetapkan dibandingkan dengan transaksi lain yang menunggu konfirmasi, semakin cepat transaksi Anda akan dimasukkan, dan sebaliknya.

Klik "Berikutnya". Anda kemudian akan tiba di layar yang memberikan detail transaksi Anda. Anda dapat memverifikasi bahwa alamat yang dimasukkan benar, bahwa jumlahnya sesuai dengan apa yang ingin Anda kirim, dan bahwa biayanya benar.

Untuk menandatangani transaksi dan menyiarkannya ke jaringan Bitcoin, geser tombol hijau di bagian bawah layar ke kanan.

![image](assets/46.webp)

Transaksi Anda sekarang muncul di dasbor dompet Bitcoin Anda.

## Kesimpulan

Selamat! Anda sekarang memiliki dompet Bitcoin self-custody Anda sendiri. Bitcoin Anda benar-benar milik Anda.

Green Wallet dari Blockstream adalah solusi yang sangat baik untuk pemula dengan jumlah bitcoin yang kecil. Seperti yang Anda lihat, sangat mudah digunakan. Namun, ini masih merupakan hot wallet. Jika Anda memiliki jumlah bitcoin yang signifikan, saya merekomendasikan menggunakan hardware wallet.

Setelah Anda belajar menguasai Green Wallet dan memahami mekanisme yang bermain, Anda dapat menjelajahi solusi yang lebih komprehensif seperti Samourai Wallet atau Sparrow Wallet.
Untuk menyimpulkan, saya ingatkan Anda sekali lagi bahwa Anda harus benar-benar merawat cadangan frasa pemulihan Anda. Ini memberikan akses langsung dan tidak terbatas ke bitcoin Anda. Jika Anda kehilangannya, Anda tidak akan lagi dapat memulihkan bitcoin Anda jika ponsel Anda hilang, rusak, atau dicuri. Siapa pun yang memiliki akses ke frasa ini dapat mencuri bitcoin Anda dan tidak akan ada cara untuk memulihkannya.

> Panduan ini diproduksi dan dimiliki oleh Bitstack. Bitstack adalah neo bank bitcoin yang berbasis di Paris yang memungkinkan DCA pada bitcoin. Panduan ditulis oleh Loic Morel pada 15/02/2023. Ini milik mereka. [Link ke artikel asli](https://www.bitstack-app.com/blog/installer-portefeuille-bitcoin-green-wallet)