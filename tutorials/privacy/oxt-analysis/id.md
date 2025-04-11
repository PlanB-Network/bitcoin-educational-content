---
name: OXT - Chain Analysis
description: Kuasai dasar-dasar analisis rantai pada Bitcoin
---
![cover](assets/cover.webp)

***PERINGATAN:** Menyusul penangkapan pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, **situs web OXT.me saat ini tidak dapat diakses**. Namun, masih mungkin bahwa alat ini akan diluncurkan kembali dalam beberapa minggu mendatang. Sementara itu, Anda masih dapat memanfaatkan tutorial ini untuk memahami dasar-dasar analisis rantai pada Bitcoin. Semua heuristik dan pola yang disajikan di sini tetap berlaku untuk transaksi Bitcoin. Meskipun alat-alat ini kurang optimal dibandingkan OXT, Anda dapat sementara menggunakan [Mempool.space](https://mempool.space/) atau [Bitcoin Explorer](https://bitcoinexplorer.org/) untuk mempraktikkan konsep teoretis artikel ini.*

_Kami terus mengikuti perkembangan kasus ini serta perkembangan terkait alat-alat yang terkait. Yakinlah bahwa kami akan memperbarui tutorial ini seiring informasi baru tersedia._

_Tutorial ini disediakan hanya untuk tujuan pendidikan dan informasi. Kami tidak mendukung atau mendorong penggunaan alat-alat ini untuk tujuan kriminal. Tanggung jawab setiap pengguna untuk mematuhi hukum di yurisdiksi mereka._

---

Dalam artikel ini, Anda akan mempelajari dasar-dasar teoretis yang diperlukan untuk memulai analisis rantai dasar pada Bitcoin, dan yang lebih penting, untuk memahami bagaimana mereka yang mengamati Anda beroperasi. Meskipun artikel ini bukan tutorial praktis tentang alat OXT (topik yang akan kami bahas dalam tutorial mendatang), artikel ini mengumpulkan sejumlah pengetahuan penting untuk penggunaannya. Untuk setiap model, metrik, dan indikator yang disajikan, link ke transaksi contoh pada OXT disediakan, yang akan memungkinkan Anda untuk lebih memahami penggunaannya dan untuk berlatih bersamaan dengan membaca Anda.

## Pendahuluan
Salah satu fungsi uang adalah untuk menyelesaikan masalah kebetulan ganda dari keinginan. Dalam sistem berbasis barter, menyelesaikan pertukaran tidak hanya memerlukan menemukan individu yang menawarkan barang yang memenuhi kebutuhan saya, tetapi juga menyediakan mereka dengan barang bernilai setara yang memuaskan kebutuhan mereka sendiri. Menemukan keseimbangan ini terbukti kompleks. Itulah mengapa kita beralih ke uang, yang memungkinkan kita untuk memindahkan nilai baik dalam ruang maupun waktu.

Agar uang dapat menyelesaikan masalah ini, sangat penting bahwa pihak yang menyediakan barang atau jasa yakin akan kemampuan mereka untuk menghabiskan jumlah tersebut nanti. Dengan demikian, setiap individu rasional yang bersedia menerima sejumlah uang, baik digital maupun fisik, akan memastikan bahwa itu memenuhi dua kriteria fundamental:
- Uang tersebut harus utuh dan asli;
- dan tidak boleh digunakan dua kali.

Jika kita menggunakan uang fisik, karakteristik pertama adalah yang paling kompleks untuk ditegaskan. Pada periode yang berbeda dalam sejarah, integritas koin logam sering terpengaruh oleh praktik seperti pemotongan atau pengeboran. Misalnya, selama zaman Romawi kuno, umum untuk warga negara mengikis tepi koin emas untuk mengumpulkan sedikit logam berharga, sambil tetap menyimpannya untuk transaksi masa depan. Inilah sebabnya mengapa alur kemudian dicap pada tepi koin. Keaslian juga merupakan karakteristik yang sulit untuk diverifikasi pada media moneter fisik. Saat ini, teknik untuk memerangi pemalsuan semakin kompleks, memaksa pedagang untuk berinvestasi dalam sistem verifikasi yang mahal.

Di sisi lain, karena sifatnya, pengeluaran ganda bukanlah masalah bagi mata uang fisik. Jika saya memberi Anda uang kertas €10, itu secara tak terelakkan meninggalkan kepemilikan saya untuk masuk ke milik Anda, dengan demikian mengecualikan kemungkinan pengeluaran berulang dari unit moneter yang diwakilinya.
Untuk mata uang digital, tantangannya berbeda. Memastikan keaslian dan integritas sebuah koin seringkali lebih sederhana, tetapi memastikan tidak adanya pengeluaran ganda lebih kompleks. Setiap barang digital pada dasarnya adalah informasi. Tidak seperti barang fisik, informasi tidak terbagi selama pertukaran tetapi berkembang biak dengan cara berlipat ganda. Sebagai contoh, jika saya mengirimkan dokumen kepada Anda melalui email, dokumen itu kemudian akan diduplikasi. Di pihak Anda, Anda tidak dapat memverifikasi dengan pasti bahwa saya telah menghapus dokumen asli.

Satu-satunya cara untuk menghindari duplikasi barang digital adalah dengan mengetahui semua pertukaran dalam sistem. Dengan cara ini, seseorang dapat mengetahui siapa yang memiliki apa dan memperbarui akun semua orang berdasarkan transaksi yang dilakukan. Inilah yang dilakukan, misalnya, dengan uang giral. Ketika Anda membayar €10 kepada seorang pedagang dengan kartu kredit, bank mencatat pertukaran ini dan memperbarui buku besar.

Pada Bitcoin, pencegahan pengeluaran ganda dilakukan dengan cara yang sama. Ini berusaha untuk mengonfirmasi ketiadaan transaksi yang telah menghabiskan koin yang bersangkutan. Jika koin tersebut belum pernah digunakan, maka kita dapat yakin bahwa tidak akan terjadi pengeluaran ganda. Ini adalah frase terkenal dari Satoshi Nakamoto dalam White Paper: "*Satu-satunya cara untuk mengonfirmasi ketiadaan transaksi adalah dengan mengetahui semua transaksi.*"

Berbeda dengan model perbankan, pada Bitcoin, kita tidak ingin harus mempercayai entitas pusat. Oleh karena itu, semua pengguna harus dapat mengonfirmasi ketiadaan pengeluaran ganda ini, tanpa mengandalkan pihak ketiga. Dengan demikian, semua orang harus mengetahui semua transaksi Bitcoin.

Tepatnya, penyebaran informasi publik ini yang mempersulit perlindungan privasi pada Bitcoin. Dalam sistem perbankan tradisional, secara teori, hanya lembaga keuangan yang mengetahui transaksi yang dilakukan. Namun, pada Bitcoin, semua pengguna diberitahu tentang semua transaksi, melalui node masing-masing.

Karena kendala pada penyebaran ini, model privasi Bitcoin berbeda dari sistem perbankan. Dalam yang terakhir, transaksi dikaitkan dengan identitas pengguna, tetapi aliran informasi diputus antara pihak ketiga terpercaya dan publik. Dengan kata lain, bankir Anda tahu bahwa Anda membeli baguette setiap pagi di toko roti lokal, tetapi tetangga Anda tidak mengetahui semua transaksi ini. Dalam kasus Bitcoin, karena aliran informasi tidak dapat diputus antara transaksi dan domain publik, model privasi mengandalkan pemisahan identitas pengguna dari transaksi itu sendiri.
![analisis](assets/en/1.webp)
*Diagram terinspirasi oleh Satoshi Nakamoto dalam White Paper: Bitcoin: A Peer-to-Peer Electronic Cash System, bagian 10 "Privasi".*
Karena transaksi Bitcoin dibuat publik, menjadi mungkin untuk menetapkan tautan antara mereka untuk menarik informasi tentang pihak yang terlibat. Kegiatan ini bahkan merupakan spesialisasi tersendiri, yang umumnya disebut "analisis rantai". Dalam artikel ini, saya mengajak Anda untuk menjelajahi dasar-dasar analisis rantai untuk memahami bagaimana bitcoin Anda dilacak.

Sebagian besar perusahaan yang mengkhususkan diri dalam analisis rantai beroperasi sebagai kotak hitam, dan tidak mengungkapkan metodologi mereka. Oleh karena itu, sulit untuk mendapatkan informasi tentang praktik ini. Untuk penulisan artikel ini, saya terutama mengandalkan beberapa sumber terbuka yang tersedia:
- Sebagian besar artikel saya diambil dari seri empat artikel yang bernama: [Memahami Privasi Bitcoin dengan OXT](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923), diproduksi oleh Samourai Wallet pada tahun 2021;
- Saya juga menggunakan berbagai laporan dari [Penelitian OXT](https://medium.com/oxt-research), serta alat analisis rantai gratis mereka;
Secara lebih luas, pengetahuan saya berasal dari berbagai tweet dan konten dari [@LaurentMT](https://twitter.com/LaurentMT) dan [@ErgoBTC](https://twitter.com/ErgoBTC); Saya juga terinspirasi oleh [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) di mana saya berpartisipasi bersama [@louneskmt](https://twitter.com/louneskmt), [@TheoPantamis](https://twitter.com/TheoPantamis), [@Sosthene___](https://twitter.com/Sosthene___), dan [@LaurentMT](https://twitter.com/LaurentMT).

Saya ingin mengucapkan terima kasih kepada para penulis, pengembang, dan produser mereka. Tanpa berbagai konten dan perangkat lunak mereka, artikel ini tidak akan ada. Saya juga berterima kasih kepada para reviewer yang dengan teliti mengoreksi teks ini dan memberikan saya nasihat ahli mereka:
- [Gilles Cadignan](https://twitter.com/gillesCadignan);
- [Ludovic Lars](https://twitter.com/lugaxker) ([https://viresinnumeris.fr/](https://viresinnumeris.fr/)).

*Untuk informasi Anda, saya telah menambahkan miniglosarium teknis di akhir artikel untuk mendefinisikan beberapa istilah. Jika Anda melihat kata yang tidak Anda mengerti dengan tanda bintang, definisinya ada di bagian bawah halaman.*

## Apa itu analisis rantai?
Analisis rantai adalah praktik yang mencakup semua metode untuk melacak aliran Bitcoin di blockchain. Umumnya, analisis rantai bergantung pada pengamatan karakteristik dalam sampel transaksi sebelumnya. Kemudian melibatkan identifikasi karakteristik yang sama dalam transaksi yang ingin dianalisis dan menyimpulkan interpretasi yang masuk akal. Metode pemecahan masalah ini, berdasarkan pendekatan praktis untuk menemukan solusi yang cukup baik, adalah apa yang disebut heuristik.

Untuk menyederhanakan, analisis rantai dilakukan dalam dua langkah utama:
1. Identifikasi karakteristik yang diketahui;
2. Penyimpulan hipotesis.

Salah satu tujuan dari analisis rantai adalah untuk mengelompokkan berbagai aktivitas pada Bitcoin untuk menentukan keunikan pengguna yang melakukannya. Selanjutnya, akan mungkin untuk mencoba menghubungkan kumpulan aktivitas ini dengan identitas nyata.

Ingat pengantar saya. Saya menjelaskan mengapa model privasi Bitcoin awalnya bergantung pada pemisahan identitas pengguna dari transaksi mereka. Oleh karena itu, akan menggoda untuk berpikir bahwa analisis rantai tidak perlu, karena bahkan jika seseorang berhasil mengelompokkan aktivitas on-chain, mereka tidak dapat dikaitkan dengan identitas nyata. Secara teoritis, pernyataan ini akurat. Pasangan kunci kriptografi digunakan untuk menetapkan kondisi pada UTXO. Pada dasarnya, pasangan kunci ini tidak mengungkapkan informasi apa pun tentang identitas pemegangnya. Jadi, bahkan jika seseorang berhasil mengelompokkan aktivitas yang terkait dengan pasangan kunci yang berbeda, ini tidak memberi tahu kita apa pun tentang entitas di balik aktivitas tersebut.
Namun, realitas praktis jauh lebih kompleks. Ada berbagai perilaku yang berisiko menghubungkan identitas nyata dengan aktivitas on-chain. Dalam analisis, ini disebut sebagai titik masuk, dan ada banyak di antaranya. Yang paling umum, tentu saja, adalah KYC (Know Your Customer). Jika Anda menarik bitcoin Anda dari platform yang diatur ke salah satu alamat penerima pribadi Anda, maka beberapa orang dapat menghubungkan identitas Anda dengan alamat ini. Lebih luas lagi, titik masuk bisa berupa bentuk interaksi apa pun antara kehidupan nyata Anda dan transaksi Bitcoin. Misalnya, jika Anda mempublikasikan alamat penerima di jejaring sosial Anda, ini bisa menjadi titik masuk untuk analisis. Jika Anda melakukan pembayaran dalam bitcoin kepada tukang roti Anda, mereka dapat mengaitkan wajah Anda (yang merupakan bagian dari identitas Anda) dengan alamat Bitcoin. Titik masuk ini hampir tidak terhindarkan saat menggunakan Bitcoin. Meskipun seseorang mungkin berusaha untuk membatasi lingkupnya, mereka akan tetap ada. Itulah mengapa sangat penting untuk menggabungkan metode yang bertujuan untuk menjaga privasi Anda. Meskipun mempertahankan pemisahan yang dapat diterima antara identitas nyata Anda dan transaksi Anda adalah pendekatan yang terpuji, itu tetap tidak cukup. Memang, jika semua aktivitas on-chain Anda dapat digabungkan, maka bahkan titik masuk terkecil pun dapat mengompromikan lapisan privasi tunggal yang telah Anda bangun.

Oleh karena itu, juga perlu untuk berurusan dengan analisis rantai dalam penggunaan Bitcoin kita. Dengan melakukan itu, kita dapat meminimalkan agregasi aktivitas kita dan membatasi dampak titik masuk pada privasi kita. Secara tepat, untuk lebih baik melawan analisis rantai, pendekatan apa yang lebih baik selain mempelajari metode yang digunakan dalam analisis rantai? Jika Anda ingin tahu cara meningkatkan privasi Anda pada Bitcoin, Anda harus memahami metode-metode ini. Ini akan memungkinkan Anda untuk lebih memahami teknik seperti [Coinjoin](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef) atau [Payjoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f), dan untuk mengurangi kesalahan yang mungkin Anda buat.

Dalam hal ini, kita dapat menarik analogi dengan kriptografi dan kriptoanalisis. Seorang kriptografer yang baik adalah terlebih dahulu seorang kriptoanalisis yang baik. Untuk membayangkan algoritma enkripsi baru, seseorang harus tahu serangan apa yang akan dihadapinya, dan juga mempelajari mengapa algoritma sebelumnya rusak. Prinsip yang sama berlaku untuk privasi pada Bitcoin. Memahami metode analisis rantai adalah kunci untuk melindungi dari itu. Itulah mengapa saya menawarkan Anda artikel ini.

Penting untuk memahami bahwa analisis rantai bukanlah ilmu pasti. Ini bergantung pada heuristik yang berasal dari pengamatan sebelumnya atau interpretasi logis. Aturan-aturan ini memungkinkan hasil yang cukup dapat diandalkan, tetapi tidak pernah dengan presisi absolut. Dengan kata lain, analisis rantai selalu melibatkan dimensi probabilitas dalam kesimpulan yang ditarik. Kita dapat memperkirakan dengan lebih atau kurang kepastian bahwa dua alamat milik entitas yang sama, tetapi kepastian total selalu di luar jangkauan.

Seluruh tujuan analisis rantai terletak tepatnya dalam agregasi berbagai heuristik untuk meminimalkan risiko kesalahan. Ini, dalam suatu cara, adalah akumulasi bukti yang memungkinkan kita untuk mendekati realitas.

Heuristik terkenal ini dapat dikelompokkan ke dalam kategori yang berbeda yang akan kita rinci bersama:
- Pola transaksi (atau model transaksi);
- Heuristik internal terhadap transaksi;
- Heuristik eksternal terhadap transaksi.

Penting untuk dicatat bahwa dua heuristik pertama pada Bitcoin dirumuskan oleh Satoshi Nakamoto sendiri. Dia membahasnya di bagian 10 dari White Paper. Seperti yang akan kita lihat nanti, menarik untuk mengamati bahwa dua heuristik ini masih mempertahankan preeminensi dalam analisis rantai hari ini. Ini adalah:
- Heuristik Kepemilikan Input Bersama (CIOH);
- dan penggunaan alamat ulang.
Mari kita jelajahi bersama karakteristik yang dapat diamati dan interpretasi yang dapat ditarik untuk melakukan analisis.
## Pola Transaksi (atau model transaksi)
Pola transaksi hanyalah model transaksi tipikal yang dapat ditemukan di blockchain, yang interpretasinya kemungkinan sudah diketahui. Saat mempelajari pola, kita akan fokus pada satu transaksi yang akan kita analisis secara tingkat tinggi. Dengan kata lain, kita hanya akan melihat jumlah input dan output, tanpa menggali detail spesifiknya atau lingkungannya lebih lanjut. Dari model yang diamati, kita akan dapat menafsirkan sifat dari transaksi tersebut. Kemudian, kita akan mencari karakteristik tentang strukturnya dan menyimpulkan sebuah interpretasi.

### Pengiriman Sederhana (atau pembayaran sederhana)
Model ini ditandai dengan konsumsi satu atau lebih UTXO sebagai input dan produksi dua UTXO sebagai output.

![analisis](assets/en/2.webp)

Interpretasi dari model ini adalah bahwa kita berada dalam kehadiran transaksi pengiriman atau pembayaran. Pengguna telah mengkonsumsi UTXO mereka sendiri sebagai input untuk memenuhi output sebuah UTXO pembayaran dan sebuah UTXO kembalian (kembalian kembali ke pengguna yang sama). Oleh karena itu, kita tahu bahwa pengguna yang diamati kemungkinan tidak lagi memiliki salah satu dari dua UTXO di output (yang pembayaran), tetapi masih memiliki UTXO lainnya (yang kembalian).

Pada titik ini, mustahil bagi kita untuk menentukan output mana yang mewakili UTXO mana, karena itu bukan tujuan dari model ini. Kita akan dapat melakukannya dengan mengandalkan heuristik yang akan kita pelajari di bagian selanjutnya. Pada tahap ini, tujuan kita terbatas pada identifikasi sifat dari transaksi yang bersangkutan, yang dalam kasus ini, adalah pengiriman sederhana.

Sebagai contoh, berikut ini adalah transaksi Bitcoin yang mengadopsi pola pengiriman sederhana:
### Pembersihan ("sweep" dalam bahasa Inggris)
Model ini ditandai dengan konsumsi satu UTXO sebagai input dan produksi satu UTXO sebagai output.

![analisis](assets/en/3.webp)

Interpretasi dari model ini adalah bahwa kita berada dalam kehadiran transfer diri. Pengguna telah mentransfer bitcoin mereka kepada diri mereka sendiri, ke alamat lain yang mereka miliki. Memang, karena tidak ada perubahan dalam transaksi, sangat tidak mungkin bahwa kita berurusan dengan pembayaran. Kemudian kita tahu bahwa pengguna yang diamati kemungkinan masih memiliki UTXO ini.

Sebagai contoh, berikut ini adalah transaksi Bitcoin yang mengadopsi pola pembersihan:
[35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d](https://mempool.space/tx/35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d)

Namun, jenis pola ini juga dapat mengungkapkan transfer diri ke akun bursa (platform pertukaran cryptocurrency). Akan menjadi studi alamat yang diketahui dan konteks transaksi yang akan memungkinkan kita untuk mengetahui apakah itu pembersihan ke dompet penyimpanan sendiri atau penarikan ke platform.

### Konsolidasi
Model ini ditandai dengan konsumsi beberapa UTXO sebagai input dan produksi satu UTXO sebagai output.

![analisis](assets/en/4.webp)
Interpretasi dari model ini adalah bahwa kita berada dalam keadaan konsolidasi. Ini adalah praktik umum di antara pengguna Bitcoin, bertujuan untuk menggabungkan beberapa UTXO dalam antisipasi kemungkinan peningkatan biaya transaksi. Dengan melakukan operasi ini selama periode ketika biaya rendah, dimungkinkan untuk menghemat biaya di masa depan.
Kita dapat menyimpulkan bahwa pengguna di balik transaksi ini kemungkinan besar memiliki semua UTXO di input dan masih memiliki UTXO di output. Oleh karena itu, ini pasti merupakan transfer diri.

Sama seperti sapuan, jenis pola ini juga dapat mengungkapkan transfer diri ke akun bursa. Ini akan menjadi studi alamat yang diketahui dan konteks transaksi yang akan memungkinkan kita untuk mengetahui apakah ini konsolidasi ke dompet penyimpanan sendiri atau penarikan ke platform.

Sebagai contoh, berikut ini adalah transaksi Bitcoin yang mengadopsi pola konsolidasi:
[77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94](https://mempool.space/tx/77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94)
### Model Pengeluaran Batch
Model ini ditandai dengan konsumsi beberapa UTXO sebagai input (seringkali hanya satu) dan produksi banyak UTXO sebagai output.

![analisis](assets/en/5.webp)

Interpretasi dari model ini adalah bahwa kita berada dalam keadaan pengeluaran batch. Ini adalah praktik yang kemungkinan mengungkapkan aktivitas ekonomi yang signifikan, seperti bursa, misalnya. Pengeluaran batch memungkinkan entitas ini untuk menghemat biaya dengan menggabungkan pengeluaran mereka ke dalam satu transaksi.

Kita dapat menyimpulkan bahwa input UTXO berasal dari perusahaan dengan aktivitas ekonomi yang signifikan dan bahwa output UTXO akan tersebar. Beberapa akan menjadi milik klien perusahaan. Lainnya mungkin menuju ke perusahaan mitra. Akhirnya, pasti akan ada perubahan yang kembali ke perusahaan penerbit.

Sebagai contoh, berikut ini adalah transaksi Bitcoin yang mengadopsi pola pengeluaran batch:
[8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43](https://mempool.space/tx/8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43)

### Transaksi Spesifik Protokol
Di antara pola transaksi, kita juga dapat mengidentifikasi model yang mengungkapkan penggunaan protokol spesifik. Misalnya, Whirlpool coinjoins akan memiliki struktur yang mudah diidentifikasi yang memungkinkan mereka untuk dibedakan dari transaksi klasik lainnya.

![analisis](assets/en/6.webp)

Analisis dari pola ini menyarankan bahwa kita kemungkinan berada dalam kehadiran transaksi kolaboratif. Juga dimungkinkan untuk mengamati coinjoin. Jika hipotesis terakhir ini terbukti akurat, maka jumlah output dapat memberi kita perkiraan kasar jumlah peserta.

Sebagai contoh, berikut ini adalah transaksi Bitcoin yang mengadopsi pola dari tipe transaksi kolaboratif coinjoin:
[00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea](https://mempool.space/tx/00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea)
Ada banyak protokol lain yang memiliki struktur khusus mereka sendiri. Dengan demikian, kita dapat membedakan transaksi dari tipe Wabisabi atau transaksi Stamps, sebagai contoh.
## Heuristik Transaksi Internal
Heuristik internal adalah karakteristik spesifik yang diidentifikasi dalam sebuah transaksi itu sendiri, tanpa perlu memeriksa lingkungannya, yang memungkinkan kita untuk membuat deduksi. Tidak seperti pola yang berfokus pada struktur keseluruhan dari transaksi, heuristik internal didasarkan pada kumpulan data yang dapat diekstrak. Ini meliputi:
- Jumlah UTXO yang berbeda baik yang masuk dan yang keluar;
- Semua yang terkait dengan skrip: alamat penerima, versioning, locktimes...

Secara umum, tipe heuristik ini memungkinkan kita untuk mengidentifikasi perubahan dalam sebuah transaksi spesifik. Dengan melakukan ini, kita kemudian dapat melanjutkan untuk melacak entitas melalui beberapa transaksi yang berbeda.

Sekali lagi, saya ingatkan bahwa heuristik ini tidak sepenuhnya akurat. Diambil secara individu, mereka hanya memungkinkan kita untuk mengidentifikasi skenario yang masuk akal. Adalah akumulasi dari beberapa heuristik yang berkontribusi untuk mengurangi ketidakpastian, tanpa pernah sepenuhnya menghilangkannya.

### Kesamaan Internal
Heuristik ini melibatkan studi tentang kesamaan antara input dan output dari transaksi yang sama. Jika karakteristik yang sama diamati pada input dan hanya pada salah satu output dari transaksi, maka kemungkinan output tersebut merupakan perubahan.

Karakteristik yang paling jelas adalah penggunaan kembali alamat penerima dalam transaksi yang sama.

![analisis](assets/en/7.webp)

Heuristik ini meninggalkan sedikit ruang untuk keraguan. Kecuali kunci privat mereka telah dikompromikan, alamat penerima yang sama tidak dapat dihindari mengungkapkan aktivitas pengguna tunggal. Interpretasi yang mengikuti adalah bahwa perubahan dari transaksi adalah output dengan alamat yang sama seperti input. Ini memungkinkan kita untuk melanjutkan pelacakan individu dari perubahan ini.

Sebagai contoh, berikut ini adalah transaksi di mana heuristik ini kemungkinan dapat diterapkan:
[54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0](https://mempool.space/tx/54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0)

Kesamaan antara input dan output tidak berhenti pada penggunaan kembali alamat. Kesamaan dalam penggunaan skrip juga dapat memungkinkan penerapan heuristik. Sebagai contoh, terkadang versi yang sama antara input dan salah satu output dari transaksi dapat diamati.

![analisis](assets/en/8.webp)
Dalam diagram ini, kita dapat melihat bahwa input nomor 0 membuka skrip P2WPKH (SegWit V0 yang dimulai dengan "bc1q"). Output nomor 0 menggunakan jenis skrip yang sama. Namun, output nomor 1 menggunakan skrip P2TR (SegWit V1 yang dimulai dengan "bc1p"). Interpretasi dari karakteristik ini adalah bahwa kemungkinan alamat dengan versioning yang sama sebagai input adalah alamat perubahan. Oleh karena itu, masih akan dimiliki oleh pengguna yang sama.
Berikut ini adalah transaksi di mana heuristik ini kemungkinan dapat diterapkan:
[db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578](https://mempool.space/tx/db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578)
Dalam transaksi ini, kita dapat melihat bahwa input nomor 0 dan output nomor 1 menggunakan skrip P2WPKH (SegWit V0), sementara output nomor 0 menggunakan tipe skrip yang berbeda, P2PKH (Legacy).
### Pembayaran Nomor Bulat
Heuristik internal lain yang dapat membantu kita mengidentifikasi perubahan adalah pembayaran nomor bulat. Umumnya, ketika dihadapkan pada pola pembayaran sederhana (1 input dan 2 output), jika salah satu output menghabiskan jumlah bulat, maka itu mewakili pembayaran.

![analisis](assets/en/9.webp)

Dengan proses eliminasi, jika satu output mewakili pembayaran, output lainnya mewakili kembalian. Oleh karena itu, kita dapat menafsirkan bahwa kemungkinan pengguna di input masih memiliki output yang diidentifikasi sebagai kembalian.

Perlu dicatat bahwa heuristik ini tidak selalu dapat diterapkan, karena sebagian besar pembayaran masih dilakukan dalam unit mata uang fiat. Memang, ketika seorang pedagang di Prancis menerima bitcoin, umumnya, mereka tidak menampilkan harga stabil dalam sats. Mereka lebih memilih untuk melakukan konversi antara harga dalam euro dan jumlah bitcoin yang harus dibayar. Oleh karena itu, seharusnya tidak ada jumlah bulat dalam output transaksi. Namun, seorang analis dapat mencoba melakukan konversi ini dengan mempertimbangkan nilai tukar yang berlaku saat transaksi disiarkan di jaringan.

Jika suatu hari, bitcoin menjadi unit akun yang disukai dalam pertukaran kita, heuristik ini bisa menjadi lebih berguna untuk analisis.

Sebagai contoh, berikut adalah transaksi di mana heuristik ini kemungkinan dapat diterapkan:
### Pengeluaran Besar

Ketika celah yang cukup besar terlihat antara dua output transaksi dalam model pembayaran sederhana, dapat diperkirakan bahwa output yang lebih besar kemungkinan adalah kembalian.

![analisis](assets/en/10.webp)

Heuristik output terbesar ini mungkin yang paling tidak tepat dari semuanya. Jika diidentifikasi sendirian, itu cukup lemah. Namun, karakteristik ini dapat dikombinasikan dengan heuristik lain untuk mengurangi ketidakpastian interpretasi kita.

Sebagai contoh, jika kita memeriksa transaksi yang menampilkan output dengan jumlah bulat dan output lain dengan jumlah yang lebih besar, penerapan bersama heuristik pembayaran bulat dan yang berkaitan dengan output terbesar memungkinkan kita untuk mengurangi tingkat ketidakpastian kita.

Sebagai contoh, berikut adalah transaksi di mana heuristik ini kemungkinan dapat diterapkan:
[b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf](https://mempool.space/tx/b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf)

## Heuristik Eksternal terhadap Transaksi
Studi tentang heuristik eksternal adalah analisis kesamaan, pola, dan karakteristik dari elemen-elemen tertentu yang tidak melekat pada transaksi itu sendiri. Dengan kata lain, jika sebelumnya kita membatasi diri pada pemanfaatan elemen intrinsik transaksi dengan heuristik internal, sekarang kita memperluas bidang analisis kita ke lingkungan transaksi berkat heuristik eksternal.

### Penggunaan Ulang Alamat
Ini adalah salah satu heuristik yang paling dikenal di kalangan pengguna Bitcoin. Penggunaan ulang alamat memungkinkan untuk menetapkan hubungan antara transaksi yang berbeda dan UTXO yang berbeda. Hal ini diamati ketika alamat penerima Bitcoin digunakan beberapa kali.

Interpretasi dari penggunaan ulang alamat adalah bahwa semua UTXO yang terkunci pada alamat ini milik (atau telah dimiliki) oleh entitas yang sama. Heuristik ini meninggalkan sedikit ruang untuk ketidakpastian. Ketika diidentifikasi, interpretasi yang mengikuti memiliki peluang besar untuk sesuai dengan kenyataan.
Seperti yang dijelaskan dalam pengantar, heuristik ini ditemukan oleh Satoshi Nakamoto sendiri. Dalam White Paper, ia secara khusus menyebutkan solusi untuk mencegah pengguna memproduksinya, yaitu dengan menggunakan alamat baru untuk setiap transaksi baru: "*Sebagai firewall tambahan, sepasang kunci baru bisa digunakan untuk setiap transaksi agar mereka tidak terhubung ke pemilik yang sama.*"
Sebagai contoh, berikut ini adalah alamat yang digunakan kembali dalam beberapa transaksi:
[bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0](https://mempool.space/address/bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0)

### Kesamaan Skrip dan Sidik Jari Dompet
Lebih dari sekedar penggunaan ulang alamat, ada banyak heuristik lain yang dapat menghubungkan tindakan ke dompet yang sama atau ke kluster alamat.

Pertama-tama, seorang analis dapat menggunakan kesamaan dalam penggunaan skrip. Sebagai contoh, skrip minoritas tertentu seperti multisig dapat lebih mudah dikenali daripada skrip SegWit V0. Semakin besar kelompok tempat kita bersembunyi, semakin sulit kita untuk dikenali. Inilah mengapa, pada protokol Coinjoin Whirlpool, semua peserta menggunakan jenis skrip yang sama persis.

Lebih luas lagi, seorang analis juga dapat fokus pada sidik jari karakteristik dari sebuah dompet. Ini adalah proses spesifik untuk penggunaan yang mungkin dicari untuk diidentifikasi guna memanfaatkannya sebagai heuristik pelacakan. Dengan kata lain, jika seseorang mengamati akumulasi karakteristik internal yang sama pada transaksi yang diatributkan kepada entitas yang dilacak, seseorang dapat mencoba mengidentifikasi karakteristik yang sama pada transaksi lain.

Sebagai contoh, dapat diidentifikasi bahwa pengguna yang dilacak secara sistematis mengirimkan perubahan mereka ke alamat P2TR* (bc1p…). Jika proses ini berulang, itu dapat digunakan sebagai heuristik untuk kelanjutan analisis kita. Sidik jari lain juga dapat digunakan, seperti urutan UTXO, penempatan perubahan di output, sinyal RBF (Replace-by-Fee), atau bahkan, nomor versi dan locktime.
Seperti yang [@LaurentMT](https://twitter.com/LaurentMT) sebutkan dalam [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) (podcast berbahasa Prancis), utilitas sidik jari dompet dalam analisis rantai semakin meningkat seiring waktu. Memang, semakin banyaknya jenis skrip dan penyebaran fitur baru secara bertahap oleh perangkat lunak dompet menonjolkan perbedaan. Bahkan terjadi bahwa seseorang dapat dengan akurat mengidentifikasi perangkat lunak yang digunakan oleh entitas yang dilacak. Oleh karena itu, penting untuk memahami bahwa studi sidik jari dompet sangat relevan untuk transaksi terbaru, lebih dari pada transaksi yang dimulai pada awal tahun 2010-an.
Untuk merangkum, sidik jari dapat berupa praktik spesifik, dilakukan secara otomatis oleh dompet atau secara manual oleh pengguna, yang dapat ditemukan pada transaksi lain untuk membantu dalam analisis kita.

### CIOH
CIOH, singkatan dari "Common Input Ownership Heuristic," yang dapat diterjemahkan sebagai "heuristik kepemilikan input bersama" atau "heuristik pengeluaran bersama," adalah heuristik yang menyatakan bahwa ketika sebuah transaksi memiliki beberapa input, input-input tersebut kemungkinan besar berasal dari satu entitas. Akibatnya, kepemilikannya bersama.
Untuk menerapkan CIOH, seseorang pertama-tama mengamati sebuah transaksi yang memiliki banyak input. Ini bisa jadi dua input, serta tiga puluh input. Setelah karakteristik ini terlihat, seseorang memeriksa apakah transaksi tersebut tidak masuk ke dalam pola yang sudah dikenal. Misalnya, jika ada 5 input dengan jumlah yang kurang lebih sama dan 5 output dengan jumlah yang persis sama, kita tahu bahwa itu adalah struktur dari Coinjoin Whirlpool. Oleh karena itu, CIOH tidak dapat diterapkan.
Namun, jika transaksi tersebut tidak masuk ke dalam pola transaksi kolaboratif yang dikenal, maka dapat diinterpretasikan bahwa semua input kemungkinan besar berasal dari entitas yang sama. Ini bisa sangat berguna untuk memperluas kluster yang sudah dikenal atau untuk melanjutkan pelacakan.

![analisis](assets/en/11.webp)

CIOH ditemukan oleh Satoshi Nakamoto. Dia membahasnya dalam bagian 10 dari White Paper: "*[...] tautan itu tidak terelakkan dengan transaksi multi-input, yang secara pasti mengungkapkan bahwa input mereka dimiliki oleh pemilik yang sama. Risikonya adalah jika pemilik kunci terungkap, tautan dapat mengungkapkan transaksi lain yang dimiliki oleh pemilik yang sama.*"
Sangat menarik untuk dicatat bahwa Satoshi Nakamoto, bahkan sebelum peluncuran resmi Bitcoin, telah mengidentifikasi dua kerentanan privasi utama bagi pengguna, yaitu CIOH dan penggunaan ulang alamat. Wawasan seperti itu cukup luar biasa, karena kedua heuristik ini tetap, bahkan hari ini, yang paling berguna dalam analisis rantai.

### Data Off-chain
Tentu saja, analisis rantai tidak terbatas pada data on-chain. Data dari analisis sebelumnya atau yang dapat diakses di Internet juga dapat digunakan untuk menyempurnakan analisis.

Misalnya, jika diamati bahwa transaksi yang dilacak secara sistematis disiarkan dari node Bitcoin yang sama dan alamat IP-nya dapat diidentifikasi, mungkin dimungkinkan untuk menemukan transaksi lain dari entitas yang sama.

Analis juga memiliki opsi untuk mengandalkan analisis yang sebelumnya dibuat open-source, atau pada analisis sebelumnya mereka sendiri. Mungkin seseorang menemukan output yang mengarah ke kluster alamat yang telah diidentifikasi sebelumnya. Terkadang, juga dimungkinkan untuk mengandalkan output yang mengarah ke bursa, alamat platform ini umumnya dikenal.

Demikian pula, seseorang dapat melakukan analisis dengan eliminasi. Misalnya, jika selama analisis transaksi dengan dua output, salah satunya terkait dengan kluster alamat yang dikenal tetapi berbeda dari entitas yang dilacak, maka dapat diinterpretasikan bahwa output lainnya kemungkinan besar mewakili kembalian.

Analisis rantai juga mencakup bagian dari OSINT (Open Source Intelligence) yang sedikit lebih umum dengan pencarian internet. Inilah sebabnya mengapa disarankan agar tidak memposting alamat penerima langsung di media sosial atau di situs web, baik di bawah pseudonim atau tidak.

### Model Temporal
Seseorang mungkin tidak langsung memikirkannya, tetapi beberapa perilaku manusia dapat dikenali on-chain. Yang paling berguna dalam sebuah studi adalah pola tidur Anda! Ya, ketika Anda sedang tidur, Anda kemungkinan besar tidak melakukan transaksi Bitcoin. Karena Anda umumnya tidur pada jam-jam yang kurang lebih sama, analisis temporal umum digunakan dalam analisis on-chain. Ini hanya melibatkan pencatatan waktu di mana transaksi entitas tertentu disiarkan ke jaringan Bitcoin. Menganalisis pola temporal ini memungkinkan kita untuk menyimpulkan banyak informasi.
Pertama dan terutama, analisis temporal terkadang dapat mengidentifikasi sifat dari entitas yang dilacak. Jika seseorang mengamati bahwa transaksi disiarkan secara konsisten selama 24 jam, ini dapat menunjukkan aktivitas ekonomi yang kuat. Entitas di balik transaksi ini kemungkinan adalah bisnis, berpotensi internasional, dan mungkin dengan prosedur otomatis secara internal.
Misalnya, saya telah mengenali pola ini beberapa minggu yang lalu saat menganalisis sebuah transaksi yang secara keliru mengalokasikan 19 bitcoin sebagai biaya. Analisis temporal sederhana telah memungkinkan saya untuk menghipotesiskan bahwa kita sedang berurusan dengan layanan otomatis, dan oleh karena itu kemungkinan besar sebuah entitas besar seperti bursa: https://twitter.com/Loic_Pandul/status/1701127409712452072
Memang, beberapa hari kemudian, ditemukan bahwa dana tersebut milik PayPal, melalui bursa Paxos.

Sebaliknya, jika seseorang melihat bahwa pola temporal lebih tersebar selama 16 jam tertentu, maka dapat diperkirakan bahwa kita sedang berurusan dengan pengguna individu, atau mungkin sebuah bisnis lokal tergantung pada volume yang ditukar.

Di luar sifat entitas yang diamati, pola temporal juga dapat memberi kita lokasi pengguna yang diperkirakan. Dengan demikian, kita dapat mengorelasikan transaksi lain, dan menggunakan timestamp dari transaksi tersebut sebagai heuristik tambahan yang dapat ditambahkan ke dalam analisis kita.

Misalnya, pada alamat yang digunakan berulang kali yang sebelumnya saya sebutkan, seseorang dapat mengamati bahwa transaksi, baik masuk atau keluar, terkonsentrasi selama interval 13 jam.
![analisis](assets/notext/12.webp)
*Kredit: OXT*

Interval ini kemungkinan besar sesuai dengan Eropa, Afrika, atau Timur Tengah. Oleh karena itu, dapat diinterpretasikan bahwa pengguna di balik transaksi-transaksi ini tinggal di sana.

Dalam register yang berbeda, ini juga merupakan analisis temporal dari jenis ini yang memungkinkan hipotesis bahwa Satoshi Nakamoto tidak beroperasi dari Jepang, tetapi memang dari Amerika Serikat: [https://medium.com/@insearchofsatoshi/the-time-zones-of-satoshi-nakamoto-aa40f035178f](https://medium.com/@insearchofsatoshi/the-time-zones-of-satoshi-nakamoto-aa40f035178f)

### Analisis Volume
Heuristik eksternal lain yang dapat digunakan adalah analisis volume perdagangan. Berdasarkan jumlah yang ada dalam setiap transaksi yang diatributkan kepada sebuah entitas, informasi ini dapat digunakan sebagai heuristik tambahan untuk sisa analisis.
Heuristik ini jelas cukup lemah, tetapi dapat membantu mengurangi ketidakpastian ketika ditambahkan ke heuristik lain.

## Bagaimana cara melindungi diri dari analisis rantai?
Sebagai pengguna Bitcoin, Anda memiliki hak untuk melindungi privasi Anda. Ini berasal dari hak alami Anda untuk memiliki dan mengatur diri Anda sendiri, yang melekat pada setiap individu, terlepas dari batasan legislatif apa pun.

Hak alami ini untuk melindungi privasi seseorang juga diubah menjadi hak klaim, yang diabadikan dalam Pasal 12 Deklarasi Universal Hak Asasi Manusia, yang menyatakan bahwa "*Tidak seorang pun boleh dikenai gangguan sewenang-wenang terhadap privasinya, keluarga, rumah atau korespondensinya, atau serangan terhadap kehormatan dan reputasinya. Setiap orang memiliki hak untuk dilindungi hukum dari gangguan atau serangan semacam itu.*".

Namun, bisnis inti dari perusahaan yang mengkhususkan diri dalam analisis rantai terdiri dari mengganggu ranah pribadi Anda, sehingga mengkompromikan kerahasiaan korespondensi Anda. Sementara seseorang mungkin berharap bahwa, sesuai dengan hak klaim yang disebutkan di atas, negara-negara akan dengan gigih mempertahankan privasi kita, tidak hanya mereka mengabaikan untuk melakukannya, tetapi mereka juga secara substansial mendanai pembiayaan perusahaan analisis ini. Juga akan sia-sia untuk berharap dukungan dari asosiasi sektor, yang tampaknya bersedia membuat semua konsesi di hadapan legislator.

Faktanya, hak klaim ini terhadap privasi di Bitcoin tidak ada. Oleh karena itu, terserah Anda, pengguna, untuk menegaskan hak alami Anda dan melindungi kerahasiaan korespondensi Anda. Ini melibatkan mengadopsi berbagai teknik dan praktik penggunaan, yang akan memungkinkan Anda untuk mencegah atau menipu heuristik yang digunakan untuk analisis rantai.

### Menghindari Terjebak dalam Heuristik
Pertama-tama, sebelum mempertimbangkan metode yang lebih radikal, disarankan untuk membatasi paparan kita terhadap heuristik yang digunakan untuk analisis rantai sebanyak mungkin. Seperti yang disebutkan sebelumnya, dua heuristik paling kuat adalah penggunaan ulang alamat dan COINJOIN.
Prinsip dasar untuk memastikan privasi Anda di Bitcoin terletak pada penggunaan alamat baru yang bersih untuk setiap transaksi masuk ke dompet Anda. Penggunaan ulang alamat benar-benar merupakan ancaman utama terhadap kerahasiaan di Bitcoin.
Untuk pengguna individu, menghasilkan alamat baru untuk setiap pembayaran masuk sangatlah sederhana. Dompet modern melakukan ini secara otomatis segera setelah Anda mengklik "Terima". Jadi, jika Anda memberikan sedikit pun pentingnya pada privasi transaksi Anda, menggunakan alamat baru merupakan hal minimal. Jika Anda memerlukan titik kontak statis di internet, alih-alih memasang alamat penerima, Anda dapat menggunakan solusi [seperti PayNym yang mengimplementasikan BIP47](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093).
Selanjutnya, jika Anda ingin bertindak melawan analisis rantai, hindari penggabungan UTXO pada input transaksi. Minimal, jika Anda benar-benar perlu menggabungkan, pilihlah UTXO yang memiliki sumber yang sama. Rekomendasi ini mengimplikasikan memiliki manajemen UTXO yang baik. Saat membeli bitcoin Anda, pilih transfer yang melibatkan jumlah besar untuk memaksimalkan jumlah pembayaran yang dapat Anda lakukan tanpa harus menggabungkan. Saya juga menyarankan Anda untuk memberi label UTXO Anda di perangkat lunak Anda untuk mengidentifikasi asalnya dan menghindari penggabungan dari sumber yang berbeda.

Lebih luas lagi, untuk semua heuristik lainnya, Anda perlu mengetahuinya untuk mencoba tidak terjebak di dalamnya:
- Jangan gunakan skrip minoritas. Lebih baik menggunakan SegWit V0 atau mungkin SegWit V1;
- Jangan melakukan pembayaran dengan angka bulat. Misalnya, jika Anda perlu mengirim 100k sats ke teman, kirimkan mereka 114,486 sats. Mereka akan membelikan Anda minuman sebagai balasannya;
- Cobalah untuk tidak selalu memiliki kembalian yang jauh lebih besar dari output pembayaran;
- Jangan memposting alamat penerima Anda di media sosial;
- Gunakan node Anda sendiri di bawah Tor untuk menyiarkan transaksi Anda;
- Cobalah untuk tidak selalu menyiarkan transaksi Bitcoin Anda pada waktu yang sama…

### Menggunakan alat privasi
Anda juga dapat beralih ke metode yang membuat penggunaan Bitcoin Anda ambigu untuk mencegah atau menipu analisis rantai.

Teknik paling populer pasti adalah Coinjoin, struktur transaksi kolaboratif yang menggerakkan beberapa UTXO dengan jumlah yang sama. Tujuan di sini adalah untuk memutuskan tautan deterministik, sehingga mencegah analisis dari masa sekarang ke masa lalu dan dari masa lalu ke masa sekarang. Coinjoin memungkinkan plausible deniability dengan menyembunyikan koin Anda dalam sekelompok besar koin yang tidak dapat dibedakan. Jika Anda ingin mempelajari lebih lanjut tentang Coinjoin, baik secara teknis maupun praktis, saya sarankan Anda membaca artikel dan tutorial lainnya:
- [COINJOIN - SAMOURAI WALLET](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef);
- [COINJOIN - SPARROW WALLET](https://planb.network/tutorials/privacy/on-chain/coinjoin-sparrow-wallet-84def86d-faf5-4589-807a-83be60720c8b);
- [WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375).
![analisis](assets/en/13.webp)

CoinJoin adalah alat yang sangat baik untuk menciptakan plausible deniability untuk koin, tetapi tidak dioptimalkan untuk semua kebutuhan privasi pengguna. Secara spesifik, CoinJoin tidak dirancang untuk menjadi alat pembayaran. Ini sangat kaku tentang jumlah yang ditukarkan untuk menyempurnakan produksi plausible deniability. Karena seseorang tidak dapat bebas memilih jumlah output transaksi, CoinJoin tidak dapat digunakan untuk melakukan pembayaran dalam bitcoin.
Misalnya, bayangkan saya ingin membayar baguette saya dengan bitcoin sambil mengoptimalkan privasi saya. Mengingat ketidakmungkinan untuk memilih jumlah UTXO yang dihasilkan dari CoinJoin, saya akan menemukan diri saya tidak dapat menyesuaikan jumlah pengeluaran saya dengan harga yang ditetapkan oleh tukang roti. Oleh karena itu, CoinJoin terbukti tidak memadai untuk transaksi pembayaran.

Alat lain telah dirancang untuk memenuhi kebutuhan privasi dalam kasus penggunaan yang lebih spesifik. Sebagai contoh, kita memiliki [PayJoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f), semacam mini-CoinJoin, yang melibatkan hanya dua peserta dan berdasarkan struktur yang memungkinkan pembayaran.

Keunikan PayJoin terletak pada kemampuannya untuk menghasilkan transaksi yang terlihat biasa, sementara sebenarnya itu adalah mini-CoinJoin antara dua pengguna. Dalam struktur ini, penerima transaksi berpartisipasi di antara input bersama dengan pengirim sebenarnya. Dengan demikian, penerima memasukkan pembayaran kepada diri mereka sendiri dalam transaksi yang memfasilitasi pembayaran sebenarnya.

Sebagai contoh, jika Anda membeli baguette dari tukang roti Anda seharga 6.000 sats dari UTXO 10.000 sats, dan Anda ingin melakukan PayJoin, tukang roti Anda akan menambahkan UTXO 15.000 sats yang milik mereka sebagai input ke transaksi asli Anda, yang akan mereka pulihkan sepenuhnya sebagai output, untuk menipu heuristik:

![analisis](assets/en/14.webp)

Biaya transaksi diabaikan untuk menyederhanakan pemahaman skema.

Tujuan PayJoin adalah dua kali lipat. Pertama, itu bertujuan untuk menipu pengamat eksternal dengan menciptakan umpan melalui COH. Memang, ketika seorang analis mengamati transaksi ini, mereka akan berpikir mereka dapat menerapkan COH, dan dengan demikian menganggap kepemilikan bersama dari input yang berbeda. Pada kenyataannya, asumsi ini salah, karena satu input milik pengirim, sementara yang lain dimiliki oleh penerima. Oleh karena itu, PayJoin merusak analisis rantai dengan membawa analis ke jalan yang salah.
Tujuan kedua PayJoin adalah untuk menipu analis tentang jumlah sebenarnya dari transaksi, berkat struktur outputnya yang spesifik. Dengan demikian, PayJoin berada dalam bidang steganografi. Ini memungkinkan jumlah sebenarnya dari transaksi untuk disembunyikan dalam transaksi penipuan.

Memang, jika kita mengunjungi kembali contoh kita menggunakan PayJoin untuk membeli baguette, seorang pengamat eksternal mungkin berpikir bahwa kita berurusan dengan pembayaran 4.000 sats atau 21.000 sats. Pada kenyataannya, pembayaran untuk baguette adalah 6.000 sats: 21.000 - 15.000 = 6.000. Nilai sebenarnya dari pembayaran oleh karena itu tersembunyi dalam pembayaran palsu yang bertindak sebagai umpan untuk analisis rantai.

Di luar PayJoin dan CoinJoin, ada banyak struktur transaksi Bitcoin lainnya yang baik memblokir analisis rantai atau menipunya. Di antara ini, saya bisa menyebutkan transaksi [Stonewall](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4) dan [StonewallX2](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b), yang memungkinkan baik untuk membuat mini Coinjoin yang fleksibel atau untuk meniru mini Coinjoin yang fleksibel. Ada juga transaksi [Ricochet](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589) yang mensimulasikan perubahan kepemilikan bitcoin dengan membuat banyak transfer palsu kepada diri sendiri.

Semua alat ini tersedia di Samourai Wallet di ponsel, dan Sparrow Wallet di PC. Jika Anda ingin mempelajari lebih lanjut tentang struktur transaksi spesifik ini, saya menyarankan Anda untuk menemukan tutorial saya:
- [PAYJOIN](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f);
- [PAYJOIN - SAMOURAI WALLET](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab);
- [PAYJOIN - SPARROW WALLET](https://planb.network/tutorials/privacy/on-chain/payjoin-sparrow-wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62);
- [STONEWALL](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4);
- [STONEWALL X2](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b);
- [RICOCHET](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).

## Kesimpulan
Analisis rantai adalah praktik yang melibatkan upaya untuk melacak aliran bitcoin dalam rantai. Untuk melakukan ini, analis mencari pola dan karakteristik untuk menarik hipotesis dan interpretasi yang lebih atau kurang masuk akal.

Akurasi dari heuristik ini bervariasi: beberapa menyediakan tingkat kepastian yang lebih tinggi daripada yang lain, tetapi tidak ada yang dapat mengklaim sebagai tidak terbantahkan. Namun, akumulasi beberapa heuristik yang konvergen dapat mengurangi keraguan ini, meskipun tetap tidak mungkin untuk sepenuhnya menghilangkannya.
Kita dapat mengategorikan metode-metode ini ke dalam tiga kategori utama yang berbeda:
- Pola, berfokus pada struktur keseluruhan dari setiap transaksi;
- Heuristik internal, yang memungkinkan pemeriksaan menyeluruh dari semua detail transaksi, tanpa meluas ke konteksnya;
- Heuristik eksternal, yang mencakup analisis transaksi dalam lingkungannya, serta data eksternal apa pun yang dapat memberikan wawasan.

Sebagai pengguna Bitcoin, sangat penting untuk menguasai prinsip-prinsip dasar analisis rantai untuk secara efektif melawannya dan dengan demikian melindungi privasi Anda.

## Mini-Glosarium Teknis:
**P2PKH:** akronim untuk Pay to Public Key Hash. Ini adalah model skrip standar yang digunakan untuk menetapkan kondisi pengeluaran pada sebuah UTXO. Ini memungkinkan penguncian bitcoin pada hash dari kunci publik, yaitu, pada alamat penerima. Skrip ini dikaitkan dengan standar Legacy dan diperkenalkan dalam versi pertama Bitcoin oleh Satoshi Nakamoto. Tidak seperti P2PK, di mana kunci publik secara eksplisit termasuk dalam skrip, P2PKH menggunakan jejak kriptografis dari kunci publik, dengan beberapa metadata, juga disebut "alamat penerima". Skrip ini mencakup hash RIPEMD160 dari SHA256 dari kunci publik dan menetapkan bahwa, untuk mengakses dana, penerima harus menyediakan kunci publik yang cocok dengan hash ini, serta tanda tangan digital yang valid yang dihasilkan dari kunci privat yang terkait. Alamat P2PKH dikodekan menggunakan format Base58Check, yang memberikan resistensi terhadap kesalahan ketik melalui penggunaan checksum. Alamat-alamat ini selalu dimulai dengan angka 1.
**P2TR:** singkatan dari Pay to Taproot ("bayar ke akar"). Ini adalah model skrip standar yang digunakan untuk menetapkan kondisi pengeluaran pada sebuah UTXO. P2TR diperkenalkan dengan implementasi Taproot pada November 2021. Ini menggunakan protokol Schnorr untuk mengagregasi kunci kriptografi, serta pohon Merkle untuk skrip alternatif, yang dikenal sebagai MAST (Merkelized Alternative Script Tree). Tidak seperti transaksi tradisional di mana kondisi pengeluaran terpapar secara publik (kadang-kadang saat penerimaan, kadang-kadang saat pengeluaran), P2TR memungkinkan penyembunyian skrip kompleks di balik satu kunci publik yang tampak. Secara teknis, skrip P2TR mengunci bitcoin pada sebuah kunci publik Schnorr unik, yang ditandai sebagai K. Namun, kunci K ini sebenarnya adalah agregat dari kunci publik P dan kunci publik M, yang terakhir dihitung dari akar Merkle dari daftar ScriptPubKeys. Agregasi kunci dilakukan menggunakan protokol tanda tangan Schnorr. Bitcoin yang dikunci dengan skrip P2TR dapat dihabiskan dengan dua cara yang berbeda: baik dengan mempublikasikan tanda tangan untuk kunci publik P, atau dengan memenuhi salah satu skrip yang terkandung dalam pohon Merkle. Opsi pertama disebut "jalur kunci" dan yang kedua "jalur skrip." Dengan demikian, P2TR memungkinkan pengguna untuk mengirim bitcoin baik ke kunci publik atau ke beberapa skrip pilihan mereka. Keuntungan lain dari skrip ini adalah, meskipun ada beberapa cara untuk menghabiskan output P2TR, hanya yang digunakan saja yang perlu diungkapkan saat pengeluaran, memungkinkan alternatif yang tidak digunakan untuk tetap pribadi. Sebagai contoh, berkat agregasi kunci Schnorr, kunci publik P itu sendiri dapat menjadi kunci agregat, berpotensi mewakili multisig. P2TR adalah output SegWit versi 1, yang berarti bahwa tanda tangan untuk input P2TR disimpan dalam saksi dari sebuah transaksi, dan bukan dalam ScriptSig. Alamat P2TR menggunakan pengkodean Bech32m dan dimulai dengan bc1p.

**P2WPKH:** Singkatan dari Pay to Witness Public Key Hash. Ini adalah model skrip standar yang digunakan untuk menetapkan kondisi pengeluaran pada sebuah UTXO. P2WPKH diperkenalkan dengan implementasi SegWit pada Agustus 2017. Skrip ini mirip dengan P2PKH (Pay to Public Key Hash), karena juga mengunci bitcoin berdasarkan hash dari sebuah kunci publik, yaitu, alamat penerima. Perbedaannya terletak pada bagaimana tanda tangan dan skrip disertakan dalam transaksi. Dalam kasus P2WPKH, informasi skrip tanda tangan (ScriptSig) dipindahkan dari struktur transaksi tradisional ke bagian terpisah yang disebut Witness. Pemindahan ini adalah fitur dari pembaruan SegWit (Segregated Witness). Teknik ini memiliki keuntungan mengurangi ukuran data transaksi dalam tubuh utama, sambil tetap mempertahankan informasi skrip yang diperlukan untuk validasi dalam bagian terpisah. Akibatnya, transaksi P2WPKH umumnya lebih murah dalam hal biaya dibandingkan dengan transaksi Legacy. Alamat P2WPKH ditulis menggunakan pengkodean Bech32, yang berkontribusi pada penulisan yang lebih ringkas dan kurang rentan kesalahan berkat checksum BCH. Alamat ini selalu dimulai dengan bc1q, membuatnya mudah dibedakan dari alamat penerima Legacy. P2WPKH adalah output SegWit versi 0.
**UTXO:** Akronim untuk Unspent Transaction Output. UTXO adalah output transaksi yang belum digunakan atau dihabiskan sebagai input untuk transaksi baru. UTXO mewakili fraksi bitcoin yang dimiliki pengguna dan yang saat ini tersedia untuk dihabiskan. Setiap UTXO dikaitkan dengan skrip output spesifik, yang mendefinisikan kondisi yang diperlukan untuk menghabiskan bitcoin tersebut. Transaksi dalam Bitcoin menggunakan UTXO ini sebagai input dan menciptakan UTXO baru sebagai output. Model UTXO sangat fundamental bagi Bitcoin, karena memungkinkan verifikasi yang mudah bahwa transaksi tidak mencoba menghabiskan bitcoin yang tidak ada atau telah dihabiskan. Pada dasarnya, UTXO adalah sepotong Bitcoin.






