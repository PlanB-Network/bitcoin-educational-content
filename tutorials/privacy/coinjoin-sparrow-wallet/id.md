---
name: Coinjoin - Sparrow Wallet
description: Bagaimana cara melakukan coinjoin di Sparrow Wallet?
---
![cover](assets/cover.webp)

***PERINGATAN:** Menyusul penangkapan pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, alat Whirlpool tidak lagi berfungsi, bahkan bagi individu yang memiliki Dojo mereka sendiri atau menggunakan Sparrow Wallet. Namun, masih mungkin bahwa alat ini dapat diaktifkan kembali dalam beberapa minggu ke depan atau diluncurkan kembali dengan cara yang berbeda. Selain itu, bagian teoretis dari artikel ini tetap relevan untuk memahami prinsip dan tujuan coinjoin secara umum (bukan hanya Whirlpool), serta memahami efektivitas model Whirlpool.*

_Kami terus mengikuti perkembangan kasus ini serta perkembangan terkait alat yang terkait. Yakinlah bahwa kami akan memperbarui tutorial ini seiring dengan tersedianya informasi baru._

_Tutorial ini disediakan hanya untuk tujuan pendidikan dan informasi. Kami tidak mendukung atau mendorong penggunaan alat ini untuk tujuan kriminal. Tanggung jawab setiap pengguna untuk mematuhi hukum di yurisdiksi mereka._

---

Dalam tutorial ini, Anda akan belajar apa itu coinjoin dan bagaimana cara melakukan coinjoin menggunakan perangkat lunak Sparrow Wallet dan implementasi Whirlpool.

## Apa itu coinjoin di Bitcoin?
**Coinjoin adalah teknik yang memutuskan jejak keberadaan bitcoin di blockchain**. Ini bergantung pada transaksi kolaboratif dengan struktur khusus yang bernama sama: transaksi coinjoin.

Coinjoin meningkatkan privasi pengguna Bitcoin dengan mempersulit analisis rantai bagi pengamat eksternal. Strukturnya memungkinkan penggabungan banyak koin dari pengguna yang berbeda ke dalam satu transaksi, sehingga mengaburkan jejak dan membuatnya sulit untuk menentukan hubungan antara alamat input dan output.

Prinsip dari coinjoin didasarkan pada pendekatan kolaboratif: beberapa pengguna yang ingin mencampur bitcoin mereka menyetorkan jumlah yang identik sebagai input dari transaksi yang sama. Jumlah ini kemudian didistribusikan kembali sebagai output dengan nilai yang sama untuk setiap pengguna. Di akhir transaksi, menjadi mustahil untuk mengaitkan output spesifik dengan pengguna yang diketahui di input. Tidak ada hubungan langsung antara input dan output, yang memutuskan asosiasi antara pengguna dan UTXO mereka, serta sejarah setiap koin.
![coinjoin](assets/notext/1.webp)

Contoh transaksi coinjoin (bukan dari saya): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

Untuk melakukan coinjoin sambil memastikan bahwa setiap pengguna tetap mengendalikan dana mereka setiap saat, proses dimulai dengan pembangunan transaksi oleh koordinator, yang kemudian mentransmisikannya ke setiap peserta. Setiap pengguna kemudian menandatangani transaksi setelah memverifikasi bahwa itu sesuai dengan mereka. Semua tanda tangan yang dikumpulkan akhirnya diintegrasikan ke dalam transaksi. Jika ada upaya untuk mengalihkan dana oleh pengguna atau koordinator, melalui modifikasi output transaksi coinjoin, tanda tangan akan terbukti tidak valid, yang mengarah pada penolakan transaksi oleh node.

Ada beberapa implementasi coinjoin, seperti Whirlpool, JoinMarket, atau Wabisabi, masing-masing bertujuan untuk mengelola koordinasi di antara peserta dan meningkatkan efisiensi transaksi coinjoin.
Dalam tutorial ini, kita akan fokus pada implementasi **Whirlpool**, yang saya anggap sebagai solusi paling efektif untuk melakukan coinjoins pada Bitcoin. Meskipun tersedia di beberapa dompet, tutorial ini secara eksklusif mengeksplorasi penggunaannya dengan perangkat lunak Sparrow Wallet Desktop.

## Mengapa Melakukan CoinJoins pada Bitcoin?

Salah satu masalah awal dengan sistem pembayaran peer-to-peer adalah double-spending: bagaimana mencegah individu jahat menghabiskan unit moneter yang sama beberapa kali tanpa harus menggunakan otoritas pusat untuk arbitrase?

Satoshi Nakamoto menyediakan solusi untuk dilema ini melalui protokol Bitcoin, sistem pembayaran elektronik peer-to-peer yang beroperasi secara independen dari otoritas pusat mana pun. Dalam white paper-nya, dia menekankan bahwa satu-satunya cara untuk memastikan tidak adanya double-spending adalah dengan memastikan visibilitas semua transaksi dalam sistem pembayaran.

Untuk memastikan setiap peserta mengetahui transaksi, mereka harus diungkapkan secara publik. Dengan demikian, operasi Bitcoin bergantung pada infrastruktur yang transparan dan terdistribusi, memungkinkan operator node mana pun untuk memverifikasi keseluruhan rantai tanda tangan elektronik dan sejarah setiap koin, dari penciptaannya oleh penambang.

Sifat transparan dan terdistribusi dari blockchain Bitcoin berarti bahwa setiap pengguna jaringan dapat mengikuti dan menganalisis transaksi semua peserta lain. Akibatnya, anonimitas pada tingkat transaksi adalah tidak mungkin. Namun, anonimitas dipertahankan pada tingkat identifikasi individu. Tidak seperti sistem perbankan tradisional di mana setiap akun dikaitkan dengan identitas pribadi, di Bitcoin, dana dikaitkan dengan pasangan kunci kriptografi, sehingga menawarkan pengguna bentuk pseudonimitas di balik pengenal kriptografi.

