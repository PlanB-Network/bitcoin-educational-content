---
name: Aqua
description: Bitcoin, Lightning, dan Liquid dalam satu dompet
---
![cover](assets/cover.webp)

Aqua adalah aplikasi mobile yang memudahkan kamu untuk membuat hot wallet Bitcoin dan Liquid, serta memungkinkan penggunaan Lightning tanpa kerumitan mengelola node, berkat fitur swap yang terintegrasi. Aplikasi ini juga memungkinkan kamu mengelola stablecoin USDT di berbagai jaringan.

Dikembangkan oleh perusahaan JAN3 di bawah arahan Samson Mow, Aqua awalnya dirancang untuk memenuhi kebutuhan pengguna di Amerika Latin. Meski begitu, aplikasi ini tetap cocok digunakan oleh siapa pun di seluruh dunia. Aqua sangat menarik bagi pemula, serta bagi mereka yang menggunakan Bitcoin setiap hari untuk pembayaran.

Dalam tutorial ini, kita akan mempelajari cara menggunakan berbagai fitur di Aqua. Namun sebelum masuk ke sana, mari kita luangkan waktu sejenak untuk memahami apa itu sidechain pada Bitcoin dan bagaimana cara kerja Liquid, agar kamu bisa memahami nilai Aqua secara utuh.


![AQUA](assets/fr/01.webp)

## Apa itu sidechain?

Protokol Bitcoin memiliki batasan teknis yang disengaja untuk membantu menjaga desentralisasi jaringan dan memastikan keamanan yang terdistribusi di antara semua pengguna. Namun, keterbatasan ini terkadang bisa membuat kamu frustrasi, terutama saat terjadi kemacetan akibat tingginya volume transaksi yang diproses secara bersamaan. Perdebatan tentang skalabilitas Bitcoin sudah lama memecah belah komunitas, terutama selama Perang Blocksize. Sejak peristiwa tersebut, komunitas Bitcoin secara luas mengakui bahwa skalabilitas harus dicapai melalui solusi off-chain, yaitu pada sistem lapisan kedua. Solusi ini mencakup sidechain, yang hingga kini masih relatif kurang dikenal dan jarang digunakan dibandingkan sistem lain seperti Lightning Network.

Sidechain adalah blockchain independen yang beroperasi secara paralel dengan blockchain utama Bitcoin. Blockchain ini menggunakan bitcoin sebagai unit akun, berkat mekanisme yang disebut "*two-way peg*". Mekanisme ini memungkinkan kamu mengunci bitcoin di rantai utama untuk merepresentasikan nilainya di sidechain, tempat bitcoin tersebut beredar dalam bentuk token yang didukung oleh bitcoin asli. Token-token ini umumnya memiliki nilai yang setara dengan bitcoin yang dikunci di rantai utama, dan proses ini dapat dibalik untuk memulihkan dana kembali ke jaringan Bitcoin.

Tujuan sidechain adalah untuk menawarkan fungsi tambahan atau peningkatan teknis, seperti transaksi yang lebih cepat, biaya yang lebih rendah, atau dukungan smart contract. Inovasi-inovasi ini tidak selalu bisa diterapkan langsung pada blockchain Bitcoin tanpa mengorbankan desentralisasi atau keamanannya. Karena itu, sidechain memungkinkan pengujian dan eksplorasi solusi baru sambil tetap menjaga integritas Bitcoin. Meski begitu, protokol ini sering kali menuntut kompromi, terutama dalam hal desentralisasi dan keamanan, tergantung pada model tata kelola dan mekanisme konsensus yang digunakan.

## Apa itu Liquid?

Liquid adalah sidechain federasi untuk Bitcoin yang dikembangkan oleh Blockstream guna meningkatkan kecepatan, kerahasiaan, dan fungsionalitas transaksi. Liquid menggunakan mekanisme penahan bilateral berbasis federasi untuk mengunci bitcoin di rantai utama dan menerbitkan Liquid-bitcoin (L-BTC) sebagai gantinya, yaitu token yang beredar di jaringan Liquid sambil tetap didukung sepenuhnya oleh bitcoin asli.

![AQUA](assets/fr/02.webp)

Jaringan Liquid bergantung pada federasi peserta yang terdiri dari entitas-entitas tepercaya dari ekosistem Bitcoin, yang bertugas memvalidasi blok dan mengelola mekanisme *two-way peg*. Selain L-BTC, Liquid juga memungkinkan penerbitan berbagai aset digital lainnya, seperti stablecoin USDT dan aset kripto lainnya.

![AQUA](assets/fr/03.webp)

## Instal aplikasi Aqua

Langkah pertama, tentu saja, mengunduh aplikasi Aqua. Buka toko aplikasi kamu:

