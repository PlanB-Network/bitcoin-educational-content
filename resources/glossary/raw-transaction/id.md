---
term: TRANSAKSI MENTAH
---

Transaksi Bitcoin yang telah dibuat dan ditandatangani, ada dalam bentuk binernya. Transaksi mentah (*raw TX*) adalah representasi akhir dari sebuah transaksi, tepat sebelum transaksi tersebut disiarkan di jaringan. Transaksi ini mengandung semua informasi yang diperlukan untuk inklusinya dalam sebuah blok:
* Versi;
* Bendera;
* Input;
* Output;
* Waktu kunci;
* Saksi.

Apa yang disebut sebagai "*transaksi mentah*" merepresentasikan data mentah yang dilewati melalui fungsi hash SHA256 sebanyak dua kali untuk menghasilkan TXID transaksi. Data-data ini kemudian digunakan dalam pohon Merkle blok untuk mengintegrasikan transaksi ke dalam blockchain.

> ► *Konsep ini juga terkadang disebut "Transaksi Terserialisasi". Dalam bahasa Prancis, istilah-istilah ini dapat diterjemahkan sebagai "transaction brute" dan "transaction sérialisée".*