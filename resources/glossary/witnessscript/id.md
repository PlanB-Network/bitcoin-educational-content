---
term: WITNESSSCRIPT
---

Skrip yang menentukan kondisi di mana bitcoin dapat dihabiskan dari UTXO P2WSH atau P2SH-P2WSH. Biasanya, `witnessScript` menentukan kondisi dari dompet multisignature di bawah standar SegWit. Dalam standar skrip ini, `scriptPubKey` dari UTXO (output) mengandung hash dari `witnessScript`. Untuk menggunakan UTXO ini sebagai input dalam transaksi baru, pemegang harus mengungkapkan `witnessScript` asli, untuk membuktikan kecocokannya dengan sidik jari dalam `scriptPubKey`. `witnessScript` kemudian harus dimasukkan dalam `scriptWitness` transaksi, yang juga mengandung elemen-elemen yang diperlukan untuk memvalidasi skrip, seperti tanda tangan. Oleh karena itu, `witnessScript` adalah setara untuk SegWit dari `redeemScript` dalam transaksi P2SH, dengan perbedaan bahwa itu ditempatkan dalam saksi transaksi, dan bukan dalam `scriptSig`.

> ► *Hati-hati, `witnessScript` tidak boleh dikacaukan dengan `scriptWitness`. Sementara `witnessScript` mendefinisikan kondisi pengeluaran dari UTXO P2WSH atau P2SH-P2WSH dan merupakan skrip tersendiri, `scriptWitness` mengandung data saksi dari setiap input SegWit.*