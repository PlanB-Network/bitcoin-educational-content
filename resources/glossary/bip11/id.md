---
term: BIP11

---
BIP diperkenalkan oleh Gavin Andresen pada bulan Maret 2012 yang mengusulkan sebuah metode standar untuk membuat transaksi multisignature pada Bitcoin. Proposal ini bertujuan untuk meningkatkan keamanan bitcoin dengan membutuhkan beberapa tanda tangan untuk memvalidasi sebuah transaksi. BIP11 memperkenalkan sebuah jenis skrip baru, yang dinamakan "M-of-N multisig", dimana `M` mewakili jumlah minimum tanda tangan yang dibutuhkan dari antara `N` kunci publik potensial. Standar ini menggunakan opcode `OP_CHECKMULTISIG`, yang sudah ada di Bitcoin, tetapi sebelumnya tidak sesuai dengan aturan standardisasi node. Walaupun jenis skrip ini tidak lagi digunakan secara umum untuk dompet multisig yang sebenarnya, dan lebih memilih P2SH atau P2WSH, penggunaannya masih memungkinkan. Skrip ini terutama digunakan dalam meta-protokol seperti Stamps. Akan tetapi, node dapat memilih untuk tidak merelay transaksi P2MS ini dengan parameter `permitbaremultisig=0`.

> ► *Saat ini, standar ini dikenal sebagai "bare-multisig" atau "P2MS".*