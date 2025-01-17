---
term: BIP141

---
Memperkenalkan konsep Segregated Witness (SegWit) yang memberi nama pada soft fork SegWit. BIP141 memperkenalkan sebuah modifikasi besar pada protokol Bitcoin yang bertujuan untuk memecahkan masalah kelenturan transaksi. SegWit memisahkan saksi (data tanda tangan) dari data transaksi lainnya. Pemisahan ini dicapai dengan memasukkan saksi ke dalam struktur data yang terpisah, yang dilakukan dalam pohon Merkle baru, yang direferensikan di dalam blok melalui transaksi coinbase, membuat SegWit kompatibel dengan protokol versi lama.