Oleh karena itu, kerahasiaan pada Bitcoin terkompromi ketika pengamat eksternal berhasil mengaitkan UTXO tertentu dengan pengguna yang teridentifikasi. Setelah asosiasi ini terbentuk, menjadi mungkin untuk melacak transaksi mereka dan menganalisis sejarah bitcoin mereka. Coinjoin adalah teknik yang dikembangkan secara tepat untuk memutuskan traceability dari UTXO, sehingga menawarkan lapisan kerahasiaan tertentu kepada pengguna Bitcoin pada tingkat transaksi.

## Bagaimana Cara Kerja Whirlpool?

Whirlpool menonjol dari metode coinjoin lainnya dengan menggunakan transaksi "_ZeroLink_", yang memastikan bahwa secara teknis tidak ada hubungan yang mungkin antara semua input dan semua output. Pencampuran sempurna ini dicapai melalui struktur di mana setiap peserta memberikan jumlah yang identik dalam input (kecuali untuk biaya penambangan), sehingga menghasilkan output dengan jumlah yang sama sempurna.

Pendekatan restriktif terhadap input memberikan transaksi coinjoin Whirlpool karakteristik unik: total ketiadaan tautan deterministik antara input dan output. Dengan kata lain, setiap output memiliki kemungkinan yang sama untuk diatribusikan kepada peserta mana pun, dibandingkan dengan semua output lain dari transaksi.
Awalnya, jumlah peserta dalam setiap coinjoin Whirlpool dibatasi menjadi 5, dengan 2 peserta baru dan 3 remixer (kami akan menjelaskan konsep ini lebih lanjut). Namun, peningkatan biaya transaksi on-chain yang diamati pada tahun 2023 mendorong tim Samourai untuk memikirkan kembali model mereka untuk meningkatkan privasi sambil mengurangi biaya. Dengan demikian, dengan mempertimbangkan situasi pasar biaya dan jumlah peserta, koordinator sekarang dapat mengatur coinjoins termasuk 6, 7, atau 8 peserta. Sesi yang ditingkatkan ini disebut sebagai "_Surge Cycles_". Penting untuk dicatat bahwa, terlepas dari pengaturannya, selalu hanya ada 2 peserta baru dalam coinjoins Whirlpool.

Oleh karena itu, transaksi Whirlpool ditandai dengan jumlah input dan output yang identik, yang bisa berupa:
- 5 input dan 5 output;
![coinjoin](assets/notext/2.webp)
- 6 input dan 6 output;
![coinjoin](assets/notext/3.webp)
- 7 input dan 7 output;
![coinjoin](assets/notext/4.webp)
- 8 input dan 8 output. ![coinjoin](assets/notext/5.webp)
Model yang diusulkan oleh Whirlpool didasarkan pada transaksi coinjoin berukuran kecil. Berbeda dengan Wasabi dan JoinMarket, di mana kekuatan anonset bergantung pada volume peserta dalam satu siklus, Whirlpool bertaruh pada penggabungan beberapa siklus berukuran kecil.

Dalam model ini, pengguna hanya menanggung biaya pada saat mereka pertama kali masuk ke dalam pool, memungkinkan mereka untuk berpartisipasi dalam berbagai remix tanpa biaya tambahan. Para peserta baru inilah yang menanggung biaya penambangan untuk para remixer.

Dengan setiap coinjoin tambahan yang diikuti oleh sebuah coin bersama dengan peer yang telah ditemuinya sebelumnya, anonset akan bertumbuh secara eksponensial. Tujuannya adalah untuk memanfaatkan remix gratis ini yang, dengan setiap kejadian, berkontribusi pada penguatan kepadatan anonset yang terkait dengan setiap coin yang dicampur.

Whirlpool dirancang dengan mempertimbangkan dua persyaratan penting:
- Kemudahan implementasi pada perangkat mobile, mengingat Samourai Wallet terutama adalah aplikasi smartphone;
- Kecepatan siklus remix untuk mendorong peningkatan signifikan dalam anonset.

Imperatif ini memandu pilihan para pengembang Samourai Wallet dalam perancangan Whirlpool, membawa mereka untuk membatasi jumlah peserta per siklus. Terlalu sedikit peserta akan mengompromikan efektivitas coinjoin, secara drastis mengurangi anonset yang dihasilkan dengan setiap siklus, sementara terlalu banyak peserta akan menimbulkan masalah manajemen pada aplikasi mobile dan akan menghambat aliran siklus.

**Pada akhirnya, tidak perlu memiliki jumlah peserta yang tinggi per coinjoin di Whirlpool karena anonset dibuat melalui akumulasi beberapa siklus coinjoin.**
[-> Pelajari lebih lanjut tentang anonset Whirlpool.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)
### Pool Coinjoin dan Biaya
Untuk memastikan bahwa beberapa siklus secara efektif meningkatkan anonset dari coin yang dicampur, harus ada kerangka kerja tertentu yang ditetapkan untuk membatasi jumlah UTXO yang digunakan. Whirlpool mendefinisikan berbagai pool untuk tujuan ini.

Sebuah pool mewakili sekelompok pengguna yang ingin mencampur bersama, yang sepakat tentang jumlah UTXO yang akan digunakan untuk mengoptimalkan proses coinjoin. Setiap pool menentukan jumlah tetap untuk UTXO, yang harus dipatuhi pengguna untuk berpartisipasi. Jadi, untuk melakukan coinjoin dengan Whirlpool, Anda perlu memilih sebuah pool. Pool yang tersedia saat ini adalah sebagai berikut:
- 0,5 bitcoin;
- 0,05 bitcoin;
- 0,01 bitcoin;
- 0,001 bitcoin (= 100.000 sats).

Dengan bergabung ke sebuah pool dengan bitcoin Anda, mereka akan dibagi untuk menghasilkan UTXO yang seragam sempurna dengan UTXO peserta lain di pool. Setiap pool memiliki batas maksimum; dengan demikian, untuk jumlah yang melebihi batas ini, Anda akan dipaksa untuk membuat dua entri terpisah dalam pool yang sama atau pindah ke pool lain dengan jumlah yang lebih tinggi:

