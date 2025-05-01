---
term: Invoice PETIR
---

Permintaan pembayaran kilat yang dibuat oleh penerima, berisi semua informasi yang diperlukan untuk menyelesaikan transaksi.


Lightning Invoice berisi tujuan pembayaran dalam bentuk kunci publik node penerima, tetapi juga awalan `LN`, jumlah, waktu kedaluwarsa, Hash rahasia yang digunakan dalam HTLC, dan metadata lainnya, beberapa di antaranya bersifat opsional, seperti opsi perutean. Faktur ini ditentukan oleh standar BOLT11. Setelah dibayar, Invoice Lightning tidak dapat digunakan kembali.


> ► *Dalam bahasa Prancis, kami dapat menerjemahkan "Invoice" sebagai "facture", tetapi kami umumnya menggunakan istilah bahasa Inggris bahkan dalam bahasa Prancis.*