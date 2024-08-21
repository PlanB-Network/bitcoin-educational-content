---
term: REDEEMSCRIPT
---

Skrip yang mendefinisikan kondisi spesifik yang harus dipenuhi oleh input untuk membuka dana yang terkait dengan output P2SH. Dalam UTXO P2SH, `scriptPubKey` berisi hash dari `redeemScript`. Ketika sebuah transaksi ingin menghabiskan UTXO ini sebagai input, transaksi tersebut harus menyediakan `redeemScript` yang jelas yang cocok dengan hash yang terkandung dalam `scriptPubKey`. `redeemScript` ini diberikan dalam `scriptSig` dari input, bersama dengan elemen lain yang diperlukan untuk memenuhi kondisi skrip, seperti tanda tangan atau kunci publik. Struktur yang terenkapsulasi ini memastikan bahwa detail dari kondisi pengeluaran tetap tersembunyi sampai bitcoin sebenarnya dihabiskan. Ini terutama digunakan untuk dompet multisignature Legacy P2SH.