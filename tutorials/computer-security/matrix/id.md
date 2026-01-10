---
name: Matrix
description: Panduan untuk memahami, mengonfigurasi, dan menggunakan Matrix, platform komunikasi yang aman, terbuka, dan terdesentralisasi.
---

![cover](assets/cover.webp)



## Apa yang dimaksud dengan Matrix?



Matrix adalah **protokol komunikasi terdesentralisasi** yang dirancang untuk memungkinkan pertukaran pesan, file, dan panggilan audio/video antara pengguna dan aplikasi, tanpa ketergantungan pada perusahaan pusat. Tidak seperti platform pengiriman pesan tradisional, Matrix adalah **infrastruktur terbuka**, sebanding dengan email: setiap orang dapat memilih server atau mengoperasikannya sendiri, dengan tetap memiliki kemampuan untuk bertukar dengan seluruh jaringan.



Matriks dibedakan oleh tiga prinsip dasar:



### Sebuah protokol, bukan aplikasi



Matrix bukanlah aplikasi seperti WhatsApp atau Telegram.


Ini adalah bahasa standar yang dapat digunakan oleh banyak aplikasi.


Dengan kata lain, berbagai macam perangkat lunak Element, FluffyChat, Cinny, Nheko, dan lainnya, menyediakan akses ke jaringan Matrix yang sama.



Hal ini menjamin kebebasan total: perubahan aplikasi tanpa kehilangan kontak, keragaman antarmuka, kemandirian dari pemasok tunggal.



![capture](assets/fr/03.webp)



### Jaringan yang terdesentralisasi dan federasi



Struktur Matrix didasarkan pada **federasi**, sebuah model di mana beberapa server independen bekerja sama satu sama lain.


Setiap server (disebut _homeserver_) dapat menjadi tuan rumah bagi pengguna, ruang obrolan, dan menyinkronkan pesan dengan server lain di jaringan.


Dengan demikian :





- tidak ada satu entitas pun yang mengendalikan seluruh sistem;
- server dapat menghilang tanpa mempengaruhi jaringan lainnya;
- setiap organisasi atau individu dapat mengelola ruangnya sendiri.



Model ini memastikan **ketangguhan yang tinggi** dan mencerminkan nilai-nilai kedaulatan teknologi.



![capture](assets/fr/03.webp)



### Sistem yang aman dan terenkripsi



Matrix mendukung **enkripsi ujung ke ujung (E2EE) ** untuk pertukaran pribadi dan grup terenkripsi.


Pesan hanya dapat dibaca oleh peserta, bukan oleh server perantara.


Pendekatan ini memungkinkan untuk berkomunikasi tanpa mengekspos konten pertukaran ke pihak ketiga, sambil mempertahankan transparansi protokol dan kemungkinan untuk meng-host server sendiri.



![capture](assets/fr/05.webp)



### Interoperabilitas yang unik



Salah satu aset utama Matrix adalah kemampuannya untuk bertindak sebagai **jembatan antara sistem komunikasi yang berbeda**. Berkat _jembatan_, semua bisa terhubung:





- Telegram
- WhatsApp
- Signal
- Messenger
- Kendur
- Perselisihan
- IRC, XMPP, dll.



Hal ini memungkinkan untuk menyatukan komunitas yang tersebar di beberapa platform, namun tetap memegang kendali atas infrastruktur.



![capture](assets/fr/06.webp)



## Bagaimana cara kerja Matrix?



Bagian ini menyajikan struktur internal jaringan Matrix untuk memahami bagaimana pengguna, server, dan aplikasi berinteraksi dalam ekosistem yang terdesentralisasi ini. Matrix didasarkan pada tiga elemen penting: _homeserver_, identitas, dan _klien_ yang digunakan untuk berkomunikasi.



### Server: pelayan rumah



Matrix berjalan pada server independen yang disebut _homeserver_.


Setiap server rumah mengelola :





- akun-akun pengguna yang dihostingnya,
- percakapan pribadi dan ruang tunggu yang diikuti oleh para pengguna,
- sinkronisasi dengan server jaringan lain.



Semua homeserver yang terhubung ke jaringan Matrix secara otomatis bertukar pesan dan acara dari ruang tamu bersama. Sebagai contoh:





