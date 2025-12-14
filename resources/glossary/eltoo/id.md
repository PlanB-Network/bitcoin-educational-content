---
term: ELTOO

---
Protokol umum untuk lapisan kedua Bitcoin yang mendefinisikan cara mengelola kepemilikan UTXO secara bersama-sama. Eltoo dirancang oleh Christian Decker, Rusty Russell, dan Olaoluwa Osuntokun, khususnya untuk menyelesaikan masalah yang terkait dengan mekanisme negosiasi status saluran Lightning, yaitu pembukaan dan penutupan. Arsitektur Eltoo menyederhanakan proses negosiasi dengan memperkenalkan sistem manajemen _state_ linier, menggantikan pendekatan berbasis penalti yang sudah ada dengan metode pembaruan yang lebih fleksibel dan tidak terlalu menghukum. Protokol ini membutuhkan penggunaan jenis _SigHash_ baru yang memungkinkan untuk mengabaikan semua input dalam tanda tangan transaksi. _SigHash_ ini pada awalnya disebut `SIGHASH_NOINPUT`, kemudian `SIGHASH_ANYPREVOUT` (*Any Previous Output*). Implementasinya direncanakan dalam BIP118.

> ► *Eltoo kadang-kadang juga disebut sebagai "LN-Symmetry".*
