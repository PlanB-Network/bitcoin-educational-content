---
term: KEPENULISAN

---
Elemen dalam entri transaksi SegWit yang berisi tanda tangan dan kunci publik yang diperlukan untuk membuka kunci bitcoin yang dikirim dalam transaksi. Mirip dengan `scriptSig` pada transaksi Legacy, `scriptWitness`, bagaimanapun juga, tidak ditempatkan di lokasi yang sama. Memang, bagian inilah, yang disebut sebagai "saksi" (`*witness*` dalam bahasa Inggris), yang dipindahkan ke database terpisah untuk menyelesaikan masalah kelenturan transaksi. Setiap input SegWit memiliki `scriptWitness` sendiri, dan semua elemen `scriptWitness` bersama-sama membentuk bidang `Witness` dari transaksi.

> ► *Hati-hati jangan sampai tertukar antara `scriptWitness` dengan `witnessScript`. Sementara `scriptWitness` berisi data saksi untuk input SegWit apa pun, `witnessScript` mendefinisikan kondisi pengeluaran P2WSH atau P2SH-P2WSH UTXO dan merupakan skrip dengan sendirinya, mirip dengan `redeemScript` untuk output P2SH.*