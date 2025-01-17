---
term: SAKSI-SAKSI

---
Skrip yang menentukan kondisi di mana bitcoin dapat dibelanjakan dari P2WSH atau P2SH-P2WSH UTXO. Biasanya, `witnessScript` menentukan kondisi dompet multisignature di bawah standar SegWit. Dalam standar skrip ini, `scriptPubKey` dari UTXO (output) berisi hash dari `witnessScript`. Untuk menggunakan UTXO ini sebagai input dalam transaksi baru, pemegang harus mengungkapkan `witnessScript` yang asli, untuk membuktikan kecocokannya dengan sidik jari dalam `scriptPubKey`. `witnessScript` kemudian harus disertakan dalam `scriptWitness` transaksi, yang juga berisi elemen-elemen yang diperlukan untuk memvalidasi skrip, seperti tanda tangan. Oleh karena itu, `witnessScript` adalah setara dengan SegWit dari `redeemScript` dalam transaksi P2SH, dengan perbedaan bahwa ia ditempatkan di saksi transaksi, dan bukan di `scriptSig`.

> ► *Perhatian, `witnessScript` tidak boleh disamakan dengan `scriptWitness`. Sementara `witnessScript` mendefinisikan kondisi pengeluaran P2WSH atau P2SH-P2WSH UTXO dan merupakan skrip dengan sendirinya, `scriptWitness` berisi data saksi dari input SegWit apa pun