---
name: Ledger Flex
description: Mengatur dan menggunakan Ledger Flex
---
![cover](assets/cover.webp)

Dompet perangkat keras adalah perangkat elektronik yang khusus dibuat untuk mengelola dan mengamankan kunci privat dari dompet Bitcoin. Berbeda dengan dompet perangkat lunak (atau dompet panas) yang terpasang di mesin umum yang sering terhubung ke Internet, dompet perangkat keras memungkinkan isolasi fisik kunci privat, sehingga risiko peretasan dan pencurian berkurang.

Tujuan utama dompet perangkat keras adalah meminimalkan fungsionalitas perangkat untuk mengecilkan permukaan serangan. Permukaan serangan yang lebih kecil berarti vektor serangan potensial lebih sedikit, yaitu, titik lemah dalam sistem yang bisa dieksploitasi oleh penyerang untuk mengakses bitcoin lebih terbatas.

Disarankan menggunakan dompet perangkat keras untuk mengamankan bitcoin kamu, terutama jika jumlahnya signifikan, baik dalam nilai absolut maupun sebagai proporsi dari total aset kamu.

Dompet perangkat keras digunakan bersamaan dengan perangkat lunak manajemen dompet di komputer atau smartphone. Perangkat lunak ini mengatur pembuatan transaksi, tetapi tanda tangan kriptografis yang diperlukan untuk memvalidasi transaksi hanya dilakukan di dalam dompet perangkat keras. Ini memastikan bahwa kunci privat tidak pernah terekspos ke lingkungan yang berpotensi rentan.

Dompet perangkat keras memberikan perlindungan ganda bagi pengguna: di satu sisi, mereka menjaga bitcoin kamu dari serangan jarak jauh dengan kunci privat tetap offline, dan di sisi lain, mereka biasanya lebih tahan terhadap upaya fisik untuk mengekstrak kunci. Berdasarkan dua kriteria keamanan ini, seseorang bisa menilai dan membandingkan model-model yang tersedia di pasar.

Dalam tutorial ini, aku akan menunjukkan salah satu solusi ini: **Ledger Flex**.


![LEDGER FLEX](assets/notext/01.webp)

## Pengenalan ke Ledger Flex

Ledger Flex adalah dompet perangkat keras yang diproduksi oleh perusahaan Prancis Ledger, dipasarkan dengan harga 249 €.

![LEDGER FLEX](assets/notext/02.webp)

Fitur ini mencakup layar sentuh E Ink besar, teknologi tampilan hitam putih yang sama dengan yang ditemukan di pembaca elektronik. Layar E Ink memungkinkan tampilan yang jelas dan mudah dibaca, bahkan di bawah cahaya matahari terang, dan mengonsumsi sangat sedikit energi, atau sama sekali tidak ada ketika layar statis. Cara kerjanya menggunakan mikrokapsul berisi partikel pigmen hitam dan putih. Saat muatan listrik diterapkan, partikel hitam atau putih bergerak ke permukaan layar, sehingga teks atau gambar terbentuk.

Ledger Flex dilengkapi dengan chip "elemen aman" bersertifikat CC EAL6+, memberikan perlindungan lanjutan terhadap serangan fisik pada perangkat keras. Layar dikontrol langsung oleh chip ini. Salah satu kritik umum adalah kode untuk chip ini tidak bersifat open-source, sehingga memerlukan tingkat kepercayaan tertentu pada integritas komponen. Namun, elemen ini diaudit oleh para ahli independen.

Dalam penggunaan sehari-hari, Ledger Flex menawarkan beberapa opsi konektivitas: Bluetooth, USB-C, dan NFC. Layar besar memudahkan verifikasi detail transaksi kamu. Ledger juga menonjol dari pesaingnya dengan adopsi cepat terhadap fitur Bitcoin baru, seperti Miniscript.

