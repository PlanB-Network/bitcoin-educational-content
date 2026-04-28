---
name: Pengantar ke Bitcoin mining
goal: Memahami Bitcoin mining dan proof-of-work dari awal
objectives: 


  - Memahami proof-of-work dan perannya dalam Bitcoin.
  - Menganalisis mekanisme penyesuaian kesulitan.
  - Ketahui apa arti istilah teknis yang terkait dengan mining.
  - Jelaskan langkah-langkah yang terlibat dalam membangun blok Bitcoin dan komponennya.
  - Mengidentifikasi perkembangan utama dalam industri mining.


---

# Temukan dasar-dasar Bitcoin mining



Untuk memahami proof of work berarti memahami cara kerja Bitcoin. Tanpa penemuan ini dan penggunaannya yang cerdik, Bitcoin tidak akan pernah ada. Kursus ini memberi Anda semua teori mining yang Anda butuhkan untuk perjalanan bitcoin Anda.



MIN 101 terutama ditujukan untuk pemula, karena kursus ini menjelaskan semua konsep secara tepat dari awal. Namun, jika Anda sudah memiliki pengetahuan tingkat menengah, kursus ini akan memungkinkan Anda untuk mengkonsolidasikan pemahaman Anda, mengoreksi beberapa perkiraan intuisi, dan mengeksplorasi detail yang sering hilang dari penjelasan umum.



Pada akhir kursus ini, Anda akan dapat menjelaskan cara kerja proof-of-work dengan cara yang sederhana dan teliti. MIN 101 juga merupakan pengantar yang ideal untuk semua kursus lanjutan lainnya yang dikhususkan untuk Bitcoin mining pada Plan ₿ Academy, baik secara teori maupun praktik.



+++


# Pendahuluan


<partId>041ff0fa-53c3-4d55-9888-d7840de283e9</partId>



## Gambaran umum kursus


<chapterId>a82d49dc-d68a-4e3f-985e-bcef6643677e</chapterId>



Selamat datang di kursus MIN 101, di mana Anda akan menemukan konsep teoretis dasar mining dan Proof-of-Work dalam sistem Bitcoin. Kursus ini adalah langkah pertama dalam perjalanan bitcoiner Anda untuk memahami cara kerja mining. Setelah Anda menyelesaikannya, Anda akan dapat melanjutkan ke kursus teori yang lebih lanjut, atau langsung praktik dan menjadi penambang bitcoin sendiri!



Dalam kursus MIN 101 ini, kita tidak akan membahas kembali konsep dasar Bitcoin, karena kita akan langsung masuk ke inti permasalahan: mining. Jika Anda belum pernah mendengar tentang Bitcoin, atau jika dasar-dasarnya masih sedikit tidak jelas bagi Anda, saya sangat menyarankan agar Anda memulai dengan kursus pengantar BTC 101. Setelah Anda menguasai dasar-dasar ini, Anda akan dapat menangani MIN 101 dengan percaya diri:



https://planb.academy/courses/2b7dc507-81e3-4b70-88e6-41ed44239966


### Bagian 1 - Pendahuluan



Kita akan memulai kursus ini dengan bab pertama yang opsional, di mana saya menawarkan penjelasan yang sangat sederhana tentang mining, untuk memberi Anda gambaran mental yang jelas sebelum masuk ke mekanisme teknis.



Tujuannya di sini bukan untuk memberikan Anda semua detail teknis (mereka akan datang nanti dalam kursus), tetapi untuk memberi Anda benang merah. Setelah kerangka kerja ini ada, setiap konsep yang lebih canggih yang diperkenalkan setelahnya akan secara alami masuk ke dalam struktur ini.



### Bagian 2 - Cara kerja proof of work



Setelah pendahuluan, Bagian 2 merupakan fondasi teknis dari program pelatihan ini. Tujuannya adalah untuk menjelaskan, langkah demi langkah, bagaimana Bitcoin menghasilkan blok yang valid. Kita akan mulai dengan menemukan struktur sebuah blok, sebelum masuk ke mekanisme proof-of-work: peran target, nonce, dan fungsi hash. Terakhir, kita akan melihat bagaimana Bitcoin dapat mempertahankan tingkat produksi blok yang stabil meskipun terdapat variasi dalam kekuatan hash, berkat mekanisme penyesuaian tingkat kesulitan. Di akhir bagian ini, Anda akan memiliki pemahaman yang lengkap mengenai prinsip-prinsip dasar dari Bitcoin dan proof-of-work.



### Bagian 3 - Sistem insentif Bitcoin mining



Pada bagian ketiga, kita akan melihat mengapa penambang didorong untuk berpartisipasi secara jujur dalam mining. Kami akan merinci prinsip block reward, komposisi dan metode penghitungannya, evolusinya dari waktu ke waktu melalui halving, dan peran spesifik dari transaksi coinbase.



### Bagian 4 - Industri Bitcoin mining



Bagian keempat menempatkan mining kembali ke dalam realitas operasionalnya. Bagian ini menelusuri evolusi mesin mining, dari awal Bitcoin hingga ASIC modern, untuk memahami kendala perangkat keras saat ini. Kami juga melihat dasar-dasar pool mining, untuk memahami bagaimana penambang dapat mengurangi varians pendapatan mereka.



### Bagian 5 - Bagian akhir



Di bagian akhir kursus, Anda dapat menguji pengetahuan Anda tentang mining dengan mengambil ijazah.



Oleh karena itu, tujuan dari kursus MIN 101 ini adalah agar Anda dapat pulang dengan pemahaman yang jelas, terstruktur, dan tahan lama tentang Bitcoin mining, baik secara teknis maupun ekonomis.



Siap untuk menemukan Bitcoin mining? Mari kita mulai!




## Bitcoin mining menjadi mudah


<chapterId>278577a6-98bb-4659-86c7-f6c4f6d5fa3e</chapterId>



