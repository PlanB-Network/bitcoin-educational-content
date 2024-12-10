---
name: Cara Kerja Dompet Bitcoin
goal: Menyelami prinsip-prinsip kriptografi yang menggerakkan dompet Bitcoin.
objectives:
  - Mendefinisikan konsep teoretis yang diperlukan untuk memahami algoritma kriptografi yang digunakan dalam Bitcoin.
  - Memahami sepenuhnya pembangunan dompet yang deterministik dan hierarkis.
  - Mengetahui cara mengidentifikasi dan mengurangi risiko yang terkait dengan pengelolaan dompet.
  - Memahami prinsip fungsi hash, kunci kriptografi, dan tanda tangan digital.
---

# Perjalanan ke Jantung Dompet Bitcoin

Temukan rahasia dompet Bitcoin yang deterministik dan hierarkis dengan kursus CYP201 kami! Baik Anda pengguna reguler atau penggemar yang ingin memperdalam pengetahuan Anda, kursus ini menawarkan penyelaman lengkap ke dalam cara kerja alat-alat ini yang kita gunakan setiap hari.

Pelajari tentang mekanisme fungsi hash, tanda tangan digital (ECDSA dan Schnorr), frasa mnemonik, kunci kriptografi, dan pembuatan alamat penerima, sembari menjelajahi strategi keamanan lanjutan.

Pelatihan ini tidak hanya akan membekali Anda dengan pengetahuan untuk memahami struktur dompet Bitcoin, tetapi juga akan mempersiapkan Anda untuk menyelami dunia kriptografi yang menarik.

Dengan pedagogi yang jelas, lebih dari 60 diagram penjelas, dan contoh konkret, CYP201 akan memungkinkan Anda untuk memahami dari A sampai Z bagaimana dompet Anda bekerja, sehingga Anda dapat menjelajahi alam semesta Bitcoin dengan percaya diri. Ambil kendali UTXO Anda hari ini dengan memahami bagaimana dompet HD berfungsi!

+++

# Pendahuluan

<partId>32960669-d13a-592f-a053-37f70b997cbf</partId>

## Pengenalan Kursus

<chapterId>fb4e8857-ea35-5a8a-ae8a-5300234e0104</chapterId>

Selamat datang di kursus CYP201, di mana kita akan menjelajahi secara mendalam cara kerja dompet HD Bitcoin. Kursus ini dirancang untuk siapa saja yang ingin memahami dasar teknis penggunaan Bitcoin, baik mereka pengguna kasual, penggemar yang terpelajar, atau calon ahli.

Tujuan dari pelatihan ini adalah untuk memberi Anda kunci untuk menguasai alat yang Anda gunakan setiap hari. Dompet HD Bitcoin, yang berada di jantung pengalaman pengguna Anda, didasarkan pada konsep-konsep yang terkadang kompleks, yang akan kami coba buat dapat diakses. Bersama-sama, kita akan membongkar misterinya!

Sebelum menyelami detail konstruksi dan operasi dompet Bitcoin, kita akan memulai dengan beberapa bab tentang primitif kriptografi yang perlu diketahui untuk apa yang akan diikuti.
Kita akan memulai dengan fungsi hash kriptografi, fundamental baik untuk dompet maupun protokol Bitcoin itu sendiri. Anda akan menemukan karakteristik utama mereka, fungsi spesifik yang digunakan dalam Bitcoin, dan dalam bab yang lebih teknis, Anda akan belajar secara detail tentang cara kerja fungsi hash ratu: SHA256.
![CYP201](assets/fr/010.webp)

Selanjutnya, kita akan membahas operasi algoritma tanda tangan digital yang Anda gunakan setiap hari untuk mengamankan UTXO Anda. Bitcoin menggunakan dua: ECDSA dan protokol Schnorr. Anda akan belajar primitif matematika apa yang mendasari algoritma ini dan bagaimana mereka memastikan keamanan transaksi.

![CYP201](assets/fr/021.webp)

Setelah kita memiliki pemahaman yang baik tentang elemen-elemen kriptografi ini, kita akhirnya akan beralih ke inti dari pelatihan: dompet yang deterministik dan hierarkis! Pertama, ada bagian yang didedikasikan untuk frasa mnemonik, urutan 12 atau 24 kata ini yang memungkinkan Anda untuk membuat dan memulihkan dompet Anda. Anda akan menemukan bagaimana kata-kata ini dihasilkan dari sumber entropi dan bagaimana mereka memfasilitasi penggunaan Bitcoin.

![CYP201](assets/fr/040.webp)
Pelatihan akan dilanjutkan dengan mempelajari passphrase BIP39, seed (jangan dikacaukan dengan frasa mnemonik), master chain code, dan master key. Kita akan melihat secara detail apa itu elemen-elemen tersebut, peran masing-masing, dan bagaimana mereka dihitung.
![CYP201](assets/fr/045.webp)

Akhirnya, dari master key, kita akan menemukan bagaimana pasangan kunci kriptografi diturunkan secara deterministik dan hierarkis hingga ke alamat penerima.

![CYP201](assets/fr/056.webp)

Pelatihan ini akan memungkinkan Anda untuk menggunakan perangkat lunak dompet Anda dengan percaya diri, sambil meningkatkan keterampilan Anda untuk mengidentifikasi dan mengurangi risiko. Bersiaplah untuk menjadi seorang ahli sejati dalam dompet Bitcoin!

# Fungsi Hash

<partId>3713fee1-2ec2-512e-9e97-b6da9e4d2f17</partId>

## Pengenalan Fungsi Hash

<chapterId>dba011f5-1805-5a48-ac2b-4bd637c93703</chapterId>

Jenis algoritma kriptografi pertama yang digunakan pada Bitcoin mencakup fungsi hash. Mereka memainkan peran penting pada berbagai tingkat protokol, tetapi juga dalam dompet Bitcoin. Mari kita temukan bersama apa itu fungsi hash dan untuk apa digunakan dalam Bitcoin.

### Definisi dan Prinsip Hashing

Hashing adalah proses yang mengubah informasi dengan panjang sembarang menjadi potongan informasi dengan panjang tetap melalui fungsi hash kriptografi. Dengan kata lain, fungsi hash mengambil input dengan ukuran berapa pun dan mengubahnya menjadi sidik jari berukuran tetap, yang disebut "hash".
Hash juga terkadang dapat disebut sebagai "digest", "condensate", "condensed", atau "hashed".

Sebagai contoh, fungsi hash SHA256 menghasilkan hash dengan panjang tetap 256 bit. Jadi, jika kita menggunakan input "_PlanB_", sebuah pesan dengan panjang sembarang, hash yang dihasilkan akan menjadi sidik jari 256-bit berikut:

```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```

![CYP201](assets/fr/001.webp)

### Karakteristik Fungsi Hash

Fungsi hash kriptografi ini memiliki beberapa karakteristik esensial yang membuatnya sangat berguna dalam konteks Bitcoin dan sistem komputer lainnya:

1. Irreversibilitas (atau resistensi terhadap pencarian gambar asli)
2. Resistensi terhadap perubahan (efek salju)
3. Resistensi terhadap tabrakan
4. Resistensi terhadap pencarian gambar asli kedua

#### 1. Irreversibilitas (resistensi terhadap pencarian gambar asli):

Irreversibilitas berarti mudah untuk menghitung hash dari informasi input, tetapi perhitungan terbalik, yaitu, menemukan input dari hash, praktis tidak mungkin. Sifat ini membuat fungsi hash sempurna untuk menciptakan sidik jari digital unik tanpa mengompromikan informasi asli. Karakteristik ini sering disebut sebagai fungsi satu arah atau "_fungsi pintu perangkap_".

Dalam contoh yang diberikan, mendapatkan hash `24f1b9…` dengan mengetahui input "_PlanB_" adalah hal yang sederhana dan cepat. Namun, menemukan pesan "_PlanB_" hanya dengan mengetahui `24f1b9…` adalah hal yang mustahil.

![CYP201](assets/fr/002.webp)

Oleh karena itu, tidak mungkin menemukan preimage $m$ untuk hash $h$ sedemikian rupa sehingga $h = \text{HASH}(m)$, di mana $\text{HASH}$ adalah fungsi hash kriptografi.

#### 2. Resistensi terhadap perubahan (efek salju)

Karakteristik kedua adalah ketahanan terhadap perubahan, juga dikenal sebagai **efek longsoran**. Karakteristik ini diamati pada fungsi hash jika perubahan kecil pada pesan masukan menghasilkan perubahan radikal pada hash keluaran.

Jika kita kembali ke contoh kita dengan masukan "_PlanB_" dan fungsi SHA256, kita telah melihat bahwa hash yang dihasilkan adalah sebagai berikut:

```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```

Jika kita membuat perubahan yang sangat kecil pada masukan dengan menggunakan "_Planb_" kali ini, maka hanya mengubah "B" besar menjadi "b" kecil sepenuhnya mengubah hash keluaran SHA256:

```text
bb038b4503ac5d90e1205788b00f8f314583c5e22f72bec84b8735ba5a36df3f
```

![CYP201](assets/fr/003.webp)

Properti ini memastikan bahwa bahkan perubahan kecil dari pesan asli segera terdeteksi, karena tidak hanya mengubah bagian kecil dari hash, tetapi seluruh hash. Ini bisa menjadi menarik di berbagai bidang untuk memverifikasi integritas pesan, perangkat lunak, atau bahkan transaksi Bitcoin.

#### 3. Ketahanan terhadap Tabrakan

Karakteristik ketiga adalah ketahanan terhadap tabrakan. Fungsi hash dikatakan tahan tabrakan jika secara komputasi tidak mungkin menemukan 2 pesan berbeda yang menghasilkan hash keluaran yang sama dari fungsi tersebut. Secara formal, sulit untuk menemukan dua pesan berbeda $m_1$ dan $m_2$ sedemikian sehingga:

$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$

![CYP201](assets/fr/004.webp)

Dalam kenyataannya, secara matematis tidak terelakkan bahwa tabrakan ada untuk fungsi hash, karena ukuran input bisa lebih besar dari ukuran output. Ini dikenal sebagai prinsip laci Dirichlet: jika $n$ objek didistribusikan ke dalam $m$ laci, dengan $m < n$, maka setidaknya satu laci akan pasti berisi dua atau lebih objek. Untuk fungsi hash, prinsip ini berlaku karena jumlah pesan yang mungkin adalah (hampir) tak terbatas, sementara jumlah hash yang mungkin adalah terbatas ($2^{256}$ dalam kasus SHA256).

Dengan demikian, karakteristik ini tidak berarti bahwa tidak ada tabrakan untuk fungsi hash, tetapi lebih kepada fungsi hash yang baik membuat probabilitas menemukan tabrakan menjadi dapat diabaikan. Karakteristik ini, misalnya, tidak lagi diverifikasi pada algoritma SHA-0 dan SHA-1, pendahulu SHA-2, yang mana tabrakan telah ditemukan. Fungsi-fungsi ini oleh karena itu sekarang disarankan untuk dihindari dan sering dianggap usang.
Untuk fungsi hash $n$ bit, ketahanan terhadap tabrakan adalah sebesar $2^{\frac{n}{2}}$, sesuai dengan serangan ulang tahun. Misalnya, untuk SHA256 ($n = 256$), kompleksitas menemukan tabrakan adalah sebesar $2^{128}$ percobaan. Dalam praktiknya, ini berarti jika seseorang melewati $2^{128}$ pesan berbeda melalui fungsi tersebut, seseorang kemungkinan akan menemukan tabrakan.

#### 4. Ketahanan terhadap Preimage Kedua

Ketahanan terhadap preimage kedua adalah karakteristik penting lainnya dari fungsi hash. Ini menyatakan bahwa diberikan sebuah pesan $m_1$ dan hashnya $h$, secara komputasi tidak mungkin untuk menemukan pesan lain $m_2 \neq m_1$ sedemikian sehingga:

$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$

Oleh karena itu, ketahanan terhadap preimage kedua agak mirip dengan ketahanan terhadap tabrakan, kecuali di sini, serangannya lebih sulit karena penyerang tidak dapat bebas memilih $m_1$.

### Aplikasi Fungsi Hash dalam Bitcoin

Fungsi hash yang paling banyak digunakan dalam Bitcoin adalah **SHA256** ("_Secure Hash Algorithm 256 bits"_). Dirancang pada awal tahun 2000-an oleh NSA dan distandarisasi oleh NIST, fungsi ini menghasilkan output hash 256-bit.

Fungsi ini digunakan dalam banyak aspek Bitcoin. Di tingkat protokol, ia terlibat dalam mekanisme Proof-of-Work, di mana ia diterapkan dalam penghashan ganda untuk mencari tabrakan parsial antara header blok kandidat, yang dibuat oleh penambang, dan target kesulitan. Jika tabrakan parsial ini ditemukan, blok kandidat menjadi valid dan dapat ditambahkan ke blockchain.

SHA256 juga digunakan dalam pembangunan pohon Merkle, yang merupakan akumulator yang digunakan untuk mencatat transaksi dalam blok. Struktur ini juga ditemukan dalam protokol Utreexo, yang memungkinkan pengurangan ukuran Set UTXO. Selain itu, dengan pengenalan Taproot pada tahun 2021, SHA256 dimanfaatkan dalam MAST (_Merkelised Alternative Script Tree_), yang memungkinkan hanya kondisi pengeluaran yang benar-benar digunakan dalam skrip yang diungkapkan, tanpa mengungkapkan opsi lain yang mungkin. Fungsi ini juga digunakan dalam perhitungan identifikasi transaksi, dalam transmisi paket melalui jaringan P2P, dalam tanda tangan elektronik... Akhirnya, dan ini sangat menarik dalam pelatihan ini, SHA256 digunakan di tingkat aplikasi untuk pembangunan dompet Bitcoin dan derivasi alamat.

Sebagian besar waktu, ketika Anda menemukan penggunaan SHA256 pada Bitcoin, itu sebenarnya akan menjadi hash ganda SHA256, dicatat sebagai "**HASH256**", yang hanya terdiri dari menerapkan SHA256 dua kali secara berturut-turut:
HASH256(m) = SHA256(SHA256(m))

Praktik penghashan ganda ini menambahkan lapisan keamanan ekstra terhadap serangan potensial tertentu, meskipun SHA256 hari ini dianggap aman secara kriptografis.

Fungsi hashing lain yang tersedia dalam bahasa Script dan digunakan untuk menghasilkan alamat penerima adalah fungsi RIPEMD160. Fungsi ini menghasilkan hash 160-bit (jadi lebih pendek dari SHA256). Umumnya dikombinasikan dengan SHA256 untuk membentuk fungsi HASH160:

$$
\text{HASH160}(m) = \text{RIPEMD160}(\text{SHA256}(m))
$$

Kombinasi ini digunakan untuk menghasilkan hash yang lebih pendek, terutama dalam pembuatan alamat Bitcoin tertentu yang mewakili hash dari kunci atau hash skrip, serta untuk menghasilkan sidik jari kunci.

Akhirnya, hanya di tingkat aplikasi, fungsi SHA512 terkadang juga digunakan, yang secara tidak langsung berperan dalam derivasi kunci untuk dompet. Fungsi ini sangat mirip dengan SHA256 dalam operasinya; keduanya termasuk dalam keluarga SHA2 yang sama, tetapi SHA512 menghasilkan, seperti namanya, hash 512-bit, dibandingkan dengan 256 bit untuk SHA256. Kita akan merinci penggunaannya dalam bab-bab berikut.

Anda sekarang mengetahui dasar-dasar esensial tentang fungsi hashing untuk apa yang akan diikuti. Dalam bab berikutnya, saya mengusulkan untuk menemukan lebih detail tentang fungsi yang merupakan inti dari Bitcoin: SHA256. Kita akan membedahnya untuk memahami bagaimana ia mencapai karakteristik yang telah kita deskripsikan di sini. Bab berikutnya cukup panjang dan teknis, tetapi tidak esensial untuk mengikuti sisa pelatihan. Jadi, jika Anda kesulitan memahaminya, jangan khawatir dan langsung saja ke bab berikutnya, yang akan jauh lebih mudah diakses.

## Cara Kerja SHA256

<chapterId>905eb320-f15b-5fb6-8d2d-5bb447337deb</chapterId>
Kita telah sebelumnya melihat bahwa fungsi hashing memiliki karakteristik penting yang membenarkan penggunaannya pada Bitcoin. Mari kita sekarang periksa mekanisme internal dari fungsi hashing ini yang memberikan mereka sifat-sifat tersebut, dan untuk melakukan ini, saya mengusulkan untuk membedah operasi dari SHA256.
Fungsi SHA256 dan SHA512 termasuk dalam keluarga SHA2 yang sama. Mekanisme mereka berdasarkan pada konstruksi spesifik yang disebut **Merkle-Damgård construction**. RIPEMD160 juga menggunakan jenis konstruksi yang sama.

Sebagai pengingat, kita memiliki pesan berukuran sembarang sebagai input ke SHA256, dan kita akan melewatinya melalui fungsi untuk mendapatkan hash 256-bit sebagai output.

### Pra-pemrosesan input

Untuk memulai, kita perlu menyiapkan pesan input $m$ kita sehingga memiliki panjang standar yang merupakan kelipatan dari 512 bit. Langkah ini sangat penting untuk fungsi algoritma selanjutnya.
Untuk melakukan ini, kita mulai dengan langkah bit padding. Kita pertama menambahkan bit pemisah `1` ke pesan, diikuti oleh sejumlah bit `0`. Jumlah bit `0` yang ditambahkan dihitung sehingga total panjang pesan setelah penambahan ini kongruen dengan 448 modulo 512. Dengan demikian, panjang $L$ dari pesan dengan bit padding adalah sama dengan:

$$
L \equiv 448 \mod 512
$$

$\text{mod}$, untuk modulo, adalah operasi matematika yang, antara dua bilangan bulat, mengembalikan sisa dari pembagian Euklides dari yang pertama oleh yang kedua. Misalnya: $16 \mod 5 = 1$. Ini adalah operasi yang banyak digunakan dalam kriptografi.

Di sini, langkah padding memastikan bahwa, setelah menambahkan 64 bit pada langkah berikutnya, total panjang pesan yang disejajarkan akan menjadi kelipatan dari 512 bit. Jika pesan awal memiliki panjang $M$ bit, jumlah ($N$) bit `0` yang akan ditambahkan adalah:

$$
N = (448 - (M + 1) \mod 512) \mod 512
$$

Misalnya, jika pesan awal adalah 950 bit, perhitungannya akan sebagai berikut:

$$
\begin{align*}
M & = 950 \\
M + 1 & = 951 \\
(M + 1) \mod 512 & = 951 \mod 512 \\
& = 951 - 512 \cdot \left\lfloor \frac{951}{512} \right\rfloor \\
& = 951 - 512 \cdot 1 \\
& = 951 - 512 \\
& = 439 \\
\\
448 - (M + 1) \mod 512 & = 448 - 439 \\
& = 9 \\
\\
N & = (448 - (M + 1) \mod 512) \mod 512 \\
N & = 9 \mod 512 \\
& = 9
\end{align*}
$$

Dengan demikian, kita akan memiliki 9 bit `0` tambahan selain pemisah `1`. Bit padding kita yang akan ditambahkan langsung setelah pesan $M$ kita akan menjadi:

```text
1000 0000 00
```

Setelah menambahkan bit padding ke pesan $M$ kita, kita juga menambahkan representasi 64-bit dari panjang asli pesan $M$, yang dinyatakan dalam biner. Ini memungkinkan fungsi hash untuk sensitif terhadap urutan bit dan panjang pesan.
Jika kita kembali ke contoh kita dengan pesan awal sebesar 950 bit, kita mengubah angka desimal `950` menjadi biner, yang memberikan kita `1110 1101 10`. Kita melengkapi angka ini dengan nol di dasar untuk membuat total 64 bit. Dalam contoh kita, ini memberikan:

```text
0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0011 1011 0110
```

Ukuran padding ini ditambahkan mengikuti padding bit. Oleh karena itu, pesan setelah pra-pemrosesan kita terdiri dari tiga bagian:

1. Pesan asli $M$;
2. Sebuah bit `1` diikuti oleh beberapa bit `0` untuk membentuk padding bit;
3. Representasi 64-bit dari panjang $M$ untuk membentuk padding dengan ukuran.

![CYP201](assets/fr/006.webp)

### Inisialisasi Variabel

SHA256 menggunakan delapan variabel keadaan awal, yang ditandai $A$ sampai $H$, masing-masing 32 bit. Variabel-variabel ini diinisialisasi dengan konstanta spesifik, yang merupakan bagian pecahan dari akar kuadrat dari delapan bilangan prima pertama. Kita akan menggunakan nilai-nilai ini selanjutnya selama proses hashing:

- $A = 0x6a09e667$
- $B = 0xbb67ae85$
- $C = 0x3c6ef372$
- $D = 0xa54ff53a$
- $E = 0x510e527f$
- $F = 0x9b05688c$
- $G = 0x1f83d9ab$
- $H = 0x5be0cd19$

SHA256 juga menggunakan 64 konstanta lainnya, yang ditandai $K_0$ sampai $K_{63}$, yang merupakan bagian pecahan dari akar kubik dari 64 bilangan prima pertama:

$$
K[0 \ldots 63] = \begin{pmatrix}
0x428a2f98, & 0x71374491, & 0xb5c0fbcf, & 0xe9b5dba5, \\
0x3956c25b, & 0x59f111f1, & 0x923f82a4, & 0xab1c5ed5, \\
0xd807aa98, & 0x12835b01, & 0x243185be, & 0x550c7dc3, \\
0x72be5d74, & 0x80deb1fe, & 0x9bdc06a7, & 0xc19bf174, \\
0xe49b69c1, & 0xefbe4786, & 0x0fc19dc6, & 0x240ca1cc, \\
0x2de92c6f, & 0x4a7484aa, & 0x5cb0a9dc, & 0x76f988da, \\
0x983e5152, & 0xa831c66d, & 0xb00327c8, & 0xbf597fc7, \\
0xc6e00bf3, & 0xd5a79147, & 0x06ca6351, & 0x14292967, \\
0x27b70a85, & 0x2e1b2138, & 0x4d2c6dfc, & 0x53380d13, \\
0x650a7354, & 0x766a0abb, & 0x81c2c92e, & 0x92722c85, \\
0xa2bfe8a1, & 0xa81a664b, & 0xc24b8b70, & 0xc76c51a3, \\
0xd192e819, & 0xd6990624, & 0xf40e3585, & 0x106aa070, \\
0x19a4c116, & 0x1e376c08, & 0x2748774c, & 0x34b0bcb5, \\
0x391c0cb3, & 0x4ed8aa4a, & 0x5b9cca4f, & 0x682e6ff3, \\
0x748f82ee, & 0x78a5636f, & 0x84c87814, & 0x8cc70208, \\
0x90befffa, & 0xa4506ceb, & 0xbef9a3f7, & 0xc67178f2
\end{pmatrix}
$$

### Pembagian Input

Setelah kita memiliki input yang diseimbangkan, kita akan beralih ke fase pemrosesan utama dari algoritma SHA256: fungsi kompresi. Langkah ini sangat penting, karena inilah yang memberikan fungsi hash sifat kriptografis yang telah kita pelajari di bab sebelumnya.

Pertama, kita mulai dengan membagi pesan yang telah diseimbangkan (hasil dari langkah-langkah pra-pemrosesan) menjadi beberapa blok $P$ sebesar 512 bit masing-masing. Jika pesan yang diseimbangkan kita memiliki ukuran total $n \times 512$ bit, kita akan memiliki $n$ blok, masing-masing sebesar 512 bit. Setiap blok 512-bit akan diproses secara individual oleh fungsi kompresi, yang terdiri dari 64 ronde operasi berturut-turut. Mari kita namai blok-blok ini $P_1$, $P_2$, $P_3$...

### Operasi Logika

Sebelum menjelajahi fungsi kompresi secara detail, penting untuk memahami operasi logika dasar yang digunakan di dalamnya. Operasi-operasi ini, berdasarkan aljabar Boolean, beroperasi pada level bit. Operasi logika dasar yang digunakan adalah:

- **Konjungsi (AND)**: ditandai $\land$, sesuai dengan logika "DAN".
- **Disjungsi (OR)**: ditandai $\lor$, sesuai dengan logika "ATAU".
- **Negasi (NOT)**: ditandai $\lnot$, sesuai dengan logika "TIDAK".

