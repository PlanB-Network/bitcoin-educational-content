---
term: TUMPUKAN

---
Dalam konteks bahasa skrip yang digunakan untuk menerapkan ketentuan pengeluaran pada Bitcoin UTXO, tumpukan adalah struktur data "LIFO" (*Last In, First Out*) yang berfungsi untuk menyimpan elemen sementara selama eksekusi skrip. Setiap operasi dalam skrip memanipulasi tumpukan ini, di mana elemen dapat ditambahkan (*push*) atau dihapus (*pop*). Skrip menggunakan tumpukan untuk mengevaluasi ekspresi, menyimpan variabel sementara, dan mengelola kondisi.

Selama eksekusi skrip Bitcoin, ada dua tumpukan yang dapat digunakan: tumpukan utama dan tumpukan alt (alternatif). Tumpukan utama digunakan untuk sebagian besar operasi skrip. Pada tumpukan inilah operasi skrip menambah, menghapus, atau memanipulasi data. Stack alternatif, di sisi lain, berfungsi untuk menyimpan data sementara selama eksekusi skrip. Opcode tertentu, seperti `OP_TOALTSTACK` dan `OP_FROMALTSTACK`, memungkinkan transfer elemen dari tumpukan utama ke tumpukan alternatif dan sebaliknya.

Sebagai contoh, selama validasi transaksi, tanda tangan dan public key didorong ke dalam tumpukan utama dan diproses oleh opcode yang berurutan untuk memverifikasi bahwa tanda tangan tersebut cocok dengan key dan data transaksi.

> ► *Dalam bahasa Inggris, terjemahan "pile" adalah "tumpukan". Istilah bahasa Inggris umumnya digunakan bahkan dalam bahasa Prancis selama diskusi teknis.*