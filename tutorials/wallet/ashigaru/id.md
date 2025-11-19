---
name: Ashigaru
description: fork dari Samourai Wallet untuk mengamankan, mengelola, dan mencampur bitcoin Anda
---

![cover](assets/cover.webp)



Ashigaru adalah aplikasi Bitcoin mobile wallet yang merupakan kelanjutan dari proyek Samourai Wallet, tetapi dalam bentuk yang baru. Perangkat lunak ini lahir dalam konteks tertentu: pada bulan April 2024, para pendiri Samourai Wallet ditangkap oleh pihak berwenang Amerika, dan server mereka disita. Meskipun aplikasi Samurai itu sendiri masih dapat digunakan, namun saat ini tidak lagi dipertahankan. Ashigaru adalah versi fork gratis dari Samurai Wallet, yang dikelola oleh tim anonim untuk menjamin kelangsungan fungsionalitas Samurai dan menjaga filosofi aslinya: untuk mempertahankan privasi dan kedaulatan pengguna Bitcoin.



Ashigaru mengambil banyak DNA dari Samourai: antarmuka yang mirip, pendekatan yang jelas-jelas bersifat mandiri, sumber terbuka dan fokus pada privasi. Kode didistribusikan di bawah lisensi GNU GPLv3, yang memastikan bahwa siapa pun dapat mengaudit, memodifikasi, atau mendistribusikan ulang perangkat lunak.



Aplikasi Ashigaru mengintegrasikan seperangkat alat canggih untuk kerahasiaan dan pengelolaan UTXO Anda:




- Whirlpool**, protokol coinjoin berdasarkan Zerolink, memungkinkan Anda untuk memutus hubungan deterministik antara entri dan keluar transaksi, tanpa kehilangan kedaulatan atas dana Anda.
- PayNym**, yang mengimplementasikan kode pembayaran yang dapat digunakan kembali (BIP47), sekarang diwakili melalui sistem avatar "*Pepehash*".
- Ricochet**, sebuah fitur yang menambahkan lompatan perantara pada transaksi agar lebih sulit dilacak.
- Dan tentu saja ***Coin Control*** untuk memilih, membekukan dan melabeli UTXO Anda secara tepat.
- Batch Spending***, untuk mengurangi biaya dengan mengelompokkan beberapa pembayaran ke dalam satu transaksi.
- Mode **Stealth**, yang menyembunyikan aplikasi pada ponsel Anda di balik peluncur tiruan agar tidak terlihat selama pemeriksaan fisik ponsel Anda.
- Alat pengeluaran tingkat lanjut untuk mengoptimalkan kerahasiaan Anda (payjoin, stonewall...).
- Sistem pemulihan yang dioptimalkan menggunakan Passphrase BIP39.
- Sistem untuk mengoptimalkan pilihan biaya transaksi secara otomatis.



![Image](assets/fr/01.webp)



Oleh karena itu, Ashigaru ditujukan untuk pengguna yang menyadari masalah seputar keterlacakan transaksi pada Bitcoin. Baik Anda pengguna yang sadar akan privasi, pengguna bitcoin berpengalaman yang berkomitmen untuk menjaga keamanan, atau seseorang yang terpapar risiko peningkatan pengawasan, aplikasi wallet ini memberi Anda alat yang Anda butuhkan untuk mendapatkan kembali kendali atas aktivitas Anda di Bitcoin.



Ashigaru tersedia dalam versi seluler melalui aplikasinya, yang akan kita bahas dalam tutorial ini. Tetapi, aplikasi ini juga bisa digunakan di PC dengan ***Ashigaru Terminal***, yang akan kami perkenalkan dalam tutorial mendatang.



![Image](assets/fr/02.webp)



Dalam tutorial ini, saya ingin memperkenalkan Anda pada penggunaan dasar Ashigaru: instalasi, koneksi ke Dojo, pencadangan, menerima dan mengirim bitcoin. Alat-alat tingkat lanjut akan disajikan dalam tutorial khusus lainnya.



## 1. Prasyarat untuk Ashigaru



Aplikasi ini memerlukan beberapa prasyarat untuk dapat berfungsi dengan baik. Pertama-tama, ini bukan aplikasi yang tersedia di toko-toko klasik seperti Google Play Store atau App Store. Aplikasi ini dipasang secara manual di ponsel Anda hanya dari file `.apk`, yang dapat diunduh melalui jaringan Tor. Jadi, jika Anda menggunakan iPhone, metode ini tidak akan berhasil: Anda memerlukan perangkat Android.



