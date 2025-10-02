---
name: Aegis Authenticator
description: Bagaimana cara menggunakan Aegis Authenticator untuk mengamankan akun Anda dengan autentikasi ganda?
---

![cover](assets/cover.webp)



Saat ini, autentikasi dua faktor (2FA) sangat penting untuk mengamankan akun online. Selain kata sandi, ini menambahkan faktor kedua (biasanya berupa kode 6 digit) yang akan kedaluwarsa setelah 30 detik, sehingga sangat menyulitkan peretas. Menggunakan aplikasi TOTP (*Time-based One-Time Password*) khusus lebih aman daripada SMS, yang dapat dibajak oleh serangan pertukaran SIM.



Namun, tidak semua aplikasi autentikasi diciptakan sama. Banyak solusi eksklusif (Google Authenticator, Authy, dll.) yang menimbulkan masalah: mereka bersifat eksklusif dan bersumber tertutup (tidak mungkin mengaudit keamanannya), terkadang mengintegrasikan pelacak iklan, tidak menawarkan cadangan terenkripsi untuk kode-kode Anda, dan bahkan bisa mencegah mengekspor akun Anda untuk mengunci Anda ke dalam ekosistem mereka.



Aegis Authenticator, di sisi lain, menghadirkan dirinya sebagai alternatif yang gratis dan etis untuk aplikasi-aplikasi ini. Aegis merupakan sebuah aplikasi sumber terbuka yang gratis, aman, untuk mengelola token verifikasi dua langkah Anda pada Android. Pengembangannya berfokus pada fitur-fitur penting yang tidak ditawarkan oleh aplikasi lain, termasuk enkripsi yang kuat untuk data lokal dan kemungkinan pencadangan yang aman. Secara keseluruhan, Aegis menawarkan solusi autentikasi ganda lokal yang dapat diaudit, ideal bagi siapa saja yang ingin mempertahankan kendali penuh atas kode 2FA mereka.



## Memperkenalkan Aegis Authenticator



Aegis Authenticator merupakan aplikasi 2FA sumber terbuka untuk Android, dirilis di bawah lisensi GPL v3. Aplikasi ini menonjol karena filosofi "privasi sesuai desain": aplikasi ini bekerja sepenuhnya secara offline dan tidak memerlukan koneksi ke layanan jarak jauh. Hasilnya, token Anda tetap tersimpan secara lokal pada perangkat Anda, dalam brankas yang aman dan hanya Anda yang memegang kuncinya.



### Fitur utama



**Brankas terenkripsi:** semua kode OTP Anda disimpan dalam brankas terenkripsi AES-256 (mode GCM), dilindungi oleh kata sandi utama yang ditentukan pengguna. Anda dapat membuka kunci brankas ini melalui kata sandi atau data biometrik (sidik jari, pengenalan wajah) untuk menambah kenyamanan. Jika tidak ada kata sandi, data tidak akan terenkripsi - jadi kami sangat menyarankan agar Anda menetapkannya.



**Organisasi tingkat lanjut:** Aegis membuat banyak akun 2FA Anda terorganisir dengan baik. Anda bisa mengurutkan entri Anda menurut abjad atau urutan pilihan Anda, mengelompokkannya berdasarkan kategori (misalnya Pribadi, Pekerjaan, Sosial) untuk memudahkan pencarian, dan memberikan setiap entri sebuah ikon yang dipersonalisasi. Bilah pencarian disertakan untuk menemukan layanan atau akun berdasarkan nama secara instan.



**Cadangan lokal terenkripsi:** Untuk memastikan Anda tidak akan pernah kehilangan akses ke akun-akun Anda, Aegis menawarkan cadangan otomatis untuk brankas Anda. Cadangan ini dienkripsi (melalui kata sandi) dan dapat disimpan di lokasi pilihan Anda (penyimpanan internal, folder cloud, dll.). Aplikasi ini juga bisa mengekspor basis data akun Anda secara manual, dalam format terenkripsi atau tidak terenkripsi sesuai kebutuhan. Mengimpor akun dari aplikasi 2FA lainnya juga sama mudahnya (Aegis mendukung impor dari Authy, Google Authenticator, FreeOTP, andOTP, dll.).



