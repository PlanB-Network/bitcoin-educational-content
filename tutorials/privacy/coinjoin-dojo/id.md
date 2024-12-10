---
name: Coinjoin - Dojo
description: Bagaimana cara melakukan coinjoin dengan Dojo Anda sendiri?
---
![cover](assets/cover.webp)

***PERINGATAN:** Menyusul penangkapan pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, alat Whirlpool tidak lagi berfungsi, bahkan bagi individu yang memiliki Dojo mereka sendiri atau menggunakan Sparrow Wallet. Namun, masih mungkin bahwa alat ini dapat diaktifkan kembali dalam beberapa minggu mendatang atau diluncurkan kembali dengan cara yang berbeda. Selain itu, bagian teoretis dari artikel ini tetap relevan untuk memahami prinsip dan tujuan coinjoins secara umum (bukan hanya Whirlpool), serta memahami efektivitas model Whirlpool.*

_Kami terus mengikuti perkembangan kasus ini serta perkembangan terkait alat yang terkait. Yakinlah bahwa kami akan memperbarui tutorial ini seiring dengan tersedianya informasi baru._

_Tutorial ini disediakan hanya untuk tujuan pendidikan dan informasi. Kami tidak mendukung atau mendorong penggunaan alat ini untuk tujuan kriminal. Tanggung jawab setiap pengguna untuk mematuhi hukum di yurisdiksi mereka._

---

Dalam tutorial ini, Anda akan belajar apa itu coinjoin dan bagaimana cara melakukan satu menggunakan perangkat lunak Samourai Wallet dan implementasi Whirlpool, dengan menggunakan Dojo Anda sendiri. Menurut saya, metode ini saat ini adalah yang terbaik untuk mencampur bitcoin Anda.

## Apa itu coinjoin pada Bitcoin?
**Coinjoin adalah teknik yang memutuskan jejak bitcoin di blockchain**. Ini bergantung pada transaksi kolaboratif dengan struktur khusus yang bernama sama: transaksi coinjoin.

Coinjoins meningkatkan privasi pengguna Bitcoin dengan mempersulit analisis rantai bagi pengamat eksternal. Strukturnya memungkinkan penggabungan beberapa koin dari pengguna yang berbeda ke dalam satu transaksi, sehingga mengaburkan jejak dan membuatnya sulit untuk menentukan hubungan antara alamat input dan output.

Prinsip dari coinjoin didasarkan pada pendekatan kolaboratif: beberapa pengguna yang ingin mencampur bitcoin mereka menyetorkan jumlah yang identik sebagai input dari transaksi yang sama. Jumlah-jumlah ini kemudian didistribusikan kembali sebagai output dengan nilai yang sama untuk setiap pengguna. Di akhir transaksi, menjadi mustahil untuk mengaitkan output tertentu dengan pengguna yang diketahui di input. Tidak ada hubungan langsung antara input dan output, yang memutuskan asosiasi antara pengguna dan UTXO mereka, serta sejarah setiap koin.
![coinjoin](assets/notext/1.webp)

Contoh transaksi coinjoin (bukan dari saya): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

Untuk melakukan coinjoin sambil memastikan bahwa setiap pengguna tetap mengendalikan dana mereka setiap saat, proses dimulai dengan transaksi yang dibangun oleh koordinator, yang kemudian mengirimkannya ke para peserta. Setiap pengguna kemudian menandatangani transaksi setelah memverifikasi bahwa itu sesuai dengan mereka. Semua tanda tangan yang dikumpulkan akhirnya diintegrasikan ke dalam transaksi. Jika ada upaya untuk mengalihkan dana oleh pengguna atau koordinator, melalui modifikasi output transaksi coinjoin, tanda tangan akan terbukti tidak valid, yang mengarah pada penolakan transaksi oleh node.

Ada beberapa implementasi coinjoin, seperti Whirlpool, JoinMarket, atau Wabisabi, masing-masing bertujuan untuk mengelola koordinasi di antara peserta dan meningkatkan efisiensi transaksi coinjoin.
Dalam tutorial ini, kita akan mendalami implementasi **Whirlpool**, yang saya anggap sebagai solusi paling efisien untuk melakukan coinjoins pada Bitcoin. Meskipun tersedia di beberapa dompet, dalam tutorial ini, kita akan secara eksklusif menjelajahi penggunaannya dengan aplikasi mobile Samourai Wallet, tanpa Dojo.
## Mengapa melakukan coinjoins pada Bitcoin?
Salah satu masalah awal dengan sistem pembayaran peer-to-peer adalah double spending: bagaimana mencegah individu jahat menghabiskan unit moneter yang sama beberapa kali tanpa harus menggunakan otoritas pusat untuk mengadili?

Satoshi Nakamoto menyediakan solusi untuk dilema ini melalui protokol Bitcoin, sistem pembayaran elektronik peer-to-peer yang beroperasi secara independen dari otoritas pusat mana pun. Dalam makalah putihnya, dia menekankan bahwa satu-satunya cara untuk memastikan tidak adanya double spending adalah dengan memastikan visibilitas semua transaksi dalam sistem pembayaran.

Untuk memastikan setiap peserta mengetahui transaksi, mereka harus diungkapkan secara publik. Oleh karena itu, operasi Bitcoin bergantung pada infrastruktur yang transparan dan terdistribusi, memungkinkan operator node mana pun untuk memverifikasi keseluruhan rantai tanda tangan elektronik dan sejarah setiap koin, dari penciptaannya oleh penambang.

Sifat transparan dan terdistribusi dari blockchain Bitcoin berarti bahwa setiap pengguna jaringan dapat mengikuti dan menganalisis transaksi semua peserta lain. Akibatnya, anonimitas pada tingkat transaksi adalah tidak mungkin. Namun, anonimitas dipertahankan pada tingkat identifikasi individu. Tidak seperti sistem perbankan tradisional di mana setiap akun dikaitkan dengan identitas pribadi, di Bitcoin, dana dikaitkan dengan pasangan kunci kriptografi, sehingga menawarkan pengguna bentuk pseudonimitas di balik pengenal kriptografi.

