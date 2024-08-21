---
term: SCRIPTWITNESS
---

Sebuah elemen dalam entri transaksi SegWit yang berisi tanda tangan dan kunci publik yang diperlukan untuk membuka bitcoin yang dikirim dalam transaksi. Mirip dengan `scriptSig` dari transaksi Legacy, `scriptWitness` ini, bagaimanapun, tidak ditempatkan di lokasi yang sama. Memang, bagian ini, yang disebut sebagai "saksi" (`*witness*` dalam bahasa Inggris), dipindahkan ke database terpisah untuk menyelesaikan masalah malleabilitas transaksi. Setiap input SegWit memiliki `scriptWitness`nya sendiri, dan semua elemen `scriptWitness` bersama-sama membentuk bidang `Witness` dari transaksi.

> ► *Berhati-hatilah untuk tidak mengacaukan `scriptWitness` dengan `witnessScript`. Sementara `scriptWitness` berisi data saksi untuk setiap input SegWit, `witnessScript` mendefinisikan kondisi pengeluaran dari sebuah UTXO P2WSH atau P2SH-P2WSH dan merupakan skrip tersendiri, mirip dengan `redeemScript` untuk output P2SH.*