| Pool (bitcoin) | Jumlah maksimum per entri (bitcoin) |
|----------------|------------------------------------|
| 0,5            | 35                                 |
| 0,05           | 3,5                                |
| 0,01           | 0,7                                |
| 0,001          | 0,025                              |
Seperti yang disebutkan sebelumnya, sebuah UTXO dianggap termasuk ke dalam sebuah kolam ketika siap untuk diintegrasikan ke dalam coinjoin. Namun, ini tidak berarti bahwa pengguna kehilangan kepemilikan atasnya. **Melalui berbagai siklus pencampuran, Anda tetap memiliki kontrol penuh atas kunci Anda dan, sebagai konsekuensinya, bitcoin Anda.** Inilah yang membedakan teknik coinjoin dari teknik pencampuran terpusat lainnya.

Untuk masuk ke kolam coinjoin, biaya layanan serta biaya penambangan harus dibayar. Biaya layanan ditetapkan untuk setiap kolam dan dimaksudkan untuk mengkompensasi tim yang bertanggung jawab atas pengembangan dan pemeliharaan Whirlpool. Bagi pengguna Sparrow Wallet, biaya ini diteruskan oleh tim Samourai kepada pengembang Sparrow.

Biaya layanan untuk menggunakan Whirlpool harus dibayar sekali saat memasuki kolam. Setelah langkah ini selesai, Anda memiliki kesempatan untuk berpartisipasi dalam jumlah remix yang tidak terbatas tanpa biaya tambahan. Berikut adalah biaya tetap saat ini untuk setiap kolam:

| Kolam (bitcoin) | Biaya Masuk (bitcoin) |
|-----------------|-----------------------|
| 0.5             | 0.0175                |
| 0.05            | 0.00175               |
| 0.01            | 0.0005 (50,000 sats)  |
| 0.001           | 0.00005 (5,000 sats)  |

Biaya ini pada dasarnya berfungsi sebagai tiket masuk ke kolam yang dipilih, terlepas dari jumlah yang Anda masukkan ke dalam coinjoin. Jadi, apakah Anda bergabung dengan kolam 0.01 dengan tepat 0.01 BTC atau Anda masuk dengan 0.5 BTC, biaya akan tetap sama dalam nilai absolut.

Sebelum melanjutkan dengan coinjoins, pengguna oleh karena itu memiliki pilihan antara 2 strategi:
- Memilih kolam yang lebih kecil untuk meminimalkan biaya layanan, mengetahui bahwa mereka akan menerima beberapa UTXO kecil sebagai balikannya;
- Atau lebih memilih kolam yang lebih besar, setuju untuk membayar biaya yang lebih tinggi untuk mendapatkan sejumlah UTXO bernilai besar yang lebih sedikit.

Umumnya disarankan untuk tidak menggabungkan beberapa UTXO campuran setelah siklus coinjoin, karena ini dapat mengompromikan kerahasiaan yang diperoleh, terutama karena Heuristik Kepemilikan Input Bersama (CIOH). Oleh karena itu, mungkin bijaksana untuk memilih kolam yang lebih besar, meskipun berarti membayar lebih, untuk menghindari memiliki terlalu banyak UTXO bernilai kecil sebagai output. Pengguna harus menimbang trade-off ini untuk memilih kolam yang mereka sukai.

Selain biaya layanan, biaya penambangan yang melekat pada setiap transaksi Bitcoin juga harus dipertimbangkan. Sebagai pengguna Whirlpool, Anda akan diminta untuk membayar biaya penambangan untuk transaksi persiapan (`Tx0`) serta untuk coinjoin pertama. Semua remix selanjutnya akan gratis, berkat model Whirlpool yang mengandalkan pembayaran dari peserta baru.

Memang, dalam setiap coinjoin Whirlpool, dua pengguna di antara input adalah peserta baru. Input lainnya berasal dari remixer. Akibatnya, biaya penambangan untuk semua peserta dalam transaksi ditanggung oleh dua peserta baru ini, yang kemudian juga akan mendapat manfaat dari remix gratis:
![coinjoin](assets/en/6.webp)
Berkat sistem biaya ini, Whirlpool benar-benar membedakan dirinya dari layanan coinjoin lainnya karena anonset dari UTXO tidak proporsional dengan harga yang dibayar oleh pengguna. Dengan demikian, dimungkinkan untuk mencapai tingkat anonimitas yang cukup tinggi hanya dengan membayar biaya masuk kolam dan biaya penambangan untuk dua transaksi (the `Tx0` dan campuran awal).
Penting untuk dicatat bahwa pengguna juga harus menanggung biaya penambangan untuk menarik UTXO mereka dari kolam setelah menyelesaikan beberapa coinjoin, kecuali mereka telah memilih opsi `mix to`, yang akan kita bahas dalam tutorial di bawah ini.
### Akun dompet HD yang digunakan oleh Whirlpool
Untuk melakukan coinjoin melalui Whirlpool, dompet harus menghasilkan beberapa akun yang berbeda. Sebuah akun, dalam konteks dompet HD (Hierarchical Deterministic), merupakan bagian yang sepenuhnya terisolasi dari yang lain, pemisahan ini terjadi pada tingkat kedalaman ketiga hierarki dompet, yaitu, pada tingkat `xpub`.
Sebuah dompet HD secara teoritis dapat menghasilkan hingga `2^(32/2)` akun yang berbeda. Akun awal, yang digunakan secara default di semua dompet Bitcoin, sesuai dengan indeks `0'`.

Untuk dompet yang disesuaikan dengan Whirlpool, seperti Samourai atau Sparrow, 4 akun digunakan untuk memenuhi kebutuhan proses coinjoin:
- Akun **deposit**, diidentifikasi dengan indeks `0'`;
- Akun **bad bank** (atau perubahan doxxic) diidentifikasi dengan indeks `2 147 483 644'`;
- Akun **premix**, diidentifikasi dengan indeks `2 147 483 645'`;
- Akun **postmix**, diidentifikasi dengan indeks `2 147 483 646'`.

Masing-masing akun ini memenuhi fungsi tertentu dalam coinjoin.