Dari operasi dasar ini, kita dapat mendefinisikan operasi yang lebih kompleks, seperti "Exclusive OR" (XOR) yang ditandai $\oplus$, yang banyak digunakan dalam kriptografi.
Setiap operasi logika dapat diwakili oleh tabel kebenaran, yang menunjukkan hasil untuk semua kombinasi nilai input biner yang mungkin (dua operand $p$ dan $q$).
Untuk XOR ($\oplus$):

| $p$ | $q$ | $p \oplus q$ |
| --- | --- | ------------ |
| 0   | 0   | 0            |
| 0   | 1   | 1            |
| 1   | 0   | 1            |
| 1   | 1   | 0            |

Untuk AND ($\land$):

| $p$ | $q$ | $p \land q$ |
| --- | --- | ----------- |
| 0   | 0   | 0           |
| 0   | 1   | 0           |
| 1   | 0   | 0           |
| 1   | 1   | 1           |

Untuk NOT ($\lnot p$):

| $p$ | $\lnot p$ |
| --- | --------- |
| 0   | 1         |
| 1   | 0         |

Mari kita ambil contoh untuk memahami operasi XOR pada level bit. Jika kita memiliki dua angka biner pada 6 bit:

- $a = 101100$
- $b = 001000$

Maka:

$$
a \oplus b = 101100 \oplus 001000 = 100100
$$

Dengan menerapkan XOR bit demi bit:

| Posisi Bit | $a$ | $b$ | $a \oplus b$ |
| ---------- | --- | --- | ------------ |
| 1          | 1   | 0   | 1            |
| 2          | 0   | 0   | 0            |
| 3          | 1   | 1   | 0            |
| 4          | 1   | 0   | 1            |
| 5          | 0   | 0   | 0            |
| 6          | 0   | 0   | 0            |

Hasilnya adalah $100100$.

Selain operasi logika, fungsi kompresi menggunakan operasi bit-shifting, yang akan memainkan peran penting dalam penyebaran bit dalam algoritma.

Pertama, ada operasi shift kanan logis, ditandai $ShR_n(x)$, yang menggeser semua bit dari $x$ ke kanan sebanyak $n$ posisi, mengisi bit kosong di kiri dengan nol.

Sebagai contoh, untuk $x = 101100001$ (pada 9 bit) dan $n = 4$:

$$
ShR_4(101100001) = 000010110
$$

Secara skematis, operasi shift kanan dapat dilihat seperti ini:

![CYP201](assets/fr/007.webp)
Operasi lain yang digunakan dalam SHA256 untuk manipulasi bit adalah rotasi kanan sirkular, ditandai $RotR_n(x)$, yang menggeser bit dari $x$ ke kanan sebanyak $n$ posisi, memasukkan kembali bit yang digeser ke awal string.
Sebagai contoh, untuk $x = 101100001$ (lebih dari 9 bit) dan $n = 4$:

$$
RotR_4(101100001) = 000110110
$$

Secara skematis, operasi shift kanan sirkular dapat dilihat seperti ini:

![CYP201](assets/fr/008.webp)

### Fungsi Kompresi

Sekarang setelah kita memahami operasi dasar, mari kita periksa fungsi kompresi SHA256 secara detail.

Pada langkah sebelumnya, kita membagi input kita menjadi beberapa bagian 512-bit $P$. Untuk setiap blok 512-bit $P$, kita memiliki:

- **Kata pesan $W_i$**: untuk $i$ dari 0 sampai 63.
- **Konstanta $K_i$**: untuk $i$ dari 0 sampai 63, didefinisikan pada langkah sebelumnya.
- **Variabel status $A, B, C, D, E, F, G, H$**: diinisialisasi dengan nilai dari langkah sebelumnya.
  16 kata pertama, $W_0$ hingga $W_{15}$, diambil langsung dari blok 512-bit yang diproses $P$. Setiap kata $W_i$ terdiri dari 32 bit berturut-turut dari blok tersebut. Jadi, sebagai contoh, kita mengambil potongan input pertama kita $P_1$, dan kita membaginya lebih lanjut menjadi potongan-potongan 32-bit yang kita sebut kata.

48 kata berikutnya ($W_{16}$ hingga $W_{63}$) dihasilkan menggunakan rumus berikut:

$$
W_i = W_{i-16} + \sigma_0(W_{i-15}) + W_{i-7} + \sigma_1(W_{i-2}) \mod 2^{32}
$$

Dengan:

- $\sigma_0(x) = RotR_7(x) \oplus RotR_{18}(x) \oplus ShR_3(x)$
- $\sigma_1(x) = RotR_{17}(x) \oplus RotR_{19}(x) \oplus ShR_{10}(x)$

Dalam kasus ini, $x$ sama dengan $W_{i-15}$ untuk $\sigma_0(x)$ dan $W_{i-2}$ untuk $\sigma_1(x)$.

Setelah kita menentukan semua kata $W_i$ untuk potongan 512-bit kita, kita dapat melanjutkan ke fungsi kompresi, yang terdiri dari melakukan 64 ronde.

![CYP201](assets/fr/009.webp)
Untuk setiap ronde $i$ dari 0 hingga 63, kita memiliki tiga jenis input yang berbeda. Pertama, $W_i$ yang baru saja kita tentukan, sebagian terdiri dari potongan pesan kita $P_n$. Selanjutnya, 64 konstanta $K_i$. Akhirnya, kita menggunakan variabel-variabel state $A$, $B$, $C$, $D$, $E$, $F$, $G$, dan $H$, yang akan berkembang sepanjang proses hashing dan dimodifikasi dengan setiap fungsi kompresi. Namun, untuk potongan pertama $P_1$, kita menggunakan konstanta awal yang diberikan sebelumnya.
Kemudian kita melakukan operasi berikut pada input kita:

- **Fungsi $\Sigma_0$:**

$$
\Sigma_0(A) = RotR_2(A) \oplus RotR_{13}(A) \oplus RotR_{22}(A)
$$

- **Fungsi $\Sigma_1$:**

$$
\Sigma_1(E) = RotR_6(E) \oplus RotR_{11}(E) \oplus RotR_{25}(E)
$$

- **Fungsi $Ch$ ("_Pilih_"):**

$$
Ch(E, F, G) = (E \land F) \oplus (\lnot E \land G)
$$

- **Fungsi $Maj$ ("_Mayoritas_"):**

$$
Maj(A, B, C) = (A \land B) \oplus (A \land C) \oplus (B \land C)
$$

Kemudian kita menghitung 2 variabel sementara:

- $temp1$:

$$
temp1 = H + \Sigma_1(E) + Ch(E, F, G) + K_i + W_i \mod 2^{32}
$$

- $temp2$:

$$
temp2 = \Sigma_0(A) + Maj(A, B, C) \mod 2^{32}
$$

Selanjutnya, kita memperbarui variabel-variabel state sebagai berikut:

$$
\begin{cases}
H = G \\
G = F \\
F = E \\
E = D + temp1 \mod 2^{32} \\
D = C \\
C = B \\
B = A \\
A = temp1 + temp2 \mod 2^{32}
\end{cases}
$$

Diagram berikut mewakili satu putaran dari fungsi kompresi SHA256 seperti yang baru saja kita jelaskan:

![CYP201](assets/fr/010.webp)

- Panah menunjukkan aliran data;
- Kotak mewakili operasi yang dilakukan;
- $+$ yang dikelilingi mewakili penambahan modulo $2^{32}$.

Kita dapat mengamati bahwa putaran ini menghasilkan variabel-variabel keadaan baru $A$, $B$, $C$, $D$, $E$, $F$, $G$, dan $H$. Variabel-variabel baru ini akan berfungsi sebagai input untuk putaran berikutnya, yang pada gilirannya akan menghasilkan variabel-variabel baru $A$, $B$, $C$, $D$, $E$, $F$, $G$, dan $H$, untuk digunakan pada putaran berikutnya. Proses ini berlanjut hingga putaran ke-64.
Setelah 64 putaran, kita memperbarui nilai-nilai awal dari variabel-variabel keadaan dengan menambahkannya ke nilai-nilai akhir di akhir putaran ke-64:

$$
\begin{cases}
A = A_{\text{initial}} + A \mod 2^{32} \\
B = B_{\text{initial}} + B \mod 2^{32} \\
C = C_{\text{initial}} + C \mod 2^{32} \\
D = D_{\text{initial}} + D \mod 2^{32} \\
E = E_{\text{initial}} + E \mod 2^{32} \\
F = F_{\text{initial}} + F \mod 2^{32} \\
G = G_{\text{initial}} + G \mod 2^{32} \\
H = H_{\text{initial}} + H \mod 2^{32}
\end{cases}

$$

Nilai-nilai baru dari $A$, $B$, $C$, $D$, $E$, $F$, $G$, dan $H$ ini akan berfungsi sebagai nilai-nilai awal untuk blok berikutnya, $P_2$. Untuk blok $P_2$ ini, kita mereplikasi proses kompresi yang sama dengan 64 putaran, kemudian kita memperbarui variabel-variabel untuk blok $P_3$, dan seterusnya hingga blok terakhir dari input kita yang telah diseimbangkan.

Setelah memproses semua blok pesan, kita menggabungkan nilai-nilai akhir dari variabel-variabel $A$, $B$, $C$, $D$, $E$, $F$, $G$, dan $H$ untuk membentuk hash akhir 256-bit dari fungsi hashing kita:


$$

\text{Hash} = A \Vert B \Vert C \Vert D \Vert E \Vert F \Vert G \Vert H

$$

Setiap variabel adalah integer 32-bit, sehingga penggabungan mereka selalu menghasilkan hasil 256-bit, terlepas dari ukuran input pesan kita ke fungsi hashing.

### Justifikasi Properti Kriptografi

Lalu, bagaimana fungsi ini tidak dapat dibalikkan, tahan terhadap tabrakan, dan tahan terhadap perubahan?

Untuk ketahanan terhadap perubahan, cukup mudah untuk dipahami. Ada begitu banyak perhitungan yang dilakukan secara berurutan, yang bergantung baik pada input maupun konstanta, sehingga perubahan terkecil pada pesan awal sepenuhnya mengubah jalur yang diambil, dan dengan demikian sepenuhnya mengubah hash output. Ini adalah apa yang disebut efek salju. Properti ini sebagian dijamin oleh pencampuran keadaan-keadaan antara dengan keadaan-keadaan awal untuk setiap bagian.
Selanjutnya, ketika membahas fungsi hash kriptografi, istilah "irreversibility" umumnya tidak digunakan. Sebaliknya, kita berbicara tentang "preimage resistance," yang menentukan bahwa untuk setiap $y$ yang diberikan, sulit untuk menemukan $x$ sedemikian sehingga $h(x) = y$. Preimage resistance ini dijamin oleh kompleksitas aljabar dan non-linearitas kuat dari operasi yang dilakukan dalam fungsi kompresi, serta oleh kehilangan informasi tertentu dalam proses tersebut. Sebagai contoh, untuk hasil penambahan modulo yang diberikan, ada beberapa operan yang mungkin:$$
3+2 \mod 10 = 5 \\
7+8 \mod 10 = 5 \\
5+10 \mod 10 = 5
$$

Dalam contoh ini, hanya dengan mengetahui modulo yang digunakan (10) dan hasilnya (5), seseorang tidak dapat menentukan dengan pasti operan mana yang benar digunakan dalam penambahan. Dikatakan bahwa ada beberapa kongruensi modulo 10.

Untuk operasi XOR, kita dihadapkan pada masalah yang sama. Ingatlah tabel kebenaran untuk operasi ini: setiap output 1-bit dapat ditentukan oleh dua konfigurasi input yang berbeda yang memiliki kemungkinan yang sama persis untuk menjadi nilai yang benar. Oleh karena itu, seseorang tidak dapat menentukan dengan pasti operan dari sebuah XOR hanya dengan mengetahui hasilnya. Jika kita meningkatkan ukuran operan XOR, jumlah input yang mungkin hanya dengan mengetahui hasilnya meningkat secara eksponensial. Selain itu, XOR sering digunakan bersama dengan operasi tingkat bit lainnya, seperti operasi $\text{RotR}$, yang menambahkan lebih banyak interpretasi yang mungkin terhadap hasilnya.

Fungsi kompresi juga menggunakan operasi $\text{ShR}$. Operasi ini menghilangkan sebagian informasi dasar, yang kemudian tidak mungkin untuk diambil kembali. Sekali lagi, tidak ada cara aljabar untuk membalikkan operasi ini. Semua operasi satu arah dan kehilangan informasi ini digunakan sangat sering dalam fungsi kompresi. Jumlah input yang mungkin untuk sebuah output hampir tak terbatas, dan setiap upaya perhitungan balik akan menghasilkan persamaan dengan jumlah yang tidak diketahui sangat tinggi, yang akan meningkat secara eksponensial pada setiap langkahnya.

Akhirnya, untuk karakteristik tahan benturan (collision resistance), beberapa parameter berperan. Pra-pemrosesan pesan asli memainkan peran penting. Tanpa pra-pemrosesan ini, mungkin lebih mudah untuk menemukan benturan pada fungsi tersebut. Meskipun, secara teoritis, benturan ada (karena prinsip pigeonhole), struktur fungsi hash, dikombinasikan dengan sifat-sifat yang disebutkan di atas, membuat kemungkinan menemukan benturan sangat rendah.
Agar sebuah fungsi hash tahan benturan, sangat penting bahwa:

- Outputnya tidak dapat diprediksi: Setiap kemungkinan prediksi dapat dimanfaatkan untuk menemukan benturan lebih cepat daripada dengan serangan brute force. Fungsi tersebut memastikan bahwa setiap bit dari output bergantung pada input dengan cara yang tidak trivial. Dengan kata lain, fungsi tersebut dirancang sehingga setiap bit dari hasil akhir memiliki probabilitas independen untuk menjadi 0 atau 1, meskipun kemandirian ini tidak absolut dalam praktiknya.
- Distribusi hash adalah pseudo-random: Ini memastikan bahwa hash didistribusikan secara seragam.
- Ukuran hash adalah substansial: semakin besar ruang yang mungkin untuk hasil, semakin sulit untuk menemukan benturan.

Kriptografer merancang fungsi-fungsi ini dengan mengevaluasi serangan terbaik yang mungkin untuk menemukan benturan, kemudian menyesuaikan parameter untuk membuat serangan ini tidak efektif.

### Konstruksi Merkle-Damgård

Struktur SHA256 didasarkan pada konstruksi Merkle-Damgård, yang memungkinkan transformasi fungsi kompresi menjadi fungsi hash yang dapat memproses pesan dengan panjang sembarang. Inilah yang telah kita lihat dalam bab ini.
Namun, beberapa fungsi hash lama seperti SHA1 atau MD5, yang menggunakan konstruksi spesifik ini, rentan terhadap serangan perpanjangan panjang. Ini adalah teknik yang memungkinkan penyerang yang mengetahui hash dari sebuah pesan $M$ dan panjang dari $M$ (tanpa mengetahui pesan itu sendiri) untuk menghitung hash dari pesan $M'$ yang terbentuk dengan menggabungkan $M$ dengan konten tambahan.
SHA256, meskipun menggunakan jenis konstruksi yang sama, secara teoritis tahan terhadap jenis serangan ini, tidak seperti SHA1 dan MD5. Ini mungkin menjelaskan misteri dari penggunaan double hashing yang diimplementasikan oleh Satoshi Nakamoto di seluruh Bitcoin. Untuk menghindari jenis serangan ini, Satoshi mungkin lebih memilih menggunakan double SHA256:

$$
\text{HASH256}(m) = \text{SHA256}(\text{SHA256}(m))
$$

Ini meningkatkan keamanan terhadap serangan potensial yang terkait dengan konstruksi Merkle-Damgård, tetapi tidak meningkatkan keamanan proses hashing dalam hal resistensi terhadap tabrakan. Selain itu, meskipun SHA256 telah rentan terhadap jenis serangan ini, hal itu tidak akan memiliki dampak serius, karena semua kasus penggunaan fungsi hash di Bitcoin melibatkan data publik. Namun, serangan perpanjangan panjang mungkin hanya berguna bagi penyerang jika data yang di-hash bersifat pribadi dan pengguna telah menggunakan fungsi hash sebagai mekanisme otentikasi untuk data tersebut, mirip dengan MAC. Dengan demikian, implementasi double hashing tetap menjadi misteri dalam desain Bitcoin.
Sekarang setelah kita telah melihat secara detail tentang cara kerja fungsi hash, khususnya SHA256, yang digunakan secara luas di Bitcoin, kita akan lebih fokus pada algoritma derivasi kriptografis yang digunakan pada level aplikasi, terutama untuk menghasilkan kunci untuk dompet Anda.

## Algoritma yang digunakan untuk derivasi

<chapterId>cc668121-7789-5e99-bf5e-1ba085f4f5f2</chapterId>

Di Bitcoin pada level aplikasi, selain fungsi hash, algoritma derivasi kriptografis digunakan untuk menghasilkan data aman dari input awal. Meskipun algoritma ini bergantung pada fungsi hash, mereka melayani tujuan yang berbeda, terutama dalam hal otentikasi dan generasi kunci. Algoritma ini mempertahankan beberapa karakteristik dari fungsi hash, seperti tidak dapat dibalik, resistensi terhadap perubahan, dan resistensi tabrakan.

Pada dompet Bitcoin, terutama 2 algoritma derivasi digunakan:

1. **HMAC (_Hash-based Message Authentication Code_)**
2. **PBKDF2 (_Password-Based Key Derivation Function 2_)**

Kita akan menjelajahi bersama fungsi dan peran masing-masing dari mereka.

### HMAC-SHA512

HMAC adalah algoritma kriptografis yang menghitung kode otentikasi berdasarkan kombinasi dari fungsi hash dan kunci rahasia. Bitcoin menggunakan HMAC-SHA512, varian dari HMAC yang menggunakan fungsi hash SHA512. Kami telah melihat di bab sebelumnya bahwa SHA512 adalah bagian dari keluarga fungsi hash yang sama dengan SHA256, tetapi menghasilkan output 512-bit.

Berikut adalah skema operasional umumnya dengan $m$ sebagai pesan input dan $K$ sebagai kunci rahasia:

![CYP201](assets/fr/011.webp)

Mari kita pelajari lebih detail apa yang terjadi di dalam kotak hitam HMAC-SHA512 ini. Fungsi HMAC-SHA512 dengan:

- $m$: pesan berukuran sembarang yang dipilih oleh pengguna (input pertama);
- $K$: kunci rahasia sembarang yang dipilih oleh pengguna (input kedua);
- $K'$: kunci $K$ disesuaikan dengan ukuran $B$ dari blok fungsi hash (1024 bit untuk SHA512, atau 128 byte);
- $\text{SHA512}$: fungsi hash SHA512;
- $\oplus$: operasi XOR (exclusive or).
- $\Vert$: operator konkatenasi, menghubungkan string bit ujung-ke-ujung;
- $\text{opad}$: konstanta yang terdiri dari byte $0x5c$ yang diulang 128 kali
- $\text{ipad}$: konstanta yang terdiri dari byte $0x36$ yang diulang 128 kali
  Sebelum menghitung HMAC, perlu untuk menyamakan kunci dan konstanta sesuai dengan ukuran blok $B$. Sebagai contoh, jika kunci $K$ lebih pendek dari 128 byte, maka akan ditambahkan nol hingga mencapai ukuran $B$. Jika $K$ lebih panjang dari 128 byte, maka akan dikompres menggunakan SHA512, dan kemudian ditambahkan nol hingga mencapai 128 byte. Dengan cara ini, diperoleh kunci yang disamakan bernama $K'$.
  Nilai dari $\text{opad}$ dan $\text{ipad}$ diperoleh dengan mengulangi byte dasar mereka ($0x5c$ untuk $\text{opad}$, $0x36$ untuk $\text{ipad}$) hingga ukuran $B$ tercapai. Dengan demikian, dengan $B = 128$ byte, kita memiliki:

$$
\text{opad} = \underbrace{0x5c5c\ldots5c}_{128 \, \text{bytes}}
$$

Setelah pra-pemrosesan selesai, algoritma HMAC-SHA512 didefinisikan oleh persamaan berikut:

$$
\text {HMAC-SHA512}_K(m) = \text{SHA512} \left( (K' \oplus \text{opad}) \parallel \text{SHA512} \left( (K' \oplus \text{ipad}) \parallel m \right) \right)
$$

Persamaan ini dipecah menjadi langkah-langkah berikut:

1. XOR kunci yang disesuaikan $K'$ dengan $\text{ipad}$ untuk mendapatkan $\text{iKpad}$;
2. XOR kunci yang disesuaikan $K'$ dengan $\text{opad}$ untuk mendapatkan $\text{oKpad}$;
3. Menggabungkan $\text{iKpad}$ dengan pesan $m$.
4. Hash hasil ini dengan SHA512 untuk mendapatkan hash sementara $H_1$.
5. Menggabungkan $\text{oKpad}$ dengan $H_1$.
6. Hash hasil ini dengan SHA512 untuk mendapatkan hasil akhir $H_2$.

Langkah-langkah ini dapat diringkas secara skematis sebagai berikut:

![CYP201](assets/fr/012.webp)

HMAC digunakan dalam Bitcoin terutama untuk derivasi kunci dalam dompet HD (Hierarchical Deterministic) (kita akan membahas ini lebih detail di bab-bab mendatang) dan sebagai komponen dari PBKDF2.

### PBKDF2

PBKDF2 (_Password-Based Key Derivation Function 2_) adalah algoritma derivasi kunci yang dirancang untuk meningkatkan keamanan kata sandi. Algoritma ini menerapkan fungsi pseudo-random (di sini HMAC-SHA512) pada kata sandi dan garam kriptografi, dan kemudian mengulangi operasi ini sejumlah kali tertentu untuk menghasilkan kunci keluaran.

Dalam Bitcoin, PBKDF2 digunakan untuk menghasilkan benih dari dompet HD dari frasa mnemonik dan kata sandi tambahan (tapi kita akan membahas ini lebih detail di bab-bab mendatang).

Proses PBKDF2 adalah sebagai berikut, dengan:

- $m$: frasa mnemonik pengguna;
- $s$: kata sandi tambahan opsional untuk meningkatkan keamanan (kolom kosong jika tidak ada kata sandi tambahan);
- $n$: jumlah iterasi fungsi, dalam kasus kita, itu adalah 2048.
  Fungsi PBKDF2 didefinisikan secara iteratif. Setiap iterasi mengambil hasil dari iterasi sebelumnya, melewatinya melalui HMAC-SHA512, dan menggabungkan hasil berturut-turut untuk menghasilkan kunci akhir:
  $$
  \text{PBKDF2}(m, s) = \text{HMAC-SHA512}^{2048}(m, s)
  $$

Secara skematis, PBKDF2 dapat digambarkan sebagai berikut:

![CYP201](assets/fr/013.webp)

Dalam bab ini, kita telah menjelajahi fungsi HMAC-SHA512 dan PBKDF2, yang menggunakan fungsi hashing untuk memastikan integritas dan keamanan dari derivasi kunci dalam protokol Bitcoin. Pada bagian selanjutnya, kita akan melihat ke dalam tanda tangan digital, metode kriptografi lain yang banyak digunakan dalam Bitcoin.

# Tanda Tangan Digital

<partId>76b58a00-0c18-54b9-870d-6b7e34029db8</partId>

## Tanda Tangan Digital dan Kurva Eliptik

<chapterId>c9dd9672-6da1-57f8-9871-8b28994d4c1a</chapterId>

Metode kriptografi kedua yang digunakan dalam Bitcoin melibatkan algoritma tanda tangan digital. Mari kita jelajahi apa ini dan bagaimana cara kerjanya.

### Bitcoin, UTXO, dan Kondisi Pengeluaran

Istilah "_dompet_" dalam Bitcoin bisa cukup membingungkan bagi pemula. Memang, apa yang disebut dompet Bitcoin adalah perangkat lunak yang tidak secara langsung menyimpan bitcoin Anda, tidak seperti dompet fisik yang dapat menyimpan koin atau uang kertas. Bitcoin hanyalah unit akun. Unit akun ini diwakili oleh **UTXO** (_Unspent Transaction Outputs_), yang merupakan output transaksi yang belum terpakai. Jika output ini belum terpakai, berarti mereka milik pengguna. UTXO, dalam satu cara, adalah potongan-potongan bitcoin, dengan ukuran variabel, yang milik pengguna.

