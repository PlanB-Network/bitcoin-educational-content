---
name: Bitcoin Keeper - Rencana Warisan
description: Rencanakan pengiriman bitcoin Anda dengan Bitcoin Keeper
---

![cover](assets/cover.webp)



Pengalihan aset Bitcoin merupakan salah satu tantangan yang paling diremehkan oleh para pemegangnya. Tidak seperti rekening bank, di mana lembaga keuangan dapat memberikan dana kepada ahli waris yang sah, Bitcoin sepenuhnya bergantung pada kepemilikan kunci pribadi. Ahli waris yang sah secara hukum tidak akan pernah dapat mengakses dana tanpa kunci ini, sementara orang jahat yang memiliki rahasia tersebut dapat membelanjakannya tanpa formalitas.



Dalam tutorial Bitcoin Keeper kedua ini, kita akan menjelajahi fitur-fitur premium yang didedikasikan untuk perencanaan warisan. Aplikasi ini menawarkan alat canggih untuk membuat Brankas yang Disempurnakan, dengan mekanisme perlindungan berjangka waktu berkat Miniscript, serta dokumen yang menyertai untuk memandu orang yang Anda cintai.



Panduan ini mengasumsikan bahwa Anda telah menguasai dasar-dasar Bitcoin Keeper (pembuatan portofolio, multisig klasik, menambahkan kunci perangkat keras) seperti yang dijelaskan dalam tutorial pertama kami:



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

