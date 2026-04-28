---
name: Liquid Bootcamp Esensial
goal: Dapatkan pemahaman yang komprehensif tentang proyek Liquid Network dan Elements, dan pelajari cara mengimplementasikan solusi canggih dalam transaksi rahasia, tokenisasi, dan arsitektur jaringan yang terdesentralisasi.
objectives: 

  - Memahami dasar-dasar arsitektur Liquid dan hubungannya dengan Bitcoin.
  - Pelajari cara mengonfigurasi dan mengoperasikan node Liquid menggunakan perangkat lunak Elements.
  - Jelajahi penggunaan transaksi rahasia dan penerbitan aset pada Liquid Network.
  - Pahami aspek bisnis dan teknis Liquid untuk aplikasi di pasar modal.

---

# Memperkenalkan jaringan Liquid


Mulailah perjalanan pendidikan yang dirancang untuk memberikan pemahaman mendalam tentang proyek Liquid Network dan Elements. Pelatihan ini menggabungkan teori dan praktik untuk mengajarkan Anda dasar-dasar teknis, arsitektur, dan bisnis yang diperlukan untuk mengimplementasikan dan memanfaatkan kemampuan Liquid. Dari transaksi rahasia hingga desain ekosistem, kursus ini sangat ideal bagi mereka yang ingin memperluas pengetahuan mereka tentang alat canggih dalam ekosistem Bitcoin.


Dengan presentasi dari para pakar industri, kursus ini mencakup topik-topik seperti arsitektur Liquid, aplikasi tokenisasi, konsep teknis Elements, dan kasus-kasus penggunaan inovatif seperti Breez SDK. Dirancang agar dapat diakses oleh pemula dan pengguna tingkat menengah, kursus ini juga menawarkan nilai tambah bagi para pengembang berpengalaman yang ingin menguasai Liquid sebagai platform untuk mengoptimalkan proyek mereka.

+++

# Pendahuluan


<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>


## Gambaran umum kursus


<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>


Selamat datang di Liquid Bootcamp, pelatihan komprehensif yang dirancang untuk membekali Anda dengan pengetahuan dan keterampilan untuk memanfaatkan proyek Liquid Network dan Elements secara efektif. Pelatihan ini menawarkan eksplorasi komprehensif tentang fitur-fitur khas Liquid, termasuk Confidential Transactions, penerbitan aset, dan arsitektur jaringan federasi, sekaligus memperkenalkan konsep dasar Elements, perangkat lunak yang mendukung Liquid.


Selama pelatihan, Anda akan menjelajahi aplikasi praktis Liquid Network, mulai dari menyiapkan dan mengoperasikan node hingga memahami penggunaannya di pasar modal dan tokenisasi Bitcoin. Dengan presentasi dari para pakar industri, Anda juga akan mendapatkan wawasan tentang topik-topik tingkat lanjut seperti HTLC, Breez SDK, dan proyek Blockstream AMP.


Pelatihan ini awalnya diadakan sebagai acara tatap muka, mengikuti jadwal terstruktur (seperti yang ditunjukkan pada gambar) yang dirancang untuk sesi langsung. Namun, untuk adaptasi kursus ini, kontennya telah ditata ulang agar lebih sesuai dengan format online dan memfasilitasi pemahaman siswa. Susunan yang baru ini memastikan perkembangan yang logis dari konsep dasar ke topik yang lebih maju dan teknis, sehingga memaksimalkan pengalaman belajar.


Perjalanan ini disusun untuk mengakomodasi peserta dengan berbagai tingkat keahlian, menawarkan perpaduan antara pengetahuan teoretis dan pengalaman langsung. Pada akhir pelatihan ini, Anda akan memiliki pemahaman yang kuat mengenai arsitektur Liquid, integrasinya dengan Bitcoin, dan bagaimana memanfaatkan fitur-fitur inovatifnya untuk membangun dan mengoptimalkan solusi keuangan.


Selami dunia sidechain Liquid dan lepaskan potensi penuhnya sekarang juga!

# Dasar-dasar


<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>


## Arsitektur Liquid


<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>


:::video id=ff6899d2-b47f-4c3d-983d-3bd66d2be59d:::

### Arsitektur Liquid Network dan Model Konsensus


