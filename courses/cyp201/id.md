---
name: Pengantar Kriptografi Bitcoin
goal: Memahami pembuatan dompet Bitcoin dari perspektif kriptografi
objectives:
  - Membuka misteri terminologi kriptografi terkait Bitcoin.
  - Menguasai pembuatan dompet Bitcoin.
  - Memahami struktur dompet Bitcoin.
  - Memahami alamat dan jalur derivasi.
---

# Sebuah Perjalanan ke dalam Kriptografi

Apakah Anda terpesona oleh Bitcoin? Bertanya-tanya bagaimana dompet Bitcoin bekerja? Bersiaplah untuk memulai perjalanan menarik ke dalam kriptografi! Loïc, ahli kami, akan memandu Anda melalui kerumitan pembuatan dompet Bitcoin, mengungkap misteri di balik istilah teknis yang menakutkan seperti hashing, derivasi kunci, dan kurva eliptik.

Pelatihan ini tidak hanya akan membekali Anda dengan pengetahuan untuk memahami struktur dompet Bitcoin, tetapi juga mempersiapkan Anda untuk menyelami dunia kriptografi yang menarik. Jadi, apakah Anda siap untuk memulai perjalanan ini? Bergabunglah dengan kami dan ubah rasa ingin tahu Anda menjadi keahlian!

+++

# Pengantar

<partId>32960669-d13a-592f-a053-37f70b997cbf</partId>

## Pengantar ke Kriptografi

<chapterId>fb4e8857-ea35-5a8a-ae8a-5300234e0104</chapterId>

### Apakah pelatihan ini untuk Anda? YA!

Kami sangat senang menyambut Anda ke kursus pelatihan baru berjudul "Crypto 301: Pengantar ke Kriptografi dan Dompet HD", yang dipimpin oleh ahli di bidangnya, Loïc Morel. Kursus ini akan membenamkan Anda ke dalam dunia kriptografi yang menarik, disiplin ilmu matematika fundamental yang memastikan enkripsi dan keamanan data Anda.

Dalam kehidupan sehari-hari, dan khususnya dalam dunia Bitcoin, kriptografi memainkan peran penting. Konsep-konsep terkait kriptografi, seperti kunci privat, kunci publik, alamat, jalur derivasi, seed, dan entropi, adalah inti dari penggunaan dan pembuatan dompet Bitcoin. Sepanjang kursus ini, Loïc akan menjelaskan secara detail bagaimana kunci privat dihasilkan dan bagaimana mereka terhubung ke alamat. Loïc juga akan menghabiskan satu jam untuk menjelaskan detail matematis dari kurva eliptik. Selain itu, Anda akan memahami mengapa penggunaan HMAC SHA512 penting untuk mengamankan dompet Anda dan apa perbedaan antara seed dan frasa mnemonik.
Tujuan utama dari pelatihan ini adalah untuk memungkinkan Anda memahami proses teknis yang terlibat dalam pembuatan dompet HD dan metode kriptografi yang digunakan. Selama bertahun-tahun, dompet Bitcoin telah berkembang menjadi lebih mudah digunakan, lebih aman, dan distandarisasi berkat BIP tertentu. Loïc akan membantu Anda memahami BIP ini untuk memahami pilihan yang dibuat oleh pengembang Bitcoin dan kriptografer. Seperti semua pelatihan yang ditawarkan oleh universitas kami, kursus ini sepenuhnya gratis dan open source. Ini berarti Anda bebas mengikutinya dan menggunakannya sesuai keinginan Anda. Kami menantikan umpan balik Anda di akhir kursus menarik ini.

### Panggung milik Anda, profesor!

Halo semua, saya Loïc Morel, pemandu Anda melalui eksplorasi teknis kriptografi yang digunakan dalam dompet Bitcoin.

Perjalanan kita dimulai dengan menyelami kedalaman fungsi hash kriptografi. Bersama-sama, kita akan membedah cara kerja SHA256 yang esensial dan menjelajahi berbagai algoritma yang didedikasikan untuk derivasi.

Kita akan melanjutkan petualangan kita dengan menguraikan dunia misterius tanda tangan digital. Anda akan menemukan bagaimana keajaiban kurva eliptik diterapkan pada tanda tangan ini, dan kita akan menerangi cara menghitung kunci publik dari kunci privat. Dan tentu saja, kita akan menyelami proses tanda tangan digital.
Selanjutnya, kita akan kembali ke masa lalu untuk melihat evolusi dompet Bitcoin, dan kita akan menjelajahi konsep entropi dan angka acak. Kita akan mengulas frase mnemonik terkenal, sambil juga menyentuh passphrase. Anda bahkan akan memiliki kesempatan untuk mengalami sesuatu yang unik dengan membuat seed dari 128 lemparan dadu!
Dengan dasar yang kokoh ini, kita akan siap untuk bagian yang paling krusial: membuat dompet Bitcoin. Mulai dari kelahiran seed dan master key, hingga studi tentang kunci ekstensi, dan derivasi pasangan kunci anak, setiap langkah akan diuraikan. Kita juga akan membahas struktur dompet dan jalur derivasi.

Untuk mengakhiri semuanya, kita akan menyimpulkan perjalanan kita dengan meneliti alamat Bitcoin. Kita akan menjelaskan bagaimana mereka dibuat dan bagaimana mereka memainkan peran penting dalam fungsi dompet Bitcoin.

Bergabunglah dengan saya dalam perjalanan menarik ini, dan bersiaplah untuk menjelajahi dunia kriptografi seperti sebelumnya. Tinggalkan prasangka Anda di pintu dan bukalah pikiran Anda untuk cara baru memahami Bitcoin dan struktur fundamentalnya.

# Fungsi Hash

<partId>3713fee1-2ec2-512e-9e97-b6da9e4d2f17</partId>

## Pengantar fungsi hash kriptografi terkait dengan Bitcoin

<chapterId>dba011f5-1805-5a48-ac2b-4bd637c93703</chapterId>

Selamat datang di sesi hari ini yang didedikasikan untuk penyelaman mendalam ke dalam dunia kriptografi fungsi hash, sebuah batu penjuru penting dari keamanan protokol Bitcoin. Bayangkan sebuah fungsi hash sebagai robot dekripsi kriptografi yang ultra-efisien yang mengubah informasi berukuran apa pun menjadi sidik jari digital unik dan berukuran tetap, yang disebut "hash," "digest," atau "checksum."
Secara ringkas, fungsi hash mengambil pesan masukan berukuran sembarang dan mengubahnya menjadi sidik jari keluaran berukuran tetap.

Mendeskripsikan profil fungsi hash kriptografi memerlukan pemahaman dua kualitas esensial: irreversibilitas mereka dan resistensi mereka terhadap pemalsuan.

Irreversibilitas, atau resistensi terhadap preimage, berarti bahwa menghitung keluaran dari masukan dapat dilakukan dengan mudah, tetapi menghitung masukan dari keluaran adalah mustahil.
Ini adalah fungsi satu arah.

![image](assets/image/section1/0.webp)

Resistensi terhadap pemalsuan berasal dari fakta bahwa bahkan modifikasi terkecil dari masukan akan menghasilkan keluaran yang sangat berbeda.
Fungsi ini memungkinkan untuk memverifikasi integritas perangkat lunak yang diunduh.

![image](assets/image/section1/1.webp)

Karakteristik penting lainnya yang mereka miliki adalah resistensi mereka terhadap tabrakan dan preimage kedua. Tabrakan terjadi ketika dua masukan berbeda menghasilkan keluaran yang sama.
Tentu saja, dalam alam semesta hashing, tabrakan tidak terelakkan, tetapi fungsi hash kriptografi yang baik meminimalkannya secara signifikan. Risikonya harus sangat rendah sehingga dapat dianggap tidak signifikan. Ini seperti setiap hash adalah sebuah rumah di kota yang luas; meskipun jumlah rumah sangat banyak, fungsi hash yang baik memastikan bahwa setiap rumah memiliki alamat unik.

Resistensi terhadap preimage kedua bergantung pada resistensi terhadap tabrakan; jika ada resistensi terhadap tabrakan, maka ada resistensi terhadap preimage kedua.
Diberikan sebuah informasi masukan yang dipaksakan pada kita, kita harus menemukan masukan kedua, berbeda dari yang pertama, yang menghasilkan tabrakan dalam keluaran hash dari fungsi tersebut. Resistensi terhadap preimage kedua mirip dengan resistensi terhadap tabrakan, kecuali bahwa masukannya dipaksakan.
Mari kita sekarang menavigasi perairan bergelombang dari fungsi hash yang sudah usang. SHA0, SHA1, dan MD5 kini dianggap sebagai cangkang berkarat di lautan hashing kriptografi. Mereka seringkali tidak disarankan karena telah kehilangan resistensi mereka terhadap tabrakan. Prinsip pigeonhole menjelaskan mengapa, meskipun upaya terbaik kita, penghindaran tabrakan adalah mustahil karena keterbatasan ukuran output. Untuk benar-benar dianggap aman, sebuah fungsi hash harus resisten terhadap tabrakan, preimages kedua, dan preimages.

Elemen kunci dalam protokol Bitcoin, fungsi hash SHA-256 adalah kapten dari kapal. Fungsi lain, seperti SHA-512, digunakan untuk derivasi dengan HMAC dan PBKDF. Selain itu, RIPMD160 digunakan untuk mengurangi sidik jari menjadi 160 bit. Ketika kita merujuk ke HASH256 dan HASH160, kita merujuk pada penggunaan double hashing dengan SHA-256 dan RIPMD.

Untuk HASH256, ini adalah double hash dari pesan menggunakan fungsi SHA256.

$$
SHA256(SHA256(pesan))
$$

Untuk HASH160, ini adalah double hash dari pesan menggunakan SHA256 terlebih dahulu, kemudian RIPMD160.

$$
RIPMD160(SHA256(pesan))
$$

Penggunaan HASH160 sangat menguntungkan karena memungkinkan keamanan SHA-256 sambil mengurangi ukuran sidik jari.

Secara keseluruhan, tujuan utama dari fungsi hash kriptografi adalah untuk mengubah informasi berukuran sembarang menjadi sidik jari berukuran tetap. Untuk diakui sebagai aman, itu harus memiliki beberapa kekuatan: tidak dapat dibalikkan, resistensi terhadap perubahan, resistensi terhadap tabrakan, dan resistensi terhadap preimages kedua.

