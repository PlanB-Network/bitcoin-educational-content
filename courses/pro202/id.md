---
name: Pemrograman Bitcoin
goal: Membangun pustaka Bitcoin yang lengkap dari awal dan memahami dasar-dasar kriptografi Bitcoin
objectives: 

 - Menerapkan operasi aritmatika bidang terbatas dan kurva elips dalam Python
 - Membangun dan mengurai transaksi Bitcoin secara terprogram
 - Membuat alamat testnet dan menyiarkan transaksi melalui jaringan
 - Menguasai dasar-dasar matematika yang mendasari model keamanan Bitcoin

---
# Perjalanan ke dalam Skrip dan Program Bitcoin


Kursus intensif dua hari ini, yang diajarkan oleh Jimmy Song, akan membawa Anda jauh ke dalam dasar-dasar teknis Bitcoin dengan membangun perpustakaan Bitcoin yang lengkap dari bawah ke atas. Dimulai dengan matematika esensial dari bidang terbatas dan kurva elips, Anda akan maju melalui penguraian transaksi, eksekusi skrip, dan komunikasi jaringan. Melalui latihan pengkodean langsung di buku catatan Jupyter, Anda akan membuat alamat testnet Anda sendiri, membuat transaksi secara manual, dan menyiarkannya langsung ke jaringan - semuanya sambil mendapatkan pemahaman mendalam tentang prinsip-prinsip kriptografi yang membuat Bitcoin aman dan tidak dapat dipercaya.


Selamat menikmati perjalanan!


+++

# Pendahuluan


<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>


## Ikhtisar Kursus


<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>


Selamat datang di kursus PRO 202 _**Pemrograman Bitcoin**_, sebuah perjalanan intensif yang akan membawa Anda dari aritmatika bidang terbatas hingga membangun dan menyiarkan transaksi nyata pada Bitcoin Testnet.


Dalam kursus ini, Anda akan secara bertahap membangun perpustakaan Bitcoin di Python sambil memperoleh dasar-dasar kriptografi, protokol, dan perangkat lunak yang diperlukan untuk menalar secara tepat tentang keamanan dan cara kerja Bitcoin. Pendekatan PRO 202 benar-benar praktis: setiap konsep langsung diimplementasikan dalam buku catatan Jupyter, memastikan bahwa teori dan kode saling memperkuat satu sama lain.


### Konsep Matematika Esensial untuk Bitcoin


Bagian pertama ini menetapkan dasar matematika yang sangat diperlukan. Anda akan mengimplementasikan aritmatika lapangan terbatas dan operasi kurva eliptik (hukum grup, penjumlahan, penggandaan, perkalian skalar...) - prasyarat untuk ECDSA. Tujuannya ada dua: untuk memahami struktur aljabar yang memungkinkan tanda tangan kriptografi dan membangun alat Python yang andal untuk memanipulasinya.


Anda kemudian akan memformalkan komponen-komponen ECDSA: pembuatan kunci, pemformatan titik, hashing, pembuatan tanda tangan, dan verifikasi. Bagian ini secara langsung menghubungkan teori dengan praktik, menekankan pada detail implementasi dan ketangguhan model keamanan yang mendasarinya.


### Cara Kerja Transaksi Bitcoin


Di bagian kedua, Anda akan membedah struktur transaksi Bitcoin: UTXO, input/output, urutan, skrip, penyandian, dan banyak lagi. Anda akan menulis kode untuk membuat, menandatangani, dan memverifikasi transaksi, mendapatkan pemahaman yang tepat tentang apa yang dilakukan oleh hash dan mengapa.


Selanjutnya, Anda akan mengimplementasikan eksekutor _Script_ minimal, meninjau opcode kunci, dan memvalidasi jalur pengeluaran. Tujuannya adalah agar Anda mampu mengaudit perilaku transaksi, mendiagnosa kegagalan validasi, dan memberikan alasan tentang keamanan kebijakan pengeluaran.


### Cara Kerja Bagian Dalam Jaringan Bitcoin


Pada bagian ketiga, Anda akan menempatkan transaksi di dalam sistem yang lebih luas: struktur blok, header, tingkat kesulitan, dan mekanisme Proof-of-Work. Anda akan menangani pesan protokol, header blok, dan pohon Merkle.


Terakhir, Anda akan mempelajari komunikasi node peer-to-peer, pengoptimalan pesan, dan pengenalan SegWit.


Seperti halnya setiap kursus Plan ₿ Academy, bagian akhir kursus ini mencakup evaluasi yang dirancang untuk mengkonsolidasikan pemahaman Anda. Siap untuk mengungkap cara kerja Bitcoin dan menulis kode yang menggerakkannya? Mari kita mulai!










# Konsep Matematika Esensial untuk Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Matematika untuk Implementasi Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>


