---
name: Trezor Safe 3
description: Mengkonfigurasi dan menggunakan Hardware Wallet Safe 3
---
![cover](assets/cover.webp)



*Kredit gambar: [Trezor.io](https://trezor.io/)*



Trezor Safe 3 adalah hardware wallet yang dirancang oleh SatoshiLabs dan dirilis pada tahun 2023. Ini adalah model yang sangat ringkas dan ringan, hanya 14 gram, dan ditujukan untuk pengguna pemula hingga menengah. Perangkat ini merupakan penerus Model One yang terkenal, dengan peningkatan yang signifikan, sambil tetap mempertahankan pendekatan open source yang menjadi ciri khas merek ini dan membedakannya dari pesaing utamanya, Ledger. Safe 3 dibanderol dengan harga €79, sehingga diposisikan di segmen hardware wallet kelas menengah dan bersaing langsung dengan Ledger Nano S Plus.

Safe 3 tidak memiliki baterai dan hanya beroperasi melalui koneksi USB-C yang digunakan untuk daya sekaligus komunikasi. Perangkat ini dilengkapi layar OLED monokrom 0,96 inci dan dua tombol fisik.


![Image](assets/fr/01.webp)



Safe 3 menawarkan semua fitur penting yang diharapkan dari hardware wallet yang baik, termasuk integrasi passphrase BIP39 yang sangat solid. Namun, perangkat ini belum mendukung Miniscript.

Model ini sangat cocok untuk pemula, dan bahkan mungkin jadi hardware wallet yang paling sering aku rekomendasikan ke pengguna baru. Perangkat ini juga tetap relevan untuk pengguna tingkat menengah. Tapi untuk pengguna tingkat lanjut yang mencari fitur lebih spesifik, seperti yang tersedia di perangkat seperti Coldcard, Safe 3 mungkin belum memenuhi semua kebutuhan tersebut. Meski begitu, kalau kamu tidak butuh fitur tingkat lanjut itu, Trezor Safe 3 bisa jadi pilihan yang sangat bagus.



## Model keamanan Trezor Safe 3



Trezor Safe 3 sekarang dilengkapi dengan **Secure Element** bersertifikasi EAL6+, sebuah peningkatan besar dibanding model sebelumnya seperti Model One dan Model T. Perangkat ini memakai chip OPTIGA Trust M V3, yang tidak langsung menyimpan seed, tetapi berfungsi sebagai komponen kriptografi untuk mengamankan akses ke seed. Secure Element menyimpan rahasia yang hanya bisa diakses setelah kamu memasukkan PIN dengan benar. Rahasia ini kemudian dipakai untuk mendekripsi seed, yang disimpan dalam keadaan terenkripsi di memori utama perangkat.

Sistem keamanan hibrida ini memberikan perlindungan fisik yang jauh lebih baik, terutama terhadap serangan ekstraksi atau analisis invasif, yang sebelumnya jadi titik lemah pada Model One, khususnya dalam pengelolaan PIN. Kerentanan ini kini bisa diminimalkan berkat penggunaan Secure Element. Model ini juga tetap mempertahankan arsitektur perangkat lunak open source: kode yang mengelola pembuatan dan penggunaan private key tetap bisa diakses dan diverifikasi sepenuhnya. Chip OPTIGA hanya menangani PIN, yaitu elemen yang berada di luar manajemen kunci Bitcoin wallet. Chip ini hanya mengeluarkan rahasia yang digunakan untuk mendekripsi seed. Selain itu, OPTIGA Trust M V3 memiliki lisensi yang relatif terbuka, sehingga SatoshiLabs bisa mempublikasikan potensi kerentanan secara bebas.

Menurutku, model keamanan ini adalah salah satu kompromi terbaik yang tersedia saat ini. Pendekatan ini menggabungkan keunggulan Secure Element dengan transparansi perangkat lunak open source. Sebelumnya, pengguna harus memilih antara perlindungan fisik ekstra lewat chip khusus atau transparansi penuh lewat open source. Dengan Trezor Safe 3, kamu bisa mendapatkan keduanya.

Dalam tutorial ini, kita akan bahas cara mengatur dan menggunakan Trezor Safe 3 dengan aman.

## Membuka Kotak Trezor Safe 3

Saat kamu menerima Safe 3, pastikan kotak dan segelnya masih utuh untuk memastikan paket belum pernah dibuka. Verifikasi perangkat lunak untuk keaslian dan integritas perangkat juga akan dilakukan saat proses setup nanti.

Isi kotak termasuk:

- Trezor Safe 3;
- Amplop berisi kartu kosong untuk mencatat seedphrase, stiker, dan instruksi mnemonic;
- Kabel USB-C ke USB-C.


![Image](assets/fr/02.webp)



Ketika dibuka, Trezor Safe 3 harus dilindungi oleh plastik pelindung dan port USB-C harus diamankan dengan Seal hologram. Pastikan itu ada di sana.



![Image](assets/fr/03.webp)



Navigasi pada perangkat ini sangat mudah: gunakan tombol kanan untuk menggulir ke kanan, dan tombol kiri untuk menggulir ke kiri. Tekan kedua tombol secara bersamaan untuk mengonfirmasi tindakan.



![Image](assets/fr/04.webp)



## Prasyarat



Untuk tutorial ini, aku akan menunjukkan ke kamu bagaimana cara menggunakan Trezor Safe 3 dengan [perangkat lunak manajemen portofolio Sparrow Wallet](https://sparrowwallet.com/download/). Jika kamu belum menginstal perangkat lunak ini, silakan lakukan sekarang. Jika Anda membutuhkan bantuan, kami juga memiliki tutorial terperinci tentang cara mengonfigurasi Sparrow Wallet:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Kamu juga butuh perangkat lunak Trezor Suite untuk mengonfigurasi Safe 3, memeriksa keasliannya, dan menginstal firmware. Kita hanya akan memakai software ini untuk proses tersebut, dan setelah itu hanya diperlukan lagi saat ada pembaruan firmware. Untuk pengelolaan wallet sehari-hari, kita akan menggunakan Sparrow Wallet saja, karena memang dioptimalkan untuk Bitcoin dan mudah dipakai, bahkan untuk pemula (Sparrow hanya mendukung Bitcoin, bukan altcoin).



[Unduh Trezor Suite dari situs web resmi](https://trezor.io/trezor-suite)



![Image](assets/fr/05.webp)



Untuk kedua program ini, aku sangat menyarankan kamu memeriksa keasliannya dengan GnuPG dan integritasnya lewat hash sebelum menginstalnya di komputer. Kalau kamu belum tahu caranya, kamu bisa mengikuti tutorial ini:


https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Memulai Trezor Safe 3



Sambungkan Safe 3 milikmu ke komputer yang sudah terinstal Trezor Suite dan Sparrow Wallet.



![Image](assets/fr/06.webp)



Buka Trezor Suite, lalu klik "*Setup my Trezor*".



![Image](assets/fr/07.webp)



Pilih "*Firmware khusus Bitcoin*", lalu klik "*Instal Bitcoin saja*".



![Image](assets/fr/08.webp)



Trezor Suite kemudian akan menginstal firmware di Safe 3 kamu. Tunggu sampai proses instalasinya selesai.


![Image](assets/fr/09.webp)



Klik "*Lanjutkan*".



![Image](assets/fr/10.webp)



Kemudian lanjutkan ke uji keaslian untuk memastikan Hardware Wallet kamu tidak palsu atau disusupi.



![Image](assets/fr/11.webp)



Pada Safe 3 kamu, tekan tombol kanan untuk mengonfirmasi.



![Image](assets/fr/12.webp)



Jika Trezor kamu asli, pesan konfirmasi akan muncul di Trezor Suite.



![Image](assets/fr/13.webp)



Kamu kemudian dapat melewati jendela dengan petunjuk pengoperasian dasar.



![Image](assets/fr/14.webp)



## Menciptakan portofolio Bitcoin



Pada Trezor Suite, klik tombol "*Buat Wallet baru*".



![Image](assets/fr/15.webp)



Untuk portofolio standar, kamu bisa pilih jenis cadangan default. Ini akan membuat wallet single-signature klasik dengan mnemonic 12 kata. Klik "*Buat Wallet*".

Kalau kamu ingin tahu lebih lanjut tentang opsi cadangan lain yang tersedia di Trezor, termasuk *Cadangan Multi-Bagi*, aku sarankan kamu juga baca tutorial ini:

https://planb.academy/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/16.webp)



Terima persyaratan penggunaan pada Hardware Wallet.



![Image](assets/fr/17.webp)



Tekan tombol kanan sekali lagi untuk membuat portofolio baru.



![Image](assets/fr/18.webp)



Di Trezor Suite, klik "*Lanjutkan pencadangan*".



![Image](assets/fr/19.webp)



Perangkat lunak ini akan memberi kamu panduan tentang cara mengelola mnemonic.

Mnemonic ini memberi kamu akses penuh dan tanpa batas ke semua bitcoin kamu. Siapa pun yang punya frasa ini bisa mencuri dana kamu, bahkan tanpa akses fisik ke Trezor Safe 3.

Frasa 12 kata ini memungkinkan kamu memulihkan akses ke bitcoin kalau terjadi kehilangan, pencurian, atau kerusakan pada hardware wallet. Karena itu, sangat penting untuk menyimpannya dengan hati-hati dan menaruhnya di tempat yang aman.

Kamu bisa menuliskannya di kartu karton yang ada di dalam kotak, atau untuk keamanan tambahan, aku sarankan mengukirnya di plat baja tahan karat supaya terlindung dari kebakaran, banjir, atau kerusakan fisik lainnya.

Konfirmasi petunjuknya, lalu klik tombol "*Buat cadangan Wallet*".



![Image](assets/fr/20.webp)



Safe 3 akan membuat mnemonic menggunakan generator angka acak. Pastikan kamu tidak diawasi selama proses ini. Tuliskan kata-kata yang muncul di layar ke media fisik pilihan kamu. Tergantung strategi keamanan kamu, kamu bisa mempertimbangkan membuat beberapa salinan fisik lengkap dari frasa tersebut, tapi yang paling penting, jangan pernah membagikannya. Sangat penting untuk menuliskan kata-kata itu secara bernomor dan berurutan.

**Tentu saja, kamu tidak boleh membagikan kata-kata ini di internet, seperti yang aku lakukan di tutorial ini. Contoh wallet ini hanya akan digunakan di testnet dan akan dihapus di akhir tutorial.**

Untuk info lebih lanjut tentang cara menyimpan dan mengelola mnemonic dengan benar, aku sangat merekomendasikan kamu mengikuti tutorial lain ini, terutama kalau kamu masih pemula:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/21.webp)



Untuk pindah ke kata berikutnya, tekan tombol kanan. Kamu bisa kembali ke kata sebelumnya dengan menekan tombol kiri. Setelah semua kata selesai kamu tulis, tahan tombol kanan untuk lanjut ke langkah berikutnya.


![Image](assets/fr/22.webp)



Pilih kata-kata dalam mnemonic sesuai urutannya untuk memastikan kamu sudah menuliskannya dengan benar. Gunakan tombol kiri dan kanan untuk berpindah di antara pilihan, lalu pilih kata yang tepat dengan menekan kedua tombol secara bersamaan.


![Image](assets/fr/23.webp)



Setelah prosedur verifikasi ini selesai, klik tombol di sebelah kanan.



![Image](assets/fr/24.webp)



## Mengatur kode PIN



Berikutnya adalah langkah untuk membuat PIN. PIN ini akan membuka kunci Trezor kamu. Karena itu, PIN memberi perlindungan terhadap akses fisik yang tidak sah. PIN tidak terlibat dalam proses derivasi kunci kriptografi wallet kamu. Jadi, meskipun tanpa akses ke PIN, kalau kamu masih punya mnemonic 12 kata, kamu tetap bisa memulihkan akses ke bitcoin kamu.

Di Trezor Suite, klik "*Lanjutkan ke PIN*", lalu klik tombol "*Setel PIN*".



![Image](assets/fr/25.webp)



Konfirmasikan dengan Safe 3.



![Image](assets/fr/26.webp)



Kami menyarankan kamu memilih PIN yang seacak mungkin. Simpan PIN ini di tempat yang terpisah dari Trezor kamu, misalnya di dalam password manager. Kamu bisa membuat PIN antara 8 sampai 50 digit. Aku sarankan pilih PIN sepanjang mungkin untuk meningkatkan keamanan.

Gunakan tombol kiri dan kanan untuk memilih setiap digit. Untuk mengonfirmasi pilihan dan lanjut ke digit berikutnya, tekan kedua tombol secara bersamaan.


![Image](assets/fr/27.webp)



Setelah selesai, klik tanda centang "*ENTER*" di awal angka, lalu konfirmasikan PIN untuk kedua kalinya.



![Image](assets/fr/28.webp)



Kode PIN kamu telah terdaftar.



![Image](assets/fr/29.webp)



Pada Trezor Suite, klik tombol "*Selesaikan pengaturan*".



![Image](assets/fr/30.webp)



Konfigurasi Safe 3 kamu sekarang sudah selesai. Kalau mau, kamu bisa mengubah nama dan tampilan beranda hardware wallet kamu.


![Image](assets/fr/31.webp)



Kita tidak akan memerlukan Trezor Suite lagi, kecuali untuk melakukan pembaruan firmware secara berkala pada hardware wallet atau kalau kamu ingin menjalankan tes pemulihan. Sekarang kita akan memakai Sparrow untuk mengelola portofolio, karena software ini memang sangat cocok untuk penggunaan Bitcoin saja.



## Menyiapkan portofolio pada Sparrow Wallet



Mulailah dengan mengunduh dan menginstal Sparrow Wallet [dari situs web resmi](https://sparrowwallet.com/) di komputer kamu, jika kamu belum melakukannya.



Setelah kamu membuka Sparrow Wallet, pastikan software ini terhubung ke node Bitcoin, yang ditandai dengan tanda centang di sudut kanan bawah antarmuka. Kalau kamu mengalami masalah saat menghubungkan Sparrow, aku sarankan kamu membaca bagian awal tutorial ini:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klik pada tab "*File*", kemudian pada "*New Wallet*".



![Image](assets/fr/32.webp)



Beri nama portofolio kamu, lalu klik "*Buat Wallet*".



![Image](assets/fr/33.webp)



Pada menu drop-down "*Jenis Skrip*", pilih jenis skrip yang akan digunakan untuk mengamankan bitcoin. Aku merekomendasikan "*Taproot*", atau jika tidak ada, "*Native SegWit*".



![Image](assets/fr/34.webp)



Klik pada tombol "*Terhubung dengan Hardware Wallet*". Safe 3 kamu tentu saja harus terhubung ke komputer dan tidak terkunci.



![Image](assets/fr/35.webp)



Klik pada tombol "*Pindai*". Safe 3 akan muncul. Klik "*Import Keystore*".



![Image](assets/fr/36.webp)



Sekarang kamu bisa melihat detail wallet kamu, termasuk extended public key dari akun pertama. Klik tombol "*Apply*" untuk menyelesaikan pembuatan wallet.


![Image](assets/fr/37.webp)



Pilih kata sandi yang kuat untuk mengamankan akses ke Sparrow Wallet. Kata sandi ini akan memastikan data Sparrow kamu tetap aman, termasuk kunci publik, alamat, label, dan riwayat transaksi, agar tidak bisa diakses oleh pihak yang tidak berwenang.

Aku sarankan kamu menyimpan kata sandi ini di password manager supaya tidak lupa.


![Image](assets/fr/38.webp)



Dan sekarang, portofolio kamu sudah diimpor ke dalam Sparrow Wallet!



![Image](assets/fr/39.webp)


Sebelum kamu menerima bitcoin pertama di wallet, **aku sangat menyarankan kamu melakukan tes pemulihan kosong dulu**. Catat beberapa informasi referensi, seperti xpub kamu, lalu reset Trezor Safe 3 saat wallet masih kosong. Setelah itu, coba pulihkan wallet di Trezor menggunakan cadangan kertas kamu. Periksa apakah xpub yang dihasilkan setelah pemulihan sama dengan yang sudah kamu catat sebelumnya. Kalau cocok, berarti cadangan kertas kamu bisa diandalkan.

Untuk tahu lebih lanjut tentang cara melakukan tes pemulihan, aku sarankan kamu membaca tutorial ini:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Bagaimana cara menerima bitcoin dengan Trezor Safe 3?



Pada Sparrow, klik tab "*Receive*".



![Image](assets/fr/40.webp)



Sebelum kamu menggunakan alamat yang diusulkan Sparrow Wallet, periksa dulu di layar Trezor kamu. Langkah ini memastikan bahwa alamat yang ditampilkan di Sparrow bukan palsu, dan bahwa hardware wallet memang menyimpan private key yang diperlukan untuk membelanjakan bitcoin yang diamankan dengan alamat tersebut. Ini membantu kamu menghindari beberapa jenis serangan.

Untuk melakukan pengecekan ini, klik tombol "*Display Address*".


![Image](assets/fr/41.webp)



Periksa apakah Address yang ditampilkan di Trezor Anda sesuai dengan yang ada di Sparrow Wallet. Sebaiknya Anda juga melakukan pemeriksaan ini sebelum mengirimkan Address Anda ke pengirim, untuk memastikan keabsahannya. Anda dapat menggunakan tombol untuk mengonfirmasi.



![Image](assets/fr/42.webp)



Kemudian kamu dapat menambahkan "*Label*" untuk mendeskripsikan sumber bitcoin yang akan diamankan dengan Address ini. Ini adalah praktik yang baik yang memungkinkanmu untuk mengelola UTXO dengan lebih baik.



![Image](assets/fr/43.webp)



Kamu kemudian dapat menggunakan Address ini untuk menerima bitcoin.



![Image](assets/fr/44.webp)



## Bagaimana cara mengirim bitcoin dengan Trezor Safe 3?



Setelah kamu menerima Sats pertama di Safe 3-aman Wallet, kamu dapat membelanjakannya juga! Hubungkan Trezor milikmu ke komputer, buka kuncinya menggunakan kode PIN, luncurkan Sparrow Wallet, lalu buka tab "*Kirim*" untuk membuat transaksi baru.



![Image](assets/fr/45.webp)



Jika kamu ingin *Coin Control*, yaitu memilih secara spesifik UTXO mana yang akan digunakan dalam transaksi, buka tab "*UTXOs*". Pilih UTXO yang ingin kamu gunakan, lalu klik "*Kirim Terpilih*". Kamu akan diarahkan ke layar yang sama pada tab "*Kirim*", tetapi dengan UTXO yang sudah dipilih untuk transaksi.


![Image](assets/fr/46.webp)



Masukkan Address tujuan. Kamu juga dapat memasukkan beberapa alamat dengan mengeklik tombol "*+ Tambah*".



![Image](assets/fr/47.webp)



Tuliskan "*Label*" untuk mengingat tujuan pengeluaran ini.



![Image](assets/fr/48.webp)



Pilih jumlah yang akan dikirim ke Address ini.



![Image](assets/fr/49.webp)



Sesuaikan tarif biaya transaksi kamu sesuai dengan pasar saat ini. Sebagai contoh, kamu dapat menggunakan [Mempool.space](https://Mempool.space/) untuk memilih tarif biaya yang sesuai.



Pastikan semua parameter transaksi kamu sudah benar, lalu klik "*Buat Transaksi*".



![Image](assets/fr/50.webp)



Jika semuanya sudah sesuai dengan keinginan, klik "*Finalisasi Transaksi untuk Penandatanganan*".



![Image](assets/fr/51.webp)



Klik "*Tanda Tangan*".



![Image](assets/fr/52.webp)



Klik "*Sign*" di sebelah Trezor Safe 3.



![Image](assets/fr/53.webp)



Periksa parameter transaksi pada layar hardware wallet kamu, termasuk address penerima, jumlah yang dikirim, dan biaya. Setelah transaksi diverifikasi di Trezor, klik kedua tombol secara bersamaan untuk menandatanganinya.


![Image](assets/fr/54.webp)



Transaksi kamu sekarang sudah ditandatangani. Periksa sekali lagi apakah semuanya sudah benar, lalu klik "*Broadcast Transaction*" untuk menyiarkannya ke jaringan Bitcoin.


![Image](assets/fr/55.webp)



Kamu bisa menemukannya di tab "*Transactions*" pada Sparrow Wallet.



![Image](assets/fr/56.webp)



Selamat, kamu sudah menguasai penggunaan dasar Trezor Safe 3 dengan Sparrow Wallet! Untuk melangkah lebih jauh, aku merekomendasikan tutorial komprehensif tentang penggunaan Trezor Hardware Wallet dengan passphrase BIP39 untuk meningkatkan keamananmu:



https://planb.academy/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Kalau kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih jika kamu mau memberikan jempol Green di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial kamu. Terima kasih banyak!