![image](assets/image/section1/2.webp)

Di akhir eksplorasi ini, kita telah mengungkap fungsi hash kriptografi, menyoroti penggunaannya dalam protokol Bitcoin, dan membedah tujuan spesifik mereka. Kita telah belajar bahwa agar fungsi hash dianggap aman, mereka harus resisten terhadap preimages, preimages kedua, tabrakan, dan perubahan. Kita juga telah membahas berbagai fungsi hash yang digunakan dalam protokol Bitcoin. Dalam sesi berikutnya, kita akan menyelami inti dari fungsi hash SHA256 dan menemukan matematika menarik yang memberikannya karakteristik unik.

## Cara Kerja SHA256

<chapterId>905eb320-f15b-5fb6-8d2d-5bb447337deb</chapterId>

Selamat datang di kelanjutan perjalanan menarik kita melalui labirin kriptografi dari fungsi hash. Hari ini, kita akan mengungkap misteri SHA256, sebuah proses yang kompleks namun cerdik yang telah kita perkenalkan sebelumnya.

Sebagai pengingat, tujuan dari fungsi hash SHA256 adalah untuk mengambil pesan input berukuran apa pun dan menghasilkan hash 256-bit sebagai output.

### Pra-pemrosesan

Mari kita melangkah lebih jauh dalam labirin ini dengan memulai pra-pemrosesan SHA256.

#### Padding Bits

Tujuan dari langkah pertama ini adalah untuk memiliki pesan yang disamakan menjadi kelipatan dari 512 bit. Untuk mencapai ini, kita akan menambahkan bit padding ke pesan.

Misalkan M adalah ukuran pesan awal.
Misalkan 1 adalah bit yang disediakan untuk pemisah.
Misalkan P adalah jumlah bit yang digunakan untuk padding, dan 64 adalah jumlah bit yang disisihkan untuk fase pra-pemrosesan kedua.
Total harus merupakan kelipatan dari 512 bit, yang diwakili oleh n.

![image](assets/image/section1/3.webp)

Contoh dengan pesan input sebesar 950 bit:

```
Langkah 1: Tentukan ukuran; jumlah bit akhir yang diinginkan.
Langkah pertama: Tentukan kelipatan pertama dari 512 > (M + 64 + 1) (dengan M = 950) adalah 1024. 1024 = 2 * 512
Jadi, n = 2.

Langkah 2: Tentukan P, jumlah bit padding yang diperlukan untuk mencapai jumlah bit akhir yang diinginkan.
-> M + 1 + P + 64 = n * 512
-> M + 1 + P + 64 = 2 * 512
-> 950 + 1 + P + 64 = 1024
-> P = 1024 - 1 - 64 - 950
-> P = 9
```

Oleh karena itu, 9 bit padding perlu ditambahkan untuk memiliki pesan yang disamakan dengan kelipatan 512.
Dan sekarang?
Tepat setelah pesan awal, pemisah 1 diikuti oleh P, yang dalam contoh kita adalah sembilan angka 0, perlu ditambahkan.

```
pesan + 1 000 000 000
```

#### Padding Ukuran

Kita sekarang beralih ke fase kedua dari pra-pemrosesan, yang melibatkan penambahan representasi biner dari ukuran pesan awal dalam bit.

Mari kita kembali ke contoh dengan input 950 bit:

```
Representasi biner dari angka 950 adalah: 11 1011 0110

Kita menggunakan 64 bit yang disediakan dari langkah sebelumnya. Kita menambahkan nol untuk membulatkan 64 bit kita ke input yang disamakan. Kemudian, kita menggabungkan pesan awal, bit padding, dan padding ukuran untuk mendapatkan input yang disamakan.
```

Berikut adalah hasilnya:

![image](assets/image/section1/4.webp)

### Pemrosesan

#### Memahami Prasyarat

##### Konstanta dan Vektor Inisialisasi

Sekarang, kita sedang mempersiapkan langkah awal pemrosesan fungsi SHA-256. Seperti dalam resep yang baik, kita memerlukan beberapa bahan dasar, yang kita sebut konstanta dan vektor inisialisasi.

Vektor inisialisasi, dari A hingga H, adalah 32 bit pertama dari bagian desimal dari akar kuadrat dari delapan bilangan prima pertama. Mereka akan berfungsi sebagai nilai dasar dalam langkah pemrosesan awal. Nilai mereka dalam format heksadesimal.

Konstanta K, dari 0 hingga 63, mewakili 32 bit pertama dari bagian desimal dari akar kubik dari 64 bilangan prima pertama. Mereka digunakan dalam setiap ronde dari fungsi kompresi. Nilai mereka juga dalam format heksadesimal.

![image](assets/image/section1/5.webp)

##### Operasi yang Digunakan

Dalam fungsi kompresi, kita menggunakan operator spesifik seperti XOR, AND, dan NOT. Kita memproses bit demi bit sesuai dengan posisinya, menggunakan operator XOR dan tabel kebenaran. Operator AND digunakan untuk mengembalikan 1 hanya jika kedua operand sama dengan 1, dan operator NOT digunakan untuk mengembalikan nilai berlawanan dari sebuah operand. Kita juga menggunakan operasi SHR untuk menggeser bit ke kanan dengan jumlah tertentu.

Tabel kebenaran:

![image](assets/image/section1/6.webp)

Operasi shift bit:

![image](assets/image/section1/7.webp)

#### Fungsi Kompresi

Sebelum menerapkan fungsi kompresi, kita membagi input menjadi blok-blok 512 bit. Setiap blok akan diproses secara independen dari yang lain.

Setiap blok 512-bit kemudian dibagi lebih lanjut menjadi potongan 32-bit yang disebut W. Dengan cara ini, W(0) mewakili 32 bit pertama dari blok 512-bit. W(1) mewakili 32 bit berikutnya, dan seterusnya, sampai kita mencapai 512 bit dari blok tersebut.
Setelah semua konstanta K dan potongan W didefinisikan, kita dapat melakukan perhitungan berikut untuk setiap potongan W di setiap ronde.

Kita melakukan 64 ronde perhitungan dalam fungsi kompresi. Di ronde terakhir, pada tingkat "Output dari fungsi", kita akan memiliki sebuah keadaan sementara yang akan ditambahkan ke keadaan awal dari fungsi kompresi.

Kemudian, kita mengulangi semua langkah ini dari fungsi kompresi pada blok 512-bit berikutnya, sampai blok terakhir.

Semua penambahan dalam fungsi kompresi adalah penambahan modulo 2^32 untuk selalu menjaga jumlah 32-bit.

![image](assets/image/section1/9.webp)

![image](assets/image/section1/8.webp)

##### Satu Ronde dari Fungsi Kompresi

![image](assets/image/section1/11.webp)

![image](assets/image/section1/10.webp)

Fungsi kompresi akan dilakukan 64 kali. Kita memiliki potongan W dan konstanta K yang telah didefinisikan sebelumnya sebagai input.
Kotak/kali merah sesuai dengan penambahan bit modulo 2^32.

Input A, B, C, D, E, F, G, H akan dikaitkan dengan nilai 32-bit untuk membuat total 32 \* 8 = 256 bit.
Kita juga memiliki urutan baru A, B, C, D, E, F, G, H sebagai output. Output ini kemudian akan digunakan sebagai input untuk ronde berikutnya dan seterusnya sampai akhir ronde ke-64.

Nilai dari urutan input untuk ronde pertama dari fungsi kompresi sesuai dengan vektor inisialisasi yang telah didefinisikan sebelumnya.
Sebagai pengingat, vektor inisialisasi mewakili 32 bit pertama dari bagian desimal dari akar kuadrat dari delapan bilangan prima pertama.

Berikut adalah contoh sebuah ronde:

![image](assets/image/section1/12.1.webp)

##### Keadaan Sementara

Sebagai pengingat, pesan dibagi menjadi blok 512 bit, yang kemudian dibagi menjadi potongan 32-bit. Untuk setiap blok 512-bit, kita menerapkan 64 ronde dari fungsi kompresi.
Keadaan sementara sesuai dengan akhir dari 64 ronde sebuah blok. Nilai dari urutan output dari ronde ke-64 ini digunakan sebagai nilai awal untuk urutan input dari ronde pertama blok berikutnya.

![image](assets/image/section1/12.2.webp)

#### Ikhtisar dari fungsi hash

![image](assets/image/section1/13.webp)

Kita dapat melihat bahwa output dari potongan pesan 512-bit pertama sesuai dengan vektor inisialisasi kita sebagai input untuk potongan pesan 512-bit kedua, dan seterusnya.

Output dari ronde terakhir, dari potongan terakhir, sesuai dengan hasil akhir dari fungsi SHA256.

Kesimpulannya, kami ingin menekankan peran penting dari perhitungan yang dilakukan dalam kotak CH, MAJ, σ0, dan σ1. Operasi-operasi ini, di antara lainnya, adalah penjaga yang memastikan kekuatan fungsi hash SHA256 terhadap serangan, menjadikannya pilihan yang disukai untuk mengamankan banyak sistem digital, terutama dalam protokol Bitcoin. Jelas bahwa, meskipun kompleks, keindahan SHA256 terletak pada kemampuannya untuk menemukan input dari hash, sementara memverifikasi hash untuk input yang diberikan adalah tindakan yang secara mekanis sederhana.

## Algoritma yang digunakan untuk derivasi

<chapterId>cc668121-7789-5e99-bf5e-1ba085f4f5f2</chapterId>
Algoritma derivasi HMAC dan PBKDF2 merupakan komponen kunci dalam mekanisme keamanan protokol Bitcoin. Mereka mencegah berbagai potensi serangan dan memastikan integritas dompet Bitcoin. HMAC dan PBKDF2 adalah alat kriptografi yang digunakan untuk berbagai tugas dalam Bitcoin. HMAC terutama digunakan untuk melawan serangan perpanjangan panjang saat menghasilkan dompet Deterministik Hierarkis (HD), sementara PBKDF2 digunakan untuk mengonversi frasa mnemonik menjadi seed.

#### HMAC-SHA512

Pasangan HMAC-SHA512 memiliki dua input: pesan m (Input 1) dan kunci K yang dipilih secara sembarangan oleh pengguna (Input 2). Ini juga memiliki output berukuran tetap: 512 bit.

