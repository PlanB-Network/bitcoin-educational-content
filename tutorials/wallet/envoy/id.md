---
name: Utusan
description: Menyiapkan dan menggunakan Passport dengan aplikasi Envoy
---
![cover](assets/cover.webp)

Envoy adalah aplikasi manajemen dompet Bitcoin yang dikembangkan oleh Foundation. Aplikasi ini dibuat khusus untuk digunakan bersama dompet perangkat keras Passport.

Passport *Batch 2* yang dibahas dalam tutorial ini adalah penerus dari edisi *Founder's Edition.* Perangkat ini hadir dengan desain premium, layar berwarna beresolusi tinggi, dan keyboard fisik yang nyaman digunakan. Beroperasi dalam mode *Air-Gap,* Passport memastikan kunci pribadimu tetap sepenuhnya terisolasi, dengan pertukaran data yang dilakukan lewat kartu MicroSD atau kode QR. Perangkat ini juga dilengkapi baterai isi ulang yang bisa dilepas, yaitu Nokia BL-5C berkapasitas 1200 mAh. Baterai non-proprietary ini mudah diganti karena tipe BL-5C banyak dijual di pasaran.

Untuk konektivitas, Passport punya port MicroSD, port USB-C untuk pengisian daya, dan kamera belakang untuk memindai kode QR.

Dari sisi keamanan, Passport menggabungkan elemen keamanan tingkat tinggi, dan seluruh kode sumbernya bersifat open source. Ia menawarkan semua fitur penting yang diharapkan dari sebuah dompet perangkat keras Bitcoin. Perlu dicatat, Passport belum mendukung miniscript, tapi fitur ini direncanakan hadir pada kuartal kedua tahun 2025.

Dengan harga $199, Passport diposisikan sebagai dompet perangkat keras kelas atas yang bersaing dengan Coldcard Q, Jade Plus, Trezor Safe 5, dan model-model terbaik dari Ledger.

![Image](assets/fr/01.webp)

Untuk mengelola dompet amannya di Passport, kamu punya beberapa opsi. Dompet perangkat keras ini kompatibel dengan banyak perangkat lunak manajemen dompet populer di pasaran, termasuk Sparrow Wallet, Specter Desktop, Nunchuk, Keeper, dan lainnya.

Dalam tutorial ini, yang ditujukan untuk pengguna pemula dan menengah, kita akan belajar cara menggunakan aplikasi Envoy bersama Passport kamu. Ini adalah cara paling mudah untuk memaksimalkan penggunaan dompet perangkat kerasmu.

Kalau kamu termasuk pengguna tingkat lanjut dan ingin menjelajahi fitur-fitur yang lebih kompleks, aku sarankan kamu cek tutorial lain yang membahas cara mengonfigurasi Passport dengan Sparrow Wallet:

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

## Membuka Kotak Paspor

Ketika Anda menerima Paspor, pastikan kotak dan segel pada karton masih utuh untuk mengonfirmasi bahwa paket tersebut belum dibuka. Verifikasi perangkat lunak terhadap keaslian dan integritas perangkat juga akan dilakukan saat perangkat diatur.

![Image](assets/fr/02.webp)

Isi kotak termasuk:


