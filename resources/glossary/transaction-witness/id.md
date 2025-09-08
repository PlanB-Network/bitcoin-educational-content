---
term: TRANSACTION WITNESS

---
Mengacu pada komponen transaksi Bitcoin yang dipindahkan dengan _soft fork_ SegWit untuk mengatasi masalah maleabilitas transaksi. _Witness_ berisi tanda tangan dan kunci publik yang diperlukan untuk membuka kunci bitcoin yang dibelanjakan dalam sebuah transaksi. Dalam transaksi Legacy, _witness_ mewakili jumlah `scriptSig` dari semua input. Dalam transaksi SegWit, _witness_ mewakili jumlah `scriptWitness` untuk setiap input, dan bagian transaksi ini sekarang dipindahkan ke pohon Merkle yang terpisah di dalam blok.

Sebelum SegWit, tanda tangan dapat sedikit diubah tanpa dibatalkan sebelum transaksi dikonfirmasi, yang mengubah pengenal transaksi. Hal ini menyulitkan untuk membangun berbagai protokol, karena transaksi yang belum dikonfirmasi dapat melihat pengenalnya berubah. Dengan memisahkan _witness_, SegWit membuat transaksi tidak mudah berubah, karena setiap perubahan pada tanda tangan tidak lagi mempengaruhi pengenal transaksi (TXID), tetapi hanya pengenal _witness_ (WTXID). Selain memecahkan masalah maleabilitas, pemisahan ini memungkinkan peningkatan kapasitas setiap blok.
