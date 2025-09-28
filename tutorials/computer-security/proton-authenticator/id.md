---
name: Proton Authenticator
description: Bagaimana cara menggunakan Proton Authenticator untuk mengamankan akun saya dengan 2FA?
---
![cover](assets/cover.webp)



Autentikasi dua faktor (2FA) menambahkan penghalang keamanan tambahan pada akun Anda dengan mengharuskan, selain kata sandi, bukti tambahan bahwa hanya Anda yang memilikinya. Mengaktifkan 2FA secara drastis mengurangi risiko peretasan, bahkan jika kata sandi Anda dibobol melalui phishing atau kebocoran data. Tanpa 2FA, penyerang hanya membutuhkan kata sandi Anda untuk mengakses akun Anda; dengan 2FA, dia juga membutuhkan faktor kedua Anda, menggagalkan sebagian besar upaya pencurian akun.



Ada berbagai jenis 2FA. Kode SMS lebih baik daripada tidak sama sekali, tetapi tetap rentan terhadap serangan pertukaran SIM dan intersepsi. Kami tidak merekomendasikan SMS sebagai 2FA utama. Aplikasi otentikasi (TOTP) generate kode sementara secara lokal di perangkat Anda, sehingga lebih sulit untuk disadap. Kunci keamanan fisik menawarkan keamanan terbaik, tetapi membutuhkan perangkat keras khusus.



Proton Authenticator adalah pengautentikasi TOTP. Ini adalah respons Proton terhadap keterbatasan aplikasi yang ada: banyak yang bersifat eksklusif, berisi pelacak iklan dan tidak menawarkan cadangan terenkripsi. Proton Authenticator membedakan dirinya dengan menyediakan aplikasi sumber terbuka, bebas dari iklan dan pelacak, dengan cadangan terenkripsi ujung ke ujung.



## Memperkenalkan Proton Authenticator



Proton Authenticator adalah aplikasi otentikasi TOTP seluler dan desktop yang dikembangkan oleh Proton, yang terkenal dengan layanan yang berfokus pada privasi. Seperti semua produk Proton, aplikasi ini bersifat open source dan telah menjalani audit keamanan independen. Aplikasi ini tersedia secara gratis di semua platform (Android, iOS, Windows, macOS, Linux).



Proton Authenticator menawarkan fitur-fitur utama berikut ini:





- Pembuatan kode **TOTP** untuk akun 2FA Anda, kompatibel dengan sebagian besar situs yang menggunakan Google Authenticator, Authy, dll.





- **Pencadangan awan terenkripsi opsional**: Anda dapat menautkan aplikasi ke akun Proton Anda untuk mencadangkan dan menyinkronkan kode Anda dengan enkripsi ujung ke ujung. Jika Anda kehilangan perangkat Anda, cukup sambungkan kembali perangkat yang baru untuk memulihkan semua kode Anda.





- **Sinkronisasi multi-perangkat**: dengan masuk ke Proton di aplikasi, kode 2FA Anda secara otomatis disinkronkan di antara beberapa perangkat melalui enkripsi ujung ke ujung. Pada iOS, alternatifnya adalah sinkronisasi melalui iCloud.





- **Penguncian lokal dengan kata sandi atau biometrik**: aplikasi ini menawarkan penguncian PIN dan/atau sidik jari / ID Wajah. Jadi, meskipun seseorang secara fisik mengakses ponsel Anda yang tidak terkunci, mereka tidak akan dapat membuka Proton Authenticator.





- **Tidak ada pengumpulan data atau pelacak**: Proton berkomitmen untuk tidak mengumpulkan data pribadi melalui aplikasi. Tidak ada iklan tersembunyi atau analisis perilaku.





- **Impor/ekspor yang mudah**: salah satu keunggulan Proton Authenticator adalah panduan impor untuk akun yang sudah ada, yang kompatibel dengan aplikasi lain (Google Authenticator, Authy, Aegis, dll.). Anda juga dapat mengekspor kode Anda ke sebuah file jika diperlukan.



Singkatnya, Proton Authenticator bertujuan untuk menjadi solusi 2FA tanpa kompromi: aman, privat, fleksibel.



## Instalasi



Proton Authenticator tersedia secara gratis di semua platform. Untuk mengunduh aplikasi, buka halaman resminya: [https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)



![PROTON AUTHENTICATOR](assets/fr/01.webp)



*Halaman resmi Proton Authenticator yang menunjukkan fitur utama aplikasi dan Interface*



