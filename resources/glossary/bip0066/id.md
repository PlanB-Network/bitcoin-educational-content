---
term: BIP0066

---
BIP ini memperkenalkan standardisasi format tanda tangan dalam transaksi. BIP ini diusulkan sebagai tanggapan terhadap perbedaan dalam cara OpenSSL menangani pengkodean tanda tangan di berbagai sistem. Heterogenitas ini menimbulkan risiko perpecahan _blockchain_. BIP66 menstandarkan format tanda tangan untuk semua transaksi dengan menggunakan pengkodean DER yang ketat (*Distinguished Encoding Rules*). Perubahan ini membutuhkan _soft fork_. Untuk aktivasinya, BIP66 kemudian menggunakan mekanisme yang sama dengan BIP34, yang mengharuskan _field_ `nVersion` ditingkatkan ke versi 3, dan menolak semua blok versi 2 atau yang lebih rendah setelah ambang batas penambang 95% tercapai. Ambang batas ini dilewati pada blok nomor 363.725 pada tanggal 4 Juli 2015.