Sebelum beralih ke penjelasan yang lebih rinci dan lebih teknis mengenai Bitcoin [mining](https://planb.academy/resources/glossary/mining), saya ingin memberi Anda gambaran umum mengenai prinsipnya, yang sengaja dibuat sederhana dan skematis. Jika Anda sudah memiliki pengetahuan dasar, Anda bisa langsung masuk ke inti permasalahan dalam bab berikutnya, setelah menjawab pertanyaan kuis. Bab ini ditujukan terutama untuk pemula, untuk memberi Anda permulaan yang baik.



Bayangkan Bitcoin sebagai sebuah buku catatan publik yang besar, yang dapat digunakan oleh semua orang, di mana kita menuliskan siapa yang mengirim bitcoin kepada siapa. Buku catatan ini disebut [blockchain](https://planb.academy/resources/glossary/blockchain). Blockchain tidak bisa dipegang oleh satu orang saja, karena ia harus dipercaya. Sebaliknya, Bitcoin bekerja secara kolektif: ribuan komputer memverifikasi dan memelihara versi yang sama dari buku catatan ini.



![Image](assets/fr/049.webp)



Dalam Bitcoin, ketika Anda melakukan pembayaran, Anda membuat [transaksi](https://planb.academy/resources/glossary/transaction-tx). Transaksi ini tidak langsung ditambahkan ke buku catatan. Transaksi ini terlebih dahulu dikirim ke jaringan, kemudian menunggu untuk diintegrasikan ke dalam paket transaksi berikutnya. Paket ini disebut [blok](https://planb.academy/resources/glossary/block).



![Image](assets/fr/050.webp)



Blok adalah sekumpulan transaksi yang dikelompokkan bersama. Ketika sebuah blok sudah siap, tidak cukup hanya dengan mempublikasikannya. Anda harus membuktikan kepada jaringan bahwa blok tersebut layak untuk ditambahkan ke dalam pool. Di sinilah mining berperan.



Mining adalah pekerjaan memvalidasi sebuah blok dengan mengkonsumsi energi. Pelaku yang disebut [penambang](https://planb.academy/resources/glossary/miner) menggunakan komputer khusus. Mesin-mesin ini mengkonsumsi listrik untuk melakukan sejumlah besar pengujian, dalam satu lingkaran, sampai mereka menemukan bukti yang diterima oleh jaringan. Ketika penambang menemukan bukti ini, maka bloknya dianggap valid.



Setelah blok divalidasi, blok tersebut disiarkan ke jaringan. [Node-node](https://planb.academy/resources/glossary/node) lain dengan cepat memeriksa apakah blok tersebut sesuai dengan aturan, kemudian menambahkannya ke urutan blok sebelumnya. Inilah sebabnya mengapa ini disebut "blockchain": setiap blok baru muncul setelah blok yang lain, secara berurutan, dan rantai ini tumbuh sedikit demi sedikit.



![Image](assets/fr/051.webp)



Singkatnya, transaksi pertama kali dibuat. Kemudian, mereka dikelompokkan bersama dalam sebuah blok. Kemudian, penambang memvalidasi blok ini dengan mengonsumsi listrik. Terakhir, blok ini ditambahkan ke blockchain, dan transaksi yang ada di dalamnya menjadi [terkonfirmasi](https://planb.academy/resources/glossary/confirmation).



Jika para penambang menggunakan listrik, itu bukan karena mereka sukarelawan. Mereka melakukannya karena ada imbalannya. Ketika seorang penambang memvalidasi sebuah blok, ia menerima dua jenis pendapatan. Di satu sisi, ia menerima bitcoin yang baru dibuat. Di sisi lain, ia mengumpulkan [biaya](https://planb.academy/resources/glossary/transaction-fees) yang dibayarkan oleh pengguna untuk transaksi yang termasuk dalam blok tersebut. Dengan kata lain, penambang mendapatkan kompensasi baik melalui penerbitan moneter yang terprogram, maupun biaya transaksi yang ditentukan oleh pasar.



Pada tahap ini, Anda sengaja diberikan pandangan yang sangat sederhana tentang mining. Ini belum menjelaskan bagaimana blok tersebut dibangun secara detail, atau bagaimana tepatnya cara kerja para penambang yang mencari proof mining, atau bagaimana Bitcoin mempertahankan kecepatan yang stabil, atau bagaimana cara menghitung reward dengan tepat, atau bagaimana cara mengklaimnya. Tidak apa-apa, hanya itu yang akan kita lihat di sisa kursus MIN 101 ini!



Tujuan dari bab ini adalah untuk memberikan Anda struktur mental yang jelas: transaksi → blok → mining → blockchain → reward. Ingatlah rantai ide ini dalam pikiran Anda. Dalam sisa kursus ini, setiap bab akan menambahkan lapisan detail teknis pada salah satu elemen ini, sampai Anda tidak hanya memahami apa yang sedang terjadi, tetapi juga bagaimana dan mengapa ia bekerja dengan andal, dalam skala besar, tanpa bos, dan tanpa perlu kepercayaan.



# Bagaimana proof of work bekerja


<partId>e917e8e3-37f2-46fb-91b2-6a5ce6f0f5c3</partId>



## Jalur transaksi Bitcoin


<chapterId>3b7a3502-4814-4554-8de1-86ac961a2958</chapterId>



Untuk memahami apa itu Bitcoin mining, pertama-tama kita harus mengikuti alur transaksi Bitcoin pada umumnya. Ini akan menunjukkan kepada Anda di mana tepatnya blok ini berperan, dan mengapa blok ini berada di jantung sistem. Itulah yang saya ingin Anda temukan dalam bab pertama ini.



Dalam Bitcoin, sebuah transaksi adalah sebuah struktur data yang memindahkan kepemilikan bitcoin dari satu pengguna ke pengguna lainnya. Secara konkret, struktur ini mengkonsumsi '[output](https://planb.academy/resources/glossary/output)' dari transaksi-transaksi sebelumnya (yang disebut [UTXO](https://planb.academy/resources/glossary/utxo)), yang disebut sebagai '[input](https://planb.academy/resources/glossary/input)', dan kemudian menciptakan 'output' baru yang menentukan kepada siapa bitcoin tersebut sekarang menjadi milik dan dalam kondisi apa bitcoin tersebut dapat dibelanjakan nantinya.



![Image](assets/fr/001.webp)



Poin penting tentang Bitcoin adalah otorisasi untuk membelanjakannya. Bitcoin tidak berada di dalam rekening, seperti uang Anda di bank, tetapi dikunci oleh ketentuan pembelanjaan. Ketika [wallet](https://planb.academy/resources/glossary/wallet) ingin menggunakan UTXO sebagai input, wallet harus memberikan bukti kriptografi bahwa ia memiliki hak untuk membukanya. Bukti ini sering kali berbentuk [tanda tangan digital](https://planb.academy/resources/glossary/digital-signature) generated dari [private key](https://planb.academy/resources/glossary/private-key). Itulah mengapa para pengguna bitcoin bersikeras untuk mengamankan kunci pribadi Anda: kunci inilah yang membuka akses ke bitcoin Anda dan, akibatnya, memungkinkan Anda untuk membelanjakannya.



![Image](assets/fr/002.webp)



Tanda tangan digital dalam Bitcoin memainkan dua peran penting:




- Otorisasi pengeluaran: ini membuktikan bahwa pengguna memiliki kunci pribadi yang diharapkan oleh kondisi pengeluaran UTXO;
- Perlindungan integritas: menghubungkan otorisasi dengan detail transaksi yang tepat (penerima, jumlah, biaya, dll.). Jika seseorang mengubah transaksi setelahnya, tanda tangan tidak akan berlaku lagi.



Setelah transaksi dibuat dengan benar dan ditandatangani oleh Bitcoin wallet pengguna, transaksi tersebut harus disiarkan di jaringan Bitcoin.



### Peran node Bitcoin dalam distribusi



Bitcoin adalah jaringan [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p): tidak ada server pusat yang menerima dan memproses semua transaksi. Peran ini dimainkan secara kolektif oleh node. Node Bitcoin adalah sebuah perangkat lunak (contohnya [Bitcoin Core](https://planb.academy/resources/glossary/bitcoin-core)) yang terhubung ke node lain dalam jaringan Bitcoin, yang misi utamanya adalah memverifikasi, menyimpan, dan meneruskan transaksi dan blok.



Ketika Anda mengirim transaksi dari wallet, wallet akan meneruskannya ke sebuah node (milik Anda, atau milik layanan). Node ini pertama-tama akan memeriksa apakah transaksi tersebut sesuai dengan berbagai aturan, seperti:




- tanda tangan yang sah;
- masukannya mengacu pada UTXO yang ada (yaitu bitcoin yang ada);
- gW-71 ini belum pernah digunakan di tempat lain;
- jumlah output kurang dari atau sama dengan jumlah input (bitcoin tidak diciptakan dari ketiadaan);
- dll.



Jika transaksi lolos dari semua pemeriksaan ini, node akan menyebarkannya ke node lain dalam jaringan yang terhubung dengannya. Mereka kemudian memeriksanya dan meneruskannya, dan seterusnya. Dalam hitungan detik, transaksi disebarkan dan diketahui oleh seluruh, atau setidaknya sebagian besar, jaringan Bitcoin.



![Image](assets/fr/003.webp)



### Mempool: ruang tunggu transaksi



Antara saat sebuah transaksi disiarkan dan saat transaksi tersebut dikonfirmasi dalam sebuah blok, transaksi tersebut harus menunggu. Area tunggu ini disebut dengan [mempool](https://planb.academy/resources/glossary/mempool) (kontraksi dari `memory` dan `pool`). Mempool adalah tempat penyimpanan sementara untuk transaksi yang valid, namun belum dikonfirmasi.



Poin penting: tidak ada yang namanya mempool tunggal, yang ada hanyalah mempool. Setiap node memelihara mempoolnya sendiri, dengan batasan lokalnya sendiri. Ini berarti bahwa pada saat tertentu, dua node mungkin memiliki isi mempool yang sedikit berbeda (tergantung pada apa yang mereka terima, apa yang mereka tolak, atau apa yang mereka bersihkan).



![Image](assets/fr/004.webp)



Pada tahap ini, jaringan mengetahui tentang transaksi tersebut, telah memverifikasinya dan menyimpannya di memori sampai transaksi tersebut dikonfirmasi. Akan tetapi, konfirmasi dari transaksi ini hanya akan terjadi ketika penambang memasukkannya ke dalam sebuah blok, dan blok ini diterima oleh jaringan.



### Blockchain: register stempel waktu publik



Karena bitcoin merupakan mata uang yang tidak berwujud, maka ia harus mengatasi satu masalah: mencegah [pembelanjaan ganda](https://planb.academy/resources/glossary/double-spending-attack) tanpa adanya otoritas pusat. Jika dua transaksi mencoba untuk membelanjakan UTXO yang sama, semua orang harus dapat menyatu pada satu keadaan yang koheren. Satoshi Nakamoto meringkas masalah ini dengan kalimat yang terkenal ini:



> Satu-satunya cara untuk memastikan tidak adanya transaksi adalah dengan mengetahui semua transaksi.

Dengan kata lain, untuk mengetahui bahwa sebuah bitcoin belum dibelanjakan, Anda membutuhkan catatan umum tentang pengeluaran sebelumnya.



Inilah peran blockchain: sebuah daftar publik yang berisi riwayat transaksi. Namun, alih-alih menulis setiap transaksi saat terjadi, Bitcoin mengelompokkannya ke dalam blok-blok. Setiap blok bertindak sebagai halaman riwayat, dan dengan demikian sistem ini berfungsi seperti sebuah server stempel waktu: sistem ini memesan transaksi dari waktu ke waktu dengan cara yang dapat diverifikasi.



Register ini tidak dapat ditulis ulang, berkat prinsip sederhana: setiap blok menyertakan sidik jari kriptografi ([hash](https://planb.academy/resources/glossary/hash-function)) dari blok sebelumnya. Dengan demikian, blok-blok saling terkait: jika Anda memodifikasi sebuah blok dari masa lalu, maka hash-nya akan berubah, yang memutus hubungan dengan blok berikutnya, yang memutus hubungan dengan blok setelahnya, dan seterusnya. Rantai ketergantungan inilah yang memberi nama "*blockchain*".



![Image](assets/fr/005.webp)



Setelah kita memahami prinsip-prinsip dasar Bitcoin ini, kita dapat menjelaskan tujuan penambang dalam istilah yang lebih konkret: membangun blok baru yang memperpanjang rantai yang sudah ada, dengan menuliskan transaksi yang tertunda, dan kemudian mencoba membuatnya valid (ini adalah "[proof of work](https://planb.academy/resources/glossary/proof-of-work)" yang akan kita pelajari di bab selanjutnya). Namun pertama-tama, mari kita pelajari bersama di bab selanjutnya bagaimana sebuah kandidat blok dibangun.



## Membangun blok Bitcoin


<chapterId>2b5cd04b-d400-4865-b0a0-e70fa7e67c17</chapterId>



Sekarang Anda telah memahami cara kerja transaksi Bitcoin dan peran blockchain. Namun, sebelum kita melihat lebih detail mengenai cara kerja proof-of-work, masih ada satu langkah penting yang harus dilakukan oleh penambang: pembangunan [blok kandidat](https://planb.academy/resources/glossary/candidate-block). Mari kita cari tahu bersama apa itu kandidat blok dan bagaimana cara penambang membangunnya, sebelum memulai pencarian bukti yang valid.



### Blok kandidat



Para Miner harus membangun blok mereka sendiri sebelum mencoba menambangnya. Setiap penambang, pada gilirannya, membangun apa yang dikenal sebagai blok kandidat dari transaksi yang tertunda di mempool-nya. Oleh karena itu, membangun blok kandidat terdiri dari:




- memilih transaksi mana yang akan disertakan;
- mengatur transaksi-transaksi ini dengan cara yang sesuai dengan aturan Bitcoin;
- menghasilkan metadata blok, yang disimpan dalam [headernya](https://planb.academy/resources/glossary/block-header).



Pilihan transaksi mengikuti logika ekonomi yang sederhana: sebuah blok memiliki kapasitas yang dibatasi oleh protokol Bitcoin, sehingga penambang berusaha untuk memaksimalkan apa yang dia dapatkan dari ruang ini. Dia memilih sebagai prioritas transaksi yang menawarkan biaya tertinggi relatif terhadap ruang yang mereka tempati di blok (ini dikenal sebagai "tingkat biaya", yang dinyatakan dalam sats/vB). Rincian biaya akan dibahas nanti; ingatlah ide pengurutan berdasarkan efisiensi ruang.



Oleh karena itu, blok Bitcoin terdiri dari dua bagian utama:




- daftar transaksi;
- tajuk blok, yang berfungsi sebagai kartu identitas blok.



![Image](assets/fr/006.webp)



Header sangat penting, karena digunakan sebagai dasar untuk proof-of-work: dalam Bitcoin, Anda tidak menambang seluruh blok secara langsung; Anda hanya menambang header dari sebuah blok, yang meringkas informasi yang diperlukan untuk menghubungkan blok ke rantai dan mengirimkan isinya. Untuk memungkinkan header mewakili semua transaksi, Bitcoin menggunakan alat kriptografi: [pohon Merkle](https://planb.academy/resources/glossary/merkle-tree).



### Pohon Merkle: meringkas sekumpulan besar transaksi



Mencantumkan semua transaksi dalam header tidak mungkin dilakukan: sebuah blok dapat berisi ribuan transaksi, sementara header memiliki ukuran yang tetap (80 byte). Oleh karena itu, solusinya adalah dengan menghitung hash unik yang bergantung pada semua transaksi dalam blok: inilah [akar Merkle](https://planb.academy/resources/glossary/merkle-root).



Prinsipnya adalah sebagai berikut:




- sidik jari kriptografi (hash) dari setiap transaksi dihitung;
- hash ini dipasangkan, digabungkan, dan kemudian di-hash lagi untuk membentuk lapisan hash baru;
- proses ini diulangi sampai satu hash terakhir diperoleh: akar Merkle.



![Image](assets/fr/007.webp)



Jadi, jika satu transaksi berubah, bahkan dengan satu bit, hasilnya adalah modifikasi sidik jarinya, yang menyebar ke akar Merkle. Akar ini termasuk dalam header blok. Jadi, memodifikasi transaksi sebelumnya berarti memodifikasi header blok di mana transaksi tersebut disertakan, dan oleh karena itu, jejak blok, dan kemudian tautan dengan blok berikutnya.



Sejak [SegWit](https://planb.academy/resources/glossary/segwit), kami telah memisahkan tanda tangan dari yang lain. Jadi, pada kenyataannya, ada 2 pohon Merkle yang bersarang di dalam setiap blok. Pemisahan ini memiliki konsekuensi pada cara kita menghitung ukuran blok dan komitmen kriptografi tertentu, tetapi ide dasarnya tetap sama: header harus melakukan komitmen, dengan cara yang ringkas, semua isi blok.



### Tajuk blok



Header blok memiliki panjang 80 byte dan berisi tepat 6 field. Keenam elemen inilah yang akan di-hash ketika mencari proof of work (lihat bab berikutnya):





- Versi (`versi`): Ini menunjukkan aturan atau sinyal pembaruan yang dipatuhi oleh blok tersebut. Ini berfungsi sebagai mekanisme untuk menjaga kompatibilitas dan evolusi protokol.




- Hash blok sebelumnya (`previousblockhash`): Ini adalah hash dari header blok sebelumnya. Inilah yang menghubungkan blok-blok tersebut. Tanpa bidang ini, kita akan memiliki blok-blok yang terpisah. Dengan menyertakan hash dari header blok sebelumnya, kita mendapatkan sebuah rantai, di mana setiap blok baru dibangun di atas blok sebelumnya.





- Akar Merkle (`merkleroot`): Ini adalah sidik jari dari semua transaksi dalam blok (melalui pohon Merkle). Ini menghubungkan header ke konten: jika penambang mengubah pilihan atau urutan transaksi, root akan berubah.





- [Cap waktu](https://planb.academy/resources/glossary/timestamp): Ini merupakan cap waktu (waktu Unix) yang dipilih oleh penambang (dengan batasan validitas), yang harus mengindikasikan kapan blok tersebut ditambang. Cap waktu tidak harus akurat sampai ke detik, tetapi harus memenuhi syarat tertentu agar tetap dapat diterima oleh jaringan.





- [Target tingkat kesulitan](https://planb.academy/resources/glossary/difficulty-target) yang dikodekan (`nbits`): Bidang ini mengkodekan target tingkat kesulitan saat ini. Kita akan membahas lebih detail dalam bab tentang tingkat kesulitan, tetapi ingatlah bahwa parameter ini adalah bagian dari header.





- [Nonce](https://planb.academy/resources/glossary/nonce) (`nonce`): Ini adalah nilai yang dapat dimodifikasi oleh penambang secara bebas. Ini berfungsi sebagai variabel yang dapat disesuaikan selama proof-of-work. Saya akan menjelaskan perannya secara lebih detail pada bab selanjutnya, tetapi penting untuk memahami bahwa nonce merupakan bagian dari header blok dan didesain untuk mengizinkan percobaan yang berurutan.



Untuk membuatnya lebih mudah divisualisasikan, berikut ini contoh header blok dalam format heksadesimal (80 byte):



```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```



Berikut ini adalah perincian bidang demi bidang:



```text
version: 00e0ff3f
previousblockhash: 5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
merkleroot: 206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
time: bcb13a64
nbits: b2e00517
nonce: 43f09a40
```



Header blok kandidat ini, yang dibuat oleh penambang, menjadi dasar pekerjaan mereka. Ketika mencari sebuah proof-of-work yang valid, bukan seluruh daftar transaksi yang langsung di-hash dalam sebuah lingkaran, melainkan blok 80-byte ini, yang berisi semua yang diperlukan untuk menghubungkan blok ke masa lalu dan mengomit isinya, dan juga menyertakan parameter yang diperlukan untuk mekanisme mining, yang akan kita bahas pada bab selanjutnya.



## Hash, target, dan nonce


<chapterId>d054323b-16bd-4556-bac5-4878654e59a3</chapterId>



Pada bab-bab sebelumnya, Anda telah mengikuti alur transaksi Bitcoin: dibuat dan ditandatangani oleh wallet, diteruskan oleh node, disimpan di mempool, kemudian dikonfirmasi ketika penambang memasukkannya ke dalam blok yang diterima oleh jaringan. Tetapi kita belum melihat bagaimana seorang penambang dapat menambahkan bloknya ke dalam blockchain. Apa proses di balik mining?



Memahami proses mining cukup mudah. Proses ini bermuara pada 3 konsep yang berjalan beriringan: fungsi hash, nilai target, dan variabel yang dapat dimodifikasi oleh penambang. Mari kita lihat bagaimana cara kerjanya.



### Fungsi hash



Fungsi hash adalah alat yang mengambil pesan sebagai input dan menghasilkan output dengan ukuran tetap, yang disebut "*sidik jari*" atau "*hash*".



![Image](assets/fr/010.webp)



Fungsi hash menarik dalam sistem komputer karena memiliki sifat-sifat tertentu:





- Jika Anda mengubah satu bit dari input, hash output yang dihasilkan akan berubah sepenuhnya dan tidak dapat diprediksi;



![Image](assets/fr/011.webp)





- Tidak mungkin beralih dari output ke input: fungsi ini tidak dapat dipulihkan;



![Image](assets/fr/012.webp)





- Tidak mungkin menemukan dua pesan berbeda yang memberikan hash yang sama persis.



![Image](assets/fr/013.webp)



Fungsi hash yang digunakan dalam Bitcoin untuk mining adalah `SHA256`, diterapkan dua kali secara berurutan. Ini dikenal sebagai [SHA256](https://planb.academy/resources/glossary/sha256) ganda, atau `SHA256d`. Hash ganda inilah yang menghasilkan sidik jari blok.



```text
hash = SHA256(SHA256(message))
```



Dalam kasus kita, `pesan` sebenarnya berhubungan dengan header blok, yang Anda lihat di bab sebelumnya. Sebagai pengingat, header adalah struktur kecil yang meringkas semua yang ada di dalam blok.



![Image](assets/fr/014.webp)



### Bukti kerja: menemukan hash yang lebih kecil dari target



Proof-of-Work sering digambarkan sebagai pemecahan masalah yang kompleks. Pada kenyataannya, ini bukanlah sebuah masalah melainkan sebuah pencarian coba-coba: penambang harus menemukan versi header yang hash-nya (setelah melewati fungsi hash `SHA256d`) sesuai dengan syarat sederhana: hash tersebut harus lebih kecil dari sebuah target tertentu.



Kondisi ini dirumuskan sebagai berikut:




- hash header blok dihitung menggunakan fungsi hash;
- kami menafsirkan hash ini sebagai angka;
- agar blok tersebut valid, angka ini harus kurang dari atau sama dengan nilai yang disebut "*target kesulitan*".



Dengan kata lain, sebuah blok valid jika:



```text
SHA256d(block_header) <= target
```



![Image](assets/fr/015.webp)



Targetnya adalah angka 256-bit. Karena hash yang dihasilkan oleh `SHA256d` juga 256 bit, keduanya dapat dibandingkan sebagai dua angka. Semakin rendah target, semakin sulit kondisinya, karena ada lebih sedikit hasil yang mungkin di bawah ambang batas ini. Sebaliknya, semakin tinggi target, semakin mudah kondisi tersebut dipenuhi, dan semakin mudah untuk menambang sebuah blok. Kita akan melihat lebih dekat bagaimana target ini ditentukan pada bab-bab selanjutnya.



Dalam sistem ini, fungsi hash sangat menarik. Ingatlah bahwa sangat mudah untuk menghitung output dari input, tetapi tidak mungkin untuk menemukan input dengan hanya mengetahui output fungsi. Dalam mining, penambang tidak diminta untuk menemukan hash yang tepat, melainkan menemukan hash di bawah nilai target. Satu-satunya cara untuk mencapai hal ini adalah dengan melakukan percobaan dalam jumlah yang sangat banyak, sampai sebuah header tertentu dari blok kandidat mereka, ketika di-hash, menghasilkan hash yang lebih kecil dari target ini.



Ketika target sudah cukup rendah, proses ini menjadi mahal. Penambang menghitung hash dari header blok kandidatnya, memeriksa hasilnya dan, jika kondisi tidak terpenuhi, memodifikasi header dan mengulangi perhitungan. Perulangan ini diulangi sampai header yang valid ditemukan. Ketika hash dari header tersebut akhirnya memenuhi syarat, maka proof of work dibuat, blok tersebut dianggap valid dan dapat disiarkan di jaringan Bitcoin untuk ditambahkan ke dalam blockchain mereka. Penambang yang menang kemudian menerima hadiah yang terkait (kami akan menjelaskan komposisinya nanti), sementara semua penambang segera mencari header baru yang valid untuk blok berikutnya.



Keuntungan mendasar dari mekanisme ini terletak pada asimetri. Memproduksi proof of work sangat mahal untuk penambang, karena membutuhkan perhitungan hash dalam jumlah besar. Di sisi lain, untuk verifikator, yaitu node jaringan, verifikasi sangat sederhana: yang harus mereka lakukan adalah meng-hash header blok yang disediakan oleh penambang dan memeriksa bahwa hash yang dihasilkan memang lebih rendah dari target. Oleh karena itu, menemukan sebuah bukti membutuhkan banyak pekerjaan dan sumber daya, sedangkan memverifikasi keabsahannya cepat dan murah. Sifat inilah yang mendefinisikan sebuah sistem proof-of-work yang efisien.



### The nonce



Sebuah pertanyaan praktis tetap ada: jika header blok kandidat yang dibuat oleh penambang tidak memberikan hash yang valid, bagaimana penambang dapat mencoba lagi? Ia perlu memodifikasi sesuatu di header untuk mendapatkan hash yang berbeda. Inilah peran dari nonce.



Ingatlah properti pertama dari fungsi hash: mengubah satu bit dari input sudah cukup untuk menghasilkan hash output yang benar-benar berbeda dan tidak dapat diprediksi. Oleh karena itu, setiap perhitungan hash mirip dengan pengundian acak.



![Image](assets/fr/016.webp)



Untuk mencoba peruntungannya lagi, penambang tidak perlu memodifikasi seluruh header dari blok kandidatnya: ia hanya perlu mengubah sebagian kecil saja, karena bahkan satu bit yang berbeda akan menghasilkan hash yang sama sekali baru, yang berpotensi valid jika lebih kecil dari target.



Inilah alasan mengapa header blok berisi nonce. Nonce merupakan sebuah nilai 32-bit, yang digunakan sekali dan kemudian diganti. Secara praktis, untuk kandidat blok yang sama, seorang penambang dapat menguji sekitar 4.29 miliar kemungkinan nilai (dari `0` sampai `2^32 - 1`). Setiap variasi dari nonce memodifikasi header blok dan, akibatnya, mengubah hash yang dihasilkan setelah menerapkan fungsi hash `SHA256d`.



Proses mining sangat sederhana:




- penambang membangun sebuah kandidat blok (transaksi + header);
- kemudian menghitung hash dari `SHA256d(header)`;
- jika hasilnya lebih besar dari target, maka akan mengubah nonce;
- dimulai lagi;
- dll.



![Image](assets/fr/017.webp)



Pada kenyataannya, nonce bukanlah satu-satunya field yang dapat dimodifikasi. Setiap modifikasi dalam transaksi sebuah blok akan mengakibatkan perubahan pada akar pohon Merkle, dan oleh karena itu modifikasi pada header blok tersebut. Dengan daya komputasi modern, memeriksa 4,29 miliar kemungkinan nilai nonce dapat dilakukan dengan relatif cepat. Itulah mengapa ada bidang lain, umumnya disebut sebagai "*[extra-nonce](https://planb.academy/resources/glossary/extra-nonce)*", yang selanjutnya melipatgandakan kemungkinan variasi header. Kita akan kembali ke mekanisme ini secara lebih rinci di bab selanjutnya.



### Apa gunanya proof of work?



Kami menyebutnya "bukti" karena hasilnya dapat segera diverifikasi: setelah sebuah blok diproduksi, setiap node dapat memeriksa, dalam waktu sepersekian detik, apakah hash kriptografi dari header-nya memang di bawah target yang diperlukan. Kami menyebutnya "kerja" karena untuk mencapai hash ini membutuhkan banyak percobaan, dan oleh karena itu membutuhkan biaya yang besar dalam hal komputasi dan energi.



Dalam [Buku Putih](https://planb.academy/resources/glossary/white-paper) Bitcoin, Satoshi Nakamoto mengedepankan dua keuntungan dalam menggunakan sistem proof-of-work di Bitcoin:





- Seal yang mencatat sejarah ekonomi:**



Setelah beban komputasi dihabiskan, blok tersebut terkunci: memodifikasinya akan membutuhkan pengulangan proof of work blok tersebut. Dan karena blok-blok tersebut dirantai bersama, mengubah blok lama juga berarti menghitung ulang semua blok berikutnya, dan kemudian mengejar dan melampaui pekerjaan yang sedang berlangsung dari rantai yang jujur.



Dengan kata lain, proof-of-work berfungsi sebagai tulang punggung dari sistem time-stamping, membuatnya semakin mahal untuk memalsukan masa lalu ketika blok-blok terakumulasi. Ketika sebuah blok baru ditambang, keamanan yang disediakan oleh proof of work diterapkan secara bersamaan dan seragam pada semua UTXO yang ada. Dengan setiap blok yang ditambahkan, setiap UTXO akan mengakumulasikan jumlah keamanan tambahan dari Proof-of-Work.





- Menetapkan aturan mayoritas ([konsensus](https://planb.academy/resources/glossary/consensus)) dan menetralisir Sybil:**



Proof-of-Work juga memungkinkan Bitcoin untuk mencapai konsensus tanpa bergantung pada aturan pemungutan suara "satu ID = satu suara", yang dapat dengan mudah dipalsukan oleh pembuatan identitas secara besar-besaran (IP, node, key...).



Dalam Bitcoin, "*mayoritas*" bukanlah jumlah peserta terbanyak, tetapi *rantai yang mengumpulkan pekerjaan terbanyak*. Seperti yang dikatakan oleh Satoshi, ini adalah prinsip "satu CPU = satu suara", yaitu suara yang dibobot oleh daya komputasi aktual yang dihabiskan untuk menghasilkan blok yang valid. Jadi, menggunakan ribuan node tidak memberikan keuntungan lebih dari Bitcoin. Tanpa daya komputasi tambahan, tidak ada lagi bukti kerja yang terakumulasi, dan [serangan Sybil](https://planb.academy/resources/glossary/sybil-attack) menjadi tidak berguna, sementara aturan keputusan tetap objektif dan tidak memerlukan identifikasi peserta.



![Image](assets/fr/018.webp)



[Nakamoto, S. (2008). *Bitcoin: Sistem Uang Elektronik Peer-to-Peer.*] (https://bitcoin.org/bitcoin.pdf)



Prinsip-prinsip yang berkaitan dengan kegunaan dan kekuatan anak di bawah umur adalah subjek yang sangat kompleks, yang tidak akan saya bahas secara lebih rinci dalam kursus ini. Namun, kita akan kembali ke subjek ini secara mendalam dalam kursus pelatihan MIN 201 di masa mendatang.



Untuk saat ini, Anda dapat meringkas cara kerja mining seperti ini: penambang membuat sebuah kandidat blok dengan transaksi yang tertunda di mempool, kemudian mencari hash dari header-nya (melalui `SHA256d`) yang kurang dari atau sama dengan target. Mereka mencapai ini dengan menguji nonce melalui uji coba.



Dalam bab berikutnya, kita akan membahas sejarah singkat mengenai prinsip proof-of-work untuk memahami latar belakangnya, dan kemudian melihat bagaimana target kesulitan ditentukan oleh sistem.



## Sejarah proof of work


<chapterId>919d9f3e-8b3b-41d9-b45a-54df4f3c31a3</chapterId>



Proof-of-work tidak diciptakan untuk Bitcoin. [Satoshi Nakamoto](https://planb.academy/resources/glossary/nakamoto-satoshi) mengambil dan mengumpulkan beberapa ide lama, yang sudah dieksplorasi dalam konteks yang berbeda.



### Hash uang tunai



Pada akhir tahun 1990-an, masalah spam email menjadi signifikan. Memang, jika mengirim email hampir tidak memerlukan biaya, seorang spammer dapat mengirim jutaan. Tetapi jika setiap pesan membutuhkan upaya komputasi yang kecil, mengirim satu pesan yang sah tetap mudah bagi pengguna normal, sedangkan mengirim jutaan pesan menjadi sangat mahal.



Ini adalah tujuan dari [Hashcash](https://planb.academy/resources/glossary/hashcash), yang diusulkan oleh Adam Back pada tahun 1997, yang dianggap sebagai penemuan prinsip proof-of-work. Prinsip Hashcash sangat mirip dengan mining: menghasilkan sebuah hash yang sesuai dengan sebuah kondisi (memiliki sejumlah angka nol di awal hash). Bukti tersebut kemudian menyertai pesan dan dapat diverifikasi dengan sangat cepat oleh penerima. Jika sebuah email diterima yang tidak mengandung bukti ini, maka email tersebut dapat langsung dianggap sebagai spam, dan oleh karena itu disaring. Spammer kemudian dipaksa untuk mengeluarkan energi yang cukup besar untuk mengirimkan jutaan pesan, yang secara drastis mengurangi (atau bahkan meniadakan sama sekali) keuntungan dari jenis operasi ini, baik untuk tujuan pemasaran atau penipuan.



Saat ini, Hashcash tidak digunakan untuk email. Penyaringan spam sekarang sebagian besar didasarkan pada sistem terpusat. Keunggulan Hashcash dibandingkan solusi yang ada saat ini terletak pada kenyataan bahwa ia tidak memerlukan penyaringan terpusat: siapa pun bisa menyesuaikan parameter sesuai dengan kriteria mereka sendiri. Juga tidak memerlukan identifikasi, karena pencarian hash dapat dilakukan secara anonim. Di atas semua itu, ia tidak bergantung pada sistem reputasi, yang cenderung memperkenalkan bentuk-bentuk penyaringan yang subjektif.



Hashcash bukan tentang menciptakan uang. Ini berusaha untuk membebankan biaya marjinal pada tindakan digital yang mudah diotomatisasi.



![Image](assets/fr/008.webp)



### Bit Gold



Pada akhir tahun 1990-an dan awal tahun 2000-an, Nick Szabo mengeksplorasi ide kelangkaan digital berdasarkan proof of work. Proyek konseptualnya, yang disebut Bit Gold, membayangkan penciptaan unit-unit nilai dengan memecahkan proof of work yang mahal, kemudian mencatat bukti-bukti ini dalam sebuah register untuk menetapkan bentuk kepemilikan.



Bit Gold tidak menghasilkan sistem yang digunakan seperti Bitcoin, tetapi mengandung beberapa wawasan penting: gagasan bahwa komputasi dapat menghasilkan kelangkaan, dan gagasan tentang elemen penanda waktu dari waktu ke waktu untuk menciptakan sejarah yang sulit untuk ditulis ulang.



### RPOW



Pada tahun 2004, Hal Finney mengusulkan RPOW (*Bukti Kerja yang Dapat Digunakan Kembali*). Idenya adalah untuk menghasilkan bukti kerja yang kemudian dapat dipertukarkan, bukan hanya dikonsumsi. RPOW bertujuan untuk membuat token digital berdasarkan proof of work, dengan sistem untuk memverifikasi dan mentransfer token ini tanpa menggandakannya. RPOW, sekali lagi, tidak secara memuaskan memecahkan masalah registri yang sepenuhnya terdesentralisasi seperti yang akan dilakukan Bitcoin, tetapi tetap menjadi salah satu prekursor besar Bitcoin.



![Image](assets/fr/009.webp)



Hashcash, Bit Gold, dan RPOW menggunakan proof-of-work untuk membebankan biaya dan menciptakan suatu bentuk kelangkaan. Bitcoin mengambil mekanisme ini, tetapi memberinya peran sentral dan kolektif: proof-of-work tidak hanya digunakan untuk menciptakan sesuatu, tetapi juga digunakan untuk memutuskan siapa yang berhak menulis halaman berikutnya dari register (blok berikutnya), dan membuat register ini mahal untuk dipalsukan.



## Menyesuaikan target kesulitan


<chapterId>528bcaa8-351e-4eae-887a-426a78a223e3</chapterId>



Pada bab sebelumnya, Anda telah melihat inti dari proof-of-work: penambang meng-hash header dari kandidat blok dengan `SHA256d`, dan blok hanya dianggap valid jika hash yang dihasilkan secara numerik kurang dari atau sama dengan nilai referensi yang disebut dengan target. Pertanyaannya kemudian adalah: dari mana target ini berasal, dan bagaimana sistem memastikan bahwa target ini tetap konsisten dari waktu ke waktu?



Bitcoin menargetkan tingkat rata-rata satu blok ditemukan setiap 10 menit. Tentu saja, kecepatan ini tidak dijamin sampai detik. Pada praktiknya, beberapa blok ditemukan beberapa detik setelah blok sebelumnya, sementara yang lain ditemukan setelah lebih dari satu jam. Yang penting di sini adalah rata-rata dalam jangka waktu yang cukup lama.



![Image](assets/fr/019.webp)



Variabilitas ini berasal dari sifat probabilistik mining: setiap hash merupakan sebuah usaha yang independen, dengan probabilitas yang konstan (dengan asumsi target tidak berubah) untuk menghasilkan sebuah hasil di bawah target. Oleh karena itu, hal ini dapat dibandingkan dengan sebuah undian dengan pengundian yang terus menerus: semakin banyak hash yang dibuat oleh para penambang per detiknya, semakin pendek penundaan yang diharapkan sebelum munculnya sebuah blok yang valid, tetapi tanpa menghilangkan keacakan dari satu pengundian ke pengundian berikutnya.



### Mengapa menargetkan 10 menit di antara blok?



Meskipun tidak ada bukti mengenai hal ini, Satoshi Nakamoto pasti memilih 10 menit sebagai kompromi praktis antara efisiensi dan keamanan. Interval yang lebih pendek akan memberikan konfirmasi yang lebih sering, tetapi akan menyebabkan lebih banyak perpecahan jaringan sementara. Untuk memahami hal ini, kita perlu kembali ke cara penyebaran blok.



Ketika seorang penambang menemukan sebuah blok yang valid, ia akan segera mendistribusikannya ke rekan-rekannya. Node yang menerimanya akan memeriksa keabsahannya (transaksi, proof of work, aturan konsensus, dll.), kemudian menyebarkannya secara bergantian. Penyebaran ini membutuhkan waktu tertentu, dibatasi oleh latensi internet, bandwidth, dan kemampuan setiap node untuk memverifikasi blok.



![Image](assets/fr/020.webp)



Jika, selama penundaan difusi ini, penambang lain juga menemukan blok yang valid pada ketinggian yang sama, jaringan mungkin akan terpecah untuk sementara waktu: satu bagian node dan penambang mengandalkan blok A, sementara yang lainnya mengandalkan blok B. Ini adalah pembagian sementara dari jaringan.



![Image](assets/fr/021.webp)



Pembagian ini bukanlah sebuah bencana. Konsensus Nakamoto memprediksi bahwa, dalam jangka panjang, hanya satu cabang yang akan bertahan: cabang yang paling banyak mengumpulkan pekerjaan. Memang, segera setelah blok baru ditambang di atas blok A, misalnya, seluruh jaringan melakukan sinkronisasi ulang pada cabang ini dan meninggalkan blok B, yang kemudian menjadi "*[blok basi](https://planb.academy/resources/glossary/stale-block)*", yang terkadang secara keliru disebut sebagai "*blok yatim piatu*" dalam bahasa sehari-hari.



![Image](assets/fr/022.webp)



Di sisi lain, mereka memiliki biaya: selama beberapa menit, sebagian kecil penambang bekerja pada cabang yang akan ditinggalkan. Pekerjaan ini kemudian terbuang sia-sia dari sudut pandang keamanan secara keseluruhan, karena tidak berkontribusi pada rantai akhir. Semakin cepat interval antara setiap blok, semakin besar kemungkinan terjadinya perpecahan, karena waktu propagasi mewakili proporsi yang lebih besar dari waktu antara setiap blok.



Interval 10 menit biasanya memberikan waktu yang cukup bagi blok yang menang untuk menyebar secara luas sebelum blok yang bersaing pada ketinggian yang sama ditemukan. Ini adalah kompromi yang membatasi perpecahan, mengurangi daya komputasi yang terbuang, dan membantu jaringan tetap tersinkronisasi dalam skala global.



### Memahami hashrate



*"[Hashrate](https://planb.academy/resources/glossary/hashrate)*" merujuk pada jumlah komputasi hash yang dihasilkan per detik, baik oleh satu penambang, sekelompok penambang, atau semua penambang di Bitcoin. Hal ini dinyatakan dalam `H/s` (hash per detik), dengan kelipatannya seperti `TH/s` (terahash per detik) atau `EH/s` (exahash per detik). Ini menunjukkan jumlah percobaan yang dapat dilakukan oleh penambang setiap detiknya untuk mendapatkan hash yang lebih rendah dari target.



Jika target tetap, maka:




- setiap upaya memiliki probabilitas keberhasilan yang tetap;
- membuat lebih banyak percobaan per detik meningkatkan kemungkinan upaya kemenangan akan muncul dengan cepat


Dengan kata lain, jika jaringan Bitcoin besok menggandakan daya komputasinya dengan menghubungkan dua kali lebih banyak mesin mining, tanpa mekanisme korektif, blok akan ditemukan rata-rata dua kali lebih cepat. Oleh karena itu, target harus disesuaikan untuk mengimbangi variasi hashrate.



### Menyesuaikan target kesulitan



Bitcoin memecahkan masalah ini dengan mekanisme penyesuaian target secara berkala, yang menyesuaikan [tingkat kesulitan](https://planb.academy/resources/glossary/difficulty-adjustment) mining. Prinsipnya adalah sebagai berikut: setiap 2016 blok (kira-kira setiap 2 minggu), setiap node menghitung ulang target tingkat kesulitan dengan mengamati berapa banyak waktu yang sebenarnya dibutuhkan untuk menghasilkan 2016 blok ini.



Tujuan dari mekanisme ini adalah untuk mengurangi waktu produksi rata-rata satu blok menjadi sekitar 10 menit, sementara keseluruhan hashrate dari jaringan terus berubah, karena adanya mesin yang terputus atau, sebaliknya, adanya mesin baru yang ditambahkan.



![Image](assets/fr/023.webp)



Perhitungan didasarkan pada waktu yang diamati untuk periode yang telah berlalu:




- jika blok-blok tahun 2016 yang lalu ditemukan terlalu cepat, ini berarti hashrate meningkat selama periode ini; Bitcoin kemudian membuat kondisi menjadi lebih sulit dengan menurunkan target untuk periode berikutnya;
- jika blok 2016 ditemukan terlalu lambat, ini berarti hashrate mengalami penurunan; Bitcoin meringankan kondisi tersebut dengan meningkatkan target.



Rumusnya adalah sebagai berikut:



```txt
Tn = To * (Ta / Tt)
```



Dengan:




- `tn`: target baru
- `to`: target lama
- `Ta`: waktu yang telah berlalu secara real time untuk blok 2016 terakhir
- `Tt`: waktu target (dalam detik)



Dengan target waktu dua minggu, yaitu `Tt = 1.209.600` detik:



```txt
Tn = To * (Ta / 1 209 600)
```



Untuk memahami cara menyesuaikan tingkat kesulitan Bitcoin mining, berikut ini contoh dengan nilai fiktif:



```txt
Tn = To * (Ta / 1 209 600)
Tn = 18 045 755 102 * (1 000 000 / 1 209 600)
Tn = 14 918 779 020
```


Dengan:



- `**Untuk = 18.045.755.102**`: Target lama, yaitu nilai referensi sebelum penyesuaian.
- `**ta = 1.000.000 detik**`: Waktu yang sebenarnya dihabiskan untuk memproduksi blok 2016 terakhir. Karena waktu ini kurang dari waktu target, jaringan telah menambang terlalu cepat.
- 1.209.600 detik ****: Target waktu yang sesuai dengan 10 menit per blok untuk blok 2016, digunakan sebagai referensi untuk penyesuaian.
- `**tn = 14.918.779.020**`: Target baru dihitung setelah penyesuaian tingkat kesulitan.



Di sini, target baru lebih rendah dari target lama, yang berarti mining menjadi lebih sulit untuk memperlambat produksi blok di periode berikutnya.


*Nilai target dalam contoh ini disederhanakan dan diskalakan untuk tujuan pengajaran; target aktual yang digunakan dalam Bitcoin adalah bilangan bulat 256-bit dengan urutan besaran yang sama sekali berbeda.*



Perhitungan ini dilakukan secara lokal oleh setiap node, berdasarkan stempel waktu yang dimasukkan dalam blok. Karena semua node menerapkan aturan yang sama, mereka sampai pada hasil yang sama, dan target baru menjadi referensi umum untuk blok 2016 berikutnya.



Ada detail penting yang perlu diperhatikan mengenai penyesuaian ini: **terbatas**. Bitcoin membatasi variasi kesulitan per periode untuk menghindari perubahan yang terlalu mendadak yang dapat memblokirnya. Faktanya, waktu aktual yang diperhitungkan dibatasi untuk tetap berada dalam kisaran yang setara dengan faktor 4 (minimal seperempat dari target lama, maksimal empat kali target lama). Hal ini mencegah penargetan ulang yang ekstrem jika cap waktu sangat tidak lazim atau dimanipulasi.



Perlu diperhatikan juga bahwa pada kenyataannya, penyesuaian kesulitan Bitcoin tidaklah sempurna. Memang, kita telah melihat bahwa kesulitan tersebut dijadwalkan untuk dihitung ulang setiap 2016 blok, dengan membandingkan waktu nyata yang berlalu dengan waktu target 14 hari (2016 × 10 menit). Namun, kode asli Satoshi mengandung kesalahan yang disebut "*off-by-one*": alih-alih mengukur waktu antara blok terakhir dari setiap periode (yaitu 2016 interval), ia mengukur waktu antara blok pertama dan terakhir, yaitu hanya 2015 interval. Secara konkret, kesulitan dihitung seolah-olah periode tersebut hanya terdiri dari 2015 blok, bukan 2016. Konsekuensinya adalah kesulitan tersebut secara sistematis sedikit terlalu tinggi, yang berarti blok-blok ditambang rata-rata sedikit lebih lambat dari target 10 menit (sekitar 0,05% lebih lambat). Bug ini sangat terkenal tetapi tidak pernah diperbaiki, karena memodifikasinya akan membutuhkan hard fork dan dampaknya tetap dapat diabaikan dalam praktik, di luar serangan teoritis yang disebut "*time warp*".

### Representasi target



Pada header blok, target tidak muncul dalam bentuk 256-bit penuh, karena ini akan menghabiskan terlalu banyak ruang. Sebagai gantinya, bidang `nBits` 32-bit mengkodekan target dalam format yang ringkas, sebanding dengan notasi ilmiah dasar 256: eksponen (1 byte) dan koefisien (3 byte). Target lengkap kemudian direkonstruksi dari dua nilai ini. Kami tidak akan membahasnya secara rinci di sini, karena subjek ini relatif rumit dan tidak menambah apa pun pada pemahaman mining. Ingatlah bahwa target tidak disimpan dalam bentuk mentah di header blok, tetapi dalam bentuk yang ringkas.



Pada bab terakhir dari Bagian I ini, kita telah melihat bagaimana cara kerja proof-of-work di Bitcoin: penambang membuat sebuah kandidat blok dengan memilih transaksi dari mempool, menghitung header blok kandidat, melakukan hash, membandingkan hash yang dihasilkan dengan target periode, kemudian memulai lagi dengan memodifikasi nonce sampai hash yang valid diperoleh. Akhirnya, setiap 2016 blok, jaringan menghitung ulang target baru untuk mempertahankan waktu rata-rata sekitar 10 menit per blok, meskipun ada variasi konstan dalam hashrate.




# Sistem insentif Bitcoin mining


<partId>27fb10c1-d53b-4dc2-90fa-3cb0309b74c1</partId>



## Block reward


<chapterId>b316fb89-9c18-417e-917b-ab98f1722646</chapterId>



Seperti yang dapat Anda bayangkan, Bitcoin mining bukanlah aktivitas altruistik. Miner memiliki biaya yang nyata: listrik untuk menjalankan komputer mining mereka, pembelian peralatan khusus, gaji untuk pemeliharaan, terkadang tempat dan sistem pendingin. Agar sistem Bitcoin dapat bekerja, kepentingan pribadi para penambang harus diselaraskan dengan kepentingan kolektif jaringan. Inilah peran dari reward mining. Reward ini mendorong para penambang untuk berinvestasi di proof of work, memasukkan transaksi yang valid, dan menghormati aturan protokol daripada mencoba merusaknya.



Logika ini didasarkan pada teori permainan: protokol ini membuat kejujuran menjadi rasional. Seorang penambang akan mendapatkan uang jika ia menghasilkan blok yang valid dan diterima oleh node. Sebaliknya, jika ia mencoba untuk berbuat curang, bloknya akan ditolak oleh node, dan ia tidak akan mendapatkan apa-apa. Karena memproduksi sebuah blok memiliki biaya, maka blok yang ditolak merupakan kerugian langsung. Dalam lingkungan yang kompetitif di mana ribuan pemain secara bersamaan mencari blok yang valid, strategi yang paling menguntungkan, sebagian besar waktu, adalah mengikuti peraturan dengan ketat dan memaksimalkan pendapatan Anda dengan jujur.



Untuk mencapai hal ini, protokol Bitcoin menetapkan bahwa penambang yang menemukan blok yang valid akan mendapatkan hak untuk menyertakan transaksi tertentu ke dalamnya, yang akan memberikan penambang sejumlah BTC. Hal ini dikenal sebagai **[block reward](https://planb.academy/resources/glossary/block-reward)**. Pada bab pertama bagian ini, tujuannya adalah untuk memahami apa itu terdiri dari dan bagaimana cara menentukannya. Kemudian, kita akan melihat bagaimana bagian penciptaan uang berkembang dari waktu ke waktu (dengan pembagian) dan bagaimana cara pengumpulannya secara teknis (melalui transaksi coinbase).



### Terdiri dari apa saja hadiah blokir?



Pada bab sebelumnya, kita telah melihat bagaimana penambang dapat menemukan blok yang valid. Ketika seorang penambang menemukan header yang hash-nya lebih kecil dari target, maka blok kandidatnya dianggap valid. Dia kemudian dapat mendistribusikannya ke seluruh jaringan Bitcoin. Blok tersebut ditambahkan ke seluruh blockchain, mengonfirmasi transaksi yang dikandungnya.



Peristiwa inilah (penambahan blok ke blockchain) yang memicu pemberian reward kepada penambang yang menang. Hadiah ini terdiri dari dua elemen berbeda yang ditambahkan bersama:




- [subsidi blokir](https://planb.academy/resources/glossary/block-subsidy)**;
- biaya transaksi**.



![Image](assets/fr/024.webp)



Mari kita lihat apa yang dimaksud dengan kedua bagian hadiah ini.



### Subsidi blokir



Subsidi blok sesuai dengan bagian penciptaan moneter dari reward. Ketika seorang penambang menghasilkan sebuah blok yang valid, protokol memberikan wewenang kepadanya untuk membuat sejumlah bitcoin baru dan mengalokasikannya untuk dirinya sendiri sebagai hadiah. Bitcoin ini diciptakan secara ex nihilo. Mereka tidak ada sebelumnya.



Akan tetapi, jumlah bitcoin yang baru dibuat sama sekali tidak sembarangan. Hal ini ditentukan secara ketat oleh aturan protokol Bitcoin dan sama untuk semua penambang. Kita akan melihat lebih dekat pada mekanisme ini di bab berikutnya, karena subsidi bukanlah nilai tetap tanpa batas: subsidi dibagi secara berkala sesuai dengan jadwal yang tepat. Untuk saat ini, ingatlah itu:




- subsidi blok adalah salah satu dari dua komponen reward blok;
- dibatasi dan ditentukan oleh protokol, bukan oleh penambang (meskipun secara teknis penambang dapat meminta kurang dari jumlah maksimum);
- itu menciptakan bitcoin dari udara.



Subsidi ini memainkan dua peran utama dalam protokol Bitcoin. Yang pertama adalah mendorong pemain untuk berpartisipasi dalam mining. Pada tahun-tahun awal Bitcoin (dan terkadang masih sampai sekarang), biaya transaksi sangat rendah. Oleh karena itu, subsidi telah menjamin kompensasi yang cukup untuk menarik para penambang dan menjaga tingkat keamanan sistem.



Peran kedua berkaitan dengan distribusi mata uang. Setiap mata uang baru menghadapi pertanyaan tentang bagaimana mendistribusikan unit moneter secara adil kepada penduduk. Subsidi blok memberikan jawaban untuk masalah ini. Dengan menciptakan bitcoin melalui mining, ini memungkinkan distribusi awal dengan cara yang terbuka dan netral: siapa pun dapat memperolehnya, asalkan mereka berpartisipasi dalam mining, tanpa memerlukan otorisasi atau identifikasi sebelumnya.



Di sisi lain, karena bitcoin diciptakan dari ketiadaan, nilainya bukan tanpa dasar. Dengan meningkatkan jumlah uang yang beredar, subsidi secara mekanis melemahkan nilai bitcoin yang ada. Oleh karena itu, hal ini memperkenalkan sebuah bentuk inflasi moneter. Namun, kita akan melihat pada bab selanjutnya bahwa subsidi ini ditakdirkan untuk menghilang secara bertahap, dan inflasi pada akhirnya akan berhenti.



![Image](assets/fr/025.webp)



### Biaya transaksi



Komponen kedua dari reward blok terkait dengan penggunaan sistem: ketika pengguna memposting sebuah transaksi, ia ingin transaksi tersebut dikonfirmasi. Akan tetapi, ruang blok terbatas, dan blok muncul rata-rata hanya setiap 10 menit atau lebih. Oleh karena itu, ruang blok merupakan sumber daya yang langka. Ketika permintaan melebihi penawaran, harga akan naik: inilah pasar biaya transaksi. Setiap penambang yang berhasil membuat blok yang valid mendapatkan hak untuk mengumpulkan, untuk akunnya sendiri, seluruh biaya transaksi yang terkait dengan semua transaksi yang telah ia masukkan ke dalam bloknya.



Anda dapat menganggapnya sebagai sistem lelang: setiap transaksi mengajukan sejumlah biaya, dan penambang memprioritaskan transaksi yang memaksimalkan pendapatan mereka, di bawah keterbatasan ruang. Mekanisme ini secara alami menyelaraskan kepentingan:




- pengguna yang terburu-buru membayar lebih banyak agar dapat dimasukkan dengan cepat;
- penambang didorong untuk memasukkan transaksi yang membayar biaya tertinggi untuk ruang blok.
- jaringan menghindari spam, karena menerbitkan transaksi memiliki biaya.



#### Bagaimana cara menghitung biaya transaksi?



Berlawanan dengan kepercayaan umum, biaya bukanlah output dalam transaksi Bitcoin. Faktanya, sebuah transaksi menghabiskan input dan menghasilkan output. Input mewakili sumber bitcoin yang digunakan, sedangkan output mewakili tujuan pembayaran. Biaya transaksi hanyalah **perbedaan antara total input dan total output**.



Dengan kata lain, input bitcoin pengguna, yang merupakan milik mereka, menciptakan output untuk penerima, tetapi tidak mereproduksi jumlah penuh yang dikonsumsi oleh input. Selisih antara keduanya mewakili biaya transaksi yang dapat dikumpulkan oleh penambang.



Mari kita ambil sebuah contoh. Sebuah transaksi mengkonsumsi dua input, satu dari `100.000 sats` dan yang lainnya dari `150.000 sats`, dan menghasilkan tiga output dari `35.000 sats`, `42.000 sats`, dan `170.000 sats`.



![Image](assets/fr/027.webp)



Oleh karena itu, jumlah input adalah sebesar `250.000 sats`, sedangkan jumlah output adalah sebesar `247.000 sats`. Ini berarti bahwa `3.000 sats` telah dikonsumsi dalam bentuk input tanpa menghasilkan output: jumlah ini sesuai dengan biaya yang diusulkan oleh transaksi ini.



![Image](assets/fr/028.webp)



Jika penambang memasukkan transaksi ini ke dalam blok yang valid, ia berhak untuk mendapatkan kembali `3.000 sats` ini, di samping biaya dari semua transaksi lain yang termasuk dalam blok tersebut. Akan tetapi, tidak ada hubungan langsung on-chain antara transaksi yang membayar biaya dengan sats yang sebenarnya dikumpulkan oleh penambang. Secara teknis, biaya sebesar `3,000 sats` dihancurkan, dan sebagai gantinya, penambang mendapatkan hak untuk membuat ulang jumlah yang sama untuk dirinya sendiri.



#### Rasio biaya



Sebuah blok tidak dibatasi oleh jumlah transaksi, tetapi oleh kapasitas totalnya (saat ini, dalam praktiknya, oleh berat blok). Beberapa transaksi membutuhkan lebih banyak ruang daripada yang lain: transaksi dengan banyak input dan output akan lebih besar daripada transaksi sederhana dengan satu input dan dua output. Skrip yang digunakan juga akan mempengaruhi ukuran.



![Image](assets/fr/026.webp)



Oleh karena itu, dua transaksi dapat membayar jumlah biaya yang sama secara absolut, tetapi tidak setara secara ekonomi dari sudut pandang penambang. Jika salah satunya dua kali lebih besar, maka akan membutuhkan dua kali lebih banyak ruang di blok tersebut. Ruang sangat terbatas, sehingga penambang berusaha untuk memaksimalkan pendapatannya per unit ruang.



Inilah sebabnya, dalam praktiknya, kami mengekspresikan daya saing transaksi dengan rasio biaya, biasanya dalam `sats/vB` ([satoshi](https://planb.academy/resources/glossary/satoshi-sat) per byte virtual). Menghitung rasio ini sangat mudah:



```text
fee rate = fee / weight (in vB)
```



Sebagai contoh, jika kita memiliki transaksi dengan berat `141 vB` dan mengalokasikan biaya `1.974 sats`, transaksi tersebut akan memiliki tarif biaya sebesar `14 sats/vB`.



```text
1 974 / 141 ≈ 14 sats/vB
```



Rasio ini menjelaskan pilihan ekonomi yang dibuat oleh para penambang: pada kapasitas yang tetap, termasuk transaksi berbiaya tinggi akan memaksimalkan total biaya blok, dan oleh karena itu, kompensasi penambang. Rasio ini juga menjelaskan mengapa transaksi berbiaya rendah tetap mengantri di mempool untuk waktu yang lama: mereka bersaing dengan transaksi lain yang membayar lebih banyak per unit ruang.



### Perlindungan jaringan terhadap spam



Biaya juga memiliki tujuan keamanan operasional: mereka memperkenalkan biaya untuk penggandaan transaksi. Jika mempublikasikan transaksi gratis, maka akan mudah untuk membanjiri jaringan dengan transaksi yang tidak berguna dan memenuhi mempool, meningkatkan beban pada node.



Dalam praktiknya, node menerapkan kebijakan relai lokal (aturan mempool) dan sering kali menetapkan ambang batas biaya minimum di bawahnya yang tidak akan merelai transaksi (secara default, `0.1 sat/vB` di Bitcoin Core melalui `minRelayTxFee`). Sebuah transaksi mungkin valid dalam arti yang ketat dari aturan konsensus, tetapi tidak akan direlay oleh sebagian besar node jika biayanya terlalu rendah. Akibatnya, transaksi tersebut tidak beredar, tidak sampai ke penambang, dan memiliki peluang yang sangat kecil untuk dikonfirmasi.



Sampai di sini, Anda sudah mengetahui inti dari reward blok: reward ini sesuai dengan kompensasi untuk penambang yang menang dan terdiri dari dua elemen yang berbeda. Di satu sisi, subsidi blok, yang ditentukan oleh aturan protokol, yang menciptakan bitcoin baru secara ex nihilo. Dan di sisi lain, biaya transaksi yang termasuk dalam blok yang ditambang.



Pada bab berikutnya, kita akan fokus lebih detail pada subsidi blok, untuk memahami dengan tepat bagaimana cara menghitungnya dan bagaimana ia berkembang dari waktu ke waktu sesuai dengan aturan protokol Bitcoin.



## Halving


<chapterId>7cdca211-7300-48f8-a1e4-53e5c2678cd8</chapterId>



Pada bab sebelumnya, kita telah melihat bahwa penambang yang menghasilkan sebuah blok yang valid akan menerima upah yang terdiri dari biaya transaksi yang termasuk dalam blok tersebut, ditambah dengan subsidi blok. Akan tetapi, kami belum menjelaskan bagaimana jumlah subsidi ini ditentukan. Mekanisme yang menentukan dan mengembangkan nilai ini dikenal sebagai ***[halving](https://planb.academy/resources/glossary/halving)***.



### Apa yang dimaksud dengan halving?



Halving adalah sebuah peristiwa yang diprogram ke dalam protokol Bitcoin yang membagi dua subsidi blok, yaitu jumlah maksimum bitcoin baru yang diizinkan untuk dibuat oleh penambang yang menang dengan setiap blok. Peristiwa ini tidak mempengaruhi biaya transaksi: biaya transaksi tetap berdiri sendiri dan tetap ditentukan oleh aktivitas pengguna dan persaingan untuk mendapatkan ruang blok.



Ketika Bitcoin diluncurkan pada tahun 2009, subsidi blok ditetapkan sebesar 50 BTC untuk setiap blok yang ditambang. Sejak saat itu, subsidi ini telah dibagi dua beberapa kali untuk setiap pembagian.



![Image](assets/fr/029.webp)



Halving tidak dipicu oleh tanggal, tetapi oleh tinggi blok. Ini dieksekusi **setiap 210.000 blok**. Karena Bitcoin menargetkan interval rata-rata sekitar 10 menit per blok, maka 210.000 blok setara dengan sekitar empat tahun.



```cpp
CAmount GetBlockSubsidy(int nHeight, const Consensus::Params& consensusParams)
{
int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;
// Force block reward to zero when right shift is undefined.
if (halvings >= 64)
return 0;

CAmount nSubsidy = 50 * COIN;
// Subsidy is cut in half every 210,000 blocks which will occur approximately every 4 years.
nSubsidy >>= halvings;
return nSubsidy;
}
```



Dengan demikian, jika kita mencatat `n` jumlah halving yang telah terjadi, subsidi blok di BTC dapat dihitung sebagai berikut:



```text
subsidy(n) = 50 / 2^n
```



### Pembagian masa lalu



Berikut ini adalah tabel ringkasan halving yang telah terjadi, dengan tinggi blok, tanggal, dan subsidi blok baru yang berlaku setelah peristiwa tersebut:



| Event               |   Height  | Date                        | Subsidy    |
| ------------------- | --------: | --------------------------- | ---------: |
| Halving 1           |   210 000 | 28 novembre 2012            |     25 BTC |
| Halving 2           |   420 000 | 9 july 2016                 |   12,5 BTC |
| Halving 3           |   630 000 | 11 may 2020                 |   6,25 BTC |
| Halving 4           |   840 000 | 20 april 2024               |  3,125 BTC |
| Halving 5 (upcoming) | 1 050 000 | Spring   2028 (estimation) | 1,5625 BTC |

### Kapan dan bagaimana subsidi berakhir?



Halving diulangi selama subsidi dapat dinyatakan dalam unit minimum sistem: satoshi.



```text
1 BTC = 100 000 000 sats
```



Ketika subsidi dikurangi setengahnya, pada akhirnya kita akan mencapai pecahan bitcoin yang sangat kecil sehingga menjadi kurang dari 1 satoshi. Pada titik ini, tidak mungkin lagi membuat setengah unit satoshi. Penciptaan uang melalui subsidi blok berhenti, dan para penambang hanya diberi kompensasi berdasarkan biaya transaksi. Mulai saat ini, semua bitcoin akan beredar, dan tidak mungkin lagi memproduksi unit baru.



Akhir definitif dari subsidi blok akan terjadi pada level blok 6.930.000, yaitu pada halving ke-33 dan terakhir. Peristiwa ini diperkirakan akan terjadi sekitar tahun 2140, meskipun tidak mungkin untuk memberikan tanggal yang pasti, karena akan tergantung pada kecepatan aktual di mana blok ditemukan antara sekarang dan saat itu.



Karena subsidi blok mengikuti urutan geometris dengan rasio 1/2 pada setiap halving, penciptaan uang sangat tinggi pada masa-masa awal Bitcoin, dan kemudian menurun dengan sangat cepat. Pada halving ke-7, lebih dari 99% bitcoin telah beredar. Ambang batas 99% diperkirakan akan terlampaui antara tahun 2032 dan 2036. Ini berarti akan membutuhkan waktu lebih dari 100 tahun untuk menambang 1% bitcoin yang tersisa. Meskipun inflasi moneter sangat tinggi ketika Bitcoin diluncurkan, untuk memungkinkan distribusi mata uang secara luas, inflasi sekarang sangat rendah dan akan terus turun, hingga mencapai tingkat mata uang keras yang sebenarnya, yang suplai yang beredar tidak dapat lagi meningkat.



![Image](assets/fr/030.webp)



### Mengapa tidak akan pernah ada 21 juta BTC?



Pasokan moneter maksimum Bitcoin sering disajikan sebagai 21 juta BTC. Ini adalah perkiraan yang baik untuk memahami kebijakan moneternya, tetapi dari sudut pandang teknis, total pasokan tidak akan pernah benar-benar mencapai 21.000.000 bitcoin.



Alasan utamanya adalah mekanis. Melalui pembagian dua yang berurutan, subsidi blok akhirnya jatuh di bawah nilai minimum 1 sat, yang mengakhiri penerbitan sebelum mencapai total teoritis yang tepat. Sebagai hasil dari perincian minimum ini dan aturan pembulatan, jumlah total bitcoin yang diciptakan oleh subsidi sedikit kurang dari 21 juta.



Selain itu, penyimpangan terkait protokol marjinal juga dapat menambah hal ini. Sebagai contoh, dalam kasus yang jarang terjadi, beberapa penambang mungkin tidak mengklaim subsidi penuh mereka, yang secara pasti mengurangi jumlah bitcoin yang sebenarnya dikeluarkan. Kita juga dapat menyebutkan [blok genesis](https://planb.academy/resources/glossary/genesis-block), yang diproduksi oleh Satoshi pada tanggal 3 Januari 2009, yang bitcoin yang dibuat bukan merupakan bagian dari [UTXO set](https://planb.academy/resources/glossary/utxo-set), serta kejadian historis tertentu yang terkait dengan bug, seperti pengidentifikasi transaksi coinbase yang duplikat.



Terakhir, kita juga harus memperhitungkan semua bitcoin yang telah dihancurkan atau diblokir:




- bitcoin terkunci dalam skrip yang tidak dapat dipecahkan;
- yang sengaja dihancurkan oleh skrip `OP_RETURN`;
- atau kehilangan kunci privat pada tingkat aplikasi.



Secara teori, pasokan Bitcoin dibatasi hingga 21 juta. Namun dalam praktiknya, tidak akan pernah ada 21 juta bitcoin yang beredar.



## Transaksi coinbase


<chapterId>69476700-3616-4aab-b006-367aba059de9</chapterId>



Pada bab-bab sebelumnya, kami telah menyampaikan dua poin penting. Pertama, penambang yang berhasil memproduksi dan mendistribusikan blok yang valid akan mendapatkan reward. Di sisi lain, kita telah melihat bahwa reward ini terdiri dari dua elemen yang berbeda:




- subsidi blok (bitcoin yang dibuat secara ex nihilo, jumlah maksimum yang ditetapkan oleh protokol dan secara bertahap dikurangi melalui pembagian);
- semua biaya transaksi yang dibayarkan oleh pengguna yang transaksinya telah dimasukkan ke dalam blokir.



Namun, ada satu pertanyaan yang tersisa: dengan mekanisme apa penambang mengumpulkan hadiah ini di Bitcoin? Inilah peran dari transaksi tertentu yang disebut "coinbase".



### Bagaimana cara kerja transaksi coinbase



Seperti yang telah kita lihat di bagian pertama kursus ini, setiap blok Bitcoin berisi daftar transaksi tertunda yang akan dikonfirmasikan. Yang pertama selalu merupakan [transaksi coinbase](https://planb.academy/resources/glossary/coinbase-transaction). Transaksi inilah yang memungkinkan penambang yang menang untuk menerima hadiah mereka.



![Image](assets/fr/031.webp)



Sekilas, transaksi ini terlihat seperti transaksi Bitcoin klasik: transaksi ini memiliki [TXID](https://planb.academy/resources/glossary/txid-transaction-identifier), output, dan termasuk dalam pohon Merkle blok. Akan tetapi, transaksi ini berbeda dalam satu hal penting: transaksi ini tidak menggunakan UTXO yang ada.



Dalam transaksi Bitcoin klasik, 'input' merujuk pada output sebelumnya yang belum digunakan (UTXO), yang memberikan nilai input. Output kemudian mendistribusikan kembali nilai ini ke UTXO yang baru, dengan kondisi pembelanjaan yang baru. Dengan kata lain, untuk mengirim bitcoin, Anda harus sudah memilikinya. Sebaliknya, transaksi coinbase tidak menggunakan bitcoin sebagai input: transaksi ini menciptakan bitcoin sebagai output langsung dari awal.



Mekanisme inilah yang memungkinkan bitcoin baru diperkenalkan ke dalam sirkulasi melalui subsidi blok, dan memberikan biaya kepada penambang dengan biaya yang terkait dengan transaksi yang termasuk dalam blok tersebut. Transaksi coinbase tidak dapat mereferensikan UTXO yang ada secara nyata (pada kenyataannya, ini mereferensikan UTXO fiktif), karena perannya justru untuk menciptakan sebagian nilai (subsidi) dan mendapatkan kembali sebagian lainnya (biaya), tanpa menerimanya dari transaksi sebelumnya. Agar keseluruhan sistem tetap konsisten, bagian yang sesuai dengan biaya harus sama persis dengan jumlah bitcoin yang dikonsumsi dalam input tetapi tidak dibuat ulang dalam output dalam transaksi lain di blok tersebut.



![Image](assets/fr/032.webp)



Transaksi ini tidak bersifat opsional. Sebuah blok yang tidak mengandung transaksi coinbase tidak valid dan akan ditolak secara sistematis oleh node jaringan.



⚠️ Harap diperhatikan: istilah "*coinbase*" tidak ada hubungannya dengan platform pertukaran dengan nama yang sama. Dalam Bitcoin, "*coinbase*" secara historis mengacu pada transaksi yang menciptakan reward blok. Perusahaan hanya mengadopsi istilah ini untuk namanya.



Transaksi coinbase sebenarnya memenuhi beberapa peran secara bersamaan:




- Yang pertama adalah yang baru saja kami jelaskan: memberikan kepada penambang hadiah yang menjadi hak mereka karena telah menghasilkan blok yang valid.
- Peran kedua, yang lebih teknis, adalah untuk mengaitkan komitmen kriptografi dengan saksi (tanda tangan) dari transaksi SegWit yang termasuk dalam blok tersebut.
- Peran ketiga, kali ini tidak secara langsung berhubungan dengan protokol tetapi terkait dengan industrialisasi modern mining, adalah bahwa coinbase sekarang sering digunakan untuk menambatkan data teknis sewenang-wenang. Data ini umumnya terkait dengan pengoperasian kumpulan mining dan organisasi internalnya.



Untuk membantu Anda memahami berbagai kegunaan ini, sekarang kita akan melihat lebih dekat pada struktur transaksi coinbase.



### Struktur dasar dari transaksi coinbase



Sebuah transaksi coinbase harus mengandung tepat satu input. Demi kesederhanaan, kita terkadang mengatakan bahwa transaksi tersebut tidak memiliki input, karena input ini tidak menggunakan UTXO yang sebenarnya. Pada kenyataannya, ada sebuah input dengan sumber yang direferensikan, tetapi input tersebut dengan sengaja menunjuk ke UTXO yang tidak ada.



Seperti yang telah kita lihat, setiap transaksi Bitcoin harus menggunakan UTXO sebagai input untuk membuat output yang valid. Dalam transaksi Bitcoin, konsumsi ini mengambil bentuk mereferensikan UTXO yang sudah ada sebagai input. Perujukan ini dilakukan hanya dengan menunjukkan pengenal transaksi sebelumnya (transaksi di mana UTXO dibuat), serta indeksnya di antara output transaksi ini. Secara konkret, UTXO didefinisikan oleh hash (TXID sebelumnya) dan indeks.



Namun dalam kasus transaksi coinbase, alih-alih merujuk ke UTXO yang sebenarnya, input harus mengarah ke UTXO palsu ini, dengan TXID yang penuh dengan angka nol, yang tidak sesuai dengan TXID yang sebenarnya:



```text
0000000000000000000000000000000000000000000000000000000000000000
```


Langsung diikuti oleh indeks palsu:


```text
0xffffffff
```


![Image](assets/fr/033.webp)



Dalam protokol dasar Bitcoin, seperti yang dijelaskan dalam Satoshi Nakamoto, input palsu ini adalah satu-satunya batasan yang dikenakan pada transaksi coinbase.



Seperti halnya UTXO yang direferensikan dalam input transaksi, UTXO diasosiasikan dengan bidang `scriptSig`. Dalam transaksi konvensional, bidang `scriptSig` ini berisi elemen-elemen yang diperlukan untuk memenuhi `scriptPubKey` dan dengan demikian membuka kunci UTXO yang dibelanjakan. Namun dalam kasus khusus coinbase, karena UTXO yang direferensikan adalah fiktif, maka field `scriptSig` sepenuhnya bebas. Oleh karena itu, Miner dapat memasukkan data apa pun yang mereka sukai. Kita akan melihat nanti bagaimana kebebasan ini digunakan.


Selain input yang salah ini, ada satu atau lebih output standar yang sempurna, yang memungkinkan penambang untuk mengumpulkan bitcoin dari reward pada salah satu alamat Bitcoin mereka. Keluaran ini adalah UTXO yang dikunci oleh sebuah `scriptPubKey` (contohnya, sebuah skrip yang mengarah ke alamat yang dikendalikan oleh penambang atau pool). Satu-satunya keunikan di sini terletak pada aturan untuk menghitung nilainya: jumlah total output coinbase tidak boleh melebihi subsidi maksimum yang diizinkan, yang ditambahkan dengan biaya blok.



Secara historis, transaksi coinbase dapat diringkas menjadi skema sederhana ini: input palsu yang merujuk pada UTXO yang tidak ada, dan satu atau beberapa output yang dirancang untuk mendistribusikan hadiah blok kepada penambang yang menang. Namun, saat ini, coinbase tidak lagi terbatas pada peran distribusi ini. Posisi spesialnya di dalam blok dan fleksibilitas yang tinggi dari strukturnya telah menghasilkan kegunaan baru, baik dalam protokol itu sendiri maupun dalam mekanisme manajemen pool mining.



### Penggunaan coinbase lainnya



Seiring berjalannya waktu, transaksi coinbase telah menjadi titik penyisipan yang sangat nyaman untuk mengintegrasikan berbagai informasi yang berguna untuk mining dan untuk struktur blok itu sendiri. Mari kita lihat mereka untuk lebih memahami organisasi coinbase secara keseluruhan.



#### BIP-34



[BIP-34](https://planb.academy/resources/glossary/bip0034) adalah fork soft yang digunakan pada bulan Maret 2013, dimulai dengan blok 227.930, yang memperkenalkan versi 2 blok Bitcoin. Versi baru ini mengharuskan setiap blok untuk menyertakan, dalam `scriptSig` dari transaksi coinbase, ketinggian blok yang sedang dibuat.



Di satu sisi, evolusi ini memperjelas cara di mana jaringan setuju untuk mengembangkan struktur blok dan aturan konsensus. Kedua, memastikan keunikan setiap blok dan transaksi coinbase.



Dengan demikian, `scriptSig` dari coinbase tidak sepenuhnya gratis. Sejak aktivasi BIP-34, ia hanya dibatasi untuk memulai dengan ketinggian blok di mana transaksi coinbase ini disertakan.



![Image](assets/fr/035.webp)



#### Ekstra yang tidak biasa



Seperti yang kita lihat pada bab-bab pertama kursus ini, penambang memiliki sebuah bidang nonce 32-bit pada header blok, yang dimodifikasi oleh penambang dengan cara mencoba-coba untuk menemukan sebuah hash yang kurang atau sama dengan target. Ruang 32-bit ini sudah memungkinkan sejumlah besar kombinasi untuk dieksplorasi, tetapi ketika tingkat kesulitan mining tinggi, rentang ini dapat habis dalam waktu yang relatif singkat dan dengan demikian tidak menghasilkan kombinasi yang menghasilkan hash yang valid. Jika semua nilai yang mungkin dari `nonce` telah diuji tanpa hasil, penambang harus memodifikasi elemen lain untuk mengubah header blok dan memulai serangkaian percobaan baru.



Karena transaksi coinbase menawarkan sebuah kolom bebas melalui `scriptSig` pada inputnya, solusi yang digunakan untuk memperluas ruang nonce adalah dengan mengeksploitasi bagian dari `scriptSig` ini. Ini umumnya disebut sebagai ekstra-nonce. Dengan memodifikasi extra-nonce, penambang memodifikasi `scriptSig` coinbase, yaitu pengenal transaksi, kemudian akar Merkle dari blok, dan akhirnya header blok itu sendiri. Dengan cara ini, mereka mendapatkan ruang pencarian hash yang baru untuk ditelusuri, tanpa harus memodifikasi komponen lain dari blok kandidat mereka.



![Image](assets/fr/036.webp)



#### Mengidentifikasi kolam dan penambang



Saat ini, sebagian besar hashrate di dunia diorganisir dalam pool mining. Struktur ini menyatukan para penambang individu untuk menggabungkan pekerjaan mereka dan mengurangi variasi pendapatan mereka.



Untuk alasan operasional, pool mining juga mengeksploitasi bidang bebas dari `scriptSig` input coinbase untuk menyisipkan berbagai informasi. Ini bervariasi dari satu pool ke pool lainnya dan dari protokol jaringan ke protokol jaringan lainnya, tetapi secara umum termasuk pengenal unik (seringkali sebuah nonce tambahan yang terstruktur ke dalam beberapa sub-bagian) yang ditugaskan ke setiap penambang, untuk menghindari duplikasi pekerjaan di dalam pool. Tag identifikasi pool biasanya ditambahkan, yang digunakan untuk atribusi publik terhadap blok yang ditemukan, statistik mining, dan tujuan pelacakan lainnya.



![Image](assets/fr/037.webp)



#### Komitmen SegWit



Sejak SegWit soft fork diaktifkan pada tahun 2017, data saksi (yaitu umumnya tanda tangan) telah dipisahkan dari data master transaksi, terutama untuk memperbaiki masalah [kelenturan transaksi Bitcoin](https://planb.academy/resources/glossary/malleability-transaction). Oleh karena itu, pemisahan ini memperkenalkan elemen baru yang akan dilakukan dalam blok.



Untuk melakukan ini, saksi-saksi dikelompokkan bersama dalam pohon Merkle khusus lainnya, yang akarnya kemudian dikomitmenkan ke transaksi coinbase melalui output `OP_RETURN`.



![Image](assets/fr/038.webp)



Saya tidak akan membahas mekanisme ini secara lebih rinci dalam kursus ini, karena ini berada di luar cakupan artikel ini, tetapi ingatlah bahwa sejak diperkenalkannya SegWit, transaksi coinbase berfungsi sebagai sarana untuk menambatkan sidik jari di blok yang merangkum semua saksi SegWit. Saksi-saksi ditempatkan di pohon Merkle independen, akar dari pohon ini ditulis ke output dari transaksi coinbase, dan transaksi coinbase ini sendiri termasuk dalam pohon Merkle utama bersama dengan semua transaksi lainnya, yang akarnya muncul di header blok. Ini adalah bagaimana saksi, yang disimpan secara terpisah dari data transaksi utama, masih berkomitmen pada header blok.



![Image](assets/fr/039.webp)



#### Pesan sewenang-wenang



Karena `scriptSig` mengizinkan penyisipan bebas dari informasi yang dipilih oleh penambang, beberapa orang telah mengambil keuntungan dari kesempatan ini untuk menambahkan pesan yang lebih bersifat pribadi, daripada pesan teknis. Kasus yang paling terkenal tentu saja adalah Satoshi Nakamoto, dengan pesannya yang sekarang menjadi ikon:



> The Times 03/Jan/2009 Kanselir di ambang dana talangan kedua untuk bank

Pesan ini, yang ada di blok Genesis (blok pertama dari Bitcoin) sebenarnya dikodekan dalam bentuk heksadesimal dalam `scriptSig` pada transaksi coinbase:



```text
5468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73
```


![Image](assets/fr/034.webp)



### Periode jatuh tempo


Setelah blok ditambang dan didistribusikan, transaksi coinbase muncul di blockchain seperti transaksi lainnya. Transaksi ini menciptakan UTXO untuk penambang yang menang, yang memungkinkan mereka untuk mengumpulkan hadiah mereka. Akan tetapi, UTXO ini tidak dapat langsung dibelanjakan: UTXO ini memiliki [masa jatuh tempo](https://planb.academy/resources/glossary/maturity-period). Jatuh tempo ini ditetapkan pada 100 blok setelah blok yang berisi coinbase. Secara konkret, transaksi coinbase harus berjumlah 101 konfirmasi agar hasilnya dapat dibelanjakan oleh penambang yang menang.


![Image](assets/fr/040.webp)


Tujuan dari aturan ini adalah untuk membatasi dampak dari reorganisasi chain terhadap ekonomi. Seperti yang telah kita lihat pada bab-bab sebelumnya, bisa saja terjadi pada ketinggian yang sama, dua blok valid yang berbeda ditemukan hampir secara bersamaan oleh penambang yang berbeda. Untuk sesaat, jaringan dapat terpecah: beberapa node menerima blok A terlebih dahulu, sementara yang lain melihat blok B terlebih dahulu. Kemudian, selama blok-blok berikutnya, salah satu dari dua cabang tersebut mengumpulkan lebih banyak pekerjaan dan menjadi cabang referensi. Cabang lainnya ditinggalkan dan bloknya menjadi usang. Transaksi yang ada di dalamnya kemudian, secara teori, dapat kembali ke mempool menunggu konfirmasi.



Dalam praktiknya, hal ini jarang terjadi, karena pasar biaya sering kali menghasilkan transaksi yang hampir sama muncul di dua blok yang bersaing pada ketinggian yang sama. Ini adalah salah satu alasan mengapa transaksi Bitcoin biasanya dianggap tidak dapat diubah setelah enam konfirmasi: reorganisasi lebih dari enam blok sangat kecil kemungkinannya sehingga dapat dianggap tidak mungkin.



![Image](assets/fr/041.webp)



Masalah dengan reorganisasi ini dalam kasus transaksi coinbase adalah bahwa ini bukan transaksi biasa. Transaksi ini memperkenalkan bitcoin baru ke dalam sirkulasi. Jika hadiah blok dapat dihabiskan dengan segera, situasi kaskade yang bermasalah dapat muncul:




- seorang penambang membelanjakan bitcoin dari coinbase,
- bitcoin ini beredar dalam perekonomian,
- kemudian blok asli akhirnya ditinggalkan selama reorganisasi.



Bitcoin yang beredar tidak akan pernah ada dalam rantai akhir, dan serangkaian transaksi yang valid pada saat diterbitkan akan menjadi tidak valid secara a posteriori.



Periode jatuh tempo memberikan jangka waktu yang cukup lama sehingga membuat skenario ini tidak realistis. Reorganisasi 101 blok dianggap, dalam praktiknya, tidak mungkin dilakukan (meskipun kemungkinannya sangat kecil). Kami tidak tahu persis mengapa Satoshi memilih nilai jatuh tempo yang tinggi, tetapi kemungkinan besar hal ini dipilih agar mekanisme akan tetap berfungsi, bahkan jika terjadi kerusakan jaringan yang besar.



Aturan ini mencegah uang block-reward yang baru dibuat untuk mulai beredar sebelum blok yang generated telah terkubur dengan aman di bawah sejumlah besar akumulasi pekerjaan.



---

Sekarang kita telah sampai pada akhir penjelasan tentang cara kerja Bitcoin mining. Anda sekarang harus memiliki gambaran yang jelas tentang mekanisme dasar yang terlibat.



Pada bagian terakhir dari kursus ini, kita akan kembali ke aspek yang lebih konkret, untuk menunjukkan kepada Anda bagaimana Bitcoin mining terwujud di dunia nyata: industrialisasinya, mesin yang digunakan, pengelompokan pemain, dan sebagainya. Tujuannya adalah untuk memberi Anda pandangan keseluruhan tentang Bitcoin mining, baik dari perspektif teori dan protokol yang baru saja kita lihat, dan juga dari sisi praktis dan operasionalnya.



# Industri Bitcoin mining


<partId>906a6e18-4718-4a1f-85f5-18854cebdf7c</partId>



## Evolusi mesin mining


<chapterId>2d2f9055-75fd-4630-b493-a577d708a39f</chapterId>



Pada masa-masa awal Bitcoin, mining bukanlah sebuah aktivitas industri. Itu adalah bagian dari perangkat lunak Bitcoin, yang diluncurkan pada komputer pribadi, sering kali karena rasa ingin tahu, kadang-kadang untuk mendukung jaringan, dan kedua untuk mendapatkan bitcoin yang pada saat itu tidak memiliki nilai pasar.



Selama bertahun-tahun, aktivitas ini telah mengalami transformasi: mesin telah berubah, tingkat kesulitannya telah meledak, dan mining telah menjadi sebuah industri tersendiri. Mari kita lihat aspek operasional Bitcoin mining.



### Memulai: mining dengan CPU



Pada tahun 2009 dan di tahun-tahun awal, mining terutama dilakukan dengan menggunakan CPU komputer konvensional. Bitcoin saat itu hanyalah sebuah perangkat lunak sederhana, yang berfungsi sebagai wallet, node, dan penambang. Cukup dengan menjalankan perangkat lunak Satoshi Nakamoto di komputer pribadi Anda sudah cukup untuk berpartisipasi dalam proses mining dan, dalam banyak kasus, menemukan blok.



CPU dapat melakukan segalanya, tetapi tidak dioptimalkan untuk apa pun. CPU menjalankan instruksi yang sangat umum, dengan logika yang rumit. Untuk tugas seperti hashing berulang-ulang pada header blok, ini bukanlah alat yang ideal, tetapi pada saat start-up jaringan, tingkat kesulitannya sangat rendah sehingga lebih dari cukup untuk menemukan blok.



Periode ini penting, karena mengingatkan kita akan suatu hal yang penting: proof of work tidak bergantung pada kategori peralatan tertentu. Yang penting adalah kemampuan untuk menghitung hash lebih cepat daripada yang lain, dengan biaya tertentu. Segera setelah keuntungan teknis muncul, secara otomatis berubah menjadi keuntungan ekonomi. Tetapi secara absolut, saat ini masih mungkin untuk mencoba menemukan blok Bitcoin menggunakan CPU konvensional. Ini adalah pendekatan yang diadopsi oleh proyek NerdMiner, sebagai contohnya. Peluang untuk menemukan blok hampir tidak ada, tetapi masih ada kemungkinan yang sangat kecil.



https://planb.academy/tutorials/mining/hardware/nerdminer-c9826fd9-c2b4-4d1e-8c78-809122de1654

### Beralih ke GPU



Tak lama kemudian, para penambang menyadari bahwa hambatannya bukanlah daya, tetapi kemampuan untuk melakukan sejumlah besar operasi serupa secara paralel. Inilah yang dapat dilakukan oleh unit pemrosesan grafis (GPU). Pada awalnya, GPU dirancang untuk melakukan operasi yang sama pada data dalam jumlah besar. Arsitektur ini sangat cocok untuk tugas seperti pengacakan berulang: alih-alih memiliki beberapa inti yang sangat serbaguna, Anda memiliki ratusan, bahkan ribuan unit yang mampu menjalankan instruksi yang sama secara bersamaan.



Dengan konsumsi daya yang sebanding, GPU dapat menghasilkan jauh lebih banyak hash per detik daripada CPU. Pada saat yang sama, bitcoin memiliki nilai tukar terhadap dolar, nilainya meningkat, dan platform pertukaran bermunculan. Sejak saat itu, sifat mining mulai berubah. Ini bukan lagi tentang berpartisipasi, tetapi tentang menghasilkan uang. Konfigurasi khusus muncul: mesin yang dibangun di sekitar beberapa kartu grafis, terkadang tanpa layar, dengan sistem minimal dan perangkat lunak khusus, yang tujuan utamanya adalah untuk menambang.



Pada titik inilah kesulitan mining mulai meledak. Antara pertengahan 2010 dan pertengahan 2011, bahkan meningkat hingga 1.000 kali lipat. Secara mekanis, spesialisasi dimulai, seperti bentuk awal industrialisasi, dan pengguna biasa - yang puas menjalankan perangkat lunak Bitcoin di komputer pribadi mereka - sekarang hanya memiliki peluang yang sangat kecil untuk menemukan blok yang valid.



![Image](assets/fr/044.webp)



*Sumber: [CoinWarz.com](https://www.coinwarz.com/mining/bitcoin/hashrate-chart)*



Di antara era GPU dan era [ASIC](https://planb.academy/resources/glossary/asic) modern, terdapat fase peralihan: penggunaan FPGA. FPGA adalah komponen yang dapat diprogram ulang: dapat dikonfigurasikan untuk secara langsung mengimplementasikan sirkuit logika yang didedikasikan untuk perhitungan tertentu, dalam hal ini `SHA256d`. Idenya adalah untuk bergerak lebih jauh lagi dari perangkat keras serba guna (CPU/GPU) untuk mendapatkan efisiensi energi. Namun tak lama kemudian, perbaikan yang dilakukan secara virtual pada FPGA akan diterapkan secara fisik pada chip itu sendiri: itulah kedatangan ASIC.



### Kedatangan ASIC



Tahap terakhir dalam spesialisasi perangkat keras mining adalah kemunculan ASIC (*Sirkuit Terpadu Khusus Aplikasi*). ASIC adalah chip yang didesain untuk satu tugas. Dalam kasus Bitcoin mining, tugas ini tepatnya adalah menjalankan `SHA256d` pada kecepatan maksimum dan dengan efisiensi energi yang optimal. Tidak seperti GPU, ASIC tidak digunakan untuk menjalankan game, rendering 3D, atau AI. Ini untuk hashing, dan hanya itu.



![Image](assets/fr/045.webp)



*ASIC S21 XP diproduksi oleh Bitmain*



Spesialisasi ini memiliki dua konsekuensi utama:




- Yang pertama adalah lompatan dalam performa dan efisiensi. Untuk perangkat dengan generasi yang sebanding, ASIC menghasilkan jauh lebih banyak hash per detik daripada GPU, namun mengonsumsi lebih sedikit daya. Mining dengan GPU dengan cepat menjadi tidak kompetitif: meskipun secara teknis berfungsi, biaya listrik jauh lebih besar daripada pendapatan yang diharapkan dalam sebagian besar konteks;
- Yang kedua adalah perubahan model: investasi terutama bergeser ke perangkat keras kelas industri. Mining sekarang melibatkan pembelian mesin yang dirancang untuk tujuan ini, menyalakannya secara terus menerus, mendinginkannya, memeliharanya, dan menyerap keusangannya. Karena ASIC tidak abadi secara ekonomi: ketika generasi baru yang lebih efisien masuk ke pasar, mesin-mesin lama menjadi semakin tidak menguntungkan, meskipun tetap berfungsi.



Sejak saat itu, kita tidak lagi hanya berbicara tentang hobi. Kita berbicara tentang sebuah sektor di mana daya saing bergantung pada sebuah persamaan:




- biaya listrik;
- biaya peralatan dan penyusutan;
- kemampuan untuk mendinginkan dan beroperasi dalam skala besar;
- ketersediaan dan keandalan alat berat;
- kecepatan komunikasi;
- dll.



### Peternakan Mining



Mesin yang terisolasi dapat menambang, tetapi dengan mengelompokkan ratusan, kemudian ribuan ASIC di satu lokasi, kami berbagi biaya tetap, mengoptimalkan logistik, dan bergerak lebih dekat ke model pusat data khusus.



Sebuah [peternakan mining](https://planb.academy/resources/glossary/mining-farm), dalam bentuk yang paling sederhana, adalah sebuah bangunan (atau sekumpulan kontainer) yang diisi dengan ASIC yang beroperasi 24/7. Tantangannya sekarang adalah mempertahankan kondisi operasi yang stabil:




- memasok sejumlah besar daya listrik yang murah dan stabil;
- mengelola panas untuk menghindari pelambatan, karena kepadatan energinya cukup besar;
- menyaring debu, mengontrol kelembapan, membersihkan;
- pemantauan kinerja alat berat secara real-time (suhu, kesalahan perangkat keras, penurunan hashrate, dll.).



![Image](assets/fr/043.webp)



*Salah satu dari tujuh bangunan yang didedikasikan untuk Bitcoin mining di lokasi Rockdale Riot Platforms, dekat Austin, Texas. Yang satu ini secara khusus didedikasikan untuk perendaman mining*



Mining sekarang digerakkan oleh para pemain industri, beberapa di antaranya terdaftar di bursa saham, yang membangun dan mengoperasikan tambak berskala sangat besar. Ini termasuk MARA Holdings (Nasdaq: `MARA`) dan Riot Platforms (Nasdaq: `RIOT`).



![Image](assets/fr/042.webp)



Bahkan tanpa membahas detail model profitabilitas, penting untuk memahami mengapa mining mengambil bentuk ini. Proof-of-work adalah mekanisme yang kompetitif: probabilitas untuk menemukan sebuah blok, dan oleh karena itu menghasilkan uang, sebanding dengan bagian hashrate yang Anda gunakan. Akibatnya, ada tekanan konstan untuk meningkatkan daya komputasi, mengurangi biaya per unit komputasi, dan membatasi kerugian. Akibatnya, lingkungan yang menawarkan listrik lebih murah, iklim yang kondusif untuk pendinginan, atau infrastruktur energi yang melimpah, secara alami menjadi lebih menarik.



Dengan demikian, Mining Bitcoin telah berevolusi dari aktivitas yang dapat diakses oleh siapa saja pada masa-masa awalnya, menjadi aktivitas yang didominasi oleh peralatan khusus dan operasi profesional. Hal ini tidak mengubah aturan protokol. Secara teori, siapa pun dapat menambang dengan mesin apa pun. Namun dalam praktiknya, tingkat kesulitan dan efisiensi ASIC telah membuat mining domestik menjadi tidak kompetitif dalam banyak konteks.



Tentu saja, masih ada situasi di mana rumah mining dapat menarik, misalnya jika Anda mendapatkan keuntungan dari listrik yang sangat murah, atau jika Anda menggunakan panas generated oleh penambang Anda untuk menghangatkan rumah Anda di musim dingin. Tetapi bagaimanapun juga, Anda tetap harus membeli mesin yang dilengkapi dengan chip ASIC. Terlebih lagi, karena daya mining Anda akan tetap sangat kecil dibandingkan dengan jaringan Bitcoin, Anda harus menemukan cara untuk mengurangi varians pendapatan Anda: inilah peran pool mining, yang akan kita bahas pada bab selanjutnya.



Jika Anda ingin menjelajahi solusi mining rumahan dengan pemulihan panas, kami memiliki tutorial tentang berbagai alat, baik yang siap pakai maupun yang dapat dibuat sendiri:



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

https://planb.academy/tutorials/mining/hardware/attakai-0d177e6b-e167-4b25-8e38-4ec74213d1fb

## Pengelompokan ke dalam kumpulan mining


<chapterId>c871bece-eebe-4ef4-9789-d47251f16c8b</chapterId>



Mining Bitcoin melibatkan biaya yang berkelanjutan dan tidak dapat dihindari, yang paling utama adalah konsumsi daya mesin. Biaya-biaya ini dikeluarkan secara independen dari hasil apa pun, meskipun pendapatan dari mining pada dasarnya bersifat langka dan acak. Penemuan sebuah blok bergantung secara eksklusif pada bagian penambang dari hashrate, yang membuat pendapatan semakin tidak dapat diprediksi jika bagian tersebut semakin kecil. Masalah praktis inilah yang dengan cepat menyebabkan meluasnya penggunaan [pool mining](https://planb.academy/resources/glossary/pool-mining). Pada bab terakhir dari kursus MIN 101 ini, saya akan memberikan pengantar tentang prinsip-prinsip dan pengoperasian pool mining di Bitcoin.



### Apa yang dimaksud dengan kolam mining?



mining pool adalah sebuah organisasi (biasanya berupa layanan online) yang menggabungkan kekuatan komputasi dari banyak penambang independen, untuk meningkatkan frekuensi kelompok mereka menemukan blok. Ketika pool menemukan sebuah blok, hadiah blok tersebut kemudian didistribusikan kembali di antara para peserta sesuai dengan aturan internal pool (yang akan dibahas dalam kursus MIN 201, karena aturan tersebut terlalu rumit untuk MIN 101).



Peserta dalam pool mining kemudian sering disebut sebagai "[hashers](https://planb.academy/resources/glossary/hasher)", bukan sebagai "penambang", karena mereka tidak lagi melakukan semua pekerjaan mining, tetapi hanya meng-hash data yang dikirimkan kepada mereka oleh pool.



Berhati-hatilah untuk tidak mengacaukan kolam mining dengan tambak mining. Ini adalah dua konsep yang berbeda. Seperti yang telah kita lihat pada bab sebelumnya, sebuah farm adalah lokasi fisik di mana satu entitas mengoperasikan banyak mesin mining. Di sisi lain, sebuah pool, di atas segalanya, merupakan pengelompokan virtual: ribuan mesin, yang sering kali tersebar secara geografis, bekerja di bawah koordinasi yang sama. Namun, sebuah farm dapat, dan sering kali, berpartisipasi dalam sebuah pool.



![Image](assets/fr/048.webp)



### Mengurangi varians pendapatan



Jadi, mengapa bergabung dengan sebuah pool? Sederhananya karena hasil dari aktivitas mining bersifat probabilistik: pada setiap percobaan hash, ada kemungkinan yang sangat kecil bahwa hash tersebut akan memenuhi target kesulitan dan oleh karena itu menghasilkan blok yang valid.



Dalam jangka waktu yang sangat panjang, penghasilan rata-rata Anda harus sebanding dengan bagian Anda dari keseluruhan hashrate. Prinsip ini mengikuti secara langsung hukum probabilitas: setiap perhitungan hash merupakan pengundian acak yang independen, dan, berdasarkan hukum bilangan besar, frekuensi Anda menemukan blok akan menyatu secara matematis terhadap bagian Anda dari total hashrate jaringan. Namun, dalam jangka pendek hingga menengah, penghasilan Anda yang sebenarnya bisa sangat tidak teratur. Perbedaan antara rata-rata teoretis dan kenyataan acak inilah yang kita sebut **varians** dalam matematika.



Berikut ini adalah contoh sederhana untuk mengilustrasikan prinsip tersebut:




- Jaringan Bitcoin menghasilkan rata-rata 144 blok per hari (sekitar satu blok setiap 10 menit);
- Jika Anda memiliki `0,0001%` dari total hashrate, ekspektasi Anda adalah `144 × 0,000001`, atau `0,000144` blok/hari;
- Dengan kata lain, Anda harus menemukan satu blok rata-rata setiap `1 / 0.000144` hari, yaitu setiap 6.944 hari, atau sekitar 19 tahun.



Namun nilai ini hanya sesuai dengan ekspektasi matematis: distribusi waktu penemuan mengikuti hukum acak, sehingga sangat mungkin, dalam praktiknya, tidak pernah menemukan satu blok pun, bahkan dalam jangka waktu yang sangat lama. Anda bisa saja tidak beruntung dan tidak menemukan apa pun untuk waktu yang sangat lama, sementara Anda harus membayar biaya berulang (listrik, perawatan, penyusutan peralatan...).



Kumpulan mining mengubah sifat dari masalah ini: dengan menggabungkan hashrate, kumpulan ini akan lebih sering menemukan blok. Setiap peserta kemudian setuju untuk menerima sebagian kecil dari setiap blok yang ditemukan, tetapi lebih sering. Ini adalah transformasi dari pendapatan yang sangat tidak stabil dan berjarak jauh menjadi pendapatan yang lebih teratur, dengan biaya berbagi hadiah dan membayar biaya layanan.



### Mengapa varians menurun ketika Anda mengelompokkan bersama?



Semakin tinggi daya komputasi Anda, semakin tinggi frekuensi yang Anda harapkan dari blok yang ditemukan. Lebih penting lagi, semakin sering kejadiannya, semakin dekat hasil yang diamati dengan rata-rata statistik selama periode tertentu.



Dalam skala solo, seorang penambang skala kecil dapat pergi selama bertahun-tahun tanpa satu blok pun, kemudian mendapatkan pembayaran besar pada suatu hari, lalu tidak mendapatkan apa-apa. Dalam sebuah pool, realitas probabilistik yang sama masih berlaku, tetapi dihaluskan dalam skala kolektif: pool menemukan blok lebih sering, dan redistribusi mengubah peristiwa ini menjadi pembayaran yang lebih teratur untuk setiap peserta. **Oleh karena itu, pool mining menjual prediktabilitas pada aktivitas mining**.



### Landmark bersejarah



Seperti yang telah kita lihat pada bab sebelumnya, pada awalnya, mining dapat dilakukan secara solo dengan komputer konvensional, karena tingkat kesulitannya sangat rendah. Namun, seiring dengan meledaknya hashrate global (GPU, kemudian ASIC), solo mining menjadi pertaruhan yang sangat menyita waktu bagi sebagian besar peserta.



Kolam-kolam pertama dibuat sebagai tanggapan atas kenyataan baru ini. Braiins Pool (sebelumnya bernama Slush Pool / Bitcoin.cz) adalah pool Bitcoin mining yang pertama: pool ini menambang blok pertamanya pada tanggal 16 Desember 2010. Keberhasilan pool mining pertama ini sangat cepat, karena hanya dalam beberapa hari saja, pool ini berhasil mendapatkan hampir 3,5% dari hashrate global.



![Image](assets/fr/047.webp)



Di sisi teknis, pool kemudian disusun berdasarkan protokol komunikasi khusus antara pool dan penambang (misalnya [Stratum](https://planb.academy/resources/glossary/stratum), kemudian Stratum V2), untuk mengatur pekerjaan yang terdistribusi secara efisien. Kita akan melihat lebih dekat konsep-konsep ini dalam kursus pelatihan MIN 201.



### Situasi modern



Pada saat penulisan (awal 2026), Bitcoin hashrate global berada pada urutan besarnya zetta-hash per detik (= 1.000 EH/s = 1.000.000.000.000.000 hash per detik), dan hampir semua blok yang ditemukan berasal dari pool mining.



Berikut ini adalah peringkat, hingga saat ini, dari pool mining utama dan bagian masing-masing dari hashrate. Peringkat ini kemungkinan besar akan berubah pada saat Anda membaca kursus ini. Untuk data terbaru, silakan kunjungi [mempool.space](https://mempool.space/graphs/mining/pools).



![Image](assets/fr/046.webp)



| Ranking    | Pool           | Blocks found  | Hashrate share   |
| ---------: | -------------- | ------------: | ---------------: |
|          1 | Foundry USA    |          1297 |           29.57% |
|          2 | AntPool        |           755 |           17.21% |
|          3 | ViaBTC         |           514 |           11.72% |
|          4 | F2Pool         |           467 |           10.65% |
|          5 | SpiderPool     |           349 |            7.96% |
|          6 | MARA Pool      |           229 |            5.22% |
|          7 | SECPOOL        |           197 |            4.49% |
|          8 | Luxor          |           128 |            2.92% |
|          9 | Binance Pool   |           105 |            2.39% |
|         10 | OCEAN          |            78 |            1.78% |
|         11 | SBI Crypto     |            70 |            1.60% |
|         12 | Braiins Pool   |            54 |            1.23% |
|         13 | WhitePool      |            33 |            0.75% |
|         14 | Mining Squared |            26 |            0.59% |
|         15 | BTC.com        |            16 |            0.36% |
|         16 | Poolin         |            14 |            0.32% |
|         17 | ULTIMUSPOOL    |            14 |            0.32% |
|         18 | GDPool         |            12 |            0.27% |
|         19 | Innopolis Tech |            11 |            0.25% |
|         20 | NiceHash       |             8 |            0.18% |
|         21 | RedRock Pool   |             8 |            0.18% |
|         22 | Unknown        |             2 |            0.05% |
|         23 | Public Pool    |             1 |            0.02% |

*Sumber [mempool.space] (https://mempool.space/graphs/mining/pools), data satu bulan, 16 Desember 2025 hingga 16 Januari 2025.*



Dalam kursus yang lebih lanjut, kita akan membahas lebih jauh mengenai cara kerja internal pool (saham, protokol jaringan, metode pembayaran...), karena di sinilah detail yang menentukan profitabilitas penambang dan implikasi potensial untuk Bitcoin berperan.



---

Sekarang kita telah sampai pada bagian akhir dari MIN 101. Terima kasih telah mengikutinya hingga akhir. Jika Anda ingin menilai keterampilan yang telah Anda peroleh selama kursus, ujian akhir menanti Anda di bagian selanjutnya.



Dengan pengetahuan dasar yang baru saja Anda peroleh, Anda sekarang dapat mengambil kursus yang lebih lanjut tentang mining di Plan ₿ Academy, baik secara teori, seperti yang satu ini, atau kursus yang lebih praktis, sehingga Anda juga dapat mulai berpartisipasi dalam Bitcoin mining!



# Bagian akhir


<partId>eced8ca1-971d-4a22-9254-dbf8bce15d1b</partId>



## Ulasan & Peringkat


<chapterId>dc005a96-f4b4-42be-ab72-d4624c110716</chapterId>


<isCourseReview>true</isCourseReview>

## Ujian akhir


<chapterId>959f06cf-fd66-4f29-b7ee-665bfedfea0d</chapterId>


<isCourseExam>true</isCourseExam>

## Kesimpulan


<chapterId>f16a4e42-c16e-466b-ad16-f42b5360f510</chapterId>


<isCourseConclusion>true</isCourseConclusion>