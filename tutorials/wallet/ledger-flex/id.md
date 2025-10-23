---
name: Ledger Flex
description: Mengatur dan menggunakan Ledger Flex
---
![cover](assets/cover.webp)

Dompet perangkat keras adalah perangkat elektronik yang dibuat khusus untuk mengelola dan mengamankan private key dari dompet Bitcoin. Berbeda dengan dompet perangkat lunak (atau dompet panas) yang dipasang di perangkat umum dan sering terhubung ke internet, dompet perangkat keras memberikan isolasi fisik bagi private key, sehingga mengurangi risiko peretasan dan pencurian.

Tujuan utama dompet perangkat keras adalah meminimalkan fungsionalitas perangkat agar permukaan serangannya sekecil mungkin. Permukaan serangan yang lebih kecil berarti lebih sedikit celah yang bisa dimanfaatkan penyerang untuk mengakses bitcoin.

Kamu disarankan untuk menggunakan dompet perangkat keras untuk mengamankan bitcoin kamu, terutama kalau kamu menyimpan jumlah yang besar, baik dari segi nilai maupun proporsi terhadap total asetmu.

Dompet perangkat keras biasanya digunakan bersama perangkat lunak pengelola dompet di komputer atau smartphone. Perangkat lunak ini menangani pembuatan transaksi, tapi tanda tangan kriptografis yang dibutuhkan untuk memvalidasi transaksi hanya dilakukan di dalam perangkat keras itu sendiri. Artinya, private key kamu tidak pernah terekspos ke lingkungan yang berpotensi rentan.

Dompet perangkat keras memberi perlindungan ganda bagi pengguna: pertama, mereka menjaga bitcoin kamu dari serangan jarak jauh dengan menyimpan private key secara offline; kedua, mereka biasanya memiliki perlindungan fisik yang lebih kuat terhadap upaya untuk mengekstrak kunci. Berdasarkan dua aspek keamanan ini, kamu bisa menilai dan membandingkan berbagai model yang tersedia di pasaran.

Dalam tutorial ini, aku akan mengajak kamu mengenal salah satu solusi tersebut: **Ledger Flex.**

![LEDGER FLEX](assets/notext/01.webp)

## Pengenalan ke Ledger Flex

Ledger Flex adalah dompet perangkat keras yang diproduksi oleh perusahaan Prancis Ledger, dipasarkan dengan harga 249 €.

![LEDGER FLEX](assets/notext/02.webp)

Fitur ini mencakup layar sentuh E Ink besar, teknologi tampilan hitam putih. Ini adalah teknologi yang sama yang ditemukan dalam pembaca elektronik. Ledger Flex menggunakan layar E Ink, yang memungkinkan tampilan tetap jelas dan mudah dibaca bahkan di bawah sinar matahari langsung. Layar ini juga sangat hemat daya, atau bahkan tidak mengonsumsi energi sama sekali saat tampilan tidak berubah. Teknologinya bekerja dengan mikrokapsul berisi partikel pigmen hitam dan putih. Ketika diberi muatan listrik, partikel-partikel ini bergerak ke permukaan layar, menampilkan teks atau gambar yang diinginkan.

Ledger Flex dilengkapi dengan chip Secure Element bersertifikat CC EAL6+, yang memberikan perlindungan tingkat lanjut terhadap serangan fisik pada perangkat keras. Layar E Ink ini dikontrol langsung oleh chip tersebut. Salah satu kritik umum terhadap pendekatan ini adalah bahwa kode di dalam chip tersebut tidak bersifat open-source, sehingga pengguna perlu menaruh tingkat kepercayaan tertentu pada integritas komponen tersebut. Namun, chip ini telah diaudit oleh para ahli independen untuk memastikan keamanannya.

Dari sisi penggunaan, Ledger Flex menyediakan beberapa opsi konektivitas: Bluetooth, USB-C, dan NFC. Layar yang besar membuat kamu lebih mudah memverifikasi detail transaksi. Ledger juga dikenal cepat mengadopsi fitur-fitur baru Bitcoin, seperti Miniscript, misalnya.

