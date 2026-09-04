---
name: Bitcoin Keeper - Rencana Warisan
description: Rencanakan pengiriman bitcoin milikmu dengan Bitcoin Keeper
---

![cover](assets/cover.webp)



Pengalihan aset Bitcoin adalah salah satu tantangan yang paling sering diremehkan oleh para pemegangnya. Tidak seperti rekening bank, di mana lembaga keuangan dapat menyalurkan dana kepada ahli waris yang sah, Bitcoin sepenuhnya bergantung pada kepemilikan private key. Ahli waris yang sah secara hukum tidak akan pernah bisa mengakses dana tanpa kunci ini, sementara pihak jahat yang memegang rahasia tersebut dapat membelanjakannya tanpa formalitas apa pun.



Dalam tutorial Bitcoin Keeper kedua ini, kita akan menjelajahi fitur-fitur premium yang didedikasikan untuk perencanaan warisan. Aplikasi ini menawarkan alat canggih untuk membuat **Enhanced Vault**, dengan mekanisme perlindungan berbasis waktu berkat Miniscript, serta dokumen pendukung untuk memandu orang-orang yang kamu cintai.



Panduan ini mengasumsikan bahwa kamu telah menguasai dasar-dasar Bitcoin Keeper (pembuatan portofolio, multisig klasik, menambahkan hardware wallet) seperti yang dijelaskan dalam tutorial pertama kami:




https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

