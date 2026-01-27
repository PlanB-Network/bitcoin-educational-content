---
name: Mempool
description: Jelajahi seluruh ekosistem Bitcoin.
---

![cover](assets/cover.webp)



Protokol Bitcoin adalah jaringan terdesentralisasi yang bersifat pseudonim dan terbuka untuk dilihat siapa saja. Para anggota (node), yaitu komputer yang menjalankan perangkat lunak Bitcoin, punya akses penuh ke semua data yang dipublikasikan di Bitcoin. Tapi, di tahun-tahun awal Bitcoin, protokol ini belum bisa diakses luas seperti sekarang.

Di masa awal itu, kamu harus menjalankan node Bitcoin untuk memakai alat yang tepat (bitcoin-cli) agar bisa menginterogasi jaringan lewat baris perintah.



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Karena itu, berbagai proyek mulai bermunculan untuk memperluas komunitas Bitcoin agar siapa saja yang tidak punya node dan/atau tidak punya keterampilan teknis yang dibutuhkan tetap bisa mengaksesnya dengan mudah.



Dalam tutorial ini, kita akan melihat proyek **Mempool.space**, fitur-fiturnya, dan dampak yang ditimbulkannya terhadap ekosistem Bitcoin.



## Apa itu Mempool.space?



**Mempool.space** adalah penjelajah open source yang menyediakan informasi berguna tentang transaksi, biaya transaksi, blok, dan para penambang di berbagai jaringan protokol Bitcoin. Diluncurkan pada 2020, aplikasi ini membawa peningkatan besar dalam pengalaman pengguna lewat grafik yang jelas, animasi yang halus, dan antarmuka yang rapi.

Untuk memahami proyek ini, Mempool (kumpulan memori) adalah ruang virtual tempat semua transaksi yang menunggu konfirmasi di jaringan Bitcoin disimpan. Mempool itu seperti ruang tunggu tempat transaksi Bitcoin menunggu untuk dikonfirmasi. Setiap komputer di jaringan (node) punya ruang tunggu sendiri, dan ini menjelaskan kenapa tidak semua transaksi bisa terlihat oleh semua orang pada waktu yang sama.

Dampak utama platform ini dalam ekosistem Bitcoin adalah memungkinkan kamu mengakses beragam informasi dari area memori sebagian besar node Bitcoin tanpa perlu menjalankannya sendiri. Mempool.space adalah tempat untuk melihat dan menelusuri jaringan protokol Bitcoin.

Penggunaannya yang semakin luas di ekosistem, ditambah fakta bahwa Mempool.space bersifat open source, membuatnya bisa diintegrasikan ke lebih banyak sistem hosting pribadi. Sekarang kamu bisa menjalankan instans Mempool.space milik kamu sendiri langsung di node pribadi. Lihat tutorial kami tentang cara mengonfigurasi Mempool.space di node Umbrel kamu di bawah ini.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Dasar-dasar Mempool.space



