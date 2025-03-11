---
name: Utusan
description: Menyiapkan dan menggunakan Paspor dengan aplikasi Envoy
---
![cover](assets/cover.webp)

Envoy adalah sebuah aplikasi manajemen dompet Bitcoin yang dikembangkan oleh Foundation. Aplikasi ini dirancang khusus untuk digunakan dengan dompet perangkat keras Passport.

Passport "*Batch 2*" yang kami perkenalkan dalam tutorial ini dengan aplikasi Envoy adalah penerus dari edisi "*Founder's Edition*". Perangkat ini memiliki desain premium, layar warna berdefinisi tinggi, dan keyboard fisik yang ergonomis. Beroperasi dalam mode "*Air-Gap*", memastikan kunci pribadi dompet Anda tetap sepenuhnya terisolasi, dengan pertukaran data yang dilakukan melalui kartu MicroSD atau kode QR. Perangkat ini dilengkapi dengan baterai isi ulang yang dapat dilepas, Nokia BL-5C berkapasitas 1200 mAh. Baterai non-proprietary ini mudah diganti karena model BL-5C tersedia luas di pasaran.

Sedangkan untuk konektivitas, Passport dilengkapi dengan port MicroSD, port USB-C untuk pengisian daya, dan kamera belakang untuk memindai kode QR.

Dalam hal keamanan, Passport menggabungkan elemen yang aman, dan kode sumber perangkat ini sepenuhnya bersifat open source. Ia menawarkan semua fitur yang diharapkan dari dompet perangkat keras Bitcoin yang baik. Perlu dicatat bahwa Passport belum mendukung miniscript, tetapi fitur ini direncanakan untuk kuartal kedua tahun 2025.

Dengan harga $199, Passport diposisikan sebagai dompet perangkat keras kelas atas, bersaing dengan Coldcard Q, Jade Plus, Tezor Safe 5, dan model-model terbaik dari Ledger.

![Image](assets/fr/01.webp)

Untuk mengelola dompet aman Anda pada Passport, Anda memiliki beberapa opsi. Dompet perangkat keras ini kompatibel dengan sebagian besar perangkat lunak manajemen dompet yang ada di pasaran, termasuk Sparrow Wallet, Specter Desktop, Nunchuk, Keeper, dan lain-lain.

Dalam tutorial ini, yang ditujukan untuk pengguna pemula dan menengah, kita akan menemukan cara menggunakan aplikasi Envoy dengan Passport Anda. Ini adalah cara termudah untuk memaksimalkan dompet perangkat keras Anda.

Jika Anda pengguna tingkat lanjut dan ingin menjelajahi fitur-fitur yang lebih kompleks, saya sarankan Anda melihat tutorial lain di mana kita mengonfigurasi Passport dengan Sparrow Wallet :

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

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

## Unduh aplikasi Envoy

Buka toko aplikasi Anda untuk mengunduh Envoy :


