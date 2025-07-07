---
term: MALLEABILITY (TRANSAKSI)

---
Mengacu pada kemampuan untuk mengubah struktur transaksi Bitcoin, tanpa mengubah efeknya, namun dengan mengubah pengenal transaksi (*TXID*). Sifat ini dapat dieksploitasi secara jahat untuk menyesatkan para pemangku kepentingan mengenai status transaksi, sehingga menyebabkan masalah seperti pembelanjaan ganda. _Malleability_ dimungkinkan oleh fleksibilitas tanda tangan digital yang digunakan. _Soft fork_ SegWit diperkenalkan untuk mencegah kelenturan transaksi Bitcoin ini, membuat implementasi Jaringan Lightning menjadi rumit. Hal ini dapat dicapai dengan menghapus data yang dapat diubah dari transaksi dari perhitungan TXID.

> ► *Meskipun jarang, istilah "mutability" terkadang digunakan untuk merujuk pada konsep yang sama.*
