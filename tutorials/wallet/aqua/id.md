---
name: Aqua
description: Bitcoin, Lightning, dan Liquid dalam satu dompet
---
![cover](assets/cover.webp)

Aqua adalah aplikasi mobile yang memudahkan pembuatan hot wallet untuk Bitcoin dan Liquid, serta menawarkan opsi penggunaan Lightning tanpa repot mengelola node, berkat fitur swap terintegrasi. Aplikasi ini juga memungkinkan pengelolaan stablecoin USDT di berbagai jaringan.

Dikembangkan oleh perusahaan JAN3 di bawah arahan Samson Mow, Aqua awalnya dirancang khusus untuk kebutuhan pengguna di Amerika Latin, meskipun tetap cocok digunakan oleh siapa pun di seluruh dunia. Aplikasi ini sangat menarik bagi pemula maupun pengguna yang memanfaatkan Bitcoin untuk pembayaran sehari-hari.

Di tutorial ini, kita akan belajar cara memakai berbagai fitur Aqua. Tapi sebelum itu, kita luangkan waktu sebentar untuk memahami apa itu sidechain di Bitcoin dan bagaimana cara kerja Liquid, supaya kita bisa melihat nilai Aqua secara utuh.

![AQUA](assets/fr/01.webp)

## Apa itu sidechain?

Protokol Bitcoin punya batasan teknis yang sengaja dibuat untuk menjaga desentralisasi jaringan dan memastikan keamanan tersebar di antara semua pengguna. Namun, batasan ini kadang bikin pengguna frustrasi, terutama saat terjadi kemacetan karena volume transaksi yang tinggi secara bersamaan. Perdebatan soal skalabilitas Bitcoin sudah lama memecah belah komunitas, terutama selama Perang Blocksize. Sejak itu, komunitas Bitcoin secara luas mengakui bahwa skalabilitas sebaiknya dicapai lewat solusi off-chain di sistem lapisan kedua. Solusi ini termasuk sidechain, yang masih relatif kurang dikenal dan jarang digunakan dibandingkan sistem lain seperti Lightning Network.

Sidechain adalah blockchain independen yang berjalan paralel dengan blockchain utama Bitcoin. Blockchain ini menggunakan bitcoin sebagai unit akun melalui mekanisme yang disebut two-way peg. Mekanisme ini memungkinkan bitcoin di blockchain utama dikunci, lalu nilainya direplikasi di sidechain dalam bentuk token yang didukung oleh bitcoin asli. Token-token ini biasanya bernilai sama dengan bitcoin yang terkunci di rantai utama, dan prosesnya bisa dibalik untuk memulihkan dana kembali ke jaringan Bitcoin.

Tujuan sidechain adalah menawarkan fitur tambahan atau peningkatan teknis, seperti transaksi lebih cepat, biaya lebih rendah, atau dukungan untuk smart contract. Inovasi semacam ini tidak selalu bisa langsung diterapkan di blockchain Bitcoin tanpa mengorbankan desentralisasi atau keamanannya. Karena itu, sidechain memberi ruang untuk menguji dan mengeksplorasi solusi baru sambil tetap menjaga integritas Bitcoin. Namun, protokol ini sering kali memerlukan kompromi, terutama soal desentralisasi dan keamanan, tergantung pada model tata kelola serta mekanisme konsensus yang digunakan.

## Apa itu Liquid?

Liquid adalah sidechain federasi untuk Bitcoin yang dikembangkan oleh Blockstream guna meningkatkan kecepatan, privasi, dan fungsionalitas transaksi. Sidechain ini menggunakan mekanisme two-way peg berbasis federasi untuk mengunci bitcoin di rantai utama, lalu membuat Liquid-bitcoin (L-BTC) sebagai gantinya, yaitu token yang beredar di Liquid tetapi tetap didukung oleh bitcoin asli.

![AQUA](assets/fr/02.webp)

Jaringan Liquid bergantung pada federasi peserta yang terdiri dari entitas terkemuka di ekosistem Bitcoin, yang bertugas memvalidasi blok dan mengelola two-way peg. Selain L-BTC, Liquid juga memungkinkan penerbitan aset digital lain, seperti stablecoin USDT dan berbagai mata uang kripto lainnya.

![AQUA](assets/fr/03.webp)

## Instal aplikasi Aqua

Langkah pertama tentu saja adalah mengunduh aplikasi Aqua. Buka toko aplikasi kamu:

