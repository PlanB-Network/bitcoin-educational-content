---
name: Trezor Safe 5
description: Mengkonfigurasi dan menggunakan Hardware Wallet Safe 5
---
![cover](assets/cover.webp)



*Kredit gambar: [Trezor.io](https://trezor.io/)*

Trezor Safe 5 adalah Hardware Wallet generasi terbaru yang dirancang oleh SatoshiLabs dan diluncurkan pada tahun 2024. Wallet ini diposisikan sebagai versi high-end dari Safe 3, dengan fokus pada kenyamanan penggunaan dan daya tahan. Safe 5 memanfaatkan kemajuan keamanan yang sama seperti pendahulunya, Safe 3, dibandingkan dengan Model One dan Model T.

Dengan harga €169, Safe 5 masuk ke kategori Hardware Wallet kelas atas, bersaing dengan model seperti Coldcard, Ledger Nano X dan Flex, Jade Plus, Passport, serta BitBox.

Safe 5 dilengkapi layar sentuh berwarna berukuran 1,54 inci yang dilindungi Gorilla Glass 3, tahan terhadap guncangan dan goresan. Wallet ini juga memiliki mesin haptic Trezor Touch yang memberikan getaran halus setiap kali disentuh. Seperti Safe 3, Safe 5 menggunakan Secure Element dan beroperasi melalui koneksi USB-C, dengan tambahan slot Micro SD.

Perbedaan utama antara Safe 3 dan Safe 5 terletak pada kualitas perangkat, bukan pada aspek keamanan. Safe 5 secara signifikan meningkatkan pengalaman pengguna dengan pengoperasian yang lebih mulus dan layar yang lebih nyaman. Dari sisi keamanan, keduanya setara.

![Image](assets/fr/01.webp)

Safe 5 punya semua fitur penting yang kamu harapkan dari sebuah Hardware Wallet yang bagus, termasuk integrasi yang sangat baik untuk passphrase BIP39. Namun, saat ini belum mendukung Miniscript.

Model ini cocok banget untuk pengguna pemula dan menengah. Di sisi lain, mungkin belum memenuhi semua harapan pengguna tingkat lanjut yang mencari fitur lebih spesifik seperti yang ada di perangkat Coldcard. Tapi kalau kamu nggak butuh opsi tingkat lanjut itu, Trezor Safe 5 bisa jadi pilihan yang pas.

## Model keamanan Trezor Safe 5

Seperti halnya Safe 3, Trezor Safe 5 dilengkapi dengan Secure Element bersertifikasi EAL6+, sebuah peningkatan besar dibandingkan model sebelumnya seperti Model One dan Model T. Chip yang digunakan adalah OPTIGA Trust M V3. Chip ini tidak menyimpan seed secara langsung, tapi berfungsi sebagai komponen kriptografi yang mengamankan akses ke seed. Secure Element menyimpan rahasia yang hanya bisa diakses setelah pengguna memasukkan PIN dengan benar. Rahasia ini kemudian digunakan untuk mendekripsi seed, yang disimpan dalam bentuk terenkripsi di memori utama perangkat.

Sistem keamanan hibrida ini memberikan perlindungan fisik yang jauh lebih kuat, terutama terhadap serangan ekstraksi atau analisis invasif — masalah yang cukup rentan terjadi pada Model One, khususnya dalam manajemen PIN. Kerentanan tersebut kini bisa diatasi berkat penggunaan Secure Element. Model ini juga tetap mempertahankan arsitektur perangkat lunak sumber terbuka: kode yang mengatur pembuatan dan penggunaan kunci privat tetap dapat diakses dan diverifikasi sepenuhnya. Chip OPTIGA hanya mengelola kode PIN, jadi tidak terlibat dalam manajemen kunci Bitcoin Wallet. Fungsinya terbatas pada melepaskan rahasia yang digunakan untuk mendekripsi seed. Selain itu, chip OPTIGA Trust M V3 memiliki lisensi yang cukup bebas, yang memungkinkan SatoshiLabs untuk secara terbuka mempublikasikan potensi kerentanannya (tanpa terikat NDA).

Model keamanan ini, menurutku, adalah salah satu kompromi terbaik yang ada di pasaran saat ini. Ia menggabungkan keunggulan Secure Element dengan transparansi perangkat lunak sumber terbuka. Dulu, pengguna harus memilih antara keamanan fisik yang kuat lewat chip atau transparansi open source. Sekarang, dengan Trezor Safe 5, kamu bisa mendapatkan keduanya.

Dalam tutorial ini, kamu akan belajar cara mengatur dan menggunakan Trezor Safe 5 dengan aman.
## Membongkar Kotak Brankas Trezor Safe 5

Ketika kamu menerima Safe 5, pastikan kotak dan Seal dalam keadaan utuh untuk mengonfirmasi bahwa paket tersebut belum dibuka. Pemeriksaan perangkat lunak terhadap keaslian dan integritas perangkat juga akan dilakukan saat perangkat ini dipasang nanti.

Isi kotak termasuk:

- Trezor Safe 5;
- Kantung yang berisi stok kartu untuk mencatat frasa, stiker, dan instruksi Mnemonic Anda;
- Kabel USB-C ke USB-C.

Ketika dibuka, Trezor Safe 5 harus dilindungi oleh plastik pelindung dan port USB-C harus diamankan dengan Seal hologram. Pastikan itu ada di sana.

![Image](assets/fr/02.webp)

Navigasi pada perangkat ini cukup intuitif:

- Sentuh bagian bawah layar untuk bergerak maju;
- Geser ke bawah untuk kembali ;
- Tekan dan tahan layar untuk mengonfirmasi operasi.

## Prasyarat

Untuk tutorial ini, aku akan menunjukkan bagaimana cara menggunakan Trezor Safe 5 dengan [perangkat lunak manajemen portofolio Sparrow Wallet] (https://sparrowwallet.com/download/). Kalau kamu belum menginstal perangkat lunak ini, silakan lakukan sekarang. Kalau kamu membutuhkan bantuan, kami juga memiliki tutorial terperinci tentang cara mengonfigurasi Sparrow Wallet:

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Kamu juga memerlukan perangkat lunak Trezor Suite untuk mengonfigurasi Safe 5, memeriksa keasliannya, dan menginstal firmware. Kita cuma akan menggunakan aplikasi ini untuk keperluan itu saja, dan setelah selesai, Trezor Suite hanya dibutuhkan saat ada pembaruan firmware.

Untuk pengelolaan Wallet sehari-hari, kita akan menggunakan Sparrow Wallet secara eksklusif, karena aplikasi ini dioptimalkan khusus untuk Bitcoin dan sangat mudah digunakan, bahkan untuk pemula. (Sparrow hanya mendukung Bitcoin, bukan altcoin.)

[Unduh Trezor Suite dari situs web resmi](https://trezor.io/trezor-suite)

![Image](assets/fr/03.webp)

Untuk kedua program ini, aku sangat menyarankan kamu memeriksa keasliannya (dengan GnuPG) dan integritasnya (melalui hash) sebelum menginstalnya di komputermu. Kalau kamu belum tahu cara melakukannya, kamu bisa mengikuti tutorial lain berikut ini:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Memulai Trezor Safe 5

Hubungkan Safe 5 ke komputer yang sudah terinstal Trezor Suite dan Sparrow Wallet.

![Image](assets/fr/04.webp)

Buka Trezor Suite, lalu klik "*Setup my Trezor*".

![Image](assets/fr/05.webp)

Pilih "*Firmware khusus Bitcoin*", lalu klik "*Instal Bitcoin saja*".

![Image](assets/fr/06.webp)

Trezor Suite kemudian akan menginstal firmware pada Brankas 5. Mohon tunggu selama proses instalasi.

![Image](assets/fr/07.webp)

Klik "*Lanjutkan*".

![Image](assets/fr/08.webp)

Kemudian lanjutkan ke uji keaslian untuk memastikan Hardware Wallet tidak palsu atau disusupi.

![Image](assets/fr/09.webp)

Pada Safe 5, tekan layar untuk mengonfirmasi.

![Image](assets/fr/10.webp)

Jika Trezor asli, pesan konfirmasi akan muncul di Trezor Suite.

![Image](assets/fr/11.webp)

Kemudian kamu dapat melewati jendela dengan petunjuk pengoperasian dasar.

![Image](assets/fr/12.webp)

## Menciptakan portofolio Bitcoin

Pada Trezor Suite, klik tombol "*Buat Wallet baru*".

![Image](assets/fr/13.webp)

Untuk membuat Wallet standar berbasis BIP39, mulailah dengan memilih "Jenis cadangan Wallet warisan" dari menu tarik-turun, lalu pilih frasa Mnemonic 12 atau 24 kata (saat ini disarankan 12 kata). Ini akan membuat kamu bisa membuat Wallet dengan satu tanda tangan klasik. Aku menyarankan kamu memilih parameter yang sesuai dengan BIP39 di tahap ini, supaya proses pemulihan lebih mudah dan tidak terikat pada batasan di lingkungan tertentu. Untuk menyelesaikannya, klik "Buat Wallet".

Kalau kamu ingin tahu lebih banyak tentang opsi pencadangan lain yang tersedia di Trezor, termasuk Cadangan Multi-Bagi, aku sarankan kamu juga membaca tutorial berikut ini:

https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e


![Image](assets/fr/14.webp)

Terima persyaratan penggunaan pada Hardware Wallet.

![Image](assets/fr/15.webp)

Tekan dan tahan layar untuk membuat portofolio baru.

![Image](assets/fr/16.webp)

Di Trezor Suite, klik "*Lanjutkan pencadangan*".

![Image](assets/fr/17.webp)

Perangkat lunak ini akan memberi petunjuk tentang cara mengelola frasa Mnemonic kamu.

Frasa Mnemonic ini memberi kamu akses penuh dan tak terbatas ke semua bitcoin yang kamu miliki. Siapa pun yang memiliki frasa ini bisa mencuri dana kamu, bahkan tanpa memegang Trezor Safe 5 milikmu secara fisik.

Frasa 12 kata ini memungkinkan kamu memulihkan akses ke bitcoin jika Hardware Wallet kamu hilang, dicuri, atau rusak. Karena itu, sangat penting untuk menyimpannya dengan hati-hati di tempat yang benar-benar aman.

Kamu bisa menuliskannya di karton yang sudah disertakan dalam kotak. Tapi untuk keamanan tambahan, aku menyarankan kamu mengukirnya di pelat baja tahan karat agar tetap terlindungi dari kebakaran, banjir, atau keruntuhan.

Konfirmasikan petunjuknya, kemudian klik tombol "*Buat cadangan Wallet*".

![Image](assets/fr/18.webp)

Safe 5 akan membuat frasa Mnemonic kamu menggunakan generator angka acak. Pastikan tidak ada siapa pun yang mengawasi selama proses ini berlangsung. Tuliskan kata-kata yang muncul di layar ke media fisik pilihanmu. Tergantung pada strategi keamanan yang kamu gunakan, kamu bisa mempertimbangkan untuk membuat beberapa salinan fisik lengkap dari frasa tersebut (tapi yang paling penting, jangan pernah membaginya). Pastikan juga setiap kata diberi nomor dan ditulis berurutan.

***Tentu saja, kamu tidak boleh membagikan kata-kata ini di Internet seperti yang aku lakukan di tutorial ini. Contoh Wallet ini hanya digunakan di Testnet dan akan dihapus setelah tutorial selesai.***

Untuk informasi lebih lanjut tentang cara terbaik menyimpan dan mengelola frasa Mnemonic kamu, aku sangat menyarankan untuk mengikuti tutorial lain ini, terutama kalau kamu masih pemula:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/19.webp)

Untuk beralih ke kata berikutnya, ketuk bagian bawah layar. Kamu bisa kembali ke kata sebelumnya dengan menggeser ke bawah. Setelah semua kata selesai kamu tulis, tahan jarimu di layar untuk lanjut ke langkah berikutnya.

![Image](assets/fr/20.webp)

Pilih kata-kata dalam frasa Mnemonic kamu sesuai urutannya untuk memastikan kalau kamu sudah menuliskannya dengan benar.

![Image](assets/fr/21.webp)

Setelah prosedur verifikasi ini selesai, klik pada layar untuk melanjutkan.

![Image](assets/fr/22.webp)

## Mengatur kode PIN

Berikutnya adalah langkah kode PIN. Kode PIN akan membuka kunci Trezor kamu. Oleh karena itu, kode ini memberikan perlindungan terhadap akses fisik yang tidak sah. Kode PIN ini tidak terlibat dalam penurunan kunci kriptografi wallet kamu. Jadi, bahkan tanpa akses ke kode PIN, kepemilikan frasa Mnemonic 12 kata kamu akan memungkinkan kamu mendapatkan kembali akses ke bitcoin kamu.

Pada Trezor Suite, klik "*Lanjutkan ke PIN*", lalu pada tombol "*Setel PIN*".

![Image](assets/fr/23.webp)

Konfirmasikan dengan Safe 5.

![Image](assets/fr/24.webp)

Kami menyarankan kamu memilih kode PIN yang benar-benar acak. Pastikan untuk menyimpannya di tempat yang terpisah dari lokasi penyimpanan Trezor kamu, misalnya di dalam pengelola kata sandi. Kamu bisa membuat kode PIN antara 8 hingga 50 digit. Aku menyarankan kamu memilih PIN yang cukup panjang supaya keamanannya lebih kuat.

Gunakan panel sentuh untuk memasukkan PIN kamu.

![Image](assets/fr/25.webp)

Setelah selesai, klik tanda centang Green di kanan bawah, lalu konfirmasikan PIN untuk kedua kalinya.

![Image](assets/fr/26.webp)

Kode PIN telah terdaftar.

![Image](assets/fr/27.webp)

Pada Trezor Suite, klik tombol "*Selesaikan pengaturan*".

![Image](assets/fr/28.webp)

Pengaturan Safe 5 sekarang sudah selesai. Jika mau, kamu dapat mengubah nama dan halaman beranda Hardware Wallet.

![Image](assets/fr/29.webp)

Kita tidak akan membutuhkan perangkat lunak Trezor Suite lagi, kecuali saat ingin memperbarui firmware Hardware Wallet secara berkala atau menjalankan tes pemulihan. Sekarang, kita akan menggunakan Sparrow untuk mengelola portofolio, karena perangkat lunak ini memang paling cocok untuk penggunaan Bitcoin saja.

## Menyiapkan portofolio pada Sparrow Wallet

Mulailah dengan mengunduh dan menginstal Sparrow Wallet [dari situs web resmi] (https://sparrowwallet.com/) di komputer, Kalau kamu belum melakukannya.

Setelah kamu membuka Sparrow Wallet, pastikan perangkat lunak ini sudah terhubung ke node Bitcoin, yang ditandai dengan ikon centang di pojok kanan bawah antarmuka. Kalau kamu mengalami masalah saat menghubungkan Sparrow, aku sarankan kamu membaca kembali bagian awal tutorial ini:

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klik pada tab "*File*", kemudian pada "*New Wallet*".

![Image](assets/fr/30.webp)

Beri nama portofolio, lalu klik "*Buat Wallet*".

![Image](assets/fr/31.webp)

Pada menu drop-down "*Jenis Skrip*", pilih jenis skrip yang akan digunakan untuk mengamankan bitcoin. Aku merekomendasikan "*Taproot*", atau jika tidak, "*Native SegWit*".

![Image](assets/fr/32.webp)

Klik pada tombol "*Terhubung Hardware Wallet*". Brankas Anda tentu saja harus terhubung ke komputer dan tidak terkunci.

Saat kamu menghubungkan Safe 5 ke komputer dengan Sparrow Wallet yang sudah terbuka, kamu akan diminta untuk memasukkan passphrase BIP39 di layar Hardware Wallet. Opsi lanjutan ini akan dibahas di tutorial berikutnya. Untuk sekarang, cukup ketuk tanda centang hijau di pojok kanan atas untuk mengonfirmasi bahwa kamu ingin menggunakan passphrase kosong (tanpa passphrase). Agar Trezor kamu tidak terus-menerus meminta passphrase setiap kali dinyalakan, buka Trezor Suite lalu masuk ke menu pengaturan, dan ubah opsi di "*Device*" > "*Default Wallet*" menjadi "*Standard*", bukan "*passphrase*".

![Image](assets/fr/33.webp)

Klik pada tombol "*Pindai*". Brankas 5 Anda akan muncul. Klik "*Import Keystore*".

![Image](assets/fr/34.webp)

Sekarang kamu dapat melihat detail Wallet, termasuk kunci publik yang diperpanjang dari akun pertama kamu. Klik pada tombol "*Apply*" untuk menyelesaikan pembuatan Wallet.

![Image](assets/fr/35.webp)

Pilih kata sandi yang kuat untuk mengamankan akses ke Sparrow Wallet kamu. Kata sandi ini akan memastikan akses yang aman ke data Sparrow Wallet, melindungi kunci publik, alamat, label, dan riwayat transaksi kamu dari akses yang tidak sah.
Aku menyarankan kamu menyimpan kata sandi ini di pengelola kata sandi supaya kamu nggak lupa.

![Image](assets/fr/36.webp)

Dan sekarang, portofolio Anda sudah diimpor ke dalam Sparrow Wallet!

![Image](assets/fr/37.webp)

Sebelum kamu menerima bitcoin pertama di Wallet kamu, **aku sangat menyarankan untuk melakukan tes pemulihan kosong.** Tuliskan beberapa informasi referensi, seperti xpub kamu, lalu setel ulang Trezor Safe 5 saat Wallet masih kosong. Setelah itu, coba pulihkan Wallet kamu di Trezor menggunakan cadangan kertas yang sudah kamu buat. Periksa apakah xpub yang dihasilkan setelah pemulihan sama dengan yang kamu catat sebelumnya. Kalau hasilnya sama, berarti cadangan kertas kamu bisa diandalkan.

Untuk mempelajari lebih lanjut tentang cara melakukan tes pemulihan, aku sarankan kamu membaca tutorial berikut ini:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Bagaimana cara menerima bitcoin dengan Trezor Safe 5?

Pada Sparrow, klik tab "*Receive*".

![Image](assets/fr/38.webp)

Sebelum menggunakan address yang ditampilkan oleh Sparrow Wallet, pastikan kamu memeriksanya di layar Trezor kamu. Langkah ini penting untuk memastikan bahwa address yang muncul di Sparrow bukan palsu, dan bahwa Hardware Wallet kamu benar-benar memiliki private key yang dibutuhkan untuk membelanjakan bitcoin yang diamankan dengan address tersebut. Dengan cara ini, kamu bisa terhindar dari berbagai jenis serangan.

Untuk melakukan pemeriksaan ini, klik tombol "*Tampilkan Address*".

![Image](assets/fr/39.webp)

Periksa apakah address yang ditampilkan di Trezor kamu sama dengan yang ada di Sparrow Wallet. Disarankan juga untuk melakukan pengecekan ini sebelum kamu mengirimkan address tersebut ke pengirim, supaya bisa memastikan keasliannya. Setelah cocok, kamu bisa menekan layar untuk mengonfirmasi.

![Image](assets/fr/40.webp)

Kamu dapat menambahkan "*Label*" untuk mendeskripsikan sumber bitcoin yang akan diamankan dengan Address ini. Ini adalah praktik yang baik yang memungkinkanmu untuk mengelola UTXO dengan lebih baik.

![Image](assets/fr/41.webp)

Kemudian kamu dapat menggunakan Address ini untuk menerima bitcoin.

![Image](assets/fr/42.webp)

## Bagaimana cara mengirim bitcoin dengan Trezor Safe 5?

Sekarang, setelah kamu menerima sats pertama di Wallet yang diamankan dengan Safe 5, kamu juga bisa membelanjakannya! Hubungkan Trezor kamu ke komputer, buka kuncinya dengan kode PIN, jalankan Sparrow Wallet, lalu buka tab "Kirim" untuk membuat transaksi baru.

![Image](assets/fr/43.webp)

Kalau kamu ingin menggunakan *Coin Control,* yaitu memilih secara spesifik UTXO mana yang akan dipakai dalam transaksi, buka tab "UTXOs". Pilih UTXO yang ingin kamu gunakan, lalu klik "Kirim Terpilih". Kamu akan diarahkan ke layar yang sama di tab "Kirim", tapi dengan UTXO yang sudah dipilih untuk transaksi tersebut.

![Image](assets/fr/44.webp)

Masukkan alamat tujuan Address. Kamu juga dapat memasukkan beberapa alamat dengan mengeklik tombol "*+ Tambah*".

![Image](assets/fr/45.webp)

Tuliskan "*Label*" untuk mengingat tujuan pengeluaran ini.

![Image](assets/fr/46.webp)

Pilih jumlah yang akan dikirim ke Address ini.

![Image](assets/fr/47.webp)

Sesuaikan tarif biaya transaksi sesuai dengan pasar saat ini. Sebagai contoh, kamu dapat menggunakan [Mempool.space] (https://Mempool.space/) untuk memilih tarif biaya yang sesuai.

Pastikan semua parameter transaksi sudah benar, lalu klik "*Buat Transaksi*".

![Image](assets/fr/48.webp)

Jika semuanya sudah sesuai dengan keinginan, klik "*Finalisasi Transaksi untuk Penandatanganan*".

![Image](assets/fr/49.webp)

Klik "*Tanda Tangan*".

![Image](assets/fr/50.webp)

Klik "*Tanda Tangan*" di sebelah Trezor Safe 5.

![Image](assets/fr/51.webp)

Periksa parameter transaksi pada layar Hardware Wallet kamu, termasuk penerima yang menerima Address, jumlah yang dikirim, dan biaya. Setelah transaksi diverifikasi di Trezor, tekan dan tahan layar untuk menandatanganinya.

![Image](assets/fr/52.webp)

Transaksi kamu sekarang sudah ditandatangani. Periksa sekali lagi untuk memastikan semuanya sudah benar, lalu klik *"Broadcast Transaction"* untuk menyiarkannya ke jaringan Bitcoin..

![Image](assets/fr/53.webp)

Kamu bisa menemukannya di tab "*Transactions*" pada Sparrow Wallet.

![Image](assets/fr/54.webp)

Selamat, kamu sekarang sudah menguasai penggunaan dasar Trezor Safe 5 dengan Sparrow Wallet! Untuk melangkah lebih jauh, aku merekomendasikan tutorial lengkap tentang cara menggunakan Trezor Hardware Wallet dengan passphrase BIP39 untuk meningkatkan keamanan kamu:

https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Kalau kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih jika kamu mau memberikan jempol Green di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial. Terima kasih banyak!
