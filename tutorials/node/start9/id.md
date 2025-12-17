---
name: Start9

description: Tutorial tentang menyiapkan server pribadi Start9

---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=DzikmY4S42Y)


*Berikut ini adalah sebuah video tutorial dari Southern Bitcoiner, sebuah panduan video yang menunjukkan kepada Anda bagaimana cara mengatur dan menggunakan server pribadi Start9/StartOS, dan bagaimana menjalankan sebuah node bitcoin.*


## 1️⃣ Pendahuluan


### Apa sebenarnya Start9 itu?


Start9 adalah perusahaan yang didirikan pada tahun 2020, yang terkenal karena mengembangkan [**StartOS**,] (https://github.com/Start9Labs/start-os), sistem operasi berbasis Linux yang dirancang untuk server pribadi. Sistem operasi ini memungkinkan pengguna untuk dengan mudah meng-host sendiri berbagai layanan perangkat lunak-seperti Bitcoin dan Lightning node, aplikasi perpesanan, atau pengelola kata sandi, sambil mempertahankan kontrol penuh atas data mereka dan menghilangkan ketergantungan pada platform teknologi terpusat. StartOS memiliki antarmuka berbasis peramban yang ramah pengguna, sebuah Marketplace yang dikurasi untuk menginstal layanan, dan alat privasi bawaan seperti integrasi Tor dan enkripsi HTTPS di seluruh sistem. Start9 juga menyediakan perangkat keras yang sudah dimuat sebelumnya dengan OS, meskipun perangkat lunaknya bisa diinstal pada perangkat keras yang kompatibel atau mesin virtual (VM).


### Opsi apa saja yang tersedia?


Start9 menawarkan opsi penerapan yang sudah jadi dan opsi penerapan DIY. **Server One**] (https://store.start9.com/collections/servers/products/server-one) dan **Server Pure**] (https://store.start9.com/collections/servers/products/server-pure) adalah perangkat keras resmi yang menampilkan komponen-komponen berkinerja tinggi: Server One menggunakan prosesor **AMD Ryzen 7 5825U** dengan RAM yang dapat dikonfigurasi (16GB-64GB) dan penyimpanan (2TB-4TB NVMe SSD), sedangkan Server Pure dilengkapi dengan **Intel i7-10710U**, yang juga menawarkan opsi RAM dan penyimpanan yang dapat dikonfigurasi. Keduanya termasuk **dukungan teknis seumur hidup** ketika dibeli langsung dari Start9. Bagi pengguna yang lebih menyukai fleksibilitas, StartOS dapat diinstal secara gratis di berbagai perangkat keras yang ada, termasuk laptop, desktop, mini PC, dan komputer papan tunggal, atau di dalam VM.


![image](assets/en/01.webp)


### Apa saja perbedaannya dengan Umbrel?


StartOS dan Umbrel sama-sama menyederhanakan instalasi layanan yang dihosting sendiri, tetapi berbeda dalam hal arsitektur dan fitur. Umbrel beroperasi sebagai lapisan aplikasi pada sistem Debian/Ubuntu atau VM, sedangkan Start9 adalah sistem operasi khusus yang membutuhkan instalasi perangkat keras atau VM secara langsung. Umbrel menampilkan antarmuka yang dipoles dan terinspirasi dari macOS, sedangkan Start9 mengutamakan desain yang fungsional dan minimal. Umbrel menawarkan [pilihan aplikasi] yang lebih banyak (https://apps.umbrel.com/), sedangkan [Start9 Marketplace] (https://marketplace.start9.com/) mengimbanginya dengan kemampuan teknis yang canggih. Start9 menyederhanakan akses ke pengaturan lanjutan melalui formulir UI yang tervalidasi, sehingga mengurangi kebutuhan akan interaksi baris perintah. Start9 juga unggul dalam manajemen pencadangan dengan pencadangan sistem terenkripsi sekali klik, sebuah fitur yang tidak dimiliki oleh Umbrel. StartOS menyediakan alat pemantauan internal dan menerapkan enkripsi HTTPS untuk akses jaringan lokal, meningkatkan keamanan. Umbrel menggunakan HTTP yang tidak terenkripsi secara lokal, meskipun kedua platform ini mendukung akses jarak jauh yang aman melalui Tor. Umbrel cocok untuk pengguna yang memprioritaskan ekosistem aplikasi yang kaya dan UI yang halus. Start9 merupakan pilihan yang kuat bagi mereka yang menghargai keamanan, konfigurasi, keandalan pencadangan, dan manajemen layanan tingkat lanjut tanpa memerlukan keahlian baris perintah. Untuk mempelajari lebih lanjut tentang Umbrel dan perbedaannya dengan Start9, silakan kunjungi kursus ini:


https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

## 2️⃣ Prasyarat DIY: Spesifikasi Minimum & Direkomendasikan


Untuk penggunaan dasar dengan layanan minimal, **spesifikasi minimum** adalah: **1 inti vCPU (2.0GHz+ boost), RAM 4GB, penyimpanan 64GB**, dan port Ethernet. Meskipun demikian, saya akan merekomendasikan lebih dari itu, terutama jika Anda menjalankan Bitcoin Node. Secara pribadi, saya memulai dengan 1TB dan dengan cepat kehabisan ruang. Lebih baik Anda memilih penyimpanan minimal 2TB, bersama dengan CPU quad-core (2,5GHz+)** dan RAM 8GB+. Hal ini membuat perbedaan besar dalam performa dan daya tahan. Jika Anda ingin mendalami lebih jauh, berikut ini adalah utas komunitas terbaru tentang [Perangkat Keras yang Mampu Menjalankan StartOS](https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/229).


## 3️⃣ Mengunduh dan Mem-flash Firmware


Untuk memulai penyiapan, gunakan komputer terpisah untuk mengunjungi [situs web Start9](https://start9.com/), dan arahkan ke bagian dokumentasi dengan mengeklik `DOCS`. Dari sana, akses `Panduan Penginstalan` untuk menemukan versi StartOS yang sesuai. Tersedia dua pilihan:



- StartOS (Raspberry Pi)
- StartOS (X86/ARM)


Tutorial ini mencakup opsi `x86/ARM`.


Versi OS terbaru dapat diunduh dari [halaman rilis Github](https://github.com/Start9Labs/start-os/releases/latest). versi [Pra-rilis] (https://github.com/Start9Labs/start-os/releases) juga tersedia bagi pengguna yang ingin menguji fitur-fitur baru. Pada bagian bawah halaman, di bawah `Assets`, unduh `x86_64` atau `x86_64-nonfree.iso`.  Image `x86_64-nonfree.iso` berisi perangkat lunak non-bebas (sumber tertutup) yang diperlukan untuk Server One dan sebagian besar perangkat keras DIY, terutama untuk dukungan grafis dan perangkat jaringan.


Disarankan untuk memverifikasi integritas file dengan memeriksa hash SHA256-nya dengan hash yang terdaftar di GitHub. Untuk Linux, perintah `sha256sum startos-0.3.4.2-efc56c0-20230525_x86_64.iso` dapat digunakan, dengan sistem operasi lain yang tercakup dalam dokumentasi.


Setelah mengunduh dan memverifikasi gambar StartOS, gambar tersebut harus di-flash ke drive USB. `BalenaEtcher` adalah perangkat lunak yang direkomendasikan untuk tugas ini. Ini adalah alat sumber terbuka gratis untuk menulis file gambar OS ke drive USB dan kartu SD, tersedia untuk Windows, macOS, dan Linux. Unduh versi yang sesuai dari [situs web resmi Balena Etcher] (https://www.balena.io/etcher/) dan jalankan penginstal. Hubungkan drive USB target atau kartu SD, buka Balena Etcher, dan klik `Flash from file` untuk memilih gambar OS yang diunduh. Etcher akan secara otomatis mendeteksi drive yang terhubung; pilih target yang benar jika ada beberapa. Klik `Flash!` untuk mulai menulis gambar. Etcher secara otomatis memvalidasi proses penulisan setelah selesai. Setelah selesai, lepaskan drive dengan aman dan gunakan untuk mem-boot perangkat.


![image](assets/en/19.webp)


## 4️⃣ Pengaturan Awal


Untuk penyiapan awal, lihat halaman [dokumentasi] Start9 (https://docs.start9.com/0.3.5.x/) di bawah `PETUNJUK PENGGUNA` diikuti dengan `Memulai - Penyiapan Awal`.  Panduan resmi ini harus dibaca untuk mendapatkan informasi terbaru.


Ada dua opsi yang disajikan:



- Mulai dengan Segar
- Opsi Pemulihan


Untuk instalasi server baru, pilih `Mulai Baru`. Pertama, sambungkan server ke daya dan kabel Ethernet. Pastikan komputer yang digunakan untuk penyiapan berada pada jaringan lokal yang sama. Lepaskan drive USB yang baru di-flash dari komputer dan masukkan ke dalam server.


Anda dapat mengontrol server dari jarak jauh dari komputer mana pun di jaringan yang sama. Buka browser web dan buka `http://start.local`.


**Catatan**: Jika terjadi masalah koneksi dengan alamat ini, biasanya disebabkan oleh jaringan rumah yang gagal menyelesaikan nama domain `.local`. Masalah ini dapat diatasi dengan mengakses server secara langsung melalui alamat IP-nya. IP dapat ditemukan dengan masuk ke antarmuka admin router (biasanya di `192.168.1.1` atau alamat yang serupa), dan menemukan perangkat di klien DHCP atau daftar peta jaringan. Kemudian, masukkan alamat IP lengkap (misalnya `http://192.168.1.105`) di browser. Cara ini akan mem-bypass resolusi DNS. Jika masalah masih berlanjut, lihat [Halaman Masalah Umum](https://docs.start9.com/0.3.5.x/support/common-issues.html#setup-troubleshoot) atau [hubungi bagian dukungan](https://start9.com/contact/)


Layar pengaturan StartOS akan muncul. Klik `Start Fresh` untuk memulai penyiapan server baru.


![image](assets/en/03.webp)


Langkah berikutnya adalah memilih drive penyimpanan tempat data StartOS akan disimpan.


![image](assets/en/04.webp)


Tetapkan `Kata Sandi` yang kuat untuk server. Catat seperti yang disarankan oleh Start9, lalu klik `FINISH`.


![image](assets/en/05.webp)


Sebuah layar akan menunjukkan bahwa StartOS sedang melakukan inisialisasi dan menyiapkan server. Langkah berikutnya adalah `Unduh info alamat` karena alamat `start.local` hanya untuk tujuan penyiapan dan tidak akan berfungsi setelahnya.


![image](assets/en/06.webp)


File konfigurasi berisi dua alamat akses penting: satu untuk `jaringan lokal (LAN) dan satu lagi untuk akses aman melalui `Tor`. Kedua alamat tersebut harus disimpan dalam pengelola kata sandi yang aman. Langkah selanjutnya adalah `Trust Root CA Anda`. Buka tab peramban baru dan ikuti petunjuk untuk mempercayai Root CA dan masuk. Sertifikat Root CA juga dapat diunduh dengan mengeklik `Unduh sertifikat` pada berkas yang diunduh.


## 5️⃣ Percayai CA Root Anda


Setelah mengunduh sertifikat, `Root CA` server harus dipercaya oleh sistem operasi. Klik `Lihat Petunjuk` dan temukan panduan untuk OS tertentu.


![image](assets/en/07.webp)


Untuk sistem Linux, perintah berikut ini digunakan. Pertama, buka Terminal dan instal paket yang diperlukan:


```shell
sudo apt update

sudo apt install -y ca-certificates p11-kit
```


Arahkan ke direktori tempat sertifikat diunduh, biasanya `~/Downloads`. Jalankan perintah ini untuk menambahkan sertifikat ke penyimpanan kepercayaan OS. Ubah ke folder unduhan dengan `cd ~/Downloads`. Buat direktori yang diperlukan dengan `sudo mkdir -p /usr/share/ca-certificates/start9`. Salin berkas sertifikat, ganti `your-filename.crt` dengan nama berkas yang sebenarnya, dengan menggunakan `sudo cp "your-filename.crt" /usr/share/ca-certificates/start9/`. Daftarkan sertifikat secara permanen dengan menambahkan jalurnya ke konfigurasi sistem dengan `sudo bash -c "echo 'start9/your-filename.crt' >> /etc/ca-certificates.conf"`. Terakhir, bangun kembali penyimpanan kepercayaan dengan `sudo update-ca-certificates`. Sangat penting untuk menggunakan nama berkas sertifikat yang sebenarnya dan memverifikasi semua jalur sebelum menjalankan perintah-perintah ini. Proses ini akan membangun kepercayaan permanen untuk koneksi HTTPS server Start9.


Instalasi yang berhasil akan ditunjukkan dengan output yang menyatakan `1 ditambahkan`. Sebagian besar aplikasi akan dapat terhubung dengan aman melalui `https`. Jika menggunakan Firefox, diperlukan [langkah terakhir] tambahan (https://docs.start9.com/0.3.5.x/misc-guides/ca-ff.html#ca-ff). Untuk Chrome atau Brave, diperlukan [langkah terakhir] yang berbeda (https://docs.start9.com/0.3.5.x/misc-guides/ca-chrome.html#ca-chrome) untuk mengonfigurasi peramban agar menghormati Root CA. Uji koneksi dengan menyegarkan halaman. Jika masalah berlanjut, keluar dan buka kembali peramban sebelum mengunjungi kembali halaman tersebut.


![image](assets/en/08.webp)


## 6️⃣ Memulai dengan StartOS


Seharusnya sekarang Anda dapat masuk menggunakan koneksi HTTPS yang aman. Masukkan `Kata Sandi` untuk mengakses `Layar Selamat Datang`.


![image](assets/en/09.webp)


Layar ini menyediakan pintasan yang berguna untuk memulai. Bilah sisi kiri berisi item menu utama untuk navigasi.


## 7️⃣ Sistem


Tab Sistem di StartOS menyediakan akses ke fungsi-fungsi sistem inti untuk mengelola server pribadi. Tab ini menawarkan alat untuk pemeliharaan sistem, keamanan, diagnostik, dan konfigurasi tanpa memerlukan keahlian baris perintah.


Bagian `Backups` memungkinkan pembuatan cadangan sistem lengkap, termasuk layanan, konfigurasi, dan data, yang dapat dipulihkan nanti. Hal ini sangat penting untuk pemulihan bencana atau migrasi ke perangkat keras baru. Cadangan dapat disimpan di drive eksternal dan dienkripsi menggunakan kata sandi utama.


Bagian `Manage` di tab Systems memungkinkan kontrol atas fungsi sistem utama. Pengguna dapat secara manual memeriksa dan menerapkan pembaruan StartOS, mempertahankan kontrol atas proses pembaruan sistem. Dimungkinkan untuk memuat layanan khusus atau pihak ketiga yang tidak tersedia di pasar resmi. Jika server tidak terhubung melalui Ethernet, pengaturan Wi-Fi dapat dikonfigurasi dari bagian ini. Pengguna tingkat lanjut dapat mengaktifkan akses SSH untuk manajemen sistem tingkat terminal.


![image](assets/en/10.webp)


Bagian `Insights` menyediakan pemantauan kinerja dan kesehatan server secara real-time, menampilkan penggunaan CPU, RAM, dan disk melalui grafik. Ini juga menunjukkan suhu sistem, yang berguna untuk perangkat seperti Raspberry Pi yang tidak memiliki pendingin aktif. Metrik waktu aktif dan rata-rata beban membantu menilai stabilitas sistem, dan log langsung tersedia untuk pemecahan masalah layanan atau masalah sistem.


Bagian `Dukungan` menawarkan akses ke FAQ bawaan, dokumentasi resmi, dan saluran dukungan komunitas. Log debug dapat diunduh dari bagian ini untuk dibagikan dengan dukungan Start9 untuk penyelesaian masalah yang lebih cepat.


![image](assets/en/11.webp)


## 8️⃣ Pasar


`Pasar` digunakan untuk menemukan, menginstal, dan mengelola layanan pada server pribadi. Ini menyediakan akses ke perangkat lunak seperti Bitcoin Core, BTCPay Server, dan electrs. StartOS mendukung beberapa pasar, termasuk Start9 Registry resmi dan registri yang dikelola komunitas. Ini dapat ditambahkan dengan mengklik `UBAH` dan beralih ke `Registri Komunitas`, yang menyediakan akses ke berbagai layanan yang lebih luas.


![image](assets/en/12.webp)


## 9️⃣ Memasang Node Penuh Bitcoin


Menginstal Bitcoin full node di StartOS memberikan kedaulatan penuh atas pengalaman Bitcoin. Hal ini memungkinkan validasi transaksi dan meningkatkan privasi dan keamanan dengan menghilangkan ketergantungan pada layanan eksternal yang dapat mencatat aktivitas. Kontrol penuh atas transaksi diperoleh, memungkinkan mereka untuk disiarkan langsung ke jaringan. Opsi defaultnya adalah `Bitcoin Core`, yang terintegrasi secara native dengan StartOS dan memungkinkan koneksi dengan wallet seperti Specter, Sparrow, atau Electrum untuk pengaturan penyimpanan mandiri. Sebuah alternatif, `Bitcoin Knots`, juga tersedia melalui Community Registry.


Untuk menginstal Bitcoin Core, buka Marketplace. Di bawah registri default, cari dan instal layanan Bitcoin Core. Setelah instalasi, prompt `Needs Config` akan muncul, yang memerlukan pengaturan untuk diselesaikan sebelum layanan dapat berjalan. Hal ini biasanya terjadi setelah pembaruan atau instalasi baru dan meminta peninjauan `Pengaturan RPC`. Lanjutkan dengan konfigurasi default dan klik `Save`.


![image](assets/en/13.webp)


Setelah tersinkronisasi sepenuhnya, node Anda dapat berfungsi sebagai backend pribadi untuk dompet seperti Sparrow, memberikan privasi yang lebih baik dan validasi transaksi. Akan tetapi, untuk pengguna yang menyimpan jumlah yang signifikan, sangat penting untuk memahami pertukaran keamanan dari koneksi langsung ini. Ketika sebuah wallet terhubung secara langsung ke Bitcoin Core, ia dapat mengekspos data sensitif, karena Bitcoin Core menyimpan kunci publik (xpubs) dan saldo wallet yang tidak terenkripsi pada mesin host. Sistem yang disusupi dapat memungkinkan penyerang untuk menemukan kepemilikan Anda dan menargetkan Anda.


Untuk mengurangi risiko ini dan mencapai model keamanan yang lebih kuat, Anda dapat menyiapkan Private Electrum Server. Server ini bertindak sebagai perantara, mengindeks blockchain tanpa menyimpan informasi spesifik wallet. Dengan menghubungkan wallet Anda ke server Electrum Anda sendiri dan bukan langsung ke Bitcoin Core, Anda mencegah wallet mengakses data sensitif node.


![image](assets/en/14.webp)


## 🔟 Mengatur elektrik


`electrs` (Electrum Rust Server) adalah pengindeks yang cepat dan efisien yang terhubung ke node Bitcoin Core Anda dan memungkinkan dompet yang kompatibel dengan Electrum untuk menanyakan riwayat transaksi dan saldo secara real time. Dengan menjalankan electrs di StartOS, Anda menghilangkan ketergantungan pada server Electrum pihak ketiga, yang secara signifikan meningkatkan privasi dan keamanan - kueri wallet Anda langsung masuk ke node yang dihosting sendiri.


Untuk menyiapkannya, pertama-tama instal layanan electrs dari Pasar StartOS. Sistem akan membutuhkan Bitcoin Core untuk disinkronkan sepenuhnya sebelum melanjutkan. Setelah instalasi, konfirmasikan pengaturan `Needs Config` dengan pengaturan default yang disarankan dan electrs mulai mengindeks blockchain, yang dapat memakan waktu hingga satu hari tergantung pada perangkat keras Anda.


![image](assets/en/15.webp)


Setelah selesai, Anda dapat menghubungkan dompet seperti Sparrow atau Specter. Koneksi yang berhasil memungkinkan wallet Anda untuk menyinkronkan langsung dengan node Anda, memberikan pengalaman Bitcoin yang aman, privat, dan dihosting sendiri.


## 1️⃣1️⃣ Hubungkan Sparrow Wallet


Untuk menyambungkan `Sparrow Wallet` ke node StartOS Anda menggunakan implementasi electrs, pertama-tama pastikan Bitcoin Core telah tersinkronisasi sepenuhnya dan electrs telah terinstal dan berjalan. Buka Sparrow Wallet pada perangkat Anda dan arahkan ke `File` -> `Settings` -> `Server`. Kemudian pilih `Private Electrum Server`. Pada kolom URL, masukkan `Tor hostname` dan `Port` untuk electrs, yang dapat Anda temukan di StartOS di bawah `Services` -> `electrs` -> `Properties` (biasanya diakhiri dengan `.onion:50001`).


![image](assets/en/16.webp)


Selanjutnya, aktifkan Tor dengan mencentang `Use Proxy`, atur alamat proxy ke `127.0.0.1` dan port ke `9050`. Klik `Test Connection` dan tunggu beberapa saat. Sambungan yang berhasil akan menampilkan pesan konfirmasi seperti `Tersambung ke electrs`. Setelah diverifikasi, tutup pengaturan dan lanjutkan untuk membuat atau memulihkan wallet Anda. Pengaturan ini memastikan wallet Anda menanyakan node Anda sendiri melalui electrs, memberikan privasi penuh dan operasi tanpa kepercayaan.


![image](assets/en/17.webp)


## 🎯 Kesimpulan


StartOS oleh Start9 adalah platform yang ramah pengguna dan berfokus pada privasi yang dirancang untuk meng-hosting sendiri layanan-layanan penting seperti node Bitcoin dan Lightning, dompet, dan aplikasi-aplikasi pribadi. Platform ini menghilangkan kebutuhan akan keahlian baris perintah dengan menawarkan antarmuka grafis yang bersih, pencadangan otomatis, pemantauan kesehatan, dan akses Tor yang aman, membuatnya ideal untuk pengguna non-teknis. Arsitektur modularnya mendukung integrasi tanpa batas dengan alat-alat seperti electrs atau Sparrow, memberikan Anda kendali penuh atas kedaulatan keuangan dan digital Anda. Dengan fokus yang kuat pada transparansi, kontrol lokal, dan perluasan, StartOS memberdayakan pengguna untuk mendapatkan kembali kepemilikan dari platform terpusat dan menjalankan infrastruktur pribadi mereka sendiri yang tangguh.