Protokol Bitcoin bersifat terdistribusi dan beroperasi tanpa otoritas pusat. Oleh karena itu, ini tidak seperti catatan perbankan tradisional, di mana euro yang menjadi milik Anda hanya dikaitkan dengan identitas pribadi Anda. Di Bitcoin, UTXO Anda menjadi milik Anda karena mereka dilindungi oleh kondisi pengeluaran yang ditentukan dalam bahasa Script. Untuk menyederhanakan, ada dua jenis skrip: skrip penguncian (_scriptPubKey_), yang melindungi UTXO, dan skrip pembukaan (_scriptSig_), yang memungkinkan membuka UTXO dan dengan demikian menghabiskan unit bitcoin yang diwakilinya.
Operasi awal Bitcoin dengan skrip P2PK melibatkan penggunaan kunci publik untuk mengunci dana, menentukan dalam _scriptPubKey_ bahwa orang yang ingin menghabiskan UTXO ini harus menyediakan tanda tangan yang valid dengan kunci pribadi yang sesuai dengan kunci publik ini. Untuk membuka UTXO ini, oleh karena itu, diperlukan tanda tangan yang valid dalam _scriptSig_. Seperti namanya, kunci publik diketahui oleh semua orang karena disiarkan di blockchain, sementara kunci pribadi hanya diketahui oleh pemilik sah dana tersebut.
Ini adalah operasi dasar Bitcoin, tetapi seiring waktu, operasi ini menjadi lebih kompleks. Pertama, Satoshi juga memperkenalkan skrip P2PKH, yang menggunakan alamat penerima dalam _scriptPubKey_, yang mewakili hash dari kunci publik. Kemudian, sistem menjadi lebih kompleks lagi dengan kedatangan SegWit dan kemudian Taproot. Namun, prinsip umum tetap pada dasarnya sama: kunci publik atau representasi dari kunci ini digunakan untuk mengunci UTXO, dan kunci pribadi yang sesuai diperlukan untuk membukanya dan dengan demikian menghabiskannya.
Seorang pengguna yang ingin melakukan transaksi Bitcoin harus menciptakan tanda tangan digital menggunakan kunci privat mereka pada transaksi yang bersangkutan. Tanda tangan tersebut dapat diverifikasi oleh peserta jaringan lainnya. Jika valid, ini berarti bahwa pengguna yang memulai transaksi memang pemilik dari kunci privat tersebut, dan oleh karena itu pemilik dari bitcoin yang ingin mereka belanjakan. Pengguna lain kemudian dapat menerima dan menyebarkan transaksi tersebut.

Sebagai hasilnya, seorang pengguna yang memiliki bitcoin yang dikunci dengan kunci publik harus menemukan cara untuk menyimpan secara aman apa yang memungkinkan membuka kunci dana mereka: kunci privat. Dompet Bitcoin adalah tepatnya sebuah perangkat yang akan memungkinkan Anda untuk dengan mudah menyimpan semua kunci Anda tanpa orang lain memiliki akses kepadanya. Oleh karena itu, ini lebih mirip sebuah gantungan kunci daripada dompet.

Hubungan matematis antara kunci publik dan kunci privat, serta kemampuan untuk melakukan tanda tangan untuk membuktikan kepemilikan kunci privat tanpa mengungkapkannya, dimungkinkan oleh algoritma tanda tangan digital. Dalam protokol Bitcoin, 2 algoritma tanda tangan digunakan: **ECDSA** (_Elliptic Curve Digital Signature Algorithm_) dan **skema tanda tangan Schnorr**. ECDSA adalah protokol tanda tangan digital yang digunakan dalam Bitcoin sejak awal. Schnorr lebih baru dalam Bitcoin, karena diperkenalkan pada November 2021 dengan pembaruan Taproot.
Kedua algoritma ini cukup serupa dalam mekanisme mereka. Keduanya berbasis pada kriptografi kurva eliptik. Perbedaan utama antara kedua protokol ini terletak pada struktur tanda tangan dan beberapa properti matematis spesifik. Oleh karena itu, kita akan mempelajari fungsi dari algoritma-algoritma ini, dimulai dengan yang tertua: ECDSA.

### Kriptografi Kurva Eliptik

Kriptografi Kurva Eliptik (ECC) adalah sekumpulan algoritma yang menggunakan kurva eliptik untuk berbagai properti matematis dan geometrisnya untuk tujuan kriptografi. Keamanan dari algoritma-algoritma ini bergantung pada kesulitan masalah logaritma diskrit pada kurva eliptik. Kurva eliptik terutama digunakan untuk pertukaran kunci, enkripsi asimetris, atau untuk menciptakan tanda tangan digital.

Sebuah properti penting dari kurva ini adalah bahwa mereka simetris terhadap sumbu x. Dengan demikian, setiap garis non-vertikal yang memotong kurva di dua titik berbeda akan selalu berpotongan dengan kurva di titik ketiga. Selain itu, setiap tangen ke kurva di titik non-singular akan berpotongan dengan kurva di titik lain. Properti-properti ini akan berguna untuk mendefinisikan operasi pada kurva.

Berikut adalah representasi dari sebuah kurva eliptik di atas lapangan bilangan riil:

![CYP201](assets/fr/014.webp)

Setiap kurva eliptik didefinisikan oleh sebuah persamaan berbentuk:

$$
y^2 = x^3 + ax + b
$$

### secp256k1

Untuk menggunakan ECDSA atau Schnorr, seseorang harus memilih parameter dari kurva eliptik, yaitu nilai dari $a$ dan $b$ dalam persamaan kurva. Ada berbagai standar kurva eliptik yang dianggap aman secara kriptografi. Yang paling terkenal adalah kurva _secp256r1_, yang didefinisikan dan direkomendasikan oleh NIST (_National Institute of Standards and Technology_).

Meskipun demikian, Satoshi Nakamoto, penemu Bitcoin, memilih untuk tidak menggunakan kurva ini. Alasan dari pilihan ini tidak diketahui, tetapi beberapa percaya dia lebih memilih untuk menemukan alternatif karena parameter dari kurva ini berpotensi mengandung backdoor. Sebaliknya, protokol Bitcoin menggunakan standar kurva **_secp256k1_**. Kurva ini didefinisikan oleh parameter $a = 0$ dan $b = 7$. Persamaannya oleh karena itu adalah:

$$
y^2 = x^3 + 7
$$

Representasi grafisnya di atas lapangan bilangan riil terlihat seperti ini:
![CYP201](assets/fr/015.webp)
Namun, dalam kriptografi, kita bekerja dengan himpunan angka yang terbatas. Lebih spesifik lagi, kita bekerja pada lapangan terbatas $\mathbb{F}_p$, yang merupakan lapangan bilangan bulat modulo sebuah bilangan prima $p$.
**Definisi**: Sebuah bilangan prima adalah bilangan bulat alami yang lebih besar atau sama dengan 2 yang hanya memiliki dua pembagi bilangan bulat positif yang berbeda: 1 dan dirinya sendiri. Sebagai contoh, angka 7 adalah bilangan prima karena hanya bisa dibagi dengan 1 dan 7. Di sisi lain, angka 8 bukan bilangan prima karena bisa dibagi dengan 1, 2, 4, dan 8.
Dalam Bitcoin, bilangan prima $p$ yang digunakan untuk mendefinisikan lapangan terbatas sangat besar. Bilangan ini dipilih sedemikian rupa sehingga orde dari lapangan (yaitu, jumlah elemen dalam $\mathbb{F}_p$) cukup besar untuk menjamin keamanan kriptografi.

Bilangan prima $p$ yang digunakan adalah:

```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```

Dalam notasi desimal, ini sesuai dengan:

$$
p = 2^{256} - 2^{32} - 977
$$

Dengan demikian, persamaan kurva eliptik kita sebenarnya adalah:

$$
y^2 \equiv x^3 + 7 \mod p
$$

Mengingat kurva ini didefinisikan di atas lapangan terbatas $\mathbb{F}_p$, ia tidak lagi menyerupai kurva kontinu tetapi lebih kepada himpunan titik-titik diskrit. Sebagai contoh, inilah tampilan kurva yang digunakan dalam Bitcoin untuk $p$ yang sangat kecil, yaitu $p = 17$:

![CYP201](assets/fr/016.webp)

Dalam contoh ini, saya sengaja membatasi lapangan terbatas ke $p = 17$ untuk alasan edukasi, tetapi harus dibayangkan bahwa yang digunakan dalam Bitcoin jauh lebih besar, hampir $2^{256}$.

Kita menggunakan lapangan terbatas bilangan bulat modulo $p$ untuk memastikan akurasi operasi pada kurva. Memang, kurva eliptik di atas lapangan bilangan real terkena ketidakakuratan karena kesalahan pembulatan selama perhitungan komputasi. Jika banyak operasi dilakukan pada kurva, kesalahan ini menumpuk dan hasil akhir bisa tidak akurat atau sulit untuk direproduksi. Penggunaan eksklusif bilangan bulat positif memastikan akurasi perhitungan yang sempurna dan dengan demikian reproduktivitas hasil.

Matematika kurva eliptik di atas lapangan terbatas analog dengan yang di atas lapangan bilangan real, dengan adaptasi bahwa semua operasi dilakukan modulo $p$. Untuk menyederhanakan penjelasan, kita akan melanjutkan di bab-bab berikutnya untuk mengilustrasikan konsep menggunakan kurva yang didefinisikan di atas bilangan real, sambil tetap ingat bahwa, dalam praktiknya, kurva didefinisikan di atas lapangan terbatas.

Jika Anda ingin mempelajari lebih lanjut tentang dasar-dasar matematika kriptografi modern, saya juga merekomendasikan untuk berkonsultasi dengan kursus lain di Jaringan Plan ₿:

https://planb.network/courses/cyp302

## Menghitung Kunci Publik dari Kunci Privat

<chapterId>fcb2bd58-5dda-5ecf-bb8f-ad1a0561ab4a</chapterId>
Seperti yang telah dilihat sebelumnya, algoritma tanda tangan digital pada Bitcoin didasarkan pada pasangan kunci privat dan publik yang secara matematis terkait. Mari kita jelajahi bersama apa hubungan matematis ini dan bagaimana mereka dihasilkan.

### Kunci Privat

Kunci privat hanyalah sebuah angka acak atau pseudo-acak. Dalam kasus Bitcoin, angka ini berukuran 256 bit. Jumlah kemungkinan untuk sebuah kunci privat Bitcoin oleh karena itu secara teoritis adalah $2^{256}$.
**Catatan**: Sebuah "angka pseudo-acak" adalah angka yang memiliki sifat-sifat yang mendekati angka acak sejati tetapi dihasilkan oleh algoritma deterministik.
Namun, dalam praktiknya, hanya ada $n$ titik berbeda pada kurva eliptik secp256k1 kita, di mana $n$ adalah ordo dari titik generator $G$ dari kurva tersebut. Kita akan melihat nanti apa arti angka ini, tetapi cukup ingat bahwa kunci privat yang valid adalah bilangan bulat antara $1$ dan $n-1$, dengan mengetahui bahwa $n$ adalah angka yang dekat tetapi sedikit kurang dari $2^{256}$. Oleh karena itu, ada beberapa angka 256-bit yang tidak valid untuk menjadi kunci privat di Bitcoin, khususnya, semua angka antara $n$ dan $2^{256}$. Jika generasi angka acak (kunci privat) menghasilkan nilai $k$ sehingga $k \geq n$, itu dianggap tidak valid, dan nilai acak baru harus dihasilkan.

Jumlah kemungkinan untuk kunci privat Bitcoin oleh karena itu sekitar $n$, yang merupakan angka dekat dengan $1.158 \times 10^{77}$. Angka ini sangat besar sehingga jika Anda memilih kunci privat secara acak, secara statistik hampir mustahil untuk mendarat pada kunci privat pengguna lain. Untuk memberi Anda gambaran tentang skala, jumlah kunci privat yang mungkin di Bitcoin adalah dari ordo magnitudo yang dekat dengan jumlah atom yang diperkirakan di alam semesta yang dapat diamati.

Seperti yang akan kita lihat dalam bab-bab mendatang, hari ini, mayoritas kunci privat yang digunakan di Bitcoin tidak dihasilkan secara acak tetapi adalah hasil dari derivasi deterministik dari frasa mnemonik, itu sendiri pseudo-acak (ini adalah frasa terkenal dari 12 atau 24 kata). Informasi ini tidak mengubah apa pun untuk penggunaan algoritma tanda tangan seperti ECDSA, tetapi itu membantu untuk memfokuskan kembali popularisasi kita pada Bitcoin.

Untuk kelanjutan penjelasan, kunci privat akan dilambangkan dengan huruf kecil $k$.

### Kunci Publik

Kunci publik adalah titik pada kurva eliptik, dilambangkan dengan huruf kapital $K$, dan dihitung dari kunci privat $k$. Titik $K$ ini diwakili oleh sepasang koordinat $(x, y)$ pada kurva eliptik, masing-masing koordinat adalah bilangan bulat modulo $p$, bilangan prima yang mendefinisikan lapangan hingga $\mathbb{F}_p$.
Dalam praktik, kunci publik yang tidak dikompresi diwakili oleh 512 bit (atau 64 byte), yang sesuai dengan dua angka 256-bit ($x$ dan $y$) yang ditempatkan ujung-ke-ujung. Angka-angka ini adalah absis ($x$) dan ordinat ($y$) dari titik kita pada secp256k1. Jika kita menambahkan prefiks, kunci publik totalnya 520 bit.

Namun, juga mungkin untuk merepresentasikan kunci publik dalam bentuk yang dikompresi menggunakan hanya 33 byte (264 bit) dengan hanya menyimpan absis $x$ dari titik kita pada kurva dan byte yang menunjukkan paritas dari $y$. Ini adalah yang dikenal sebagai kunci publik yang dikompresi. Saya akan berbicara lebih banyak tentang ini di bab-bab terakhir pelatihan ini. Tetapi yang perlu Anda ingat adalah bahwa kunci publik $K$ adalah titik yang dijelaskan oleh $x$ dan $y$.

Untuk menghitung titik $K$ yang sesuai dengan kunci publik kita, kita menggunakan operasi perkalian skalar pada kurva eliptik, yang didefinisikan sebagai penambahan berulang ($k$ kali) dari titik generator $G$:

$$
K = k \cdot G
$$

di mana:

- $k$ adalah kunci privat (bilangan bulat acak antara $1$ dan $n-1$);
- $G$ adalah titik generator dari kurva eliptik yang digunakan oleh semua peserta jaringan Bitcoin; - $\cdot$ mewakili perkalian skalar pada kurva eliptik, yang setara dengan menambahkan titik $G$ ke dirinya sendiri $k$ kali.

Fakta bahwa titik $G$ ini umum untuk semua kunci publik di Bitcoin memungkinkan kita untuk yakin bahwa kunci privat yang sama $k$ akan selalu memberikan kita kunci publik yang sama $K$:

![CYP201](assets/fr/017.webp)

Karakteristik utama dari operasi ini adalah bahwa itu adalah fungsi satu arah. Mudah untuk menghitung kunci publik $K$ dengan mengetahui kunci privat $k$ dan titik generator $G$, tetapi praktis tidak mungkin untuk menghitung kunci privat $k$ dengan hanya mengetahui kunci publik $K$ dan titik generator $G$. Menemukan $k$ dari $K$ dan $G$ berarti menyelesaikan masalah logaritma diskrit pada kurva eliptik, sebuah masalah matematika yang sulit untuk mana tidak ada algoritma efisien yang diketahui. Bahkan kalkulator paling kuat saat ini tidak mampu menyelesaikan masalah ini dalam waktu yang wajar.

### Penambahan dan Penggandaan Titik pada Kurva Eliptik

Konsep penambahan pada kurva eliptik didefinisikan secara geometris. Jika kita memiliki dua titik $P$ dan $Q$ pada kurva, operasi $P + Q$ dihitung dengan menggambar garis yang melewati $P$ dan $Q$. Garis ini akan selalu berpotongan dengan kurva di titik ketiga $R'$. Kemudian kita mengambil citra cermin dari titik ini terhadap sumbu-x untuk mendapatkan titik $R$, yang merupakan hasil dari penambahan:

$$
P + Q = R
$$

Secara grafis, ini dapat diwakili sebagai berikut:

![CYP201](assets/fr/019.webp)

Untuk penggandaan titik, yaitu operasi $P + P$, kita menggambar tangen ke kurva di titik $P$. Tangen ini berpotongan dengan kurva di titik lain $S'$. Kemudian kita mengambil citra cermin dari titik ini terhadap sumbu-x untuk mendapatkan titik $S$, yang merupakan hasil dari penggandaan:

$$
2P = S
$$

Secara grafis, ini ditunjukkan sebagai:

![CYP201](assets/fr/020.webp)

Dengan menggunakan operasi penambahan dan penggandaan ini, kita dapat melakukan perkalian skalar dari sebuah titik dengan bilangan bulat $k$, ditulis $kP$, dengan melakukan penggandaan dan penambahan berulang.

Misalnya, anggap kita telah memilih kunci privat $k = 4$. Untuk menghitung kunci publik yang terkait, kita lakukan:

$$
K = k \cdot G = 4G
$$

Secara grafis, ini sesuai dengan melakukan serangkaian penambahan dan penggandaan:

- Hitung $2G$ dengan menggandakan $G$.
- Hitung $4G$ dengan menggandakan $2G$.

![CYP201](assets/fr/021.webp)

Jika kita ingin, misalnya, menghitung titik $3G$, kita harus terlebih dahulu menghitung titik $2G$ dengan menggandakan titik $G$, kemudian menambahkan $G$ dan $2G$. Untuk menambahkan $G$ dan $2G$, cukup gambar garis yang menghubungkan kedua titik ini, ambil titik unik $-3G$ di persimpangan antara garis ini dan kurva eliptik, dan kemudian tentukan $3G$ sebagai lawan dari $-3G$.

Kita akan memiliki:

$$
G + G = 2G
$$

$$
2G + G = 3G
$$

Secara grafis, ini akan diwakili sebagai berikut:

### Fungsi Satu Arah

Berkat operasi-operasi ini, kita dapat memahami mengapa mudah untuk menurunkan kunci publik dari kunci privat, tetapi sebaliknya hampir mustahil.

Mari kita kembali ke contoh sederhana kita. Dengan kunci privat $k = 4$. Untuk menghitung kunci publik yang terkait, kita melakukan:

$$
K = k \cdot G = 4G
$$

Dengan demikian, kita dapat dengan mudah menghitung kunci publik $K$ dengan mengetahui $k$ dan $G$.

Sekarang, jika seseorang hanya mengetahui kunci publik $K$, mereka dihadapkan pada masalah logaritma diskrit: menemukan $k$ sedemikian sehingga $K = k \cdot G$. Masalah ini dianggap sulit karena tidak ada algoritma efisien untuk menyelesaikannya pada kurva eliptik. Ini memastikan keamanan algoritma ECDSA dan Schnorr.

Tentu saja, dalam contoh sederhana ini dengan $k = 4$, akan mungkin untuk menemukan $k$ melalui coba-coba, karena jumlah kemungkinannya rendah. Namun, dalam praktiknya pada Bitcoin, $k$ adalah bilangan bulat 256-bit, membuat jumlah kemungkinannya sangat besar (sekitar $1.158 \times 10^{77}$). Oleh karena itu, tidak mungkin untuk menemukan $k$ dengan brute force.

## Menandatangani dengan Kunci Privat

<chapterId>bb07826f-826e-5905-b307-3d82001fb778</chapterId>

Sekarang setelah Anda tahu cara menurunkan kunci publik dari kunci privat, Anda sudah dapat menerima bitcoin dengan menggunakan pasangan kunci ini sebagai kondisi pengeluaran. Tapi bagaimana cara menghabiskannya? Untuk menghabiskan bitcoin, Anda perlu membuka _scriptPubKey_ yang terlampir pada UTXO Anda untuk membuktikan bahwa Anda memang pemilik sahnya. Untuk melakukan ini, Anda harus menghasilkan tanda tangan $s$ yang cocok dengan kunci publik $K$ yang ada dalam _scriptPubKey_ menggunakan kunci privat $k$ yang awalnya digunakan untuk menghitung $K$. Tanda tangan digital ini menjadi bukti tak terbantahkan bahwa Anda memiliki kunci privat yang terkait dengan kunci publik yang Anda klaim.

### Parameter Kurva Eliptik

Untuk melakukan tanda tangan digital, semua peserta harus terlebih dahulu sepakat pada parameter dari kurva eliptik yang digunakan. Dalam kasus Bitcoin, parameter dari **secp256k1** adalah sebagai berikut:

Lapangan terbatas $\mathbb{Z}_p$ didefinisikan oleh:

$$
p = 2^{256} - 2^{32} - 977
$$

```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```

$p$ adalah bilangan prima yang sangat besar sedikit kurang dari $2^{256}$.

Kurva eliptik $y^2 = x^3 + ax + b$ di atas $\mathbb{Z}_p$ didefinisikan oleh:

$$
a = 0, \quad b = 7
$$

Titik generator atau titik asal $G$:

```text
G = 0x0279BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
```

Angka ini adalah bentuk terkompresi yang hanya memberikan absis dari titik $G$. Awalan `02` di awal menentukan mana dari dua nilai yang memiliki absis $x$ ini yang akan digunakan sebagai titik generator.
Orde $n$ dari $G$ (jumlah titik yang ada) dan faktor kofaktor $h$:

```text
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
```

$n$ adalah angka yang sangat besar, sedikit kurang dari $p$.

$$
h=1
$$

$h$ adalah faktor kofaktor atau jumlah subkelompok. Saya tidak akan menjelaskan apa yang ini representasikan di sini, karena cukup kompleks, dan dalam kasus Bitcoin, kita tidak perlu memperhitungkannya karena sama dengan $1$.

Semua informasi ini publik dan diketahui oleh semua peserta. Berkat mereka, pengguna dapat membuat tanda tangan digital dan memverifikasinya.

### Tanda Tangan dengan ECDSA

Algoritma ECDSA memungkinkan pengguna untuk menandatangani pesan menggunakan kunci privat mereka, sedemikian rupa sehingga siapa pun yang mengetahui kunci publik yang sesuai dapat memverifikasi keabsahan tanda tangan, tanpa kunci privat pernah diungkapkan. Dalam konteks Bitcoin, pesan yang akan ditandatangani tergantung pada _sighash_ yang dipilih oleh pengguna. Ini adalah _sighash_ yang akan menentukan bagian mana dari transaksi yang dicakup oleh tanda tangan. Saya akan membahas lebih lanjut tentang ini di bab berikutnya.

Berikut adalah langkah-langkah untuk menghasilkan tanda tangan ECDSA:

Pertama, kita menghitung hash ($e$) dari pesan yang perlu ditandatangani. Pesan $m$ dengan demikian dilewatkan melalui fungsi hash kriptografi, umumnya SHA256 atau double SHA256 dalam kasus Bitcoin:

$$
e = \text{HASH}(m)
$$

Selanjutnya, kita menghitung nonce. Dalam kriptografi, nonce hanyalah angka yang dihasilkan secara acak atau pseudo-acak yang digunakan hanya sekali. Artinya, setiap kali tanda tangan digital baru dibuat dengan pasangan kunci ini, akan sangat penting untuk menggunakan nonce yang berbeda, jika tidak, itu akan mengompromikan keamanan kunci privat. Oleh karena itu, cukup menentukan bilangan bulat acak dan unik $r$ sedemikian rupa sehingga $1 \leq r \leq n-1$, di mana $n$ adalah urutan titik pembangkit $G$ dari kurva elips.

Kemudian, kita akan menghitung titik $R$ pada kurva elips dengan koordinat $(x_R, y_R)$ sedemikian rupa sehingga:

$$
R = r \cdot G
$$

Kita ekstrak nilai absis dari titik $R$ ($x_R$). Nilai ini mewakili bagian pertama dari tanda tangan. Dan akhirnya, kita menghitung bagian kedua dari tanda tangan $s$ dengan cara ini:

$$
s = r^{-1} \left( e + k \cdot x_R \right) \mod n
$$

di mana:

- $r^{-1}$ adalah invers modular dari $r$ modulo $n$, yaitu, bilangan bulat sedemikian rupa sehingga $r \cdot r^{-1} \equiv 1 \mod n$;
- $k$ adalah kunci privat pengguna;
- $e$ adalah hash dari pesan;
- $n$ adalah urutan titik pembangkit $G$ dari kurva elips.