Di halaman ini, Anda akan menemukan tautan unduhan untuk semua sistem operasi: Android, iOS, Windows, macOS, dan Linux. Cukup klik pada sistem operasi pilihan Anda dan ikuti langkah-langkah instalasi standar.



Dalam tutorial ini, kami akan menunjukkan cara memasang dan mengonfigurasinya di macOS, lalu kita akan melihat cara memasang aplikasi di iOS dan menyinkronkan kode Anda di antara kedua perangkat.



### Instalasi di macOS



Setelah Anda mengunduh dan menginstal aplikasi, luncurkan Proton Authenticator. Saat pertama kali diluncurkan, aplikasi akan memandu Anda melalui beberapa layar konfigurasi awal:



![PROTON AUTHENTICATOR](assets/fr/02.webp)



*Layar selamat datang Proton Authenticator dengan pesan "Keamanan di setiap kode" dan tombol "Mulai "*



### Impor awal



Jika Proton Authenticator mendeteksi bahwa Anda sebelumnya menggunakan aplikasi 2FA lain, wizard impor mungkin muncul. Ini mendukung impor langsung dari aplikasi tertentu (Google Authenticator, 2FAS, Authy, Aegis, dll.). Atau, Anda bisa melewatkan langkah ini dan menambahkan akun secara manual nanti.



![PROTON AUTHENTICATOR](assets/fr/03.webp)



*Panduan impor untuk mentransfer kode dari aplikasi autentikasi lain*



![PROTON AUTHENTICATOR](assets/fr/04.webp)



*Aplikasi impor yang kompatibel: 2FAS, Aegis Authenticator, Authy, Bitwarden Authenticator, Ente Auth, dan Google Authenticator*



### Perlindungan aplikasi lokal



Tetapkan PIN buka kunci, atau aktifkan buka kunci biometrik (Touch ID) jika tersedia. Langkah ini sangat penting untuk mencegah siapa pun yang menggunakan Mac Anda mendapatkan akses gratis ke kode 2FA.



![PROTON AUTHENTICATOR](assets/fr/05.webp)



*Layar konfigurasi Touch ID dengan pesan "Lindungi data Anda" dan tombol "Aktifkan Touch ID "*



### Opsi sinkronisasi



Aplikasi ini juga memungkinkan Anda mengaktifkan sinkronisasi iCloud untuk mencadangkan data dengan aman di antara perangkat Apple Anda.



![PROTON AUTHENTICATOR](assets/fr/06.webp)



*Opsi sinkronisasi iCloud dengan pesan "Cadangkan data Anda dengan aman dengan sinkronisasi iCloud terenkripsi "*



Setelah langkah-langkah ini selesai, Proton Authenticator siap digunakan.



![PROTON AUTHENTICATOR](assets/fr/07.webp)



*Interface Proton Authenticator kosong utama dengan opsi "Buat kode baru" dan "Impor kode "*



## Tambahkan akun 2FA dengan ProtonMail



Sekarang kita akan melihat cara menambahkan kode 2FA pertama Anda, dengan menggunakan ProtonMail sebagai contoh. Metode ini bekerja sama untuk semua layanan yang mendukung autentikasi dua faktor.



### Mengaktifkan 2FA di ProtonMail



Pertama-tama, Anda dapat membaca panduan kami untuk ProtonMail untuk informasi lebih lanjut:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

Masuk ke akun ProtonMail Anda dan buka pengaturan keamanan. Cari opsi "Autentikasi dua faktor" dan aktifkan.



![PROTON AUTHENTICATOR](assets/fr/08.webp)



*Halaman pengaturan ProtonMail dengan opsi "Aplikasi autentikator" di bagian "Otentikasi dua faktor "*



Klik pada tombol untuk mengaktifkan autentikator dan ProtonMail akan meminta Anda untuk memilih aplikasi autentikasi.



![PROTON AUTHENTICATOR](assets/fr/09.webp)



*Jendela konfigurasi ProtonMail 2FA dengan tombol "Batal" dan "Berikutnya"*



ProtonMail kemudian akan menampilkan kode QR untuk Anda pindai dengan aplikasi autentikasi Anda.



![PROTON AUTHENTICATOR](assets/fr/10.webp)



*Kode QR ProtonMail untuk dipindai dengan aplikasi autentikasi Anda, dengan opsi "Masukkan kunci secara manual sebagai gantinya" tersedia*



Jika Anda lebih suka memasukkan kunci secara manual, klik "Masukkan kunci secara manual" untuk melihat kunci rahasia.



