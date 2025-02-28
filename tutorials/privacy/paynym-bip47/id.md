---
name: BIP47 - PayNym

description: Cara Kerja PayNym
---
***PERINGATAN:** Menyusul penangkapan pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, aplikasi tersebut tidak lagi dapat digunakan oleh pengguna yang tidak memiliki Dojo mereka sendiri. BIP47 tetap dapat digunakan di Sparrow Wallet untuk semua pengguna dan **di Samourai Wallet hanya untuk pengguna yang memiliki Dojo**.*

_Kami terus mengikuti perkembangan kasus ini serta perkembangan terkait alat-alat yang terkait. Yakinlah bahwa kami akan memperbarui tutorial ini seiring dengan tersedianya informasi baru._

_Tutorial ini disediakan hanya untuk tujuan pendidikan dan informasi. Kami tidak mendukung atau mendorong penggunaan alat-alat ini untuk tujuan kriminal. Tanggung jawab setiap pengguna adalah untuk mematuhi hukum di yurisdiksi mereka._

---

> "Dia terlalu besar," kata mereka semua, dan ayam kalkun, yang lahir dengan taji dan mengira dirinya seorang kaisar, mengembang seperti kapal dengan semua layar terkembang, dan berjalan langsung kepadanya dengan penuh amarah, matanya merah seperti api. Bebek kecil malang itu tidak tahu harus bertahan atau lari, dan sangat tidak bahagia karena dia dihina oleh semua bebek di halaman.

![BIP47, ilustrasi bebek jelek](assets/1.webp)

Salah satu masalah terbesar pada protokol Bitcoin adalah penggunaan ulang alamat. Transparansi dan distribusi jaringan membuat praktik ini berbahaya bagi privasi pengguna. Untuk menghindari masalah terkait ini, disarankan untuk menggunakan alamat penerima kosong baru untuk setiap pembayaran masuk baru ke dompet, yang bisa sulit dicapai dalam beberapa kasus.

Kompromi ini sudah ada sejak White Paper. Satoshi sudah memperingatkan kita tentang risiko ini dalam karyanya yang diterbitkan pada akhir 2008:

> "Sebagai firewall tambahan, sepasang kunci baru harus digunakan untuk setiap transaksi agar mereka tidak dikaitkan dengan pemilik yang sama."

Ada banyak solusi yang tersedia untuk menerima beberapa pembayaran tanpa penggunaan ulang alamat. Masing-masing dari mereka memiliki kompromi dan kekurangannya. Di antara semua solusi ini, ada [BIP47](https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki), sebuah usulan yang dikembangkan oleh Justus Ranvier dan diterbitkan pada tahun 2015, yang memungkinkan untuk generasi kode pembayaran yang dapat digunakan kembali. Tujuannya adalah untuk memungkinkan beberapa transaksi dilakukan kepada orang yang sama tanpa menggunakan ulang alamat.

