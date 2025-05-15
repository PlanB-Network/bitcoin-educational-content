---
name: Trezor Model Satu
description: Menyiapkan dan menggunakan Hardware Wallet Model One
---
![cover](assets/cover.webp)



*Kredit gambar: [Trezor.io](https://trezor.io/)*



Trezor Model One adalah Hardware Wallet pertama yang pernah dirilis, diluncurkan pada tahun 2014 oleh SatoshiLabs. Setelah lebih dari sepuluh tahun berdiri, ini tetap menjadi pilihan yang menarik, terutama bagi pengguna yang mencari Hardware Wallet yang dapat diakses baik secara teknis maupun dalam hal anggaran. Bahkan, harganya hanya €49 di situs web resmi Trezor. Ini adalah satu-satunya dompet perangkat keras dalam kisaran harga ini. Harga ini berada di tengah-tengah antara perangkat entry-level dengan harga sekitar €20, seperti Tapsigner, yang sering kali tidak memiliki layar, dan perangkat kelas menengah dengan harga sekitar €80, seperti Ledger Nano S Plus atau Trezor Safe 3.



Model One memiliki layar OLED monokrom 0,96 inci dan dua tombol fisik. Kamera ini beroperasi tanpa baterai, hanya menggunakan koneksi micro-USB untuk daya dan data Exchange.



![Image](assets/fr/01.webp)



Kelemahan utama dari Model One adalah kurangnya Secure Element, yang membuatnya rentan terhadap berbagai serangan fisik, beberapa di antaranya relatif mudah dieksekusi. Serangan ini dapat mencakup analisis saluran tambahan untuk menentukan PIN perangkat, atau teknik yang lebih canggih untuk mengekstrak seed yang terenkripsi untuk melakukan brute-force nantinya. Perhatikan bahwa serangan ini membutuhkan akses fisik ke perangkat. Namun, kerentanan ini dapat dikurangi secara signifikan dengan menggunakan passphrase BIP39 yang solid. Jika Anda memilih Hardware Wallet ini, saya sangat menyarankan Anda untuk mengkonfigurasi passphrase.



Model One menawarkan dua keuntungan penting:




- Hal ini didasarkan pada arsitektur yang sepenuhnya sumber terbuka. Tidak seperti model yang lebih baru dengan Secure Element, semua komponen perangkat keras dan perangkat lunak Model One dapat diaudit;
- Kamera ini dilengkapi dengan layar. Sepengetahuan saya, ini adalah satu-satunya Hardware Wallet yang ada di pasaran dalam kisaran harga ini yang dilengkapi layar. Ini adalah fitur yang sangat penting, karena memungkinkan informasi yang ditandatangani dan alamat penerimaan diverifikasi, sehingga mencegah banyak serangan digital.



Oleh karena itu, Trezor Model One dapat menjadi pilihan yang bijaksana bagi pengguna pemula dan menengah dengan anggaran terbatas. Namun demikian, penting untuk tetap menyadari keterbatasannya dalam hal perlindungan fisik, karena tidak adanya Secure Element. Jika anggaran Anda terbatas, ini merupakan pilihan yang bagus, tetapi jika Anda mampu memilih model yang lebih unggul, seperti Trezor Safe 3 dengan harga €79, itu lebih baik, karena sudah dilengkapi dengan Secure Element.



## Membuka Kotak Trezor Model One



Ketika Anda menerima Model One, pastikan kotak dan Seal dalam keadaan utuh untuk mengonfirmasi bahwa paket tersebut belum dibuka. Verifikasi perangkat lunak atas keaslian dan integritas perangkat juga akan dilakukan ketika perangkat ini diatur nanti.



Isi kotak termasuk:




- Trezor Model One;
- Stok kartu untuk mencatat frasa, stiker, dan instruksi Mnemonic Anda;
- Kabel USB-A ke micro-USB.



![Image](assets/fr/02.webp)



Menavigasi perangkat ini sangat sederhana:




- Klik kanan untuk mengonfirmasi dan melanjutkan ke langkah berikutnya;
- Gunakan tombol kiri untuk kembali.



## Prasyarat



Untuk tutorial ini, saya akan menunjukkan kepada Anda bagaimana cara menggunakan Trezor Model One dengan [perangkat lunak manajemen portofolio Sparrow Wallet] (https://sparrowwallet.com/download/). Jika Anda belum menginstal perangkat lunak ini, silakan lakukan sekarang. Jika Anda memerlukan bantuan, kami juga memiliki tutorial terperinci tentang konfigurasi Sparrow Wallet:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Anda juga memerlukan perangkat lunak Trezor Suite untuk mengonfigurasi Model One, memeriksa keasliannya, dan menginstal firmware. Kami hanya akan menggunakan perangkat lunak ini untuk itu, dan setelah itu hanya diperlukan untuk pembaruan firmware. Untuk pengelolaan Wallet sehari-hari, kami akan menggunakan Sparrow Wallet secara eksklusif, karena dioptimalkan untuk Bitcoin dan mudah digunakan, bahkan untuk pemula (Sparrow hanya mendukung Bitcoin, bukan altcoin).



[Unduh Trezor Suite dari situs web resmi](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



Untuk kedua program ini, saya sangat menyarankan agar Anda memeriksa keasliannya (dengan GnuPG) dan integritasnya (melalui Hash) sebelum menginstalnya di komputer Anda. Jika Anda tidak tahu cara melakukannya, Anda dapat mengikuti tutorial lain ini:



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Memulai Trezor Model One



Hubungkan Model One Anda ke komputer yang sudah terinstal Trezor Suite dan Sparrow Wallet.



![Image](assets/fr/04.webp)



Buka Trezor Suite, lalu klik "*Setup my Trezor*".



![Image](assets/fr/05.webp)



Pilih "*Firmware khusus Bitcoin*", lalu klik "*Instal Bitcoin saja*".



![Image](assets/fr/06.webp)



Trezor Suite kemudian akan menginstal firmware pada Model One Anda. Harap tunggu selama proses instalasi.



![Image](assets/fr/07.webp)



Klik "*Lanjutkan*".



![Image](assets/fr/08.webp)



## Menciptakan portofolio Bitcoin



Pada Trezor Suite, klik tombol "*Buat Wallet baru*".



![Image](assets/fr/09.webp)



Menerima persyaratan penggunaan pada Hardware Wallet.



![Image](assets/fr/10.webp)



Di Trezor Suite, klik "*Lanjutkan pencadangan*".



![Image](assets/fr/11.webp)



Perangkat lunak ini memberikan petunjuk tentang cara mengelola frasa Mnemonic Anda.



Mnemonic ini memberikan Anda akses penuh dan tidak terbatas ke semua bitcoin Anda. Siapa pun yang memiliki frasa ini dapat mencuri dana Anda, bahkan tanpa akses fisik ke Trezor Model One Anda.



Frasa 24 kata ini mengembalikan akses ke bitcoin Anda jika terjadi kehilangan, pencurian, atau kerusakan pada Hardware Wallet Anda. Oleh karena itu, sangat penting untuk menyimpannya dengan hati-hati dan menyimpannya di tempat yang aman.



Anda bisa menuliskannya pada karton yang disertakan dalam kotak, atau untuk keamanan tambahan, saya sarankan untuk mengukirnya pada dasar baja tahan karat untuk melindunginya dari kebakaran, banjir atau keruntuhan.



Konfirmasikan instruksi, lalu klik tombol "*Buat cadangan Wallet*".



![Image](assets/fr/12.webp)



Model One akan membuat frasa Mnemonic Anda menggunakan generator nomor acak. Pastikan Anda tidak diawasi selama operasi ini. Tuliskan kata-kata yang disediakan di layar pada media fisik pilihan Anda. Tergantung pada strategi keamanan Anda, Anda dapat mempertimbangkan untuk membuat beberapa salinan fisik lengkap dari frasa tersebut (tetapi yang terpenting, jangan membaginya). Sangat penting untuk membuat kata-kata tersebut bernomor dan berurutan.



***Tentu saja, Anda tidak boleh membagikan kata-kata ini di Internet, seperti yang saya lakukan dalam tutorial ini. Contoh Wallet ini hanya akan digunakan pada Testnet dan akan dihapus pada akhir tutorial



Untuk informasi lebih lanjut mengenai cara yang tepat untuk menyimpan dan mengelola frasa Mnemonic Anda, saya sangat merekomendasikan untuk mengikuti tutorial lainnya, khususnya jika Anda seorang pemula:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Untuk beralih ke kata-kata berikutnya, klik kanan. Setelah Anda menuliskan semua kata, klik tombol kanan lagi untuk melanjutkan ke langkah berikutnya.



![Image](assets/fr/13.webp)



Hardware Wallet Anda sekali lagi menunjukkan semua kata-kata Anda. Pastikan Anda telah menuliskan semuanya.



![Image](assets/fr/14.webp)



## Mengatur kode PIN



Berikutnya adalah langkah kode PIN. Kode PIN akan membuka kunci Trezor anda. Oleh karena itu, kode ini memberikan perlindungan terhadap akses fisik yang tidak sah. Kode PIN ini tidak terlibat dalam penurunan kunci kriptografi Wallet anda. Jadi, bahkan tanpa akses ke kode PIN, kepemilikan frasa Mnemonic 12 kata Anda akan memungkinkan Anda untuk mendapatkan kembali akses ke bitcoin Anda.



Pada Trezor Suite, klik "*Lanjutkan ke PIN*", lalu pada tombol "*Setel PIN*".



![Image](assets/fr/15.webp)



Konfirmasikan pada Model Satu.



![Image](assets/fr/16.webp)



Kami menyarankan untuk memilih kode PIN yang seacak mungkin. Pastikan untuk menyimpan kode ini di lokasi yang terpisah dari tempat penyimpanan Trezor anda (contoh: di dalam pengelola kata sandi). Anda dapat menentukan kode PIN antara 8 hingga 50 digit. Saya sarankan anda untuk memilih kode PIN sepanjang mungkin untuk meningkatkan keamanan.



Kode PIN harus dimasukkan ke dalam Trezor Suite di komputer anda dengan mengklik titik-titik yang sesuai dengan angka-angka tersebut, sesuai dengan konfigurasi keyboard yang ditampilkan pada Trezor Model One.



Metode entri PIN khusus ini diperlukan setiap kali Anda membuka kunci Trezor Model One, baik melalui Trezor Suite atau Sparrow Wallet.



![Image](assets/fr/17.webp)



Setelah selesai, klik tombol "*Masukkan PIN*".



![Image](assets/fr/18.webp)



Tuliskan kembali PIN Anda untuk mengonfirmasi.



![Image](assets/fr/19.webp)



Pada Trezor Suite, klik tombol "*Selesaikan pengaturan*".



![Image](assets/fr/20.webp)



Konfigurasi Model One Anda sekarang sudah selesai. Jika mau, Anda dapat mengubah nama dan halaman beranda Hardware Wallet.



![Image](assets/fr/21.webp)



Kita tidak akan membutuhkan perangkat lunak Trezor Suite lagi, kecuali untuk melakukan pembaruan firmware secara berkala pada Hardware Wallet Anda, atau jika Anda ingin menjalankan tes pemulihan. Kita sekarang akan menggunakan Sparrow untuk mengelola portofolio, karena perangkat lunak ini sangat cocok untuk penggunaan Bitcoin saja.



## Menyiapkan portofolio pada Sparrow Wallet



Mulailah dengan mengunduh dan menginstal Sparrow Wallet [dari situs web resmi] (https://sparrowwallet.com/) di komputer Anda, jika Anda belum melakukannya.



Setelah Anda membuka Sparrow Wallet, pastikan perangkat lunak ini terhubung ke node Bitcoin, yang ditandai dengan tanda centang di sudut kanan bawah Interface. Jika Anda mengalami masalah dalam menghubungkan Sparrow, saya sarankan Anda untuk membaca bagian awal tutorial ini:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klik pada tab "*File*", kemudian pada "*New Wallet*".



![Image](assets/fr/22.webp)



Beri nama portofolio Anda, lalu klik "*Buat Wallet*".



![Image](assets/fr/23.webp)



Pada menu drop-down "*Jenis Skrip*", pilih jenis skrip yang akan digunakan untuk mengamankan bitcoin Anda. Saya merekomendasikan "*Taproot*", atau jika tidak, "*Native SegWit*".



![Image](assets/fr/24.webp)



Klik pada tombol "*Terhubung Hardware Wallet*". Model One Anda tentu saja harus terhubung ke komputer.



![Image](assets/fr/25.webp)



Klik pada tombol "*Pindai*". Model One Anda akan muncul.



Ketika Anda menghubungkan Model One ke komputer dengan Sparrow Wallet terbuka, Anda kemudian akan diminta untuk memasukkan passphrase BIP39 pada Sparrow. Opsi lanjutan ini akan dibahas dalam tutorial mendatang. Untuk saat ini, Anda cukup memilih "*Toggle passphrase Off*" untuk mencegah Trezor Anda meminta Anda memasukkan passphrase setiap kali Anda memulai.



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)



Klik "*Import Keystore*".



![Image](assets/fr/27.webp)



Anda sekarang dapat melihat detail Wallet Anda, termasuk kunci publik yang diperpanjang dari akun pertama Anda. Klik pada tombol "*Apply*" untuk menyelesaikan pembuatan Wallet.



![Image](assets/fr/28.webp)



Pilih kata sandi yang kuat untuk mengamankan akses ke Sparrow Wallet. Kata sandi ini akan memastikan akses yang aman ke data Sparrow Wallet Anda, melindungi kunci publik, alamat, label, dan riwayat transaksi Anda dari akses yang tidak sah.



Saya menyarankan Anda untuk menyimpan kata sandi ini dalam sebuah pengelola kata sandi agar Anda tidak lupa.



![Image](assets/fr/29.webp)



Dan sekarang, portofolio Anda sudah diimpor ke dalam Sparrow Wallet!



![Image](assets/fr/30.webp)



Sebelum Anda menerima bitcoin pertama Anda di dalam Wallet, **Saya sangat menyarankan Anda untuk melakukan tes pemulihan kosong**. Tuliskan beberapa informasi referensi, seperti xpub Anda, kemudian setel ulang Trezor Model One Anda ketika Wallet masih kosong. Kemudian cobalah untuk memulihkan Wallet anda pada Trezor menggunakan cadangan kertas anda. Periksa apakah xpub yang dihasilkan setelah pemulihan sesuai dengan yang Anda tulis sebelumnya. Jika sesuai, Anda dapat yakin bahwa cadangan kertas Anda dapat diandalkan.



Untuk mempelajari lebih lanjut tentang cara melakukan tes pemulihan, saya sarankan Anda membaca tutorial lain ini:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Bagaimana cara menerima bitcoin dengan Trezor Model One?



Pada Sparrow, klik tab "*Receive*".



![Image](assets/fr/31.webp)



Sebelum menggunakan Address yang diusulkan oleh Sparrow Wallet, periksa di layar Trezor Anda. Praktik ini memungkinkan Anda untuk mengonfirmasi bahwa Address yang ditampilkan di Sparrow tidak palsu, dan bahwa Hardware Wallet memang menyimpan private key yang diperlukan untuk membelanjakan bitcoin yang diamankan dengan Address ini. Hal ini membantu Anda untuk menghindari beberapa jenis serangan.



Untuk melakukan pemeriksaan ini, klik tombol "*Display Address*".



![Image](assets/fr/32.webp)



Periksa apakah Address yang ditampilkan di Trezor Anda cocok dengan yang ada di Sparrow Wallet. Sebaiknya Anda juga melakukan pemeriksaan ini sebelum mengirimkan Address Anda ke pengirim, untuk memastikan keabsahannya. Anda dapat menekan tombol kanan untuk mengonfirmasi.



![Image](assets/fr/33.webp)



Anda juga dapat menambahkan "*Label*" untuk mendeskripsikan sumber bitcoin yang akan diamankan dengan Address ini. Ini adalah praktik yang baik yang memungkinkan Anda untuk mengelola UTXO dengan lebih baik.



![Image](assets/fr/34.webp)



Anda kemudian dapat menggunakan Address ini untuk menerima bitcoin.



![Image](assets/fr/35.webp)



## Bagaimana cara mengirim bitcoin dengan Trezor Model One?



Sekarang setelah Anda menerima Satss pertama Anda di Model One-secured Wallet, Anda dapat membelanjakannya juga! Hubungkan Trezor Anda ke komputer, luncurkan Sparrow Wallet, lalu buka tab "*Kirim*" untuk membuat transaksi baru.



![Image](assets/fr/36.webp)



Jika Anda ingin *Coin Control*, yaitu memilih secara spesifik UTXO mana yang akan digunakan dalam transaksi, buka tab "*UTXOs*". Pilih UTXO yang ingin Anda gunakan, lalu klik "*Kirim Terpilih*". Anda akan diarahkan ke layar yang sama pada tab "*Kirim*", tetapi dengan UTXO yang sudah dipilih untuk transaksi.



![Image](assets/fr/37.webp)



Masukkan alamat tujuan Address. Anda juga dapat memasukkan beberapa alamat dengan mengeklik tombol "*+ Tambah*".



![Image](assets/fr/38.webp)



Tuliskan "*Label*" untuk mengingat tujuan pengeluaran ini.



![Image](assets/fr/39.webp)



Pilih jumlah yang akan dikirim ke Address ini.



![Image](assets/fr/40.webp)



Sesuaikan tarif biaya transaksi Anda sesuai dengan pasar saat ini. Sebagai contoh, Anda dapat menggunakan [Mempool.space] (https://Mempool.space/) untuk memilih tarif biaya yang sesuai.



Pastikan semua parameter transaksi Anda sudah benar, lalu klik "*Buat Transaksi*".



![Image](assets/fr/41.webp)



Jika semuanya sudah sesuai dengan keinginan Anda, klik "*Finalisasi Transaksi untuk Penandatanganan*".



![Image](assets/fr/42.webp)



Klik "*Tanda Tangan*".



![Image](assets/fr/43.webp)



Klik "*Sign*" di samping Trezor Model One Anda.



![Image](assets/fr/44.webp)



Periksa parameter transaksi di layar Hardware Wallet Anda, termasuk penerima yang menerima Address, jumlah yang dikirim, dan biaya. Setelah transaksi diverifikasi di Trezor, klik kanan untuk menandatanganinya.



![Image](assets/fr/45.webp)



Transaksi Anda sekarang sudah ditandatangani. Periksa untuk terakhir kalinya apakah semuanya baik-baik saja, lalu klik "*Broadcast Transaction*" untuk menyiarkannya di jaringan Bitcoin.



![Image](assets/fr/46.webp)



Anda bisa menemukannya di tab "*Transactions*" pada Sparrow Wallet.



![Image](assets/fr/47.webp)



Selamat, Anda sekarang sudah menguasai penggunaan dasar Trezor Model One dengan Sparrow Wallet! Untuk melangkah lebih jauh, saya merekomendasikan tutorial komprehensif tentang penggunaan Trezor Hardware Wallet dengan passphrase BIP39 untuk memperkuat keamanan Anda:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Jika Anda merasa tutorial ini bermanfaat, saya akan sangat berterima kasih jika Anda mau memberikan jempol Green di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial Anda. Terima kasih banyak!