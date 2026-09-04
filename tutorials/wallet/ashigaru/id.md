---
name: Ashigaru
description: fork dari Samourai Wallet untuk mengamankan, mengelola, dan mencampur bitcoin Anda
---

![cover](assets/cover.webp)



Ashigaru adalah aplikasi mobile Bitcoin wallet yang merupakan kelanjutan dari proyek Samourai Wallet, tetapi dalam bentuk baru. Perangkat lunak ini lahir dalam konteks tertentu: pada April 2024, para pendiri Samourai Wallet ditangkap oleh pihak berwenang Amerika dan server mereka disita. Meskipun aplikasi Samourai itu sendiri masih bisa digunakan, saat ini sudah tidak lagi dipertahankan. Ashigaru adalah versi fork gratis dari Samourai Wallet, yang dikelola oleh tim anonim untuk menjamin keberlanjutan fungsionalitas Samourai dan menjaga filosofi aslinya: mempertahankan privasi dan kedaulatan pengguna Bitcoin.

Ashigaru mengambil banyak DNA dari Samourai: antarmuka yang mirip, pendekatan yang jelas bersifat mandiri, open source, dan fokus kuat pada privasi. Kode didistribusikan di bawah lisensi GNU GPLv3, yang memastikan siapa pun dapat mengaudit, memodifikasi, atau mendistribusikan ulang perangkat lunak ini.

Aplikasi Ashigaru mengintegrasikan seperangkat alat canggih untuk kerahasiaan dan pengelolaan UTXO kamu:

- Whirlpool**, protokol coinjoin berbasis Zerolink, memungkinkan kamu memutus hubungan deterministik antara input dan output transaksi tanpa kehilangan kedaulatan atas dana kamu.
- PayNym**, yang mengimplementasikan payment code yang dapat digunakan kembali (BIP47), kini direpresentasikan melalui sistem avatar "*Pepehash*".
- Ricochet**, fitur yang menambahkan lompatan perantara pada transaksi agar lebih sulit dilacak.
- Dan tentu saja ***Coin Control*** untuk memilih, membekukan, dan memberi label pada UTXO kamu secara presisi.
- Batch Spending***, untuk mengurangi biaya dengan mengelompokkan beberapa pembayaran ke dalam satu transaksi.
- Mode **Stealth**, yang menyembunyikan aplikasi di ponsel kamu di balik launcher tiruan agar tidak terlihat saat pemeriksaan fisik perangkat.
- Alat pengeluaran tingkat lanjut untuk mengoptimalkan kerahasiaan kamu (payjoin, stonewall...).
- Sistem pemulihan yang dioptimalkan menggunakan BIP39 Passphrase.
- Sistem untuk mengoptimalkan pemilihan biaya transaksi secara otomatis.




![Image](assets/fr/01.webp)



Oleh karena itu, Ashigaru ditujukan untuk pengguna yang menyadari masalah seputar keterlacakan transaksi pada Bitcoin. Baik kamu pengguna yang sadar akan privasi, pengguna Bitcoin berpengalaman yang berkomitmen menjaga keamanan, atau seseorang yang terpapar risiko peningkatan pengawasan, aplikasi wallet ini memberi kamu alat yang dibutuhkan untuk mendapatkan kembali kendali atas aktivitas di Bitcoin.

Ashigaru tersedia dalam versi seluler melalui aplikasinya, yang akan kita bahas dalam tutorial ini. Namun, aplikasi ini juga bisa digunakan di PC melalui ***Ashigaru Terminal***, yang akan diperkenalkan dalam tutorial mendatang.




![Image](assets/fr/02.webp)



Dalam tutorial ini, aku ingin memperkenalkan kamu pada penggunaan dasar Ashigaru: instalasi, koneksi ke Dojo, pencadangan, serta menerima dan mengirim Bitcoin. Alat-alat tingkat lanjut akan disajikan dalam tutorial khusus lainnya.



## 1. Prasyarat untuk Ashigaru



Aplikasi ini memerlukan beberapa prasyarat agar dapat berfungsi dengan baik. Pertama, ini bukan aplikasi yang tersedia di toko klasik seperti Google Play Store atau App Store. Aplikasi ini dipasang secara manual di ponsel kamu hanya dari file `.apk`, yang bisa diunduh melalui jaringan Tor. Jadi, jika kamu menggunakan iPhone, metode ini tidak akan berhasil: kamu memerlukan perangkat Android.



