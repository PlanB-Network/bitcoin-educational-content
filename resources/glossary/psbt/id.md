---
term: PSBT

---
Akronim untuk "Transaksi Bitcoin yang Ditandatangani Sebagian". Ini adalah sebuah spesifikasi yang diperkenalkan dengan BIP174 untuk menstandarkan cara di mana transaksi yang belum selesai dibuat dalam perangkat lunak yang terkait dengan Bitcoin, seperti perangkat lunak dompet. PSBT merangkum sebuah transaksi yang inputnya mungkin belum sepenuhnya ditandatangani. PSBT mencakup semua informasi yang diperlukan oleh partisipan untuk menandatangani transaksi tanpa memerlukan data tambahan. Dengan demikian, PSBT dapat memiliki 3 bentuk yang berbeda:


- Transaksi yang sudah selesai, tetapi belum ditandatangani;
- Transaksi yang ditandatangani sebagian, di mana beberapa input ditandatangani sementara yang lain belum;
- Atau transaksi Bitcoin yang sudah ditandatangani, yang dapat dikonversi agar siap disiarkan di jaringan.

Format PSBT memfasilitasi interoperabilitas antara perangkat lunak dompet dan perangkat tanda tangan yang berbeda (dompet perangkat keras). Saat ini, versi 0 dari PSBT digunakan, seperti yang didefinisikan dalam BIP174, tetapi versi 2 sedang diusulkan melalui BIP370.

> ► *Versi 1 PSBT tidak ada. Karena versi 0 adalah versi pertama, maka versi kedua secara informal disebut versi 2. Ava Chow, yang menulis BIP370, dengan demikian memutuskan untuk memberikan nomor 2 pada versi baru ini untuk menghindari kebingungan