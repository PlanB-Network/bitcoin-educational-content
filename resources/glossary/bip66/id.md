---
term: BIP66
---

Memperkenalkan standarisasi format tanda tangan dalam transaksi. BIP ini diajukan sebagai respons terhadap perbedaan cara OpenSSL menangani pengkodean tanda tangan di berbagai sistem. Heterogenitas ini menimbulkan risiko pemisahan blockchain. BIP66 menstandarisasi format tanda tangan untuk semua transaksi menggunakan pengkodean DER yang ketat (*Distinguished Encoding Rules*). Perubahan ini memerlukan soft fork. Untuk aktivasi, BIP66 kemudian menggunakan mekanisme yang sama seperti BIP34, yang mengharuskan bidang `nVersion` ditingkatkan ke versi 3, dan menolak semua blok versi 2 atau lebih rendah setelah ambang batas penambang 95% tercapai. Ambang batas ini terlampaui pada nomor blok 363,725 pada 4 Juli 2015.