Tanda tangan kemudian hanya merupakan konkatenasi dari $x_R$ dan $s$:

$$
\text{SIG} = x_R \Vert s
$$

### Verifikasi Tanda Tangan ECDSA

Untuk memverifikasi tanda tangan $(x_R, s)$, siapa pun yang mengetahui kunci publik $K$ dan parameter dari kurva elips dapat melanjutkan dengan cara ini:
Pertama, verifikasi bahwa $x_R$ dan $s$ berada dalam interval $[1, n-1]$. Ini memastikan bahwa tanda tangan menghormati batasan matematis dari grup eliptik. Jika ini tidak terpenuhi, verifikator langsung menolak tanda tangan sebagai tidak valid.
Kemudian, hitung hash dari pesan:

$$
e = \text{HASH}(m)
$$

Hitung invers modular dari $s$ modulo $n$:

$$
s^{-1} \mod n
$$

Hitung dua nilai skalar $u_1$ dan $u_2$ dengan cara berikut:

$$
\begin{align*}
u_1 &= e \cdot s^{-1} \mod n \\
u_2 &= x_R \cdot s^{-1} \mod n
\end{align*}
$$

Dan akhirnya, hitung titik $V$ pada kurva eliptik sedemikian rupa:

$$
V = u_1 \cdot G + u_2 \cdot K
$$

Tanda tangan hanya valid jika $x_V \equiv x_R \mod n$, di mana $x_V$ adalah koordinat $x$ dari titik $V$. Memang, dengan menggabungkan $u_1 \cdot G$ dan $u_2 \cdot K$, seseorang mendapatkan titik $V$ yang, jika tanda tangannya valid, harus sesuai dengan titik $R$ yang digunakan selama penandatanganan (modulo $n$).

### Tanda Tangan dengan Protokol Schnorr

Skema tanda tangan Schnorr adalah alternatif untuk ECDSA yang menawarkan banyak keuntungan. Telah dimungkinkan untuk menggunakannya pada Bitcoin sejak 2021 dan pengenalan Taproot, dengan pola skrip P2TR. Seperti ECDSA, skema Schnorr memungkinkan penandatanganan pesan menggunakan kunci privat, sedemikian rupa sehingga tanda tangan dapat diverifikasi oleh siapa saja yang mengetahui kunci publik yang sesuai.
Dalam kasus Schnorr, kurva yang sama persis seperti ECDSA digunakan dengan parameter yang sama. Namun, kunci publik direpresentasikan sedikit berbeda dibandingkan dengan ECDSA. Memang, mereka hanya ditunjuk oleh koordinat $x$ dari titik pada kurva eliptik. Tidak seperti ECDSA, di mana kunci publik terkompresi direpresentasikan oleh 33 byte (dengan byte awalan menunjukkan paritas dari $y$), Schnorr menggunakan kunci publik 32-byte, yang hanya sesuai dengan koordinat $x$ dari titik $K$, dan diasumsikan bahwa $y$ genap secara default. Representasi yang disederhanakan ini mengurangi ukuran tanda tangan dan memfasilitasi optimisasi tertentu dalam algoritma verifikasi.
Kunci publik kemudian adalah koordinat $x$ dari titik $K$:

$$
\text{pk} = K_x
$$

Langkah pertama untuk menghasilkan tanda tangan adalah meng-hash pesan. Namun, tidak seperti ECDSA, hal ini dilakukan dengan nilai lain dan fungsi hash berlabel digunakan untuk menghindari tabrakan dalam konteks yang berbeda. Fungsi hash berlabel sederhananya melibatkan penambahan label sembarang ke input fungsi hash bersama dengan data pesan.

![CYP201](assets/fr/023.webp)

Selain pesan, koordinat $x$ dari kunci publik $K_x$, serta titik $R$ yang dihitung dari nonce $r$ ($R=r \cdot G$) yang sendiri adalah bilangan bulat unik untuk setiap tanda tangan, dihitung secara deterministik dari kunci privat dan pesan untuk menghindari kerentanan terkait penggunaan nonce kembali, juga dimasukkan ke dalam fungsi berlabel. Sama seperti untuk kunci publik, hanya koordinat $x$ dari titik nonce $R_x$ yang dipertahankan untuk menggambarkan titik.

Hasil dari hashing ini dicatat $e$ disebut "tantangan":

$$
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n
$$

Di sini, $\text{HASH}$ adalah fungsi hash SHA256, dan $\text{``BIP0340/challenge''}$ adalah tag spesifik untuk hashing.

Akhirnya, parameter $s$ dihitung dengan cara ini dari kunci privat $k$, nonce $r$, dan tantangan $e$:

$$
s = (r + e \cdot k) \mod n
$$

Tanda tangan kemudian hanya pasangan $Rx$ dan $s$.

$$
\text{SIG} = R_x \Vert s
$$

### Verifikasi Tanda Tangan Schnorr

Verifikasi tanda tangan Schnorr lebih sederhana daripada tanda tangan ECDSA. Berikut adalah langkah-langkah untuk memverifikasi tanda tangan $(R_x, s)$ dengan kunci publik $K_x$ dan pesan $m$:
Pertama, kita verifikasi bahwa $K_x$ adalah integer yang valid dan kurang dari $p$. Jika ini kasusnya, kita mengambil titik yang sesuai pada kurva dengan $K_y$ yang genap. Kita juga mengekstrak $R_x$ dan $s$ dengan memisahkan tanda tangan $\text{SIG}$. Kemudian, kita periksa bahwa $R_x < p$ dan $s < n$ (urutan kurva).
Selanjutnya, kita menghitung tantangan $e$ dengan cara yang sama seperti penerbit tanda tangan:

$$
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n
$$

Kemudian, kita menghitung titik referensi pada kurva dengan cara ini:

$$
R' = s \cdot G - e \cdot K
$$

Akhirnya, kita verifikasi bahwa $R'_x = R_x$. Jika kedua koordinat x cocok, maka tanda tangan $(R_x, s)$ memang valid dengan kunci publik $K_x$.

### Mengapa ini berhasil?

Penandatangan telah menghitung $s = r + e \cdot k \mod n$, jadi $R' = s \cdot G - e \cdot K$ seharusnya sama dengan titik asli $R$, karena:

$$
s \cdot G = (r + e \cdot k) \cdot G = r \cdot G + e \cdot k \cdot G
$$

Karena $K = k \cdot G$, kita memiliki $e \cdot k \cdot G = e \cdot K$. Jadi:

$$
R' = r \cdot G = R
$$

Oleh karena itu, kita memiliki:

$$
R'_x = R_x
$$

### Keuntungan dari tanda tangan Schnorr

Skema tanda tangan Schnorr menawarkan beberapa keuntungan untuk Bitcoin dibandingkan dengan algoritma ECDSA asli. Pertama, Schnorr memungkinkan agregasi kunci dan tanda tangan. Ini berarti bahwa beberapa kunci publik dapat digabungkan menjadi satu kunci.

![CYP201](assets/fr/024.webp)

Dan demikian pula, beberapa tanda tangan dapat diagregasi menjadi satu tanda tangan yang valid. Jadi, dalam kasus transaksi multisignature, satu set peserta dapat menandatangani dengan satu tanda tangan dan satu kunci publik yang teragregasi. Ini secara signifikan mengurangi biaya penyimpanan dan komputasi untuk jaringan, karena setiap node hanya perlu memverifikasi satu tanda tangan.

![CYP201](assets/fr/025.webp)

Selain itu, agregasi tanda tangan meningkatkan privasi. Dengan Schnorr, menjadi tidak mungkin untuk membedakan transaksi multisignature dari transaksi tanda tangan tunggal. Homogenitas ini membuat analisis rantai lebih sulit, karena membatasi kemampuan untuk mengidentifikasi sidik jari dompet.
Akhirnya, Schnorr juga menawarkan kemungkinan verifikasi batch. Dengan memverifikasi beberapa tanda tangan secara bersamaan, node dapat memperoleh efisiensi, terutama untuk blok yang mengandung banyak transaksi. Optimasi ini mengurangi waktu dan sumber daya yang diperlukan untuk memvalidasi sebuah blok. Selain itu, tanda tangan Schnorr tidak dapat dimanipulasi, tidak seperti tanda tangan yang dihasilkan dengan ECDSA. Ini berarti bahwa penyerang tidak dapat memodifikasi tanda tangan yang valid untuk membuat tanda tangan valid lainnya untuk pesan yang sama dan kunci publik yang sama. Kerentanan ini sebelumnya ada pada Bitcoin dan secara khusus mencegah implementasi aman dari Lightning Network. Ini diatasi untuk ECDSA dengan softfork SegWit pada tahun 2017, yang melibatkan pemindahan tanda tangan ke database terpisah dari transaksi untuk mencegah kemampuan manipulasinya.

### Mengapa Satoshi memilih ECDSA?

Seperti yang telah kita lihat, Satoshi awalnya memilih untuk mengimplementasikan ECDSA untuk tanda tangan digital pada Bitcoin. Namun, kita juga telah melihat bahwa Schnorr lebih unggul dari ECDSA dalam banyak aspek, dan protokol ini diciptakan oleh Claus-Peter Schnorr pada tahun 1989, 20 tahun sebelum penemuan Bitcoin.

Nah, kita tidak benar-benar tahu mengapa Satoshi tidak memilihnya, tetapi hipotesis yang mungkin adalah bahwa protokol ini berada di bawah paten hingga tahun 2008. Meskipun Bitcoin diciptakan setahun kemudian, pada Januari 2009, tidak ada standarisasi sumber terbuka untuk tanda tangan Schnorr yang tersedia pada saat itu. Mungkin Satoshi menganggap lebih aman menggunakan ECDSA, yang sudah banyak digunakan dan diuji dalam perangkat lunak sumber terbuka dan memiliki beberapa implementasi yang diakui (terutama pustaka OpenSSL yang digunakan hingga 2015 pada Bitcoin Core, kemudian digantikan oleh libsecp256k1 dalam versi 0.10.0). Atau mungkin dia sederhana tidak menyadari bahwa paten ini akan berakhir pada tahun 2008. Bagaimanapun, hipotesis yang paling mungkin tampaknya terkait dengan paten ini dan fakta bahwa ECDSA memiliki sejarah terbukti dan lebih mudah untuk diimplementasikan.

## The sighash flags

<chapterId>231c41a2-aff2-4655-9048-47b6d2d83d64</chapterId>

Seperti yang telah kita lihat dalam bab-bab sebelumnya, tanda tangan digital sering digunakan untuk membuka skrip dari sebuah input. Dalam proses penandatanganan, perlu untuk memasukkan data yang ditandatangani dalam perhitungan, yang ditunjuk dalam contoh kita oleh pesan $m$. Data ini, setelah ditandatangani, tidak dapat dimodifikasi tanpa membuat tanda tangan menjadi tidak valid. Memang, baik untuk ECDSA maupun Schnorr, verifikator tanda tangan harus memasukkan pesan $m$ yang sama dalam perhitungan mereka. Jika berbeda dari pesan $m$ yang awalnya digunakan oleh penandatangan, hasilnya akan salah dan tanda tangan akan dianggap tidak valid. Maka dikatakan bahwa sebuah tanda tangan mencakup data tertentu dan melindunginya, dalam suatu cara, dari modifikasi yang tidak sah.

### Apa itu sighash flag?

Dalam kasus khusus Bitcoin, kita telah melihat bahwa pesan $m$ sesuai dengan transaksi. Namun, pada kenyataannya, ini sedikit lebih kompleks. Memang, berkat sighash flags, dimungkinkan untuk memilih data spesifik dalam transaksi yang akan dicakup atau tidak oleh tanda tangan.
"Sighash flag" adalah parameter yang ditambahkan ke setiap input, memungkinkan penentuan komponen transaksi yang dicakup oleh tanda tangan yang terkait. Komponen-komponen ini adalah input dan output. Pilihan sighash flag ini menentukan input dan output mana dari transaksi yang diperbaiki oleh tanda tangan dan mana yang masih dapat dimodifikasi tanpa membuatnya tidak valid. Mekanisme ini memungkinkan tanda tangan untuk mengkomit data transaksi sesuai dengan niat penandatangan.
Jelas, setelah transaksi dikonfirmasi di blockchain, ia menjadi tidak dapat diubah, terlepas dari flag sighash yang digunakan. Kemungkinan modifikasi melalui flag sighash terbatas pada periode antara penandatanganan dan konfirmasi.
Umumnya, perangkat lunak dompet tidak menawarkan Anda opsi untuk secara manual memodifikasi flag sighash dari input Anda saat Anda membuat transaksi. Secara default, `SIGHASH_ALL` disetel. Secara pribadi, saya hanya tahu Sparrow Wallet yang memungkinkan modifikasi ini dari antarmuka pengguna.

### Apa saja flag sighash yang ada di Bitcoin?

Di Bitcoin, ada terutama 3 flag sighash dasar:

- `SIGHASH_ALL` (`0x01`): Tanda tangan berlaku untuk semua input dan semua output dari transaksi. Transaksi ini dengan demikian sepenuhnya dilindungi oleh tanda tangan dan tidak dapat lagi dimodifikasi. `SIGHASH_ALL` adalah sighash yang paling sering digunakan dalam transaksi sehari-hari ketika seseorang hanya ingin melakukan transaksi tanpa bisa dimodifikasi.

![CYP201](assets/fr/026.webp)

Dalam semua diagram dari bab ini, warna oranye mewakili elemen yang dilindungi oleh tanda tangan, sementara warna hitam menunjukkan yang tidak.

- `SIGHASH_NONE` (`0x02`): Tanda tangan mencakup semua input tetapi tidak ada output, sehingga memungkinkan modifikasi output setelah tanda tangan. Secara konkret, ini mirip dengan cek kosong. Penandatangan membuka UTXO di input tetapi meninggalkan bidang output sepenuhnya dapat dimodifikasi. Siapa pun yang mengetahui transaksi ini dapat menambahkan output pilihan mereka, misalnya dengan menentukan alamat penerima untuk mengumpulkan dana yang digunakan oleh input, dan kemudian menyiarkan transaksi untuk memulihkan bitcoin. Tanda tangan pemilik input tidak akan dibatalkan, karena hanya mencakup input.

![CYP201](assets/fr/027.webp)

- `SIGHASH_SINGLE` (`0x03`): Tanda tangan mencakup semua input serta satu output, sesuai dengan indeks input yang ditandatangani. Misalnya, jika tanda tangan membuka _scriptPubKey_ dari input #0, maka itu juga mencakup output #0. Tanda tangan juga melindungi semua input lain, yang tidak dapat lagi dimodifikasi. Namun, siapa pun dapat menambahkan output tambahan tanpa membatalkan tanda tangan, asalkan output #0, yang merupakan satu-satunya yang dilindungi olehnya, tidak dimodifikasi.
  ![CYP201](assets/fr/028.webp)

Selain ketiga flag sighash ini, ada juga modifikator `SIGHASH_ANYONECANPAY` (`0x80`). Modifikator ini dapat digabungkan dengan flag sighash dasar untuk menciptakan tiga flag sighash baru:

- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Tanda tangan mencakup satu input sambil mencakup semua output dari transaksi. Flag sighash gabungan ini memungkinkan, misalnya, pembuatan transaksi crowdfunding. Penyelenggara menyiapkan output dengan alamat mereka dan jumlah target, dan setiap investor kemudian dapat menambahkan input untuk mendanai output ini. Setelah dana yang cukup terkumpul di input untuk memenuhi output, transaksi dapat disiarkan.

![CYP201](assets/fr/029.webp)

- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): Tanda tangan mencakup satu input, tanpa berkomitmen pada output apa pun;

![CYP201](assets/fr/030.webp)

- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Tanda tangan ini mencakup satu input serta output yang memiliki indeks yang sama dengan input ini. Sebagai contoh, jika tanda tangan membuka _scriptPubKey_ dari input #3, ini juga akan mencakup output #3. Sisa transaksi tetap dapat dimodifikasi, baik dalam hal input lain maupun output lain.
  ![CYP201](assets/fr/031.webp)

### Proyek untuk Menambahkan Bendera Sighash Baru

Saat ini (2024), hanya bendera sighash yang disajikan di bagian sebelumnya yang dapat digunakan pada Bitcoin. Namun, beberapa proyek sedang mempertimbangkan penambahan bendera sighash baru. Sebagai contoh, BIP118, yang diusulkan oleh Christian Decker dan Anthony Towns, memperkenalkan dua bendera sighash baru: `SIGHASH_ANYPREVOUT` dan `SIGHASH_ANYPREVOUTANYSCRIPT` (_AnyPrevOut = "Output Sebelumnya Apapun"_).

Kedua bendera sighash ini akan menawarkan kemungkinan tambahan pada Bitcoin: menciptakan tanda tangan yang tidak mencakup input spesifik apa pun dari transaksi.

![CYP201](assets/fr/032.webp)

Ide ini awalnya dirumuskan oleh Joseph Poon dan Thaddeus Dryja dalam White Paper Lightning. Sebelum dinamai ulang, bendera sighash ini dinamakan `SIGHASH_NOINPUT`.
Jika bendera sighash ini diintegrasikan ke dalam Bitcoin, ini akan memungkinkan penggunaan covenants, tetapi ini juga merupakan prasyarat wajib untuk mengimplementasikan Eltoo, protokol umum untuk lapisan kedua yang mendefinisikan cara bersama mengelola kepemilikan UTXO. Eltoo dirancang khusus untuk menyelesaikan masalah yang terkait dengan mekanisme negosiasi status saluran Lightning, yaitu, antara pembukaan dan penutupan.

Untuk memperdalam pengetahuan Anda tentang Lightning Network, setelah kursus CYP201, saya sangat merekomendasikan kursus LNP201 oleh Fanis Michalakis, yang membahas topik ini secara detail:

https://planb.network/courses/lnp201

Di bagian selanjutnya, saya mengusulkan untuk menemukan bagaimana frasa mnemonik di dasar dompet Bitcoin Anda bekerja.

# Frasa Mnemonik

<partId>4070af16-c8a2-58b5-9871-a22c86c07458</partId>

## Evolusi Dompet Bitcoin

<chapterId>9d9acd5d-a0e5-5dfd-b544-f043fae8840f</chapterId>

Sekarang setelah kita telah menjelajahi cara kerja fungsi hash dan tanda tangan digital, kita dapat mempelajari bagaimana dompet Bitcoin berfungsi. Tujuannya akan menjadi untuk membayangkan bagaimana dompet pada Bitcoin dibangun, bagaimana ia diuraikan, dan apa saja informasi yang membentuknya digunakan untuk. Pemahaman tentang mekanisme dompet ini akan memungkinkan Anda untuk meningkatkan penggunaan Bitcoin Anda dalam hal keamanan dan privasi.

Sebelum menyelami detail teknis, penting untuk menjelaskan apa yang dimaksud dengan "dompet Bitcoin" dan untuk memahami kegunaannya.

### Apa itu Dompet Bitcoin?

Berbeda dengan dompet tradisional, yang memungkinkan Anda untuk menyimpan uang kertas dan koin fisik, dompet Bitcoin tidak "mengandung" bitcoin per se. Memang, bitcoin tidak ada dalam bentuk fisik atau digital yang dapat disimpan, tetapi diwakili oleh unit akun yang digambarkan dalam sistem dalam bentuk **UTXOs** (_Unspent Transaction Output_).
UTXOs merepresentasikan fragmen-fragmen bitcoin, dengan ukuran yang bervariasi, yang dapat dibelanjakan asalkan _scriptPubKey_ mereka terpenuhi. Untuk menghabiskan bitcoinnya, pengguna harus menyediakan _scriptSig_ yang membuka _scriptPubKey_ yang terkait dengan UTXO miliknya. Bukti ini umumnya dibuat melalui tanda tangan digital, yang dihasilkan dari kunci privat yang sesuai dengan kunci publik yang ada dalam _scriptPubKey_. Dengan demikian, elemen krusial yang harus diamankan oleh pengguna adalah kunci privat. Peran dari dompet Bitcoin adalah untuk mengelola kunci-kunci privat ini secara aman. Pada kenyataannya, perannya lebih mirip dengan gantungan kunci daripada dompet dalam pengertian tradisional.

### Dompet JBOK (_Just a Bunch Of Keys_)

Dompet pertama yang digunakan pada Bitcoin adalah dompet JBOK (_Just a Bunch Of Keys_), yang mengelompokkan kunci-kunci yang dihasilkan secara privat secara independen dan tanpa ada hubungan antara satu dengan yang lain. Dompet ini beroperasi pada model sederhana di mana setiap kunci privat dapat membuka alamat penerima Bitcoin yang unik.

![CYP201](assets/fr/033.webp)

Jika seseorang ingin menggunakan beberapa kunci privat, maka diperlukan untuk membuat banyak cadangan untuk memastikan akses ke dana jika terjadi masalah dengan perangkat yang menyimpan dompet. Jika menggunakan satu kunci privat, struktur dompet ini mungkin cukup, karena satu cadangan sudah cukup. Namun, ini menimbulkan masalah: di Bitcoin, sangat disarankan untuk tidak selalu menggunakan kunci privat yang sama. Memang, sebuah kunci privat dikaitkan dengan alamat unik, dan alamat penerima Bitcoin biasanya dirancang untuk penggunaan satu kali. Setiap kali Anda menerima dana, Anda harus menghasilkan alamat kosong baru.

Keterbatasan ini berasal dari model privasi Bitcoin. Dengan menggunakan alamat yang sama berulang kali, ini memudahkan pengamat eksternal untuk melacak semua transaksi Bitcoin saya. Itulah mengapa menggunakan kembali alamat penerima sangat tidak disarankan. Namun, untuk memiliki beberapa alamat dan memisahkan transaksi kita secara publik, diperlukan untuk mengelola beberapa kunci privat. Dalam kasus dompet JBOK, ini menyiratkan pembuatan banyak cadangan sebanyak pasangan kunci baru, tugas yang dapat dengan cepat menjadi kompleks dan sulit untuk dipertahankan bagi pengguna.

Untuk mempelajari lebih lanjut tentang model privasi Bitcoin dan menemukan metode untuk melindungi privasi Anda, saya juga merekomendasikan mengikuti kursus BTC204 saya di Plan ₿ Network:

https://planb.network/courses/btc204

### Dompet HD (_Hierarchical Deterministic_)

Untuk mengatasi keterbatasan dompet JBOK, struktur dompet baru kemudian digunakan. Pada tahun 2012, Pieter Wuille memperkenalkan perbaikan dengan BIP32, yang memperkenalkan dompet deterministik hierarkis. Prinsip dari dompet HD adalah untuk menurunkan semua kunci privat dari satu sumber informasi, yang disebut benih, secara deterministik dan hierarkis. Benih ini dihasilkan secara acak saat dompet dibuat dan merupakan cadangan unik yang memungkinkan untuk merekreasi semua kunci privat dompet. Dengan demikian, pengguna dapat menghasilkan jumlah kunci privat yang sangat besar untuk menghindari penggunaan ulang alamat dan menjaga privasi mereka, sambil hanya perlu membuat satu cadangan dompet mereka melalui benih.
![CYP201](assets/fr/034.webp)

Dalam dompet HD, derivasi kunci dilakukan menurut struktur hierarkis yang memungkinkan kunci-kunci untuk diorganisir ke dalam subruang derivasi, setiap subruang dapat dibagi lebih lanjut, untuk memfasilitasi pengelolaan dana dan interoperabilitas antara perangkat lunak dompet yang berbeda. Saat ini, standar ini diadopsi oleh mayoritas pengguna Bitcoin. Untuk alasan ini, kami akan memeriksanya secara detail dalam bab-bab berikut.

### Standar BIP39: Frasa Mnemonik

Selain BIP32, BIP39 menstandarkan format seed sebagai frasa mnemonik, untuk memudahkan pencadangan dan pembacaan oleh pengguna. Frasa mnemonik, juga disebut frasa pemulihan atau frasa 24 kata, adalah urutan kata yang diambil dari daftar yang telah ditentukan sebelumnya yang mengkodekan secara aman seed dompet.

Frasa mnemonik sangat mempermudah pencadangan bagi pengguna. Dalam kasus kehilangan, kerusakan, atau pencurian perangkat yang menyimpan dompet, dengan hanya mengetahui frasa mnemonik ini memungkinkan untuk merekreasi dompet dan memulihkan akses ke semua dana yang diamankan olehnya.