Awalnya, usulan ini disambut dengan penghinaan oleh sebagian komunitas, dan tidak pernah ditambahkan ke Bitcoin Core. Namun, beberapa perangkat lunak masih memilih untuk mengimplementasikannya sendiri. Misalnya, Samourai Wallet mengembangkan implementasi mereka sendiri dari BIP47: PayNym. Saat ini, implementasi ini tersedia di Samourai Wallet untuk smartphone, serta di [Sparrow Wallet](https://sparrowwallet.com/) untuk PC.

Seiring waktu, Samourai telah memprogram fitur baru yang langsung terkait dengan PayNym. Sekarang, ada seluruh ekosistem alat yang tersedia untuk mengoptimalkan privasi pengguna berdasarkan PayNym dan BIP47.
Dalam artikel ini, Anda akan menemukan prinsip BIP47 dan PayNym, mekanisme protokol-protokol ini, dan aplikasi praktis yang dihasilkan dari mereka. Saya hanya akan membahas versi pertama dari BIP47, yang saat ini digunakan untuk PayNym, tetapi versi 2, 3, dan 4 bekerja dengan cara yang hampir sama.
Satu-satunya perbedaan utama ditemukan dalam transaksi notifikasi. Versi 1 menggunakan alamat sederhana dengan OP_RETURN untuk notifikasi, versi 2 menggunakan skrip multisig (bloom-multisig) dengan OP_RETURN, dan versi 3 dan 4 hanya menggunakan skrip multisig (cfilter-multisig). Mekanisme yang dibahas dalam artikel ini, termasuk metode kriptografi yang dipelajari, oleh karena itu berlaku untuk keempat versi tersebut. Sampai saat ini, implementasi PayNym di Samourai Wallet dan Sparrow menggunakan versi pertama dari BIP47.

## Ringkasan:

1- Masalah penggunaan ulang alamat.

2- Prinsip-prinsip BIP47 dan PayNym.

3- Tutorial: Menggunakan PayNym.

- Membangun transaksi BIP47 dengan Samourai Wallet.
- Membangun transaksi BIP47 dengan Sparrow Wallet.

4- Cara kerja BIP47.

- Kode pembayaran yang dapat digunakan kembali.
- Metode kriptografi: Pertukaran kunci Diffie-Hellman yang didirikan pada kurva eliptik (ECDH).
- Transaksi notifikasi.
- Membangun transaksi notifikasi.
- Menerima transaksi notifikasi.
- Transaksi pembayaran BIP47.
- Menerima pembayaran BIP47 dan menurunkan kunci privat.
- Mengembalikan pembayaran BIP47.

5- Penggunaan turunan dari PayNym.

6- Opini pribadi saya tentang BIP47.

## Masalah penggunaan ulang alamat.

Alamat penerima digunakan untuk menerima bitcoin. Alamat ini dihasilkan dari kunci publik dengan meng-hash-nya dan menerapkan format tertentu. Dengan demikian, ini memungkinkan untuk menciptakan kondisi pengeluaran baru pada koin untuk mengubah pemiliknya.

> Untuk mempelajari lebih lanjut tentang menghasilkan alamat penerima, saya merekomendasikan membaca bagian terakhir dari artikel ini: Dompet Bitcoin - kutipan dari [ebook Bitcoin Démocratisé 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2#viewer-epio7).

Selain itu, Anda mungkin sudah pernah mendengar dari seorang bitcoiner yang berpengetahuan bahwa alamat penerima adalah untuk penggunaan satu kali, dan bahwa Anda harus menghasilkan yang baru untuk setiap pembayaran masuk baru ke dompet Anda. Oke, tapi mengapa?
Pada dasarnya, penggunaan ulang alamat tidak langsung membahayakan dana Anda. Penggunaan kriptografi pada kurva eliptik memungkinkan Anda untuk membuktikan kepada jaringan bahwa Anda memiliki kunci privat tanpa mengungkapkan kunci tersebut. Oleh karena itu, Anda dapat mengunci UTXO (Unspent Transaction Outputs) yang berbeda pada alamat yang sama dan menghabiskannya pada waktu yang berbeda. Jika Anda tidak mengungkapkan kunci privat yang terkait dengan alamat tersebut, tidak ada yang dapat mengakses dana Anda. Masalah dengan penggunaan ulang alamat lebih terkait dengan privasi.

Seperti disebutkan dalam pengantar, transparansi dan distribusi jaringan Bitcoin berarti bahwa setiap pengguna dengan akses ke node dapat mengamati transaksi dari sistem pembayaran. Akibatnya, mereka dapat melihat saldo berbeda dari alamat. Satoshi Nakamoto kemudian menyebutkan kemungkinan menghasilkan pasangan kunci baru, dan dengan demikian alamat baru, untuk setiap pembayaran masuk baru ke dompet. Tujuannya adalah untuk memiliki firewall tambahan dalam kasus asosiasi antara identitas pengguna dan salah satu pasangan kuncinya.

Hari ini, dengan kehadiran perusahaan analisis rantai dan pengembangan KYC (Know Your Customer), penggunaan alamat kosong bukan lagi firewall tambahan, tetapi kewajiban bagi siapa saja yang peduli sedikit pun tentang privasi mereka.

Pengejaran privasi bukanlah kenyamanan atau fantasi dari Bitcoiner maksimalis. Ini adalah parameter spesifik yang langsung mempengaruhi keamanan pribadi Anda dan keamanan dana Anda. Untuk membantu Anda memahami ini, berikut adalah contoh yang sangat konkret:
- Bob membeli Bitcoin melalui Dollar Cost Averaging (DCA), yang berarti dia memperoleh sejumlah kecil Bitcoin pada interval reguler untuk meratakan harga masuknya. Bob secara sistematis mengirimkan dana yang dibeli ke alamat penerima yang sama. Dia membeli 0,01 Bitcoin setiap minggu dan mengirimkannya ke alamat yang sama ini. Setelah dua tahun, Bob telah mengumpulkan satu Bitcoin penuh di alamat ini.
- Tukang roti di sudut jalan menerima pembayaran Bitcoin. Senang bisa menghabiskan Bitcoin, Bob pergi untuk membeli baguetnya dalam satoshi. Untuk membayar, dia menggunakan dana yang terkunci dengan alamatnya. Tukang rotinya sekarang tahu bahwa dia memiliki sebuah Bitcoin. Jumlah yang signifikan ini bisa menarik iri hati, dan Bob berpotensi menghadapi risiko serangan fisik di masa depan.

Penggunaan ulang alamat memungkinkan pengamat untuk membuat tautan yang tidak dapat disangkal antara UTXO Anda yang berbeda dan terkadang antara identitas Anda dan seluruh dompet Anda.
Inilah mengapa sebagian besar perangkat lunak dompet Bitcoin secara otomatis menghasilkan alamat penerima baru ketika Anda mengklik tombol "Terima". Bagi pengguna reguler, membiasakan diri menggunakan alamat baru bukanlah ketidaknyamanan yang besar. Namun, untuk bisnis online, bursa, atau kampanye donasi, kendala ini dapat dengan cepat menjadi tidak terkelola.
Ada banyak solusi untuk organisasi-organisasi ini. Masing-masing memiliki kelebihan dan kekurangannya, tetapi hingga saat ini, dan seperti yang akan kita lihat nanti, BIP47 benar-benar menonjol dari yang lain.

Masalah penggunaan ulang alamat ini jauh dari sepele dalam Bitcoin. Seperti yang Anda lihat pada grafik di bawah ini yang diambil dari situs web oxt.me, tingkat penggunaan ulang alamat secara keseluruhan oleh pengguna Bitcoin saat ini adalah 52%:
Grafik dari OXT.me menunjukkan evolusi tingkat penggunaan ulang alamat secara keseluruhan pada jaringan Bitcoin.

![image](assets/2.webp)

Kredit: OXT

Mayoritas penggunaan ulang ini berasal dari bursa, yang, karena alasan efisiensi dan kenyamanan, menggunakan alamat yang sama berkali-kali. Hingga saat ini, BIP47 akan menjadi solusi terbaik untuk menanggulangi fenomena ini di antara bursa. Ini akan membantu mengurangi tingkat penggunaan ulang alamat secara keseluruhan tanpa menyebabkan terlalu banyak gesekan bagi entitas-entitas ini.

Ukuran global ini di seluruh jaringan sangat relevan dalam kasus ini. Memang, penggunaan ulang alamat bukan hanya masalah bagi orang yang terlibat dalam praktik ini, tetapi juga bagi siapa saja yang bertransaksi dengan mereka. Kehilangan privasi pada Bitcoin bertindak seperti virus, menyebar dari pengguna ke pengguna. Mempelajari ukuran global pada semua transaksi jaringan memungkinkan kita untuk memahami sejauh mana fenomena ini.

## Prinsip BIP47 dan PayNym.

BIP47 bertujuan untuk menyediakan cara sederhana untuk menerima beberapa pembayaran tanpa penggunaan ulang alamat. Operasinya didasarkan pada penggunaan kode pembayaran yang dapat digunakan kembali.

Dengan demikian, beberapa pengirim dapat mengirim beberapa pembayaran ke satu kode pembayaran yang dapat digunakan kembali dari pengguna lain, tanpa penerima perlu menyediakan alamat kosong baru untuk setiap transaksi baru.

Seorang pengguna dapat dengan bebas membagikan kode pembayarannya (di jejaring sosial, di situs web mereka...) tanpa risiko kehilangan privasi, tidak seperti alamat penerima reguler atau kunci publik.
Untuk melakukan pertukaran, kedua pengguna harus memiliki dompet Bitcoin dengan implementasi BIP47, seperti PayNym di Samourai Wallet atau Sparrow Wallet. Asosiasi kode pembayaran kedua pengguna akan menetapkan saluran rahasia di antara mereka. Untuk benar-benar menetapkan saluran ini, pengirim harus melakukan transaksi di blockchain Bitcoin: transaksi notifikasi (saya akan menjelaskan lebih lanjut tentang ini nanti).

Asosiasi kode pembayaran kedua pengguna menghasilkan rahasia bersama yang sendiri menghasilkan sejumlah besar alamat penerima Bitcoin unik (tepatnya 2^32). Dengan demikian, dalam kenyataannya, pembayaran dengan BIP47 tidak dikirim ke kode pembayaran, tetapi ke alamat normal sepenuhnya, yang berasal dari kode pembayaran pihak yang terlibat.
Kode pembayaran berfungsi sebagai pengenal virtual, yang berasal dari seed dompet. Dalam struktur derivasi dompet HD, kode pembayaran berada pada kedalaman 3, di tingkat akun dompet.
![image](assets/3.webp)

Tujuan derivasinya dicatat sebagai 47' (0x8000002F) merujuk pada BIP47. Sebagai contoh, sebuah jalur derivasi untuk kode pembayaran yang dapat digunakan kembali adalah:

> m/47'/0'/0'/

Untuk memberi Anda gambaran tentang bagaimana kode pembayaran itu terlihat, berikut adalah milik saya:

> PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5

Ini juga dapat dikodekan sebagai kode QR untuk memfasilitasi komunikasi:

![image](assets/4.webp)

Mengenai PayNym Bots, robot-robot yang Anda lihat di Twitter, mereka hanyalah representasi visual dari kode pembayaran Anda, yang dibuat oleh Samourai Wallet. Mereka dihasilkan menggunakan fungsi hash, yang membuatnya hampir unik. Berikut adalah milik saya dengan identifikasinya:

> +throbbingpond8B1

![image](assets/5.webp)

Bot-Bot ini tidak memiliki utilitas teknis yang sebenarnya. Sebaliknya, mereka memfasilitasi interaksi antar pengguna dengan menciptakan identitas visual virtual.

Untuk pengguna, proses melakukan pembayaran BIP47 dengan implementasi PayNym sangatlah sederhana. Mari kita bayangkan bahwa Alice ingin mengirim pembayaran kepada Bob:

1. Bob membagikan kode QR-nya atau langsung kode pembayaran yang dapat digunakan kembali. Dia dapat menempatkannya di situs webnya, di berbagai jaringan sosial publiknya, atau mengirimkannya kepada Alice melalui sarana komunikasi lain.
2. Alice membuka perangkat lunak Samourai atau Sparrow-nya dan memindai atau menempelkan kode pembayaran Bob.
3. Alice menghubungkan PayNym-nya dengan milik Bob ("Follow" dalam bahasa Inggris). Operasi ini dilakukan secara off-chain dan tetap sepenuhnya gratis.

4. Alice menghubungkan PayNym-nya dengan milik Bob ("Connect" dalam bahasa Inggris). Operasi ini dilakukan "on-chain". Alice harus membayar biaya penambangan transaksi serta biaya tetap sebesar 15.000 sats untuk layanan di Samourai. Biaya layanan dikecualikan di Sparrow. Langkah ini adalah apa yang kita sebut transaksi notifikasi.

5. Setelah transaksi notifikasi dikonfirmasi, Alice dapat membuat transaksi pembayaran BIP47 kepada Bob. Dompetnya akan secara otomatis menghasilkan alamat penerima baru yang kosong yang hanya Bob yang memiliki kunci privatnya.

Melakukan transaksi notifikasi, yaitu, menghubungkan PayNym-nya, adalah prasyarat wajib untuk melakukan pembayaran BIP47. Namun, setelah ini dilakukan, pengirim dapat melakukan banyak pembayaran kepada penerima (tepatnya 2^32) tanpa perlu melakukan transaksi notifikasi baru.

Anda mungkin telah memperhatikan bahwa ada dua operasi berbeda untuk menghubungkan PayNym bersama-sama: "follow" dan "connect". Operasi koneksi ("connect") sesuai dengan transaksi notifikasi BIP47, yang hanyalah transaksi Bitcoin dengan informasi tertentu yang ditransmisikan melalui output OP_RETURN. Dengan demikian, ini membantu menetapkan komunikasi terenkripsi antara dua pengguna untuk menghasilkan rahasia bersama yang diperlukan untuk menghasilkan alamat penerima baru yang kosong.

Di sisi lain, operasi penghubungan ("follow" atau "relier") memungkinkan untuk tautan pada Soroban, protokol komunikasi terenkripsi berbasis Tor, yang dikembangkan khusus oleh tim Samourai.

Untuk merangkum:
- Menghubungkan dua PayNym ("mengikuti") sepenuhnya gratis. Ini membantu membangun komunikasi terenkripsi off-chain, khususnya untuk menggunakan alat transaksi kolaboratif Samourai (Stowaway atau StonewallX2). Operasi ini spesifik untuk PayNym dan tidak dijelaskan dalam BIP47.
- Menghubungkan dua PayNym memerlukan biaya. Ini melibatkan pelaksanaan transaksi notifikasi untuk memulai koneksi. Biaya terdiri dari biaya layanan apa pun, biaya penambangan transaksi, dan 546 sats yang dikirim ke alamat notifikasi penerima untuk memberitahu mereka tentang pembukaan terowongan. Operasi ini terkait dengan BIP47. Setelah selesai, pengirim dapat melakukan beberapa pembayaran BIP47 ke penerima.

Untuk menghubungkan dua PayNym, mereka harus sudah terhubung.

## Tutorial: Menggunakan PayNym.

Sekarang setelah kita telah melihat teorinya, mari kita pelajari praktiknya bersama. Ide dari tutorial di bawah ini adalah untuk menghubungkan PayNym saya di dompet Sparrow saya dengan PayNym saya di dompet Samourai saya. Tutorial pertama menunjukkan cara melakukan transaksi menggunakan kode pembayaran yang dapat digunakan kembali dari Samourai ke Sparrow, dan tutorial kedua menjelaskan mekanisme yang sama dari Sparrow ke Samourai.

> Saya melakukan tutorial ini di Testnet. Ini bukan bitcoin yang sebenarnya.

### Membangun transaksi BIP47 dengan Dompet Samourai.

Untuk memulai, Anda tentu saja memerlukan aplikasi Dompet Samourai. Anda dapat langsung mengunduhnya dari Google Play Store atau dengan file APK yang tersedia di situs web resmi Samourai.

Setelah dompet diinisialisasi, jika Anda belum melakukannya, mintalah PayNym Anda dengan mengklik plus (+) di kanan bawah, lalu pada "PayNym".

Langkah pertama untuk melakukan pembayaran BIP47 adalah mengambil kode pembayaran yang dapat digunakan kembali dari penerima kita. Kemudian, kita akan dapat terhubung dengan mereka dan selanjutnya terhubung:

![video](assets/6.mp4)

Setelah transaksi notifikasi dikonfirmasi, saya dapat mengirim beberapa pembayaran ke penerima saya. Setiap transaksi akan secara otomatis dibuat dengan alamat kosong baru yang kunci-kuncinya dimiliki oleh penerima. Penerima tidak perlu melakukan tindakan apa pun, semuanya dihitung di sisi saya.

Berikut cara melakukan transaksi BIP47 di Dompet Samourai:

![video](assets/7.mp4)

### Membangun transaksi BIP47 dengan Dompet Sparrow.

Sama seperti dengan Samourai, Anda tentu saja perlu memiliki perangkat lunak Sparrow. Ini tersedia di komputer Anda. Anda dapat mengunduhnya dari [situs web resmi](https://sparrowwallet.com/) mereka.

Pastikan untuk memverifikasi tanda tangan pengembang dan integritas perangkat lunak yang diunduh sebelum menginstalnya di mesin Anda.

Buat dompet dan minta PayNym Anda dengan mengklik "Tampilkan PayNym" dari menu "Alat" di bilah atas:

![image](assets/8.webp)

Kemudian, Anda perlu menghubungkan dan menghubungkan PayNym Anda dengan PayNym penerima Anda. Untuk melakukan ini, masukkan kode pembayaran yang dapat digunakan kembali mereka di jendela "Temukan Kontak", ikuti mereka, dan kemudian lakukan transaksi notifikasi dengan mengklik "Hubungkan Kontak":

![image](assets/9.webp)

Setelah transaksi notifikasi dikonfirmasi, Anda dapat mengirim pembayaran ke kode pembayaran yang dapat digunakan kembali. Berikut cara melakukannya:

![video](assets/10.mp4)

Sekarang setelah kita dapat mempelajari aspek praktis dari implementasi PayNym dari BIP47, mari kita lihat bagaimana semua mekanisme ini bekerja dan metode kriptografi apa yang digunakan.

## Cara Kerja BIP47.
Untuk mempelajari mekanisme BIP47, sangat penting untuk memahami struktur dompet deterministik hierarkis (HD), mekanisme untuk menghasilkan pasangan kunci anak, serta prinsip-prinsip kriptografi kurva eliptik. Untungnya, Anda dapat menemukan semua informasi yang diperlukan untuk memahami bagian ini di blog saya:
- [Memahami jalur derivasi dari dompet Bitcoin](https://www.pandul.fr/post/comprendre-les-chemins-de-d%C3%A9rivation-d-un-portefeuille-bitcoin)

- [Dompet Bitcoin - kutipan dari ebook Bitcoin Democratized 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2)

### Kode pembayaran yang dapat digunakan kembali.

Seperti yang dijelaskan di bagian kedua dari makalah ini, kode pembayaran yang dapat digunakan kembali berada pada kedalaman tiga dari dompet HD. Hal ini agak dapat dibandingkan dengan xpub, baik dalam penempatan dan struktur, serta dalam perannya.

Berikut adalah bagian-bagian yang membentuk kode pembayaran 80-byte:

- Byte 0: Versi. Jika menggunakan versi pertama dari BIP47, byte ini akan sama dengan 0x01.

- Byte 1: Bidang bit. Ruang ini diperuntukkan untuk memberikan indikasi tambahan dalam kasus penggunaan spesifik. Jika hanya menggunakan PayNym, byte ini akan sama dengan 0x00.

- Byte 2: Paritas y. Byte ini menunjukkan 0x02 atau 0x03 tergantung pada paritas (angka genap atau ganjil) dari nilai koordinat y dari kunci publik kita. Untuk informasi lebih lanjut tentang praktik ini, silakan baca langkah 1 dari bagian "derivasi alamat" dari artikel ini.

- Dari byte 3 sampai byte 34: Nilai x. Byte-byte ini menunjukkan koordinat x dari kunci publik kita. Penggabungan x dan paritas y memberi kita kunci publik terkompresi kita.

- Dari byte 35 sampai byte 66: Kode rantai. Ruang ini diperuntukkan untuk kode rantai yang terkait dengan kunci publik yang disebutkan di atas.

- Dari byte 67 sampai byte 79: Padding. Ruang ini diperuntukkan untuk pengembangan masa depan yang mungkin. Untuk versi 1, kita hanya mengisinya dengan nol untuk mencapai 80 byte, yang merupakan ukuran data untuk output OP_RETURN.

Berikut adalah representasi heksadesimal dari kode pembayaran yang dapat digunakan kembali saya, yang disajikan di bagian sebelumnya, dengan warna yang sesuai dengan byte yang disajikan di atas:
Selanjutnya, Anda juga perlu menambahkan byte awalan "P" untuk dengan cepat mengidentifikasi bahwa kita sedang berurusan dengan kode pembayaran. Byte ini adalah 0x47.

> 0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000

Akhirnya, kita menghitung checksum dari kode pembayaran ini menggunakan HASH256, yang berarti penghashan ganda dengan fungsi SHA256. Kita mengambil empat byte pertama dari digest ini dan menggabungkannya di akhir (dalam warna merah muda).
Kode pembayaran sudah siap, sekarang kita hanya perlu mengonversinya ke Base 58:

> PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5

Seperti yang Anda lihat, konstruksi ini sangat mirip dengan struktur dari kunci publik ekstensi tipe "xpub".

Selama proses ini untuk mendapatkan kode pembayaran kita, kami menggunakan kunci publik terkompresi dan kode rantai. Kedua elemen ini adalah hasil dari derivasi deterministik dan hierarkis dari benih dompet, mengikuti jalur derivasi berikut: m/47'/0'/0'/
Secara konkret, untuk mendapatkan kunci publik dan kode rantai dari kode pembayaran yang dapat digunakan kembali, kami akan menghitung kunci privat utama dari benih, kemudian menurunkan pasangan anak dengan indeks 47 + 2^31 (derivasi diperketat). Kemudian, kami menurunkan dua pasangan anak lagi dengan indeks 2^31 (derivasi diperketat).

> Jika Anda ingin belajar lebih lanjut tentang menurunkan pasangan kunci anak dalam dompet Bitcoin deterministik hierarkis, saya merekomendasikan untuk mengambil CRYPTO301.

### Metode kriptografi: Pertukaran kunci Elliptic Curve Diffie-Hellman (ECDH).

Metode kriptografi yang digunakan di inti BIP47 adalah ECDH (Elliptic-Curve Diffie-Hellman). Protokol ini adalah varian dari pertukaran kunci Diffie-Hellman klasik.

Diffie-Hellman, dalam versi pertamanya, adalah protokol kesepakatan kunci yang dipresentasikan pada tahun 1976 yang memungkinkan dua pihak, masing-masing dengan pasangan kunci publik dan privat, untuk menentukan rahasia bersama dengan bertukar informasi melalui saluran komunikasi yang tidak aman.

![image](assets/11.webp)

Rahasia bersama ini (kunci merah) kemudian dapat digunakan untuk tugas lain. Biasanya, rahasia bersama ini dapat digunakan untuk mengenkripsi dan mendekripsi komunikasi melalui jaringan yang tidak aman:

![image](assets/12.webp)

Untuk mencapai pertukaran ini, Diffie-Hellman menggunakan aritmetika modular untuk menghitung rahasia bersama. Berikut adalah penjelasan sederhana tentang cara kerjanya:

- Alice dan Bob sepakat pada warna umum, dalam hal ini, kuning. Warna ini diketahui oleh semua orang. Ini adalah informasi publik.

- Alice memilih warna rahasia, dalam hal ini, merah. Dia mencampur kedua warna tersebut, menghasilkan oranye.

- Bob memilih warna rahasia, dalam hal ini, biru teal. Dia mencampur kedua warna tersebut, menghasilkan biru langit.

- Alice dan Bob dapat bertukar warna yang mereka dapatkan: oranye dan biru langit. Pertukaran ini dapat terjadi melalui jaringan yang tidak aman dan dapat diamati oleh penyerang.

- Alice mencampur warna biru langit yang diterima dari Bob dengan warna rahasianya (merah). Dia mendapatkan coklat.

- Bob mencampur warna oranye yang diterima dari Alice dengan warna rahasianya (biru teal). Dia juga mendapatkan coklat.

![image](assets/13.webp)
> z sama dengan A dipangkatkan dengan b modulo p:
> z = A^b % p

- Sebagai pengingat, A = g^a % p. Oleh karena itu:

  > z = A^b % p
  > z = (g^a)^b % p
  >
  > Menurut aturan eksponensial:
  >
  > (x^n)^m = x^nm
  >
  > Oleh karena itu:
  >
  > z = g^ab % p

Warna coklat dalam penyederhanaan ini mewakili rahasia bersama antara Alice dan Bob. Harus dibayangkan bahwa dalam kenyataannya, mustahil bagi penyerang untuk memisahkan warna oranye dan biru langit untuk mengambil rahasia warna Alice atau Bob.

Sekarang, mari kita pelajari cara kerjanya yang sebenarnya. Pada pandangan pertama, Diffie-Hellman mungkin tampak rumit untuk dipahami. Namun, prinsip operasinya hampir seperti permainan anak-anak. Sebelum menjelaskan mekanismenya, saya akan cepat mengingatkan Anda tentang dua konsep matematika yang akan kita perlukan (dan kebetulan, juga digunakan dalam banyak metode kriptografi lainnya).

1. Sebuah bilangan prima adalah bilangan alami yang hanya memiliki dua pembagi: 1 dan dirinya sendiri. Misalnya, angka 7 adalah prima karena hanya bisa dibagi dengan 1 dan 7 (dirinya sendiri). Di sisi lain, angka 8 bukan prima karena bisa dibagi dengan 1, 2, 4, dan 8. Jadi, ia tidak hanya memiliki dua pembagi, tetapi empat pembagi yang seluruhnya positif.

2. "Modulo" (dilambangkan "mod" atau "%") adalah operasi matematika yang memungkinkan dua bilangan bulat mengembalikan sisa dari pembagian Euklides dari bilangan pertama oleh bilangan kedua. Misalnya, 16 mod 5 sama dengan 1.

Pertukaran kunci Diffie-Hellman antara Alice dan Bob berfungsi sebagai berikut:

- Alice dan Bob menentukan dua angka umum: p dan g. p adalah bilangan prima. Semakin besar angka p ini, semakin aman Diffie-Hellman akan. g adalah akar primitif dari p. Kedua angka ini dapat dikomunikasikan dalam teks biasa melalui jaringan yang tidak aman, mereka adalah setara dengan warna kuning dalam penyederhanaan di atas. Alice dan Bob hanya perlu memiliki nilai yang sama persis untuk p dan g.

- Setelah parameter dipilih, Alice dan Bob masing-masing menentukan sebuah angka acak rahasia sendiri. Angka acak yang diperoleh Alice dinamakan a (setara dengan warna merah) dan angka acak yang diperoleh Bob dinamakan b (setara dengan warna teal). Kedua angka ini harus tetap rahasia.

- Alih-alih bertukar angka-angka a dan b ini, masing-masing pihak akan menghitung A (huruf besar) dan B (huruf besar) sedemikian rupa:

> A sama dengan g dipangkatkan dengan a modulo p:
> A = g^a % p

> B sama dengan g dipangkatkan dengan b modulo p:
> B = g^b % p

- Angka-angka A (setara dengan warna oranye) dan B (setara dengan warna biru langit) akan ditukar antara kedua pihak. Pertukaran dapat dilakukan dalam teks biasa melalui jaringan yang tidak aman.

- Alice, yang sekarang mengetahui B, akan menghitung nilai z sedemikian rupa:

> z sama dengan B dipangkatkan dengan a modulo p:
> z = B^a % p

- Sebagai pengingat, B = g^b % p. Oleh karena itu:

  > z = B^a % p
  > z = (g^b)^a % p
  >
  > Menurut aturan eksponensial:
  >
  > (x^n)^m = x^nm
  >
  > Oleh karena itu:
  >
  > z = g^ba % p

- Bob, yang sekarang mengetahui A, juga akan menghitung nilai z sebagai berikut:
z sama dengan A dipangkatkan dengan b modulo p:
> z = A^b % p

Oleh karena itu:

> z = (g^a)^b % p
> z = g^ab % p
> z = g^ba % p

Berkat sifat distributif dari operator modulo, Alice dan Bob menemukan nilai z yang sama persis. Angka ini mewakili rahasia bersama mereka, yang setara dengan warna coklat dalam penjelasan sebelumnya. Mereka dapat menggunakan rahasia bersama ini untuk mengenkripsi komunikasi antara mereka di jaringan yang tidak aman.

![Diagram Operasi Teknis Diffie-Hellman](assets/14.webp)

Seorang penyerang yang memiliki p, g, A, dan B akan tidak mampu menghitung a, b, atau z. Melakukan operasi ini akan memerlukan pembalikan eksponensiasi, yang tidak mungkin dilakukan selain dengan mencoba semua kemungkinan satu per satu karena kita bekerja dengan bidang terbatas. Ini akan setara dengan menghitung logaritma diskrit, yang merupakan kebalikan dari eksponensiasi dalam grup siklik terbatas.

Oleh karena itu, selama kita memilih nilai a, b, dan p yang cukup besar, Diffie-Hellman aman. Biasanya, dengan parameter 2.048 bit (angka dengan 600 digit dalam desimal), menguji semua kemungkinan untuk a dan b akan tidak praktis. Sampai saat ini, dengan angka sebesar ini, algoritma dianggap aman.

Inilah tepatnya di mana kelemahan utama dari protokol Diffie-Hellman terletak. Untuk aman, algoritma harus menggunakan angka-angka besar. Akibatnya, algoritma ECDH sekarang lebih disukai, yang merupakan varian dari Diffie-Hellman yang menggunakan kurva aljabar, khususnya kurva elips. Ini memungkinkan kita untuk bekerja dengan angka yang jauh lebih kecil sambil mempertahankan keamanan yang setara, sehingga mengurangi sumber daya komputasi dan penyimpanan yang diperlukan.

Prinsip umum dari algoritma tetap sama. Namun, alih-alih menggunakan angka acak a dan angka A yang dihitung dari a menggunakan eksponensiasi modular, kita akan menggunakan sepasang kunci yang ditetapkan pada kurva elips. Alih-alih mengandalkan sifat distributif dari operator modulo, kita akan menggunakan hukum grup pada kurva elips, khususnya asosiativitas dari hukum ini.
Jika Anda tidak memiliki pengetahuan tentang bagaimana kunci privat dan publik bekerja pada kurva elips, saya akan menjelaskan dasar-dasar metode ini dalam enam bagian pertama dari artikel ini.

Untuk merangkum secara kasar, kunci privat adalah angka acak antara 1 dan n-1 (di mana n adalah urutan dari kurva), dan kunci publik adalah titik unik pada kurva yang ditentukan oleh kunci privat melalui penambahan titik dan penggandaan dari titik generator, sebagai berikut:

> K = k·G

Di mana K adalah kunci publik, k adalah kunci privat, dan G adalah titik generator.

Salah satu sifat dari pasangan kunci ini adalah sangat mudah untuk menentukan K jika Anda tahu k dan G, tetapi saat ini tidak mungkin untuk menentukan k jika Anda tahu K dan G. Ini adalah fungsi satu arah.

Dengan kata lain, Anda dapat dengan mudah menghitung kunci publik jika Anda tahu kunci privat, tetapi tidak mungkin untuk menghitung kunci privat jika Anda tahu kunci publik. Keamanan ini sekali lagi didasarkan pada ketidakmungkinan menghitung logaritma diskrit.

Kita akan menggunakan sifat ini untuk menyesuaikan algoritma Diffie-Hellman kita. Dengan demikian, prinsip operasi ECDH adalah sebagai berikut:

- Alice dan Bob sepakat pada kurva elips yang aman secara kriptografi dan parameternya. Informasi ini bersifat publik.
- Alice menghasilkan sebuah angka acak ka, yang akan menjadi kunci privatnya. Kunci privat ini harus tetap rahasia. Dia menentukan kunci publiknya Ka dengan menambahkan dan menggandakan titik-titik pada kurva eliptik yang dipilih.
> Ka = ka·G

- Bob juga menghasilkan sebuah angka acak kb, yang akan menjadi kunci privatnya. Dia menghitung kunci publik terkait Kb.

> Kb = kb·G

- Alice dan Bob bertukar kunci publik mereka Ka dan Kb melalui jaringan publik yang tidak aman.

- Alice menghitung sebuah titik (x, y) pada kurva dengan menerapkan kunci privatnya ka ke kunci publik Bob Kb.

> (x, y) = ka·Kb

- Bob menghitung sebuah titik (x, y) pada kurva dengan menerapkan kunci privatnya kb ke kunci publik Alice Ka.

> (x, y) = kb·Ka

- Alice dan Bob mendapatkan titik yang sama pada kurva eliptik. Rahasia bersama akan menjadi koordinat x dari titik ini.

Mereka memperoleh rahasia bersama yang sama karena:

> (x, y) = ka·Kb = ka·kb·G = kb·ka·G = kb·Ka

Seorang penyerang potensial yang mengamati jaringan publik yang tidak aman hanya dapat memperoleh kunci publik dari masing-masing pihak dan parameter kurva yang dipilih. Seperti yang dijelaskan sebelumnya, kedua informasi ini saja tidak memungkinkan untuk menentukan kunci privat, sehingga penyerang tidak dapat mengakses rahasia.
ECDH adalah algoritma yang memungkinkan pertukaran kunci. Sering digunakan bersama dengan metode kriptografi lain untuk mendefinisikan protokol. Sebagai contoh, ECDH digunakan dalam inti TLS (Transport Layer Security), protokol enkripsi dan otentikasi yang digunakan untuk lapisan transport internet. TLS menggunakan ECDHE untuk pertukaran kunci, varian dari ECDH di mana kunci-kunci bersifat efemeral untuk menyediakan kerahasiaan yang persisten. Selain ECDHE, TLS juga menggunakan algoritma otentikasi seperti ECDSA, algoritma enkripsi seperti AES, dan fungsi hash seperti SHA256.

TLS mendefinisikan "s" dalam "https" dan ikon gembok kecil yang Anda lihat di sudut kiri atas browser internet Anda, yang menjamin komunikasi terenkripsi. Jadi, Anda saat ini menggunakan ECDH dengan membaca artikel ini, dan kemungkinan Anda menggunakannya setiap hari tanpa menyadarinya.

### Transaksi notifikasi.

Seperti yang kita temukan di bagian sebelumnya, ECDH adalah varian dari pertukaran Diffie-Hellman yang melibatkan pasangan kunci yang didirikan pada kurva eliptik. Untungnya, kita memiliki banyak pasangan kunci yang memenuhi standar ini di dompet Bitcoin kita!

Ide ini adalah menggunakan pasangan kunci dari dompet Bitcoin hierarkis deterministik kedua belah pihak untuk menetapkan rahasia bersama dan efemeral di antara mereka. Dalam BIP47, ECDHE (Elliptic Curve Diffie-Hellman Ephemeral) digunakan sebagai gantinya.

ECDHE digunakan awalnya dalam BIP47 untuk mentransmisikan kode pembayaran pengirim ke penerima. Ini adalah transaksi notifikasi yang terkenal. Agar BIP47 dapat digunakan, kedua belah pihak (pengirim yang mengirim pembayaran dan penerima yang menerima pembayaran) perlu mengetahui kode pembayaran masing-masing. Ini diperlukan untuk menurunkan kunci publik efemeral dan oleh karena itu alamat penerimaan yang didedikasikan.
Sebelum pertukaran ini, pengirim secara logis sudah mengetahui kode pembayaran penerima karena mereka bisa mendapatkannya secara off-chain, misalnya dari situs web atau media sosial mereka. Namun, penerima mungkin tidak necessarily mengetahui kode pembayaran pengirim. Ini perlu ditransmisikan kepada mereka, jika tidak mereka tidak akan dapat menurunkan kunci efemeral mereka dan oleh karena itu tidak akan dapat mengetahui di mana bitcoin mereka berada dan membuka dana mereka. Ini bisa ditransmisikan kepada mereka secara off-chain, menggunakan sistem komunikasi lain, tetapi ini akan menimbulkan masalah jika dompet dipulihkan dari seed. Memang, seperti yang telah saya sebutkan, alamat BIP47 tidak diturunkan dari seed penerima (jika tidak, akan lebih baik menggunakan salah satu xpub mereka secara langsung), tetapi merupakan hasil dari perhitungan yang melibatkan kode pembayaran penerima dan kode pembayaran pengirim. Oleh karena itu, jika penerima kehilangan dompet mereka dan mencoba memulihkannya dari seed mereka, mereka akan necessarily perlu memiliki semua kode pembayaran orang-orang yang telah mengirimkan mereka bitcoin melalui BIP47.

Akan mungkin untuk menggunakan BIP47 tanpa transaksi notifikasi ini, tetapi setiap pengguna perlu membackup kode pembayaran rekan mereka. Situasi ini akan tetap tidak terkelola sampai cara yang sederhana dan tangguh untuk membuat, menyimpan, dan memperbarui backup ini ditemukan. Transaksi notifikasi oleh karena itu hampir wajib dalam keadaan saat ini.

Selain perannya dalam membackup kode pembayaran, seperti namanya, transaksi ini juga berfungsi sebagai notifikasi kepada penerima. Ini menginformasikan klien mereka bahwa sebuah terowongan baru saja dibuka.

Sebelum menjelaskan lebih detail tentang fungsi teknis transaksi notifikasi, saya ingin sedikit berbicara tentang model privasi. Memang, model privasi BIP47 membenarkan beberapa tindakan pencegahan yang diambil saat membangun transaksi awal ini.

Kode pembayaran itu sendiri tidak langsung menimbulkan risiko terhadap privasi. Tidak seperti model Bitcoin klasik, yang memungkinkan pemutusan aliran informasi antara identitas pengguna dan transaksi, terutama dengan menjaga anonimitas kunci publik, kode pembayaran dapat langsung dikaitkan dengan identitas. Ini tidak wajib, tetapi tautan ini tidak berbahaya.

Memang, kode pembayaran tidak langsung menurunkan alamat yang digunakan untuk menerima pembayaran BIP47. Sebaliknya, alamat diperoleh dengan menerapkan ECDHE antara kunci anak dari kode pembayaran kedua belah pihak.

Oleh karena itu, kode pembayaran sendiri tidak menimbulkan risiko langsung terhadap privasi karena hanya alamat notifikasi yang diturunkan darinya. Beberapa informasi dapat disimpulkan darinya, tetapi normalnya seseorang tidak dapat mengetahui dengan siapa Anda bertransaksi.

Oleh karena itu, sangat penting untuk mempertahankan pemisahan ketat antara kode pembayaran pengguna. Dalam hal ini, langkah komunikasi awal dari kode adalah momen kritis untuk privasi pembayaran, dan namun itu wajib untuk fungsi protokol yang tepat. Jika salah satu kode pembayaran dapat diambil secara publik (misalnya, dari situs web), kode kedua, yaitu kode pengirim, tidak boleh dikaitkan dengan yang pertama.

Misalnya, mari kita bayangkan saya ingin membuat donasi dengan BIP47 ke gerakan protes damai di Kanada:

- Organisasi ini telah mempublikasikan kode pembayarannya langsung di situs web atau platform media sosial mereka.
- Kode ini oleh karena itu dikaitkan dengan gerakan tersebut.

- Saya mengambil kode pembayaran ini.

- Sebelum saya dapat mengirimkan mereka transaksi, saya harus memastikan bahwa mereka menyadari kode pembayaran pribadi saya, yang juga dikaitkan dengan identitas saya karena saya menggunakannya untuk menerima transaksi dari jaringan sosial saya.

Bagaimana saya bisa mentransmisikannya kepada mereka? Jika saya mengirimkannya kepada mereka menggunakan sarana komunikasi konvensional, informasi mungkin bocor, dan saya mungkin diidentifikasi sebagai orang yang mendukung gerakan damai.
Transaksi notifikasi tentunya bukan satu-satunya solusi untuk mentransmisikan kode pembayaran pengirim secara rahasia, namun saat ini peran tersebut terpenuhi dengan sempurna dengan menerapkan berbagai lapisan keamanan. Pada diagram di bawah ini, garis merah mewakili momen ketika aliran informasi harus diputus, dan panah hitam mewakili hubungan yang tidak dapat disangkal yang dapat dibuat oleh pengamat eksternal:

![Model privasi diagram untuk kode pembayaran yang dapat digunakan kembali](assets/15.webp)

Dalam kenyataannya, untuk model privasi klasik Bitcoin, seringkali sulit untuk sepenuhnya memutus aliran informasi antara pasangan kunci dan pengguna, terutama saat melakukan transaksi jarak jauh. Sebagai contoh, dalam kasus kampanye donasi, penerima akan diminta untuk mengungkapkan alamat atau kunci publik di situs web atau platform media sosial mereka. Penggunaan BIP47 yang tepat, yaitu, dengan transaksi notifikasi, menyelesaikan masalah ini melalui ECDHE dan lapisan enkripsi yang akan kita pelajari.

Tentu saja, model privasi klasik Bitcoin masih diamati pada tingkat kunci publik efemeral yang berasal dari asosiasi dua kode pembayaran. Kedua model tersebut saling tergantung. Saya hanya ingin menekankan di sini bahwa, tidak seperti penggunaan klasik kunci publik untuk menerima bitcoin, kode pembayaran dapat dikaitkan dengan identitas karena informasi "Bob melakukan transaksi dengan Alice" diputus pada momen lain. Kode pembayaran digunakan untuk menghasilkan alamat pembayaran, tetapi dengan hanya mengamati blockchain, mustahil untuk mengaitkan transaksi pembayaran BIP47 dengan kode pembayaran yang digunakan untuk membuatnya.

### Konstruksi transaksi notifikasi.

Sekarang, mari kita lihat bagaimana transaksi notifikasi ini bekerja. Bayangkan Alice ingin mengirim dana ke Bob menggunakan BIP47. Dalam contoh saya, Alice bertindak sebagai pengirim dan Bob sebagai penerima. Bob telah mempublikasikan kode pembayarannya di situs webnya, jadi Alice sudah mengetahui kode pembayaran Bob.

1. Alice menghitung rahasia bersama dengan ECDH:

- Dia memilih sepasang kunci dari dompet HD-nya yang terletak pada cabang yang berbeda dari kode pembayarannya. Perlu diperhatikan bahwa pasangan ini seharusnya tidak mudah dikaitkan dengan alamat notifikasi Alice atau identitas Alice (lihat bagian sebelumnya).
- Alice memilih kunci privat dari pasangan ini. Kita akan menyebutnya "a" (huruf kecil).

> a

- Alice mengambil kunci publik yang terkait dengan alamat notifikasi Bob. Kunci ini adalah anak pertama yang berasal dari kode pembayaran Bob (indeks 0). Kita akan menyebut kunci publik ini "B" (huruf besar). Kunci privat yang terkait dengan kunci publik ini disebut "b" (huruf kecil). "B" ditentukan oleh penambahan titik dan penggandaan pada kurva eliptik dari "G" (titik generator) dengan "b" (kunci privat).

> B = b·G

- Alice menghitung titik rahasia "S" (huruf besar) pada kurva eliptik dengan penambahan titik dan penggandaan, menerapkan kunci privatnya "a" ke kunci publik Bob "B".

> S = a·B

- Alice menghitung faktor penyamaran "f" yang akan digunakan untuk mengenkripsi kode pembayarannya. Untuk melakukan ini, dia akan menghasilkan nomor pseudo-acak menggunakan fungsi HMAC-SHA512. Sebagai input kedua ke fungsi ini, dia menggunakan nilai yang hanya bisa diambil oleh Bob: (x), yang merupakan koordinat x dari titik rahasia yang sebelumnya dihitung. Input pertama adalah (o), yang merupakan UTXO yang dikonsumsi sebagai input untuk transaksi ini (outpoint).

> f = HMAC-SHA512(o, x)

2. Alice mengonversi kode pembayarannya ke basis 2 (biner).
3. Dia menggunakan faktor pengaburan ini sebagai kunci untuk melakukan enkripsi simetris pada muatan kode pembayarannya. Algoritma enkripsi yang digunakan adalah XOR. Operasi yang dilakukan mirip dengan sandi Vernam, yang juga dikenal sebagai "one-time pad":
- Alice pertama-tama membagi faktor pengaburannya menjadi dua bagian: 32 byte pertama disebut "f1" dan 32 byte terakhir disebut "f2". Jadi kita memiliki:

> f = f1 || f2

- Alice menghitung ciphertext (x') dari koordinat x dari kunci publik (x) dari kode pembayarannya, dan secara terpisah menghitung ciphertext (c') dari kode rantainya (c). "f1" dan "f2" bertindak sebagai kunci enkripsi, dan operasi XOR digunakan.

> x' = x XOR f1
>
> c' = c XOR f2

- Alice menggantikan nilai sebenarnya dari absis kunci publik (x) dan kode rantai (c) dalam kode pembayarannya dengan nilai-nilai terenkripsi (x') dan (c').

Sebelum melanjutkan dengan deskripsi teknis transaksi notifikasi ini, mari kita bahas sejenak tentang operasi XOR. XOR adalah operator logika bitwise berdasarkan aljabar Boolean. Diberikan dua operan bit, ini mengembalikan 1 jika bit yang bersesuaian berbeda, dan mengembalikan 0 jika bit yang bersesuaian sama. Berikut adalah tabel kebenaran untuk XOR berdasarkan nilai operan D dan E:

| D   | E   | D XOR E |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

Contohnya:

> 0110 XOR 1110 = 1000

Atau:

> 010011 XOR 110110 = 100101

Dengan ECDH, penggunaan XOR sebagai lapisan enkripsi sangat koheren. Pertama, berkat operator ini, enkripsinya simetris. Ini memungkinkan penerima untuk mendekripsi kode pembayaran dengan kunci yang sama yang digunakan untuk enkripsi. Kunci enkripsi dan dekripsi dihitung dari rahasia bersama menggunakan ECDH.

Simetri ini diaktifkan oleh sifat komutativitas dan asosiativitas dari operator XOR:

- Sifat lainnya:
  -> D ⊕ D = 0
  -> D ⊕ 0 = D

- Komutativitas:
  D ⊕ E = E ⊕ D

- Asosiativitas:
  D ⊕ (E ⊕ Z) = (D ⊕ E) ⊕ Z = D ⊕ E ⊕ Z

- Simetri:
  Jika: D ⊕ E = L
  Maka: D ⊕ L = D ⊕ (D ⊕ E) = D ⊕ D ⊕ E = 0 ⊕ E = E
  -> D ⊕ L = E
Selanjutnya, metode enkripsi ini sangat mirip dengan sandi Vernam (One-Time Pad), satu-satunya algoritma enkripsi yang hingga saat ini diketahui memiliki keamanan mutlak (atau tanpa syarat). Agar sandi Vernam memiliki karakteristik ini, kunci enkripsi harus benar-benar acak, berukuran sama dengan pesan, dan hanya digunakan sekali. Dalam metode enkripsi yang digunakan di sini untuk BIP47, kunci memang berukuran sama dengan pesan, faktor pengaburan persis berukuran sama dengan penggabungan koordinat x dari kunci publik dengan kode rantai kode pembayaran. Kunci enkripsi ini memang hanya digunakan sekali. Namun, kunci ini tidak berasal dari sumber acak sempurna karena merupakan HMAC. Ini lebih bersifat pseudo-random. Oleh karena itu, ini bukan sandi Vernam, tetapi metodenya serupa.
Mari kita kembali ke konstruksi transaksi notifikasi kami:

4. Saat ini Alice memiliki kode pembayarannya dengan muatan terenkripsi. Dia akan membangun dan menyiarkan transaksi yang melibatkan kunci publiknya "A" sebagai input, output ke alamat notifikasi Bob, dan output OP_RETURN yang terdiri dari kode pembayarannya dengan muatan terenkripsi. Transaksi ini adalah transaksi notifikasi.

OP_RETURN adalah Opcode, yang merupakan skrip yang menandai output transaksi Bitcoin sebagai tidak valid. Saat ini, digunakan untuk menyiarkan atau mengankor informasi di blockchain Bitcoin. Ini dapat menyimpan hingga 80 byte data yang dicatat di rantai dan oleh karena itu terlihat oleh semua pengguna lain.

Seperti yang kita lihat di bagian sebelumnya, Diffie-Hellman digunakan untuk menghasilkan rahasia bersama antara dua pengguna yang berkomunikasi melalui jaringan yang tidak aman, yang berpotensi diamati oleh penyerang. Dalam BIP47, ECDH digunakan untuk berkomunikasi di jaringan Bitcoin, yang secara alamiah adalah jaringan komunikasi transparan yang diamati oleh banyak penyerang. Rahasia bersama yang dihitung melalui pertukaran kunci Diffie-Hellman pada kurva eliptik kemudian digunakan untuk mengenkripsi informasi rahasia yang akan ditransmisikan: kode pembayaran pengirim (Alice).

Berikut adalah diagram yang diambil dari BIP47 yang menggambarkan apa yang baru saja kami jelaskan:

![Diagram Alice mengirim kode pembayaran bertopengnya ke alamat notifikasi Bob](assets/16.webp)

Kredit: Kode Pembayaran yang Dapat Digunakan Kembali untuk Dompet Deterministik Hierarkis, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Jika kita cocokkan diagram ini dengan apa yang saya jelaskan sebelumnya:

- "Wallet Priv-Key" di sisi Alice sesuai dengan: a.

- "Child Pub-Key 0" di sisi Bob sesuai dengan: B.
- "Notification Shared Secret" sesuai dengan: f.
- "Masked Payment Code" sesuai dengan kode pembayaran terenkripsi, yaitu, dengan muatan terenkripsi: x' dan c'.

- "Notification Transaction" adalah transaksi yang berisi OP_RETURN.

Mari kita rekap langkah-langkah yang baru saja kita lalui untuk melakukan transaksi notifikasi:

- Alice mengambil kode pembayaran dan alamat notifikasi Bob.

- Alice memilih UTXO yang miliknya di dompet HD-nya dengan pasangan kunci yang sesuai.

- Dia menghitung titik rahasia pada kurva eliptik menggunakan ECDH.

- Dia menggunakan titik rahasia ini untuk menghitung HMAC, yang merupakan faktor pengaburan.

- Dia menggunakan faktor pengaburan ini untuk mengenkripsi muatan kode pembayaran pribadinya.

- Dia menggunakan output transaksi OP_RETURN untuk mentransfer kode pembayaran bertopeng ke Bob.

Untuk lebih memahami operasinya, terutama penggunaan OP_RETURN, mari kita pelajari transaksi notifikasi nyata bersama-sama. Saya melakukan transaksi jenis ini di Testnet, yang bisa Anda temukan dengan mengklik di sini:
Dengan mengamati transaksi ini, kita dapat melihat bahwa transaksi ini memiliki satu input dan 4 output:

- Output pertama adalah OP_RETURN yang berisi kode pembayaran saya yang telah disamarkan.

- Output kedua sebesar 546 sats mengarah ke alamat notifikasi penerima.

- Output ketiga sebesar 15.000 sats mewakili biaya layanan, karena saya menggunakan Samourai Wallet untuk membangun transaksi ini.

- Output keempat sebesar dua juta sats mewakili kembalian, yaitu selisih yang tersisa dari input saya yang kembali ke alamat lain yang dimiliki oleh saya.

Yang paling menarik untuk dipelajari adalah tentunya output 0 menggunakan OP_RETURN. Mari kita lihat lebih dekat apa yang terkandung di dalamnya:

Kita menemukan skrip heksadesimal dari output:

> 6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d800000000000000000000000000

Dalam skrip ini, kita dapat memecah beberapa bagian:
Di antara opcode, kita dapat mengenali 0x6a yang merujuk pada OP_RETURN dan 0x4c yang merujuk pada OP_PUSHDATA1. Byte berikutnya setelah opcode ini menunjukkan ukuran payload yang mengikuti. Ini menunjukkan 0x50, yang adalah 80 byte.

Selanjutnya datang kode pembayaran dengan payload terenkripsi.

Berikut adalah kode pembayaran saya yang digunakan dalam transaksi ini:

> Dalam base 58:
>
> PM8TJQCyt6ovbozreUCBrfKqmSVmTzJ5vjqse58LnBzKFFZTwny3KfCDdwTqAEYVasn11tTMPc2FJsFygFd3YzsHvwNXLEQNADgxeGnMK8Ugmin62TZU
>
> Dalam base 16 (HEX):
> 4701000277507c9c17a89cfca2d3af554745d6c2db0e7f6b2721a3941a504933103cc42add94881210d6e752a9abc8a9fa0070e85184993c4f643f1121dd807dd556d1dc000000000000000000000000008604e4db

Jika kita membandingkan kode pembayaran saya dengan OP_RETURN, kita dapat melihat bahwa HRP (dalam coklat) dan checksum (dalam merah muda) tidak ditransmisikan. Ini normal, karena informasi ini ditujukan untuk manusia.
Selanjutnya, kita dapat mengenali (dalam warna hijau) versi (0x01), bidang bit (0x00), dan paritas kunci publik (0x02). Dan, di akhir kode pembayaran, byte kosong dalam warna hitam (0x00) yang memungkinkan padding untuk mencapai total 80 byte. Semua metadata ini ditransmisikan dalam plaintext (tidak terenkripsi). Akhirnya, kita dapat mengamati bahwa koordinat-x dari kunci publik (dalam warna biru) dan kode rantai (dalam warna merah) telah dienkripsi. Ini merupakan payload dari kode pembayaran.

### Menerima transaksi notifikasi.

Sekarang Alice telah mengirim transaksi notifikasi kepada Bob, mari kita lihat bagaimana dia menafsirkannya.

Sebagai pengingat, Bob harus bisa mengakses kode pembayaran Alice. Tanpa informasi ini, seperti yang akan kita lihat di bagian selanjutnya, dia tidak akan bisa menurunkan pasangan kunci yang dibuat oleh Alice, dan oleh karena itu, dia tidak akan bisa mengakses bitcoinnya yang diterima dengan BIP47. Untuk saat ini, payload kode pembayaran Alice dienkripsi. Mari kita lihat bersama bagaimana Bob mendekripsinya.

1. Bob memantau transaksi yang menciptakan output dengan alamat notifikasinya.

2. Ketika sebuah transaksi memiliki output ke alamat notifikasinya, Bob menganalisisnya untuk melihat apakah itu mengandung output OP_RETURN yang mematuhi standar BIP47.

3. Jika byte pertama dari payload OP_RETURN adalah 0x01, Bob memulai pencariannya untuk rahasia bersama yang mungkin dengan ECDH:

- Bob memilih kunci publik dalam input transaksi. Yaitu, kunci publik Alice yang dinamakan "A" dengan:

> A = a·G

- Bob memilih kunci privat "b" yang terkait dengan alamat notifikasi pribadinya:

> b

- Bob menghitung titik rahasia "S" (rahasia bersama ECDH) pada kurva eliptik dengan menambahkan dan menggandakan titik, menerapkan kunci privat "b" ke kunci publik Alice "A":

> S = b·A

- Bob menentukan faktor penyamaran "f" yang akan memungkinkan dia untuk mendekripsi payload kode pembayaran Alice. Dengan cara yang sama seperti Alice menghitungnya sebelumnya, Bob akan menemukan "f" dengan menerapkan HMAC-SHA512 ke (x) nilai koordinat-x dari titik rahasia "S", dan ke (o) UTXO yang dikonsumsi sebagai input dalam transaksi notifikasi ini:

> f = HMAC-SHA512(o, x)

4. Bob menafsirkan data dalam OP_RETURN dari transaksi notifikasi sebagai kode pembayaran. Dia hanya mendekripsi payload dari kode pembayaran potensial ini menggunakan faktor penyamaran "f".

- Bob memisahkan faktor penyamaran "f" menjadi dua bagian: 32 byte pertama dari "f" akan menjadi "f1" dan 32 byte terakhir akan menjadi "f2".
- Bob mendekripsi nilai koordinat-x yang dienkripsi (x') dari kunci publik kode pembayaran Alice:

> x = x' XOR f1

- Bob mendekripsi nilai kode rantai yang dienkripsi (c') dari kode pembayaran Alice:

> c = c' XOR f2

5. Bob memeriksa apakah nilai kunci publik kode pembayaran Alice merupakan bagian dari grup secp256k1. Jika iya, dia menafsirkannya sebagai kode pembayaran yang valid. Jika tidak, dia mengabaikan transaksi tersebut.

Sekarang Bob mengetahui kode pembayaran Alice, dia dapat mengiriminya hingga 2^32 pembayaran tanpa perlu melakukan transaksi notifikasi seperti ini lagi.

Mengapa ini berhasil? Bagaimana Bob bisa menentukan faktor penyamaran yang sama seperti Alice dan mendekripsi kode pembayarannya? Mari kita periksa proses ECDH lebih detail berdasarkan apa yang baru saja kita deskripsikan.
Pertama-tama, kita berurusan dengan enkripsi simetris. Ini berarti bahwa kunci enkripsi dan kunci dekripsi memiliki nilai yang sama. Dalam kasus ini, kunci dalam transaksi notifikasi adalah faktor pengaburan (f = f1 || f2). Alice dan Bob perlu mendapatkan nilai yang sama untuk f tanpa mengirimkannya secara langsung, karena penyerang dapat mencegatnya dan mendekripsi informasi rahasia.

Faktor pengaburan ini diperoleh dengan menerapkan HMAC-SHA512 pada dua nilai: koordinat x dari titik rahasia dan UTXO yang digunakan dalam input transaksi. Oleh karena itu, Bob perlu memiliki dua informasi ini untuk mendekripsi payload kode pembayaran Alice.

Untuk UTXO input, Bob dapat dengan mudah mengambilnya dengan mengamati transaksi notifikasi. Untuk titik rahasia, Bob akan harus menggunakan ECDH.

Seperti yang terlihat dalam bagian tentang Diffie-Hellman, dengan bertukar kunci publik masing-masing dan secara rahasia menerapkan kunci privat mereka ke kunci publik orang lain, Alice dan Bob dapat menemukan titik spesifik dan rahasia pada kurva eliptik. Transaksi notifikasi bergantung pada mekanisme ini:

> Pasangan kunci Bob:
>
> B = b·G
>
> Pasangan kunci Alice:
>
> A = a·G
>
> Untuk titik rahasia S (x,y):
>
> S = a·B = a·b·G = b·a·G = b·A

![Diagram menghasilkan rahasia bersama dengan ECDHE](assets/19.webp)
Sekarang Bob mengetahui kode pembayaran Alice, dia akan dapat mendeteksi pembayaran BIP47-nya dan menurunkan kunci privat yang menghalangi bitcoin yang diterimanya.
![Bob menafsirkan transaksi notifikasi Alice](assets/20.webp)

Kredit: Kode Pembayaran yang Dapat Digunakan Kembali untuk Dompet Deterministik Hierarkis, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Jika kita cocokkan diagram ini dengan apa yang telah saya jelaskan kepada Anda sebelumnya:

- "Wallet Pub-Key" di sisi Alice sesuai dengan: A.

- "Child Priv-Key 0" di sisi Bob sesuai dengan: b.

- "Notification Shared Secret" sesuai dengan: f.

- "Masked Payment Code" sesuai dengan kode pembayaran Alice yang terenkripsi, yaitu, dengan payload terenkripsi: x' dan c'.

- "Notification Transaction" adalah transaksi yang berisi OP_RETURN.

Izinkan saya merangkum langkah-langkah yang baru saja kita lihat bersama untuk menerima dan menafsirkan transaksi notifikasi:

- Bob memantau output transaksi ke alamat notifikasinya.

- Ketika dia mendeteksi satu, dia mengambil informasi yang terkandung dalam OP_RETURN.

- Bob memilih kunci publik input dan menghitung titik rahasia menggunakan ECDH.

- Dia menggunakan titik rahasia ini untuk menghitung HMAC, yang merupakan faktor pengaburan.

- Dia menggunakan faktor pengaburan ini untuk mendekripsi payload kode pembayaran Alice yang terkandung dalam OP_RETURN.

### Transaksi pembayaran BIP47.

Mari kita sekarang mempelajari proses pembayaran dengan BIP47. Untuk mengingatkan Anda tentang situasi saat ini:

- Alice mengetahui kode pembayaran Bob, yang dia ambil sederhana dari situs webnya.

- Bob mengetahui kode pembayaran Alice berkat transaksi notifikasi.

- Alice akan melakukan pembayaran awal kepada Bob. Dia dapat melakukan banyak lagi dengan cara yang sama.

Sebelum menjelaskan proses ini kepada Anda, saya pikir penting untuk mengingatkan Anda tentang indeks mana yang saat ini kita kerjakan:

Kita mendeskripsikan jalur derivasi kode pembayaran sebagai berikut: m/47'/0'/0'/.

Kedalaman berikutnya mendistribusikan indeks sebagai berikut:
- Pasangan anak pertama (non-hardened) digunakan untuk menghasilkan alamat notifikasi yang kita bahas di bagian sebelumnya: m/47'/0'/0'/0/.
- Pasangan kunci anak normal digunakan dalam ECDH untuk menghasilkan alamat penerima pembayaran BIP47, seperti yang akan kita lihat di bagian ini: m/47'/0'/0'/ dari 0 hingga 2.147.483.647/.

- Pasangan kunci anak yang hardened adalah kode pembayaran efemeral: m/47'/0'/0'/ dari 0' hingga 2.147.483.647'/.
  Setiap kali Alice ingin mengirim pembayaran ke Bob, dia menghasilkan alamat kosong unik baru, sekali lagi berkat protokol ECDH:
- Alice memilih kunci privat pertama yang berasal dari kode pembayaran pribadi yang dapat digunakan kembali:

> a

- Alice memilih kunci publik yang belum digunakan yang berasal dari kode pembayaran Bob. Kunci publik ini, kita akan menyebutnya "B". Ini terkait dengan kunci privat "b" yang hanya diketahui oleh Bob.

> B = b·G

- Alice menghitung titik rahasia "S" pada kurva eliptik dengan menambahkan dan menggandakan titik, menerapkan kunci privatnya "a" ke kunci publik Bob "B":

> S = a·B

- Dari titik rahasia ini, Alice akan menghitung rahasia bersama "s" (huruf kecil). Untuk melakukan ini, dia memilih koordinat x dari titik rahasia "S" yang disebut "Sx", dan dia memasukkan nilai ini ke dalam fungsi hash SHA256.

> s = SHA256(Sx)

Jangan percaya. Verifikasi! Jika Anda ingin memahami prinsip dasar dari fungsi hash, Anda akan menemukan yang Anda butuhkan dalam artikel ini. Dan jika Anda tidak mempercayai NIST (Anda benar), dan Anda ingin dapat memahami secara detail bagaimana SHA256 bekerja, saya menjelaskan semuanya dalam artikel ini dalam bahasa Prancis.

- Alice menggunakan rahasia bersama "s" ini untuk menghitung alamat penerima pembayaran Bitcoin. Pertama, dia memeriksa bahwa "s" berada dalam urutan kurva secp256k1. Jika tidak, dia meningkatkan indeks kunci publik Bob untuk menghasilkan rahasia bersama lainnya.

- Kedua, dia menghitung kunci publik "K0" dengan menambahkan titik "B" dan "s·G" pada kurva eliptik. Dengan kata lain, Alice menambahkan kunci publik yang berasal dari kode pembayaran Bob "B" dengan titik lain yang dihitung pada kurva eliptik dengan menambahkan dan menggandakan titik dengan rahasia bersama "s" dari titik generator kurva secp256k1 "G". Titik baru ini mewakili kunci publik, dan kita menyebutnya "K0":

> K0 = B + s·G

- Dengan kunci publik "K0" ini, Alice dapat menghasilkan alamat penerima kosong dengan cara standar (misalnya, SegWit V0 dalam Bech32).

Setelah Alice memiliki alamat penerima "K0" yang milik Bob, dia dapat membuat transaksi Bitcoin standar dengan memilih UTXO yang miliknya pada cabang lain dari dompet HD-nya, dan menghabiskannya ke alamat "K0" Bob.

![Alice mengirim bitcoin dengan BIP47 ke Bob](assets/21.webp)

Kredit: Kode Pembayaran yang Dapat Digunakan Kembali untuk Dompet Deterministik Hierarkis, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki
Jika kita cocokkan diagram ini dengan yang saya jelaskan kepada Anda sebelumnya:

- "Child Priv-Key" di sisi Alice sesuai dengan: a.
- "Child Pub-Key 0" di sisi Bob sesuai dengan: B.
- "Payment Secret 0" sesuai dengan: s.
- "Payment Pub-Key 0" sesuai dengan: K0.
Izinkan saya merangkum langkah-langkah yang baru saja kita lalui bersama untuk mengirim pembayaran BIP47:

- Alice memilih kunci privat anak turunan pertama dari kode pembayaran pribadinya.
- Dia menghitung titik rahasia pada kurva eliptik menggunakan ECDH dari kunci publik anak turunan pertama yang belum digunakan dari kode pembayaran Bob.
- Dia menggunakan titik rahasia ini untuk menghitung rahasia bersama dengan SHA256.
- Dia menggunakan rahasia bersama ini untuk menghitung titik rahasia baru pada kurva eliptik.
- Dia menambahkan titik rahasia baru ini ke kunci publik Bob.
- Dia mendapatkan kunci publik efemeral baru yang hanya Bob yang memiliki kunci privat yang terkait.
- Alice dapat mengirim transaksi reguler ke Bob dengan alamat penerima efemeral yang diturunkan.

Jika dia ingin melakukan pembayaran kedua, dia akan mengulangi langkah-langkah di atas, kecuali dia akan memilih kunci publik anak turunan kedua dari kode pembayaran Bob. Artinya, kunci yang belum digunakan berikutnya. Dia kemudian akan memiliki alamat penerima kedua yang dimiliki oleh Bob, "K1".

![Alice menurunkan tiga alamat penerima BIP47 untuk Bob](assets/22.webp)

Kredit: Kode Pembayaran yang Dapat Digunakan Kembali untuk Dompet Deterministik Hierarkis, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Dia dapat melanjutkan seperti ini dan menurunkan hingga 2^32 alamat kosong yang dimiliki oleh Bob.

Dari perspektif eksternal, dengan mengamati blockchain Bitcoin, secara teoritis tidak mungkin membedakan pembayaran BIP47 dari pembayaran reguler. Berikut adalah contoh transaksi pembayaran BIP47 di Testnet:

https://blockstream.info/testnet/tx/94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

TXID:

> 94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

Ini terlihat seperti transaksi reguler dengan input yang terpakai, output pembayaran sebesar 210.000 sats, dan perubahan.

![Transaksi pembayaran Bitcoin dengan BIP47](assets/23.webp)

Kredit: https://blockstream.info/

### Menerima pembayaran BIP47 dan menurunkan kunci privat.

Alice baru saja melakukan pembayaran pertamanya ke alamat BIP47 kosong yang dimiliki oleh Bob. Sekarang mari kita lihat bagaimana Bob menerima pembayaran ini. Kita juga akan melihat mengapa Alice tidak memiliki akses ke kunci privat dari alamat yang baru saja dia buat, dan bagaimana Bob mengambil kunci ini untuk menghabiskan bitcoin yang baru saja dia terima.

Segera setelah Bob menerima transaksi notifikasi dari Alice, dia menurunkan kunci publik BIP47 "K0" bahkan sebelum dia mengirim pembayaran kepadanya. Dia oleh karena itu mengamati pembayaran apa pun ke alamat yang terkait. Sebenarnya, dia segera menurunkan beberapa alamat yang akan dia amati (K0, K1, K2, K3...). Berikut cara dia menurunkan kunci publik ini "K0":

- Bob memilih kunci privat anak turunan pertama dari kode pembayarannya. Kunci privat ini dinamakan "b". Ini terkait dengan kunci publik "B" yang digunakan Alice pada langkah sebelumnya:

> b

- Bob memilih kunci publik anak turunan pertama Alice dari kode pembayarannya. Kunci ini dinamakan "A". Ini terkait dengan kunci privat "a" yang digunakan Alice dalam perhitungannya, dan hanya Alice yang mengetahuinya. Bob dapat melakukan proses ini karena dia mengetahui kode pembayaran Alice yang ditransmisikan kepadanya dengan transaksi notifikasi.

> A = a·G
- Bob menghitung titik rahasia "S" dengan menambahkan dan menggandakan titik pada kurva eliptik, menerapkan kunci privatnya "b" ke kunci publik Alice "A". Di sini kita menggunakan ECDH, yang menjamin bahwa titik "S" ini akan sama untuk Bob dan Alice.
> S = b·A

- Sama seperti yang dilakukan Alice, Bob mengisolasi koordinat x dari titik "S" ini. Kami telah menamai nilai ini "Sx". Dia melewati nilai ini melalui fungsi SHA256 untuk menemukan rahasia bersama "s" (huruf kecil).

> s = SHA256(Sx)

- Sama seperti Alice, Bob menghitung titik "s·G" pada kurva eliptik. Kemudian, dia menambahkan titik rahasia ini ke kunci publiknya "B". Dia kemudian memperoleh titik baru pada kurva eliptik yang dia interpretasikan sebagai kunci publik "K0":

> K0 = B + s·G

Setelah Bob memiliki kunci publik "K0" ini, dia dapat menurunkan kunci privat terkait untuk menghabiskan bitcoinnya. Dia adalah satu-satunya yang dapat menghasilkan angka ini.

- Bob menambahkan kunci privat anak turunan "b" dari kode pembayaran pribadinya. Dia adalah satu-satunya yang dapat memperoleh nilai "b". Kemudian, dia menambahkan "b" ke rahasia bersama "s" untuk memperoleh k0, kunci privat dari K0:

> k0 = b + s
> Berkat hukum grup dari kurva eliptik, Bob mendapatkan tepat kunci privat yang sesuai dengan kunci publik yang digunakan oleh Alice. Jadi kita memiliki:
> K0 = k0·G

![Bob menghasilkan alamat penerimaan BIP47-nya](assets/24.webp)

Kredit: Kode Pembayaran yang Dapat Digunakan Kembali untuk Dompet Deterministik Hierarkis, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Jika kita cocokkan diagram ini dengan yang saya jelaskan kepada Anda sebelumnya:

- "Child Priv-Key 0" di sisi Bob sesuai dengan: b.

- "Child Pub-Key 0" di sisi Alice sesuai dengan: A.

- "Payment Secret 0" sesuai dengan: s.

- "Payment Pub-Key 0" sesuai dengan: K0.

- "Payment Priv-Key 0" sesuai dengan: k0.

Mari saya rangkum langkah-langkah yang baru saja kita lihat bersama untuk menerima pembayaran BIP47 dan menghitung kunci privat yang sesuai:

- Bob memilih kunci privat anak turunan pertama dari kode pembayaran pribadinya.

- Dia menghitung titik rahasia pada kurva eliptik menggunakan ECDH dari kunci publik anak turunan pertama dari kode rantai Alice.

- Dia menggunakan titik rahasia ini untuk menghitung rahasia bersama dengan SHA256.

- Dia menggunakan rahasia bersama ini untuk menghitung titik rahasia baru pada kurva eliptik.

- Dia menambahkan titik rahasia baru ini ke kunci publik pribadinya.

- Dia memperoleh kunci publik efemeral baru, ke mana Alice akan mengirim pembayaran pertamanya.

- Bob menghitung kunci privat yang terkait dengan kunci publik efemeral ini dengan menambahkan kunci privat anak turunan dari kode pembayarannya dan rahasia bersama.

Karena Alice tidak dapat memperoleh "b," kunci privat Bob, dia tidak dapat menentukan k0, kunci privat yang terkait dengan alamat penerimaan BIP47 Bob.

Secara skematis, kita dapat merepresentasikan perhitungan rahasia bersama "S" sebagai berikut:

![Perhitungan rahasia bersama dengan ECDHE](assets/25.webp)

Setelah rahasia bersama ditemukan dengan ECDH, Alice dan Bob menghitung kunci publik pembayaran BIP47 "K0," dan Bob juga menghitung kunci privat terkait "k0".
### Pengembalian Dana Pembayaran BIP47.

Karena Bob sudah mengetahui kode pembayaran yang dapat digunakan kembali milik Alice, dia sudah memiliki semua informasi yang diperlukan untuk mengirimkan pengembalian dana kepadanya. Dia tidak perlu menghubungi Alice untuk meminta informasi apapun. Dia hanya perlu memberitahukannya dengan transaksi notifikasi, terutama agar dia dapat memulihkan alamat BIP47-nya dengan seed-nya, dan kemudian dia juga dapat mengirimkan hingga 2^32 pembayaran kepadanya.
Bob kemudian dapat mengganti dana Alice dengan cara yang sama seperti dia mengirimkan pembayaran kepadanya. Peran mereka terbalik:

![Bob mengirimkan pengembalian dana kepada Alice dengan BIP47](assets/27.webp)

Kredit: Kode Pembayaran yang Dapat Digunakan Kembali untuk Dompet Deterministik Hierarkis, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Anda sekarang mengetahui semua kelebihan dan kekurangan solusi luar biasa yang BIP47 wakili.

## Penggunaan Turunan dari PayNym.

Implementasi BIP47 ini pada Samourai Wallet telah menghasilkan PayNyms, pengenal yang dihitung dari kode pembayaran pengguna. Saat ini, kegunaannya jauh melampaui penggunaan BIP47.

Tim Samourai secara bertahap mengembangkan seluruh ekosistem alat dan layanan berdasarkan PayNym pengguna. Di antaranya, tentu saja semua alat pengeluaran yang memungkinkan optimasi privasi pengguna dengan menambahkan entropi ke transaksi, dan dengan demikian menambahkan plausible deniability.

Penggunaan gabungan dari Soroban, jaringan komunikasi terenkripsi berbasis Tor, dan PayNyms telah sangat mengoptimalkan pengalaman pengguna saat membangun transaksi kolaboratif, sambil mempertahankan tingkat keamanan yang baik. Dengan demikian, mudah untuk melakukan transaksi Stowaway (PayJoin) dan StonewallX2 tanpa harus secara manual melakukan pertukaran transaksi yang tidak ditandatangani yang diperlukan untuk mengatur transaksi kolaboratif seperti itu.

Berbeda dengan penggunaan BIP47, karena transaksi kolaboratif ini tidak memerlukan transaksi notifikasi, cukup untuk menghubungkan PayNyms untuk menggunakan alat ini. Tidak perlu menghubungkannya.

Jika Anda ingin mempelajari lebih lanjut tentang transaksi kolaboratif, dan lebih luas tentang semua alat pengeluaran Samourai Wallet, Anda dapat membaca bagian "Alat Pengeluaran" dalam artikel ini. Anda akan menemukan penjelasan teknis dan tutorial terperinci untuk setiap alat.

Selain transaksi kolaboratif ini, baru-baru ini diamati bahwa tim Samourai sedang mengerjakan protokol autentikasi yang terkait dengan PayNym: Auth47. Alat ini sudah diimplementasikan dan memungkinkan, misalnya, autentikasi dengan PayNym di situs web yang menerima metode ini. Di masa depan, saya pikir bahwa di luar kemungkinan autentikasi di web ini, Auth47 akan menjadi bagian dari proyek yang lebih besar seputar ekosistem BIP47/PayNym/Samourai. Mungkin protokol ini akan digunakan untuk lebih mengoptimalkan pengalaman pengguna Samourai Wallet, terutama dalam penggunaan alat pengeluaran. Kita lihat saja...

## Pendapat Pribadi Saya tentang BIP47.

Jelas, kelemahan utama dari BIP47 adalah transaksi notifikasi. Ini membuat pengguna harus mengeluarkan biaya untuk penambangannya, yang bisa menjadi masalah bagi sebagian orang. Namun, argumen "spam" di blockchain Bitcoin sama sekali tidak dapat diterima. Siapa pun yang membayar biaya untuk transaksinya harus dapat mencatatnya di buku besar, terlepas dari tujuannya. Mengklaim sebaliknya adalah mendukung sensor.

Mungkin di masa depan, solusi lain yang lebih murah akan ditemukan untuk mengkomunikasikan kode pembayaran pengirim ke penerima, dan bagi penerima untuk menyimpannya dengan aman. Tapi untuk saat ini, transaksi notifikasi tetap menjadi solusi dengan kompromi paling sedikit.
Kerugian ini tetap dapat diabaikan ketika mempertimbangkan semua manfaat dari BIP47. Dari semua usulan yang ada untuk menyelesaikan masalah penggunaan ulang alamat ini, menurut saya, ini adalah solusi terbaik.

Seperti yang dijelaskan sebelumnya, sebagian besar penggunaan ulang alamat berasal dari bursa. BIP47 adalah satu-satunya solusi yang masuk akal dan benar-benar menyelesaikan masalah ini dari sumbernya. Setiap usulan yang bertujuan untuk mengurangi jumlah penggunaan ulang alamat harus fokus pada aspek ini dan menyesuaikan solusinya dengan sumber utama masalah tersebut.

Dari segi kegunaan, meskipun mekanisme internalnya cukup kompleks, prosedur pembayaran BIP47 sangat sederhana. Kode pembayaran yang dapat digunakan kembali oleh karena itu dapat dengan mudah diadopsi, bahkan oleh pengguna pemula.

Dari segi privasi, BIP47 sangat menarik. Seperti yang saya jelaskan dalam bagian tentang transaksi notifikasi, kode pembayaran tidak mengungkapkan informasi apa pun tentang alamat efemeral yang diturunkan. Oleh karena itu, ini memutus aliran informasi antara transaksi Bitcoin dan pengenal penerima, tidak seperti penggunaan tradisional alamat penerima.

Dan yang terpenting, implementasi PayNym dari BIP47 berhasil! Ini telah tersedia di Samourai Wallet sejak 2016 dan di Sparrow Wallet sejak awal tahun ini. Ini bukan proyek ilmiah, tetapi solusi yang telah diuji kemarin dan sepenuhnya berfungsi hari ini.

Semoga, di masa depan, kode pembayaran yang dapat digunakan kembali ini akan diadopsi oleh aktor ekosistem, diimplementasikan dalam perangkat lunak dompet, dan digunakan oleh para pengguna Bitcoin.

Setiap solusi yang benar-benar positif untuk privasi pengguna harus didiskusikan, didorong, dan dibela, agar Bitcoin tidak menjadi tempat bermain CA dan alat pengawasan pemerintah.
Dia memikirkan bagaimana dia telah dianiaya dan dihina di mana-mana, dan sekarang dia mendengar semua orang mengatakan bahwa dia adalah yang paling indah dari semua burung indah ini! Dan bahkan pohon elderberry membungkuk cabangnya ke arahnya, dan matahari menyebarkan cahaya yang hangat dan penuh welas asih! Kemudian bulunya mengembang, lehernya yang ramping terentang, dan dia berseru dengan sepenuh hatinya, "Bagaimana aku bisa bermimpi tentang kebahagiaan sebanyak ini ketika aku hanya seekor anak itik yang jelek."

## Untuk lebih lanjut:

- Memahami dan menggunakan CoinJoin di Bitcoin.

- Memahami jalur derivasi dari dompet Bitcoin.

- Menginstal dan menggunakan node Bitcoin RoninDojo Anda.

### Sumber eksternal dan ucapan terima kasih:

Terima kasih kepada LaurentMT dan Théo Pantamis atas banyak konsep yang mereka jelaskan kepada saya, yang saya gunakan dalam artikel ini. Saya berharap saya telah menyampaikannya dengan akurat.

Terima kasih kepada Fanis Michalakis atas koreksi teks ini dan saran ahlinya.

- https://bitcoiner.guide/paynym/
- https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman_bas%C3%A9_sur_les_courbes_elliptiques
- https://security.stackexchange.com/questions/46802/what-is-the-difference-between-dhe-and-ecdh#:~:text=The%20difference%20between%20DHE%20and%20ECDH%20in%20two%20bullet%20points,a%20type%20of%20algebraic%20curve).
- https://commandlinefanatic.com/cgi-bin/showarticle.cgi?article=art060
- https://ee.stanford.edu/~hellman/publications/24.pdf
- https://www.researchgate.net/publication/317339928_A_study_on_diffie-hellman_key_exchange_protocols