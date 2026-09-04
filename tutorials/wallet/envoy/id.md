---
name: Envoy
description: Menyiapkan dan menggunakan Paspor dengan aplikasi Envoy
---
![cover](assets/cover.webp)

Envoy adalah aplikasi manajemen dompet Bitcoin yang dikembangkan oleh Foundation. Aplikasi ini dirancang khusus untuk digunakan dengan dompet perangkat keras Passport.

Passport "*Batch 2*" yang kami perkenalkan dalam tutorial ini dengan aplikasi Envoy adalah penerus dari edisi "*Founder's Edition*". Perangkat ini memiliki desain premium, layar warna berdefinisi tinggi, dan keyboard fisik yang ergonomis. Beroperasi dalam mode *Air-Gap*, memastikan kunci pribadi dompet kamu tetap sepenuhnya terisolasi, dengan pertukaran data yang dilakukan melalui kartu MicroSD atau kode QR. Perangkat ini dilengkapi dengan baterai isi ulang yang dapat dilepas, Nokia BL-5C berkapasitas 1200 mAh. Baterai non-proprietary ini mudah diganti karena model BL-5C tersedia luas di pasaran.

Untuk konektivitas, Passport dilengkapi dengan port MicroSD, port USB-C untuk pengisian daya, dan kamera belakang untuk memindai kode QR.

Dalam hal keamanan, Passport menggabungkan elemen yang aman, dan kode sumber perangkat ini sepenuhnya bersifat open source. Ia menawarkan semua fitur yang diharapkan dari dompet perangkat keras Bitcoin yang baik. Perlu dicatat bahwa Passport belum mendukung miniscript, tetapi fitur ini direncanakan untuk kuartal kedua tahun 2025.

Dengan harga $199, Passport diposisikan sebagai dompet perangkat keras kelas atas, bersaing dengan Coldcard Q, Jade Plus, Tezor Safe 5, dan model-model terbaik dari Ledger.


![Image](assets/fr/01.webp)

Untuk mengelola dompet aman kamu pada Passport, kamu memiliki beberapa opsi. Dompet perangkat keras ini kompatibel dengan sebagian besar perangkat lunak manajemen dompet yang ada di pasaran, termasuk Sparrow Wallet, Specter Desktop, Nunchuk, Keeper, dan lain-lain.

Dalam tutorial ini, yang ditujukan untuk pengguna pemula dan menengah, kita akan melihat cara menggunakan aplikasi Envoy dengan Passport kamu. Ini adalah cara termudah untuk memaksimalkan dompet perangkat keras kamu.

Jika kamu pengguna tingkat lanjut dan ingin menjelajahi fitur-fitur yang lebih kompleks, aku sarankan melihat tutorial lain di mana kita mengonfigurasi Passport dengan Sparrow Wallet :

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

## Membuka Kotak Paspor

Ketika kamu menerima Paspor, pastikan kotak dan segel pada karton masih utuh untuk mengonfirmasi bahwa paket tersebut belum dibuka. Verifikasi perangkat lunak terhadap keaslian dan integritas perangkat juga akan dilakukan saat perangkat diatur.

![Image](assets/fr/02.webp)

Isi kotak termasuk:


- Paspor;
- Selembar karton untuk menuliskan frasa mnemonik kamu;
- Kabel USB-C untuk pengisian daya ;
- Kartu microSD ;
- Dua adapter MicroSD ke Lightning atau USB-C ;
- Stiker.

Pada perangkat, kamu akan menemukan :


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

Buka toko aplikasi kamu untuk mengunduh Envoy :