Dalam bab-bab berikutnya, kita akan menjelajahi cara kerja internal dompet HD, termasuk mekanisme derivasi kunci dan struktur hierarkis yang berbeda. Ini akan memungkinkan Anda untuk lebih memahami dasar kriptografi yang menjadi landasan keamanan dana pada Bitcoin. Dan untuk memulai, di bab selanjutnya, saya usulkan kita menemukan peran entropi di dasar dompet Anda.

## Entropi dan Nomor Acak

<chapterId>b43c715d-affb-56d8-a697-ad5bc2fffd63</chapterId>
Dompet HD modern (deterministik dan hierarkis) mengandalkan satu potongan informasi awal yang disebut "entropi" untuk menghasilkan seluruh set kunci dompet secara deterministik. Entropi ini adalah nomor pseudo-acak yang tingkat kekacaunya sebagian menentukan keamanan dompet.

### Definisi Entropi

Entropi, dalam konteks kriptografi dan informasi, adalah ukuran kuantitatif dari ketidakpastian atau ketidakterdugaan yang terkait dengan sumber data atau proses acak. Ini memainkan peran penting dalam keamanan sistem kriptografi, terutama dalam generasi kunci dan nomor acak. Entropi tinggi memastikan bahwa kunci yang dihasilkan cukup tidak terduga dan tahan terhadap serangan brute force, di mana penyerang mencoba semua kombinasi yang mungkin untuk menebak kunci.

Dalam konteks Bitcoin, entropi digunakan untuk menghasilkan seed. Saat membuat dompet deterministik dan hierarkis, konstruksi frasa mnemonik dilakukan dari nomor acak, yang sendiri berasal dari sumber entropi. Frasa tersebut kemudian digunakan untuk menghasilkan beberapa kunci privat, secara deterministik dan hierarkis, untuk menciptakan kondisi pengeluaran pada UTXO.

### Metode Menghasilkan Entropi

Entropi awal yang digunakan untuk dompet HD umumnya adalah 128 bit atau 256 bit, di mana:

- **128 bit entropi** sesuai dengan frasa mnemonik **12 kata**;
- **256 bit entropi** sesuai dengan frasa mnemonik **24 kata**.

Dalam kebanyakan kasus, nomor acak ini dihasilkan secara otomatis oleh perangkat lunak dompet menggunakan PRNG (_Pseudo-Random Number Generator_). PRNG adalah kategori algoritma yang digunakan untuk menghasilkan urutan nomor dari keadaan awal, yang memiliki karakteristik mendekati nomor acak, tanpa benar-benar menjadi satu. PRNG yang baik harus memiliki sifat seperti keseragaman output, ketidakdugaan, dan ketahanan terhadap serangan prediktif. Berbeda dengan generator nomor acak sejati (TRNG), PRNG adalah deterministik dan dapat direproduksi.

![CYP201](assets/fr/035.webp)

Alternatifnya adalah menghasilkan entropi secara manual, yang menawarkan kontrol yang lebih baik tetapi juga jauh lebih berisiko. Saya sangat menyarankan agar tidak menghasilkan entropi untuk dompet HD Anda sendiri.

Dalam bab selanjutnya, kita akan melihat bagaimana kita beralih dari nomor acak ke frasa mnemonik dari 12 atau 24 kata.

## Frasa Mnemonik

<chapterId>8f9340c1-e6dc-5557-a2f2-26c9669987d5</chapterId>
Frasa mnemonik, juga disebut "frasa benih", "frasa pemulihan", "frasa rahasia", atau "frasa 24 kata", adalah urutan yang biasanya terdiri dari 12 atau 24 kata, yang dihasilkan dari entropi. Ini digunakan untuk secara deterministik menurunkan semua kunci dari dompet HD. Ini berarti dari frasa ini, dimungkinkan untuk secara deterministik menghasilkan dan merekreasi semua kunci privat dan publik dari dompet Bitcoin, dan akibatnya mengakses dana yang dilindungi dengannya. Tujuan dari frasa mnemonik adalah untuk menyediakan sarana cadangan dan pemulihan bitcoin yang aman dan mudah digunakan. Ini diperkenalkan ke dalam standar pada tahun 2013 dengan BIP39.
Mari kita temukan bersama bagaimana cara pergi dari entropi ke frasa mnemonik.

### Checksum

Untuk mengubah entropi menjadi frasa mnemonik, seseorang harus terlebih dahulu menambahkan checksum (atau "jumlah kontrol") di akhir entropi. Checksum ini adalah urutan bit pendek yang memastikan integritas data dengan memverifikasi bahwa tidak ada modifikasi tidak sengaja yang telah diperkenalkan.

Untuk menghitung checksum, fungsi hash SHA256 diterapkan pada entropi (hanya sekali; ini adalah salah satu kasus langka dalam Bitcoin di mana hash SHA256 tunggal digunakan alih-alih hash ganda). Operasi ini menghasilkan hash 256-bit. Checksum terdiri dari bit pertama dari hash ini, dan panjangnya tergantung pada panjang entropi, menurut rumus berikut:

$$
\text{CS} = \frac{\text{ENT}}{32}
$$

di mana $\text{ENT}$ mewakili panjang entropi dalam bit, dan $\text{CS}$ panjang checksum dalam bit.

Misalnya, untuk entropi 256 bit, 8 bit pertama dari hash diambil untuk membentuk checksum:

$$
\text{CS} = \frac{256}{32} = 8 \text{ bit}
$$

Setelah checksum dihitung, itu digabungkan dengan entropi untuk mendapatkan urutan bit yang diperpanjang dicatat $\text{ENT} \Vert \text{CS}$ ("concatenate" berarti untuk diletakkan ujung-ke-ujung).

![CYP201](assets/fr/036.webp)

### Korespondensi antara Entropi dan Frasa Mnemonik

Jumlah kata dalam frasa mnemonik tergantung pada ukuran entropi awal, seperti yang diilustrasikan dalam tabel berikut dengan:

- $\text{ENT}$: ukuran dalam bit dari entropi;
- $\text{CS}$: ukuran dalam bit dari checksum;
- $w$: jumlah kata dalam frasa mnemonik akhir.

$$
\begin{array}{|c|c|c|c|}
\hline
\text{ENT} & \text{CS} & \text{ENT} \Vert \text{CS} & w \\
\hline
128 & 4 & 132 & 12 \\
160 & 5 & 165 & 15 \\
192 & 6 & 198 & 18 \\
224 & 7 & 231 & 21 \\
256 & 8 & 264 & 24 \\
\hline
\end{array}
$$

Misalnya, untuk entropi 256-bit, hasil $\text{ENT} \Vert \text{CS}$ adalah 264 bit dan menghasilkan frasa mnemonik dari 24 kata.

### Konversi Urutan Biner menjadi Frasa Mnemonik

Urutan bit $\text{ENT} \Vert \text{CS}$ kemudian dibagi menjadi segmen-segmen 11 bit. Setiap segmen 11-bit, setelah dikonversi ke desimal, sesuai dengan nomor antara 0 dan 2047, yang menunjukkan posisi kata [dalam daftar 2048 kata yang distandarisasi oleh BIP39](https://github.com/Planb-Network/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf).

![CYP201](assets/fr/037.webp)
Misalnya, untuk entropi 128-bit, checksum adalah 4 bit, sehingga total urutan berukuran 132 bit. Ini dibagi menjadi 12 segmen dari 11 bit (bit oranye menunjukkan checksum):
![CYP201](assets/fr/038.webp)

Setiap segmen kemudian dikonversi menjadi sebuah angka desimal yang mewakili sebuah kata dalam daftar. Misalnya, segmen biner `01011010001` setara dalam desimal dengan `721`. Dengan menambahkan 1 untuk menyelaraskan dengan pengindeksan daftar (yang dimulai dari 1 bukan 0), ini memberikan peringkat kata `722`, yang adalah "*focus*" dalam daftar.

![CYP201](assets/fr/039.webp)

Korespondensi ini diulang untuk setiap dari 12 segmen, untuk mendapatkan frasa 12 kata.

![CYP201](assets/fr/040.webp)

### Karakteristik dari Daftar Kata BIP39

Sebuah kekhasan dari daftar kata BIP39 adalah tidak ada kata yang berbagi empat huruf pertama yang sama dalam urutan yang sama dengan kata lain. Ini berarti bahwa mencatat hanya empat huruf pertama dari setiap kata sudah cukup untuk menyimpan frasa mnemonik. Ini bisa menarik untuk menghemat ruang, terutama bagi mereka yang ingin mengukirnya pada dukungan logam.

Daftar ini dari 2048 kata ada dalam beberapa bahasa. Ini bukan sekedar terjemahan, tetapi kata-kata yang berbeda untuk setiap bahasa. Namun, sangat disarankan untuk tetap menggunakan versi bahasa Inggris, karena versi dalam bahasa lain umumnya tidak didukung oleh perangkat lunak dompet.

### Panjang Mana yang Harus Dipilih untuk Frasa Mnemonik Anda?
Untuk menentukan panjang optimal dari frasa mnemonik Anda, seseorang harus mempertimbangkan keamanan aktual yang disediakannya. Frasa 12 kata menjamin keamanan 128 bit, sementara frasa 24 kata menawarkan 256 bit.

Namun, perbedaan ini dalam keamanan tingkat frasa tidak meningkatkan keamanan keseluruhan dari dompet Bitcoin, karena kunci privat yang berasal dari frasa ini hanya mendapat manfaat dari keamanan 128 bit. Memang, seperti yang telah kita lihat sebelumnya, kunci privat Bitcoin dihasilkan dari angka acak (atau berasal dari sumber acak) yang berkisar antara $1$ dan $n-1$, di mana $n$ mewakili urutan titik generator $G$ dari kurva secp256k1, sebuah angka sedikit kurang dari $2^{256}$. Seseorang mungkin berpikir bahwa kunci privat ini menawarkan keamanan 256 bit. Namun, keamanannya terletak pada kesulitan menemukan kunci privat dari kunci publiknya, sebuah kesulitan yang ditetapkan oleh masalah logaritma diskrit pada kurva eliptik (*ECDLP*). Hingga saat ini, algoritma terbaik yang diketahui untuk menyelesaikan masalah ini adalah algoritma rho Pollard, yang mengurangi jumlah operasi yang diperlukan untuk memecahkan kunci menjadi akar kuadrat dari ukurannya.

Untuk kunci 256-bit, seperti yang digunakan pada Bitcoin, algoritma rho Pollard dengan demikian mengurangi kompleksitas menjadi $2^{128}$ operasi:


$$

O(\sqrt{2^{256}}) = O(2^{128})

$$

Oleh karena itu, dianggap bahwa kunci privat yang digunakan pada Bitcoin menawarkan keamanan 128 bit.

Sebagai hasilnya, memilih frasa 24 kata tidak memberikan perlindungan tambahan untuk dompet, karena 256 bit keamanan pada frasa tidak berguna jika kunci yang berasal hanya menawarkan keamanan 128 bit. Untuk mengilustrasikan prinsip ini, ini seperti memiliki rumah dengan dua pintu: sebuah pintu kayu tua dan sebuah pintu bertulang. Dalam kejadian perampokan, pintu bertulang tidak akan berguna, karena perampok akan melewati pintu kayu. Ini adalah situasi analog di sini.
Frasa 12 kata, yang juga menawarkan keamanan 128 bit, saat ini sudah cukup untuk melindungi bitcoin Anda dari setiap upaya pencurian. Selama algoritma tanda tangan digital tidak berubah untuk menggunakan kunci yang lebih besar atau bergantung pada masalah matematika lain selain ECDLP, frasa 24 kata tetap berlebihan. Selain itu, frasa yang lebih panjang meningkatkan risiko kehilangan saat pencadangan: pencadangan yang dua kali lebih singkat selalu lebih mudah dikelola.
Untuk lebih lanjut dan belajar secara konkret bagaimana menghasilkan frasa mnemonik tes secara manual, saya menyarankan Anda untuk menemukan tutorial ini:

https://planb.network/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228
Sebelum melanjutkan dengan derivasi dompet dari frasa mnemonik ini, saya akan memperkenalkan Anda, dalam bab berikutnya, ke frasa sandi BIP39, karena ini berperan dalam proses derivasi, dan berada pada level yang sama dengan frasa mnemonik.
## Frasa Sandi
<chapterId>6a51b397-f3b5-5084-b151-cef94bc9b93f</chapterId>

Seperti yang baru saja kita lihat, dompet HD dihasilkan dari frasa mnemonik yang biasanya terdiri dari 12 atau 24 kata. Frasa ini sangat penting karena memungkinkan pemulihan semua kunci dompet jika perangkat fisiknya (seperti dompet perangkat keras, misalnya) hilang. Namun, ini merupakan satu titik kegagalan, karena jika dikompromikan, penyerang dapat mencuri semua bitcoin. Di sinilah frasa sandi BIP39 berperan.

### Apa itu frasa sandi BIP39?

Frasa sandi adalah kata sandi opsional, yang dapat Anda pilih secara bebas, yang ditambahkan ke frasa mnemonik dalam proses derivasi kunci untuk meningkatkan keamanan dompet.

Hati-hati, frasa sandi tidak boleh disamakan dengan kode PIN dari dompet perangkat keras Anda atau kata sandi yang digunakan untuk membuka akses ke dompet Anda di komputer. Tidak seperti semua elemen ini, frasa sandi berperan dalam derivasi kunci dompet Anda. **Ini berarti tanpa itu, Anda tidak akan pernah bisa memulihkan bitcoin Anda.**

Frasa sandi bekerja bersama dengan frasa mnemonik, memodifikasi benih dari mana kunci dihasilkan. Jadi, meskipun seseorang mendapatkan frasa 12 atau 24 kata Anda, tanpa frasa sandi, mereka tidak dapat mengakses dana Anda. Menggunakan frasa sandi pada dasarnya menciptakan dompet baru dengan kunci yang berbeda. Memodifikasi (bahkan sedikit) frasa sandi akan menghasilkan dompet yang berbeda.

![CYP201](assets/fr/041.webp)

### Mengapa Anda harus menggunakan frasa sandi?

Frasa sandi bersifat sewenang-wenang dan bisa berupa kombinasi karakter apa pun yang dipilih oleh pengguna. Menggunakan frasa sandi dengan demikian menawarkan beberapa keuntungan. Pertama-tama, ini mengurangi semua risiko yang terkait dengan kompromi frasa mnemonik dengan memerlukan faktor kedua untuk mengakses dana (pencurian, akses ke rumah Anda, dll.).

Selanjutnya, ini dapat digunakan secara strategis untuk menciptakan dompet umpan, untuk menghadapi kendala fisik mencuri dana Anda seperti serangan "_$5 wrench_" yang terkenal. Dalam skenario ini, ideanya adalah memiliki dompet tanpa frasa sandi yang hanya berisi sejumlah kecil bitcoin, cukup untuk memuaskan penyerang potensial, sambil memiliki dompet tersembunyi. Yang terakhir ini menggunakan frasa mnemonik yang sama tetapi diamankan dengan frasa sandi tambahan.
Akhirnya, penggunaan frasa sandi menarik ketika seseorang ingin mengontrol keacakan dari generasi benih dompet HD.
### Bagaimana memilih frasa sandi yang baik?

Agar frasa sandi efektif, harus cukup panjang dan acak. Seperti dengan kata sandi yang kuat, saya merekomendasikan memilih frasa sandi yang sepanjang dan seacak mungkin, dengan keragaman huruf, angka, dan simbol untuk membuat serangan brute force menjadi mustahil.
Juga penting untuk menyimpan passphrase ini dengan benar, sama seperti frase mnemonik. **Kehilangannya berarti kehilangan akses ke bitcoin Anda**. Saya sangat menyarankan agar tidak hanya mengingatnya di kepala, karena ini meningkatkan risiko kehilangan secara tidak wajar. Yang ideal adalah menuliskannya pada media fisik (kertas atau logam) yang terpisah dari frase mnemonik. Cadangan ini jelas harus disimpan di tempat yang berbeda dari tempat penyimpanan frase mnemonik Anda untuk mencegah keduanya dikompromikan secara bersamaan.
![CYP201](assets/fr/042.webp)

Pada bagian berikut, kita akan menemukan bagaimana kedua elemen ini di dasar dompet Anda — frase mnemonik dan passphrase — digunakan untuk menurunkan pasangan kunci yang digunakan dalam *scriptPubKey* yang mengunci UTXO Anda.

# Pembuatan Dompet Bitcoin
<partId>9c25e767-7eae-50b8-8c5f-679d8fc83bab</partId>

## Pembuatan Seed dan Master Key
<chapterId>63093760-2010-5691-8d0e-9a04732ae557</chapterId>

Setelah frase mnemonik dan passphrase opsional dihasilkan, proses penurunan dompet Bitcoin HD dapat dimulai. Frase mnemonik pertama kali diubah menjadi seed yang merupakan dasar dari semua kunci dompet.

![CYP201](assets/fr/043.webp)

### Seed dari Dompet HD

Standar BIP39 mendefinisikan seed sebagai urutan 512-bit, yang berfungsi sebagai titik awal untuk penurunan semua kunci dari dompet HD. Seed diturunkan dari frase mnemonik dan passphrase opsional menggunakan algoritma **PBKDF2** (*Password-Based Key Derivation Function 2*) yang telah kita bahas di bab 3.3. Dalam fungsi penurunan ini, kita akan menggunakan parameter berikut:

- $m$ : frase mnemonik;
- $p$ : passphrase opsional yang dipilih oleh pengguna untuk meningkatkan keamanan seed. Jika tidak ada passphrase, bidang ini dibiarkan kosong;
- $\text{PBKDF2}$ : fungsi penurunan dengan $\text{HMAC-SHA512}$ dan $2048$ iterasi;
- $s$: seed dompet 512-bit.
Terlepas dari panjang frase mnemonik yang dipilih (132 bit atau 264 bit), fungsi PBKDF2 akan selalu menghasilkan output 512-bit, dan seed akan selalu berukuran demikian.

### Skema Penurunan Seed dengan PBKDF2

Persamaan berikut mengilustrasikan penurunan seed dari frase mnemonik dan passphrase:


$$

s = \text{PBKDF2}_{\text{HMAC-SHA512}}(m, p, 2048)

$$

![CYP201](assets/fr/044.webp)

Nilai seed ini dipengaruhi oleh nilai frase mnemonik dan passphrase. Dengan mengubah passphrase, seed yang berbeda diperoleh. Namun, dengan frase mnemonik dan passphrase yang sama, seed yang sama selalu dihasilkan, karena PBKDF2 adalah fungsi deterministik. Ini memastikan bahwa pasangan kunci yang sama dapat diambil kembali melalui cadangan kita.

**Catatan:** Dalam bahasa umum, istilah "seed" sering kali merujuk, karena penyalahgunaan bahasa, ke frase mnemonik. Memang, tanpa passphrase, satu hanyalah pengkodean dari yang lain. Namun, seperti yang telah kita lihat, dalam realitas teknis dompet, seed dan frase mnemonik memang dua elemen yang berbeda.

Sekarang kita memiliki seed kita, kita dapat melanjutkan dengan penurunan dompet Bitcoin kita.
### Kunci Utama dan Kode Rantai Utama
Setelah benih diperoleh, langkah selanjutnya dalam menghasilkan dompet HD melibatkan perhitungan kunci privat utama dan kode rantai utama, yang akan mewakili kedalaman 0 dari dompet kita.

Untuk mendapatkan kunci privat utama dan kode rantai utama, fungsi HMAC-SHA512 diterapkan pada benih, menggunakan kunci tetap "*Bitcoin Seed*" yang identik untuk semua pengguna Bitcoin. Konstanta ini dipilih untuk memastikan bahwa derivasi kunci spesifik untuk Bitcoin. Berikut adalah elemennya:
- $\text{HMAC-SHA512}$: fungsi derivasi;
- $s$: benih dompet 512-bit;
- $\text{"Bitcoin Seed"}$: konstanta derivasi umum untuk semua dompet Bitcoin.


$$

\text{output} = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)

$$

Output dari fungsi ini adalah 512 bit. Kemudian dibagi menjadi 2 bagian:
- 256 bit kiri membentuk **kunci privat utama**;
- 256 bit kanan membentuk **kode rantai utama**.

Secara matematis, kedua nilai ini dapat dicatat sebagai berikut dengan $k_M$ sebagai kunci privat utama dan $C_M$ sebagai kode rantai utama:


$$
k_M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)_{[:256]}
$$

$$
C_M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)_{[256:]}
$$


![CYP201](assets/fr/045.webp)

### Peran Kunci Utama dan Kode Rantai

Kunci privat utama dianggap sebagai kunci induk, dari mana semua kunci privat turunan — anak, cucu, cicit, dan seterusnya — akan dihasilkan. Ini mewakili level nol dalam hierarki derivasi.

Kode rantai utama, di sisi lain, memperkenalkan sumber entropi tambahan ke dalam proses derivasi kunci untuk anak-anak, untuk mengatasi serangan potensial tertentu. Selain itu, dalam dompet HD, setiap pasangan kunci memiliki kode rantai unik yang terkait dengannya, yang juga digunakan untuk menurunkan kunci anak dari pasangan ini, tetapi kita akan membahas ini lebih detail di bab mendatang.

Sebelum melanjutkan dengan derivasi dompet HD dengan elemen berikutnya, saya ingin, di bab selanjutnya, memperkenalkan Anda pada kunci terluas, yang sering kali disalahpahami sebagai kunci utama. Kita akan melihat bagaimana mereka dibangun dan peran apa yang mereka mainkan dalam dompet Bitcoin.

## Kunci Terluas
<chapterId>8dcffce1-31bd-5e0b-965b-735f5f9e4602</chapterId>

Kunci terluas hanyalah penggabungan dari sebuah kunci (baik privat maupun publik) dan kode rantai yang terkait dengannya. Kode rantai ini penting untuk derivasi kunci anak karena, tanpanya, mustahil untuk menurunkan kunci anak dari kunci induk, tetapi kita akan menemukan proses ini lebih tepat di bab berikutnya. Kunci terluas ini memungkinkan penggabungan semua informasi yang diperlukan untuk menurunkan kunci anak, dengan demikian menyederhanakan manajemen akun dalam dompet HD.

![CYP201](assets/fr/046.webp)

Kunci terluas terdiri dari dua bagian:
- Muatan, yang berisi kunci privat atau publik serta kode rantai yang terkait;
- Metadata, yang merupakan berbagai informasi untuk memfasilitasi interoperabilitas antar perangkat lunak dan meningkatkan pemahaman bagi pengguna.

### Cara Kerja Kunci Terluas
Ketika kunci yang diperluas mengandung kunci privat, ini disebut sebagai kunci privat yang diperluas. Ini dikenali dari prefiksnya yang mengandung sebutan `prv`. Selain kunci privat, kunci privat yang diperluas juga mengandung kode rantai yang terkait. Dengan jenis kunci yang diperluas ini, dimungkinkan untuk menurunkan semua jenis kunci privat anak, dan oleh karena itu dengan penambahan dan penggandaan titik pada kurva elips, ini juga memungkinkan untuk penurunan keseluruhan kunci publik anak.

Ketika kunci yang diperluas tidak mengandung kunci privat, tetapi sebaliknya, sebuah kunci publik, ini disebut sebagai kunci publik yang diperluas. Ini dikenali dari prefiksnya yang mengandung sebutan `pub`. Jelas, selain kunci, ini juga mengandung kode rantai yang terkait. Tidak seperti kunci privat yang diperluas, kunci publik yang diperluas memungkinkan untuk penurunan hanya kunci publik anak "normal" (berarti tidak dapat menurunkan kunci anak "hardened"). Kita akan melihat dalam bab berikutnya apa arti kualifikasi "normal" dan "hardened" ini.

Namun dalam kasus apapun, kunci publik yang diperluas tidak memungkinkan untuk penurunan kunci privat anak. Oleh karena itu, meskipun seseorang memiliki akses ke `xpub`, mereka tidak akan dapat menghabiskan dana yang terkait, karena mereka tidak akan memiliki akses ke kunci privat yang sesuai. Mereka hanya dapat menurunkan kunci publik anak untuk mengamati transaksi yang terkait.

