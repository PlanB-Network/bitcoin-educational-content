---
term: VIN
---

Elemen spesifik dari transaksi Bitcoin yang menentukan sumber dana yang digunakan untuk memenuhi output. Setiap `vin` merujuk pada output yang belum terpakai (UTXO) dari transaksi sebelumnya. Sebuah transaksi dapat mengandung beberapa input, masing-masing diidentifikasi oleh kombinasi `txid` (pengenal dari transaksi asli) dan `vout` (indeks dari output dalam transaksi tersebut).

Setiap `vin` mencakup informasi berikut:
* `txid`: pengenal dari transaksi sebelumnya yang mengandung output yang digunakan di sini sebagai input;
* `vout`: indeks dari output dalam transaksi sebelumnya;
* `scriptSig` atau `scriptWitness`: sebuah skrip pembuka yang menyediakan data yang diperlukan untuk memenuhi kondisi yang diajukan oleh `scriptPubKey` dari transaksi sebelumnya yang dananya sedang digunakan, biasanya dengan menyediakan tanda tangan kriptografis;
* `nSequence`: sebuah bidang spesifik yang digunakan untuk menunjukkan bagaimana input ini dikunci waktu, serta opsi lain seperti RBF.