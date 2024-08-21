---
term: TRANSACTION WITNESS
---

Merujuk pada komponen dari transaksi Bitcoin yang dipindahkan dengan soft fork SegWit untuk mengatasi masalah malleability transaksi. Witness berisi tanda tangan dan kunci publik yang diperlukan untuk membuka bitcoin yang digunakan dalam sebuah transaksi. Dalam transaksi Legacy, witness mewakili jumlah `scriptSig` dari semua input. Dalam transaksi SegWit, witness mewakili jumlah `scriptWitness` untuk setiap input, dan bagian ini dari transaksi sekarang dipindahkan ke dalam sebuah Merkle tree terpisah dalam blok.

Sebelum SegWit, tanda tangan bisa sedikit diubah tanpa menjadi tidak valid sebelum transaksi dikonfirmasi, yang mengubah pengidentifikasi transaksi. Ini membuatnya sulit untuk membangun berbagai protokol, karena transaksi yang belum dikonfirmasi bisa melihat pengidentifikasinya berubah. Dengan memisahkan witness, SegWit membuat transaksi tidak dapat dimanipulasi, karena perubahan apa pun pada tanda tangan tidak lagi mempengaruhi pengidentifikasi transaksi (TXID), tetapi hanya pengidentifikasi witness (WTXID). Selain menyelesaikan masalah malleability, pemisahan ini memungkinkan peningkatan kapasitas setiap blok.

> ► *Dalam bahasa Inggris, "témoin" diterjemahkan sebagai "witness".*