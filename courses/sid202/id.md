---
name: Membangun dengan Elemen dan Jaringan Cair
goal: Belajar menggunakan dan mengembangkan dengan platform blockchain sumber terbuka Elements dan fitur-fitur utamanya
objectives: 

  - Memahami konsep dasar platform blockchain Elements dan sidechain Liquid.
  - Pelajari cara menyiapkan dan menjalankan node Elements untuk konfigurasi mandiri dan sidechain.
  - Dapatkan pengalaman praktis dengan penandatanganan blok federasi dan Federated 2-Way Peg.
  - Mengatur dan mengelola lingkungan blockchain yang aman dan efisien untuk kasus penggunaan di dunia nyata.

---
# Bangun di atas Cairan dan Elemen

Temukan fitur-fitur canggih dan kemampuan Liquid dan Elements, dan pelajari cara menggunakan alat ini secara efektif untuk meningkatkan proyek pengembangan Anda. Pelatihan ini memberikan landasan teori dan praktik yang lengkap, memungkinkan Anda untuk menguasai fitur-fitur seperti Transaksi Rahasia, Aset yang Diterbitkan, dan Penandatanganan Blok Federasi.

Liquid, berdasarkan kerangka kerja Elements, dirancang untuk meningkatkan privasi, skalabilitas, dan fungsionalitas untuk solusi keuangan dan teknis. Dalam kursus ini, Anda akan mendapatkan pengalaman langsung dengan penerbitan dan manajemen aset, Federated 2-Way Peg, dan penggunaan alat seperti elementsd dan elements-cli, yang memberdayakan Anda untuk membuat solusi inovatif yang disesuaikan dengan kebutuhan Anda.

Kursus ini dirancang untuk para pengembang dari semua tingkat pengalaman. Pengguna pemula dan menengah akan menemukan penjelasan yang mudah dipahami dan contoh-contoh praktis, sementara pengguna tingkat lanjut dapat mempelajari lebih dalam tentang detail teknis dan fitur-fitur yang kurang dikenal dari Liquid dan Elements.

Bergabunglah bersama kami untuk meningkatkan keterampilan Anda, membuka potensi penuh Liquid dan Elements, dan menciptakan alat yang berdampak bagi masa depan inovasi Liquid.

+++
# Pendahuluan

<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>

## Pengenalan Kursus

<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>