Semua akun ini terhubung ke satu seed, yang memungkinkan pengguna untuk memulihkan akses ke semua bitcoin mereka dengan menggunakan frasa pemulihan mereka dan, jika berlaku, passphrase mereka. Namun, perlu untuk menentukan kepada perangkat lunak, selama operasi pemulihan ini, indeks akun yang berbeda yang digunakan.

Mari kita lihat berbagai tahapan coinjoin Whirlpool dalam akun-akun ini.

### Tahapan berbeda dari coinjoins di Whirlpool
**Tahap 1: Tx0**
Titik awal dari setiap coinjoin Whirlpool adalah akun **deposit**. Akun ini adalah yang Anda gunakan secara otomatis ketika Anda membuat dompet Bitcoin baru. Akun ini harus dikreditkan dengan bitcoin yang ingin Anda campur.

`Tx0` mewakili tahap pertama dari proses pencampuran Whirlpool. Tujuannya adalah untuk mempersiapkan dan menyamakan UTXO untuk coinjoin, dengan membaginya menjadi unit yang sesuai dengan jumlah kolam yang dipilih, untuk memastikan homogenitas pencampuran. UTXO yang disamakan kemudian dikirim ke akun **premix**. Sedangkan perbedaan yang tidak dapat masuk ke kolam dipisahkan ke dalam akun tertentu: **bad bank** (atau "perubahan doxxic").

Transaksi awal `Tx0` ini juga berfungsi untuk menyelesaikan biaya layanan yang harus dibayar kepada koordinator campuran. Berbeda dengan tahapan berikutnya, transaksi ini tidak kolaboratif; pengguna oleh karena itu harus menanggung seluruh biaya penambangan:
![coinjoin](assets/en/7.webp)
Dalam contoh transaksi `Tx0` ini, sebuah input sebesar `372,000 sats` dari akun **deposit** kita dibagi menjadi beberapa UTXO keluar, yang didistribusikan sebagai berikut:
- Sejumlah `5,000 sats` yang ditujukan untuk koordinator untuk biaya layanan, sesuai dengan masuknya ke kolam `100,000 sats`;
- Tiga UTXO yang disiapkan untuk pencampuran, dialihkan ke akun **premix** kita dan didaftarkan dengan koordinator. UTXO ini disamakan pada `108,000 sats` masing-masing, untuk menutupi biaya penambangan untuk campuran awal mereka;
- Kelebihan, yang tidak dapat masuk ke dalam kolam karena terlalu kecil, dianggap sebagai perubahan beracun. Ini dikirim ke akun spesifiknya. Di sini, perubahan ini berjumlah `40,000 sats`;
- Akhirnya, ada `3,000 sats` yang tidak merupakan output, tetapi merupakan biaya penambangan yang diperlukan untuk mengonfirmasi `Tx0`.

Sebagai contoh, berikut ini adalah Tx0 Whirlpool nyata (yang tidak berasal dari saya): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Langkah 2: Perubahan Beracun**
Kelebihan, yang tidak dapat terintegrasi ke dalam kolam, di sini setara dengan `40,000 sats`, diarahkan kembali ke akun **bad bank**, juga disebut sebagai "perubahan beracun", untuk memastikan pemisahan ketat dari UTXO lainnya dalam dompet.

UTXO ini berbahaya bagi privasi pengguna karena tidak hanya selalu terikat dengan masa lalunya, dan oleh karena itu mungkin dengan identitas pemiliknya, tetapi juga, dicatat sebagai milik pengguna yang telah melakukan coinjoin.

Jika UTXO ini digabungkan dengan output campuran, yang terakhir akan kehilangan semua privasi yang diperoleh selama siklus coinjoin, terutama karena CIOH (*Common-Input-Ownership-Heuristic*). Jika digabungkan dengan perubahan beracun lainnya, pengguna berisiko kehilangan privasi karena ini akan menghubungkan berbagai entri dari siklus coinjoin. Oleh karena itu, harus diperlakukan dengan hati-hati. Cara mengelola UTXO beracun ini akan dijelaskan secara rinci di bagian terakhir dari artikel ini, dan tutorial mendatang akan lebih mendalam ke dalam metode-metode ini di Jaringan PlanB.

**Langkah 3: Campuran Awal**
Setelah penyelesaian `Tx0`, UTXO yang diseimbangkan dikirim ke akun **premix** dompet kami, siap untuk diperkenalkan ke dalam siklus coinjoin pertama mereka, juga disebut "campuran awal". Jika, seperti dalam contoh kami, `Tx0` menghasilkan beberapa UTXO yang dimaksudkan untuk pencampuran, masing-masing dari mereka akan diintegrasikan ke dalam coinjoin awal yang terpisah.
Di akhir campuran awal ini, akun **premix** akan kosong, sementara koin kami, setelah membayar biaya penambangan untuk coinjoin pertama ini, akan disesuaikan tepat ke jumlah yang ditentukan oleh kolam yang dipilih. Dalam contoh kami, UTXO awal kami sebesar `108 000 sats` akan dikurangi menjadi tepat `100 000 sats`.
![coinjoin](assets/en/8.webp)
**Langkah 4: Remixes**
Setelah campuran awal, UTXO ditransfer ke akun **postmix**. Akun ini mengumpulkan UTXO yang sudah dicampur dan yang menunggu remixing. Ketika klien Whirlpool aktif, UTXO yang berada di akun **postmix** secara otomatis tersedia untuk remixing dan akan dipilih secara acak untuk berpartisipasi dalam siklus baru ini.

