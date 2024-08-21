---
term: TRANSAKSI (TX)
---

Dalam konteks Bitcoin, sebuah transaksi (disingkat sebagai "TX") adalah operasi yang dicatat di blockchain yang mentransfer kepemilikan bitcoin dari satu atau lebih input ke satu atau lebih output. Setiap transaksi menggunakan Output Transaksi yang Belum Terpakai (UTXOs) sebagai input, yang merupakan output dari transaksi sebelumnya, dan menciptakan UTXOs baru sebagai output, yang dapat digunakan sebagai input dalam transaksi masa depan.

Setiap input mencakup referensi ke output yang ada bersama dengan skrip tanda tangan (`scriptSig`) yang memenuhi kondisi pengeluaran (`scriptPubKey`) yang ditetapkan oleh output yang dirujuk. Inilah yang memungkinkan bitcoin dapat dibuka. Output mendefinisikan kondisi pengeluaran baru (`scriptPubKey`) untuk bitcoin yang ditransfer, seringkali dalam bentuk kunci publik atau alamat tempat bitcoin sekarang dikaitkan.