---
term: SAKSI TRANSAKSI

---
Mengacu pada komponen transaksi Bitcoin yang dipindahkan dengan soft fork SegWit untuk mengatasi masalah kelenturan transaksi. Saksi berisi tanda tangan dan kunci publik yang diperlukan untuk membuka kunci bitcoin yang dibelanjakan dalam sebuah transaksi. Dalam transaksi Legacy, saksi mewakili jumlah `scriptSig` dari semua input. Dalam transaksi SegWit, saksi mewakili jumlah `scriptWitness` untuk setiap input, dan bagian transaksi ini sekarang dipindahkan ke pohon Merkle yang terpisah di dalam blok.

Sebelum SegWit, tanda tangan dapat sedikit diubah tanpa dibatalkan sebelum transaksi dikonfirmasi, yang mengubah pengenal transaksi. Hal ini menyulitkan untuk membangun berbagai protokol, karena transaksi yang belum dikonfirmasi dapat melihat pengenalnya berubah. Dengan memisahkan saksi, SegWit membuat transaksi tidak mudah berubah, karena setiap perubahan pada tanda tangan tidak lagi mempengaruhi pengenal transaksi (TXID), tetapi hanya pengenal saksi (WTXID). Selain memecahkan masalah kelenturan, pemisahan ini memungkinkan peningkatan kapasitas setiap blok.

> ► *Dalam bahasa Inggris, "témoin" diterjemahkan sebagai "saksi".*