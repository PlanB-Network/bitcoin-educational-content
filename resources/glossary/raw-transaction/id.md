---
term: TRANSAKSI MENTAH

---
Transaksi Bitcoin yang dibuat dan ditandatangani, ada dalam bentuk biner. Transaksi mentah (*raw TX*) adalah representasi akhir dari sebuah transaksi, sebelum disiarkan di jaringan. Transaksi ini berisi semua informasi yang diperlukan untuk dimasukkan ke dalam blok:


- Versi;
- _Flag_;
- Input;
- Output;
- _Timelock_;
- _Witness_.

Apa yang disebut sebagai "*transaksi mentah*" mewakili data mentah yang dilewatkan melalui fungsi _hash_ SHA256 dua kali untuk menghasilkan TXID transaksi. Data ini kemudian digunakan dalam pohon Merkle blok untuk mengintegrasikan transaksi ke dalam _blockchain_.

> ► *Konsep ini juga terkadang disebut "Transaksi Terserialisasi (Serialized Transaction)"*
