---
name: Pemrograman Bitcoin
goal: Membangun pustaka Bitcoin yang lengkap dari awal dan memahami dasar-dasar kriptografi Bitcoin
objectives: 

 - Menerapkan operasi aritmatika bidang terbatas dan kurva elips dalam Python
 - Membangun dan mengurai transaksi Bitcoin secara terprogram
 - Membuat alamat Testnet dan menyiarkan transaksi melalui jaringan
 - Menguasai dasar-dasar matematika yang mendasari model keamanan Bitcoin

---
# Perjalanan ke skrip dan program Bitcoin


Kursus intensif dua hari ini, yang diajarkan oleh Jimmy Song, akan membawa Anda jauh ke dalam dasar-dasar teknis Bitcoin dengan membangun perpustakaan Bitcoin yang lengkap dari bawah ke atas. Dimulai dengan matematika esensial dari bidang terbatas dan kurva elips, Anda akan berkembang melalui penguraian transaksi, eksekusi skrip, dan komunikasi jaringan. Melalui latihan pengkodean langsung di buku catatan Jupyter, Anda akan membuat Testnet Address Anda sendiri, membuat transaksi secara manual, dan menyiarkannya langsung ke jaringan - semuanya sambil mendapatkan pemahaman mendalam tentang prinsip-prinsip kriptografi yang membuat Bitcoin aman dan Trustless.


Nikmati penemuan Anda!


+++

# Pendahuluan

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## Ikhtisar Kursus

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

Selamat datang di kursus PRO 202 _**Programming Bitcoin**_, perjalanan intensif yang membawa Anda dari aritmetika lapangan hingga membangun dan menyiarkan transaksi nyata di Testnet Bitcoin.

Dalam kursus ini, Anda akan secara bertahap membangun pustaka Bitcoin di Python sambil memperoleh dasar-dasar kriptografi, protokol, dan perangkat lunak yang diperlukan untuk memahami dengan tepat keamanan dan cara kerja internal Bitcoin. Pendekatan PRO 202 sepenuhnya praktis: setiap konsep langsung diterapkan di notebook Jupyter, memastikan teori dan kode saling memperkuat.

### Konsep Matematika Penting untuk Bitcoin

Bagian pertama ini menetapkan landasan matematika yang tak tergantikan. Anda akan mengimplementasikan aritmetika bidang hingga dan operasi kurva elips (hukum grup, penjumlahan, penggandaan, perkalian skalar...) — prasyarat untuk ECDSA. Tujuannya dua: memahami struktur aljabar yang membuat tanda tangan kriptografis mungkin dan membangun alat Python yang andal untuk memanipulasinya.

Kemudian Anda akan memformalkan komponen ECDSA: pembuatan kunci, pemformatan titik, hashing, pembuatan tanda tangan, dan verifikasi. Bagian ini secara langsung menghubungkan teori dengan praktik, menekankan detail implementasi dan ketangguhan model keamanan yang mendasarinya.

### Mekanisme Internal Transaksi Bitcoin

Di bagian kedua, Anda akan membedah struktur dari sebuah transaksi Bitcoin: UTXO, input/output, urutan, skrip, pengkodean, dan lainnya. Anda akan menulis kode untuk membangun, menandatangani, dan memverifikasi transaksi, sehingga memperoleh pemahaman yang tepat tentang apa yang dikomit oleh hash dan alasannya.

Selanjutnya, Anda akan mengimplementasikan eksekutor _Script_ minimal, meninjau opcode utama, dan memvalidasi jalur pengeluaran. Tujuannya adalah agar Anda mampu mengaudit perilaku transaksi, mendiagnosis kegagalan validasi, dan menilai keamanan kebijakan pengeluaran.

### Mekanisme Internal Jaringan Bitcoin

Pada bagian ketiga, Anda akan menempatkan transaksi dalam sistem yang lebih luas: struktur blok, header, tingkat kesulitan, dan mekanisme Proof-of-Work. Anda akan menangani pesan protokol, header blok, dan pohon Merkle.

Akhirnya, Anda akan mempelajari komunikasi node peer-to-peer, optimalisasi pesan, dan pengenalan SegWit.

Seperti setiap kursus di Plan ₿ Academy, bagian terakhir mencakup evaluasi yang dirancang untuk memperkuat pemahaman Anda. Siap untuk mengungkap cara kerja internal Bitcoin dan menulis kode yang menggerakkannya? Mari kita mulai!

# Konsep Matematika Esensial untuk Bitcoin

<partId>e545b7a7-b596-436e-86e9-d0ddceb72543</partId>


## Matematika untuk Implementasi Bitcoin

<chapterId>790e5214-836b-40fe-bbd6-f4ccc920b778</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Kriptografi Kurva Elips

<chapterId>7d3d842e-ae88-472e-85ff-196d60655815</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Cara Kerja Transaksi Bitcoin

<partId>774c0e80-d316-414a-bd59-0bbd185d3b58</partId>


## Penguraian Transaksi Bitcoin dan Tanda Tangan ECDSA

<chapterId>ae86fc27-2f27-4de9-b17c-351c00690144</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Naskah dan Validasi Transaksi

<chapterId>8f0d4381-2b36-4c66-8bee-1100b2dfd8ed</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Konstruksi Transaksi dan Pembayaran ke Naskah Hash


<chapterId>1a6ca3fa-a71f-4b7e-9337-7c84a0b3f928</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Pekerjaan Dalam Jaringan Bitcoin

<partId>6af9d722-07da-487b-bf08-1b30bc3db3d4</partId>


## Blok Bitcoin dan Proof of Work

<chapterId>28a0f5d3-af1b-4093-be49-e3112e1d48a4</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Komunikasi Jaringan dan Pohon Merkle

<chapterId>dd8e23bc-ddd6-45a6-8d3a-16bc86ba49ac</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Komunikasi Simpul Tingkat Lanjut dan Saksi Terpisah

<chapterId>8d70c283-4609-46a8-ad24-83b04a68529a</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Bagian Akhir


<partId>f338e5f4-216e-4b38-bf56-8333e674c04c</partId>


## Ulasan & Peringkat


<chapterId>e149d14b-e99f-428a-a775-ed50cd0a6e9b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Kesimpulan


<chapterId>247bcefb-b158-42a3-82f4-c58bcad4a47a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