Setelah mengujinya, aku terkesan dengan kualitas produk. Pengalaman pengguna sangat baik, dan perangkatnya intuitif. Ini adalah dompet perangkat keras yang sangat baik. Namun, menurutku, ada 2 kelemahan utama: ketidakmampuan untuk memverifikasi kode chip dan, tentu saja, harganya, yang secara signifikan lebih tinggi dibanding pesaing. Untuk perbandingan, model paling canggih dari Foundation dijual seharga $199, Coinkite $219,99, sementara Trezor terbaru, yang juga dilengkapi layar sentuh besar, ditawarkan dengan harga 169€.


## Bagaimana Cara Membeli Ledger Flex?
Ledger Flex dapat dibeli [di situs resmi](https://shop.ledger.com/pages/ledger-flex). Untuk membelinya di toko fisik, Anda juga dapat menemukan [daftar reseller bersertifikat](https://www.ledger.com/reseller) di situs web Ledger.
## Prasyarat

Setelah Anda menerima Ledger Flex Anda, langkah pertama adalah memeriksa kemasannya untuk memastikan belum dibuka.

![LEDGER FLEX](assets/notext/03.webp)

Kemasan Ledger harus mencakup 2 strip segel. Jika strip ini hilang atau rusak, itu bisa menunjukkan bahwa dompet perangkat keras telah dikompromikan dan mungkin tidak asli.

![LEDGER FLEX](assets/notext/04.webp)

Setelah dibuka, kamu seharusnya menemukan item berikut di dalam kotak:
- **Ledger Flex**;
- Kabel USB-C;
- Buku panduan pengguna;
- Kartu untuk menuliskan **seedphrase** kamu.

![LEDGER FLEX](assets/notext/05.webp)

Untuk tutorial ini, Anda akan memerlukan 2 perangkat lunak: Ledger Live untuk menginisialisasi Ledger Flex, dan Sparrow Wallet untuk mengelola dompet Bitcoin Anda. Unduh [Ledger Live](https://www.ledger.com/ledger-live) dan [Sparrow Wallet](https://sparrowwallet.com/download/) dari situs web resmi mereka.

![LEDGER FLEX](assets/notext/06.webp)
Kami akan segera menawarkan tutorial tentang cara memverifikasi keaslian dan integritas perangkat lunak yang kamu unduh. Aku sangat menyarankan untuk melakukannya di sini untuk **Ledger Live** dan **Sparrow**.

## Bagaimana Cara Menginisialisasi Ledger Flex dengan Ledger Live?

Nyalakan Ledger Flex Anda dengan menekan tombol sisi kanan selama beberapa detik.

![LEDGER FLEX](assets/notext/07.webp)

Gulir melalui berbagai halaman pengantar.

![LEDGER FLEX](assets/notext/08.webp)

Pilih opsi "*Set up without Ledger Live*", kemudian klik tombol "*Skip Ledger Live*".

![LEDGER FLEX](assets/notext/09.webp)

Anda kemudian akan diminta untuk memilih nama untuk Ledger Anda. Klik pada "*Set name*", dan kemudian masukkan nama pilihan Anda.

![LEDGER FLEX](assets/notext/10.webp)

Pilih kode PIN untuk perangkat kamu, yang akan digunakan untuk membuka kunci **Ledger** kamu. Ini berfungsi sebagai perlindungan terhadap akses fisik yang tidak sah. Kode PIN ini tidak memengaruhi derivasi kunci kriptografis dompet kamu. Dengan demikian, bahkan tanpa akses ke kode PIN, memiliki **seedphrase** 24 kata kamu akan memungkinkan kamu mendapatkan kembali akses ke bitcoin.

Disarankan memilih kode PIN 8 digit yang seacak mungkin. Pastikan juga untuk menyimpan kode ini di tempat berbeda dari lokasi penyimpanan **Ledger Flex** kamu (misalnya, di pengelola kata sandi).


![LEDGER FLEX](assets/notext/11.webp)

Masukkan PIN Anda untuk kedua kalinya untuk mengonfirmasinya.

![LEDGER FLEX](assets/notext/12.webp)

Kamu kemudian akan diminta untuk memilih antara memulihkan dompet yang ada atau membuat yang baru. Dalam tutorial ini, kita akan membuat dompet baru dari awal, jadi pilih opsi "*Set up as a new Ledger*" untuk menghasilkan **seedphrase** baru.

![LEDGER FLEX](assets/notext/13.webp)

**Flex** kamu akan memberikan instruksi tentang cara mengelola **seedphrase** kamu.  
**Seedphrase ini memberikan akses penuh dan tak terbatas ke semua bitcoin kamu**. Siapapun yang memilikinya bisa mencuri dana kamu, bahkan tanpa akses fisik ke **Ledger** kamu. Frasa 24 kata ini memungkinkan pemulihan akses ke bitcoin jika **Ledger Flex** hilang, dicuri, atau rusak. Oleh karena itu, sangat penting untuk menyimpannya dengan aman dan hati-hati.

Kamu bisa menuliskannya di kartu kertas yang disediakan bersama **Ledger**, atau untuk keamanan tambahan, aku menyarankan mengukirnya pada media stainless steel untuk melindungi dari risiko kebakaran, banjir, atau kerusakan fisik.

Kamu bisa menjelajahi instruksi ini dan melewati halaman dengan menyentuh layar.


![LEDGER FLEX](assets/notext/14.webp)
**Ledger** akan membuat **seedphrase** kamu menggunakan generator angka acak. Pastikan tidak ada yang mengamati selama proses ini. Tuliskan kata-kata yang diberikan **Ledger** pada media fisik pilihan kamu. Tergantung strategi keamanan kamu, pertimbangkan untuk membuat beberapa salinan fisik lengkap dari frasa tersebut (tetapi yang paling penting, jangan dibagikannya). Penting untuk menjaga kata-kata tetap bernomor dan berurutan.

***Jelas, kamu seharusnya tidak pernah membagikan kata-kata ini di internet, berbeda dengan apa yang aku lakukan dalam tutorial ini. Dompet contoh ini hanya digunakan di Testnet dan akan dihapus di akhir tutorial.***


![LEDGER FLEX](assets/notext/15.webp)

Untuk berpindah ke kelompok kata berikutnya, klik tombol "*Next*". Setelah semua kata dicatat, klik tombol "*Done*" untuk melanjutkan ke langkah berikutnya.

![LEDGER FLEX](assets/notext/16.webp)

Klik tombol "*Start confirmation*", lalu pilih kata-kata dari **seedphrase** kamu sesuai urutannya untuk mengonfirmasi bahwa kamu telah mencatatnya dengan benar. Lanjutkan prosedur ini sampai kata ke-24.

![LEDGER FLEX](assets/notext/17.webp)

Jika frasa yang kamu konfirmasi cocok persis dengan yang diberikan **Flex** pada langkah sebelumnya, kamu bisa melanjutkan. Jika tidak, ini berarti cadangan fisik **seedphrase** kamu salah dan kamu perlu memulai proses dari awal.

![LEDGER FLEX](assets/notext/18.webp)

Dan begitulah, **seed** kamu telah berhasil dibuat di **Ledger Flex** kamu. Sebelum melanjutkan untuk membuat dompet Bitcoin baru dari seed ini, mari kita jelajahi pengaturan perangkat bersama-sama.

## Bagaimana cara mengubah pengaturan Ledger kamu?

Untuk mengunci dan membuka kunci **Ledger** kamu, tekan tombol samping. Kamu kemudian akan diminta memasukkan kode PIN yang telah kamu tetapkan pada langkah sebelumnya.

![LEDGER FLEX](assets/notext/19.webp)

Untuk mengakses pengaturan, klik pada simbol roda gigi di bagian bawah kiri perangkat kamu.

![LEDGER FLEX](assets/notext/20.webp)

Menu "*Name*" memungkinkanmu untuk mengubah nama Ledger kamu.

![LEDGER FLEX](assets/notext/21.webp)

Di "*About this Ledger*," kamu akan menemukan informasi tentang Flex kamu.

![LEDGER FLEX](assets/notext/22.webp)

Di menu "*Lock screen*", kamu punya opsi untuk mengubah gambar yang ditampilkan pada layar kunci dengan memilih "*Customize lock screen picture*". Berkat teknologi layar E Ink pada perangkat, layar bisa tetap menyala tanpa mengonsumsi baterai. Layar E Ink tidak menggunakan energi untuk mempertahankan gambar statis. Namun, layar ini tetap mengonsumsi energi saat tampilan berubah.

Submenu "*Auto-lock*" memungkinkan kamu mengatur dan mengaktifkan penguncian otomatis **Ledger** kamu setelah periode tidak aktif yang ditentukan.

![LEDGER FLEX](assets/notext/23.webp)
Menu "*Sounds*" memungkinkan kamu mengaktifkan atau menonaktifkan suara pada **Flex** kamu. Dan di menu "*Language*", kamu bisa mengubah bahasa tampilan.
![LEDGER FLEX](assets/notext/24.webp)

Dengan mengklik panah kanan, kamu bisa mengakses pengaturan lainnya. "*Change PIN*" memungkinkan kamu mengubah kode PIN kamu.

![LEDGER FLEX](assets/notext/25.webp)

Menu "*Bluetooth*" dan "*NFC*" memungkinkanmu untuk mengelola komunikasi ini.

![LEDGER FLEX](assets/notext/26.webp)

Di "*Battery*" kamu dapat mengatur penonaktifan otomatis Ledger.

![LEDGER FLEX](assets/notext/27.webp)

Bagian "*Advanced*" memberi kamu akses ke pengaturan keamanan yang lebih canggih. Disarankan untuk tetap mengaktifkan opsi "*PIN shuffle*" demi meningkatkan keamanan. Di menu ini juga kamu bisa mengonfigurasi passphrase BIP39.

![LEDGER FLEX](assets/notext/28.webp)

Passphrase adalah kata sandi opsional yang, jika digabungkan dengan **seedphrase**, memberikan lapisan keamanan tambahan untuk dompet kamu.

Saat ini, dompet kamu dihasilkan dari **seedphrase** yang terdiri dari 24 kata. Frasa pemulihan ini sangat penting karena memungkinkan kamu memulihkan semua kunci dompet jika terjadi kehilangan. Namun, ini juga merupakan single point of failure (SPOF). Jika dikompromikan, bitcoin kamu berada dalam bahaya. Di sinilah passphrase berperan. Ini adalah kata sandi opsional yang bisa kamu pilih secara bebas, yang ditambahkan ke **seedphrase** untuk memperkuat keamanan dompet.

Passphrase tidak boleh disamakan dengan kode PIN. Passphrase berperan dalam derivasi kunci kriptografis kamu. Ini bekerja bersama **seedphrase**, memodifikasi seed tempat kunci dihasilkan. Jadi, meskipun seseorang mendapatkan frasa 24 kata kamu, tanpa passphrase mereka tidak bisa mengakses dana kamu. Menggunakan passphrase pada dasarnya menciptakan dompet baru dengan kunci yang berbeda. Mengubah passphrase, bahkan sedikit saja, akan menghasilkan dompet yang berbeda.

Passphrase adalah alat yang sangat kuat untuk meningkatkan keamanan bitcoin kamu. Namun, sangat penting memahami cara kerjanya sebelum menggunakannya, agar tidak kehilangan akses ke dompet kamu. Aku akan menjelaskan cara menggunakan passphrase dalam tutorial khusus lainnya.


![LEDGER FLEX](assets/notext/29.webp)

Passphrase adalah alat yang sangat kuat untuk memperkuat keamanan bitcoin kamu. Namun, sangat penting untuk memahami cara kerjanya sebelum menggunakannya, agar tidak kehilangan akses ke dompet kamu. Itu sebabnya aku menjelaskannya secara lengkap dalam tutorial terpisah berikut:

https://planb.academy/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

Terakhir, halaman pengaturan memungkinkan kamu untuk mereset **Ledger** kamu. Lakukan reset ini hanya jika kamu yakin perangkat tidak menyimpan kunci apa pun yang mengamankan bitcoin, karena kamu bisa kehilangan akses ke dana secara permanen.
![LEDGER FLEX](assets/notext/30.webp)

## Bagaimana cara menginstal aplikasi Bitcoin?

Mulailah dengan meluncurkan perangkat lunak Ledger Live di komputer kamu, kemudian sambungkan dan buka kunci Ledger Flex kamu.

![LEDGER FLEX](assets/notext/31.webp)

Di Ledger Live, pergi ke menu "*My Ledger*". Kamu akan diminta untuk mengizinkan akses ke Flex kamu.

![LEDGER FLEX](assets/notext/32.webp)

Validasi akses pada Ledger kamu dengan mengklik tombol "*Allow*".

![LEDGER FLEX](assets/notext/33.webp)

Pertama, jika firmware **Ledger Flex** kamu belum versi terbaru, **Ledger Live** akan otomatis menawarkan pembaruan. Jika tersedia, klik "*Update firmware*", lalu "*Install update*" untuk memulai instalasi.

![LEDGER FLEX](assets/notext/34.webp)

Di Ledger kamu, klik pada tombol "*Install*", lalu tunggu selama instalasi.

![LEDGER FLEX](assets/notext/35.webp)

Firmware Ledger Flex kamu sekarang sudah terbaru.
![LEDGER FLEX](assets/notext/36.webp)
Jika mau, kamu bisa mengubah wallpaper layar kunci **Ledger Flex** kamu. Untuk melakukannya, klik "*Add >*".

![LEDGER FLEX](assets/notext/37.webp)

Klik tombol "*Upload from computer*" lalu pilih wallpaper kamu dari foto-foto kamu.

![LEDGER FLEX](assets/notext/38.webp)

Kamu dapat memotong gambar.

![LEDGER FLEX](assets/notext/39.webp)

Pilih kontras dari berbagai opsi, kemudian klik pada "*Confirm contrast*".

![LEDGER FLEX](assets/notext/40.webp)

Di Flex, klik pada tombol "*Load picture*".

![LEDGER FLEX](assets/notext/41.webp)

Jika kamu puas dengan gambar tersebut, klik pada "*Keep*" untuk mengaturnya sebagai wallpaper layar kunci.

![LEDGER FLEX](assets/notext/42.webp)

Akhirnya, kami akan menambahkan aplikasi Bitcoin. Untuk melakukan ini, di Ledger Live, klik pada tombol "*Install*" di sebelah "*Bitcoin (BTC)*".

![LEDGER FLEX](assets/notext/43.webp)

Aplikasi akan terinstal di Flex kamu.

![LEDGER FLEX](assets/notext/44.webp)

Mulai sekarang, kamu tidak lagi memerlukan perangkat lunak **:contentReference[oaicite:0]{index=0}** untuk pengelolaan dompet secara rutin. Kamu bisa kembali menggunakannya sesekali untuk memperbarui firmware ketika versi baru tersedia. Untuk hal lainnya, kita akan menggunakan **:contentReference[oaicite:1]{index=1}**, yang merupakan alat yang lebih komprehensif untuk mengelola dompet Bitcoin secara efisien.

## Bagaimana cara menyiapkan dompet Bitcoin baru dengan Sparrow?
Buka **Sparrow Wallet** dan lewati halaman pengantar untuk mengakses layar utama. Pastikan kamu benar-benar terhubung ke sebuah node dengan melihat sakelar yang berada di pojok kanan bawah layar.

![LEDGER FLEX](assets/notext/45.webp)

Aku sangat merekomendasikan menggunakan node Bitcoin kamu sendiri. Dalam tutorial ini, aku menggunakan node publik (kuning) karena berada di testnet, tetapi untuk penggunaan normal, lebih baik memilih **:contentReference[oaicite:0]{index=0}** lokal (hijau) atau server Electrum yang terhubung ke node jarak jauh (biru).

Klik pada menu "*File*" kemudian "*New Wallet*".

![LEDGER FLEX](assets/notext/46.webp)

Pilih nama untuk dompet ini, kemudian klik pada "*Create Wallet*".

![LEDGER FLEX](assets/notext/47.webp)

Dalam menu dropdown "*Script Type*", pilih jenis skrip yang akan digunakan untuk mengamankan bitcoin Anda. Saya merekomendasikan untuk memilih "*Taproot*", atau jika tidak tersedia, "*Native SegWit*".

![LEDGER FLEX](assets/notext/48.webp)

Klik pada tombol "*Connected Hardware Wallet*".

![LEDGER FLEX](assets/notext/49.webp)

Hubungkan **Ledger Flex** kamu ke komputer, buka kunci dengan kode PIN kamu, lalu buka aplikasi "*Bitcoin*". Dalam tutorial ini, aku menggunakan aplikasi "*Bitcoin Testnet*", tetapi prosedurnya tetap sama untuk mainnet.


![LEDGER FLEX](assets/notext/50.webp)

Di Sparrow, klik pada tombol "*Scan*".

![LEDGER FLEX](assets/notext/51.webp)

Kemudian klik pada "*Import Keystore*".

![LEDGER FLEX](assets/notext/52.webp)

Kamu sekarang bisa melihat detail dompet kamu, termasuk kunci publik yang diperluas dari akun pertama kamu. Klik tombol "*Apply*" untuk menyelesaikan pembuatan dompet.

![LEDGER FLEX](assets/notext/53.webp)
Pilih kata sandi yang kuat untuk mengamankan akses ke **Sparrow Wallet**. Kata sandi ini menjaga keamanan akses ke data dompet kamu di Sparrow, sehingga membantu melindungi kunci publik, alamat, label, dan riwayat transaksi dari akses yang tidak sah.

Aku menyarankan menyimpan kata sandi ini di pengelola kata sandi agar tidak lupa.

![LEDGER FLEX](assets/notext/54.webp)

Dan begitulah, dompet kamu sekarang telah dibuat!

![LEDGER FLEX](assets/notext/55.webp)
Sebelum menerima bitcoin pertama kamu di dompet, aku sangat menyarankan melakukan tes pemulihan kering. Catat informasi referensi, seperti xpub kamu, lalu reset **Ledger Flex** sementara dompet masih kosong. Setelah itu, coba pulihkan dompet kamu di **Ledger** menggunakan cadangan kertas kamu. Periksa bahwa xpub yang dihasilkan setelah pemulihan cocok dengan yang kamu catat sebelumnya. Jika sama, kamu bisa yakin bahwa cadangan kertas kamu dapat diandalkan.

## Bagaimana cara menerima bitcoin dengan Ledger Flex?

Klik pada tab "*Receive*".


![LEDGER FLEX](assets/notext/56.webp)

Hubungkan **Ledger Flex** kamu ke komputer, buka kunci dengan kode PIN kamu, lalu buka aplikasi "*Bitcoin*".

![LEDGER FLEX](assets/notext/57.webp)

Sebelum menggunakan alamat yang diberikan oleh **Sparrow Wallet**, verifikasi terlebih dahulu di layar **Ledger Flex** kamu. Praktik ini memastikan bahwa alamat yang ditampilkan di Sparrow bukan alamat palsu dan bahwa Ledger benar-benar memiliki kunci privat yang diperlukan untuk membelanjakan bitcoin yang diamankan dengan alamat tersebut nantinya.

Untuk melakukan verifikasi ini, klik tombol "*Display Address*".

![LEDGER FLEX](assets/notext/58.webp)

Pastikan alamat yang ditampilkan di **Ledger Flex** kamu cocok dengan yang ditunjukkan di **Sparrow Wallet**. Disarankan juga melakukan verifikasi ini tepat sebelum memberikan alamat kamu kepada pengirim, untuk memastikan alamat tersebut benar dan valid.

![LEDGER FLEX](assets/notext/59.webp)

Kamu bisa menambahkan "*Label*" untuk menggambarkan sumber bitcoin yang akan diamankan dengan alamat ini. Ini adalah praktik yang baik karena membantu kamu mengelola UTXO dengan lebih baik.

![LEDGER FLEX](assets/notext/60.webp)

Untuk informasi lebih lanjut tentang pelabelan, saya juga menyarankan kamu untuk melihat tutorial lain ini:

https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Kamu kemudian dapat menggunakan alamat ini untuk menerima bitcoin.

![LEDGER FLEX](assets/notext/61.webp)

## Bagaimana cara mengirim bitcoin dengan Ledger Flex?

Sekarang setelah kamu menerima sats pertama di dompet yang diamankan dengan **Flex**, kamu juga bisa membelanjakannya. Hubungkan **Ledger** kamu ke komputer, buka kunci, jalankan **Sparrow Wallet**, lalu masuk ke tab "*Send*" untuk membuat transaksi baru.

![LEDGER FLEX](assets/notext/62.webp)

Jika kamu ingin melakukan "*coin control*", yaitu memilih secara spesifik UTXO mana yang akan digunakan dalam transaksi, masuk ke tab "*UTXOs*". Pilih UTXO yang ingin kamu belanjakan, lalu klik "*Send Selected*". Kamu akan diarahkan ke layar yang sama di tab "*Send*", tetapi dengan UTXO kamu sudah dipilih untuk transaksi.

![LEDGER FLEX](assets/notext/63.webp)
Masukkan alamat tujuan. Kamu juga dapat memasukkan beberapa alamat dengan mengklik tombol "*+ Add*".

![LEDGER FLEX](assets/notext/64.webp)

Catat sebuah "*Label*" untuk mengingat tujuan pengeluaran ini.  
Pilih jumlah yang ingin kamu kirim ke alamat tersebut.

Sesuaikan tarif biaya transaksi sesuai kondisi pasar saat ini.

Pastikan semua pengaturan transaksi sudah benar, lalu klik "*Buat Transaksi*".

Jika semuanya sudah sesuai, klik "*Finalisasi Transaksi untuk Ditandatangani*".

Klik "*Tandatangan*".

Klik "*Tandatangan*" di sebelah **Ledger Flex** kamu.

Verifikasi detail transaksi di layar **Flex**, termasuk alamat penerima, jumlah yang dikirim, dan biaya transaksi.

Untuk menandatangani, tahan jari kamu pada tombol "*Tahan untuk menandatangani*".

Transaksi kamu sekarang sudah ditandatangani. Klik "*Siarkan Transaksi*" untuk menyiarkannya ke jaringan Bitcoin.

Kamu bisa menemukannya di tab "*Transaksi*" di **Sparrow Wallet**.

Selamat, sekarang kamu sudah menguasai penggunaan dasar **Ledger Flex** dengan **Sparrow Wallet**! Dalam tutorial berikutnya, kita akan melihat cara menggunakan Ledger Flex dengan Liana untuk memanfaatkan Miniscript.

Kalau kamu merasa tutorial ini bermanfaat, aku akan sangat menghargai jempol ke atas di bawah ini. Jangan ragu untuk membagikan artikel ini di media sosial kamu. Terima kasih banyak!