![Video](https://youtu.be/gkQfnwYLyI0?si=H6cIPhgZaSAwHaHI)

Tujuan dari Elements Academy adalah untuk memperkenalkan dan menjelaskan konsep-konsep utama Elements, platform sumber terbuka yang menjadi dasar dari Liquid. Pada akhir kursus, Anda akan memiliki pemahaman yang baik tentang fitur utama Elements, seperti Transaksi Rahasia dan Aset yang Diterbitkan, dan proses yang terlibat dalam menjalankan Elements Core.

Setiap bagian akan memiliki pelajaran dengan teks penjelasan dan video yang diakhiri dengan kuis. Jumlah pertanyaan berhubungan dengan ukuran topik sebelumnya. Bagian 10 akan merangkum konten kursus dan diakhiri dengan kuis yang lebih besar.

Setiap pertanyaan, permintaan informasi tambahan, atau pertanyaan mengenai jawaban kuis dapat ditujukan kepada guru Anda, James Dorfman.

## Ikhtisar Elemen

<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>

![Video](https://youtu.be/ns-JLGdkNig?si=fmWye_boRSvVF1Bt)

Elements adalah platform blockchain open source berkemampuan sidechain, yang menyediakan akses ke fitur-fitur canggih yang dikembangkan oleh anggota komunitas, seperti Transaksi Rahasia dan Aset yang Diterbitkan.

Elements, pada intinya, merupakan sebuah protokol yang memungkinkan konsensus dibentuk di sekitar riwayat transaksi dan aturan yang mengatur transfer dan pembuatan aset yang disimpan dalam buku besar blockchain yang terdistribusi.

Informasi latar belakang lebih lanjut tentang Elements dapat ditemukan dengan mudah di situs web Elements Project (https://elementsproject.org/), blog resmi Liquid (https://blog.liquid.net/), dan portal pengembang (https://liquid.net/devs).

### Elemen

Diluncurkan pada tahun 2015, Elements mengurangi biaya pengembangan dan penelitian internal serta memanfaatkan teknologi blockchain terbaru, membuka banyak kasus penggunaan baru untuk implementasi. Blockchain berbasis Elements dapat beroperasi sebagai Blockchain mandiri atau dipasangkan ke Blockchain lain dan dijalankan sebagai Sidechain. Menjalankan Elements sebagai Sidechain memungkinkan aset ditransfer secara terverifikasi di antara blockchain yang berbeda.

Dibangun di atas dan memperluas basis kode Bitcoin, ini memungkinkan pengembang yang terbiasa dengan API bitcoind dengan cepat dan hemat biaya untuk membuat blockchain yang berfungsi dan menguji proyek-proyek bukti konsep. Dibangun di atas basis kode Bitcoin juga memungkinkan Elements untuk berfungsi sebagai testbed untuk perubahan pada protokol Bitcoin itu sendiri.

Sebagian fitur utama Elements tercantum di bawah ini.

#### Transaksi Rahasia

Secara default, semua alamat di Elements dibutakan menggunakan Transaksi Rahasia. Penyembunyian adalah proses di mana jumlah dan jenis aset yang ditransfer disembunyikan secara kriptografis dari semua orang, kecuali peserta dan mereka yang mereka pilih untuk mengungkapkan kunci penyembunyian.

#### Aset yang Diterbitkan

Aset yang Diterbitkan pada Elemen memungkinkan beberapa jenis aset untuk diterbitkan dan ditransfer di antara peserta jaringan. Aset yang Diterbitkan juga mendapat manfaat dari Transaksi Rahasia dan dapat diterbitkan kembali atau dimusnahkan oleh siapa pun yang memegang token penerbitan ulang yang relevan.

#### Pasak 2 Arah Federasi

Elements adalah sebuah platform blockchain tujuan umum yang juga dapat "dipasangkan" ke blockchain yang sudah ada (seperti Bitcoin) untuk memungkinkan transfer aset dua arah dari satu rantai ke rantai lainnya. Menerapkan Elements sebagai sidechain memungkinkan Anda untuk mengatasi beberapa properti yang melekat pada chain utama, sambil mempertahankan tingkat keamanan yang baik yang disediakan oleh aset yang diamankan pada chain utama.

#### Blok yang Ditandatangani

Elements menggunakan Federasi penandatangan yang kuat, yang disebut Penandatangan Blok, yang menandatangani dan membuat blok dengan cara yang dapat diandalkan dan tepat waktu. Hal ini menghilangkan latensi transaksi dari proses penambangan PoW, yang tunduk pada varians waktu blok yang besar karena distribusi poissonnya yang acak. Proses Penandatanganan Blok Federasi mencapai pembuatan blok yang dapat diandalkan tanpa memperkenalkan kebutuhan akan kepercayaan pihak ketiga atau penambangan berbasis algoritma komputasi.

Elements menambahkan semua fitur ini di atas basis kode Bitcoin Core, memperluas kemampuan protokol mainchain dan memungkinkan kasus penggunaan bisnis baru ketika digunakan sebagai sidechain atau sebagai solusi blockchain mandiri.

# Elemen

<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>

## Bagaimana Elemen Bekerja

<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>

![Video](https://youtu.be/v0lzmfH81AY?si=V-xDWfmDLKyBcdPs)

Elements menyediakan solusi teknis untuk masalah yang dihadapi pengguna blockchain setiap hari; latensi transaksi, kurangnya privasi, dan risiko terhadap fungibilitas.

Elements mengatasi masalah ini melalui penggunaan Penandatanganan Blok Federasi dan Transaksi Rahasia.

Tidak seperti jaringan Bitcoin, proses penandatanganan blok dalam Elements tidak bergantung pada Dynamic Membership Multiparty Signatures (DMMS) dan Proof of Work (PoW). Sebagai gantinya, Elements menggunakan Federasi penandatangan yang kuat, yang disebut Penandatangan Blok, yang dapat menandatangani dan membuat blok dengan cara yang dapat diandalkan dan tepat waktu. Hal ini menghilangkan latensi transaksi dari proses penambangan PoW, yang tunduk pada varians waktu blok yang besar karena distribusi poissonnya yang acak. Proses Penandatanganan Blok Federasi mencapai pembuatan blok yang dapat diandalkan tanpa memerlukan kepercayaan pihak ketiga.

Elements dapat berjalan sebagai sidechain ke blockchain lain, seperti Bitcoin, atau sebagai blockchain mandiri tanpa ketergantungan pada jaringan lain.

Ketika digunakan sebagai sidechain, Strong Federation juga berisi anggota yang memungkinkan transfer aset yang aman dan terkendali antara chain utama dan sidechain Elements. Transfer aset yang terkendali disebut Federated 2-Way Peg dan anggota yang melakukan peran transfer aset disebut Watchmen.

Proses yang terlibat dalam menjalankan jaringan Elements dan peran para peserta dalam jaringan sangat penting untuk memahami cara kerja Elements.

Baik diimplementasikan sebagai sidechain atau blockchain mandiri, Elements menggunakan Federasi Penandatangan Blok yang kuat untuk menghasilkan blok.

### Federasi yang kuat

Elements menggunakan model konsensus yang pertama kali diusulkan oleh Blockstream, yang disebut Federasi Kuat. Federasi Kuat tidak membutuhkan Proof of Work (PoW) dan sebagai gantinya bergantung pada tindakan kolektif dari sekelompok peserta yang saling percaya, yang disebut Fungsionaris.

Peran yang dapat dilakukan oleh seorang Fungsionaris dalam Federasi yang Kuat adalah: Penandatangan Blok dan Penjaga. Block Signers diperlukan jika Anda menjalankan Elements dalam mode sidechain atau blockchain mandiri, sedangkan Watchmen hanya diperlukan dalam pengaturan sidechain.

Tindakan yang dapat dilakukan oleh anggota Strong Federation dibagi menjadi dua peran yang berbeda untuk meningkatkan keamanan dan membatasi kerusakan yang dapat ditimbulkan oleh penyerang.

Ketika digabungkan, peran para partisipan ini memungkinkan Elements untuk memberikan pembuatan blok yang cepat (konfirmasi transaksi yang lebih cepat dan akhir) dan aset yang terjamin dan dapat ditransfer (aset yang dipatok yang dapat dihubungkan langsung ke blockchain lain).

Anda dapat membaca whitepaper Strong Federations di sini: https://blockstream.com/strong-federations.pdf

### Penandatangan Blokir

Sebuah blockchain seperti Bitcoin diperpanjang ketika seseorang yang menjadi bagian dari kelompok dinamis penandatangan blok memperpanjang rantai dengan menunjukkan bukti kerja yang telah dilakukan. Sifat dinamis dari himpunan ini memperkenalkan masalah latensi yang melekat pada sistem tersebut.

Dengan menggunakan set penanda tangan tetap, model Federasi menggantikan set dinamis dengan set yang dikenal, skema multi-tanda tangan. Mengurangi jumlah partisipan yang dibutuhkan untuk memperluas blockchain akan meningkatkan kecepatan dan skalabilitas sistem, sementara validasi oleh semua pihak memastikan integritas riwayat transaksi.

Penandatanganan blok federasi terdiri dari beberapa fase:


- Langkah 1 - Penanda Tangan Blok mengusulkan kandidat blok secara round-robin kepada semua Penanda Tangan Blok yang berpartisipasi.
- Langkah 2 - Setiap Penandatangan Blok menandakan niat mereka dengan melakukan pra-komitmen untuk menandatangani kandidat blok yang diberikan.
- Langkah 3 - Jika ambang batas yang diberikan untuk pra-komitmen terpenuhi, setiap Penandatangan Blok menandatangani blok tersebut.
- Langkah 4 - Jika ambang batas tanda tangan (yang mungkin berbeda dengan langkah 3) terpenuhi, blok diterima dan dikirim ke jaringan. Strong Federation telah mencapai konsensus pada blok transaksi terbaru.
- Langkah 5 - Blok berikutnya kemudian diusulkan oleh Penandatangan Blok berikutnya dalam round-robin dan prosesnya berulang.

Karena pembuatan blok Strong Federation tidak bersifat probabilistik dan didasarkan pada sekumpulan penanda tangan yang tetap, maka tidak akan pernah mengalami reorganisasi multi blok. Hal ini memungkinkan pengurangan yang signifikan dalam waktu tunggu yang terkait dengan konfirmasi transaksi. Ini juga menghilangkan insentif untuk menambang demi keuntungan (yaitu, imbalan blok) dan menggantinya dengan insentif untuk berpartisipasi secara produktif dalam jaringan di mana semua peserta memiliki tujuan bersama yang sama; memastikan jaringan terus berfungsi dengan cara yang bermanfaat bagi semua. Hal ini dilakukan tanpa memperkenalkan satu titik kegagalan atau persyaratan kepercayaan yang lebih tinggi.

### Elemen sebagai Sidechain - Penjaga dan Pasak 2 Arah Federasi

Ketika dijalankan sebagai sidechain, beberapa anggota Strong Federation memiliki peran tambahan yang harus dipenuhi, yaitu Watchmen. Watchmen bertanggung jawab atas transfer aset ke dalam dan ke luar sidechain Elements, proses yang dikenal sebagai `Peg-In` dan `Peg-Out`.

Agar sidechain dapat beroperasi dengan cara yang dapat dipercaya, sidechain harus memungkinkan para partisipan untuk memverifikasi bahwa pasokan aset terkontrol dan dapat diverifikasi. Sidechain Elements menggunakan 2-Way Federated Peg untuk memungkinkan transfer aset dua arah masuk dan keluar dari blockchain Elements. Ini memenuhi persyaratan penerbitan yang dapat dibuktikan dan transfer antar-rantai.

Fitur Federated 2-way Peg memungkinkan sebuah aset untuk dapat dioperasikan dengan blockchain lain dan mewakili aset asli blockchain lain. Dengan mematok blockchain Anda ke blockchain lain, Anda dapat memperluas kemampuan blockchain utama dan mengatasi beberapa keterbatasan yang melekat.

Pada tingkat yang lebih tinggi, transfer ke dalam sidechain terjadi ketika seseorang mengirimkan aset mainchain ke alamat yang dikendalikan oleh dompet Watchmen multi-tanda tangan. Ini secara efektif membekukan aset di mainchain. Watchmen kemudian memvalidasi transaksi dan melepaskan jumlah yang sama dari aset terkait di dalam sidechain. Aset yang dilepaskan dikirim ke dompet sidechain yang dapat membuktikan klaim ke aset mainchain asli. Proses ini secara efektif memindahkan aset dari chain induk ke sidechain.

Untuk mentransfer aset kembali ke mainchain, pengguna melakukan transaksi peg-out khusus pada sidechain. Transaksi ini diperiksa oleh Watchmen yang kemudian menandatangani pengeluaran transaksi dari dompet multi-tanda tangan yang mereka kendalikan di mainchain. Sejumlah ambang batas peserta dalam federasi harus menandatangani sebelum transaksi mainchain menjadi valid. Ketika Watchmen mengirim aset kembali ke mainchain, mereka juga menghancurkan jumlah yang sesuai di sidechain, secara efektif mentransfer aset antar blockchain.

## Menyiapkan dan Menjalankan Elemen

<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>

![Video](https://youtu.be/Frr_OjTEPAM?si=iq5XonJyQk8S5OAu)

Karena Elements didasarkan pada basis kode Bitcoin, komponen-komponen yang membentuk jaringan yang berfungsi sangat mirip.

Perangkat lunak simpul Elements itu sendiri disebut `elementsd` dan berjalan sebagai daemon pada mesin pengguna. Daemon (atau layanan di Windows) adalah program yang berjalan sebagai layanan latar belakang tanpa memerlukan kontrol langsung dari pengguna yang masuk.

Catatan: Di sepanjang dokumen ini, kita akan selalu merujuk ke elementsd sebagai versi daemon, tetapi semuanya dapat dilakukan dengan elements-qt, asalkan opsi server diaktifkan.

Daemon Elements terhubung ke node lain di jaringan sehingga dapat bertukar data transaksi dan blokir, memvalidasi dan memperluas salinan lokal blockchain jaringan.

Perangkat lunak Elements juga terdiri dari sebuah program klien yang disebut `elements-cli` yang memungkinkan anda untuk mengirim perintah Remote Procedure Call (RPC) ke elementsd dari baris perintah. Ini dapat digunakan untuk menanyakan saldo dompet, melihat transaksi atau memblokir data atau menyiarkan transaksi misalnya. Pengaturan ini seharusnya tidak asing lagi bagi siapa saja yang pernah menggunakan Bitcoin yang setara; bitcoind dan bitcoin-cli.

Karena node Elements dapat dikonfigurasi dengan memasukkan parameter pada saat startup atau melalui file konfigurasi, maka dimungkinkan untuk memiliki lebih dari satu instance yang berjalan pada mesin yang sama. Hal ini berguna untuk tujuan pengujian dan pengembangan karena Anda dapat mengatur jaringan lokal Anda sendiri pada satu mesin, dengan setiap node Elements memiliki salinan data blockchain sendiri, mengelola kumpulan transaksi valid yang belum dikonfirmasi dan mendengarkan permintaan RPC pada port yang berbeda.

### Repositori dan Komunitas Kode Elemen

Elements adalah proyek sumber terbuka dan kode sumbernya dapat ditemukan di repositori GitHub Elements di https://github.com/ElementsProject/elements. Repositori ini berisi sumber untuk program elementsd dan elements-cli bersama dengan alat instalasi dan pembangunan yang mendukung, serangkaian tes dan beberapa dokumentasi instruksional.

Untuk melengkapi repositori kode, ada juga situs web https://elementsproject.org, sumber daya yang berfokus pada komunitas yang berisi penjelasan tentang apa itu Elements, bagaimana cara kerjanya, dan bagian tutorial yang komprehensif. Tutorial ini berfokus pada pembelajaran tentang Elements dengan mengikuti contoh-contoh baris perintah dan menunjukkan kepada Anda bagaimana membangun aplikasi desktop dan web sederhana di atasnya. Situs ini juga mencantumkan forum diskusi komunitas Elements yang populer dan dihosting di GitHub, sehingga memungkinkan kontribusi komunitas untuk dibuat pada konten situs.

Untuk menjalankan Elements pada komputer Anda, pertama-tama Anda harus mengkloning (mengunduh salinan) kode sumber, menginstal semua dependensi yang dimiliki kode tersebut, dan akhirnya membangun daemon dan eksekusi klien. Perangkat lunak Elements kemudian siap untuk dikonfigurasi dan dijalankan.

## Mengkonfigurasi Node dan Jaringan

<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>

Pengaturan konfigurasi dapat diteruskan ke node Elements pada saat startup untuk mengubah cara kerjanya, memvalidasi data, menghubungkan ke node lain, dan menginisialisasi data blockchain-nya.

Pengaturan dapat dimuat dari file `elements.conf` yang ditunjuk atau dimasukkan sebagai parameter melalui baris perintah.

Sebagian hal dapat diubah dengan menggunakan parameter ini:


- Nama aset default yang digunakan dalam implementasi blockchain mandiri.
- Jumlah aset awal yang dibuat.
- Aset yang akan digunakan saat membayar biaya transaksi di jaringan.
- Lokasi penyimpanan file data blockchain.
- Kredensial RPC yang digunakan untuk terhubung ke node Bitcoin.
- Ambang batas `n dari m` yang harus dipenuhi dan kunci publik yang valid yang dapat menandatangani blok.
- Skrip yang harus dipenuhi untuk mentransfer aset masuk dan keluar dari sidechain.
- Apakah akan terhubung ke node Bitcoin sebagai sidechain atau tidak.

Banyak dari aturan ini merupakan bagian dari aturan konsensus jaringan, sehingga penting untuk diterapkan di semua node pada saat startup. Beberapa dapat diubah setelah rantai diinisialisasi, tetapi beberapa perlu diperbaiki setelah digunakan untuk menginisialisasi rantai.

Penggunaan parameter akan dibahas nanti dalam kursus ini, jika parameter tersebut berhubungan dengan setiap bagian.

### Operasi Dasar Menggunakan Baris Perintah

Kursus ini akan menunjukkan contoh-contoh yang menggunakan program `elements-cli` untuk melakukan panggilan RPC ke satu atau beberapa node Elements. Hal ini dilakukan dari sesi terminal dan untuk membuat perintah menjadi lebih singkat, sebuah `alias` akan digunakan. Dengan konvensi ini ketika Anda melihat sesuatu seperti perintah berikut:

```bash
e1-dae
e1-cli getnewaddress
```

`e1-dae` dan `e1-cli` sebenarnya merupakan pintasan ketik yang memanfaatkan fitur `alias` pada terminal. `e1-dae` dan `e1-cli` sebenarnya akan diganti ketika perintah dijalankan dan perintah yang akan dijalankan akan mirip dengan:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```

Apa yang kita lihat di atas adalah sebuah panggilan untuk memulai daemon Elements dan sebuah panggilan ke program elements-cli yang terletak di direktori `$HOME/elements/src` dan sebuah nilai untuk parameter `datadir`. Parameter `datadir` memungkinkan kita untuk memberi tahu daemon dan klien di mana menemukan file konfigurasi mereka dan, dalam kasus daemon, di mana menyimpan salinan blockchain. Ketika mereka berbagi file konfigurasi, klien akan dapat melakukan panggilan RPC ke daemon.

Dengan menjalankan perintah di atas sekali lagi, tetapi dengan nilai `datadir` yang berbeda, kita dapat memulai lebih dari satu contoh Elements, masing-masing dengan salinan blockchain dan pengaturan konfigurasi yang terpisah. Dengan konvensi ini, kita akan menggunakan alias `e2-dae` dan `e2-cli` dalam kursus ini untuk merujuk ke direktori datadir yang berbeda dari e1. Jadi, contoh di atas untuk contoh `e2` kedua kita adalah:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```

Hal ini akan memungkinkan kita untuk melakukan berbagai macam operasi seperti transaksi aset antar node, menerbitkan aset dan memeriksa penggunaan blinding dalam Transaksi Rahasia antara node yang berbeda pada jaringan yang sama.

# Menggunakan kasus penggunaan Praktis Elemen

<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>

## Transaksi Rahasia

<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>

![Video](https://youtu.be/-by2xBtXQeE?si=7bLo_geGn3qh7MXN)

Pada bagian ini, Anda akan mempelajari cara menggunakan fitur Transaksi Rahasia di Elements.

Semua alamat di Elements, secara default, dibutakan menggunakan Transaksi Rahasia, yang menjaga jumlah dan jenis aset yang ditransfer hanya dapat dilihat oleh peserta dalam transaksi (dan mereka yang mereka pilih untuk mengungkapkan kunci yang membutakan), sementara secara kriptografis menjamin bahwa tidak ada lebih banyak koin yang dapat dibelanjakan daripada yang tersedia.

### Alamat Rahasia dan Transaksi Rahasia

Secara default, saat Anda membuat alamat baru di Elements menggunakan perintah `getnewaddress`, alamat tersebut dibuat sebagai alamat rahasia.

Untuk mendemonstrasikan transaksi rahasia, kita akan membuat e2 mengirimkan sejumlah dana kepada dirinya sendiri dan kemudian mencoba melihat transaksi dari e1. Hal ini akan menunjukkan sifat rahasia dari transaksi di Elements.

Setiap alamat baru yang dihasilkan oleh simpul Elements bersifat rahasia secara default. Kita dapat mendemonstrasikan hal ini dengan menggunakan e2 untuk menghasilkan alamat baru.

```
e2-cli getnewaddress
```

Perhatikan bahwa alamat dimulai dengan e1. Ini mengidentifikasikannya sebagai Alamat Rahasia. Memeriksa alamat secara lebih rinci menggunakan perintah getaddressinfo akan menampilkan detail alamat yang lebih lengkap.

```
e2-cli getaddressinfo <address>
```

Anda dapat melihat bahwa ada properti confidential_key yang memberi tahu kita bahwa itu adalah alamat rahasia.

Secret_key adalah kunci penyamaran publik, yang ditambahkan ke alamat rahasia itu sendiri. Ini adalah alasan mengapa alamat rahasia sangat panjang.

Alamat ini juga memiliki alamat tidak rahasia yang terkait. Jika Anda ingin menggunakan transaksi biasa, non-rahasia, di dalam Elements, aset harus dikirim ke alamat ini dan bukan ke alamat dengan awalan lq1.

Sekarang kita dapat meminta e2 untuk mengirimkan sejumlah dana ke alamat yang dibuatnya. Ini nantinya akan menunjukkan bahwa e1, karena bukan salah satu pihak yang bertransaksi, tidak akan dapat melihat detail transaksi.

```
e2-cli sendtoaddress <address>
```

Catat ID transaksi. Konfirmasikan transaksi.

```
e2-cli -generate 101
```

Melihat transaksi di mana e2 mengirimkan sejumlah dana ke dirinya sendiri dari perspektif e2 itu sendiri.

```
e2-cli gettransaction <txid>
```

Dengan menggulir ke atas detail transaksi, Anda dapat melihat bahwa e2 dapat melihat jumlah yang dikirim dan diterima serta aset yang ditransaksikan. Anda juga dapat melihat properti amountblinder dan assetblinder, yang digunakan untuk membutakan detail dari node lain yang tidak terlibat dalam transaksi.

Untuk memeriksa rincian transaksi yang sama dari e1, pertama-tama kita perlu mendapatkan rincian transaksi mentah.

```
e1-cli getrawtransaction <txid>
```

Itu mengembalikan detail transaksi mentah. Jika Anda melihat di dalam bagian vout, Anda dapat melihat bahwa ada tiga contoh. Dua contoh pertama adalah jumlah penerimaan dan kembalian, dan yang ketiga adalah biaya transaksi. Dari ketiga jumlah ini, biaya adalah satu-satunya yang dapat Anda lihat nilainya, karena biaya itu sendiri selalu tidak dibutakan di dalam Elements.

### Tombol yang Menyilaukan

Apa yang ditunjukkan oleh dua bagian vout pertama adalah "rentang yang dibutakan" dari jumlah nilai dan data komitmen yang bertindak sebagai bukti jumlah aktual dan jenis aset yang ditransaksikan.

Bahkan jika kita mengimpor private key e2 ke dalam dompet e1, dompet e1 masih tidak dapat melihat jumlah dan jenis aset yang ditransaksikan karena ia tidak memiliki pengetahuan tentang blinding key yang digunakan oleh e2. Kita akan membuktikan hal ini dengan mengimpor private key yang digunakan oleh dompet e2 ke dalam dompet e1. Pertama, kita perlu mengekspor kunci dari e2

```
e2-cli dumpprivkey <address>
```

Kemudian impor ke dalam e1.

```
e1-cli importprivkey <privkey>
```

Sekarang kita dapat membuktikan bahwa e1 masih belum dapat melihat nilainya.

```
e1-cli gettransaction <txid>
```

Memang, ini menunjukkan 0 sebagai jumlah tx padahal sebenarnya 1.

Untuk dapat melihat nilai yang sebenarnya, nilai yang tidak diblok, kita membutuhkan blinding key. Untuk melakukan hal ini, pertama-tama kita mengekspor blinding key dari e2.

```
e2-cli dumpblindingkey <address>
```

Kemudian impor ke dalam e1.

```
e1-cli importblindingkey <address> <blinding key>
```

Sekarang ketika kita mendapatkan detail transaksi dari e1.

```
e1-cli gettransaction <txid>
```

Ini menunjukkan bahwa dengan blinding key yang diimpor, kita sekarang dapat melihat nilai 1 yang sebenarnya di dalam transaksi.

Pada bagian ini kita telah melihat bahwa penggunaan blinding key menyembunyikan jumlah dan jenis aset dalam sebuah transaksi, dan dengan mengimpor blinding key yang tepat, kita dapat mengungkapkan nilai-nilai tersebut. Dalam penggunaan praktis, blinding key dapat, sebagai contoh, diberikan kepada auditor, jika ada kebutuhan untuk memverifikasi jumlah dan jenis aset yang dimiliki oleh suatu pihak. Fitur Transaksi Rahasia pada Elements juga memungkinkan untuk melakukan "bukti rentang". Bukti rentang dapat membuktikan bahwa sejumlah aset disimpan dalam rentang tertentu, tanpa perlu mengekspos jumlah sebenarnya.

Kita juga telah melihat bahwa Transaksi Rahasia adalah opsional, tetapi diaktifkan secara default ketika alamat baru dibuat.

Sekian untuk pelajaran kali ini; semoga berhasil dalam kuis dan sampai jumpa di pelajaran berikutnya!

## Aset yang Diterbitkan

<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>

![Video](https://youtu.be/XnY4WZUNSs4?si=dG8I5OoSh_0EBdvL)

Pada bagian ini anda akan mempelajari bagaimana cara menggunakan fitur Issued Assets di Elements.

Aset yang Diterbitkan memungkinkan beberapa jenis aset untuk diterbitkan dan ditransfer antara peserta jaringan Elements. Setiap node di jaringan dapat menerbitkan asetnya sendiri. Penerbitan dapat mewakili kepemilikan yang setara atas aset apa pun termasuk voucher, kupon, mata uang, deposito, obligasi, saham, dll. Aset yang Diterbitkan membuka pintu untuk membangun pertukaran tanpa kepercayaan, opsi, dan kontrak pintar canggih lainnya yang melibatkan aset yang diterbitkan sendiri.

Aset yang Diterbitkan juga mendapat manfaat dari Transaksi Rahasia dan dapat diterbitkan kembali oleh siapa pun yang memegang token terkait.

Langkah pertama adalah kita memerlukan akses ke dua node Elements, yang akan kita sebut e1 dan e2. Node-node tersebut telah disetel ulang blockchain-nya dan aset defaultnya telah dibagi di antara keduanya.

Kedua node berada pada jaringan lokal yang sama, dan terhubung satu sama lain, dan oleh karena itu berbagi transaksi yang sama dalam mempool transaksi dan blockchain yang sama. Walaupun mereka berjalan pada mesin yang sama, perlu dicatat bahwa mereka tidak berbagi file blockchain yang sama. Setiap node mengelola salinan lokal blockchain-nya sendiri, yang berisi riwayat transaksi yang sama karena mereka berada dalam konsensus dan mematuhi aturan protokol yang sama satu sama lain.

Mari kita mulai dengan memeriksa tampilan setiap node dari penerbitan aset yang ada di jaringan.

Hal ini dilakukan dengan menggunakan perintah listissuances.

```
e1-cli listissuances
e2-cli listissuances
```

Seperti yang dapat Anda lihat, kedua node menunjukkan riwayat penerbitan yang sama. Keduanya menampilkan satu aset, yaitu penerbitan awal 21 juta Bitcoin yang dibuat pada inisialisasi chain. Anda dapat melihat hex id dari aset tersebut pada hasil dari menjalankan perintah di atas dan juga label yang diberikan kepada aset tersebut, yaitu 'bitcoin'.

Perlu dicatat bahwa aset default selalu diberi label ketika chain diinisialisasi. Ketika Anda menerbitkan aset Anda sendiri, Anda dapat mengatur label untuk aset tersebut, yang akan segera kita lakukan. Sebelum kita dapat melakukannya, kita perlu menerbitkan aset kita sendiri.

Kita akan meminta e1 untuk menerbitkan aset baru. Hal ini dilakukan dengan menggunakan perintah issueasset.

```
e1-cli issueasset 100 1 false
```

`issueasset` menerima 3 parameter.

Jumlah aset baru yang akan diterbitkan, kami menggunakan 100. Jumlah token yang akan dibuat (token digunakan untuk menerbitkan kembali jumlah aset), yang kami pilih 1. Parameter terakhir memberi tahu Elements untuk membuat penerbitan aset sebagai blinded atau unblinded. Kita akan menggunakan unblinded karena kita ingin melihat jumlah penerbitan dari e2 sebentar lagi, jadi kita akan memasukkan nilai false.

Menjalankan perintah tersebut akan mengembalikan data tentang penerbitan. Ini termasuk id transaksi, yang dapat Anda ambil salinannya untuk digunakan nanti, nilai heksa unik aset, dan nilai heksa unik token aset.

Buat blok untuk mengonfirmasi transaksi penerbitan.

```
e1-cli -generate 1
```

Jalankan perintah `listissuances` terhadap e1 lagi.

```
e1-cli listissuances
```

Hal ini menunjukkan kepada kita bahwa e1 sekarang mengetahui adanya 2 penerbitan, yaitu penerbitan awal Bitcoin dan aset yang baru saja diterbitkan, di mana kita dapat melihat 100 aset. Perhatikan nilai hex dari aset baru dan bahwa tidak ada label aset yang terkait, seperti yang ada pada penerbitan bitcoin.

Periksa kembali daftar penerbitan e2 yang diketahui.

```
e2-cli listissuances
```

Hal ini menunjukkan kepada kita bahwa e2 tidak mengetahui penerbitan aset yang dilakukan oleh e1. Ia hanya dapat melihat penerbitan awal bitcoin yang sudah dapat dilihatnya.

Hal ini karena e2 tidak mengetahui, dan tidak mengawasi, alamat tujuan pengiriman aset baru ketika aset tersebut diterbitkan oleh e1.

Perlu dicatat bahwa meskipun e2 tidak dapat melihat penerbitan itu sendiri, e1 masih dapat mengirimkan sejumlah aset kepada e2. Aset baru tersebut kemudian akan muncul sebagai saldo yang tersedia di dompet e2, meskipun ia tidak mengetahui penerbitan aslinya.

Agar e2 dapat melihat penerbitan yang sebenarnya (dan oleh karena itu jumlah yang diterbitkan), kita perlu menambahkan alamat tersebut ke e2 sebagai alamat yang diawasi.

Untuk melakukan ini, kita perlu mencari tahu alamat tujuan pengiriman aset tersebut. Untuk itu, kita akan menggunakan id transaksi yang telah kita salin sebelumnya dan meminta e1 untuk mengambil detail dari transaksi tersebut sehingga kita dapat menemukan alamat yang benar untuk ditambahkan ke daftar pantauan dompet e2.

```
e1-cli gettransaction <the-issuance-transaction-id>
```

Dengan menggulir ke atas melewati heksa data transaksi, Anda akan melihat alamat yang menerima 100 aset baru kami, yang diidentifikasi berdasarkan nilai heksanya.

Ambil alamatnya dan salin agar kita dapat mengimpornya ke e2.

Sekarang mari kita mengimpor alamat tersebut ke dalam e2. Untuk melakukan hal ini kita menggunakan perintah importaddress.

```
e2-cli importaddress <the-issued-to-address>
```

Jika kita sekarang memeriksa daftar penerbitan e2.

```
e2-cli listissuances
```

Anda dapat melihat bahwa aset yang baru diterbitkan sekarang sudah masuk ke dalam daftar. Node e2 juga dapat menentukan jumlah aset yang telah diterbitkan, bersama dengan jumlah token yang terkait, karena penerbitan tersebut merupakan penerbitan yang tidak dibutakan. Untuk mengaktifkan penggunaan ID aset ke pemetaan nama di dalam Elements, hentikan dulu Elements.

```
e1-cli stop
```

Kemudian mulai ulang dengan parameter tambahan yang memetakan hex aset ke label yang disediakan. Hal ini memungkinkan node untuk menampilkan data mengenai aset kepada kita dalam format yang lebih mudah dibaca oleh manusia. Anda dapat menambahkan ini di akhir elements.conf jika Anda mau, maka Anda tidak perlu menambahkan argumen ke daemon setiap kali Anda menjalankannya. Sebagai contoh:

```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```

Tetapi kita akan menggunakan metode argumen di sini.

```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```

Menanyakan node untuk daftar penerbitan lagi.

```
e1-cli listissuances
```

Ini menunjukkan kepada kita bahwa pemetaan nilai heksa aset ke labelnya berhasil. Memeriksa kembali daftar penerbitan node e2.

```
e2-cli listissuances
```

Anda dapat melihat bahwa node e2 tidak memiliki akses ke label ini, karena label hanya tersedia untuk node yang menetapkannya. Tentu saja, kita dapat memberikan label yang berbeda pada hex aset yang sama pada e2 daripada yang kita lakukan pada e1. Pertama-tama hentikan node e2.

```
e2-cli stop
```

Memulai ulang dengan label yang berbeda yang ditetapkan ke hex aset baru kita.

```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```

Pencatatan penerbitan dari e2.

```
e2-cli listissuances
```

Label aset bersifat lokal untuk setiap node, hanya heksa aset yang dikenali oleh node lain di jaringan.

Pemetaan label ke hex aset berguna ketika melakukan tindakan seperti transaksi dan kueri saldo dompet, karena memungkinkan cara singkat untuk merujuk ke aset. Sebagai contoh, jika kita ingin mengirimkan beberapa aset baru (sejumlah 10) dari e1 ke e2 tanpa menggunakan label.

Pertama, kita perlu mendapatkan alamat untuk mengirim aset.

```
e2-cli getnewaddress
```

Kemudian gunakan perintah sendtoaddress.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```

Konfirmasikan transaksi dengan membuat blok.

```
generate 1
```

Memeriksa aset telah diterima pada e2.

```
e2-cli getwalletinfo
```

Kita dapat melihat bahwa aset tersebut memang telah diterima.

Perhatikan bahwa e2 memetakan hex dari aset yang diterima dan menampilkannya menggunakan labelnya sendiri. Cara yang lebih mudah untuk melakukan hal yang sama adalah dengan menggunakan label aset e1 saat mengirim.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```

Di balik layar, Elements memetakan label lokal ke nilai heksa untuk membantu menyederhanakan penggunaan aset yang diterbitkan.

Pada bagian ini kita telah melihat bagaimana cara menerbitkan dan melabeli aset. Pada bagian selanjutnya kita akan melihat bagaimana cara menerbitkan kembali dan memusnahkan aset yang sudah diterbitkan.

## Menerbitkan Kembali Aset

<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>

![Video](https://youtu.be/5em79YHtYk0?si=rhponm6Hw9AB6RJp)

Pada bagian ini Anda akan mempelajari cara menerbitkan lebih banyak aset yang sudah diterbitkan dan juga cara menghancurkan sejumlah aset yang sudah diterbitkan.

Kebutuhan untuk menerbitkan kembali (membuat lebih banyak) aset atau menghancurkan sejumlah aset adalah sesuatu yang mungkin terjadi ketika aset mewakili sesuatu yang tidak memiliki pasokan tetap. Hal ini dapat diterapkan pada aset yang mewakili emas yang disimpan di lemari besi misalnya; ketika unit emas bergerak masuk dan keluar dari lemari besi, aset yang mewakili pasokan lemari besi perlu disesuaikan naik atau turun.

Penerbitan ulang sejumlah aset membutuhkan kepemilikan token terkait yang dibuat bersama aset tersebut saat pertama kali diterbitkan.

Ketika membuat lebih banyak aset, tidak masalah node mana yang menerbitkan aset di tempat pertama, selama node yang menerbitkan kembali sejumlah aset memiliki apa yang biasa disebut token penerbitan ulang aset. Kita akan melihat bagaimana cara membuat token penerbitan ulang, cara menggunakannya untuk menerbitkan ulang sejumlah aset dan juga cara mentransfer token penerbitan ulang ke node lain, sehingga mereka juga memiliki izin untuk menerbitkan ulang aset tersebut.

Kita akan membutuhkan akses ke dua node Elements, yang akan kita sebut sebagai e1 dan e2. Node-node tersebut telah disetel ulang blockchainnya dan aset default dibagi di antara keduanya.

Kita akan membuat e1 menerbitkan sejumlah 100 aset baru dan membuat 1 token penerbitan ulang untuk aset yang sama. Kita akan membuat penerbitan sebagai unblinded untuk menyederhanakan contoh. Jadi, mari kita lanjutkan dan terbitkan aset dan token penerbitan ulang terkait.

```
e1-cli issueasset 100 1 false
```

Catat ID aset dan juga ID token (penerbitan ulang).

Karena nantinya kita akan menerbitkan kembali lebih banyak aset dari e2, kita perlu mencatat ID transaksi saat aset diterbitkan dan menggunakannya untuk mengimpor alamat tujuan pengiriman aset.

Konfirmasi transaksi.

```
e1-cli -generate 1
```

Sekarang kita akan memeriksa detail transaksi dengan menggunakan perintah gettransaction:

```
e1-cli gettransaction <txid>
```

Dengan menggulir ke atas melewati hex dari data transaksi, Anda akan melihat bahwa dalam transaksi tersebut e1 menerima 1 token penerbitan ulang dan 100 aset terkait.

Ambil salinan alamat tersebut agar kita dapat mengimpornya ke dalam e2.

Dan sekarang mengimpor alamat tersebut ke dalam dompet e2.

```
e2-cli importaddress <address>
```

Sekarang kita dapat melihat bahwa baik e1 dan e2 mengetahui penerbitan aset.

```
e1-cli listissuances
e2-cli listissuances
```

Saat ini e1 memegang sejumlah aset dan 1 token penerbitan ulang, tetapi e2 tidak.

```
e1-cli getwalletinfo
```

Perhatikan juga bahwa e1 memiliki lebih sedikit aset default daripada sebelumnya karena membayar sejumlah kecil untuk menutupi biaya transaksi. Jumlah ini akan ditagih oleh e1 ketika blok yang dibuat telah jatuh tempo lebih dari 100 blok.

```
e2-cli getwalletinfo
```

Karena e1 memegang token penerbitan ulang, maka ia dapat menerbitkan lebih banyak token. Ini dilakukan dengan menggunakan perintah reissueasset. Misalkan e1 akan menerbitkan kembali 100 aset lainnya.

```
e1-cli reissueasset <asset-id> 100
```

Memeriksa penerbitan ulang berhasil.

```
e1-cli getwalletinfo
```

Anda bisa melihat bahwa e1 sekarang memiliki 200 aset seperti yang diharapkan.

Karena e2 tidak memiliki sejumlah token penerbitan ulang, mereka akan menerima kesalahan jika mencoba menerbitkan ulang aset.

```
e2-cli reissueasset <asset-id> 100
```

Perhatikan pesan kesalahan.

Kita dapat melihat rincian penerbitan ulang dari e1 menggunakan perintah listissuances.

```
e1-cli listissuances
```

Perhatikan bendera `is_reissuance`.

Jika kita sekarang mengirim e2 sejumlah token penerbitan ulang, mereka akan dapat menerbitkan ulang sejumlah aset itu sendiri. Pertama, kita perlu alamat untuk mengirimkannya. Perlu dicatat bahwa token penerbitan ulang diperlakukan sama seperti aset lainnya di dalam elemen saat mengirim dan menampilkan saldo dan juga dapat dipecah menjadi denominasi yang lebih kecil seperti aset lainnya, jadi kita tidak perlu mengirim 1 token penerbitan ulang ke e2 agar dapat menerbitkan ulang aset tersebut. Denominasi apa pun bisa digunakan. Membuat alamat untuk e2 untuk menerima token penerbitan ulang.

```
e2-cli getnewaddress
```

Kemudian kirimkan sebagian kecil RIT dari e1 ke e2.

```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Konfirmasi transaksi.

```
e1-cli -generate 1
```

Sekarang kita bisa melihat bahwa e2 menyimpan 0.1 yang dikirim.

```
e2-cli getwalletinfo
```

Ini berarti e2 sekarang dapat menerbitkan kembali lebih banyak aset yang terkait dengan RIT yang ada di dalam dompetnya. Kita akan memiliki e2 yang menerbitkan kembali 500 aset.

```
e2-cli reissueasset <asset-id> 500
```

Periksa hasil penerbitan ulang.

```
e2-cli getwalletinfo
```

Anda dapat melihat bahwa e2 sekarang menyimpan jumlah yang diterbitkan ulang di saldo dompetnya dan bahwa RIT itu sendiri tidak dikonsumsi dalam proses penerbitan ulang aset.

Menghancurkan sejumlah aset adalah sesuatu yang dapat dilakukan oleh siapa saja yang memiliki setidaknya jumlah yang dihancurkan, tidak diatur oleh token penerbitan ulang.

```
e2-cli destroyamount <asset-id>
e2-cli getwalletinfo
```

Pada bagian ini kita telah melihat bagaimana cara menerbitkan aset, bersama dengan cara menggunakan token penerbitan ulang yang secara opsional dibuat sebagai bagian dari penerbitan aset. Kita juga telah melihat bagaimana mentransfer token penerbitan ulang semudah mentransfer aset lainnya, dan bahwa memegang sejumlah token penerbitan ulang memberikan hak kepada pemegangnya untuk menerbitkan lebih banyak aset terkait. Oleh karena itu, sangat penting untuk mengontrol siapa saja yang memiliki akses ke token penerbitan ulang di jaringan Anda. Kita juga telah melihat bagaimana cara menghancurkan sejumlah aset dan bahwa proses ini tidak dikendalikan oleh kepemilikan token penerbitan ulang.

# Federasi Elemen

<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>

## Penandatanganan Blok

<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>

![Video](https://youtu.be/kxWX91fCnus?si=KItm_Am3_RrBcLBN)

Elements mendukung model penandatanganan federasi yang memungkinkan Anda untuk menentukan jumlah anggota Strong Federation yang harus menandatangani blok yang diusulkan untuk menghasilkan blok yang valid.

Sebelumnya, dan untuk memudahkan, kita telah membuat blok menggunakan perintah `generate`, yang tidak perlu memenuhi persyaratan multisignature agar blok yang dibuat dapat diterima oleh jaringan sebagai blok yang valid.

Kita akan menyiapkan node kita untuk membutuhkan pembuatan blok multisig 2-dari-2. Ini akan diatur menggunakan parameter signblockscript, yang dapat ditambahkan ke file konfigurasi atau dimasukkan ke dalam node pada saat startup. Untuk menginisialisasi rantai dengan parameter ini, pertama-tama kita harus membuat skrip yang terdiri dari parameter tersebut.

Kita akan melakukan ini dengan menggunakan beberapa node yang ada, menyimpan data yang mereka keluarkan dan kemudian menghapus rantai sehingga kita dapat memulai ulang menggunakan parameter signblockscript. Hal ini diperlukan karena skrip tersebut merupakan bagian dari aturan konsensus jaringan dan perlu disetel pada inisialisasi rantai. Skrip ini tidak dapat ditambahkan di kemudian hari ke chain yang sudah ada.

Kita akan membutuhkan akses ke dua node Elements, yang akan kita sebut sebagai e1 dan e2. Node-node tersebut telah disetel ulang blockchainnya dan aset default dibagi di antara keduanya.

Pastikan bahwa parameter con_max_block_sig_size disetel ke nilai yang tinggi dalam berkas elements.conf Anda, jika tidak, penandatanganan blok akan gagal di bagian ini. Kami telah menetapkan con_max_block_sig_size = 2000 untuk tutorial ini.

Karena kita akan mengatur ulang blockchain dan menghapus wallet yang terkait dengan e1 dan e2, kita perlu mengambil salinan alamat, kunci publik dan kunci privat yang kita gunakan untuk membuat skrip penandatanganan blok agar dapat digunakan nanti.

Pertama, kita membutuhkan setiap node penandatanganan blok untuk menghasilkan alamat baru, yang perlu Anda ambil salinannya.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

Kemudian kita perlu mengekstrak kunci publik dari alamat-alamat tersebut dan mencatatnya untuk digunakan nanti.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

Kemudian ekstrak kunci privat, yang akan kita impor ulang nanti sehingga node dapat menandatangani blok setelah kita menginisialisasi ulang data blockchain dan dompet kita.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Sekarang kita perlu membuat sebuah skrip penukaran dengan 2 dari 2 persyaratan multi-tanda tangan. Kita melakukan ini dengan menggunakan perintah createmultisig dan memberikan parameter pertama sebagai 2 dan kemudian memberikan dua kunci publik. Kunci-kunci inilah yang perlu dibuktikan kepemilikannya nanti ketika blok dibuat.

Salah satu simpul, e1 atau e2, dapat menghasilkan multisig.

```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```

Ini memberi kita redeemscript, yang bisa Anda salin untuk digunakan nanti.

Sekarang kita perlu menghapus data blockchain dan dompet yang ada sehingga kita dapat memulai lagi dengan signblockscript yang baru sebagai bagian dari aturan konsensus rantai. Inilah sebabnya mengapa kita perlu mengambil salinan dari beberapa data sebelumnya, seperti private key yang akan digunakan dalam chain baru untuk menandatangani blok. Anda perlu melakukan ini sebelum melanjutkan.

Dengan data wallet dan chain yang telah dihapus, kita sekarang dapat memulai node dan menginisialisasi chain baru dengan menggunakan parameter signblockscript. Mari kita masukkan -evbparams=dynafed:0::: untuk menonaktifkan aktivasi dynafed, karena kita tidak memerlukan fitur lanjutan tersebut untuk contoh ini.

```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```

Sekarang kita perlu mengimpor private key yang telah kita simpan sebelumnya agar node kita dapat menandatangani dan membantu menyelesaikan blok yang diusulkan.

```
e1-cli importprivkey <e1-priv-key>
e2-cli importprivkey <e2-priv-key>
```

Penggunaan perintah generate sekarang akan mengalami kesalahan karena gagal memenuhi aturan penandatanganan blok yang diperlukan yang sekarang diberlakukan oleh node kita.

```
e1-cli -generate 1
```

Untuk mengusulkan blok baru, setiap node dapat memanggil perintah getnewblockhex. Perintah ini mengembalikan hex dari blok baru yang perlu ditandatangani sebelum diterima oleh node mana pun di jaringan kita.

```
e1-cli getnewblockhex
```

Ingatlah bahwa perintah tersebut hanya membuat blok yang diusulkan, tidak menghasilkan blok.

Untuk mengonfirmasi hal ini, kita dapat melihat bahwa saat ini tidak ada blok di blockchain kita.

```
e1-cli getblockcount
```

Jika kita mencoba mengirimkan blok hex tanpa menandatanganinya terlebih dahulu.

```
e1-cli submitblock <block-hex>
```

Kami mendapatkan pesan yang memberitahukan bahwa bukti blokir tidak valid. Ini karena belum ditandatangani oleh 2 dari 2 pihak yang diperlukan.

Jadi, mari kita minta e1 untuk menandatangani blok yang diusulkan.

```
e1-cli signblock <block-hex>
```

Mintalah e2 untuk menandatangani hex.

```
e2-cli signblock <block-hex>
```

Perhatikan bahwa e2 tidak menandatangani keluaran yang dibuat dari e1 yang menandatangani blok yang diusulkan. Keduanya menandatangani hex blok yang diusulkan secara independen dari hasil satu sama lain.

Sekarang kita perlu menggabungkan tanda tangan blok dari e1 dan e2. Salah satu node dapat melakukan ini, yang mereka butuhkan hanyalah hex blok yang ditandatangani dari node lainnya.

```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```

Anda dapat melihat perintah combineblocksigs mengeluarkan hex dari blok yang telah ditandatangani serta status selesai, yang memberi tahu kita bahwa hex blok tersebut telah siap untuk dikirimkan.

Sekarang salah satu node dapat mengirimkan hex blok yang sudah selesai. Kita akan meminta e1 untuk melakukannya.

```
e1-cli submitblock <combined-signed-hex>
```

Memeriksa apakah pengajuan tersebut valid.

```
e1-cli getblockcount
e2-cli getblockcount
```

Anda dapat melihat bahwa e1 dan e2 telah menerima blok tersebut sebagai valid dan menambahkannya ke ujung salinan lokal blockchain mereka.

Untuk meringkas prosesnya. Di bagian ini kita sudah sampai:


- Mengusulkan sebuah blok.
- Mintalah setiap simpul menandatanganinya.
- Menggabungkan tanda tangan.
- Memeriksa apakah tanda tangan tersebut valid dan memenuhi ambang batas penukaran chain.
- Mengirimkan blok tersebut.

Setiap node di jaringan memvalidasi blok dan menambahkannya ke salinan lokal blockchain mereka.

### Blok SIgning

Meskipun proses awalnya tampak rumit, urutan penandatanganan blok di Elements selalu sama dan penyiapan awal hanya perlu dilakukan satu kali:

1. Penyiapan awal (dilakukan sekali)

2. Alamat multisignature dibuat dengan nama `signblockscript` menggunakan kunci publik dari Federated Block Signers.

3. Skrip penukaran dari ini digunakan untuk memulai blockchain baru.

4. Produksi blok (sedang berlangsung)

5. Blok yang diusulkan dibuat dan ditukar untuk ditandatangani.

Setelah sejumlah penandatangan menandatangani blok yang diusulkan, blok tersebut akan digabungkan dan dikirimkan ke jaringan. Jika memenuhi kriteria `signblockscript` rantai, node menerimanya sebagai blok yang valid.

## Elemen sebagai Rantai Samping

<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>

![Video](https://youtu.be/egYzj4N8CB8?si=v7_-IXsjHPE-ARDe)

Elements adalah sebuah platform blockchain open-source, tujuan umum yang juga dapat "dipasangkan" ke blockchain yang sudah ada, seperti Bitcoin. Ketika dipasangkan ke blockchain lain, Elements dikatakan beroperasi sebagai `sidechain`. Sidechain memungkinkan transfer aset dua arah dari satu rantai ke rantai lainnya. Menerapkan Elements sebagai sidechain memungkinkan Anda untuk mengatasi beberapa keterbatasan yang melekat pada blockchain utama, sambil mempertahankan tingkat keamanan yang baik yang disediakan oleh aset yang diamankan di blockchain utama.

Walaupun sidechain mengetahui mainchain dan riwayat transaksinya, mainchain tidak mengetahui sidechain dan tidak ada yang dibutuhkan untuk pengoperasiannya. Hal ini memungkinkan sidechain untuk berinovasi tanpa batasan atau penundaan yang terkait dengan proposal peningkatan protokol mainchain. Daripada mencoba mengubahnya secara langsung, memperluas protokol utama memungkinkan mainchain itu sendiri untuk tetap aman dan terspesialisasi, mendukung kelancaran operasi sidechain.

Dengan memperluas fungsionalitas Bitcoin dan meningkatkan keamanan yang mendasarinya, sidechain berbasis Elements dapat menyediakan fungsionalitas baru yang sebelumnya tidak tersedia untuk pengguna mainchain. Contoh sidechain berbasis Elements yang digunakan dalam produksi adalah Liquid Network.

Untuk menginisialisasi blockchain Elements sebagai sidechain, kita perlu menggunakan parameter skrip pasak terfederasi. Parameter ini dapat diatur dalam file konfigurasi node atau dimasukkan pada saat memulai.

Skrip pasak federasi mendefinisikan anggota federasi yang kuat mana yang dapat melakukan fungsi pasak-in dan pasak-out. Para fungsionaris ini disebut sebagai `Watchmen` karena mereka mengawasi mainchain dan sidechain untuk transaksi peg-in dan peg-out yang valid dan menindaklanjutinya jika valid. Untuk `peg-out` berarti memindahkan aset yang dipatok keluar dari sidechain dan masuk ke dalam mainchain dan untuk `peg-in` berarti memindahkan aset yang dipatok ke dalam sidechain dari mainchain. Ketika kita mengatakan `pindah ke sidechain`, yang sebenarnya kita maksudkan adalah dana terkunci dalam alamat multi-tanda tangan di mainchain dan jumlah aset yang sesuai dibuat di sidechain Elements. Ketika kami mengatakan `pindah dari sidechain`, yang kami maksud adalah aset dihancurkan di sidechain Elements dan jumlah yang sesuai dilepaskan dari dana terkunci yang dipegang di blockchain utama. Izin untuk melakukan fungsi peg-in dan peg-out mengharuskan fungsionaris untuk membuktikan kepemilikan kunci publik yang digunakan dalam skrip pasak yang difederasi. Ini dilakukan dengan menggunakan private key yang sesuai.

Untuk membuat skrip pasak federasi, pertama-tama kita harus membuat setiap node menghasilkan kunci publik. Kita juga perlu menyimpan private key yang terkait untuk digunakan nanti karena kita perlu menghapus data chain yang ada dan menginisialisasi chain baru menggunakan skrip pasak yang difederasi. Ini karena skrip pasak federasi merupakan bagian dari aturan konsensus sidechain, dan tidak dapat diterapkan pada blockchain yang sudah ada dan tidak dipasak di kemudian hari.

Jadi, mari kita buat alamat untuk setiap node kita, simpan data yang relevan untuk digunakan nanti, dan buat skrip pasak terfederasi yang akan kita gunakan untuk menginisialisasi sidechain kita nanti.

Pertama, kita membutuhkan setiap node kita, yang akan bertindak sebagai Watchmen dalam jaringan kita, untuk menghasilkan alamat baru.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

Kemudian kami memvalidasi alamat tersebut untuk mendapatkan kunci publik.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

Dan kemudian mengambil kunci pribadi yang terkait dengan setiap alamat.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Simpan kunci privat dan publik untuk digunakan di kemudian hari.

Sekarang kita perlu menghapus data blockchain dan wallet yang ada karena kita akan menginisialisasi chain baru menggunakan skrip federated peg. Anda dapat melakukan ini sekarang. Jangan lupa untuk menjalankan daemon Bitcoin, yang perlu kita pasak.

Sekarang kita dapat menginisialisasi rantai baru dengan skrip pasak federasi yang dibuat menggunakan kunci publik yang telah kita simpan sebelumnya. Angka-angka yang kita masukkan dan yang mengelilingi kunci publik kita mendefinisikan dan membatasi jumlah kunci yang digunakan, dan kepemilikan kunci yang harus dibuktikan untuk melakukan peg-in dan peg-out pada sidechain kita.

```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```

Sekarang kita akan mengimpor private key yang telah kita simpan sebelumnya, sehingga node kita nantinya dapat menandatangani dan menyelesaikan transfer aset antar chain dan memenuhi persyaratan dari skrip pasak federasi.

```
e1-cli importprivkey <priv-key-1>
e2-cli importprivkey <priv-key-1>
```

Sekarang kita perlu mematangkan beberapa blok di kedua chain. Kematangan blok adalah persyaratan dari proses peg karena melindungi dari reorganisasi blok pada rantai utama yang mengarah ke penggelembungan pasokan aset yang dipatok dalam sidechain.

Untuk menjaga agar bagian ini tetap fokus pada federated peg, kita akan membuat blok tanpa menggunakan model penandatanganan blok yang telah kita lihat pada bagian sebelumnya, dan kembali menggunakan perintah 'generate' untuk membuat blok baru.

```
b-cli generate 101
e1-cli generate 1
```

Kita tidak perlu membuat blok sekarang untuk elemen. Tapi, mari kita buat satu saja. Ini adalah praktik yang baik untuk menghindari potensi inkonsistensi.

Sekarang rantai kita siap untuk melakukan peg-in. Untuk melakukan peg-in, kita perlu membuat alamat khusus menggunakan perintah getpeginaddress. Perhatikan bahwa durasi antara pembuatan alamat peg-in dengan getpeginaddress dan mengklaimnya dengan claimpegin harus dijaga sekecil mungkin. alamat peg-in tidak tahan lama dan tidak boleh digunakan kembali.

```
e1-cli getpeginaddress
```

Anda dapat melihat bahwa perintah tersebut membuat alamat mainchain baru, serta skrip baru yang perlu dipenuhi untuk mengklaim dana peg-in. Alamat mainchain adalah alamat `pay to script hash` yang akan digunakan oleh fungsionaris yang menjalankan peran Watchmen di dalam jaringan Elements.

Seperti getnewaddress, getpeginaddress menambahkan rahasia baru ke dalam dompet node pemanggil, jadi penting untuk memasukkan cadangan file dompet ke dalam proses manajemen node Anda.

Sekarang kita akan mengirimkan sejumlah bitcoin dari mainchain ke sidechain. Dompet uji regresi mainchain kita sudah menyimpan sejumlah dana.

```
b-cli getwalletinfo
```

Kita dapat melihat bahwa dompet tersebut menyimpan 50 bitcoin. Kita akan mengirimkan satu bitcoin dari mainchain ke sidechain. Kita perlu mengirim dana ke alamat mainchain yang telah dibuat oleh node kita sebelumnya.

```
b-cli sendtoaddress <e1-pegin-address>
```

Kami perlu menyimpan ID transaksi ini karena kami membutuhkannya untuk bukti pendanaan nanti.

Sekarang kita dapat melihat bahwa saldo dompet mainchain telah berkurang sebesar jumlah yang kita kirimkan, ditambah dengan sejumlah kecil tambahan untuk menutupi biaya transaksi.

```
b-cli getwalletinfo
```

Kami perlu mematangkan transaksi lagi.

```
b-cli generate 101
```

Agar node Elements dapat mengklaim dana peg-in, kita harus mendapatkan 'bukti' bahwa transaksi peg-in telah dilakukan. Bukti kriptografi menggunakan ID transaksi pendanaan untuk menghitung jalur merkel dan membuktikan bahwa transaksi tersebut ada di blok yang telah dikonfirmasi.

```
b-cli gettxoutproof '["<tx-id>"]'
```

Kami juga membutuhkan data transaksi mentah.

```
b-cli getrawtransaction <tx-id>
```

Dengan bukti dan data mentah untuk transaksi peg-in, node elemen kami sekarang dapat mengklaim peg-in menggunakan transaksi mentah dan bukti transaksi.

```
e1-cli claimpegin <raw> <proof>
```

Perhatikan bahwa ada argumen ketiga opsional yang dapat kita berikan kepada claimpegin. Parameter ketiga ini dapat digunakan untuk menentukan alamat sidechain yang akan digunakan untuk mengirim dana yang diklaim. Ini tidak diperlukan dalam contoh kita karena kita memanggil perintah dari node yang sama dengan alamat tujuan dana yang diklaim.

Memeriksa saldo e1.

```
e1-cli getwalletinfo
```

Membuat blok untuk mengonfirmasi klaim.

```
e1-cli generate 1
```

Memeriksa saldo e1.

```
e1-cli getwalletinfo
```

Kita dapat melihat bahwa peg-in telah berhasil diklaim.

Untuk mematok harga, prosesnya serupa. Sebuah alamat dibuat, dana dikirim ke alamat tersebut dan dana dilepaskan jika transaksi valid. Kita tidak akan membahas seluruh proses peg-out karena melibatkan pekerjaan di mainchain yang berada di luar cakupan kursus ini. Langkah-langkah dalam hal peristiwa Elements adalah bahwa sebuah alamat dibuat di mainchain.

```
b-cli getnewaddress
```

Dana dikirim ke alamat mainchain dari node Elements menggunakan perintah sendtomainchain.

```
e1-cli sendtomainchain <new-address> 1
```

Membuat blok untuk mengonfirmasi transaksi.

```
e1-cli generate 1
```

Periksa saldo dompet node.

```
e1-cli getwalletinfo
```

Dan lihatlah bahwa saldo telah berkurang.

Pada bagian ini, kita sudah melihat bagaimana caranya:


- Buatlah skrip pasak federasi.
- Inisialisasi rantai baru yang menggunakan skrip sebagai aturan parameter konsensus jaringan.
- Mengirimkan dana dari mainchain ke sidechain.
- Klaim dana dalam sidechain Elements.
- Pahami bagaimana pengiriman dana kembali ke mainchain dimulai.

### FederatedPegScript

Agar Elements dapat bekerja sebagai sidechain, blok genesis dalam blockchain harus dibuat dengan `fedpegscript`. Ini dilakukan dengan memasukkan parameter `fedpegscript` pada saat node dimulai. Skrip ini kemudian akan menjadi bagian dari aturan konsensus blockchain Elements dan memungkinkan permintaan peg-in dan peg-out untuk divalidasi dan ditindaklanjuti.

Fedpegscript terdiri dari kunci publik yang dikontrol oleh mereka yang berwenang untuk melakukan tindakan pasak. Berikut ini menunjukkan contoh format dari fedpegscript multisignature 2-dari-2:

```
fedpegscript=5221<public key 1>21<public key 2>52ae
```

Catatan: Karakter di luar kunci publik adalah pembatas yang mengindikasikan kunci publik dan persyaratan `n dari m`. Sebagai contoh, templat untuk fedpegscript 1 dari 1 adalah '5121<pub key 1>51ae'.

### Peg-in

Sebelum sebuah peg-in dapat diterima oleh sidechain Elements, peg-in tersebut harus memiliki konfirmasi yang cukup di mainchain. Hal ini diperlukan untuk menghindari inflasi dalam pasokan aset yang dipatok di sidechain Elements yang dapat disebabkan oleh pengorganisasian ulang mainchain.

Pengorganisasian ulang yang singkat pada ujung blockchain Bitcoin diharapkan sebagai bagian dari operasi normal mekanisme konsensus Proof of Work (PoW). Dengan demikian, Elements hanya menerima sebuah peg-in yang valid jika memiliki kedalaman yang cukup di dalam blockchain Bitcoin. Hal ini berfungsi untuk mencegah Elements menerima peg-in yang sama lebih dari satu kali.

### Peg-Out

Peg-out terjadi ketika node Elements memanggil perintah `sendtomainchain`, yang menerima input alamat mainchain (tujuan peg-out) serta jumlah aset yang dipatok yang akan 'ditarik'. Ini menciptakan transaksi peg-out pada sidechain. Setelah Fungsionaris yang bertindak sebagai Watchmen mendeteksi bahwa transaksi peg-out telah dikonfirmasi di sidechain, mereka akan melepaskan aset di mainchain ke tujuan peg-out, seperti yang telah kita pelajari di bagian sebelumnya dalam kursus ini.

## Elemen sebagai Blockchain Mandiri

<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>

![Video](https://youtu.be/u-3rV7DGtD0?si=G1__H0Uelf4sTUDM)

Sejauh ini, kita telah melihat cara menjalankan Elements sebagai sidechain. Akan tetapi, ia juga dapat beroperasi sebagai solusi blockchain mandiri dengan aset asli bawaannya sendiri. Dalam pengaturan ini, blockchain Elements masih mempertahankan semua fitur implementasi sidechain, seperti Transaksi Rahasia dan Aset yang Diterbitkan, tetapi tidak memerlukan peg-in atau peg-out untuk menambah atau menghapus jumlah aset default dari sirkulasi.

Pada bagian ini kita akan membahasnya:

Inisialisasi blockchain Elements baru dengan aset default bernama `newasset`.

Tentukan 1.000.000 `newasset` yang akan dibuat bersama dengan 2 token penerbitan ulang untuknya.

Klaim semua koin `newasset` yang bisa dibelanjakan oleh siapa saja.

Klaim semua token penerbitan ulang yang bisa dibelanjakan siapa saja untuk 'aset baru'.

Kirim aset dan token penerbitan ulangnya ke dompet node lain.

Terbitkan kembali lebih banyak 'aset baru' dari kedua node.

Untuk menginisialisasi jaringan Elements agar dapat beroperasi sebagai blockchain mandiri, setiap node harus dimulai dengan beberapa parameter dasar. Parameter tersebut digunakan untuk memberitahu node agar tidak mencoba dan memvalidasi peg-in dari blockchain lain, nama aset default jaringan dan jumlah aset default serta token penerbitan ulang yang akan dibuat.

Kita akan memulai rantai baru menggunakan parameter ini pada dua node Elements yang terhubung sekarang. Kita akan menamai aset default dengan `newasset` dan menerbitkan satu juta dan dua token penerbitan ulang `newasset`.

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

Perhatikan bahwa jumlah yang digunakan di sini adalah dalam denominasi terkecil yang dapat diterima oleh jaringan, sehingga dua ratus juta token penerbitan ulang sebenarnya sama dengan dua token utuh. Hal yang sama juga berlaku untuk denominasi koin gratis awal.

Periksa saldo dompet node kita saat ini.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Kita dapat melihat bahwa inisialisasi bekerja dengan benar.

Karena penerbitan awal aset dibuat sebagai 'siapa saja dapat membelanjakan', kita akan meminta e1 untuk mengklaim semuanya sehingga kita dapat menghapus akses e2 ke aset tersebut.

```
e1-cli getnewaddress
e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```

Perhatikan bahwa kita tidak perlu menentukan 'newasset' sebagai aset yang akan dikirim karena ini sudah menjadi aset default. dan oleh karena itu juga merupakan aset default yang digunakan untuk membayar biaya jaringan.

Di dalam Elements, Anda dapat mengirim beberapa jenis aset ke alamat yang sama, sehingga kita dapat menggunakan kembali alamat yang baru saja kita buat untuk menerima aset default, dan menggunakannya sebagai alamat tujuan untuk token yang diterbitkan ulang.

```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Konfirmasikan transaksi.

```
e1-cli generate 101
```

Kita akan memeriksa bahwa e1 adalah satu-satunya pemegang aset dan token penerbitan ulang sekarang.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Yang bisa kita lihat memang demikian.

Sekarang kita akan mengirimkan beberapa 'aset baru' ke e2, yang saat ini memiliki saldo nol.

```
e2-cli getnewaddress
e1-cli sendtoaddress <e2-address> 500 "" "" false
```

Perhatikan bahwa kita tidak perlu menentukan jenis aset yang akan dikirim, karena `newasset` telah dibuat sebagai aset default jaringan

Mari kita kirimkan juga beberapa token penerbitan ulang untuk `newasset` ke e2.

```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Konfirmasikan transaksi.

```
e1-cli generate 101
```

Kami dapat memeriksa apakah dompet telah diperbarui.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Sekarang kita akan menerbitkan kembali beberapa aset default dari e1. Perhatikan bahwa kemampuan untuk melakukan hal ini diaktifkan oleh parameter startup initialreissuancetokens. Yang jika dihilangkan atau disetel ke nol akan menghasilkan aset default yang tidak dapat diterbitkan kembali di kemudian hari.

```
e1-cli reissueasset newasset 100
```

Kita dapat menggunakan label `newasset` daripada harus memberikan nilai id hex karena rantai Elements selalu memberi label pada aset defaultnya.

Memeriksa apakah penerbitan ulang aset default berhasil:

```
e1-cli generate 101
e1-cli getwalletinfo
```

Sekarang kita akan membuktikan bahwa karena e2 memiliki beberapa token penerbitan ulang `newasset`, maka e2 juga dapat menerbitkan ulang aset default.

```
e2-cli reissueasset newasset 100
```

Memeriksa apakah penerbitan ulang aset default oleh e2 berhasil.

```
e2-cli generate 101
e2-cli getwalletinfo
```

Pada bagian ini, kita telah menyiapkan Elements sebagai blockchain mandiri dan memeriksa apakah fungsionalitas dasar berfungsi seperti yang kita harapkan.

Kami menggunakan parameter startup untuk:

Inisialisasi blockchain Elements baru dengan aset default bernama 'newasset'.

Tentukan jumlah aset default yang akan dibuat pada inisialisasi rantai.

Buat beberapa token penerbitan ulang untuk aset bawaan dan terbitkan kembali lebih banyak aset bawaan dari kedua node.

Pada jaringan blockchain Elements mandiri kami, semua operasi transaksional lainnya akan beroperasi dengan cara yang sama seperti contoh-contoh yang dibahas di bagian utama kursus ini, tetapi akan menggunakan 'newasset' alih-alih `bitcoin` sebagai aset default dan aset biaya.

### Parameter Inisialisasi Node dan Inisialisasi Rantai

Untuk memberi tahu node Elements agar beroperasi sebagai blockchain mandiri, beberapa parameter harus digunakan bersama-sama. Kita akan melihat masing-masing parameter dan mencari tahu apa yang mereka lakukan.

#### `validatepegin=0`

Karena blockchain mandiri tidak perlu memvalidasi transaksi peg-in atau peg-out, kita perlu menonaktifkan pengecekan tersebut. Dengan pengaturan ini, Anda tidak perlu menjalankan perangkat lunak klien Bitcoin atau menyimpan salinan blockchain Bitcoin, karena jaringan Elements akan beroperasi secara independen.

#### `defaultpeggedassetname`

Ini memungkinkan Anda untuk menentukan nama aset default yang dibuat pada saat inisialisasi blockchain.

#### `initialfreecoins`

Jumlah (setara dengan unit Satoshi Bitcoin) dari aset default yang akan dibuat.

#### 'initialreissuancetokens'

Jumlah (setara dengan unit Satoshi Bitcoin) dari token penerbitan ulang untuk aset default yang akan dibuat. Tanpa ini, tidak mungkin untuk membuat lebih banyak aset default. Jika Anda tidak ingin membuat lebih banyak aset default, ini dapat diatur ke nol atau dihilangkan.

Dengan menggunakan parameter ini, hal yang umum untuk memulai sebuah simpul akan terlihat seperti ini:

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

### Operasi Dasar

Parameter `defaultpeggedassetname` akan memberikan label pada aset default. Tanpa pengaturan ini, aset default akan secara otomatis diberi nama `bitcoin`. Pada bagian sebelumnya, ketika kita mengirim aset yang kita terbitkan sendiri ke node lain, kita harus menentukan heksa aset atau label aset yang diterapkan secara lokal untuk memberi tahu Elements aset mana yang kita kirim. Karena `defaultpeggedassetname` berlaku di semua node, kita tidak perlu menamainya ketika kita mengirimnya, meskipun namanya bukan `bitcoin`. Setiap fungsi yang sebelumnya akan mengirim `bitcoin` secara default sekarang akan mengirim apa pun yang Anda pilih untuk melabeli aset default.

Jadi, mengirim 10 aset default baru ke sebuah alamat sangatlah mudah:

```
e1-cli sendtoaddress <destination address> 10 "" "" true
```

Jika Anda juga memberikan node dengan nilai untuk `initialreissuancetokens` yang lebih besar dari nol, maka Anda juga akan dapat menerbitkan kembali lebih banyak aset default, sesuatu yang tidak mungkin dilakukan jika Anda menjalankan Elements sebagai sidechain.

Untuk melakukan ini, setiap node yang memiliki sejumlah token yang terkait dengan aset default hanya perlu mengeluarkan perintah dalam formulir:

```
e1-cli reissueasset <default asset name> <amount>
```

Dengan menggunakan parameter di atas, Anda dapat mengoperasikan Elements sebagai blockchain mandiri dengan aset defaultnya sendiri, terpisah dari Bitcoin dan blockchain lainnya.

## Kesimpulan

<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>

![Video](https://youtu.be/CTMdamTZBBM?si=16LBcXvN4pBfC7lr)

Dalam kursus ini, kita telah mempelajari bahwa Elements adalah protokol jaringan sumber terbuka yang dapat diimplementasikan sebagai sidechain ke blockchain lain, atau sebagai solusi blockchain mandiri.

Kita telah melihat bahwa kode sumber dan situs web untuk Elements (https://github.com/ElementsProject/elements) dihosting di GitHub dan ada forum diskusi komunitas, seperti Build On L2 (https://community.liquid.net/c/developers/), atau Telegram Pengembang Liquid (https://t.me/liquid_devel), yang dapat digunakan untuk mempelajari lebih lanjut tentang penerapan dan pengembangan aplikasi di Elements dan Liquid. Fitur-fitur utama seperti Transaksi Rahasia dan Aset yang Diterbitkan juga dibahas, bersama dengan bagaimana anggota Federasi yang Kuat memungkinkan penandatanganan blok federasi dan mekanisme 2-Way Peg.

Langkah selanjutnya adalah menantang diri Anda dengan kuis kumulatif yang mencakup semua bagian sebelumnya, kemudian memulai perjalanan Elements Anda...semoga berhasil!

# Kesimpulan

<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>

## Ulasan & Peringkat

<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>true</isCourseReview>

## Kesimpulan

<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>

Selamat telah menyelesaikan kursus ini!

Kami sangat senang bahwa Anda telah berhasil mencapai tonggak penting dalam perjalanan pembelajaran Anda. Melalui dedikasi dan keterlibatan Anda, Anda telah memperoleh pengetahuan dan keterampilan yang berharga yang akan berguna bagi Anda dalam pengembangan profesional Anda.