![PROTON AUTHENTICATOR](assets/fr/11.webp)



*Memasukkan informasi 2FA secara manual: Kunci, Interval (30) dan Angka (6)*



### Pindai kode QR dengan Proton Authenticator



Di Proton Authenticator di macOS, klik "Buat kode baru". Aplikasi ini menawarkan beberapa opsi: **Pindai kode QR** atau **Masukkan kunci secara manual**.



Gunakan kamera Mac Anda untuk memindai kode QR yang ditampilkan pada layar ProtonMail. Setelah Anda memindai kode QR, Anda akan dibawa ke layar konfigurasi kode yang baru.



![PROTON AUTHENTICATOR](assets/fr/12.webp)



*Jendela pembuatan entri baru dengan Judul (ProtonMail), Rahasia, Pengirim (Proton), parameter digit, dan bidang interval*



Proton Authenticator akan secara otomatis mengisi informasi tersebut. Anda dapat menyesuaikan nama jika Anda mau, lalu klik "Simpan".



![PROTON AUTHENTICATOR](assets/fr/13.webp)



*Kode TOTP yang dihasilkan untuk ProtonMail (848 812) dengan sisa waktu yang ditampilkan*



### Memvalidasi konfigurasi



ProtonMail akan meminta Anda memasukkan kode 6 digit yang dihasilkan oleh Proton Authenticator untuk mengonfirmasi bahwa 2FA berfungsi dengan benar.



![PROTON AUTHENTICATOR](assets/fr/14.webp)



*Layar validasi ProtonMail yang meminta Anda memasukkan kode 6 digit (848812)*



Salin kode dari aplikasi (dengan mengkliknya) dan tempelkan ke ProtonMail untuk menyelesaikan aktivasi.



Setelah divalidasi, ProtonMail akan meminta Anda untuk mengunduh kode pemulihan. Sangat penting untuk menyimpannya dengan hati-hati.



![PROTON AUTHENTICATOR](assets/fr/15.webp)



*Layar kode pemulihan ProtonMail dengan daftar kode penyelamatan dan tombol "Unduh "*



### Kode darurat



Saat menambahkan akun, simpan kode pemulihan yang disediakan oleh layanan. Sebagian besar situs menawarkan kode pemulihan statis dan sekali pakai untuk disimpan di tempat yang aman. Simpan kode cadangan ini di luar Proton Authenticator sehingga Anda dapat mengakses akun Anda jika Anda kehilangan akses ke aplikasi 2FA.



## Instalasi iOS dan impor kode



Setelah Anda menyiapkan Proton Authenticator di macOS, Anda mungkin juga ingin menggunakannya di iPhone atau iPad. Berikut ini cara mendapatkan kode 2FA di beberapa perangkat.



### Unduh aplikasi di iOS



Buka App Store dan cari "Proton Authenticator". Unduh dan instal aplikasi pada perangkat iOS Anda.



![PROTON AUTHENTICATOR](assets/fr/16.webp)



*Proses instalasi di iOS: layar selamat datang, wizard impor, pemilihan aplikasi yang kompatibel, dan layar "Impor kode dari Proton Authenticator "* terakhir



### Metode 1: Ekspor/Impor melalui file JSON



Jika Anda tidak menggunakan sinkronisasi otomatis (akun iCloud atau Proton), Anda harus mentransfer kode secara manual dari Mac ke iPhone:



**Langkah 1 - Ekspor dari macOS**:



Di Mac Anda, buka Proton Authenticator dan masuk ke Pengaturan (ikon roda gigi). Di menu, klik "Ekspor".



![PROTON AUTHENTICATOR](assets/fr/17.webp)



*Menu pengaturan Proton Authenticator di macOS dengan opsi "Ekspor" yang terlihat*



![PROTON AUTHENTICATOR](assets/fr/18.webp)



*Jendela ekspor dengan nama file "Proton_Authenticator_backup_2025" dan tombol "Simpan" *



Simpan file JSON di Mac Anda. Anda dapat mengirimkannya melalui email yang aman atau menyimpannya di iCloud Drive untuk akses dari iPhone Anda.



**Langkah 2 - Impor di iOS** :



Pada iPhone Anda, instal Proton Authenticator dan selama konfigurasi, pilih untuk mengimpor kode. Pilih "Proton Authenticator" dari daftar dan impor file JSON.



![PROTON AUTHENTICATOR](assets/fr/19.webp)



*Proses impor di iOS: Pelokalan file JSON, konfirmasi impor, dan layar konfigurasi dengan opsi Face ID dan iCloud*



