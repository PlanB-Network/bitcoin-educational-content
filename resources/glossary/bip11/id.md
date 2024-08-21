---
istilah: BIP11
---

BIP yang diperkenalkan oleh Gavin Andresen pada Maret 2012 yang mengusulkan metode standar untuk membuat transaksi multisignature di Bitcoin. Usulan ini bertujuan untuk meningkatkan keamanan bitcoin dengan memerlukan beberapa tanda tangan untuk memvalidasi sebuah transaksi. BIP11 memperkenalkan sebuah tipe skrip baru, yang dinamakan "M-of-N multisig," di mana `M` mewakili jumlah minimum tanda tangan yang diperlukan dari antara `N` kunci publik potensial. Standar ini menggunakan opcode `OP_CHECKMULTISIG`, yang sudah ada di Bitcoin, namun sebelumnya tidak sesuai dengan aturan standarisasi dari node-node. Meskipun tipe skrip ini tidak lagi umum digunakan untuk dompet multisig aktual, lebih memilih P2SH atau P2WSH, penggunaannya masih dimungkinkan. Ini secara khusus digunakan dalam meta-protokol seperti Stamps. Node, bagaimanapun, dapat memilih untuk tidak meneruskan transaksi P2MS ini dengan parameter `permitbaremultisig=0`.

> ► *Saat ini, standar ini dikenal sebagai "bare-multisig" atau "P2MS".*