Untuk selanjutnya, kita akan mengadopsi notasi berikut:
- $K_{\text{PAR}}$: sebuah kunci publik orang tua;
- $k_{\text{PAR}}$: sebuah kunci privat orang tua;
- $C_{\text{PAR}}$: sebuah kode rantai orang tua;
- $C_{\text{CHD}}$: sebuah kode rantai anak;
- $K_{\text{CHD}}^n$: sebuah kunci publik anak normal;
- $k_{\text{CHD}}^n$: sebuah kunci privat anak normal;
- $K_{\text{CHD}}^h$: sebuah kunci publik anak hardened;
- $k_{\text{CHD}}^h$: sebuah kunci privat anak hardened.

![CYP201](assets/fr/047.webp)

### Konstruksi Kunci yang Diperluas

Sebuah kunci yang diperluas terstruktur sebagai berikut:
- **Versi**: Kode versi untuk mengidentifikasi sifat kunci (`xprv`, `xpub`, `yprv`, `ypub`...). Kita akan melihat di akhir bab ini apa yang dimaksud dengan huruf `x`, `y`, dan `z`.
- **Kedalaman**: Tingkat hierarkis dalam dompet HD relatif terhadap kunci induk (0 untuk kunci induk).
- **Sidik Jari Orang Tua**: 4 byte pertama dari hash HASH160 dari kunci publik orang tua yang digunakan untuk menurunkan kunci yang ada dalam muatan.
- **Nomor Indeks**: Pengidentifikasi anak di antara kunci saudara, yaitu, di antara semua kunci pada tingkat turunan yang sama yang memiliki kunci orang tua yang sama.
- **Kode Rantai**: Kode unik 32-byte untuk menurunkan kunci anak.
- **Kunci**: Kunci privat (diprefiks dengan 1 byte untuk ukuran) atau kunci publik.
- **Checksum**: Sebuah checksum yang dihitung dengan fungsi HASH256 (SHA256 ganda) juga ditambahkan, yang memungkinkan untuk verifikasi integritas kunci yang diperluas selama transmisi atau penyimpanannya.

Format lengkap dari kunci yang diperluas oleh karena itu adalah 78 byte tanpa checksum, dan 82 byte dengan checksum. Kemudian dikonversi ke Base58 untuk menghasilkan representasi yang mudah dibaca oleh pengguna. Format Base58 sama dengan yang digunakan untuk alamat penerima *Legacy* (sebelum *SegWit*).

| Elemen            | Deskripsi                                                                                                          | Ukuran    |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ | --------- |
| Versi             | Menunjukkan apakah kunci tersebut publik (`xpub`, `ypub`) atau privat (`xprv`, `zprv`), serta versi dari kunci ekstensi | 4 byte    |
| Kedalaman         | Level dalam hierarki relatif terhadap kunci induk                                                                   | 1 byte    |
| Sidik Jari Orang Tua | 4 byte pertama dari HASH160 dari kunci publik orang tua                                                             | 4 byte    |
| Nomor Indeks      | Posisi kunci dalam urutan anak-anak                                                                                  | 4 byte    |
| Kode Rantai       | Digunakan untuk menurunkan kunci anak                                                                               | 32 byte   |
| Kunci             | Kunci privat (dengan awalan 1-byte) atau kunci publik                                                               | 33 byte   |
| Checksum          | Checksum untuk memverifikasi integritas                                                                             | 4 byte    |

Jika satu byte ditambahkan ke kunci privat saja, itu karena kunci publik yang dikompresi lebih panjang dari kunci privat sebanyak satu byte. Byte tambahan ini, ditambahkan di awal kunci privat sebagai `0x00`, menyamakan ukurannya, memastikan bahwa muatan dari kunci ekstensi memiliki panjang yang sama, apakah itu kunci publik atau kunci privat.

### Awalan Kunci Ekstensi
Seperti yang baru saja kita lihat, kunci ekstensi mencakup awalan yang menunjukkan baik versi dari kunci ekstensi tersebut maupun sifatnya. Notasi `pub` menunjukkan bahwa itu merujuk pada kunci publik ekstensi, dan notasi `prv` menunjukkan kunci privat ekstensi. Huruf tambahan di dasar kunci ekstensi membantu menunjukkan apakah standar yang diikuti adalah Legacy, SegWit v0, SegWit v1, dll.
Berikut adalah ringkasan dari awalan yang digunakan dan artinya:

| Base 58 Prefix  | Base 16 Prefix  | Network | Purpose             | Associated Scripts  | Derivation            | Key Type     |
| --------------- | --------------- | ------- | ------------------- | ------------------- | --------------------- | ------------ |
| `xpub`          | `0488b21e`      | Mainnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/0'`, `m/86'/0'` | public       |
| `xprv`          | `0488ade4`      | Mainnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/0'`, `m/86'/0'` | private      |
| `tpub`          | `043587cf`      | Testnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/1'`, `m/86'/1'` | public       |
| `tprv`          | `04358394`      | Testnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/1'`, `m/86'/1'` | private      |
| `ypub`          | `049d7cb2`      | Mainnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/0'`             | public       |
| `yprv`          | `049d7878`      | Mainnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/0'`             | private      |
| `upub`          | `049d7cb2`      | Testnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/1'`             | public       |
| `uprv`          | `044a4e28`      | Testnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/1'`             | private      |
| `zpub`          | `04b24746`      | Mainnet | SegWit V0           | P2WPKH              | `m/84'/0'`             | public       |
| `zprv`          | `04b2430c`      | Mainnet | SegWit V0           | P2WPKH              | `m/84'/0'`             | private      |
| `vpub`          | `045f1cf6`      | Testnet | SegWit V0           | P2WPKH              | `m/84'/1'`             | public       |
| `vprv`          | `045f18bc`      | Testnet | SegWit V0           | P2WPKH              | `m/84'/1'`             | private      |


### Detail Elemen Kunci Ekstensi

Untuk lebih memahami struktur internal dari sebuah kunci ekstensi, mari kita ambil satu sebagai contoh dan pecahkan. Berikut adalah sebuah kunci ekstensi:

- **Dalam Base58**:

```text
xpub6CTNzMUkzpurBWaT4HQoYzLP4uBbGJuWY358Rj7rauiw4rMHCyq3Rfy9w4kyJXJzeFfyrKLUar2rUCukSiDQFa7roTwzjiAhyQAdPLEjqHT
```

- **Dalam heksadesimal**:

```text
0488B21E036D5601AD80000000C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A89303772CCB99F4EF346078D167065404EED8A58787DED31BFA479244824DF50658051F067C3A
```

Kunci ekstensi ini terpecah menjadi beberapa elemen berbeda:

1. **Versi**: `0488B21E`

4 byte pertama adalah versi. Di sini, ini sesuai dengan kunci publik ekstensi pada Mainnet dengan tujuan derivasi baik *Legacy* atau *SegWit v1*.

2. **Kedalaman**: `03`

Bidang ini menunjukkan tingkat hierarkis kunci dalam dompet HD. Dalam kasus ini, kedalaman `03` berarti bahwa kunci ini adalah tiga tingkat derivasi di bawah kunci induk.

3. **Sidik jari induk**: `6D5601AD`
Ini adalah 4 byte pertama dari hash HASH160 dari kunci publik induk yang digunakan untuk menurunkan `xpub` ini.
4. **Nomor Indeks**: `80000000`

Indeks ini menunjukkan posisi kunci di antara anak-anak induknya. Prefiks `0x80` menunjukkan bahwa kunci diturunkan dengan cara yang diperketat, dan karena sisanya diisi dengan nol, ini menunjukkan bahwa kunci ini adalah yang pertama di antara saudara kandungnya yang mungkin.

5. **Kode Rantai**: `C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A893`
6. **Kunci Publik**: `03772CCB99F4EF346078D167065404EED8A58787DED31BFA479244824DF5065805`
7. **Checksum**: `1F067C3A`

Checksum ini sesuai dengan 4 byte pertama dari hash (SHA256 ganda) dari semua yang lain.

Dalam bab ini, kita menemukan bahwa ada dua jenis kunci anak yang berbeda. Kita juga belajar bahwa derivasi kunci anak ini memerlukan sebuah kunci (baik privat maupun publik) dan kode rantainya. Dalam bab selanjutnya, kita akan memeriksa secara detail sifat dari berbagai jenis kunci ini dan bagaimana menurunkannya dari kunci induk dan kode rantainya.

## Derivasi Pasangan Kunci Anak
<chapterId>61c0807c-845b-5076-ad06-7f395b36adfd</chapterId>

Derivasi pasangan kunci anak dalam dompet HD Bitcoin bergantung pada struktur hierarkis yang memungkinkan menghasilkan sejumlah besar kunci, sambil mengorganisir pasangan ini ke dalam kelompok yang berbeda melalui cabang. Setiap pasangan anak yang diturunkan dari pasangan induk dapat digunakan langsung dalam *scriptPubKey* untuk mengunci bitcoin, atau sebagai titik awal untuk menghasilkan lebih banyak kunci anak, dan seterusnya, untuk menciptakan pohon kunci.

Semua derivasi ini dimulai dengan kunci induk dan kode rantai induk, yang merupakan orang tua pertama pada tingkat kedalaman 0. Mereka, dalam suatu cara, adalah Adam dan Hawa dari kunci dompet Anda, leluhur bersama dari semua kunci yang diturunkan.

![CYP201](assets/fr/048.webp)

Mari kita jelajahi bagaimana derivasi deterministik ini bekerja.

### Berbagai Jenis Derivasi Kunci Anak

Seperti yang kita singgung secara singkat di bab sebelumnya: kunci anak dibagi menjadi dua jenis utama:
1. **Kunci anak normal** ($k_{\text{CHD}}^n, K_{\text{CHD}}^n$): Ini diturunkan dari kunci publik terluas ($K_{\text{PAR}}$), atau kunci privat terluas ($k_{\text{PAR}}$), dengan pertama-tama menurunkan kunci publik.
2. **Kunci anak diperketat** ($k_{\text{CHD}}^h, K_{\text{CHD}}^h$): Ini hanya dapat diturunkan dari kunci privat terluas ($k_{\text{PAR}}$) dan oleh karena itu tidak terlihat oleh pengamat yang hanya memiliki kunci publik terluas.
Setiap pasangan kunci anak diidentifikasi oleh sebuah **indeks** 32-bit (dinamakan $i$ dalam perhitungan kami). Indeks untuk kunci normal berkisar dari $0$ sampai $2^{31}-1$, sementara itu untuk kunci yang diperkuat berkisar dari $2^{31}$ sampai $2^{32}-1$. Angka-angka ini digunakan untuk membedakan pasangan kunci saudara selama derivasi. Memang, setiap pasangan kunci induk harus mampu menghasilkan beberapa pasangan kunci anak. Jika kita menerapkan perhitungan yang sama secara sistematis dari kunci induk, semua kunci saudara yang diperoleh akan identik, yang tidak diinginkan. Indeks dengan demikian memperkenalkan variabel yang memodifikasi perhitungan derivasi, memungkinkan setiap pasangan saudara dapat dibedakan. Kecuali untuk penggunaan spesifik dalam protokol tertentu dan standar derivasi, umumnya kita mulai dengan menghasilkan kunci anak pertama dengan indeks `0`, yang kedua dengan indeks `1`, dan seterusnya.
### Proses Derivasi dengan HMAC-SHA512

Derivasi setiap kunci anak didasarkan pada fungsi HMAC-SHA512, yang telah kita bahas di Bagian 2 tentang fungsi hash. Ini mengambil dua input: kode rantai induk $C_{\text{PAR}}$ dan penggabungan kunci induk (baik kunci publik $K_{\text{PAR}}$ atau kunci privat $k_{\text{PAR}}$, tergantung pada jenis kunci anak yang diinginkan) dan indeks. Output dari HMAC-SHA512 adalah urutan 512-bit, dibagi menjadi dua bagian:
- **32 byte pertama** (atau $h_1$) digunakan untuk menghitung pasangan anak baru.
- **32 byte terakhir** (atau $h_2$) berfungsi sebagai kode rantai baru $C_{\text{CHD}}$ untuk pasangan anak.

Dalam semua perhitungan kami, saya akan menandai $\text{hash}$ output dari fungsi HMAC-SHA512.

![CYP201](assets/fr/049.webp)

#### Derivasi Kunci Privat Anak dari Kunci Privat Induk

Untuk menghasilkan kunci privat anak $k_{\text{CHD}}$ dari kunci privat induk $k_{\text{PAR}}$, dua skenario mungkin tergantung pada apakah kunci yang diperkuat atau normal yang diinginkan.

Untuk **kunci anak normal** ($i < 2^{31}$), perhitungan $\text{hash}$ adalah sebagai berikut:


$$

\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}}, G \cdot k_{\text{PAR}} \Vert i)

$$

Dalam perhitungan ini, kita melihat bahwa fungsi HMAC kita mengambil dua input: pertama, kode rantai induk, dan kemudian penggabungan indeks dengan kunci publik yang terkait dengan kunci privat induk. Kunci publik induk digunakan di sini karena kita mencari untuk menghasilkan kunci anak normal, bukan yang diperkuat.
Sekarang kita memiliki $\text{hash}$ 64-byte yang akan kita bagi menjadi 2 bagian masing-masing 32 byte: $h_1$ dan $h_2$:


$$

\text{hash} = h_1 \Vert h_2

$$


$$

h*1 = \text{hash}_{[:32]} \quad, \quad h*2 = \text{hash}_{[32:]}

$$

Kunci privat anak $k_{\text{CHD}}^n$ kemudian dihitung sebagai berikut:


$$

k_{\text{CHD}}^n = \text{parse256}(h_1) + k_{\text{PAR}} \mod n

$$
Dalam perhitungan ini, operasi $\text{parse256}(h_1)$ terdiri dari interpretasi 32 byte pertama dari $\text{hash}$ sebagai bilangan bulat 256-bit. Angka ini kemudian ditambahkan ke kunci privat induk, semuanya diambil modulo $n$ untuk tetap dalam urutan kurva eliptik, seperti yang kita lihat di bagian 3 tentang tanda tangan digital. Jadi, untuk menurunkan kunci privat anak yang normal, meskipun kunci publik induk digunakan sebagai dasar perhitungan dalam input fungsi HMAC-SHA512, selalu diperlukan kunci privat induk untuk menyelesaikan perhitungan.
Dari kunci privat anak ini, dimungkinkan untuk menurunkan kunci publik yang sesuai dengan menerapkan ECDSA atau Schnorr. Dengan cara ini, kita memperoleh sepasang kunci yang lengkap.

Kemudian, bagian kedua dari $\text{hash}$ hanya diinterpretasikan sebagai kode rantai untuk pasangan kunci anak yang baru saja kita turunkan:


$$

C\_{\text{CHD}} = h_2

$$

Berikut adalah representasi skematik dari keseluruhan turunan:

![CYP201](assets/fr/050.webp)

Untuk **kunci anak yang diperkuat** ($i \geq 2^{31}$), perhitungan $\text{hash}$ adalah sebagai berikut:


$$

hash = \text{HMAC-SHA512}(C_{\text{PAR}}, 0x00 \Vert k_{\text{PAR}} \Vert i)

$$

Dalam perhitungan ini, kita melihat bahwa fungsi HMAC kita mengambil dua input: pertama, kode rantai induk, dan kemudian penggabungan indeks dengan kunci privat induk. Kunci privat induk digunakan di sini karena kita mencari untuk menurunkan kunci anak yang diperkuat. Selain itu, byte yang sama dengan `0x00` ditambahkan di awal kunci. Operasi ini menyamakan panjangnya agar sesuai dengan kunci publik yang dikompresi.
Jadi, sekarang kita memiliki $\text{hash}$ 64-byte yang akan kita bagi menjadi 2 bagian masing-masing 32 byte: $h_1$ dan $h_2$:
$$

\text{hash} = h_1 \Vert h_2

$$


$$

h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]

$$

Kunci privat anak $k_{\text{CHD}}^h$ kemudian dihitung sebagai berikut:


$$

k_{\text{CHD}}^h = \text{parse256}(h_1) + k_{\text{PAR}} \mod n

$$

Selanjutnya, kita hanya menginterpretasikan bagian kedua dari $\text{hash}$ sebagai kode rantai untuk pasangan kunci anak yang baru saja kita turunkan:


$$

C\_{\text{CHD}} = h_2

$$

Berikut adalah representasi skematik dari keseluruhan turunan:

![CYP201](assets/fr/051.webp)

Kita dapat melihat bahwa turunan normal dan turunan yang diperkuat berfungsi dengan cara yang sama, dengan perbedaan ini: turunan normal menggunakan kunci publik induk sebagai input ke fungsi HMAC, sementara turunan yang diperkuat menggunakan kunci privat induk.

#### Menurunkan kunci publik anak dari kunci publik induk
Jika kita hanya mengetahui kunci publik induk $K_{\text{PAR}}$ dan kode rantai yang terkait $C_{\text{PAR}}$, yaitu, sebuah kunci publik ekstensi, maka dimungkinkan untuk menurunkan kunci publik anak $K_{\text{CHD}}^n$, tetapi hanya untuk kunci anak normal (non-hardened). Prinsip ini memungkinkan pemantauan pergerakan akun dalam dompet Bitcoin dari `xpub` (*hanya-pantau*).
Untuk melakukan perhitungan ini, kita akan menghitung $\text{hash}$ dengan indeks $i < 2^{31}$ (turunan normal):


$$

\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}}, K_{\text{PAR}} \Vert i)

$$

Dalam perhitungan ini, kita melihat bahwa fungsi HMAC kita mengambil dua input: pertama kode rantai induk, kemudian penggabungan indeks dengan kunci publik induk.

Jadi, sekarang kita memiliki $hash$ sebesar 64 byte yang akan kita bagi menjadi 2 bagian masing-masing 32 byte: $h_1$ dan $h_2$:


$$

\text{hash} = h_1 \Vert h_2

$$


$$

h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]

$$

Kunci publik anak $K_{\text{CHD}}^n$ kemudian dihitung sebagai berikut:


$$

K_{\text{CHD}}^n = G \cdot \text{parse256}(h_1) + K_{\text{PAR}}

$$
Jika $\text{parse256}(h_1) \geq n$ (urutan kurva eliptik) atau jika $K_{\text{CHD}}^n$ adalah titik di tak hingga, turunan tersebut tidak valid, dan indeks lain harus dipilih.
Dalam perhitungan ini, operasi $\text{parse256}(h_1)$ melibatkan interpretasi 32 byte pertama dari $\text{hash}$ sebagai bilangan bulat 256-bit. Angka ini digunakan untuk menghitung titik pada kurva eliptik melalui penambahan dan penggandaan dari titik generator $G$. Titik ini kemudian ditambahkan ke kunci publik induk untuk mendapatkan kunci publik anak normal. Jadi, untuk menurunkan kunci publik anak normal, hanya kunci publik induk dan kode rantai induk yang diperlukan; kunci privat induk tidak pernah terlibat dalam proses ini, tidak seperti perhitungan kunci privat anak yang kita lihat sebelumnya.

Selanjutnya, kode rantai anak hanyalah:


$$

C\_{\text{CHD}} = h_2

$$

Berikut adalah representasi skematik dari turunan keseluruhan:

![CYP201](assets/fr/052.webp)

### Korespondensi antara kunci publik dan privat anak

Pertanyaan yang mungkin muncul adalah bagaimana kunci publik anak normal yang diturunkan dari kunci publik induk dapat sesuai dengan kunci privat anak normal yang diturunkan dari kunci privat induk yang sesuai. Tautan ini tepatnya dijamin oleh sifat-sifat kurva eliptik. Memang, untuk menurunkan kunci publik anak normal, HMAC-SHA512 diterapkan dengan cara yang sama, tetapi outputnya digunakan secara berbeda:
   - **Kunci privat anak normal**: $k_{\text{CHD}}^n = \text{parse256}(h_1) + k_{\text{PAR}} \mod n$
   - **Kunci publik anak normal**: $K_{\text{CHD}}^n = G \cdot \text{parse256}(h_1) + K_{\text{PAR}}$
Terima kasih kepada operasi penambahan dan penggandaan pada kurva eliptik, kedua metode tersebut menghasilkan hasil yang konsisten: kunci publik yang berasal dari kunci privat anak identik dengan kunci publik anak yang berasal langsung dari kunci publik orang tua.

### Ringkasan Jenis-jenis Turunan

Untuk merangkum, berikut adalah berbagai jenis turunan yang mungkin:

$$
\begin{array}{|c|c|c|c|}
\hline
\rightarrow & \text{PAR} & \text{CHD} & \text{n/h} \\
\hline
k_{\text{PAR}} \rightarrow k_{\text{CHD}} & k_{\text{PAR}} & \{ k_{\text{CHD}}^n, k_{\text{CHD}}^h \} & \{ n, h \} \\
k_{\text{PAR}} \rightarrow K_{\text{CHD}} & k_{\text{PAR}} & \{ K_{\text{CHD}}^n, K_{\text{CHD}}^h \} & \{ n, h \} \\
K_{\text{PAR}} \rightarrow k_{\text{CHD}} & K_{\text{PAR}} & \times & \times \\
K_{\text{PAR}} \rightarrow K_{\text{CHD}} & K_{\text{PAR}} & K_{\text{CHD}}^n & n \\
\hline
\end{array}
$$

Untuk merangkum, sejauh ini Anda telah belajar untuk menciptakan elemen dasar dari dompet HD: frasa mnemonik, benih, dan kemudian kunci utama serta kode rantai utama. Anda juga telah menemukan cara untuk menurunkan pasangan kunci anak dalam bab ini. Dalam bab berikutnya, kita akan menjelajahi bagaimana turunan-turunan ini disusun dalam dompet Bitcoin dan struktur apa yang harus diikuti untuk secara konkret mendapatkan alamat penerima serta pasangan kunci yang digunakan dalam *scriptPubKey* dan *scriptSig*.

## Struktur Dompet dan Jalur Turunan
<chapterId>34e1bbda-67de-5493-b268-1fded8d67689</chapterId>

Struktur hierarkis dari dompet HD pada Bitcoin memungkinkan untuk pengorganisasian pasangan kunci dengan berbagai cara. Ide ini adalah untuk menurunkan, dari kunci privat utama dan kode rantai utama, beberapa tingkat kedalaman. Setiap tingkat yang ditambahkan sesuai dengan turunan dari pasangan kunci anak dari pasangan kunci orang tua.

Seiring waktu, BIP yang berbeda telah memperkenalkan standar untuk jalur turunan ini, dengan tujuan untuk menstandarisasi penggunaannya di berbagai perangkat lunak. Jadi, dalam bab ini, kita akan menemukan makna dari setiap tingkat turunan dalam dompet HD, sesuai dengan standar ini.

### Kedalaman Turunan dari Dompet HD

Jalur turunan disusun ke dalam lapisan kedalaman, mulai dari kedalaman 0, yang mewakili kunci utama dan kode rantai utama, hingga lapisan sub-level untuk menurunkan alamat yang digunakan untuk mengunci UTXO. BIP (*Bitcoin Improvement Proposals*) mendefinisikan standar untuk setiap lapisan, yang membantu untuk menyelaraskan praktik di berbagai perangkat lunak manajemen dompet.

Sebuah jalur turunan, oleh karena itu, merujuk pada urutan indeks yang digunakan untuk menurunkan kunci anak dari kunci utama.

**Kedalaman 0: Kunci Utama (BIP32)**

Kedalaman ini sesuai dengan kunci privat utama dan kode rantai utama dompet. Ini diwakili oleh notasi $m/$.

**Kedalaman 1: Tujuan (BIP43)**
Tujuan menentukan struktur logis dari turunan. Sebagai contoh, alamat P2WPKH akan memiliki $/84'/$ pada kedalaman 1 (menurut BIP84), sementara alamat P2TR akan memiliki $/86'/$ (menurut BIP86). Lapisan ini memfasilitasi kompatibilitas antar dompet dengan menunjukkan nomor indeks yang sesuai dengan nomor BIP.

Dengan kata lain, setelah Anda memiliki kunci induk dan kode rantai induk, ini berfungsi sebagai pasangan kunci induk untuk menurunkan pasangan kunci anak. Indeks yang digunakan dalam turunan ini bisa, sebagai contoh, $/84'/$ jika dompet dimaksudkan untuk menggunakan skrip tipe SegWit v0. Pasangan kunci ini kemudian berada pada kedalaman 1. Perannya bukan untuk mengunci bitcoin, tetapi hanya untuk berfungsi sebagai titik perhentian dalam hierarki turunan.

