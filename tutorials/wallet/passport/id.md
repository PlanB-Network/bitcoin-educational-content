---
name: Passport Core
description: Mengonfigurasi dan menggunakan dompet perangkat keras Passport dalam mode manual
---
![cover](assets/cover.webp)

Passport adalah dompet perangkat keras khusus Bitcoin yang dibuat oleh Foundation Devices, perusahaan asal Amerika yang berdiri pada April 2020 di Boston.

Passport Batch 2 yang dibahas di tutorial ini adalah penerus dari edisi Founder’s Edition. Perangkat ini punya desain premium, layar warna beresolusi tinggi, dan keyboard fisik yang nyaman digunakan. Beroperasi dalam mode Air-Gap, Passport memastikan kunci privat kamu tetap sepenuhnya terisolasi, dengan pertukaran data yang dilakukan lewat kartu MicroSD atau kode QR.

Perangkat ini juga dilengkapi baterai isi ulang yang bisa dilepas, yaitu Nokia BL-5C berkapasitas 1200 mAh. Baterai non-proprietary ini mudah diganti karena model BL-5C banyak tersedia di pasaran.

💡 **Pembaruan:** Sejak Maret 2025, nama dompet perangkat keras ini bukan lagi "Passport" atau "Passport V2", melainkan "Passport Core".

Untuk konektivitas, Passport dilengkapi dengan port MicroSD, port USB-C untuk pengisian daya, dan kamera belakang untuk memindai kode QR.

Dari sisi keamanan, Passport menggabungkan elemen keamanan khusus, dan seluruh kode sumbernya bersifat open source. Perangkat ini menawarkan semua fitur yang diharapkan dari dompet perangkat keras Bitcoin yang andal. Perlu dicatat bahwa Passport belum mendukung miniscript, tapi fitur ini sudah direncanakan untuk rilis pada kuartal kedua tahun 2025.

Dengan harga $199, Passport diposisikan sebagai dompet perangkat keras kelas atas yang bersaing dengan Coldcard Q, Jade Plus, Trezor Safe 5, dan model-model premium dari Ledger.

![Image](assets/fr/01.webp)

Untuk mengelola dompet aman kamu di Passport, ada beberapa opsi yang bisa dipilih. Dompet perangkat keras ini kompatibel dengan berbagai perangkat lunak manajemen dompet populer seperti Sparrow Wallet, Specter Desktop, Nunchuk, Keeper, dan lainnya. Dalam tutorial ini, kita akan mempelajari cara menggunakannya bersama Sparrow Wallet.

Kalau kamu masih pemula, pilihan paling mudah adalah memakai Passport dengan aplikasi bawaan bernama Envoy, yang juga dikembangkan oleh Foundation. Untuk panduan lengkap cara menggunakan Envoy dengan Passport, kamu bisa lihat di tutorial terpisah berikut:

https://planb.network/tutorials/wallet/mobile/envoy-3ae5d6c7-623b-45b3-bb34-abcf9572b7cb

## Membuka Kotak Paspor

Ketika kamu menerima Paspor, pastikan kotak dan segel pada karton masih utuh untuk mengonfirmasi bahwa paket tersebut belum dibuka. Verifikasi perangkat lunak terhadap keaslian dan integritas perangkat juga akan dilakukan saat perangkat diatur.

![Image](assets/fr/02.webp)

Isi kotak termasuk:


- Paspor;
- Selembar karton untuk menuliskan frasa mnemonik Anda;
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

## Paspor awal

Tekan tombol on/off di samping unit untuk menyalakannya.

![Image](assets/fr/04.webp)

Tekan tombol konfirmasi untuk mengakses menu berikutnya.

![Image](assets/fr/05.webp)

Dalam tutorial ini, kita akan menggunakan Sparrow Wallet untuk mengelola dompet dengan keamanan Passport. Pilih "*Penyiapan Manual*".

![Image](assets/fr/06.webp)

Kemudian, setujui persyaratan penggunaan.

