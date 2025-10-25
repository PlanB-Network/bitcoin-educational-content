---
name: Ente Auth
description: Pengautentikasi 2FA terenkripsi sumber terbuka dan ujung ke ujung
---
![cover](assets/cover.webp)



Autentikasi dua faktor (2FA) menjadi sangat penting untuk mengamankan akun online kita. Selain kata sandi Anda yang biasa, diperlukan kode sementara, biasanya dibuat oleh aplikasi khusus. Mekanisme ini, yang dikenal sebagai TOTP (Time-Based One-Time Password), menjamin bahwa meskipun kata sandi Anda dibobol, penyerang tidak akan bisa mengakses akun Anda tanpa memiliki faktor kedua ini, yang diperbaharui setiap 30 detik.



Namun, memilih aplikasi otentikasi yang tepat bukanlah hal yang sepele. Google Authenticator, meskipun populer, memiliki keterbatasan utama: kode kepemilikan yang tidak mungkin diaudit, sinkronisasi tanpa enkripsi ujung ke ujung, dan risiko kehilangan kode secara keseluruhan jika terjadi masalah pada ponsel Anda. Solusi lain, seperti Authy, membutuhkan nomor telepon dan tidak menjamin kerahasiaan total.



**Ente Auth** menonjol sebagai alternatif yang modern dan aman. Aplikasi gratis, open source, dan lintas platform ini, yang dikembangkan oleh tim di balik [Ente Photos](https://ente.io), menawarkan pencadangan awan terenkripsi ujung ke ujung dan sinkronisasi tanpa batas di antara semua perangkat Anda. Tidak seperti solusi eksklusif, Ente Auth memberi Anda kontrol penuh atas kode otentikasi Anda tanpa mengorbankan privasi Anda.



Dalam tutorial ini, kami akan menunjukkan kepada Anda langkah demi langkah cara menginstal dan menggunakan Ente Auth, dan mengapa solusi ini berbeda dari autentikator tradisional.



## Memperkenalkan Ente Auth



Ente Auth dikembangkan oleh tim di balik Ente Photos, sebuah layanan penyimpanan foto yang terenkripsi secara menyeluruh dan ramah privasi. Sesuai dengan filosofi Ente ("Ente" berarti "milikku" dalam bahasa Melayu, melambangkan kontrol atas data Anda), Ente Auth dirancang untuk memberikan pengguna kembali kendali penuh atas kode otentikasi dua faktor mereka.



### Fitur utama



**Kode TOTP standar**: Ente Auth menghasilkan kode sementara yang kompatibel dengan sebagian besar layanan (GitHub, Google, Binance, ProtonMail, dll.). Anda bisa menambahkan akun 2FA sebanyak yang Anda butuhkan, dan aplikasi ini menghitung kode-kode tersebut berdasarkan rahasia yang disediakan.



**Pencadangan awan terenkripsi dari ujung ke ujung**: Kode Anda disimpan dengan aman secara online. Hanya Anda yang dapat mendekripsinya - kunci enkripsi berasal dari kata sandi Anda dan hanya diketahui oleh Anda. Ente (server) tidak memiliki pengetahuan tentang rahasia Anda, atau bahkan judul akun Anda, karena semuanya dienkripsi di sisi klien menggunakan arsitektur tanpa pengetahuan.



**Sinkronisasi multi-perangkat**: Anda dapat menginstal Ente Auth di beberapa perangkat (ponsel cerdas, tablet, komputer) dan mengakses kode Anda di semua perangkat tersebut. Setiap perubahan secara otomatis dan langsung disebarkan ke perangkat Anda yang lain melalui cloud terenkripsi, memberikan Anda fleksibilitas yang tinggi dalam pekerjaan sehari-hari.



**Interface yang minimalis dan intuitif**: Aplikasi ini menawarkan Interface yang ramping, mudah dipelajari bahkan oleh pengguna non-teknis. akun 2FA ditampilkan dengan nama layanan, login Anda dan kode 6 digit, yang diperbarui secara real time. Ente Auth juga menampilkan kode berikutnya beberapa detik sebelumnya untuk menghindari kedaluwarsa.



**Sumber terbuka dan telah diaudit**: Kode sumber Ente Auth adalah [publik di GitHub] (https://github.com/ente-io/auth) di bawah lisensi AGPL v3.0. Setiap pengembang dapat mengauditnya untuk memeriksa kekurangan atau perilaku yang tidak diinginkan. Kriptografi yang diimplementasikan telah menjadi subjek dari [audit eksternal independen] (https://ente.io/blog/cryptography-audit/), sebuah jaminan keseriusan keamanan aplikasi.



### Keuntungan dan keterbatasan



**Manfaat:**




- Privasi berdasarkan desain dengan enkripsi ujung ke ujung
- Sinkronisasi yang aman antara semua perangkat Anda
- Kode sumber terbuka yang dapat diaudit
- Interface pengguna yang jelas dan intuitif Interface
- Pencadangan otomatis untuk mencegah hilangnya kode
- Tersedia di semua platform (seluler dan desktop)



**Batas:**




- Diperlukan koneksi internet untuk sinkronisasi
- Pengguna tingkat lanjut mungkin lebih memilih solusi offline 100% seperti Aegis (khusus Android)
- Relatif baru dibandingkan dengan solusi yang sudah ada



## Instalasi



Ente Auth tersedia di sebagian besar platform populer. Anda dapat mengunduh aplikasi ini dari [situs web resmi] (https://ente.io/auth) atau dari toko-toko resmi.



![Installation d'Ente Auth](assets/fr/01.webp)



*Halaman unduhan Ente Auth dengan semua platform yang tersedia*



### Android


Anda memiliki beberapa opsi:




- **Google Play Store**: Cari "Ente Auth" untuk instalasi klasik
- **F-Droid**: Tersedia dari katalog aplikasi sumber terbuka Android, dengan jaminan konstruksi terverifikasi dan tidak ada konten eksklusif
- **Instalasi manual**: File APK dapat diunduh dari [halaman GitHub proyek](https://github.com/ente-io/auth/releases) dengan pemberitahuan terintegrasi tentang versi baru



### iOS (iPhone/iPad)


Instal Ente Auth langsung dari Apple App Store dengan mencari nama aplikasinya. Aplikasi iOS juga dapat dijalankan pada Mac yang dilengkapi dengan chip Apple Silicon (M1/M2) melalui Mac App Store.



### Komputer (Windows, macOS, Linux)


Ente Auth menawarkan aplikasi desktop asli. Kunjungi [ente.io/download] (https://ente.io/download) atau [bagian Rilis GitHub] (https://github.com/ente-io/auth/releases):





- **Windows**: Penginstal EXE disertakan
- **macOS**: Seret dan lepaskan gambar disk DMG di Aplikasi
- **Linux**: Tersedia beberapa format (AppImage portable, .deb untuk Debian/Ubuntu, .rpm untuk Fedora/Red Hat)



**Catatan:** Tutorial ini didasarkan pada Ente Auth v4.4.4 dan yang lebih baru. Versi sebelumnya mungkin memiliki sedikit perbedaan Interface.



### Interface Web


Tanpa instalasi, Anda dapat mengakses kode Anda melalui [auth.ente.io](https://auth.ente.io) dari browser apa pun. Web Interface terbatas untuk melihat kode (berguna untuk pemecahan masalah), karena menambahkan akun memerlukan aplikasi seluler atau desktop untuk alasan keamanan.



## Konfigurasi pertama



### Pembuatan akun



Saat pertama kali meluncurkan Ente Auth, Anda memiliki dua opsi:



![Premier lancement d'Ente Auth](assets/fr/02.webp)



*Layar beranda Ente Auth dengan opsi pembuatan akun*



**Dengan akun (disarankan)**: Pilih "Buat Akun" dan masukkan email Anda Address dan kata sandi. **Penting**: kata sandi ini berfungsi sebagai kata sandi utama untuk mengenkripsi data Anda. Pilihlah kata sandi yang kuat dan unik, karena tidak ada prosedur pengaturan ulang konvensional tanpa kehilangan data. Jika Anda salah memasukkannya, data terenkripsi Anda tidak akan dapat dipulihkan.



**Mode Offline**: Pilih "Gunakan tanpa cadangan" untuk menggunakan aplikasi secara lokal tanpa cloud. Dalam mode ini, kode Anda tetap ada di perangkat, tetapi Anda harus mengekspornya secara manual agar tidak hilang.



![Vérification email et récupération de clé](assets/fr/03.webp)



*Proses verifikasi email dan pembuatan kunci pemulihan 24 kata*



Verifikasi email mungkin diminta untuk memvalidasi pembuatan akun dan mengaktifkan pemulihan pada perangkat baru. Ente Auth juga akan memberi Anda kunci pemulihan 24 kata (berdasarkan metode BIP39). **Anda harus menyimpan kunci ini di tempat yang aman: kunci ini adalah satu-satunya cara untuk memulihkan data jika Anda lupa kata sandi.**



### Keamanan lokal



Saya sangat menyarankan untuk mengaktifkan perlindungan lokal dengan kode atau biometrik. Buka **Pengaturan → Keamanan → Layar kunci** dan konfigurasikan:





- **Pembukaan kunci biometrik**: ID wajah, sidik jari, tergantung pada kemampuan perangkat Anda
- **PIN/kata sandi khusus aplikasi**
- **Penundaan Penguncian Otomatis**: misalnya "Segera" atau setelah 30 detik tidak ada aktivitas



Perlindungan ini mencegah akses yang tidak sah ke kode Anda jika seseorang mendapatkan akses ke ponsel Anda yang tidak terkunci. Perhatikan bahwa kunci ini merupakan penghalang tambahan: data Anda tetap terenkripsi secara end-to-end meskipun tanpa perlindungan ini.



## Menambahkan akun 2FA



### Prosedur standar



Untuk menambahkan akun 2FA baru, mari kita ambil contoh konkret untuk mengaktifkan 2FA pada Bull Bitcoin:



![Configuration du premier compte](assets/fr/04.webp)



*Interface utama Ente Auth siap untuk menambahkan akun 2FA* pertama



**Sisi layanan (Bull Bitcoin)**: Masuk ke akun Bull Bitcoin Anda, buka pengaturan keamanan, dan aktifkan autentikasi dua faktor.



![Paramètres de sécurité Bull Bitcoin](assets/fr/05.webp)



*Menu pengaturan keamanan Interface Bull Bitcoin*



![Activation 2FA Bull Bitcoin](assets/fr/06.webp)



*Opsi untuk mengaktifkan autentikasi dua faktor pada Bull Bitcoin*



Layanan ini kemudian akan menampilkan kode QR untuk Anda pindai dengan aplikasi autentikasi Anda:



![QR code 2FA Bull Bitcoin](assets/fr/07.webp)



*Kode QR yang dihasilkan oleh Bull Bitcoin untuk dipindai dengan autentikator Anda*



**Masuk ke Ente Auth**: Klik "Masukkan kunci pengaturan" lalu pindai kode QR yang ditampilkan oleh Bull Bitcoin. Ente Auth akan secara otomatis mengenali akun dan mengisi kolom-kolomnya.



![Ajout du compte dans Ente Auth](assets/fr/08.webp)



*Mengkonfigurasi detail akun Bull Bitcoin di Ente Auth*



Anda dapat menyesuaikan nama layanan dan login Anda agar lebih mudah ditemukan. Pengaturan lanjutan (algoritme SHA1, periode 30-an, 6 digit) umumnya sudah benar secara default.



**Validasi sisi layanan**: Kembali ke Bull Bitcoin dan masukkan kode 6 digit yang dihasilkan oleh Ente Auth untuk menyelesaikan aktivasi.



![Saisie du code 2FA](assets/fr/09.webp)



*Masukkan kode yang dihasilkan oleh Ente Auth untuk memvalidasi aktivasi 2FA*



![2FA activée](assets/fr/10.webp)



*Konfirmasi aktivasi 2FA yang berhasil pada Bull Bitcoin*



**Kode cadangan**: Bull Bitcoin akan memberi Anda kode pemulihan. **Simpan kode-kode tersebut di tempat yang aman, terpisah dari autentikator Anda.**



![Gestion des codes de sauvegarde](assets/fr/11.webp)



*Opsi untuk kode cadangan darurat generate pada Bull Bitcoin*



![Codes de récupération](assets/fr/12.webp)



*Daftar kode pemulihan untuk disimpan di tempat yang aman*



### Organisasi dan manajemen



Ente Auth menawarkan beberapa fitur praktis:



**Salin Cepat**: Tekan kode untuk menyalinnya secara otomatis ke clipboard.



**Tindakan yang peka terhadap konteks**: Tekan terus (atau klik kanan pada desktop) untuk mengedit, menghapus, berbagi, atau menyematkan entri.



**Tag dan pencarian**: Atur akun Anda dengan tag (pribadi/profesional, berdasarkan kategori layanan) dan gunakan bilah pencarian untuk memfilter dengan cepat.



![Création d'un tag](assets/fr/17.webp)



*Proses pembuatan tag: menu kontekstual dan dialog pembuatan*



![Tag appliqué](assets/fr/18.webp)



*Tag "Bitcoin" berhasil diterapkan pada akun Bull Bitcoin*



**Ikon otomatis**: Setiap entri dapat diilustrasikan dengan logo layanan, berkat integrasi paket ikon [Ikon Sederhana] (https://simpleicons.org/).



**Berbagi aman sementara**: Fitur Ente Auth yang unik, berbagi aman memungkinkan Anda mengirimkan kode 2FA ke kolega tanpa mengungkapkan rahasia yang mendasarinya. generate tautan terenkripsi yang berlaku selama maksimum 2, 5 atau 10 menit - penerima melihat kode secara real time, tetapi tidak dapat mengekspor atau mengakses data akun. Metode ini ideal untuk bantuan teknis atau kolaborasi sementara, menawarkan tingkat keamanan yang tidak dapat dilakukan dengan tangkapan layar atau pesan teks sederhana.



![Partage sécurisé](assets/fr/19.webp)



*Interface berbagi aman sementara: pilih durasi (5 menit)*



**Ekspor/impor yang aman**: Ente Auth memungkinkan Anda mengekspor kode Anda ke aplikasi lain, atau mengimpornya dari Google Authenticator dan solusi lainnya. Ekspor dilakukan melalui file terenkripsi atau kode QR, menjamin portabilitas data Anda tanpa mengorbankan keamanan.



**Kunci pemulihan BIP39**: Aplikasi ini secara otomatis menghasilkan frasa pemulihan 24 kata sesuai dengan standar BIP39 (Bitcoin Improvement Proposal), yang identik dengan dompet mata uang kripto. Frasa ini adalah kunci pemulihan utama Anda, yang memungkinkan Anda untuk memulihkan semua kode Anda bahkan jika Anda lupa kata sandi utama Anda.



## Konfigurasi dan pengaturan



Ente Auth menawarkan banyak opsi penyesuaian yang dapat diakses melalui pengaturan aplikasi:



![Paramètres principaux d'Ente Auth](assets/fr/13.webp)



*Ikhtisar parameter yang tersedia di Ente Auth*



### Manajemen akun dan data



![Paramètres de sécurité](assets/fr/14.webp)



*Opsi keamanan tingkat lanjut: verifikasi email, kode PIN, sesi aktif*



Pengaturan keamanan memungkinkan Anda untuk :




- Mengaktifkan verifikasi email untuk koneksi baru
- Aktifkan Kunci Sandi
- Melihat sesi aktif di berbagai perangkat Anda
- Menyiapkan kode PIN atau biometrik



### Interface dan opsi penggunaan



![Paramètres généraux](assets/fr/15.webp)



*Parameter Interface dan kustomisasi aplikasi*



Pengaturan umum meliputi :




- **Bahasa**: Interface multibahasa
- **Tampilan**: Ikon besar, mode ringkas
- **Privasi**: Sembunyikan kode, pencarian cepat
- **Telemetri**: Pelaporan kesalahan (dapat dinonaktifkan)



## Pencadangan dan sinkronisasi



### Bagaimana enkripsi bekerja



Ketika Anda menambahkan akun dengan akun Ente yang terhubung, aplikasi ini segera mengenkripsi data sensitif ini secara lokal menggunakan kunci utama Anda (berasal dari kata sandi Anda). Data yang terenkripsi kemudian dikirim ke server Ente untuk disimpan.



Berkat mekanisme ini, cadangan awan terenkripsi end-to-end dari kode-kode Anda selalu tersedia. Jika Anda kehilangan perangkat Anda, cukup instal ulang Ente Auth dan sambungkan kembali: aplikasi ini akan secara otomatis mengunduh dan mendekripsi semua kode Anda.



### Sinkronisasi multi-perangkat



Jika Anda menggunakan Ente Auth pada ponsel cerdas dan komputer, setiap penambahan atau perubahan pada satu perangkat akan muncul dalam hitungan detik pada perangkat lainnya. Sinkronisasi ini dilakukan melalui cloud Ente, tetapi karena data dienkripsi dari ujung ke ujung, server hanya melihat konten terenkripsi yang tidak dapat dibaca.



![Synchronisation mobile](assets/fr/16.webp)



*Demo sinkronisasi: akun Bull Bitcoin yang sama dapat diakses di ponsel dan desktop*



Sinkronisasi sangat mudah: instal Ente Auth pada ponsel cerdas Anda, masuk dengan kredensial Anda, dan semua kode 2FA Anda (di sini Bull Bitcoin) muncul secara otomatis. Contoh di atas menunjukkan sinkronisasi yang sempurna antara desktop dan seluler - kode Bull Bitcoin yang sama dapat diakses di kedua perangkat.



Dalam hal kerahasiaan, baik Ente maupun pihak ketiga mana pun tidak memiliki akses ke rahasia 2FA Anda. Bahkan metadata (tag, catatan, nama layanan) dienkripsi sebelum dikirim. Arsitektur tanpa pengetahuan ini memastikan bahwa hanya Anda yang dapat menguraikan kode Anda.



### Penggunaan offline



Sinkronisasi membutuhkan Internet, tetapi Ente Auth bekerja dengan sempurna secara offline di setiap perangkat, karena semua data disimpan secara lokal. Perubahan offline akan diantrekan dan disinkronkan segera setelah koneksi pulih.



## Keamanan dan privasi



### Jaminan kriptografi



Ente Auth didasarkan pada enkripsi end-to-end yang kuat dengan arsitektur tanpa pengetahuan. Kode Anda dienkripsi dengan kunci yang hanya Anda sendiri yang memegangnya, yang berasal dari kata sandi utama Anda menggunakan fungsi derivasi kunci tingkat lanjut.



**Arsitektur tanpa pengetahuan:** Ente tidak dapat mengakses data Anda secara fisik. Bahkan metadata (nama layanan, tag, catatan) dienkripsi di sisi klien sebelum transmisi. Pendekatan ini memastikan bahwa, jika terjadi serangan pada server Anda atau permintaan pemerintah, Ente hanya dapat mengungkapkan data terenkripsi yang tidak dapat dibaca tanpa kata sandi Anda.



**Enkripsi lokal**: Proses enkripsi dilakukan sepenuhnya di perangkat Anda sebelum dikirim ke cloud. Server Ente hanya menerima dan menyimpan data yang terenkripsi, sehingga akses yang tidak sah menjadi tidak mungkin, bahkan untuk administrator layanan.



### Transparansi dan audit



Karena kodenya [open source](https://github.com/ente-io/auth), komunitas dapat memverifikasi ketiadaan pintu belakang. Ente telah memiliki [beberapa audit eksternal](https://ente.io/blog/cryptography-audit/) yang dilakukan untuk memvalidasi keamanan implementasinya:





- **Cure53** (Jerman): Audit keamanan aplikasi dan kriptografi
- **Perangkat Lunak Simbolik** (Prancis): Keahlian kriptografi khusus
- **Dapat disalahgunakan** (India): Pengujian penetrasi dan analisis kerentanan



Audit independen ini, yang dilakukan oleh perusahaan-perusahaan yang diakui, menjamin bahwa implementasi kriptografi Ente Auth mematuhi praktik keamanan terbaik dan tidak memiliki kekurangan yang kritis.



### Kebijakan privasi



Ente Auth menerapkan [kebijakan privasi yang patut dicontoh](https://ente.io/privacy/) berdasarkan pengumpulan data minimal. Hanya informasi yang benar-benar diperlukan untuk pengoperasian layanan yang disimpan: email Anda Address untuk otentikasi dan pemulihan akun.



**Tidak ada pelacakan atau telemetri**: Tidak seperti kebanyakan aplikasi, Ente Auth tidak mengumpulkan metrik penggunaan, tidak mengidentifikasi data kerusakan, dan tidak ada informasi perilaku. Aplikasi ini bekerja tanpa iklan yang mengganggu atau pelacak analitik.



**Kepatuhan terhadap GDPR**: Ente sepenuhnya mematuhi Peraturan Perlindungan Data Umum Eropa. Anda memiliki hak untuk mengakses, memperbaiki, atau menghapus data Anda kapan saja. Ekspor data] (https://ente.io/take-control/) hanya dengan sekali klik, dan menghapus akun Anda secara permanen akan menghapus semua data Anda dari server.



**Penyimpanan yang terdesentralisasi dan aman**: Data terenkripsi Anda direplikasi pada 3 penyedia yang berbeda, di 3 negara yang berbeda, menjamin ketersediaan yang optimal sambil menghindari ketergantungan pada satu penyedia cloud.



Model bisnis Ente didasarkan pada layanan Ente Photos berbayar, yang memungkinkan kami untuk menawarkan Ente Auth **gratis dan tanpa batasan** tanpa mengorbankan privasi Anda dengan memonetisasi data Anda. Pendekatan ini menjamin keberlanjutan layanan tanpa bergantung pada iklan atau penjualan kembali data pribadi.



## Perbandingan dengan solusi lain



| Application              | Open Source | Sauvegarde Cloud | E2EE | Sync multi-devices | Plateformes                                        |
| ------------------------ | ----------- | ---------------- | ---- | ------------------ | -------------------------------------------------- |
| **Ente Auth**            | ✅           | ✅                | ✅    | ✅                  | Android, iOS, Linux, macOS, Windows                |
| **Google Authenticator** | ❌           | ✅ (sans E2EE)    | ❌    | ✅                  | Android, iOS                                       |
| **Aegis**                | ✅           | ❌                | ✅    | ❌                  | Android                                            |
| **Authy**                | ❌           | ✅                | ❌    | ✅                  | Android, iOS *(apps desktop supprimées août 2024)* |
| **Proton Auth**          | ✅           | ✅                | ✅    | ✅                  | Android, iOS *(récent, moins établi)*              |

Ente Auth menonjol sebagai salah satu dari sedikit solusi yang menggabungkan semua keunggulan: transparansi kode sumber, pencadangan awan terenkripsi, dan sinkronisasi lintas platform.



## Kasus penggunaan yang disarankan



### Pengguna perorangan



Ente Auth sangat ideal untuk individu yang sadar akan keamanan yang secara sistematis mengaktifkan 2FA. Anda tidak perlu lagi khawatir kehilangan kode saat mengganti ponsel, atau harus memilih antara kenyamanan dan keamanan.



### Penggunaan bersama keluarga dan beberapa perangkat



Aplikasi ini menjadi sangat berguna jika Anda menggunakan beberapa perangkat. Anda dapat menyimpan kode di ponsel cerdas dan tablet, atau berbagi kode keluarga tertentu (Netflix, cloud keluarga) secara sinkron dan aman.



### Penggunaan profesional



Untuk tim yang mengelola akun-akun sensitif, Ente Auth memfasilitasi kolaborasi sekaligus menjaga keamanan, berkat fitur berbagi canggihnya yang terintegrasi ke dalam bagian "Organisasi dan manajemen".



## Praktik terbaik





- **Simpan kode darurat Anda**: Simpan kode pemulihan yang disediakan oleh setiap layanan dari ponsel Anda.





- **Gunakan kata sandi utama yang kuat**: Kata sandi utama Ente Auth Anda harus unik dan kuat, karena kata sandi ini melindungi semua kode Anda.





- **Mengaktifkan perlindungan lokal**: Konfigurasikan PIN atau biometrik untuk mencegah akses fisik yang tidak sah.





- Jangan melakukan penyesuaian yang berlebihan: Hindari modifikasi tingkat lanjut yang dapat mengganggu sinkronisasi.





- **Selalu perbarui aplikasi**: Memperbaiki kelemahan keamanan dan meningkatkan fungsionalitas.





- **Uji pemulihan**: Sesekali periksa apakah Anda dapat memulihkan kode Anda di perangkat lain.



## Kesimpulan



Ente Auth merupakan solusi modern dan komprehensif untuk autentikasi dua faktor. Dengan menggabungkan keamanan, transparansi, dan kemudahan penggunaan, aplikasi sumber terbuka ini memenuhi kebutuhan pengguna yang menuntut tanpa mengorbankan kenyamanan.



Tidak seperti solusi eksklusif yang mengunci Anda ke dalam ekosistem yang tidak jelas, Ente Auth memberi Anda kembali kendali atas data otentikasi Anda sekaligus melindungi Anda dari kehilangan yang tidak disengaja berkat cadangannya yang terenkripsi.



Entah Anda seorang individu yang ingin mengamankan akun pribadi Anda, atau sebuah tim yang mengelola akses bisnis, Ente Auth merupakan pilihan cerdas untuk memodernisasi pendekatan Anda terhadap keamanan digital tanpa mengorbankan privasi.



## Sumber daya dan dukungan



### Dokumentasi resmi




- **Situs web resmi**: [ente.io/auth](https://ente.io/auth)
- **Pusat bantuan**: [help.ente.io/auth](https://help.ente.io/auth)
- **Blog teknis**: [ente.io/blog](https://ente.io/blog)



### Kode sumber dan transparansi




- **GitHub**: [github.com/ente-io/auth](https://github.com/ente-io/auth)
- **Audit kriptografi**: [ente.io/blog/cryptography-audit](https://ente.io/blog/cryptography-audit)



### Komunitas




- **Perselisihan**: [discord.gg/z2YVKkycX3](https://discord.gg/z2YVKkycX3)
- **Reddit**: [r/enteio](https://reddit.com/r/enteio)