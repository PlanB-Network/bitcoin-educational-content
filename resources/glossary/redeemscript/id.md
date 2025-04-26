---
term: TUKAR TUKAR

---
Skrip yang mendefinisikan kondisi spesifik yang harus dipenuhi oleh input untuk membuka dana yang terkait dengan output P2SH. Dalam P2SH UTXO, `scriptPubKey` berisi hash dari `redeemScript`. Ketika sebuah transaksi ingin menggunakan UTXO ini sebagai input, transaksi tersebut harus memberikan `redeemScript` yang jelas yang sesuai dengan hash yang terkandung dalam `scriptPubKey`. Dengan demikian, `redeemScript` diberikan dalam `scriptSig` dari input, bersama dengan elemen-elemen lain yang diperlukan untuk memenuhi ketentuan skrip, seperti tanda tangan atau kunci publik. Struktur yang dienkapsulasi ini memastikan bahwa detail kondisi pembelanjaan tetap tersembunyi sampai bitcoin benar-benar dibelanjakan. Ini terutama digunakan untuk dompet multisignature P2SH lawas.