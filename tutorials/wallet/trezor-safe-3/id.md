---
name: Trezor Safe 3
description: Mengkonfigurasi dan menggunakan Hardware Wallet Safe 3
---
![cover](assets/cover.webp)



*Kredit gambar: [Trezor.io](https://trezor.io/)*

Trezor Safe 3 adalah hardware wallet yang dibuat oleh SatoshiLabs dan diluncurkan pada tahun 2023. Wallet ini sangat ringkas dan ringan (14 gram), dirancang khusus untuk pengguna pemula hingga menengah. Safe 3 merupakan penerus dari Model One yang legendaris, dengan peningkatan besar namun tetap mempertahankan filosofi open-source khas Trezor yang membedakannya dari pesaing utamanya, Ledger. Safe 3 dijual dengan harga €79, sehingga berada di kelas menengah dan bersaing langsung dengan Ledger Nano S Plus.

Safe 3 tidak memiliki baterai dan hanya berfungsi melalui koneksi USB-C yang digunakan untuk daya sekaligus komunikasi data. Wallet ini dilengkapi dengan layar OLED monokrom berukuran 0,96 inci dan dua tombol fisik.

![Image](assets/fr/01.webp)

Safe 3 menawarkan semua fitur penting yang kamu harapkan dari sebuah hardware wallet yang solid, termasuk dukungan penuh untuk passphrase BIP39. Namun, perangkat ini belum mendukung Miniscript.

Model ini sangat cocok untuk pemula, dan bahkan bisa dibilang salah satu hardware wallet yang paling aku rekomendasikan untuk pengguna baru. Wallet ini juga cocok buat pengguna tingkat menengah. Tapi, mungkin belum cukup memenuhi kebutuhan pengguna tingkat lanjut yang mencari fitur lebih spesifik seperti yang ada di perangkat Coldcard. Meski begitu, kalau kamu nggak membutuhkan opsi tingkat lanjut tersebut, Trezor Safe 3 bisa jadi pilihan yang sangat bagus.


## Model keamanan Trezor Safe 3

Trezor Safe 3 kini dilengkapi dengan Secure Element bersertifikasi EAL6+, sebuah peningkatan besar dibanding model sebelumnya seperti Model One dan Model T. Chip yang digunakan adalah OPTIGA Trust M V3, yang tidak menyimpan seed secara langsung, melainkan berfungsi sebagai komponen kriptografi untuk mengamankan akses ke seed. Secure Element ini menyimpan rahasia yang hanya bisa diakses setelah pengguna memasukkan PIN dengan benar. Rahasia tersebut kemudian digunakan untuk mendekripsi seed yang disimpan secara terenkripsi di memori utama perangkat.

Sistem keamanan hibrida ini memberikan perlindungan fisik yang jauh lebih baik, terutama terhadap serangan ekstraksi atau analisis invasif — masalah yang cukup rentan pada Model One, khususnya dalam pengelolaan PIN. Kerentanan itu kini berhasil diatasi berkat penggunaan Secure Element. Model ini juga tetap mempertahankan arsitektur perangkat lunak open-source: kode yang mengelola pembuatan dan penggunaan private key tetap terbuka dan bisa diverifikasi sepenuhnya. Chip OPTIGA hanya menangani proses terkait PIN, bukan manajemen kunci Bitcoin Wallet. Chip ini hanya mengeluarkan rahasia yang digunakan untuk mendekripsi seed. Selain itu, OPTIGA Trust M V3 memiliki lisensi yang cukup bebas, sehingga memberi wewenang kepada SatoshiLabs untuk mempublikasikan potensi kerentanan secara transparan.

Model keamanan ini, menurutku, adalah salah satu kompromi terbaik yang ada di pasaran saat ini. Trezor Safe 3 berhasil menggabungkan keunggulan Secure Element dengan transparansi perangkat lunak open-source. Sebelumnya, pengguna harus memilih antara keamanan fisik ekstra dari chip tertutup atau transparansi kode terbuka. Sekarang, dengan Trezor Safe 3, kamu bisa mendapatkan keduanya sekaligus.

Dalam tutorial ini, aku akan menunjukkan cara mengatur dan menggunakan Trezor Safe 3 kamu dengan aman.


## Membongkar Kotak Brankas Trezor 3

Saat kamu menerima Safe 3, pastikan kotak dan segelnya masih utuh untuk memastikan paket belum pernah dibuka. Nanti, saat proses pemasangan, perangkat lunak juga akan memverifikasi keaslian dan integritas perangkat.

Isi kotaknya meliputi:

- Trezor Safe 3
- Kantung berisi kartu catatan seedphrase, stiker, dan panduan mnemonic
- Kabel USB-C ke USB-C

![Image](assets/fr/02.webp)

Saat dibuka, Trezor Safe 3 kamu akan dilindungi oleh plastik pelindung, dan port USB-C-nya harus tertutup dengan segel hologram. Pastikan segel itu benar-benar ada dan masih utuh.

![Image](assets/fr/03.webp)

Navigasi pada perangkat ini sangat mudah: gunakan tombol kanan untuk menggulir ke kanan, dan tombol kiri untuk menggulir ke kiri. Tekan kedua tombol secara bersamaan untuk mengonfirmasi tindakan.

![Image](assets/fr/04.webp)

## Prasyarat

Untuk tutorial ini, aku akan menunjukkanmu bagaimana cara menggunakan Trezor Safe 3 dengan [perangkat lunak manajemen portofolio Sparrow Wallet] (https://sparrowwallet.com/download/). Kalau kamu belum menginstal perangkat lunak ini, silakan lakukan sekarang. Kalau butuh bantuan, kamu juga bisa melihat tutorial lengkap kami tentang cara mengatur Sparrow Wallet:

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Kamu juga memerlukan perangkat lunak Trezor Suite untuk mengonfigurasi Safe 3, memeriksa keasliannya, dan menginstal firmware. Kita hanya akan menggunakan perangkat lunak ini untuk keperluan tersebut, dan setelah itu Trezor Suite hanya dibutuhkan saat ada pembaruan firmware. Untuk pengelolaan wallet sehari-hari, kita akan sepenuhnya menggunakan Sparrow Wallet, karena wallet ini dioptimalkan khusus untuk Bitcoin dan sangat mudah digunakan, bahkan untuk pemula (Sparrow hanya mendukung Bitcoin, bukan altcoin).

[Unduh Trezor Suite dari situs web resmi](https://trezor.io/trezor-suite)

![Image](assets/fr/05.webp)

Untuk kedua program ini, aku sangat menyarankan kamu memeriksa keasliannya (dengan GnuPG) dan integritasnya (menggunakan hash) sebelum menginstalnya di komputer kamu. Kalau kamu belum tahu cara melakukannya, kamu bisa mengikuti tutorial lain ini:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Memulai Trezor Safe 3

Sambungkan Safe 3 kamu ke komputer yang sudah terinstal Trezor Suite dan Sparrow Wallet.

![Image](assets/fr/06.webp)

Buka Trezor Suite, lalu klik "*Setup my Trezor*".

![Image](assets/fr/07.webp)

Pilih "*Firmware khusus Bitcoin*", lalu klik "*Instal Bitcoin saja*".

![Image](assets/fr/08.webp)

Trezor Suite kemudian akan menginstal firmware pada Safe 3 kamu. Tunggu saja sampai proses instalasi selesai.

![Image](assets/fr/09.webp)

Klik "*Lanjutkan*".

![Image](assets/fr/10.webp)

Kemudian lanjutkan ke uji keaslian untuk memastikan Hardware Wallet tidak palsu atau disusupi.

![Image](assets/fr/11.webp)

Pada Safe 3, tekan tombol kanan untuk mengonfirmasi.

![Image](assets/fr/12.webp)

Jika Trezor asli, pesan konfirmasi akan muncul di Trezor Suite.

![Image](assets/fr/13.webp)

Kamu kemudian dapat melewati jendela dengan petunjuk pengoperasian dasar.

![Image](assets/fr/14.webp)

## Menciptakan portofolio Bitcoin

Pada Trezor Suite, klik tombol "*Buat Wallet baru*".

![Image](assets/fr/15.webp)

Untuk portofolio standar, kamu bisa memilih opsi cadangan default. Ini akan membuat wallet dengan tanda tangan tunggal klasik menggunakan seedphrase sebanyak 12 kata. Klik "Buat Wallet".

Kalau kamu ingin tahu lebih banyak tentang opsi pencadangan lain yang tersedia di Trezor, termasuk Cadangan Multi-Bagi, aku sarankan kamu membaca tutorial berikut ini:

https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/16.webp)

Terima persyaratan penggunaan pada Hardware Wallet.

![Image](assets/fr/17.webp)

Tekan tombol kanan sekali lagi untuk membuat portofolio baru.

![Image](assets/fr/18.webp)

Di Trezor Suite, klik "*Lanjutkan pencadangan*".

![Image](assets/fr/19.webp)

Perangkat lunak ini akan memberi petunjuk tentang cara mengelola seedphrase kamu.

Seedphrase ini memberi kamu akses penuh dan tak terbatas ke semua bitcoin yang kamu miliki. Siapa pun yang mengetahui seedphrase ini bisa mencuri dana kamu, bahkan tanpa memegang Trezor Safe 3 kamu secara fisik.

Frasa 12 kata ini bisa memulihkan akses ke bitcoin kamu jika hardware wallet hilang, dicuri, atau rusak. Karena itu, sangat penting untuk menyimpannya dengan hati-hati di tempat yang benar-benar aman.

Kamu bisa menuliskannya di kartu yang disertakan dalam kotak, atau kalau ingin keamanan ekstra, aku sarankan untuk mengukirnya di lempengan baja tahan karat agar tetap aman dari kebakaran, banjir, atau keruntuhan.

Konfirmasikan petunjuknya, kemudian klik tombol "*Buat cadangan Wallet*".

![Image](assets/fr/20.webp)

Safe 3 akan membuat seedphrase kamu menggunakan generator angka acak. Pastikan tidak ada siapa pun yang mengawasi selama proses ini berlangsung. Tuliskan kata-kata yang muncul di layar ke media fisik pilihan kamu. Tergantung pada strategi keamananmu, kamu bisa mempertimbangkan untuk membuat beberapa salinan fisik lengkap dari seedphrase tersebut (tapi yang paling penting, jangan pernah membaginya). Pastikan setiap kata diberi nomor dan ditulis dalam urutan yang benar.

***Tentu saja, kamu tidak boleh membagikan kata-kata ini di Internet seperti yang aku lakukan di tutorial ini. Contoh wallet ini hanya digunakan di Testnet dan akan dihapus setelah tutorial selesai.***

Untuk informasi lebih lanjut tentang cara yang benar menyimpan dan mengelola seedphrase kamu, aku sangat menyarankan kamu membaca tutorial lain ini, terutama kalau kamu masih pemula:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/21.webp)

Untuk berpindah ke kata berikutnya, klik tombol kanan. Kamu bisa kembali ke kata sebelumnya dengan menekan tombol kiri. Setelah semua kata selesai kamu tulis, tahan tombol kanan untuk lanjut ke langkah berikutnya.

![Image](assets/fr/22.webp)

Pilih kata-kata dalam seedphrase kamu sesuai urutannya untuk memastikan semuanya sudah kamu tulis dengan benar. Gunakan tombol kiri dan kanan untuk berpindah di antara pilihan kata, lalu pilih kata yang benar dengan menekan kedua tombol secara bersamaan.

![Image](assets/fr/23.webp)

Setelah prosedur verifikasi ini selesai, klik tombol di sebelah kanan.

![Image](assets/fr/24.webp)

## Mengatur kode PIN

Berikutnya adalah langkah kode PIN. Kode PIN akan membuka kunci Trezor kamu. Oleh karena itu, kode ini memberikan perlindungan terhadap akses fisik yang tidak sah. Kode PIN ini tidak terlibat dalam penurunan kunci kriptografi wallet kamu. Jadi, bahkan tanpa akses ke kode PIN, kepemilikan seedphrase 12 kata kamu akan memungkinkan kamu mendapatkan kembali akses ke bitcoin kamu.

Pada Trezor Suite, klik "*Lanjutkan ke PIN*", lalu pada tombol "*Setel PIN*".

![Image](assets/fr/25.webp)

Konfirmasikan dengan Safe 3.

![Image](assets/fr/26.webp)

Kami menyarankan kamu memilih kode PIN yang benar-benar acak. Pastikan kode ini disimpan di tempat yang terpisah dari lokasi penyimpanan Trezor kamu (misalnya di dalam pengelola kata sandi). Kamu bisa membuat kode PIN antara 8 hingga 50 digit. Aku sarankan kamu memilih PIN yang cukup panjang untuk meningkatkan keamanan.

Gunakan tombol kiri dan kanan untuk memilih setiap digit. Untuk mengonfirmasi pilihan dan lanjut ke digit berikutnya, tekan kedua tombol secara bersamaan.

![Image](assets/fr/27.webp)

Setelah selesai, klik tanda centang "*ENTER*" di awal angka, lalu konfirmasikan PIN untuk kedua kalinya.

![Image](assets/fr/28.webp)

Kode PIN telah terdaftar.

![Image](assets/fr/29.webp)

Pada Trezor Suite, klik tombol "*Selesaikan pengaturan*".

![Image](assets/fr/30.webp)

Konfigurasi Safe 3 sekarang sudah selesai. Kalau mau, kamu bisa mengubah nama dan halaman beranda Hardware Wallet Anda.

![Image](assets/fr/31.webp)

Kita nggak akan memerlukan perangkat lunak Trezor Suite lagi, kecuali kalau kamu ingin melakukan pembaruan firmware secara berkala pada hardware wallet, atau menjalankan tes pemulihan. Sekarang kita akan menggunakan Sparrow untuk mengelola portofolio, karena perangkat lunak ini memang paling cocok untuk penggunaan Bitcoin saja.

## Menyiapkan portofolio pada Sparrow Wallet

Mulailah dengan mengunduh dan menginstal Sparrow Wallet [dari situs web resmi] (https://sparrowwallet.com/) di komputer, kalau kamu belum melakukannya.

Setelah kamu membuka Sparrow Wallet, pastikan perangkat lunak ini sudah terhubung ke node Bitcoin, yang ditandai dengan ikon centang di pojok kanan bawah tampilan. Kalau kamu mengalami masalah saat menghubungkan Sparrow, aku sarankan kamu membaca bagian awal tutorial ini:

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klik pada tab "*File*", kemudian pada "*New Wallet*".

![Image](assets/fr/32.webp)

Beri nama portofolio, lalu klik "*Buat Wallet*".

![Image](assets/fr/33.webp)

Pada menu drop-down "*Jenis Skrip*", pilih jenis skrip yang akan digunakan untuk mengamankan bitcoin. Aku merekomendasikan "*Taproot*", atau kalau tidak ada, "*Native SegWit*".

![Image](assets/fr/34.webp)

Klik pada tombol "*Terhubung dengan Hardware Wallet*". Safe 3 tentu saja harus terhubung ke komputer dan tidak terkunci.

![Image](assets/fr/35.webp)

Klik pada tombol "*Pindai*". Safe 3 Anda akan muncul. Klik "*Import Keystore*".

![Image](assets/fr/36.webp)

Sekarang kamu bisa melihat detail Wallet milikmu, termasuk kunci publik yang diperpanjang dari akun pertama. Klik pada tombol "*Apply*" untuk menyelesaikan pembuatan Wallet.

![Image](assets/fr/37.webp)

Pilih kata sandi yang kuat untuk mengamankan akses ke Sparrow Wallet kamu. Kata sandi ini akan melindungi data wallet kamu — termasuk kunci publik, alamat, label, dan riwayat transaksi, dari akses yang tidak sah.

Aku sarankan kamu menyimpan kata sandi ini di pengelola kata sandi supaya nggak lupa di kemudian hari.

![Image](assets/fr/38.webp)

Dan sekarang, portofolio sudah diimpor ke dalam Sparrow Wallet!

![Image](assets/fr/39.webp)

Sebelum kamu menerima bitcoin pertama di dalam wallet, **aku sangat menyarankan kamu untuk melakukan tes pemulihan kosong.** Tuliskan beberapa informasi referensi, seperti xpub kamu, lalu reset Trezor Safe 3 kamu saat wallet masih kosong. Setelah itu, coba pulihkan wallet kamu di Trezor menggunakan cadangan kertas yang sudah kamu buat. Periksa apakah xpub yang muncul setelah pemulihan sama dengan yang kamu catat sebelumnya. Kalau hasilnya sama, berarti cadangan kertas kamu bisa diandalkan.

Untuk mempelajari lebih lanjut tentang cara melakukan tes pemulihan, aku sarankan kamu membaca tutorial berikut ini:
https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Bagaimana cara menerima bitcoin dengan Trezor Safe 3?

Pada Sparrow, klik tab "*Receive*".

![Image](assets/fr/40.webp)

Sebelum menggunakan address yang ditampilkan oleh Sparrow Wallet, pastikan kamu memverifikasinya di layar Trezor kamu. Langkah ini penting untuk memastikan bahwa address yang muncul di Sparrow bukan palsu, dan bahwa hardware wallet kamu benar-benar menyimpan private key yang dibutuhkan untuk membelanjakan bitcoin yang diamankan di address tersebut. Praktik ini membantu kamu terhindar dari berbagai jenis serangan.

Untuk melakukan pemeriksaan ini, klik tombol "*Display Address*".

![Image](assets/fr/41.webp)

Periksa apakah address yang ditampilkan di Trezor kamu sama persis dengan yang ada di Sparrow Wallet. Sebaiknya kamu juga melakukan pengecekan ini sebelum mengirimkan address ke pengirim, untuk memastikan keasliannya. Setelah kamu yakin, gunakan tombol di Trezor untuk mengonfirmasi.

![Image](assets/fr/42.webp)

Kemudian kamu dapat menambahkan "*Label*" untuk mendeskripsikan sumber bitcoin yang akan diamankan dengan Address ini. Ini adalah praktik yang baik yang memungkinkanmu untuk mengelola UTXO dengan lebih baik.

![Image](assets/fr/43.webp)

Kemudian kamu dapat menggunakan Address ini untuk menerima bitcoin.

![Image](assets/fr/44.webp)

## Bagaimana cara mengirim bitcoin dengan Trezor Safe 3?

Setelah kamu menerima Satss pertama di Trezor Safe 3 Wallet, kamu dapat membelanjakannya juga! Hubungkan Trezor ke komputer, buka kuncinya menggunakan kode PIN, luncurkan Sparrow Wallet, lalu buka tab "*Kirim*" untuk membuat transaksi baru.

![Image](assets/fr/45.webp)

Kalau kamu ingin menggunakan fitur Coin Control, yaitu memilih secara spesifik UTXO mana yang akan dipakai dalam transaksi, buka tab "UTXOs". Pilih UTXO yang ingin kamu gunakan, lalu klik "Kirim Terpilih". Kamu akan diarahkan ke layar yang sama di tab "Kirim", tapi dengan UTXO yang sudah dipilih untuk transaksi.

![Image](assets/fr/46.webp)

Masukkan Address tujuan. Kamu juga dapat memasukkan beberapa alamat dengan mengeklik tombol "*+ Tambah*".

![Image](assets/fr/47.webp)


Tuliskan "*Label*" untuk mengingat tujuan pengeluaran ini.

![Image](assets/fr/48.webp)

Pilih jumlah yang akan dikirim ke Address ini.

![Image](assets/fr/49.webp)

Sesuaikan tarif biaya transaksi sesuai dengan pasar saat ini. Sebagai contoh, kamu bisa menggunakan [Mempool.space] (https://Mempool.space/) untuk memilih tarif biaya yang sesuai.

Pastikan semua parameter transaksi kamu sudah benar, lalu klik "*Buat Transaksi*".

![Image](assets/fr/50.webp)

Jika semuanya sudah sesuai dengan keinginan, klik "*Finalisasi Transaksi untuk Penandatanganan*".

![Image](assets/fr/51.webp)

Klik "*Tanda Tangan*".

![Image](assets/fr/52.webp)

Klik "*Sign*" di sebelah Trezor Safe 3 milikmu.

![Image](assets/fr/53.webp)

Periksa parameter transaksi di layar hardware wallet kamu, termasuk address penerima, jumlah yang dikirim, dan biaya transaksi. Setelah semuanya kamu pastikan benar, tekan kedua tombol di Trezor secara bersamaan untuk menandatangani transaksi.

![Image](assets/fr/54.webp)

Sekarang transaksi kamu sudah ditandatangani. Periksa untuk terakhir kalinya apakah semuanya baik-baik saja, lalu klik "*Broadcast Transaction*" untuk menyiarkannya di jaringan Bitcoin.

![Image](assets/fr/55.webp)

Kamu bisa menemukannya di tab "*Transactions*" pada Sparrow Wallet.

![Image](assets/fr/56.webp)

Selamat! Sekarang kamu sudah menguasai penggunaan dasar Trezor Safe 3 dengan Sparrow Wallet. Untuk melangkah lebih jauh, aku sarankan kamu membaca tutorial lengkap tentang cara menggunakan Trezor hardware wallet dengan passphrase BIP39 untuk meningkatkan keamanan kamu:

https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Kalau kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih kalau kamu mau memberikan jempol hijau di bawah ini. Jangan ragu juga untuk membagikan artikel ini di jejaring sosial kamu. Terima kasih banyak!
