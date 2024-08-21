---
term: MALLEABILITY (TRANSAKSI)
---

Merujuk pada kemampuan untuk sedikit memodifikasi struktur transaksi Bitcoin, tanpa mengubah efeknya, namun sambil mengubah pengenal transaksi (*TXID*). Sifat ini dapat dimanfaatkan secara jahat untuk menyesatkan pemangku kepentingan tentang status transaksi, sehingga menyebabkan masalah seperti pengeluaran ganda. Malleability dimungkinkan oleh fleksibilitas tanda tangan digital yang digunakan. Soft fork SegWit secara khusus diperkenalkan untuk mencegah malleability transaksi Bitcoin ini, membuat implementasi Lightning Network menjadi rumit. Ini dicapai dengan menghilangkan data yang dapat dimodifikasi dari perhitungan TXID transaksi.

> ► *Meskipun jarang, istilah "mutability" terkadang digunakan untuk merujuk pada konsep yang sama.*