---
name: Protokol RGB, dari teori ke praktik
goal: Memperoleh keterampilan yang diperlukan untuk memahami dan menggunakan RGB
objectives: 

  - Memahami konsep dasar protokol RGB
  - Menguasai prinsip-prinsip validasi sisi klien dan komitmen Bitcoin
  - Pelajari cara membuat, mengelola, dan mentransfer kontrak RGB
  - Cara mengoperasikan simpul Lightning yang kompatibel dengan RGB

---
# Menemukan protokol RGB

Selami dunia RGB, sebuah protokol yang dirancang untuk mengimplementasikan dan menegakkan hak-hak digital, dalam bentuk kontrak dan aset, berdasarkan aturan konsensus dan operasi blockchain Bitcoin. Kursus pelatihan komprehensif ini akan memandu Anda melalui dasar-dasar teknis dan praktis RGB, mulai dari konsep "Validasi Sisi Klien" dan "Segel Sekali Pakai", hingga implementasi kontrak pintar tingkat lanjut.

Melalui program terstruktur, langkah demi langkah, Anda akan menemukan mekanisme validasi sisi klien, komitmen deterministik pada Bitcoin, dan pola interaksi antar pengguna. Pelajari cara membuat, mengelola, dan mentransfer token RGB di Bitcoin atau Lightning Network.

Apakah Anda seorang pengembang, penggemar Bitcoin, atau hanya ingin tahu lebih banyak tentang teknologi ini, kursus ini akan memberi Anda alat dan pengetahuan yang Anda butuhkan untuk menguasai RGB dan membangun solusi inovatif dengan Bitcoin.

Kursus ini didasarkan pada seminar langsung yang diselenggarakan oleh Fulgur'Ventures dan diajarkan oleh tiga guru terkenal dan pakar RGB.

+++
# Pendahuluan

<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>

## Presentasi kursus

<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>

Halo semuanya, dan selamat datang di kursus pelatihan yang didedikasikan untuk RGB, sebuah sistem kontrak pintar yang divalidasi di sisi klien yang berjalan di Bitcoin dan Lightning Network. Struktur kursus ini dirancang untuk memungkinkan eksplorasi mendalam tentang subjek yang kompleks ini. Berikut adalah bagaimana kursus ini diatur:

**Bagian 1: Teori

Bagian pertama didedikasikan untuk konsep teoritis yang diperlukan untuk memahami dasar-dasar validasi sisi klien dan RGB. Seperti yang akan Anda temukan dalam kursus ini, RGB memperkenalkan sejumlah konsep teknis yang biasanya tidak terlihat dalam Bitcoin. Di bagian ini, Anda juga akan menemukan glosarium yang memberikan definisi untuk semua istilah khusus untuk protokol RGB.

**Bagian 2: Latihan

Bagian kedua akan berfokus pada penerapan konsep teoretis yang terlihat di bagian 1. Kita akan belajar cara membuat dan memanipulasi kontrak RGB. Kita juga akan melihat cara memprogram dengan alat-alat ini. Dua bagian pertama ini disajikan oleh Maxim Orlovsky.

**Bagian 3: Aplikasi

Bagian terakhir dipandu oleh pembicara lain yang menyajikan aplikasi berbasis RGB yang konkret, untuk menyoroti kasus penggunaan dalam kehidupan nyata.

