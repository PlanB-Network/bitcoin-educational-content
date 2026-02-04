---
term: BIP0141

definition: Pengenalan SegWit (Segregated Witness), memisahkan tanda tangan dari sisa transaksi untuk menyelesaikan masalah maleabilitas.
---
Memperkenalkan konsep Segregated Witness (SegWit) yang merupakan dari _soft fork_ terkait. BIP141 memperkenalkan sebuah modifikasi besar pada protokol Bitcoin yang bertujuan untuk memecahkan masalah _transaction malleability_. SegWit memisahkan _witness_ (data tanda tangan) dari data transaksi lainnya. Pemisahan ini dicapai dengan memasukkan _witness_ ke dalam struktur data yang terpisah, yang dilakukan dalam pohon Merkle baru, yang direferensikan di dalam blok melalui transaksi coinbase, membuat SegWit kompatibel dengan protokol versi lama.