- pengguna yang terdaftar di server A dapat mengobrol dengan pengguna di server B,
- sebuah salon dapat tersebar di puluhan server,
- tidak ada yang memiliki kendali atas salon atau komunitas secara keseluruhan.



Model ini sangat tangguh dan memungkinkan setiap organisasi atau individu untuk mengelola infrastruktur mereka sendiri.



### Pengidentifikasi matriks



Setiap pengguna memiliki pengenal unik, yang disebut **MXID** (_Matrix ID_), yang terlihat seperti alamat:



```bash
@nomdutilisateur:serveur.xyz
```



Terdiri dari :





- nama pengguna, diawali dengan **@**
- nama server tempat akun dibuat, diawali dengan **:**



Contoh:





- `@alice:matrix.org`
- `@bened:monserveur.bj`



Pengenal ini memungkinkan komunikasi dengan pengguna Matrix lainnya, terlepas dari server asalnya.



### Klien matriks (aplikasi)



Untuk menggunakan Matrix, Anda harus terhubung dengan aplikasi yang disebut **client Matrix**.



Yang paling terkenal adalah :





- Elemen (web, seluler, desktop)
- FluffyChat (seluler)
- Cinny (web/desktop minimalis)
- Nheko (desktop)



Aplikasi-aplikasi ini hanyalah antarmuka untuk file :





- untuk melihat pesan,
- mengirim teks, gambar, atau file,
- bergabung atau membuat pameran dagang,
- melakukan panggilan audio/video.



Semua aplikasi berkomunikasi dengan server melalui protokol standar yang sama.



### Kamar dan pesan pribadi (DM)



Di Matrix, pertukaran dilakukan di **ruangan** :





- sebuah ruangan bisa bersifat publik atau privat
- dapat menampung dua orang atau ribuan orang
- dapat dibagi di antara beberapa server
- memiliki pengenal unik yang dimulai dengan **!**



Pesan pribadi hanyalah ruang obrolan dengan dua peserta, sering disebut sebagai **DM (Direct Messages)**.



Sinkronisasi salon berlangsung secara real time antara server yang berpartisipasi, memastikan pengalaman yang mulus dengan tetap mempertahankan desentralisasi.



## Mengapa menggunakan Matrix?



Matrix bukan hanya sebuah alternatif dari sistem pesan terpusat: Matrix adalah teknologi yang memenuhi kebutuhan nyata dalam hal kedaulatan digital, keamanan, dan interoperabilitas. Ada banyak alasan mengapa semakin banyak orang, perusahaan, dan institusi memilih protokol ini untuk berkomunikasi.



### Dapatkan kembali kendali atas komunikasi Anda



Sebagian besar platform perpesanan beroperasi dengan model terpusat: satu pemain mengendalikan server, akses, data, dan aturan penggunaan. Model ini menyiratkan ketergantungan total pada pemasok.


Matrix mengambil pendekatan yang berbeda.


Siapa pun bisa memilih tempat untuk meng-host akun mereka, atau bahkan menggunakan server mereka sendiri. Tidak ada entitas yang dapat memblokir pengguna, meminta identifikasi yang mengganggu, atau memaksakan perubahan kebijakan.


Arsitektur ini memberikan otonomi kembali kepada individu dan organisasi. Komunikasi tidak lagi didasarkan pada kepercayaan terhadap perusahaan, tetapi pada protokol yang terbuka, terdokumentasi, dan dapat diverifikasi.



### Komunikasi yang aman dan terenkripsi



Matrix mendukung enkripsi ujung ke ujung untuk percakapan pribadi dan grup. Mekanisme ini memastikan bahwa hanya peserta yang dapat membaca pesan, bahkan jika pesan tersebut melewati server pihak ketiga dalam federasi.



Protokol ini menggunakan algoritma Megolm/Olm, yang dirancang khusus untuk memberikan keamanan yang kuat dalam lingkungan multi-perangkat yang terdistribusi.



Hal ini memungkinkan untuk :





- melindungi percakapan sensitif,
- mencegah akses yang tidak sah (bahkan dari server host),
- menjaga kerahasiaan dalam jangka panjang.



