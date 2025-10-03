---
term: BIP0118

---
Proposal untuk meningkatkan Bitcoin yang bertujuan untuk memperkenalkan dua pengubah _SigHash Flag_ baru: `SIGHASH_ANYPREVOUT` dan `SIGHASH_ANYPREVOUTANYSCRIPT`. Fitur-fitur ini memperluas kemampuan transaksi Bitcoin, terutama dalam hal kontrak pintar dan solusi _overlay_ seperti Jaringan Lightning. BIP118 memungkinkan penggunaan Eltoo. Keuntungan utama dari `SIGHASH_ANYPREVOUT` adalah memungkinkan penggunaan ulang tanda tangan di berbagai transaksi, yang menawarkan fleksibilitas yang lebih tinggi. Secara khusus, SigHash ini mengijinkan penggunaan tanda tangan yang tidak mencakup semua input transaksi.
