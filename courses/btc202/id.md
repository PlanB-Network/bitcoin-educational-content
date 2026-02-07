---
name: Menyiapkan node Bitcoin pertama Anda
goal: Memahami, memasang, mengonfigurasi, dan menggunakan node Bitcoin
objectives: 

  - Memahami peran dan tujuan node Bitcoin.
  - Mengidentifikasi berbagai solusi perangkat keras dan perangkat lunak yang tersedia.
  - Memasang dan mengkonfigurasi Full node (Bitcoin core).
  - Gunakan Interface Umbrel dan tambahkan aplikasi yang berguna.
  - Hubungkan Wallet pribadi ke simpulnya sendiri.
  - Jelajahi pengaturan lanjutan dan praktik keamanan terbaik.

---
# Menjadi seorang bitcoiner yang berdaulat

Anda mungkin sudah familiar dengan pepatah "Tidak ada kunci Anda, tidak ada koin Anda" (Not your keys, not your coins), yang mendorong penyimpanan mandiri (self-custody) atas Bitcoin Anda. Memegang kunci Anda sendiri memang merupakan langkah pertama yang penting, tetapi itu tidak cukup. Untuk mencapai kedaulatan moneter sejati, Anda juga perlu memasang dan menjalankan Node Bitcoin Anda sendiri. Kursus ini dirancang untuk memandu Anda melalui langkah mendasar dalam perjalanan Bitcoin Anda!

BTC202 adalah kursus yang mudah diakses yang dirancang untuk mengajari Anda cara menjalankan Node Bitcoin Anda sendiri, bahkan jika Anda bukan seorang ahli teknis. Kita akan mulai dengan mendefinisikan apa itu Node Bitcoin, apa fungsinya, dan mengapa menjalankan satu node secara pribadi sangat penting. Setelah itu, saya akan memandu Anda langkah demi langkah dalam memilih perangkat keras Anda (hardware), memasang perangkat lunak yang diperlukan (software), menghubungkan perangkat lunak wallet Anda, dan melakukan optimasi awal yang mungkin untuk melangkah lebih jauh.

Menjalankan Node Bitcoin bukan sekadar pilihan bagi para ahli; itu adalah suatu keharusan. Ini adalah alat ketahanan (resilience tool) yang perlu dipahami dan diimplementasikan oleh setiap pengguna. Kursus ini adalah titik awal Anda untuk menjadi bitcoiner yang berdaulat!

+++

# Pendahuluan

<partId>fc46ccd7-5d6d-40c3-9e9f-fbbb323c760a</partId>

## Gambaran umum kursus

<chapterId>916b1f86-38a4-4ede-bdb7-83841d5a7abe</chapterId>

Selamat datang di BTC 202, di mana Anda akan belajar cara memasang, mengonfigurasi, dan menggunakan Node Bitcoin dengan mudah dan mandiri. Namun, bukan hanya itu: Anda juga akan belajar lebih banyak tentang lokasi dan fungsi node dalam sistem Bitcoin. Kursus ini bergantian antara penjelasan teoretis dan praktik langsung yang dibimbing.

### Bagian 1 - Pendahuluan

Pada bagian pertama kursus ini, kita akan menjelaskan gagasan dasar dan kemudian melanjutkan ke definisi yang lebih tepat. Apa itu node? Apa perbedaan antara node, wallet (wallet), dan miner (penambang)? Anda kemudian akan belajar tentang Bitcoin Core dan implementasi protokol. Tujuannya adalah untuk berbicara dalam bahasa yang sama, menghindari kebingungan, dan membangun fondasi teoretis yang kuat.

### Bagian 2 - Menjadi pengguna bitcoin yang berdaulat

Pada bagian kedua ini, saya akan mulai dengan menjelaskan mengapa penting untuk menjalankan Node Bitcoin Anda sendiri. Kita kemudian akan menjelajahi berbagai jenis node yang ada (lengkap, pruned, SPV...), cara kerjanya, dan implikasi teknisnya.

Kami kemudian akan memberi Anda gambaran umum tentang perangkat lunak yang tersedia untuk menjalankan Node Bitcoin, termasuk kelebihan dan kekurangannya. Akhirnya, kami akan menyimpulkan dengan beberapa rekomendasi yang sangat praktis untuk memilih perangkat keras (hardware) yang tepat untuk kebutuhan dan anggaran Anda.

Oleh karena itu, bagian ini mengilustrasikan jalur bitcoiner yang berdaulat: memahami mengapa menjalankan node itu perlu, memilih jenis node, berdasarkan pilihan ini, memilih perangkat lunak, dan, tergantung pada perangkat lunak yang dipilih, menentukan perangkat keras yang sesuai.

### Bagian 3 - Memasang node Bitcoin dengan mudah

Setelah persiapan ini selesai, saatnya untuk menjadi praktis dengan Bagian 3 yang dikhususkan untuk Umbrel: OS home cloud yang menyederhanakan self-hosting serta pemasangan node Bitcoin dan Lightning.

Setelah pengenalan singkat tentang Umbrel, kami akan memberikan tutorial terperinci untuk memandu Anda melalui proses instalasi dan konfigurasi pada mesin DIY (rakitan sendiri) Anda sendiri. Tujuan dari bagian ini jelas: untuk memiliki Node Bitcoin pertama Anda yang berfungsi penuh dan tersinkronisasi.

### Bagian 4 - Menghubungkan Wallet Anda ke node Anda

Sekarang setelah Anda mengatur Node Bitcoin, saatnya untuk menggunakannya! Di bagian ini, Anda akan belajar cara menghubungkan perangkat lunak manajemen wallet Anda (seperti Sparrow wallet) ke pengindeks alamat Anda sendiri (Electrs atau Fulcrum), atau langsung ke Bitcoin Core, sehingga Anda tidak lagi bergantung pada server publik.

Kami juga akan menguji peran indexer dan berbagai metode koneksi ke node Anda (LAN, Tor, Tailscale, dll.). Akhirnya, di bab terakhir, kami akan meninjau aplikasi paling berguna yang tersedia di Umbrel untuk bitcoiner sehari-hari.

### Bagian 5 - Konsep lanjutan dan praktik terbaik

Di bagian akhir BTC 202 ini, tujuannya adalah untuk memperdalam pengetahuan Anda. Pertama, kita akan melihat praktik terbaik yang harus diterapkan dengan Node Bitcoin baru Anda dan cara memeliharanya dalam jangka panjang.

Kita kemudian akan meluangkan waktu untuk meninjau beberapa teori yang dibahas sebelumnya dalam kursus, termasuk memahami proses IBD (Initial Block Download) dan peer discovery secara rinci, menjelajahi anatomi node, dan akhirnya belajar cara menggunakan file Bitcoin.conf untuk menyempurnakan pengaturan Anda.

### Bagian 6 - Bagian akhir

Seperti semua kursus Plan ₿ Academy, di bagian akhir Anda akan menemukan ujian akhir untuk menguji pengetahuan Anda tentang Node Bitcoin.

Jadi, apakah Anda siap untuk menyalakan Node Bitcoin pertama Anda? Tetapkan arah menuju kedaulatan!

## Apa yang dimaksud dengan node Bitcoin?

<chapterId>0a9fd4e0-94ab-405e-924c-023397393027</chapterId>

Seperti yang dijelaskan oleh penciptanya, Satoshi Nakamoto, Bitcoin memperkenalkan diri sebagai sistem uang elektronik peer-to-peer. Kalimat sederhana ini, yang merupakan judul White Paper, mengandung banyak petunjuk tentang sifat Bitcoin:

- Pertama, Satoshi mendeskripsikan Bitcoin sebagai "sistem", dengan kata lain, satu set komponen perangkat keras (hardware) dan perangkat lunak (software) yang koheren yang berinteraksi untuk menyediakan layanan atau menjalankan fungsi tertentu;
- Selanjutnya, ia menjelaskan bahwa sistem ini memungkinkan penggunaan uang elektronik, yaitu bentuk mata uang tak berwujud;
- Terakhir, ia menunjukkan bahwa sistem ini tidak bergantung pada entitas pusat apa pun: Sistem ini bersifat peer-to-peer, artinya pengguna sendirilah yang mengoperasikan sistem tersebut.

Karena Bitcoin adalah sebuah sistem, ia harus dijalankan pada komputer. Dan, karena sifatnya yang peer-to-peer, para pengguna sendirilah yang bertanggung jawab untuk menjalankan mesin-mesin ini. Apa yang kita sebut sebagai "Node Bitcoin" adalah komputer tempat menjalankan lunak yang mengimplementasikan protokol Bitcoin (seperti Bitcoin Core, tetapi kita akan kembali ke sana nanti) berjalan. Inilah yang memungkinkan Bitcoin beroperasi tanpa otoritas pusat: validasi dilakukan secara terdistribusi, oleh ribuan mesin independen milik ribuan pengguna.

![Image](assets/fr/047.webp)

Nakamoto, S. (2008). *Bitcoin: Sistem Uang Elektronik Peer-to-Peer*. https://Bitcoin.org/Bitcoin.pdf

Para pengguna inilah yang memastikan keamanan Bitcoin. Seperti yang dijelaskan oleh Eric Voskuil dalam bukunya *Cryptoeconomics*, keamanan Bitcoin tidak bergantung pada Blockchain, tidak juga pada kekuatan hashing, tidak juga pada validasi, desentralisasi, kriptografi, open source, atau teori permainan. Keamanan Bitcoin bergantung terutama pada individu yang bersedia mengekspos diri mereka sendiri terhadap risiko pribadi. Desentralisasi memungkinkan risiko ini tersebar ke sejumlah besar individu, dan hanya kemampuan mereka untuk menolak yang memastikan ketahanan sistem.

Justru para pengguna inilah yang memastikan keamanan Bitcoin. Seperti yang dijelaskan Eric Voskuil dalam bukunya _Cryptoeconomics_, keamanan Bitcoin tidak bergantung pada Blockchain, kekuatan hashing, validasi, desentralisasi, kriptografi, open source, atau teori permainan. Keamanan Bitcoin terutama bergantung pada individu-individu yang bersedia mengekspos diri pada risiko pribadi. Desentralisasi memungkinkan risiko ini disebarkan ke sejumlah besar individu, dan hanya kemampuan mereka untuk menahanlah yang menjamin ketahanan sistem.

Prinsip ini mudah dipahami: jika Bitcoin bergantung pada satu node tunggal yang dimiliki oleh satu orang, memenjarakan orang itu sudah cukup untuk mematikan jaringan, karena mereka sendirilah yang menanggung semua risiko. Dengan puluhan ribu node yang tersebar di seluruh dunia, risikonya tersebar: setiap operator ini harus dinetralkan untuk mematikan Bitcoin.

![Image](assets/fr/048.webp)

Dengan demikian, Kita dapat membedakan dan menamakan beberapa konsep untuk memperjelas berbagai hal dalam kursus ini:

- Mata uang Bitcoin: unit hitung yang digunakan untuk transaksi di dalam sistem ini;
- Jaringan Bitcoin: kumpulan semua node yang terhubung;
- Node Bitcoin: mesin yang menjalankan implementasi Bitcoin;
- Implementasi Bitcoin: perangkat lunak yang menerjemahkan protokol menjadi instruksi yang dapat dieksekusi;
- Protokol Bitcoin: serangkaian aturan yang mengatur operasi sistem;
- Sistem Bitcoin: kombinasi koheren dari semua elemen ini.

### Peran node Bitcoin

Node Bitcoin secara kolektif membentuk apa yang dikenal sebagai Jaringan Bitcoin. Jaringan ini memungkinkan seluruh sistem beroperasi secara otonom, tanpa perlu menggunakan otoritas pusat atau hierarki server.

Sejak awal, Bitcoin dirancang untuk memungkinkan setiap pengguna menjalankan node pribadi. Kasus ini tetap valid dengan perangkat lunak Bitcoin Core saat ini, yang menggabungkan peran wallet dan node. Namun saat ini, fungsi ini sering dipisahkan: banyak wallet Bitcoin modern hanyalah wallet yang terhubung ke node eksternal (milik orang yang sama atau bukan).

### Mengamankan Blockchain

Tugas pertama node adalah memelihara salinan lokal dari Blockchain. Untuk mencegah double-spending pada Bitcoin tanpa melibatkan otoritas pusat, setiap pengguna harus memeriksa bahwa tidak ada transaksi yang sudah ada dalam sistem. Satu-satunya cara untuk yakin akan hal ini adalah dengan mengetahui semua transaksi yang telah dilakukan di Bitcoin. Untuk alasan ini, semua transaksi diberi timestamp dan dikelompokkan ke dalam blok, dan setiap node menyimpan seluruh Blockchain.

> "Satu-satunya cara untuk mengkonfirmasi tidak adanya transaksi adalah dengan mengetahui semua transaksi." 

Nakamoto, S. (2008). *Bitcoin: Sistem Uang Elektronik Peer-to-Peer*. https://Bitcoin.org/Bitcoin.pdf

Blockchain merupakan sebuah tabel yang terus berkembang: setiap kali blok baru diterbitkan oleh miner, node memeriksa validitasnya sebelum menambahkannya ke salinan chain lokalnya. Hingga saat ini (Juli 2025), Blockchain lengkap melebihi 675 GB, dan ukuran ini terus bertambah, karena blok baru ditambahkan rata-rata setiap 10 menit.

![Image](assets/fr/049.webp)

Node juga memelihara catatan lokal dari semua UTXO yang ada pada waktu tertentu, yang dikenal sebagai **UTXO set**. Database ini berisi semua fragmen Bitcoin yang belum terpakai. Kita akan meninjau subjek ini secara rinci di bagian akhir kursus.

### Memverifikasi dan mendistribusikan transaksi

Peran kedua node adalah memastikan verifikasi dan penyebaran transaksi. Ketika transaksi baru mencapai node (baik melalui perangkat lunak wallet atau node lain), node akan memeriksa apakah transaksi itu mematuhi serangkaian aturan (aturan konsensus dan aturan relay). Contohnya:

- Bitcoin yang digunakan harus ada dalam UTXO set-nya (database output yang belum digunakan);
- signature harus valid, dan semua kondisi pengeluaran harus dipenuhi (valid script);
- jumlah total output tidak boleh melebihi jumlah total input, yang berarti biaya tidak boleh negatif.

![Image](assets/fr/050.webp)

Setelah validasi, transaksi disimpan dalam Mempool node, ruang memori sementara yang disediakan untuk transaksi yang belum dikonfirmasi, dan kemudian diteruskan ke peer jaringan lain yang terhubung dengannya. Mekanisme distribusi dan validasi ini berlanjut dari node ke node. Dengan cara ini, transaksi disebarkan ke seluruh Jaringan Bitcoin, dan setiap node menyimpannya di Mempool hingga dimasukkan ke dalam blok yang valid oleh miner, yang kemudian bertindak berdasarkan konfirmasi pertamanya.

### Memeriksa dan mendistribusikan blok

Peran ketiga node melibatkan pengelolaan blok yang ditambang. Ketika seorang miner menemukan blok baru dengan Proof of Work yang valid, blok itu disiarkan di jaringan. Para node menerimanya, memeriksa bahwa blok tersebut sesuai dengan semua aturan protokol, dan kemudian mengintegrasikannya ke dalam salinan lokal Blockchain mereka jika valid. Seperti halnya transaksi, blok yang baru divalidasi kemudian diteruskan ke semua peer yang terhubung ke node. Proses ini berlanjut hingga semua node di Jaringan Bitcoin mengetahui blok baru tersebut.

![Image](assets/fr/051.webp)

## Apa perbedaan antara node dan Wallet?

<chapterId>de5af634-a628-4b90-b869-468c208e178b</chapterId>

Sangatlah penting untuk membedakan antara dua jenis perangkat lunak yang berbeda saat menggunakan Bitcoin: node dan Wallet.

Node Bitcoin: Seperti yang disebutkan di atas, node adalah perangkat lunak yang berpartisipasi aktif dalam jaringan peer-to-peer. Ia melakukan tiga tugas utama:

- Mencadangkan Blockchain.
- Memvalidasi dan meneruskan transaksi.
- Memvalidasi blok dan relai.

Wallet Bitcoin, di sisi lain, adalah perangkat lunak yang dirancang untuk menyimpan dan mengelola kunci pribadi Anda. Kunci-kunci ini memungkinkan Anda menggunakan Bitcoin Anda dengan memenuhi script penguncian (biasanya melalui signature). Sebuah wallet dapat terhubung ke node (baik lokal maupun jarak jauh) untuk melihat status Blockchain dan menyiarkan transaksi yang dibuatnya, tetapi wallet bukan merupakan partisipan dalam jaringan.

Dalam beberapa kasus, kedua fungsi ini berlangsung berdampingan dalam perangkat lunak yang sama, seperti pada Bitcoin Core, yang berfungsi sebagai full node dan wallet. Namun, banyak program wallet populer (Sparrow, BlueWallet, dll.) memerlukan koneksi ke node eksternal (milik Anda sendiri atau pihak ketiga) untuk menyiarkan transaksi dan menentukan saldo Wallet.

![Image](assets/fr/052.webp)

## Apa perbedaan antara node dan Miner?

<chapterId>d2992614-7ab7-4bf9-81b1-f548cda67257</chapterId>

Pengertian tentang node dan miner sering kali tertukar. Padahal, kedua elemen ini melakukan fungsi yang sangat berbeda dalam sistem.

Pada awalnya, ketika Bitcoin diluncurkan oleh Satoshi Nakamoto pada tahun 2009, setiap pengguna diharapkan untuk berpartisipasi dalam jaringan secara keseluruhan. Oleh karena itu, perangkat lunak Bitcoin yang asli menggabungkan beberapa fungsi sekaligus: ia bertindak sebagai Wallet, sebuah node, dan juga sebagai Miner, yang mampu menghasilkan blok-blok baru. Pada saat itu, tingkat kesulitan Mining sangat rendah. Anda hanya perlu menjalankan perangkat lunak Bitcoin di komputer Anda untuk menemukan blok dan menerima Bitcoin sebagai hadiah.

Namun, dengan popularisasi Bitcoin secara bertahap dan peningkatan jumlah miner, lanskap persaingan dalam mining telah mengalami perubahan signifikan. Saat ini, mining telah menjadi aktivitas yang sangat kompetitif, didominasi oleh pemain industri yang dilengkapi dengan infrastruktur khusus. Daya yang dibutuhkan untuk menambang blok baru kini sangat besar sehingga hampir tidak mungkin bagi pengguna individu untuk mencapainya hanya dengan menggunakan komputer konvensional. Akibatnya, mining kini terutama dilakukan menggunakan mesin khusus yang disebut ASIC (_Application-Specific Integrated Circuits_). Chip ini dioptimalkan secara eksklusif untuk menjalankan double SHA-256, algoritma yang digunakan untuk mining pada Bitcoin.

![Image](assets/fr/053.webp)

Dalam enghadapi evolusi ini, peran Node Bitcoin dan Miner telah menjadi jelas berbeda. Seperti yang ditunjukkan di atas, peran Node Bitcoin murni bersifat informasional dan berbasis validasi. Peran miner berbeda:

- Miner memilih transaksi yang tertunda di Mempool.
- Miner membangun blok kandidat yang mengintegrasikan transaksi ini.
- Miner mencari proof of work yang valid melalui coba-coba.
- Jika Miner menemukan proof yang valid, Miner menyiarkan blok tersebut melalui node-nya ke node lain.

Seorang miner membutuhkan Node Bitcoin untuk berinteraksi dengan jaringan.

Peran miner juga terkadang dibedakan dari peran pemotong (mincer). Mincer adalah mesin yang tugasnya adalah hashing template blocks yang disediakan oleh server pool, mencari hash yang memenuhi target kesulitan yang ditentukan untuk shares, dan bukan target kesulitan Bitcoin. Sisa dari proses mining, yang mencakup konstruksi blok yang sebenarnya, pemilihan transaksi, atau pencarian proof-of-work sesuai dengan kesulitan Bitcoin sendiri, serta distribusi, dilakukan langsung oleh pool.

![Image](assets/fr/054.webp)

Terakhir, ada perbedaan penting dalam hal insentif ekonomi antara miner dan node. Menjalankan Node Bitcoin tidak memberikan manfaat moneter langsung. Di sisi lain, mengambil bagian dalam mining memberikan hadiah (subsidi dan biaya transaksi) untuk setiap blok yang ditemukan.

Dalam Bagian 2, kita akan menjelajahi lebih detail manfaat praktis dan pribadi dari memasang dan menggunakan Node Bitcoin, di luar manfaat finansialnya saja.

## Bitcoin core dan implementasi protokol

<chapterId>72381876-9317-4faa-8d41-2b252a945b8a</chapterId>

Protokol Bitcoin bukanlah perangkat lunak: ini adalah sekumpulan aturan tersirat (tacit rules) yang dibagikan di antara pengguna jaringan. Protokol ini mendefinisikan kondisi validitas transaksi, mekanisme penciptaan uang, format blok, kondisi proof-of-work, dan banyak spesifikasi lainnya. Untuk berinteraksi dengan protokol ini, pengguna harus menjalankan perangkat lunak yang mengimplementasikan aturan-aturan ini: inilah yang dikenal sebagai **Implementasi** dari Bitcoin.

Oleh karena itu, implementasi adalah perangkat lunak node: program yang mampu berinteraksi dengan mesin lain di Jaringan Bitcoin, mengunduh, memverifikasi, menyimpan, dan menyebarkan blok serta transaksi, dan secara lokal memberlakukan aturan konsensus dan relay. Setiap implementasi adalah interpretasi konkret dari protokol, ditulis dalam bahasa pemrograman tertentu, dengan arsitektur, kinerja, dan ergonominya sendiri. Setiap implementasi juga akan memiliki organisasi pengembangannya sendiri, dengan pembagian tanggung jawabnya.

Di antara semua implementasi ini, ada satu yang paling mendominasi: **Bitcoin core**.

![Image](assets/fr/055.webp)

### Implementasi bersejarah yang telah menjadi tolok ukur

Bitcoin Core adalah perangkat lunak referensi untuk protokol Bitcoin. Ia berasal dari kode asli yang ditulis oleh Satoshi Nakamoto pada 2008-2009, dan merupakan kelanjutan langsung darinya. Awalnya dikenal sebagai "Bitcoin", kemudian _"Bitcoin QT_" (karena penambahan Graphical Interface melalui library Qt), namanya diganti menjadi "Bitcoin Core" pada tahun 2014 untuk membedakan perangkat lunak secara jelas dari jaringan. Sejak versi 0.5, Bitcoin Core didistribusikan dengan dua komponen: Bitcoin-qt (Graphical Interface) dan bitcoind (Command-line Interface).

Secara teori, Bitcoin Core tidak mewakili protokol Bitcoin; melainkan, ini hanyalah salah satu implementasi di antara banyak lainnya. Namun, Bitcoin core dibedakan oleh adopsi masifnya, usianya, kekokohan kodenya, dan ketelitian proses pengembangannya. Akibatnya, dalam praktiknya, aturan yang diterapkan oleh Bitcoin Core secara de facto adalah aturan Protokol Bitcoin: pengguna, pengembang, miner, dan layanan ekosistem merujuk padanya hampir secara eksklusif.

### Distribusi implementasi saat ini

[Menurut data yang dikumpulkan pada Agustus 2025 oleh Luke Dashjr]https://luke.dashjr.org/programs/Bitcoin/files/charts/software.html) (seorang pengembang terkenal di ekosistem), distribusi implementasi di antara node publik jaringan adalah sebagai berikut:

- **Bitcoin Core**: 87.3% dari node
- **Bitcoin Knots**: 12.5%
- Implementasi Kumulatif Lainnya: 0.2% (btcsuite, Bcoin, BTCD...)

![Image](assets/fr/056.webp)

Dengan kata lain, sekitar 9 dari 10 node publik menjalankan Bitcoin Core. Sisa jaringan bergantung pada aplikasi lebih marjinal (meskipun bagian Knots telah meningkat tajam dalam beberapa bulan terakhir). Implementasi alternatif ini sering dikelola oleh satu orang atau tim kecil.

**Catatan**: Angka-angka ini masih berupa perkiraan, karena terutama didasarkan pada _listening nodes_, yaitu node yang menerima koneksi masuk (dengan port 8333 terbuka). Non-listening nodes jauh lebih kompleks untuk dihitung, karena tidak mungkin untuk terhubung langsung dengannya: Anda harus menunggu inisiatif datang dari mereka, dalam bentuk koneksi keluar.
Situs web Luke Dashjr mengklaim mencoba menghitung _non-listening nodes_ ini juga, tetapi tetap tidak mungkin mendapatkan data yang akurat sempurna tentang mereka, dan pembaruan statistik ini pasti akan tertinggal dari kenyataan."

### Pengoperasian internal Bitcoin core