Dengan demikian, kerahasiaan pada Bitcoin terkompromi ketika pengamat eksternal berhasil mengasosiasikan UTXO tertentu dengan pengguna yang diidentifikasi. Setelah asosiasi ini terbentuk, menjadi mungkin untuk melacak transaksi mereka dan menganalisis sejarah bitcoin mereka. Coinjoin adalah teknik yang dikembangkan secara tepat untuk memutuskan traceability dari UTXO, dengan demikian menawarkan lapisan kerahasiaan tertentu kepada pengguna Bitcoin pada tingkat transaksi.

## Bagaimana cara Whirlpool bekerja?
Whirlpool menonjol dari metode coinjoin lainnya dengan menggunakan transaksi "_ZeroLink_", yang memastikan bahwa secara teknis tidak ada hubungan yang mungkin antara semua input dan semua output. Pencampuran sempurna ini dicapai melalui struktur di mana setiap peserta memberikan jumlah yang identik dalam input (kecuali untuk biaya penambangan), sehingga menghasilkan output dengan jumlah yang sama sempurna.
Pendekatan restriktif terhadap input memberikan transaksi coinjoin Whirlpool fitur unik: ketiadaan lengkap tautan deterministik antara input dan output. Dengan kata lain, setiap output memiliki kemungkinan yang sama untuk diatribusikan kepada peserta mana pun, dibandingkan dengan semua output lain dalam transaksi.
Awalnya, jumlah peserta dalam setiap coinjoin Whirlpool dibatasi menjadi 5, dengan 2 peserta baru dan 3 remixer (kami akan menjelaskan konsep ini lebih lanjut). Namun, peningkatan biaya transaksi on-chain yang diamati pada tahun 2023 mendorong tim Samourai untuk memikirkan kembali model mereka untuk meningkatkan privasi sambil mengurangi biaya. Dengan demikian, dengan mempertimbangkan situasi pasar biaya dan jumlah peserta, koordinator sekarang dapat mengorganisir coinjoins termasuk 6, 7, atau 8 peserta. Sesi yang ditingkatkan ini disebut sebagai "_Surge Cycles_". Penting untuk dicatat bahwa, terlepas dari pengaturannya, selalu hanya ada 2 peserta baru dalam coinjoins Whirlpool.

Dengan demikian, transaksi Whirlpool ditandai dengan jumlah input dan output yang identik, yang bisa:
- 5 input dan 5 output;
![coinjoin](assets/notext/2.webp)
- 6 input dan 6 output;
![coinjoin](assets/notext/3.webp)
- 7 input dan 7 output;
![coinjoin](assets/notext/4.webp)- 8 input dan 8 output.
![coinjoin](assets/notext/5.webp)
Model yang diusulkan oleh Whirlpool didasarkan pada transaksi coinjoin berukuran kecil. Berbeda dengan Wasabi dan JoinMarket, di mana kekuatan anonset bergantung pada volume peserta dalam satu siklus, Whirlpool bertaruh pada penggabungan beberapa siklus berukuran kecil.

Dalam model ini, pengguna hanya membayar biaya pada saat mereka pertama kali masuk ke dalam sebuah pool, memungkinkan mereka untuk berpartisipasi dalam berbagai remix tanpa biaya tambahan. Para peserta baru inilah yang menanggung biaya penambangan untuk para remixer.

Dengan setiap coinjoin tambahan yang diikuti oleh sebuah coin bersama dengan peer yang telah ditemuinya sebelumnya, anonset akan bertumbuh secara eksponensial. Tujuannya adalah untuk memanfaatkan remix gratis ini yang, dengan setiap kejadiannya, berkontribusi pada peningkatan kepadatan anonset yang terkait dengan setiap coin yang dicampur.

Whirlpool dirancang dengan mempertimbangkan dua persyaratan penting:
- Kemudahan implementasi pada perangkat mobile, mengingat Samourai Wallet terutama adalah aplikasi smartphone;
- Kecepatan siklus remix untuk mendorong peningkatan signifikan dalam anonset.
Imperatif ini memandu pilihan para pengembang Samourai Wallet dalam desain Whirlpool, membawa mereka untuk membatasi jumlah peserta per siklus. Terlalu sedikit peserta akan mengompromikan efisiensi coinjoin, secara drastis mengurangi anonset yang dihasilkan setiap siklus, sementara terlalu banyak peserta akan menimbulkan masalah manajemen pada aplikasi mobile dan akan menghambat aliran siklus.
**Pada akhirnya, tidak perlu memiliki jumlah peserta yang tinggi per coinjoin di Whirlpool karena anonset dicapai melalui akumulasi beberapa siklus coinjoin.**

