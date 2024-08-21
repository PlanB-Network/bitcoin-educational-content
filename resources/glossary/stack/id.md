---
term: STACK
---

Dalam konteks bahasa skrip yang digunakan untuk menerapkan kondisi pengeluaran pada Bitcoin UTXOs, stack adalah struktur data "LIFO" (*Last In, First Out*) yang berfungsi untuk menyimpan elemen sementara selama eksekusi skrip. Setiap operasi dalam skrip memanipulasi stack ini, di mana elemen dapat ditambahkan (*push*) atau dihapus (*pop*). Skrip menggunakan stack untuk mengevaluasi ekspresi, menyimpan variabel sementara, dan mengelola kondisi.

Selama eksekusi skrip Bitcoin, 2 stack dapat digunakan: stack utama dan stack alt (alternatif). Stack utama digunakan untuk sebagian besar operasi skrip. Di stack inilah operasi skrip menambah, menghapus, atau memanipulasi data. Di sisi lain, stack alternatif berfungsi untuk menyimpan data sementara selama eksekusi skrip. Opcodes tertentu, seperti `OP_TOALTSTACK` dan `OP_FROMALTSTACK`, memungkinkan transfer elemen dari stack utama ke stack alternatif dan sebaliknya.

Sebagai contoh, selama validasi transaksi, tanda tangan dan kunci publik didorong ke stack utama dan diproses oleh opcodes berturut-turut untuk memverifikasi bahwa tanda tangan cocok dengan kunci dan data transaksi.

> ► *Dalam bahasa Inggris, terjemahan dari « pile » adalah « stack ». Istilah bahasa Inggris umumnya digunakan bahkan dalam bahasa Prancis selama diskusi teknis.*