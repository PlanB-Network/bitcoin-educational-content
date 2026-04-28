---
name: Peach
description: Panduan lengkap untuk menggunakan Peach dan memperdagangkan bitcoin di P2P
---

![cover](assets/cover.webp)





## Pendahuluan



Pertukaran peer-to-peer (P2P) yang bebas KYC sangat penting untuk menjaga kerahasiaan dan otonomi keuangan pengguna. Bursa ini memungkinkan transaksi langsung antar individu tanpa memerlukan verifikasi identitas, yang sangat penting bagi mereka yang menghargai privasi. Untuk pemahaman yang lebih mendalam mengenai konsep teori, lihat kursus BTC204:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### 1. Apa itu Peach?



Peach adalah platform pertukaran P2P yang memungkinkan pengguna untuk membeli dan menjual bitcoin tanpa KYC. Platform ini menawarkan antarmuka yang intuitif dan fitur keamanan yang canggih. Dibandingkan dengan solusi lain seperti Bisq, HodlHodl, dan Robosat, Peach menonjol karena kemudahan penggunaannya.


Sistem escrow multisignature (2-2) menjamin keamanan dana selama transaksi. Peach mendukung berbagai metode pembayaran, dan memiliki sistem reputasi untuk memandu para trader dalam bertindak. Seperti biasa dengan platform P2P, penting untuk menjaga reputasi yang baik untuk menjaga kredibilitas dengan trader lain.



### 2. Privasi dan data yang dikumpulkan



**Informasi apa yang dikumpulkan oleh Peach?



Peach berusaha untuk menyimpan data seminimal mungkin tentang penggunanya. Berikut ini adalah ikhtisar data yang disimpan di server kami:





- hash pengenal aplikasi unik Anda (AdID)
- Sebuah hash dari data pembayaran Anda
- Percakapan terenkripsi Anda
- Data transaksi untuk memastikan bahwa pengguna anonim tidak melebihi batas perdagangan (jenis metode pembayaran yang digunakan, jumlah pembelian dan penjualan)
- Address digunakan untuk mengirim dan menerima dari rekening escrow
- Data penggunaan (Firebase & Google Analytics), hanya dengan persetujuan Anda



Sebagai pengingat, hash adalah data yang tidak dapat dikenali, mirip dengan enkripsi. Data yang sama akan selalu menghasilkan hash yang sama, sehingga memungkinkan untuk mendeteksi duplikat tanpa mengetahui data aslinya.



*Untuk penjelasan yang lebih rinci tentang hashing, ikuti kursus ini:*



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

**Siapa saja yang dapat melihat detail pembayaran saya?





- Hanya rekanan Anda yang dapat melihat detail pembayaran Anda
- Data ditransmisikan melalui server Peach, tetapi sepenuhnya dienkripsi dari ujung ke ujung
- Jika terjadi perselisihan, detail pembayaran dan riwayat percakapan Anda akan terlihat oleh mediator Peach yang ditugaskan



## Instalasi dan konfigurasi



### 1. Instal aplikasi Peach



![Installation de Peach](assets/fr/01.webp)





