---
term: WITNESS SCRIPT

---
Skrip yang menentukan kondisi di mana bitcoin dapat dibelanjakan dari P2WSH atau P2SH-P2WSH UTXO. Biasanya, `witnessScript` menentukan kondisi dompet _multisignature_ di bawah standar SegWit. Dalam standar skrip ini, `scriptPubKey` dari UTXO (output) berisi _hash_ dari `witnessScript`. Untuk menggunakan UTXO ini sebagai input dalam transaksi baru, pemegang harus mengungkapkan `witnessScript` yang asli, untuk membuktikan kecocokannya dengan sidik jari dalam `scriptPubKey`. `witnessScript` kemudian harus disertakan dalam `scriptWitness` transaksi, yang juga berisi elemen-elemen yang diperlukan untuk memvalidasi skrip, seperti tanda tangan. Oleh karena itu, `witnessScript` setara dengan SegWit dari `redeemScript` dalam transaksi P2SH, dengan perbedaan bahwa ia ditempatkan di _witness_ transaksi, dan bukan di `scriptSig`.

> ► *Catatan: `witnessScript` tidak sama dengan `scriptWitness`. Sementara `witnessScript` mendefinisikan kondisi pengeluaran P2WSH atau P2SH-P2WSH UTXO dan merupakan skrip dengan sendirinya, `scriptWitness` berisi data _witness_ dari input SegWit apa pun.*