**Kedalaman 2: Tipe Mata Uang (BIP44)**

Dari pasangan kunci pada kedalaman 1, turunan baru dilakukan untuk mendapatkan pasangan kunci pada kedalaman 2. Kedalaman ini memungkinkan pembedaan akun Bitcoin dari mata uang kripto lainnya dalam dompet yang sama.

Setiap mata uang memiliki indeks unik untuk memastikan kompatibilitas lintas dompet multi-mata uang. Sebagai contoh, untuk Bitcoin, indeksnya adalah $/0'/$ (atau `0x80000000` dalam notasi heksadesimal). Indeks mata uang dipilih dalam rentang dari $2^{31}$ hingga $2^{32}-1$ untuk memastikan turunan yang diperkuat.

Untuk memberi Anda contoh lain, berikut adalah indeks dari beberapa mata uang:
- $1'$ (`0x80000001`) untuk bitcoin testnet;
- $2'$ (`0x80000002`) untuk Litecoin;
- $60'$ (`0x8000003c`) untuk Ethereum...

**Kedalaman 3: Akun (BIP32)**

Setiap dompet dapat dibagi menjadi beberapa akun, bernomor dari $2^{31}$, dan diwakili pada kedalaman 3 oleh $/0'/$ untuk akun pertama, $/1'/$ untuk kedua, dan seterusnya. Umumnya, ketika merujuk pada kunci terluas `xpub`, ini merujuk pada kunci pada kedalaman turunan ini.

Pemisahan ke dalam akun yang berbeda ini opsional. Ini bertujuan untuk menyederhanakan organisasi dompet bagi pengguna. Dalam praktiknya, seringkali hanya satu akun yang digunakan, biasanya yang pertama secara default. Namun, dalam beberapa kasus, jika seseorang ingin membedakan pasangan kunci untuk penggunaan yang berbeda secara jelas, ini bisa berguna. Sebagai contoh, dimungkinkan untuk membuat akun pribadi dan akun profesional dari benih yang sama, dengan kelompok kunci yang sepenuhnya berbeda dari kedalaman turunan ini.
**Kedalaman 4: Rantai (BIP32)**
Setiap akun yang ditentukan pada kedalaman 3 kemudian terstruktur menjadi dua rantai:
- **Rantai eksternal**: Dalam rantai ini, apa yang dikenal sebagai alamat "publik" diturunkan. Alamat penerima ini dimaksudkan untuk mengunci UTXO yang datang dari transaksi eksternal (yaitu, berasal dari konsumsi UTXO yang tidak milik Anda). Secara sederhana, rantai eksternal ini digunakan kapan pun seseorang ingin menerima bitcoin. Ketika Anda mengklik "*terima*" di perangkat lunak dompet Anda, selalu alamat dari rantai eksternal yang ditawarkan kepada Anda. Rantai ini diwakili oleh pasangan kunci yang diturunkan dengan indeks $/0/$.
- **Rantai internal (kembalian)**: Rantai ini diperuntukkan bagi alamat penerima yang mengunci bitcoin yang berasal dari konsumsi UTXO yang milik Anda, dengan kata lain, alamat kembalian. Ini diidentifikasi oleh indeks $/1/$.

**Kedalaman 5: Indeks Alamat (BIP32)**
Akhirnya, kedalaman 5 mewakili langkah terakhir dari derivasi dalam dompet. Meskipun secara teknis mungkin untuk terus berlanjut tanpa batas, standar saat ini berhenti di sini. Pada kedalaman akhir ini, pasangan kunci yang akan benar-benar digunakan untuk mengunci dan membuka UTXO diturunkan. Setiap indeks memungkinkan membedakan antara pasangan kunci saudara: dengan demikian, alamat penerima pertama akan menggunakan indeks $/0/$, yang kedua menggunakan indeks $/1/$, dan seterusnya.
![CYP201](assets/fr/053.webp)

### Notasi Jalur Derivasi