---
Kursus pelatihan ini awalnya berkembang dari bootcamp pengembangan lanjutan selama dua minggu di Viareggio, Tuscany, yang diselenggarakan oleh [Fulgur'Ventures](https://fulgur.ventures/). Minggu pertama, yang berfokus pada Rust dan SDK, dapat ditemukan di kursus lainnya:

https://planb.network/courses/lnp402
Dalam kursus ini, kita akan fokus pada minggu kedua bootcamp, yang berfokus pada RGB.

**Minggu 1 - LNP402:**

![RGB-Bitcoin](assets/fr/001.webp)

**Minggu 2 - Pelatihan saat ini CSV402:**

![RGB-Bitcoin](assets/fr/002.webp)

Terima kasih banyak kepada penyelenggara kursus langsung ini dan kepada 3 pengajar yang ikut serta:


- Maxim Orlovsky: *Ex Tenebrae sententia sapiens dominabitur astris. Cypher, AI, robotika, transhumanisme. Pencipta RGB, Prime, Radiant dan lnp_bp, mycitadel_io & cyphernet_io*;
- Hunter Trujilo: *Pengembang, Karat, Bitcoin, Petir, RGB*;
- Federico Tenga: *Saya melakukan bagian saya untuk mengubah dunia menjadi distopia cypherpunk. Saat ini sedang mengerjakan RGB di Bitfinex*.

Versi tertulis dari kursus pelatihan ini disusun dengan menggunakan 2 sumber utama:


- Video seminar Maxim Orlovsky, Hunter Trujilo dan Frederico Tenga di Lightning Bootcamp ;
- Dokumentasi RGB, yang produksinya disponsori oleh [Bitfinex](https://www.bitfinex.com/).

# RGB dalam teori

<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>

## Pengenalan konsep komputasi terdistribusi

<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>

![video](https://youtu.be/AF2XbifPGXM)

RGB adalah sebuah protokol yang didesain untuk menerapkan dan menegakkan hak-hak digital (dalam bentuk kontrak dan aset) dengan cara yang terukur dan rahasia, berdasarkan aturan konsensus dan operasi blockchain Bitcoin. Tujuan dari bab pertama ini adalah untuk menyajikan konsep dasar dan terminologi seputar protokol RGB, menyoroti secara khusus hubungan eratnya dengan konsep komputasi terdistribusi dasar seperti Validasi Sisi Klien dan Segel Sekali Pakai.

Pada bab ini, kita akan membahas dasar-dasar **sistem konsensus terdistribusi** dan melihat bagaimana RGB cocok dengan keluarga teknologi ini. Kami juga akan memperkenalkan prinsip-prinsip utama yang membantu kita memahami mengapa RGB bertujuan untuk dapat diperluas dan tidak bergantung pada mekanisme konsensus Bitcoin, namun tetap bergantung pada mekanisme konsensus Bitcoin ketika diperlukan.

### Pendahuluan

Komputasi terdistribusi, sebuah cabang ilmu komputer yang spesifik, mempelajari protokol yang digunakan untuk mengedarkan dan memproses informasi pada jaringan node. Bersama-sama, node-node ini dan aturan protokol membentuk apa yang dikenal sebagai sistem terdistribusi. Di antara sifat-sifat penting yang mencirikan sistem tersebut adalah :


- Kemampuan verifikasi dan validasi independen **kemampuan verifikasi dan validasi** data tertentu oleh setiap node;
- Kemungkinan bagi node untuk membangun (tergantung pada protokol) tampilan informasi yang lengkap atau sebagian. Tampilan ini adalah **state** dari sistem terdistribusi;
- Urutan kronologis operasi, sehingga data dapat dicap waktu dengan andal dan ada konsensus tentang urutan kejadian (urutan status).

Secara khusus, pengertian **konsensus** dalam sistem terdistribusi mencakup dua aspek:


- Pengakuan keabsahan** perubahan status (sesuai dengan aturan protokol);
- Kesepakatan mengenai urutan perubahan status ini, yang membuatnya tidak mungkin untuk menulis ulang atau membalikkan operasi yang telah divalidasi secara a posteriori (hal ini juga dikenal dalam Bitcoin sebagai "proteksi pembelanjaan ganda").

Implementasi mekanisme konsensus terdistribusi yang fungsional dan bebas izin pertama kali diperkenalkan oleh Satoshi Nakamoto dengan Bitcoin, berkat penggunaan gabungan struktur data blockchain dan algoritma Proof-of-Work (PoW). Dalam sistem ini, kredibilitas riwayat blok bergantung pada daya komputasi yang dicurahkan oleh node (penambang). Oleh karena itu, Bitcoin merupakan contoh utama dan bersejarah dari sistem konsensus terdistribusi yang terbuka untuk semua orang (*permissionless*).

Dalam dunia blockchain dan komputasi terdistribusi, kita dapat membedakan dua paradigma mendasar: ***blockchain*** dalam pengertian tradisional, dan **state channels***, contoh terbaiknya adalah Lightning Network. Blockchain didefinisikan sebagai daftar peristiwa yang diurutkan secara kronologis, direplikasi oleh konsensus dalam jaringan terbuka dan bebas izin. Di sisi lain, state channel adalah saluran peer-to-peer yang memungkinkan dua (atau lebih) peserta untuk mempertahankan state yang diperbarui di luar rantai, menggunakan blockchain hanya ketika membuka dan menutup saluran ini.

Dalam konteks Bitcoin, Anda tentu sudah tidak asing lagi dengan prinsip-prinsip penambangan, desentralisasi, dan finalitas transaksi pada blockchain, serta cara kerja saluran pembayaran. Dengan RGB, kami memperkenalkan paradigma baru yang disebut **Validasi Sisi Klien**, yang tidak seperti blockchain atau Lightning, terdiri dari penyimpanan dan validasi secara lokal (sisi klien) untuk memvalidasi transisi status kontrak pintar. Ini juga berbeda dari teknik "DeFi" lainnya (_rollups_, _plasma_, _ARK_, dll.), karena Validasi Sisi Klien bergantung pada blockchain untuk mencegah pengeluaran ganda dan memiliki sistem stempel waktu, sambil tetap menyimpan daftar status dan transisi off-chain, hanya dengan peserta yang bersangkutan.

![RGB-Bitcoin](assets/fr/003.webp)

Selanjutnya, kami juga akan memperkenalkan istilah penting: gagasan "**stash**", yang mengacu pada sekumpulan data sisi klien yang diperlukan untuk mempertahankan status kontrak, karena data ini tidak direplikasi secara global di seluruh jaringan. Terakhir, kita akan melihat alasan di balik RGB, sebuah protokol yang memanfaatkan Validasi Sisi Klien, dan mengapa protokol ini melengkapi pendekatan yang sudah ada (blockchain dan state channel).

### Trilema dalam komputasi terdistribusi

Untuk memahami bagaimana Validasi Sisi Klien dan RGB mengatasi masalah yang tidak dapat diselesaikan oleh blockchain dan Lightning, mari kita temukan 3 "trilema" utama dalam komputasi terdistribusi:


- Skalabilitas, Desentralisasi, Privasi**;
- Teorema CAP** (Konsistensi, Ketersediaan, Toleransi Partisi);
- Trilema CIA** (Kerahasiaan, Integritas, Ketersediaan).

#### 1. Skalabilitas, desentralisasi, dan kerahasiaan


- Blockchain (Bitcoin)**

Blockchain sangat terdesentralisasi, tetapi tidak terlalu terukur. Terlebih lagi, karena semuanya berada dalam daftar publik global, kerahasiaan menjadi terbatas. Kita dapat mencoba meningkatkan kerahasiaan dengan teknologi tanpa pengetahuan (transaksi rahasia, skema mimblewimble, dll.), tetapi rantai publik tidak dapat menyembunyikan grafik transaksi.


- Saluran petir/Saluran negara**

Saluran negara (seperti halnya Lightning Network) lebih terukur dan lebih privat daripada blockchain, karena transaksi terjadi di luar rantai. Akan tetapi, kewajiban untuk mengumumkan elemen-elemen tertentu (transaksi pendanaan, topologi jaringan) dan pemantauan lalu lintas jaringan dapat membahayakan kerahasiaan. Desentralisasi juga menderita: perutean bersifat padat modal, dan node utama dapat menjadi titik sentralisasi. Inilah fenomena yang mulai kita lihat di Lightning.


- Validasi Sisi Klien (RGB)**

Paradigma baru ini bahkan lebih terukur dan lebih rahasia, karena kita tidak hanya dapat mengintegrasikan teknik proof-of-knowledge tanpa pengungkapan, tetapi juga tidak ada grafik transaksi global, karena tidak ada yang memegang seluruh register. Di sisi lain, ini juga menyiratkan kompromi tertentu pada desentralisasi: penerbit kontrak pintar dapat memiliki peran sentral (seperti "penyebar kontrak" di Ethereum). Akan tetapi, tidak seperti blockchain, dengan Validasi Sisi Klien, Anda hanya menyimpan dan memvalidasi kontrak yang Anda minati, yang meningkatkan skalabilitas dengan menghindari kebutuhan untuk mengunduh dan memverifikasi semua status yang ada.

![RGB-Bitcoin](assets/fr/004.webp)

#### 2. Teorema CAP (Konsistensi, Ketersediaan, Toleransi partisi)

Teorema CAP menekankan bahwa sistem terdistribusi tidak mungkin memenuhi konsistensi (*Konsistensi*), ketersediaan (*Ketersediaan*), dan toleransi partisi (*Toleransi partisi*) secara bersamaan.


- Blockchain**

Blockchain mendukung konsistensi dan ketersediaan, tetapi tidak bekerja dengan baik dengan partisi jaringan: jika Anda tidak dapat melihat sebuah blok, Anda tidak dapat bertindak dan memiliki pandangan yang sama dengan seluruh jaringan.


- Petir** (dalam bahasa Prancis)

Sebuah sistem state channel memiliki ketersediaan dan toleransi partisi (karena dua node dapat tetap terhubung satu sama lain walaupun jaringan terfragmentasi), tetapi konsistensi secara keseluruhan bergantung pada pembukaan dan penutupan channel pada blockchain.


- Validasi Sisi Klien (RGB)**

Sistem seperti RGB menawarkan konsistensi (setiap peserta memvalidasi datanya secara lokal, tanpa ambiguitas) dan toleransi partisi (Anda menyimpan data Anda secara mandiri), tetapi tidak menjamin ketersediaan global (setiap orang harus memastikan bahwa mereka memiliki bagian yang relevan dari sejarah, dan beberapa peserta mungkin tidak mempublikasikan apa pun atau berhenti berbagi informasi tertentu).

![RGB-Bitcoin](assets/fr/005.webp)

#### 3. Trilema CIA (Kerahasiaan, Integritas, Ketersediaan)

Trilema ini mengingatkan kita bahwa kerahasiaan, integritas, dan ketersediaan tidak dapat dioptimalkan secara bersamaan. Blockchain, Lightning, dan Validasi Sisi Klien berada pada posisi yang berbeda dalam keseimbangan ini. Idenya adalah bahwa tidak ada satu sistem pun yang dapat menyediakan segalanya; perlu untuk menggabungkan beberapa pendekatan (time-stamping blockchain, pendekatan sinkron Lightning, dan validasi lokal dengan RGB) untuk mendapatkan paket yang koheren yang menawarkan jaminan yang baik di setiap dimensi.

![RGB-Bitcoin](assets/fr/006.webp)

### Peran blockchain dan gagasan sharding

Blockchain (dalam hal ini, Bitcoin) berfungsi terutama sebagai mekanisme _waktu-stempel_ dan perlindungan terhadap pengeluaran ganda. Alih-alih memasukkan data lengkap dari kontrak pintar atau sistem terdesentralisasi, kami hanya menyertakan **komitmen kriptografi** (_commitments_) untuk transaksi (dalam arti Validasi Sisi Klien, yang akan kami sebut "transisi negara"). Dengan demikian :


- Kami membebaskan blockchain dari sejumlah besar data dan logika;
- Setiap pengguna hanya menyimpan riwayat yang diperlukan untuk bagian kontraknya sendiri ("*shard*" miliknya), daripada mereplikasi status global.

Sharding adalah sebuah konsep yang berasal dari database terdistribusi (misalnya MySQL untuk jejaring sosial seperti Facebook atau Twitter). Untuk mengatasi masalah volume data dan latensi sinkronisasi, basis data disegmentasi ke dalam _shard_ (Amerika Serikat, Eropa, Asia, dll.). Setiap segmen konsisten secara lokal dan hanya sebagian yang disinkronkan dengan yang lain.

Untuk smart contract tipe RGB, kami melakukan shard sesuai dengan kontrak itu sendiri. Setiap kontrak adalah _shard_ independen. Misalnya, jika Anda hanya memiliki token USDT, Anda tidak perlu menyimpan atau memvalidasi seluruh riwayat token lain seperti USDC. Pada Bitcoin, blockchain tidak melakukan _sharding_: Anda memiliki satu set global UTXO. Dengan Validasi Sisi Klien, setiap peserta hanya menyimpan data kontrak yang dipegang atau digunakannya.

Oleh karena itu, kita dapat membayangkan ekosistem sebagai berikut:


- Blockchain (Bitcoin)** sebagai fondasi yang memastikan replikasi lengkap dari daftar minimal dan berfungsi sebagai lapisan pencatat waktu;
- Lightning Network** untuk transaksi yang cepat dan rahasia, masih berdasarkan pada keamanan dan penyelesaian akhir blockchain Bitcoin;
- RGB dan Validasi Sisi Klien** untuk menambahkan logika smart contract yang lebih kompleks, tanpa mengacaukan blockchain atau kehilangan kerahasiaan.

![RGB-Bitcoin](assets/fr/007.webp)

Ketiga elemen ini membentuk satu kesatuan segitiga, bukan tumpukan linear "lapisan 2", "lapisan 3", dan seterusnya. Lightning dapat terhubung langsung ke Bitcoin, atau dikaitkan dengan transaksi Bitcoin yang menggunakan data RGB. Demikian pula, penggunaan "BiFi" (keuangan pada Bitcoin) dapat dibuat dengan blockchain, dengan Lightning dan dengan RGB sesuai dengan kebutuhan kerahasiaan, skalabilitas, atau logika kontrak.

![RGB-Bitcoin](assets/fr/008.webp)

### Gagasan tentang transisi negara bagian

Dalam sistem terdistribusi, tujuan dari mekanisme validasi adalah untuk dapat **menentukan validitas dan urutan kronologis dari perubahan status**. Tujuannya adalah untuk memverifikasi bahwa aturan protokol telah dipatuhi, dan untuk membuktikan bahwa perubahan status ini mengikuti satu sama lain dalam urutan yang pasti dan tidak dapat diganggu gugat.

Untuk memahami bagaimana validasi ini bekerja dalam konteks **Bitcoin** dan, secara umum, untuk memahami filosofi di balik Validasi Sisi Klien, pertama-tama mari kita lihat kembali mekanisme blockchain Bitcoin, sebelum melihat bagaimana Validasi Sisi Klien berbeda dengan mekanisme tersebut dan pengoptimalan apa yang dimungkinkan.

![RGB-Bitcoin](assets/fr/009.webp)

Dalam kasus blockchain Bitcoin, validasi transaksi didasarkan pada sebuah aturan sederhana:


- Semua node jaringan mengunduh setiap blok dan transaksi;
- Mereka memvalidasi transaksi-transaksi ini untuk memverifikasi evolusi yang benar dari set UTXO (semua output yang tidak terpakai);
- Mereka menyimpan data ini (dalam bentuk blok) sehingga riwayat dapat diputar ulang jika perlu.

![RGB-Bitcoin](assets/fr/010.webp)

Namun demikian, model ini memiliki dua kelemahan utama:


- Skalabilitas**: karena setiap node harus memproses, memverifikasi, dan mengarsipkan transaksi setiap orang, ada batasan yang jelas untuk kapasitas transaksi, khususnya terkait dengan ukuran blok maksimum (rata-rata 1 MB dalam waktu 10 menit untuk Bitcoin, tidak termasuk cookie);
- Privasi**: semuanya disiarkan dan disimpan secara publik (jumlah, alamat tujuan, dll.), yang membatasi kerahasiaan pertukaran.

![RGB-Bitcoin](assets/fr/012.webp)

Pada praktiknya, model ini berfungsi untuk Bitcoin sebagai lapisan dasar (Lapisan 1), tetapi mungkin tidak mencukupi untuk penggunaan yang lebih kompleks yang secara bersamaan membutuhkan throughput transaksi yang tinggi dan tingkat kerahasiaan tertentu.

Validasi sisi klien didasarkan pada ide yang berlawanan: daripada mengharuskan seluruh jaringan untuk memvalidasi dan menyimpan semua transaksi, setiap peserta (klien) akan memvalidasi hanya bagian dari riwayat yang menyangkut dirinya:


- Ketika seseorang menerima sebuah aset (atau properti digital lainnya), mereka hanya perlu mengetahui dan memverifikasi rantai operasi (transisi status) yang mengarah ke aset tersebut dan membuktikan keabsahannya;
- Urutan operasi ini, dari ***Genesis*** (edisi awal) hingga transaksi terbaru, membentuk graf berarah siklik (DAG) atau pecahan, yaitu sebagian kecil dari keseluruhan riwayat.

![RGB-Bitcoin](assets/fr/013.webp)

Pada saat yang sama, agar seluruh jaringan (atau lebih tepatnya, lapisan yang mendasari, seperti Bitcoin) dapat mengunci keadaan akhir tanpa melihat rincian data ini, Validasi Sisi Klien bergantung pada gagasan ***komitmen***.

Sebuah *commitment* adalah sebuah komitmen kriptografi, biasanya berupa _hash_ (SHA-256 misalnya) yang dimasukkan ke dalam sebuah transaksi Bitcoin, yang membuktikan bahwa data pribadi telah disertakan, tanpa mengungkapkan data ini.

Berkat _komitmen_ ini, kami dapat membuktikannya:


- Keberadaan informasi (karena informasi tersebut berkomitmen pada hash);
- Keaslian informasi ini (karena informasi ini berlabuh dan dicap waktu di blockchain, dengan tanggal dan urutan blok).

Namun demikian, isi persisnya tidak diungkapkan, sehingga menjaga kerahasiaannya.

Secara konkret, berikut ini cara kerja transisi status RGB:


- Anda menyiapkan transisi status baru (misalnya transfer token RGB);
- Anda menghasilkan komitmen kriptografi untuk transisi ini dan memasukkannya ke dalam transaksi Bitcoin (komitmen ini disebut "*anchors*" dalam protokol RGB);
- Mitra pengimbang (penerima) mengambil riwayat sisi pelanggan yang terkait dengan aset ini dan memvalidasi konsistensi ujung ke ujung, mulai dari asal mula smart contract hingga transisi yang Anda kirimkan ke aset tersebut.

![RGB-Bitcoin](assets/fr/014.webp)

Validasi dari sisi klien menawarkan dua manfaat utama:


- Skalabilitas:**

Komitmen (*commitments*) yang disertakan dalam blockchain berukuran kecil (sekitar beberapa puluh byte). Hal ini memastikan bahwa ruang blok tidak jenuh, karena hanya hash yang perlu disertakan. Hal ini juga memungkinkan protokol off-chain untuk berkembang, karena setiap pengguna hanya perlu menyimpan fragmen riwayatnya (_stash_).


- Privasi :**

Transaksi itu sendiri (yaitu konten detailnya) tidak dipublikasikan secara on-chain. Hanya sidik jarinya (*hash*) yang dipublikasikan. Dengan demikian, jumlah, alamat, dan logika kontrak tetap bersifat pribadi, dan penerima dapat memverifikasi, secara lokal, keabsahan pecahannya dengan memeriksa semua transisi sebelumnya. Tidak ada alasan bagi penerima untuk mempublikasikan data ini, kecuali jika terjadi perselisihan atau jika diperlukan bukti.

Dalam sebuah sistem seperti RGB, beberapa transisi status dari kontrak yang berbeda (atau aset yang berbeda) dapat digabungkan ke dalam satu transaksi Bitcoin melalui satu _commitment_. Mekanisme ini membentuk sebuah hubungan deterministik dan tertera waktu antara transaksi on-chain dan data off-chain (transisi yang divalidasi dari sisi klien), dan memungkinkan beberapa pecahan untuk secara bersamaan direkam dalam satu titik jangkar, sehingga mengurangi biaya dan jejak on-chain.

Pada praktiknya, ketika transaksi Bitcoin ini divalidasi, transaksi ini secara permanen "mengunci" keadaan kontrak yang mendasarinya, karena tidak mungkin untuk mengubah hash yang telah tertulis dalam blockchain.

![RGB-Bitcoin](assets/fr/015.webp)

### Konsep simpanan

Stash adalah sekumpulan data sisi klien yang harus disimpan oleh peserta untuk menjaga integritas dan riwayat kontrak pintar RGB. Tidak seperti saluran Lightning, di mana status tertentu dapat direkonstruksi secara lokal dari informasi yang dibagikan, simpanan kontrak RGB tidak direplikasi di tempat lain: jika Anda kehilangannya, tidak ada yang bisa mengembalikannya kepada Anda, karena Anda bertanggung jawab atas bagian sejarah Anda. Inilah sebabnya mengapa Anda perlu mengadopsi sistem dengan prosedur pencadangan yang dapat diandalkan di RGB.

![RGB-Bitcoin](assets/fr/016.webp)

### Segel sekali pakai: asal-usul dan pengoperasian

Ketika menerima aset seperti mata uang, dua jaminan sangat penting:


- Keaslian barang yang diterima;
- Keunikan barang yang diterima, untuk menghindari pengeluaran ganda.

Untuk aset fisik, seperti uang kertas, keberadaan fisik sudah cukup untuk membuktikan bahwa aset tersebut belum diduplikasi. Namun, di dunia digital, di mana aset murni berupa informasi, verifikasi ini lebih kompleks, karena informasi dapat dengan mudah berkembang biak dan diduplikasi.

Seperti yang telah kita lihat sebelumnya, pengungkapan pengirim mengenai sejarah transisi status memungkinkan kita untuk memastikan keaslian token RGB. Dengan memiliki akses ke semua transaksi sejak transaksi awal, kita dapat memastikan keaslian token tersebut. Prinsip ini mirip dengan Bitcoin, di mana sejarah koin dapat ditelusuri kembali ke transaksi coinbase asli untuk memverifikasi keabsahannya. Namun, tidak seperti Bitcoin, riwayat transisi status dalam RGB bersifat pribadi dan disimpan di sisi klien.

Untuk mencegah penggunaan ganda token RGB, kami menggunakan mekanisme yang disebut "**Single-use Seal**". Sistem ini memastikan bahwa setiap token, setelah digunakan, tidak dapat digunakan kembali secara curang untuk kedua kalinya.

Segel sekali pakai adalah primitif kriptografi, yang diusulkan pada tahun 2016 oleh Peter Todd, mirip dengan konsep segel fisik: setelah segel ditempatkan pada wadah, menjadi tidak mungkin untuk membuka atau memodifikasinya tanpa merusak segel secara permanen.

![RGB-Bitcoin](assets/fr/018.webp)

Pendekatan ini, yang dialihkan ke dunia digital, memungkinkan untuk membuktikan bahwa rangkaian peristiwa memang telah terjadi, dan tidak dapat lagi diubah secara a posteriori. Segel sekali pakai dengan demikian melampaui logika sederhana `hash + cap waktu`, menambahkan gagasan segel yang dapat ditutup **hanya sekali**.

![RGB-Bitcoin](assets/fr/017.webp)

Agar Segel Sekali Pakai dapat berfungsi, Anda membutuhkan media bukti publikasi yang mampu membuktikan ada atau tidaknya publikasi, dan sulit (jika bukan tidak mungkin) untuk dipalsukan setelah informasi tersebut disebarkan. Sebuah **blockchain** (seperti Bitcoin) dapat mengisi peran ini, seperti halnya koran dengan sirkulasi publik, misalnya. Idenya adalah sebagai berikut:


- Kami ingin membuktikan bahwa komitmen tertentu pada pesan `h(m)` telah dipublikasikan kepada audiens tanpa mengungkapkan isi pesan `m`;
- Kami ingin membuktikan bahwa tidak ada komitmen pesan `h(m')` lain yang bersaing yang telah diterbitkan sebagai pengganti `h(m)`;
- Kami juga ingin dapat memeriksa bahwa pesan `m` ada sebelum tanggal tertentu.

Blockchain sangat cocok untuk peran ini: segera setelah sebuah transaksi dimasukkan ke dalam sebuah blok, seluruh jaringan memiliki bukti yang tidak dapat dipalsukan mengenai keberadaan dan isinya (setidaknya sebagian, karena _commitment_ dapat menyembunyikan detailnya sekaligus membuktikan keaslian pesan).

Oleh karena itu, Segel Sekali Pakai dapat dilihat sebagai janji formal untuk mempublikasikan pesan (yang masih belum diketahui pada tahap ini) sekali dan hanya sekali, dengan cara yang dapat diverifikasi oleh semua pihak yang berkepentingan.

Tidak seperti _komitmen_ (hash) atau stempel waktu yang sederhana, yang membuktikan tanggal keberadaannya, Segel Sekali Pakai menawarkan jaminan tambahan bahwa **tidak ada komitmen alternatif** yang dapat hidup berdampingan: Anda tidak dapat menutup segel yang sama dua kali, atau mencoba mengganti pesan yang disegel.

Perbandingan berikut ini membantu untuk memahami prinsip ini:


- Komitmen kriptografi (hash)**: Dengan fungsi hash, Anda dapat berkomitmen pada sepotong data (angka) dengan menerbitkan hash-nya. Data tetap rahasia sampai Anda mengungkapkan pra-gambar, tetapi Anda dapat membuktikan bahwa Anda sudah mengetahuinya sebelumnya;
- Stempel waktu (blockchain)**: Dengan memasukkan hash ini ke dalam blockchain, kita juga membuktikan bahwa kita mengetahuinya pada saat yang tepat (saat dimasukkan ke dalam blok);
- Segel sekali pakai**: Dengan segel sekali pakai, kami melangkah lebih jauh dengan membuat komitmen yang unik. Dengan satu hash, Anda dapat membuat beberapa komitmen yang bertentangan secara paralel (masalah dokter yang mengumumkan "*Ini anak laki-laki*" kepada keluarga dan "*Ini anak perempuan*" dalam buku harian pribadinya). Segel Sekali Pakai menghilangkan kemungkinan ini dengan menghubungkan komitmen ke media bukti publikasi, seperti blockchain Bitcoin, sehingga pengeluaran UTXO secara definitif menyegel komitmen tersebut. Setelah dibelanjakan, UTXO yang sama tidak dapat dibelanjakan kembali untuk menggantikan komitmen.

| Segel sekali pakai | Stempel waktu | Komitmen sederhana (digest/hash) | Segel sekali pakai

| -------------------------------------------------------------------------------- | ------------------------------- | ---------- | ---------------- |

| Publikasi komitmen tidak mengungkapkan pesan | Ya | Ya | Ya | Ya

| Bukti tanggal komitmen / keberadaan pesan sebelum tanggal tertentu | Tidak mungkin | Mungkin | Mungkin | Mungkin

| Bukti bahwa tidak ada komitmen alternatif lain yang dapat dilakukan | Tidak mungkin | Mungkin |

Segel sekali pakai bekerja dalam tiga tahap utama:

*definisi Segel :** * Segel Definisi :**


- Alice mendefinisikan terlebih dahulu aturan untuk menerbitkan segel (kapan, di mana, dan bagaimana pesan akan diterbitkan);
- Bob menerima atau mengetahui ketentuan-ketentuan ini.

![RGB-Bitcoin](assets/fr/021.webp)

**Penutupan Segel :**


- Pada saat runtime, Alice menutup segel dengan mempublikasikan pesan yang sebenarnya (biasanya dalam bentuk _commitment_, misalnya hash);
- Segel ini juga menyediakan **saksi** (bukti kriptografi) yang membuktikan bahwa segel tersebut tertutup dan tidak dapat dibatalkan.

![RGB-Bitcoin](assets/fr/019.webp)

**Verifikasi Segel :**


- Setelah segel ditutup, Bob tidak dapat lagi membukanya: dia hanya dapat memeriksa bahwa segel telah ditutup;
- Bob mengumpulkan stempel, **saksi** dan pesan (atau komitmennya) untuk memastikan bahwa semuanya cocok dan tidak ada stempel yang bersaing atau versi yang berbeda.

Prosesnya dapat diringkas sebagai berikut:

```txt
# Défini par Alice, validé ou accepté par Bob
seal <- Define()
# Fermeture du sceau par Alice avec le message
witness <- Close(seal, message)
# Vérification par Bob
bool <- Verify(seal, witness, message)
```

Akan tetapi, validasi sisi klien melangkah lebih jauh: jika definisi segel itu sendiri tetap berada di luar blockchain, ada kemungkinan (secara teori) bagi seseorang untuk menantang keberadaan atau keabsahan segel yang dimaksud. Untuk mengatasi masalah ini, rantai Segel Sekali Pakai yang saling terkait digunakan:


- Setiap segel tertutup berisi definisi segel berikut ini;
- Kami mendaftarkan penutupan ini (dengan _komitmen_ mereka) di dalam blockchain (dalam transaksi Bitcoin);
- Dengan demikian, setiap usaha untuk memodifikasi segel sebelumnya akan bertentangan dengan sejarah yang tertanam dalam Bitcoin.

Inilah yang dilakukan oleh sistem RGB:


- Pesan yang dipublikasikan adalah _komitmen_ terhadap data yang divalidasi di sisi klien;
- Definisi segel dikaitkan dengan Bitcoin UTXO;
- Segel akan menutup ketika UTXO ini dihabiskan atau ketika output baru dikreditkan ke komitmen yang sama;
- Rantai transaksi yang menggunakan UTXO ini sesuai dengan bukti publikasi: setiap transisi atau perubahan status pada RGB ditambatkan pada Bitcoin.

Kesimpulannya:


- Definisi _seal_ adalah UTXO yang ingin Anda gunakan untuk menyegel komitmen di masa depan;
- Penutupan _seal_ terjadi ketika Anda membelanjakan UTXO ini, menciptakan transaksi yang berisi komitmen;
- Saksi adalah transaksi itu sendiri, yang membuktikan bahwa Anda telah menutup segel dengan konten ini;
- Anda tidak dapat membuktikan bahwa sebuah seal belum ditutup (Anda tidak dapat benar-benar yakin bahwa UTXO belum dibelanjakan atau tidak akan dibelanjakan di blok yang belum Anda lihat), tetapi Anda dapat membuktikan bahwa seal tersebut memang telah ditutup.

Keunikan ini penting untuk Validasi Sisi Klien: ketika Anda memvalidasi transisi keadaan, Anda memeriksa bahwa transisi tersebut sesuai dengan UTXO yang unik, bukan yang sebelumnya dibelanjakan dalam komitmen yang bersaing. Inilah yang menjamin tidak adanya pembelanjaan ganda dalam smart contract off-chain.

### Berbagai komitmen dan akar

Sebuah kontrak pintar RGB mungkin perlu menggunakan beberapa Segel Sekali Pakai (beberapa UTXO) secara bersamaan. Terlebih lagi, satu transaksi Bitcoin dapat merujuk ke beberapa kontrak yang berbeda, masing-masing menyegel transisi statusnya sendiri. Hal ini membutuhkan mekanisme **multi-komitmen** untuk membuktikan, secara pasti dan unik, bahwa tidak ada komitmen yang ada dalam bentuk ganda. Di sinilah gagasan tentang **anchor** berperan dalam RGB: sebuah struktur khusus yang menghubungkan transaksi Bitcoin dan satu atau lebih komitmen dari sisi klien (state transition), yang masing-masing berpotensi menjadi bagian dari kontrak yang berbeda. Kita akan melihat lebih dekat konsep ini di bab selanjutnya.

![RGB-Bitcoin](assets/fr/023.webp)

Dua repositori GitHub utama proyek ini (di bawah organisasi LNPBP) mengelompokkan implementasi dasar dari konsep-konsep yang telah dipelajari di bab pertama:


- client_side_validation** : Berisi primitif Rust untuk validasi lokal;
- segel sekali pakai**: Menerapkan logika untuk menentukan dan menutup segel ini dengan aman.

![RGB-Bitcoin](assets/fr/020.webp)

Perlu dicatat bahwa batu bata perangkat lunak ini bersifat agnostik terhadap Bitcoin; secara teori, batu bata ini dapat diterapkan pada media bukti publikasi lainnya (registri lain, jurnal, dan lain-lain). Dalam praktiknya, RGB bergantung pada Bitcoin karena ketangguhan dan konsensus yang luas.

![RGB-Bitcoin](assets/fr/021.webp)

### Pertanyaan dari masyarakat

#### Menuju penggunaan Segel Sekali Pakai yang lebih luas

Peter Todd juga menciptakan protokol _Open Timestamps_, dan konsep Segel Sekali Pakai merupakan perluasan alami dari ide-ide ini. Di luar RGB, kasus penggunaan lain dapat dipertimbangkan, seperti pembangunan _sidechain_ tanpa menggunakan _merge mining_ atau proposal terkait drivechain seperti BIP300. Sistem apa pun yang membutuhkan komitmen tunggal pada prinsipnya dapat mengeksploitasi primitif kriptografi ini. Saat ini, RGB merupakan implementasi skala penuh yang pertama.

#### Masalah ketersediaan data

Karena dalam Validasi Sisi Klien, setiap pengguna menyimpan bagian riwayatnya sendiri, ketersediaan data tidak dijamin secara global. Jika penerbit kontrak menahan atau mencabut informasi tertentu, Anda mungkin tidak mengetahui evolusi penawaran yang sebenarnya. Dalam beberapa kasus (seperti stablecoin), penerbit diharapkan untuk menyimpan data publik untuk membuktikan volume yang beredar, tetapi tidak ada kewajiban teknis untuk melakukannya. Oleh karena itu, ada kemungkinan untuk mendesain kontrak yang sengaja dibuat buram dengan pasokan yang tidak terbatas, yang menimbulkan pertanyaan tentang kepercayaan.

#### Isolasi pecahan dan kontrak

Setiap kontrak mewakili _shard_ yang terisolasi: USDT dan USDC, misalnya, tidak harus berbagi sejarah. Pertukaran atom masih dimungkinkan, tetapi ini tidak melibatkan penggabungan register mereka. Semuanya dilakukan dengan komitmen kriptografi, tanpa mengungkapkan seluruh grafik riwayat kepada setiap peserta.

### Kesimpulan

Kita telah melihat bagaimana konsep Validasi Sisi Klien cocok dengan blockchain dan _state channel_, bagaimana konsep ini menanggapi trilema komputasi terdistribusi, dan bagaimana konsep ini memanfaatkan blockchain Bitcoin secara unik untuk menghindari pembelanjaan ganda dan untuk *time-stamping*. Idenya didasarkan pada gagasan **Single-use Seal**, yang memungkinkan pembuatan komitmen unik yang tidak dapat Anda gunakan kembali sesuka hati. Dengan cara ini, setiap peserta hanya mengunggah riwayat yang benar-benar diperlukan, meningkatkan skalabilitas dan kerahasiaan smart contract sambil mempertahankan keamanan Bitcoin sebagai latar belakang.

Langkah selanjutnya adalah menjelaskan secara lebih detail bagaimana mekanisme Segel Sekali Pakai ini diterapkan dalam Bitcoin (melalui UTXO), bagaimana jangkar dibuat dan divalidasi, dan kemudian bagaimana kontrak pintar yang lengkap dibuat dalam RGB. Secara khusus, kita akan melihat masalah komitmen ganda, tantangan teknis untuk membuktikan bahwa transaksi Bitcoin secara bersamaan menyegel beberapa transisi keadaan dalam kontrak yang berbeda, tanpa menimbulkan kerentanan atau komitmen ganda.

Sebelum masuk ke dalam detail yang lebih teknis pada bab kedua, jangan ragu untuk membaca ulang definisi-definisi kunci (Validasi Sisi Klien, Segel sekali pakai, jangkar, dll.) dan ingatlah logika secara keseluruhan: kita ingin menyatukan kekuatan blockchain Bitcoin (keamanan, desentralisasi, stempel waktu) dengan solusi-solusi di luar rantai (kecepatan, kerahasiaan, skalabilitas), dan inilah yang ingin dicapai oleh RGB dan Validasi Sisi Klien.

## Lapisan komitmen

<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>

![video](https://youtu.be/FS6PDprWl5Q)

Pada bab ini, kita akan melihat implementasi Validasi Sisi Klien dan Segel Sekali Pakai di dalam blockchain Bitcoin. Kami akan menyajikan prinsip-prinsip utama dari **lapisan komitmen** (lapisan 1) RGB, dengan fokus khusus pada skema **TxO2**, yang digunakan RGB untuk mendefinisikan dan menutup segel dalam transaksi Bitcoin. Selanjutnya, kita akan membahas dua poin penting yang belum dibahas secara mendetail:


- Komitmen Bitcoin yang bersifat deterministik;
- Komitmen multi-protokol.

Kombinasi dari konsep-konsep inilah yang memungkinkan kita untuk menumpangkan beberapa sistem atau kontrak di atas satu UTXO dan oleh karena itu menjadi satu blockchain.

Perlu diingat bahwa operasi kriptografi yang dijelaskan dapat diterapkan, secara absolut, pada blockchain atau media penerbitan lainnya, tetapi karakteristik Bitcoin (dalam hal desentralisasi, resistensi terhadap penyensoran dan keterbukaan terhadap semua) menjadikannya fondasi yang ideal untuk mengembangkan programabilitas tingkat lanjut seperti yang dibutuhkan oleh **RGB**.

### Skema komitmen dalam Bitcoin dan penggunaannya oleh RGB

Seperti yang telah kita lihat pada bab pertama kursus ini, Segel Sekali Pakai adalah sebuah konsep umum: kita membuat sebuah janji untuk menyertakan sebuah komitmen (_commitment_) pada sebuah lokasi tertentu pada sebuah transaksi, dan lokasi ini berfungsi seperti sebuah segel yang menutup sebuah pesan. Akan tetapi, pada blockchain Bitcoin, terdapat beberapa pilihan untuk memilih di mana kita dapat menempatkan _commitment_ ini.

Untuk memahami logikanya, mari kita ingat kembali prinsip dasarnya: untuk menutup _segel sekali pakai_, kita menghabiskan area yang disegel dengan memasukkan _komitmen_ pada pesan yang diberikan. Dalam Bitcoin, hal ini dapat dilakukan dengan beberapa cara:


- Gunakan kunci atau alamat publik**

Kita dapat memutuskan bahwa kunci atau alamat publik tertentu adalah _segel sekali pakai_. Segera setelah kunci atau alamat ini muncul secara berantai dalam sebuah transaksi, ini berarti segel tersebut ditutup dengan pesan tertentu.


- Menggunakan hasil transaksi Bitcoin**

Ini berarti bahwa segel sekali pakai didefinisikan sebagai _outpoint_ yang tepat (pasangan nomor TXID + nomor keluaran). Segera setelah _outpoint_ ini dihabiskan, segel ditutup.

Ketika mengerjakan RGB, kami mengidentifikasi setidaknya 4 cara berbeda untuk mengimplementasikan segel ini pada Bitcoin:


- Tentukan segel melalui kunci publik, dan tutup dalam _output_ ;
- Tentukan segel dengan _outpoint_ dan tutup dengan _output_ ;
- Tentukan segel melalui nilai kunci publik, dan tutup dalam _input_ ;
- Tentukan segel melalui _outpoint_, dan tutup dengan _input_.

| Definisi segel | Penutupan segel | Persyaratan tambahan | Aplikasi utama | Skema pertunangan yang memungkinkan |

| ------------- | ------------------------- | --------------------- | ----------------------------------------------------------------- | ---------------------------- | ------------------------------ |

| P2 (W) PKH | Tidak ada saat ini | Keytweak, taptweak, opret |

| TxO2 | Keluaran transaksi | Keluaran transaksi | Membutuhkan komitmen deterministik pada Bitcoin | RGBv1 (universal) | Keytweak, tapret, opret

| PkI | Nilai kunci publik | Entri transaksi | Hanya Taproot & tidak kompatibel dengan dompet lama | Identitas berbasis Bitcoin | Sigtweak, witweak

| TxO1 | Keluaran transaksi | Masukan transaksi | Hanya Taproot & tidak kompatibel dengan dompet lama | Tidak ada saat ini | Sigtweak, witweak |

Kita tidak akan membahas secara detail mengenai masing-masing konfigurasi ini, karena dalam RGB kita telah memilih untuk menggunakan _outpoint_ sebagai definisi seal**, dan menempatkan _commitment_ pada keluaran transaksi yang menggunakan _outpoint_ ini. Oleh karena itu, kita dapat memperkenalkan konsep-konsep berikut untuk sekuelnya:


- "Definisi segel "** : Titik _output_ yang diberikan (diidentifikasi oleh TXID + no. output);
- "Penutupan segel "**: Transaksi yang menghabiskan _outpoint_ ini, di mana _komitmen_ ditambahkan ke pesan.

Skema ini dipilih karena kompatibilitasnya dengan arsitektur RGB, tetapi konfigurasi lainnya dapat berguna untuk penggunaan yang berbeda.

"O2" dalam "TxO2" mengingatkan kita bahwa definisi dan penutupan didasarkan pada pengeluaran (atau penciptaan) output transaksi.

### Contoh diagram TxO2

Sebagai pengingat, mendefinisikan _single-use seal_ tidak selalu membutuhkan penerbitan transaksi on-chain. Alice, misalnya, cukup memiliki UTXO yang tidak terpakai. Dia dapat memutuskan: "Titik keluar ini (yang sudah ada) sekarang menjadi segel saya". Dia mencatat ini secara lokal (_sisi-klien_), dan sampai UTXO ini dibelanjakan, segel dianggap terbuka.

![RGB-Bitcoin](assets/fr/024.webp)

Pada hari ketika ia ingin menutup segel (untuk menandakan sebuah peristiwa, atau untuk menambatkan pesan tertentu), ia akan menggunakan UTXO ini dalam sebuah transaksi baru (transaksi ini sering disebut dengan "_witness transaction_" (tidak ada hubungannya dengan _segwit_, ini hanyalah istilah yang kami berikan). Transaksi baru ini akan berisi _commitment_ untuk pesan tersebut.

![RGB-Bitcoin](assets/fr/025.webp)

Perhatikan, bahwa dalam contoh ini :


- Tidak seorang pun kecuali Bob (atau orang yang dipilih Alice untuk mengungkapkan bukti lengkap) akan mengetahui bahwa ada pesan tertentu yang disembunyikan dalam transaksi ini;
- Semua orang dapat melihat bahwa _outpoint_ telah dibelanjakan, tetapi hanya Bob yang memiliki bukti bahwa pesan tersebut benar-benar berlabuh dalam transaksi.

Untuk mengilustrasikan skema TxO2 ini, kita dapat menggunakan segel sekali pakai sebagai mekanisme untuk mencabut kunci PGP. Alih-alih menerbitkan sertifikat pencabutan pada server, Alice dapat mengatakan: "Keluaran Bitcoin ini, jika dibelanjakan, berarti kunci PGP saya telah dicabut".

Oleh karena itu, Alice memiliki UTXO tertentu, di mana status atau data tertentu (yang hanya diketahui olehnya) diasosiasikan secara lokal (di sisi klien).

Alice memberi tahu Bob bahwa jika UTXO ini dibelanjakan, sebuah peristiwa tertentu akan dianggap telah terjadi. Dari luar, yang kita lihat hanyalah sebuah transaksi Bitcoin; tetapi Bob tahu bahwa pengeluaran ini memiliki makna tersembunyi.

![RGB-Bitcoin](assets/fr/026.webp)

Ketika Alice membelanjakan UTXO ini, ia menutup segel pada pesan yang menunjukkan kunci barunya, atau hanya pencabutan kunci lama. Dengan cara ini, siapa pun yang memonitor on-chain akan melihat bahwa UTXO telah dihabiskan, tetapi hanya mereka yang memiliki bukti lengkap yang akan mengetahui bahwa yang terjadi adalah pencabutan kunci PGP.

![RGB-Bitcoin](assets/fr/027.webp)

Agar Bob atau siapa pun yang terlibat dapat memeriksa pesan tersembunyi tersebut, Alice harus memberinya informasi di luar rantai.

![RGB-Bitcoin](assets/fr/028.webp)

Oleh karena itu, Alice harus memberikan Bob dengan :


- Pesan itu sendiri (misalnya, kunci PGP yang baru);
- Bukti kriptografi bahwa pesan tersebut terlibat dalam transaksi (dikenal sebagai _bukti transaksi tambahan_ atau _anchor_).

![RGB-Bitcoin](assets/fr/029.webp)

Pihak ketiga tidak memiliki informasi ini. Mereka hanya melihat bahwa UTXO telah dibelanjakan. Oleh karena itu, kerahasiaan terjamin.

Untuk memperjelas strukturnya, mari kita rangkum prosesnya dalam dua transaksi:


- Transaksi 1**: Ini berisi _definisi segel_, yaitu _titik akhir_ yang akan berfungsi sebagai segel.

![RGB-Bitcoin](assets/fr/031.webp)


- Transaksi 2**: Menghabiskan _outpoint_ ini. Ini menutup segel dan, dalam transaksi yang sama, memasukkan _komitmen_ pada pesan.

![RGB-Bitcoin](assets/fr/033.webp)

Oleh karena itu, kami menyebut transaksi kedua sebagai "transaksi saksi".

Untuk mengilustrasikan hal ini dari sudut pandang yang lain, kita bisa menggambarkannya dalam dua lapisan:


- Lapisan teratas (blockchain, publik)**: semua orang melihat transaksi dan mengetahui bahwa sebuah _outpoint_ telah dibelanjakan;
- Lapisan bawah (sisi klien, privat)**: hanya Alice (atau orang yang bersangkutan) yang tahu bahwa pengeluaran ini berhubungan dengan pesan ini dan itu, melalui bukti kriptografi dan pesan yang dia simpan secara lokal.

![RGB-Bitcoin](assets/fr/034.webp)

Tetapi ketika menutup segel, muncul pertanyaan di mana _commitment_ harus dimasukkan

Pada bagian sebelumnya, kita telah membahas secara singkat bagaimana model Validasi Sisi Klien dapat diterapkan pada RGB dan sistem lainnya. Di sini, kita akan membahas bagian mengenai **komitmen Bitcoin deterministik** dan bagaimana cara mengintegrasikannya ke dalam sebuah transaksi. Idenya adalah untuk memahami mengapa kita mencoba memasukkan satu komitmen ke dalam _witness transaction_, dan yang terpenting adalah bagaimana cara memastikan bahwa tidak ada komitmen lain yang tidak diungkapkan.

### Lokasi komitmen dalam sebuah transaksi

Ketika Anda memberikan bukti kepada seseorang bahwa sebuah pesan tertentu tertanam dalam sebuah transaksi, Anda harus dapat menjamin bahwa tidak ada bentuk komitmen lain (pesan kedua yang tersembunyi) dalam transaksi yang sama yang belum diungkapkan kepada Anda. Agar validasi dari sisi klien tetap kuat, Anda membutuhkan sebuah mekanisme **deterministik** untuk menempatkan sebuah _komitmen_ dalam transaksi yang menutup _segel sekali pakai_.

Transaksi _witness_ menghabiskan UTXO yang terkenal (atau _seal definition_) dan pengeluaran ini sesuai dengan penutupan segel. Secara teknis, kita tahu bahwa setiap titik keluar hanya dapat dibelanjakan satu kali. Inilah yang mendasari perlawanan Bitcoin terhadap pengeluaran ganda. Namun, transaksi pengeluaran dapat memiliki beberapa _input_, beberapa _output_, atau disusun dengan cara yang rumit (coinjoin, Lightning channel, dll.). Oleh karena itu, kita perlu mendefinisikan dengan jelas di mana kita harus memasukkan _commitment_ dalam struktur ini, dengan jelas dan seragam.

Apapun metodenya (PkO, TxO2, dll.), _commitment_ dapat disisipkan:


- Dalam sebuah Input** melalui :
    - Sigtweak** (memodifikasi komponen `r` dari tanda tangan ECDSA, mirip dengan prinsip "Tanda tangan-ke-kontrak");
    - Witweak** (data _segregated witness_ transaksi dimodifikasi).
- Dalam sebuah Output** melalui :
    - Keytweak** (kunci publik penerima "diutak-atik" dengan pesan);
    - Opret** (pesan ditempatkan dalam output yang tidak dapat dihabiskan `OP_RETURN`);
    - Tapret** (atau _Taptweak_), yang bergantung pada taproot untuk menyisipkan komitmen ke dalam bagian skrip dari kunci taproot, sehingga memodifikasi kunci publik secara deterministik.

![RGB-Bitcoin](assets/fr/035.webp)

Berikut ini adalah rincian dari masing-masing metode:

![RGB-Bitcoin](assets/fr/038.webp)

***Sig tweak (tanda tangan untuk kontrak) :***

Skema sebelumnya melibatkan eksploitasi bagian acak dari tanda tangan (ECDSA atau Schnorr) untuk menyematkan _komitmen_: ini adalah teknik yang dikenal sebagai "**Sign-to-contract**". Anda mengganti nonce yang dihasilkan secara acak dengan hash yang berisi data. Dengan cara ini, tanda tangan secara implisit mengungkapkan komitmen Anda, tanpa ruang tambahan dalam transaksi. Pendekatan ini memiliki beberapa keuntungan:


- Tidak ada kelebihan beban pada rantai (Anda menggunakan tempat yang sama dengan nonce dasar);
- Secara teori, hal ini bisa jadi sangat berbeda, karena nonce pada awalnya merupakan datum acak.

Namun demikian, ada 2 kelemahan utama yang muncul:


- Multisig sebelum Taproot: ketika Anda memiliki beberapa penandatangan, Anda harus memutuskan tanda tangan mana yang akan membawa _commitment_. Tanda tangan dapat dipesan secara berbeda, dan jika penandatangan menolak, Anda kehilangan kendali atas hasil _commitment_;
- MuSig dan nonce bersama: dengan Schnorr multisig (*MuSig*), pembuatan nonce merupakan sebuah algoritma multipartai, dan hampir tidak mungkin untuk mengubah nonce satu per satu.

Dalam praktiknya, **sig tweak** juga tidak terlalu kompatibel dengan perangkat keras yang ada (dompet perangkat keras) dan format (Lightning, dll.). Jadi, ide yang bagus ini sulit untuk dipraktikkan.

***Key tweak (bayar sesuai kontrak) :***

Tweak kunci ini mengambil konsep historis dari _bayar-ke-kontrak_. Kita mengambil kunci publik `X` dan mengubahnya dengan menambahkan nilai `H(pesan)`. Secara khusus, jika `X = x * G` dan `h = H(pesan)`, maka kunci baru akan menjadi `X' = X + h * G`. Kunci yang telah diubah ini menyembunyikan komitmen terhadap `pesan`. Pemegang kunci privat yang asli dapat, dengan menambahkan `h` ke kunci privatnya `x`, membuktikan bahwa ia memiliki kunci untuk mengeluarkan output. Secara teori, ini adalah hal yang elegan, karena :


- Komitmen_ dimasukkan tanpa menambahkan kolom tambahan;
- Anda tidak menyimpan data on-chain tambahan apa pun.

Namun dalam praktiknya, kami menghadapi beberapa kesulitan berikut ini:


- Dompet tidak lagi mengenali kunci publik standar, karena kunci tersebut telah "di-tweak", sehingga mereka tidak dapat dengan mudah mengasosiasikan UTXO dengan kunci yang biasa Anda gunakan;
- Dompet perangkat keras tidak didesain untuk menandatangani dengan kunci yang bukan berasal dari turunan standarnya;
- Anda perlu menyesuaikan skrip, deskriptor, dll.

Dalam konteks RGB, jalur ini telah dipertimbangkan hingga tahun 2021, tetapi terbukti terlalu rumit untuk membuatnya bekerja dengan standar dan infrastruktur saat ini.

***Saksikan perubahan :***

Ide lain, yang telah dipraktikkan oleh protokol tertentu seperti _inscriptions Ordinals_, adalah menempatkan data secara langsung pada bagian `saksi` dari transaksi (oleh karena itu disebut sebagai "witness tweak"). Akan tetapi, metode ini :


- Membuat keterlibatan segera terlihat (Anda benar-benar menempelkan data mentah ke dalam saksi);
- Dapat dikenakan sensor (penambang atau node dapat menolak untuk melakukan relay jika terlalu besar atau karakteristik sewenang-wenang lainnya);
- Menghabiskan ruang dalam blok, bertentangan dengan tujuan RGB yaitu keleluasaan dan cahaya.

Selain itu, saksi dirancang untuk dapat dipangkas dalam konteks tertentu, yang dapat membuat pembuktian yang kuat menjadi lebih rumit.

***Pengembalian terbuka (opret) :***

Sangat sederhana dalam pengoperasiannya, `OP_RETURN` memungkinkan Anda untuk menyimpan hash atau pesan dalam bidang khusus transaksi. Tetapi hal ini dapat segera terdeteksi: semua orang melihat bahwa ada _commitment_ dalam transaksi, dan dapat disensor atau dibuang, serta menambahkan output tambahan. Karena hal ini meningkatkan transparansi dan ukuran, ini dianggap kurang memuaskan dari sudut pandang solusi Validasi Sisi Klien.

```txt
34-byte_Opret_Commitment =
OP_RETURN   OP_PUSHBYTE_32   <mpc::Commitment>
|_________| |______________| |_________________|
1-byte       1-byte         32 bytes
```

### Tapret

Opsi terakhir adalah penggunaan **Taproot** (diperkenalkan dengan BIP341) dengan skema *Tapret*. *Tapret* adalah bentuk komitmen deterministik yang lebih kompleks, yang membawa peningkatan dalam hal jejak pada blockchain dan kerahasiaan untuk operasi kontrak. Ide utamanya adalah untuk menyembunyikan komitmen di bagian `Script Path Spend` dari [transaksi taproot] (https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki).

![RGB-Bitcoin](assets/fr/036.webp)

Sebelum menjelaskan bagaimana komitmen dimasukkan ke dalam transaksi taproot, mari kita lihat **bentuk yang tepat** dari komitmen, yang harus **secara imperatif** sesuai dengan string 64-byte [constructed] (https://github.com/BP-WG/bp-core/blob/master/dbc/src/tapret/mod.rs#L179-L196) sebagai berikut:

```txt
64-byte_Tapret_Commitment =
OP_RESERVED ...  ... .. OP_RESERVED   OP_RETURN   OP_PUSHBYTE_33  <mpc::Commitment>  <Nonce>
|___________________________________| |_________| |______________| |_______________|  |______|
OP_RESERVED x 29 times = 29 bytes      1 byte         1 byte          32 bytes        1 byte
|________________________________________________________________| |_________________________|
TAPRET_SCRIPT_COMMITMENT_PREFIX = 31 bytes                    MPC commitment + NONCE = 33 bytes
```


- 29 byte `OP_RESERVED`, diikuti dengan `OP_RETURN`, lalu `OP_PUSHBYTE_33`, membentuk bagian _prefix_ sebanyak 31 byte;
- Berikutnya adalah 32-byte _commitment_ (biasanya akar Merkle dari **MPC**), yang kemudian kita tambahkan 1 byte dari **Nonce** (total 33 byte untuk bagian kedua ini).

Jadi metode `Tapret` 64-byte terlihat seperti sebuah `Opret` yang mana kita telah mengawali 29 byte dari `OP_RESERVED` dan menambahkan byte tambahan sebagai Nonce.

Untuk menjaga fleksibilitas dalam hal implementasi, kerahasiaan, dan penskalaan, skema Tapret mempertimbangkan berbagai kasus penggunaan, tergantung pada kebutuhan:


- Penggabungan unik komitmen Tapret ke dalam transaksi taproot tanpa struktur Script Path yang sudah ada sebelumnya;
- Integrasi komitmen Tapret ke dalam transaksi Taproot yang sudah dilengkapi dengan Script Path.

Mari kita cermati lebih dekat masing-masing dari kedua skenario ini.

#### Penggabungan Tapret tanpa Jalur Skrip yang sudah ada

Dalam kasus pertama ini, kita mulai dari kunci keluaran taproot (*Kunci Keluaran Taproot*) `Q` yang hanya berisi kunci publik internal `P` *(Kunci Internal*), tanpa jalur skrip yang terkait (*Jalur Skrip*):

![RGB-Bitcoin](assets/fr/047.webp)


- `P`: kunci publik internal untuk _Key Path Spend_.
- `G`: titik pembangkit kurva elips [secp256k1] (https://en.bitcoin.it/wiki/Secp256k1).
- t = tH_TWEAK(P)` adalah faktor tweak, yang dihitung melalui hash yang ditandai (misalnya `SHA-256(SHA-256(TapTweak) || P)`), sesuai dengan [BIP86] (https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki#address-derivation). Ini membuktikan bahwa tidak ada skrip yang tersembunyi.

Untuk menyertakan komitmen **Tapret**, tambahkan **Skrip Jalur Pengeluaran** dengan **skrip unik**, sebagai berikut:

![RGB-Bitcoin](assets/fr/048.webp)


- t = tH_TWEAK(P || Script_root)` kemudian menjadi faktor tweak yang baru, termasuk **Script_root**.
- `Script_root = tH_BRANCH(64-byte_Tapret_Commitment)` merepresentasikan root dari **script** ini, yang merupakan sebuah hash dengan tipe `SHA-256(SHA-256(TapBranch) || 64-byte_Tapret_Commitment)`.

Bukti inklusi dan keunikan dalam pohon akar tunggang di sini bermuara pada kunci publik internal tunggal `P`.

#### Integrasi Tapret ke dalam Jalur Skrip yang sudah ada sebelumnya

Skenario kedua menyangkut keluaran `Q` taproot** yang lebih kompleks, yang sudah berisi beberapa skrip. Sebagai contoh, kita memiliki sebuah pohon yang terdiri dari 3 skrip:

![RGB-Bitcoin](assets/fr/049.webp)


- tH_LEAF(x)` menunjuk fungsi hash tag yang dinormalisasi dari skrip daun.
- a, B, C` mewakili skrip yang sudah termasuk dalam struktur akar tunggang.

Untuk menambahkan komitmen Tapret, kita perlu menyisipkan *script yang tidak dapat dihabiskan* pada tingkat pertama dari pohon, menggeser script yang ada satu tingkat ke bawah. Secara visual, pohon tersebut menjadi :

![RGB-Bitcoin](assets/fr/050.webp)


- tHABC` mewakili hash yang ditandai dari pengelompokan tingkat atas `A, B, C`.
- tHT` mewakili hash skrip yang sesuai dengan `Tapret` 64-byte.

Menurut aturan akar tunggang, setiap cabang/daun harus digabungkan menurut urutan hash leksikografis. Ada dua kasus yang mungkin terjadi:


- `tHT` > `tHABC`: komitmen Tapret bergerak ke sebelah kanan pohon. Bukti keunikan hanya membutuhkan `tHABC` dan `P`;
- tHT` < `tHABC`**: komitmen Tapret ditempatkan di sebelah kiri. Untuk membuktikan bahwa tidak ada komitmen Tapret lain di sebelah kanan, `tHAB` dan `tHC` harus diungkap untuk menunjukkan tidak adanya skrip lain.

Contoh visual untuk kasus pertama (`tHABC < tHT`):

![RGB-Bitcoin](assets/fr/051.webp)

Contoh untuk kasus kedua (`tHABC > tHT`):

![RGB-Bitcoin](assets/fr/052.webp)

#### Optimalisasi dengan nonce

Untuk meningkatkan kerahasiaan, kita dapat "menambang" (istilah yang lebih tepat adalah "bruteforcing") nilai dari `<Nonce>` (byte terakhir dari 64-byte `Tapret`) dalam upaya untuk mendapatkan hash `tHT` sedemikian rupa sehingga `tHABC < tHT`. Dalam kasus ini, komitmen ditempatkan di sebelah kanan, sehingga pengguna tidak perlu membocorkan seluruh isi skrip yang ada untuk membuktikan keunikan Tapret.

Singkatnya, `Tapret` menawarkan cara diskrit dan deterministik untuk memasukkan komitmen ke dalam transaksi taproot, sambil tetap menghormati persyaratan keunikan dan ketidakjelasan yang penting untuk Validasi Sisi Klien dan logika Segel Sekali Pakai RGB.

#### Pintu keluar yang valid

Untuk transaksi komitmen RGB, persyaratan utama untuk skema komitmen Bitcoin yang valid adalah sebagai berikut: Transaksi (*transaksi saksi*) harus dapat dibuktikan mengandung satu komitmen. Persyaratan ini membuat tidak mungkin untuk membuat riwayat alternatif untuk data yang divalidasi dari sisi klien dalam transaksi yang sama. Ini berarti bahwa pesan yang ditutup oleh _single-use seal_ adalah unik.

Untuk memenuhi prinsip ini, dan terlepas dari jumlah output dalam sebuah transaksi, kami mensyaratkan bahwa **satu dan hanya satu output** yang dapat berisi komitmen (*komitmen*). Untuk setiap skema yang digunakan (*Opret* atau *Tapret*), satu-satunya keluaran yang valid yang dapat berisi _komitmen_ RGB adalah :


- Keluaran pertama `OP_RETURN` (jika ada) untuk skema *Opret*;
- Output akar tunggang pertama (jika ada) untuk skema *Tapret*.

Perhatikan bahwa sangat mungkin sebuah transaksi mengandung satu komitmen `Opret` dan satu komitmen `Tapret` dalam dua keluaran yang terpisah. Berkat sifat deterministik dari Seal Definition, kedua komitmen ini kemudian sesuai dengan dua bagian data yang berbeda yang divalidasi di sisi klien.

### Analisis dan pilihan praktis dalam RGB

Ketika kami memulai RGB, kami meninjau semua metode ini untuk menentukan di mana dan bagaimana menempatkan _commitment_ dalam sebuah transaksi dengan cara yang deterministik. Kami mendefinisikan beberapa kriteria:


- Kompatibilitas dengan berbagai skenario (mis. multisig, Lightning, dompet perangkat keras, dll.);
- Berdampak pada ruang on-chain;
- Kesulitan implementasi dan pemeliharaan;
- Kerahasiaan dan ketahanan terhadap sensor.

| Ukuran jejak dan on-chain | Ukuran sisi klien | Integrasi portofolio | Kompatibilitas perangkat keras | Kompatibilitas Lightning | Kompatibilitas Taproot |

| --------------------------------------------------- | ------------------------ | ------------------ | ----------------------------- | ------------------------ | ----------------------- | --------------------- |

| Keytweak (P2C deterministik) | 🟢 | 🟡 | 🔴 | 🟠 | 🔴 BOLT, 🔴 Bifrost | 🟠 Taproot, 🟢 MuSig |

| Sigtweak (S2C deterministik) | 🟢 | 🟠 | 🔴 | 🔴 BOLT, 🔴 Bifrost | 🟠 Taproot, 🔴 MuSig |

| Opret (OP_RETURN) | 🔴 | 🟢 | 🟢 | 🟠 | 🔴 BOLT, 🟠 Bifrost | - |

| Algoritma Tapret: simpul kiri atas | 🟠 | 🔴 | 🟠 | 🟢 | 🔴 BOLT, 🟢 Bifrost | 🟢 Taproot, 🟢 MuSig |

| Algoritma Tapret #4: simpul apa saja + bukti | 🟢 | 🟠 | 🟢 | 🔴 BOLT, 🟢 Bifrost | 🟢 Taproot, 🟢 MuSig |

| Skema komitmen deterministik | Standar | Biaya on-chain | Ukuran bukti dari sisi pelanggan |

| ------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |

| Keytweak (P2C deterministik) | LNPBP-1, 2 | 0 byte | 33 byte (kunci yang tidak diubah) |

| Sigtweak (S2C deterministik) | WIP (LNPBP-39) | 0 byte | 0 byte |

| Opret (OP_RETURN) | - | 36 (v) byte (TxOut tambahan) | 0 byte

| Algoritma Tapret: simpul kiri atas | LNPBP-6 | 32 byte dalam saksi (8 vbytes) pada multisig n-of-m dan pengeluaran per jalur skrip | 0 byte pada skrip tanpa skrip taproot ~ 270 byte dalam satu kasus skrip, ~ 128 byte jika lebih dari satu skrip

| Algoritma Tapret #4: simpul apa pun + bukti keunikan | LNPBP-6 | 32 byte pada saksi (8 vbyte) untuk kasus skrip tunggal, 0 byte pada saksi di sebagian besar kasus lainnya | 0 byte pada skrip tanpa skrip taproot, 65 byte hingga Taptree memiliki selusin skrip

| Lapisan | Biaya on-chain (byte/vbyte) | Biaya on-chain (byte/vbyte) | Biaya on-chain (byte/vbyte) | Biaya on-chain (byte/vbyte) | Biaya on-chain (byte/vbyte) | Biaya sisi-klien (byte) | Biaya sisi-klien (byte) | Biaya sisi-klien (byte) | Biaya sisi-klien (byte) | Biaya sisi-klien (byte) | Biaya sisi-klien (byte)

| ------------------------------ | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |

| **Tipe** | **Tapret** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret** | **Tapret** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret** |

| Tanda tunggal | 0 | 0 | 0 | 0 | 32 | 0 | 0 | 32 | 0? | 0 | 0 |

| MuSig (n-of-n) | 0 | 0 | 0 | 32 | 0 | 0 | 32 | ? > 0 | 0 |

| Multi-sig 2-dari-3 | 32/8 | 32/8 atau 0 | 0 n/a | 32 | ~270 | 65 | 32 | n/a | 0 |

| Multi-sig 3-dari-5 | 32/8 | 32/8 atau 0 | 0 n/a | 32 | ~340 | 65 | 32 | n/a | 0 |

| Multi-sig 2-dari-3 dengan batas waktu | 32/8 | 0 | 0 n/a | 32 | 64 | 65 | 32 | n/a | 0 | 0

| Lapisan | Biaya pada rantai (vbytes) | Biaya pada rantai (vbytes) | Biaya pada rantai (vbytes) | Biaya di sisi klien (byte) | Biaya di sisi klien (byte)

| -------------------------------- | ---------------------- | ---------------------- | ---------------------- | ------------------------ | ------------------------ |

| **Tipe** | **Dasar** | **Tapret #2** | **Tapret #4** | **Tapret #2** | **Tapret #4** |

| MuSig (n-of-n) | 16.5 | 0 | 0 | 0 | 0 | 0

| FROST (n-dari-m) | ? | 0 | 0 | 0 | 0 |

| Multi_a (n-dari-m) | 1+16n+8m | 8 | 8 | 33 * m | 65 |

| Cabang MuSig / Multi_a (n-dari-m) | 1+16n+8n+8xlog(n) | 8 | 0 | 64 | 65 |

| Dengan batas waktu (n-dari-m) | 1+16n+8n+8xlog(n) | 8 | 0 | 64 | 65 |

| Metode | Kerahasiaan dan skalabilitas | Interoperabilitas | Kompatibilitas | Portabilitas | Kompleksitas |

| ----------------------------------------- | ------------------------------ | ---------------- | ------------- | ----------- | ---------- |

| Keytweak (P2C deterministik) | 🟢 | 🔴 | 🔴 | 🟡 | 🟡 |

| Sigtweak (S2C deterministik) | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 |

| Opret (OP_RETURN) | 🔴 | 🟠 | 🔴 | 🟢 | 🟢 |

| Algo Tapret: simpul kiri atas | 🟠 | 🟢 | 🔴 | 🟠 |

| Algo Tapret #4: Simpul apa saja + bukti | 🟢 | 🟢 | 🟢 | 🟠 | 🔴 |

Selama penelitian, menjadi jelas bahwa tidak ada skema komitmen yang sepenuhnya kompatibel dengan standar Lightning saat ini (yang tidak menggunakan Taproot, _muSig2_ atau dukungan _komitmen_ tambahan). Upaya sedang dilakukan untuk memodifikasi konstruksi saluran Lightning (*BiFrost*) untuk memungkinkan penyisipan komitmen RGB. Ini adalah area lain di mana kita perlu meninjau struktur transaksi, kunci dan cara di mana pembaruan saluran ditandatangani.

Analisis menunjukkan bahwa, pada kenyataannya, metode lain (key tweak, sig tweak, witness tweak, dll.) menghadirkan bentuk komplikasi lain:


- Entah kita memiliki volume on-chain yang besar;
- Entah ada ketidakcocokan radikal dengan kode dompet yang ada;
- Solusi tersebut tidak dapat digunakan dalam multisig non-kooperatif.

Untuk RGB, ada dua metode yang menonjol: ***Opret*** dan **Tapret***, keduanya diklasifikasikan sebagai "Output Transaksi", dan kompatibel dengan mode TxO2 yang digunakan oleh protokol.

### Komitmen Multi Protokol - MPC

Pada bagian ini, kita akan melihat bagaimana **RGB** menangani agregasi beberapa kontrak (atau, lebih tepatnya, _bundel transisi_) dalam satu komitmen (*komitmen_) yang dicatat dalam transaksi Bitcoin melalui skema deterministik (menurut `Opret` atau `Tapret`). Untuk mencapai hal ini, urutan Merkelisasi dari berbagai kontrak dilakukan dalam sebuah struktur yang disebut **MPC Tree** (Pohon Komitmen Multi Protokol). Pada bagian ini, kita akan melihat konstruksi dari Pohon MPC ini, bagaimana mendapatkan akarnya, dan bagaimana beberapa kontrak dapat berbagi transaksi yang sama secara rahasia dan jelas.

Multi Protocol Commitment (MPC) dirancang untuk memenuhi dua kebutuhan:


- Konstruksi hash `mpc::Commitment`: ini akan dimasukkan ke dalam blockchain Bitcoin sesuai dengan skema `Opret` atau `Tapret`, dan harus merefleksikan semua perubahan status yang akan divalidasi;
- Penyimpanan beberapa kontrak secara simultan dalam satu _commitment_, memungkinkan pembaruan terpisah pada beberapa aset atau kontrak RGB untuk dikelola dalam satu transaksi Bitcoin.

Secara konkret, setiap _bundel transisi_ adalah milik kontrak tertentu. Semua informasi ini dimasukkan ke dalam **MPC Tree**, yang akarnya (`mpc::Root`) kemudian di-hash lagi untuk menghasilkan `mpc::Commitment`. Hash terakhir inilah yang ditempatkan dalam transaksi Bitcoin (_witness transaction_), sesuai dengan metode deterministik yang dipilih.

![RGB-Bitcoin](assets/fr/042.webp)

#### Hash Akar MPC

Nilai yang sebenarnya ditulis secara on-chain (dalam `Opret` atau `Tapret`) disebut `mpc::Commitment`. Ini dihitung dalam bentuk [BIP-341] (https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki), menurut rumus :

```txt
mpc::Commitment = SHA-256(SHA-256(mpc_tag) || SHA-256(mpc_tag) || depth || cofactor || mpc::Root )
```

di mana:


- `mpc_tag` adalah sebuah tag: `urn:ubideco:mpc:commitment#2024-01-31`, yang dipilih menurut [konvensi penandaan RGB](https://github.com/RGB-WG/rgb-core/blob/master/doc/Commitments.md);
- `depth` (1 byte) menunjukkan kedalaman *MPC Tree*;
- kofaktor` (16 bit, dalam Little Endian) adalah sebuah parameter yang digunakan untuk mempromosikan keunikan posisi yang ditetapkan untuk setiap kontrak dalam pohon;
- `mpc::Root` adalah akar dari *MPC Tree*, dihitung menurut proses yang dijelaskan pada bagian berikutnya.

![RGB-Bitcoin](assets/fr/044.webp)

#### Konstruksi pohon MPC

Untuk membangun Pohon MPC ini, kita perlu memastikan bahwa setiap kontrak berhubungan dengan posisi daun yang unik. Misalkan kita memiliki :


- c` kontrak yang akan disertakan, diindeks oleh `i` dalam `i = {0,1,..,C-1}`;
- Untuk setiap kontrak `c_i`, kita memiliki pengenal `ContractId(i) = c_i`.

Kita kemudian membuat sebuah pohon dengan lebar `w` dan kedalaman `d` sedemikian rupa sehingga `2^d = w`, dengan `w > C`, sehingga setiap kontrak dapat ditempatkan pada _daun_ yang terpisah. Posisi `pos(c_i)` dari setiap kontrak dalam pohon ditentukan oleh :

```txt
pos(c_i) = c_i mod (w - cofactor)
```

di mana `cofactor` adalah bilangan bulat yang meningkatkan probabilitas untuk mendapatkan posisi yang berbeda untuk setiap kontrak. Dalam praktiknya, konstruksi mengikuti proses berulang:


- Kita mulai dari kedalaman minimum (`d=3` menurut konvensi untuk menyembunyikan jumlah kontrak yang tepat);
- Kami mencoba `cofactor` yang berbeda (hingga `w/2`, atau maksimum 500 untuk alasan performa);
- Jika kita gagal memposisikan semua kontrak tanpa tabrakan, kita menambah `d` dan memulai lagi.

Tujuannya adalah untuk menghindari pohon yang terlalu tinggi, sekaligus menjaga risiko tabrakan seminimal mungkin. Perlu diketahui bahwa fenomena tabrakan mengikuti logika distribusi acak, yang terkait dengan [Paradoks Hari Jadi] (https://en.wikipedia.org/wiki/Birthday_problem).

#### Daun yang dihuni

Setelah posisi `C` yang berbeda `pos(c_i)` telah diperoleh untuk kontrak `i = {0,1,..,C-1}`, setiap lembar diisi dengan fungsi hash (*tagged hash*):

```txt
tH_MPC_LEAF(c_i) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x10 || c_i || BundleId(c_i))
```

di mana:


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, selalu dipilih sesuai dengan konvensi Merkle RGB;
- `0x10` mengidentifikasi sebuah _daun kontrak_ ;
- `c_i` adalah pengenal kontrak 32-byte (berasal dari hash Genesis);
- bundleId(c_i)` adalah hash 32-byte yang menggambarkan himpunan `State Transitions` relatif terhadap `c_i` (dikumpulkan ke dalam *Transition Bundle*).

#### Daun yang tidak berpenghuni

Daun yang tersisa, yang tidak ditetapkan untuk kontrak (yaitu daun `w - C`), diisi dengan nilai "dummy" (daun _entropi_):

```txt
tH_MPC_LEAF(j) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x11 || entropy || j )
```

di mana:


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, selalu dipilih sesuai dengan konvensi Merkle RGB;
- `x11` menunjukkan sebuah _entropi daun_;
- 'Entropi' adalah nilai acak sebesar 64 byte, yang dipilih oleh orang yang membangun pohon;
- `j` adalah posisi (dalam 32 bit Little Endian) dari daun ini di dalam pohon.

#### Node MPC

Setelah menghasilkan daun `w` (berpenghuni atau tidak), kita lanjutkan ke merkelisasi. Setiap simpul internal di-hash sebagai berikut:

```txt
tH_MPC_BRANCH(tH1 || tH2) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || b || d || w || tH1 || tH2)
```

di mana:


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, selalu dipilih sesuai dengan konvensi Merkle RGB;
- b` adalah faktor percabangan (8 bit). Paling sering, `b=0x02` karena pohonnya biner dan lengkap;
- d` adalah kedalaman simpul dalam pohon;
- `w` adalah lebar pohon (dalam biner Little Endian 256-bit);
- tH1` dan `tH2` adalah hash dari simpul-simpul anak (atau daun), yang sudah dihitung seperti yang ditunjukkan di atas.

Dengan cara ini, kita mendapatkan root `mpc::Root`. Kita kemudian dapat menghitung `mpc::Commitment` (seperti yang dijelaskan di atas) dan menyisipkannya secara berantai.

Untuk mengilustrasikan hal ini, mari kita bayangkan sebuah contoh di mana `C=3` (tiga kontrak). Posisi mereka diasumsikan sebagai `pos(c_0)=7`, `pos(c_1)=4`, `pos(c_2)=2`. Daun-daun lainnya (posisi 0, 1, 3, 5, 6) adalah _devices entropi_. Diagram di bawah ini menunjukkan urutan hash ke akar dengan :


- `BUNDLE_i` yang merepresentasikan `BundleId(c_i)`;
- `tH_MPC_LEAF(A)` dan seterusnya, yang merepresentasikan daun (beberapa untuk kontrak, yang lain untuk entropi);
- Setiap cabang `tH_MPC_BRANCH(...)` menggabungkan hash dari dua anaknya.

Hasil akhirnya adalah **mpc::Root**, lalu `mpc::Commitment`.

![RGB-Bitcoin](assets/fr/053.webp)

#### Pemeriksaan poros MPC

Ketika seorang verifier ingin memastikan bahwa kontrak `c_i` (dan `BundleId`-nya) disertakan dalam `mpc::Commitment` akhir, dia cukup menerima bukti Merkle. Bukti ini mengindikasikan node-node yang dibutuhkan untuk melacak daun (dalam hal ini, _contract leaf_ dari `c_i`) kembali ke akar. Tidak perlu mengungkapkan seluruh *MPC Tree*: ini melindungi kerahasiaan kontrak-kontrak lainnya.

Pada contoh, verifier `c_2` hanya membutuhkan hash perantara (`tH_MPC_LEAF(D)`), dua buah `tH_MPC_BRANCH(...)`, bukti posisi `pos(c_2)`, dan nilai `cofactor`. Kemudian ia dapat merekonstruksi root secara lokal, lalu menghitung ulang `mpc::Commitment` dan membandingkannya dengan yang ditulis dalam transaksi Bitcoin (dalam `Opret` atau `Tapret`).

![RGB-Bitcoin](assets/fr/054.webp)

Mekanisme ini memastikan bahwa :


- Status relatif terhadap `c_2` memang termasuk dalam blok informasi agregat (sisi klien);
- Tidak ada yang dapat membuat riwayat alternatif dengan transaksi yang sama, karena _commitment_ on-chain menunjuk ke satu akar MPC.

#### Ringkasan struktur MPC

Multi Protocol Commitment* (MPC) adalah prinsip yang memungkinkan RGB untuk menggabungkan beberapa kontrak ke dalam satu transaksi Bitcoin, dengan tetap menjaga keunikan komitmen dan kerahasiaan terhadap partisipan lainnya. Berkat konstruksi pohon yang deterministik, setiap kontrak diberikan posisi yang unik, dan adanya daun "dummy" (*Entropy Leaves*) menutupi sebagian jumlah total kontrak yang berpartisipasi dalam transaksi.

Seluruh pohon Merkle tidak pernah disimpan pada klien. Kami hanya membuat _Merkle path_ untuk setiap kontrak yang bersangkutan, untuk dikirimkan ke penerima (yang kemudian dapat memvalidasi komitmen). Dalam beberapa kasus, Anda mungkin memiliki beberapa aset yang telah melewati UTXO yang sama. Anda kemudian dapat menggabungkan beberapa _Merkle path_ ke dalam apa yang disebut _block komitmen multi-protokol_, untuk menghindari duplikasi data yang terlalu banyak.

Oleh karena itu, setiap _Merkle proof_ ringan, terutama karena kedalaman pohon tidak akan melebihi 32 dalam RGB. Ada juga gagasan tentang "blok Merkle", yang menyimpan lebih banyak informasi (penampang melintang, entropi, dll.), yang berguna untuk menggabungkan atau memisahkan beberapa cabang.

Itulah mengapa butuh waktu lama untuk menyelesaikan RGB. Kami memiliki visi keseluruhan dari tahun 2019: meletakkan semuanya di sisi klien, mengedarkan token di luar rantai. Tetapi untuk detail seperti sharding untuk beberapa kontrak, struktur pohon Merkle, cara menangani tabrakan dan menggabungkan bukti... semua ini membutuhkan iterasi.

### Jangkar: perakitan global

Sebagai kelanjutan dari konstruksi komitmen kami (`Opret` atau `Tapret`) dan MPC (*Multi Protocol Commitment*), kita perlu membahas pengertian **Anchor** dalam protokol RGB. Anchor adalah struktur tervalidasi di sisi klien yang menyatukan elemen-elemen yang dibutuhkan untuk memverifikasi bahwa komitmen Bitcoin benar-benar berisi informasi kontrak tertentu. Dengan kata lain, Anchor merangkum semua data yang dibutuhkan untuk memvalidasi _komitmen_ yang dijelaskan di atas.

Jangkar terdiri dari tiga bidang yang dipesan:


- `Txid`
- 'Bukti MPC'
- bukti Transaksi Ekstra - ETP

Masing-masing bidang ini berperan dalam proses validasi, baik dalam hal merekonstruksi transaksi Bitcoin yang mendasari atau membuktikan adanya komitmen tersembunyi (terutama dalam kasus `Tapret`).

#### TxId

Kolom `Txid` sesuai dengan pengenal 32-byte dari transaksi Bitcoin yang berisi komitmen `Opret` atau `Tapret`.

Secara teori, adalah mungkin untuk menemukan `Txid` ini dengan menelusuri rantai transisi status yang mengarah ke setiap transaksi saksi, mengikuti logika Segel Sekali Pakai. Akan tetapi, untuk memudahkan dan mempercepat verifikasi, `Txid` ini hanya disertakan di dalam Anchor, sehingga validator tidak perlu menelusuri seluruh riwayat off-chain.

#### Bukti MPC

Kolom kedua, `Bukti MPC`, merujuk pada bukti bahwa kontrak khusus ini (misalnya `c_i`) termasuk dalam _Komitmen Multi Protokol_. Ini adalah kombinasi dari :


- `pos_i`, posisi kontrak ini dalam pohon MPC;
- kofaktor`, nilai yang ditentukan untuk menyelesaikan tabrakan posisi;
- bukti Merkle, yaitu kumpulan node dan hash yang digunakan untuk merekonstruksi root MPC dan memverifikasi bahwa pengenal kontrak dan `Transition Bundle`-nya telah dikomitmenkan ke root.

Mekanisme ini telah dijelaskan pada bagian sebelumnya tentang membangun *MPC Tree*, di mana setiap kontrak mendapatkan daun yang unik berkat ekstensi :

```txt
pos(c_i) = c_i mod (w - cofactor)
```

Kemudian, skema merkelisasi deterministik digunakan untuk menggabungkan semua daun (kontrak + entropi). Pada akhirnya, `MPC Proof` memungkinkan root untuk direkonstruksi secara lokal dan dibandingkan dengan `mpc::Commitment` yang disertakan pada rantai.

#### Bukti Transaksi Ekstra - ETP

Kolom ketiga, **ETP**, bergantung pada jenis komitmen yang digunakan. Jika komitmennya bertipe `Opret`, tidak ada bukti tambahan yang diperlukan. Validator memeriksa keluaran `OP_RETURN` pertama dari transaksi dan menemukan `mpc::Commitment` secara langsung di sana.

**Jika komitmennya berjenis `Tapret`, bukti tambahan yang disebut *Bukti Transaksi Ekstra - ETP* harus disediakan. Ini berisi :


- Kunci publik internal (`P`) dari keluaran akar tunggang di mana *komitmen* disematkan;
- Node mitra dari `Skrip Path Spend` (ketika Tapret *commitment* disisipkan dalam skrip), untuk membuktikan lokasi yang tepat dari skrip ini dalam pohon akar tunggang:
 - Jika *komitmen `Tapret` berada di cabang sebelah kanan, kita memperlihatkan simpul sebelah kiri (misalnya `tHABC`),
 - Jika *komitmen `Tapret` ada di sebelah kiri, Anda perlu mengungkapkan 2 node (mis. `tHAB` dan `tHC`) untuk membuktikan bahwa tidak ada *komitmen lain di sebelah kanan.
- `nonce` dapat digunakan untuk "menambang" konfigurasi terbaik, yang memungkinkan *komitmen* ditempatkan di sebelah kanan pohon (pengoptimalan bukti).

Bukti tambahan ini penting karena, tidak seperti `Opret`, komitmen `Tapret` diintegrasikan ke dalam struktur skrip taproot, yang membutuhkan pengungkapan bagian dari pohon taproot untuk memvalidasi lokasi *komitmen* dengan benar.

![RGB-Bitcoin](assets/fr/045.webp)

Oleh karena itu, **Anchor** merangkum semua informasi yang diperlukan untuk memvalidasi komitmen Bitcoin dalam konteks RGB. Mereka menunjukkan transaksi yang relevan (`Txid`) dan bukti posisi kontrak (`MPC Proof`), sambil mengelola bukti tambahan (`ETP`) dalam kasus `Tapret`. Dengan cara ini, Anchor melindungi integritas dan keunikan keadaan off-chain dengan memastikan bahwa transaksi yang sama tidak dapat ditafsirkan ulang untuk data kontrak lainnya.

### Kesimpulan

Dalam bab ini, kita akan membahas :


- Bagaimana menerapkan konsep Segel Sekali Pakai dalam Bitcoin (khususnya melalui _outpoint_);
- Berbagai metode untuk memasukkan _commitment_ secara deterministik ke dalam transaksi (Sig tweak, Key tweak, witness tweak, op_return, Taproot/Tapret);
- Alasan mengapa RGB berfokus pada komitmen Tapret ;
- Manajemen multi-kontrak melalui _komitmen multi-protokol_, penting jika Anda tidak ingin mengekspos seluruh negara bagian atau kontrak lain ketika Anda ingin membuktikan poin tertentu;
- Kita juga telah melihat peran _Anchors_, yang menyatukan semuanya (TXID transaksi, bukti pohon Merkle, dan bukti Taproot) dalam satu paket.

Dalam praktiknya, implementasi teknis dibagi antara beberapa peti khusus Rust (dalam _client_side_validation_, _commit-verify_, _bp_core_, dan lain-lain). Gagasan mendasarnya ada di sana:

![RGB-Bitcoin](assets/fr/046.webp)

Pada bab selanjutnya, kita akan melihat komponen off-chain murni dari RGB, yaitu logika kontrak. Kita akan melihat bagaimana kontrak RGB, yang diorganisir sebagai _finite state machine_ yang direplikasi sebagian, mencapai ekspresi yang jauh lebih tinggi daripada skrip Bitcoin, sambil menjaga kerahasiaan datanya.

## Pengantar kontrak pintar dan statusnya

<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>

![video](https://youtu.be/tmAVdyXGmj4)

Pada bab ini dan bab berikutnya, kita akan melihat gagasan **kontrak pintar** dalam lingkungan RGB dan mengeksplorasi berbagai cara di mana kontrak ini dapat mendefinisikan dan mengembangkan *state* mereka. Kita akan melihat mengapa arsitektur RGB, dengan menggunakan urutan yang teratur dari Segel Sekali Pakai, memungkinkan untuk mengeksekusi berbagai jenis ***Operasi Kontrak*** dengan cara yang dapat diskalakan dan tanpa melalui registri terpusat. Kita juga akan melihat peran mendasar dari ***Business Logic*** dalam membingkai evolusi status kontrak.

### Kontrak pintar dan hak pembawa digital

Tujuan RGB adalah menyediakan infrastruktur untuk mengimplementasikan kontrak pintar pada Bitcoin. Yang dimaksud dengan "kontrak pintar" adalah sebuah perjanjian antara beberapa pihak yang diberlakukan secara otomatis dan secara komputasi, tanpa campur tangan manusia untuk memberlakukan klausul-klausulnya. Dengan kata lain, hukum kontrak ditegakkan oleh perangkat lunak, bukan oleh pihak ketiga yang terpercaya.

Otomatisasi ini menimbulkan pertanyaan tentang desentralisasi: bagaimana kita dapat membebaskan diri kita dari registri terpusat (mis. platform atau basis data pusat) untuk mengelola kepemilikan dan kinerja kontrak? Ide awalnya, yang diambil oleh RGB, adalah untuk kembali ke mode kepemilikan yang dikenal sebagai "instrumen pembawa". Secara historis, sekuritas tertentu (obligasi, saham, dll.) diterbitkan dalam bentuk pembawa, memungkinkan siapa pun yang secara fisik memiliki dokumen tersebut untuk menegakkan hak-haknya.

![RGB-Bitcoin](assets/fr/055.webp)

RGB menerapkan konsep ini ke dunia digital: hak (dan kewajiban) dikemas dalam data yang dimanipulasi di luar rantai, dan status data ini divalidasi oleh para partisipan itu sendiri. Hal ini memungkinkan, secara apriori, tingkat kerahasiaan dan kemandirian yang jauh lebih besar daripada yang ditawarkan oleh pendekatan lain yang didasarkan pada register publik.

### Pengenalan status RGB Smart Contract

Kontrak pintar dalam RGB dapat dilihat sebagai mesin negara, yang didefinisikan oleh :


- A **State**, yaitu sekumpulan informasi yang mencerminkan konfigurasi kontrak saat ini;
- Sebuah **Business Logic** (seperangkat aturan), yang menjelaskan dalam kondisi apa dan oleh siapa status dapat dimodifikasi.

![RGB-Bitcoin](assets/fr/056.webp)

Penting untuk dipahami bahwa kontrak-kontrak ini tidak terbatas pada transfer token yang sederhana. Kontrak ini dapat mewujudkan berbagai macam aplikasi: mulai dari aset tradisional (token, saham, obligasi) hingga mekanisme yang lebih kompleks (hak penggunaan, ketentuan komersial, dll.). Tidak seperti blockchain lainnya, di mana kode kontrak dapat diakses dan dieksekusi oleh semua orang, pendekatan RGB mengkotak-kotakan akses dan pengetahuan tentang kontrak kepada para peserta ("***peserta kontrak***"). Ada beberapa peran:


- Penerbit** atau pembuat kontrak, yang mendefinisikan Kejadian kontrak dan variabel awalnya;
- Pihak yang memiliki hak** (*kepemilikan*) atau kemampuan penegakan hukum lainnya;
- Pengamat**, berpotensi terbatas untuk melihat informasi tertentu, tetapi tidak dapat memicu modifikasi.

Pemisahan peran ini berkontribusi pada ketahanan terhadap sensor, dengan memastikan bahwa hanya orang yang berwenang yang dapat berinteraksi dengan status kontrak. Hal ini juga memberikan RGB kemampuan untuk menskalakan secara horizontal: sebagian besar validasi terjadi di luar blockchain, dan hanya jangkar kriptografi (*komitmen*) yang tertulis di Bitcoin.

### Status dan Logika Bisnis dalam RGB

Dari sudut pandang praktis, **Logika Bisnis** kontrak berbentuk aturan dan skrip, yang didefinisikan dalam apa yang disebut RGB sebagai **Skema**. Skema mengkodekan :


- Struktur negara (bidang mana yang bersifat publik? Bidang mana yang dimiliki oleh pihak mana?
- Ketentuan validitas (apa yang harus diperiksa sebelum mengotorisasi pembaruan status?
- Otorisasi (siapa yang dapat memulai *Transisi Negara*? Siapa yang hanya dapat mengamati?).

Pada saat yang sama, **Kondisi Kontrak** sering kali terbagi menjadi dua komponen:


- A **Global State**: bagian publik, berpotensi dapat diamati oleh semua orang (tergantung konfigurasi);
- Owned States**: bagian pribadi, dialokasikan secara khusus kepada pemilik melalui UTXO yang dirujuk dalam logika kontrak.

Seperti yang akan kita lihat pada bab-bab selanjutnya, setiap pembaruan status (*Contract Operation*) harus terhubung dengan _commitment_ Bitcoin (melalui `Opret` atau `Tapret`) dan sesuai dengan skrip *Business Logic* agar dianggap valid.

### Operasi Kontrak: penciptaan dan evolusi Negara

Di alam semesta RGB, ***Operasi Kontrak*** adalah peristiwa apa pun yang mengubah kontrak dari **kondisi lama** ke **kondisi baru**. Operasi ini mengikuti logika berikut:


- Kami mencatat status kontrak saat ini;
- Kita menerapkan aturan atau operasi (***State Transition***, ***Genesis*** jika ini adalah state pertama, atau ***State Extension*** jika ada *valensi* publik untuk dipicu kembali);
- Kami mengaitkan modifikasi melalui _commitment_ baru pada blockchain, menutup satu _segel sekali pakai_ dan membuat yang lain;
- Pemegang hak yang bersangkutan memvalidasi secara lokal (*sisi klien*) bahwa transisi tersebut sesuai dengan *Skema* dan bahwa transaksi Bitcoin yang terkait didaftarkan secara on-chain.

![RGB-Bitcoin](assets/fr/057.webp)

Hasil akhirnya adalah sebuah kontrak yang telah diperbarui, dengan status yang berbeda. Transisi ini tidak mengharuskan seluruh jaringan Bitcoin untuk memperhatikan detailnya, karena hanya sidik jari kriptografi kecil (_commitment_) yang dicatat dalam blockchain. Urutan Segel Sekali Pakai mencegah pengeluaran ganda atau penggunaan ganda dari State.

### Rantai operasi: dari Kejadian hingga Status Terminal

Untuk menempatkan ini ke dalam perspektif, kontrak pintar RGB dimulai dengan **Genesis**, keadaan pertama. Setelah itu, berbagai Operasi Kontrak mengikuti satu sama lain, membentuk DAG (*Directed Acyclic Graph*) operasi:


- Setiap transisi didasarkan pada keadaan sebelumnya (atau beberapa keadaan, dalam kasus transisi konvergen);
- Urutan kronologis dijamin dengan dimasukkannya setiap transisi ke dalam jangkar Bitcoin, yang dicap waktu dan tidak dapat diubah berkat konsensus oleh Proof-of-Work ;
- Ketika tidak ada lagi operasi yang sedang berlangsung, **Terminal State** tercapai: kondisi kontrak yang paling baru dan lengkap.

![RGB-Bitcoin](assets/fr/012.webp)

Topologi DAG ini (bukan rantai linear sederhana) mencerminkan kemungkinan bahwa bagian-bagian yang berbeda dari kontrak dapat berkembang secara paralel, selama mereka tidak bertentangan satu sama lain. RGB kemudian menghindari ketidakkonsistenan dengan melakukan verifikasi *sisi-klien* terhadap setiap peserta yang terlibat.

### Ringkasan

Kontrak pintar di RGB memperkenalkan model instrumen pembawa digital, terdesentralisasi tetapi berlabuh di Bitcoin untuk penanda waktu dan menjamin urutan transaksi. Eksekusi otomatis dari kontrak-kontrak ini didasarkan pada :


- Status Kontrak*, yang menunjukkan konfigurasi kontrak saat ini (hak, saldo, variabel, dll.);
- Logika Bisnis (*Skema*), yang mendefinisikan transisi mana yang diperbolehkan dan bagaimana transisi tersebut harus divalidasi;
- Operasi Kontrak**, yang memperbarui status ini selangkah demi selangkah, berkat komitmen yang ditambatkan pada transaksi Bitcoin.

Pada bab selanjutnya, kita akan membahas lebih detail mengenai representasi konkret dari ***state*** dan ***state transition*** pada tingkat off-chain, dan bagaimana mereka berhubungan dengan UTXO dan Segel Sekali Pakai yang tertanam pada Bitcoin. Ini akan menjadi kesempatan untuk melihat bagaimana mekanisme internal RGB, berdasarkan validasi sisi klien, berhasil menjaga konsistensi kontrak pintar sambil menjaga kerahasiaan data.

## Operasi kontrak RGB

<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>

![video](https://youtu.be/lUTjeuM0oTA)

Pada bab ini, kita akan melihat bagaimana operasi dalam smart contract dan transisi state bekerja, sekali lagi dalam protokol RGB. Tujuannya juga untuk memahami bagaimana beberapa peserta bekerja sama untuk mentransfer kepemilikan aset.

### Transisi status dan mekanismenya

Prinsip umumnya masih sama dengan Validasi Sisi Klien, di mana data negara dipegang oleh pemilik dan divalidasi oleh penerima. Namun, kekhususan di sini dengan RGB terletak pada kenyataan bahwa Bob, sebagai penerima, meminta Alice untuk memasukkan informasi tertentu ke dalam data kontrak untuk memiliki kontrol nyata atas aset yang diterima, melalui referensi tersembunyi ke salah satu UTXO-nya.

Untuk mengilustrasikan proses *Transisi Status* (yang merupakan salah satu ***Operasi Kontrak*** fundamental dalam RGB), mari kita ambil contoh langkah demi langkah transfer aset antara Alice dan Bob:

**Situasi awal:**

Alice memiliki ***stash RGB*** data yang divalidasi secara lokal (*sisi klien*). Stash ini merujuk pada salah satu UTXO-nya di Bitcoin. Ini berarti bahwa _seal definition_ dalam data ini menunjuk pada UTXO milik Alice. Idenya adalah untuk memungkinkannya mentransfer hak digital tertentu yang terkait dengan aset (misalnya token RGB) kepada Bob.

![RGB-Bitcoin](assets/fr/058.webp)

**Bob juga memiliki UTXO :**

Bob, di sisi lain, memiliki setidaknya satu UTXO miliknya sendiri, tanpa hubungan langsung dengan Alice. Jika Bob tidak memiliki UTXO, masih memungkinkan untuk melakukan transfer kepadanya menggunakan *transaksi saksi* itu sendiri: hasil dari transaksi ini kemudian akan menyertakan komitmen (_komitmen_) dan secara implisit mengasosiasikan kepemilikan kontrak baru dengan Bob.

![RGB-Bitcoin](assets/fr/059.webp)

**Pembangunan properti baru (*Negara Bagian Baru*) :**

Bob mengirimkan informasi kepada Alice yang dikodekan dalam bentuk ***invoice*** (kita akan membahas lebih detail tentang konstruksi invoice di bab selanjutnya), memintanya untuk membuat state baru yang sesuai dengan aturan kontrak. State ini akan menyertakan *definisi segel* baru yang menunjuk ke salah satu UTXO milik Bob. Dengan cara ini, Bob diberikan kepemilikan atas aset yang didefinisikan dalam state baru ini, misalnya sejumlah token RGB.

![RGB-Bitcoin](assets/fr/060.webp)

**Persiapan transaksi sampel:**

Alice kemudian membuat sebuah transaksi Bitcoin dengan menggunakan UTXO yang dirujuk pada segel sebelumnya (segel yang melegitimasinya sebagai pemegang). Pada output dari transaksi ini, sebuah *komitmen* (melalui `Opret` atau `Tapret`) disisipkan untuk mengaitkan status RGB yang baru. Komitmen `Opret` atau `Tapret` berasal dari sebuah *MPC tree* (seperti yang terlihat pada bab-bab sebelumnya), yang dapat menggabungkan beberapa transisi dari kontrak yang berbeda.

**Pengiriman *Konsinyasi* ke Bob:**

Sebelum menyiarkan transaksi, Alice mengirimi Bob sebuah ***Konsinyasi*** yang berisi semua data *sisi-klien* yang diperlukan (simpanannya) dan informasi status baru yang menguntungkan Bob. Pada titik ini, Bob menerapkan aturan konsensus RGB:


- Ini memvalidasi semua data RGB yang terkandung dalam *Consignment*, termasuk negara bagian baru yang memberinya kepemilikan atas aset tersebut;
- Mengandalkan *Anchors* yang termasuk dalam *Consignment*, ini memverifikasi kronologi transaksi saksi (dari Genesis hingga transisi terbaru) dan memvalidasi komitmen yang sesuai dalam blockchain.

**Penyelesaian transisi:**

Jika Bob puas, dia dapat memberikan persetujuannya (misalnya, dengan menandatangani *konsinyasi*). Alice kemudian dapat menyiarkan transaksi sampel yang telah disiapkan. Setelah dikonfirmasi, hal ini akan menutup segel yang sebelumnya dipegang oleh Alice dan meresmikan kepemilikan oleh Bob. Keamanan anti-pembelanjaan ganda kemudian didasarkan pada mekanisme yang sama seperti pada Bitcoin: UTXO dibelanjakan, membuktikan bahwa Alice tidak dapat lagi menggunakannya kembali.

![RGB-Bitcoin](assets/fr/061.webp)

Status baru sekarang merujuk pada UTXO milik Bob, memberikan Bob kepemilikan yang sebelumnya dipegang oleh Alice. Keluaran Bitcoin di mana data RGB ditambatkan menjadi bukti yang tidak dapat dibatalkan dari transfer kepemilikan.

Sebuah contoh DAG minimal (*Directed Acyclic Graph*) yang terdiri dari dua operasi kontrak (**Genesis** kemudian ***State Transition***) dapat mengilustrasikan bagaimana state RGB (*lapisan sisi-klien, berwarna merah) terhubung ke blockchain Bitcoin (*lapisan Komitmen, berwarna oranye).

![RGB-Bitcoin](assets/fr/062.webp)

Ini menunjukkan bahwa sebuah Genesis mendefinisikan sebuah seal (*seal definition*), kemudian sebuah *State Transition* menutup seal ini untuk membuat seal baru di UTXO lain.

Dalam konteks ini, berikut ini beberapa pengingat terminologi:


- Sebuah ***Penugasan*** menggabungkan :
    - Definisi Segel*** (yang menunjuk ke UTXO);
    - Status Kepemilikan**, yaitu data yang terkait dengan kepemilikan (misalnya, jumlah token yang ditransfer).
- Sebuah **Negara Global** menyatukan sifat-sifat umum dari kontrak, yang dapat dilihat oleh semua orang, dan memastikan konsistensi evolusi global.

State Transition**, yang dijelaskan pada bab sebelumnya, adalah bentuk utama operasi kontrak. Mereka mengacu pada satu atau lebih state sebelumnya (dari Genesis atau State Transition lain) dan memperbaruinya ke state baru.

![RGB-Bitcoin](assets/fr/063.webp)

Diagram ini menunjukkan bagaimana, dalam *State Transition Bundle*, beberapa segel dapat ditutup dalam satu transaksi sampel, sementara secara bersamaan membuka segel baru. Memang, fitur yang menarik dari protokol RGB adalah kemampuannya untuk menskalakan: beberapa transisi dapat digabungkan ke dalam Transition Bundle, setiap agregasi dikaitkan dengan daun yang berbeda dari pohon *MPC* (pengenal bundel yang unik). Berkat mekanisme *Deterministic Bitcoin Commitment* (DBC), seluruh pesan dimasukkan ke dalam output `Tapret` atau `Opret`, sambil menutup segel sebelumnya dan mungkin mendefinisikan segel baru. Jangkar (Anchor) berfungsi sebagai penghubung langsung antara komitmen yang tersimpan dalam blockchain dan struktur validasi sisi klien (*client-side).

Pada bab-bab berikutnya, kita akan melihat semua komponen dan proses yang terlibat dalam membangun dan memvalidasi State Transition. Sebagian besar elemen ini merupakan bagian dari konsensus RGB, yang diimplementasikan dalam **RGB Core Library**.

### Bundel Transisi

Pada RGB, dimungkinkan untuk menggabungkan beberapa State Transition yang berbeda yang termasuk dalam kontrak yang sama (yaitu berbagi **ContractId** yang sama, yang berasal dari **OpId** Genesis). Dalam kasus yang paling sederhana, seperti antara Alice dan Bob pada contoh di atas, sebuah **Transition Bundle** hanya berisi satu transisi. Tetapi dukungan untuk operasi multi-pemain (seperti coinjoin, pembukaan saluran Lightning, dll.) Berarti bahwa beberapa pengguna dapat menggabungkan State Transitions mereka dalam satu bundel.

Setelah terkumpul, transisi ini ditambatkan (dengan mekanisme MPC + DBC) dalam satu transaksi Bitcoin:


- Setiap Transisi Negara di-hash dan dikelompokkan ke dalam Bundel Transisi;
- Bundel Transisi itu sendiri di-hash dan dimasukkan ke dalam daun pohon MPC yang sesuai dengan kontrak ini (BundleId);
- Pohon MPC akhirnya dilibatkan melalui `Opret` atau `Tapret` dalam transaksi saksi, yang dengan demikian menutup segel yang dikonsumsi dan mendefinisikan segel baru.

Secara teknis, **BundleId** yang disisipkan dalam lembar MPC diperoleh dari hash yang ditandai yang diterapkan pada serialisasi ketat bidang *InputMap* bundel:

```txt
BundleId = SHA256( SHA256(bundle_tag) || SHA256(bundle_tag) || InputMap )
```

Di mana `bundle_tag = urn:lnp-bp:rgb:bundle#2024-02-03` sebagai contoh.

*InputMap* adalah struktur data yang berisi daftar, untuk setiap input `i` dari contoh transaksi, referensi ke *OpId* dari State Transition yang sesuai. Sebagai contoh:

```txt
InputMap =
N               input_0    OpId(input_0)    input_1    OpId(input_1)   ...    input_N-1  OpId(input_N-1)
|____________________| |_________||______________| |_________||______________|       |__________||_______________|
16-bit Little Endian   32-bit LE   32-byte hash
|_________________________| |_________________________|  ...  |___________________________|
MapElement1                MapElement2                       MapElementN
```


- `N` adalah jumlah total entri dalam transaksi yang merujuk pada `OpId`;
- opId(input_j)` adalah pengenal operasi dari salah satu State Transition yang ada di dalam bundel.

Dengan mereferensikan setiap entri hanya satu kali dan dengan cara yang teratur, kami mencegah segel yang sama digunakan dua kali dalam dua State Transition secara bersamaan.

### Pembuatan Status dan Status Aktif

Oleh karena itu, State Transitions dapat digunakan untuk mentransfer kepemilikan aset dari satu orang ke orang lain. Namun, mereka bukan satu-satunya operasi yang memungkinkan dalam protokol RGB. Protokol ini mendefinisikan tiga **Operasi Kontrak**:


- Transisi Negara** ;
- Kejadian** ;
- Perpanjangan Negara**.

Di antaranya, **Genesis** dan **State Extension** kadang-kadang disebut "*Operasi Pembuatan State*", karena mereka membuat state baru tanpa langsung menutup state yang lain. Ini adalah poin yang sangat penting: **Genesis** dan **State Extension** tidak melibatkan penutupan segel. Melainkan, mereka mendefinisikan sebuah segel baru, yang kemudian harus dihabiskan oleh **Transisi Negara** berikutnya untuk benar-benar divalidasi dalam sejarah blockchain.

![RGB-Bitcoin](assets/fr/064.webp)

Status **Active State** dari sebuah kontrak sering kali didefinisikan sebagai sekumpulan status terbaru yang dihasilkan dari riwayat (DAG) transaksi, dimulai dari Genesis dan mengikuti semua jangkar dalam blockchain Bitcoin. Status lama yang sudah tidak aktif (yaitu yang melekat pada UTXO yang sudah habis) tidak lagi dianggap aktif, tetapi tetap penting untuk memeriksa konsistensi riwayat.

### Kejadian

Genesis adalah titik awal dari setiap kontrak RGB. Genesis dibuat oleh penerbit kontrak dan mendefinisikan parameter awal, sesuai dengan **Skema**. Dalam kasus token RGB, Genesis dapat menentukan, misalnya :


- Jumlah token yang awalnya dibuat dan pemiliknya;
- Total plafon masalah yang mungkin terjadi;
- Aturan penerbitan ulang, dan peserta mana saja yang memenuhi syarat.

Sebagai transaksi pertama dalam kontrak, Genesis tidak merujuk pada state sebelumnya, dan juga tidak menutup segel apa pun. Namun, untuk muncul dalam riwayat dan divalidasi, Genesis harus **dikonsumsi** (ditutup) oleh State Transition pertama (sering kali merupakan transaksi pemindaian/pembelanjaan otomatis ke penerbit itu sendiri, atau distribusi awal ke pengguna).

### Perpanjangan Negara Bagian

State Extensions** menawarkan sebuah fitur orisinil untuk smart contract. Mereka memungkinkan untuk menukarkan hak digital tertentu (*Valensi*) yang disediakan dalam definisi kontrak, tanpa segera menutup segel. Paling sering, hal ini menyangkut :


- Masalah token yang didistribusikan;
- Mekanisme pertukaran aset ;
- Penerbitan ulang bersyarat (yang mungkin termasuk penghancuran aset lain, dll.).

Secara teknis, State Extension mereferensikan *Redeem* (jenis input RGB tertentu) yang sesuai dengan *Valency* yang didefinisikan sebelumnya (misalnya, dalam Genesis atau State Transition lainnya). Ini mendefinisikan segel baru, tersedia untuk orang atau kondisi yang mendapatkan manfaat darinya. Agar segel ini menjadi efektif, segel ini harus dihabiskan oleh State Transition berikutnya.

![RGB-Bitcoin](assets/fr/065.webp)

Sebagai contoh: Genesis menciptakan hak penerbitan (*Valency*). Ini dapat dilakukan oleh aktor yang berwenang, yang kemudian membangun Ekstensi Negara :


- Ini mengacu pada Valensi (menebus);
- Ini menciptakan *penugasan* baru (data *Negara Bagian* baru) yang menunjuk ke UTXO;
- Transisi Negara di masa depan, yang dikeluarkan oleh pemilik UTXO baru ini, akan benar-benar mentransfer atau mendistribusikan token yang baru diterbitkan.

### Komponen Operasi Kontrak

Sekarang saya ingin melihat secara rinci setiap elemen penyusun **Operasi Kontrak** di RGB. Operasi Kontrak adalah tindakan yang memodifikasi status kontrak, dan yang divalidasi di sisi klien, dengan cara deterministik, oleh penerima yang sah. Secara khusus, kita akan melihat bagaimana Operasi Kontrak memperhitungkan, di satu sisi, **keadaan lama** (*Keadaan Lama*) dari kontrak, dan di sisi lain, definisi **keadaan baru** (*Keadaan Baru*).

```txt
+---------------------------------------------------------------------------------------------------------------------+
|  Contract Operation                                                                                                 |
|                                                                                                                     |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|  | Ffv |     | ContractId | SchemaId |      | TransitionType | ExtensionType |      | Testnet |     | AltLayers1 |  |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Metadata                                      |  | Global State                                               |  |
|  |                                               |  | +----------------------------------+                       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  | |          Structured Data            |       |  | | |  GlobalStateType  | |  Data  | |     ...     ...       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  |                                               |  | +----------------------------------+                       |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|                                                                                                                     +---------> OpId |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|  | Inputs                                        |  | Assignments                                                |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #1                                  | |  | | Assignment #1                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ + ---------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #2                                  | |  | | Assignment #2                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  |       ...           ...          ...          |  |     ...          ...             ...                       |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Redeems                                       |  | Valencies                                                  |  |
|  |                                               |  |                                                            |  |
|  | +------------------------------+              |  |                                                            |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
| OpId +--------------> PrevOpId | | ValencyType | |  ...   ...   |  |  | ValencyType |  | ValencyType |         ...              |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
|  | +------------------------------+              |  |                                                            |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------+
```

Jika kita melihat diagram di atas, kita dapat melihat bahwa Operasi Kontrak mencakup elemen-elemen yang mengacu pada **New State** dan elemen-elemen lain yang mengacu pada **Old State** yang telah diperbarui.

Elemen-elemen dari **Negara Baru** adalah :


- Penugasan**, yang di dalamnya didefinisikan :
 - Definisi Segel **Definisi Segel**;
 - Negara yang Dimiliki**.
- Status **Global**, yang dapat dimodifikasi atau diperkaya;
- Valuta**, mungkin didefinisikan dalam Transisi Negara atau Kejadian.

Status **Lama** direferensikan melalui :


- Input**, yang menunjuk ke *Penugasan* dari transisi status sebelumnya (tidak ada di Genesis);
- Penukaran**, yang mengacu pada Valuta yang telah ditentukan sebelumnya (hanya dalam Ekstensi Negara).

Selain itu, Operasi Kontrak mencakup bidang-bidang yang lebih umum yang spesifik untuk operasi tersebut:


- ffv` (*Versi maju cepat*): bilangan bulat 2-byte yang menunjukkan versi kontrak;
- transitionType` atau ExtensionType`: bilangan bulat 16-bit yang menentukan jenis Transisi atau Ekstensi, sesuai dengan logika bisnis;
- `ContractId`: nomor 32-byte yang mengacu pada *OpId* dari Genesis kontrak. Termasuk dalam Transisi dan Ekstensi, tetapi tidak dalam Genesis ;
- schemaId: hanya ada di Genesis, ini adalah hash 32-byte yang mewakili struktur (*Skema*) kontrak;
- testnet`: Boolean yang menunjukkan apakah Anda berada di jaringan Testnet atau Mainnet. Hanya untuk kejadian;
- altlayers1`: variabel yang mengidentifikasi lapisan alternatif (sidechain atau lainnya) yang digunakan untuk menambatkan data selain Bitcoin. Hanya ada di Genesis ;
- metadata": bidang yang dapat menyimpan informasi sementara, berguna untuk memvalidasi kontrak yang kompleks, tetapi tidak boleh dicatat dalam riwayat status akhir.

Terakhir, semua bidang ini dipadatkan dengan proses hashing yang disesuaikan, untuk menghasilkan sidik jari yang unik, yaitu `OpId`. OpId ini kemudian diintegrasikan ke dalam Transition Bundle, sehingga memungkinkannya untuk diautentikasi dan divalidasi di dalam protokol.

Oleh karena itu, setiap *Operasi Kontrak* diidentifikasi dengan hash 32-byte bernama `OpId`. Hash ini dihitung dengan hash SHA256 dari semua elemen yang membentuk operasi. Dengan kata lain, setiap *Contract Operation* memiliki komitmen kriptografinya sendiri, yang mencakup semua data yang diperlukan untuk memverifikasi keaslian dan konsistensi operasi.

Kontrak RGB kemudian diidentifikasi oleh `ContractId`, yang berasal dari Genesis `OpId` (karena tidak ada operasi pra-Genesis). Secara konkret, kita mengambil Genesis `OpId`, membalik urutan byte dan menerapkan pengkodean Base58. Pengkodean ini membuat `ContractId` lebih mudah ditangani dan dikenali.

### Metode dan aturan pembaruan status

Status Kontrak** mewakili sekumpulan informasi yang harus dilacak oleh protokol RGB untuk kontrak tertentu. Ini terdiri dari :


- Satu Global State**: ini adalah bagian global yang bersifat publik dan dapat dilihat oleh semua orang;
- Satu atau lebih Owned State**: setiap Owned State dikaitkan dengan segel unik (dan oleh karena itu merupakan UTXO pada Bitcoin). Perbedaan dibuat antara :
    - Negara-negara yang dimiliki oleh publik,
    - Negara yang Dimiliki oleh **swasta**.

![RGB-Bitcoin](assets/fr/066.webp)

Negara Bagian Global* secara langsung disertakan dalam *Operasi Kontrak* sebagai satu blok. Negara Bagian yang Dimiliki* didefinisikan dalam setiap *Penugasan*, di samping *Definisi Segel*.

Fitur utama RGB adalah cara di mana Status Global dan Status Milik dimodifikasi. Pada umumnya ada dua jenis perilaku:


- Dapat berubah**: ketika sebuah elemen state dideskripsikan sebagai dapat berubah, setiap operasi baru akan menggantikan state sebelumnya dengan state yang baru. Data lama kemudian dianggap usang;
- Akumulasi**: ketika elemen status didefinisikan sebagai akumulasi, setiap operasi baru menambahkan informasi baru ke status sebelumnya, tanpa menimpanya. Hasilnya adalah semacam akumulasi sejarah.

Jika, dalam kontrak, sebuah elemen state tidak didefinisikan sebagai dapat diubah atau kumulatif, elemen ini akan tetap kosong untuk operasi selanjutnya (dengan kata lain, tidak ada versi baru untuk bidang ini). Skema kontrak (yaitu logika bisnis yang dikodekan) yang menentukan apakah sebuah state (Global atau Owned) dapat berubah, kumulatif, atau tetap. Setelah Genesis didefinisikan, properti ini hanya dapat dimodifikasi jika kontrak itu sendiri mengizinkannya, misalnya melalui State Extension tertentu.

Tabel di bawah ini mengilustrasikan bagaimana setiap jenis Operasi Kontrak dapat memanipulasi (atau tidak) Global State dan Owned State:

| Kejadian | Perpanjangan Status | Transisi Status |

| ---------------------------- | :-----: | :-------------: | :--------------: |

| **Tambahkan Status Global** | + | - | + |

| n/a | - | + | **Mutasi Status Global** | - | + |

| **Tambahkan Negara Bagian Milik** | + | - | + |

| **Mutasi Status Kepemilikan** | n/a | Tidak | + |

| **Tambahkan Nilai** | + | + | + | + |

**`+`** : tindakan yang mungkin dilakukan jika Skema kontrak mengizinkannya.

**`-`**: operasi harus dikonfirmasi oleh Transisi Status berikutnya (Perpanjangan Status saja tidak menutup Segel Sekali Pakai).

Selain itu, cakupan temporal dan hak pembaruan setiap jenis data dapat dibedakan dalam tabel berikut:

| Metadata | Negara Global | Negara Milik

| ------------------------------- | ---------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |

| Ditetapkan untuk satu Operasi Kontrak | Ditetapkan secara global untuk kontrak | Ditetapkan untuk setiap segel (*Penugasan*) | Ditetapkan untuk satu Operasi Kontrak | Ditetapkan secara global untuk kontrak | Ditetapkan untuk setiap segel (*Penugasan*) | Ditetapkan untuk setiap segel (*Penugasan*) | Ditetapkan untuk setiap kontrak

| Tidak dapat diaktualisasikan (data sementara) | Transaksi yang dikeluarkan oleh aktor (penerbit, dll.) | Tergantung pada pemegang segel yang sah (orang yang dapat membelanjakannya dalam transaksi berikutnya)

status ditetapkan sebelum operasi (oleh *Seal Definition* dari operasi sebelumnya) | Status ditetapkan di akhir operasi | Status ditetapkan di akhir operasi | Status ditetapkan di akhir operasi | Status ditetapkan sebelum operasi (oleh *Seal Definition* dari operasi sebelumnya) | Status ditetapkan di akhir operasi | Status ditetapkan sebelum operasi (oleh *Seal Definition* dari operasi sebelumnya)

### Status Global

Global State sering digambarkan sebagai "tidak ada yang memiliki, semua orang tahu". Ini berisi informasi umum tentang kontrak, yang dapat dilihat oleh publik. Sebagai contoh, dalam kontrak penerbitan token, ini berpotensi berisi :


- Ticker (singkatan simbolis dari token): `ticker` ;
- Nama lengkap token: `nama` ;
- Presisi (jumlah tempat desimal): `precision` ;
- Penawaran awal (dan/atau batas maksimum token): `issuedSupply` ;
- Tanggal penerbitan: `dibuat` ;
- Data hukum atau informasi publik lainnya: `data`.

Global State ini dapat ditempatkan pada sumber daya publik (situs web, IPFS, Nostr, Torrent, dll.) dan didistribusikan ke komunitas. Selain itu, insentif ekonomi (kebutuhan untuk menyimpan dan mentransfer token ini, dll.) secara alami mendorong pengguna kontrak untuk memelihara dan menyebarkan data ini sendiri.

### Penugasan

The *Assignment* adalah struktur dasar untuk mendefinisikan :


- Segel (*Definisi Segel*), yang menunjuk ke UTXO tertentu;
- Status *Milik*, yaitu properti atau data yang terkait dengan segel ini.

Sebuah *Assignment* dapat dilihat sebagai analog dari hasil transaksi Bitcoin, namun dengan fleksibilitas yang lebih tinggi. Di sinilah letak logika transfer properti: *Assignment* mengasosiasikan jenis aset atau hak tertentu (`AssignmentType`) dengan segel. Siapa pun yang memiliki kunci pribadi UTXO yang terhubung dengan segel ini (atau siapa pun yang dapat membelanjakan UTXO ini) dianggap sebagai pemilik dari *State Milik* ini.

Salah satu kekuatan besar RGB terletak pada kemampuannya untuk menyingkap (*reveal*) atau menyembunyikan (*conceal*) bidang *Seal Definition* dan *Owned State* sesuka hati. Hal ini menawarkan kombinasi yang kuat antara kerahasiaan dan selektivitas. Sebagai contoh, Anda dapat membuktikan bahwa sebuah transisi valid tanpa mengungkapkan semua data, dengan memberikan versi yang terungkap kepada orang yang harus memvalidasinya, sementara pihak ketiga hanya melihat versi tersembunyi (hash). Dalam praktiknya, `OpId` dari sebuah transisi selalu dihitung dari data yang *disembunyikan.

![RGB-Bitcoin](assets/fr/067.webp)

#### Definisi Segel

Definisi Segel, dalam bentuknya yang terungkap, memiliki empat bidang dasar: `txptr`, `vout`, `blinding` dan `method` :


- txptr**: ini adalah referensi ke UTXO pada Bitcoin:
    - Dalam kasus **Segel Genesis**, segel ini menunjuk langsung ke UTXO yang ada (yang terkait dengan Genesis);
    - Dalam kasus **Graph seal**, kita dapat memiliki :
        - Sebuah `txid` sederhana, jika menunjuk ke UTXO tertentu,
        - Atau `WitnessTx`, yang menunjukkan referensi mandiri: segel menunjuk ke transaksi itu sendiri. Ini sangat berguna ketika tidak ada UTXO eksternal yang tersedia, misalnya dalam transaksi pembukaan saluran Lightning, atau jika penerima tidak memiliki UTXO.
- vout** : nomor keluaran dari transaksi yang ditunjukkan oleh `txptr`. Hanya ada untuk segel Graph standar (bukan untuk `WitnessTx`);
- blinding**: angka acak 8 byte, untuk memperkuat kerahasiaan dan mencegah upaya brute force pada identitas UTXO;
- method** : menunjukkan metode penahan yang digunakan (`Tapret` atau `Opret`).

Bentuk *disembunyikan* dari Definisi Segel adalah hash SHA256 (ditandai) dari gabungan 4 bidang ini, dengan tag khusus untuk RGB.

![RGB-Bitcoin](assets/fr/068.webp)

#### Negara Bagian yang Dimiliki

Komponen kedua dari *Penugasan* adalah Status Milik. Tidak seperti Global State, ini bisa ada dalam bentuk publik atau privat:


- Negara Milik Publik**: semua orang mengetahui data yang terkait dengan segel. Misalnya, gambar publik;
- Status Milik Pribadi**: data disembunyikan, hanya diketahui oleh pemiliknya (dan mungkin validator jika diperlukan). Misalnya, jumlah token yang dimiliki.

RGB mendefinisikan empat jenis status yang mungkin (*StateTypes*) untuk Status Milik:


- Deklaratif**: tidak berisi data numerik, hanya hak deklaratif (misalnya hak untuk memilih). Bentuk yang tersembunyi dan yang terungkap adalah identik;
- Fungible**: mewakili kuantitas yang dapat dipertukarkan (seperti token). Dalam bentuk terbuka, kita memiliki `jumlah` dan `kebodohan`. Dalam bentuk tersembunyi, kita memiliki satu *komitmen Pedersen* yang menyembunyikan jumlah dan blinding;
- Terstruktur**: menyimpan data terstruktur (hingga 64 kB). Dalam bentuk yang terlihat, ini adalah gumpalan data. Dalam bentuk tersembunyi, ini adalah hash yang ditandai dari gumpalan ini:

```txt
SHA-256(SHA-256(tag_data) || SHA-256(tag_data) || blob)
```

Dengan, misalnya :

```txt
tag_data = urn:lnp-bp:rgb:state-data#2024-02-12
```


- Lampiran**: menautkan berkas (audio, gambar, biner, dll.) ke Status Milik, menyimpan hash berkas `file_hash`, tipe MIME `tipe media` dan garam kriptografi `salt`. File itu sendiri dihosting di tempat lain. Dalam bentuk tersembunyi, file tersebut merupakan hash yang ditandai dengan tiga item data sebelumnya:

```txt
SHA-256(SHA-256(tag_attachment) || SHA-256(tag_attachment) || file_hash || media_type || salt)
```

Dengan, misalnya :

```txt
tag_attachment = urn:rgb:state-attach#2024-02-12
```

Sebagai rangkuman, berikut ini adalah 4 jenis negara yang mungkin dalam bentuk publik dan tersembunyi:

```txt
State                      Concealed form                              Revealed form
+---------------------------------------------------------------------------------------------------------
+--------------------------------------------------------------------------------+
|                                                                                |
Declarative        |                              < void >                                          |
|                                                                                |
+--------------------------------------------------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------+ +----------+       |
Fungible           | | Pedersen Commitement | | <========== |         | Amount | | Blinding |       |
| +----------------------+ |             |         +--------+ +----------+       |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------------------+        |
Structured         | |     Tagged Hash      | | <========== |         |     Data Blob      |        |
| +----------------------+ |             |         +--------------------+        |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             | +-----------+ +------------+ +------+ |
Attachments        | |     Tagged Hash      | | <========== | | File Hash | | Media Type | | Salt | |
| +----------------------+ |             | +-----------+ +------------+ +------+ |
+--------------------------+             +---------------------------------------+
```

**Deklaratif** | **Bisa Dipadukan** | **Terstruktur** | **Lampiran** |

| --------------------- | -------------- | ------------------------------------ | ----------------------------- | ---------------------------- |

| Tidak ada | Bilangan bulat bertanda tangan atau tidak bertanda tangan 64-bit | Semua tipe data yang ketat | File apa pun |

| Jenis informasi** | Tidak ada | Tidak ada | Ditandatangani atau tidak ditandatangani | Jenis ketat | Jenis MIME

| Komitmen Pedersen | Hashing dengan membutakan | ID file ter-hash

| Batas ukuran** | N/A | 256 byte | Hingga 64 KB | Hingga ~500 Gb |

### Masukan

Input dari *Operasi Kontrak* mengacu pada *Penugasan* yang digunakan dalam operasi baru ini. Sebuah Input menunjukkan :


- prevOpId` : pengenal (`OpId`) dari operasi sebelumnya di mana *Penugasan* berada;
- assignmentType` : jenis *Assignment* (misalnya, `assetOwner` untuk sebuah token);
- `Indeks`: indeks dari *Penugasan* dalam daftar yang terkait dengan `OpId` sebelumnya, yang ditentukan setelah pengurutan leksikografi dari segel tersembunyi.

Input tidak pernah muncul di Genesis, karena tidak ada Assignment sebelumnya. Mereka juga tidak muncul di State Extensions (karena State Extensions tidak menutup segel; melainkan mendefinisikan ulang segel baru berdasarkan Valensi).

Ketika kita memiliki Status Milik dengan tipe `Fungible`, logika validasi (melalui skrip AluVM yang disediakan di Skema) memeriksa konsistensi jumlah: jumlah token yang masuk (*Input*) harus sama dengan jumlah token yang keluar (di *Assignment* yang baru).

### Metadata

Bidang **Metadata** dapat berukuran hingga 64 KiB dan digunakan untuk menyertakan data sementara yang berguna untuk validasi, tetapi tidak diintegrasikan ke dalam kondisi permanen kontrak. Sebagai contoh, variabel perhitungan perantara untuk skrip yang kompleks dapat disimpan di sini. Ruang ini tidak dimaksudkan untuk disimpan dalam riwayat global, oleh karena itu ruang ini berada di luar cakupan Status Milik atau Status Global.

### Valuta

Valensi** adalah mekanisme protokol RGB asli. Mereka dapat ditemukan di Genesis, State Transitions atau State Extensions. Mereka mewakili hak numerik yang dapat diaktifkan oleh State Extension (melalui *Redeems*), kemudian diselesaikan oleh Transisi berikutnya. Setiap Valensi diidentifikasi oleh `ValencyType` (16 bit). Semantiknya (hak penerbitan ulang, pertukaran token, hak bakar, dll.) didefinisikan dalam Skema.

Secara konkret, kita dapat membayangkan sebuah Genesis yang mendefinisikan valensi "hak untuk menerbitkan kembali". Sebuah State Extension akan mengkonsumsinya (*Redeem*) jika kondisi tertentu terpenuhi, untuk memperkenalkan jumlah token yang baru. Kemudian, sebuah State Transition yang berasal dari pemegang segel yang telah dibuat dapat mentransfer token-token baru ini.

### Menebus

Penebusan adalah Valensi yang setara dengan Input untuk Penugasan. Mereka hanya muncul di State Extensions, karena di sinilah Valensi yang telah didefinisikan sebelumnya diaktifkan. Penukaran terdiri dari dua bidang:


- `PrevOpId`: `OpId` dari operasi di mana Valensi ditentukan;
- `ValencyType`: jenis Valensi yang ingin Anda aktifkan (setiap `ValencyType` hanya dapat digunakan satu kali oleh State Extension).

Contoh: Penukaran dapat berhubungan dengan eksekusi CoinSwap, tergantung pada apa yang dikodekan dalam Valuta.

### Karakteristik status RGB

Sekarang, kita akan mencermati beberapa karakteristik keadaan mendasar dalam RGB. Khususnya, kita akan mencermati :


- Sistem Ketik Ketat**, yang menerapkan pengaturan data yang tepat dan diketik;
- Pentingnya memisahkan **validasi** dari **kepemilikan**;
- Sistem **evolusi konsensus** dalam RGB, yang mencakup gagasan *cepat-maju* dan *mundur-mundur*.

Seperti biasa, ingatlah bahwa segala sesuatu yang berkaitan dengan status kontrak divalidasi di sisi klien sesuai dengan aturan konsensus yang ditetapkan dalam protokol, dan referensi kriptografi utamanya berlabuh pada transaksi Bitcoin.

#### Sistem Tipe yang Ketat

RGB menggunakan *System Tipe Ketat* dan mode serialisasi deterministik (*Strict Encoding*). Organisasi ini dirancang untuk menjamin reproduktifitas dan presisi yang sempurna dalam definisi, penanganan, dan validasi data kontrak.

Di banyak lingkungan pemrograman (JSON, YAML...), struktur data dapat menjadi fleksibel, bahkan terlalu permisif. Di RGB, di sisi lain, Struktur dan Jenis setiap bidang didefinisikan dengan batasan eksplisit. Sebagai contoh :


- Setiap variabel memiliki tipe tertentu (misalnya, bilangan bulat 8-bit tidak bertanda `u8`, atau bilangan bulat bertanda 16-bit, dll.);
- Tipe dapat disusun (tipe bersarang). Ini berarti Anda dapat mendefinisikan sebuah tipe berdasarkan tipe lain (misalnya, tipe agregat yang berisi field `u8`, field `bool`, dll.);
- Koleksi juga dapat ditentukan: daftar (*list*), set (*set*) atau kamus (*map*), dengan urutan perkembangan yang deterministik;
- Setiap bidang dibatasi (*batas bawah* / *batas atas*). Kami juga memberikan batasan pada jumlah elemen dalam koleksi (penahanan);
- Data disejajarkan secara byte dan serialisasi didefinisikan secara ketat dan tidak ambigu.

Berkat protokol penyandian yang ketat ini:


- Urutan bidang selalu sama, terlepas dari implementasi atau bahasa pemrograman yang digunakan;
- Oleh karena itu, hash yang dihitung pada set data yang sama dapat direproduksi dan identik (sangat deterministik *komitmen*);
- Batasan mencegah pertumbuhan ukuran data yang tidak terkendali (misalnya terlalu banyak field);
- Bentuk pengkodean ini memfasilitasi verifikasi kriptografi, karena setiap peserta tahu persis bagaimana cara menserialisasi dan meng-hash data.

Dalam praktiknya, struktur (*Skema*) dan kode yang dihasilkan (*Interface* dan logika terkait) dikompilasi. Bahasa deskriptif digunakan untuk mendefinisikan kontrak (jenis, bidang, aturan) dan menghasilkan format biner yang ketat. Ketika dikompilasi, hasilnya adalah :


- Tata Letak Memori untuk setiap bidang;
- Pengidentifikasi semantik (yang menunjukkan apakah mengubah nama variabel berdampak pada logika, meskipun struktur memori tetap sama).

Sistem tipe yang ketat juga memungkinkan pemantauan perubahan yang tepat: setiap modifikasi pada struktur (bahkan perubahan nama bidang) dapat dideteksi dan dapat menyebabkan perubahan pada jejak keseluruhan.

Terakhir, setiap kompilasi menghasilkan sidik jari, sebuah pengenal kriptografi yang membuktikan versi yang tepat dari kode (data, aturan, validasi). Sebagai contoh, pengenal dalam bentuk :

```txt
BEiLYE-am9WhTW1-oK8cpvw4-FEMtzMrf-mKocuGZn-qWK6YF#ginger-parking-nirvana
```

Hal ini memungkinkan untuk mengelola konsensus atau pembaruan implementasi, sekaligus memastikan penelusuran terperinci dari versi yang digunakan dalam jaringan.

Untuk mencegah keadaan kontrak RGB menjadi terlalu rumit untuk divalidasi di sisi klien, aturan konsensus memberlakukan ukuran maksimum `2^16` byte (64 Kio) untuk setiap data yang terlibat dalam perhitungan validasi. Hal ini berlaku untuk setiap variabel atau struktur: tidak lebih dari 65536 byte, atau yang setara dengan angka (32768 bilangan bulat 16-bit, dll.). Hal ini juga berlaku untuk koleksi (daftar, set, peta), yang tidak boleh melebihi elemen `2^16`.

Batas ini menjamin :


- Mengontrol ukuran maksimum data yang akan dimanipulasi selama transisi status;
- Kompatibilitas dengan mesin virtual (*AluVM*) yang digunakan untuk menjalankan skrip validasi.

#### Validasi!= Paradigma kepemilikan

Salah satu inovasi utama RGB adalah pemisahan yang tegas antara dua konsep:


- Validasi**: memeriksa apakah transisi keadaan mematuhi aturan kontrak (logika bisnis, riwayat, dll.);
- Kepemilikan (ownership): fakta kepemilikan Bitcoin UTXO yang memungkinkan Segel Sekali Pakai untuk digunakan (atau ditutup), dan dengan demikian transisi negara terjadi.

Validasi** terjadi pada tingkat tumpukan perangkat lunak RGB (pustaka, protokol *komitmen*, dll.). Perannya adalah untuk memastikan bahwa aturan internal kontrak (jumlah, izin, dll.) dihormati. Pengamat atau peserta lain juga dapat memvalidasi riwayat data.

Kepemilikan**, di sisi lain, sepenuhnya bergantung pada keamanan Bitcoin. Memiliki private key dari UTXO berarti mengendalikan kemampuan untuk meluncurkan transisi baru (menutup Segel Sekali Pakai). Jadi, meskipun seseorang dapat melihat atau memvalidasi data, mereka tidak dapat mengubah status jika mereka tidak memiliki UTXO yang bersangkutan.

![RGB-Bitcoin](assets/fr/069.webp)

Pendekatan ini membatasi kerentanan klasik yang ditemukan pada blockchain yang lebih kompleks (di mana semua kode smart contract bersifat publik dan dapat dimodifikasi oleh siapa saja, yang terkadang menyebabkan peretasan). Pada RGB, seorang penyerang tidak dapat dengan mudah berinteraksi dengan status on-chain, karena hak untuk bertindak atas status tersebut (*kepemilikan*) dilindungi oleh lapisan Bitcoin.

Terlebih lagi, pemisahan ini memungkinkan RGB untuk berintegrasi secara alami dengan Lightning Network. Saluran Lightning dapat digunakan untuk melibatkan dan memindahkan aset RGB tanpa melibatkan *komitmen* on-chain setiap saat. Kita akan melihat lebih dekat pada integrasi RGB pada Lightning ini di bab-bab selanjutnya dalam kursus ini.

#### Perkembangan konsensus dalam RGB

Selain versi kode semantik, RGB mencakup sistem untuk mengembangkan atau memperbarui aturan konsensus kontrak dari waktu ke waktu. Ada dua bentuk utama evolusi:


- Maju cepat**
- Dorong ke belakang** (dalam bahasa Prancis)

Kemajuan cepat terjadi ketika aturan yang sebelumnya tidak valid menjadi valid. Misalnya, jika kontrak berevolusi untuk mengizinkan jenis baru `TipePenugasan` atau bidang baru:


- Ini tidak dapat dibandingkan dengan hardfork blockchain klasik, karena RGB bekerja dalam validasi sisi klien dan tidak memengaruhi kompatibilitas blockchain secara keseluruhan;
- Dalam istilah praktis, jenis perubahan ini ditunjukkan oleh bidang `Ffv` (*fast-forward version*) dalam operasi kontrak;
- Pemegang saat ini tidak dirugikan: status mereka tetap berlaku;
- Di sisi lain, penerima baru (atau pengguna baru), perlu memperbarui perangkat lunak mereka (dompet mereka) untuk mengenali aturan baru.

Push-back berarti bahwa aturan yang sebelumnya valid menjadi tidak valid. Oleh karena itu, ini adalah "pengerasan" aturan, tetapi tidak sepenuhnya merupakan softfork:


- Pemegang yang sudah ada mungkin akan terkena dampak (mereka mungkin mendapati diri mereka dengan aset yang dianggap usang atau tidak valid dalam versi baru);
- Kita dapat menganggap bahwa kita sebenarnya sedang membuat protokol baru: siapa pun yang mengadopsi aturan baru akan meninggalkan aturan lama;
- Penerbit dapat memutuskan untuk menerbitkan kembali aset dalam protokol baru ini, memaksa pengguna untuk mempertahankan dua dompet terpisah (satu untuk protokol lama, satu lagi untuk protokol baru), jika mereka ingin mengelola kedua versi tersebut.

Dalam bab tentang operasi kontrak RGB ini, kita telah menjelajahi prinsip-prinsip dasar yang mendasari protokol ini. Seperti yang Anda ketahui, kompleksitas yang melekat pada protokol RGB memerlukan penggunaan banyak istilah teknis. Jadi, di bab berikutnya, saya akan memberi Anda daftar istilah yang akan merangkum semua konsep yang tercakup dalam bagian teori pertama ini, dengan definisi semua istilah teknis yang berkaitan dengan RGB. Kemudian, pada bagian berikutnya, kita akan melihat secara praktis pada definisi dan implementasi kontrak RGB.

## Daftar Istilah RGB

<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>

Jika Anda perlu kembali ke glosarium singkat tentang istilah teknis penting yang digunakan dalam dunia RGB (terdaftar dalam urutan abjad), Anda akan menemukannya berguna. Bab ini tidak penting jika Anda sudah memahami semua yang sudah kita bahas di bagian pertama.

#### AluVM

Singkatan AluVM adalah singkatan dari "_Algorithmic logic unit Virtual Machine_", sebuah mesin virtual berbasis register yang dirancang untuk validasi kontrak pintar dan komputasi terdistribusi. Mesin ini digunakan (tetapi tidak secara eksklusif disediakan) untuk validasi kontrak RGB. Skrip atau operasi yang termasuk dalam kontrak RGB dapat dieksekusi di lingkungan AluVM.

Untuk informasi lebih lanjut: [Situs web resmi AluVM](https://www.aluvm.org/)

#### Jangkar

Anchor mewakili sekumpulan data sisi klien yang digunakan untuk membuktikan penyertaan _commitment_ yang unik dalam sebuah transaksi. Dalam protokol RGB, Anchor terdiri dari elemen-elemen berikut:


- Pengidentifikasi transaksi Bitcoin (TXID) dari **transaksi saksi**;
- Komitmen Multi Protokol (MPC);
- Komitmen Bitcoin Deterministik (DBC) **;
- Bukti Transaksi Ekstra (ETP) jika mekanisme komitmen **Tapret** digunakan (lihat bagian yang didedikasikan untuk model ini).

Oleh karena itu, Anchor berfungsi untuk membuat hubungan yang dapat diverifikasi antara transaksi Bitcoin tertentu dengan data pribadi yang divalidasi oleh protokol RGB. Anchor menjamin bahwa data-data ini memang dimasukkan ke dalam blockchain, tanpa konten yang sebenarnya terekspos ke publik.

#### Penugasan

Dalam logika RGB, Penugasan setara dengan keluaran transaksi yang memodifikasi, memperbarui, atau membuat properti tertentu dalam status kontrak. Penugasan terdiri dari dua elemen:


- A **Definisi Segel** (referensi ke UTXO tertentu);
- Status **Milik** (data yang menjelaskan status yang terkait dengan pemilik baru ini).

Oleh karena itu, Penugasan menunjukkan bahwa sebagian negara (misalnya, aset) sekarang dialokasikan kepada pemegang tertentu, yang diidentifikasi melalui Segel Sekali Pakai yang ditautkan ke UTXO.

#### Logika Bisnis

Logika Bisnis mengelompokkan semua aturan dan operasi internal kontrak, yang dijelaskan oleh **skema** (yaitu struktur kontrak itu sendiri). Skema ini menentukan bagaimana keadaan kontrak dapat berkembang, dan dalam kondisi apa.

#### Validasi Sisi Klien

Validasi Sisi Klien mengacu pada proses di mana setiap pihak (klien) memverifikasi serangkaian data yang dipertukarkan secara pribadi, sesuai dengan aturan protokol. Dalam kasus RGB, data yang dipertukarkan ini dikelompokkan bersama dalam apa yang dikenal sebagai **kiriman**. Tidak seperti protokol Bitcoin, yang mengharuskan semua transaksi dipublikasikan secara on-chain, RGB hanya mengizinkan _commitment_ (berlabuh di Bitcoin) untuk disimpan di publik, sementara informasi kontrak yang penting (transisi, pengesahan, bukti) tetap berada di luar jaringan, hanya dibagikan di antara para pengguna yang bersangkutan.

#### Komitmen

Komitmen (dalam pengertian kriptografi) adalah sebuah objek matematika, dilambangkan dengan `C`, yang diturunkan secara deterministik dari sebuah operasi pada data terstruktur `m` (pesan) dan sebuah nilai acak `r`. Kami menulis :

$$
C = \text{commit}(m, r)
$$

Mekanisme ini terdiri dari dua operasi utama:


- Commit**: fungsi kriptografi diterapkan pada pesan `m` dan angka acak `r` untuk menghasilkan `C`;
- Verify**: kita menggunakan `C`, pesan `m`, dan nilai `r` untuk memeriksa apakah komitmen ini benar. Fungsi ini mengembalikan `True` atau `False`.

Sebuah komitmen harus menghormati dua sifat:


- Pengikatan**: tidak mungkin menemukan dua pesan berbeda yang menghasilkan `C` yang sama:

$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$

Seperti :

$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$


- Menyembunyikan**: pengetahuan tentang `C` tidak boleh mengungkapkan isi `m`.

Dalam protokol RGB, sebuah komitmen disertakan dalam transaksi Bitcoin untuk membuktikan keberadaan sebuah informasi tertentu pada waktu tertentu, tanpa mengungkapkan informasi itu sendiri.

#### Konsinyasi

Konsinyasi **Konsinyasi** mengelompokkan data yang dipertukarkan di antara kedua belah pihak, tunduk pada Validasi Sisi Klien di RGB. Ada dua kategori utama konsinyasi:


- Konsinyasi Kontrak**: disediakan oleh *issuer* (penerbit kontrak), ini mencakup informasi inisialisasi seperti Skema, Kejadian, Antarmuka, dan Implementasi Antarmuka.
- Konsinyasi Transfer**: disediakan oleh pihak yang membayar (*pembayar*). Ini berisi seluruh riwayat transisi status yang mengarah ke pengiriman terminal (yaitu status akhir yang diterima oleh pembayar).

Kiriman ini tidak dicatat secara publik di blockchain; mereka dipertukarkan secara langsung antara pihak-pihak yang bersangkutan melalui saluran komunikasi pilihan mereka.

#### Kontrak

Kontrak adalah seperangkat hak yang dieksekusi secara digital antara beberapa aktor melalui protokol RGB. Kontrak memiliki status aktif dan logika bisnis, yang ditentukan oleh Skema, yang menentukan operasi mana yang diotorisasi (transfer, ekstensi, dll.). Status kontrak, serta aturan validitasnya, dinyatakan dalam Skema. Pada waktu tertentu, kontrak berkembang hanya sesuai dengan apa yang diizinkan oleh Skema ini dan oleh skrip validasi (dijalankan, misalnya, di AluVM).

#### Operasi Kontrak

Operasi Kontrak adalah pembaruan status kontrak yang dilakukan sesuai dengan aturan Skema. Operasi-operasi berikut ini ada di RGB:


- Transisi Negara** ;
- Kejadian** ;
- Perpanjangan Negara**.

Setiap operasi memodifikasi status dengan menambahkan atau mengganti data tertentu (Status Global, Status Milik...).

#### Peserta Kontrak

Peserta Kontrak adalah aktor yang mengambil bagian dalam operasi yang berkaitan dengan kontrak. Dalam RGB, ada perbedaan antara :


- Penerbit kontrak, yang menciptakan Genesis (asal mula kontrak);
- Para pihak dalam kontrak, yaitu pemegang hak atas keadaan kontrak;
- Pihak publik, yang dapat membangun Ekstensi Negara jika kontrak menawarkan Mata Uang yang dapat diakses oleh publik.

#### Hak-hak Kontrak

Hak Kontrak mengacu pada berbagai hak yang dapat digunakan oleh mereka yang terlibat dalam kontrak RGB. Hak-hak tersebut terbagi dalam beberapa kategori:


- Hak kepemilikan**, terkait dengan kepemilikan UTXO tertentu (melalui _Definisi Segel_);
- Hak eksekutif**, yaitu kemampuan untuk membangun satu atau lebih transisi (Transisi Negara) sesuai dengan Skema ;
- Hak publik**, ketika Skema mengizinkan penggunaan publik tertentu, misalnya pembuatan Ekstensi Negara melalui penukaran Valuta.

#### Status Kontrak

Status Kontrak berhubungan dengan keadaan kontrak saat ini pada saat tertentu. Status kontrak dapat terdiri dari data publik dan privat, yang mencerminkan keadaan kontrak. RGB membedakan antara :


- Status **Global**, yang mencakup properti publik kontrak (diatur dalam Genesis atau ditambahkan melalui pembaruan resmi);
- Negara Milik**, yang dimiliki oleh pemilik tertentu, yang diidentifikasi oleh UTXO mereka.

#### Komitmen Bitcoin Deterministik - DBC

Deterministic Bitcoin Commitment (DBC) adalah seperangkat aturan yang digunakan untuk mendaftarkan sebuah _commitment_ dalam transaksi Bitcoin secara unik dan terbukti. Dalam protokol RGB, ada dua bentuk utama DBC:


- Opret**
- Tapret**

Mekanisme ini mendefinisikan dengan tepat bagaimana _komitmen_ dikodekan dalam output atau struktur transaksi Bitcoin, untuk memastikan bahwa komitmen ini dapat dilacak dan diverifikasi secara pasti.

#### Graf Akiklik Terarah - DAG

DAG (atau *Acyclic Guided Graph*) adalah sebuah graf bebas siklus, yang memungkinkan penjadwalan topologi. Blockchain, seperti pecahan kontrak RGB, dapat diwakili oleh DAG.

Untuk informasi lebih lanjut: [Graf Asiklik Berarah](https://en.wikipedia.org/wiki/Directed_acyclic_graph)

#### Ukiran

Pengukiran adalah string data opsional yang dapat dimasukkan oleh pemilik kontrak yang berurutan ke dalam riwayat kontrak. Fitur ini ada, misalnya, di antarmuka **RGB21** dan memungkinkan informasi peringatan atau deskriptif ditambahkan ke riwayat kontrak.

#### Bukti Transaksi Ekstra - ETP

ETP (*Extra Transaction Proof*) adalah bagian dari Anchor yang berisi data tambahan yang diperlukan untuk memvalidasi **Tapret** *commitment* (dalam konteks _taproot_). Ini termasuk, antara lain, kunci publik internal skrip taproot (_internal PubKey_) dan informasi khusus untuk _Script Path Spend_.

#### Kejadian

Genesis mengacu pada sekumpulan data, yang diatur oleh Skema, yang membentuk status awal dari setiap kontrak dalam RGB. Hal ini dapat dibandingkan dengan konsep _Genesis Block_ Bitcoin, atau dengan konsep transaksi Coinbase, tetapi di sini di tingkat _client-side_ dan token RGB.

#### Status Global

Global State adalah sekumpulan properti publik yang terdapat dalam Contract State. Hal ini didefinisikan di Genesis dan, tergantung pada aturan kontrak, dapat diperbarui dengan transisi yang sah. Tidak seperti Owned State, Global State bukan milik entitas tertentu; ini lebih dekat dengan registri publik dalam kontrak.

#### Antarmuka

Antarmuka adalah sekumpulan instruksi yang digunakan untuk memecahkan kode data biner yang dikompilasi dalam Skema atau dalam operasi kontrak dan statusnya, agar dapat dibaca oleh pengguna atau dompetnya. Ini bertindak sebagai lapisan interpretasi.

#### Implementasi Antarmuka

Implementasi Antarmuka adalah serangkaian deklarasi yang menghubungkan **Interface** ke **Skema**. Hal ini memungkinkan penerjemahan semantik yang dilakukan oleh Antarmuka itu sendiri, sehingga data mentah dari sebuah kontrak dapat dimengerti oleh pengguna atau perangkat lunak yang terlibat (dompet).

#### Faktur

Faktur berbentuk URL yang dikodekan dalam [base58] (https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58), yang menyematkan data yang diperlukan untuk pembuatan **Transisi Status** (oleh pembayar). Dengan kata lain, faktur ini memungkinkan rekanan (*pembayar*) untuk membuat transisi yang sesuai untuk mentransfer aset atau memperbarui status kontrak.

#### Jaringan Petir

Lightning Network adalah sebuah jaringan terdesentralisasi dari saluran pembayaran (atau _state channels_) pada Bitcoin, yang terdiri dari 2/2 dompet multi tanda tangan. Jaringan ini memungkinkan transaksi _off-chain_ yang cepat dan berbiaya rendah, dengan tetap mengandalkan Layer 1 Bitcoin untuk arbitrase (atau penutupan) jika diperlukan.

Untuk informasi lebih lanjut mengenai cara kerja Lightning, saya sarankan Anda mengikuti kursus lainnya:

https://planb.network/courses/lnp201
#### Komitmen Multi Protokol - MPC

Multi Protocol Commitment (MPC) mengacu pada struktur pohon Merkle yang digunakan dalam RGB untuk menyertakan, dalam satu transaksi Bitcoin, beberapa **Transition Bundle** dari kontrak yang berbeda. Idenya adalah untuk mengelompokkan beberapa komitmen (yang mungkin berhubungan dengan kontrak yang berbeda atau aset yang berbeda) dalam satu titik jangkar untuk mengoptimalkan penggunaan ruang blok.

#### Negara Bagian yang Dimiliki

Status Milik adalah bagian dari Status Kontrak yang dilampirkan dalam Penugasan dan terkait dengan pemegang tertentu (melalui Segel Sekali Pakai yang menunjuk ke UTXO). Ini mewakili, misalnya, aset digital atau hak kontrak tertentu yang diberikan kepada orang tersebut.

#### Kepemilikan

Kepemilikan mengacu pada kemampuan untuk mengontrol dan membelanjakan UTXO yang dirujuk oleh Definisi Segel. Ketika Status Milik dikaitkan dengan UTXO, pemilik UTXO ini memiliki hak, secara potensial, untuk mentransfer atau mengembangkan status terkait, sesuai dengan aturan kontrak.

#### Transaksi Bitcoin yang Ditandatangani Sebagian - PSBT

PSBT (_Partially Signed Bitcoin Transaction_) adalah sebuah transaksi Bitcoin yang belum sepenuhnya ditandatangani. Transaksi ini dapat dibagi di antara beberapa entitas, yang masing-masing dapat menambahkan atau memverifikasi elemen tertentu (tanda tangan, skrip...), hingga transaksi dianggap siap untuk didistribusikan secara on-chain.

Untuk informasi lebih lanjut: [BIP-0174](https://github.com/bitcoin/bips/blob/master/bip-0174.mediawiki)

#### Komitmen Pedersen

Komitmen Pedersen adalah sebuah jenis komitmen kriptografi dengan sifat **homomorfis** sehubungan dengan operasi penjumlahan. Ini berarti bahwa dimungkinkan untuk memvalidasi jumlah dari dua komitmen tanpa mengungkapkan nilai individual.

Secara formal, jika :

$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$

kemudian:

$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$

Properti ini berguna, misalnya, untuk menyembunyikan jumlah token yang dipertukarkan, namun tetap dapat memverifikasi totalnya.

Informasi lebih lanjut: [Pedersen commitment](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)

#### Tebus

Dalam Perpanjangan Status, Penebusan mengacu pada tindakan mengklaim kembali (atau mengeksploitasi) **Valensi** yang telah dideklarasikan sebelumnya. Karena Valensi adalah hak publik, Penukaran memungkinkan peserta yang berwenang untuk mengklaim perpanjangan status kontrak tertentu.

#### Skema

Skema dalam RGB adalah bagian kode deklaratif yang menjelaskan serangkaian variabel, aturan, dan logika bisnis (*Logika Bisnis*) yang mengatur pengoperasian kontrak. Skema mendefinisikan struktur state, jenis transisi yang diizinkan dan kondisi validasi.

#### Definisi Segel

Definisi Segel adalah bagian dari Penugasan yang mengaitkan _komitmen_ dengan UTXO yang dimiliki oleh pemegang baru. Dengan kata lain, ini menunjukkan di mana kondisi tersebut berada (di UTXO mana), dan menetapkan kepemilikan aset atau hak.

#### Pecahan

Sebuah Shard mewakili sebuah cabang dalam DAG dari riwayat Transisi Negara dari kontrak RGB. Dengan kata lain, ini adalah bagian yang koheren dari keseluruhan riwayat kontrak, sesuai, misalnya, dengan urutan transisi yang diperlukan untuk membuktikan keabsahan aset yang diberikan sejak _Genesis_.

#### Segel sekali pakai

Segel Sekali Pakai adalah janji kriptografi komitmen untuk pesan yang belum diketahui, yang hanya akan diungkapkan sekali di masa depan dan harus diketahui oleh semua anggota audiens tertentu. Tujuannya adalah untuk mencegah terciptanya beberapa komitmen yang saling bersaing untuk segel yang sama.

#### Simpanan

Stash adalah kumpulan data sisi klien yang disimpan pengguna untuk satu atau beberapa kontrak RGB, untuk tujuan validasi (*Validasi Sisi Klien*). Ini termasuk riwayat transisi, kiriman, bukti validitas, dll. Setiap pemegang hanya menyimpan bagian dari riwayat yang mereka butuhkan (*pecahan*).

#### Perpanjangan Negara Bagian

State Extension adalah operasi kontrak yang digunakan untuk memicu kembali pembaruan status dengan menebus **Valensi** yang telah dideklarasikan sebelumnya. Agar efektif, State Extension harus ditutup dengan State Transition (yang memperbarui status akhir kontrak).

#### Transisi Negara

State Transition adalah operasi yang mengubah status kontrak RGB ke status baru. Transisi ini dapat mengubah data Global State dan/atau Owned State. Dalam praktiknya, setiap transisi diverifikasi oleh aturan Skema dan berlabuh di blockchain Bitcoin melalui _commitment_.

#### Akar tunggang

Mengacu pada format transaksi Segwit v1 Bitcoin, yang diperkenalkan oleh [BIP341] (https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) dan [BIP342] (https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki). Taproot meningkatkan kerahasiaan dan fleksibilitas skrip, khususnya dengan membuat transaksi menjadi lebih ringkas dan lebih sulit untuk dibedakan satu sama lain.

#### Terminal Konsinyasi - Titik Akhir Konsinyasi

Konsinyasi Terminal (atau _Titik Akhir Konsinyasi_) adalah *konsinyasi transfer* yang berisi status akhir kontrak, termasuk Transisi Status yang dibuat dari Faktur penerima (*penerima pembayaran*). Oleh karena itu, ini adalah titik akhir transfer, dengan data yang diperlukan untuk membuktikan bahwa kepemilikan atau status telah ditransfer.

#### Bundel Transisi

Bundel Transisi adalah sekumpulan Transisi Status RGB (yang termasuk dalam kontrak yang sama) yang semuanya terlibat dalam transaksi ***saksi*** Bitcoin yang sama. Hal ini memungkinkan untuk menggabungkan beberapa pembaruan atau transfer ke dalam satu jangkar on-chain.

#### UTXO

Sebuah Bitcoin UTXO (*Unspent Transaction Output*) didefinisikan oleh hash dari sebuah transaksi dan indeks output (*vout*). Kadang-kadang juga disebut _outpoint_. Dalam protokol RGB, referensi ke UTXO (melalui **Seal Definition**) memungkinkan lokasi **Owned State**, yaitu properti yang dimiliki di blockchain.

#### Valensi

Valensi adalah hak publik yang tidak memerlukan penyimpanan negara, tetapi dapat ditebus melalui **Perpanjangan Negara**. Oleh karena itu, ini adalah bentuk kemungkinan yang terbuka untuk semua (atau pemain tertentu), yang dinyatakan dalam logika kontrak, untuk melakukan perpanjangan tertentu di kemudian hari.

#### Transaksi Saksi

Transaksi Saksi adalah transaksi Bitcoin yang menutup Segel Sekali Pakai di sekitar pesan yang berisi Komitmen Multi Protokol (MPC). Transaksi ini menghabiskan UTXO atau menciptakannya, untuk menyegel komitmen yang terkait dengan protokol RGB. Ini bertindak sebagai bukti on-chain bahwa status telah ditetapkan pada titik waktu tertentu.

# Pemrograman pada RGB

<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>

## Menerapkan kontrak RGB

<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>

![video](https://youtu.be/Uo1UoxiImsI)

Pada bab ini, kita akan melihat lebih dekat bagaimana kontrak RGB didefinisikan dan diimplementasikan. Kita akan melihat apa saja komponen-komponen dari kontrak RGB, apa saja perannya, dan bagaimana cara membuatnya.

### Komponen-komponen kontrak RGB

Sejauh ini, kita telah membahas **Genesis**, yang mewakili titik awal dari sebuah kontrak, dan kita telah melihat bagaimana hal ini sesuai dengan logika *Contract Operation* dan status protokol. Namun, definisi lengkap dari kontrak RGB tidak terbatas pada Genesis saja: kontrak ini melibatkan tiga komponen pelengkap yang, bersama-sama, membentuk inti dari implementasi.

Komponen pertama disebut **Skema**. Ini adalah file yang menjelaskan struktur dasar dan logika bisnis (*business logic*) dari kontrak. Ini menentukan tipe data yang digunakan, aturan validasi, operasi yang diizinkan (misalnya penerbitan token awal, transfer, kondisi khusus, dll.) - singkatnya, kerangka kerja umum yang menentukan cara kerja kontrak.

Komponen kedua adalah **Interface**. Komponen ini berfokus pada bagaimana pengguna (dan dengan perluasan, perangkat lunak portofolio) akan berinteraksi dengan kontrak ini. Ini menggambarkan semantik, yaitu representasi yang dapat dibaca dari berbagai bidang dan tindakan. Jadi, sementara Skema mendefinisikan bagaimana kontrak bekerja secara teknis, Antarmuka mendefinisikan bagaimana menyajikan dan mengekspos fungsi-fungsi ini: nama metode, tampilan data, dll.

Komponen ketiga adalah **Implementasi Antarmuka**, yang melengkapi dua komponen sebelumnya dengan bertindak sebagai semacam jembatan antara Skema dan Antarmuka. Dengan kata lain, komponen ini mengasosiasikan semantik yang diekspresikan oleh Antarmuka dengan aturan-aturan yang mendasari yang didefinisikan dalam Skema. Implementasi inilah yang akan mengatur, sebagai contoh, konversi antara parameter yang dimasukkan ke dalam dompet dan struktur biner yang dipaksakan oleh protokol, atau kompilasi aturan validasi dalam bahasa mesin.

Modularitas ini merupakan fitur menarik dari RGB, karena memungkinkan berbagai kelompok pengembang untuk bekerja secara terpisah pada aspek-aspek ini (*Skema*, *Interface*, *Implementasi*), selama mereka mengikuti aturan konsensus protokol.

Singkatnya, setiap kontrak terdiri dari :


- Genesis**, yang merupakan kondisi awal kontrak (dan dapat disamakan dengan transaksi khusus yang mendefinisikan kepemilikan pertama suatu aset, hak, atau data lain yang dapat diparameterkan);
- Skema**, yang menjelaskan logika bisnis kontrak (tipe data, aturan validasi, dll.);
- Antarmuka**, yang menyediakan lapisan semantik untuk dompet dan pengguna manusia, memperjelas pembacaan dan eksekusi transaksi;
- Antarmuka Implementasi**, yang menjembatani kesenjangan antara logika bisnis dan presentasi, untuk memastikan bahwa definisi kontrak konsisten dengan pengalaman pengguna.

![RGB-Bitcoin](assets/fr/070.webp)

Penting untuk diperhatikan bahwa agar dompet dapat mengelola aset RGB (baik itu token yang dapat dipertukarkan atau hak dalam bentuk apa pun), dompet harus memiliki semua elemen ini: *Skema*, *Interface*, *Implementasi Interface*, dan *Genesis*. Ini ditransmisikan melalui ***kiriman kontrak***, yaitu paket data yang berisi semua yang diperlukan untuk memvalidasi kontrak sisi klien.

Untuk membantu memperjelas pengertian ini, berikut adalah tabel ringkasan yang membandingkan komponen-komponen kontrak RGB dengan konsep-konsep yang telah dikenal baik dalam pemrograman berorientasi objek (OOP) atau dalam ekosistem Ethereum:

| Komponen Kontrak RGB | Arti | Setara OOP | Setara Ethereum |

| ---------------------------- | --------------------------------------- | -------------------------------------------------- | ---------------------------------- |

| Konstruktor kelas | Konstruktor kontrak | Status awal kontrak

| Kelas | Logika bisnis kontrak

| Semantik kontrak | Antarmuka (Java) / sifat (Rust) / protokol (Swift) | Standar ERC |

| Antarmuka Biner Aplikasi (ABI) | Impl (Rust) / Implementasi (Java) | Pemetaan semantik dan logika

Kolom sebelah kiri menunjukkan elemen yang spesifik untuk protokol RGB. Kolom tengah menunjukkan fungsi konkret dari masing-masing komponen. Kemudian, di kolom "OOP equivalent", kita menemukan istilah yang setara dalam pemrograman berorientasi objek:


- **Genesis** memainkan peran yang mirip dengan peran *Class constructor*: di sinilah status kontrak diinisialisasi;
- Skema **Skema** adalah deskripsi dari sebuah kelas, yaitu definisi properti, metode, dan logika yang mendasarinya;
- **Interface** berhubungan dengan *interface* (Java), *traits* (Rust) atau *protocols* (Swift): ini adalah definisi umum dari fungsi, peristiwa, bidang... ;
- Implementasi Antarmuka berhubungan dengan *Impl* di Rust atau *Implements* di Java, di mana kita menentukan bagaimana kode akan menjalankan metode yang diumumkan di antarmuka.

Dalam konteks Ethereum, Genesis lebih dekat dengan *contract constructor*, Skema ke definisi kontrak, Antarmuka ke standar seperti ERC-20 atau ERC-721, dan Implementasi Antarmuka ke ABI (*Application Binary Interface*), yang menentukan format interaksi dengan kontrak.

Keuntungan dari modularitas RGB juga terletak pada kenyataan bahwa pemangku kepentingan yang berbeda dapat menulis, misalnya, Implementasi Antarmuka mereka sendiri, selama mereka menghormati logika *Skema * dan semantik *Interface *. Dengan demikian, penerbit dapat mengembangkan front-end (Antarmuka) baru yang lebih ramah pengguna, tanpa mengubah logika kontrak, atau sebaliknya, seseorang dapat memperluas Skema untuk menambahkan fungsionalitas, dan menyediakan versi baru dari Implementasi Antarmuka yang diadaptasi, sementara implementasi lama akan tetap berlaku untuk fungsionalitas dasar.

Ketika kami menyusun kontrak baru, kami menghasilkan Genesis (langkah pertama dalam menerbitkan atau mendistribusikan aset), serta komponen-komponennya (Skema, Antarmuka, Implementasi Antarmuka). Setelah itu, kontrak akan beroperasi penuh dan dapat disebarkan ke dompet dan pengguna. Metode ini, di mana Genesis digabungkan dengan ketiga komponen ini, menjamin tingkat penyesuaian yang tinggi (setiap kontrak dapat memiliki logikanya sendiri), desentralisasi (setiap orang dapat berkontribusi pada komponen tertentu), dan keamanan (validasi tetap ditentukan secara ketat oleh protokol, tanpa bergantung pada kode on-chain yang sewenang-wenang seperti yang sering terjadi pada blockchain lain).

Sekarang saya ingin melihat lebih dekat pada masing-masing komponen ini: **Skema**, **Interface** dan **Implementasi Interface**.

### Skema

Pada bagian sebelumnya, kita telah melihat bahwa dalam ekosistem RGB, sebuah kontrak terdiri dari beberapa elemen: Genesis, yang menetapkan keadaan awal, dan beberapa komponen pelengkap lainnya. Tujuan dari Skema adalah untuk mendeskripsikan semua logika bisnis dari kontrak, yaitu struktur data, jenis yang digunakan, operasi yang diizinkan, dan kondisinya. Oleh karena itu, Schema merupakan elemen yang sangat penting dalam membuat kontrak dapat beroperasi di sisi klien, karena setiap partisipan (dompet, misalnya) harus memeriksa bahwa transisi state yang diterimanya sesuai dengan logika yang didefinisikan dalam Schema.

Skema dapat disamakan dengan "kelas" dalam pemrograman berorientasi objek (OOP). Secara umum, skema berfungsi sebagai model yang mendefinisikan komponen-komponen kontrak, seperti :


- Berbagai jenis Status Milik dan Penugasan ;
- Valuta, yaitu hak khusus yang dapat dipicu (*ditukarkan) untuk operasi tertentu;
- Bidang Status Global, yang menjelaskan properti global, publik, dan bersama dari kontrak;
- Struktur Genesis (operasi pertama yang mengaktifkan kontrak) ;
- Bentuk-bentuk Transisi State dan Ekstensi State yang diizinkan, dan bagaimana operasi ini dapat memodifikasi file ;
- Metadata yang terkait dengan setiap operasi, untuk menyimpan informasi sementara atau tambahan;
- Aturan yang menentukan bagaimana data kontrak internal dapat berkembang (misalnya, apakah suatu bidang dapat diubah atau kumulatif);
- Urutan operasi yang dianggap valid: misalnya, urutan transisi yang harus dipatuhi atau serangkaian kondisi logis yang harus dipenuhi.

![RGB-Bitcoin](assets/fr/071.webp)

Ketika *penerbit* aset di RGB menerbitkan kontrak, ia menyediakan Genesis dan Skema yang terkait dengannya. Pengguna atau dompet yang ingin berinteraksi dengan aset mengambil Skema ini untuk memahami logika di balik kontrak, dan untuk dapat memverifikasi nanti bahwa transisi yang akan mereka ikuti adalah sah.

Langkah pertama, bagi siapa pun yang menerima informasi tentang aset RGB (misalnya transfer token), adalah memvalidasi informasi ini terhadap Schema. Ini melibatkan penggunaan kompilasi Skema ke file :


- Periksa apakah Status Milik, Penugasan, dan elemen lainnya didefinisikan dengan benar dan bahwa mereka menghormati tipe yang diberlakukan (yang disebut *sistem tipe yang ketat*);
- Periksa apakah aturan transisi (skrip validasi) sudah terpenuhi. Skrip ini dapat dijalankan melalui AluVM, yang ada di sisi klien dan bertanggung jawab untuk memvalidasi konsistensi logika bisnis (jumlah transfer, kondisi khusus, dll.).

Pada praktiknya, Skema bukanlah kode yang dapat dieksekusi, seperti yang dapat dilihat pada blockchain yang menyimpan kode on-chain (EVM pada Ethereum). Sebaliknya, RGB memisahkan logika bisnis (deklaratif) dari kode yang dapat dieksekusi pada blockchain (yang terbatas pada jangkar kriptografi). Dengan demikian, Skema menentukan aturan, tetapi penerapan aturan ini terjadi di luar blockchain, di situs masing-masing peserta, sesuai dengan prinsip Validasi Sisi Klien.

Skema harus dikompilasi sebelum dapat digunakan oleh aplikasi RGB. Kompilasi ini menghasilkan file biner (mis. `.rgb`) atau file biner terenkripsi (`.rgba`). Ketika dompet mengimpor file ini, dompet akan mengetahui file :


- Seperti apa setiap tipe data (bilangan bulat, struktur, array...) terlihat berkat sistem tipe yang ketat;
- Bagaimana Genesis harus disusun (untuk memahami inisialisasi aset);
- Berbagai jenis operasi (Transisi State, Ekstensi State) dan bagaimana mereka dapat memodifikasi state;
- Aturan skrip (diperkenalkan dalam Skema) yang akan diterapkan oleh mesin AluVM untuk memeriksa validitas operasi.

Seperti yang telah dijelaskan pada bab-bab sebelumnya, *strict type system* memberi kita format pengkodean yang stabil dan deterministik: semua variabel, baik Owned State, Global State atau Valuta, dideskripsikan dengan tepat (ukuran, batas bawah dan batas atas jika perlu, tipe yang bertanda tangan atau tidak bertanda tangan, dan lain-lain). Hal ini juga memungkinkan untuk mendefinisikan struktur bertingkat, misalnya untuk mendukung kasus penggunaan yang kompleks.

Secara opsional, Schema dapat mereferensikan sebuah root `SchemaId`, yang memfasilitasi penggunaan kembali struktur dasar yang sudah ada (template). Dengan cara ini, Anda dapat mengembangkan kontrak atau membuat variasi (mis. jenis token baru) dari template yang sudah terbukti. Modularitas ini menghindari kebutuhan untuk membuat ulang seluruh kontrak, dan mendorong standarisasi praktik terbaik.

Poin penting lainnya adalah logika evolusi state (transfer, pembaruan, dll.) dijelaskan dalam Schema dalam bentuk skrip, aturan, dan ketentuan. Jadi, jika perancang kontrak ingin mengesahkan penerbitan ulang atau memberlakukan mekanisme pembakaran (penghancuran token), ia dapat menentukan skrip yang sesuai untuk AluVM di bagian validasi Skema.

#### Perbedaan dari blockchain on-chain yang dapat diprogram

Tidak seperti sistem seperti Ethereum, di mana kode kontrak pintar (yang dapat dieksekusi) ditulis ke dalam blockchain itu sendiri, RGB menyimpan kontrak (logikanya) di luar rantai, dalam bentuk dokumen deklaratif yang dikompilasi. Ini menyiratkan bahwa :


- Tidak ada VM Turing-complete yang berjalan di setiap node dalam jaringan Bitcoin. Aturan-aturan kontrak RGB tidak dijalankan pada blockchain, tetapi pada setiap pengguna yang ingin memvalidasi sebuah state;
- Data kontrak tidak mencemari blockchain: hanya bukti kriptografi (*komitmen*) yang disematkan pada transaksi Bitcoin (melalui `Tapret` atau `Opret`);
- Skema dapat diperbarui atau ditolak (*fast-forward*, *push-back*, dll.), tanpa memerlukan fork pada blockchain Bitcoin. Dompet hanya perlu mengimpor Skema baru dan beradaptasi dengan perubahan konsensus.

#### Penggunaan oleh penerbit dan pengguna

Ketika *emiten* membuat aset (misalnya, token yang tidak mengalami inflasi), ia akan menyiapkan :


- Skema yang menjelaskan aturan emisi, transfer, dll. ;
- Genesis yang disesuaikan dengan Skema ini (dengan jumlah total token yang diterbitkan, identitas pemilik awal, Valas khusus untuk penerbitan ulang, dll.).

Kemudian membuat Skema yang dikompilasi (file `.rgb`) tersedia untuk pengguna, sehingga siapa pun yang menerima transfer token ini dapat memeriksa konsistensi operasi secara lokal. Tanpa Skema ini, pengguna tidak akan dapat menafsirkan data status atau memeriksa apakah data tersebut sesuai dengan aturan kontrak.

Jadi, ketika dompet baru ingin mendukung suatu aset, dompet tersebut hanya perlu mengintegrasikan Schema yang relevan. Mekanisme ini memungkinkan untuk menambahkan kompatibilitas ke jenis aset RGB baru, tanpa mengubah basis perangkat lunak dompet secara invasif: yang diperlukan hanyalah mengimpor biner Schema dan memahami strukturnya.

Skema mendefinisikan logika bisnis dalam RGB. Skema ini mencantumkan aturan evolusi kontrak, struktur datanya (Status Milik, Status Global, Valuta) dan skrip validasi terkait (dapat dieksekusi oleh AluVM). Berkat dokumen deklaratif ini, definisi kontrak (file yang dikompilasi) dipisahkan dengan jelas dari eksekusi aturan yang sebenarnya (sisi klien). Pemisahan ini memberikan fleksibilitas yang tinggi kepada RGB, memungkinkan berbagai kasus penggunaan (token yang dapat dipertukarkan, NFT, kontrak yang lebih canggih) sambil menghindari kerumitan dan kekurangan yang khas dari blockchain on-chain yang dapat diprogram.

#### Contoh skema

Mari kita lihat contoh konkret dari Skema untuk kontrak RGB. Ini adalah ekstrak dalam Rust dari file `nia.rs` (inisial untuk "*Non-Inflatable Assets*"), yang mendefinisikan model untuk token yang dapat dipertukarkan yang tidak dapat diterbitkan kembali di luar pasokan awal mereka (aset yang tidak mengalami inflasi). Jenis token ini dapat dilihat sebagai padanan, di alam semesta RGB, dari ERC20 di Ethereum, yaitu token yang dapat dipertukarkan yang menghormati aturan dasar tertentu (misalnya pada transfer, inisialisasi suplai, dll.).

Sebelum masuk ke dalam kode, ada baiknya kita mengingat kembali struktur umum Skema RGB. Terdapat serangkaian deklarasi yang membingkai :


- Kemungkinan `SchemaId` yang menunjukkan penggunaan Skema dasar lain sebagai templat;
- Negara Global** dan Negara Milik** (dengan tipe-tipe yang ketat);
- Nilai tukar** (jika ada);
- Operasi **Operasi** (Kejadian, Transisi Keadaan, Ekstensi Keadaan) yang dapat merujuk keadaan dan valensi ini;
- Sistem **Strict Type System** digunakan untuk mendeskripsikan dan memvalidasi data;
- Skrip validasi** (dijalankan melalui AluVM).

![RGB-Bitcoin](assets/fr/072.webp)

Kode di bawah ini menunjukkan definisi lengkap dari Skema Karat. Kami akan mengomentari bagian demi bagian, mengikuti anotasi (1) hingga (9) di bawah ini:

```rust
// ===== PART 1: Function Header and SubSchema =====
fn nia_schema() -> SubSchema {
// definitions of libraries and variables
// ===== PART 2: General Properties (ffv, subset_of, type_system) =====
Schema {
ffv: zero!(),
subset_of: None,
type_system: types.type_system(),
// ===== PART 3: Global States =====
global_types: tiny_bmap! {
GS_NOMINAL => GlobalStateSchema::once(types.get("RGBContract.DivisibleAssetSpec")),
GS_DATA => GlobalStateSchema::once(types.get("RGBContract.ContractData")),
GS_TIMESTAMP => GlobalStateSchema::once(types.get("RGBContract.Timestamp")),
GS_ISSUED_SUPPLY => GlobalStateSchema::once(types.get("RGBContract.Amount")),
},
// ===== PART 4: Owned Types =====
owned_types: tiny_bmap! {
OS_ASSET => StateSchema::Fungible(FungibleType::Unsigned64Bit),
},
// ===== PART 5: Valencies =====
valency_types: none!(),
// ===== PART 6: Genesis: Initial Operations =====
genesis: GenesisSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: tiny_bmap! {
GS_NOMINAL => Occurrences::Once,
GS_DATA => Occurrences::Once,
GS_TIMESTAMP => Occurrences::Once,
GS_ISSUED_SUPPLY => Occurrences::Once,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
},
// ===== PART 7: Extensions =====
extensions: none!(),
// ===== PART 8: Transitions: TS_TRANSFER =====
transitions: tiny_bmap! {
TS_TRANSFER => TransitionSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: none!(),
inputs: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
}
},
// ===== PART 9: Script AluVM and Entry Points =====
script: Script::AluVM(AluScript {
libs: confined_bmap! { alu_id => alu_lib },
entry_points: confined_bmap! {
EntryPoint::ValidateGenesis => LibSite::with(FN_GENESIS_OFFSET, alu_id),
EntryPoint::ValidateTransition(TS_TRANSFER) => LibSite::with(FN_TRANSFER_OFFSET, alu_id),
},
}),
}
}
```


- (1) - Tajuk fungsi dan SubSkema**

Fungsi `nia_schema()` mengembalikan sebuah `SubSchema`, yang mengindikasikan bahwa Skema ini dapat mewarisi sebagian dari skema yang lebih umum. Dalam ekosistem RGB, fleksibilitas ini memungkinkan untuk menggunakan kembali elemen standar tertentu dari skema master, dan kemudian mendefinisikan aturan khusus untuk kontrak yang bersangkutan. Di sini, kita memilih untuk tidak mengaktifkan pewarisan, karena `subset_of` akan menjadi `None`.


- (2) - Properti umum: ffv, subset_of, type_system**

Properti `ffv` berhubungan dengan versi kontrak *fast-forward*. Nilai `zero!()` di sini menunjukkan bahwa kita berada di versi 0 atau versi awal skema ini. Jika Anda kemudian ingin menambahkan fungsi baru (jenis operasi baru, dll.), Anda dapat meningkatkan versi ini untuk menunjukkan perubahan konsensus.

Properti `subset_of: Tidak ada` mengonfirmasi tidak adanya pewarisan. Bidang `type_system` mengacu pada sistem tipe ketat yang sudah didefinisikan dalam pustaka `types`. Baris ini menunjukkan bahwa semua data yang digunakan oleh kontrak menggunakan implementasi serialisasi ketat yang disediakan oleh pustaka yang bersangkutan.


- (3) - Negara Global

Dalam blok `global_types`, kita mendeklarasikan empat elemen. Kita menggunakan kunci, seperti `GS_NOMINAL` atau `GS_ISSUED_SUPPLY`, untuk mereferensikannya nanti:


- `GS_NOMINAL` mengacu pada tipe `DivisibleAssetSpec`, yang menjelaskan berbagai bidang dari token yang dibuat (nama lengkap, ticker, presisi...);
- `GS_DATA` mewakili data umum, seperti penafian, metadata, atau teks lainnya;
- `GS_TIMESTAMP` mengacu pada tanggal penerbitan;
- `GS_ISSUED_SUPPLY` menetapkan total pasokan, yaitu jumlah maksimum token yang dapat dibuat.

Kata kunci `sekali(...)` berarti bahwa setiap bidang ini hanya dapat muncul satu kali.


- (4) - Tipe Milik Sendiri

Di dalam `owned_types`, kita mendeklarasikan `OS_ASSET`, yang menggambarkan sebuah kondisi yang dapat dipertukarkan. Kita menggunakan `StateSchema::Fungible(FungibleType::Unsigned64Bit)`, yang mengindikasikan bahwa jumlah aset (token) disimpan sebagai bilangan bulat tidak bertanda tangan 64-bit. Dengan demikian, setiap transaksi akan mengirimkan sejumlah unit token ini, yang akan divalidasi sesuai dengan struktur numerik yang diketik secara ketat ini.


- (5) - Nilai tukar**

Kami mengindikasikan `valency_types: none!()`, yang berarti tidak ada Valensi dalam skema ini, dengan kata lain tidak ada hak khusus atau tambahan (seperti penerbitan ulang, pembakaran bersyarat, dll.). Jika sebuah skema memiliki hak khusus, maka hak khusus tersebut akan dideklarasikan di bagian ini.


- (6) - Kejadian: operasi pertama

Di sini kita memasuki bagian yang menyatakan Operasi Kontrak. Kejadian dijelaskan oleh :


- Tidak adanya `metadata` (bidang `metadata: Ty::<SemId>::UNIT.id(None)`) ;
- Negara-negara Global yang masing-masing harus hadir satu kali (`Sekali`);
- Daftar Penugasan di mana `OS_ASSET` harus muncul `Sekali Atau Lebih`. Ini berarti bahwa Genesis membutuhkan setidaknya satu Penugasan `OS_ASSET` (pemegang awal);
- Tidak ada Valensi : `valensi: tidak ada!() `.

Ini adalah cara kita membatasi definisi penerbitan token awal: kita harus mendeklarasikan pasokan yang diterbitkan (`GS_ISSUED_SUPPLY`), ditambah setidaknya satu pemegang (Status Milik tipe `OS_ASSET`).


- (7) - Ekstensi

Kolom `extensions: none!()` menunjukkan bahwa tidak ada Perpanjangan Status yang diperkirakan dalam kontrak ini. Ini berarti bahwa tidak ada operasi untuk menebus hak digital (Valensi) atau melakukan ekstensi negara sebelum Transisi. Semuanya dilakukan melalui Genesis atau State Transitions.


- (8) - Transisi: TS_TRANSFER

Dalam `transisi`, kita mendefinisikan jenis operasi `TS_TRANSFER`. Kami menjelaskan bahwa :


- Tidak memiliki metadata;
- Ini tidak memodifikasi Global State (yang sudah didefinisikan dalam Genesis);
- Dibutuhkan satu atau lebih `OS_ASSET` sebagai input. Ini berarti ia harus menggunakan Status Milik yang ada;
- Ini menciptakan (`penugasan`) setidaknya satu `OS_ASSET` baru (dengan kata lain, penerima atau penerima menerima token);
- Ini tidak menghasilkan Valensi baru.

Ini memodelkan perilaku transfer dasar, yang mengkonsumsi token pada UTXO, kemudian menciptakan Status Milik baru yang mendukung penerima, dan dengan demikian menjaga kesetaraan jumlah total antara input dan output.


- (9) - Skrip AluVM dan Titik Masuk** (dalam bahasa Prancis)

Terakhir, kita mendeklarasikan skrip AluVM (`Skrip::AluVM(AluScript {... })`). Skrip ini berisi file :


- Satu atau lebih pustaka eksternal (`lib`) yang akan digunakan selama validasi;
- Titik masuk yang menunjuk ke offset fungsi dalam kode AluVM, sesuai dengan validasi Genesis (`ValidateGenesis`) dan setiap Transisi yang dideklarasikan (`ValidateTransition (TS_TRANSFER) `).

Kode validasi ini bertanggung jawab untuk menerapkan logika bisnis. Sebagai contoh, kode ini akan memeriksa :


- Bahwa `GS_ISSUED_SUPPLY` tidak terlampaui selama Kejadian ;
- Bahwa jumlah `input` (token yang dihabiskan) sama dengan jumlah `penugasan` (token yang diterima) untuk `TS_TRANSFER`.

Jika aturan ini tidak dipatuhi, transisi akan dianggap tidak sah.

Contoh Skema "*Non Inflatable Fungible Asset*" ini memberikan pemahaman yang lebih baik tentang struktur kontrak token fungible RGB sederhana. Kita dapat dengan jelas melihat pemisahan antara deskripsi data (Global dan Owned States), deklarasi operasi (Genesis, Transisi, Ekstensi), dan implementasi validasi (skrip AluVM). Berkat model ini, sebuah token berperilaku seperti token fungible klasik, tetapi tetap divalidasi di sisi klien dan tidak bergantung pada infrastruktur on-chain untuk menjalankan kodenya. Hanya komitmen kriptografi yang ditambatkan dalam blockchain Bitcoin.

### Antarmuka

Antarmuka adalah lapisan yang dirancang untuk membuat kontrak dapat dibaca dan dimanipulasi, baik oleh pengguna (pembacaan manusia) maupun oleh portofolio (pembacaan perangkat lunak). Oleh karena itu, Antarmuka memainkan peran yang sebanding dengan antarmuka dalam bahasa pemrograman berorientasi objek (Java, Rust trait, dll.), dalam hal ini ia mengekspos dan memperjelas struktur fungsional kontrak, tanpa harus mengungkapkan detail internal logika bisnis.

Tidak seperti Skema, yang murni deklaratif dan dikompilasi ke dalam file biner yang sulit digunakan sebagaimana adanya, Antarmuka menyediakan kunci pembacaan yang diperlukan untuk file :


- Sebutkan dan jelaskan Negara Global dan Negara Milik yang termasuk dalam kontrak;
- Mengakses nama dan nilai dari setiap bidang, sehingga dapat ditampilkan (misalnya untuk token, cari tahu ticker, jumlah maksimum, dll.);
- Menafsirkan dan membangun Operasi Kontrak (Genesis, State Transition, atau State Extension) dengan mengaitkan data dengan nama yang dapat dimengerti (misalnya, melakukan transfer dengan menyebutkan "jumlah" secara jelas, bukan dengan pengenal biner).

![RGB-Bitcoin](assets/fr/073.webp)

Berkat Antarmuka, Anda dapat, misalnya, menulis kode dalam dompet yang, alih-alih memanipulasi bidang, secara langsung memanipulasi label seperti "jumlah token", "nama aset", dll. Dengan cara ini, mengelola kontrak menjadi lebih intuitif. Dengan cara ini, manajemen kontrak menjadi lebih intuitif.

#### Operasi umum

Metode ini memiliki banyak keuntungan:


- Standardisasi:**

Jenis kontrak yang sama dapat didukung oleh sebuah Antarmuka standar, yang digunakan bersama oleh beberapa implementasi dompet. Hal ini memfasilitasi kompatibilitas dan penggunaan ulang kode.


- Pemisahan yang jelas antara Skema dan Antarmuka:**

Dalam desain RGB, Skema (logika bisnis) dan Antarmuka (presentasi dan manipulasi) adalah dua entitas independen. Pengembang yang menulis logika kontrak dapat berkonsentrasi pada Schema, tanpa mengkhawatirkan ergonomi atau representasi data, sementara tim lain (atau tim yang sama, tetapi pada jadwal yang berbeda) dapat mengembangkan Antarmuka.


- Evolusi yang fleksibel:**

Antarmuka dapat dimodifikasi atau ditambahkan setelah aset diterbitkan, tanpa harus mengubah kontrak itu sendiri. Ini adalah perbedaan utama dari beberapa sistem smart contract on-chain, di mana Antarmuka (sering kali dicampur dengan kode eksekusi) dibekukan dalam blockchain.


- Kemampuan multi-antarmuka

Kontrak yang sama dapat diekspos melalui Antarmuka yang berbeda yang disesuaikan dengan kebutuhan yang berbeda: Antarmuka sederhana untuk pengguna akhir, Antarmuka lain yang lebih canggih untuk penerbit yang perlu mengelola operasi konfigurasi yang kompleks. Dompet kemudian dapat memilih Antarmuka mana yang akan diimpor, tergantung pada penggunaannya.

![RGB-Bitcoin](assets/fr/074.webp)

Dalam praktiknya, ketika dompet mengambil kontrak RGB (melalui file `.rgb` atau `.rgba`), dompet juga mengimpor Antarmuka yang terkait, yang juga dikompilasi. Pada saat runtime, dompet dapat, misalnya, membuat file :


- Jelajahi daftar negara bagian dan baca namanya, untuk menampilkan Ticker, Jumlah Awal, Tanggal Terbit, dll. pada antarmuka pengguna, daripada pengenal numerik yang tidak dapat dibaca;
- Buatlah sebuah operasi (seperti transfer) dengan menggunakan nama parameter eksplisit: alih-alih menulis `penugasan { OS_ASSET => 1 }`, ini dapat menawarkan kepada pengguna sebuah kolom "Jumlah" dalam formulir, dan menerjemahkan informasi ini ke dalam kolom yang diketikkan secara ketat sesuai dengan yang diharapkan oleh kontrak.

#### Perbedaan dari Ethereum dan sistem lainnya

Di Ethereum, Antarmuka (dijelaskan melalui ABI, *Application Binary Interface*) umumnya berasal dari kode yang tersimpan secara on-chain (kontrak pintar). Memodifikasi bagian tertentu dari antarmuka tanpa menyentuh kontrak itu sendiri dapat menjadi mahal atau rumit. Akan tetapi, RGB didasarkan pada logika yang sepenuhnya off-chain, dengan data yang tersimpan dalam *komitmen* pada Bitcoin. Desain ini memungkinkan untuk memodifikasi Antarmuka (atau implementasinya) tanpa memengaruhi keamanan dasar kontrak, karena validasi aturan bisnis tetap berada di dalam Skema dan kode AluVM yang direferensikan.

#### Kompilasi antarmuka

Seperti halnya Skema, Antarmuka didefinisikan dalam kode sumber (sering kali dalam bahasa Rust) dan dikompilasi ke dalam file `.rgb` atau `.rgba`. File biner ini berisi semua informasi yang dibutuhkan oleh dompet untuk :


- Mengidentifikasi bidang berdasarkan nama ;
- Tautkan setiap bidang (dan nilainya) ke jenis sistem ketat yang ditentukan dalam kontrak;
- Ketahui berbagai operasi yang diizinkan dan cara membuatnya.

Setelah Antarmuka diimpor, dompet dapat menampilkan kontrak dengan benar dan mengusulkan interaksi kepada pengguna.

### Antarmuka yang distandarisasi oleh asosiasi LNP/BP

Dalam ekosistem RGB, Antarmuka digunakan untuk memberikan makna yang dapat dibaca dan dimanipulasi pada data dan operasi kontrak. Dengan demikian, Antarmuka melengkapi Skema, yang menggambarkan logika bisnis secara internal (tipe yang ketat, skrip validasi, dll.). Pada bagian ini, kita akan melihat Antarmuka standar yang dikembangkan oleh asosiasi LNP/BP untuk jenis kontrak yang umum (token yang dapat dipertukarkan, NFT, dll.).

Sebagai pengingat, idenya adalah bahwa setiap Antarmuka menjelaskan cara menampilkan dan memanipulasi kontrak di sisi dompet, dengan jelas menamai bidang-bidangnya (seperti `spec`, `ticker`, `issuedSupply`...) dan mendefinisikan operasi-operasi yang mungkin dilakukan (seperti `Transfer`, `Burn`, `Rename`...). Beberapa Antarmuka sudah beroperasi, tetapi akan ada lebih banyak lagi di masa depan.

#### Beberapa antarmuka yang siap digunakan

**RGB20** adalah Antarmuka untuk aset yang dapat dipertukarkan, yang dapat dibandingkan dengan standar ERC20 Ethereum. Namun, ini melangkah lebih jauh, menawarkan fungsionalitas yang lebih luas:


- Misalnya, kemampuan untuk mengganti nama aset (perubahan *ticker* atau nama lengkap) setelah diterbitkan, atau untuk menyesuaikan ketepatannya (*pemecahan saham*);
- Hal ini juga dapat menjelaskan mekanisme untuk penerbitan ulang sekunder (terbatas atau tidak terbatas) dan untuk pembakaran dan kemudian penggantian, dalam rangka memberikan wewenang kepada penerbit untuk menghancurkan dan kemudian menciptakan kembali aset dalam kondisi tertentu;

Sebagai contoh, Antarmuka RGB20 dapat dihubungkan ke skema **Non-Inflatable Asset (NIA) **, yang memberlakukan pasokan awal yang tidak dapat diinflasi, atau ke skema yang lebih canggih lainnya sesuai kebutuhan.

**GBP21** berkaitan dengan kontrak tipe NFT, atau lebih luas lagi, konten digital yang unik, seperti representasi media digital (gambar, musik, dll.). Selain menjelaskan masalah dan transfer aset tunggal, ini mencakup fitur-fitur seperti :


- Dukungan terintegrasi untuk penyertaan file secara langsung (hingga 16 MB) dalam kontrak (untuk pengambilan dari sisi klien);
- Kemungkinan bagi pemilik untuk memasukkan "*ukiran*" dalam riwayat untuk membuktikan kepemilikan NFT di masa lalu.

**RGB25** adalah standar hibrida yang menggabungkan aspek yang dapat dipertukarkan dan yang tidak dapat dipertukarkan. Ini dirancang untuk aset yang dapat dipertukarkan sebagian, seperti tokenisasi real estat, di mana Anda ingin memisahkan properti sambil mempertahankan tautan ke satu aset root (dengan kata lain, Anda memiliki potongan rumah yang dapat dipertukarkan, yang ditautkan ke rumah yang tidak dapat dipertukarkan). Secara teknis, antarmuka ini dapat ditautkan ke skema **Collectible Fungible Asset* (CFA), yang memperhitungkan gagasan pemisahan sambil melacak aset asli.

#### Antarmuka yang sedang dikembangkan

Antarmuka lain direncanakan untuk penggunaan yang lebih khusus, tetapi belum tersedia:


- RGB22**, didedikasikan untuk identitas digital, untuk mengelola pengidentifikasi dan profil on-chain dalam ekosistem RGB;
- RGB23**, untuk stempel waktu tingkat lanjut, menggunakan sebagian ide *Opentimestamps*, tetapi dengan fitur penelusuran;
- RGB24**, yang bertujuan untuk setara dengan sistem nama domain terdesentralisasi (DNS) yang mirip dengan *Ethereum Name Service*;
- RGB26**, dirancang untuk mengelola DAO (*Decentralized Autonomous Organization*) dalam format yang lebih kompleks (tata kelola, pemungutan suara, dll.);
- RGB30**, sangat mirip dengan RGB20 tetapi dengan kekhususan memperhitungkan penerbitan awal yang terdesentralisasi dan menggunakan Ekstensi Negara. Ini akan digunakan untuk aset yang penerbitan ulangnya dikelola oleh beberapa entitas, atau tunduk pada kondisi yang lebih baik.

Tentu saja, tergantung pada tanggal Anda membaca kursus ini, antarmuka-antarmuka ini mungkin sudah beroperasi dan dapat diakses.

#### Contoh antarmuka

Potongan kode Rust ini menunjukkan Antarmuka [RGB20] (https://github.com/RGB-WG/rgb-std/blob/master/src/interface/rgb20.rs) (aset yang dapat dipertukarkan). Kode ini diambil dari file `rgb20.rs` dalam pustaka RGB standar. Mari kita lihat untuk memahami struktur Antarmuka dan bagaimana ia menyediakan jembatan antara, di satu sisi, logika bisnis (didefinisikan dalam Skema) dan, di sisi lain, fungsi yang terpapar ke dompet dan pengguna.

```rust
// ...
fn rgb20() -> Iface {
let types = StandardTypes::with(rgb20_stl());
Iface {
version: VerNo::V1,
name: tn!("RGB20"),
global_state: tiny_bmap! {
fname!("spec") => GlobalIface::required(types.get("RGBContract.DivisibleAssetSpec")),
fname!("data") => GlobalIface::required(types.get("RGBContract.ContractData")),
fname!("created") => GlobalIface::required(types.get("RGBContract.Timestamp")),
fname!("issuedSupply") => GlobalIface::one_or_many(types.get("RGBContract.Amount")),
fname!("burnedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
fname!("replacedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
},
assignments: tiny_bmap! {
fname!("inflationAllowance") => AssignIface::public(OwnedIface::Amount, Req::NoneOrMore),
fname!("updateRight") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnEpoch") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnRight") => AssignIface::public(OwnedIface::Rights, Req::NoneOrMore),
fname!("assetOwner") => AssignIface::private(OwnedIface::Amount, Req::NoneOrMore),
},
valencies: none!(),
genesis: GenesisIface {
metadata: Some(types.get("RGBContract.IssueMeta")),
global: tiny_bmap! {
fname!("spec") => ArgSpec::required(),
fname!("data") => ArgSpec::required(),
fname!("created") => ArgSpec::required(),
fname!("issuedSupply") => ArgSpec::required(),
},
assignments: tiny_bmap! {
fname!("assetOwner") => ArgSpec::many(),
fname!("inflationAllowance") => ArgSpec::many(),
fname!("updateRight") => ArgSpec::optional(),
fname!("burnEpoch") => ArgSpec::optional(),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_RESERVES
},
},
transitions: tiny_bmap! {
tn!("Transfer") => TransitionIface {
optional: false,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("previous") => ArgSpec::from_non_empty("assetOwner"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_non_empty("assetOwner"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Issue") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.IssueMeta")),
globals: tiny_bmap! {
fname!("issuedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_non_empty("inflationAllowance"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_many("inflationAllowance"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
ISSUE_EXCEEDS_ALLOWANCE,
INSUFFICIENT_RESERVES
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("OpenEpoch") => TransitionIface {
optional: true,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnEpoch"),
},
assignments: tiny_bmap! {
fname!("next") => ArgSpec::from_optional("burnEpoch"),
fname!("burnRight") => ArgSpec::required()
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("burnRight")),
},
tn!("Burn") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("burnedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: None,
},
tn!("Replace") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("replacedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS,
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Rename") => TransitionIface {
optional: true,
metadata: None,
globals: tiny_bmap! {
fname!("new") => ArgSpec::from_required("spec"),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("updateRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("updateRight"),
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("future")),
},
},
extensions: none!(),
error_type: types.get("RGB20.Error"),
default_operation: Some(tn!("Transfer")),
type_system: types.type_system(),
}
}
```

Pada antarmuka ini, kami melihat kesamaan dengan struktur Skema: kami menemukan deklarasi Global State, Owned States, Operasi Kontrak (Genesis dan Transisi), serta penanganan kesalahan. Tetapi Antarmuka berfokus pada presentasi dan manipulasi elemen-elemen ini untuk dompet atau aplikasi lainnya.

Perbedaannya dengan Schema terletak pada sifat tipe. Schema menggunakan tipe yang ketat (seperti `FungibleType::Unsigned64Bit`) dan pengenal yang lebih teknis. Antarmuka menggunakan nama field, makro (`fname!()`, `tn!()`), dan referensi ke kelas-kelas argumen (`ArgSpec`, `OwnedIface::Rights`...). Tujuannya adalah untuk memudahkan pemahaman fungsional dan pengorganisasian elemen-elemen dompet.

Selain itu, Antarmuka dapat memperkenalkan fungsionalitas tambahan pada Skema dasar (misalnya manajemen hak `burnEpoch`), selama ini tetap konsisten dengan logika sisi klien yang telah divalidasi. Bagian "skrip" AluVM dalam Skema akan memastikan validitas kriptografi, sementara Antarmuka menjelaskan bagaimana pengguna (atau dompet) berinteraksi dengan status dan transisi ini.

#### Status dan Penugasan Global

Pada bagian `global_state`, kita dapat menemukan kolom seperti `spec` (deskripsi aset), `data`, `dibuat`, `issuedSupply`, `burnedSupply`, `replacedSupply`. Ini adalah bidang yang dapat dibaca dan ditampilkan oleh dompet. Sebagai contoh:


- `spec` akan menampilkan konfigurasi token;
- `issuedSupply` atau `burnedSupply` memberi kita jumlah total token yang diterbitkan atau dibakar, dll.

Pada bagian `penugasan`, kami mendefinisikan berbagai peran atau hak. Sebagai contoh:


- `PemilikAset` berhubungan dengan kepemilikan token (ini adalah *Status Milik yang dapat dipertukarkan);
- `burnRight` berhubungan dengan kemampuan untuk membakar token;
- updateRight` berhubungan dengan hak untuk mengganti nama aset.

Kata kunci `public` atau `private` (misalnya `AssignIface::public(...)`) mengindikasikan apakah status ini dapat dilihat (`public`) atau rahasia (`private`). Sedangkan untuk `Req::NoneOrMore`, `Req::Optional`, menunjukkan kejadian yang diharapkan.

#### Kejadian dan transisi

Bagian `genesis` menjelaskan bagaimana aset diinisialisasi:


- Bidang `spec`, `data`, `created`, `issuedSupply` wajib diisi (`ArgSpec::required()`);
- Penugasan seperti `assetOwner` dapat hadir dalam beberapa salinan (`ArgSpec::many()`), yang memungkinkan token didistribusikan ke beberapa pemegang awal;
- Field seperti `inflationAllowance` atau `burnEpoch` dapat (atau mungkin tidak) disertakan dalam Genesis.

Kemudian, untuk setiap Transisi (`Transfer`, `Issue`, `Burn`...), Antarmuka mendefinisikan bidang mana yang diharapkan oleh operasi sebagai input, bidang mana yang akan dihasilkan oleh operasi sebagai output, dan kesalahan apa pun yang mungkin terjadi. Sebagai contoh:

** Transisi :**


- Input : `sebelumnya` → harus berupa `pemilikaset`;
- Penugasan : `penerima manfaat` → akan menjadi `pemilikaset` yang baru;
- Kesalahan: `NON_EQUAL_AMOUNTS` (dompet akan dapat menangani kasus dimana jumlah input tidak sesuai dengan jumlah output).

**Transisi `Masalah` :**


- Opsional (`optional: true`), karena emisi tambahan tidak harus diaktifkan;
- Masukan: `used` → sebuah `inflationAllowance`, yaitu izin untuk menambahkan lebih banyak token;
- Penugasan: penerima (token baru yang diterima) dan `masa depan` (sisa `Tunjangan Inflasi`);
- Kemungkinan kesalahan: `SUPPLY_MISMATCH`, `ISSUE_EXCEEDS_ALLOWANCE`, dll.

** Transisi pembakaran :**


- Masukan : `digunakan` → sebuah `bakarKanan`;
- Global : `burnedSupply` diperlukan;
- Penugasan: `masa depan` → kemungkinan kelanjutan dari `bakarKanan` jika kita belum membakar semuanya;
- Kesalahan: `KETIDAKCOCOKAN_PASOKAN`, `BUKTI_INVALID`, `CAKUPAN_KURANG`.

Oleh karena itu, setiap operasi dijelaskan dengan cara yang dapat dibaca oleh dompet. Hal ini memungkinkan untuk menampilkan antarmuka grafis yang dapat dilihat dengan jelas oleh pengguna: "Anda memiliki hak untuk membakar. Apakah Anda ingin membakar dalam jumlah tertentu? Kode tahu untuk mengisi kolom `burnedSupply` dan memeriksa apakah `burnRight` valid.

Singkatnya, penting untuk diingat bahwa Antarmuka, betapapun lengkapnya, tidak dengan sendirinya mendefinisikan logika internal kontrak. Inti dari pekerjaan ini dilakukan oleh **Skema**, yang mencakup tipe yang ketat, struktur Genesis, transisi, dan sebagainya. Antarmuka hanya memaparkan elemen-elemen ini dengan cara yang lebih intuitif dan dinamai, untuk digunakan dalam aplikasi.

Berkat modularitas RGB, Antarmuka dapat ditingkatkan (misalnya, dengan menambahkan transisi `Rename`, mengoreksi tampilan bidang, dll.) tanpa harus menulis ulang seluruh kontrak. Pengguna Antarmuka ini kemudian dapat segera mendapatkan manfaat dari peningkatan ini, segera setelah mereka memperbarui file `.rgb` atau `.rgba`.

Tetapi setelah Anda mendeklarasikan sebuah Interface, Anda harus menghubungkannya dengan Skema yang sesuai. Hal ini dilakukan melalui ***Implementasi Antarmuka***, yang menentukan cara memetakan setiap field bernama (seperti `fname!("assetOwner")`) ke ID ketat (seperti `OS_ASSET`) yang didefinisikan dalam Skema. Hal ini memastikan, sebagai contoh, ketika dompet memanipulasi field `burnRight`, ini adalah status yang, dalam Skema, menjelaskan kemampuan untuk membakar token.

### Implementasi Antarmuka

Dalam arsitektur RGB, kita telah melihat bahwa setiap komponen (Skema, Antarmuka, dll.) dapat dikembangkan dan dikompilasi secara independen. Namun, masih ada satu elemen yang sangat diperlukan yang menghubungkan blok bangunan yang berbeda ini bersama-sama: ***Implementasi Antarmuka***. Inilah yang secara eksplisit memetakan pengidentifikasi atau bidang yang didefinisikan dalam Skema (di sisi logika bisnis) ke nama-nama yang dideklarasikan dalam Antarmuka (di sisi presentasi dan interaksi pengguna). Jadi, ketika wallet memuat kontrak, wallet dapat memahami dengan tepat field mana yang berhubungan dengan apa, dan bagaimana sebuah operasi yang dinamai di Antarmuka berhubungan dengan logika Skema.

Poin penting adalah bahwa Implementasi Antarmuka tidak selalu dimaksudkan untuk mengekspos semua fungsi Skema, atau semua bidang Antarmuka: dapat dibatasi pada subset. Dalam praktiknya, hal ini memungkinkan untuk membatasi atau memfilter aspek-aspek tertentu dari Skema. Sebagai contoh, Anda dapat memiliki Skema dengan empat jenis operasi, tetapi Antarmuka Implementasi yang memetakan hanya dua di antaranya dalam konteks tertentu. Sebaliknya, jika Antarmuka mengusulkan titik akhir tambahan, kita dapat memilih untuk tidak mengimplementasikannya di sini.

Berikut adalah contoh klasik Implementasi Antarmuka, di mana kami mengaitkan Skema *Non-Inflatable Asset* (NIA) dengan Antarmuka RGB20:

```rust
fn nia_rgb20() -> IfaceImpl {
let schema = nia_schema();
let iface = Rgb20::iface();
IfaceImpl {
version: VerNo::V1,
schema_id: schema.schema_id(),
iface_id: iface.iface_id(),
script: none!(),
global_state: tiny_bset! {
NamedField::with(GS_NOMINAL, fname!("spec")),
NamedField::with(GS_DATA, fname!("data")),
NamedField::with(GS_TIMESTAMP, fname!("created")),
NamedField::with(GS_ISSUED_SUPPLY, fname!("issuedSupply")),
},
assignments: tiny_bset! {
NamedField::with(OS_ASSET, fname!("assetOwner")),
},
valencies: none!(),
transitions: tiny_bset! {
NamedType::with(TS_TRANSFER, tn!("Transfer")),
},
extensions: none!(),
}
}
```

Dalam Antarmuka Implementasi ini:


- Kami secara eksplisit mereferensikan Skema, melalui `nia_schema()`, dan Antarmuka, melalui `Rgb20::iface()`. Panggilan `schema.schema_id()` dan `iface.iface_id()` digunakan untuk menambatkan Implementasi Antarmuka di sisi kompilasi (ini mengaitkan pengidentifikasi kriptografi dari kedua komponen ini);
- Pemetaan dibuat antara elemen Skema dan elemen Antarmuka. Sebagai contoh, bidang `GS_NOMINAL` dalam Skema dihubungkan ke string `"spec"` di sisi Antarmuka (`NamedField::with(GS_NOMINAL, fname!("spec"))`). Kami melakukan hal yang sama untuk operasi, seperti `TS_TRANSFER`, yang kami tautkan ke `"Transfer"` di Antarmuka... ;
- Kita dapat melihat bahwa tidak ada valensi (`valensi: none!()`) atau ekstensi (`ekstensi: none!()`), yang mencerminkan fakta bahwa kontrak NIA ini tidak menggunakan fitur-fitur ini.

Hasil setelah kompilasi adalah file `.rgb` atau `.rgba` yang terpisah, yang akan diimpor ke dalam dompet sebagai tambahan dari Skema dan Antarmuka. Dengan demikian, perangkat lunak tahu bagaimana menghubungkan secara konkret kontrak NIA ini (yang logikanya dijelaskan oleh Skema) ke Antarmuka "RGB20" (yang menyediakan nama manusia dan mode interaksi untuk token yang dapat dipertukarkan), menerapkan Implementasi Antarmuka ini sebagai pintu gerbang di antara keduanya.

#### Mengapa memisahkan Implementasi Antarmuka?

Pemisahan meningkatkan fleksibilitas. Satu Skema dapat memiliki beberapa Implementasi Antarmuka yang berbeda, masing-masing memetakan serangkaian fungsi yang berbeda. Terlebih lagi, Implementasi Antarmuka itu sendiri dapat berevolusi atau ditulis ulang tanpa memerlukan perubahan pada Skema atau Antarmuka. Ini mempertahankan prinsip modularitas RGB: setiap komponen (Skema, Antarmuka, Implementasi Antarmuka) dapat diberi versi dan diperbarui secara independen, selama aturan kompatibilitas yang diberlakukan oleh protokol dipatuhi (pengidentifikasi yang sama, konsistensi jenis, dll.).

Dalam penggunaan konkret, ketika dompet memuat kontrak, dompet harus :


- Muat **Skema** yang telah dikompilasi (untuk mengetahui struktur logika bisnis);
- Memuat **Interface** yang dikompilasi (untuk memahami nama dan operasi sisi pengguna);
- Memuat kompilasi **Implementasi Antarmuka** (untuk menghubungkan logika Skema ke nama Antarmuka, operasi demi operasi, bidang demi bidang).

Arsitektur modular ini memungkinkan skenario penggunaan yang memungkinkan, seperti :


- Batasi operasi tertentu untuk pengguna tertentu: tawarkan Antarmuka Implementasi parsial yang hanya memberikan akses ke transfer dasar, tanpa menawarkan fungsi pembakaran atau pembaruan, misalnya;
- Ubah presentasi: merancang Implementasi Antarmuka yang mengganti nama bidang di Antarmuka atau memetakannya secara berbeda, tanpa mengubah dasar kontrak;
- Mendukung beberapa skema: dompet dapat memuat beberapa Implementasi Antarmuka untuk jenis Antarmuka yang sama, untuk menangani skema yang berbeda (logika token yang berbeda), asalkan strukturnya kompatibel.

Pada bab berikutnya, kita akan melihat cara kerja transfer kontrak, dan bagaimana faktur RGB dibuat.

## Transfer kontrak

<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>

![video](https://youtu.be/sVoKIi-1XbY)

Pada bab ini, kita akan menganalisis proses transfer kontrak dalam ekosistem RGB. Untuk mengilustrasikan hal ini, kita akan melihat Alice dan Bob, tokoh protagonis yang biasa kita temui, yang ingin menukarkan aset RGB. Kita juga akan menunjukkan beberapa kutipan perintah dari alat bantu baris perintah `rgb`, untuk melihat bagaimana cara kerjanya dalam praktik.

### Memahami transfer kontrak RGB

Mari kita ambil contoh transfer antara Alice dan Bob. Dalam contoh ini, kita asumsikan bahwa Bob baru saja mulai menggunakan RGB, sementara Alice sudah memiliki aset RGB di dompetnya. Kita akan melihat bagaimana Bob menyiapkan lingkungannya, mengimpor kontrak yang relevan, kemudian meminta transfer dari Alice, dan akhirnya bagaimana Alice melakukan transaksi yang sebenarnya di blockchain Bitcoin.

#### 1) Memasang dompet RGB

Pertama-tama, Bob harus menginstal dompet RGB, yaitu perangkat lunak yang kompatibel dengan protokol. Ini tidak mengandung kontrak apa pun di awal. Bob juga akan membutuhkan :


- Dompet Bitcoin untuk mengelola UTXO Anda;
- Koneksi ke node Bitcoin (atau ke server Electrum), sehingga Anda dapat mengidentifikasi UTXO Anda dan menyebarkan transaksi Anda di jaringan.

Sebagai pengingat, **Owned States** dalam RGB merujuk pada UTXO Bitcoin. Oleh karena itu, kita harus selalu dapat mengelola dan menggunakan UTXO dalam transaksi Bitcoin yang menyertakan komitmen kriptografi (`Tapret` atau `Opret`) yang menunjuk ke data RGB.

#### 2) Akuisisi informasi kontrak

Bob kemudian perlu mengambil data kontrak yang dia minati. Data ini dapat beredar melalui saluran apa pun: situs web, email, aplikasi perpesanan... Dalam praktiknya, data-data tersebut dikelompokkan bersama dalam sebuah ***konsinyasi***, yaitu sebuah paket kecil data yang berisi file :


- Genesis**, yang mendefinisikan keadaan awal kontrak;
- **Skema**, yang menjelaskan logika bisnis (tipe yang ketat, skrip validasi, dll.);
- Antarmuka **Interface**, yang mendefinisikan lapisan presentasi (nama bidang, operasi yang dapat diakses);
- Implementasi Antarmuka, yang secara konkret menghubungkan Skema ke Antarmuka.

![RGB-Bitcoin](assets/fr/075.webp)

Ukuran totalnya biasanya hanya beberapa kilobyte, karena setiap komponen umumnya memiliki berat kurang dari 200 byte. Kiriman ini juga dapat disiarkan di Base58, melalui saluran yang tahan sensor (seperti Nostr atau melalui Lightning Network, misalnya), atau sebagai kode QR.

#### 3) Impor dan validasi kontrak

Setelah Bob menerima kiriman, dia mengimpornya ke dalam dompet RGB-nya. Ini kemudian akan :


- Periksa apakah Genesis dan Skema sudah valid;
- Memuat Antarmuka dan Implementasi Antarmuka ;
- Perbarui simpanan data sisi klien Anda.

Bob sekarang dapat melihat aset di dompetnya (meskipun dia belum memilikinya) dan memahami bidang apa saja yang tersedia, operasi apa saja yang mungkin dilakukan... Dia kemudian perlu menghubungi orang yang benar-benar memiliki aset yang akan ditransfer. Dalam contoh kita, ini adalah Alice.

Proses menemukan siapa yang memegang aset RGB tertentu mirip dengan menemukan pembayar Bitcoin. Detail dari koneksi ini bergantung pada penggunaannya (pasar, saluran obrolan pribadi, faktur, penjualan barang dan jasa, gaji...).

#### 4) Menerbitkan faktur

Untuk memulai transfer aset RGB, Bob harus terlebih dahulu menerbitkan faktur. Faktur ini digunakan untuk :


- Beritahu Alice jenis operasi yang akan dilakukan (misalnya, `Transfer` dari antarmuka RGB20);
- Berikan definisi *seal* Bob kepada Alice (yaitu UTXO tempat ia ingin menerima aset);
- Tentukan jumlah bahan aktif yang dibutuhkan (misalnya 100 unit).

Bob menggunakan alat `rgb` pada baris perintah. Misalkan dia menginginkan 100 unit token yang `ContractId`-nya diketahui, ingin mengandalkan `Tapret`, dan menentukan UTXO-nya (`456e3..dfe1:0`):

```bash
bob$ rgb invoice RGB20 100 <ContractId> tapret1st:456e3..dfe1:0
```

Kita akan mencermati lebih dekat struktur faktur RGB di akhir bab ini.

#### 5) Pengiriman faktur

Faktur yang dibuat (misalnya sebagai URL: `rgb:2WBcas9.../RGB20/100+utxob:...`) berisi semua informasi yang dibutuhkan Alice untuk mempersiapkan transfer. Seperti halnya kiriman, ini dapat dikodekan secara ringkas (Base58 atau format lain) dan dikirim melalui aplikasi perpesanan, email, Nostr...

![RGB-Bitcoin](assets/fr/076.webp)

#### 6) Persiapan transaksi di sisi Alice

Alice menerima faktur dari Bob. Di dalam dompet RGB-nya, ia memiliki simpanan yang berisi aset yang akan ditransfer. Untuk membelanjakan UTXO yang berisi aset tersebut, Alice harus terlebih dahulu membuat PSBT (*Transaksi Bitcoin Bertanda Tangan Sebagian*), yaitu transaksi Bitcoin yang belum selesai, dengan menggunakan UTXO yang dimilikinya:

```bash
alice$ wallet construct tx.psbt
```

Transaksi dasar ini (belum ditandatangani untuk saat ini) akan digunakan untuk mengaitkan komitmen kriptografi yang terkait dengan transfer ke Bob. UTXO milik Alice akan dihabiskan, dan pada keluarannya, kita akan menempatkan komitmen `Tapret` atau `Opret` untuk Bob.

#### 7) Pembuatan konsinyasi transfer

Selanjutnya, Alice membangun ***terminal konsinyasi*** (kadang-kadang disebut "konsinyasi transfer") melalui perintah :

```bash
alice$ rgb transfer tx.psbt <invoice> consignment.rgb
```

File `konsinyasi.rgb` yang baru ini berisi file :


- Riwayat lengkap Transisi Negara yang diperlukan untuk memvalidasi aset hingga saat ini (sejak Genesis);
- Transisi Negara baru yang mentransfer aset dari Alice ke Bob, sesuai dengan faktur yang telah diterbitkan Bob;
- Transaksi Bitcoin yang tidak lengkap (*transaksi saksi*) (`tx.psbt`), yang menghabiskan Segel Sekali Pakai milik Alice, dimodifikasi untuk menyertakan komitmen kriptografi kepada Bob.

Pada tahap ini, transaksi belum disiarkan di jaringan Bitcoin. Konsinyasi ini lebih besar daripada konsinyasi dasar, karena mencakup seluruh riwayat (*rantai bukti*) untuk membuktikan keabsahan aset.

#### 8) Bob memeriksa dan menerima kiriman

Alice mengirimkan **kiriman terminal** ini kepada Bob. Bob kemudian akan:


- Periksa keabsahan Transisi Negara (pastikan riwayatnya konsisten, aturan kontrak dipatuhi, dll.);
- Tambahkan ke simpanan lokal Anda;
- Mungkin membuat tanda tangan (`sig:...`) pada kiriman, untuk membuktikan bahwa kiriman tersebut telah diperiksa dan disetujui (terkadang disebut "*payslip*").

```bash
bob$ rgb accept consignment.rgb
sig:DbwzvSu4BZU81jEpE9FVZ3xjcyuTKWWy2gmdnaxtACrS
```

![RGB-Bitcoin](assets/fr/077.webp)

#### 9) Opsi: Bob mengirimkan konfirmasi kembali ke Alice (*slip gaji*)

Jika Bob mau, dia bisa mengirimkan tanda tangan ini kembali ke Alice. Ini menunjukkan:


- Bahwa ia mengakui transisi tersebut valid;
- Bahwa ia menyetujui transaksi Bitcoin disiarkan.

Hal ini tidak wajib dilakukan, tetapi dapat memberikan jaminan kepada Alice bahwa tidak akan ada perselisihan di kemudian hari atas transfer tersebut.

#### 10) Alice menandatangani dan mempublikasikan transaksi

Alice kemudian bisa :


- Periksa tanda tangan Bob (`rgb check <sig>`);
- Tanda tangani *transaksi saksi* yang masih dalam bentuk PSBT (`tanda dompet`);
- Publikasikan transaksi saksi di jaringan Bitcoin (`-publish`).

```bash
alice$ rgb check <sig>
alice$ wallet sign —publish tx.psbt
```

![RGB-Bitcoin](assets/fr/078.webp)

Setelah dikonfirmasi, transaksi ini menandai berakhirnya transfer. Bob menjadi pemilik baru aset tersebut: dia sekarang memiliki Status Milik yang menunjuk ke UTXO yang dia kendalikan, dibuktikan dengan adanya komitmen dalam transaksi.

Sebagai rangkuman, berikut ini adalah proses transfer secara lengkap:

![RGB-Bitcoin](assets/fr/079.webp)

### Keuntungan dari transfer RGB


- Kerahasiaan** :

Hanya Alice dan Bob yang memiliki akses ke semua data State Transition. Mereka bertukar informasi ini di luar blockchain, melalui pengiriman. Komitmen kriptografi dalam transaksi Bitcoin tidak mengungkapkan jenis aset atau jumlahnya, yang menjamin kerahasiaan yang jauh lebih besar daripada sistem token on-chain lainnya.


- Validasi dari sisi pelanggan**:

Bob dapat memeriksa konsistensi transfer dengan membandingkan *kiriman* dengan *pengirim* dalam blockchain Bitcoin. Dia tidak memerlukan validasi pihak ketiga. Alice tidak perlu mempublikasikan riwayat lengkap pada blockchain, yang mengurangi beban pada protokol dasar dan meningkatkan kerahasiaan.


- Atomisitas yang disederhanakan**:

Pertukaran yang kompleks (pertukaran atomik antara BTC dan aset RGB, misalnya) dapat dilakukan dalam satu transaksi, sehingga tidak memerlukan skrip HTLC atau PTLC. Jika perjanjian tidak disiarkan, semua orang dapat menggunakan kembali UTXO mereka dengan cara lain.

### Diagram ringkasan transfer

Sebelum melihat faktur secara lebih detail, berikut ini adalah diagram ringkasan dari keseluruhan aliran transfer RGB:


- Bob memasang dompet RGB dan mendapatkan konsinyasi kontrak awal;
- Bob menerbitkan faktur yang menyebutkan UTXO tempat menerima aset;
- Alice menerima faktur, membuat PSBT, dan menghasilkan konsinyasi terminal;
- Bob menerimanya, memeriksa, menambahkan data ke dalam simpanannya, dan menandatangani (*slip gaji*) jika perlu;
- Alice mempublikasikan transaksi tersebut di jaringan Bitcoin;
- Konfirmasi transaksi membuat transfer menjadi resmi.

![RGB-Bitcoin](assets/fr/080.webp)

Transfer ini menggambarkan semua kekuatan dan fleksibilitas protokol RGB: pertukaran pribadi, divalidasi di sisi klien, berlabuh secara minimal dan diam-diam di blockchain Bitcoin, dan mempertahankan keamanan protokol yang terbaik (tidak ada risiko pembelanjaan ganda). Hal ini membuat RGB menjadi ekosistem yang menjanjikan untuk transfer nilai yang lebih rahasia dan terukur daripada blockchain yang dapat diprogram secara on-chain.

### Faktur RGB

Pada bagian ini, kami akan menjelaskan secara rinci bagaimana **invoice** bekerja dalam ekosistem RGB dan bagaimana mereka memungkinkan operasi (khususnya transfer) dilakukan dengan kontrak. Pertama, kita akan melihat pengidentifikasi yang digunakan, kemudian bagaimana pengidentifikasi tersebut dikodekan, dan akhirnya pada struktur faktur yang dinyatakan sebagai URL (format yang cukup berguna untuk digunakan di dompet).

#### Pengidentifikasi dan pengkodean

Pengenal unik ditentukan untuk setiap elemen berikut ini:


- Kontrak RGB;
- Skema (logika bisnis) nya;
- Antarmuka dan Implementasi Antarmuka ;
- Asetnya (token, NFT, dll.),

Keunikan ini sangat penting, karena setiap komponen sistem harus dapat dibedakan. Sebagai contoh, kontrak X tidak boleh tertukar dengan kontrak Y, dan dua antarmuka yang berbeda (RGB20 vs RGB21, misalnya) harus memiliki pengenal yang berbeda.

Untuk membuat pengenal ini efisien (ukurannya kecil) dan mudah dibaca, kami menggunakan :


- Pengkodean Base58, yang menghindari penggunaan karakter yang membingungkan (misalnya `0` dan huruf `O`) dan menyediakan string yang relatif pendek;
- Awalan yang menunjukkan sifat pengenal, biasanya dalam bentuk `rgb:` atau URN yang serupa.

Sebagai contoh, `ContractId` dapat diwakili oleh sesuatu seperti :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Awalan `rgb:` mengonfirmasi bahwa ini adalah pengenal RGB, dan bukan tautan HTTP atau protokol lainnya. Berkat awalan ini, dompet dapat menafsirkan string dengan benar.

#### Segmentasi pengenal

Pengidentifikasi RGB sering kali cukup panjang, karena keamanan (kriptografi) yang mendasarinya mungkin memerlukan bidang 256 bit atau lebih. Untuk memudahkan pembacaan dan verifikasi oleh manusia, kami memenggal string ini menjadi beberapa blok yang dipisahkan oleh tanda hubung (`-`). Jadi, alih-alih memiliki string karakter yang panjang dan tidak terputus, kita membaginya menjadi beberapa blok yang lebih pendek. Praktik ini biasa dilakukan pada kartu kredit atau nomor telepon, dan ini juga berlaku di sini untuk memudahkan verifikasi. Jadi, misalnya, pengguna atau mitra dapat diberitahu: "*Tolong periksa apakah blok ketiga adalah `9GEgnyMj7`*", daripada harus membandingkan semuanya sekaligus. Blok terakhir sering digunakan sebagai **checksum**, untuk memiliki sistem pendeteksi kesalahan atau kesalahan pengetikan.

Sebagai contoh, `ContractId` dalam base58 yang dikodekan dan disegmentasi dapat berupa :

```txt
2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Setiap tanda hubung memecah string menjadi beberapa bagian. Hal ini tidak memengaruhi semantik kode, hanya penyajiannya saja.

#### Menggunakan URL untuk faktur

Faktur RGB disajikan sebagai URL. Ini berarti dapat diklik atau dipindai (sebagai kode QR), dan dompet dapat langsung menafsirkannya untuk melakukan transaksi. Kesederhanaan interaksi ini berbeda dengan beberapa sistem lain yang mengharuskan Anda untuk menyalin dan menempelkan berbagai data ke dalam bidang yang berbeda dalam perangkat lunak.

Faktur untuk token yang dapat dipertukarkan (misalnya token RGB20) mungkin terlihat seperti ini:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Mari kita analisis URL ini:


- `rgb:`** (awalan): mengindikasikan sebuah tautan yang menggunakan protokol RGB (analog dengan `http:` atau `bitcoin:` dalam konteks lain);
- `2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX`**: merepresentasikan `ContractId` token yang ingin Anda manipulasi;
- `/RGB20/100`**: mengindikasikan bahwa antarmuka `RGB20` digunakan dan 100 unit aset diminta. Sintaksnya adalah: `/Interface/jumlah` ;
- `+utxob:`**: menentukan bahwa informasi tentang UTXO penerima (atau, lebih tepatnya, definisi Segel Sekali Pakai) ditambahkan;
- `egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb`**: ini adalah UTXO yang *dibutakan* (atau definisi segel). Dengan kata lain, Bob telah menutupi UTXO yang sebenarnya, sehingga pengirim (Alice) tidak tahu alamat yang sebenarnya. Dia hanya tahu bahwa ada segel yang valid yang mengacu pada UTXO yang dikendalikan oleh Bob.

Fakta bahwa semuanya dapat dimasukkan ke dalam satu URL membuat hidup lebih mudah bagi pengguna: klik atau pindai sederhana di dompet, dan operasi siap dijalankan.

Kita dapat membayangkan sistem di mana ticker sederhana (misalnya `USDT`) digunakan sebagai pengganti `ContractId`. Akan tetapi, hal ini akan menimbulkan masalah besar dalam hal kepercayaan dan keamanan: ticker bukanlah sebuah referensi yang unik (beberapa kontrak dapat mengklaim sebagai `USDT`). Dengan RGB, kami menginginkan pengenal kriptografi yang unik dan tidak ambigu. Oleh karena itu, kami menggunakan string 256-bit, yang dikodekan dalam base58 dan tersegmentasi. Pengguna mengetahui bahwa ia memanipulasi kontrak dengan ID `2WBcas9-yjz...` dan bukan yang lainnya.

#### Parameter URL tambahan

Anda juga dapat menambahkan parameter tambahan ke URL, dengan cara yang sama seperti pada HTTP, seperti :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb?sig=6kzbKKffP6xftkxn9UP8gWqiC41W16wYKE5CYaVhmEve
```


- `?sig=...`: mewakili, misalnya, tanda tangan yang terkait dengan faktur, yang dapat diverifikasi oleh beberapa dompet;
- Jika dompet tidak mengelola tanda tangan ini, maka dompet akan mengabaikan parameter ini.

Mari kita ambil contoh kasus NFT melalui antarmuka RGB21. Sebagai contoh, kita bisa memiliki :

```txt
rgb:7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK/RGB21/DbwzvSu-4BZU81jEp-E9FVZ3xj-cyuTKWWy-2gmdnaxt-ACrS+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Di sini kita lihat :


- `rgb:`**: Awalan URL ;
- `7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK`**: ID Kontrak (NFT);
- rGB21**: antarmuka untuk aset yang tidak dapat dipertukarkan (NFT);
- `DbwzvSu-4BZU81jEp-...`**: referensi eksplisit ke bagian unik NFT, misalnya hash dari gumpalan data (media, metadata...);
- `+utxob:egXsFnw-...`**: definisi segel.

Idenya sama: mengirimkan sebuah tautan unik yang dapat ditafsirkan oleh wallet, dengan jelas mengidentifikasi aset unik yang akan ditransfer.

#### Operasi lain melalui URL

URL RGB tidak hanya digunakan untuk meminta transfer. URL ini juga dapat mengkodekan operasi yang lebih canggih, seperti menerbitkan token baru (*penerbitan*). Sebagai contoh:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/issue/100000+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Di sini kami menemukan :


- `rgb:` : protokol ;
- `2WBcas9-...`: ID Kontrak;
- `/RGB20/issue/100000`: mengindikasikan bahwa Anda ingin menggunakan transisi "*Issue*" untuk membuat 100.000 token tambahan;
- `+utxob:`: definisi segel.

Sebagai contoh, dompet tersebut mungkin bertuliskan: "Saya telah diminta untuk melakukan operasi `masalah` dari antarmuka `RGB20`, dengan kontrak ini dan itu, untuk 100.000 unit, untuk kepentingan Segel Sekali Pakai ini dan itu.*"

Sekarang, setelah kita melihat elemen utama pemrograman RGB, saya akan mengajak Anda membaca bab berikutnya mengenai cara menyusun kontrak RGB.

## Menyusun kontrak pintar

<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>

![video](https://youtu.be/GRwS-NvWF3I)

Pada bab ini, kita akan melakukan pendekatan langkah demi langkah untuk menulis kontrak, menggunakan alat bantu baris perintah `rgb`. Tujuannya adalah untuk menunjukkan cara menginstal dan memanipulasi CLI, mengkompilasi **Skema**, mengimpor **Interface** dan **Implementasi Antarmuka**, kemudian menerbitkan (*issue*) aset. Kita juga akan melihat logika yang mendasarinya, termasuk kompilasi dan validasi state. Pada akhir bab ini, Anda seharusnya dapat mereproduksi proses tersebut dan membuat kontrak RGB Anda sendiri.

Sebagai pengingat, logika internal RGB didasarkan pada pustaka Rust yang dapat Anda, sebagai pengembang, impor ke dalam proyek Anda untuk mengelola bagian Validasi Sisi Klien. Selain itu, tim Asosiasi LNP/BP sedang mengerjakan binding untuk bahasa lain, tetapi ini belum selesai. Selain itu, entitas lain seperti Bitfinex sedang mengembangkan tumpukan integrasi mereka sendiri (kita akan membicarakannya di 2 bab terakhir kursus ini). Oleh karena itu, untuk saat ini, CLI `rgb` adalah referensi resmi, meskipun masih relatif belum disempurnakan.

### Instalasi dan presentasi alat rgb

Perintah utamanya hanya disebut `rgb`. Perintah ini didesain untuk mengingatkan kita pada `git`, dengan serangkaian sub-perintah untuk memanipulasi kontrak, memintanya, menerbitkan aset, dan sebagainya. Dompet Bitcoin saat ini belum terintegrasi, namun akan segera hadir dalam versi berikutnya (0.11). Versi berikutnya ini akan memungkinkan pengguna untuk membuat dan mengelola dompet mereka (melalui deskriptor) secara langsung dari `rgb`, termasuk pembuatan PSBT, kompatibilitas dengan perangkat keras eksternal (mis. Dompet perangkat keras) untuk penandatanganan, dan interoperabilitas dengan perangkat lunak seperti Sparrow. Ini akan menyederhanakan seluruh skenario penerbitan dan transfer aset.

#### Pemasangan melalui Kargo

Kami memasang alat ini di Karat dengan :

```bash
cargo install rgb-contracts --all-features
```

(Catatan: crate bernama `rgb-contracts`, dan perintah yang terinstal akan diberi nama `rgb`. Jika sebuah peti bernama `rgb` sudah ada, mungkin telah terjadi tabrakan, oleh karena itu namanya)

Instalasi mengkompilasi sejumlah besar dependensi (misalnya penguraian perintah, integrasi Electrum, manajemen bukti tanpa pengetahuan, dll.).

Setelah instalasi selesai, file :

```bash
rgb
```

Menjalankan `rgb` (tanpa argumen) akan menampilkan daftar sub-perintah yang tersedia, seperti `interfaces`, `schema`, `import`, `export`, `issue`, `invoice`, `transfer`, dan lain-lain. Anda dapat mengubah direktori penyimpanan lokal (tempat penyimpanan yang menyimpan semua log, skema dan implementasi), memilih jaringan (testnet, mainnet) atau mengkonfigurasi server Electrum Anda.

![RGB-Bitcoin](assets/fr/081.webp)

#### Gambaran umum pertama tentang kontrol

Apabila Anda menjalankan perintah berikut ini, Anda akan melihat bahwa antarmuka `RGB20` sudah terintegrasi secara default:

```bash
rgb interfaces
```

Jika antarmuka ini tidak terintegrasi, kloning file :

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Kompilasi itu:

```bash
cargo run
```

Kemudian, impor antarmuka pilihan Anda:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-Bitcoin](assets/fr/082.webp)

Di sisi lain, kami diberitahu bahwa belum ada skema yang diimpor ke dalam perangkat lunak. Juga tidak ada kontrak dalam simpanan. Untuk melihatnya, jalankan perintah :

```bash
rgb schemata
```

Anda kemudian dapat mengkloning repositori untuk mengambil skema tertentu:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-Bitcoin](assets/fr/083.webp)

Repositori ini berisi, dalam direktori `src/`, beberapa file Rust (misalnya `nia.rs`) yang mendefinisikan skema (NIA untuk "*Non Inflatable Asset*", UDA untuk "*Unique Digital Asset*", dll.). Untuk mengkompilasi, Anda kemudian dapat menjalankan file :

```bash
cd rgb-schemata
cargo run
```

Ini menghasilkan beberapa file `.rgb` dan `.rgba` yang sesuai dengan skema yang dikompilasi. Sebagai contoh, Anda akan menemukan `NonInflatableAsset.rgb`.

#### Mengimpor Skema dan Implementasi Antarmuka

Anda sekarang dapat mengimpor skematik ke dalam `rgb`:

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-Bitcoin](assets/fr/084.webp)

Ini akan menambahkannya ke simpanan lokal. Jika kita menjalankan perintah berikut, kita akan melihat bahwa skemanya sekarang muncul:

```bash
rgb schemata
```

### Pembuatan kontrak (penerbitan)

Ada dua pendekatan untuk membuat aset baru:


- Entah kita menggunakan skrip atau kode di Rust yang membangun Kontrak dengan mengisi bidang skema (negara global, Negara Milik, dll.) dan menghasilkan file `.rgb` atau `.rgba`;
- Atau gunakan sub-perintah `issue` secara langsung, dengan file YAML (atau TOML) yang menjelaskan properti token.

Anda dapat menemukan contoh di Rust dalam folder `examples`, yang mengilustrasikan bagaimana Anda membuat `ContractBuilder`, mengisi `global state` (nama aset, ticker, pasokan, tanggal, dll.), menentukan Owned State (ke mana UTXO ditugaskan), kemudian mengkompilasi semua ini menjadi *contract consignment* yang dapat Anda ekspor, validasi, dan impor ke dalam simpanan.

Cara lainnya adalah mengedit file YAML secara manual untuk menyesuaikan `ticker`, `nama`, `supply`, dan seterusnya. Misalkan file tersebut bernama `RGB20-demo.yaml`. Anda dapat menentukan ekstensi :


- `spec`: ticker, nama, presisi ;
- 'istilah': bidang untuk pemberitahuan hukum ;
- `issuedSupply`: jumlah token yang diterbitkan;
- 'assignments': menunjukkan Segel Sekali Pakai (*definisi segel*) dan jumlah yang dibuka.

Berikut ini adalah contoh file YAML yang akan dibuat:

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-Bitcoin](assets/fr/085.webp)

Kemudian, jalankan saja perintah :

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-Bitcoin](assets/fr/086.webp)

Dalam kasus saya, pengenal skema unik (harus diapit dengan tanda kutip tunggal) adalah `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` dan saya tidak mencantumkan penerbit apa pun. Jadi pesanan saya adalah :

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

Jika Anda tidak mengetahui ID skema, jalankan perintah :

```bash
rgb schemata
```

CLI menjawab bahwa sebuah kontrak baru telah diterbitkan dan ditambahkan ke dalam simpanan. Jika kita mengetikkan perintah berikut, kita akan melihat bahwa sekarang ada sebuah kontrak tambahan, yang sesuai dengan kontrak yang baru saja diterbitkan:

```bash
rgb contracts
```

![RGB-Bitcoin](assets/fr/087.webp)

Kemudian, perintah selanjutnya menampilkan status global (nama, ticker, pasokan...) dan daftar Status Milik, yaitu alokasi (misalnya, 1 juta token `PBN` yang didefinisikan dalam UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-Bitcoin](assets/fr/088.webp)

### Ekspor, impor, dan validasi

Untuk berbagi kontrak ini dengan pengguna lain, kontrak ini dapat diekspor dari simpanan ke file :

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-Bitcoin](assets/fr/089.webp)

File `myContractPBN.rgb` dapat diteruskan ke pengguna lain, yang dapat menambahkannya ke simpanannya dengan perintah :

```bash
rgb import myContractPBN.rgb
```

Pada saat impor, jika ini adalah *kiriman kontrak* yang sederhana, kita akan mendapatkan pesan "`Importing consignment rgb`". Jika ini adalah *state transition consignment* yang lebih besar, perintahnya akan berbeda (`rgb accept`).

Untuk memastikan validitas, Anda juga dapat menggunakan fungsi validasi lokal. Misalnya, Anda dapat menjalankan :

```bash
rgb validate myContract.rgb
```

#### Penggunaan, verifikasi, dan tampilan simpanan

Sebagai pengingat, stash adalah inventaris lokal dari skema, antarmuka, implementasi, dan kontrak (Genesis + transisi). Setiap kali Anda menjalankan "impor", Anda menambahkan sebuah elemen ke dalam stash. Stash ini dapat dilihat secara detail dengan perintah :

```bash
rgb dump
```

![RGB-Bitcoin](assets/fr/090.webp)

Ini akan menghasilkan folder dengan rincian seluruh simpanan.

### Transfer dan PSBT

Untuk melakukan transfer, Anda perlu memanipulasi dompet Bitcoin lokal untuk mengelola komitmen `Tapret` atau `Opret`.

#### Membuat faktur

Dalam banyak kasus, interaksi antara peserta dalam kontrak (misalnya Alice dan Bob) terjadi melalui pembuatan faktur. Jika Alice ingin Bob melakukan sesuatu (transfer token, penerbitan ulang, tindakan dalam DAO, dll.), Alice membuat faktur yang merinci instruksinya kepada Bob. Jadi, kita memiliki :


- Alice** (penerbit faktur);
- Bob** (yang menerima dan melaksanakan faktur).

Tidak seperti ekosistem lainnya, faktur RGB tidak terbatas pada pengertian pembayaran. Faktur ini dapat menyematkan permintaan apa pun yang terkait dengan kontrak: mencabut kunci, memberikan suara, membuat ukiran (*engraving*) pada NFT, dll. Operasi yang sesuai dapat dijelaskan dalam antarmuka kontrak. Operasi yang sesuai dapat dijelaskan dalam antarmuka kontrak.

Perintah berikut ini menghasilkan faktur RGB:

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

Dengan:


- `$KONTRAK`: Pengenal kontrak (*ContractId*) ;
- `$INTERFACE`: antarmuka yang akan digunakan (mis. `RGB20`);
- `$ACTION`: nama operasi yang ditentukan dalam antarmuka (untuk transfer token yang dapat dipertukarkan, ini bisa berupa "Transfer"). Jika antarmuka sudah menyediakan tindakan default, Anda tidak perlu memasukkannya lagi di sini;
- `$STATE`: data status yang akan ditransfer (misalnya, jumlah token jika token yang dapat ditukar ditransfer);
- `$SEAL`: Segel sekali pakai penerima (Alice), yaitu referensi eksplisit ke UTXO. Bob akan menggunakan informasi ini untuk membuat transaksi saksi, dan keluaran yang sesuai akan menjadi milik Alice (dalam bentuk *blinded UTXO* atau tidak terenkripsi).

Misalnya, dengan perintah berikut ini

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

CLI akan menghasilkan faktur seperti :

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

Ini dapat dikirimkan ke Bob melalui saluran apa pun (teks, kode QR, dll.).

#### Melakukan transfer

Untuk mentransfer dari faktur ini :


- Bob (yang menyimpan token dalam simpanannya) memiliki dompet Bitcoin. Dia perlu menyiapkan transaksi Bitcoin (dalam bentuk PSBT, misalnya `tx.psbt`) yang membelanjakan UTXO di mana token RGB yang diperlukan berada, ditambah satu UTXO untuk mata uang (penukaran);
- Bob menjalankan perintah berikut:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- Ini menghasilkan file `konsinyasi.rgb` yang berisi file :
 - Riwayat transisi membuktikan kepada Alice bahwa token tersebut asli;
 - Transisi baru yang mentransfer token ke Segel Sekali Pakai Alice;
 - Transaksi saksi (tidak ditandatangani).
- Bob mengirimkan file `consignment.rgb` ini ke Alice (melalui email, server berbagi atau protokol RGB-RPC, Storm, dll.);
- Alice menerima `kiriman.rgb` dan menerimanya dalam simpanannya sendiri:

```bash
alice$ rgb accept consignment.rgb
```


- CLI memeriksa validitas transisi dan menambahkannya ke simpanan Alice. Jika tidak valid, perintah akan gagal dengan pesan kesalahan yang mendetail. Jika tidak, perintah tersebut berhasil, dan melaporkan bahwa contoh transaksi belum disiarkan di jaringan Bitcoin (Bob menunggu lampu hijau dari Alice);
- Sebagai konfirmasi, perintah `accept` mengembalikan tanda tangan (*payslip*) yang dapat dikirimkan Alice kepada Bob untuk menunjukkan kepadanya bahwa dia telah memvalidasi *kiriman*;
- Bob kemudian dapat menandatangani dan mempublikasikan (`-publish`) transaksi Bitcoin-nya:

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- Segera setelah transaksi ini dikonfirmasi secara on-chain, kepemilikan aset dianggap berpindah ke Alice. Dompet Alice, yang memantau penambangan transaksi, melihat Status Milik baru muncul di simpanannya.

Dalam bab berikutnya, kita akan melihat lebih dekat pada pengintegrasian RGB ke dalam Lightning Network.

## RGB pada Jaringan Petir

<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>

![video](https://youtu.be/mqCupTlDbA0)

Dalam bab ini, saya mengusulkan untuk memeriksa bagaimana RGB dapat digunakan dalam Lightning Network, untuk mengintegrasikan dan memindahkan aset RGB (token, NFT, dll.) melalui saluran pembayaran off-chain.

Ide dasarnya adalah bahwa transisi status RGB (*State Transition*) dapat dikomitmenkan ke dalam transaksi Bitcoin yang, pada gilirannya, dapat tetap berada di luar rantai sampai saluran Lightning ditutup. Jadi, setiap kali saluran diperbarui, transisi status RGB yang baru dapat dimasukkan ke dalam transaksi baru yang berkomitmen, yang kemudian membatalkan transisi lama. Dengan cara ini, saluran Lightning dapat digunakan untuk mentransfer aset RGB, dan dapat dirutekan dengan cara yang sama seperti pembayaran Lightning konvensional.

### Pembuatan saluran dan pendanaan

Untuk membuat saluran Lightning yang membawa aset RGB, kita memerlukan dua elemen:


- Pendanaan Bitcoin untuk membuat multisig 2/2 saluran (UTXO dasar untuk saluran);
- Pendanaan RGB, yang mengirimkan aset ke multisig yang sama.

Dalam istilah Bitcoin, transaksi pendanaan harus ada untuk menentukan referensi UTXO, meskipun hanya berisi sejumlah kecil satoshi (ini hanya masalah setiap output dalam transaksi komitmen di masa depan tetap berada di atas batas debu). Misalnya, Alice dapat memutuskan untuk menyediakan 10 ribu sat dan 500 USDT (diterbitkan sebagai aset RGB). Pada transaksi pendanaan, kita menambahkan komitmen (`Opret` atau `Tapret`) yang mengaitkan transisi status RGB.

![RGB-Bitcoin](assets/fr/091.webp)

Setelah transaksi pendanaan disiapkan (tetapi belum disiarkan), transaksi komitmen dibuat sehingga salah satu pihak dapat menutup saluran secara sepihak kapan saja. Transaksi ini menyerupai transaksi komitmen klasik Lightning, kecuali bahwa kami menambahkan output tambahan yang berisi jangkar RGB (OP_RETURN atau Taproot) yang terhubung ke transisi status baru.

Transisi keadaan RGB kemudian memindahkan aset dari multisig 2/2 dari pendanaan ke output dari transaksi komitmen. Keuntungan dari proses ini adalah bahwa keamanan status RGB sama persis dengan mekanisme hukuman Lightning: jika Bob menyiarkan status saluran yang lama, Alice dapat menghukumnya dan menghabiskan hasilnya, untuk memulihkan sat dan token RGB. Oleh karena itu, insentifnya bahkan lebih kuat daripada di saluran Lightning tanpa aset RGB, karena penyerang tidak hanya dapat kehilangan sat, tetapi juga aset RGB saluran.

Oleh karena itu, transaksi komitmen yang ditandatangani oleh Alice dan dikirim ke Bob akan terlihat seperti ini:

![RGB-Bitcoin](assets/fr/092.webp)

Dan transaksi komitmen yang menyertainya, yang ditandatangani oleh Bob dan dikirim ke Alice, akan terlihat seperti ini:

![RGB-Bitcoin](assets/fr/093.webp)

### Pembaruan saluran

Ketika pembayaran terjadi antara dua peserta saluran (atau mereka ingin mengubah alokasi aset), mereka membuat sepasang transaksi komitmen baru. Jumlah dalam sat pada setiap output mungkin atau mungkin tidak tetap tidak berubah, tergantung pada implementasinya, karena peran utamanya adalah untuk memungkinkan pembangunan UTXO yang valid. Di sisi lain, output OP_RETURN (atau Taproot) harus dimodifikasi untuk memuat jangkar RGB baru, yang mewakili distribusi aset baru di dalam saluran.

Sebagai contoh, jika Alice mentransfer 30 USDT ke Bob di dalam channel, transisi keadaan baru akan mencerminkan saldo 400 USDT untuk Alice dan 100 USDT untuk Bob. Transaksi komit ditambahkan ke (atau dimodifikasi oleh) jangkar OP_RETURN/Taproot untuk menyertakan transisi ini. Perhatikan bahwa, dari sudut pandang RGB, input untuk transisi tetap merupakan multisig awal (di mana aset on-chain benar-benar dialokasikan sampai saluran ditutup). Hanya output (alokasi) RGB yang berubah, tergantung pada redistribusi yang diputuskan.

Transaksi komitmen yang ditandatangani oleh Alice, siap didistribusikan oleh Bob:

![RGB-Bitcoin](assets/fr/094.webp)

Transaksi komitmen yang ditandatangani oleh Bob, siap didistribusikan oleh Alice:

![RGB-Bitcoin](assets/fr/095.webp)

### Manajemen HTLC

Pada kenyataannya, Lightning Network memungkinkan pembayaran untuk dirutekan melalui beberapa saluran, menggunakan HTLC (*Hashed Time-Locked Contracts*). Sama halnya dengan RGB: untuk setiap pembayaran yang transit melalui saluran, output HTLC ditambahkan ke transaksi yang dilakukan, dan alokasi RGB yang terkait dengan HTLC ini. Dengan demikian, siapa pun yang membelanjakan output HTLC (berkat rahasia atau setelah berakhirnya timelock) akan mendapatkan kembali sat dan aset RGB yang terkait. Di sisi lain, Anda tentu saja harus memiliki cukup uang tunai di jalan dalam hal sat dan aset RGB.

![RGB-Bitcoin](assets/fr/096.webp)

Oleh karena itu, pengoperasian RGB pada Lightning harus dipertimbangkan secara paralel dengan pengoperasian Lightning Network itu sendiri. Jika Anda ingin mempelajari subjek ini lebih dalam, saya sangat menyarankan Anda untuk melihat kursus pelatihan komprehensif lainnya:

https://planb.network/courses/lnp201
### Peta kode RGB

Terakhir, sebelum beralih ke bagian berikutnya, saya ingin memberikan gambaran umum tentang kode yang digunakan dalam RGB. Protokol ini didasarkan pada seperangkat pustaka Rust dan spesifikasi sumber terbuka. Berikut ini adalah gambaran umum dari repositori dan crate utama:

![RGB-Bitcoin](assets/fr/097.webp)

#### Validasi Sisi Klien


- Repositori**: [validasi_sisi_klien](https://github.com/LNP-BP/client_side_validation)
- Peti ** : [validasi sisi klien](https://crates.io/crates/client_side_validation), [segel sekali pakai](https://crates.io/crates/single_use_seals)

Manajemen validasi off-chain dan logika Segel Sekali Pakai.

#### Komitmen Bitcoin Deterministik (DBC)


- Repositori**: [bp-core](https://github.com/BP-WG/bp-core)
- Peti**: [bp-dbc](https://crates.io/crates/bp-dbc)

Manajemen penahan deterministik dalam transaksi Bitcoin (Tapret, OP_RETURN, dll.).

#### Komitmen Multi Protokol (MPC)


- Repositori**: [validasi_sisi_klien](https://github.com/LNP-BP/client_side_validation)
- Peti ** : [commit_verify](https://crates.io/crates/commit_verify)

Kombinasi dan integrasi berbagai keterlibatan dengan protokol yang berbeda.

#### Tipe Ketat & Pengkodean Ketat


- Spesifikasi**: [situs web strict-types.org](https://www.strict-types.org/)
- Repositori**: [strict-types](https://github.com/strict-types/strict-types), [strict-encoding](https://github.com/strict-types/strict-encoding)
- Peti ** : [strict_types](https://crates.io/crates/strict_types), [strict_encoding](https://crates.io/crates/strict_encoding)

Sistem pengetikan yang ketat dan serialisasi deterministik yang digunakan untuk validasi sisi klien.

#### Inti RGB


- Repositori**: [rgb-core](https://github.com/RGB-WG/rgb-core)
- Peti**: [rgb-core](https://crates.io/crates/rgb-core)

Inti protokol, yang mencakup logika utama validasi RGB.

#### Perpustakaan & Dompet Standar RGB


- Repositori**: [rgb-std](https://github.com/RGB-WG/rgb-std)
- Peti ** : [rgb-std](https://crates.io/crates/rgb-std)

Implementasi standar, manajemen simpanan dan dompet.

#### RGB CLI


- Repositori**: [rgb](https://github.com/RGB-WG/rgb)
- Peti**: [rgb-cli](https://crates.io/crates/rgb-cli), [rgb-wallet](https://crates.io/crates/rgb-wallet)

CLI `rgb` dan dompet peti, untuk manipulasi baris perintah pada kontrak.

#### Skema RGB


- Repositori**: [rgb-schemata](https://github.com/RGB-WG/rgb-schemata/)

Berisi contoh-contoh skema (NIA, UDA, dll.) dan implementasinya.

#### ALuVM


- Info** : [aluvm.org](https://www.aluvm.org/)
- Repositori**: [aluvm-spec](https://github.com/AluVM/aluvm-spec), [alure](https://github.com/AluVM/alure)
- Peti **: [aluvm](https://crates.io/crates/aluvm), [aluasm](https://crates.io/crates/aluasm)

Mesin virtual berbasis registri yang digunakan untuk menjalankan skrip validasi.

#### Protokol Bitcoin - BP


- Repositori** : [bp-core](https://github.com/BP-WG/bp-core), [bp-std](https://github.com/BP-WG/bp-std), [bp-wallet](https://github.com/BP-WG/bp-wallet)

Pengaya untuk mendukung protokol Bitcoin (transaksi, bypass, dll.).

#### Komputasi Deterministik di Mana-mana - UBIDECO


- Repositori**: [UBIDECO](https://github.com/UBIDECO)

Ekosistem yang terkait dengan pengembangan deterministik sumber terbuka.

# Membangun di atas RGB

<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>

## DIBA dan proyek Bitmask

<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>

![video](https://youtu.be/nbUtV8GOR_U)

Bagian terakhir dari kursus ini didasarkan pada presentasi yang dibuat oleh berbagai pembicara pada pelatihan RGB. Bagian ini mencakup testimoni dan refleksi tentang RGB dan ekosistemnya, serta presentasi alat dan proyek berdasarkan protokol. Bab pertama ini dimoderatori oleh Hunter Beast, dan dua bab berikutnya oleh Frederico Tenga.

### Dari JavaScript ke Rust, dan masuk ke dalam ekosistem Bitcoin

Pada awalnya, Hunter Beast bekerja terutama dalam JavaScript. Kemudian dia menemukan **Rust**, yang sintaksnya tampak tidak menarik dan membuat frustasi pada awalnya. Namun, dia kemudian menghargai kekuatan bahasa ini, kontrol terhadap memori (*heap* dan *stack*), dan keamanan serta performa yang menyertainya. Dia menekankan bahwa Rust adalah tempat pelatihan yang sangat baik untuk pemahaman mendalam tentang cara kerja komputer.

Hunter Beast menceritakan latar belakangnya dalam berbagai proyek dalam ekosistem *altcoin*, seperti Ethereum (dengan Solidity, TypeScript, dll.), dan kemudian Filecoin. Dia menjelaskan bahwa dia awalnya terkesan dengan beberapa protokol, tetapi akhirnya merasa kecewa dengan sebagian besar protokol tersebut, tidak terkecuali karena tokenomics mereka. Dia mengecam insentif keuangan yang meragukan, penciptaan token yang menggelembung yang melemahkan investor, dan aspek yang berpotensi eksploitatif dari proyek-proyek ini. Jadi, dia akhirnya mengadopsi sikap **Bitcoin maximalist**, paling tidak karena beberapa orang membuka matanya pada mekanisme ekonomi Bitcoin yang lebih sehat, dan pada kekuatan sistem ini.

### Daya tarik RGB dan membangun di atas lapisan

Apa yang membuatnya yakin akan relevansi Bitcoin, menurutnya, adalah penemuan RGB dan konsep lapisan. Dia percaya bahwa fungsi yang ada pada blockchain lain dapat direproduksi pada lapisan yang lebih tinggi, di atas Bitcoin, tanpa mengubah protokol dasar.

Pada bulan Februari 2022, ia bergabung dengan **DIBA** untuk bekerja secara khusus pada RGB, dan khususnya pada dompet **Bitmask**. Pada saat itu, Bitmask masih dalam versi 0.01 dan menjalankan RGB pada versi 0.4, hanya untuk pengelolaan token tunggal. Dia mencatat bahwa ini kurang berorientasi pada penyimpanan sendiri dibandingkan saat ini, karena logikanya sebagian berbasis server. Sejak saat itu, arsitekturnya telah berevolusi ke arah model ini, yang sangat dihargai oleh para pengguna bitcoin.

### Dasar-dasar protokol RGB

Protokol **RGB** adalah perwujudan terbaru dan tercanggih dari konsep _colored coins_, yang sudah dieksplorasi sekitar tahun 2012-2013. Pada saat itu, beberapa tim berusaha mengaitkan nilai bitcoin yang berbeda pada UTXO, yang menyebabkan beberapa implementasi yang tersebar. Kurangnya standarisasi dan rendahnya permintaan pada saat itu mencegah solusi ini untuk mendapatkan pijakan yang langgeng.

Saat ini, RGB menonjol karena kekokohan konseptual dan spesifikasi terpadu melalui asosiasi LNP/BP. Prinsipnya didasarkan pada validasi sisi klien. Blockchain Bitcoin hanya menyimpan komitmen kriptografi (_commitments_, melalui Taproot atau OP_RETURN), sementara sebagian besar data (definisi kontrak, riwayat transfer, dll.) disimpan oleh pengguna yang bersangkutan. Dengan cara ini, beban penyimpanan didistribusikan dan kerahasiaan pertukaran diperkuat, tanpa membebani blockchain. Pendekatan ini memungkinkan penciptaan aset yang dapat dipertukarkan (standar **RGB20**) atau aset unik (standar **RGB21**), dalam kerangka kerja yang modular dan terukur.

### Fungsi token (RGB20) dan aset unik (RGB21)

Dengan **RGB20**, kita mendefinisikan token yang dapat dipertukarkan pada Bitcoin. Penerbit memilih _supply_, _precision_, dan membuat _contract_ di mana ia dapat melakukan transfer. Setiap transfer direferensikan ke Bitcoin UTXO, yang bertindak sebagai *Single-use Seal*. Logika ini memastikan bahwa pengguna tidak akan bisa membelanjakan aset yang sama dua kali, karena hanya orang yang mampu membelanjakan UTXO yang memegang kunci untuk memperbarui status kontrak sisi klien.

**RGB21** menargetkan aset unik (atau "NFT"). Aset ini memiliki persediaan 1, dan dapat dikaitkan dengan metadata (file gambar, audio, dll.) yang dijelaskan melalui bidang tertentu. Tidak seperti NFT di blockchain publik, data dan pengenal MIME-nya dapat tetap bersifat pribadi, didistribusikan secara peer-to-peer sesuai dengan kebijaksanaan pemiliknya.

### Solusi Bitmask: dompet untuk RGB

Untuk mengeksploitasi kemampuan RGB dalam praktiknya, proyek **DIBA** telah mendesain sebuah dompet yang disebut [Bitmask] (https://bitmask.app/). Idenya adalah untuk menyediakan alat berbasis Taproot yang tidak dikurung, yang dapat diakses sebagai aplikasi web atau ekstensi peramban. Bitmask mengelola aset RGB20 dan RGB21, dan mengintegrasikan berbagai mekanisme keamanan:


- Kode inti ditulis dalam Rust, kemudian dikompilasi dalam WebAssembly untuk dijalankan dalam lingkungan JavaScript (React);
- Kunci dibuat secara lokal, kemudian disimpan secara terenkripsi secara lokal;
- Data status (simpanan) disimpan dalam memori, diserialisasikan dan dienkripsi melalui pustaka **Carbonado**, yang melakukan kompresi, koreksi kesalahan, enkripsi, dan verifikasi aliran menggunakan Blake3.

Berkat arsitektur ini, semua transaksi aset terjadi di sisi klien. Dari luar, transaksi Bitcoin tidak lebih dari transaksi pembelanjaan Taproot klasik, yang tidak akan dicurigai oleh siapa pun yang juga melakukan transfer token yang dapat dipertukarkan atau NFT. Tidak adanya overloading on-chain (tidak ada metadata yang disimpan secara publik) menjamin tingkat keleluasaan tertentu dan membuatnya lebih mudah untuk menolak upaya penyensoran yang mungkin terjadi.

### Keamanan dan arsitektur terdistribusi

Sejauh protokol RGB mengharuskan setiap partisipan untuk menyimpan riwayat transaksinya (untuk membuktikan keabsahan transfer yang diterimanya), pertanyaan tentang penyimpanan muncul. Bitmask mengusulkan untuk menserialisasikan simpanan ini secara lokal, kemudian mengirimkannya ke beberapa server atau cloud (opsional). Data tetap dienkripsi oleh pengguna melalui **Carbonado**, sehingga server tidak dapat membacanya. Jika terjadi kerusakan parsial, lapisan koreksi kesalahan dapat menyusun kembali konten.

Penggunaan CRDT (_Tipe data yang direplikasi bebas konflik_) memungkinkan versi simpanan yang berbeda untuk digabungkan, jika ada perbedaan. Setiap orang bebas untuk menyimpan data ini di mana pun mereka inginkan, karena tidak ada satu pun node yang membawa semua informasi yang terkait dengan aset. Hal ini mencerminkan filosofi *Validasi Sisi Klien*, di mana setiap pemilik bertanggung jawab untuk menyimpan bukti validitas aset RGB mereka.

### Menuju ekosistem yang lebih luas: pasar, interoperabilitas, dan fungsi-fungsi baru

Perusahaan di balik Bitmask tidak membatasi diri pada pengembangan dompet yang sederhana. DIBA bermaksud untuk mengembangkan :


- Sebuah **pasar** untuk menukar token, terutama dalam bentuk **RGB21**;
- Kompatibilitas dengan dompet lain (seperti *Iris Wallet*);
- Teknik transfer batching**, yaitu kemungkinan untuk menyertakan beberapa transfer RGB yang berurutan dalam satu transaksi.

Pada saat yang sama, kami sedang mengerjakan **WebBTC** atau **WebLN** (standar yang memungkinkan situs web untuk meminta dompet untuk menandatangani transaksi Bitcoin atau Lightning), serta kemampuan untuk "teleburn" entri Ordinals (jika kami ingin memulangkan Ordinals ke format RGB yang lebih bijaksana dan fleksibel).

### Kesimpulan

Keseluruhan proses ini menunjukkan bagaimana ekosistem RGB dapat digunakan dan dapat diakses oleh pengguna akhir melalui solusi teknis yang kuat. Transisi dari perspektif altcoin ke visi yang lebih berpusat pada Bitcoin, ditambah dengan penemuan *Validasi Sisi Klien*, menggambarkan jalur yang cukup logis: kami memahami bahwa dimungkinkan untuk mengimplementasikan berbagai fungsi (token yang dapat dipertukarkan, NFT, kontrak pintar ...) tanpa melakukan forking pada blockchain, cukup dengan memanfaatkan komitmen kriptografi pada transaksi Taproot atau OP_RETURN.

Dompet **Bitmask** adalah bagian dari pendekatan ini: di sisi blockchain, yang Anda lihat hanyalah transaksi Bitcoin biasa; di sisi pengguna, Anda memanipulasi antarmuka web tempat Anda membuat, menukar, dan menyimpan semua jenis aset di luar jaringan. Model ini dengan jelas memisahkan infrastruktur moneter (Bitcoin) dari logika penerbitan dan transfer (RGB), sambil memastikan tingkat kerahasiaan yang tinggi dan skalabilitas yang lebih baik.

## Karya Bitfinex pada RGB

<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>

![vidéo](https://youtu.be/5iAhsgCSL3U)

Dalam bab ini, berdasarkan presentasi oleh Frederico Tenga, kita akan melihat seperangkat alat dan proyek yang dibuat oleh tim Bitfinex yang didedikasikan untuk RGB, dengan tujuan untuk mendorong munculnya ekosistem yang kaya dan beragam di sekitar protokol ini. Tujuan awal tim ini bukan untuk merilis produk komersial tertentu, melainkan untuk menyediakan blok bangunan perangkat lunak, berkontribusi pada protokol RGB itu sendiri, dan mengusulkan referensi implementasi konkret seperti dompet seluler (*Iris Wallet *) atau simpul Lightning yang kompatibel dengan RGB.

### Latar belakang dan tujuan

Sejak sekitar tahun 2022, tim RGB Bitfinex telah berkonsentrasi pada pengembangan tumpukan teknologi yang memungkinkan RGB dieksploitasi dan diuji secara efisien. Beberapa kontribusi telah dibuat:


- Partisipasi dalam kode sumber dan spesifikasi protokol, termasuk menulis proposal peningkatan, memperbaiki bug, dll;
- Alat bantu bagi para pengembang untuk menyederhanakan integrasi RGB dalam aplikasi mereka;
- Desain dompet seluler bernama [Iris](https://iriswallet.com/) untuk bereksperimen dan mengilustrasikan praktik terbaik dalam menggunakan RGB;
- Pembuatan simpul Lightning yang disesuaikan, yang mampu mengelola saluran dengan aset RGB;
- Mendukung tim lain dalam membangun solusi RGB, untuk mendorong keragaman dan ekosistem yang kuat.

Pendekatan ini bertujuan untuk mencakup seluruh rantai kebutuhan: dari pustaka tingkat rendah (*[RGBlib](https://github.com/RGB-Tools/rgb-lib)*), yang memungkinkan implementasi dompet, hingga aspek produksi (node Lightning, dompet untuk Android, dll.).

### Perpustakaan RGBlib: menyederhanakan pengembangan aplikasi RGB

Poin penting dalam mendemokratisasi pembuatan dompet dan aplikasi RGB adalah menyediakan abstraksi yang cukup sederhana sehingga pengembang tidak perlu mempelajari semua hal tentang logika internal protokol. Inilah tujuan dari **RGBlib**, yang ditulis dalam bahasa Rust.

RGBlib bertindak sebagai jembatan antara persyaratan RGB yang sangat fleksibel (tetapi terkadang rumit) yang telah kita pelajari di bab-bab sebelumnya, dan kebutuhan konkret pengembang aplikasi. Dengan kata lain, sebuah dompet (atau layanan) yang ingin mengelola transfer token, penerbitan aset, verifikasi, dan lain-lain, dapat mengandalkan RGBlib tanpa mengetahui setiap detail kriptografi atau setiap parameter RGB yang dapat disesuaikan.

Toko buku menawarkan :


- Fungsi turnkey untuk menerbitkan (_issue_) aset (dapat dipertukarkan atau tidak);
- Kemampuan untuk mentransfer (mengirim/menerima) aset dengan memanipulasi objek-objek sederhana (alamat, jumlah, UTXO, dll.);
- Mekanisme untuk menyimpan dan memuat informasi status (*kiriman*) yang diperlukan untuk Validasi Sisi Klien.

Oleh karena itu, RGBlib bergantung pada gagasan kompleks yang spesifik untuk RGB (Validasi Sisi Klien, jangkar Tapret/Opret), tetapi merangkumnya sehingga aplikasi akhir tidak perlu memprogram ulang semuanya atau membuat keputusan yang berisiko. Terlebih lagi, RGBlib sudah diikat dalam beberapa bahasa (Kotlin dan Python), membuka pintu untuk penggunaan di luar semesta Rust yang sederhana.

### Iris Wallet: contoh dompet RGB di Android

Untuk membuktikan keefektifan RGBlib, tim Bitfinex telah mengembangkan **Iris Wallet**, secara eksklusif di Android pada tahap ini. Ini adalah dompet seluler yang menggambarkan pengalaman pengguna yang mirip dengan dompet Bitcoin biasa: Anda dapat menerbitkan aset, mengirimnya, menerimanya, dan melihat riwayatnya, sambil tetap menggunakan model penyimpanan mandiri.

Iris memiliki sejumlah fitur menarik:

**Menggunakan server Electrum:**

Seperti dompet lainnya, Iris perlu mengetahui tentang konfirmasi transaksi pada blockchain. Daripada menyematkan sebuah node yang lengkap, Iris secara default menggunakan server Electrum yang dikelola oleh tim Bitfinex. Akan tetapi, pengguna dapat mengonfigurasi server mereka sendiri atau layanan pihak ketiga lainnya. Dengan cara ini, transaksi Bitcoin dapat divalidasi dan informasi dapat diambil (pengindeksan) secara modular.

**Server proxy RGB:**

Tidak seperti Bitcoin, RGB membutuhkan pertukaran metadata off-chain (*kiriman*) antara pengirim dan penerima. Untuk menyederhanakan proses ini, Iris menawarkan sebuah solusi di mana komunikasi dilakukan melalui server proxy. Dompet penerima menghasilkan sebuah *invoice* yang menyebutkan ke mana pengirim harus mengirimkan data *sisi-klien*. Secara default, URL mengarah ke proxy yang dihosting oleh tim Bitfinex, tetapi Anda dapat mengubah proxy ini (atau menghosting proxy Anda sendiri). Idenya adalah untuk kembali ke pengalaman pengguna yang sudah dikenal di mana penerima menampilkan kode QR, dan pengirim memindai kode ini untuk transaksi, tanpa manipulasi tambahan yang rumit.

**Pencadangan berkelanjutan:**

Dalam konteks Bitcoin, mencadangkan seed Anda pada umumnya sudah cukup (meskipun saat ini kami menyarankan untuk mencadangkan seed dan deskriptornya saja). Dengan RGB, hal ini tidaklah cukup: Anda juga harus menyimpan riwayat lokal (*kiriman*) yang membuktikan bahwa Anda benar-benar memiliki aset RGB. Setiap kali Anda menerima tanda terima, perangkat menyimpan data baru, yang sangat penting untuk pembelanjaan berikutnya. Iris secara otomatis mengelola cadangan terenkripsi di Google Drive pengguna. Hal ini tidak memerlukan kepercayaan khusus pada Google, karena cadangan dienkripsi, dan opsi yang lebih kuat (seperti server pribadi) direncanakan untuk masa depan untuk menghindari risiko penyensoran atau penghapusan oleh operator pihak ketiga.

**Fitur lainnya:**


- Buat faucet untuk menguji atau mendistribusikan token dengan cepat untuk eksperimen atau promosi;
- Sebuah sistem sertifikasi (saat ini terpusat) untuk membedakan token yang sah dengan token palsu yang meniru ticker terkenal. Di masa depan, sertifikasi ini dapat menjadi lebih terdesentralisasi (melalui DNS atau mekanisme lainnya).

Secara keseluruhan, Iris menawarkan pengalaman pengguna yang mirip dengan dompet Bitcoin klasik, menutupi kerumitan tambahan (manajemen simpanan, riwayat *konsinyasi*, dll.) berkat RGBlib dan penggunaan server proxy.

### Server proxy dan pengalaman pengguna

Server proxy yang diperkenalkan di atas perlu dijelaskan secara rinci, karena ini adalah kunci untuk pengalaman pengguna yang lancar. Alih-alih pengirim harus secara manual mengirimkan *kiriman* ke penerima, transaksi RGB berlangsung di latar belakang melalui file :


- Penerima membuat *invoice* (berisi, antara lain, alamat proxy);
- Pengirim mengirimkan (melalui permintaan HTTP) proyek transisi (*konsinyasi*) ke proxy;
- Penerima mengambil proyek ini, mengeksekusi validasi *sisi-klien* secara lokal;
- Penerima kemudian mempublikasikan, melalui proxy, penerimaan (atau mungkin penolakan) dari transisi negara ;
- Pengirim dapat melihat status validasi dan, jika diterima, menyiarkan transaksi Bitcoin yang menyelesaikan transfer.

Dengan cara ini, dompet berperilaku hampir seperti dompet biasa. Pengguna tidak menyadari semua langkah perantara. Harus diakui, proxy saat ini tidak dienkripsi atau diautentikasi (yang menimbulkan kekhawatiran tentang kerahasiaan dan integritas), tetapi perbaikan ini mungkin dilakukan di versi yang lebih baru. Konsep proxy tetap sangat berguna untuk menciptakan pengalaman "Saya mengirim kode QR, Anda memindai untuk membayar".

### Integrasi RGB pada Jaringan Lightning

Fokus utama lain dari pekerjaan tim Bitfinex adalah membuat Lightning Network kompatibel dengan aset RGB. Tujuannya adalah untuk mengaktifkan saluran Lightning dalam USDT (atau token lainnya), dan untuk mendapatkan keuntungan yang sama dengan bitcoin di Lightning (transaksi hampir seketika, perutean, dll.). Secara konkret, ini melibatkan pembuatan node Lightning yang dimodifikasi menjadi :


- Buka saluran dengan menempatkan tidak hanya satoshi, tetapi juga satu atau lebih aset RGB dalam pendanaan multisig UTXO;
- Menghasilkan transaksi komitmen Lightning (sisi Bitcoin) disertai dengan transisi status RGB yang sesuai. Setiap kali saluran diperbarui, transisi RGB mendefinisikan ulang distribusi aset dalam output Lightning;
- Mengaktifkan penutupan sepihak, di mana aset diambil dalam UTXO eksklusif, sesuai dengan aturan Lightning Network (HTLC, penguncian waktu, hukuman, dll.).

Solusi ini, yang dijuluki "**RGB Lightning Node**", menggunakan LDK (*Lightning Dev Kit*) sebagai basis, dan menambahkan mekanisme yang diperlukan untuk menyuntikkan token RGB ke dalam saluran. Komitmen petir mempertahankan struktur klasik (keluaran yang dapat ditembus, penguncian waktu...), dan sebagai tambahan jangkar transisi status RGB (melalui `Opret` atau `Tapret`). Bagi pengguna, ini membuka jalan menuju saluran Lightning di stablecoin atau aset lain yang dipancarkan melalui RGB.

### Potensi dan dampak DEX terhadap Bitcoin

Setelah beberapa aset dikelola melalui Lightning, menjadi mungkin untuk membayangkan **pertukaran atom** pada jalur perutean Lightning tunggal, menggunakan logika rahasia dan penguncian waktu yang sama. Sebagai contoh, pengguna A menyimpan bitcoin di satu jalur Lightning, dan pengguna B menyimpan USDT RGB di jalur Lightning yang lain. Mereka dapat membangun jalur yang menghubungkan dua saluran mereka dan secara bersamaan menukar BTC dengan USDT, tanpa perlu kepercayaan. Ini tidak lebih dari sebuah **pertukaran atom** yang terjadi dalam beberapa lompatan, membuat peserta di luar hampir tidak menyadari fakta bahwa mereka sedang melakukan perdagangan, bukan hanya perutean. Pendekatan ini menawarkan :


- Latensi yang sangat rendah, karena semuanya tetap berada di luar rantai pada Lightning.
- Privasi yang unggul: tidak ada yang tahu bahwa ini adalah perdagangan, dan bukan perutean normal;
- Menghindari frontrunning, masalah berulang untuk DEX on-chain;
- Mengurangi biaya (Anda tidak membayar blockspace, hanya biaya perutean Lightning).

Kita kemudian dapat membayangkan sebuah ekosistem di mana node Lightning menawarkan harga swap (dengan menyediakan likuiditas). Setiap node, jika diinginkan, dapat berperan sebagai _market maker_, membeli dan menjual berbagai aset di Lightning. Prospek DEX _layer-2_ ini memperkuat gagasan bahwa tidak perlu bercabang atau menggunakan blockchain pihak ketiga untuk mendapatkan pertukaran aset yang terdesentralisasi.

Dampaknya terhadap Bitcoin bisa jadi positif: Infrastruktur Lightning (node, saluran, dan layanan) akan lebih banyak digunakan berkat volume yang dihasilkan oleh *stablecoin*, turunan, dan token lainnya. Pedagang yang tertarik dengan pembayaran USDT di Lightning akan secara otomatis menemukan pembayaran BTC di Lightning (dikelola oleh stack yang sama). Pemeliharaan dan pembiayaan infrastruktur Lightning Network juga dapat memperoleh manfaat dari penggandaan aliran non-BTC ini, yang secara tidak langsung akan menguntungkan pengguna Bitcoin.

### Kesimpulan dan sumber daya

Tim Bitfinex yang didedikasikan untuk RGB mengilustrasikan, melalui karyanya, keragaman yang dapat dilakukan di atas protokol. Di satu sisi, ada RGBlib, sebuah perpustakaan yang memfasilitasi desain dompet dan aplikasi. Di sisi lain, kami memiliki Iris Wallet, sebuah demonstrasi praktis di Android dari antarmuka pengguna akhir yang rapi. Terakhir, integrasi RGB dengan Lightning menunjukkan bahwa saluran stablecoin dimungkinkan, dan membuka jalan menuju DEX terdesentralisasi yang potensial di Lightning.

Pendekatan ini sebagian besar masih bersifat eksperimental dan terus berkembang: pustaka RGBlib sedang disempurnakan seiring berjalannya waktu, Iris Wallet menerima penyempurnaan secara teratur, dan simpul Lightning khusus belum menjadi klien Lightning utama.

Bagi mereka yang ingin mempelajari lebih lanjut atau berkontribusi, beberapa sumber daya tersedia, termasuk :


- [Repositori GitHub RGB Tools](https://github.com/RGB-Tools);
- [Situs informasi yang didedikasikan untuk Iris Wallet](https://iriswallet.com/) untuk menguji dompet di Android.

Dalam bab berikutnya, kita akan melihat lebih dekat pada cara meluncurkan node RGB Lightning.

## RLN - Simpul Petir RGB

<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>

![vidéo](https://youtu.be/piQQH4Q2nr0)

Dalam bab terakhir ini, Frederico Tenga akan memandu Anda langkah demi langkah dalam menyiapkan node Lightning RGB di lingkungan Regtest, dan menunjukkan kepada Anda cara membuat token RGB di dalamnya. Dengan meluncurkan dua node terpisah, Anda juga akan menemukan cara membuka saluran Lightning di antara keduanya dan bertukar aset RGB.

Video ini berfungsi sebagai tutorial, serupa dengan yang kita bahas dalam bab sebelumnya, tetapi kali ini secara khusus difokuskan pada Lightning!

Sumber daya utama untuk video ini adalah repositori Github [RGB Lightning Node](https://github.com/RGB-Tools/rgb-lightning-node), yang memudahkan Anda untuk meluncurkan konfigurasi ini di Regtest.

### Menerapkan simpul Lightning yang kompatibel dengan RGB

Proses ini mengambil dan mempraktikkan semua konsep yang telah dibahas dalam bab-bab sebelumnya:


- Gagasan bahwa **UTXO** yang diblokir pada multisig 2/2 dari saluran Lightning tidak hanya dapat menerima bitcoin, tetapi juga menjadi Segel Sekali Pakai aset RGB (dapat ditukarkan atau tidak);
- Penambahan, dalam setiap transaksi keterlibatan Lightning, output (`Tapret` atau `Opret`) yang didedikasikan untuk menambatkan transisi status RGB;
- Infrastruktur terkait (bitcoind/indexer/proxy) untuk memvalidasi transaksi Bitcoin dan pertukaran data *sisi klien*.

### Memperkenalkan rgb-lightning-node

Proyek **`rgb-lightning-node`` adalah sebuah daemon Rust yang didasarkan pada garpu `rust-lightning` (LDK) yang dimodifikasi untuk memperhitungkan keberadaan aset RGB dalam sebuah saluran. Ketika sebuah saluran dibuka, keberadaan aset dapat ditentukan, dan setiap kali status saluran diperbarui, transisi RGB dibuat, yang mencerminkan distribusi aset dalam output Lightning. Hal ini memungkinkan :


- Buka saluran Lightning dalam USDT, misalnya;
- Rutekan token-token ini melalui jaringan, asalkan jalur perutean memiliki likuiditas yang cukup;
- Manfaatkan hukuman Lightning dan logika timelock tanpa modifikasi: cukup jangkarkan transisi RGB dalam output tambahan dari transaksi komitmen.

Kode ini masih dalam tahap alfa: kami sarankan untuk menggunakannya di **regtest** atau di **testnet** saja.

### Instalasi node

Untuk mengkompilasi dan menginstal biner `rgb-lightning-node`, kita mulai dengan mengkloning repositori dan sub-modulnya, lalu kita jalankan berkas :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RGB-Bitcoin](assets/fr/098.webp)


- Opsi `--recurse-submodules` juga mengkloning sub-perangkat yang diperlukan (termasuk versi modifikasi dari `rust-lightning`);
- Opsi `--shallow-submodules` membatasi kedalaman klon untuk mempercepat pengunduhan, sambil tetap menyediakan akses ke komit yang penting.

Dari root proyek, jalankan perintah berikut untuk mengkompilasi dan menginstal biner :

```bash
cargo install --locked --debug --path .
```

![RGB-Bitcoin](assets/fr/099.webp)


- `--locked` memastikan bahwa versi dependensi benar-benar dihormati;
- `--debug` tidak wajib, tetapi dapat membantu Anda fokus (Anda dapat menggunakan `--release` jika Anda mau);
- `--path .` memberitahu `cargo install` untuk menginstal dari direktori saat ini.

Pada akhir perintah ini, sebuah eksekusi `rgb-lightning-node` akan tersedia pada `$CARGO_HOME/bin/`. Pastikan jalur ini ada di `$PATH` Anda sehingga Anda dapat memanggil perintah dari direktori mana pun.

### Persyaratan kinerja

Agar dapat berfungsi, daemon `rgb-lightning-node` memerlukan keberadaan dan konfigurasi :


- Sebuah simpul `bitcoind`**

Setiap instance RLN perlu berkomunikasi dengan `bitcoind` untuk menyiarkan dan memonitor transaksi on-chain. Otentikasi (login/kata sandi) dan URL (host/port) harus disediakan untuk daemon.


- Pengindeks** (Electrum atau Esplora)

Daemon harus dapat membuat daftar dan menjelajahi transaksi on-chain, khususnya untuk menemukan UTXO tempat sebuah aset ditambatkan. Anda harus menentukan URL server Electrum atau Esplora Anda.


- Proksi RGB**

Seperti yang terlihat pada bab-bab sebelumnya, **server proxy** adalah sebuah komponen (opsional, tetapi sangat disarankan) untuk menyederhanakan pertukaran *kiriman* di antara rekan-rekan Lightning. Sekali lagi, sebuah URL harus ditentukan.

ID dan URL dimasukkan ketika daemon dibuka kuncinya melalui API. Lebih lanjut tentang ini nanti.

### Peluncuran pengujian ulang

Untuk penggunaan sederhana, ada skrip `regtest.sh` yang secara otomatis memulai, melalui Docker, serangkaian layanan: `bitcoind`, `electrs` (pengindeks), `rgb-proxy-server`.

![RGB-Bitcoin](assets/fr/100.webp)

Hal ini memungkinkan Anda untuk meluncurkan lingkungan lokal, terisolasi, dan telah dikonfigurasi sebelumnya. Ini membuat dan menghancurkan kontainer dan direktori data pada setiap reboot. Kita akan mulai dengan memulai file :

```bash
./regtest.sh start
```

Skrip ini akan :


- Buat direktori `docker/` untuk menyimpan file ;
- Jalankan `bitcoind` di regtest, serta pengindeks `electrs` dan `rgb-proxy-server`;
- Tunggu sampai semuanya siap digunakan.

![RGB-Bitcoin](assets/fr/101.webp)

Selanjutnya, kita akan meluncurkan beberapa node RLN. Pada shell terpisah, jalankan, misalnya (untuk meluncurkan 3 node RLN) :

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RGB-Bitcoin](assets/fr/102.webp)


- Parameter `--network regtest` mengindikasikan penggunaan konfigurasi regtest;
- `--daemon-listening-port` mengindikasikan pada port REST mana node Lightning akan mendengarkan panggilan API (JSON);
- `--ldk-peer-listening-port` menentukan port p2p Lightning mana yang akan didengarkan;
- `dataldk0/`, `dataldk1/` adalah jalur ke direktori penyimpanan (setiap simpul menyimpan informasinya secara terpisah).

Anda juga dapat menjalankan perintah pada node RLN Anda dari browser Anda:

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

Agar sebuah node dapat membuka sebuah saluran, node tersebut harus memiliki bitcoin pada alamat yang dibuat dengan perintah berikut (untuk node n°1, misalnya):

```bash
curl -X POST http://localhost:3001/address
```

Jawabannya akan memberi Anda sebuah alamat.

![RGB-Bitcoin](assets/fr/103.webp)

Pada Regtest `bitcoind`, kita akan menambang beberapa bitcoin. Jalankan:

```bash
./regtest.sh mine 101
```

![RGB-Bitcoin](assets/fr/104.webp)

Kirim dana ke alamat node yang dibuat di atas:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RGB-Bitcoin](assets/fr/105.webp)

Kemudian lakukan penambangan blok untuk mengonfirmasi transaksi:

```bash
./regtest.sh mine 1
```

![RGB-Bitcoin](assets/fr/106.webp)

### Peluncuran Testnet (tanpa Docker)

Jika Anda ingin menguji skenario yang lebih realistis, Anda dapat meluncurkan 3 node RLN di Testnet daripada di Regtest, yang mengarah ke layanan publik:

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

Secara default, jika tidak ada konfigurasi yang ditemukan, daemon akan mencoba menggunakan ekstensi :


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

Dengan login :


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `kata sandi`

Anda juga dapat menyesuaikan elemen-elemen ini melalui API `init`/`unlock`.

### Menerbitkan token RGB

Untuk menerbitkan token, kita akan mulai dengan membuat UTXO yang "dapat diwarnai":

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RGB-Bitcoin](assets/fr/107.webp)

Anda tentu saja dapat menyesuaikan pesanan. Untuk mengonfirmasi transaksi, kami menambang file :

```bash
./regtest.sh mine 1
```

Sekarang kita dapat membuat aset RGB. Perintahnya akan bergantung pada jenis aset yang ingin Anda buat dan parameternya. Di sini saya membuat token NIA (*Non Inflatable Asset*) bernama "PBN" dengan persediaan 1000 unit. `Presision` memungkinkan Anda untuk menentukan pembagian unit.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RGB-Bitcoin](assets/fr/108.webp)

Tanggapannya mencakup ID aset yang baru dibuat. Ingatlah untuk mencatat pengenal ini. Dalam kasus saya, ini adalah :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RGB-Bitcoin](assets/fr/109.webp)

Anda kemudian dapat mentransfernya secara on-chain, atau mengalokasikannya dalam saluran Lightning. Itulah yang akan kita lakukan di bagian selanjutnya.

### Membuka saluran dan mentransfer aset RGB

Anda harus terlebih dahulu menyambungkan node Anda ke peer di jaringan Lightning menggunakan perintah `/connectpeer`. Dalam contoh saya, saya mengendalikan kedua node. Jadi, saya akan mengambil kunci publik dari node Lightning kedua dengan perintah ini:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

Perintah ini mengembalikan kunci publik dari simpul saya n°2:

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RGB-Bitcoin](assets/fr/110.webp)

Selanjutnya, kita akan membuka channel dengan menentukan aset yang relevan (`PBN`). Perintah `/openchannel` memungkinkan Anda menentukan ukuran saluran di satoshi dan memilih untuk menyertakan aset RGB. Tergantung pada apa yang ingin Anda buat, tetapi dalam kasus saya, perintahnya adalah :

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

Cari tahu lebih lanjut di sini:


- `peer_pubkey_and_opt_addr`: Pengidentifikasi peer yang ingin kita sambungkan (kunci publik yang kita temukan sebelumnya);
- `kapasitas_sat`: Total kapasitas saluran dalam satoshi;
- `push_msat`: Jumlah dalam milisatos yang awalnya ditransfer ke peer ketika saluran dibuka (di sini saya langsung mentransfer 10.000 sat supaya dia bisa melakukan transfer RGB nanti);
- `jumlah_aset`: Jumlah aset RGB yang akan dikomitmenkan ke saluran;
- `asset_id`: Pengidentifikasi unik dari aset RGB yang terlibat dalam saluran;
- `public`: Menunjukkan apakah saluran harus dibuat publik untuk perutean di jaringan.

![RGB-Bitcoin](assets/fr/111.webp)

Untuk mengonfirmasi transaksi, 6 blok ditambang:

```bash
./regtest.sh mine 6
```

![RGB-Bitcoin](assets/fr/112.webp)

Saluran Lightning sekarang terbuka dan juga berisi 500 token `PBN` di sisi node n°1. Jika node n°2 ingin menerima token `PBN`, ia harus membuat faktur. Berikut cara melakukannya:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

Dengan:


- `amt_msat`: Jumlah faktur dalam milisatoshi (minimal 3000 sat);
- `expiry_sec`: Waktu kedaluwarsa faktur dalam hitungan detik;
- `asset_id`: Pengidentifikasi aset RGB yang terkait dengan faktur;
- `jumlah_aset`: Jumlah aset RGB yang akan ditransfer dengan faktur ini.

Sebagai tanggapan, Anda akan mendapatkan faktur RGB (seperti yang dijelaskan dalam bab sebelumnya):

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RGB-Bitcoin](assets/fr/113.webp)

Sekarang kita akan membayar faktur ini dari node pertama, yang menyimpan uang tunai yang diperlukan dengan token `PBN`:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RGB-Bitcoin](assets/fr/114.webp)

Pembayaran telah dilakukan. Hal ini dapat diverifikasi dengan menjalankan perintah :

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RGB-Bitcoin](assets/fr/115.webp)

Berikut ini adalah cara menggunakan simpul Lightning yang dimodifikasi untuk membawa aset RGB. Demonstrasi ini didasarkan pada :


- Lingkungan regtest (melalui `./regtest.sh`) atau testnet ;
- Simpul Lightning (`rgb-lightning-node`) yang didasarkan pada `bitcoind`, sebuah pengindeks dan `rgb-proxy-server`;
- Serangkaian API REST JSON untuk membuka/menutup saluran, menerbitkan token, mentransfer aset melalui Lightning, dll.

Berkat proses ini :


- Transaksi keterlibatan petir mencakup output tambahan (OP_RETURN atau Taproot) dengan penahan transisi RGB;
- Transfer dilakukan dengan cara yang persis sama dengan pembayaran Lightning tradisional, tetapi dengan tambahan token RGB;
- Beberapa node RLN dapat dihubungkan ke rute dan bereksperimen dengan pembayaran di beberapa node, asalkan ada likuiditas yang cukup dalam bitcoin dan RGB aset di jalur tersebut.

Proyek ini masih dalam tahap alfa. Oleh karena itu, sangat disarankan agar Anda membatasi diri Anda pada lingkungan pengujian (regtest, testnet).

Peluang yang dibuka oleh kompatibilitas LN-RGB ini cukup besar: stablecoin di Lightning, DEX layer-2, transfer token yang dapat dipertukarkan atau NFT dengan biaya yang sangat rendah... Bab-bab sebelumnya telah menguraikan arsitektur konseptual dan logika validasi. Sekarang Anda memiliki pandangan praktis tentang cara membuat node seperti itu aktif dan berjalan, untuk pengembangan atau pengujian di masa mendatang.

# Kesimpulan

<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>


## Ulasan & Peringkat

<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>

<isCourseReview>true</isCourseReview>

## Kesimpulan

<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>

<isCourseConclusion>true</isCourseConclusion>