- Unduh aplikasi dari [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/). Pada iOS, Anda harus terlebih dahulu menginstal aplikasi [testflight](https://apps.apple.com/us/app/testflight/id899247664).
- Ikuti petunjuk pemasangan pada perangkat Anda.
- Selama instalasi, Anda akan diminta untuk memilih apakah Anda ingin berbagi data tertentu untuk menyempurnakan aplikasi Peach. (gambar 1)
- Pada layar berikutnya (gambar 2), Anda memiliki dua opsi:
 - Jika Anda adalah pengguna baru, klik "Pengguna baru" untuk membuat profil baru
 - Jika Anda sudah memiliki akun, gunakan "Pulihkan" untuk memulihkan profil Anda yang sudah ada
- Jika Anda memiliki kode referral, Anda dapat memasukkannya di sini.
- Untuk memulihkan akun yang sudah ada (gambar 3), Anda memerlukan :
 - File cadangan Anda
 - Kata sandi untuk mendekripsi file ini



### 2. Gambaran Umum Layar Utama



Aplikasi Peach diatur di sekitar empat layar utama yang dapat diakses dari bilah navigasi bawah:



![Navigation dans l'application](assets/fr/02.webp)





- Beranda (4)** : Layar utama tempat Anda dapat memilih untuk membeli atau menjual, membuat transaksi baru, dan mengakses penawaran yang tersedia:
 - membuat penawaran dengan dua tombol di bawah ini (buat beli / buat jual)
 - manfaatkan penawaran yang sudah ada yang dibuat oleh pengguna lain, dengan menggunakan dua tombol di bawah ini ("Beli"/"Jual").





- Wallet (5)**: Bitcoin wallet terintegrasi Anda yang memungkinkan Anda untuk :
 - Periksa saldo Anda
 - Menerima bitcoin
 - Bitcoin Envoyer (dengan kontrol koin)
 - Melihat riwayat transaksi Anda
 - Membiayai penjualan Anda





- Perdagangan (6)**: kontrak Anda saat ini dan sebelumnya, di bawah tiga tab:
 - Pembelian dalam proses
 - Penjualan dalam proses
 - Riwayat bursa Anda





- Pengaturan (7)** : Pusat konfigurasi untuk
 - Melihat profil Anda (reputasi, lencana, batasan, dll.)
 - Mengelola keamanan (cadangan, pin)
 - Mengelola metode pembayaran Anda
 - Hubungi dukungan
 - Mengubah bahasa
 - dll.



### 3. Mengonfigurasi metode pembayaran Anda



![Accès aux paramètres de paiement](assets/fr/03.webp)



Anda dapat mengelola metode pembayaran dalam pengaturan (gambar 8)



Peach menawarkan pembayaran online, dan pembayaran tatap muka (hanya pada pertemuan yang terdaftar).



**Pembayaran online



**Penting:**


untuk melindungi pengguna, Peach mengharuskan sumber dana sesuai dengan yang diiklankan. Terserah kepada para pedagang untuk memastikan bahwa ini adalah kasusnya, untuk perlindungan mereka sendiri.



![Configuration des paiements en ligne](assets/fr/04.webp)



Untuk menambahkan metode :




- Pada tab "online", klik "tambahkan mata uang/metode"
- Pilih mata uang Anda
- Pilih metode pembayaran pilihan Anda



*Jenis metode pembayaran yang tersedia:*



*** Untuk transfer bank: ***




- SEPA (standar atau instan)
- Isi detail bank SEPA Anda.



***Daring wallet diterima :***




- Beberapa opsi tersedia tergantung pada negara Anda (Revolut, Paypal, Wise, Strike, dll.)
- Ikuti petunjuk untuk menambahkan detail login Anda



*kartu hadiah dapat digunakan:*** Kartu hadiah dapat digunakan:*** Kartu hadiah dapat digunakan:*** Kartu hadiah dapat digunakan:*** Kartu hadiah dapat digunakan:*** Kartu hadiah dapat digunakan:***




- Amazon, Steam, dll.
- Masukkan negara penerbit kartu dan informasi lain yang diperlukan



***Opsi pembayaran nasional:***


Sistem pembayaran khusus negara :




- Satispay (Italia)
- MB Way (Portugal)
- Bizum (Spanyol)
- Pembayaran Lebih Cepat (Inggris)
- dll.



*** Untuk pembayaran tatap muka: ***



![Configuration des paiements en personne](assets/fr/05.webp)





- Pilih "Pertemuan" (gambar 12)
- Kemudian pilih pertemuan Anda dari daftar (gambar 13)



### Petunjuk penggunaan





- Anda dapat menambahkan beberapa metode pembayaran
- Semakin banyak metode yang Anda tambahkan, semakin luas jangkauan penawaran yang dapat Anda akses
- Periksa keakuratan informasi Anda sebelum mendaftar
- Anda dapat mengubah atau menghapus metode pembayaran Anda kapan saja



**Catatan keamanan**: Informasi pembayaran Anda dienkripsi dan hanya dibagikan dengan mitra bursa Anda selama transaksi, kecuali jika terjadi perselisihan di mana mediator Peach juga akan memiliki akses.



### 4. Cara mengamankan portofolio Anda



**Memahami akun Peach Anda



Akun Peach tidak memiliki nama pengguna dan kata sandi. Ini adalah sebuah file yang disimpan secara lokal di ponsel Anda, yang berarti Peach tidak perlu menyimpan data Anda atau mengetahui identitas Anda: Anda yang memegang kendali. File ini berisi semua data Anda: termasuk 12 kata pemulihan bitcoin, kunci PGP, detail pembayaran, dan sebagainya. Jadi, sangat penting untuk menyimpan file ini dan melindunginya dengan kata sandi yang kuat.



Pendekatan ini menjamin tingkat kerahasiaan, dan menyerahkan tanggung jawab pengelolaan data dan cadangan di tangan pengguna. Kehilangan ponsel Anda tanpa cadangan berarti kehilangan akses ke akun dan dana Peach Anda.



**Buat cadangan Anda**






- Mengakses pengaturan dari tab di kanan bawah layar beranda
- Pilih opsi "cadangan" di menu pengaturan



![Processus de sauvegarde](assets/fr/06.webp)



Tersedia dua jenis cadangan yang tersedia:



**Simpan file akun (gambar 14)**




- Klik "Buat cadangan baru"
- Buat kata sandi **kuat** untuk mengenkripsi file cadangan Anda
- Kirim file ini ke lokasi yang akan memastikan redundansinya jika ponsel hilang.



Cadangan file memulihkan akun Peach Anda yang lengkap, termasuk file :




- Portofolio Anda
- Metode pembayaran Anda
- Data pembayaran
- Riwayat transaksi dengan detail rekanan dan percakapan dengan mereka



**Menyimpan frasa pemulihan (gambar 15)**




- Ikuti petunjuk untuk menampilkan frasa pemulihan Anda
- Tuliskan kata-kata dengan hati-hati dalam urutan yang benar
- Simpan cadangan ini di lokasi yang aman, idealnya berbeda dari file akun



Frasa pemulihan memungkinkan Anda untuk memulihkan :




- Reputasi Anda, perdagangan Anda
- Dana bitcoin Anda



Tetapi **BUKAN** yang berikut ini:




- Percakapan Anda saat ini dan sebelumnya
- Data pembayaran
- Informasi mitra pengimbang dalam riwayat transaksi




## Membeli dan menjual bitcoin



### 1.a Cara membeli bitcoin: Mengambil penawaran untuk menjual



Refleks pertama seorang pembeli adalah memeriksa penawaran penjualan yang sudah dibiayai dengan bitcoin.



![Vue des offres de vente et filtres](assets/fr/07.webp)





- Pada layar beranda, klik tombol "Beli" (gambar 16)
- Anda kemudian dapat menelusuri daftar bitcoin yang telah ditempatkan di sistem escrow dan siap untuk dijual (gambar 17). Anda bisa melihat jumlah, harga (dalam % relatif terhadap pasar KYC), metode pembayaran, dan mata uang yang diterima.
- Gunakan filter untuk menyortir dan mengurutkan penawaran (gambar 18).
- Catatan: tombol di bagian bawah halaman filter memungkinkan Anda untuk menerima notifikasi ketika penawaran yang cocok dengan filter Anda telah dipublikasikan; dan tombol "reset", yang akan menghapus semua filter (gambar 18).



![Sélection et confirmation d'achat](assets/fr/08.webp)





- Lihat penawaran yang sesuai untuk Anda dan kirim permintaan penukaran (gambar 19)
- Anda dapat membuat beberapa permintaan penukaran, dan penawaran positif pertama akan membatalkan permintaan Anda yang lain.
- Lakukan pembayaran dengan metode yang telah disepakati.


**Pengingat:** sumber dana harus sesuai dengan yang Anda tentukan saat menambahkan metode pembayaran.




- Konfirmasikan pembayaran Anda dalam aplikasi segera setelah selesai**.
- Tunggu sampai penjual menerima pembayaran dan menyatakannya (gambar 20)
- Dan terakhir, evaluasi pengalaman Anda dengan penjual (gambar 21)



![Réception des bitcoins](assets/fr/09.webp)





- Melacak status transaksi Anda
- Periksa konfirmasi penerimaan bitcoin
- Dana akan tersedia dalam portofolio Peach Anda (gambar 22 dan 23)



### 1.b Cara membeli bitcoin: Membuat penawaran



Jika Anda tidak bisa menemukan penawaran yang cocok untuk dijual, Anda bisa membuat penawaran untuk membeli. Karena ini tidak melibatkan bitcoin apa pun pada tahap ini, peluang Anda untuk menemukan mitra bursa akan lebih kecil, terutama jika rekam jejak dan reputasi Anda buruk atau bahkan tidak ada sama sekali. Untuk mengatasinya, saat membuat penawaran, penting untuk *membuat penawaran dengan harga tinggi* untuk memotivasi penjual agar memilih penawaran Anda. Mari kita lanjutkan:



![Creation d'ordre d'achat](assets/fr/10.webp)





- Pada layar beranda, klik tombol "Buat penawaran pembelian" (gambar 24)
- Tambahkan metode pembayaran, jika Anda belum melakukannya, dan masukkan preferensi Anda (jumlah, premium, dll.) (gambar 25).


Opsi "instan" memungkinkan Anda menerima permintaan jual beli secara otomatis.




 - Klik lagi pada "buat tawaran" untuk melanjutkan
- Setelah dibuat, giliran penjual yang akan mendatangi Anda dengan permintaan pertukaran. Anda bisa menutup dan keluar dari aplikasi ini tanpa perlu khawatir.
- Anda bisa mengubah premi jika Anda tidak menerima permintaan apa pun. Ingat: premi yang lebih tinggi akan memotivasi penjual untuk mencari penawaran Anda (gambar 26).
- Anda akan menemukan penawaran Anda di tab "Beli", yang berada di jendela "Exchange" (gbr. 27)



![Reception d'une demande de vente, messagerie](assets/fr/11.webp)





- Ketika Anda menerima permintaan jual beli (gbr. 28) (dan jika Anda belum menonaktifkan jual beli instan pada gbr. 25), terima jual beli tersebut setelah memeriksa reputasi penjual. Jika jual beli instan diaktifkan, langsung ke gambar 29.
- Penjual kemudian harus menempatkan bitcoin dalam sistem escrow, ("mendanai brankas"). (gambar 29)
- Kemudian bayarlah kepada penjual di tempat tujuan yang ditunjukkan pada Gbr. 30, melalui sistem perbankan pribadi Anda. Jangan seret kursor "Saya telah melakukan pembayaran" sampai Anda selesai melakukannya!
- Anda dapat berkomunikasi dengan penjual melalui sistem pesan (terenkripsi P2P). Jika terjadi masalah, Anda dapat membuka sengketa dengan mengklik ikon di sudut kanan atas (gambar 31). Seorang mediator Peach kemudian akan masuk ke dalam diskusi.



![Offre de vente completée](assets/fr/12.webp)





- Setelah penjual menerima uang, ia akan melaporkannya dan sistem escrow akan melepaskan bitcoin, yang akan dikirim ke wallet Anda (secara default melalui GroupHug, sistem pengelompokan transaksi Peach, yang berjalan sekali sehari),
- Beri nilai pengalaman Anda dengan penjual



Itu dia!



**Catatan untuk pembeli baru:** Penjual mendasarkan jual beli mereka pada reputasi pembeli, dan cenderung menghindari tawaran dari pembeli yang belum menyelesaikan jual beli. Akan lebih mudah, pada awalnya, untuk membangun reputasi dengan menerima penawaran yang sudah ada untuk dijual.




### 2.a Cara menjual bitcoin: Membuat penjualan



Cara tercepat dan termudah untuk menjual di Peach adalah dengan **membuat penawaran jual**.



![Création d'un ordre de vente](assets/fr/13.webp)





- Dari halaman beranda, klik "Buat penawaran penjualan" (gambar 32)
- Siapkan penawaran Anda, pastikan Anda memasukkan metode pembayaran dan parameter yang tepat


anda juga bisa :




  - membuat beberapa penawaran yang identik
  - aktifkan "pertukaran instan" sehingga pembeli pertama yang datang dapat mengambil kontrak (tanpa konfirmasi Anda) dan melanjutkan pembayaran.
  - memilih alamat pengembalian dana
  - membiayai bagasi dari wallet Peach Anda
- Membiayai transaksi dengan mengirimkan bitcoin ke alamat yang diberikan (gambar 34)
- Tunggu konfirmasi transaksi. Setelah selesai, penawaran Anda akan terlihat di pasar.



![Attente du paiement](assets/fr/14.webp)





- Tunggu hingga pembeli menerima penawaran Anda. Pertimbangkan untuk meningkatkan premi (%) jika Anda ingin mempercepat prosesnya (gambar 36)
- Setelah Anda menerima permintaan jual beli, periksa reputasi pembeli. Tentukan sendiri apakah profil tersebut cocok untuk Anda, dan klik "terima" jika cocok. (37)
- Sekarang giliran pembeli yang melakukan pembayaran dari banknya ke bank Anda. Dia kemudian akan meneruskan pembayaran kepada Anda. Jangan ragu untuk menghubungi pembeli melalui obrolan.
- setelah memeriksa bahwa dana telah diterima oleh bank Anda*, keluarkan dana dengan mengeklik tombol "saya telah menerima pembayaran" (gambar 38). Jangan pernah mengonfirmasi penerimaan pembayaran sebelum memeriksa bahwa pembayaran telah diterima di rekening Anda.
- Mengevaluasi transaksi
- Bitcoin secara otomatis dilepaskan kepada pembeli,



Ini dia!



**Catatan keamanan dan tips untuk transaksi yang sukses:**




 - Amati detail pembeli, dan periksa apakah asal dana sesuai dengan yang dijelaskan di Peach. Jika asal dana tidak sesuai dengan yang diumumkan, buka Chat dan buka argumen (gambar 39), dan kirimkan kembali dana ke asalnya.
 - Ikuti petunjuk pada kucing kuning.
 - Menanggapi pesan dari rekanan Anda dengan cepat
 - waspada terhadap sikap pembeli, terutama ketika berhadapan dengan profil yang kurang berpengalaman
 - Jangan ragu untuk menggunakan layanan mediasi jika Anda memiliki masalah



### 2.b Cara menjual bitcoin: terima tawaran



Anda juga dapat melihat dan memilih penawaran pembelian. Anda harus sangat berhati-hati, karena di sinilah tempat yang paling banyak ditemukan penipu.



![Prendre une offre d'achat](assets/fr/15.webp)





- Dari halaman beranda, klik "Penjualan" (gambar 40)
- Gunakan filter untuk melihat dan memilih penawaran yang paling menarik (gambar 41)



![vérification de la réputation](assets/fr/16.webp)





- sebelum mengajukan jual beli, kami sarankan Anda menilai kesesuaian profil pembeli. Anda bisa mengklik penawaran, lalu ID pengguna untuk melihat profilnya. Sebagai contoh, penawaran pada gambar 42 dapat dianggap "berisiko" (pengguna baru, jumlah yang relatif tinggi). "Risiko" yang Anda hadapi dengan menerima penawaran ini hanyalah membuang-buang waktu, selama Anda tidak membuat kesalahan dengan melepaskan bitcoin tanpa menerima uangnya. Anda masih bisa menyimpan bitcoin di brankas.


Sebaliknya, penawaran pada gambar 43 berasal dari trader berpengalaman (gambar 44), tanpa ada sengketa dalam sejarahnya. Oleh karena itu, ini adalah penawaran yang lebih kecil risikonya.



![Match avec vendeur](assets/fr/17.webp)





- Setelah penawaran diajukan, jika pembeli menerima permintaan Anda, aplikasi akan membawa Anda ke gambar 34, di mana Anda bisa melanjutkan jual beli seperti yang dijelaskan di bawah ini.




## Keuntungan dan kerugian



### Manfaat Peach





- Tidak memerlukan KYC**: Menjaga kerahasiaan pengguna.
- Tidak ada akses ke detail bank**: Peach tidak memiliki akses ke detail bank atau identitas Anda.
- Interface yang intuitif**: Mudah digunakan untuk pengguna tingkat menengah.
- Sumber Terbuka**: Kode sumber bersifat publik dan dapat diverifikasi oleh komunitas.



### Kekurangan Peach





- Liquidity terbatas**: Volume perdagangan lebih sedikit daripada platform yang lebih mapan.
- Risiko regulasi** : Aplikasi ini dikelola oleh perusahaan Swiss. Oleh karena itu, aplikasi ini tunduk pada peraturan Swiss, yang dapat berkembang dan berpotensi menyensor aplikasi.



## Sumber daya yang berguna





- Video penjelasan bahasa Prancis: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Panduan memulai dengan cepat: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)
- [Support telegram](t.me/peachtopeach) (waspadalah terhadap penipu, administrator tidak akan pernah mengirimi Anda pesan pribadi terlebih dahulu)