- [Untuk Android](https://play.google.com/store/apps/details?id=io.aquawallet.android);
- [Untuk Apple](https://apps.apple.com/us/app/aqua-wallet/id6468594241).
![AQUA](assets/fr/04.webp)

Untuk pengguna Android, kamu juga memiliki opsi untuk menginstal aplikasi melalui file `.apk` [tersedia di GitHub mereka](https://github.com/AquaWallet/aqua-wallet/releases).

![AQUA](assets/fr/05.webp)

Luncurkan aplikasi, lalu centang kotak "*Saya telah membaca dan menyetujui Ketentuan Layanan & Kebijakan Privasi*".

![AQUA](assets/fr/06.webp)

## Buat portofolio kamu di Aqua

Klik tombol "*Buat Dompet*".

![AQUA](assets/fr/07.webp)

Dan voila, portofolio kamu sudah tercipta!

![AQUA](assets/fr/08.webp)

Namun, karena ini adalah dompet penyimpanan mandiri, sangat penting bagi kamu untuk membuat cadangan fisik mnemonic kamu. **Mnemonic ini memberi kamu akses penuh dan tanpa batas ke semua bitcoin kamu**. Siapa pun yang memiliki mnemonic ini dapat mencuri dana kamu, bahkan tanpa akses fisik ke ponsel kamu.

Cadangan ini memungkinkan kamu memulihkan akses ke bitcoin jika ponsel kamu hilang, dicuri, atau rusak. Karena itu, mnemonic harus disimpan dengan sangat hati-hati di media fisik, bukan digital, dan diletakkan di lokasi yang aman. Kamu bisa menuliskannya di selembar kertas, atau untuk keamanan tambahan, terutama jika ini adalah dompet dengan jumlah bitcoin yang besar, aku menyarankan untuk mengukirnya pada media baja tahan karat agar terlindung dari risiko kebakaran, banjir, atau kerusakan fisik lainnya. Untuk hot wallet yang memang ditujukan menyimpan jumlah bitcoin kecil, cadangan kertas sederhana biasanya sudah cukup.


Untuk melakukan ini, klik pada menu Pengaturan.

![AQUA](assets/fr/09.webp)

Kemudian klik "*Lihat Frasa Benih*". Buatlah cadangan fisik dari frasa 12 kata ini.

![AQUA](assets/fr/10.webp)

Dalam menu pengaturan yang sama, kamu juga dapat mengubah bahasa aplikasi dan mata uang fiat yang digunakan.

![AQUA](assets/fr/11.webp)

Sebelum kamu menerima bitcoin pertama di dompet kamu, **aku sangat menyarankan kamu untuk melakukan tes pemulihan kosong**. Catat beberapa informasi referensi, seperti xpub atau alamat penerima pertama kamu, lalu hapus wallet kamu di aplikasi Aqua saat masih kosong. Setelah itu, coba pulihkan dompet kamu di Aqua menggunakan cadangan kertas yang sudah kamu buat. Periksa apakah informasi yang dihasilkan setelah pemulihan sesuai dengan yang kamu catat sebelumnya. Jika sesuai, kamu bisa yakin bahwa cadangan kertas kamu dapat diandalkan. Untuk mempelajari lebih lanjut cara melakukan uji pemulihan, silakan baca tutorial berikut:

https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Opsi ini mungkin tidak terlihat di layar karena aku menggunakan emulator, tetapi kamu juga akan menemukan pengaturan untuk mengunci aplikasi menggunakan sistem autentikasi biometrik. Aku sangat merekomendasikan kamu mengaktifkan fitur keamanan ini, karena tanpa perlindungan tersebut, siapa pun yang memiliki akses ke ponsel kamu yang tidak terkunci dapat mencuri bitcoin kamu. Kamu bisa menggunakan Face ID di iOS atau sidik jari di Android. Jika metode biometrik gagal saat autentikasi, kamu tetap dapat mengakses aplikasi menggunakan kode PIN ponsel kamu.

## Terima bitcoin di Aqua

Sekarang dompet kamu sudah siap, kamu siap untuk menerima sats pertama kamu. Cukup klik tombol "*Terima*" di menu "*Dompet*".

![AQUA](assets/fr/12.webp)

Kamu bisa memilih untuk menerima bitcoin langsung di blockchain, di Liquid, atau melalui Lightning.

![AQUA](assets/fr/13.webp)

Untuk transaksi onchain, Aqua akan menghasilkan alamat penerima khusus tempat kamu bisa menerima bitcoin kamu.

![AQUA](assets/fr/14.webp)

Demikian juga, dengan memilih Liquid, Aqua akan memberikan kamu alamat Liquid.

![AQUA](assets/fr/15.webp)

Jika kamu lebih memilih menerima dana melalui Lightning, kamu perlu terlebih dahulu menentukan jumlah yang ingin diterima.

![AQUA](assets/fr/16.webp)

Kemudian klik "*Generate Invoice*".

![AQUA](assets/fr/17.webp)

Aqua akan membuat faktur untuk menerima dana dari dompet Lightning. Perlu diperhatikan bahwa, berbeda dengan opsi onchain dan Liquid, dana yang diterima melalui Lightning akan secara otomatis dikonversi menjadi L-BTC di Liquid menggunakan layanan Boltz, karena Aqua bukan merupakan node Lightning. Proses ini memungkinkan kamu menerima dan mengirim dana melalui Lightning tanpa harus menyimpan bitcoin kamu di Lightning.

![AQUA](assets/fr/18.webp)

Secara pribadi, aku akan memulai dengan mengirim bitcoin ke Aqua melalui Lightning. Setelah transaksi selesai menggunakan faktur yang disediakan, kamu akan menerima konfirmasi.

![AQUA](assets/fr/19.webp)

Untuk mengikuti perkembangan swap, kembali ke halaman beranda dompet kamu lalu klik akun "*L2 Bitcoin*", yang menampilkan transaksi Lightning (melalui swap) dan Liquid.

![AQUA](assets/fr/20.webp)

Di sini kamu dapat melihat transaksi dan saldo L-BTC milikmu.

![AQUA](assets/fr/21.webp)

## Pertukaran Bitcoin dengan Aqua

Setelah kamu memiliki aset di dompet Aqua, kamu bisa menukarnya langsung dari aplikasi, baik untuk mentransfernya ke blockchain Bitcoin utama maupun ke Liquid. Kamu juga bisa mengonversi bitcoin kamu menjadi stablecoin USDT atau aset lainnya. Untuk melakukannya, buka menu "*Marketplace*".

![AQUA](assets/fr/22.webp)

Klik "*Swaps*".

![AQUA](assets/fr/23.webp)

Di kotak "*Transfer dari*", pilih aset yang ingin kamu perdagangkan. Saat ini, aku hanya memiliki L-BTC, jadi itulah yang kupilih.

![AQUA](assets/fr/24.webp)

Pada kotak "*Transfer ke*", pilih aset target untuk swap kamu. Aku sendiri memilih USDT di jaringan Liquid.

![AQUA](assets/fr/25.webp)

Masukkan jumlah yang ingin kamu konversi.

![AQUA](assets/fr/26.webp)

Konfirmasikan dengan mengeklik "*Lanjutkan*".

![AQUA](assets/fr/27.webp)

Pastikan kamu puas dengan pengaturan swap, kemudian konfirmasikan dengan menyeret tombol "*Swap*" di bagian bawah layar.

![AQUA](assets/fr/28.webp)

Penukaran kamu sekarang telah dikonfirmasi.

![AQUA](assets/fr/29.webp)

Melihat kembali portofolio kami, kita dapat melihat bahwa kami sekarang memiliki USDT di Liquid.

![AQUA](assets/fr/30.webp)

## Kirim bitcoin dengan Aqua

Sekarang setelah kamu memiliki bitcoin di dompet Aqua, kamu bisa mengirimkannya. Klik tombol "*Kirim*".

![AQUA](assets/fr/31.webp)

Pilih aset yang ingin kamu kirim atau pilih jaringan untuk melakukan transaksi. Aku sendiri akan mengirim bitcoin melalui Lightning.

![AQUA](assets/fr/32.webp)

Selanjutnya, masukkan informasi yang diperlukan untuk mengirim pembayaran. Untuk bitcoin onchain atau Liquid, kamu perlu memasukkan alamat penerima. Untuk Lightning, kamu perlu memasukkan faktur. Kamu bisa menempelkan informasi tersebut langsung ke kolom yang tersedia, atau menggunakan ikon kode QR untuk membuka kamera dan memindai alamat atau faktur. Setelah itu, klik "*Lanju*

![AQUA](assets/fr/33.webp)

Klik "*Lanjutkan*" sekali lagi jika semua informasi sudah benar.

![AQUA](assets/fr/34.webp)

Aqua kemudian akan menampilkan ringkasan transaksi untuk kamu. Pastikan semua informasi sudah benar, termasuk alamat tujuan, biaya, dan jumlah. Untuk mengonfirmasi transaksi, geser tombol "*Geser untuk mengirim*" di bagian bawah layar.

![AQUA](assets/fr/35.webp)

Kemudian kamu akan menerima konfirmasi pengiriman.

![AQUA](assets/fr/36.webp)

Sekarang kamu sudah tahu cara menggunakan aplikasi Aqua untuk menerima dan membelanjakan dana di Bitcoin, Lightning, dan Liquid, semuanya dari satu antarmuka.

Kalau kamu merasa tutorial ini bermanfaat, aku akan sangat berterima kasih jika kamu memberikan jempol hijau di bawah ini. Jangan ragu untuk membagikan artikel ini di jejaring sosial kamu. Terima kasih banyak.

Aku juga menyarankan kamu untuk melihat tutorial komprehensif lainnya tentang aplikasi seluler Blockstream Green, yang merupakan alternatif menarik untuk menyiapkan dompet Liquid kamu:

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

