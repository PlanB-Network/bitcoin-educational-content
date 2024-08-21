---
term: BIP118
---

Proposal untuk meningkatkan Bitcoin yang bertujuan memperkenalkan dua modifikasi baru pada SigHash Flag: `SIGHASH_ANYPREVOUT` dan `SIGHASH_ANYPREVOUTANYSCRIPT`. Fitur-fitur ini memperluas kemampuan transaksi Bitcoin, khususnya dalam hal kontrak pintar dan solusi overlay seperti Lightning Network. BIP118 akan memungkinkan penggunaan Eltoo. Keuntungan utama dari `SIGHASH_ANYPREVOUT` adalah memungkinkan penggunaan kembali tanda tangan di berbagai transaksi, yang menawarkan lebih banyak fleksibilitas. Secara spesifik, SigHash ini memungkinkan tanda tangan yang tidak mencakup input transaksi apapun.