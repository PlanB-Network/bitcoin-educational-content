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

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Matematika untuk Implementasi Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Kriptografi Kurva Elips

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Cara Kerja Transaksi Bitcoin

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Penguraian Transaksi Bitcoin dan Tanda Tangan ECDSA

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Naskah dan Validasi Transaksi

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Konstruksi Transaksi dan Pembayaran ke Naskah Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Pekerjaan Dalam Jaringan Bitcoin

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Blok Bitcoin dan Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Komunikasi Jaringan dan Pohon Merkle

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Komunikasi Simpul Tingkat Lanjut dan Saksi Terpisah

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Bagian Akhir


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Ulasan & Peringkat


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>


## Kesimpulan


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