- Di [Google Play Store](https://play.google.com/store/apps/details?id=com.foundationdevices.envoy);
- Di [App Store](https://apps.apple.com/us/app/envoy-by-foundation/id1584811818);
- Pada [F-Cold](https://foundation.xyz/fdroid/).

![Image](assets/fr/50.webp)

kamu juga dapat mengunduh file APK secara langsung [dari repositori GitHub Foundation](https://github.com/Foundation-Devices/envoy/releases).

![Image](assets/fr/51.webp)

Setelah aplikasi terbuka, pilih "*Kelola Paspor*".

![Image](assets/fr/52.webp)

Pilih apakah kamu ingin mengaktifkan koneksi Tor untuk memperkuat kerahasiaan, lalu tekan "*Lanjutkan*".

![Image](assets/fr/53.webp)

Pilih "*Hubungkan Passport yang sudah ada*" jika Passport kamu sudah dikonfigurasi, atau "*Siapkan Passport baru*" jika kamu menginisialisasi dompet perangkat keras untuk pertama kalinya.

![Image](assets/fr/54.webp)

Menerima persyaratan penggunaan.

![Image](assets/fr/55.webp)

Kamu kemudian akan diminta untuk memverifikasi keaslian Paspor. Klik "*Selanjutnya*".

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

Langkah selanjutnya adalah memeriksa perangkat kamu. Hal ini akan mengonfirmasi keaslian Passport kamu dan memastikan bahwa Passport kamu belum dirusak dalam perjalanan. Kamu akan diminta untuk memindai kode QR.

![Image](assets/fr/08.webp)

Pindai kode QR dinamis yang ditampilkan dalam aplikasi dengan Paspor kamu. Setelah pemindaian selesai, klik "*Selanjutnya*".

![Image](assets/fr/59.webp)

Kemudian gunakan ponsel kamu untuk memindai kode QR yang ditampilkan pada Paspor.

![Image](assets/fr/60.webp)

Jika muncul pesan "*Paspor Anda aman*", ini mengonfirmasi bahwa dompet perangkat keras kamu asli. Sekarang kamu bisa menggunakannya untuk mengamankan dompet Bitcoin.

![Image](assets/fr/61.webp)

Konfirmasikan hasil tes pada Paspor.

![Image](assets/fr/14.webp)

## Mengatur kode PIN

Berikutnya adalah langkah kode PIN. Kode PIN akan membuka kunci Passport kamu. Oleh karena itu, kode PIN memberikan perlindungan terhadap akses fisik yang tidak sah. Kode PIN tidak terlibat dalam penurunan kunci kriptografi dompet kamu. Jadi, bahkan tanpa akses ke kode PIN, kepemilikan *seedphrase* 12 atau 24 kata kamu akan memungkinkan kamu mendapatkan kembali akses ke bitcoin kamu.

![Image](assets/fr/15.webp)

Kami menyarankan untuk memilih kode PIN yang seacak mungkin. Selain itu, pastikan untuk menyimpan kode ini di tempat yang terpisah dari tempat penyimpanan Passport kamu (misalnya di pengelola kata sandi).

Kamu dapat memilih kode PIN antara 6 dan 12 digit. Aku menyarankan membuatnya sepanjang mungkin.

Gunakan papan tombol untuk memasukkan nomor PIN kamu. Setelah selesai, klik tombol konfirmasi.

![Image](assets/fr/16.webp)

Konfirmasikan PIN kamu untuk kedua kalinya.

![Image](assets/fr/17.webp)

Kode PIN kamu telah terdaftar.

![Image](assets/fr/18.webp)

## Perbarui firmware Paspor

Dompet perangkat keras kamu menyarankan agar kamu memperbarui firmware-nya. Aku sarankan segera memperbarui untuk mendapatkan manfaat dari peningkatan dan perbaikan yang dibawa oleh versi terbaru. Untuk melanjutkan, klik tombol konfirmasi di sebelah kanan.

![Image](assets/fr/19.webp)

Passport kamu siap menerima firmware baru melalui kartu MicroSD.

![Image](assets/fr/20.webp)

### Tanpa aplikasi Envoy

Untuk melakukan ini, gunakan kartu MicroSD yang disertakan dalam kotak Passport kamu (atau kartu lainnya), dan masukkan ke dalam komputer kamu. Unduh versi firmware terbaru dari [situs dokumentasi Foundation](https://docs.foundation.xyz/firmware-updates/passport/) atau [repositori GitHub](https://github.com/Foundation-Devices/passport2/releases).

![Image](assets/fr/21.webp)

Sebelum menginstalnya di perangkatmu, kami sangat menyarankanmu untuk memeriksa keaslian dan integritas firmware yang diunduh. Jika kamu memerlukan bantuan dalam hal ini, bacalah tutorial ini:

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### Dengan aplikasi Envoy

Opsi lain yang lebih sederhana adalah menggunakan aplikasi Envoy secara langsung. Klik "*Unduh Firmware*".

![Image](assets/fr/62.webp)

Gunakan adaptor yang disertakan bersama Paspor untuk menyambungkan kartu MicroSD ke ponsel kamu.

![Image](assets/fr/63.webp)

Pilih kartu MicroSD di file explorer untuk menyimpan firmware.

![Image](assets/fr/64.webp)

Firmware sekarang telah disimpan. Lepaskan MicroSD dari smartphone kamu dan masukkan ke dalam Passport.

![Image](assets/fr/65.webp)

Penjelajah file Passport akan terbuka. Pilih file `vN.N.N-passport.bin`.

![Image](assets/fr/22.webp)

Klik "*Pilih*".

![Image](assets/fr/23.webp)

Kemudian konfirmasikan pemasangan firmware.

![Image](assets/fr/24.webp)

Harap tunggu hingga pembaruan selesai.

![Image](assets/fr/25.webp)

Setelah pembaruan selesai, masukkan kode PIN kamu untuk membuka kunci perangkat dan melanjutkan konfigurasi.

![Image](assets/fr/26.webp)

## Membuat dompet Bitcoin baru

Sekarang saatnya membuat dompet Bitcoin baru. Klik pada tombol konfirmasi.

![Image](assets/fr/27.webp)

Untuk membuat portofolio baru, klik "*Buat Bibit Baru*".

![Image](assets/fr/28.webp)

Kamu dapat memilih antara *seedphrase* 12 atau 24 kata. Keamanan yang ditawarkan oleh kedua opsi ini serupa, sehingga kamu dapat memilih salah satu yang paling mudah disimpan, yaitu 12 kata.

![Image](assets/fr/29.webp)

Klik "*Lanjutkan*".

![Image](assets/fr/30.webp)

Passport kamu sekarang akan menghasilkan "*Kode Cadangan*". Ini merupakan serangkaian angka yang dapat digunakan untuk mendekripsi cadangan dompet kamu yang tersimpan di MicroSD. Sistem pencadangan ini, khusus untuk perangkat Foundation, merupakan pencadangan tambahan untuk *seedphrase* kamu, namun tidak kompatibel dengan perangkat lunak Bitcoin lainnya.

Jika kamu memutuskan untuk menggunakan "*Kode Cadangan*" ini, pastikan menyimpannya di lokasi yang berbeda dengan MicroSD kamu yang berisi cadangan terenkripsi dompet kamu. Namun, kamu dapat memilih untuk tidak menggunakan sistem ini jika merasa bahwa cadangan *seedphrase* kamu sudah cukup.

![Image](assets/fr/31.webp)

Masukkan "*Kode Cadangan*" untuk mengonfirmasi bahwa kamu telah menyimpannya dengan benar.

![Image](assets/fr/32.webp)

Jika MicroSD telah dimasukkan, cadangan terenkripsi portofolio kamu telah disimpan di sana.

![Image](assets/fr/33.webp)

Passport kamu akan menampilkan *seedphrase* 12 kata. Kata-kata ini memberikan kamu akses penuh dan tidak terbatas ke semua bitcoin kamu. Siapa pun yang memiliki *seedphrase* ini dapat mencuri dana kamu, bahkan tanpa akses fisik ke Passport kamu.

*Seedphrase* 12 kata ini mengembalikan akses ke bitcoin kamu jika terjadi kehilangan, pencurian, atau kerusakan pada Passport kamu. Oleh karena itu, sangat penting untuk menyimpannya dengan hati-hati dan di lokasi yang aman.

Kamu bisa menuliskannya pada karton yang disertakan dalam kotak, atau untuk keamanan tambahan, aku sarankan mengukirnya pada baja tahan karat untuk melindunginya dari kebakaran, banjir, atau keruntuhan.

Klik tombol konfirmasi untuk melihat *seedphrase* kamu.

![Image](assets/fr/34.webp)

Untuk informasi lebih lanjut mengenai cara yang tepat untuk menyimpan dan mengelola *seedphrase* kamu, aku sangat merekomendasikan mengikuti tutorial lainnya, khususnya jika kamu seorang pemula:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Tentu saja, kamu tidak boleh membagikan kata-kata ini di Internet, seperti yang aku lakukan dalam tutorial ini. Portofolio contoh ini hanya akan digunakan di Testnet dan akan dihapus di akhir tutorial.

Buatlah cadangan fisik dari kalimat ini.

![Image](assets/fr/35.webp)

Paspor kamu telah berhasil dikonfigurasi. Klik tombol konfirmasi untuk melanjutkan.

![Image](assets/fr/36.webp)

## Menyiapkan portofolio di Envoy

Dalam tutorial ini, aku akan menunjukkan cara menggunakan Passport dengan aplikasi Envoy. Namun, dompet perangkat keras ini juga kompatibel dengan Sparrow Wallet, Keeper, BlueWallet, Nunchuk, Specter, dan masih banyak lagi...

![Image](assets/fr/66.webp)

Gunakan aplikasi Envoy untuk memindai kode QR yang ditampilkan pada Paspor kamu.

![Image](assets/fr/67.webp)

Kunci publik Anda sekarang telah diimpor ke dalam aplikasi. Klik pada "*Validasi alamat penerima*".

![Image](assets/fr/68.webp)

Gunakan Paspor kamu untuk memindai alamat yang ditampilkan di Envoy.

![Image](assets/fr/69.webp)

Paspor kamu akan mengonfirmasi apakah dompet yang diimpor di Envoy valid. Konfirmasikan di aplikasi.

![Image](assets/fr/70.webp)

Sekarang kamu bisa mengakses informasi publik dompet Anda di Envoy, tetapi untuk membelanjakan bitcoin, Anda harus menggunakan Passport.

![Image](assets/fr/71.webp)

## Temukan menu Passport

Antarmuka Passport kamu memiliki tiga menu utama:

- "*Rekening*";
- "*Lebih banyak*";
- "*Pengaturan*".

Untuk menavigasi di antara menu-menu ini, gunakan panah kiri dan kanan pada directional pad.

### *Menu "Akun"*

Pada menu "*Akun*", kamu akan menemukan fitur-fitur utama dompet Bitcoin kamu. Kamu bisa menandatangani transaksi melalui kamera atau melalui port MicroSD.

![Image](assets/fr/37.webp)

Submenu "*Account Tools*" menawarkan opsi seperti memverifikasi alamat, menandatangani pesan, atau melihat alamat dalam portofolio.

![Image](assets/fr/38.webp)

Pada submenu "*Manage Account*", kamu dapat menghubungkan dompet Bitcoin kamu ke perangkat lunak manajemen dompet (yang akan kita bahas pada langkah selanjutnya dalam tutorial ini), atau melihat dan mengganti nama akun kamu.

![Image](assets/fr/39.webp)

### Menu "Lainnya

Di menu "*Lebih Banyak*", kamu bisa membuat akun baru dalam portofolio milikmu, yang ditautkan ke frasa mnemonik yang sama.

![Image](assets/fr/40.webp)

Kamu juga dapat memasukkan kata sandi BIP39 atau menggunakan seed sementara.

![Image](assets/fr/41.webp)

### Menu "Pengaturan

Di menu "*Pengaturan*", kamu akan menemukan semua pengaturan dompet dan perangkat kamu.

![Image](assets/fr/42.webp)

Submenu "*Perangkat*" memberi kamu opsi untuk menyesuaikan kecerahan layar, mengatur penundaan sebelum penguncian otomatis, mengubah kode PIN, atau mengganti nama perangkat.

![Image](assets/fr/43.webp)

Submenu "*Backup*" memungkinkan kamu mengekspor cadangan portofolio terenkripsi, memeriksa validitas cadangan yang sudah ada, atau mencari "*Kode Cadangan*" lagi.

![Image](assets/fr/44.webp)

Submenu "*Firmware*" digunakan untuk memperbarui firmware Passport kamu. Kami menyarankan melakukan pembaruan ini secara teratur untuk mendapatkan manfaat dari perbaikan dan fitur terbaru.

![Image](assets/fr/45.webp)

Submenu "*Bitcoin*" memungkinkan kamu untuk mengubah unit yang ditampilkan (BTC atau satoshi), mengelola dompet Multisig yang mungkin kamu miliki, atau beralih ke mode "*Testnet*".

![Image](assets/fr/46.webp)

Dalam "*Advanced*", kamu dapat melihat kata-kata *seedphrase* kamu, melakukan tindakan pada MicroSD yang dimasukkan, mengatur ulang Passport ke pengaturan pabrik, atau melakukan pemeriksaan keaslian, seperti yang dilakukan sebelumnya.

![Image](assets/fr/47.webp)

Kamu dapat mengaktifkan "*Security Words*", sebuah fitur yang menambahkan lapisan keamanan dengan menampilkan dua kata tertentu ketika membuka kunci perangkat setelah memasukkan empat digit pertama kode PIN. Kata-kata ini, yang akan disimpan selama konfigurasi, memastikan bahwa Passport belum diganti atau dirusak. Jika terjadi perbedaan di kemudian hari, aku menyarankan untuk tidak menggunakan perangkat. Aku sarankan mengaktifkan opsi ini untuk mencegah sebagian besar risiko gangguan fisik pada perangkat.

![Image](assets/fr/48.webp)

Terakhir, sub-menu "*Extensions*" memungkinkanmu mengaktifkan fungsi yang spesifik untuk penggunaan alat tertentu, misalnya, protokol coinjoin Whirlpool.

![Image](assets/fr/49.webp)

## Menerima bitcoin

Setelah Passport kamu siap, kamu siap untuk menerima satoshi pertama kamu di dompet Bitcoin baru kamu. Untuk melakukannya, pada Envoy, klik akun "*Primary 0*" kamu.

![Image](assets/fr/72.webp)

Klik pada tombol "*Terima*".

![Image](assets/fr/73.webp)

Aplikasi Envoy akan menampilkan alamat kosong pertama yang tersedia di dompet kamu. Sebelum menggunakannya, mari kita periksa alamat tersebut di layar Passport untuk memastikan bahwa alamat tersebut benar-benar milik dompet Bitcoin kita. Pada menu "*Akun*" di Passport kamu, pilih "*Alat Akun*".

![Image](assets/fr/74.webp)

Klik "*Verifikasi Alamat*", lalu pindai kode QR yang ditampilkan pada Envoy.

![Image](assets/fr/75.webp)

Pastikan alamat yang ditampilkan di Paspor sama persis dengan alamat yang ditampilkan di Sparrow, dan muncul tulisan "*Verified*".

![Image](assets/fr/76.webp)

Sekarang kamu bisa menggunakannya untuk menerima bitcoin. Ketika transaksi disiarkan di jaringan, transaksi tersebut akan muncul di Envoy. Tunggu hingga kamu menerima konfirmasi yang cukup untuk menganggap transaksi tersebut sudah pasti.

![Image](assets/fr/77.webp)

## Kirim bitcoin

Sekarang setelah kamu memiliki beberapa satoshi di dompet kamu, kamu juga dapat mengirim beberapa. Untuk melakukannya, klik tombol "*Kirim*".

![Image](assets/fr/78.webp)

Masukkan alamat penerima, baik dengan menempelkannya secara langsung, atau dengan memindai kode QR dengan kamera ponsel cerdas kamu.

![Image](assets/fr/79.webp)

Tentukan jumlah yang ingin kamu kirim, lalu klik "*Konfirmasi*".

![Image](assets/fr/80.webp)

Pilih biaya transaksi sesuai dengan situasi pasar saat ini, lalu periksa informasi transaksi. Jika semuanya sudah benar, klik "*Tanda tangani dengan Paspor*".

![Image](assets/fr/81.webp)

Tambahkan label pada transaksi kamu untuk menyimpan catatan yang jelas tentang tujuannya.

![Image](assets/fr/82.webp)

Envoy kemudian menampilkan PSBT (*Partially Signed Bitcoin Transaction*). Aplikasi telah membuat transaksi, tetapi masih belum memiliki tanda tangan untuk membuka kunci bitcoin yang digunakan dalam input. Tanda tangan ini hanya dapat dilakukan oleh Passport, yang menjadi tempat penyimpanan *seed* kamu dan memberikan akses ke private key yang diperlukan untuk menandatangani transaksi.

![Image](assets/fr/83.webp)

Pada Paspor kamu, akses menu "*Akun*" dan klik "*Tanda Tangan dengan Kode QR*".

![Image](assets/fr/84.webp)

Pindai PSBT (*Transaksi Bitcoin yang Ditandatangani Sebagian*) yang ditampilkan di Envoy.

![Image](assets/fr/85.webp)

Konfirmasikan bahwa alamat penerima dan jumlah yang dikirim sudah benar, lalu tekan tombol konfirmasi.

![Image](assets/fr/86.webp)

Periksa alamat pertukaran. Dalam contoh ini, tidak ada, karena transaksi ini mencakup satu keluaran.

![Image](assets/fr/87.webp)

Pastikan biaya tersebut sesuai dengan yang kamu pilih.

![Image](assets/fr/88.webp)

Jika semua informasi sudah benar, klik tombol konfirmasi untuk menandatangani transaksi.

![Image](assets/fr/89.webp)

Paspor kamu menunjukkan transaksi yang telah ditandatangani dalam bentuk kode QR.

![Image](assets/fr/90.webp)

Pada aplikasi Envoy, klik ikon kode QR, lalu pindai PSBT yang ditampilkan pada layar Paspor kamu.

![Image](assets/fr/91.webp)

Periksa detail transaksi kamu untuk terakhir kalinya. Jika semuanya sudah benar, tekan "*Kirim Transaksi*" untuk menyiarkannya di jaringan Bitcoin.

![Image](assets/fr/92.webp)

Transaksi kami sekarang sedang menunggu konfirmasi. Kamu dapat memantau statusnya langsung dari akun Anda.

![Image](assets/fr/93.webp)

Selamat, kamu sekarang tahu cara mengatur dan menggunakan Passport dengan aplikasi Envoy. Jika kamu merasa tutorial ini bermanfaat, aku akan berterima kasih jika kamu memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial kamu. Terima kasih telah berbagi!

Untuk informasi lebih lanjut, lihat tutorial kami tentang perangkat lunak Liana:

https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
