---
name: Bisq Easy Mobile
description: Protokol perdagangan peer-to-peer untuk pengguna bitcoin baru - tanpa perantara, tanpa KYC.
---
![cover](assets/cover.webp)


## Pendahuluan


Protokol perdagangan [Bisq Easy] (https://bisq.network/bisq-easy/) dirancang untuk [Bisq 2] (https://github.com/bisq-network/bisq2), penerus dari [Bisq v1] (https://github.com/bisq-network/bisq). Bisq 2 akan mendukung beberapa protokol perdagangan, jaringan privasi, dan identitas. Ini memfasilitasi pembelian Bitcoin tanpa biaya perdagangan dan tidak ada persyaratan uang jaminan. Ini ditujukan untuk pembeli Bitcoin baru yang mencari opsi non-KYC yang ingin diintegrasikan secara efisien oleh penjual berpengalaman dan berpengetahuan luas yang terbiasa dengan platform Bisq.


Saat ini, Bisq Easy adalah satu-satunya protokol perdagangan untuk Bisq 2. Lebih banyak protokol perdagangan direncanakan untuk masa depan. Pelajari lebih lanjut tentang Bisq 2 di tutorial ini:


https://planb.academy/tutorials/exchange/peer-to-peer/bisq-v2-c1c6a702-6c16-4101-8b90-62c424017b80

Panduan singkat ini merupakan pelengkap dari tutorial di atas mengenai cara membeli Bitcoin dengan menggunakan aplikasi [Bisq Easy Mobile] (https://github.com/bisq-network/bisq-mobile) dan Lightning.


## 1️⃣ Memulai


Untuk memulai, unduh Bisq Easy Mobile dari [halaman unduh] (https://bisq.network/downloads/). Disarankan untuk memverifikasi unduhan. Petunjuk verifikasi juga tersedia di [halaman unduh](https://bisq.network/downloads/). Setelah instalasi, Anda harus menerima `Perjanjian Pengguna`. Selanjutnya, buatlah profil publik yang terdiri dari `nickname` dan avatar (diwakili oleh `bot icon`). Dengan Bisq Easy, Anda juga dapat membuat beberapa profil pengguna dalam satu klien. Setelah inisialisasi singkat, Anda akan masuk ke `Layar Utama`. Aplikasi ini menyoroti materi edukasi langsung di halaman utama. Ketuk `Panduan Perdagangan Terbuka` untuk membiasakan diri Anda dengan informasi terbaru.


![image](assets/en/01.webp)


Panduan Perdagangan menjelaskan segala sesuatu yang relevan dalam langkah-langkah mudah:



- Cara berdagang di Bisq Mudah
- Bagaimana cara kerja proses jual beli
- Apa yang perlu saya ketahui tentang peraturan perdagangan.


Bagian penting lainnya adalah **"Seberapa amankah berdagang di Bisq Easy? "**


![image](assets/en/08.webp)


Centang kotak berlabel `Saya telah membaca dan memahami` dan ketuk `Selesai`.


![image](assets/en/02.webp)


## 2️⃣ Cadangkan data Anda


Sebelum kita mulai, mari kita selesaikan beberapa tugas rumah tangga dan membuat `backup` file penyimpanan data Anda. Buka `Lainnya` > `Cadangan & Pulihkan` untuk menyimpan profil dan riwayat perdagangan Anda. Jika Anda kehilangan perangkat tanpa cadangan, reputasi dan transaksi yang sedang berlangsung tidak dapat dipulihkan. Berikan `Kata Sandi` untuk mengenkripsi cadangan Anda.


![image](assets/en/11.webp)


## 3️⃣ Penawaran


Dari `Layar awal`, ada dua cara untuk menavigasi ke penawaran. Ketuk `Jelajahi penawaran` di tengah layar atau ketuk `Penawaran` di menu bagian bawah. Dari sana, pilih `mata uang` yang ingin Anda perdagangkan.


![image](assets/en/03.webp)


Tidak seperti [Bisq 1] (https://planb.academy/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04), yang membutuhkan jaminan, Bisq Easy hanya mengandalkan reputasi penjual untuk keamanan. Meskipun pendekatan ini memungkinkan pembeli untuk membeli Bitcoin untuk pertama kalinya tanpa kepemilikan sebelumnya, pendekatan ini menempatkan tingkat kepercayaan yang tinggi pada kemampuan penjual untuk mengirimkan Bitcoin setelah menerima pembayaran fiat. Oleh karena itu, model keamanan Bisq Easy dioptimalkan hanya untuk jumlah perdagangan yang kecil dan perdagangan dibatasi hingga setara dengan $600 USD per transaksi untuk meminimalkan risiko. Pada bagian `Offerbook`, pilih filter untuk metode pembayaran dan penyelesaian dalam Lightning atau Bitcoin (on-chain).


![image](assets/en/04.webp)


Setelah menerapkan `filter`, pilih penawaran yang sesuai dari mitra jual beli terkemuka. Metode pembayaran dan jenis penyelesaian yang telah dipilih sebelumnya oleh penjual (`Lightning` atau `on-chain`) akan ditampilkan. Pastikan ini sesuai dengan preferensi Anda sebelum melanjutkan. Kami memilih opsi Lightning ⚡ di sini.


![image](assets/en/05.webp)


Tinjau dan konfirmasikan detail jual beli dengan mengetuk `Konfirmasi terima penawaran`. Kemudian layar Popup akan muncul untuk mengonfirmasi bahwa Anda telah berhasil menerima penawaran. Ketuk Tampilkan jual beli di `Buka Jual Beli`. Di bagian Buka Jual Beli, tempelkan `Faktur Kilat` dan ketuk `Kirim ke penjual` untuk membagikannya. Sekarang tunggu data akun pembayaran penjual. Penjual mungkin membutuhkan waktu untuk merespons. Periksa kembali secara berkala untuk mengetahui pembaruan di jendela obrolan.


![image](assets/en/06.webp)


Kirimkan salam singkat dalam obrolan. Penjual akan membagikan detail pembayaran saat mereka online


![image](assets/en/09.webp)


Setelah Anda menerima rincian pembayaran yang diperlukan dari penjual, lanjutkan dengan menyelesaikan pembayaran. Setelah itu, tekan tombol `Konfirmasi Anda telah melakukan pembayaran`, lalu tunggu dengan sabar konfirmasi pembayaran Anda. ️ ⌛️


Terakhir, ketika penjual mengonfirmasi tanda terima pembayaran, Anda juga harus mengonfirmasi tanda terima Bitcoin. Ini menyelesaikan pembelian dengan menggunakan Bisq dalam Mode Mudah. Selamat! Sekarang Anda bisa menekan tombol `tutup jual beli`.


![image](assets/en/10.webp)


## 4️⃣ Penyelesaian Sengketa pada Bisq Mudah


Jika terjadi kesalahan dalam jual beli Anda, pembeli dan penjual dapat meminta bantuan mediasi.


**Apa yang dapat dilakukan oleh mediator:**

- Membantu memfasilitasi penyelesaian perdagangan yang sukses

- Verifikasi pembayaran fiat, altcoin, dan Bitcoin

- Membatalkan perdagangan bila perlu

- Laporkan pelanggaran peraturan yang serius kepada moderator untuk kemungkinan pelarangan pengguna


**Konsekuensi untuk Penjual yang Curang:**

Tergantung pada jenis reputasi mereka:



- Reputasi Obligasi BSQ**: DAO dapat menyita BSQ terikat mereka
- Reputasi Address Bawang Merah**: Alamat bawang Bisq 1 mereka mungkin diblokir


**Catatan Penting:** Karena semua reputasi terkait dengan profil pengguna Anda, larangan akan menonaktifkan reputasi Anda sepenuhnya.


## 5️⃣ Buat penawaran Anda sendiri


Alih-alih mengambil penawaran yang sudah ada, Anda bisa membuat penawaran beli sendiri dan membiarkan penjual yang mendatangi Anda. Ini adalah opsi yang tepat jika Anda tidak menemukan penawaran dengan premi atau metode pembayaran yang tepat di pasar yang ingin Anda perdagangkan, meskipun Anda harus menunggu sampai ada penjual yang menerimanya.


Dari layar `Penawaran`, ketuk ikon `+` berwarna hijau di pojok kanan bawah. Kemudian pilih `Beli Bitcoin` dan pilih mata uang fiat Anda.


Tetapkan parameter perdagangan Anda:



- Jumlah tetap atau Jumlah kisaran**: Pilih jumlah yang ingin Anda belanjakan.
- Metode pembayaran**: Pilih dari opsi yang tersedia
- Penyelesaian**: Pilih Lightning ⚡ atau ₿ on-chain


Tinjau detail Anda dan ketuk `Buat penawaran`. Penawaran Anda sekarang muncul di `Buku Penawaran`.


![image](assets/en/07.webp)


*Catatan: Sebagai pembeli di Bisq Easy, Anda tidak memerlukan reputasi-ini adalah keuntungan utama. Penjual menanggung persyaratan dan risiko reputasi, itulah sebabnya mereka mengenakan premi. Penawaran Anda hanya perlu diberi harga yang cukup menarik untuk dipertimbangkan oleh penjual bereputasi baik.*


Setelah diterbitkan, tunggu di bagian `Penawaran`. Ketika penjual menerima penawaran Anda, Anda akan menerima pemberitahuan. Buka jual beli di `Jual Beli Terbuka`, di mana penjual dan Anda dapat bertukar detail pembayaran. Kirim alamat Bitcoin atau faktur Lightning Anda ke penjual. Setelah mengirim fiat, konfirmasi pembayaran. Setelah penjual mengonfirmasi penerimaan, mereka akan melepaskan Bitcoin untuk menyelesaikan jual beli.


## 🎯 Kesimpulan


Bisq Easy memungkinkan pembelian Bitcoin tanpa agunan, memecahkan masalah klasik ayam dan telur bagi pembeli baru. Imbalannya jelas: Anda mengandalkan reputasi penjual, bukan dana yang dikunci untuk keamanan. Pendekatan berbasis kepercayaan ini menjelaskan premi 5-15% yang biasa dikenakan, yang memberi kompensasi kepada penjual yang memiliki reputasi baik atas investasi mereka dalam membangun kepercayaan dan memberikan dukungan. Meskipun sistem membatasi perdagangan dalam jumlah kecil untuk menahan potensi kerugian, selalu pilih penjual dengan nilai reputasi yang baik. Untuk pendatang baru yang bersedia menerima persyaratan ini, Bisq Easy menawarkan titik masuk yang mudah ke Bitcoin.


## 📚 Bisq Sumber Daya Seluler yang Mudah


[Github](https://github.com/bisq-network/bisq-mobile) | [Situs web](https://bisq.network/bisq-easy/) | [Wiki](https://bisq.wiki/Bisq_Easy)