---
term: BIP118

---
Proposal untuk meningkatkan Bitcoin yang bertujuan untuk memperkenalkan dua pengubah SigHash Flag baru: `SIGHASH_ANYPREVOUT` dan `SIGHASH_ANYPREVOUTANYSCRIPT`. Fitur-fitur ini memperluas kemampuan transaksi Bitcoin, terutama dalam hal kontrak pintar dan solusi overlay seperti Lightning Network. BIP118 akan memungkinkan penggunaan Eltoo. Keuntungan utama dari `SIGHASH_ANYPREVOUT` adalah memungkinkan penggunaan ulang tanda tangan di berbagai transaksi, yang menawarkan fleksibilitas yang lebih tinggi. Secara khusus, SigHash ini mengijinkan tanda tangan yang tidak mencakup semua input transaksi.