**Keamanan dan privasi:** aplikasi ini sepenuhnya offline secara default. Tidak memerlukan izin jaringan - yang berarti tidak mengirimkan data ke dunia luar, dan tidak memiliki pelacak iklan atau modul analisis perilaku. Aegis tidak menampilkan iklan, dan tidak memerlukan akun pengguna: segera setelah diinstal, dia langsung aktif dan berjalan tanpa registrasi. Karena kode sumbernya tersedia untuk umum di GitHub, komunitas bisa mengauditnya dengan bebas, menjamin tidak adanya fungsi berbahaya atau tersembunyi.



**Interface Modern:** Aegis mengadopsi Desain Material yang rapi, dengan dukungan tema gelap (termasuk mode AMOLED) dan bahkan tampilan ubin opsional untuk menampilkan kode Anda sebagai kisi-kisi. Interface tidak berantakan, tanpa embel-embel, dan mencegah tangkapan layar kode sebagai langkah keamanan.



## Instalasi



Karena Aegis Authenticator merupakan sumber terbuka, pengembangnya lebih menyukai saluran distribusi yang ramah privasi. Ada dua cara utama untuk menginstalnya:



### Melalui F-Droid (disarankan)



Cara yang paling aman dan mudah adalah melalui F-Droid, toko alternatif gratis. Jika F-Droid belum terinstal di ponsel Anda, mulailah dengan mengunduhnya dari situs web resmi [F-Droid.org] (https://f-droid.org). Kemudian :





- Buka F-Droid dan pastikan Anda telah memperbarui repositori untuk mendapatkan daftar aplikasi terbaru
- Cari "Aegis Authenticator" di F-Droid. Aplikasi resmi akan muncul (penerbit: Beem Development)
- Mulai instalasi dengan menekan Install. Karena Aegis adalah salah satu aplikasi yang diverifikasi oleh F-Droid, Anda mendapatkan keuntungan dari unduhan yang andal dan aman



Menginstal melalui F-Droid menawarkan keuntungan untuk menerima pembaruan aplikasi secara otomatis segera setelah dirilis. Terlebih lagi, F-Droid menjamin bahwa aplikasi ini bebas dari komponen eksklusif yang tidak diinginkan.



### Melalui GitHub (APK yang ditandatangani)



Jika Anda lebih suka menginstal aplikasi tanpa melalui toko, Anda bisa mengunduh APK resmi langsung dari halaman GitHub proyek. Pada repositori Aegis ([github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis)), buka bagian Rilis di mana versi stabil diterbitkan.





- Unduh versi APK terbaru
- Sebelum menginstal APK, pastikan Anda telah mengesahkan instalasi aplikasi dari sumber yang tidak dikenal pada perangkat Anda (di Pengaturan Android)
- APK yang disediakan di GitHub ditandatangani oleh pengembang dengan kunci yang sama seperti di F-Droid



Setelah instalasi manual, aplikasi akan berfungsi secara identik. Harap dicatat bahwa pembaruan tidak akan otomatis: Anda harus memeriksa GitHub secara berkala untuk versi baru.



### Google Play Store vs F-Droid



Aegis Authenticator tersedia di Google Play Store dan F-Droid, memberikan Anda pilihan metode instalasi:



**Google Play Store:**




- ✅ Pembaruan otomatis yang terintegrasi ke dalam sistem Android
- ✅ Instalasi yang sederhana dan familiar
- ✅ APK bertanda tangan yang sama seperti di saluran lain



**F-Droid (disarankan): **F-Droid (disarankan)




- ✅ Toko sumber terbuka dan gratis
- ✅ Konstruksi yang dapat direproduksi dan diverifikasi
- ✅ Tidak diperlukan layanan Google
- ✅ Menghormati filosofi perangkat lunak bebas



Pilihan di antara kedua opsi ini tergantung pada preferensi Anda mengenai ekosistem Google. Jika Anda lebih menyukai kesederhanaan, Play Store sangat ideal. Jika Anda menginginkan pendekatan yang lebih ramah privasi, terlepas dari layanan Google, F-Droid adalah pilihan yang lebih baik.



## Konfigurasi pertama



Ketika Aegis diluncurkan untuk pertama kalinya, prosedur konfigurasi awal diusulkan untuk mengamankan kode 2FA Anda dengan aman:



![Configuration initiale Aegis](assets/fr/01.webp)



*Proses konfigurasi Aegis awal: layar selamat datang, pilihan keamanan, definisi kata sandi utama, dan finalisasi*



### Mengatur kata sandi utama



Aegis pertama-tama akan meminta Anda untuk memilih kata sandi utama. Kata sandi ini akan digunakan untuk mengenkripsi semua token autentikasi Anda yang tersimpan di brankas. Kami sangat menyarankan agar Anda membuat kata sandi yang kuat dan unik yang hanya Anda yang tahu.



**⚠️ Peringatan:** Jangan lupa kata sandi ini - jika Anda lupa, kode 2FA terenkripsi Anda tidak akan dapat diakses (tidak ada pintu belakang). Aegis akan meminta Anda memasukkan kata sandi dua kali untuk konfirmasi.



### Mengaktifkan pembukaan kunci biometrik (opsional)



Jika perangkat Android Anda dilengkapi dengan pembaca sidik jari atau sensor biometrik lainnya, Aegis akan meminta Anda untuk mengaktifkan pembukaan kunci biometrik. Opsi ini opsional tetapi sangat praktis: memungkinkan Anda membuka kunci aplikasi dengan cepat menggunakan sidik jari atau wajah, daripada mengetikkan kata sandi setiap kali.



Perhatikan bahwa biometrik adalah kenyamanan tambahan: kata sandi utama Anda masih diperlukan jika biometrik diubah atau perangkat dihidupkan ulang.



### Temukan pengaturan aplikasi



Setelah Anda berada di dalam aplikasi (Interface utama pada awalnya kosong), biasakan diri Anda dengan opsi konfigurasi yang tersedia. Akses pengaturan melalui menu tarik-turun di bagian kanan atas layar (tiga titik vertikal), lalu pilih "Pengaturan".



![Interface principale et paramètres](assets/fr/02.webp)



*Aegis utama Interface kosong saat memulai, akses ke menu parameter dan ikhtisar opsi yang tersedia*



Menu pengaturan Aegis mengelompokkan beberapa bagian penting:





- **Penampilan**: Menyesuaikan tema (terang, gelap, AMOLED), bahasa, dan pengaturan visual lainnya
- **Perilaku**: Mengonfigurasi perilaku aplikasi saat berinteraksi dengan daftar entri
- **Paket ikon**: mengelola dan mengimpor paket ikon untuk menyesuaikan tampilan dan nuansa akun Anda
- **Keamanan**: Pengaturan untuk enkripsi, pembukaan kunci biometrik, penguncian otomatis, dan parameter keamanan lainnya
- **Cadangan**: Konfigurasikan pencadangan otomatis ke lokasi pilihan Anda
- **Impor & Ekspor**: Mengimpor cadangan dari aplikasi autentikasi lain dan mengekspor brankas Aegis Anda secara manual
- **Log audit**: Log terperinci dari semua peristiwa penting dalam aplikasi



Organisasi yang jelas ini memungkinkan Anda mengonfigurasi Aegis sesuai dengan preferensi dan kebutuhan keamanan Anda.



## Menambahkan akun 2FA



Setelah Aegis terkonfigurasi, mari kita lanjutkan ke hal yang lebih penting: menambahkan akun dua faktor Anda. Prosesnya sederhana, dan Aegis menawarkan beberapa metode untuk mengintegrasikan kode autentikasi Anda.



### Tiga metode penambahan yang tersedia



Dari Aegis Interface utama, tekan tombol **+** di kanan bawah untuk mengakses opsi tambah. Anda memiliki tiga pilihan:





- **Memindai kode QR**: Memindai secara langsung kode QR yang ditampilkan oleh layanan web
- **Memindai gambar**: Memindai kode QR dari gambar yang tersimpan di perangkat Anda
- **Masukkan secara manual**: Masukkan informasi akun 2FA secara manual



### Contoh praktis: mengkonfigurasi Bitwarden



Mari kita ambil contoh konkret aktivasi 2FA di Bitwarden untuk mengilustrasikan prosesnya:



![Exemple avec Bitwarden](assets/fr/04.webp)



*Contoh aktivasi 2FA di Bitwarden: Web Interface dengan opsi autentikasi dan rekomendasi Aegis*





- **Masuk dan mengakses pengaturan**: Masuk ke akun Bitwarden Anda dan akses pengaturan, tab "Keamanan"
- **Bagian Penyedia**: Buka bagian "Penyedia" dan klik "Kelola" di bagian "Aplikasi autentikator"



![Configuration 2FA avec QR code](assets/fr/05.webp)



*Menyelesaikan proses penambahan akun: Kode QR ditampilkan oleh layanan, kunci rahasia terlihat dan kode verifikasi dimasukkan*





- **Pindai kode QR**: Jendela popup terbuka dengan kode QR dan kunci rahasia
- Dalam **Aegis**: Gunakan "Pindai kode QR" untuk menangkap informasi secara otomatis
- **Verifikasi**: Masukkan kode 6 digit yang dihasilkan oleh Aegis di bidang "Kode verifikasi"
- **Aktivasi**: Klik "Nyalakan" untuk menyelesaikan aktivasi



### Menambahkan detail secara manual



Jika Anda lebih suka atau tidak dapat memindai kode QR, gunakan opsi "Masukkan secara manual". Formulir ini memungkinkan Anda untuk memasukkan :



![Ajout d'un compte 2FA](assets/fr/03.webp)



*Proses untuk menambahkan akun 2FA baru: Interface kosong, opsi tambah, formulir entri manual, dan akun berhasil ditambahkan*





- **Nama** : Nama layanan (mis. Bitwarden, GitHub...)
- **Penerbit** : Penerbit (sering kali identik dengan nama)
- **Grup**: Opsional, untuk mengatur akun Anda berdasarkan kategori
- **Catatan**: Komentar pribadi di akun ini
- **Rahasia** : Kunci rahasia yang disediakan oleh layanan (disembunyikan secara default)
- **Tingkat Lanjut**: Parameter lanjutan (algoritme, periode, jumlah digit)



Setelah akun ditambahkan, akun tersebut akan muncul di daftar Anda dengan kode saat ini dan indikator waktu yang menunjukkan waktu yang tersisa sebelum pembaruan.



### Kompatibilitas universal



Aegis kompatibel dengan semua layanan yang menggunakan standar TOTP dan HOTP, termasuk hampir semua situs yang menawarkan 2FA: jejaring sosial, bank, pengelola kata sandi, platform kripto, dll.



### Organisasi pintu masuk



Setelah Anda menambahkan beberapa akun, Anda akan menghargai alat organisasi Aegis:





- **Pengurutan khusus:** Secara default, akun didaftarkan dalam urutan abjad, tetapi Anda dapat mengubah urutannya secara manual
- **Grup dan kategori:** Buat grup untuk memisahkan akun pribadi Anda dari akun bisnis, atau kelompokkan berdasarkan jenis layanan (perbankan, email, jejaring sosial, dll.)
- **Ikon yang disesuaikan:** Aegis mencoba untuk secara otomatis menetapkan ikon yang sesuai jika tersedia, jika tidak, Anda dapat memilih dari banyak ikon umum atau mengimpor gambar
- **Pencarian cepat:** Bilah pencarian di bagian atas memungkinkan Anda mengetikkan beberapa huruf untuk langsung menyaring entri yang cocok



Dengan menyentuh entri, kode OTP ditampilkan dalam ukuran penuh (jika disembunyikan) dan Anda dapat menyalinnya ke clipboard dengan menekan lama - berguna untuk menempelkannya ke dalam aplikasi yang ingin Anda sambungkan.



## Keamanan dan pencadangan



Dengan keamanan sebagai inti dari Aegis, penting untuk memahami bagaimana kode 2FA Anda dilindungi, dan bagaimana memastikannya tetap ada jika terjadi masalah.



### Arsitektur keamanan



**Enkripsi yang kuat**: Semua kode Anda disimpan dalam brankas terenkripsi menggunakan **algoritma AES-256 dalam mode GCM**, digabungkan dengan kata sandi utama Anda. Penurunan kunci didasarkan pada **scrypt**, menawarkan perlindungan yang lebih baik terhadap serangan brute force.



**Pembukaan kunci yang aman**: Kata sandi utama diperlukan untuk mendekripsi data Anda. Biometrik (opsional) menggunakan **Android Secure Keystore** dan TEE (Lingkungan Eksekusi Tepercaya) untuk melindungi kunci enkripsi.



**Izin minimal**: Aegis beroperasi secara offline secara default, hanya memerlukan akses ke kamera (pemindaian QR), biometrik, dan vibrator. Tidak ada data yang dikumpulkan atau dibagikan.



### Opsi pencadangan



Aegis menawarkan beberapa strategi pencadangan yang sesuai dengan kebutuhan keamanan dan kenyamanan yang berbeda:



![Configuration des sauvegardes](assets/fr/06.webp)



*Interface lengkap dengan akun yang ditambahkan, peringatan pencadangan, pengaturan pencadangan otomatis, dan strategi pencadangan*



**1. Pencadangan lokal otomatis**




- Konfigurasikan folder tujuan pilihan Anda
- Frekuensi yang dapat disesuaikan (setelah setiap perubahan, setiap hari, dll.)
- File terenkripsi yang dilindungi kata sandi (.aesvault)
- Kompatibel dengan folder yang disinkronkan (Nextcloud, Dropbox, dll.)



![Sélection du dossier de sauvegarde](assets/fr/07.webp)



*Proses pemilihan folder cadangan: penjelajah file, folder tujuan, dan otorisasi akses*



**2. Pencadangan awan Android**




- Integrasi opsional dengan sistem cadangan Android
- Hanya tersedia untuk brankas terenkripsi (keamanan terjaga)
- Pencadangan transparan dengan data Android lainnya
- Pemulihan otomatis saat pergantian perangkat



**3. Ekspor secara manual**




- Ekspor sesuai permintaan melalui **Pengaturan > Impor & Ekspor**
- Pilihan format terenkripsi (disarankan) atau format yang jelas
- Berguna untuk migrasi atau pencadangan sesekali



### Praktik-praktik keselamatan yang baik





- Simpan beberapa versi **cadangan** untuk mencegah kerusakan
- **Uji** cadangan Anda secara teratur dengan mencoba memulihkannya
- Simpan kode pemulihan yang disediakan oleh layanan Anda secara terpisah
- Kata sandi utama **Anda** masih diperlukan bahkan dengan cadangan awan
- **Amankan kata sandi utama Anda**: gunakan kata sandi yang unik dan kuat yang disimpan dalam pengelola kata sandi
- Selalu perbarui **aplikasi Anda** dengan patch keamanan terbaru
- Aktifkan **penguncian otomatis** dalam pengaturan untuk mengamankan akses ke aplikasi
- Nonaktifkan **tangkapan layar** (opsi default) untuk mencegah kode Anda disadap
- **Gunakan biometrik dengan hemat**: lebih memilih kata sandi untuk akses penting



## Perbandingan dengan aplikasi lain



Bagaimana Aegis dibandingkan dengan aplikasi autentikasi populer lainnya?



### Aegis vs Google Authenticator



** Aegis :**




- ✅ Sumber terbuka dan dapat diaudit
- ✅ Cadangan terenkripsi lokal
- ✅ Organisasi lanjutan (grup, ikon, pencarian)
- ✅ Tidak ada pengumpulan data
- ❌ Hanya untuk Android



**Pengesahan Google :**




- ✅ Tersedia di Android dan iOS
- ✅ Sinkronisasi awan (sejak tahun 2023)
- ❌ Kode sumber tertutup
- ❌ Fungsionalitas terbatas
- ❌ Potensi pengumpulan data Google



### Aegis vs Authy



** Aegis :**




- ✅ Sumber terbuka
- ✅ Tidak diperlukan akun
- ✅ Ekspor kode dimungkinkan
- ✅ Kontrol data total
- ❌ Tidak ada sinkronisasi multi-perangkat asli



** Authy :**




- ✅ Sinkronisasi multi-perangkat
- ✅ Tersedia di Android dan iOS
- ❌ Kode sumber tertutup
- ❌ Memerlukan nomor telepon
- ❌ Tidak dapat mengekspor kode
- ❌ Aplikasi desktop dihapus pada bulan Maret 2024



Aegis unggul bagi pengguna Android yang menghargai transparansi, keamanan lokal, dan kontrol penuh atas data mereka. Alternatif seperti Authy lebih cocok jika Anda benar-benar membutuhkan sinkronisasi multi-perangkat otomatis.




## Kesimpulan



Aegis Authenticator merupakan solusi yang sangat baik bagi mereka yang mencari aplikasi 2FA yang ramah privasi, aman, dan transparan. Pendekatan sumber terbukanya, dikombinasikan dengan enkripsi yang tangguh dan Interface yang rapi, menjadikannya pilihan terbaik untuk mengamankan akun online Anda.



Meskipun terbatas pada Android dan tidak memiliki sinkronisasi cloud asli, Aegis lebih dari sekadar menebus keterbatasan ini dengan filosofi "privasi menurut desain" dan kontrol data total. Bagi para pengguna yang peduli dengan privasi digital mereka, Aegis menawarkan alternatif yang kredibel dan kuat untuk solusi-solusi eksklusif yang dominan di pasar.



Keamanan akun online Anda tidak harus bergantung pada niat baik perusahaan komersial. Dengan Aegis, Anda tetap memegang kendali atas kode autentikasi Anda, dalam brankas digital yang kuncinya hanya Anda sendiri yang memegangnya.



## Sumber daya



### Situs web resmi




- **Situs web resmi**: [getaegis.app](https://getaegis.app/) - Presentasi dan pengunduhan aplikasi
- **Kode sumber**: [github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis) - Repositori resmi GitHub
- **F-Droid**: [f-droid.org/packages/com.beemdevelopment.aegis](https://f-droid.org/packages/com.beemdevelopment.aegis/) - Instalasi melalui toko gratis



### Dokumentasi teknis




- **Dokumentasi lemari besi**: [Desain Vault](https://github.com/beemdevelopment/Aegis/blob/master/docs/vault.md) - Deskripsi teknis enkripsi dan arsitektur yang aman
- **Pertanyaan Umum Resmi**: [getaegis.app/#faq](https://getaegis.app/#faq) - Jawaban atas pertanyaan yang sering diajukan
- **Wiki proyek**: [github.com/beemdevelopment/Aegis/wiki](https://github.com/beemdevelopment/Aegis/wiki) - Dokumentasi pengguna lengkap