Jalur derivasi ditulis dengan memisahkan setiap tingkat dengan garis miring ($/$). Setiap garis miring menunjukkan derivasi dari pasangan kunci induk ($k_{\text{PAR}}$, $K_{\text{PAR}}$, $C_{\text{PAR}}$) ke pasangan kunci anak ($k_{\text{CHD}}$, $K_{\text{CHD}}$, $C_{\text{CHD}}$). Nomor yang dicatat pada setiap kedalaman sesuai dengan indeks yang digunakan untuk menurunkan kunci ini dari induknya. Tanda petik satu ($'$) yang terkadang diletakkan di sebelah kanan indeks menunjukkan derivasi yang diperkuat ($k_{\text{CHD}}^h$, $K_{\text{CHD}}^h$). Terkadang, tanda petik satu ini digantikan oleh $h$. Dalam ketiadaan tanda petik satu atau $h$, ini adalah derivasi normal ($k_{\text{CHD}}^n$, $K_{\text{CHD}}^n$).
Seperti yang telah kita lihat dalam bab-bab sebelumnya, indeks kunci yang diperkuat dimulai dari $2^{31}$, atau `0x80000000` dalam heksadesimal. Oleh karena itu, ketika sebuah indeks diikuti oleh tanda petik satu dalam jalur derivasi, $2^{31}$ harus ditambahkan ke angka yang ditunjukkan untuk mendapatkan nilai sebenarnya yang digunakan dalam fungsi HMAC-SHA512. Misalnya, jika jalur derivasi menentukan $/44'/$, indeks sebenarnya akan menjadi:
$$

i = 44 + 2^{31} = 2\,147\,483\,692

$$

Dalam heksadesimal, ini adalah `0x8000002C`.

Sekarang setelah kita telah memahami prinsip utama jalur derivasi, mari kita ambil contoh! Berikut adalah jalur derivasi untuk alamat penerima Bitcoin:


$$

m / 84' / 0' / 1' / 0 / 7

$$

Dalam contoh ini:
- $84'$ menunjukkan standar P2WPKH (SegWit v0);
- $0'$ menunjukkan mata uang Bitcoin di mainnet;
- $1'$ sesuai dengan akun kedua dalam dompet;
- $0$ menunjukkan bahwa alamat berada di rantai eksternal;
- $7$ menunjukkan alamat eksternal ke-8 dari akun ini.

### Ringkasan Struktur Derivasi

| Kedalaman | Deskripsi        | Contoh Standar                  |
| --------- | ---------------- | ------------------------------- |
| 0         | Kunci Utama      | $m/$                            |
| 1         | Tujuan           | $/86'/$ (P2TR)                  |
| 2         | Mata Uang        | $/0'/$ (Bitcoin)                |
| 3         | Akun             | $/0'/$ (Akun pertama)           |
| 4         | Rantai           | $/0/$ (eksternal) atau $/1/$ (perubahan)|
| 5         | Indeks Alamat    | $/0/$ (alamat pertama)          |
Pada bab selanjutnya, kita akan menemukan apa itu "*output script descriptors*", sebuah inovasi yang baru diperkenalkan dalam Bitcoin Core yang mempermudah pencadangan dompet Bitcoin.
## Output script descriptors
<chapterId>e4f1c2d3-9b8a-4d3e-8f2a-7b6c5d4e3f2a</chapterId>
Seringkali kita diberitahu bahwa frasa mnemonik saja sudah cukup untuk memulihkan akses ke sebuah dompet. Namun, pada kenyataannya, hal-hal bisa menjadi lebih kompleks. Pada bab sebelumnya, kita telah melihat struktur derivasi dari dompet HD, dan Anda mungkin telah menyadari bahwa proses ini cukup kompleks. Jalur derivasi memberitahu perangkat lunak arah mana yang harus diikuti untuk menurunkan kunci pengguna. Namun, ketika memulihkan dompet Bitcoin, jika seseorang tidak mengetahui jalur-jalur ini, frasa mnemonik saja tidak cukup. Ini memungkinkan untuk mendapatkan kunci induk dan kode rantai induk, tetapi kemudian diperlukan untuk mengetahui indeks yang digunakan untuk mencapai kunci anak.

Secara teoritis, akan diperlukan untuk menyimpan tidak hanya frasa mnemonik dari dompet kita, tetapi juga jalur ke akun yang kita gunakan. Dalam praktiknya, seringkali mungkin untuk mendapatkan kembali akses ke kunci anak tanpa informasi ini, asalkan standar telah diikuti. Dengan menguji setiap standar satu per satu, umumnya mungkin untuk mendapatkan kembali akses ke bitcoin. Namun, ini tidak dijamin dan ini terutama rumit bagi pemula. Juga, dengan diversifikasi jenis skrip dan munculnya konfigurasi yang lebih kompleks, informasi ini bisa menjadi sulit untuk diekstrapolasi, sehingga mengubah data ini menjadi informasi pribadi dan sulit untuk dipulihkan dengan brute force. Inilah mengapa sebuah inovasi baru-baru ini diperkenalkan dan mulai diintegrasikan ke dalam perangkat lunak dompet favorit Anda: *output script descriptors*.

### Apa itu "descriptor"?

"*Output script descriptors*", atau sederhananya "*descriptors*", adalah ekspresi terstruktur yang sepenuhnya mendeskripsikan sebuah output script (*scriptPubKey*) dan menyediakan semua informasi yang diperlukan untuk mengikuti transaksi yang terkait dengan skrip tertentu. Mereka memfasilitasi pengelolaan kunci dalam dompet HD dengan menawarkan deskripsi yang terstandarisasi dan lengkap dari struktur dompet dan jenis alamat yang digunakan.

Keuntungan utama dari descriptor terletak pada kemampuannya untuk mengenkapsulasi semua informasi esensial untuk memulihkan dompet dalam satu string (selain dari frasa pemulihan). Dengan menyimpan descriptor bersama dengan frasa mnemonik yang terkait, menjadi mungkin untuk memulihkan kunci pribadi dengan mengetahui secara tepat posisi mereka dalam hierarki. Untuk dompet multisig, yang pencadangannya awalnya lebih kompleks, descriptor mencakup `xpub` dari setiap faktor, sehingga memastikan kemungkinan untuk menghasilkan kembali alamat dalam kasus masalah.

### Konstruksi dari sebuah descriptor

Descriptor terdiri dari beberapa elemen:
* Fungsi skrip seperti `pk` (*Pay-to-PubKey*), `pkh` (*Pay-to-PubKey-Hash*), `wpkh` (*Pay-to-Witness-PubKey-Hash*), `sh` (*Pay-to-Script-Hash*), `wsh` (*Pay-to-Witness-Script-Hash*), `tr` (*Pay-to-Taproot*), `multi` (*Multisignature*), dan `sortedmulti` (*Multisignature dengan kunci yang diurutkan*);
* Jalur derivasi, misalnya, `[d34db33f/44h/0h/0h]` yang menunjukkan jalur akun yang diturunkan dan sidik jari kunci induk tertentu;
* Kunci dalam berbagai format seperti kunci publik heksadesimal atau kunci publik yang diperluas (`xpub`);
* Sebuah checksum, didahului oleh tanda hash, untuk memverifikasi integritas dari descriptor.
Sebagai contoh, deskriptor untuk dompet P2WPKH (SegWit v0) dapat terlihat seperti:
```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7nr4
```

Dalam deskriptor ini, fungsi derivasi `wpkh` menunjukkan tipe skrip *Pay-to-Witness-Public-Key-Hash*. Ini diikuti oleh jalur derivasi yang berisi:
* `cdeab12f`: sidik jari kunci utama;
* `84h`: yang menandakan penggunaan tujuan BIP84, dimaksudkan untuk alamat SegWit v0;
* `0h`: yang menunjukkan bahwa ini adalah mata uang BTC di mainnet;
* `0h`: yang merujuk pada nomor akun spesifik yang digunakan dalam dompet.

Deskriptor juga mencakup kunci publik ekstensi yang digunakan dalam dompet ini:

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```

Selanjutnya, notasi `/<0;1>/*` menentukan bahwa deskriptor dapat menghasilkan alamat dari rantai eksternal (`0`) dan rantai internal (`1`), dengan wildcard (`*`) yang memungkinkan untuk derivasi sekuensial dari beberapa alamat secara konfiguratif, mirip dengan mengelola "batas gap" pada perangkat lunak dompet tradisional.
Akhirnya, `#jy0l7nr4` mewakili checksum untuk memverifikasi integritas deskriptor.
Anda sekarang tahu segalanya tentang operasi dompet HD di Bitcoin dan proses derivasi pasangan kunci. Namun, dalam bab terakhir, kami membatasi diri pada generasi kunci privat dan publik, tanpa membahas konstruksi alamat penerima. Ini akan tepatnya menjadi subjek dari bab berikutnya!

## Alamat Penerima
<chapterId>ca80a89d-f8da-4e09-8c35-43179b65bced</chapterId>

Alamat penerima adalah potongan informasi yang tertanam dalam *scriptPubKey* untuk mengunci UTXO yang baru dibuat. Sederhananya, sebuah alamat berfungsi untuk menerima bitcoin. Mari kita jelajahi operasinya sehubungan dengan apa yang telah kita pelajari dalam bab-bab sebelumnya.

### Peran Alamat Bitcoin dalam Skrip

Seperti yang dijelaskan sebelumnya, peran transaksi adalah untuk mentransfer kepemilikan bitcoin dari input ke output. Proses ini melibatkan konsumsi UTXO sebagai input sambil menciptakan UTXO baru sebagai output. UTXO ini diamankan oleh skrip, yang mendefinisikan kondisi yang diperlukan untuk membuka dana.
Ketika seorang pengguna menerima bitcoin, pengirim membuat sebuah output UTXO dan menguncinya dengan *scriptPubKey*. Skrip ini berisi aturan yang biasanya menentukan tanda tangan dan kunci publik yang diperlukan untuk membuka UTXO ini. Untuk menghabiskan UTXO ini dalam transaksi baru, pengguna harus menyediakan informasi yang diminta melalui *scriptSig*. Eksekusi *scriptSig* bersama dengan *scriptPubKey* harus mengembalikan "true" atau `1`. Jika kondisi ini terpenuhi, UTXO dapat dihabiskan untuk membuat UTXO baru, yang dikunci oleh *scriptPubKey* baru, dan seterusnya.
![CYP201](assets/fr/054.webp)

Tepatnya dalam *scriptPubKey* tempat alamat penerima ditemukan. Namun, penggunaannya bervariasi tergantung pada standar skrip yang diadopsi. Berikut adalah tabel ringkasan informasi yang terkandung dalam *scriptPubKey* menurut standar yang digunakan, serta informasi yang diharapkan dalam *scriptSig* untuk membuka *scriptPubKey*.

| Standar            | *scriptPubKey*                                              | *scriptSig*                     | *redeem script*     | *witness*                                |
| ------------------ | ----------------------------------------------------------- | ------------------------------- | ------------------- | ---------------------------------------- |
| P2PK               | `<pubkey> OP_CHECKSIG`                                      | `<signature>`                   |                     |                                          |
| P2PKH              | `OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG` | `<signature> <public key>`      |                     |                                          |
| P2SH               | `OP_HASH160 <scriptHash> OP_EQUAL`                          | `<data pushes> <redeem script>` | Data sembarang      |                                          |
| P2WPKH             | `0 <pubKeyHash>`                                            |                                 |                     | `<signature> <public key>`               |
| P2WSH              | `0 <witnessScriptHash>`                                     |                                 |                     | `<data pushes> <witness script>`         |
| P2SH-P2WPKH        | `OP_HASH160 <redeemScriptHash> OP_EQUAL`                    | `<redeem script>`               | `0 <pubKeyHash>`    | `<signature> <public key>`               |
| P2SH-P2WSH         | `OP_HASH160 <redeemScriptHash> OP_EQUAL`                    | `<redeem script>`               | `0 <scriptHash>`    | `<data pushes> <witness script>`         |
| P2TR (jalur kunci) | `1 <public key>`                                            |                                 |                     | `<signature>`                            |
| P2TR (jalur skrip) | `1 <public key>`                                            |                                 |                     | `<data pushes> <script> <blok kontrol>`  |

*Sumber: Bitcoin Core PR review club, 7 Juli 2021 - Gloria Zhao*

Opcodes yang digunakan dalam skrip dirancang untuk memanipulasi informasi, dan, jika perlu, untuk membandingkan atau mengujinya. Mari kita ambil contoh skrip P2PKH, yang adalah sebagai berikut:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```

Seperti yang akan kita lihat dalam bab ini, `<pubKeyHash>` sebenarnya mewakili payload dari alamat penerima yang digunakan untuk mengunci UTXO. Untuk membuka *scriptPubKey* ini, diperlukan *scriptSig* yang berisi:

```text
<signature> <public key>
```
Dalam bahasa skrip, "stack" adalah struktur data "*LIFO*" ("*Last In, First Out*") yang digunakan untuk menyimpan sementara elemen selama eksekusi skrip. Setiap operasi skrip memanipulasi stack ini, di mana elemen dapat ditambahkan (*push*) atau dihapus (*pop*). Skrip menggunakan stack ini untuk mengevaluasi ekspresi, menyimpan variabel sementara, dan mengelola kondisi.
Eksekusi skrip yang baru saja saya berikan sebagai contoh mengikuti proses ini:

- Kami memiliki *scriptSig*, *ScriptPubKey*, dan stack:

![CYP201](assets/fr/055.webp)

- *scriptSig* di-push ke dalam stack:

![CYP201](assets/fr/056.webp)

- `OP_DUP` menduplikasi kunci publik yang disediakan dalam *scriptSig* di stack:

![CYP201](assets/fr/057.webp)

- `OP_HASH160` mengembalikan hash dari kunci publik yang baru saja diduplikasi:

![CYP201](assets/fr/058.webp)

- `OP_PUSHBYTES_20 <pubKeyHash>` mendorong alamat Bitcoin yang terkandung dalam *scriptPubKey* ke stack:

![CYP201](assets/fr/059.webp)

- `OP_EQUALVERIFY` memverifikasi bahwa hash kunci publik cocok dengan alamat penerima yang disediakan:

![CYP201](assets/fr/060.webp)
`OP_CHECKSIG` memeriksa tanda tangan yang terkandung dalam *scriptSig* menggunakan kunci publik. Opcode ini pada dasarnya melakukan verifikasi tanda tangan seperti yang kami jelaskan di bagian 3 dari pelatihan ini:
![CYP201](assets/fr/061.webp)

- Jika `1` tetap ada di stack, maka skrip tersebut valid:

![CYP201](assets/fr/062.webp)

Oleh karena itu, untuk merangkum, skrip ini memungkinkan verifikasi, dengan bantuan tanda tangan digital, bahwa pengguna yang mengklaim kepemilikan UTXO ini dan ingin menghabiskannya memang memiliki kunci privat yang terkait dengan alamat penerima yang digunakan selama pembuatan UTXO ini.

### Berbagai jenis alamat Bitcoin

Seiring dengan evolusi Bitcoin, beberapa model skrip standar telah ditambahkan. Masing-masing menggunakan jenis alamat penerima yang berbeda. Berikut adalah gambaran umum dari model skrip utama yang tersedia hingga saat ini:

**P2PK (*Pay-to-PubKey*)**:

Model skrip ini diperkenalkan dalam versi pertama Bitcoin oleh Satoshi Nakamoto. Skrip P2PK mengunci bitcoin langsung menggunakan kunci publik mentah (dengan demikian, tidak ada alamat penerima yang digunakan dengan model ini). Strukturnya sederhana: berisi kunci publik dan memerlukan tanda tangan digital yang sesuai untuk membuka dana. Skrip ini merupakan bagian dari standar "*Legacy*".

**P2PKH (*Pay-to-PubKey-Hash*)**:

Seperti P2PK, skrip P2PKH diperkenalkan pada peluncuran Bitcoin. Berbeda dengan pendahulunya, ia mengunci bitcoin menggunakan hash dari kunci publik, bukan langsung menggunakan kunci publik mentah. *scriptSig* kemudian harus menyediakan kunci publik yang terkait dengan alamat penerima, serta tanda tangan yang valid. Alamat yang sesuai dengan model ini dimulai dengan `1` dan dikodekan dalam *base58check*. Skrip ini juga termasuk dalam standar "*Legacy*".

**P2SH (*Pay-to-Script-Hash*)**:
Diperkenalkan pada tahun 2012 dengan BIP16, model P2SH memungkinkan penggunaan hash dari skrip sembarang dalam *scriptPubKey*. Skrip yang di-hash ini, yang disebut "*redeemScript*", berisi kondisi untuk membuka dana. Untuk menghabiskan UTXO yang dikunci dengan P2SH, diperlukan untuk menyediakan *scriptSig* yang mengandung *redeemScript* asli serta data yang diperlukan untuk memvalidasinya. Model ini terutama digunakan untuk multisig lama. Alamat yang terkait dengan P2SH dimulai dengan `3` dan dikodekan dalam *base58check*. Skrip ini juga termasuk dalam standar "*Legacy*".

**P2WPKH (*Pay-to-Witness-PubKey-Hash*)**:
Skrip ini mirip dengan P2PKH, karena juga mengunci bitcoin menggunakan hash dari kunci publik. Namun, tidak seperti P2PKH, *scriptSig* dipindahkan ke bagian terpisah yang disebut "*Witness*". Ini terkadang disebut sebagai "*scriptWitness*" untuk menunjukkan kumpulan yang terdiri dari tanda tangan dan kunci publik. Setiap input SegWit memiliki *scriptWitness* sendiri, dan kumpulan *scriptWitnesses* merupakan bidang *Witness* dari transaksi. Pemindahan data tanda tangan ini adalah inovasi yang diperkenalkan oleh pembaruan SegWit, bertujuan khusus untuk mencegah kemungkinan manipulasi transaksi karena tanda tangan ECDSA.
Alamat P2WPKH menggunakan pengkodean *bech32* dan selalu dimulai dengan `bc1q`. Tipe skrip ini sesuai dengan output SegWit versi 0.

**P2WSH (*Pay-to-Witness-Script-Hash*)**:

Model P2WSH juga diperkenalkan dengan pembaruan SegWit pada Agustus 2017. Mirip dengan model P2SH, ia mengunci bitcoin menggunakan hash dari skrip. Perbedaan utama terletak pada bagaimana tanda tangan dan skrip dimasukkan ke dalam transaksi. Untuk menghabiskan bitcoin yang dikunci dengan tipe skrip ini, penerima harus menyediakan skrip asli, yang disebut *witnessScript* (setara dengan *redeemScript* di P2SH), bersama dengan data yang diperlukan untuk memvalidasi *witnessScript* ini. Mekanisme ini memungkinkan implementasi kondisi pengeluaran yang lebih kompleks, seperti multisig.

Alamat P2WSH menggunakan pengkodean *bech32* dan selalu dimulai dengan `bc1q`. Skrip ini juga sesuai dengan output SegWit versi 0.

**P2TR (*Pay-to-Taproot*)**:

Model P2TR diperkenalkan dengan implementasi Taproot pada November 2021. Ini didasarkan pada protokol Schnorr untuk agregasi kunci kriptografis, serta pada pohon Merkle untuk skrip alternatif, yang disebut MAST (*Merkelized Alternative Script Tree*). Tidak seperti tipe skrip lainnya, di mana kondisi pengeluaran terpapar secara publik (baik saat penerimaan atau pengeluaran), P2TR memungkinkan untuk menyembunyikan skrip kompleks di balik satu kunci publik yang tampak.

Secara teknis, skrip P2TR mengunci bitcoin pada kunci publik Schnorr unik, yang ditandai sebagai $Q$. Kunci $Q$ ini sebenarnya adalah agregat dari kunci publik $P$ dan kunci publik $M$, yang terakhir dihitung dari akar Merkle dari daftar *scriptPubKey*. Bitcoin yang dikunci dengan tipe skrip ini dapat dihabiskan dengan dua cara:
- Dengan menerbitkan tanda tangan untuk kunci publik $P$ (*key path*).
- Dengan memenuhi salah satu skrip yang terkandung dalam pohon Merkle (*script path*).
P2TR menawarkan fleksibilitas yang besar, karena memungkinkan penguncian bitcoin baik dengan kunci publik unik, dengan beberapa skrip pilihan, atau keduanya secara bersamaan. Keuntungan dari struktur pohon Merkle ini adalah hanya skrip pengeluaran yang digunakan yang diungkapkan selama transaksi, tetapi semua skrip alternatif lainnya tetap rahasia.

P2TR sesuai dengan output SegWit versi 1, yang berarti bahwa tanda tangan untuk input P2TR disimpan di bagian *Witness* transaksi, dan tidak di *scriptSig*. Alamat P2TR menggunakan pengkodean *bech32m* dan dimulai dengan `bc1p`, tetapi mereka cukup unik karena tidak menggunakan fungsi hash untuk konstruksinya. Memang, mereka secara langsung mewakili kunci publik $Q$ yang hanya diformat dengan metadata. Oleh karena itu, ini adalah model skrip yang dekat dengan P2PK.

Sekarang setelah kita telah membahas teorinya, mari kita lanjutkan ke praktik! Dalam bab berikut, saya mengusulkan untuk menurunkan baik alamat SegWit v0 maupun alamat SegWit v1 dari sepasang kunci.

## Turunan Alamat
<chapterId>3ebdc750-4135-4881-b07e-08965941b93e</chapterId>

Mari kita jelajahi bersama bagaimana menghasilkan alamat penerima dari sepasang kunci yang terletak, misalnya, pada kedalaman 5 dari dompet HD. Alamat ini kemudian dapat digunakan dalam perangkat lunak dompet untuk mengunci UTXO.

Karena proses penghasilan alamat bergantung pada model skrip yang diadopsi, mari kita fokus pada dua kasus spesifik: menghasilkan alamat SegWit v0 dalam P2WPKH dan alamat SegWit v1 dalam P2TR. Kedua jenis alamat ini mencakup mayoritas penggunaan saat ini.

### Kompresi Kunci Publik

Setelah melakukan semua langkah turunan dari kunci induk ke kedalaman 5 menggunakan indeks yang sesuai, kita memperoleh sepasang kunci ($k$, $K$) dengan $K = k \cdot G$. Meskipun mungkin untuk menggunakan kunci publik ini apa adanya untuk mengunci dana dengan standar P2PK, itu bukan tujuan kita di sini. Sebaliknya, kita bertujuan untuk membuat alamat dalam P2WPKH dalam contoh pertama, dan kemudian dalam P2TR untuk contoh lainnya.

Langkah pertama adalah mengompres kunci publik $K$. Untuk memahami proses ini dengan baik, mari kita ingat kembali beberapa dasar yang dibahas di bagian 3. Kunci publik pada Bitcoin adalah titik $K$ yang terletak pada kurva eliptik. Ini diwakili dalam bentuk $(x, y)$, di mana $x$ dan $y$ adalah koordinat titik. Dalam bentuknya yang tidak dikompres, kunci publik ini berukuran 520 bit: 8 bit untuk awalan (nilai awal `0x04`), 256 bit untuk koordinat $x$, dan 256 bit untuk koordinat $y$. Namun, kurva eliptik memiliki properti simetri terhadap sumbu x: untuk koordinat $x$ yang diberikan, hanya ada dua nilai yang mungkin untuk $y$: $y$ dan $-y$. Kedua titik ini terletak di kedua sisi sumbu x. Dengan kata lain, jika kita tahu $x$, cukup untuk menentukan apakah $y$ genap atau ganjil untuk mengidentifikasi titik yang tepat pada kurva.
Untuk mengompres kunci publik, hanya $x$ yang dikodekan, yang menempati 256 bit, dan sebuah prefiks ditambahkan untuk menentukan paritas dari $y$. Metode ini mengurangi ukuran kunci publik menjadi 264 bit daripada awalnya 520. Prefiks `0x02` menunjukkan bahwa $y$ genap, dan prefiks `0x03` menunjukkan bahwa $y$ ganjil.
Mari kita ambil contoh untuk memahami dengan baik, dengan kunci publik mentah dalam representasi tidak terkompresi:

```text
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Jika kita mendekomposisi kunci ini, kita memiliki:
   - Prefiks: `04`;
   - $x$: `678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6`;
   - $y$: `49f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f`

Karakter heksadesimal terakhir dari $y$ adalah `f`. Dalam basis 10, `f = 15`, yang sesuai dengan angka ganjil. Oleh karena itu, $y$ ganjil, dan prefiks akan `0x03` untuk menunjukkan ini.

Kunci publik terkompresi menjadi:

```text
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```
Operasi ini berlaku untuk semua model skrip berbasis ECDSA, yaitu semua kecuali P2TR yang menggunakan Schnorr. Dalam kasus Schnorr, seperti dijelaskan di bagian 3, kita hanya menyimpan nilai dari $x$, tanpa menambahkan prefiks untuk menunjukkan paritas dari $y$, tidak seperti ECDSA. Ini dimungkinkan oleh fakta bahwa paritas unik secara arbitrer dipilih untuk semua kunci. Ini memungkinkan sedikit pengurangan dalam ruang penyimpanan yang diperlukan untuk kunci publik.
### Turunan dari alamat SegWit v0 (bech32)

Sekarang setelah kita mendapatkan kunci publik terkompresi kita, kita dapat menurunkan alamat penerima SegWit v0 darinya.

Langkah pertama adalah menerapkan fungsi hash HASH160 ke kunci publik terkompresi. HASH160 adalah komposisi dari dua fungsi hash berturut-turut: SHA256, diikuti oleh RIPEMD160:


$$

\text{HASH160}(K) = \text{RIPEMD160}(\text{SHA256}(K))

$$

Pertama, kita lewati kunci melalui SHA256:

```text
SHA256(K) = C489EBD66E4103B3C4B5EAFF462B92F5847CA2DCE0825F4997C7CF57DF35BF3A
```

Kemudian kita lewati hasilnya melalui RIPEMD160:

```text
RIPEMD160(SHA256(K)) = 9F81322CC88622CA4CCB2A52A21E2888727AA535
```
Kami telah memperoleh hash 160-bit dari kunci publik, yang merupakan apa yang disebut sebagai payload dari alamat. Payload ini merupakan bagian pusat dan paling penting dari alamat. Ini juga digunakan dalam *scriptPubKey* untuk mengunci UTXOs. Namun, untuk membuat payload ini lebih mudah digunakan oleh manusia, metadata ditambahkan ke dalamnya. Langkah selanjutnya melibatkan pengkodean hash ini ke dalam kelompok-kelompok 5 bit dalam desimal. Transformasi desimal ini akan berguna untuk konversi ke *bech32*, yang digunakan oleh alamat pasca-SegWit. Hash biner 160-bit ini kemudian dibagi menjadi 32 kelompok dari 5 bit:

$$
\begin{array}{|c|c|}
\hline
\text{5 bits} & \text{Decimal} \\
\hline
10011 & 19 \\
11110 & 30 \\
00000 & 0 \\
10011 & 19 \\
00100 & 4 \\
01011 & 11 \\
00110 & 6 \\
01000 & 8 \\
10000 & 16 \\
11000 & 24 \\
10001 & 17 \\
01100 & 12 \\
10100 & 20 \\
10011 & 19 \\
00110 & 6 \\
01011 & 11 \\
00101 & 5 \\
01001 & 9 \\
01001 & 9 \\
01010 & 10 \\
00100 & 4 \\
00111 & 7 \\
10001 & 17 \\
01000 & 8 \\
10001 & 17 \\
00001 & 1 \\
11001 & 25 \\
00111 & 7 \\
10101 & 21 \\
00101 & 5 \\
00101 & 5 \\
10101 & 21 \\
\hline
\end{array}
$$
Jadi, kita memiliki:

```text
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
```

Setelah hash dikodekan ke dalam kelompok-kelompok 5 bit, checksum ditambahkan ke alamat. Checksum ini digunakan untuk memverifikasi bahwa payload dari alamat tidak telah diubah selama penyimpanan atau transmisi. Misalnya, ini memungkinkan perangkat lunak dompet untuk memastikan bahwa Anda tidak membuat kesalahan ketik saat memasukkan alamat penerima. Tanpa verifikasi ini, Anda bisa secara tidak sengaja mengirim bitcoin ke alamat yang salah, mengakibatkan kehilangan dana secara permanen, karena Anda tidak memiliki kunci publik atau privat yang terkait. Oleh karena itu, checksum adalah perlindungan terhadap kesalahan manusia.

Untuk alamat Bitcoin *Legacy* lama, checksum hanya dihitung dari awal hash alamat dengan fungsi HASH256. Dengan pengenalan SegWit dan format *bech32*, kode BCH (*Bose, Ray-Chaudhuri, dan Hocquenghem*) kini digunakan. Kode-kode koreksi kesalahan ini digunakan untuk mendeteksi dan memperbaiki kesalahan dalam urutan data. Mereka memastikan bahwa informasi yang ditransmisikan tiba utuh di tujuannya, bahkan dalam kasus perubahan minor. Kode BCH digunakan di banyak bidang, seperti SSD, DVD, dan kode QR. Misalnya, berkat kode BCH ini, kode QR yang sebagian terhalang masih dapat dibaca dan didekode.

Dalam konteks Bitcoin, kode BCH menawarkan kompromi yang lebih baik antara ukuran dan kemampuan deteksi kesalahan dibandingkan dengan fungsi hash sederhana yang digunakan untuk alamat *Legacy*. Namun, pada Bitcoin, kode BCH hanya digunakan untuk deteksi kesalahan, bukan koreksi. Dengan demikian, perangkat lunak dompet akan menandai alamat penerima yang salah tetapi tidak akan secara otomatis memperbaikinya. Keterbatasan ini disengaja: memungkinkan koreksi otomatis akan mengurangi kemampuan deteksi kesalahan.

Untuk menghitung checksum dengan kode BCH, kita perlu menyiapkan beberapa elemen:
- **Bagian yang Dapat Dibaca Manusia (HRP - *Human Readable Part*)**: Untuk Bitcoin mainnet, HRP adalah `bc`;
HRP harus diperluas dengan memisahkan setiap karakter menjadi dua bagian:
- Mengambil karakter HRP dalam ASCII:
	- `b`: `01100010`
- `c`: `01100011`
- Mengekstrak 3 bit paling signifikan dan 5 bit paling tidak signifikan:
  - 3 bit paling signifikan: `011` (3 dalam desimal)
  - 3 bit paling signifikan: `011` (3 dalam desimal)
  - 5 bit paling tidak signifikan: `00010` (2 dalam desimal)
  - 5 bit paling tidak signifikan: `00011` (3 dalam desimal)

Dengan pemisah `0` antara dua karakter, ekstensi HRP adalah:

```text
03 03 00 02 03
```

- **Versi saksi (witness version)**: Untuk SegWit versi 0, adalah `00`;

- **Payload**: Nilai desimal dari hash kunci publik;

- **Reservasi untuk checksum**: Kami menambahkan 6 nol `[0, 0, 0, 0, 0, 0]` di akhir urutan.

Semua data yang digabungkan untuk dimasukkan ke dalam program untuk menghitung checksum adalah sebagai berikut:

```text
HRP = 03 03 00 02 03
SEGWIT v0 = 00
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
CHECKSUM = 00 00 00 00 00 00

INPUT = 03 03 00 02 03 00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 00 00 00 00 00 00
```

Perhitungan checksum cukup kompleks. Ini melibatkan aritmetika lapangan polinomial terbatas. Kami tidak akan menjelaskan perhitungan ini di sini dan akan langsung ke hasilnya. Dalam contoh kita, checksum yang diperoleh dalam desimal adalah:

```text
10 16 11 04 13 18
```

Kita sekarang dapat membuat alamat penerima dengan menggabungkan dalam urutan berikut:
- **Versi SegWit**: `00`
- **Payload**: Hash kunci publik
- **Checksum**: Nilai yang diperoleh pada langkah sebelumnya (`10 16 11 04 13 18`)

Ini memberi kita dalam desimal:

```text
00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 10 16 11 04 13 18
```

Kemudian, setiap nilai desimal harus dipetakan ke karakter *bech32* nya menggunakan tabel konversi berikut:


$$
\begin{array}{|c|c|c|c|c|c|c|c|c|}
\hline
 & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
\hline
+0 & q & p & z & r & y & 9 & x & 8 \\
\hline
+8 & g & f & 2 & t & v & d & w & 0 \\
\hline
+16 & s & 3 & j & n & 5 & 4 & k & h \\
\hline
+24 & c & e & 6 & m & u & a & 7 & l \\
\hline
\end{array}
$$

Untuk mengonversi nilai menjadi karakter _bech32_ menggunakan tabel ini, cukup temukan nilai-nilai pada kolom pertama dan baris pertama yang, ketika ditambahkan bersama, menghasilkan hasil yang diinginkan. Kemudian, ambil karakter yang sesuai. Sebagai contoh, angka desimal `19` akan dikonversi menjadi huruf `n`, karena $19 = 16 + 3$.
Dengan memetakan semua nilai kita, kita mendapatkan alamat berikut:

```
qn7qnytxgsc3v5nxt9ff2y83g3pe849942stydj
```

Yang tersisa hanyalah menambahkan HRP `bc`, yang menunjukkan bahwa ini adalah alamat untuk Bitcoin mainnet, serta pemisah `1`, untuk mendapatkan alamat penerima lengkap:

```
bc1qn7qnytxgsc3v5nxt9ff2y83g3pe849942stydj
```

Keunikan dari alfabet _bech32_ ini adalah termasuk semua karakter alfanumerik kecuali `1`, `b`, `i`, dan `o` untuk menghindari kebingungan visual antara karakter yang serupa, terutama selama entri atau pembacaan oleh manusia.

Untuk merangkum, berikut adalah proses derivasinya:

![CYP201](assets/fr/065.webp)

Inilah cara mendapatkan alamat penerima P2WPKH (SegWit v0) dari sepasang kunci. Mari kita lanjutkan ke alamat P2TR (SegWit v1 / Taproot) dan temukan proses generasinya.

### Derivasi Alamat SegWit v1 (bech32m)

Untuk alamat Taproot, proses generasinya sedikit berbeda. Mari kita lihat bersama!

Dari langkah kompresi kunci publik, sebuah perbedaan pertama muncul dibandingkan dengan ECDSA: kunci publik yang digunakan untuk Schnorr di Bitcoin hanya diwakili oleh absisnya ($x$). Oleh karena itu, tidak ada awalan, dan kunci yang dikompresi ukurannya tepat 256 bit.
Seperti yang kita lihat di bab sebelumnya, skrip P2TR mengunci bitcoin pada kunci publik Schnorr yang unik, yang ditunjuk dengan $Q$. Kunci ini $Q$ adalah agregat dari dua kunci publik: $P$, kunci publik internal utama, dan $M$, kunci publik yang berasal dari akar Merkle dari daftar _scriptPubKey_. Bitcoin yang dikunci dengan jenis skrip ini dapat dihabiskan dengan dua cara:

- Dengan mempublikasikan tanda tangan untuk kunci publik $P$ (_jalur kunci_);
- Dengan memenuhi salah satu skrip yang termasuk dalam pohon Merkle (_jalur skrip_).

Pada kenyataannya, kedua kunci ini tidak benar-benar "diagregat." Kunci $P$ sebaliknya di-tweak oleh kunci $M$. Dalam kriptografi, untuk "men-tweak" sebuah kunci publik berarti memodifikasi kunci ini dengan menerapkan nilai aditif yang disebut "tweak." Operasi ini memungkinkan kunci yang dimodifikasi tetap kompatibel dengan kunci privat asli dan tweak. Secara teknis, tweak adalah nilai skalar $t$ yang ditambahkan ke kunci publik awal. Jika $P$ adalah kunci publik asli, kunci yang di-tweak menjadi:

$$
P' = P + tG
$$

Di mana $G$ adalah generator dari kurva eliptik yang digunakan. Operasi ini menghasilkan kunci publik baru yang berasal dari kunci asli, sambil mempertahankan properti kriptografi yang memungkinkan penggunaannya.
Jika Anda tidak perlu menambahkan skrip alternatif (menghabiskan secara eksklusif melalui _jalur kunci_), Anda dapat menghasilkan alamat Taproot yang didirikan hanya berdasarkan kunci publik yang ada pada kedalaman 5 dari dompet Anda. Dalam kasus ini, perlu untuk membuat skrip yang tidak dapat dihabiskan untuk _jalur skrip_, agar memenuhi persyaratan struktur tersebut. Tweak $t$ kemudian dihitung dengan menerapkan fungsi hash bertag, **`TapTweak`**, pada kunci publik internal $P$:

$$
t = \text{H}_{\text{TapTweak}}(P)
$$

di mana:

- **$\text{H}_{\text{TapTweak}}$** adalah fungsi hash SHA256 yang ditandai dengan tag `TapTweak`. Jika Anda tidak familiar dengan apa itu fungsi hash bertag, saya mengundang Anda untuk berkonsultasi pada bab 3.3;
- $P$ adalah kunci publik internal, direpresentasikan dalam format 256-bit terkompresi, menggunakan hanya koordinat $x$.

Kunci publik Taproot $Q$ kemudian dihitung dengan menambahkan tweak $t$, dikalikan dengan generator kurva eliptik $G$, ke kunci publik internal $P$:

$$
Q = P + t \cdot G
$$

Setelah kunci publik Taproot $Q$ diperoleh, kita dapat menghasilkan alamat penerima yang sesuai. Tidak seperti format lain, alamat Taproot tidak didirikan pada hash dari kunci publik. Oleh karena itu, kunci $Q$ dimasukkan langsung ke dalam alamat, secara mentah.

Untuk memulai, kita ekstrak koordinat $x$ dari titik $Q$ untuk mendapatkan kunci publik terkompresi. Pada payload ini, checksum dihitung menggunakan kode BCH, seperti dengan alamat SegWit v0. Namun, program yang digunakan untuk alamat Taproot sedikit berbeda. Memang, setelah pengenalan format _bech32_ dengan SegWit, sebuah bug ditemukan: ketika karakter terakhir dari sebuah alamat adalah `p`, memasukkan atau menghapus `q` tepat sebelum `p` ini tidak membuat checksum menjadi tidak valid. Meskipun bug ini tidak memiliki konsekuensi pada SegWit v0 (berkat batasan ukuran), ini bisa menjadi masalah di masa depan. Bug ini telah diperbaiki untuk alamat Taproot, dan format baru yang diperbaiki disebut "_bech32m_".

Alamat Taproot dihasilkan dengan mengkodekan koordinat $x$ dari $Q$ dalam format _bech32m_, dengan elemen-elemen berikut:

- **HRP (_Human Readable Part_)**: `bc`, untuk menunjukkan jaringan Bitcoin utama;
- **Versi**: `1` untuk menunjukkan Taproot / SegWit v1;
- **Checksum**.

Alamat akhir akan memiliki format:

```
bc1p[Qx][checksum]
```

Di sisi lain, jika Anda ingin menambahkan skrip alternatif selain menghabiskan dengan kunci publik internal (_jalur skrip_), perhitungan alamat penerima akan sedikit berbeda. Anda perlu memasukkan hash dari skrip alternatif dalam perhitungan tweak. Dalam Taproot, setiap skrip alternatif, yang terletak di ujung pohon Merkle, disebut "leaf".

Setelah skrip alternatif yang berbeda ditulis, Anda harus melewatinya secara individu melalui fungsi hash bertag `TapLeaf`, disertai dengan beberapa metadata:

$$
\text{h}_{\text{leaf}} = \text{H}_{\text{TapLeaf}} (v \Vert sz \Vert S)
$$

Dengan:

- $v$: nomor versi skrip (default `0xC0` untuk Taproot);
- $sz$: ukuran skrip yang dikodekan dalam format _CompactSize_; 
- $S$: skripnya.

Berbagai hash skrip ($\text{h}_{\text{leaf}}$) pertama-tama diurutkan dalam urutan leksikografis. Kemudian, mereka digabungkan secara berpasangan dan dilewati melalui fungsi hash bertag `TapBranch`. Proses ini diulang secara iteratif untuk membangun, langkah demi langkah, pohon Merkle:

$$
\text{h}_{\text{branch}} = \text{H}_{\text{TapBranch}}(\text{h}_{\text{leaf1}} \Vert \text{h}_{\text{leaf2}})
$$

Kemudian kita melanjutkan dengan menggabungkan hasilnya dua demi dua, melewatinya pada setiap langkah melalui fungsi hash bertag `TapBranch`, sampai kita mendapatkan akar pohon Merkle:

![CYP201](assets/fr/066.webp)

Setelah akar Merkle $h_{\text{root}}$ dihitung, kita dapat menghitung tweak. Untuk itu, kunci publik internal dompet $P$ digabungkan dengan akar $h_{\text{root}}$, dan hasilnya dimasukkan ke dalam fungsi hash bertanda `TapTweak`:

$$
t = \text{H}_{\text{TapTweak}}(P \Vert h_{\text{root}})
$$

Akhirnya, seperti sebelumnya, kunci publik Taproot $Q$ diperoleh dengan menambahkan kunci publik internal $P$ ke hasil perkalian tweak $t$ dan titik generator $G$:

$$
Q = P + t \cdot G
$$

Kemudian, pembuatan alamat mengikuti proses yang sama, menggunakan kunci publik mentah $Q$ sebagai payload, bersama dengan beberapa metadata tambahan.


Dan itulah! Kita telah mencapai akhir kursus CYP201 ini. Jika Anda merasa kursus ini bermanfaat, saya akan sangat berterima kasih jika Anda bisa meluangkan waktu sejenak untuk memberikannya penilaian yang baik di bab evaluasi berikutnya. Jangan ragu untuk juga membagikannya dengan orang-orang terkasih atau di jejaring sosial Anda. Akhirnya, jika Anda ingin mendapatkan diploma untuk kursus ini, Anda dapat mengikuti ujian akhir tepat setelah bab evaluasi.

# Kesimpulan

<partId>58111408-b734-54db-9ea7-0d5b67f99f99</partId>

## Evaluasi kursus ini

<chapterId>0cd71541-a7fd-53db-b66a-8611b6a28b04</chapterId>
<isCourseReview>true</isCourseReview>

## Ujian Akhir

<chapterId>a53ea27d-0f84-56cd-b37c-a66210a4b31d</chapterId>
<isCourseExam>true</isCourseExam>

## Kesimpulan

<chapterId>d291428b-3cfa-5394-930e-4b514be82d5a</chapterId>

Kita telah mencapai akhir dari pelatihan CYP201. Saya harap ini telah bermanfaat dalam perjalanan pembelajaran Bitcoin Anda dan membantu Anda lebih memahami cara kerja dompet HD yang Anda gunakan sehari-hari. Terima kasih telah mengikuti kursus ini hingga selesai!

Menurut saya, pengetahuan tentang dompet ini sangat fundamental, karena menghubungkan aspek teoritis Bitcoin dengan penggunaan praktisnya. Memang, jika Anda menggunakan Bitcoin, Anda pasti menangani perangkat lunak dompet. Memahami cara kerjanya memungkinkan Anda menerapkan strategi keamanan yang efektif sambil menguasai mekanisme yang mendasarinya, risiko, dan potensi kelemahannya. Dengan demikian, Anda dapat menggunakan Bitcoin dengan lebih aman dan percaya diri.

Jika Anda belum melakukannya, saya mengundang Anda untuk menilai dan mengomentari pelatihan ini. Ini akan sangat membantu saya. Anda juga dapat membagikan pelatihan ini di jejaring sosial Anda untuk menyebarkan pengetahuan ini kepada sebanyak mungkin orang.

Untuk melanjutkan perjalanan Anda lebih dalam, saya sangat merekomendasikan pelatihan **BTC204**, yang juga saya produksi di Plan ₿ Network. Ini didedikasikan untuk privasi Bitcoin dan mengeksplorasi tema-tema kunci: Apa model privasinya? Bagaimana analisis rantai bekerja? Bagaimana menggunakan Bitcoin secara optimal untuk memaksimalkan privasi Anda? Langkah logis berikutnya untuk memperdalam keterampilan Anda!

https://planb.network/courses/btc204

Selain itu, untuk terus memperdalam pengetahuan Anda di alam semesta Bitcoin, kami mengundang Anda untuk mengeksplorasi kursus lain yang tersedia di Plan ₿ Network seperti:

#### Pelajari cara membuat komunitas Bitcoin Anda dengan

https://planb.network/courses/btc302

#### Temukan Lightning Network dengan

https://planb.network/courses/lnp201

#### Temukan pemikiran ekonomi Sekolah Austria dengan

https://planb.network/courses/eco201

#### Temukan sejarah asal-usul Bitcoin dengan

https://planb.network/courses/his201

#### Temukan evolusi kebebasan sepanjang masa dengan

https://planb.network/courses/phi201




