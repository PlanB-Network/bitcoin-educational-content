---
term: TRANSAKSI (TX)

---
Dalam konteks Bitcoin, sebuah transaksi (disingkat "TX") adalah sebuah operasi yang dicatat di blockchain yang mentransfer kepemilikan bitcoin dari satu atau lebih input ke satu atau lebih output. Setiap transaksi menggunakan Unspent Transaction Outputs (UTXO) sebagai input, yang merupakan output dari transaksi sebelumnya, dan menciptakan UTXO baru sebagai output, yang dapat digunakan sebagai input dalam transaksi di masa depan.

Setiap input menyertakan referensi ke output yang sudah ada bersama dengan skrip tanda tangan (`scriptSig`) yang memenuhi kondisi pengeluaran (`scriptPubKey`) yang dibuat oleh output yang direferensikan. Inilah yang memungkinkan bitcoin untuk dibuka. Output mendefinisikan kondisi pengeluaran baru (`scriptPubKey`) untuk bitcoin yang ditransfer, sering kali dalam bentuk kunci publik atau alamat yang sekarang dikaitkan dengan bitcoin.