Untuk mengunduh berkas `.apk` melalui Tor, kamu memerlukan peramban yang mampu mengakses situs-situs `.onion`. Cara termudah adalah memasang aplikasi Tor Browser pada ponsel kamu, tersedia dari [Google Play Store](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) atau secara langsung [melalui file `.apk`](https://www.torproject.org/download/#android).



![Image](assets/fr/03.webp)



Sebagian besar ponsel pintar terbaru memblokir instalasi aplikasi dari sumber yang tidak dikenal secara default. Kamu harus sementara mengaktifkan opsi ini untuk Tor Browser di pengaturan perangkat agar penginstalan dapat dilakukan. Setelah aplikasi terinstal, ingat untuk menonaktifkan kembali fungsi ini guna memperkuat keamanan ponsel kamu.



Prasyarat penting lainnya untuk menggunakan Ashigaru adalah node Bitcoin Dojo. Demi alasan keamanan dan kedaulatan, tim Ashigaru tidak mengelola server terpusat untuk menghubungkan aplikasi kamu. Jadi, kamu harus menjalankan instance Dojo sendiri, atau terhubung ke Dojo yang tepercaya.



Dojo memungkinkan aplikasi Ashigaru kamu untuk berkonsultasi dengan informasi blockchain, melihat saldo alamat, dan menyiarkan transaksi di jaringan Bitcoin.



Untuk mempelajari lebih lanjut tentang Dojo dan cara menginstalnya, aku mengundang kamu untuk mengikuti tutorial khusus ini:



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Kalau kamu benar-benar tidak mampu menjalankan Dojo kamu sendiri, kamu dapat menemukan orang yang bersedia membagikan instance mereka secara gratis di [dojobay.pw](https://www.dojobay.pw/mainnet/). Ini mungkin merupakan solusi sementara, tetapi dalam jangka panjang, aku menyarankanmu menggunakan Dojo sendiri untuk menjamin kedaulatan dan kerahasiaan kamu.



## 2. Periksa dan instal aplikasi Ashigaru



### 2.1. Unduh aplikasi Ashigaru



Pada ponsel kamu, buka Tor Browser dan buka [situs web resmi Ashigaru](https://ashigaru.rs/download/), di bagian `Unduh`. Kemudian klik pada tombol `Unduh untuk Android` untuk mengunduh berkas instalasi.



![Image](assets/fr/04.webp)



Sebelum menginstal aplikasi di perangkat kamu, kita akan memeriksa keaslian dan integritasnya. Ini adalah langkah yang sangat penting, terutama saat menginstal aplikasi langsung dari file `.apk`.



### 2.2. Periksa aplikasi Ashigaru



Kembali ke [situs web resmi Ashigaru](https://ashigaru.rs/download/) di bagian `Download`, lalu salin pesan yang ditampilkan di bawah judul `SHA-256 Hash file APK`. Salin seluruh blok, dari `MULAI PESAN BERTANDATANGAN PGP` hingga `AKHIRI TANDATANGAN PGP`.



![Image](assets/fr/05.webp)



Masih pada ponsel kamu, buka tab baru pada Tor Browser dan masuk ke [alat verifikasi Keybase](https://keybase.io/verify). Rekatkan pesan yang baru saja kamu salin ke dalam bidang yang disediakan, lalu klik tombol `Verify`.



![Image](assets/fr/06.webp)



Jika tanda tangan tersebut asli, Keybase akan menampilkan pesan yang mengonfirmasi bahwa file tersebut telah ditandatangani oleh pengembang Ashigaru. Kamu juga dapat mengklik profil `ashigarudev` yang ditunjukkan oleh Keybase dan memeriksa apakah sidik jarinya sama persis dengan sidik jari : `A138 06B1 FA2A 676B`.



Namun, jika muncul kesalahan pada tahap ini, berarti tanda tangan tersebut tidak valid. Dalam hal ini, **jangan menginstal APK**. Mulai lagi dari awal, atau minta bantuan komunitas sebelum melanjutkan.



![Image](assets/fr/07.webp)



Keybase telah memberikan kamu hash dari aplikasi tersebut. Sekarang kita akan memeriksa apakah hash dari file `.apk` yang telah kamu unduh sesuai dengan yang diverifikasi di Keybase. Untuk melakukannya, buka [HASH FILE ONLINE](https://hash-file.online/).



![Image](assets/fr/08.webp)



Klik tombol `BROWSE... ` dan pilih file `.apk` yang telah diunduh pada langkah 2.1.


Kemudian pilih fungsi hash `SHA-256`, dan klik `HITUNG HASH` untuk menghitung hash file kamu.



![Image](assets/fr/09.webp)



Situs ini akan menampilkan hash file `.apk` kamu. Bandingkan dengan hash yang kamu verifikasi di Keybase.io. Jika kedua hash tersebut identik, pemeriksaan keaslian dan integritas telah berhasil. Kamu sekarang dapat melanjutkan untuk menginstal aplikasi.



![Image](assets/fr/10.webp)



### 2.3. Instal aplikasi Ashigaru



Untuk menginstal aplikasi, buka manajer file ponsel kamu dan buka folder unduhan. Kemudian klik file `.apk` yang baru saja kamu periksa, dan konfirmasikan penginstalan ketika diminta.



![Image](assets/fr/11.webp)



Ashigaru sekarang sudah terinstal di ponsel kamu.



## 3. Inisialisasi aplikasi dan buat portofolio Bitcoin



Saat meluncurkan aplikasi untuk pertama kalinya, pilih `MAINNET`.



![Image](assets/fr/12.webp)



Kemudian klik `Mulai`.



![Image](assets/fr/13.webp)



Sekarang kita akan membuat portofolio Bitcoin yang baru. Tekan tombol `Buat wallet baru`.



![Image](assets/fr/14.webp)



### 3.1. Membuat portofolio Bitcoin



Ashigaru membutuhkan BIP39 passphrase. Pilih passphrase kamu dan masukkan di kolom yang sesuai. Passphrase ini harus panjang dan seacak mungkin agar tahan terhadap serangan brute force.



Segera buat cadangan fisik dari passphrase ini. Ini langkah yang sangat penting: jika kamu kehilangan ponsel, **jika kamu tidak lagi memiliki passphrase ini, kamu tidak akan bisa mengakses Bitcoin yang tersimpan di Ashigaru wallet kamu**. Passphrase yang sama juga digunakan untuk mengenkripsi file pemulihan wallet.



Jika kamu belum tahu apa itu passphrase, atau belum sepenuhnya memahami cara kerjanya, aku sangat menyarankan kamu membaca tutorial tambahan ini. Ini penting karena passphrase adalah elemen krusial dalam keamanan: kesalahan penggunaan dapat mengakibatkan hilangnya dana secara permanen.



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Setelah Anda memasukkan passphrase Anda, klik `NEXT`.



![Image](assets/fr/15.webp)



Kemudian pilih kode PIN. Kode ini akan digunakan untuk membuka kunci Ashigaru wallet kamu, melindunginya dari akses fisik yang tidak sah. Kode ini tidak terlibat dalam derivasi kriptografi kunci wallet kamu. Artinya, bahkan tanpa mengetahui kode PIN, siapa pun yang memiliki frasa mnemonik dan passphrase kamu tetap bisa memperoleh kembali akses ke Bitcoin kamu.



Pilih kode PIN yang panjang dan acak. Ingat untuk menyimpan salinan cadangannya di lokasi terpisah dari ponsel, agar keduanya tidak bisa dibobol sekaligus.




![Image](assets/fr/16.webp)



Setelah kode PIN dibuat, Ashigaru akan menampilkan frasa mnemonik wallet kamu. Peringatan: frasa ini, digabung dengan passphrase kamu, memberikan akses penuh ke Bitcoin kamu. Siapa pun yang memegangnya dapat mengambil dana kamu, meskipun mereka tidak memiliki akses ke ponsel. Urutan 12 kata ini bisa digunakan untuk mengembalikan wallet jika ponsel hilang, dicuri, atau rusak. Oleh karena itu, penting untuk menyimpannya dengan sangat hati-hati pada media fisik (kertas atau logam).



Jangan pernah menyimpan frasa ini dalam bentuk digital, karena kamu berisiko mengekspos dana pada pencurian. Tergantung strategi keamanan, kamu bisa membuat beberapa salinan fisik, tetapi jangan pernah membaginya. Simpan kata-kata sesuai urutannya, dan pastikan diberi nomor.



Terakhir, jangan pernah menyimpan mnemonic dan passphrase di tempat yang sama. Jika keduanya disusupi sekaligus, penyerang bisa mendapatkan akses ke wallet kamu.



![Image](assets/fr/17.webp)



Untuk mempelajari lebih lanjut mengenai cara mengamankan frasa mnemonik kamu, silakan baca tutorial pelengkap ini:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ashigaru kemudian meminta kamu untuk mengonfirmasi ulang passphrase. Gunakan kesempatan ini untuk memeriksa apakah cadangan fisik kamu sudah benar.



![Image](assets/fr/18.webp)



### 3.2. Menghubungkan dojo



Berikutnya adalah langkah menghubungkan ke Dojo milikmu. Seperti yang telah dijelaskan di bagian pendahuluan, Ashigaru harus terhubung ke Dojo agar dapat berinteraksi dengan jaringan Bitcoin.



Masuk ke "Alat Pemeliharaan" Dojo Anda dan buka menu `PAIRING`.



![Image](assets/fr/19.webp)



Pada Ashigaru, tekan tombol `Pindai QR`, lalu pindai kode QR koneksi yang ditampilkan oleh DMT kamu. Kemudian klik `Lanjutkan` untuk mengonfirmasi.



![Image](assets/fr/20.webp)



Masukkan kode PIN untuk membuka kunci wallet. Ini akan membawa Anda ke halaman sinkronisasi. Kesalahan *PayNym* pada tahap ini merupakan hal yang wajar, karena wallet masih baru. Cukup klik `Lanjutkan`.



![Image](assets/fr/21.webp)



Kemudian kamu akan dibawa ke halaman beranda portofolio milikmu.



![Image](assets/fr/22.webp)



Sebelum melangkah lebih jauh, aku sarankan kamu melakukan uji coba pemulihan saat wallet masih kosong dari Bitcoin. Ini memungkinkan kamu memeriksa apakah cadangan kertas kamu berfungsi dengan baik. Untuk mengetahui caranya, ikuti tutorial ini:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. Menyiapkan aplikasi Ashigaru



Untuk mengakses pengaturan aplikasi, klik gambar *PayNym* Anda di sudut kiri atas, lalu pilih `Pengaturan`.



![Image](assets/fr/23.webp)



Di sini kamu akan menemukan beberapa opsi untuk menyesuaikan cara kerja Ashigaru sesuai kebutuhan. Meski begitu, aku sangat menyarankan agar kamu mengaktifkan 2 parameter penting sejak awal.



Mulailah dengan membuka menu `Keamanan > Mode siluman`, lalu aktifkan fitur ini jika kamu membutuhkannya. Fitur ini menyembunyikan aplikasi Ashigaru di balik nama, logo, dan antarmuka aplikasi biasa yang terpasang di ponsel kamu. Tujuannya untuk mencegah siapa pun mengidentifikasi Ashigaru jika terjadi pemeriksaan fisik pada ponsel kamu.




![Image](assets/fr/24.webp)



Setiap aplikasi palsu yang ditawarkan memiliki metode khusus untuk membuka antarmuka Ashigaru yang asli. Sebagai contoh, jika kamu memilih kalkulator, aplikasi Ashigaru akan menghilang dari layar beranda dan digantikan oleh kalkulator palsu. Saat kamu membukanya, kamu akan melihat antarmuka kalkulator klasik yang berfungsi normal, tetapi untuk mengakses Ashigaru, yang perlu kamu lakukan hanyalah mengetuk simbol `=` lima kali dengan cepat.



Parameter penting kedua yang harus diaktifkan adalah [**RBF** (*Replace-by-Fee*)](https://planb.academy/resources/glossary/rbf-replacebyfee). Opsi ini memungkinkanmu untuk meningkatkan biaya transaksi jika terjebak dalam mempool karena biayanya terlalu rendah. Kamu dapat mengaktifkannya melalui menu `Transactions > Spend using RBF`.



![Image](assets/fr/25.webp)



Tips: kamu dapat mengubah unit tampilan portofolio kamu dari `BTC` ke `sat` hanya dengan mengklik total saldo yang ditampilkan di halaman beranda.



## 5. Menerima bitcoin di Ashigaru



Sekarang, setelah portofolio kamu beroperasi, kamu dapat menerima satss. Untuk melakukannya, tekan tombol `+` di bagian kanan bawah antarmuka, lalu tombol `Terima` berwarna hijau.



![Image](assets/fr/26.webp)



Ashigaru kemudian menampilkan alamat penerima pertama yang belum digunakan di wallet kamu, untuk mencegah penggunaan ulang alamat, karena praktik ini sangat buruk bagi privasi. Kamu kemudian bisa meneruskan alamat ini kepada orang atau layanan yang perlu mengirimkan Bitcoin kepada kamu.



![Image](assets/fr/27.webp)



Setelah transaksi disiarkan di jaringan, transaksi akan secara otomatis muncul di halaman beranda aplikasi.



![Image](assets/fr/28.webp)



## 6. Kirim bitcoin dengan Ashigaru



Sekarang setelah kamu memiliki bitcoin di Ashigaru wallet, kamu juga bisa mengirimkannya. Untuk melakukannya, tekan tombol `+` di kanan bawah, lalu pilih tombol `Kirim` berwarna merah.



![Image](assets/fr/29.webp)



Kemudian pilih akun dari mana kamu ingin melakukan pengeluaran. Untuk saat ini, kita belum membahas akun `Postmix`, yang disediakan untuk koin bersama, yang akan kita bahas di tutorial selanjutnya. Jadi kita akan mengirim dana dari akun deposit utama.



![Image](assets/fr/30.webp)



Masukkan detail transaksi kamu: jumlah yang akan dikirim dan alamat Bitcoin penerima.



![Image](assets/fr/31.webp)



Dengan mengklik tiga titik kecil di sudut kanan atas, kemudian pada `Show unspent outputs`, kamu juga dapat memilih dengan tepat UTXO mana yang ingin Anda keluarkan, untuk meningkatkan privasi kamu.



![Image](assets/fr/32.webp)



Setelah kamu mengisi semua detail, klik panah putih di bagian bawah antarmuka untuk melanjutkan.



Kamu kemudian akan dibawa ke halaman ringkasan yang menampilkan semua detail transaksi kamu. Beberapa elemen penting ditampilkan:




- Di blok `Tujuan`, periksa terakhir kali bahwa alamat penerima dan jumlah yang dikirim sudah benar.  
- Pada blok `Biaya`, kamu bisa melihat tarif biaya yang dipilih secara otomatis oleh Ashigaru dan, jika perlu, memodifikasinya dengan mengeklik `MANAGE`.  
- Blok `Transaksi` menunjukkan jenis transaksi yang akan dilakukan. Di sini, kita berbicara tentang transaksi sederhana, tetapi Ashigaru juga mendukung jenis transaksi yang dioptimalkan untuk privasi, yang akan dibahas secara rinci dalam tutorial mendatang.  
- Blok merah `Peringatan Transaksi` memperingatkan kamu jika transaksi menunjukkan pola yang dapat dikenali oleh alat analisis rantai, yang bisa membahayakan privasi. Dengan mengekliknya, kamu bisa melihat detailnya. Sebagai contoh, dalam kasusku, Ashigaru memberi tahu bahwa jumlah yang dikirim adalah bulat (`3000 sats`), sehingga aku bisa menyimpulkan hasil mana yang sesuai dengan pengeluaran dan mana yang merupakan pertukaran. Untuk mempelajari lebih lanjut tentang heuristik analisis rantai ini, aku mengundang kamu mengikuti pelatihan BTC 204 di Plan ₿ Academy.  
- Terakhir, kamu bisa menambahkan label pada transaksi untuk mencatat tujuannya.




https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Setelah kamu memeriksa semua informasi, gunakan tanda panah hijau untuk mengirim bitcoin. Tahan panah, lalu seret ke kanan untuk mengonfirmasi pengiriman.



![Image](assets/fr/33.webp)



Transaksi kamu telah disiarkan di jaringan Bitcoin.



![Image](assets/fr/34.webp)



## 7. Memulihkan Ashigaru wallet kamu



Pemulihan Ashigaru wallet sedikit berbeda dari Bitcoin wallet klasik, karena aplikasi ini menggunakan metode yang sama dengan Samourai Wallet. Jika kamu kehilangan akses ke wallet (entah karena lupa PIN, menghapus instalasinya, atau kehilangan ponsel), ada beberapa cara untuk memulihkan Bitcoin kamu.



Jika kamu masih memiliki akses ke ponsel, atau telah membuat cadangan file ini, metode paling sederhana adalah menggunakan file cadangan `ashigaru.txt`. File ini berisi semua informasi yang diperlukan untuk memulihkan portofolio pada instance baru Ashigaru (atau pada Sparrow Wallet), tetapi file ini dienkripsi dengan passphrase yang telah kamu tetapkan pada langkah 3.1 tutorial ini. Oleh karena itu, kamu harus memiliki file `ashigaru.txt` dan passphrase untuk menggunakan metode ini.



Dengan kedua elemen ini, kamu bisa, misalnya, memulihkan portofolio pada Sparrow Wallet.




![Image](assets/fr/35.webp)



Jika kamu tidak memiliki akses ke file `ashigaru.txt`, kamu masih bisa mendapatkan kembali akses ke dana dengan menggunakan frasa mnemonik dan passphrase, sama seperti untuk portofolio Bitcoin lainnya. Aku sarankan melakukan pemulihan ini pada instance Ashigaru yang baru, atau langsung pada Sparrow Wallet, agar lebih mudah memulihkan jalur bypass dari Whirlpool jika kamu menggunakannya. Atau, kamu bisa mengimpor informasi ini ke perangkat lunak lain yang kompatibel dengan BIP39 dengan memasukkan jalur turunan secara manual.



Untuk informasi lebih lanjut tentang proses ini, silakan baca tutorial lengkap yang sudah aku tulis mengenai cara memulihkan Samourai Wallet dan wallet lainnya. Karena Ashigaru adalah fork, prosedurnya pun sama:



https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

Seperti yang kamu lihat, apa pun metode pemulihan yang digunakan, passphrase sangat diperlukan. Jadi, pastikan untuk mencadangkannya dengan hati-hati. Kamu juga bisa membuat beberapa salinan, tergantung strategi keamanan kamu.



## 8. Perbarui aplikasi



Untuk memperbarui aplikasi Ashigaru, karena kamu menginstalnya dari file `.apk` dan bukan melalui Play Store seperti aplikasi biasa, kamu harus mengunduh file `.apk` baru yang sesuai dengan versi terbaru, lalu menginstalnya secara manual.



Ulangi langkah-langkah yang dijelaskan di bagian 2 tutorial ini, kecuali saat kamu mengklik file `.apk` untuk memulai penginstalan, **ponsel Android akan menawarkan opsi `Update`, bukan `Install`.




![Image](assets/fr/41.webp)



Ini adalah poin yang sangat penting: jika Android menampilkan `Install` dan bukannya `Update`, kamu mungkin menginstal versi yang salah. Dalam hal ini, segera hentikan prosedur instalasi.



Seperti instalasi pertama, periksa keaslian dan integritas file `.apk` sebelum melanjutkan pembaruan.



Untuk mengetahui kapan versi baru tersedia, periksa situs web resmi Ashigaru dari waktu ke waktu. Tenang aja, Ashigaru adalah aplikasi yang stabil dan matang, yang diwarisi dari Samourai Wallet, dan pembaruannya relatif jarang dibandingkan dengan perangkat lunak yang lebih muda.



## 9. Donasi untuk proyek Ashigaru



Ashigaru adalah proyek sumber terbuka. Jika Anda ingin mendukung pengembangannya, kamu dapat memberikan donasi langsung dari aplikasi melalui PayNym.



Untuk melakukannya, klik PayNym Anda di bagian kanan atas antarmuka, lalu pilih kode pembayaran yang dimulai dengan `PM...`.



![Image](assets/fr/36.webp)



Kemudian tekan tombol `+` di bagian kanan bawah layar.



![Image](assets/fr/37.webp)



Pilih `Ashigaru Open Source Project` sebagai penerima.



![Image](assets/fr/38.webp)



Klik tombol `CONNECT` untuk membuat saluran komunikasi BIP47 (lebih lanjut tentang protokol ini dalam tutorial di bawah).



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)



Setelah transaksi notifikasi dikonfirmasi, kamu dapat mengirimkan donasi ke proyek dengan mengklik panah putih kecil di sudut kanan atas antarmuka.



![Image](assets/fr/40.webp)



Sekarang kamu tahu bagaimana cara menggunakan fitur-fitur dasar aplikasi Ashigaru. Dalam tutorial selanjutnya, kita akan melihat cara memanfaatkan transaksi pembelanjaan tingkat lanjut, serta Whirlpool, implementasi coinjoin yang diwarisi dari Samurai Wallet.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add