Bitcoin Core adalah perangkat lunak yang ditulis dalam bahasa C++. Ini juga merupakan proyek open-source yang dikelola oleh komunitas pengembang yang merupakan sukarelawan atau didanai oleh berbagai entitas (seringkali perusahaan di dalam ekosistem yang memiliki kepentingan untuk memastikan bahwa pengembangan Core berjalan baik). [Kode tersebut di-host di GitHub](https://github.com/bitcoin/bitcoin), dan pengembangan mengikuti model yang ketat:

- **Kontributor** mengajukan proposal dalam bentuk _pull request_ (PR). Siapa pun pada prinsipnya dapat mengusulkan perubahan, tetapi harus diuji, didokumentasikan, dan melalui proses peninjauan sejawat (peer review).
- **Pengelola** memiliki hak untuk menyetujui dan menggabungkan PR. Merekalah yang menjamin koherensi dan stabilitas proyek. Pada Juli 2025, ada lima maintainer: Hennadii Stepanov, Michael Ford, Andrew Chow, Gloria Zhao, dan Ryan Ofsky.
- Tidak ada **pemelihara utama** sejak Februari 2023. Peran ini awalnya dipegang oleh Satoshi Nakamoto, kemudian oleh Gavin Andresen, dan akhirnya oleh Wladimir J. Van Der Laan dari 2014 hingga 2023.

![Image](assets/fr/057.webp)

Pengembangan Bitcoin Core mengikuti logika meritokratis: kontributor baru didorong untuk meninjau dan menguji kode sebelum mengusulkan perubahan apa pun. Keputusan didasarkan pada konsensus teknis, dan modifikasi besar (terutama dalam area konsensus) memerlukan diskusi serius di saluran publik,seperti milis atau kelompok peninjau PR.

### Implementasi Bitcoin lainnya

Meskipun marjinal dalam hal adopsi, aplikasi lain memang ada. Yang terbanyak adalah Bitcoin Knots, yang dikembangkan oleh Luke Dashjr, sebuah fork dari Bitcoin Core yang menggabungkan opsi tambahan dan pendekatan pengembangan yang lebih konservatif. Ini termasuk pembatasan yang lebih ketat pada format transaksi.

![Image](assets/fr/058.webp)

Kita juga dapat menyebutkan:

- **Libbitcoin**: library C++ yang modular yang dikembangkan oleh Amir Taaki dan dipelihara oleh Eric Voskuil;
- **Bcoin**: Implementasi JavaScript (tidak lagi aktif dipelihara).
- **BTCD/btcsuite**: Implementasi dalam Go.

Proyek-proyek ini berkontribusi pada keragaman ekosistem, tetapi adopsi mereka tetap sangat terbatas, sehingga menyulitkan Bitcoin Core untuk berevolusi secara mandiri.

### Kekuatan pengembang Core

Anda mungkin berpikir bahwa pengembang Bitcoin Core memiliki kendali langsung atas Bitcoin, tetapi kenyataannya tidak demikian. Mereka tidak dapat memaksakan perubahan pada protokol. Peran mereka adalah mengusulkan kode. Terserah pada setiap pengguna, melalui node mereka, untuk memutuskan apakah akan menggunakan kode ini atau tidak.

Ini berarti bahwa jika perubahan dalam Bitcoin Core tidak memenuhi konsensus, itu dapat diabaikan oleh node, baik dengan tidak memperbarui Bitcoin Core atau hanya dengan mengganti implementasi. Sebaliknya, jika fitur yang diinginkan pengguna terhalang dalam proses pengembangan Core, hal ini memungkinkan untuk beralih ke implementasi lain atau fork proyek.

Seperti yang akan kita bahas nanti dalam kursus ini, Node-node, sesuai dengan bobot ekonominya (yaitu, para pedagang), yang memberikan utilitas pada versi protokol (dan karenanya pada mata uang yang sesuai), dengan menerima unit yang mematuhi aturannya. Oleh karena itu, kekuatan tata kelola yang sebenarnya atas Bitcoin terletak pada para pedagang ini, bukan pada para pengembang.

# Menjadi seorang bitcoiner yang berdaulat

<partId>df64cad2-e92d-4949-9cca-14394aad0bc6</partId>

## Mengapa menjalankan node sendiri?

<chapterId>39c0cd19-67f9-4c64-bfb3-dbd6eec0bf42</chapterId>

Ada kepercayaan yang dipegang secara luas bahwa mengoperasikan Node Bitcoin adalah tindakan yang murni altruistik, tanpa keuntungan pribadi, semata-mata demi desentralisasi jaringan. Beberapa menganggapnya sebagai bentuk kewajiban bagi para bitcoiner untuk mendukung sistem dan menunjukkan rasa terima kasih mereka kepada Bitcoin.

Seperti yang telah kita tekankan di bab-bab sebelumnya, menjalankan node tidak memberikan keuntungan finansial langsung. Oleh karena itu, orang mungkin berpikir tidak ada manfaat pribadi dalam melakukannya. Namun, mengoperasikan node Anda sendiri membawa banyak keuntungan individual. Untuk meyakinkan Anda tentang hal ini, dalam bab ini saya akan menyajikan semua alasan—baik teknis maupun strategis—yang seharusnya mendorong Anda untuk memasang dan menggunakan Node Bitcoin Anda sendiri.

### Penyebaran transaksi yang lebih rahasia

Ketika perangkat lunak wallet terhubung ke node eksternal, perangkat lunak ini mengirimkan transaksinya ke infrastruktur yang tidak berada di bawah kendali Anda. Hal ini menimbulkan risiko pengawasan yang jelas: operator node jarak jauh dapat menganalisis detail transaksi Anda, termasuk jumlah dan frekuensi, dan, dengan mencocokkan metadata tertentu (seperti alamat IP, waktu, dan lokasi), berpotensi mengaitkannya dengan identitas Anda.

Memang, seperti yang ditunjukkan di bab sebelumnya, wallet tidak berkomunikasi dengan Jaringan Bitcoin secara ajaib; wallet harus terhubung ke node untuk melihat saldo atau menyiarkan transaksi. Jika Anda belum pernah mengatur node Anda sendiri, ini berarti wallet Anda bergantung pada infrastruktur pihak ketiga (biasanya perusahaan di belakang perangkat lunak). Pihak ketiga ini, terutama jika itu adalah perusahaan, dapat mengamati, mengeksploitasi, atau bahkan mengungkapkan data ini: baik untuk alasan komersial, di bawah batasan hukum, atau sebagai akibat dari peretasan.

![Image](assets/fr/059.webp)

Dengan menggunakan node Anda sendiri, Anda menyiarkan transaksi Anda langsung ke jaringan, tanpa perantara. Asalkan Anda mengamankan node Anda dengan benar (yang akan kita bahas nanti) atau mematuhi standar tertentu, tidak ada informasi yang terekspos: baik alamat IP Anda maupun detail transaksi Anda tidak melewati entitas yang tidak Anda kontrol. Ini adalah prasyarat dasar untuk menjaga kerahasiaan Anda di Bitcoin.

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Transaksi yang tidak dapat disensor

Untuk alasan yang sama yang disebutkan di atas, perangkat lunak wallet yang didasarkan pada node pihak ketiga rentan terhadap risiko sensor: operator node jarak jauh dapat menolak untuk meneruskan transaksi tertentu karena berbagai alasan. Mereka dapat menganggapnya mencurigakan atau bertentangan dengan kebijakan mereka. Transaksi juga dapat diblokir jika tidak mematuhi aturan relay node. Terakhir, operator dapat secara spesifik menargetkan alamat IP Anda untuk memblokir penyiaran transaksi Anda.

Sebaliknya, dengan menggunakan node Anda sendiri, Anda memastikan penyebaran transaksi Anda di dalam jaringan peer-to-peer. Ini berarti Anda mempertahankan kontrol total atas distribusi transaksi Anda, tanpa ketergantungan pada perantara. Selama transaksi mematuhi aturan konsensus dan relay dari node yang terhubung dengan node Anda, transaksi itu akan disiarkan di jaringan, dan kemudian, asalkan biaya yang cukup disertakan, diintegrasikan ke dalam blok oleh miner. Memiliki node Anda sendiri menjamin konfirmasi transaksi Anda yang netral dan bebas izin.

### Verifikasi data independen

Tanpa node pribadi, Anda tetap bergantung pada pihak ketiga untuk akses ke informasi, seperti saldo alamat Anda, status konfirmasi transaksi, dan validitas blok. Hal ini menyiratkan kepercayaan implisit pada keakuratan dan integritas node eksternal.

![Image](assets/fr/060.webp)

Menjalankan full node berarti Anda dapat memeriksa semua aturan protokol sendiri, untuk setiap transaksi dan setiap blok. Akibatnya, saldo yang ditampilkan oleh wallet Anda bukanlah data yang diterima dari server jarak jauh, tetapi hasil yang dihitung secara lokal dari salinan Blockchain lengkap, yang divalidasi blok demi blok. Pendekatan ini memberikan makna penuh pada pepatah para bitcoiner:

> Jangan percaya, verifikasi.

### Distribusi keamanan sistem yang lebih baik

Setiap node yang bergabung dengan jaringan memperkuat redudansi dan ketahanan Bitcoin. Ini memfasilitasi penyebaran informasi dan memungkinkan peer baru untuk terhubung satu sama lain. Tanpa node, sistem tidak akan dapat dioperasikan.

Seperti yang telah kita lihat, keamanan Bitcoin tidak didasarkan pada desentralisasi, mining, atau kriptografi: seperti sistem apa pun, ia bergantung pada individu. Lebih tepatnya, ia bergantung pada kemampuan operator node untuk melawan paksaan.

Apa yang membedakan sistem terdesentralisasi seperti Bitcoin adalah distribusi risiko di antara semua yang terlibat dalam operasinya. Menjalankan Node Bitcoin Anda sendiri berarti menerima bagian dari risiko ini dengan memastikan keamanan instans Anda; dengan melakukan itu, Anda juga meringankan beban risiko bagi operator node lain.

Jadi ini bukan manfaat pribadi secara langsung: menjalankan node membuat Anda sebagian bertanggung jawab atas keamanan jaringan. Yang terpenting, ini adalah manfaat kolektif, karena keterlibatan Anda membantu menyebarkan risiko. Pada gilirannya, Anda meningkatkan kemampuan Anda sendiri untuk menggunakan Bitcoin secara andal.

### Memperdalam pemahaman Anda tentang sistem

Menginstalasi full node bukanlah operasi sepele. Ini melibatkan pemasangan perangkat lunak, memahami operasi dasar, memantau sinkronisasi, memeriksa log jika terjadi masalah, dan bahkan menggunakan terminal. Ini pasti akan menuntun Anda untuk memperdalam pemahaman Anda tentang protokol. Ini adalah keuntungan tidak langsung, tetapi bukan keuntungan yang signifikan.

Memperoleh pengetahuan ini memperkuat kepercayaan Anda pada programnya dan dapat mengurangi risiko kesalahan atau paparan terhadap penipuan. Menjalankan node Anda sendiri juga berarti proses belajar.

### Memilih aturan mana yang akan diterapkan

Aspek penting, yang sering disalahpahami, adalah bahwa mengoperasikan node memungkinkan Anda memilih aturan yang Anda terapkan secara lokal. Ada dua jenis aturan utama:

- **Aturan Konsensus:**

Ini adalah aturan fundamental dari protokol Bitcoin, memastikan integritas sistem dan menetapkan kriteria untuk memvalidasi transaksi dan blok. Setiap transaksi yang tidak mematuhi aturan konsensus ini tidak akan pernah dapat dimasukkan dalam blok yang valid. Misalnya, transaksi dengan tanda tangan yang tidak valid akan secara sistematis dikecualikan.

Mengubah aturan ini setara dengan mengubah protokol, dan ternasuk juga mata uang (Hard Fork). Namun, fakta sederhana untuk secara ketat menerapkan aturan yang ada memberikan kekuatan tertentu: jika sebuah blok melanggar aturan, node segera menolaknya.

- **Aturan Relai**:

Ini adalah aturan spesifik untuk setiap Node Bitcoin, yang ditambahkan ke aturan konsensus untuk mendefinisikan struktur transaksi yang belum dikonfirmasi yang diterima di Mempool dan diteruskan ke peer. Setiap node mengonfigurasi dan menerapkan aturan ini secara lokal, yang menjelaskan mengapa aturan tersebut mungkin berbeda dari satu node ke node lain. Aturan ini hanya berlaku untuk transaksi yang belum dikonfirmasi: transaksi yang dianggap "tidak standar" oleh node hanya akan diterima jika sudah muncul dalam blok yang valid. Mengubah aturan ini tidak mengecualikan node dari sistem Bitcoin. Mengubah aturan ini tidak mengeluarkan node dari sistem Bitcoin.

Contoh: Transaksi tanpa biaya, menurut aturan konsensus, sepenuhnya valid, tetapi secara default akan ditolak menurut kebijakan relay Bitcoin Core, karena parameter `minRelayTxFee` diatur ke `0,00001` (dalam BTC/kB). Namun, dimungkinkan, pada node Anda sendiri, untuk menurunkan ambang batas ini untuk meneruskan transaksi dengan biaya lebih rendah, atau, sebaliknya, meningkatkan batas, misalnya, menjadi 2 Sats/vB, untuk menghindari merelay transaksi dengan biaya rendah.


Memutar simpul Anda sendiri berarti menegaskan: "Saya memvalidasi apa yang saya pilih untuk divalidasi, sesuai dengan aturan yang saya terapkan sendiri "*. Dengan demikian, Anda menjadi aktor dalam tata kelola sistem, dapat menolak evolusi yang tampaknya tidak dapat Anda terima, atau menyetujui pembaruan sesuai dengan kriteria Anda sendiri.

Menjalankan node Anda sendiri berarti menegaskan: _"Saya memvalidasi apa yang saya pilih untuk divalidasi, sesuai dengan aturan yang saya adopsi sendiri"_. Dengan demikian, Anda menjadi aktor dalam tata kelola sistem, mampu menolak evolusi yang tampaknya tidak dapat diterima oleh Anda, atau menyetujui pembaruan sesuai dengan kriteria Anda sendiri.

Jadi, kita dapat dengan cepat mencoba memahami seberapa besar berkat dari kekuatan yang Anda miliki atas aturan dari node Anda. Dan tingkat kekuatan ini akan bergantung pada jenis aturannya.

#### Untuk aturan relai

Sejauh menyangkut aturan relay, hal mendasar adalah memiliki node, terlepas dari aktivitas ekonominya. Yang dipertaruhkan di sini adalah apakah Anda setuju atau tidak untuk meneruskan jenis transaksi tertentu.

Jika, misalnya, Anda yakin bahwa transaksi dengan biaya kurang dari 1 sat/vB harus diterima di Bitcoin, Anda dapat menyesuaikan aturan ini pada node Anda sehingga menyiarkan transaksi tersebut, dengan demikian memfasilitasi penyebarannya di jaringan sampai miner pada akhirnya memasukkannya ke dalam blok yang valid. Pada dasarnya, ini adalah masalah kekuatan atas penyebaran transaksi: setiap node memiliki kekuatan pengambilan keputusan, karena menyetujui untuk meneruskan jenis transaksi sama saja dengan mempromosikan penerimaannya di Jaringan Bitcoin. Akibatnya, jika Anda mengoperasikan beberapa node, Anda memiliki pengaruh yang lebih besar terhadap kebijakan relay, karena setiap node memiliki koneksi dan area dampaknya sendiri pada jaringan.

Memang, Memiliki satu atau lebih node yang dikonfigurasi dengan aturan relay spesifik berarti menentukan bagian mana dari jaringan yang menerima untuk menyebarkan jenis transaksi tertentu. Menyebarkan pesan dalam grafik peer-to-peer, seperti halnya untuk transaksi Bitcoin, mengikuti logika teori perkolasi. Bayangkan setiap node sebagai situs yang dapat aktif (`p` = ia merelay) atau tidak aktif (`1-p`). Segera setelah proporsi `p` melewati ambang batas kritis (`p_c`), komponen raksasa muncul: transaksi berhasil melintasi jaringan dan memiliki setiap peluang untuk mencapai miner. Dalam jaringan seperti Bitcoin, di mana setiap node memelihara rata-rata 8 koneksi keluar, ambang batas `p_c` umumnya ditetapkan hanya pada beberapa persen, bahkan lebih rendah jika beberapa node memiliki jumlah koneksi yang sangat besar.

![Image](assets/fr/061.webp)

Selama `p` tetap berada di bawah `p_c`, transaksi tetap terbatas pada kantong-kantong terisolasi dan tidak mencapai miner. Segera setelah ambang batas ini terlampaui, transaksi menyebar hampir seketika ke seluruh jaringan.

Pada akhirnya, selalu para miner yang memutuskan apakah akan menyertakan transaksi dalam blok atau tidak. Namun, para node melakukan intervensi di bagian hulu dengan memengaruhi distribusi transaksi: mereka menentukan apakah para miner akan mengetahui transaksi tertentu atau tidak. Jika transaksi tidak diteruskan ke miner, jelas tidak mungkin bagi mereka untuk memasukkannya ke dalam blok.

Menambahkan beberapa node lagi karena itu hanya akan memiliki dampak marjinal jika jaringan sudah berada dalam fase perkolasi untuk jenis transaksi tertentu, tetapi dapat terbukti menentukan karena ambang batas perkolasi mendekat. Memiliki atau memengaruhi beberapa node, terutama jika node terhubung dengan baik, dapat meningkatkan atau mengurangi nilai `p` dan, akibatnya, secara tidak langsung mengarahkan aturan relay yang menentukan transaksi mana yang dilihat dan pada akhirnya diterima oleh miner.

#### Untuk aturan konsensus

Ketika menyangkut pengaruh node Anda pada aturan konsensus, bobot ekonominya lah, di atas segalanya, yang akan menjadi penentu. Ini adalah konsep krusial: nilai mata uang apa pun secara langsung terkait dengan kemampuannya untuk memfasilitasi pertukaran. Memang, jika suatu objek tidak diterima oleh siapa pun dalam pertukaran barang atau jasa, secara teoretis ia tidak memiliki utilitas moneter. Misalnya, jika tidak ada pedagang yang menerima kerikil sebagai alat pembayaran, kerikil tersebut tidak berguna sebagai uang. Tentu saja, utilitas tetap merupakan gagasan subjektif pada skala individu, tetapi di wilayah tertentu, semakin besar jumlah pedagang yang menerima suatu objek sebagai alat tukar, semakin besar kemungkinan objek tersebut memiliki utilitas moneter bagi orang-orang yang tinggal di wilayah ini.

Mari kita ambil contoh desa di mana banyak pedagang menerima emas sebagai ganti membeli barang: kemungkinan besar emas memiliki utilitas moneter bagi penduduk desa. Ini menunjukkan bahwa utilitas mata uang bergantung langsung pada keputusan para pedagang untuk menerima atau menolak mata uang tersebut.

Konsep ini sangat penting untuk memahami dinamika kekuasaan yang dimainkan dalam sistem Bitcoin. Satoshi menjelaskan: Bitcoin adalah sistem uang elektronik; dengan kata lain, sistem ini menyediakan layanan yang menawarkan bentuk mata uang, Bitcoin (atau BTC). Ketika aturan protokol dimodifikasi dengan cara yang tidak kompatibel ke belakang (Hard Fork), ini sama saja dengan menciptakan sistem baru dan karenanya mata uang baru. Keberhasilan atau kegagalan Fork ini kemudian bergantung pada ukuran ekonominya, yang pada gilirannya ditentukan oleh jumlah pedagang yang menerima bentuk mata uang baru ini.

![Image](assets/fr/062.webp)

Mari kita ambil contoh: anggaplah Bitcoin mengalami Hard Fork. Maka akan ada 2 bentuk mata uang yang berbeda: BTC-1 (versi asli, tidak berubah) dan BTC-2 (mata uang baru dengan aturan konsensus yang berbeda). Jika semua pedagang yang menerima BTC-1 terus melakukannya, tetapi menolak BTC-2, maka yang terakhir secara teoretis, memiliki utilitas moneter yang sangat terbatas. Sebagai pengguna, saya tidak akan tertarik untuk menyimpan dan menggunakan BTC-2, karena mengetahui bahwa tidak ada pedagang yang menginginkannya sebagai ganti barang atau jasa. Sebaliknya, jika 50% pedagang memilih untuk menerima BTC-2 secara eksklusif dan 50% sisanya hanya mengambil BTC-1, maka utilitas BTC-1 akan, secara teoretis, berkurang setengahnya. Saya menggunakan istilah "secara teoretis" karena utilitas tetap merupakan gagasan subjektif pada tingkat individu dan bergantung pada banyak faktor (seperti wilayah dan kebiasaan konsumsi) yang sulit dipahami berdasarkan kasus per kasus.

Pada Bitcoin, peran "pedagang", dipahami sebagai entitas apa pun dengan bobot ekonomi tertentu, tentu saja termasuk bisnis (toko fisik, situs penjualan online, penyedia layanan, dll.), tetapi juga platform exchange, karena mereka menerima Bitcoin sebagai ganti mata uang lain, dan miner, karena mereka menerima Bitcoin melalui biaya sebagai ganti layanan memasukkan transaksi ke dalam blok.

Sejauh menyangkut aturan konsensus, node Anda memungkinkan Anda mengarahkan aktivitas ekonomi Anda menuju satu mata uang atau mata uang lain. Misalnya, jika Anda memiliki 10 full node di rumah, tetapi tidak ada aktivitas ekonomi yang signifikan, pengaruh Anda selama Fork akan hampir nol. Sebaliknya, satu node yang digunakan untuk mengelola rantai 200 toko yang menerima Bitcoin memberikan bobot ekonomi yang signifikan.

Jadi, bukan jumlah node yang penting, tetapi pentingnya aktivitas ekonomi yang mereka dukung. Terlebih lagi, jika aktivitas ekonomi Anda bergantung pada node yang tidak Anda kontrol, pemiliknya akan memutuskan mata uang apa yang Anda gunakan, selama Anda tetap terhubung ke node tersebut. Inilah mengapa menjalankan dan menggunakan node Anda sendiri sangat penting dalam konteks tata kelola sistem:

> Bukan node Anda, bukan aturan Anda. 

## Berbagai jenis node Bitcoin yang berbeda

<chapterId>be8f0baa-41f2-4b54-b011-092f4ccc93aa</chapterId>

Node Bitcoin, oleh karena itu, adalah mesin yang menjalankan implementasi dari protokol Bitcoin. Di balik definisi umum node ini, terdapat beberapa kemungkinan konfigurasi, yang tidak semuanya menawarkan tingkat otonomi, konsumsi sumber daya, dan kegunaan yang sama untuk jaringan. Dalam bab ini, kami akan mencoba memahami perbedaan-perbedaan ini untuk membantu Anda memilih arsitektur node yang sesuai dengan penggunaan dan kendala perangkat keras Anda.

### Full Node

Full Node adalah Node Bitcoin yang secara sederhana mengunduh seluruh Blockchain dari blok Genesis, memvalidasi setiap blok secara independen, dan menyimpan seluruh riwayat Blockchain tersebut secara lokal. Ini adalah bentuk node yang "normal", seperti yang dibayangkan oleh Satoshi Nakamoto.

![Image](assets/fr/063.webp)

Full Node tidak perlu memercayai siapa pun karena ia memvalidasi dan mengetahui semua informasi dalam sistem. Ini adalah jenis node yang memberi Anda jaminan paling besar: Anda tahu, tanpa bergantung pada pihak ketiga, apakah pembayaran valid, apakah blok valid, apakah reorganisasi sah, dan sebagainya.

Dalam praktiknya, Full Node membutuhkan sumber daya yang tidak sedikit, termasuk beberapa ratus gigabyte untuk file blok, prosesor yang mampu memvalidasi script, RAM untuk Mempool dan cache, serta bandwidth yang stabil. Sinkronisasi pertama (IBD – Initial Block Download) membaca dan memverifikasi riwayat lengkap: ini intensif, tetapi hanya terjadi sekali. Full Node secara aktif berpartisipasi dalam jaringan, meneruskan blok dan transaksi, dan dapat menerima koneksi masuk untuk membantu peer lain.

Tergantung pada kebutuhan Anda, Anda dapat menambahkan indexer ke Full Node Anda. Bitcoin Core menawarkan pengindeksan transaksi sebagai fitur opsional (dinonaktifkan secara default), yang dapat berguna untuk tujuan tertentu. Namun, ini tidak menyertakan pengindeks alamat (address indexer), yang seringkali merupakan fitur yang paling dicari untuk pengguna individu. Untuk mengatasinya, Anda dapat memasang perangkat lunak khusus pada node Anda, seperti Electrs atau Fulcrum, untuk mempercepat query verifikasi saldo alamat dari UTXO yang terkait. Kita akan kembali membahas peran indexer secara lebih rinci dalam bab terpisah.

### Pruned Node

Pruned Node memvalidasi semuanya seperti Full Node, mulai dari blok Genesis hingga puncak rantai dengan proof-of-work terbanyak, **tetapi hanya menyimpan bagian yang paling baru dari file blok**. Setelah blok-blok lama diperiksa, node akan secara bertahap menghapusnya untuk tetap berada di bawah batas ruang yang dapat Anda tentukan. Konfigurasi ini ideal jika Anda memiliki keterbatasan ruang disk: Anda mempertahankan independensi validasi blok, tanpa perlu menyimpan arsip riwayat Blockchain lengkap. Opsi ini sangat berguna jika Anda hanya ingin memasang Bitcoin Core di komputer pribadi Anda, tanpa menggunakan mesin khusus.

![Image](assets/fr/064.webp)

Implikasi teknis dari opsi ini cukup jelas: pruned node mampu menyiarkan transaksi Anda dengan sempurna, berpartisipasi dalam relay, memverifikasi blok dan transaksi, serta melacak chain. Di sisi lain, ia tidak dapat berfungsi sebagai sumber data historis di luar batasnya untuk aplikasi lain (misalnya, explorer penuh, indexer, wallet). Oleh karena itu, fungsi yang memerlukan arsip (atau indeks global) tidak akan tersedia.

Secara praktis, Anda dapat menggunakan pruned node untuk menghubungkan perangkat lunak manajemen wallet seperti Sparrow wallet. Namun, Anda tidak akan dapat memindai transaksi pada wallet Anda yang mendahului batas pemangkasan. Misalnya, jika Anda memiliki transaksi yang terdaftar di blok 901.458, tetapi node Anda hanya menyimpan blok dari 905.402 ke atas (karena yang tertua telah dipangkas), Anda tidak akan dapat memindai transaksi ini. Di sisi lain, jika Anda sudah memindainya ketika node Anda masih memiliki blok tingkat ini, maka perangkat lunak manajemen wallet Anda akan menyimpan informasi tersebut dan menampilkan saldo UTXO yang sesuai dengan benar.

Singkatnya, pelacakan wallet berfungsi tanpa hambatan pada pruned node jika Anda membuat wallet baru saat perangkat lunak Anda sudah terhubung ke node tersebut. Namun, Anda mungkin menghadapi kesulitan jika Anda memulihkan wallet lama, karena transaksi masa lalu yang tidak lagi disimpan oleh node, jelas tidak akan dapat diambil.

### Node ringan / SPV

Node SPV (_Simplified Payment Verification_), atau node ringan, hanya menyimpan header blok, bukan detail transaksi, dan bergantung pada full node lain untuk mendapatkan bukti bahwa suatu transaksi ada dalam blok (Merkle proofs melalui tree) yang headernya dimilikinya. Konsep verifikasi pembayaran sederhana ini bukanlah hal baru, karena telah diusulkan oleh Satoshi Nakamoto sendiri di Bagian 8 dari White Paper.

![Image](assets/fr/066.webp)

Nakamoto, S. (2008). _Bitcoin: A Peer-to-Peer Electronic Cash System_. https://Bitcoin.org/Bitcoin.pdf

Jenis node ini jelas jauh lebih ringan dalam hal penggunaan penyimpanan dan CPU daripada full node atau bahkan pruned node. Oleh karena itu, node SPV sangat cocok untuk perangkat yang lebih kecil dan koneksi yang terputus-putus (intermittent connections). Faktanya, node ini seringkali diintegrasikan langsung ke dalam wallet, terutama perangkat lunak seluler seperti Blockstream App.

Konsekuensinya adalah mengorbankan kepercayaan dan kerahasiaan: Aplikasi SPV tidak memeriksa script atau kebijakan validasi sendiri; ia mengasumsikan bahwa chain dengan proof-of-work terbanyak adalah valid, dan bergantung pada satu atau lebih full node untuk mendapatkan respons. Menggunakan jenis node ini adalah opsi yang lebih baik daripada terhubung ke node pihak ketiga; namun, ini masih kurang menguntungkan daripada memiliki full node atau bahkan pruned node.

![Image](assets/fr/065.webp)

### Node mana untuk kebutuhan yang mana?

- Pengguna seluler / pemula

Bagi pengguna pemula yang hanya memiliki wallet di aplikasi seluler, menggunakan Node SPV (Simplified Payment Verification) sudah pasti merupakan cara terbaik untuk memulai. Pemasangannya cepat, membutuhkan sedikit sumber daya, dan pengalamannya sederhana serta lancar. Ini berarti Anda dapat memverifikasi informasi tertentu sendiri dan, oleh karena itu, mengurangi ketergantungan pada node pihak ketiga sekaligus lebih independen dalam hal penyiaran transaksi.

- PC / pengguna menengah

Pengguna tingkat menengah dengan PC dapat memasang Pruned Node (Node Terpangkas) untuk mendapatkan hampir semua keuntungan dari Full Node, tanpa membebani mesin mereka setiap hari: validasi penuh, penggunaan disk yang moderat, dan pemeliharaan yang sederhana. Ini adalah solusi ideal untuk menghubungkan desktop wallet Anda dan tetap independen dalam distribusi transaksi Anda, tanpa berinvestasi pada mesin khusus atau membebani ruang disk Anda.

- Bitcoiner berdaulat / mahir

Full Node (Node Penuh) tetap merupakan solusi terbaik jika Anda ingin sepenuhnya independen dalam penggunaan Bitcoin Anda dan tidak membatasi diri Anda di kemudian hari untuk penggunaan lanjutan seperti indexer, Node Lightning, atau bahkan block explorer. Itulah yang akan kita jelajahi secara mendalam dalam kursus ini!

## Gambaran umum solusi perangkat lunak

<chapterId>0d48b89a-e8b5-441e-a707-537a035fc15e</chapterId>

Dari sisi perangkat lunak, ada 2 cara utama untuk menjalankan Node Bitcoin:

- Menginstal langsung implementasi protokol, seperti Bitcoin Core (direkomendasikan), atau Bitcoin Knots,
- Atau menggunakan distribusi turnkey (sering disebut "_node-in-a-box_") yang mengintegrasikan implementasi Bitcoin dengan cara yang sama, tetapi juga mencakup sistem administrasi Interface, toko aplikasi, dan alat siap pakai (Lightning, browser, server indexer, bahkan aplikasi self-hosting di luar Bitcoin...).

Kedua pendekatan ini mengarah pada tujuan yang sama: memiliki node Anda sendiri, tetapi keduanya berbeda dalam hal pemasangan dan penggunaan Interface, pemeliharaan, pengembangan, dan biaya. Itulah yang akan kita jelajahi dalam bab ini.

### Implementasi node Bitcoin manual

Memasang implementasi manual berarti langsung menggunakan perangkat lunak dari implementasi protokol Bitcoin (seperti Core), tanpa lapisan perangkat lunak tambahan apa pun. Anda mengelola sendiri konfigurasi, pembaruan, dan layanan terkait (indexing, API, Lightning, backup, dll.), sesuai dengan kebutuhan Anda.

Ini adalah pendekatan yang paling berdaulat dan fleksibel: Anda tahu persis apa yang berjalan, di mana data berada, dan bagaimana semuanya bekerja. Di sisi lain, ini menjadi lebih kompleks segera setelah Anda ingin melampaui operasi sederhana dari Node Bitcoin. Jika tujuan Anda hanya untuk memiliki node, kompleksitasnya sebanding dengan node-in-a-box, atau bahkan kurang, karena ini hanyalah masalah memasang perangkat lunak.

#### Bitcoin Core (Aplikasi Dominan)

[Bitcoin Core adalah client yang sangat mayoritas di jaringan](https://bitcoincore.org/). Bitcoin Core mengunduh, memvalidasi, dan memelihara Blockchain, menyediakan API RPC/REST, dan dapat mengintegrasikan wallet. Jika Anda lebih memilih alat standar dan merasa nyaman menambahkan layanan sendiri (seperti server Electrum, explorer, dan LND), sebaiknya Anda menggunakan Core apa adanya.

**Keuntungan:** Stabilitas maksimum, perilaku yang dapat diprediksi, raw experience, mudah dipasang dan dikonfigurasi.

**Kerugian:** Anda harus membangun sisa stack secara manual untuk membuat lingkungan aplikasi yang lengkap, bukan hanya node Bitcoin.

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

#### Bitcoin Knots (Aplikasi alternatif utama)

[Bitcoin Knots adalah Fork dari Bitcoin core](https://bitcoinknots.org/), yang dikelola oleh Luke Dashjr. Ini adalah aplikasi alternatif utama untuk Core dalam mengimplementasikan protokol Bitcoin. Sepenuhnya kompatibel dengan sisa jaringan (sama sekali bukan Hard Fork seperti Bitcoin Cash), namun ia menawarkan fitur tambahan, termasuk opsi kebijakan relay yang tidak ada di Core, atau diterapkan lebih ketat secara default untuk membatasi apa yang oleh beberapa orang dianggap sebagai spam.

Ada 2 alasan yang mungkin untuk memilih Knots daripada Core:

- **Teknis:** Opsi yang berbeda dari Core, terutama dalam hal manajemen relay, dengan menentukan transaksi mana yang diterima dan disiarkan oleh node Anda.
- **Kebijakan**: Beberapa orang lebih suka menggunakan aplikasi alternatif seperti Knots untuk alasan non-teknis, terutama untuk mendukung alternatif Core dan dengan demikian mengurangi monopolinya. Jika Core suatu saat disusupi, akan berguna tidak hanya memiliki aplikasi alternatif yang solid dan terawat dengan baik tetapi juga tahu cara memanfaatkannya secara efektif. Yang lain menggunakan Knots untuk tujuan protes, karena mereka telah kehilangan kepercayaan pada pengembang Core atau tidak menyetujui manajemen mayoritas aplikasi.

https://planb.academy/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Secara pribadi, saya merekomendasikan Anda memilih Core, terutama untuk mendapatkan manfaat dari patch keamanan lebih cepat. Memang, beberapa kerentanan yang ditemukan di Knots dikoreksi dengan penundaan. Secara umum, proses pengembangan Core terstruktur dengan kokoh dan didukung oleh sejumlah besar kontributor, sedangkan Knots dikelola oleh satu orang dan memiliki komunitas yang jauh lebih kecil. Di sisi lain, aturan relay cenderung kehilangan kegunaannya saat ini, terutama ketika diterapkan hanya oleh sebagian kecil dari jaringan (sesuai teori perkolasi).

### Node-in-a-box distributions

Node-in-a-box menggabungkan Bitcoin Core (atau Knots) dengan sistem operasi yang telah dikonfigurasi sebelumnya, Interface Web, dan Toko Aplikasi (App Store) layanan self-hosting (Lightning, explorer, server Electrum, Mempool, BTCPay Server, Nextcloud, dll.). Hanya dengan satu klik, Anda dapat memasang, memperbarui, dan menghubungkan berbagai modul yang beragam ini.

Ini adalah solusi yang jauh lebih sederhana untuk memulai dan mengelola banyak aplikasi tambahan sehari-hari. Sisi negatifnya adalah ketika masalah terjadi (misalnya, konflik image Docker, pembaruan yang salah, database yang rusak), debugging bisa menjadi sangat kompleks, karena Anda bergantung pada integrasi distribusi itu sendiri. Terlebih lagi, dukungan komunitas atau resmi seringkali rumit.

Jadi, node-in-a-box sangat mudah digunakan selama semuanya berjalan dengan baik, tetapi jika terjadi bug, Anda harus siap untuk melakukan pencarian panjang, menunggu bantuan, dan "mengotori tangan Anda".

Sebagian besar solusi ini tersedia dalam dua format:

- Mesin yang Sudah Dirakit (Pre-assembled machine): Komputer lengkap dengan OS sudah terinstal. Mesin berbayar ini hanya perlu disambungkan ke listrik dan dihubungkan ke Internet agar dapat beroperasi. Jika anggaran Anda memungkinkan, opsi ini memiliki keunggulan pengaturan yang sangat sederhana, seringkali menawarkan dukungan prioritas, dan berkontribusi pada pendanaan pengembangan, karena model bisnis perusahaan-perusahaan ini umumnya didasarkan pada penjualan hardware.

- DIY (Do It Yourself): Memasang OS distribusi pada mesin Anda sendiri (PC lama, NUC, Raspberry Pi, home server...). Ini adalah solusi yang paling ekonomis, karena Anda dapat mendaur ulang mesin lama atau memilih hardware yang secara tepat sesuai dengan kebutuhan dan anggaran Anda. Ini juga merupakan opsi yang paling fleksibel, dan yang paling memuaskan untuk dikonfigurasi. Pendekatan inilah yang akan kita jelajahi di bagian praktis kursus.

Berikut adalah gambaran umum dari solusi node-in-a-box utama yang tersedia (pada tahun 2025):

### Umbrel (umbrelOS & Umbrel Home)

Peran Miner juga terkadang dibedakan dengan peran grind. Grind adalah sebuah mesin yang bertugas untuk membuat template blok yang disediakan oleh server pool, mencari hash yang memenuhi target tingkat kesulitan yang ditentukan untuk saham, dan bukan untuk Bitcoin. Sisa dari proses Mining, yang meliputi konstruksi blok aktual, pemilihan transaksi, atau pencarian Proof-of-Work sesuai dengan tingkat kesulitan Bitcoin, serta distribusi, dilakukan secara langsung oleh pool.

![Image](assets/fr/067.webp)

Diluncurkan pada tahun 2020 sebagai node Bitcoin sederhana yang disertai dengan beberapa aplikasi tambahan, Umbrel secara bertahap berevolusi menjadi home cloud modern yang berfitur lengkap.

Saya tidak akan membahas lebih detail di sini tentang cara kerjanya dan fitur spesifiknya, karena kita akan memeriksanya lebih dalam di bab pertama bagian selanjutnya. Memang, untuk tujuan kursus BTC 202 ini, saya telah memilih untuk menggunakan UmbrelOS, yang saya yakini sebagai solusi node-in-a-box terbaik saat ini untuk pengguna pemula dan menengah.

https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

### Start9 (StartOS)

[Start9 menawarkan StartOS](https://start9.com/), sebuah sistem yang dirancang untuk "komputasi berdaulat" (sovereign computing): tujuannya adalah agar setiap orang memiliki dan mengelola server pribadi mereka sendiri, ditingkatkan dengan pasar aplikasi self-hosted. Anda dapat membeli server Start9 (Server One seharga $619, Server Pure seharga $899) atau merakitnya sendiri dalam mode DIY pada komputer Anda.

Di sisi Bitcoin, StartOS memungkinkan Anda memasang full node, Node Lightning, BTCPay Server, Electrs, dan banyak layanan lainnya. Namun, daya tarik Start9 meluas melampaui ini: ia menawarkan kemungkinan untuk menemukan, mengonfigurasi, dan mengekspos berbagai perangkat lunak (file cloud, perpesanan, pemantauan) secara terpadu, dengan kendali penuh. Oleh karena itu, proyek ini ditujukan untuk pengguna yang menginginkan platform self-hosting yang tangguh, bukan hanya node Bitcoin sederhana. Ini mungkin ekosistem yang paling lengkap setelah Umbrel.

![Image](assets/fr/068.webp)

Perbedaan utama dengan Umbrel terletak pada Interface. Umbrel mengandalkan UX yang sangat halus, sementara Start9 menawarkan Interface yang lebih kasar, tetapi lebih fungsional. Ekosistem aplikasi Start9 kurang kaya daripada Umbrel, tetapi ia mengimbanginya dengan beberapa keunggulan teknis: akses ke pengaturan aplikasi lanjutan yang disederhanakan, sedangkan Umbrel dengan cepat menjadi terbatas jika opsi yang diinginkan tidak disediakan oleh Interface. Start9 juga unggul dalam manajemen backup: terlepas dari solusi efisien Umbrel untuk LND, tidak ada mekanisme terpadu, tidak seperti Start9. Terlebih lagi, ia menawarkan alat pemantauan yang lebih mudah diakses dan koneksi jarak jauh terenkripsi (`https`), sedangkan akses lokal ke Umbrel adalah melalui `http`.

Singkatnya, jika Anda hanya membutuhkan aplikasi penting untuk Bitcoin, tanpa minat khusus pada ekosistem Umbrel yang sangat beragam, dan Interface pengguna bukan prioritas, maka Start9 adalah pilihan yang lebih baik. Jika tidak, Umbrel adalah pilihan yang lebih baik.

https://planb.academy/tutorials/node/bitcoin/start9-8c8b6827-8423-4929-bcba-89057670ed6a

### MyNode

[MyNode adalah distribusi yang difokuskan secara eksklusif pada Bitcoin dan Lightning](https://mynodebtc.com/), menawarkan web Interface, pasar aplikasi, dan upgrade sekali klik. Anda bisa membeli perangkat keras siap pakai (*Model Dua* tersedia dengan harga $ 549) atau menginstal MyNode secara gratis di komputer Anda. Proyek ini juga menawarkan versi *Premium* dari perangkat lunak ($94), yang mencakup dukungan prioritas dan fitur-fitur canggih.

[MyNode adalah distribusi yang secara eksklusif berfokus pada Bitcoin dan Lightning](https://mynodebtc.com/), menawarkan web interface, app market, dan upgrade sekali klik. Anda dapat membeli hardware siap pakai (_Model Two_ tersedia seharga $549) atau memasang MyNode secara gratis di komputer Anda sendiri. Proyek ini juga menawarkan versi Premium dari perangkat lunak ($94), yang mencakup dukungan prioritas dan fitur-fitur lanjutan.

![Image](assets/fr/069.webp)

Dalam praktiknya, MyNode menyatukan semua building block dasar yang diperlukan untuk mengoperasikan full node, serta aplikasi yang penting bagi pengguna Bitcoin. Oleh karena itu, ini adalah solusi yang cocok jika Anda tidak memerlukan aplikasi eksternal dari ekosistem Bitcoin, seperti aplikasi self-hosted yang ditemukan di sistem Start9 dan Umbrel.

https://planb.academy/tutorials/node/bitcoin/mynode-a481fef3-2fd3-4df3-91c0-112cffa094eb

### RaspiBlitz

[RaspiBlitz adalah proyek open source 100%](https://docs.raspiblitz.org/) (lisensi MIT) untuk memasang node Bitcoin dan Node Lightning pada Raspberry Pi. Cukup unduh image, boot, lalu ikuti wizard untuk memiliki node-in-a-box yang berfungsi pada Raspberry Pi Anda. Kit yang sudah dirakit sebelumnya juga tersedia dari pihak ketiga, biasanya antara $300 hingga $400, tergantung pada hardware. RaspiBlitz juga menawarkan berbagai aplikasi tambahan yang mudah dipasang.

![Image](assets/fr/070.webp)

Jika Anda memiliki Raspberry Pi, ini adalah pilihan yang sangat baik, karena sistem yang lebih lengkap seperti Umbrel menjadi semakin berat untuk jenis mini-PC ini.

https://planb.academy/tutorials/node/bitcoin/raspiblitz-d8cdba2e-a682-46cf-9fdc-d8602fbeac02

### RoninDojo

[RoninDojo adalah node-in-a-box yang berfokus pada privasi](https://wiki.ronindojo.io/en/home) yang mengotomatiskan penerapan Samurai Dojo dan Whirlpool, dengan Interface khusus dan plugin yang dirancang khusus untuk ekosistem Samurai.

Prinsipnya sederhana: jika Anda menggunakan Ashigaru Wallet (penerus Fork dari Samurai Wallet,setelah pengembangnya ditangkap) atau jika Anda ingin mendapatkan manfaat dari alat privasi lanjutan, RoninDojo cocok untuk Anda.

![Image](assets/fr/071.webp)

Proyek ini sebelumnya menawarkan mesin yang telah dikonfigurasi sebelumnya yang disebut Tanto, tetapi saat ini tidak tersedia. Mungkin akan kembali di kemudian hari. Sementara itu, dimungkinkan untuk dengan mudah memasang RoninDojo pada Rock5B+ atau Rockpro64, atau bahkan secara tidak langsung pada Raspberry Pi.

https://planb.academy/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

### Nodl

Solusi [node-in-a-box](https://www.nodl.eu/) lainnya adalah Nodl. Sama seperti proyek-proyek sebelumnya, Anda dapat membeli hardware yang telah dikonfigurasi sebelumnya (antara €599 dan €799, tergantung model) atau memasangnya sendiri dalam mode DIY.

Di sisi perangkat lunak, Nodl mengintegrasikan Bitcoin Core, LND, BTCPay Server, Electrs, Dojo, Whirlpool, Lightning Terminal, RTL, serta BTC RPC Explorer, semuanya dengan pembaruan chain terintegrasi dan kode open-source di bawah lisensi MIT.

![Image](assets/fr/072.webp)

Setelah menjelajahi berbagai solusi perangkat lunak, sekarang saatnya untuk memilih mesin yang akan menjadi host node Anda!

## Gambaran umum solusi perangkat keras

<chapterId>245d6add-9cda-46b9-9343-31dcdd70456e</chapterId>

Sekarang setelah kita menjelajahi semua kemungkinan perangkat lunak, mari kita fokus pada perangkat keras (hardware) yang dibutuhkan untuk node Anda. Saya akan memberikan beberapa saran konkret tentang pemilihan komponen, beserta konfigurasi yang disesuaikan untuk berbagai anggaran. Tentu saja, ini adalah pendapat dan pengalaman pribadi saya: tentu ada alternatif relevan lainnya selain yang disajikan di sini. Selanjutnya, saya tidak akan membahas kembali mesin rakitan yang ditawarkan oleh proyek node-in-a-box, yang telah kita bahas di bab sebelumnya. Di sini, kita akan fokus secara eksklusif pada solusi DIY (Do It Yourself).

### Apakah Anda benar-benar membutuhkan mesin khusus?

Selama beberapa tahun terakhir, para bitcoiner semakin menyadari kesalahpahaman umum, terutama dengan popularisasi node-in-a-box pada awal tahun 2020-an: bahwa Node Bitcoin harus selalu berjalan pada mesin yang didedikasikan secara eksklusif untuk tujuan ini. Tetapi ini tidak benar. Anda tidak selalu memerlukan komputer khusus untuk menjalankan Node Bitcoin: Bitcoin Core sangat mampu berjalan di PC sehari-hari Anda. Jika Anda memiliki ruang disk yang cukup untuk Blockchain atau mengaktifkan pemangkasan, Anda dapat memvalidasi chain, menghubungkan wallet Anda, dan bahkan menutup program saat Anda selesai menggunakannya. Keuntungan dari pendekatan ini sangat besar: nol investasi awal dan minimal kerumitan.

![Image](assets/fr/074.webp)

Meskipun demikian, menggunakan mesin khusus seringkali lebih nyaman. Mesin tersebut dapat berjalan terus menerus (24/7), dapat diakses dari jarak jauh setiap saat, tidak memonopoli sumber daya mesin utama Anda, dan, yang terpenting, mengisolasi penggunaan (praktik keamanan yang baik: jika PC pribadi Anda mengalami masalah, node Anda terus berfungsi, dan sebaliknya). Jadi, pertanyaannya bukanlah "Apakah saya perlu mendedikasikan sebuah mesin?", melainkan "Apakah saya memerlukan node yang terus online, dapat diakses oleh perangkat lain, dan mampu berevolusi?" (Lightning, indexer, aplikasi tambahan...). Jika jawabannya ya, memilih mesin terpisah akan membuat segalanya jauh lebih sederhana.

Menurut [data yang dikumpulkan pada Agustus 2025 oleh Luke Dashjr](https://luke.dashjr.org/programs/Bitcoin/files/charts/software.html) (pengembang terkenal di ekosistem), distribusi implementasi di antara node publik jaringan adalah sebagai berikut:

#### Mendaur ulang PC lama

Ini adalah solusi yang paling ekonomis. Sebagian besar dari kita memiliki PC lama yang berdebu di rumah, atau di antara teman dan keluarga: ini adalah kesempatan sempurna untuk menggunakannya kembali! Untuk mengadaptasinya sebagai Node Bitcoin, cukup tambahkan SSD 2TB dan, tergantung kebutuhan Anda, ganti atau tambahkan kepingan RAM untuk meningkatkan RAM. Perkirakan biaya antara €100 hingga €200 untuk mesin yang berfungsi penuh.

Sebelum membeli hardware apa pun, periksa jumlah slot disk yang tersedia, jenis koneksi (M.2 atau SATA), format RAM (SODIMM atau DIMM), dan generasinya (DDR4, dll.). Anda juga harus memanfaatkan kesempatan ini untuk membersihkan mesin, terutama kipas, untuk memastikan kinerja optimal.

Namun, berhati-hatilah jika Anda menggunakan laptop: baterai dapat menjadi masalah seiring berjalannya waktu (lebih lanjut mengenai hal ini nanti di bab ini).

#### Rekondisi atau bekas

Pasar penuh dengan bisnis mini-PC rekondisi seperti Lenovo _ThinkCentre Tiny_, _HP EliteDesk Mini_, atau _Dell OptiPlex Micro_. Mesin-mesin ini kokoh, ringkas, senyap, dan hemat energi. Harganya jauh di bawah harga baru, dan mudah untuk menemukan model yang dilengkapi dengan prosesor i5/i7 generasi ke-6 hingga ke-10 dan RAM 8 hingga 16 GB, semuanya dengan harga yang sangat menarik, umumnya antara €70 hingga €200, tergantung pada konfigurasi. Menurut pendapat saya, ini kemungkinan adalah pilihan terbaik jika Anda mencari mesin khusus untuk Node Bitcoin Anda.

![Image](assets/fr/075.webp)

Anda juga dapat untuk menemukan PC dan laptop bekas yang berasal dari beberapa tahun lalu, dengan konfigurasi yang menarik dan nilai uang yang sangat terjangkau.

**Catatan**: mesin dari barang perusahaan, seperti _ThinkCentre_ Tiny, seringkali hanya dilengkapi dengan port _DisplayPort_ (DP) untuk layar, tanpa output HDMI. Jadi, jangan lupa membawa adaptor atau kabel DP-ke-HDMI jika Anda membutuhkannya.

#### Membeli baru

Jika anggaran Anda memungkinkan, Anda juga dapat memilih mesin baru. Ini adalah pilihan yang baik jika Anda ingin memiliki hardware terbaru dengan kinerja yang baik, terutama jika Anda berencana menggunakan Umbrel atau Start9 dengan aplikasi tambahan di luar ekosistem Bitcoin untuk self-hosting.

### Jenis mesin apa yang harus saya pilih?

#### Mini-PC "NUC" / barebone

Menurut pendapat saya, PC Mini menawarkan pilihan terbaik untuk menjadi host Node Bitcoin di rumah. Hemat ruang, mudah diletakkan di rak, mengonsumsi daya minimal, dan memungkinkan modifikasi hardware yang mudah, seperti menambahkan RAM atau mengganti SSD.

Secara pribadi, saya lebih suka _Lenovo ThinkCentre Tiny_, yang sangat luas di pasar barang bekas (dari barang perusahaan); mesin ini sangat tangguh dan mudah dimodifikasi. Tentu saja, ada banyak produk serupa dari produsen lain: _Dell OptiPlex Micro, HP ProDesk / EliteDesk Mini / Micro, Intel NUC, Gigabyte BRIX, MSI Cubi..._

![Image](assets/fr/001.webp)

**Keunggulan**: hemat ruang, konsumsi daya sedang, kebisingan rendah, skalabilitas (tergantung model), dan keandalan.

**Kelemahan**: Sedikit lebih mahal daripada SBC jenis Raspberry Pi, tidak ada layar bawaan (akses jarak jauh atau melalui monitor eksternal), tidak ada baterai (shutdown mendadak jika listrik padam).

#### Laptop khusus

Ini adalah alternatif berbiaya rendah yang sangat baik untuk PC Mini: saat ini, Anda dapat menemukan laptop bekas atau bahkan baru dengan harga murah, dilengkapi dengan prosesor yang layak, banyak port, serta layar dan keyboard terintegrasi (sangat praktis untuk instalasi awal). Yang terpenting, baterai bertindak sebagai UPS alami: jika terjadi pemadaman listrik, node tidak mati mendadak, dan bahkan dapat tetap beroperasi selama beberapa jam.

![Image](assets/fr/076.webp)

**Keunggulan**: Solusi All-in-one, baterai berfungsi sebagai UPS (tidak ada pemadaman), instalasi lebih sederhana berkat layar dan keyboard terintegrasi, Wi-Fi terintegrasi, dan pilihan pasar bekas dan baru yang luas (yang sering kali berarti Anda dapat membandingkan harga).

**Kelemahan**: Konsumsi daya sedikit lebih tinggi daripada PC Mini tanpa komponen, kerusakan baterai bertahap dalam operasi 24/7 dengan hilangnya kapasitas, risiko pembengkakan baterai atau thermal runaway yang jarang tetapi nyata seiring bertambahnya usia. Aspek inilah yang membuat saya menganggap PC Mini sebagai opsi yang lebih baik daripada laptop: degradasi baterai yang bertahap dan risiko terkait.

Jika Anda memilih solusi ini, saya sarankan untuk mengawasi kondisi baterai dengan cermat untuk mencegah bahaya apa pun. Perhatikan panas berlebih, bau yang tidak biasa, ketidakstabilan, atau hardcase yang berubah bentuk. Jika ada peringatan, segera matikan dan cabut laptop, lalu buang baterai di fasilitas daur ulang khusus.

**Saran**: Jika BIOS/UEFI atau fitur dari pabrikan mengizinkannya, atur batas pengisian (load limit) (misalnya, 60% atau 80%) untuk memperpanjang masa pakai baterai.

#### Raspberry Pi dan SBC lainnya: ide yang salah

Pada awal tahun 2020-an, dengan maraknya perangkat lunak node-in-a-box, kegilaan Raspberry Pi juga muncul sebagai sarana untuk menjalankan Node Bitcoin. Idenya tampak menarik: murah, ringkas, dan mudah diakses.

![Image](assets/fr/073.webp)

Dalam praktiknya, jika tujuan Anda semata-mata menjalankan Node Bitcoin tanpa aplikasi tambahan, Raspberry Pi mungkin sudah cukup. Tetapi begitu Anda ingin menggunakan Umbrel, Start9, atau ekosistem yang lebih kaya (block explorer, address indexer, Node Lightning, aplikasi self-hosting...), mesin tersebut akan cepat mencapai batasnya.

Raspberry Pi memiliki sejumlah kelemahan:

- Prosesor yang terlalu tipis, dengan arsitektur ARM yang terkadang tidak kompatibel dengan perangkat lunak tertentu atau membutuhkan lebih banyak penanganan;
- RAM yang disolder, tidak mungkin ditingkatkan, dengan konfigurasi terbatas (seringkali maksimum 8 GB);
- Kotak eksternal untuk SSD yang terhubung dengan kabel, sumber bug yang sering, membutuhkan pembelian card spesifik untuk SSD yang stabil;
- Kecenderungan untuk cepat panas dan kesulitan dalam memastikan pendinginan yang benar;
- Kebutuhan untuk membeli hardware tambahan (casing, kipas, SSD card, dll.);
- Konektivitas yang sangat terbatas.

Secara historis, keuntungan besar SBC seperti Raspberry Pi adalah harganya: dengan beberapa puluh euro, Anda bisa mendapatkan mesin khusus. Namun, saat ini, harga telah naik tajam, dan setelah Anda menambahkan semua hardware tambahan penting, biayanya mendekati harga PC Mini x86 bekas atau refurbished, yang, menurut saya, menawarkan jauh lebih banyak keuntungan. Karena alasan ini, saya tidak merekomendasikan untuk memilih SBC.

### Memilih komponen

#### Penyimpanan disk: Wajib SSD, minimum 2 TB

Secara teknis, dimungkinkan untuk menjalankan Node Bitcoin pada HDD. Masalahnya adalah semuanya akan melambat secara signifikan, terutama IBD (Initial Block Download), yang akan menjadi sangat lama karena penggunaan disk pada Bitcoin Core yang intensif sebagai cache (terutama untuk set UTXO). Inilah mengapa saya sangat menyarankan untuk tidak menggunakan HDD: ini menciptakan bottleneck nyata, sangat membatasi evolusi di masa depan (misalnya, untuk Node Lightning), dan bahkan dapat menyebabkan ketidaksesuaian sinkronisasi dengan puncak Blockchain. Terlebih lagi, tekanan konstan pada disk mekanis meningkatkan risiko kerusakan dini.

SSD secara radikal mengubah pengalaman pengguna Anda: semuanya menjadi lebih cepat dan lebih lancar, dengan keandalan yang jauh lebih baik. Oleh karena itu, penggunaan SSD adalah (hampir) wajib untuk node Anda, dan Anda tidak akan menyesalinya, terutama karena model berkapasitas tinggi sekarang relatif terjangkau.

![Image](assets/fr/077.webp)

Dalam hal kapasitas, 2TB secara bertahap memantapkan dirinya sebagai minimum yang wajar yang baru. Pada musim panas 2025, Blockchain sudah mendekati 700 GB, dan jika Anda menambahkan Umbrel, address indexer, dan beberapa aplikasi, SSD 1 TB akan segera penuh. Dengan 2TB, Anda memiliki margin yang nyaman untuk tahun-tahun mendatang (dalam perkiraan luas, antara 5 hingga 15 tahun). Anda juga dapat memilih 4TB jika Anda berencana menggunakan banyak aplikasi di Umbrel, menyimpan file besar dalam self-hosting, atau jika Anda ingin mengantisipasi kebutuhan ruang disk Anda yang membesar.

![Image](assets/fr/078.webp)

Mengenai formatnya, ini akan bergantung pada port yang tersedia di mesin Anda; namun, jika memungkinkan, saya merekomendasikan penggunaan NVMe M.2 SSD.

#### Memori (RAM): 8 hingga 16 GB

Untuk Bitcoin Core saja (tanpa overlay Umbrel), rekomendasi pengembang menunjukkan minimum 256 MB RAM dengan pengaturan disesuaikan ke pengaturan terendah, 512 MB dengan pengaturan default, dan 1 GB untuk penggunaan normal.

Di sisi lain, jika Anda menggunakan sistem node-in-a-box seperti Umbrel atau Start9, persyaratan RAM secara signifikan lebih tinggi. Pengembang Umbrel merekomendasikan minimum 4 GB RAM. Ini mungkin cukup untuk menjalankan Core saja, tetapi Anda akan segera terbatas. Oleh karena itu, mereka merekomendasikan 8 GB, yang juga saya anggap minimum untuk konfigurasi dasar di sekitar Bitcoin (Core, LND, indexer, dan beberapa aplikasi). Dalam pengalaman saya, dengan Umbrel dan beberapa layanan tambahan, 8 GB masih kurang nyaman. Agar benar-benar nyaman dan memiliki sedikit margin, saya merekomendasikan 16 GB RAM.

#### Prosesor (CPU)

Untuk node Umbrel, persyaratan minimum adalah prosesor dual-core 64-bit dari Intel atau AMD. Jika Anda ingin menggunakan beberapa aplikasi selain Bitcoin Core, quad-core (atau lebih tinggi) akan membuat perbedaan nyata dalam hal kelancaran. Misalnya, prosesor i5/i7 generasi ke-6 hingga ke-10 adalah pilihan yang sangat baik di pasar bekas.

### Contoh konfigurasi konkret

Di bawah ini, saya mengusulkan tiga konfigurasi nyata, disesuaikan dengan anggaran dan kebutuhan yang berbeda, dengan model yang tepat untuk mendukungnya. Pilihan ini disediakan sebagai contoh untuk mengilustrasikan informasi dalam bab ini; Anda tidak wajib memilih model-model ini secara persis. Karena saya menganggap PC Mini sebagai opsi terbaik dalam jangka panjang, saya akan mengandalkan format ini untuk tiga konfigurasi yang diusulkan.

_Harga yang ditampilkan di bawah ini hanya perkiraan saja dan dapat bervariasi sesuai dengan wilayah, vendor, dan periode_

Yang pertama dan terpenting, Anda memerlukan SSD yang cukup besar untuk menampung Blockchain, sementara masih menyisakan ruang untuk bermanuver. SSD memiliki masa pakai terbatas dalam hal siklus tulis dan volume total data yang ditulis. Namun, Node Bitcoin memberikan beban yang signifikan pada disk saat menulis. Itulah mengapa saya tidak merekomendasikan model entry-level; sebaliknya, saya menyarankan NVMe SSD, yang menawarkan kinerja yang jauh lebih baik.

Sebagai contoh, untuk tujuan kursus ini, saya telah memilih model berikut: Samsung 990 EVO Plus NVMe M.2 SSD 2Tb, tersedia dengan harga sekitar €120 di Amazon. Anda juga dapat memilih merek terkenal lainnya seperti Crucial, Western Digital, atau Kingston.

![Image](assets/fr/046.webp)

#### Konfigurasi anggaran rendah

Jelas, jika anggaran Anda sangat terbatas (di bawah €200), saya menyarankan Anda untuk tidak berinvestasi pada mesin khusus, tetapi lebih baik memasang Bitcoin Core langsung di PC sehari-hari Anda (pruned mode jika Anda kekurangan ruang disk).

Jika tidak, untuk anggaran entry-level, saya merekomendasikan _HP EliteDesk 800 G2 Mini_. Saya menemukan model refurbished seharga €96 di Amazon, dilengkapi dengan prosesor Intel Core i5 generasi ke-6 dan RAM 8 GB. Ini adalah pilihan yang sangat menarik untuk pemula: prosesor ini dan jumlah memori ini lebih dari cukup untuk menjalankan Core pada Umbrel, serta beberapa aplikasi secara bersamaan, seperti indexer Electrs, Node Lightning, dan instance Mempool, asalkan Anda tidak mengalokasikan terlalu banyak cache ke Core. Terlebih lagi, jenis PC Mini ini memudahkan untuk meningkatkan RAM menjadi 16 GB, misalnya, jika kebutuhan muncul (perkirakan biaya tambahan sekitar €30-40 untuk satu atau dua keping memori berkualitas).

![Image](assets/fr/045.webp)

Kemudian cukup tambahkan SSD ke dalam anggaran. Dimulai dengan Samsung 2TB seharga €120, kami mendapatkan biaya total €216 untuk mesin lengkap dan berfungsi.

#### Konfigurasi anggaran menengah

Jika Anda memiliki anggaran rata-rata sekitar €300 untuk mesin yang akan menjadi host node Anda, saya merekomendasikan _Lenovo ThinkCentre Tiny_, misalnya, dilengkapi dengan prosesor berkinerja tinggi dan RAM yang memadai. Saya menemukan model refurbished di Amazon seharga €180, menampilkan prosesor Intel Core i7 generasi ke-6 dan RAM 16GB. Dengan tambahan SSD 2TB seharga €120, total biaya menjadi €300.

![Image](assets/fr/044.webp)

Dengan mesin ini, Anda memiliki konfigurasi yang nyaman: IBD yang cepat dan kemampuan untuk menjalankan banyak aplikasi di Umbrel atau Start9 Anda tanpa kesulitan. Inilah tepatnya konfigurasi yang saya gunakan untuk kursus BTC 202 ini.

#### Konfigurasi High-End

Dengan anggaran yang lebih besar, kemungkinannya menjadi jauh lebih luas. Anda dapat memilih konfigurasi DIY, atau bahkan memilih mesin rakitan awal yang ditawarkan langsung oleh proyek node-in-a-box.

Misalnya, _ASUS NUC 14 Pro_ tersedia baru dari Amazon seharga €540. Untuk harga ini, Anda mendapatkan prosesor Intel Core Ultra 5 (baru dan berkinerja sangat tinggi), disertai dengan RAM DDR5 16 GB. Dengan konfigurasi seperti itu, Anda akan dapat menyelesaikan IBD dalam waktu singkat dan memasang aplikasi yang berat tanpa kesulitan.

Ini adalah konfigurasi yang sangat nyaman, bahkan berlebihan jika tujuan awalnya hanya menjalankan Node Bitcoin. Di sisi lain, jika Anda ingin memanfaatkan sepenuhnya semua aplikasi self-hosting yang tersedia di Umbrel dan Start9, pilihan ini tepat untuk Anda.

![Image](assets/fr/043.webp)

Tergantung pada penggunaan yang Anda inginkan, Anda dapat memilih SSD 2TB, seperti dalam konfigurasi lain, atau langsung untuk SSD 4TB seharga €260 jika Anda juga ingin menyimpan file pribadi dan memperluas penggunaan self-hosting Anda. Dengan SSD 2TB, total biaya konfigurasi adalah €660, sedangkan dengan SSD 4TB, mencapai €800.

### Beberapa kiat tambahan

- Jika Anda ingin membeli peralatan bekas dan membayar dengan bitcoin, datanglah ke pertemuan di dekat Anda! Dengan mengobrol dengan peserta lain, Anda pasti akan menemukan peralatan yang cocok dengan harga yang bagus, sambil membantu menjaga ekonomi sirkular di sekitar Bitcoin tetap hidup. Ini juga merupakan kesempatan untuk mendapatkan saran yang baik dari komunitas.
- Untuk koneksi Internet, Anda tentu saja akan membutuhkan kabel Ethernet RJ45, setidaknya untuk instalasi sistem.
- Beberapa environment, seperti Umbrel, memungkinkan Anda menggunakan Wi-Fi, tetapi kinerjanya umumnya akan lebih buruk (terutama jika Anda ingin menggunakan Node Lightning Anda dari jarak jauh, karena ini dapat berdampak). Jika Anda memilih Wi-Fi, pastikan mesin Anda memiliki build-in card atau tambahkan dongle yang kompatibel.
- Selalu gunakan power supply pabrikan asli untuk mesin Anda. Ini sangat penting untuk mencegah kerusakan pada peralatan Anda dan untuk mencegah risiko kebakaran.
- Jika mesin Anda tidak memiliki baterai bawaan, ada baiknya berinvestasi pada inverter (UPS) untuk menghindari shutdown mendadak.
- Tergantung pada nilai peralatan Anda dan lokasi geografis Anda, sistem penangkal petir juga mungkin tepat, baik langsung di panel sakelar (switchboard) atau pada soket listrik yang digunakan.
- Terakhir, ingatlah untuk mengoptimalkan pendinginan mesin Anda: bersihkan secara teratur, dan pasang di tempat yang sejuk, berventilasi baik, dan tidak berantakan untuk menghindari panas berlebih, yang dapat menyebabkan throttling (pembatasan kecepatan prosesor Anda secara otomatis).



# Memasang node Bitcoin dengan mudah


<partId>ca6cf2a5-0bcc-41d9-b556-0d38865bf98f</partId>




## Umbrel: lebih dari sekadar simpul Bitcoin


<chapterId>dd4c04f1-924a-43e1-94f3-ea9fbc83dd43</chapterId>



Umbrel adalah sistem operasi server pribadi yang dirancang untuk membuat hos mandiri dapat diakses: Anda menginstal Umbrel, membuka peramban di `umbrel.local`, dan mengelola segala sesuatunya melalui Interface jarak jauh yang sederhana.



Proyek ini pertama kali mempopulerkan ide Bitcoin dan Lightning node satu-klik, kemudian diperluas menjadi "cloud rumah" yang sesungguhnya: penyimpanan file dan foto, streaming multimedia, alat jaringan, otomatisasi rumah, AI lokal, dan ratusan aplikasi yang dapat diinstal dari App Store yang terintegrasi.



Di Umbrel, setiap aplikasi berjalan dalam kontainer Docker (isolasi, pembaruan atomik, start/stop independen). Interface memusatkan akses ke semua aplikasi ini, menawarkan sistem masuk tunggal (dengan 2FA opsional), pembaruan sekali klik untuk OS dan aplikasi, pemantauan langsung mesin (CPU, RAM, suhu, penyimpanan), manajemen perizinan di antara aplikasi, dan ikhtisar konsumsinya.



Oleh karena itu, tujuan Umbrel adalah untuk memberi Anda kembali kendali dan kerahasiaan atas data Anda, tanpa bergantung pada layanan cloud, lebih dari sekadar mengoperasikan node Bitcoin.



### Umbrel Home vs umbrelOS



Umbrel menawarkan dua pendekatan yang berbeda:





- [**Umbrel Home**](https://umbrel.com/umbrel-home): ini adalah server mini yang siap pakai, yang dirancang dan dioptimalkan secara khusus untuk umbrelOS. Ringkas, senyap, terhubung dengan Ethernet, dilengkapi dengan SSD NVMe (opsional hingga 4TB), RAM 16GB, dan CPU quad-core. Anda memesannya, mencolokkannya, dan membuka `umbrel.local`. Anda bisa memiliki Umbrel yang operasional dan berjalan dalam hitungan menit. Itu adalah opsi plug-and-play.



![Image](assets/fr/081.webp)





- [**umbrelOS**](https://umbrel.com/umbrelos): ini adalah sistem operasi yang dapat Anda instal sendiri pada perangkat keras Anda sendiri (mini-PC, NUC, tower, laptop khusus...). Anda memiliki Interface yang sama dan App Store yang sama seperti pada Umbrel Home.



![Image](assets/fr/080.webp)



Dalam kedua kasus tersebut, pengalaman pengguna identik di sisi perangkat lunak: administrasi berbasis browser, pembaruan sekali klik, instalasi aplikasi sesuai permintaan... Solusi DIY sering kali lebih ekonomis daripada membeli Umbrel Home (tergantung pada mesin yang digunakan). Namun, saya tidak akan selalu menyarankan Anda untuk memilih opsi DIY, karena **membeli Umbrel Home berkontribusi langsung pada pembiayaan pengembangan proyek**, karena model bisnisnya didasarkan pada penjualan perangkat keras. Dan sejujurnya, dengan harga €389 untuk penyimpanan 2TB, harga tersebut masih sangat masuk akal mengingat kualitas mesin yang ditawarkan.



![Image](assets/fr/079.webp)



Di bab selanjutnya, kita akan membahas cara menginstal umbrelOS secara DIY di mesin Anda sendiri. Namun, Anda dapat mengikuti kursus BTC 202 ini dengan cara yang sama jika Anda telah memilih Umbrel Home.



### Kasus penggunaan: dari node Bitcoin ke cloud rumah



Umbrel dapat tetap sangat minimalis dan hanya berfokus pada Bitcoin, atau berevolusi menjadi server pribadi multifungsi yang sesungguhnya, tergantung pada kebutuhan Anda. Berikut ini adalah kegunaan utama Umbrel:





- Node Bitcoin sederhana**: ini adalah penggunaan awal yang menjadi andalan Umbrel sejak awal. Anda dapat menjalankan Bitcoin core (atau Knot), menghubungkan dompet Anda secara langsung ke node Anda, mengekspos server Electrum, meng-host Mempool Block explorer Anda untuk melihat Blockchain, dan memperkirakan biaya... Penggunaan-penggunaan inilah yang akan kita fokuskan dalam kursus ini.



![Image](assets/fr/082.webp)





- Lightning Network**: Umbrel juga memungkinkan Anda menggunakan LND atau Core Lightning, dua implementasi dari Lightning Network, untuk mengelola node Lightning Anda sendiri. Anda akan dapat membuka saluran, mengelola likuiditas, melakukan pembayaran, mengotomatiskan penyeimbangan, menawarkan layanan, menghubungkan Wallet jarak jauh, atau memanfaatkan manajemen Interface tingkat lanjut berkat banyak aplikasi yang tersedia. Kita akan melihat kasus penggunaan khusus ini dalam kursus LNP 202 berikutnya.



![Image](assets/fr/083.webp)





- Hosting mandiri umum**: dengan Nextcloud, Immich, Jellyfin/Plex, pemblokir iklan di seluruh DNS (Pi-hole/AdGuard), VPN (WireGuard, Tailscale), otomatisasi rumah (Asisten Rumah Tangga), pencadangan, manajemen catatan, alat kantor, AI lokal (Ollama + Open WebUI)... Umbrel dapat menjadi server pribadi Anda, memungkinkan Anda untuk mendapatkan kembali kendali atas data Anda. Anda meng-host sendiri layanan yang Anda gunakan setiap hari, dengan pengalaman pengguna yang dipoles yang sangat mirip dengan solusi eksternal, sambil mempertahankan kontrol penuh atas data dan privasi Anda.



Dengan men-deploy aplikasi dalam kontainer, Anda dapat membentuk Umbrel sesuai keinginan: mulai dengan node Bitcoin sederhana dan beberapa aplikasi yang ditautkan ke ekosistemnya, lalu instal node Lightning di samping node Bitcoin, dan secara bertahap memperkaya instance Anda dengan aplikasi hosting mandiri yang Anda perlukan.



### Komunitas dan gotong royong



Salah satu keunggulan utama Umbrel dibandingkan para pesaingnya adalah komunitas penggunanya yang luas dan sangat aktif. Anda bisa menjangkau mereka terutama melalui [Discord mereka](https://discord.gg/efNtFzqtdx) dan [forum online mereka](https://community.umbrel.com/). Di sini, Anda tidak hanya akan menemukan saran praktis tetapi, di atas segalanya, solusi untuk memecahkan masalah atau memperbaiki bug. Ini adalah tempat yang tepat untuk memulai, berkembang, dan pada akhirnya, membantu pengguna lain, sehingga Anda tidak akan merasa kesepian dengan Coin Anda.



![Image](assets/fr/084.webp)



### Lisensi UmbrelOS



Kode Umbrel tersedia untuk umum (Anda dapat melihat, Fork, dan memodifikasinya), tetapi tidak berada di bawah lisensi sumber terbuka yang sebenarnya. Faktanya, umbrelOS didistribusikan di bawah lisensi [*PolyForm Noncommercial 1.0*](https://polyformproject.org/licenses/noncommercial/1.0.0/), meskipun beberapa alat pengembangan terkait tersedia di bawah lisensi MIT.



Secara praktis, Anda bisa melakukan hampir semua hal yang Anda suka dengan umbrelOS, selama itu untuk penggunaan pribadi dan non-komersial: modifikasi, redistribusi untuk tujuan nirlaba, pembuatan turunan untuk Anda sendiri atau untuk organisasi nirlaba, asalkan Anda menghormati pemberitahuan hukum.



Namun, dilarang menjual Umbrel atau turunannya (misalnya, mesin yang sudah dirakit dengan UmbrelOS yang sudah diinstal sebelumnya), menawarkan layanan yang terkait dengan Umbrel secara komersial, atau mengintegrasikan kodenya ke dalam sebuah produk untuk mendapatkan keuntungan.



Secara teknis, lisensi ini tidak membatasi instalasi, audit, atau adaptasi Umbrel untuk penggunaan pribadi. Secara hukum, lisensi ini melindungi proyek dari penjualan kembali atau hosting komersial yang tidak sah, terutama oleh penyedia layanan cloud. Oleh karena itu, Umbrel bukanlah sumber terbuka, meskipun kodenya tetap dapat diakses oleh publik.



Namun, setiap aplikasi di Store mempertahankan lisensinya sendiri, sering kali bersifat open source.




## Memasang Full node dengan Umbrel


<chapterId>61bc09c7-787d-4649-b142-457ec018b0f4</chapterId>



Sekarang setelah kita memiliki semua informasi yang diperlukan, sekarang saatnya untuk mempelajari detailnya. Dalam tutorial ini, kami akan menunjukkan kepada Anda cara menginstal node Bitcoin secara lengkap menggunakan UmbrelOS.



### Bahan yang dibutuhkan



Di sini, kita akan menggunakan image UmbrelOS x86 (lebih tepatnya, versi x86_64). Anda bisa mengikuti panduan ini pada mesin apa pun yang Anda pilih, asalkan tidak dilengkapi dengan prosesor berarsitektur ARM (bukan Apple Silicon, Raspberry Pi, dll.). Ini berarti bahwa komputer apa pun dengan prosesor Intel atau AMD 64-bit sudah cukup, selama memenuhi persyaratan minimum, tergantung pada bagaimana Anda ingin menggunakan Umbrel Anda (setidaknya disarankan prosesor dual-core).



Jika Anda memilih Raspberry Pi 5 (opsi yang tidak saya rekomendasikan, seperti yang disebutkan di bagian sebelumnya), penginstalannya sedikit berbeda. Anda kemudian dapat mengikuti tutorial khusus ini dan kembali ke kursus saya sekali di web Interface `http://umbrel.local`:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Seperti yang telah disebutkan di bagian sebelumnya, saya memilih untuk menjalankan tutorial ini di sebuah PC kecil yang telah diperbaharui yang saya temukan dengan harga terjangkau: *Lenovo ThinkCentre M900 Tiny* yang dilengkapi dengan prosesor Intel Core i7 dan RAM 16 GB. Ini adalah konfigurasi yang sangat nyaman untuk menjalankan Umbrel, terutama untuk node Bitcoin. Namun, saya memilih konfigurasi ini karena saya ingin memasang node Lightning dan aplikasi lain yang lebih berat nantinya. Saya juga menambahkan SSD 2TB ke ThinkCentre saya untuk mempertahankan Blockchain secara penuh dan masih memiliki margin yang nyaman. Dengan konfigurasi ini, total biaya yang dikeluarkan adalah €270, sudah termasuk semua pengeluaran.



![Image](assets/fr/001.webp)



Saya sangat menyukai jajaran ThinkCentre Tiny dari Lenovo, karena mereka adalah mesin yang ringkas, tidak berisik, dan sangat kuat. Komputer-komputer ini sangat populer di kalangan bisnis dan oleh karena itu berlimpah di pasar barang bekas, di mana Anda bisa menemukan konfigurasi menarik antara €70 dan €200.



Jika, seperti saya, Anda memilih PC tanpa monitor, **Anda hanya perlu menyambungkan monitor dan keyboard** selama proses instalasi. Setelah itu, Anda akan dapat mengaksesnya dari jarak jauh dari komputer lain di jaringan yang sama (atau melalui metode lain yang akan kita bahas di bab selanjutnya). Anda juga memerlukan kabel Ethernet RJ45 untuk menghubungkan mesin Anda ke jaringan lokal, dan kunci USB minimal 4 GB untuk menyimpan image instalasi.



Sebagai rangkuman, berikut ini adalah persyaratan peralatannya:




- Komputer dengan prosesor x86_64 (minimal Dual-core, disarankan Quad-core);
- Memori RAM (minimum 4 GB, disarankan 8 GB atau lebih untuk penggunaan yang lama);
- SSD (disarankan + 2 TB);
- Kunci USB (+ 4 GB) untuk penginstalan citra UmbrelOS;
- Monitor dan keyboard (hanya berguna untuk instalasi awal jika PC tidak dilengkapi dengan monitor);
- Kabel Ethernet RJ45.



### Langkah 1 - Memasang komputer



Tergantung pada perangkat keras yang Anda pilih, langkah pertama adalah merakit berbagai komponen komputer Anda. Sebagai contoh, dalam kasus saya, SSD asli hanya berkapasitas 256 GB, jadi saya akan mendaur ulang untuk penggunaan lain dan menggantinya dengan SSD 2 TB. Jika Anda juga ingin mengganti modul RAM, sekaranglah saatnya untuk melakukannya.



### Langkah 2: Siapkan kunci USB yang dapat di-boot



Sebelum menginstal UmbrelOS pada mesin Anda, Anda perlu membuat kunci USB yang dapat di-boot yang berisi sistem operasi. Semua langkah pada langkah 2 harus dilakukan pada komputer pribadi Anda (dan tidak langsung pada komputer yang akan menjadi node Anda).





- Mulailah dengan mengunduh versi terbaru UmbrelOS dalam format USB:



Kunjungi [situs web resmi Umbrel untuk mengunduh citra ISO](https://download.umbrel.com/release/latest/umbrelos-amd64-usb-installer.iso) untuk instalasi melalui kunci USB. Pastikan Anda memilih versi yang kompatibel dengan arsitektur x86_64 (file bernama `umbrelos-amd64-usb-installer.iso`). Pengunduhan mungkin memerlukan waktu, karena gambarnya cukup besar.



![Image](assets/fr/002.webp)





- Pasang Balena Etcher:



Untuk membuat stik USB yang dapat di-booting, Anda akan menggunakan alat sederhana lintas platform yang disebut [Balena Etcher](https://www.balena.io/etcher/). Unduh dan instal di komputer Anda.



![Image](assets/fr/003.webp)





- Masukkan kunci USB kosong minimal 4 GB:



Colokkan kunci USB ke komputer Anda (komputer yang baru saja mengunduh gambar UmbrelOS dan Balena Etcher). **Peringatan: semua data pada kunci akan terhapus**. Pastikan kunci tersebut tidak berisi file penting.





- Bakar citra ISO ke stik USB dengan Balena Etcher:



Luncurkan Balena Etcher dan pilih file ISO `umbrelos-amd64-usb-installer.iso` yang baru saja Anda unduh dengan mengeklik tombol "*Flash from file*". Kemudian, pilih kunci USB sebagai perangkat target dan klik "*Flash!*" untuk mulai menulis.



![Image](assets/fr/004.webp)



Setelah operasi selesai, Anda akan memiliki kunci USB yang dapat di-boot yang berisi UmbrelOS, siap untuk mem-boot dan menginstal Umbrel di mesin Anda.



![Image](assets/fr/005.webp)



### Langkah 3: Mem-boot komputer dari kunci USB



Sekarang stik USB yang dapat di-boot yang berisi UmbrelOS telah siap, Anda dapat mem-boot komputer Anda ke stik USB tersebut untuk memulai instalasi sistem. Cabut kunci USB dari komputer utama Anda dan masukkan ke dalam perangkat tempat Anda ingin menginstal Umbrel dan node Bitcoin.



Seperti yang dijelaskan di awal bab ini, untuk menyelesaikan instalasi, Anda memerlukan perangkat tampilan dan perangkat input. Hubungkan layar melalui HDMI (atau port lain, tergantung pada PC Anda) dan sambungkan keyboard melalui USB ke komputer Anda. Perangkat-perangkat ini hanya diperlukan untuk instalasi; Anda tidak akan memerlukannya setelah itu, karena Umbrel akan diakses dari jarak jauh dari komputer lain. Hubungkan kedua perangkat ini ke PC Anda.



**Saran:** Jika Anda tidak memiliki layar periferal di rumah, Anda bisa menggunakan TV. Dengan input HDMI (atau lainnya), ini bisa digunakan sebagai layar sementara sementara Anda menginstal sistem operasi.



Umbrel jelas membutuhkan koneksi Internet. Sambungkan kabel Ethernet RJ45 antara perangkat Anda dan router.



![Image](assets/fr/006.webp)



Nyalakan mesin Anda. Pada sebagian besar kasus, komputer akan secara otomatis mendeteksi kunci USB dan melakukan booting. Anda kemudian akan melihat layar instalasi UmbrelOS Interface muncul.



Jika perangkat melakukan booting pada sistem lain atau menampilkan pesan kesalahan, ini mungkin berarti perangkat tidak melakukan booting secara otomatis dari kunci USB. Dalam kasus ini, boot ulang dan masuk ke pengaturan BIOS/UEFI (biasanya diakses dengan menekan `DEL`, `F2`, `F12`, atau `ESC`, tergantung pada produsen komputer). Kemudian, ubah urutan boot untuk memprioritaskan kunci USB. Kemudian hidupkan ulang perangkat untuk meluncurkan UmbrelOS.



### Langkah 4: Instal UmbrelOS di komputer Anda



Setelah perangkat melakukan booting dari stik USB, Anda akan disambut oleh instalasi Interface UmbrelOS. Langkah ini melibatkan penginstalan sistem secara langsung ke disk Hard internal mesin Anda.



Layar yang muncul berisi daftar semua perangkat penyimpanan internal yang terdeteksi oleh komputer. Setiap disk disertai dengan nomor, nama, dan kapasitas penyimpanan. Cari disk tempat Anda ingin menginstal Umbrel. **Peringatan: semua file pada disk ini akan dihapus secara permanen.**



![Image](assets/fr/007.webp)



Setelah Anda mengidentifikasi disk yang benar (biasanya disk dengan kapasitas terbesar, untuk menampung Blockchain), catat nomor yang ditetapkan untuk disk tersebut. Sebagai contoh, jika disk yang Anda pilih muncul di bawah nomor `2`, cukup masukkan `2`, kemudian tekan tombol `Enter` pada keyboard.



![Image](assets/fr/008.webp)



Program ini akan memformat disk yang dipilih, menginstal UmbrelOS, dan secara otomatis mengkonfigurasi sistem. Ini mungkin memerlukan waktu beberapa menit. Biarkan proses berjalan tanpa gangguan.



![Image](assets/fr/009.webp)



Setelah penginstalan selesai, Anda akan diminta untuk mematikan perangkat. Tekan sembarang tombol untuk mematikan komputer.



![Image](assets/fr/010.webp)



Anda sekarang dapat melepas kunci USB, keyboard, dan layar, yang tidak lagi diperlukan untuk Umbrel Anda. Yang tersisa dari node Anda hanyalah daya Supply dan kabel Ethernet RJ45.



![Image](assets/fr/011.webp)



Sebelum menghidupkan ulang perangkat, periksa dua hal berikut ini:





- Kunci USB dicabut**: jika tetap tersambung, sistem mungkin akan melakukan boot ulang dan bukannya menggunakan disk internal;
- Kabel Ethernet dicolokkan**: perangkat harus tersambung ke router agar dapat beroperasi.



Tekan tombol daya. Sistem akan melakukan booting secara otomatis dari disk internal tempat UmbrelOS diinstal. Booting pertama mungkin memerlukan waktu sekitar **5 menit**. Selama waktu ini, Umbrel akan menginisialisasi layanan dan Interface.



Dari komputer lain (PC yang Anda gunakan sehari-hari) yang terhubung ke **jaringan lokal yang sama**, buka peramban web (Firefox, Chrome...) dan buka:



```
http://umbrel.local
```



Address ini digunakan untuk mengakses pengguna grafis Umbrel Interface dari jarak jauh dan memulai konfigurasi.



Jika Address `http://umbrel.local` tidak berfungsi pada browser Anda setelah menunggu setidaknya 5 menit, coba saja:



```
http://umbrel
```



Jika ini masih tidak berhasil, masukkan IP lokal Umbrel Anda Address langsung ke peramban. Sebagai contoh (ganti `42` dengan nomor mesin Anda yang menghosting Umbrel pada jaringan lokal):



```
http://192.168.1.42
```



Untuk mengidentifikasi IP Address Umbrel Anda, ada beberapa metode, dari yang paling sederhana hingga yang paling canggih:





- Akses administrasi router Anda Interface dan temukan IP Address perangkat Umbrel di jaringan lokal.





- Gunakan perangkat lunak pemindaian jaringan seperti Angry IP Scanner untuk mendeteksi perangkat yang terhubung dan menemukan IP Umbrel Address Anda.



![Image](assets/fr/012.webp)



https://planb.academy/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d



- Sebagai upaya terakhir, sambungkan kembali monitor dan keyboard ke perangkat, masuk (login default: `umbrel`, kata sandi: `umbrel`), lalu ketik perintah berikut:



```
hostname -I
```



Sekarang Anda siap menggunakan Umbrel!



### Langkah 5: Memulai dengan Umbrel



Untuk mulai mengkonfigurasi Umbrel Anda, klik tombol "*Start*".



![Image](assets/fr/013.webp)



#### Membuat akun



Pilih nama samaran atau masukkan nama Anda, lalu tetapkan kata sandi yang kuat. Hati-hati: kata sandi ini merupakan satu-satunya penghalang yang melindungi akses ke Umbrel Anda dari jaringan Anda (dan oleh karena itu, berpotensi juga untuk bitcoin Anda jika Anda menjalankan node Lightning di Umbrel). Kata sandi ini juga melindungi akses jarak jauh melalui Tor atau VPN, jika layanan ini diaktifkan.



Pilih kata sandi yang kuat dan pastikan Anda menyimpan setidaknya satu cadangan (disarankan menggunakan pengelola kata sandi).



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.academy/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Setelah Anda memasukkan kata sandi, klik tombol "*Buat*".



![Image](assets/fr/014.webp)



Konfigurasi Umbrel Anda sekarang sudah selesai.



![Image](assets/fr/015.webp)



#### Penemuan Interface



Interface dari Umbrel cukup intuitif:





- Pada halaman beranda, Anda dapat melihat aplikasi dan widget yang terinstal.



![Image](assets/fr/016.webp)





- "*App Store*" memungkinkan Anda menginstal aplikasi baru,



![Image](assets/fr/017.webp)





- Menu "*Files*" memusatkan semua dokumen yang tersimpan di Umbrel Anda.



![Image](assets/fr/018.webp)





- Menu "*Pengaturan*" memungkinkan Anda memodifikasi pengaturan Umbrel dan mengakses informasinya, termasuk:
    - Memperbarui, memulai ulang, atau menghentikan mesin Anda;
    - Konsultasikan ruang penyimpanan yang tersedia, penggunaan RAM, dan suhu prosesor;
    - Mengubah wallpaper;
    - Kelola akses jarak jauh melalui Tor, aktifkan Wi-Fi, atau 2FA.



![Image](assets/fr/019.webp)



#### Pengaturan keamanan dan koneksi



Pertama dan terutama, saya sangat menyarankan untuk mengaktifkan autentikasi dua faktor (2FA). Ini akan menambah keamanan ekstra Layer pada kata sandi Anda. Ini hampir sangat diperlukan jika Anda berencana untuk menggunakan Umbrel Anda untuk menyimpan berkas pribadi, menjalankan simpul Lightning, atau melakukan aktivitas sensitif lainnya.



https://planb.academy/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Untuk melakukan ini, klik pada kotak yang sesuai dalam pengaturan.



![Image](assets/fr/020.webp)



Kemudian pindai kode QR yang ditampilkan menggunakan aplikasi autentikasi Anda. Kemudian masukkan kode dinamis 6 digit di bidang yang disediakan pada Umbrel Anda.



Mulai sekarang, setiap koneksi baru ke Umbrel Anda akan memerlukan kata sandi dan kode 6 digit yang dihasilkan oleh aplikasi autentikasi dua faktor (2FA).



![Image](assets/fr/021.webp)



Mengenai akses jarak jauh melalui Tor, jika Anda tidak memerlukannya, saya sarankan untuk membiarkan opsi ini dinonaktifkan untuk membatasi permukaan serangan Umbrel Anda. Secara default, simpul Anda hanya dapat diakses dari mesin yang tersambung ke jaringan lokal yang sama. Mengaktifkan akses melalui Tor akan memungkinkan Anda untuk mengelola Umbrel Anda saat bepergian.



Jika Anda mengaktifkan fitur ini, secara teoritis memungkinkan mesin apa pun di dunia ini untuk mencoba koneksi ke simpul Anda, asalkan mesin tersebut mengetahui Tor Address. Namun, kata sandi dan 2FA Anda akan tetap melindungi Anda.



Jika Anda mengaktifkan opsi ini, pastikan Anda mengaktifkan autentikasi dua faktor (2FA), kata sandi yang kuat, dan jangan pernah mengungkapkan koneksi Tor Anda Address.



Cukup masukkan Tor Address ini dalam peramban Tor Anda untuk mengakses Interface Umbrel dari jaringan mana pun.



![Image](assets/fr/026.webp)



Terakhir, pada halaman pengaturan ini, Anda juga dapat mengaktifkan koneksi Wi-Fi. Jika mesin yang menghosting Umbrel memiliki kartu jaringan Wi-Fi atau dongle Wi-Fi, ini memungkinkan Anda mengakses Internet tanpa menggunakan kabel RJ45. Namun, tergantung pada konfigurasi Anda, solusi ini dapat memperlambat koneksi, yang dapat memengaruhi sinkronisasi awal (IBD) dan penggunaan node di masa mendatang (misalnya, untuk transaksi Lightning). Secara pribadi, saya tidak menyarankan opsi ini, karena node tidak dimaksudkan untuk penggunaan seluler: node selalu diakses dari jarak jauh, jadi sebaiknya Anda membiarkannya tetap terhubung.



### Langkah 6: Pasang node Bitcoin pada Umbrel



Setelah UmbrelOS terinstal dan terkonfigurasi dengan benar di komputer Anda, Anda bisa melanjutkan dengan menginstal node Bitcoin. Tidak ada yang lebih sederhana: buka App Store, buka kategori "*Bitcoin*", lalu pilih aplikasi "*Bitcoin Node*" (sebenarnya adalah Bitcoin core).



![Image](assets/fr/022.webp)



Kemudian klik tombol "*Instal*".



![Image](assets/fr/023.webp)



Setelah instalasi selesai, node Bitcoin Anda akan meluncurkan IBD (*Initial Block Download*): node ini akan mengunduh dan memvalidasi semua transaksi dan blok sejak Bitcoin dibuat pada tahun 2009.



![Image](assets/fr/024.webp)



Tahap ini sangat memakan waktu, karena durasinya tergantung pada beberapa faktor, termasuk jumlah RAM yang dialokasikan ke cache node, kecepatan disk, kecepatan koneksi Internet, dan daya prosesor. Oleh karena itu, rentang durasinya sangat luas, tergantung pada konfigurasinya. Dengan PC berkinerja tinggi (SSD NVMe, RAM +32 GB, prosesor yang kuat, dan koneksi Internet yang baik), IBD dapat diselesaikan dalam waktu sekitar sepuluh jam. Di sisi lain, prosesor lama, RAM rendah, atau, lebih buruk lagi, disk Hard mekanis (sangat tidak disarankan) dapat memperpanjang operasi ini hingga beberapa minggu.



Dengan PC dengan konfigurasi normal (prosesor yang layak, RAM 8 hingga 16 GB, dan SSD), waktu yang dibutuhkan sekitar 2 hingga 7 hari.



Untuk sedikit mempercepat IBD, Anda dapat meningkatkan RAM yang dialokasikan ke cache node (terutama digunakan untuk set UTXO, yang akan kita bahas nanti dalam kursus) melalui parameter `dbcache`. Pada Umbrel, modifikasi ini dilakukan pada parameter node Anda, pada tab "*Optimization*".



![Image](assets/fr/025.webp)



Secara default, nilai parameter `dbcache` di Bitcoin core diatur ke 450 MiB, atau sekitar 472 MB. Dengan meningkatkan nilai ini, Anda dapat sedikit mempercepat IBD. Namun, saya tidak menyarankan untuk mendorong parameter ini terlalu tinggi: bahkan mengaturnya ke 4 GiB hanya akan membuat sinkronisasi sekitar 10% lebih cepat, dan dapat menyebabkan Anda kehilangan waktu jika terjadi gangguan selama IBD.



Berhati-hatilah untuk tidak mengalokasikan nilai yang terlalu besar untuk mesin Anda. Jika RAM yang tersedia untuk UmbrelOS habis, simpul Anda mungkin berhenti tiba-tiba, mengganggu IBD dan mengharuskan Anda memulai ulang secara manual, yang mengakibatkan hilangnya banyak waktu.



Untuk mengetahui lebih lanjut tentang dampak parameter `dbcache` pada sinkronisasi awal, saya merekomendasikan analisis ini oleh Jameson Lopp: [*Pengaruh Ukuran DBcache pada Kecepatan Sinkronisasi Node Bitcoin*](https://blog.lopp.net/effects-dbcache-size-Bitcoin-node-sync-speed/)



Setelah IBD node Anda selesai (sinkronisasi 100%), Anda sekarang memiliki node Bitcoin yang beroperasi penuh. Selamat, Anda sekarang menjadi bagian integral dari jaringan Bitcoin!



![Image](assets/fr/027.webp)



Pada bagian selanjutnya, kita akan membahas penggunaan praktis dari node baru Anda: bagaimana menghubungkan Wallet Anda ke node tersebut, dan aplikasi apa saja yang harus Anda instal untuk menjadi seorang Bitcoiner yang berdaulat.





# Menghubungkan Wallet Anda ke node Anda


<partId>418d0afd-3a61-4b5a-9db4-203c0335fd29</partId>



## Pengindeks: peran, operasi, dan solusi


<chapterId>4f93c07a-f0cb-435f-8b68-162f316d7039</chapterId>



Jika Anda telah menjelajahi node Bitcoin sebelum mengikuti kursus ini, Anda mungkin pernah menemukan istilah "pengindeks". Ini adalah alat seperti Electrs atau Fulcrum, yang dapat ditambahkan ke node Bitcoin core. Tapi apa sebenarnya peran mereka? Bagaimana cara kerjanya dalam praktik? Dan haruskah Anda menginstalnya pada node Bitcoin yang baru? Itulah yang akan kita bahas dalam bab ini.



### Apa yang dimaksud dengan pengindeks?



Secara umum, pengindeks adalah program yang memindai sekumpulan data mentah, mengekstrak kunci-kunci yang relevan (seperti kata, pengenal, dan alamat), dan membuat file tambahan, yang disebut "indeks", di mana setiap kunci merujuk ke lokasi data yang tepat dalam korpus. Fase pra-pemrosesan ini menggunakan waktu CPU dan membutuhkan beberapa ruang disk, tetapi menghilangkan kebutuhan untuk memproses seluruh korpus setiap kali basis data ditanyakan; cukup dengan menginterogasi indeks akan menghasilkan respons yang hampir seketika.



Dalam istilah awam, prinsipnya sama seperti indeks dalam buku: jika Anda mencari informasi tertentu, daripada membaca ulang seluruh buku, Anda membaca indeks untuk langsung menemukan halaman di mana informasi yang Anda cari muncul.



Pada node Bitcoin, seperti Bitcoin core, data Blockchain disimpan dalam bentuk mentah dan kronologis. Setiap blok berisi transaksi, yang pada gilirannya berisi input dan output, tanpa klasifikasi tertentu berdasarkan Address, pengenal, atau Wallet. Organisasi linier ini dioptimalkan untuk validasi blok, tetapi tidak cocok untuk pencarian yang ditargetkan. Sebagai contoh, jika Anda ingin menemukan semua transaksi yang terkait dengan Address tertentu di node yang tidak diindeks, Anda harus meninjau secara manual seluruh Blockchain, blok demi blok dan transaksi demi transaksi. Di sinilah pengindeks pada node Bitcoin Anda berperan.



![Image](assets/fr/085.webp)



Pengindeks adalah program perangkat lunak khusus yang menganalisis kumpulan data mentah ini (set Blockchain, Mempool, UTXO) dan mengekstrak kunci, seperti pengidentifikasi transaksi, alamat, dan ketinggian blok. Dari kunci-kunci ini, program ini membangun indeksnya, mengasosiasikan setiap kunci dengan lokasi yang tepat dari informasi dalam penyimpanan node.



![Image](assets/fr/086.webp)



Pengindeksan memungkinkan Anda untuk mencari informasi di node Anda dengan cepat, akurat, dan efisien. Sebagai contoh, ketika Anda menghubungkan Wallet seperti Sparrow ke node Anda, node tersebut dapat menampilkan saldo Address hampir seketika. Secara konkret, ini menanyakan pengindeks dengan permintaan seperti: "_UTXO mana yang terkait dengan skrip ini-Hash?_" Pengindeks merespons hampir seketika, tanpa harus membaca ulang seluruh Blockchain, karena data ini sudah terdaftar di dalam basis datanya.



### Apakah Bitcoin core memiliki pengindeks?



Tanpa memerlukan perangkat lunak tambahan, Bitcoin core tidak menawarkan pengindeks Address yang lengkap seperti yang terdapat pada perangkat lunak seperti Electrs atau Fulcrum. Namun demikian, Bitcoin core menggabungkan beberapa mekanisme pengindeksan internal, serta opsi opsional untuk memperluas kemampuan pengindeksannya. Untuk memahami situasi ini sepenuhnya, kita perlu melihat kembali sejarah proyek ini.



Hingga Bitcoin core versi 0.8.0, validasi transaksi didasarkan pada indeks transaksi global, yang dikenal sebagai `txindex`. Indeks ini mereferensikan semua transaksi Blockchain dan keluarannya. Ketika sebuah node menerima transaksi baru, node tersebut berkonsultasi dengan indeks ini untuk memverifikasi bahwa output yang dikonsumsi (dalam input) benar-benar ada dan belum digunakan. oleh karena itu, `txindex` sangat diperlukan untuk validasi transaksi pada saat itu.



Namun, pendekatan ini memiliki keterbatasan: lambat, mahal dalam hal penyimpanan, dan berlebihan dalam hal informasi. Untuk mengatasi hal ini, versi 0.8.0 memperkenalkan perombakan model validasi yang disebut ***Ultraprune***. Alih-alih menyimpan semuanya dalam bentuk indeks transaksi, Bitcoin core memelihara basis data sederhana yang didedikasikan khusus untuk UTXO, yang disebut `chainstate` (dalam bahasa sehari-hari, ini dikenal sebagai "set UTXO"), dan memperbarui daftarnya saat output dikonsumsi dan dibuat.



Metode ini jauh lebih cepat dan hanya menyimpan status register saat ini, sehingga pengindeks `txindex` tidak diperlukan. Namun, alih-alih menghapus kode `txindex`, para pengembang memilih untuk menyimpan fungsionalitas ini di balik parameter sederhana (`txindex=1`). Dengan mengaktifkan opsi ini pada node Anda, Anda dapat menanyakan transaksi apa pun dari `txid`.



Berlawanan dengan kepercayaan umum, Bitcoin core tidak menawarkan pengindeksan berbasis Address seperti Electrs atau Fulcrum. Ada beberapa alasan untuk pilihan ini:





- Peran Bitcoin core bukan untuk menjadi Block explorer yang lengkap, atau untuk menyediakan API yang disesuaikan untuk setiap penggunaan. Mengintegrasikan indeks berbasis Address akan menyiratkan pemeliharaan jangka panjang Commitment yang melampaui cakupan awal perangkat lunak.





- Sebagian besar kasus penggunaan sudah dapat dicakup dengan cara lain. Sebagai contoh, untuk memperkirakan saldo Address, Anda dapat menggunakan perintah `scantxoutset`, yang secara langsung menanyakan set UTXO tanpa memerlukan indeks lengkap.





- Setiap program perangkat lunak memiliki persyaratan khusus mengenai format atau jenis data yang akan diindeks (skrip Address, Hash, tag hak milik, dll.). Lebih fleksibel dan logis untuk membiarkan program-program ini membangun indeks khusus mereka sendiri daripada memperbaiki solusi generik di Bitcoin core.



Bitcoin core memiliki pengindeks transaksi opsional (`txindex`), sisa-sisa operasi historisnya, tetapi tidak menyediakan indeks Address, atau Interface langsung untuk pencarian yang kompleks. Oleh karena itu, dalam beberapa kasus, mungkin berguna untuk menambahkan pengindeks eksternal.



### Haruskah Anda menambahkan pengindeks Address ke node Anda?



Menambahkan pengindeks Address, seperti Electrs atau Fulcrum, tidak wajib; tergantung pada kebutuhan spesifik Anda.



Jika Anda hanya ingin menghubungkan Wallet, seperti Sparrow, ke node Anda untuk melihat saldo dan menyiarkan transaksi, hal ini sangat mungkin dilakukan secara langsung melalui Bitcoin core Interface RPC, baik secara lokal maupun jarak jauh melalui Tor.



Di sisi lain, untuk menggunakan perangkat lunak yang lebih canggih, seperti menjalankan Mempool.Secara lokal, pemasangan pengindeks Address menjadi sangat diperlukan untuk ruang Block explorer.



Pengindeks memerlukan waktu sinkronisasi tertentu (lebih singkat daripada IBD) dan akan menggunakan ruang disk tambahan. Jika SSD Anda masih memiliki ruang kosong yang cukup setelah mengunduh Blockchain, Anda dapat dengan mudah menambahkan pengindeks.



### Pengindeks mana yang harus dipilih?



Dua program perangkat lunak biasanya digunakan untuk membangun jenis indeks Address ini dan membuatnya dapat diakses: **Electrs** dan **Fulcrum**. Alat-alat ini mengindeks Blockchain menurut script-Hash (alamat) dan kemudian mengusulkan Interface standar (protokol Electrum), yang terhubung dengan berbagai dompet, seperti Electrum Wallet, Sparrow, atau Phoenix.



![Image](assets/fr/087.webp)



Sederhananya, Electrs cukup ringkas: mengindeks Blockchain lebih cepat dan menggunakan lebih sedikit ruang disk, tetapi kinerjanya sedikit kurang baik dibandingkan Fulcrum dalam hal kueri. Sebaliknya, Fulcrum menghabiskan lebih banyak ruang disk dan membutuhkan waktu lebih lama untuk mengindeks, tetapi menawarkan kinerja kueri yang superior.



Untuk penggunaan individu, saya merekomendasikan Electrs: ia mengkonsumsi lebih sedikit ruang, terpelihara dengan baik, dan, meskipun sedikit lebih lambat pada permintaan tertentu daripada Fulcrum, masih lebih dari cukup untuk penggunaan sehari-hari. Jika Anda memiliki waktu dan ruang penyimpanan, Anda juga bisa mencoba Fulcrum, yang akan berkinerja jauh lebih baik, terutama pada dompet dengan banyak alamat yang harus diverifikasi.



Secara konkret, pada bulan Agustus 2025, Electrs akan membutuhkan sekitar 56 GB penyimpanan, dibandingkan dengan sekitar 178 GB untuk Fulcrum. Oleh karena itu, pilihan pengindeks Anda juga tergantung pada kapasitas penyimpanan Anda:




- Jika ruang disk Anda sangat terbatas, Anda harus puas dengan Bitcoin core tanpa pengindeks Address eksternal.
- Jika Anda ingin menggunakan pengindeks, tetapi masih terkendala oleh kapasitas, pilihlah Electrs.
- Jika Anda memiliki jumlah ruang disk yang nyaman, Fulcrum mungkin yang Anda cari.



Untuk sisa kursus BTC 202 ini, saya akan menggunakan Electrs, tetapi Anda dapat dengan mudah mengikuti dengan Fulcrum: prosedur instalasi identik, seperti halnya koneksi Interface ke Wallet, karena keduanya mengekspos server Electrum.



### Bagaimana cara memasang pengindeks di Umbrel?



Untuk memasang Electrs (atau Fulcrum) pada Umbrel Anda, prosedurnya sangat mudah: buka App Store, cari aplikasi yang relevan (terletak di tab Bitcoin), lalu klik tombol "*Install*".



![Image](assets/fr/028.webp)



Setelah instalasi selesai, Electrs akan melanjutkan dengan fase sinkronisasi (pengindeksan), yang dapat memakan waktu beberapa jam.



![Image](assets/fr/029.webp)



Setelah sinkronisasi selesai, Anda dapat menghubungkan perangkat lunak Wallet Anda ke server Electrum, yang dihosting di Umbrel.



## Bagaimana cara menghubungkan Wallet saya ke node Bitcoin saya?


<chapterId>35519b1a-f681-4a69-a652-9fbe510cd17f</chapterId>



Sekarang setelah Anda memiliki node Bitcoin yang lengkap, saatnya untuk memanfaatkannya dengan baik! Di bab berikutnya, kita akan menjelajahi potensi penggunaan lain untuk instance Umbrel Anda. Namun, mari kita mulai dengan dasar-dasarnya: menghubungkan perangkat lunak Wallet Anda untuk memanfaatkan informasi dari Blockchain Anda sendiri dan mendistribusikan transaksi melalui node Anda sendiri.



Seperti disebutkan di atas, ada dua antarmuka koneksi utama:




- Sambungan langsung ke Bitcoin core melalui RPC;
- Atau sambungkan ke server Electrum (Electrs atau Fulcrum).



Dalam tutorial ini, kita akan berkonsentrasi pada koneksi ke node Anda melalui Tor, karena ini adalah solusi yang sederhana dan aman untuk pemula. Saya sangat menyarankan agar Anda tidak membuka port RPC node Anda secara terbuka, karena kesalahan konfigurasi akan menimbulkan risiko yang signifikan terhadap keamanan dan kerahasiaan data Anda. Kerugian utama dari komunikasi melalui Tor adalah kelambatannya. Dalam bab berikutnya, kita akan menjelajahi alternatif yang cepat dan aman untuk Tor untuk akses jarak jauh ke node Anda: VPN.



Kita akan menggunakan Sparrow sebagai contoh dalam bab ini, tetapi prosedurnya sama untuk semua perangkat lunak manajemen Wallet yang menerima koneksi ke server Electrum. Cukup cari pengaturan yang sesuai di parameter aplikasi Anda (biasanya di "*Server*", "*Network*", "*Node*"...).



Pada Sparrow, buka tab "*File*" dan masuk ke menu "Pengaturan".



![Image](assets/fr/030.webp)



Kemudian klik "*Server*" untuk mengakses parameter koneksi.



![Image](assets/fr/031.webp)



Anda kemudian akan menemukan tiga opsi untuk menautkan perangkat lunak Anda ke node Bitcoin:




- Public Server* (kuning): secara default, jika Anda tidak memiliki node Bitcoin, opsi ini menghubungkan Anda ke node publik yang tidak Anda miliki (biasanya milik perusahaan). Opsi ini tidak relevan di sini, karena Anda memiliki node Anda sendiri di Umbrel.
- Bitcoin core* (Green): opsi ini sesuai dengan koneksi melalui Interface RPC, yaitu langsung ke Bitcoin core.
- Private Electrum* (biru): opsi ini memungkinkan Anda terhubung melalui pengindeks Interface Electrum Server (Electrs atau Fulcrum) milik pengindeks Anda.



### Koneksi ke Bitcoin core RPC



Jika node Umbrel Anda tidak memiliki pengindeks, ini adalah opsi yang perlu Anda pilih. Pada Sparrow, klik "*Bitcoin core*".



![Image](assets/fr/032.webp)



Anda kemudian perlu memasukkan beberapa informasi untuk membuat koneksi ke node Anda. Semua data ini dapat diakses dari aplikasi "*Bitcoin Node*" pada Umbrel dengan mengklik tombol "*Connect*" di sudut kanan atas Interface.



![Image](assets/fr/033.webp)



Tab "*Detail RPC*" menampilkan semua informasi yang diperlukan untuk koneksi. Pilih untuk menyambung melalui Tor Address (dalam format `.onion`).



![Image](assets/fr/034.webp)



Masukkan data ini di bidang yang sesuai pada Sparrow wallet, lalu klik tombol "*Test Connection*".



![Image](assets/fr/035.webp)



Jika koneksi berhasil, tanda centang Green dan pesan konfirmasi akan muncul.



![Image](assets/fr/036.webp)



Tanda centang di kanan bawah Interface Sparrow wallet sekarang akan menjadi Green (mengindikasikan koneksi langsung ke Bitcoin core).



**Catatan:** Agar koneksi berhasil, node Anda harus 100% tersinkronisasi. Jika tidak demikian, harap tunggu hingga akhir IBD.



### Terhubung ke Electrs



Jika node Anda memiliki pengindeks, lebih baik untuk terhubung ke pengindeks daripada menggunakan Bitcoin core secara langsung, karena kueri Anda akan diproses lebih cepat.



Pada Sparrow, buka tab "*Private Electrum*".



![Image](assets/fr/037.webp)



Anda kemudian harus memasukkan beberapa informasi untuk membuat koneksi dengan pengindeks Anda. Anda akan menemukan data ini di aplikasi "*Electrs*" (atau, jika ada, "*Fulcrum*") di Umbrel.



Pilih tab "*Tor*" untuk mendapatkan koneksi `.onion` Address. Jika Anda ingin menghubungkan perangkat lunak Wallet seluler, Anda juga dapat memindai kode QR secara langsung.



![Image](assets/fr/038.webp)



Cukup masukkan Tor Address dari server Electrum Anda pada kolom "*URL*", lalu klik tombol "*Test Connection*".



![Image](assets/fr/039.webp)



Jika koneksi berhasil, tanda centang dan pesan konfirmasi akan ditampilkan.



![Image](assets/fr/040.webp)



Tanda centang di sudut kanan bawah Interface Sparrow wallet akan berubah menjadi biru (warna yang terkait dengan koneksi ke server Electrum).



**Catatan:** Agar koneksi dapat berfungsi, pengindeks Anda harus disinkronkan 100%. Jika tidak demikian, tunggu sampai proses pengindeksan selesai.



Sekarang Anda sudah tahu cara menghubungkan Wallet Anda ke node Bitcoin Anda! Pada bab berikutnya, saya akan memperkenalkan Anda pada beberapa aplikasi tambahan yang tersedia di Umbrel yang sangat saya sukai, dan yang akan memungkinkan Anda untuk meningkatkan penggunaan Bitcoin sehari-hari melalui node Anda.




## Ikhtisar aplikasi yang tersedia


<chapterId>2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594</chapterId>



Umbrel menawarkan toko aplikasi yang luas. Seperti yang akan Anda lihat, ada banyak alat yang terkait dengan Bitcoin, tetapi juga berbagai macam aplikasi di bidang yang sangat berbeda: solusi self-hosting untuk layanan dan file, aplikasi produktivitas, alat keuangan yang lebih umum, manajemen media, keamanan dan administrasi jaringan, pengembangan, kecerdasan buatan, jejaring sosial, dan bahkan otomatisasi rumah.



Dalam kursus BTC 202 ini, kita akan berkonsentrasi secara eksklusif pada aplikasi yang berhubungan dengan Bitcoin. Namun, jangan ragu untuk menjelajahi katalog lainnya untuk alat yang mungkin berguna bagi Anda.



Tentu saja, tidak mungkin untuk mencantumkan semua aplikasi Bitcoin di sini. Dalam bab ini, saya ingin memperkenalkan Anda pada alat bantu penting yang akan memfasilitasi dan memperkaya penggunaan Bitcoin sehari-hari.



### Mempool.space



Dalam penggunaan Bitcoin sehari-hari, jika ada satu alat yang benar-benar sangat diperlukan, itu adalah Block explorer. Baik dapat diakses secara online maupun diinstal secara lokal, alat ini mengubah data mentah Blockchain menjadi format yang terstruktur, jelas, dan mudah dibaca. Alat ini juga dilengkapi dengan mesin pencari yang memungkinkan pengguna untuk menemukan blok, transaksi, atau Address tertentu dengan cepat.



Secara konkret, penjelajah memungkinkan Anda untuk memperkirakan biaya yang diperlukan agar transaksi Anda dapat dimasukkan ke dalam sebuah blok, kemudian melacak perkembangannya: cari tahu apakah transaksi tersebut akan dimasukkan dalam waktu dekat, tergantung pada pasar biaya, dan akhirnya mengonfirmasi bahwa transaksi tersebut telah dimasukkan ke dalam sebuah blok. Ini juga menawarkan kemungkinan untuk menganalisis transaksi Anda di masa lalu dan melihat riwayatnya. Singkatnya, ini adalah Pisau Tentara Swiss bagi para bitcoiner.



Seperti yang telah disebutkan sebelumnya, penjelajah dapat di-host secara online di situs web atau dijalankan secara lokal di komputer Anda. Kerugian utama dari layanan online adalah mereka bisa membahayakan privasi Anda. Tanpa VPN atau Tor, server yang meng-hosting penjelajah bisa menghubungkan IP Address Anda dengan transaksi yang Anda lihat, yang bisa memberikan titik masuk yang ideal untuk analisis rantai.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Terlebih lagi, Penyedia Layanan Internet (ISP) Anda mungkin mengetahui bahwa Anda melihat transaksi tertentu melalui situs Block explorer. Hal ini juga menimbulkan pertanyaan tentang kepercayaan: Anda harus bergantung pada layanan online untuk memberikan Anda informasi yang akurat tentang transaksi Anda, tanpa dapat memverifikasi kebenarannya sendiri.



Itulah sebabnya mengapa selalu lebih baik menggunakan Block explorer lokal Anda sendiri. Dengan cara ini, tidak ada data yang terkait dengan aktivitas penelusuran Anda yang akan bocor, karena semua kueri diproses secara langsung di mesin yang Anda kendalikan, tanpa melewati Internet. Terlebih lagi, penjelajah lokal mengandalkan data dari node Bitcoin Anda sendiri, yang telah Anda validasi sendiri, sesuai dengan aturan Anda sendiri, dan yang dapat Anda percayai.



Umbrel menawarkan beberapa penjelajah blok:




- Mempool.Space
- Bitfeed
- BTC RPC Explorer



Saya sangat menyukai Mempool.Space, yang saya pasang di node saya. Harap diperhatikan: untuk menggunakan sebagian besar penjelajah blok di Umbrel, diperlukan pengindeks Address. Oleh karena itu, Anda memerlukan aplikasi Bitcoin Node (atau Bitcoin Knots), yang memiliki Blockchain yang tersinkronisasi 100%, serta pengindeks seperti Electrs atau Fulcrum, yang juga tersinkronisasi 100%.



Setelah aplikasi terinstal, cukup buka aplikasi tersebut untuk mengakses penjelajah Anda.



![Image](assets/fr/041.webp)



Untuk mempelajari lebih lanjut tentang cara menggunakan Mempool.Space explorer, saya merekomendasikan tutorial komprehensif ini:



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

### Simpul Petir



Setelah Anda memiliki node Bitcoin Anda sendiri, Anda juga dapat menyiapkan node Lightning Anda sendiri untuk melakukan transaksi off-chain, tanpa bergantung pada infrastruktur pihak ketiga.



Umbrel menawarkan sejumlah aplikasi untuk membantu Anda menyiapkan dan menjalankan simpul Lightning Anda. Anda sudah bisa memilih di antara dua implementasi utama:




- LND, melalui aplikasi *Lightning Node*;
- Inti Petir.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Anda kemudian dapat mengelola node Anda dari Interface utama, atau, untuk fungsionalitas yang lebih besar dan opsi lanjutan, instal *Ride The Lightning* atau *ThunderHub*. Alat-alat ini akan memberi Anda sistem manajemen Interface berbasis web yang jauh lebih komprehensif untuk node Anda.



https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

![Image](assets/fr/088.webp)



Terakhir, saya merekomendasikan aplikasi *Lightning Network+*, yang memungkinkan Anda menemukan rekan-rekan yang dapat diajak untuk membuka saluran, sehingga memungkinkan transaksi tunai keluar dan masuk.



![Image](assets/fr/089.webp)



Berkat Umbrel, pengelolaan node Lightning pribadi menjadi lebih sederhana, namun tetap relatif kompleks. Oleh karena itu, saya merekomendasikan Anda untuk mengikuti kursus LNP 202, yang merupakan kelanjutan logis dari kursus BTC 202, dan di mana saya mendampingi Anda langkah demi langkah dalam menyiapkan dan mengelola node Lightning Anda di Umbrel.



https://planb.academy/courses/593e483e-1785-4e83-aa7e-32b99056844c

### Skala ekor



Aplikasi lain yang sangat saya sukai di Umbrel adalah Tailscale. Ini adalah aplikasi VPN yang dirancang untuk menyederhanakan pembuatan jaringan aman di antara beberapa perangkat, di mana pun mereka berada di dunia. Tidak seperti VPN tradisional, yang mengandalkan server terpusat, Tailscale menggunakan protokol WireGuard untuk membuat koneksi terenkripsi ujung-ke-ujung di antara berbagai mesin Anda. Ini berarti Anda bisa menggunakan VPN yang berfungsi hanya dalam beberapa menit, tanpa perlu konfigurasi jaringan yang rumit.



Di Umbrel, instalasi Tailscale menghubungkan node Bitcoin Anda ke jaringan pribadi virtual Anda sendiri. Setelah dikonfigurasi, node Anda mendapatkan IP Tailscale Address pribadi, yang hanya dapat diakses dari perangkat lain yang terhubung ke jaringan Tailscale yang sama (seperti komputer, ponsel cerdas, dan tablet). Koneksi ini dienkripsi dari ujung ke ujung dan tidak melewati jaringan publik yang tidak terlindungi, sehingga secara signifikan meningkatkan keamanan dibandingkan dengan koneksi yang tidak terenkripsi.



![Image](assets/fr/090.webp)



Secara konkret, Tailscale menawarkan beberapa keuntungan saat menggunakan Umbrel Anda:





- Anda dapat mengelola Interface Umbrel atau mengakses aplikasi yang terhubung ke node Anda (seperti Mempool, Ride The Lightning, ThunderHub...) dari mana saja, seolah-olah Anda berada di jaringan lokal yang sama, tanpa membuka port di Internet dan tanpa melalui Tor, yang sangat lambat;





- Anda bisa tersambung ke peladen Electrum Anda (Electrs atau Fulcrum) atau langsung ke Bitcoin core melalui VPN Anda, melewati Tor. Ini memberikan koneksi yang aman, sebanding dengan menggunakan Tor, tetapi dengan kecepatan yang jauh lebih tinggi dan latensi yang lebih rendah. Singkatnya, Anda tetap mendapatkan manfaat privasi dan keamanan dari Tor sambil menikmati kecepatan koneksi Clearnet. Untuk On-Chain Wallet, keuntungan ini mungkin terlihat kecil, tetapi jika Anda berencana untuk menyiapkan node Lightning Anda sendiri di kemudian hari, perbedaannya cukup besar. Memang, melakukan pembayaran melalui node Anda saat bepergian dengan Tor sangat lambat karena banyaknya pertukaran yang diperlukan, sedangkan dengan Tailscale, ini bekerja dengan sempurna.





- Tidak perlu mengonfigurasi aturan NAT, membuka porta, atau menyiapkan server VPN konvensional. Setelah aplikasi terinstal di Umbrel dan perangkat Anda, jaringan secara otomatis terbentuk.



Oleh karena itu, Tailscale pada Umbrel merupakan solusi yang sangat menarik jika Anda ingin mengakses node Anda dari mana saja di seluruh dunia dengan cara yang aman, berkinerja tinggi, dan mudah dikonfigurasikan, tanpa mengorbankan privasi atau keamanan.



Untuk menginstal dan mengkonfigurasi Tailscale pada Umbrel Anda, lihat tutorial ini, bagian 4: "*Menggunakan Tailscale pada Umbrel*":



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Nostr



Nostr, singkatan dari "*Notes and Other Stuff Transmitted by Relays*", adalah protokol terbuka dan terdesentralisasi yang dirancang untuk memungkinkan pesan dipublikasikan dan dipertukarkan di Internet tanpa bergantung pada platform terpusat. Setiap pengguna memiliki sepasang kunci kriptografi: kunci publik (`npub`), yang berfungsi sebagai pengenal, dan kunci privat (`nsec`), yang digunakan untuk menandatangani pesan dan menjamin keasliannya.



Pesan dikirim melalui jaringan relai independen. Arsitektur terdistribusi ini membuat Nostr tahan terhadap penyensoran: tidak ada satu server pun yang mengontrol akses atau distribusi, dan pengguna dapat terhubung ke sebanyak mungkin relai yang mereka inginkan.



Protokol ini sangat populer di dalam komunitas Bitcoin karena, seperti halnya Bitcoin, Nostr membahas masalah kedaulatan digital dan kontrol data. Penciptanya, Fiatjaf, adalah seorang pengembang yang telah dikenal dalam ekosistem karena kontribusinya yang banyak.



Dengan Umbrel, Anda dapat mengoptimalkan penggunaan Nostr. Dengan menginstal aplikasi ***Nostr Relay***, Anda dapat meng-host relai pribadi Anda langsung di mesin Anda, memastikan bahwa semua postingan dan interaksi Anda di Nostr disimpan secara lokal dan tidak dapat hilang melalui penghapusan oleh relai publik.



Klien Nostr ***noStrudel*** atau ***Snort*** juga tersedia di Umbrel. Berkat aplikasi-aplikasi ini, Anda dapat mempublikasikan, membaca, mencari profil, dan berinteraksi dengan ekosistem Nostr secara langsung dari web Interface di Umbrel Anda.



Akhirnya, ada aplikasi ***Nostr Wallet Connect*** di Umbrel, yang memungkinkan pembayaran Lightning asli di dalam Nostr. Secara konkret, Anda dapat menghubungkan node Lightning Anda di masa depan ke klien Nostr Anda untuk mengirimkan mikro-pembayaran, disebut "*zaps*", guna memberi penghargaan pada konten atau berinteraksi secara termonetisasi tanpa melalui layanan pihak ketiga. Pembayaran ini dikirim langsung dari node pribadi Anda melalui saluran Anda.



Untuk mengetahui cara menggunakan semua aplikasi ini, saya sarankan Anda membaca tutorial lengkap ini:



https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

### Server BTCPay



BTCPay Server adalah prosesor pembayaran sumber terbuka gratis yang memungkinkan Anda menerima pembayaran melalui Bitcoin dan Lightning Network tanpa perantara, sambil tetap menyimpan dana sendiri.



Arsitektur BTCPay Server didasarkan pada node Bitcoin dan, untuk Lightning, pada implementasi yang kompatibel (LND, Core Lightning...), menjadikannya satu-satunya solusi PoS yang sepenuhnya non-kustodian. Ini juga merupakan perangkat lunak yang paling komprehensif untuk pelacakan dan akuntansi.



![Image](assets/fr/091.webp)



Jika Anda memiliki bisnis dan ingin menerima pembayaran Bitcoin secara langsung melalui node Umbrel Anda, aplikasi BTCPay Server sangat ideal untuk Anda. Untuk mengetahui lebih lanjut tentang hal ini, saya sarankan Anda membaca sumber-sumber berikut:





- Kursus BIZ 101 tentang penggunaan Bitcoin dalam bisnis Anda:



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a



- Kursus POS 305 tentang penggunaan BTCPay Server:



https://planb.academy/courses/6fc12131-e464-4515-9d3f-9255365d5fa1



- Tutorial Server BTCPay:



https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


# Konsep lanjutan dan praktik terbaik


<partId>fc77a62a-8d9f-4144-9080-3057b04db2c6</partId>



## Merawat node Umbrel Anda


<chapterId>06d77d09-bf24-4555-b2ba-c08bbda477c7</chapterId>



Untuk memulai bagian terakhir ini, dan sebelum beralih ke teori yang lebih lanjut, saya ingin membahas praktik terbaik dan tindakan nyata yang dapat Anda lakukan setelah node Umbrel Anda terinstal, tersinkronisasi, dan terkonfigurasi dengan benar dalam bab singkat ini. Bagaimana Anda memeliharanya setiap hari?



### Menjaga peralatan tetap sehat



Node yang andal dimulai dengan perangkat keras yang stabil. Pastikan mesin yang menjadi tempat node Anda memiliki ventilasi yang baik, bebas Dust, dan dipasang di lingkungan yang kering, jauh dari sumber panas dan kelembapan. Hindari menjejalkannya ke dalam ruang terbatas dan pilihlah lokasi yang berventilasi baik.



Pada Raspberry Pi dan mini-PC, Dust pada akhirnya akan menyumbat heatsink, meningkatkan suhu dan menyebabkan throttling (pembatasan penggunaan sumber daya secara sukarela), yang pada gilirannya akan menurunkan efisiensi node Anda. Itulah mengapa saya menyarankan untuk membersihkan saluran udara dan kipas secara berkala, idealnya setiap beberapa bulan sekali.



Pastikan Anda menggunakan Supply daya berkualitas tinggi, karena tegangan yang tidak stabil dapat menyebabkan kerusakan sistem dan bahkan menimbulkan bahaya kebakaran. Idealnya, Anda harus menggunakan Supply daya asli yang disediakan oleh produsen mesin Anda. Waspadai juga panas berlebih akibat efek Joule pada soket ekstensi: selalu patuhi daya maksimum yang diizinkan dan jangan pernah menyambungkan beberapa soket ekstensi secara bertingkat.



Saya juga menyarankan untuk berinvestasi dalam UPS. Hal ini melindungi node Anda dari pemadaman mendadak, memungkinkan Umbrel untuk mati dengan bersih jika terjadi pemadaman, dan memastikan kontinuitas operasi selama pemadaman mikro atau kegagalan jangka pendek.



Di sisi penyimpanan, perhatikan perkembangannya: jika disk mendekati titik jenuh, pertimbangkan untuk mengosongkan ruang (hapus instalan aplikasi yang tidak terpakai, sesuaikan pengaturan pengindeks) atau migrasi ke SSD yang lebih besar. Kerugian dari node Bitcoin yang penuh adalah kebutuhan penyimpanannya terus meningkat, karena blok baru dibuat setiap 10 menit dan blok lama tidak dapat dihapus (kecuali jika node tersebut adalah pruned). Oleh karena itu, saya menyarankan Anda untuk merencanakan kapasitas yang cukup besar saat membeli perangkat keras Anda (minimal 2 TB).



### Memperbarui



Pembaruan node penting untuk tiga alasan utama: pertama, keamanan (patch kerentanan, pengerasan jaringan, dan perlindungan DoS); kedua, kompatibilitas (perubahan kebijakan relai, perubahan format, dan peningkatan protokol); dan ketiga, keandalan dan kinerja (perbaikan bug, konsumsi sumber daya, dan peningkatan lainnya). Jadi, periksa secara berkala apakah UmbrelOS dan aplikasi Anda sudah diperbarui:





- Untuk memperbarui sistem: Buka menu pengaturan, lalu klik tombol "*Periksa Pembaruan*" di samping parameter "*UmbrelOS*".



![Image](assets/fr/042.webp)





- Untuk memperbarui aplikasi: Buka App Store. Jika ada aplikasi Anda yang perlu diperbarui, tombol dengan gelembung merah akan muncul di sudut kanan atas Interface. Cukup klik tombol tersebut, lalu perbarui setiap aplikasi.



Lakukan operasi ini secara teratur untuk menjaga agar sistem operasi dan aplikasi Anda tetap mutakhir.



### Cadangan



Jika Anda hanya menggunakan node Bitcoin untuk memvalidasi dan mendistribusikan transaksi Anda, tetapi dompet Anda dikelola di luar Umbrel (misalnya, dengan Hardware Wallet dan Sparrow wallet), tidak ada yang perlu dicadangkan langsung ke Umbrel. Dalam kasus ini, cadangan penting tetap menggunakan frasa pemulihan dan Descriptor dari Wallet eksternal Anda, dan ini berlaku baik Anda menggunakan node Anda sendiri atau tidak. Jadi tidak ada yang berubah dari konfigurasi Anda sebelumnya.



Di sisi lain, tergantung pada aplikasi tambahan yang Anda gunakan di Umbrel, pencadangan lebih lanjut mungkin diperlukan. Hal ini terutama terjadi jika Anda mengoperasikan node Lightning pada Umbrel. Dalam kasus ini, sangat penting untuk mencadangkan seed yang disertakan saat Anda memasang node Lightning. Selain seed, Anda memerlukan ***Static Channel Backup (SCB)*** yang mutakhir untuk dapat memulihkan node Lightning Anda jika terjadi masalah. SCB memungkinkan Anda untuk memulihkan dana Anda dengan menutup saluran secara paksa. Jika salah satu dari seed atau SCB tidak ada, maka tidak mungkin untuk memulihkan node Lightning.



Umbrel juga menawarkan opsi untuk mencadangkan SCB ini secara otomatis dan dinamis di server mereka, melalui Tor, untuk memastikan bahwa file terbaru selalu tersedia. Dalam hal ini, hanya seed yang diperlukan untuk memulihkan node.



Kita akan meninjau kembali aspek-aspek ini secara rinci dalam kursus LNP202 berikutnya.



### Keselamatan operasional sehari-hari



Dari segi keamanan, gunakan kata sandi yang panjang, unik, dan acak untuk Interface Umbrel, dan ingatlah untuk mengaktifkan otentikasi dua faktor (2FA). Untuk aplikasi yang menawarkan perlindungan kata sandi dan 2FA, selalu aktifkan keduanya dan ubah kata sandi default.



Jangan pernah membuka dasbor ke Internet tanpa menggunakan gateway yang aman (seperti VPN, Tor, atau akses lokal saja). Batasi jumlah aplikasi yang Anda instal, dan hapus aplikasi yang tidak Anda perlukan secara teratur, untuk mengurangi permukaan serangan.



Untuk memperdalam pengetahuan Anda tentang keamanan komputer secara umum, saya sangat menyarankan Anda untuk melihat kursus gratis ini:



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Diagnosis dan bantuan mandiri



Jika terjadi bug pada Umbrel Anda, pertama-tama generate bundel diagnostik melalui bagian pemecahan masalah UmbrelOS atau aplikasi yang bersangkutan, kemudian restart aplikasi dengan bersih. Jika perlu, cobalah juga untuk melakukan boot ulang sistem secara keseluruhan.



Jika masalah terus berlanjut, saya sarankan Anda [bergabunglah dengan komunitas pengguna Umbrel di Discord mereka](https://discord.gg/efNtFzqtdx). Mulailah dengan melakukan pencarian untuk menentukan apakah ada orang yang mengalami kesulitan yang sama dan menemukan solusinya. Jika belum, Anda bisa mengirim pesan di saluran `dukungan umum`. Anda juga bisa menggunakan [forum Umbrel](https://community.umbrel.com/).



Area-area ini memungkinkan Anda tidak hanya untuk mengikuti pengumuman dan pembaruan keamanan, tetapi juga untuk mengajukan pertanyaan dan, pada akhirnya, membantu pengguna lain. Sering kali di dalam bursa inilah praktik-praktik terbaik ditemukan.



Dengan kebiasaan sederhana ini, node Umbrel Anda akan tetap stabil, aman, dan berguna, baik untuk Anda maupun jaringan Bitcoin.




## Memahami IBD dan proses penemuan teman sebaya


<chapterId>175ac9d1-ea23-45d9-9918-d3e7352435cd</chapterId>



Node Bitcoin Anda dimulai tanpa mengetahui riwayat transaksi sebelumnya. Awalnya, ini hanyalah sebuah komputer yang menjalankan perangkat lunak (Bitcoin core atau sejenisnya). Untuk menjadi node Bitcoin yang tersinkronisasi dan beroperasi penuh, node ini harus merekonstruksi keadaan Ledger secara lokal dengan memeriksa semua blok yang diterbitkan sejak blok Genesis (blok 0, yang diterbitkan oleh Satoshi Nakamoto pada tanggal 3 Januari 2009). Langkah ini disebut **IBD (_Initial Block Download_)**.



IBD terdiri dari mengunduh dan memverifikasi setiap blok dan transaksi satu per satu, dengan menerapkan aturan konsensus, untuk membangun versinya sendiri dari Blockchain. Tujuannya bukan hanya untuk mengambil salinan data yang belum diverifikasi, tetapi untuk sampai pada kesimpulan yang sama sepenuhnya secara independen, sebagai mayoritas yang jujur dari jaringan.



![Image](assets/fr/092.webp)



### Pencapaian IBD



Sinkronisasi dimulai dengan langkah _**headers-first**_. Node Anda meminta urutan header blok dari beberapa rekan dan, untuk masing-masing, memverifikasi Proof of Work, penyesuaian kesulitan, sintaksis, serta Timestamp dan aturan nomor versi. Singkatnya, ini memastikan bahwa setiap header yang diterima sesuai dengan aturan konsensus.



![Image](assets/fr/093.webp)



Sebagai pengingat, blok Bitcoin terdiri dari header 80-byte dan daftar transaksi. Sidik jari blok diperoleh dengan menerapkan SHA-256 Hash ganda pada header ini, yang berisi 6 bidang:




- versi
- Hash dari blok sebelumnya
- Merkle Root transaksi
- Timestamp (lebih besar dari waktu rata-rata 11 blok sebelumnya)
- target kesulitan
- Nonce



![Image](assets/fr/094.webp)



Transaksi dilakukan pada sebuah Merkle Tree. Ini merupakan struktur yang meringkas sekumpulan besar data (dalam hal ini, semua transaksi dalam blok) dengan menggabungkan hash mereka secara progresif dua per dua ke satu "root", sehingga membuktikan bahwa sebuah elemen adalah bagian dari kumpulan tersebut (dan mendeteksi modifikasi apa pun). Dengan cara ini, setiap modifikasi pada transaksi juga memodifikasi root dari Merkle Tree dan oleh karena itu sidik jari header blok. SegWit telah memperkenalkan Commitment tambahan yang terpisah untuk cookie (tanda tangan), yang ditempatkan di dalam basis koin.



![Image](assets/fr/095.webp)



Langkah _**headers-first**_ ini memungkinkan node untuk mengidentifikasi cabang yang paling banyak bekerja (terlepas dari jumlah bloknya), yang merupakan cabang tempat node Bitcoin melakukan sinkronisasi. Setelah cabang ini diidentifikasi, node akan mengunduh isi blok secara paralel dari beberapa koneksi, kemudian memvalidasi setiap transaksi: format, validitas skrip (kecuali `assumevalid=1`), jumlah, dan tidak adanya pengeluaran ganda. Dengan setiap pemeriksaan yang berhasil, status koin yang tidak terpakai (set UTXO) saat ini diperbarui dalam database `chainstate/`: output yang terpakai akan dihapus, sementara output baru yang valid akan ditambahkan.



Mempool, di sisi lain, hanya berperan ketika mendekati ujung rantai: selama node tetap terlambat, tidak ada transaksi yang tertunda untuk disimpan.



Setelah IBD selesai, node memasuki fase normalnya: node memvalidasi blok baru saat diterbitkan, mempertahankan Mempool dengan transaksi yang tertunda sesuai dengan aturan relai, merelay transaksi dan blok, dan mengelola reorganisasi rantai.



### AsumsikanValid



Bitcoin core menggabungkan mekanisme yang dirancang untuk mengurangi waktu yang dibutuhkan sebelum sebuah node beroperasi penuh, dengan tetap mempertahankan esensi dari prinsip verifikasi otonom: AsumsikanValid.



Parameter `assumevalid` didasarkan pada blok referensi sebelumnya, yaitu Hash yang diintegrasikan ke dalam setiap versi perangkat lunak. Selama IBD, jika node Anda menemukan bahwa blok ini memang berada di cabang yang paling banyak bekerja, node tersebut dapat mengabaikan verifikasi skrip untuk semua transaksi sebelum titik ini.



Semua aturan lainnya (struktur blok, Proof of Work, batas ukuran, jumlah transaksi, UTXO, dll.) tetap diverifikasi sepenuhnya. Hanya perhitungan skrip sebelum blok referensi ini yang diabaikan. Peningkatan kinerja sangat signifikan pada IBD, karena verifikasi tanda tangan menyumbang sebagian besar beban CPU. Di luar blok referensi ini, verifikasi kembali ke kondisi normal.



Anda dapat memaksa validasi penuh semua skrip dengan menonaktifkan mekanisme ini, dengan biaya IBD yang lebih lama, menggunakan parameter `assumevalid=0` di file `Bitcoin.conf`.



### AsumsikanUTXO



`assumeutxo` adalah parameter lain yang ada, tetapi tidak seperti `assumevalid`, parameter ini tidak diaktifkan secara default. Mekanisme ini memungkinkan perangkat lunak untuk memuat snapshot dari set UTXO, bersama dengan metadata, dan untuk sementara menganggapnya sebagai status referensi, setelah memverifikasi bahwa header memang mengarah ke Blockchain yang paling banyak bekerja.



Dengan demikian, node dengan cepat menjadi operasional untuk penggunaan umum (RPC, menghubungkan dompet, dll.), sambil secara bersamaan meluncurkan rekonstruksi lengkap dan terverifikasi dari set UTXO-nya sendiri di latar belakang. Setelah tahap ini selesai, snapshot awal digantikan oleh kondisi yang direkonstruksi secara lokal. Pendekatan ini memisahkan penyediaan node yang cepat dari verifikasi penuh, tanpa mengorbankan yang terakhir.



### Penemuan rekan: Bagaimana node Anda menemukan jaringan Bitcoin?



Ketika sebuah node memulai untuk pertama kalinya, node tersebut belum mengenal rekan-rekannya. Namun, ia harus menemukan node Bitcoin lain di Internet untuk meminta header, kemudian blok, untuk menyelesaikan IBD-nya. Untuk memulai koneksi ini, Bitcoin core mengikuti logika prioritas.



![Image](assets/fr/096.webp)



Ketika node dinyalakan kembali setelah digunakan, Core pertama-tama mencoba menyambungkan kembali ke peers yang terdaftar sebelum dimatikan, informasi disimpan dalam file `anchors.dat`. Kemudian, ia berkonsultasi dengan buku IP Address **`peers.dat`**, yang menyimpan daftar peers yang ditemui sebelumnya, untuk menyambungkan kembali ke mereka. Ini hanyalah file lokal, diperbarui dan disimpan oleh Core. Di sisi lain, untuk node baru yang baru saja diluncurkan, kedua file ini kosong, karena belum pernah berkomunikasi dengan node Bitcoin lainnya.



Dalam kasus ini, perangkat lunak menanyakan _**DNS seeds**_. Ini adalah [server yang dikelola oleh pengembang ekosistem yang diakui](https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp), yang mengembalikan daftar alamat IP dari node yang diduga aktif. Alamat-alamat ini memungkinkan node baru untuk memulai koneksi pertamanya dan meminta data yang diperlukan dari IBD. Berikut ini adalah daftar *benih DNS* yang aktif hingga saat ini (Agustus 2025):




- Pieter Wuille: `seed.Bitcoin.sipa.be.`
- Matt Corallo: `dnsseed.bluematt.me.`
- Luke Dashjr: `dnsseed.Bitcoin.dashjr-list-of-P2P-nodes.us.`
- Jonas Schnelli: `seed.Bitcoin.jonasschnelli.ch.`
- Peter Todd: `seed.btc.petertodd.net.`
- Sjors Provoost: `seed.Bitcoin.sprovoost.nl.`
- Stephan Oeste: `dnsseed.emzy.de.`
- Jason Maurice: `seed.Bitcoin.wiz.biz.`
- Ava Chow: `seed.Mainnet.achownodes.xyz.`



Pada sebagian besar kasus, langkah *DNS seeds* sudah cukup untuk membuat koneksi pertama dengan node lain. Jika, secara luar biasa, server ini gagal merespons dalam waktu 60 detik, node akan beralih ke metode lain: [daftar statis lebih dari 1.000 alamat](https://github.com/Bitcoin/Bitcoin/blob/master/src/chainparamsseeds.h) dari _seed node_ dibangun ke dalam kode Bitcoin core dan diperbarui secara teratur. Jika dua metode pertama untuk mendapatkan alamat IP gagal, solusi terakhir ini akan membuat koneksi awal, yang kemudian node dapat meminta alamat IP baru.



![Image](assets/fr/097.webp)



Sebagai upaya terakhir, Anda dapat secara manual Supply alamat IP melalui file `peers.dat` untuk memaksa koneksi tertentu.



Setelah di-bootstrap, manajer internal Address mendiversifikasi sumber-sumber (jaringan otonom yang terpisah, clearnet, dan Tor, serta berbagai area geografis) untuk mengurangi risiko isolasi topologi. Node membuat koneksi keluar ini (koneksi yang dipilihnya sendiri, dan karena itu lebih aman).



Jika node Anda mendengarkan pada port terbuka (secara default, 8333), maka node tersebut akan menerima koneksi yang masuk. Hal ini memperkuat ketahanan jaringan secara keseluruhan dengan menyediakan titik kontak untuk node baru, tanpa memberikan manfaat khusus pada IBD Anda. Jika node Anda berjalan pada Tor, logikanya tetap sama, tetapi alamat yang digunakan adalah layanan `.onion`.




## Anatomi node Bitcoin Anda


<chapterId>b420bd9d-7e2a-4984-bc70-2b732a94c8ce</chapterId>



Ketika node Anda telah menyelesaikan sinkronisasi awal, node akan menyimpan beberapa set data pelengkap secara lokal, sehingga memungkinkannya untuk memvalidasi blok dan transaksi, melayani rekan-rekan jaringan, dan memulai ulang dengan cepat sambil mempertahankan statusnya. 3 batu bata utama sangat penting pada sebuah node:




- **blok** blockchain yang disimpan di disk,
- set **UTXO** yang disimpan dalam basis data nilai kunci,
- dan **Mempool** disimpan dalam RAM dan diserialisasikan secara berkala.



Selain itu, beberapa file tambahan (rekan kerja, perkiraan biaya, daftar pengecualian, dompet, dll.) melengkapi gambar. Mari kita cari tahu peran dari semua file ini.



### Di mana sebenarnya data node berada?



Secara default, Bitcoin core menyimpan datanya di direktori kerja tertentu. Di bawah GNU/Linux, ini biasanya berada di `~/.Bitcoin/`, di bawah Windows di `%APPDATA%\Bitcoin/`, dan di bawah macOS di `~/Library/Application Support/Bitcoin/`. Jika Anda menggunakan solusi paket (misalnya, dalam distribusi node), direktori ini dapat dipasang di tempat lain, tetapi strukturnya tetap sama. Sub-folder dan berkas penting yang dijelaskan di bawah ini masih berada di sini.



![Image](assets/fr/098.webp)



### Blok-blok



Oleh karena itu, Blockchain adalah kumpulan blok. Full node menyimpan blok-blok ini sebagai file datar berurutan dan mempertahankan indeks paralel untuk pengambilan cepat. Bila diperlukan (reorganisasi, pemindaian ulang Wallet, layanan peer), data ini dibaca ulang sebagaimana adanya.



**Catatan:** Reorganisasi, atau sinkronisasi ulang, adalah fenomena di mana Blockchain mengalami modifikasi struktur karena adanya blok yang bersaing pada ketinggian yang sama. Hal ini terjadi ketika sebagian Blockchain digantikan oleh rantai lain dengan jumlah akumulasi pekerjaan yang lebih besar. Sinkronisasi ulang ini adalah bagian alami dari operasi Bitcoin, di mana penambang yang berbeda dapat menemukan blok baru hampir secara bersamaan, sehingga membelah jaringan Bitcoin menjadi dua. Dalam kasus seperti itu, jaringan dapat terpecah untuk sementara waktu menjadi rantai yang saling bersaing. Pada akhirnya, ketika salah satu rantai ini mengumpulkan lebih banyak pekerjaan, rantai yang lain akan ditinggalkan oleh node, dan blok mereka dikenal sebagai "blok usang" atau "blok yatim piatu" Proses penggantian satu rantai dengan rantai lainnya disebut sinkronisasi ulang.



#### File Blk * .dat (data blok mentah)



Blok yang diterima dan divalidasi ditulis ke wadah berurutan bernama `blkNNNNN.dat`, yang disimpan dalam folder `blocks/`. Setiap file diisi secara berurutan hingga mencapai ukuran maksimum 128 MiB, di mana pada saat itu Core membuka file berikutnya. Di dalam, setiap blok diserialisasikan dalam format jaringan, diawali dengan pengenal ajaib dan panjangnya. Pengaturan ini memungkinkan penulisan cepat ke disk dan memfasilitasi layanan blok untuk menyinkronkan rekan-rekan.



![Image](assets/fr/099.webp)



Dalam mode pruned, simpul hanya menyimpan jendela terbaru dari berkas-berkas ini untuk membatasi jejak disk. Mode ini menghapus container `blk*.dat` tertua segera setelah target ruang yang dikonfigurasi tercapai, sambil mempertahankan riwayat yang cukup untuk tetap konsisten dengan rantai yang paling terkenal. Indeks dan set UTXO tetap normal, memungkinkan transaksi dan blok berikutnya untuk divalidasi.



#### File Rev * .dat (data pembatalan)



Agar dapat kembali ke masa lalu selama reorganisasi, Core menyimpan, secara paralel dengan setiap file `blk`, file `revNNNNN.dat` di `blocks/`. File ini berisi informasi yang diperlukan untuk membatalkan efek blok pada set UTXO: untuk setiap output yang dikonsumsi oleh blok, status sebelumnya dari UTXO yang sesuai disimpan (jumlah, skrip, tinggi ...). Jika terjadi pembatalan blok, node dapat dengan cepat menyusun kembali keadaan sebelumnya tanpa harus memindai ulang seluruh rantai.



![Image](assets/fr/100.webp)



#### Indeks blok (blok/indeks)



Mencari sebuah blok secara langsung di dalam berkas datar akan terlalu memakan waktu. Oleh karena itu, Core memelihara basis data LevelDB di `blocks/index/` yang berisi daftar, untuk setiap blok yang diketahui, metadata seperti Hash, tinggi, status validasi, file `blk`, dan offset di mana blok tersebut berada. Ketika sebuah peer meminta sebuah blok, atau ketika sebuah komponen internal perlu mengakses blok tertentu, indeks ini menyediakan akses cepat. Tanpa indeks ini, terlalu banyak operasi yang diperlukan.



![Image](assets/fr/101.webp)



#### Indeks opsional (indeks/)



Beberapa indeks bersifat opsional dan dinonaktifkan secara default, karena indeks tersebut meningkatkan jejak disk:




- `indexes/txindex/`, yang telah kami sebutkan, menyediakan tabel pemetaan transaksi → lokasi, sehingga memungkinkan untuk mengambil transaksi yang telah dikonfirmasi tanpa mengetahui blok yang berisi transaksi tersebut. Ini berguna untuk kueri Wallet tipe `getrawtransaction` di luar RPC, tetapi cukup mahal.
- indexes/blockfilter/` yang dapat berisi filter blok ringkas (BIP157/158) untuk thin client. Struktur ini mempercepat verifikasi sisi klien dengan mengorbankan penyimpanan tambahan pada simpul pengindeks.



### Set UTXO (status rantai)



Model UTXO (*Output Transaksi yang Tidak Terpakai*) adalah representasi akuntansi dari Bitcoin: setiap output yang tidak terpakai adalah "Coin" yang tersedia yang dapat digunakan sebagai input untuk transaksi di masa depan.



![Image](assets/fr/102.webp)



Totalitas dari semua bagian ini pada saat tertentu T merupakan kumpulan UTXO: daftar besar dari semua bagian yang sekarang tersedia. Keadaan inilah yang dikonsultasikan oleh node untuk memutuskan apakah sebuah transaksi menggunakan unit yang sah yang belum digunakan dalam transaksi sebelumnya (untuk menghindari Double-spending).



![Image](assets/fr/103.webp)



Kumpulan UTXO disimpan dalam folder `chainstate/` sebagai basis data LevelDB yang ringkas. Setiap bagian mengaitkan kunci yang berasal dari Hash transaksi dan indeks keluaran dengan nilai yang berisi: jumlah, kunci `scriptPubKey`, tinggi blok pembuatan, dan indikator coinbase.



![Image](assets/fr/104.webp)



Node mempertahankan cache memori di atas LevelDB untuk menyerap operasi baca dan tulis yang sering dilakukan. Parameter `dbcache` dapat digunakan untuk memodifikasi ukuran cache ini: semakin besar ukurannya, semakin banyak akses memori yang diuntungkan oleh IBD dan validasi saat ini, dengan mengorbankan konsumsi RAM yang lebih tinggi. Ketika sebuah blok baru ditemukan oleh Miner, node menghapus dari UTXO mengatur output yang dihabiskan (atau dikonsumsi) oleh transaksi yang termasuk dalam blok tersebut dan menambahkan output yang baru dibuat.



Secara teoritis, kita dapat memvalidasi sebuah transaksi dengan memindai ulang riwayat blok untuk memeriksa apakah sebuah output belum pernah dibelanjakan. Akan tetapi, pada praktiknya, hal ini akan terlalu memakan waktu, karena seluruh Blockchain harus dipindai untuk setiap transaksi baru. Oleh karena itu, set UTXO menyediakan tampilan minimum yang diperlukan untuk membuktikan secara lokal dan dalam waktu yang wajar tidak adanya Double-spending.



Perhatikan bahwa set UTXO sering kali menjadi pusat perhatian tentang desentralisasi Bitcoin, karena ukurannya secara alami meningkat dengan cepat. Hal ini sebagian disebabkan oleh kenaikan harga Bitcoin, yang mendorong fragmentasi suku cadang, dan sebagian lagi karena adopsi sistem yang terus meningkat: semakin banyak pengguna, semakin besar permintaan UTXO.



![Image](assets/fr/105.webp)



Pertumbuhan set UTXO juga berasal dari struktur transaksi pembayaran sederhana pada Bitcoin. Memang, ketika Anda melakukan pembayaran, Anda mengonsumsi satu UTXO sebagai input dan membuat 2 UTXO baru sebagai output (satu untuk pembayaran dan satu lagi untuk Exchange). Terakhir, heuristik analisis rantai, yang disebut CIOH (*Common Input Ownership Heuristic*), memberikan insentif lebih lanjut untuk menghindari konsolidasi Coin.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Karena sebagian harus disimpan dalam RAM untuk memverifikasi transaksi dalam waktu yang wajar, set UTXO secara bertahap dapat membuat pengoperasian Full node menjadi terlalu mahal. Untuk mengatasi masalah ini, beberapa proposal sudah ada, terutama [Utreexo](https://planb.academy/resources/glossary/utreexo).



### Mempool



Mempool adalah kumpulan lokal dari transaksi valid yang telah diterima tetapi belum dikonfirmasi. Sebagai pengingat, "transaksi terkonfirmasi" adalah transaksi yang telah dimasukkan ke dalam blok yang valid. Setiap node menyimpan Mempool-nya sendiri, yang mungkin berbeda dengan node lain dalam jaringan, tergantung pada:




- ukuran yang dialokasikan ke Mempool melalui parameter `maxmempool`: node dengan Mempool yang lebih besar akan dapat menampung lebih banyak transaksi daripada node dengan Mempool yang lebih kecil (kecuali jika node yang terakhir menjadi kosong);
- aturan mempool: merupakan subset dari aturan perantara node dan menentukan karakteristik yang harus dipenuhi oleh transaksi yang belum dikonfirmasi agar diterima ke dalam mempool;
- perembesan transaksi: karena berbagai faktor, transaksi tertentu mungkin telah didistribusikan ke satu bagian jaringan, tetapi belum mencapai bagian lain.



Penting untuk dicatat bahwa mempool node tidak memiliki nilai konsensus. Bitcoin bekerja dengan sempurna meskipun setiap node memiliki Mempool yang berbeda. Pada akhirnya, blok otoritatif selalu merupakan blok yang ditambahkan ke Blockchain. Sebagai contoh, meskipun sebuah node pada awalnya menolak transaksi yang diberikan dalam Mempool-nya (valid menurut aturan konsensus), node tersebut akan berkewajiban untuk menerimanya jika pada akhirnya dimasukkan ke dalam blok dengan Proof of Work yang valid. Jika ia gagal melakukannya dan menolak blok ini, meskipun sesuai dengan aturan konsensus, maka akan memicu Hard Fork, yaitu pembuatan Bitcoin yang baru dan terpisah di mana ia akan berdiri sendiri.



#### Kebijakan dan manajemen memori



Ketika sebuah transaksi diterima, Core menerapkan serangkaian pemeriksaan terhadap aturan konsensus (sintaks, skrip yang valid, tidak ada pengeluaran ganda, dll.) dan aturan Mempool, yang merupakan kebijakan lokal (RBF, ambang batas biaya minimum, batas data dalam `OP_RETURN`, dll.). Jika transaksi mematuhi aturan-aturan ini, maka transaksi akan disimpan dalam memori.



Ukuran Mempool dibatasi oleh parameter `maxmempool` dalam file `Bitcoin.conf` (lebih lanjut mengenai hal ini dalam bab berikutnya). Secara default, batasnya adalah 300 MB. Ketika sudah penuh, node akan secara dinamis menaikkan ambang batas muatan minimumnya dan mengeluarkan transaksi yang paling tidak menguntungkan terlebih dahulu (dengan kata lain, node akan menyimpan transaksi yang harus ditambang terlebih dahulu). Transaksi yang terlalu lama juga dapat kedaluwarsa setelah penundaan yang dikonfigurasi.



#### Kegigihan Mempool pada disk



Untuk mempercepat restart, Core secara berkala menserialisasi status Mempool dalam file `Mempool.dat` ketika node dimatikan. Selain Mempool yang sebenarnya, yang tetap berada di memori, Core menyimpan file `Mempool.dat` ini pada disk. Saat berikutnya node diluncurkan, node akan memuat ulang snapshot ini dan menghapus apa pun yang tidak lagi valid untuk Blockchain saat ini.



### File dan basis data tambahan



Beberapa file lain pada tingkat yang sama dengan `blocks/`, `chainstate/`, dan `indexes/` ikut serta dalam berfungsinya file :




- `peers.dat` menyimpan buku IP Address yang berisi peers potensial, yang diperoleh dari penemuan DNS awal, pertukaran jaringan, dan penambahan secara manual. Ketika node mulai hidup, node dapat menggunakan file ini untuk membuat koneksi keluar.
- Ketika node dimatikan, `anchors.dat` menyimpan alamat rekan-rekan yang keluar, sehingga Anda dapat mencoba menghubungi mereka lagi dengan cepat pada saat Anda memulai lagi.
- `banlist.json` berisi larangan lokal yang diputuskan oleh operator atau oleh node (perilaku tidak valid yang berulang), untuk mencegah node menyambung kembali atau menerima koneksi dari rekan-rekan tertentu.
- `fee_estimates.dat` menyimpan statistik horizon waktu pada konfirmasi yang diamati, yang digunakan oleh estimator biaya untuk mengusulkan tarif biaya yang konsisten dengan tujuan penundaan yang dipilih saat membuat transaksi.
- `bitcoin.conf` berisi parameter konfigurasi node Anda. Dalam file inilah aturan perantara dapat disesuaikan. Saya akan membahasnya lebih detail di bab berikutnya;
- `settings.json` berisi parameter tambahan untuk `Bitcoin.conf`.
- `debug.log` adalah log teks diagnostik, yang dapat digunakan untuk memahami aktivitas node jika terjadi bug.
- `bitcoind.pid` mencatat ID proses selama eksekusi, memungkinkan aplikasi atau skrip lain untuk dengan mudah mengidentifikasi Bitcoind (*Bitcoin Daemon*) dan berinteraksi dengannya jika diperlukan. File ini dibuat saat node dijalankan dan dihapus saat node berhenti;
- `ip_asn.map` adalah tabel pemetaan IP → ASN (sistem mandiri) yang digunakan untuk bucketing dan diversifikasi peer (opsi `-asmap`).
- `onion_v3_private_key` menyimpan kunci privat dari layanan Tor v3 ketika opsi `-listenonion` diaktifkan, untuk menjaga kestabilan onion Address di antara proses reboot.
- `i2p_private_key` menyimpan kunci privat I2P ketika `-i2psam=` digunakan, untuk membuat koneksi keluar dan mungkin masuk pada I2P.
- `.cookie` berisi autentikasi RPC token sementara (dibuat saat pengaktifan, dihapus saat pematian) ketika autentikasi cookie digunakan. Ini dapat digunakan, misalnya, untuk menghubungkan perangkat lunak Wallet.
- `.lock` adalah kunci direktori data, yang mencegah beberapa instance menulis ke datadir yang sama secara bersamaan.
- `guisettings.ini.bak` adalah penyimpanan otomatis pengaturan GUI (*Bitcoin Qt*) ketika opsi `resetguisettings` digunakan.



Seperti yang telah kita lihat di bagian pertama kursus BTC 202 ini, Bitcoin core adalah perangkat lunak node Bitcoin dan Wallet. Namun, ini bukanlah solusi yang saya rekomendasikan untuk mengelola wallet Anda, karena Interface masih sangat sederhana dan fungsinya terbatas dibandingkan dengan perangkat lunak modern seperti Sparrow atau Liana. Core juga menyertakan file untuk mengelola dompet Anda:





- `wallets/` adalah direktori default yang menampung satu atau lebih dompet;
- `wallets/<name>/Wallet.dat` adalah basis data SQLite dari Wallet (kunci, deskriptor, metadata transaksi, dll.);
- `wallets/<name>/wallet.dat-journal` adalah jurnal rollback SQLite.



Sebagai rangkuman, berikut ini adalah struktur file Bitcoin core:



```
~/.bitcoin/
├── bitcoin.conf
├── blocks/
│   ├── blk00000.dat
│   ├── blk00001.dat
│   ├── rev00000.dat
│   ├── rev00001.dat
│   └── index/
├── chainstate/
├── indexes/
│   ├── txindex/
│   ├── blockfilter/
│   │   └── basic/
│   │       ├── db/
│   │       └── fltrNNNNN.dat
│   └── coinstats/
│       └── db/
├── wallets/
│   └── <wallet_name>/
│       ├── wallet.dat
│       └── wallet.dat-journal
├── peers.dat
├── anchors.dat
├── banlist.json
├── mempool.dat
├── fee_estimates.dat
├── bitcoind.pid
├── debug.log
├── ip_asn.map
├── onion_v3_private_key
├── i2p_private_key
├── settings.json
├── guisettings.ini.bak
├── .cookie
└── .lock
```



### Jalur validasi untuk blok baru



Setelah menerima blok baru, node Anda memeriksa Proof of Work dan, secara umum, kepatuhan terhadap aturan konsensus. Jika semuanya baik-baik saja, ia akan menerapkan perubahan transaksi demi transaksi ke dalam set UTXO: ia memeriksa bahwa setiap entri menggunakan UTXO yang ada dengan skrip yang valid, menghapus UTXO ini, dan menambahkan jalan keluar yang baru. Jika semuanya valid, perubahan akan dikomit ke `chainstate/`.



Secara paralel, data pembatalan ditulis ke `rev*.dat` dan metadata ke indeks `blocks/index/`. Blok kemudian diserialisasikan ke file `blk*.dat` yang benar. Jika terjadi reorganisasi, simpul membaca `rev*.dat` secara terbalik untuk memutuskan blok yang ditinggalkan dengan bersih, mengembalikan set UTXO, dan kemudian menghubungkan blok-blok dari rantai terbaik yang baru.





## Memahami Bitcoin.conf


<chapterId>c54a629a-ddb1-41cb-9a88-21dfd9be50ca</chapterId>



File `Bitcoin.conf` adalah file konfigurasi Interface utama untuk Bitcoin core. Ini memungkinkan Anda untuk menyesuaikan perilaku dan parameter node Anda tanpa harus mengkompilasi ulang kode sumbernya atau membuat modifikasi baris perintah. Secara konkret, ini adalah file teks biasa yang terstruktur dalam pasangan nilai-kunci, yang berarti bahwa setiap baris file mereferensikan parameter tertentu (kunci) dan nilai terkait, yang dapat dimodifikasi untuk menyesuaikan parameter itu.



Jaringan, relai transaksi, kinerja, pengindeksan, pencatatan, dan parameter akses RPC dapat didefinisikan dalam `Bitcoin.conf`. Namun, file konfigurasi ini tidak pernah mengubah aturan konsensus protokol: file ini hanya menetapkan kebijakan lokal node (aturan relay), cara menghubungkan, mengindeks, dan mengekspos layanan.



### Lokasi dan prioritas



Secara default, `Bitcoin.conf` berada di direktori data Bitcoin core. Ini adalah direktori terkenal yang kami sebutkan pada bab sebelumnya. Namun, file ini tidak secara otomatis dibuat oleh Bitcoin core, kecuali pada lingkungan tertentu, seperti Umbrel. Jika belum ada, Anda harus membuat generate sendiri dengan membuat file bernama `Bitcoin.conf`, lalu membukanya dalam editor teks untuk membuat modifikasi.



Parameter yang ditentukan dalam `Bitcoin.conf` dapat ditimpa oleh 2 lapisan:




- `settings.json` (ditulis secara dinamis oleh grafis Interface atau beberapa RPC),
- dan opsi yang dimodifikasi melalui baris perintah.



Perhatikan bahwa modifikasi apa pun pada `Bitcoin.conf` memerlukan restart node untuk menerapkannya.



### Format dan struktur



Oleh karena itu, format `Bitcoin.conf` sangat sederhana: satu baris per opsi, dalam bentuk `option=value`. Spasi yang tidak perlu dan baris kosong diabaikan, dan komentar kode dimulai dengan `#`.



Hampir semua opsi Boolean dapat dinonaktifkan dengan awalan `no`. Sebagai contoh, `dengarkan=0` dan `nolisten=1` adalah setara, tergantung versinya.



Untuk mengelompokkan konfigurasi berdasarkan jaringan, Anda dapat menggunakan bagian: `[main]`, `[test]` (testnet3), `[testnet4]`, `[bookmark]`, `[regtest]`. Atau, Anda dapat mengawali nama opsi dengan `regtest.maxmempool=100`.



### Apa yang bisa dan tidak bisa dilakukan Bitcoin.conf



Seperti yang dijelaskan di atas, aturan konsensus jelas tidak dapat dikonfigurasi dalam `Bitcoin.conf`, karena hal ini dapat membuat Hard Fork. Di sisi lain, banyak aspek lain yang dapat dikonfigurasi. Ada 3 kelas yang berguna untuk diingat:




- Parameter lokal murni. Parameter ini hanya mempengaruhi simpul Anda: ukuran cache (`dbcache`), mode pruned (`prune`), indeks opsional... Parameter-parameter ini mempengaruhi kinerja mesin Anda, tetapi tidak mempengaruhi jaringan.
- Kebijakan Relay dan Mempool. Kebijakan-kebijakan ini memutuskan apa yang diterima, disimpan, dan direlay oleh node Anda sebelum konfirmasi: ambang batas biaya minimum (`minrelaytxfee`), ukuran dan waktu penyimpanan Mempool (`maxmempool`, `mempoolexpiry`), penggantian transaksi (RBF)... Aturan-aturan ini bukan bagian dari konsensus, sehingga dua node yang berbeda dapat memiliki kebijakan yang berbeda dan masih sepenuhnya kompatibel. Di sisi lain, parameter-parameter ini akan memiliki pengaruh pada jaringan Bitcoin (seperti yang dijelaskan pada bagian pertama, terutama dengan teori perkolasi).
- Konektivitas jaringan. Opsi-opsi ini menentukan bagaimana node Anda menemukan rekan, mendengarkan, melintasi NAT, menggunakan Tor atau proksi, atau membatasi bandwidth. Opsi-opsi ini membentuk topologi Anda, tetapi tidak mengubah pengiriman transaksi.



Memahami pemisahan ini sangatlah penting: jika sebuah transaksi tidak mematuhi aturan konsensus, maka node Anda akan menolaknya. Tetapi kebijakan lokal yang lebih ketat dapat menolak untuk menyampaikan transaksi yang valid dalam pengertian konsensus.



### Jaringan dan topologi



Pertama-tama, penting untuk membedakan dengan jelas antara 2 jenis koneksi yang dapat dimiliki oleh node Bitcoin:




- Sambungan keluar, yang dimulai oleh node kita ke node lain;



![Image](assets/fr/106.webp)





- Sambungan masuk, dimulai oleh node lain ke node kita.



![Image](assets/fr/107.webp)



Kedua jenis koneksi ini sangat mampu untuk bertukar data yang sama di kedua arah; ini bukan masalah membatasi arah aliran, tetapi hanya perbedaan dalam inisiator koneksi. Dari sudut pandang node kami, koneksi keluar umumnya dianggap lebih aman, karena kami menginisiasinya dan memilih dengan tepat node mana yang akan terhubung, sehingga kecil kemungkinannya koneksi tersebut berbahaya. Secara default, Bitcoin core mempertahankan 10 koneksi keluar (8 "*full-relay*" + 2 "*block-relay-only*").



Full node menambah nilai lebih pada jaringan dengan menerima koneksi yang masuk. Parameter `listen=1` memungkinkan mendengarkan pada port default 8333 dari jaringan yang bersangkutan, memungkinkan koneksi yang masuk ini diterima di clearnet. Agar dapat berfungsi, port ini juga harus terbuka pada router Anda. Jika tidak, node Anda akan terus bekerja dengan koneksi keluar saja, yang tidak akan berdampak pada penggunaan pribadi Bitcoin Anda. Pilihan untuk mengizinkan koneksi masuk ada di tangan Anda; tidak ada "pilihan terbaik"



Jika Anda memilih untuk tidak membuka port pada router Anda, tetapi masih menerima sambungan masuk, Anda dapat mengaktifkan parameter `listenonion=1`. Ini akan mencapai hasil yang sama, tetapi hanya melalui jaringan Tor dan bukan clearnet.



Di tingkat jaringan, kami juga memiliki:




- `addnode`: menambahkan teman sebaya ke kontak selain penemuan biasa (dapat ditentukan beberapa kali).
- `connect`: secara ketat membatasi koneksi ke alamat yang diberikan (dapat ditentukan beberapa kali). Core tidak akan terhubung ke node lain;
- `seednode`: hanya digunakan untuk mengisi buku-Address saat menyambung ke node, kemudian memutuskan sambungan.
- `maxconnections`: mendefinisikan batas atas global untuk koneksi masuk + keluar. Secara default, parameter ini disetel ke 125, yang berarti bahwa node Anda tidak akan pernah menerima lebih dari 125 koneksi.
- `maxuploadtarget` : membatasi unggahan untuk mengendalikan bandwidth dalam jangka waktu bergulir 24 jam. Batas ini tidak mengorbankan penyebaran elemen penting yang baru;
- `onlynet`: membatasi koneksi keluar hanya pada jaringan tertentu (`ipv4`, `ipv6`, `onion`, `i2p`, `cjdns`). Sebagai contoh, jika Anda ingin node Anda terhubung ke jaringan Bitcoin hanya melalui Tor, Anda dapat mengaktifkan parameter `onlynet=onion` dan menonaktifkan koneksi yang masuk (atau hanya mengizinkan koneksi melalui Tor juga).
- dnsseed`: mengizinkan atau melarang _DNS seeds_ untuk meminta peer ketika pool Address lokal Anda rendah (default: `1`, kecuali `-connect` atau `-maxconnections=0`).
- `forcednsseed`: memaksa _DNS seeds_ untuk diminta pada saat startup, bahkan jika Anda sudah memiliki stok alamat (default: `0`).
- `benih tetap`: Izinkan penggunaan *simpul seed* (daftar Address yang dikodekan dengan kode keras) jika _benih DNS_ gagal atau dinonaktifkan (default: `1`).
- `dns`: Mengesahkan resolusi DNS secara umum (misalnya, untuk `-addnode`/`-seednode`/`-connect`).



Secara default, node Anda berkomunikasi melalui clearnet, Tor, dan I2P. Ini berarti bahwa rekan-rekan yang terhubung dengannya di clearnet dapat melihat IP publik Anda Address, dan ISP Anda kemungkinan akan dapat mendeteksi bahwa Anda menjalankan node Bitcoin (meskipun P2P Transport V2 membuat lebih sulit bagi ISP untuk menguping). Ini tidak selalu menjadi masalah, tetapi jika Anda ingin menghindari kebocoran informasi ini, Anda dapat menyambungkan node Anda secara eksklusif melalui jaringan Tor.



Untuk sepenuhnya mendukung Tor, Anda perlu memaksa Bitcoin core untuk hanya menggunakan jaringan ini dan membuat layanan tersembunyi untuk koneksi yang masuk (jika Anda ingin mengaktifkannya). Dalam `Bitcoin.conf`, Anda perlu menambahkan konfigurasi ini:




- `onlynet=onion`,
- `proxy=127.0.0.1:9050`,
- `listenonion=1`,
- `torcontrol=127.0.0.1:9051`,
- `proxyrandomize=1`,
- `dengarkan=1`,
- `bind=127.0.0.1`,
- `upnp=0`,
- `natpmp=0`.



Semua koneksi P2P Anda melalui Tor. Node Anda menerima `.onion` Address untuk sambungan masuk, jadi tidak ada port yang perlu dibuka pada router. ISP Anda hanya melihat lalu lintas Tor, dan rekan-rekan Anda tidak mengetahui IP publik Anda yang sebenarnya Address.



Untuk menghindari resolusi DNS secara jelas, Anda dapat menambahkan `dnsseed=0` dan `dns=0` pada konfigurasi Anda. Anda kemudian harus menyediakan peer `.onion` secara manual melalui `seednode=` atau `addnode=`, karena jika tidak, penemuan node baru akan sulit dilakukan.



Tentunya, jika Anda seorang pemula, saya sarankan Anda untuk membiarkan semua pengaturan jaringan ini untuk sementara waktu. Konfigurasi default sering kali sudah cukup.



### Mempool dan kebijakan relai



#### Parameter dasar



Berikut ini adalah parameter dasar yang dapat Anda modifikasi pada `Bitcoin.conf` Anda terkait pengelolaan Mempool dan penyampaian transaksi yang belum dikonfirmasi:





- `maxmempool=<n>`: Membatasi ukuran maksimum Mempool lokal hingga `<n>` megabyte (default: `300`). Ketika batas tersebut tercapai, node Anda secara dinamis menaikkan ambang batas biaya efektif dan memprioritaskan transaksi yang paling tidak menguntungkan (berdasarkan tingkat biaya, bukan nilai absolut) untuk tetap berada di bawah batas tersebut. Anda dapat membiarkan pengaturan ini sebagai default. Meningkatkannya dapat berguna jika Anda menggunakan Mining secara solo, atau jika Anda ingin mendapatkan pandangan yang lebih akurat tentang kemacetan Mempool dan meningkatkan estimasi biaya. Sebaliknya, menguranginya akan menghemat RAM dan, pada tingkat yang lebih rendah, sumber daya sistem lainnya.





- `mempoolexpiry=<n>`: Waktu penyimpanan maksimum untuk transaksi yang belum dikonfirmasi di Mempool (dalam jam, default: `336`). Setelah waktu ini, transaksi akan dihapus meskipun ruang masih tersedia.





- `persistmempool=1`: Menyimpan snapshot Mempool saat berhenti dan memuatnya kembali saat reboot (default: `1`). Hal ini mempercepat pemulihan setelah reboot, sehingga tidak perlu mempelajari ulang status melalui jaringan.





- `maxorphantx=<n>`: Jumlah maksimum transaksi anak yatim yang dipertahankan (input tergantung dari UTXO yang belum terlihat dalam set UTXO, default: `100`). Di luar ambang batas ini, transaksi tertua akan dihapus untuk menghindari pertumbuhan cache yang tidak terkendali.





- `blocksonly=1` : Menonaktifkan penerimaan dan penerusan transaksi yang belum dikonfirmasi dari rekan (kecuali dengan izin khusus). Node hanya mengunduh dan mengumumkan blok. Transaksi yang dibuat secara lokal masih dapat disiarkan (untuk menggunakan node Anda dengan perangkat lunak dompet Anda). Ini sangat mengurangi penggunaan bandwidth dan kebutuhan RAM dengan mengorbankan kegunaan relay dan tanpa pengetahuan tentang mempool.





- `minrelaytxfee=<n>`: Tingkat biaya minimum (dalam BTC/kvB) di bawahnya, transaksi tidak diterima di Mempool node dan tidak direlay ke rekan-rekannya (default: `0.00001` = 1 sat/kvB). Semakin tinggi nilai ini, semakin agresif node Anda menyaring transaksi berbiaya rendah.





- `mempoolfullrbf=1`: Menerima transaksi RBF bahkan tanpa sinyal RBF eksplisit dalam transaksi yang digantikan. Dengan kebijakan "*full-RBF*" ini, sebuah transaksi yang menawarkan tingkat biaya yang lebih tinggi dapat menggantikan transaksi lain dalam Mempool jika kondisi penggantian lainnya terpenuhi.



Sebagai pengingat, RBF adalah sebuah mekanisme transaksi yang memungkinkan pengirim untuk mengganti sebuah transaksi dengan transaksi yang memiliki biaya yang lebih tinggi untuk mempercepat konfirmasi. Jika transaksi dengan biaya yang terlalu rendah tetap diblokir, pengirim dapat menggunakan *Replace-by-fee* untuk meningkatkan biaya dan memprioritaskan transaksi pengganti mereka di mempool dan dengan penambang.



#### Pengaturan lanjutan dan spesifik



Berikut ini adalah pengaturan lanjutan untuk Mempool dan kebijakan relai. Jika Anda seorang pemula, Anda tidak perlu memodifikasi pengaturan ini:





- `datacarrier=1` : Mengizinkan relay dan (jika menambang melalui node) penyertaan transaksi yang membawa data non-keuangan melalui output `OP_RETURN` (default: `1`). Menonaktifkan parameter ini sedikit mengurangi potensi spam data non-keuangan dengan mengorbankan kompatibilitas dengan beberapa penggunaan. Dalam semua kasus, Anda harus menerima `OP_RETURN` yang ditambang.





- `datacarriersize = <n>`: Ukuran maksimum (dalam byte) dari `OP_RETURN` yang direlay oleh node (default: `83`). Menurunkan nilai ini akan membatasi muatan yang diangkut melalui `OP_RETURN`. Perhatikan bahwa batas ini akan dihapus secara default dalam versi Bitcoin core yang akan datang.





- `bytespersigop=<n>`: Parameter yang mengubah transaksi tanda tangan menjadi byte yang setara untuk evaluasi batas relai (default: `20`). Ini akan mempengaruhi penerimaan transaksi kaya `sigops` sesuai dengan aturan kebijakan lokal.





- `permitbaremultisig = 1`: Mengizinkan pengiriman ulang transaksi P2MS *bare-Multisig* (default: `1`). Ini adalah templat skrip tertua untuk menetapkan kondisi multisignature pada UTXO (ditemukan pada tahun 2011 oleh Gavin Andresen).





- `whitelistrelay=1`: Secara otomatis memberikan izin relai kepada peer yang masuk dalam daftar putih (default: `1`). Peers ini memiliki transaksi yang diterima oleh relai meskipun node Anda tidak dalam mode relai umum.





- `whitelistforcerelay=1`: Menetapkan izin "*forcerelay*" ke peer yang masuk daftar putih dengan izin default (default: `0`). Node kemudian merelay transaksi mereka meskipun sudah ada di Mempool, sehingga melewati mekanisme anti-redundansi.





- `whitebind=<[permissions@]addr>` / `whitelist=<[permissions@]CIDR>`: Mengikat rentang Interface atau Address dan memberikan izin yang lebih halus kepada rekan-rekan yang sesuai: `relay`, `forcerelay`, `Mempool` (permintaan konten Mempool), `noban`, `download`, `addr`, `bloomfilter`. Ini dapat berguna untuk memberikan perlakuan istimewa kepada rekan-rekan tepercaya (seperti gateway, LAN, dan layanan internal).





- `peerbloomfilters=1` : Mengaktifkan dukungan untuk filter Bloom (BIP37) guna melayani blok/transaksi yang difilter ke klien ringan (default: `0`). Perhatian, ini meningkatkan beban pada sumber daya Anda.





- `peerblockfilters=1` : Menyediakan filter kompak BIP157 (*Neutrino*) ke rekan (default: `0`).





- `blockreconstructionextratxn=<n>`: Jumlah transaksi tambahan yang disimpan dalam memori untuk membangun kembali blok ringkas (default: `100`). Meningkatkan keberhasilan rekonstruksi selama sinkronisasi ringkas, dengan mengorbankan sedikit memori.



Sebagai pengingat, semua aturan relai ini tidak berdampak pada validitas transaksi yang termasuk dalam blok yang valid. Aturan-aturan ini berfungsi untuk menyesuaikan kontribusi Anda pada relai, melindungi sumber daya Anda, dan membuat node Anda dapat diprediksi dalam lingkungan yang terbatas, tetapi tidak pernah mengizinkan Anda untuk menolak blok yang menghormati aturan konsensus.



### Dompet



Anda juga dapat mengatur cara pengelolaan wallet Anda dalam file `Bitcoin.conf`. Jika Anda tidak menggunakan Wallet secara langsung di Core, tetapi menggunakan perangkat lunak manajemen eksternal seperti Sparrow atau Liana, parameter ini tidak terlalu penting:





- `addresstype=<legacy|p2sh-segwit|bech32|bech32m>` : Menentukan format alamat yang dihasilkan oleh dompet untuk penerimaan.





- `changetype = <legacy|P2SH-SegWit|bech32|bech32m>`: Memaksakan format Exchange Address (sisa input pada satu pembayaran).





- `Wallet=<path>`: Memuat Wallet yang sudah ada saat pengaktifan (dapat diulang untuk memuat beberapa dompet).





- `walletdir=<dir>`: Direktori yang berisi wallet (default: `<datadir>/wallets` jika ada, jika tidak, `<datadir>`). Ini dapat berguna jika anda ingin menyimpan wallet pada volume khusus atau terenkripsi.





- `walletbroadcast=1`: Secara otomatis menyiarkan transaksi yang dibuat oleh dompet yang dimuat (default: `1`). Atur ke `0` jika Anda ingin mengelola siaran melalui saluran lain.





- `walletrbf=1`: Mengaktifkan keikutsertaan RBF untuk memberi sinyal RBF pada semua transaksi (default: `1`). Memungkinkan Anda untuk meningkatkan biaya di kemudian hari jika terjadi transaksi yang diblokir.





- `txconfirmtarget=<n>`: Target konfirmasi untuk transaksi (dalam jumlah blok, default: `6`). Wallet akan secara otomatis menetapkan biaya untuk transaksi yang akan dikonfirmasi dalam jumlah blok ini.





- `paytxfee=<amt>`: Tarif biaya tetap (BTC/kvB) yang diterapkan pada transaksi Wallet. Hindari secara umum: gunakan estimasi adaptif melalui `txconfirmtarget`.





- `fallbackfee=<amt>` : Tarif cadangan (BTC/kvB) yang digunakan jika estimator kekurangan data (default: `0.00`). Mengaturnya ke 0 akan menonaktifkan fallback sepenuhnya.





- `mintxfee=<amt>`: Ambang batas minimum (BTC/kvB) untuk Wallet untuk membuat transaksi (default: `0.00001`). Wallet akan menolak membuat transaksi di bawah ambang batas ini.





- `maxtxfee=<amt>`: Batas absolut pada total biaya untuk transaksi Wallet (default: `0.10` BTC). Melindungi dari biaya yang sangat tinggi yang tidak perlu yang akan menghancurkan bitcoin.





- `hindari pengeluaran parsial = 1`: Memilih UTXO berdasarkan cluster Address untuk menghindari pengeluaran sebagian.





- `spendzeroconfchange=1`: Memungkinkan UTXO Exchange yang belum dikonfirmasi untuk digunakan kembali sebagai entri dalam transaksi baru (default: `1`).





- `consolidatefeerate=<amt>`: Tingkat maksimum (BTC/kvB) di luar itu Wallet menghindari menambahkan lebih banyak input daripada yang diperlukan untuk konsolidasi. Hal ini memungkinkan konsolidasi oportunistik dengan harga rendah dan mengurangi biaya ketika biaya tinggi.





- `maxapsfee=<n>`: Anggaran untuk biaya tambahan (BTC, nilai absolut) yang disetujui oleh Wallet untuk membayar untuk mengaktifkan opsi "*hindari pengeluaran sebagian*".





- `discardfee=<amt>`: Nilai (BTC/kvB) yang menunjukkan toleransi Anda untuk membuang Exchange dengan menambahkannya ke biaya. Keluaran yang harganya lebih dari sepertiga nilainya dengan tarif ini akan dibuang.





- `keypool=<n>`: Ukuran kumpulan Address yang telah dibuat sebelumnya (default: `1000`). Nilai yang terlalu kecil akan meningkatkan risiko pemulihan yang tidak lengkap.


Hampir semua opsi Boolean dapat dinonaktifkan dengan awalan `no`. Sebagai contoh, `listen=0` dan `nolisten=1` adalah setara, tergantung versinya.

Untuk mengelompokkan konfigurasi berdasarkan jaringan, Anda dapat menggunakan bagian: `[main]`, `[test]` (testnet3), `[testnet4]`, `[bookmark]`, `[regtest]`. Atau, Anda dapat mengawali nama opsi dengan `regtest.maxmempool=100`.

### Apa yang bisa dan tidak bisa dilakukan Bitcoin.conf

Seperti yang dijelaskan di atas, aturan konsensus jelas tidak dapat dikonfigurasi di `Bitcoin.conf`, karena ini dapat membuat Hard Fork. Di sisi lain, banyak aspek lain yang dapat dikonfigurasi. Ada 3 kelas berguna yang perlu diingat:

- Parameter murni lokal. Ini hanya memengaruhi node Anda: ukuran cache (`dbcache`), mode pangkas (`prune`), indeks opsional... Ini memengaruhi kinerja mesin Anda, tetapi tidak memengaruhi jaringan.
- Kebijakan Relay dan Mempool. Ini memutuskan apa yang diterima, disimpan, dan diteruskan oleh node Anda sebelum konfirmasi: ambang batas biaya minimum (`minrelaytxfee`), ukuran Mempool dan waktu retensi (`maxmempool`, `mempoolexpiry`), penggantian transaksi (RBF)... Aturan-aturan ini bukan bagian dari konsensus, jadi dua node yang berbeda dapat memiliki kebijakan yang berbeda dan tetap sepenuhnya kompatibel. Di sisi lain, parameter ini akan berpengaruh pada jaringan Bitcoin (seperti yang dijelaskan di bagian pertama, terutama dengan teori perkolasi).
- Konektivitas jaringan. Opsi ini menentukan bagaimana node Anda menemukan peer, mendengarkan, melintasi NAT, menggunakan Tor atau proksi, atau membatasi bandwidth-nya. Opsi ini membentuk topologi Anda, tetapi tidak mengubah relai transaksi.

Memahami pemisahan ini sangat penting: jika sebuah transaksi tidak mematuhi aturan konsensus, node Anda akan menolaknya dalam kasus apa pun. Tetapi kebijakan lokal yang lebih ketat dapat menolak untuk merelai transaksi yang valid dalam arti konsensus.

### Jaringan dan topologi

Pertama-tama, penting untuk membedakan dengan jelas antara 2 jenis koneksi yang dapat dimiliki oleh node Bitcoin:

- Koneksi keluar (outgoing connections), yang dimulai oleh node kita ke node lain;

![Image](assets/fr/106.webp)

- Koneksi masuk (incoming connections), yang dimulai oleh node lain ke node kita.

![Image](assets/fr/107.webp)

Kedua jenis koneksi ini sangat mampu bertukar data yang sama di kedua arah; ini bukan masalah membatasi arah aliran, tetapi hanya perbedaan pada inisiator koneksi. Dari sudut pandang node kita, koneksi keluar umumnya dianggap lebih aman, karena kita yang memulainya dan memilih dengan tepat node mana yang akan dihubungi, sehingga kecil kemungkinannya koneksi tersebut berbahaya. Secara default, Bitcoin Core mempertahankan 10 koneksi keluar (8 "_full-relay_" + 2 "_block-relay-only_").

Sebuah full node menambah lebih banyak nilai ke jaringan dengan menerima koneksi masuk. Parameter `listen=1` memungkinkan listening pada port default 8333 dari jaringan yang bersangkutan, memungkinkan koneksi masuk ini diterima di clearnet. Agar ini berfungsi, port ini juga harus terbuka di router Anda. Jika tidak, node Anda akan terus bekerja hanya dengan koneksi keluar, yang tidak akan berdampak pada penggunaan pribadi Bitcoin Anda. Pilihan apakah akan mengizinkan koneksi masuk adalah milik Anda; tidak ada "pilihan terbaik."

Jika Anda lebih suka tidak membuka port di router Anda, tetapi tetap ingin menerima koneksi masuk, Anda dapat mengaktifkan parameter `listenonion=1`. Ini akan mencapai hasil yang sama, tetapi hanya melalui jaringan Tor, bukan clearnet.

Di tingkat jaringan, kami juga memiliki:

- `addnode`: menambahkan peer untuk dihubungi selain penemuan biasa (dapat ditentukan beberapa kali).
- `connect`: ecara ketat membatasi koneksi ke alamat yang disediakan (dapat ditentukan beberapa kali). Core tidak akan terhubung ke node lain;
- `seednode`: hanya digunakan untuk mengisi address book saat menyambung ke node, kemudian memutuskan sambungan.
- `maxconnections`: mendefinisikan batas global untuk koneksi masuk + keluar. Secara default, parameter ini diatur ke 125, yang berarti node Anda tidak akan pernah menerima lebih dari 125 koneksi.
- `maxuploadtarget` : membatasi unggahan untuk membatasi bandwidth selama jendela 24 jam bergulir. Batas ini tidak mengorbankan penyebaran elemen-elemen penting terbaru;
- `onlynet`: membatasi koneksi keluar hanya pada jaringan tertentu (`ipv4`, `ipv6`, `onion`, `i2p`, `cjdns`). Sebagai contoh, jika Anda ingin node Anda terhubung ke jaringan Bitcoin hanya melalui Tor, Anda dapat mengaktifkan parameter `onlynet=onion` dan menonaktifkan koneksi yang masuk (atau hanya mengizinkan koneksi melalui Tor juga).
- `dnsseed`: mengizinkan atau melarang _DNS seeds_ untuk meminta peer ketika pool Address lokal Anda rendah (default: `1`, kecuali `-connect` atau `-maxconnections=0`).
- `forcednsseed`: memaksa _DNS seeds_ untuk diminta pada saat startup, bahkan jika Anda sudah memiliki stok alamat (default: `0`).
- `fixedseeds`: Izinkan penggunaan *seed node* (daftar Address yang dikodekan dengan hardcode) jika _DNS seeds_ gagal atau dinonaktifkan (default: `1`).
- `dns`: Mengesahkan resolusi DNS secara umum (misalnya, untuk `-addnode`/`-seednode`/`-connect`).

Secara default, node Anda berkomunikasi melalui clearnet, Tor, dan I2P. Ini berarti bahwa rekan-rekan yang terhubung dengannya di clearnet dapat melihat IP publik Anda Address, dan ISP Anda kemungkinan akan dapat mendeteksi bahwa Anda menjalankan node Bitcoin (meskipun P2P Transport V2 membuat lebih sulit bagi ISP untuk menguping). Ini tidak selalu menjadi masalah, tetapi jika Anda ingin menghindari kebocoran informasi ini, Anda dapat menyambungkan node Anda secara eksklusif melalui jaringan Tor.

Secara default, node Anda berkomunikasi melalui clearnet, Tor, dan I2P. Ini berarti bahwa peer yang terhubung dengannya di clearnet dapat melihat alamat IP publik Anda, dan ISP Anda kemungkinan besar akan dapat mendeteksi bahwa Anda menjalankan node Bitcoin (meskipun P2P Transport V2 membuatnya lebih sulit bagi ISP untuk mengintai). Ini tidak selalu menjadi masalah, tetapi jika Anda ingin menghindari kebocoran informasi ini, Anda dapat menghubungkan node Anda secara eksklusif melalui jaringan Tor.

Agar sepenuhnya Tor-enabled, Anda perlu memaksa Bitcoin Core untuk hanya menggunakan jaringan ini dan membuat layanan tersembunyi (hidden service) untuk koneksi masuk (jika Anda ingin mengaktifkannya). Di `Bitcoin.conf`, Anda perlu menambahkan konfigurasi ini:

- `onlynet=onion`,
- `proxy=127.0.0.1:9050`,
- `listenonion=1`,
- `torcontrol=127.0.0.1:9051`,
- `proxyrandomize=1`,
- `listen=1`,
- `bind=127.0.0.1`,
- `upnp=0`,
- `natpmp=0`.

Semua koneksi P2P Anda melewati Tor. Node Anda menerima alamat `.onion` untuk koneksi masuk, jadi tidak perlu membuka port di router. ISP Anda hanya melihat lalu lintas Tor, dan peer Anda tidak mengetahui alamat IP publik Anda yang sebenarnya.

Untuk menghindari resolusi DNS secara jelas, Anda dapat menambahkan `dnsseed=0` dan `dns=0` pada konfigurasi Anda. Anda kemudian harus menyediakan peer `.onion` secara manual melalui `seednode=` atau `addnode=`, karena jika tidak, penemuan node baru akan sulit dilakukan.

Untuk menghindari resolusi DNS secara terbuka, Anda dapat menambahkan `dnsseed=0` dan `dns=0` ke konfigurasi Anda. Anda kemudian perlu menyediakan peer `.onion` secara manual melalui `seednode=` atau `addnode=`, karena penemuan node baru akan sulit jika tidak.

Tentu saja, jika Anda seorang pemula, saya sarankan Anda untuk membiarkan semua pengaturan jaringan ini apa adanya untuk saat ini. Konfigurasi default seringkali sudah cukup.

### Mempool dan kebijakan relai

#### Parameter dasar

Berikut adalah parameter-parameter dasar yang dapat Anda modifikasi pada file `Bitcoin.conf` Anda terkait manajemen Mempool dan proses relai (penerusan) transaksi yang belum terkonfirmasi:

- `maxmempool=<n>`: Membatasi ukuran maksimum Mempool lokal hingga `<n>` megabita (default: `300`). Ketika batas ini tercapai, node Anda akan secara dinamis menaikkan ambang batas biaya efektifnya dan memprioritaskan transaksi yang paling tidak menguntungkan (berdasarkan fee rate, bukan nilai absolut) untuk tetap berada di bawah batas. Anda bisa membiarkan pengaturan ini pada nilai default. Meningkatkannya bisa berguna jika Anda melakukan solo mining, atau jika Anda ingin mendapatkan gambaran yang lebih akurat tentang kepadatan mempool dan meningkatkan estimasi biaya. Sebaliknya, menguranginya akan menghemat RAM dan, pada tingkat yang lebih rendah, sumber daya sistem lainnya.
- `mempoolexpiry=<n>`: Waktu penyimpanan maksimum untuk transaksi yang belum dikonfirmasi di Mempool (dalam jam, default: `336`). Setelah waktu ini, transaksi akan dihapus meskipun ruang masih tersedia.
- `persistmempool=1`: Menyimpan snapshot Mempool saat berhenti dan memuatnya kembali saat reboot (default: `1`). Hal ini mempercepat pemulihan setelah reboot, sehingga tidak perlu mempelajari ulang status melalui jaringan.
- `maxorphantx=<n>`: Jumlah maksimum transaksi _orphan_ yang dipertahankan (input tergantung dari UTXO yang belum terlihat dalam set UTXO, default: `100`). Di luar ambang batas ini, transaksi tertua akan dihapus untuk menghindari pertumbuhan cache yang tidak terkendali.
- `blocksonly=1` : Menonaktifkan penerimaan dan penerusan transaksi yang belum dikonfirmasi dari peer (kecuali dengan izin khusus). Node hanya mengunduh dan mengumumkan blok. Transaksi yang dibuat secara lokal masih dapat disiarkan (untuk menggunakan node Anda dengan perangkat lunak wallet Anda). Ini sangat mengurangi penggunaan bandwidth dan kebutuhan RAM dengan mengorbankan kegunaan relay dan tanpa pengetahuan tentang mempool.
- `minrelaytxfee=<n>`: Tingkat biaya minimum (dalam BTC/kvB) di bawahnya, transaksi tidak diterima di Mempool node dan tidak direlay ke peers (default: `0.00001` = 1 sat/kvB). Semakin tinggi nilai ini, semakin agresif node Anda menyaring transaksi berbiaya rendah.
- `mempoolfullrbf=1`: Menerima transaksi RBF bahkan tanpa sinyal RBF eksplisit dalam transaksi yang digantikan. Dengan kebijakan "*full-RBF*" ini, sebuah transaksi yang menawarkan tingkat biaya yang lebih tinggi dapat menggantikan transaksi lain dalam Mempool jika kondisi penggantian lainnya terpenuhi.

Sebagai pengingat, RBF adalah sebuah mekanisme transaksi yang memungkinkan pengirim untuk mengganti sebuah transaksi dengan transaksi yang memiliki biaya yang lebih tinggi untuk mempercepat konfirmasi. Jika transaksi dengan biaya yang terlalu rendah tetap diblokir, pengirim dapat menggunakan *Replace-by-fee* untuk meningkatkan biaya dan memprioritaskan transaksi pengganti mereka di mempool dan dengan miner.

#### Pengaturan lanjutan dan spesifik

Berikut ini adalah pengaturan lanjutan untuk Mempool dan kebijakan relai. Jika Anda seorang pemula, Anda tidak perlu memodifikasi pengaturan ini:

- `datacarrier=1` : Mengizinkan relai dan (jika mining melalui node) penyertaan transaksi yang membawa data non-finansial melalui output `OP_RETURN` (default: `1`). Menonaktifkan parameter ini sedikit mengurangi celah potensi spam data non-finansial dengan mengorbankan kompatibilitas yang lebih rendah dengan beberapa kasus penggunaan. Dalam semua kasus, Anda harus menerima `OP_RETURN` yang sudah dimining.
- `datacarriersize = <n>`: Ukuran maksimum (dalam byte) dari `OP_RETURN` yang direlay oleh node (default: `83`). Menurunkan nilai ini akan membatasi payload yang diangkut melalui `OP_RETURN`. Perhatikan bahwa batas ini akan dihapus secara default dalam versi Bitcoin core yang akan datang.
- `bytespersigop=<n>`: Parameter yang mengubah signature transaksi menjadi byte yang setara untuk evaluasi batas relai (default: `20`). Ini akan mempengaruhi penerimaan transaksi kaya akan `sigops` sesuai dengan aturan kebijakan lokal.
- `permitbaremultisig = 1`: Mengizinkan pengiriman ulang transaksi P2MS *bare-Multisig* (default: `1`). Ini adalah template skrip tertua untuk menetapkan kondisi multisignature pada UTXO (ditemukan pada tahun 2011 oleh Gavin Andresen).
- `whitelistrelay=1`: Secara otomatis memberikan izin relai kepada peer yang masuk dalam daftar putih (default: `1`). Peers ini memiliki transaksi yang diterima oleh relai meskipun node Anda tidak dalam mode relai umum.
- `whitelistforcerelay=1`: Menetapkan izin "*forcerelay*" ke peer yang masuk daftar putih dengan izin default (default: `0`). Node kemudian merelay transaksi mereka meskipun sudah ada di Mempool, sehingga melewati mekanisme anti-redundansi.
- `whitebind=<[permissions@]addr>` / `whitelist=<[permissions@]CIDR>`: Mengikat rentang Interface atau Address dan memberikan izin yang lebih halus kepada peers yang sesuai: `relay`, `forcerelay`, `Mempool` (permintaan konten Mempool), `noban`, `download`, `addr`, `bloomfilter`. Ini dapat berguna untuk memberikan perlakuan istimewa kepada rekan-rekan tepercaya (seperti gateway, LAN, dan layanan internal).
- `peerbloomfilters=1` : Mengaktifkan dukungan untuk filter Bloom (BIP37) guna melayani blok/transaksi yang difilter ke klien ringan (default: `0`). Perhatian, ini meningkatkan beban pada sumber daya Anda.
- `peerblockfilters=1` : Menyediakan filter kompak BIP157 (*Neutrino*) ke rekan (default: `0`).
- `blockreconstructionextratxn=<n>`: Jumlah transaksi tambahan yang disimpan dalam memori untuk membangun kembali blok ringkas (default: `100`). Meningkatkan keberhasilan rekonstruksi selama sinkronisasi ringkas, dengan mengorbankan sedikit memori.

Sebagai pengingat, semua aturan relai ini tidak berdampak pada validitas transaksi yang termasuk dalam blok yang valid. Aturan-aturan ini berfungsi untuk menyesuaikan kontribusi Anda pada proses relai, melindungi sumber daya Anda, dan membuat node Anda dapat diprediksi dalam lingkungan yang terbatas, tetapi tidak pernah memungkinkan Anda untuk menolak blok yang menghormati aturan konsensus.

### Wallet

Anda juga dapat mengatur cara pengelolaan wallet Anda dalam file `Bitcoin.conf`. Jika Anda tidak menggunakan Wallet secara langsung di Core, tetapi menggunakan perangkat lunak manajemen eksternal seperti Sparrow atau Liana, parameter ini tidak terlalu penting:

- `addresstype=<legacy|p2sh-segwit|bech32|bech32m>` : Menentukan format alamat yang dihasilkan oleh wallet untuk penerimaan.
- `changetype = <legacy|P2SH-SegWit|bech32|bech32m>`: Memaksakan format Exchange Address (sisa input pada satu pembayaran).
- `Wallet=<path>`: Memuat Wallet yang sudah ada saat pengaktifan (dapat diulang untuk memuat beberapa wallet).
- `walletdir=<dir>`: Direktori yang berisi wallet (default: `<datadir>/wallets` jika ada, jika tidak, `<datadir>`). Ini dapat berguna jika anda ingin menyimpan wallet pada volume khusus atau terenkripsi.
- `walletbroadcast=1`: Secara otomatis menyiarkan transaksi yang dibuat oleh wallet yang dimuat (default: `1`). Atur ke `0` jika Anda ingin mengelola siaran melalui saluran lain.
- `walletrbf=1`: Mengaktifkan keikutsertaan RBF untuk memberi sinyal RBF pada semua transaksi (default: `1`). Memungkinkan Anda untuk meningkatkan biaya di kemudian hari jika terjadi transaksi yang diblokir.
- `txconfirmtarget=<n>`: Target konfirmasi untuk transaksi (dalam jumlah blok, default: `6`). Wallet akan secara otomatis menetapkan biaya untuk transaksi yang akan dikonfirmasi dalam jumlah blok ini.
- `paytxfee=<amt>`: Tarif biaya tetap (BTC/kvB) yang diterapkan pada transaksi Wallet. Hindari secara umum: gunakan estimasi adaptif melalui `txconfirmtarget`.
- `fallbackfee=<amt>` : Tarif cadangan (BTC/kvB) yang digunakan jika estimator kekurangan data (default: `0.00`). Mengaturnya ke 0 akan menonaktifkan fallback sepenuhnya.
- `mintxfee=<amt>`: Ambang batas minimum (BTC/kvB) untuk Wallet untuk membuat transaksi (default: `0.00001`). Wallet akan menolak membuat transaksi di bawah ambang batas ini.
- `maxtxfee=<amt>`: Batas absolut pada total biaya untuk transaksi Wallet (default: `0.10` BTC). Melindungi dari biaya yang sangat tinggi yang tidak perlu yang akan menghancurkan bitcoin.
- `hindari pengeluaran parsial = 1`: Memilih UTXO berdasarkan cluster Address untuk menghindari pengeluaran sebagian.
- `spendzeroconfchange=1`: Memungkinkan UTXO Exchange yang belum dikonfirmasi untuk digunakan kembali sebagai entri dalam transaksi baru (default: `1`).
- `consolidatefeerate=<amt>`: Tingkat maksimum (BTC/kvB) di luar itu Wallet menghindari menambahkan lebih banyak input daripada yang diperlukan untuk konsolidasi. Hal ini memungkinkan konsolidasi oportunistik dengan harga rendah dan mengurangi biaya ketika biaya tinggi.
- `maxapsfee=<n>`: Anggaran untuk biaya tambahan (BTC, nilai absolut) yang disetujui oleh Wallet untuk membayar untuk mengaktifkan opsi "*hindari pengeluaran sebagian*".
- `discardfee=<amt>`: Nilai (BTC/kvB) yang menunjukkan toleransi Anda untuk membuang Exchange dengan menambahkannya ke biaya. Keluaran yang harganya lebih dari sepertiga nilainya dengan tarif ini akan dibuang.
- `keypool=<n>`: Ukuran kumpulan Address yang telah dibuat sebelumnya (default: `1000`). Nilai yang terlalu kecil akan meningkatkan risiko pemulihan yang tidak lengkap.
- `disablewallet = 1`: Memulai Bitcoin core tanpa subsistem Wallet dan menonaktifkan RPC yang terkait. Mengurangi potensi serangan dan jejak jika node hanya digunakan untuk validasi / rilis.

### Penyimpanan, pengindeksan, dan kinerja

File konfigurasi juga memungkinkan Anda untuk menyesuaikan parameter yang terkait dengan perangkat Anda. Hal ini dapat sangat relevan jika Anda memiliki sumber daya yang terbatas, atau, sebaliknya, kapasitas yang tersedia dalam jumlah besar:

- `datadir = <dir>`: Mengatur direktori data utama Bitcoin core.
- `blocksdir=<dir>`: Memisahkan lokasi file blok (`blocks/blk*.dat` dan `blocks/rev*.dat`) dari `datadir`. Hal ini dapat berguna untuk menempatkan arsip blok pada volume yang berbeda, sambil menjaga database (`chainstate/`) pada media yang lebih cepat, misalnya.
- `dbcache=<n>`: Mengalokasikan `<n>` MiB ke cache basis data (*LevelDB*) yang digunakan oleh indeks blok dan `chainstate` (default: `450`). Semakin tinggi nilainya, semakin cepat IBD dan validasi saat ini, dengan membuat konsumsi RAM yang lebih tinggi.
- `pangkas=<n>`: Mengaktifkan pemangkasan file blok dan menetapkan target ruang disk dalam MiB (default: `0` = dinonaktifkan; `1` = pemangkasan manual melalui RPC; `> = 550` = pemangkasan otomatis di bawah target). Tidak kompatibel dengan `txindex=1`. Node tetap menjadi node yang tervalidasi sepenuhnya, tetapi tidak dapat lagi menyediakan riwayat lama. Opsi ini sangat berguna jika ruang disk Anda terbatas, misalnya, saat memasang node di komputer rumah Anda.
- `txindex=1` : Membangun dan memelihara indeks global dari transaksi yang dikonfirmasi. Penting untuk beberapa permintaan (`getrawtransaction` di luar wallet) dan untuk keperluan eksplorasi, tetapi secara signifikan meningkatkan penggunaan disk. Tidak kompatibel dengan mode pruned.
- `assumevalid=<hex>`: Menunjukkan blok yang diasumsikan valid, sehingga Anda dapat melewatkan pemeriksaan skrip untuk nenek moyangnya (setel `0` untuk memeriksa semuanya). Lihat bab sebelumnya untuk informasi lebih lanjut.
- `reindex=1`: Merekonstruksi indeks blok dan status (`chainstate`) dari file `blk*.dat` pada disk. Juga membangun kembali indeks aktif opsional. Ini adalah operasi yang memakan waktu untuk digunakan untuk memperbaiki basis data yang rusak atau mengaktifkan/menonaktifkan indeks yang berat.
- `reindex-chainstate=1`: Membangun ulang hanya `chainstate` dari indeks blok saat ini. Lebih disukai ketika file blok dalam kondisi baik.
- `blockfilterindex=<type>`: Mempertahankan indeks filter blok ringkas (misalnya, `basic`) yang digunakan oleh thin client (BIP157/158) dan beberapa RPC. Dinonaktifkan secara default (`0`). Memakan ruang disk tambahan dan waktu pengindeksan.
- `coinstatsindex = 1`: Mempertahankan indeks statistik set UTXO yang dioperasikan oleh panggilan `getxoutsetinfo`. Berguna untuk audit dan metrik, sehingga tidak perlu melakukan penghitungan ulang yang mahal. Dinonaktifkan secara default.
- `loadblock = <file>`: Mengimpor blok saat pengaktifan dari file `blk*.dat` eksternal. Digunakan untuk memuat riwayat dari sumber offline (salinan lokal, media eksternal) untuk mempercepat inisialisasi.
- `par=<n>`: Mengatur jumlah thread verifikasi skrip (dari `-10` hingga `15`, `0` = otomatis, `<0` = mengosongkan jumlah core). Memungkinkan Anda menyesuaikan paralelisme CPU selama validasi. Mode otomatis cocok untuk sebagian besar kasus.
- `debuglogfile=<file>`: Menentukan lokasi log `debug.log`.
- `shrinkdebugfile=1`: Mengurangi ukuran `debug.log` saat pengaktifan (default: `1` saat `-debug` tidak aktif).
- `settings=<file>`: Jalur ke file pengaturan dinamis `settings.json`.

### Akses RPC dan keamanan operasional

Terakhir, file `Bitcoin.conf` juga memungkinkan Anda untuk mengkonfigurasi parameter akses untuk node Anda. Berhati-hatilah dengan pengaturan ini, terutama jika Anda baru memulai: hindari mengubahnya tanpa pemahaman mendalam tentang implikasinya, karena ini dapat menimbulkan celah keamanan.

- `server=1`: Mengaktifkan server JSON-RPC. Penting jika Anda mengendalikan `bitcoind` melalui `bitcoin-cli` atau aplikasi pihak ketiga. Nonaktifkan (`0`) pada node validasi murni yang tidak mengekspos API apa pun, atau sudah menggunakan server Electrum.
- `rpcbind=<addr>[:port]`: Server RPC mendengarkan Address/port. Secara default, mendengarkan hanya dilakukan secara lokal (`127.0.0.1` dan `::1`). Parameter ini diabaikan jika `rpcallowip` juga tidak didefinisikan. Gunakan untuk secara eksplisit membatasi Interface.
- `rpcport=<port>`: Port RPC (default: `8332` pada Mainnet, `18332` pada Testnet, `38332` pada bookmark, `18443` pada regtest).
- `rpcallowip=<ip|cidr>`: Mengizinkan klien RPC dari IP atau subnet tertentu (dapat diulang). Gunakan bersama dengan `rpcbind` untuk mengekspos API hanya ke segmen tepercaya (LAN/VPN).
- `rpcauth=<USERNAME>:<SALT>$<Hash>`: Metode autentikasi RPC yang direkomendasikan (kata sandi ter-hash). Memungkinkan beberapa entri dan menghindari penyimpanan rahasia dalam teks yang jelas.
- `rpccookiefile=<path>`: Jalur ke cookie autentikasi (default: file `.cookie` di bawah `datadir/`). Ini digunakan untuk akses lokal oleh pengguna yang sama tanpa mengelola kata sandi yang tetap. Sebagai contoh, Anda dapat menggunakannya untuk menghubungkan Liana Wallet ke Bitcoin core pada mesin yang sama.
- `rpcuser=<user>` / `rpcpassword=<pw>`: Otentikasi RPC klasik dengan kata sandi teks biasa. Hindari penggunaan ini sebagai pengganti `rpcauth` atau cookie.
- `rpcthreads=<n>`: Jumlah thread untuk melayani panggilan RPC (default: `4`). Tingkatkan jika Anda memiliki puncak panggilan yang tinggi pada sisi pemantauan/alat eksternal.
- `rpcwhitelist=<USERNAME>:<rpc1>,<rpc2>,...`: Whitelist API yang diotorisasi. Mengurangi potensi serangan dengan membatasi metode yang dapat diakses.
- `rpcwhitelistdefault=1|0`: Perilaku Whitelist default: jika diaktifkan dan Whitelist digunakan, panggilan yang tidak terdaftar akan ditolak. Ini juga dapat memaksa set default kosong (tidak ada panggilan yang diizinkan) selama tidak ada yang secara eksplisit terdaftar.
- `rest=1`: Mengaktifkan REST API publik (dinonaktifkan secara default). Untuk diekspos hanya pada jaringan tepercaya (peringatan yang sama seperti pada JSON-RPC).
- `conf=<file>`: Menentukan, pada baris perintah saja, file konfigurasi read-only. Berguna untuk membekukan profil eksekusi (tidak dapat diubah) pada sisi operasi.
- `includeconf=<file>`: Memuat file konfigurasi tambahan (jalur relatif ke `datadir/`). Memungkinkan pemisahan peran: basis umum + kelebihan beban lokal yang sensitif.
- `daemon=1` / `daemonwait=1`: Memulai `bitcoind` di background dan, dengan `daemonwait`, menunggu inisialisasi selesai sebelum menyerahkannya. Hal ini memudahkan integrasi dengan supervisor (systemd, runit).
- `pid=<file>`: Lokasi file PID.
- `sandbox=<log-and-abort|abort>`: Mengaktifkan sandboxing syscall eksperimental: hanya syscall yang diharapkan yang diizinkan.
- `startupnotify = <cmd>` / `shutdownnotify = <cmd>`: Menjalankan perintah saat pengaktifan atau penonaktifan.
- `alertnotify = <cmd>`: Memicu perintah saat menerima peringatan.
- `blocknotify = <cmd>`: Menjalankan perintah untuk setiap blok baru.
- `debug=<kategori>|1` / `debugexclude=<kategori>`: Mengaktifkan/menonaktifkan kategori log yang terperinci (misalnya `net`, `Mempool`, `RPC`, `validasi`...).
- `logips=1`: Mencatat alamat IP.
- `logsourcelocations=1` / `logthreadnames=1` / `logtimestamps=1`: Menambahkan lokasi sumber, nama utas, dan stempel waktu yang tepat ke log.
- `printtoconsole=1`: Mengirimkan jejak/debug ke konsol (*stdout*).
- `help-debug=1`: Menampilkan bantuan opsi debug dan berhenti.
- `uacomment=<cmt>`: Menambahkan komentar ke Agen-Pengguna P2P.

Kita sekarang telah selesai membuat daftar sebagian besar parameter konfigurasi. File `Bitcoin.conf` ini dengan demikian merupakan dashboard sebenarnya dari node Anda: ia mendefinisikan konfigurasi jaringan, manajemen Mempool, penggunaan disk dan memori, pengindeksan, dan administrasi umum. Jika Anda ingin mempelajari lebih lanjut tentang file ini dan membuat satu yang disesuaikan dengan kebutuhan Anda, saya sarankan menggunakan [generator Jameson Lopp](https://jlopp.github.io/Bitcoin-core-config-generator/).

Kita telah sampai pada kesimpulan dari kursus BTC 202 ini, yang akan memungkinkan Anda tidak hanya untuk memahami dasar-dasar cara kerja node dan bagaimana mereka berinteraksi dalam sistem, tetapi juga untuk menyiapkan node Anda sendiri. Anda sekarang adalah seorang Bitcoiner yang berdaulat, dengan wallet self-custody Anda sendiri, menyiarkan transaksi Anda melalui node Anda sendiri. Selamat!

Kita sekarang telah selesai membuat daftar sebagian besar parameter konfigurasi. File `Bitcoin.conf` ini merupakan dashboard yang sebenarnya dari node Anda: mendefinisikan konfigurasi jaringan, manajemen Mempool, penggunaan disk dan memori, pengindeksan, dan administrasi umum. Jika anda ingin mempelajari lebih lanjut tentang berkas ini dan membuat berkas yang sesuai dengan kebutuhan anda, saya sarankan untuk menggunakan [generator Jameson Lopp](https://jlopp.github.io/Bitcoin-core-config-generator/).



Kita telah mencapai kesimpulan dari kursus BTC 202 ini, yang akan memungkinkan Anda untuk tidak hanya memahami dasar-dasar cara kerja node dan bagaimana mereka berinteraksi dalam sistem, tetapi juga untuk membuat node Anda sendiri. Sekarang Anda adalah seorang Bitcoiner yang berdaulat, dengan Wallet milik Anda sendiri, yang menyiarkan transaksi Anda melalui node Anda sendiri. Selamat!



Sekarang Anda dapat melanjutkan ke bagian akhir kursus, di mana Anda akan dapat mengevaluasi BTC 202, kemudian mengambil ijazah Anda untuk memeriksa apakah Anda telah menguasai semua konsep yang dibahas.



Kini tersedia beberapa jalur bagi Anda. Langkah logis berikutnya adalah menyiapkan node Lightning Anda sendiri, agar sepenuhnya mandiri dalam transaksi off-chain Anda. Inilah tepatnya topik dari kursus lain di Plan ₿ Academy:



https://planb.academy/courses/593e483e-1785-4e83-aa7e-32b99056844c

Saya juga mengundang Anda untuk mengenal pelatihan BTC 204, yang akan memungkinkan Anda memahami dan menguasai prinsip-prinsip perlindungan privasi dalam penggunaan Bitcoin:

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

# Bagian akhir

<partId>679169f5-b990-47e1-9a00-45098ba8096b</partId>

## Ulasan & Peringkat

<chapterId>c18f672d-1074-427e-9505-eecd7ae43e71</chapterId>

<isCourseReview>true</isCourseReview>

## Ujian akhir

<chapterId>a4c97701-996c-4cc5-81fa-37d2dc4ee856</chapterId>

<isCourseExam>true</isCourseExam>

## Kesimpulan

<chapterId>28c5cf1f-7b9c-4b68-8b8f-eee109629764</chapterId>

<isCourseConclusion>true</isCourseConclusion>