- [Untuk Android](https://play.google.com/store/apps/details?id=io.aquawallet.android);
- [Untuk Apple](https://apps.apple.com/us/app/aqua-wallet/id6468594241).
![AQUA](assets/fr/04.webp)

Untuk pengguna Android, kamu juga punya opsi untuk menginstal aplikasi lewat file .apk` [tersedia di GitHub mereka] (https://github.com/AquaWallet/aqua-wallet/releases).

![AQUA](assets/fr/05.webp)

Buka aplikasi, lalu centang kotak "*Saya telah membaca dan menyetujui Ketentuan Layanan & Kebijakan Privasi*".

![AQUA](assets/fr/06.webp)

## Buat portofoliomu di Aqua

Klik tombol "*Buat Dompet*".

![AQUA](assets/fr/07.webp)

Dan voila, portofolio mu sudah jadi!

![AQUA](assets/fr/08.webp)

Namun, pertama-tama, karena ini adalah dompet penyimpanan mandiri, maka sangat penting bagi kamu untuk membuat cadangan fisik mnemonic. **Mnemonik ini memberikanmu akses penuh dan tidak terbatas ke semua bitcoin milikmu**. Siapapun yang memiliki mnemonik ini dapat mencuri uangmu, bahkan tanpa akses fisik ke ponsel.

Hal ini memungkinkan kamu memulihkan akses ke bitcoin jika ponsel hilang, dicuri, atau rusak. Karena itu, sangat penting untuk menyimpannya dengan hati-hati di media fisik (bukan digital) dan menaruhnya di tempat yang aman. Kamu bisa menuliskannya di selembar kertas, atau untuk keamanan ekstra—terutama jika ini adalah dompet dengan jumlah besar—sebaiknya ukir di media baja tahan karat agar terlindung dari risiko kebakaran, banjir, atau kerusakan. Untuk hot wallet yang hanya menyimpan sedikit bitcoin, cadangan kertas sederhana biasanya sudah cukup.

Untuk melakukan ini, klik pada menu Pengaturan.

![AQUA](assets/fr/09.webp)

Kemudian klik "*Lihat Frasa Benih*". Buatlah cadangan fisik dari frasa 12 kata ini.

![AQUA](assets/fr/10.webp)

Dalam menu pengaturan yang sama, Anda juga dapat mengubah bahasa aplikasi dan mata uang fiat yang digunakan.

![AQUA](assets/fr/11.webp)

Sebelum kamu menerima bitcoin pertama di dompet, **aku sangat menyarankan untuk melakukan tes pemulihan kosong.** Catat dulu beberapa informasi referensi, seperti xpub atau alamat penerima pertama, lalu hapus dompet di aplikasi Aqua saat masih kosong. Setelah itu, coba pulihkan dompet di Aqua menggunakan cadangan kertas yang kamu punya. Periksa apakah informasi yang muncul setelah pemulihan sesuai dengan yang sudah kamu catat sebelumnya. Kalau cocok, berarti cadangan kertas kamu bisa diandalkan. Untuk tahu lebih lanjut cara melakukan uji coba pemulihan, silakan baca tutorial lainnya:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Ini tidak muncul di layar saya karena saya memakai emulator, tapi di pengaturan ada opsi untuk mengunci aplikasi dengan autentikasi biometrik. Aku sangat merekomendasikan mengaktifkan fitur keamanan ini, karena tanpa itu, siapa pun yang memegang ponsel kamu saat tidak terkunci bisa mencuri bitcoin. Di iOS kamu bisa pakai Face ID, sedangkan di Android bisa pakai sidik jari. Kalau metode ini gagal saat autentikasi, kamu tetap bisa mengakses aplikasi lewat kode PIN ponsel.

## Terima bitcoin di Aqua

Sekarang dompetmu sudah siap, kamu siap untuk menerima satwa pertamamu! Cukup klik tombol "*Terima*" di menu "*Dompet*".

![AQUA](assets/fr/12.webp)

Kamu bisa memilih untuk menerima bitcoin di blockchain, di Liquid, atau melalui Lightning.

![AQUA](assets/fr/13.webp)

Untuk transaksi on-chain, Aqua akan membuat alamat penerima khusus yang bisa kamu gunakan untuk menerima satoshi kamu.

![AQUA](assets/fr/14.webp)

Demikian juga, jika kamu memilih Liquid, Aqua akan memberikan alamat Liquid untukmu.

![AQUA](assets/fr/15.webp)

Kalau kamu ingin menerima dana lewat Lightning, kamu harus terlebih dulu menentukan jumlah yang diinginkan.

![AQUA](assets/fr/16.webp)

Kemudian klik "*Generate Invoice*".

![AQUA](assets/fr/17.webp)

Aqua akan membuat invoice untuk menerima dana dari dompet Lightning. Perlu diperhatikan, berbeda dengan opsi on-chain dan Liquid, dana yang diterima lewat Lightning akan otomatis dikonversi menjadi L-BTC di Liquid menggunakan alat Boltz, karena Aqua bukan node Lightning. Proses ini memungkinkan kamu menerima dan mengirim dana lewat Lightning tanpa harus menyimpan bitcoin di jaringan Lightning.

![AQUA](assets/fr/18.webp)

Secara pribadi, aku akan memulai dengan mengirim bitcoin lewat Lightning ke Aqua. Setelah transaksi selesai menggunakan invoice yang disediakan, kita akan menerima konfirmasi.

![AQUA](assets/fr/19.webp)

Untuk memantau proses swap, kembali ke beranda dompet dan klik akun "L2 Bitcoin", yang menampilkan transaksi Lightning (melalui swap) dan Liquid.

![AQUA](assets/fr/20.webp)

Di sini kamu dapat melihat transaksi dan saldo L-BTC milikmu.

![AQUA](assets/fr/21.webp)

## Pertukaran Bitcoin dengan Aqua

Setelah kamu punya aset di dompet Aqua, kamu bisa menukarnya langsung dari aplikasi, baik untuk memindahkannya ke blockchain utama Bitcoin maupun ke Liquid. Kamu juga bisa mengonversi bitcoin menjadi stablecoin USDT (atau aset lainnya). Untuk melakukannya, buka menu "*Marketplace*".

![AQUA](assets/fr/22.webp)

Klik "*Swaps*".

![AQUA](assets/fr/23.webp)

Di kotak "*Transfer dari*", Pilih aset yang ingin kamu tukarkan. Saat ini aku hanya punya L-BTC, jadi itu yang aku pilih.

![AQUA](assets/fr/24.webp)

Pada kotak "*Transfer ke*", Pilih aset target untuk swap. Aku sendiri memilih USDT di jaringan Liquid.

![AQUA](assets/fr/25.webp)

Masukkan jumlah yang ingin kamu konversi.

![AQUA](assets/fr/26.webp)

Konfirmasikan dengan mengeklik "*Lanjutkan*".

![AQUA](assets/fr/27.webp)

Pastikan kamu puas dengan pengaturan swap, kemudian konfirmasikan dengan menyeret tombol "*Swap*" di bagian bawah layar.

![AQUA](assets/fr/28.webp)

Penukaran kamu sekarang sudah dikonfirmasi.

![AQUA](assets/fr/29.webp)

Melihat kembali portofolio kami, kita dapat melihat bahwa kami sekarang memiliki USDT di Liquid.

![AQUA](assets/fr/30.webp)

## Kirim bitcoin dengan Aqua

Sekarang setelah kamu memiliki bitcoin di dompet Aqua milikmu, kamu bisa mengirimkannya. Klik tombol "*Kirim*".

![AQUA](assets/fr/31.webp)

Pilih aset yang ingin kamu kirim atau pilih jaringan untuk melakukan transaksi. Aku sendiri akan mengirim bitcoin melalui Lightning.

![AQUA](assets/fr/32.webp)

Selanjutnya, masukkan informasi yang dibutuhkan untuk mengirim pembayaran: untuk Bitcoin on-chain atau Liquid, masukkan alamat penerima; untuk Lightning, masukkan invoice. Kamu bisa menempelkan informasi ini langsung ke kolom yang tersedia, atau menggunakan ikon kode QR untuk membuka kamera dan memindai alamat atau invoice tersebut. Kemudian klik "*Lanjutkan*".

![AQUA](assets/fr/33.webp)

Klik "*Lanjutkan*" sekali lagi jika semua informasi sudah benar.

![AQUA](assets/fr/34.webp)

Aqua kemudian akan menampilkan ringkasan transaksi. Pastikan semua informasinya sudah benar, termasuk alamat tujuan, biaya, dan jumlah. Untuk mengonfirmasi transaksi, geser tombol "*Geser untuk mengirim*" di bagian bawah layar.

![AQUA](assets/fr/35.webp)

Kemudian, kamu akan menerima konfirmasi pengiriman.

![AQUA](assets/fr/36.webp)

Jadi, sekarang kamu sudah tahu cara menggunakan aplikasi Aqua untuk menerima dan membelanjakan dana di Bitcoin, Lightning, dan Liquid, semuanya dari satu antarmuka.

Jika Anda merasa tutorial ini bermanfaat, aku akan sangat berterima kasih jika kamu memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di media sosial. Terima kasih banyak!

Aku juga menyarankanmu untuk melihat tutorial komprehensif lainnya di aplikasi seluler Blockstream Green, yang merupakan solusi menarik lainnya untuk menyiapkan dompet Liquid milikmu:

https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

