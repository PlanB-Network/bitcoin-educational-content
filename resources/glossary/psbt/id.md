---
term: PSBT
---

Akronim untuk "Partially Signed Bitcoin Transaction" (Transaksi Bitcoin yang Ditandatangani Sebagian). Ini adalah spesifikasi yang diperkenalkan dengan BIP174 untuk menstandarkan cara di mana transaksi yang belum selesai dibangun dalam perangkat lunak terkait dengan Bitcoin, seperti perangkat lunak dompet. Sebuah PSBT mengemas transaksi di mana input mungkin belum sepenuhnya ditandatangani. Ini mencakup semua informasi yang diperlukan bagi peserta untuk menandatangani transaksi tanpa memerlukan data tambahan. Dengan demikian, PSBT dapat mengambil 3 bentuk berbeda:
* Transaksi yang sepenuhnya dibangun, tetapi belum ditandatangani;
* Transaksi yang ditandatangani sebagian, di mana beberapa input ditandatangani sementara yang lain belum;
* Atau transaksi Bitcoin yang sepenuhnya ditandatangani, yang dapat dikonversi untuk siap disiarkan di jaringan.

Format PSBT memfasilitasi interoperabilitas antara perangkat lunak dompet yang berbeda dan perangkat tanda tangan (hardware wallet). Saat ini, versi 0 dari PSBT digunakan, seperti yang didefinisikan dalam BIP174, tetapi versi 2 sedang diusulkan melalui BIP370.

> ► *Versi 1 dari PSBT tidak ada. Karena versi 0 adalah versi pertama, versi kedua secara informal disebut versi 2. Ava Chow, yang mengarang BIP370, dengan demikian memutuskan untuk menetapkan nomor 2 untuk versi baru ini untuk menghindari kebingungan.*