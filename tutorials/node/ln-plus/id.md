---
name: Lightning Network+
description: Dapatkan likuiditas masuk gratis dengan pembukaan koperasi pada node Lightning Anda
---

![cover](assets/cover.webp)



## Pendahuluan



[LN+ (Lightning Network Plus)] (https://lightningnetwork.plus/) adalah platform komunitas yang dirancang untuk memfasilitasi kerja sama antara operator simpul Lightning Network. Tujuan utamanya adalah untuk meningkatkan konektivitas, likuiditas, dan desentralisasi jaringan Lightning, tanpa perlu perantara terpusat.



Tutorial ini akan berfokus pada layanan **"Swap "**, yang merupakan fitur strukturisasi yang paling banyak digunakan dan paling banyak digunakan pada LN+ saat ini. Layanan lain yang ditawarkan oleh platform ini juga akan disajikan.



## Gambaran umum LN+



### Apa itu Lightning Network Plus?



Lightning Network Plus (LN+) adalah platform komunitas untuk operator simpul Lightning yang ingin bekerja sama secara langsung dan sukarela. Hal ini bertujuan untuk memfasilitasi pembuatan saluran Lightning yang berguna, seimbang dan berkelanjutan, sambil menghindari kebutuhan akan solusi terpusat atau hub yang dipaksakan.



LN+ didasarkan pada prinsip dasar: kerja sama peer-to-peer, yang didasarkan pada transparansi, timbal balik, dan reputasi.



### Sekilas tentang layanan LN+



LN+ menawarkan beberapa layanan yang dirancang untuk meningkatkan topologi dan likuiditas jaringan Lightning, termasuk:





- Swap**: pembukaan saluran secara timbal balik antar operator (layanan utama).
- Rings**: bukaan saluran melingkar di antara beberapa peserta.
- Swap berbasis kepercayaan**: varian yang lebih mengandalkan kepercayaan dan riwayat peserta.
- Fitur sosial**: profil, komentar, dan sistem reputasi.



Dalam sisa tutorial ini, kita akan berkonsentrasi secara eksklusif pada layanan **Swaps**, yang merupakan inti dari penggunaan LN+ saat ini.



## Layanan "Swap" LN+



### Definisi swap LN+



Pertukaran LN+ adalah perjanjian sukarela antara dua operator simpul Lightning untuk saling membuka saluran Lightning dengan kapasitas yang setara (atau yang telah disepakati sebelumnya). Tidak seperti pembukaan saluran sepihak konvensional, pertukaran ini didasarkan pada **timbal balik eksplisit**.



Dalam praktiknya :





- Anda membuka saluran ke node mitra Anda.
- Mitra Anda membuka saluran ke node Anda.
- Kedua belah pihak mengikat jumlah bitcoin on-chain yang sama.



### Apa tujuan pertukaran untuk operator node?



Layanan Swap mengatasi beberapa masalah utama yang dihadapi oleh operator Lightning:





- Konektivitas yang lebih baik**: pembuatan saluran dua arah yang berguna segera setelah saluran tersebut dibuka.
- Manajemen likuiditas yang lebih baik**: masing-masing pihak memiliki kapasitas masuk dan keluar.
- Mengurangi risiko saluran yang tidak perlu**: mitra didorong untuk tetap membuka saluran.
- Desentralisasi yang lebih besar**: koneksi langsung antara operator, tanpa hub yang dipaksakan.



### Untuk profil simpul mana saja swap berguna?



Swap sangat berguna untuk :





- Node baru yang ingin meningkatkan kemampuan rutenya dengan cepat.
- Operator perantara yang ingin meningkatkan kepadatan grafik saluran mereka.
- Node yang berorientasi pada perutean yang ingin mengoptimalkan topologi mereka.



## Hubungkan node Lightning Anda ke LN+



### Persyaratan teknis



Sebelum memulai, Anda akan memerlukan :





- Simpul Petir yang berfungsi (LND, Core Lightning atau Eclair).
- Akses ke antarmuka manajemen node Anda.
- Kapasitas on-chain yang memadai untuk membuka saluran.



Buka situs web [Lightning Network] (https://lightningnetwork.plus/) Plus dan klik tombol `Login` di bagian kanan atas antarmuka.



![capture](assets/fr/03.webp)



### Otentikasi dengan tanda tangan pesan



Untuk mengautentikasi diri Anda, Anda perlu menandatangani pesan yang disediakan menggunakan kunci pribadi Lightning node Anda. Dengan ThunderHub, operasi ini sangat sederhana.



Mulailah dengan menyalin pesan yang ditampilkan oleh LN+.



![capture](assets/fr/04.webp)



Pada ThunderHub, buka tab `Tools`, kemudian klik tombol `Sign` di bagian `Messages`.



![capture](assets/fr/05.webp)



Rekatkan pesan autentikasi yang disediakan oleh LN+, lalu klik `Tanda tangani`.



![capture](assets/fr/06.webp)



ThunderHub kemudian menandatangani pesan ini menggunakan kunci privat node Anda. Salin tanda tangan yang dihasilkan.



![capture](assets/fr/07.webp)



Rekatkan tanda tangan ini ke dalam bidang yang sesuai di situs LN+, lalu klik `Masuk`.



![capture](assets/fr/08.webp)



Anda sekarang terhubung ke LN+ dengan node Lightning Anda. Proses ini memungkinkan LN+ untuk memverifikasi bahwa Anda adalah pemilik sah dari node yang Anda klaim di platform mereka.



![capture](assets/fr/09.webp)



Jika mau, Anda dapat mempersonalisasi profil LN+ Anda, misalnya dengan menambahkan biografi singkat.



## Berpartisipasi dalam swap yang ada



### Akses ke penawaran swap



Untuk berpartisipasi dalam pembukaan saluran pertama Anda, buka menu `Swaps` di bagian atas antarmuka. Di sini Anda akan menemukan semua swap yang tersedia saat ini, tergantung pada karakteristik node Anda.



![capture](assets/fr/10.webp)



### Ketentuan kelayakan



Untuk bergabung dengan penawaran swap yang sudah ada, cukup pilih iklan yang sesuai dan daftar. Namun, LN+ memungkinkan pembuat swap untuk menentukan **ketentuan kelayakan** tertentu, seperti :





- jumlah minimum saluran yang sudah terbuka ;
- total kapasitas simpul minimum;
- jenis koneksi tertentu yang diterima.



### Node terbaru



Akibatnya, terutama pada tahap awal penggunaan, ada kemungkinan **sedikit atau tidak ada penawaran yang tersedia** untuk node Anda. Ini adalah situasi yang umum terjadi pada node baru atau node yang belum terhubung.



Dalam kasus saya, meskipun ada beberapa saluran yang terbuka, tidak ada satu pun penawaran yang memenuhi kriteria yang dibutuhkan.



## Buat penawaran swap Anda sendiri



### Kapan sebaiknya Anda membuat swap Anda sendiri?



Jika tidak ada penawaran yang tersedia, membuat swap Anda sendiri sering kali merupakan solusi terbaik. Hal ini juga memungkinkan Anda untuk mempertahankan kontrol atas parameter swap.



### Konfigurasi penukaran



Klik **Mulai Liquidity Swap**, lalu konfigurasikan parameter penawaran Anda:





- pilih jumlah total peserta (3, 4 atau 5);
- menunjukkan kapasitas saluran yang akan dibuka;
- menentukan periode komitmen di mana peserta setuju untuk tidak menutup saluran mereka;
- tentukan batasan apa pun yang berlaku untuk peserta (jumlah saluran minimum, kapasitas total minimum, jenis koneksi yang diterima).



![capture](assets/fr/11.webp)



### Publikasi dan harapan peserta



Setelah semua parameter dimasukkan, klik **Mulai Liquidity Swap** untuk mempublikasikan penawaran Anda. Sekarang yang harus Anda lakukan adalah menunggu operator lain mendaftar.



![capture](assets/fr/12.webp)



## Menyelesaikan pertukaran



### Pembukaan saluran yang efektif



Sekarang setelah semua posisi swap telah diambil, setiap peserta dapat melihat, dari antarmuka LN+-nya, node mana yang dia perlukan untuk membuka saluran Lightning.



![capture](assets/fr/13.webp)



Di sisi Anda, buka saluran menggunakan Node ID yang disediakan oleh LN+ dan perhatikan jumlah yang ditunjukkan. Operasi ini dapat dilakukan melalui ThunderHub, manajer node Lightning lain atau langsung melalui antarmuka dasar node Anda.



![capture](assets/fr/14.webp)



Setelah dibuka, saluran akan muncul di bagian saluran tunggu.



![capture](assets/fr/15.webp)



### Konfirmasi dalam LN+



Kemudian kembali ke LN+ untuk mengonfirmasi bahwa Anda telah memulai pembukaan saluran, dengan mengeklik tombol `Pembukaan Saluran Dimulai`.



![capture](assets/fr/16.webp)



### Akhir pertukaran



Ketika semua peserta telah membuka saluran yang telah mereka komit, swap dianggap selesai.



## Reputasi dan praktik komunikasi yang baik



### Sistem reputasi LN+



LN+ menggabungkan sistem reputasi berdasarkan opini yang ditinggalkan oleh para peserta pada akhir swap. Opini ini bersifat publik dan secara langsung memengaruhi kemampuan operator untuk bergabung atau membuat swap di masa mendatang.



![capture](assets/fr/17.webp)



### Praktik terbaik yang direkomendasikan



Untuk menjaga reputasi yang baik dan memastikan kelancaran swap, disarankan untuk :





- menghormati tenggat waktu pembukaan saluran;
- berkomunikasi dengan cepat jika terjadi masalah atau penundaan;
- gunakan bagian komentar untuk bertukar pandangan dengan peserta lain;
- tidak menutup saluran sebelum akhir periode komitmen.




![capture](assets/fr/18.webp)



### Mengapa reputasi merupakan hal yang penting bagi LN+



LN+ didasarkan pada model kerja sama sukarela, tanpa kendala teknis yang kuat. Oleh karena itu, reputasi merupakan insentif utama untuk memastikan keandalan dan kepercayaan para peserta.



## Layanan LN+ lainnya



Selain Swap, LN+ menawarkan layanan lain yang dirancang untuk meningkatkan konektivitas dan koordinasi antara operator simpul Lightning. Rings** memungkinkan beberapa peserta untuk membuat lingkaran bukaan saluran, sehingga memperkuat redundansi jalur perutean dan kepadatan grafik Lightning. Trust-based swap** didasarkan pada prinsip-prinsip yang mirip dengan swap klasik, tetapi menawarkan fleksibilitas yang lebih besar kepada peserta yang sudah memiliki reputasi yang mapan di platform.



LN+ juga mengintegrasikan fitur-fitur sosial seperti profil simpul publik, bertukar komentar dan sistem reputasi. Alat-alat ini bukanlah layanan teknis semata, tetapi memainkan peran penting dalam kelancaran platform, memfasilitasi komunikasi, koordinasi, dan kepercayaan antar operator.



## Kesimpulan



Layanan Swap LN+ adalah alat yang efektif untuk meningkatkan konektivitas, likuiditas, dan desentralisasi dalam jaringan Lightning. Dengan mempromosikan pembukaan saluran yang timbal balik dan terkoordinasi, LN+ memungkinkan operator node untuk memperkuat topologi mereka, sementara pada saat yang sama mempromosikan kerja sama yang bertanggung jawab dan terdesentralisasi.