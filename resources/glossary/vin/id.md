---
term: VIN

---
Elemen spesifik dari transaksi Bitcoin yang menentukan sumber dana yang digunakan untuk memenuhi output. Setiap `vin` merujuk pada output yang belum digunakan (UTXO) dari transaksi sebelumnya. Sebuah transaksi dapat berisi beberapa input, masing-masing diidentifikasi dengan kombinasi `txid` (pengenal transaksi asli) dan `vout` (indeks output dalam transaksi tersebut).

Setiap `vin` mencakup informasi berikut:


- `txid`: pengenal dari transaksi sebelumnya yang berisi output yang digunakan di sini sebagai input;
- `vout`: indeks dari output pada transaksi sebelumnya;
- `scriptSig` atau `scriptWitness`: skrip pembuka kunci yang menyediakan data yang diperlukan untuk memenuhi persyaratan yang diberikan oleh `scriptPubKey` dari transaksi sebelumnya yang dananya digunakan, biasanya dengan memberikan tanda tangan kriptografi;
- `nSequence`: bidang khusus yang digunakan untuk menunjukkan bagaimana input ini dikunci waktu, serta opsi lain seperti RBF.