Untuk mengunduh berkas `.apk` melalui Tor, Anda memerlukan peramban yang mampu mengakses situs-situs `.onion`. Cara termudah adalah memasang aplikasi Tor Browser pada ponsel Anda, tersedia dari [Google Play Store](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) atau secara langsung [melalui file `.apk`](https://www.torproject.org/download/#android).



![Image](assets/fr/03.webp)



Sebagian besar ponsel pintar terbaru memblokir instalasi aplikasi dari sumber yang tidak dikenal secara default. Anda harus mengaktifkan sementara opsi ini untuk Tor Browser di pengaturan perangkat Anda untuk mengizinkan penginstalan. Setelah aplikasi terinstal, ingatlah untuk menonaktifkan fungsi ini untuk memperkuat keamanan ponsel Anda.



Prasyarat penting lainnya untuk menggunakan Ashigaru adalah node Bitcoin Dojo. Untuk alasan keamanan dan kedaulatan, tim Ashigaru tidak mengelola server terpusat untuk menghubungkan aplikasi Anda. Jadi, Anda harus menjalankan instance Dojo Anda sendiri, atau terhubung ke Dojo yang tepercaya.



Dojo memungkinkan aplikasi Ashigaru Anda untuk berkonsultasi dengan informasi blockchain, melihat saldo alamat Anda, dan menyiarkan transaksi Anda di jaringan Bitcoin.



Untuk mengetahui lebih lanjut tentang Dojo dan mempelajari cara menginstalnya, saya mengundang Anda untuk mengikuti tutorial khusus ini:



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Jika Anda benar-benar tidak mampu menjalankan Dojo Anda sendiri, Anda dapat menemukan orang yang bersedia membagikan instance mereka secara gratis di [dojobay.pw] (https://www.dojobay.pw/mainnet/). Ini mungkin merupakan solusi sementara, tetapi dalam jangka panjang, saya sarankan Anda menggunakan Dojo Anda sendiri untuk menjamin kedaulatan dan kerahasiaan Anda.



## 2. Periksa dan instal aplikasi Ashigaru



### 2.1. Unduh aplikasi Ashigaru



Pada ponsel Anda, buka Tor Browser dan buka [situs web resmi Ashigaru] (https://ashigaru.rs/download/), di bagian `Unduh`. Kemudian klik pada tombol `Unduh untuk Android` untuk mengunduh berkas instalasi.



![Image](assets/fr/04.webp)



Sebelum menginstal aplikasi pada perangkat Anda, kami akan memeriksa keaslian dan integritasnya. Ini adalah langkah yang sangat penting, terutama ketika menginstal aplikasi langsung dari file `.apk'.



### 2.2. Periksa aplikasi Ashigaru



Kembali ke [situs web resmi Ashigaru](https://ashigaru.rs/download/) di bagian `Download`, lalu salin pesan yang ditampilkan di bawah judul `SHA-256 Hash file APK`. Salin seluruh blok, dari `MULAI PESAN BERTANDATANGAN PGP` hingga `AKHIRI TANDATANGAN PGP`.



![Image](assets/fr/05.webp)



Masih pada ponsel Anda, buka tab baru pada Tor Browser dan masuk ke [alat verifikasi Keybase](https://keybase.io/verify). Rekatkan pesan yang baru saja Anda salin ke dalam bidang yang disediakan, lalu klik tombol `Verify`.



![Image](assets/fr/06.webp)



Jika tanda tangan tersebut asli, Keybase akan menampilkan pesan yang mengonfirmasi bahwa file tersebut telah ditandatangani oleh pengembang Ashigaru. Anda juga dapat mengklik profil `ashigarudev` yang ditunjukkan oleh Keybase dan memeriksa apakah sidik jarinya sama persis dengan sidik jari : `A138 06B1 FA2A 676B`.



Namun, jika muncul kesalahan pada tahap ini, berarti tanda tangan tersebut tidak valid. Dalam hal ini, **jangan menginstal APK**. Mulai lagi dari awal, atau minta bantuan komunitas sebelum melanjutkan.



![Image](assets/fr/07.webp)



Keybase telah memberikan Anda hash dari aplikasi tersebut. Sekarang kita akan memeriksa apakah hash dari file `.apk` yang telah Anda unduh sesuai dengan yang diverifikasi di Keybase. Untuk melakukannya, buka [HASH FILE ONLINE](https://hash-file.online/).



![Image](assets/fr/08.webp)



Klik tombol `BROWSE... ` dan pilih file `.apk` yang telah diunduh pada langkah 2.1.


Kemudian pilih fungsi hash `SHA-256`, dan klik `HITUNG HASH` untuk menghitung hash file Anda.



![Image](assets/fr/09.webp)



Situs ini akan menampilkan hash file `.apk` Anda. Bandingkan dengan hash yang Anda verifikasi di Keybase.io. Jika kedua hash tersebut identik, pemeriksaan keaslian dan integritas telah berhasil. Anda sekarang dapat melanjutkan untuk menginstal aplikasi.



![Image](assets/fr/10.webp)



### 2.3. Instal aplikasi Ashigaru



Untuk menginstal aplikasi, buka manajer file ponsel Anda dan buka folder unduhan. Kemudian klik file `.apk` yang baru saja Anda periksa, dan konfirmasikan penginstalan ketika diminta.



![Image](assets/fr/11.webp)



Ashigaru sekarang sudah terinstal di ponsel Anda.



## 3. Inisialisasi aplikasi dan buat portofolio Bitcoin



Saat meluncurkan aplikasi untuk pertama kalinya, pilih `MAINNET`.



![Image](assets/fr/12.webp)



Kemudian klik `Mulai`.



![Image](assets/fr/13.webp)



Sekarang kita akan membuat portofolio Bitcoin yang baru. Tekan tombol `Buat wallet baru`.



![Image](assets/fr/14.webp)



### 3.1. membuat portofolio Bitcoin



Ashigaru membutuhkan passphrase BIP39. Pilih passphrase Anda dan masukkan di kolom yang sesuai. Ini harus sepanjang dan seacak mungkin untuk menahan serangan brute force.



Buatlah cadangan fisik dari passphrase ini dengan segera. Ini adalah langkah yang sangat penting: jika Anda kehilangan ponsel Anda, **jika Anda tidak lagi memiliki passphrase ini, Anda tidak lagi dapat mengakses bitcoin Anda** yang tersimpan di Ashigaru wallet Anda. passphrase yang sama ini juga digunakan untuk mengenkripsi file pemulihan wallet.



Jika Anda tidak tahu apa itu passphrase, atau tidak sepenuhnya memahami cara kerjanya, saya sangat menyarankan Anda untuk membaca tutorial tambahan ini. Ini penting, karena passphrase adalah elemen penting dalam keamanan Anda: kesalahpahaman dalam penggunaannya dapat mengakibatkan hilangnya dana Anda secara permanen.



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Setelah Anda memasukkan passphrase Anda, klik `NEXT`.



![Image](assets/fr/15.webp)



Kemudian pilih kode PIN. Kode ini akan digunakan untuk membuka kunci Ashigaru wallet Anda, melindunginya dari akses fisik yang tidak sah. Kode ini tidak terlibat dalam derivasi kriptografi kunci wallet Anda. Ini berarti, bahkan tanpa mengetahui kode PIN, siapapun yang memiliki frasa mnemonik dan passphrase Anda akan dapat memperoleh kembali akses ke bitcoin Anda.



Pilihlah kode PIN yang panjang dan acak. Ingatlah untuk menyimpan salinan cadangan di lokasi yang terpisah dari ponsel Anda, untuk mencegah keduanya dibobol secara bersamaan.



![Image](assets/fr/16.webp)



Setelah kode PIN dibuat, Ashigaru akan menampilkan frasa mnemonik wallet Anda. Peringatan: frasa ini, digabungkan dengan passphrase Anda, memberikan akses penuh ke bitcoin Anda. Siapa pun yang memegangnya dapat mengambil dana Anda, meskipun mereka tidak memiliki akses ke ponsel Anda. Urutan 12 kata ini dapat digunakan untuk mengembalikan wallet Anda jika ponsel Anda hilang, dicuri, atau rusak. Oleh karena itu, penting untuk menyimpannya dengan sangat hati-hati pada media fisik (kertas atau logam).



Jangan pernah menyimpan frasa ini dalam bentuk digital, atau Anda berisiko mengekspos dana Anda pada pencurian. Tergantung pada strategi keamanan Anda, Anda bisa membuat beberapa salinan fisik, namun jangan pernah membaginya. Simpanlah kata-kata tersebut sesuai dengan urutannya, dan pastikan kata-kata tersebut diberi nomor.



Terakhir, jangan pernah menyimpan mnemonic dan passphrase di tempat yang sama. Jika keduanya disusupi secara bersamaan, penyerang bisa mendapatkan akses ke wallet Anda.



![Image](assets/fr/17.webp)



Untuk mempelajari lebih lanjut mengenai cara mengamankan frasa mnemonik Anda, silakan baca tutorial pelengkap ini:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ashigaru kemudian meminta Anda untuk mengonfirmasi ulang passphrase Anda. Gunakan kesempatan ini untuk memeriksa apakah cadangan fisik Anda sudah benar.



![Image](assets/fr/18.webp)



### 3.2. Menghubungkan dojo



Berikutnya adalah langkah menghubungkan ke Dojo Anda. Seperti yang telah dijelaskan di bagian pendahuluan, Ashigaru harus terhubung ke Dojo agar dapat berinteraksi dengan jaringan Bitcoin.



Masuk ke "Alat Pemeliharaan" Dojo Anda dan buka menu `PAIRING`.



![Image](assets/fr/19.webp)



Pada Ashigaru, tekan tombol `Pindai QR`, lalu pindai kode QR koneksi yang ditampilkan oleh DMT Anda. Kemudian klik `Lanjutkan` untuk mengonfirmasi.



![Image](assets/fr/20.webp)



Masukkan kode PIN Anda untuk membuka kunci wallet. Ini akan membawa Anda ke halaman sinkronisasi. Kesalahan *PayNym* pada tahap ini merupakan hal yang wajar, karena wallet masih baru. Cukup klik `Lanjutkan`.



![Image](assets/fr/21.webp)



Anda kemudian akan dibawa ke halaman beranda portofolio Anda.



![Image](assets/fr/22.webp)



Sebelum melangkah lebih jauh, saya sarankan Anda untuk melakukan uji coba pemulihan ketika wallet masih belum berisi bitcoin. Hal ini akan memungkinkan Anda untuk memeriksa apakah cadangan kertas Anda berfungsi dengan baik. Untuk mengetahui caranya, ikuti tutorial ini:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. Menyiapkan aplikasi Ashigaru



Untuk mengakses pengaturan aplikasi, klik gambar *PayNym* Anda di sudut kiri atas, lalu pilih `Pengaturan`.



![Image](assets/fr/23.webp)



Di sini Anda akan menemukan beberapa opsi untuk menyesuaikan pengoperasian Ashigaru dengan kebutuhan Anda. Namun demikian, saya sangat menyarankan agar Anda mengaktifkan 2 parameter penting sejak awal.



Mulailah dengan membuka menu `Keamanan > Mode siluman`, lalu aktifkan fitur ini jika Anda membutuhkannya. Fitur ini menyembunyikan aplikasi Ashigaru di balik nama, logo, dan antarmuka aplikasi biasa yang terpasang di ponsel Anda. Tujuannya adalah untuk mencegah siapa pun mengidentifikasi Ashigaru jika terjadi pemeriksaan fisik pada ponsel Anda.



![Image](assets/fr/24.webp)



Setiap aplikasi palsu yang ditawarkan memiliki metode khusus untuk membuka antarmuka Ashigaru yang asli. Sebagai contoh, jika Anda memilih kalkulator, aplikasi Ashigaru akan menghilang dari layar beranda dan digantikan oleh kalkulator palsu. Ketika Anda membukanya, Anda akan melihat antarmuka kalkulator klasik yang berfungsi, tetapi untuk mengakses Ashigaru, yang harus Anda lakukan adalah mengetuk simbol `=` lima kali dengan cepat.



Parameter penting kedua yang harus diaktifkan adalah [**RBF** (*Replace-by-Fee*)] (https://planb.academy/resources/glossary/rbf-replacebyfee). Opsi ini memungkinkan Anda untuk meningkatkan biaya transaksi jika terjebak dalam mempool karena biayanya terlalu rendah. Anda dapat mengaktifkannya melalui menu `Transactions > Spend using RBF`.



![Image](assets/fr/25.webp)



Tips: Anda dapat mengubah unit tampilan portofolio Anda dari `BTC` ke `sat` hanya dengan mengklik total saldo yang ditampilkan di halaman beranda.



## 5. Menerima bitcoin di Ashigaru



Sekarang, setelah portofolio Anda beroperasi, Anda dapat menerima satss. Untuk melakukannya, tekan tombol `+` di bagian kanan bawah antarmuka, lalu tombol `Terima` berwarna hijau.



![Image](assets/fr/26.webp)



Ashigaru kemudian menunjukkan kepada Anda alamat penerima pertama yang tidak digunakan dalam wallet Anda, untuk mencegah penggunaan ulang alamat (penggunaan ulang alamat merupakan praktik yang sangat buruk bagi privasi Anda). Anda kemudian dapat meneruskan alamat ini kepada orang atau layanan yang perlu mengirimkan bitcoin kepada Anda.



![Image](assets/fr/27.webp)



Setelah transaksi disiarkan di jaringan, transaksi akan secara otomatis muncul di halaman beranda aplikasi.



![Image](assets/fr/28.webp)



## 6. Kirim bitcoin dengan Ashigaru



Sekarang setelah Anda memiliki bitcoin di Ashigaru wallet, Anda juga bisa mengirimkannya. Untuk melakukannya, tekan tombol `+` di kanan bawah, lalu pilih tombol `Kirim` berwarna merah.



![Image](assets/fr/29.webp)



Kemudian pilih akun dari mana Anda ingin melakukan pengeluaran. Untuk saat ini, kita belum membahas akun `Postmix`, yang disediakan untuk koin bersama, yang akan kita bahas di tutorial selanjutnya. Jadi kita akan mengirim dana dari akun deposit utama.



![Image](assets/fr/30.webp)



Masukkan detail transaksi Anda: jumlah yang akan dikirim dan alamat Bitcoin penerima.



![Image](assets/fr/31.webp)



Dengan mengklik tiga titik kecil di sudut kanan atas, kemudian pada `Show unspent outputs`, Anda juga dapat memilih dengan tepat UTXO mana yang ingin Anda keluarkan, untuk meningkatkan privasi Anda.



![Image](assets/fr/32.webp)



Setelah Anda mengisi semua detail, klik panah putih di bagian bawah antarmuka untuk melanjutkan.



Anda kemudian akan dibawa ke halaman ringkasan yang menampilkan semua detail transaksi Anda. Beberapa elemen penting ditampilkan:




- Di blok `Tujuan`, periksa untuk terakhir kalinya bahwa alamat penerima dan jumlah yang dikirim sudah benar;
- Pada blok `Biaya`, Anda dapat melihat tarif biaya yang dipilih secara otomatis oleh Ashigaru dan, jika perlu, memodifikasinya dengan mengeklik `MANAGE`;
- Blok `Transaksi` menunjukkan jenis transaksi yang akan Anda lakukan. Di sini, kita berbicara tentang transaksi sederhana, tetapi Ashigaru juga mendukung jenis transaksi yang dioptimalkan untuk privasi, yang akan kita bahas secara rinci dalam tutorial mendatang;
- Blok merah `Peringatan Transaksi` memperingatkan Anda jika transaksi Anda menunjukkan pola yang dapat dikenali oleh alat analisis rantai, dan dapat membahayakan privasi Anda. Dengan mengkliknya, Anda bisa melihat detailnya. Sebagai contoh, dalam kasus saya, Ashigaru memberi tahu saya bahwa jumlah yang dikirim adalah bulat (`3000 sats`), sehingga saya dapat menyimpulkan hasil mana yang sesuai dengan pengeluaran dan mana yang merupakan pertukaran. Untuk mengetahui lebih lanjut tentang heuristik analisis rantai ini, saya mengundang Anda untuk mengikuti pelatihan BTC 204 saya di Plan ₿ Academy;
- Terakhir, Anda dapat menambahkan label pada transaksi Anda untuk mencatat tujuannya.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Setelah Anda memeriksa semua informasi, gunakan tanda panah hijau untuk mengirim bitcoin. Tahan panah, lalu seret ke kanan untuk mengonfirmasi pengiriman.



![Image](assets/fr/33.webp)



Transaksi Anda telah disiarkan di jaringan Bitcoin.



![Image](assets/fr/34.webp)



## 7. Memulihkan Ashigaru wallet Anda



Pemulihan Ashigaru wallet sedikit berbeda dengan Bitcoin wallet klasik, karena aplikasi ini menggunakan metode yang sama dengan Samurai Wallet. Jika Anda kehilangan akses ke wallet Anda (entah karena lupa PIN, menghapus instalasinya, atau kehilangan ponsel), ada beberapa cara untuk memulihkan bitcoin Anda.



Jika Anda masih memiliki akses ke ponsel Anda, atau jika Anda telah membuat cadangan file ini, metode yang paling sederhana adalah dengan menggunakan file cadangan `ashigaru.txt`. File ini berisi semua informasi yang anda perlukan untuk memulihkan portofolio anda pada contoh baru Ashigaru (atau pada Sparrow Wallet), tetapi file ini dienkripsi dengan passphrase yang telah anda tetapkan pada langkah 3.1 tutorial ini. Oleh karena itu, Anda harus memiliki file `ashigaru.txt` dan passphrase Anda untuk menggunakan metode ini.



Dengan kedua elemen ini, Anda dapat, misalnya, memulihkan portofolio Anda pada Sparrow Wallet.



![Image](assets/fr/35.webp)



Jika Anda tidak memiliki akses ke file `ashigaru.txt`, Anda masih dapat memperoleh kembali akses ke dana Anda dengan menggunakan frasa mnemonik passphrase, sama seperti yang Anda lakukan untuk portofolio Bitcoin lainnya. Saya sarankan Anda melakukan pemulihan ini pada instance Ashigaru yang baru, atau langsung pada Sparrow Wallet, untuk dengan mudah memulihkan jalur bypass dari Whirlpool jika Anda menggunakannya. Atau, Anda dapat mengimpor informasi ini ke dalam perangkat lunak lain yang kompatibel dengan BIP39 dengan memasukkan jalur turunan secara manual.



Untuk informasi lebih lanjut mengenai proses ini, silakan baca tutorial lengkap yang sudah saya tulis mengenai cara memulihkan Samurai Wallet dan wallet. Karena Ashigaru adalah fork, maka prosedurnya pun sama:



https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

Seperti yang Anda lihat, apa pun metode pemulihan yang Anda gunakan, passphrase sangat diperlukan. Jadi, pastikan untuk mencadangkannya dengan hati-hati. Anda juga bisa membuat beberapa salinan, tergantung pada strategi keamanan Anda.



## 8. Perbarui aplikasi



Untuk memperbarui aplikasi Ashigaru, karena Anda menginstalnya dari file `.apk` dan bukan melalui Play Store seperti aplikasi biasa, Anda harus mengunduh file `.apk` baru yang sesuai dengan versi yang diperbarui, lalu menginstalnya secara manual.



Ulangi langkah-langkah yang dijelaskan di bagian 2 tutorial ini, kecuali ketika Anda mengklik file `.apk` untuk meluncurkan penginstalan, **ponsel Android Anda akan menawarkan opsi `Update`, bukan `Install`.



![Image](assets/fr/41.webp)



Ini adalah poin yang sangat penting: jika Android menampilkan `Install` dan bukannya `Update`, Anda mungkin menginstal versi yang salah. Dalam hal ini, segera hentikan prosedur instalasi.



Seperti instalasi pertama, periksa keaslian dan integritas file `.apk` sebelum melanjutkan pembaruan.



Untuk mengetahui kapan versi baru tersedia, periksa situs web resmi Ashigaru dari waktu ke waktu. Tenang saja, Ashigaru adalah aplikasi yang stabil dan matang, yang diwarisi dari Samourai Wallet, dan pembaruannya relatif jarang dibandingkan dengan perangkat lunak yang lebih muda.



## 9. Donasi untuk proyek Ashigaru



Ashigaru adalah proyek sumber terbuka. Jika Anda ingin mendukung pengembangannya, Anda dapat memberikan donasi langsung dari aplikasi melalui PayNym.



Untuk melakukannya, klik PayNym Anda di bagian kanan atas antarmuka, lalu pilih kode pembayaran yang dimulai dengan `PM...`.



![Image](assets/fr/36.webp)



Kemudian tekan tombol `+` di bagian kanan bawah layar.



![Image](assets/fr/37.webp)



Pilih `Ashigaru Open Source Project` sebagai penerima.



![Image](assets/fr/38.webp)



Klik tombol `CONNECT` untuk membuat saluran komunikasi BIP47 (lebih lanjut tentang protokol ini dalam tutorial di bawah).



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)



Setelah transaksi notifikasi dikonfirmasi, Anda dapat mengirimkan donasi Anda ke proyek dengan mengklik panah putih kecil di sudut kanan atas antarmuka.



![Image](assets/fr/40.webp)



Anda sekarang tahu bagaimana cara menggunakan fitur-fitur dasar aplikasi Ashigaru. Dalam tutorial selanjutnya, kita akan melihat cara memanfaatkan transaksi pembelanjaan tingkat lanjut, serta Whirlpool, implementasi coinjoin yang diwarisi dari Samurai Wallet.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add
