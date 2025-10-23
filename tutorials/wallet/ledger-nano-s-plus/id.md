---
name: Ledger Nano S Plus
description: Pengaturan dan penggunaan Ledger Nano S Plus
---
![cover](assets/cover.webp)

Dompet perangkat keras adalah perangkat elektronik yang dibuat khusus untuk mengelola dan mengamankan kunci privat dari dompet Bitcoin. Berbeda dengan dompet perangkat lunak (atau dompet panas) yang terpasang di perangkat umum dan sering terhubung ke internet, dompet perangkat keras memungkinkan isolasi fisik kunci privat, sehingga mengurangi risiko peretasan dan pencurian.

Tujuan utama dompet perangkat keras adalah meminimalkan fungsi perangkat sebanyak mungkin agar permukaan serangan jadi sekecil mungkin. Permukaan serangan yang kecil berarti lebih sedikit celah potensial yang bisa dimanfaatkan penyerang untuk mengakses bitcoin.

Kamu sangat disarankan memakai dompet perangkat keras untuk mengamankan bitcoin, terutama kalau kamu menyimpan jumlah yang signifikan, baik dalam nilai absolut maupun sebagai proporsi dari total aset kamu.

Dompet perangkat keras digunakan bersama dengan perangkat lunak manajemen dompet di komputer atau smartphone. Perangkat lunak ini mengelola pembuatan transaksi, tapi tanda tangan kriptografis yang diperlukan untuk memvalidasi transaksi dilakukan sepenuhnya di dalam dompet perangkat keras. Artinya, kunci privat tidak pernah terekspos ke lingkungan yang berpotensi rentan.

Dompet perangkat keras memberikan perlindungan ganda: di satu sisi, mereka menjaga bitcoin kamu dari serangan jarak jauh dengan menyimpan kunci privat secara offline, dan di sisi lain, mereka biasanya memiliki ketahanan fisik yang lebih baik terhadap upaya untuk mengekstrak kunci. Berdasarkan dua aspek keamanan inilah, kamu bisa menilai dan membandingkan berbagai model yang tersedia di pasaran.

Dalam tutorial ini, aku mengajak kamu untuk mengenal salah satu solusi terbaik: **Ledger Nano S Plus.**

![NANO S PLUS LEDGER](assets/notext/01.webp)

## Pengenalan ke Ledger Nano S Plus

Ledger Nano S Plus adalah dompet perangkat keras yang diproduksi oleh perusahaan Prancis Ledger, dipasarkan dengan harga 79 €.

![NANO S PLUS LEDGER](assets/notext/02.webp)

Nano S Plus dilengkapi dengan chip bersertifikat CC EAL6+ (elemen aman), yang memberikan perlindungan lanjutan terhadap serangan fisik pada perangkat keras. Layar dan tombolnya dikendalikan langsung oleh chip ini. Salah satu kritik yang sering muncul adalah bahwa kode chip ini tidak bersifat open-source, sehingga pengguna harus menaruh kepercayaan tertentu pada integritas komponennya. Namun, elemen ini telah diaudit oleh para ahli independen.

Dalam hal penggunaan, Ledger Nano S Plus hanya dapat dioperasikan melalui koneksi kabel USB-C.

Ledger menonjol dari para pesaingnya karena selalu cepat mengadopsi fitur-fitur Bitcoin terbaru, seperti Taproot dan Miniscript, yang sangat diapresiasi komunitas. Setelah aku mencobanya, aku merasa Ledger Nano S Plus adalah dompet perangkat keras tingkat pemula yang sangat solid. Perangkat ini menawarkan tingkat keamanan tinggi dengan harga yang cukup wajar. Kekurangannya dibandingkan perangkat lain di kisaran harga yang sama adalah fakta bahwa kode firmware-nya tidak open-source. Selain itu, layar Nano S Plus relatif kecil dibandingkan model yang lebih mahal seperti Ledger Flex atau Coldcard Q1. Meski begitu, antarmukanya dirancang dengan sangat baik: meskipun hanya memiliki dua tombol dan layar kecil, penggunaannya tetap mudah, bahkan untuk fitur-fitur lanjutan seperti passphrase BIP39. Ledger Nano S Plus tidak memiliki baterai, koneksi air-gap, kamera, atau port microSD, tapi hal ini wajar untuk kelas harganya.