- Paspor;
- Selembar karton untuk menuliskan frasa mnemonik;
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
- Pada [F-Cold] (https://foundation.xyz/fdroid/).

![Image](assets/fr/50.webp)

Kamu juga dapat mengunduh file APK secara langsung [dari repositori GitHub Foundation] (https://github.com/Foundation-Devices/envoy/releases).

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

Langkah selanjutnya adalah memverifikasi perangkatmu. Proses ini akan memastikan keaslian Passport dan menjamin bahwa perangkatmu tidak mengalami gangguan apa pun selama pengiriman. Kamu akan diminta untuk memindai kode QR.

![Image](assets/fr/08.webp)

Pindai kode QR dinamis yang muncul di aplikasi menggunakan Passport kamu. Setelah pemindaian selesai, tekan *Selanjutnya.*
![Image](assets/fr/59.webp)

Kemudian gunakan ponsel kamu untuk memindai kode QR yang ditampilkan pada Paspor Anda.

![Image](assets/fr/60.webp)

Jika muncul pesan "*Paspor Anda aman*", ini mengonfirmasi bahwa dompet perangkat keras kamu asli. Sekarang kamu bisa menggunakannya untuk mengamankan dompet Bitcoin.

![Image](assets/fr/61.webp)

Konfirmasikan hasil tes pada Paspor kamu.

![Image](assets/fr/14.webp)

## Mengatur kode PIN

Berikutnya adalah langkah pembuatan kode PIN. Kode PIN digunakan untuk membuka kunci Passport kamu dan melindunginya dari akses fisik yang tidak sah. Kode PIN ini tidak digunakan dalam proses penurunan kunci kriptografi dompetmu. Jadi, meskipun seseorang tidak punya akses ke kode PIN, selama kamu masih memiliki seedphrase 12 atau 24 kata, kamu tetap bisa memulihkan akses ke bitcoinmu.

![Image](assets/fr/15.webp)

Disarankan untuk memilih kode PIN yang benar-benar acak. Selain itu, pastikan kamu menyimpannya di tempat yang terpisah dari Passport kamu, misalnya di pengelola kata sandi.

Kamu dapat memilih kode PIN antara 6 dan 12 digit. Aku menyarankan kamu untuk membuatnya sepanjang mungkin.

Gunakan papan tombol untuk memasukkan nomor PIN. Setelah selesai, klik tombol konfirmasi.

![Image](assets/fr/16.webp)

Konfirmasikan PIN kamu untuk kedua kalinya.

![Image](assets/fr/17.webp)

Kode PIN telah terdaftar.

![Image](assets/fr/18.webp)

## Perbarui firmware Paspor

Dompet perangkat kerasmu mungkin menyarankan untuk memperbarui firmware. Aku sarankan kamu segera melakukannya agar bisa mendapatkan peningkatan dan perbaikan dari versi terbaru. Untuk melanjutkan, tekan tombol konfirmasi di sisi kanan.

![Image](assets/fr/19.webp)

Passport kamu siap menerima firmware baru melalui kartu MicroSD.

![Image](assets/fr/20.webp)

### Tanpa aplikasi Envoy

Untuk melakukan ini, gunakan kartu MicroSD yang disertakan dalam kotak Passport kamu (atau kartu lainnya), dan masukkan ke dalam komputer kamu. Unduh versi firmware terbaru dari [situs dokumentasi Foundation](https://docs.foundation.xyz/firmware-updates/passport/) atau [repositori GitHub](https://github.com/Foundation-Devices/passport2/releases).

![Image](assets/fr/21.webp)

Sebelum menginstalnya di perangkat kamu, kami sangat menyarankan kamu untuk memeriksa keaslian dan integritas firmware yang diunduh. Jika kamu memerlukan bantuan dalam hal ini, bacalah tutorial ini:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### Dengan aplikasi Envoy

Pilihan lain yang lebih sederhana adalah menggunakan aplikasi Envoy secara langsung. Klik "*Unduh Firmware*".

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

Kamu bisa memilih antara seedphrase 12 atau 24 kata. Tingkat keamanan keduanya sebenarnya sama, jadi kamu bisa memilih yang paling mudah disimpan biasanya 12 kata.

![Image](assets/fr/29.webp)

Klik "*Lanjutkan*".

![Image](assets/fr/30.webp)

Passport kamu sekarang akan membuat Kode Cadangan. Ini adalah rangkaian angka yang bisa digunakan untuk mendekripsi cadangan dompetmu yang tersimpan di MicroSD. Sistem pencadangan ini, yang khusus dibuat oleh Foundation, berfungsi sebagai cadangan tambahan untuk seedphrase kamu, namun tidak kompatibel dengan perangkat lunak Bitcoin lainnya.

Kalau kamu memutuskan untuk menggunakan Kode Cadangan ini, pastikan menyimpannya di tempat yang berbeda dari MicroSD yang berisi cadangan terenkripsi dompetmu. Tapi, kamu juga bisa memilih untuk tidak menggunakan sistem ini jika merasa seedphrase sudah cukup sebagai cadangan.

![Image](assets/fr/31.webp)

Masukkan "*Kode Cadangan*" untuk mengonfirmasi bahwa kamu telah menyimpannya dengan benar.

![Image](assets/fr/32.webp)

Jika MicroSD telah dimasukkan, cadangan terenkripsi portofolio kamu telah disimpan di sana.

![Image](assets/fr/33.webp)

Passport kamu akan menampilkan seedphrase berisi 12 kata. Seedphrase ini memberi kamu akses penuh dan tidak terbatas ke semua bitcoinmu. Siapa pun yang memiliki frasa ini bisa mencuri dana kamu, bahkan tanpa harus menyentuh Passport-mu secara fisik.

Seedphrase 12 kata ini bisa memulihkan akses ke bitcoinmu jika Passport hilang, dicuri, atau rusak. Karena itu, sangat penting untuk menyimpannya dengan hati-hati dan menaruhnya di tempat yang benar-benar aman.

Kamu bisa menuliskannya di kartu yang disertakan dalam kotak, atau untuk keamanan ekstra, sebaiknya ukir seedphrase tersebut di lempengan baja tahan karat agar terlindungi dari kebakaran, banjir, atau keruntuhan.

Tekan tombol konfirmasi untuk menampilkan seedphrase kamu.

![Image](assets/fr/34.webp)

Untuk informasi lebih lanjut mengenai cara yang tepat untuk menyimpan dan mengelola frasa mnemonik kamu, aku sangat merekomendasikan untuk mengikuti tutorial lainnya, khususnya jika kamu seorang pemula:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

tentu saja, kamu tidak boleh membagikan kata-kata ini di Internet, seperti yang aku lakukan dalam tutorial ini. Portofolio contoh ini hanya akan digunakan di Testnet dan akan dihapus di akhir tutorial.**_

Buatlah cadangan fisik dari kalimat ini.

![Image](assets/fr/35.webp)

Paspor kamu telah berhasil dikonfigurasi. Klik tombol konfirmasi untuk melanjutkan.

![Image](assets/fr/36.webp)

## Menyiapkan portofolio di Envoy

Dalam tutorial ini, aku akan menunjukkan cara menggunakan Passport dengan aplikasi Envoy. Namun, dompet perangkat keras ini juga kompatibel dengan Sparrow Wallet, Keeper, BlueWallet, Nunchuk, Specter, dan banyak lagi lainnya.

![Image](assets/fr/66.webp)

Gunakan aplikasi Envoy untuk memindai kode QR yang ditampilkan pada Paspor kamu.

![Image](assets/fr/67.webp)

Kunci publik kamu sekarang telah diimpor ke dalam aplikasi. Klik pada "*Validasi alamat penerima*".

![Image](assets/fr/68.webp)

Gunakan Paspor kamu untuk memindai alamat yang ditampilkan di Envoy.

![Image](assets/fr/69.webp)

Paspor Anda akan mengonfirmasi apakah dompet yang diimpor di Envoy valid. Konfirmasikan di aplikasi.

![Image](assets/fr/70.webp)

Sekarang kamu bisa mengakses informasi publik dompet Anda di Envoy, tetapi untuk membelanjakan bitcoin, Anda harus menggunakan Passport.

![Image](assets/fr/71.webp)

## Temukan menu Paspor

Antarmuka Passport kamu memiliki tiga menu utama:


- "*Rekening*";
- "*Lebih banyak*";
- "*Pengaturan*".

Untuk menavigasi di antara menu-menu ini, gunakan panah kiri dan kanan pada directional pad.

### *Menu "Akun*

Pada menu "*Account*", kamu akan menemukan fitur-fitur utama dompet Bitcoin kamu. Kamu bisa menandatangani transaksi melalui kamera atau melalui port MicroSD.

![Image](assets/fr/37.webp)

Submenu "*Account Tools*" menawarkan opsi seperti memverifikasi alamat, menandatangani pesan, atau melihat alamat dalam portofolio kamu.

![Image](assets/fr/38.webp)

Pada submenu "*Manage Account*", kamu dapat menghubungkan dompet Bitcoin kamu ke perangkat lunak manajemen dompet (yang akan kita bahas pada langkah selanjutnya dalam tutorial ini), atau melihat dan mengganti nama akun kamu.

![Image](assets/fr/39.webp)

### Menu "Lainnya

Di menu "*Lebih Banyak*", kamu bisa membuat akun baru dalam portofolio kamu, yang ditautkan ke frasa mnemonik yang sama.

![Image](assets/fr/40.webp)

Kamu juga dapat memasukkan kata sandi BIP39 atau menggunakan seed sementara.

![Image](assets/fr/41.webp)

### Menu "Pengaturan

Di menu "*Pengaturan*", kamu akan menemukan semua pengaturan dompet dan perangkat kamu.

![Image](assets/fr/42.webp)

Submenu "*Perangkat*" memberi kamu opsi untuk menyesuaikan kecerahan layar, mengatur penundaan sebelum penguncian otomatis, mengubah kode PIN, atau mengganti nama perangkat.

![Image](assets/fr/43.webp)

Submenu "*Backup*" memungkinkan kamu mengekspor cadangan portofolio terenkripsi, memeriksa validitas cadangan yang sudah ada, atau mencari "*Backup Code*" lagi.

![Image](assets/fr/44.webp)

Sub-menu "*Firmware*" untuk memperbarui firmware Passport kamu. Kami menyarankan agar kamu melakukan pembaruan ini secara teratur untuk mendapatkan manfaat dari perbaikan dan fitur terbaru.

![Image](assets/fr/45.webp)

Sub-menu "*Bitcoin*" memungkinkan kamu untuk mengubah unit yang ditampilkan (BTC atau satoshi), mengelola dompet Multisig yang mungkin, atau beralih ke mode "*Testnet*".

![Image](assets/fr/46.webp)

Dalam "*Advanced*", kamu dapat melihat kata-kata frasa mnemonik kamu, melakukan tindakan pada MicroSD yang dimasukkan, mengatur ulang Passport ke pengaturan pabrik, atau melakukan pemeriksaan keaslian, seperti yang dilakukan sebelumnya.

![Image](assets/fr/47.webp)

Kamu dapat mengaktifkan "*Security Words*", sebuah fitur yang menambahkan lapisan keamanan dengan menampilkan dua kata tertentu ketika membuka kunci perangkat setelah memasukkan empat digit pertama kode PIN. Kata-kata ini, yang akan disimpan selama konfigurasi, memastikan bahwa Passport belum diganti atau dirusak. Jika terjadi perbedaan di kemudian hari, kami menyarankan kamu untuk tidak menggunakan perangkat. Aku menyarankan kamu untuk mengaktifkan opsi ini untuk mencegah sebagian besar risiko gangguan fisik pada perangkat.

![Image](assets/fr/48.webp)

Terakhir, sub-menu "*Extensions*" memungkinkanmu mengaktifkan fungsi yang spesifik untuk penggunaan alat tertentu, misalnya, protokol coinjoin Whirlpool.

![Image](assets/fr/49.webp)

## Menerima bitcoin

Setelah Passport siap, kamu siap untuk menerima satoshi pertama di dompet Bitcoin baru kamu. Untuk melakukannya, pada Envoy, klik akun "*Primary 0*" kamu.

![Image](assets/fr/72.webp)

Klik pada tombol "*Terima*".

![Image](assets/fr/73.webp)

Aplikasi Envoy akan menampilkan alamat kosong pertama yang tersedia di dompet kamu. Sebelum menggunakannya, mari kita periksa alamat tersebut di layar Passport untuk memastikan bahwa alamat tersebut benar-benar milik dompet Bitcoin kita. Pada menu "*Akun*" di Passport kamu, pilih "*Alat Akun*".

![Image](assets/fr/74.webp)

Klik "*Verifikasi Alamat*", lalu pindai kode QR yang ditampilkan pada Envoy.

![Image](assets/fr/75.webp)

Pastikan alamat yang ditampilkan di Paspor sama persis dengan alamat yang ditampilkan di Sparrow, dan muncul tulisan "*Verified*".

![Image](assets/fr/76.webp)

Sekarang kamu bisa menggunakannya untuk menerima bitcoin. Ketika transaksi disiarkan ke jaringan, transaksi itu akan muncul di Envoy. Tunggu sampai kamu menerima konfirmasi yang cukup agar transaksi dianggap sudah pasti.

![Image](assets/fr/77.webp)

## Kirim bitcoin

Sekarang setelah Anda memiliki beberapa sat dalam dompet kamu, kamu juga dapat mengirim beberapa. Untuk melakukannya, klik tombol "*Kirim*".

![Image](assets/fr/78.webp)

Masukkan alamat penerima, baik dengan menempelkannya secara langsung, atau dengan memindai kode QR dengan kamera ponsel cerdas kamu.

![Image](assets/fr/79.webp)

Tentukan jumlah yang ingin kamu kirim, lalu klik "*Konfirmasi*".

![Image](assets/fr/80.webp)

Pilih biaya transaksi sesuai dengan situasi pasar saat ini, lalu periksa informasi transaksi. Jika semuanya sudah benar, klik "*Tanda tangani dengan Paspor*".

![Image](assets/fr/81.webp)

Tambahkan label pada transaksi kamu untuk menyimpan catatan yang jelas tentang tujuannya.

![Image](assets/fr/82.webp)

Envoy kemudian menampilkan PSBT (*Transaksi Bitcoin yang Ditandatangani Sebagian*). Aplikasi telah membuat transaksi, tetapi masih belum memiliki tanda tangan untuk membuka kunci bitcoin yang digunakan dalam input. Tanda tangan ini hanya dapat dilakukan oleh Passport, yang menjadi tempat penyimpanan seed kamu dan memberikan akses ke private key yang diperlukan untuk menandatangani transaksi.

![Image](assets/fr/83.webp)

Pada Paspor kamu, akses menu "*Akun*" dan klik "*Tanda Tangan dengan Kode QR*".

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

Paspor kamu menunjukkan transaksi yang telah ditandatangani dalam bentuk kode QR.

![Image](assets/fr/90.webp)

Pada aplikasi Envoy, klik ikon kode QR, lalu pindai PSBT yang ditampilkan pada layar Paspor kamu.

![Image](assets/fr/91.webp)

Periksa detail transaksi kamu untuk terakhir kalinya. Jika semuanya sudah benar, tekan "*Kirim Transaksi*" untuk menyiarkannya di jaringan Bitcoin.

![Image](assets/fr/92.webp)

Transaksi kamu sekarang sedang menunggu konfirmasi. Kamu dapat memantau statusnya langsung dari akun Anda.

![Image](assets/fr/93.webp)

Selamat, sekarang kamu sudah tahu cara mengatur dan menggunakan Passport dengan aplikasi Envoy. Kalau kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih kalau kamu mau memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di media sosialmu. Terima kasih sudah berbagi!

Untuk informasi lebih lanjut, lihat tutorial kami tentang perangkat lunak Liana:

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