### Metode 2: Sinkronisasi otomatis



**Melalui akun Proton (untuk sinkronisasi multi-platform)**:



Jika Anda belum membuat akun Proton dan ingin menyinkronkan antara sistem operasi yang berbeda, aplikasi akan meminta Anda untuk membuat atau menghubungkan akun Proton.



![PROTON AUTHENTICATOR](assets/fr/20.webp)



*Layar sinkronisasi perangkat yang meminta Anda untuk membuat akun Proton gratis atau menyambungkan ke akun yang sudah ada*



**Melalui iCloud (hanya untuk ekosistem Apple)** :


Jika Anda hanya menggunakan perangkat Apple, Anda dapat memilih sinkronisasi iCloud dalam pengaturan aplikasi. Metode ini akan secara otomatis dan aman menyinkronkan kode Anda di antara semua perangkat Apple Anda, tanpa memerlukan akun Proton.



## Pencadangan dan pemulihan terenkripsi



Salah satu fitur utama Proton Authenticator adalah pencadangan kode 2FA yang menyeluruh, memastikan bahwa kehilangan atau pergantian perangkat tidak berarti Anda harus memulai dari awal lagi.



### Enkripsi ujung ke ujung



Ketika berbicara tentang pencadangan awan terenkripsi dengan Proton Authenticator, rahasia TOTP Anda dienkripsi secara lokal di perangkat Anda sebelum dikirim ke server Proton. Dekripsi hanya dapat dilakukan oleh Anda, pada perangkat yang terhubung ke akun Proton Anda. Proton AG tidak memiliki kunci untuk membaca kode yang Anda daftarkan.



Di iOS, jika Anda memilih iCloud daripada akun Proton, data Anda dienkripsi dengan standar Apple. Pencadangan lokal di Android memungkinkan Anda mengenkripsi file cadangan dengan kata sandi pilihan Anda.



### Pemulihan jika terjadi kehilangan



Jika ponsel Anda hilang, dicuri, atau Anda berganti handset:



**Dengan pencadangan Proton diaktifkan**: Instal Proton Authenticator pada perangkat baru. Selama penyiapan awal, masuk ke akun Proton yang sama. Segera, aplikasi akan menyinkronkan dan mengunduh semua kode 2FA Anda dari cadangan terenkripsi.



**Dengan cadangan iCloud (iOS)**: Hubungkan iPhone/iPad baru dengan ID Apple yang sama dan pastikan untuk mengaktifkan Rantai Kunci iCloud. Setelah menginstal Proton Authenticator, sambungkan ke iCloud. Kode Anda akan disinkronkan melalui iCloud dan muncul.



**Tidak ada pencadangan awan**: Anda harus mengimpor akun Anda secara manual. Jika Anda telah mengekspor file cadangan, gunakan fungsi Impor di Proton Authenticator. Dalam skenario terburuk, jika Anda tidak memiliki cadangan, Anda harus menggunakan kode cadangan untuk setiap layanan, atau menghubungi dukungan.



Proton Authenticator memungkinkan Anda mengekspor akun Anda kapan saja, baik sebagai file terenkripsi atau sebagai kode QR multi-akun. Opsi ini memberi Anda jaminan tambahan.



## Praktik terbaik



Menggunakan autentikator 2FA sangat meningkatkan keamanan Anda, tetapi praktik terbaik tertentu harus diperhatikan:



### Menyimpan kode darurat Anda



Ketika Anda mengaktifkan 2FA pada sebuah layanan, Anda sering kali diberikan daftar kode pemulihan. Simpanlah kode-kode tersebut di ponsel Anda (di atas kertas, di dalam pengelola kata sandi terenkripsi, dll.). Jika terjadi kehilangan total pada autentikator Anda, kode-kode statis ini akan menyelamatkan Anda.



### Jangan mencampur kata sandi dan kode 2FA Anda



Sangat menggoda untuk menggunakan pengelola kata sandi yang juga menyimpan TOTP. Namun, menyimpan kata sandi dan kode 2FA di tempat yang sama akan menciptakan satu titik kegagalan dan melemahkan autentikasi ganda. Untuk keamanan maksimum, banyak ahli merekomendasikan untuk memisahkan dua faktor: kata sandi dalam pengelola yang aman, dan kode 2FA dalam aplikasi terpisah seperti Proton Authenticator. Namun, menggunakan manajer terintegrasi masih lebih baik daripada tidak memiliki 2FA sama sekali.