Mari kita catat:

- m: pesan berukuran sembarang yang dipilih oleh pengguna (input 1)
- K: kunci sembarang yang dipilih oleh pengguna (input 2)
- K': kunci K yang disamakan. Ini telah disesuaikan dengan ukuran B dari blok.
- ||: operasi penggabungan.
- opad: konstanta yang ditentukan oleh byte 0x5c yang diulang B kali.
- ipad: konstanta yang ditentukan oleh byte 0x36 yang diulang B kali.
- B: Ukuran blok dari fungsi hash yang digunakan.

![image](assets/image/section1/14.webp)

HMAC-SHA512, yang mengambil pesan dan kunci sebagai input, menghasilkan output berukuran tetap. Untuk memastikan keseragaman, kunci disesuaikan berdasarkan ukuran blok yang digunakan dalam fungsi hash. Dalam konteks derivasi dompet HD, HMAC-SHA-512 digunakan. Ini beroperasi dengan blok 1024-bit (128-byte) dan menyesuaikan kunci sesuai. Ini menggunakan konstanta OPAD (0x5c) dan IPAD (0x36), diulang sesuai kebutuhan untuk meningkatkan keamanan.

Proses HMAC-SHA-512 melibatkan penggabungan hasil SHA-512 yang diterapkan pada kunci XOR OPAD dan kunci XOR IPAD dengan pesan. Saat digunakan dengan blok 1024-bit (128-byte), kunci input dipad dengan nol jika perlu, kemudian XORed dengan IPAD dan OPAD. Kunci yang dimodifikasi kemudian digabungkan dengan pesan.

![image](assets/image/section1/15.webp)

Penambahan garam dalam kode string meningkatkan keamanan kunci yang diturunkan. Tanpanya, serangan bisa mengkompromikan seluruh dompet dan mencuri semua bitcoin.

PBKDF2 digunakan untuk mengonversi frasa mnemonik menjadi seed. Algoritma ini melakukan 2048 putaran menggunakan HMAC SHA512. Melalui algoritma derivasi ini, input yang berbeda dapat menghasilkan output yang unik dan tetap, yang mengurangi masalah serangan perpanjangan panjang pada fungsi keluarga SHA-2.
Serangan perpanjangan panjang memanfaatkan properti spesifik dari beberapa fungsi hash kriptografi. Dalam serangan semacam itu, penyerang yang sudah memiliki hash dari pesan yang tidak diketahui dapat menggunakannya untuk menghitung hash dari pesan yang lebih panjang, yang merupakan perpanjangan dari pesan asli. Ini sering kali mungkin tanpa mengetahui isi dari pesan asli, yang dapat menyebabkan kerentanan keamanan yang signifikan jika jenis fungsi hash ini digunakan untuk tugas seperti verifikasi integritas.

![image](assets/image/section1/16.webp)

Kesimpulannya, algoritma HMAC dan PBKDF2 memainkan peran penting dalam keamanan derivasi dompet HD dalam protokol Bitcoin. HMAC-SHA-512 digunakan untuk melindungi dari serangan perpanjangan panjang, sementara PBKDF2 memungkinkan konversi frasa mnemonik menjadi seed. Kode string menambahkan sumber entropi tambahan dalam derivasi kunci, memastikan kekuatan sistem.

# Tanda Tangan Digital

<partId>76b58a00-0c18-54b9-870d-6b7e34029db8</partId>

## Tanda Tangan Digital dan Kurva Eliptik

<chapterId>c9dd9672-6da1-57f8-9871-8b28994d4c1a</chapterId>

Di mana bitcoin yang terkenal itu disimpan? Tidak dalam dompet Bitcoin, seperti yang mungkin dipikirkan orang. Pada kenyataannya, dompet Bitcoin menyimpan kunci privat yang diperlukan untuk membuktikan kepemilikan atas bitcoin. Bitcoin itu sendiri dicatat di blockchain, sebuah basis data terdesentralisasi yang mengarsipkan semua transaksi.

Dalam sistem Bitcoin, unit akun adalah bitcoin (perhatikan "b" kecil). Bitcoin dapat dibagi hingga delapan tempat desimal, dengan unit terkecilnya adalah satoshi. UTXO, atau "Unspent Transaction Outputs," mewakili output transaksi yang belum dihabiskan yang dimiliki oleh kunci publik yang secara matematis terhubung ke kunci privat. Untuk menghabiskan bitcoin ini, seseorang harus dapat memenuhi kondisi pengeluaran dari transaksi tersebut. Kondisi pengeluaran yang tipikal melibatkan pembuktian kepada jaringan lain bahwa pengguna adalah pemilik sah dari kunci publik yang terkait dengan UTXO. Untuk melakukan ini, pengguna harus menunjukkan kepemilikan kunci privat yang sesuai dengan kunci publik yang terhubung ke setiap UTXO tanpa mengungkapkan kunci privat tersebut.

Di sinilah tanda tangan digital berperan. Ini berfungsi sebagai bukti matematis kepemilikan kunci privat yang terkait dengan kunci publik tertentu. Teknik perlindungan data ini terutama didasarkan pada bidang kriptografi yang menarik yang disebut kriptografi kurva eliptik (ECC).

Tanda tangan dapat diverifikasi secara matematis oleh peserta lain dalam jaringan Bitcoin.

![image](assets/image/section2/0.webp)

Untuk memastikan keamanan transaksi, Bitcoin mengandalkan dua protokol tanda tangan digital: ECDSA (Elliptic Curve Digital Signature Algorithm) dan Schnorr. ECDSA telah menjadi protokol tanda tangan yang terintegrasi ke dalam Bitcoin sejak peluncurannya pada tahun 2009, sementara tanda tangan Schnorr ditambahkan lebih baru-baru ini pada November 2021. Meskipun kedua protokol tersebut didasarkan pada kriptografi kurva eliptik dan menggunakan mekanisme matematis yang serupa, mereka terutama berbeda dalam hal struktur tanda tangan.

Dalam kursus ini, kami akan memperkenalkan algoritma ECDSA.

### Apa itu kurva eliptik?

Kriptografi kurva eliptik adalah sekumpulan algoritma yang menggunakan kurva eliptik untuk berbagai properti geometris dan matematisnya dalam konteks kriptografi, dengan keamanan yang didasarkan pada kesulitan menghitung logaritma diskrit.

Kurva eliptik berguna dalam berbagai aplikasi kriptografi dalam protokol Bitcoin, mulai dari pertukaran kunci hingga enkripsi asimetris dan tanda tangan digital.

Kurva eliptik memiliki properti yang menarik:

- Simetri: Setiap garis non-vertikal yang memotong dua titik pada kurva eliptik akan memotong kurva pada titik ketiga.
- Setiap garis non-vertikal yang menyinggung kurva pada suatu titik akan selalu memotong kurva pada titik kedua yang unik.

Protokol Bitcoin menggunakan kurva eliptik tertentu yang disebut Secp256k1 untuk operasi kriptografinya.

Sebelum lebih dalam mempelajari mekanisme tanda tangan ini, penting untuk memahami apa itu kurva eliptik. Kurva eliptik didefinisikan oleh persamaan y² = x³ + ax + b. Setiap titik pada kurva ini memiliki simetri yang khas yang kunci untuk kegunaannya dalam kriptografi.

![image](assets/image/section2/1.webp)

Pada akhirnya, berbagai kurva eliptik diakui aman untuk penggunaan kriptografi. Yang paling terkenal mungkin adalah kurva secp256r1. Namun, untuk Bitcoin, Satoshi Nakamoto memilih kurva yang berbeda: secp256k1.
Kurva ini ditentukan oleh parameter a=0 dan b=7, dan persamaannya adalah y² = x³ + 7 modulo n, di mana n mewakili bilangan prima yang menentukan urutan kurva.
![image](assets/image/section2/2.webp)

Gambar pertama mewakili kurva secp256k1 di atas lapangan riil dan persamaannya.
Gambar kedua adalah representasi dari kurva secp256k1 di atas lapangan ZP, lapangan bilangan asli positif, modulo p di mana p adalah bilangan prima. Ini terlihat seperti awan titik. Kami menggunakan lapangan bilangan asli positif ini untuk menghindari pendekatan.
p adalah bilangan prima, dan itu adalah urutan dari kurva yang digunakan.
Akhirnya, persamaan yang digunakan dalam protokol Bitcoin adalah:$$
y^2 = (x^3 + 7) mod(p) $$
Persamaan kurva eliptik dalam Bitcoin sesuai dengan persamaan terakhir dalam gambar sebelumnya.

Di bagian selanjutnya dari kursus ini, kami akan menggunakan kurva yang berada di lapangan riil hanya untuk memudahkan pemahaman.

## Menghitung kunci publik dari kunci privat

<chapterId>fcb2bd58-5dda-5ecf-bb8f-ad1a0561ab4a</chapterId>

Untuk memulai, mari kita selami dunia Algoritma Tanda Tangan Digital Kurva Eliptik (ECDSA). Bitcoin menggunakan algoritma tanda tangan digital ini untuk menghubungkan kunci privat dan publik. Dalam sistem ini, kunci privat adalah angka 256-bit acak atau pseudo-acak. Jumlah total kemungkinan untuk sebuah kunci privat secara teoritis adalah 2^256, tetapi pada kenyataannya, itu sedikit kurang dari itu. Untuk lebih tepatnya, beberapa kunci privat 256-bit tidak valid untuk Bitcoin.

Untuk kompatibel dengan Bitcoin, sebuah kunci privat harus berada di antara 1 dan n-1, di mana n mewakili urutan dari kurva eliptik. Ini berarti bahwa jumlah total kemungkinan untuk sebuah kunci privat Bitcoin hampir sama dengan 1.158 x 10^77. Untuk memberikan perspektif, itu kira-kira jumlah atom yang ada di alam semesta yang dapat diamati.

![image](assets/image/section2/3.webp)

Kunci privat unik, yang ditandai sebagai k, kemudian digunakan untuk menentukan sebuah kunci publik.

Kunci publik, yang ditandai sebagai K, adalah titik pada kurva eliptik yang berasal dari kunci privat menggunakan algoritma tak reversibel seperti ECDSA. Ketika kita memiliki pengetahuan tentang kunci privat, sangat mudah untuk mengambil kunci publik, tetapi ketika kita hanya memiliki kunci publik, mustahil untuk mengambil kunci privat. Ketidakreversibelan ini adalah batu penjuru keamanan dompet Bitcoin.