Seperti yang telah disebutkan di atas, [Mempool.space](https://Mempool.space) adalah penjelajah protokol Bitcoin yang memungkinkan Anda untuk memonitor transaksi Anda dan penyebarannya di jaringan Bitcoin yang dipilih secara real time, dari sebuah grafis Interface.



Mempool.space mendukung banyak jaringan protokol Bitcoin.


Pada bilah menu, kamu akan menemukan jaringan berikut ini:




- **Mainnet**: Jaringan Bitcoin utama tempat transaksi Bitcoin yang sebenarnya terjadi.
- **Signet**: Jaringan uji coba yang menggunakan tanda tangan digital untuk memvalidasi blok tanpa memerlukan sumber daya yang dibutuhkan oleh jaringan utama.
- **Testnet 3**: Jaringan pengujian dan pengembangan bebas risiko pada protokol Bitcoin.
- **Testnet 4**: Versi baru Testnet 3 menghadirkan stabilitas yang lebih baik dan aturan konsensus baru ke lingkungan pengujian.



![reseaux](assets/fr/01.webp)



Pada halaman beranda, di sebelah kiri berwarna hijau, kamu akan melihat blok-blok potensial di masa depan yang siap untuk divalidasi dan diintegrasikan (ditambang) ke dalam jaringan Bitcoin. Secara rata-rata, satu blok ditambang setiap sepuluh menit, simpan informasi ini karena akan sangat berguna nantinya dalam pengembangan pembahasan kita.

Di sisi kanan, dengan warna keunguan, kamu akan menemukan blok-blok terakhir yang telah ditambang di Bitcoin, di mana nomor blok terbaru merepresentasikan ketinggian jaringan saat ini.



![blocs](assets/fr/02.webp)



Bagian **Biaya Transaksi** adalah perkiraan biaya transaksi. Semakin tinggi biaya yang kamu alokasikan untuk transaksi kamu, semakin besar kemungkinan transaksi tersebut akan dimasukkan ke dalam blok berikutnya yang siap untuk ditambang.

Biaya transaksi adalah biaya yang akan diambil oleh miner dari kamu untuk memasukkan transaksi kamu ke dalam blok kandidat untuk mining. Biaya ini ditentukan oleh rasio sat/vB (satoshi per virtual byte), yang merepresentasikan jumlah satoshi yang kamu bayarkan untuk ruang yang akan ditempati oleh transaksi kamu di dalam blok kandidat.

⚠️ PENTING: Jika terjadi kejenuhan mempool, miner akan memprioritaskan transaksi yang menawarkan rasio sat/vB terbaik. Semakin berat atau besar transaksi kamu, semakin banyak satoshi yang perlu kamu sertakan agar transaksi tersebut dapat diproses dengan cepat.



![fees-visualizer](assets/fr/03.webp)



Bagian **Mempool Goggles** memungkinkan Anda memvisualisasikan ruang yang ditempati oleh suatu transaksi.



![mempool](assets/fr/04.webp)



Sebuah blok ditambang kira-kira setiap sepuluh menit karena tingkat kesulitan Proof of Work yang harus dipenuhi oleh para penambang untuk menambahkan blok kandidat mereka ke dalam rantai blok. Tingkat kesulitan ini menyesuaikan setiap **2016 blok**, yang setara dengan sekitar **2 minggu**. Kamu dapat melihat evolusi tingkat kesulitan ini di sini.



![difficulty](assets/fr/05.webp)



Penambahan blok baru ke rantai utama memberikan hak kepada Miner dari blok yang divalidasi untuk mendapatkan hadiah yang terdiri dari bagian tetap (dibelah dua setiap 210.000 blok**, setara dengan sekitar 4 tahun** selama pembagian) dan biaya transaksi.



![halving](assets/fr/06.webp)



## Mengakses detail transaksi Anda



Pada bilah pencarian Mempool.space, kamu dapat memasukkan alamat Bitcoin atau transaction ID untuk mengetahui lebih lanjut tentang riwayat kamu.



![search](assets/fr/07.webp)



Pada halaman detail transaksi, kamu akan menemukan informasi umum mengenai transaksi kamu:



- **Status**: Dikonfirmasi saat ditambahkan ke blok, belum dikonfirmasi saat menunggu di Mempool.
- Biaya transaksi.
- **Perkiraan waktu kedatangan (ETA)**: Perkiraan waktu yang diperlukan agar transaksi kamu ditambahkan ke dalam blok. Ini dihitung berdasarkan rasio yang merupakan biaya yang terkait dengan transaksi ini.



![general-txinfo](assets/fr/08.webp)



Bagian **Flow** menunjukkan grafik komponen transaksi Anda.



Input (sebelumnya UTXO), digunakan untuk transaksi kamu, dan output yang memberikan hak kepada penerima untuk menggunakan bitcoin dari setiap output dengan menunjukkan tanda tangan yang diperlukan untuk pengeluaran mereka.



![flow](assets/fr/09.webp)



Rincian lebih lanjut mengenai alamat yang digunakan dapat ditemukan di bagian **Input & Output**.



![address](assets/fr/10.webp)



Temukan berbagai skema transaksi Bitcoin untuk meningkatkan kerahasiaan kamu.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Mempercepat transaksi Anda



Dalam ekosistem Bitcoin, proses validasi transaksi oleh miner secara intrinsik terkait dengan biaya transaksi yang melekat pada transaksi tersebut. Miner memprioritaskan transaksi dengan rasio biaya yang lebih tinggi (satoshi/vB), yang dapat memengaruhi apakah transaksi kamu akan segera diproses jika kamu tidak membayar biaya yang wajar dan dapat diterima oleh miner. Dalam kondisi ini, transaksi kamu akan tertahan di mempool sambil menunggu adanya blok yang menerima rasio biaya tersebut.


Untungnya, ada dua metode yang tersedia di jaringan Bitcoin untuk mempercepat konfirmasi transaksi kamu.





- **RBF** - Replacement by Fee: Metode yang memungkinkan kamu untuk membelanjakan input yang sama dari transaksi berbiaya rendah kamu, tetapi kali ini dengan meningkatkan biaya transaksi untuk mempercepat validasi. Transaksi baru kamu akan divalidasi lebih cepat dan dimasukkan ke dalam blok, sehingga transaksi dengan biaya rendah sebelumnya akan dibatalkan.

Kamu dapat melakukan penggantian biaya ini menggunakan wallet yang mendukung mekanisme tersebut. Sebagai contoh, lihat artikel kami tentang wallet BlueWallet.


https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- **CPFP** - Child pay for parent: Pendekatan yang terinspirasi oleh RBF, tetapi dari sisi penerima. Ketika transaksi di mana kamu berperan sebagai penerima tertahan di mempool, kamu memiliki opsi untuk membelanjakan output (UTXO) dari transaksi tersebut, meskipun transaksi itu belum dikonfirmasi, dengan mengalokasikan biaya yang lebih tinggi pada transaksi baru ini. Dengan cara ini, biaya rata-rata dari transaksi saat kamu menjadi penerima dan transaksi yang kamu inisiasi akan cukup menarik bagi miner untuk menyertakan kedua transaksi tersebut ke dalam satu blok.



⚠️ Transaksi pertama harus dimasukkan dalam blok agar transaksi kedua dapat dikonfirmasi.



Jika semua istilah ini tampak terlalu teknis, aku sarankan kamu [membaca daftar istilah kami](https://planb.academy/resources/glossary), yang berisi definisi semua istilah teknis yang terkait dengan Bitcoin dan ekosistemnya.



Selain metode-metode tersebut, Mempool.space, berkat koneksinya dengan lebih dari 80% penambang di jaringan Bitcoin, juga memungkinkan kamu untuk mempercepat transaksi **belum dikonfirmasi** kamu, termasuk transaksi yang tidak mengaktifkan RBF, dengan memberikan pertimbangan kepada para penambang di exchange agar memasukkan transaksi berbiaya rendah kamu ke dalam blok berikutnya yang siap untuk ditambang.


Pada halaman detail transaksi, klik tombol **Accelerate**, lalu lanjutkan dengan membayar rekanan Anda ke penambang.



![accelerate-section](assets/fr/11.webp)


## Anak di bawah umur



Seorang miner mengacu pada individu atau entitas yang mengoperasikan mesin penambangan, yaitu komputer yang terlibat dalam proses mining dan berpartisipasi dalam mekanisme Proof of Work. Miner mengelompokkan transaksi yang tertunda di mempool mereka untuk membentuk sebuah blok kandidat. Selanjutnya, mereka mencari hash yang valid, kurang dari atau sama dengan target, untuk header blok tersebut dengan memodifikasi berbagai nonce. Jika hash yang valid ditemukan, blok tersebut akan disiarkan ke jaringan Bitcoin dan miner akan menerima imbalan yang terkait, yang terdiri dari subsidi blok (penciptaan bitcoin baru secara ex nihilo) dan biaya transaksi.



https://planb.academy/courses/ce272232-0d97-4482-884a-0f77a2ebc036

❗Penambang seperti "validator" yang memverifikasi dan mengelompokkan transaksi ke dalam blok. Untuk menambahkan blok baru ke jaringan Bitcoin, mereka harus memecahkan teka-teki matematika yang rumit (Proof-of-Work). Miner pertama yang berhasil memecahkan teka-teki tersebut akan mendapatkan hadiah Bitcoin (hibah blok + biaya untuk transaksi yang termasuk dalam blok tersebut).



Tingkat kesulitan Proof of Work ini dimonitor, sehingga kamu dapat memvisualisasikan evolusi daya komputasi yang diperlukan untuk penambang. Kamu akan menemukannya di bagian di bawah ini:





- Perkiraan total reward yang didapatkan oleh para penambang selama penyesuaian tingkat kesulitan terakhir, serta perkiraan Halving berikutnya dari block grant, yang terjadi setiap 210.000 blok (sekitar 04 tahun).



![rewards](assets/fr/12.webp)



Tingkat kesulitan ini disesuaikan setiap 2016 blok, atau sekitar dua minggu. Penyesuaian ini berbanding terbalik dengan waktu rata-rata yang dibutuhkan para penambang untuk menambang blok selama periode 2016 blok tersebut.

Ketika waktu rata-rata yang dibutuhkan para penambang kurang dari 10 menit, tingkat kesulitan akan meningkat, yang menunjukkan bahwa para penambang relatif lebih mudah memvalidasi blok. Sebaliknya, ketika waktu rata-rata yang dibutuhkan lebih dari 10 menit, tingkat kesulitan akan menurun.



![mining-pool](assets/fr/13.webp)





- Kelompok penambang: Mengingat tingkat kesulitan yang ada, para penambang dapat berkolaborasi untuk membantu menemukan Proof of Work di Bitcoin, dalam apa yang disebut sebagai pool. Ketika sebuah blok berhasil ditambang oleh kelompok tersebut, reward yang diperoleh akan didistribusikan sesuai dengan persentase kontribusi setiap miner dalam pencarian solusi parsial, yaitu berdasarkan daya komputasi yang disumbangkan dalam proses Proof of Work, atau mengikuti metode remunerasi yang telah disepakati dalam kerja sama tersebut.





![mining](assets/fr/14.webp)



## Infrastruktur Lightning Network



Mempool tidak hanya memberikan informasi tentang infrastruktur jaringan Bitcoin (rantai utama). Alat ini juga mengintegrasikan alat visualisasi dan eksplorasi untuk hamparan Lightning Bitcoin.



Di bagian **Lightning**, kamu bisa melihat semua koneksi yang ada di antara node Lightning.



![network-stats](assets/fr/15.webp)



Interface ini memberikan informasi tentang :





- Statistik Lightning Network.



![distribution](assets/fr/16.webp)




⚠️ **PENTING**: Kapasitas saluran pembayaran menunjukkan jumlah maksimum yang dapat dikirim oleh sebuah node ke node lain selama transaksi Lightning.





- Node Lightning dialokasikan menurut penyedia layanan Internet (layanan hosting) dan secara opsional menurut kapasitas saluran pembayaran.



![distribution](assets/fr/17.webp)





- Sejarah kapasitas keseluruhan Lightning Network.


Kamu juga akan menemukan peringkat node-node ini sesuai dengan kapasitas saluran pembayaran mereka.



![ranking](assets/fr/18.webp)



## Lebih banyak grafik



Mempool.space adalah platform yang ideal untuk berinteraksi dengan jaringan protokol Bitcoin. Grafik yang disediakan tidak hanya menampilkan data visual untuk membantu kamu menentukan waktu terbaik dalam melakukan transaksi, tetapi juga parameter yang relevan sehingga kamu dapat memvisualisasikan, secara real time, kekuatan dan kesehatan jaringan Bitcoin serta infrastruktur Lightning yang terkait.


Pada bagian **Grafik**, kamu dapat melihat data penting tentang jaringan Bitcoin:




- Evolusi ukuran Mempool: Kamu dapat mengamati bagaimana ukuran Mempool berfluktuasi, yang dapat mengindikasikan periode aktivitas tinggi atau rendah pada jaringan.



![graphs](assets/fr/19.webp)






- Evolusi transaksi dan biaya transaksi pada jaringan yang dipilih: Dengan melacak variasi jumlah transaksi per detik, kamu dapat mengantisipasi periode kemacetan atau aktivitas rendah, lalu mengoptimalkan biaya transaksi kamu. Grafik ini memberikan perspektif mengenai kapasitas jaringan dalam menangani volume transaksi.


![graphs](assets/fr/20.webp)



Sekarang kamu telah mencapai akhir perjalanan kamu di Mempool.space, saatnya menjadi penjelajah kamu sendiri dan melacak transaksi kamu secara real time. Silakan baca artikel kami tentang penjelajah Public Pool Bitcoin di bawah ini.


https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1
