---
name: Mempool
description: Jelajahi seluruh ekosistem Bitcoin.
---

![cover](assets/cover.webp)



Protokol Bitcoin adalah jaringan terdesentralisasi yang bersifat pseudonim dan terbuka untuk konsultasi. Anggota (node), yaitu komputer yang memiliki contoh perangkat lunak Bitcoin, memiliki akses tak terbatas ke semua data yang dipublikasikan di Bitcoin. Namun, pada tahun-tahun awal Bitcoin, protokol ini tidak dapat diakses secara luas seperti saat ini.


Pada masa-masa awal Bitcoin, perlu menjalankan node Bitcoin untuk mengakses alat yang sesuai (bitcoin-cli) untuk menginterogasi jaringan dari baris perintah.



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Oleh karena itu, berbagai proyek telah diluncurkan untuk memperluas komunitas Bitcoin, sehingga lebih mudah diakses oleh siapa saja yang tidak memiliki node dan/atau tidak memiliki keterampilan teknis yang diperlukan.



Dalam tutorial ini, kita akan melihat proyek **Mempool.space**, fitur-fiturnya, dan dampak yang ditimbulkannya terhadap ekosistem Bitcoin.



## Apa itu Mempool.space?



**Mempool.space** adalah penjelajah sumber terbuka yang menyediakan informasi berguna tentang transaksi, biaya transaksi, blok, dan penambang di berbagai jaringan protokol Bitcoin. Diluncurkan pada tahun 2020, aplikasi ini membawa peningkatan yang signifikan dalam pengalaman pengguna melalui grafik yang representatif, animasi yang halus, dan antarmuka yang rapi.



Untuk memahami proyek ini, Mempool (kumpulan memori) adalah ruang virtual tempat semua transaksi yang menunggu konfirmasi di jaringan Bitcoin disimpan. Mempool seperti sebuah "ruang tunggu" di mana transaksi Bitcoin menunggu untuk dikonfirmasi. Setiap komputer di jaringan (node) memiliki ruang tunggu sendiri, yang menjelaskan mengapa tidak semua transaksi dapat dilihat oleh semua orang pada waktu yang sama.



Dampak utama dari platform dalam ekosistem Bitcoin adalah memungkinkan Anda untuk mengakses beragam informasi di area memori sebagian besar node yang ada di Bitcoin tanpa perlu menjalankannya. Mempool.space adalah tempat penyimpanan untuk melihat dan mencari jaringan protokol Bitcoin.



Penggunaan yang semakin meluas dalam ekosistem dan fakta bahwa Mempool.space adalah open source telah memungkinkannya untuk diintegrasikan ke dalam lebih banyak sistem hosting pribadi. Anda sekarang dapat memiliki instans Mempool.space Anda sendiri secara langsung di node pribadi Anda. Lihat tutorial kami tentang cara mengonfigurasi Mempool.space pada node Umbrel Anda di bawah ini.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Dasar-dasar Mempool.space