![video](https://youtu.be/tCld_-n2d30)



## Paket berlangganan Bitcoin Keeper



Bitcoin Keeper beroperasi dengan model freemium dengan tiga tingkat langganan yang menawarkan fungsionalitas progresif. Untuk mengakses paket, buka tab **Lainnya**, lalu ketuk paket Anda saat ini (standarnya adalah "Pleb") untuk membuka layar **Kelola Langganan**.



![Plans d'abonnement](assets/fr/01.webp)



Paket **Pleb** (gratis) menyediakan akses ke hal-hal penting: pembuatan dompet satu kunci dan multi-kunci yang tidak terbatas, kompatibilitas dengan semua dompet perangkat keras utama (Coldcard, Trezor, Ledger, Jade, Tapsigner...), kontrol koin, pelabelan, dan koneksi ke server Electrum pribadi. Paket ini cukup untuk penggunaan standar dan bahkan untuk konfigurasi multi-sig klasik.



Paket **Hodler** (€9.99/bulan, dengan gratis 1 bulan jika dibayar tahunan) mencakup semua fitur Pleb dan menambahkan cadangan terenkripsi ke awan (iCloud atau Google Drive) untuk memulihkan brankas Anda di perangkat apa pun, Kunci Server untuk menambahkan kebijakan pengeluaran otomatis dan 2FA di atas ambang batas tertentu, dan Dompet Kenari untuk mendeteksi akses tidak sah ke kunci Anda.



Paket **Diamond Hands** (€29.99/bulan, dengan gratis 1 bulan jika dibayar setiap tahun) adalah paket lengkap untuk perencanaan warisan. Paket ini mencakup seluruh paket Hodler dan membuka Kunci Warisan (aktivasi yang ditangguhkan), Kunci Darurat (kunci darurat untuk pemulihan jika terjadi kehilangan), alat dan dokumen Perencanaan Warisan, dan panggilan dukungan dengan tim Concierge untuk memvalidasi konfigurasi Anda. Ini adalah penawaran bagi para bitcoiners yang ingin mewariskan warisan mereka selama beberapa generasi.



Poin penting: brankas yang telah Anda buat akan tetap dapat diakses meskipun Anda kembali ke paket gratis. Konfigurasi Anda didasarkan pada standar terbuka (BSMS, Miniscript) dan beroperasi secara independen dari langganan Anda.



## Dokumen warisan



Setelah Anda mengaktifkan langganan Diamond Hands, akses bagian **Dokumen Warisan** dari tab Lainnya. Bitcoin Keeper menyediakan lima contoh dokumen untuk menyusun rencana warisan Anda, serta bagian tips:



![Documents d'héritage](assets/fr/02.webp)





- Templat Kata Benih**: templat untuk mencatat frasa pemulihan Anda dengan rapi secara terorganisir
- Kontak Tepercaya**: templat untuk mencantumkan rincian kontak orang-orang tepercaya yang terlibat dalam rencana Anda (notaris, pengacara, ahli waris, pemegang kunci)
- Kunci Berbagi Tambahan**: dokumen yang merinci informasi teknis untuk setiap kunci: Kode PIN, jalur turunan, lokasi fisik, jenis perangkat, dan informasi lain yang berguna untuk mengidentifikasi dan menggunakan kunci
- Petunjuk Pemulihan**: petunjuk langkah demi langkah bagi ahli waris atau penerima manfaat untuk memulihkan dana
- Surat untuk Pengacara**: surat yang telah diisi sebelumnya yang dapat disesuaikan untuk pengacara atau notaris Anda



Bagian **Tips Warisan** menawarkan saran praktis untuk mengamankan kunci bagi ahli waris dan mengoptimalkan rencana warisan Anda.



Sesuaikan dokumen-dokumen ini agar sesuai dengan situasi Anda, dan simpanlah di tempat yang aman, terpisah dari kunci itu sendiri.



## Mengonfigurasi Pencadangan Cloud



Sebelum membuat brankas lama, aktifkan pencadangan awan untuk melindungi file konfigurasi Anda. Dari tab Lainnya, tekan **Cadangan Cloud Pribadi**.



![Configuration Cloud Backup](assets/fr/03.webp)



Pilih kata sandi yang kuat untuk mengenkripsi cadangan Anda. Kata sandi ini hanya melindungi file konfigurasi wallet (bukan kunci pribadi Anda). Konfirmasikan kata sandi dan tekan **Konfirmasi**. Cadangan Anda akan disimpan di iCloud atau Google Drive, tergantung pada perangkat Anda. Tekan **Backup Now** untuk meluncurkan pencadangan pertama Anda.



## Mengimpor kunci perangkat keras Anda



Untuk contoh kita, kita akan membuat brankas 2-dari-3 dengan dua kunci tambahan (Warisan dan Darurat). Mari kita mulai dengan mengimpor semua kunci yang diperlukan ke dalam tab **Keys**.



![Import des clés hardware](assets/fr/04.webp)



Tekan **Tambah tombol**, lalu pilih **Tambah tombol dari perangkat keras** untuk menyambungkan perangkat keras wallet. Bitcoin Keeper mendukung banyak perangkat: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner, dan Specter Solutions.



Dalam konfigurasi kami, kami mengimpor file :




- 2 tombol **Coldcard** (MK4SP dan MK4)
- 2 tombol **Tapsigner** (Metro dan Genesis)



Untuk menambahkan Coldcard, pilih dari daftar dan ikuti petunjuk di layar untuk mengekspor kunci publik melalui kode QR, file, USB, atau NFC. Untuk detail lebih lanjut tentang cara menggunakan Coldcard atau Tapsigner, silakan lihat tutorial khusus kami:



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/tutorials/wallet/hardware/coldcard-mk4-5d44dd94-423d-4e37-9a8c-3fc38b45ce59


Setelah semua kunci Anda diimpor, Anda akan menemukannya di tab Kunci dengan nama khusus.



## Buat wallet yang sudah ada sebelumnya



Mari kita lanjutkan ke pembuatan trunk. Dari tab **Wallets**, tekan **Addend Wallet**, pilih **Bitcoin Wallet**, kemudian **Create Wallet**.



![Création du wallet](assets/fr/05.webp)



Pilih tipe wallet. Untuk paket lama kami, pilih **2 dari 3 kunci multi**. Di bagian bawah layar, aktifkan **Pilihan Keamanan yang Ditingkatkan** lalu tekan **Lanjutkan**.



![Options de sécurité avancées](assets/fr/06.webp)



Pada popup Opsi Keamanan yang Ditingkatkan, centang :




- Kunci Warisan**: kunci tambahan yang akan ditambahkan ke kuorum setelah jangka waktu tertentu
- Kunci Darurat**: kunci dengan kontrol total yang ditangguhkan untuk memulihkan dana jika terjadi kehilangan kunci



Tekan **Simpan Perubahan**. Kemudian pilih 3 kunci yang akan membentuk wallet Anda dari yang diimpor (mis. Kunci Benih, Coldcard MK4SP, dan Tapsigner Metro).



## Menetapkan tenggat waktu kunci khusus



Layar berikutnya memungkinkan Anda mengonfigurasi Tombol Darurat dan Tombol Warisan. Di sinilah Anda menentukan penundaan yang mengatur aktivasi kunci khusus ini.



![Configuration des délais](assets/fr/07.webp)



Untuk **Kunci Darurat**, pilih kunci perangkat keras yang akan berfungsi sebagai cadangan utama (di sini Coldcard MK4) dan pilih penundaan aktivasi (dalam contoh kami: 2 tahun). Tidak seperti Kunci Warisan, Kunci Darurat tidak menambah kuorum: kunci ini memungkinkan Anda untuk **memotong multisig** sepenuhnya, dan memberikan Anda kendali penuh atas dana setelah batas waktu berakhir. Ini adalah solusi terakhir Anda: jika beberapa kunci hilang atau dihancurkan, kunci tunggal ini memungkinkan Anda untuk memulihkan semuanya. Oleh karena itu, kunci ini harus dilindungi dengan sangat ketat.



Untuk **Kunci Warisan**, pilih kunci yang ditujukan untuk ahli waris (di sini Coldcard MK4SP) dan pilih penundaan (dalam contoh kami: 1 tahun). Setelah satu tahun tanpa pergerakan, kunci ini **akan ditambahkan ke kuorum tanda tangan**. Secara praktis, wallet 2-of-3 Anda akan menjadi wallet 2-of-4 setelah periode ini berlalu, sehingga ahli waris dapat berpartisipasi dalam penandatanganan bersama dengan kunci yang ada.



### Bagaimana cara kerja kunci waktu?



Bitcoin Keeper menggunakan **pengunci waktu absolut** (CLTV - CheckLockTimeVerify), yang dimungkinkan oleh Miniscript. Tidak seperti penguncian waktu relatif (CSV), yang dimulai ketika setiap UTXO diterima, penguncian waktu absolut bekerja dengan **tanggal kedaluwarsa tetap** yang ditentukan ketika wallet dibuat.



Secara konkret, jika Anda membuat wallet hari ini dengan Inheritance Key 1 tahun, tanggal aktivasi adalah "hari ini + 1 tahun". Semua dana yang disimpan dalam wallet ini, kapan pun tanggal penyetorannya, akan dapat diakses melalui Kunci Warisan pada tanggal yang sama.



Keuntungan dari timelock absolut adalah memungkinkan waktu tunggu lebih dari 15 bulan (batas timelock CSV relatif), yang menjelaskan mengapa Bitcoin Keeper dapat menawarkan opsi seperti 2 tahun.



### Mekanisme penyegaran



Untuk mencegah aktivasi kunci khusus selama masa pakai, Anda harus "menyegarkan" wallet Anda secara berkala. Dengan penguncian waktu absolut, hal ini melibatkan **pembuatan ulang wallet dengan tanggal kedaluwarsa baru** yang diundur ke masa depan, kemudian mentransfer dana Anda ke wallet baru ini.



Bitcoin Keeper menyederhanakan proses ini dengan fungsi penyegaran yang terintegrasi. Aplikasi ini secara otomatis menangani kerumitan di latar belakang: Anda cukup mengikuti langkah-langkah yang dipandu, tanpa harus membuat wallet baru secara manual atau mentransfer dana sendiri. Rencanakan operasi ini secara teratur, jauh sebelum berakhirnya jangka waktu terpendek yang dikonfigurasi. Misalnya, dengan Inheritance Key 1 tahun, lakukan penyegaran setiap 9-10 bulan untuk menjaga margin keamanan.



## Menyimpan dan mengekspor konfigurasi



Setelah wallet dibuat, aplikasi akan mengingatkan Anda untuk menyimpan file konfigurasi. **Langkah ini sangat penting**: tanpa file ini, ahli waris Anda tidak akan dapat menyusun ulang multisig wallet.



![Export de la configuration](assets/fr/08.webp)



Tekan **Backup Wallet Recovery File**. Beberapa opsi ekspor tersedia:




- Ekspor PDF **: menghasilkan dokumen lengkap dengan semua informasi wallet
- Tampilkan QR**: menampilkan kode QR untuk mengimpor konfigurasi pada perangkat lain
- Airdrop / Ekspor File**: mengekspor file melalui opsi berbagi
- NFC**: berbagi melalui NFC dengan perangkat yang kompatibel



Gandakan salinannya: satu di notaris Anda, satu di brankas bank, satu lagi versi digital terenkripsi. wallet baru Anda sekarang muncul di tab Dompet dengan label "Multi-kunci", "2 dari 3", "Kunci Warisan", dan "Kunci Darurat".



## Membuat Kenari Wallet



Canary Wallet adalah sistem peringatan dini. Idenya: setiap kunci yang digunakan dalam multi-kunci wallet juga dapat digunakan dalam kunci tunggal wallet yang terpisah. Dengan menyimpan sejumlah kecil uang pada "kenari" wallet ini, setiap gerakan yang tidak sah menandakan adanya kompromi pada kunci tersebut.



![Canary Wallets](assets/fr/09.webp)



Ada dua cara untuk mengonfigurasi Canary Wallet. Dari tab **Lainnya**, tekan **Dompet Kenari** di bagian "Kunci dan Dompet". Layar akan menjelaskan prinsipnya: jika seseorang mengakses salah satu kunci Anda dan menemukan dana di kunci tunggal wallet yang terkait, mereka akan mencoba menghapusnya, yang akan memperingatkan Anda.



![Configuration Canary depuis une clé](assets/fr/10.webp)



Anda juga dapat mengonfigurasi Canary secara langsung dari tombol. Pada tab **Keys**, pilih tombol (mis. Tapsigner Genesis), tekan ikon **Pengaturan** (roda gigi), lalu **Canary Wallet**. Kenari wallet yang terkait akan terbuka, siap untuk menerima beberapa satoshi pengawasan.



Depositkan sejumlah kecil dana (beberapa ribu satoshi) pada setiap Canary Wallet. Jika dana ini berpindah tanpa persetujuan Anda, segera hapus kunci yang disusupi dari brankas multisig Anda.



## Praktik terbaik



**Uji coba konfigurasi Anda** dengan sejumlah kecil uang sebelum memasukkan uang dalam jumlah besar. Kirim beberapa ribu satoshi ke brankas, lalu coba pengeluaran keluar untuk memeriksa apakah Anda telah menguasai proses penandatanganan dengan setiap perangkat. Coba juga mengimpor file konfigurasi di ponsel lain untuk memastikan bahwa cadangannya berfungsi.



**Bagikan kunci secara cerdas**. Untuk Tapsigner, serahkan dalam amplop tertutup dengan PIN yang dikomunikasikan secara terpisah (misalnya, dalam surat Instruksi Pemulihan yang disimpan di tempat lain). Untuk dompet perangkat keras klasik, simpan perangkat pada pihak ketiga yang tepercaya dan seed di atas kertas atau logam bersama Anda atau pihak ketiga lainnya. Catat sidik jari setiap tombol dan namanya dalam file konfigurasi untuk menghindari kebingungan.



**Rencanakan uji coba berkala** (latihan kebakaran). Setiap tahun, periksa apakah Anda dapat membangun kembali brankas dari cadangan pada telepon kosong. Uji peringatan Canary dengan memeriksa saldo. Simulasikan skenario kehilangan ("bagaimana jika saya kehilangan Coldcard?") untuk memastikan bahwa kombinasi kunci yang tersisa sudah mencukupi.



**Jangan lupa untuk menyegarkan diri Anda. Jika Anda telah mengatur Kunci Warisan Anda menjadi 1 tahun, segarkan diri Anda setiap 9-10 bulan. Ini adalah harga yang Anda bayarkan untuk transmisi otomatis tanpa campur tangan pihak ketiga.



**Selalu perbarui rencana tersebut**. Setiap perubahan (penggantian kunci, perubahan ahli waris, perubahan tenggat waktu) harus tercermin dalam semua cadangan dan dokumen. Buat ulang PDF setelah setiap modifikasi dan distribusikan versi baru.



## Batasan dan pertimbangan



Terlepas dari kekuatan alat bantu ini, penting untuk mengenali keterbatasannya agar dapat mengelolanya seefektif mungkin.



Kerumitan brankas multisig dengan penguncian waktu dapat menjadi risiko tersendiri: kesalahan konfigurasi, kesalahpahaman oleh ahli waris, kehilangan elemen penting di antara banyak komponen. Bitcoin Keeper menyederhanakan pengalaman semaksimal mungkin, tetapi tetap merupakan operasi teknis. Gunakanlah paket ini hanya jika jumlah yang akan dilindungi sesuai dengan kebutuhan. Untuk jumlah yang kecil, rencana yang lebih sederhana mungkin sudah cukup.



Ketergantungan aplikasi **application dependency** perlu dipikirkan. Walaupun kodenya bersifat open source dan berdasarkan standar terbuka (Miniscript, BSMS), beberapa fungsi tertentu bergantung pada ekosistem Keeper. Simpanlah salinan aplikasi (Android APK atau iOS IPA) dan dokumentasikan dalam surat-surat Anda kepada ahli waris mengenai kemungkinan menggunakan dompet yang kompatibel dengan Miniscript (seperti Liana) untuk memulihkan dana.



Broker tepercaya** memperkenalkan risiko manusia. Apa yang terjadi jika kerabat yang berniat buruk menggunakan kunci yang dipercayakan kepadanya sebelum tenggat waktu? Atau jika pengacara salah meletakkan dokumen Anda? Pilihlah orang-orang ini dengan hati-hati, jelaskan tanggung jawab mereka dengan jelas, dan miliki rencana B. Dompet Kenari, cadangan yang berlebihan, dan struktur multisig tetap menjadi perlindungan terbaik Anda terhadap bahaya-bahaya ini.



## Kesimpulan



Bitcoin Keeper, dengan paket Diamond Hands-nya, menawarkan kotak peralatan lengkap untuk perencanaan perkebunan: Brankas yang disempurnakan dengan kunci berjangka waktu, dokumen yang menyertai, Dompet Kenari, dan dukungan yang dipersonalisasi.



Ini lebih dari sekadar masalah teknis: ini adalah pertanyaan tentang merancang arsitektur perkebunan Anda, mendistribusikan kunci dan pengetahuan dengan cerdas, dan secara teratur menguji sistem. Rencana warisan Bitcoin yang dirancang dengan baik akan mengubah satoshi Anda menjadi warisan yang nyata dan dapat dipindahtangankan.