Sebagai pengingat, remix kemudian 100% gratis: tidak diperlukan biaya layanan tambahan atau biaya penambangan. Menjaga UTXO di akun **postmix** dengan demikian mempertahankan nilai mereka tetap utuh, dan pada saat yang sama meningkatkan anonset mereka. Itulah mengapa penting untuk membiarkan koin-koin ini berpartisipasi dalam beberapa siklus coinjoin. Ini tidak mengeluarkan biaya apa pun dari Anda, dan meningkatkan tingkat anonimitas mereka.
Ketika Anda memutuskan untuk menghabiskan UTXO campuran, Anda dapat melakukannya langsung dari akun **postmix** ini. Disarankan untuk menyimpan UTXO campuran di akun ini untuk mendapatkan keuntungan dari remix gratis dan untuk mencegah mereka keluar dari sirkuit Whirlpool, yang dapat mengurangi privasi mereka.
Seperti yang akan kita lihat dalam tutorial berikut, ada juga opsi `mix to` yang menawarkan kemungkinan untuk secara otomatis mengirim koin campuran Anda ke dompet lain, seperti dompet dingin, setelah jumlah coinjoin yang ditentukan.

Setelah membahas teori, mari kita langsung praktik dengan tutorial menggunakan Whirlpool melalui perangkat lunak desktop Sparrow Wallet!

## Tutorial: Coinjoin Whirlpool di Sparrow Wallet
Ada banyak opsi untuk menggunakan Whirlpool. Yang pertama ingin saya perkenalkan kepada Anda adalah opsi Sparrow Wallet, sebuah perangkat lunak manajemen dompet Bitcoin sumber terbuka untuk PC.
Menggunakan Sparrow memiliki keuntungan karena cukup mudah untuk memulai, cepat untuk diatur, dan tidak memerlukan peralatan selain komputer dan koneksi internet. Namun, ada kekurangan yang patut diperhatikan: coinjoin hanya akan terjadi ketika Sparrow diluncurkan dan terhubung. Ini berarti jika Anda ingin mencampur dan mencampur ulang bitcoin Anda 24/7, Anda perlu terus menjaga komputer Anda tetap menyala.