### Mengaktifkan beberapa metode 2FA



Idealnya, gunakan lebih dari satu faktor kedua pada akun-akun penting Anda. Jangan ragu untuk menambahkan kunci keamanan fisik jika layanan mengizinkannya. Lihat tutorial kami tentang kunci fisik Yubikey untuk informasi lebih lanjut:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Selain itu, simpanlah kode darurat yang telah dicetak.



### Tetap berhati-hati dan lindungi perangkat Anda



Jangan biarkan siapa pun mencari ponsel Anda yang tidak terkunci. Dengan Proton Authenticator, kode Anda dilindungi oleh PIN/biometrik - jangan membocorkan PIN ini. Demikian pula, waspadalah terhadap phishing: bahkan dengan 2FA, jika Anda memberikan kode ke situs palsu secara real time, kode tersebut dapat digunakan oleh penyerang.



### Pembaruan dan audit



Selalu perbarui Proton Authenticator (pembaruan untuk memperbaiki kekurangan yang mungkin terjadi). Karena kode ini terbuka, komunitas melakukan audit informal, dan Proton mempublikasikan hasil audit formal.



## Perbandingan dengan aplikasi lain



Bagaimana Proton Authenticator dibandingkan dengan aplikasi autentikasi lainnya? Inilah ringkasan komparatifnya:



**Pengautentikasi Proton**: Sumber terbuka, cadangan awan terenkripsi E2EE opsional, sinkronisasi multi-perangkat, penguncian lokal, tidak ada pelacakan, tersedia di ponsel dan desktop.



**Autentikator Google**: Hak milik, pencadangan melalui akun Google sejak tahun 2023 tetapi tanpa enkripsi ujung ke ujung (kunci dapat dilihat oleh Google), sinkronisasi multi-perangkat ditambahkan pada tahun 2023, tidak ada kunci aplikasi secara default, berisi pelacak Google.



**Aegis Authenticator**: Sumber terbuka, hanya cadangan lokal, tidak ada sinkronisasi cloud, kunci kode/biometrik, tidak ada pelacakan, hanya untuk Android.



**Authy**: Cadangan awan yang dienkripsi dengan kata sandi tetapi kode tertutup, sinkronisasi multi-perangkat, kunci PIN/sidik jari, mengumpulkan nomor telepon, aplikasi desktop dihentikan pada bulan Maret 2024.



Anda dapat menemukan panduan kami untuk Authy di bawah ini:



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Proton Authenticator adalah salah satu solusi paling komprehensif dan aman yang tersedia: sumber terbuka, sinkronisasi terenkripsi multi-perangkat, tanpa tindak lanjut komersial.



## Sumber daya dan dukungan



### Dokumentasi resmi




- **Situs web resmi**: [proton.me/authenticator](https://proton.me/authenticator) - Presentasi dan unduhan produk
- **Halaman unduhan**: [proton.me/en/authenticator/download](https://proton.me/fr/authenticator/download) - Tautan untuk semua OS
- **Dukungan Proton**: [proton.me/support/two-factor-authentication-2fa](https://proton.me/support/two-factor-authentication-2fa) - Panduan aktivasi 2FA resmi
- **Blog Proton**: [proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - Pengumuman dan fitur rinci



### Kode sumber dan transparansi




- **GitHub Proton Authenticator**: [github.com/ProtonMail/proton-authenticator](https://github.com/ProtonMail/proton-authenticator) - Kode sumber terbuka
- **Audit keamanan**: [proton.me/community/security-audits](https://proton.me/community/security-audits) - Laporan audit independen



### Uji keamanan yang disarankan


Setelah konfigurasi, uji pengaturan Anda:




- [Have I Been Been Pwned] (https://haveibeenpwned.com/) - Periksa apakah akun Anda telah disusupi
- [Direktori 2FA] (https://2fa.directory/) - Daftar layanan yang mendukung 2FA



### Komunitas dan diskusi




- Reddit r/Proton: [reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - Komunitas resmi Proton
- **Forum Panduan Privasi** : [discuss.privacyguides.net](https://discuss.privacyguides.net) - Diskusi teknis tentang masalah privasi
- Reddit **r/privacy**: [reddit.com/r/privacy](https://reddit.com/r/privacy) - Kiat-kiat privasi umum



### Lainnya




- [Have I Been Been Pwned] (https://haveibeenpwned.com/) - Periksa apakah akun Anda telah disusupi
- [Direktori 2FA] (https://2fa.directory/) - Daftar layanan yang mendukung 2FA