Enkripsi bukanlah sebuah pilihan: ini adalah komponen inti dari protokol.



### Tidak lagi bergantung pada satu aplikasi



Matrix bukanlah sebuah aplikasi, tetapi sebuah protokol.



Keragaman pelanggan ini menjamin :





- pilihan yang disesuaikan dengan kebutuhan individu,
- kemampuan untuk menggunakan Matrix pada semua jenis perangkat,
- tidak ada ketergantungan pada satu perangkat lunak.



Jika pelanggan tidak cocok atau tidak lagi dipertahankan, cukup pilih yang lain: akun terus beroperasi secara normal.



### Menyatukan dan menghubungkan berbagai komunitas yang berbeda



Federasi memungkinkan server-server yang berbeda untuk bekerja bersama sambil dikelola secara independen.


Dengan demikian :





- sebuah organisasi dapat mengelola homeserver-nya sendiri,
- individu dapat bergabung dengan server publik,
- semua dapat berkomunikasi satu sama lain seolah-olah mereka berada di platform yang sama.



Fleksibilitas ini memungkinkan untuk menciptakan ruang komunikasi yang disesuaikan dengan setiap kebutuhan: tim, asosiasi, komunitas, institusi, atau proyek open source.



Matrix sangat populer di kalangan teknis, kolektif aktivis, peneliti, pemerintah, dan semakin populer di komunitas Bitcoin.



### Interoperabilitas yang unik dalam lanskap perpesanan



Salah satu aset utama Matrix adalah kemampuannya untuk **memperluas** pertukaran berkat jembatan yang mampu menghubungkan :





- WhatsApp
- Telegram
- Signal
- Kendur
- Perselisihan
- IRC
- XMPP
- dan banyak platform lainnya



Dengan demikian, Matrix menjadi lapisan pemersatu untuk komunikasi, menyatukan beberapa komunitas yang tersebar di berbagai aplikasi.



Interoperabilitas ini mengurangi fragmentasi dan menyederhanakan kolaborasi.



### Protokol yang gratis, terbuka, dan berkelanjutan



Protokol Matrix sepenuhnya open source dan dikembangkan secara transparan.


Hal ini menjamin beberapa keuntungan:





- evolusi berkelanjutan dari standar,
- kemampuan bagi siapa saja untuk memeriksa kode,
- independensi dari perubahan komersial atau politik,
- ketahanan jangka panjang.



Tidak seperti sistem perpesanan berpemilik, masa depan Matrix tidak bergantung pada satu perusahaan, tetapi pada komunitas global dan standar terbuka.



## Bagaimana cara membuat akun Matrix?



Membuat akun Matrix sangat mudah dan tidak memerlukan keahlian teknis. Pengguna dapat bergabung dengan server yang sudah ada, membuat login dan langsung mulai mengobrol. Bagian ini menguraikan langkah-langkah penting.



### Pilih server (publik atau pribadi)



Matrix adalah jaringan federasi: ada banyak server (homeserver) yang dikelola oleh berbagai organisasi, komunitas, atau individu. Pilihan server hanya menentukan di mana akun di-host, tetapi tidak menghalangi komunikasi dengan seluruh jaringan.


*tersedia dua opsi:** * Dua pilihan



### - Gunakan server publik



Ini adalah solusi yang paling sederhana.


Contoh-contoh server yang populer:





- _matrix.org_ (yang paling terkenal)
- _envs.net_
- server komunitas tematik (teknologi, privasi, sumber terbuka...)



Server-server ini cocok untuk pengguna pemula yang ingin mendaftar dengan cepat.



### - Gunakan server pribadi



Ideal untuk :





- sebuah organisasi,
- sebuah keluarga,
- sebuah proyek sumber terbuka,
- tim kerja,
- atau untuk penggunaan yang berdaulat dan mandiri.



Dalam hal ini, seseorang harus mengelola server (Synapse, Dendrite, Conduit...).


Apa pun server yang Anda pilih, para pengguna dapat berbicara satu sama lain berkat federasi.



### Membuat akun langkah demi langkah



Karena Matrix adalah protokol terbuka, ia dapat diakses oleh beberapa aplikasi.