### Instal Sparrow Wallet
Untuk memulai, Anda tentu saja akan memerlukan perangkat lunak Sparrow Wallet. Anda dapat langsung mengunduhnya dari [situs resmi](https://sparrowwallet.com/download/) atau di [GitHub mereka](https://github.com/sparrowwallet/sparrow/releases).

Sebelum menginstal perangkat lunak, akan penting untuk memverifikasi tanda tangan dan integritas dari eksekutabel yang baru saja Anda unduh. Jika Anda ingin lebih banyak detail tentang proses instalasi dan verifikasi perangkat lunak Sparrow, saya menyarankan Anda untuk membaca tutorial lain ini: *[Panduan Sparrow Wallet](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607)*.

### Membuat Dompet Perangkat Lunak
Setelah menginstal perangkat lunak, Anda perlu melanjutkan dengan membuat dompet Bitcoin. Penting untuk dicatat bahwa untuk berpartisipasi dalam coinjoin, penggunaan dompet perangkat lunak (juga disebut "hot wallet") adalah esensial. Oleh karena itu, **tidak akan mungkin untuk melakukan coinjoin dengan dompet yang diamankan oleh dompet perangkat keras**.

Meskipun tidak wajib, jika Anda berencana untuk mencampur jumlah yang signifikan, sangat disarankan untuk memilih penggunaan frasa sandi BIP39 yang kuat untuk dompet ini.

Untuk membuat dompet baru, buka Sparrow, lalu klik pada tab `File` dan `New Wallet`.

![sparrow](assets/notext/9.webp)

Pilih nama untuk dompet ini, misalnya: "Coinjoin Wallet". Klik pada tombol `Create Wallet`.

![sparrow](assets/notext/10.webp)

Biarkan pengaturan default, lalu klik pada tombol `New or Imported Software Wallet`.

![sparrow](assets/notext/11.webp)

Ketika Anda mengakses jendela pembuatan dompet, saya merekomendasikan memilih urutan 12 kata, karena itu sudah lebih dari cukup. Pilih `Generate New` untuk menghasilkan frasa pemulihan baru, dan klik pada `Use Passphrase` jika Anda ingin menambahkan frasa sandi BIP39. Penting untuk membuat cadangan informasi pemulihan Anda secara fisik, baik di kertas atau di dukungan logam, untuk memastikan keamanan bitcoin Anda.

![sparrow](assets/notext/12.webp)
Pastikan validitas cadangan frasa pemulihan Anda sebelum mengklik `Confirm Backup...`. Sparrow kemudian akan meminta Anda untuk memasukkan frasa Anda lagi untuk memverifikasi bahwa Anda telah mencatatnya. Setelah langkah ini selesai, lanjutkan dengan mengklik `Create Keystore`.
![sparrow](assets/notext/13.webp)
Biarkan jalur derivasi yang disarankan sebagai default dan tekan `Import Keystore`. Dalam contoh saya, jalur derivasi sedikit berbeda karena saya menggunakan Testnet untuk tutorial ini. Jalur derivasi yang seharusnya muncul untuk Anda adalah sebagai berikut:
```plaintext
m/84'/0'/0'
```

![sparrow](assets/notext/14.webp)

Setelah itu, Sparrow akan menampilkan detail derivasi dari dompet baru Anda. Jika Anda telah menetapkan passphrase, sangat disarankan untuk mencatat `Master fingerprint` Anda. Meskipun sidik jari kunci utama ini bukan data sensitif, ini akan berguna bagi Anda untuk nanti memverifikasi bahwa Anda memang mengakses dompet yang benar dan untuk mengonfirmasi ketiadaan kesalahan saat memasukkan passphrase Anda.

Klik tombol `Apply`.

![sparrow](assets/notext/15.webp)

Sparrow mengundang Anda untuk membuat kata sandi untuk dompet Anda. Kata sandi ini akan diperlukan untuk mengaksesnya melalui perangkat lunak Sparrow Wallet. Pilih kata sandi yang kuat, buat cadangan dari kata sandi tersebut, lalu klik pada `Set Password`.

![sparrow](assets/notext/16.webp)

### Menerima bitcoin
Setelah membuat dompet Anda, awalnya Anda akan memiliki satu akun, dengan indeks `0'`. Ini adalah akun **deposit** yang telah kita bahas di bagian sebelumnya. Ini adalah akun tempat Anda perlu mengirim bitcoin untuk dicampur.

Untuk melakukan ini, pilih tab `Receive` di sisi kiri jendela. Sparrow akan secara otomatis menghasilkan alamat baru yang kosong untuk menerima bitcoin.

![sparrow](assets/notext/17.webp)

Anda dapat memasukkan label untuk alamat ini, lalu kirim bitcoin yang akan dicampur ke alamat tersebut.

![sparrow](assets/notext/18.webp)

### Melakukan Tx0
Setelah transaksi Anda dikonfirmasi, Anda kemudian dapat pergi ke tab `UTXOs`.

![sparrow](assets/notext/19.webp)

Selanjutnya, pilih UTXO(s) yang ingin Anda kirimkan ke siklus coinjoin. Untuk memilih beberapa UTXO secara bersamaan, tahan tombol `Ctrl` sambil mengklik pada UTXO pilihan Anda.

![sparrow](assets/notext/20.webp)

Lalu klik tombol `Mix Selected` di bagian bawah jendela. Jika tombol ini tidak muncul di antarmuka Anda, itu karena Anda menggunakan dompet yang diamankan dengan dompet perangkat keras. Anda perlu menggunakan dompet perangkat lunak untuk melakukan coinjoins dengan Sparrow.
![sparrow](assets/notext/21.webp)
Sebuah jendela terbuka untuk menjelaskan bagaimana Whirlpool bekerja. Ini adalah penyederhanaan dari apa yang saya jelaskan di bagian sebelumnya. Klik `Next` untuk melanjutkan.

![sparrow](assets/notext/22.webp)

Di halaman berikutnya, Anda dapat memasukkan "SCODE" jika Anda memilikinya. SCODE adalah kode promosi yang menawarkan diskon pada biaya layanan pool. Samourai Wallet sesekali memberikan kode seperti ini kepada penggunanya selama acara khusus. Saya menyarankan Anda untuk [mengikuti Samourai Wallet](https://twitter.com/SamouraiWallet) di media sosial agar tidak ketinggalan SCODE masa depan.
Di halaman yang sama, Anda juga perlu menetapkan tarif biaya untuk `Tx0` dan campuran awal Anda. Pilihan ini akan mempengaruhi kecepatan konfirmasi untuk transaksi persiapan Anda dan coinjoin pertama Anda. Ingat bahwa Anda bertanggung jawab atas biaya penambangan untuk `Tx0` dan campuran awal, tetapi Anda tidak akan berutang biaya penambangan untuk remix selanjutnya. Sesuaikan slider `Premix Priority` sesuai dengan preferensi Anda, kemudian klik `Next`.
![sparrow](assets/notext/23.webp)

Di jendela baru ini, Anda akan memiliki opsi untuk memilih kolam yang ingin Anda masuki menggunakan daftar dropdown. Dalam kasus saya, setelah awalnya memilih UTXO sebesar `456 214 sats`, pilihan satu-satunya saya adalah kolam `100 000 sats`. Antarmuka ini juga memberi tahu Anda tentang biaya layanan yang harus dibayar serta jumlah UTXO yang akan diintegrasikan ke dalam kolam. Jika kondisinya tampak memuaskan bagi Anda, lanjutkan dengan mengklik `Preview Premix`.

![sparrow](assets/notext/24.webp)

Setelah langkah ini, Sparrow akan meminta Anda untuk memasukkan kata sandi untuk dompet Anda, yang Anda tetapkan saat membuatnya di perangkat lunak. Setelah kata sandi dimasukkan, Anda akan mengakses pratinjau `Tx0` Anda. Di sisi kiri jendela Anda, Anda akan melihat bahwa Sparrow telah menghasilkan akun yang berbeda yang diperlukan untuk menggunakan Whirlpool (`Deposit`, `Premix`, `Postmix`, dan `Badbank`). Anda juga akan memiliki kesempatan untuk melihat struktur `Tx0` Anda, dengan output yang berbeda:
- Biaya layanan;
- UTXO yang disejajarkan yang dimaksudkan untuk masuk ke kolam;
- Perubahan beracun (Doxxic Change).

![sparrow](assets/notext/25.webp)

Jika transaksi sesuai dengan keinginan Anda, klik `Broadcast Transaction` untuk menyiarkan `Tx0` Anda. Jika tidak, Anda memiliki opsi untuk menyesuaikan parameter `Tx0` ini dengan memilih `Clear` untuk menghapus data yang dimasukkan dan memulai proses pembuatan dari awal.

### Melakukan Coinjoins
Setelah Tx0 disiarkan, Anda akan menemukan UTXO Anda siap untuk dicampur di akun `Premix`.
![sparrow](assets/notext/26.webp)

Setelah `Tx0` dikonfirmasi, UTXO Anda akan terdaftar dengan koordinator, dan campuran awal akan dimulai secara otomatis secara berturut-turut.

![sparrow](assets/notext/27.webp)

Dengan memeriksa akun `Postmix`, Anda akan mengamati UTXO yang dihasilkan dari campuran awal. Koin-koin ini akan tetap siap untuk remix selanjutnya, yang tidak akan menimbulkan biaya tambahan.

![sparrow](assets/notext/28.webp)

Di kolom `Mixes`, dimungkinkan untuk melihat jumlah coinjoins yang dilakukan oleh setiap koin Anda. Seperti yang akan kita lihat di bagian selanjutnya, yang benar-benar penting bukanlah jumlah remix per se, tetapi lebih kepada anonsets yang terkait, meskipun kedua indikator ini sebagian terkait.

![sparrow](assets/notext/29.webp)

Untuk sementara menghentikan coinjoins, cukup klik `Stop Mixing`. Anda akan memiliki opsi untuk melanjutkan operasi kapan saja dengan memilih `Start Mixing`.

![sparrow](assets/notext/30.webp)
Untuk memastikan ketersediaan UTXO Anda secara terus-menerus untuk remixing, perlu untuk menjaga perangkat lunak Sparrow tetap aktif. Menutup perangkat lunak atau mematikan komputer Anda akan menjeda coinjoins. Solusi untuk mengatasi masalah ini adalah dengan menonaktifkan fungsi tidur melalui pengaturan sistem operasi Anda. Selain itu, Sparrow menawarkan opsi untuk mencegah komputer Anda tidur secara otomatis, yang dapat Anda temukan di bawah tab `Tools` dengan judul `Prevent Computer Sleep`.

![sparrow](assets/notext/31.webp)

### Menyelesaikan coinjoins
Untuk menghabiskan bitcoin yang telah dicampur Anda, Anda memiliki beberapa pilihan. Metode paling langsung adalah mengakses akun `Postmix` dan memilih tab `Send`.

![sparrow](assets/notext/32.webp)

Di bagian ini, Anda akan memiliki opsi untuk memasukkan alamat tujuan, jumlah yang akan dikirim, dan biaya transaksi, sama seperti transaksi lain yang dilakukan dengan Sparrow Wallet. Jika Anda mau, Anda juga dapat memanfaatkan fitur privasi lanjutan seperti Stonewall, dengan mengklik tombol `Privacy`.

![sparrow](assets/notext/33.webp)

[-> Pelajari lebih lanjut tentang transaksi Stonewall.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

Jika Anda ingin membuat seleksi koin yang lebih tepat untuk dibelanjakan, pergilah ke tab `UTXOs`. Pilih UTXO yang secara khusus ingin Anda konsumsi, kemudian tekan tombol `Send Selected` untuk memulai transaksi.

![sparrow](assets/notext/34.webp)
Akhirnya, opsi `Mix to...` yang tersedia di Sparrow memungkinkan penghapusan otomatis UTXO terpilih dari siklus coinjoin, tanpa menimbulkan biaya tambahan. Fitur ini memungkinkan penentuan jumlah remix setelah itu UTXO tidak akan diintegrasikan kembali ke akun `Postmix` Anda, tetapi akan langsung ditransfer ke dompet lain. Opsi ini sering digunakan untuk secara otomatis mengirim bitcoin yang telah dicampur ke cold wallet.
Untuk menggunakan opsi ini, mulailah dengan membuka dompet penerima bersamaan dengan dompet coinjoin Anda dalam perangkat lunak Sparrow.

![sparrow](assets/notext/35.webp)

Kemudian, pergilah ke tab `UTXOs`, dan pilih koin yang menarik bagi Anda, kemudian klik pada tombol `Mix to...` di bagian bawah jendela.

![sparrow](assets/notext/36.webp)

Sebuah jendela terbuka, mulailah dengan memilih dompet tujuan dari daftar dropdown.

![sparrow](assets/notext/37.webp)

Pilih ambang batas coinjoin di mana penarikan akan dilakukan secara otomatis. Saya tidak dapat memberi Anda jumlah remix yang tepat untuk dilakukan, karena ini bervariasi menurut situasi pribadi Anda dan tujuan privasi Anda, tetapi hindari memilih ambang batas yang terlalu rendah. Saya merekomendasikan untuk berkonsultasi dengan artikel lain ini untuk mempelajari lebih lanjut tentang proses remixing: [REMIX - WHIRLPOOL](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa).

Anda dapat meninggalkan opsi `Index range` pada nilai defaultnya, `Full`. Fungsi ini memungkinkan pencampuran secara simultan dari klien yang berbeda, tetapi itu bukan yang ingin kita lakukan dalam tutorial ini. Untuk menyelesaikan dan mengaktifkan opsi `Mix to...`, tekan `Restart Whirlpool`.

![sparrow](assets/notext/38.webp)

Namun, berhati-hatilah saat menggunakan opsi `Mix to`, karena mengeluarkan koin campuran dari akun `Postmix` Anda dapat secara signifikan meningkatkan risiko kompromi privasi Anda. Alasan potensial untuk ini dijelaskan dalam bagian berikut.

## Bagaimana cara mengetahui kualitas dari siklus coinjoin kita?
Untuk coinjoin agar benar-benar efektif, sangat penting bahwa ia menunjukkan homogenitas yang baik antara jumlah input dan output. Keseragaman ini memperluas jumlah interpretasi yang mungkin di mata pengamat eksternal, sehingga meningkatkan ketidakpastian seputar transaksi. Untuk mengukur ketidakpastian yang dihasilkan oleh coinjoin, seseorang dapat menghitung entropi transaksi. Untuk eksplorasi mendalam tentang indikator-indikator ini, saya mengarahkan Anda ke tutorial: [BOLTZMANN CALCULATOR](https://planb.network/en/tutorials/privacy/boltzmann-entropy). Model Whirlpool diakui sebagai yang membawa homogenitas terbanyak dalam coinjoins. Selanjutnya, kinerja beberapa siklus coinjoin dievaluasi berdasarkan ukuran grup tempat sebuah koin disembunyikan. Ukuran grup ini mendefinisikan apa yang disebut anonsets. Ada dua jenis anonsets: yang pertama menilai privasi yang diperoleh terhadap analisis retrospektif (dari sekarang ke masa lalu) dan yang kedua, terhadap analisis prospektif (dari masa lalu ke sekarang). Untuk penjelasan rinci tentang kedua indikator ini, saya mengundang Anda untuk mengkonsultasikan tutorial: [WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375).

## Bagaimana mengelola postmix?
Setelah melakukan siklus coinjoin, strategi terbaik adalah menyimpan UTXO Anda di akun **postmix**, menunggu penggunaan masa depan mereka. Bahkan disarankan untuk membiarkan mereka remix secara tak terbatas sampai Anda perlu menghabiskannya.

Beberapa pengguna mungkin mempertimbangkan untuk mentransfer bitcoin yang telah dicampur ke dompet yang diamankan oleh dompet perangkat keras. Ini mungkin, tetapi penting untuk mengikuti rekomendasi dari Samourai Wallet secara teliti agar tidak mengompromikan kerahasiaan yang diperoleh.

Menggabungkan UTXO adalah kesalahan yang paling sering dilakukan. Perlu untuk menghindari menggabungkan UTXO yang telah dicampur dengan UTXO yang belum dicampur dalam transaksi yang sama, untuk menghindari CIOH (*Common-Input-Ownership-Heuristic*). Ini memerlukan pengelolaan UTXO Anda dalam dompet Anda dengan hati-hati, terutama dalam hal pelabelan. Di luar coinjoin, menggabungkan UTXO umumnya merupakan praktik buruk yang sering menyebabkan kehilangan privasi jika tidak dikelola dengan benar.

Juga penting untuk berhati-hati dalam mengkonsolidasikan UTXO yang telah dicampur satu sama lain. Konsolidasi moderat dapat dipertimbangkan jika UTXO yang telah dicampur Anda memiliki anonsets yang signifikan, tetapi ini akan tak terhindarkan menurunkan kerahasiaan koin Anda. Pastikan konsolidasi tidak terlalu besar atau dilakukan setelah jumlah remix yang tidak cukup, karena ini berisiko menetapkan tautan yang dapat ditelusuri antara UTXO Anda sebelum dan setelah siklus coinjoin. Jika ragu tentang manipulasi ini, praktik terbaik adalah tidak mengkonsolidasikan UTXO postmix, dan mentransfernya satu per satu ke dompet perangkat keras Anda, menghasilkan alamat kosong baru setiap kali. Lagi, ingat untuk memberi label yang tepat pada setiap UTXO yang diterima.
Juga disarankan untuk tidak mentransfer UTXO postmix Anda ke dompet yang menggunakan skrip tidak umum. Misalnya, jika Anda memasuki Whirlpool dari dompet multisig yang menggunakan skrip `P2WSH`, ada sedikit kesempatan Anda akan dicampur dengan pengguna lain yang memiliki jenis dompet yang sama secara asli. Jika Anda menarik postmix Anda ke dompet multisig yang sama ini, tingkat privasi bitcoin yang telah dicampur Anda akan sangat berkurang. Di luar skrip, ada banyak jejak dompet lain yang dapat menipu Anda.
Seperti halnya transaksi Bitcoin apa pun, juga penting untuk tidak menggunakan kembali alamat penerimaan. Setiap transaksi baru harus diterima di alamat kosong baru.
Solusi paling sederhana dan aman adalah membiarkan UTXO campuran Anda beristirahat di akun **postmix** mereka, membiarkan mereka remix dan hanya menyentuhnya untuk pengeluaran. Dompet Samourai dan Sparrow memiliki perlindungan tambahan terhadap semua risiko terkait analisis rantai ini. Perlindungan ini membantu Anda menghindari kesalahan.

## Bagaimana cara mengelola perubahan doxxic?
Selanjutnya, Anda perlu berhati-hati dalam mengelola perubahan doxxic, perubahan yang tidak bisa masuk ke kolam coinjoin. UTXO beracun ini, yang dihasilkan dari penggunaan Whirlpool, menimbulkan risiko terhadap privasi Anda karena mereka menetapkan tautan antara Anda dan penggunaan coinjoin. Oleh karena itu, sangat penting untuk menanganinya dengan hati-hati dan tidak menggabungkannya dengan UTXO lain, terutama UTXO campuran. Berikut adalah strategi yang berbeda untuk mempertimbangkan penggunaannya:
- **Campurkan mereka di kolam yang lebih kecil:** Jika UTXO beracun Anda cukup signifikan untuk masuk ke kolam yang lebih kecil sendirian, pertimbangkan untuk mencampurnya. Ini seringkali merupakan opsi terbaik. Namun, sangat penting untuk tidak menggabungkan beberapa UTXO beracun untuk mengakses kolam, karena ini dapat menghubungkan berbagai entri Anda;
- **Tandai mereka sebagai "tidak dapat dibelanjakan":** Pendekatan lain adalah untuk tidak lagi menggunakannya, menandainya sebagai "tidak dapat dibelanjakan" di akun khusus mereka, dan hanya Hodl. Ini memastikan Anda tidak secara tidak sengaja menghabiskannya. Jika nilai bitcoin meningkat, kolam baru yang lebih cocok untuk UTXO beracun Anda mungkin muncul;
- **Buat donasi:** Pertimbangkan untuk membuat donasi, bahkan yang sederhana, kepada pengembang yang bekerja pada Bitcoin dan perangkat lunak terkaitnya. Anda juga dapat mendonasikan ke organisasi yang menerima BTC. Jika mengelola UTXO beracun Anda terlalu rumit, Anda dapat dengan mudah menyingkirkannya dengan membuat donasi;
- **Beli Kartu Hadiah:** Platform seperti [Bitrefill](https://www.bitrefill.com/) memungkinkan Anda menukar bitcoin dengan kartu hadiah yang dapat digunakan di berbagai pedagang. Ini bisa menjadi cara untuk menyingkirkan UTXO beracun Anda tanpa kehilangan nilai terkait.
- **Konsolidasikan mereka di Monero:** Dompet Samourai sekarang menawarkan layanan pertukaran atom antara BTC dan XMR. Ini ideal untuk mengelola UTXO beracun dengan mengkonsolidasikannya di Monero, tanpa mengorbankan privasi Anda melalui CIOH, sebelum mengirimkannya kembali ke Bitcoin. Namun, opsi ini bisa mahal dalam hal biaya penambangan dan premi karena kendala likuiditas.
- **Kirimkan mereka ke Lightning Network:** Memindahkan UTXO ini ke Lightning Network untuk mendapatkan manfaat dari biaya transaksi yang lebih rendah adalah opsi yang mungkin menarik. Namun, metode ini dapat mengungkapkan informasi tertentu tergantung pada penggunaan Lightning Anda dan oleh karena itu harus dipraktikkan dengan hati-hati.

Tutorial terperinci tentang implementasi teknik-teknik berbeda ini akan segera ditawarkan di PlanB Network.

**Sumber Daya Tambahan:**
- [Sparrow Wallet Video Tutorial](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607);
- [Samourai Wallet Video Tutorial](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956);
- [Dokumentasi Samourai Wallet - Whirlpool](https://docs.samourai.io/whirlpool/basic-concepts);
- [Thread Twitter tentang CoinJoins](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Postingan Blog tentang CoinJoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).