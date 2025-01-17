---
term: TRANSAKSI MENTAH

---
Transaksi Bitcoin yang dibuat dan ditandatangani, ada dalam bentuk biner. Transaksi mentah (*raw TX*) adalah representasi akhir dari sebuah transaksi, sebelum disiarkan di jaringan. Transaksi ini berisi semua informasi yang diperlukan untuk dimasukkan ke dalam blok:


- Versi;
- Bendera;
- Masukan;
- Keluarannya;
- Waktu penguncian;
- Saksi.

Apa yang disebut sebagai "*transaksi mentah*" mewakili data mentah yang dilewatkan melalui fungsi hash SHA256 dua kali untuk menghasilkan TXID transaksi. Data ini kemudian digunakan dalam pohon Merkle blok untuk mengintegrasikan transaksi ke dalam blockchain.

> ► *Konsep ini juga terkadang disebut "Transaksi Berseri". Dalam bahasa Prancis, istilah-istilah ini masing-masing dapat diterjemahkan sebagai "transaction brute" dan "transaction sérialisée".*