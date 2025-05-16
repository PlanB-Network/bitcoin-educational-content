---
name: Trezor Safe 3
description: Mengkonfigurasi dan menggunakan Hardware Wallet Safe 3
---
![cover](assets/cover.webp)



*Kredit gambar: [Trezor.io](https://trezor.io/)*



Trezor Safe 3 adalah Hardware Wallet yang dirancang oleh SatoshiLabs dan dibuat pada tahun 2023. Ini adalah model yang sangat ringkas dan ringan (14 gram) yang dirancang untuk pengguna pemula dan menengah. Ini adalah penerus Model One yang terkenal, dengan tambahan yang signifikan, dengan tetap mempertahankan pendekatan sumber terbuka merek yang membedakannya dari pesaing utamanya, Ledger. Safe 3 dibanderol dengan harga €79. Oleh karena itu, Safe 3 diposisikan di segmen Hardware Wallet kelas menengah, bersaing langsung dengan Ledger Nano S Plus.



Safe 3 tidak memiliki baterai dan beroperasi secara eksklusif melalui koneksi USB-C, yang digunakan untuk daya dan komunikasi. Dilengkapi dengan layar OLED monokrom 0,96 inci dan dua tombol fisik.



![Image](assets/fr/01.webp)



Safe 3 menawarkan semua fitur penting yang diharapkan dari sebuah Hardware Wallet yang baik, termasuk integrasi yang sangat baik dari passphrase BIP39. Namun, belum mendukung Miniscript.



Model ini khususnya cocok untuk pemula, dan bahkan mungkin Hardware Wallet yang saya rekomendasikan kepada pengguna baru. Kamera ini juga cocok untuk pengguna tingkat menengah. Di sisi lain, ini mungkin tidak memenuhi semua harapan pengguna tingkat lanjut yang mencari fitur yang lebih spesifik, yang tersedia pada perangkat seperti Coldcard. Namun demikian, jika Anda tidak memerlukan opsi tingkat lanjut ini, Trezor Safe 3 mungkin merupakan pilihan yang sangat baik.



## Model keamanan Trezor Safe 3



Trezor Safe 3 kini dilengkapi dengan **Secure Element** bersertifikasi EAL6+, sebuah kemajuan yang signifikan dari model sebelumnya seperti Model One dan Model T. Ini adalah chip OPTIGA Trust M V3, yang tidak secara langsung menyimpan seed, tetapi bertindak sebagai komponen kriptografi untuk mengamankan akses ke seed. Secure Element menyimpan rahasia yang hanya dapat diakses setelah pengguna memasukkan PIN dengan benar. Rahasia ini kemudian digunakan untuk mendekripsi seed, yang disimpan secara terenkripsi dalam memori utama perangkat.



Sistem keamanan hibrida ini menawarkan perlindungan fisik yang lebih baik, terutama terhadap serangan ekstraksi atau analisis invasif, masalah yang rentan terjadi pada Model One, terutama dalam manajemen PIN. Kerentanan ini sekarang dapat diatasi berkat penggunaan Secure Element. Model ini juga mempertahankan arsitektur perangkat lunak sumber terbuka: kode yang mengelola pembuatan dan penggunaan kunci privat tetap dapat diakses dan diverifikasi sepenuhnya. Chip OPTIGA hanya mengelola kode PIN, sebuah elemen di luar manajemen kunci Bitcoin Wallet. Chip ini hanya mengeluarkan rahasia yang dapat digunakan untuk mendekripsi seed. Selain itu, chip OPTIGA Trust M V3 mendapatkan keuntungan dari lisensi yang relatif gratis, yang memberikan wewenang kepada SatoshiLabs untuk secara bebas mempublikasikan potensi kerentanan.



Model keamanan ini, menurut pendapat saya, merupakan salah satu kompromi terbaik yang tersedia di pasaran saat ini. Model ini menggabungkan keunggulan Secure Element dengan manajemen perangkat lunak sumber terbuka. Sebelumnya, pengguna harus memilih antara keamanan fisik yang ditingkatkan dengan sebuah chip dan transparansi dengan sumber terbuka; dengan Trezor Safe 3, pengguna bisa mendapatkan keuntungan dari keduanya.



Dalam tutorial ini, kami akan menunjukkan kepada Anda cara mengatur dan menggunakan Trezor Safe 3 Anda dengan aman.



## Membongkar Kotak Brankas Trezor 3



Ketika Anda menerima Safe 3, pastikan kotak dan Seal dalam keadaan utuh untuk mengonfirmasi bahwa paket tersebut belum dibuka. Verifikasi perangkat lunak terhadap keaslian dan integritas perangkat juga akan dilakukan saat perangkat ini dipasang nanti.



Isi kotak termasuk:




- Trezor Safe 3;
- Kantung yang berisi stok kartu untuk mencatat frasa, stiker, dan instruksi Mnemonic Anda;
- Kabel USB-C ke USB-C.



![Image](assets/fr/02.webp)



Ketika dibuka, Trezor Safe 3 Anda harus dilindungi oleh plastik pelindung dan port USB-C harus diamankan dengan Seal hologram. Pastikan itu ada di sana.



![Image](assets/fr/03.webp)



Navigasi pada perangkat ini sangat mudah: gunakan tombol kanan untuk menggulir ke kanan, dan tombol kiri untuk menggulir ke kiri. Tekan kedua tombol secara bersamaan untuk mengonfirmasi tindakan.



![Image](assets/fr/04.webp)



## Prasyarat



Untuk tutorial ini, saya akan menunjukkan kepada Anda bagaimana cara menggunakan Trezor Safe 3 dengan [perangkat lunak manajemen portofolio Sparrow Wallet] (https://sparrowwallet.com/download/). Jika Anda belum menginstal perangkat lunak ini, silakan lakukan sekarang. Jika Anda membutuhkan bantuan, kami juga memiliki tutorial terperinci tentang cara mengonfigurasi Sparrow Wallet:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Anda juga memerlukan perangkat lunak Trezor Suite untuk mengonfigurasi Safe 3, memeriksa keasliannya, dan menginstal firmware. Kami hanya akan menggunakan perangkat lunak ini untuk itu saja, dan setelah itu hanya diperlukan untuk pembaruan firmware. Untuk pengelolaan Wallet sehari-hari, kita akan menggunakan Sparrow Wallet secara eksklusif, karena dioptimalkan untuk Bitcoin dan mudah digunakan, bahkan untuk pemula (Sparrow hanya mendukung Bitcoin, bukan altcoin).



[Unduh Trezor Suite dari situs web resmi](https://trezor.io/trezor-suite)



![Image](assets/fr/05.webp)



Untuk kedua program ini, saya sangat menyarankan agar Anda memeriksa keasliannya (dengan GnuPG) dan integritasnya (melalui Hash) sebelum menginstalnya di komputer Anda. Jika Anda tidak tahu cara melakukannya, Anda dapat mengikuti tutorial lain ini:



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Memulai Trezor Safe 3



Sambungkan Safe 3 Anda ke komputer yang sudah terinstal Trezor Suite dan Sparrow Wallet.



![Image](assets/fr/06.webp)



Buka Trezor Suite, lalu klik "*Setup my Trezor*".



![Image](assets/fr/07.webp)



Pilih "*Firmware khusus Bitcoin*", lalu klik "*Instal Bitcoin saja*".



![Image](assets/fr/08.webp)



Trezor Suite kemudian akan menginstal firmware pada Brankas 3 Anda. Mohon tunggu selama proses instalasi.



![Image](assets/fr/09.webp)



Klik "*Lanjutkan*".



![Image](assets/fr/10.webp)



Kemudian lanjutkan ke uji keaslian untuk memastikan Hardware Wallet Anda tidak palsu atau disusupi.



![Image](assets/fr/11.webp)



Pada Safe 3 Anda, tekan tombol kanan untuk mengonfirmasi.



![Image](assets/fr/12.webp)



Jika Trezor Anda asli, pesan konfirmasi akan muncul di Trezor Suite.



![Image](assets/fr/13.webp)



Anda kemudian dapat melewati jendela dengan petunjuk pengoperasian dasar.



![Image](assets/fr/14.webp)



## Menciptakan portofolio Bitcoin



Pada Trezor Suite, klik tombol "*Buat Wallet baru*".



![Image](assets/fr/15.webp)



Untuk portofolio standar, Anda bisa memilih jenis cadangan default. Ini akan menciptakan portofolio tanda tangan tunggal klasik dengan frasa Mnemonic sebanyak 12 kata. Klik "*Buat Wallet*".



Jika Anda ingin mempelajari lebih lanjut tentang opsi pencadangan lain yang tersedia di Trezor, termasuk *Cadangan Multi-Bagi*, saya sarankan Anda juga membaca tutorial ini:



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/16.webp)



Terima persyaratan penggunaan pada Hardware Wallet.



![Image](assets/fr/17.webp)



Tekan tombol kanan sekali lagi untuk membuat portofolio baru.



![Image](assets/fr/18.webp)



Di Trezor Suite, klik "*Lanjutkan pencadangan*".



![Image](assets/fr/19.webp)



Perangkat lunak ini memberikan petunjuk tentang cara mengelola frasa Mnemonic Anda.



Mnemonic ini memberikan Anda akses penuh dan tidak terbatas ke semua bitcoin Anda. Siapa pun yang memiliki frasa ini dapat mencuri dana Anda, bahkan tanpa akses fisik ke Trezor Safe 3 Anda.



Frasa 12 kata ini mengembalikan akses ke bitcoin Anda jika terjadi kehilangan, pencurian, atau kerusakan pada Hardware Wallet Anda. Oleh karena itu, sangat penting untuk menyimpannya dengan hati-hati dan menyimpannya di tempat yang aman.



Anda bisa menuliskannya pada karton yang disertakan dalam kotak, atau untuk keamanan tambahan, saya sarankan untuk mengukirnya pada dasar baja tahan karat untuk melindunginya dari kebakaran, banjir atau keruntuhan.



Konfirmasikan petunjuknya, kemudian klik tombol "*Buat cadangan Wallet*".



![Image](assets/fr/20.webp)



Safe 3 akan membuat frasa Mnemonic Anda menggunakan generator angka acak. Pastikan Anda tidak diawasi selama operasi ini. Tuliskan kata-kata yang disediakan di layar pada media fisik pilihan Anda. Tergantung pada strategi keamanan Anda, Anda bisa mempertimbangkan untuk membuat beberapa salinan fisik lengkap dari frasa tersebut (tetapi yang terpenting, jangan membaginya). Sangat penting untuk membuat kata-kata tersebut bernomor dan berurutan.



***Tentu saja, Anda tidak boleh membagikan kata-kata ini di Internet, seperti yang saya lakukan dalam tutorial ini. Contoh Wallet ini hanya akan digunakan pada Testnet dan akan dihapus pada akhir tutorial



Untuk informasi lebih lanjut mengenai cara yang tepat untuk menyimpan dan mengelola frasa Mnemonic Anda, saya sangat merekomendasikan untuk mengikuti tutorial lainnya, khususnya jika Anda seorang pemula:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/21.webp)



Untuk beralih ke kata berikutnya, klik kanan. Anda dapat mundur dengan mengklik tombol kiri. Setelah Anda menuliskan semua kata, tahan tombol kanan untuk melanjutkan ke langkah berikutnya.



![Image](assets/fr/22.webp)



Pilih kata-kata dalam frasa Mnemonic Anda sesuai dengan urutannya untuk mengonfirmasi bahwa Anda telah menuliskannya dengan benar. Gunakan tombol kiri dan kanan untuk menavigasi di antara proposal, lalu pilih kata yang benar dengan mengklik 2 tombol secara bersamaan.



![Image](assets/fr/23.webp)



Setelah prosedur verifikasi ini selesai, klik tombol di sebelah kanan.



![Image](assets/fr/24.webp)



## Mengatur kode PIN



Berikutnya adalah langkah kode PIN. Kode PIN akan membuka kunci Trezor anda. Oleh karena itu, kode ini memberikan perlindungan terhadap akses fisik yang tidak sah. Kode PIN ini tidak terlibat dalam penurunan kunci kriptografi Wallet anda. Jadi, bahkan tanpa akses ke kode PIN, kepemilikan frasa Mnemonic 12 kata Anda akan memungkinkan Anda untuk mendapatkan kembali akses ke bitcoin Anda.



Pada Trezor Suite, klik "*Lanjutkan ke PIN*", lalu pada tombol "*Setel PIN*".



![Image](assets/fr/25.webp)



Konfirmasikan dengan Safe 3.



![Image](assets/fr/26.webp)



Kami menyarankan untuk memilih kode PIN yang seacak mungkin. Pastikan untuk menyimpan kode ini di lokasi yang terpisah dari tempat penyimpanan Trezor anda (contoh: di dalam pengelola kata sandi). Anda dapat menentukan kode PIN antara 8 hingga 50 digit. Saya sarankan anda untuk memilih kode PIN sepanjang mungkin untuk meningkatkan keamanan.



Gunakan tombol kiri dan kanan untuk memilih setiap digit. Untuk mengonfirmasi pilihan Anda dan beralih ke digit berikutnya, tekan kedua tombol secara bersamaan.



![Image](assets/fr/27.webp)



Setelah selesai, klik tanda centang "*ENTER*" di awal angka, lalu konfirmasikan PIN Anda untuk kedua kalinya.



![Image](assets/fr/28.webp)



Kode PIN Anda telah terdaftar.



![Image](assets/fr/29.webp)



Pada Trezor Suite, klik tombol "*Selesaikan pengaturan*".



![Image](assets/fr/30.webp)



Konfigurasi Safe 3 Anda sekarang sudah selesai. Jika mau, Anda bisa mengubah nama dan halaman beranda Hardware Wallet Anda.



![Image](assets/fr/31.webp)



Kita tidak akan memerlukan perangkat lunak Trezor Suite lagi, kecuali untuk melakukan pembaruan firmware secara berkala pada Hardware Wallet, atau jika Anda ingin menjalankan tes pemulihan. Sekarang kita akan menggunakan Sparrow untuk mengelola portofolio, karena perangkat lunak ini sangat cocok untuk penggunaan Bitcoin saja.



## Menyiapkan portofolio pada Sparrow Wallet



Mulailah dengan mengunduh dan menginstal Sparrow Wallet [dari situs web resmi] (https://sparrowwallet.com/) di komputer Anda, jika Anda belum melakukannya.



Setelah Anda membuka Sparrow Wallet, pastikan perangkat lunak ini terhubung ke node Bitcoin, yang ditandai dengan tanda centang di sudut kanan bawah Interface. Jika Anda mengalami masalah dalam menghubungkan Sparrow, saya sarankan Anda membaca bagian awal tutorial ini:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klik pada tab "*File*", kemudian pada "*New Wallet*".



![Image](assets/fr/32.webp)



Beri nama portofolio Anda, lalu klik "*Buat Wallet*".



![Image](assets/fr/33.webp)



Pada menu drop-down "*Jenis Skrip*", pilih jenis skrip yang akan digunakan untuk mengamankan bitcoin Anda. Saya merekomendasikan "*Taproot*", atau jika tidak ada, "*Native SegWit*".



![Image](assets/fr/34.webp)



Klik pada tombol "*Terhubung dengan Hardware Wallet*". Brankas 3 Anda tentu saja harus terhubung ke komputer dan tidak terkunci.



![Image](assets/fr/35.webp)



Klik pada tombol "*Pindai*". Brankas 3 Anda akan muncul. Klik "*Import Keystore*".



![Image](assets/fr/36.webp)



Anda sekarang dapat melihat detail Wallet Anda, termasuk kunci publik yang diperpanjang dari akun pertama Anda. Klik pada tombol "*Apply*" untuk menyelesaikan pembuatan Wallet.



![Image](assets/fr/37.webp)



Pilih kata sandi yang kuat untuk mengamankan akses ke Sparrow Wallet. Kata sandi ini akan memastikan akses yang aman ke data Sparrow Wallet Anda, melindungi kunci publik, alamat, label, dan riwayat transaksi Anda dari akses yang tidak sah.



Saya menyarankan Anda untuk menyimpan kata sandi ini dalam sebuah pengelola kata sandi agar Anda tidak lupa.



![Image](assets/fr/38.webp)



Dan sekarang, portofolio Anda sudah diimpor ke dalam Sparrow Wallet!



![Image](assets/fr/39.webp)



Sebelum anda menerima bitcoin pertama anda di dalam Wallet, **Saya sangat menyarankan anda untuk melakukan tes pemulihan kosong**. Tuliskan beberapa informasi referensi, seperti xpub Anda, kemudian setel ulang Trezor Safe 3 Anda ketika Wallet masih kosong. Kemudian cobalah untuk memulihkan Wallet anda pada Trezor menggunakan cadangan kertas anda. Periksa apakah xpub yang dihasilkan setelah pemulihan sesuai dengan yang anda tulis sebelumnya. Jika sesuai, Anda dapat yakin bahwa cadangan kertas Anda dapat diandalkan.



Untuk mempelajari lebih lanjut tentang cara melakukan tes pemulihan, saya sarankan Anda membaca tutorial lain ini:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Bagaimana cara menerima bitcoin dengan Trezor Safe 3?



Pada Sparrow, klik tab "*Receive*".



![Image](assets/fr/40.webp)



Sebelum menggunakan Address yang diusulkan oleh Sparrow Wallet, periksa di layar Trezor Anda. Praktik ini memungkinkan Anda untuk mengonfirmasi bahwa Address yang ditampilkan di Sparrow tidak palsu, dan bahwa Hardware Wallet memang menyimpan private key yang diperlukan untuk membelanjakan bitcoin yang diamankan dengan Address ini. Hal ini membantu Anda untuk menghindari beberapa jenis serangan.



Untuk melakukan pemeriksaan ini, klik tombol "*Display Address*".



![Image](assets/fr/41.webp)



Periksa apakah Address yang ditampilkan di Trezor Anda sesuai dengan yang ada di Sparrow Wallet. Sebaiknya Anda juga melakukan pemeriksaan ini sebelum mengirimkan Address Anda ke pengirim, untuk memastikan keabsahannya. Anda dapat menggunakan tombol untuk mengonfirmasi.



![Image](assets/fr/42.webp)



Anda kemudian dapat menambahkan "*Label*" untuk mendeskripsikan sumber bitcoin yang akan diamankan dengan Address ini. Ini adalah praktik yang baik yang memungkinkan Anda untuk mengelola UTXO dengan lebih baik.



![Image](assets/fr/43.webp)



Anda kemudian dapat menggunakan Address ini untuk menerima bitcoin.



![Image](assets/fr/44.webp)



## Bagaimana cara mengirim bitcoin dengan Trezor Safe 3?



Sekarang setelah Anda menerima Satss pertama Anda di Brankas 3-aman Wallet, Anda dapat membelanjakannya juga! Hubungkan Trezor Anda ke komputer, buka kuncinya menggunakan kode PIN, luncurkan Sparrow Wallet, lalu buka tab "*Kirim*" untuk membuat transaksi baru.



![Image](assets/fr/45.webp)



Jika Anda ingin *Coin Control*, yaitu memilih secara spesifik UTXO mana yang akan digunakan dalam transaksi, buka tab "*UTXOs*". Pilih UTXO yang ingin Anda gunakan, lalu klik "*Kirim Terpilih*". Anda akan diarahkan ke layar yang sama pada tab "*Kirim*", tetapi dengan UTXO yang sudah dipilih untuk transaksi.



![Image](assets/fr/46.webp)



Masukkan Address tujuan. Anda juga dapat memasukkan beberapa alamat dengan mengeklik tombol "*+ Tambah*".



![Image](assets/fr/47.webp)



Tuliskan "*Label*" untuk mengingat tujuan pengeluaran ini.



![Image](assets/fr/48.webp)



Pilih jumlah yang akan dikirim ke Address ini.



![Image](assets/fr/49.webp)



Sesuaikan tarif biaya transaksi Anda sesuai dengan pasar saat ini. Sebagai contoh, Anda dapat menggunakan [Mempool.space] (https://Mempool.space/) untuk memilih tarif biaya yang sesuai.



Pastikan semua parameter transaksi Anda sudah benar, lalu klik "*Buat Transaksi*".



![Image](assets/fr/50.webp)



Jika semuanya sudah sesuai dengan keinginan Anda, klik "*Finalisasi Transaksi untuk Penandatanganan*".



![Image](assets/fr/51.webp)



Klik "*Tanda Tangan*".



![Image](assets/fr/52.webp)



Klik "*Sign*" di sebelah Trezor Safe 3 Anda.



![Image](assets/fr/53.webp)



Periksa parameter transaksi pada layar Hardware Wallet Anda, termasuk penerima yang menerima Address, jumlah yang dikirim, dan biaya. Setelah transaksi diverifikasi di Trezor, klik kedua tombol secara bersamaan untuk menandatanganinya.



![Image](assets/fr/54.webp)



Transaksi Anda sekarang sudah ditandatangani. Periksa untuk terakhir kalinya apakah semuanya baik-baik saja, lalu klik "*Broadcast Transaction*" untuk menyiarkannya di jaringan Bitcoin.



![Image](assets/fr/55.webp)



Anda bisa menemukannya di tab "*Transactions*" pada Sparrow Wallet.



![Image](assets/fr/56.webp)



Selamat, Anda sekarang sudah menguasai penggunaan dasar Trezor Safe 3 dengan Sparrow Wallet! Untuk melangkah lebih jauh, saya merekomendasikan tutorial komprehensif tentang penggunaan Trezor Hardware Wallet dengan passphrase BIP39 untuk meningkatkan keamanan Anda:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda mau memberikan jempol Green di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial Anda. Terima kasih banyak!