![video](https://youtu.be/tCld_-n2d30)



## Paket berlangganan Bitcoin Keeper



Bitcoin Keeper beroperasi dengan model freemium dengan tiga tingkat langganan yang menawarkan fungsionalitas secara bertahap. Untuk mengakses paketnya, buka tab **Lainnya**, lalu ketuk paket kamu saat ini (standarnya adalah "Pleb") untuk membuka layar **Kelola Langganan**.



![Plans d'abonnement](assets/fr/01.webp)



Paket **Pleb** (gratis) menyediakan akses ke hal-hal penting: pembuatan dompet satu kunci dan multi-kunci tanpa batas, kompatibilitas dengan semua hardware wallet utama (Coldcard, Trezor, Ledger, Jade, Tapsigner...), coin control, pelabelan, serta koneksi ke server Electrum pribadi. Paket ini sudah cukup untuk penggunaan standar, bahkan untuk konfigurasi multi-sig klasik.



Paket **Hodler** (€9.99/bulan, dengan gratis 1 bulan jika dibayar tahunan) mencakup semua fitur Pleb dan menambahkan cadangan terenkripsi ke cloud (iCloud atau Google Drive) untuk memulihkan brankas kamu di perangkat apa pun, **Server Key** untuk menambahkan kebijakan pengeluaran otomatis dan 2FA di atas ambang batas tertentu, serta **Canary Wallet** untuk mendeteksi akses tidak sah ke kunci kamu.



Paket **Diamond Hands** (€29.99/bulan, dengan gratis 1 bulan jika dibayar tahunan) adalah paket paling lengkap untuk perencanaan warisan. Paket ini mencakup seluruh fitur Hodler dan membuka **Inheritance Key** (aktivasi tertunda), **Emergency Key** (kunci darurat untuk pemulihan jika terjadi kehilangan), alat serta dokumen **Inheritance Planning**, dan panggilan dukungan dengan tim Concierge untuk memvalidasi konfigurasi kamu. Ini adalah penawaran untuk para bitcoiner yang ingin mewariskan aset mereka lintas generasi.



Poin penting: brankas yang sudah kamu buat akan tetap bisa diakses meskipun kamu kembali ke paket gratis. Konfigurasi kamu berbasis standar terbuka (BSMS, Miniscript) dan beroperasi secara independen dari status langganan kamu.




## Dokumen warisan



Setelah kamu mengaktifkan langganan Diamond Hands, buka bagian **Dokumen Warisan** dari tab **Lainnya**. Bitcoin Keeper menyediakan lima contoh dokumen untuk membantu menyusun rencana warisan kamu, serta satu bagian berisi tips:



![Documents d'héritage](assets/fr/02.webp)





- **Template Seedphrase**: template untuk mencatat seedphrase kamu dengan rapi dan terorganisir
- **Kontak Tepercaya**: template untuk mencantumkan detail kontak orang-orang tepercaya yang terlibat dalam rencana kamu (notaris, pengacara, ahli waris, pemegang kunci)
- **Kunci Berbagi Tambahan**: dokumen yang merinci informasi teknis untuk setiap kunci, seperti PIN, jalur derivasi, lokasi fisik, jenis perangkat, dan informasi lain yang berguna untuk mengidentifikasi serta menggunakan kunci
- **Petunjuk Pemulihan**: panduan langkah demi langkah bagi ahli waris atau penerima manfaat untuk memulihkan dana
- **Surat untuk Pengacara**: surat siap pakai yang dapat disesuaikan untuk pengacara atau notaris kamu




Bagian **Tips Warisan** menawarkan saran praktis untuk mengamankan kunci bagi ahli waris dan mengoptimalkan rencana warisan.



Sesuaikan dokumen-dokumen ini agar sesuai dengan situasi kamu, dan simpanlah di tempat yang aman, terpisah dari kunci itu sendiri.



## Mengonfigurasi Pencadangan Cloud



Sebelum membuat brankas lama, aktifkan pencadangan awan untuk melindungi file konfigurasi kamu. Dari tab Lainnya, tekan **Cadangan Cloud Pribadi**.



![Configuration Cloud Backup](assets/fr/03.webp)



Pilih kata sandi yang kuat untuk mengenkripsi cadangan kamu. Kata sandi ini hanya melindungi file konfigurasi wallet, bukan private key kamu. Konfirmasikan kata sandi tersebut dan tekan **Konfirmasi**. Cadangan kamu akan disimpan di iCloud atau Google Drive, tergantung pada perangkat yang kamu gunakan. Tekan **Backup Now** untuk memulai pencadangan pertama kamu.



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


Setelah semua kunci kamu diimpor, kamu akan menemukannya di tab Kunci dengan nama khusus.



## Buat wallet yang sudah ada sebelumnya



Mari kita lanjutkan ke pembuatan trunk. Dari tab **Wallets**, tekan **Addend Wallet**, pilih **Bitcoin Wallet**, kemudian **Create Wallet**.



![Création du wallet](assets/fr/05.webp)



Pilih tipe wallet. Untuk paket lama kami, pilih **2 dari 3 kunci multi**. Di bagian bawah layar, aktifkan **Pilihan Keamanan yang Ditingkatkan** lalu tekan **Lanjutkan**.



![Options de sécurité avancées](assets/fr/06.webp)



Pada popup Opsi Keamanan yang Ditingkatkan, centang :




- Kunci Warisan**: kunci tambahan yang akan ditambahkan ke kuorum setelah jangka waktu tertentu
- Kunci Darurat**: kunci dengan kontrol total yang ditangguhkan untuk memulihkan dana jika terjadi kehilangan kunci



Tekan **Simpan Perubahan**. Kemudian pilih 3 kunci yang akan membentuk wallet kamu dari yang diimpor (mis. Seedphrase, Coldcard MK4SP, dan Tapsigner Metro).



## Menetapkan tenggat waktu kunci khusus



Layar berikutnya memungkinkan kamu mengonfigurasi Tombol Darurat dan Tombol Warisan. Di sinilah kamu menentukan penundaan yang mengatur aktivasi kunci khusus ini.



![Configuration des délais](assets/fr/07.webp)



Untuk **Kunci Darurat**, pilih hardware wallet yang akan berfungsi sebagai cadangan utama (di sini Coldcard MK4) dan tentukan penundaan aktivasi (dalam contoh ini: 2 tahun). Berbeda dengan Kunci Warisan, Kunci Darurat tidak menambah kuorum. Kunci ini memungkinkan kamu untuk **memotong multisig** sepenuhnya dan memberi kamu kendali penuh atas dana setelah batas waktu berakhir. Ini adalah solusi terakhir kamu: jika beberapa kunci hilang atau dihancurkan, satu kunci ini memungkinkan kamu memulihkan semuanya. Karena itu, kunci ini harus dilindungi dengan sangat ketat.



Untuk **Kunci Warisan**, pilih kunci yang ditujukan untuk ahli waris (di sini Coldcard MK4SP) dan tentukan penundaan (dalam contoh ini: 1 tahun). Setelah satu tahun tanpa aktivitas, kunci ini **akan ditambahkan ke kuorum tanda tangan**. Secara praktis, wallet 2-of-3 kamu akan menjadi wallet 2-of-4 setelah periode ini berlalu, sehingga ahli waris dapat ikut serta dalam proses penandatanganan bersama kunci-kunci yang sudah a



### Bagaimana cara kerja kunci waktu?



Bitcoin Keeper menggunakan **absolute timelock** (CLTV - CheckLockTimeVerify), yang dimungkinkan oleh Miniscript. Berbeda dengan relative timelock (CSV), yang mulai berjalan saat setiap UTXO diterima, absolute timelock bekerja dengan **tanggal kedaluwarsa tetap** yang ditentukan ketika wallet dibuat.



Secara konkret, jika kamu membuat wallet hari ini dengan Inheritance Key selama 1 tahun, maka tanggal aktivasinya adalah "hari ini + 1 tahun". Semua dana yang disimpan di wallet ini, kapan pun tanggal penyetorannya, akan bisa diakses melalui Kunci Warisan pada tanggal yang sama.



Keuntungan dari absolute timelock adalah memungkinkan waktu tunggu lebih dari 15 bulan (batas pada CSV relative timelock), yang menjelaskan mengapa Bitcoin Keeper dapat menawarkan opsi seperti 2 tahun.




### Mekanisme penyegaran



Untuk mencegah aktivasi kunci khusus selama masa pakai, kamu perlu "menyegarkan" wallet secara berkala. Dengan absolute timelock, proses ini melibatkan **pembuatan ulang wallet dengan tanggal kedaluwarsa baru** yang diundur ke masa depan, lalu mentransfer dana kamu ke wallet baru tersebut.



Bitcoin Keeper menyederhanakan proses ini dengan fitur penyegaran terintegrasi. Aplikasi ini secara otomatis menangani kerumitan di latar belakang. Kamu cukup mengikuti langkah-langkah yang dipandu, tanpa perlu membuat wallet baru secara manual atau mentransfer dana sendiri. Jadwalkan proses ini secara rutin, jauh sebelum jangka waktu terpendek yang dikonfigurasi berakhir. Sebagai contoh, dengan Inheritance Key 1 tahun, lakukan penyegaran setiap 9 hingga 10 bulan untuk menjaga margin keamanan.



## Menyimpan dan mengekspor konfigurasi



Setelah wallet dibuat, aplikasi akan mengingatkan kamu untuk menyimpan file konfigurasi. **Langkah ini sangat penting**: tanpa file ini, ahli waris kamu tidak akan dapat menyusun ulang multisig wallet.



![Export de la configuration](assets/fr/08.webp)



Tekan **Backup Wallet Recovery File**. Beberapa opsi ekspor tersedia:




- Ekspor PDF **: menghasilkan dokumen lengkap dengan semua informasi wallet
- Tampilkan QR**: menampilkan kode QR untuk mengimpor konfigurasi pada perangkat lain
- Airdrop / Ekspor File**: mengekspor file melalui opsi berbagi
- NFC**: berbagi melalui NFC dengan perangkat yang kompatibel



Gandakan salinannya: satu di notaris Anda, satu di brankas bank, satu lagi versi digital terenkripsi. wallet baru kamu sekarang muncul di tab Dompet dengan label "Multi-kunci", "2 dari 3", "Kunci Warisan", dan "Kunci Darurat".



## Membuat Kenari Wallet



Canary Wallet adalah sistem peringatan dini. Idenya: setiap kunci yang digunakan dalam multi-kunci wallet juga dapat digunakan dalam kunci tunggal wallet yang terpisah. Dengan menyimpan sejumlah kecil uang pada "kenari" wallet ini, setiap gerakan yang tidak sah menandakan adanya kompromi pada kunci tersebut.



![Canary Wallets](assets/fr/09.webp)



Ada dua cara untuk mengonfigurasi Canary Wallet. Dari tab **Lainnya**, tekan **Dompet Kenari** di bagian "Kunci dan Dompet". Layar akan menjelaskan prinsipnya: jika seseorang mengakses salah satu kunci kamu dan menemukan dana di kunci tunggal wallet yang terkait, mereka akan mencoba menghapusnya, yang akan memperingatkanmu.



![Configuration Canary depuis une clé](assets/fr/10.webp)



Kamu juga dapat mengonfigurasi Canary secara langsung dari tombol. Pada tab **Keys**, pilih tombol (mis. Tapsigner Genesis), tekan ikon **Pengaturan** (roda gigi), lalu **Canary Wallet**. Kenari wallet yang terkait akan terbuka, siap untuk menerima beberapa satoshi pengawasan.



Depositkan sejumlah kecil dana (beberapa ribu satoshi) pada setiap Canary Wallet. Jika dana ini berpindah tanpa persetujuanmu, segera hapus kunci yang disusupi dari brankas multisig kamu.



## Praktik terbaik



**Uji coba konfigurasi kamu** dengan jumlah kecil sebelum memasukkan dana dalam jumlah besar. Kirim beberapa ribu satoshi ke brankas, lalu coba melakukan pengeluaran untuk memastikan kamu sudah memahami proses penandatanganan dengan setiap perangkat. Coba juga mengimpor file konfigurasi di ponsel lain untuk memastikan cadangannya berfungsi dengan baik.



**Bagikan kunci secara cerdas**. Untuk Tapsigner, serahkan dalam amplop tertutup dengan PIN yang dikomunikasikan secara terpisah, misalnya melalui Surat Petunjuk Pemulihan yang disimpan di lokasi lain. Untuk hardware wallet klasik, simpan perangkat pada pihak ketiga yang tepercaya dan seedphrase di atas kertas atau logam bersama kamu atau pihak ketiga lainnya. Catat fingerprint setiap key dan namanya di file konfigurasi untuk menghindari kebingungan.



**Rencanakan pengujian berkala** (fire drill). Setiap tahun, periksa apakah kamu dapat membangun kembali brankas dari cadangan di ponsel kosong. Uji peringatan Canary dengan memeriksa saldo. Simulasikan skenario kehilangan, seperti "bagaimana jika aku kehilangan Coldcard", untuk memastikan kombinasi kunci yang tersisa masih mencukupi.



**Jangan lupa melakukan penyegaran secara berkala**. Jika kamu mengatur Kunci Warisan menjadi 1 tahun, lakukan penyegaran setiap 9 hingga 10 bulan. Ini adalah konsekuensi yang harus diterima untuk transmisi otomatis tanpa campur tangan pihak ketiga.



**Selalu perbarui rencana tersebut**. Setiap perubahan, baik penggantian kunci, perubahan ahli waris, maupun perubahan tenggat waktu, harus tercermin di semua cadangan dan dokumen. Buat ulang PDF setelah setiap modifikasi dan distribusikan versi terbaru.




## Batasan dan pertimbangan



Terlepas dari kekuatan alat-alat ini, penting untuk mengenali keterbatasannya agar kamu bisa mengelolanya seefektif mungkin.



Kerumitan brankas multisig dengan timelock bisa menjadi risiko tersendiri: kesalahan konfigurasi, kesalahpahaman oleh ahli waris, atau hilangnya elemen penting di antara banyak komponen. Bitcoin Keeper menyederhanakan pengalaman semaksimal mungkin, tetapi tetap merupakan operasi teknis. Gunakan paket ini hanya jika jumlah yang ingin dilindungi memang sepadan dengan tingkat kompleksitasnya. Untuk jumlah yang lebih kecil, rencana yang lebih sederhana mungkin sudah cukup.



Ketergantungan pada aplikasi juga perlu dipertimbangkan. Walaupun kodenya bersifat open source dan berbasis standar terbuka (Miniscript, BSMS), beberapa fungsi tertentu tetap bergantung pada ekosistem Keeper. Simpan salinan aplikasi (Android APK atau iOS IPA) dan dokumentasikan dalam surat kepada ahli waris tentang kemungkinan menggunakan wallet yang kompatibel dengan Miniscript, seperti Liana, untuk memulihkan dana.



**Broker tepercaya** memperkenalkan risiko manusia. Apa yang terjadi jika kerabat yang berniat buruk menggunakan kunci yang dipercayakan kepadanya sebelum tenggat waktu? Atau jika pengacara salah menyimpan dokumen kamu? Pilih orang-orang ini dengan sangat hati-hati, jelaskan tanggung jawab mereka secara jelas, dan siapkan rencana cadangan. Dompet Kenari, cadangan berlapis, dan struktur multisig tetap menjadi perlindungan terbaik kamu terhadap risiko-risiko ini.



## Kesimpulan



Bitcoin Keeper, melalui paket Diamond Hands, menawarkan kotak peralatan lengkap untuk perencanaan warisan: Brankas yang Disempurnakan dengan kunci berjangka waktu, dokumen pendukung, Dompet Kenari, dan dukungan yang dipersonalisasi.



Ini bukan sekadar persoalan teknis. Ini adalah tentang merancang arsitektur warisan kamu, mendistribusikan kunci dan pengetahuan secara cerdas, serta menguji sistem secara rutin. Rencana warisan Bitcoin yang dirancang dengan baik akan mengubah satoshi kamu menjadi warisan yang nyata dan dapat dipindahtangankan.
