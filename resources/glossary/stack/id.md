---
term: STACK
---

Dalam konteks bahasa skrip yang digunakan untuk membubuhkan kondisi pengeluaran pada Bitcoin UTXO, _stack_ adalah struktur data LIFO (*Last In, First Out*) yang digunakan untuk menyimpan elemen sementara selama eksekusi skrip. Setiap operasi dalam skrip memanipulasi tumpukan ini, di mana elemen dapat ditambahkan (*push*) atau dihapus (*pop*). Skrip menggunakan _stack_ untuk mengevaluasi ekspresi, menyimpan variabel sementara, dan mengelola kondisi.


Ketika mengeksekusi skrip Bitcoin, ada dua _stack_ yang dapat digunakan: _stack_ utama dan _stack_ alternatif. _Stack_ utama digunakan untuk sebagian besar operasi skrip. Pada _stack_ inilah operasi skrip menambah, menghapus, atau memanipulasi data dilakukan. Di sisi lain, _stack_ alternatif digunakan untuk menyimpan data sementara selama eksekusi skrip. Opcode tertentu, seperti `OP_TOALTSTACK` dan `OP_FROMALTSTACK`, memungkinkan Anda untuk mentransfer elemen dari _stack_ utama ke _stack_ alternatif dan sebaliknya.


Sebagai contoh, ketika sebuah transaksi divalidasi, tanda tangan dan kunci publik didorong ke _stack_ utama dan diproses oleh opcode yang berurutan untuk memverifikasi bahwa tanda tangan tersebut cocok dengan kunci dan data transaksi.
