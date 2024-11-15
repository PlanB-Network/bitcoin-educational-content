---
name: Pengantar Teoretis ke Jaringan Lightning
goal: Menemukan Jaringan Lightning dari perspektif teknis
objectives:
  - Memahami operasi saluran jaringan.
  - Membiasakan diri dengan istilah HTLC, LNURL, dan UTXO.
  - Menyerap pengelolaan likuiditas dan biaya LNN.
  - Mengenali Jaringan Lightning sebagai sebuah jaringan.
  - Memahami penggunaan teoretis Jaringan Lightning.
---

# Perjalanan ke Lapisan Kedua Bitcoin

Menyelami inti dari Jaringan Lightning, sebuah sistem esensial untuk masa depan transaksi Bitcoin. LNP201 adalah kursus teoretis tentang cara kerja teknis Lightning. Ini mengungkap fondasi dan mekanisme dari jaringan lapisan kedua ini, yang dirancang untuk membuat pembayaran Bitcoin cepat, ekonomis, dan dapat diskalakan.

Berkat jaringan saluran pembayarannya, Lightning memungkinkan transaksi cepat dan aman tanpa mencatat setiap pertukaran di blockchain Bitcoin. Sepanjang bab, Anda akan belajar bagaimana pembukaan, pengelolaan, dan penutupan saluran bekerja, bagaimana pembayaran dialihkan melalui node perantara secara aman sambil meminimalkan kebutuhan akan kepercayaan, dan bagaimana mengelola likuiditas. Anda akan menemukan apa itu transaksi komitmen, HTLC, kunci pembatalan, mekanisme hukuman, pengarahan bawang, dan faktur.

Baik Anda pemula Bitcoin atau pengguna yang lebih berpengalaman, kursus ini akan memberikan informasi berharga untuk memahami dan menggunakan Jaringan Lightning. Meskipun kami akan membahas beberapa dasar operasi Bitcoin di bagian pertama, sangat penting untuk menguasai dasar-dasar penemuan Satoshi sebelum menyelami LNP201.

Nikmati penemuan Anda!

+++

# Dasar-Dasar

<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>

## Memahami Jaringan Lightning

<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>