Seperti yang telah disebutkan di atas, [Mempool.space](https://Mempool.space) adalah penjelajah protokol Bitcoin yang memungkinkan Anda untuk memonitor transaksi Anda dan penyebarannya di jaringan Bitcoin yang dipilih secara real time, dari sebuah grafis Interface.



Mempool.space mendukung banyak jaringan protokol Bitcoin.


Pada bilah menu, Anda akan menemukan jaringan berikut ini:




- **Mainnet**: Jaringan Bitcoin utama tempat transaksi Bitcoin yang sebenarnya terjadi.
- **Signet**: Jaringan uji coba yang menggunakan tanda tangan digital untuk memvalidasi blok tanpa memerlukan sumber daya yang dibutuhkan oleh jaringan utama.
- **Testnet 3**: Jaringan pengujian dan pengembangan bebas risiko pada protokol Bitcoin.
- **Testnet 4**: Versi baru Testnet 3 menghadirkan stabilitas yang lebih baik dan aturan konsensus baru ke lingkungan pengujian.



![reseaux](assets/fr/01.webp)



Pada halaman beranda, di sebelah kiri di Green, Anda akan melihat kemungkinan blok-blok (kelompok transaksi) di masa depan yang siap untuk divalidasi dan diintegrasikan (ditambang) ke dalam jaringan Bitcoin. Rata-rata, sebuah blok ditambang setiap sepuluh menit: simpan informasi ini, karena akan sangat berguna di kemudian hari dalam pengembangan kita.


Pada warna keunguan, di sisi kanan, Anda akan menemukan blok-blok terakhir yang ditambang di Bitcoin, dengan nomor blok terakhir yang ditambang mewakili ketinggian jaringan saat ini.



![blocs](assets/fr/02.webp)



Bagian **Biaya Transaksi** adalah perkiraan biaya transaksi. Semakin tinggi biaya yang dialokasikan untuk transaksi Anda, semakin besar kemungkinan transaksi Anda akan ditambahkan ke blok berikutnya yang siap untuk ditambang.


Biaya transaksi merupakan biaya yang akan diambil Miner dari Anda untuk memasukkan transaksi Anda ke dalam blok kandidat untuk Mining. Biaya ini ditentukan oleh rasio sat/vB (Satoshi/Virtual Bytes) yang mewakili jumlah satoshi yang Anda bayarkan untuk ruang yang akan ditempati oleh transaksi Anda di blok kandidat.



⚠️ PENTING: Jika terjadi kejenuhan Mempool, penambang akan memprioritaskan transaksi yang menawarkan rasio Satoshi/vByte terbaik. Semakin berat (besar) transaksi Anda, semakin banyak satoshi yang perlu dimasukkan dengan cepat.



![fees-visualizer](assets/fr/03.webp)



Bagian **Mempool Goggles** memungkinkan Anda memvisualisasikan ruang yang ditempati oleh suatu transaksi.



![mempool](assets/fr/04.webp)



Sebuah blok ditambang kira-kira setiap sepuluh menit karena tingkat kesulitan Proof of Work yang harus disediakan oleh para penambang untuk menambahkan kandidat blok mereka ke dalam rantai blok yang ditambang. Tingkat kesulitan ini bervariasi setiap **2016 blok**, setara dengan sekitar **2 minggu**. Anda dapat melihat evolusi tingkat kesulitan ini di sini.



![difficulty](assets/fr/05.webp)



Penambahan blok baru ke rantai utama memberikan hak kepada Miner dari blok yang divalidasi untuk mendapatkan hadiah yang terdiri dari bagian tetap (dibelah dua setiap 210.000 blok**, setara dengan sekitar 4 tahun** selama pembagian) dan biaya transaksi.



![halving](assets/fr/06.webp)



## Mengakses detail transaksi Anda



Pada bilah pencarian Mempool.space, Anda dapat memasukkan Bitcoin Address atau transaction ID untuk mengetahui lebih lanjut tentang riwayat Anda.



![search](assets/fr/07.webp)



Pada halaman detail transaksi, Anda akan menemukan informasi umum tentang transaksi Anda:




- **Status**: Dikonfirmasi saat ditambahkan ke blok, belum dikonfirmasi saat menunggu di Mempool.
- Biaya transaksi.
- **Perkiraan waktu kedatangan (ETA)**: Perkiraan waktu yang diperlukan agar transaksi Anda ditambahkan ke dalam blok. Ini dihitung berdasarkan rasio yang merupakan biaya yang terkait dengan transaksi ini.



![general-txinfo](assets/fr/08.webp)



Bagian **Flow** menunjukkan grafik komponen transaksi Anda.



Input (sebelumnya UTXO), digunakan untuk transaksi Anda, dan output yang memberikan hak kepada penerima untuk menggunakan bitcoin dari setiap output dengan menunjukkan tanda tangan yang diperlukan untuk pengeluaran mereka.



![flow](assets/fr/09.webp)



Rincian lebih lanjut mengenai alamat yang digunakan dapat ditemukan di bagian **Input & Output**.



![address](assets/fr/10.webp)



Temukan berbagai skema transaksi Bitcoin untuk meningkatkan kerahasiaan Anda.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Mempercepat transaksi Anda



Dalam ekosistem Bitcoin, aspek validasi transaksi oleh penambang secara intrinsik terkait dengan biaya transaksi yang terkait dengan transaksi tersebut. Penambang memprioritaskan transaksi dengan rasio biaya yang lebih tinggi (satoshi/vBytes), yang dapat memengaruhi keabsahan transaksi Anda jika Anda tidak membayar biaya yang wajar yang diterima oleh penambang. Transaksi Anda akan tertahan di Mempool karena menunggu blok yang menerima rasio biaya tersebut.



Untungnya, ada dua metode yang tersedia di jaringan Bitcoin untuk mempercepat konfirmasi transaksi Anda.





- **RBF** - Penggantian Dengan Biaya: Metode yang memungkinkan Anda untuk membelanjakan entri yang sama dengan transaksi berbiaya rendah Anda, tetapi kali ini dengan meningkatkan biaya transaksi untuk mempercepat validasi. Transaksi baru Anda akan divalidasi lebih cepat dan dimasukkan ke dalam blok, sehingga membatalkan transaksi dengan biaya rendah.



Anda dapat melakukan tindakan penggantian biaya dengan portofolio yang menerima mekanisme ini. Sebagai contoh, lihat artikel kami tentang portofolio Blue Wallet.



https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- **CPFP** - Child pay for parent: Pendekatan yang terinspirasi oleh RBF, tetapi dari sisi penerima. Ketika transaksi di mana Anda sebagai penerima diblokir dalam Mempool, Anda memiliki opsi untuk membelanjakan hasil (UTXO) dari transaksi ini, terlepas dari fakta bahwa transaksi tersebut belum dikonfirmasi, dengan mengalokasikan lebih banyak biaya ke transaksi baru ini sehingga biaya rata-rata - dari transaksi di mana Anda sebagai penerima dan transaksi yang diprakarsai - mendorong para penambang untuk menyertakan kedua transaksi tersebut ke dalam satu blok.



⚠️ Transaksi pertama harus dimasukkan dalam blok agar transaksi kedua dapat dikonfirmasi.



Jika semua istilah ini tampak terlalu teknis, saya sarankan Anda [membaca daftar istilah kami](https://planb.academy/resources/glossary), yang berisi definisi semua istilah teknis yang terkait dengan Bitcoin dan ekosistemnya.



Selain metode-metode ini, Mempool.space, berkat koneksinya dengan lebih dari 80% penambang yang ada di jaringan Bitcoin, juga memungkinkan Anda untuk mempercepat transaksi **belum dikonfirmasi** Anda, bahkan yang tidak mengaktifkan RBF, dengan memberikan pertimbangan kepada para penambang di Exchange untuk memasukkan transaksi berbiaya rendah Anda ke dalam blok berikutnya yang siap untuk ditambang.



Pada halaman detail transaksi, klik tombol **Accelerate**, lalu lanjutkan dengan membayar rekanan Anda ke penambang.



![accelerate-section](assets/fr/11.webp)


## Anak di bawah umur



Sebuah Miner mengacu pada seseorang yang mengelola tambang, yaitu komputer yang terlibat dalam proses Mining, yang terdiri dari partisipasi dalam Proof-of-Work. Miner mengelompokkan transaksi yang tertunda dalam Mempool-nya untuk membentuk sebuah blok kandidat. Kemudian ia mencari Hash yang valid, kurang dari atau sama dengan target, untuk header blok ini dengan memodifikasi berbagai nonce. Jika ia menemukan Hash yang valid, ia akan menyiarkan bloknya ke jaringan Bitcoin dan mengantongi imbalan uang yang terkait, yang terdiri dari subsidi blok (pembuatan bitcoin baru ex-nihilo), dan biaya transaksi.



https://planb.academy/courses/ce272232-0d97-4482-884a-0f77a2ebc036

❗Penambang seperti "validator" yang memverifikasi dan mengelompokkan transaksi ke dalam blok. Untuk menambahkan blok baru ke jaringan Bitcoin, mereka harus memecahkan teka-teki matematika yang rumit (Proof-of-Work). Miner pertama yang berhasil memecahkan teka-teki tersebut akan mendapatkan hadiah Bitcoin (hibah blok + biaya untuk transaksi yang termasuk dalam blok tersebut).



Tingkat kesulitan Proof of Work ini dimonitor, sehingga Anda dapat memvisualisasikan evolusi daya komputasi yang diperlukan untuk penambang. Anda akan menemukannya di bagian di bawah ini:





- Perkiraan total reward yang didapatkan oleh para penambang selama penyesuaian tingkat kesulitan terakhir, serta perkiraan Halving berikutnya dari block grant, yang terjadi setiap 210.000 blok (sekitar 04 tahun).



![rewards](assets/fr/12.webp)



Tingkat kesulitan ini disesuaikan setiap 2016 blok (sekitar dua minggu). Hal ini berbanding terbalik dengan waktu rata-rata yang dibutuhkan oleh para penambang untuk mencapai Miner setiap 2016 blok.


Ketika waktu rata-rata yang dibutuhkan oleh para penambang kurang dari 10 menit, maka tingkat kesulitannya meningkat, yang membuktikan bahwa lebih mudah bagi para penambang untuk memvalidasi blok Miner. Sebaliknya, ketika waktu rata-rata yang dibutuhkan lebih besar dari 10 menit, maka tingkat kesulitannya menurun.



![mining-pool](assets/fr/13.webp)





- Kelompok penambang: Mengingat tingkat kesulitan yang ada, sekelompok penambang berkolaborasi untuk membantu menemukan Proof of Work di Bitcoin, dalam apa yang kami sebut sebagai **pool**. Ketika sebuah blok ditambang oleh kelompok, reward yang diperoleh akan didistribusikan sesuai dengan persentase keberhasilan dalam pencarian solusi parsial setiap Miner, yaitu kontribusi daya komputasi dalam pencarian Proof-of-Work, atau sesuai dengan metode remunerasi yang telah disepakati oleh kerjasama.





![mining](assets/fr/14.webp)



## Infrastruktur Lightning Network



Mempool tidak hanya memberikan informasi tentang infrastruktur jaringan Bitcoin (rantai utama). Alat ini juga mengintegrasikan alat visualisasi dan eksplorasi untuk hamparan Lightning Bitcoin.



Di bagian **Lightning**, Anda bisa melihat semua koneksi yang ada di antara node Lightning.



![network-stats](assets/fr/15.webp)



Interface ini memberikan informasi tentang :





- Statistik Lightning Network.



![distribution](assets/fr/16.webp)




⚠️ **PENTING**: Kapasitas saluran pembayaran menunjukkan jumlah maksimum yang dapat dikirim oleh sebuah node ke node lain selama transaksi Lightning.





- Node Lightning dialokasikan menurut penyedia layanan Internet (layanan hosting) dan secara opsional menurut kapasitas saluran pembayaran.



![distribution](assets/fr/17.webp)





- Sejarah kapasitas keseluruhan Lightning Network.


Anda juga akan menemukan peringkat node-node ini sesuai dengan kapasitas saluran pembayaran mereka.



![ranking](assets/fr/18.webp)



## Lebih banyak grafik



Mempool.space adalah platform yang ideal untuk menikmati interaksi dengan jaringan protokol Bitcoin. Grafik tidak hanya menyediakan data visual untuk membantu Anda memutuskan kapan harus melakukan transaksi, tetapi juga parameter yang tepat sehingga Anda dapat memvisualisasikan, secara real time, kekuatan dan kesehatan jaringan Bitcoin dan infrastruktur Lightning yang terkait.



Pada bagian **Grafik**, Anda dapat melihat data penting tentang jaringan Bitcoin:




- Evolusi ukuran Mempool: Anda dapat mengamati bagaimana ukuran Mempool berfluktuasi, yang dapat mengindikasikan periode aktivitas tinggi atau rendah pada jaringan.



![graphs](assets/fr/19.webp)






- Evolusi transaksi dan biaya transaksi pada jaringan yang dipilih: Dengan melacak variasi transaksi per detik, Anda dapat mengantisipasi periode kemacetan atau aktivitas rendah, dan mengoptimalkan biaya transaksi Anda. Grafik ini memberi Anda perspektif tentang kapasitas jaringan untuk menangani volume transaksi.



![graphs](assets/fr/20.webp)



Sekarang Anda telah mencapai akhir perjalanan Anda di Mempool.space, jadilah penjelajah Anda sendiri dan lacak transaksi Anda secara real time. Silakan baca artikel kami tentang penjelajah **Public Pool** Bitcoin di bawah ini.



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1