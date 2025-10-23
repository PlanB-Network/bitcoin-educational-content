---
name: Trezor Model One
description: Menyiapkan dan menggunakan Hardware Wallet Model One
---
![cover](assets/cover.webp)

*Kredit gambar: [Trezor.io](https://trezor.io/)*

Trezor Model One adalah hardware wallet pertama yang pernah dirilis, diluncurkan pada tahun 2014 oleh SatoshiLabs. Setelah lebih dari sepuluh tahun, dompet ini tetap jadi pilihan menarik, terutama buat kamu yang mencari hardware wallet yang mudah diakses, baik dari sisi teknis maupun anggaran. Bahkan, harganya cuma €49 di situs resmi Trezor. Ini satu-satunya dompet perangkat keras di kisaran harga tersebut. Posisinya berada di tengah antara perangkat entry-level seharga sekitar €20 seperti Tapsigner, yang sering kali tidak punya layar, dan perangkat kelas menengah seharga sekitar €80 seperti Ledger Nano S Plus atau Trezor Safe 3.

Model One punya layar OLED monokrom berukuran 0,96 inci dan dua tombol fisik. Perangkat ini tidak memiliki baterai dan hanya berfungsi saat terhubung melalui kabel micro-USB untuk daya dan pertukaran data.

![Image](assets/fr/01.webp)

Kelemahan utama Model One adalah tidak adanya Secure Element, yang membuatnya rentan terhadap berbagai serangan fisik, beberapa di antaranya cukup mudah dilakukan. Serangan ini bisa mencakup analisis saluran samping untuk menebak PIN perangkat, atau teknik yang lebih canggih untuk mengekstrak seed terenkripsi agar bisa di-brute-force nanti. Perlu diingat, serangan seperti ini memerlukan akses fisik ke perangkat. Meski begitu, risiko tersebut bisa dikurangi secara signifikan dengan menggunakan passphrase BIP39 yang kuat. Kalau kamu memilih hardware wallet ini, aku sangat menyarankan untuk mengonfigurasikan passphrase.


Model One menawarkan dua keuntungan penting:

- Model One dibangun dengan arsitektur yang sepenuhnya open source. Berbeda dengan model yang lebih baru yang menggunakan Secure Element, semua komponen perangkat keras dan perangkat lunak pada Model One bisa diaudit sepenuhnya;
- Perangkat ini dilengkapi dengan layar. Sejauh yang aku tahu, ini adalah satu-satunya hardware wallet di pasaran dalam kisaran harga ini yang sudah punya layar. Fitur ini sangat penting karena memungkinkan kamu memverifikasi informasi yang ditandatangani dan alamat penerima, sehingga bisa mencegah banyak jenis serangan digital.

Karena itu, Trezor Model One bisa jadi pilihan yang bijak untuk pengguna pemula maupun menengah dengan anggaran terbatas. Meski begitu, penting untuk tetap sadar akan keterbatasannya dalam hal perlindungan fisik karena tidak memiliki Secure Element. Kalau anggaranmu terbatas, ini tetap pilihan yang bagus. Tapi kalau kamu bisa menambah sedikit untuk model yang lebih unggul seperti Trezor Safe 3 seharga €79, itu akan lebih baik karena sudah dilengkapi dengan Secure Element.

## Membuka Kotak Trezor Model One

Saat kamu menerima Model One, pastikan kotak dan segelnya masih utuh untuk memastikan paket tersebut belum pernah dibuka. Nantinya, keaslian dan integritas perangkat juga akan diverifikasi secara perangkat lunak saat kamu melakukan pengaturan awal.

Isi kotak termasuk:

- Trezor Model One;
- Stok kartu untuk mencatat frasa, stiker, dan instruksi Mnemonic kamu;
- Kabel USB-A ke micro-USB.

![Image](assets/fr/02.webp)



Menavigasi perangkat ini sangat sederhana:

- Klik kanan untuk mengonfirmasi dan melanjutkan ke langkah berikutnya;
- Gunakan tombol kiri untuk kembali.



## Prasyarat

Untuk tutorial ini, aku akan menunjukkan kepada kamu bagaimana cara menggunakan Trezor Model One dengan [perangkat lunak manajemen portofolio Sparrow Wallet] (https://sparrowwallet.com/download/). Jika kamu belum menginstal perangkat lunak ini, silakan lakukan sekarang. Kalau kamu memerlukan bantuan, kami juga memiliki tutorial terperinci tentang konfigurasi Sparrow Wallet:

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Kamu juga memerlukan perangkat lunak Trezor Suite untuk mengonfigurasi Model One, memeriksa keasliannya, dan menginstal firmware. Kita hanya akan menggunakan perangkat lunak ini untuk hal-hal tersebut, dan setelah itu, Trezor Suite hanya diperlukan saat memperbarui firmware. Untuk pengelolaan wallet sehari-hari, kita akan menggunakan Sparrow Wallet secara eksklusif, karena wallet ini dioptimalkan untuk Bitcoin dan mudah digunakan, bahkan oleh pemula (Sparrow hanya mendukung Bitcoin, bukan altcoin).

[Unduh Trezor Suite dari situs web resmi](https://trezor.io/trezor-suite)

![Image](assets/fr/03.webp)

Untuk kedua program ini, aku sangat menyarankan kamu untuk memeriksa keasliannya (dengan GnuPG) dan integritasnya (melalui hash) sebelum menginstalnya di komputer kamu. Kalau kamu belum tahu cara melakukannya, kamu bisa mengikuti tutorial lain berikut ini:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Memulai Trezor Model One

Hubungkan Model One milikmu ke komputer yang sudah terinstal Trezor Suite dan Sparrow Wallet.

![Image](assets/fr/04.webp)

Buka Trezor Suite, lalu klik "*Setup my Trezor*".

![Image](assets/fr/05.webp)

Pilih "*Firmware khusus Bitcoin*", lalu klik "*Instal Bitcoin saja*".

![Image](assets/fr/06.webp)

Trezor Suite kemudian akan menginstal firmware pada Model One. Harap tunggu selama proses instalasi.

![Image](assets/fr/07.webp)

Klik "*Lanjutkan*".

![Image](assets/fr/08.webp)

## Menciptakan portofolio Bitcoin

Pada Trezor Suite, klik tombol "*Buat Wallet baru*".

![Image](assets/fr/09.webp)

Menerima persyaratan penggunaan pada Hardware Wallet.

![Image](assets/fr/10.webp)

Di Trezor Suite, klik "*Lanjutkan pencadangan*".

![Image](assets/fr/11.webp)

Perangkat lunak ini memberikan petunjuk tentang cara mengelola frasa Mnemonic milikmu.

Seedphrase ini memberi kamu akses penuh dan tak terbatas ke semua bitcoin milikmu. Siapa pun yang memiliki seedphrase ini bisa mencuri dana kamu, bahkan tanpa perlu akses fisik ke Trezor Model One.

Frasa 24 kata ini memungkinkan kamu memulihkan akses ke bitcoin jika hardware wallet kamu hilang, dicuri, atau rusak. Karena itu, sangat penting untuk menyimpannya dengan hati-hati dan menaruhnya di tempat yang aman.

Kamu bisa menuliskannya di kartu yang disertakan dalam kotak, atau untuk keamanan ekstra, aku sarankan mengukirnya pada pelat baja tahan karat supaya tetap aman dari risiko kebakaran, banjir, atau jatuh.

Konfirmasikan instruksi, lalu klik tombol "*Buat cadangan Wallet*".

![Image](assets/fr/12.webp)

Model One akan membuat seedphrase kamu menggunakan generator angka acak. Pastikan kamu tidak diawasi selama proses ini. Tuliskan kata-kata yang muncul di layar pada media fisik pilihanmu. Tergantung strategi keamananmu, kamu bisa mempertimbangkan membuat beberapa salinan fisik lengkap dari seedphrase itu, tetapi yang terpenting, jangan membagikannya. Sangat penting untuk memberi nomor dan menyusunnya secara berurutan.

**Tentu saja, kamu tidak boleh membagikan kata-kata ini di internet, seperti yang aku lakukan dalam tutorial ini. Contoh wallet ini hanya akan digunakan pada Testnet dan akan dihapus pada akhir tutorial.**

Untuk informasi lebih lanjut tentang cara yang tepat menyimpan dan mengelola seedphrase kamu, aku sangat menyarankan mengikuti tutorial lain, terutama kalau kamu masih pemula:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Untuk informasi lebih lanjut tentang cara yang tepat menyimpan dan mengelola seedphrase kamu, aku sangat menyarankan mengikuti tutorial lain, terutama kalau kamu masih pemula:

![Image](assets/fr/13.webp)

Hardware wallet kamu sekali lagi akan menampilkan semua kata-katanya. Pastikan kamu sudah menuliskan semuanya.

![Image](assets/fr/14.webp)

## Mengatur kode PIN

Selanjutnya adalah langkah pembuatan PIN. PIN akan membuka kunci Trezor kamu, sehingga memberikan perlindungan terhadap akses fisik yang tidak sah. PIN ini tidak terlibat dalam penurunan kunci kriptografi wallet kamu. Artinya, meskipun orang lain tidak tahu PIN, siapa pun yang memiliki seedphrase 12 kata kamu tetap bisa memulihkan akses ke bitcoin-mu.

Pada Trezor Suite, klik "*Lanjutkan ke PIN*", lalu pada tombol "*Setel PIN*".

![Image](assets/fr/15.webp)

Konfirmasikan pada Model One.

![Image](assets/fr/16.webp)

Kami menyarankan untuk memilih PIN yang seacak mungkin. Pastikan menyimpan PIN ini di tempat yang terpisah dari lokasi penyimpanan Trezor kamu, misalnya di pengelola kata sandi. Kamu bisa menentukan PIN sepanjang 8 hingga 50 digit. Aku sarankan memilih PIN sepanjang mungkin untuk meningkatkan keamanan.

PIN harus dimasukkan ke Trezor Suite di komputer kamu dengan mengklik titik-titik yang sesuai dengan angka-angka, mengikuti konfigurasi keyboard yang ditampilkan di Trezor Model One.

Metode memasukkan PIN khusus ini diperlukan setiap kali kamu membuka kunci Trezor Model One, baik lewat Trezor Suite maupun Sparrow Wallet.

![Image](assets/fr/17.webp)

Setelah selesai, klik tombol "*Masukkan PIN*".

![Image](assets/fr/18.webp)

Tuliskan kembali PIN kamu untuk mengonfirmasi.

![Image](assets/fr/19.webp)

Pada Trezor Suite, klik tombol "*Selesaikan pengaturan*".

![Image](assets/fr/20.webp)

Konfigurasi Model One milikmu sekarang sudah selesai. Jika mau, kamu dapat mengubah nama dan halaman beranda Hardware Wallet.

![Image](assets/fr/21.webp)

Kita tidak akan lagi membutuhkan Trezor Suite, kecuali saat ingin memperbarui firmware secara berkala atau menjalankan tes pemulihan. Sekarang kita akan menggunakan Sparrow untuk mengelola portofolio, karena perangkat ini memang sangat cocok untuk penggunaan Bitcoin saja.

## Menyiapkan portofolio pada Sparrow Wallet

Mulailah dengan mengunduh dan menginstal Sparrow Wallet [dari situs web resmi] (https://sparrowwallet.com/) di komputermu, kalau kamu belum melakukannya.

Setelah membuka Sparrow Wallet, pastikan perangkat lunak ini terhubung ke node Bitcoin, ditandai dengan tanda centang di sudut kanan bawah antarmuka. Kalau kamu mengalami masalah saat menghubungkan Sparrow, aku sarankan membaca kembali bagian awal tutorial ini:

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klik pada tab "*File*", kemudian pada "*New Wallet*".

![Image](assets/fr/22.webp)

Beri nama portofolio kamu, lalu klik "*Buat Wallet*".

![Image](assets/fr/23.webp)

Pada menu drop-down "*Jenis Skrip*", pilih jenis skrip yang akan digunakan untuk mengamankan Bitcoin kamu. Kamu merekomendasikan "*Taproot*", atau jika tidak, "*Native SegWit*".

![Image](assets/fr/24.webp)

Klik pada tombol "*Terhubung Hardware Wallet*". Model One kamu tentu saja harus terhubung ke komputer.

![Image](assets/fr/25.webp)

Klik pada tombol "*Pindai*". Model One kamu akan muncul.

Saat kamu menghubungkan Model One ke komputer dengan Sparrow Wallet terbuka, kamu akan diminta memasukkan passphrase BIP39 di Sparrow. Opsi lanjutan ini akan dibahas di tutorial berikutnya. Untuk sekarang, cukup pilih "Toggle passphrase Off" agar Trezor tidak meminta passphrase setiap kali kamu memulai.

https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)

Klik "*Import Keystore*".

![Image](assets/fr/27.webp)

Sekarang kamu dapat melihat detail Wallet kamu, termasuk kunci publik yang diperpanjang dari akun pertama kamu. Klik pada tombol "*Apply*" untuk menyelesaikan pembuatan Wallet.

![Image](assets/fr/28.webp)

Pilih kata sandi yang kuat untuk mengamankan akses ke Sparrow Wallet. Kata sandi ini memastikan data Sparrow Wallet kamu tetap aman, melindungi kunci publik, alamat, label, dan riwayat transaksi dari akses yang tidak sah.

Aku sarankan menyimpan kata sandi ini di pengelola kata sandi supaya kamu tidak lupa.

![Image](assets/fr/29.webp)

Dan sekarang, portofolio kamu sudah diimpor ke dalam Sparrow Wallet!

![Image](assets/fr/30.webp)

Sebelum menerima bitcoin pertama di wallet, aku sangat menyarankan untuk melakukan tes pemulihan kosong. Tuliskan beberapa informasi referensi, seperti xpub, kemudian setel ulang Trezor Model One saat wallet masih kosong. Setelah itu, cobalah memulihkan wallet menggunakan cadangan kertasmu. Periksa apakah xpub yang dihasilkan setelah pemulihan sesuai dengan yang kamu tulis sebelumnya. Jika sesuai, kamu bisa yakin bahwa cadangan kertasmu dapat diandalkan.

Untuk mempelajari lebih lanjut tentang cara melakukan tes pemulihan, aku sarankan membaca tutorial lain berikut ini:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Bagaimana cara menerima bitcoin dengan Trezor Model One?

Pada Sparrow, klik tab "*Receive*".

![Image](assets/fr/31.webp)

Sebelum menggunakan alamat yang diberikan Sparrow Wallet, periksa di layar Trezor kamu. Praktik ini memastikan alamat yang ditampilkan di Sparrow bukan palsu, dan bahwa hardware wallet memang menyimpan private key yang diperlukan untuk membelanjakan bitcoin yang terkait dengan alamat tersebut. Hal ini membantu kamu menghindari beberapa jenis serangan.

Untuk melakukan pemeriksaan ini, klik tombol "*Display Address*".

![Image](assets/fr/32.webp)

Periksa apakah alamat yang ditampilkan di Trezor kamu cocok dengan yang ada di Sparrow Wallet. Sebaiknya kamu juga melakukan pemeriksaan ini sebelum mengirimkan alamatmu ke pengirim, untuk memastikan keabsahannya. Kamu bisa menekan tombol kanan untuk mengonfirmasi.

![Image](assets/fr/33.webp)

Kamu juga bisa menambahkan Label untuk mendeskripsikan sumber Bitcoin yang akan diamankan dengan alamat ini. Ini adalah praktik yang baik karena memudahkan kamu mengelola UTXO dengan lebih efisien.

![Image](assets/fr/34.webp)

Kamu kemudian bisa menggunakan alamat ini untuk menerima bitcoin.

![Image](assets/fr/35.webp)

## Bagaimana cara mengirim bitcoin dengan Trezor Model One?

Sekarang setelah kamu menerima satoshi pertamamu di wallet yang diamankan Model One, kamu juga bisa membelanjakannya! Hubungkan Trezor ke komputer, buka Sparrow Wallet, lalu masuk ke tab *Kirim* untuk membuat transaksi baru.

![Image](assets/fr/36.webp)

Kalau kamu ingin melakukan *Coin Control*, yaitu memilih UTXO tertentu yang akan digunakan dalam transaksi, buka tab "*UTXOs*". Pilih UTXO yang ingin digunakan, lalu klik "*Kirim Terpilih*". Kamu akan diarahkan ke layar yang sama di tab "*Kirim*", tetapi dengan UTXO yang sudah dipilih untuk transaksi.

![Image](assets/fr/37.webp)

Masukkan alamat tujuan Address. Kamu juga dapat memasukkan beberapa alamat dengan mengeklik tombol "*+ Tambah*".

![Image](assets/fr/38.webp)

Tuliskan "*Label*" untuk mengingat tujuan pengeluaran ini.

![Image](assets/fr/39.webp)

Pilih jumlah yang akan dikirim ke Address ini.

![Image](assets/fr/40.webp)

Sesuaikan tarif biaya transaksi kamu sesuai dengan pasar saat ini. Sebagai contoh, kamu dapat menggunakan [Mempool.space] (https://Mempool.space/) untuk memilih tarif biaya yang sesuai.

Pastikan semua parameter transaksi kamu sudah benar, lalu klik "*Buat Transaksi*".

![Image](assets/fr/41.webp)

Jika semuanya sudah sesuai dengan keinginanmu, klik "*Finalisasi Transaksi untuk Penandatanganan*".

![Image](assets/fr/42.webp)

Klik "*Tanda Tangan*".

![Image](assets/fr/43.webp)

Klik "*Sign*" di samping Trezor Model One kamu.

![Image](assets/fr/44.webp)

Periksa parameter transaksi di layar hardware wallet kamu, termasuk alamat penerima, jumlah yang dikirim, dan biaya. Setelah transaksi diverifikasi di Trezor, tekan tombol kanan untuk menandatanganinya.

![Image](assets/fr/45.webp)

Transaksimu sekarang sudah ditandatangani. Periksa sekali lagi apakah semuanya benar, lalu klik "Broadcast Transaction" untuk menyiarkannya ke jaringan Bitcoin.

![Image](assets/fr/46.webp)

Kamu bisa menemukannya di tab "*Transactions*" pada Sparrow Wallet.

![Image](assets/fr/47.webp)

Selamat, sekarang kamu sudah menguasai penggunaan dasar Trezor Model One dengan Sparrow Wallet! Untuk melangkah lebih jauh, aku merekomendasikan tutorial komprehensif tentang penggunaan Trezor hardware wallet dengan passphrase BIP39 untuk meningkatkan keamananmu:

https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Kalau kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih kalau kamu memberi jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di media sosialmu. Terima kasih banyak!