![Image](assets/fr/07.webp)

Langkah selanjutnya adalah memeriksa perangkat kamu. Ini dilakukan untuk memastikan keaslian Passport dan memastikan bahwa perangkatmu tidak mengalami gangguan atau kerusakan selama pengiriman. Kamu akan diminta untuk memindai kode QR.

![Image](assets/fr/08.webp)

Kunjungi [situs verifikasi resmi](https://validate.foundationdevices.com/) dan pilih "*Passport*".

![Image](assets/fr/09.webp)

Gunakan kamera Paspor untuk memindai kode QR yang ditampilkan di situs.

![Image](assets/fr/10.webp)

Perangkat kamu kemudian akan menampilkan 4 kata.

![Image](assets/fr/11.webp)

Masukkan kata-kata ini di situs web untuk mengonfirmasi keaslian Paspor Anda dan klik "*Validate*".

![Image](assets/fr/12.webp)

Jika muncul pesan "*Lulus*", berarti dompet perangkat keras kamu asli. Sekarang kamu bisa menggunakannya untuk mengamankan dompet Bitcoin.

![Image](assets/fr/13.webp)

Konfirmasikan hasil tes pada Paspor kamu.

![Image](assets/fr/14.webp)

## Mengatur kode PIN

Berikutnya adalah langkah membuat kode PIN. Kode PIN ini digunakan untuk membuka kunci Passport kamu, sehingga berfungsi sebagai perlindungan terhadap akses fisik yang tidak sah. Kode PIN tidak berperan dalam proses penurunan kunci kriptografi dompet kamu. Jadi, meskipun seseorang tidak memiliki kode PIN, kepemilikan seedphrase 12 atau 24 kata tetap memungkinkanmu untuk memulihkan akses ke bitcoin milikmu.

![Image](assets/fr/15.webp)

Kami menyarankan kamu untuk memilih kode PIN yang benar-benar acak. Selain itu, simpan kode ini di tempat yang terpisah dari lokasi penyimpanan Passport kamu, misalnya di pengelola kata sandi.

Kamu bisa memilih kode PIN antara 6 hingga 12 digit. Disarankan untuk membuatnya sepanjang mungkin agar lebih aman.

Gunakan keyboard pada perangkat untuk memasukkan kode PIN kamu, lalu tekan tombol konfirmasi setelah selesai.

![Image](assets/fr/16.webp)

Konfirmasikan PIN kamu untuk kedua kalinya.

![Image](assets/fr/17.webp)

Kode PIN kamu telah terdaftar.

![Image](assets/fr/18.webp)

## Perbarui firmware Paspor

Passport kamu akan menyarankan untuk memperbarui firmware-nya. Disarankan agar kamu segera melakukan pembaruan supaya bisa mendapatkan peningkatan dan perbaikan dari versi terbaru. Untuk melanjutkan, cukup tekan tombol konfirmasi di sisi kanan.

![Image](assets/fr/19.webp)

Passport kamu siap menerima firmware baru melalui kartu MicroSD.

![Image](assets/fr/20.webp)

Untuk melakukan ini, gunakan kartu MicroSD yang disertakan dalam kotak Passport milikmu (atau kartu lainnya), dan masukkan ke dalam komputer milikmu. Unduh versi firmware terbaru dari [situs dokumentasi Foundation](https://docs.foundation.xyz/firmware-updates/passport/) atau [repositori GitHub](https://github.com/Foundation-Devices/passport2/releases).

![Image](assets/fr/21.webp)

Sebelum menginstalnya di perangkat, kami sangat menyarankan milikmu untuk memeriksa keaslian dan integritas firmware yang diunduh. Jika Anda memerlukan bantuan dalam hal ini, bacalah tutorial ini:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Setelah memeriksa file `.bin`, letakkan file tersebut di MicroSD milikmu, lalu masukkan ke dalam Passport. Penjelajah file Passport akan terbuka. Pilih file `vN.N.N-passport.bin`.

![Image](assets/fr/22.webp)

Klik "*Pilih*".

![Image](assets/fr/23.webp)

Kemudian konfirmasikan pemasangan firmware.

![Image](assets/fr/24.webp)

Harap tunggu hingga pembaruan selesai.

![Image](assets/fr/25.webp)

Setelah pembaruan selesai, masukkan kode PIN untuk membuka kunci perangkat dan melanjutkan konfigurasi.

![Image](assets/fr/26.webp)

## Membuat dompet Bitcoin baru

Sekarang saatnya membuat dompet Bitcoin baru. Klik pada tombol konfirmasi.

![Image](assets/fr/27.webp)

Untuk membuat portofolio baru, klik "*Buat Bibit Baru*".

![Image](assets/fr/28.webp)

Kamu bisa memilih antara seedphrase 12 atau 24 kata. Tingkat keamanan keduanya sebenarnya serupa, jadi kamu bisa memilih yang paling mudah untuk disimpan, biasanya 12 kata sudah cukup.

![Image](assets/fr/29.webp)

Klik "*Lanjutkan*".

![Image](assets/fr/30.webp)

Passport kamu sekarang akan menghasilkan *Kode Cadangan.* Ini adalah serangkaian angka yang bisa digunakan untuk mendekripsi cadangan dompet kamu yang tersimpan di MicroSD. Sistem pencadangan ini merupakan fitur khusus dari perangkat Foundation dan berfungsi sebagai pelengkap untuk seedphrase kamu, namun tidak kompatibel dengan perangkat lunak Bitcoin lainnya.

Kalau kamu memutuskan untuk menggunakan *Kode Cadangan* ini, pastikan untuk menyimpannya di tempat yang berbeda dari MicroSD yang berisi cadangan terenkripsi dompetmu. Namun, kamu juga bisa memilih untuk tidak menggunakan sistem ini jika merasa bahwa cadangan seedphrase saja sudah cukup.

![Image](assets/fr/31.webp)

Masukkan "*Kode Cadangan*" untuk mengonfirmasi bahwa kamu telah menyimpannya dengan benar.

![Image](assets/fr/32.webp)

Jika MicroSD telah dimasukkan, cadangan terenkripsi portofolio kamu telah disimpan di sana.

![Image](assets/fr/33.webp)

Passport kamu akan menampilkan seedphrase berisi 12 kata. Seedphrase ini memberi kamu akses penuh ke semua bitcoin milikmu. Siapa pun yang memiliki frasa ini bisa mencuri dana kamu, bahkan tanpa menyentuh perangkat Passport secara fisik.

Seedphrase 12 kata ini juga berfungsi untuk memulihkan akses ke bitcoin kamu jika Passport hilang, dicuri, atau rusak. Karena itu, sangat penting untuk menyimpannya dengan hati-hati di tempat yang benar-benar aman.

Kamu bisa menuliskannya di kartu yang sudah disertakan dalam kotak, atau untuk keamanan ekstra, sebaiknya diukir di lempengan baja tahan karat agar tetap terlindungi dari kebakaran, banjir, atau keruntuhan.

Klik tombol konfirmasi untuk melihat seedphrase kamu.

![Image](assets/fr/34.webp)

Untuk informasi lebih lanjut tentang cara yang tepat menyimpan dan mengelola seedphrase kamu, aku sangat menyarankan untuk mengikuti tutorial lainnya, terutama kalau kamu masih pemula:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Tentu saja, kamu tidak boleh membagikan kata-kata ini di Internet, seperti yang aku lakukan dalam tutorial ini. Portofolio contoh ini hanya akan digunakan di Testnet dan akan dihapus di akhir tutorial.**_

Buatlah cadangan fisik dari kalimat ini.

![Image](assets/fr/35.webp)

Paspor kamu telah berhasil dikonfigurasi. Klik tombol konfirmasi untuk melanjutkan.

![Image](assets/fr/36.webp)

## Penemuan menu

Antarmuka Passport kamu memiliki tiga menu utama:

- "*Rekening*";
- "*Lebih banyak*";
- "*Pengaturan*".

Untuk menavigasi di antara menu-menu ini, gunakan panah kiri dan kanan pada directional pad.

### *Menu "Akun*

Pada menu "*Account*", kamu akan menemukan fitur-fitur utama dompet Bitcoin kamu. Anda bisa menandatangani transaksi melalui kamera atau melalui port MicroSD.

![Image](assets/fr/37.webp)

Submenu "*Account Tools*" menawarkan opsi seperti memverifikasi alamat, menandatangani pesan, atau melihat alamat dalam portofolio Anda.

![Image](assets/fr/38.webp)

Pada submenu "*Manage Account*", kamu dapat menghubungkan dompet Bitcoin kamu ke perangkat lunak manajemen dompet (yang akan kita bahas pada langkah selanjutnya dalam tutorial ini), atau melihat dan mengganti nama akun kamu.

![Image](assets/fr/39.webp)

### Menu "Lainnya

Di menu "*Lebih Banyak*", kamu bisa membuat akun baru dalam portofolio kamu, yang ditautkan ke frasa mnemonik yang sama.

![Image](assets/fr/40.webp)

Kamu juga dapat memasukkan kata sandi BIP39 (lihat bagian berikutnya) atau menggunakan seed sementara.

![Image](assets/fr/41.webp)

### Menu "Pengaturan

Di menu "*Pengaturan*", kamu akan menemukan semua pengaturan dompet dan perangkat milikmu.

![Image](assets/fr/42.webp)

Submenu "*Perangkat*" memberi kamu opsi untuk menyesuaikan kecerahan layar, mengatur penundaan sebelum penguncian otomatis, mengubah kode PIN, atau mengganti nama perangkat.

![Image](assets/fr/43.webp)

Submenu "*Backup*" memungkinkan kamu mengekspor cadangan portofolio terenkripsi, memeriksa validitas cadangan yang sudah ada, atau mencari "*Backup Code*" lagi.

![Image](assets/fr/44.webp)

Sub-menu "*Firmware*" untuk memperbarui firmware Passport. Kami menyarankan agar kamu melakukan pembaruan ini secara teratur untuk mendapatkan manfaat dari perbaikan dan fitur terbaru.

![Image](assets/fr/45.webp)

Sub-menu "*Bitcoin*" memungkinkanmu untuk mengubah unit yang ditampilkan (BTC atau satoshi), mengelola dompet Multisig yang mungkin, atau beralih ke mode "*Testnet*".

![Image](assets/fr/46.webp)

Dalam "*Advanced*", kamu dapat melihat kata-kata frasa mnemonik kamu, melakukan tindakan pada MicroSD yang dimasukkan, mengatur ulang Passport ke pengaturan pabrik, atau melakukan pemeriksaan keaslian, seperti yang dilakukan sebelumnya.

![Image](assets/fr/47.webp)

Kamu bisa mengaktifkan *Security Words,* yaitu fitur yang menambahkan lapisan keamanan ekstra dengan menampilkan dua kata tertentu setiap kali kamu membuka kunci perangkat setelah memasukkan empat digit pertama kode PIN. Kata-kata ini akan disimpan saat proses konfigurasi dan berfungsi untuk memastikan bahwa Passport kamu belum diganti atau dirusak.

Kalau nantinya kata yang muncul berbeda dari biasanya, sebaiknya jangan gunakan perangkat tersebut. Aku sangat menyarankan untuk mengaktifkan fitur ini karena bisa membantu mencegah sebagian besar risiko gangguan fisik pada perangkatmu.

![Image](assets/fr/48.webp)

Terakhir, sub-menu "*Extensions*" memungkinkan kamu mengaktifkan fungsi yang spesifik untuk penggunaan alat tertentu, misalnya, protokol coinjoin Whirlpool.

![Image](assets/fr/49.webp)

## Menambahkan kata sandi BIP39

Sebelum melanjutkan, kamu bisa menambahkan kata sandi BIP39 jika mau. Kata sandi BIP39 adalah kata sandi opsional yang bisa kamu tentukan sendiri, dan berfungsi sebagai lapisan tambahan yang dikombinasikan dengan seedphrase untuk memperkuat keamanan dompet. Dengan mengaktifkan fitur ini, akses ke dompet Bitcoin kamu akan memerlukan dua hal sekaligus: seedphrase dan kata sandi. Tanpa keduanya, pemulihan dompet tidak akan mungkin dilakukan.

Sebelum mengatur opsi ini di Passport kamu, sangat disarankan untuk membaca artikel berikut agar benar-benar memahami cara kerja kata sandi ini dan menghindari kesalahan yang bisa menyebabkan hilangnya bitcoin kamu:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Untuk mengaktifkannya, buka menu "*Lainnya*" dan klik "*Masukkan Kata Sandi*".

![Image](assets/fr/50.webp)

Masukkan kata sandi kamu menggunakan keypad aA1, lalu pastikan untuk menyimpannya minimal satu kali di media fisik seperti kertas atau logam. Sebagai contoh, di sini aku menggunakan kata sandi yang sangat lemah, tapi kamu harus memilih kata sandi yang kuat dan acak, gabungkan berbagai jenis karakter dan buat cukup panjang agar benar-benar aman.

![Image](assets/fr/51.webp)

Perlu diperhatikan bahwa kata sandi BIP39 sangat peka terhadap huruf besar-kecil dan kesalahan ketik. Jika kamu memasukkan kata sandi yang sedikit berbeda dari yang pertama kali dikonfigurasi, Passport tidak akan menampilkan pesan kesalahan, tapi akan menghasilkan satu set kunci kriptografi yang berbeda dari dompet aslimu.

Karena itu, sangat penting untuk mencatat sidik jari kunci utama (master key fingerprint) yang akan ditampilkan pada langkah berikutnya. Sebagai contoh, dengan kata sandi `Plan B Network`, sidik jari kunci utama yang dihasilkan adalah `745D526B`.

![Image](assets/fr/52.webp)

Setiap kali kamu membuka kunci Passport, kamu harus kembali ke menu ini untuk memasukkan kata sandi dan menerapkannya ke dompet, karena Passport tidak menyimpan kata sandi tersebut.

Setelah memasukkan kata sandi, pastikan untuk memeriksa di layar konfirmasi bahwa sidik jari yang muncul sama dengan yang kamu catat saat konfigurasi awal. Jika cocok, berarti kata sandi kamu benar dan kamu telah mengakses dompet Bitcoin yang tepat. Tapi kalau berbeda, berarti kamu sedang masuk ke dompet yang salah—coba lagi dan pastikan tidak ada kesalahan input.

Sebelum kamu menerima bitcoin pertama di dompetmu, aku sangat menyarankan untuk melakukan tes pemulihan kosong terlebih dulu. Catat beberapa informasi referensi seperti xpub atau alamat penerima pertamamu, lalu hapus wallet di Passport selagi masih kosong (`Pengaturan -> Lanjutan -> Hapus Passport`).

Setelah itu, coba pulihkan dompet kamu menggunakan cadangan kertas yang berisi seedphrase dan kata sandi (jika kamu mengaktifkannya). Pastikan informasi yang muncul setelah proses pemulihan, seperti xpub atau alamat pertama, benar-benar sama dengan yang kamu catat sebelumnya. Kalau hasilnya cocok, berarti cadangan kertas kamu sudah dapat diandalkan.

Untuk panduan lengkap tentang cara melakukan tes pemulihan ini, kamu bisa membaca tutorial lainnya:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895


![Image](assets/fr/53.webp)

## Mengonfigurasi dompet di Dompet Sparrow

Dalam tutorial ini, aku akan menunjukkan cara penggunaan lanjutan Passport dengan Sparrow Wallet. Namun, dompet perangkat keras ini juga kompatibel dengan Envoy (aplikasi buatan Foundation), Keeper, BlueWallet, Nunchuk, Specter, dan masih banyak lagi.

Mulailah dengan mengunduh dan menginstal Sparrow Wallet [dari situs web resmi] (https://sparrowwallet.com/) di komputer kamu, jika kamu belum melakukannya.

![Image](assets/fr/54.webp)

Pastikan untuk memeriksa keaslian dan integritas perangkat lunak sebelum instalasi. Kalau kamu tidak tahu cara melakukannya, silakan baca tutorial ini:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Setelah Sparrow Wallet terbuka, klik tab "*File*", lalu "*Dompet Baru*".

![Image](assets/fr/55.webp)

Beri nama dompet kamu, lalu klik "*Buat Dompet*".

![Image](assets/fr/56.webp)

Pilih "*Dompet Perangkat Keras yang Terisi Penuh*".

![Image](assets/fr/57.webp)

Klik "*Pindai...*" di samping opsi "*Passport*". Ini akan membuka webcam kamu.

![Image](assets/fr/58.webp)

Pada dompet perangkat keras kamu, buka menu "*Akun*", pilih submenu "*Kelola Akun*", dan klik "*Hubungkan Dompet*".

![Image](assets/fr/59.webp)

Pada daftar tarik-turun yang muncul, pilih "*Sparrow*".

![Image](assets/fr/60.webp)

Kemudian pilih "*Single-sig*" untuk konfigurasi normal, tanpa multisig.

![Image](assets/fr/61.webp)

Pilih opsi "*Kode QR*".

![Image](assets/fr/62.webp)

Passport kamu kemudian akan menampilkan kode QR dinamis. Gunakan webcam komputer kamu untuk memindai kode tersebut ke dalam aplikasi Sparrow.

![Image](assets/fr/63.webp)

Sekarang kamu akan melihat xpub dan sidik jari kunci utama kamu, yang seharusnya cocok dengan yang ditampilkan di Paspor kamu saat Anda memasukkan kata sandi. Klik pada tombol "*Apply*".

![Image](assets/fr/64.webp)

Buat kata sandi yang kuat untuk melindungi akses ke dompet Sparrow kamu. Kata sandi ini akan menjaga kunci publik, alamat, label, dan riwayat transaksi kamu dari akses yang tidak sah. Sebaiknya simpan kata sandi ini di pengelola kata sandi supaya tidak lupa.

![Image](assets/fr/65.webp)

Passport kamu kemudian akan meminta untuk memindai alamat penerima pertama sebagai konfirmasi bahwa proses impor telah berhasil.

![Image](assets/fr/66.webp)

Di Sparrow, buka tab "*Receive*" dan pindai kode QR dari alamat pertama.

![Image](assets/fr/67.webp)

Jika operasi berhasil, Paspor milikmu akan menampilkan "*Verified*".

![Image](assets/fr/68.webp)

Hal ini menegaskan bahwa impor tersebut berhasil.

![Image](assets/fr/69.webp)

## Menerima bitcoin

Setelah Passport siap, kamu siap untuk menerima satoshi pertama Anda di dompet Bitcoin baru. Untuk melakukannya, pada Sparrow, klik menu "*Receive*".

![Image](assets/fr/70.webp)

Sparrow akan menampilkan alamat tanda terima kosong pertama dalam portofolio. Kamu bisa menambahkan label.

![Image](assets/fr/71.webp)

Sebelum menggunakannya, kita akan memeriksa alamat di layar Passport untuk memastikan alamat tersebut adalah milik dompet Bitcoin kita. Di Sparrow, kamu bisa memperbesar kode QR alamat tersebut dengan mengekliknya jika perlu. Pada menu "*Akun*" di Passport kamu, pilih "*Alat Akun*".

![Image](assets/fr/72.webp)

Klik "*Verifikasi Alamat*", lalu pindai kode QR yang ditampilkan di Sparrow Wallet.

![Image](assets/fr/73.webp)

Pastikan alamat yang ditampilkan di Paspor sama persis dengan alamat yang ditampilkan di Sparrow, dan muncul tulisan "*Verified*".

![Image](assets/fr/74.webp)

Kamu sekarang bisa menggunakannya untuk menerima bitcoin. Ketika transaksi disiarkan di jaringan, transaksi itu akan muncul di Sparrow. Tunggu sampai kamu menerima konfirmasi yang cukup untuk menganggap transaksi tersebut sudah pasti.

![Image](assets/fr/75.webp)

## Kirim bitcoin

Sekarang setelah kamu memiliki beberapa sat di dompet, kamu juga dapat mengirim beberapa. Untuk melakukannya, klik menu "*UTXOs*".

![Image](assets/fr/76.webp)

Pilih UTXO yang ingin kamu gunakan sebagai input untuk transaksi ini, lalu klik "*Kirim Terpilih*".

![Image](assets/fr/77.webp)

Masukkan alamat penerima, label untuk mengingatkan kamu tentang tujuan transaksi dan jumlah yang ingin kamu kirim ke alamat ini.

![Image](assets/fr/78.webp)

Sesuaikan tarif biaya sesuai dengan kondisi pasar saat ini, lalu klik "*Buat Transaksi*".

![Image](assets/fr/79.webp)

Pastikan semua parameter transaksi sudah benar, lalu klik "*Finalisasi Transaksi untuk Penandatanganan*".

![Image](assets/fr/80.webp)

Klik *Show QR* untuk menampilkan PSBT (*Partially Signed Bitcoin Transaction*). Sparrow sudah membuat transaksinya, tapi belum memiliki tanda tangan untuk membuka kunci bitcoin yang digunakan sebagai input. Tanda tangan ini hanya bisa dilakukan oleh Passport, karena di sanalah seed kamu disimpan dan dari situ juga Passport mengakses private key yang dibutuhkan untuk menandatangani transaksi.

![Image](assets/fr/81.webp)

Pada Paspor milikmu, akses menu "*Akun*" dan klik "*Tanda Tangan dengan Kode QR*".

![Image](assets/fr/82.webp)

Pindai PSBT (*Transaksi Bitcoin Bertanda Tangan Sebagian*) yang ditampilkan di Dompet Sparrow.

![Image](assets/fr/83.webp)

Konfirmasikan bahwa alamat penerima dan jumlah yang dikirim sudah benar, lalu tekan tombol konfirmasi.

![Image](assets/fr/84.webp)

Periksa alamat pertukaran. Dalam contohku ini, tidak ada, karena transaksi ini mencakup satu keluaran.

![Image](assets/fr/85.webp)

Pastikan biaya tersebut sesuai dengan yang kamu pilih.

![Image](assets/fr/86.webp)

Jika semua informasi sudah benar, klik tombol konfirmasi untuk menandatangani transaksi.

![Image](assets/fr/87.webp)

Pada Sparrow Wallet, klik "*Pindai QR*" dan pindai kode QR yang ditampilkan pada Paspor milikmu.

![Image](assets/fr/88.webp)

Transaksi yang kamu tandatangani sekarang siap untuk disiarkan di jaringan Bitcoin dan dimasukkan ke dalam blok oleh penambang. Jika semuanya sudah benar, klik "*Siarkan Transaksi*".

![Image](assets/fr/89.webp)

Transaksi kamu telah disiarkan dan menunggu konfirmasi.

![Image](assets/fr/90.webp)

Selamat, sekarang kamu sudah tahu cara mengonfigurasi dan menggunakan Passport. Kalau kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih kalau kamu mau memberi jempol hijau di bawah ini. Jangan ragu juga untuk membagikan artikel ini di media sosialmu. Terima kasih sudah membaca dan ikut berbagi!

Untuk informasi lebih lanjut, cek juga tutorial kami tentang perangkat lunak Liana:

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