Seperti yang dijelaskan di atas, mereka menawarkan antarmuka dan fungsi yang berbeda, tergantung pada kebutuhan:





- Element**: klien terlengkap, tersedia di semua platform.
- FluffyChat**: sederhana, modern, dan ideal untuk ponsel.
- Nheko**: klien yang ringan dan ergonomis untuk PC.
- SchildiChat**: Varian elemen dengan peningkatan ergonomis.
- NeoChat**: terintegrasi ke dalam ekosistem KDE.



Pilihan klien tidak berdampak pada akun: semua bekerja dengan server Matrix mana pun.



### Langkah-langkah klasik :





- Buka aplikasi yang dipilih. Dalam kasus kita, kita akan melakukan ini dengan [Element](app.element.io).
- Pilih "Buat akun".



![cover-kali](assets/fr/10.webp)



Untuk mempermudah, Anda dapat membuat akun Matrix menggunakan **Google, Facebook, Apple, GitHub atau GitLab**. Layanan-layanan ini hanya akan mengetahui bahwa akun mereka telah digunakan untuk mengakses Matrix: ini dikenal sebagai **koneksi sosial**.



Untuk kerahasiaan yang lebih baik, Anda juga dapat mendaftar secara manual dengan memilih **nama pengguna**, **kata sandi**, dan **alamat email**.



Tergantung pada server yang dipilih, **captcha** mungkin diperlukan, serta persetujuan atas **syarat penggunaan**.



Setelah pendaftaran divalidasi, email konfirmasi akan dikirimkan.


Cukup klik tautan untuk mengaktifkan akun Anda dan mengakses aplikasi web (Element) untuk bergabung dalam percakapan Matrix pertama Anda.



![cover-kali](assets/fr/11.webp)



Anda sekarang memiliki akun dan menggunakan versi Web Element.



## Tambahkan kontak pertama Anda



Untuk berkomunikasi dengan seseorang di Matrix, yang perlu Anda ketahui adalah pengenal lengkapnya, yaitu **Matrix ID**.



Contoh:



`@alice:matrix.org @bened:monserveur.bj`



### Menambahkan kontak



Untuk mengundang teman ke obrolan grup Anda, klik lingkaran `i` di sudut kanan atas. Ini akan membuka panel sebelah kanan. Klik "Orang" untuk menampilkan daftar anggota di ruangan ini: Anda seharusnya menjadi satu-satunya yang hadir saat ini.



![cover-kali](assets/fr/12.webp)



Klik "Undang ke ruangan ini" di bagian atas daftar orang dan sebuah prompt akan terbuka sehingga Anda dapat mengundang teman Anda untuk bergabung dengan Anda di Matrix. Jika mereka sudah masuk ke Matrix, masukkan ID Matrix mereka. Jika belum, masukkan alamat email mereka dan mereka akan diundang untuk bergabung.



Tidak ada sistem "teman": kontak hanyalah seseorang yang telah membuka percakapan.



![cover-kali](assets/fr/13.webp)



Orang yang Anda undang dapat menerima atau menolak undangan tersebut. Jika mereka menerima, Anda akan melihat mereka bergabung ke dalam ruangan. Lebih banyak lebih baik!



![cover-kali](assets/fr/14.webp)



### Menyiapkan server Anda sendiri



Matrix benar-benar menjadi miliknya ketika digunakan bersama dengan server pribadi.


Menyebarkan server rumah Anda sendiri memungkinkan Anda untuk :





- mempertahankan kontrol penuh atas data,
- menentukan aturan penggunaannya sendiri,
- meng-host beberapa akun (teman, tim, komunitas),
- dan memastikan ketahanan maksimum jika terjadi pembatasan atau penyensoran.



**Solusi yang tersedia:**





- Synapse**: implementasi bersejarah dan terlengkap.
- Dendrite**: lebih ringan, lebih bertenaga, dan dirancang untuk protokol masa depan.
- Conduit**: varian minimalis yang mudah digunakan.



*prasyarat:** *** Persyaratan





- nama domain,
- mesin atau VPS,
- keterampilan administrasi sistem minimum.