![Memahami Jaringan Lightning](https://youtu.be/PszWk046x-I)

Selamat datang di kursus LNP201, yang bertujuan untuk menjelaskan fungsi teknis dari Jaringan Lightning.

Jaringan Lightning adalah jaringan saluran pembayaran yang dibangun di atas protokol Bitcoin, bertujuan untuk memungkinkan transaksi cepat dan biaya rendah. Ini memungkinkan pembuatan saluran pembayaran antar peserta, di mana transaksi dapat dilakukan hampir secara instan dan dengan biaya minimal, tanpa harus mencatat setiap transaksi secara individu di blockchain. Dengan demikian, Jaringan Lightning berusaha untuk meningkatkan skalabilitas Bitcoin dan membuatnya dapat digunakan untuk pembayaran nilai rendah.

Sebelum menjelajahi aspek "jaringan", penting untuk memahami konsep **saluran pembayaran** di Lightning, bagaimana cara kerjanya, dan spesifikasinya. Ini adalah subjek dari bab pertama ini.

### Konsep Saluran Pembayaran

Saluran pembayaran memungkinkan dua pihak, di sini **Alice** dan **Bob**, untuk bertukar dana melalui Jaringan Lightning. Setiap protagonis memiliki sebuah node, disimbolkan dengan lingkaran, dan saluran di antara mereka diwakili oleh segmen garis.

![LNP201](assets/en/01.webp)

Dalam contoh kita, Alice memiliki 100.000 satoshi di sisinya dari saluran, dan Bob memiliki 30.000, untuk total 130.000 satoshi, yang merupakan **kapasitas saluran**.

**Tapi apa itu satoshi?**

**Satoshi** (atau "sat") adalah unit akun di Bitcoin. Mirip dengan sen untuk euro, satoshi hanyalah pecahan dari Bitcoin. Satu satoshi sama dengan **0,00000001 Bitcoin**, atau satu per seratus juta dari sebuah Bitcoin. Menggunakan satoshi menjadi semakin praktis seiring naiknya nilai Bitcoin.

### Alokasi Dana dalam Saluran
Mari kembali ke saluran pembayaran. Konsep kunci di sini adalah "**sisi dari saluran**". Setiap peserta memiliki dana di sisi saluran mereka: Alice 100.000 satoshi dan Bob 30.000. Seperti yang telah kita lihat, jumlah dana ini mewakili kapasitas total dari saluran, sebuah angka yang ditetapkan ketika dibuka.

![LNP201](assets/en/02.webp)

Mari kita ambil contoh transaksi Lightning. Jika Alice ingin mengirim 40.000 satoshi ke Bob, ini mungkin karena dia memiliki dana yang cukup (100.000 satoshi). Setelah transaksi ini, Alice akan memiliki 60.000 satoshi di sisinya dan Bob 70.000.

![LNP201](assets/en/03.webp)

**Kapasitas saluran**, pada 130.000 satoshi, tetap konstan. Yang berubah adalah alokasi dana. Sistem ini tidak memungkinkan mengirim lebih banyak dana daripada yang dimiliki seseorang. Misalnya, jika Bob ingin mengirim kembali 80.000 satoshi ke Alice, dia tidak bisa, karena dia hanya memiliki 70.000.

Cara lain untuk membayangkan alokasi dana adalah dengan memikirkan sebuah **slider** yang menunjukkan di mana dana tersebut berada di dalam saluran. Awalnya, dengan 100.000 satoshi untuk Alice dan 30.000 untuk Bob, slider secara logis berada di sisi Alice. Setelah transaksi 40.000 satoshi, slider akan bergerak sedikit ke sisi Bob, yang sekarang memiliki 70.000 satoshi.

![LNP201](assets/en/04.webp)

Representasi ini bisa berguna untuk membayangkan keseimbangan dana dalam sebuah saluran.

### Aturan Dasar dari Saluran Pembayaran

Poin pertama yang harus diingat adalah bahwa **kapasitas saluran** itu tetap. Ini agak mirip dengan diameter pipa: menentukan jumlah maksimum dana yang dapat dikirim melalui saluran sekaligus.
Mari kita ambil contoh: jika Alice memiliki 130.000 satoshi di sisinya, dia hanya dapat mengirim maksimum 130.000 satoshi ke Bob dalam satu transaksi. Namun, Bob kemudian dapat mengirim dana ini kembali ke Alice, baik sebagian atau seluruhnya.

Yang penting untuk dipahami adalah bahwa kapasitas tetap dari saluran membatasi jumlah maksimum dari satu transaksi, tetapi tidak jumlah total transaksi yang mungkin, atau volume keseluruhan dana yang ditukar dalam saluran.

**Apa yang harus Anda ambil dari bab ini?**

- Kapasitas saluran itu tetap dan menentukan jumlah maksimum yang dapat dikirim dalam satu transaksi.
- Dana dalam saluran didistribusikan antara dua peserta, dan masing-masing hanya dapat mengirim ke yang lain dana yang mereka miliki di sisinya.
- Jaringan Lightning dengan demikian memungkinkan pertukaran dana yang cepat dan efisien, sambil menghormati batasan yang diberlakukan oleh kapasitas saluran.

Ini adalah akhir dari bab pertama ini, di mana kami telah meletakkan dasar untuk Jaringan Lightning. Dalam bab-bab berikutnya, kita akan melihat bagaimana membuka saluran dan mendalami konsep-konsep yang dibahas di sini.

## Bitcoin, Alamat, UTXO, dan Transaksi

<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>

![bitcoin, alamat, utxo, dan transaksi](https://youtu.be/cadCJ2V7zTg)
Bab ini cukup spesial karena tidak akan langsung didedikasikan untuk Lightning, melainkan untuk Bitcoin. Memang, Lightning Network adalah lapisan di atas Bitcoin. Oleh karena itu, sangat penting untuk memahami beberapa konsep fundamental Bitcoin untuk benar-benar mengerti cara kerja Lightning di bab-bab selanjutnya. Dalam bab ini, kita akan mengulas dasar-dasar alamat penerima Bitcoin, UTXOs, serta cara kerja transaksi Bitcoin.

### Alamat Bitcoin, Kunci Privat, dan Kunci Publik

Alamat Bitcoin adalah serangkaian karakter yang berasal dari **kunci publik**, yang sendiri dihitung dari **kunci privat**. Seperti yang Anda pasti tahu, ini digunakan untuk mengunci bitcoin, yang setara dengan menerima mereka di dompet kita.

Kunci privat adalah elemen rahasia yang **tidak boleh pernah dibagikan**, sementara kunci publik dan alamat dapat dibagikan tanpa risiko keamanan (pembukaan mereka hanya mewakili risiko terhadap privasi Anda). Berikut adalah representasi umum yang akan kita adopsi sepanjang pelatihan ini:

- **Kunci privat** akan diwakili **secara vertikal**.
- **Kunci publik** akan diwakili **secara horizontal**.
- Warna mereka menunjukkan siapa yang memilikinya (Alice dalam oranye dan Bob dalam hitam...).

### Transaksi Bitcoin: Mengirim Dana dan Skrip

Di Bitcoin, sebuah transaksi melibatkan pengiriman dana dari satu alamat ke alamat lain. Mari kita ambil contoh Alice mengirim 0.002 Bitcoin ke Bob. Alice menggunakan kunci privat yang terkait dengan alamatnya untuk **menandatangani** transaksi, dengan demikian membuktikan bahwa dia memang dapat menghabiskan dana tersebut. Tapi apa sebenarnya yang terjadi di balik transaksi ini? Dana pada alamat Bitcoin dikunci oleh **skrip**, semacam mini-program yang memberlakukan kondisi tertentu untuk menghabiskan dana.

Skrip yang paling umum memerlukan tanda tangan dengan kunci privat yang terkait dengan alamat. Ketika Alice menandatangani transaksi dengan kunci privatnya, dia **membuka skrip** yang mengunci dana, dan mereka kemudian dapat ditransfer. Transfer dana melibatkan penambahan skrip baru pada dana ini, menetapkan bahwa untuk menghabiskannya kali ini, tanda tangan kunci privat **Bob** akan diperlukan.

![LNP201](assets/en/05.webp)

### UTXOs: Unspent Transaction Outputs

Di Bitcoin, apa yang sebenarnya kita tukarkan bukanlah bitcoin secara langsung, melainkan **UTXOs** (_Unspent Transaction Outputs_), yang berarti "output transaksi yang belum dihabiskan".

UTXO adalah sepotong bitcoin yang bisa bernilai berapa saja, misalnya, **2.000 bitcoin**, **8 bitcoin**, atau bahkan **8.000 sats**. Setiap UTXO dikunci oleh skrip, dan untuk menghabiskannya, seseorang harus memenuhi kondisi skrip, seringkali sebuah tanda tangan dengan kunci privat yang sesuai dengan alamat penerima tertentu.

UTXOs tidak dapat dibagi. Setiap kali mereka digunakan untuk menghabiskan jumlah dalam bitcoin yang mereka wakili, itu harus dilakukan secara keseluruhan. Ini sedikit seperti uang kertas: jika Anda memiliki uang kertas €10 dan Anda berhutang kepada tukang roti €5, Anda tidak bisa hanya memotong uang kertas itu menjadi dua. Anda harus memberikannya uang kertas €10, dan dia akan memberi Anda €5 kembali. Prinsip yang sama persis berlaku untuk UTXOs di Bitcoin! Misalnya, ketika Alice membuka skrip dengan kunci privatnya, dia membuka seluruh UTXO. Jika dia ingin mengirim hanya sebagian dari dana yang diwakili oleh UTXO ini ke Bob, dia dapat "memecah"nya menjadi beberapa yang lebih kecil. Dia kemudian akan mengirim 0.0015 BTC ke Bob dan mengirim sisanya, 0.0005 BTC, ke **alamat kembalian**.

Berikut adalah contoh transaksi dengan 2 output:
- UTXO sebesar 0,0015 BTC untuk Bob, dikunci oleh skrip yang memerlukan tanda tangan kunci privat Bob.
- UTXO sebesar 0,0005 BTC untuk Alice, dikunci oleh skrip yang memerlukan tanda tangan kunci privatnya sendiri.

![LNP201](assets/en/06.webp)

### Alamat Multi-signature

Selain alamat sederhana yang dihasilkan dari satu kunci publik, juga dimungkinkan untuk membuat **alamat multi-signature** dari beberapa kunci publik. Kasus yang sangat menarik untuk Lightning Network adalah **alamat multi-signature 2/2**, yang dihasilkan dari dua kunci publik:

![LNP201](assets/en/07.webp)

Untuk menghabiskan dana yang dikunci dengan alamat multi-signature 2/2 ini, diperlukan tanda tangan dengan dua kunci privat yang terkait dengan kunci publik.

![LNP201](assets/en/08.webp)

Tipe alamat ini secara tepat merupakan representasi di blockchain Bitcoin dari saluran pembayaran pada Lightning Network.

**Apa yang harus Anda pahami dari bab ini?**

- **Alamat Bitcoin** berasal dari kunci publik, yang sendiri berasal dari kunci privat.
- Dana pada Bitcoin dikunci oleh **skrip**, dan untuk menghabiskan dana tersebut, seseorang harus memenuhi skrip, yang umumnya melibatkan penyediaan tanda tangan dengan kunci privat yang sesuai.
- **UTXOs** adalah potongan-potongan bitcoin yang dikunci oleh skrip, dan setiap transaksi pada Bitcoin terdiri dari membuka UTXO dan kemudian menciptakan satu atau lebih yang baru sebagai gantinya.
- **Alamat multi-signature 2/2** memerlukan tanda tangan dari dua kunci privat untuk menghabiskan dana. Alamat spesifik ini digunakan dalam konteks Lightning untuk membuat saluran pembayaran.

Bab ini tentang Bitcoin telah memungkinkan kita untuk meninjau beberapa konsep esensial untuk apa yang akan diikuti. Dalam bab selanjutnya, kita akan secara khusus menemukan bagaimana pembukaan saluran pada Lightning Network bekerja.

# Membuka dan Menutup Saluran

<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>

## Pembukaan Saluran

<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>

![open a channel](https://youtu.be/B2caBC0Rxko)

Dalam bab ini, kita akan melihat lebih rinci bagaimana membuka saluran pembayaran pada Lightning Network dan memahami hubungan antara operasi ini dan sistem Bitcoin yang mendasarinya.

### Saluran Lightning

Seperti yang kita lihat di bab pertama, **saluran pembayaran** pada Lightning dapat dibandingkan dengan "pipa" untuk bertukar dana antara dua peserta (**Alice** dan **Bob** dalam contoh kita). Kapasitas dari saluran ini sesuai dengan jumlah dana yang tersedia di setiap sisi. Dalam contoh kita, Alice memiliki **100.000 satoshi** dan Bob memiliki **30.000 satoshi**, memberikan **kapasitas total** sebesar **130.000 satoshi**.

![LNP201](assets/en/09.webp)

### Tingkatan Pertukaran Informasi

Sangat penting untuk membedakan dengan jelas berbagai tingkatan pertukaran pada Lightning Network:

- **Komunikasi peer-to-peer (protokol Lightning)**: Ini adalah pesan yang dikirimkan node-node Lightning satu sama lain untuk berkomunikasi. Kami akan merepresentasikan pesan-pesan ini dengan garis putus-putus hitam dalam diagram kami.
- **Saluran pembayaran (protokol Lightning)**: Ini adalah jalur untuk bertukar dana pada Lightning, yang akan kami representasikan dengan garis hitam padat.
- **Transaksi Bitcoin (protokol Bitcoin)**: Ini adalah transaksi yang dilakukan onchain, yang akan kami representasikan dengan garis oranye.

![LNP201](assets/en/10.webp)
Penting untuk dicatat bahwa sebuah node Lightning dapat berkomunikasi melalui protokol P2P tanpa membuka saluran, tetapi untuk bertukar dana, sebuah saluran diperlukan.
### Langkah-langkah Membuka Saluran Lightning

1. **Pertukaran pesan**: Alice ingin membuka saluran dengan Bob. Dia mengiriminya pesan yang berisi jumlah yang ingin dia setorkan ke dalam saluran (130.000 sats) dan kunci publiknya. Bob merespons dengan membagikan kunci publiknya sendiri.

![LNP201](assets/en/11.webp)

2. **Pembuatan alamat multisignature**: Dengan kedua kunci publik ini, Alice membuat **alamat multisignature 2/2**, yang berarti dana yang nantinya akan disetorkan pada alamat ini akan memerlukan kedua tanda tangan (Alice dan Bob) untuk dihabiskan.

![LNP201](assets/en/12.webp)

3. **Transaksi setoran**: Alice menyiapkan transaksi Bitcoin untuk menyetorkan dana pada alamat multisignature ini. Sebagai contoh, dia mungkin memutuskan untuk mengirim **130.000 satoshi** ke alamat multisignature ini. Transaksi ini **dibuat tetapi belum dipublikasikan** di blockchain.

![LNP201](assets/en/13.webp)

4. **Transaksi penarikan**: Sebelum mempublikasikan transaksi setoran, Alice membuat transaksi penarikan sehingga dia dapat memulihkan dananya jika terjadi masalah dengan Bob. Memang, setelah Alice mempublikasikan transaksi setoran, satoshinya akan terkunci pada alamat multisignature 2/2 yang memerlukan kedua tanda tangan (Alice dan Bob) untuk dibuka. Alice melindungi diri dari risiko kehilangan ini dengan membuat transaksi penarikan yang memungkinkan dia untuk memulihkan dananya.

![LNP201](assets/en/14.webp)

5. **Tanda tangan Bob**: Alice mengirim transaksi setoran kepada Bob sebagai bukti dan memintanya untuk menandatangani transaksi penarikan. Setelah tanda tangan Bob diperoleh pada transaksi penarikan, Alice merasa yakin bahwa dia dapat memulihkan dananya kapan saja, karena hanya tanda tangan dia sendiri yang sekarang diperlukan untuk membuka multisignature.

![LNP201](assets/en/15.webp)

6. **Publikasi transaksi setoran**: Setelah tanda tangan Bob diperoleh, Alice dapat mempublikasikan transaksi setoran di blockchain Bitcoin, dengan demikian secara resmi membuka saluran Lightning antara kedua pengguna.

![LNP201](assets/en/16.webp)

### Kapan saluran dianggap terbuka?

Saluran dianggap terbuka setelah transaksi setoran dimasukkan dalam blok Bitcoin dan telah mencapai kedalaman konfirmasi tertentu (jumlah blok berikutnya).

**Apa yang harus Anda ingat dari bab ini?**

- Membuka saluran dimulai dengan pertukaran **pesan** antara kedua pihak (pertukaran jumlah dan kunci publik).
- Saluran dibentuk dengan membuat **alamat multisignature 2/2** dan menyetorkan dana ke dalamnya melalui transaksi Bitcoin.
- Orang yang membuka saluran memastikan mereka dapat **memulihkan dana mereka** melalui transaksi penarikan yang ditandatangani oleh pihak lain sebelum mempublikasikan transaksi setoran.

Di bab selanjutnya, kita akan menjelajahi cara kerja teknis transaksi Lightning dalam sebuah saluran.

## Transaksi Komitmen

<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>

![Transaksi Lightning & transaksi komitmen](https://youtu.be/aPqI34tpypM)

Dalam bab ini, kita akan menemukan fungsi teknis dari sebuah transaksi dalam saluran di Jaringan Lightning, yaitu, ketika dana dipindahkan dari satu sisi saluran ke sisi lainnya.

### Pengingat siklus hidup saluran
Seperti yang telah dilihat sebelumnya, sebuah saluran Lightning dimulai dengan **pembukaan** melalui transaksi Bitcoin. Saluran tersebut dapat **ditutup** kapan saja, juga melalui transaksi Bitcoin. Di antara kedua momen tersebut, hampir tak terbatas jumlah transaksi yang dapat dilakukan dalam saluran, tanpa harus melalui blockchain Bitcoin. Mari kita lihat apa yang terjadi selama transaksi dalam saluran.

![LNP201](assets/en/17.webp)

### Kondisi Awal Saluran

Pada saat membuka saluran, Alice menyetorkan **130.000 satoshi** pada alamat multisignature dari saluran. Dengan demikian, dalam kondisi awal, semua dana berada di sisi Alice. Sebelum membuka saluran, Alice juga membuat Bob menandatangani sebuah **transaksi penarikan**, yang akan memungkinkan dia untuk mengambil kembali dananya jika dia ingin menutup saluran.

![LNP201](assets/en/18.webp)

### Transaksi yang Tidak Dipublikasikan: Transaksi Komitmen

Ketika Alice melakukan transaksi dalam saluran untuk mengirim dana ke Bob, sebuah transaksi Bitcoin baru dibuat untuk mencerminkan perubahan ini dalam distribusi dana. Transaksi ini, yang disebut **transaksi komitmen**, tidak dipublikasikan di blockchain tetapi mewakili kondisi baru saluran setelah transaksi Lightning.

Mari kita ambil contoh dengan Alice mengirim 30.000 satoshi ke Bob:

- **Awalnya**: Alice memiliki 130.000 satoshi.
- **Setelah transaksi**: Alice memiliki 100.000 satoshi, dan Bob 30.000 satoshi.
  Untuk memvalidasi transfer ini, Alice dan Bob membuat **transaksi Bitcoin baru yang tidak dipublikasikan** yang akan mengirim **100.000 satoshi ke Alice** dan **30.000 satoshi ke Bob** dari alamat multisignature. Kedua pihak membangun transaksi ini secara independen, tetapi dengan data yang sama (jumlah dan alamat). Setelah dibangun, masing-masing menandatangani transaksi dan bertukar tanda tangan dengan yang lain. Ini memungkinkan salah satu pihak untuk mempublikasikan transaksi kapan saja jika diperlukan untuk memulihkan bagian mereka dari saluran di blockchain Bitcoin utama.
  ![LNP201](assets/en/19.webp)

### Proses Transfer: Faktur

Ketika Bob ingin menerima dana, dia mengirim Alice sebuah **_faktur_** untuk 30.000 satoshi. Alice kemudian melanjutkan untuk membayar faktur ini dengan memulai transfer dalam saluran. Seperti yang telah kita lihat, proses ini bergantung pada pembuatan dan penandatanganan **transaksi komitmen** baru.

Setiap transaksi komitmen mewakili distribusi dana baru dalam saluran setelah transfer. Dalam contoh ini, setelah transaksi, Bob memiliki 30.000 satoshi dan Alice memiliki 100.000 satoshi. Jika salah satu dari dua peserta memutuskan untuk mempublikasikan transaksi komitmen ini di blockchain, itu akan mengakibatkan penutupan saluran dan dana akan didistribusikan sesuai dengan distribusi terakhir ini.

![LNP201](assets/en/20.webp)

### Kondisi Baru Setelah Transaksi Kedua

Mari kita ambil contoh lain: setelah transaksi pertama di mana Alice mengirim 30.000 satoshi ke Bob, Bob memutuskan untuk mengirim **10.000 satoshi kembali ke Alice**. Ini menciptakan kondisi baru saluran. **Transaksi komitmen** baru akan mewakili distribusi yang diperbarui ini:

- **Alice** sekarang memiliki **110.000 satoshi**.
- **Bob** memiliki **20.000 satoshi**.

![LNP201](assets/en/21.webp)

Sekali lagi, transaksi ini tidak dipublikasikan di blockchain tetapi dapat dipublikasikan kapan saja jika saluran ditutup.

Secara ringkas, ketika dana ditransfer dalam saluran Lightning:
- Alice dan Bob membuat **transaksi komitmen** baru, yang mencerminkan distribusi dana yang baru.
- Transaksi Bitcoin ini **ditandatangani** oleh kedua belah pihak, namun **tidak dipublikasikan** di blockchain Bitcoin selama saluran tetap terbuka.
- Transaksi komitmen memastikan bahwa setiap peserta dapat memulihkan dana mereka kapan saja di blockchain Bitcoin dengan mempublikasikan transaksi terakhir yang ditandatangani.

Namun, sistem ini memiliki kelemahan potensial, yang akan kita bahas di bab berikutnya. Kita akan melihat bagaimana setiap peserta dapat melindungi diri mereka dari upaya curang oleh pihak lain.

## Kunci Pembatalan

<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>
![transaksi bagian 2](https://youtu.be/RRvoVTLRJ84)
Dalam bab ini, kita akan mendalami lebih dalam tentang bagaimana transaksi bekerja di Jaringan Lightning dengan membahas mekanisme yang ada untuk melindungi dari kecurangan, memastikan bahwa setiap pihak mematuhi aturan dalam sebuah saluran.

### Pengingat: Transaksi Komitmen

Seperti yang telah dilihat sebelumnya, transaksi di Lightning bergantung pada **transaksi komitmen** yang tidak dipublikasikan. Transaksi ini mencerminkan distribusi dana saat ini di saluran. Ketika transaksi Lightning baru dilakukan, transaksi komitmen baru dibuat dan ditandatangani oleh kedua belah pihak untuk mencerminkan keadaan baru saluran.

Mari kita ambil contoh sederhana:

- **Keadaan awal**: Alice memiliki **100.000 satoshi**, Bob **30.000 satoshi**.
- Setelah transaksi di mana Alice mengirim **40.000 satoshi** ke Bob, transaksi komitmen baru mendistribusikan dana sebagai berikut:
  - Alice: **60.000 satoshi**
  - Bob: **70.000 satoshi**

![LNP201](assets/en/22.webp)

Kapan saja, kedua belah pihak dapat mempublikasikan **transaksi komitmen terakhir** yang ditandatangani untuk menutup saluran dan memulihkan dana mereka.

### Kekurangan: Kecurangan dengan Memublikasikan Transaksi Lama

Masalah potensial muncul jika salah satu pihak memutuskan untuk **berbuat curang** dengan mempublikasikan transaksi komitmen lama. Misalnya, Alice dapat mempublikasikan transaksi komitmen yang lebih lama di mana dia memiliki **100.000 satoshi**, meskipun sekarang dia hanya memiliki **60.000** secara nyata. Ini akan memungkinkan dia untuk mencuri **40.000 satoshi** dari Bob.

![LNP201](assets/en/23.webp)

Lebih buruk lagi, Alice dapat mempublikasikan transaksi penarikan pertama, yang sebelum saluran dibuka, di mana dia memiliki **130.000 satoshi**, dan dengan demikian mencuri seluruh dana saluran.

![LNP201](assets/en/24.webp)

### Solusi: Kunci Pembatalan dan Timelock

Untuk mencegah jenis kecurangan ini oleh Alice, di Jaringan Lightning, **mekanisme keamanan** ditambahkan ke transaksi komitmen:

1. **Timelock**: Setiap transaksi komitmen mencakup timelock untuk dana Alice. Timelock adalah primitif kontrak pintar yang menetapkan kondisi waktu yang harus dipenuhi agar transaksi dapat ditambahkan ke blok. Ini berarti bahwa Alice tidak dapat memulihkan dana nya sampai sejumlah blok telah berlalu jika dia mempublikasikan salah satu transaksi komitmen. Timelock ini mulai berlaku dari konfirmasi transaksi komitmen. Durasi nya umumnya proporsional dengan ukuran saluran, tetapi juga dapat dikonfigurasi secara manual.
2. **Kunci Pembatalan**: Dana Alice juga dapat segera dihabiskan oleh Bob jika dia memiliki **kunci pembatalan**. Kunci ini terdiri dari rahasia yang dipegang oleh Alice dan rahasia yang dipegang oleh Bob. Perhatikan bahwa rahasia ini berbeda untuk setiap transaksi komitmen.
Berikut adalah terjemahan dari teks yang diberikan:

Berkat dua mekanisme gabungan ini, Bob memiliki waktu untuk mendeteksi upaya Alice untuk menipu, dan untuk menghukumnya dengan mengambil kembali outputnya menggunakan kunci pembatalan, yang bagi Bob berarti memulihkan semua dana dari saluran tersebut. Transaksi komitmen baru kita sekarang akan terlihat seperti ini:
![LNP201](assets/en/25.webp)

Mari kita rinci bersama fungsi mekanisme ini.

### Proses Pembaruan Transaksi

Ketika Alice dan Bob memperbarui status saluran dengan transaksi Lightning baru, mereka bertukar terlebih dahulu **rahasia** masing-masing untuk transaksi komitmen sebelumnya (yang akan menjadi usang dan bisa memungkinkan salah satu dari mereka untuk menipu). Ini berarti bahwa, dalam status baru saluran:

- Alice dan Bob memiliki transaksi komitmen baru yang mewakili distribusi dana saat ini setelah transaksi Lightning.
- Masing-masing memiliki rahasia transaksi sebelumnya dari yang lain, yang memungkinkan mereka untuk menggunakan kunci pembatalan hanya jika salah satu dari mereka mencoba menipu dengan mempublikasikan transaksi dengan status lama di mempool node Bitcoin. Memang, untuk menghukum pihak lain, diperlukan untuk memegang kedua rahasia dan transaksi komitmen pihak lain, yang mencakup input yang ditandatangani. Tanpa transaksi ini, kunci pembatalan sendirian tidak berguna. Satu-satunya cara untuk mendapatkan transaksi ini adalah dengan mengambilnya dari mempool (dalam transaksi yang menunggu konfirmasi) atau dalam transaksi yang dikonfirmasi di blockchain selama timelock, yang membuktikan bahwa pihak lain mencoba menipu, baik sengaja maupun tidak.

Mari kita ambil contoh untuk memahami proses ini dengan baik:

1. **Keadaan Awal**: Alice memiliki **100.000 satoshi**, Bob **30.000 satoshi**.

![LNP201](assets/en/26.webp)

2. Bob ingin menerima 40.000 satoshi dari Alice melalui saluran Lightning mereka. Untuk melakukan ini:
   - Dia mengirimkan faktur bersama dengan rahasianya untuk kunci pembatalan transaksi komitmen sebelumnya.
   - Sebagai tanggapan, Alice memberikan tanda tangannya untuk transaksi komitmen baru Bob, serta rahasianya untuk kunci pembatalan transaksi sebelumnya.
   - Akhirnya, Bob mengirimkan tanda tangannya untuk transaksi komitmen baru Alice.
   - Pertukaran ini memungkinkan Alice untuk mengirim **40.000 satoshi** kepada Bob di Lightning melalui saluran mereka, dan transaksi komitmen baru sekarang mencerminkan distribusi dana baru ini.

![LNP201](assets/en/27.webp)

3. Jika Alice mencoba mempublikasikan transaksi komitmen lama di mana dia masih memiliki **100.000 satoshi**, Bob, setelah mendapatkan kunci pembatalan, dapat segera memulihkan dana menggunakan kunci ini, sementara Alice diblokir oleh timelock.

![LNP201](assets/en/28.webp)

Meskipun, dalam kasus ini, Bob tidak memiliki kepentingan ekonomi untuk mencoba menipu, jika dia melakukannya, Alice juga mendapat manfaat dari perlindungan simetris yang memberinya jaminan yang sama.

**Apa yang harus Anda ambil dari bab ini?**

**Transaksi komitmen** di Lightning Network mencakup mekanisme keamanan yang mengurangi baik risiko menipu maupun insentif untuk melakukannya. Sebelum menandatangani transaksi komitmen baru, Alice dan Bob bertukar **rahasia** masing-masing untuk transaksi komitmen sebelumnya. Jika Alice mencoba mempublikasikan transaksi komitmen lama, Bob dapat menggunakan **kunci pembatalan** untuk memulihkan semua dana sebelum Alice bisa (karena dia diblokir oleh timelock), yang menghukumnya karena mencoba menipu.

Sistem keamanan ini memastikan bahwa peserta mematuhi aturan Lightning Network, dan mereka tidak dapat memperoleh keuntungan dari mempublikasikan transaksi komitmen lama.
Pada titik ini dalam pelatihan, Anda sekarang sudah mengetahui bagaimana saluran Lightning dibuka dan bagaimana transaksi dalam saluran ini bekerja. Pada bab selanjutnya, kita akan menemukan berbagai cara untuk menutup saluran dan memulihkan bitcoin Anda di blockchain utama.
## Penutupan Saluran

<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>

![tutup saluran](https://youtu.be/FVmQvNpVW8Y)

Dalam bab ini, kita akan membahas **penutupan saluran** di Jaringan Lightning, yang dilakukan melalui transaksi Bitcoin, sama seperti membuka saluran. Setelah melihat bagaimana transaksi dalam saluran bekerja, sekarang saatnya untuk melihat cara menutup saluran dan memulihkan dana di blockchain Bitcoin.

### Pengingat siklus hidup saluran

**Siklus hidup saluran** dimulai dengan **pembukaannya**, melalui transaksi Bitcoin, kemudian transaksi Lightning dilakukan di dalamnya, dan akhirnya, ketika para pihak ingin memulihkan dana mereka, saluran **ditutup** melalui transaksi Bitcoin kedua. Transaksi perantara yang dibuat di Lightning diwakili oleh **transaksi komitmen** yang tidak dipublikasikan.

![LNP201](assets/en/29.webp)

### Tiga jenis penutupan saluran

Ada tiga cara utama untuk menutup saluran ini, yang dapat disebut **yang baik, yang kasar, dan yang nakal** (terinspirasi oleh Andreas Antonopoulos dalam _Mastering the Lightning Network_):

1. **Yang Baik**: **penutupan kooperatif**, di mana Alice dan Bob setuju untuk menutup saluran.
2. **Yang Buruk**: **penutupan paksa**, di mana salah satu pihak memutuskan untuk menutup saluran dengan jujur, tetapi tanpa persetujuan pihak lain.
3. **Yang Jelek**: **penutupan dengan kecurangan**, di mana salah satu pihak mencoba mencuri dana dengan mempublikasikan transaksi komitmen lama (apapun kecuali yang terakhir, yang mencerminkan distribusi dana yang sebenarnya dan adil).

Mari kita ambil contoh:

- Alice memiliki **100.000 satoshi** dan Bob **30.000 satoshi**.
- Distribusi ini tercermin dalam **2 transaksi komitmen** (satu per pengguna) yang tidak dipublikasikan, tetapi bisa saja dalam kejadian penutupan saluran.

![LNP201](assets/en/30.webp)

### Yang Baik: penutupan kooperatif

Dalam **penutupan kooperatif**, Alice dan Bob setuju untuk menutup saluran. Begini caranya:

1. Alice mengirim pesan ke Bob melalui protokol komunikasi Lightning untuk mengusulkan penutupan saluran.
2. Bob setuju, dan kedua pihak tidak melakukan transaksi lebih lanjut di saluran.

![LNP201](assets/en/31.webp)

3. Alice dan Bob bersama-sama menegosiasikan biaya dari **transaksi penutupan**. Biaya ini umumnya dihitung berdasarkan pasar biaya Bitcoin pada saat penutupan. Penting untuk dicatat bahwa **selalu orang yang membuka saluran** (Alice dalam contoh kita) yang membayar biaya penutupan.
4. Mereka membuat **transaksi penutupan** baru. Transaksi ini menyerupai transaksi komitmen, tetapi tanpa timelock atau mekanisme pencabutan, karena kedua pihak bekerja sama dan tidak ada risiko kecurangan. Transaksi penutupan kooperatif ini oleh karena itu berbeda dari transaksi komitmen.
Misalnya, jika Alice memiliki **100.000 satoshi** dan Bob **30.000 satoshi**, transaksi penutupan akan mengirim **100.000 satoshi** ke alamat Alice dan **30.000 satoshi** ke alamat Bob, tanpa batasan timelock. Setelah transaksi ini ditandatangani oleh kedua belah pihak, Alice akan mempublikasikannya. Setelah transaksi dikonfirmasi di blockchain Bitcoin, saluran Lightning akan resmi ditutup.
![LNP201](assets/en/32.webp)

**Penutupan kooperatif** adalah metode penutupan yang disukai karena cepat (tanpa timelock) dan biaya transaksi disesuaikan menurut kondisi pasar Bitcoin saat ini. Ini menghindari pembayaran yang terlalu sedikit, yang bisa berisiko memblokir transaksi di mempool, atau membayar terlalu banyak secara tidak perlu, yang mengakibatkan kerugian finansial yang tidak perlu bagi para peserta.

### Yang Buruk: penutupan paksa

Ketika node Alice mengirim pesan ke Bob meminta penutupan kooperatif, jika dia tidak merespon (misalnya, karena gangguan internet atau masalah teknis), Alice dapat melanjutkan dengan **penutupan paksa** dengan mempublikasikan **transaksi komitmen terakhir yang ditandatangani**.
Dalam kasus ini, Alice akan mempublikasikan transaksi komitmen terakhir, yang mencerminkan keadaan saluran pada saat transaksi Lightning terakhir terjadi dengan distribusi dana yang benar.

![LNP201](assets/en/33.webp)

Transaksi ini mencakup **timelock** untuk dana Alice, membuat penutupan menjadi lebih lambat.

![LNP201](assets/en/34.webp)

Juga, biaya dari transaksi komitmen mungkin tidak sesuai pada saat penutupan, karena ditetapkan ketika transaksi dibuat, terkadang beberapa bulan sebelumnya. Umumnya, klien Lightning memperkirakan biaya lebih tinggi untuk menghindari masalah di masa depan, tetapi ini dapat menyebabkan biaya yang berlebihan, atau sebaliknya terlalu rendah.

Secara ringkas, **penutupan paksa** adalah opsi terakhir ketika rekan tidak lagi merespon. Ini lebih lambat dan kurang ekonomis daripada penutupan kooperatif. Oleh karena itu, sebisa mungkin harus dihindari.

### Kecurangan: penipuan

Akhirnya, penutupan dengan **kecurangan** terjadi ketika salah satu pihak mencoba mempublikasikan transaksi komitmen lama, seringkali di mana mereka memiliki lebih banyak dana daripada yang seharusnya. Misalnya, Alice mungkin mempublikasikan transaksi lama di mana dia memiliki **120.000 satoshi**, sementara dia sebenarnya hanya memiliki **100.000** sekarang.

![LNP201](assets/en/35.webp)

Bob, untuk mencegah kecurangan ini, memantau blockchain Bitcoin dan mempoolnya untuk memastikan Alice tidak mempublikasikan transaksi lama. Jika Bob mendeteksi upaya kecurangan, dia dapat menggunakan **kunci pembatalan** untuk mengambil dana Alice dan menghukumnya dengan mengambil seluruh dana saluran. Karena Alice diblokir oleh timelock pada outputnya, Bob memiliki waktu untuk menghabiskannya tanpa timelock di sisinya untuk memulihkan seluruh jumlah pada alamat yang dia miliki.

![LNP201](assets/en/36.webp)

Jelas, kecurangan berpotensi berhasil jika Bob tidak bertindak dalam waktu yang ditetapkan oleh timelock pada output Alice. Dalam kasus ini, output Alice dibuka, memungkinkannya untuk mengkonsumsinya untuk membuat output baru ke alamat yang dia kontrol.

**Apa yang harus Anda ambil dari bab ini?**

Ada tiga cara untuk menutup saluran:

1. **Penutupan Kooperatif**: Cepat dan kurang mahal, di mana kedua belah pihak setuju untuk menutup saluran dan mempublikasikan transaksi penutupan yang disesuaikan.
2. **Penutupan Paksa**: Kurang diinginkan, karena bergantung pada penerbitan transaksi komitmen, dengan biaya yang mungkin tidak sesuai dan timelock, yang memperlambat penutupan.
3. **Kecurangan**: Jika salah satu pihak mencoba mencuri dana dengan mempublikasikan transaksi lama, pihak lain dapat menggunakan kunci pembatalan untuk menghukum kecurangan tersebut.
Dalam bab-bab berikutnya, kita akan menjelajahi Jaringan Lightning dari perspektif yang lebih luas, berfokus pada bagaimana jaringannya beroperasi.

# Jaringan Likuiditas

<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>

## Jaringan Lightning

<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>

![jaringan lightning](https://youtu.be/RAZAa3v41DM)

Dalam bab ini, kita akan menjelajahi bagaimana pembayaran di Jaringan Lightning dapat mencapai penerima meskipun mereka tidak terhubung langsung oleh saluran pembayaran. Lightning memang merupakan **jaringan dari saluran pembayaran**, yang memungkinkan dana dikirim ke node yang jauh melalui saluran dari peserta lain. Kita akan menemukan bagaimana pembayaran dialihkan melintasi jaringan, bagaimana likuiditas bergerak antar saluran, dan bagaimana biaya transaksi dihitung.

### Jaringan Saluran Pembayaran

Di Jaringan Lightning, sebuah transaksi sesuai dengan transfer dana antara dua node. Seperti yang terlihat di bab-bab sebelumnya, diperlukan untuk membuka saluran dengan seseorang untuk melakukan transaksi Lightning. Saluran ini memungkinkan untuk hampir tak terbatas jumlah transaksi off-chain sebelum menutupnya untuk mengklaim kembali saldo on-chain. Namun, metode ini memiliki kelemahan memerlukan saluran langsung dengan orang lain untuk menerima atau mengirim dana, yang menyiratkan transaksi pembukaan dan penutupan untuk setiap saluran. Jika saya berencana untuk melakukan sejumlah besar pembayaran dengan orang ini, membuka dan menutup saluran menjadi hemat biaya. Sebaliknya, jika saya hanya perlu melakukan beberapa transaksi Lightning, membuka saluran langsung tidak menguntungkan, karena itu akan menghabiskan biaya saya 2 transaksi on-chain untuk jumlah transaksi off-chain yang terbatas. Kasus ini mungkin terjadi, misalnya, ketika ingin membayar dengan Lightning di pedagang tanpa berencana untuk kembali.

Untuk menyelesaikan masalah ini, Jaringan Lightning memungkinkan untuk mengalihkan pembayaran melalui beberapa saluran dan node perantara, sehingga memungkinkan transaksi tanpa saluran langsung dengan orang lain.

Misalnya, bayangkan bahwa:

- **Alice** (dalam oranye) memiliki saluran dengan **Suzie** (dalam abu-abu) dengan **100.000 satoshi** di sisinya dan **30.000 satoshi** di sisi Suzie.
- **Suzie** memiliki saluran dengan **Bob** di mana dia memiliki **250.000 satoshi** dan di mana Bob tidak memiliki satoshi.

![LNP201](assets/en/37.webp)

Jika Alice ingin mengirim dana ke Bob tanpa membuka saluran langsung dengannya, dia harus melalui Suzie, dan setiap saluran perlu menyesuaikan likuiditas di setiap sisi. **Satoshi yang dikirim tetap dalam saluran masing-masing**; mereka sebenarnya tidak "melintasi" saluran, tetapi transfer dilakukan melalui penyesuaian likuiditas internal di setiap saluran.

Misalkan Alice ingin mengirim **50.000 satoshi** ke Bob:

1. **Alice** mengirim 50.000 satoshi ke **Suzie** di saluran bersama mereka.
2. **Suzie** mereplikasi transfer ini dengan mengirim 50.000 satoshi ke **Bob** di saluran mereka.

![LNP201](assets/en/38.webp)
Dengan demikian, pembayaran dialihkan ke Bob melalui pergerakan likuiditas di setiap saluran. Di akhir operasi, Alice berakhir dengan 50.000 satoshi. Dia memang telah mentransfer 50.000 satoshi karena awalnya, dia memiliki 100.000. Bob, di sisinya, berakhir dengan tambahan 50.000 satoshi. Untuk Suzie (node perantara), operasi ini netral: awalnya, dia memiliki 30.000 satoshi di salurannya dengan Alice dan 250.000 satoshi di salurannya dengan Bob, total 280.000 satoshi. Setelah operasi, dia memegang 80.000 satoshi di salurannya dengan Alice dan 200.000 satoshi di salurannya dengan Bob, yang merupakan jumlah yang sama seperti di awal.
Transfer ini dengan demikian dibatasi oleh **likuiditas yang tersedia** dalam arah transfer.

### Perhitungan Rute dan Batas Likuiditas

Mari kita ambil contoh teoretis dari jaringan lain dengan:

- **130.000 satoshi** di sisi Alice (dalam oranye) di salurannya dengan **Suzie** (dalam abu-abu).
- **90.000 satoshi** di sisi **Suzie** dan **200.000 satoshi** di sisi **Carol** (dalam pink).
- **150.000 satoshi** di sisi **Carol** dan **100.000 satoshi** di sisi **Bob**.

![LNP201](assets/en/39.webp)

Maksimum yang dapat Alice kirim ke Bob dalam konfigurasi ini adalah **90.000 satoshi**, karena dia dibatasi oleh likuiditas terkecil yang tersedia di saluran dari **Suzie ke Carol**. Dalam arah sebaliknya (dari Bob ke Alice), tidak ada pembayaran yang mungkin karena sisi **Suzie** di saluran dengan **Alice** tidak mengandung satoshi. Oleh karena itu, tidak ada **rute** yang dapat digunakan untuk transfer dalam arah ini.
Alice mengirim **40.000 satoshi** ke Bob melalui saluran:

1. Alice mentransfer 40.000 satoshi ke salurannya dengan Suzie.
2. Suzie mentransfer 40.000 satoshi ke Carol di saluran bersama mereka.
3. Carol akhirnya mentransfer 40.000 satoshi ke Bob.

![LNP201](assets/en/40.webp)

**Satoshi yang dikirim** di setiap saluran **tetap di saluran**, jadi satoshi yang dikirim oleh Carol ke Bob bukanlah sama dengan yang dikirim oleh Alice ke Suzie. Transfer dilakukan hanya dengan menyesuaikan likuiditas di dalam setiap saluran. Selain itu, kapasitas total saluran tetap tidak berubah.

![LNP201](assets/en/41.webp)

Seperti dalam contoh sebelumnya, setelah transaksi, node sumber (Alice) memiliki 40.000 satoshi lebih sedikit. Node perantara (Suzie dan Carol) mempertahankan jumlah total yang sama, membuat operasi netral bagi mereka. Akhirnya, node tujuan (Bob) menerima tambahan 40.000 satoshi.

Peran node perantara oleh karena itu sangat penting dalam fungsi Lightning Network. Mereka memfasilitasi transfer dengan menawarkan beberapa jalur untuk pembayaran. Untuk mendorong node ini menyediakan likuiditas mereka dan berpartisipasi dalam merutekan pembayaran, **biaya perutean** dibayarkan kepada mereka.

### Biaya Perutean

Node perantara menerapkan biaya untuk memungkinkan pembayaran melewati saluran mereka. Biaya ini ditetapkan oleh **setiap node untuk setiap saluran**. Biaya terdiri dari 2 elemen:

1. "**Biaya Dasar**": jumlah tetap per saluran, sering kali **1 sat** secara default, tetapi dapat disesuaikan.
2. "**Biaya variabel**": persentase dari jumlah yang ditransfer, dihitung dalam **bagian per juta (ppm)**. Secara default, ini adalah **1 ppm** (1 sat per juta satoshi yang ditransfer), tetapi ini juga dapat disesuaikan.
Biaya juga berbeda tergantung pada arah transfer. Misalnya, untuk transfer dari Alice ke Suzie, biaya Alice yang berlaku. Sebaliknya, dari Suzie ke Alice, biaya Suzie yang digunakan.

Sebagai contoh, untuk sebuah saluran antara Alice dan Suzie, kita bisa memiliki:

- **Alice**: biaya dasar 1 sat dan 1 ppm untuk biaya variabel.
- **Suzie**: biaya dasar 0.5 sat dan 10 ppm untuk biaya variabel.

![LNP201](assets/en/42.webp)

Untuk lebih memahami bagaimana biaya bekerja, mari kita pelajari jaringan Lightning yang sama seperti sebelumnya, tetapi sekarang dengan biaya perutean berikut:

- Saluran **Alice - Suzie**: biaya dasar 1 satoshi dan 1 ppm untuk Alice.
- Saluran **Suzie - Carol**: biaya dasar 0 satoshi dan 200 ppm untuk Suzie.
- Saluran **Carol - Bob**: biaya dasar 1 satoshi dan 1 ppm untuk Suzie 2.
  ![LNP201](assets/en/43.webp)

Untuk pembayaran yang sama sebesar **40,000 satoshi** ke Bob, Alice harus mengirim sedikit lebih banyak, karena setiap node perantara akan mengurangi biayanya:

- **Carol** mengurangi 1.04 satoshi di saluran dengan Bob:
  $$ f*{\text{Carol-Bob}} = \text{biaya dasar} + \left(\frac{\text{ppm} \times \text{jumlah}}{10^6}\right) $$
  $$ f*{\text{Carol-Bob}} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0.04 = 1.04 \text{ sats} $$

- **Suzie** mengurangi 8 satoshi dalam biaya di saluran dengan Carol:
  $$ f*{\text{Suzie-Carol}} = \text{biaya dasar} + \left(\frac{\text{ppm} \times \text{jumlah}}{10^6}\right) $$
  $$ f*{\text{Suzie-Carol}} = 0 + \frac{200 \times 40001.04}{10^6} = 0 + 8.0002 \approx 8 \text{ sats} $$

Total biaya untuk pembayaran ini di jalur ini adalah **9.04 satoshi**. Dengan demikian, Alice harus mengirim **40,009.04 satoshi** agar Bob menerima tepat **40,000 satoshi**.

![LNP201](assets/en/44.webp)

Likuiditas oleh karena itu diperbarui:

![LNP201](assets/en/45.webp)

### Onion Routing

Untuk merutekan pembayaran dari pengirim ke penerima, Jaringan Lightning menggunakan metode yang disebut "**onion routing**". Tidak seperti perutean data klasik, di mana setiap router menentukan arah data berdasarkan tujuan mereka, onion routing bekerja secara berbeda:

- **Node pengirim menghitung seluruh rute**: Alice, misalnya, menentukan bahwa pembayarannya harus melewati Suzie dan Carol sebelum mencapai Bob.
- **Setiap node perantara hanya mengetahui tetangga terdekatnya**: Suzie hanya tahu bahwa dia menerima dana dari Alice dan dia harus mentransfernya ke Carol. Namun, Suzie tidak tahu apakah Alice adalah node sumber atau node perantara, dan dia juga tidak tahu apakah Carol adalah node penerima atau hanya node perantara lainnya. Prinsip ini juga berlaku untuk Carol dan semua node lain di jalur tersebut. Routing bawang merah (onion routing) dengan demikian menjaga kerahasiaan transaksi dengan menyembunyikan identitas pengirim dan penerima akhir. Untuk memastikan node pengirim dapat menghitung rute lengkap ke penerima dalam onion routing, node tersebut harus memelihara **grafik jaringan** untuk mengetahui topologinya dan menentukan rute yang mungkin.
  **Apa yang harus Anda ambil dari bab ini?**

1. Di Lightning, pembayaran dapat dialihkan antar node yang tidak terhubung langsung melalui saluran perantara. Setiap node perantara ini memfasilitasi relay likuiditas.
2. Node perantara menerima komisi untuk layanannya, yang terdiri dari biaya tetap dan variabel.
3. Onion routing memungkinkan node pengirim untuk menghitung rute lengkap tanpa node perantara mengetahui sumber atau tujuan akhir.

Dalam bab ini, kita telah menjelajahi routing pembayaran di Jaringan Lightning. Namun, pertanyaan muncul: apa yang mencegah node perantara menerima pembayaran masuk tanpa meneruskannya ke tujuan berikutnya, dengan tujuan untuk mencegat transaksi? Inilah peran HTLC yang akan kita pelajari di bab berikutnya.

## HTLC – Hashed Time Locked Contract

<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>

![HTLC](https://youtu.be/-JC4mkq7H48)

Dalam bab ini, kita akan menemukan bagaimana Lightning memungkinkan pembayaran untuk transit melalui node perantara tanpa perlu mempercayai mereka, berkat **HTLC** (_Hashed Time-Locked Contracts_). Kontrak pintar ini memastikan bahwa setiap node perantara hanya akan menerima dana dari salurannya jika ia meneruskan pembayaran ke penerima akhir, jika tidak, pembayaran tidak akan divalidasi.

Masalah yang muncul untuk routing pembayaran adalah kepercayaan yang diperlukan pada node perantara, dan di antara node perantara itu sendiri. Untuk mengilustrasikan ini, mari kita kembali ke contoh jaringan Lightning yang disederhanakan dengan 3 node dan 2 saluran:

- Alice memiliki saluran dengan Suzie.
- Suzie memiliki saluran dengan Bob.

Alice ingin mengirim 40.000 sats ke Bob tetapi dia tidak memiliki saluran langsung dengannya dan tidak ingin membuka satu. Dia mencari rute dan memutuskan untuk melalui node Suzie.

![LNP201](assets/en/46.webp)

Jika Alice secara naif mengirim 40.000 satoshi ke Suzie dengan harapan Suzie akan mentransfer jumlah tersebut ke Bob, Suzie bisa menyimpan dana tersebut untuk dirinya sendiri dan tidak mentransmisikan apa pun ke Bob.

![LNP201](assets/en/47.webp)
Untuk menghindari situasi ini, di Lightning, kita menggunakan HTLCs (Hashed Time-Locked Contracts), yang membuat pembayaran ke node perantara bersyarat, artinya Suzie harus memenuhi kondisi tertentu untuk mengakses dana Alice dan mentransfernya ke Bob.

### Bagaimana HTLC Bekerja

HTLC adalah kontrak khusus yang didasarkan pada dua prinsip:

- **Kondisi akses**: Penerima harus mengungkapkan rahasia untuk membuka pembayaran yang jatuh tempo kepada mereka.
- **Kedaluwarsa**: Jika pembayaran tidak sepenuhnya selesai dalam periode yang ditentukan, pembayaran dibatalkan, dan dana kembali ke pengirim.

Berikut cara kerja proses ini dalam contoh kita dengan Alice, Suzie, dan Bob:

![LNP201](assets/en/48.webp)
**Membuat Rahasia**: Bob menghasilkan sebuah rahasia acak yang dinotasikan sebagai _s_ (preimage), dan menghitung hash-nya yang dinotasikan sebagai _r_ dengan fungsi hash yang dinotasikan sebagai _h_. Kita memiliki:
$$
r = h(s)
$$

Menggunakan fungsi hash membuatnya tidak mungkin untuk menemukan _s_ hanya dengan _h(s)_, tetapi jika _s_ disediakan, mudah untuk memverifikasi bahwa itu sesuai dengan _h(s)_.

![LNP201](assets/en/49.webp)

**Mengirim Permintaan Pembayaran**: Bob mengirimkan sebuah **invoice** kepada Alice meminta pembayaran. Invoice ini secara khusus mencakup hash _r_.

![LNP201](assets/en/50.webp)

**Mengirim Pembayaran Bersyarat**: Alice mengirimkan HTLC sebesar 40.000 satoshi kepada Suzie. Syarat agar Suzie menerima dana ini adalah dia harus memberikan Alice sebuah rahasia _s'_ yang memenuhi persamaan berikut:

$$
h(s') = r
$$

![LNP201](assets/en/51.webp)

**Mentransfer HTLC ke Penerima Akhir**: Suzie, untuk mendapatkan 40.000 satoshi dari Alice, harus mentransfer HTLC serupa sebesar 40.000 satoshi kepada Bob, yang memiliki syarat yang sama, yaitu dia harus memberikan Suzie sebuah rahasia _s'_ yang memenuhi persamaan:

$$
h(s') = r
$$

![LNP201](assets/en/52.webp)

**Validasi oleh Rahasia _s_**: Bob memberikan _s_ kepada Suzie untuk menerima 40.000 satoshi yang dijanjikan dalam HTLC. Dengan rahasia ini, Suzie kemudian dapat membuka HTLC Alice dan mendapatkan 40.000 satoshi dari Alice. Pembayaran kemudian dengan benar dialihkan ke Bob.

![LNP201](assets/en/53.webp)
Proses ini mencegah Suzie menyimpan dana Alice tanpa menyelesaikan transfer ke Bob, karena dia harus mengirim pembayaran ke Bob untuk mendapatkan rahasia _s_ dan dengan demikian membuka HTLC Alice. Operasi tetap sama bahkan jika rute mencakup beberapa node perantara: ini hanya masalah mengulangi langkah-langkah Suzie untuk setiap node perantara. Setiap node dilindungi oleh kondisi HTLC, karena membuka HTLC terakhir oleh penerima secara otomatis memicu pembukaan semua HTLC lainnya secara beruntun.

### Kedaluwarsa dan Pengelolaan HTLC dalam Kasus Masalah

Jika selama proses pembayaran, salah satu node perantara, atau node penerima, berhenti merespon, terutama dalam kasus gangguan internet atau listrik, maka pembayaran tidak dapat diselesaikan, karena rahasia yang diperlukan untuk membuka HTLC tidak ditransmisikan. Mengambil contoh kita dengan Alice, Suzie, dan Bob, masalah ini terjadi, misalnya, jika Bob tidak mentransmisikan rahasia _s_ kepada Suzie. Dalam kasus ini, semua HTLC di jalur hulu diblokir, dan dana yang mereka amankan juga demikian.

![LNP201](assets/en/54.webp)

Untuk menghindari ini, HTLC di Lightning memiliki waktu kedaluwarsa yang memungkinkan penghapusan HTLC jika tidak diselesaikan setelah waktu tertentu. Kedaluwarsa mengikuti urutan tertentu karena dimulai terlebih dahulu dengan HTLC yang paling dekat dengan penerima, dan kemudian secara bertahap bergerak ke atas ke pengirim transaksi. Dalam contoh kita, jika Bob tidak pernah memberikan rahasia _s_ kepada Suzie, ini akan pertama-tama menyebabkan HTLC Suzie ke Bob kedaluwarsa.

![LNP201](assets/en/55.webp)

Kemudian HTLC dari Alice ke Suzie.
![LNP201](assets/en/56.webp)
Jika urutan kedaluwarsa dibalik, Alice bisa memulihkan pembayarannya sebelum Suzie bisa melindungi dirinya dari potensi kecurangan. Memang, jika Bob kembali untuk mengklaim HTLC-nya sementara Alice telah menghapus miliknya, Suzie akan berada dalam posisi yang tidak menguntungkan. Urutan kedaluwarsa HTLC yang berurutan ini memastikan bahwa tidak ada node perantara yang menderita kerugian yang tidak adil.

### Representasi HTLC dalam transaksi komitmen

Transaksi komitmen merepresentasikan HTLC sedemikian rupa sehingga kondisi yang mereka terapkan pada Lightning dapat ditransfer ke Bitcoin dalam kejadian penutupan saluran paksa selama masa hidup HTLC. Sebagai pengingat, transaksi komitmen merepresentasikan keadaan saat ini dari saluran antara dua pengguna dan memungkinkan penutupan paksa sepihak dalam kasus masalah. Dengan setiap keadaan baru dari saluran, 2 transaksi komitmen dibuat: satu untuk setiap pihak. Mari kita kembali ke contoh kita dengan Alice, Suzie, dan Bob, tetapi lihat lebih dekat apa yang terjadi di tingkat saluran antara Alice dan Suzie ketika HTLC dibuat.
![LNP201](assets/en/57.webp)

Sebelum dimulainya pembayaran 40.000 sats antara Alice dan Bob, Alice memiliki 100.000 sats di salurannya dengan Suzie, sementara Suzie memiliki 30.000. Transaksi komitmen mereka adalah sebagai berikut:

![LNP201](assets/en/58.webp)

Alice baru saja menerima faktur Bob, yang secara khusus berisi _r_, hash dari rahasia. Dia dapat dengan demikian membangun HTLC sebesar 40.000 satoshi dengan Suzie. HTLC ini direpresentasikan dalam transaksi komitmen terbaru sebagai output yang disebut "**_HTLC Out_**" di sisi Alice, karena dana keluar, dan "**_HTLC In_**" di sisi Suzie, karena dana masuk.

![LNP201](assets/en/59.webp)

Output yang terkait dengan HTLC ini memiliki kondisi yang sama persis, yaitu:

- Jika Suzie mampu menyediakan rahasia _s_, dia dapat membuka output ini segera dan mentransfernya ke alamat yang dia kontrol.
- Jika Suzie tidak memiliki rahasia _s_, dia tidak dapat membuka output ini, dan Alice akan dapat membukanya setelah timelock untuk mengirimkannya ke alamat yang dia kontrol. Timelock dengan demikian memberikan Suzie periode untuk bereaksi jika dia memperoleh _s_.

Kondisi ini hanya berlaku jika saluran ditutup (yaitu, transaksi komitmen dipublikasikan on-chain) sementara HTLC masih aktif di Lightning, yang berarti pembayaran antara Alice dan Bob belum diselesaikan, dan HTLC belum kedaluwarsa. Berkat kondisi ini, Suzie dapat memulihkan 40.000 satoshi HTLC yang berhutang kepadanya dengan menyediakan _s_. Jika tidak, Alice memulihkan dana setelah kedaluwarsa timelock, karena jika Suzie tidak tahu _s_, itu berarti dia tidak telah mentransfer 40.000 satoshi ke Bob, dan oleh karena itu, dana Alice tidak berhutang kepadanya.

Selanjutnya, jika saluran ditutup sementara beberapa HTLC tertunda, akan ada sebanyak output tambahan sebanyak HTLC yang sedang berlangsung.
Jika saluran tidak ditutup, maka setelah kedaluwarsa atau keberhasilan pembayaran Lightning, transaksi komitmen baru dibuat untuk mencerminkan keadaan baru, sekarang stabil, dari saluran, yaitu, tanpa HTLC yang tertunda. Output yang terkait dengan HTLC dapat dengan demikian dihapus dari transaksi komitmen.
![LNP201](assets/en/60.webp)
Akhirnya, dalam kasus penutupan saluran kerjasama sementara HTLC aktif, Alice dan Suzie berhenti menerima pembayaran baru dan menunggu resolusi atau kedaluwarsa dari HTLC yang sedang berlangsung. Ini memungkinkan mereka untuk menerbitkan transaksi penutupan yang lebih ringan, tanpa output yang terkait dengan HTLC, sehingga mengurangi biaya dan menghindari menunggu kemungkinan timelock.
**Apa yang harus Anda ambil dari bab ini?**

HTLC memungkinkan perutean pembayaran Lightning melalui beberapa node tanpa harus mempercayai mereka. Berikut adalah poin-poin kunci untuk diingat:

1. HTLC memastikan keamanan pembayaran melalui rahasia (preimage) dan waktu kedaluwarsa.
2. Resolusi atau kedaluwarsa dari HTLC mengikuti urutan tertentu: kemudian dari tujuan menuju sumber, untuk melindungi setiap node.
3. Selama HTLC tidak diselesaikan atau kedaluwarsa, itu dipertahankan sebagai output dalam transaksi komitmen terbaru.

Di bab selanjutnya, kita akan menemukan bagaimana sebuah node yang mengeluarkan transaksi Lightning menemukan dan memilih rute untuk pembayarannya mencapai node penerima.

## Menemukan Jalan Anda

<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>

![menemukan jalan Anda](https://youtu.be/wnUGJjOxd9Q)

Dalam bab-bab sebelumnya, kita melihat bagaimana menggunakan saluran node lain untuk merutekan pembayaran dan mencapai node tanpa harus terhubung langsung dengannya melalui saluran. Kita juga membahas bagaimana memastikan keamanan transfer tanpa mempercayai node perantara. Dalam bab ini, kita akan fokus pada menemukan rute terbaik untuk mencapai node target.

### Masalah Perutean di Lightning

Seperti yang telah kita lihat, dalam Lightning, node pengirim pembayaran yang harus menghitung rute lengkap ke penerima, karena kita menggunakan sistem perutean onion. Node perantara tidak mengetahui baik titik asal maupun tujuan akhir. Mereka hanya tahu dari mana pembayaran datang dan ke node mana mereka harus mentransfernya selanjutnya. Ini berarti bahwa node pengirim harus memelihara topologi lokal dinamis dari jaringan, dengan node Lightning yang ada dan saluran di antara masing-masing, dengan mempertimbangkan pembukaan, penutupan, dan pembaruan status.

![LNP201](assets/en/61.webp)
Bahkan dengan topologi Jaringan Lightning ini, ada informasi penting untuk perutean yang tetap tidak dapat diakses oleh node pengirim, yaitu distribusi likuiditas yang tepat di saluran pada setiap saat tertentu. Memang, setiap saluran hanya menampilkan **kapasitas total**nya, tetapi distribusi dana internal hanya diketahui oleh dua node yang berpartisipasi. Ini menimbulkan tantangan untuk perutean yang efisien, karena keberhasilan pembayaran tergantung terutama pada apakah jumlahnya kurang dari likuiditas terendah di rute yang dipilih. Namun, likuiditas tidak semua terlihat oleh node pengirim.
![LNP201](assets/en/62.webp)

### Pembaruan Peta Jaringan

Untuk menjaga peta jaringan mereka tetap terkini, node secara teratur bertukar pesan melalui algoritma yang disebut "**_gossip_**". Ini adalah algoritma terdistribusi yang digunakan untuk menyebarkan informasi secara epidemi ke semua node dalam jaringan, yang memungkinkan pertukaran dan sinkronisasi dari keadaan global saluran dalam beberapa siklus komunikasi. Setiap node menyebarkan informasi ke satu atau lebih tetangga yang dipilih secara acak atau tidak, mereka, pada gilirannya, menyebarkan informasi ke tetangga lain dan seterusnya sampai keadaan yang disinkronkan secara global tercapai.

2 pesan utama yang ditukar antara node Lightning adalah sebagai berikut:

- "**Pengumuman Saluran**": pesan yang menandakan pembukaan saluran baru.
- "**Pembaruan Saluran**": pesan pembaruan tentang status sebuah saluran, khususnya tentang evolusi biaya (tetapi tidak tentang distribusi likuiditas).
Node Lightning juga memantau blockchain Bitcoin untuk mendeteksi transaksi penutupan saluran. Saluran yang ditutup kemudian dihapus dari peta karena tidak lagi dapat digunakan untuk merutekan pembayaran kita.

### Merutekan Pembayaran

Mari kita ambil contoh sebuah jaringan Lightning kecil dengan 7 node: Alice, Bob, 1, 2, 3, 4, dan 5. Bayangkan Alice ingin mengirim pembayaran ke Bob tetapi harus melalui node perantara.

![LNP201](assets/en/63.webp)

Berikut adalah distribusi dana aktual di saluran-saluran ini:

- **Saluran antara Alice dan 1**: 250.000 sats di sisi Alice, 80.000 di sisi 1 (kapasitas total 330.000 sats).
- **Saluran antara 1 dan 2**: 300.000 sats di sisi 1, 200.000 di sisi 2 (kapasitas total 500.000 sats).
- **Saluran antara 2 dan 3**: 50.000 sats di sisi 2, 60.000 di sisi 3 (kapasitas total 110.000 sats).
- **Saluran antara 2 dan 5**: 90.000 sats di sisi 2, 160.000 di sisi 5 (kapasitas total 250.000 sats).
- **Saluran antara 2 dan 4**: 180.000 sats di sisi 2, 110.000 di sisi 4 (kapasitas total 290.000 sats).
- **Saluran antara 4 dan 5**: 200.000 sats di sisi 4, 10.000 di sisi 5 (kapasitas total 210.000 sats).
- **Saluran antara 3 dan Bob**: 50.000 sats di sisi 3, 250.000 di sisi Bob (kapasitas total 300.000 sats).
- **Saluran antara 5 dan Bob**: 260.000 sats di sisi 5, 100.000 di sisi Bob (kapasitas total 360.000 sats).

![LNP201](assets/en/64.webp)

Untuk melakukan pembayaran 100.000 sats dari Alice ke Bob, opsi rute terbatas oleh likuiditas yang tersedia di setiap saluran. Rute optimal untuk Alice, berdasarkan distribusi likuiditas yang diketahui, bisa jadi urutan `Alice → 1 → 2 → 4 → 5 → Bob`:

![LNP201](assets/en/65.webp)

Namun, karena Alice tidak mengetahui distribusi dana yang tepat di setiap saluran, dia harus memperkirakan rute optimal secara probabilistik, dengan mempertimbangkan kriteria berikut:

- **Probabilitas keberhasilan**: sebuah saluran dengan kapasitas total yang lebih tinggi kemungkinan besar mengandung likuiditas yang cukup. Misalnya, saluran antara node 2 dan node 3 memiliki kapasitas total 110.000 sats, jadi kemungkinan kecil untuk menemukan 100.000 sats atau lebih di sisi node 2, meskipun tetap mungkin.
- **Biaya transaksi**: dalam memilih rute terbaik, node pengirim juga mempertimbangkan biaya yang diterapkan oleh setiap node perantara dan berusaha meminimalkan total biaya rute.
- **Kadaluwarsa HTLCs**: untuk menghindari pembayaran yang terblokir, waktu kadaluwarsa HTLCs juga merupakan parameter yang harus dipertimbangkan.
- **Jumlah node perantara**: akhirnya, secara lebih luas, node pengirim akan berusaha menemukan rute dengan jumlah node serendah mungkin untuk mengurangi risiko kegagalan dan membatasi biaya transaksi Lightning.
Dengan menganalisis kriteria ini, node pengirim dapat menguji rute yang paling mungkin dan mencoba mengoptimalkannya. Dalam contoh kita, Alice dapat merangking rute terbaik sebagai berikut:

1. `Alice → 1 → 2 → 5 → Bob`, karena ini adalah rute terpendek dengan kapasitas tertinggi.
2. `Alice → 1 → 2 → 4 → 5 → Bob`, karena rute ini menawarkan kapasitas yang baik, meskipun lebih panjang dari yang pertama.
3. `Alice → 1 → 2 → 3 → Bob`, karena rute ini termasuk saluran `2 → 3`, yang memiliki kapasitas sangat terbatas, tetapi tetap berpotensi dapat digunakan.

### Eksekusi Pembayaran

Alice memutuskan untuk menguji rute pertamanya (`Alice → 1 → 2 → 5 → Bob`). Oleh karena itu, dia mengirimkan HTLC sebesar 100.000 sats ke node 1. Node ini memeriksa bahwa ia memiliki likuiditas yang cukup dengan node 2, dan melanjutkan transmisi. Node 2 kemudian menerima HTLC dari node 1, tetapi menyadari bahwa ia tidak memiliki cukup likuiditas di salurannya dengan node 5 untuk merutekan pembayaran sebesar 100.000 sats. Kemudian, ia mengirimkan pesan kesalahan kembali ke node 1, yang meneruskannya ke Alice. Rute ini telah gagal.

![LNP201](assets/en/66.webp)

Alice kemudian mencoba merutekan pembayarannya menggunakan rute keduanya (`Alice → 1 → 2 → 4 → 5 → Bob`). Dia mengirimkan HTLC sebesar 100.000 sats ke node 1, yang meneruskannya ke node 2, lalu ke node 4, ke node 5, dan akhirnya ke Bob. Kali ini, likuiditasnya cukup, dan rute berfungsi. Setiap node membuka kunci HTLC-nya secara bertahap menggunakan preimage yang disediakan oleh Bob (rahasia _s_), yang memungkinkan pembayaran Alice ke Bob berhasil diselesaikan.

![LNP201](assets/en/67.webp)

Pencarian rute dilakukan sebagai berikut: node pengirim mulai dengan mengidentifikasi rute terbaik yang mungkin, kemudian mencoba pembayaran secara bertahap sampai rute yang berfungsi ditemukan.

Penting untuk dicatat bahwa Bob dapat memberikan informasi kepada Alice dalam **invoice** untuk memfasilitasi perutean. Misalnya, dia dapat menunjukkan saluran terdekat dengan likuiditas yang cukup atau mengungkapkan keberadaan saluran privat. Indikasi ini memungkinkan Alice menghindari rute dengan peluang keberhasilan yang kecil dan terlebih dahulu mencoba jalur yang direkomendasikan oleh Bob.

**Apa yang harus Anda ambil dari bab ini?**

1. Node mempertahankan peta topologi jaringan melalui pengumuman dan dengan memantau penutupan saluran di blockchain Bitcoin.
2. Pencarian rute optimal untuk pembayaran tetap probabilistik dan bergantung pada banyak kriteria.
3. Bob dapat memberikan indikasi dalam **invoice** untuk memandu perutean Alice dan menyelamatkannya dari menguji rute yang tidak mungkin.

Dalam bab berikutnya, kita akan secara khusus mempelajari fungsi invoice, selain beberapa alat lain yang digunakan di Jaringan Lightning.

# Alat-alat Jaringan Lightning

<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>

## Invoice, LNURL, dan Keysend

<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>
![invoice, LNURL, Keysend](https://youtu.be/CHnXJuZTarU)
Dalam bab ini, kita akan melihat lebih dekat operasi **invoice** Lightning, yaitu permintaan pembayaran yang dikirim oleh node penerima ke node pengirim. Tujuannya adalah untuk memahami cara membayar dan menerima pembayaran di Lightning. Kita juga akan membahas 2 alternatif untuk invoice klasik: LNURL dan Keysend.
![LNP201](assets/en/68.webp)

### Struktur Invoice Lightning

Seperti yang dijelaskan dalam bab tentang HTLCs, setiap pembayaran dimulai dengan pembuatan **invoice** oleh penerima. Invoice ini kemudian ditransmisikan ke pembayar (melalui kode QR atau dengan menyalin dan menempel) untuk memulai pembayaran. Invoice terdiri dari dua bagian utama:

1. **Bagian yang Dapat Dibaca Manusia**: bagian ini berisi metadata yang jelas terlihat untuk meningkatkan pengalaman pengguna.
2. **Payload**: bagian ini mencakup informasi yang dimaksudkan untuk mesin dalam memproses pembayaran.

Struktur tipikal dari sebuah invoice dimulai dengan pengenal `ln` untuk "Lightning", diikuti oleh `bc` untuk Bitcoin, kemudian jumlah invoice. Sebuah pemisah `1` membedakan bagian yang dapat dibaca manusia dari bagian data (payload).

Mari kita ambil invoice berikut sebagai contoh:

```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Kita sudah bisa membaginya menjadi 2 bagian. Pertama, ada Bagian yang Dapat Dibaca Manusia:

```invoice
lnbc100u
```

Kemudian bagian yang dimaksudkan untuk payload:

```invoice

p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```
Dua bagian tersebut dipisahkan oleh `1`. Pemisah ini dipilih alih-alih karakter khusus untuk memudahkan menyalin seluruh faktur dengan mengklik ganda.

Pada bagian pertama, kita dapat melihat bahwa:

- `ln` menunjukkan bahwa ini adalah transaksi Lightning.
- `bc` menunjukkan bahwa jaringan Lightning berada di blockchain Bitcoin (dan bukan di testnet atau di Litecoin).
- `100u` menunjukkan jumlah faktur, dinyatakan dalam **mikrosatoshis** (`u` berarti "mikro"), yang di sini sama dengan 10.000 sats.

Untuk menunjukkan jumlah pembayaran, ini dinyatakan dalam sub-unit bitcoin. Berikut adalah unit yang digunakan:

- **Millibitcoin (ditandai `m`):** Mewakili satu-ribu dari satu bitcoin.

  $$
  1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satoshis}
  $$

- **Microbitcoin (ditandai `u`):** Juga terkadang disebut "bit", mewakili satu-juta dari satu bitcoin.

  $$
  1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satoshis}
  $$

- **Nanobitcoin (ditandai `n`):** Mewakili satu-miliar dari satu bitcoin.

  $$
  1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satoshis}
  $$

- **Picobitcoin (ditandai `p`):** Mewakili satu-triliun dari satu bitcoin.
  $$
  1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satoshis}
  $$

### Muatan Faktur

Muatan faktur mencakup beberapa informasi yang diperlukan untuk memproses pembayaran:

- **Timestamp:** Momen pembuatan faktur, dinyatakan dalam Unix Timestamp (jumlah detik yang telah berlalu sejak 1 Januari 1970).
- **Meng-hash Rahasia**: Seperti yang kita lihat dalam bagian tentang HTLCs, node penerima harus memberikan node pengirim hash dari preimage. Ini digunakan dalam HTLCs untuk mengamankan transaksi. Kami menyebutnya sebagai "_r_".
- **Rahasia Pembayaran**: Rahasia lain dihasilkan oleh penerima, tetapi kali ini ditransmisikan ke node pengirim. Ini digunakan dalam onion routing untuk mencegah node-node perantara menebak apakah node berikutnya adalah penerima akhir atau tidak. Ini dengan demikian menjaga bentuk kerahasiaan bagi penerima terhadap node perantara terakhir di rute.
- **Kunci Publik Penerima**: Menunjukkan kepada pembayar identifier orang yang akan dibayar.
- **Durasi Kedaluwarsa**: Waktu maksimum untuk faktur dibayar (secara default 1 jam).
- **Petunjuk Rute**: Informasi tambahan yang diberikan oleh penerima untuk membantu pengirim mengoptimalkan rute pembayaran.
- **Tanda Tangan**: Menjamin integritas faktur dengan mengautentikasi semua informasi.

Faktur kemudian dikodekan dalam **bech32**, format yang sama seperti untuk alamat Bitcoin SegWit (format dimulai dengan `bc1`).

### Penarikan LNURL
Dalam transaksi tradisional, seperti pembelian di toko, faktur dihasilkan untuk jumlah total yang harus dibayar. Setelah faktur disajikan (dalam bentuk kode QR atau rangkaian karakter), pelanggan dapat memindainya dan menyelesaikan transaksi. Pembayaran kemudian mengikuti proses tradisional yang telah kita pelajari di bagian sebelumnya. Namun, proses ini terkadang bisa sangat merepotkan untuk pengalaman pengguna, karena memerlukan penerima untuk mengirim informasi ke pengirim melalui faktur.
Untuk situasi tertentu, seperti menarik bitcoin dari layanan online, proses tradisional terlalu merepotkan. Dalam kasus seperti itu, solusi penarikan **LNURL** menyederhanakan proses ini dengan menampilkan kode QR yang dipindai oleh dompet penerima untuk secara otomatis membuat faktur. Layanan kemudian membayar faktur, dan pengguna hanya melihat penarikan instan.

![LNP201](assets/en/69.webp)

LNURL adalah protokol komunikasi yang menentukan serangkaian fungsi yang dirancang untuk menyederhanakan interaksi antara node Lightning dan klien, serta aplikasi pihak ketiga. Penarikan LNURL, seperti yang baru saja kita lihat, hanyalah salah satu contoh di antara fungsi lainnya.
Protokol ini berbasis HTTP dan memungkinkan pembuatan tautan untuk berbagai operasi, seperti permintaan pembayaran, permintaan penarikan, atau fungsi lain yang meningkatkan pengalaman pengguna. Setiap LNURL adalah URL yang dikodekan bech32 dengan awalan lnurl, yang, setelah dipindai, memicu serangkaian tindakan otomatis pada dompet Lightning.
Misalnya, fitur LNURL-withdraw (LUD-03) memungkinkan penarikan dana dari layanan dengan memindai kode QR, tanpa perlu menghasilkan faktur secara manual. Demikian pula, LNURL-auth (LUD-04) memungkinkan masuk ke layanan online menggunakan kunci pribadi di dompet Lightning seseorang alih-alih kata sandi.

### Mengirim Pembayaran Lightning Tanpa Faktur: Keysend

Kasus menarik lainnya adalah transfer dana tanpa menerima faktur terlebih dahulu, yang dikenal sebagai "**Keysend**". Protokol ini memungkinkan pengiriman dana dengan menambahkan preimage dalam data pembayaran terenkripsi, yang hanya dapat diakses oleh penerima. Preimage ini memungkinkan penerima untuk membuka HTLC, sehingga mengambil dana tanpa harus menghasilkan faktur terlebih dahulu.

Untuk menyederhanakan, dalam protokol ini, pengirim yang menghasilkan rahasia yang digunakan dalam HTLC, bukan penerima. Secara praktis, ini memungkinkan pengirim untuk melakukan pembayaran tanpa harus berinteraksi dengan penerima terlebih dahulu.

![LNP201](assets/en/70.webp)

**Apa yang harus Anda ambil dari bab ini?**

1. **Lightning Invoice** adalah permintaan pembayaran yang terdiri dari bagian yang dapat dibaca manusia dan bagian data mesin.
2. Faktur dikodekan dalam **bech32**, dengan pemisah `1` untuk memudahkan penyalinan dan bagian data yang berisi semua informasi yang diperlukan untuk memproses pembayaran.
3. Proses pembayaran lainnya ada di Lightning, terutama **LNURL-Withdraw** untuk memudahkan penarikan, dan **Keysend** untuk transfer langsung tanpa faktur.

Di bab berikutnya, kita akan melihat bagaimana operator node dapat mengelola likuiditas di saluran mereka, agar tidak pernah terblokir dan selalu dapat mengirim dan menerima pembayaran di Jaringan Lightning.

## Mengelola Likuiditas Anda

<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>

![mengelola likuiditas anda](https://youtu.be/YuPrbhEJXbg)

Dalam bab ini, kita akan menjelajahi strategi untuk mengelola likuiditas secara efektif di Jaringan Lightning. Pengelolaan likuiditas bervariasi tergantung pada jenis pengguna dan konteks. Kita akan melihat prinsip utama dan teknik yang ada untuk lebih memahami cara mengoptimalkan pengelolaan ini.

### Kebutuhan Likuiditas
Ada tiga profil pengguna utama di Lightning, masing-masing dengan kebutuhan likuiditas spesifik:
1. **Pembayar**: Ini adalah orang yang melakukan pembayaran. Mereka membutuhkan likuiditas keluar untuk dapat mentransfer dana ke pengguna lain. Sebagai contoh, ini bisa jadi seorang konsumen.
2. **Penjual (atau Penerima Pembayaran)**: Ini adalah orang yang menerima pembayaran. Mereka membutuhkan likuiditas masuk untuk dapat menerima pembayaran ke node mereka. Sebagai contoh, ini bisa jadi sebuah bisnis atau toko online.
3. **Router**: Sebuah node perantara, sering kali spesialisasi dalam merutekan pembayaran, yang harus mengoptimalkan likuiditasnya di setiap saluran untuk merutekan sebanyak mungkin pembayaran dan mendapatkan biaya.

Profil-profil ini jelas tidak tetap; seorang pengguna dapat beralih antara pembayar dan penerima pembayaran tergantung pada transaksi. Sebagai contoh, Bob bisa menerima gajinya di Lightning dari majikannya, menempatkannya dalam posisi "penjual" yang memerlukan likuiditas masuk. Selanjutnya, jika dia ingin menggunakan gajinya untuk membeli makanan, dia menjadi "pembayar" dan harus memiliki likuiditas keluar.

Untuk lebih memahami, mari kita ambil contoh jaringan sederhana yang terdiri dari tiga node: pembeli (Alice), router (Suzie), dan penjual (Bob).

![LNP201](assets/en/71.webp)

Bayangkan bahwa pembeli ingin mengirim 30.000 satoshi ke penjual dan pembayaran tersebut melewati node router. Setiap pihak kemudian harus memiliki jumlah likuiditas minimum dalam arah pembayaran:

- Pembayar harus memiliki setidaknya 30.000 satoshi di sisi mereka dari saluran dengan router.
- Penjual harus memiliki saluran di mana 30.000 satoshi berada di sisi berlawanan untuk dapat menerimanya.
- Router harus memiliki 30.000 satoshi di sisi pembayar dalam saluran mereka, dan juga 30.000 satoshi di sisi mereka dalam saluran dengan penjual, untuk dapat merutekan pembayaran.

![LNP201](assets/en/72.webp)

### Strategi Manajemen Likuiditas

Pembayar harus memastikan untuk memelihara likuiditas yang cukup di sisi saluran mereka untuk menjamin likuiditas keluar. Ini terbukti relatif sederhana, karena cukup dengan membuka saluran Lightning baru untuk memiliki likuiditas ini. Memang, dana awal yang terkunci dalam multisig on-chain sepenuhnya berada di sisi pembayar dalam saluran Lightning pada awalnya. Kapasitas pembayaran dengan demikian dijamin selama saluran dibuka dengan dana yang cukup. Ketika likuiditas keluar habis, cukup dengan membuka saluran baru.
Di sisi lain, untuk penjual, tugasnya lebih kompleks. Untuk dapat menerima pembayaran, mereka harus memiliki likuiditas di sisi berlawanan dari saluran mereka. Oleh karena itu, membuka saluran saja tidak cukup: mereka juga harus melakukan pembayaran dalam saluran ini untuk memindahkan likuiditas ke sisi lain sebelum mereka dapat menerima pembayaran sendiri. Untuk beberapa profil pengguna Lightning, seperti pedagang, ada ketidakseimbangan yang jelas antara apa yang dikirim node mereka dan apa yang diterima, karena tujuan bisnis terutama adalah untuk mengumpulkan lebih banyak daripada yang dibelanjakan, untuk menghasilkan keuntungan. Untungnya, bagi pengguna ini dengan kebutuhan likuiditas masuk spesifik, beberapa solusi ada:

- **Menarik saluran**: Pedagang mendapat keuntungan dari keuntungan karena volume pembayaran masuk yang diharapkan pada node mereka. Dengan mempertimbangkan hal ini, mereka dapat mencoba menarik node router yang mencari pendapatan dari biaya transaksi dan yang mungkin membuka saluran ke arah mereka, berharap untuk merutekan pembayaran mereka dan mengumpulkan biaya terkait.
- **Pergerakan Likuiditas**: Penjual juga dapat membuka sebuah saluran dan mentransfer sebagian dana ke sisi yang berlawanan dengan membuat pembayaran fiktif ke node lain, yang akan mengembalikan uang tersebut dengan cara lain. Kita akan melihat di bagian selanjutnya bagaimana melaksanakan operasi ini.
- **Pembukaan Segitiga**: Platform tersedia bagi node yang ingin membuka saluran secara kolaboratif, memungkinkan masing-masing untuk mendapatkan keuntungan dari likuiditas masuk dan keluar secara langsung. Sebagai contoh, [LightningNetwork+](https://lightningnetwork.plus/) menawarkan layanan ini. Jika Alice, Bob, dan Suzie ingin membuka saluran dengan 100.000 sats, mereka dapat sepakat di platform ini agar Alice membuka saluran ke arah Bob, Bob ke arah Suzie, dan Suzie ke arah Alice. Dengan cara ini, masing-masing memiliki 100.000 sats likuiditas keluar dan 100.000 sats likuiditas masuk, sambil hanya mengunci 100.000 sats.

![LNP201](assets/en/73.webp)

- **Membeli Saluran**: Layanan untuk menyewa saluran Lightning juga ada untuk mendapatkan likuiditas masuk, seperti [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) atau [Lightning Labs Pool](https://lightning.engineering/pool/). Sebagai contoh, Alice dapat membeli saluran satu juta satoshi ke arah nodenya agar dia dapat menerima pembayaran.

![LNP201](assets/en/74.webp)

Akhirnya, bagi router, yang tujuannya adalah untuk memaksimalkan jumlah pembayaran yang diproses dan biaya yang dikumpulkan, mereka harus:

- Membuka saluran yang dibiayai dengan baik dengan node strategis.
- Secara rutin menyesuaikan distribusi dana di saluran sesuai dengan kebutuhan jaringan.

### Layanan Loop Out

Layanan [Loop Out](https://lightning.engineering/loop/), yang ditawarkan oleh Lightning Labs, memungkinkan untuk memindahkan likuiditas ke sisi yang berlawanan dari saluran sambil mengklaim kembali dana tersebut di blockchain Bitcoin. Sebagai contoh, Alice mengirim 1 juta satoshi melalui Lightning ke node loop, yang kemudian mengembalikan dana tersebut kepadanya dalam bitcoin on-chain. Ini menyeimbangkan salurannya dengan 1 juta satoshi di setiap sisi, mengoptimalkan kapasitasnya untuk menerima pembayaran.

![LNP201](assets/en/75.webp)

Oleh karena itu, layanan ini memungkinkan likuiditas masuk sambil mengklaim kembali bitcoin seseorang di on-chain, yang membantu untuk membatasi imobilisasi kas yang diperlukan untuk menerima pembayaran dengan Lightning.

**Apa yang harus Anda ambil dari bab ini?**

- Untuk mengirim pembayaran di Lightning, Anda harus memiliki cukup likuiditas di sisi Anda dalam saluran Anda. Untuk meningkatkan kapasitas pengiriman ini, cukup buka saluran baru.
- Untuk menerima pembayaran, Anda perlu memiliki likuiditas di sisi yang berlawanan dalam saluran Anda. Meningkatkan kapasitas penerimaan ini lebih kompleks, karena memerlukan orang lain untuk membuka saluran ke arah Anda, atau untuk membuat pembayaran (fiktif atau nyata) untuk memindahkan likuiditas ke sisi lain.
- Memelihara likuiditas sesuai keinginan bisa menjadi lebih menantang tergantung pada penggunaan saluran. Itulah mengapa alat dan layanan ada untuk membantu menyeimbangkan saluran sesuai keinginan.

Di bab selanjutnya, saya mengusulkan untuk meninjau konsep-konsep paling penting dari pelatihan ini.

# Lanjutkan Lebih Jauh

<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>

## Kesimpulan Pelatihan

<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>

![kesimpulan](https://youtu.be/MaWpD0rbkVo)
Dalam bab terakhir ini yang menandai akhir dari pelatihan LNP201, saya mengusulkan untuk mengunjungi kembali konsep-konsep penting yang telah kita bahas bersama. Tujuan dari pelatihan ini adalah untuk memberikan Anda pemahaman yang komprehensif dan teknis tentang Lightning Network. Kita telah menemukan bagaimana Lightning Network mengandalkan blockchain Bitcoin untuk melakukan transaksi off-chain, sambil mempertahankan karakteristik fundamental dari Bitcoin, terutama ketiadaan kebutuhan untuk mempercayai node lain.

### Saluran Pembayaran

Dalam bab awal, kita menjelajahi bagaimana dua pihak, dengan membuka saluran pembayaran, dapat melakukan transaksi di luar blockchain Bitcoin. Berikut adalah langkah-langkah yang dibahas:

1. **Pembukaan Saluran**: Pembuatan saluran dilakukan melalui transaksi Bitcoin yang mengunci dana dalam alamat multisignature 2/2. Deposit ini mewakili saluran Lightning di blockchain.

![LNP201](assets/en/76.webp) 2. **Transaksi dalam Saluran**: Di saluran ini, kemudian dimungkinkan untuk melakukan banyak transaksi tanpa harus mempublikasikannya di blockchain. Setiap transaksi Lightning menciptakan keadaan baru dari saluran yang tercermin dalam transaksi komitmen.
![LNP201](assets/en/77.webp)

3. **Pengamanan dan Penutupan**: Peserta berkomitmen pada keadaan baru saluran dengan bertukar kunci pembatalan untuk mengamankan dana dan mencegah kecurangan. Kedua belah pihak dapat menutup saluran secara kooperatif dengan membuat transaksi baru di blockchain Bitcoin, atau sebagai pilihan terakhir melalui penutupan paksa. Opsi terakhir ini, meskipun kurang efisien karena lebih lama dan terkadang dinilai buruk dalam hal biaya, masih memungkinkan untuk pemulihan dana. Dalam kasus kecurangan, korban dapat menghukum penipu dengan memulihkan semua dana dari saluran di blockchain.

![LNP201](assets/en/78.webp)

### Jaringan Saluran

Setelah mempelajari saluran terisolasi, kita memperluas analisis kita ke jaringan saluran:

- **Routing**: Ketika dua pihak tidak langsung terhubung oleh sebuah saluran, jaringan memungkinkan routing melalui node perantara. Pembayaran kemudian transit dari satu node ke node lain.

![LNP201](assets/en/79.webp)

- **HTLCs**: Pembayaran yang transit melalui node perantara diamankan oleh "_Hash Time-Locked Contracts_" (HTLC), yang memungkinkan dana untuk dikunci sampai pembayaran selesai dari ujung ke ujung.

![LNP201](assets/en/80.webp)

- **Onion Routing**: Untuk memastikan kerahasiaan pembayaran, onion routing menyembunyikan tujuan akhir ke node perantara. Node pengirim oleh karena itu harus menghitung seluruh rute, tetapi dalam ketiadaan informasi lengkap tentang likuiditas saluran, ia melanjutkan melalui percobaan berturut-turut untuk merutekan pembayaran.

![LNP201](assets/en/81.webp)

### Manajemen Likuiditas

Kita telah melihat bahwa manajemen likuiditas adalah tantangan di Lightning untuk memastikan aliran pembayaran yang lancar. Mengirim pembayaran relatif sederhana: hanya memerlukan pembukaan saluran. Namun, menerima pembayaran memerlukan likuiditas di sisi berlawanan dari saluran seseorang. Berikut adalah beberapa strategi yang dibahas:

- **Menarik Saluran**: Dengan mendorong node lain untuk membuka saluran ke arah diri sendiri, pengguna memperoleh likuiditas masuk.

- **Memindahkan Likuiditas**: Dengan mengirim pembayaran ke saluran lain, likuiditas berpindah ke sisi berlawanan.

![LNP201](assets/en/82.webp)

- **Menggunakan Layanan seperti Loop dan Pool**: Layanan ini memungkinkan untuk menyeimbangkan kembali atau membeli saluran dengan likuiditas di sisi berlawanan.
  ![LNP201](assets/en/83.webp)
- **Pembukaan Kolaboratif**: Ada juga platform yang tersedia untuk terhubung melakukan pembukaan segitiga dan untuk memiliki likuiditas masuk.

![LNP201](assets/en/84.webp)

### Pengakuan
Saya ingin mengucapkan terima kasih kepada setiap dari Anda atas minat, dukungan, dan pertanyaan sepanjang seri ini. Awalnya, ide saya adalah untuk membuat konten dalam bahasa Prancis mengenai aspek teknis dari Lightning, mengingat kurangnya sumber daya yang tersedia. Ini adalah tantangan pribadi yang ingin saya ambil dengan menggabungkan ketelitian teknis dengan aksesibilitas. Jika Anda menikmati kursus gratis ini, silakan untuk memberi penilaian di bagian "_Rate this course_" dan bagikan dengan orang-orang terkasih serta di jaringan sosial Anda.
Terima kasih, sampai jumpa lagi!

### Bonus: Wawancara dengan Fanis

![Wawancara dengan Fanis](https://youtu.be/VeJ4oJIXo9k)

## Nilai kursus ini

<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>
<isCourseReview>true</isCourseReview>

## Ujian Akhir

<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>
<isCourseExam>true</isCourseExam>

## Kesimpulan

<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>

**Selamat Anda telah menyelesaikan kursus ini!**

Harap dicatat bahwa bab ini saat ini sedang dalam pembangunan dan versi yang lebih baik akan segera tiba. Sementara itu, jika Anda ingin melanjutkan perjalanan Bitcoin Anda, kami mengundang Anda untuk menjelajahi kursus dan tutorial lain yang tersedia di platform kami. Teruskan pekerjaan bagus dan selamat belajar!

```

```