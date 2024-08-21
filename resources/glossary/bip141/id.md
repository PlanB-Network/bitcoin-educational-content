---
term: BIP141
---

Memperkenalkan konsep Segregated Witness (SegWit) yang memberi nama pada soft fork SegWit. BIP141 memperkenalkan modifikasi besar pada protokol Bitcoin yang bertujuan untuk menyelesaikan masalah malleabilitas transaksi. SegWit memisahkan data saksi (data tanda tangan) dari sisanya data transaksi. Pemisahan ini dicapai dengan memasukkan saksi ke dalam struktur data terpisah, yang dikomit dalam Merkle tree baru, yang sendiri dirujuk dalam blok melalui transaksi coinbase, membuat SegWit kompatibel dengan versi lama dari protokol.