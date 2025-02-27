---
name: Paspor - Yayasan
description: Mengonfigurasi dan menggunakan dompet perangkat keras Passport dalam mode manual
---
![cover](assets/cover.webp)

Passport adalah dompet perangkat keras khusus Bitcoin, yang dirancang oleh Foundation Devices, sebuah perusahaan Amerika yang didirikan pada bulan April 2020 di Boston.

Passport "*Batch 2*" yang kami sajikan dalam tutorial ini adalah penerus "*Founder's Edition*". Passport ini memiliki desain premium, layar warna definisi tinggi dan keyboard fisik yang ergonomis. Perangkat ini beroperasi dalam mode "*Air-Gap*", memastikan bahwa kunci pribadi dompet Anda tetap terisolasi sepenuhnya, dengan pertukaran dapat dilakukan melalui kartu MicroSD atau kode QR. Perangkat ini dilengkapi baterai 1200 mAh yang dapat dilepas.

Sedangkan untuk konektivitas, Passport dilengkapi dengan port MicroSD, port USB-C untuk pengisian daya, dan kamera belakang untuk memindai kode QR.

Dalam hal keamanan, Passport menggabungkan elemen yang aman, dan kode sumber perangkat ini sepenuhnya bersifat open source. Ia menawarkan semua fitur yang diharapkan dari dompet perangkat keras Bitcoin yang baik. Perlu dicatat bahwa Passport belum mendukung miniscript, tetapi fitur ini direncanakan untuk kuartal kedua tahun 2025.

Dengan harga $199, Passport diposisikan sebagai dompet perangkat keras kelas atas, bersaing dengan Coldcard Q, Jade Plus, Tezor Safe 5, dan model-model terbaik dari Ledger.

![Image](assets/fr/01.webp)

Untuk mengelola dompet aman Anda pada Passport, Anda memiliki beberapa opsi. Dompet perangkat keras ini kompatibel dengan sebagian besar perangkat lunak manajemen dompet yang ada di pasaran, termasuk Sparrow Wallet, Specter Desktop, Nunchuk, Keeper, dan lain-lain. Dalam tutorial ini, kita akan mempelajari cara menggunakannya dengan Sparrow Wallet.

Jika Anda seorang pemula, pilihan termudah adalah menggunakan Passport Anda dengan aplikasi asli Envoy, yang dikembangkan oleh Foundation. Untuk mengetahui cara menggunakan Envoy dengan Passport Anda, lihat tutorial lainnya:

https://planb.network/tutorials/wallet/mobile/envoy-3ae5d6c7-623b-45b3-bb34-abcf9572b7cb
## Membuka Kotak Paspor

Ketika Anda menerima Paspor, pastikan kotak dan segel pada karton masih utuh untuk mengonfirmasi bahwa paket tersebut belum dibuka. Verifikasi perangkat lunak terhadap keaslian dan integritas perangkat juga akan dilakukan saat perangkat diatur.

![Image](assets/fr/02.webp)

Isi kotak termasuk:


- Paspor;
- Selembar karton untuk menuliskan frasa mnemonik Anda;
- Kabel USB-C untuk pengisian daya ;
- Kartu microSD ;
- Dua adapter MicroSD ke Lightning atau USB-C ;
- Stiker.

Pada perangkat, Anda akan menemukan :


- Keyboard (1) ;
- Port USB-C (2);
- Tombol hapus (3);
- Tombol kembali (4) ;
- Tombol konfirmasi (5);
- Pad arah (6);
- Tombol on/off (7);
- Indikator status (8);
- Port microSD (9) ;
- Tombol untuk mengubah mode aA1 (10) ;
- Kamera belakang.

![Image](assets/fr/03.webp)

## Paspor awal

Tekan tombol on/off di samping unit untuk menyalakannya.

![Image](assets/fr/04.webp)

Tekan tombol konfirmasi untuk mengakses menu berikutnya.

![Image](assets/fr/05.webp)