Kunci publik memiliki panjang 512 bit karena sesuai dengan titik pada kurva dengan koordinat x sepanjang 256 bit dan koordinat y sepanjang 256 bit. Namun, ini dapat dikompres menjadi angka 264-bit.

![image](assets/image/section2/4.webp)

Titik generator (G) adalah titik pada kurva dari mana semua kunci publik dihasilkan dalam protokol Bitcoin. Ini memiliki koordinat x dan y tertentu, biasanya direpresentasikan dalam heksadesimal. Untuk secp256k1, koordinat G adalah, dalam heksadesimal:

- `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
- `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8` Titik ini berguna untuk menurunkan semua kunci publik. Untuk menghitung kunci publik K, cukup kalikan titik G dengan kunci privat k, sehingga: K = k.G

Kita akan sekarang mempelajari bagaimana menambahkan dan mengalikan titik pada kurva eliptik.

#### Penambahan dan penggandaan titik pada kurva eliptik

##### Menambahkan dua titik M + L

Salah satu sifat luar biasa dari kurva eliptik adalah bahwa sebuah garis non-vertikal yang memotong kurva di dua titik juga akan memotongnya di titik ketiga, yang disebut titik O dalam contoh kita. Sifat ini digunakan untuk menentukan titik U, yang merupakan kebalikan dari titik O.

M + L = U

![image](assets/image/section2/5.webp)

##### Menambahkan titik kepada dirinya sendiri = Penggandaan titik

Menambahkan titik G kepada dirinya sendiri dilakukan dengan menggambar tangen ke kurva pada titik tersebut. Tangen ini, menurut sifat-sifat kurva eliptik, akan memotong kurva di titik unik kedua -J. Kebalikan dari titik ini, J, adalah hasil dari penambahan titik G kepada dirinya sendiri.
G + G = J

Sebenarnya, titik G adalah titik awal untuk menghitung semua kunci publik pengguna sistem Bitcoin.

![image](assets/image/section2/6.webp)

#### Perkalian skalar pada kurva eliptik

Perkalian skalar sebuah titik dengan n setara dengan menambahkan titik tersebut kepada dirinya sendiri n kali.

Mirip dengan penggandaan titik, perkalian skalar titik G dengan titik n dilakukan dengan menggambar tangen ke kurva pada titik G. Tangen ini, menurut sifat-sifat kurva eliptik, akan memotong kurva di titik unik kedua -2G. Kebalikan dari titik ini, 2G, adalah hasil dari penambahan titik G kepada dirinya sendiri.

Jika n = 4, maka operasi diulangi sampai mencapai 4G.

![image](assets/image/section2/7.webp)

Berikut adalah contoh perhitungan untuk 3G:

![image](assets/image/section2/8.webp)

Operasi-operasi pada titik-titik kurva eliptik adalah dasar untuk menghitung kunci publik. Menurunkan kunci publik dengan mengetahui kunci privat sangat mudah.
Kunci publik adalah titik pada kurva eliptik, itu adalah hasil dari penambahan dan penggandaan titik G k kali. Dengan k = kunci privat.

Dalam contoh ini:

- Kunci privat k = 4
- Kunci publik K = kG = 4G

![image](assets/image/section2/9.webp)

Dengan mengetahui kunci privat k, sangat mudah untuk menghitung kunci publik K. Namun, mustahil untuk mengambil kembali kunci privat berdasarkan kunci publik. Apakah ini hasil dari penambahan atau penggandaan titik?

Dalam pelajaran berikutnya, kita akan menjelajahi bagaimana tanda tangan digital dibuat menggunakan algoritma ECDSA dengan kunci privat untuk menghabiskan bitcoin.

## Menandatangani dengan kunci privat

<chapterId>bb07826f-826e-5905-b307-3d82001fb778</chapterId>

Proses tanda tangan digital adalah metode kunci untuk membuktikan bahwa Anda adalah pemegang kunci privat tanpa mengungkapkannya. Ini dicapai menggunakan algoritma ECDSA, yang melibatkan penentuan nonce unik, menghitung angka spesifik V, dan menciptakan tanda tangan digital yang terdiri dari dua bagian, S1 dan S2.
Sangat penting untuk selalu menggunakan nonce yang unik untuk menghindari serangan keamanan. Contoh terkenal dari apa yang bisa terjadi ketika aturan ini tidak diikuti adalah peretasan PlayStation 3, yang dikompromikan karena penggunaan ulang nonce.
![](assets/image/section2/10.webp)

Langkah-langkah:

- Tentukan nonce v, yang merupakan nomor acak unik.
  Nonce = Number Only Used Once.
  Ini ditentukan oleh orang yang melakukan tanda tangan.
- Hitung dengan menambahkan dan menggandakan titik pada kurva eliptik dari titik G, posisi V pada kurva eliptik.
  Sehingga V = v.G
  x dan y adalah koordinat V pada bidang.
- Hitung S1.
  S1 = x mod n dengan n = urutan kurva dan x sebuah koordinat V pada bidang.
  Catatan: Jumlah kunci publik yang mungkin lebih besar dari jumlah titik pada kurva eliptik di lapangan bilangan bulat positif yang digunakan dalam Bitcoin.
  Urutan kurva hanya sesuai dengan kemungkinan yang dapat diambil oleh kunci publik pada kurva.
- Hitung S2.
  H(Tx) = Hash dari transaksi
  k = kunci privat
- Hitung tanda tangan: konkatenasi dari S1 + S2.
- Hitung P, perhitungan verifikasi tanda tangan.
  K = kunci publik

Sebagai contoh, untuk mendapatkan kunci publik 3G, Anda menggambar tangen ke titik G, menghitung lawan dari -G untuk mendapatkan 2G, dan kemudian menambahkan G dan 2G. Untuk melakukan transaksi, Anda harus membuktikan bahwa Anda mengetahui nomor 3 dengan membuka bitcoin yang terkait dengan kunci publik 3G.

Untuk membuat tanda tangan digital dan membuktikan bahwa Anda mengetahui kunci privat yang terkait dengan kunci publik 3G, Anda pertama-tama menghitung nonce, kemudian titik V yang terkait dengan nonce ini (dalam contoh yang diberikan, itu adalah 4G). Kemudian, Anda menghitung titik T dengan menambahkan kunci publik 3G dan titik V, yang memberikan 7G.

![image](assets/image/section2/11.webp)

Mari kita sederhanakan proses tanda tangan digital.
Dalam gambar sebelumnya, kunci privat k = 3.
Kita dapat dengan mudah menghitung kunci publik K yang terkait dengan kunci privat ini: K = 3G.
Kemudian, kita menghasilkan nonce secara pseudo-acak: v = 4.
Dari nonce ini, dimungkinkan untuk menghitung V sedemikian rupa: V = v.G = 4G.

Dari titik V ini, kita menghitung titik T sedemikian rupa:
T = t.G = 7G (dengan t = 7).

Sekarang saatnya untuk melanjutkan dengan verifikasi tanda tangan digital.

Memverifikasi tanda tangan digital adalah langkah penting dalam menggunakan algoritma ECDSA, yang memungkinkan konfirmasi keaslian pesan yang ditandatangani tanpa memerlukan kunci privat pengirim. Berikut cara kerjanya secara detail:

Dalam contoh kita, kita memiliki dua nilai penting: t dan V.
t adalah nilai numerik (7 dalam contoh ini), dan V adalah titik pada kurva eliptik (dipresentasikan oleh 4G di sini). Nilai-nilai ini dihasilkan selama pembuatan tanda tangan digital dan kemudian dikirim bersama dengan pesan untuk memungkinkan verifikasi.

Ketika penerima mendapatkan pesan, mereka juga akan menerima dua nilai ini, t dan V.

Berikut adalah langkah-langkah yang akan diikuti oleh penerima untuk memvalidasi tanda tangan:

1. Pertama, mereka akan menghitung hash dari pesan, yang akan kita sebut H.
2. Kemudian, mereka akan menghitung u1 dan u2. Untuk melakukan ini, mereka akan menggunakan rumus berikut:

- u1 = H /\* (S2)^-1 mod n - u2 = T /\* (S2)^-1 mod n
  Di mana S2 adalah bagian kedua dari tanda tangan digital, n adalah urutan dari kurva eliptik, dan (S2)^-1 adalah invers dari S2 mod n.

3. Verifikator kemudian akan menghitung sebuah titik P' pada kurva eliptik menggunakan rumus: P' = u1 _ G + u2 _ K
   - G adalah titik generator dari kurva
   - K adalah kunci publik pengirim
4. Verifikator kemudian akan menghitung I', yang hanyalah koordinat x dari titik P' modulo n.
5. Akhirnya, verifikator akan memastikan bahwa I' sama dengan t. Jika ini kasusnya, tanda tangan dianggap valid. Jika tidak, tanda tangan tidak valid.
   Prosedur ini memastikan bahwa hanya pengirim yang memiliki kunci privat yang sesuai yang bisa menghasilkan tanda tangan yang lolos proses verifikasi ini.

![image](assets/image/section2/12.webp)

Dengan kata yang lebih sederhana:
Orang yang menghasilkan tanda tangan akan memberikan nomor t (dalam contoh kita, t = 7) dan titik V kepada orang yang memverifikasinya.

Tidak mungkin untuk menentukan kunci publik atau kunci privat dari nomor 7 dan nomor V.

Langkah-langkah untuk memverifikasi tanda tangan digital adalah sebagai berikut:

- Di kurva, verifikator menambahkan titik dari kunci publik ke titik V untuk mengambil titik T'.
- Verifikator menghitung nomor t.G.
- Verifikator memeriksa bahwa hasil dari t.G memang sama dengan nomor T'.

Kesimpulannya, memverifikasi tanda tangan digital adalah prosedur penting dalam transaksi Bitcoin. Ini memastikan bahwa pesan yang ditandatangani tidak diubah selama transmisi dan bahwa pengirim memang pemegang kunci privat. Teknik otentikasi digital ini didasarkan pada prinsip matematika yang kompleks, termasuk aritmetika kurva eliptik, sambil menjaga kerahasiaan kunci privat. Ini memberikan dasar keamanan yang solid untuk transaksi kriptografi.

Dengan demikian, pengelolaan kunci-kunci ini, serta penciptaannya, adalah pertanyaan penting lainnya dalam Bitcoin. Bagaimana cara menghasilkan pasangan kunci baru? Bagaimana cara mengatur sejumlah besar kunci secara aman dan efisien? Bagaimana cara memulihkannya jika perlu?

Untuk menjawab pertanyaan-pertanyaan ini dan memperdalam pemahaman Anda tentang keamanan kriptografi, kursus berikutnya kami akan berfokus pada konsep Hierarchical Deterministic Wallets (HD wallets) dan penggunaan frasa mnemonik. Mekanisme ini menawarkan cara elegan untuk mengelola kunci kriptocurrency Anda sambil meningkatkan keamanan.

# Frasa Mnemonik

<partId>4070af16-c8a2-58b5-9871-a22c86c07458</partId>

## Evolusi Dompet Bitcoin

<chapterId>9d9acd5d-a0e5-5dfd-b544-f043fae8840f</chapterId>

Hierarchical Deterministic Wallet, yang lebih dikenal sebagai HD wallet, memainkan peran penting dalam ekosistem cryptocurrency. Istilah "wallet" mungkin menyesatkan bagi mereka yang baru di bidang ini, karena tidak melibatkan penyimpanan uang atau mata uang. Sebaliknya, ini merujuk pada koleksi kunci privat kriptografi.

Dompet awal adalah perangkat lunak yang mengelompokkan kunci yang ditentukan secara pribadi secara pseudo-acak tetapi tidak memiliki koneksi di antara mereka. Dompet ini disebut "Just a Bunch Of Keys" (JBOK).

Karena kunci-kunci tersebut tidak memiliki koneksi di antara mereka, pengguna diharuskan membuat cadangan baru untuk setiap pasangan kunci baru yang dihasilkan.
Apakah pengguna selalu menggunakan pasangan kunci yang sama dan mengompromikan kerahasiaan, atau menghasilkan pasangan kunci baru secara acak dan oleh karena itu perlu membuat cadangan baru dari kunci-kunci ini.
Namun, kompleksitas dalam mengelola kunci-kunci ini diimbangi oleh serangkaian protokol yang disebut Bitcoin Improvement Proposals (BIPs). Proposal peningkatan ini berada di inti dari fungsionalitas dan keamanan dompet HD. Sebagai contoh, [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), yang diluncurkan pada tahun 2012, merevolusi cara kunci-kunci ini dihasilkan dan disimpan dengan memperkenalkan konsep kunci yang diturunkan secara deterministik dan hierarkis. Ide ini adalah untuk menurunkan semua kunci secara deterministik dan hierarkis dari satu informasi unik: seed. Ini sangat menyederhanakan proses pencadangan kunci-kunci ini sambil mempertahankan tingkat keamanan mereka.
Selanjutnya, [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) memperkenalkan inovasi signifikan: frasa mnemonik 24 kata. Sistem ini mengubah urutan angka yang kompleks dan sulit diingat menjadi serangkaian kata biasa, membuatnya jauh lebih mudah untuk dihafal dan disimpan. Selain itu, [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) mengusulkan penambahan passphrase tambahan untuk meningkatkan keamanan kunci individu. Perbaikan berturut-turut ini mengarah pada standar BIP43 dan BIP44, yang menstandarisasi struktur dan hierarkisasi dompet HD, membuatnya lebih mudah diakses dan ramah pengguna bagi masyarakat umum.

Dalam bagian berikut, kita akan lebih dalam membahas cara kerja dompet HD. Kita akan membahas prinsip-prinsip derivasi kunci dan mengkaji konsep-konsep fundamental entropi dan generasi nomor acak, yang sangat penting untuk memastikan keamanan dompet HD Anda.

Secara kesimpulan, sangat penting untuk menyoroti peran sentral BIP32 dan BIP39 dalam desain dan keamanan dompet HD. Protokol-protokol ini memungkinkan generasi beberapa kunci dari satu seed, yang seharusnya merupakan nomor acak atau pseudo-acak. Saat ini, standar-standar ini diadopsi oleh mayoritas dompet cryptocurrency, baik yang didedikasikan untuk satu cryptocurrency atau mendukung berbagai jenis mata uang.

## Entropi dan Nomor Acak

<chapterId>b43c715d-affb-56d8-a697-ad5bc2fffd63</chapterId>

Pentingnya keamanan kunci privat dalam ekosistem Bitcoin tidak dapat disangkal. Mereka memang merupakan batu penjuru yang menjamin keamanan transaksi Bitcoin. Untuk menghindari kerentanan yang terkait dengan prediktabilitas, kunci-kunci ini harus dihasilkan secara benar-benar acak, yang dapat dengan cepat menjadi latihan yang berat. Masalahnya adalah dalam ilmu komputer, mustahil untuk menghasilkan nomor yang benar-benar acak karena selalu berasal dari proses deterministik; sebuah kode. Itulah mengapa sangat penting untuk mempelajari tentang berbagai Random Number Generators (RNG). Jenis RNG bervariasi, mulai dari Pseudo-Random Number Generators (PRNG) hingga True Random Number Generators (TRNG), serta PRNG yang menggabungkan sumber entropi.

Entropi merujuk pada keadaan "ketidakaturan" dari sebuah sistem. Dari entropi eksternal, yaitu sumber informasi eksternal, dimungkinkan untuk menggunakan generator nomor acak untuk mendapatkan nomor acak.

![image](assets/image/section3/2.webp)

Mari kita lihat bagaimana Pseudo-Random Number Generator (PRNG) bekerja.

Ini mengambil seed sebagai input, yang sesuai dengan internal state 0.
Pada internal state ini, sebuah fungsi transformasi diterapkan, dan hasilnya, yang merupakan nomor pseudo-acak, sesuai dengan internal state 1.
Pada internal state 1 ini, lagi, sebuah fungsi transformasi diterapkan, menghasilkan nomor acak baru = internal state 2.
Dan seterusnya.
Kekurangan utama adalah bahwa setiap benih identik akan selalu menghasilkan keluaran yang sama. Juga, jika kita mengetahui hasil dari fungsi transformasi awal, kita akan dapat mengambil kembali nomor acak pada keluaran proses tersebut.
Sebuah contoh dari fungsi transformasi adalah fungsi PBKDF2.

**Secara ringkas, sebuah PRNG yang aman secara kriptografis harus:**

- secara statistik acak
- tidak dapat diprediksi
- tetap aman meskipun hasilnya diungkapkan
- memiliki periode yang cukup panjang

![image](assets/image/section3/3.webp)

Dalam kasus Bitcoin, kunci privat dihasilkan dari satu potongan informasi di dasar dompet. Informasi ini memungkinkan derivasi deterministik dan hierarkis dari pasangan kunci anak. Entropi adalah dasar dari setiap dompet HD, meskipun tidak ada standar untuk menghasilkan nomor acak ini. Oleh karena itu, generasi nomor acak merupakan tantangan besar dalam mengamankan transaksi Bitcoin.

## Frase Mnemonik

<chapterId>8f9340c1-e6dc-5557-a2f2-26c9669987d5</chapterId>

Keamanan dompet Bitcoin merupakan perhatian utama bagi semua penggunanya. Salah satu cara penting untuk memastikan cadangan dompet adalah dengan menghasilkan frase mnemonik berdasarkan entropi dan checksum.

![image](assets/image/section3/5.webp)

Untuk mengonversi entropi menjadi frase mnemonik, cukup hitung checksum dari entropi dan gabungkan entropi dan checksum tersebut.

Setelah entropi dihasilkan, fungsi SHA256 digunakan pada entropi untuk membuat hash.
8 bit pertama dari hash diambil, yang merupakan checksum.
Frase mnemonik adalah hasil dari penambahan entropi dengan checksum.

Checksum memastikan verifikasi keakuratan frase pemulihan. Tanpa checksum ini, kesalahan dalam frase dapat menghasilkan pembuatan dompet yang berbeda dan oleh karena itu kehilangan dana. Checksum diperoleh dengan melewati entropi melalui fungsi SHA256 dan mengambil 8 bit pertama dari hash.

![image](assets/image/section3/6.webp)

Berbagai standar ada untuk frase mnemonik tergantung pada ukuran entropi. Standar yang paling umum digunakan untuk frase pemulihan 24 kata adalah entropi sebesar 256 bit. Ukuran checksum ditentukan dengan membagi ukuran entropi dengan 32.

Sebagai contoh, entropi sebesar 256 bit menghasilkan checksum 8 bit. Penggabungan entropi dan checksum kemudian mengarah pada ukuran masing-masing 128 bit, 160 bit, dll. Tergantung pada ukuran entropi, frase pemulihan akan terdiri dari 12 kata untuk 128 bit, 15 kata untuk 160 bit, dan 24 kata untuk 256 bit.

**Pengkodean frase mnemonik:**

![image](assets/image/section3/7.webp)

8 bit terakhir sesuai dengan checksum.
Setiap segmen 11-bit dikonversi menjadi desimal.
Setiap desimal sesuai dengan sebuah kata dari daftar 2048 kata pada BIP39. Penting untuk dicatat bahwa tidak ada kata yang memiliki urutan empat huruf pertama yang sama.

Sangat penting untuk mencadangkan frase pemulihan 24 kata untuk menjaga integritas dompet Bitcoin. Dua standar yang paling umum digunakan didasarkan pada entropi 128 atau 256 bit dan penggabungan 12 atau 24 kata. Menambahkan passphrase adalah opsi tambahan untuk meningkatkan keamanan dompet.

Kesimpulannya, menghasilkan frase mnemonik untuk mengamankan dompet Bitcoin adalah proses yang sangat penting. Penting untuk mematuhi standar frase mnemonik berdasarkan ukuran entropi. Mencadangkan frase pemulihan 24 kata sangat penting untuk mencegah kehilangan dana.

## Passphrase

<chapterId>6a51b397-f3b5-5084-b151-cef94bc9b93f</chapterId>
Frasa sandi adalah kata sandi tambahan yang dapat diintegrasikan ke dalam dompet Bitcoin untuk meningkatkan keamanannya. Penggunaannya bersifat opsional dan tergantung pada kebijakan pengguna. Dengan menambahkan informasi sembarang yang, bersama dengan frasa mnemonik, memungkinkan perhitungan benih dompet, frasa sandi meningkatkan keamanannya.

![image](assets/image/section3/8.webp)

Frasa sandi adalah garam kriptografi opsional dengan ukuran yang dipilih oleh pengguna. Ini meningkatkan keamanan dompet HD dengan menambahkan informasi sembarang yang, ketika digabungkan dengan frasa mnemonik, akan memungkinkan perhitungan benih.

Setelah ditetapkan selama pembuatan dompet, frasa sandi diperlukan untuk derivasi semua kunci dompet. Fungsi pbkdf2 digunakan untuk menghasilkan benih dari frasa sandi. Benih ini memungkinkan derivasi semua pasangan kunci anak dari dompet. Jika frasa sandi diubah, dompet Bitcoin menjadi sepenuhnya berbeda.

Frasa sandi adalah alat penting untuk meningkatkan keamanan dompet Bitcoin. Ini dapat memungkinkan implementasi berbagai strategi keamanan. Misalnya, dapat digunakan untuk membuat duplikat dan memfasilitasi cadangan frasa mnemonik. Ini juga dapat meningkatkan keamanan dompet dengan mengurangi risiko yang terkait dengan generasi acak frasa mnemonik.

Frasa sandi yang efektif harus panjang (20 hingga 40 karakter) dan beragam (menggunakan huruf besar, huruf kecil, angka, dan simbol). Ini tidak boleh langsung terkait dengan pengguna atau lingkungan mereka. Lebih aman menggunakan urutan karakter acak daripada kata sederhana sebagai frasa sandi.

![image](assets/image/section3/9.webp)

Frasa sandi lebih aman daripada kata sandi sederhana. Frasa sandi yang ideal adalah panjang, bervariasi, dan acak. Ini dapat meningkatkan keamanan dompet atau perangkat lunak panas. Ini juga dapat digunakan untuk membuat cadangan yang redundan dan aman.

Sangat penting untuk menjaga cadangan frasa sandi untuk menghindari kehilangan akses ke dompet. Frasa sandi adalah pilihan untuk dompet HD. Ini dapat dihasilkan secara acak dengan dadu atau generator nomor pseudo-acak lainnya. Tidak disarankan untuk menghafal frasa sandi atau frasa mnemonik.

Pada pelajaran berikutnya, kami akan memeriksa secara detail fungsi benih dan pasangan kunci pertama yang dihasilkan darinya. Jangan ragu untuk mengikuti kursus ini untuk melanjutkan pembelajaran Anda. Kami menantikan kedatangan Anda kembali sangat segera.

# Pembuatan Dompet Bitcoin

<partId>9c25e767-7eae-50b8-8c5f-679d8fc83bab</partId>

## Pembuatan Benih dan Kunci Utama

<chapterId>63093760-2010-5691-8d0e-9a04732ae557</chapterId>

Dalam bagian kursus ini, kami akan menjelajahi langkah-langkah untuk menderivasi Dompet Deterministik Hierarkis (HD Wallet), yang memungkinkan penciptaan dan pengelolaan kunci privat dan publik secara hierarkis dan deterministik.

![image](assets/image/section4/0.webp)

Dasar dari HD Wallet bergantung pada dua elemen penting: frasa mnemonik dan frasa sandi (kata sandi tambahan opsional). Bersama-sama, mereka membentuk benih, urutan alfanumerik 512 bit yang berfungsi sebagai dasar untuk menderivasi kunci dompet. Dari benih ini, dimungkinkan untuk menderivasi semua pasangan kunci anak dari dompet Bitcoin. Benih adalah kunci yang memberikan akses ke semua bitcoin yang terkait dengan dompet, apakah Anda menggunakan frasa sandi atau tidak.

![image](assets/image/section4/1.webp)
Untuk mendapatkan seed, fungsi pbkdf2 (Password-Based Key Derivation Function 2) digunakan dengan frasa mnemonik dan passphrase. Output dari pbkdf2 adalah seed 512-bit.
Dari seed tersebut, dimungkinkan untuk menentukan master private key dan chain code menggunakan algoritma HMAC SHA-512 (Hash-based Message Authentication Code Secure Hash Algorithm 512). Algoritma ini memerlukan sebuah pesan dan sebuah kunci sebagai input untuk menghasilkan sebuah hasil. Master private key dihitung dari seed dan frasa "Bitcoin SEED". Frasa ini identik untuk semua turunan dari semua HD wallets, memastikan konsistensi lintas dompet.

Awalnya, fungsi SHA-512 tidak diimplementasikan dalam protokol Bitcoin, itulah sebabnya HMAC SHA-512 digunakan. Penggunaan HMAC SHA-512 dengan frasa "Bitcoin SEED" membatasi pengguna untuk menghasilkan dompet yang spesifik untuk Bitcoin. Hasil dari HMAC SHA-512 adalah angka 512-bit, dibagi menjadi dua bagian: 256 bit paling kiri mewakili master private key, sementara 256 bit paling kanan mewakili master chain code.

![image](assets/image/section4/2.webp)

Master private key adalah kunci induk dari semua kunci masa depan dalam dompet, sementara master chain code terlibat dalam derivasi kunci anak. Penting untuk dicatat bahwa tidak mungkin untuk menurunkan pasangan kunci anak tanpa mengetahui chain code yang sesuai dari pasangan induk.

Pasangan kunci dalam dompet terdiri dari kunci privat, kunci publik, dan chain code. Chain code memperkenalkan sumber keacakan dalam derivasi kunci anak dan mengisolasi setiap pasangan kunci untuk mencegah kebocoran informasi.
Penting untuk dicatat bahwa master private key adalah kunci privat pertama yang diturunkan dari seed dan tidak memiliki koneksi ke kunci-kunci ekstensi dari dompet.

Pada pelajaran selanjutnya, kita akan menjelajahi kunci-kunci ekstensi secara detail, seperti xPub, xPRV, zPub, dan memahami mengapa mereka digunakan dan bagaimana mereka dibangun.

## Kunci Ekstensi

<chapterId>8dcffce1-31bd-5e0b-965b-735f5f9e4602</chapterId>

Dalam bagian pelajaran ini, kita akan mempelajari kunci-kunci ekstensi (xPub, zPub, yPub) dan prefiks mereka, yang memainkan peran penting dalam derivasi kunci anak dalam Hierarchical Deterministic Wallet (HD Wallet).

![image](assets/image/section4/3.webp)

Kunci ekstensi berbeda dari kunci induk. Sebuah HD wallet menghasilkan frasa mnemonik dan seed untuk mendapatkan master key dan master chain code. Kunci ekstensi digunakan untuk menurunkan kunci anak dan memerlukan baik kunci induk dan chain code yang sesuai. Kunci ekstensi menggabungkan kedua informasi ini untuk menyederhanakan proses derivasi.

![image](assets/image/section4/4.webp)

Kunci publik ekstensi hanya dapat menurunkan kunci publik anak normal, sementara kunci privat ekstensi dapat menurunkan baik kunci publik dan privat anak, baik melalui derivasi normal maupun hardened. Derivasi hardened adalah derivasi dari kunci privat induk, sementara derivasi normal sesuai dengan derivasi dari kunci publik induk.

Menggunakan kunci ekstensi dengan prefiks XPUB memungkinkan untuk derivasi alamat baru tanpa kembali ke kunci privat yang sesuai, sehingga memberikan keamanan yang lebih baik. Metadata yang terkait dengan kunci ekstensi memberikan informasi penting tentang peran dan posisi mereka dalam hierarki kunci.
Kunci yang diperluas diidentifikasi oleh prefiks tertentu (XPRV, XPUB, YPUB, ZPUB) yang menunjukkan apakah itu adalah kunci privat atau publik yang diperluas, serta tujuan spesifiknya. Metadata yang terkait dengan kunci yang diperluas mencakup versi (prefiks), kedalaman, sidik jari kunci induk, indeks, dan muatan (kode rantai dan kunci induk).
![image](assets/image/section4/5.webp)

Versi sesuai dengan jenis kunci: xpub, xprv, ...

Kedalaman sesuai dengan jumlah turunan antara kunci induk dan anak sejak kunci master.

Sidik jari induk adalah 4 byte pertama dari hash 160 dari kunci induk. Indeks adalah jumlah pasangan yang digunakan untuk menghasilkan kunci yang diperluas di antara saudara kandungnya. (saudara kandung = kunci dengan kedalaman yang sama) Sebagai contoh, jika kita ingin menurunkan xpub dari akun ketiga kita, indeksnya akan 2 (karena indeks dimulai dari 0).

Muatan terdiri dari kode rantai (32 byte) dan kunci induk (33 byte).

Kunci publik yang dikompresi memiliki ukuran 33 byte, sementara kunci publik mentah adalah 512 bit. Kunci publik yang dikompresi mempertahankan informasi yang sama seperti kunci mentah, tetapi dengan ukuran yang lebih kecil. Kunci yang diperluas memiliki ukuran 82 byte dan prefiksnya diwakili dalam basis 58 melalui konversi ke heksadesimal. Checksum dihitung menggunakan fungsi hash HASH256.

![image](assets/image/section4/6.webp)

Turunan yang ditingkatkan dimulai dari indeks yang merupakan pangkat dari 2 (2^31). Menarik untuk dicatat bahwa prefiks yang paling sering digunakan adalah xpub dan zpub, yang masing-masing sesuai dengan standar warisan dan segwit v1 serta segwit v0.

Pada pelajaran berikutnya, kita akan fokus pada turunan pasangan kunci anak menggunakan pengetahuan yang diperoleh tentang kunci yang diperluas dan kunci master dari dompet.

## Turunan Pasangan Kunci Anak

<chapterId>61c0807c-845b-5076-ad06-7f395b36adfd</chapterId>

Sebagai pengingat, kita telah membahas perhitungan benih dan kunci master, yang merupakan elemen pertama yang penting untuk organisasi hierarkis dan turunan dari dompet HD (Hierarchical Deterministic). Benih, dengan panjang 128 hingga 256 bit, dihasilkan secara acak atau dari frasa rahasia. Ini memainkan peran deterministik dalam turunan semua kunci lainnya. Kunci master adalah kunci pertama yang diturunkan dari benih, dan ini memungkinkan turunan semua pasangan kunci anak lainnya.

Kode rantai master memainkan peran penting dalam pemulihan dompet dari benih. Perlu dicatat bahwa semua kunci yang diturunkan dari benih yang sama akan memiliki kode rantai master yang sama.

![image](assets/image/section4/7.webp)

Organisasi hierarkis dan turunan dari dompet HD menawarkan pengelolaan kunci dan struktur dompet yang lebih efisien. Kunci yang diperluas memungkinkan turunan pasangan kunci anak dari pasangan kunci induk menggunakan perhitungan matematis dan algoritma spesifik.
Ada berbagai jenis pasangan kunci anak, termasuk kunci yang diperkuat dan kunci normal. Kunci publik yang diperluas hanya memungkinkan turunan kunci publik anak normal, sementara kunci privat yang diperluas memungkinkan turunan semua kunci anak, baik publik maupun privat, apakah mereka dalam mode normal atau diperkuat. Setiap pasangan kunci memiliki indeks yang memungkinkan mereka dibedakan satu sama lain.

![image](assets/image/section4/8.webp)
Turunan kunci anak menggunakan fungsi HMAC-SHA512 dengan menggunakan kunci induk yang digabungkan dengan indeks dan kode rantai yang terkait dengan pasangan kunci. Kunci anak normal memiliki indeks yang berkisar dari 0 hingga 2 pangkat 31 dikurangi 1, sementara kunci anak yang diperkuat memiliki indeks yang berkisar dari 2 pangkat 31 hingga 2 pangkat 32 dikurangi 1.

![image](assets/image/section4/9.webp)

![image](assets/image/section4/10.webp)

Ada dua jenis pasangan kunci anak: pasangan yang diperkuat dan pasangan normal. Proses turunan kunci anak menggunakan kunci publik untuk menghasilkan kondisi pengeluaran, sementara kunci privat digunakan untuk penandatanganan. Kunci publik yang diperluas hanya memungkinkan turunan dari kunci publik anak normal, sementara kunci privat yang diperluas memungkinkan turunan dari semua kunci anak, baik publik maupun privat, dalam mode normal atau diperkuat.

![image](assets/image/section4/11.webp)
![image](assets/image/section4/12.webp)

Turunan yang diperkuat menggunakan kunci privat induk, sementara turunan normal menggunakan kunci publik induk. Fungsi HMAC-SHA512 digunakan untuk turunan yang diperkuat, sementara turunan normal menggunakan digest 512-bit. Kunci publik anak diperoleh dengan mengalikan kunci privat anak dengan generator kurva eliptik.

![image](assets/image/section4/13.webp)
![image](assets/image/section4/14.webp)

Turunan secara hierarkis dan turunan banyak pasangan kunci secara deterministik memungkinkan pembuatan struktur pohon untuk turunan hierarkis. Dalam pelajaran berikutnya dari pelatihan ini, kita akan mempelajari struktur dari dompet HD serta jalur turunan, dengan fokus khusus pada notasi jalur turunan.

## Struktur Dompet dan Jalur Turunan

<chapterId>34e1bbda-67de-5493-b268-1fded8d67689</chapterId>

Dalam bab ini, kita akan mempelajari struktur dari pohon turunan dalam Dompet Deterministik Hierarkis (HD Wallet). Kita sudah mengeksplorasi perhitungan benih, kunci induk, dan turunan dari pasangan kunci anak. Sekarang, kita akan fokus pada pengorganisasian kunci dalam dompet.

Dompet HD menggunakan lapisan kedalaman untuk mengorganisir kunci. Setiap turunan dari pasangan induk ke pasangan anak sesuai dengan lapisan kedalaman.

![image](assets/image/section4/15.webp)

- Kedalaman 0 sesuai dengan kunci induk dan kode rantai induk.

- Kedalaman 1 digunakan untuk menurunkan kunci anak untuk tujuan tertentu, yang ditentukan oleh indeks. Tujuan-tujuan ini sesuai dengan standar BIP 84 dan Segwit v0/v1.

- Kedalaman 2 memungkinkan diferensiasi akun untuk mata uang kripto atau jaringan yang berbeda. Ini memungkinkan pengorganisasian dompet berdasarkan sumber dana yang berbeda. Untuk bitcoin, indeksnya akan 0.

- Kedalaman 3 digunakan untuk mengorganisir dompet ke dalam akun yang berbeda, menyediakan struktur yang lebih jelas dan lebih terorganisir.

- Kedalaman 4 sesuai dengan rantai eksternal dan internal, yang digunakan untuk alamat yang dimaksudkan untuk dikomunikasikan secara publik. Indeks 0 dikaitkan dengan rantai eksternal, sementara indeks 1 dikaitkan dengan rantai internal. Setiap akun memiliki dua rantai: rantai eksternal (0) dan rantai internal (1). Kedalaman 4 juga digunakan untuk mengelola jenis skrip dalam kasus dompet multi-tanda tangan.

- Kedalaman 5 digunakan untuk alamat penerimaan dalam dompet standar. Dalam bagian berikutnya, kita akan memeriksa turunan dari pasangan kunci anak secara lebih detail.

![image](assets/image/section4/16.webp)

Untuk setiap lapisan kedalaman, kita menggunakan indeks untuk membedakan pasangan kunci anak.
Indeks tanpa apostrof merujuk pada indeks yang digunakan sebenarnya, sementara indeks dengan apostrof merujuk pada indeks sebenarnya + 2^31. Derivasi yang diperkuat menggunakan indeks dari 2^31 hingga 2^32-1. Sebagai contoh, indeks 44' merujuk pada indeks sebenarnya 2^31 + 44.
Untuk menghasilkan alamat penerimaan spesifik, kita menurunkan pasangan kunci anak dari kunci induk dan kode rantai induk. Kemudian, kita menggunakan indeks untuk membedakan antara pasangan kunci anak yang berbeda pada kedalaman yang sama.

Kunci ekstensi, seperti XPUB, memungkinkan Anda untuk berbagi dompet Anda dengan beberapa orang. Jalur derivasi digunakan untuk membedakan antara rantai eksternal (alamat yang dimaksudkan untuk dibagikan) dan rantai internal (alamat perubahan).

Dalam bab berikutnya, kita akan mempelajari alamat penerimaan, keuntungan penggunaannya, dan langkah-langkah yang terlibat dalam konstruksinya.

# Apa itu alamat Bitcoin?

<partId>81ec8d17-f8ee-5aeb-8035-d370866f4281</partId>

## Alamat Bitcoin

<chapterId>0a887ed8-3424-5a52-98e1-e4b406150475</chapterId>

Dalam bab ini, kita akan menjelajahi alamat penerimaan, yang memainkan peran penting dalam sistem Bitcoin. Alamat ini memungkinkan dana diterima dalam sebuah transaksi dan dihasilkan dari pasangan kunci privat dan publik. Meskipun ada jenis skrip yang disebut Pay2PublicKey yang memungkinkan bitcoin dikunci ke kunci publik, pengguna umumnya lebih suka menggunakan alamat penerimaan daripada skrip ini.

![image](assets/image/section5/0.webp)

Ketika penerima ingin menerima bitcoin, mereka menyediakan alamat penerimaan kepada pengirim alih-alih kunci publik mereka. Sebuah alamat sebenarnya adalah hash dari kunci publik, dengan format tertentu. Kunci publik diturunkan dari kunci privat anak menggunakan operasi matematika seperti penambahan titik dan penggandaan pada kurva eliptik.

![image](assets/image/section5/1.webp)

Penting untuk dicatat bahwa tidak mungkin untuk membalikkan dari alamat ke kunci publik, atau dari kunci publik ke kunci privat. Menggunakan alamat mengurangi ukuran informasi kunci publik, yang awalnya adalah 512 bit.

Alamat Bitcoin telah dikurangi ukurannya untuk memudahkan penggunaannya. Mereka memiliki checksum, yang memungkinkan untuk mendeteksi kesalahan ketik dan mengurangi risiko kehilangan bitcoin. Di sisi lain, kunci publik tidak memiliki checksum, yang berarti bahwa kesalahan ketik dapat mengakibatkan kehilangan dana yang sesuai.

Alamat juga menyediakan lapisan keamanan kedua antara informasi publik dan privat, membuatnya lebih sulit untuk mengambil kendali kunci privat.

Sangat penting untuk menekankan bahwa setiap alamat harus digunakan hanya sekali. Menggunakan alamat yang sama berulang kali menimbulkan masalah privasi dan harus dihindari.

Awalan yang berbeda digunakan untuk alamat Bitcoin. Sebagai contoh, BC1Q sesuai dengan alamat Segwit V0, BC1P untuk alamat Taproot/Segwit V1, dan awalan 1 dan 3 dikaitkan dengan alamat Pay2PublicKeyH/Pay2ScriptH (legacy). Dalam pelajaran berikutnya, kita akan menjelaskan langkah demi langkah cara menurunkan alamat dari kunci publik.

## Bagaimana cara membuat alamat Bitcoin?

<chapterId>6dee7bf3-7767-5f8d-a01b-659b95cfe0a5</chapterId>

Dalam bab ini, kita akan membahas konstruksi alamat penerimaan untuk transaksi Bitcoin. Alamat penerimaan adalah representasi alfanumerik dari kunci publik yang dikompresi. Konversi kunci publik menjadi alamat penerimaan melibatkan beberapa langkah.

### Langkah 1: Kompresi kunci publik

Sebuah alamat dihasilkan dari kunci publik anak.

Kunci publik adalah titik pada kurva eliptik. Berkat simetri kurva eliptik, sebuah titik pada kurva eliptik akan memiliki koordinat x yang terkait dengan hanya dua nilai y yang mungkin: positif atau negatif. Namun, dalam protokol Bitcoin, kita bekerja dengan satu set bilangan bulat positif yang terbatas daripada dengan satu set bilangan riil. Untuk membedakan antara dua nilai y yang mungkin, cukup untuk menunjukkan apakah y genap atau ganjil.

Kompresi kunci publik mengurangi ukurannya dari 520 bit menjadi 264 bit.

Kita menggunakan awalan 0x02 untuk y genap dan 0x03 untuk y ganjil. Ini adalah bentuk terkompresi dari kunci publik.

### Langkah 2: Hashing dari kunci publik terkompresi

Hashing dari kunci publik terkompresi dilakukan menggunakan fungsi SHA256. Fungsi RIPEMD160 kemudian diterapkan pada digest.

### Langkah 3: Payload = Alamat payload

Digest biner dari RIPEMD160(SHA256(K)) digunakan untuk membentuk kelompok 5 bit. Setiap kelompok diubah menjadi basis 16 (Heksadesimal) dan/atau basis 10.

### Langkah 4: Menambahkan metadata untuk perhitungan checksum dengan program BCH

Dalam kasus alamat warisan, kita menggunakan hashing SHA256 ganda untuk menghasilkan checksum alamat. Namun, untuk alamat Segwit V0 dan V1, kita mengandalkan teknologi checksum BCH untuk memastikan deteksi kesalahan. Program BCH mampu menyarankan dan memperbaiki kesalahan dengan probabilitas kesalahan yang sangat rendah. Saat ini, program BCH digunakan untuk mendeteksi dan menyarankan modifikasi yang harus dilakukan, tetapi tidak secara otomatis melakukannya atas nama pengguna.

Program BCH memerlukan beberapa informasi masukan, termasuk HRP (Human Readable Part) yang perlu diperluas. Memperluas HRP melibatkan pengkodean setiap huruf dalam basis 2 menurut kode ASCII mereka. Kemudian, dengan mengambil 3 bit pertama dari hasil untuk setiap huruf dan mengonversinya ke basis 10 (dalam biru pada gambar). Masukkan pemisah 0. Kemudian menggabungkan 5 bit berikutnya dari setiap huruf yang sebelumnya dikonversi ke basis 10 (dalam kuning pada gambar).

Memperluas HRP dalam basis 10 memungkinkan isolasi lima bit terakhir dari setiap karakter, sehingga memperkuat checksum.

Versi Segwit V0 diwakili oleh kode 00 dan "payload" dalam hitam, dalam basis 10. Ini diikuti oleh enam karakter yang disediakan untuk checksum.

### Langkah 5: Menghitung checksum dengan program BCH

Input yang berisi metadata kemudian diserahkan ke program BCH untuk mendapatkan checksum dalam basis 10.

Di sini kita memiliki checksum.

### Langkah 6: Konstruksi alamat dan konversi ke Bech32

Penggabungan versi, payload, dan checksum memungkinkan pembangunan alamat. Karakter basis 10 kemudian dikonversi menjadi karakter Bech32 menggunakan tabel korespondensi. Abjad Bech32 mencakup semua karakter alfanumerik, kecuali untuk 1, b, i, dan o, untuk menghindari kebingungan.

### Langkah 7: Menambahkan HRP dan pemisah

Dalam pink, checksum.
Dalam warna hitam, payload = hash dari kunci publik. Dalam warna biru, versinya.

Semuanya dikonversi ke Bech32, kemudian 'bc' ditambahkan untuk bitcoin dan '1' sebagai pemisah, dan inilah alamatnya.

# Lebih Lanjut

<partId>58111408-b734-54db-9ea7-0d5b67f99f99</partId>

## Membuat seed dari 128 lemparan dadu!

<chapterId>0f4d40a7-cf0e-5faf-bc4d-691486771ac1</chapterId>

Membuat frasa mnemonik adalah langkah penting dalam mengamankan dompet kripto Anda. Ada beberapa metode untuk menghasilkan frasa mnemonik, namun, kita akan fokus pada metode generasi manual menggunakan dadu. Penting untuk dicatat bahwa metode ini tidak cocok untuk dompet bernilai tinggi. Disarankan untuk menggunakan perangkat lunak sumber terbuka atau dompet perangkat keras untuk menghasilkan frasa mnemonik. Untuk membuat frasa mnemonik, kita akan menggunakan dadu untuk menghasilkan informasi biner. Tujuannya adalah untuk memahami proses pembuatan frasa mnemonik.

**Langkah 1 - Persiapan:**
Pastikan Anda memiliki distribusi Linux amnesik, seperti Tails OS, yang terinstal pada kunci USB untuk keamanan tambahan. Catat bahwa tutorial ini tidak seharusnya digunakan untuk membuat dompet utama.
**Langkah 2 - Menghasilkan angka biner acak:**
Kita akan menggunakan dadu untuk menghasilkan informasi biner. Lempar dadu sebanyak 128 kali dan catat setiap hasilnya (1 untuk ganjil, 0 untuk genap).

**Langkah 3 - Mengorganisir angka biner:**
Organisir angka biner yang diperoleh ke dalam baris yang terdiri dari 11 digit untuk memudahkan perhitungan lebih lanjut. Baris kedua belas hanya harus memiliki 7 digit.

**Langkah 4 - Menghitung checksum:**
4 digit terakhir untuk baris kedua belas sesuai dengan checksum. Untuk menghitung checksum ini, kita perlu menggunakan terminal dari distribusi Linux. Disarankan untuk menggunakan [TailOs](https://tails.boum.org/index.fr.html), yang merupakan distribusi tanpa memori yang dapat di-boot dari kunci USB. Setelah berada di terminal Anda, masukkan perintah `echo <binary number> | shasum -a 254 -0`. Ganti `<binary number>` dengan daftar 128 nol dan satu Anda. Outputnya adalah hash heksadesimal. Catat karakter pertama dari hash ini dan konversikan ke biner. Anda dapat menggunakan [tabel](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table) ini untuk bantuan. Tambahkan checksum biner (4 digit) ke baris kedua belas dari lembar Anda.

**Langkah 5 - Konversi ke desimal:**
Untuk menemukan kata-kata yang terkait dengan setiap baris Anda, pertama-tama Anda perlu mengonversi setiap seri dari 11 bit menjadi desimal. Di sini, Anda tidak dapat menggunakan konverter online karena bit-bit ini mewakili frasa mnemonik Anda. Oleh karena itu, Anda akan perlu mengonversi menggunakan kalkulator dan trik sebagai berikut: setiap bit dikaitkan dengan pangkat dari 2, jadi dari kiri ke kanan, kita memiliki 11 peringkat yang sesuai dengan 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1. Untuk mengonversi seri 11 bit Anda menjadi desimal, cukup tambahkan hanya peringkat yang mengandung 1. Sebagai contoh, untuk seri 00110111011, ini sesuai dengan penjumlahan berikut: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. Anda sekarang dapat mengonversi setiap baris menjadi desimal. Dan sebelum melanjutkan ke pengkodean menjadi kata-kata, tambahkan +1 ke semua baris karena indeks dari daftar kata BIP39 dimulai dari 1, bukan 0.
**Langkah 8 - Menghasilkan frasa mnemonik:**
Mulailah dengan mencetak [daftar 2048 kata](https://seedxor.com/files/wordlist.pdf) untuk mengonversi antara angka desimal Anda dan kata-kata BIP39. Keunikan dari daftar ini adalah tidak ada kata yang berbagi 4 huruf pertama dengan kata lain dalam kamus ini. Kemudian, cari kata yang terkait dengan nomor desimal setiap baris Anda.
**Langkah 9 - Tes Frasa Mnemonik:**
Segera tes frasa mnemonik Anda di Sparrow Wallet dengan membuat dompet dari frasa tersebut. Jika Anda menerima kesalahan checksum yang tidak valid, kemungkinan Anda membuat kesalahan perhitungan. Koreksi kesalahan ini dengan kembali ke langkah 4 dan tes lagi di Sparrow Wallet. Voilà! Anda baru saja membuat dompet Bitcoin baru dari 128 lemparan dadu.

Menghasilkan frasa mnemonik adalah proses penting untuk mengamankan dompet cryptocurrency Anda. Disarankan untuk menggunakan metode yang lebih aman, seperti menggunakan perangkat lunak sumber terbuka atau dompet perangkat keras, untuk menghasilkan frasa mnemonik. Namun, menyelesaikan lokakarya ini membantu untuk lebih memahami bagaimana kita dapat membuat dompet Bitcoin dari angka acak.

## BONUS: Wawancara dengan Théo Pantamis

<chapterId>39f0ec5a-e258-55cb-9789-bc46d314d816</chapterId>

Metode kriptografi lain yang banyak digunakan pada protokol Bitcoin adalah metode tanda tangan digital.

![video](https://youtu.be/c9MvtGJsEvY?si=bQ1N5NCd6op0G6nW)



## Evaluasi kursus ini
<chapterId>0cd71541-a7fd-53db-b66a-8611b6a28b04</chapterId>
<isCourseReview>true</isCourseReview>

## Ujian Akhir
<chapterId>a53ea27d-0f84-56cd-b37c-a66210a4b31d</chapterId>
<isCourseExam>true</isCourseExam>


## Kesimpulan dan Akhir

<chapterId>d291428b-3cfa-5394-930e-4b514be82d5a</chapterId>

### Terima kasih dan terus menggali lubang kelinci

Kami ingin mengucapkan terima kasih yang tulus kepada Anda karena telah menyelesaikan kursus Crypto 301. Kami berharap pengalaman ini telah menjadi pengayaan dan edukatif bagi Anda. Kami telah membahas banyak topik menarik, mulai dari matematika hingga kriptografi hingga cara kerja protokol Bitcoin.

Jika Anda ingin mendalami subjek ini lebih lanjut, kami memiliki sumber daya tambahan untuk menawarkan Anda. Kami melakukan wawancara eksklusif dengan Théo Pantamis dan Loïc Morel, dua ahli terkenal di bidang kriptografi. Wawancara ini mengeksplorasi berbagai aspek subjek secara mendalam dan memberikan perspektif yang menarik.

Jangan ragu untuk menonton wawancara ini untuk terus menjelajahi bidang kriptografi yang menarik. Kami berharap itu akan berguna dan menginspirasi dalam perjalanan Anda. Sekali lagi, terima kasih atas partisipasi dan komitmen Anda sepanjang kursus ini.

### Dukung Kami

Kursus ini, bersama dengan seluruh konten di universitas ini, telah disediakan untuk Anda secara gratis oleh komunitas kami. Untuk mendukung kami, Anda dapat membagikannya dengan orang lain, menjadi anggota universitas, dan bahkan berkontribusi pada pengembangannya melalui GitHub. Atas nama seluruh tim, terima kasih!

### Nilai kursus

Sistem penilaian untuk pelatihan ini akan segera diintegrasikan ke dalam platform E-learning baru ini! Sementara itu, terima kasih banyak telah mengikuti kursus ini, dan jika Anda menikmatinya, pertimbangkan untuk membagikannya dengan orang lain.