Meskipun memerlukan sedikit konfigurasi, mengelola server Anda sendiri mengubah Matrix menjadi alat yang berdaulat dan tahan lama.



### Bergabung dengan pameran dagang pertama Anda



Matrix sangat bergantung pada _ruang_ (ruang keluarga).


Ada pameran perdagangan publik, swasta, komunitas, teknis, lokal, dan internasional.



**Tiga cara untuk bergabung dengan salon:**



1. **Melalui tautan undangan** (biasanya dalam bentuk URL `matrix.to`).


2. **Mencari nama salon** dalam aplikasi.


3. **Dengan memasukkan ID acara lengkap**, mis:


`#bitcoin:matrix.org`


`#communauté-bénin:monsrv.bj`



Setelah bergabung, chatroom berperilaku seperti newsgroup klasik, dengan riwayat, enkripsi, file, reaksi, dan panggilan audio/video, tergantung pada klien yang digunakan.



![capture](assets/fr/09.webp)



## Melangkah lebih jauh



Setelah Anda menguasai dasar-dasarnya, Matrix menawarkan sejumlah kemungkinan tingkat lanjut. Apakah Anda ingin menghubungkan sistem perpesanan lain, meng-host server Anda sendiri atau mengorganisir sebuah komunitas, ekosistemnya sangat kaya.



### Jembatan (WhatsApp, Telegram, Signal, dll.)



Sebuah jembatan yang menghubungkan Matrix ke sistem perpesanan lainnya.


Dengannya, Anda dapat mengirim dan menerima pesan dari :





- WhatsApp
- Telegram**
- Signal**
- Facebook Messenger
- Perselisihan
- Kendur**
- IRC** (IRC)
- dan banyak lainnya



### Apa yang dapat dilakukan jembatan





- Memusatkan semua percakapan Anda di Matrix
- Menyediakan antarmuka terbuka untuk interaksi dengan layanan berpemilik
- Mengelola komunitas multi-platform dari satu lokasi



Beberapa jembatan merupakan jembatan resmi, sementara yang lainnya berbasis komunitas.


Tergantung pada departemennya, mereka mungkin memerlukan :





- server pribadi,
- konfigurasi tambahan,
- atau penggunaan jembatan umum yang sudah ada.



### Menggunakan Matrix untuk organisasi, komunitas, atau proyek Bitcoin



Matrix bukan hanya alat bantu pribadi.


Ini dapat digunakan untuk menyusun kelompok kerja, mengorganisir komunitas lokal atau mengelola komunikasi proyek.



**Contoh penggunaan:**





- Komunitas sumber terbuka
- Proyek ekosistem Bitcoin dan Lightning
- Kelompok mahasiswa atau pengembang
- Organisasi warga negara
- Media independen
- Kelompok dan asosiasi lokal



**Mengapa ini menarik?





- 100% alat sumber terbuka**
- Komunikasi yang berdaulat dan terdesentralisasi**
- Ruang yang diatur ke dalam **lounge**, **subkelompok**, **ruang pribadi**, dll.
- Integrasikan dengan Nextcloud, GitLab, Mattermost, atau bot khusus
- Manajemen izin dan moderasi yang disesuaikan dengan baik



Matrix kemudian menjadi pilar komunikasi untuk struktur apa pun yang ingin tetap independen dari platform besar yang terpusat.



## Kesimpulan



Matrix mewakili solusi modern, terbuka dan aman untuk komunikasi real-time, menawarkan alternatif terdesentralisasi untuk platform tradisional. Berkat arsitektur federasi dan protokol enkripsi yang canggih, Matrix memungkinkan pengguna untuk mempertahankan kendali atas data mereka sambil menikmati pengalaman yang lancar dan dapat dioperasikan. Baik untuk penggunaan pribadi, profesional, atau komunitas, Matrix menawarkan kerangka kerja yang kuat dan terukur untuk membangun lingkungan komunikasi yang disesuaikan dengan kebutuhan saat ini.



Untuk mengetahui lebih lanjut dan menemukan semua fitur yang ditawarkan oleh Matrix, Anda dapat membaca dokumentasi resmi yang tersedia di sini :


[https://matrix.org/docs/](https://matrix.org/docs/)