- Di [Google Play Store](https://play.google.com/store/apps/details?id=com.foundationdevices.envoy);
- Di [App Store](https://apps.apple.com/us/app/envoy-by-foundation/id1584811818);
- Pada [F-Cold] (https://foundation.xyz/fdroid/).

![Image](assets/fr/50.webp)

Anda juga dapat mengunduh file APK secara langsung [dari repositori GitHub Foundation] (https://github.com/Foundation-Devices/envoy/releases).

![Image](assets/fr/51.webp)

Setelah aplikasi terbuka, pilih "*Kelola Paspor*".

![Image](assets/fr/52.webp)

Pilih apakah Anda ingin mengaktifkan koneksi Tor untuk memperkuat kerahasiaan, lalu tekan "*Lanjutkan*".

![Image](assets/fr/53.webp)

Pilih "*Hubungkan Passport yang sudah ada*" jika Passport Anda sudah dikonfigurasi, atau "*Siapkan Passport baru*" jika Anda menginisialisasi dompet perangkat keras untuk pertama kalinya.

![Image](assets/fr/54.webp)

Menerima persyaratan penggunaan.

![Image](assets/fr/55.webp)

Anda kemudian akan diminta untuk memverifikasi keaslian Paspor. Klik "*Selanjutnya*".

![Image](assets/fr/56.webp)

## Paspor awal

Tekan tombol on/off di samping unit untuk menyalakannya.

![Image](assets/fr/04.webp)

Tekan tombol konfirmasi untuk mengakses menu berikutnya.

![Image](assets/fr/05.webp)

Dalam tutorial ini, kita akan menggunakan Envoy untuk mengelola dompet dengan keamanan Passport. Pilih "*Aplikasi Envoy*".

![Image](assets/fr/57.webp)

Klik "*Lanjutkan di Envoy*".

![Image](assets/fr/58.webp)

Langkah selanjutnya adalah memeriksa perangkat Anda. Hal ini akan mengonfirmasi keaslian Paspor Anda dan memastikan bahwa Paspor Anda belum dirusak dalam perjalanan. Anda akan diminta untuk memindai kode QR.

![Image](assets/fr/08.webp)

Pindai kode QR dinamis yang ditampilkan dalam aplikasi dengan Paspor Anda. Setelah pemindaian selesai, klik "*Selanjutnya*".

![Image](assets/fr/59.webp)

Kemudian gunakan ponsel Anda untuk memindai kode QR yang ditampilkan pada Paspor Anda.

![Image](assets/fr/60.webp)

Jika muncul pesan "*Paspor Anda aman*", ini mengonfirmasi bahwa dompet perangkat keras Anda asli. Sekarang Anda bisa menggunakannya untuk mengamankan dompet Bitcoin.

![Image](assets/fr/61.webp)

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

### Tanpa aplikasi Envoy

Untuk melakukan ini, gunakan kartu MicroSD yang disertakan dalam kotak Passport Anda (atau kartu lainnya), dan masukkan ke dalam komputer Anda. Unduh versi firmware terbaru dari [situs dokumentasi Foundation](https://docs.foundation.xyz/firmware-updates/passport/) atau [repositori GitHub](https://github.com/Foundation-Devices/passport2/releases).

![Image](assets/fr/21.webp)

Sebelum menginstalnya di perangkat Anda, kami sangat menyarankan Anda untuk memeriksa keaslian dan integritas firmware yang diunduh. Jika Anda memerlukan bantuan dalam hal ini, bacalah tutorial ini:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### Dengan aplikasi Envoy

Opsi lain yang lebih sederhana adalah menggunakan aplikasi Envoy secara langsung. Klik "*Unduh Firmware*".

![Image](assets/fr/62.webp)

Gunakan adaptor yang disertakan bersama Paspor untuk menyambungkan kartu MicroSD ke ponsel Anda.

![Image](assets/fr/63.webp)

Pilih kartu MicroSD di file explorer untuk menyimpan firmware.

![Image](assets/fr/64.webp)

Firmware sekarang telah disimpan. Lepaskan MicroSD dari smartphone Anda dan masukkan ke dalam Passport.

![Image](assets/fr/65.webp)

Penjelajah file Passport akan terbuka. Pilih file `vN.N.N-passport.bin`.

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

Paspor Anda sekarang akan menghasilkan "*Kode Cadangan*". Ini merupakan serangkaian angka yang dapat digunakan untuk mendekripsi cadangan dompet Anda yang tersimpan di MicroSD. Sistem pencadangan ini, khusus untuk perangkat Foundation, merupakan pencadangan tambahan untuk frasa mnemonik Anda, namun tidak kompatibel dengan perangkat lunak Bitcoin lainnya.

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

## Menyiapkan portofolio di Envoy

Dalam tutorial ini, saya akan menunjukkan kepada Anda cara menggunakan Passport dengan aplikasi Envoy. Namun, dompet perangkat keras ini juga kompatibel dengan Sparrow Wallet, Keeper, BlueWallet, Nunchuk, Specter, dan masih banyak lagi...

![Image](assets/fr/66.webp)

Gunakan aplikasi Envoy untuk memindai kode QR yang ditampilkan pada Paspor Anda.

![Image](assets/fr/67.webp)

Kunci publik Anda sekarang telah diimpor ke dalam aplikasi. Klik pada "*Validasi alamat penerima*".

![Image](assets/fr/68.webp)

Gunakan Paspor Anda untuk memindai alamat yang ditampilkan di Envoy.

![Image](assets/fr/69.webp)

Paspor Anda akan mengonfirmasi apakah dompet yang diimpor di Envoy valid. Konfirmasikan di aplikasi.

![Image](assets/fr/70.webp)

Sekarang Anda bisa mengakses informasi publik dompet Anda di Envoy, tetapi untuk membelanjakan bitcoin, Anda harus menggunakan Passport.

![Image](assets/fr/71.webp)

## Temukan menu Paspor

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

Anda juga dapat memasukkan kata sandi BIP39 atau menggunakan seed sementara.

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

## Menerima bitcoin

Setelah Passport Anda siap, Anda siap untuk menerima satoshi pertama Anda di dompet Bitcoin baru Anda. Untuk melakukannya, pada Envoy, klik akun "*Primary 0*" Anda.

![Image](assets/fr/72.webp)

Klik pada tombol "*Terima*".

![Image](assets/fr/73.webp)

Aplikasi Envoy akan menampilkan alamat kosong pertama yang tersedia di dompet Anda. Sebelum menggunakannya, mari kita periksa alamat tersebut di layar Passport untuk memastikan bahwa alamat tersebut benar-benar milik dompet Bitcoin kita. Pada menu "*Akun*" di Passport Anda, pilih "*Alat Akun*".

![Image](assets/fr/74.webp)

Klik "*Verifikasi Alamat*", lalu pindai kode QR yang ditampilkan pada Envoy.

![Image](assets/fr/75.webp)

Pastikan alamat yang ditampilkan di Paspor sama persis dengan alamat yang ditampilkan di Sparrow, dan muncul tulisan "*Verified*".

![Image](assets/fr/76.webp)

Sekarang Anda bisa menggunakannya untuk menerima bitcoin. Ketika transaksi disiarkan di jaringan, transaksi tersebut akan muncul di Envoy. Tunggu hingga Anda menerima konfirmasi yang cukup untuk menganggap transaksi tersebut sudah pasti.

![Image](assets/fr/77.webp)

## Kirim bitcoin

Sekarang setelah Anda memiliki beberapa sat dalam dompet Anda, Anda juga dapat mengirim beberapa. Untuk melakukannya, klik tombol "*Kirim*".

![Image](assets/fr/78.webp)

Masukkan alamat penerima, baik dengan menempelkannya secara langsung, atau dengan memindai kode QR dengan kamera ponsel cerdas Anda.

![Image](assets/fr/79.webp)

Tentukan jumlah yang ingin Anda kirim, lalu klik "*Konfirmasi*".

![Image](assets/fr/80.webp)

Pilih biaya transaksi sesuai dengan situasi pasar saat ini, lalu periksa informasi transaksi. Jika semuanya sudah benar, klik "*Tanda tangani dengan Paspor*".

![Image](assets/fr/81.webp)

Tambahkan label pada transaksi Anda untuk menyimpan catatan yang jelas tentang tujuannya.

![Image](assets/fr/82.webp)

Envoy kemudian menampilkan PSBT (*Transaksi Bitcoin yang Ditandatangani Sebagian*). Aplikasi telah membuat transaksi, tetapi masih belum memiliki tanda tangan untuk membuka kunci bitcoin yang digunakan dalam input. Tanda tangan ini hanya dapat dilakukan oleh Passport, yang menjadi tempat penyimpanan seed Anda dan memberikan akses ke private key yang diperlukan untuk menandatangani transaksi.

![Image](assets/fr/83.webp)

Pada Paspor Anda, akses menu "*Akun*" dan klik "*Tanda Tangan dengan Kode QR*".

![Image](assets/fr/84.webp)

Pindai PSBT (*Transaksi Bitcoin yang Ditandatangani Sebagian*) yang ditampilkan di Envoy.

![Image](assets/fr/85.webp)

Konfirmasikan bahwa alamat penerima dan jumlah yang dikirim sudah benar, lalu tekan tombol konfirmasi.

![Image](assets/fr/86.webp)

Periksa alamat pertukaran. Dalam contoh saya, tidak ada, karena transaksi ini mencakup satu keluaran.

![Image](assets/fr/87.webp)

Pastikan biaya tersebut sesuai dengan yang Anda pilih.

![Image](assets/fr/88.webp)

Jika semua informasi sudah benar, klik tombol konfirmasi untuk menandatangani transaksi.

![Image](assets/fr/89.webp)

Paspor Anda menunjukkan transaksi yang telah ditandatangani dalam bentuk kode QR.

![Image](assets/fr/90.webp)

Pada aplikasi Envoy, klik ikon kode QR, lalu pindai PSBT yang ditampilkan pada layar Paspor Anda.

![Image](assets/fr/91.webp)

Periksa detail transaksi Anda untuk terakhir kalinya. Jika semuanya sudah benar, tekan "*Kirim Transaksi*" untuk menyiarkannya di jaringan Bitcoin.

![Image](assets/fr/92.webp)

Transaksi Anda sekarang sedang menunggu konfirmasi. Anda dapat memantau statusnya langsung dari akun Anda.

![Image](assets/fr/93.webp)

Selamat, Anda sekarang tahu cara mengatur dan menggunakan Passport dengan aplikasi Envoy. Jika Anda merasa tutorial ini bermanfaat, saya akan berterima kasih jika Anda memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial Anda. Terima kasih telah berbagi!

Untuk informasi lebih lanjut, lihat tutorial kami tentang perangkat lunak Liana:

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
