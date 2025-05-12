---
term: BATERAI
---

Dalam konteks bahasa skrip yang digunakan untuk membubuhkan kondisi pengeluaran pada Bitcoin UTXO, stack adalah struktur data LIFO (*Last In, First Out*) yang digunakan untuk menyimpan Elements sementara selama eksekusi skrip. Setiap operasi dalam skrip memanipulasi tumpukan ini, di mana Elements dapat ditambahkan (*push*) atau dihapus (*pop*). Skrip menggunakan stack untuk mengevaluasi ekspresi, menyimpan variabel sementara, dan mengelola kondisi.


Ketika mengeksekusi skrip Bitcoin, ada dua tumpukan yang dapat digunakan: tumpukan utama dan tumpukan alt (alternatif). Stack utama digunakan untuk sebagian besar operasi skrip. Pada stack inilah operasi skrip menambah, menghapus, atau memanipulasi data. Di sisi lain, stack alternatif digunakan untuk menyimpan data sementara selama eksekusi skrip. Opcode tertentu, seperti `OP_TOALTSTACK` dan `OP_FROMALTSTACK`, memungkinkan Anda untuk mentransfer Elements dari tumpukan utama ke tumpukan alternatif dan sebaliknya.


Sebagai contoh, ketika sebuah transaksi divalidasi, tanda tangan dan kunci publik didorong ke tumpukan utama dan diproses oleh opcode yang berurutan untuk memverifikasi bahwa tanda tangan tersebut cocok dengan kunci dan data transaksi.