Dalam tutorial ini, kita akan menggunakan Sparrow Wallet untuk mengelola dompet dengan keamanan Passport. Pilih "*Penyiapan Manual*".

![Image](assets/fr/06.webp)

Kemudian, setujui persyaratan penggunaan.

![Image](assets/fr/07.webp)

Langkah selanjutnya adalah memeriksa perangkat Anda. Hal ini akan mengonfirmasi keaslian Paspor Anda dan memastikan bahwa Paspor Anda belum dirusak dalam perjalanan. Anda akan diminta untuk memindai kode QR.

![Image](assets/fr/08.webp)

Kunjungi [situs verifikasi resmi](https://validate.foundationdevices.com/) dan pilih "*Passport*".

![Image](assets/fr/09.webp)

Gunakan kamera Paspor Anda untuk memindai kode QR yang ditampilkan di situs.

![Image](assets/fr/10.webp)

Perangkat Anda kemudian akan menampilkan 4 kata.

![Image](assets/fr/11.webp)

Masukkan kata-kata ini di situs web untuk mengonfirmasi keaslian Paspor Anda dan klik "*Validate*".

![Image](assets/fr/12.webp)

Jika muncul pesan "*Lulus*", berarti dompet perangkat keras Anda asli. Sekarang Anda bisa menggunakannya untuk mengamankan dompet Bitcoin.

![Image](assets/fr/13.webp)

Konfirmasikan hasil tes pada Paspor Anda.

![Image](assets/fr/14.webp)

## Mengatur kode PIN

Berikutnya adalah langkah kode PIN. Kode PIN akan membuka kunci Paspor Anda. Oleh karena itu, kode PIN memberikan perlindungan terhadap akses fisik yang tidak sah. Kode PIN tidak terlibat dalam penurunan kunci kriptografi dompet Anda. Jadi, bahkan tanpa akses ke kode PIN, kepemilikan frasa mnemonik 12 atau 24 kata Anda akan memungkinkan Anda untuk mendapatkan kembali akses ke bitcoin Anda.

![Image](assets/fr/15.webp)

Kami menyarankan untuk memilih kode PIN yang seacak mungkin. Selain itu, pastikan untuk menyimpan kode ini di tempat yang terpisah dari tempat penyimpanan Paspor Anda (misalnya di pengelola kata sandi).

Anda dapat memilih kode PIN antara 6 dan 12 digit. Saya menyarankan Anda untuk membuatnya sepanjang mungkin.

Gunakan papan tombol untuk memasukkan nomor PIN Anda. Setelah selesai, klik tombol konfirmasi.

![Image](assets/fr/16.webp)

Konfirmasikan PIN Anda untuk kedua kalinya.

![Image](assets/fr/17.webp)

Kode PIN Anda telah terdaftar.

![Image](assets/fr/18.webp)

## Perbarui firmware Paspor

Dompet perangkat keras Anda menyarankan agar Anda memperbarui firmware-nya. Saya sarankan Anda segera memperbarui untuk mendapatkan manfaat dari peningkatan dan perbaikan yang dibawa oleh versi terbaru. Untuk melanjutkan, klik tombol konfirmasi di sebelah kanan.

![Image](assets/fr/19.webp)

Passport Anda siap menerima firmware baru melalui kartu MicroSD.

![Image](assets/fr/20.webp)

Untuk melakukan ini, gunakan kartu MicroSD yang disertakan dalam kotak Passport Anda (atau kartu lainnya), dan masukkan ke dalam komputer Anda. Unduh versi firmware terbaru dari [situs dokumentasi Foundation](https://docs.foundation.xyz/firmware-updates/passport/) atau [repositori GitHub](https://github.com/Foundation-Devices/passport2/releases).

![Image](assets/fr/21.webp)

Sebelum menginstalnya di perangkat Anda, kami sangat menyarankan Anda untuk memeriksa keaslian dan integritas firmware yang diunduh. Jika Anda memerlukan bantuan dalam hal ini, bacalah tutorial ini:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Setelah memeriksa file `.bin`, letakkan file tersebut di MicroSD Anda, lalu masukkan ke dalam Passport. Penjelajah file Passport akan terbuka. Pilih file `vN.N.N-passport.bin`.

![Image](assets/fr/22.webp)

Klik "*Pilih*".

![Image](assets/fr/23.webp)

Kemudian konfirmasikan pemasangan firmware.

![Image](assets/fr/24.webp)

Harap tunggu hingga pembaruan selesai.

![Image](assets/fr/25.webp)

Setelah pembaruan selesai, masukkan kode PIN Anda untuk membuka kunci perangkat dan melanjutkan konfigurasi.

![Image](assets/fr/26.webp)

## Membuat dompet Bitcoin baru

Sekarang saatnya membuat dompet Bitcoin baru. Klik pada tombol konfirmasi.

![Image](assets/fr/27.webp)

Untuk membuat portofolio baru, klik "*Buat Bibit Baru*".

![Image](assets/fr/28.webp)

Anda dapat memilih antara frasa mnemonik 12 atau 24 kata. Keamanan yang ditawarkan oleh kedua opsi ini serupa, sehingga Anda dapat memilih salah satu yang paling mudah disimpan, yaitu 12 kata.

![Image](assets/fr/29.webp)

Klik "*Lanjutkan*".

![Image](assets/fr/30.webp)

Paspor Anda sekarang akan menghasilkan "*Kode Cadangan*". Ini merupakan serangkaian angka yang dapat digunakan untuk mendekripsi cadangan dompet Anda yang tersimpan di MicroSD. Sistem pencadangan ini, khusus untuk perangkat Foundation, merupakan pencadangan tambahan untuk frasa mnemonik Anda, tetapi tidak kompatibel dengan perangkat lunak Bitcoin lainnya.

Jika anda memutuskan untuk menggunakan "*Kode Cadangan*" ini, pastikan untuk menyimpannya di lokasi yang berbeda dengan MicroSD anda yang berisi cadangan terenkripsi dompet anda. Akan tetapi, Anda dapat memilih untuk tidak menggunakan sistem ini jika Anda merasa bahwa cadangan frasa mnemonik Anda sudah cukup.

![Image](assets/fr/31.webp)

Masukkan "*Kode Cadangan*" untuk mengonfirmasi bahwa Anda telah menyimpannya dengan benar.

![Image](assets/fr/32.webp)

Jika MicroSD telah dimasukkan, cadangan terenkripsi portofolio Anda telah disimpan di sana.

![Image](assets/fr/33.webp)

Paspor Anda akan menampilkan frasa mnemonik 12 kata. Kata mnemonik ini memberikan Anda akses penuh dan tidak terbatas ke semua bitcoin Anda. Siapa pun yang memiliki frasa ini dapat mencuri dana Anda, bahkan tanpa akses fisik ke Paspor Anda.

Frasa 12 kata ini mengembalikan akses ke bitcoin Anda jika terjadi kehilangan, pencurian, atau kerusakan pada Paspor Anda. Oleh karena itu, sangat penting untuk menyimpannya dengan hati-hati dan menyimpannya di lokasi yang aman.


Anda bisa menuliskannya pada karton yang disertakan dalam kotak, atau untuk keamanan tambahan, saya sarankan untuk mengukirnya pada dasar baja tahan karat untuk melindunginya dari kebakaran, banjir atau keruntuhan.

Klik tombol konfirmasi untuk melihat frasa mnemonik Anda.

![Image](assets/fr/34.webp)

Untuk informasi lebih lanjut mengenai cara yang tepat untuk menyimpan dan mengelola frasa mnemonik Anda, saya sangat merekomendasikan untuk mengikuti tutorial lainnya, khususnya jika Anda seorang pemula:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
tentu saja, Anda tidak boleh membagikan kata-kata ini di Internet, seperti yang saya lakukan dalam tutorial ini. Portofolio contoh ini hanya akan digunakan di Testnet dan akan dihapus di akhir tutorial.**_

Buatlah cadangan fisik dari kalimat ini.

![Image](assets/fr/35.webp)

Paspor Anda telah berhasil dikonfigurasi. Klik tombol konfirmasi untuk melanjutkan.

![Image](assets/fr/36.webp)

## Penemuan menu

Antarmuka Passport Anda memiliki tiga menu utama:


- "*Rekening*";
- "*Lebih banyak*";
- "*Pengaturan*".

Untuk menavigasi di antara menu-menu ini, gunakan panah kiri dan kanan pada directional pad.

### *Menu "Akun*

Pada menu "*Account*", Anda akan menemukan fitur-fitur utama dompet Bitcoin Anda. Anda bisa menandatangani transaksi melalui kamera atau melalui port MicroSD.

![Image](assets/fr/37.webp)

Submenu "*Account Tools*" menawarkan opsi seperti memverifikasi alamat, menandatangani pesan, atau melihat alamat dalam portofolio Anda.

![Image](assets/fr/38.webp)

Pada submenu "*Manage Account*", Anda dapat menghubungkan dompet Bitcoin Anda ke perangkat lunak manajemen dompet (yang akan kita bahas pada langkah selanjutnya dalam tutorial ini), atau melihat dan mengganti nama akun Anda.

![Image](assets/fr/39.webp)

### Menu "Lainnya

Di menu "*Lebih Banyak*", Anda bisa membuat akun baru dalam portofolio Anda, yang ditautkan ke frasa mnemonik yang sama.

![Image](assets/fr/40.webp)

Anda juga dapat memasukkan kata sandi BIP39 (lihat bagian berikutnya) atau menggunakan seed sementara.

![Image](assets/fr/41.webp)

### Menu "Pengaturan

Di menu "*Pengaturan*", Anda akan menemukan semua pengaturan dompet dan perangkat Anda.

![Image](assets/fr/42.webp)

Submenu "*Perangkat*" memberi Anda opsi untuk menyesuaikan kecerahan layar, mengatur penundaan sebelum penguncian otomatis, mengubah kode PIN, atau mengganti nama perangkat.

![Image](assets/fr/43.webp)

Submenu "*Backup*" memungkinkan Anda mengekspor cadangan portofolio terenkripsi, memeriksa validitas cadangan yang sudah ada, atau mencari "*Backup Code*" lagi.

![Image](assets/fr/44.webp)

Sub-menu "*Firmware*" untuk memperbarui firmware Passport Anda. Kami menyarankan agar Anda melakukan pembaruan ini secara teratur untuk mendapatkan manfaat dari perbaikan dan fitur terbaru.

![Image](assets/fr/45.webp)

Sub-menu "*Bitcoin*" memungkinkan Anda untuk mengubah unit yang ditampilkan (BTC atau satoshi), mengelola dompet Multisig yang mungkin, atau beralih ke mode "*Testnet*".

![Image](assets/fr/46.webp)

Dalam "*Advanced*", Anda dapat melihat kata-kata frasa mnemonik Anda, melakukan tindakan pada MicroSD yang dimasukkan, mengatur ulang Passport ke pengaturan pabrik, atau melakukan pemeriksaan keaslian, seperti yang dilakukan sebelumnya.

![Image](assets/fr/47.webp)

Anda dapat mengaktifkan "*Security Words*", sebuah fitur yang menambahkan lapisan keamanan dengan menampilkan dua kata tertentu ketika membuka kunci perangkat setelah memasukkan empat digit pertama kode PIN. Kata-kata ini, yang akan disimpan selama konfigurasi, memastikan bahwa Passport belum diganti atau dirusak. Jika terjadi perbedaan di kemudian hari, kami menyarankan Anda untuk tidak menggunakan perangkat. Saya menyarankan Anda untuk mengaktifkan opsi ini untuk mencegah sebagian besar risiko gangguan fisik pada perangkat.

![Image](assets/fr/48.webp)

Terakhir, sub-menu "*Extensions*" memungkinkan Anda mengaktifkan fungsi yang spesifik untuk penggunaan alat tertentu, misalnya, protokol coinjoin Whirlpool.

![Image](assets/fr/49.webp)

## Menambahkan kata sandi BIP39

Sebelum melanjutkan, jika Anda mau, Anda dapat menambahkan kata sandi BIP39. Kata sandi BIP39 adalah kata sandi opsional yang bisa Anda pilih secara bebas, dan ditambahkan ke frasa mnemonik Anda untuk memperkuat keamanan dompet. Dengan mengaktifkan fitur ini, akses ke dompet Bitcoin Anda akan membutuhkan kata kunci dan frasa sandi. Tanpa keduanya, mustahil untuk memulihkan dompet.

Sebelum mengonfigurasi opsi ini pada Passport Anda, sangat disarankan agar Anda membaca artikel ini untuk memahami sepenuhnya operasi teoritis dari kata sandi dan menghindari kesalahan yang dapat menyebabkan hilangnya bitcoin Anda:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Untuk mengaktifkannya, buka menu "*Lainnya*" dan klik "*Masukkan Kata Sandi*".

![Image](assets/fr/50.webp)

Masukkan kata sandi Anda menggunakan keypad aA1, dan pastikan Anda menyimpannya satu kali atau lebih pada media fisik (kertas atau logam). Sebagai contoh, saya menggunakan kata sandi yang sangat lemah, tetapi Anda harus memilih kata sandi yang kuat dan acak, termasuk semua jenis karakter dan cukup panjang (seperti kata sandi yang kuat).

![Image](assets/fr/51.webp)

Harap diperhatikan bahwa kata sandi BIP39 peka terhadap huruf besar-kecil dan kesalahan ketik. Jika Anda memasukkan kata sandi yang sedikit berbeda dengan yang dikonfigurasikan pada awalnya, Passport tidak akan melaporkan kesalahan, tetapi akan mendapatkan satu set kunci kriptografi lain yang tidak sama dengan kunci yang ada di dompet awal Anda.


Oleh karena itu, penting sekali, ketika mengonfigurasi, untuk mencatat di suatu tempat sidik jari kunci utama yang akan diberikan pada langkah berikutnya. Sebagai contoh, dengan kata sandi saya `Plan B Network`, sidik jari kunci utama saya adalah `745D526B`.

![Image](assets/fr/52.webp)

Setiap kali Anda membuka kunci Passport, Anda harus kembali ke menu ini untuk memasukkan kata sandi dan menerapkannya ke dompet. Passport tidak menyimpan kata sandi.

 fix-nakamochi-elysium-tutos
Setiap kali Anda membuka kunci, setelah menuliskan kata sandi, periksa pada layar konfirmasi bahwa sidik jari yang diberikan sama dengan yang Anda tuliskan selama konfigurasi. Jika ya, kata sandi Anda sudah benar dan Anda mengakses dompet Bitcoin yang benar. Jika tidak, Anda menggunakan dompet yang salah dan perlu mencoba lagi, berhati-hatilah agar tidak melakukan kesalahan input.


Sebelum Anda menerima bitcoin pertama Anda di dompet Anda, **Saya sangat menyarankan Anda untuk melakukan tes pemulihan kosong**. Catatlah beberapa informasi referensi, seperti xpub atau alamat penerima pertama Anda, kemudian hapus wallet Anda di Passport saat masih kosong (`Pengaturan -> Lanjutan -> Hapus Passport`). Kemudian coba pulihkan dompet Anda menggunakan cadangan kertas dari frasa mnemonik dan kata sandi apa pun. Periksa apakah informasi cookie yang dihasilkan setelah pemulihan sesuai dengan yang Anda tulis sebelumnya. Jika sesuai, Anda bisa yakin bahwa cadangan kertas Anda dapat diandalkan. Untuk mengetahui lebih lanjut tentang cara melakukan pemulihan tes, silakan baca tutorial lainnya:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
![Image](assets/fr/53.webp)

## Mengonfigurasi dompet di Dompet Sparrow

Dalam tutorial ini, saya akan menunjukkan kepada Anda penggunaan lanjutan Passport dengan Sparrow Wallet. Namun, dompet perangkat keras ini juga kompatibel dengan Envoy (aplikasi Foundation), Keeper, BlueWallet, Nunchuk, Spectre, dan banyak lagi...

Mulailah dengan mengunduh dan menginstal Sparrow Wallet [dari situs web resmi] (https://sparrowwallet.com/) di komputer Anda, jika Anda belum melakukannya.

![Image](assets/fr/54.webp)

Pastikan untuk memeriksa keaslian dan integritas perangkat lunak sebelum instalasi. Jika Anda tidak tahu cara melakukannya, silakan baca tutorial ini:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Setelah Sparrow Wallet terbuka, klik tab "*File*", lalu "*Dompet Baru*".

![Image](assets/fr/55.webp)

Beri nama dompet Anda, lalu klik "*Buat Dompet*".

![Image](assets/fr/56.webp)

Pilih "*Dompet Perangkat Keras yang Terisi Penuh*".

![Image](assets/fr/57.webp)

Klik "*Pindai...*" di samping opsi "*Passport*". Ini akan membuka webcam Anda.

![Image](assets/fr/58.webp)

Pada dompet perangkat keras Anda, buka menu "*Akun*", pilih submenu "*Kelola Akun*", dan klik "*Hubungkan Dompet*".

![Image](assets/fr/59.webp)

Pada daftar tarik-turun yang muncul, pilih "*Sparrow*".

![Image](assets/fr/60.webp)

Kemudian pilih "*Single-sig*" untuk konfigurasi normal, tanpa multisig.

![Image](assets/fr/61.webp)

Pilih opsi "*Kode QR*".

![Image](assets/fr/62.webp)

Paspor Anda kemudian akan menghasilkan kode QR dinamis. Gunakan webcam komputer Anda untuk memindai kode tersebut ke dalam perangkat lunak Sparrow.

![Image](assets/fr/63.webp)

Sekarang Anda akan melihat xpub dan sidik jari kunci utama Anda, yang seharusnya cocok dengan yang ditampilkan di Paspor Anda saat Anda memasukkan kata sandi. Klik pada tombol "*Apply*".

![Image](assets/fr/64.webp)

Tetapkan kata sandi yang kuat untuk mengamankan akses ke Dompet Sparrow Anda. Kata sandi ini akan melindungi kunci publik, alamat, label, dan riwayat transaksi Anda dari akses yang tidak sah. Sebaiknya simpan kata sandi ini di pengelola kata sandi, agar Anda tidak lupa.

![Image](assets/fr/65.webp)

Paspor Anda kemudian meminta Anda untuk memindai alamat penerimaan pertama untuk mengonfirmasi bahwa impor telah berhasil.

![Image](assets/fr/66.webp)

Di Sparrow, buka tab "*Receive*" dan pindai kode QR dari alamat pertama.

![Image](assets/fr/67.webp)

Jika operasi berhasil, Paspor Anda akan menampilkan "*Verified*".

![Image](assets/fr/68.webp)

Hal ini menegaskan bahwa impor tersebut berhasil.

![Image](assets/fr/69.webp)

## Menerima bitcoin

Setelah Passport Anda siap, Anda siap untuk menerima satoshi pertama Anda di dompet Bitcoin baru Anda. Untuk melakukannya, pada Sparrow, klik menu "*Receive*".

![Image](assets/fr/70.webp)

Sparrow akan menampilkan alamat tanda terima kosong pertama dalam portofolio Anda. Anda dapat menambahkan label.

![Image](assets/fr/71.webp)

Sebelum menggunakannya, kita akan memeriksa alamat di layar Passport untuk memastikan alamat tersebut adalah milik dompet Bitcoin kita. Di Sparrow, Anda bisa memperbesar kode QR alamat tersebut dengan mengekliknya jika perlu. Pada menu "*Akun*" di Passport Anda, pilih "*Alat Akun*".

![Image](assets/fr/72.webp)

Klik "*Verifikasi Alamat*", lalu pindai kode QR yang ditampilkan di Sparrow Wallet.

![Image](assets/fr/73.webp)

Pastikan alamat yang ditampilkan di Paspor sama persis dengan alamat yang ditampilkan di Sparrow, dan muncul tulisan "*Verified*".

![Image](assets/fr/74.webp)

Anda sekarang dapat menggunakannya untuk menerima bitcoin. Ketika transaksi disiarkan di jaringan, transaksi tersebut akan muncul di Sparrow. Tunggu hingga Anda menerima konfirmasi yang cukup untuk menganggap transaksi tersebut sudah pasti.

![Image](assets/fr/75.webp)

## Kirim bitcoin

Sekarang setelah Anda memiliki beberapa sat di dompet Anda, Anda juga dapat mengirim beberapa. Untuk melakukannya, klik menu "*UTXOs*".

![Image](assets/fr/76.webp)

Pilih UTXO yang ingin Anda gunakan sebagai input untuk transaksi ini, lalu klik "*Kirim Terpilih*".

![Image](assets/fr/77.webp)

Masukkan alamat penerima, label untuk mengingatkan Anda tentang tujuan transaksi dan jumlah yang ingin Anda kirim ke alamat ini.

![Image](assets/fr/78.webp)

Sesuaikan tarif biaya sesuai dengan kondisi pasar saat ini, lalu klik "*Buat Transaksi*".

![Image](assets/fr/79.webp)

Pastikan semua parameter transaksi sudah benar, lalu klik "*Finalisasi Transaksi untuk Penandatanganan*".

![Image](assets/fr/80.webp)

Klik "*Show QR*" untuk menampilkan PSBT (*Transaksi Bitcoin yang Ditandatangani Sebagian*). Sparrow telah membuat transaksi, tetapi masih belum memiliki tanda tangan untuk membuka kunci bitcoin yang digunakan dalam input. Tanda tangan ini hanya dapat dilakukan oleh Passport, yang menjadi tempat penyimpanan seed Anda dan memberikan akses ke private key yang diperlukan untuk menandatangani transaksi.

![Image](assets/fr/81.webp)

Pada Paspor Anda, akses menu "*Akun*" dan klik "*Tanda Tangan dengan Kode QR*".

![Image](assets/fr/82.webp)

Pindai PSBT (*Transaksi Bitcoin Bertanda Tangan Sebagian*) yang ditampilkan di Dompet Sparrow.

![Image](assets/fr/83.webp)

Konfirmasikan bahwa alamat penerima dan jumlah yang dikirim sudah benar, lalu tekan tombol konfirmasi.

![Image](assets/fr/84.webp)

Periksa alamat pertukaran. Dalam contoh saya, tidak ada, karena transaksi ini mencakup satu keluaran.

![Image](assets/fr/85.webp)

Pastikan biaya tersebut sesuai dengan yang Anda pilih.

![Image](assets/fr/86.webp)

Jika semua informasi sudah benar, klik tombol konfirmasi untuk menandatangani transaksi.

![Image](assets/fr/87.webp)

Pada Sparrow Wallet, klik "*Pindai QR*" dan pindai kode QR yang ditampilkan pada Paspor Anda.

![Image](assets/fr/88.webp)

Transaksi yang Anda tandatangani sekarang siap untuk disiarkan di jaringan Bitcoin dan dimasukkan ke dalam blok oleh penambang. Jika semuanya sudah benar, klik "*Siarkan Transaksi*".

![Image](assets/fr/89.webp)

Transaksi Anda telah disiarkan dan menunggu konfirmasi.

![Image](assets/fr/90.webp)

Selamat, Anda sekarang tahu cara mengonfigurasi dan menggunakan Passport. Jika Anda merasa tutorial ini bermanfaat, saya akan berterima kasih jika Anda memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial Anda. Terima kasih telah berbagi!

Untuk informasi lebih lanjut, lihat tutorial kami tentang perangkat lunak Liana:

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04