Menurut aku, Ledger Nano S Plus adalah pilihan bagus untuk mengamankan dompet Bitcoin kamu, cocok untuk pengguna pemula maupun menengah. Tapi di kisaran harga yang sama, aku pribadi lebih memilih Trezor Safe 3, yang menawarkan opsi serupa. Keunggulan Trezor menurut aku ada pada cara mereka mengelola elemen keamanannya: seedphrase dan kunci dikelola sepenuhnya oleh kode sumber terbuka, namun tetap mendapat perlindungan dari chip. Kekurangannya, Trezor kadang agak lambat dalam mengimplementasikan fitur baru, tidak secepat Ledger.

## Bagaimana cara membeli Ledger Nano S Plus?

Ledger Nano S Plus tersedia untuk dijual [di situs resmi](https://shop.ledger.com/products/ledger-nano-s-plus). Untuk membelinya di toko fisik, kamu juga dapat menemukan [daftar reseller resmi](https://www.ledger.com/reseller) di situs web Ledger.

## Prasyarat

Setelah kamu menerima Ledger Nano kamu, langkah pertama adalah memeriksa kemasannya untuk memastikan tidak ada yang terbuka. Jika kemasannya rusak, itu bisa jadi tanda bahwa dompet perangkat keras kamu telah dikompromikan dan mungkin tidak asli.

Saat membuka, kamu seharusnya menemukan item berikut di dalam kotak:
- Ledger Nano S Plus;
- Kabel USB-C ke USB-A;
- Buku panduan pengguna;
- Kartu untuk menuliskan frasa mnemonik kamu.

Untuk tutorial ini, kamu akan memerlukan 2 aplikasi perangkat lunak: Ledger Live untuk menginisialisasi Ledger, dan Sparrow Wallet untuk mengelola dompet Bitcoin kamu. Unduh [Ledger Live](https://www.ledger.com/ledger-live) dan [Sparrow Wallet](https://sparrowwallet.com/download/) dari situs web resmi mereka.

![NANO S PLUS LEDGER](assets/notext/03.webp)
Untuk kedua perangkat lunak ini, aku sangat menyarankan kamu untuk memeriksa keasliannya (menggunakan GnuPG) dan integritasnya (melalui hash) sebelum menginstalnya di perangkat kamu. Kalau kamu belum tahu cara melakukannya, kamu bisa mengikuti tutorial lain berikut ini:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Bagaimana Cara Menginisialisasi Ledger Nano?

Hubungkan Nano kamu ke komputer yang sudah terpasang Ledger Live dan Sparrow Wallet. Untuk navigasi di Ledger kamu, gunakan tombol kiri untuk berpindah ke kiri dan tombol kanan untuk berpindah ke kanan. Untuk memilih atau mengonfirmasi opsi, tekan kedua tombol secara bersamaan.

![NANO S PLUS LEDGER](assets/notext/04.webp)

Scroll melalui berbagai halaman pengantar, lalu klik pada 2 tombol untuk memulai.

![NANO S PLUS LEDGER](assets/notext/05.webp)

Pilih opsi "*Setup as a new device*".

![NANO S PLUS LEDGER](assets/notext/06.webp)

Pilih kode PIN yang akan digunakan untuk membuka kunci Ledger kamu. Ini adalah perlindungan terhadap akses fisik yang tidak sah. Kode PIN ini tidak berperan dalam derivasi kunci kriptografis dompet kamu. Jadi, bahkan tanpa akses ke kode PIN ini, memiliki seedphrase 24 kata kamu akan memungkinkan kamu untuk mendapatkan kembali akses ke bitcoin kamu.

![NANO S PLUS LEDGER](assets/notext/07.webp)

Disarankan untuk memilih PIN 8 digit yang benar-benar acak. Pastikan juga kamu menyimpan kode ini di tempat yang berbeda dari lokasi penyimpanan Ledger Nano S Plus kamu, misalnya di pengelola kata sandi.

Gunakan tombol untuk berpindah di antara digit, lalu pilih setiap digit dengan menekan kedua tombol secara bersamaan.

![NANO S PLUS LEDGER](assets/notext/08.webp)

Masukkan PIN untuk kedua kalinya untuk mengonfirmasinya.
Nano akan memberikan instruksi tentang cara mengelola frasa pemulihan milikmu.

**Frasa mnemonik ini memberikan akses penuh dan tidak terbatas ke semua bitcoin Anda**. Siapa pun yang memiliki seedphrase ini bisa mencuri dana kamu, bahkan tanpa perlu akses fisik ke Ledger kamu. Seedphrase 24 kata ini memungkinkan kamu memulihkan akses ke bitcoin kamu jika Ledger Nano kamu hilang, dicuri, atau rusak. Karena itu, sangat penting untuk mencatat dan menyimpannya dengan hati-hati di tempat yang benar-benar aman.

Kamu bisa menuliskannya di kartu kertas yang disertakan bersama Ledger kamu, atau untuk keamanan ekstra, aku sarankan mengukirnya di media stainless steel agar tahan terhadap risiko kebakaran, banjir, atau kerusakan fisik.

Kamu bisa membaca instruksi ini dan berpindah halaman dengan menekan tombol kanan.

Ledger akan membuat seedphrase kamu menggunakan generator angka acak. Pastikan kamu tidak diamati selama operasi ini. Tuliskan kata-kata yang disediakan oleh Ledger pada media fisik pilihan kamu. Tergantung pada strategi keamanan kamu, kamu mungkin mempertimbangkan untuk membuat beberapa salinan fisik lengkap dari seedphrase tersebut (tetapi yang penting, jangan membagikannya). Sangat penting untuk menjaga kata-kata tersebut bernomor dan dalam urutan berurutan.
***Jelas, kamu seharusnya tidak pernah membagikan kata-kata ini di internet, berbeda dengan apa yang saya lakukan dalam tutorial ini. Dompet contoh ini hanya akan digunakan pada Testnet dan akan dihapus setelah tutorial.***

Untuk beralih ke kata-kata berikutnya, klik tombol kanan.

Setelah semua kata dicatat, klik 2 tombol untuk beralih ke langkah selanjutnya.

Klik pada dua tombol "*Konfirmasi frasa Pemulihan Anda*", kemudian pilih kata-kata dari frasa mnemonik kamu dalam urutan mereka untuk mengonfirmasi bahwa kamu telah mencatatnya dengan benar. Gunakan tombol kiri dan kanan untuk menavigasi antar opsi, kemudian pilih kata yang benar dengan mengklik 2 tombol. Lanjutkan prosedur ini sampai kata ke-24.

Jika seedphrase yang kamu konfirmasi cocok persis dengan yang diberikan Ledger pada langkah sebelumnya, kamu bisa melanjutkan. Jika tidak cocok, berarti cadangan fisik seedphrase kamu salah, dan kamu perlu mengulangi prosesnya dari awal.

Dan selesai, seed kamu sudah berhasil dibuat di Ledger Nano S Plus kamu. Sebelum lanjut membuat dompet Bitcoin baru dari seed ini, ayo kita jelajahi dulu pengaturan perangkatnya bersama-sama.

## Bagaimana cara memodifikasi pengaturan Ledger Anda?

Untuk mengakses pengaturan, tahan kedua tombol selama beberapa detik.

Klik pada menu "*Pengaturan*".

Dan pilih "*Umum*".

Di menu "*Bahasa*", kamu dapat mengubah bahasa tampilan.

Di menu "*Kecerahan*", kamu dapat menyesuaikan kecerahan layar. Kami tidak tertarik dengan pengaturan umum lainnya untuk saat ini.

Sekarang, pergilah ke bagian pengaturan "*Keamanan*".
"*Ubah PIN*" memungkinkanmu untuk mengubah kode PIN Anda. ![NANO S PLUS LEDGER](assets/notext/22.webp)
"*Passphrase*" memungkinkanmu untuk menetapkan passphrase BIP39. Passphrase adalah kata sandi opsional yang, dikombinasikan dengan frasa pemulihanmu, memberikan lapisan keamanan tambahan untuk dompet Anda.

![NANO S PLUS LEDGER](assets/notext/23.webp)

Saat ini, dompet kamu dihasilkan dari seedphrase yang terdiri dari 24 kata. Seedphrase ini sangat penting karena memungkinkan kamu memulihkan semua kunci dompet jika terjadi kehilangan. Tapi, ini juga merupakan single point of failure (SPOF). Jika seedphrase kamu sampai jatuh ke tangan orang lain, bitcoin kamu dalam bahaya. Di sinilah peran passphrase. Ini adalah kata sandi opsional yang bisa kamu tentukan sendiri, dan ditambahkan ke seedphrase untuk meningkatkan keamanan dompet.

Passphrase tidak boleh disamakan dengan kode PIN. Ia berperan langsung dalam proses derivasi kunci kriptografis kamu. Passphrase bekerja bersama seedphrase untuk mengubah seed yang menjadi dasar pembuatan kunci. Jadi, bahkan jika seseorang memiliki seedphrase 24 kata kamu, tanpa passphrase, mereka tetap tidak bisa mengakses dana kamu. Menggunakan passphrase pada dasarnya menciptakan dompet baru dengan kunci yang berbeda. Mengubah passphrase (bahkan sedikit saja) akan menghasilkan dompet yang sepenuhnya berbeda.

Passphrase adalah alat yang sangat kuat untuk meningkatkan keamanan bitcoin kamu. Tapi penting banget untuk benar-benar memahami cara kerjanya sebelum kamu menerapkannya, supaya tidak kehilangan akses ke dompet kamu sendiri. Karena itu, aku sarankan kamu untuk membaca tutorial lain yang secara khusus membahas cara mengatur passphrase di Ledger kamu:

https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

Menu "*PIN lock*" memungkinkan kamu untuk mengonfigurasi dan mengaktifkan penguncian otomatis Ledger Anda setelah periode ketidakaktifan yang ditentukan.

![NANO S PLUS LEDGER](assets/notext/24.webp)

Menu "*Screen saver*" memungkinkanmu untuk menyesuaikan mode tidur dari Ledger Nano Anda. Perlu dicatat bahwa screen saver tidak akan meminta kamu memasukkan PIN saat perangkat aktif kembali, kecuali jika opsi PIN lock diaktifkan agar sesuai dengan mode tidur. Fitur ini sangat berguna untuk perangkat Ledger Nano X yang memiliki baterai, karena membantu mengurangi konsumsi daya.

![NANO S PLUS LEDGER](assets/notext/25.webp)

Akhirnya, menu "*Reset device*" memungkinkanmu untuk mereset Ledger milikmu. Lanjutkan dengan reset ini hanya kalau kamy yakin tidak mengandung kunci apa pun yang mengamankan bitcoin, karena kamu bisa kehilangan akses ke dana Anda secara permanen. Opsi ini bisa berguna untuk melakukan tes pemulihan kosong, tetapi saya akan membicarakan ini sedikit lebih lanjut nanti.

![NANO S PLUS LEDGER](assets/notext/26.webp)
## Bagaimana Cara Memasang Aplikasi Bitcoin?

Mulailah dengan meluncurkan perangkat lunak Ledger Live di komputermu, kemudian sambungkan dan buka kunci Ledger Nano. Di Ledger Live, pergi ke menu "*My Ledger*". Kamu akan diminta untuk mengizinkan akses ke Nano kamu.

![NANO S PLUS LEDGER](assets/notext/27.webp)

Validasi akses di Ledger Anda dengan mengklik dua tombol.

![NANO S PLUS LEDGER](assets/notext/28.webp)

Pertama, di Ledger Live, pastikan "*Genuine check*" muncul. Ini mengonfirmasi bahwa perangkat Anda asli.

![NANO S PLUS LEDGER](assets/notext/29.webp)

Jika firmware dari Ledger Nano milikmu tidak terbaru, Ledger Live secara otomatis akan menawarkan untuk memperbaruinya. Kalau perlu, klik pada "*Update firmware*", kemudian pada "*Install update*" untuk memulai instalasi. Di Ledger kamu, klik dua tombol untuk mengonfirmasi, kemudian tunggu selama instalasi.
Akhirnya, kita akan menambahkan aplikasi Bitcoin. Untuk melakukan ini, di Ledger Live, klik tombol "*Install*" di sebelah "*Bitcoin (BTC)*".
![NANO S PLUS LEDGER](assets/notext/30.webp)

Aplikasi akan terinstal pada Nano.

![NANO S PLUS LEDGER](assets/notext/31.webp)

Mulai sekarang, kamu tidak lagi memerlukan perangkat lunak Ledger Live untuk mengelola dompet kamu sehari-hari. Kamu hanya perlu membukanya sesekali kalau ada pembaruan firmware baru yang tersedia. Untuk semua kebutuhan lainnya, kita akan menggunakan Sparrow Wallet, yang jauh lebih lengkap dan efektif untuk mengelola dompet Bitcoin.

![NANO S PLUS LEDGER](assets/notext/32.webp)

## Bagaimana Cara Menyiapkan Dompet Bitcoin Baru dengan Sparrow?

Buka Sparrow Wallet dan lewati halaman pengantarnya sampai kamu masuk ke layar utama. Pastikan kamu sudah terhubung dengan benar ke sebuah node dengan melihat indikator di pojok kanan bawah layar.

![NANO S PLUS LEDGER](assets/notext/33.webp)

Aku sangat menyarankan kamu untuk menggunakan node Bitcoin kamu sendiri. Dalam tutorial ini, aku menggunakan node publik (kuning) karena sedang berada di testnet, tapi untuk penggunaan normal, lebih baik memilih Bitcoin Core lokal (hijau) atau server Electrum yang terhubung ke node jarak jauh (biru).

Klik pada menu "*File*" kemudian "*New Wallet*".

![NANO S PLUS LEDGER](assets/notext/34.webp)

Pilih nama untuk dompet ini, kemudian klik pada "*Create Wallet*".

![NANO S PLUS LEDGER](assets/notext/35.webp)

Di menu dropdown "*Script Type*", pilih jenis skrip yang akan digunakan untuk mengamankan bitcoin milikmu. Aku merekomendasikan untuk memilih "*Taproot*", atau jika tidak tersedia, "*Native SegWit*".

![NANO S PLUS LEDGER](assets/notext/36.webp)
Klik pada tombol "*Connected Hardware Wallet*".
![NANO S PLUS LEDGER](assets/notext/37.webp)

Kalau kamu belum melakukannya, hubungkan Ledger Nano S Plus kamu ke komputer, buka kunci dengan kode PIN kamu, dan kemudian buka aplikasi "*Bitcoin*" dengan mengklik 2 tombol sekali pada logo Bitcoin.

*Dalam tutorial ini, aku menggunakan aplikasi Bitcoin Testnet, tetapi prosedurnya tetap sama untuk mainnet.*

![NANO S PLUS LEDGER](assets/notext/38.webp)

Di Sparrow, klik pada tombol "*Scan*".

![NANO S PLUS LEDGER](assets/notext/39.webp)

Kemudian klik pada "*Import Keystore*".

![NANO S PLUS LEDGER](assets/notext/40.webp)

Sekarang kamu bisa melihat detail dompet kamu, termasuk extended public key dari akun pertama kamu. Klik tombol Apply untuk menyelesaikan proses pembuatan dompet

![NANO S PLUS LEDGER](assets/notext/41.webp)

Pilih kata sandi yang kuat untuk mengamankan akses ke Sparrow Wallet. Kata sandi ini akan melindungi data dompet kamu di Sparrow, termasuk kunci publik, alamat, label, dan riwayat transaksi dari akses yang tidak sah.

Aku sarankan kamu menyimpan kata sandi ini di pengelola kata sandi supaya tidak lupa.

![NANO S PLUS LEDGER](assets/notext/42.webp)

Dan sekarang, dompet Anda telah dibuat!

![NANO S PLUS LEDGER](assets/notext/43.webp)
Sebelum kamu menerima bitcoin pertama di dompetmu, **aku sangat menyarankan kamu untuk melakukan tes pemulihan tanpa transaksi**. Catat informasi referensi, seperti xpub kamu, kemudian reset Ledger Nano kamu sementara dompet masih kosong. Setelah itu, coba pulihkan dompet kamu di Ledger menggunakan cadangan kertas kamu. Periksa bahwa xpub yang dihasilkan setelah pemulihan cocok dengan yang kamu catat awalnya. Jika iya, Anda dapat yakin bahwa cadangan kertas kamu dapat diandalkan.
Untuk mempelajari lebih lanjut tentang cara melakukan tes pemulihan, aku menyarankanmu untuk berkonsultasi dengan tutorial lain ini:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Bagaimana cara menerima bitcoin dengan Ledger Nano?

Klik pada tab "*Receive*".

![NANO S PLUS LEDGER](assets/notext/44.webp)

Hubungkan Ledger Nano S Plus ke komputer, buka kunci dengan kode PIN Anda, kemudian buka aplikasi "*Bitcoin*".

![NANO S PLUS LEDGER](assets/notext/45.webp)
Sebelum menggunakan alamat yang disediakan oleh Sparrow Wallet, verifikasi di layar Ledger. Praktik ini memungkinkan Anda untuk memastikan bahwa alamat yang ditampilkan di Sparrow tidak palsu dan bahwa dompet perangkat keras memang memiliki kunci privat yang diperlukan untuk menghabiskan bitcoin yang diamankan dengan alamat ini nanti. Ini membantu kamu menghindari beberapa jenis serangan.
Untuk melakukan verifikasi ini, klik pada tombol "*Display Address*".

![NANO S PLUS LEDGER](assets/notext/46.webp)

Pastikan alamat yang ditampilkan di Ledger kamu cocok dengan yang muncul di Sparrow Wallet. Sebaiknya lakukan verifikasi ini tepat sebelum kamu memberikan alamat tersebut ke pengirim, untuk memastikan alamatnya valid. Kamu bisa menggunakan tombol di Ledger untuk menampilkan alamat secara lengkap.

![NANO S PLUS LEDGER](assets/notext/47.webp)

Kemudian klik pada "*Approve*" jika alamatnya memang identik.

![NANO S PLUS LEDGER](assets/notext/48.webp)

Kamu dapat menambahkan "*Label*" untuk mendeskripsikan sumber bitcoin yang akan diamankan dengan alamat ini. Ini adalah praktik yang baik yang membantu kamu mengelola UTXO dengan lebih baik.

![NANO S PLUS LEDGER](assets/notext/49.webp)

Untuk informasi lebih lanjut tentang pelabelan, aku juga menyarankanmu untuk memeriksa tutorial lain ini:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Kemudian kamu dapat menggunakan alamat ini untuk menerima bitcoin.

![NANO S PLUS LEDGER](assets/notext/50.webp)

## Bagaimana cara mengirim bitcoin dengan Ledger Nano?

Sekarang setelah kamu menerima sats pertama kamu di dompet yang diamankan dengan Nano S Plus, kamu juga bisa mulai menggunakannya! Hubungkan Ledger kamu ke komputer, buka kuncinya, jalankan Sparrow Wallet, lalu buka tab Send untuk membuat transaksi baru.

![NANO S PLUS LEDGER](assets/notext/51.webp)

Jika kamu ingin melakukan "*coin control*", yang berarti secara spesifik memilih UTXO mana yang akan dikonsumsi dalam transaksi, pergi ke tab "*UTXOs*". Pilih UTXO yang ingin kamu habiskan, kemudian klik pada "*Send Selected*". Kamu akan diarahkan ke layar yang sama dari tab "*Send*", tetapi dengan UTXO kamu sudah dipilih untuk transaksi.

![NANO S PLUS LEDGER](assets/notext/52.webp)

Masukkan alamat tujuan. kamu juga dapat memasukkan beberapa alamat dengan mengklik tombol "*+ Add*".

![NANO S PLUS LEDGER](assets/notext/53.webp)

Catat sebuah "*Label*" untuk mengingat tujuan pengeluaran ini.

![NANO S PLUS LEDGER](assets/notext/54.webp)
Pilih jumlah yang akan dikirim ke alamat ini.
![NANO S PLUS LEDGER](assets/notext/55.webp)

Sesuaikan tarif biaya transaksi sesuai dengan pasar saat ini.

![NANO S PLUS LEDGER](assets/notext/56.webp)
Pastikan semua pengaturan transaksi kamu sudah benar, kemudian klik pada "*Create Transaction*".
![NANO S PLUS LEDGER](assets/notext/57.webp)

Jika semuanya terlihat baik, klik pada "*Finalize Transaction for Signing*".

![NANO S PLUS LEDGER](assets/notext/58.webp)

Klik pada "*Sign*".

![NANO S PLUS LEDGER](assets/notext/59.webp)

Klik pada "*Sign*" di sebelah Ledger Nano S Plus.

![NANO S PLUS LEDGER](assets/notext/60.webp)

Verifikasi pengaturan transaksi di layar Ledger, termasuk alamat penerima, jumlah yang dikirim, dan jumlah biaya.

![NANO S PLUS LEDGER](assets/notext/61.webp)

Jika semuanya sudah terlihat baik, tekan dua tombol pada "*Sign transaction*" untuk menandatangani.

![NANO S PLUS LEDGER](assets/notext/62.webp)

Transaksi kamu sekarang sudah ditandatangani. Periksa kembali apakah semuanya sudah sesuai, lalu klik Broadcast Transaction untuk menyiarkannya ke jaringan Bitcoin.

![NANO S PLUS LEDGER](assets/notext/63.webp)

Kamu dapat menemukannya di tab "*Transactions*" dari Sparrow Wallet.

![NANO S PLUS LEDGER](assets/notext/64.webp)

Selamat, kamu sekarang sudah menguasai penggunaan dasar Ledger Nano S Plus dengan Sparrow Wallet! Dalam tutorial berikutnya, kita akan membahas cara menggunakan Ledger dengan Liana untuk memanfaatkan Miniscript.

Kalau kamu merasa tutorial ini bermanfaat, aku bakal sangat menghargai kalau kamu mau kasih jempol ke atas di bawah ini. Jangan ragu juga untuk membagikan artikel ini di media sosial kamu. Terima kasih banyak!

Aku juga menyarankan kamu untuk melihat tutorial lengkap tentang Ledger Flex berikut ini:

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