Liquid Network adalah sidechain federasi yang dibangun di atas basis kode Elements, yang dirancang untuk memperluas kemampuan Bitcoin dengan tetap mengandalkan keamanan fundamentalnya. Tidak seperti Bitcoin, [Proof-of-Work](https://planb.academy/resources/glossary/proof-of-work), Liquid beroperasi dengan model [Konsensus](https://planb.academy/resources/glossary/consensus) Federasi. Jaringan ini dikelola oleh sekelompok anggota yang tersebar secara global, termasuk bursa, meja perdagangan, dan penyedia infrastruktur. Dari keanggotaan ini, lima belas "fungsionaris" dipilih untuk bertindak sebagai penandatangan [blok](https://planb.academy/resources/glossary/block).


Para fungsionaris ini menghasilkan blok secara round-robin deterministik, dengan blok baru yang dihasilkan setiap menit. Waktu yang tepat ini berbeda dengan Bitcoin yang memiliki interval sepuluh menit yang bersifat probabilistik. Agar sebuah blok menjadi valid, dibutuhkan tanda tangan dari setidaknya 11 dari 15 fungsionaris (dua pertiga ditambah satu ambang batas). Mekanisme ini memberikan Liquid dengan "finalitas dua blok," yang berarti bahwa setelah sebuah [transaksi](https://planb.academy/resources/glossary/transaction-tx) memiliki dua konfirmasi (sekitar dua menit), secara matematis tidak mungkin untuk mengatur ulang rantai. Kecepatan dan kepastian ini sangat penting untuk arbitrase, perdagangan otomatis, dan penyelesaian antar bursa yang cepat.


Federasi ini bersifat dinamis. Melalui protokol Dynamic Federation (Dynafed), jaringan dapat merotasi fungsionaris atau memperbarui parameter tanpa memerlukan [fork](https://planb.academy/resources/glossary/fork) yang keras. Hal ini memungkinkan sistem untuk berevolusi dan mengganti perangkat keras atau anggota dengan mulus sambil mempertahankan operasi yang berkelanjutan.


### Confidential Transactions dan Manajemen Aset


Fitur yang menentukan dari Liquid adalah dukungan aslinya untuk Confidential Transactions (CT) dan beberapa aset. Pada rantai utama Bitcoin, semua detail transaksi - pengirim, penerima, dan jumlah - bersifat publik. Pada Liquid, CT menggunakan komitmen kriptografi untuk menyembunyikan jenis dan jumlah aset dari buku besar publik, namun tetap mengizinkan jaringan untuk memverifikasi bahwa transaksi tersebut valid (dengan kata lain, tidak ada [penggelembungan](https://planb.academy/resources/glossary/inflation) yang terjadi). Hanya peserta yang memegang kunci blinding yang dapat melihat nilai spesifik, menawarkan tingkat privasi komersial yang penting bagi institusi yang memindahkan posisi besar.


Liquid memperlakukan semua aset sebagai warga asli [blockchain](https://planb.academy/resources/glossary/blockchain). Ini termasuk Liquid Bitcoin (LBTC), stablecoin seperti USDT, dan token keamanan. Menerbitkan aset tidak membutuhkan smart contract yang rumit; ini adalah fungsi dasar dari protokol.


#### Aset yang Diatur dan AMP

Untuk aset yang membutuhkan kepatuhan, seperti token keamanan, Liquid menggunakan Platform Manajemen Aset Blockstream (AMP). Ini memperkenalkan lapisan berizin di mana transaksi memerlukan tanda tangan kedua dari server otorisasi. Hal ini memungkinkan penerbit untuk menegakkan aturan - seperti persyaratan Daftar Putih atau KYC - pada tingkat granular, menggabungkan efisiensi blockchain dengan kontrol regulasi keuangan tradisional.


### Pasak Dua Arah dan Infrastruktur Keamanan


Koneksi antara Liquid dan Bitcoin dipertahankan melalui pasak dua arah. Untuk "peg-in," pengguna mengirimkan Bitcoin ke alamat yang dihasilkan pada mainchain. Dana ini dikunci selama 102 konfirmasi (sekitar 17 jam) untuk menghilangkan risiko reorganisasi. Setelah dikonfirmasi, jumlah LBTC yang setara akan dicetak pada sidechain Liquid.


Proses "peg-out" memungkinkan pengguna untuk menukarkan LBTC dengan Bitcoin. Proses ini membutuhkan pembakaran LBTC dan otorisasi kriptografi dari federasi. Untuk mencegah pencurian, peg-out dikontrol secara ketat oleh Peg-out Authorization Keys (PAK) yang dipegang oleh anggota federasi. Selain itu, dana dapat ditukar secara instan melalui penyedia pihak ketiga seperti SideSwap, melewati penundaan penyelesaian untuk likuiditas yang lebih cepat.


#### Modul Keamanan Perangkat Keras (HSM)

Keamanan ditegakkan secara ketat melalui perangkat keras. Para fungsionaris tidak menyimpan [kunci pribadi](https://planb.academy/resources/glossary/private-key) pada server standar; sebagai gantinya, mereka mengoperasikan Modul Keamanan Perangkat Keras (HSM). Perangkat ini terpisah dari logika server host dan diprogram dengan aturan yang ketat. Sebagai contoh, HSM akan menolak untuk menandatangani sebuah blok jika tingginya tidak lebih besar dari yang sebelumnya, mencegah penulisan ulang riwayat. Model keamanan "lawan" ini mengasumsikan bahwa server host dapat disusupi, memastikan bahwa kunci tetap aman walaupun lokasi fisiknya dibobol.


## Dasar-dasar Elements


<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>


:::video id=5652dcb2-4303-484c-8be5-d98063b39c1c:::

### Elements: Fondasi dari Liquid


Elements adalah platform blockchain sumber terbuka yang berasal dari basis kode Bitcoin Core. Platform ini memperluas fungsionalitas Bitcoin dengan mengaktifkan sidechains-blockchain independen yang dapat mentransfer aset ke dan dari Bitcoin. Sementara Bitcoin Core memberi kekuatan pada jaringan Bitcoin, Elements adalah mesin perangkat lunak di belakang Liquid Network dan sidechain khusus lainnya.


Hubungannya sangat mudah: Liquid adalah "contoh" spesifik dari sidechain Elements, yang dikonfigurasikan untuk penggunaan produksi dengan model konsensus federasi. Pengembang yang terbiasa dengan Bitcoin akan menemukan Elements yang intuitif, karena Elements mempertahankan antarmuka RPC (Panggilan Prosedur Jarak Jauh) yang sama dan struktur baris perintah (`elements-cli`, `elements-d`, `elements-qt`). Perbedaan utama terletak pada konfigurasi: pengaturan `chain=liquidv1` menghubungkan sebuah [node](https://planb.academy/resources/glossary/node) ke jaringan utama Liquid, sementara `chain=elementsregtest` menjalankan lingkungan pengujian regresi lokal di mana para pengembang dapat melakukan blok generate secara instan dan melakukan pengujian tanpa ketergantungan eksternal.


#### Penerbitan Aset

Fitur yang menonjol dari Elements adalah penerbitan aset asli. Tidak seperti Ethereum, di mana token adalah kontrak pintar yang kompleks, aset dalam Elements adalah warga kelas satu yang dibuat melalui perintah RPC sederhana (`issueasset`).


- Pengenal Unik:** Setiap aset mendapatkan ID heksadesimal 64 karakter yang unik.
- Token Penerbitan Ulang:** Penerbit dapat secara opsional membuat token penerbitan ulang, yang memberikan hak kepada pemegangnya untuk mencetak lebih banyak aset di kemudian hari (berguna untuk stablecoin atau token keamanan).
- Asset Registry:** Karena ID hex tidak dapat dibaca oleh manusia, Blockstream Asset Registry memetakan ID ini ke nama dan ticker (misalnya, "USDT"), mirip dengan DNS untuk aset.


### Privasi melalui Confidential Transactions


Elements mengatasi salah satu keterbatasan utama blockchain publik: kurangnya privasi komersial. Pada Bitcoin, setiap jumlah transaksi dapat dilihat oleh dunia. Elements memperkenalkan **Confidential Transactions (CT)**, yang secara kriptografis membutakan jumlah dan jenis aset namun tetap memungkinkan jaringan untuk memverifikasi keabsahan transaksi.


Hal ini dicapai dengan menggunakan **Komitmen Pedersen** dan **Bukti Rentang**.


- Komitmen Pedersen** menggantikan jumlah yang terlihat dengan komitmen kriptografi. Karena enkripsi homomorfis, validator dapat memeriksa bahwa *Komitmen Masukan = Komitmen Keluaran + Biaya* tanpa melihat nilai sebenarnya.
- Range Proofs** mencegah pengguna untuk menciptakan uang secara tiba-tiba (contohnya, dengan menggunakan bilangan negatif) dengan membuktikan secara matematis bahwa nilai yang disembunyikan adalah sebuah bilangan bulat positif dalam sebuah range yang valid.


Bagi pengamat luar, Transaksi Rahasia menunjukkan input dan output yang valid, namun mengaburkan *apa* yang dikirim dan *berapa banyak*. Hanya pengirim dan penerima (yang memiliki kunci yang membutakan) yang dapat melihat data cleartext.


### Pengembangan dan Alur Kerja RPC


Berinteraksi dengan node Elements terutama dilakukan melalui antarmuka JSON-RPC. Ini memungkinkan aplikasi yang ditulis dalam Python, JavaScript, atau Go untuk berkomunikasi dengan blockchain.



- Pengaturan:** Pengembang biasanya memulai dalam mode `regtest`. Hal ini memungkinkan pembuatan blok secara instan (`generateblock`) untuk mengonfirmasi transaksi dengan segera, melewati waktu blok 1 menit dari jaringan langsung.
- Perintah:** Perintah standar Bitcoin seperti `getblockchaininfo` tersedia, di samping perintah khusus Elements seperti `dumpblindingkey` (untuk mengaudit CT) atau `pegin` (untuk memindahkan BTC ke dalam sidechain).
- Alias:** Untuk mengelola beberapa node (misalnya, "pengirim" dan "penerima" untuk pengujian), pengembang sering menggunakan shell alias seperti `e1-cli` dan `e2-cli` yang menunjuk ke direktori data yang berbeda, yang mensimulasikan jaringan [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p) pada satu mesin.


Arsitektur ini memberdayakan pengembang untuk membangun aplikasi keuangan yang canggih-seperti platform sekuritas atau gerbang pembayaran pribadi-menggunakan perkakas yang kuat dan familiar dari ekosistem Bitcoin.


## Menghubungkan Lapisan Bitcoin


<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>


:::video id=31368c02-b979-44d7-b217-ceed96c7ca5c:::

### Infrastruktur Lintas-Layer dan HTLC


Ekosistem Bitcoin telah berevolusi menjadi arsitektur berlapis-lapis, dengan Mainchain yang menyediakan penyelesaian, Lightning yang menawarkan kecepatan, dan Liquid yang memungkinkan kemampuan aset tingkat lanjut. Memindahkan nilai di antara lapisan-lapisan ini tanpa perantara terpusat membutuhkan primitif kriptografi yang tidak dapat dipercaya: [Hash](https://planb.academy/resources/glossary/hash-function) Time Locked Contract ([HTLC](https://planb.academy/resources/glossary/htlc)).


HTLC menciptakan [saluran pembayaran](https://planb.academy/resources/glossary/payment-channel) bersyarat yang menghubungkan sistem independen secara atomis. Ini berfungsi melalui dua batasan utama: **hash lock** dan **waktu lock**.


- Kunci Hash:** Dana dapat segera dibelanjakan jika penerima mengungkapkan "gambar awal" rahasia yang cocok dengan hash kriptografi tertentu.
- Kunci Waktu:** Jika penerima gagal mengungkapkan rahasia dalam jangka waktu yang ditentukan (tinggi blok), pengirim asli dapat mengambil kembali dana tersebut.


Struktur jalur ganda ini memastikan keamanan. Dalam pertukaran lintas lapisan, kunci hash yang sama digunakan pada kedua jaringan. Ketika penerima mengungkapkan rahasia untuk mengklaim dana pada satu lapisan (misalnya, Liquid), rahasia tersebut akan terlihat oleh pengirim, yang kemudian dapat menggunakannya untuk mengklaim dana timbal balik pada lapisan lainnya (misalnya, Lightning). Pengikatan kriptografi ini menjamin bahwa swap akan berhasil dilakukan oleh kedua belah pihak atau gagal untuk keduanya, sehingga menghilangkan risiko satu pihak kehilangan dana sementara pihak lainnya mendapatkannya.


### Peningkatan Taproot dan MuSig2


HTLC lama ([SegWit](https://planb.academy/resources/glossary/segwit) v0) berfungsi dengan baik tetapi memiliki kekurangan dalam hal privasi dan efisiensi. Mereka membutuhkan penerbitan seluruh logika [skrip](https://planb.academy/resources/glossary/script) on-chain, membuat transaksi swap mudah diidentifikasi oleh analis blockchain dan lebih mahal karena ukuran datanya. Pengenalan [Taproot](https://planb.academy/resources/glossary/taproot) (SegWit v1) dan protokol MuSig2 telah merevolusi arsitektur ini.


Taproot memungkinkan untuk **Key Aggregation** melalui MuSig2. Daripada mengungkapkan skrip yang kompleks dengan beberapa [public key](https://planb.academy/resources/glossary/public-key), MuSig2 mengizinkan para peserta swap untuk menggabungkan key mereka ke dalam satu public key yang diagregasi.


- "Jalur Kunci" kooperatif:** Jika kedua belah pihak menyetujui pertukaran ("jalur bahagia"), mereka akan menandatangani bersama transaksi tersebut. Bagi jaringan, ini terlihat identik dengan pembayaran standar dengan tanda tangan tunggal. Ini menghabiskan ruang blok minimal dan sama sekali tidak mengungkapkan informasi tentang kondisi swap.
- "Jalur Skrip" yang berlawanan:** Jika salah satu pihak menjadi tidak responsif atau jahat, skrip yang mendasarinya (yang berisi kunci hash/waktu) baru akan diungkap saat itu juga. Ini diatur dalam sebuah pohon [Merkle](https://planb.academy/resources/glossary/merkle-tree), yang memungkinkan pihak yang jujur untuk mengekspos hanya cabang tertentu yang diperlukan untuk memulihkan dana, menjaga logika kontrak lainnya tetap tersembunyi.


### Implementasi Praktis: Liquid-Penukar Petir


Dalam praktiknya, protokol ini memungkinkan pertukaran yang mulus di antara lapisan Bitcoin. Pertukaran Liquid-ke-Lightning yang khas dimulai dengan klien yang meminta pertukaran dari penyedia layanan. Klien memberikan [faktur Lightning](https://planb.academy/resources/glossary/invoice-lightning), dan penyedia mengunci Liquid Bitcoin (L-BTC) yang setara dengan Liquid ke dalam alamat HTLC yang mendukung Taproot.


Atomisitas diberlakukan ketika pembayaran diselesaikan. Untuk mengklaim L-BTC, penyedia layanan harus memiliki gambar awal. Mereka mendapatkan gambar awal ini hanya ketika mereka berhasil membayar faktur Lightning klien. Saat pembayaran Lightning diselesaikan, preimage terungkap, memungkinkan penyedia untuk membuka dana Liquid.


#### Wallet Abstraksi dan Manajemen UTXO

Untuk pengguna akhir, kerumitan ini sepenuhnya abstrak. Dompet modern seperti Aqua menangani pembuatan kunci, pembuatan faktur, dan proses penandatanganan di latar belakang. Pengguna cukup "membayar" faktur Lightning menggunakan saldo Liquid mereka. Di belakang layar, layanan ini mengelola konsolidasi [UTXO](https://planb.academy/resources/glossary/utxo), secara berkala menyapu hasil yang kecil, tidak diklaim, atau dikembalikan untuk menjaga efisiensi [wallet](https://planb.academy/resources/glossary/wallet) dan meminimalkan dampak biaya selama periode lalu lintas tinggi.


## Gambaran Umum Liquid Network


<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>


:::video id=0bac0a62-90f2-41da-ac7c-330c0604bc61:::

### Arsitektur dan Konsensus Liquid Network


Liquid Network beroperasi sebagai sidechain federasi yang dibangun di atas basis kode **Elements**. Sementara Elements - fork dari Bitcoin Core - menyediakan fondasi perangkat lunak, Liquid adalah implementasi jaringan produksi. Tidak seperti Bitcoin, yang bergantung pada [mining](https://planb.academy/resources/glossary/mining) yang kompetitif, Liquid menggunakan model **Konsensus Gabungan**.


Jaringan ini dikelola oleh lima belas "fungsionaris" yang didistribusikan secara global Entitas-entitas ini mengoperasikan server khusus yang menjalankan dua peran penting:

1.  **Produksi Blok:** Para fungsionaris bergiliran membuat blok dalam jadwal round-robin deterministik, menghasilkan blok baru setiap menit.

2.  **Penandatanganan Blok:** Agar blok menjadi sah, blok harus ditandatangani oleh setidaknya 11 dari 15 fungsionaris.


Ambang batas 11-dari-15 ini memastikan jaringan dapat mentolerir kegagalan hingga empat node tanpa berhenti. Keuntungan utama dari pertukaran ini adalah **kepastian akhir yang deterministik**. Sementara Bitcoin berurusan dengan probabilitas, Liquid mencapai kepastian penyelesaian setelah dua blok (sekitar dua menit). Setelah satu blok memiliki satu konfirmasi di atasnya, rantai tidak dapat diatur ulang, membuatnya sangat efektif untuk arbitrase dan penyelesaian yang cepat.


### Confidential Transactions dan Aset Asli


Fitur penentu Liquid adalah penggunaan default **Confidential Transactions (CT)**. Pada Bitcoin mainchain, pengirim, penerima, dan jumlah bersifat publik. Liquid memperbaiki hal ini dengan menyamarkan jumlah dan jenis aset secara kriptografis, namun tetap membiarkan alamat pengirim dan penerima terlihat untuk verifikasi.


Untuk memastikan bahwa pengguna tidak dapat mencetak uang (contohnya, dengan mengirimkan jumlah negatif), Liquid menggunakan **Komitmen Pedersen** dan **Bukti Rentang**. Primitif kriptografi ini memungkinkan jaringan untuk memverifikasi bahwa *Input = Output + Biaya* dan semua nilai adalah bilangan bulat positif, tanpa harus mengungkapkan angka-angka spesifik ke buku besar publik. Hanya peserta yang memegang kunci yang membutakan yang dapat melihat data yang didekripsi.


#### Penerbitan Aset

Liquid memperlakukan semua aset sebagai "asli" Baik itu Liquid Bitcoin (L-BTC), stablecoin seperti USDT, atau sekuritas token, semuanya memiliki arsitektur yang sama. Menerbitkan aset tidak memerlukan kontrak pintar - hanya dengan panggilan RPC yang sederhana.


- Aset yang Tidak Diatur:** Dapat dikeluarkan tanpa izin oleh siapa pun.
- Aset yang Diatur:** Memanfaatkan Platform Manajemen Aset Blockstream (AMP), penerbit dapat menegakkan aturan kepatuhan (seperti KYC/AML) dengan meminta tanda tangan kedua dari server otorisasi sebelum aset dapat dipindahkan.


### Pasak Dua Arah dan Federasi Dinamis


Jembatan antara Bitcoin dan Liquid adalah **Pasak Dua Arah**. Ini memungkinkan pengguna untuk memindahkan BTC ke sidechain (Peg-in) dan kembali ke mainchain (Peg-out).


**Proses Peg-in:**

Ini tidak memerlukan izin. Seorang pengguna mengirimkan BTC ke alamat yang dikontrol oleh federasi. Untuk melindungi dari reorganisasi blockchain Bitcoin, dana ini harus menunggu **102 konfirmasi** (sekitar 17 jam) sebelum L-BTC yang setara dicetak di sidechain.


**Proses Peg-out:**

Untuk kembali ke Bitcoin, L-BTC dibakar. Namun, untuk mencegah pencurian cadangan Bitcoin yang mendasarinya, peg-out tidak sepenuhnya otomatis. Mereka membutuhkan otorisasi dari anggota yang memegang **Kunci Otorisasi Peg-Out (PAK)**. Dana Bitcoin sendiri diamankan dalam 11 dari 15 multisignature wallet, dengan kunci yang disimpan dalam Modul Keamanan Perangkat Keras (HSM) yang terputus dari server utama para fungsionaris.


**Federasi Dinamis (Dynafed):**

Untuk memastikan umur panjang, Liquid menggunakan Dynafed, sebuah protokol yang memungkinkan jaringan untuk merotasi fungsionaris atau memperbarui parameter tanpa fork yang keras. Jika ada petugas yang perlu diganti, jaringan akan menyiarkan transaksi transisi. Setelah periode tumpang tindih selama dua minggu, konfigurasi baru mengambil alih, memungkinkan federasi untuk berkembang dengan mulus sambil mempertahankan waktu kerja yang berkelanjutan.


## Ekosistem dan Pasar Modal


<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>


:::video id=07e0b82f-2d60-4eb3-9b5d-2ccb7ad06e8a:::

### Liquid Network: Strategi dan Ekosistem Bisnis


Liquid lebih dari sekadar sidechain teknis; ini adalah lapisan infrastruktur yang berfokus pada bisnis yang dirancang untuk menangani persyaratan kompleks pasar modal yang tidak dapat didukung secara efisien oleh Bitcoin mainchain. Sementara [Lightning Network](https://planb.academy/resources/glossary/lightning-network) dioptimalkan untuk pembayaran frekuensi tinggi dan bernilai rendah, Liquid menargetkan transfer bernilai tinggi, penerbitan aset, dan penyelesaian antar-bursa.


Ekosistem ini digerakkan oleh **Liquid Federation**, sebuah konsorsium yang terdiri dari ~73 perusahaan termasuk bursa, meja perdagangan, dan penyedia infrastruktur. Model kolaboratif ini mencerminkan lembaga kliring keuangan tradisional tetapi beroperasi dengan transparansi yang lebih besar dan waktu penyelesaian yang jauh lebih singkat (2 menit vs T+2 hari).


### Tokenisasi Aset Dunia Nyata (RWA)


Kasus bisnis inti untuk Liquid adalah "Tokenisasi" - merepresentasikan nilai dunia nyata (saham, obligasi, kontrak mining) sebagai token digital pada blockchain. Ini menawarkan tiga keuntungan utama:

1.  **24/7 Pasar Global:** Menghapus jam perbankan dan pembatasan geografis.

2.  **Efisiensi Operasional:** Menghilangkan kesalahan rekonsiliasi melalui buku besar bersama yang tidak dapat diubah.

3.  **Penyelesaian Otomatis:** Mengurangi risiko mitra pengimbang dengan memastikan pengiriman terjadi bersamaan dengan pembayaran.


#### Aset yang Diatur dan AMP

Sebagian besar aset institusional tidak dapat diperdagangkan tanpa izin karena persyaratan hukum. Platform Manajemen Aset (AMP) adalah standar teknis yang memberlakukan peraturan ini.


- Daftar putih:** Emiten dapat membatasi kepemilikan dan perdagangan ke alamat yang diverifikasi KYC.
- Kontrol Multisig:** Tindakan kepatuhan (seperti membekukan dana yang dicuri atau menerbitkan kembali token yang hilang) dikelola melalui otorisasi multi tanda tangan, memastikan tidak ada karyawan yang dapat bertindak secara sepihak.


Infrastruktur ini sudah aktif hari ini. Platform seperti **Stalker** menyediakan layanan tokenisasi end-to-end di Eropa, sementara **Sideswap** bertindak sebagai pertukaran terdesentralisasi dan wallet non-kustodian, memungkinkan perdagangan aset peer-to-peer seperti **Blockstream Mining Note (BMN) ** dan saham MicroStrategy yang ditokenisasi (CMSTR).


### Kesuksesan di Dunia Nyata: Studi Kasus Mayfell


Bukti paling kuat dari kegunaan Liquid berasal dari **Mayfell** di Meksiko. Di pasar di mana pembiayaan tradisional bergantung pada surat promes kertas-yang rentan terhadap kehilangan, penipuan, dan pemrosesan yang lambat-Mayfell memindahkan seluruh infrastruktur ke Liquid.



- Skala:** Lebih dari 25.000 surat utang yang diterbitkan, mewakili nilai **$1,5 miliar+**.
- Privasi:** Dengan menggunakan Confidential Transactions, jumlah pinjaman hanya dapat dilihat oleh pemberi pinjaman dan peminjam, menjaga privasi komersial sekaligus memungkinkan auditor untuk memverifikasi integritas buku besar.
- Dampak:** Dengan menghubungkan pemberi pinjaman non-bank ke pasar modal global melalui blockchain, Mayfell mengurangi biaya dan memperluas akses kredit untuk UKM Meksiko, menunjukkan bahwa proposisi nilai Liquid jauh melampaui perdagangan spekulatif.


### Penentuan Posisi Strategis vs Rantai Lainnya


Liquid bersaing di pasar yang penuh sesak dengan platform tokenisasi (Ethereum, Solana, dll.), tetapi memiliki keunggulan strategis yang berbeda:


- Kejelasan Peraturan:** Liquid menggunakan Bitcoin (L-BTC) sebagai aset aslinya. Ia tidak memiliki token yang telah ditambang sebelumnya atau ICO, menghindari risiko "keamanan tidak terdaftar" yang mengganggu blockchain L1 lainnya.
- Stabilitas:** Tidak seperti model akun Ethereum di mana transaksi yang gagal masih membakar biaya gas, model Liquid UTXO bersifat deterministik dan dapat diandalkan untuk data keuangan yang sangat penting.
- Privasi:** Kerahasiaan default adalah persyaratan bagi sebagian besar lembaga keuangan, sebuah fitur yang ditawarkan Liquid secara native yang sulit diimplementasikan oleh rantai publik tanpa add-on yang rumit.


Bagi para pengembang, ekosistem ini menawarkan peluang yang jelas: membangun alat (dasbor, dompet, integrasi kepatuhan) yang menjembatani keuangan tradisional dengan lapisan penyelesaian yang aman dari Bitcoin.


## AMP aliran blok


<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>


:::video id=f00822b4-dc1a-46ff-adfc-ff7c97a0024d:::

### Blockstream AMP: Kontrol Aset yang Diizinkan pada Liquid


Blockstream AMP (Platform Manajemen Aset) berfungsi sebagai lapisan infrastruktur penting pada Liquid Network, yang dirancang khusus untuk penerbit sekuritas digital teregulasi dan stablecoin. Meskipun Liquid menyediakan lapisan dasar tanpa izin dengan penerbitan aset asli, entitas yang teregulasi sering kali membutuhkan pengawasan dan kemampuan kepatuhan yang ketat. AMP menjembatani kesenjangan ini dengan memperkenalkan lapisan kontrol berizin atas aset tertentu tanpa mengorbankan manfaat privasi dari Liquid.


Proposisi nilai inti platform ini bertumpu pada dua kemampuan utama: visibilitas penerbit yang komprehensif dan otorisasi transaksi. Tidak seperti aset Liquid standar yang jumlah dan jenisnya tidak dapat diketahui oleh semua orang kecuali partisipan, aset AMP memungkinkan penerbit untuk mempertahankan jejak audit unblinded sepenuhnya. Transparansi ini sangat penting untuk pelaporan regulasi dan audit internal. Selain itu, AMP memberlakukan model otorisasi yang ketat melalui mekanisme penandatanganan bersama. Setiap transfer aset AMP memerlukan tanda tangan dari server AMP. Hal ini memungkinkan penerbit untuk menegakkan aturan yang kompleks off-chain-seperti membekukan akun, memasukkan investor yang terakreditasi ke dalam daftar putih, atau memberlakukan batas transfer-secara efektif bertindak sebagai penjaga gerbang yang terpusat dalam jaringan yang terdesentralisasi.


#### Pengorbanan Operasional

Arsitektur ini memperkenalkan pertukaran tertentu. Sistem ini bergantung pada ketersediaan server AMP; jika server bertindak sebagai penandatangan bersama dan offline, likuiditas aset akan terhenti. Selain itu, meskipun privasi pengguna-ke-pengguna dipertahankan, investor harus menerima bahwa penerbit memiliki visibilitas penuh ke dalam kepemilikan mereka. Model ini sangat ideal untuk token keamanan yang sesuai tetapi tidak cocok untuk [mata uang kripto](https://planb.academy/resources/glossary/cryptocurrency) yang tahan sensor.


### Evolusi Arsitektur dan Jalur Integrasi


Ekosistem AMP saat ini sedang bertransisi dari iterasi pertamanya ke arsitektur "Versi 2" yang lebih fleksibel dan dapat dioperasikan. Sistem lama mengharuskan penerbit untuk mempertahankan node Elements yang tersinkronisasi sepenuhnya dan memaksa pengembang untuk sangat bergantung pada SDK Green yang monolitik. Meskipun fungsional, hal ini menciptakan hambatan teknis yang tinggi untuk masuk dan membatasi pilihan wallet.


Arsitektur generasi berikutnya secara fundamental menyederhanakan persyaratan ini dengan mengalihkan kompleksitas ke server. Pada model baru ini, server AMP menangani pekerjaan berat konstruksi transaksi, pemilihan UTXO, dan penghitungan biaya. Ini memberikan penerbit dengan Transaksi Elements yang Ditandatangani Sebagian (Partially Signed Elements Transaction (PSET) yang hanya membutuhkan tanda tangan. Pendekatan "server pintar, wallet bodoh" ini menghilangkan kebutuhan penerbit untuk menjalankan node penuh dan memungkinkan penggunaan dompet perangkat keras dan pengaturan multisignature standar untuk manajemen perbendaharaan.


Bagi pengembang, evolusi ini berarti beralih dari SDK berpemilik ke deskriptor standar dan alur kerja PSET. Dompet sekarang dapat mendaftarkan deskriptor multisignature ke server AMP untuk menetapkan hak otorisasi. Hal ini menyelaraskan pengembangan AMP dengan standar Bitcoin wallet yang lebih luas, sehingga integrasi dapat diakses oleh aplikasi apa pun yang mampu menangani format PSBT/PSET. Pengembang yang membuat aplikasi saat ini didorong untuk menggunakan alat bantu seperti Kit Liquid Wallet (LWK), yang mendukung arsitektur modern berbasis deskriptor ini, yang memastikan aplikasi mereka terbukti di masa depan untuk standar AMP yang baru.


### Ekosistem dan Kerahasiaan Liquid Wallet


Membangun aplikasi pada Liquid membutuhkan navigasi stack yang lebih kompleks daripada pengembangan Bitcoin standar karena adanya fitur-fitur seperti aset asli dan Confidential Transactions. Ekosistem ini didukung oleh arsitektur berlapis: pustaka tingkat rendah seperti `secp256k1-zkp` menangani primitif kriptografi, sementara toolkit tingkat tinggi mengelola logika wallet.


Secara historis, Green Development Kit (GDK) memberikan solusi yang komprehensif namun kaku. Alternatif modern adalah Liquid Wallet Kit (LWK), yang menawarkan pendekatan modular. LWK memisahkan masalah ke dalam peti yang berbeda-menangani deskriptor, penandatanganan, dan komunikasi perangkat keras secara independen-memberi pengembang fleksibilitas untuk membangun solusi khusus tanpa overhead perpustakaan monolitik.


#### Penanganan Confidential Transactions

Tantangan yang paling berbeda dalam ekosistem ini adalah mengelola siklus hidup yang membutakan. Dalam Liquid, output transaksi dienkripsi menggunakan pertukaran kunci Elliptic Curve Diffie-Hellman (ECDH). Pengirim menggunakan kunci publik blinding dari penerima untuk mengenkripsi jumlah dan jenis aset, menghasilkan sebuah bukti rentang yang memverifikasi keabsahan transaksi tanpa mengungkapkan nilainya.


Agar wallet dapat berfungsi, ia harus berhasil membalikkan proses ini. Ketika wallet mendeteksi sebuah transaksi yang masuk, ia akan mencoba untuk membuka kunci penyembunyian menggunakan kunci penyembunyian pribadinya. Jika rahasia bersama cocok, wallet dapat mendekripsi nilai dan menambahkannya ke saldo pengguna. Proses ini sangat intensif secara komputasi dan membutuhkan manajemen yang tepat dari faktor pemblokiran untuk memastikan transaksi seimbang secara matematis, sebuah kerumitan yang ingin disederhanakan oleh alat seperti LWK untuk pengembang.


# Teknis


<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>

<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>


## Breez SDK - Tanpa Anggukan


<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>


:::video id=1a6289b5-fdae-4320-b5b1-41925150108c:::

### Pengantar ke Breez Liquid SDK


Breez Liquid SDK adalah toolkit sumber terbuka yang bersifat self-custodial yang dirancang untuk menjembatani kesenjangan antara Liquid Network dan ekosistem Bitcoin yang lebih luas. Misi utamanya adalah mengabstraksikan kompleksitas manajemen node Lightning Network dan pertukaran atom, yang memungkinkan pengembang untuk membangun aplikasi keuangan tanpa gesekan.


Dibangun dengan filosofi "mobile-first", logika inti ditulis dalam Rust untuk kinerja dan keamanan, tetapi menggunakan UniFFI (Unified Foreign Function Interface) untuk menyediakan binding asli untuk Kotlin, Swift, Python, C#, Dart, dan Flutter. Hal ini memastikan bahwa pengembang dapat mengintegrasikan fungsionalitas Bitcoin ke dalam lingkungan yang mereka sukai tanpa mengelola operasi kriptografi tingkat rendah.


**Jenis Transaksi yang Didukung:**

SDK beroperasi dengan Liquid sebagai "home base" SDK ini unggul dalam tiga operasi spesifik:

1.  **Liquid ke Liquid:** Transfer langsung on-chain.

2.  **Liquid-ke-Lightning:** Membayar faktur Lightning menggunakan dana Liquid.

3.  **Liquid ke Bitcoin:** Menukar dana secara langsung ke Bitcoin mainchain.


*Catatan: SDK tidak mendukung transaksi Lightning-to-Lightning atau Bitcoin-ke-Bitcoin secara langsung. Ini benar-benar alat yang berpusat pada Liquid.*


### Arsitektur Pembayaran: Pertukaran Kapal Selam


Untuk mencapai interoperabilitas antara Liquid, Lightning, dan Bitcoin tanpa kustodian terpusat, Breez mengandalkan **Submarine Swap**. Ini adalah operasi atomik di mana transaksi berhasil diselesaikan dengan sukses di kedua jaringan atau gagal di keduanya, memastikan dana tidak pernah hilang dalam perjalanan.


#### Kirim Petir (Pertukaran Kapal Selam)

Ketika pengguna membayar faktur Lightning, SDK menyiarkan transaksi "penguncian" pada Liquid Network. Hal ini secara efektif menempatkan dana dalam escrow. Penyedia swap (Boltz) mendeteksi hal ini, membayar faktur Lightning, dan kemudian menggunakan gambar awal pembayaran (tanda terima kriptografi) untuk mengklaim dana Liquid yang terkunci.


#### Penerima Petir (Penukaran Kapal Selam Terbalik)

Menerima Lightning adalah proses sebaliknya. Pengguna membuat faktur, dan penyedia swap mengunci dana pada Lightning Network. SDK memonitor proses ini melalui WebSockets. Setelah penguncian dikonfirmasi, SDK secara otomatis mengeksekusi transaksi klaim untuk memindahkan dana yang setara ke dalam Liquid wallet pengguna.


#### Bitcoin Rantai Silang

Untuk transfer Liquid ke Bitcoin, arsitekturnya menggunakan mekanisme "dual-swap". Transaksi penguncian terjadi pada kedua rantai secara bersamaan. Pengirim mengklaim dana pada Bitcoin, sedangkan penerima mengklaim dana pada Liquid. Hal ini memungkinkan penghubung tanpa kepercayaan tanpa ketergantungan pada federated peg-out atau bursa terpusat.


### Pengembang Interface dan Manajemen Otomatis


Breez SDK menyederhanakan pengalaman pengembang dengan memadatkan aliran keuangan yang kompleks menjadi proses tiga langkah standar: **Hubungkan, Persiapkan, dan Jalankan**.


1.  **Menghubungkan:** Menginisialisasi wallet, menyinkronkan dengan blockchain menggunakan Liquid Wallet Kit (LWK), dan membuat koneksi WebSocket untuk pemantauan waktu nyata.

2.  **Persiapan:** Sebelum melakukan pengiriman dana, langkah ini menghitung dan mengembalikan semua biaya jaringan dan biaya swap yang terkait, sehingga UI dapat menampilkan total yang jelas kepada pengguna.

3.  **Eksekusi:** Langkah ini membuat transaksi, menyiarkannya, dan memulai swap.


#### Mekanisme Keamanan Otomatis

Salah satu fitur SDK yang paling penting adalah **Manajemen Pengembalian Dana Otomatis**. Jika terjadi kegagalan jaringan atau rekanan yang tidak kooperatif, dana secara teoritis dapat terjebak dalam kontrak yang terkunci waktu. SDK mengabstraksikan logika pemulihan sepenuhnya. SDK memonitor keadaan setiap swap; jika swap gagal atau waktu habis, SDK secara otomatis membuat dan menyiarkan transaksi pengembalian dana untuk mengembalikan dana ke wallet pengguna.


Selain itu, SDK menangani **Resolusi Metadata**. SDK ini menggabungkan data swap off-chain (disediakan oleh swapper Boltz) dengan riwayat transaksi on-chain. Hal ini memastikan bahwa riwayat transaksi pengguna dapat dibaca oleh manusia, menampilkan detail faktur dan konteks pembayaran, bukan hanya hash transaksi heksadesimal mentah.


# Bagian Akhir


<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>


## Ulasan & Peringkat


<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>


<isCourseReview>true</isCourseReview>

## Ujian Akhir


<chapterId>b13c4aa8-ced6-11f0-8515-afd3f381a001</chapterId>

<isCourseExam>true</isCourseExam>

## Kesimpulan


<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>

<isCourseConclusion>true</isCourseConclusion>