![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


### Dasar-dasar Pemrograman Bitcoin: Struktur Matematika Inti


Kursus ini memadatkan matematika esensial di balik sistem kriptografi Bitcoin ke dalam alur kerja yang sangat praktis. Konsep-konsep akan dijelaskan, didemonstrasikan dengan contoh-contoh, dan kemudian diimplementasikan dalam Jupyter Notebook. Ide panduannya sederhana: Anda hanya benar-benar memahami primitif kriptografi setelah Anda mengkodekannya. Selama dua hari, para siswa akan mempelajari alamat testnet generate, membangun dan menyiarkan [transaksi](https://planb.academy/resources/glossary/transaction-tx), dan pada akhirnya berinteraksi dengan jaringan tanpa penjelajah blok. Semua ini membutuhkan fondasi yang kuat dalam bidang terbatas dan kurva elips.


### Bidang Berhingga: Mesin Aritmatika Kriptografi


Lapangan terbatas F(p) adalah sistem aritmatika yang didefinisikan oleh bilangan prima p, yang berisi elemen 0 sampai p-1. Field prima memastikan setiap elemen bukan nol memiliki kebalikannya dan semua operasi tetap berada di dalam field tersebut. Aritmatika membungkus menggunakan modulo p untuk penjumlahan, pengurangan, dan perkalian. Python `pow(base, exp, mod)` memungkinkan eksponensial modular yang efisien, sangat penting untuk eksponen besar yang digunakan dalam operasi kriptografi yang sebenarnya.


#### Perilaku Multiplikatif

Mengalikan setiap elemen bukan nol k dengan semua elemen dari sebuah lapangan prima menghasilkan sebuah permutasi dari lapangan tersebut. Sifat ini menjamin keseragaman dan mencegah kelemahan struktural, membuat lapangan prima ideal untuk pembuatan kunci yang aman dan [tanda tangan digital](https://planb.academy/resources/glossary/digital-signature).


#### Pembagian dan Teorema Kecil Fermat

Pembagian diimplementasikan melalui invers perkalian. Teorema Kecil Fermat menyatakan bahwa

n^(p-1) ≡ 1 (mod p),

jadi kebalikannya adalah n^(p-2). Python mendukung hal ini secara langsung dengan `pow(n, -1, p)`. Operasi-operasi ini muncul secara konstan dalam rutinitas kriptografi yang mendasari [ECDSA](https://planb.academy/resources/glossary/ecdsa) dan Bitcoin.


### Kurva Elips: Struktur Nonlinier untuk Keamanan Kunci Publik


Kurva elips mengikuti persamaan y² = x³ + ax + b. Bitcoin menggunakan secp256k1, yang didefinisikan sebagai y² = x³ + 7 pada bidang terbatas. Titik-titik pada kurva elips membentuk kelompok matematika di bawah penjumlahan titik. Sebuah garis yang ditarik melalui dua titik P dan Q memotong kurva pada titik ketiga R; merefleksikan R pada sumbu x menghasilkan P + Q. Sistem ini bersifat asosiatif dan memiliki sebuah elemen identitas: titik di tak terhingga.


Penggandaan sebuah titik menggunakan garis singgung dan bukannya garis sekan, dengan kemiringan yang berasal dari turunan kurva. Meskipun rumus-rumus ini melibatkan kalkulus pada bilangan real, rumus-rumus ini menjadi sepenuhnya diskrit dan eksak ketika kurva didefinisikan pada bidang yang terbatas-konteks yang digunakan dalam Bitcoin.


### Dari Matematika hingga Kriptografi Bitcoin


Bidang terbatas menyediakan aritmatika yang deterministik dan dapat dibalik; kurva eliptik menyediakan struktur nonlinier di mana komputasi k-P mudah dilakukan, namun membalikkannya tidak mungkin dilakukan secara komputasi. Menggabungkan keduanya akan menghasilkan fondasi untuk kunci publik/privat Bitcoin, tanda tangan ECDSA, dan keamanan transaksi. Dengan memahami dasar-dasar ini, para pelajar dapat mengimplementasikan kunci, transaksi, dan tanda tangan secara langsung-tanpa abstraksi atau alat bantu eksternal.


## Kriptografi Kurva Elips

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>


![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


Bab ini memperkenalkan kurva eliptik yang didefinisikan pada bidang terbatas dan menjelaskan mengapa kurva ini membentuk tulang punggung matematika dari [kriptografi](https://planb.academy/resources/glossary/cryptography) Bitcoin. Meskipun kurva eliptik pada bilangan real terlihat mulus dan kontinu, menerapkan persamaan yang sama pada bidang yang terbatas akan menghasilkan sekumpulan titik yang diskrit dan tersebar. Terlepas dari perbedaan visual, semua rumus penjumlahan titik, kemiringan, dan aturan aljabar berperilaku sama persis - hanya aritmatika yang berubah menjadi aritmatika modular. Bitcoin menggunakan kurva y² = x³ + 7 (secp256k1), yang mempertahankan simetri dan perilaku nonlinier yang sangat penting untuk keamanan kriptografi.


### Memverifikasi Poin dan Implementasi Lapangan Terbatas


Sebuah titik terletak pada sebuah kurva eliptik bidang terbatas jika koordinatnya memenuhi persamaan kurva di bawah modulo p. Memverifikasi sebuah titik seperti (73,128) pada F₁₃₇ membutuhkan pengecekan bahwa y² mod p sama dengan x³ + 7 mod p. Menerapkan hal ini pada kode melibatkan pembuatan kelas-kelas untuk elemen-elemen bidang terbatas dan titik-titik kurva. Kelebihan operator memastikan bahwa semua aritmatika-penjumlahan, perkalian, eksponensial, pembagian-dilakukan secara otomatis dalam bentuk modulo p. Ketika abstraksi-abstraksi ini sudah ada, operasi-operasi kriptografi yang lebih canggih akan lebih mudah untuk ditulis dan dinalar.


#### Properti Grup dan Penambahan Poin

Titik-titik kurva elips membentuk kelompok matematika di bawah penjumlahan. Grup ini memenuhi sifat penutupan, asosiatif, identitas (titik pada tak terhingga), dan invers (refleksi pada sumbu x). Konstruksi geometris mengkonfirmasi sifat-sifat ini, membuat perkalian skalar (P ditambahkan ke dirinya sendiri berulang kali) terdefinisi dengan baik. Aturan kelompok ini memungkinkan kriptografi kurva eliptik dan memastikan perilaku yang konsisten dan dapat diprediksi dalam operasi titik berulang.


### Grup Siklik dan Masalah Logaritma Diskrit


Memilih titik generator G pada kurva memungkinkan kita untuk membuat grup siklik: G, 2G, 3G, ..., nG = 0. Titik-titik tersebut tampak nonlinier dan tidak dapat diprediksi, bahkan ketika dibangkitkan secara berurutan. Ketidakpastian ini menciptakan fondasi untuk masalah logaritma diskrit: menghitung P = sG adalah mudah, tetapi menentukan s dari P secara komputasi tidak dapat dilakukan untuk grup-grup yang besar. Fungsi satu arah inilah yang membuat kriptografi [kunci publik](https://planb.academy/resources/glossary/public-key) menjadi aman. Skala ([kunci privat](https://planb.academy/resources/glossary/private-key)) ditulis dengan huruf kecil; titik (kunci publik) dengan huruf besar.


#### Perkalian Skalar yang Efisien

Untuk menghitung sG secara efisien, implementasi menggunakan algoritma double-and-add: memindai representasi biner dari skalar, menggandakan titik pada setiap langkah, dan menambahkan G hanya jika bitnya adalah 1. Hal ini mengurangi komputasi dari penambahan O(n) menjadi O(log n), sehingga memungkinkan operasi kriptografi yang praktis bahkan dengan skalar 256-bit.


#### Kurva secp256k1 dalam Bitcoin


Bitcoin menggunakan kurva secp256k1, yang didefinisikan oleh y² = x³ + 7 pada bidang prima di mana p = 2²⁵⁶ - 2³² - 977. Titik generator G memiliki koordinat tetap yang dipilih dengan menggunakan prosedur NUMS ("tidak ada yang bisa saya lakukan") yang deterministik. Urutan kelompok n adalah bilangan prima yang besar yang mendekati 2²⁵⁶, memastikan bahwa setiap titik bukan nol menghasilkan kelompok yang sama. Ukuran 2²⁵⁶ (~10⁷⁷) sangat besar secara astronomis, membuat kunci pribadi yang dipaksakan secara fisik menjadi tidak mungkin. Bahkan satu triliun superkomputer yang berjalan selama satu triliun tahun tidak akan mengurangi ruang kunci secara signifikan.


### Kunci Publik, Kunci Privat, dan Serialisasi SEC


Kunci privat adalah sebuah skalar acak s; kunci publik adalah P = sG. Karena pemecahan masalah log diskrit tidak mungkin dilakukan, P dapat dibagikan tanpa mengungkapkan s. Kunci publik harus diserialisasikan untuk transmisi menggunakan format SEC. Format SEC yang tidak terkompresi menggunakan 65 byte: awalan 0x04 + koordinat x + koordinat y. Format terkompresi hanya menggunakan 33 byte: awalan 0x02 atau 0x03 (tergantung pada paritas y) + koordinat-x. Bitcoin awalnya menggunakan kunci yang tidak terkompresi tetapi sekarang lebih memilih yang terkompresi untuk efisiensi.


#### Bitcoin Address Penciptaan


Alamat Bitcoin adalah hash dari kunci publik, bukan kunci mentah itu sendiri. Untuk generate sebuah alamat, serialisasi kunci publik dalam format SEC, hitung hash160 ([SHA-256](https://planb.academy/resources/glossary/sha256) kemudian RIPEMD-160), tambahkan awalan jaringan (0x00 untuk mainnet, 0x6F untuk testnet), hitung checksum dengan menggunakan SHA-256 ganda, tambahkan empat byte checksum pertama, dan enkode hasilnya dengan menggunakan Base58. Pengkodean ini menghilangkan karakter yang ambigu dan menyertakan checksum untuk mencegah kesalahan transkripsi. Pipeline multi-langkah menyembunyikan kunci publik hingga terjadi pengeluaran, menambahkan identifikasi jaringan, dan memastikan alamat yang dapat dibaca manusia dan tahan terhadap kesalahan.


# Bitcoin Cara Kerja Transaksi Bagian Dalam

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Penguraian Transaksi Bitcoin dan Tanda Tangan ECDSA

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>


![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


### Memahami ECDSA: Fondasi Tanda Tangan Digital Bitcoin


Bitcoin mengandalkan ECDSA, sebuah skema tanda tangan berbasis kurva eliptik yang menawarkan keamanan yang kuat dengan ukuran kunci yang jauh lebih kecil daripada RSA. Keamanannya berasal dari masalah logaritma diskrit kurva eliptik: mengingat P = eG, menghitung P mudah, tetapi mendapatkan e dari P tidak mungkin dilakukan secara komputasi. Asimetri ini memungkinkan kriptografi kunci publik sekaligus menjaga kunci pribadi tetap aman.


#### Pengkodean DER Tanda Tangan ECDSA


Bitcoin mengkodekan tanda tangan ECDSA menggunakan format DER:


- 0x30 (penanda urutan)
- panjang byte
- 0x02 + panjang + R byte
- 0x02 + panjang + S byte


Hal ini menambah overhead, memperluas tanda tangan 64-byte menjadi ~71-72 byte. [Taproot](https://planb.academy/resources/glossary/taproot) menghilangkan ketidakefisienan ini dengan mengadopsi tanda tangan [Schnorr](https://planb.academy/resources/glossary/schnorr-protocol) ukuran tetap.


### Komitmen Tanda Tangan dan Proses Penandatanganan


Tanda tangan ECDSA bergantung pada persamaan komitmen: UG + VP = KG. Penanda tangan memilih nilai U dan V yang bukan nol, dan sebuah [nonce](https://planb.academy/resources/glossary/nonce) acak K, yang membuktikan pengetahuan tentang kunci pribadi tanpa mengungkapkannya. Pesan tersebut di-hash menjadi Z, sebuah K acak dibangkitkan, R adalah koordinat x dari KG, dan S = (Z + RE) / K. Tanda tangan adalah pasangan (R, S). Keamanan sangat bergantung pada penggunaan K yang unik dan tidak dapat diprediksi-jika K digunakan kembali atau bocor, kunci privat akan terganggu. Implementasi modern menggunakan pembangkitan K deterministik (RFC 6979) untuk menghindari kegagalan RNG.


#### Verifikasi Tanda Tangan

Diberikan Z, (R, S), dan kunci publik P, verifikator menghitung U = Z/S dan V = R/S, kemudian memeriksa apakah koordinat x dari UG + VP sama dengan R. Hal ini berhasil karena aljabar verifikasi merekonstruksi KG tanpa membutuhkan kunci privat. Memalsukan tanda tangan akan membutuhkan pemecahan masalah log diskrit atau memecahkan fungsi hash.


#### Tanda Tangan Schnorr dan Konteks Sejarah


Tanda tangan Schnorr secara matematis lebih bersih dan mendukung fitur agregasi, tetapi dipatenkan ketika Bitcoin diluncurkan. ECDSA menawarkan alternatif gratis, meskipun dengan kompleksitas yang lebih tinggi dan tanda tangan yang lebih besar. Dengan berakhirnya masa paten, Bitcoin menambahkan tanda tangan Schnorr melalui Taproot, menyediakan tanda tangan 64-byte yang tetap dan privasi yang lebih baik. ECDSA tetap didukung untuk kompatibilitas lama.



### Struktur Transaksi dan Input/Output


Transaksi Bitcoin terdiri dari:


- versi (4 byte, ujung kecil)
- daftar masukan
- daftar keluaran
- waktu penguncian (4 byte)


Input mereferensikan [UTXO](https://planb.academy/resources/glossary/utxo) sebelumnya berdasarkan hash transaksi dan indeks output, dan termasuk [skrip](https://planb.academy/resources/glossary/script) pembuka kunci (scriptSig) dan nomor urut yang digunakan untuk penguncian waktu atau RBF. Keluaran menentukan jumlah (8 byte) dan skrip penguncian (scriptPubKey), yang menentukan kondisi pengeluaran. Alamat Bitcoin adalah representasi dari skrip ini.


#### Model UTXO

Bitcoin melacak output yang belum dibelanjakan, bukan saldo akun. UTXO harus dibelanjakan seluruhnya - pembelanjaan sebagian tidak mungkin dilakukan. Untuk membelanjakan 1 BTC dari 100 BTC UTXO, sebuah transaksi harus menyertakan hasil perubahan. Melupakan output perubahan akan mengubah sisanya menjadi biaya penambang.


#### Serialisasi dan Penguraian Transaksi


Transaksi menggunakan format biner yang ringkas. Setelah bidang versi, sebuah varint mengkodekan jumlah input. Masukan meliputi:


- hash tx sebelumnya (32 byte)
- indeks keluaran (4 byte)
- scriptSig (varstr)
- urutan (4 byte)


Keluaran termasuk jumlah 8-byte dan scriptPubKey (varstr). Waktu penguncian mengontrol kapan transaksi menjadi valid. Serialisasi menggunakan pengurutan ujung kecil untuk sebagian besar bilangan bulat. Pengurai mengkonsumsi byte secara berurutan dan mendelegasikan ke kelas khusus untuk input, output, dan skrip.


### Biaya, Perubahan, dan Kelenturan


Biaya bersifat implisit:

biaya = jumlah (nilai input) - jumlah (nilai output).

Setiap nilai yang tidak ditetapkan menjadi biaya, membuat konstruksi keluaran perubahan yang benar menjadi penting. Sebelum [SegWit](https://planb.academy/resources/glossary/segwit), tanda tangan memungkinkan perubahan S menjadi N-S menghasilkan transaksi baru yang valid dengan ID yang berbeda. Bitcoin sekarang memberlakukan aturan S rendah, dan SegWit mengisolasi tanda tangan dari perhitungan txid, membuat ID stabil dan memungkinkan protokol lapisan kedua seperti [Lightning](https://planb.academy/resources/glossary/lightning-network).


## Bitcoin Skrip dan Validasi Transaksi

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>


![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


Bitcoin Script adalah bahasa kontrak pintar kecil berbasis stack yang mendefinisikan bagaimana koin dapat dibelanjakan. Setiap output membawa scriptPubKey (skrip pengunci) dan setiap input membawa scriptSig (skrip pembuka). Bersama-sama mereka membentuk sebuah program yang harus mengevaluasi "benar" agar pembelanjaan menjadi valid. Script sengaja tidak dibuat Turing-complete agar semua jalur eksekusi dapat diprediksi dan mudah divalidasi di seluruh jaringan.


### Operasi Skrip dan Model Eksekusi


Skrip adalah urutan elemen data dan opcode. Data push (tanda tangan, kunci publik, hash) ditempatkan pada stack, sementara opcode yang dimulai dengan `OP_` mengubah stack. Setelah dieksekusi, elemen tumpukan paling atas harus bukan nol agar berhasil. Contoh: `OP_DUP` menduplikasi elemen teratas, `OP_HASH160` menerapkan SHA256 kemudian RIPEMD160, dan `OP_CHECKSIG` memverifikasi tanda tangan terhadap sighash transaksi dan kunci publik, dengan memberikan nilai 1 untuk valid, 0 untuk tidak valid. Aturan penguraian membedakan antara data mentah (diawali dengan panjang) dan opcode (dicari berdasarkan nilai byte), dan mesin virtual kecil mengeksekusinya secara deterministik pada setiap [node](https://planb.academy/resources/glossary/node).


### P2PK dan P2PKH: Pola Pembayaran Inti


Pola yang paling awal, Pay-to-Public-Key (P2PK), mengunci koin secara langsung ke public key secara penuh: scriptPubKey adalah `<pubkey> OP_CHECKSIG`, dan scriptSig hanyalah sebuah tanda tangan. Pola ini sederhana namun tidak efisien dalam penggunaan ruang dan membuka kunci publik sebelum koin dibelanjakan.


#### P2PKH dan Alamat

Pay-to-Public-Key-Hash (P2PKH) memperbaiki hal ini dengan mengunci ke hash 20-byte dari kunci publik. ScriptPubKey adalah `OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG`, dan scriptSig menyediakan `<signature> <pubkey>`. Eksekusi memeriksa apakah kunci publik yang disediakan memiliki hash dengan nilai yang dikomitmenkan dan kemudian memverifikasi tanda tangan. Hal ini menyembunyikan kunci publik sampai menghabiskan waktu, mengurangi ukuran, dan mencocokkan format alamat "1..." Format alamat mainnet.


### Validasi Transaksi dan Hashing Tanda Tangan


Sebuah simpul yang memvalidasi sebuah transaksi harus memastikan:

1) Setiap input merujuk pada output yang sudah ada dan tidak digunakan.

2) Total nilai input ≥ total nilai output (selisihnya adalah biaya).

3) Setiap scriptSig dengan benar membuka scriptPubKey yang direferensikan.


Verifikasi tanda tangan membutuhkan pembuatan pesan yang sama persis dengan pesan yang ditandatangani, yang disebut sighash. Untuk ECDSA lama, validasi mengosongkan semua scriptSig, mengganti scriptSig input saat ini dengan scriptPubKey yang sesuai, menambahkan tipe hash 4-byte (biasanya `SIGHASH_ALL`), dan melakukan hash ganda pada hasilnya. Nilai 256-bit itulah yang digunakan oleh `OP_CHECKSIG`. Jenis hash alternatif (misalnya, `SINGLE`, `NONE`, dengan atau tanpa `ANYONECANPAY`) mengubah bagian mana dari transaksi yang dikomitmenkan, sehingga memungkinkan kasus penggunaan khusus seperti pendanaan kolaboratif atau transaksi yang ditentukan secara parsial, tetapi jarang digunakan dalam praktiknya.


#### Hashing Kuadratik dan SegWit

Karena setiap input dalam transaksi lama membutuhkan komputasi sighash sendiri atas struktur yang mencakup semua input, waktu validasi dapat bertambah secara kuadratik dengan jumlah input. Transaksi multi-input yang besar pernah menyebabkan penundaan validasi yang nyata. SegWit mendesain ulang perhitungan sighash untuk menyimpan bagian yang digunakan bersama dan mengurangi kompleksitas menjadi waktu linier, meningkatkan skalabilitas dan membuat serangan penolakan layanan menjadi lebih sulit.


### Teka-teki Naskah dan Pelajaran Keamanan


Script dapat mengekspresikan lebih dari sekadar "satu tanda tangan membuka koin-koin ini." Teka-teki skrip mendemonstrasikan hal ini dengan mengkodekan kondisi yang berubah-ubah - masalah matematika, tantangan hash preimage, atau bahkan collision bounty - dimana siapa saja yang memberikan data yang benar dapat membelanjakan koin. Akan tetapi, keluaran yang hanya mengandalkan data publik (tanpa tanda tangan) rentan terhadap [penambang](https://planb.academy/resources/glossary/miner) yang sedang berjalan di depan: setelah solusi yang valid muncul di [mempool](https://planb.academy/resources/glossary/mempool), penambang manapun dapat menyalinnya dan mengarahkan pembayaran untuk mereka sendiri.


Pelajaran praktisnya adalah bahwa kontrak di dunia nyata hampir selalu menyertakan pemeriksaan tanda tangan, bahkan ketika kontrak tersebut mengandung logika yang lebih kompleks seperti multisig, timelock, atau hashlock. Tanda tangan mengikat solusi kepada pihak tertentu, menjaga insentif dan mencegah pihak lain mencuri pembayaran. Memahami model tumpukan Script, pola standar, dan jebakan halus sangat penting untuk merancang kontrak pintar Bitcoin yang aman dan untuk penalaran tentang bagaimana transaksi sebenarnya divalidasi di jaringan.


## Konstruksi Transaksi dan Bayar-ke-Naskah Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>


![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


### Membangun Transaksi Bitcoin dan P2SH


Konstruksi transaksi Bitcoin menjembatani pengetahuan protokol teoretis dengan implementasi praktis. Sebuah transaksi memilih UTXO untuk dibelanjakan, membangun output dengan skrip penguncian, membuat tanda tangan untuk setiap input, dan menserialisasikan semuanya dalam format yang tepat yang diharapkan node. Proses ini membutuhkan pemahaman tentang pembuatan sighash, perilaku Skrip, dan penanganan biaya dan perubahan yang benar.


### Konstruksi Transaksi Dasar


Setiap input transaksi mengacu pada output sebelumnya dengan txid dan indeks. Output menentukan jumlah dalam satoshi dan skrip penguncian. Perbedaan antara total input dan total output adalah biaya. Untuk menandatangani sebuah input, versi modifikasi dari transaksi diserialisasikan, sighash-nya dihitung, dan private key menandatanganinya. Tanda tangan yang dihasilkan dan kunci publik membentuk ScriptSig. Setelah setiap input ditandatangani, transaksi mentah dapat disiarkan ke jaringan.


### Transaksi dengan banyak tanda tangan


Multisig telanjang menggunakan `OP_CHECKMULTISIG` untuk membutuhkan tanda tangan m-of-n. Karena adanya bug off-by-one di awal, OP_CHECKMULTISIG menggunakan elemen tumpukan tambahan, yang membutuhkan `OP_0` di ScriptSig. Bare multisig berfungsi tetapi tidak efisien: semua kunci publik muncul on-chain, membuat scriptPubKeys menjadi besar, mahal, dan sulit untuk dikodekan sebagai alamat. Keterbatasan ini memotivasi pengenalan pay-to-script-hash.


#### Arsitektur P2SH

P2SH menyembunyikan skrip yang kompleks di balik HASH160 20-byte. ScriptPubKey ditetapkan: `OP_HASH160 <20-byte hash> OP_EQUAL`. Skrip penukaran yang mendasari - yang berisi multisig, penguncian waktu, atau kondisi lainnya - hanya terungkap dan dieksekusi saat pengeluaran. Pengirim hanya melihat hash, sementara penerima mengelola skrip penukaran secara pribadi. Desain ini mengurangi ukuran on-chain, meningkatkan privasi, dan memungkinkan kontrak yang kompleks tanpa membebani pengirim.


### Pengeluaran dan Implementasi P2SH


Untuk mengeluarkan output P2SH, ScriptSig harus menyertakan data pembuka kunci yang diperlukan * plus* skrip penukaran itu sendiri. Validasi terjadi dalam dua langkah:

1) HASH160(redeem_script) harus cocok dengan hash scriptPubKey.

2) Setelah verifikasi, skrip penukaran dieksekusi dengan data yang disediakan.


Ketika membuat tanda tangan untuk input P2SH, proses sighash menggunakan skrip penukaran sebagai pengganti scriptPubKey. Setiap penandatangan harus memiliki skrip penukaran penuh ke tanda tangan valid generate. Alamat P2SH menggunakan versi byte 0x05 pada mainnet (alamat "3...") dan 0xC4 pada testnet (alamat "2...").


#### Pertimbangan Keamanan Praktis


Kehilangan skrip penukaran berarti kehilangan dana: pengeluaran membutuhkan kunci privat dan skrip penukaran itu sendiri. Peserta Multisig harus memverifikasi bahwa public key mereka telah disertakan dengan benar sebelum menerima setoran. P2SH mendukung konstruksi tingkat lanjut seperti multisig, timelock, dan hashlock, tetapi kesalahan dalam logika skrip dapat mengunci dana secara permanen, sehingga pengujian pada testnet sangat penting.


P2SH meningkatkan privasi dengan menyembunyikan kondisi pembelanjaan hingga pembelanjaan pertama, tetapi setelah skrip penukaran muncul on-chain, skrip tersebut akan terlihat secara permanen. Meskipun demikian, manfaat dari ukuran yang lebih kecil, kompatibilitas ke belakang, dan dukungan kontrak yang fleksibel menjadikan P2SH sebagai tonggak utama, yang memengaruhi peningkatan selanjutnya seperti SegWit dan Taproot.


# Cara Kerja Jaringan Bitcoin Bagian Dalam

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Blok Bitcoin dan Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>


![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


Bitcoin memblokir transaksi kelompok dan mengamankannya menggunakan [proof of work](https://planb.academy/resources/glossary/proof-of-work). Setiap [blok](https://planb.academy/resources/glossary/block) mencakup [header](https://planb.academy/resources/glossary/block-header) 80-byte ditambah daftar transaksi. Meskipun biaya energi yang besar untuk memproduksi sebuah blok yang valid, memverifikasi blok tersebut tidaklah mahal: menyimpan semua ~900 ribu header hanya membutuhkan ~72 MB, sehingga memungkinkan perangkat yang kecil sekalipun untuk memverifikasi proof of work rantai secara efisien.


### Transaksi Coinbase dan Hadiah Blokir


Setiap blok dimulai dengan tepat satu [transaksi Coinbase](https://planb.academy/resources/glossary/coinbase-transaction) - satu-satunya cara bitcoin baru memasuki sirkulasi. Ia memiliki hash prev-tx nol dan indeks 0xffffffffff, yang secara unik mengidentifikasinya. Subsidi dimulai dari 50 BTC dan dibagi dua setiap 210.000 blok (50, 25, 12,5, 6,25, 3,125,...). Penambang juga memasukkan biaya transaksi. Karena nonce 4-byte terlalu kecil untuk ASIC modern, penambang memodifikasi data dalam transaksi Coinbase untuk mengubah root [Merkle](https://planb.academy/resources/glossary/merkle-tree) dan membuat ruang pencarian tambahan. [BIP](https://planb.academy/resources/glossary/bip)34 membutuhkan penyematan tinggi blok dalam skrip CoinbaseSig untuk memastikan setiap Coinbase txid unik.


### Bidang Header Blok dan Pensinyalan Soft Fork


Header 80-byte berisi:


- versi (4 byte)
- hash blok sebelumnya (32 byte)
- Akar Merkle (32 byte)
- cap waktu (4 byte)
- bit (target [tingkat kesulitan](https://planb.academy/resources/glossary/difficulty), 4 byte)
- nonce (4 byte)


Nomor versi berevolusi menjadi sistem pensinyalan bit-field melalui BIP9, yang memungkinkan para penambang untuk mengoordinasikan kesiapan [soft-fork](https://planb.academy/resources/glossary/soft-fork). Stempel waktu adalah nilai waktu Unix 32-bit dan perlu diperbarui sekitar tahun 2106.


#### Bidang Bit dan Target

Bidang bit mengkodekan target dalam bentuk ringkas: target = koefisien × 256^(eksponen-3). Hash blok yang valid harus secara numerik berada di bawah target ini. Karena hash ditafsirkan sebagai bilangan bulat dengan ujung kecil, hash yang valid sering kali muncul dengan banyak angka nol di belakangnya saat ditampilkan dalam heksa.


### Kesulitan, Validasi, dan Penyesuaian


Tingkat kesulitan didefinisikan sebagai lowest_target / current_target, yang menyatakan seberapa sulitnya mining saat ini dibandingkan dengan tingkat kesulitan yang paling mudah. Validasi hanya perlu membandingkan hash dari header dengan target-sangat murah dibandingkan dengan mining.


Setiap blok 2016, Bitcoin menyesuaikan tingkat kesulitan untuk menargetkan interval blok ~10 menit. Penyesuaian ini membandingkan waktu aktual untuk blok 2016 sebelumnya dengan dua minggu yang diharapkan. Batasan membatasi penyesuaian hingga dalam faktor empat. Peristiwa besar di dunia nyata - seperti larangan mining di Tiongkok - menunjukkan ketahanan mekanisme ini ketika tingkat hash turun tajam dan tingkat kesulitan disesuaikan ke bawah untuk mengimbanginya.


### Subsidi Blok dan Total Supply


Subsidi pada ketinggian h dihitung sebagai: subsidi = 5_000_000_000 >> (h // 210_000). Hal ini menghasilkan jadwal pembagian dua yang konvergen menuju total pasokan ~21 juta BTC. Penjumlahan deret geometris (50 + 25 + 12,5 + ...) × 210.000 menjelaskan batasannya. Penambang dapat mengklaim kurang dari subsidi yang diizinkan tetapi tidak boleh lebih, atau blok menjadi tidak valid. Ketika subsidi menyusut selama halving yang berurutan, biaya transaksi menjadi komponen yang semakin penting untuk pendapatan penambang dan keamanan jaringan jangka panjang.


## Komunikasi Jaringan dan Pohon Merkle

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>


![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


### Arsitektur Jaringan Bitcoin


Jaringan [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p) Bitcoin beroperasi sebagai sistem gosip terdesentralisasi di mana node menyampaikan transaksi dan blok tanpa mempercayai satu sama lain. Node baru melakukan bootstrap dengan menghubungi seed DNS yang sudah dikodekan yang dikelola oleh pengembang inti. Seed DNS ini mengembalikan IP dari peers yang aktif, memungkinkan node untuk menemukan jaringan dan kemudian meminta peers tambahan melalui getaddr. Jaringan sengaja tidak bersifat [konsensus](https://planb.academy/resources/glossary/consensus)-kritis, sehingga implementasinya dapat berbeda selama aturan konsensus tidak berubah.


### Struktur Pesan dan Jabat Tangan


Semua pesan Bitcoin P2P menggunakan amplop tetap: nilai ajaib 4-byte (F9BEB4D9 untuk mainnet), perintah ASCII 12-byte, panjang payload little-endian 4-byte, checksum 4-byte (4-byte pertama [hash](https://planb.academy/resources/glossary/hash-function)256), dan payload. Perintah yang umum termasuk versi, verack, inv, getdata, tx, block, getheader, header, ping, dan pong.


Jabat tangan dimulai ketika simpul penghubung mengirim pesan versi. Penerima membalas dengan verack dan versinya sendiri. Setelah kedua belah pihak bertukar kedua pesan ini, koneksi aktif dan node dapat mulai menyampaikan inventaris dan data.


### Pohon Merkle dan Akar Merkle


Bitcoin menyimpan satu akar Merkle 32-byte di setiap header blok sebagai komitmen untuk semua transaksi dalam blok. Transaksi di-hash (hash256), dipasangkan, digabungkan, dan di-hash berulang kali sampai tersisa satu hash. Ketika sebuah level memiliki jumlah ganjil, hash terakhir akan diduplikasi. Secara internal, hash adalah big-endian, sedangkan data blok serial menggunakan little-endian, yang membutuhkan pembalikan sebelum dan sesudah konstruksi pohon.


#### Bukti Merkle dan SPV

Bukti Merkle memungkinkan untuk memverifikasi bahwa sebuah transaksi termasuk dalam sebuah blok tanpa mengunduh seluruh blok. Bukti ini terdiri dari hash saudara di sepanjang jalur menuju root. Klien SPV yang ringan hanya menyimpan header blok dan meminta bukti-bukti ini dari [seluruh node](https://planb.academy/resources/glossary/full-node). Karena pohon Merkle tumbuh secara logaritmik, pembuktian penyertaan dalam sebuah blok dengan ribuan transaksi hanya membutuhkan beberapa ratus byte.


Taproot memperluas konsep ini dengan melakukan kondisi pengeluaran ke pohon skrip Merklized (MAST), yang hanya mengungkapkan cabang yang dieksekusi bersama dengan bukti Merkle. Hal ini meningkatkan efisiensi dan privasi.


### Operasi Jaringan dan Sinkronisasi Blok


Node menggunakan getdata untuk meminta transaksi atau blok, dengan menentukan ID jenis (1 = tx, 2 = blok, 3 = blok yang disaring, 4 = blok ringkas) ditambah dengan pengenal 32-byte. Untuk sinkronisasi rantai, node mengirim header dengan hash blok awal, menerima hingga 2000 header sebagai tanggapan. Setiap header yang dikembalikan terdiri dari 80 byte yang diikuti dengan jumlah transaksi dummy nol.


Verifikasi penuh atas blok yang diterima membutuhkan dua kali pemeriksaan:

1. Hash blok harus berada di bawah target yang dikodekan dalam bidang bit.

2. Akar Merkle yang dihitung dari semua transaksi (dengan penanganan endianness yang tepat) harus sesuai dengan akar header.


Hanya jika kedua kondisi tersebut berhasil, sebuah node akan menerima blok tersebut, yang mencerminkan prinsip "jangan percaya, verifikasi" dari Bitcoin.


## Komunikasi Simpul Tingkat Lanjut dan Saksi Terpisah

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>


![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


Sesi ini menyatukan jaringan P2P tingkat lanjut dengan Segregated Witness, menunjukkan bagaimana perangkat lunak Bitcoin modern berinteraksi langsung dengan node saat menggunakan struktur transaksi SegWit-aware. Para pengembang belajar untuk mengambil blok, memindai transaksi yang relevan, dan membangun transaksi hanya dengan menggunakan komunikasi jaringan mentah - tidak perlu penjelajah blok.


### Pengambilan Transaksi Berbasis Blok dan Privasi


[Dompet](https://planb.academy/resources/glossary/wallet) harus mendeteksi pembayaran yang masuk dengan memindai blok untuk mencari output yang sesuai dengan scriptPubKey mereka. Mengambil seluruh blok akan melindungi privasi dengan lebih baik dibandingkan dengan meminta transaksi individu, yang membocorkan sinyal kuat mengenai aktivitas pengguna. Bahkan permintaan blok dapat membocorkan informasi pada rantai bervolume rendah, membuat filter blok ringkas (BIP158) sangat penting untuk klien ringan yang menjaga privasi. Filter dapat menghasilkan positif palsu tetapi tidak pernah negatif palsu, memungkinkan klien untuk mengunduh hanya blok yang berpotensi relevan tanpa mengungkapkan alamat tertentu.


### Trustless Interaksi Jaringan


Alur kerja `get_block` menunjukkan penggunaan jaringan yang benar: kirim getdata, terima blok, lalu verifikasi akar Merkle dan proof of work secara independen. Sebuah blok diterima hanya jika hash header yang diterima sesuai dengan hash yang diminta dan akar Merkle yang dihitung sesuai dengan header. Ini mewujudkan "jangan percaya, verifikasi," untuk memastikan bahwa rekan yang jahat sekalipun tidak dapat mengelabui node untuk menerima data yang telah diubah.


#### Mengambil Transaksi dari Blok

Transaksi sebuah blok dapat dipindai untuk mencocokkan scriptPubKeys dengan menggunakan iterasi sederhana. Dompet produksi melakukan hal ini secara terus menerus ketika blok baru tiba, membuktikan kepemilikan output secara ketat melalui validasi kriptografi daripada mengandalkan API pihak ketiga.


### Tujuan dan Desain SegWit


Segregated Witness (SegWit) memperbaiki kelenturan transaksi dengan menghapus data tanda tangan dari perhitungan txid. Hal ini memungkinkan rantai transaksi yang telah ditandatangani sebelumnya dapat diandalkan dan membuat Lightning Network menjadi praktis. SegWit juga meningkatkan kapasitas blok dengan menggunakan "bobot blok": node lama masih melihat blok ≤1 MB, sementara node yang ditingkatkan memvalidasi hingga 4 MB termasuk data saksi. Program saksi berversi (sejauh ini v0-v1) membuat jalur peningkatan terstruktur untuk jenis skrip di masa depan.


#### P2WPKH (SegWit asli)


P2WPKH menggantikan struktur P2PKH yang lama dengan skrip 22-byte: OP_0 + push20 + hash160 (pubkey). Pengeluaran memindahkan tanda tangan dan pubkey ke dalam bidang saksi yang terpisah.


- Node pra-SegWit: lihat "siapa pun-dapat-membelanjakan," anggap sebagai valid.
- Node pasca-SegWit: kenali hash OP_0 + 20-byte dan validasi menggunakan data saksi.


Pemisahan ini memperbaiki kelenturan dan mengurangi biaya. Saksi menggunakan hitungan varint yang diikuti dengan tanda tangan dan pubkey.


#### P2SH-P2WPKH (SegWit yang Kompatibel dengan SegWit)


Untuk memungkinkan dompet lama mengirim ke alamat SegWit, skrip P2WPKH dapat dibungkus dengan P2SH.


- scriptPubKey: standar P2SH hash160 (redeemScript)
- scriptSig: script penukaran (program P2WPKH)
- saksi: tanda tangan + pubkey


Lapisan validasi:

1. Node pra-BIP16 menerima redeemScript sebagai valid.

2. Node pasca-BIP16 mengevaluasinya, meninggalkan OP_0 + hash pada tumpukan.

3. Node SegWit melakukan validasi saksi penuh.


#### P2WSH untuk Skrip Kompleks


P2WSH menggeneralisasi SegWit untuk multisig dan skrip tingkat lanjut dengan melakukan komitmen ke SHA256 (skrip), bukan hash160. Tumpukan saksi multisig 2-dari-3 yang khas:


- elemen kosong (bug CHECKMULTISIG)
- sig1
- sig2
- skrip saksi (skrip multisig)


Node SegWit memverifikasi SHA256 (witnessScript) yang cocok dengan hash scriptPubKey dan kemudian mengeksekusinya. Menggunakan SHA256 dan hash 32-byte memungkinkan untuk membedakan P2WSH dari P2WPKH dan memperkuat keamanan.


#### P2SH-P2WSH (Kompatibilitas Maksimum)


Skrip SegWit yang kompleks juga dapat dibungkus dengan P2SH:


- scriptSig: menukarkan Script (OP_0 + hash 32-byte)
- saksi: tanda tangan + naskah saksi


Validasi melewati tiga generasi aturan persis seperti pada P2SH-P2WPKH. Pembungkus ini sangat penting untuk penerapan Lightning awal yang membutuhkan multisig tanpa kelenturan. Meskipun P2WSH asli lebih disukai saat ini, bentuk yang dibungkus memastikan kompatibilitas di seluruh sistem wallet yang lebih tua.


### Dampak SegWit


SegWit disediakan:


- iD transaksi yang stabil
- biaya yang lebih rendah melalui diskon data saksi
- throughput blok yang lebih tinggi melalui bobot blok
- kompatibilitas untuk node lama
- jalur peningkatan yang bersih untuk Taproot dan ekstensi di masa mendatang


Bersama dengan interaksi jaringan yang tidak dapat dipercaya, alat-alat ini membentuk tulang punggung pengembangan Bitcoin modern.



# Bagian Akhir


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Ulasan & Peringkat


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Ujian Akhir


<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>



<isCourseExam>true</isCourseExam>

## Kesimpulan



<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>


<isCourseConclusion>true</isCourseConclusion>