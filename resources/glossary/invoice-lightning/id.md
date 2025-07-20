---
term: INVOICE LIGHTNING
---

Permintaan pembayaran Lightning yang dibuat oleh penerima, berisi semua informasi yang diperlukan untuk menyelesaikan transaksi.


Lightning _Invoice_ berisi tujuan pembayaran dalam bentuk kunci publik node penerima, tetapi juga awalan `LN`, jumlah, waktu kedaluwarsa, _Hash_ rahasia yang digunakan dalam HTLC, dan metadata lainnya, beberapa di antaranya bersifat opsional, seperti opsi perutean. _Invoice_ ini ditentukan oleh standar BOLT11. Setelah dibayar, _Invoice_ Lightning tidak dapat digunakan kembali.


> ► *Dalam bahasa Indonesia, istilah "Invoice" dapat digunakan secara langsung.*