[-> Pelajari lebih lanjut tentang anonset Whirlpool.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### Pool dan biaya coinjoin
Agar siklus berganda ini secara efektif meningkatkan anonset dari coin yang dicampur, sebuah kerangka kerja tertentu harus ditetapkan untuk membatasi jumlah UTXO yang digunakan. Whirlpool mendefinisikan berbagai pool.

Sebuah pool mewakili sekelompok pengguna yang ingin mencampur bersama, yang setuju pada jumlah UTXO yang akan digunakan untuk mengoptimalkan proses coinjoin. Setiap pool menentukan jumlah tetap untuk UTXO, yang harus dipatuhi pengguna untuk berpartisipasi. Jadi, untuk melakukan coinjoin dengan Whirlpool, Anda perlu memilih sebuah pool. Pool yang saat ini tersedia adalah sebagai berikut:
- 0,5 bitcoin;
- 0,05 bitcoin;
- 0,01 bitcoin;
- 0,001 bitcoin (= 100.000 sats).

Dengan bergabung ke sebuah pool dengan bitcoin Anda, mereka akan dibagi untuk menghasilkan UTXO yang sempurna homogen dengan UTXO peserta lain dalam pool. Setiap pool memiliki batas maksimum; dengan demikian, untuk jumlah yang melebihi batas ini, Anda akan dipaksa untuk membuat dua entri terpisah dalam pool yang sama atau pindah ke pool lain dengan jumlah yang lebih tinggi:

| Pool (bitcoin) | Jumlah maksimum per entri (bitcoin) |
|----------------|------------------------------------|
| 0,5            | 35                                 |
| 0,05           | 3,5                                |
| 0,01           | 0,7                                |
| 0,001          | 0,025                              |
Seperti yang telah disebutkan sebelumnya, sebuah UTXO dianggap termasuk ke dalam sebuah pool ketika siap untuk diintegrasikan ke dalam coinjoin. Namun, ini tidak berarti bahwa pengguna kehilangan kepemilikan atasnya. **Melalui berbagai siklus pencampuran, Anda tetap memiliki kontrol penuh atas kunci Anda dan, sebagai konsekuensinya, bitcoin Anda.** Inilah yang membedakan teknik coinjoin dari teknik pencampuran terpusat lainnya.
Untuk masuk ke dalam pool coinjoin, biaya layanan serta biaya penambangan harus dibayar. Biaya layanan ditetapkan untuk setiap pool dan dimaksudkan untuk mengkompensasi tim yang bertanggung jawab atas pengembangan dan pemeliharaan Whirlpool.
Biaya layanan untuk menggunakan Whirlpool hanya perlu dibayar sekali saat memasuki pool. Setelah langkah ini, Anda memiliki kesempatan untuk berpartisipasi dalam jumlah remix tanpa batas tanpa biaya tambahan. Berikut adalah biaya tetap saat ini untuk setiap pool:

| Pool (bitcoin) | Biaya Masuk (bitcoin)      |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


Biaya ini pada dasarnya berfungsi sebagai tiket masuk untuk pool yang dipilih, terlepas dari jumlah yang Anda masukkan ke dalam coinjoin. Jadi, apakah Anda bergabung dengan pool 0.01 dengan tepat 0.01 BTC atau memasukinya dengan 0.5 BTC, biaya akan tetap sama dalam nilai absolut.

Sebelum melanjutkan ke coinjoins, pengguna oleh karena itu memiliki pilihan antara 2 strategi:
- Memilih pool yang lebih kecil untuk meminimalkan biaya layanan, mengetahui bahwa mereka akan menerima beberapa UTXO kecil sebagai balikannya;
- Atau lebih memilih pool yang lebih besar, setuju untuk membayar biaya yang lebih tinggi untuk mendapatkan jumlah UTXO yang lebih besar dengan nilai yang lebih tinggi.

Umumnya disarankan untuk tidak menggabungkan beberapa UTXO campuran setelah siklus coinjoin, karena ini dapat mengompromikan kerahasiaan yang diperoleh, terutama karena Heuristik Kepemilikan Input Bersama (CIOH). Oleh karena itu, mungkin bijaksana untuk memilih pool yang lebih besar, meskipun berarti membayar lebih, untuk menghindari memiliki terlalu banyak UTXO bernilai kecil di output. Pengguna harus menimbang trade-off ini untuk memilih pool yang mereka sukai.

Selain biaya layanan, biaya penambangan yang melekat pada setiap transaksi Bitcoin juga harus dipertimbangkan. Sebagai pengguna Whirlpool, Anda akan diwajibkan untuk membayar biaya penambangan untuk transaksi persiapan (`Tx0`) serta untuk coinjoin pertama. Semua remix selanjutnya akan gratis, berkat model Whirlpool yang mengandalkan pembayaran dari peserta baru.

Memang, dalam setiap coinjoin Whirlpool, dua pengguna di antara input adalah peserta baru. Input lainnya berasal dari remixer. Akibatnya, biaya penambangan untuk semua peserta dalam transaksi ditanggung oleh dua peserta baru ini, yang kemudian juga akan mendapat manfaat dari remix gratis:
![coinjoin](assets/en/6.webp)
Berkat sistem biaya ini, Whirlpool benar-benar membedakan dirinya dari layanan coinjoin lainnya karena anonsets dari UTXO tidak proporsional dengan harga yang dibayar oleh pengguna. Dengan demikian, dimungkinkan untuk mencapai tingkat anonimitas yang cukup tinggi hanya dengan membayar biaya masuk pool dan biaya penambangan untuk dua transaksi (the `Tx0` dan campuran awal).
Penting untuk dicatat bahwa pengguna juga harus menanggung biaya penambangan untuk menarik UTXO mereka dari kolam setelah menyelesaikan beberapa coinjoin, kecuali mereka telah memilih opsi `mix to`, yang akan kita bahas dalam tutorial di bawah ini.
### Akun dompet HD yang digunakan oleh Whirlpool
Untuk melakukan coinjoin melalui Whirlpool, dompet harus menghasilkan beberapa akun yang berbeda. Sebuah akun, dalam konteks dompet HD (*Hierarchical Deterministic*), merupakan bagian yang sepenuhnya terisolasi dari yang lain, pemisahan ini terjadi pada tingkat kedalaman ketiga dari hierarki dompet, yaitu, pada tingkat `xpub`.

Sebuah dompet HD secara teoritis dapat menghasilkan hingga `2^(32/2)` akun yang berbeda. Akun awal, yang digunakan secara default di semua dompet Bitcoin, sesuai dengan indeks `0'`.

Untuk dompet yang disesuaikan dengan Whirlpool, seperti Samourai atau Sparrow, 4 akun digunakan untuk memenuhi kebutuhan proses coinjoin:
- Akun **deposit**, diidentifikasi dengan indeks `0'`;
- Akun **bad bank** (atau perubahan doxxic) diidentifikasi dengan indeks `2 147 483 644'`;
- Akun **premix**, diidentifikasi dengan indeks `2 147 483 645'`;
- Akun **postmix**, diidentifikasi dengan indeks `2 147 483 646'`.

Masing-masing akun ini memenuhi fungsi tertentu dalam coinjoin.

Semua akun ini terhubung ke satu seed, yang memungkinkan pengguna untuk memulihkan akses ke semua bitcoin mereka menggunakan frasa pemulihan mereka dan, jika perlu, passphrase mereka. Namun, perlu untuk menentukan ke perangkat lunak, selama operasi pemulihan ini, indeks akun yang berbeda yang digunakan.

Mari kita lihat berbagai tahapan coinjoin Whirlpool dalam akun-akun ini.

### Tahapan berbeda dari coinjoins di Whirlpool
**Tahap 1: Tx0**
Titik awal dari setiap coinjoin Whirlpool adalah akun **deposit**. Akun ini adalah yang Anda gunakan secara otomatis ketika Anda membuat dompet Bitcoin baru. Akun ini harus dikreditkan dengan bitcoin yang ingin dicampur.
`Tx0` mewakili langkah pertama dalam proses pencampuran Whirlpool. Ini bertujuan untuk mempersiapkan dan menyamakan UTXO untuk coinjoin, dengan membaginya menjadi unit yang sesuai dengan jumlah kolam yang dipilih, untuk memastikan homogenitas pencampuran. UTXO yang disamakan kemudian dikirim ke akun **premix**. Sedangkan perbedaan yang tidak dapat masuk ke kolam, dipisahkan ke dalam akun tertentu: **bad bank** (atau "perubahan doxxic").
Transaksi awal `Tx0` ini juga berfungsi untuk menyelesaikan biaya layanan yang harus dibayar kepada koordinator campuran. Tidak seperti langkah-langkah berikutnya, transaksi ini tidak kolaboratif; pengguna oleh karena itu harus menanggung semua biaya penambangan:
![coinjoin](assets/en/7.webp)

Dalam contoh transaksi `Tx0` ini, sebuah input sebesar `372,000 sats` dari akun **deposit** kita dibagi menjadi beberapa output UTXO, yang didistribusikan sebagai berikut:
- Sejumlah `5,000 sats` yang ditujukan untuk koordinator untuk biaya layanan, sesuai dengan masuknya ke kolam sebesar `100,000 sats`;
- Tiga UTXO yang disiapkan untuk pencampuran, dialihkan ke akun **premix** kita dan didaftarkan dengan koordinator. UTXO ini disamakan pada `108,000 sats` masing-masing, untuk menutupi biaya penambangan untuk campuran awal mereka;
- Kelebihan yang tidak bisa masuk ke dalam kolam, karena terlalu kecil, dianggap sebagai perubahan beracun. Ini dikirim ke akun spesifiknya. Di sini, perubahan ini berjumlah `40,000 sats`;
- Akhirnya, ada `3,000 sats` yang tidak merupakan output, tetapi merupakan biaya penambangan yang diperlukan untuk mengonfirmasi `Tx0`.

Sebagai contoh, berikut ini adalah transaksi Whirlpool Tx0 nyata (bukan dari saya): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Langkah 2: Perubahan Beracun**
Kelebihan yang tidak dapat diintegrasikan ke dalam kolam, di sini setara dengan `40,000 sats`, dialihkan ke akun **bank buruk**, juga disebut sebagai "perubahan beracun", untuk memastikan pemisahan ketat dari UTXO lain dalam dompet.

UTXO ini berbahaya bagi privasi pengguna karena tidak hanya masih terikat dengan masa lalunya, dan oleh karena itu mungkin dengan identitas pemiliknya, tetapi juga dicatat sebagai milik pengguna yang telah melakukan coinjoin.
Jika UTXO ini digabungkan dengan output yang dicampur, mereka akan kehilangan semua kerahasiaan yang diperoleh selama siklus coinjoin, terutama karena Heuristik-Kepemilikan-Input-Bersama (CIOH). Jika digabungkan dengan perubahan beracun lainnya, pengguna berisiko kehilangan kerahasiaan karena ini akan menghubungkan input yang berbeda dari siklus coinjoin. Oleh karena itu, harus ditangani dengan hati-hati. Cara mengelola UTXO beracun ini akan dijelaskan secara rinci di bagian terakhir artikel ini, dan tutorial mendatang akan membahas metode-metode ini lebih mendalam di Jaringan PlanB.

**Langkah 3: Campuran Awal**
Setelah `Tx0` selesai, UTXO yang diseimbangkan dikirim ke akun **premix** dompet kami, siap untuk diperkenalkan ke dalam siklus coinjoin pertama mereka, juga disebut "campuran awal". Jika, seperti dalam contoh kami, `Tx0` menghasilkan beberapa UTXO yang dimaksudkan untuk pencampuran, masing-masing akan diintegrasikan ke dalam coinjoin awal yang terpisah.

Di akhir campuran pertama ini, akun **premix** akan kosong, sementara koin kami, setelah membayar biaya penambangan untuk coinjoin pertama ini, akan disesuaikan tepat dengan jumlah yang ditentukan oleh kolam yang dipilih. Dalam contoh kami, UTXO awal kami sebesar `108 000 sats` akan dikurangi menjadi tepat `100 000 sats`.
![coinjoin](assets/en/8.webp)
**Langkah 4: Remix**
Setelah campuran awal, UTXO ditransfer ke akun **postmix**. Akun ini mengumpulkan UTXO yang sudah dicampur dan yang menunggu pencampuran ulang. Ketika klien Whirlpool aktif, UTXO yang berada di akun **postmix** secara otomatis tersedia untuk pencampuran ulang dan akan dipilih secara acak untuk berpartisipasi dalam siklus baru ini.

Sebagai pengingat, remix kemudian 100% gratis: tidak diperlukan biaya layanan tambahan atau biaya penambangan. Menjaga UTXO di akun **postmix** dengan demikian mempertahankan nilai mereka tetap utuh dan secara simultan meningkatkan anonset mereka. Itulah mengapa penting untuk membiarkan koin-koin ini berpartisipasi dalam beberapa siklus coinjoin. Ini tidak mengeluarkan biaya apa pun dari Anda, dan meningkatkan tingkat anonimitas mereka.
Ketika Anda memutuskan untuk menghabiskan UTXO campuran, Anda dapat melakukannya langsung dari akun **postmix** ini. Disarankan untuk menyimpan UTXO campuran di akun ini untuk mendapatkan keuntungan dari remix gratis dan untuk menghindari mereka meninggalkan sirkuit Whirlpool, yang dapat menurunkan kerahasiaan mereka.
Seperti yang akan kita lihat dalam tutorial berikut, ada juga opsi `mix to` yang menawarkan kemungkinan untuk secara otomatis mengirim koin campuran Anda ke dompet lain, seperti dompet dingin, setelah jumlah coinjoin yang ditentukan.
Setelah membahas teori, mari kita terjun ke praktik dengan tutorial menggunakan Whirlpool melalui aplikasi Android Samourai Wallet, disinkronkan dengan Whirlpool CLI dan GUI di Dojo Anda sendiri!
## Tutorial: Coinjoin Whirlpool dengan Dojo Anda Sendiri
Ada banyak opsi untuk menggunakan Whirlpool. Yang ingin saya perkenalkan di sini adalah opsi Samourai Wallet, sebuah aplikasi manajemen dompet Bitcoin sumber terbuka di Android, tetapi kali ini **dengan Dojo Anda sendiri**.

Melakukan coinjoin melalui Samourai Wallet menggunakan Dojo Anda sendiri, menurut saya, adalah strategi paling efektif untuk melakukan coinjoin di Bitcoin hingga saat ini. Pendekatan ini memerlukan beberapa investasi awal dalam hal pengaturan, tetapi sekali terpasang, ini menawarkan kemungkinan untuk mencampur dan mencampur ulang bitcoin Anda secara terus-menerus, 24 jam sehari, 7 hari seminggu, tanpa perlu menjaga aplikasi Samourai Anda aktif setiap saat. Memang, berkat operasi Whirlpool CLI pada node Bitcoin, Anda selalu siap untuk berpartisipasi dalam coinjoins. Aplikasi Samourai kemudian memberi Anda kesempatan untuk menghabiskan dana campuran Anda kapan saja, di mana saja, langsung dari smartphone Anda. Selain itu, metode ini memiliki keuntungan tidak pernah menghubungkan Anda ke server yang dikelola oleh tim Samourai, sehingga menjaga `xpub` Anda dari paparan eksternal.

Teknik ini oleh karena itu ideal bagi mereka yang mencari privasi maksimum dan siklus coinjoin berkualitas tertinggi. Namun, ini memerlukan memiliki node Bitcoin di disposisi Anda dan, seperti yang akan kita lihat nanti, memerlukan beberapa pengaturan. Oleh karena itu, lebih cocok untuk pengguna menengah hingga lanjutan. Untuk pemula, saya sarankan untuk mengenal coinjoin melalui dua tutorial lain ini, yang menunjukkan cara melakukannya dari Sparrow Wallet atau Samourai Wallet (tanpa Dojo):
- **[Tutorial coinjoin Sparrow Wallet](https://planb.network/en/tutorials/privacy/coinjoin-sparrow-wallet)**;
- **[Tutorial coinjoin Samourai Wallet (tanpa Dojo)](https://planb.network/en/tutorials/privacy/coinjoin-samourai-wallet)**.

### Memahami Pengaturan
Untuk memulai, Anda akan membutuhkan Dojo! Dojo adalah implementasi node Bitcoin berdasarkan Bitcoin Core, dikembangkan oleh tim Samourai.

Untuk menjalankan Dojo Anda sendiri, Anda memiliki opsi untuk menginstal node Dojo secara mandiri, atau memanfaatkan Dojo di atas solusi node Bitcoin "node-in-box" lainnya. Saat ini, opsi yang tersedia adalah:
- [RoninDojo](https://ronindojo.io/), yang merupakan Dojo yang ditingkatkan dengan alat tambahan, termasuk asisten instalasi dan asisten administrasi. Saya merinci prosedur untuk pengaturan dan penggunaan RoninDojo dalam tutorial lain ini: [RONINDOJO V2](https://planb.network/en/tutorials/node/ronin-dojo-v2);
- [Umbrel](https://umbrel.com/) dengan aplikasi "Samourai Server";
- [MyNode](https://mynodebtc.com/) dengan aplikasi "Dojo";
- [Nodl](https://www.nodl.eu/) dengan aplikasi "Dojo";
- [Citadel](https://runcitadel.space/) dengan aplikasi "Samourai".
![coinjoin](assets/notext/9.webp)
Dalam pengaturan kami, kami akan berinteraksi dengan tiga antarmuka yang berbeda:
- **Samourai Wallet**, yang akan menjadi host dompet Bitcoin kami yang didedikasikan untuk coinjoins. Tersedia gratis di Android, aplikasi FOSS ini memungkinkan Anda untuk mengontrol dompet mixing Anda, terutama untuk menghabiskan postmix Anda dari smartphone;
- **Whirlpool CLI** (_Command Line Interface_), yang akan beroperasi pada node yang menjadi host Dojo. Perangkat lunak ini akan memiliki akses ke kunci dompet Samourai Anda. Ini bertanggung jawab untuk berkomunikasi dengan koordinator dan mengelola coinjoins secara terus-menerus. Ini bertindak sebagai salinan dompet Samourai Anda di node Anda, siap untuk berpartisipasi dalam coinjoins kapan saja;
- **Whirlpool GUI** (_Graphical User Interface_), antarmuka pengguna grafis yang akan kami gunakan untuk memantau aktivitas Whirlpool CLI dan memulai mixing dari jarak jauh. Whirlpool GUI menyediakan representasi visual dari operasi yang dilakukan oleh Whirlpool CLI. Perangkat lunak ini harus diinstal pada komputer yang terpisah dari Dojo. Untuk pengguna Umbrel, MyNode, Nodl, dan Citadel, Whirlpool GUI adalah wajib. Namun, dengan RoninDojo, antarmuka Whirlpool GUI sudah terintegrasi ke dalam antarmuka web node Anda melalui aplikasi `Whirlpool`. Oleh karena itu, Anda tidak perlu menginstalnya pada PC terpisah.

Menurut saya, menggunakan RoninDojo merupakan solusi terbaik untuk melakukan coinjoins dengan Dojo. Karena perangkat lunak node-in-box ini dalam kemitraan langsung dengan tim Samourai, RoninDojo jauh lebih optimal untuk melakukan ini. Selain itu, integrasi Whirlpool GUI ke dalam antarmuka web sangat menyederhanakan proses pengaturan. Dalam tutorial ini, saya masih akan menjelaskan cara melakukannya dengan solusi lain yang mengintegrasikan Dojo (Umbrel, Nodl, MyNode, dan Citadel).

### Menyiapkan Dojo Anda
Untuk memulai, Anda perlu menginstal Dojo dan mendapatkan kode QR atau tautan yang akan memungkinkan Anda untuk terhubung ke sana dari jarak jauh. Tautan ini adalah alamat Tor yang berakhir dengan `.onion`. Jika Anda menggunakan RoninDojo, cukup navigasikan ke menu `Pairing` untuk mengakses informasi ini.
![coinjoin](assets/notext/10.webp)

Di bawah `Samourai Dojo`, klik tombol `Pair now`.

![coinjoin](assets/notext/11.webp)

Kode QR koneksi Anda dan tautan yang sesuai akan ditampilkan.

![coinjoin](assets/notext/12.webp)

Jika Anda menggunakan Umbrel, pergi ke App Store dan cari aplikasi `Samourai Server`. Ini terletak di tab `Bitcoin`.

![coinjoin](assets/notext/13.webp)

Instal aplikasi tersebut.

![coinjoin](assets/notext/14.webp)

Setelah membuka aplikasi, Anda kemudian akan memiliki akses ke kode QR untuk terhubung ke Dojo Anda.

![coinjoin](assets/notext/15.webp)

Jika Anda menggunakan perangkat lunak node-in-box lain seperti MyNode, Citadel, atau Nodl, prosesnya serupa dengan Umbrel. Anda perlu menginstal aplikasi Samourai atau Dojo untuk mendapatkan informasi yang diperlukan untuk terhubung ke Dojo Anda.

![coinjoin](assets/notext/16.webp)

### Menyiapkan Dompet Samourai Anda
Setelah mengambil informasi koneksi ke Dojo Anda, sekarang saatnya untuk menyiapkan dompet Anda untuk coinjoins. Ada dua skenario: jika Anda belum memiliki Samourai Wallet di smartphone Anda, prosesnya sederhana, cukup buat yang baru.
Di sisi lain, jika Anda sudah memiliki Samourai Wallet, Anda perlu menginstal ulang aplikasi untuk mengaitkannya dengan Dojo baru. Langkah ini diperlukan karena koneksi ke Dojo hanya dapat dibuat pada peluncuran pertama aplikasi. Namun, berkat file cadangan terenkripsi yang secara otomatis dihasilkan oleh Samourai di ponsel Anda, prosedur ini sederhana dan cepat.

*Jika Anda belum pernah menggunakan Samourai, Anda dapat melewati langkah awal ini dan langsung melanjutkan ke instalasi aplikasi.*

Pertama dan terutama, pastikan aplikasi Samourai Wallet Anda terbaru. Untuk melakukan ini, periksa Google Play Store atau bandingkan versi aplikasi Anda di `Settings > Other` dengan yang tersedia di situs web Samourai.

![coinjoin](assets/notext/17.webp)

Pastikan Anda memiliki frasa pemulihan dompet Samourai Anda dan bahwa itu dapat dibaca. Kemudian, lakukan tes frasa BIP39 Anda dengan menavigasi ke `Settings > Troubleshoot > Passphrase/Backup test` untuk mengonfirmasi keakuratannya.

![coinjoin](assets/notext/18.webp)
Masukkan frasa sandi Anda, kemudian verifikasi bahwa Samourai mengonfirmasi kevalidannya.
![coinjoin](assets/notext/19.webp)

Jika frasa sandi Anda tidak valid, atau jika Anda tidak memiliki frasa pemulihan Anda, sangat penting untuk segera menghentikan prosedur! **Anda berisiko kehilangan bitcoin Anda selama operasi ini.** Dalam kasus ini, disarankan untuk mentransfer dana Anda ke dompet lain dan memulai dengan Samourai wallet baru yang kosong. Langkah-langkah berikut hanya harus diikuti jika Anda yakin memiliki semua informasi cadangan yang diperlukan dan bahwa frasa sandi Anda valid.

Kemudian lanjutkan dengan membuat cadangan terenkripsi dari dompet Anda dan salin ke clipboard Anda. Untuk melakukan operasi ini, klik pada tiga titik kecil yang terletak di kanan atas layar, kemudian pilih `Export wallet backup`.

![coinjoin](assets/notext/20.webp)

**Dari langkah ini, jangan menyalin apa pun lagi ke clipboard Anda!** Sangat penting bahwa Anda menyimpan cadangan yang telah Anda salin.

Jika Anda telah mengeksekusi langkah sebelumnya dengan benar, Anda sekarang dapat dengan aman menghapus dompet Samourai Anda. Untuk melakukan ini, pergi ke: `Settings > Wallet > Secure erase the wallet`.

![coinjoin](assets/notext/21.webp)

![coinjoin](assets/notext/22.webp)

*Jika Anda belum pernah menggunakan Samourai dan menginstal aplikasi dari awal, Anda dapat melanjutkan tutorial di langkah ini.*

Aplikasi Samourai Anda sekarang direset. Buka aplikasi dan lanjutkan dengan langkah-langkah pengaturan seolah-olah Anda menggunakannya untuk pertama kali.

![coinjoin](assets/notext/23.webp)

Pada langkah selanjutnya, Anda akan mengakses halaman yang didedikasikan untuk mengonfigurasi Dojo Anda. Pilih opsi `Dojo`, kemudian masukkan informasi login Dojo Anda. Untuk melakukan ini, Anda memiliki opsi untuk memindai informasi dengan menekan `Scan QR`.

![coinjoin](assets/notext/24.webp)

*Untuk pengguna baru Samourai, kemudian akan diperlukan untuk membuat dompet dari awal. Jika Anda memerlukan bantuan, Anda dapat berkonsultasi dengan instruksi untuk menyiapkan dompet Samourai baru [dalam tutorial ini, khususnya di bagian "Creating a software wallet"](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef).*
Jika Anda sedang melanjutkan pemulihan dompet Samourai yang sudah ada, pilih `Restore existing wallet`, kemudian pilih `I have a Samourai backup file`.
![coinjoin](assets/notext/25.webp)
Biasanya, Anda seharusnya selalu memiliki file pemulihan Anda di clipboard. Kemudian klik pada `PASTE` untuk memasukkan file Anda ke lokasi yang ditentukan. Untuk mendekripsinya, akan diperlukan juga untuk memasukkan frasa sandi BIP39 dari dompet Anda di kolom yang sesuai, yang terletak tepat di bawahnya. Untuk menyelesaikan, klik pada `FINISH`.
![coinjoin](assets/notext/26.webp)

Anda kemudian akan diarahkan ke Dompet Samourai Anda yang, kali ini, akan terhubung ke Dojo Anda sendiri.

![coinjoin](assets/notext/27.webp)

### Memasang Whirlpool GUI
Sekarang saatnya untuk memasang Whirlpool GUI, antarmuka pengguna grafis yang akan memungkinkan Anda untuk mengelola siklus coinjoin dari PC biasa Anda. Bagi pengguna RoninDojo, langkah ini tidak diperlukan karena pengelolaan coinjoins dapat dilakukan langsung melalui antarmuka web di `Apps > Whirlpool`. Namun, jika Anda menggunakan solusi "node-in-box" Bitcoin lainnya, sangat penting untuk melanjutkan dengan pemasangan ini.
![coinjoin](assets/notext/28.webp)
Pergi ke komputer pribadi Anda dan unduh perangkat lunak Whirlpool dari situs web resmi Samourai Wallet, memilih versi yang sesuai dengan sistem operasi Anda.

![coinjoin](assets/notext/29.webp)

Sebelum meluncurkan Whirlpool GUI, perlu untuk memasang JAVA 8 atau versi yang lebih tinggi di mesin Anda. Untuk ini, [Anda dapat memasang OpenJDK](https://adoptium.net/).
![coinjoin](assets/notext/30.webp)
Juga diperlukan untuk memiliki Tor Daemon atau Tor Browser beroperasi di latar belakang pada komputer Anda. Pastikan untuk memulai Tor sebelum setiap sesi penggunaan Whirlpool GUI. Jika Tor belum terpasang di mesin Anda, [Anda dapat mengunduh dan memasangnya dari situs web proyek resmi](https://www.torproject.org/download/), kemudian pastikan untuk meluncurkannya di latar belakang.

![coinjoin](assets/notext/31.webp)

Setelah JDK terpasang di sistem Anda dan Tor diluncurkan di latar belakang, Anda dapat memulai Whirlpool GUI.

![coinjoin](assets/notext/32.webp)

Dari Whirlpool GUI, klik pada `Advanced: Remote CLI` untuk menghubungkan Whirlpool CLI Anda yang ada di Dojo Anda. Anda akan memerlukan alamat Tor dari Whirlpool CLI Anda.

![coinjoin](assets/notext/33.webp)

Untuk menemukan alamat Tor Anda di Umbrel dan solusi "node-in-box" lainnya, cukup mulai aplikasi Samourai Server atau Dojo (nama dapat bervariasi tergantung pada perangkat lunak yang digunakan). Alamat Tor akan langsung terlihat di halaman aplikasi.
![coinjoin](assets/notext/34.webp)
Di Whirlpool GUI, masukkan alamat Tor yang Anda peroleh sebelumnya di kolom `CLI address`. Pertahankan prefiks `http://`, tetapi jangan tambahkan port `:8899` di akhir. Tempelkan hanya alamat seperti yang diberikan kepada Anda.
![coinjoin](assets/notext/35.webp)
Di bidang Tor Proxy, masukkan `socks5://127.0.0.1:9050` jika Anda menggunakan Tor Daemon, atau `socks5://127.0.0.1:9150` jika itu adalah Tor Browser. Ketika Anda pertama kali terhubung ke Whirlpool CLI melalui Whirlpool GUI, Anda bisa meninggalkan kolom kunci API kosong. Jika ini bukan koneksi pertama Anda, silakan masukkan kunci API Anda di ruang yang disediakan. Kunci ini dapat ditemukan di halaman yang sama dengan alamat Tor Anda.
![coinjoin](assets/notext/36.webp)

Setelah Anda mengisi semuanya, klik tombol `Connect`. Harap tunggu, koneksi mungkin membutuhkan beberapa menit.

![coinjoin](assets/notext/37.webp)

### Menghubungkan Dompet Samourai Anda dengan Whirlpool GUI
*Untuk pengguna RoninDojo, Anda dapat melanjutkan tutorial di sini.*

Kami akan sekarang menghubungkan dompet Samourai yang telah kita konfigurasi sebelumnya dengan perangkat lunak Whirlpool GUI, atau langsung dengan RoninDojo bagi mereka yang menggunakan perangkat lunak ini. Baik Anda menggunakan Whirlpool GUI atau RoninDojo, Anda akan diminta untuk menempelkan atau memindai informasi penghubung dari dompet Samourai Anda.

![coinjoin](assets/notext/38.webp)

Untuk menemukan informasi ini, pergi ke pengaturan dompet Anda.

![coinjoin](assets/notext/39.webp)

Klik pada `Transaksi`, kemudian pada `Pair to Whirlpool GUI`.

![coinjoin](assets/notext/40.webp)

Samourai kemudian akan memberikan Anda informasi yang diperlukan untuk membangun koneksi. Hati-hati, data ini sensitif! Anda dapat mentransfernya ke PC Anda baik dengan menyalinnya langsung atau dengan memindai kode QR yang ditampilkan, menggunakan webcam komputer Anda setelah mengklik simbol kode QR.

![coinjoin](assets/notext/41.webp)

Setelah melakukan operasi ini, di Whirlpool GUI, pilih `Initialize GUI`. Harap tunggu, karena langkah ini mungkin membutuhkan waktu sebentar.

![coinjoin](assets/notext/42.webp)

Baik Anda menggunakan Whirlpool GUI atau RoninDojo, Anda akan diminta untuk memasukkan frasa sandi dari dompet Samourai Anda. Masukkan di kolom yang disediakan, kemudian tekan tombol `Login` untuk melanjutkan.

![coinjoin](assets/notext/43.webp)

Anda kemudian akan tiba di halaman utama Whirlpool CLI

![coinjoin](assets/notext/44.webp)

### Memulai coinjoins dari Whirlpool GUI
*Untuk pengguna RoninDojo, proses yang harus diikuti identik. Antarmuka aplikasi Whirlpool yang terintegrasi ke dalam RoninDojo menawarkan opsi dan fungsionalitas yang sama seperti perangkat lunak Whirlpool GUI di desktop. Oleh karena itu, Anda dapat mengikuti instruksi ini dengan cara yang sama.*
Sekarang setelah semuanya siap, Anda siap untuk mulai mencampur bitcoin Anda. Untuk melakukan ini, transfer bitcoin yang ingin Anda campur ke akun **Deposit** dari Dompet Samourai Anda. Operasi ini dapat dilakukan baik langsung melalui aplikasi Dompet Samourai atau di Whirlpool GUI. Dari halaman utama, klik tombol `+ Deposit` yang terletak di kiri atas.

![coinjoin](assets/notext/45.webp)
Whirlpool GUI akan menghasilkan alamat penerimaan. Ini juga akan menampilkan jumlah minimum yang diperlukan untuk berpartisipasi dalam setiap kolam coinjoin. Jumlah ini bervariasi tergantung pada pasar biaya. Disarankan untuk menyetorkan jumlah yang sedikit lebih tinggi dari yang diperlukan, karena jika biaya penambangan tidak menurun, UTXO Anda mungkin tidak akan diterima di kolam yang diinginkan. Oleh karena itu, kirimkan bitcoin Anda ke alamat yang disediakan. Untuk mendapatkan alamat baru, cukup klik tombol `Perbarui alamat`.

![coinjoin](assets/notext/46.webp)

Setelah deposit dikonfirmasi, Anda akan dapat melihatnya muncul di akun **Deposit** pada Whirlpool GUI.

![coinjoin](assets/notext/47.webp)

Untuk memulai siklus coinjoin, pilih UTXO yang ingin Anda campur dan tekan tombol `Premix`. Berhati-hatilah: jika Anda memilih beberapa UTXO yang berbeda pada saat yang sama, mereka akan digabungkan selama transaksi persiapan `TX0`. Penggabungan ini dapat menyebabkan penurunan privasi, terutama jika UTXO berasal dari sumber yang berbeda, karena Heuristik Kepemilikan Input Bersama (CIOH).

![coinjoin](assets/notext/48.webp)

Halaman konfigurasi Whirlpool terbuka. Anda dapat memilih kolam yang ingin Anda masuki. Juga pilih biaya penambangan yang didedikasikan untuk `TX0` dan coinjoin pertama. Di bagian bawah halaman ini, ringkasan akan menampilkan jumlah perubahan doxxic serta jumlah dan nomor UTXO yang akan diseimbangkan dan dimasukkan dalam siklus coinjoin. Jika Anda puas dengan konfigurasi ini, tekan tombol `Premix` untuk memulai siklus coinjoin.
![coinjoin](assets/notext/49.webp)

Setelah `TX0` dibuat, Anda akan dapat melihat UTXO Anda yang diseimbangkan di akun **Premix**, menunggu konfirmasi. Untuk memungkinkan koin Anda dicampur ulang secara otomatis 24 jam sehari, 7 hari seminggu, saya sarankan mengaktifkan opsi `Campur otomatis premix & postmix`. Anda akan menemukan fitur ini di tab `Konfigurasi`, yang terletak di sebelah kiri jendela Whirlpool GUI Anda.
![coinjoin](assets/notext/50.webp)
Setelah memulai coinjoin, Anda dapat keluar dari Whirlpool GUI serta Samourai Wallet. Hanya node Anda yang perlu tetap terhubung untuk dapat berpartisipasi dalam coinjoin terus menerus. Namun, disarankan untuk secara berkala memeriksa kemajuan siklus coinjoin Anda. Jika Anda memperhatikan bahwa UTXO Anda tidak lagi dipilih untuk coinjoin dalam beberapa waktu, ini dapat menunjukkan adanya bug. Dalam kasus ini, buka Whirlpool CLI dan pilih `Mulai` untuk memulai kembali ketersediaan Anda untuk coinjoin.

![coinjoin](assets/notext/51.webp)

UTXO Anda yang telah dicampur terlihat dari akun **Postmix** pada Whirlpool GUI. Selain itu, Anda memiliki opsi untuk melihat dan menghabiskannya langsung melalui antarmuka Whirlpool di Samourai Wallet Anda. Untuk mengakses menu ini, klik pada `+` biru di bagian bawah layar Anda, lalu pilih `Whirlpool`.

![coinjoin](assets/notext/52.webp)

Akun Whirlpool mudah dikenali di Samourai Wallet dengan warna birunya. Ini memungkinkan Anda untuk menghabiskan UTXO Anda yang telah dicampur dari mana saja dan kapan saja, langsung dari smartphone Anda.

![coinjoin](assets/notext/53.webp)
Untuk melacak coinjoin otomatis Anda, saya juga merekomendasikan untuk mengatur dompet hanya-pantau melalui aplikasi Sentinel. Tambahkan ZPUB dari akun **Postmix** Anda dan pantau progres siklus coinjoin Anda secara real-time. Jika Anda ingin memahami cara menggunakan Sentinel, saya merekomendasikan untuk berkonsultasi dengan tutorial lain ini di PlanB Network: [**SENTINEL WATCH-ONLY**](https://planb.network/tutorials/wallet/mobile/sentinel-9876f960-e964-4d20-8a6e-36231de1f4d9).