---
name: Bitchat
description: Pesan terdesentralisasi dan bebas Internet untuk komunikasi gratis
---

![cover](assets/cover.webp)


![video](https://youtu.be/WfzcKAzgB9s)


*Video tutorial dari BTC Sessions ini akan memandu Anda melalui proses pengaturan dan penggunaan Bitchat!


Bitchat muncul dari upaya pembuatan prototipe yang cepat di mana [@jack](https://primal.net/jack) mengembangkan konsep awal selama sesi coding di akhir pekan. [@calle](https://primal.net/calle) bergabung dengan proyek ini tidak lama kemudian untuk ikut mengembangkan implementasi Android. Jack saat ini memimpin pengembangan versi iOS, sementara calle mengawasi versi Android dengan dukungan dari banyak kontributor lainnya.


## Pendahuluan: Mengobrol dengan Bebas, Tanpa Kisi-kisi


Bayangkan mengirim pesan saat internet mati, saat terjadi bencana alam, atau di tempat-tempat yang komunikasinya terbatas. Bitchat memungkinkan hal ini terjadi. Bitchat adalah aplikasi pesan peer-to-peer terdesentralisasi yang melewatkan server pusat, sehingga memungkinkan perangkat untuk berbicara langsung satu sama lain, sepenuhnya secara offline menggunakan Bluetooth dan jaringan mesh. Dirancang dengan mempertimbangkan privasi dan ketahanan, Bitchat sangat ideal untuk digunakan di area-area di mana konektivitas tradisional tidak dapat diandalkan atau tidak tersedia-seperti saat terjadi bencana, di lokasi terpencil, atau bagi mereka yang ingin menghindari pengawasan. Pada intinya, Bitchat menggunakan kriptografi untuk memastikan setiap pesan dienkripsi secara end-to-end, diverifikasi, dan anti perusakan.


Dalam tutorial ini, kami akan menunjukkan cara kerja Bitchat dan bagaimana Anda dapat menggunakannya untuk komunikasi yang benar-benar pribadi dan siap untuk offline.


## 🚀 Fitur Utama


Bitchat memungkinkan pengiriman pesan secara offline melalui [fitur-fitur] ini (https://github.com/permissionlesstech/bitchat-android?tab=readme-ov-file#features):



- Kompatibel Lintas Platform**: Kompatibilitas protokol penuh antara iOS dan Android.
- Jaringan Jaring Terdesentralisasi**: Penemuan rekan otomatis dan relai pesan multi-hop melalui Bluetooth Low Energy (BLE)
- Enkripsi ujung ke ujung**: Pertukaran kunci X25519 + AES-256-GCM untuk pesan pribadi
- Obrolan Berbasis Saluran**: Perpesanan grup berbasis topik dengan perlindungan kata sandi opsional
- Simpan & Teruskan**: Pesan yang disimpan untuk rekan-rekan yang offline dan dikirim ketika mereka terhubung kembali
- Mengutamakan Privasi**: Tanpa akun, tanpa nomor telepon, tanpa pengenal yang persisten
- Perintah-perintah Gaya IRC: Antarmuka gaya `/join, /msg, /who` yang sudah dikenal.
- Penyimpanan Pesan**: Penyimpanan pesan di seluruh saluran opsional yang dikendalikan oleh pemilik saluran
- Penghapusan Darurat**: Logo ketuk tiga kali untuk menghapus semua data secara instan
- UI Android modern**: Jetpack Compose dengan Desain Material 3
- Tema Gelap/Terang**: Versi iOS yang terinspirasi dari estetika yang serasi dengan terminal
- Optimalisasi Baterai**: Pemindaian adaptif dan manajemen daya


## 1️⃣ Bagaimana Bitchat Bekerja - sederhana


Bitchat memungkinkan Anda mengirim pesan ke ponsel terdekat secara langsung melalui Bluetooth (`BLE` sebagai berikut), tanpa perlu internet atau sinyal seluler. Ketika Anda memulai obrolan, ponsel melakukan jabat tangan yang aman untuk membuat kunci enkripsi sementara yang unik untuk percakapan Anda. Setiap pesan dilindungi dengan enkripsi ujung ke ujung, dan kunci baru digunakan untuk setiap pesan untuk memastikan pesan yang lalu tetap aman meskipun ponsel Anda dibobol nanti. Terakhir, aplikasi ini membagi pesan menjadi bagian-bagian kecil dan mencampurkannya dengan data tiruan acak untuk menyembunyikan aktivitas perpesanan Anda. Untuk obrolan langsung dari perangkat ke perangkat, aplikasi ini hanya bekerja dalam jangkauan hingga ~100m. Ini seperti memberikan catatan terenkripsi di ruangan yang penuh sesak-perangkat berbisik langsung satu sama lain, mengacak-acak kunci setelah setiap pesan.


Bitchat juga memungkinkan Anda untuk bergabung dengan ruang obrolan berbasis lokasi menggunakan protokol Nostr dan `#geohash`. Geohash adalah kode pendek, seperti `#u33d`, yang mewakili area geografis tertentu, dari satu lingkungan, hingga seluruh kota atau wilayah. Anda dapat `teleportasi` ke ruang obrolan geohash mana pun di seluruh dunia hanya dengan memasukkan tag-nya. Pesan Anda dikirim melalui jaringan relai yang terdesentralisasi, yang melindungi lokasi Anda. Selain itu, setiap kali Anda bergabung dengan ruang geohash, Anda diberi identitas baru yang bersifat sementara, menambahkan lapisan privasi ekstra pada percakapan berbasis lokasi Anda.


Untuk detail teknis yang lebih akurat, silakan merujuk ke [Whitepaper resmi](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md).


## 2️⃣ Instalasi & Pengaturan


### Di mana Mendapatkan Bitchat


Anda dapat menginstal Bitchat melalui:



- [Apple App Store](https://apps.apple.com/us/app/bitchat-mesh/id6748219622) (untuk perangkat iOS)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bitchat.droid) (untuk perangkat Android)


Pengguna Android juga memiliki opsi alternatif:



- Unduh APK langsung dari halaman [Rilis GitHub](https://github.com/permissionlesstech/bitchat-android/releases) atau
- Instal melalui [Zapstore] yang kompatibel dengan Nostr (https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqgkxmmd9e3xjarrdpshgtnywfhkjeqxtfkcr)


![image](assets/en/01.webp)


**Catatan**: tutorial ini terutama berfokus pada implementasi Android. Versi iOS mungkin berbeda._


### Proses Pengaturan


Setelah instalasi, buka Bitchat untuk melihat layar perizinan awal. Inilah yang perlu Anda lakukan:


1. **Berikan izin yang diperlukan berikut ini:**


   - Akses Bluetooth** (untuk menemukan pengguna Bitchat terdekat)
   - Lokasi yang tepat** (Android memerlukan ini untuk fungsionalitas Bluetooth)
   - Pemberitahuan** (untuk menerima peringatan pesan pribadi)

2. **Nonaktifkan pengoptimalan baterai**:


   - Hal ini memungkinkan Bitchat berjalan di latar belakang
   - Mempertahankan koneksi jaringan jala secara terus menerus


Ketuk `Berikan Izin`, ikuti `petunjuk` dan `Nonaktifkan Pengoptimalan Baterai` untuk beralih ke layar berikutnya.


![image](assets/en/02.webp)


Selamat datang di layar utama Bitchat. Mari kita berorientasi:


### Pengaturan


Hal pertama yang pertama. Menu pengaturan dapat dibuka dengan mengetuk `Logo Bitchat`.  Pilihan berikut ini tersedia:



- Mengatur `penampilan` (sistem/cerah/gelap).
- aktifkan `Bukti kerja` ke geohash untuk pencegahan spam (opsional)
- Aktifkan `Tor` untuk meningkatkan privasi.


![image](assets/en/16.webp)


### Tetapkan Identitas Anda


Ketuk bidang `bitchat/anonXXXX` di bagian atas untuk memilih nama pengguna Anda. Dengan cara inilah orang lain akan melihat Anda dalam mode Bluetooth dan internet. Sebagai contoh, Anda dapat mengubah "anon2022" menjadi nama pengguna pilihan Anda.


![image](assets/en/03.webp)


### Memilih Saluran Jaringan


Gunakan menu `#saluran lokasi` (sebelah kanan nama pengguna) untuk beralih di antara jenis koneksi:



- BLE Mesh***: Mode Bluetooth default (tanpa internet, dari jangkauan 10 hingga 50 meter)
- #geohashes**: Komunitas geografis yang diaktifkan di Internet menggunakan [protokol Nostr](https://nostr.com/)


Ketika Anda memilih mode `#geohashes`, Bitchat berintegrasi dengan protokol Nostr untuk mengaktifkan komunitas geografis. Pesan-pesan Anda dipublikasikan ke `relay Nostr terdesentralisasi` dan bukan ke jaringan peer-to-peer Bitchat, sehingga memungkinkan percakapan yang lebih luas tetapi disaring berdasarkan lokasi. Yang paling penting, kunci identitas Bitchat Anda secara kriptografis menandatangani semua peristiwa Nostr untuk menjaga otentikasi, sementara tag geohash (seperti `#u4pruyd` untuk sebuah lingkungan) memfilter pesan ke tingkat presisi yang Anda pilih. Ini berarti Anda dapat berpartisipasi dalam diskusi lokal tanpa mengungkapkan koordinat yang tepat, meskipun akses internet diperlukan.


![image](assets/en/04.webp)


### Memantau Rekan Kerja

lisensi: CC-BY-SA-V4

Penghitung rekan menunjukkan pengguna:



- Terdekat (BLE Mesh) atau
- Di zona geohash Anda (#geohash)


![image](assets/en/05.webp)


## 3️⃣ Obrolan Global & Pesan Pribadi


Bitchat menyediakan dua mode komunikasi yang berbeda untuk memenuhi kebutuhan yang berbeda:



- Saluran Publik:** Untuk percakapan terbuka dengan orang lain. Anda dapat terhubung melalui jaringan mesh BLE lokal untuk pengguna di sekitar Anda atau melalui #geohash global untuk komunitas berbasis lokasi yang mendukung internet.
- Pesan Pribadi:** Untuk percakapan empat mata yang aman. Ini membuat koneksi langsung dan terenkripsi untuk menjaga kerahasiaan percakapan Anda.


Memahami kedua mode tersebut akan membantu Anda menavigasi percakapan Anda.


### Saluran Publik: Pusat Komunitas


Menu `#saluran lokasi` (kanan atas) mengontrol visibilitas publik Anda. Memilih `jaring` menghubungkan Anda ke semua pengguna terdekat melalui jaring BLE, biasanya perangkat dalam jarak 10-50 meter. Hal ini menciptakan forum terbuka di mana pesan disiarkan ke semua orang dalam jangkauan, ideal untuk pengumuman acara atau peringatan lokal.


Untuk jangkauan geografis yang lebih luas, pilih tag `#geohash` untuk bergabung dengan komunitas yang didukung internet yang disaring berdasarkan lokasi. Saluran ini menggunakan relay protokol Nostr, yang memungkinkan komunikasi lintas kota atau wilayah dengan tetap mempertahankan relevansi berbasis lokasi. Pesan Anda akan muncul secara langsung kepada orang lain di saluran yang sama, dengan peserta baru secara otomatis melihat riwayat pesan terbaru saat bergabung.


![image](assets/en/06.webp)


### Percakapan pribadi: Aman & Terenkripsi


Untuk memulai percakapan pribadi, ketuk satu kali secara langsung pada `nama pengguna` yang ditampilkan di `Ringkasan Rekan Kerja.` Anda juga dapat mengetuk `ikon bintang` untuk menandai pengguna ini sebagai favorit, yang akan membuatnya tetap terlihat di daftar kontak Anda meskipun sedang offline.


![image](assets/en/07.webp)


Bitchat secara otomatis memulai `jabat tangan keamanan` ketika Anda memulai obrolan pribadi. Perangkat bertukar kunci sementara untuk membuat terowongan terenkripsi khusus untuk percakapan Anda. Proses ini memastikan bahwa semua pesan dan file yang Anda bagikan tetap rahasia berkat enkripsi ujung ke ujung yang berkelanjutan. Pesan pribadi mendukung berbagi teks dan file.


![image](assets/en/08.webp)


## 4️⃣ Fitur tambahan


Anda dapat mengakses panel tindakan secara instan dengan mengetik `/` di mana saja di Bitchat. Ini akan menampilkan menu perintah untuk tindakan cepat.



- Mengelola koneksi**: `Blokir pengguna` atau `Buka blokir rekan`
- Kontrol saluran**: `Tampilkan saluran` atau `Gabung/buat saluran`
- Interaksi sosial**: `Kirim pelukan hangat` atau `tampar ikan trout` 🎣
- Pemeliharaan obrolan**: `Menghapus pesan obrolan`
- Alat privasi**: `Lihat siapa yang online` atau `Kirim pesan pribadi`


Perintah-perintah langsung dijalankan - seperti `/blokir Satoshi` untuk membungkam para pengkritik atau `/peluk Hal` untuk menyebarkan hal positif 🫂.


![image](assets/en/09.webp)


## 5️⃣ Membuat saluran


Saluran di Bitchat memungkinkan komunikasi yang terorganisir di sekitar topik, lokasi, atau komunitas. Untuk membuat saluran Anda sendiri, ikuti alur kerja ini:


### Langkah 1: Membuat saluran


Untuk membuat saluran, ketik `/j` atau `/join` diikuti dengan `nama saluran` di obrolan mana pun (contoh: `/j <nama saluran>`). Setelah pembuatan, sebuah `ikon ⧉` baru akan muncul yang menunjukkan saluran baru. Pengguna lain dapat bergabung dengan mengetikkan perintah yang sama (contoh: `/j bitchat_tutorial`).


![image](assets/en/10.webp)


### Langkah 2: Mengkonfigurasi pengaturan


Selain perintah default, pengaturan berikut ini tersedia di dalam saluran:



- `/save` untuk menyimpan pesan secara lokal
- `/transfer` untuk mentransfer kepemilikan saluran dan
- `/pass` untuk mengubah kata sandi saluran.


Untuk komunitas pribadi, perintah ini memungkinkan perlindungan kata sandi, yang mengharuskan anggota yang telah disetujui untuk memasukkan kata sandi khusus sebelum bergabung.


## 6️⃣ Mode Panik


Sekarang, mari kita bahas tentang `mode panik`: mengetuk tiga kali pada `logo Bitchat` akan memulai penghapusan semua pesan dan data lokal dalam aplikasi. Ini adalah perlindungan privasi utama Anda, sempurna untuk situasi yang membutuhkan kebijaksanaan segera.


**Pengingat penting:** _Mode panik bersifat permanen. Setelah diaktifkan, data tidak dapat dipulihkan. Gunakan dengan hati-hati._


![image](assets/en/11.webp)


## 7️⃣ Geohash


Saluran Geohash memungkinkan percakapan yang ditargetkan berdasarkan `lokasi geografis` daripada koneksi jaringan tradisional. Fitur ini mengubah bitchat menjadi alat komunikasi yang sadar lokasi, ideal untuk koordinasi lokal, pembangunan komunitas, dan diskusi spesifik lokasi.


### Bagaimana `#geohash` bekerja


Sistem ini membagi dunia ke dalam kotak-kotak grid menggunakan [sistem Geohash](https://en.wikipedia.org/wiki/Geohash), di mana setiap karakter dalam hash merepresentasikan presisi yang lebih tinggi:



- Level 4** (misalnya, `u33d`): Mencakup sekitar 25 km × 25 km - ideal untuk diskusi di seluruh kota
- Level 6** (misalnya, `u33d8z`): Mencakup sekitar 1,2 km × 1,2 km - ketepatan lingkungan
- Level 8** (misalnya, `u33d8z1k`): Mencakup sekitar 150 m x 150 m - akurasi segmen jalan


Pemilihan presisi menyeimbangkan privasi dengan utilitas: tingkat yang lebih tinggi menciptakan zona yang lebih eksklusif tetapi mengungkapkan lokasi Anda dengan lebih tepat.


### Bergabung dengan saluran `#geohash`


1. Akses menu `#saluran lokasi`.

2. Pilih tingkat presisi yang Anda inginkan dan masukkan `#geohash` (contoh: #u33d)

3. Ketuk tombol `Teleportasi` untuk bergabung dengan `#saluran lokasi`.


![image](assets/en/12.webp)


Atau, Anda dapat mengetuk `ikon peta` untuk menggunakan tampilan peta guna menentukan tingkat presisi dan mengetuk `pilih` untuk bergabung dengan `#saluran lokasi`.


![image](assets/en/13.webp)


**Pengingat penting**: fungsionalitas _#geohash memerlukan koneksi internet aktif - tidak seperti BLE mesh yang beroperasi secara offline melalui Bluetooth._


## 8️⃣ Peta Panas


Peta panas adalah cara yang keren untuk menemukan acara dan saluran Bitchat di seluruh dunia. [Bitmap](https://bitmap.lat/) memvisualisasikan dan melacak pesan-pesan anonim berbasis lokasi di seluruh jaringan Nostr, menampilkan acara-acara Nostr yang bersifat sementara. Lihat dan bergabunglah dengan saluran dan obrolan khusus lokasi.


![image](assets/en/15.webp)


## 🎯 Kesimpulan


Bitchat memungkinkan komunikasi yang aman dan terdesentralisasi untuk skenario di mana pengiriman pesan tradisional gagal. Aplikasi ini dapat beroperasi tanpa infrastruktur internet menggunakan jaringan mesh BLE, sehingga cocok untuk protes, zona bencana, dan daerah terpencil di mana konektivitas terbatas atau disensor. Aplikasi ini memastikan privasi melalui enkripsi kunci sementara, saluran lokasi berbasis geohash, dan penghapusan data mode panik.


Aplikasi ini masih dalam tahap awal pengembangan, tetapi sudah menunjukkan hasil yang menjanjikan. Pengguna harus mengharapkan adanya bug sesekali dan melaporkan masalah melalui [GitHub](https://github.com/permissionlesstech/bitchat-android/issues). Perbaikan direncanakan, termasuk integrasi `ecash` untuk transaksi dalam aplikasi pribadi menggunakan protokol Cashu.


![image](assets/en/14.webp)


## 📚 Sumber Daya Bitchat


[Github](https://github.com/permissionlesstech) | [Situs web](https://bitchat.free/) | [Whitepaper](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)