Setelah aku mencobanya sendiri, aku cukup terkesan dengan kualitas produknya. Pengalaman pengguna terasa halus, intuitif, dan desainnya solid. Ledger Flex benar-benar dompet perangkat keras yang sangat baik. Tapi, menurutku, ada dua kelemahan utama: pertama, ketidakmampuan untuk memverifikasi kode dalam chip Secure Element; dan kedua, harganya yang cukup tinggi dibandingkan kompetitornya. Sebagai perbandingan, model paling canggih dari Foundation dijual sekitar $199, Coinkite sekitar $219,99, sementara Trezor terbaru dengan layar sentuh besar ditawarkan sekitar 169€

## Bagaimana Cara Membeli Ledger Flex?
Ledger Flex dapat dibeli [di situs resmi](https://shop.ledger.com/pages/ledger-flex). Untuk membelinya di toko fisik, kamu juga bisa menemukan [daftar reseller bersertifikat](https://www.ledger.com/reseller) di situs web Ledger.
## Prasyarat

Setelah kamu menerima Ledger Flex milikmu, langkah pertama adalah memeriksa kemasannya untuk memastikan belum dibuka.

![LEDGER FLEX](assets/notext/03.webp)

Kemasan Ledger seharusnya menyertakan dua strip segel keamanan. Kalau salah satu strip ini hilang atau rusak, itu bisa jadi tanda bahwa dompet perangkat keras kamu telah dikompromikan dan kemungkinan besar tidak asli.

![LEDGER FLEX](assets/notext/04.webp)

Setelah dibuka, kamu seharusnya menemukan item berikut di dalam kotak:
- Ledger Flex;
- Kabel USB-C;
- Buku panduan pengguna;
- Kartu untuk menuliskan frasa mnemonik milikmu.

![LEDGER FLEX](assets/notext/05.webp)

Untuk tutorial ini, kamu akan memerlukan 2 perangkat lunak: Ledger Live untuk menginisialisasi Ledger Flex, dan Sparrow Wallet untuk mengelola dompet Bitcoinmu. Unduh [Ledger Live](https://www.ledger.com/ledger-live) dan [Sparrow Wallet](https://sparrowwallet.com/download/) dari situs web resmi mereka.

![LEDGER FLEX](assets/notext/06.webp)
Kami akan segera merilis tutorial tentang cara memverifikasi keaslian dan integritas perangkat lunak yang kamu unduh. Aku sangat menyarankan kamu untuk melakukan verifikasi ini, terutama untuk Ledger Live dan Sparrow.
## Bagaimana Cara Menginisialisasi Ledger Flex dengan Ledger Live?

Nyalakan Ledger Flex dengan menekan tombol sisi kanan selama beberapa detik.

![LEDGER FLEX](assets/notext/07.webp)

Scroll melalui berbagai halaman pengantar.

![LEDGER FLEX](assets/notext/08.webp)

Pilih opsi "*Set up without Ledger Live*", kemudian klik tombol "*Skip Ledger Live*".

![LEDGER FLEX](assets/notext/09.webp)

Kamu akan diminta untuk memilih nama untuk Ledger milikmu. Klik pada "*Set name*", dan kemudian masukkan nama pilihan Anda.

![LEDGER FLEX](assets/notext/10.webp)

Pilih kode PIN untuk perangkat kamu. Kode ini digunakan untuk membuka kunci Ledger kamu dan berfungsi sebagai perlindungan terhadap akses fisik yang tidak sah. PIN ini tidak berperan dalam proses derivasi kunci kriptografis dompet kamu. Jadi, meskipun kamu kehilangan akses ke kode PIN, kamu tetap bisa memulihkan bitcoin kamu selama masih memiliki seedphrase 24 kata.

Disarankan untuk memilih PIN dengan 8 digit yang benar-benar acak. Pastikan juga kamu menyimpannya di tempat yang terpisah dari Ledger Flex kamu, misalnya di dalam pengelola kata sandi.

![LEDGER FLEX](assets/notext/11.webp)

Masukkan PIN untuk kedua kalinya untuk mengonfirmasinya.

![LEDGER FLEX](assets/notext/12.webp)

Kemudian kamu akan diminta untuk memilih antara memulihkan dompet yang ada atau membuat yang baru. Dalam tutorial ini, kami membahas membuat dompet baru dari awal, jadi pilih opsi "*Set up as a new Ledger*" untuk menghasilkan frasa mnemonik baru.

![LEDGER FLEX](assets/notext/13.webp)

Ledger Flex kamu akan memberikan instruksi tentang cara mengelola seedphrase pemulihan kamu.
Seedphrase ini memberikan akses penuh dan tak terbatas ke semua bitcoin kamu. **Siapa pun yang memiliki seedphrase ini bisa mencuri dana kamu, bahkan tanpa akses fisik ke Ledger kamu.** Seedphrase 24 kata memungkinkan pemulihan akses ke bitcoin kamu jika Ledger Flex hilang, dicuri, atau rusak. Oleh karena itu sangat penting untuk menyimpan seedphrase ini di tempat yang aman dan merawatnya dengan sangat hati-hati.
Kamu bisa menuliskannya pada kertas karton yang disertakan bersama Ledger, atau untuk keamanan ekstra aku sarankan mengukirnya pada media stainless steel untuk melindungi dari risiko kebakaran, banjir, atau kerusakan fisik.

Kamu dapat menelusuri instruksi ini dan melewati halaman dengan menyentuh layar.

![LEDGER FLEX](assets/notext/14.webp)
Ledger akan membuat seedphrase kamu menggunakan generator angka acak pada perangkat. Pastikan kamu tidak sedang diamati selama proses ini. Tuliskan kata-kata yang disediakan Ledger pada media fisik pilihanmu. Tergantung strategi keamananmu, kamu bisa mempertimbangkan membuat beberapa salinan fisik lengkap dari seedphrase tersebut, tetapi yang paling penting, jangan membagikannya. Penting untuk menjaga kata-kata itu bernomor dan berurutan.

***Jelas, kamu tidak boleh pernah membagikan kata-kata ini di internet, berbeda dengan apa yang aku lakukan dalam tutorial ini. Dompet contoh ini hanya akan digunakan di Testnet dan akan dihapus di akhir tutorial.***

![LEDGER FLEX](assets/notext/15.webp)

Untuk berpindah ke kelompok kata berikutnya, klik tombol "*Next*". Setelah semua kata dicatat, klik tombol "*Done*" untuk melanjutkan ke langkah selanjutnya.

![LEDGER FLEX](assets/notext/16.webp)

Klik tombol "*Start confirmation*", lalu pilih kata-kata dari frasa mnemonik sesuai urutannya untuk mengonfirmasi bahwa kamu telah mencatatnya dengan benar. Lanjutkan prosedur ini sampai kata ke-24.

![LEDGER FLEX](assets/notext/17.webp)

Jika seedphrase yang kamu konfirmasi persis sama dengan yang ditampilkan oleh Flex pada langkah sebelumnya, kamu bisa melanjutkan prosesnya. Tapi kalau tidak cocok, itu berarti cadangan fisik seedphrase kamu salah, dan kamu harus mengulang proses dari awal.

![LEDGER FLEX](assets/notext/18.webp)

Dan begitulah, seedphrase kamu sudah berhasil dibuat di Ledger Flex. Sebelum lanjut membuat dompet Bitcoin baru dari seed ini, mari kita jelajahi dulu pengaturan perangkatnya bareng-bareng.

## Bagaimana cara mengubah pengaturan Ledger Anda?

Untuk mengunci atau membuka kunci Ledger kamu, cukup tekan tombol di samping perangkat. Setelah itu, kamu akan diminta memasukkan kode PIN yang sudah kamu buat di langkah sebelumnya.

![LEDGER FLEX](assets/notext/19.webp)

Untuk mengakses pengaturan, klik pada simbol roda gigi di bagian bawah kiri perangkat.

![LEDGER FLEX](assets/notext/20.webp)

Menu "*Name*" memungkinkanmu untuk mengubah nama Ledger milikmu.

![LEDGER FLEX](assets/notext/21.webp)

Di "*About this Ledger*," Kamu akan menemukan informasi tentang Flex milikmu.

![LEDGER FLEX](assets/notext/22.webp)

Di menu *Lock screen*, kamu bisa mengubah gambar yang ditampilkan di layar kunci dengan memilih opsi *Customize lock screen picture*. Berkat teknologi layar E Ink, perangkat ini bisa mempertahankan tampilan di layar tanpa mengonsumsi baterai. Layar E Ink tidak membutuhkan energi untuk menampilkan gambar statis, hanya saat tampilan berubah.

Submenu *Auto-lock* memungkinkan kamu mengatur dan mengaktifkan penguncian otomatis Ledger setelah periode tidak aktif yang kamu tentukan.

![LEDGER FLEX](assets/notext/23.webp)

Menu "*Sounds*" memungkinkan Anda untuk mengaktifkan atau menonaktifkan suara pada Flex Anda. Dan di menu "Language", Anda dapat mengubah bahasa tampilan.

![LEDGER FLEX](assets/notext/24.webp)

Dengan mengklik panah kanan, kamu bisa mengakses pengaturan lainnya. "*Change PIN*" berfungsi untuk mengubah kode PIN kamu.

![LEDGER FLEX](assets/notext/25.webp)

Menu "*Bluetooth*" dan "*NFC*" memungkinkanmu untuk mengelola komunikasi ini.

![LEDGER FLEX](assets/notext/26.webp)

Di "*Battery*" kamu dapat mengatur penonaktifan otomatis Ledger.

![LEDGER FLEX](assets/notext/27.webp)

Bagian "*Advanced*" memberimmu akses ke pengaturan keamanan yang lebih canggih. Disarankan untuk menjaga opsi "*PIN shuffle*" tetap aktif untuk meningkatkan keamanan. Juga di menu ini kamu dapat mengonfigurasi passphrase BIP39.

![LEDGER FLEX](assets/notext/28.webp)

Passphrase adalah kata sandi opsional yang, bila dikombinasikan dengan seedphrase, memberikan lapisan keamanan tambahan untuk dompet kamu.

Saat ini, dompet kamu dibuat dari seedphrase yang terdiri dari 24 kata. Seedphrase ini sangat penting karena memungkinkan kamu memulihkan semua kunci dompet jika perangkat hilang. Namun, seedphrase juga merupakan single point of failure (SPOF) — jika seedphrase kamu jatuh ke tangan orang lain, bitcoin kamu dalam bahaya. Di sinilah passphrase berperan. Ini adalah kata sandi opsional yang bisa kamu pilih sendiri, dan akan digabungkan dengan seedphrase untuk memperkuat keamanan dompet.

Passphrase tidak boleh disamakan dengan PIN, karena passphrase benar-benar berperan dalam proses derivasi kunci kriptografis. Ia bekerja bersama seedphrase untuk memodifikasi seed dasar tempat semua kunci dihasilkan. Jadi, meskipun seseorang memiliki seedphrase 24 kata kamu, tanpa passphrase mereka tetap tidak bisa mengakses dana kamu. Menggunakan passphrase pada dasarnya menciptakan dompet baru dengan kunci yang berbeda. Bahkan perubahan kecil pada passphrase akan menghasilkan dompet yang sepenuhnya berbeda.

Passphrase adalah alat yang sangat kuat untuk meningkatkan keamanan bitcoin kamu. Tapi penting banget buat benar-benar memahami cara kerjanya sebelum digunakan, supaya kamu tidak kehilangan akses ke dompet sendiri. Aku akan jelaskan cara memakai passphrase ini dalam tutorial khusus lainnya.

![LEDGER FLEX](assets/notext/29.webp)

Passphrase adalah alat yang sangat kuat untuk memperkuat keamanan bitcoin kamu. Namun penting sekali untuk memahami cara kerjanya sebelum menerapkannya agar kamu tidak kehilangan akses ke dompet kamu. Itulah sebabnya aku menjelaskannya secara lengkap dalam tutorial terpisah berikut:

https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

Terakhir, halaman pengaturan ini memungkinkan kamu untuk mereset Ledger kamu. Lakukan reset hanya jika kamu benar-benar yakin perangkat tersebut tidak menyimpan kunci apa pun yang mengamankan bitcoin kamu, karena tindakan ini bisa menyebabkan kamu kehilangan akses ke dana secara permanen.

![LEDGER FLEX](assets/notext/30.webp)

## Bagaimana cara menginstal aplikasi Bitcoin?

Mulailah dengan meluncurkan perangkat lunak Ledger Live di komputer kamu, kemudian sambungkan dan buka kunci Ledger Flex kamu.

![LEDGER FLEX](assets/notext/31.webp)

Di Ledger Live, pergi ke menu "*My Ledger*". Kamu akan diminta untuk mengizinkan akses ke Flex milikmu.

![LEDGER FLEX](assets/notext/32.webp)

Validasi akses pada Ledger kamu dengan mengklik tombol "*Allow*".

![LEDGER FLEX](assets/notext/33.webp)

Pertama, jika firmware Ledger Flex kamu tidak terbaru, Ledger Live secara otomatis akan menawarkan untuk memperbaruinya. Jika berlaku, klik pada "*Update firmware*", kemudian pada "*Install update*" untuk memulai instalasi.

![LEDGER FLEX](assets/notext/34.webp)

Di Ledger kamu, klik pada tombol "*Install*", lalu tunggu selama instalasi.

![LEDGER FLEX](assets/notext/35.webp)

Firmware Ledger Flex kamu sekarang sudah terbaru.

![LEDGER FLEX](assets/notext/36.webp)

Kalau kamu ingin, kamu bisa mengubah wallpaper layar kunci Ledger Flex. Untuk melakukan ini, klik pada "*Add >*".

![LEDGER FLEX](assets/notext/37.webp)

Klik tombol "*Upload from computer*" dan pilih wallpaper dari foto-foto milikmu.

![LEDGER FLEX](assets/notext/38.webp)

Kamu bisa memotong milikmu

![LEDGER FLEX](assets/notext/39.webp)

Pilih kontras dari berbagai opsi, kemudian klik pada "*Confirm contrast*".

![LEDGER FLEX](assets/notext/40.webp)

Lalu, klik pada tombol "*Load picture*".

![LEDGER FLEX](assets/notext/41.webp)

Kalau kamu puas dengan gambar tersebut, klik pada "*Keep*" untuk mengaturnya sebagai wallpaper layar kunci.

![LEDGER FLEX](assets/notext/42.webp)

Akhirnya, kami akan menambahkan aplikasi Bitcoin. Untuk melakukan ini, di Ledger Live, klik pada tombol "*Install*" di sebelah "*Bitcoin (BTC)*".

![LEDGER FLEX](assets/notext/43.webp)

Aplikasi akan terinstal di Flex Anda.

![LEDGER FLEX](assets/notext/44.webp)

Mulai sekarang, kamu tidak lagi memerlukan perangkat lunak Ledger Live untuk pengelolaan dompet sehari-hari. Kamu hanya perlu membukanya sesekali untuk memperbarui firmware jika ada versi baru yang dirilis. Untuk semua kebutuhan lainnya, kita akan menggunakan Sparrow Wallet, yang merupakan alat yang jauh lebih lengkap dan efisien untuk mengelola dompet Bitcoin.

## Bagaimana cara menyiapkan dompet Bitcoin baru dengan Sparrow?
Buka Sparrow Wallet dan lewati halaman pengantar untuk mengakses layar utama. Periksa bahwa kalau benar-benar terhubung ke sebuah node dengan mengamati sakelar yang terletak di pojok kanan bawah layar.
![LEDGER FLEX](assets/notext/45.webp)

ChatGPT said:

Aku sangat menyarankan kamu untuk menggunakan node Bitcoin kamu sendiri. Dalam tutorial ini, aku menggunakan node publik (kuning) karena sedang berada di testnet, tapi untuk penggunaan normal, sebaiknya pilih Bitcoin Core lokal (hijau) atau server Electrum yang terhubung ke node pribadi jarak jauh (biru).

Klik pada menu "*File*" kemudian "*New Wallet*".

![LEDGER FLEX](assets/notext/46.webp)

Pilih nama untuk dompet ini, kemudian klik pada "*Create Wallet*".

![LEDGER FLEX](assets/notext/47.webp)

Dalam menu dropdown "*Script Type*", pilih jenis skrip yang akan digunakan untuk mengamankan bitcoin kamu. Kamu merekomendasikan untuk memilih "*Taproot*", atau jika tidak tersedia, "*Native SegWit*".

![LEDGER FLEX](assets/notext/48.webp)

Klik pada tombol "*Connected Hardware Wallet*".

![LEDGER FLEX](assets/notext/49.webp)

Hubungkan Ledger Flex kamu ke komputer, buka kunci dengan kode PIN milikmu, kemudian buka aplikasi "*Bitcoin*". Dalam tutorial ini, aku menggunakan aplikasi "*Bitcoin Testnet*", tetapi prosedurnya tetap sama untuk mainnet.

![LEDGER FLEX](assets/notext/50.webp)

Di Sparrow, klik pada tombol "*Scan*".

![LEDGER FLEX](assets/notext/51.webp)

Kemudian klik pada "*Import Keystore*".

![LEDGER FLEX](assets/notext/52.webp)

Sekarang kamu bisa melihat detail dompet kamu, termasuk extended public key dari akun pertamamu. Klik tombol *Apply* untuk menyelesaikan proses pembuatan dompet.
![LEDGER FLEX](assets/notext/53.webp)

Pilih kata sandi yang kuat untuk mengamankan akses ke Sparrow Wallet. Kata sandi ini akan melindungi data dompet kamu di Sparrow, termasuk public key, alamat, label, dan riwayat transaksi dari akses yang tidak sah.

Aku sarankan kamu menyimpan kata sandi ini di pengelola kata sandi, supaya tidak lupa dan tetap aman.

![LEDGER FLEX](assets/notext/54.webp)

Dan begitulah, dompet kamu sekarang telah dibuat!

![LEDGER FLEX](assets/notext/55.webp)

Sebelum menerima bitcoin pertama kamu di dompet, aku sangat menyarankan untuk melakukan tes pemulihan kering terlebih dahulu. Catat informasi referensi seperti xpub kamu, lalu reset Ledger Flex saat dompet masih kosong. Setelah itu, coba pulihkan dompet di Ledger menggunakan cadangan kertas yang kamu punya. Periksa apakah xpub yang muncul setelah pemulihan sama dengan yang kamu catat sebelumnya. Kalau cocok, berarti cadangan kertas kamu bisa diandalkan sepenuhnya.

## Bagaimana cara menerima bitcoin dengan Ledger Flex?

Klik pada tab "*Receive*".

![LEDGER FLEX](assets/notext/56.webp)

Hubungkan Ledger Flex ke komputer, buka kunci dengan kode PIN, kemudian buka aplikasi "*Bitcoin*".

![LEDGER FLEX](assets/notext/57.webp)

Sebelum menggunakan alamat yang ditampilkan di Sparrow Wallet, pastikan kamu memverifikasinya langsung di layar Ledger Flex kamu. Langkah ini penting untuk memastikan bahwa alamat yang muncul di Sparrow benar-benar valid dan bukan hasil manipulasi, serta memastikan bahwa Ledger kamu memang memiliki private key yang diperlukan untuk menghabiskan bitcoin yang diamankan dengan alamat tersebut nantinya.

Untuk melakukan verifikasi ini, klik pada tombol "*Display Address*".

![LEDGER FLEX](assets/notext/58.webp)

Pastikan alamat yang ditampilkan di Ledger Flex kamu benar-benar sama dengan yang muncul di Sparrow Wallet. Disarankan juga untuk melakukan verifikasi ini tepat sebelum kamu memberikan alamat tersebut kepada pengirim, supaya kamu bisa memastikan alamatnya valid dan aman.

![LEDGER FLEX](assets/notext/59.webp)

Kamu dapat menambahkan "*Label*" untuk menggambarkan sumber bitcoin yang akan diamankan dengan alamat ini. Ini adalah praktik yang baik yang membantu kamu mengelola UTXO Anda dengan lebih baik.

![LEDGER FLEX](assets/notext/60.webp)

Untuk informasi lebih lanjut tentang pelabelan, aku juga menyarankanmu untuk melihat tutorial lain ini:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Kemudian kamu dapat menggunakan alamat ini untuk menerima bitcoin.

![LEDGER FLEX](assets/notext/61.webp)

## Bagaimana cara mengirim bitcoin dengan Ledger Flex?

Sekarang setelah kamu menerima sats pertama di dompet yang diamankan dengan Ledger Flex, kamu juga bisa mulai menggunakannya! Hubungkan Ledger kamu ke komputer, buka kuncinya, jalankan Sparrow Wallet, lalu buka tab *Send* untuk membuat transaksi baru.

![LEDGER FLEX](assets/notext/62.webp)

Kalau kamu ingin melakukan "*coin control*", yaitu secara spesifik memilih UTXO mana yang akan dikonsumsi dalam transaksi, pergi ke tab "*UTXOs*". Pilih UTXO yang ingin kamu habiskan, kemudian klik pada "*Send Selected*". Kamu akan diarahkan ke layar yang sama dari tab "*Send*", tetapi dengan UTXO Anda sudah dipilih untuk transaksi.
![LEDGER FLEX](assets/notext/63.webp)
Masukkan alamat tujuan. Kamu juga dapat memasukkan beberapa alamat dengan mengklik tombol "*+ Add*".

![LEDGER FLEX](assets/notext/64.webp)

Catat sebuah "*Label*" untuk mengingat tujuan pengeluaran ini.
Pilih jumlah yang akan dikirim ke alamat ini.

Sesuaikan tarif biaya transaksi kamu sesuai dengan pasar saat ini.

Pastikan semua pengaturan transaksi kamu sudah benar, kemudian klik pada "*Buat Transaksi*".

Jika semuanya sesuai dengan keinginanmu, klik pada "*Finalisasi Transaksi untuk Ditandatangani*".

Klik pada "*Tandatangan*".

Klik pada "*Tandatangan*" di sebelah Ledger Flex kamu.

Verifikasi pengaturan transaksi di layar Flex, termasuk alamat penerima, jumlah yang dikirim, dan jumlah biaya.

Untuk menandatangani, tahan jari pada tombol "*Tahan untuk menandatangani*".

Sekarang transaksi sudah ditandatangani. Klik pada "*Siarkan Transaksi*" untuk menyiarkannya di jaringan Bitcoin.

Kamu dapat menemukannya di tab "*Transaksi*" dari Sparrow Wallet.

Selamat, sekarang kamu sudah menguasai penggunaan dasar Ledger Flex dengan Sparrow Wallet! Di tutorial berikutnya, kita akan membahas cara menggunakan Ledger Flex dengan Liana untuk memanfaatkan fitur Miniscript.

Kalau kamu merasa tutorial ini bermanfaat, aku akan sangat menghargai kalau kamu kasih jempol ke atas di bawah ini. Jangan ragu buat membagikan artikel ini di media sosial kamu. Terima kasih banyak!
